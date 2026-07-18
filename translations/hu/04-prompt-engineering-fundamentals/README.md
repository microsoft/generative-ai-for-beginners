# Prompt Műszaki Alapok

[![Prompt Műszaki Alapok](../../../translated_images/hu/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Bevezetés
Ez a modul a generatív MI modellekben hatékony promptok létrehozásához szükséges alapvető fogalmakat és technikákat tárgyalja. Fontos az is, hogyan írjuk meg a promptot az LLM számára. Egy gondosan megtervezett prompt jobb választ eredményezhet. De pontosan mit jelentenek a _prompt_ és _prompt mérnöki munka_ kifejezések? És hogyan javíthatom az LLM-nek küldött prompt _bemenetet_? Ezekre a kérdésekre próbálunk választ adni ebben és a következő fejezetben.

A _generatív MI_ képes új tartalmakat (például szöveget, képeket, hangot, kódot stb.) létrehozni a felhasználó kéréseire reagálva. Ezt olyan _Nagy Nyelvi Modellek_ segítségével éri el, mint az OpenAI GPT (Generative Pre-trained Transformer) sorozata, amelyeket természetes nyelv és kód használatára képeztek ki.

A felhasználók most már ismerős párbeszédes formában léphetnek kapcsolatba ezekkel a modellekkel, technikai tudás vagy képzés nélkül. A modellek _prompt alapúak_ – a felhasználók szöveges bemenetet (promptot) küldenek, és az MI választ (befejezést) kap vissza. Ezután több körben, iteratívan „beszélgethetnek az MI-vel”, finomítva a promptot, amíg a válasz megfelel az elvárásaiknak.

A „promptok” mostantól a generatív MI alkalmazások elsődleges _programozási felületévé_ váltak, megmondva a modelleknek, mit tegyenek és befolyásolva a visszakapott válaszok minőségét. A „Prompt Mérnöki Munka” egy gyorsan fejlődő tudományterület, amely a promptok _tervezésére és optimalizálására_ összpontosít, hogy méretezhetően konzisztens és minőségi válaszokat adjon.

## Tanulási célok

Ebben az órában megtanuljuk, mi az a Prompt Mérnöki Munka, miért fontos, és hogyan alkothatunk hatékonyabb promptokat egy adott modell és alkalmazási cél számára. Megismerjük a prompt mérnöki munka alapfogalmait és bevált módszereit – és bemutatjuk az interaktív Jupyter Notebook „játszóteret”, ahol láthatjuk ezen elvek gyakorlati alkalmazását.

Az óra végére képesek leszünk:

1. Megmagyarázni, mi az a prompt mérnöki munka és miért lényeges.
2. Leírni a prompt összetevőit és azok használatát.
3. Megtanulni a prompt mérnöki munka legjobb gyakorlatait és technikáit.
4. Az elsajátított technikákat valós példákon alkalmazni, OpenAI végpont használatával.

## Főbb fogalmak

Prompt Mérnöki Munka: A bemenetek tervezésének és finomításának folyamata annak érdekében, hogy az MI modellek a kívánt kimeneteket állítsák elő.
Tokenizáció: A szöveg kisebb egységekre, úgynevezett tokenekre bontásának folyamata, amelyet a modell megért és feldolgoz.
Instrukcióra hangolt LLM-ek: Nagy Nyelvi Modellek (LLM-ek), amelyeket specifikus utasításokkal finomhangoltak a válaszok pontosságának és relevanciájának javítására.

## Tanuló játszótér

A prompt mérnöki munka jelenleg inkább művészet, mint tudomány. Az intuíció fejlesztésének legjobb módja a _gyakorlás_, és a próbálkozás alapú megközelítés alkalmazása, amely kombinálja az alkalmazási terület szakértelmét a javasolt technikákkal és modellspecifikus optimalizációkkal.

Az ehhez az órához tartozó Jupyter Notebook egy _játszótér_ környezetet biztosít, ahol kipróbálhatod, amit tanulsz – folyamatosan vagy a kód kihívás részeként a végén. A feladatok végrehajtásához szükséged lesz:

1. **Egy Azure OpenAI API kulcsra** - a telepített LLM szolgáltatás végpontja.
2. **Egy Python futtatókörnyezetre** - amelyben a Notebook végrehajtható.
3. **Helyi környezeti változókra** - _most végezd el a [BEÁLLÍTÁS](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) lépéseit, hogy készen állj_.

A notebook _kezdő_ feladatokat tartalmaz – de bátorítunk, hogy adj hozzá saját _Markdown_ (leírás) és _Kód_ (prompt kérés) szakaszokat, hogy több példát vagy ötletet próbálj ki – és fejleszd az intuíciódat a prompt tervezéshez.

## Illusztrált útmutató

Szeretnéd látni a tananyag nagy egészét, mielőtt belevágsz? Nézd meg ezt az illusztrált útmutatót, amely bemutatja a főbb témákat és a legfontosabb gondolatokat, amelyeket érdemes átgondolnod. Az útiterv az alapfogalmak és kihívások megértésétől vezet el a releváns prompt mérnöki technikák és legjobb gyakorlatok alkalmazásáig. Ne feledd, hogy ennek az útmutatónak az „Haladó technikák” része a tananyag _következő_ fejezetéhez kapcsolódik.

![Illusztrált útmutató a prompt mérnöki munkához](../../../translated_images/hu/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## A mi startupunk

Most nézzük meg, hogyan kapcsolódik _ez a téma_ startup küldetésünkhöz, az [MI innováció oktatásba való behozatalához](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Célunk, hogy MI-alapú, _személyre szabott tanulási_ alkalmazásokat fejlesszünk – így gondolkodjunk el arról, hogyan „tervezhetnek” promptokat alkalmazásunk különböző felhasználói:

- **Adminisztrátorok** az MI-t arra kérhetik, hogy _elemezze a tantervi adatokat, hogy azonosítsa a lefedetlenségi hiányosságokat_. Az MI összefoglalhatja az eredményeket vagy vizualizálhatja őket kóddal.
- **Oktatók** az MI-t arra kérhetik, hogy _készítsen tantervet egy célközönség és téma számára_. Az MI a személyre szabott tervet meghatározott formátumban készítheti el.
- **Diákok** az MI-t arra kérhetik, hogy _támogassa őket nehéz tantárgyban_. Az MI most már tanórákkal, tippekkel és példákkal segíti őket, szintjükre szabva.

Ez csak a jéghegy csúcsa. Nézd meg a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) nyílt forráskódú, oktatási szakértők által összeállított prompt könyvtárat – hogy szélesebb képet kapj a lehetőségekről! _Próbáld ki néhány promptot a játszótéren vagy az OpenAI Playground-ban, hogy lásd, mi történik!_

<!--
LESSON TEMPLATE:
Ez az egység az alapfogalom #1-et kell lefedje.
Példákkal és hivatkozásokkal erősítse meg a fogalmat.

FOGALOM #1:
Prompt mérnöki munka.
Definiáld és magyarázd el, miért van rá szükség.
-->

## Mi az a Prompt Mérnöki Munka?

Ezt az órát azzal kezdtük, hogy a **prompt mérnöki munkát** a szöveges bemenetek (promptok) _megtervezésének és optimalizálásának_ folyamataként határoztuk meg, ami következetes és minőségi válaszokat (befejezéseket) eredményez adott alkalmazási cél és modell alapján. Ezt egy kétlépcsős folyamatként képzelhetjük el:

- a kezdő prompt _megtervezése_ adott modell és cél érdekében
- a prompt _finomítása_ iteratívan a válasz minőségének javításához

Ez szükségszerűen egy próbálkozásos folyamat, amely felhasználói intuíciót és erőfeszítést igényel az optimális eredmény eléréséhez. Miért fontos ez akkor? A válaszhoz először három fogalmat kell megértenünk:

- _Tokenizáció_ = hogyan „látja” a modell a promptot
- _Alap LLM-ek_ = hogyan „feldolgozza” a modell a promptot
- _Instrukcióra hangolt LLM-ek_ = hogyan „látja” most már a feladatokat a modell

### Tokenizáció

Egy LLM a promptokat _tokenek sorozataként_ látja, ahol különböző modellek (vagy ugyanazon modell verziói) másként tokenizálhatják ugyanazt a promptot. Mivel az LLM-ek tokeneken (nem nyers szövegen) tanultak, a promptok tokenizálásának módja közvetlenül befolyásolja a generált válasz minőségét.

Az tokenizáció intuíciójának megértéséhez kipróbálhatod az alábbi [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) eszközt. Másold be a promptodat – és nézd meg, hogyan alakul tokenekké, figyelve arra, hogyan kezeli a szóközöket és írásjeleket. Megjegyzés: itt egy régebbi LLM-et (GPT-3) látsz - így egy újabb modell más eredményt adhat.

![Tokenizáció](../../../translated_images/hu/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Fogalom: Alapmodell (Foundation Models)

Amint a prompt tokenizálva van, az ["Alap LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (vagy Alapmodell) elsődleges feladata az adott token előrejelzése a sorozatban. Az LLM-ek hatalmas szövegadatokon vannak kiképezve, így jó statisztikai érzékük van a tokenek közötti összefüggésekhez, és bizonyos fokú magabiztossággal képesek előre jelezni a következőt. Nem értik a prompt vagy token _értelmét_; csak egy mintát látnak, amit „kiegészíthetnek” a következő előrejelzéssel. Ezt a folyamatot addig folytatják, amíg a felhasználó nem állítja le, vagy ki nem teljesül egy előre meghatározott feltétel.

Szeretnéd látni, hogyan működik a prompt alapú befejezés? Írd be a fenti promptot a [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) oldalra az alapértelmezett beállításokkal. A rendszer úgy kezeli a promptokat, mint információkérés - így olyan befejezést kapsz, ami illeszkedik ehhez a kontextushoz.

De mi van akkor, ha a felhasználó pontosabb vagy valamilyen kritériumnak, célfeladatnak megfelelő választ szeretne látni? Itt lépnek be a képbe az _instrukcióra hangolt_ LLM-ek.

![Alap LLM chat befejezés](../../../translated_images/hu/04-playground-chat-base.65b76fcfde0caa67.webp)

### Fogalom: Instrukcióra hangolt LLM-ek

Egy [Instrukcióra Hangolt LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) az alapmodellből indul ki, és példák vagy bemenet/kimenet párok (például többkörös „üzenetek”) segítségével finomhangolja azt, melyek tartalmazhatnak egyértelmű utasításokat – az MI válasza pedig követi ezeket az utasításokat.

Ehhez olyan technikákat alkalmaznak, mint az Emberi Visszacsatolásos Megerősítéses Tanulás (RLHF), amely a modellt arra tanítja, hogy _kövesse az utasításokat_, és _tanuljon a visszajelzésekből_, így a válaszok jobban alkalmazkodnak a gyakorlati alkalmazásokhoz és relevánsabbak a felhasználói célok szempontjából.

Próbáljuk ki – térj vissza a fenti prompthoz, de most változtasd meg a _rendszer üzenetet_ és add meg a következő utasítást a kontextusként:

> _Összegzed a megadott tartalmat egy másodikos diáknak. Egy bekezdésből álljon az összefoglaló 3-5 felsorolási ponttal._

Látod, hogy most a válasz az elvárt célnak és formátumnak megfelelően lett hangolva? Egy oktató közvetlenül felhasználhatja ezt a választ az adott tanórán.

![Instrukcióra hangolt LLM chat befejezés](../../../translated_images/hu/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Miért van szükségünk prompt mérnöki munkára?

Most, hogy tudjuk, hogyan dolgozzák fel az LLM-ek a promptokat, beszéljünk arról, _miért_ van szükség prompt mérnöki munkára. A válasz abban rejlik, hogy a jelenlegi LLM-ek számos kihívást jelentenek, amelyek megnehezítik a _megbízható és következetes_ válaszok elérését anélkül, hogy erőfeszítést tennénk a prompt felépítésébe és optimalizálásába. Például:

1. **A modellválaszok sztochasztikusak.** Az _ugyanaz a prompt_ különböző modelleknél vagy verzióknál eltérő válaszokat adhat. Sőt, _ugyanazzal a modellel_ különböző időpontokban is eltérő eredményeket generálhat. _A prompt mérnöki technikák segíthetnek minimalizálni ezeket a változásokat jobb védőkorlátok biztosításával_.

1. **A modellek valótlan válaszokat generálhatnak.** A modellek _nagy, de véges_ adathalmazokon vannak előképzve, így hiányos a tudásuk a tanítási határon kívüli fogalmakról. Ennek következtében pontatlan, kitalált vagy ellentmondó válaszokat is adhatnak. _A prompt mérnöki technikák segítenek azonosítani és kezelni ezeket a kitalált válaszokat, például idézetek vagy érvelések kérésével az MItől_.

1. **A modellek képességei eltérőek lehetnek.** Az újabb modellek vagy generációk gazdagabb képességekkel rendelkeznek, de sajátos furcsaságokat és költség- illetve komplexitás-különbségeket is hoznak. _A prompt mérnökség segít kidolgozni bevált gyakorlatokat és munkafolyamatokat, amelyek elrejtik a különbségeket és alkalmazkodnak a modellspecifikus követelményekhez, méretezhető és zökkenőmentes módon_.

Nézzük meg ezt gyakorlatban az OpenAI vagy Azure OpenAI Playground-ban:

- Használd ugyanazt a promptot különböző LLM telepítéseknél (pl. OpenAI, Azure OpenAI, Hugging Face) – tapasztaltad a különbségeket?
- Használd ugyanazt a promptot többször ugyanazzal az LLM telepítéssel (pl. Azure OpenAI playground) – mik voltak a különbségek?

### Kitalált válasz példa

Ebben a tanfolyamban a **„kitalálás”** (fabrication) kifejezést használjuk arra a jelenségre, amikor az LLM-k néha tényszerűen hibás információt generálnak a képzésük vagy egyéb korlátok miatt. Ezt gyakran _„hallucinációnak”_ is nevezik népszerű cikkekben vagy kutatási anyagokban. Javasoljuk azonban, hogy a „kitalálás” kifejezést használjuk, hogy elkerüljük az emberi jellemvonások mesterséges alkalmazását egy gépi eredményre. Ez erősíti a [Felelős MI iránymutatásokat](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminológiai szempontból, eltávolítva olyan kifejezéseket, amelyek bizonyos kontextusokban sértők vagy nem befogadóak lehetnek.

Szeretnéd látni, hogyan működnek a kitalált válaszok? Gondolj arra a promtra, amely az MI-t arra utasítja, hogy generáljon tartalmat egy nem létező témáról (hogy biztosan ne legyen benne a képzési adathalmazban). Például ezt a promptot próbáltam:

> **Prompt:** készíts tantervet a Marsi háború 2076-os eseményeiről.

Egy webes keresés azt mutatta, hogy vannak képzeletbeli művek (például tévésorozatok vagy könyvek) a Marsi háborúkról – de egyik sem 2076-ban. Az egészséges ész azt is mondja, hogy 2076 _a jövőben_ van, tehát nem társítható valós eseményhez.


Mi történik, ha ezt a promptot különböző LLM szolgáltatókkal futtatjuk?

> **Válasz 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/hu/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Válasz 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/hu/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Válasz 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/hu/04-fabrication-huggingchat.faf82a0a51278956.webp)

Ahogy várható volt, minden modell (vagy modellverzió) kissé eltérő válaszokat ad a sztochasztikus viselkedés és a modell képességeinek különbségei miatt. Például az egyik modell egy 8. osztályos közönséget céloz meg, míg a másik egy középiskolás tanulóra számít. Azonban mindhárom modell olyan válaszokat generált, amelyek meggyőzhetnek egy tájékozatlan felhasználót arról, hogy az esemény valódi volt.

A prompt mérnökség technikák, mint a _metaprompting_ és a _hőmérséklet konfiguráció_ bizonyos mértékben csökkenthetik a modell által generált hamis információkat. Az új prompt mérnökségi _architektúrák_ pedig zavartalanul integrálják az új eszközöket és technikákat a prompt folyamba, hogy mérsékeljék vagy csökkentsék ezeknek az effekteknek egy részét.

## Esettanulmány: GitHub Copilot

Zárjuk ezt a szakaszt azzal, hogy megvizsgáljuk, hogyan alkalmazzák a prompt mérnökséget valós megoldásokban egy esettanulmányon keresztül: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

A GitHub Copilot a „te AI Párprogramozód” – amely szöveges promptokat alakít át kód kiegészítésekké, és integráltan működik a fejlesztői környezetedben (például Visual Studio Code), zökkenőmentes felhasználói élményt biztosítva. Az alábbi blog sorozatban dokumentáltak szerint a legrégebbi verzió az OpenAI Codex modellen alapult – a mérnökök pedig gyorsan rájöttek, hogy szükség van a modell finomhangolására és jobb prompt mérnökségi technikák kidolgozására a kód minőségének javítása érdekében. Júliusban [bemutatták a Codex-t túlszárnyaló, továbbfejlesztett AI modellt](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), amely még gyorsabb javaslatokat ad.

Olvasd el a bejegyzéseket sorrendben, hogy kövesd a tanulási folyamatukat.

- **2023 május** | [GitHub Copilot egyre jobb kódértésben](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023 május** | [Bennfentes beszélgetés: LLM-ek munkája a GitHub Copilot mögött](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023 június** | [Hogyan írj jobb promptokat a GitHub Copilot számára](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023 július** | [.. GitHub Copilot túlszárnyalja a Codex-et továbbfejlesztett AI modellel](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023 július** | [Fejlesztői útmutató a prompt mérnökséghez és LLM-ekhez](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023 szeptember** | [Hogyan építs felvállalati LLM alkalmazást: tanulságok a GitHub Copilotból](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Böngészhetsz a [Mérnökségi blogjukban](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) is további bejegyzésekért, például [ebben](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), amely bemutatja, hogyan _alkalmazzák_ ezeket a modelleket és technikákat valós alkalmazások létrehozására.

---

<!--
LESSON TEMPLATE:
Ennek az egységnek a központi fogalom #2-t kell lefednie.
A fogalmat példákkal és hivatkozásokkal kell megerősíteni.

FOGALOM #2:
Prompt Tervezés.
Illusztrálva példákkal.
-->

## Prompt felépítése

Láttuk, miért fontos a prompt mérnökség - most értsük meg, hogyan _épülnek fel_ a promptok, hogy különböző technikákat tudjunk értékelni a hatékonyabb prompt tervezéshez.

### Alapvető prompt

Kezdjük az alapvető prompttal: egy szöveges bemenet, amelyet a modellnek küldünk kontextus nélkül. Íme egy példa - amikor az amerikai himnusz első néhány szavát küldjük az OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) felé, azonnal _kiegészíti_ a választ a következő néhány sorral, bemutatva az alapvető előrejelzési működést.

| Prompt (Bemenet)  | Befejezés (Kimenet)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Úgy hangzik, mintha az "A csillagos lobogó" (The Star-Spangled Banner) amerikai himnusz kezdősora lenne. A teljes szöveg így hangzik ...      |

### Összetett prompt

Most adjunk kontextust és utasításokat az alapvető prompthoz. A [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lehetővé teszi, hogy egy összetett promptot _üzenetek_ gyűjteményeként állítsunk össze:

- Bemenet/kimenet párok, amelyek tükrözik a _felhasználó_ kérdését és az _asszisztens_ válaszát.
- Rendszerüzenet, amely beállítja az asszisztens viselkedésének vagy személyiségének kontextusát.

A kérés most az alábbi formában van, ahol a _tokenizáció_ hatékonyan rögzíti a kontextusból és a beszélgetésből kinyert releváns információkat. A rendszerkontextus megváltoztatása legalább olyan jelentős hatással lehet a válaszok minőségére, mint a felhasználó által megadott bemenetek.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Utasító prompt

A fenti példákban a felhasználói prompt egy egyszerű szöveges kérés volt, amely információkérésként értelmezhető. Az _utasító_ promptokkal a szöveget arra használhatjuk, hogy részletesebben meghatározzunk egy feladatot, ezzel jobb útmutatást adva az AI-nak. Íme egy példa:

| Prompt (Bemenet)                                                                                                                                                                                                                         | Befejezés (Kimenet)                                                                                                        | Utasítás típusa    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Írj leírást a Polgárháborúról                                                                                                                                                                                                         | _egyszerű bekezdést adott vissza_                                                                                           | Egyszerű              |
| Írj leírást a Polgárháborúról. Adj kulcsfontosságú dátumokat és eseményeket, és ismertesd a jelentőségüket                                                                                                                                 | _egy bekezdést adott és kulcs események dátumainak listáját ismertetővel_                                                   | Összetett             |
| Írj leírást a Polgárháborúról 1 bekezdésben. Adj 3 pontban kulcsfontosságú dátumokat azok jelentőségével. Adj további 3 pontot jelentős történelmi személyekről és hozzájárulásaikról. Az eredményt JSON fájl formátumban add vissza.                     | _szövegdobozban több részletes adatot ad vissza, JSON formátumban, amit másolhatsz, menthetsz, és szükség szerint validálhatsz_ | Összetett. Formázott. |

## Elsődleges tartalom

A fenti példákban a prompt még eléggé nyitott volt, lehetővé téve az LLM számára, hogy eldöntse, a kipreparált adatainak mely része releváns. Az _elsődleges tartalom_ tervezési mintával a bemeneti szöveget két részre bontjuk:

- egy utasításra (tevékenység)
- releváns tartalomra (ami befolyásolja a tevékenységet)

Íme egy példa, ahol az utasítás: "fogalmazd össze 2 mondatban".

| Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Befejezés (Kimenet)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A Jupiter a Nap ötödik bolygója és a Naprendszer legnagyobb bolygója. Gázóriás, amelynek tömege a Nap tömegének ezredrésze, de a Naprendszer összes többi bolygójának tömegének két és félszerese. A Jupiter az egyik legfényesebb égitest, amely szabad szemmel látható az éjszakai égbolton, és már az ókori civilizációk is ismerték. A nevét a római Jupiter istenről kapta.[19] Földről nézve a Jupiter elég fényes lehet ahhoz, hogy visszavert fényével látható árnyékokat vetítsen,[20] és általában az éjszakai égbolt harmadik legfényesebb természetes objektuma a Hold és a Vénusz után. <br/> **Fogalmazd meg ezt 2 rövid mondatban** | A Jupiter, a Nap ötödik bolygója, a Naprendszer legnagyobb bolygója, és az éjszakai égbolt egyik legfényesebb objektuma. Nevét a római Jupiter istenről kapta, és gázóriás, amelynek tömege a Naprendszer többi bolygójának két és félszerese.                            |

Az elsődleges tartalmi szegmenst különböző módon lehet használni a hatékonyabb utasításokhoz:

- **Példák** - ahelyett, hogy explicite megmondanánk a modellnek, mit tegyen, adjunk neki példákat, hogy levonja a mintát.
- **Jelek** - az utasítást kövesse egy "jel", amely előkészíti a modellt a választához, irányítva a modellt relevánsabb válaszok felé.
- **Sablonok** - ismételhető 'receptek' promptokra helyőrzőkkel (változókkal), amelyeket speciális adatokról lehet testreszabni.

Nézzük meg ezt működés közben.

### Példák használata

Ez egy olyan megközelítés, ahol az elsődleges tartalommal "etetjük" a modellt néhány példával a kívánt kimenetre adott utasításra, és hagyjuk, hogy kihámozza a mintát a kívánt kimenethez. A példák számától függően beszélhetünk zero-shot, one-shot, few-shot promptolásról stb.

A prompt most három összetevőből áll:

- Egy feladat leírása
- Néhány példa a kívánt kimenetre
- Egy újabb példa kezdete (ami implicit feladatleírássá válik)

| Tanulási típus | Prompt (Bemenet)                                                                                                                                        | Befejezés (Kimenet)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Fordítsd le spanyolra                                                                                                           | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | A játékos körbefutott az alapoknál => Baseball <br/> A játékos ászt ütött => Tenisz <br/> A játékos hatost ütött => Krikett <br/> A játékos zsákolt =>      | Kosárlabda                   |
|               |                                                                                                                                                       |                             |

Figyeld meg, hogy zero-shot promptolásnál explicite kellett megadni az utasítást ("Fordítsd le spanyolra"), míg one-shot promptolásnál ezt már a modell kihámozza. A few-shot példa pedig mutatja, hogy több példa hozzáadása pontosabb következtetések levonását teszi lehetővé utasítás nélkül.

### Prompt jelek

Egy másik technika az elsődleges tartalom használatára, hogy példák helyett _jeleket_ adunk. Ilyenkor a modellt egy apró "lökéssel" irányítjuk a kívánt válaszformátum felé egy olyan részlettel, amely tükrözi a kívánt kimenetet. A modell ezután "felveszi a jelet", és hasonló módon folytatja.

| A jelek száma | Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Befejezés (Kimenet)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | A Jupiter a Nap ötödik bolygója és a Naprendszer legnagyobb bolygója. Gázóriás, amelynek tömege a Nap tömegének ezredrésze, de a Naprendszer összes többi bolygójának tömegének két és félszerese. A Jupiter az egyik legfényesebb égitest, amely szabad szemmel látható az éjszakai égbolton, és már az ókori civilizációk is ismerték. <br/>**Fogalmazd meg ezt**                                       | A Jupiter a Naprendszer legnagyobb bolygója és a Nap ötödik bolygója. Gázóriás, amelynek tömege a Nap tömegének ezredrésze, de nehezebb, mint az összes többi bolygó együttvéve. Az ókori civilizációk régóta ismerik, és könnyen látható az éjszakai égbolton.  |
| 1              | A Jupiter a Nap ötödik bolygója és a Naprendszer legnagyobb bolygója. Gázóriás, amelynek tömege a Nap tömegének ezredrésze, de a Naprendszer összes többi bolygójának tömegének két és félszerese. A Jupiter az egyik legfényesebb égitest, amely szabad szemmel látható az éjszakai égbolton, és már az ókori civilizációk is ismerték. <br/>**Fogalmazd meg ezt** <br/> Amit megtudtunk, hogy a Jupiter | a Nap ötödik bolygója és a Naprendszer legnagyobb bolygója. Gázóriás, amelynek tömege a Nap tömegének ezredrésze, de a Naprendszer összes többi bolygójának tömegének két és félszerese. Szabad szemmel könnyen látható, és az ókor óta ismert.                                    |

| 2              | A Jupiter a Naprendszer ötödik bolygója és a legnagyobb a rendszerben. Egy gázóriás, tömege a Nap tömege ezredrésze, de a többi Naprendszerbeli bolygó tömegének kétszer és félszerese. A Jupiter az egyik legfényesebb tárgy, amelyet szabad szemmel lehet látni az éjszakai égbolton, és az ókori civilizációk is ismerték már az írott történelem előtti időkből. <br/>**Összefoglaló** <br/> A három legfontosabb tény, amit megtanultunk:         | 1. A Jupiter a Naprendszer ötödik bolygója és a legnagyobb a Naprendszerben. <br/> 2. Egy gázóriás, tömege a Nap tömege ezredrésze...<br/> 3. A Jupiter az ókortól kezdve látható szabad szemmel ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Parancs sablonok

A parancs sablon egy _előre megírt recept egy parancshoz_, amely elmenthető és szükség szerint újra felhasználható, hogy nagyobb léptékben következetesebb felhasználói élményeket biztosítson. Egyszerű formájában ez egy parancs példák gyűjteménye, mint például [ez az OpenAI példája](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), amely biztosítja az interaktív parancs összetevőket (felhasználói és rendszerüzenetek) és az API-alapú kérés formátumát - a felhasználás támogatásához.

Összetettebb formájában, mint például [ez a LangChain példája](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), tartalmaz _helykitöltőket_, amelyek különböző forrásokból származó adatokat helyettesíthetnek (felhasználói bevitel, rendszerkörnyezet, külső adatforrások stb.) a parancs dinamikus generálásához. Ez lehetővé teszi újrafelhasználható parancsok könyvtárának létrehozását, amelyeket **programozottan** használhatunk a következetes felhasználói élmények biztosítására nagy léptékben.

Végül a sablonok valódi értéke az, hogy képesek létrehozni és közzétenni _parancs könyvtárakat_ vertikális alkalmazási területek számára - ahol a parancssablon most _optimalizálva_ van az alkalmazás specifikus kontextus vagy példák tükrözésére, amelyek relevánsabbá és pontosabbá teszik a válaszokat a célzott felhasználói közönség számára. A [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) adattár kiváló példája ennek a megközelítésnek, egy parancskönyvtárat válogat össze az oktatási terület számára, kiemelve a kulcscélokat, mint például az óratervezés, tantervtervezés, diák oktatás stb.

## Támogató tartalom

Ha a parancs felépítését úgy gondoljuk, hogy van egy utasítás (feladat) és egy cél (elsődleges tartalom), akkor a _másodlagos tartalom_ olyan plusz kontextus, amelyet adunk, hogy **valamilyen módon befolyásoljuk a kimenetet**. Ez lehet hangolási paraméterek, formázási utasítások, témataxonómiák stb., amelyek segíthetnek a modellnek _testre szabni_ a választ, hogy megfeleljen a kívánt felhasználói céloknak vagy elvárásoknak.

Például: Vegyük egy tanfolyam katalógust kiterjedt metaadatokkal (név, leírás, szint, metaadat címkék, oktató stb.) az összes elérhető tanfolyamról a tanrendben:

- meghatározhatunk egy utasítást, hogy "összefoglaljuk a tanfolyam katalógust 2023 őszére"
- az elsődleges tartalmat használhatjuk néhány kívánt kimeneti példa bemutatására
- a másodlagos tartalmat használhatjuk a legfontosabb 5 "címke" azonosítására.

Most a modell tud egy összefoglalót adni a néhány példával megadott formátumban - de ha egy eredmény több címkét tartalmaz, előnyben részesítheti azokat az 5 címkét, amelyeket a másodlagos tartalom azonosított.

---

<!--
ÓRAVÁZLAT SABLON:
Ez az egység bemutatja az 1. alapfogalmat.
Erősítsük meg a fogalmat példákkal és hivatkozásokkal.

ALAPFOGALOM #3:
Parancs mérnöki technikák.
Melyek a parancs mérnöki alaptechnikák?
Mutassuk be néhány gyakorlat segítségével.
-->

## Parancs adás legjobb gyakorlata

Most, hogy tudjuk, hogyan _szerkeszthetők_ parancsok, elkezdhetjük gondolkodni azon, hogyan _tervezhetjük meg_ őket, figyelembe véve a legjobb gyakorlatokat. Két részben gondolkodhatunk: a megfelelő _hozzáállás_ és a megfelelő _technikák_ alkalmazásában.

### Parancs mérnöki hozzáállás

A parancs mérnökség próbálkozás és hibázás folyamat, ezért tarts három széles irányelveket szem előtt:

1. **A terület ismerete számít.** A válasz pontossága és relevanciája a _területtől_ függ, amelyben az alkalmazás vagy felhasználó működik. Használd az intuíciódat és a területi szakértelmedet, hogy **testreszabd a technikákat**. Például határozz meg _területspecifikus személyiségeket_ rendszerparancsaidban, vagy használj _területspecifikus sablonokat_ felhasználói parancsaidban. Adj meg másodlagos tartalmat, amely tükrözi a területspecifikus kontextusokat, vagy használj _területspecifikus jeleket és példákat_, hogy irányítsd a modellt ismerős felhasználási minták felé.

2. **A modell ismerete számít.** Tudjuk, hogy a modellek természetüknél fogva sztochasztikusak. De a modell implementációk eltérhetnek a felhasznált tréning adatbázis (előzetesen tanult tudás), a kínált képességek (pl. API vagy SDK-n keresztül), és az optimalizált tartalomtípus (pl. kód vs. képek vs. szöveg) tekintetében. Ismerd meg a használt modell erősségeit és korlátait, és ezt a tudást használd fel, hogy _prioritást adj a feladatoknak_ vagy készíts _testreszabott sablonokat_, amelyek optimalizáltak a modell képességeihez.

3. **Ismétlés és érvényesítés számít.** A modellek gyorsan fejlődnek, ahogy a parancs mérnöki technikák is. Mint területi szakértő, lehet, hogy vannak más kontextusaid vagy kritériumaid _a saját_ alkalmazásodra, amelyek nem alkalmazhatók a szélesebb közösségre. Használd a parancs mérnöki eszközöket és technikákat, hogy "beindítsd" a parancs felépítést, majd ismételd és érvényesítsd az eredményeket a saját intuícióddal és területi szakértelmeddel. Jegyezd fel meglátásaidat és hozz létre egy **tudásbázist** (pl. parancskönyvtárakat), amelyeket mások új alapként használhatnak a jövőbeni gyorsabb iterációkhoz.

## Legjobb gyakorlatok

Nézzük most a gyakori legjobb gyakorlatokat, amelyeket az [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) és az [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) szakértői ajánlanak.

| Mi                               | Miért                                                                                                                                                                                                                                              |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Értékeld a legújabb modelleket.  | Az új modellgenerációk valószínűleg fejlettebb funkciókkal és jobb minőséggel rendelkeznek - de magasabb költséget is jelenthetnek. Értékeld őket hatásuk alapján, majd hozz migrációs döntéseket.                                                      |
| Különítsd el az utasításokat és a kontextust | Ellenőrizd, hogy a modell/szolgáltató definiál-e _elválasztókat_, amelyek egyértelműbben megkülönböztetik az utasításokat, elsődleges és másodlagos tartalmat. Ez segítheti a modelleket abban, hogy pontosabban súlyozzák a tokeneket.                   |
| Legyél specifikus és világos       | Adj több részletet a kívánt kontextusról, eredményről, hosszúságról, formátumról, stílusról stb. Ez javítja mind a válaszok minőségét, mind konzisztenciáját. Rögzítsd a recepteket újrafelhasználható sablonokban.                                   |
| Legyél leíró, használj példákat   | A modellek jobban reagálhatnak a „mutasd és mondd el” megközelítésre. Kezdd egy `zero-shot` megoldással, ahol csak utasítást adsz (példák nélkül), majd próbáld ki a `few-shot` finomítást, ahol néhány példa segítségével adod meg az elvárt kimenetet. Használj analógiákat. |
| Használj jeleket a beindításhoz  | Bíztasd a modellt egy kívánt eredmény felé úgy, hogy adsz neki néhány kezdő szót vagy kifejezést, amelyet válaszként felhasználhat.                                                                                                                |
| Ismételj meg                   | Néha meg kell ismételned önmagad. Adj utasítást a fő tartalom előtt és után, használj utasítást és egy jelet, stb. Ismételj és validálj, hogy lásd, mi működik.                                                                                      |
| A sorrend számít                | Az információk bemutatásának sorrendje befolyásolhatja a kimenetet, még a tanulási példák esetén is a legfrissebb információk preferálása miatt. Próbálj ki több lehetőséget, hogy megtudd, melyik működik a legjobban.                                  |
| Adj a modellnek egy „kimenekülési” lehetőséget | Adj a modellnek egy _visszavonási_ válaszként szolgáló befejezést, amelyet akkor adhat ki, ha bármilyen okból nem tudja teljesíteni a feladatot. Ez csökkenti az esetleges hamis vagy kitalált válaszok generálásának esélyét.                                 |
|                                   |                                                                                                                                                                                                                                                   |

Mint minden legjobb gyakorlat esetén, tartsd észben, hogy _az eredmények eltérhetnek_ a modelltől, a feladattól és a területtől függően. Használd ezeket kiindulópontként, és ismételj, hogy megtaláld, mi működik a legjobban számodra. Folyamatosan értékeld újra parancs mérnöki folyamatodat, amint új modellek és eszközök állnak rendelkezésre, a folyamat skálázhatóságára és a válasz minőségére összpontosítva.

<!--
ÓRAVÁZLAT SABLON:
Ebben az egységben biztosíts kód kihívást, ha releváns

KIHÍVÁS:
Linkelj egy Jupyter Notebook-ot, amelyben csak a kód megjegyzések vannak az instrukciókban (a kód szakaszok üresek).

MEGOLDÁS:
Linkelj egy másolatot arról a Notebook-ról, ahol a parancsokat kitöltötték és lefuttatták, bemutatva egy példát.
-->

## Feladat

Gratulálunk! Eljutottál az óra végére! Itt az idő, hogy néhány koncepciót és technikát valós példákon tesztelj!

Feladatunkhoz egy Jupyter Notebookot fogunk használni interaktívan végrehajtható gyakorlatokkal. A Notebookot saját Markdown és Kód cellákkal is bővítheted, hogy felfedezd az ötleteket és technikákat a saját tempódban.

### A kezdéshez először készíts egy forkot a repóról, majd

- (Ajánlott) Indítsd el a GitHub Codespaces-t
- (Alternatív megoldás) Klónozd a repót helyi eszközödre és használd Docker Desktop-tal
- (Alternatív megoldás) Nyisd meg a Notebookot a preferált környezetedben.

### Ezután állítsd be a környezeti változókat

- Másold a `.env.copy` fájlt a repó gyökérkönyvtárában `.env` névre, majd töltsd ki az `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` és `AZURE_OPENAI_DEPLOYMENT` értékeket. Térj vissza a [Learning Sandbox szakasz](#tanuló-játszótér)hoz, hogy megtudd, hogyan.

### Ezután nyisd meg a Jupyter Notebookot

- Válaszd ki a futtatási kernelt. Ha az 1. vagy 2. opciót használod, egyszerűen válaszd a dev konténer által biztosított alapértelmezett Python 3.10.x kernelt.

Készen állsz, hogy fusd a gyakorlatokat. Ne feledd, hogy itt nincsenek _helyes és helytelen_ válaszok – csak opciók kipróbálása próbálkozás útján és intuíció építése arról, hogy mi működik egy adott modell és alkalmazási terület esetében.

_Ezért nincsenek Kód Megoldás szegmensek ebben az órában. Helyette a Notebookban lesznek Markdown cellák "Az én megoldásom:" címmel, amelyek egy példakimenetet mutatnak be referenciaként._

 <!--
ÓRAVÁZLAT SABLON:
Foglald össze a szakaszt egy összegzéssel és önálló tanuláshoz forrásokkal.
-->

## Tudásellenőrzés

Melyik a következők közül jó parancs, amely néhány ésszerű legjobb gyakorlatot követ?

1. Mutass egy képet egy piros autóról
2. Mutass egy képet egy piros Volvóról, XC90 modellről, amely egy szikla mellett parkol, a lemenő nap fényében
3. Mutass egy képet egy piros Volvóról, XC90 modellről

Válasz: 2, mert ez a legjobb parancs, mivel részleteket ad "mit" akarunk, konkrét típust és modellt is megad, és leírja a környezetet is. A 3 a következő legjobb, mert szintén sok leírást tartalmaz.

## 🚀 Kihívás

Próbáld használni a "jel" technikát a következő paranccsal: Fejezd be a mondatot "Mutass egy képet egy piros Volvóról és ". Mit válaszol rá, és hogyan fejlesztenéd tovább?

## Nagyszerű munka! Folytasd a tanulást

Szeretnél többet megtudni a különféle parancs mérnöki fogalmakról? Látogass el a [további tanulási oldalra](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), ahol más nagyszerű forrásokat találsz ezen a témán.

Menj át az 5. leckébe, ahol [haladó parancsadási technikákat](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) tanulmányozunk!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->