<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:29:49+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "cs"
}
-->
# Úvod do neuronových sítí. Vícevrstvý perceptron

V předchozí části jste se seznámili s nejjednodušším modelem neuronové sítě - jednovrstvým perceptronem, lineárním modelem pro dvoutřídní klasifikaci.

V této části rozšíříme tento model na flexibilnější rámec, který nám umožní:

* provádět **vícetřídní klasifikaci** vedle dvoutřídní
* řešit **regresní problémy** vedle klasifikace
* oddělovat třídy, které nejsou lineárně oddělitelné

Také vyvineme vlastní modulární rámec v Pythonu, který nám umožní konstruovat různé architektury neuronových sítí.

## Formalizace strojového učení

Začněme formalizací problému strojového učení. Předpokládejme, že máme trénovací dataset **X** s označeními **Y**, a potřebujeme vytvořit model *f*, který bude dělat co nejpřesnější předpovědi. Kvalita předpovědí se měří pomocí **ztrátové funkce** ℒ. Často se používají následující ztrátové funkce:

* Pro regresní problém, kdy potřebujeme předpovědět číslo, můžeme použít **absolutní chybu** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, nebo **kvadratickou chybu** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pro klasifikaci používáme **0-1 ztrátu** (což je v podstatě totéž jako **přesnost** modelu), nebo **logistickou ztrátu**.

Pro jednovrstvý perceptron byla funkce *f* definována jako lineární funkce *f(x)=wx+b* (kde *w* je matice vah, *x* je vektor vstupních vlastností a *b* je vektor posunu). Pro různé architektury neuronových sítí může tato funkce nabývat složitějšího tvaru.

> V případě klasifikace je často žádoucí získat pravděpodobnosti odpovídajících tříd jako výstup sítě. K převedení libovolných čísel na pravděpodobnosti (např. k normalizaci výstupu) často používáme funkci **softmax** σ, a funkce *f* se stává *f(x)=σ(wx+b)*

Ve výše uvedené definici *f* se *w* a *b* nazývají **parametry** θ=⟨*w,b*⟩. Při daném datasetu ⟨**X**,**Y**⟩ můžeme vypočítat celkovou chybu na celém datasetu jako funkci parametrů θ.

> ✅ **Cílem tréninku neuronové sítě je minimalizovat chybu změnou parametrů θ**

## Optimalizace pomocí gradientního sestupu

Existuje známá metoda optimalizace funkcí zvaná **gradientní sestup**. Myšlenkou je, že můžeme vypočítat derivaci (v multidimenzionálním případě nazývanou **gradient**) ztrátové funkce vzhledem k parametrům a měnit parametry takovým způsobem, že se chyba sníží. To lze formalizovat následovně:

* Inicializujte parametry nějakými náhodnými hodnotami w<sup>(0)</sup>, b<sup>(0)</sup>
* Opakujte následující krok mnohokrát:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Během tréninku se očekává, že optimalizační kroky budou počítány s ohledem na celý dataset (pamatujte, že ztráta se počítá jako součet přes všechny trénovací vzorky). Nicméně v reálném životě bereme malé části datasetu nazývané **minibatche** a počítáme gradienty na základě podmnožiny dat. Protože se podmnožina bere pokaždé náhodně, taková metoda se nazývá **stochastický gradientní sestup** (SGD).

## Vícevrstvé perceptrony a zpětná propagace

Jednovrstvá síť, jak jsme viděli výše, je schopna klasifikovat lineárně oddělitelné třídy. K vytvoření bohatšího modelu můžeme kombinovat několik vrstev sítě. Matematicky by to znamenalo, že funkce *f* by měla složitější tvar a bude vypočítávána v několika krocích:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Zde, α je **nelineární aktivační funkce**, σ je funkce softmax, a parametry θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritmus gradientního sestupu by zůstal stejný, ale bylo by obtížnější počítat gradienty. Podle pravidla řetězové diferenciace můžeme vypočítat derivace jako:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravidlo řetězové diferenciace se používá k výpočtu derivací ztrátové funkce vzhledem k parametrům.

Všimněte si, že levá část všech těchto výrazů je stejná, a proto můžeme efektivně počítat derivace počínaje ztrátovou funkcí a jít "zpětně" skrze výpočetní graf. Proto se metoda tréninku vícevrstvého perceptronu nazývá **zpětná propagace**, nebo 'backprop'.

> TODO: citace obrázku

> ✅ Zpětnou propagaci probereme mnohem podrobněji v našem příkladu v notebooku.

## Závěr

V této lekci jsme vytvořili vlastní knihovnu neuronových sítí a použili ji pro jednoduchý dvoudimenzionální klasifikační úkol.

## 🚀 Výzva

V doprovodném notebooku implementujete vlastní rámec pro vytváření a trénování vícevrstvých perceptronů. Budete moci podrobně vidět, jak moderní neuronové sítě fungují.

Pokračujte do notebooku OwnFramework a projděte si ho.

## Přehled a samostudium

Zpětná propagace je běžný algoritmus používaný v AI a ML, stojí za to ho studovat podrobněji.

## Zadání

V této laboratoři jste požádáni, abyste použili rámec, který jste vytvořili v této lekci, k řešení klasifikace ručně psaných číslic MNIST.

* Instrukce
* Notebook

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatizovaný překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace je doporučen profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.