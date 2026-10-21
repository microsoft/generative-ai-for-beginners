# רישום שינויים

כל השינויים הבולטים בתכנית Generative AI for Beginners מתועדים בקובץ זה.

הפורמט מבוסס על [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). מאחר שמדובר בתכנית לימודים ולא בחבילת תוכנה עם גרסאות, הערכים מאורגנים לפי תאריך.


## [2026-07-16] — אימות תוכן + נכסי תמונה לשיעור 09

### שונה

- **שיעור 10 (אפליקציות AI עם קוד נמוך):** עדכון שני קישורים לפלטפורמת `docs.microsoft.com/powerapps/...` מותשת
  לקישורים העדכניים ב-`learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (אומתו חיים).
- **שיעור 17 (סוכני AI):** ייעול דוגמת מודל ישנה (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) ושם פריסת מיקום לדוגמת Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **שארית `README.md`:** נוסף מזהה מעקב חסר `?WT.mc_id=academic-105485-koreyst` לקישור
  *Microsoft for Startups*.
- **נכסי תמונות לשיעור 09** נשנו מחדש באמצעות מודל `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, ו-
  `images/startup.png` (זוג דוגמאות הקודם/אחר העריכה נוצר באמצעות שיחת `client.images.edit` אמיתית עם מסכת יצירה).




  נכונים לעכשיו; לא נדרשו שינויים.
  שמות וקישורים); אין צורך בשינויים.
- ביצע אימות מלא של markdown על כל 41 קבצי ה-markdown במאגר (למעט תרגומים) עבור
  נתיבי מסמכים מיושנים, `/en-us/` אזורי מיקרוסופט, שמות מוצר/דגם מיושנים, מזהי מעקב חסרים,
  וקישורים/תמונות יחסיים שבורים. רק הפער היחיד במזהה מעקב של *Microsoft for Startups* היה
  בר-ביצוע; כל שאר הדגלים אושרו כחיוביים שגויים (קישורי תרגום שנוצרו אוטומטית,
  מצייני מקום שהוסתרו בהערות, וכתובות URL מבניות של צד שלישי `/en/`).

## [2026-07-15] — שיעור 09 (יישומי תמונות) כתיבה מחדש עבור דגמי תמונות GPT

### שונה

- **שכתב את שיעור 09 "בניית יישומי יצירת תמונות"** סביב **`gpt-image`** העדכני
  משפחת מודלים (ברירת מחדל **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` גם GA), מחליפה את
  התוכן הישן של DALL·E 2/3. תיקונים חשובים:
  - דגמי `gpt-image` מחזירים את התמונה כ**base64 (`b64_json`)**, לא ככתובת URL. עדכון כל הדוגמאות ל-
    `base64.b64decode(...)` במקום להוריד `url` עם `requests`.
  - שדרוג גרסת ה-API של תמונות ל-`2025-04-01-preview`.
  - הוחלפה הסעיף המצורף "טמפרטורה" (דגמי תמונה לא מקבלים `temperature`) ו
    תוכן ה-**שינויים** בתמונה של DALL·E-2 בלבד בחלק של **עריכת תמונות** (מסכה/ציור מחדש).
  - עודכן `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, שניהם
    מחברות משימות (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), וגם מחברת .NET `.dib`.

### הוסר

- נמחקו דוגמאות מיושנות של `python/aoai-app-variation.py` ו-`python/oai-app-variation.py`
  (`images.create_variation` מיועד ל-DALL·E-2 בלבד ואינו נתמך על ידי `gpt-image`).
- נמחקו 4 נכסי תמונה מנותקים הקשורים לסעיף ההשוואה של הטמפרטורה שהוסר
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- הוסר התלות המיותרת `requests` מדוגמאות ופירורי ההוראה בפייתון.

### אומת

- הרצה של `aoai-app.py` מקצה לקצה נגד דגם `gpt-image-1.5` מפורס ומאומת שהזרימה של דיקוד/שמירת בסיס64 מפיקה PNG. האפסנופים אושרו כ-JSON תקין.






- **מודל השיחה ברירת המחדל `gpt-4o-mini` → `gpt-5-mini`** בכל דוגמאות ההפעלה בתוכנית הלימודים,
  התיעוד והקונפיגורציה. זה הונע על ידי סטטוס מחזור החיים של המודל: במיקרוסופט פאונדרי,
  `gpt-4o-mini` (יפסק ב-2026-10-01) וכל משפחת `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, ייפסקו ב-2026-10-14) **מתבטלים**, בעוד ש**משפחת GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) זמינה בדרך כלל** (יפסק ב-2027-02-06). עודכן:
  - `.env.copy`, `00-course-setup/03-providers.md` (הפצתו המומלצת ופקודות הפריסה `az cognitiveservices`),
    ו-README של השעורים 04, 06, 07 ו-15.
  - דוגמאות פייתון בשיעור 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) וקטעי קוד של שיעור 08.
  - דוגמאות TypeScript / JavaScript בשיעורים 06, 07, ו-11, ובמחברות `.dib` .NET עבור
    שיעורים 06 ו-07.
  - מחברות משימות בשיעורים 04, 06, 07, ו-11 (תאי קוד), בנוסף לדוגמאות `shared/python/api_utils.py`
    של docstring.
- **הנחיה לפרמטר reasoning-model (חדש).** `gpt-5-mini` הוא מודל *הסקה*: הוא **לא**
  תומך ב-`temperature`/`top_p`, ומשתמש ב-`max_completion_tokens` (השלמות צ'אט) /
  ב-`max_output_tokens` (API תגובות) במקום ב-`max_tokens`. בהתאם לכך:
  - הוסר `temperature`/`top_p`/`max_tokens` מהדוגמאות שכעת כברירות מחדל משתמשות ב-`gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, שיעור 15 RAG README).
  - נוסף הערה **"מודלי הסקה לא משתמשים ב-`temperature`"** לשיעור 06, המסבירה ש-
    מודלי הסקה מונחים עם **הנדסת פקודות + בקרות הסקה** במקום
    כפתורי דגימה, בעוד ש-`temperature`/`top_p` נשארים תקפים במודלים שאינם מבוססי הסקה
    (GPT-4.x, Mistral, Llama, Phi, מודלים פתוחים).
