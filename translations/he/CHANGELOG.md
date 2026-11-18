# יומן שינויים

כל השינויים הבולטים בתכנית הלימודים של AI גנרטיבי למתחילים מתועדים בקובץ זה.

הפורמט מבוסס על [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). מכיוון שזו תכנית לימודים
ולא חבילת תוכנה בגרסאות, הרשומות מקובצות לפי תאריך.

## [2026-07-16] — אימות תוכן + נכסי תמונה לשיעור 09

### שונה

- **שיעור 10 (יישומי AI עם קוד נמוך):** עדכון שני קישורי `docs.microsoft.com/powerapps/...` Dataverse שפורשו
  לקישורי `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` הנוכחיים
  (נבדקו חיים).
- **שיעור 17 (סוכני AI):** מודרניזציה של דוגמת מודל מיושנת (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) ושם פריסת מחרוזת מישמש בדוגמת מסגרת הסוכן
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **שורש `README.md`:** הוספת מזהה מעקב `?WT.mc_id=academic-105485-koreyst` חסר לקישור
  *Microsoft for Startups*.
- **נכסי תמונה של שיעור 09** שוחזרו עם מודל `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, ו-
  `images/startup.png` (זוג הדוגמה לעריכה לפני/אחרי הופק באמצעות קריאה אמיתית של
  `client.images.edit` עם מסכה שנוצרה).

### מאומת

- בדקתי את קבצי ה-README של השיעורים 01, 03, 05, 12, 14, ו-16 — כולם עדכניים (שמות Microsoft Foundry וקישורים נכונים);
  לא נדרשו שינויים.
- הרצתי אימות מלא של markdown על כל 41 קבצי markdown במאגר (ללא תרגומים) עבור
  נתיבי תיעוד מיושנים, `/en-us/` אזורי Microsoft, שמות מוצר/דגם לא מעודכנים, מזהי מעקב חסרים,
  וקישורים/תמונות יחסיים שבורים. רק הפער היחיד במזהה מעקב *Microsoft for Startups* היה
  ניתן לטיפול; כל הדגלים האחרים אושרו כחיוביים שגויים (קישורי תרגום שנוצרו אוטומטית,
  משתני דיבוג שהוסתרו, וכתובות מבניות של צד שלישי `/en/`).

## [2026-07-15] — שיעור 09 (יישומי תמונה) כתיבה מחדש עבור דגמי תמונה GPT

### שונה

- **נכתבה מחדש שיעור 09 "בניית יישומי יצירת תמונות"** סביב ה- **`gpt-image`**
  משפחת מודלים (ברירת מחדל **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` גם GA), מחליפים את
  תוכן ה-DALL·E 2/3 הישן. תיקונים עיקריים:
  - דגמי `gpt-image` מחזירים את התמונה כ-**base64 (`b64_json`)**, לא ככתובת URL. כל הדוגמאות עודכנו ל-
    `base64.b64decode(...)` במקום הורדת `url` עם `requests`.
  - שדרגתי את גרסת ה-API של התמונה ל-`2025-04-01-preview`.
  - החלפתי את סקשן ה"temperature" המומצא (מודלי תמונה לא מקבלים `temperature`) ואת
    התוכן של **שינויים** בתמונה המיועד רק ל-DALL·E-2 בקטגוריית **עריכת תמונה** (מסכה/צביעה מחדש).
  - עדכנתי את `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, גם
    מחברות השיעורים (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), ואת מחברת ה-.NET `.dib`.

### הוסר

- מחקתי את דוגמאות ה-`python/aoai-app-variation.py` וה-`python/oai-app-variation.py` המיושנות
  (`images.create_variation` מיועד רק ל-DALL·E-2 ואינו נתמך על ידי `gpt-image`).
- מחקתי 4 נכסי תמונה יתומים הקשורים לסקשן שנמחק של השוואת הטמפרטורות
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- הסרתי את התלות המיותרת ב-`requests` מדוגמאות הפייתון והדרישות של השיעור.

### אומת

- הרצתי את `aoai-app.py` מקצה לקצה מול מודל פרוס של `gpt-image-1.5` ואישרתי שזרם הפיענוח/שמירת base64 מייצר PNG. המחברות אומתו כקובצי JSON תקינים.


## [2026-07-14] — עדכון מודל ברירת מחדל + הנחיית מודל הסקת מסקנות

### שונה

- **דגם הצ'אט ברירת המחדל `gpt-4o-mini` → `gpt-5-mini`** בכל דוגמות הריצה של הקורס,
  התיעוד, וההגדרות. זה הונע לפי סטטוס מחזור החיים של הדגם: ב-Microsoft Foundry,
  `gpt-4o-mini` (יוצא מהשירות ב-2026-10-01) וכל משפחת `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, יוצאות מהשירות ב-2026-10-14) הן **מתבטלות בהדרגה**, בעוד ש**משפחת GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) זמינה באופן כללי** (יוצאת מהשירות ב-2027-02-06). עודכן:
  - `.env.copy`, `00-course-setup/03-providers.md` (הגדרת פריסה מומלצת ופקודות `az cognitiveservices` 
    לפריסה), ותיעודי ה-README של השיעורים 04, 06, 07, ו-15.
  - דוגמאות בפייתון בשיעור 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) וסקריפטים בשיעור 08.
  - דוגמאות TypeScript / JavaScript בשיעורים 06, 07, ו-11, וערכת המחברות של `.dib` ב-.NET לשיעורים
    06 ו-07.
  - מחברות משימות בשיעורים 04, 06, 07, ו-11 (תאי קוד), בנוסף לדוגמאות דוקסטרינג של `shared/python/api_utils.py`.

