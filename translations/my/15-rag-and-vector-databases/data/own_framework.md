<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:52:27+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "my"
}
-->
# Neural Networks အကြောင်း မိတ်ဆက်ခြင်း။ Multi-Layered Perceptron

ယခင်အပိုင်းတွင် သင်သည် အလွယ်တကူနားလည်နိုင်သော neural network မော်ဒယ်ဖြစ်သော တစ်လွှာ perceptron၊ လိုင်းနီယာ နှစ်အုပ်စုခွဲခြားမှု မော်ဒယ်အကြောင်း သင်ယူခဲ့ပါသည်။

ဒီအပိုင်းမှာတော့ ဒီမော်ဒယ်ကို ပိုမိုတိုးချဲ့ပြီး ပိုမိုလွယ်ကူစွာ အသုံးပြုနိုင်တဲ့ ဖွဲ့စည်းပုံတစ်ခုအဖြစ် ဖန်တီးမှာဖြစ်ပြီး၊ အောက်ပါအရာများကို လုပ်ဆောင်နိုင်ပါမယ်-

* နှစ်အုပ်စု classification အပြင် **အုပ်စုများစွာ classification** လုပ်ဆောင်နိုင်ခြင်း
* classification အပြင် **regression ပြဿနာများကို ဖြေရှင်းနိုင်ခြင်း**
* လိုင်းနီယာဖြင့် ခွဲခြား၍ မရသော အုပ်စုများကို ခွဲခြားနိုင်ခြင်း

Python ဖြင့် မိမိတို့ရဲ့ modular framework ကို ဖန်တီးပြီး neural network အမျိုးမျိုးကို တည်ဆောက်နိုင်မယ့် နည်းလမ်းကိုလည်း တီထွင်သွားမှာ ဖြစ်ပါတယ်။

## Machine Learning ကို Formalize လုပ်ခြင်း

Machine Learning ပြဿနာကို formalize လုပ်ခြင်းနဲ့ စလိုက်ကြရအောင်။ သင့်မှာ training dataset **X** နဲ့ label တွေ **Y** ရှိတယ်ဆိုပါစို့၊ အဲ့ဒီမှာ အတိအကျဆုံး ခန့်မှန်းချက်တွေ ပြုလုပ်ပေးမယ့် မော်ဒယ် *f* တစ်ခု တည်ဆောက်ဖို့ လိုပါတယ်။ ခန့်မှန်းချက်ရဲ့ အရည်အသွေးကို **Loss function** ℒ နဲ့ တိုင်းတာပါတယ်။ အောက်ပါ loss function တွေကို မကြာခဏ အသုံးပြုကြပါတယ်-

* regression ပြဿနာအတွက်၊ နံပါတ်တစ်ခု ခန့်မှန်းဖို့လိုတဲ့အခါမှာ **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| သို့မဟုတ် **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> ကို အသုံးပြုနိုင်ပါတယ်
* classification အတွက်တော့ **0-1 loss** (မော်ဒယ်ရဲ့ **တိကျမှု**နဲ့ တူညီပါတယ်) သို့မဟုတ် **logistic loss** ကို အသုံးပြုကြပါတယ်။

တစ်လွှာ perceptron အတွက် function *f* ကို လိုင်းနီယာ function *f(x)=wx+b* (ဒီမှာ *w* က weight matrix, *x* က input features vector, *b* က bias vector) အဖြစ် သတ်မှတ်ထားပါတယ်။ neural network architecture မတူညီတာတွေအတွက် ဒီ function က ပိုရှုပ်ထွေးတဲ့ ပုံစံတွေ ရနိုင်ပါတယ်။

> classification အတွက်ဆိုရင်တော့၊ network output အနေနဲ့ အုပ်စုတစ်ခုချင်း probabilities ရရှိဖို့ လိုအပ်တတ်ပါတယ်။ အနည်းငယ် မတူညီတဲ့ နံပါတ်တွေကို probability တွေဖြစ်အောင် (ဥပမာ output ကို normalize လုပ်ဖို့) **softmax** function σ ကို မကြာခဏ အသုံးပြုကြပြီး function *f* က *f(x)=σ(wx+b)* ဖြစ်သွားပါတယ်။

အထက်ပါ *f* မှာ *w* နဲ့ *b* ကို **parameters** θ=⟨*w,b*⟩ လို့ ခေါ်ပါတယ်။ dataset ⟨**X**,**Y**⟩ ရှိတဲ့အခါ parameter θ အပေါ်မှာ အမှားစုစုပေါင်းကို တွက်ချက်နိုင်ပါတယ်။

> ✅ **neural network training ရဲ့ ရည်ရွယ်ချက်က parameter θ တွေကို ပြောင်းလဲခြင်းဖြင့် အမှားကို အနည်းဆုံးဖြစ်အောင် လုပ်ခြင်းဖြစ်ပါတယ်။**

## Gradient Descent Optimization

function optimization နဲ့ ပတ်သက်ပြီး လူသိများတဲ့ နည်းလမ်းတစ်ခုက **gradient descent** ဖြစ်ပါတယ်။ အဓိကအယူအဆကတော့ loss function ရဲ့ parameter တွေ အပေါ် derivative (multi-dimensional အတွက် **gradient** လို့ခေါ်) ကို တွက်ချက်ပြီး parameter တွေကို အမှားလျော့နည်းအောင် ပြောင်းလဲသွားတာပါ။ အောက်ပါအတိုင်း formalize လုပ်နိုင်ပါတယ်-

