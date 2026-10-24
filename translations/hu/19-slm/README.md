# Bevezetés a kis nyelvi modellekbe a generatív MI kezdők számára
A generatív MI az a mesterséges intelligencia izgalmas területe, amely olyan rendszerek létrehozására koncentrál, amelyek képesek új tartalmak generálására. Ezek a tartalmak lehetnek szövegek, képek, zene, sőt akár teljes virtuális környezetek is. A generatív MI egyik legizgalmasabb alkalmazása a nyelvi modellek területén található.

## Mik azok a kis nyelvi modellek?

A kis nyelvi modell (SLM) egy nagy nyelvi modell (LLM) kicsinyített változatát jelenti, amely kihasználja a nagy nyelvi modellek számos építészeti elvét és technikáját, ugyanakkor jelentősen csökkentett számítási igénnyel rendelkezik. 

Az SLM-ek a nyelvi modellek egy alcsoportja, amelyek emberhez hasonló szöveget generálnak. Nagyobb társaikkal, például a GPT-4-gyel ellentétben az SLM-ek kompaktabbak és hatékonyabbak, ezért ideálisak olyan alkalmazásokhoz, ahol a számítási erőforrások korlátozottak. Méretük ellenére még mindig képesek különféle feladatok elvégzésére. Az SLM-ek általában úgy jönnek létre, hogy tömörítéssel vagy desztillációval alakítják át az LLM-eket, céljuk az eredeti modell funkcionalitásának és nyelvi képességeinek jelentős részének megtartása. A modell méretének csökkenése csökkenti az összetettséget, így az SLM-ek hatékonyabbak mind memóriahasználat, mind számítási igény szempontjából. Ezek az optimalizációk mellett az SLM-ek különböző természetes nyelvfeldolgozási (NLP) feladatokat is képesek ellátni:

- Szöveggenerálás: összefüggő és kontextusban releváns mondatok vagy bekezdések létrehozása.
- Szöveg kiegészítése: adott bemenet alapján mondatok előrejelzése és kiegészítése.
- Fordítás: szöveg átalakítása egyik nyelvről a másikra.
- Összefoglalás: hosszú szövegek rövidebb, könnyebben emészthető összefoglalóvá tömörítése.

Bár bizonyos teljesítménybeli vagy mélyebb megértésbeli kompromisszumokkal járnak a nagyobb modellekhez képest. 

## Hogyan működnek a kis nyelvi modellek?
Az SLM-ek hatalmas mennyiségű szöveges adatból tanulnak. A tanulás során felismerik a nyelv mintázatait és szerkezeteit, így képesek grammatikailag helyes és kontextushoz illő szövegeket generálni. A tanítási folyamat az alábbi lépésekből áll:

- Adatgyűjtés: nagy szöveges adathalmazok gyűjtése különböző forrásokból.
- Előfeldolgozás: az adatok megtisztítása és rendezése, hogy alkalmasak legyenek a tanításra.
- Tanítás: gépi tanulási algoritmusokkal a modell megtanítása szöveg megértésére és generálására.
- Finomhangolás: a modell teljesítményének javítása specifikus feladatokban.

Az SLM-ek fejlesztése összhangban áll azzal az egyre növekvő igénnyel, hogy olyan modellek legyenek elérhetők, amelyek korlátozott erőforrású környezetekben, például mobil eszközökön vagy él számítási platformokon is futtathatók, ahol a nagy méretű LLM-ek nehezen alkalmazhatók nagymértékű erőforrásigényük miatt. Az SLM-ek hatékonyságra való fókuszálása kiegyensúlyozza a teljesítményt az elérhetőséggel, lehetővé téve szélesebb körű alkalmazásukat különböző területeken.

