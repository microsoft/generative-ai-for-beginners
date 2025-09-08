<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:36:07+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "hu"
}
-->
# Neurális Hálózat Keretrendszerek

Ahogy már megtanultuk, a neurális hálózatok hatékony tanításához két dolgot kell tudnunk:

* Műveleteket végezni tenzorokon, például szorzás, összeadás, illetve olyan függvények kiszámítása, mint a sigmoid vagy softmax
* Kiszámítani az összes kifejezés gradiensét, hogy elvégezhessük a gradiens csökkenéses optimalizációt

Míg a `numpy` könyvtár az első részhez elegendő, szükségünk van egy mechanizmusra a gradiensszámításhoz. A korábbi szakaszban fejlesztett keretrendszerünkben manuálisan kellett megírnunk az összes derivált függvényt a `backward` metódusban, amely a visszaterjesztést végzi. Ideális esetben egy keretrendszer lehetőséget kell adjon bármilyen általunk definiált kifejezés gradiensének kiszámítására.

Egy másik fontos szempont, hogy képesek legyünk számításokat végezni GPU-n vagy más speciális számítóegységeken, például TPU-n. A mély neurális hálózatok tanítása *rengeteg* számítást igényel, és nagyon fontos, hogy ezeket a számításokat párhuzamosítani tudjuk GPU-kon.

> ✅ A 'párhuzamosítás' azt jelenti, hogy a számításokat több eszköz között osztjuk meg.

Jelenleg a két legnépszerűbb neurális keretrendszer a TensorFlow és a PyTorch. Mindkettő alacsony szintű API-t biztosít tenzorok kezelésére CPU-n és GPU-n egyaránt. Az alacsony szintű API fölött magasabb szintű API is elérhető, ezek a Keras és a PyTorch Lightning.

Alacsony szintű API | TensorFlow | PyTorch
-------------------|------------|---------
Magas szintű API   | Keras      | PyTorch

**Az alacsony szintű API-k** mindkét keretrendszerben lehetővé teszik úgynevezett **számítási gráfok** építését. Ez a gráf meghatározza, hogyan számoljuk ki a kimenetet (általában a veszteségfüggvényt) adott bemeneti paraméterekkel, és ha elérhető, GPU-n is futtatható. Vannak függvények, amelyek képesek differenciálni ezt a számítási gráfot és kiszámítani a gradienseket, amelyeket aztán a modellparaméterek optimalizálására használhatunk.

**A magas szintű API-k** a neurális hálózatokat jellemzően **rétegek sorozataként** kezelik, és megkönnyítik a legtöbb hálózat felépítését. A modell tanítása általában az adatok előkészítését, majd a `fit` függvény meghívását jelenti.

A magas szintű API lehetővé teszi, hogy tipikus neurális hálózatokat nagyon gyorsan építsünk anélkül, hogy sok részlettel kellene foglalkoznunk. Ugyanakkor az alacsony szintű API sokkal nagyobb kontrollt ad a tanítási folyamat felett, ezért kutatásokban gyakran használják, amikor új neurális hálózati architektúrákkal dolgozunk.

Fontos megérteni, hogy mindkét API-t együtt is használhatjuk, például saját hálózati rétegarchitektúrát fejleszthetünk alacsony szintű API-val, majd ezt beilleszthetjük egy nagyobb, magas szintű API-val épített és tanított hálózatba. Vagy definiálhatunk egy hálózatot magas szintű API-val rétegek sorozataként, majd saját alacsony szintű tanítási ciklust használhatunk az optimalizációhoz. Mindkét API ugyanazokon az alapelveken nyugszik, és úgy tervezték, hogy jól működjenek együtt.

## Tanulás

Ebben a tanfolyamban a tartalom nagy részét mind PyTorch, mind TensorFlow esetén kínáljuk. Választhatod a neked tetsző keretrendszert, és csak a hozzá tartozó jegyzeteket nézheted át. Ha nem vagy biztos, melyik keretrendszert válaszd, olvass el néhány internetes vitát a **PyTorch vs. TensorFlow** témában. Érdemes mindkettőt megnézni, hogy jobban megértsd őket.

Ahol csak lehet, egyszerűség miatt magas szintű API-kat használunk. Ugyanakkor fontosnak tartjuk, hogy az alapoktól értsd meg a neurális hálózatok működését, ezért az elején alacsony szintű API-val és tenzorokkal dolgozunk. Ha viszont gyorsan szeretnél haladni, és nem akarsz sok időt tölteni ezeknek a részleteknek a tanulásával, átugorhatod ezt, és egyből a magas szintű API-s jegyzetekhez mehetsz.

