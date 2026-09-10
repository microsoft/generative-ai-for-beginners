# Bevezetés a kis nyelvi modellekhez a generatív MI kezdőknek
A generatív MI az AI egy lenyűgöző területe, amely olyan rendszerek létrehozására összpontosít, amelyek képesek új tartalmak generálására. Ezek a tartalmak a szövegtől és képektől a zenén át egészen teljes virtuális környezetekig terjedhetnek. A generatív MI egyik legizgalmasabb alkalmazása a nyelvi modellek területén található.

## Mik azok a kis nyelvi modellek?

Egy kis nyelvi modell (SLM) a nagy nyelvi modellek (LLM-ek) lecsökkentett változatát jelenti, amely számos LLM építészeti elvét és technikáját használja fel, miközben jelentősen csökkentett számítási lábnyommal rendelkezik.

Az SLM-ek olyan nyelvi modellek alosztálya, amelyek emberihez hasonló szöveg generálására lettek tervezve. A nagyobb társaikkal, például a GPT-4-gyel ellentétben az SLM-ek kompaktabbak és hatékonyabbak, ami ideálissá teszi őket olyan alkalmazásokhoz, ahol a számítási erőforrások korlátozottak. Méretük ellenére még mindig képesek számos feladat ellátására. Az SLM-eket általában úgy alakítják ki, hogy kompresszióval vagy desztillációval csökkentik az LLM-eket, az eredeti modell funkcióinak és nyelvi képességeinek jelentős részét megtartva. Ez a méretcsökkenés csökkenti az összetettséget, így az SLM-ek hatékonyabbak a memóriában és a számítási igényben egyaránt. Ezekkel az optimalizációkkal az SLM-ek még mindig széles körű természetes nyelvfeldolgozási (NLP) feladatokat képesek ellátni:

- Szöveg generálás: összefüggő és kontextusban releváns mondatok vagy bekezdések létrehozása.
- Szöveg kiegészítés: adatok alapján mondatok előrejelzése és befejezése.
- Fordítás: szövegek átalakítása egyik nyelvről a másikra.
- Összefoglalás: hosszú szövegek rövidebb, könnyebben fogyasztható összefoglalóvá tömörítése.

Habár bizonyos kompromisszumokat hordozhatnak a teljesítmény vagy a mélyebb megértés terén nagyobb társaikhoz képest.

## Hogyan működnek a kis nyelvi modellek?
Az SLM-eket hatalmas mennyiségű szöveges adaton tanítják. A tanulási folyamat során megtanulják a nyelv mintázatait és szerkezetét, ami lehetővé teszi, hogy olyan szöveget generáljanak, ami nyelvtanilag helyes és kontextusban megfelelő. A tanítási folyamat a következőket foglalja magában:

- Adatgyűjtés: nagy méretű szöveges adatforrások összegyűjtése.
- Előfeldolgozás: az adatok tisztítása és rendszerezése a tanításhoz való alkalmassá tétele érdekében.
- Tanítás: gépi tanulási algoritmusok használata a modell szövegértési és generálási képességeinek fejlesztésére.
- Finomhangolás: a modell teljesítményének javítása specifikus feladatokhoz.

Az SLM-ek fejlesztése összhangban áll a növekvő igénnyel az olyan modellek iránt, amelyeket erőforrásszegény környezetekben is lehet használni, például mobil eszközökön vagy peremszámítási platformokon, ahol a teljes méretű LLM-ek túlzottan erőforrás-igényesek lehetnek. A hatékonyságra való összpontosítás révén az SLM-ek egyensúlyt teremtenek a teljesítmény és az elérhetőség között, lehetővé téve széleskörű alkalmazásukat különféle területeken.

![slm](../../../translated_images/hu/slm.4058842744d0444a.webp)

## Tanulási célok

Ebben az órában az SLM-ek ismeretét kívánjuk bemutatni, és azt a Microsoft Phi-3-mal ötvözve különféle szövegtartalom-, látás- és MoE-szcenáriókat tanulni.

Az óra végére a következő kérdésekre kell tudnod válaszolni:

- Mi az az SLM?
- Mi a különbség az SLM és az LLM között?
- Mi az a Microsoft Phi-3/3.5 család?
- Hogyan kell futtatni a következtetést a Microsoft Phi-3/3.5 családdal?