- **`gpt-5-mini` אינו משמש במדריך לכיוונון עדין (שיעור 18).** GPT-5 תומך רק
  בכיוונון עדין באמצעות תגמול (RFT); סרט ההדרכה של השיעור 18 לכיוונון עדין מפוקח (SFT) ממשיך
  להשתמש ב-`gpt-4.1-mini`, שתומך ב-SFT/DPO.
- **הדגמות הטמפרטורה משתמשות בדגם Llama.** כדי לשמר הדרכה של `temperature` (שדגמי ההנמקה
  דוחים), משתמשים בדגם `Llama-3.3-70B-Instruct` דרך נקודת הקצה Foundry Models. נוסף משתנה חדש
  `AZURE_INFERENCE_CHAT_MODEL` ל-`.env.copy`; הפנקסים של השיעורים 04/06 `githubmodels` ו-
  הדוגמה של `06` `js-githubmodels` קוראים אותו (וחוזרים לברירת המחדל `Llama-3.3-70B-Instruct`) ושומרים את ההדגמות שלהם
  `temperature`/`top_p`/`max_tokens`.
- **דוגמאות JS / .NET עודכנו עבור GPT-5.** הוסרו `temperature`/`top_p`/`max_tokens` מדוגמאות GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - שגם מעלה `MaxOutputTokenCount`
  כך שהתוצאה של הטיעון לא מתקצרת). דוגמת `06` `js-githubmodels` משתמשת כעת ב- Llama כדי לשמור על ה
  הדגמת הטמפרטורה. `.dib` מציין ש- `Azure.AI.Inference` + מודל Llama היא הדרך לה
  להדגים `Temperature` ב-.NET.
- הושארו `gpt-4o-mini` / `gpt-5-mini` במקומם שם הם נכונים: התייחסויות לקידוד טוקנים `tiktoken`,
  רשימות זמינות קטלוג מודלים, ומודלים לדיבור בשיעור 02 (`gpt-4o-transcribe`).
- דוגמאות משיעור 20 (Mistral) ו-21 (Meta) שומרות על `temperature`/`max_tokens` כי הן מיועדות
  למודלים של Mistral/Llama התומכים בפרמטרים אלה.

## [2026-07-06] — רענון מודרניזציה של תוכן

רענון רחב לשמירה על דיוק הקורס לשנת 2026: APIs מודרניים, שמות מוצר ומודלים עדכניים,
הנחיות ספק מעודכנות, וכלי חווית מפתח חדשים.

### נוסף

- סעיף **Microsoft Agent Framework** בשיעור `17-ai-agents` המכסה סוכני שיחה בודדים,  
  כלים / קריאת פונקציות, קונפיגורציית Azure OpenAI (Microsoft Foundry), ותזמור זרימת עבודה של סוכני ריבוי (`SequentialBuilder` / `ConcurrentBuilder`).  
 
- **Foundry Local** מתועד כספק לא מקוון / במכשיר (לצד Ollama) ב  
  `00-course-setup/03-providers.md` ובשיעור `19-slm`.  
- **זרימות עבודה של אינטגרציה רציפה**:  
  - `.github/workflows/code-quality.yml` — Ruff + Black (מאכפים על מודול `shared/` המתוחזק, הנחייה על שאר תוכנית הלימודים), מעבר ESLint ייעוצי, ועבודת pytest.  
 
  - `.github/workflows/security.yml` — ניתוח CodeQL (Python + JavaScript/TypeScript) ובדיקת תלות על בקשות משיכה.  
 
