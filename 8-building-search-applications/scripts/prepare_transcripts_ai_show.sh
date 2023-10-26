#!/bin/bash

# This script will process the transcripts
# 1. Download the transcripts from YouTube
# 2. Enrich the transcripts with speaker information
# 3. Enrich the transcripts into 3 minute buckets
# 4. Enrich the transcripts with with OpenAI ChatGPT summaries
# 5. Enrich the transcripts with embeddings
# 6. Enrich the transcripts with lite embeddings - removes the text property


export TRANSCRIPT_FOLDER=transcripts_the_ai_show
export TRANSCRIPT_BUCKET_MINUTES=3

mkdir -p $TRANSCRIPT_FOLDER/output

python3 transcript_download.py -f $TRANSCRIPT_FOLDER -p PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1

python3 transcript_enrich_speaker.py -f $TRANSCRIPT_FOLDER
python3 transcript_enrich_bucket.py -f $TRANSCRIPT_FOLDER -m $TRANSCRIPT_BUCKET_MINUTES
python3 transcript_enrich_summaries.py -f $TRANSCRIPT_FOLDER
python3 transcript_enrich_embeddings.py -f $TRANSCRIPT_FOLDER
python3 transcript_enrich_lite.py -f $TRANSCRIPT_FOLDER

# bash test ./output/master_enriched.json file exists then rename it to include segment minutes
if [ -f "./$TRANSCRIPT_FOLDER/output/master_enriched.json" ]; then
    mv ./$TRANSCRIPT_FOLDER/output/master_enriched.json ./$TRANSCRIPT_FOLDER/output/embedding_index_full_${TRANSCRIPT_BUCKET_MINUTES}m.json
fi

# bash test ./output/master_enriched_lite.json file exists then rename it to include segment minutes
if [ -f "./$TRANSCRIPT_FOLDER/output/master_enriched_lite.json" ]; then
    mv ./$TRANSCRIPT_FOLDER/output/master_enriched_lite.json ./$TRANSCRIPT_FOLDER/output/embedding_index_${TRANSCRIPT_BUCKET_MINUTES}m.json
fi
