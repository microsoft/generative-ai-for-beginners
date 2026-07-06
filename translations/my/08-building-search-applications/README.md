# ဘေးရှာဖွေရေးလျှောက်လွှာများဆောက်လုပ်ခြင်း

[![Introduction to Generative AI and Large Language Models](../../../translated_images/my/08-lesson-banner.8fff48c566dad08a.webp)](https://youtu.be/W0-nzXjOjr0?si=GcsqiTTvd7RKbo7V)

> > _ဤသင်ခန်းစာ၏ ဗီဒီယိုကိုကြည့်ရန် အပေါ်မှဓာတ်ပုံကိုနှိပ်ပါ_

LLM များသည် စကားပြောစက်များနှင့် စာသားဖန်တီးခြင်းထက်ပို၍ ရှိသည်။ Embeddings ကို အသုံးပြု၍ ဘေးရှာဖွေရေးလျှောက်လွှာများ ဆောက်လုပ်နိုင်ပါသည်။ Embeddings တွင် ဒေတာ၏ နံပါတ်ပြ အထမ်းဆောင်မှုများ ဖြစ်ပြီး vectors ဟုလည်း သိကြသည်။ ဒါကို ဒေတာအတွက် အဓိပ္ပါယ်ဆိုင်ရာ ဘေးရှာဖွေရေးအတွက် အသုံးပြုနိုင်ပါသည်။

ဤသင်ခန်းစာတွင် ကျွန်ုပ်တို့ပညာရေး စတတ်အပ် အဖွဲ့အစည်းအတွက် ဘေးရှာဖွေရေးလျှောက်လွှာတစ်ခု ဆောက်လုပ်ပြမည်ဖြစ်သည်။ ကျွန်ုပ်တို့ စတတ်အပ်သည် ဖွံ့ဖြိုးတိုးတက်နေသောနိုင်ငံများရှိ ကျောင်းသားများကို အခမဲ့ပညာပေးသည့် အကျိုးပြုအဖွဲ့အစည်းတစ်ခုဖြစ်သည်။ ကျွန်ုပ်တို့ စတတ်အပ်တွင် AI အကြောင်းသင်ယူနိုင်ရန် ကျောင်းသားများအသုံးပြုနိုင်သော YouTube ဗီဒီယိုများစွာ ပါရှိသည်။ ကျွန်ုပ်တို့ စတတ်အပ်သည် ကျောင်းသားများကို စကားမေးပြီး YouTube ဗီဒီယိုများကို ရှာဖွေဖို့ အခွင့်အလမ်းပေးသည့် ဘေးရှာဖွေရေး လျှောက်လွှာတစ်ခု ဆောက်လုပ်လိုသည်။

ဥပမာ၊ ကျောင်းသားတစ်ယောက်က 'Jupyter Notebooks ဆိုတာဘာလဲ?' သို့မဟုတ် 'Azure ML ဆိုတာဘာလဲ?' ဟူသော မေးခွန်းများ ရိုက်ထည့်နိုင်ပြီး၊ ဤဘေးရှာဖွေရေးလျှောက်လွှာက မေးခွန်းနှင့်သက်ဆိုင်သော YouTube ဗီဒီယိုစာရင်းကို ပြန်ပေးမည်ဖြစ်ပြီး အကောင်းဆုံးမှာ မေးခွန်းအဖြေ ရှိသော ဗီဒီယိုအပိုင်းသို့ ချိတ်ဆက်ထားသောလင့်ခ်ကိုလည်း ပြန်ပေးမည်ဖြစ်သည်။

## မှတ်ချက်

ဤသင်ခန်းစာတွင် ကျွန်ုပ်တို့ ဖော်ပြမည့်အကြောင်းအရာများမှာ-

- Semantic နှင့် Keyword search ကြားကွာခြားချက်။
- Text Embeddings ဆိုသည့်အကြောင်း။
- Text Embeddings Index ဖန်တီးခြင်း။
- Text Embeddings Index တွင် ရှာဖွေရေး။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာပြီးဆုံးပါက-

- semantic နှင့် keyword search များ၏ ကွာခြားချက်ကို ပြောပြနိုင်မည်။
- Text Embeddings များအား ရှင်းရွင်းဖော်ပြနိုင်မည်။
- Embeddings အသုံးပြု၍ ဒေတာရှာဖွေရေး လျှောက်လွှာတစ်ခု ဖန်တီးနိုင်မည်။

## ဘယ်ကြောင့် ဘေးရှာဖွေရေးလျှောက်လွှာ ဆောက်လုပ်သနည်း?

ဘေးရှာဖွေရေးလျှောက်လွှာ တစ်ခု ဆောက်လုပ်ခြင်းဖြင့် Embeddings ကို ဒေတာရှာဖွေရေးအတွက် အသုံးပြုနည်း လေ့လာ လိုက်ပါမည်။ ကျောင်းသားများ အချက်အလက်များကို မြန်မြန်ဆန်ဆန် ရှာတွေ့နိုင်ရန်လည်း လျှောက်လွှာတစ်ခု ဖန်တီးရမည်ဖြစ်သည်။

သင်ခန်းစာတွင် Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) YouTube ချန်နယ်၏ transcript များအတွက် Embedding Index ပါဝင်သည်။ AI Show သည် AI နှင့် machine learning ကို သင်ကြားပေးသော YouTube ချန်နယ်ဖြစ်သည်။ Embedding Index တွင် ၂၀၂၃ ခုနှစ် အောက်တိုဘာလအထိ YouTube transcript စာသားများအတွက် Embeddings များ ပါရှိသည်။ သင်သည် ထို Embedding Index ကို အသုံးပြုပြီး ကျွန်ုပ်တို့ စတတ်အပ်အတွက် ဘေးရှာဖွေရေးလျှောက်လွှာတစ်ခု ဖန်တီးမည်ဖြစ်သည်။ ဤလျှောက်လွှာသည် မေးခွန်းနှင့် သက်ဆိုင်သော ဗီဒီယိုအပိုင်းသို့ Direct Link ကို ပြန်ပေးသည်။ အကောင်းဆုံးကျောင်းသားများ လိုအပ်သည့် အချက်အလက်များကို အလျင်အမြန် ရှာတွေ့နိုင်စေသည်။

