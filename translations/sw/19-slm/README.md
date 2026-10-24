# Utangulizi kwa Modeli Ndogo za Lugha kwa AI Inayozalisha kwa Waanzilishi
AI Inayozalisha ni eneo la kuvutia la akili bandia ambalo linazingatia kuunda mifumo inayoweza kuzalisha maudhui mapya. Maudhui haya yanaweza kuwa maneno, picha, muziki na hata mazingira yote ya kidijitali. Moja ya matumizi yanayovutia zaidi ya AI inayozalisha ni katika sekta ya modeli za lugha.

## Modeli Ndogo za Lugha ni Nini?

Modeli Ndogo ya Lugha (SLM) ni toleo lililopunguzwa la modeli kubwa ya lugha (LLM), likitumia kanuni nyingi za usanifu na mbinu za LLMs, huku likionyesha matumizi kidogo sana ya rasilimali za kompyuta. 

SLMs ni sehemu ndogo ya modeli za lugha zilizoundwa kuzalisha maandishi yanayofanana na ya binadamu. Tofauti na marafiki zao wakubwa kama GPT-4, SLMs ni ndogo na za ufanisi zaidi, na kufanya ziwe bora kwa matumizi ambapo rasilimali za kompyuta ni ndogo. Licha ya ukubwa wao mdogo, bado wanaweza kufanya kazi mbalimbali. Kwa kawaida, SLMs hujengwa kwa kuchanganya au kuondoa sehemu za LLMs, lengo likiwa ni kuhifadhi sehemu kubwa ya utendaji wa modeli asili na uwezo wa lugha. Kupunguzwa kwa ukubwa wa modeli kunapunguza ugumu wake kwa ujumla, na kufanya SLMs ziwe bora zaidi kwa matumizi ya kumbukumbu na mahitaji ya kompyuta. Licha ya uboreshaji huu, SLMs bado zinaweza kufanya kazi anuwai katika usindikaji wa lugha asilia (NLP):

- Kizalishaji cha Maandishi: Kuunda sentensi zilizo na muundo mzuri na zinazohusiana na muktadha.
- Ukamilisho wa Maandishi: Kubashiri na kukamilisha sentensi kulingana na ombi lililotolewa.
- Tafsiri: Kubadilisha maandishi kutoka lugha moja kwenda nyingine.
- Muhtasari: Kuweka vipande virefu vya maandishi kuwa muhtasari mfupi na rahisi kuelewa.

Ingawa kuna baadhi ya kompromo la utendaji au uelewa ikilinganishwa na marafiki zao wakubwa. 

## Modeli Ndogo za Lugha Hufanya Kazi Gani?
SLMs hulazwa kwa kiasi kikubwa cha data ya maandishi. Wakati wa mafunzo, hujifunza mifumo na miundo ya lugha, iliyorahisisha kuzalisha maandishi yanayozingatia sarufi na muktadha unaofaa. Mchakato wa mafunzo unajumuisha:

- Ukusanyaji wa Data: Kusanya seti kubwa za data ya maandishi kutoka vyanzo mbalimbali.
- Usindikaji Kabla ya Mafunzo: Kusafisha na kupanga data ili ifae kwa mafunzo.
- Mafunzo: Kutumia algorithms za kujifunza kwa mashine kuwafundisha modeli jinsi ya kuelewa na kuzalisha maandishi.
- Urekebishaji: Kurekebisha modeli ili kuboresha utendaji wake katika kazi maalum.

Maendeleo ya SLMs yanajumuishwa na hitaji linaloongezeka la modeli zinazoweza kutumika katika mazingira yenye rasilimali chache kama vile vifaa vya simu au majukwaa ya edge computing, ambapo LLMs kamili zinaweza kuwa hazifanyiki kutokana na mahitaji makubwa ya rasilimali. Kwa kuzingatia ufanisi, SLMs huweka uwiano kati ya utendaji na upatikanaji, kuruhusu matumizi zaidi katika nyanja mbalimbali.

