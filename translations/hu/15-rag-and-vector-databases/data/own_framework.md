<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:29:26+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "hu"
}
-->
# Bevezetés a Neurális Hálózatokba. Többrétegű Perceptron

Az előző részben megismerkedtél a legegyszerűbb neurális hálózat modellel - az egyrétegű perceptronnal, egy lineáris kétosztályú osztályozási modellel.

Ebben a részben kiterjesztjük ezt a modellt egy rugalmasabb keretrendszerre, amely lehetővé teszi számunkra:

* **többosztályú osztályozást** végrehajtani a kétosztályú mellett
* **regressziós problémákat** megoldani az osztályozás mellett
* nem lineárisan elválasztható osztályokat szétválasztani

Ezenkívül kifejlesztjük saját moduláris keretrendszerünket Pythonban, amely lehetővé teszi számunkra különböző neurális hálózati architektúrák felépítését.

## Gépi Tanulás Formalizálása

Kezdjük a gépi tanulás problémájának formalizálásával. Tegyük fel, hogy van egy edzési adathalmazunk **X** címkékkel **Y**, és szükségünk van egy modellre *f*, amely a legpontosabb előrejelzéseket adja. Az előrejelzések minőségét a **veszteségfüggvény** ℒ méri. A következő veszteségfüggvényeket gyakran használják:

* Regressziós probléma esetén, amikor egy számot kell előre jeleznünk, használhatjuk az **abszolút hibát** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, vagy a **négyzetes hibát** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Osztályozásnál a **0-1 veszteséget** (ami lényegében ugyanaz, mint a modell **pontossága**), vagy a **logisztikus veszteséget** használjuk.

Az egyszintű perceptron esetében az *f* függvény egy lineáris függvényként volt definiálva *f(x)=wx+b* (ahol *w* a súlymátrix, *x* a bemeneti jellemzők vektora, és *b* az eltolás vektora). Különböző neurális hálózati architektúrák esetében ez a függvény összetettebb formát ölthet.

> Osztályozás esetén gyakran kívánatos, hogy az adott osztályok valószínűségeit kapjuk meg a hálózat kimeneteként. Az önkényes számok valószínűségekké való átalakításához (például a kimenet normalizálásához) gyakran használjuk a **softmax** függvényt σ, és az *f* függvény *f(x)=σ(wx+b)* formát ölt

Az *f* fent meghatározott definíciójában *w* és *b* a **paraméterek** θ=⟨*w,b*⟩. Az adathalmaz ⟨**X**,**Y**⟩ alapján kiszámíthatjuk az összes hibát az egész adathalmazon a paraméterek θ függvényében.

> ✅ **A neurális hálózatok tanításának célja a hiba minimalizálása a paraméterek θ változtatásával**

## Gradiens Descent Optimalizálás

Van egy jól ismert módszer a függvény optimalizálására, amelyet **gradiens descent**-nek neveznek. Az ötlet az, hogy kiszámíthatjuk a deriváltat (többdimenziós esetben **gradiens**-nek nevezzük) a veszteségfüggvény paraméterekre vonatkozóan, és úgy változtathatjuk a paramétereket, hogy a hiba csökkenjen. Ez formálisan így fogalmazható meg:

* Inicializáljuk a paramétereket néhány véletlen értékkel w<sup>(0)</sup>, b<sup>(0)</sup>
* Ismételjük meg a következő lépést sokszor:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

A képzés során az optimalizálási lépéseket az egész adathalmaz figyelembevételével kell kiszámítani (ne feledjük, hogy a veszteség az összes edzési minta összegzéseként van kiszámítva). Azonban a valós életben az adathalmaz kis részeit, úgynevezett **minibatch-eket** vesszük, és a gradiens-eket az adatok egy részhalmazán alapulva számítjuk ki. Mivel minden alkalommal véletlenszerűen veszünk részhalmazt, ezt a módszert **sztochasztikus gradiens descent**-nek (SGD) nevezik.

## Többrétegű Perceptronok és Backpropagation

Ahogy fentebb láttuk, az egyrétegű hálózat képes lineárisan elválasztható osztályokat osztályozni. A gazdagabb modell építéséhez kombinálhatunk több réteget a hálózatban. Matematikailag ez azt jelentené, hogy az *f* függvény összetettebb formát ölt, és több lépésben lesz kiszámítva:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Itt α egy **nemlineáris aktivációs függvény**, σ egy softmax függvény, és a paraméterek θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

A gradiens descent algoritmus ugyanaz marad, de nehezebb lesz a gradiens-ek kiszámítása. Az összetett deriválás szabálya alapján a deriváltakat így számíthatjuk ki:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Az összetett deriválás szabályát használjuk a veszteségfüggvény paraméterekre vonatkozó deriváltjainak kiszámításához.

Figyeljük meg, hogy ezeknek a kifejezéseknek a bal szélső része ugyanaz, így hatékonyan számíthatjuk ki a deriváltakat a veszteségfüggvénytől kezdve, és "visszafelé" haladva a számítási gráfon. Ezért a többrétegű perceptron tanítási módszerét **backpropagation**-nek, vagy 'backprop'-nak nevezzük.

> TODO: kép forrásmegjelölés

> ✅ A backpropagation-t sokkal részletesebben fogjuk tárgyalni a notebook példánkban.

## Következtetés

Ebben a leckében saját neurális hálózat könyvtárat építettünk, és egy egyszerű kétdimenziós osztályozási feladatra használtuk.

## 🚀 Kihívás

A kísérő notebookban saját keretrendszert fogsz megvalósítani többrétegű perceptronok építésére és tanítására. Részletesen megfigyelheted, hogyan működnek a modern neurális hálózatok.

Folytasd az OwnFramework notebookkal és dolgozd át.

## Felülvizsgálat és Önálló Tanulás

A backpropagation egy gyakori algoritmus az AI és ML területén, érdemes részletesebben tanulmányozni.

## Feladat

Ebben a laborban arra kérünk, hogy a keretrendszert, amit ebben a leckében építettél, használd az MNIST kézzel írt számjegyek osztályozására.

* Utasítások
* Notebook

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás használatával készült fordítás. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.