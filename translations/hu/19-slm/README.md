# Bevezetés a kis nyelvi modellekbe a generatív MI kezdőknek szóló útmutatójában
A generatív MI az a mesterséges intelligencia izgalmas területe, amely olyan rendszerek létrehozására összpontosít, amelyek képesek új tartalmak generálására. Ez a tartalom terjedhet a szövegtől és képektől a zenén át akár teljes virtuális környezetekig. A generatív MI egyik legizgalmasabb alkalmazási területe a nyelvi modellek világa.

## Mik azok a kis nyelvi modellek?

A kis nyelvi modell (SLM) a nagy nyelvi modell (LLM) egy kicsinyített változatát jelenti, amely sok nagy nyelvi modell architekturális elvét és technikáját alkalmazza, miközben jelentősen csökkentett számítási erőforrás-igénnyel bír. 

Az SLM-ek a nyelvi modellek egy alcsoportja, amelyeket emberhez hasonló szöveg generálására terveztek. A nagyobb társaikkal, például a GPT-4-el ellentétben az SLM-ek kompaktabbak és hatékonyabbak, ezért ideálisak olyan alkalmazásokhoz, ahol korlátozott a számítási kapacitás. Méretük kisebb mivolta ellenére még mindig különféle feladatokat képesek ellátni. Általában az SLM-ek úgy készülnek, hogy nagy nyelvi modelleket tömörítenek vagy desztillálnak, céljuk pedig, hogy megőrizzék az eredeti modell funkcionalitásának és nyelvi képességeinek jelentős részét. A modell méretének csökkentése egyszerűsíti a modellt, így az SLM-ek mind memóriahasználat, mind számítási igények tekintetében hatékonyabbak. Ezek az optimalizációk ellenére az SLM-ek még mindig széles körű természetesnyelv-feldolgozási (NLP) feladatokat képesek ellátni:

- Szöveg generálása: koherens és kontextusban releváns mondatok vagy bekezdések létrehozása.
- Szöveg kiegészítése: mondatok előrejelzése és kiegészítése adott bemenet alapján.
- Fordítás: szöveg átalakítása egyik nyelvről a másikra.
- Összefoglalás: hosszú szövegek összefoglalása rövidebb, könnyebben emészthető összefoglalókká.

Bár teljesítmény vagy mélyebb megértés tekintetében bizonyos kompromisszumokkal járnak a nagyobb modellekhez képest.

## Hogyan működnek a kis nyelvi modellek?
Az SLM-ek hatalmas mennyiségű szöveges adaton tanulnak. A tanulás során megértik a nyelv mintázatait és szerkezetét, lehetővé téve, hogy olyan szöveget generáljanak, amely nyelvtanilag helyes és kontextusban megfelelő. A tanítási folyamat a következő lépésekből áll:

- Adatgyűjtés: nagy mennyiségű szöveges adat összegyűjtése különböző forrásokból.
- Előkészítés: az adatok tisztítása és rendszerezése, hogy alkalmassá váljanak a tanításra.
- Tanítás: gépi tanulási algoritmusok alkalmazása a modell megtanítására a szöveg megértésére és generálására.
- Finomhangolás: a modell beállítása annak érdekében, hogy adott feladatokban jobb teljesítményt nyújtson.

Az SLM-ek fejlesztése összhangban áll azzal az egyre növekvő igénnyel, hogy olyan modellek jöjjenek létre, amelyek erőforrás-korlátozott környezetekben, például mobil eszközökön vagy éloldali számítástechnikai platformokon telepíthetők, ahol a teljes méretű LLM-ek erőforrásigénye miatt nem praktikusak. Az SLM-ek a hatékonyságra törekedve egyensúlyt teremtenek a teljesítmény és az elérhetőség között, lehetővé téve szélesebb körű alkalmazást különféle területeken.

![slm](../../../translated_images/hu/slm.4058842744d0444a.webp)

## Tanulási célok

Ebben az órában be szeretnénk mutatni az SLM-ek ismereteit, és a Microsoft Phi-3-mal kombinálva megismerni a szöveg-, látás- és MoE forgatókönyveket.

A lecke végére képesnek kell lennie arra, hogy válaszoljon a következő kérdésekre:

- Mi az az SLM?
- Mi a különbség az SLM és az LLM között?
- Mi az a Microsoft Phi-3/3.5 család?
- Hogyan futtassunk inferenciát a Microsoft Phi-3/3.5 családdal?

