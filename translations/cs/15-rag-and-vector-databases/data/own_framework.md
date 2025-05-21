<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:25:58+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "cs"
}
-->
# Úvod do neuronových sítí. Vícevrstvý perceptron

V předchozí části jste se seznámili s nejjednodušším modelem neuronové sítě - jednovrstvým perceptronem, což je lineární model pro dvoutřídní klasifikaci.

V této části rozšíříme tento model na flexibilnější rámec, který nám umožní:

* provádět **vícetřídní klasifikaci** kromě dvoutřídní
* řešit **regresní problémy** kromě klasifikace
* oddělit třídy, které nejsou lineárně separovatelné

Vyvineme také vlastní modulární rámec v Pythonu, který nám umožní konstruovat různé architektury neuronových sítí.

## Formalizace strojového učení

Začněme formalizací problému strojového učení. Předpokládejme, že máme trénovací datovou sadu **X** s označeními **Y** a potřebujeme vytvořit model *f*, který bude dělat co nejpřesnější předpovědi. Kvalita předpovědí je měřena pomocí **ztrátové funkce** ℒ. Následující ztrátové funkce se často používají:

* Pro regresní problém, kdy potřebujeme předpovědět číslo, můžeme použít **absolutní chybu** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| nebo **kvadratickou chybu** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pro klasifikaci používáme **0-1 ztrátu** (což je v podstatě totéž jako **přesnost** modelu) nebo **logistickou ztrátu**.

Pro jednovrstvý perceptron byla funkce *f* definována jako lineární funkce *f(x)=wx+b* (zde *w* je matice vah, *x* je vektor vstupních znaků a *b* je vektor biasu). Pro různé architektury neuronových sítí může tato funkce nabýt složitější formy.

> V případě klasifikace je často žádoucí získat pravděpodobnosti odpovídajících tříd jako výstup sítě. K převodu libovolných čísel na pravděpodobnosti (např. k normalizaci výstupu) často používáme funkci **softmax** σ, a funkce *f* se stává *f(x)=σ(wx+b)*

Ve výše uvedené definici *f* se *w* a *b* nazývají **parametry** θ=⟨*w,b*⟩. Vzhledem k datové sadě ⟨**X**,**Y**⟩ můžeme vypočítat celkovou chybu na celé datové sadě jako funkci parametrů θ.

> ✅ **Cílem trénování neuronové sítě je minimalizovat chybu změnou parametrů θ**

## Optimalizace gradientního sestupu

Existuje známá metoda optimalizace funkcí nazvaná **gradientní sestup**. Myšlenka je, že můžeme vypočítat derivaci (v multidimenzionálním případě nazývanou **gradient**) ztrátové funkce vzhledem k parametrům a měnit parametry takovým způsobem, aby se chyba zmenšovala. To lze formalizovat následovně:

* Inicializujte parametry nějakými náhodnými hodnotami w<sup>(0)</sup>, b<sup>(0)</sup>
* Opakujte následující krok mnohokrát:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Během trénování se očekává, že optimalizační kroky budou vypočítány s ohledem na celou datovou sadu (pamatujte, že ztráta se počítá jako součet přes všechny trénovací vzorky). V reálném životě však bereme malé části datové sady nazývané **minibatch**, a počítáme gradienty na základě podmnožiny dat. Protože podmnožina je pokaždé vybírána náhodně, taková metoda se nazývá **stochastický gradientní sestup** (SGD).

## Vícevrstvé perceptrony a zpětná propagace

Jednovrstvá síť, jak jsme viděli výše, je schopná klasifikovat lineárně separovatelné třídy. Abychom vytvořili bohatší model, můžeme kombinovat několik vrstev sítě. Matematicky by to znamenalo, že funkce *f* by měla složitější formu a bude vypočítána v několika krocích:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Zde je α **nelineární aktivační funkce**, σ je softmax funkce a parametry θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>

Algoritmus gradientního sestupu by zůstal stejný, ale bylo by obtížnější vypočítat gradienty. Vzhledem k pravidlu řetězové diferenciace můžeme vypočítat derivace jako:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravidlo řetězové diferenciace se používá k výpočtu derivací ztrátové funkce vzhledem k parametrům.

Všimněte si, že levá část všech těchto výrazů je stejná, a tak můžeme efektivně vypočítat derivace začínající od ztrátové funkce a jít "zpět" skrze výpočetní graf. Takže metoda trénování vícevrstvého perceptronu se nazývá **zpětná propagace**, nebo 'backprop'.

> TODO: citace obrázku

> ✅ Zpětnou propagaci probereme mnohem podrobněji v našem příkladu v notebooku.

## Závěr

V této lekci jsme vytvořili vlastní knihovnu neuronových sítí a použili jsme ji pro jednoduchý dvourozměrný klasifikační úkol.

## 🚀 Výzva

V přiloženém notebooku implementujete vlastní rámec pro vytváření a trénování vícevrstvých perceptronů. Budete mít možnost vidět podrobně, jak moderní neuronové sítě fungují.

Pokračujte do notebooku OwnFramework a projděte si ho.

## Přehled & Samostudium

Zpětná propagace je běžný algoritmus používaný v AI a ML, stojí za to ji podrobněji prostudovat.

## Úkol

V této laboratoři jste požádáni, abyste použili rámec, který jste vytvořili v této lekci, k vyřešení klasifikace ručně psaných číslic MNIST.

* Pokyny
* Notebook

**Upozornění**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo chybné interpretace vyplývající z použití tohoto překladu.