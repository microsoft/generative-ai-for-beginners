<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-07-09T10:52:55+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "hu"
}
-->
# Prompttervezés alapjai

[![Prompttervezés alapjai](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.hu.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Bevezetés  
Ez a modul azokat az alapvető fogalmakat és technikákat tárgyalja, amelyek hatékony promptok létrehozásához szükségesek generatív AI modellek esetén. Az, hogy hogyan írod meg a promptodat egy LLM-nek, szintén számít. Egy gondosan megtervezett prompt jobb minőségű választ eredményezhet. De mit is jelentenek pontosan az olyan kifejezések, mint a _prompt_ és a _prompttervezés_? És hogyan javíthatom a prompt _bemenetet_, amit az LLM-nek küldök? Ezekre a kérdésekre próbálunk választ adni ebben és a következő fejezetben.

A _generatív AI_ képes új tartalmakat létrehozni (például szöveget, képeket, hangot, kódot stb.) a felhasználói kérésekre válaszul. Ezt olyan _Nagy Nyelvi Modellek_ segítségével éri el, mint az OpenAI GPT ("Generative Pre-trained Transformer") sorozata, amelyeket természetes nyelv és kód használatára képeztek ki.

A felhasználók most már ismerős párbeszédes formátumban léphetnek interakcióba ezekkel a modellekkel, anélkül, hogy technikai tudásra vagy képzésre lenne szükségük. A modellek _prompt-alapúak_ – a felhasználók szöveges bemenetet (promptot) küldenek, és visszakapják az AI válaszát (kiegészítést). Ezután többszörös körökben "beszélgethetnek az AI-val", finomítva a promptot, amíg a válasz megfelel az elvárásaiknak.

A "promptok" mára a generatív AI alkalmazások elsődleges _programozási felületévé_ váltak, amelyek megmondják a modelleknek, mit tegyenek, és befolyásolják a visszakapott válaszok minőségét. A "prompttervezés" egy gyorsan fejlődő tudományterület, amely a promptok _tervezésére és optimalizálására_ fókuszál, hogy következetes és minőségi válaszokat biztosítson nagy léptékben.

## Tanulási célok

Ebben a leckében megtanuljuk, mi az a prompttervezés, miért fontos, és hogyan készíthetünk hatékonyabb promptokat adott modell és alkalmazási cél esetén. Megismerjük a prompttervezés alapfogalmait és bevált gyakorlatait – valamint egy interaktív Jupyter Notebook "sandbox" környezetet, ahol ezeket a fogalmakat valós példákon keresztül láthatjuk alkalmazva.

A lecke végére képesek leszünk:

1. Elmagyarázni, mi az a prompttervezés és miért fontos.
2. Leírni egy prompt összetevőit és azok használatát.
3. Megtanulni a prompttervezés legjobb gyakorlatait és technikáit.
4. Alkalmazni a tanult technikákat valós példákon, OpenAI végpont használatával.

## Kulcsfogalmak

Prompttervezés: Az a gyakorlat, amikor bemeneteket tervezünk és finomítunk, hogy az AI modellek a kívánt kimeneteket állítsák elő.  
Tokenizáció: A szöveg kisebb egységekre, úgynevezett tokenekre bontásának folyamata, amelyet a modell képes értelmezni és feldolgozni.  
Instrukcióra hangolt LLM-ek: Olyan nagy nyelvi modellek, amelyeket specifikus utasításokkal finomhangoltak a válaszok pontosságának és relevanciájának javítása érdekében.

## Tanulási sandbox

A prompttervezés jelenleg inkább művészet, mint tudomány. A legjobb módja, hogy fejlesszük az intuíciót, ha _többet gyakorolunk_, és kipróbálásos, hibákon keresztüli megközelítést alkalmazunk, amely ötvözi az alkalmazási terület szakértelmét a javasolt technikákkal és modell-specifikus optimalizációkkal.

A lecke mellé csatolt Jupyter Notebook egy _sandbox_ környezetet biztosít, ahol kipróbálhatod, amit tanulsz – menet közben vagy a végén lévő kód kihívás részeként. A gyakorlatok végrehajtásához szükséged lesz:

1. **Egy Azure OpenAI API kulcsra** – a telepített LLM szolgáltatási végpontjához.  
2. **Egy Python futtatókörnyezetre** – amelyben a Notebook futtatható.  
3. **Helyi környezeti változókra** – _most végezd el a [BEÁLLÍTÁS](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) lépéseit, hogy készen állj_.

A notebook alapgyakorlatokat tartalmaz – de bátorítunk, hogy adj hozzá saját _Markdown_ (leírás) és _Kód_ (prompt kérések) szekciókat, hogy több példát vagy ötletet próbálhass ki, és fejleszd a prompttervezési intuíciódat.

## Illusztrált útmutató

Szeretnéd átlátni, miről szól ez a lecke, mielőtt belevágsz? Nézd meg ezt az illusztrált útmutatót, amely áttekintést ad a fő témákról és a legfontosabb tanulságokról, amelyeken érdemes elgondolkodni. A lecke útiterv végigvezet a kulcsfogalmak és kihívások megértésétől azok kezeléséig a releváns prompttervezési technikák és bevált gyakorlatok segítségével. Fontos megjegyezni, hogy az útmutató "Haladó technikák" része a tananyag _következő_ fejezetében tárgyalt tartalomra utal.

![Illusztrált útmutató a prompttervezéshez](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.hu.png)

## A startupunk

Most beszéljünk arról, hogyan kapcsolódik _ez a téma_ a startupunk küldetéséhez, hogy [AI innovációt hozzunk az oktatásba](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). AI-alapú, _személyre szabott tanulást_ támogató alkalmazásokat szeretnénk fejleszteni – gondoljuk át, hogyan "tervezhetnek" promptokat az alkalmazásunk különböző felhasználói:

- **Adminisztrátorok** kérhetik az AI-t, hogy _elemezze a tantervi adatokat, és azonosítsa a lefedetlenségeket_. Az AI összefoglalhatja az eredményeket vagy kód segítségével vizualizálhatja azokat.  
- **Oktatók** kérhetik az AI-t, hogy _készítsen tanmenetet egy célközönség és téma számára_. Az AI személyre szabott tervet állíthat össze meghatározott formátumban.  
- **Diákok** kérhetik az AI-t, hogy _segítse őket egy nehéz tantárgyban_. Az AI most már szintjükhöz igazított leckékkel, tippekkel és példákkal vezetheti őket.

Ez csak a jéghegy csúcsa. Nézd meg a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) nyílt forráskódú promptkönyvtárat, amelyet oktatási szakértők állítottak össze – hogy szélesebb képet kapj a lehetőségekről! _Próbálj ki néhány promptot a sandboxban vagy az OpenAI Playground-ban, hogy lásd, mi történik!_

<!--  
LECKE SABLON:  
Ez az egység az 1. alapfogalmat kell, hogy lefedje.  
Erősítsd meg a fogalmat példákkal és hivatkozásokkal.

ALAPFOGALOM #1:  
Prompttervezés.  
Határozd meg és magyarázd el, miért van rá szükség.  
-->

## Mi az a prompttervezés?

Ezt a leckét azzal kezdtük, hogy a **prompttervezést** úgy definiáltuk, mint a szöveges bemenetek (promptok) _tervezésének és optimalizálásának_ folyamatát, amelynek célja, hogy adott alkalmazási cél és modell esetén következetes és minőségi válaszokat (kiegészítéseket) adjon. Ezt kétlépéses folyamatként képzelhetjük el:

- az adott modell és cél számára az elsődleges prompt _megtervezése_  
- a prompt _finomítása_ iteratív módon a válasz minőségének javítása érdekében

Ez szükségszerűen egy próbálkozásos, hibákon keresztüli folyamat, amely felhasználói intuíciót és erőfeszítést igényel az optimális eredmény eléréséhez. De miért fontos ez? A válaszhoz először három fogalmat kell megértenünk:

- _Tokenizáció_ = hogyan "látja" a modell a promptot  
- _Alap LLM-ek_ = hogyan "feldolgozza" a modell az alap promptot  
- _Instrukcióra hangolt LLM-ek_ = hogyan képes a modell most már "feladatokat" értelmezni

### Tokenizáció

Egy LLM a promptokat _tokenek sorozataként_ látja, ahol különböző modellek (vagy egy modell különböző verziói) eltérő módon tokenizálhatják ugyanazt a promptot. Mivel az LLM-ek tokeneken (nem pedig nyers szövegen) tanulnak, a promptok tokenizálásának módja közvetlen hatással van a generált válasz minőségére.

Ahhoz, hogy megértsd, hogyan működik a tokenizáció, próbáld ki az olyan eszközöket, mint az alábbi [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst). Másold be a promptodat, és nézd meg, hogyan alakul át tokenekké, figyelve arra, hogyan kezeli a szóközöket és az írásjeleket. Fontos megjegyezni, hogy ez a példa egy régebbi LLM-et (GPT-3) mutat, így egy újabb modell esetén eltérő eredményt kaphatsz.

![Tokenizáció](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.hu.png)

### Fogalom: Alapmodellek

Miután a prompt tokenizálva lett, az ["Alap LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (vagy alapmodell) elsődleges feladata, hogy megjósolja a tokenek sorozatában a következő tokeneket. Mivel az LLM-ek hatalmas szöveges adatbázisokon tanultak, jól ismerik a tokenek közötti statisztikai összefüggéseket, és viszonylag magabiztosan tudják előre jelezni a következő elemet. Fontos megjegyezni, hogy nem értik a prompt vagy a tokenek _jelentését_; csupán egy mintát látnak, amelyet a következő jóslatukkal "kiegészíthetnek". A sorozatot addig folytatják, amíg a felhasználó meg nem szakítja vagy egy előre meghatározott feltétel nem teljesül.

Szeretnéd látni, hogyan működik a prompt-alapú kiegészítés? Írd be a fenti promptot az Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) felületére az alapértelmezett beállításokkal. A rendszer úgy van konfigurálva, hogy a promptokat információkérésként kezelje – így olyan választ kell kapnod, amely megfelel ennek a kontextusnak.

De mi van akkor, ha a felhasználó valami konkrétat szeretne látni, ami megfelel egy kritériumnak vagy feladatcélkitűzésnek? Itt lépnek be a képbe az _instrukcióra hangolt_ LLM-ek.

![Alap LLM chat kiegészítés](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.hu.png)

### Fogalom: Instrukcióra hangolt LLM-ek

Egy [instrukcióra hangolt LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) az alapmodellre épül, és finomhangolják példák vagy bemenet/kimenet párok (például többszörös körös "üzenetek") segítségével, amelyek egyértelmű utasításokat tartalmazhatnak – és az AI válasza megpróbálja követni ezeket az utasításokat.

Ez olyan technikákat használ, mint az emberi visszacsatoláson alapuló megerősítéses tanulás (RLHF), amely képes megtanítani a modellt az _utasítások követésére_ és a _visszajelzésekből való tanulásra_, így olyan válaszokat ad, amelyek jobban megfelelnek a gyakorlati alkalmazásoknak és relevánsabbak a felhasználói célok szempontjából.

Próbáljuk ki – térj vissza a fenti prompthoz, de most változtasd meg a _rendszerüzenetet_, hogy a következő utasítást adja meg kontextusként:

> _Foglald össze a megadott tartalmat egy másodikos diák számára. Tartsd az eredményt egy bekezdésben, 3-5 pontban._

Látod, hogy az eredmény most már a kívánt célnak és formátumnak megfelelően hangolt? Egy oktató ezt a választ közvetlenül felhasználhatja az adott óra diáiban.

![Instrukcióra hangolt LLM chat kiegészítés](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.hu.png)

## Miért van szükség prompttervezésre?

Most, hogy tudjuk, hogyan dolgozzák fel az LLM-ek a promptokat, beszéljünk arról, _miért_ van szükség prompttervezésre. A válasz abban rejlik, hogy a jelenlegi LLM-ek számos kihívást jelentenek, amelyek megnehezítik a _megbízható és következetes válaszok_ elérését anélkül, hogy erőfeszítést fektetnénk a promptok megalkotásába és optimalizálásába. Például:

1. **A modell válaszai sztochasztikusak.** Ugyanaz a prompt valószínűleg eltérő válaszokat ad különböző modelleknél vagy modellverzióknál. Sőt, ugyanazzal a modellel is különböző eredményeket kaphatunk különböző időpontokban. _A prompttervezési technikák segíthetnek minimalizálni ezeket a változásokat jobb keretek biztosításával_.

2. **A modellek képesek kitalált válaszokat adni.** A modelleket _nagy, de véges_ adathalmazokon képezték, ami azt jelenti, hogy hiányzik a tudásuk azokon a fogalmakon kívül, amelyek nem szerepelnek a tanító adatokban. Ennek eredményeként pontatlan, kitalált vagy a tényekkel ellentétes válaszokat adhatnak. _A prompttervezési technikák segítenek azonosítani és csökkenteni az ilyen kitalálásokat, például azzal, hogy az AI-t idézetek vagy érvelés megadására kérjük_.

3. **A modellek képességei eltérőek.** Az újabb modellek vagy generációk gazdagabb képességekkel rendelkeznek, de egyedi furcsaságokat és költség- illetve komplexitásbeli kompromisszumokat is hoznak. _A prompttervezés segíthet kialakítani olyan bevált gyakorlatokat és munkafolyamatokat, amelyek elvonatkoztatják a különbségeket, és zökkenőmentesen alkalmazkodnak a modell-specifikus követelményekhez nagy léptékben_.

Nézzük meg ezt a gyakorlatban
# Az 2076-os Marsi Háború tanmenete

## Bevezetés
Ebben az órában megismerkedünk az 2076-os Marsi Háborúval, amely az emberiség és a marsi kolóniák közötti konfliktus volt. Megvizsgáljuk a háború okait, főbb eseményeit és következményeit.

## Tanulási célok
- Megérteni az 2076-os Marsi Háború hátterét és kiváltó okait  
- Áttekinteni a háború főbb csatáit és stratégiai fordulópontjait  
- Elemezni a háború társadalmi és politikai hatásait az emberi civilizációra  

## Óravázlat

### 1. rész: Háttér és okok (15 perc)
- A marsi kolóniák kialakulása és fejlődése  
- Feszültségek az anyaország és a marsi telepesek között  
- Gazdasági és politikai tényezők, amelyek a konfliktushoz vezettek  

### 2. rész: A háború főbb eseményei (25 perc)
- Az első összecsapások és a háború kitörése  
- Jelentős csaták és hadműveletek  
- Technológiai újítások és fegyverek szerepe a konfliktusban  

### 3. rész: Következmények és tanulságok (20 perc)
- A háború vége és békekötés  
- A marsi társadalom átalakulása  
- Az emberiség jövője a háború után  

## Feladatok
- Csoportos vita: Milyen alternatív megoldások lehettek volna a konfliktus elkerülésére?  
- Írásbeli feladat: Fogalmazd meg, hogyan befolyásolta az 2076-os Marsi Háború a mai társadalmat!  

## Források
- Tudományos cikkek és dokumentumok az 2076-os Marsi Háborúról  
- Interaktív térképek és idővonalak  
- Videóanyagok a háború kulcsfontosságú eseményeiről  

## Megjegyzés
[!IMPORTANT] Az órán használt anyagok és források hitelességét mindig ellenőrizzük, mivel a Marsi Háború története még mindig vitatott témának számít.
Egy webes keresés során kiderült, hogy léteznek kitalált beszámolók (például tévésorozatok vagy könyvek) a marsi háborúkról – de egyetlen sem 2076-ból. A józan ész is azt mondja, hogy 2076 _a jövőben van_, így nem köthető valós eseményhez.

Mi történik, ha ezt a promptot különböző LLM szolgáltatókkal futtatjuk?

> **Válasz 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.hu.png)

