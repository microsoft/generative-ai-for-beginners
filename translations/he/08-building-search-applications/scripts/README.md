<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:52:25+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "he"
}
-->
# הכנת נתוני תמלול

סקריפטי הכנת נתוני התמלול מורידים תמלולים של סרטוני יוטיוב ומכינים אותם לשימוש עם החיפוש הסמנטי באמצעות OpenAI Embeddings ו-Functions.

סקריפטי הכנת נתוני התמלול נבדקו על הגרסאות האחרונות של Windows 11, macOS Ventura ו-Ubuntu 22.04 (ומעלה).

## יצירת משאבים נדרשים של Azure OpenAI Service

> [!IMPORTANT]
> אנו ממליצים לעדכן את Azure CLI לגרסה האחרונה כדי להבטיח תאימות עם OpenAI
> ראו [תיעוד](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. יצירת קבוצת משאבים

> [!NOTE]
> להוראות אלה אנו משתמשים בקבוצת המשאבים בשם "semantic-video-search" במזרח ארה"ב.
> ניתן לשנות את שם קבוצת המשאבים, אך בעת שינוי המיקום למשאבים,
> בדקו את [טבלת זמינות המודלים](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. יצירת משאב Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. קבלת נקודת הקצה והמפתחות לשימוש ביישום זה

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. פרסו את המודלים הבאים:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

```console
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name gpt-35-turbo \
    --model-name gpt-35-turbo \
    --model-version "0613"  \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## תוכנה נדרשת

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) או גרסה מתקדמת יותר

## משתני סביבה

המשתנים הבאים נדרשים להפעלת סקריפטי הכנת נתוני התמלול מיוטיוב.

### ב-Windows

מומלץ להוסיף את המשתנים ל-`user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### ב-Linux וב-macOS

מומלץ להוסיף את ההגדרות הבאות לקובץ `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## התקנת ספריות Python הנדרשות

1. התקנת [לקוח git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) אם הוא לא מותקן כבר.
1. מחלון `Terminal`, שיבטו את הדוגמה לתיקיית הריפו המועדפת עליכם.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. נווטו לתיקיית `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. יצירת סביבה וירטואלית של Python.

    ב-Windows:

    ```powershell
    python -m venv .venv
    ```

    ב-macOS ו-Linux:

    ```bash
    python3 -m venv .venv
    ```

1. הפעלת הסביבה הווירטואלית של Python.

   ב-Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   ב-macOS ו-Linux:

   ```bash
   source .venv/bin/activate
   ```

1. התקנת הספריות הנדרשות.

   ב-Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   ב-macOS ו-Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## הפעלת סקריפטי הכנת נתוני התמלול מיוטיוב

### ב-Windows

```powershell
.\transcripts_prepare.ps1
```

### ב-macOS ו-Linux

```bash
./transcripts_prepare.sh
```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל טעויות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לכל אי הבנות או פרשנויות שגויות הנובעות מהשימוש בתרגום זה.