<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:43:40+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "hu"
}
-->
# Bevezetés a neurális hálózatokba: Perceptron

Az első próbálkozások egy modern neurális hálózathoz hasonló rendszer megvalósítására Frank Rosenblatt nevéhez fűződnek, aki a Cornell Aeronautical Laboratory-nál dolgozott 1957-ben. Ez egy hardveres megvalósítás volt, amelyet "Mark-1"-nek neveztek, és amelyet primitív geometriai alakzatok, például háromszögek, négyzetek és körök felismerésére terveztek.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='A Mark 1 Perceptron' />|

> Képek a Wikipédiáról

A bemeneti kép egy 20x20-as fotocella mátrixként volt reprezentálva, így a neurális hálózatnak 400 bemenete és egy bináris kimenete volt. Egy egyszerű hálózat egy neuront tartalmazott, amelyet **küszöblogikai egységnek** is neveztek. A neurális hálózat súlyai potenciométerként működtek, amelyeket kézzel kellett beállítani a tanulási fázis során.

> ✅ A potenciométer egy olyan eszköz, amely lehetővé teszi a felhasználó számára, hogy beállítsa egy áramkör ellenállását.

> A New York Times akkoriban ezt írta a perceptronról: *az elektronikus számítógép embriója, amelyről [a Haditengerészet] azt várja, hogy képes lesz járni, beszélni, látni, írni, önmagát reprodukálni és tudatában lenni a létezésének.*

## Perceptron modell

Tegyük fel, hogy N jellemzőnk van a modellünkben, ebben az esetben a bemeneti vektor egy N méretű vektor lesz. A perceptron egy **bináris osztályozási** modell, azaz két osztály közötti különbségtételre képes a bemeneti adatok alapján. Feltételezzük, hogy minden bemeneti vektor x esetében a perceptron kimenete vagy +1, vagy -1 lesz, az osztálytól függően. A kimenetet az alábbi képlet alapján számítjuk ki:

y(x) = f(w<sup>T</sup>x)

ahol f egy lépés aktivációs függvény

## A perceptron tanítása

A perceptron tanításához meg kell találnunk egy súlyvektort w, amely a legtöbb értéket helyesen osztályozza, azaz a legkisebb **hibát** eredményezi. Ezt a hibát a **perceptron kritérium** határozza meg a következő módon:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ahol:

* az összeg azokra a tanulási adatpontokra vonatkozik i, amelyek hibás osztályozást eredményeznek
* x<sub>i</sub> a bemeneti adat, és t<sub>i</sub> -1 vagy +1 a negatív és pozitív példák esetében.

Ezt a kritériumot a súlyok w függvényeként tekintjük, és minimalizálnunk kell. Gyakran egy **gradiens csökkenés** nevű módszert alkalmaznak, amelyben néhány kezdeti súlyokkal w<sup>(0)</sup> kezdünk, majd minden lépésben frissítjük a súlyokat az alábbi képlet szerint:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Itt η az úgynevezett **tanulási ráta**, és ∇E(w) az E **gradiensét** jelöli. Miután kiszámítottuk a gradienset, az alábbi képletet kapjuk:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

A Python algoritmus így néz ki:

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

Ebben a leckében megismerkedtél a perceptronnal, amely egy bináris osztályozási modell, és megtanultad, hogyan kell tanítani egy súlyvektor használatával.

## 🚀 Kihívás

Ha szeretnéd kipróbálni saját perceptronod építését, próbáld ki ezt a labort a Microsoft Learn oldalon, amely az Azure ML tervezőt használja.

## Áttekintés és önálló tanulás

Ha szeretnéd látni, hogyan lehet perceptront használni egy játékszerű probléma, valamint valós életbeli problémák megoldására, és szeretnéd folytatni a tanulást, látogass el a Perceptron jegyzetfüzetbe.

Itt egy érdekes cikk is található a perceptronokról.

## Feladat

Ebben a leckében megvalósítottunk egy perceptront bináris osztályozási feladathoz, és használtuk két kézzel írt számjegy osztályozására. Ebben a laborban arra kérünk, hogy oldd meg a számjegy osztályozás problémáját teljes egészében, azaz határozd meg, melyik számjegy valószínűleg megfelel egy adott képnek.

* Utasítások
* Jegyzetfüzet

**Jogi nyilatkozat**:  
Ezt a dokumentumot a [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítószolgáltatás segítségével fordítottuk le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum anyanyelvén tekintendő a hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félremagyarázásokért.