Készen áll? Kezdjük.

## A nagy nyelvi modellek (LLM-ek) és a kis nyelvi modellek (SLM-ek) közötti különbségek

Mind az LLM-ek, mind az SLM-ek valószínűségi gépi tanulási elveken alapulnak, hasonló megközelítéseket követnek az architekturális tervezésükben, a tanítási módszertanukban, az adatok generálásában és a modellek értékelésében. Azonban számos kulcsfontosságú tényező megkülönbözteti ezt a két modelltípust.

## Kis nyelvi modellek alkalmazási területei

Az SLM-ek számos alkalmazási területtel rendelkeznek, többek között:

- Csevegőrobotok: ügyfélszolgálat nyújtása és felhasználókkal való interakció beszélgetés formájában.
- Tartalomkészítés: írók segítése ötletek generálásával vagy akár teljes cikkek megírásával.
- Oktatás: diákok segítése írásbeli feladatokban vagy új nyelvek tanulásában.
- Elérhetőség: eszközök létrehozása fogyatékkal élők számára, például szövegfelolvasó rendszerek.

**Méret**
  
Az egyik legfőbb különbség az LLM-ek és az SLM-ek között a modellek méretében rejlik. Az LLM-ek, például a ChatGPT (GPT-4) becslések szerint 1,76 billió paraméterből állhatnak, míg az olyan nyílt forráskódú SLM-ek, mint a Mistral 7B, jelentősen kevesebb paraméterrel — körülbelül 7 milliárddal — rendelkeznek. Ez a különbség elsősorban a modellarchitektúra és a tanítási folyamatok eltéréseiből adódik. Például a ChatGPT a self-attention mechanizmust alkalmazza egy kódoló-dekódoló keretrendszerben, míg a Mistral 7B csúszóablakos attention-t használ, ami hatékonyabb tanítást tesz lehetővé egy kizárólag dekódoló modellben. Ez az architekturális eltérés mélyreható következményekkel jár a modellek komplexitására és teljesítményére nézve.

**Megértés**

Az SLM-ek tipikusan úgy vannak optimalizálva, hogy adott szakterületeken magas teljesítményt nyújtsanak, így erősen specializáltak, ugyanakkor korlátozottak lehetnek abban, hogy széleskörű kontextuális megértést adjanak át több tudományterületen átívelően. Ezzel szemben az LLM-ek az emberi intelligenciát próbálják szélesebb értelemben szimulálni. Hatalmas, sokféle adatbázisokon tanulva az LLM-ek jól teljesítenek különféle területeken, nagyobb sokoldalúságot és alkalmazkodóképességet kínálva. Ennek következtében az LLM-ek alkalmasabbak szélesebb körű alkalmazási feladatokra, mint például a természetes nyelvfeldolgozás vagy a programozás.

**Számítási igény**

Az LLM-ek tanítása és üzemeltetése erőforrás-igényes folyamat, amely gyakran jelentős számítási infrastruktúrát, többek között nagyméretű GPU klasztereket igényel. Például egy ChatGPT-szerű modell teljes körű tanítása több ezer GPU-t igényelhet hosszú időn keresztül. Ezzel szemben az SLM-ek, kisebb paraméterszámuk miatt, számítási szempontból elérhetőbbek. A Mistral 7B például helyi gépen is tanítható és futtatható közepes GPU kapacitással, bár a tanítás még mindig több órát vesz igénybe több GPU használatával.

**Elfogultság**

Az elfogultság ismert probléma az LLM-eknél, főként a tanítási adatok jellege miatt. Ezek a modellek gyakran nyers, nyíltan elérhető internetes adatokat használnak, amelyek alulreprezentálhatnak vagy tévesen ábrázolhatnak bizonyos csoportokat, hibás címkézést tartalmazhatnak, vagy nyelvi elfogultságot tükrözhetnek, amelyek hatással vannak a dialektusokra, földrajzi eltérésekre és nyelvtani szabályokra. Ezen túlmenően az LLM architektúrák összetettsége véletlenül fokozhatja az elfogultságot, amely gondos finomhangolás nélkül észrevétlen maradhat. Ezzel szemben az SLM-ek, melyek szűkebb, szakterület-specifikus adatbázisokon tanulnak, természetüknél fogva kevésbé hajlamosak ilyen elfogultságokra, bár nem teljesen mentesek tőlük.

**Inferencia**

