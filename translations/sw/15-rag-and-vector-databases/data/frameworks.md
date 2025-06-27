<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:08:31+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sw"
}
-->
# Mfumo wa Mitandao ya Neural

Kama tulivyojifunza tayari, ili kuweza kufundisha mitandao ya neural kwa ufanisi tunahitaji kufanya mambo mawili:

* Kufanya kazi kwenye tensors, mfano kuzidisha, kuongeza, na kuhesabu baadhi ya kazi kama sigmoid au softmax
* Kuhesabu gradients za maelezo yote, ili kutekeleza optimizim ya gradient descent

Wakati maktaba ya `numpy` inaweza kufanya sehemu ya kwanza, tunahitaji baadhi ya utaratibu wa kuhesabu gradients. Katika mfumo wetu ambao tumetengeneza katika sehemu iliyopita tulilazimika kuandika kwa mkono kazi zote za derivative ndani ya njia ya `backward`, ambayo inafanya backpropagation. Kwa hali bora, mfumo unapaswa kutupa fursa ya kuhesabu gradients za *maelezo yoyote* ambayo tunaweza kufafanua.

Jambo lingine muhimu ni uwezo wa kufanya hesabu kwenye GPU, au vitengo vingine maalum vya hesabu, kama TPU. Mafunzo ya mitandao ya neural inahitaji *hesabu nyingi*, na uwezo wa kuratibu hesabu hizo kwenye GPUs ni muhimu sana.

> ✅ Neno 'parallelize' linamaanisha kusambaza hesabu kwenye vifaa vingi.

Kwa sasa, mifumo miwili maarufu zaidi ya neural ni: TensorFlow na PyTorch. Zote mbili zinatoa API ya kiwango cha chini ya kufanya kazi na tensors kwenye CPU na GPU. Juu ya API ya kiwango cha chini, kuna pia API ya kiwango cha juu, inayoitwa Keras na PyTorch Lightning mtawalia.

API ya Kiwango cha Chini | TensorFlow| PyTorch
-------------------------|-------------------------------------|--------------------------------
API ya Kiwango cha Juu| Keras| Pytorch

**APIs za kiwango cha chini** katika mifumo yote miwili zinakuruhusu kujenga kinachoitwa **computational graphs**. Grafu hii inafafanua jinsi ya kuhesabu matokeo (kwa kawaida kazi ya hasara) na vigezo vya ingizo vilivyotolewa, na inaweza kusukumwa kwa hesabu kwenye GPU, ikiwa inapatikana. Kuna kazi za kutofautisha grafu hii ya hesabu na kuhesabu gradients, ambazo zinaweza kutumika kwa kuoptimiza vigezo vya mfano.

**APIs za kiwango cha juu** kwa kiasi kikubwa zinazingatia mitandao ya neural kama **mlolongo wa tabaka**, na hufanya kujenga mitandao mingi ya neural kuwa rahisi zaidi. Kufundisha mfano kwa kawaida kunahitaji kuandaa data na kisha kupiga kazi ya `fit` ili kufanya kazi.

API ya kiwango cha juu inakuruhusu kujenga mitandao ya neural ya kawaida haraka sana bila kuwa na wasiwasi kuhusu maelezo mengi. Wakati huo huo, API ya kiwango cha chini inatoa udhibiti zaidi juu ya mchakato wa mafunzo, na hivyo zinatumiwa sana katika utafiti, unaposhughulika na miundo mipya ya mitandao ya neural.

Ni muhimu pia kuelewa kwamba unaweza kutumia APIs zote mbili pamoja, mfano unaweza kutengeneza usanifu wako wa tabaka la mtandao kwa kutumia API ya kiwango cha chini, na kisha kuitumia ndani ya mtandao mkubwa uliojengwa na kufundishwa na API ya kiwango cha juu. Au unaweza kufafanua mtandao kwa kutumia API ya kiwango cha juu kama mlolongo wa tabaka, na kisha kutumia mzunguko wako wa mafunzo wa kiwango cha chini ili kutekeleza optimizim. APIs zote mbili zinatumia dhana za msingi sawa, na zimeundwa kufanya kazi vizuri pamoja.

## Kujifunza

Katika kozi hii, tunatoa maudhui mengi kwa PyTorch na TensorFlow. Unaweza kuchagua mfumo unaopendelea na kupitia vitabu vya mazoezi vinavyohusiana tu. Ikiwa huna uhakika ni mfumo gani wa kuchagua, soma baadhi ya mijadala kwenye mtandao kuhusu **PyTorch vs. TensorFlow**. Unaweza pia kuangalia mifumo yote miwili ili kupata ufahamu bora.

Ikiwezekana, tutatumia APIs za Kiwango cha Juu kwa urahisi. Hata hivyo, tunaamini ni muhimu kuelewa jinsi mitandao ya neural inavyofanya kazi kutoka mwanzo, hivyo mwanzoni tunaanza kwa kufanya kazi na API ya kiwango cha chini na tensors. Hata hivyo, ikiwa unataka kuanza haraka na hutaki kutumia muda mwingi kujifunza maelezo haya, unaweza kuruka hayo na kwenda moja kwa moja kwenye vitabu vya mazoezi vya API ya kiwango cha juu.

