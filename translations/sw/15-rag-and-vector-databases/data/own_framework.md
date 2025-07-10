<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:49:58+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sw"
}
-->
# Utangulizi wa Mitandao ya Neva. Multi-Layered Perceptron

Katika sehemu iliyopita, ulijifunza kuhusu mfano rahisi wa mtandao wa neva - perceptron yenye tabaka moja, mfano wa uainishaji wa darasa mbili wa mstari.

Katika sehemu hii tutaongeza mfano huu kuwa mfumo wenye ufanisi zaidi, utatuwezesha:

* kufanya **uainishaji wa madarasa mengi** zaidi ya madarasa mawili
* kutatua **matatizo ya regression** zaidi ya uainishaji
* kutenganisha madarasa ambayo hayawezi kutenganishwa kwa mstari moja

Pia tutaendeleza mfumo wetu wa moduli kwa Python ambao utatuwezesha kujenga miundo tofauti ya mitandao ya neva.

## Ufafanuzi wa Machine Learning

Tuanze kwa kufafanua tatizo la Machine Learning. Tuseme tuna seti ya mafunzo **X** yenye lebo **Y**, na tunahitaji kujenga mfano *f* ambao utatoa utabiri sahihi zaidi. Ubora wa utabiri hupimwa kwa **kazi ya hasara** ℒ. Kazi zifuatazo za hasara hutumika mara kwa mara:

* Kwa tatizo la regression, tunapohitaji kutabiri nambari, tunaweza kutumia **makosa ya moja kwa moja** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, au **makosa ya mraba** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Kwa uainishaji, tunatumia **hasara ya 0-1** (ambayo ni sawa na **usahihi** wa mfano), au **hasara ya logistic**.

Kwa perceptron ya tabaka moja, kazi *f* ilifafanuliwa kama kazi ya mstari *f(x)=wx+b* (hapa *w* ni matriki ya uzito, *x* ni vekta ya sifa za ingizo, na *b* ni vekta ya upendeleo). Kwa miundo tofauti ya mitandao ya neva, kazi hii inaweza kuwa na muundo mgumu zaidi.

> Katika kesi ya uainishaji, mara nyingi tunapendelea kupata uwezekano wa madarasa husika kama matokeo ya mtandao. Ili kubadilisha nambari yoyote kuwa uwezekano (mfano. kusawazisha matokeo), mara nyingi tunatumia kazi ya **softmax** σ, na kazi *f* inakuwa *f(x)=σ(wx+b)*

Katika ufafanuzi wa *f* hapo juu, *w* na *b* huitwa **vigezo** θ=⟨*w,b*⟩. Tukichukua seti ya data ⟨**X**,**Y**⟩, tunaweza kuhesabu makosa ya jumla kwenye seti nzima kama kazi ya vigezo θ.

> ✅ **Lengo la mafunzo ya mtandao wa neva ni kupunguza makosa kwa kubadilisha vigezo θ**

## Uboreshaji kwa Gradient Descent

Kuna njia maarufu ya kuboresha kazi inayoitwa **gradient descent**. Wazo ni kwamba tunaweza kuhesabu mtoaji (katika kesi ya vipimo vingi huitwa **gradient**) wa kazi ya hasara kuhusiana na vigezo, na kubadilisha vigezo kwa njia ambayo makosa yanapungua. Hii inaweza kufafanuliwa kama ifuatavyo:

* Anzisha vigezo kwa baadhi ya thamani za nasibu w<sup>(0)</sup>, b<sup>(0)</sup>
* Rudia hatua ifuatayo mara nyingi:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Wakati wa mafunzo, hatua za uboreshaji zinapaswa kuhesabiwa kwa kuzingatia seti nzima ya data (kumbuka kuwa hasara huhesabiwa kama jumla ya sampuli zote za mafunzo). Hata hivyo, katika maisha halisi tunachukua sehemu ndogo za seti ya data zinazoitwa **minibatches**, na kuhesabu gradients kwa msingi wa sehemu ndogo ya data. Kwa sababu sehemu ndogo huchaguliwa nasibu kila mara, njia hii huitwa **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons na Backpropagation

Mtandao wa tabaka moja, kama tulivyoona hapo juu, unaweza kuainisha madarasa yanayotenganishwa kwa mstari. Ili kujenga mfano tajiri zaidi, tunaweza kuunganisha tabaka kadhaa za mtandao. Kimaandishi hii itamaanisha kuwa kazi *f* itakuwa na muundo mgumu zaidi, na itahesabiwa kwa hatua kadhaa:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Hapa, α ni **kazi ya uanzishaji isiyo ya mstari**, σ ni kazi ya softmax, na vigezo θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoriti ya gradient descent itabaki ile ile, lakini itakuwa vigumu zaidi kuhesabu gradients. Kwa kutumia kanuni ya mnyororo wa utofauti, tunaweza kuhesabu mtoaji kama ifuatavyo:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kanuni ya mnyororo wa utofauti hutumika kuhesabu mtoaji wa kazi ya hasara kuhusiana na vigezo.

Kumbuka kuwa sehemu ya kushoto kabisa ya maelezo haya ni sawa, hivyo tunaweza kuhesabu mtoaji kwa ufanisi kuanzia kazi ya hasara na kurudi "nyuma" kupitia grafu ya hesabu. Hivyo njia ya kufundisha multi-layered perceptron huitwa **backpropagation**, au 'backprop'.

> TODO: image citation

> ✅ Tutashughulikia backprop kwa undani zaidi katika mfano wetu wa daftari.

## Hitimisho

Katika somo hili, tumejenga maktaba yetu ya mtandao wa neva, na tumeitumia kwa kazi rahisi ya uainishaji wa vipimo viwili.

## 🚀 Changamoto

Katika daftari linalohusiana, utaanzisha mfumo wako wa kujenga na kufundisha multi-layered perceptrons. Utaweza kuona kwa undani jinsi mitandao ya neva ya kisasa inavyofanya kazi.

Endelea kwenye daftari la OwnFramework na ufanye kazi kupitia.

## Mapitio & Kujisomea

Backpropagation ni algoriti inayotumika sana katika AI na ML, inafaa kusomewa kwa undani zaidi

## Kazi ya Nyumbani

Katika maabara hii, unahitajika kutumia mfumo uliouunda katika somo hili kutatua tatizo la uainishaji wa nambari za maandishi za MNIST.

* Maelekezo
* Daftari

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.