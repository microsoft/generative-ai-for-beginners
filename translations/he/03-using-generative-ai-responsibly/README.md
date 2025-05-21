<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:44:21+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "he"
}
-->
# שימוש באינטליגנציה מלאכותית גנרטיבית באחריות

> _לחצו על התמונה למעלה לצפייה בסרטון של שיעור זה_

קל להתפעל מאינטליגנציה מלאכותית ובפרט מאינטליגנציה מלאכותית גנרטיבית, אך חשוב לשקול כיצד להשתמש בה באחריות. יש לשקול דברים כמו כיצד להבטיח שהפלט יהיה הוגן, לא מזיק ועוד. פרק זה נועד לספק לך את ההקשר הנזכר, מה לשקול וכיצד לנקוט צעדים פעילים כדי לשפר את השימוש שלך ב-AI.

## הקדמה

שיעור זה יכסה:

- מדוע עליך לתת עדיפות ל-AI אחראי בעת בניית יישומי AI גנרטיביים.
- עקרונות הליבה של AI אחראי וכיצד הם קשורים ל-AI גנרטיבי.
- כיצד ליישם את עקרונות ה-AI האחראי הללו באמצעות אסטרטגיה וכלים.

## מטרות למידה

לאחר סיום השיעור הזה תדע:

- החשיבות של AI אחראי בעת בניית יישומי AI גנרטיביים.
- מתי לחשוב וליישם את עקרונות הליבה של AI אחראי בעת בניית יישומי AI גנרטיביים.
- אילו כלים ואסטרטגיות זמינים לך כדי ליישם את רעיון ה-AI האחראי בפועל.

## עקרונות AI אחראי

ההתרגשות סביב AI גנרטיבי מעולם לא הייתה גבוהה יותר. התרגשות זו הביאה הרבה מפתחים חדשים, תשומת לב ומימון לתחום זה. למרות שזה מאוד חיובי עבור כל מי שמחפש לבנות מוצרים וחברות תוך שימוש ב-AI גנרטיבי, חשוב גם להתקדם באחריות.

במהלך קורס זה, אנו מתמקדים בבניית הסטארט-אפ שלנו ומוצר החינוך שלנו ב-AI. נשתמש בעקרונות ה-AI האחראי: הוגנות, הכללה, אמינות/בטיחות, אבטחה ופרטיות, שקיפות ואחריות. עם עקרונות אלו, נחקור כיצד הם קשורים לשימוש שלנו ב-AI גנרטיבי במוצרים שלנו.

## מדוע עליך לתת עדיפות ל-AI אחראי

בעת בניית מוצר, גישה ממוקדת באדם תוך שמירה על האינטרס הטוב ביותר של המשתמש שלך מובילה לתוצאות הטובות ביותר.

הייחודיות של AI גנרטיבי היא כוחו ליצור תשובות מועילות, מידע, הדרכה ותוכן עבור משתמשים. זה יכול להיעשות ללא צעדים ידניים רבים שיכולים להוביל לתוצאות מרשימות מאוד. ללא תכנון ואסטרטגיות נכונות, זה יכול גם למרבה הצער להוביל לכמה תוצאות מזיקות עבור המשתמשים שלך, המוצר שלך והחברה כולה.

בואו נסתכל על כמה (אבל לא כל) מהתוצאות המזיקות הפוטנציאליות הללו:

### הזיות

הזיות הן מונח המשמש לתיאור כאשר LLM מייצר תוכן שהוא או חסר היגיון לחלוטין או משהו שאנו יודעים שהוא שגוי עובדתית על סמך מקורות מידע אחרים.

נניח לדוגמה שאנחנו בונים תכונה לסטארט-אפ שלנו המאפשרת לסטודנטים לשאול שאלות היסטוריות למודל. סטודנט שואל את השאלה `Who was the sole survivor of Titanic?`

המודל מייצר תגובה כמו זו שלמטה:

