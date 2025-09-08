<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T15:22:57+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "hi"
}
-->
# क्लाउड सेटअप ☁️ – GitHub Codespaces

**इस गाइड का इस्तेमाल करें अगर आप कुछ भी लोकली इंस्टॉल नहीं करना चाहते।**  
Codespaces आपको एक फ्री, ब्राउज़र-बेस्ड VS Code इंस्टेंस देता है जिसमें सभी dependencies पहले से इंस्टॉल होती हैं।

---

## 1.  Codespaces क्यों?

| फ़ायदा | आपके लिए इसका मतलब |
|---------|----------------------|
| ✅ कोई इंस्टॉल नहीं | Chromebook, iPad, स्कूल लैब PCs पर भी चलता है… |
| ✅ पहले से बना हुआ dev container | Python 3, Node.js, .NET, Java पहले से मौजूद हैं |
| ✅ फ्री कोटा | पर्सनल अकाउंट्स को **120 कोर-घंटे / 60 GB-घंटे हर महीने** मिलते हैं |

> 💡 **टिप**  
> अपना कोटा बचाने के लिए **idle codespaces को रोकें या डिलीट करें**  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Codespace बनाएं (सिर्फ एक क्लिक में)

1. **Fork** करें इस repo को (ऊपर दाईं ओर **Fork** बटन)।  
2. अपने fork में, **Code ▸ Codespaces ▸ Create codespace on main** पर क्लिक करें।  
   ![कोडस्पेस बनाने के लिए बटन दिखाने वाला डायलॉग](../../../00-course-setup/images/who-will-pay.webp)

✅ एक ब्राउज़र VS Code विंडो खुलेगी और dev container बनना शुरू होगा।
पहली बार इसमें **~2 मिनट** लग सकते हैं।

## 3. अपना API key जोड़ें (सुरक्षित तरीका)

### विकल्प A Codespaces Secrets — सुझाया गया

1. ⚙️ गियर आइकन -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Name: OPENAI_API_KEY
3. Value: अपना key पेस्ट करें → Add secret

बस हो गया—हमारा कोड इसे खुद-ब-खुद ले लेगा।

### विकल्प B .env फाइल (अगर आपको सच में चाहिए)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**अस्वीकरण**:
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में ही प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।