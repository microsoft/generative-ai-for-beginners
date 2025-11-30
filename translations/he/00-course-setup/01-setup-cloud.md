<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T17:56:27+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "he"
}
-->
# הגדרת ענן ☁️ – GitHub Codespaces

**השתמש במדריך הזה אם אתה לא רוצה להתקין כלום על המחשב שלך.**  
Codespaces נותן לך סביבת VS Code בדפדפן, עם כל התלויות מותקנות מראש – בחינם.

---

## 1.  למה Codespaces?

| יתרון | מה זה אומר בשבילך |
|---------|----------------------|
| ✅ בלי התקנות | עובד על Chromebook, iPad, מחשבי מעבדה בבית ספר… |
| ✅ מכולת פיתוח מוכנה מראש | Python 3, Node.js, .NET, Java כבר בפנים |
| ✅ מכסה חינמית | חשבונות אישיים מקבלים **120 שעות-ליבה / 60 שעות-GB בחודש** |

> 💡 **טיפ**  
> שמור על המכסה שלך על ידי **עצירה** או **מחיקה** של codespaces לא פעילים  
> (תפריט View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  צור Codespace (בלחיצה אחת)

1. **פצל** (Fork) את המאגר הזה (כפתור **Fork** למעלה מימין).  
2. במאגר שלך, לחץ **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![דיאלוג עם כפתורים ליצירת codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ חלון VS Code בדפדפן ייפתח והמכולה תתחיל להיבנות.
בפעם הראשונה זה לוקח **~2 דקות**.

## 3. הוסף את מפתח ה-API שלך (בצורה בטוחה)

### אפשרות א' – Codespaces Secrets — מומלץ

1. ⚙️ סמל גלגל שיניים -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. שם: OPENAI_API_KEY
3. ערך: הדבק את המפתח שלך → Add secret

וזהו—הקוד שלנו יזהה אותו אוטומטית.

### אפשרות ב' – קובץ .env (אם אתה ממש חייב)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

Certainly! Here is the translation to Hebrew:

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל טעויות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו המקורית כמקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנה או פירוש שגוי הנובעים מהשימוש בתרגום זה.