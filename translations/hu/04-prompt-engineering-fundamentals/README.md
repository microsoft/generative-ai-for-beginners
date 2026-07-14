# A Prompt Mérnökség Alapjai

[![A Prompt Mérnökség Alapjai](../../../translated_images/hu/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Bevezetés
Ez a modul az alapvető fogalmakat és technikákat tárgyalja, amelyek hatékony promptok készítéséhez szükségesek generatív MI modelleknél. Az, hogy hogyan írjuk meg a promptot egy LLM-nek, szintén számít. Egy gondosan megalkotott prompt jobb minőségű választ eredményezhet. De mit is jelentenek pontosan az olyan kifejezések, mint a _prompt_ és a _prompt mérnökség_? És hogyan javíthatom azt a prompt _bemenetet_, amit az LLM-nek küldök? Ezekre a kérdésekre próbálunk válaszokat találni ebben a fejezetben és a következőben.

_Generatív MI_ képes új tartalmat létrehozni (például szöveget, képeket, hangot, kódot stb.) a felhasználói kérésekre reagálva. Ezt _Nagy Nyelvi Modellek_ segítségével éri el, mint például az OpenAI GPT ("Generatív Előtanított Transformer") sorozat, amelyet természetes nyelv és kód használatára képeztek ki.

A felhasználók most már ismert párbeszédes formákon keresztül interakcióba léphetnek ezekkel a modellekkel, anélkül, hogy technikai szakértelem vagy képzés lenne szükséges. A modellek _prompt-alapúak_ - a felhasználók szöveges bemenetet (promptot) küldenek és AI választ (kiegészítést) kapnak vissza. Ezután többszörös fordulós beszélgetésekben "cseveghetnek az AI-val", finomítva a promptot, amíg a válasz megfelel az elvárásoknak.

A "promptok" most már a fő _programozási interfésszé_ váltak a generatív MI alkalmazásoknál, amely megmondja a modelleknek, mit tegyenek, és befolyásolja a visszakapott válaszok minőségét. A "Prompt Mérnökség" egy gyorsan fejlődő tanulmányi terület, amely a promptok _tervezésére és optimalizálására_ fókuszál, hogy következetes és minőségi válaszokat biztosítson nagy léptékben.

## Tanulási Célok

Ebben az órában megtanuljuk, mi a Prompt Mérnökség, miért fontos, és hogyan alkothatunk hatékonyabb promptokat adott modell és alkalmazási cél szempontjából. Megértjük az alapvető fogalmakat és legjobb gyakorlatokat a prompt mérnökséghez - és megismerkedünk egy interaktív Jupyter Notebook "homokozó" környezettel, ahol valós példákon láthatjuk ezeket a fogalmakat alkalmazva.

Az óra végére képesek leszünk:

1. Elmagyarázni, mi a prompt mérnökség és miért fontos.
2. Leírni egy prompt összetevőit és használatukat.
3. Megtanulni a legjobb gyakorlatokat és technikákat a prompt mérnökségben.
4. Alkalmazni a tanult technikákat valós példákon, egy OpenAI végponton keresztül.

## Kulcsfogalmak

Prompt Mérnökség: Az a gyakorlat, amely során bemeneteket terveznek és finomítanak, hogy az AI modellek kívánt kimeneteket állítsanak elő.
Tokenizáció: Az a folyamat, amikor a szöveget kisebb egységekre, úgynevezett tokenekre bontják, amelyeket egy modell megért és feldolgoz.
Utasításra Hangolt LLM-ek: Nagy Nyelvi Modellek (LLM-ek), amelyeket specifikus utasításokkal hangoltak finomra a válaszok pontosságának és relevanciájának javítása érdekében.

## Tanuló Homokozó

A prompt mérnökség jelenleg inkább művészet, mint tudomány. A legjobb módja az intuíció fejlesztésének, ha _többet gyakorolunk_, kísérletezünk, és az alkalmazási szaktudást összekapcsoljuk ajánlott technikákkal és modell-specifikus optimalizációkkal.

A tanulást segítő Jupyter Notebook mellékletében van egy _homokozó_ környezet, ahol kipróbálhatjuk, amit tanultunk - menet közben vagy a kód kihívás részeként a végén. Az gyakorlatok végrehajtásához szükséged lesz:

1. **Azure OpenAI API kulcsra** - a telepített LLM szolgáltatás végpontja.
2. **Python futtatókörnyezetre** - amelyben a Notebook futtatható.
3. **Helyi környezeti változókra** - _most végezd el a [BEÁLLÍTÁS](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) lépéseit, hogy készen állj_.

A notebook _kezdő_ feladatokat tartalmaz - de bátorítunk arra, hogy adj hozzá saját _Markdown_ (leírás) és _Kód_ (prompt kérések) részeket, hogy több példát vagy ötletet próbálj ki - és építsd tovább az intuíciódat a prompt tervezéshez.

## Illusztrált Útmutató

Szeretnéd átlátni az óra főbb témáit mielőtt belevágsz? Nézd meg ezt az illusztrált útmutatót, amely érzékelteti a fő témaköröket és a kulcsfontosságú tanulságokat, amiket érdemes átgondolni mindegyiknél. Az óra útiterv végigvezet a fogalmak és kihívások megértésén, majd ezek kezelése során bemutatja a kapcsolódó prompt mérnökségi technikákat és legjobb gyakorlatokat. Fontos megjegyezni, hogy ezen útmutató "Haladó Technikai" szakasza a _következő_ fejezet tartalmára utal.

![Illusztrált útmutató a Prompt Mérnökséghez](../../../translated_images/hu/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## A Startupunk

Most beszéljünk arról, hogy _ez a téma_ hogyan kapcsolódik startup küldetésünkhöz, amely a [MI innováció oktatásba való behozatalát célozza](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). MI-alapú, _személyre szabott tanulás_ alkalmazások fejlesztését tervezzük - ezért gondoljuk át, hogyan "tervezhetnek" promptokat az alkalmazásunk különböző felhasználói:

- **Adminisztrátorok** azt kérhetnék az AI-tól, hogy _elemezze a tantervadat, azonosítsa a lefedettség hiányosságait_. Az AI összefoglalhatja az eredményeket vagy vizualizálhatja kóddal.
- **Oktatók** arra kérhetnék az AI-t, hogy _generáljon tanmenetet egy célközönség és téma számára_. Az AI személyre szabott tervet építhet meghatározott formátumban.
- **Tanulók** arra kérhetnék az AI-t, hogy _oktatást nyújtson nehéz tárgyakban_. Az AI most már szintjükhöz igazított leckékkel, tippekkel és példákkal irányíthatja őket.

Ez csak a jéghegy csúcsa. Nézd meg a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) nyílt forráskódú prompt könyvtárat, amelyet oktatási szakértők összeállítottak, hogy átfogóbb képet kapj a lehetőségekről! _Próbáld ki ezeket a promptokat a homokozóban vagy az OpenAI Playground-ban, hogy lásd, mi történik!_

<!--
LESSON TEMPLATE:
Ez az egység az 1. alapfogalmat kell lefedje.
Erősítsd meg a fogalmat példákkal és hivatkozásokkal.

ALAPFOGALOM #1:
Prompt Mérnökség.
Határozd meg és magyarázd el, miért van rá szükség.
-->

## Mi a Prompt Mérnökség?

Ezt az órát a **Prompt Mérnökség** meghatározásával kezdtük, amely a szöveges bemenetek (promptok) _megtervezésének és optimalizálásának_ folyamata, hogy adott alkalmazási cél és modell esetén következetes és minőségi válaszokat (kiegészítéseket) adjon. Ezt két lépéses folyamatként képzelhetjük el:

- az adott modell és cél érdekében az elsődleges prompt _megtervezése_
- a prompt _finomítása_ ismételten a válasz minőségének javítására

Ez feltétlenül próbálgatós, hibákon alapuló folyamat, amely felhasználói intuíciót és erőfeszítést igényel az optimális eredmény eléréséhez. De miért fontos ez? A válaszhoz először három fogalmat kell megértenünk:

- _Tokenizáció_ = hogyan "látja" a modell a promptot
- _Alap LLM-ek_ = hogyan "feldolgozzák" a promptot az alapmodellek
- _Utasításra Hangolt LLM-ek_ = hogyan látja most már a modell a "feladatokat"

### Tokenizáció

Egy LLM úgy látja a promptokat, mint egy _tokenek sorozatát_, ahol különböző modellek (vagy egy modell különböző verziói) máshogy tokenizálhatják ugyanazt a promptot. Mivel az LLM-ek tokeneken tanulnak (nem nyers szövegen), a prompt tokenizálásának módja közvetlen hatással van a generált válasz minőségére.

Hogy értsük a tokenizáció működését, próbáld ki az alábbi [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) eszközt. Másold be a promptod, és nézd meg, hogyan alakul tokenekké, figyelve a szóközök és írásjelek kezelésére. Megjegyzés: ez a példa egy régebbi LLM-et (GPT-3) mutat, így újabb modellekkel más eredményt kaphatsz.

![Tokenizáció](../../../translated_images/hu/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Fogalom: Alapmodellek

Miután a prompt tokenizálva lett, az ["Alap LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (vagy Alapmodell) elsődleges feladata a token előrejelzése a sorozatban. Mivel az LLM-ek hatalmas szöveges adatbázison vannak betanítva, jól ismerik a tokenek közötti statisztikai összefüggéseket, és ennek alapján bizalommal tesznek jóslatokat. Fontos, hogy nem értik a promptban levő szavak _jelentését_ vagy a tokenek értelmét; csupán mintázatokat látnak, amelyeket a következő jóslattal ki tudnak egészíteni. Folytatják a sorozat előrejelzését, amíg a felhasználó meg nem szakítja vagy egy előre meghatározott feltétel nem teljesül.

Szeretnéd látni, hogyan működik a prompt-alapú kiegészítés? Írd be a fenti promptot a [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)-ba az alapértelmezett beállításokkal. A rendszer úgy van beállítva, hogy a promptokat információs kéréseknek tekintse - így olyan választ kell kapnod, ami kielégíti ezt a kontextust.

De mi van akkor, ha a felhasználó valami specifikusat akar látni, ami megfelel bizonyos feltételeknek vagy feladati célnak? Itt lépnek be a képbe az _utasításra hangolt_ LLM-ek.

![Alap LLM Chat kiegészítés](../../../translated_images/hu/04-playground-chat-base.65b76fcfde0caa67.webp)

### Fogalom: Utasításra Hangolt LLM-ek

Egy [Utasításra Hangolt LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) az alapmodellel kezd, majd finomhangolja azt példák vagy bemenet/kimenet párok (például többszörös fordulós "üzenetek") segítségével, amelyek világos utasításokat tartalmazhatnak - és az AI válasza megpróbálja követni ezt az utasítást.

Olyan technikákat alkalmaz, mint az Emberi Visszacsatolással Támogatott Megerősítéses Tanulás (RLHF), amelyek révén a modellt megtanítják _követni az utasításokat_ és _tanulni a visszajelzésekből_, hogy olyan válaszokat adjon, amelyek jobban megfelelnek a gyakorlati alkalmazásoknak és a felhasználók céljainak.

Próbáljuk ki - térj vissza a fenti prompthoz, de változtasd meg a _rendszer üzenetet_ úgy, hogy a következő utasítást adja meg kontextusként:

> _Foglald össze az adott tartalmat egy másodikos diák számára. Tartsd az eredményt egy bekezdésben 3-5 felsorolópontban._

Nézd meg, hogyan igazodik az eredmény a kívánt célhoz és formátumhoz! Egy oktató most már közvetlenül felhasználhatja ezt a választ az adott óra diáiban.

![Utasításra hangolt LLM Chat kiegészítés](../../../translated_images/hu/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Miért van szükség a Prompt Mérnökségre?

Most, hogy tudjuk, hogyan dolgozzák fel az LLM-ek a promptokat, beszéljünk arról, _miért_ van szükség a prompt mérnökségre. A válasz abban rejlik, hogy a jelenlegi LLM-ek számos kihívást jelentenek, amelyek megnehezítik a _megbízható és következetes válaszok_ elérését anélkül, hogy erőfeszítést fordítanánk a promptok összeállítására és optimalizálására. Például:

1. **A modellválaszok sztochasztikusak.** Az _ugyanaz a prompt_ valószínűleg eltérő válaszokat ad különböző modelleknél vagy model verzióknál. És akár ugyanazzal a modellel is eltérő eredmény születhet különböző alkalommal. _A prompt mérnökség technikái segíthetnek minimalizálni ezeket a változásokat, megfelelő védősávokat nyújtva_.

1. **A modellek hihető válaszokat képesek kitalálni.** A modellek előre tanítottak _nagy, de véges_ adatbázisokon, ami azt jelenti, hogy hiányzik tudásuk bizonyos fogalmakról, amelyek kívül esnek ezen a képzési körön. Ennek eredményeként pontatlan, kitalált vagy ismert tényekkel ellenkező kiegészítéseket generálhatnak. _A prompt mérnökség technikái segítenek a felhasználóknak az ilyen kitalációk felismerésében és csökkentésében, például kérve az AI-t idézetekre vagy érvelésre_.

1. **A modellek képességei eltérnek.** Az újabb modellek vagy generációk gazdagabb képességekkel rendelkeznek, de jellegzetes sajátosságokat, költségeket és összetettséget is hoznak. _A prompt mérnökség segíthet kialakítani legjobb gyakorlatokat és munkafolyamatokat, amelyek elrejtik a különbségeket és alkalmazkodnak a modell-specifikus igényekhez skálázható, zökkenőmentes módon_.

Nézzük meg ezt működés közben az OpenAI vagy Azure OpenAI Playgroundban:

- Használd ugyanazt a promptot más LLM telepítésekkel (pl. OpenAI, Azure OpenAI, Hugging Face) - láttad a különbségeket?
- Használd ugyanazt a promptot ismétlődően ugyanazon LLM telepítéssel (pl. Azure OpenAI playground) - hogyan különböztek ezek a változatok?

### Példa: Kitalációk

Ebben a tanfolyamban a **"kitaláció"** kifejezést arra használjuk, amikor az LLM-ek néha tényszerűen helytelen információkat generálnak a képzésük korlátai vagy egyéb feltételezések miatt. Ezt hallhattad már _"hallucinációknak"_ is nevezni népszerű cikkekben vagy kutatási dolgozatokban. Ugyanakkor erősen javasoljuk, hogy a _"kitaláció"_ kifejezést használjuk, hogy ne tulajdonítsunk emberi vonásokat egy gépi eredménynek. Ez megfelel a [Felelős MI irányelveknek](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst), eltávolítva azokat a kifejezéseket, amelyek sértőek vagy nem inkluzívak lehetnek bizonyos kontextusokban.

Szeretnél érzékelni, hogyan működnek a kitalációk? Gondolj egy olyan promptra, amely azt utasítja az AI-t, hogy generáljon tartalmat egy nem létező témáról (hogy biztosítsuk, hogy nincs benne a képzési adatbázisban). Például próbáltam ezt a promptot:

> **Prompt:** készíts tanmenetet a marsi háborúról 2076-ban.

Egy webes keresés alapján találtam kitalált beszámolókat (például televíziós sorozatokat vagy könyveket) a marsi háborúkról - de egyiket sem 2076-ra. Az egészséges józan ész szerint 2076 a _jövőben_ van, így nem kapcsolható valós eseményhez.


Mi történik, ha ezt a promptot különböző LLM szolgáltatókkal futtatjuk?

> **Válasz 1**: OpenAI Playground (GPT-35)

![Válasz 1](../../../translated_images/hu/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Válasz 2**: Azure OpenAI Playground (GPT-35)

![Válasz 2](../../../translated_images/hu/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Válasz 3**: : Hugging Face Chat Playground (LLama-2)

![Válasz 3](../../../translated_images/hu/04-fabrication-huggingchat.faf82a0a51278956.webp)

Ahogy várható volt, minden modell (vagy modellverzió) kissé eltérő válaszokat ad a sztochasztikus viselkedés és a modell képességeinek különbségei miatt. Például az egyik modell nyolcadikos közönségnek szól, míg a másik középiskolás diáknak feltételezi a felhasználót. De mindhárom modell olyan válaszokat adott, amelyek meggyőzhették egy tájékozatlan felhasználót arról, hogy az esemény valós volt.

A prompt-mérnökség technikái, mint a _metaprompting_ és a _temperature configuration_ részben csökkenthetik a modellek kitalációit. Az új prompt-mérnökségi _architektúrák_ is zökkenőmentesen beépítenek új eszközöket és technikákat a prompt folyamatába, hogy mérsékeljék vagy csökkentsék ezeket a hatásokat.

## Esettanulmány: GitHub Copilot

Zárjuk ezt a részt azzal, hogy betekintést nyerünk abba, hogyan használják a prompt-mérnökséget a valós megoldásokban, egy esettanulmány segítségével: a [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

A GitHub Copilot az „AI páros programozód” – a szöveges promptokat kód-kiegészítésekké alakítja át, és be van építve fejlesztőkörnyezetedbe (például Visual Studio Code), hogy zökkenőmentes felhasználói élményt nyújtson. Az alábbi blog sorozatban dokumentálták, hogy a legkorábbi verzió az OpenAI Codex modelljén alapult – a mérnökök gyorsan felismerték a modell finomhangolásának szükségességét és jobb prompt-mérnökségi technikák kidolgozását a kódminőség javítása érdekében. Júliusban bemutattak egy [fejlettebb AI modellt, amely túlmutat a Codexen](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) még gyorsabb javaslatokért.

A blogokat sorrendben olvasva követheted tanulási útjukat.

- **2023 május** | [A GitHub Copilot egyre jobban érti a kódodat](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023 május** | [Belső GitHub: A GitHub Copilot mögötti LLM-ek működéséről](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023 június** | [Hogyan írjunk jobb promptokat a GitHub Copilothoz](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023 július** | [.. A GitHub Copilot túlmutat a Codexen fejlettebb AI modellel](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023 július** | [Fejlesztői útmutató prompt-mérnökséghez és LLM-ekhez](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023 szeptember** | [Hogyan építsünk vállalati LLM alkalmazást: Tanulságok a GitHub Copilotból](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Böngészhetsz továbbá a [Mérnökségi blogjukban](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) is további bejegyzések között, mint például [ez](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), amely bemutatja, hogyan _alkalmazzák_ ezeket a modelleket és technikákat a valós alkalmazások működtetésére.

---

<!--
LESSON TEMPLATE:
Ez az egység a 2. alapkoncepciót kell, hogy lefedje.
Erősítsük meg a koncepciót példákkal és hivatkozásokkal.

KONCEPCIÓ #2:
Prompt tervezés.
Példákkal szemléltetve.
-->

## Prompt felépítése

Láttuk, miért fontos a prompt mérnökség – most nézzük meg, hogyan _épülnek fel_ a promptok, hogy értékelni tudjuk a különböző technikákat a hatékonyabb prompt tervezés érdekében.

### Alap prompt

Kezdjük az alap prompttal: egy szöveges bemenet, melyet a modellnek kontextus nélkül küldünk. Példa erre, amikor az Egyesült Államok nemzeti himnuszának első néhány szavát küldjük az OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst)-jának, amely azonnal _kiegészíti_ a választ a következő néhány sorral, szemléltetve az alapvető előrejelzési viselkedést.

| Prompt (Bemenet)   | Kiegészítés (Kimenet)                                                                                                                      |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Úgy hangzik, mintha az „The Star-Spangled Banner”, az Egyesült Államok nemzeti himnuszának szövegét kezdenéd el. A teljes dalszöveg ...        |

### Összetett prompt

Most adjunk kontextust és utasításokat az alap prompthoz. A [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lehetővé teszi, hogy összetett promptot építsünk fel _üzenetek_ gyűjteményeként, amelyek:

- Bemenet/kimenet párokat tartalmaznak, tükrözve a _felhasználó_ bemenetét és az _asszisztens_ válaszát.
- Egy rendszerüzenetet, amely beállítja az asszisztens viselkedésének vagy személyiségének kontextusát.

A kérés most az alábbi formában van, ahol a _tokenizáció_ hatékonyan rögzíti a releváns információkat a kontextusból és a beszélgetésből. A rendszer kontextusának megváltoztatása mostanra annyira befolyásolja a kiegészítések minőségét, mint a felhasználói bemenetek.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Utasítás prompt

A fenti példákban a felhasználói prompt egy egyszerű szöveges lekérdezés volt, amely információkérésként értelmezhető. Az _utasítás_ promptok esetében ezt a szöveget használhatjuk konkrét feladat részletezésére, jobb iránymutatást adva az MI-nek. Íme egy példa:

| Prompt (Bemenet)                                                                                                                                                                                                                         | Kiegészítés (Kimenet)                                                                                                        | Utasítás típusa    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Írj egy leírást a polgárháborúról                                                                                                                                                                                                    | _egyszerű bekezdést adott vissza_                                                                                          | Egyszerű            |
| Írj egy leírást a polgárháborúról. Adj meg főbb dátumokat és eseményeket, és ismertesd azok jelentőségét                                                                                                                                     | _bekezdést adott, majd kulcsfontosságú események dátumait és leírását felsoroló listát_                                    | Összetett            |
| Írj egy leírást a polgárháborúról egy bekezdésben. Adj három pontban kulcsfontosságú dátumokat és jelentőségüket. Adj további három pontot fontos történelmi személyiségekkel és hozzájárulásaikkal. Az eredményt JSON fájlként add vissza | _részletesebb válasz szövegdobozban, JSON formátumban, amit kimásolhatsz és szükség szerint ellenőrizhetsz_                 | Összetett. Formázott. |

## Elsődleges tartalom

A fenti példákban a prompt továbbra is viszonylag nyitott volt, lehetővé téve az LLM számára, hogy eldöntse, melyik előképzett adathalmaz-rész releváns. Az _elsődleges tartalom_ tervezési mintában a bemeneti szöveget két részre osztjuk:

- egy utasításra (művelet)
- egy releváns tartalomra (ami befolyásolja a végrehajtást)

Íme egy példa, ahol az utasítás a „fogalmazd meg két mondatban”.

| Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Kiegészítés (Kimenet)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A Jupiter a Nap ötödik bolygója és a Naprendszer legnagyobb bolygója. Egy gázóriás, tömege a Nap tömege ezred része, de kétszer és félszerese az összes többi bolygó tömegének együttvéve. A Jupiter az egyik legfényesebb szabad szemmel látható égitest az éjszakai égbolton, és az ősi civilizációk már az írott történelem előtt ismerték. A római Jupiter istenről nevezték el.[19] Földről nézve a Jupiter elég fényes, hogy visszavert fényével látható árnyékokat vessen,[20] és átlagosan a Hold és a Vénusz után a harmadik legfényesebb természetes objektum az éjszakai égbolton. <br/> **Fogalmazd meg két rövid mondatban** | A Jupiter, a Nap ötödik bolygója, a Naprendszer legnagyobb bolygója, és az egyik legfényesebb égitest az éjszakai égbolton. A római Jupiter istenről nevezték el; egy gázóriás, amelynek tömege kétszer és félszerese az összes többi bolygó együttes tömegének. |

Az elsődleges tartalom szegmenst különböző módon használhatjuk, hogy hatékonyabb utasításokat adjunk:

- **Példák** - ahelyett, hogy megmondanánk a modellnek egy explicit utasítással, mit tegyen, adjunk neki példákat arra, mit kell tennie, és hagyjuk, hogy kikövesse a mintát.
- **Jelek** - kövessük az utasítást egy „jellel”, ami a kiegészítést irányítja, és a modellt relevánsabb válaszok felé tereli.
- **Sablonok** - ezek ismételhető „receptek” a promptokhoz helyőrzőkkel (változókkal), amelyeket adott adatokkal személyre szabhatunk konkrét esetekhez.

Nézzük meg ezeket működés közben.

### Példák használata

Ez egy olyan megközelítés, amelynél az elsődleges tartalmat arra használjuk, hogy a modellnek adjunk néhány példát a kívánt kimenetre adott utasítás esetén, és hagyjuk, hogy kikövesse a kívánt kimenet mintáját. A megadott példák számától függően beszélünk zero-shot, one-shot, few-shot promptokról stb.

A prompt most három elemből áll:

- Egy feladat leírásából
- Néhány példából a kívánt kimenetre
- Egy új példa kezdetéből (ami implicit feladatleírássá válik)

| Tanulási típus | Prompt (Bemenet)                                                                                                                                        | Kiegészítés (Kimenet)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Fordítsd le spanyolra                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Megjegyzendő, hogy zero-shot promptolás esetén explicit utasítást kellett adnunk ("Fordítsd le spanyolra"), de one-shot példában ezt a modell már kikövetkeztette. A few-shot példa pedig megmutatja, hogy több példa hozzáadása pontosabb következtetésekhez vezet további utasítások nélkül.

### Prompt jelek

Egy másik technika az elsődleges tartalom felhasználására, ha _jeleket_ adunk példák helyett. Ebben az esetben a modellt egy kis mozdulattal indítjuk el a kívánt válasz formátum felé egy rövid részlettel. A modell ezután „veszi a jelet”, hogy ebben a stílusban folytassa.

| Jelek száma | Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Kiegészítés (Kimenet)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | A Jupiter a Nap ötödik bolygója és a Naprendszer legnagyobb bolygója. Egy gázóriás, tömege a Nap tömege ezred része, de kétszer és félszerese az összes többi bolygó tömegének együttvéve. A Jupiter az egyik legfényesebb szabad szemmel látható égitest az éjszakai égbolton, és az ősi civilizációk már az írott történelem előtt ismerték. <br/>**Összefoglalás**                                       | A Jupiter a legnagyobb bolygó a Naprendszerben és az ötödik a Naptól. Gázóriás, melynek tömege a Nap tömegének ezred része, de súlyosabb az összes többi bolygónál együttvéve. Az ősi civilizációk régóta ismerik, és könnyen látható az éjszakai égbolton..                               |
| 1              | A Jupiter a Nap ötödik bolygója és a Naprendszer legnagyobb bolygója. Egy gázóriás, tömege a Nap tömege ezred része, de kétszer és félszerese az összes többi bolygó tömegének együttvéve. A Jupiter az egyik legfényesebb szabad szemmel látható égitest az éjszakai égbolton, és az ősi civilizációk már az írott történelem előtt ismerték. <br/>**Összefoglalás** <br/> Amit megtanultunk, hogy a Jupiter | a Nap ötödik bolygója és a Naprendszer legnagyobb bolygója. Egy gázóriás, amelynek tömege a Nap tömegének ezred része, de kétszer és félszerese az összes többi bolygó tömegének együttvéve. Könnyen látható szabad szemmel, és az ősidők óta ismert.                        |

| 2              | A Jupiter a Naprendszer ötödik bolygója és a legnagyobb. Egy gázóriás, amelynek tömege a Nap tömegének ezredrésze, de a Naprendszer többi bolygójának össztömegének két és félszerese. A Jupiter az egyik legfényesebb, szabad szemmel is látható égitest az éjszakai égbolton, és ismert az ókori civilizációk óta a feljegyzett történelem előtti időkből. <br/>**Foglaljuk össze** <br/> A megtanult top 3 tény:         | 1. A Jupiter a Naprendszer ötödik bolygója és a legnagyobb. <br/> 2. Egy gázóriás, amelynek tömege a Nap tömegének ezredrésze...<br/> 3. A Jupiter már az ókor óta látható szabad szemmel ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt sablonok

A prompt sablon egy _előre meghatározott recept a promptokhoz_, amely elmenthető és szükség szerint újra felhasználható, hogy konzisztens felhasználói élményeket biztosítson nagy léptékben. Egyszerű formájában ez csupán egy gyűjtemény prompt példákból, mint például [ez az OpenAI példája](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), amely tartalmazza mind az interaktív prompt komponenseket (felhasználói és rendsz üzenetek), mind az API-n keresztüli kérés formátumát - az újrahasznosítást támogatóan.

Bonyolultabb formájában, mint [ez a LangChain példája](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), tartalmaz _helykitöltőket_, amelyeket különböző forrásokból származó adatokkal (felhasználói bemenet, rendszer kontextus, külső adatforrások stb.) lehet helyettesíteni dinamikus prompt generáláshoz. Ez lehetővé teszi újra felhasználható promptok könyvtárának létrehozását, amelyeket programozottan használhatunk konzisztens felhasználói élmények létrehozásához nagy léptékben.

Végül, a sablonok valódi értéke abban rejlik, hogy képesek vagyunk _prompt könyvtárakat_ létrehozni és publikálni vertikális alkalmazási területekre - ahol a prompt sablon most _optimalizált_ az adott alkalmazási kontextusra vagy példákra, amelyek relevánsabbá és pontosabbá teszik a válaszokat a célzott felhasználói közönség számára. A [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) tárház kiváló példa erre a megközelítésre, amely az oktatási szektorra fókuszáló prompt gyűjteményt tartalmaz kulcsfontosságú célokkal, mint óra tervezés, tanterv készítés, diákok támogatása stb.

## Támogató tartalom

Ha a prompt konstrukciót úgy tekintjük, hogy van egy instrukció (feladat) és egy cél (elsődleges tartalom), akkor a _másodlagos tartalom_ olyan, mint egy további kontextus, amelyet megadunk, hogy **valamilyen módon befolyásoljuk a kimenetet**. Ez lehet beállítási paraméter, formázási utasítás, témakör taxonómia stb., amelyek segíthetnek a modellnek a válasz _testreszabásában_, hogy megfeleljen a kívánt felhasználói elvárásoknak vagy céloknak.

Például: Adott egy kurzuskatalógus kiterjedt metaadatokkal (név, leírás, szint, metaadat címkék, oktató stb.) az összes elérhető tanfolyamról a tantervben:

- meghatározhatunk egy instrukciót, hogy "foglaljuk össze a 2023 őszi kurzuskatalógust"
- az elsődleges tartalomban néhány példát adhatunk a kívánt kimenetre
- a másodlagos tartalomban megjelölhetjük az 5 legfontosabb "címkét".

Most a modell az összefoglalót a példák formátumában adhatja meg - de ha egy eredmény több címkét tartalmaz, az elsőbbséget a másodlagos tartalomban megjelölt 5 címkének adhatja.

---

<!--
ÓRATERV SABLON:
Ez az egység az 1. fő fogalom bemutatását tartalmazza.
Erősítse meg a fogalmat példákkal és hivatkozásokkal.

FOGALOM #3:
Prompt mérnöki technikák.
Melyek az alapvető technikák a prompt mérnökséghez?
Mutassa be néhány feladattal.
-->

## Promptálási legjobb gyakorlatok

Most, hogy tudjuk, hogyan _épülnek fel_ a promptok, elkezdhetünk gondolkodni arról, hogyan _tervezzük meg_ őket, hogy tükrözzék a legjobb gyakorlatokat. Ezt két részre bonthatjuk - a helyes _gondolkodásmód_ elsajátítására és a megfelelő _technikák_ alkalmazására.

### Prompt mérnöki gondolkodásmód

A prompt mérnökség próba-szerencse alapú folyamat, ezért tartsd szem előtt három nagy vezérelvet:

1. **A doménismeret számít.** A válasz pontossága és relevanciája azon a _doménen_ múlik, amelyben az alkalmazás vagy a felhasználó működik. Használd az intuíciódat és a szakmai tapasztalatodat, hogy tovább _testreszabhasd a technikákat_. Például határozz meg _domén-specifikus személyiségeket_ a rendszer promptjaidban, vagy használj _domén-specifikus sablonokat_ a felhasználói promptokban. Adj meg olyan másodlagos tartalmat, amely domén-specifikus kontextusokat tükröz, vagy használj _domén-specifikus jelzéseket és példákat_ a modell irányításához ismerős használati minták felé.

2. **A modell ismerete számít.** Tudjuk, hogy a modellek természetüknél fogva sztochasztikusak. De a modell implementációk változhatnak a képzési adathalmaz, a képességek (pl. API vagy SDK által) és az optimalizált tartalomtípus (pl. kód vs. képek vs. szöveg) szerint is. Ismerd meg a használt modell erősségeit és korlátait, és használd ezt a tudást a _feladatok priorizálásához_ vagy _testreszabott sablonok_ építéséhez, amelyek optimalizáltak a modell képességeihez.

3. **Iteráció és validáció számít.** A modellek gyorsan fejlődnek, és a prompt mérnökség technikái is. Domén szakértőként lehet egyéb kontextusod vagy kritériumaid _saját_ alkalmazásodra, amelyek nem feltétlenül vonatkoznak az egész közösségre. Használj prompt mérnökség eszközöket és technikákat a prompt konstrukció „elindításához”, majd iterálj és validálj az intuitióddal és szakmai tapasztalatoddal. Rögzítsd az eredményeidet, és hozz létre egy **tudásbázist** (pl. prompt könyvtárakat), amely mások számára is új alapot jelenthet a gyorsabb további iterációkhoz.

## Legjobb gyakorlatok

Most nézzük meg a gyakori legjobb gyakorlatokat, amelyeket az [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) és az [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) szakemberei ajánlanak.

| Mit                              | Miért                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Értékeld a legújabb modelleket.   | Az új modell generációk valószínűleg jobb funkciókat és minőséget nyújtanak - de magasabb költséggel is járhatnak. Értékeld őket hatás alapján, majd hozd meg a migrációs döntéseket.                                                                     |
| Válaszd külön az instrukciókat és a kontextust | Ellenőrizd, hogy a modelled/szolgáltatód meghatároz-e _határolókat_ az instrukciók, elsődleges és másodlagos tartalom egyértelműbb megkülönböztetéséhez. Ez segíthet a modelleknek pontosabban súlyozni a tokeneket.                                         |
| Legyél specifikus és világos         | Adj több részletet a kívánt kontextusról, eredményről, hosszúságról, formátumról, stílusról stb. Ez javítja a válaszok minőségét és konzisztenciáját. Együttműködj az újrahasználható sablonokba foglalt receptekkel.                                     |
| Legyél leíró, használj példákat     | A modellek jobban reagálhatnak a „mutass és mondj” megközelítésre. Kezdd egy `zero-shot` megközelítéssel, ahol csak instrukciót adsz (példák nélkül), majd finomítsd `few-shot` példákkal, megadva pár példát a kívánt kimenetre. Használj analógiákat.  |
| Használj jelzéseket a válasz indításához | Tereld a választ egy kívánt irányba, ha olyan vezető szavakat vagy kifejezéseket adsz meg, amelyeket a modell válasz kezdőpontként használhat.                                                                                                         |
| Ismételd meg, ha kell              | Néha ismételni kell a modellnek az instrukciót. Adj instrukciót az elsődleges tartalom előtt és után, használj utasítást és jelzést stb. Iterálj és validálj, hogy lásd, mi működik.                                                                        |
| A sorrend számít                   | A modell számára bemutatott információk sorrendje hatással lehet a kimenetre, akár a tanulási példák esetében is, a frissességi torzítás miatt. Próbálj ki különböző variációkat, hogy megtaláld a legjobbat.                                                 |
| Adj a modellnek egy „kimenekülési” lehetőséget | Adj a modellnek egy _visszaesési_ válaszlehetőséget, amit akkor adhat, ha bármilyen okból nem tudja befejezni a feladatot. Ez csökkenti a hibás vagy kitalált válaszok lehetőségét.                                                                     |
|                                   |                                                                                                                                                                                                                                                   |

Mint minden legjobb gyakorlatnál, ne feledd, hogy _a te tapasztalatod eltérhet_ a modelltől, a feladattól és a doméntól függően. Használd ezeket kiindulópontként, és iterálj, hogy megtaláld azt, ami a legjobban működik neked. Folyamatosan értékeld újra a prompt mérnökségi folyamatodat új modellek és eszközök megjelenésekor, külön fókuszálva a folyamat skálázhatóságára és a válasz minőségére.

<!--
ÓRATERV SABLON:
Ebben az egységben, ha lehetséges, legyen kód kihívás

KIHÍVÁS:
Hivatkozás egy Jupyter Notebookra, amelyben csak kód megjegyzések vannak az utasításokban (kód szekciók üresek).

MEGOLDÁS:
Hivatkozás egy másolt Notebookra, ahol a promptok kitöltöttek és lefuttatottak, bemutatva egy példát.
-->

## Feladat

Gratulálunk! Eljutottál az óra végére! Itt az idő, hogy néhány itt tanult fogalmat és technikát valós példákon kipróbálj!

A feladat során interaktívan teljesíthető gyakorlatokat tartalmaz egy Jupyter Notebook. Kiterjesztheted a Notebookot saját Markdown és kód cellákkal, hogy önállóan fedezz fel ötleteket és technikákat.

### Kezdésként forkoljad a repo-t, majd

- (Ajánlott) Indítsd el a GitHub Codespaces-t
- (Alternatív megoldás) Klónozd le a repo-t a helyi eszközödre, és használd Docker Desktop-pal
- (Alternatív megoldás) Nyisd meg a Notebookot a kedvenc Notebook futtatókörnyezeteddel.

### Ezután állítsd be a környezeti változókat

- Másold a repo gyökérkönyvtárában lévő `.env.copy` fájlt `.env`-re, és töltsd ki az `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` és `AZURE_OPENAI_DEPLOYMENT` értékeket. Térj vissza a [Learning Sandbox szekcióhoz](#tanuló-homokozó), hogy megtudd, hogyan kell.

### Ezután nyisd meg a Jupyter Notebookot

- Válaszd ki a futtatókörnyezet kernelt. Ha az 1. vagy 2. opciót választod, egyszerűen válaszd az alapértelmezett Python 3.10.x kernt, amit a fejlesztő konténer biztosít.

Már készen állsz a gyakorlatok futtatására. Fontos megjegyezni, hogy nincsenek „helyes és helytelen” válaszok - csak a próba-szerencse próbálgatása és az intuíció építése arról, hogy mi működik egy adott modell és alkalmazási terület esetén.

_Ezért ebben az órában nincsenek Kód Megoldás szegmensek. Ehelyett a Notebookban „My Solution:” című Markdown cellák vannak, amelyek egy példakimenetet mutatnak referencia céljából._

 <!--
ÓRATERV SABLON:
Összefoglalóval és önálló tanulást támogató forrásokkal zárd le a szakaszt.
-->

## Tudásellenőrzés

Melyik a következő közül egy jó prompt, néhány reális legjobb gyakorlat betartásával?

1. Mutass egy képet egy piros autóról
2. Mutass egy képet egy piros Volvó típusú, XC90 modelltől sziklák mellett parkoló autóról, naplementével a háttérben
3. Mutass egy képet egy piros Volvó típusú, XC90 modellről

A: a 2-es a legjobb prompt, mert részletezi a „mit”, és konkrétumokat is tartalmaz (nem csak autó, hanem speciális márka és modell), továbbá leírja az általános környezetet is. A 3-as a következő legjobb, mert szintén sok leírást tartalmaz.

## 🚀 Kihívás

Próbáld meg használni a „cue” technikát a következő prompttal: „Fejezd be a mondatot: Mutass egy képet egy piros Volvó típusú autóról, amely...” Mivel válaszol, és hogyan javítanád ezt?

## Szép munka! Folytasd a tanulást

Szeretnél többet megtudni a különböző Prompt Mérnöki koncepciókról? Menj a [további tanulási oldalra](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), ahol más remek forrásokat találhatsz erről a témáról.

Lépj tovább az 5. leckére, ahol [fejlett prompt technikákat](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) nézünk meg!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->