Készen állsz? Kezdjük el.

## Különbségek a nagy nyelvi modellek (LLM-ek) és a kis nyelvi modellek (SLM-ek) között

Az LLM-ek és az SLM-ek egyaránt a valószínűségi gépi tanulás alapelvein nyugszanak, hasonló megközelítéseket követve építészeti kialakításukban, tanítási módszereikben, adatgenerálásban és értékelésben. Ugyanakkor több kulcsfontosságú tényező különbözteti meg ezt a két modelltípust.

## A kis nyelvi modellek alkalmazási területei

Az SLM-ek számos területen alkalmazhatók, például:

- Csevegőbotok: ügyféltámogatás nyújtása és felhasználókkal való párbeszéd.
- Tartalomkészítés: írók segítése ötletek generálásában vagy akár teljes cikkek megírásában.
- Oktatás: diákok segítése írásfeladatokban vagy új nyelvek tanulásában.
- Akadálymentesítés: eszközök készítése fogyatékkal élők számára, például szövegfelolvasó rendszerek.

**Méret**
  
Az LLM-ek és az SLM-ek közötti legfőbb különbség a modellek méretében rejlik. Az LLM-ek, mint például a ChatGPT (GPT-4), becslések szerint 1,76 billió paramétert tartalmazhatnak, míg az olyan nyílt forráskódú SLM-ek, mint a Mistral 7B, jóval kevesebb paraméterrel készülnek — körülbelül 7 milliárddal. Ez a különbség elsősorban a modellarchitektúra és a tanítási folyamatok eltéréseiből adódik. Például a ChatGPT egy önfigyelő mechanizmust alkalmaz egy kódoló-dekódoló keretrendszeren belül, míg a Mistral 7B csúszóablakos figyelmet használ, ami lehetővé teszi hatékonyabb tanítást egy csak dekóderes modellben. Ez az építészeti különbség mélyreható hatással van a modellek összetettségére és teljesítményére.

**Megértés**

Az SLM-ek általában specifikus területekre optimalizáltak, így nagyon specializáltak, de korlátozottabbak lehetnek a széles kontextuális megértés terén több tudományterület között. Ezzel szemben az LLM-ek célja, hogy emberihez hasonló intelligenciát szimuláljanak átfogóbb szinten. Nagy, változatos adatbázisokon tanítva, az LLM-ek jól teljesítenek számos területen, nagyobb sokoldalúságot és alkalmazkodóképességet kínálva. Ennek megfelelően az LLM-ek alkalmasabbak számos alapszintű feladatra, mint például a természetes nyelvfeldolgozás vagy programozás.

**Számítási igény**

Az LLM-ek tanítása és alkalmazása erőforrás-igényes folyamat, gyakran nagy számítási infrastruktúrát követelve, például nagyméretű GPU klasztereket. Például egy ChatGPT-hez hasonló modell nulláról történő betanítása több ezer GPU-t igényelhet hosszú időn keresztül. Ezzel szemben az SLM-ek kisebb paraméterszámuk miatt számítási szempontból elérhetőbbek. Olyan modelleket, mint a Mistral 7B, helyben is ki lehet tanítani és futtatni mérsékelt GPU kapacitással rendelkező gépeken, bár a tanítás néhány órát igényel több GPU kombinációjával.

**Elfogultság**

Az elfogultság ismert probléma az LLM-ek esetén, főként az edzési adatok természetéből adódóan. Ezek a modellek gyakran az internet nyers, nyílt adataira támaszkodnak, amelyek egyes csoportokat alul- vagy félreábrázolhatnak, hibásan címkézhetnek, illetve a nyelvi elfogultságokat is tükrözhetnek, melyeket a dialektusok, földrajzi eltérések és nyelvtani szabályok is befolyásolnak. Ezen túlmenően az LLM architektúrák összetettsége véletlenül felerősítheti az elfogultságot, amit gondos finomhangolás nélkül nem mindig észlelnek. Ezzel szemben az SLM-ek, amelyek korlátozottabb, specifikusabb adatbázisokon tanulnak, kevésbé hajlamosak az ilyen elfogultságokra, bár nem teljesen mentesek tőlük.

**Következtetés**

