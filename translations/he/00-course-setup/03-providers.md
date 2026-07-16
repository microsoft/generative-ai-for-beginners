# בחירת ספק LLM והגדרתו 🔑

משימות **יכולות** גם להיות מוגדרות לעבוד מול פריסות של מודל שפה גדול (LLM) דרך ספק שירות נתמך כמו OpenAI, Azure או Hugging Face. אלו מספקים _נקודת קצה מתארחת_ (API) שניתן לגשת אליה תכנותית עם האישורים הנכונים (מפתח API או טוקן). בקורס זה, נדון בספקים הבאים:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) עם מודלים מגוונים כולל סדרת GPT המרכזית.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) עבור מודלים של OpenAI עם מיקוד למוכנות ארגונית
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) עבור נקודת קצה אחת ומפתח API לגישה למאות מודלים מ-OpenAI, Meta, Mistral, Cohere, Microsoft ועוד (מחליף את GitHub Models, שייפסק בסוף יולי 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) עבור מודלים בקוד פתוח ושרת אינפרנסים
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) או [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) אם אתם מעדיפים להריץ מודלים במלואם ללא חיבור לאינטרנט במכשיר שלכם, ללא צורך במנוי ענן

**תזדקקו לחשבונות שלכם עבור התרגילים האלה**. המשימות הן אופציונליות כך שתוכלו לבחור להגדיר אחד, את כולם - או אף אחד - מהספקים על פי תחומי העניין שלכם. כמה הנחיות להרשמה:

