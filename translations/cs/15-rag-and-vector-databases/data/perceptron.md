<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T06:42:56+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "cs"
}
-->
# Úvod do neuronových sítí: Perceptron

Jedním z prvních pokusů o implementaci něčeho podobného moderní neuronové síti byl v roce 1957 Frank Rosenblatt z Cornell Aeronautical Laboratory. Byla to hardwarová implementace nazvaná "Mark-1", navržená k rozpoznávání primitivních geometrických tvarů, jako jsou trojúhelníky, čtverce a kruhy.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrázky z Wikipedie

Vstupní obraz byl reprezentován maticí fotobuněk o rozměru 20x20, takže neuronová síť měla 400 vstupů a jeden binární výstup. Jednoduchá síť obsahovala jeden neuron, také nazývaný **jednotka prahové logiky**. Váhy neuronové sítě fungovaly jako potenciometry, které vyžadovaly ruční nastavení během tréninkové fáze.

> ✅ Potenciometr je zařízení, které umožňuje uživateli nastavit odpor v obvodu.

> The New York Times tehdy o perceptronu napsal: *embryo elektronického počítače, který [námořnictvo] očekává, že bude schopen chodit, mluvit, vidět, psát, reprodukovat se a být si vědom své existence.*

## Model perceptronu

Předpokládejme, že máme v našem modelu N znaků, v takovém případě by vstupní vektor byl vektor o velikosti N. Perceptron je model pro **binární klasifikaci**, tj. dokáže rozlišovat mezi dvěma třídami vstupních dat. Předpokládáme, že pro každý vstupní vektor x by výstup našeho perceptronu byl buď +1, nebo -1, v závislosti na třídě. Výstup bude vypočítán pomocí vzorce:

y(x) = f(w<sup>T</sup>x)

kde f je kroková aktivační funkce

## Trénování perceptronu

Abychom perceptron natrénovali, potřebujeme najít vektor vah w, který správně klasifikuje většinu hodnot, tj. vede k nejmenší **chybě**. Tato chyba je definována **perceptronovým kritériem** následujícím způsobem:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kde:

* součet se bere přes ty tréninkové datové body i, které vedou k nesprávné klasifikaci
* x<sub>i</sub> je vstupní data a t<sub>i</sub> je buď -1 nebo +1 pro negativní a pozitivní příklady.

Toto kritérium je považováno za funkci vah w, a my jej potřebujeme minimalizovat. Často se používá metoda nazývaná **gradientní sestup**, při které začínáme s nějakými počátečními váhami w<sup>(0)</sup> a poté v každém kroku aktualizujeme váhy podle vzorce:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Zde η je tzv. **rychlost učení** a ∇E(w) označuje **gradient** E. Po výpočtu gradientu skončíme s

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

V této lekci jste se naučili o perceptronu, což je model pro binární klasifikaci, a jak ho trénovat pomocí vektoru vah.

## 🚀 Výzva

Pokud byste si chtěli zkusit vytvořit vlastní perceptron, zkuste tento lab na Microsoft Learn, který využívá Azure ML designer.

## Přehled a samostudium

Abyste viděli, jak můžeme použít perceptron k řešení hračkového problému i reálných problémů, a pokračovali v učení, podívejte se na notebook o perceptronu.

Zde je také zajímavý článek o perceptronech.

## Zadání

V této lekci jsme implementovali perceptron pro úlohu binární klasifikace a použili jsme ho k rozlišení mezi dvěma ručně psanými číslicemi. V tomto labu jste požádáni, abyste zcela vyřešili problém klasifikace číslic, tj. určete, která číslice nejpravděpodobněji odpovídá danému obrázku.

* Pokyny
* Notebook

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace je doporučen profesionální lidský překlad. Nejsme odpovědní za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.