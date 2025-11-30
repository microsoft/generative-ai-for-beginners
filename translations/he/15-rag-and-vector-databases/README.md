<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T20:03:46+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "he"
}
-->
# יצירת תשובות מועשרות על בסיס מידע (RAG) ומאגרי נתונים וקטוריים

[![יצירת תשובות מועשרות על בסיס מידע (RAG) ומאגרי נתונים וקטוריים](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.he.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

בשיעור על יישומי חיפוש, למדנו בקצרה כיצד לשלב נתונים משלכם במודלים שפה גדולים (LLMs). בשיעור זה, נעמיק יותר במושגים של עיגון הנתונים שלכם ביישום LLM, במכניקה של התהליך ובשיטות לאחסון נתונים, כולל הטמעות וטקסט.

> **וידאו בקרוב**

## מבוא

בשיעור זה נעסוק בנושאים הבאים:

- מבוא ל-RAG, מה זה ולמה משתמשים בו בבינה מלאכותית.

- הבנת מה הם מאגרי נתונים וקטוריים ויצירת אחד עבור היישום שלנו.

- דוגמה מעשית כיצד לשלב RAG ביישום.

## מטרות למידה

לאחר סיום השיעור, תוכלו:

- להסביר את החשיבות של RAG בשליפת נתונים ועיבודם.

- להגדיר יישום RAG ולעגן את הנתונים שלכם ל-LLM.

- לשלב בצורה יעילה את RAG ומאגרי נתונים וקטוריים ביישומי LLM.

## התרחיש שלנו: שיפור ה-LLM שלנו עם נתונים משלנו

בשיעור זה, אנו רוצים להוסיף את ההערות שלנו לסטארטאפ חינוכי, שמאפשר לצ'אטבוט לקבל מידע נוסף על נושאים שונים. באמצעות ההערות שיש לנו, הלומדים יוכלו ללמוד טוב יותר ולהבין את הנושאים השונים, מה שיקל עליהם להתכונן למבחנים. כדי ליצור את התרחיש שלנו, נשתמש ב:

- `Azure OpenAI:` ה-LLM שבו נשתמש כדי ליצור את הצ'אטבוט שלנו.

- `שיעור למתחילים על רשתות נוירונים:` זה יהיה הנתון שעליו נעגן את ה-LLM שלנו.

- `Azure AI Search` ו-`Azure Cosmos DB:` מאגר נתונים וקטורי לאחסון הנתונים שלנו וליצירת אינדקס חיפוש.

משתמשים יוכלו ליצור מבחני תרגול מההערות שלהם, כרטיסי חזרה וסיכומים תמציתיים. כדי להתחיל, בואו נבחן מה זה RAG וכיצד הוא עובד:

## יצירת תשובות מועשרות על בסיס מידע (RAG)

צ'אטבוט מבוסס LLM מעבד פניות משתמשים כדי ליצור תגובות. הוא נועד להיות אינטראקטיבי ומתקשר עם משתמשים במגוון רחב של נושאים. עם זאת, התגובות שלו מוגבלות להקשר שסופק ולנתוני האימון הבסיסיים שלו. לדוגמה, הידע של GPT-4 מוגבל לספטמבר 2021, כלומר, הוא חסר ידע על אירועים שהתרחשו לאחר תקופה זו. בנוסף, הנתונים ששימשו לאימון LLMs אינם כוללים מידע חסוי כמו הערות אישיות או מדריך מוצר של חברה.

### כיצד פועלים RAGs (יצירת תשובות מועשרות על בסיס מידע)

![שרטוט שמראה כיצד פועלים RAGs](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.he.png)

נניח שאתם רוצים לפרוס צ'אטבוט שיוצר מבחנים מההערות שלכם, תצטרכו חיבור לבסיס הידע. כאן נכנס לתמונה RAG. RAGs פועלים כך:

- **בסיס ידע:** לפני השליפה, יש להכניס ולעבד את המסמכים הללו, בדרך כלל על ידי פירוק מסמכים גדולים לחלקים קטנים יותר, הפיכתם להטמעות טקסט ואחסונם במאגר נתונים.

- **שאלת משתמש:** המשתמש שואל שאלה.

- **שליפה:** כאשר משתמש שואל שאלה, מודל ההטמעה שולף מידע רלוונטי מבסיס הידע שלנו כדי לספק יותר הקשר שישולב בפנייה.

- **יצירה מועשרת:** ה-LLM משפר את תגובתו על סמך הנתונים שנשלפו. זה מאפשר לתגובה שנוצרת להתבסס לא רק על נתוני האימון אלא גם על מידע רלוונטי מההקשר שנוסף. הנתונים שנשלפו משמשים להעשיר את תגובות ה-LLM. לאחר מכן ה-LLM מחזיר תשובה לשאלת המשתמש.

![שרטוט שמראה את הארכיטקטורה של RAGs](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.he.png)

הארכיטקטורה של RAGs מיושמת באמצעות טרנספורמרים המורכבים משני חלקים: מקודד ומפענח. לדוגמה, כאשר משתמש שואל שאלה, הטקסט הקלט 'מקודד' לווקטורים שתופסים את משמעות המילים והווקטורים 'מפוענחים' לאינדקס המסמכים שלנו ומייצרים טקסט חדש על סמך שאלת המשתמש. ה-LLM משתמש גם במודל מקודד-מפענח כדי ליצור את הפלט.

שתי גישות ליישום RAG לפי המאמר המוצע: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) הן:

- **_RAG-Sequence_** שימוש במסמכים שנשלפו כדי לחזות את התשובה הטובה ביותר לשאלת המשתמש.

- **RAG-Token** שימוש במסמכים כדי ליצור את הטוקן הבא, ואז לשלוף אותם כדי לענות על שאלת המשתמש.

### למה להשתמש ב-RAGs?

- **עושר מידע:** מבטיח שהתשובות הטקסטואליות יהיו עדכניות ומעודכנות. לכן, הוא משפר ביצועים במשימות ספציפיות לתחום על ידי גישה לבסיס הידע הפנימי.

- מפחית יצירת מידע שגוי על ידי שימוש ב**נתונים מאומתים** בבסיס הידע כדי לספק הקשר לשאלות המשתמשים.

- הוא **חסכוני** מכיוון שהם חסכוניים יותר בהשוואה להתאמה אישית של LLM.

## יצירת בסיס ידע

היישום שלנו מבוסס על הנתונים האישיים שלנו, כלומר, השיעור על רשתות נוירונים בתוכנית הלימודים של AI למתחילים.

### מאגרי נתונים וקטוריים

מאגר נתונים וקטורי, בניגוד למאגרי נתונים מסורתיים, הוא מאגר נתונים מיוחד שנועד לאחסן, לנהל ולחפש וקטורים מוטמעים. הוא מאחסן ייצוגים מספריים של מסמכים. פירוק נתונים להטמעות מספריות מקל על מערכת הבינה המלאכותית שלנו להבין ולעבד את הנתונים.

אנו מאחסנים את ההטמעות שלנו במאגרי נתונים וקטוריים מכיוון של-LLMs יש מגבלה על מספר הטוקנים שהם מקבלים כקלט. מכיוון שלא ניתן להעביר את כל ההטמעות ל-LLM, נצטרך לפרק אותן לחלקים וכאשר משתמש שואל שאלה, ההטמעות הדומות ביותר לשאלה יוחזרו יחד עם הפנייה. פירוק גם מפחית עלויות על מספר הטוקנים שעוברים דרך LLM.

כמה מאגרי נתונים וקטוריים פופולריים כוללים Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant ו-DeepLake. ניתן ליצור מודל Azure Cosmos DB באמצעות Azure CLI עם הפקודה הבאה:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### מטקסט להטמעות

לפני שנאחסן את הנתונים שלנו, נצטרך להמיר אותם להטמעות וקטוריות לפני שהם מאוחסנים במאגר הנתונים. אם אתם עובדים עם מסמכים גדולים או טקסטים ארוכים, תוכלו לפרק אותם על סמך השאלות שאתם מצפים. פירוק יכול להתבצע ברמת המשפט או ברמת הפסקה. מכיוון שפירוק נגזר ממשמעות המילים סביבן, תוכלו להוסיף הקשר נוסף לחלק, לדוגמה, על ידי הוספת כותרת המסמך או הכללת טקסט לפני או אחרי החלק. ניתן לפרק את הנתונים כך:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

לאחר הפירוק, נוכל להטמיע את הטקסט שלנו באמצעות מודלים שונים להטמעה. כמה מודלים שניתן להשתמש בהם כוללים: word2vec, ada-002 של OpenAI, Azure Computer Vision ועוד רבים. בחירת מודל לשימוש תלויה בשפות שבהן אתם משתמשים, בסוג התוכן המקודד (טקסט/תמונות/אודיו), בגודל הקלט שהוא יכול לקודד ובאורך הפלט של ההטמעה.

דוגמה לטקסט מוטמע באמצעות מודל `text-embedding-ada-002` של OpenAI היא:
![הטמעה של המילה חתול](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.he.png)

## שליפה וחיפוש וקטורי

כאשר משתמש שואל שאלה, המערכת ממירה אותה לווקטור באמצעות מקודד השאלות, ואז מחפשת באינדקס המסמכים שלנו וקטורים רלוונטיים במסמכים שקשורים לקלט. לאחר מכן, היא ממירה את הווקטור הקלט ואת וקטורי המסמכים לטקסט ומעבירה אותו דרך ה-LLM.

### שליפה

שליפה מתרחשת כאשר המערכת מנסה למצוא במהירות את המסמכים מהאינדקס שממלאים את קריטריוני החיפוש. מטרת השליפה היא להשיג מסמכים שישמשו לספק הקשר ולעגן את ה-LLM על הנתונים שלכם.

ישנן מספר דרכים לבצע חיפוש בתוך מאגר הנתונים שלנו כגון:

- **חיפוש לפי מילות מפתח** - משמש לחיפושי טקסט.

- **חיפוש סמנטי** - משתמש במשמעות הסמנטית של מילים.

- **חיפוש וקטורי** - ממיר מסמכים מטקסט לייצוגים וקטוריים באמצעות מודלים להטמעה. השליפה תתבצע על ידי שאילת המסמכים שייצוגיהם הווקטוריים קרובים ביותר לשאלת המשתמש.

- **היברידי** - שילוב של חיפוש לפי מילות מפתח וחיפוש וקטורי.

אתגר עם שליפה מתרחש כאשר אין תגובה דומה לשאלה במאגר הנתונים, המערכת תחזיר את המידע הטוב ביותר שהיא יכולה להשיג, עם זאת, ניתן להשתמש בטקטיקות כמו הגדרת המרחק המרבי לרלוונטיות או שימוש בחיפוש היברידי שמשלב גם מילות מפתח וגם חיפוש וקטורי. בשיעור זה נשתמש בחיפוש היברידי, שילוב של חיפוש וקטורי וחיפוש לפי מילות מפתח. נאחסן את הנתונים שלנו במסגרת נתונים עם עמודות המכילות את החלקים כמו גם את ההטמעות.

### דמיון וקטורי

המערכת תחפש בבסיס הידע הטמעות שקרובות זו לזו, השכן הקרוב ביותר, מכיוון שהן טקסטים שדומים. בתרחיש שבו משתמש שואל שאלה, היא קודם מוטמעת ואז מותאמת להטמעות דומות. המדידה הנפוצה שמשמשת כדי למצוא עד כמה וקטורים שונים דומים היא דמיון קוסינוס המבוסס על הזווית בין שני וקטורים.

ניתן למדוד דמיון באמצעות חלופות אחרות כמו מרחק אוקלידי שהוא הקו הישר בין נקודות הקצה של הווקטורים ומכפלה פנימית שמודדת את סכום המכפלות של האלמנטים המתאימים של שני וקטורים.

### אינדקס חיפוש

כאשר מבצעים שליפה, נצטרך לבנות אינדקס חיפוש עבור בסיס הידע שלנו לפני שנבצע חיפוש. אינדקס יאחסן את ההטמעות שלנו ויוכל לשלוף במהירות את החלקים הדומים ביותר גם במאגר נתונים גדול. ניתן ליצור את האינדקס שלנו באופן מקומי באמצעות:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### דירוג מחדש

לאחר ששאלתם את מאגר הנתונים, ייתכן שתצטרכו למיין את התוצאות מהכי רלוונטיות. LLM לדירוג מחדש משתמש בלמידת מכונה כדי לשפר את הרלוונטיות של תוצאות החיפוש על ידי סידורן מהכי רלוונטיות. באמצעות Azure AI Search, דירוג מחדש מתבצע אוטומטית עבורכם באמצעות דירוג סמנטי. דוגמה לאופן שבו דירוג מחדש עובד באמצעות שכנים קרובים:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## חיבור הכל יחד

השלב האחרון הוא הוספת ה-LLM שלנו לתהליך כדי לקבל תגובות שמבוססות על הנתונים שלנו. ניתן ליישם זאת כך:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## הערכת היישום שלנו

### מדדי הערכה

- איכות התגובות המסופקות, לוודא שהן נשמעות טבעיות, שוטפות ודומות לאנושיות.

- עיגון הנתונים: הערכת האם התגובה הגיעה מהמסמכים שסופקו.

- רלוונטיות: הערכת האם התגובה תואמת ומתקשרת לשאלה שנשאלה.

- שוטפות - האם התגובה הגיונית מבחינה דקדוקית.

## שימושים ל-RAG (יצירת תשובות מועשרות על בסיס מידע) ומאגרי נתונים וקטוריים

ישנם שימושים רבים שבהם קריאות פונקציה יכולות לשפר את היישום שלכם כמו:

- שאלות ותשובות: עיגון נתוני החברה שלכם לצ'אט שניתן להשתמש בו על ידי עובדים לשאול שאלות.

- מערכות המלצה: שבהן ניתן ליצור מערכת שמתאימה את הערכים הדומים ביותר, לדוגמה, סרטים, מסעדות ועוד.

- שירותי צ'אטבוט: ניתן לאחסן היסטוריית צ'אט ולהתאים אישית את השיחה על סמך נתוני המשתמש.

- חיפוש תמונות על בסיס הטמעות וקטוריות, שימושי כאשר עושים זיהוי תמונות וזיהוי חריגות.

## סיכום

כיסינו את התחומים הבסיסיים של RAG מהוספת הנתונים שלנו ליישום, שאלת המשתמש ופלט התשובה. כדי לפשט את יצירת RAG, ניתן להשתמש במסגרות כמו Semantic Kernel, Langchain או Autogen.

## משימה

כדי להמשיך ללמוד על יצירת תשובות מועשרות על בסיס מידע (RAG) תוכלו לבנות:

- לבנות ממשק קדמי ליישום באמצעות המסגרת לבחירתכם.

- להשתמש במסגרת, בין אם LangChain או Semantic Kernel, ולשחזר את היישום שלכם.

ברכות על סיום השיעור 👏.

## הלמידה לא עוצרת כאן, המשיכו במסע

לאחר סיום השיעור, בדקו את [אוסף הלמידה של AI גנרטיבי](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך ולהעמיק את הידע שלכם בבינה מלאכותית גנרטיבית!

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.