| הרשמה | עלות | מפתח API | פלטפורמת משחק | הערות |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [תמחור](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [מבוסס פרויקטים](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ללא קוד, רשת](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | מודלים מרובים זמינים |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [תמחור](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [התחלה מהירה ב-SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [התחלה מהירה בסטודיו](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [חובה להגיש בקשה מראש לקבלת גישה](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [תמחור](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [דף סקירת פרויקט](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [פלטפורמת Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | יש שכבת חינם; נקודת קצה אחת + מפתח בשביל ספקי מודלים רבים |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [תמחור](https://huggingface.co/pricing) | [טוקני גישה](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [ל-Hugging Chat יש מודלים מוגבלים](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | חינם (רץ על המכשיר שלך) | לא נדרש | [CLI/SDK מקומי](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | נקודת קצה תואמת OpenAI במצב לא מקוון מלא |
| | | | | |

עקבו אחר ההוראות למטה כדי _לקנפג_ את המאגר הזה לשימוש עם ספקים שונים. משימות שדורשות ספק ספציפי יכללו אחת התגים האלה בשם הקובץ שלהן:

- `aoai` - דורש נקודת קצה ומפתח Azure OpenAI
- `oai` - דורש נקודת קצה ומפתח OpenAI
- `hf` - דורש טוקן Hugging Face
- `githubmodels` - דורש נקודת קצה ומפתח Microsoft Foundry Models (GitHub Models ייסגר בסוף יולי 2026)

ניתן להגדיר אחד, אף אחד או את כל הספקים. משימות קשורות פשוט יציגו שגיאה אם האישורים חסרים.

## צור קובץ `.env`

מניחים שכבר קראת את ההנחיות לעיל, נרשמת לספק הרלוונטי, וקיבלת את האישורים הדרושים לאימות (API_KEY או טוקן). במקרה של Azure OpenAI, מניחים שגם יש לך פריסת שירות Azure OpenAI תקפה (נקודת קצה) עם לפחות מודל GPT אחד פרוס לסיום שיחה.

השלב הבא הוא להגדיר את **משתני הסביבה המקומיים** שלך כך:

1. חפש בתיקיית השורש קובץ `.env.copy` שלרוב יכיל תוכן כזה:

   ```bash
   # ספק OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI ב־Microsoft Foundry
   ## (שירות Azure OpenAI הוא עכשיו חלק מ־Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ברירת המחדל נקבעה! (גרסת ה-API היציבה הנוכחית)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## דגמי Microsoft Foundry (קטלוג דגמים רב-ספקי, מחליף את דגמי GitHub, שיפסיקו בסוף יולי 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. העתק את הקובץ הזה ל-`.env` באמצעות הפקודה למטה. קובץ זה מופעל ב-.gitignore ושומר על סודות בטוחים.

   ```bash
   cp .env.copy .env
   ```

3. מלא את הערכים (החלף את המקומות המוחזקים מצד ימין של `=`) כפי שמתואר בסעיף הבא.

4. (אופציה) אם אתם משתמשים ב-GitHub Codespaces, יש לכם אפשרות לשמור משתני סביבה כ_סודות Codespaces_ המשויכים למאגר זה. במקרה כזה, לא תצטרכו להגדיר קובץ .env מקומי. **עם זאת, שימו לב שאפשרות זו פועלת רק אם אתם משתמשים ב-GitHub Codespaces.** תצטרכו עדיין להגדיר את קובץ ה-.env אם אתם משתמשים ב-Docker Desktop.

## מלא את קובץ `.env`

בואו נבחן במהירות את שמות המשתנים כדי להבין למה הם מתייחסים:

| משתנה  | תיאור  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | זהו טוקן גישת המשתמש שהגבת בפרופיל שלך |
| OPENAI_API_KEY | זהו מפתח האישור לשימוש בשירות עבור נקודות קצה שאינן Azure OpenAI |
| AZURE_OPENAI_API_KEY | זהו מפתח האישור לשירות זה |
| AZURE_OPENAI_ENDPOINT | זו נקודת הקצה שהופעלה עבור משאב Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | זו נקודת הקצה של מודל _יצירת טקסט_ שפורס |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | זו נקודת הקצה של מודל _הטמעת טקסט_ שפורס |
| AZURE_INFERENCE_ENDPOINT | זו נקודת הקצה עבור פרויקט Microsoft Foundry שלך, משמשת עבור Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | זהו מפתח ה-API עבור פרויקט Microsoft Foundry שלך |
| | |

הערה: שני המשתנים האחרונים של Azure OpenAI מייצגים מודל ברירת מחדל לסיום שיחה (יצירת טקסט) וחיפוש וקטורי (הטמעות) בהתאמה. הוראות להגדיר אותם יינתנו במשימות רלוונטיות.

## הגדר Azure OpenAI: מהפורטל

> **הערה:** שירות Azure OpenAI הוא כעת חלק מ-[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). משאבים ופריסות עדיין מוצגים בפורטל Azure, אבל ניהול המודלים היומיומי (פריסות, פלטפורמה, ניטור) נעשה כעת בפורטל Foundry במקום סטודיו עצמאי ישן של "Azure OpenAI".

ערכי נקודת הקצה ומפתח Azure OpenAI יימצאו ב-[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), אז בואו נתחיל שם.

1. עבור ל-[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. לחץ על האופציה **Keys and Endpoint** בתפריט הצדדי (תפריט משמאל).
1. לחץ על **Show Keys** - תראה את הפריטים הבאים: KEY 1, KEY 2 ו-Endpoint.
1. השתמש בערך KEY 1 עבור AZURE_OPENAI_API_KEY
1. השתמש בערך Endpoint עבור AZURE_OPENAI_ENDPOINT

לאחר מכן, נדרש לקבל את נקודות הקצה עבור המודלים הספציפיים שפרסת.

1. לחץ על האופציה **Model deployments** בתפריט הצדדי (תפריט משמאל) עבור משאב Azure OpenAI.
1. בעמוד הייעודי, לחץ על **Go to Microsoft Foundry portal** (או **Manage Deployments**, תלוי בסוג המשאב שלך)

זה יוביל אותך לפורטל Microsoft Foundry, שם נמצא את הערכים האחרים כמפורט מטה.

## הגדר Azure OpenAI: מתוך פורטל Microsoft Foundry

1. ניווט ל-[פורטל Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **מהמשאב שלך** כפי שתואר למעלה.
1. לחץ על לשונית **Deployments** (תפריט צד, שמאל) כדי לצפות במודלים שפורסו כרגע.
1. אם המודל הרצוי אינו פרוס, השתמש ב-**Deploy model** לפרוס אותו מ-[קטלוג המודלים](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. תזדקק למודל _יצירת טקסט_ - אנו ממליצים על: **gpt-4o-mini**
1. תזדקק למודל _הטמעת טקסט_ - אנו ממליצים על **text-embedding-3-small**

עכשיו עדכן את משתני הסביבה לשקף את שם ה_פריסה_ ששימש. בדרך כלל זה יהיה אותו שם כמו שם המודל אלא אם שינית אותו במפורש. לדוגמה, ייתכן שתרצה:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**אל תשכח לשמור את קובץ ה-.env לאחר הסיום**. כעת תוכל לצאת מהקובץ ולחזור להוראות להרצת המחברת.

## הגדר OpenAI: מתוך הפרופיל

מפתח ה-API של OpenAI שלך נמצא ב-[חשבון OpenAI שלך](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). אם אין לך אחד, תוכל להירשם וליצור מפתח API. לאחר שיש לך את המפתח, תוכל למלא את המשתנה `OPENAI_API_KEY` בקובץ `.env`.

## הגדר Hugging Face: מתוך הפרופיל

הטוקן של Hugging Face נמצא בפרופיל שלך תחת [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). אל תפרסם או שתף אותם בפומבי. במקום זאת, צור טוקן חדש לשימוש בפרויקט זה והעתק אותו לקובץ `.env` תחת המשתנה `HUGGING_FACE_API_KEY`. _הערה:_ טכנית זה לא מפתח API אלא משמש לאימות ולכן אנחנו שומרים על השם הזה למען עקביות.

## הגדר Microsoft Foundry Models: מתוך פורטל

> **הערה:** GitHub Models ייסגר בסוף יולי 2026. Microsoft Foundry Models הוא התחליף הישיר, ומציע אותו קטלוג מודלים חינמי לנסות וניסיון SDK של Azure AI Inference / OpenAI.

1. עבור ל-[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ויצר (או פתח) פרויקט Foundry.
1. דפדף ב-[קטלוג המודלים](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ופרוס מודל, לדוגמה `gpt-4o-mini`.
1. בעמוד ה**סקירה** של הפרויקט, העתק את **נקודת הקצה** ו**מפתח ה-API**.
1. השתמש בערך נקודת הקצה ל-`AZURE_INFERENCE_ENDPOINT` ובערך המפתח ל-`AZURE_INFERENCE_CREDENTIAL` בקובץ `.env` שלך.

## ספקים לא מקוונים / מקומיים

אם אתה מעדיף לא להשתמש במנוי ענן בכלל, ניתן להריץ מודלים פתוחים תואמים ישירות במכשיר שלך:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - סביבת הריצה של מיקרוסופט במכשיר. היא בוחרת אוטומטית את ספק הביצוע הטוב ביותר (NPU, GPU או CPU) וחשופה נקודת קצה תואמת OpenAI, כך שתוכל להשתמש ברוב קוד הדוגמה בקורס זה עם מינימום שינויים. צפה ב-[תיעוד Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) כדי להתחיל, או התקן עם `winget install Microsoft.FoundryLocal` (ווינדוס) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - אלטרנטיבה פופולרית להרצת מודלים פתוחים כמו Llama, Phi, Mistral ו-Gemma באופן מקומי.


ראה [שיעור 19: בנייה עם SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) לדוגמאות מעשיות המשתמשות בשתי האפשרויות.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->