> **Válasz 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.hu.png)

> **Válasz 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.hu.png)

Ahogy várható volt, minden modell (vagy modellverzió) kissé eltérő válaszokat ad a sztochasztikus viselkedés és a modell képességeinek különbségei miatt. Például az egyik modell egy 8. osztályos közönséget céloz meg, míg a másik egy középiskolás diákot feltételez. De mindhárom modell olyan válaszokat adott, amelyek meggyőzhették a tájékozatlan felhasználót arról, hogy az esemény valós.

A prompttervezési technikák, mint a _metaprompting_ és a _hőmérséklet beállítása_ bizonyos mértékig csökkenthetik a modell által generált hamis információkat. Az új prompttervezési _architektúrák_ pedig zökkenőmentesen integrálnak új eszközöket és technikákat a promptfolyamba, hogy mérsékeljék vagy csökkentsék ezeket a hatásokat.

## Esettanulmány: GitHub Copilot

Zárjuk ezt a részt azzal, hogy megismerjük, hogyan használják a prompttervezést a valós megoldásokban egy esettanulmányon keresztül: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

A GitHub Copilot az „AI páros programozód” – szöveges promptokat alakít kódjavaslatokká, és integrálva van a fejlesztői környezetedbe (például Visual Studio Code), hogy zökkenőmentes felhasználói élményt nyújtson. Az alábbi blog-sorozatban dokumentáltak szerint a legkorábbi verzió az OpenAI Codex modellen alapult – a mérnökök gyorsan felismerték, hogy szükség van a modell finomhangolására és jobb prompttervezési technikák kidolgozására a kódminőség javítása érdekében. Júliusban [bemutattak egy továbbfejlesztett AI modellt, amely túlmutat a Codexen](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), hogy még gyorsabb javaslatokat adjon.