Az SLM-ek kisebb mérete jelentős előnyt jelent a következtetés sebessége terén, lehetővé téve, hogy hatékonyan generáljanak kimeneteket helyi hardveren, anélkül, hogy kiterjedt párhuzamos számítást igényelnének. Ezzel szemben az LLM-ek mérete és összetettsége miatt gyakran nagymértékű párhuzamos számítási erőforrást igényelnek elfogadható következtetési idő eléréséhez. Több egyidejű felhasználó jelenléte tovább lassítja az LLM-ek válaszidejét, különösen nagy méretű telepítés esetén.

Összefoglalva, bár az LLM-ek és az SLM-ek azonos alapokra, a gépi tanulásra épülnek, jelentősen különböznek a modell méretében, erőforrás-igényben, kontextuális megértésben, elfogultságra való hajlamukban és a következtetési sebességben. Ezek a különbségek tükrözik, hogy mely területeken a legalkalmasabbak: az LLM-ek sokoldalúbbak, de erőforrás-igényesek, míg az SLM-ek kizárólagosabb hatékonyságot kínálnak csökkentett számítási követelmények mellett.

***Megjegyzés: Ebben az órában a Microsoft Phi-3 / 3.5 példáján keresztül mutatjuk be az SLM-eket.***

## Bemutatjuk a Phi-3 / Phi-3.5 családot

A Phi-3 / 3.5 család elsősorban szöveg-, látás- és Agent (MoE) alkalmazási forgatókönyveket céloz meg:

### Phi-3 / 3.5 Instruct

Elsősorban szöveg generálásra, chat befejezésre és tartalmi információk kinyerésére, stb.

**Phi-3-mini**

A 3,8 milliárd paraméteres nyelvi modell elérhető a Microsoft Foundry-n, a Hugging Face-en és az Ollama-n. A Phi-3 modellek lényegesen felülmúlják az azonos vagy nagyobb méretű nyelvi modelleket a kulcsfontosságú benchmarkokon (a benchmark számokat lásd lentebb, a magasabb szám jobb). A Phi-3-mini jobb eredményeket ér el kétszer akkora méretű modelleknél is, míg a Phi-3-small és Phi-3-medium nagyobb modelleket, így a GPT-3.5-öt is felülmúlja.

**Phi-3-small & medium**

A Phi-3-small, amely mindössze 7 milliárd paraméterrel rendelkezik, számos nyelvi, érvelési, kódolási és matematikai benchmarkon jobban teljesít, mint a GPT-3.5T.

A Phi-3-medium 14 milliárd paraméterrel folytatja ezt a tendenciát, és felülmúlja a Gemini 1.0 Pro-t.

**Phi-3.5-mini**

Ezt tekinthetjük a Phi-3-mini frissítésének. A paraméterek változatlanok maradnak, de javul a többnyelvű támogatás (több mint 20 nyelvet támogat: arab, kínai, cseh, dán, holland, angol, finn, francia, német, héber, magyar, olasz, japán, koreai, norvég, lengyel, portugál, orosz, spanyol, svéd, thai, török, ukrán) és erősebb támogatás kerül a hosszú kontextushoz.

A Phi-3.5-mini 3,8 milliárd paraméterrel felülmúlja az azonos méretű nyelvi modelleket, és megegyezik a kétszer akkora modellekkel.

### Phi-3 / 3.5 Vision

A Phi-3/3.5 Instruct modellt tekinthetjük Phi képességének, hogy megértse a világot, a Vision pedig az a "szeme", amely lehetővé teszi Phi számára a világ megértését.


**Phi-3-Vision**

A Phi-3-vision csupán 4,2 milliárd paraméterrel folytatja ezt a tendenciát, és jobban teljesít olyan nagyobb modelleknél, mint a Claude-3 Haiku és Gemini 1.0 Pro V általános vizuális érvelési feladatokon, OCR-en, valamint táblázatok és diagramok megértésén.


**Phi-3.5-Vision**

A Phi-3.5-Vision a Phi-3-Vision továbbfejlesztése, amely több kép támogatását is hozzáadja. Úgy gondolhatjuk, mint a látás fejlesztését: nemcsak képeket, hanem videókat is képes látni.

A Phi-3.5-vision olyan nagyobb modelleket is meghalad, mint a Claude-3.5 Sonnet és a Gemini 1.5 Flash az OCR, táblázat- és diagrammegértési feladatokban, és hasonló szinten áll általános vizuális tudás érvelési feladatokban. Több képkockás bemenetet támogat, vagyis több bemeneti képen is képes érvelni.