Az SLM-ek kisebb mérete jelentős előnyt jelent az inferencia sebességében, lehetővé téve, hogy helyi hardveren hatékonyan generáljanak outputokat kiterjedt párhuzamos feldolgozás nélkül. Ezzel szemben az LLM-ek méretük és komplexitásuk miatt gyakran nagy párhuzamos számítási kapacitást igényelnek elfogadható inferenciaidő eléréséhez. Több párhuzamos felhasználó jelenléte tovább lassítja az LLM-ek válaszidejét, különösen, ha nagy méretekben vannak telepítve.

Összefoglalva, habár az LLM-ek és az SLM-ek is a gépi tanuláson alapulnak, jelentősen eltérnek a modellméret, erőforrás-igény, kontextuális megértés, elfogultságra való hajlam és inferenciasebesség tekintetében. Ezek a különbségek tükrözik azt, hogy mely felhasználási esetekre a legalkalmasabbak: az LLM-ek sokoldalúbbak, de erőforrás-igényesek, míg az SLM-ek szakterületileg hatékonyabbak, alacsonyabb számítási követelményekkel.

***Megjegyzés: Ebben az órában az SLM-et a Microsoft Phi-3 / 3.5 segítségével mutatjuk be példaként.***

## A Phi-3 / Phi-3.5 család bemutatása

A Phi-3 / 3.5 család elsősorban szöveg-, látás- és Agent (MoE) alkalmazási forgatókönyvekre fókuszál:

### Phi-3 / 3.5 Instruct

Elsősorban szöveg generálásra, csevegés kiegészítésére és tartalominformáció kinyerésre, stb.

**Phi-3-mini**

A 3,8 milliárd paraméteres nyelvi modell elérhető a Microsoft Foundry-n, a Hugging Face-en és az Ollama-n keresztül. A Phi-3 modellek jelentősen felülmúlják az azonos vagy nagyobb méretű nyelvi modelleket kulcsfontosságú referenciaméréseken (lásd a lenti benchmark számokat, magasabb érték jobb). A Phi-3-mini teljesítménye jobb, mint a kétszer olyan nagy modelleké, míg a Phi-3-small és Phi-3-medium nagyobb modelleket is, köztük a GPT-3.5-öt is felülmúlja.

**Phi-3-small & medium**

A csupán 7 milliárd paraméterrel rendelkező Phi-3-small különféle nyelvi, logikai, kódolási és matematikai benchmarkokon jobban teljesít, mint a GPT-3.5T.

A Phi-3-medium 14 milliárd paraméterrel folytatja ezt a tendenciát, és felülmúlja a Gemini 1.0 Prót.

**Phi-3.5-mini**

Ezt tekinthetjük a Phi-3-mini továbbfejlesztésének. A paraméterek nem változtak, de javítja a többnyelvű támogatást (20+ nyelvet támogat: arab, kínai, cseh, dán, holland, angol, finn, francia, német, héber, magyar, olasz, japán, koreai, norvég, lengyel, portugál, orosz, spanyol, svéd, thai, török, ukrán), továbbá erősebb támogatást nyújt a hosszú kontextushoz.

A 3,8 milliárd paraméteres Phi-3.5-mini felülmúlja az azonos méretű nyelvi modelleket, és kiegyenlíti a kétszer akkora modelleket is.

### Phi-3 / 3.5 Vision

A Phi-3/3.5 Instruct modellt úgy képzelhetjük el, mint Phi értelmezési képességét, a Vision pedig azt az „szemet”, ami Phi-nak a világ megértését biztosítja.


**Phi-3-Vision**

A Phi-3-vision, amely csupán 4,2 milliárd paraméterrel rendelkezik, folytatja ezt a tendenciát, és felülmúlja a nagyobb modelleket, például a Claude-3 Haiku-t és a Gemini 1.0 Pro-t általános vizuális érvelési feladatokban, OCR-ben, illetve táblázat- és diagramértelmezési feladatokban.


**Phi-3.5-Vision**

A Phi-3.5-Vision szintén a Phi-3-Vision továbbfejlesztése, amely támogatja a több képet. Úgy tekinthetjük, mint a látás fejlesztését; nemcsak képeket, hanem videókat is képes „megnézni”.

A Phi-3.5-vision jobb teljesítményt nyújt nagyobb modelleknél, például a Claude-3.5 Sonnet-nél és a Gemini 1.5 Flash-nél OCR, táblázat- és diagramértelmező feladatokban, és az általános vizuális tudásalapú érvelési feladatokban is azonos szinten áll. Többképes bemenetet támogat, azaz egyszerre több képen végez érvelést.