![slm](../../../translated_images/sw/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Malengo ya Kujifunza

Katika somo hili, tunatumaini kuanzisha uelewa wa SLM na kuunganishwa nayo na Microsoft Phi-3 kujifunza hali tofauti katika maudhui ya maandishi, kuona na MoE.

Mwisho wa somo hili, unapaswa kuwa na uwezo wa kujibu maswali yafuatayo:

- SLM ni nini?
- Tofauti kati ya SLM na LLM ni nini?
- Familia ya Microsoft Phi-3/3.5 ni nini?
- Jinsi ya kufanya uchambuzi kwa familia ya Microsoft Phi-3/3.5?

Tayari? Tuanzie sasa.

## Tofauti kati ya Modeli Kubwa za Lugha (LLMs) na Modeli Ndogo za Lugha (SLMs)

LLMs na SLMs zote mbili zinajengwa kwa misingi ya kujifunza kwa mashine inayotegemea uwezekano, zikifuata mbinu sawa katika usanifu, mbinu za mafunzo, michakato ya uzalishaji data, na mbinu za tathmini ya modeli. Hata hivyo, kuna mambo kadhaa muhimu yanayotofautisha aina hizi mbili za modeli.

## Matumizi ya Modeli Ndogo za Lugha

SLMs zina matumizi mengi, ikiwa ni pamoja na:

- Chatbots: Kutoa msaada kwa wateja na kuwasiliana na watumiaji kwa njia ya mazungumzo.
- Kuunda Maudhui: Kusaidia waandishi kwa kuzalisha mawazo au hata kuandika makala zote.
- Elimu: Kuwasaidia wanafunzi kwa kazi za uandishi au kujifunza lugha mpya.
- Upatikanaji: Kuunda zana kwa watu wenye ulemavu, kama mifumo ya maandishi kwenda sauti.

**Ukubwa**
  
Tofauti kuu kati ya LLMs na SLMs iko katika ukubwa wa modeli. LLMs, kama ChatGPT (GPT-4), zinaweza kuwa na vigezo takriban trilioni 1.76, wakati SLMs za chanzo wazi kama Mistral 7B zimeundwa na vigezo kidogo sana—takriban bilioni 7. Tofauti hii inatokana hasa na tofauti za usanifu wa modeli na michakato ya mafunzo. Kwa mfano, ChatGPT hutumia utaratibu wa self-attention ndani ya mfumo wa encoder-decoder, wakati Mistral 7B hutumia sliding window attention, ambayo inafanya mafunzo kuwa ya ufanisi zaidi katika modeli yenye decoder pekee. Tofauti hii ya usanifu ina maana kubwa kwa ugumu na utendaji wa modeli hizi.

**Uelewa**

SLMs kawaida huwezeshwa kufanya kazi vizuri katika nyanja maalum, na kufanya kuwa maalumu sana lakini labda na ukomo katika uwezo wa kutoa uelewa mpana wa muktadha katika nyanja mbalimbali za maarifa. Kinyume chake, LLMs lengo ni kuiga akili ya binadamu kwa kiwango pana zaidi. Zilizofunzwa kwa seti kubwa na tofauti za data, LLMs zinalenga kufanya vyema katika nyanja mbalimbali, zikitoa ubunifu zaidi na urekebishaji. Kwa hivyo, LLMs ni bora kwa aina mbalimbali za kazi, kama usindikaji wa lugha asilia na programu.

**Kuhesabu**

Mafunzo na uenezwaji wa LLMs yanahitaji rasilimali nyingi, mara nyingi zinahitaji miundombinu kubwa ya kompyuta, ikiwa ni pamoja na makundi makubwa ya GPU. Kwa mfano, kufundisha modeli kama ChatGPT kutoka mwanzo kunaweza kuhitaji maelfu ya GPU kwa vipindi virefu. Kinyume chake, SLMs, zilizokuwa na idadi ndogo ya vigezo, ni rahisi zaidi kwa rasilimali za kompyuta. Modeli kama Mistral 7B zinaweza kufundishwa na kutumika kwenye mashine za ndani zilizo na uwezo wa GPU wa wastani, ingawa mafunzo bado yanahitaji masaa kadhaa kwa GPUs nyingi.

**Upendeleo**

Upendeleo ni tatizo linalojulikana kwenye LLMs, hasa kwa sababu ya aina ya data za mafunzo. Modeli hizi mara nyingi hutumia data ghafi zilizopo mtandaoni, ambazo zinaweza kuwakosea au kutoakisi kikamilifu makundi fulani, kuanzisha lebo zisizo sahihi, au kuakisi upendeleo wa lugha kutokana na lahaja, tofauti za kijiografia, na sheria za sarufi. Zaidi ya hayo, ugumu wa usanifu wa LLM unaweza kusababisha upendeleo kuongezeka bila kujazamka ikiwa hakuna urekebishaji makini. Kwa upande mwingine, SLMs, zinazofunzwa kwa seti za data zilizobanwa na maalumu katika nyanja, mara nyingi hazina unyanyapaa mwingi kama huo, ingawa haziko salama kabisa.

**Uchambuzi**

Ukubwa mdogo wa SLMs unawawezesha kuwa na faida kubwa kwa kasi ya uchambuzi, wakiruhusu kuzalisha matokeo kwa ufanisi kwenye vifaa vya ndani bila haja ya usindikaji wa sambamba mkubwa. Kinyume chake, LLMs, kutokana na ukubwa na ugumu wao, mara nyingi huhitaji rasilimali kubwa za kompyuta sambamba kufanikisha wakati wa uchambuzi unaokubalika. Uwepo wa watumiaji wengi kwa wakati mmoja pia huongeza kuchelewa kwa LLMs, hasa zinapotumika kwa wingi.

Kwa ufupi, ingawa LLMs na SLMs zinashiriki msingi wa kujifunza kwa mashine, zinatofautiana sana katika ukubwa wa modeli, mahitaji ya rasilimali, uelewa wa muktadha, uwezekano wa upendeleo, na kasi ya uchambuzi. Tofauti hizi zinaonyesha ufanisi wao kwa matumizi tofauti, LLM zikiwa na ubunifu zaidi lakini zinahitaji rasilimali nyingi, na SLM zikiwa na ufanisi zaidi wa maeneo maalumu na mahitaji madogo ya kompyuta.

***Kumbuka: Katika somo hili, tutaanzisha SLM tukitumia Microsoft Phi-3 / 3.5 kama mfano.***

## Utangulizi wa Familia ya Phi-3 / Phi-3.5

Familia ya Phi-3 / 3.5 inalenga zaidi hali za matumizi za maandishi, kuona, na Wakala (MoE):

### Phi-3 / 3.5 Instruct

Kimsingi kwa kizalishaji cha maandishi, kukamilisha mazungumzo, na kutoa taarifa za maudhui, n.k.

**Phi-3-mini**

Modeli hii ya lugha yenye parameta 3.8B inapatikana kwenye Microsoft Foundry, Hugging Face, na Ollama. Modeli za Phi-3 zinafanya vizuri zaidi sana ikilinganishwa na modeli za lugha za ukubwa sawa au kubwa kwenye viwango muhimu (angalia nambari za kipimo hapa chini, nambari kubwa ni bora). Phi-3-mini ina fanya vyema zaidi kuliko modeli mbili za ukubwa wake, wakati Phi-3-small na Phi-3-medium zinafanya zaidi kuliko modeli kubwa, ikiwa ni pamoja na GPT-3.5.

**Phi-3-small & medium**

Kwa vigezo 7B tu, Phi-3-small inaibuka juu ya GPT-3.5T katika aina mbalimbali za nguvu za lugha, kufikiri, kuandika programu, na hesabu.

Phi-3-medium yenye vigezo 14B inaendelea na mwelekeo huu na kuizidi Gemini 1.0 Pro.

**Phi-3.5-mini**

Tunaweza kuiangalia kama uboreshaji wa Phi-3-mini. Ingawa vigezo havijabadilika, inaimarisha uwezo wa kusaidia lugha nyingi (inaunga mkono lugha zaidi ya 20: Kiarabu, Kichina, Kicheki, Kidanishi, Kiholanzi, Kiingereza, Kifini, Kifaransa, Kijerumani, Kiebrania, Kihungari, Kiitaliano, Kijapani, Kikorea, Kinorwe, Kipolandi, Kireno, Kirusi, Kihispania, Kiswidi, Kithai, Kituruki, Kiukrania) na kuongeza msaada mkali kwa muktadha mrefu.

Phi-3.5-mini yenye parameta 3.8B inaibuka juu ya modeli za lugha za ukubwa sawa na ni sawa na modeli mbili za ukubwa wake.

### Phi-3 / 3.5 Vision

Tunaweza kuangalia modeli ya Instruct ya Phi-3/3.5 kama uwezo wa Phi kuelewa, na Vision ndiyo inayoipa Phi macho ya kuelewa dunia.


**Phi-3-Vision**

Phi-3-vision, yenye parameta 4.2B tu, inaendelea na mwelekeo huu na kuizidi modeli kubwa kama Claude-3 Haiku na Gemini 1.0 Pro V katika kazi za uelewa wa picha kwa ujumla, OCR, na kazi za kuelewa meza na michoro.


**Phi-3.5-Vision**

Phi-3.5-Vision pia ni uboreshaji wa Phi-3-Vision, ikiongeza msaada kwa picha nyingi. Unaweza kuiangalia kama uboreshaji katika kuona, sio tu utaweza kuona picha, bali pia video.

Phi-3.5-vision inaibuka juu ya modeli kubwa kama Claude-3.5 Sonnet na Gemini 1.5 Flash katika kazi za OCR, kujua meza na chati na ni sawa katika kazi za uelewa wa maarifa ya kuona kwa ujumla. Inaunga mkono pembejeo za fremu nyingi, yaani, kufanya uchambuzi kwa picha nyingi.


### Phi-3.5-MoE

***Mixture of Experts(MoE)*** inaruhusu modeli kufundishwa awali kwa kutumia rasilimali chache zaidi, ambayo ina maana unaweza kuongeza ukubwa wa modeli au seti ya data kwa kiwango kikubwa kwa bajeti sawa ya rasilimali kama modeli yenye maumbo mazito. Hasa, modeli ya MoE inapaswa kufikia ubora sawa na mfano wake mzito kwa kasi zaidi wakati wa mafunzo ya awali.

Phi-3.5-MoE ina modules 16x3.8B za wataalamu. Phi-3.5-MoE yenye parameta 6.6B tu zinazotumika inafikia viwango sawa vya kufikiri, uelewa wa lugha, na hesabu kama modeli kubwa zaidi

Tunaweza kutumia modeli za familia ya Phi-3/3.5 kulingana na hali tofauti. Tofauti na LLM, unaweza kupeleka Phi-3/3.5-mini au Phi-3/3.5-Vision kwenye vifaa vya edge.


## Jinsi ya kutumia modeli za familia ya Phi-3/3.5

Tunatarajia kutumia Phi-3/3.5 katika hali tofauti. Ifuatayo, tutatumia Phi-3/3.5 kulingana na hali tofauti.

![phi3](../../../translated_images/sw/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Uchambuzi kupitia APIs za Wingu

**Modeli za Microsoft Foundry**

> **Kumbuka:** Modeli za GitHub zinaondolewa mwisho wa Julai 2026. [Modeli za Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ni mbadala wa moja kwa moja.

Modeli za Microsoft Foundry ni njia ya moja kwa moja zaidi. Unaweza kufikia haraka modeli ya Phi-3/3.5-Instruct kupitia katalogi ya modeli ya Foundry. Ikiwa unachanganya na Azure AI Inference SDK / OpenAI SDK, unaweza kufikia API kupitia msimbo ili kukamilisha mwito wa Phi-3/3.5-Instruct. Pia unaweza kujaribu athari tofauti kupitia Playground.

- Demo: Ulinganisho wa athari za Phi-3-mini na Phi-3.5-mini katika hali za Kichina

![phi3](../../../translated_images/sw/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/sw/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Au kama tunataka kutumia modeli za kuona na MoE, unaweza kutumia Microsoft Foundry kukamilisha mwito. Ikiwa una nia, unaweza kusoma Kitabu cha Mapishi cha Phi-3 kujifunza jinsi ya kuita Phi-3/3.5 Instruct, Vision, MoE kupitia Microsoft Foundry [Bonyeza kiungo hiki](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Mbali na katalogi ya modeli za Microsoft Foundry zinazotegemea wingu, unaweza pia kutumia [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) kukamilisha miito inayohusiana. Unaweza kutembelea NVIDIA NIM ili kukamilisha miito ya API ya familia ya Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) ni seti za huduma ndogo za uchambuzi zilizoendeshwa kiwezeshi kut help developers deploy AI modeli efficiently katika mazingira mbalimbali, ikiwa ni pamoja na mawingu, vituo vya data, na vituo vya kazi.

Hapa kuna baadhi ya vipengele muhimu vya NVIDIA NIM:

- **Urahisi wa Uwasilishaji:** NIM inaruhusu uanzishaji wa modeli za AI kwa amri moja, ikifanya iwe rahisi kuingiza katika mchakato uliopo.
- **Utendaji Bora:** Inatumia injini za uchambuzi zilizoboreshwa za NVIDIA, kama TensorRT na TensorRT-LLM, kuhakikisha ucheleweshaji mdogo na kasi ya juu.
- **Uwezo wa Kupanuka:** NIM inaunga mkono ukubwa wa kiotomatiki kwenye Kubernetes, ikiruhusu kushughulikia mzigo tofauti kwa ufanisi.
- **Usalama na Udhibiti:** Mashirika yanaweza kudhibiti data na programu zao kwa kuendesha mwenyewe huduma ndogo za NIM kwenye miundombinu yao iliyosimamiwa.
- **API za Kawaida:** NIM hutoa API za viwanda vya kiwango, kufanya iwe rahisi kujenga na kuunganisha programu za AI kama vile chatbots, wasaidizi wa AI, na zaidi.

NIM ni sehemu ya NVIDIA AI Enterprise, ambayo inalenga kurahisisha usambazaji na uendeshaji wa mifano ya AI, kuhakikisha inaendeshwa kwa ufanisi kwenye GPUs za NVIDIA.

- Demo: Kutumia NVIDIA NIM kuita Phi-3.5-Vision-API  [[Bonyeza kiungo hiki](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Kuendesha Phi-3/3.5 Kwenye Kompyuta Yako
Ufafanuzi wa Phi-3, au mfano wowote wa lugha kama GPT-3, unahusu mchakato wa kutoa majibu au utabiri kwa msingi wa ingizo unalopokea. Unapompa Phi-3 kauli au swali, hutumia mtandao wake wa neva uliobobea kutoa majibu yanayowezekana zaidi na yanayofaa kwa kuchambua mifumo na uhusiano katika data aliyefunzwa.

**Hugging Face Transformer**
Hugging Face Transformers ni maktaba yenye nguvu iliyoundwa kwa usindikaji wa lugha asilia (NLP) na majukumu mengine ya mashine ya kujifunza. Hapa kuna vidokezo muhimu kuhusu hiyo:

1. **Mifano Iliyoandaliwa Awali**: Inatoa maelfu ya mifano iliyofunzwa awali inayoweza kutumika kwa kazi mbalimbali kama vile uainishaji wa maandishi, utambuzi wa entiti, majibu ya maswali, muhtasari, tafsiri, na uzalishaji wa maandishi.

2. **Ushirikiano wa Mifumo**: Maktaba inaunga mkono mifumo mingi ya kujifunza kwa kina, ikiwa ni pamoja na PyTorch, TensorFlow, na JAX. Hii inakuwezesha kufundisha mfano katika mfumo mmoja na kuitumia katika mwingine.

3. **Uwezo wa Multimodal**: Mbali na NLP, Hugging Face Transformers pia inaunga mkono kazi katika kuona kwa kompyuta (kama uainishaji wa picha, utambuzi wa vitu) na usindikaji sauti (kama utambuzi wa hotuba, uainishaji wa sauti).

4. **Urahisi wa Matumizi**: Maktaba hutoa API na zana za kupakua na kurekebisha mifano kwa urahisi, hivyo inapatikana kwa wataalamu na wanaoanza.

5. **Jumuiya na Rasilimali**: Hugging Face ina jumuiya yenye mitandao na nyaraka, mafunzo, na miongozo inayosaidia watumiaji kuanza na kutumia maktaba kikamilifu.
[nyaraka rasmi](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) au [repo ya GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Hii ni njia inayotumika zaidi, lakini pia inahitaji kuharakishwa kwa GPU. Baada ya yote, hali kama Vision na MoE zinahitaji mahesabu mengi, ambayo yatachelewa sana kwenye CPU ikiwa hazitatumiwa kupunguzwa.


- Demo: Kutumia Transformer kuita Phi-3.5-Instruct [Bonyeza kiungo hiki](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Kutumia Transformer kuita Phi-3.5-Vision [Bonyeza kiungo hiki](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Kutumia Transformer kuita Phi-3.5-MoE [Bonyeza kiungo hiki](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ni jukwaa lililoundwa kurahisisha kuendesha mifano mikubwa ya lugha (LLMs) kwa karibu kwenye mashine yako. Linaunga mkono mifano mbalimbali kama Llama 3.1, Phi 3, Mistral, na Gemma 2, miongoni mwa wengine. Jukwaa hili hurahisisha mchakato kwa kuunganisha uzito wa mfano, usanidi, na data katika kifurushi kimoja, na kufanya iwe rahisi kwa watumiaji kubadilisha na kutengeneza mifano yao wenyewe. Ollama inapatikana kwa macOS, Linux, na Windows. Ni zana nzuri ikiwa unataka kujaribu au kupeleka LLM bila kutegemea huduma za wingu. Ollama ni njia ya moja kwa moja zaidi, unahitaji tu kutekeleza amri ifuatayo.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ni mfumo wa Microsoft wa kuendesha mifano kwa offline na kwenye kifaa, kama Phi, kabisa kwenye vifaa vyako - haitaji usajili wa Azure, kitufe cha API, au muunganisho wa mtandao. Huchagua mtoa huduma bora zaidi wa utekelezaji (NPU, GPU, au CPU) kiotomatiki na hutambua sehemu ya OpenAI inayofanana, ili nambari ya `openai`/Azure AI Inference SDK iliyopo iweze kuielekeza kwa mabadiliko madogo. Tazama [nyaraka za Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) kuanza.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Au tumia SDK moja kwa moja kwa Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime kwa GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) ni kiimarishaji cha mashine ya kujifunza kwa haraka wa utoaji na mafunzo unaoendeshwa kwa majukwaa mbalimbali. ONNX Runtime kwa GenAI ni zana yenye nguvu inayokusaidia kuendesha mifano ya AI ya kuzalisha kwa ufanisi katika majukwaa mbalimbali.

## ONNX Runtime ni Nini?
ONNX Runtime ni mradi wa chanzo huria unaowezesha utoaji wa kasi wa mifano ya mashine ya kujifunza. Inasaidia mifano katika umbizo la Open Neural Network Exchange (ONNX), ambalo ni kiwango kwa kuwakilisha mifano ya mashine ya kujifunza. ONNX Runtime inaweza kuharakisha uzoefu wa wateja na kupunguza gharama, ikiwaunga mkono mifano kutoka kwa mifumo ya kujifunza kwa kina kama PyTorch na TensorFlow/Keras pamoja na maktaba za kawaida za mashine ya kujifunza kama scikit-learn, LightGBM, XGBoost, n.k. ONNX Runtime inafaa na vifaa mbalimbali, madereva, na mfumo wa uendeshaji, na hutoa utendaji bora kwa kutumia viimarishaji vya vifaa pamoja na uboreshaji na mabadiliko ya mchoro.

## AI ya Kuzalisha ni Nini?
AI ya Kuzalisha inahusu mifumo ya AI inayoweza kuzalisha maudhui mapya, kama maandishi, picha, au muziki, kwa msingi wa data walizofunzwa nayo. Mifano ni pamoja na mifano ya lugha kama GPT-3 na mifano ya uzalishaji wa picha kama Stable Diffusion. Maktaba ya ONNX Runtime kwa GenAI hutoa mzunguko wa AI ya kuzalisha kwa mifano ya ONNX, ikijumuisha utoaji kwa ONNX Runtime, usindikaji wa logits, utafutaji na sampuli, na usimamizi wa KV cache.

## ONNX Runtime kwa GENAI
ONNX Runtime kwa GENAI inaongeza uwezo wa ONNX Runtime kuunga mkono mifano ya AI ya kuzalisha. Hapa kuna sifa kuu:

- **Kusaidia Majukwaa Mingi:** Inafanya kazi katika majukwaa mbalimbali, ikiwa ni pamoja na Windows, Linux, macOS, Android, na iOS.
- **Kusaidia Mifano:** Inasaidia mifano mingi maarufu ya AI ya kuzalisha, kama LLaMA, GPT-Neo, BLOOM, na zaidi.
- **Uboreshaji wa Utendaji:** Inajumuisha uboreshaji kwa viimarishaji tofauti vya vifaa kama GPUs za NVIDIA, GPUs za AMD, na zaidi2.
- **Urahisi wa Matumizi:** Inatoa API kwa usawa rahisi katika programu, kuwezesha kuzalisha maandishi, picha, na maudhui mengine kwa kutumia nambari kidogo
- Watumiaji wanaweza kuita njia ya juu ya generate(), au kuendesha kila mzunguko wa mfano katika mduara, wakizalisha tokeni moja kwa wakati, na hiari kusasisha vigezo vya uzalishaji ndani ya mduara.
- ONNX runtime pia inaunga mkono utafutaji wa greedy/beam na sampuli za TopP, TopK kuzalisha mfululizo wa tokeni na usindikaji wa logits uliojengwa kama adhabu za kurudia. Unaweza pia kuongeza alama za kibinafsi kwa urahisi.

## Kuanzia
Kuanzia na ONNX Runtime kwa GENAI, unaweza kufuata hatua hizi:

### Sakinisha ONNX Runtime:
```Python
pip install onnxruntime
```
### Sakinisha Upanuzi wa AI ya Kuzalisha:
```Python
pip install onnxruntime-genai
```

### Endesha Mfano: Hapa kuna mfano rahisi kwa Python:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo:Kutumia ONNX Runtime GenAI kuita Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Nyingine**

Mbali na ONNX Runtime, Ollama, na mbinu za rejea za Foundry Local, tunaweza pia kukamilisha rejea za mifano ya kiasi kwa kutumia mbinu za rejea za mifano zinazotolewa na watengenezaji mbalimbali. Kama vile mfumo wa Apple MLX na Apple Metal, Qualcomm QNN na NPU, Intel OpenVINO na CPU/GPU, n.k. Pia unaweza kupata maudhui zaidi kutoka [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Zaidi

Tumepata maarifa ya msingi ya Familia ya Phi-3/3.5, lakini kujifunza zaidi kuhusu SLM tunahitaji maarifa zaidi. Unaweza kupata majibu katika Phi-3 Cookbook. Ikiwa unataka kujifunza zaidi, tafadhali tembelea [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->