### Phi-3.5-MoE

***Szakértői keverék (Mixture of Experts, MoE)*** lehetővé teszi, hogy a modelleket lényegesen kevesebb számítással előtanítsák, ami azt jelenti, hogy drasztikusan skálázható a modell vagy adatbázis mérete ugyanazzal a számítási költséggel, mint egy sűrű modell esetén. Különösen a MoE modell gyorsabban éri el a sűrű társa minőségi szintjét az előtanítás során.

A Phi-3.5-MoE 16 x 3,8 milliárd paraméteres szakértői modult tartalmaz. A Phi-3.5-MoE mindössze 6,6 milliárd aktív paraméterrel hasonló szinten ér el érvelést, nyelvi megértést és matematikai tudást, mint sokkal nagyobb modellek.

A Phi-3/3.5 család modelljei különböző szcenáriókban használhatók. Az LLM-től eltérően a Phi-3/3.5-mini vagy Phi-3/3.5-Vision telepíthető perem eszközökre is.


## Hogyan használjuk a Phi-3/3.5 család modelleket

Reméljük, hogy a Phi-3/3.5 különböző szcenáriókban fog működni. A következőkben különféle szituációkra alapozva fogjuk használni a Phi-3/3.5-öt.

![phi3](../../../translated_images/hu/phi3.655208c3186ae381.webp)

### Következtetés felhő API-kon keresztül

**Microsoft Foundry modellek**

> **Megjegyzés:** A GitHub modellek 2026 júliusának végén kivezetésre kerülnek. A [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) azonnali helyettesítést nyújt.

A Microsoft Foundry Models a legközvetlenebb mód. Gyorsan hozzáférhetsz a Phi-3/3.5-Instruct modellhez a Foundry modell katalógusán keresztül. Az Azure AI Inference SDK / OpenAI SDK kombinációjával az API elérése kód által is megoldható a Phi-3/3.5-Instruct hívás elvégzéséhez. A Playground-on különféle hatásokat is tesztelhetsz.

- Demó: Phi-3-mini és Phi-3.5-mini hatásainak összehasonlítása kínai nyelvi forgatókönyvekben

