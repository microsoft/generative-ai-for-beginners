# Prompt Mérnökség Alapjai

[![Prompt Mérnökség Alapjai](../../../translated_images/hu/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Bevezetés
Ez a modul az alapvető fogalmakat és technikákat tárgyalja, amelyek hatékony promptok létrehozásához szükségesek generatív AI modelleknél. Fontos az is, hogy miként írjuk meg a promptunkat egy nagy nyelvi modellnek (LLM). Egy gondosan megtervezett prompt jobb minőségű választ eredményezhet. De mit is jelentenek pontosan olyan kifejezések, mint a _prompt_ és a _prompt mérnökség_? Hogyan javíthatom a prompt _bemenetet_, amit az LLM-nek küldök? Ezekre a kérdésekre próbálunk választ adni ebben a fejezetben és a következőben.

A _generatív AI_ képes új tartalmakat létrehozni (például szöveg, képek, hang, kód stb.) a felhasználói kérésekre reagálva. Ezt olyan _nagy nyelvi modellekkel_ éri el, mint az OpenAI GPT ("Generative Pre-trained Transformer") sorozata, amelyeket természetes nyelv és kód feldolgozására képeztek ki.

A felhasználók most már ismerős párbeszédes módokon kommunikálhatnak ezekkel a modellekkel, technikai ismeretek vagy képzés nélkül. A modellek _prompt-alapúak_ – a felhasználók szöveges bemenetet (prompt) küldenek, és választ (kiegészítést) kapnak vissza az AI-tól. Ezután többfordulós beszélgetésekben 'beszélgethetnek az AI-val', többször finomítva a promptot, amíg a válasz megfelel az elvárásoknak.

A "promtok" most már a generatív AI alkalmazások elsődleges _programozási interfészévé_ váltak, mondják meg a modelleknek, mit tegyenek, és befolyásolják a visszakapott válaszok minőségét. A "Prompt Mérnökség" egy gyorsan növekvő tudományterület, amely a promptok _tervezésére és optimalizálására_ összpontosít annak érdekében, hogy konzisztens és minőségi válaszokat nyújtson nagyszabásúan.

## Tanulási Célok

Ebben az órában megismerjük, mi a Prompt Mérnökség, miért fontos, és hogyan készíthetünk hatékonyabb promptokat egy adott modellhez és alkalmazási célhoz. Megértjük a prompt mérnökség alapfogalmait és bevált gyakorlatait – és megismerkedünk egy interaktív Jupyter jegyzetfüzet "sandbox" környezettel, ahol ezek a fogalmak valós példákon alkalmazhatók.

A tananyag végére képesek leszünk:

1. Elmagyarázni, mi a prompt mérnökség és miért fontos.
2. Leírni egy prompt összetevőit és azok használatát.
3. Megtanulni a prompt mérnökség legjobb gyakorlatait és technikáit.
4. Alkalmazni a tanult technikákat valós példákon, OpenAI végponton keresztül.

## Kulcsfogalmak

Prompt Mérnökség: A bemenetek tervezésének és finomításának gyakorlata, amelynek segítségével az AI modellek a kívánt kimenetek előállítására irányíthatók.  
Tokenizáció: A szöveg kisebb egységekre, úgynevezett tokenekre bontásának folyamata, amelyet a modell képes értelmezni és feldolgozni.  
Instrukcióval Finomhangolt LLM-ek: Olyan nagy nyelvi modellek, amelyeket speciális utasításokkal finomhangoltak a válaszok pontosságának és relevanciájának javítása érdekében.

## Tanulási Sandbox

A prompt mérnökség jelenleg inkább művészet, mint tudomány. A legjobb módja az intuíció fejlesztésének a _több gyakorlás_, valamint egy próbálkozás-alapú megközelítés alkalmazása, amely ötvözi az alkalmazási terület szakértelmét a javasolt technikákkal és modell-specifikus optimalizációkkal.

A tananyaghoz tartozó Jupyter jegyzetfüzet egy _sandbox_ környezetet biztosít, ahol kipróbálhatod, amit tanultál – menet közben vagy a végén található kód kihívás részeként. Az óragyakorlathoz szükséged lesz:

1. **Egy Azure OpenAI API kulcsra** – a telepített LLM szolgáltatás végpontjára.  
2. **Egy Python futtatókörnyezetre** – ahol a jegyzetfüzet futtatható.  
3. **Lokális környezeti változókra** – _a [BEÁLLÍTÁS](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) lépéseit most végezd el_, hogy kész legyél.

A jegyzetfüzet _kezdő_ feladatokat is tartalmaz – de arra bátorítunk, hogy adj hozzá saját _Markdown_ (leírás) és _Kód_ (prompt kérések) részeket, hogy több példát vagy ötletet próbálhass ki, és fejleszd a prompt tervezési intuíciódat.

## Illusztrált Útmutató

Szeretnéd az első pillantásra átlátni, miről szól ez az óra? Nézd meg ezt az illusztrált útmutatót, amely áttekintést ad a fő témakörökről és a legfontosabb tanulságokról, amelyekre érdemes odafigyelni. A tananyagtérkép végigvezet az alapfogalmak és kihívások megértésétől a prompt mérnökség releváns technikáinak és bevált gyakorlataival történő megoldásokig. Megjegyzendő, hogy az „Haladó Technikusok” szakasz ebben az útmutatóban a tananyag _következő_ fejezetében tárgyalt tartalmakra utal.

![Prompt Mérnökség Illusztrált Útmutató](../../../translated_images/hu/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Startupunk

Beszéljünk most arról, hogyan kapcsolódik _ez a téma_ az oktatáshoz kapcsolódó startup-missziónkhoz, amely az [AI innováció oktatásba való behozatalát](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst) célozza. Olyan AI-alapú alkalmazásokat kívánunk építeni, amelyek a _személyre szabott tanulást_ támogatják – gondolkodjunk együtt azon, hogy miként tervezhetnek promptokat az alkalmazásunk különböző felhasználói:

- **Adminisztrátorok** AI-t kérhetnek arra, hogy _elemzze a tantervi adatokat a lefedettségi hiányosságok azonosításához_. Az AI összegzi az eredményeket vagy kód segítségével vizualizációt készít.
- **Oktatók** AI-t kérhetnek, hogy _készítsen tanmenetet egy célzott közönségnek és témakörnek_. Az AI megépíti a személyre szabott tervet egy meghatározott formátumban.
- **Tanulók** AI-t kérhetnek, hogy _segítse őket egy nehéz tantárgyban_. Az AI most már a tanulók szintjére szabott leckékkel, tippekkel és példákkal vezetheti őket.

Ez csak a jéghegy csúcsa. Nézd meg a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) nyílt forráskódú prompt-könyvtárat, amelyet oktatási szakértők válogattak össze, hogy szélesebb körű képet kapj a lehetőségekről! _Próbáld ki valamelyiket a sandboxban vagy az OpenAI Playgroundon, hogy lásd, mi történik!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Mi az a Prompt Mérnökség?

A leckét úgy kezdtük, hogy a **Prompt Mérnökséget** definiáltuk, mint a szöveges bemenetek (promptok) _megtervezésének és optimalizálásának_ folyamatát, amely konzisztens és minőségi válaszokat (kiegészítéseket) eredményez egy adott alkalmazási cél és modell esetében. Ezt kétlépéses folyamatként is elképzelhetjük:

- az elsődleges prompt _megtervezése_ adott modell és cél számára  
- a prompt _finomítása_ iteratívan, a válasz minőségének javítása érdekében

Ez szükségszerűen próbálkozás-alapú folyamat, amely felhasználói intuíciót és erőfeszítést igényel az optimális eredmény eléréséhez. De miért fontos ez? Ahhoz, hogy ezt megértsük, három fogalmat kell előbb felfognunk:

- _Tokenizáció_ = hogyan "látja" a modell a promptot  
- _Alap LLM-ek_ = hogyan "feldolgozza" az alapmodell a promptot  
- _Instrukcióval Finomhangolt LLM-ek_ = hogyan láthatja most a modell a "feladatokat"  

### Tokenizáció

Az egy LLM a promptokat _token sorozatként_ kezeli, ahol különböző modellek (vagy verziók) ugyanazt a promptot különböző módokon tokenizálhatják. Mivel az LLM-ek tokeneken vannak kiképezve (nem nyers szövegen), a promptok tokenizációjának módja közvetlenül befolyásolja a generált válaszok minőségét.

Az intuíció fejlesztéséhez, hogy hogyan működik a tokenizáció, próbáld ki az olyan eszközöket, mint az [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) lent. Illeszd be a promptodat, és nézd meg, hogyan alakul át tokenekké, figyelve arra, hogyan kezeli a szóközöket és írásjeleket. Fontos megjegyezni, hogy ez a példa egy régebbi LLM-et (GPT-3) mutat, ezért újabb modellekkel más eredményt kaphatsz.

![Tokenizáció](../../../translated_images/hu/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Fogalom: Alapmodellek

Ha a prompt tokenizálva van, az ["Alap LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (vagy Foundation modell) elsődleges funkciója ezeknek a tokeneknek a következő elemzés szerinti előrejelzése. Mivel az LLM-ek hatalmas szövegadat-készleteken vannak kiképezve, jól értik a tokenek közti statisztikai összefüggéseket, és egy bizonyos biztonsággal képesek megjósolni a következő tokent. Meg kell jegyezni, hogy nem értik a prompt vagy token szavainak _jelentését_; csak látnak egy mintát, amelyet a következő előrejelzésükkel "kiegészítenek". A sorozatot folytathatják, amíg a felhasználó be nem avatkozik, vagy valamilyen előre meghatározott feltétel meg nem állítja őket.

Szeretnéd látni, hogyan működik a prompt alapú válasz? Írd be a fenti promptot az Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) alapértelmezett beállításai mellett. A rendszer úgy van konfigurálva, hogy a promptokat információkérésekként kezelje – így olyan választ kell kapnod, amely megfelel ennek a kontextusnak.

De mi van, ha a felhasználó valami konkrétat akar látni, ami megfelel egy kritériumnak vagy feladatcélkitűzésnek? Itt jönnek képbe az _instrukcióval finomhangolt_ LLM-ek.

![Alap LLM Chat Válasz](../../../translated_images/hu/04-playground-chat-base.65b76fcfde0caa67.webp)

### Fogalom: Instrukcióval Finomhangolt LLM-ek

Egy [Instrukcióval Finomhangolt LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) az alapmodellel kezd, majd példák vagy bemenet/kimenet párok (például többszörös fordulós "üzenetek"), amelyekben tiszta utasítások vannak, segítségével finomhangolja azt – és az AI válasza megpróbálja követni az adott instrukciót.

Ehhez olyan technikákat alkalmaznak, mint az Emberi Visszacsatolásos Megerősítéses Tanulás (RLHF), amely képes megtanítani a modellt, hogy _kövesse az utasításokat_ és _tanuljon a visszajelzésekből_, így olyan válaszokat ad, amelyek jobban illeszkednek a gyakorlati alkalmazásokhoz és relevánsabbak a felhasználói célok szempontjából.

Próbáljuk ki – térj vissza a fenti prompthoz, de most változtasd meg a _rendszerüzenetet_, hogy a következő utasítást tartalmazza kontextusként:

> _Foglald össze a megadott tartalmat egy második osztályos diáknak. Tartsd az eredményt egy bekezdésben, 3-5 felsorolási ponttal._

Látod, hogyan hangolódik most az eredmény a kívánt célra és formátumra? Egy oktató most már közvetlenül felhasználhatja ezt a választ a tanórájának diáin.

![Instrukcióval Finomhangolt LLM Chat Válasz](../../../translated_images/hu/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Miért van szükség Prompt Mérnökségre?

Most, hogy tudjuk, hogyan dolgozzák fel az LLM-ek a promptokat, beszéljünk arról, _miért_ van szükség prompt mérnökségre. A válasz abban rejlik, hogy a jelenlegi LLM-ek számos kihívást jelentenek, amelyek megnehezítik a _megbízható és konzisztens kiegészítések_ elérését anélkül, hogy időt és energiát szánnánk a promptok megalkotására és optimalizálására. Például:

1. **A modell válaszai sztochasztikusak.** Ugyanazzal a _promttal_ valószínűleg különböző válaszokat kapsz különböző modelleken vagy modellverziókon. Még ugyanazzal a _modellel_ is eltérő eredmények születhetnek különböző alkalommal. _A prompt mérnökség technikái segítenek minimalizálni ezeket a változásokat jobb keretek biztosításával_.

2. **A modellek képesek téves válaszokat gyártani.** A modelleket _nagy, de véges_ adatkészleteken képezik, így hiányozhatnak náluk olyan ismeretek, amelyek a képzésen kívüli fogalmakra vonatkoznak. Ennek eredményeként pontatlan, képzeletbeli, vagy a tényekkel ellentétes kiegészítéseket állíthatnak elő. _A prompt mérnökség segít azonosítani és mérsékelni az ilyen téves információkat, például azzal, hogy az AI-t idézetek vagy érvelés megadására kérjük_.

3. **A modellek képességei változóak.** Az újabb modellek vagy generációk gazdagabb képességekkel rendelkeznek, de sajátos sajátosságokat és kompromisszumokat is hoznak költségek és összetettség tekintetében. _A prompt mérnökség segít kialakítani a legjobb gyakorlatokat és munkafolyamatokat, amelyek elvonják a különbségeket, és alkalmazkodnak a modell-specifikus követelményekhez nagyszabásúan és zökkenőmentesen_.

Nézzük meg mindezt az OpenAI vagy Azure OpenAI Playgroundban:

- Használd ugyanazt a promptot különböző LLM telepítéseknél (például OpenAI, Azure OpenAI, Hugging Face) – észrevetted a különbségeket?  
- Használd ugyanazt a promptot többször ugyanazzal az LLM telepítéssel (például Azure OpenAI playground) – hogyan változtak ezek az eredmények?

### Téves Információk Példája

Ebben a tanfolyamban a **"téves információk gyártása"** (fabrication) kifejezést használjuk arra a jelenségre, amikor az LLM-ek néha valótlan információkat generálnak a képzésük korlátai vagy egyéb tényezők miatt. Ezt gyakran nevezik _"hallucinációnak"_ a népszerű cikkekben vagy kutatásokban. Ugyanakkor erősen javasoljuk, hogy használjuk a _"fabrication"_ kifejezést, hogy elkerüljük a viselkedés emberi tulajdonsággal való téves azonosítását. Ez összhangban áll a [Felelős AI irányelvekkel](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst), eltávolítva az olyan kifejezéseket, amelyek bizonyos kontextusokban sértőnek vagy nem befogadónak tekinthetők.

Szeretnéd látni, hogyan működnek a téves információk? Gondolj egy olyan promptra, amely arra utasítja az AI-t, hogy egy nem létező témáról generáljon tartalmat (hogy az ne legyen benne a képzési adathalmazban). Például – ezt a promptot próbáltam:

> **Prompt:** készíts tanmenetet a 2076-os Marsi Háborúról.
Egy webes keresés azt mutatta, hogy léteznek fiktív beszámolók (pl. tévésorozatok vagy könyvek) a marsi háborúkról – de egyik sem 2076-ban. Az egészséges ész azt is mondja, hogy 2076 _a jövőben_ van, így nem köthető valós eseményhez.

Szóval mi történik, ha ezt a promptot különböző LLM szolgáltatókkal futtatjuk?

> **Válasz 1**: OpenAI Playground (GPT-35)

![Válasz 1](../../../translated_images/hu/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Válasz 2**: Azure OpenAI Playground (GPT-35)

![Válasz 2](../../../translated_images/hu/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Válasz 3**: : Hugging Face Chat Playground (LLama-2)

![Válasz 3](../../../translated_images/hu/04-fabrication-huggingchat.faf82a0a51278956.webp)

Ahogy várható volt, minden modell (vagy modellverzió) kissé eltérő válaszokat ad a sztochasztikus viselkedés és a modell képességei különbségei miatt. Például az egyik modell egy 8. osztályos közönséget céloz meg, míg a másik egy gimnazista diákra számít. De mindhárom modell generált válaszokat, amelyek meggyőzőek lehetnek egy tájékozatlan felhasználó számára, hogy az esemény valós volt.

A prompt-tervezési technikák, mint a _metaprompting_ és a _hőmérséklet konfigurálása_ bizonyos mértékig csökkenthetik a modell hibás állításait. Új prompt-tervezési _architektúrák_ szintén zökkenőmentesen integrálnak új eszközöket és technikákat a prompt folyamatába, hogy mérsékeljék vagy csökkentsék ezen hatásokat.

## Esettanulmány: GitHub Copilot

Zárjuk ezt a részt azzal, hogy megértjük, milyen módon használják a prompt-tervezést a valós megoldásokban egy esettanulmány segítségével: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

A GitHub Copilot az "AI páros programozód" – szöveges promptokat kód-kiegészítésé alakít át, és integrálva van a fejlesztői környezetedbe (pl. Visual Studio Code), hogy zökkenőmentes felhasználói élményt nyújtson. Az alábbi blogcikk-sorozatban dokumentált módon az első verzió az OpenAI Codex modellre épült – a mérnökök gyorsan felismerték a szükségét a finomhangolásnak és jobb prompt-tervezési eljárások fejlesztésének a kódminőség javítása érdekében. Júliusban [bemutatták a Codex-en túlmutató fejlettebb AI modellt](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) a még gyorsabb javaslatokért.

Olvasd el a bejegyzéseket sorrendben, hogy nyomon kövesd tanulási útjukat.

- **2023. május** | [A GitHub Copilot jobb abban, hogy megértse a kódodat](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023. május** | [A GitHub belsejében: Működés az LLM-ekkel a GitHub Copilot mögött](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023. június** | [Hogyan írjunk jobb promptokat a GitHub Copilothoz](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023. július** | [.. A GitHub Copilot túlmutat a Codexen fejlettebb AI modellel](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023. július** | [Fejlesztői útmutató a prompt-tervezéshez és az LLM-ekhez](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023. szeptember** | [Hogyan építsünk vállalati LLM alkalmazást: Tanulságok a GitHub Copilot-tól](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Továbbá böngészheted a [mérnöki blogjukat](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) további bejegyzésekért, mint például [ez a poszt](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), amely megmutatja, hogyan _alkalmazzák_ ezeket a modelleket és technikákat valós alkalmazások előmozdítására.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Prompt Készítése

Már láttuk, miért fontos a prompt-tervezés – most pedig értsük meg, hogyan _épülnek fel_ a promptok, hogy értékelhessük a különböző technikákat a hatékonyabb prompt tervezés érdekében.

### Alapvető Prompt

Kezdjük az alapvető prompttal: egy szöveges bemenet, amit a modellnek küldünk, más kontextus nélkül. Íme egy példa – amikor elküldjük az USA himnuszának első néhány szavát az OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) számára, a modell azonnal _kiegészíti_ a választ a következő néhány sorral, illusztrálva a alapvető előrejelzési viselkedést.

| Prompt (Bemenet)     | Befejezés (Kimenet)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Úgy hangzik, mintha az „The Star-Spangled Banner” (Az Amerikai Himnusz) dalszövegét kezdenéd el, az Egyesült Államok nemzeti himnuszát. A teljes dalszöveg ... |

### Összetett Prompt

Most adjunk kontextust és utasításokat ehhez az alapvető prompthoz. A [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lehetővé teszi összetett promptok összeállítását _üzenetek_ gyűjteményeként, ahol:

- Bemenet/kimenet párok tükrözik a _felhasználó_ bemenetét és az _asszisztens_ válaszát.
- Rendszerüzenet állítja be az asszisztens viselkedésének vagy személyiségének kontextusát.

A kérés most az alábbi formában van, ahol a _tokenizáció_ hatékonyan rögzíti a kontextusból és a beszélgetésből származó releváns információkat. Ezért a rendszer kontextusának megváltoztatása éppoly befolyásoló lehet a kimenetek minőségére, mint a felhasználó által adott bemenetek.

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

### Utasításos Prompt

A fenti példákban a felhasználói prompt egyszerű szöveges kérdés volt, amit információkéréssé lehetett értelmezni. Az _utasításos_ promptokkal ezt a szöveget a feladat részletesebb meghatározására használhatjuk, jobb iránymutatást adva a mesterséges intelligenciának. Íme egy példa:

| Prompt (Bemenet)                                                                                                                                                                                                                         | Befejezés (Kimenet)                                                                                                        | Utasítás Típusa    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Írj egy leírást a polgárháborúról                                                                                                                                                                                                       | _egyszerű bekezdést adott vissza_                                                                                           | Egyszerű            |
| Írj egy leírást a polgárháborúról. Add meg a fontos dátumokat és eseményeket, illetve ismertesd ezek jelentőségét                                                                                                                                     | _bekezdést adott, majd felsorolásban kulcseseményeket magyarázatokkal_                                                      | Összetett           |
| Írj egy leírást a polgárháborúról 1 bekezdésben. Adj 3 pontba foglalt kulcsfontosságú dátumot és jelentőséget. Adj még 3 pontot fontos történelmi személyekről és hozzájárulásaikról. Add vissza JSON fájl formátumban | _részletesebb, JSON formátumú szöveget ad vissza, ami másolható, fájlba illeszthető és ellenőrizhető_                         | Összetett. Formázott.|

## Elsődleges Tartalom

A fenti példákban a prompt még eléggé nyitott volt, lehetővé téve, hogy az LLM maga döntsön arról, hogy a tanított adathalmazából mi releváns. Az _elsődleges tartalom_ tervezési mintával a bemeneti szöveg két részre oszlik:

- egy utasításra (cselekvésre)
- releváns tartalomra (ami befolyásolja a cselekvést)

Íme egy példa, ahol az utasítás így szól: „foglald össze két mondatban”.

| Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Befejezés (Kimenet)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A Jupiter a Nap ötödik bolygója és a Naprendszer legnagyobbja. Egy gázóriás, amelynek tömege a Nap tömegének ezredrésze, de a Naprendszer összes többi bolygójának tömegének kétszer és fél szerese. A Jupiter az egyik legfényesebb égitest, amely szabad szemmel látható az éjszakai égbolton, és az ókori civilizációk már a történelmi idők előtt ismerték. A római Jupiter istenről kapta a nevét.[19] Földről nézve a Jupiter elég fényes lehet ahhoz, hogy visszavert fénye látható árnyékokat vetítsen,[20] és átlagosan a Hold és a Vénusz után a harmadik legfényesebb természetes égi objektum az éjszakai égbolton. <br/> **Foglalja össze két rövid mondatban** | A Jupiter, a Nap ötödik bolygója, a Naprendszer legnagyobb bolygója, és az éjszakai égbolt egyik legfényesebb égi objektuma. Római istenről, Jupiterről kapta a nevét, és egy gázóriás, amelynek tömege a többi bolygó tömegének kétszer és fél szerese együttesen. |

Az elsődleges tartalom szegmens többféleképpen használható a hatékonyabb utasítások meghajtására:

- **Példák** – ahelyett, hogy a modellnek expliciten mondanánk meg, mit tegyen, adjunk neki példákat a kívánt feladatra, és hagyjuk, hogy felismerje a mintát.
- **Eszközök** – kövessük az utasítást egy „jelzéssel”, amely beindítja a kimenetet, irányítva a modellt relevánsabb válaszokra.
- **Sablonok** – ismételhető „receptek” promptokhoz, helyőrzőkkel (változókkal), amiket az adott adatokhoz igazítva testre lehet szabni.

Nézzük meg ezeket a gyakorlatban.

### Példák Használata

Ez egy olyan megközelítés, amikor az elsődleges tartalommal „etetjük meg” a modellt a kívánt kimenet néhány példájával egy adott utasításhoz, és hagyjuk, hogy felismerje a mintát. A példák száma alapján lehet zero-shot promptolás, one-shot promptolás, few-shot promptolás stb.

A prompt most három részből áll:

- Egy feladat leírásából
- A kívánt kimenet néhány példájából
- Egy új példa kezdetéből (ami implicit feladatleírásként szolgál)

| Tanulási Típus | Prompt (Bemenet)                                                                                                                                        | Befejezés (Kimenet)       |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------- |
| Zero-shot     | „The Sun is Shining”. Fordítsd le spanyolra                                                                                                            | „El Sol está brillando”.    |
| One-shot      | „The Sun is Shining” => „El Sol está brillando”. <br> „It's a Cold and Windy Day” =>                                                                 | „Es un día frío y ventoso”. |
| Few-shot      | A játékos megfutotta az alapokat => Baseball <br/> A játékos ászt ütött => Tenisz <br/> A játékos hatost ütött => Krikett <br/> A játékos zsákolt => | Kosárlabda                |
|               |                                                                                                                                                       |                            |

Figyeld meg, hogy a zero-shot promptolásban precíz utasítást kellett adni („Fordítsd le spanyolra”), míg az one-shot példa ezt implicit módon tartalmazza. A few-shot példában az egyre több példa lehetővé teszi a modellek számára, hogy vizsgált minták alapján pontosabb következtetéseket vonjanak le utasítás nélkül.

### Prompt Jelzések

Egy másik megközelítés az elsődleges tartalom használatára az, ha _jelzéseket_ adunk, nem pedig példákat. Ebben az esetben egy kis részlettel _indítjuk el_ a modellt, ami visszatükrözi a kívánt válasz formátumát. A modell „megérti a jelet”, és folytatja azt az irányt.

| Jelzések száma | Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Befejezés (Kimenet)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | A Jupiter a Nap ötödik bolygója és a Naprendszer legnagyobbja. Egy gázóriás, amelynek tömege a Nap tömegének ezredrésze, de a Naprendszer összes többi bolygójának tömegének kétszer és fél szerese. A Jupiter az egyik legfényesebb égitest, amely szabad szemmel látható az éjszakai égbolton, és az ókori civilizációk már a történelmi idők előtt ismerték. <br/>**Foglalja össze**                                       | A Jupiter a Naprendszer legnagyobb bolygója és a Nap ötödik bolygója. Egy gázóriás, melynek tömege a Nap tömegének 1/1000-e, de nehezebb, mint az összes többi bolygó együttesen. Az ókori civilizációk régóta ismerik, és könnyen látható az éjszakai égbolton. |
| 1              | A Jupiter az ötödik bolygó a Naptól és a Naprendszer legnagyobb bolygója. Gázevő óriás, amelynek tömege ezered része a Napénak, de más összes bolygó tömegének két és félszerese. A Jupiter a legfényesebb szabad szemmel látható égi objektumok egyike éjszaka, és az ókori civilizációk óta ismert, még az írott történelem előttről. <br/>**Összefoglalás** <br/> Amit megtanultunk, hogy a Jupiter | az ötödik bolygó a Naptól és a Naprendszer legnagyobb bolygója. Gázevő óriás, amelynek tömege ezered része a Napénak, de más bolygók össztömegének két és félszerese. Könnyen látható szabad szemmel, és ősidők óta ismert.                        |
| 2              | A Jupiter az ötödik bolygó a Naptól és a Naprendszer legnagyobb bolygója. Gázevő óriás, amelynek tömege ezered része a Napénak, de más összes bolygó tömegének két és félszerese. A Jupiter a legfényesebb szabad szemmel látható égi objektumok egyike éjszaka, és az ókori civilizációk óta ismert, még az írott történelem előttről. <br/>**Összefoglalás** <br/> A legfontosabb 3 tény amit megtanultunk:         | 1. A Jupiter az ötödik bolygó a Naptól és a Naprendszer legnagyobb bolygója. <br/> 2. Gázevő óriás, amelynek tömege ezered része a Napénak...<br/> 3. A Jupiter szabad szemmel látható az ősidők óta ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt sablonok

A prompt sablon egy _előre megadott recept egy prompt számára_, amit tárolhatunk és szükség szerint újra felhasználhatunk, hogy skálázhatóbb és konzisztens felhasználói élményt nyújtsunk. Egyszerű formájában ez egyszerűen egy promptpéldák gyűjteménye, mint [ez itt az OpenAI-tól](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), amely interaktív prompt összetevőket (felhasználó és rendszerüzenetek) és az API hívás formátumát is tartalmazza - az újrafelhasználhatóság támogatására.

Bonyolultabb formában, mint [ez az példa a LangChain-től](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), helyőrzőket tartalmaz, amelyeket különböző forrásokból származó adatokkal (felhasználói bemenet, rendszerkörnyezet, külső adatok stb.) dinamikusan cserélhetünk ki. Ez lehetővé teszi egy újrafelhasználható promptkönyvtár létrehozását, amely programozottan, nagyobb szabásban támogatja a konzisztens felhasználói élmények megvalósítását.

Végül a sablonok valódi értéke abban rejlik, hogy képesek vagyunk vertikális alkalmazási területek számára _prompt könyvtárakat_ létrehozni és publikálni - ahol a prompt sablon az adott alkalmazás-specifikus kontextust vagy példákat tükrözi, hogy a válaszok relevánsabbak és pontosabbak legyenek a célozott felhasználói közönség számára. A [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repozitórium egy remek példa erre a megközelítésre, amely a tanítási területhez készít prompt könyvtárakat, hangsúlyt fektetve olyan kulcscélokra, mint az óratervezés, tananyag-tervezés, tanuló oktatás stb.

## Támogató tartalom

Ha úgy gondoljuk, hogy a prompt felépítése rendelkezik egy utasítással (feladat) és egy céltartalommal (fő tartalom), akkor a _másodlagos tartalom_ olyan, mint további kontextus, amit adunk annak érdekében, hogy a kimenetet valamilyen módon befolyásoljuk. Ez lehet hangolási paraméter, formázási utasítások, témakör-taxonómiák stb., amelyek segítenek a modellnek a választ az elvárt célokhoz vagy elvárásokhoz igazítani.

Például: Adott egy kurzuskatalógus, amelyben bőséges metaadatok vannak (név, leírás, szint, metaadat címkék, oktató stb.) az összes tananyaghoz a tantervben:

- meghatározhatunk egy utasítást, hogy "összefoglalja az őszi 2023-as kurzuskatalógust"
- a fő tartalmat felhasználhatjuk a kívánt kimenet pár példájának bemutatására
- a másodlagos tartalmat felhasználhatjuk az 5 legfontosabb "címke" megjelölésére.

Most a modell egy összefoglalót tud adni a megadott példák formátumában - de ha az eredmény több címkét is tartalmaz, az előzőleg megjelölt 5 címkét fogja előnyben részesíteni a másodlagos tartalom alapján.

---

<!--
LECKE SABLON:
Ez az egység az alapfogalom #1-et kell hogy lefedje.
Megerősíteni a fogalmat példákkal és hivatkozásokkal.

FOGALOM #3:
Prompt használati technikák.
Mik a prompt tervezés alapvető technikái?
példákkal szemléltetni.
-->

## Prompt használati legjobb gyakorlatok

Most, hogy tudjuk, miképp lehet promptokat _összerakni_, elkezdhetjük azt is gondolni, hogyan kell ezeket _tervezni_ a legjobb gyakorlatok szerint. Két részre bonthatjuk ezt – a megfelelő _hozzáállás_ kialakítására és a helyes _technikák_ alkalmazására.

### A prompt tervezés hozzáállás

A prompt tervezés egy próbálkozás-alapú folyamat, ezért tarts három tágabb iránymutatást szem előtt:

1. **A domén megértése számít.** A válasz pontossága és relevanciája a _domén_ függvénye, amelyben az alkalmazás vagy a felhasználó működik. Használd az intuíciódat és domén szakértelmedet a technikák testreszabásához. Például definiálj _domén-specifikus személyiségeket_ a rendszerüzenetekben vagy használj _domén-specifikus sablonokat_ a felhasználói promptokban. Adj másodlagos tartalmat, amely tükrözi a domén specifikus kontextust, vagy használj _domén-specifikus jeleket és példákat_, hogy a modellt a megszokott használati minták felé tereld.

2. **A modell megértése számít.** Tudjuk, hogy a modellek véletlenszerűek. Azonban a modell implementációja változhat a képzési adatkészlet, a képességek (például API vagy SDK által) és a célzott tartalomtípus (pl. kód, kép, szöveg) alapján. Ismerd meg a használt modell erősségeit és korlátait, és azokat használd arra, hogy feladatokat priorizálj vagy egyéni sablonokat építs, amelyek a modell képességeire vannak optimalizálva.

3. **Ismétlés és validálás számít.** A modellek gyorsan fejlődnek, és a prompt tervezési technikák is. Domén szakértőként lehet, hogy van olyan további kontextusod vagy kritériumod, ami a konkrét alkalmazásodra jellemző, és nem alkalmazható általánosan. Használj prompt tervező eszközöket és technikákat a gyors kezdéshez, majd ismételj, és validáld eredményeidet a saját intuícióddal és szakértelmeddel. Jegyezd le felismeréseidet, és készíts egy **tudásbázist** (pl. prompt könyvtárakat), amelyeket mások is alapnak használhatnak a gyorsabb további iterációhoz.

## Legjobb gyakorlatok

Tekintsük át a leggyakoribb, [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) és [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) szakértők által ajánlott legjobb gyakorlatokat.

| Mi                              | Miért                                                                                                                                                                                                                                               |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Értékeld a legújabb modelleket. | Az új generációk valószínűleg fejlettebb funkciókkal és jobb minőséggel rendelkeznek, de általában magasabb költséggel is járnak. Értékeld őket hatásuk alapján, majd dönts a migrációról.                                                          |
| Válaszd szét az utasítást és a kontextust | Ellenőrizd, hogy a modell/szolgáltató definiál-e _elválasztókat_ az utasítás, elsődleges és másodlagos tartalom egyértelmű megkülönböztetéséhez. Ez segíthet, hogy a modellek pontosabban súlyozzák a tokeneket.                                         |
| Légy specifikus és egyértelmű  | Adj több részletet a kívánt kontextusról, eredményről, hosszúságról, formátumról, stílusról stb. Ez javítani fogja a válaszok minőségét és következetességét. Rendszerezd recepteket újrafelhasználható sablonokban.                                    |
| Légy részletes, használj példákat | A modellek jobban reagálhatnak "mutasd és mond" megközelítésre. Kezdd `nullás lövés` móddal, amikor adsz utasítást (példák nélkül), majd finomíts `néhány lövés` módra példákkal. Használj analógiákat is.                                                   |
| Használj jeleket a komplettálás megindításához | Terelj egy kívánt eredmény felé, ha életkezdető szavakat vagy kifejezéseket adsz, amelyeket a modell kezdőpontként használhat a válaszhoz.                                                                                                         |
| Ismétlés                       | Néha meg kell ismételni az utasításokat a modellnek. Adj utasítást a fő tartalom előtt és után, használj utasítást és jelet, stb. Ismételj és validálj, hogy megtaláld, mi működik.                                                                 |
| Számít a sorrend               | Az információ sorrendje befolyásolhatja a válaszokat, még tanulási példák esetén is a közelmúlt hatása miatt. Próbálj ki több lehetőséget, hogy megtaláld a legjobbat.                                                                              |
| Adj a modellnek lehetőséget a „kihátrálásra” | Adj a modellnek egy _visszaesési_ válaszlehetőséget arra az esetre, ha nem tudja elvégezni a feladatot. Ez csökkenti a hamis vagy kitalált válaszok valószínűségét.                                                                                |
|                                |                                                                                                                                                                                                                                                    |

Ahogy bármelyik legjobb gyakorlatnál, emlékezz rá, hogy _a saját tapasztalatod változhat_ a modell, feladat és domén függvényében. Használd kezdőpontként, és iterálj, hogy megtaláld, mi működik a legjobban számodra. Folyamatosan értékeld újra a prompt tervezési folyamataidat az új modellek és eszközök megjelenésekor, a folyamat skálázhatóságára és válasz minőségére koncentrálva.

<!--
LECKE SABLON:
Ebben az egységben legyen egy kód kihívás, ha releváns.

KIHÍVÁS:
Linkelj egy Jupyter Notebookot, amelyben csak a kódrészekhez vannak megjegyzések az instrukciókban (a kódrészek üresek).

MEGOLDÁS:
Linkelj egy példányt ugyanabból a Notebookból, tele promptokkal kitöltve és lefuttatva, egy példa kimenettel.
-->

## Feladat

Gratulálunk! Eljutottál a lecke végére! Itt az ideje, hogy kipróbáld ezeknek a fogalmaknak és technikáknak a használatát valódi példákon!

A feladatunkhoz egy Jupyter Notebookot fogunk használni, amelyben interaktívan végezheted el a gyakorlatokat. A Notebookot bővítheted saját Markdown és kódcellákkal is, hogy saját magad fedezz fel ötleteket és technikákat.

### Kezdéshez készíts forkot az adattárról, majd

- (Javasolt) Indítsd el a GitHub Codespaces-t
- (Alternatív) Klónozd le a repót a saját eszközödre, és futtasd Docker Desktop segítségével
- (Alternatív) Nyisd meg a Notebookot a választott futtatókörnyezetedben

### Ezután állítsd be a környezeti változókat

- Másold át a `.env.copy` fájlt a repó alapkönyvtárában `.env` fájlra, és töltsd ki az `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` és `AZURE_OPENAI_DEPLOYMENT` értékeket. Lépj vissza a [Learning Sandbox szakaszhoz](#tanulási-sandbox), hogy megtanuld, hogyan.

### Ezután nyisd meg a Jupyter Notebookot

- Válaszd ki a futtatókörnyezet kerneljét. Ha az 1-es vagy 2-es opciót használod, egyszerűen válaszd ki az alapértelmezett Python 3.10.x kernelt, amelyet a fejlesztői konténer biztosít.

Minden készen áll a gyakorlatokra. Ne feledd, itt nincs _jó vagy rossz_ válasz, csak a kísérletezés és az intuíció fejlesztése, hogy mi működik egy adott modell és alkalmazási terület számára.

_Azért nincs ebben a leckében konkrét kód megoldás, mert a Notebook tartalmaz "Saját megoldás:" címkéjű Markdown cellákat, amelyek példaként mutatnak egy lehetséges választ._

 <!--
LECKE SABLON:
Zárd le a szakaszt összefoglalóval és önálló tanuláshoz ajánlott forrásokkal.
-->

## Ismeretfelmérés

Melyik az alábbiak közül egy jó prompt, amely néhány ésszerű legjobb gyakorlatot követ?

1. Mutass egy képet egy piros autóról  
2. Mutass egy képet egy piros Volvóról, XC90 modellről, ami egy szikla mellett parkol naplementekor  
3. Mutass egy képet egy piros Volvóról, XC90 modellről

A: 2, ez a legjobb prompt, mert részletezi a „mit” és konkrét (nem csak egy autó, hanem egy adott típus és modell), és leírja a teljes környezetet is. A 3 a második legjobb, mert sok leírást tartalmaz.

## 🚀 Kihívás

Próbáld ki a "jelzés" technikát a következő prompttal: Fejezd be a mondatot: "Mutass egy képet egy piros Volvóról és ". Mivel válaszol, és hogyan javítanád?

## Szép munka! Folytasd a tanulást

Szeretnél többet megtudni a különféle Prompt mérnöki fogalmakról? Látogass el a [folytatólagos tanulási oldalra](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), ahol további nagyszerű forrásokat találsz a témában.

Menj a 5. leckéhez, ahol [fejlettebb prompttechnikákat](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) fogunk tanulmányozni!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->