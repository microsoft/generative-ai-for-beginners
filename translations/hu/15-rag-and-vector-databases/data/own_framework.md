<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:50:16+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "hu"
}
-->
# Bevezetés a neurális hálózatokba. Többrétegű perceptron

Az előző részben megismerted a legegyszerűbb neurális hálózati modellt – az egyrétegű perceptront, ami egy lineáris kétosztályos osztályozó modell.

Ebben a részben ezt a modellt egy rugalmasabb keretrendszerré bővítjük, amely lehetővé teszi számunkra, hogy:

* végezzünk **többosztályos osztályozást** a kétosztályos mellett
* oldjunk meg **regressziós problémákat** az osztályozás mellett
* szétválasszuk azokat az osztályokat, amelyek nem lineárisan elválaszthatók

Emellett saját moduláris keretrendszert is fejlesztünk Pythonban, amely lehetővé teszi különböző neurális hálózati architektúrák felépítését.

## A gépi tanulás formalizálása

Kezdjük a gépi tanulás problémájának formalizálásával. Tegyük fel, hogy van egy tanító adatbázisunk **X** címkékkel **Y**, és egy olyan modellt *f* kell építenünk, amely a lehető legpontosabb előrejelzéseket adja. Az előrejelzések minőségét a **veszteségfüggvény** ℒ méri. A következő veszteségfüggvényeket használjuk gyakran:

* Regressziós problémánál, amikor számot kell előre jelezni, használhatjuk az **abszolút hibát** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, vagy a **négyzetes hibát** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Osztályozásnál használjuk a **0-1 veszteséget** (ami lényegében a modell **pontosságával** egyezik meg), vagy a **logisztikus veszteséget**.

Az egyrétegű perceptron esetén az *f* függvényt lineáris függvényként definiáltuk: *f(x)=wx+b* (itt *w* a súlymátrix, *x* a bemeneti jellemzők vektora, és *b* az eltolásvektor). Különböző neurális hálózati architektúráknál ez a függvény bonyolultabb formát ölthet.

> Osztályozás esetén gyakran kívánatos, hogy a hálózat kimenete az adott osztályok valószínűsége legyen. Az általános számokat valószínűségekké alakításhoz (például a kimenet normalizálásához) gyakran használjuk a **softmax** függvényt σ, így az *f* függvény *f(x)=σ(wx+b)* lesz.

Az *f* definíciójában *w* és *b* az ún. **paraméterek** θ=⟨*w,b*⟩. Adott az adatbázis ⟨**X**,**Y**⟩, kiszámíthatjuk az összesített hibát az egész adathalmazon a paraméterek θ függvényében.

> ✅ **A neurális hálózat tanításának célja, hogy a paraméterek változtatásával minimalizáljuk a hibát.**

## Gradiens csökkenéses optimalizáció

Ismert módszer a függvényoptimalizálásra a **gradiens csökkenés**. Az ötlet az, hogy kiszámoljuk a veszteségfüggvény deriváltját (többdimenziós esetben **gradiensét**) a paraméterek szerint, és úgy változtatjuk a paramétereket, hogy a hiba csökkenjen. Ezt a következőképpen formalizálhatjuk:

* Inicializáljuk a paramétereket véletlenszerű értékekkel w<sup>(0)</sup>, b<sup>(0)</sup>
* Ismételjük a következő lépést sokszor:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

A tanítás során az optimalizációs lépéseket az egész adathalmaz figyelembevételével kellene kiszámolni (emlékezzünk, hogy a veszteség az összes tanító minta összegzése). Azonban a gyakorlatban az adathalmazból kis részeket, ún. **minicsomagokat** (minibatch-eket) veszünk, és ezek alapján számoljuk a gradiens értékeket. Mivel a részhalmaz minden alkalommal véletlenszerűen kerül kiválasztásra, ezt a módszert **sztochasztikus gradiens csökkenésnek** (SGD) nevezzük.

## Többrétegű perceptronok és visszaterjesztés

Az egyrétegű hálózat, ahogy láttuk, képes lineárisan elválasztható osztályokat osztályozni. Egy gazdagabb modell felépítéséhez több réteget kapcsolhatunk össze. Matematikailag ez azt jelenti, hogy az *f* függvény bonyolultabb formát ölt, és több lépésben számoljuk ki:

* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Itt α egy **nemlineáris aktivációs függvény**, σ a softmax függvény, és a paraméterek θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

A gradiens csökkenés algoritmusa ugyanaz marad, de a gradiens kiszámítása bonyolultabbá válik. A láncszabály segítségével a deriváltakat így számolhatjuk:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ A láncszabályt használjuk a veszteségfüggvény paraméterek szerinti deriváltjainak kiszámításához.

Fontos megjegyezni, hogy ezeknek a kifejezéseknek a bal szélső része azonos, így hatékonyan számolhatjuk a deriváltakat a veszteségfüggvénytől kiindulva, "visszafelé" haladva a számítási gráfon. Ezért a többrétegű perceptron tanítási módszerét **visszaterjesztésnek** vagy 'backprop'-nak nevezzük.

> TODO: kép forrása

> ✅ A visszaterjesztést részletesebben is bemutatjuk a jegyzetfüzetünkben.

## Összefoglalás

Ebben a leckében saját neurális hálózati könyvtárat építettünk, és egy egyszerű kétdimenziós osztályozási feladaton használtuk.

## 🚀 Kihívás

A mellékelt jegyzetfüzetben megvalósítod saját keretrendszeredet többrétegű perceptronok építésére és tanítására. Részletesen megismerheted, hogyan működnek a modern neurális hálózatok.

Folytasd az OwnFramework jegyzetfüzettel, és dolgozd végig.

## Áttekintés és önálló tanulás

A visszaterjesztés egy gyakori algoritmus az AI és ML területén, érdemes mélyebben tanulmányozni.

## Feladat

Ebben a laborban a leckében felépített keretrendszert használva kell megoldanod az MNIST kézírásos számfelismerési osztályozási feladatot.

* Útmutató
* Jegyzetfüzet

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.