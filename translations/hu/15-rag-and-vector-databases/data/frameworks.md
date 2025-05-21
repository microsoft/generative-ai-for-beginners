<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:05:38+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "hu"
}
-->
# Neurális Hálózat Keretrendszerek

Ahogy már megtanultuk, a neurális hálók hatékony tanításához két dolgot kell tennünk:

* Műveleteket végezni tenzorokon, például szorzás, összeadás, és néhány függvény, mint a szigmoid vagy softmax kiszámítása
* Az összes kifejezés deriváltját kiszámítani, hogy gradient descent optimalizálást végezhessünk

Míg a `numpy` könyvtár elvégezheti az első részt, szükségünk van valamilyen mechanizmusra a deriváltak kiszámításához. Az általunk az előző szakaszban kifejlesztett keretrendszerben manuálisan kellett programoznunk az összes derivált függvényt a `backward` metódusban, amely a backpropagation-t végzi. Ideális esetben egy keretrendszernek lehetőséget kellene biztosítania számunkra, hogy *bármely kifejezés* deriváltját kiszámítsuk, amit meg tudunk határozni.

Egy másik fontos dolog, hogy képesek legyünk számításokat végezni GPU-n vagy bármilyen más speciális számítási egységen, mint például a TPU. A mély neurális háló tanítása *sok* számítást igényel, és nagyon fontos, hogy ezeket a számításokat párhuzamosíthassuk GPU-kon.

> ✅ A 'párhuzamosítás' kifejezés azt jelenti, hogy a számításokat több eszközre osztjuk szét.

Jelenleg a két legnépszerűbb neurális keretrendszer: TensorFlow és PyTorch. Mindkettő alacsony szintű API-t biztosít a tenzorokkal való műveletekhez mind CPU-n, mind GPU-n. Az alacsony szintű API fölött létezik egy magasabb szintű API is, amelyet Kerasnak és PyTorch Lightningnak hívnak.

Alacsony szintű API | TensorFlow | PyTorch
--------------|-------------------------------------|--------------------------------
Magas szintű API | Keras | Pytorch

**Az alacsony szintű API-k** mindkét keretrendszerben lehetővé teszik az úgynevezett **számítási gráfok** felépítését. Ez a gráf határozza meg, hogyan kell kiszámítani a kimenetet (általában a veszteségfüggvényt) a megadott bemeneti paraméterekkel, és ha elérhető, átadható a GPU-n való számításra. Vannak funkciók, amelyekkel megkülönböztethetjük ezt a számítási gráfot és kiszámíthatjuk a deriváltakat, amelyeket aztán a modell paramétereinek optimalizálására használhatunk.

**A magas szintű API-k** nagyrészt a neurális hálókat **rétegek sorozataként** kezelik, és megkönnyítik a legtöbb neurális háló felépítését. A modell tanítása általában az adatok előkészítését igényli, majd egy `fit` függvény hívását a feladat elvégzéséhez.

A magas szintű API lehetővé teszi, hogy tipikus neurális hálókat nagyon gyorsan építsünk fel anélkül, hogy sok részlet miatt aggódnánk. Ugyanakkor az alacsony szintű API sokkal nagyobb kontrollt biztosít a tanítási folyamat felett, ezért sokat használják a kutatásban, amikor új neurális háló architektúrákkal foglalkozunk.

Fontos megérteni, hogy mindkét API-t együtt is használhatjuk, például fejleszthetjük saját hálózati réteg architektúránkat alacsony szintű API-val, majd használhatjuk azt a magas szintű API-val konstruált és tanított nagyobb hálózatban. Vagy meghatározhatunk egy hálózatot a magas szintű API-val rétegek sorozataként, majd használhatjuk saját alacsony szintű tanítási ciklusunkat az optimalizálás végrehajtásához. Mindkét API ugyanazokat az alapvető fogalmakat használja, és úgy tervezték őket, hogy jól működjenek együtt.

## Tanulás

Ebben a kurzusban a legtöbb tartalmat mind PyTorch, mind TensorFlow számára kínáljuk. Választhatod a kedvenc keretrendszered, és csak a megfelelő jegyzetfüzeteket olvashatod el. Ha nem vagy biztos benne, melyik keretrendszert válaszd, olvass el néhány internetes vitát a **PyTorch vs. TensorFlow** témában. Megnézheted mindkét keretrendszert is, hogy jobban megértsd őket.

Ahol lehetséges, a magas szintű API-kat fogjuk használni az egyszerűség kedvéért. Ugyanakkor úgy gondoljuk, fontos megérteni, hogyan működnek a neurális hálók az alapoktól kezdve, ezért kezdetben az alacsony szintű API-val és tenzorokkal dolgozunk. Azonban ha gyorsan szeretnél haladni, és nem akarsz sok időt tölteni ezeknek a részleteknek a megtanulásával, átugorhatod ezeket, és közvetlenül a magas szintű API jegyzetfüzetekbe kezdhetsz.

