<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:35:39+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sw"
}
-->
# Neural Network Frameworks

Kama tulivyoshajifunza, ili kuweza kufundisha mitandao ya neva kwa ufanisi tunahitaji kufanya mambo mawili:

* Kufanya kazi na tensors, mfano kuzidisha, kuongeza, na kuhesabu baadhi ya kazi kama sigmoid au softmax
* Kuongeza gradients za maelezo yote, ili kufanya uboreshaji wa gradient descent

Wakati maktaba ya `numpy` inaweza kufanya sehemu ya kwanza, tunahitaji njia ya kuhesabu gradients. Katika mfumo wetu tuliouunda katika sehemu iliyopita tulilazimika kuandika programu kwa mikono kazi zote za derivative ndani ya njia ya `backward`, ambayo hufanya backpropagation. Kwa kawaida, mfumo unapaswa kutupa fursa ya kuhesabu gradients za *maelezo yoyote* tunayoweza kufafanua.

Jambo lingine muhimu ni uwezo wa kufanya mahesabu kwenye GPU, au vyombo vingine maalum vya kompyuta, kama TPU. Mafunzo ya mitandao ya neva ya kina yanahitaji *mahesabu mengi*, na uwezo wa kuendesha mahesabu hayo kwa usawa kwenye GPUs ni muhimu sana.

> ✅ Neno 'parallelize' linamaanisha kugawanya mahesabu kwenye vifaa vingi.

Hivi sasa, mifumo miwili maarufu zaidi ya mitandao ya neva ni: TensorFlow na PyTorch. Zote hutoa API ya kiwango cha chini ya kufanya kazi na tensors kwenye CPU na GPU. Juu ya API ya kiwango cha chini, kuna pia API ya kiwango cha juu, inayoitwa Keras na PyTorch Lightning mtawalia.

Low-Level API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras| Pytorch

**API za kiwango cha chini** katika mifumo yote hutoa uwezo wa kujenga kinachoitwa **michoro ya mahesabu**. Mchoro huu unaeleza jinsi ya kuhesabu matokeo (kawaida ni kazi ya hasara) kwa kutumia vigezo vilivyotolewa, na unaweza kusukumwa kwa mahesabu kwenye GPU, ikiwa ipo. Kuna kazi za kutofautisha mchoro huu wa mahesabu na kuhesabu gradients, ambazo zinaweza kutumika baadaye kuboresha vigezo vya modeli.

**API za kiwango cha juu** kwa kiasi kikubwa huchukulia mitandao ya neva kama **mlolongo wa tabaka**, na hufanya ujenzi wa mitandao mingi ya neva kuwa rahisi zaidi. Mafunzo ya modeli kawaida yanahitaji kuandaa data kisha kuita kazi ya `fit` kufanya kazi hiyo.

API ya kiwango cha juu inakuwezesha kujenga mitandao ya kawaida ya neva haraka bila wasiwasi wa maelezo mengi. Wakati huo huo, API ya kiwango cha chini hutoa udhibiti zaidi juu ya mchakato wa mafunzo, na kwa hivyo hutumika sana katika utafiti, hasa unaposhughulika na miundo mipya ya mitandao ya neva.

Ni muhimu pia kuelewa kwamba unaweza kutumia API zote mbili pamoja, mfano unaweza kuunda usanifu wa tabaka la mtandao wako kwa kutumia API ya kiwango cha chini, kisha kuitumia ndani ya mtandao mkubwa uliotengenezwa na kufunzwa kwa API ya kiwango cha juu. Au unaweza kufafanua mtandao kwa kutumia API ya kiwango cha juu kama mlolongo wa tabaka, kisha kutumia mzunguko wako wa mafunzo wa kiwango cha chini kufanya uboreshaji. API zote mbili zinatumia dhana za msingi zinazofanana, na zimetengenezwa kufanya kazi pamoja vizuri.

## Kujifunza

Katika kozi hii, tunatoa maudhui mengi kwa PyTorch na TensorFlow. Unaweza kuchagua mfumo unaopendelea na kupitia tu daftari zinazohusiana. Ikiwa huna uhakika ni mfumo gani kuchagua, soma mijadala kwenye mtandao kuhusu **PyTorch vs. TensorFlow**. Pia unaweza kuangalia mifumo yote miwili kupata uelewa bora.

Pale panapowezekana, tutatumia API za Kiwango cha Juu kwa urahisi. Hata hivyo, tunaamini ni muhimu kuelewa jinsi mitandao ya neva inavyofanya kazi kutoka mwanzo, hivyo mwanzoni tunaanza kwa kufanya kazi na API ya kiwango cha chini na tensors. Lakini, ikiwa unataka kuanza haraka na hutaki kutumia muda mwingi kujifunza maelezo haya, unaweza kuruka na kuingia moja kwa moja kwenye daftari za API ya kiwango cha juu.

