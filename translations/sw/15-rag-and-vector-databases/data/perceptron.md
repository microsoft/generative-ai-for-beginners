<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T17:00:13+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "sw"
}
-->
# Utangulizi wa Mitandao ya Neva: Perceptron

Moja ya jaribio la kwanza la kutekeleza kitu kinachofanana na mtandao wa neva wa kisasa lilifanywa na Frank Rosenblatt kutoka Cornell Aeronautical Laboratory mwaka 1957. Ilikuwa utekelezaji wa vifaa ulioitwa "Mark-1", ulioundwa kutambua takwimu za kijiometri za awali, kama vile mviringo, mraba na mviringo.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Picha kutoka Wikipedia

Picha ya ingizo iliwakilishwa na safu ya photocell 20x20, hivyo mtandao wa neva ulikuwa na ingizo 400 na toleo moja la binary. Mtandao rahisi ulikuwa na neva moja, pia uitwao **kitengo cha mantiki cha kikomo**. Uzito wa mtandao wa neva ulifanya kazi kama potentiometers ambazo zilihitaji kurekebishwa kwa mkono wakati wa awamu ya mafunzo.

> ✅ Potentiometer ni kifaa kinachomruhusu mtumiaji kurekebisha upinzani wa mzunguko.

> The New York Times ilichapisha kuhusu perceptron wakati huo: *mbegu ya kompyuta ya elektroniki ambayo [Navy] inatarajia itakuwa na uwezo wa kutembea, kuzungumza, kuona, kuandika, kujizalisha na kuwa na ufahamu wa kuwepo kwake.*

## Mfano wa Perceptron

Tuseme tuna sifa N katika mfano wetu, ambapo vector ya ingizo itakuwa vector ya ukubwa N. Perceptron ni mfano wa **ugawaji wa binary**, yaani inaweza kutofautisha kati ya makundi mawili ya data za ingizo. Tutadhani kwamba kwa kila vector ya ingizo x, toleo la perceptron yetu litakuwa +1 au -1, kulingana na kundi. Toleo litahesabiwa kwa kutumia fomula:

y(x) = f(w<sup>T</sup>x)

ambapo f ni kazi ya uanzishaji wa hatua

## Mafunzo ya Perceptron

Ili kufundisha perceptron tunahitaji kupata vector ya uzito w inayogawanya kwa usahihi zaidi ya thamani, yaani kusababisha **kosa** ndogo zaidi. Kosa hili linafafanuliwa na **kigezo cha perceptron** kwa njia ifuatayo:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ambapo:

* jumla inachukuliwa kwa data za mafunzo i ambazo husababisha ugawaji mbaya
* x<sub>i</sub> ni data ya ingizo, na t<sub>i</sub> ni -1 au +1 kwa mifano hasi na chanya mtawalia.

Kigezo hiki kinachukuliwa kama kazi ya uzito w, na tunahitaji kukipunguza. Mara nyingi, njia inayoitwa **kupungua kwa mwelekeo wa mwinuko** hutumika, ambapo tunaanza na uzito fulani wa awali w<sup>(0)</sup>, kisha kila hatua tunasasisha uzito kulingana na fomula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Hapa η ni kinachoitwa **kasi ya kujifunza**, na ∇E(w) inaonyesha **mwelekeo wa mwinuko** wa E. Baada ya kuhesabu mwelekeo wa mwinuko, tunapata

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoriti katika Python inaonekana kama ifuatavyo:

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

Ikiwa ungependa kujaribu kujenga perceptron yako mwenyewe, jaribu maabara hii kwenye Microsoft Learn inayotumia Azure ML designer

## Mapitio & Kujifunza Binafsi

Ili kuona jinsi tunavyoweza kutumia perceptron kutatua tatizo la mfano pamoja na matatizo halisi ya maisha, na kuendelea kujifunza - nenda kwenye daftari la Perceptron.

Hapa kuna makala ya kuvutia kuhusu perceptrons pia.

## Kazi ya Nyumbani

Katika somo hili, tumeunda perceptron kwa kazi ya ugawaji wa binary, na tumetumia kuainisha kati ya nambari mbili zilizoandikwa kwa mkono. Katika maabara hii, unahitajika kutatua tatizo la ugawaji wa nambari kikamilifu, yaani kubaini ni nambari gani ina uwezekano mkubwa zaidi kuendana na picha fulani.

* Maelekezo
* Daftari

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.