## ✍️ Mazoezi: Mifumo

Endelea kujifunza katika vitabu vya mazoezi vifuatavyo:

API ya Kiwango cha Chini | TensorFlow+Keras Notebook | PyTorch
-------------------------|-------------------------------------|--------------------------------
API ya Kiwango cha Juu| Keras | *PyTorch Lightning*

Baada ya kufanikiwa katika mifumo, hebu turejee dhana ya overfitting.

# Overfitting

Overfitting ni dhana muhimu sana katika ujifunzaji wa mashine, na ni muhimu sana kuipata kwa usahihi!

Fikiria tatizo lifuatalo la kukadiria nukta 5 (zinazoonyeshwa na `x` kwenye grafu zifuatazo):

!linear | overfit
-------------------------|--------------------------
**Mfano wa Linear, vigezo 2** | **Mfano usio wa Linear, vigezo 7**
Makosa ya mafunzo = 5.3 | Makosa ya mafunzo = 0
Makosa ya uthibitishaji = 5.1 | Makosa ya uthibitishaji = 20

* Kushoto, tunaona ukadiriaji mzuri wa mstari wa moja kwa moja. Kwa sababu idadi ya vigezo inatosha, mfano unapata wazo nyuma ya usambazaji wa nukta kwa usahihi.
* Kulia, mfano ni wenye nguvu kupita kiasi. Kwa sababu tuna nukta 5 tu na mfano una vigezo 7, inaweza kujiweka katika njia ambayo inapita kwenye nukta zote, kufanya makosa ya mafunzo kuwa 0. Hata hivyo, hii inazuia mfano kuelewa muundo sahihi nyuma ya data, hivyo makosa ya uthibitishaji ni makubwa sana.

Ni muhimu sana kupata usawa sahihi kati ya utajiri wa mfano (idadi ya vigezo) na idadi ya sampuli za mafunzo.

## Kwa nini overfitting hutokea

  * Data ya mafunzo haitoshi
  * Mfano wenye nguvu kupita kiasi
  * Kelele nyingi katika data ya ingizo

## Jinsi ya kugundua overfitting

Kama unavyoona kutoka kwenye grafu hapo juu, overfitting inaweza kugunduliwa na makosa ya mafunzo ya chini sana, na makosa ya uthibitishaji ya juu. Kwa kawaida wakati wa mafunzo tutaona makosa ya mafunzo na uthibitishaji yakianza kupungua, na kisha kwa wakati fulani makosa ya uthibitishaji yanaweza kuacha kupungua na kuanza kupanda. Hii itakuwa ishara ya overfitting, na kiashiria kwamba tunapaswa kuacha mafunzo kwa wakati huu (au angalau kufanya snapshot ya mfano).

## Jinsi ya kuzuia overfitting

Ikiwa unaona kwamba overfitting inatokea, unaweza kufanya mojawapo ya yafuatayo:

 * Ongeza kiasi cha data ya mafunzo
 * Punguza ugumu wa mfano
 * Tumia mbinu za regularization, kama Dropout, ambayo tutazingatia baadaye.

## Overfitting na Bias-Variance Tradeoff

Overfitting kwa kweli ni kesi ya tatizo la jumla zaidi katika takwimu linaloitwa Bias-Variance Tradeoff. Ikiwa tutazingatia vyanzo vinavyowezekana vya makosa katika mfano wetu, tunaweza kuona aina mbili za makosa:

* **Makosa ya Bias** yanayosababishwa na algorithm yetu kushindwa kukamata uhusiano kati ya data ya mafunzo kwa usahihi. Inaweza kutokea kutokana na ukweli kwamba mfano wetu hauna nguvu ya kutosha (**underfitting**).
* **Makosa ya Variance**, ambayo yanatokana na mfano kukadiria kelele katika data ya ingizo badala ya uhusiano wa maana (**overfitting**).

Wakati wa mafunzo, makosa ya bias yanapungua (kama mfano wetu unajifunza kukadiria data), na makosa ya variance yanaongezeka. Ni muhimu kuacha mafunzo - ama kwa mkono (tunapogundua overfitting) au kiotomatiki (kwa kuanzisha regularization) - ili kuzuia overfitting.

## Hitimisho

Katika somo hili, umejifunza kuhusu tofauti kati ya APIs mbalimbali kwa mifumo miwili maarufu zaidi ya AI, TensorFlow na PyTorch. Aidha, umejifunza kuhusu mada muhimu sana, overfitting.

## 🚀 Changamoto

Katika vitabu vya mazoezi vinavyosindikiza, utapata 'majukumu' chini; pitia vitabu vya mazoezi na kamilisha majukumu.

## Tathmini & Kujisomea

Fanya utafiti juu ya mada zifuatazo:

- TensorFlow
- PyTorch
- Overfitting

Jiulize maswali yafuatayo:

- Ni tofauti gani kati ya TensorFlow na PyTorch?
- Ni tofauti gani kati ya overfitting na underfitting?

## Kazi

Katika maabara hii, unaombwa kutatua matatizo mawili ya uainishaji kwa kutumia mitandao iliyounganishwa kikamilifu yenye tabaka moja na nyingi kwa kutumia PyTorch au TensorFlow.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya kibinadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.