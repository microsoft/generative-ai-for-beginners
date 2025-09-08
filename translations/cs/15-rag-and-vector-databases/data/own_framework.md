<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:50:34+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "cs"
}
-->
# Úvod do neuronových sítí. Vícevrstvý perceptron

V předchozí části jste se seznámili s nejjednodušším modelem neuronové sítě – jednovrstvým perceptronem, což je lineární model pro dvoutřídní klasifikaci.

V této části tento model rozšíříme do flexibilnějšího rámce, který nám umožní:

* provádět **vícetřídní klasifikaci** kromě dvoutřídní
* řešit **regresní úlohy** kromě klasifikace
* oddělit třídy, které nejsou lineárně separabilní

Také si vytvoříme vlastní modulární rámec v Pythonu, který nám umožní sestavovat různé architektury neuronových sítí.

## Formalizace strojového učení

Začněme formalizací problému strojového učení. Předpokládejme, že máme trénovací datovou sadu **X** s popisky **Y** a potřebujeme vytvořit model *f*, který bude dělat co nejpřesnější predikce. Kvalita predikcí se měří pomocí **ztrátové funkce** ℒ. Často používané ztrátové funkce jsou:

* Pro regresní úlohu, kdy potřebujeme předpovědět číslo, můžeme použít **absolutní chybu** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, nebo **čtvercovou chybu** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pro klasifikaci používáme **0-1 ztrátu** (což je v podstatě totéž jako **přesnost** modelu), nebo **logistickou ztrátu**.

U jednovrstvého perceptronu byla funkce *f* definována jako lineární funkce *f(x)=wx+b* (kde *w* je matice vah, *x* je vektor vstupních rysů a *b* je vektor biasů). U různých architektur neuronových sítí může mít tato funkce složitější podobu.

> V případě klasifikace je často žádoucí získat jako výstup sítě pravděpodobnosti příslušných tříd. Pro převedení libovolných čísel na pravděpodobnosti (např. normalizaci výstupu) často používáme **softmax** funkci σ, a funkce *f* se pak stává *f(x)=σ(wx+b)*

Ve výše uvedené definici *f* jsou *w* a *b* nazývány **parametry** θ=⟨*w,b*⟩. Pro danou datovou sadu ⟨**X**,**Y**⟩ můžeme spočítat celkovou chybu na celé sadě jako funkci parametrů θ.

> ✅ **Cílem tréninku neuronové sítě je minimalizovat chybu změnou parametrů θ**

## Optimalizace pomocí gradientního sestupu

Existuje známá metoda optimalizace funkcí nazývaná **gradientní sestup**. Myšlenka je taková, že můžeme spočítat derivaci (v případě více rozměrů nazývanou **gradient**) ztrátové funkce vzhledem k parametrům a měnit parametry tak, aby se chyba snižovala. Formálně to lze vyjádřit takto:

* Inicializujeme parametry náhodnými hodnotami w<sup>(0)</sup>, b<sup>(0)</sup>
* Opakujeme následující krok mnohokrát:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Během tréninku by se optimalizační kroky měly počítat s ohledem na celou datovou sadu (pamatujte, že ztráta se počítá jako součet přes všechny trénovací vzorky). V praxi však bereme malé části dat nazývané **minibatches** a počítáme gradienty na základě podmnožiny dat. Protože podmnožina je pokaždé náhodná, tato metoda se nazývá **stochastický gradientní sestup** (SGD).

## Vícevrstvý perceptron a zpětná propagace

Jednovrstvá síť, jak jsme viděli výše, dokáže klasifikovat lineárně separabilní třídy. Pro vytvoření bohatšího modelu můžeme zkombinovat několik vrstev sítě. Matematicky to znamená, že funkce *f* bude mít složitější podobu a bude se počítat ve více krocích:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Zde je α **nelineární aktivační funkce**, σ je softmax funkce a parametry θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritmus gradientního sestupu zůstává stejný, ale výpočet gradientů je složitější. Díky pravidlu řetězce pro derivace můžeme spočítat derivace takto:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravidlo řetězce se používá k výpočtu derivací ztrátové funkce vzhledem k parametrům.

Všimněte si, že levá část všech těchto výrazů je stejná, a proto můžeme efektivně počítat derivace začínající od ztrátové funkce a postupovat „zpětně“ přes výpočetní graf. Tato metoda tréninku vícevrstvého perceptronu se nazývá **zpětná propagace** (backpropagation), nebo zkráceně 'backprop'.



> TODO: citace obrázku

> ✅ Zpětnou propagaci podrobněji probereme v našem příkladu v notebooku.  

## Závěr

V této lekci jsme si vytvořili vlastní knihovnu pro neuronové sítě a použili ji pro jednoduchý dvourozměrný klasifikační úkol.

## 🚀 Výzva

V přiloženém notebooku si implementujete vlastní rámec pro tvorbu a trénink vícevrstvých perceptronů. Podrobně uvidíte, jak moderní neuronové sítě fungují.

Přejděte do notebooku OwnFramework a projděte si ho.

## Přehled a samostudium

Zpětná propagace je běžný algoritmus používaný v AI a ML, stojí za to se mu věnovat podrobněji.

## Zadání

V tomto cvičení máte za úkol použít rámec, který jste si vytvořili v této lekci, k řešení klasifikace ručně psaných číslic MNIST.

* Instrukce
* Notebook

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.