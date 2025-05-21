<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:05:13+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sw"
}
-->
# Mfumo wa Mitandao ya Neural

Kama tulivyojifunza tayari, ili kuweza kufundisha mitandao ya neural kwa ufanisi tunahitaji kufanya mambo mawili:

* Kufanya kazi na tensors, mfano kuzidisha, kuongeza, na kuhesabu baadhi ya kazi kama sigmoid au softmax
* Kuhesabu gradients za maelezo yote, ili kufanya uboreshaji wa gradient descent

Wakati maktaba ya `numpy` inaweza kufanya sehemu ya kwanza, tunahitaji baadhi ya mbinu za kuhesabu gradients. Katika mfumo wetu tuliouendeleza katika sehemu iliyopita tulilazimika kupanga programu za derivatives zote ndani ya njia ya `backward`, ambayo inafanya backpropagation. Kimsingi, mfumo unapaswa kutupa fursa ya kuhesabu gradients za *maelezo yoyote* ambayo tunaweza kufafanua.

Jambo lingine muhimu ni kuweza kufanya hesabu kwenye GPU, au vitengo vingine maalum vya hesabu, kama TPU. Mafunzo ya mitandao ya neural inahitaji *hesabu nyingi sana*, na kuweza kuratibu hesabu hizo kwenye GPUs ni muhimu sana.

> ✅ Neno 'kuratibu' linamaanisha kusambaza hesabu kwenye vifaa vingi.

Kwa sasa, mifumo miwili maarufu ya neural ni: TensorFlow na PyTorch. Zote zinatoa API ya kiwango cha chini kufanya kazi na tensors kwenye CPU na GPU. Juu ya API ya kiwango cha chini, kuna API ya kiwango cha juu, inayoitwa Keras na PyTorch Lightning mtawalia.

Low-Level API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras| Pytorch

**Low-level APIs** katika mifumo yote miwili inakuwezesha kujenga kinachoitwa **grafu za hesabu**. Grafu hii inafafanua jinsi ya kuhesabu matokeo (kawaida kazi ya hasara) kwa kutumia vigezo vilivyotolewa, na inaweza kusukumwa kwa hesabu kwenye GPU, ikiwa inapatikana. Kuna kazi za kutofautisha grafu hii ya hesabu na kuhesabu gradients, ambazo zinaweza kutumika kwa kuboresha vigezo vya modeli.

**High-level APIs** kimsingi huzingatia mitandao ya neural kama **mlolongo wa tabaka**, na kufanya ujenzi wa mitandao mingi ya neural kuwa rahisi zaidi. Kufundisha modeli kawaida kunahitaji kuandaa data na kisha kuita kazi ya `fit` kufanya kazi.

API ya kiwango cha juu inakuwezesha kujenga mitandao ya neural ya kawaida haraka sana bila kujali maelezo mengi. Wakati huo huo, API ya kiwango cha chini inatoa udhibiti zaidi juu ya mchakato wa mafunzo, na hivyo zinatumiwa sana katika utafiti, unapo husika na miundo mipya ya mitandao ya neural.

Pia ni muhimu kuelewa kuwa unaweza kutumia API zote mbili pamoja, mfano unaweza kuendeleza muundo wako wa tabaka la mtandao kwa kutumia API ya kiwango cha chini, na kisha kuitumia ndani ya mtandao mkubwa ulioundwa na kufundishwa na API ya kiwango cha juu. Au unaweza kufafanua mtandao kwa kutumia API ya kiwango cha juu kama mlolongo wa tabaka, na kisha kutumia mzunguko wako wa mafunzo wa kiwango cha chini kufanya uboreshaji. API zote mbili zinatumia dhana za msingi zinazofanana, na zimeundwa kufanya kazi vizuri pamoja.

## Kujifunza

Katika kozi hii, tunatoa maudhui mengi kwa PyTorch na TensorFlow. Unaweza kuchagua mfumo unaopendelea na kupitia tu vitabu vya maandishi vinavyohusiana. Ikiwa huna uhakika ni mfumo gani wa kuchagua, soma baadhi ya mijadala kwenye mtandao kuhusu **PyTorch vs. TensorFlow**. Pia unaweza kuangalia mifumo yote miwili ili kupata uelewa bora.

Pale inapowezekana, tutatumia API za Kiwango cha Juu kwa urahisi. Hata hivyo, tunaamini ni muhimu kuelewa jinsi mitandao ya neural inavyofanya kazi kutoka chini, hivyo mwanzoni tunaanza kwa kufanya kazi na API ya kiwango cha chini na tensors. Hata hivyo, ikiwa unataka kuanza haraka na hutaki kutumia muda mwingi kujifunza maelezo haya, unaweza kuruka na kwenda moja kwa moja kwenye vitabu vya maandishi vya API ya kiwango cha juu.

## ✍️ Mazoezi: Mifumo

Endelea kujifunza katika vitabu vya maandishi vifuatavyo:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