- **מארז בדיקות** תחת `tests/` — 41 בדיקות pytest המכסות את מודול הכלי המשותף.  
- **מיומנות מיגרציה מ-Azure OpenAI ל-Responses API** תחת  
  `.github/skills/azure-openai-to-responses/` המשמש להנחיית המיגרציה של ה-API.  

### שונה  

- **Chat Completions API → Responses API** בכל דוגמאות השיחה ב-Python ו-TypeScript  
  (`client.responses.create(...)` → `response.output_text`), כולל שיעורים 04, 06, 07, 11,  
  15, ו-18, בנוסף למסמכי ה-README שלהם.  
- **דגמי GitHub → דגמי Microsoft Foundry** בכל הטקסט, הקישורים והדוגמאות. דגמי GitHub
  פורשים בסוף יולי 2026; הדוגמאות כעת מפנות אל קטלוג הדגמים של Microsoft Foundry ומשתמשות
  במשתני הסביבה `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, ותיעוד ספקים** עודכנו כדי לשקף ש-Azure OpenAI הוא עכשיו חלק
  מ-Microsoft Foundry, וגרסת ה-API המוגדרת כברירת מחדל הועלתה ל-`2024-10-21`.
- **דוגמאות TypeScript** (שיעורים 06, 07, 08, 11) הועברו מחבילת ה-beta המודרת `@azure/openai`
  לחבילת `openai` (יישומי הצ׳אט משתמשים ב-Responses API; יישום החיפוש משתמש ב-
  embeddings client).
- **מחברות .NET** (`dotnet/*.dib`) אומתו ל-`Azure.AI.OpenAI` **2.1.0**: שיעורים 06 ו-07
  משתמשים ב-`ChatClient` API, שיעור 08 משתמש ב-`EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), ו-
  שיעור 09 משתמש ב-`ImageClient` (`GenerateImage`) עם `gpt-image-1`, המחליף את
  ה-`OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` הישן מ-`1.0.0-beta.9`.
- **עידן שם המוצר**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (שיעורים 14, 16, 17) ו-"Bing" → **Microsoft Copilot** (שיעור 12), כאשר הם התייחסו ל-
  המוצרים הנוכחיים.
- **DevContainer** (`.devcontainer/`) כעת שולח תוספים של Pylance, Black, Ruff, ESLint, Prettier, ו-Copilot,
  מאפשר עיצוב-בעת-שמירה, ומתקין את `ruff`, `black`, `mypy`, ו-`pytest` כך שניתן לשחזר את בדיקות ה-CI
  באופן מקומי.
- **יצירת תמונה** (שיעור 09) ממליץ על `gpt-image-1` עבור Azure (קטלוג Azure הוריד
  את `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** עודכן בהתאם לעבודה שהושלמה (הגירת API, CI,
  DevContainer, בדיקות) ולעובדות הנוכחיות (התרגומים מיוצרים אוטומטית על ידי
  מתרגם Azure Co-op; API של העוזרים הוחלף על ידי API של התגובות).

### תוקנו

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` מחזיר עכשיו
  מחרוזת ריקה עבור קלט שמכיל רק רווחים במקום להעלות שגיאת "קצר מדי" (תואם ל-
  מקרה של `None`). נמצא וכוסה על ידי מערך הבדיקות החדש.
- **דוגמאות תמונות של שיעור 09** — תוקנו שגיאות אמיתיות: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  ומשתנה שהצל על המודול `openai`.
- **מחברת RAG של שיעור 15** — תוקנה הגדרת הלקוח, הוחלף `DataFrame.append` שהוסר
  ב-`pd.concat`, ומודרנה השימוש ב-SDK הישן.
- שמות מודלים שיושמו / פורשו (`gpt-3.5-turbo`, `gpt-35-turbo`) הוחלפו ב-`gpt-4o-mini`
  בדוגמאות פעילות; תוצאות כוונון עדין היסטוריות בשיעור 18 נשמרו וסומנו
  במקום להיכתב מחדש.

### יושמו / הערות

- **דוגמאות של מודלים של Microsoft Foundry** שמשתמשות ב-`azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — הדוגמאות והשיעורים 19, 20,
  ו-21 של `githubmodels-*` ו-`js-githubmodels` — נשארים על Model Inference API, שאינו **תומך** ב-Responses API. אלו
  הושארו במכוון על ה-SDK הזה.
- `AzureOpenAI()` נשמר במכוון במקום בו הוא עדיין מתאים (הטמעות ויצירת תמונות),
  מכיוון שתהליכים אלה אינם חלק מההגירה ל-Responses API.
- הפניות ל-`text-embedding-ada-002` נשמרות במקום בו אינדקס הטמעות מחושב מראש תלוי בהן.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->