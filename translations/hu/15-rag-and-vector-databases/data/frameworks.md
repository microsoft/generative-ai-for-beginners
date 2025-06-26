<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:08:55+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "hu"
}
-->
# Neurális hálózat keretrendszerek

Ahogy már megtanultuk, a neurális hálózatok hatékony tanításához két dolgot kell tennünk:

* Műveleteket kell végezni tenzorokon, például szorzás, összeadás, és néhány függvény kiszámítása, mint a sigmoid vagy softmax
* Az összes kifejezés gradiensét kell kiszámítani, hogy gradiens alapú optimalizálást végezhessünk

Míg az `numpy` könyvtár képes az első részre, szükségünk van egy mechanizmusra a gradiens kiszámításához. Az általunk a korábbi szakaszban kifejlesztett keretrendszerben manuálisan kellett programoznunk az összes derivált függvényt az `backward` módszeren belül, ami a visszaterjesztést végzi. Ideális esetben egy keretrendszernek lehetőséget kellene adnia, hogy *bármely kifejezés* gradiensét kiszámítsuk, amit definiálni tudunk.

Egy másik fontos dolog, hogy képesek legyünk GPU-n vagy bármilyen más speciális számítási egységen, mint például TPU, végrehajtani a számításokat. A mély neurális hálózatok tanítása *sok* számítást igényel, és nagyon fontos, hogy ezeket a számításokat párhuzamosíthassuk GPU-kon.

> ✅ A 'párhuzamosítás' kifejezés azt jelenti, hogy a számításokat több eszközön osztjuk szét.

Jelenleg a két legnépszerűbb neurális keretrendszer: TensorFlow és PyTorch. Mindkettő alacsony szintű API-t biztosít a tenzorokkal való műveletekhez CPU-n és GPU-n egyaránt. Az alacsony szintű API mellett van egy magasabb szintű API is, amelyet Kerasnak és PyTorch Lightningnek hívnak.

Alacsony szintű API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
Magas szintű API| Keras| PyTorch Lightning

**Alacsony szintű API-k** mindkét keretrendszerben lehetővé teszik úgynevezett **számítási gráfok** építését. Ez a gráf meghatározza, hogyan számítsuk ki a kimenetet (általában a veszteségfüggvényt) adott bemeneti paraméterekkel, és GPU-n is futtatható, ha elérhető. Vannak funkciók, amelyekkel különböző számítási gráfokat lehet megkülönböztetni és kiszámítani a gradienseket, amelyek aztán felhasználhatók a modell paramétereinek optimalizálására.

**Magas szintű API-k** a neurális hálózatokat lényegében **rétegek sorozataként** kezelik, és a legtöbb neurális hálózat építését sokkal egyszerűbbé teszik. A modell tanítása általában az adatok előkészítését igényli, majd egy `fit` függvény meghívását a feladat elvégzésére.

A magas szintű API lehetővé teszi, hogy tipikus neurális hálózatokat nagyon gyorsan építsünk fel, anélkül, hogy sok részlet miatt aggódnánk. Ugyanakkor az alacsony szintű API sokkal nagyobb kontrollt biztosít a tanítási folyamat felett, ezért sokat használják kutatásban, amikor új neurális hálózati architektúrákkal foglalkoznak.

Fontos megérteni, hogy mindkét API-t együtt is használhatjuk, például kifejleszthetjük saját hálózati réteg architektúránkat alacsony szintű API-val, majd használhatjuk azt a nagyobb hálózaton belül, amelyet a magas szintű API-val építettünk és tanítottunk. Vagy definiálhatunk egy hálózatot a magas szintű API-val rétegek sorozataként, majd használhatjuk saját alacsony szintű tanítási ciklusunkat az optimalizálás elvégzésére. Mindkét API ugyanazokat az alapvető koncepciókat használja, és úgy van kialakítva, hogy jól működjön együtt.

## Tanulás

Ebben a kurzusban a legtöbb tartalmat mind PyTorch, mind TensorFlow számára kínáljuk. Kiválaszthatja a preferált keretrendszert, és csak a megfelelő jegyzetfüzeteket nézheti át. Ha nem biztos benne, melyik keretrendszert válassza, olvasson néhány vitát az interneten a **PyTorch vs. TensorFlow** témában. Megnézheti mindkét keretrendszert is, hogy jobban megértse őket.

Ahol lehet, magas szintű API-kat fogunk használni az egyszerűség kedvéért. Azonban úgy véljük, fontos megérteni, hogyan működnek a neurális hálózatok az alapoktól kezdve, ezért kezdetben alacsony szintű API-val és tenzorokkal dolgozunk. Azonban, ha gyorsan szeretne haladni, és nem szeretne sok időt tölteni ezeknek a részleteknek a megtanulásával, átugorhatja ezeket, és közvetlenül a magas szintű API jegyzetfüzetekbe léphet.

