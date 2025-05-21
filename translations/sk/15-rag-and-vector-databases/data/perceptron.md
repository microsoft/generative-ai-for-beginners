<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T06:43:14+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "sk"
}
-->
# Úvod do neurónových sietí: Perceptron

Jedným z prvých pokusov implementovať niečo podobné modernej neurónovej sieti uskutočnil Frank Rosenblatt z Cornell Aeronautical Laboratory v roku 1957. Išlo o hardvérovú implementáciu nazývanú "Mark-1", navrhnutú na rozpoznávanie primitívnych geometrických tvarov, ako sú trojuholníky, štvorce a kruhy.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrázky z Wikipédie

Vstupný obraz bol reprezentovaný mriežkou 20x20 fotobuniek, takže neurónová sieť mala 400 vstupov a jeden binárny výstup. Jednoduchá sieť obsahovala jeden neurón, tiež nazývaný **práh logická jednotka**. Váhy neurónovej siete fungovali ako potenciometre, ktoré bolo potrebné manuálne nastaviť počas fázy učenia.

> ✅ Potenciometer je zariadenie, ktoré umožňuje užívateľovi nastaviť odpor v obvode.

> The New York Times v tom čase napísal o perceptrone: *zárodok elektronického počítača, od ktorého [Námorníctvo] očakáva, že bude schopný chodiť, rozprávať, vidieť, písať, reprodukovať sa a byť si vedomý svojej existencie.*

## Model perceptronu

Predpokladajme, že v našom modeli máme N vlastností, v takom prípade by vstupný vektor bol vektorom veľkosti N. Perceptron je model **binárnej klasifikácie**, t.j. dokáže rozlišovať medzi dvoma triedami vstupných dát. Predpokladáme, že pre každý vstupný vektor x bude výstup nášho perceptronu buď +1 alebo -1, v závislosti od triedy. Výstup sa vypočíta pomocou vzorca:

y(x) = f(w<sup>T</sup>x)

kde f je aktivačná funkcia typu schod

## Tréning perceptronu

Aby sme perceptron vytrénovali, musíme nájsť vektor váh w, ktorý správne klasifikuje väčšinu hodnôt, t.j. výsledkom je najmenšia **chyba**. Táto chyba je definovaná **perceptronovým kritériom** nasledujúcim spôsobom:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kde:

* súčet sa berie na tých tréningových dátach i, ktoré vedú k nesprávnej klasifikácii
* x<sub>i</sub> je vstupný údaj a t<sub>i</sub> je buď -1 alebo +1 pre negatívne a pozitívne príklady zodpovedajúco.

Toto kritérium je považované za funkciu váh w, a musíme ho minimalizovať. Často sa používa metóda nazývaná **gradientný zostup**, pri ktorej začíname s nejakými počiatočnými váhami w<sup>(0)</sup>, a potom v každom kroku aktualizujeme váhy podľa vzorca:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tu η je tzv. **rýchlosť učenia** a ∇E(w) označuje **gradient** E. Po vypočítaní gradientu skončíme s

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmus v Pythone vyzerá takto:

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

## Záver

V tejto lekcii ste sa naučili o perceptrone, ktorý je modelom binárnej klasifikácie, a ako ho trénovať pomocou vektora váh.

## 🚀 Výzva

Ak si chcete vyskúšať vytvoriť vlastný perceptron, vyskúšajte tento laboratórny cvičenie na Microsoft Learn, ktoré používa Azure ML designer.

## Prehľad a samostatné štúdium

Ak chcete vidieť, ako môžeme použiť perceptron na riešenie jednoduchých aj reálnych problémov a pokračovať v učení, prejdite na poznámkový blok Perceptron.

Tu je tiež zaujímavý článok o perceptronoch.

## Zadanie

V tejto lekcii sme implementovali perceptron pre úlohu binárnej klasifikácie a použili sme ho na klasifikáciu medzi dvoma ručne písanými číslicami. V tomto laboratóriu máte za úlohu úplne vyriešiť problém klasifikácie číslic, t.j. určiť, ktorá číslica najpravdepodobnejšie zodpovedá danému obrázku.

* Inštrukcie
* Poznámkový blok

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.