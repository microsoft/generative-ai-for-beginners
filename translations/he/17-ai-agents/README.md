[![דגמי קוד פתוח](../../../translated_images/he/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## מבוא

סוכני בינה מלאכותית מייצגים התפתחות מרתקת בתחום האינטליגנציה הגנרטיבית, ומאפשרים למודלים לשוניים גדולים (LLMs) להתפתח מסייעים לסוכנים שיכולים לבצע פעולות. מסגרות סוכן AI מאפשרות למפתחים ליצור יישומים שנותנים ל-LLMs גישה לכלים ולניהול מצב. מסגרות אלו גם משפרות את הנראות, ומאפשרות למשתמשים ומפתחים לעקוב אחר הפעולות שתוכננו על ידי ה-LLMs, ובכך לשפר את ניהול החוויה.

השיעור יכלול את התחומים הבאים:

- הבנת מהו סוכן AI - מה בדיוק הוא סוכן AI?
- חקר חמש מסגרות סוכן AI שונות - מה מייחד כל אחת מהן?
- יישום סוכנים אלו למקרים שימוש שונים - מתי כדאי להשתמש בסוכני AI?

## מטרות הלמידה

לאחר שיעור זה, תוכלו:

- להסביר מה הם סוכני AI וכיצד ניתן להשתמש בהם.
- להבין את ההבדלים בין חלק ממסגרות סוכן AI הפופולריות, וכיצד הן שונות.
- להבין כיצד סוכני AI פועלים כדי לבנות יישומים איתם.

## מהו סוכן AI?

סוכני AI הם תחום מאוד מרגש בעולם האינטליגנציה הגנרטיבית. עם ההתרגשות הזו לעיתים מגיע בלבול לגבי המונחים והשימוש בהם. כדי להישאר פשוטים ולכלול את רוב הכלים המתייחסים לסוכני AI, נשתמש בהגדרה הבאה:

סוכני AI מאפשרים למודלים לשוניים גדולים (LLMs) לבצע משימות על ידי מתן גישה ל**מצב** ו**כלים**.

![מודל סוכן](../../../translated_images/he/what-agent.21f2893bdfd01e6a.webp)

נבהיר את המונחים הללו:

**מודלים לשוניים גדולים** – אלו המודלים שמוזכרים בכל הקורס כמו GPT-5, GPT-4o, ולמה 3.3 וכדומה.

**מצב** – מתייחס להקשר שבו עובד ה-LLM. ה-LLM משתמש בהקשר של פעולות העבר שלו ובהקשר הנוכחי, שמנחה את קבלת ההחלטות שלו לגבי פעולות עתידיות. מסגרות סוכן AI מאפשרות למפתחים לנהל הקשר זה בצורה קלה יותר.

**כלים** – כדי להשלים את המשימה שהמשתמש ביקש וה-LLM תכנן, ה-LLM צריך גישה לכלים. כמה דוגמאות לכלים יכולות להיות מסד נתונים, API, יישום חיצוני או אפילו מודל LLM אחר!

ההגדרות הללו בתקווה יתנו לכם בסיס טוב להמשך כשנסתכל כיצד הם מיושמים. בואו נחקור כמה מסגרות סוכן AI שונות:

## סוכני LangChain

[סוכני LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) הם מימוש של ההגדרות שסיפקנו למעלה.

לניהול **המצב**, הוא משתמש בפונקציה מובנית שנקראת `AgentExecutor`. פונקציה זו מקבלת את ה`agent` שהוגדר ואת ה`tools` הזמינים לו.

ה`Agent Executor` גם שומר את היסטוריית השיחה כדי לספק את ההקשר של השיחה.

![סוכני Langchain](../../../translated_images/he/langchain-agents.edcc55b5d5c43716.webp)

LangChain מציעה [קטלוג של כלים](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) שניתן לייבא ליישום שלכם ושה-LLM יכול לקבל גישה אליהם. כלים אלו נעשים על ידי הקהילה ועל ידי צוות LangChain.

לאחר מכן ניתן להגדיר כלים אלו ולעבור אותם ל`Agent Executor`.

נראות היא היבט חשוב נוסף כשמדברים על סוכני AI. חשוב שמפתחי היישום יבינו איזה כלי ה-LLM משתמש ומדוע. לצורך זה, צוות LangChain פיתח את LangSmith.

## AutoGen

מסגרת סוכן AI הבאה שנדון בה היא [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). המוקד המרכזי של AutoGen הוא שיחות. סוכנים הם גם **ניתני שיחה** וגם **ניתני התאמה אישית**.

**ניתני שיחה -** LLMs יכולים להתחיל ולהמשיך שיחה עם LLM אחר כדי להשלים משימה. זה נעשה על ידי יצירת `AssistantAgents` ומתן הודעת מערכת ספציפית להם.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**ניתני התאמה אישית** - סוכנים יכולים להיות מוגדרים לא רק כלוקחים תפקיד LLM אלא גם להיות משתמש או כלי. כמפתח, ניתן להגדיר `UserProxyAgent` האחראי על אינטראקציה עם המשתמש לקבלת משוב בהשלמת משימה. המשוב הזה יכול להמשיך בביצוע המשימה או לעצור אותה.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### מצב וכלים

כדי לשנות ולנהל את המצב, סוכן העוזר מייצר קוד פייתון כדי להשלים את המשימה.

הנה דוגמה לתהליך:

![AutoGen](../../../translated_images/he/autogen.dee9a25a45fde584.webp)

#### LLM מוגדר עם הודעת מערכת

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

הודעת מערכת זו ממקדת את ה-LLM הספציפי לאילו פונקציות רלוונטיות למשימה שלו. זכור, עם AutoGen אתה יכול להגדיר מספר AssistantAgents עם הודעות מערכת שונות.

#### השיחה מתחילה על ידי המשתמש

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

הודעה זו מה-user_proxy (אדם) היא שתתחיל את תהליך הסוכן לחקור את הפונקציות האפשריות שעליו לבצע.

#### פונקציה מבוצעת

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

לאחר שהשיחה הראשונית מעובדת, הסוכן ישלח את הכלי המוצע לקריאה. במקרה זה, זו פונקציה בשם `get_weather`. בהתאם להגדרתך, פונקציה זו יכולה להתבצע אוטומטית ולהיקרא על ידי הסוכן או להתבצע על בסיס קלט המשתמש.

ניתן למצוא רשימה של [דוגמאות קוד AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) להמשך חקירה כיצד להתחיל לבנות.

## מסגרת סוכנים של מיקרוסופט

[מסגרת סוכנים של מיקרוסופט](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) היא SDK קוד פתוח של מיקרוסופט לבניית סוכני AI ומערכות רב-סוכנים ב**Python** ו-**.NET**. היא מחברת יחד את חוזקות שני פרויקטים קודמים של מיקרוסופט — תכונות ארגוניות של **Semantic Kernel** והאורקסטרציה של סוכנים מרובים של **AutoGen** — למסגרת אחת נתמכת. אם אתם מתחילים פרויקט סוכן חדש היום, זו ההמלצה להמשך ל-AutoGen.

המסגרת מתרחבת מסוכן שיחה בודד ועד לזרימות עבודה מורכבות של סוכנים מרובים, ומשלבת ישירות עם Microsoft Foundry, Azure OpenAI, ו-OpenAI. היא גם מספקת נראות משולבת דרך OpenTelemetry כך שתוכלו לעקוב בדיוק אחר מה שהסוכנים שלכם עושים.

### מצב וכלים

**מצב** – המסגרת מנהלת את הקשר של השיחה בשבילכם דרך **שרשורים**. סוכן שומר על היסטוריית ההודעות (בקשות משתמש, קריאות לכלים ותוצאותיהם), כך שכל סבב מתבסס על הקודמים. השרשורים גם יכולים להיות מתועדים, מה שמאפשר לשיחה לעצור ולהמשיך מאוחר יותר.

**כלים** – אתם נותנים לסוכן כלים על ידי העברת פונקציות פייתון פשוטות. פרמטרים עם הערות טיפוס מתורגמים אוטומטית לסכימה, כך שהמודל יודע מתי ואיך לקרוא להן (קריאת פונקציה). המסגרת גם תומכת בשרתי Model Context Protocol (MCP) וכלים מתארחים כמו מתרגם קוד.

הנה דוגמה לסוכן יחיד עם כלי מותאם אישית:

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

לחיבור ל-Azure OpenAI ב-Microsoft Foundry במקום זאת, העבירו את נקודת הקצה והאישורים ללקוח:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### זרימות עבודה רב-סוכניות

איפה שהמסגרת באמת בולטת הוא בתיאום מספר סוכנים יחד. לדוגמה, ניתן להריץ סוכנים אחד אחרי השני (כאשר כל אחד מעביר את ההקשר שלו לסוכן הבא) או לפצל למספר סוכנים במקביל ולרכז את תוצאותיהם:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# הפעל סוכנים ברצף, תוך העברת הקשר השיחה לאורך השרשרת
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# פזר לסוכנים במקביל, ולאחר מכן אסוף את התגובות שלהם
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

להתקנת המסגרת ולהתחלה:

```bash
pip install agent-framework-core
# אינטגרציות אופציונליות
pip install agent-framework-openai       # OpenAI ו-Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

ניתן להעמיק עוד ב-[מאגר מסגרת הסוכנים של מיקרוסופט](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) וב-[התיעוד הרשמי](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

מסגרת הסוכן הבאה שנחקור היא [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). היא ידועה כסוכן "קוד-קודם" מכיוון שבמקום לעבוד רק עם מחרוזות (`strings`), היא יכולה לעבוד עם DataFrames בפייתון. זה הופך לשימושי מאוד לניתוח נתונים ומשימות יצירה. לדוגמה יצירת גרפים ותרשימים או יצירת מספרים אקראיים.

### מצב וכלים

כדי לנהל את מצב השיחה, TaskWeaver משתמשת במושג `Planner`. ה`Planner` הוא LLM שלוקח את הבקשה מהמשתמשים וממפה את המשימות שצריך להשלים כדי למלא את הבקשה.

כדי להשלים את המשימות, ה`Planner` נחשף לאוסף כלים הנקראים `Plugins`. אלו יכולים להיות מחלקות פייתון או מתרגם קוד כללי. תוספים אלו נשמרים כהטמעות (embeddings) כדי שה-LLM יוכל לחפש טוב יותר את התוסף הנכון.

![Taskweaver](../../../translated_images/he/taskweaver.da8559999267715a.webp)

הנה דוגמה לתוסף לטיפול בגילוי חריגות:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

הקוד מאומת לפני ביצוע. תכונה נוספת לניהול הקשר ב-Taskweaver היא ה`experience`. ה-Experience מאפשר לשמור את הקשר של שיחה לטווח ארוך בקובץ YAML. ניתן להגדיר זאת כך שה-LLM משתפר עם הזמן במשימות מסוימות בכך שהוא נחשף לשיחות קודמות.

## JARVIS

מסגרת הסוכן האחרונה שנחקור היא [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). מה שמייחד את JARVIS הוא שהיא משתמשת ב-LLM לניהול ה`state` של השיחה ושה`tools` הם מודלים AI אחרים. כל המודלים הם מודלים מומחים שמבצעים משימות מסוימות כמו זיהוי אובייקטים, התמלול או יצירת כותרות לתמונות.

![JARVIS](../../../translated_images/he/jarvis.762ddbadbd1a3a33.webp)

ה-LLM, בהיותו מודל כללי, מקבל את הבקשה מהמשתמש ומזהה את המשימה הספציפית ואת כל הטיעונים/הנתונים הדרושים להשלמת המשימה.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

ה-LLM מעצב את הבקשה בצורה שהמודל המומחה יכול לפרש, כגון JSON. לאחר שהמודל המומחה החזיר את התחזית שלו על פי המשימה, ה-LLM מקבל את התגובה.

אם נדרשים מספר מודלים להשלמת המשימה, ה-LLM גם יפרש את התגובה מהמודלים הללו לפני שיאחד אותם ליצירת תגובה למשתמש.

הדוגמה למטה מראה כיצד זה יעבוד כאשר משתמש מבקש תיאור וספירת האובייקטים בתמונה:

## משימה

להמשך הלמידה על סוכני AI, תוכלו לבנות עם מסגרת סוכני מיקרוסופט:

- יישום המדמה ישיבת עסקים עם מחלקות שונות בסטארטאפ חינוך.
- יצירת הודעות מערכת שמנחות את ה-LLM בהבנת פרסונות שונות ופריוריטטים ומאפשרות למשתמש להציע רעיון למוצר חדש.
- לאחר מכן, ה-LLM צריך ליצור שאלות המשך מכל מחלקה כדי לשפר ולחדד את ההצעה ואת הרעיון למוצר.

## הלמידה לא נעצרת כאן, המשיכו במסע

לאחר סיום שיעור זה, בדקו את [אוסף הלמידה של אינטיליגנציה גנרטיבית שלנו](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך ולשפר את הידע שלכם בתחום האינטליגנציה הגנרטיבית!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->