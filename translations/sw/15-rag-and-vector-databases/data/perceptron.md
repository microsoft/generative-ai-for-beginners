<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:43:21+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "sw"
}
-->
# Utangulizi wa Mitandao ya Neural: Perceptron

Moja ya majaribio ya kwanza ya kutekeleza kitu kinachofanana na mtandao wa neural wa kisasa ilifanywa na Frank Rosenblatt kutoka Cornell Aeronautical Laboratory mwaka 1957. Ilikuwa ni utekelezaji wa vifaa vilivyoitwa "Mark-1", iliyoundwa kutambua maumbo ya kijiometri ya kimsingi, kama vile pembe tatu, miraba na miduara.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Picha kutoka Wikipedia

Picha ya ingizo iliwakilishwa na safu ya seli za picha 20x20, hivyo mtandao wa neural ulikuwa na viingilio 400 na pato moja la binary. Mtandao rahisi ulikuwa na neuroni moja, pia inayoitwa **kikomo cha mantiki**. Uzito wa mtandao wa neural ulifanya kazi kama potentiometers ambazo zilihitaji marekebisho ya mwongozo wakati wa awamu ya mafunzo.

> ✅ Potentiometer ni kifaa kinachomruhusu mtumiaji kurekebisha upinzani wa mzunguko.

> The New York Times iliandika kuhusu perceptron wakati huo: *kiinitete cha kompyuta ya kielektroniki ambayo [Jeshi la Majini] linatarajia itaweza kutembea, kuzungumza, kuona, kuandika, kujizalisha na kuwa na ufahamu wa uwepo wake.*

## Mfano wa Perceptron

Tuseme tuna vipengele N katika mfano wetu, ambapo vector ya ingizo itakuwa vector ya ukubwa N. Perceptron ni mfano wa **uainishaji wa binary**, yaani inaweza kutofautisha kati ya madarasa mawili ya data ya ingizo. Tutadhani kwamba kwa kila vector ya ingizo x, pato la perceptron yetu litakuwa ama +1 au -1, kutegemea darasa. Pato litahesabiwa kwa kutumia fomula:

y(x) = f(w<sup>T</sup>x)

ambapo f ni kazi ya uanzishaji ya hatua

## Mafunzo ya Perceptron

Ili kufundisha perceptron tunahitaji kupata vector ya uzito w ambayo inatofautisha thamani nyingi kwa usahihi, yaani inasababisha **kosa** dogo zaidi. Kosa hili linafafanuliwa na **kigezo cha perceptron** kwa njia ifuatayo:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ambapo:

* jumla inachukuliwa kwa zile data za mafunzo i ambazo zinasababisha uainishaji usio sahihi
* x<sub>i</sub> ni data ya ingizo, na t<sub>i</sub> ni ama -1 au +1 kwa mifano hasi na chanya ipasavyo.

Kigezo hiki kinachukuliwa kama kazi ya uzito w, na tunahitaji kuipunguza. Mara nyingi, njia inayoitwa **mteremko wa gradient** hutumika, ambapo tunaanza na uzito wa awali w<sup>(0)</sup>, na kisha katika kila hatua husasisha uzito kulingana na fomula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Hapa η inaitwa **kiwango cha mafunzo**, na ∇E(w) inaonyesha **gradient** ya E. Baada ya kuhesabu gradient, tunapata

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algorithm katika Python inaonekana kama hii:

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

Katika somo hili, umejifunza kuhusu perceptron, ambayo ni mfano wa uainishaji wa binary, na jinsi ya kuifundisha kwa kutumia vector ya uzito.

## 🚀 Changamoto

Kama ungependa kujaribu kujenga perceptron yako mwenyewe, jaribu maabara hii kwenye Microsoft Learn inayotumia Azure ML designer

## Mapitio & Kujisomea

Ili kuona jinsi tunavyoweza kutumia perceptron kutatua tatizo la mfano na pia matatizo halisi, na kuendelea kujifunza - nenda kwenye daftari la Perceptron.

Hapa kuna makala ya kuvutia kuhusu perceptrons pia.

## Kazi

Katika somo hili, tumetekeleza perceptron kwa kazi ya uainishaji wa binary, na tumetumia kuainisha kati ya tarakimu mbili zilizoandikwa kwa mkono. Katika maabara hii, unatakiwa kutatua tatizo la uainishaji wa tarakimu kabisa, yaani kuamua ni tarakimu gani ina uwezekano mkubwa wa kuendana na picha fulani.

* Maelekezo
* Daftari

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya kiasili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kibinadamu ya kitaalamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.