### Phi-3.5-MoE

***A szakértők keveréke (Mixture of Experts, MoE)*** lehetővé teszi, hogy a modelleket sokkal kevesebb számítással előtanítsák, ami azt jelenti, hogy ugyanakkora számítási keretből drasztikusan növelhető a modell vagy az adathalmaz mérete. Különösen egy MoE modellnek gyorsabban kell elérnie ugyanazt a minőséget, mint annak hagyományos, sűrű párja esetében az előtanítás során.

A Phi-3.5-MoE 16x3,8 milliárd paraméteres szakértői modult foglal magában. A Phi-3.5-MoE, amelynek aktív paramétereinek száma csupán 6,6 milliárd, hasonló szintű érvelésben, nyelvi megértésben és matematikában teljesít, mint sokkal nagyobb modellek.

A Phi-3/3.5 család modelljeit különféle forgatókönyvekben használhatjuk. Ellentétben az LLM-ekkel, a Phi-3/3.5-mini vagy a Phi-3/3.5-Vision telepíthető éloldali eszközökön is.


## Hogyan használjuk a Phi-3/3.5 család modelljeit

Azt reméljük, hogy a Phi-3/3.5 modellt különféle helyzetekben alkalmazhatjuk. Ezután bemutatjuk a Phi-3/3.5 használatát különböző forgatókönyvek alapján.

![phi3](../../../translated_images/hu/phi3.655208c3186ae381.webp)

### Inferencia felhő API-kon keresztül

**Microsoft Foundry modellek**

