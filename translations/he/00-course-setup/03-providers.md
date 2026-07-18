# בחירה והגדרת ספק LLM 🔑

ניתן גם להגדיר תרגילים שיפעלו מול פריסות מודל שפה גדול (LLM) דרך ספק שירות נתמך כדוגמת OpenAI, Azure או Hugging Face. אלו מספקים _נקודת גישה מנוהלת_ (API) אליה נוכל לגשת באופן תכנותי עם אישורים מתאימים (מפתח API או טוקן). בקורס זה, נדון בספקים הבאים:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) עם דגמים מגוונים כולל סדרת GPT המרכזית.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) עבור דגמי OpenAI, תוך דגש על מוכנות עסקית
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) עבור נקודת גישה אחת ומפתח API לגישה למאות דגמים מ-OpenAI, Meta, Mistral, Cohere, מייקרוסופט ועוד (מחליף את GitHub Models, שיפסיק לפעול בסוף יולי 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) עבור דגמים מקור פתוח ושרת הסקה
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) או [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) אם אתם מעדיפים להריץ דגמים באופן מלא במכשירכם, ללא צורך במנוי ענן

**תצטרכו להשתמש בחשבונות האישיים שלכם עבור התרגילים האלה**. התרגילים הם אופציונליים ואתם יכולים לבחור להגדיר אחד, כולם - או אף אחד - מהספקים בהתאם לתחומי העניין שלכם. כמה הנחיות להרשמה:

| הרשמה | מחיר | מפתח API | מגרש משחקים | הערות |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [תמחור](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [מבוסס פרויקט](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ללא קוד, אינטרנט](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | דגמים רבים זמינים |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [תמחור](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [התחלת עבודה עם SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [התחלת עבודה בסטודיו](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [יש להגיש בקשה מראש לקבלת גישה](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [תמחור](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [דף סקירת הפרויקט](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | שכבת חינם זמינה; נקודת גישה אחת + מפתח למספר ספקי דגמים |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [תמחור](https://huggingface.co/pricing) | [טוקני גישה](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [ל-Hugging Chat יש דגמים מוגבלים](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | חינם (רצים במכשירך) | לא נדרש | [Local CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | נקודת גישה תואמת OpenAI במצב אופליין מלא |
| | | | | |

עקבו אחר ההוראות מטה כדי _להגדיר_ מאגר זה לשימוש עם ספקים שונים. תרגילים שדורשים ספק מסוים יכילו אחת התגיות האלה בשם הקובץ שלהם:

- `aoai` - דורש נקודת גישה ומפתח Azure OpenAI
- `oai` - דורש נקודת גישה ומפתח OpenAI
- `hf` - דורש טוקן Hugging Face
- `githubmodels` - דורש נקודת גישה ומפתח Microsoft Foundry Models (GitHub Models יופסק בסוף יולי 2026)

אתם יכולים להגדיר אחד, אף אחד או את כל הספקים. תרגילים הקשורים לזה ייכשלו אם אישורי הגישה חסרים.

## יצירת קובץ `.env`

הנחה שנקראת כבר ההנחיה לעיל ונרשמתם עם הספק הרלוונטי, וקיבלתם את אישורי האימות הנדרשים (API_KEY או טוקן). במקרה של Azure OpenAI, הנחה שיש לכם גם פריסה תקפה של שירות Azure OpenAI (נקודת גישה) עם לפחות דגם GPT פרוס לשיחה.

השלב הבא הוא להגדיר את **משתני הסביבה המקומיים** כך:

1. חפשו בתיקיית השורש קובץ `.env.copy` שצריך להכיל תוכן כמו זה:

   ```bash
   # ספק OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI ב- Microsoft Foundry
   ## (שירות Azure OpenAI הוא כעת חלק מ- Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ברירת המחדל הוגדרה! (גרסת API יציבה נוכחית)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## דגמי Microsoft Foundry (קטלוג דגמים מרובי ספקים, מחליף את דגמי GitHub, שייפסק בסוף יולי 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. העתיקו את הקובץ ל-`.env` באמצעות הפקודה למטה. קובץ זה כלול ב-_gitignore_, לשמירת סודיות.

   ```bash
   cp .env.copy .env
   ```

3. מלאו את הערכים (החליפו את הממוינים בצד ימין של `=`) כפי שמתואר בסעיף הבא.

4. (אופציונלי) אם אתם משתמשים ב-GitHub Codespaces, יש לכם אפשרות לשמור משתני סביבה כסודות _Codespaces_ המקושרים למאגר זה. במקרה כזה, אינכם צריכים להגדיר קובץ .env מקומי. **עם זאת, אפשרות זו פועלת רק אם אתם משתמשים ב-GitHub Codespaces.** עדיין תצטרכו להגדיר את קובץ .env אם אתם משתמשים ב-Docker Desktop במקום.

## מילוי קובץ `.env`

בואו נסקור בקצרה את שמות המשתנים להבנת משמעותם:

| משתנה | תיאור |
| :--- | :--- |
| HUGGING_FACE_API_KEY | זהו טוקן גישת המשתמש שהגדרת בפרופיל שלך |
| OPENAI_API_KEY | זהו מפתח האישור לשימוש בשירות עבור נקודות גישה שאינן Azure OpenAI |
| AZURE_OPENAI_API_KEY | זהו מפתח האישור לשימוש בשירות הזה |
| AZURE_OPENAI_ENDPOINT | זוהי נקודת הגישה שהופעלה למשאב Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | זוהי נקודת גישה לפריסת מודל _יצירת טקסט_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | זוהי נקודת גישה לפריסת מודל _אימבדינגטקסט_ |
| AZURE_INFERENCE_ENDPOINT | זוהי נקודת הגישה לפרויקט Microsoft Foundry שלך, המשמשת עבור Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | זהו מפתח ה-API לפרויקט Microsoft Foundry שלך |
| | |

הערה: שני המשתנים האחרונים של Azure OpenAI משקפים מודל ברירת מחדל להשלמת שיחה (יצירת טקסט) ולחיפוש וקטורי (אימבדינגס) בהתאמה. ההוראות להגדרתם יופיעו בתרגילים הרלוונטיים.

## הגדרת Azure OpenAI: מפורטל

> **הערה:** שירות Azure OpenAI הוא עכשיו חלק מ-[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). המשאבים והפריסות עדיין מוצגים בפורטל Azure, אך ניהול מודלים יומיומי (פריסות, מגרש משחקים, ניטור) מתבצע כעת בפורטל Foundry במקום "Azure OpenAI Studio" הישן העצמאי.

ערכי נקודת הגישה והמפתח של Azure OpenAI יימצאו ב-[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), אז נתחיל שם.

1. כנסו ל-[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. לחצו על אפשרות **Keys and Endpoint** בסרגל הצד (תפריט שמאלי).
1. לחצו על **Show Keys** - אמור להופיע הבא: KEY 1, KEY 2 ו-Endpoint.
1. השתמשו בערך KEY 1 עבור AZURE_OPENAI_API_KEY
1. השתמשו בערך Endpoint עבור AZURE_OPENAI_ENDPOINT

עכשיו, אנו זקוקים לנקודות הגעה עבור הדגמים הספציפיים שהפעלנו.

1. לחצו על אפשרות **Model deployments** בסרגל הצד (תפריט שמאלי) עבור משאב Azure OpenAI.
1. בדף היעד, לחצו על **Go to Microsoft Foundry portal** (או **Manage Deployments**, תלוי בסוג המשאב שלכם)

זה יקח אתכם לפורטל Microsoft Foundry, שם נמצא את הערכים הנוספים כפי שמתואר מטה.

## הגדרת Azure OpenAI: מפורטל Microsoft Foundry

1. נווטו ל[פורטל Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **מהמשאב שלכם** כמו שתואר למעלה.
1. לחצו על לשונית **Deployments** (סרגל צד, שמאל) לצפייה בדגמים המופעלים כרגע.
1. אם המודל הרצוי לכם לא פרוס, השתמשו ב**Deploy model** כדי לפרוס אותו מתוך [קטלוג הדגמים](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. תזדקקו למודל _יצירת טקסט_ - מומלץ: **gpt-5-mini**
1. תזדקקו למודל _אימבדינג טקסט_ - מומלץ **text-embedding-3-small**

עכשיו עדכנו את משתני הסביבה לשקף את שם הפריסה (_Deployment name_) שהשתמשתם בו. בדרך כלל זה יהיה זהה לשם המודל אלא אם שיניתם מפורשות. לדוגמה, ייתכן שיהיה לכם:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**אל תשכחו לשמור את קובץ ה-.env בתום השינויים**. כעת תוכלו לצאת מהקובץ ולחזור להוראות להרצת פנקס התיעוד.

## הגדרת OpenAI: מפרופיל

מפתח ה-API של OpenAI נמצא ב[חשבון OpenAI שלך](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). אם אין לך מפתח, תוכל להירשם וליצור מפתח API חדש. לאחר שתקבל את המפתח, יש להשתמש בו כדי למלא את המשתנה `OPENAI_API_KEY` בקובץ `.env`.

## הגדרת Hugging Face: מפרופיל

טוקן Hugging Face שלך נמצא בפרופיל תחת [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). אל תפרסם או תשתף את הטוקנים האלה בפומבי. במקום זאת, צור טוקן חדש לשימוש בפרויקט זה והעתק אותו לתוך קובץ `.env` תחת המשתנה `HUGGING_FACE_API_KEY`. _הערה:_ זה טכנית לא מפתח API אך משמש לאימות, ולכן שומרים על שם זה למטרת עקביות.

## הגדרת Microsoft Foundry Models: מהפורטל

> **הערה:** GitHub Models ייסגר בסוף יולי 2026. Microsoft Foundry Models הוא התחליף הישיר, ומציע את אותו קטלוג הדגמים להיסיון חופשי וחווית SDK להסקה של Azure AI / OpenAI.

1. כנסו ל-[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) וצור (או פתח) פרויקט Foundry.
1. דפדפו ב[קטלוג הדגמים](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ופרוס מודל, למשל `gpt-5-mini`.
1. בעמוד **סקירת הפרויקט**, העתיקו את **נקודת הגישה** ואת **מפתח ה-API**.
1. השתמשו בערך נקודת הגישה עבור `AZURE_INFERENCE_ENDPOINT` ובערך המפתח עבור `AZURE_INFERENCE_CREDENTIAL` בקובץ `.env`.

## ספקים אופליין / מקומיים

אם אתם מעדיפים לא להשתמש במנוי ענן כלל, ניתן להריץ דגמים פתוחים תואמים ישירות במכשירכם:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - ריצת זמן של מייקרוסופט במכשיר. בוחרת אוטומטית את ספק הביצוע הטוב ביותר (NPU, GPU, או CPU) וחשופה נקודת גישה תואמת OpenAI, כך שתוכלו להפעיל את רוב קוד הדוגמא בקורס זה עם מינימום שינויים. ראו את [התיעוד של Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) להתחלה, או התקינו עם `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - חלופה פופולרית להרצת דגמים פתוחים כמו Llama, Phi, Mistral ו-Gemma מקומית.


ראה [שיעור 19: בנייה עם SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) לדוגמאות מעשיות המשתמשות בשתי האפשרויות.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->