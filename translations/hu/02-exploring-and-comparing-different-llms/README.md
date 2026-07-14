# Különböző LLM-ek felfedezése és összehasonlítása

[![Különböző LLM-ek felfedezése és összehasonlítása](../../../translated_images/hu/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Kattintson a fenti képre a lecke videójának megtekintéséhez_

Az előző leckében láttuk, hogyan változtatja meg a generatív mesterséges intelligencia a technológiai környezetet, hogyan működnek a nagy nyelvi modellek (LLM-ek), és hogyan alkalmazhatja egy üzlet - mint például mi, a startupunk - ezeket az eseteiben és növekedhet! Ebben a fejezetben különböző típusú nagy nyelvi modelleket (LLM-eket) hasonlítunk össze, hogy megértsük az előnyeiket és hátrányaikat.

A következő lépés startupunk útján az LLM-ek jelenlegi helyzetének feltérképezése és annak megértése, hogy melyek megfelelőek az eseteinkhez.

## Bevezetés

Ez a lecke az alábbiakat fogja lefedni:

- Különböző típusú LLM-ek a jelenlegi környezetben.
- Különböző modellek tesztelése, iterálása és összehasonlítása az Azure-ban az eseteihez.
- Hogyan lehet egy LLM-et telepíteni.

## Tanulási célok

A lecke elvégzése után képes lesz arra, hogy:

- Kiválassza a megfelelő modellt az eseteihez.
- Megértse, hogyan teszteljen, iteráljon és javítsa modellje teljesítményét.
- Tudja, hogyan telepítenek modelleket az üzletek.

## Értsük meg az LLM-ek különböző típusait

Az LLM-ek többféle kategorizálása lehetséges az architektúrájuk, a képzési adataik és az eseteik alapján. E különbségek megértése segít startupunknak kiválasztani a helyes modellt az adott forgatókönyvhöz, és megérteni, hogyan teszteljünk, iteráljunk és javítsuk a teljesítményt.

Sokféle LLM modell létezik, a modell kiválasztása attól függ, mire kívánja használni őket, milyen adatai vannak, mennyit hajlandó fizetni és más tényezők.

Attól függően, hogy a modelleket szöveg, hang, videó, kép generálására vagy másra szeretné használni, más típusú modellt választhat.

- **Hang- és beszédfelismerés**. A Whisper-stílusú modellek még mindig hasznosak általános célú beszédfelismerésre, de a gyártási választások közé tartoznak az újabb beszéd-szöveg modellek is, mint például a `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` és diarizációs változatok. Értékelje a nyelvi lefedettséget, diarizációt, valós idejű támogatást, késleltetést és költséget az adott szcenárióban. Tudjon meg többet az [OpenAI beszéd-szöveg dokumentációjában](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Kép generálás**. A DALL-E és a Midjourney jól ismert kép generáló lehetőségek, de a jelenlegi OpenAI kép API-k a `gpt-image-2` jellegű GPT kép modellekre koncentrálnak, miközben a Stable Diffusion, Imagen, Flux és más modellcsaládok is gyakori választások. Használjon prompt követést, szerkesztési támogatást, stíluskontrollt, biztonsági követelményeket és licencelést összehasonlítva. Tudjon meg többet az [OpenAI kép generálási útmutatójában](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) és a tananyagnak a 9. fejezetében.

- **Szöveg generálás**. A szövegmodellek lefedik a frontier modelleket, érvelő modelleket, kisebb, alacsony késleltetésű modelleket és nyílt súlyú modelleket. Jelenlegi példák az OpenAI GPT-5.x modellek, Anthropic Claude 4.x modellek, Google Gemini 3.x modellek, Meta Llama 4 modellek és Mistral modellek. Ne válasszon csak a megjelenési dátum vagy ár alapján; hasonlítsa össze a feladat minőségét, késleltetést, kontextusablakot, eszközhasználatot, biztonsági viselkedést, regionális elérhetőséget és teljes költséget. A [Microsoft Foundry modell katalógus](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) jó hely az Azure-on elérhető modellek összehasonlításához.

- **Multi-modalitás**. Sok jelenlegi modell képes több mint csak szöveg feldolgozására. Egyesek képet, hangot vagy videót is elfogadnak bemenetként; némelyek eszközöket képesek hívni; és speciális modellek képet, hangot vagy videót generálhatnak. Például a jelenlegi OpenAI modellek támogatják a szöveget és kép bemenetet, a Gemini modellek verziótól függően támogatják a szöveg, kód, kép, hang és videó bemeneteket, míg a Llama 4 Scout és Maverick nyílt súlyú natívan multimodális modellek. Mindig ellenőrizze minden modell kártyáját a támogatott bemeneti és kimeneti modalitások miatt, mielőtt munkafolyamatot épít köréjük.

Egy modell kiválasztása bizonyos alapvető képességeket ad, azonban ezek önmagukban nem mindig elegendőek. Gyakran rendelkezik a cég specifikus adatokkal, amelyeket valahogy el kell juttatni az LLM-hez. Ennek többféle megközelítése létezik, ezekről később részletesebben is szó lesz.

### Alapmodellek versus LLM-ek

Az Alapmodell kifejezést a [Stanford kutatói alkották meg](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst), és egy olyan mesterséges intelligencia modellt jelent, amely az alábbi kritériumokat követi:

- **Félig felügyelt vagy önfelügyelt tanulással vannak kiképezve**, azaz felcímkézetlen multimodális adatokat használnak, és nem igényelnek emberi annotációt vagy címkézést a képzési folyamat során.
- **Nagyon nagy modellek**, nagyon mély neurális hálózatokon alapulnak, amelyek milliárdnyi paraméteren vannak kiképezve.
- **Általában ‘alapként’ szolgálnak más modellekhez**, vagyis kiindulópontként használhatók más modellek építéséhez, amelyeket finomhangolással lehet továbbfejleszteni.

![Alapmodellek versus LLM-ek](../../../translated_images/hu/FoundationModel.e4859dbb7a825c94.webp)

Kép forrása: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

A különbség további tisztázása érdekében vegyük a ChatGPT-t történelmi példaként. A ChatGPT korai verziói a GPT-3.5 modellt használták alapmodellként. Az OpenAI ezután chat-specifikus adatokat és összehangolási technikákat alkalmazott, hogy olyan finomhangolt verziót hozzon létre, amely jobban teljesít beszélgetési forgatókönyvekben, például chatbotokban. A modern AI szolgáltatások gyakran több modellvariáns között választanak, így a szolgáltatás neve és az alapmodell neve nem mindig egyezik meg.

![Alapmodell](../../../translated_images/hu/Multimodal.2c389c6439e0fc51.webp)

Kép forrása: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Nyílt súlyú / nyílt forráskódú versus tulajdonosi modellek

Egy másik módja az LLM-ek kategorizálásának, hogy azok nyílt súlyúak, nyílt forráskódúak vagy tulajdonosi modellek-e.

A nyílt forráskódú és nyílt súlyú modellek modell artefaktumait átláthatóvá teszik ellenőrzésre, letöltésre vagy testreszabásra, de a licencük eltérő lehet. Egyesek teljesen nyílt forráskódúak, míg mások nyílt súlyú modellek felhasználási korlátozásokkal. Hasznosak lehetnek, amikor egy üzletnek nagyobb irányításra van szüksége a telepítés, adatok lokalitása, költség vagy testreszabás terén. Azonban a csapatoknak még mindig át kell nézniük a licencfeltételeket, a szolgáltatási költségeket, karbantartást, biztonsági frissítéseket és az értékelési minőséget a termelési használat előtt. Példák erre a [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), néhány [Mistral modell](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) és sok modell a [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst) oldalon.

A tulajdonosi modelleket egy szolgáltató birtokolja és üzemelteti. Ezek a modellek általában kezelhető gyártási használatra vannak optimalizálva, és erős támogatást, biztonsági rendszereket, eszközintegrációt és skálázhatóságot kínálnak. Az ügyfelek azonban rendszerint nem ellenőrizhetik vagy módosíthatják a modell súlyokat, és át kell tekinteniük a szolgáltató adatvédelmi, megőrzési, megfelelőségi és elfogadható használati feltételeit. Példák erre az [OpenAI modellek](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst), és [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Beágyazás, képalkotás, szöveg- és kódgenerálás

Az LLM-eket a kimeneti típusuk alapján is kategorizálhatjuk.

A beágyazások olyan modellek csoportja, amelyek képesek a szöveget numerikus formára, azaz beágyazásra alakítani, ami az input szöveg numerikus reprezentációja. A beágyazások segítik a gépeket a szavak vagy mondatok közötti kapcsolatok jobb megértésében, és más modellek bemeneteként használhatóak, mint osztályozó vagy klaszterező modellek, amelyek numerikus adaton jobban teljesítenek. A beágyazó modelleket gyakran használják átvitel- vagy transzfer tanulásra, ahol egy modellt egy nagy adatmennyiséggel rendelkező helyettesítő feladatra képeznek, majd a modell súlyait (beágyazásokat) újrafelhasználják más downstream feladatokra. Példa erre a kategóriára az [OpenAI beágyazások](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Beágyazás](../../../translated_images/hu/Embedding.c3708fe988ccf760.webp)

A képalkotó modellek olyan modellek, amelyek képeket generálnak. Ezeket gyakran használják kép szerkesztésére, kép szintézisre és kép átalakításra. A képalkotó modelleket általában nagy képadatbázisokon képezik ki, mint például a [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), és használhatók új képek generálására vagy meglévő képek szerkesztésére például festéssel (inpainting), felbontás növeléssel (super-resolution) és színezéssel. Példák erre a kategóriára a [GPT kép modellek](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion modellek](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) és Imagen modellek.

![Képalkotás](../../../translated_images/hu/Image.349c080266a763fd.webp)

A szöveg- és kódgeneráló modellek olyan modellek, amelyek szöveget vagy kódot generálnak. Ezeket gyakran használják szöveg összefoglalására, fordításra és kérdés-válaszra. A szöveg generáló modelleket általában nagy szöveg adatbázisokon képezik ki, mint például a [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), és használhatók új szöveg generálására vagy kérdések megválaszolására. A kódgeneráló modelleket, mint a [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), nagy kódadatbázisokon képezik ki, például GitHub-on, és használhatók új kód generálására vagy hibák javítására meglévő kódban.

![Szöveg- és kódgenerálás](../../../translated_images/hu/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder kontra csak Decoder

Az LLM-ek különböző architektúráinak megbeszéléséhez használjunk egy analógiát.

Tegyük fel, hogy a vezetője adott egy feladatot: készítsen egy kvízt a diákoknak. Két kollégája van; az egyik a tartalom létrehozásáért, a másik azok átnézéséért felelős.

A tartalomfejlesztő olyan, mint egy csak dekóder modell: megnézi a témát, látja, mit írt már, majd ezen a kontextuson alapulva folytatja a tartalom generálását. Nagyon jó abban, hogy érdekfeszítő és informatív tartalmat írjon, de nem mindig a legjobb választás, ha csak osztályozni, visszakeresni vagy kódolni kell az információt. Példák csak dekóder modellcsaládokra a GPT és Llama modellek.

A lektor olyan, mint egy csak enkóder modell, megnézi a megírt anyagot és a válaszokat, észleli a kapcsolatokat és érti a kontextust, de nem jó tartalom-generálásban. Egy példa a csak enkóder modellre a BERT.

Tegyük fel, hogy van valaki, aki tudna tartalmat készíteni és lektorálni is egyben, ez egy Encoder-Decoder modell lenne. Példák erre a BART és a T5.

### Szolgáltatás kontra Modell

Most beszéljünk a különbségről egy szolgáltatás és egy modell között. Egy szolgáltatást a felhőszolgáltató kínál termékként, és gyakran több modell, adat és egyéb komponens kombinációja. A modell a szolgáltatás magja, és gyakran egy alapmodell, például egy LLM.

A szolgáltatások általában a termelési használatra optimalizáltak, és gyakran könnyebben használhatók a szolgáltatás grafikus felületén keresztül, mint a modellek. Azonban a szolgáltatások nem mindig ingyenesek, és előfizetést vagy díjat igényelnek a használatért cserébe, a szolgáltató gépeinek és erőforrásainak kihasználására, a költségek optimalizálására és a könnyű skálázásra. Egy példa szolgáltatásra az [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), amely "fizess amennyit használsz" díjszabást kínál, azaz a felhasználók arányosan fizetnek a szolgáltatás használatuk alapján. Az Azure OpenAI Service vállalati szintű biztonságot és felelős MI keretrendszert is kínál a modellek képességein túl.

A modellek a neurális hálózat artefaktumai: paraméterek, súlyok, architektúra, tokenizáló és a támogató konfiguráció. Egy modell futtatása helyben vagy egy privát környezetben megfelelő hardvert, szolgáltatási infrastruktúrát, monitorozást és vagy kompatibilis nyílt forráskódú/nyílt súlyú licencet, vagy kereskedelmi licencet igényel. Nyílt súlyú modellek, mint a Llama 4 vagy a Mistral modellek önállóan hosztolhatók, de mégis számítási kapacitást és működtetési szakértelmet követelnek meg.

## Hogyan teszteljünk és iteráljunk különböző modellekkel az Azure-on a teljesítmény megértése érdekében


Miután csapatunk feltérképezte a jelenlegi LLM-ek tájképét és azonosított néhány jó jelöltet a szcenárióikhoz, a következő lépés az, hogy teszteljük őket az adataikon és a munkaterhelésükön. Ez egy iteratív folyamat, amely kísérletezéssel és mérésekkel történik.
A legtöbb modell, amit az előző bekezdésekben említettünk (OpenAI modellek, nyílt súlyú modellek, mint a Llama 4 és a Mistral, valamint a Hugging Face modellek) elérhető a [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst) alatt.

A [Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), korábban Azure AI Studio/Azure AI Foundry néven ismert, egy egységes Azure platform AI alkalmazások és ügynökök építésére. Segíti a fejlesztőket az életciklus kezelésében az kísérletezéstől és értékeléstől a bevezetésen, felügyeleten és irányításon át. A Microsoft Foundry modellkatalógusa lehetővé teszi a felhasználó számára, hogy:

- Megtalálja az érdeklődésre számot tartó alapmodellt a katalógusban, beleértve az Azure által árusított modelleket, valamint a partnerek és közösségi szolgáltatók modelljeit. A felhasználók szűrhetnek feladat, szolgáltató, licenc, bevezetési lehetőség vagy név alapján.

![Model catalog](../../../translated_images/hu/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Megtekintheti a modellkártyát, beleértve a célzott használat részletes leírását, a képzési adatokat, kódrészleteket és az eredményértékeléseket a belső értékelési könyvtárban.

![Model card](../../../translated_images/hu/ModelCard.598051692c6e400d.webp)

- Összehasonlíthatja a benchmarkokat a különböző modellek és iparági adatkészletek között annak érdekében, hogy felmérje, melyik felel meg legjobban az üzleti szcenáriónak, a [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) panel segítségével.

![Model benchmarks](../../../translated_images/hu/ModelBenchmarks.254cb20fbd06c03a.webp)

- Finomhangolhatja a támogatott modelleket egyéni képzési adatokon, hogy javítsa a modell teljesítményét egy adott munkaterhelés esetén, kihasználva a Microsoft Foundry kísérletezési és nyomonkövetési képességeit.

![Model fine-tuning](../../../translated_images/hu/FineTuning.aac48f07142e36fd.webp)

- Telepítheti az eredeti előre betanított modellt vagy a finomhangolt verziót egy távoli, valós idejű becslési végpontra, kezelt számítási vagy szerver nélküli telepítési lehetőségeket használva, hogy az alkalmazások képesek legyenek azt fogyasztani.

![Model deployment](../../../translated_images/hu/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Nem minden modell érhető el jelenleg finomhangolásra és/vagy fogyasztás szerinti telepítésre a katalógusban. Ellenőrizze a modellkártyát a modell képességeiről és korlátairól szóló részletekért.

## LLM eredmények javítása

Startup csapatunkkal különféle LLM-eket és egy felhőplatformot (Microsoft Foundry) vizsgáltunk, amely lehetővé teszi a különböző modellek összehasonlítását, tesztadatokon való értékelését, a teljesítmény javítását és becslési végpontokon való telepítését.

De mikor érdemes inkább finomhangolni egy modellt, mint előre betanított modellt használni? Vannak-e más megközelítések a modell teljesítményének javítására specifikus munkaterheléseken?

Számos megközelítés létezik, amelyeket egy vállalkozás használhat, hogy megszerezze a kívánt eredményeket egy LLM-től. Különböző típusú modelleket választhat, más-más képzési szinttel, amikor LLM-et vezet be éles környezetben, különböző komplexitás, költség és minőség szinttel. Íme néhány különböző megközelítés:

- **Prompt mérnökség kontextussal**. Az ötlet az, hogy elegendő kontextust biztosítunk a kérdésben, hogy biztosan megkapjuk a kívánt válaszokat.

- **Retrieval Augmented Generation, RAG**. Az ön adatai például egy adatbázisban vagy webes végponton létezhetnek, hogy biztosítsuk ennek az adatnak, vagy annak egy részének a bevonását a kérdezés időpontjában, lekérheti a releváns adatokat, és beépítheti a felhasználó promptjába.

- **Finomhangolt modell**. Itt tovább képezte a modellt a saját adataival, ami a modell pontosabbá és igényekhez jobban igazodóvá tette, de költséges lehet.

![LLMs deployment](../../../translated_images/hu/Deploy.18b2d27412ec8c02.webp)

Kép forrása: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt mérnökség kontextussal

Az előre betanított LLM-ek nagyon jól működnek általános természetes nyelvű feladatokon, még akkor is, ha csak egy rövid promptot adnak meg nekik, például egy befejezendő mondatot vagy kérdést – az úgynevezett „zero-shot” tanulást.

Azonban minél inkább a felhasználó képes részletes kérdést és példákat adni – a Kontextust –, annál pontosabb és a felhasználó elvárásaihoz közelebb álló választ kap. Ebben az esetben „one-shot” tanulásról beszélünk, ha a prompt csak egy példát tartalmaz, és „few shot” tanulásról, ha több példát is tartalmaz.
A prompt mérnökség kontextussal a leggazdaságosabb megközelítés az induláshoz.

### Retrieval Augmented Generation (RAG)

Az LLM-ek abban korlátozottak, hogy csak azokat az adatokat használhatják, amelyeket a képzés során felhasználtak a válasz generálásához. Ez azt jelenti, hogy nem tudnak semmit azokról a tényekről, amelyek a képzési folyamat után történtek, és nem férnek hozzá nem nyilvános információkhoz (például cégadatokhoz).
Ezt meg lehet oldani a RAG technikával, amely promptokat egészít ki külső adatokkal dokumentumdarabok formájában, figyelembe véve a prompt hosszának korlátait. Ezt támogatják a vektoralapú adatbázis eszközök (például [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), amelyek előhívják a hasznos darabokat különböző előre definiált adatforrásokból és hozzáadják a prompt Kontextusához.

Ez a technika nagyon hasznos, amikor egy vállalkozásnak nincs elég adata, ideje vagy erőforrása az LLM finomhangolására, de mégis javítani szeretné a teljesítményt egy adott munkaterhelés esetén, és csökkenteni a hallucinált, elavult vagy nem támogatott válaszok kockázatát.

### Finomhangolt modell

A finomhangolás egy olyan folyamat, amely átviteli tanulást használ a modell „adaptálására” egy specifikus feladatra vagy probléma megoldására. A „few-shot” tanulástól és a RAG-tól eltérően egy új modell jön létre, frissített súlyokkal és eltolódásokkal. Ehhez egy képzési példakészletre van szükség, amely egyetlen bemenetből (prompt) és annak kapcsolódó kimenetéből (befejezés) áll.
Ez lenne az előnyben részesített megközelítés, ha:

- **Kisebb, feladatspecifikus modelleket használunk**. Egy vállalkozás inkább finomhangolna egy kisebb modellt egy szűk feladatra, mint hogy ismételten promptoljon egy nagyobb, csúcskategóriás modellt, ami költséghatékonyabb és gyorsabb megoldást eredményez.

- **Latencia figyelembevétele**. A latencia fontos egy adott esetben, ezért nem használhatók nagyon hosszú promptok vagy a megtanulandó példák száma nem fér bele a prompt hosszkorlátjába.

- **Stabil viselkedés adaptálása**. Egy vállalkozásnak sok minőségi példája van, és azt akarja, hogy a modell következetesen kövesse a feladat mintázatát, kimeneti formátumát, hangnemét vagy domén-specifikus stílusát. Ha a fő probléma frissebb tények vagy privát ismeretek gyakori változása, inkább a RAG-et használjuk, a finomhangolás önmagában nem elég.

### Betanított modell

Egy LLM-et az alapoktól betanítani kétségtelenül a legnehezebb és legösszetettebb megközelítés, amely hatalmas adatmennyiséget, szakképzett erőforrásokat és megfelelő számítási kapacitást igényel. Ez az opció csak akkor javasolt, ha egy vállalkozásnak van domén-specifikus esete és nagy mennyiségű domén-központú adata.

## Tudásellenőrzés

Mi lehet egy jó megközelítés az LLM befejezési eredmények javítására?

1. Prompt mérnökség kontextussal
1. RAG
1. Finomhangolt modell

V: Mindhárom segíthet. Kezdje a prompt mérnökséggel és kontextussal a gyors javításokhoz, majd használja a RAG-et, amikor a modellnek aktuális tényekre vagy privát üzleti adatokra van szüksége. Válassza a finomhangolást, ha van elegendő minőségi példája, és szükséges, hogy a modell következetesen kövesse a feladatot, formátumot, hangnemet vagy domén mintát.

## 🚀 Kihívás

Olvasson tovább arról, hogyan tudja [használni a RAG-et](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) az üzleti céljaira.

## Nagyszerű munka, folytassa a tanulást

A lecke befejezése után tekintse meg a [Generative AI Learning gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejlessze generatív AI tudását!

Lépjen át a 3. leckére, ahol megvizsgáljuk, hogyan [építhet felelősségteljesen generatív AI-val](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->