Olvasd el a bejegyzéseket sorrendben, hogy kövesd a tanulási folyamatukat.

- **2023. május** | [A GitHub Copilot egyre jobban érti a kódodat](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023. május** | [Belső infók: a GitHub Copilot mögötti LLM-ek működése](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023. június** | [Hogyan írjunk jobb promptokat a GitHub Copilot számára](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023. július** | [GitHub Copilot túlmutat a Codexen továbbfejlesztett AI modellel](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023. július** | [Fejlesztői útmutató a prompttervezéshez és LLM-ekhez](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023. szeptember** | [Hogyan építsünk vállalati LLM alkalmazást: tanulságok a GitHub Copilotból](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Böngészhetsz továbbá a [mérnöki blogjukban](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) további bejegyzések között, mint például [ez a poszt](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), amely bemutatja, hogyan _alkalmazzák_ ezeket a modelleket és technikákat valós alkalmazások fejlesztésére.

---

<!--
TANULÁSI TÉMA:
Ez az egység a 2. alapfogalmat tárgyalja.
A fogalmat példákkal és hivatkozásokkal erősíti meg.

ALAPFOGALOM #2:
Prompt tervezés.
Példákkal illusztrálva.
-->

## Prompt felépítése

Láttuk, miért fontos a prompttervezés – most nézzük meg, hogyan _épülnek fel_ a promptok, hogy különböző technikákat értékelhessünk a hatékonyabb prompttervezés érdekében.

### Alap prompt

Kezdjük az alap prompttal: egy szöveges bemenet, amit a modellnek küldünk, más kontextus nélkül. Íme egy példa – amikor az USA nemzeti himnuszának első néhány szavát elküldjük az OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) számára, azonnal _kiegészíti_ a választ a következő sorokkal, bemutatva az alapvető előrejelző viselkedést.

| Prompt (Bemenet)     | Kiegészítés (Kimenet)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Úgy tűnik, az „The Star-Spangled Banner” (Az amerikai nemzeti himnusz) szövegét kezded el. A teljes dalszöveg így hangzik ... |

### Összetett prompt

Most adjunk kontextust és utasításokat az alap prompthoz. A [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lehetővé teszi, hogy összetett promptot építsünk fel _üzenetek_ gyűjteményeként, amelyek:

- Bemenet/kimenet párokat tartalmaznak, tükrözve a _felhasználó_ bemenetét és az _asszisztens_ válaszát.
- Rendszerüzenetet, amely beállítja az asszisztens viselkedésének vagy személyiségének kontextusát.

A kérés most az alábbi formában van, ahol a _tokenizáció_ hatékonyan ragadja meg a kontextusból és a beszélgetésből származó releváns információkat. A rendszer kontextusának megváltoztatása ugyanolyan hatással lehet a kiegészítések minőségére, mint a felhasználói bemenetek.

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

### Utasításos prompt

A fenti példákban a felhasználói prompt egyszerű szöveges kérdés volt, amit információkérésként lehetett értelmezni. Az _utasításos_ promptokkal ezt a szöveget arra használhatjuk, hogy részletesebben meghatározzunk egy feladatot, jobb iránymutatást adva az AI-nak. Íme egy példa:

| Prompt (Bemenet)                                                                                                                                                                                                                         | Kiegészítés (Kimenet)                                                                                                        | Utasítás típusa    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Írj egy leírást a polgárháborúról                                                                                                                                                                                                   | _egyszerű bekezdést adott vissza_                                                                                              | Egyszerű              |
| Írj egy leírást a polgárháborúról. Sorold fel a fontos dátumokat és eseményeket, és írd le jelentőségüket                                                                                                                                     | _bekezdést adott vissza, majd egy listát a fontos események dátumaival és leírásaival_                                             | Összetett             |
| Írj egy leírást a polgárháborúról 1 bekezdésben. Adj 3 felsorolást a fontos dátumokról és jelentőségükről. Adj még 3 felsorolást a fontos történelmi személyekről és hozzájárulásaikról. Add vissza az eredményt JSON fájlként | _szövegdobozban részletesebb információkat ad vissza, JSON formátumban, amit kimásolhatsz és fájlba menthetsz, majd ellenőrizhetsz_ | Összetett. Formázott. |

## Elsődleges tartalom

A fenti példákban a prompt még elég nyitott volt, lehetővé téve, hogy az LLM maga döntsön arról, melyik előzetesen betanított adatbázis-részlet releváns. Az _elsődleges tartalom_ tervezési mintával a bemeneti szöveget két részre osztjuk:

- egy utasításra (művelet)
- releváns tartalomra (ami befolyásolja a műveletet)

Íme egy példa, ahol az utasítás az, hogy „fogalmazd meg két mondatban”.

| Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Kiegészítés (Kimenet)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A Jupiter a Nap ötödik bolygója és a Naprendszer legnagyobb bolygója. Egy gázóriás, amelynek tömege a Nap tömegének ezredrésze, de a Naprendszer összes többi bolygójának tömegének kétszer és félszerese. A Jupiter az egyik legfényesebb égitest, amely szabad szemmel látható az éjszakai égbolton, és az ókori civilizációk már az írott történelem előtt ismerték. A római Jupiter istenről kapta a nevét.[19] A Földről nézve a Jupiter elég fényes lehet ahhoz, hogy visszavert fénye látható árnyékokat vetítsen,[20] és átlagosan az éjszakai égbolt harmadik legfényesebb természetes objektuma a Hold és a Vénusz után. <br/> **Fogalmazd meg ezt 2 rövid mondatban** | A Jupiter, a Nap ötödik bolygója, a Naprendszer legnagyobb bolygója, és az egyik legfényesebb égitest az éjszakai égbolton. A római Jupiter istenről elnevezett gázóriás tömege kétszer és félszerese az összes többi bolygó tömegének együttvéve. |

Az elsődleges tartalmi szegmens különböző módokon használható a hatékonyabb utasítások érdekében:

- **Példák** – ahelyett, hogy explicit utasítást adnánk a modellnek, mutassunk neki példákat, és hagyjuk, hogy felismerje a mintát.
- **Jelek** – az utasítást követően adjunk egy „jelet”, ami előkészíti a kiegészítést, és a modellt relevánsabb válaszok felé tereli.
- **Sablonok** – ismételhető „receptek” promptokhoz, helyőrzőkkel (változókkal), amelyeket adott adatokkal testre szabhatunk specifikus esetekhez.

Nézzük meg ezeket a gyakorlatban.

### Példák használata

Ez egy olyan megközelítés, ahol az elsődleges tartalommal „etetjük” a modellt néhány példával a kívánt kimenetre egy adott utasításhoz, és hagyjuk, hogy felismerje a mintát. A példák számától függően beszélhetünk zero-shot, one-shot, few-shot promptolásról stb.

A prompt most három részből áll:

- Egy feladatleírásból
- Néhány példából a kívánt kimenetre
- Egy új példa kezdetéből (ami implicit feladatleírássá válik)

| Tanulási típus | Prompt (Bemenet)                                                                                                                                        | Kiegészítés (Kimenet)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Fordítsd le spanyolra                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Figyeld meg, hogy a zero-shot promptolásban explicit utasítást kellett adnunk („Fordítsd le spanyolra”), míg az one-shot példában ez már kikövetkeztethető volt. A few-shot példa pedig azt mutatja, hogy több példa hozzáadásával a modellek pontosabb következtetéseket tudnak levonni anélkül, hogy további utasításokat adnánk.

### Prompt jelek

Egy másik technika az elsődleges tartalom használatára, ha _jeleket_ adunk példák helyett. Ebben az esetben a modellt egy kis „löketet” kap, egy olyan részlettel, ami tükrözi a kívánt válaszformátumot. A modell ezt a jelet követve folytatja a választ.

| Jelzések száma | Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Kiegészítés (Kimenet)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | A Jupiter a Nap ötödik bolygója és a Naprendszer legnagyobb bolygója. Egy gázóriás, amelynek tömege a Nap tömegének ezredrésze, de a Naprendszer összes többi bolygójának tömegének kétszer és félszerese. A Jupiter az egyik legfényesebb égitest, amely szabad szemmel látható az éjszakai égbolton, és az ókori civilizációk már az írott történelem előtt ismerték.

**Összefoglalás**                                       | A Jupiter a Naprendszer legnagyobb bolygója, és a Naptól számítva az ötödik. Gázóriás, amelynek tömege a Nap tömegének ezredrésze, de mégis nehezebb, mint az összes többi bolygó együttvéve. Az ókori civilizációk régóta ismerik a Jupitert, és könnyen látható az éjszakai égbolton. |
| 1              | A Jupiter a Naprendszer ötödik bolygója a Naptól, és a legnagyobb. Gázóriás, amelynek tömege a Nap tömegének ezredrésze, de az összes többi bolygó tömegének két és félszerese. A Jupiter az egyik legfényesebb égi objektum, amely szabad szemmel látható, és az ókori civilizációk már az írott történelem előtt ismerték. <br/>**Összefoglalás** <br/> Amit megtanultunk, hogy a Jupiter | a Naprendszer ötödik bolygója a Naptól, és a legnagyobb. Gázóriás, amelynek tömege a Nap tömegének ezredrésze, de az összes többi bolygó tömegének két és félszerese. Könnyen látható szabad szemmel, és már az ókor óta ismert.                        |
| 2              | A Jupiter a Naprendszer ötödik bolygója a Naptól, és a legnagyobb. Gázóriás, amelynek tömege a Nap tömegének ezredrésze, de az összes többi bolygó tömegének két és félszerese. A Jupiter az egyik legfényesebb égi objektum, amely szabad szemmel látható, és az ókori civilizációk már az írott történelem előtt ismerték. <br/>**Összefoglalás** <br/> A három legfontosabb tény, amit megtanultunk:         | 1. A Jupiter a Naprendszer ötödik bolygója a Naptól, és a legnagyobb. <br/> 2. Gázóriás, amelynek tömege a Nap tömegének ezredrésze...<br/> 3. A Jupiter már az ókor óta látható szabad szemmel ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt sablonok

A prompt sablon egy _előre meghatározott recept egy prompt számára_, amelyet el lehet tárolni és szükség szerint újra felhasználni, hogy nagyobb léptékben következetesebb felhasználói élményeket biztosítsunk. Egyszerű formájában ez csupán egy gyűjteménye a prompt példáknak, mint például [ez az OpenAI példája](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), amely tartalmazza az interaktív prompt elemeket (felhasználói és rendszerüzenetek) és az API által vezérelt kérés formátumát – a könnyebb újrafelhasználás érdekében.

Bonyolultabb formában, mint például [ez a LangChain példája](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), tartalmaz _helyőrzőket_, amelyeket különböző forrásokból (felhasználói bemenet, rendszerkörnyezet, külső adatforrások stb.) származó adatokkal lehet helyettesíteni, így dinamikusan generálható a prompt. Ez lehetővé teszi, hogy egy újrafelhasználható prompt könyvtárat hozzunk létre, amely **programozottan** képes következetes felhasználói élményeket biztosítani nagy léptékben.

Végül a sablonok valódi értéke abban rejlik, hogy képesek vagyunk _prompt könyvtárakat_ létrehozni és publikálni vertikális alkalmazási területekre – ahol a prompt sablon már _optimalizált_ az adott alkalmazási kontextus vagy példák alapján, így a válaszok relevánsabbak és pontosabbak lesznek a célzott felhasználói közönség számára. A [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) tároló kiváló példa erre a megközelítésre, amely oktatási területre fókuszáló prompt könyvtárat gyűjt össze, hangsúlyt fektetve olyan kulcscélokra, mint az óratervezés, tantervfejlesztés, diákok oktatása stb.

## Támogató tartalom

Ha a prompt felépítését úgy tekintjük, hogy van egy utasítás (feladat) és egy cél (elsődleges tartalom), akkor a _másodlagos tartalom_ olyan, mint egy további kontextus, amelyet azért adunk meg, hogy valamilyen módon **befolyásoljuk a kimenetet**. Ez lehet hangolási paraméter, formázási utasítás, témakörök taxonómiája stb., amelyek segíthetnek a modellnek, hogy a választ a kívánt felhasználói célokhoz vagy elvárásokhoz igazítsa.

Például: Adott egy kurzuskatalógus kiterjedt metaadatokkal (név, leírás, szint, metaadat címkék, oktató stb.) az összes elérhető kurzusról a tantervben:

- meghatározhatunk egy utasítást, hogy "foglalja össze a 2023 őszi kurzuskatalógust"
- az elsődleges tartalomként néhány példát adhatunk a kívánt kimenetre
- a másodlagos tartalomként megjelölhetjük az 5 legfontosabb "címkét"

Most a modell a példák által mutatott formátumban adhat összefoglalót – de ha egy eredmény több címkét is tartalmaz, akkor előnyben részesítheti a másodlagos tartalomban megjelölt 5 címkét.

---

<!--
ÓRAVÁZLAT:
Ez az egység a 1. alapfogalmat kell, hogy lefedje.
Erősítsük meg a fogalmat példákkal és hivatkozásokkal.

3. FOGALOM:
Prompt tervezési technikák.
Mik az alapvető prompt tervezési technikák?
Mutassuk be néhány gyakorlattal.
-->

## Promptolási legjobb gyakorlatok

Most, hogy tudjuk, hogyan lehet promptokat _felépíteni_, elkezdhetünk gondolkodni arról, hogyan _tervezzük_ meg őket a legjobb gyakorlatok tükrében. Ezt két részre bonthatjuk – a megfelelő _gondolkodásmód_ kialakítására és a megfelelő _technikák_ alkalmazására.

### Prompt tervezési gondolkodásmód

A prompt tervezés egy próbálkozásos folyamat, ezért tartsd szem előtt a három fő irányelvet:

1. **A domén ismerete számít.** A válasz pontossága és relevanciája attól függ, hogy az adott alkalmazás vagy felhasználó milyen _szakterületen_ működik. Használd az intuíciódat és a domén szakértelmedet, hogy tovább _testreszabhasd a technikákat_. Például definiálj _domén-specifikus személyiségeket_ a rendszer promptokban, vagy használj _domén-specifikus sablonokat_ a felhasználói promptokban. Adj meg másodlagos tartalmat, amely tükrözi a domén-specifikus kontextust, vagy használj _domén-specifikus jelzéseket és példákat_, hogy a modellt a megszokott használati minták felé tereld.

2. **A modell ismerete számít.** Tudjuk, hogy a modellek természetüknél fogva sztochasztikusak. De a modell implementációk eltérhetnek a használt tanító adathalmaz (előzetes tudás), a képességek (pl. API vagy SDK) és az optimalizált tartalomtípus (pl. kód, képek, szöveg) tekintetében is. Ismerd meg a használt modell erősségeit és korlátait, és használd ezt a tudást a _feladatok priorizálására_ vagy _testreszabott sablonok_ készítésére, amelyek a modell képességeihez igazodnak.

3. **Ismétlés és validálás számít.** A modellek gyorsan fejlődnek, és a prompt tervezési technikák is. Domén szakértőként lehet, hogy van más kontextusod vagy kritériumod a _saját_ alkalmazásodra, amely nem feltétlenül érvényes a szélesebb közösségre. Használj prompt tervezési eszközöket és technikákat a prompt felépítésének "gyors elindításához", majd ismételd és validáld az eredményeket a saját intuíciód és szakértelmed alapján. Jegyezd fel a tapasztalataidat, és hozz létre egy **tudásbázist** (pl. prompt könyvtárakat), amelyeket mások is használhatnak új alapként a gyorsabb iterációkhoz.

## Legjobb gyakorlatok

Most nézzük meg a leggyakoribb legjobb gyakorlatokat, amelyeket az [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) és az [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) szakértői ajánlanak.

| Mi                              | Miért                                                                                                                                                                                                                                               |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Értékeld a legújabb modelleket. | Az új modellgenerációk valószínűleg fejlettebb funkciókat és jobb minőséget kínálnak – de magasabb költségekkel is járhatnak. Értékeld őket hatásuk alapján, majd hozd meg a migrációs döntéseket.                                                     |
| Válaszd szét az utasításokat és a kontextust | Ellenőrizd, hogy a modell vagy szolgáltató definiál-e _elválasztókat_, amelyek egyértelműbben megkülönböztetik az utasításokat, az elsődleges és másodlagos tartalmat. Ez segíthet a modelleknek pontosabban súlyozni a tokeneket.                      |
| Legyél specifikus és világos     | Adj több részletet a kívánt kontextusról, eredményről, hosszúságról, formátumról, stílusról stb. Ez javítja a válaszok minőségét és következetességét. Rögzítsd a recepteket újrafelhasználható sablonokban.                                         |
| Legyél leíró, használj példákat | A modellek jobban reagálhatnak a "mutasd és mondd" megközelítésre. Kezdd egy `zero-shot` módszerrel, ahol csak utasítást adsz (példák nélkül), majd finomítsd `few-shot` módszerrel, néhány példa megadásával a kívánt kimenetre. Használj analógiákat. |
| Használj jelzéseket a befejezés indításához | Tereld a modellt a kívánt eredmény felé azzal, hogy adsz neki néhány vezető szót vagy kifejezést, amelyeket a válasz kezdőpontjaként használhat.                                                                                                   |
| Ismétlés                        | Néha meg kell ismételned magad a modellnek. Adj utasításokat a fő tartalom előtt és után, használj utasítást és jelzést, stb. Ismételj és validálj, hogy megtudd, mi működik.                                                                       |
| A sorrend számít                | Az információk bemutatásának sorrendje befolyásolhatja a kimenetet, még a tanulási példák esetén is, a frissességi torzítás miatt. Próbálj ki különböző lehetőségeket, hogy megtaláld a legjobbat.                                                     |
| Adj a modellnek "kimenekülési lehetőséget" | Adj a modellnek egy _tartalék_ befejezést, amelyet akkor adhat, ha valamilyen okból nem tudja teljesíteni a feladatot. Ez csökkentheti a hamis vagy kitalált válaszok esélyét.                                                                     |
|                                |                                                                                                                                                                                                                                                   |

Mint minden legjobb gyakorlat esetén, ne feledd, hogy _a te tapasztalatod eltérhet_ a modelltől, a feladattól és a doméntől függően. Használd ezeket kiindulópontként, és ismételj, hogy megtaláld, mi működik a legjobban számodra. Folyamatosan értékeld újra a prompt tervezési folyamatodat, ahogy új modellek és eszközök válnak elérhetővé, a folyamat skálázhatóságára és a válaszok minőségére fókuszálva.

<!--
ÓRAVÁZLAT:
Ez az egység kód kihívást is tartalmazhat, ha releváns.

KIHÍVÁS:
Link egy Jupyter Notebookhoz, amelyben csak a kód kommentek vannak az utasításokban (a kódrészek üresek).

MEGOLDÁS:
Link egy másolatához a Notebooknak, amelyben a promptok ki vannak töltve és lefuttatva, bemutatva egy példát.
-->

## Feladat

Gratulálunk! Eljutottál az óra végére! Itt az ideje, hogy néhány fogalmat és technikát valós példákon tesztelj!

A feladatunkhoz egy Jupyter Notebookot fogunk használni, amelyben interaktívan végezheted el a gyakorlatokat. A Notebookot saját Markdown és Kód cellákkal is bővítheted, hogy saját ötleteidet és technikáidat fedezd fel.

### Kezdéshez, forkold a repót, majd

- (Ajánlott) Indítsd el a GitHub Codespaces-t
- (Alternatív) Klónozd a repót a helyi gépedre, és használd Docker Desktop segítségével
- (Alternatív) Nyisd meg a Notebookot a kedvenc futtatókörnyezetedben.

### Ezután állítsd be a környezeti változókat

- Másold a repó gyökerében lévő `.env.copy` fájlt `.env` néven, és töltsd ki az `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` és `AZURE_OPENAI_DEPLOYMENT` értékeket. Ezután térj vissza a [Learning Sandbox szekcióhoz](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), hogy megtudd, hogyan tovább.

### Ezután nyisd meg a Jupyter Notebookot

- Válaszd ki a futtatókörnyezet kernelét. Ha az 1. vagy 2. opciót használod, egyszerűen válaszd ki az alapértelmezett Python 3.10.x kernelt, amelyet a fejlesztői konténer biztosít.

Készen állsz a gyakorlatok futtatására. Ne feledd, itt nincsenek _helyes vagy helytelen_ válaszok – csak a lehetőségek kipróbálása próbálkozás és hiba útján, valamint az intuíció építése arra, hogy mi működik egy adott modell és alkalmazási terület esetén.

_Ezért ebben az órában nincsenek Kód Megoldás szegmensek. Ehelyett a Notebookban lesznek "Az én megoldásom:" című Markdown cellák, amelyek egy példakimenetet mutatnak referencia gyanánt._

 <!--
ÓRAVÁZLAT:
Zárd le a szakaszt összefoglalóval és önálló tanulást segítő forrásokkal.
-->

## Tudásellenőrzés

Melyik az alábbiak közül egy jó prompt, amely néhány ésszerű legjobb gyakorlatot követ?

1. Mutass egy képet egy piros autóról
2. Mutass egy képet egy piros Volvo XC90 típusú autóról, amely egy szikla mellett parkol, miközben a nap lemegy
3. Mutass egy képet egy piros Volvo XC90 típusú autóról

Válasz: 2, ez a legjobb prompt, mert részletezi, hogy "mit" kérünk, és konkrétumokat is megad (nem csak bármilyen autót, hanem egy adott márkát és modellt), valamint leírja a környezetet is. A 3 a következő legjobb, mert szintén sok leírást tartalmaz.

## 🚀 Kihívás

Próbáld ki a "jelzés" technikát a következő prompttal: Fejezd be a mondatot: "Mutass egy képet egy piros Volvo típusú autór

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.