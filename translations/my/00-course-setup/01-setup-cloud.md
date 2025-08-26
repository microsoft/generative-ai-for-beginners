<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T19:54:19+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "my"
}
-->
# Cloud Setup ☁️ – GitHub Codespaces

**တစ်ခုခုကို ကိုယ်ပိုင်ကွန်ပျူတာမှာ တင်သွင်းချင်မယ်ဆိုရင် ဒီလမ်းညွှန်ကို အသုံးပြုပါ။**  
Codespaces က သင့် browser မှာ အခမဲ့ VS Code ကို အသုံးပြုနိုင်ပြီး လိုအပ်တဲ့ dependency တွေ အားလုံးကို ကြိုတင်တပ်ဆင်ထားပါတယ်။

---

## 1.  Codespaces ကို ဘာကြောင့် အသုံးပြုသင့်လဲ?

| အကျိုးအမြတ် | သင့်အတွက် ဘာအဓိပ္ပါယ်ရှိသလဲ |
|-------------|------------------------------|
| ✅ တင်သွင်းစရာမလို | Chromebook, iPad, ကျောင်း lab PC တွေမှာတောင် အလုပ်လုပ်နိုင် |
| ✅ ကြိုတင်တည်ဆောက်ထားတဲ့ dev container | Python 3, Node.js, .NET, Java အားလုံးပါဝင်ပြီးသား |
| ✅ အခမဲ့ quota | ကိုယ်ပိုင်အကောင့်တွေမှာ **လစဉ် 120 core-hour / 60 GB-hour** ရရှိနိုင် |

> 💡 **Tip**  
> သင့် quota ကို ကောင်းစွာ ထိန်းသိမ်းဖို့ **အလုပ်မလုပ်တဲ့ codespace တွေကို ရပ်** သို့မဟုတ် **ဖျက်** လိုက်ပါ  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Codespace တစ်ခု ဖန်တီးရန် (တစ်ချက်တည်းနဲ့)

1. ဒီ repo ကို **Fork** လုပ်ပါ (အပေါ်ညာဘက် **Fork** ခလုတ်ကို နှိပ်ပါ)။  
2. သင့် fork မှာ **Code ▸ Codespaces ▸ Create codespace on main** ကို နှိပ်ပါ။  
   ![ialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Browser VS Code window တစ်ခု ဖွင့်ပြီး dev container ကို တည်ဆောက်ဖို့ စတင်ပါလိမ့်မယ်။
ပထမဆုံးအကြိမ်မှာ **~၂ မိနစ်** လောက် ကြာနိုင်ပါတယ်။

## 3. သင့် API key ကို ထည့်ပါ (လုံခြုံတဲ့နည်း)

### Option A Codespaces Secrets — အကြံပြုထားသောနည်း

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Name: OPENAI_API_KEY
3. Value: သင့် key ကို paste လုပ်ပြီး → Add secret

ပြီးပါပြီ—ကျွန်ုပ်တို့ရဲ့ code က အလိုအလျောက် သုံးသွားပါလိမ့်မယ်။

### Option B .env file (တကယ်လိုအပ်ရင်သာ)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းသည် မူလဘာသာစကားဖြင့် အာဏာပိုင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာနိုင်သော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။