## ✍️ Gyakorlatok: Keretrendszerek

Folytasd a tanulást a következő jegyzetekben:

Alacsony szintű API | TensorFlow+Keras jegyzet | PyTorch
--------------------|----------------------------|---------
Magas szintű API    | Keras                      | *PyTorch Lightning*

Miután elsajátítottad a keretrendszereket, tekintsük át az overfitting fogalmát.

# Overfitting (Túltanulás)

Az overfitting rendkívül fontos fogalom a gépi tanulásban, és nagyon lényeges, hogy helyesen értsük meg!

Vegyük az alábbi problémát, ahol 5 pontot kell közelítenünk (a grafikonokon `x` jelöli őket):

!linear | overfit
-------------------------|--------------------------
**Lineáris modell, 2 paraméter** | **Nemlineáris modell, 7 paraméter**
Tanulási hiba = 5.3 | Tanulási hiba = 0
Validációs hiba = 5.1 | Validációs hiba = 20

* Bal oldalon egy jó egyenes vonal közelítést látunk. Mivel a paraméterek száma megfelelő, a modell jól megragadja a pontok eloszlásának lényegét.
* Jobb oldalon a modell túl erős. Mivel csak 5 pont van, de a modellnek 7 paramétere, képes úgy igazodni, hogy átmenjen az összes ponton, így a tanulási hiba 0 lesz. Ez azonban megakadályozza, hogy a modell megértse az adatok mögötti helyes mintázatot, ezért a validációs hiba nagyon magas.

Nagyon fontos megtalálni a megfelelő egyensúlyt a modell komplexitása (paraméterek száma) és a tanító minták száma között.

## Miért alakul ki az overfitting?

  * Nem elég tanító adat áll rendelkezésre
  * Túl erős modell
  * Túl sok zaj van a bemeneti adatokban

## Hogyan ismerhető fel az overfitting?

Ahogy a fenti grafikonon is látható, az overfittinget nagyon alacsony tanulási hiba és magas validációs hiba jellemzi. Általában a tanítás során mind a tanulási, mind a validációs hiba csökken, majd egy ponton a validációs hiba megáll a csökkenésben, és elkezd nőni. Ez az overfitting jele, és arra utal, hogy valószínűleg itt kellene leállítani a tanítást (vagy legalább készíteni egy pillanatképet a modellről).

overfitting

## Hogyan előzhető meg az overfitting?

Ha észleled az overfittinget, a következők egyikét teheted:

 * Növeld a tanító adatok mennyiségét
 * Csökkentsd a modell komplexitását
 * Használj valamilyen regularizációs technikát, például Dropout-ot, amit később tárgyalunk

## Overfitting és a Bias-Variance kompromisszum

Az overfitting valójában egy általánosabb statisztikai probléma, az úgynevezett Bias-Variance kompromisszum esete. Ha megnézzük a modell hibáinak lehetséges forrásait, két típust különböztethetünk meg:

* **Bias hibák** abból adódnak, hogy az algoritmus nem képes helyesen megragadni a tanító adatok közötti összefüggést. Ez abból fakadhat, hogy a modell nem elég erős (**alultanulás**).
* **Variance hibák** abból erednek, hogy a modell a bemeneti adatok zaját közelíti, nem pedig a valódi összefüggést (**túltanulás**).

A tanítás során a bias hiba csökken (ahogy a modell megtanulja az adatokat), míg a variance hiba nő. Fontos, hogy a tanítást időben leállítsuk – akár manuálisan (amikor észleljük az overfittinget), akár automatikusan (regularizáció bevezetésével) –, hogy megelőzzük a túlillesztést.

## Összefoglalás

Ebben a leckében megismerted a két legnépszerűbb AI keretrendszer, a TensorFlow és a PyTorch különböző API-jainak különbségeit. Emellett egy nagyon fontos témáról, az overfittingről is tanultál.

## 🚀 Feladat

A mellékelt jegyzetek alján találsz 'feladatokat'; dolgozd végig a jegyzeteket, és oldd meg a feladatokat.

## Áttekintés és önálló tanulás

Kutatásokat végezhetsz a következő témákban:

- TensorFlow
- PyTorch
- Overfitting

Tedd fel magadnak a következő kérdéseket:

- Mi a különbség a TensorFlow és a PyTorch között?
- Mi a különbség az overfitting és az underfitting között?

## Házi feladat

Ebben a laborban két osztályozási problémát kell megoldanod egy- és többrétegű, teljesen összekapcsolt hálózatokkal PyTorch vagy TensorFlow használatával.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.