> **Megjegyzés:** A GitHub Models 2026 júliusának végén megszűnik. A közvetlen helyettesítő a [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

A Microsoft Foundry modellek használata a legközvetlenebb út. Gyorsan elérhetjük a Phi-3/3.5-Instruct modellt a Foundry modellkatalóguson keresztül. Az Azure AI Inference SDK / OpenAI SDK segítségével kódon keresztül érhetjük el az API-t, hogy végrehajtsuk a Phi-3/3.5-Instruct hívást. Különféle hatások tesztelésére a Playground is használható.

- Demó: a Phi-3-mini és a Phi-3.5-mini hatásainak összehasonlítása kínai helyzetekben

![phi3](../../../translated_images/hu/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/hu/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ha pedig a látás- vagy MoE modelleket szeretnénk használni, a Microsoft Foundryt is igénybe vehetjük a hívások végrehajtásához. Ha érdekli, elolvashatja a Phi-3 szakácskönyvet, amely bemutatja, hogyan lehet Phi-3/3.5 Instructot, Visiont és MoE-t hívni Microsoft Foundryn keresztül [Erre a linkre kattintva](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

A felhőalapú Microsoft Foundry modelelkatalógus mellett használhatja a [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst)-et is a kapcsolódó hívások végrehajtásához. Az NVIDIA NIM segítségével elérheti a Phi-3/3.5 család API hívásait. Az NVIDIA NIM (NVIDIA Inference Microservices) egy gyorsított inferencia mikro-szolgáltatásokból álló készlet, amely segíti a fejlesztőket AI modellek hatékony telepítésében különböző környezetekben, mint például felhőkben, adatközpontokban és munkaállomásokon.

Íme néhány fő jellemzője az NVIDIA NIM-nek:

- **Egyszerű telepítés:** Az NIM lehetővé teszi AI modellek egyetlen paranccsal történő telepítését, megkönnyítve a meglévő munkafolyamatokba való integrációt.

- **Optimalizált teljesítmény:** Az NVIDIA előre optimalizált inferencia motorjait használja, mint például a TensorRT és a TensorRT-LLM, amelyek alacsony késleltetést és nagy átviteli sebességet biztosítanak.
- **Skálázhatóság:** A NIM támogatja a Kubernetes alapú automatikus skálázást, ami lehetővé teszi a változó munkaterhelések hatékony kezelését.
- **Biztonság és irányítás:** A szervezetek megtarthatják az irányítást adataik és alkalmazásaik felett azáltal, hogy a NIM mikroszolgáltatásokat saját, kezelt infrastruktúrájukon üzemeltetik.
- **Iparági szabvány API-k:** A NIM iparági szabvány API-kat biztosít, így könnyű AI alkalmazásokat építeni és integrálni, mint például chatbotokat, AI-asszisztenseket és még sok mást.

A NIM az NVIDIA AI Enterprise része, amelynek célja az AI modellek telepítésének és üzemeltetésének egyszerűsítése, biztosítva azok hatékony futtatását NVIDIA GPU-kon.

- Demó: NVIDIA NIM használata Phi-3.5-Vision-API hívásához  [[Kattintson ide](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 helyi futtatása
Az inferencia Phi-3-mal vagy bármely nyelvi modellel (mint a GPT-3) az a folyamat, amely során az adott bemenet alapján választ vagy előrejelzést generál. Amikor egy utasítást vagy kérdést adsz a Phi-3-nak, a kiképzett neurális hálózata elemzi a tanított adatokban lévő mintákat és összefüggéseket, hogy a legvalószínűbb és legmegfelelőbb választ állítsa elő.

**Hugging Face Transformer**
A Hugging Face Transformers egy hatékony könyvtár természetes nyelv feldolgozáshoz (NLP) és más gépi tanulási feladatokhoz. Íme néhány kulcspont róla:

1. **Előtréningezett modellek**: Több ezer előre betanított modellt kínál, amelyeket különböző feladatokhoz használhatunk, mint például szöveg osztályozás, név szerinti entitás felismerés, kérdés-válasz, összefoglalás, fordítás és szöveg generálás.

2. **Keretrendszer interoperabilitás:** A könyvtár több mély tanulási keretrendszert támogat, beleértve a PyTorch, TensorFlow és JAX rendszereket. Ez lehetővé teszi, hogy egy modellt egy keretrendszerben tanítsunk, majd egy másikban használjuk.

3. **Multimodális képességek:** Az NLP-n kívül a Hugging Face Transformers támogat feladatokat számítógépes látásban (pl. képosztályozás, objektumfelismerés) és audiofeldolgozásban (pl. beszédfelismerés, audio osztályozás).

4. **Egyszerű használat:** A könyvtár API-kat és eszközöket kínál a modellek könnyű letöltéséhez és finomhangolásához, így kezdők és szakértők számára egyaránt hozzáférhető.

5. **Közösség és források:** A Hugging Face élénk közösséggel és széleskörű dokumentációval, oktatóanyagokkal és útmutatókkal rendelkezik, hogy segítsen a felhasználóknak elindulni és a legtöbbet kihozni a könyvtárból.
[hivatalos dokumentáció](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) vagy a [GitHub tárházuk](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ez a leggyakrabban használt módszer, de GPU gyorsítást igényel. Már csak azért is, mert például a Vision és a MoE forgatókönyvek sok számítást igényelnek, amelyek CPU-n nagyon lassúak lennének, ha nem kvantáltak.


- Demó: Transformer használata Phi-3.5-Instruct hívásához [Kattintson ide](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demó: Transformer használata Phi-3.5-Vision hívásához [Kattintson ide](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demó: Transformer használata Phi-3.5-MoE hívásához [Kattintson ide](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
Az [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) egy platform, amely megkönnyíti a nagy nyelvi modellek (LLM-ek) helyi futtatását a gépeden. Különféle modelleket támogat, mint például a Llama 3.1, Phi 3, Mistral és Gemma 2, többek között. A platform leegyszerűsíti a folyamatot azáltal, hogy a modell súlyokat, konfigurációt és adatokat egyetlen csomagba rendezi, így könnyebb a felhasználóknak testre szabni és létrehozni saját modelljeiket. Az Ollama elérhető macOS, Linux és Windows rendszereken. Remek eszköz, ha szeretnél kísérletezni vagy telepíteni LLM-eket anélkül, hogy felhőszolgáltatásokra támaszkodnál. Az Ollama a legközvetlenebb mód, csak ki kell adnod a következő parancsot.


```bash

ollama run phi3.5

```

**Foundry Local**

A [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) a Microsoft offline, helyi futtatási környezete modellek, például a Phi futtatásához kizárólag a saját hardvereden – nem szükséges Azure előfizetés, API kulcs vagy hálózati kapcsolat. Automatikusan kiválasztja a legjobb elérhető futtatási szolgáltatót (NPU, GPU vagy CPU), és egy OpenAI-kompatibilis végpontot nyújt, így a meglévő `openai`/Azure AI Inferencia SDK kód minimális módosítással használható. Kezdéshez lásd a [Foundry Local dokumentációját](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Vagy használd az SDK-t közvetlenül Pythonban:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime a GenAI-hoz**

Az [ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) egy platformközi inferencia- és tanulásgyorsító gépi tanuláshoz. Az ONNX Runtime a Generatív AI-hoz (GENAI) egy erős eszköz, amely hatékony futtatást biztosít generatív AI modellek számára különféle platformokon.

## Mi az az ONNX Runtime?
Az ONNX Runtime egy nyílt forráskódú projekt, amely lehetővé teszi gépi tanulási modellek nagy teljesítményű inferenciáját. Támogatja az Open Neural Network Exchange (ONNX) formátumban lévő modelleket, amely egy gépi tanulási modellek ábrázolására szolgáló szabvány. Az ONNX Runtime inferencia gyorsabb ügyfélélményeket és alacsonyabb költségeket tesz lehetővé, támogatva modelleket mély tanulási keretrendszerekből, például PyTorch és TensorFlow/Keras, valamint klasszikus gépi tanulási könyvtárakból, mint a scikit-learn, LightGBM, XGBoost stb. Az ONNX Runtime kompatibilis különböző hardverekkel, driverekkel és operációs rendszerekkel, és optimális teljesítményt nyújt, kihasználva a hardver gyorsítókat, valamint grafikus optimalizációkat és transzformációkat.

## Mi az a Generatív AI?
A generatív AI olyan AI rendszerekre utal, amelyek képesek új tartalmakat generálni, például szöveget, képeket vagy zenét a betanított adataik alapján. Példák erre a nyelvi modellek, mint a GPT-3, és a képalkotó modellek, mint a Stable Diffusion. Az ONNX Runtime GenAI könyvtár biztosítja a generatív AI körforgást az ONNX modellekhez, beleértve az inferenciát az ONNX Runtime-tal, a logit feldolgozást, keresést és mintavételt, valamint a KV gyorsítótár kezelését.

## ONNX Runtime a GENAI-hoz
Az ONNX Runtime a GENAI-hoz kiterjeszti az ONNX Runtime képességeit, hogy támogassa a generatív AI modelleket. Íme néhány kulcsfontosságú jellemző:

- **Széles platform támogatás:** Működik különféle platformokon, beleértve Windows-t, Linuxot, macOS-t, Androidot és iOS-t.
- **Modelltámogatás:** Sok népszerű generatív AI modellt támogat, mint a LLaMA, GPT-Neo, BLOOM és mások.
- **Teljesítményoptimalizáció:** Optimalizációkat tartalmaz különböző hardver gyorsítókhoz, például NVIDIA GPU-khoz, AMD GPU-khoz és egyebekhez.
- **Egyszerű használat:** API-kat biztosít az alkalmazásokba való egyszerű integráláshoz, hogy minimális kóddal generálhass szöveget, képeket és más tartalmakat.
- A felhasználók egy magas szintű generate() metódust hívhatnak, vagy futtathatják a modell minden iterációját egy ciklusban, egyszerre egy token generálásával, és opcionálisan frissíthetik a generálási paramétereket a ciklusban.
- Az ONNX runtime támogatja a greedy/beam keresést és a TopP, TopK mintavételt token sorozatok generálásához, valamint beépített logit feldolgozást, például ismétlődési büntetések kezelését. Egyéni pontozás is könnyen hozzáadható.

## Kezdés
Az ONNX Runtime a GENAI-hoz kezdéséhez kövesd az alábbi lépéseket:

### Telepítsd az ONNX Runtime-ot:
```Python
pip install onnxruntime
```
### Telepítsd a Generatív AI kiterjesztéseket:
```Python
pip install onnxruntime-genai
```

### Futtass egy modellt: Íme egy egyszerű példa Pythonban:
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
### Demó: ONNX Runtime GenAI használata Phi-3.5-Vision hívásához


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

Az ONNX Runtime, Ollama és Foundry Local referencia módszerein túlmenően befejezhetjük a kvantitatív modellek referencia készletét is a különböző gyártók által biztosított modell referencia módszerek alapján. Ilyen például az Apple MLX keretrendszer Apple Metal-lel, a Qualcomm QNN NPU-val, az Intel OpenVINO CPU/GPU-val stb. További tartalomhoz látogass el a [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) oldalra.


## Továbbiak

Megismertük a Phi-3/3.5 család alapjait, de hogy többet tudjunk meg az SLM-ről, több tudásra van szükségünk. A válaszokat megtalálod a Phi-3 Cookbookban. Ha többet szeretnél tanulni, látogass el a [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) oldalra.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->