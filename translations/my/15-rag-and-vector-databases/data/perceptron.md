<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T17:02:03+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "my"
}
-->
# Neural Networks အကြောင်း မိတ်ဆက်ခြင်း: Perceptron

ခေတ်မီ neural network တစ်ခုနဲ့ ဆင်တူတဲ့ အရာတစ်ခုကို ပထမဆုံး ကြိုးစားတည်ဆောက်ခဲ့တာက ၁၉၅၇ ခုနှစ်မှာ Cornell Aeronautical Laboratory မှ Frank Rosenblatt ဖြစ်ပါတယ်။ ဒါဟာ "Mark-1" လို့ခေါ်တဲ့ hardware တည်ဆောက်မှုဖြစ်ပြီး၊ သုံးထောင့်၊ စတုရန်း၊ စက်ဝိုင်းလို ပုံစံရိုးရှင်းတဲ့ ဂျီယိုမက်ထရစ်ပုံစံတွေကို မှတ်သားနိုင်ဖို့ ဒီဇိုင်းဆွဲထားတာပါ။

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Wikipedia မှ ရယူထားသော ပုံများ

Input ပုံတစ်ပုံကို 20x20 photocell အတွင်းက အစိတ်အပိုင်းတွေဖြင့် ဖော်ပြထားပြီး၊ neural network မှာ input ၄၀၀ ခုနဲ့ binary output တစ်ခုရှိပါတယ်။ ရိုးရှင်းတဲ့ network တစ်ခုမှာ neuron တစ်ခုသာ ပါပြီး၊ ဒါကို **threshold logic unit** လို့လည်း ခေါ်ပါတယ်။ Neural network ရဲ့ weight တွေက training အချိန်မှာ manually ပြင်ဆင်ရတဲ့ potentiometer တွေလို ဖြစ်ပါတယ်။

> ✅ potentiometer ဆိုတာက စက်လည်ပတ်မှုအတွင်း resistance ကို အသုံးပြုသူက ပြင်ဆင်နိုင်တဲ့ စက်ပစ္စည်းတစ်ခုပါ။

> New York Times က perceptron အကြောင်းကို အဲဒီအချိန်မှာ ဒီလိုရေးသားခဲ့ပါတယ် - *[Navy] က လမ်းလျှောက်၊ စကားပြော၊ မြင်၊ ရေး၊ ကိုယ်ပိုင်ကို ပြန်ထုတ်လုပ်နိုင်ပြီး ကိုယ်တိုင် ရှိနေမှုကို သိရှိနိုင်မယ့် အီလက်ထရွန်းနစ် ကွန်ပျူတာရဲ့ မျိုးစေ့ဖြစ်တယ်လို့ မျှော်လင့်ထားပါတယ်။*

## Perceptron မော်ဒယ်

ကျွန်တော်တို့မှာ N ခုသော feature တွေရှိတယ်ဆိုပါစို့၊ input vector ကတော့ အရွယ်အစား N ရှိတဲ့ vector ဖြစ်ပါမယ်။ Perceptron က **binary classification** မော်ဒယ်တစ်ခုဖြစ်ပြီး၊ input data နှစ်မျိုးကို ခွဲခြားနိုင်ပါတယ်။ input vector x တစ်ခုစီအတွက် perceptron ရဲ့ output က +1 သို့မဟုတ် -1 ဖြစ်မယ်၊ class အပေါ်မူတည်ပြီး ဖြစ်ပါတယ်။ output ကို အောက်ပါ သင်္ချာနည်းဖြင့်တွက်ချက်ပါမယ်-

y(x) = f(w<sup>T</sup>x)

ဒီမှာ f က step activation function ဖြစ်ပါတယ်။

## Perceptron ကို သင်ကြားခြင်း

Perceptron ကို သင်ကြားဖို့အတွက် weight vector w ကို ရှာဖွေရမယ်၊ ဒါက အများဆုံး data တွေကို မှန်ကန်စွာ ခွဲခြားနိုင်ဖို့ ဖြစ်ပြီး၊ အမှားအနည်းဆုံး ဖြစ်အောင် လုပ်ရပါမယ်။ ဒီအမှားကို **perceptron criterion** အဖြစ် အောက်ပါအတိုင်း သတ်မှတ်ထားပါတယ်-

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ဒီမှာ-

* စုစုပေါင်းကို training data တွေထဲမှ မှားယွင်းစွာ ခွဲခြားထားတဲ့ i တွေမှာသာ ယူဆောင်ထားပါတယ်။
* x<sub>i</sub> က input data ဖြစ်ပြီး၊ t<sub>i</sub> က negative နဲ့ positive ဥပမာအတွက် -1 သို့မဟုတ် +1 ဖြစ်ပါတယ်။

ဒီ criteria ကို weight w ရဲ့ function အဖြစ် သတ်မှတ်ပြီး၊ minimize လုပ်ဖို့ လိုပါတယ်။ အများအားဖြင့် **gradient descent** ဆိုတဲ့ နည်းလမ်းကို အသုံးပြုကြပြီး၊ အစမှာ w<sup>(0)</sup> ဆိုတဲ့ initial weight နဲ့ စပြီး၊ နောက်တစ်ဆင့်တိုင်းမှာ အောက်ပါနည်းဖြင့် weight တွေကို update လုပ်ပါတယ်-

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

ဒီမှာ η က **learning rate** ဖြစ်ပြီး၊ ∇E(w) က E ရဲ့ **gradient** ကို ဆိုလိုပါတယ်။ gradient တွက်ပြီးနောက်မှာ

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python မှာ ဒီ algorithm ကို အောက်ပါအတိုင်း ရေးနိုင်ပါတယ်-

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## နိဂုံးချုပ်

ဒီသင်ခန်းစာမှာ perceptron ဆိုတာ ဘာလဲ၊ binary classification မော်ဒယ်တစ်ခုဖြစ်တာနဲ့ weight vector ကို အသုံးပြုပြီး ဘယ်လို သင်ကြားရမလဲ ဆိုတာကို သင်ယူခဲ့ပါပြီ။

## 🚀 စိန်ခေါ်မှု

သင့်ကိုယ်ပိုင် perceptron တည်ဆောက်ဖို့ စိတ်ဝင်စားရင် Microsoft Learn မှာ Azure ML designer ကို အသုံးပြုပြီး ဒီ lab ကို ကြိုးစားကြည့်ပါ။

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

Perceptron ကို ကစားစရာပြဿနာနဲ့ အမှန်တကယ်ဖြေရှင်းရမယ့် ပြဿနာတွေမှာ ဘယ်လို အသုံးပြုနိုင်မလဲ၊ နောက်ထပ် သင်ယူဖို့ Perceptron notebook ကို သွားကြည့်ပါ။

Perceptron အကြောင်း စိတ်ဝင်စားဖွယ် ဆောင်းပါးတစ်ပုဒ်လည်း ရှိပါတယ်။

## အလုပ်အပ်နှံချက်

ဒီသင်ခန်းစာမှာ binary classification အတွက် perceptron တစ်ခုကို တည်ဆောက်ပြီး၊ နှစ်လုံးလက်ရေးဂဏန်းတွေကို ခွဲခြားဖို့ အသုံးပြုခဲ့ပါတယ်။ ဒီ lab မှာတော့ ပုံတစ်ပုံနဲ့ ကိုက်ညီနိုင်တဲ့ ဂဏန်းကို သတ်မှတ်ဖို့ digit classification ပြဿနာကို အပြည့်အစုံ ဖြေရှင်းဖို့ တောင်းဆိုထားပါတယ်။

* လမ်းညွှန်ချက်များ
* Notebook

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။