<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:29:02+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sw"
}
-->
# Utangulizi wa Mitandao ya Neva. Perceptron ya Tabaka Nyingi

Katika sehemu iliyopita, ulijifunza kuhusu mtindo rahisi zaidi wa mtandao wa neva - perceptron ya tabaka moja, mtindo wa uainishaji wa tabaka mbili wa mstari.

Katika sehemu hii tutapanua mtindo huu katika mfumo unaonyumbulika zaidi, utakaotuwezesha:

* kufanya **uainishaji wa tabaka nyingi** kwa kuongeza tabaka mbili
* kutatua **matatizo ya urejeleaji** kwa kuongeza uainishaji
* kutenganisha tabaka ambazo haziwezi kutenganishwa kimstari

Tutaunda pia mfumo wetu wa moduli katika Python ambao utatuwezesha kujenga usanifu tofauti wa mitandao ya neva.

## Urasmishaji wa Kujifunza kwa Mashine

Tuanze kwa kurasmisha tatizo la Kujifunza kwa Mashine. Tuseme tuna seti ya mafunzo **X** yenye lebo **Y**, na tunahitaji kujenga mtindo *f* ambao utatoa utabiri sahihi zaidi. Ubora wa utabiri hupimwa na **Kazi ya Hasara** ℒ. Kazi za hasara zifuatazo hutumiwa mara nyingi:

* Kwa tatizo la urejeleaji, tunapohitaji kutabiri namba, tunaweza kutumia **makosa ya wastani** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, au **makosa ya mraba** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Kwa uainishaji, tunatumia **hasara ya 0-1** (ambayo kimsingi ni sawa na **usahihi** wa mtindo), au **hasara ya logisti**.

Kwa perceptron ya kiwango kimoja, kazi *f* ilifafanuliwa kama kazi ya mstari *f(x)=wx+b* (hapa *w* ni matriki ya uzito, *x* ni vekta ya vipengele vya ingizo, na *b* ni vekta ya upendeleo). Kwa usanifu tofauti wa mitandao ya neva, kazi hii inaweza kuchukua fomu ngumu zaidi.

> Katika hali ya uainishaji, mara nyingi ni vyema kupata uwezekano wa tabaka zinazohusiana kama pato la mtandao. Ili kubadilisha namba za kiholela kuwa uwezekano (kwa mfano, ili kusawazisha pato), mara nyingi tunatumia kazi ya **softmax** σ, na kazi *f* inakuwa *f(x)=σ(wx+b)*

Katika ufafanuzi wa *f* hapo juu, *w* na *b* huitwa **vigezo** θ=⟨*w,b*⟩. Kwa kuzingatia seti ya data ⟨**X**,**Y**⟩, tunaweza kuhesabu kosa la jumla kwenye seti nzima ya data kama kazi ya vigezo θ.

> ✅ **Lengo la mafunzo ya mtandao wa neva ni kupunguza kosa kwa kubadilisha vigezo θ**

## Uboreshaji wa Kupungua kwa Gradienti

Kuna njia inayojulikana ya uboreshaji wa kazi inayoitwa **kupungua kwa gradienti**. Wazo ni kwamba tunaweza kuhesabu mnyambuliko (katika hali ya vipimo vingi inayoitwa **gradienti**) ya kazi ya hasara kwa heshima na vigezo, na kubadilisha vigezo kwa njia ambayo kosa litapungua. Hii inaweza kurasmishwa kama ifuatavyo:

* Anzisha vigezo kwa baadhi ya thamani za nasibu w<sup>(0)</sup>, b<sup>(0)</sup>
* Rudia hatua ifuatayo mara nyingi:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Wakati wa mafunzo, hatua za uboreshaji zinapaswa kuhesabiwa kwa kuzingatia seti nzima ya data (kumbuka kuwa hasara inahesabiwa kama jumla kupitia sampuli zote za mafunzo). Hata hivyo, katika maisha halisi tunachukua sehemu ndogo za seti ya data inayoitwa **minibatches**, na kuhesabu gradienti kwa msingi wa sehemu ndogo ya data. Kwa sababu sehemu ndogo huchukuliwa kiholela kila wakati, njia hii inaitwa **kupungua kwa gradienti kwa nasibu** (SGD).

## Perceptrons za Tabaka Nyingi na Kurudisha Nyuma

Mtandao wa tabaka moja, kama tulivyoona hapo juu, una uwezo wa kuainisha tabaka zinazoweza kutenganishwa kimstari. Ili kujenga mtindo tajiri zaidi, tunaweza kuchanganya tabaka kadhaa za mtandao. Kihisabati, itamaanisha kuwa kazi *f* itakuwa na fomu ngumu zaidi, na itahesabiwa katika hatua kadhaa:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Hapa, α ni **kazi ya uanzishaji isiyo ya mstari**, σ ni kazi ya softmax, na vigezo θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoriti ya kupungua kwa gradienti itabaki kuwa ile ile, lakini itakuwa ngumu zaidi kuhesabu gradienti. Kwa kuzingatia kanuni ya mnyambuliko wa mnyororo, tunaweza kuhesabu mnyambuliko kama ifuatavyo:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kanuni ya mnyambuliko wa mnyororo inatumika kuhesabu mnyambuliko ya kazi ya hasara kwa heshima na vigezo.

Kumbuka kuwa sehemu ya kushoto zaidi ya maelezo hayo yote ni sawa, na hivyo tunaweza kuhesabu mnyambuliko kwa ufanisi kuanzia kazi ya hasara na kwenda "nyuma" kupitia grafu ya hesabu. Hivyo njia ya kufundisha perceptron ya tabaka nyingi inaitwa **kurudisha nyuma**, au 'backprop'.

> TODO: marejeleo ya picha

> ✅ Tutashughulikia kurudisha nyuma kwa undani zaidi katika mfano wetu wa daftari.

## Hitimisho

Katika somo hili, tumejenga maktaba yetu ya mtandao wa neva, na tumeitumia kwa kazi rahisi ya uainishaji wa vipimo viwili.

## 🚀 Changamoto

Katika daftari linaloambatana, utaweza kutekeleza mfumo wako wa kujenga na kufundisha perceptrons za tabaka nyingi. Utaweza kuona kwa undani jinsi mitandao ya neva ya kisasa inavyofanya kazi.

Endelea kwenye daftari la OwnFramework na lifanye kazi kupitia hilo.

## Mapitio & Kujisomea

Kurudisha nyuma ni algoriti ya kawaida inayotumika katika AI na ML, inayofaa kusomewa kwa undani zaidi.

## Kazi

Katika maabara hii, unatakiwa kutumia mfumo ulioujenga katika somo hili kutatua uainishaji wa nambari za mkono wa MNIST.

* Maelekezo
* Daftari

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya awali katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, tafsiri ya kibinadamu ya kitaalamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.