## ✍️ Gyakorlatok: Keretrendszerek

Folytassa a tanulást a következő jegyzetfüzetekben:

Alacsony szintű API | TensorFlow+Keras Jegyzetfüzet | PyTorch
--------------|-------------------------------------|--------------------------------
Magas szintű API| Keras | *PyTorch Lightning*

A keretrendszerek elsajátítása után tekintsük át a túlillesztés fogalmát.

# Túlillesztés

A túlillesztés rendkívül fontos fogalom a gépi tanulásban, és nagyon fontos, hogy jól értsük!

Vegyük figyelembe az alábbi problémát, amely 5 pontot közelít meg (amelyet `x` képvisel az alábbi grafikonokon):

!linear | túlillesztés
-------------------------|--------------------------
**Lineáris modell, 2 paraméter** | **Nem-lineáris modell, 7 paraméter**
Tanítási hiba = 5.3 | Tanítási hiba = 0
Validációs hiba = 5.1 | Validációs hiba = 20

* Bal oldalon egy jó egyenes vonal közelítést látunk. Mivel a paraméterek száma megfelelő, a modell jól érti a pontok eloszlása mögött rejlő ötletet.
* Jobb oldalon a modell túl erős. Mivel csak 5 pontunk van, és a modellnek 7 paramétere van, úgy tudja beállítani magát, hogy minden ponton áthaladjon, így a tanítási hiba 0 lesz. Ez azonban megakadályozza a modellt abban, hogy megértse az adatok mögött rejlő helyes mintát, így a validációs hiba nagyon magas.

Nagyon fontos, hogy megtaláljuk a megfelelő egyensúlyt a modell gazdagsága (paraméterek száma) és a tanító minták száma között.

## Miért fordul elő túlillesztés

  * Nem elég tanító adat
  * Túl erős modell
  * Túl sok zaj a bemeneti adatokban

## Hogyan lehet észlelni a túlillesztést

Ahogy a fenti grafikonon látható, a túlillesztést nagyon alacsony tanítási hiba és magas validációs hiba jelzi. Általában a tanítás során mind a tanítási, mind a validációs hibák csökkenni kezdenek, majd egy bizonyos ponton a validációs hiba megállhat a csökkenésben és növekedni kezdhet. Ez a túlillesztés jele lesz, és azt jelzi, hogy valószínűleg meg kellene állítanunk a tanítást ezen a ponton (vagy legalábbis készítsünk egy pillanatképet a modellről).

túlillesztés

## Hogyan lehet megelőzni a túlillesztést

Ha látja, hogy túlillesztés történik, az alábbiakat teheti:

 * Növelje a tanító adatok mennyiségét
 * Csökkentse a modell összetettségét
 * Használjon valamilyen regularizációs technikát, például Dropoutot, amelyet később megvizsgálunk.

## Túlillesztés és Bias-Variance Tradeoff

A túlillesztés valójában egy általánosabb statisztikai probléma esete, amelyet Bias-Variance Tradeoffnak neveznek. Ha figyelembe vesszük a modellünk hibaforrásait, kétféle hibát láthatunk:

* **Bias hibák**, amelyeket az algoritmusunk nem képes helyesen megragadni a tanító adatok közötti kapcsolatot. Ez abból adódhat, hogy a modellünk nem elég erős (**alulillesztés**).
* **Variance hibák**, amelyeket a modell a bemeneti adatok zajának közelítése okoz ahelyett, hogy jelentős kapcsolatot ragadna meg (**túlillesztés**).

A tanítás során a bias hiba csökken (mivel a modell megtanulja közelíteni az adatokat), és a variance hiba nő. Fontos megállítani a tanítást - akár manuálisan (amikor túlillesztést észlelünk), akár automatikusan (regularizáció bevezetésével) - a túlillesztés megelőzése érdekében.

## Következtetés

Ebben a leckében megtanulta a különbségeket a két legnépszerűbb AI keretrendszer, a TensorFlow és a PyTorch különféle API-jai között. Ezenkívül megismerkedett egy nagyon fontos témával, a túlillesztéssel.

## 🚀 Kihívás

A kísérő jegyzetfüzetekben 'feladatokat' talál az alján; dolgozza végig a jegyzetfüzeteket, és végezze el a feladatokat.

## Áttekintés és Önálló Tanulás

Végezzen kutatást a következő témákban:

- TensorFlow
- PyTorch
- Túlillesztés

Tegye fel magának a következő kérdéseket:

- Mi a különbség a TensorFlow és a PyTorch között?
- Mi a különbség a túlillesztés és az alulillesztés között?

## Feladat

Ebben a laborban két osztályozási problémát kell megoldania egy- és több rétegű teljesen összekapcsolt hálózatokkal PyTorch vagy TensorFlow használatával.

**Jogi nyilatkozat**:  
Ezt a dokumentumot a [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével fordítottuk le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.