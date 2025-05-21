<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:25:24+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "hu"
}
-->
# Bevezetés a neurális hálózatokba. Többrétegű perceptron

Az előző részben megismerkedtél a legegyszerűbb neurális hálózat modellel - az egyrétegű perceptronnal, amely egy lineáris kétosztályos osztályozó modell.

Ebben a részben kiterjesztjük ezt a modellt egy rugalmasabb keretrendszerre, amely lehetővé teszi számunkra, hogy:

* **többosztályos osztályozást** végezzünk a kétosztályos mellett
* **regressziós problémákat** oldjunk meg az osztályozás mellett
* elkülönítsük azokat az osztályokat, amelyek nem lineárisan elkülöníthetőek

Saját moduláris keretrendszert is kifejlesztünk Pythonban, amely lehetővé teszi különböző neurális hálózati architektúrák létrehozását.

## Gépi tanulás formalizálása

Kezdjük a gépi tanulás problémájának formalizálásával. Tegyük fel, hogy van egy tanuló adathalmazunk **X** címkékkel **Y**, és létre kell hoznunk egy *f* modellt, amely a lehető legpontosabb előrejelzéseket adja. Az előrejelzések minőségét a **veszteségfüggvény** ℒ méri. A következő veszteségfüggvényeket gyakran használják:

* Regressziós problémáknál, amikor egy számot kell előrejelezni, használhatjuk az **abszolút hibát** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, vagy a **négyzetes hibát** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Osztályozásnál használjuk a **0-1 veszteséget** (ami lényegében ugyanaz, mint a modell **pontossága**), vagy a **logisztikus veszteséget**.

Az egyrétegű perceptron esetében az *f* függvényt lineáris függvényként határoztuk meg *f(x)=wx+b* (ahol *w* a súlymátrix, *x* a bemeneti jellemzők vektora, és *b* az eltolás vektora). Különböző neurális hálózati architektúrák esetén ez a függvény összetettebb formát ölthet.

> Osztályozás esetén gyakran kívánatos, hogy a hálózat kimeneteként a megfelelő osztályok valószínűségeit kapjuk meg. Az önkényes számok valószínűségekké alakításához (pl. a kimenet normalizálásához) gyakran használjuk a **softmax** függvényt σ, és az *f* függvény így alakul: *f(x)=σ(wx+b)*

Az *f* fenti definíciójában *w* és *b* **paramétereknek** nevezzük, θ=⟨*w,b*⟩. Az adathalmaz ⟨**X**,**Y**⟩ alapján kiszámíthatjuk a teljes adathalmazon az összesített hibát, mint a paraméterek θ függvényét.

> ✅ **A neurális hálózatok tanításának célja a hiba minimalizálása a paraméterek θ változtatásával**

## Gradiens lejtmenet optimalizálás

Van egy jól ismert függvényoptimalizálási módszer, amelyet **gradiens lejtmenetnek** neveznek. Az ötlet az, hogy kiszámíthatjuk a veszteségfüggvény deriváltját (többdimenziós esetben **gradiensnek** nevezzük) a paraméterekre vonatkozóan, és úgy változtathatjuk a paramétereket, hogy a hiba csökkenjen. Ezt a következőképpen formalizálhatjuk:

* Inicializáljuk a paramétereket véletlenszerű értékekkel w<sup>(0)</sup>, b<sup>(0)</sup>
* Ismételjük meg a következő lépést sokszor:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

A tanítás során az optimalizálási lépéseket a teljes adathalmaz figyelembevételével kell kiszámítani (ne feledd, hogy a veszteséget az összes tanuló minta összegzéseként számítjuk). Azonban a valóságban az adathalmaz kis részleteit, úgynevezett **minibatch-eket** veszünk, és az adatok egy részhalmazán alapuló gradiensszámítást végzünk. Mivel a részhalmaz minden alkalommal véletlenszerűen kerül kiválasztásra, ezt a módszert **sztochasztikus gradiens lejtmenetnek** (SGD) nevezzük.

## Többrétegű perceptronok és visszaterjesztés

Ahogy láttuk, az egyrétegű hálózat képes lineárisan elkülöníthető osztályok osztályozására. Egy gazdagabb modell létrehozásához több réteget kombinálhatunk a hálózatban. Matematikailag ez azt jelentené, hogy az *f* függvény összetettebb formát ölt, és több lépésben számítódik ki:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Itt α egy **nemlineáris aktivációs függvény**, σ egy softmax függvény, és a paraméterek θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

A gradiens lejtmenet algoritmus ugyanaz maradna, de a gradiensszámítás bonyolultabbá válna. A láncszabály alkalmazásával a deriváltakat a következőképpen számíthatjuk ki:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ A láncszabályt a veszteségfüggvény deriváltjainak kiszámítására használják a paraméterekkel szemben.

Figyeljük meg, hogy ezeknek a kifejezéseknek a bal szélső része ugyanaz, így hatékonyan kiszámíthatjuk a deriváltakat a veszteségfüggvénytől kezdve, és "visszafelé" haladva a számítási gráfon keresztül. Így a többrétegű perceptron tanítási módszerét **visszaterjesztésnek**, vagy 'backprop'-nak nevezzük.

> TODO: kép hivatkozás

> ✅ A visszaterjesztést sokkal részletesebben fogjuk megvizsgálni a notebook példánkban.

## Összefoglalás

Ebben a leckében saját neurális hálózati könyvtárat építettünk, és egy egyszerű kétdimenziós osztályozási feladatra használtuk.

## 🚀 Kihívás

A mellékelt notebookban megvalósítod a saját keretrendszeredet többrétegű perceptronok építésére és tanítására. Részletesen megismerheted, hogyan működnek a modern neurális hálózatok.

Haladj tovább az OwnFramework notebookhoz és dolgozz rajta.

## Áttekintés és önálló tanulás

A visszaterjesztés egy gyakori algoritmus az AI és ML területén, érdemes részletesebben tanulmányozni.

## Feladat

Ebben a laborban arra kérünk, hogy a jelen leckében felépített keretrendszerrel oldd meg az MNIST kézzel írott számjegyek osztályozását.

* Utasítások
* Notebook

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) használatával lett lefordítva. Bár igyekszünk pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelven tekintendő hiteles forrásnak. Kritikus információk esetén ajánlott a professzionális emberi fordítás. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félremagyarázásokért.