![phi3](../../../translated_images/hu/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/hu/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ha a látás és a MoE modelleket szeretnénk használni, a Microsoft Foundry segítségével is végezhetjük a hívást. Érdeklődés esetén elolvashatod a Phi-3 Cookbook-ot, hogy megtanuld, hogyan hívhatod a Phi-3/3.5 Instruct, Vision, MoE modelleket a Microsoft Foundry-n keresztül [Kattints ide](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

A felhőalapú Microsoft Foundry Models katalógus mellett a [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) szolgáltatást is igénybe veheted a kapcsolódó hívásokhoz. Az NVIDIA NIM (NVIDIA Inference Microservices) egy gyorsított következtetési mikroszolgáltatás-csomag, amely hatékony AI modell telepítést tesz lehetővé különböző környezetekben, beleértve felhőket, adatközpontokat és munkaállomásokat.

Íme néhány kulcsfontosságú jellemzője az NVIDIA NIM-nek:

- **Egyszerű telepítés:** Az NIM lehetővé teszi az AI modellek egy parancsos telepítését, így könnyen integrálható meglévő munkafolyamatokba.

- **Optimalizált teljesítmény:** kihasználja az NVIDIA előre optimalizált inferencia motorjait, mint például a TensorRT és TensorRT-LLM, hogy alacsony késleltetést és nagy áteresztőképességet biztosítson.
- **Skálázhatóság:** a NIM támogatja az automatikus skálázódást Kubernetes-en, így hatékonyan kezeli a változó munkaterheléseket.
- **Biztonság és irányítás:** a szervezetek megőrizhetik az adataik és alkalmazásaik feletti irányítást azzal, hogy saját általuk kezelt infrastruktúrán önállóan telepítik a NIM mikroszolgáltatásokat.
- **IPARÁGI SZABVÁNYOKNAK MEGFELELŐ API-K:** a NIM iparági szabványos API-kat biztosít, megkönnyítve az AI alkalmazások, például chatbotok, AI asszisztensek és más fejlesztését és integrálását.

A NIM az NVIDIA AI Enterprise része, melynek célja az AI modellek telepítésének és működtetésének egyszerűsítése, biztosítva, hogy azok hatékonyan fussanak NVIDIA GPU-kon.

- Bemutató: NVIDIA NIM használata a Phi-3.5-Vision-API hívására [[Kattints ide](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 helyi futtatása
Az inferencia a Phi-3-mal vagy bármely más, például GPT-3 típusú nyelvi modellel kapcsolatban a válaszok vagy előrejelzések generálását jelenti a bemenet alapján. Amikor egy kérést vagy kérdést ad meg a Phi-3 számára, az a betanított neurális hálózatával elemzi az adatok mintázatait és összefüggéseit, és meghatározza a legvalószínűbb és legmegfelelőbb választ.

**Hugging Face Transformer**
A Hugging Face Transformers egy erőteljes könyvtár természetes nyelvfeldolgozáshoz (NLP) és más gépi tanulási feladatokhoz. Íme néhány fontos pont róla:

1. **Előre betanított modellek**: Több ezer előre betanított modellt kínál, melyek különféle feladatokra használhatók, mint például szöveg osztályozás, név szerinti entitás felismerés, kérdés-válasz, összefoglalás, fordítás és szöveg generálás.

2. **Keretrendszer interoperabilitás:** Támogat több mélytanulási keretrendszert, köztük a PyTorch-ot, TensorFlow-t és JAX-et, lehetővé téve egy modell egyik keretrendszerben való betanítását és másikban való használatát.

3. **Multimodális képességek:** Az NLP mellett támogat számítógépes látási feladatokat (például képosztályozás, objektumfelismerés) és hangfeldolgozást (például beszédfelismerés, hangosztályozás).

4. **Könnyű használat:** API-kat és eszközöket kínál a modellek egyszerű letöltéséhez és finomhangolásához, elérhetővé téve kezdők és szakértők számára is.

5. **Közösség és erőforrások:** A Hugging Face élénk közösséggel, bőséges dokumentációval, oktatóanyagokkal és útmutatókkal segíti a felhasználókat a kezdésben és a könyvtár kiaknázásában.
[hivatalos dokumentáció](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) vagy a [GitHub tárhelyük](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ez a leggyakrabban használt módszer, de GPU gyorsítást igényel. Különösen a Vision és MoE esetek sok számítást igényelnek, ami CPU-n nagyon lassú lesz, ha nincsenek kvantáltak.


- Bemutató: Transformer használata Phi-3.5-Instruct hívására [Kattints ide](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Bemutató: Transformer használata Phi-3.5-Vision hívására [Kattints ide](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Bemutató: Transformer használata Phi-3.5-MoE hívására [Kattints ide](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) egy platform, amely megkönnyíti a nagy nyelvi modellek (LLM) helyi futtatását a gépeden. Számos modellt támogat, például Llama 3.1, Phi 3, Mistral és Gemma 2-t, többek között. A platform leegyszerűsíti a folyamatot azáltal, hogy a modell súlyokat, konfigurációt és adatokat egy csomagba rendezi, így könnyebben testreszabható és saját modellek hozhatók létre. Az Ollama elérhető macOS-re, Linuxra és Windows-ra. Kitűnő eszköz, ha LLM-ekkel szeretnél kísérletezni vagy telepíteni őket anélkül, hogy felhőszolgáltatásokra támaszkodnál. Az Ollama a legegyszerűbb mód, csak ki kell adnod a következő parancsot.


```bash

ollama run phi3.5

```

**Foundry Local**

A [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) a Microsoft offline, eszközön futó környezete, amely teljes egészében az ön hardverén futtatja a Phi-hez hasonló modelleket – nincs szükség Azure előfizetésre, API kulcsra vagy hálózati kapcsolatra. Automatikusan kiválasztja a legjobb elérhető végrehajtási szolgáltatót (NPU, GPU vagy CPU), és nyíltai kompatibilis végpontot biztosít, így a meglévő `openai`/Azure AI Inference SDK kód minimális módosítással irányítható erre. A kezdéshez lásd a [Foundry Local dokumentációt](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Vagy használhatod közvetlenül az SDK-t Pythonban:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime a Generatív AI-hoz**

Az [ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) egy többplatformos inferencia és betanítási gépi tanulási gyorsító. Az ONNX Runtime a Generatív AI-hoz (GENAI) egy erőteljes eszköz, amely segít hatékonyan futtatni generatív AI modelleket különböző platformokon.

## Mi az az ONNX Runtime?
Az ONNX Runtime egy nyílt forráskódú projekt, amely nagy teljesítményű inferenciát tesz lehetővé gépi tanulási modellek számára. Támogatja a gépi tanulási modellek ábrázolására szolgáló Open Neural Network Exchange (ONNX) formátumot, amely szabvány a gépi tanulási modellek reprezentálására. Az ONNX Runtime inferencia gyorsabb ügyfélélményt és alacsonyabb költségeket tesz lehetővé, támogatva mélytanulási keretrendszerekből, mint a PyTorch és TensorFlow/Keras, valamint klasszikus gépi tanulási könyvtárakból, például scikit-learn, LightGBM, XGBoost stb. származó modelleket. Az ONNX Runtime kompatibilis különböző hardverekkel, driverekkel és operációs rendszerekkel, és optimális teljesítményt nyújt a hardver gyorsítók kihasználásával, valamint gráf optimalizációkkal és transzformációkkal.

## Mi az a Generatív AI?
A generatív AI olyan mesterséges intelligencia rendszerekre utal, amelyek új tartalmat képesek létrehozni, például szöveget, képeket vagy zenét, a betanított adatok alapján. Példák erre a nyelvi modellek, mint a GPT-3, vagy a képgeneráló modellek, mint a Stable Diffusion. Az ONNX Runtime a GenAI-hoz könyvtár biztosítja az ONNX modellek generatív AI ciklusát, beleértve az ONNX Runtime-os inferenciát, logits feldolgozást, keresést és mintavételezést, valamint a KV cache kezelést.

## ONNX Runtime a GENAI-hoz
Az ONNX Runtime a GENAI-hoz kiterjeszti az ONNX Runtime képességeit a generatív AI modellek támogatására. Néhány kulcsfontosságú jellemzője:

- **Széles körű platform támogatás:** működik több platformon, beleértve a Windows, Linux, macOS, Android és iOS rendszereket.
- **Modelltámogatás:** számos népszerű generatív AI modellt támogat, mint például a LLaMA, GPT-Neo, BLOOM és még sok más.
- **Teljesítmény-optimalizálás:** tartalmaz optimalizációkat különböző hardvergyorsítók, például NVIDIA GPU-k, AMD GPU-k és mások számára.
- **Könnyű használat:** API-kat kínál az alkalmazásokba való egyszerű integrációhoz, lehetővé téve szöveg, képek és egyéb tartalom generálását minimális kód mellett.
- A felhasználók hívhatják a magas szintű generate() metódust, vagy futtathatják a modell egyes iterációit ciklusban, egy token generálásával egyszerre, és opcionálisan frissíthetik a generálási paramétereket a cikluson belül.
- Az ONNX runtime támogatja a greedy/beam keresést és a TopP, TopK mintavételezést token sorozatok generálásához, valamint beépített logits feldolgozást, például ismétlődési büntetéseket. Egyéni pontozás is könnyen hozzáadható.

## Kezdés
Az ONNX Runtime a GENAI-hoz használatának megkezdéséhez kövesd az alábbi lépéseket:

### ONNX Runtime telepítése:
```Python
pip install onnxruntime
```
### A Generatív AI kiterjesztések telepítése:
```Python
pip install onnxruntime-genai
```

### Modell futtatása: Íme egy egyszerű példa Pythonban:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Bemutató: ONNX Runtime GenAI használata Phi-3.5-Vision hívására


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Egyebek**

Az ONNX Runtime, Ollama és Foundry Local referencia módszerein túlmenően a különböző gyártók által biztosított modell referencia módszerek alapján kvantitatív modellek is elkészíthetők. Például Apple MLX keretrendszer az Apple Metal-lel, Qualcomm QNN NPU-val, Intel OpenVINO CPU/GPU-val stb. További tartalmakat a [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) oldalon találhatsz.


## Továbbiak

Megtanultuk a Phi-3/3.5 család alapjait, de hogy többet tudjunk meg az SLM-ről, több ismeretre van szükség. A válaszokat megtalálod a Phi-3 Cookbookban. Ha többet szeretnél megtudni, kérlek látogasd meg a [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) oldalt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->