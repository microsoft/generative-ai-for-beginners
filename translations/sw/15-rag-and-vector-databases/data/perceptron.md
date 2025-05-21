<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T06:42:20+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "sw"
}
-->
# Utangulizi wa Mitandao ya Neural: Perceptron

Moja ya majaribio ya kwanza ya kutekeleza kitu kinachofanana na mtandao wa neural wa kisasa ilifanywa na Frank Rosenblatt kutoka Maabara ya Anga ya Cornell mnamo 1957. Ilikuwa utekelezaji wa vifaa vilivyoitwa "Mark-1", iliyoundwa kutambua maumbo ya kijiometri ya msingi, kama vile pembe tatu, miraba na miduara.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Picha kutoka Wikipedia

Picha ya ingizo iliwakilishwa na safu ya seli za picha za 20x20, hivyo mtandao wa neural ulikuwa na ingizo 400 na pato moja la binary. Mtandao rahisi ulikuwa na neuroni moja, pia inayoitwa **kitengo cha mantiki ya kizingiti**. Uzito wa mtandao wa neural ulifanya kazi kama potentiometers ambazo zilihitaji kurekebishwa kwa mkono wakati wa awamu ya mafunzo.

> ✅ Potentiometer ni kifaa kinachomruhusu mtumiaji kurekebisha upinzani wa mzunguko.

> The New York Times iliandika kuhusu perceptron wakati huo: *kiinitete cha kompyuta ya kielektroniki ambayo [Navy] inatarajia itaweza kutembea, kuzungumza, kuona, kuandika, kujizalisha na kuwa na ufahamu wa kuwepo kwake.*

## Mfano wa Perceptron

Tuseme tuna vipengele N katika mfano wetu, ambapo vector ya ingizo itakuwa vector ya ukubwa N. Perceptron ni mfano wa **ugawaji wa binary**, yaani inaweza kutofautisha kati ya madarasa mawili ya data ya ingizo. Tutadhani kwamba kwa kila vector ya ingizo x, pato la perceptron yetu litakuwa aidha +1 au -1, kulingana na darasa. Pato litahesabiwa kwa kutumia fomula:

y(x) = f(w<sup>T</sup>x)

ambapo f ni kazi ya uanzishaji ya hatua

## Kufundisha Perceptron

Ili kufundisha perceptron tunahitaji kupata vector ya uzito w ambayo inagawa maadili mengi kwa usahihi, yaani inasababisha **kosa** dogo zaidi. Kosa hili linafafanuliwa na **kigezo cha perceptron** kwa namna ifuatayo:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ambapo:

* jumla inachukuliwa kwenye hizo data za mafunzo i ambazo zinasababisha ugawaji mbaya
* x<sub>i</sub> ni data ya ingizo, na t<sub>i</sub> ni aidha -1 au +1 kwa mifano hasi na chanya ipasavyo.

Kigezo hiki kinachukuliwa kama kazi ya uzito w, na tunahitaji kukipunguza. Mara nyingi, njia inayoitwa **gradient descent** hutumika, ambapo tunaanza na uzito fulani wa awali w<sup>(0)</sup>, na kisha katika kila hatua tunasasisha uzito kulingana na fomula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Hapa η inaitwa **kiwango cha mafunzo**, na ∇E(w) inaashiria **gradient** ya E. Baada ya kuhesabu gradient, tunapata

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algorithimu katika Python inaonekana kama hii:

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

## Hitimisho

Katika somo hili, umejifunza kuhusu perceptron, ambayo ni mfano wa ugawaji wa binary, na jinsi ya kuifundisha kwa kutumia vector ya uzito.

## 🚀 Changamoto

Kama ungependa kujaribu kujenga perceptron yako mwenyewe, jaribu maabara hii kwenye Microsoft Learn inayotumia mbuni wa Azure ML

## Mapitio & Kujisomea

Ili kuona jinsi tunavyoweza kutumia perceptron kutatua tatizo la mfano pamoja na matatizo ya maisha halisi, na kuendelea kujifunza - nenda kwenye daftari la Perceptron.

Hapa kuna makala ya kuvutia kuhusu perceptrons pia.

## Kazi ya Nyumbani

Katika somo hili, tumetekeleza perceptron kwa kazi ya ugawaji wa binary, na tumeitumia kugawa kati ya tarakimu mbili zilizoandikwa kwa mkono. Katika maabara hii, unaombwa kutatua tatizo la ugawaji wa tarakimu kabisa, yaani kubaini ni tarakimu gani ina uwezekano mkubwa wa kuendana na picha fulani.

* Maagizo
* Daftari

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa habari muhimu, tafsiri ya kibinadamu ya kitaalamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.