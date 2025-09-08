<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T15:42:35+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "mr"
}
-->
# क्लाउड सेटअप ☁️ – GitHub Codespaces

**हा मार्गदर्शक वापरा जर तुम्हाला स्थानिकपणे काहीही इन्स्टॉल करायचे नसेल.**  
Codespaces तुम्हाला एक मोफत, ब्राउझर-आधारित VS Code इन्स्टन्स देते ज्यामध्ये सर्व आवश्यक गोष्टी आधीच इन्स्टॉल केलेल्या असतात.

---

## 1.  Codespaces का वापरावे?

| फायदा | तुमच्यासाठी याचा अर्थ |
|---------|----------------------|
| ✅ शून्य इन्स्टॉल | Chromebook, iPad, शाळेतील PC… सर्वत्र चालते |
| ✅ आधीच तयार केलेले dev container | Python 3, Node.js, .NET, Java आधीच उपलब्ध |
| ✅ मोफत कोटा | वैयक्तिक खात्यांना **प्रति महिना १२० कोर-तास / ६० जीबी-तास** मिळतात |

> 💡 **टीप**  
> तुमचा कोटा चांगला ठेवण्यासाठी निष्क्रिय codespaces **थांबवा** किंवा **डिलीट** करा  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Codespace तयार करा (फक्त एक क्लिक)

1. **Fork** करा हे repo (वरच्या उजव्या बाजूला **Fork** बटण).  
2. तुमच्या fork मध्ये, **Code ▸ Codespaces ▸ Create codespace on main** वर क्लिक करा.  
   ![Codespace तयार करण्यासाठी बटणांचे डायलॉग](../../../00-course-setup/images/who-will-pay.webp)

✅ एक ब्राउझर VS Code विंडो उघडेल आणि dev container तयार होऊ लागेल.
पहिल्यांदा याला **~२ मिनिटे** लागतात.

## 3. तुमची API key जोडा (सुरक्षित मार्ग)

### पर्याय A Codespaces Secrets — शिफारस केलेले

1. ⚙️ गियर आयकॉन -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. नाव: OPENAI_API_KEY
3. मूल्य: तुमची key पेस्ट करा → Add secret

बस्स—आपला कोड ती आपोआप ओळखेल.

### पर्याय B .env फाइल (जर खरोखरच गरज असेल तर)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**अस्वीकरण**:
हे दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अपूर्णता असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानावा. अत्यावश्यक माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.