နောက်ထပ် ဥပမာအနေနှင့် 'can you use rstudio with azure ml?' ဆိုသောမေးခွန်းအတွက် semantic query ဖြစ်သည်။ YouTube url တွင် timestamp ပါရှိ၍ မေးခွန်းဖြေရာ ဗီဒီယိုအပိုင်းသို့ တိုက်ရိုက် သွားရောက်နိုင်သည်။

![Semantic query for the question "can you use rstudio with Azure ML"](../../../translated_images/my/query-results.bb0480ebf025fac6.webp)

## Semantic search ဆိုတာဘာလဲ?

အခု သင်အံ့သြနိင်တာက semantic search ဆိုတာဘာလဲဆိုတာဖြစ်နိုင်သည်။ Semantic search ဆိုသည်မှာ query တွင် အသုံးပြုထားသော အသုံးအနှုန်းများ၏ အဓိပ္ပါယ်ကို အသုံးပြုကာ သက်ဆိုင်ရာ ဖြေရှင်းချက်များကို ပြန်ပေးသည့် ရှာဖွေရေးနည်းပညာဖြစ်သည်။

ဤမှာ semantic search ဥပမာတစ်ခုရှိသည်။ မော်တော်ကား ဝယ်ယူရန် မျှော်မှန်းနေသောသူတစ်ဦးရှိသည်ဟု ယူဆပါက၊ “my dream car” ဟု ရှာဖွေမည်ဆိုပါက semantic search သည် “အိပ်မက်ဖြစ်စေသောကား” မဟုတ်ဘဲ “စိတ်ကြိုက်” ကား ဝယ်လိုသည်ဟု နားလည်သည်။ Semantic search သည် ရည်ရွယ်ချက်ကို နားလည်ကာ သက်ဆိုင်ရာ ရလဒ်များပြန်ပေးမည်ဖြစ်သည်။ Keyword search သည် အနိူင်ဖြစ်သည်ဟုသတ်မှတ်၍ အခါအားလျော်စွာ သက်ဆိုင်မှုမရှိသော ရလဒ်များ ပြန်လာနိုင်သည်။

## Text Embeddings ဆိုတာဘာလဲ?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) သည် [ဘာသာစကား သဘာဝလုပ်ငန်းဂဏန်း](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst) တွင် အသုံးပြုသော စာသား ကိုယ်စားပြုနည်းဖြစ်သည်။ Text embeddings သည် စာသားများ၏ Semantic နံပါတ်ဆိုင်ရာ ကိုယ်စားပြုမှုများပါသည်။ Embeddings များသည် ကွန်ပြူတာ များအတွက် နားလည်ရန် လွယ်ကူစေရန် ဒေတာကို ကိုယ်စားပြုထုတ်ပေးသည်။ Text embeddings ဖန်တီးခြင်းအတွက် မော်ဒယ်များစွာရှိသော်လည်း ဤသင်ခန်းစာတွင် OpenAI Embedding Model ကို အသုံးပြု၍ Embeddings ထုတ်လုပ်သည့် နည်းကို ဦးစားပေး လေ့လာမည်။

