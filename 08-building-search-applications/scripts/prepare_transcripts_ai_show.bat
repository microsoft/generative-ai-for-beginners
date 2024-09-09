@echo off

REM This script will process the transcripts
REM 1. Download the transcripts from YouTube
REM 2. Enrich the transcripts with speaker information
REM 3. Enrich the transcripts into 3 minute buckets
REM 4. Enrich the transcripts with OpenAI ChatGPT summaries
REM 5. Enrich the transcripts with embeddings
REM 6. Enrich the transcripts with lite embeddings - removes the text property

set TRANSCRIPT_FOLDER=transcripts_the_ai_show
set TRANSCRIPT_BUCKET_MINUTES=3

if not exist %TRANSCRIPT_FOLDER%\output (
    mkdir %TRANSCRIPT_FOLDER%\output
)

python transcript_download.py -f %TRANSCRIPT_FOLDER% -p PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1

python transcript_enrich_speaker.py -f %TRANSCRIPT_FOLDER%
python transcript_enrich_bucket.py -f %TRANSCRIPT_FOLDER% -m %TRANSCRIPT_BUCKET_MINUTES%
python transcript_enrich_summaries.py -f %TRANSCRIPT_FOLDER%
python transcript_enrich_embeddings.py -f %TRANSCRIPT_FOLDER%
python transcript_enrich_lite.py -f %TRANSCRIPT_FOLDER%

REM Check if master_enriched.json file exists then rename it to include segment minutes
if exist "%TRANSCRIPT_FOLDER%\output\master_enriched.json" (
    move "%TRANSCRIPT_FOLDER%\output\master_enriched.json" "%TRANSCRIPT_FOLDER%\output\embedding_index_full_%TRANSCRIPT_BUCKET_MINUTES%m.json"
)

REM Check if master_enriched_lite.json file exists then rename it to include segment minutes
if exist "%TRANSCRIPT_FOLDER%\output\master_enriched_lite.json" (
    move "%TRANSCRIPT_FOLDER%\output\master_enriched_lite.json" "%TRANSCRIPT_FOLDER%\output\embedding_index_%TRANSCRIPT_BUCKET_MINUTES%m.json"
)