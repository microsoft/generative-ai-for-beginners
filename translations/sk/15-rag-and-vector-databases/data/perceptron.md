<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T17:00:50+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "sk"
}
-->
# Úvod do neurónových sietí: Perceptrón

Jedným z prvých pokusov o implementáciu niečoho podobného modernej neurónovej sieti urobil Frank Rosenblatt z Cornell Aeronautical Laboratory v roku 1957. Išlo o hardvérovú implementáciu nazvanú "Mark-1", navrhnutú na rozpoznávanie primitívnych geometrických tvarov, ako sú trojuholníky, štvorce a kruhy.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrázky z Wikipédie

Vstupný obraz bol reprezentovaný maticou 20x20 fotobuniek, takže neurónová sieť mala 400 vstupov a jeden binárny výstup. Jednoduchá sieť obsahovala jeden neurón, nazývaný aj **prahová logická jednotka**. Váhy neurónovej siete fungovali ako potenciometre, ktoré bolo potrebné manuálne nastavovať počas tréningovej fázy.

> ✅ Potenciometer je zariadenie, ktoré umožňuje používateľovi nastaviť odpor v obvode.

> The New York Times v tom čase o perceptróne napísal: *embryo elektronického počítača, ktorý [Námorníctvo] očakáva, že bude schopný chodiť, rozprávať, vidieť, písať, rozmnožovať sa a byť si vedomý svojej existencie.*

## Model perceptrónu

Predpokladajme, že v našom modeli máme N vlastností, v takom prípade by vstupný vektor mal veľkosť N. Perceptrón je model **binárnej klasifikácie**, teda dokáže rozlíšiť medzi dvoma triedami vstupných dát. Predpokladáme, že pre každý vstupný vektor x bude výstup nášho perceptrónu buď +1 alebo -1, v závislosti od triedy. Výstup sa vypočíta podľa vzorca:

y(x) = f(w<sup>T</sup>x)

kde f je prahová aktivačná funkcia

## Tréning perceptrónu

Na natrénovanie perceptrónu potrebujeme nájsť vektor váh w, ktorý správne klasifikuje väčšinu hodnôt, teda vedie k najmenšej **chybe**. Táto chyba je definovaná pomocou **perceptrónového kritéria** nasledovne:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kde:

* súčet sa berie cez tie trénovacie dáta i, ktoré vedú k nesprávnej klasifikácii
* x<sub>i</sub> sú vstupné dáta a t<sub>i</sub> je buď -1 alebo +1 pre negatívne a pozitívne príklady

Toto kritérium sa považuje za funkciu váh w, ktorú potrebujeme minimalizovať. Často sa používa metóda nazývaná **gradientný zostup**, pri ktorej začíname s nejakými počiatočnými váhami w<sup>(0)</sup> a potom v každom kroku aktualizujeme váhy podľa vzorca:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Kde η je tzv. **rýchlosť učenia** a ∇E(w) označuje **gradient** funkcie E. Po výpočte gradientu dostaneme

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

V tejto lekcii ste sa naučili o perceptróne, ktorý je modelom binárnej klasifikácie, a ako ho natrénovať pomocou vektora váh.

## 🚀 Výzva

Ak by ste si chceli vyskúšať vytvoriť vlastný perceptrón, vyskúšajte tento lab na Microsoft Learn, ktorý používa Azure ML designer.

## Prehľad a samostatné štúdium

Ak chcete vidieť, ako môžeme použiť perceptrón na riešenie jednoduchých aj reálnych problémov a pokračovať v učení, prejdite na Perceptron notebook.

Tu je tiež zaujímavý článok o perceptrónoch.

## Zadanie

V tejto lekcii sme implementovali perceptrón pre úlohu binárnej klasifikácie a použili sme ho na rozlíšenie medzi dvoma ručne písanými číslicami. V tomto labe máte za úlohu vyriešiť problém klasifikácie číslic úplne, teda určiť, ktorá číslica najpravdepodobnejšie zodpovedá danému obrázku.

* Inštrukcie
* Notebook

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.