Baada ya kuweza mifumo, hebu tukumbuke dhana ya overfitting.

# Overfitting

Overfitting ni dhana muhimu sana katika ujifunzaji wa mashine, na ni muhimu sana kuielewa vizuri!

Fikiria tatizo lifuatalo la kukadiria nukta 5 (zilizowakilishwa na `x` kwenye grafu zifuatazo):

!linear | overfit
-------------------------|--------------------------
**Modeli ya Linear, vigezo 2** | **Modeli isiyo ya Linear, vigezo 7**
Makosa ya mafunzo = 5.3 | Makosa ya mafunzo = 0
Makosa ya uthibitishaji = 5.1 | Makosa ya uthibitishaji = 20

* Kushoto, tunaona makadirio mazuri ya mstari wa moja kwa moja. Kwa sababu idadi ya vigezo ni ya kutosha, modeli inapata wazo nyuma ya usambazaji wa nukta vizuri.
* Kulia, modeli ni yenye nguvu sana. Kwa sababu tuna nukta 5 tu na modeli ina vigezo 7, inaweza kurekebisha kwa namna ya kupita kwenye nukta zote, na kufanya makosa ya mafunzo kuwa 0. Hata hivyo, hii inazuia modeli kuelewa muundo sahihi nyuma ya data, hivyo makosa ya uthibitishaji ni ya juu sana.

Ni muhimu sana kupata usawa sahihi kati ya utajiri wa modeli (idadi ya vigezo) na idadi ya sampuli za mafunzo.

## Kwa nini overfitting hutokea

  * Data ya mafunzo haitoshi
  * Modeli yenye nguvu sana
  * Kelele nyingi katika data ya ingizo

## Jinsi ya kugundua overfitting

Kama unavyoona kutoka kwenye grafu hapo juu, overfitting inaweza kugunduliwa na makosa ya mafunzo ya chini sana, na makosa ya uthibitishaji ya juu. Kawaida wakati wa mafunzo tutaona makosa ya mafunzo na uthibitishaji yakianza kupungua, na kisha kwa wakati fulani makosa ya uthibitishaji yanaweza kuacha kupungua na kuanza kupanda. Hii itakuwa ishara ya overfitting, na kiashiria kwamba tunapaswa kuacha mafunzo wakati huu (au angalau kufanya snapshot ya modeli).

## Jinsi ya kuzuia overfitting

Ikiwa unaweza kuona kwamba overfitting inatokea, unaweza kufanya moja ya yafuatayo:

 * Ongeza idadi ya data ya mafunzo
 * Punguza ugumu wa modeli
 * Tumia mbinu za kudhibiti, kama Dropout, ambayo tutazingatia baadaye.

## Overfitting na Bias-Variance Tradeoff

Overfitting kwa kweli ni kesi ya tatizo la jumla zaidi katika takwimu linaloitwa Bias-Variance Tradeoff. Ikiwa tunazingatia vyanzo vinavyowezekana vya makosa katika modeli yetu, tunaweza kuona aina mbili za makosa:

* **Makosa ya Bias** husababishwa na algorithimu yetu kushindwa kukamata uhusiano kati ya data ya mafunzo kwa usahihi. Inaweza kusababishwa na ukweli kwamba modeli yetu si yenye nguvu ya kutosha (**underfitting**).
* **Makosa ya Variance**, ambayo husababishwa na modeli kukadiria kelele katika data ya ingizo badala ya uhusiano wa maana (**overfitting**).

Wakati wa mafunzo, makosa ya bias hupungua (kama modeli yetu inajifunza kukadiria data), na makosa ya variance huongezeka. Ni muhimu kuacha mafunzo - ama kwa mikono (tunapogundua overfitting) au kiotomatiki (kwa kuanzisha udhibiti) - ili kuzuia overfitting.

## Hitimisho

Katika somo hili, umejifunza kuhusu tofauti kati ya API mbalimbali kwa mifumo miwili maarufu ya AI, TensorFlow na PyTorch. Aidha, umejifunza kuhusu mada muhimu sana, overfitting.

## 🚀 Changamoto

Katika vitabu vya maandishi vinavyoambatana, utapata 'majukumu' chini; pitia vitabu vya maandishi na kamilisha majukumu.

## Tathmini & Kujisomea

Fanya utafiti kuhusu mada zifuatazo:

- TensorFlow
- PyTorch
- Overfitting

Jiulize maswali yafuatayo:

- Ni tofauti gani kati ya TensorFlow na PyTorch?
- Ni tofauti gani kati ya overfitting na underfitting?

## Jukumu

Katika maabara hii, unaombwa kutatua matatizo mawili ya uainishaji kwa kutumia mitandao ya fully-connected ya tabaka moja na nyingi kwa kutumia PyTorch au TensorFlow.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuelewana. Hati asilia katika lugha yake ya kiasili inapaswa kuzingatiwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya kibinadamu inapendekezwa. Hatuwajibiki kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.