![שאלה "מי היה הניצול היחיד של הטיטניק"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(מקור: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

זו תשובה מאוד בטוחה ומפורטת. למרבה הצער, זה לא נכון. אפילו עם כמות מינימלית של מחקר, ניתן לגלות שהיו יותר מניצול אחד מאסון הטיטניק. עבור סטודנט שרק מתחיל לחקור את הנושא הזה, התשובה הזו יכולה להיות משכנעת מספיק כדי לא להיחקר ולהתייחס אליה כעובדה. ההשלכות של כך יכולות להוביל לכך שהמערכת ה-AI תהיה לא אמינה ולהשפיע לרעה על המוניטין של הסטארט-אפ שלנו.

עם כל איטרציה של כל LLM נתון, ראינו שיפורי ביצועים סביב צמצום הזיות. גם עם שיפור זה, אנו כבוני יישומים ומשתמשים עדיין צריכים להישאר מודעים למגבלות אלה.

### תוכן מזיק

כיסינו בסעיף הקודם כאשר LLM מייצר תגובות שגויות או חסרות היגיון. סיכון נוסף שעלינו להיות מודעים אליו הוא כאשר מודל מגיב בתוכן מזיק.

תוכן מזיק יכול להיות מוגדר כ:

- מתן הוראות או עידוד פגיעה עצמית או פגיעה בקבוצות מסוימות.
- תוכן שנאה או מזלזל.
- הנחיית תכנון כל סוג של התקפה או מעשי אלימות.
- מתן הוראות כיצד למצוא תוכן לא חוקי או לבצע מעשים לא חוקיים.
- הצגת תוכן מיני מפורש.

עבור הסטארט-אפ שלנו, אנחנו רוצים לוודא שיש לנו את הכלים והאסטרטגיות הנכונים כדי למנוע מהסוג הזה של תוכן להיראות על ידי סטודנטים.

### חוסר הוגנות

הוגנות מוגדרת כ"להבטיח שמערכת AI תהיה חופשית מהטיה ואפליה ושהיא תתייחס לכולם בהוגנות ושוויון." בעולם ה-AI הגנרטיבי, אנו רוצים להבטיח שהשקפות עולם המוציאות את המודלים לא יחוזקו על ידי פלט המודל.

סוגי פלט אלו אינם רק הרסניים לבניית חוויות מוצר חיוביות עבור המשתמשים שלנו, אלא הם גם גורמים נזק חברתי נוסף. כמתכנתי יישומים, עלינו תמיד לזכור בסיס משתמשים רחב ומגוון בעת בניית פתרונות עם AI גנרטיבי.

## כיצד להשתמש ב-AI גנרטיבי באחריות

עכשיו שזיהינו את החשיבות של AI גנרטיבי אחראי, בואו נסתכל על 4 צעדים שנוכל לנקוט כדי לבנות את פתרונות ה-AI שלנו באחריות:

### למדוד נזקים פוטנציאליים

בבדיקות תוכנה, אנו בודקים את הפעולות הצפויות של משתמש על יישום. באופן דומה, בדיקת מגוון רחב של פקודות שמשתמשים עשויים להשתמש בהן היא דרך טובה למדוד נזק פוטנציאלי.

מכיוון שהסטארט-אפ שלנו בונה מוצר חינוכי, יהיה טוב להכין רשימה של פקודות הקשורות לחינוך. זה יכול להיות כדי לכסות נושא מסוים, עובדות היסטוריות ופקודות על חיי הסטודנט.

### למתן נזקים פוטנציאליים

עכשיו הזמן למצוא דרכים שבהן נוכל למנוע או להגביל את הנזק הפוטנציאלי הנגרם על ידי המודל והתגובות שלו. נוכל להסתכל על זה ב-4 שכבות שונות:

- **מודל**. בחירת המודל הנכון עבור המקרה הנכון. מודלים גדולים ומורכבים יותר כמו GPT-4 יכולים לגרום ליותר סיכון לתוכן מזיק כאשר הם מיושמים על מקרים קטנים וספציפיים יותר. שימוש בנתוני האימון שלך כדי לבצע כיוונון עדין גם מפחית את הסיכון לתוכן מזיק.

- **מערכת בטיחות**. מערכת בטיחות היא סט כלים ותצורות על הפלטפורמה המשרתת את המודל המסייעת למתן נזק. דוגמה לכך היא מערכת סינון התוכן בשירות Azure OpenAI. מערכות צריכות גם לזהות התקפות jailbreak ופעילות לא רצויה כמו בקשות מבוטים.

- **מטה-פקודה**. מטה-פקודות והקרקעה הם דרכים שבהן נוכל להנחות או להגביל את המודל על סמך התנהגויות ומידע מסוימים. זה יכול להיות שימוש בקלטי מערכת כדי להגדיר מגבלות מסוימות של המודל. בנוסף, לספק פלטים שרלוונטיים יותר להיקף או לתחום של המערכת.

זה יכול להיות גם שימוש בטכניקות כמו Generation Augmented Generation (RAG) כדי שהמודל ימשוך מידע רק ממבחר מקורות מהימנים. יש שיעור מאוחר יותר בקורס זה ל[בניית יישומי חיפוש](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **חוויית משתמש**. השכבה הסופית היא המקום שבו המשתמש מתקשר ישירות עם המודל דרך הממשק של האפליקציה שלנו בדרך כלשהי. בדרך זו אנו יכולים לעצב את ה-UI/UX כדי להגביל את המשתמש בסוגי הקלטים שהוא יכול לשלוח למודל וכן בטקסטים או תמונות המוצגות למשתמש. כאשר אנו משיקים את יישום ה-AI, עלינו גם להיות שקופים לגבי מה יישום ה-AI הגנרטיבי שלנו יכול ולא יכול לעשות.

יש לנו שיעור שלם המוקדש ל[עיצוב UX ליישומי AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **הערכת מודל**. עבודה עם LLMs יכולה להיות מאתגרת מכיוון שאין לנו תמיד שליטה על הנתונים שעליהם המודל אומן. ללא קשר לכך, עלינו תמיד להעריך את הביצועים והפלטים של המודל. עדיין חשוב למדוד את הדיוק, הדמיון, הקרקעה והרלוונטיות של הפלט של המודל. זה עוזר לספק שקיפות ואמון לבעלי עניין ולמשתמשים.

### הפעלת פתרון AI גנרטיבי אחראי

בניית נוהל תפעולי סביב יישומי ה-AI שלך היא השלב האחרון. זה כולל שיתוף פעולה עם חלקים אחרים בסטארט-אפ שלנו כמו מחלקות משפטיות וביטחון כדי להבטיח שאנו עומדים בכל מדיניות הרגולציה. לפני ההשקה, אנו גם רוצים לבנות תוכניות סביב אספקה, טיפול בתקלות והחזרה לאחור כדי למנוע כל נזק למשתמשים שלנו מגידול.

## כלים

בעוד שעבודת הפיתוח של פתרונות AI אחראיים עשויה להיראות כעבודה רבה, זו עבודה ששווה את המאמץ. ככל שתחום ה-AI הגנרטיבי מתפתח, יותר כלים שיעזרו למפתחים לשלב אחריות ביעילות בתהליכי העבודה שלהם יתבגרו. לדוגמה, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) יכול לעזור לזהות תוכן ותמונות מזיקים באמצעות בקשת API.

## בדיקת ידע

מהם הדברים שעליך לדאוג להם כדי להבטיח שימוש אחראי ב-AI?

1. שהתשובה נכונה.
1. שימוש מזיק, שה-AI לא ישמש למטרות פליליות.
1. להבטיח שה-AI חופשי מהטיה ואפליה.

תשובה: 2 ו-3 נכונים. AI אחראי עוזר לך לשקול כיצד למתן השפעות מזיקות והטיות ועוד.

## 🚀 אתגר

קרא על [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) וראה מה אתה יכול לאמץ לשימושך.

## עבודה מצוינת, המשך ללמוד

לאחר שסיימת את השיעור הזה, בדוק את [אוסף הלמידה של AI גנרטיבי שלנו](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך לשפר את הידע שלך ב-AI גנרטיבי!

עבור לשיעור 4 שבו נסתכל על [יסודות הנדסת פקודות](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום אנושי מקצועי. אנו לא נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.