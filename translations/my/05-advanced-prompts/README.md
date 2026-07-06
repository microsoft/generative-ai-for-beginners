# အဆင့်မြင့် prompt များ ဖန်တီးခြင်း

[![Creating Advanced Prompts](../../../translated_images/my/05-lesson-banner.522610fd4a2cd82d.webp)](https://youtu.be/BAjzkaCdRok?si=NmUIyRf7-cDgbjtt)

မနောက်ကအခန်းက သင်ယူချက်အချို့ကို ပြန်လည်သုံးသပ်ကြရအောင်-

> Prompt _engineering_ ဆိုသည်မှာ မောက်ဒယ်အား ပိုဆန်းသစ်ပြီးသင့်တော်သော ဖြေကြားမှုများရရှိစေရန်အတွက် အသုံးဝင်သောညွှန်ကြားချက်များ သို့မဟုတ် ဆက်စပ်အကြောင်းအရာများ ပေးသည့်အတွက် မောက်ဒယ်အား လမ်းညွှန်ပေးခြင်းဖြစ်သည်။

Prompt များရေးသားခြင်းတွင် နှစ်ခြမ်းကို လုပ်ဆောင်ရမည်။ အနက် အတည် ပြု ဆက်စပ်တဲ့အကြောင်းအရာများ ပေးပြီး prompt ကို မူပိုင်တည်ဆောက်ခြင်းနှင့်၊ _optimization_ ဆိုသည်မှာ သေးသေးငယ်ငယ် အတိုင်းအတာများဖြင့် prompt ကို တဖြည်းဖြည်း တိုးတက်အောင်လုပ်ခြင်းဖြစ်သည်။

ယခုအချိန်တွင် prompt များရေးသားနည်းအခြေခံ သိရှိမှုရှိသော်လည်း နက်ရှိုင်းရန်လိုအပ်သည်။ ဤအခန်းတွင် သင်သည်အမျိုးမျိုးသော prompt များစမ်းသပ်ခြင်းမှ တစ်ဆင့် နောက်တစ်ခုထက်ပို၍ အဆင်ပြေကြောင်း သိရှိလာမည်ဖြစ်ပြီးအခြေခံနည်းလမ်းများကို LLM မည်သည့်အမျိုးအစားတွင်မဆို အသုံးပြုနိုင်ရန် prompt များကို တည်ဆောက်နည်းကို သင်ယူပါမည်။

## နိဒါန်း

ဤအခန်းတွင် အောက်ပါအကြောင်းအရာများကို ဖော်ပြပါမည်-

- prompt engineering ပိုမိုအကောင်းပြည့်စုံဖို့ နည်းလမ်းအမျိုးမျိုးကို သင်၏ prompt များသို့ အသုံးပြုခြင်း။
- အထွက်အလွတ်ကို မတူညီစေရန် သို႔မဟုတ် အတိအကျ ဖြစ်အောင် prompt များကို သတ်မှတ်ခြင်း။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာပြီးမြောက်ပြီးလျှင် အောက်ပါအရည်အချင်းများ ရရှိမည်။

- prompt အထွက်အတိုးတက်စေရန် prompt engineering နည်းလမ်းများ အသုံးပြုနိုင်ခြင်း။
- output ကို မတူညီစေရန် (varied) သို့မဟုတ် တိတိကျကျ ဖြစ်အောင် (deterministic) prompt ထုတ်နိုင်ခြင်း။

## Prompt engineering

Prompt engineering ဆိုသည်မှာ မျှော်မှန်းထားသော အထွက်ရရှိမည့် prompt များ ဖန်တီးခြင်း ဖြစ်သည်။ ပုံမှန် စာသား prompt မွတ်ပုံရေးခြင်းထက် ပို၍နက်ရှိုင်းပြီးနည်းရှာသုံးစွဲမှုတွေ ပါဝင်သည်။ Prompt engineering မှာ အင်ဂျင်နီယာနယ်ပညာတစ်ရပ်မဟုတ်ဘဲ သင်ရေးသားလိုသော အထွက်ရရှိရေးနည်းလမ်းတစ်စု ဖြစ်သည်။

### Prompt ၏ ဥပမာတစ်ခု

အောက်ပါ အခြေခံ prompt ကိုယူကြည့်ကြပါစို့-

> Generate 10 questions on geography.

ဒီ prompt တွင် prompt နည်းလမ်းအမျိုးမျိုးကို အသုံးပြုနေသည်။

အောက်ပါအတိုင်း ခွဲခြမ်းကြည့်မည်-

- **Context (ဆက်စပ်အကြောင်းအရာ)** - "geography" အကြောင်းဖြစ်ရန် သတ်မှတ်ထားသည်။
- **Output ကန့်သတ်ခြင်း** - တစ်ခုထက်မပိုသော ၁၀ ဆောင်းပါး ဖန်တီးရန် တောင်းဆိုထားသည်။

### ရိုးရှင်း prompt များ၏ ကန့်သတ်ချက်များ

စိတ်လိုနှစ်သက်သော အဖြေ မရနိုင်တတ်ပါ။ သင်၏ မေးခွန်းများ ဖန်တီးပေးမည်ဖြစ်သော်လည်း geography သည် ကြီးမားသော အကြောင်းအရာဖြစ်ကာ အောက်ပါအကြောင်းရင်းများကြောင့် သင့်လိုအပ်သလို မရနိုင်ပါ-

- **ကြီးမားသော သီအိုရီ** - ပင်လယ်ပြင်၊ မြို့တော်များ၊ မြစ်များ စသည်ဖြင့် အကြောင်းအရာ ရွေးချယ်ဖို့ မသိပါ။
- **ပုံစံ** - မေးခွန်းများကို သတ်မှတ်ထားသော ပုံစံမျိုးဖြင့် ဖန်တီးရန်လိုပါက နားလည်ရေးအခက်အခဲရှိနိုင်သည်။

prompt ဖန်တီးရာတွင် စဉ်းစားရမည့် အချက်များ များပြားပါသည်။

ယခုအချိန်အထိ ရိုးရှင်း prompt ၎င်းကိုမြင်ရပြီးတော့ဟုတ်သော်လည်း generative AI သည် လူအမျိုးမျိုး စွမ်းဆောင်ရည် (roles) နှင့် စီးပွားရေးကဏ္ဍ (industries) များအတွက် ပိုမိုအကျိုးရှိစေစွမ်းရည်ရှိသည်။ ကျွန်ုပ်တို့ အခြေခံ နည်းလမ်း အနည်းငယ်ကို အောက်တွင် စူးစမ်းကြည့်ပါမည်။

### Prompting နည်းလမ်းများ

ပထမဦးဆုံး၊ prompting သည် LLM ၏ _ဖော်ထုတ်လာသော_ လက္ခဏာ (emergent property) ဖြစ်ကြောင်းနားလည်ရမည်။ မှတ်သားစရာကတော့ မောက်ဒယ်တွင် ပါဝင်သည့် နောက်ခံဂုဏ်သတ္တိ မဟုတ်ပါ၊ မောက်ဒယ်ကိုသုံးစွဲရာတွင် တွေ့ရှိရသည့်အရာဖြစ်သည်။

LLM ကို prompt ပေးရာတွင် အသုံးပြုနိုင်သည့် အခြေခံနည်းလမ်းများ ရှိသည်။ အောက်တွင် လေ့လာကြပါစို့-

- **Zero-shot prompting** - အခြေခံ prompt ပုံစံဖြစ်သည်။ မောက်ဒယ်၏ ပြုလုပ်သည့် သင်ကြားမှုအချက်အလက်ပေါ် မူတည်၍ တစ်ခုသော prompt ဖြင့် ဖြေကြားမှုတောင်းဆိုခြင်း။
- **Few-shot prompting** - မပေါ်ပါသည့် လက်တွေ့ ဥပမာအနည်းငယ် ပေးပြီး မောက်ဒယ်အား ညွှန်ကြားမှု ပေးခြင်းဖြစ်သည်။
- **Chain-of-thought** - မောက်ဒယ်အား တစ်ဆင့်ချင်းစီ ပြဋ္ဌာန်းချက်များအဖြစ် ပြဌာန်းပြုစုရန် ပြောကြားခြင်း ဖြစ်သည်။
- **Generated knowledge** - prompt ဖြေကြားမှု ကောင်းမွန်စေရန်အတွက် မိမိတို့သိထားသည့် အချက်အလက်များကို ထည့်သွင်းပေးခြင်း။
- **Least to most** - chain-of-thought နှင့် ဆင်တူပြီး ပြဌာန်းချက်များကို အဆင့်လိုက် ခွဲခြမ်းပြီး အစဉ်လိုက် လုပ်ဆောင်ရန်တောင်းဆိုခြင်း။
- **Self-refine** - မောက်ဒယ်၏ ဖြေကြားမှုကို ပြန်လည် ဝေဖန်ပြီး တိုးတက်အောင် တောင်းဆိုခြင်း။
- **Maieutic prompting** - self-refine နှင့် ဆင်တူပြီး မောက်ဒယ်၏ ဖြေကြားချက်မှန်ကန်မှု ရှိ/မရှိကို စစ်ဆေးရန် ချဉ်းကပ်မှု။

### Zero-shot prompting

Бұл prompting စတိုင်သည် ရိုးရှင်းပြီး, တစ်ခါထဲမေးခွန်းတစ်ခုဖြစ်သည်။ ဒီနည်းလမ်းကို LLM တွေကို ဖြေချက်ရယူရာတွင် အသုံးပြုနေရသည်။ ဥပမာ-

- Prompt: "Algebra ဆိုတာ ဘာလဲ?"
- မြန်မာလိုအဖြေ: "Algebra သည် သင်္ကေတများနှင့် ဥပဒေများကို လေ့လာသော သင်္ချာခွဲတစ်ခုဖြစ်သည်။"

### Few-shot prompting

ဒီ prompting နည်းသည် မူတည်၍ တစ်ခုထက် ပိုများသော ဥပမာများကို အသုံးပြုပြီး ဖြေကြားမှုရရှိအောင် ညွှန်ကြားသည်။ တစ်ခုသော prompt နှင့် အုပ်စုအမည်အတူ တောင်းဆိုမှုပါဝင်သည်။ ဥပမာ-

- Prompt: "Shakespeare စကားပုံစံဖြင့် ကဗျာတစ်ပုဒ်ရေးပါ။ Shakespearean sonnets အနည်းငယ် ထည့်သွင်းပေးထားသည်။
  Sonnet 18: 'ဘာသာရပ်သည် နွေရာသီနေ့တစ်နေ့ထို့နဲ့ နှိုင်းယှဉ်သင့်သလား? သင်သည် ပိုမိုလှပ၍ ပိုမိုသဘာဝလွှမ်းမိုးသည်...'
  Sonnet 116: 'တကယ်တမ်းစိတ်နှင့် မထိန်းညှိမှုမရှိ ဖျက်ပစ်ခြင်းမရှိမှုကို သတိပြုပါ...'
  Sonnet 132: 'သင့်မျက်လုံးများကို ချစ်သည်၊ ရိုသေမှုရှိသည်၊ စိတ်ရင်းနှလုံးသည် နာကျင်ရာ သွေးလိမ့်သည်...'
  အခုလောလောဆယ်ကို လကိုအလှပဆုံးအကြောင်းပါ ရေးပါ။"
- မြန်မာလို အဖြေ: "ကောင်းကင်ပေါ်တွင် လရောင်က စကာတော်ယှဉ်ကြည့်စေသည်၊ ကြွယ်ဝသော မီးခိုးရောင်ဖြင့် သက်တမ်းပေးသည်..."

ဥပမာများက မောက်ဒယ်အား ဆက်စပ်ချက်၊ ပုံစံ၊ စတိုင်ကို ရှင်းလင်းစေရန် အထောက်အကူဖြစ်သည်။

### Chain-of-thought

chain-of-thought နည်းလမ်းသည် LLM ကို အဆင့်လိုက် ခြေလှမ်းများ ဖြတ်သန်းစေခြင်းဖြစ်သည်။ ထိုနည်းလမ်းဖြင့် မောက်ဒယ်အား အဆင့်လိုက်လုပ်ဆောင်နည်းကို သင်ကြားပေးနိုင်သည်။ ဥပမာ- chain-of-thought မပါ၊ ပါ နှိုင်းယှဉ်ကြည့်ပါ-

    - Prompt: "Alice ရဲ့ပန်းသီး ၅ လုံးရှိသည်၊ ၃ လုံး ပစ်ပြီး၊ Bob ကို ၂ လုံးပေးပြီး၊ Bob က ၁ လုံးပြန်ပေးပါတယ်၊ Alice ရဲ့ ပန်းသီးလက်ကျန် ဘယ်လောက်လဲ?"
    - အဖြေ: ၅

 LLm သည် ၅ ဟု ဖြေသည်။ မှားသည်။ မှန်ကန်သောဖြေ၀ှယ်မှာ ပန်းသီး ၁ လုံး (5 -3 -2 +1 =1) ဖြစ်သည်။

 မောက်ဒယ်အား တိကျမှန်ကန်စွာ လေ့လာစေဖို့ မည်သို့သင်ကြားမလဲ?

 Chain-of-thought ကို အသုံးပြုမယ်ဆိုရင်- 

1. မောက်ဒယ်အား နမူနာတစ်ခု ပေးသည်။
2. တွက်ချက်မှု နမူနာတွင် မှန်ကန်စွာပြသည်။
3. မူလ prompt ကို ထပ်မံပေးသည်။

ဥပမာ-

- Prompt: "Lisa ရဲ့ပန်းသီး ၇ လုံးရှိသည်၊ ၁ လုံးပစ်ပြီး၊ Bart ကို ၄ လုံးပေးပြီး၊ Bart က ၁ လုံးပြန်ပေးသည်။
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice ရဲ့ပန်းသီး ၅ လုံးရှိသည်၊ ၃ လုံး ပစ်ပြီး၊ Bob ကို ၂ လုံးပေးပြီး၊ Bob က ၁ လုံးပြန်ပေးသည်၊ ဘယ်လောက်လဲ?"
  အဖြေ: 1

 ဒီလိုနဲ့ နမူနာနဲ့ တွက်ချက်ခြင်းပြပြီး သင်ချင်း တိုက်ရိုက်အဖြေကို ရနိုင်ပြီ။

 Chain-of-thought က သက်ကြီး အားလုံးအတွက် အရှိန်အဟုန်ကြီးသောနည်းလမ်းဖြစ်သည်။

### Generated knowledge

မကြာခဏ prompt ဖန်တီးသောအခါမှာ မိမိကုမ္ပဏီ၏ ဒေတာများကို အသုံးပြုလိုသည်။ prompt ၏ တစ်စိတ်တစ်ပိုင်းမှာ ကုမ္ပဏီ၏အချက်အလက်ဖြစ်ရမည်မို့ အခြားပိုင်းမှာ သငျ့တင်သည့် prompt ဖြစ်ရမည်။

ဥပမာ- အာမခံလုပ်ငန်းတွင်ရှိလျှင်-

```text
{{company}}: {{company_name}}
{{products}}:
{{products_list}}
Please suggest an insurance given the following budget and requirements:
Budget: {{budget}}
Requirements: {{requirements}}
```

 အထက်ပါလို ဗဗာစတမ်းဖြင့် prompt ဖန်တီးထားသည်။ template ၌ `{{variable}}` ဟု ဖြစ်သော အမျိုးအစားများ ပါရှိကာ ကုမ္ပဏီ API မှတဆင့် အမှန်တကယ် ဒေတာထိုးထားသည်။

ကုမ္ပဏီဒေတာဖြင့် variable များ ဖြည့်စွက်ပြီး သင်၏ prompt ကို လိုသလို ဖန်တီးနိုင်သည်-

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- Car, cheap, 500 USD
- Car, expensive, 1100 USD
- Home, cheap, 600 USD
- Home, expensive, 1200 USD
- Life, cheap, 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000
Requirements: Car, Home, and Life insurance
```

 ဒီ prompt ကို LLM တွင် အတွင်းခံပြေးလိုက်လျှင် အောက်ပါ အဖြေကိုရမည်။

```output
Given the budget and requirements, we suggest the following insurance package from ACME Insurance:
- Car, cheap, 500 USD
- Home, cheap, 600 USD
- Life, cheap, 100 USD
Total cost: $1,200 USD
```

 Life insurance ကိုလည်း အကြံပြုသော်လည်း မသင့်တော်ပါ။ ၎င်းသည် prompt  ကို ပိုမိုရှင်းလင်းစေဖို့လိုပါသည်။ _trial and error_ ဖြင့် အောက်ပါ prompt ကို ရရှိခဲ့သည်။

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- type: Car, cheap, cost: 500 USD
- type: Car, expensive, cost: 1100 USD
- type: Home, cheap, cost: 600 USD
- type: Home, expensive, cost: 1200 USD
- type: Life, cheap, cost: 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000 restrict choice to types: Car, Home
```

 _type_ နဲ့ _cost_ ကို ထည့်သွင်းပြီး restriction keyword ကို အသုံးပြုခြင်းဖြင့် LLM တွင် ဘာလိုချင်သည်ဆိုတာ သဘောပေါက်စေသည်။

အခုရရှိသော အဖြေမှာ-

```output
Given the budget and requirements, we suggest the Car, Cheap insurance product which costs 500 USD per month.
```

 ဤဥပမာသည် _generated knowledge_ တို့ကဲ့သို့သော နည်းများ အသုံးပြုနေသော် လည်း prompt ကို အနည်းငယ် တိုးတက်အောင် ပြင်ဆင်ရသောကိစ္စ ရှိကြောင်း ဖေါ်ပြသည်။

### Least-to-most

Least-to-most prompting တွင် ချင်းကြီး မမြုတ် ချင်းလေးများသို့ ခွဲခြမ်းပြီး LLM ကို နယူးအဆင့်တိုင်းဆက်လက် ဖြေရှင်းရန် ညွှန်ကြားသည်။ ဥပမာအနေဖြင့် ဒေတာ သိပ္ပံလုပ်ငန်းတွင်-

> Prompt: ဒေတာ သိပ္ပံ အဆင့် ၅ ချက်ဖြင့် မည်ကဲ့သို့ ဆောင်ရွက်မည်နည်း?

 AI အကူအညီဖြင့်-

1. ဒေတာ စုဆောင်းခြင်း
1. ဒေတာ သန့်ရှင်းခြင်း
1. ဒေတာ ဆန်းစစ်ခြင်း
1. ဒေတာ ရိုက်နှိပ်ခြင်း
1. ဒေတာ တင်ပြခြင်း

### Self-refine, ဖြေဆိုမှုကို ဝေဖန်ခြင်း

Generative AI နှင့် LLM များသည် အထွက်ကို မယုံကြည်ရပေ။ ထိုအထွက်သည် မှန်ကန်မှုမဟုတ်ဘဲ ဆက်လက်ဖြေကြားနိုင်သော နောက်တစ်ခုထပ်ဖြေဆိုခြင်း ဖြစ်သည်။ ဒီကြောင့် မောက်ဒယ်ကို ချွတ်ယွင်းချက်များ ပြန်စစ်ပြီးတိုးတက်စေရန် တောင်းဆိုခြင်း (self-refine) လုပ်ပါ။

လုပ်ဆောင်ပုံ-

1. မူလ prompt ဖြင့် ဖြေချက် တောင်းဆိုသည်။
2. LLM က ဖြေသည်။
3. ဖြေချက်ကို သင် ဝေဖန်ပြီး AI ကို တိုးတက်အောင် တောင်းဆိုသည်။
4. LLM က ချွတ်ယွင်းချက် အသိအမှတ်ပြုကာ တိုးတက်သွားသော ဖြေချက်တွေ ပြန်ပေးသည်။

ဒီလုပ်ငန်းစဉ်ကို လိုချင်သမွ် ထပ်ဆင့်ဆက်လုပ်နိုင်သည်။

ဥပမာ-

> Prompt: "Python Web API ကို products နှင့် customers routes ပါသော အခင်းအကျင်း အဖြစ် ဖန်တီးပါ"

 AI ၏ အဖြေ-

```python
import flask
app = Flask(__name__)

@app.route('/products')
def products():
    return 'Products'

@app.route('/customers')
def customers():
    return 'Customers'
```

> Prompt: အထက်ပါ ကုဒ်ကို တိုးတက်အောင် အကြံ ၃ ချက်တင်ပြပါ

 AI ၏ အဖြေ-

```text
Sure, here are three suggestions to improve the code:

Import the correct module: The first line should import Flask instead of flask. The correct import statement should be from flask import Flask.

Add a main function: Add a if __name__ == '__main__': block to the end of the file to run the application when the file is executed.

Use f-strings: Use f-strings to format the return statements in the route functions. For example, return 'Products' can be changed to return f'This is the {request.path} page'.
```

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/products')
def products():
    return f'This is the {request.path} page'

@app.route('/customers')
def customers():
    return f'This is the {request.path} page'

if __name__ == '__main__':
    app.run()
```

ဒီအတိုင်း AI ၏ ပထမဆုံး ထောက်ပြခဲ့သည့် ကုဒ်ကို တိုးတက်အောင် ပြုပြင်ထားသည်။

### Maieutic prompting

 Maieutic prompting သည် self-refine နည်းနှင့် ဆင်တူသော်လည်း မောက်ဒယ်၏ ဖြေကြားချက်ကို ပြန်လည်ရှင်းလင်းရန် ညွှန်ကြားခြင်းဖြစ်သည်။ ရည်ရွယ်ချက်မှာ သီးခြား အပိုင်းရေးထားချက်များအတွက် မမှန်ကန်မှု မရှိစေရန်ဖြစ်သည်။ လုပ်ဆောင်မှု ခြေလှမ်းများ-

1. မေးခွန်းတစ်ခုကို အဖြေတောင်းသည်။
2. အဖြေတစ်ခုချင်းစီအတွက် ရှင်းလင်းချက်ထပ်မံမေးသည်။
3. မညီမျှမှုရှိပါက မညီမျှသော အပိုင်းကို ဖယ်ရှားသည်။

 နောက်တစ်ဆင့်သို့ ပိုမိုရှင်းလင်းသောအဖြေများ ရရှိသည်အထိ အဆင့် ၂ နှင့် ၃ ကို ထပ်မံလုပ်ဆောင်သည်။

ဥပမာ prompt-

> prompt: ကမ္ဘာလုံးဆိုင်ရာ ရောဂါ ကပ်ဘေးကို စီမံကိန်း ၅ ချက်ဖြင့် မည်ကဲ့သို့ မျှတစွာလျှော့ချမည်နည်း?
> LLM အဖြေ-

```text
1. Identify the risks
1. Identify the stakeholders
1. Identify the resources
1. Identify the actions
1. Identify the communication channels
```

အဆင့် ၅ ချက် သိရှိသော်လည်း မှန်ကန်မှု ရှိ/မရှိ စစ်ဆေးရန် လိုအပ်သည်။ အဆင့် ၁ ကို ပိုမိုဖော်ပြရန် LLM ချွန်ပြောကြားရန် မေးမြန်းပါ-

> prompt: ပထမဆုံး အဆင့်ကို အသေးစိတ်ရှင်းပြပါ၊ ကပ်ဘေးတွင် ခြိမ်းခြောက်မှုများက ဘာများပါသလဲ?

```text
The risks are the following:

- Loss of life
- Loss of business
- Loss of reputation
- Loss of customers
- Loss of employees
```

ယခုမှာ LLM ဖြေမှုမှန်ကန်မှုရှိ/မရှိ စစ်ဆေးရန် ပထမဆုံး ခြိမ်းခြောက်မှုကို အသေးစိတ် မေးပြီး ကျွန်ုပ်တို့ အောက်ပါအတိုင်း လိုက်နာနိုင်သည်။

> prompt: ကပ်ဘေးတွင် အကြီးဆုံး ခြိမ်းခြောက်မှု ဘာဖြစ်ပြီး မည်ကြောင့်လဲ?

```text
The biggest risk is loss of life because it's the most important thing to protect.
```

> ကပ်ဘေးမျိုးတွင် အကြီးဆုံးခြိမ်းခြောက်မှု နှစ်ခု ဘာများရှိသလဲ?

```text
The two biggest risks are loss of life and loss of business.
```

ယခုအချိန်တွင် LLM သည် "အသက်" နှင့် "စီးပွားရေး" ကို ထိပ်ဆုံးခြိမ်းခြောက်မှုနှစ်ခုအဖြစ် ဖော်ပြသည်။ ထို့နောက် နောက်တစ်ဆင့်ဆက်လက်လုပ်လိုက်နိုင်ပြီး ယုံကြည်မှုရှိနိုင်သည်။ သို့သော် LLM ကို ဘေးကင်းစွာ ယုံကြည်၍ အတည်ပြုမှုကို အမြဲတမ်း ပြုလုပ်သင့်သည်။

## Output ကို မတူညီစေပါ

LLM များသည် မတည်ငြိမ်သော (nondeterministic) ဖြစ်ကြ၍ တူညီသော prompt ကို ထပ်မံ ခေါ်ယူလျှင် မတူညီသောရလဒ် များ ရပါသည်။ ဥပမာ prompt-

> "Python Web API အတွက် ကုဒ် ဖန်တီးပါ"

```python
# လိုအပ်သော မော်ဒယ်များကို တင်သွင်းပါ
import flask
from flask import request, jsonify

# Flask app တစ်ခု ဖန်တီးပါ
app = flask.Flask(__name__)

# API အတွက် လမ်းကြောင်းတစ်ခု ဖန်တီးပါ
@app.route('/api', methods=['GET'])
def api():
    # တောင်းဆိုမှုမှ ဒေတာကို ယူပါ
    data = request.args

    # ဒေတာကို ပြုလုပ်ပါ
    result = process_data(data)

    # ရလဒ်ကို JSON အဖြစ် ပြန်ပို့ပါ
    return jsonify(result)

# ဒေတာကို ပြုလုပ်ရန် အလုပ်လုပ်မည့် function
def process_data(data):
    # ဒေတာနှင့် အလုပ်လုပ်ပါ
    result = data + 1

    # ရလဒ်ကို ပြန်ပေးပါ
    return result

# app ကို run ပါ
if __name__ == '__main__':
    app.run()

```

ထပ်မံ ထည့်နိုင်သည်-

```python
#လိုအပ်သော package များကို import ပြုလုပ်ပါ
import flask
from flask import request, jsonify

#Flask application ကို ဖန်တီးပါ
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#စာအုပ်စာရင်းတစ်ခု ဖန်တီးပါ
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

#API အတွက် endpoint တစ်ခု ဖန်တီးပါ
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Books API</h1>
<p>A prototype API for retrieving books.</p>'''

#စာအုပ်အားလုံးကို ပြန်ပေးပို့ရန် endpoint တစ်ခု ဖန်တီးပါ
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

#စာအုပ်တစ်အုပ်ကို ပြန်ပေးပို့ရန် endpoint တစ်ခု ဖန်တီးပါ
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    #URL အတွင်း ID ပါဝင်ခဲ့ရှိမရှိ စစ်ဆေးပါ
    #ID ပါရှိပါက အတည်ပြုသည့် variable သို့ သတ်မှတ်ပါ
    #ID မပါရှိပါက အမှားတစ်ခု ပြပါ
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    #ရလဒ်များအတွက် ဖေါ်ထုတ်ရန် အလွတ်စာရင်း တစ်ခု ဖန်တီးပါ
    results = []

    #ဒေတာများကို လည်ပတ်ပြီး တောင်းဆိုထားသော ID နှင့် ကိုက်ညီသော ရလဒ်များကို သွားရှာပါ
    #ID များမှာ တစ်ခုချင်းစီ ထူးခြားသော်လည်း အခြား ကွက်များက များစွာသော ရလဒ်များ ပေးနိုင်သည်
    for book in books:
        if book['id'] == id:
            results.append(book)

    #Flask ရဲ့ jsonify ဖင်ခွန်းကို အသုံးပြု၍ သင့်စာရင်းကို
    #Python dictionary များမှ JSON ပုံစံသို့ ပြောင်းပါ
    return jsonify(results)

app.run()
```

> output မတူညီမှုသည် ပြဿနာဖြစ်ပါသလား?

 သင့် ရည်ရွယ်ချက်ပေါ် မူတည်ပါသည်။ သင့်လိုအပ်သည့် ဖြေချက်တစ်ခုသာ အရေးကြီးလျှင် ပြဿနာဖြစ်သည်။ အကယ်၍ "Geography အကြောင်း မေးခွန်း ၃ ခု မည်သည့် ၃ ခု မဆို ဖန်တီးပါ" ဆိုရင် မပြဿနာဖြစ်ပါ။

### Temperature ကို အသုံးပြုပြီး output မတူညီမှု ထိန်းချုပ်ခြင်း

တူညီထွက်ရှိမှုတစ်ခု ထင်ရှားစေရန်၊ သိပ်မတည်ငြိမ်စေရန် Temperature ၏ တန်ဖိုးကို အသုံးပြုနိုင်သည်။ Temperature သည် 0 မှ 1 အကြား တန်ဖိုးဖြစ်ပြီး၊ 0 တွင် အတိအကျ (deterministic) အမြင့်ဆုံး၊ 1 တွင် output အမျိုးမျိုး မတူညီမှု အမြင့်ဆုံး ဖြစ်သည်။ မူရင်းတန်ဖိုးမှာ 0.7 ဖြစ်သည်။ Temperature ကို 0.1 သတ်မှတ်၍ တံတားချည်းကို အတူတူ prompt ကို ၂ ကြိမ် ဆောင်ရွက်ကြည့်မည်-

> "Python Web API အတွက် ကုဒ် ဖန်တီးပါ"

```python
#လိုအပ်သော စာကြည့်တိုက်များကို တင်သွင်းသည်
import flask
from flask import request, jsonify

#Flask class ၏ အမူအရာတစ်ခု ဖန်တီးသည်
app = flask.Flask(__name__)

#API အတွက် endpoint တစ်ခု ဖန်တီးသည်
@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    #တောင်းဆိုမှု ဒေတာကို ရယူသည်
    data = request.get_json()

    #ဒေတာကို ပြုလုပ်စီမံသည်
    result = process_data(data)

    #ရလဒ်ကို ပြန်ပေးပို့သည်
    return jsonify(result)

#ဒေတာကို ပြုလုပ်စီမံရန် function
def process_data(data):
    #ဒေတာကို ပြုလုပ်စီမံသည်
    result = {'result': 'success'}

    #ရလဒ်ကို ပြန်ပေးပို့သည်
    return result

#Flask အက်ပ်ကို လည်ပတ်သည်
if __name__ == '__main__':
    app.run()

```

ထပ်မံ တစ်ကြိမ် run လိုက်ရင်-

```python
#လိုအပ်သောစာကြည့်တိုက်များကိုထည့်သွင်းပါ
import flask
from flask import request, jsonify

#Flask app တစ်ခုကိုဖန်တီးပါ
app = flask.Flask(__name__)

#API အတွက် route တစ်ခုဖန်တီးပါ
@app.route('/api', methods=['GET'])
def api_call():
    #request မှ ဒေတာကိုရယူပါ
    data = request.get_json()

    #ဒေတာကိုကိန်းတွက်ပါ
    result = process_data(data)

    #အနုတ်တစ်ခုကိုပြန်ပေးပါ
    return jsonify(result)

#process_data function ကိုသတ်မှတ်ပါ
def process_data(data):
    #ဒေတာနှင့်အတူအတတ်ပညာတစ်ခုလုပ်ပါ
    result = data + 1

    #အနုတ်တစ်ခုကိုပြန်ပေးပါ
    return result

#app ကို run ပါ
if __name__ == '__main__':
    app.run()

```

 ဒီ နှစ် output မှ တစ်ခုချင်းစီမှာ အနည်းငယ်သာ ကွဲပြားနေသည်။ ယခုအကြိမ်မှာ 0.9 ထားပြီး လုပ်ကြည့်မည်-

```python
# လိုအပ်သော 라이브러리များကို တင်သွင်းပါ
import flask
from flask import request, jsonify

# Flask အက်ပ်ကို ဖန်တီးပါ
app = flask.Flask(__name__)

# API အတွက် လမ်းကြောင်းတစ်ခု ဖန်တီးပါ
@app.route('/api', methods=['GET'])
def api_call():
    # တောင်းဆိုမှုမှ ဒေတာကို ရယူပါ
    data = request.args

    # ဒေတာကို ပြန်လည်ထုတ်လုပ်ပါ
    result = process_data(data)

    # ရလဒ်ကို ပြန်ပေးပါ
    return jsonify(result)

# ဒေတာကို 처리လုပ်ရန် 함수
def process_data(data):
    # ဒေတာနှင့် တစ်စုံတစ်ရာလုပ်ဆောင်ပါ
    result = data + 1

    # ရလဒ်ကို ပြန်ပေးပါ
    return result

# အက်ပ်ကို chạyပါ
if __name__ == '__main__':
    app.run()

```

နောက်တစ်ကြိမ်လည်း 0.9 ချိန်ညှိထားမှုဖြင့်-

```python
import flask
from flask import request, jsonify

# Flask app ကိုဖန်တီးပါ
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# စမ်းသပ်မှုဒေတာတွေ ဖန်တီးပါ
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# endpoint တစ်ခုဖန်တီးပါ
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

ဖော်ပြထားသောအတိုင်း, output များမှာ အလွန် ကွဲပြားကြသည်။
> မှတ်ချက်၊ ထုတ်လွှင့်မှုကို မတူညီစေရန် ပြောင်းလဲနိုင်သော ပမာဏများ များစွာ ရှိပြီး top-k, top-p, repetition penalty, length penalty နှင့် diversity penalty ကဲ့သို့ ရှိပါသည်၊ သို့သော် ၎င်းတို့ကို ဤသင်ခန်းစာအစီအစဉ်၏ နယ်ပယ်တွင် မပါဝင်ပါ။

## ကောင်းမွန်သော ကျင့်စဉ်များ

လိုချင်သလို ရရှိစေရန် ကြိုးစားနိုင်သော ကျင့်စဉ်များ များစွာ တက်နိုင်သည်။ သင်ဟာ prompt များကို ပိုမိုအသုံးပြုတဲ့အခါ သင်ကိုယ်တိုင်၏ စတိုင်ကို ရှာတွေ့မယ်။

ကျွန်ုပ်တို့ ပြောပြခဲ့သော နည်းလမ်းများအပြင် LLM အား prompt ထားစဉ်တွင် စဉ်းစားသင့်သည့် ကောင်းသော ကျင့်စဉ်များ ရှိပါသည်။

အောက်ပါက အတွက် စဉ်းစားရန် ကောင်းသော ကျင့်စဉ်များဖြစ်သည် -

- **အကြောင်းအရာကို သတ်မှတ်ပါ**။ အကြောင်းအရာသည် အရေးပါသည်၊ ဒိုမိန်း၊ ခေါင်းစဉ် စသည့် အချက်များကို များ၍ သတ်မှတ်နိုင်သလောက် ရနိုင်သည်။
- ထုတ်လွှင့်မှုကို ကန့်သတ်ပါ။ တိတိကျကျ အရေအတွက် သို့မဟုတ် အရှည် ပမာဏ တစ်ခုလိုလျှင် သတ်မှတ်ပါ။
- **ဘာချင်သည်နှင့် ဘယ်လိုချင်သည်နှစ်ခုကိုလည်း သတ်မှတ်ပါ**။ ဥပမာ "routes products နှင့် customers ဦးတည်သော Python Web API တည်ဆောက်၍ မျှဝေစု ၃ ခုခွဲပါ" ကဲ့သို့ ဘာလိုချင်သည်နှင့် ဘယ်လိုလိုချင်သည်ကို နှစ်ခုလုံး ဖော်ပြပါ။
- **တမ်းပလိတ်များကို အသုံးပြုပါ**။ မကြာခဏ သင်၏ ကုမ္ပဏီမှ ဒေတာဖြင့် prompt များကို ပိုမိုကြွယ်ဝစေရန် လိုစဉ်ပါသည်။ တမ်းပလိတ်များကို အသုံးပြုပါ။ တမ်းပလိတ်များတွင် တကယ့်ဒေတာဖြင့် ထည့်သွင်းရန် အစားထိုးရမည့် မျက်နှာလွှာများ ရှိနိုင်သည်။
- **သရေမတည့်စွာ စာလုံးပေါင်းထည့်ပါ**။ LLM များက မှန်ကန်သော တုံ့ပြန်မှု ပေးနိုင်ပေမယ့် သရေမတည့်စွာ စာလုံးပေါင်းထားမှ ပိုကောင်းသော တုံ့ပြန်မှု ရရှိမည်။

## လေ့ကျင့်မှု

Flask အသုံးပြုကာ ရိုးရှင်းသော API တည်ဆောက်မှု ကို Python ဖြင့် ပြသထားသော ကုဒ်ဖြစ်သည် -

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
```

GitHub Copilot သို့မဟုတ် ChatGPT ကဲ့သို့ AI အကူအညီပေးကို အသုံးပြု၍ "self-refine" နည်းလမ်းဖြင့် ကုဒ်တိုးတက်အောင် ပြုလုပ်ပါ။

## ဖြေရှင်းချက်

သင့်အနေဖြင့် ကုဒ်တွင် သင့်တော်သော prompt များ ထည့်သွင်းကာ လေ့ကျင့်မှုကို နိုင်နိုင်သလောက် ဖြေရှင်းရန် ကြိုးစားပါ။

> [!TIP]
> ပိုမိုတိုးတက်အောင် ခေါ်ဆိုရန် prompt တစ်ခု ချရေးပါ၊ တိုးတက်မှု များအား ကန့်သတ်ထားတာကောင်းပါတယ်။ ထို့အပြင် ဝါရင့်တိုးတက်မှုကို အထူးအလေးထား၍ တိုးတက်အောင် လိုလားနိုင်ပြီး ဥပမာ နေရာရပ်တည်မှု, စွမ်းဆောင်ရည်, လုံခြုံရေး စသည့်အတိုင်း တိုးတက်အောင် တောင်းနိုင်သည်။

[ဖြေရှင်းချက်](../../../05-advanced-prompts/python/aoai-solution.py)

## အသိပညာ စစ်ဆေးခြင်း

chain-of-thought prompting ကို ဘာကြောင့် အသုံးပြုရမလဲ? တစ်ခုမှန်ကန်သော တုံ့ပြန်ချက်နှင့် မှားသော တုံ့ပြန်ချက် နှစ်ခု ပြပါ။

1. LLM ကို ပြဿနာဖြေရှင်းနည်း သင်ပေးရန်။
1. B၊ LLM ကို ကုဒ်အမှား ရှာဖွေသင်ကြားရန်။
1. C၊ LLM ကို မတူညီသော ဖြေရှင်းနည်းများ ဖန်တီးသင်ကြားရန်။

A: 1၊ chain-of-thought ဆိုတာ အဆင့်ဆင့်ဖြေရှင်းချက်များနှင့် ဆင်တူသော ပြဿနာများကို ဖြေရှင်းပုံကို LLM သို့ သရုပ်ပြ၍ ပြဿနာဖြေရှင်းနည်း သင်ပေးခြင်း ဖြစ်သည်။

## 🚀 စိန်ခေါ်မှု

သင်သည် လေ့ကျင့်မှုတွင် self-refine နည်းပြကို အသုံးပြုခဲ့သည်။ သင်တည်ဆောက်ခဲ့သည့် โปรแกรมတစ်ခုသာ ရွေးပြီး အဲဒီ ထိရောက်မှုများကို တိုးတက်အောင် ဆောင်ရွက်ချင်သည်။ ယခု self-refine နည်းဖြင့် အဆိုပါ ပြောင်းလဲမှုများကို အကောင်အထည်ဖော်ပါ။ ရလဒ်ကို ဘယ်လို တွေးပါသလဲ၊ ပိုကောင်းသလား၊ မကောင်းသလား?

## အလွန်းကောင်းသော အလုပ်! သင်ခန်းစာကို ဆက်လက်လေ့လာပါ

ဤသင်ခန်းစာ ပြီးဆုံးပြီးနောက် ကျွန်ုပ်တို့၏ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုကာ Generative AI ဗဟုသုတကို ပိုမိုမြှင့်တင်ပါ!

Lesson 6 သို့ သွားပါ၊ ဤမှာ ကျွန်ုပ်တို့၏ Prompt Engineering ကို အသုံးပြုပြီး [စာသားထုတ်လုပ်မှု ဆော့ဖ်ဝဲများ တည်ဆောက်ခြင်း](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst) ကို လေ့လာပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->