ဥပမာအားဖြင့် AI Show YouTube ချန်နယ်ရှိ episode တစ်ခုမှ transcript စာသားမှာ အောက်ပါအတိုင်းဖြစ်သည်-

```text
Today we are going to learn about Azure Machine Learning.
```


ကျွန်ုပ်တို့သည် ဤစာသားကို OpenAI Embedding API သို့ ပေးပို့ပြီး ၁၅၃၆နံပါတ်ပါဝင်သော vector တစ်ခု ရရှိမည်ဖြစ်သည်။ Vector ထဲရှိ နံပါတ်တစ်ခုချင်းစီသည် စာသား၏ အသေးစိတ် အချက်အလက်တစ်ခုကို ကိုယ်စားပြုပြီး သုံးသပ်နိုင်သည်။ တိကျမှုအတွက် ဤမှာ vector ၏ ပထမ ၁၀ နံပါတ်ကိုသာ ဖော်ပြထားသည်။

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```


## Embedding index ကို မည်ကဲ့သို့ ဖန်တီးထားသနည်း?

ဤသင်ခန်းစာအတွက် Embedding index ကို Python script များ စဉ်ဆက်မပြတ် အသုံးပြု၍ ဖန်တီးထားသည်။ Script များနှင့် အသုံးပြုနည်း ညွှန်ကြားချက်များကို ဤသင်ခန်းစာ အတွင်းရှိ 'scripts' ဖိုင်တွဲအောက်ရှိ [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) မှာ တွေ့ရမည်ဖြစ်သည်။ သင်ဤသင်ခန်းစာကို ပြီးမြောက်ရန်အတွက် script များကို မရောလျှောက် နှစ်သက်စွာ မသွားရောက် မဖွင့်ဆောင်ခွင့်မရှိသေးပါ၊ အခြားနေရာတွင်ရရှိထားသည့် Embedding Index ကိုသာ အသုံးပြုလျက်ရှိသည်။

ဤ script များက ပြုလုပ်သော လုပ်ဆောင်ချက်များမှာ-

၁။ [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) playlist အတွက် YouTube ဗီဒီယို တစ်ခုချင်းစီ၏ transcript ကို ဒေါင်းလုတ်ရယူသည်။
၂။ [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst) ကို အသုံးပြု၍ YouTube transcript ၏ ပထမ ၃ မိနစ်အတွင်း ပါသည့် စကားပြောသူ အမည်ကို ဖော်ထုတ်ရန် ကြိုးပမ်းသည်။ ဗီဒီယိုတစ်ခုချင်းစီ၏ စကားပြောသူအမည်ကို Embedding Index `embedding_index_3m.json` တွင်သိမ်းဆည်းထားသည်။
၃။ Transcript စာသားကို **၃ မိနစ်စာ ပိုင်းခြားချက်များတွင်ပိုင်းခွဲ**သည်။ ပိုင်းခြားချက်တိုင်းသည် နောက်ပိုင်းပိုင်းခြားချက်၏ စာလုံး ၂၀ အနီးအနားမှ ကွက်လပ်ဖြတ်ထားခြင်းရှိသည်။ ၎င်းက နောက်ပိုင်းအပိုင်းက ဒေတာဖြတ်ခြင်းမဖြစ်စေရန်နှင့် ရှာဖွေရေးအတွက် ပိုမိုကောင်းမွန်သော ပတ်ဝန်းကျင်ပုံစံကို ဖန်တီးရန်ဖြစ်သည်။
၄။ တစ်ခုချင်းစီသော စာသားပိုင်းခြားကို OpenAI Chat API သို့ ပေးပို့ပြီး စာသားကို ၆၀ စကားလုံး သို့ စုပေါင်းချုပ်နိင်မှု ပြုလုပ်သည်။ ဆက်တင်ကိုလည်း Embedding Index `embedding_index_3m.json` တွင်သိမ်းဆည်းထားသည်။
၅။ နောက်ဆုံးတွင် အဆိုပါ စာသားပိုင်းခြားကို OpenAI Embedding API သို့ ပေးပို့သည်။ Embedding API မှ ၁၅၃၆ ကိန်းဂဏန်းပါရှိသော vector ကို ပြန်ပေးသည်။ ဤ vector သည် စာသားပိုင်းခြား၏ အဓိပ္ပါယ်ဆိုင်ရာ ကိုယ်စားပြုမှု ဖြစ်သည်။ စာသားပိုင်းခြားနှင့် OpenAI Embedding vector ကို Embedding Index `embedding_index_3m.json` တွင် သိမ်းဆည်းထားသည်။

### Vector Database များ

သင်ခန်းစာ အလွယ်တကူ ဖြစ်စေရန် Embedding Index ကို `embedding_index_3m.json` ဟူသော JSON ဖိုင်တွင်သိမ်းဆည်းကာ Pandas DataFrame တွင် ဖတ်ယူထားသည်။ သို့သော် ထုတ်လုပ်မှုတွင် Embedding Index ကို vector database များဖြစ်သည့် [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst) စသည့် service များတွင် သိမ်းဆည်းထားသည်။

## cosine similarity ကို နားလည်ခြင်း

Text embeddings များကို သင်ယူပြီးနောက် ဘယ်လို အသုံးပြုကာ ဒေတာရှာဖွေရမည်နှင့် ထူးခြားပြီး ပို၍ ဆန်ဆန်သော embedding များ ရှာဖွေရန် cosine similarity ကို ဘယ်လိုသုံးရမည်ဆိုင်ရာကို ကုန်ဆုံးခြင်းဖြစ်သည်။

### cosine similarity ဆိုတာ ဘာလဲ?

Cosine similarity သည် vector နှစ်ခုကြား တွဲဖက်ဆင်ခြင်းအတိုင်းအတာဖြစ်ပြီး `nearest neighbor search` ဟုလည်း ခေါ်ဆိုကြသည်။ cosine similarity ရှာဖွေရေး လုပ်ရန် query စာသားကို OpenAI Embedding API ဖြင့် _vectorize_ ပြုလုပ်ရမည်။ ထို့နောက် query vector နှင့် Embedding Index ရှိ vectors တစ်ခုချင်းဆီအကြား cosine similarity ကိုတွက်ချက်ရမည်။ 기억ပါ၊ Embedding Index တွင် YouTube transcript စာသားပိုင်းခြားတစ်ခုချင်းစီအတွက် vector ရှိသည်။ နောက်ဆုံး cosine similarity အဆင့်အတန်းဖြင့် ရလဒ်များကို စီစဉ်ပြီး cosine similarity မြင့်သော စာသားပိုင်းခြားများသည် query နှင့် အနီးဆုံး ပုံစံဖြစ်သည်။

သင်္ချာပညာနည်းမှာ cosine similarity သည် multidimensional အာကာသရှိ vector နှစ်ခုကြား ထောင့်ခွာခြားမှု၏ cosine ကိုတိုင်းတာသည်။ ဤတိုင်းတာသည် အကျိုးရှိသည်၊ အကယ်၍ ဒေတာနှစ်ခု Euclidean ခြားနားမှုကြောင့် ဝေးလွန်းနေပါက size မတူပေမယ့် ထောင့်ကဏ္ဍများနားတွင် ပိုမိုနီးစပ်၍ ကျော်ကြားသော cosine similarity ရရှိနိုင်ပါသည်။ cosine similarity သင်္ချာအချက်အလက်များကို [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst) တွင် ဖတ်ရှုနိုင်သည်။

## သင့်ပထမဆုံး ဘေးရှာဖွေရေးလျှောက်လွှာ ဆောက်လုပ်ခြင်း

နောက်တစ်ခုမှာ Embeddings ကို အသုံးပြုပြီး ဘေးရှာဖွေရေးလျှောက်လွှာ တစ်ခု ဆောက်လုပ်နည်းကို သင်ယူ မည်ဖြစ်သည်။ ဤလိုက်လျောညီမှုလျှောက်လွှာက ကျောင်းသားများ၏ မေးခွန်းတစ်ခုရိုက်ထည့်ခြင်းဖြင့် ဗီဒီယိုရှာဖွေလုပ်နိုင်စေမည်ဖြစ်သည်။ လျှောက်လွှာသည် မေးခွန်းနှင့်သက်ဆိုင်သော ဗီဒီယိုစာရင်းများ ဖော်ပြမည်ဖြစ်ပြီး မေးခွန်းဖြေရာ ဗီဒီယိုအပိုင်းသို့ ချိတ်ဆက်ထားသော လင့်ခ်ကိုလည်း ပြန်ပေးမည်ဖြစ်သည်။

ဤ ဖြေရှင်းချက်သည် Windows 11, macOS, နှင့် Ubuntu 22.04 ပတ်ဝန်းကျင်များတွင် Python 3.10 သို့မဟုတ် 그 이상의 ကူးစောင်းဖြင့် စမ်းသပ်ထားသည်။ Python ကို [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) မှ ဒေါင်းလုပ်ထုတ်နိုင်ပါသည်။

## ကြိုးစားမှု - ကျောင်းသားများအတွက် ဘေးရှာဖွေရေးလျှောက်လွှာ ဆောက်လုပ်ခြင်း

ဤသင်ခန်းစာအစပိုင်းတွင် ကျွန်ုပ်တို့ စတတ်အပ်အဖွဲ့အစည်းကို မိတ်ဆက်ခဲ့သည်။ ယခု အခါ ကျောင်းသားများအတွက် သင်ခန်းစာစာမေးပွဲများအတွက် ဘေးရှာဖွေရေးလျှောက်လွှာတစ်ခုမှာ ဖန်တီးပေးချိန်ဖြစ်သည်။

ဤလုပ်ငန်းဆောင်တာတွင် ဘေးရှာဖွေရေးလျှောက်လွှာ တည်ဆောက်ရန် အသုံးပြုမည့် Azure OpenAI Services များကို တည်ဆောက်မည်ဖြစ်သည်။ အောက်ပါ Azure OpenAI Services အား တည်ဆောက်ရမည်ဖြစ်ပြီး အဆိုပါလုပ်ငန်းဆောင်တာကို ပြီးမြောက်ရန် Azure subscription လိုအပ်မည်ဖြစ်သည်။

### Azure Cloud Shell စတင်ခြင်း

၁။ [Azure portal](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) တွင် စာရင်းဝင်ပါ။
၂။ Azure portal ၏ ညာဘက်အထက်ဆုံးတွင် Cloud Shell သင်္ကေတကို နှိပ်ပါ။
၃။ ပတ်ဝန်းကျင်အမျိုးအစား အဖြစ် **Bash** ကို ရွေးပါ။

#### resource group တည်ဆောက်ခြင်း

> ဤညွှန်ကြားချက်များတွင် East US တွင် "semantic-video-search" ဟူသော resource group ကို အသုံးပြုထားသည်။
> resource group အမည်ကို ပြောင်းလဲနိုင်သော်လည်း resource များတည်နေရာပြောင်းရာတွင်
> [မော်ဒယ်ရရှိနိုင်မှုဇယား](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ကို စစ်ဆေးပါ။

```shell
az group create --name semantic-video-search --location eastus
```


#### Azure OpenAI Service resource တည်ဆောက်ခြင်း

Azure Cloud Shell မှ အောက်ပါ command ကို အသုံးပြုပြီး Azure OpenAI Service resource တစ်ခုဖန်တီးပါ။

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```


