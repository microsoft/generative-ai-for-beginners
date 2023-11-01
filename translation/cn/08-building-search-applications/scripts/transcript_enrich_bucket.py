""" This script generates a master csv file from the transcript files."""

# from the transcript files, generate a master csv file
# from the transcript folder read all the .json files then load the associated .vtt file

from datetime import datetime, timedelta
import glob
import os
import json
import argparse
import tiktoken
import logging
from rich.progress import Progress

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


SEGMENT_LENGTH_MINUTES = 5
PERCENTAGE_OVERLAP = 0.05
TRANSCRIPT_FOLDER = "transcripts"
MAX_TOKENS = 2048

segments = []
total_files = 0

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder")
parser.add_argument("-m", "--minutes")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()
if args.verbose:
    logger.setLevel(logging.DEBUG)

TRANSCRIPT_FOLDER = args.folder if args.folder else None
SEGMENT_LENGTH_MINUTES = int(args.minutes) if args.minutes else SEGMENT_LENGTH_MINUTES

if not TRANSCRIPT_FOLDER:
    logger.error("Transcript folder not provided")
    exit(1)

# https://stackoverflow.com/questions/75804599/openai-api-how-do-i-count-tokens-before-i-send-an-api-request
ENCODING_MODEL = "gpt-3.5-turbo"
tokenizer = tiktoken.encoding_for_model(ENCODING_MODEL)


class VttSegment:
    def __init__(self, segment: dict[str, str | float]) -> None:
        self.text = segment.get("text")
        self.start = segment.get("start")
        self.duration = segment.get("duration")

    text: str
    start: float
    duration: float


def gen_metadata_master(metadata):
    """generate the metadata master csv file"""
    text = metadata["title"] + " " + metadata["description"]
    metadata["start"] = "00:00:00"

    text = text.strip()

    if text == "" or text is None:
        metadata["text"] = "No description available."
    else:
        # clean the text
        text = text.replace("\n", "")
        metadata["text"] = text.strip()


def clean_text(text):
    """clean the text"""
    text = text.replace("\n", " ")  # remove new lines
    text = text.replace("&#39;", "'")
    text = text.replace(">>", "")  # remove '>>'
    text = text.replace("  ", " ")  # remove double spaces
    text = text.replace("[inaudible]", "")  # [inaudible]

    return text


def append_text_to_previous_segment(text):
    """
    append PERCENTAGE_OVERLAP text to the previous segment to smooth context transition
    """
    if len(segments) > 0:
        words = text.split(" ")
        word_count = len(words)
        if word_count > 0:
            append_text = " ".join(words[0 : int(word_count * PERCENTAGE_OVERLAP)])
            segments[-1]["text"] += append_text


def add_new_segment(metadata, text, segment_begin_seconds):
    """add a new segment to the segments list"""
    # convert the segment_begin_time float to 00:00:00 formatted string
    delta = timedelta(seconds=segment_begin_seconds)
    begin_time = datetime.min + delta
    metadata["start"] = begin_time.strftime("%H:%M:%S")
    metadata["seconds"] = segment_begin_seconds

    metadata["text"] = text
    segments.append(metadata.copy())


def parse_json_vtt_transcript(vtt, metadata):
    """parse the json vtt file and return the transcript"""
    text = ""
    current_seconds = None
    seg_begin_seconds = None
    seg_finish_seconds = None
    current_token_length = 0
    first_segment = True

    # add the speaker name to the transcript
    if "speaker" in metadata and metadata["speaker"] != "":
        metadata["speaker"] = clean_text(metadata.get("speaker"))
        text = "The speaker's name is " + metadata["speaker"] + ". "

    # add the title to the transcript
    if "title" in metadata and metadata["title"] != "":
        metadata["title"] = clean_text(metadata.get("title"))
        text += metadata.get("title") + ". "

    # add the description to the transcript
    if "description" in metadata and metadata["description"] != "":
        metadata["description"] = clean_text(metadata.get("description"))
        text += metadata.get("description") + ". "

    current_token_length = len(tokenizer.encode(text))

    # open the vtt file
    with open(vtt, "r", encoding="utf-8") as json_file:
        json_vtt = json.load(json_file)

        for segment in json_vtt:
            seg = VttSegment(segment)
            current_seconds = int(seg.start)
            current_text = seg.text

            if seg_begin_seconds is None:
                seg_begin_seconds = current_seconds
                # calculate the finish time from the segment_begin_time
                seg_finish_seconds = seg_begin_seconds + SEGMENT_LENGTH_MINUTES * 60

            # Get the number of tokens in the text.
            # Need to calc to allow for 1024 tokens for 
            # summary request in next pipeline step
            total_tokens = len(tokenizer.encode(current_text)) + current_token_length

            if current_seconds < seg_finish_seconds and total_tokens < MAX_TOKENS:
                # add the text to the transcript
                text += current_text + " "
                current_token_length = total_tokens
            else:
                if not first_segment:
                    # append PERCENTAGE_OVERLAP text to the previous segment
                    # to smooth context transition
                    append_text_to_previous_segment(text)
                first_segment = False
                add_new_segment(metadata, text, seg_begin_seconds)

                text = current_text + " "

                # reset the segment_begin_time
                seg_begin_seconds = None
                seg_finish_seconds = None

                current_token_length = len(tokenizer.encode(text))

        # Append the last text segment to the last segment in segments dictionary
        if seg_begin_seconds and text != "":
            previous_segment_tokens = len(tokenizer.encode(segments[-1]["text"]))
            current_segment_tokens = len(tokenizer.encode(text))

            if previous_segment_tokens + current_segment_tokens < MAX_TOKENS:
                segments[-1]["text"] += text
            else:
                if not first_segment:
                    # append PERCENTAGE_OVERLAP text to the previous segment
                    # to smooth context transition
                    append_text_to_previous_segment(text)
                first_segment = False
                add_new_segment(metadata, text, seg_begin_seconds)


def get_transcript(metadata):
    """get the transcript from the .vtt file"""
    global total_files
    vtt = os.path.join(TRANSCRIPT_FOLDER, metadata["videoId"] + ".json.vtt")

    # check that the .vtt file exists
    if not os.path.exists(vtt):
        logger.info("vtt file does not exist: %s", vtt)
        return None
    else:
        logger.debug("Processing file: %s", vtt)
        total_files += 1

    parse_json_vtt_transcript(vtt, metadata)


logger.debug("Transcription folder: %s", TRANSCRIPT_FOLDER)
logger.debug("Segment length %d minutes", SEGMENT_LENGTH_MINUTES)

folder = os.path.join(TRANSCRIPT_FOLDER, "*.json")

with Progress() as progress:
    task1 = progress.add_task("[green]Enriching Buckets...", total=total_files)

    for file in glob.glob(folder):
        # load the json file
        meta = json.load(open(file, encoding="utf-8"))

        get_transcript(meta)
        progress.update(task1, advance=1)


logger.debug("Total files: %s", total_files)
logger.debug("Total segments: %s", len(segments))

# save segments to a json file

output_file = os.path.join(TRANSCRIPT_FOLDER, "output", "master_transcriptions.json")
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(segments, f, ensure_ascii=False, indent=4)
