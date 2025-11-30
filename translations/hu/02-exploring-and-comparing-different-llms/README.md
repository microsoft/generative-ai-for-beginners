<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6b7629b8ee4d7d874a27213e903d86a7",
  "translation_date": "2025-10-17T21:27:32+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "hu"
}
-->
# Különböző LLM-ek felfedezése és összehasonlítása

[![Különböző LLM-ek felfedezése és összehasonlítása](../../../translated_images/02-lesson-banner.ef94c84979f97f60f07e27d905e708cbcbdf78707120553ccab27d91c947805b.hu.png)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Kattints a fenti képre, hogy megnézd a leckéről szóló videót_

Az előző leckében láthattuk, hogyan változtatja meg a generatív mesterséges intelligencia a technológiai környezetet, hogyan működnek a nagy nyelvi modellek (LLM-ek), és hogyan alkalmazhatja egy vállalkozás - például a mi startupunk - ezeket a saját eseteiben, hogy növekedjen! Ebben a fejezetben különböző típusú nagy nyelvi modelleket (LLM-eket) fogunk összehasonlítani, hogy megértsük azok előnyeit és hátrányait.

Startupunk következő lépése az LLM-ek jelenlegi környezetének feltérképezése és annak megértése, hogy melyek alkalmasak a mi felhasználási esetünkre.

## Bevezetés

Ez a lecke az alábbiakat fogja tárgyalni:

- Az LLM-ek különböző típusai a jelenlegi környezetben.
- Különböző modellek tesztelése, iterálása és összehasonlítása az Azure-ban történő felhasználásra.
- Hogyan telepítsünk egy LLM-et.

## Tanulási célok

A lecke elvégzése után képes leszel:

- Kiválasztani a megfelelő modellt a saját felhasználási esethez.
- Megérteni, hogyan kell tesztelni, iterálni és javítani a modell teljesítményét.
- Tudni, hogyan telepítik a vállalkozások a modelleket.

## Különböző típusú LLM-ek megértése

Az LLM-eket többféleképpen lehet kategorizálni az architektúrájuk, a tanítási adataik és a felhasználási esetük alapján. Ezeknek a különbségeknek a megértése segít a startupunknak kiválasztani a megfelelő modellt az adott helyzethez, valamint megérteni, hogyan kell tesztelni, iterálni és javítani a teljesítményt.

Számos különböző típusú LLM-modell létezik, és a választásod attól függ, hogy mire szeretnéd használni őket, milyen adataid vannak, mennyit vagy hajlandó fizetni, és még sok más tényezőtől.

Attól függően, hogy a modelleket szöveg-, hang-, videó-, képgenerálásra stb. szeretnéd használni, eltérő típusú modellt választhatsz.

- **Hang- és beszédfelismerés**. Erre a célra a Whisper típusú modellek kiváló választásnak bizonyulnak, mivel általános célúak és beszédfelismerésre irányulnak. Sokféle hanganyagon tanították őket, és képesek többnyelvű beszédfelismerésre. További információ a [Whisper típusú modellekről itt](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Képgenerálás**. A képgeneráláshoz a DALL-E és a Midjourney két nagyon ismert választás. A DALL-E-t az Azure OpenAI kínálja. [További információ a DALL-E-ről itt](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst), valamint a tananyag 9. fejezetében.

- **Szöveggenerálás**. A legtöbb modellt szöveggenerálásra tanították, és számos választási lehetőség áll rendelkezésre, például GPT-3.5-től GPT-4-ig. Ezek különböző költségekkel járnak, a GPT-4 a legdrágább. Érdemes megnézni az [Azure OpenAI játszóteret](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst), hogy értékelni tudjuk, mely modellek felelnek meg legjobban az igényeinknek képességek és költségek szempontjából.

- **Multimodalitás**. Ha többféle adatot szeretnél kezelni bemenetként és kimenetként, érdemes lehet olyan modelleket megvizsgálni, mint például a [gpt-4 turbo vizuális funkcióval vagy gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) - az OpenAI modellek legújabb kiadásai -, amelyek képesek kombinálni a természetes nyelvi feldolgozást a vizuális megértéssel, lehetővé téve a multimodális interfészeken keresztüli interakciókat.

Egy modell kiválasztása alapvető képességeket biztosít, amelyek azonban nem mindig elegendőek. Gyakran előfordul, hogy a vállalatnak specifikus adatai vannak, amelyeket valahogyan közölni kell az LLM-mel. Erre többféle megközelítés létezik, amelyeket a következő szakaszokban tárgyalunk.

### Alapmodellek és LLM-ek

Az Alapmodell kifejezést [Stanford kutatók alkották meg](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst), és olyan AI modellként definiálták, amely megfelel bizonyos kritériumoknak, például:

- **Nem felügyelt tanulással vagy önfelügyelt tanulással tanítják őket**, ami azt jelenti, hogy címkézetlen multimodális adatokon tanítják őket, és nem igényelnek emberi annotációt vagy adatcímkézést a tanítási folyamathoz.
- **Nagyon nagy modellek**, amelyek nagyon mély neurális hálózatokon alapulnak, és milliárdnyi paraméterrel vannak tanítva.
- **Általában más modellek „alapjaként” szolgálnak**, ami azt jelenti, hogy kiindulópontként használhatók más modellek építéséhez, amit finomhangolással lehet elérni.

![Alapmodellek és LLM-ek](../../../translated_images/FoundationModel.e4859dbb7a825c94b284f17eae1c186aabc21d4d8644331f5b007d809cf8d0f2.hu.png)

Kép forrása: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

A különbség további tisztázása érdekében vegyük példának a ChatGPT-t. A ChatGPT első verziójának létrehozásához egy GPT-3.5 nevű modell szolgált alapmodellként. Ez azt jelenti, hogy az OpenAI néhány chat-specifikus adatot használt fel egy finomhangolt GPT-3.5 verzió létrehozásához, amelyet kifejezetten arra specializáltak, hogy jól teljesítsen beszélgetési helyzetekben, például chatbotok esetében.

![Alapmodell](../../../translated_images/Multimodal.2c389c6439e0fc51b0b7b226d95d7d900d372ae66902d71b8ce5ec4951b8efbe.hu.png)

Kép forrása: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Nyílt forráskódú és zárt modellek

Az LLM-eket aszerint is lehet kategorizálni, hogy nyílt forráskódúak vagy zártak.

A nyílt forráskódú modellek olyan modellek, amelyeket a nyilvánosság számára elérhetővé tesznek, és bárki használhatja őket. Gyakran az őket létrehozó vállalat vagy a kutatói közösség teszi elérhetővé őket. Ezeket a modelleket lehet ellenőrizni, módosítani és testre szabni az LLM-ek különböző felhasználási eseteihez. Azonban nem mindig optimalizáltak a termelési használatra, és nem biztos, hogy olyan teljesítményesek, mint a zárt modellek. Ráadásul a nyílt forráskódú modellek finanszírozása korlátozott lehet, és nem biztos, hogy hosszú távon karbantartják őket, vagy frissítik a legújabb kutatásokkal. Népszerű nyílt forráskódú modellek például [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) és [LLaMA](https://llama.meta.com).

A zárt modellek olyan modellek, amelyeket egy vállalat birtokol, és nem tesznek nyilvánosan elérhetővé. Ezeket a modelleket gyakran optimalizálják termelési használatra. Azonban nem lehet őket ellenőrizni, módosítani vagy testre szabni különböző felhasználási esetekhez. Ráadásul nem mindig ingyenesek, és előfizetést vagy fizetést igényelhetnek a használathoz. Továbbá a felhasználók nem rendelkeznek kontrollal a modell tanításához használt adatok felett, ami azt jelenti, hogy a modell tulajdonosának kell megbízhatóan biztosítania az adatvédelem és az AI felelős használatának betartását. Népszerű zárt modellek például [OpenAI modellek](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) vagy [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Beágyazás, képgenerálás, szöveg- és kódgenerálás

Az LLM-eket az általuk generált kimenet alapján is kategorizálhatjuk.

A beágyazások olyan modellek, amelyek képesek a szöveget numerikus formává, úgynevezett beágyazássá alakítani, amely az input szöveg numerikus reprezentációja. A beágyazások megkönnyítik a gépek számára a szavak vagy mondatok közötti kapcsolatok megértését, és más modellek, például osztályozási vagy klaszterezési modellek bemeneteként is felhasználhatók, amelyek jobban teljesítenek numerikus adatokkal. A beágyazási modelleket gyakran használják transzfer tanulásra, ahol egy modellt egy helyettesítő feladatra építenek, amelyhez bőséges adat áll rendelkezésre, majd a modell súlyait (beágyazásokat) újra felhasználják más downstream feladatokhoz. Példa erre a kategóriára: [OpenAI beágyazások](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Beágyazás](../../../translated_images/Embedding.c3708fe988ccf76073d348483dbb7569f622211104f073e22e43106075c04800.hu.png)

A képgenerálási modellek olyan modellek, amelyek képeket generálnak. Ezeket a modelleket gyakran használják kép szerkesztésére, kép szintézisére és kép átalakítására. A képgenerálási modelleket gyakran nagy képadatbázisokon tanítják, például [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), és új képek generálására vagy meglévő képek szerkesztésére használhatók, például inpainting, szuperfelbontás és színezési technikák segítségével. Példák: [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) és [Stable Diffusion modellek](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Képgenerálás](../../../translated_images/Image.349c080266a763fd255b840a921cd8fc526ed78dc58708fa569ff1873d302345.hu.png)

A szöveg- és kódgenerálási modellek olyan modellek, amelyek szöveget vagy kódot generálnak. Ezeket a modelleket gyakran használják szövegösszefoglalásra, fordításra és kérdések megválaszolására. A szöveggenerálási modelleket gyakran nagy szövegadatbázisokon tanítják, például [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), és új szövegek generálására vagy kérdések megválaszolására használhatók. A kódgenerálási modelleket, mint például [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), gyakran nagy kódadatbázisokon tanítják, például GitHubon, és új kód generálására vagy meglévő kód hibáinak javítására használhatók.

![Szöveg- és kódgenerálás](../../../translated_images/Text.a8c0cf139e5cc2a0cd3edaba8d675103774e6ddcb3c9fc5a98bb17c9a450e31d.hu.png)

### Kódoló-dekódoló vs. Csak dekódoló

Az LLM-ek különböző architektúráinak megértéséhez használjunk egy hasonlatot.

Képzeld el, hogy a vezetőd adott neked egy feladatot, hogy írj egy kvízt a diákok számára. Két kollégád van; az egyik a tartalom létrehozásáért, a másik pedig annak ellenőrzéséért felel.

A tartalomkészítő olyan, mint egy csak dekódoló modell, amely képes megnézni a témát és azt, amit már leírtál, majd ennek alapján megírni egy tananyagot. Nagyon jó az érdekes és informatív tartalom írásában, de nem túl jó a téma és a tanulási célok megértésében. Néhány példa a dekódoló modellekre: a GPT család modelljei, például a GPT-3.

Az ellenőrző olyan, mint egy csak kódoló modell, amely megnézi az elkészült tananyagot és a válaszokat, észreveszi a kapcsolatokat és megérti a kontextust, de nem jó a tartalom generálásában. Példa a csak kódoló modellre: BERT.

Képzeld el, hogy lehetne valaki, aki egyszerre tudna kvízt készíteni és ellenőrizni, ez egy kódoló-dekódoló modell. Néhány példa: BART és T5.

### Szolgáltatás vs. Modell

Most beszéljünk a különbségről egy szolgáltatás és egy modell között. A szolgáltatás egy termék, amelyet egy felhőszolgáltató kínál, és gyakran modellek, adatok és más összetevők kombinációja. A modell egy szolgáltatás alapvető összetevője, és gyakran egy alapmodell, például egy LLM.

A szolgáltatások gyakran optimalizáltak termelési használatra, és gyakran könnyebben használhatók, például grafikus felhasználói felületen keresztül. Azonban a szolgáltatások nem mindig ingyenesek, és előfizetést vagy fizetést igényelhetnek a használathoz, cserébe a szolgáltatás tulajdonosának berendezései és erőforrásai használatáért, a költségek optimalizálásáért és az egyszerű skálázásért. Példa egy szolgáltatásra: [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), amely pay-as-you-go díjcsomagot kínál, ami azt jelenti, hogy a felhasználókat arányosan terhelik a szolgáltatás használatának mértékével. Az Azure OpenAI Service emellett vállalati szintű biztonságot és felelős AI keretrendszert kínál a modellek képességei mellett.

A modellek csak a neurális hálózatot jelentik, a paraméterekkel, súlyokkal és másokkal. Lehetővé teszik a vállalatok számára, hogy helyben futtassák őket, azonban ehhez berendezéseket kell vásárolni, struktúrát kell építeni a skálázáshoz, és licencet kell vásárolni vagy nyílt forráskódú modellt kell használni. Egy modell, mint például LLaMA, elérhető a használatra, de számítási kapacitás szükséges a
A legtöbb modell, amelyet az előző bekezdésekben említettünk (OpenAI modellek, nyílt forráskódú modellek, mint például a Llama2, és Hugging Face transformerek), elérhető a [Modellek katalógusában](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) az [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) platformon.

Az [Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) egy felhőalapú platform, amelyet fejlesztők számára terveztek generatív AI alkalmazások létrehozására és a teljes fejlesztési életciklus kezelésére - a kísérletezéstől az értékelésig -, azáltal, hogy az összes Azure AI szolgáltatást egyetlen központba integrálja, egy praktikus grafikus felülettel. Az Azure AI Studio Modellek katalógusa lehetővé teszi a felhasználók számára, hogy:

- Megtalálják az érdeklődésüknek megfelelő alapmodellt a katalógusban - akár saját fejlesztésű, akár nyílt forráskódú -, feladat, licenc vagy név alapján szűrve. A kereshetőség javítása érdekében a modellek gyűjteményekbe vannak rendezve, mint például az Azure OpenAI gyűjtemény, Hugging Face gyűjtemény és mások.

![Modellek katalógusa](../../../translated_images/AzureAIStudioModelCatalog.3cf8a499aa8ba0314f2c73d4048b3225d324165f547525f5b7cfa5f6c9c68941.hu.png)

- Áttekintsék a modellkártyát, amely részletes leírást tartalmaz a tervezett felhasználásról és a képzési adatokkal kapcsolatos információkról, kódpéldákat és értékelési eredményeket az Azure belső értékelési könyvtárában.

![Modellkártya](../../../translated_images/ModelCard.598051692c6e400d681a713ba7717e8b6e5e65f08d12131556fcec0f1789459b.hu.png)

- Összehasonlítsák az iparágban elérhető modellek és adathalmazok benchmarkjait, hogy felmérjék, melyik felel meg legjobban az üzleti igényeknek, a [Modellek benchmarkjai](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) panelen keresztül.

![Modellek benchmarkjai](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.hu.png)

- Finomhangolják a modellt egyedi képzési adatokkal, hogy javítsák a modell teljesítményét egy adott munkaterhelésben, kihasználva az Azure AI Studio kísérletezési és nyomonkövetési képességeit.

![Modell finomhangolása](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.hu.png)

- Telepítsék az eredeti előre betanított modellt vagy a finomhangolt verziót távoli valós idejű következtetésre - kezelt számítási környezetre - vagy szerver nélküli API végpontra - [fizetés használat alapján](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) -, hogy lehetővé tegyék az alkalmazások számára a modell használatát.

![Modell telepítése](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.hu.png)

> [!NOTE]
> Nem minden modell érhető el jelenleg finomhangolásra és/vagy fizetés használat alapján történő telepítésre a katalógusban. Ellenőrizze a modellkártyát a modell képességeiről és korlátairól szóló részletekért.

## LLM eredmények javítása

Startup csapatunkkal különböző típusú LLM-eket és egy felhőalapú platformot (Azure Machine Learning) vizsgáltunk meg, amely lehetővé teszi számunkra, hogy összehasonlítsuk a különböző modelleket, tesztadatokon értékeljük őket, javítsuk a teljesítményt és telepítsük őket következtetési végpontokra.

De mikor érdemes finomhangolni egy modellt az előre betanított helyett? Vannak más megközelítések is, amelyek javíthatják a modell teljesítményét egy adott munkaterhelésben?

Számos megközelítés létezik, amelyet egy vállalkozás alkalmazhat, hogy elérje a kívánt eredményeket egy LLM-től. Különböző típusú modelleket választhat, amelyek eltérő mértékű képzést kaptak, amikor egy LLM-et telepít a gyártásba, különböző szintű komplexitással, költséggel és minőséggel. Íme néhány megközelítés:

- **Prompt tervezés kontextussal**. Az ötlet az, hogy elegendő kontextust biztosítsunk a promptban, hogy biztosítsuk a szükséges válaszokat.

- **Retrieval Augmented Generation, RAG**. Az adatok például egy adatbázisban vagy webes végponton létezhetnek, és annak érdekében, hogy ezek az adatok vagy azok egy része bekerüljön a promptba, a releváns adatokat lekérhetjük, és a felhasználó promptjának részévé tehetjük.

- **Finomhangolt modell**. Itt a modellt tovább képezték saját adatokon, ami pontosabbá és az igényekre érzékenyebbé tette, bár költséges lehet.

![LLM-ek telepítése](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.hu.png)

Kép forrása: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt tervezés kontextussal

Az előre betanított LLM-ek nagyon jól működnek általános természetes nyelvi feladatokban, még akkor is, ha csak egy rövid promptot kapnak, például egy befejezendő mondatot vagy egy kérdést – az úgynevezett „zero-shot” tanulás.

Azonban minél részletesebben tudja a felhasználó megfogalmazni a kérdését, egy részletes kéréssel és példákkal – a kontextussal –, annál pontosabb és közelebb áll a válasz a felhasználó elvárásaihoz. Ebben az esetben „one-shot” tanulásról beszélünk, ha a prompt csak egy példát tartalmaz, és „few-shot” tanulásról, ha több példát tartalmaz.
A prompt tervezés kontextussal a legköltséghatékonyabb megközelítés a kezdéshez.

### Retrieval Augmented Generation (RAG)

Az LLM-ek korlátozása, hogy csak azokat az adatokat tudják használni, amelyeket a képzésük során használtak fel válasz generálásához. Ez azt jelenti, hogy nem tudnak semmit a képzési folyamatuk után történt eseményekről, és nem férnek hozzá nem nyilvános információkhoz (például vállalati adatokhoz).
Ez leküzdhető a RAG segítségével, egy olyan technikával, amely külső adatokat ad hozzá a prompthoz dokumentumdarabok formájában, figyelembe véve a prompt hosszának korlátait. Ezt támogatják a vektoralapú adatbázis eszközök (például [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), amelyek hasznos darabokat keresnek előre meghatározott adatforrásokból, és hozzáadják őket a prompt kontextusához.

Ez a technika nagyon hasznos, ha egy vállalkozásnak nincs elegendő adata, ideje vagy erőforrása egy LLM finomhangolásához, de mégis szeretné javítani a teljesítményt egy adott munkaterhelésben, és csökkenteni a téves információk, azaz a valóság elferdítésének vagy káros tartalom kockázatát.

### Finomhangolt modell

A finomhangolás egy olyan folyamat, amely a transzfer tanulást használja fel arra, hogy a modellt egy adott feladathoz vagy problémához „adaptálja”. A few-shot tanulástól és a RAG-tól eltérően ez egy új modell létrehozását eredményezi, frissített súlyokkal és torzításokkal. Ehhez egy képzési példákból álló készlet szükséges, amely egyetlen bemenetet (a promptot) és a hozzá tartozó kimenetet (a befejezést) tartalmazza.
Ez lenne az előnyben részesített megközelítés, ha:

- **Finomhangolt modellek használata**. Egy vállalkozás inkább kevésbé teljesítményorientált finomhangolt modelleket (például beágyazási modelleket) használna, mint nagy teljesítményű modelleket, ami költséghatékonyabb és gyorsabb megoldást eredményez.

- **Késleltetés figyelembevétele**. A késleltetés fontos egy adott felhasználási esetben, így nem lehetséges nagyon hosszú promptokat használni, vagy a példák száma, amelyeket a modellnek meg kell tanulnia, nem fér bele a prompt hosszának korlátjába.

- **Naprakészség fenntartása**. Egy vállalkozásnak sok kiváló minőségű adata és valós címkéje van, valamint megvannak az erőforrásai, hogy ezeket az adatokat idővel naprakészen tartsa.

### Képzett modell

Egy LLM nulláról történő képzése kétségtelenül a legnehezebb és legösszetettebb megközelítés, amely hatalmas mennyiségű adatot, képzett erőforrásokat és megfelelő számítási kapacitást igényel. Ezt az opciót csak akkor érdemes fontolóra venni, ha egy vállalkozásnak van egy speciális területre vonatkozó felhasználási esete és nagy mennyiségű, terület-specifikus adata.

## Tudásellenőrzés

Mi lehet egy jó megközelítés az LLM befejezési eredmények javítására?

1. Prompt tervezés kontextussal
1. RAG
1. Finomhangolt modell

A: 3, ha van elég idő, erőforrás és kiváló minőségű adatok, a finomhangolás a jobb opció a naprakészség fenntartásához. Azonban, ha az idő szűkös, érdemes először a RAG-ot fontolóra venni.

## 🚀 Kihívás

Olvasson többet arról, hogyan használhatja a [RAG-ot](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) vállalkozása számára.

## Nagyszerű munka, folytassa a tanulást

A lecke befejezése után tekintse meg [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejlessze generatív AI ismereteit!

Lépjen tovább a 3. leckére, ahol megvizsgáljuk, hogyan lehet [felelősségteljesen építeni generatív AI-val](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.