- **הנחיות לפרמטר reason-model (חדש).** `gpt-5-mini` הוא *מודל הסקה*: הוא **אינו**
  תומך ב-`temperature`/`top_p`, ומשתמש ב-`max_completion_tokens` (שיחות השלמה) /
  `max_output_tokens` (ממשק API לתגובות) במקום `max_tokens`. בהתאם לכך:
  - הוסר `temperature`/`top_p`/`max_tokens` מדוגמאות שהסטנדרט שלהם עכשיו הוא `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, שיעור 15 RAG README).
  - נוסף הערה **"מודלי הסקה לא משתמשים ב-`temperature`"** לשיעור 06, שמסבירה כי
    מודלי הסקה מכוונים באמצעות **הנדסת פרומפט + בקרים של הסקה** במקום
    כפתורי דגימה, בעוד ש-`temperature`/`top_p` נשארים בתוקף על מודלים שלא מבוססים על הסקה
    (GPT-4.x, Mistral, Llama, Phi, מודלים פתוחים).
- **`gpt-5-mini` אינו בשימוש במדריך לכוונון עדין (שיעור 18).** GPT-5 תומך רק
  בכוונון עדין מבוסס חיזוק (RFT); הסבר המדריך לשיעור 18 לכוונון עדין מפוקח (SFT)
  שומר על `gpt-4.1-mini`, שתומך ב-SFT/DPO.
- **דוגמאות טמפרטורה משתמשות במודל ללה.** כדי להמשיך ללמד `temperature` (שמודלים של היגיון
  דוחים), משתמשים במודל `Llama-3.3-70B-Instruct` דרך נקודת הקצה של מודלים Foundry. נוסף משתנה
  חדש `AZURE_INFERENCE_CHAT_MODEL` ל-`.env.copy`; מחברות השיעור 04/06 `githubmodels` ודגימת
  `06` `js-githubmodels` קוראים לזה (נופלים חזרה ל-`Llama-3.3-70B-Instruct`) ושומרים על
  דוגמאות `temperature`/`top_p`/`max_tokens` שלהם.
- **דוגמאות JS / .NET עודכנו עבור GPT-5.** הוסרו `temperature`/`top_p`/`max_tokens` מ-GPT-5
  דוגמאות (`06` `recipe-app` TypeScript, `06` `.dib` .NET - שגם מגדיל `MaxOutputTokenCount`
  כך שפלט ההסקה לא יקוצר). דוגמת `06` `js-githubmodels` כעת משתמשת ב- Llama כדי לשמור על 
  הדגמת הטמפרטורה שלה. `.dib` מציין ש- `Azure.AI.Inference` + מודל Llama הוא הדרך 
  להדגים `Temperature` ב-.NET.
- שמאלה `gpt-4o-mini` / `gpt-5-mini` במקום שבו הם נשארים מדויקים: הפניות לקידוד טוקנים `tiktoken`,
  רשימות זמינות קטלוג מודלים, ודגמי דיבור בשיעור 02 (`gpt-4o-transcribe`).
- דוגמאות השיעור 20 (Mistral) ו-21 (Meta) שומרים על `temperature`/`max_tokens` כי הן מכוונות ל-
  מודלי Mistral/Llama, התומכים בפרמטרים האלה.

## [2026-07-06] — רענון מודרניזציה של תוכן

רענון רחב לשמירת הדיוק של התכנית לשנת 2026: ממשקי API מודרניים, שמות מוצרים עדכניים ו-
שמות מודלים, הנחיות ספק מעודכנות, וכלי חווית מפתח חדשים.

### נוסף

- קטע **מסגרת סוכני מיקרוסופט** בשיעור `17-ai-agents` הכולל סוכני שיחה בודדים,
  כלים/קריאות פונקציה, קונפיגורציית Azure OpenAI (Microsoft Foundry), וסוכנים מרובים
  תזמור זרימות עבודה (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** מתועד כספק לא מקוון / על המכשיר (לצד Ollama) ב-
  `00-course-setup/03-providers.md` והדרכה `19-slm`.
- **זרימות עבודה של אינטגרציה רציפה**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (מוחל על מודול ה-`shared/` המתוחזק,
    מייעץ לשאר הקורס), מעבר ייעוץ ESLint, ועבודת pytest.
  - `.github/workflows/security.yml` — ניתוח CodeQL (פייתון + JavaScript/TypeScript) ו-
    סקירת תלות על בקשות משיכה.
- **מערך בדיקות** תחת `tests/` — 41 בדיקות pytest המכסות את מודול השירות המשותף.
- **Azure OpenAI → מיומנות מעבר ל-Responses API** תחת
  `.github/skills/azure-openai-to-responses/` המשמש להנחיית מעבר ה-API.

### שונה

- **מ-Chat Completions API ל-Responses API** בכל דוגמאות הצ'אט ב-Python ו-TypeScript
  (`client.responses.create(...)` → `response.output_text`), כולל שיעורים 04, 06, 07, 11,
  15 ו-18, בנוסף ל-READMEs שלהם.
- **מ- GitHub Models ל- Microsoft Foundry Models** בכל הטקסט, הקישורים והדוגמאות. GitHub Models
  יפסיק לפעול בסוף יולי 2026; הדוגמאות כעת מצביעות על קטלוג הדגמים של Microsoft Foundry ומשתמשות
  במשתני הסביבה `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, והתיעוד של הספק** עודכנו לשקף ש-Azure OpenAI היא כעת חלק
  מ-Microsoft Foundry, וגרסת ה-API ברירת המחדל הועלתה ל-`2024-10-21`.
