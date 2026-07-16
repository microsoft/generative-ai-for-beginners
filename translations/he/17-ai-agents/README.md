[![מודלים קוד פתוח](../../../translated_images/he/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## מבוא

סוכני בינה מלאכותית (AI Agents) מהווים פיתוח מרתק בתחום הבינה המלאכותית היוצרת, המאפשר למודלים שפתיים גדולים (LLMs) להתפתח מעוזרים לסוכנים המסוגלים לנקוט בפעולות. מסגרות סוכני AI מאפשרות למפתחים ליצור יישומים שנותנים ל-LLMs גישה לכלים ולניהול מצב. מסגרות אלו גם משפרות את השקיפות, ומאפשרות למשתמשים ולמפתחים לעקוב אחרי הפעולות שתוכננו על ידי ה-LLMs, ובכך משפרות את ניהול החוויה.

השיעור יעסוק בתחומים הבאים:

- הבנת מהו סוכן בינה מלאכותית - מה בעצם הוא סוכן AI?
- חקר חמש מסגרות סוכני AI שונות - מה מבדל אותן?
- יישום סוכני AI במקרים שונים - מתי כדאי להשתמש בסוכני AI?

## מטרות הלמידה

לאחר שתיקחו את השיעור, תוכלו:

- להסביר מה הם סוכני AI ואיך ניתן להשתמש בהם.
- להבין את ההבדלים בין כמה מהמסגרות הפופולריות לסוכני AI, וכיצד הן שונות.
- להבין כיצד פועלים סוכני AI על מנת לבנות יישומים איתם.

## מה הם סוכני AI?

סוכני AI הם תחום מרתק מאוד בעולם הבינה המלאכותית היוצרת. עם ההתלהבות הזאת לעיתים מופיעים בלבולים במונחים ובשימושם. על מנת לשמור על פשטות ולהיות כוללניים לרוב הכלים המתייחסים לסוכני AI, נשתמש בהגדרה הבאה:

סוכני AI מאפשרים למודלים שפתיים גדולים (LLMs) לבצע משימות על ידי מתן גישה ל**מצב** ו**כלים**.

![מודל סוכן](../../../translated_images/he/what-agent.21f2893bdfd01e6a.webp)

נבהיר את המונחים הבאים:

**מודלים שפתיים גדולים** - אלו הם המודלים המוזכרים לאורך הקורס כגון GPT-3.5, GPT-4, Llama-2 וכו'.

**מצב** - מתייחס להקשר שבו מודל השפה עובד. המודל משתמש בקונטקסט של פעולות העבר והקונטקסט הנוכחי, ומנחה את קבלת ההחלטות שלו בפעולות הבאות. מסגרות סוכני AI מאפשרות למפתחים לנהל את ההקשר הזה בקלות רבה יותר.

**כלים** - על מנת להשלים את המשימה שהמשתמש ביקש והמודל תכנן, המודל צריך גישה לכלים. דוגמאות לכלים יכולות להיות מסד נתונים, API, אפליקציה חיצונית או אפילו מודל שפה נוסף!

הגדרות אלו יעניקו לכם בסיס טוב להמשך בהתבוננות על יישומם. בואו נחקור כמה מסגרות שונות לסוכני AI:

## סוכני LangChain

[סוכני LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) הם מימוש של ההגדרות שסיפקנו לעיל.

לניהול ה**מצב**, משתמשים בפונקציה מובנית בשם `AgentExecutor`. זו מקבלת את ה`agent` שהוגדר וה`tools` הזמינים לו.

ה`Agent Executor` גם שומר את היסטוריית השיחות כדי לספק את הקונטקסט של השיחה.

![סוכני LangChain](../../../translated_images/he/langchain-agents.edcc55b5d5c43716.webp)

LangChain מציעה [קטלוג כלים](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) שניתן לייבא ליישום שלכם ולקבל דרכם גישה ל-LLM. כלים אלו נבנו על ידי הקהילה וצוות LangChain.

לאחר מכן ניתן להגדיר כלים אלו ולהעבירם ל`Agent Executor`.

שקיפות היא היבט חשוב נוסף כשמדברים על סוכני AI. חשוב שמפתחי יישומים יבינו איזה כלי ה-LLM משתמש ולמה. לשם כך, צוות LangChain פיתח את LangSmith.

## AutoGen

מסגרת סוכן ה-AI הבאה נדון בה היא [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). המוקד המרכזי ב-AutoGen הוא שיחות. הסוכנים גם **ניתנים לשיחה** וגם **ניתנים להתאמה אישית**.

**ניתנים לשיחה** - מודלים שפתיים גדולים יכולים לפתוח ולהמשיך שיחה עם מודל שפה נוסף על מנת להשלים משימה. הדבר נעשה על ידי יצירת `AssistantAgents` ומתן הודעת מערכת ספציפית להם.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**ניתנים להתאמה אישית** - סוכנים יכולים להיות מוגדרים לא רק כמודלים שפתיים אלא גם כמשתמש או ככלי. כמפתח, ניתן להגדיר `UserProxyAgent` שאחראי על אינטראקציה עם המשתמש לקבלת משוב להשלמת המשימה. משוב זה יכול להמשיך את ביצוע המשימה או לעצור אותה.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### מצב וכלים

לניהול ושינוי מצב, סוכן עוזר (Assistant Agent) מייצר קוד פייתון לביצוע המשימה.

לדוגמה של התהליך:

![AutoGen](../../../translated_images/he/autogen.dee9a25a45fde584.webp)

#### מודל שפה מוגדר עם הודעת מערכת

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

הודעת מערכת זו מכוונת את מודל השפה הספציפי אילו פונקציות רלוונטיות למשימה שלו. זכרו, עם AutoGen תוכלו להגדיר מספר AssistantAgents עם הודעות מערכת שונות.

#### משתמש מתחיל שיחה

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

הודעה זו מ`user_proxy` (אנושי) תתחיל את תהליך הסוכן לחקור את הפונקציות האפשריות שהוא צריך לבצע.

#### הפעלת פונקציה

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

לאחר עיבוד השיחה ההתחלתית, הסוכן ישלח את ההמלצה לקרוא לכלי. במקרה הזה, זו פונקציה בשם `get_weather`. בהתאם לקונפיגורציה, פונקציה זו יכולה להתבצע אוטומטית ולהיקרא על ידי הסוכן או להידרש הפעלה על ידי המשתמש.

תוכלו למצוא רשימת [דוגמאות קוד AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) להמשך חקר ופיתוח.

## מסגרת סוכנים של מיקרוסופט

[מסגרת סוכני מיקרוסופט](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) היא ערכת פיתוח קוד פתוח של מיקרוסופט לבניית סוכני AI ומערכות רב-סוכניות בשפות **Python** ו**.NET**. היא משלבת את היתרונות של שני פרויקטים קודמים של מיקרוסופט — תכונות הארגון של **Semantic Kernel** ואת תזמור הסוכנים הרבים של **AutoGen** — במסגרת אחת נתמכת. אם אתם מתחילים בפרויקט סוכן חדש היום, זו ההמלצה להמשיך במקום AutoGen.

המסגרת מתרחבת מסוכן שיחה יחיד ועד לזרימות עבודה מורכבות של סוכנים רבים, ומשתלבת ישירות עם Microsoft Foundry, Azure OpenAI, ו-OpenAI. היא גם מספקת תצפיות משולבות דרך OpenTelemetry כדי שתוכלו לעקוב בדיוק מה הסוכנים עושים.

### מצב וכלים

**מצב** - המסגרת מנהלת עבורכם את קונטקסט השיחה דרך **תפריטים** (threads). הסוכן עוקב אחר היסטוריית ההודעות (בקשות משתמש, קריאות לכלים ותוצאותיהם), כך שכל סיבוב מתבסס על הקודמים. ניתן גם לשמור תפריטים כדי להשהות ולהמשיך שיחה מאוחר יותר.

**כלים** - אתם מספקים לסוכן כלים על ידי העברת פונקציות פייתון רגילות. פרמטרים עם טיפוס מועברים אוטומטית לסכימה, כך שהמודל יודע מתי ואיך לקרוא להם (קריאת פונקציות). המסגרת גם תומכת בשרתים של Model Context Protocol (MCP) וכלים מתארחים כמו פרשן קוד.

כאן דוגמה לסוכן יחיד עם כלי מותאם אישי:

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

כדי להתחבר ל-Azure OpenAI ב-Microsoft Foundry במקום זאת, העבירו את נקודת הסיום ואישורי הגישה ללקוח:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### זרימות עבודה עם סוכנים מרובים

היתרון האמיתי של המסגרת הוא התזמור של כמה סוכנים יחד. לדוגמה, ניתן להריץ סוכנים בזה אחר זה (כאשר כל אחד מעביר את הקונטקסט לסוכן הבא) או לפצל לסוכנים רבים במקביל ולרכז את התוצאות שלהם:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# הרץ סוכנים ברצף, מעביר את הקשר של השיחה לאורך השרשרת
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# פזר אל הסוכנים במקביל, ואז אסוף את התגובות שלהם
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

להתקין את המסגרת ולהתחיל:

```bash
pip install agent-framework-core
# אינטגרציות אופציונליות
pip install agent-framework-openai       # OpenAI ו-Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

אפשר לחקור עוד ב[מאגר מסגרת הסוכנים של מיקרוסופט](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) וב[תיעוד הרשמי](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

מסגרת הסוכן הבאה שנחקור היא [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). היא ידועה כסוכן "קוד-קודם" מאחר שבמקום לעבוד רק עם `strings`, היא יכולה לעבוד עם DataFrames בפייתון. זה מאוד שימושי לניתוח ויצירת נתונים, לדוגמה יצירת גרפים, טבלאות או יצירת מספרים אקראיים.

### מצב וכלים

לניהול מצב השיחה, TaskWeaver משתמש ב"רעיון" של `Planner`. ה`Planner` הוא מודל שפה גדול שלוקח את הבקשה מהמשתמשים וממפה את המשימות שצריך להשלים כדי למלא את הבקשה.

כדי להשלים את המשימות, ה`Planner` נגיש לאוסף כלים הנקראים `Plugins`. אלה יכולים להיות מחלקות פייתון או פרשן קוד כללי. תוספים אלו נשמרים כמטבעות (embeddings) כך שהמודל יכול לחפש טוב יותר את התוסף הנכון.

![Taskweaver](../../../translated_images/he/taskweaver.da8559999267715a.webp)

הנה דוגמה לתוסף לניהול גילוי חריגות:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

הקוד מאומת לפני ההפעלה. תכונה נוספת לניהול הקונטקסט ב-Taskweaver היא `experience`. Experience מאפשר לאחסן את הקונטקסט של שיחה לאורך זמן בקובץ YAML. ניתן להגדיר זאת כך שהמודל ישתפר עם הזמן במשימות מסוימות בעלי גישה לשיחות קודמות.

## JARVIS

המסגרת הסופית שנחקור היא [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). מה שמייחד את JARVIS הוא שהוא משתמש במודל שפה לנהל את `המצב` של השיחה, ו`הכלים` הם מודלים של AI אחרים. כל אחד מהמודלים מיוחד לביצוע משימות מסוימות כגון זיהוי עצמים, תמלול או כיתוב תמונות.

![JARVIS](../../../translated_images/he/jarvis.762ddbadbd1a3a33.webp)

מודל השפה, כמכלול כללי, מקבל את הבקשה מהמשתמש ומזהה את המשימה הספציפית וכל ארגומנטים/נתונים הדרושים להשלמת המשימה.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

מודל השפה מעצב את הבקשה בצורה שהמודל המיוחד יכול לפרש, כמו JSON. לאחר שהמודל המיוחד הוחזר עם התחזית שלו בהתבסס על המשימה, מודל השפה מקבל את התגובה.

אם יש צורך במספר מודלים להשלמת המשימה, הוא גם מפרש את התגובות מהם לפני שאיגד אותם ליצירת התגובה למשתמש.

הדוגמה למטה מראה איך זה יעבוד כאשר משתמש מבקש תיאור וספירת עצמים בתמונה:

## משימה

להמשך למידה על סוכני AI תוכלו לבנות עם מסגרת הסוכנים של מיקרוסופט:

- אפליקציה המדמה ישיבת עסקים עם מחלקות שונות של סטארטאפ חינוכי.
- צרו הודעות מערכת שמנחות את ה-LLM להבין פרסונות שונות ועדיפויות, ומאפשרות למשתמש להציג רעיון מוצר חדש.
- לאחר מכן על ה-LLM להפיק שאלות המשך מכל מחלקה לשיפור והעמקת ההצעה ורעיון המוצר.

## הלמידה לא נגמרת כאן, המשיכו במסע

לאחר שתסיימו את השיעור, בדקו את [אוסף הלמידה של בינה מלאכותית יוצרת](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך להעשיר את הידע שלכם בתחום!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->