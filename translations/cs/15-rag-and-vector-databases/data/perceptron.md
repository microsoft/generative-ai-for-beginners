<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:44:01+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "cs"
}
-->
# Úvod do neuronových sítí: Perceptron

Jedním z prvních pokusů o implementaci něčeho podobného moderní neuronové síti byl proveden Frankem Rosenblattem z Cornell Aeronautical Laboratory v roce 1957. Byla to hardwarová implementace nazvaná "Mark-1", navržená k rozpoznávání primitivních geometrických tvarů, jako jsou trojúhelníky, čtverce a kruhy.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrázky z Wikipedie

Vstupní obraz byl reprezentován maticí 20x20 fotobuněk, takže neuronová síť měla 400 vstupů a jeden binární výstup. Jednoduchá síť obsahovala jeden neuron, nazývaný také **prahová logická jednotka**. Váhy neuronové sítě fungovaly jako potenciometry, které bylo třeba ručně nastavovat během fáze tréninku.

> ✅ Potenciometr je zařízení, které uživateli umožňuje nastavit odpor obvodu.

> The New York Times tehdy o perceptronu napsal: *embryo elektronického počítače, od kterého [námořnictvo] očekává, že bude umět chodit, mluvit, vidět, psát, reprodukovat se a být si vědomo své existence.*

## Model perceptronu

Předpokládejme, že máme N vlastností v našem modelu, v takovém případě by vstupní vektor byl vektor o velikosti N. Perceptron je model pro **binární klasifikaci**, tzn. dokáže rozlišit mezi dvěma třídami vstupních dat. Budeme předpokládat, že pro každý vstupní vektor x bude výstup našeho perceptronu buď +1, nebo -1, v závislosti na třídě. Výstup bude vypočítán pomocí vzorce:

y(x) = f(w<sup>T</sup>x)

kde f je aktivační funkce kroku

## Trénink perceptronu

Pro trénink perceptronu potřebujeme najít vektor vah w, který klasifikuje většinu hodnot správně, tj. vede k nejmenší **chybě**. Tato chyba je definována **kritériem perceptronu** následujícím způsobem:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kde:

* součet je prováděn na těch tréninkových datech i, které vedou k nesprávné klasifikaci
* x<sub>i</sub> jsou vstupní data a t<sub>i</sub> je buď -1 nebo +1 pro negativní a pozitivní příklady odpovídajícím způsobem.

Toto kritérium je považováno za funkci vah w a je potřeba jej minimalizovat. Často se používá metoda nazývaná **gradientní sestup**, při které začínáme s nějakými počátečními vahami w<sup>(0)</sup>, a pak v každém kroku aktualizujeme váhy podle vzorce:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Zde η je takzvaná **rychlost učení** a ∇E(w) označuje **gradient** E. Po výpočtu gradientu dostaneme

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmus v Pythonu vypadá takto:

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

## Závěr

V této lekci jste se dozvěděli o perceptronu, což je model pro binární klasifikaci, a jak jej trénovat pomocí vektoru vah.

## 🚀 Výzva

Pokud byste si chtěli zkusit vytvořit vlastní perceptron, zkuste tento lab na Microsoft Learn, který využívá Azure ML designer.

## Recenze a samostudium

Chcete-li vidět, jak můžeme použít perceptron k řešení jednoduchého problému i reálných problémů, a pokračovat v učení - přejděte do poznámkového bloku Perceptron.

Zde je také zajímavý článek o perceptronech.

## Úkol

V této lekci jsme implementovali perceptron pro úkol binární klasifikace a použili jsme jej k rozlišení mezi dvěma ručně psanými číslicemi. V tomto labu jste požádáni, abyste vyřešili problém klasifikace číslic kompletně, tj. určete, která číslice s největší pravděpodobností odpovídá danému obrázku.

* Pokyny
* Poznámkový blok

**Upozornění**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace je doporučen profesionální lidský překlad. Nejsme zodpovědní za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.