## ✍️ Gyakorlatok: Keretrendszerek

Folytasd a tanulást a következő jegyzetfüzetekben:

Alacsony szintű API | TensorFlow+Keras Jegyzetfüzet | PyTorch
--------------|-------------------------------------|--------------------------------
Magas szintű API | Keras | *PyTorch Lightning*

Miután elsajátítottad a keretrendszereket, foglaljuk össze az overfitting fogalmát.

# Overfitting

Az overfitting rendkívül fontos fogalom a gépi tanulásban, és nagyon fontos, hogy helyesen kezeljük!

Tekintsük a következő problémát, amely 5 pontot közelít (amit a `x` jelöl az alábbi gráfokon):

!linear | overfit
-------------------------|--------------------------
**Lineáris modell, 2 paraméter** | **Nem-lineáris modell, 7 paraméter**
Tanítási hiba = 5.3 | Tanítási hiba = 0
Validációs hiba = 5.1 | Validációs hiba = 20

* Balra egy jó egyenes vonal közelítést látunk. Mivel a paraméterek száma megfelelő, a modell helyesen érti a pontok eloszlását.
* Jobbra a modell túl erős. Mivel csak 5 pontunk van, és a modellnek 7 paramétere, úgy tudja beállítani magát, hogy mindegyik ponton áthaladjon, így a tanítási hiba 0 lesz. Ez azonban megakadályozza, hogy a modell megértse az adatok mögötti helyes mintázatot, így a validációs hiba nagyon magas.

Nagyon fontos megtalálni a megfelelő egyensúlyt a modell gazdagsága (paraméterek száma) és a tanító minták száma között.

## Miért fordul elő overfitting

  * Nem elég tanító adat
  * Túl erős modell
  * Túl sok zaj a bemeneti adatokban

## Hogyan lehet felismerni az overfittinget

Ahogy a fenti gráfról is látható, az overfittinget nagyon alacsony tanítási hibával és magas validációs hibával lehet felismerni. Általában a tanítás során azt látjuk, hogy mind a tanítási, mind a validációs hibák csökkenni kezdenek, majd egy ponton a validációs hiba megállhat a csökkenésben és emelkedni kezdhet. Ez az overfitting jele lesz, és annak az indikátora, hogy valószínűleg abba kellene hagynunk a tanítást (vagy legalábbis készíteni egy pillanatképet a modellről).

## Hogyan lehet megelőzni az overfittinget

Ha látod, hogy overfitting történik, az alábbiakat teheted:

 * Növeld a tanító adatok mennyiségét
 * Csökkentsd a modell bonyolultságát
 * Használj valamilyen regularizációs technikát, mint például a Dropout, amit később megvizsgálunk.

## Overfitting és Bias-Variance Tradeoff

Az overfitting valójában egy általánosabb probléma esete a statisztikában, amit Bias-Variance Tradeoff-nak hívnak. Ha megvizsgáljuk a modellünk lehetséges hibaforrásait, kétféle hibát láthatunk:

* **Bias hibák** abból adódnak, hogy algoritmusunk nem képes helyesen megragadni a kapcsolatot a tanító adatok között. Ez abból fakadhat, hogy a modellünk nem elég erős (**underfitting**).
* **Variance hibák**, amelyek abból adódnak, hogy a modell a bemeneti adatok zaját közelíti ahelyett, hogy értelmes kapcsolatot találna (**overfitting**).

A tanítás során a bias hiba csökken (ahogy a modell megtanulja közelíteni az adatokat), és a variance hiba nő. Fontos abbahagyni a tanítást - akár manuálisan (amikor overfittinget észlelünk), akár automatikusan (regularizáció bevezetésével) -, hogy megelőzzük az overfittinget.

## Következtetés

Ebben a leckében megismerkedtél a két legnépszerűbb AI keretrendszer, a TensorFlow és a PyTorch különböző API-jainak különbségeivel. Ezen kívül megismerkedtél egy nagyon fontos témával, az overfittinggel.

## 🚀 Kihívás

A mellékelt jegyzetfüzetekben 'feladatokat' találsz az alján; dolgozd végig a jegyzetfüzeteket és végezd el a feladatokat.

## Áttekintés és Önálló Tanulás

Végezz kutatást a következő témákban:

- TensorFlow
- PyTorch
- Overfitting

Tedd fel magadnak a következő kérdéseket:

- Mi a különbség a TensorFlow és a PyTorch között?
- Mi a különbség az overfitting és az underfitting között?

## Feladat

Ebben a laborban két osztályozási problémát kell megoldanod egy- és többrétegű, teljesen összekapcsolt hálózatok használatával PyTorch vagy TensorFlow segítségével.

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás használatával készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum saját nyelvén tekintendő a hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.