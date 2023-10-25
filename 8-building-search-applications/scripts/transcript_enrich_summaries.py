""" Summarize a youtube transcript using chatgpt"""

import json
import os
import queue
import threading
import logging
import argparse
import openai
from tenacity import (
    retry,
    wait_random_exponential,
    stop_after_attempt,
    retry_if_not_exception_type,
)
from rich.progress import Progress

API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
RESOURCE_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = os.getenv(
    "AZURE_OPENAI_MODEL_DEPLOYMENT_NAME", "gpt-35-turbo"
)
MAX_TOKENS = 512
PROCESSOR_THREADS = 10
OPENAI_REQUEST_TIMEOUT = 30

openai.api_type = "azure"
openai.api_key = API_KEY
openai.api_base = RESOURCE_ENDPOINT
openai.api_version = "2023-07-01-preview"

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", action="store_true")
parser.add_argument("-f", "--folder")
args = parser.parse_args()

TRANSCRIPT_FOLDER = args.folder if args.folder else None
if not TRANSCRIPT_FOLDER:
    logger.error("Transcript folder not provided")
    exit(1)

if args.verbose:
    logger.setLevel(logging.DEBUG)

segments = []
output_segments = []
total_segments = 0

errors = 0


class Counter:
    """thread safe counter"""

    def __init__(self):
        """initialize the counter"""
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        """increment the counter"""
        with self.lock:
            self.value += 1
            return self.value


counter = Counter()


@retry(
    wait=wait_random_exponential(min=10, max=45),
    stop=stop_after_attempt(20),
    retry=retry_if_not_exception_type(openai.InvalidRequestError),
)
def chatgpt_summary(text):
    """generate a summary using chatgpt"""

    messages = [
        {
            "role": "system",
            "content": "You're an AI Assistant for video, write an authoritative 60 word summary.Avoid starting sentences with 'This video'.",
        },
        {"role": "user", "content": text},
    ]

    response = openai.ChatCompletion.create(
        engine=AZURE_OPENAI_MODEL_DEPLOYMENT_NAME,
        messages=messages,
        temperature=0.7,
        max_tokens=MAX_TOKENS,
        top_p=0.0,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        request_timeout=OPENAI_REQUEST_TIMEOUT,
    )

    # print(response)

    text = response.get("choices", [])[0].get("message", {}).get("content", text)
    finish_reason = response.get("choices", [])[0].get("finish_reason", "")

    # print(finish_reason)
    if finish_reason != "stop":
        logger.warning("Stop reason: %s", finish_reason)
        logger.warning("Text: %s", text)
        logger.warning("Increase Max Tokens and try again")
        exit(1)

    return text


def process_queue(progress, task):
    """process the queue"""
    while not q.empty():
        if errors > 100:
            logger.exit("Too many errors. Exiting...")
            exit(1)

        segment = q.get()

        text = segment.get("text")

        # Think about this some more. Idea is to reduce processing time
        # text_hash = hash(text)

        # # check if there is a summary already in the segment and the hash is the same
        # # If found then don't generate a new summary
        # if "summary" in segment and "text_hash" in segment and text_hash == segment["text_hash"]:
        #     output_segments.append(segment.copy())
        #     q.task_done()
        #     continue

        # get a summary of the text using chatgpt
        try:
            summary = chatgpt_summary(text)
        except openai.InvalidRequestError as invalid_request_error:
            logger.warning("Error: %s", invalid_request_error)
            summary = text
        except Exception as e:
            logger.warning("Error: %s", e)
            summary = text

        count = counter.increment()
        progress.update(task, advance=1)
        logger.debug("Processed %d segments of %d", count, total_segments)

        # add the summary and text hash to the segment dictionary
        segment["summary"] = summary

        output_segments.append(segment.copy())
        q.task_done()


logger.debug("Starting OpenAI summarization")

# load the segments from a json file
input_file = os.path.join(TRANSCRIPT_FOLDER, "output", "master_transcriptions.json")
with open(input_file, "r", encoding="utf-8") as f:
    segments = json.load(f)

total_segments = len(segments)

logger.debug("Total segments to be processed: %s", len(segments))

# add segment list to a queue
q = queue.Queue()
for segment in segments:
    q.put(segment)

with Progress() as progress:
    task1 = progress.add_task("[purple]Enriching Summaries...", total=total_segments)

    # create multiple threads to process the queue
    threads = []
    for i in range(PROCESSOR_THREADS):
        t = threading.Thread(target=process_queue, args=(progress, task1))
        t.start()
        threads.append(t)

    # wait for all threads to finish
    for t in threads:
        t.join()


# convert time '00:01:20' to seconds
def convert_time_to_seconds(value):
    """convert time to seconds"""
    time_value = value.split(":")
    if len(time_value) == 3:
        h, m, s = time_value
        return int(h) * 3600 + int(m) * 60 + int(s)
    else:
        return 0


# sort the output segments by videoId and start
output_segments.sort(key=lambda x: (x["videoId"], convert_time_to_seconds(x["start"])))

logger.debug("Total segments processed: %s", len(output_segments))

# save the output segments to a json file
output_file = os.path.join(TRANSCRIPT_FOLDER, "output", "master_enriched.json")
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output_segments, f, ensure_ascii=False, indent=4)
