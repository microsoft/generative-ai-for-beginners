<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:24:59+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sw"
}
-->
# Utangulizi wa Mitandao ya Neural. Multi-Layered Perceptron

Katika sehemu iliyopita, ulijifunza kuhusu mfano rahisi zaidi wa mtandao wa neural - perceptron ya tabaka moja, mfano wa uainishaji wa darasa mbili wa mstari.

Katika sehemu hii tutapanua mfano huu kuwa mfumo unaonyumbulika zaidi, ambao utaturuhusu:

* kufanya **uainishaji wa darasa nyingi** kwa kuongezea darasa mbili
* kutatua **matatizo ya regression** kwa kuongezea uainishaji
* kutenganisha madarasa ambayo hayajatenganishwa kwa mstari

Pia tutaendeleza mfumo wetu wa modular katika Python ambao utaturuhusu kujenga miundo tofauti ya mitandao ya neural.

## Urasmishaji wa Kujifunza kwa Mashine

Tuanzie na kurasmisha tatizo la Kujifunza kwa Mashine. Tuseme tuna seti ya mafunzo **X** yenye lebo **Y**, na tunahitaji kujenga mfano *f* ambao utatoa utabiri sahihi zaidi. Ubora wa utabiri hupimwa na **Kazi ya Hasara** ℒ. Kazi zifuatazo za hasara hutumiwa mara nyingi:

* Kwa tatizo la regression, wakati tunahitaji kutabiri namba, tunaweza kutumia **makosa ya moja kwa moja** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, au **makosa ya mraba** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Kwa uainishaji, tunatumia **hasara ya 0-1** (ambayo kimsingi ni sawa na **usahihi** wa mfano), au **hasara ya logistic**.

Kwa perceptron ya kiwango kimoja, kazi *f* ilifafanuliwa kama kazi ya mstari *f(x)=wx+b* (hapa *w* ni matrix ya uzito, *x* ni vector ya vipengele vya ingizo, na *b* ni vector ya upendeleo). Kwa miundo tofauti ya mitandao ya neural, kazi hii inaweza kuchukua muundo mgumu zaidi.

> Katika kesi ya uainishaji, mara nyingi inatamanika kupata uwezekano wa madarasa yanayolingana kama matokeo ya mtandao. Ili kubadilisha namba za kiholela kuwa uwezekano (mfano, kuhalalisha matokeo), mara nyingi tunatumia kazi ya **softmax** σ, na kazi *f* inakuwa *f(x)=σ(wx+b)*

Katika ufafanuzi wa *f* hapo juu, *w* na *b* huitwa **vigezo** θ=⟨*w,b*⟩. Kutokana na seti ya data ⟨**X**,**Y**⟩, tunaweza kuhesabu kosa la jumla kwenye seti yote ya data kama kazi ya vigezo θ.

> ✅ **Lengo la mafunzo ya mtandao wa neural ni kupunguza kosa kwa kubadilisha vigezo θ**

## Uboreshaji wa Gradient Descent

Kuna mbinu inayojulikana ya uboreshaji wa kazi inayoitwa **gradient descent**. Wazo ni kwamba tunaweza kuhesabu derivative (katika kesi ya pande nyingi huitwa **gradient**) ya kazi ya hasara kwa kuzingatia vigezo, na kubadilisha vigezo kwa njia ambayo kosa litapungua. Hii inaweza kurasmishwa kama ifuatavyo:

* Anzisha vigezo kwa baadhi ya thamani za kiholela w<sup>(0)</sup>, b<sup>(0)</sup>
* Rudia hatua ifuatayo mara nyingi:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Wakati wa mafunzo, hatua za uboreshaji zinatakiwa kuhesabiwa kwa kuzingatia seti nzima ya data (kumbuka kwamba hasara inahesabiwa kama jumla kupitia sampuli zote za mafunzo). Hata hivyo, katika maisha halisi tunachukua sehemu ndogo za seti ya data zinazoitwa **minibatches**, na kuhesabu gradients kulingana na subset ya data. Kwa sababu subset huchukuliwa kiholela kila wakati, njia hii huitwa **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons na Backpropagation

Mtandao wa tabaka moja, kama tulivyoona hapo juu, una uwezo wa kuainisha madarasa yaliyotenganishwa kwa mstari. Ili kujenga mfano tajiri zaidi, tunaweza kuchanganya tabaka kadhaa za mtandao. Kihisabati ingemaanisha kuwa kazi *f* ingekuwa na muundo mgumu zaidi, na itahesabiwa kwa hatua kadhaa:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Hapa, α ni **kazi ya uanzishaji isiyo ya mstari**, σ ni kazi ya softmax, na vigezo θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoriti ya gradient descent ingesalia kuwa ile ile, lakini itakuwa vigumu zaidi kuhesabu gradients. Kutokana na sheria ya differentiation ya mnyororo, tunaweza kuhesabu derivatives kama:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Sheria ya differentiation ya mnyororo inatumika kuhesabu derivatives ya kazi ya hasara kwa kuzingatia vigezo.

Kumbuka kwamba sehemu ya kushoto kabisa ya maelezo hayo yote ni sawa, na hivyo tunaweza kuhesabu derivatives kwa ufanisi kuanzia na kazi ya hasara na kwenda "nyuma" kupitia grafu ya kihesabu. Hivyo basi njia ya kufundisha perceptron yenye tabaka nyingi inaitwa **backpropagation**, au 'backprop'.

> TODO: image citation

> ✅ Tutachambua backprop kwa undani zaidi katika mfano wetu wa daftari.

## Hitimisho

Katika somo hili, tumejenga maktaba yetu ya mtandao wa neural, na tumeitumia kwa kazi rahisi ya uainishaji wa vipimo viwili.

## 🚀 Changamoto

Katika daftari linaloambatana, utatekeleza mfumo wako mwenyewe wa kujenga na kufundisha perceptrons zenye tabaka nyingi. Utaweza kuona kwa undani jinsi mitandao ya neural ya kisasa inavyofanya kazi.

Endelea kwenye daftari la OwnFramework na ulifanyie kazi.

## Mapitio & Kujisomea

Backpropagation ni algoriti ya kawaida inayotumiwa katika AI na ML, inafaa kusomwa kwa undani zaidi

## Kazi

Katika maabara hii, unaombwa kutumia mfumo uliojengwa katika somo hili kutatua uainishaji wa tarakimu za maandishi ya mkono wa MNIST.

* Maagizo
* Daftari

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kibinadamu ya kitaalamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.