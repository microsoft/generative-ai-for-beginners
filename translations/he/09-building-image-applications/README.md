# בניית אפליקציות ליצירת תמונות

[![בניית אפליקציות ליצירת תמונות](../../../translated_images/he/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

יש ל-LLM יותר מאשר יצירת טקסט. אפשר גם לייצר תמונות מתיאורי טקסט. תמונות כמדיום שימושיות בתחומים כמו MedTech, אדריכלות, תיירות, פיתוח משחקים, שיווק ועוד. בשיעור זה נבחן את דגמי **GPT Image** העדכניים ונבנה אפליקציית יצירת תמונות.

## מבוא

יצירת תמונות מאפשרת להפוך פקודת שפה טבעית לתמונה. בשיעור זה נעבוד עם משפחת המודלים **`gpt-image`** של OpenAI - הדור הנוכחי של דגמי תמונות הזמינים ב-[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ופלטפורמת OpenAI. דגמים אלו מחליפים את דגמי DALL·E הישנים (DALL·E 2/3 הם מורשת).

לאורך השיעור נשתמש בסטארטאפ בדוי, **Edu4All**, שמפתח כלי למידה. הצוות רוצה לייצר איורים למשימות ולחומרי לימוד.

## מטרות הלמידה

בסוף שיעור זה תוכל:

- להסביר מהי יצירת תמונות והיכן היא שימושית.
- להבין את משפחת מודלי `gpt-image` ואיך הם שונים מדגמי DALL·E הוותיקים.
- לבנות אפליקציית יצירת תמונות בפייתון (וב-TypeScript / .NET).
- לערוך תמונות וליישם כללי הגנה באמצעות מטא-פרומפטים.

## מהי יצירת תמונות?

דגמי יצירת תמונות יוצרים תמונות מתוך פקודת טקסט. דגמים מודרניים כמו `gpt-image` מבוססים על טכניקות Transformer + Diffusion: המודל לומד את הקשר בין טקסט לתמונות במהלך האימון, ואז, בהינתן פקודה, מסיר בהדרגה רעש אקראי לתמונה שתואמת את התיאור.

שתי משפחות ידועות של דגמי תמונה הן:

- **`gpt-image` (OpenAI)** - הדור הנוכחי, בשימוש בשיעור זה. תומך ביצירת תמונה מטקסט ועריכת תמונות (inpainting עם מסכה).
- **Midjourney** - מודל צד שלישי פופולרי עם שירות עצמאי וזרימת עבודה מבוססת Discord.

> דגמי OpenAI הוותיקים - **DALL·E 2** ו-**DALL·E 3** - הם מורשת. DALL·E 3 אינו זמין לפריסות חדשות, ופיצ'רים כמו `create_variation` היו קיימים רק ב-DALL·E 2. השתמש בדגמי `gpt-image` לאפליקציות חדשות.

### איזה דגם `gpt-image` כדאי להשתמש?

ב-Microsoft Foundry זמינים באופן **כללי**:

| מודל | הערות |
| --- | --- |
| **`gpt-image-2`** | המודל העדכני והמתקדם ביותר - ברירת מחדל מומלצת. |
| `gpt-image-1.5` | זמין באופן כללי; איכות טובה במחיר נמוך יותר. |
| `gpt-image-1-mini` | זמין באופן כללי; הכי מהיר והכי זול. |
| `gpt-image-1` | לצפייה בלבד. |

תמיד בדוק את [רשימת דגמי התמונות ב-Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) למידע על זמינות ואזורי פעילות.

> **חשוב:** דגמי `gpt-image` מחזירים את התמונה שנוצרה ב**base64** (`b64_json`), לא כ-URL. הקוד שלך מפענח את מחרוזת ה-base64 לבייטים ושומר אותה - אין URL לתמונה להורדה.

## הגדרות

אפשר להריץ את הדוגמאות מול **Azure OpenAI ב-Microsoft Foundry** (הדוגמאות `aoai-*`) או מול **פלטפורמת OpenAI** (הדוגמאות `oai-*`).

### 1. צור ופרוס מודל

עקוב אחרי מדריך [יצירת משאב](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) כדי ליצור משאב ב-Microsoft Foundry, ואז פרוס מודל תמונה - מומלץ **`gpt-image-2`**.

### 2. הגדר את הקובץ `.env` שלך

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

מצא ערכים אלו בדף **פריסות** של המשאב שלך ב-[פורטל Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. התקן את הספריות

צור קובץ `requirements.txt`:

```text
python-dotenv
openai
pillow
```

לאחר מכן צור והפעל סביבה וירטואלית והתקן:

```bash
python3 -m venv venv
source venv/bin/activate        # חלונות: venv\Scripts\activate
pip install -r requirements.txt
```

## בניית האפליקציה

צור את הקובץ `app.py` עם הקוד הבא. הוא יוצר תמונה ושומר אותה כקובץ PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# הפנה את הלקוח למשאב Azure OpenAI (Microsoft Foundry) שלך.
# דגמי תמונה מצריכים גרסת API עדכנית - בדוק את תיעוד Foundry עבור הגרסה שהמודל שלך צריך.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # לדוגמה, "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # גם 1536x1024 (נוף), 1024x1536 (תמונה עומדת), או "אוטומטי"
    n=1,
)

# דגמי gpt-image מחזירים base64 (b64_json), לא כתובת URL - פענח זאת לבייטים.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

הרץ אותו עם `python app.py`. תקבל קובץ PNG שמור בתיקייה `images/`.

> כל קריאה ל-`images.generate` יוצרת תמונה שונה עבור אותו פרומפט - לדגמי תמונה אין פרמטר `temperature` (הוא שייך לשליטה ביצירת טקסט). לקבלת גיוון, פשוט קרא שוב ל-API; להפחתת גיוון - הפוך את הפרומפט שלך למדויק יותר.

## עריכת תמונות

דגמי `gpt-image` יכולים **לערוך** תמונה קיימת: ספק את התמונה, מסכה **אופציונלית** (שמציינת את האזור לשינוי), ופרומפט שמתאר את השינוי. כמו ביצירה, העריכות מוחזרות ב-base64.

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/he/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/he/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/he/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## הגדרת גבולות עם מטא-פרומפטים

לאחר שתוכל ליצור תמונות, אתה צריך כללי הגנה כדי שהאפליקציה שלך לא תפיק תוכן לא בטוח או לא מותאם למותג. **מטא-פרומפט** הוא טקסט שאתה מוסיף לפני הפרומפט של המשתמש כדי להגביל את הפלט של המודל.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# העבר את `prompt` ל-client.images.generate(...)
```

כל תמונה נוצרת עכשיו בתוך הגבולות שהציב המטא-פרומפט. שלב זאת עם מסנני התוכן הבנויים ב-Microsoft Foundry להגנה ברמת עומק.

## משימה - ננגיש לסטודנטים

לסטודנטים של Edu4All דרושות תמונות למבחנים שלהם. בנה אפליקציה שיוצרת תמונות של **אנדרטאות** (איזה אנדרטאות זה תלוי בך) במצבים שונים ויצירתיים - למשל, נקודת ציון מפורסמת בשקיעה עם ילד צופה.

נסה זאת בעצמך, ואז השווה לפתרונות המ-reference:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) אפליקציה מלאה ליצירה: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

עבד גם עם המחברות בתיקייה [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` ל-Azure, `oai-assignment.ipynb` ל-OpenAI).

## עבודה מצוינת! המשך ללמוד

לאחר שסיימת את השיעור, עיין ב-[אוספת הלימוד לבינה מלאכותית יוצרת שלנו](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך לשפר את הידע שלך ב-Generative AI!

עבור לשיעור 10 להמשך הלמידה.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->