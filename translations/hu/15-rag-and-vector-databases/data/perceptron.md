<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T06:42:38+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "hu"
}
-->
# Bevezetés a neurális hálózatokba: Perceptron

Az egyik első kísérlet egy modern neurális hálózat megvalósítására Frank Rosenblatt nevéhez fűződik, aki a Cornell Aeronautical Laboratoryban dolgozott 1957-ben. Ez egy hardveres megvalósítás volt, amit "Mark-1"-nek hívtak, és primitív geometriai alakzatok, például háromszögek, négyzetek és körök felismerésére tervezték.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='A Mark 1 Perceptron' />|

> Képek a Wikipédiáról

A bemeneti kép egy 20x20 fotocella mátrixként volt reprezentálva, így a neurális hálózatnak 400 bemenete és egy bináris kimenete volt. Egy egyszerű hálózat egy neuront tartalmazott, amit **küszöb logikai egységnek** is neveztek. A neurális hálózat súlyai potenciométerekként működtek, amelyek kézi beállítást igényeltek a tanulási fázis során.

> ✅ A potenciométer egy olyan eszköz, amely lehetővé teszi a felhasználó számára, hogy beállítsa egy áramkör ellenállását.

> A New York Times abban az időben így írt a perceptronról: *az elektronikus számítógép embriója, amelyről [a Haditengerészet] azt várja, hogy képes lesz járni, beszélni, látni, írni, reprodukálni önmagát és tudatában lenni a létezésének.*

## Perceptron modell

Tegyük fel, hogy N jellemzőnk van a modellünkben, ebben az esetben a bemeneti vektor egy N méretű vektor lenne. A perceptron egy **bináris osztályozási** modell, azaz két osztályt tud megkülönböztetni a bemeneti adatok közül. Feltételezzük, hogy minden bemeneti vektor x esetén a perceptronunk kimenete +1 vagy -1 lesz, az osztálytól függően. A kimenet a következő képlet alapján kerül kiszámításra:

y(x) = f(w<sup>T</sup>x)

ahol f egy lépés aktivációs függvény

## A perceptron tanítása

A perceptron tanításához meg kell találnunk egy súlyvektort w, amely a legtöbb értéket helyesen osztályozza, azaz a legkisebb **hibát** eredményezi. Ez a hiba a **perceptron kritérium** alapján van definiálva a következő módon:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ahol:

* az összeg azoknál a tanulási adatpontoknál i van véve, amelyek helytelen osztályozást eredményeznek
* x<sub>i</sub> a bemeneti adat, és t<sub>i</sub> vagy -1 vagy +1 a negatív és pozitív példák esetén.

Ezt a kritériumot a súlyok w függvényének tekintjük, és minimalizálnunk kell. Gyakran egy **gradiens csökkenés** nevű módszert alkalmaznak, amely során néhány kezdeti súllyal w<sup>(0)</sup> kezdünk, majd minden lépésnél frissítjük a súlyokat a következő képlet szerint:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Itt η az úgynevezett **tanulási ráta**, és ∇E(w) jelöli az E **gradiensét**. Miután kiszámítjuk a gradienset, a következőképpen végzünk:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Az algoritmus Pythonban így néz ki:

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

## Következtetés

Ebben a leckében megismerkedtél a perceptronnal, amely egy bináris osztályozási modell, és megtanultad, hogyan lehet tanítani egy súlyvektor használatával.

## 🚀 Kihívás

Ha szeretnéd kipróbálni saját perceptron létrehozását, próbáld ki ezt a labort a Microsoft Learn-en, amely az Azure ML tervezőt használja.

## Áttekintés és önálló tanulás

Ha szeretnéd látni, hogyan használhatjuk a perceptront játékos problémák és valós életbeli problémák megoldására, és folytatni a tanulást - menj a Perceptron jegyzetfüzethez.

Itt van egy érdekes cikk a perceptronokról is.

## Feladat

Ebben a leckében megvalósítottunk egy perceptront bináris osztályozási feladathoz, és használtuk két kézzel írott számjegy közötti osztályozásra. Ebben a laborban arra kérünk, hogy teljesen oldd meg a számjegyosztályozás problémáját, azaz határozd meg, melyik számjegy valószínűleg megfelel egy adott képnek.

* Útmutatások
* Jegyzetfüzet

**Felelősség kizárása**:  
Ez a dokumentum a [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítás ajánlott. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félremagyarázásokért.