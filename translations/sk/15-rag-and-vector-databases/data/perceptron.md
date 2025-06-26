<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:44:18+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "sk"
}
-->
# Úvod do neurónových sietí: Perceptron

Jedným z prvých pokusov o implementáciu niečoho podobného modernej neurónovej sieti urobil Frank Rosenblatt z Cornell Aeronautical Laboratory v roku 1957. Bola to hardvérová implementácia nazvaná "Mark-1", navrhnutá na rozpoznávanie primitívnych geometrických útvarov, ako sú trojuholníky, štvorce a kruhy.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrázky z Wikipédie

Vstupný obraz bol reprezentovaný maticou fotobuniek 20x20, takže neurónová sieť mala 400 vstupov a jeden binárny výstup. Jednoduchá sieť obsahovala jeden neurón, tiež nazývaný **jednotka logického prahu**. Váhy neurónovej siete pôsobili ako potenciometre, ktoré si vyžadovali manuálne nastavenie počas fázy učenia.

> ✅ Potenciometer je zariadenie, ktoré umožňuje používateľovi nastaviť odpor v obvode.

> The New York Times v tom čase písal o perceptrone: *embryo elektronického počítača, od ktorého [námorníctvo] očakáva, že bude schopné chodiť, rozprávať, vidieť, písať, reprodukovať sa a byť si vedomé svojej existencie.*

## Model perceptronu

Predpokladajme, že máme N vlastností v našom modeli, v takom prípade by vstupný vektor bol vektor veľkosti N. Perceptron je model **binárnej klasifikácie**, t.j. dokáže rozlišovať medzi dvoma triedami vstupných dát. Predpokladáme, že pre každý vstupný vektor x bude výstup nášho perceptronu buď +1 alebo -1, v závislosti od triedy. Výstup bude vypočítaný pomocou vzorca:

y(x) = f(w<sup>T</sup>x)

kde f je kroková aktivačná funkcia

## Tréning perceptronu

Na natrénovanie perceptronu potrebujeme nájsť vektor váh w, ktorý klasifikuje väčšinu hodnôt správne, t.j. vedie k najmenšej **chybe**. Táto chyba je definovaná pomocou **kritéria perceptronu** nasledovne:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kde:

* súčet je brán na tých tréningových dátových bodoch i, ktoré vedú k nesprávnej klasifikácii
* x<sub>i</sub> sú vstupné dáta a t<sub>i</sub> je buď -1 alebo +1 pre negatívne a pozitívne príklady podľa potreby.

Toto kritérium je považované za funkciu váh w, a potrebujeme ho minimalizovať. Často sa používa metóda nazývaná **gradientný zostup**, pri ktorej začíname s nejakými počiatočnými váhami w<sup>(0)</sup>, a potom v každom kroku aktualizujeme váhy podľa vzorca:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tu η je tzv. **rýchlosť učenia**, a ∇E(w) označuje **gradient** E. Po vypočítaní gradientu skončíme s

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

V tejto lekcii ste sa naučili o perceptrone, ktorý je modelom binárnej klasifikácie, a ako ho natrénovať pomocou vektora váh.

## 🚀 Výzva

Ak chcete skúsiť vytvoriť vlastný perceptron, vyskúšajte tento laboratórny úkol na Microsoft Learn, ktorý používa Azure ML designer.

## Prehľad a samostatné štúdium

Aby ste videli, ako môžeme použiť perceptron na riešenie jednoduchých problémov, ako aj problémov z reálneho života, a aby ste pokračovali v učení - choďte na zápisník Perceptron.

Tu je tiež zaujímavý článok o perceptronoch.

## Úloha

V tejto lekcii sme implementovali perceptron pre úlohu binárnej klasifikácie a použili sme ho na klasifikáciu medzi dvoma ručne písanými číslicami. V tomto laboratórnom úkole máte za úlohu vyriešiť problém klasifikácie číslic úplne, t.j. určiť, ktorá číslica najpravdepodobnejšie zodpovedá danému obrazu.

* Pokyny
* Zápisník

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.