![slm](../../../translated_images/hu/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Tanulási célok

Ebben a leckében az SLM-ekről szóló ismereteket szeretnénk bemutatni, és a Microsoft Phi-3-mal kombinálva különböző szöveges, látási és MoE-alapú forgatókönyveket tanulni.

A lecke végére képesnek kell lenned válaszolni az alábbi kérdésekre:

- Mi az az SLM?
- Mi a különbség az SLM és az LLM között?
- Mi a Microsoft Phi-3/3.5 család?
- Hogyan lehet futtatni a következtetést a Microsoft Phi-3/3.5 családdal?

Készen állsz? Kezdjünk hozzá.

## Különbségek a nagy nyelvi modellek (LLM) és a kis nyelvi modellek (SLM) között

Mind az LLM-ek, mind az SLM-ek a valószínűségi gépi tanulás alapelveire épülnek, hasonló megközelítéseket követve az építészeti kialakításban, tanítási módszertanban, adatgenerálási folyamatokban és modellértékelésben. Ugyanakkor több kulcsfontosságú tényező megkülönbözteti ezt a két modelltípust.

## A kis nyelvi modellek alkalmazásai

Az SLM-ek számos területen alkalmazhatók, például:

- Csevegőrobotok: ügyfélszolgálat nyújtása és felhasználókkal folytatott párbeszéd.
- Tartalomkészítés: írók segítése ötletekkel vagy teljes cikkek tervezésével.
- Oktatás: diákok támogatása írásbeli feladatokban vagy új nyelvek tanulásában.
- Hozzáférhetőség: eszközök létrehozása fogyatékkal élők számára, például szövegfelolvasó rendszerek.

**Méret**
  
Az LLM-ek és az SLM-ek egyik fő különbsége a modellek méretében rejlik. Az LLM-ek, mint például a ChatGPT (GPT-4), becslések szerint akár 1,76 billió paramétert is tartalmazhatnak, míg az open-source SLM-ek, mint a Mistral 7B, jelentősen kevesebb paraméterrel készülnek, körülbelül 7 milliárddal. Ez a különbség elsősorban az architektúra és a tanítási folyamatok eltéréseiből fakad. Például a ChatGPT önfigyelő mechanizmust használ egy kódoló-dekódoló keretrendszerben, míg a Mistral 7B csúszóablakos figyelmet alkalmaz, amely hatékonyabb tanítást tesz lehetővé egy kizárólag dekódoló modellben. Ez az architekturális eltérés mélyreható hatással van a modellek összetettségére és teljesítményére.

**Megértés**

Az SLM-eket általában adott szakterületeken való teljesítményre optimalizálják, ezért nagyon specializáltak, de korlátozottabbak lehetnek a széleskörű kontextusértés terén több tudományág átívelésében. Ezzel szemben az LLM-ek célja, hogy emberi intelligenciához hasonló szintet szimuláljanak átfogóbb módon. Hatalmas, változatos adatbázisokon tanítva, az LLM-ek több területen is jól teljesítenek, nagyobb sokoldalúságot és alkalmazkodóképességet kínálva. Következésképpen az LLM-ek alkalmasabbak szélesebb körű alárendelt feladatokra, mint például a természetes nyelvfeldolgozás és programozás.

**Számítási igény**

Az LLM-ek tanítása és működtetése erőforrás-igényes folyamat, amely gyakran jelentős számítási infrastruktúrát, például nagyszabású GPU klasztereket igényel. Például egy ChatGPT modell nulláról történő tanítása akár több ezer GPU-t is megkövetelhet hosszabb időszakon keresztül. Ezzel szemben az SLM-ek, kisebb paraméterszámuk miatt, számítási erőforrások tekintetében hozzáférhetőbbek. Olyan modelleket, mint a Mistral 7B, helyi gépeken, mérsékelt GPU képességekkel is lehet tanítani és futtatni, bár a tanítás több órát igényel több GPU-n.

**Elfogultság**

Az elfogultság ismert probléma az LLM-eknél, elsősorban a tanító adatok jellege miatt. Ezek a modellek gyakran nyers, nyíltan elérhető internetes adatokra támaszkodnak, amelyek alulreprezentálhatnak vagy tévesen ábrázolhatnak bizonyos csoportokat, hibás címkézést tartalmazhatnak, vagy nyelvi elfogultságokat tükrözhetnek, amelyeket a dialektus, földrajzi eltérések és nyelvtani szabályok befolyásolnak. Ezen túlmenően az LLM-ek összetett architektúrája véletlenül fokozhatja az elfogultságot, amely finomhangolás nélkül észrevétlen maradhat. Másrészt az SLM-ek, amelyek szűkebb, adott szakterületre szabott adatokon tanulnak, kevésbé hajlamosak ilyen elfogultságokra, bár nem teljesen mentesek tőlük.

**Következtetés**

Az SLM-ek kisebb mérete jelentős előnyt jelent a következtetés sebessége tekintetében, lehetővé téve számukra, hogy helyi hardveren hatékonyan generáljanak kimeneteket kiterjedt párhuzamos feldolgozás szükségessége nélkül. Ezzel szemben az LLM-ek nagyságuk és összetettségük miatt gyakran jelentős párhuzamos számítási erőforrásokat igényelnek elfogadható következtetési idők eléréséhez. Több egyidejű felhasználó jelenléte tovább lassítja az LLM-ek válaszidejét, különösen nagyszabású üzemeltetés esetén.

Összefoglalva, bár mind az LLM-ek, mind az SLM-ek gépi tanulási alapokon nyugszanak, jelentős különbségek vannak a modellméret, az erőforrásigény, a kontextuális megértés, az elfogultságra való hajlam és a következtetési sebesség tekintetében. Ezek a különbségek tükrözik alkalmazhatóságukat különböző esetekre, az LLM-ek sokoldalúbbak, de erőforrás-igényesebbek, míg az SLM-ek szűkebb területen nyújtanak hatékonyabb működést alacsonyabb számítási igénnyel.

***Megjegyzés: Ebben a leckében az SLM-et a Microsoft Phi-3 / 3.5 példáján keresztül mutatjuk be.***

## A Phi-3 / Phi-3.5 család bemutatása

A Phi-3 / 3.5 család elsősorban szöveg, látás és ügynök (MoE) alkalmazási forgatókönyvekre fókuszál:

### Phi-3 / 3.5 Instruct

Főként szöveggenerálásra, csevegés befejezésére és tartalminformáció-kivonásra, stb.

**Phi-3-mini**

A 3,8 milliárd paraméteres nyelvi modell elérhető a Microsoft Foundry, Hugging Face és Ollama platformokon. A Phi-3 modellek jelentősen felülmúlják az azonos vagy nagyobb méretű nyelvi modelleket kulcsfontosságú benchmarkokon (lásd alább a benchmark számokat, a magasabb szám jobb). A Phi-3-mini kétszer akkora méretű modelleknél is jobb teljesítményt nyújt, míg a Phi-3-small és Phi-3-medium nagyobb modelleket is túlszárnyal, többek között a GPT-3.5-öt.

**Phi-3-small & medium**

Mindössze 7 milliárd paraméterrel a Phi-3-small számos nyelvi, érvelési, kódolási és matematikai benchmarkon jobban teljesít, mint a GPT-3.5T.

A Phi-3-medium, 14 milliárd paraméterrel, folytatja ezt a trendet, és felülmúlja a Gemini 1.0 Pro modellt.

**Phi-3.5-mini**

Ezt tekinthetjük a Phi-3-mini fejlesztett változatának. Bár a paraméterek száma változatlan marad, javul a többnyelvű támogatás képessége (több mint 20 nyelvet támogat: arab, kínai, cseh, dán, holland, angol, finn, francia, német, héber, magyar, olasz, japán, koreai, norvég, lengyel, portugál, orosz, spanyol, svéd, thai, török, ukrán), továbbá erősebb támogatást ad a hosszú kontextushoz.

A Phi-3.5-mini 3,8 milliárd paraméterrel felülmúlja az azonos méretű nyelvi modelleket, és egy szinten van a kétszer akkora méretű modellekkel.

### Phi-3 / 3.5 Vision

A Phi-3/3.5 Instruct modellt úgy képzelhetjük el, mint Phi képességét a megértésre, a Vision pedig az, ami Phi-nak "szemeket" ad a világ megértéséhez.


**Phi-3-Vision**

A Phi-3-vision, mindössze 4,2 milliárd paraméterrel, folytatja ezt a trendet, és felülmúlja a nagyobb modelleket, mint a Claude-3 Haiku és a Gemini 1.0 Pro V általános vizuális érvelési, OCR, táblázat- és diagramértelmezési feladatokon.


**Phi-3.5-Vision**

A Phi-3.5-Vision szintén a Phi-3-Vision továbbfejlesztése, többszörös képtámogatással bővítve. Ezt úgy is elképzelhetjük, mint fejlesztést a látásban; nem csak képeket, hanem videókat is "lát".

A Phi-3.5-vision jobban teljesít olyan nagyobb modelleknél, mint a Claude-3.5 Sonnet és Gemini 1.5 Flash OCR, táblázat és diagram értelmezési feladatokban, és hasonló szinten van az általános vizuális tudás érvelési feladataiban. Több képkockás bemenetet támogat, vagyis több képen végzett érvelést végez.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** lehetővé teszi, hogy a modelleket sokkal kevesebb számítással elő legyenek tanítva, ami azt jelenti, hogy ugyanazzal a számítási büdzsével drámaian növelhető a modell vagy az adatkészlet mérete egy sűrű modellhez képest. Különösen, egy MoE modell előtanítási fázisban sokkal gyorsabban érhet el ugyanolyan minőséget, mint a sűrű megfelelője.

A Phi-3.5-MoE 16x3,8 milliárd paraméteres szakértői modulból áll. A Phi-3.5-MoE, amelynek aktív paramétereinek száma csak 6,6 milliárd, hasonló szintű érvelést, nyelvi megértést és matematikai képességeket tud nyújtani, mint sokkal nagyobb modellek.

A Phi-3/3.5 család modelljei különböző forgatókönyvek alapján használhatók. Az LLM-ekkel ellentétben a Phi-3/3.5-mini vagy Phi-3/3.5-Vision telepíthető él eszközökön is.


## Hogyan használjuk a Phi-3/3.5 család modelleket

Azt reméljük, hogy a Phi-3/3.5-öt különféle forgatókönyvekben használjuk. Ezután különböző helyzetek alapján fogjuk használni a Phi-3/3.5-öt.

![phi3](../../../translated_images/hu/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Következtetés felhőalapú API-kon keresztül

**Microsoft Foundry Modellek**

> **Megjegyzés:** A GitHub Modellek 2026 júliusának végén megszűnnek. A közvetlen helyettesítő a [Microsoft Foundry Modellek](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

A Microsoft Foundry Modellek a legközvetlenebb mód. Gyorsan elérheted a Phi-3/3.5-Instruct modellt a Foundry modellkatalógus segítségével. Az Azure AI Inference SDK / OpenAI SDK-val kombinálva kódból érheted el az API-t, és végezheted el a Phi-3/3.5-Instruct hívást. Különböző hatásokat is kipróbálhatsz a Playground-ban.

- Demó: A Phi-3-mini és Phi-3.5-mini hatásainak összehasonlítása kínai forgatókönyvekben

![phi3](../../../translated_images/hu/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/hu/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Vagy, ha a látási és MoE modelleket szeretnénk használni, a Microsoft Foundry segítségével tudjuk a hívást elvégezni. Érdeklődés esetén olvasd el a Phi-3 Cookbook-ot, hogy megtanuld, hogyan kell Phi-3/3.5 Instruct, Vision, MoE hívásokat végrehajtani Microsoft Foundry-n keresztül [Kattints ide](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

A felhőalapú Microsoft Foundry Modellek katalógus mellett a [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) használatával is végrehajthatod a kapcsolódó hívásokat. Látogasd meg az NVIDIA NIM-et, hogy végrehajtsd a Phi-3/3.5 család API hívásait. Az NVIDIA NIM (NVIDIA Inference Microservices) egy felgyorsított következtetési mikroszolgáltatások gyűjteménye, amelynek célja, hogy segítsen a fejlesztőknek hatékonyan telepíteni MI modelleket különféle környezetekben — beleértve a felhőket, adatközpontokat és munkaállomásokat.

Néhány kulcsfontosságú jellemzője az NVIDIA NIM-nek:

- **Egyszerű telepítés:** Az NIM lehetővé teszi az MI modellek egy parancssal való telepítését, így könnyű beilleszteni a meglévő munkafolyamatokba.
- **Optimalizált teljesítmény:** Használja az NVIDIA előre optimalizált következtetési motorjait, például a TensorRT-t és a TensorRT-LLM-et az alacsony késleltetés és magas áteresztőképesség biztosítására.
- **Skálázhatóság:** Az NIM támogatja a Kubernetes automatikus skálázást, így hatékonyan kezelhető a változó munkaterhelés.
- **Biztonság és irányítás:** A szervezetek maguk kezelhetik adataikat és alkalmazásaikat azzal, hogy az NIM mikroszolgáltatásokat saját felügyelt infrastruktúrájukon futtatják.
- **Szabványos API-k:** A NIM ipari szabványos API-kat biztosít, amelyek megkönnyítik az olyan AI-alkalmazások, mint például chatbotok, AI-asszisztensek és mások fejlesztését és integrálását.

A NIM az NVIDIA AI Enterprise része, amelynek célja az AI modellek telepítésének és üzemeltetésének egyszerűsítése, biztosítva, hogy azok hatékonyan fussanak NVIDIA GPU-kon.

- Demo: NVIDIA NIM használata Phi-3.5-Vision-API hívásához [[Kattintson erre a linkre](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 helyi futtatása
Az inferencia a Phi-3-mal vagy bármilyen nyelvi modellel, mint például a GPT-3, arra a folyamatra utal, amikor a modell az adott bemenet alapján válaszokat vagy előrejelzéseket generál. Amikor egy promptot vagy kérdést adunk a Phi-3-nak, az a betanított neurális hálózatát használja, hogy a tanult adatok mintázatait és összefüggéseit elemezve a legvalószínűbb és legrelevánsabb választ generálja.

**Hugging Face Transformer**
A Hugging Face Transformers egy erőteljes könyvtár, amely természetes nyelvfeldolgozásra (NLP) és más gépi tanulási feladatokra készült. Íme néhány fontos pont róla:

1. **Előre betanított modellek**: Több ezer előre betanított modell érhető el, amelyek különféle feladatokra használhatók, például szöveg osztályozásra, névazonosító entitás felismerésre, kérdés-válaszolásra, összefoglalásra, fordításra és szöveggenerálásra.

2. **Keretrendszerek közötti kompatibilitás**: A könyvtár több mélytanulási keretrendszert támogat, köztük a PyTorch-ot, TensorFlow-t és JAX-et. Ez lehetővé teszi, hogy egy modellt az egyik keretrendszerben taníts meg, és a másikban használd.

3. **Multimodális képességek**: Az NLP mellett a Hugging Face Transformers támogatja a számítógépes látást (például képosztályozás, objektumfelismerés) és az audiófeldolgozást (például beszédfelismerés, audió osztályozás).

4. **Könnyű használat**: A könyvtár API-kat és eszközöket kínál a modellek egyszerű letöltéséhez és finomhangolásához, így kezdők és szakértők számára egyaránt hozzáférhető.

5. **Közösség és erőforrások**: A Hugging Face élénk közösséggel rendelkezik, valamint bőséges dokumentációval, oktatóanyagokkal és útmutatókkal, amelyek segítenek a felhasználóknak a könyvtár lehetőségeinek kihasználásában.
[hivatalos dokumentáció](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) vagy a [GitHub tárhelyük](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ez a leggyakrabban használt módszer, de GPU gyorsítást igényel. Végül is, olyan forgatókönyvek, mint a Vision és MoE, sok számítást igényelnek, ami a CPU-n nagyon lassú lesz, ha nem kvantáltak.


- Demo: Transformer használata Phi-3.5-Instruct hívásához [Kattintson erre a linkre](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer használata Phi-3.5-Vision hívásához [Kattintson erre a linkre](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer használata Phi-3.5-MoE hívásához [Kattintson erre a linkre](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
Az [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) egy olyan platform, amely megkönnyíti a nagy nyelvi modellek (LLM-ek) helyi futtatását a gépeden. Támogat különféle modelleket, mint például Llama 3.1, Phi 3, Mistral és Gemma 2. A platform leegyszerűsíti a folyamatot azzal, hogy a modell súlyokat, konfigurációt és adatokat egyetlen csomagba foglalja, így ez könnyebbé teszi a felhasználók számára a testreszabást és a saját modellek létrehozását. Az Ollama elérhető macOS-re, Linuxra és Windowsra. Remek eszköz, ha kísérletezni vagy telepíteni szeretnél LLM-eket anélkül, hogy felhőszolgáltatásokra támaszkodnál. Az Ollama a legközvetlenebb mód, csak ki kell futtatnod a következő parancsot.


```bash

ollama run phi3.5

```

**Foundry Local**

A [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) a Microsoft offline, eszközön futó környezete a Phi-hoz hasonló modellek teljesen saját hardvereden történő futtatásához - nem szükséges Azure előfizetés, API kulcs vagy hálózati kapcsolat. Automatikusan kiválasztja a legjobb rendelkezésre álló végrehajtó szolgáltatót (NPU, GPU vagy CPU), és egy OpenAI-kompatibilis végpontot tesz elérhetővé, így a meglévő `openai`/Azure AI Inference SDK kód minimális változtatással használhatja. Lásd a [Foundry Local dokumentációját](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) a kezdéshez.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Vagy használd közvetlenül az SDK-t Pythonban:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime generatív AI-hoz**

Az [ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) egy többplatformos inferencia és tanulás gépi tanulási gyorsító. Az ONNX Runtime a generatív AI (GENAI) számára egy erőteljes eszköz, amely segít hatékonyan futtatni generatív AI modelleket különböző platformokon.

## Mi az ONNX Runtime?
Az ONNX Runtime egy nyílt forráskódú projekt, amely lehetővé teszi a gépi tanulási modellek nagy teljesítményű inferenciáját. Támogatja a modelleket az Open Neural Network Exchange (ONNX) formátumban, amely egy szabvány a gépi tanulási modellek ábrázolására. Az ONNX Runtime inferencia gyorsabb ügyfélélményt és alacsonyabb költségeket biztosíthat, támogatva például mélytanulási keretrendszerekből származó modelleket, mint a PyTorch és TensorFlow/Keras, valamint klasszikus gépi tanulási könyvtárakat, mint a scikit-learn, LightGBM, XGBoost stb. Az ONNX Runtime kompatibilis különböző hardverekkel, driverekkel és operációs rendszerekkel, és optimális teljesítményt nyújt a hardveres gyorsítók kihasználásával, valamint gráfoptimalizációkkal és transzformációkkal.

## Mi a generatív AI?
A generatív AI olyan AI rendszerekre utal, amelyek képesek új tartalmakat generálni, például szöveget, képeket vagy zenét a betanított adatok alapján. Példák erre a nyelvi modellek, mint a GPT-3, vagy képgeneráló modellek, mint a Stable Diffusion. Az ONNX Runtime generatív AI-hoz könyvtár biztosítja az ONNX modellek generatív AI körforgását, beleértve az inferenciát az ONNX Runtime-tal, logits feldolgozást, keresést és mintavételezést, valamint a KV cache kezelését.

## ONNX Runtime a GENAI-hoz
Az ONNX Runtime a GENAI számára kibővíti az ONNX Runtime képességeit, hogy támogassa a generatív AI modelleket. Íme néhány fő jellemzője:

- **Széles platformtámogatás:** Különböző platformokon működik, beleértve a Windowst, Linuxot, macOS-t, Androidot és iOS-t.
- **Modelltámogatás:** Számos népszerű generatív AI modellt támogat, mint a LLaMA, GPT-Neo, BLOOM és mások.
- **Teljesítményoptimalizálás:** Tartalmaz optimalizációkat különféle hardveres gyorsítókhoz, például NVIDIA GPU-khoz, AMD GPU-khoz és másokhoz is.
- **Könnyű használat:** API-kat biztosít az alkalmazásokba való egyszerű integrációhoz, lehetővé téve szöveg, képek és más tartalmak generálását minimális kóddal.
- A felhasználók hívhatják a magas szintű generate() metódust, vagy egy ciklusban futtathatják a modell minden iterációját, egyszerre egy token generálásával, valamint opcionálisan frissítve a generálási paramétereket a ciklusban.
- Az ONNX runtime támogatja a mohó/sugár keresést, a TopP, TopK mintavételezést token sorozatok generálására, valamint beépített logits feldolgozást, például ismétlődési büntetéseket. Emellett egyszerűen hozzáadhatsz egyéni pontozást is.

## Kezdő lépések
Az ONNX Runtime a GENAI-hoz való használatának megkezdéséhez a következő lépéseket követheted:

### ONNX Runtime telepítése:
```Python
pip install onnxruntime
```
### A generatív AI bővítmények telepítése:
```Python
pip install onnxruntime-genai
```

### Egy modell futtatása: Íme egy egyszerű példa Pythonban:
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
### Demo: ONNX Runtime GenAI használata Phi-3.5-Vision hívásához


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

Az ONNX Runtime, Ollama és Foundry Local referencia módszerein túlmenően teljesíthetjük a kvantitatív modellek referálását is a különböző gyártók által biztosított modell referencia módszerei alapján. Ilyen például az Apple MLX keretrendszer Apple Metal-lel, Qualcomm QNN NPU-val, Intel OpenVINO CPU/GPU-val stb. Több tartalmat is kaphatsz a [Phi-3 Cookbook-ban](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).


## Továbbiak

Megtanultuk a Phi-3/3.5 család alapjait, de hogy többet tudjunk meg az SLM-ről, több ismeretre van szükségünk. A válaszokat megtalálhatod a Phi-3 Cookbookban. Ha többet szeretnél megtudni, kérjük, látogasd meg a [Phi-3 Cookbook]-ot (https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->