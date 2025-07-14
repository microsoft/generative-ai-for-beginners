<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T17:00:26+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "hu"
}
-->
# Bevezetés a neurális hálózatokba: Perceptron

Az egyik első kísérlet arra, hogy valami hasonlót hozzanak létre a modern neurális hálózathoz, Frank Rosenblatt nevéhez fűződik, aki 1957-ben a Cornell Aeronautical Laboratory-nál dolgozott. Ez egy hardveres megvalósítás volt, amit "Mark-1"-nek neveztek, és primitív geometriai alakzatok, például háromszögek, négyzetek és körök felismerésére tervezték.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Képek a Wikipédiáról

A bemeneti képet egy 20x20-as fotocella-rács reprezentálta, így a neurális hálózatnak 400 bemenete és egy bináris kimenete volt. Egy egyszerű hálózat egyetlen neuront tartalmazott, amit **küszöblogikai egységnek** is neveznek. A neurális hálózat súlyai potméterekhez hasonlóan működtek, amelyeket a tanulási fázis során kézzel kellett beállítani.

> ✅ A potméter egy olyan eszköz, amely lehetővé teszi a felhasználó számára az áramkör ellenállásának állítását.

> A New York Times akkoriban így írt a perceptronról: *az elektronikus számítógép embriója, amelyről a [Haditengerészet] azt várja, hogy képes lesz járni, beszélni, látni, írni, önmagát reprodukálni és tudatában lenni a létezésének.*

## Perceptron modell

Tegyük fel, hogy a modellünkben N jellemző van, ekkor a bemeneti vektor mérete N lesz. A perceptron egy **bináris osztályozó** modell, vagyis képes megkülönböztetni két osztályba tartozó bemeneti adatot. Feltételezzük, hogy minden bemeneti vektor x esetén a perceptron kimenete vagy +1, vagy -1 lesz, az osztálytól függően. A kimenetet a következő képlettel számítjuk ki:

y(x) = f(w<sup>T</sup>x)

ahol f egy lépcsős aktivációs függvény

## A perceptron tanítása

A perceptron tanításához meg kell találnunk egy w súlyvektort, amely a legtöbb értéket helyesen osztályozza, vagyis a legkisebb **hibát** eredményezi. Ezt a hibát a **perceptron kritérium** a következőképpen definiálja:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ahol:

* az összeg azokból a tanító adatpontokból i származik, amelyek helytelen osztályozást eredményeznek
* x<sub>i</sub> a bemeneti adat, t<sub>i</sub> pedig -1 vagy +1 a negatív és pozitív példák esetén.

Ezt a kritériumot a súlyok w függvényének tekintjük, és minimalizálni szeretnénk. Gyakran alkalmazzák a **gradiens csökkenés** nevű módszert, amely során egy kezdeti súlyvektorral w<sup>(0)</sup> indulunk, majd minden lépésben a súlyokat a következő képlettel frissítjük:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Itt η az úgynevezett **tanulási ráta**, ∇E(w) pedig E gradiensét jelöli. A gradiens kiszámítása után a képlet a következő lesz:

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

## Összefoglalás

Ebben a leckében megismerted a perceptront, amely egy bináris osztályozó modell, és azt, hogyan tanítható egy súlyvektor segítségével.

## 🚀 Kihívás

Ha szeretnéd kipróbálni a saját perceptronod megépítését, próbáld ki ezt a Microsoft Learn laboratóriumot, amely az Azure ML designer-t használja.

## Áttekintés és önálló tanulás

Ahhoz, hogy megtudd, hogyan használhatjuk a perceptront játékos problémák és valós életbeli feladatok megoldására, és hogy tovább tanulhass, látogass el a Perceptron jegyzetfüzethez.

Itt egy érdekes cikk is a perceptronokról.

## Feladat

Ebben a leckében egy bináris osztályozási feladatra implementáltunk egy perceptront, és két kézzel írt számjegy osztályozására használtuk. Ebben a laborban azt a feladatot kell megoldanod, hogy teljes egészében osztályozd a számjegyeket, vagyis határozd meg, melyik számjegy valószínűleg melyik képen szerepel.

* Utasítások
* Jegyzetfüzet

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.