- **דוגמאות TypeScript** (שיעורים 06, 07, 08, 11) הועברו מה-SDK הביתא המיושן `@azure/openai`
  לחבילת `openai` (אפליקציות צ'אט משתמשות ב-Responses API; אפליקציית החיפוש משתמשת ב-
  embeddings client).
- **מחברות .NET** (`dotnet/*.dib`) וסטנדרטיות ב־`Azure.AI.OpenAI` **2.1.0**: שיעורים 06 ו־07
  משתמשים ב־API של `ChatClient`, שיעור 08 משתמש ב־`EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), ו-
  שיעור 09 משתמש ב־`ImageClient` (`GenerateImage`) עם `gpt-image-1`, מחליף את ה־
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` הישן מ־`1.0.0-beta.9`.
- **מודרניזציה של שם המוצר**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (שיעורים 14, 16, 17) ו-"Bing" → **Microsoft Copilot** (שיעור 12), כאשר אלה התייחסו ל־
  המוצרים הנוכחיים.
- **DevContainer** (`.devcontainer/`) כעת כולל את התוספים Pylance, Black, Ruff, ESLint, Prettier ו-Copilot
  מאפשר עיצוב אוטומטי בעת שמירה, ומתקין את `ruff`, `black`, `mypy`, ו-`pytest` כך שניתן לשכפל
  את בדיקות ה-CI באופן מקומי.
- **יצירת תמונות** (שיעור 09) ממליץ על `gpt-image-1` עבור Azure (קטלוג Azure הפסיק
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** עודכן כדי לשקף עבודה שהושלמה (העברת API, CI,
  DevContainer, בדיקות) ועובדות נוכחיות (התרגומים מיוצרים אוטומטית על ידי
  Azure Co-op Translator; ממשק ה-API של העוזרים הוחלף בממשק ה-API של התגובות).

### תוקן

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` עכשיו מחזיר
  מחרוזת ריקה עבור קלט המכיל רק רווחים במקום להעלות שגיאת "קצר מדי" (תואם ל-
  `None` מקרה). נמצא ומוכלל על ידי ערכת הבדיקה החדשה.
- **דוגמאות תמונות שיעור 09** — תוקנו באגים אמיתיים: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  ומשתנה שהסתיר את המודול `openai`.
- **מחברת שיעור 15 RAG** — תוקן הגדר הלקוח, הוחלף ה-`DataFrame.append` שהוסר  
  עם `pd.concat`, ועדכנו את השימוש בממשק ה- SDK המיושן.
- שמות מודלים מיושנים / פרישה (`gpt-3.5-turbo`, `gpt-35-turbo`) הוחלפו ב- `gpt-4o-mini`
  בדוגמאות פעילות; פלטים של כוונון עדין היסטורי בשיעור 18 נשמרו ותיועדו
  במקום להיכתב מחדש.

### מיושן / הערות

- **דוגמאות Microsoft Foundry Models** שמשתמשות ב-`azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — דוגמאות `githubmodels-*` ו-`js-githubmodels` והלקחים 19, 20,
  ו-21 — נשארות על Model Inference API, שאינו תומך ב-Responses API. אלה
  מותירות במכוון ב-SDK הזה.
- `AzureOpenAI()` נשמר בכוונה כאשר הוא עדיין מתאים (הטמעות ויצירת תמונות),
  מכיוון שזרימות עבודה אלה אינן חלק מהגירת API התגובות.
- הפניות ל- `text-embedding-ada-002` נשמרות כאשר אינדקס הטמעה מחושב מראש תלוי בהן.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->