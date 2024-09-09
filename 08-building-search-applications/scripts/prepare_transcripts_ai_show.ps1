# This script will process the transcripts
# 1. Download the transcripts from YouTube
# 2. Enrich the transcripts with speaker information
# 3. Enrich the transcripts into 3 minute buckets
# 4. Enrich the transcripts with OpenAI ChatGPT summaries
# 5. Enrich the transcripts with embeddings
# 6. Enrich the transcripts with lite embeddings - removes the text property

$TRANSCRIPT_FOLDER = "transcripts_the_ai_show"
$TRANSCRIPT_BUCKET_MINUTES = 3

# Create output directory if it doesn't exist
if (-Not (Test-Path "$TRANSCRIPT_FOLDER\output")) {
    New-Item -ItemType Directory -Path "$TRANSCRIPT_FOLDER\output"
}

# Run the Python scripts
python transcript_download.py -f $TRANSCRIPT_FOLDER -p "PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1"

python transcript_enrich_speaker.py -f $TRANSCRIPT_FOLDER
python transcript_enrich_bucket.py -f $TRANSCRIPT_FOLDER -m $TRANSCRIPT_BUCKET_MINUTES
python transcript_enrich_summaries.py -f $TRANSCRIPT_FOLDER
python transcript_enrich_embeddings.py -f $TRANSCRIPT_FOLDER
python transcript_enrich_lite.py -f $TRANSCRIPT_FOLDER

# Check if master_enriched.json file exists then rename it to include segment minutes
if (Test-Path "$TRANSCRIPT_FOLDER\output\master_enriched.json") {
    Move-Item -Path "$TRANSCRIPT_FOLDER\output\master_enriched.json" -Destination "$TRANSCRIPT_FOLDER\output\embedding_index_full_${TRANSCRIPT_BUCKET_MINUTES}m.json" -Force
}

# Check if master_enriched_lite.json file exists then rename it to include segment minutes
if (Test-Path "$TRANSCRIPT_FOLDER\output\master_enriched_lite.json") {
    Move-Item -Path "$TRANSCRIPT_FOLDER\output\master_enriched_lite.json" -Destination "$TRANSCRIPT_FOLDER\output\embedding_index_${TRANSCRIPT_BUCKET_MINUTES}m.json" -Force
}
