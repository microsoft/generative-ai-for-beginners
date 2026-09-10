# הכנת נתוני תמלול

סקריפטים להכנת נתוני תמלול מורידים תמלולים של סרטוני YouTube ומכינים אותם לשימוש עם הדוגמה של חיפוש סמנטי עם OpenAI Embeddings ופונקציות.

סקריפטים להכנת נתוני תמלול נבדקו על הגרסאות האחרונות של Windows 11, macOS Ventura ו-Ubuntu 22.04 (ומעלה).

## יצירת משאבי Azure OpenAI Service הנדרשים

> [!IMPORTANT]
> אנו ממליצים לעדכן את Azure CLI לגרסה האחרונה כדי להבטיח תאימות עם OpenAI
> ראה [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. צור קבוצת משאבים

> [!NOTE]
> להוראות אלו אנו משתמשים בקבוצת המשאבים בשם "semantic-video-search" באזור East US.
> ניתן לשנות את שם קבוצת המשאבים, אך כאשר משנים את המיקום של המשאבים,
> בדוק את [טבלת זמינות הדגמים](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. צור משאב Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. קבל את נקודת הקצה והמפתחות לשימוש ביישום זה

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. פרוס את הדגמים הבאים:
   - `text-embedding-ada-002` גרסה `2` ומעלה, בשם `text-embedding-ada-002`
   - `gpt-5-mini` בשם `gpt-5-mini`

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
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## תוכנה נדרשת

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ומעלה

## משתני סביבה

משתני הסביבה הבאים נדרשים להרצת הסקריפטים להכנת נתוני התמלול של YouTube.

### ב-Windows

מומלץ להוסיף את המשתנים למשתני הסביבה של `user`.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` עבור [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- ניתן להוסיף את משתני הסביבה לפרופיל PowerShell שלך.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### בלינוקס וב-macOS

מומלץ להוסיף את הייצוא הבא לקובץ `~/.bashrc` או `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## התקנת הספריות הנדרשות בפייתון

1. התקן את [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) אם הוא לא מותקן כבר.
1. מחלון `Terminal`, שכפל את הדוגמה לתיקיית הריפו המועדפת עליך.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. עבור לתיקיית `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. צור סביבה וירטואלית לפייתון.

    ב-Windows:

    ```powershell
    python -m venv .venv
    ```

    ב-macOS ולינוקס:

    ```bash
    python3 -m venv .venv
    ```

1. הפעל את הסביבה הוירטואלית של פייתון.

   ב-Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   ב-macOS ולינוקס:

   ```bash
   source .venv/bin/activate
   ```

1. התקן את הספריות הנדרשות.

   ב-Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   ב-macOS ולינוקס:

   ```bash
   pip3 install -r requirements.txt
   ```

## הרצת סקריפטי הכנת נתוני התמלול של YouTube

### ב-Windows

```powershell
.\transcripts_prepare.ps1
```

### ב-macOS ולינוקס

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->