#### ဤလျှောက်လွှာတွင် အသုံးပြုရန် endpoint နှင့် keys ရယူခြင်း

Azure Cloud Shell ထဲမှ အောက်ပါ command များကို run လုပ်၍ Azure OpenAI Service resource အတွက် endpoint နှင့် keys များ ရယူပါ။

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```


#### OpenAI Embedding မော်ဒယ် တပ်ဆင်ခြင်း

Azure Cloud Shell မှ အောက်ပါ command ဖြင့် OpenAI Embedding မော်ဒယ် တပ်ဆင်ပါ။

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```


## ဖြေရှင်းချက်

GitHub Codespaces တွင်ရှိသော [solution notebook](./python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) ကို ဖွင့်၍ Jupyter Notebook အတွင်း ညွှန်ကြားချက်များအတိုင်း ဆောင်ရွက်ပါ။

Notebook ကို run လုပ်သောအခါ query ရိုက်ထည့်ရန် ပြတင်းပေါ်တက်မည်။ ရိုက်ရန် input box ကို အောက်ပါအတိုင်း မြင်ရမည်ဖြစ်သည်။

![Input box for the user to input a query](../../../translated_images/my/notebook-search.1e320b9c7fcbb0bc.webp)

## အံ့သြစရာ ကောင်းပါပြီ! သင်ယူမှု ဆက်လက်လုပ်ဆောင်ပါ

ဤသင်ခန်းစာပြီးဆုံးပြီးနောက် ကျွန်ုပ်တို့၏ [Generative AI သင်ယူမှု စုစည်းမှု](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကို လေ့လာပြီး Generative AI ကျွမ်းကျင်မှုပိုမိုမြှင့်တင်ပါ!

သင်ခန်းစာ ၉ သို့ သွားပါ။ ဤနေရာတွင် [ပုံဖန်တီးခြင်းလျှောက်လွှာများ ဆောက်လုပ်နည်း](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရှုသင်ယူမည် ဖြစ်သည်!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->