## ✍️ Mazoezi: Frameworks

Endelea kujifunza katika daftari zifuatazo:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

Baada ya kumudu mifumo, tuchambue tena dhana ya overfitting.

# Overfitting

Overfitting ni dhana muhimu sana katika kujifunza mashine, na ni muhimu sana kuelewa vizuri!

Tazama tatizo lifuatalo la kukisia nukta 5 (zinazoonyeshwa na `x` kwenye michoro hapa chini):

!linear | overfit
-------------------------|--------------------------
**Mfano wa mstari, vigezo 2** | **Mfano usio wa mstari, vigezo 7**
Kosa la mafunzo = 5.3 | Kosa la mafunzo = 0
Kosa la uhakiki = 5.1 | Kosa la uhakiki = 20

* Kushoto, tunaona makisio mazuri ya mstari wa moja kwa moja. Kwa sababu idadi ya vigezo ni ya kutosha, modeli inapata wazo sahihi kuhusu usambazaji wa nukta.
* Kulia, modeli ni yenye nguvu sana. Kwa sababu tuna nukta 5 tu na modeli ina vigezo 7, inaweza kubadilika kwa njia ya kupita kwenye nukta zote, na kufanya kosa la mafunzo kuwa 0. Hata hivyo, hii inazuia modeli kuelewa muundo sahihi wa data, hivyo kosa la uhakiki ni kubwa sana.

Ni muhimu sana kupata usawa sahihi kati ya utajiri wa modeli (idadi ya vigezo) na idadi ya sampuli za mafunzo.

## Kwa nini overfitting hutokea

  * Data ya mafunzo haitoshi
  * Modeli yenye nguvu sana
  * Sauti nyingi sana katika data ya ingizo

## Jinsi ya kugundua overfitting

Kama unavyoona kwenye mchoro hapo juu, overfitting inaweza kugunduliwa kwa kosa la mafunzo kuwa chini sana, na kosa la uhakiki kuwa juu. Kawaida wakati wa mafunzo tutaona makosa ya mafunzo na uhakiki yakiendelea kupungua, kisha mahali fulani kosa la uhakiki linaweza kuacha kupungua na kuanza kuongezeka. Hii itakuwa ishara ya overfitting, na dalili kwamba tunapaswa kuacha mafunzo hapo (au angalau kuchukua picha ya modeli).

overfitting

## Jinsi ya kuzuia overfitting

Ikiwa unaona overfitting inatokea, unaweza kufanya mojawapo ya yafuatayo:

 * Ongeza kiasi cha data ya mafunzo
 * Punguza ugumu wa modeli
 * Tumia mbinu za kuzuia overfitting, kama Dropout, ambayo tutazungumzia baadaye.

## Overfitting na Mkataba wa Bias-Variance

Overfitting ni mfano wa tatizo pana zaidi katika takwimu linaloitwa Bias-Variance Tradeoff. Tukichunguza chanzo cha makosa katika modeli yetu, tunaweza kuona makosa mawili:

* **Makosa ya Bias** husababishwa na algorithm yetu kushindwa kushikilia uhusiano kati ya data ya mafunzo kwa usahihi. Hii inaweza kutokana na modeli kuwa dhaifu sana (**underfitting**).
* **Makosa ya Variance**, ambayo husababishwa na modeli kukisia kelele katika data badala ya uhusiano halisi (**overfitting**).

Wakati wa mafunzo, kosa la bias hupungua (kama modeli inajifunza kukisia data), na kosa la variance huongezeka. Ni muhimu kuacha mafunzo - ama kwa mikono (tunapogundua overfitting) au kwa njia ya moja kwa moja (kwa kuanzisha mbinu za kuzuia) - ili kuzuia overfitting.

## Hitimisho

Katika somo hili, umejifunza tofauti kati ya API mbalimbali za mifumo miwili maarufu ya AI, TensorFlow na PyTorch. Zaidi ya hayo, umejifunza kuhusu mada muhimu sana, overfitting.

## 🚀 Changamoto

Katika daftari zinazohusiana, utapata 'kazi' chini; fanya kazi kupitia daftari na ukamilishe kazi hizo.

## Mapitio & Kujifunza Binafsi

Fanya utafiti kuhusu mada zifuatazo:

- TensorFlow
- PyTorch
- Overfitting

Jiulize maswali haya:

- Tofauti gani kati ya TensorFlow na PyTorch?
- Tofauti gani kati ya overfitting na underfitting?

## Kazi ya Nyumbani

Katika maabara hii, unahitajika kutatua matatizo mawili ya uainishaji kwa kutumia mitandao ya fully-connected yenye tabaka moja au zaidi kwa kutumia PyTorch au TensorFlow.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.