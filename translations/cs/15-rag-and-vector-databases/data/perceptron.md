<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T17:00:39+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "cs"
}
-->
# Úvod do neuronových sítí: Perceptron

Jedním z prvních pokusů o implementaci něčeho podobného moderní neuronové síti byl Frank Rosenblatt z Cornell Aeronautical Laboratory v roce 1957. Šlo o hardwarovou implementaci nazvanou „Mark-1“, navrženou k rozpoznávání primitivních geometrických tvarů, jako jsou trojúhelníky, čtverce a kruhy.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrázky z Wikipedie

Vstupní obraz byl reprezentován maticí 20x20 fotobuněk, takže neuronová síť měla 400 vstupů a jeden binární výstup. Jednoduchá síť obsahovala jeden neuron, nazývaný také **prahová logická jednotka**. Váhy neuronové sítě fungovaly jako potenciometry, které bylo potřeba ručně nastavovat během tréninkové fáze.

> ✅ Potenciometr je zařízení, které umožňuje uživateli upravit odpor v obvodu.

> The New York Times tehdy o perceptronu napsal: *embryo elektronického počítače, o kterém [Námořnictvo] očekává, že bude schopen chodit, mluvit, vidět, psát, reprodukovat se a být si vědom své existence.*

## Model perceptronu

Předpokládejme, že máme v našem modelu N rysů, v takovém případě by vstupní vektor měl velikost N. Perceptron je model **binární klasifikace**, tedy dokáže rozlišit mezi dvěma třídami vstupních dat. Předpokládáme, že pro každý vstupní vektor x bude výstup našeho perceptronu buď +1, nebo -1, v závislosti na třídě. Výstup se vypočítá podle vzorce:

y(x) = f(w<sup>T</sup>x)

kde f je kroková aktivační funkce

## Trénink perceptronu

K tréninku perceptronu potřebujeme najít vektor vah w, který správně klasifikuje většinu hodnot, tedy vede k co nejmenší **chybě**. Tato chyba je definována pomocí **perceptronového kritéria** následovně:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kde:

* součet je počítán přes ty tréninkové body i, které vedou k nesprávné klasifikaci
* x<sub>i</sub> jsou vstupní data a t<sub>i</sub> je buď -1 nebo +1 pro záporné a kladné příklady

Toto kritérium je považováno za funkci vah w, kterou je potřeba minimalizovat. Často se používá metoda zvaná **gradientní sestup**, při které začínáme s nějakými počátečními váhami w<sup>(0)</sup> a pak v každém kroku aktualizujeme váhy podle vzorce:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Zde η je tzv. **učící rychlost** a ∇E(w) označuje **gradient** funkce E. Po výpočtu gradientu dostaneme

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

V této lekci jste se naučili, co je perceptron, což je model binární klasifikace, a jak ho trénovat pomocí vektorů vah.

## 🚀 Výzva

Pokud si chcete vyzkoušet vytvořit vlastní perceptron, zkuste tento lab na Microsoft Learn, který využívá Azure ML designer.

## Přehled a samostudium

Chcete-li vidět, jak lze perceptron použít k řešení jednoduchých i reálných problémů a pokračovat ve studiu, přejděte do notebooku Perceptron.

Tady je také zajímavý článek o perceptronech.

## Zadání

V této lekci jsme implementovali perceptron pro úlohu binární klasifikace a použili ho k rozlišení dvou ručně psaných číslic. V tomto labu máte za úkol vyřešit problém klasifikace číslic kompletně, tedy určit, která číslice nejpravděpodobněji odpovídá danému obrázku.

* Instrukce
* Notebook

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.