* parameter တွေကို အစမှာ အမှတ်တရ random တန်ဖိုး w<sup>(0)</sup>, b<sup>(0)</sup> နဲ့ စတင်ပါ
* အောက်ပါအဆင့်ကို မကြာခဏ ထပ်လုပ်ပါ-
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

training အတွင်းမှာ optimization အဆင့်တွေကို dataset အားလုံးကို ထည့်သွင်းတွက်ချက်ရမှာဖြစ်ပါတယ် (loss ကို training sample အားလုံး စုစုပေါင်းတွက်ချက်တာကို မှတ်ထားပါ)။ သို့သော် လက်တွေ့မှာ dataset ကို အစိတ်အပိုင်းသေးသေးလေးတွေဖြစ်တဲ့ **minibatches** အဖြစ် ခွဲပြီး gradient တွေကို subset အပေါ်မှာ တွက်ချက်ပါတယ်။ အဲ့ဒီ subset ကို မကြာခဏ random ရွေးတဲ့အတွက် ဒီနည်းကို **stochastic gradient descent** (SGD) လို့ ခေါ်ကြပါတယ်။

## Multi-Layered Perceptrons နဲ့ Backpropagation

တစ်လွှာ network က လိုင်းနီယာဖြင့် ခွဲခြားနိုင်တဲ့ အုပ်စုတွေကိုသာ ခွဲခြားနိုင်ပါတယ်။ ပိုမိုခိုင်မာတဲ့ မော်ဒယ်တစ်ခု ဖန်တီးဖို့အတွက် network အလွှာအများကြီးကို ပေါင်းစပ်နိုင်ပါတယ်။ သင်္ချာနဲ့ပြောရရင် function *f* က ပိုရှုပ်ထွေးတဲ့ ပုံစံဖြစ်ပြီး အဆင့်အတန်းအနည်းငယ်ဖြင့် တွက်ချက်ရမှာဖြစ်ပါတယ်-
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

ဒီမှာ α က **non-linear activation function** ဖြစ်ပြီး σ က softmax function ဖြစ်ပါတယ်။ parameter တွေက θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*> ဖြစ်ပါတယ်။

gradient descent algorithm က အတူတူပဲ ဖြစ်မှာဖြစ်ပေမယ့် gradient တွေ တွက်ချက်ရတာ ပိုခက်ခဲလာမှာ ဖြစ်ပါတယ်။ chain differentiation rule ကို အသုံးပြုပြီး derivative တွေကို အောက်ပါအတိုင်း တွက်ချက်နိုင်ပါတယ်-

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ chain differentiation rule ကို parameter တွေ အပေါ် loss function ရဲ့ derivative တွေ တွက်ချက်ဖို့ အသုံးပြုပါတယ်။

ဒီ expression တွေမှာ ဘယ်ဘက်ဆုံး အပိုင်းက တူညီတာကြောင့် loss function ကနေ စပြီး "နောက်ပြန်" computational graph ကို ဖြတ်သွားပြီး derivative တွေကို ထိရောက်စွာ တွက်ချက်နိုင်ပါတယ်။ ဒါကြောင့် multi-layered perceptron ကို training လုပ်တဲ့ နည်းလမ်းကို **backpropagation** သို့မဟုတ် 'backprop' လို့ ခေါ်ကြပါတယ်။

> TODO: image citation

> ✅ backprop ကို ကျွန်တော်တို့ရဲ့ notebook ဥပမာမှာ ပိုမိုအသေးစိတ် ဖော်ပြသွားမှာ ဖြစ်ပါတယ်။

## နိဂုံးချုပ်

ဒီသင်ခန်းစာမှာ ကျွန်တော်တို့ရဲ့ neural network library ကို တည်ဆောက်ပြီး၊ ရိုးရှင်းတဲ့ နှစ်-အတိုင်းအတာ classification လုပ်ငန်းအတွက် အသုံးပြုခဲ့ပါတယ်။

## 🚀 စိန်ခေါ်မှု

အတူတကွ notebook မှာ သင့်ကိုယ်ပိုင် multi-layered perceptron ဖန်တီးခြင်းနဲ့ training framework ကို တည်ဆောက်ဖို့ လုပ်ဆောင်ပါမယ်။ ခေတ်မီ neural network တွေ ဘယ်လို လည်ပတ်ကြတာကို အသေးစိတ် မြင်တွေ့နိုင်မှာ ဖြစ်ပါတယ်။

OwnFramework notebook ကို ဆက်လက်ဖတ်ရှု၍ လေ့လာပါ။

## ပြန်လည်သုံးသပ်ခြင်းနှင့် ကိုယ်တိုင်လေ့လာခြင်း

Backpropagation က AI နဲ့ ML မှာ အသုံးများတဲ့ algorithm တစ်ခုဖြစ်ပြီး ပိုမိုအသေးစိတ် လေ့လာဖို့ တန်ဖိုးရှိပါတယ်။

## အလုပ်အပ်

ဒီ lab မှာ သင်က ဒီသင်ခန်းစာမှာ တည်ဆောက်ထားတဲ့ framework ကို အသုံးပြုပြီး MNIST လက်ရေးနံပါတ် ခွဲခြားမှု ပြဿနာကို ဖြေရှင်းဖို့ တောင်းဆိုထားပါတယ်။

* လမ်းညွှန်ချက်များ
* Notebook

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။