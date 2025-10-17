<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0135e6c271f3ece8699050d4debbce88",
  "translation_date": "2025-10-17T21:32:06+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "hu"
}
-->
# Prompt Engineering Alapjai

[![Prompt Engineering Alapjai](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.hu.png)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Bevezetés
Ez a modul a generatív AI modellek hatékony utasításainak létrehozásához szükséges alapvető fogalmakat és technikákat tárgyalja. Az, hogy hogyan fogalmazzuk meg az utasításokat egy LLM számára, szintén számít. Egy gondosan megfogalmazott utasítás jobb minőségű választ eredményezhet. De mit is jelentenek pontosan az olyan kifejezések, mint a _prompt_ és a _prompt engineering_? És hogyan javíthatom az LLM-nek küldött utasítás _bemenetét_? Ezekre a kérdésekre próbálunk választ adni ebben a fejezetben és a következőben.

A _generatív AI_ képes új tartalmakat létrehozni (például szövegeket, képeket, hangokat, kódokat stb.) a felhasználói kérésekre válaszul. Ezt olyan _Nagy Nyelvi Modellek_ segítségével éri el, mint az OpenAI GPT ("Generative Pre-trained Transformer") sorozata, amelyeket természetes nyelv és kód használatára képeztek ki.

A felhasználók most már ismerős paradigmák, például chat segítségével léphetnek kapcsolatba ezekkel a modellekkel, anélkül hogy technikai szakértelemre vagy képzésre lenne szükségük. A modellek _utasítás-alapúak_ - a felhasználók szöveges bemenetet (utasítást) küldenek, és visszakapják az AI válaszát (kimenetet). Ezután "beszélgethetnek az AI-val" iteratívan, többfordulós párbeszédekben, finomítva az utasítást, amíg a válasz megfelel az elvárásaiknak.

Az "utasítások" most a generatív AI alkalmazások elsődleges _programozási interfészévé_ válnak, amelyek megmondják a modelleknek, mit tegyenek, és befolyásolják a visszakapott válaszok minőségét. A "Prompt Engineering" egy gyorsan növekvő tanulmányi terület, amely az utasítások _tervezésére és optimalizálására_ összpontosít, hogy következetes és minőségi válaszokat érjen el nagy léptékben.

## Tanulási célok

Ebben a leckében megtanuljuk, mi az a Prompt Engineering, miért fontos, és hogyan készíthetünk hatékonyabb utasításokat egy adott modellhez és alkalmazási célhoz. Megértjük a prompt engineering alapfogalmait és legjobb gyakorlatait - és megismerünk egy interaktív Jupyter Notebook "sandbox" környezetet, ahol ezek a fogalmak valós példákon alkalmazhatók.

A lecke végére képesek leszünk:

1. Elmagyarázni, mi az a prompt engineering és miért fontos.
2. Leírni az utasítások összetevőit és azok használatát.
3. Megtanulni a prompt engineering legjobb gyakorlatait és technikáit.
4. Alkalmazni a tanult technikákat valós példákra, egy OpenAI végpont használatával.

## Kulcsfogalmak

Prompt Engineering: Az AI modellek kívánt kimenetek előállítására irányuló bemenetek tervezésének és finomításának gyakorlata.  
Tokenizáció: A szöveg kisebb egységekre, úgynevezett tokenekre bontásának folyamata, amelyeket a modell megérthet és feldolgozhat.  
Instruction-Tuned LLM-ek: Nagy Nyelvi Modellek (LLM-ek), amelyeket specifikus utasításokkal finomhangoltak, hogy javítsák válaszaik pontosságát és relevanciáját.

## Tanulási Sandbox

A prompt engineering jelenleg inkább művészet, mint tudomány. A legjobb módja annak, hogy javítsuk az intuíciót, ha _többet gyakorlunk_, és egy próbálgatásos megközelítést alkalmazunk, amely ötvözi az alkalmazási terület szakértelmét az ajánlott technikákkal és modell-specifikus optimalizálásokkal.

A lecke mellé tartozó Jupyter Notebook egy _sandbox_ környezetet biztosít, ahol kipróbálhatjuk, amit tanulunk - menet közben vagy a kódolási kihívás részeként a végén. Az gyakorlatok végrehajtásához szükség lesz:

1. **Egy Azure OpenAI API kulcsra** - a telepített LLM szolgáltatási végpontjára.  
2. **Egy Python futtatási környezetre** - amelyben a Notebook futtatható.  
3. **Helyi környezeti változókra** - _végezd el a [BEÁLLÍTÁS](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) lépéseit most, hogy készen állj_.

A notebook _kezdő_ gyakorlatokat tartalmaz - de bátorítunk, hogy adj hozzá saját _Markdown_ (leírás) és _Code_ (utasítás kérések) szekciókat, hogy kipróbálj több példát vagy ötletet - és fejleszd az intuíciódat az utasítások tervezésében.

## Illusztrált útmutató

Szeretnéd átlátni, miről szól ez a lecke, mielőtt belemerülsz? Nézd meg ezt az illusztrált útmutatót, amely bemutatja a főbb témákat és a legfontosabb tanulságokat, amelyeket érdemes átgondolni mindegyiknél. A lecke útvonala elvezet a főbb fogalmak és kihívások megértésétől azok kezeléséig releváns prompt engineering technikákkal és legjobb gyakorlatokkal. Ne feledd, hogy az útmutató "Haladó technikák" szekciója a tananyag _következő_ fejezetében tárgyalt tartalomra utal.

![Prompt Engineering Illusztrált Útmutató](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.hu.png)

## Startupunk

Most beszéljünk arról, hogyan kapcsolódik _ez a téma_ a startup küldetésünkhöz, amelynek célja [az AI innováció eljuttatása az oktatásba](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). AI-alapú alkalmazásokat szeretnénk építeni a _személyre szabott tanulás_ érdekében - ezért gondoljuk át, hogyan tervezhetnek különböző felhasználók utasításokat az alkalmazásunkban:

- **Adminisztrátorok** kérhetik az AI-t, hogy _elemezze a tantervi adatokat, és azonosítsa a hiányosságokat_. Az AI összefoglalhatja az eredményeket, vagy kód segítségével vizualizálhatja azokat.  
- **Oktatók** kérhetik az AI-t, hogy _készítsen egy tantervet egy célközönség és téma számára_. Az AI személyre szabott tervet készíthet egy megadott formátumban.  
- **Diákok** kérhetik az AI-t, hogy _segítsen nekik egy nehéz tantárgyban_. Az AI most már irányíthatja a diákokat órákkal, tippekkel és példákkal, amelyek az ő szintjükhöz igazodnak.

Ez csak a jéghegy csúcsa. Nézd meg a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - egy nyílt forráskódú utasítások könyvtárát, amelyet oktatási szakértők állítottak össze - hogy szélesebb képet kapj a lehetőségekről! _Próbálj ki néhányat ezek közül az utasítások közül a sandboxban vagy az OpenAI Playgroundban, hogy lásd, mi történik!_

<!--
LECKE SABLON:
Ez az egység az alapfogalom #1-et kell, hogy lefedje.
Erősítsd meg a fogalmat példákkal és hivatkozásokkal.

FOGALOM #1:
Prompt Engineering.
Határozd meg, és magyarázd el, miért van rá szükség.
-->

## Mi az a Prompt Engineering?

Ezt a leckét azzal kezdtük, hogy a **Prompt Engineering**-et úgy határoztuk meg, mint a szöveges bemenetek (utasítások) _tervezésének és optimalizálásának_ folyamatát, amelynek célja, hogy következetes és minőségi válaszokat (kimeneteket) érjen el egy adott alkalmazási cél és modell esetében. Ezt egy 2 lépéses folyamatként képzelhetjük el:

- Az _eredeti utasítás megtervezése_ egy adott modellhez és célhoz.  
- Az utasítás _iteratív finomítása_ a válasz minőségének javítása érdekében.  

Ez szükségszerűen egy próbálgatásos folyamat, amely felhasználói intuíciót és erőfeszítést igényel az optimális eredmények eléréséhez. De miért fontos ez? Ahhoz, hogy erre a kérdésre válaszoljunk, először három fogalmat kell megértenünk:

- _Tokenizáció_ = hogyan "látja" a modell az utasítást.  
- _Alap LLM-ek_ = hogyan "dolgozza fel" az alapmodell az utasítást.  
- _Instruction-Tuned LLM-ek_ = hogyan látja a modell most már a "feladatokat".  

### Tokenizáció

Egy LLM az utasításokat _tokenek sorozataként_ látja, ahol különböző modellek (vagy egy modell különböző verziói) ugyanazt az utasítást különböző módon tokenizálhatják. Mivel az LLM-ek tokeneken (és nem nyers szövegen) vannak kiképezve, az utasítások tokenizálásának módja közvetlen hatással van a generált válasz minőségére.

Hogy intuíciót szerezzünk arról, hogyan működik a tokenizáció, próbáljunk ki olyan eszközöket, mint az [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), amelyet az alábbiakban láthatunk. Másold be az utasításodat - és nézd meg, hogyan alakul át tokenekké, figyelve arra, hogyan kezelik a szóköz karaktereket és írásjeleket. Ne feledd, hogy ez a példa egy régebbi LLM-et (GPT-3) mutat - így ha egy újabb modellel próbálkozol, eltérő eredményt kaphatsz.

![Tokenizáció](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.hu.png)

### Fogalom: Alapmodellek

Miután egy utasítás tokenizálásra került, az ["Alap LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (vagy Alapmodell) elsődleges funkciója az, hogy megjósolja a sorozat következő tokenjét. Mivel az LLM-ek hatalmas szöveges adatbázisokon vannak kiképezve, jól ismerik a tokenek közötti statisztikai összefüggéseket, és bizonyos magabiztossággal képesek megjósolni a következő lépést. Ne feledd, hogy nem értik a szavak _jelentését_ az utasításban vagy a tokenben; csak egy mintát látnak, amelyet "befejezhetnek" a következő jóslatukkal. Folytathatják a sorozat előrejelzését, amíg a felhasználó be nem avatkozik, vagy amíg egy előre meghatározott feltétel meg nem szakad.

Szeretnéd látni, hogyan működik az utasítás-alapú kimenet? Írd be a fenti utasítást az Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) alapértelmezett beállításaival. A rendszer úgy van konfigurálva, hogy az utasításokat információkérésként kezelje - így egy olyan kimenetet kell látnod, amely kielégíti ezt a kontextust.

De mi van akkor, ha a felhasználó valami konkrétat szeretne látni, amely megfelel bizonyos kritériumoknak vagy feladati célnak? Itt jönnek képbe az _instruction-tuned_ LLM-ek.

![Alap LLM Chat Kimenet](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.hu.png)

### Fogalom: Instruction-Tuned LLM-ek

Egy [Instruction-Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) az alapmodellel kezdődik, és példákkal vagy bemenet/kimenet párokkal (például többfordulós "üzenetekkel") finomhangolják, amelyek egyértelmű utasításokat tartalmazhatnak - és az AI válasza megpróbálja követni az utasítást.

Ez olyan technikákat használ, mint az Emberi Visszacsatolással Támogatott Megerősítő Tanulás (RLHF), amely képes a modellt _utasítások követésére_ és _visszacsatolásokból való tanulásra_ képezni, hogy olyan válaszokat állítson elő, amelyek jobban megfelelnek a gyakorlati alkalmazásoknak és relevánsabbak a felhasználói célok szempontjából.

Próbáljuk ki - térjünk vissza a fenti utasításhoz, de most változtassuk meg a _rendszerüzenetet_, hogy a következő utasítást adja meg kontextusként:

> _Foglalja össze a kapott tartalmat egy második osztályos tanuló számára. Tartsa az eredményt egy bekezdésben, 3-5 pontban._

Látható, hogy az eredmény most már a kívánt célhoz és formátumhoz igazodik? Egy oktató most már közvetlenül felhasználhatja ezt a választ az osztályának szánt diákok számára készített diákban.

![Instruction-Tuned LLM Chat Kimenet](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.hu.png)

## Miért van szükségünk Prompt Engineeringre?

Most, hogy tudjuk, hogyan dolgozzák fel az LLM-ek az utasításokat, beszéljünk arról, _miért_ van szükségünk prompt engineeringre. A válasz abban rejlik, hogy a jelenlegi LLM-ek számos kihívást jelentenek, amelyek megnehezítik a _megbízható és következetes kimenetek_ elérését anélkül, hogy erőfeszítést tennénk az utasítások megalkotására és optimalizálására. Például:

1. **A modell válaszai sztochasztikusak.** Az _ugyanaz az utasítás_ valószínűleg különböző válaszokat eredményez különböző modellekkel vagy modellverziókkal. És még az _ugyanazon modell_ is különböző eredményeket produkálhat különböző időpontokban. _A prompt engineering technikák segíthetnek minimalizálni ezeket a variációkat jobb irányelvek megadásával_.  

1. **A modellek hamis válaszokat adhatnak.** A modellek _nagy, de véges_ adatbázisokon vannak előkészítve, ami azt jelenti, hogy hiányzik a tudásuk a képzési körön kívüli fogalmakról. Ennek eredményeként olyan kimeneteket állíthatnak elő, amelyek pontatlanok, képzeletbeliek vagy közvetlenül ellentmondanak a tényeknek. _A prompt engineering technikák segítenek a felhasználóknak az ilyen hamisítások azonosításában és enyhítésében, például az AI-tól idézetek vagy érvelés kérésével_.  

1. **A modellek képességei eltérőek lehetnek.** Az újabb modellek vagy modellgenerációk gazdagabb képességekkel rendelkeznek, de egyedi sajátosságokat és kompromisszumokat is hoznak a költs
Egy webes keresés azt mutatta, hogy léteznek kitalált történetek (pl. televíziós sorozatok vagy könyvek) a marsi háborúkról – de egyik sem 2076-ban játszódik. Józan ésszel is belátható, hogy 2076 _a jövőben van_, így nem kapcsolható valódi eseményhez.

Mi történik tehát, ha ezt a kérdést különböző LLM szolgáltatókkal futtatjuk?

> **Válasz 1**: OpenAI Playground (GPT-35)

![Válasz 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.hu.png)

> **Válasz 2**: Azure OpenAI Playground (GPT-35)

![Válasz 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.hu.png)

> **Válasz 3**: Hugging Face Chat Playground (LLama-2)

![Válasz 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.hu.png)

Ahogy várható volt, minden modell (vagy modellverzió) kissé eltérő válaszokat generál a sztochasztikus viselkedés és a modell képességeinek különbségei miatt. Például az egyik modell egy nyolcadikos közönséget céloz meg, míg a másik egy középiskolás diákot feltételez. Mindhárom modell azonban olyan válaszokat generált, amelyek meggyőzhetik egy tájékozatlan felhasználót arról, hogy az esemény valós.

Olyan prompttervezési technikák, mint a _metaprompting_ és a _hőmérséklet-konfiguráció_ bizonyos mértékig csökkenthetik a modell által generált téves információkat. Az új prompttervezési _architektúrák_ pedig zökkenőmentesen integrálják az új eszközöket és technikákat a promptfolyamatba, hogy enyhítsék vagy csökkentsék ezeket a hatásokat.

## Esettanulmány: GitHub Copilot

Zárjuk ezt a szakaszt azzal, hogy megismerjük, hogyan használják a prompttervezést valós megoldásokban, egy esettanulmányon keresztül: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

A GitHub Copilot az "AI páros programozója" – szöveges utasításokat alakít kódkiegészítésekké, és integrálva van a fejlesztési környezetedbe (pl. Visual Studio Code), hogy zökkenőmentes felhasználói élményt nyújtson. Az alábbi blogok sorozatában dokumentáltak szerint a legkorábbi verzió az OpenAI Codex modellen alapult – a mérnökök gyorsan felismerték a modell finomhangolásának és a jobb prompttervezési technikák kidolgozásának szükségességét a kódminőség javítása érdekében. Júliusban [bemutatták egy továbbfejlesztett AI modellt, amely túlmutat a Codexen](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), még gyorsabb javaslatok érdekében.

Olvasd el a bejegyzéseket sorrendben, hogy nyomon követhesd a tanulási folyamatukat.

- **2023. május** | [GitHub Copilot egyre jobban érti a kódodat](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023. május** | [GitHub belülről: Munka az LLM-ekkel a GitHub Copilot mögött](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023. június** | [Hogyan írjunk jobb promptokat a GitHub Copilot számára](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023. július** | [.. GitHub Copilot túlmutat a Codexen egy továbbfejlesztett AI modellel](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023. július** | [Fejlesztői útmutató a prompttervezéshez és LLM-ekhez](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023. szeptember** | [Hogyan építsünk vállalati LLM alkalmazást: Tanulságok a GitHub Copilotból](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Böngészheted az [Engineering blogjukat](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) további bejegyzésekért, például [ezt](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), amely bemutatja, hogyan alkalmazzák ezeket a modelleket és technikákat valós alkalmazások fejlesztéséhez.

---

## Prompt Felépítése

Láttuk, miért fontos a prompttervezés – most értsük meg, hogyan _épülnek fel_ a promptok, hogy értékelni tudjuk a különböző technikákat a hatékonyabb prompttervezés érdekében.

### Alapvető Prompt

Kezdjük az alapvető prompttal: egy szöveges bemenet, amelyet a modellnek küldünk, további kontextus nélkül. Íme egy példa – amikor az Egyesült Államok nemzeti himnuszának első néhány szavát elküldjük az OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) szolgáltatásának, az azonnal _kiegészíti_ a választ a következő sorokkal, bemutatva az alapvető előrejelzési viselkedést.

| Prompt (Bemenet)     | Kiegészítés (Kimenet)                                                                                                                        |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see   | Úgy tűnik, hogy az Egyesült Államok nemzeti himnuszának, a "The Star-Spangled Banner"-nek a szövegét kezded el. A teljes szöveg így hangzik... |

### Összetett Prompt

Most adjunk kontextust és utasításokat az alapvető prompthoz. A [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lehetővé teszi, hogy egy összetett promptot _üzenetek_ gyűjteményeként állítsunk össze:

- Bemenet/kimenet párok, amelyek a _felhasználói_ bemenetet és az _asszisztens_ válaszát tükrözik.
- Rendszerüzenet, amely beállítja az asszisztens viselkedésének vagy személyiségének kontextusát.

A kérés most az alábbi formában van, ahol a _tokenizálás_ hatékonyan rögzíti a kontextusból és a beszélgetésből származó releváns információkat. Most a rendszer kontextusának megváltoztatása ugyanolyan hatással lehet a kiegészítések minőségére, mint a megadott felhasználói bemenetek.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```


### Utasítás Prompt

A fenti példákban a felhasználói prompt egy egyszerű szöveges lekérdezés volt, amely információkérésként értelmezhető. Az _utasítás_ promptokkal ezt a szöveget arra használhatjuk, hogy részletesebben meghatározzuk egy feladatot, jobb iránymutatást adva az AI-nak. Íme egy példa:

| Prompt (Bemenet)                                                                                                                                                                                                                         | Kiegészítés (Kimenet)                                                                                                        | Utasítás típusa     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Írj egy leírást az amerikai polgárháborúról                                                                                                                                                                                             | _egyszerű bekezdést adott vissza_                                                                                           | Egyszerű            |
| Írj egy leírást az amerikai polgárháborúról. Adj meg kulcsfontosságú dátumokat és eseményeket, és írd le azok jelentőségét.                                                                                                             | _bekezdést adott vissza, majd kulcsfontosságú események dátumainak listáját leírásokkal_                                    | Összetett           |
| Írj egy leírást az amerikai polgárháborúról 1 bekezdésben. Adj meg 3 pontot kulcsfontosságú dátumokkal és azok jelentőségével. Adj meg további 3 pontot kulcsfontosságú történelmi személyekkel és hozzájárulásaikkal. Az eredményt JSON fájl formátumban add vissza. | _részletesebb információkat adott vissza egy szövegdobozban, JSON formátumban, amelyet másolhatsz-beilleszthetsz fájlba és validálhatsz_ | Összetett. Formázott.|

## Elsődleges Tartalom

A fenti példákban a prompt még mindig meglehetősen nyitott volt, lehetővé téve az LLM számára, hogy eldöntse, melyik része az előre betanított adatbázisának releváns. Az _elsődleges tartalom_ tervezési mintával a bemeneti szöveg két részre oszlik:

- egy utasítás (cselekvés)
- releváns tartalom (amely befolyásolja a cselekvést)

Íme egy példa, ahol az utasítás az, hogy "foglalja össze ezt 2 mondatban".

| Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Kiegészítés (Kimenet)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A Jupiter az ötödik bolygó a Naptól, és a legnagyobb a Naprendszerben. Ez egy gázóriás, amelynek tömege az ezredrésze a Napénak, de kétszer és félszer akkora, mint az összes többi bolygó tömege együttvéve. A Jupiter az egyik legfényesebb objektum, amely szabad szemmel látható az éjszakai égbolton, és az ősi civilizációk már a történelem előtti időkben is ismerték. A római Jupiter istenről nevezték el. A Földről nézve a Jupiter elég fényes lehet ahhoz, hogy visszavert fénye látható árnyékokat vessen, és átlagosan a harmadik legfényesebb természetes objektum az éjszakai égbolton a Hold és a Vénusz után. <br/> **Foglalja össze ezt 2 rövid mondatban** | A Jupiter, az ötödik bolygó a Naptól, a Naprendszer legnagyobb bolygója, és az éjszakai égbolt egyik legfényesebb objektuma. A római Jupiter istenről elnevezett gázóriás tömege kétszer és félszer nagyobb, mint az összes többi bolygó tömege együttvéve. |

Az elsődleges tartalom szegmens különböző módokon használható a hatékonyabb utasítások megfogalmazására:

- **Példák** – ahelyett, hogy kifejezett utasítást adnánk a modellnek, hogy mit tegyen, adjunk neki példákat arra, hogy mit kell tennie, és hagyjuk, hogy következtessen a mintára.
- **Célzások** – kövessük az utasítást egy "célzással", amely irányt ad a kiegészítésnek, és a modellt relevánsabb válaszok felé tereli.
- **Sablonok** – ezek ismételhető "receptjei" a promptoknak, amelyek helyőrzőket (változókat) tartalmaznak, és konkrét felhasználási esetekhez testreszabhatók.

Nézzük meg ezeket működés közben.

### Példák használata

Ez egy olyan megközelítés, amelyben az elsődleges tartalmat arra használjuk, hogy "etessük a modellt" néhány példával a kívánt kimenetről egy adott utasítás esetében, és hagyjuk, hogy következtessen a kívánt kimenet mintájára. A megadott példák számától függően lehet nulla-lövéses promptolás, egy-lövéses promptolás, néhány-lövéses promptolás stb.

A prompt most három összetevőből áll:

- Egy feladatleírás
- Néhány példa a kívánt kimenetre
- Egy új példa kezdete (amely implicit feladatleírássá válik)

| Tanulási típus | Prompt (Bemenet)                                                                                                                                        | Kiegészítés (Kimenet)         |
| :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Nulla-lövéses  | "Süt a nap". Fordítsd le spanyolra                                                                                                                    | "El Sol está brillando".    |
| Egy-lövéses    | "Süt a nap" => ""El Sol está brillando". <br> "Hideg és szeles nap van" =>                                                                            | "Es un día frío y ventoso". |
| Néhány-lövéses | A játékos körbefutotta a bázisokat => Baseball <br/> A játékos ütött egy ászt => Tenisz <br/> A játékos ütött egy hatost => Krikett <br/> A játékos zsákolt => | Kosárlabda                  |
|                |                                                                                                                                                       |                             |

Figyeld meg, hogy kifejezett utasítást kellett adni ("Fordítsd le spanyolra") a nulla-lövéses promptolásban, de ez már következtethető az egy-lövéses promptolás példájában. A néhány-lövéses példa azt mutatja, hogy több példa hozzáadása lehetővé teszi a modellek számára, hogy pontosabb következtetéseket vonjanak le további utasítások nélkül.

### Prompt Célzások

Egy másik technika az elsődleges tartalom használatára, ha _célzásokat_ adunk, nem pedig példákat. Ebben az esetben a modellnek egy olyan részletet adunk, amely tükrözi a kívánt válasz formátumát, és a modell "felveszi a fonalat", hogy ebben a stílusban folytassa.

| Célzások száma | Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Kiegészítés (Kimenet)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | A Jupiter az ötödik bolygó a Naptól, és a legnagyobb a Naprendszerben. Ez egy gázóriás, amelynek tömege az ezredrésze a Napénak, de kétszer és félszer akkora, mint az összes többi bolygó tömege együttvéve. A Jupiter az egyik legfényesebb objektum, amely szabad szemmel látható az éjszakai égbolton, és az ősi civilizációk már a történelem előtti időkben is ismerték. <br/>**Foglalja össze ezt**                                       | A Jupiter a Naprendszer legnagyobb bolygója, és az ötödik a Naptól. Ez egy gázóriás, amelynek tömege kétszer és félszer nagyobb, mint az összes többi bolygóé együttvéve, és az ősi civilizációk már régóta ismerik.                                                                                     |
| 1              | A Jupiter az ötödik bolygó a Naptól és a legnagyobb a Naprendszerben. Ez egy gázóriás, amelynek tömege az ezredrésze a Nap tömegének, de két és félszerese az összes többi bolygó tömegének együttvéve. A Jupiter az egyik legfényesebb objektum, amely szabad szemmel látható az éjszakai égbolton, és már az ősi civilizációk is ismerték a történelem előtti idők óta. <br/>**Összefoglalás** <br/> Amit megtudtunk, hogy a Jupiter | az ötödik bolygó a Naptól és a legnagyobb a Naprendszerben. Ez egy gázóriás, amelynek tömege az ezredrésze a Nap tömegének, de két és félszerese az összes többi bolygó tömegének együttvéve. Könnyen látható szabad szemmel, és már az ősi idők óta ismert.                        |
| 2              | A Jupiter az ötödik bolygó a Naptól és a legnagyobb a Naprendszerben. Ez egy gázóriás, amelynek tömege az ezredrésze a Nap tömegének, de két és félszerese az összes többi bolygó tömegének együttvéve. A Jupiter az egyik legfényesebb objektum, amely szabad szemmel látható az éjszakai égbolton, és már az ősi civilizációk is ismerték a történelem előtti idők óta. <br/>**Összefoglalás** <br/> A 3 legfontosabb tény, amit megtudtunk:         | 1. A Jupiter az ötödik bolygó a Naptól és a legnagyobb a Naprendszerben. <br/> 2. Ez egy gázóriás, amelynek tömege az ezredrésze a Nap tömegének...<br/> 3. A Jupiter szabad szemmel látható az ősi idők óta ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt sablonok

Egy prompt sablon egy _előre definiált recept egy prompthoz_, amelyet el lehet menteni és szükség esetén újra felhasználni, hogy következetesebb felhasználói élményeket érjünk el nagy léptékben. A legegyszerűbb formájában ez egyszerűen egy gyűjtemény prompt példákból, mint [ez az OpenAI-tól](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), amely tartalmazza az interaktív prompt komponenseket (felhasználói és rendszerüzenetek) és az API-alapú kérés formátumát - az újrafelhasználás támogatására.

Komplexebb formájában, mint [ez a példa LangChain-től](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), _helyettesítőket_ tartalmaz, amelyeket különböző forrásokból származó adatokkal (felhasználói bemenet, rendszerkörnyezet, külső adatforrások stb.) lehet helyettesíteni, hogy dinamikusan generáljon egy promptot. Ez lehetővé teszi, hogy létrehozzunk egy újrafelhasználható promptok könyvtárát, amelyeket programozottan lehet használni következetes felhasználói élmények elérésére nagy léptékben.

Végül, a sablonok valódi értéke abban rejlik, hogy létrehozhatunk és publikálhatunk _prompt könyvtárakat_ vertikális alkalmazási területek számára - ahol a prompt sablon most _optimalizált_ az alkalmazás-specifikus kontextus vagy példák tükrözésére, amelyek relevánsabbá és pontosabbá teszik a válaszokat a célzott felhasználói közönség számára. A [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository remek példa erre a megközelítésre, amely egy könyvtárat kurál az oktatási terület számára, hangsúlyt fektetve kulcsfontosságú célokra, mint például óratervezés, tanterv kialakítása, diákok mentorálása stb.

## Támogató tartalom

Ha a prompt konstrukciót úgy tekintjük, mint egy utasítást (feladat) és egy célt (elsődleges tartalom), akkor a _másodlagos tartalom_ olyan további kontextus, amelyet azért biztosítunk, hogy **valamilyen módon befolyásolja a kimenetet**. Ez lehet hangolási paraméterek, formázási utasítások, témakör taxonómiák stb., amelyek segítenek a modellnek _testreszabni_ a válaszát, hogy megfeleljen a kívánt felhasználói céloknak vagy elvárásoknak.

Például: Adott egy kurzuskatalógus kiterjedt metaadatokkal (név, leírás, szint, metaadat címkék, oktató stb.) az összes elérhető kurzusról a tantervben:

- meghatározhatunk egy utasítást, hogy "foglalja össze a 2023 őszi kurzuskatalógust"
- használhatjuk az elsődleges tartalmat, hogy néhány példát adjunk a kívánt kimenetre
- használhatjuk a másodlagos tartalmat, hogy azonosítsuk az 5 legfontosabb "címkét", amelyek érdekesek.

Most a modell képes lesz összefoglalót adni a példák által mutatott formátumban - de ha egy eredménynek több címkéje van, akkor prioritást adhat az 5 azonosított címkének a másodlagos tartalomban.

---

<!--
LECKE SABLON:
Ez az egység az 1. alapfogalmat kell, hogy lefedje.
Erősítse meg a fogalmat példákkal és hivatkozásokkal.

FOGALOM #3:
Prompt mérnöki technikák.
Melyek a prompt mérnöki alaptechnikák?
Mutassa be gyakorlatokkal.
-->

## Promptolási legjobb gyakorlatok

Most, hogy tudjuk, hogyan lehet promptokat _felépíteni_, elkezdhetünk gondolkodni azon, hogyan lehet őket _megtervezni_, hogy tükrözzék a legjobb gyakorlatokat. Ezt két részre oszthatjuk - a megfelelő _hozzáállás_ kialakítása és a megfelelő _technikák_ alkalmazása.

### Prompt mérnöki hozzáállás

A prompt mérnökség egy próbálgatásos folyamat, ezért három széles irányelvet tartsunk szem előtt:

1. **A terület ismerete számít.** A válasz pontossága és relevanciája az alkalmazás vagy felhasználó működési _területének_ függvénye. Alkalmazza intuícióját és területi szakértelmét, hogy **testreszabja a technikákat**. Például határozzon meg _terület-specifikus személyiségeket_ a rendszer promptjaiban, vagy használjon _terület-specifikus sablonokat_ a felhasználói promptokban. Biztosítson másodlagos tartalmat, amely tükrözi a terület-specifikus kontextusokat, vagy használjon _terület-specifikus utalásokat és példákat_, hogy a modellt a megszokott használati minták felé irányítsa.

2. **A modell ismerete számít.** Tudjuk, hogy a modellek természetüknél fogva sztochasztikusak. De a modell implementációk is eltérhetnek az általuk használt tanítási adathalmaz (előre tanított tudás), az általuk nyújtott képességek (pl. API vagy SDK révén) és az általuk optimalizált tartalom típusa (pl. kód vs. képek vs. szöveg) tekintetében. Értsük meg az általunk használt modell erősségeit és korlátait, és használjuk ezt a tudást a _feladatok prioritásának meghatározására_ vagy _testreszabott sablonok_ létrehozására, amelyek optimalizáltak a modell képességeihez.

3. **Iteráció és validáció számít.** A modellek gyorsan fejlődnek, és a prompt mérnöki technikák is. Mint területi szakértő, lehet, hogy van más kontextus vagy kritérium, amely _az Ön_ specifikus alkalmazására vonatkozik, és nem alkalmazható a szélesebb közösségre. Használja a prompt mérnöki eszközöket és technikákat a prompt konstrukció "beindítására", majd iterálja és validálja az eredményeket saját intuíciója és területi szakértelme alapján. Rögzítse meglátásait, és hozzon létre egy **tudásbázist** (pl. prompt könyvtárakat), amelyeket mások új alapként használhatnak a jövőbeli gyorsabb iterációkhoz.

## Legjobb gyakorlatok

Most nézzük meg a [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) és [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) szakemberek által ajánlott általános legjobb gyakorlatokat.

| Mi                              | Miért                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Értékelje a legújabb modelleket.       | Az új modellgenerációk valószínűleg jobb funkciókkal és minőséggel rendelkeznek - de magasabb költségekkel is járhatnak. Értékelje hatásukat, majd hozzon migrációs döntéseket.                                                                                |
| Válassza szét az utasításokat és a kontextust   | Ellenőrizze, hogy a modell/szolgáltató meghatároz-e _elválasztókat_, amelyek egyértelműbben megkülönböztetik az utasításokat, az elsődleges és másodlagos tartalmat. Ez segíthet a modelleknek pontosabban súlyozni a tokeneket.                                                         |
| Legyen specifikus és világos             | Adjon több részletet a kívánt kontextusról, eredményről, hosszúságról, formátumról, stílusról stb. Ez javítja a válaszok minőségét és következetességét. Rögzítse a recepteket újrafelhasználható sablonokban.                                                          |
| Legyen leíró, használjon példákat      | A modellek jobban reagálhatnak egy "mutasd és mondd" megközelítésre. Kezdje egy `zero-shot` megközelítéssel, ahol utasítást ad (de nincs példa), majd próbálja ki a `few-shot` finomítást, néhány példa megadásával a kívánt kimenetre. Használjon analógiákat. |
| Használjon utalásokat a válaszok beindításához | Irányítsa a kívánt eredmény felé, ha megad néhány kezdő szót vagy kifejezést, amelyeket a modell használhat a válasz kiindulópontjaként.                                                                                                               |
| Ismételje meg                       | Néha szükség lehet arra, hogy megismételje magát a modellnek. Adjon utasítást az elsődleges tartalom előtt és után, használjon utasítást és utalást stb. Iterálja és validálja, hogy mi működik.                                                         |
| A sorrend számít                     | Az információk modellnek való bemutatásának sorrendje hatással lehet a kimenetre, még a tanulási példákban is, a frissességi torzítás miatt. Próbáljon ki különböző opciókat, hogy lássa, mi működik a legjobban.                                                               |
| Adjon a modellnek egy "kibúvót"           | Adjon a modellnek egy _visszaesési_ válaszlehetőséget, amelyet akkor adhat, ha bármilyen okból nem tudja teljesíteni a feladatot. Ez csökkentheti annak esélyét, hogy a modellek hamis vagy kitalált válaszokat generáljanak.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Mint minden legjobb gyakorlat esetében, ne feledje, hogy _az Ön tapasztalata eltérhet_ a modelltől, a feladattól és a területtől függően. Használja ezeket kiindulópontként, és iterálja, hogy megtalálja, mi működik a legjobban az Ön számára. Folyamatosan értékelje újra a prompt mérnöki folyamatát, ahogy új modellek és eszközök válnak elérhetővé, a folyamat skálázhatóságára és a válaszok minőségére összpontosítva.

<!--
LECKE SABLON:
Ez az egység kódos kihívást kell, hogy tartalmazzon, ha alkalmazható

KIHÍVÁS:
Link egy Jupyter Notebookhoz, amelyben csak a kód kommentek vannak az utasításokban (a kód szekciók üresek).

MEGOLDÁS:
Link egy másolatához annak a Notebooknak, amelyben a promptok kitöltve és futtatva vannak, bemutatva, hogy egy példa hogyan nézhet ki.
-->

## Feladat

Gratulálunk! Eljutott a lecke végére! Itt az ideje, hogy néhány fogalmat és technikát teszteljen valódi példákkal!

A feladatunkhoz egy Jupyter Notebookot fogunk használni, amelyben interaktívan végezhet gyakorlatokat. A Notebookot saját Markdown és kód cellákkal is bővítheti, hogy saját ötleteket és technikákat fedezzen fel.

### Kezdéshez, forkolja a repót, majd

- (Ajánlott) Indítsa el a GitHub Codespaces-t
- (Alternatív) Klónozza a repót a helyi eszközére, és használja Docker Desktop-tal
- (Alternatív) Nyissa meg a Notebookot a preferált Notebook futtatási környezetével.

### Ezután konfigurálja a környezeti változókat

- Másolja a `.env.copy` fájlt a repo gyökerében `.env`-be, és töltse ki az `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` és `AZURE_OPENAI_DEPLOYMENT` értékeket. Térjen vissza a [Tanulási Sandbox szekcióhoz](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), hogy megtudja, hogyan.

### Ezután nyissa meg a Jupyter Notebookot

- Válassza ki a futtatási kernelt. Ha az 1-es vagy 2-es opciót használja, egyszerűen válassza ki az alapértelmezett Python 3.10.x kernelt, amelyet a fejlesztői konténer biztosít.

Minden készen áll a gyakorlatok futtatására. Ne feledje, hogy itt nincsenek _helyes vagy helytelen_ válaszok - csak opciók felfedezése próbálgatással és intuíció kialakítása arról, hogy mi működik egy adott modell és alkalmazási terület esetében.

_Ezért ebben a leckében nincsenek Kód Megoldás szegmensek. Ehelyett a Notebookban lesznek "Az én megoldásom:" című Markdown cellák, amelyek egy példa kimenetet mutatnak referenciaként._

 <!--
LECKE SABLON:
Zárja le a szekciót egy összefoglalóval és önálló tanulási forrásokkal.
-->

## Tudásellenőrzés

Melyik a jó prompt a legjobb gyakorlatok követése alapján?

1. Mutass egy képet egy piros autóról
2. Mutass egy képet egy piros autóról, amely Volvo márkájú és XC90 modell, egy szikla mellett parkolva, naplementében
3. Mutass egy képet egy piros autóról, amely Volvo márkájú és XC90 modell

A: 2, ez a legjobb prompt, mivel részleteket ad arról, hogy "mi", és specifikus (nem csak bármilyen autó, hanem egy konkrét márka és modell), valamint leírja az általános környezetet. A 3 a következő legjobb, mivel szintén sok leírást tartalmaz.

## 🚀 Kihívás

Próbálja ki, hogy használja az "utalás" technikát a következő prompttal: Fejezze be a mondatot "Mutass egy képet egy piros autóról, amely Volvo márkájú és ". Mit válaszol, és hogyan javítaná?

## Nagyszerű munka! Folytassa a tanulást

Szeretne

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.