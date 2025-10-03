<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b3cb38518cf4fe7714d2f5e74dfa3eb",
  "translation_date": "2025-10-03T10:11:26+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "hu"
}
-->
# Prompttervezés Alapjai

[![Prompttervezés Alapjai](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.hu.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Bevezetés
Ez a modul a generatív AI modellek hatékony utasításainak megalkotásához szükséges alapvető fogalmakat és technikákat tárgyalja. Az, hogy hogyan írjuk meg az utasítást egy LLM-nek, szintén számít. Egy gondosan megfogalmazott utasítás jobb minőségű választ eredményezhet. De mit is jelentenek pontosan az olyan kifejezések, mint _utasítás_ és _prompttervezés_? És hogyan javíthatom az LLM-nek küldött _bemeneti utasítást_? Ezekre a kérdésekre próbálunk választ adni ebben a fejezetben és a következőben.

A _generatív AI_ képes új tartalmakat létrehozni (pl. szöveg, képek, hang, kód stb.) a felhasználói kérésekre válaszul. Ezt _nagy nyelvi modellek_ (Large Language Models, LLM) segítségével éri el, mint például az OpenAI GPT ("Generative Pre-trained Transformer") sorozata, amelyet természetes nyelv és kód használatára képeztek ki.

A felhasználók most már technikai szakértelem vagy képzés nélkül is interakcióba léphetnek ezekkel a modellekkel, ismerős paradigmák, például chat segítségével. A modellek _utasítás-alapúak_ - a felhasználók szöveges bemenetet (utasítást) küldenek, és visszakapják az AI válaszát (kiegészítést). Ezután "beszélgethetnek az AI-val" iteratívan, többfordulós párbeszédekben, finomítva az utasítást, amíg a válasz megfelel az elvárásaiknak.

Az "utasítások" most a generatív AI alkalmazások elsődleges _programozási interfészévé_ válnak, amelyek megmondják a modelleknek, mit tegyenek, és befolyásolják a visszakapott válaszok minőségét. A "prompttervezés" egy gyorsan növekvő tanulmányi terület, amely az utasítások _tervezésére és optimalizálására_ összpontosít, hogy következetes és minőségi válaszokat érjen el nagy léptékben.

## Tanulási célok

Ebben a leckében megtanuljuk, mi az a prompttervezés, miért fontos, és hogyan készíthetünk hatékonyabb utasításokat egy adott modellhez és alkalmazási célhoz. Megértjük a prompttervezés alapfogalmait és legjobb gyakorlatait - valamint megismerünk egy interaktív Jupyter Notebook "sandbox" környezetet, ahol ezek a fogalmak valós példákon alkalmazhatók.

A lecke végére képesek leszünk:

1. Elmagyarázni, mi az a prompttervezés és miért fontos.
2. Leírni az utasítások összetevőit és azok használatát.
3. Megtanulni a prompttervezés legjobb gyakorlatait és technikáit.
4. Alkalmazni a tanult technikákat valós példákra, egy OpenAI végpont használatával.

## Kulcsfogalmak

Prompttervezés: Az AI modellek kívánt kimeneteinek előállítását irányító bemenetek tervezésének és finomításának gyakorlata.
Tokenizáció: A szöveg kisebb egységekre, úgynevezett tokenekre bontásának folyamata, amelyeket a modell megérthet és feldolgozhat.
Instrukcióra hangolt LLM-ek: Nagy nyelvi modellek (LLM-ek), amelyeket specifikus utasításokkal finomhangoltak, hogy javítsák válaszaik pontosságát és relevanciáját.

## Tanulási Sandbox

A prompttervezés jelenleg inkább művészet, mint tudomány. A legjobb módja annak, hogy javítsuk az intuíciót, ha _többet gyakorlunk_, és egy próbálgatásos megközelítést alkalmazunk, amely ötvözi az alkalmazási terület szakértelmét az ajánlott technikákkal és modell-specifikus optimalizálásokkal.

A lecke mellé tartozó Jupyter Notebook egy _sandbox_ környezetet biztosít, ahol kipróbálhatjuk, amit tanulunk - menet közben vagy a végén található kód kihívás részeként. Az gyakorlatok végrehajtásához szükség lesz:

1. **Egy Azure OpenAI API kulcsra** - a telepített LLM szolgáltatási végpontjára.
2. **Egy Python futtatási környezetre** - amelyben a Notebook futtatható.
3. **Helyi környezeti változókra** - _végezd el a [BEÁLLÍTÁS](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) lépéseket most, hogy készen állj_.

A notebook _kezdő_ gyakorlatokat tartalmaz - de arra ösztönzünk, hogy adj hozzá saját _Markdown_ (leírás) és _Code_ (utasítás kérések) szakaszokat, hogy kipróbálj több példát vagy ötletet - és építsd az intuíciódat az utasítások tervezéséhez.

## Illusztrált útmutató

Szeretnéd átlátni, miről szól ez a lecke, mielőtt belevágnál? Nézd meg ezt az illusztrált útmutatót, amely bemutatja a főbb témákat és a kulcsfontosságú tanulságokat, amelyeket érdemes átgondolni mindegyikben. A lecke útvonala elvezet az alapfogalmak és kihívások megértésétől azok kezeléséig releváns prompttervezési technikákkal és legjobb gyakorlatokkal. Ne feledd, hogy az útmutató "Haladó technikák" szakasza a tananyag _következő_ fejezetében tárgyalt tartalomra utal.

![Prompttervezés Illusztrált Útmutató](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.hu.png)

## Startupunk

Most beszéljünk arról, hogyan kapcsolódik _ez a téma_ a startup küldetésünkhöz, hogy [AI innovációt hozzunk az oktatásba](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). AI-alapú alkalmazásokat szeretnénk építeni a _személyre szabott tanulás_ érdekében - gondoljuk át, hogyan "tervezhetnek" utasításokat az alkalmazásunk különböző felhasználói:

- **Adminisztrátorok** kérhetik az AI-t, hogy _elemezze a tantervi adatokat a lefedettségi hiányosságok azonosítása érdekében_. Az AI összefoglalhatja az eredményeket vagy kód segítségével vizualizálhatja azokat.
- **Oktatók** kérhetik az AI-t, hogy _készítsen óratervet egy célközönség és téma számára_. Az AI személyre szabott tervet készíthet egy megadott formátumban.
- **Diákok** kérhetik az AI-t, hogy _segítsen nekik egy nehéz tantárgyban_. Az AI most már irányíthatja a diákokat órákkal, tippekkel és példákkal, amelyek az ő szintjükhöz igazodnak.

Ez csak a jéghegy csúcsa. Nézd meg a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - egy oktatási szakértők által összeállított nyílt forráskódú utasítások könyvtárát - hogy szélesebb képet kapj a lehetőségekről! _Próbálj ki néhányat ezek közül az utasítások közül a sandboxban vagy az OpenAI Playgroundban, hogy lásd, mi történik!_

<!--
LECKE SABLON:
Ez az egység az alapfogalom #1-et kell, hogy lefedje.
Erősítsd meg a fogalmat példákkal és hivatkozásokkal.

FOGALOM #1:
Prompttervezés.
Határozd meg és magyarázd el, miért van rá szükség.
-->

## Mi az a Prompttervezés?

Ezt a leckét azzal kezdtük, hogy a **Prompttervezést** úgy határoztuk meg, mint a szöveges bemenetek (utasítások) _tervezésének és optimalizálásának_ folyamatát, hogy következetes és minőségi válaszokat (kiegészítéseket) érjünk el egy adott alkalmazási célhoz és modellhez. Ezt egy 2 lépéses folyamatként képzelhetjük el:

- Az _elsődleges utasítás_ megtervezése egy adott modellhez és célhoz
- Az utasítás _finomítása_ iteratívan a válasz minőségének javítása érdekében

Ez szükségszerűen egy próbálgatásos folyamat, amely felhasználói intuíciót és erőfeszítést igényel az optimális eredmények eléréséhez. De miért fontos ez? Ahhoz, hogy erre a kérdésre válaszoljunk, először három fogalmat kell megértenünk:

- _Tokenizáció_ = hogyan "látja" a modell az utasítást
- _Alap LLM-ek_ = hogyan "dolgozza fel" az alapmodell az utasítást
- _Instrukcióra hangolt LLM-ek_ = hogyan látja a modell most már a "feladatokat"

### Tokenizáció

Egy LLM az utasításokat _tokenek sorozataként_ látja, ahol különböző modellek (vagy egy modell különböző verziói) ugyanazt az utasítást különböző módon tokenizálhatják. Mivel az LLM-ek tokeneken (és nem nyers szövegen) vannak kiképezve, az utasítások tokenizálásának módja közvetlen hatással van a generált válasz minőségére.

Ahhoz, hogy intuíciót szerezzünk arról, hogyan működik a tokenizáció, próbáljunk ki olyan eszközöket, mint az [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), amelyet az alábbiakban láthatunk. Másold be az utasításodat - és nézd meg, hogyan alakul át tokenekké, figyelve arra, hogyan kezelik a szóköz karaktereket és írásjeleket. Ne feledd, hogy ez a példa egy régebbi LLM-et (GPT-3) mutat - tehát ha ezt egy újabb modellel próbálod, eltérő eredményt kaphatsz.

![Tokenizáció](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.hu.png)

### Fogalom: Alapmodellek

Miután egy utasítás tokenizálva lett, az ["Alap LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (vagy alapmodell) elsődleges funkciója az, hogy megjósolja a tokeneket ebben a sorozatban. Mivel az LLM-ek hatalmas szöveges adathalmazokon vannak kiképezve, jó érzékük van a tokenek közötti statisztikai kapcsolatokhoz, és ezt a jóslatot bizonyos magabiztossággal meg tudják tenni. Ne feledd, hogy nem értik a szavak vagy tokenek _jelentését_ az utasításban; csak egy mintát látnak, amelyet a következő jóslatukkal "kiegészíthetnek". Folytathatják a sorozat jóslását, amíg a felhasználó be nem avatkozik, vagy valamilyen előre meghatározott feltétel nem áll fenn.

Szeretnéd látni, hogyan működik az utasítás-alapú kiegészítés? Írd be a fenti utasítást az Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) alapértelmezett beállításaival. A rendszer úgy van konfigurálva, hogy az utasításokat információkérésként kezelje - tehát egy olyan kiegészítést kell látnod, amely kielégíti ezt a kontextust.

De mi van akkor, ha a felhasználó valami konkrétat szeretne látni, amely megfelel bizonyos kritériumoknak vagy feladati célnak? Itt jönnek képbe az _instrukcióra hangolt_ LLM-ek.

![Alap LLM Chat Kiegészítés](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.hu.png)

### Fogalom: Instrukcióra Hangolt LLM-ek

Egy [Instrukcióra Hangolt LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) az alapmodellel kezdődik, és példákkal vagy bemenet/kimenet párokkal (pl. többfordulós "üzenetekkel") finomhangolják, amelyek egyértelmű utasításokat tartalmazhatnak - és az AI válasza megpróbálja követni az utasítást.

Ez olyan technikákat használ, mint az emberi visszacsatolással történő megerősítéses tanulás (Reinforcement Learning with Human Feedback, RLHF), amely képes a modellt _utasítások követésére_ és _visszacsatolásból tanulásra_ kiképezni, így olyan válaszokat hoz létre, amelyek jobban megfelelnek a gyakorlati alkalmazásoknak és relevánsabbak a felhasználói célokhoz.

Próbáljuk ki - térjünk vissza a fenti utasításhoz, de most változtassuk meg a _rendszerüzenetet_, hogy a következő utasítást adjuk meg kontextusként:

> _Foglalja össze a kapott tartalmat egy második osztályos tanuló számára. Tartsa az eredményt egy bekezdésben, 3-5 ponttal._

Látod, hogy az eredmény most már a kívánt célhoz és formátumhoz igazodik? Egy oktató most közvetlenül felhasználhatja ezt a választ az adott osztály diáihoz.

![Instrukcióra Hangolt LLM Chat Kiegészítés](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.hu.png)

## Miért van szükségünk Prompttervezésre?

Most, hogy tudjuk, hogyan dolgozzák fel az utasításokat az LLM-ek, beszéljünk arról, _miért_ van szükségünk prompttervezésre. A válasz abban rejlik, hogy a jelenlegi LLM-ek számos kihívást jelentenek, amelyek megnehezítik a _megbízható és következetes kiegészítések_ elérését anélkül, hogy erőfeszítést tennénk az utasítások megalkotásába és optimalizálásába. Például:

1. **A modell válaszai sztochasztikusak.** Ugyanaz az _utasítás_ valószínűleg különböző válaszokat eredményez különböző modellekkel vagy modellverziókkal. És még ugyanazzal a _modellel_ is eltérő eredményeket adhat különböző időpontokban. _A prompttervezési technikák segíthetnek minimalizálni ezeket a variációkat jobb irányelvek biztosításával_.

1. **A modellek kitalálhatnak válaszokat.** A modellek _nagy, de véges_ adathalmazokkal vannak előképzve, ami azt jelenti, hogy hiányzik a tudásuk a képzési körön kívüli fogalmakról. Ennek eredményeként olyan kiegészítéseket hozhatnak létre, amelyek pontatlanok, képzeletbeliek vagy közvetlenül ellentmondanak ismert tényeknek. _A prompttervezési technikák segítenek a felhasználóknak az ilyen kitalálások azonosításában és enyhítésében, például az AI-tól idézetek vagy érvelés kérésével_.

1. **A modellek képességei eltérőek lesznek.** Az újabb modellek vagy modellgenerációk gazdagabb kép
Egy webes keresés azt mutatta, hogy léteznek kitalált történetek (pl. televíziós sorozatok vagy könyvek) a marsi háborúkról – de egyik sem 2076-ban. A józan ész azt is sugallja, hogy 2076 _a jövőben van_, így nem köthető valódi eseményhez.

Mi történik, ha ezt a feladatot különböző LLM szolgáltatókkal futtatjuk?

> **Válasz 1**: OpenAI Playground (GPT-35)

![Válasz 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.hu.png)

> **Válasz 2**: Azure OpenAI Playground (GPT-35)

![Válasz 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.hu.png)

> **Válasz 3**: Hugging Face Chat Playground (LLama-2)

![Válasz 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.hu.png)

Ahogy várható volt, minden modell (vagy modellverzió) kissé eltérő válaszokat ad, köszönhetően a sztochasztikus viselkedésnek és a modell képességeinek különbségeinek. Például az egyik modell egy 8. osztályos közönséget céloz meg, míg a másik középiskolás diákokra gondol. Mindhárom modell azonban olyan válaszokat generált, amelyek meggyőzhetik egy tájékozatlan felhasználót arról, hogy az esemény valódi.

A prompttervezési technikák, mint például a _metaprompting_ és a _hőmérséklet konfiguráció_, bizonyos mértékig csökkenthetik a modell által generált téves információkat. Az új prompttervezési _architektúrák_ szintén zökkenőmentesen integrálnak új eszközöket és technikákat a promptfolyamatba, hogy enyhítsék vagy csökkentsék ezeket a hatásokat.

## Esettanulmány: GitHub Copilot

Zárjuk le ezt a részt azzal, hogy megvizsgáljuk, hogyan használják a prompttervezést valós megoldásokban, egy esettanulmányon keresztül: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

A GitHub Copilot az "AI páros programozója" – szöveges promptokat alakít át kódkiegészítésekké, és integrálva van a fejlesztési környezetedbe (pl. Visual Studio Code), hogy zökkenőmentes felhasználói élményt nyújtson. Az alábbi blogok sorozatában dokumentáltak szerint a legkorábbi verzió az OpenAI Codex modellen alapult – a mérnökök gyorsan felismerték a modell finomhangolásának és jobb prompttervezési technikák kidolgozásának szükségességét a kódminőség javítása érdekében. Júliusban [bemutatták egy továbbfejlesztett AI modellt, amely túlmutat a Codexen](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), még gyorsabb javaslatok érdekében.

Olvasd el a bejegyzéseket sorrendben, hogy nyomon követhesd a tanulási folyamatukat.

- **2023. május** | [GitHub Copilot egyre jobban érti a kódodat](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023. május** | [GitHub belülről: Együttműködés az LLM-ekkel a GitHub Copilot mögött](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023. június** | [Hogyan írjunk jobb promptokat a GitHub Copilot számára](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **2023. július** | [.. GitHub Copilot túlmutat a Codexen egy továbbfejlesztett AI modellel](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023. július** | [Fejlesztői útmutató a prompttervezéshez és LLM-ekhez](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023. szeptember** | [Hogyan építsünk vállalati LLM alkalmazást: Tanulságok a GitHub Copilotból](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Böngészheted az [Engineering blogjukat](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) további bejegyzésekért, például [ezt](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), amely bemutatja, hogyan alkalmazzák ezeket a modelleket és technikákat valós alkalmazások fejlesztésére.

---

<!--
LECKE SABLON:
Ez az egység a 2. alapfogalmat kell, hogy lefedje.
Erősítsd meg a fogalmat példákkal és hivatkozásokkal.

FOGALOM #2:
Prompttervezés.
Példákkal illusztrálva.
-->

## Prompt Felépítése

Láttuk, miért fontos a prompttervezés – most értsük meg, hogyan _épülnek fel_ a promptok, hogy értékelni tudjuk a különböző technikákat a hatékonyabb prompttervezés érdekében.

### Alapvető Prompt

Kezdjük az alapvető prompttal: egy szöveges bemenet, amelyet a modellnek küldünk további kontextus nélkül. Íme egy példa – amikor az Egyesült Államok nemzeti himnuszának első néhány szavát küldjük az OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) számára, az azonnal _kiegészíti_ a választ a következő sorokkal, bemutatva az alapvető előrejelzési viselkedést.

| Prompt (Bemenet) | Completion (Kimenet)                                                                                                                        |
| :--------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Úgy tűnik, hogy az Egyesült Államok nemzeti himnuszának, a "The Star-Spangled Banner"-nek a szövegét kezded. A teljes szöveg így hangzik... |

### Összetett Prompt

Most adjunk kontextust és utasításokat az alapvető prompthoz. A [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lehetővé teszi, hogy egy összetett promptot _üzenetek_ gyűjteményeként állítsunk össze:

- Bemenet/kimenet párok, amelyek tükrözik a _felhasználói_ bemenetet és az _asszisztens_ válaszát.
- Rendszerüzenet, amely beállítja az asszisztens viselkedésének vagy személyiségének kontextusát.

A kérés most az alábbi formában van, ahol a _tokenizálás_ hatékonyan rögzíti a kontextusból és a beszélgetésből származó releváns információkat. Most a rendszer kontextusának megváltoztatása ugyanolyan hatással lehet a kimenetek minőségére, mint a megadott felhasználói bemenetek.

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

| Prompt (Bemenet)                                                                                                                                                                                                                         | Completion (Kimenet)                                                                                                        | Utasítás Típusa     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Írj egy leírást az amerikai polgárháborúról                                                                                                                                                                                                   | _egyszerű bekezdést adott vissza_                                                                                              | Egyszerű              |
| Írj egy leírást az amerikai polgárháborúról. Adj meg kulcsfontosságú dátumokat és eseményeket, és írd le azok jelentőségét.                                                                                                                                     | _bekezdést adott vissza, majd egy listát kulcsfontosságú események dátumaival és leírásaival_                                             | Összetett             |
| Írj egy leírást az amerikai polgárháborúról 1 bekezdésben. Adj meg 3 pontot kulcsfontosságú dátumokkal és azok jelentőségével. Adj meg további 3 pontot kulcsfontosságú történelmi személyekkel és hozzájárulásaikkal. Add vissza az eredményt JSON fájl formátumban. | _részletesebb információkat adott vissza egy szövegdobozban, JSON formátumban, amelyet másolhatsz és fájlba illeszthetsz, majd validálhatsz_ | Összetett. Formázott. |

## Elsődleges Tartalom

A fenti példákban a prompt még mindig meglehetősen nyitott volt, lehetővé téve az LLM számára, hogy eldöntse, melyik része az előre betanított adatbázisának releváns. Az _elsődleges tartalom_ tervezési mintával a bemeneti szöveg két részre oszlik:

- egy utasítás (cselekvés)
- releváns tartalom (amely befolyásolja a cselekvést)

Íme egy példa, ahol az utasítás az, hogy "foglalja össze ezt 2 mondatban".

| Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Kimenet)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A Jupiter az ötödik bolygó a Naptól, és a legnagyobb a Naprendszerben. Ez egy gázóriás, amelynek tömege az ezredrésze a Napénak, de két és félszerese az összes többi bolygó együttes tömegének. A Jupiter az egyik legfényesebb objektum, amely szabad szemmel látható az éjszakai égbolton, és az ősi civilizációk már a történelem előtti idők óta ismerik. A római Jupiter istenről nevezték el. A Földről nézve a Jupiter elég fényes lehet ahhoz, hogy visszavert fénye látható árnyékokat vessen, és átlagosan a harmadik legfényesebb természetes objektum az éjszakai égbolton a Hold és a Vénusz után. <br/> **Foglalja össze ezt 2 rövid mondatban** | A Jupiter, az ötödik bolygó a Naptól, a legnagyobb a Naprendszerben, és az egyik legfényesebb objektum az éjszakai égbolton. A római Jupiter istenről elnevezett gázóriás tömege két és félszerese az összes többi bolygó együttes tömegének. |

Az elsődleges tartalom szegmens különböző módokon használható fel a hatékonyabb utasítások érdekében:

- **Példák** – ahelyett, hogy explicit utasítást adnánk a modellnek, hogy mit tegyen, adjunk neki példákat arra, mit kell tennie, és hagyjuk, hogy következtessen a mintára.
- **Célzások** – kövesd az utasítást egy "célzással", amely előkészíti a kiegészítést, irányítva a modellt a relevánsabb válaszok felé.
- **Sablonok** – ezek ismételhető "receptek" promptokhoz, amelyek helyőrzőket (változókat) tartalmaznak, és testreszabhatók adatokkal konkrét felhasználási esetekhez.

Nézzük meg ezeket működés közben.

### Példák Használata

Ez egy olyan megközelítés, ahol az elsődleges tartalmat arra használjuk, hogy "etessük a modellt" néhány példával a kívánt kimenetről egy adott utasítás esetén, és hagyjuk, hogy következtessen a kívánt kimenet mintájára. A megadott példák számától függően lehet nulladik lövéses promptolás, egy lövéses promptolás, néhány lövéses promptolás stb.

A prompt most három összetevőből áll:

- Feladatleírás
- Néhány példa a kívánt kimenetre
- Egy új példa kezdete (amely implicit feladatleírássá válik)

| Tanulási Típus | Prompt (Bemenet)                                                                                                                                        | Completion (Kimenet)         |
| :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Nulladik lövés | "Süt a Nap". Fordítsd le spanyolra                                                                                                            | "El Sol está brillando".    |
| Egy lövés      | "Süt a Nap" => ""El Sol está brillando". <br> "Hideg és szeles nap van" =>                                                                 | "Es un día frío y ventoso". |
| Néhány lövés   | A játékos körbefutotta a bázisokat => Baseball <br/> A játékos ászt ütött => Tenisz <br/> A játékos hatost ütött => Krikett <br/> A játékos zsákolt => | Kosárlabda                  |
|               |                                                                                                                                                       |                             |

Figyeld meg, hogy explicit utasítást kellett adni ("Fordítsd le spanyolra") a nulladik lövéses promptolásban, de ez következtetésre kerül az egy lövéses promptolás példájában. A néhány lövéses példa azt mutatja, hogy több példa hozzáadása lehetővé teszi a modellek számára, hogy pontosabb következtetéseket vonjanak le további utasítások nélkül.

### Prompt Célzások

Egy másik technika az elsődleges tartalom használatára, hogy _célzásokat_ adjunk példák helyett. Ebben az esetben a modellt a kívánt válaszformátumot tükröző részlettel _indítjuk el_. A modell ezután "veszi a célzást", és folytatja ebben a szellemben.

| Célzások Száma | Prompt (Bemenet)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Kimenet)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | A Jupiter az ötödik bolygó a Naptól, és a legnagyobb a Naprendszerben. Ez egy gázóriás, amelynek tömege az ezredrésze a Napénak, de két és félszerese az összes többi bolygó együttes tömegének. A Jupiter az egyik legfényesebb objektum, amely szabad szemmel látható az éjszakai égbolton, és az ősi civilizációk már a történelem előtti idők óta ismerik. <br/>**Foglalja Össze**                                       | A Jupiter a legnagyobb bolygó a Naprendszerben, és az ötödik a Naptól. Ez egy gázóriás, amelynek tömege az összes többi bolygó együttes tömegének két és félszerese. Az ősi civilizációk régóta ismerik, és könnyen látható az éjszakai égbolton. |
| 1              | A Jupiter az ötödik bolygó a Naptól és a legnagyobb a Naprendszerben. Ez egy gázóriás, amelynek tömege az ezredrésze a Nap tömegének, de két és félszerese az összes többi bolygó tömegének együttvéve. A Jupiter az egyik legfényesebb objektum, amely szabad szemmel látható az éjszakai égbolton, és már az ősi civilizációk is ismerték a történelem előtti idők óta. <br/>**Összefoglalás** <br/> Amit megtanultunk, hogy a Jupiter | az ötödik bolygó a Naptól és a legnagyobb a Naprendszerben. Ez egy gázóriás, amelynek tömege az ezredrésze a Nap tömegének, de két és félszerese az összes többi bolygó tömegének együttvéve. Könnyen látható szabad szemmel, és már az ősi idők óta ismert.                        |
| 2              | A Jupiter az ötödik bolygó a Naptól és a legnagyobb a Naprendszerben. Ez egy gázóriás, amelynek tömege az ezredrésze a Nap tömegének, de két és félszerese az összes többi bolygó tömegének együttvéve. A Jupiter az egyik legfényesebb objektum, amely szabad szemmel látható az éjszakai égbolton, és már az ősi civilizációk is ismerték a történelem előtti idők óta. <br/>**Összefoglalás** <br/> A 3 legfontosabb tény, amit megtanultunk:         | 1. A Jupiter az ötödik bolygó a Naptól és a legnagyobb a Naprendszerben. <br/> 2. Ez egy gázóriás, amelynek tömege az ezredrésze a Nap tömegének...<br/> 3. A Jupiter szabad szemmel látható már az ősi idők óta ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt sablonok

Egy prompt sablon egy _előre meghatározott recept egy prompthoz_, amelyet el lehet menteni és szükség esetén újra felhasználni, hogy következetesebb felhasználói élményeket érjünk el nagy léptékben. A legegyszerűbb formájában ez egyszerűen egy gyűjtemény prompt példákból, mint [ez az OpenAI-tól](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), amely tartalmazza az interaktív prompt komponenseket (felhasználói és rendszerüzenetek) és az API-alapú kérés formátumát - a könnyebb újrafelhasználás érdekében.

Komplexebb formájában, mint [ez a példa LangChain-től](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), _helyettesítőket_ tartalmaz, amelyeket különböző forrásokból származó adatokkal (felhasználói bemenet, rendszerkörnyezet, külső adatforrások stb.) lehet helyettesíteni, hogy dinamikusan generáljunk egy promptot. Ez lehetővé teszi, hogy létrehozzunk egy újrafelhasználható promptok könyvtárát, amelyeket programozottan lehet használni következetes felhasználói élmények elérésére nagy léptékben.

Végül a sablonok valódi értéke abban rejlik, hogy képesek _prompt könyvtárakat_ létrehozni és publikálni vertikális alkalmazási területek számára - ahol a prompt sablon most _optimalizált_ az alkalmazás-specifikus kontextus vagy példák tükrözésére, amelyek relevánsabbá és pontosabbá teszik a válaszokat a célzott felhasználói közönség számára. A [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository remek példa erre a megközelítésre, amely egy prompt könyvtárat kurál az oktatási terület számára, hangsúlyt fektetve kulcsfontosságú célokra, mint például óratervezés, tanterv kialakítása, diákok mentorálása stb.

## Támogató tartalom

Ha a prompt konstrukciót úgy tekintjük, mint egy utasítást (feladat) és egy célt (elsődleges tartalom), akkor a _másodlagos tartalom_ olyan további kontextus, amelyet azért biztosítunk, hogy **valamilyen módon befolyásoljuk a kimenetet**. Ez lehet hangolási paraméterek, formázási utasítások, témakör taxonómiák stb., amelyek segíthetnek a modellnek _testreszabni_ a válaszát a kívánt felhasználói célokhoz vagy elvárásokhoz.

Például: Adott egy tanfolyam katalógus, amely kiterjedt metaadatokat tartalmaz (név, leírás, szint, metaadat címkék, oktató stb.) az összes elérhető tanfolyamról a tantervben:

- meghatározhatunk egy utasítást, hogy "összefoglaljuk a 2023-as őszi tanfolyam katalógust"
- az elsődleges tartalmat használhatjuk néhány példa biztosítására a kívánt kimenetről
- a másodlagos tartalmat használhatjuk az 5 legfontosabb "címke" azonosítására.

Most a modell képes lesz összefoglalót nyújtani a példák által mutatott formátumban - de ha egy eredménynek több címkéje van, akkor prioritást adhat az 5 azonosított címkének a másodlagos tartalomban.

---

<!--
LECKE SABLON:
Ez az egység az 1. alapfogalmat kell, hogy lefedje.
Erősítse meg a fogalmat példákkal és hivatkozásokkal.

FOGALOM #3:
Prompt mérnöki technikák.
Melyek az alapvető technikák a prompt mérnökségben?
Mutassa be gyakorlatokkal.
-->

## Promptolási legjobb gyakorlatok

Most, hogy tudjuk, hogyan lehet a promptokat _felépíteni_, elkezdhetünk gondolkodni azon, hogyan lehet őket _megtervezni_, hogy tükrözzék a legjobb gyakorlatokat. Ezt két részre oszthatjuk - a megfelelő _hozzáállás_ kialakítása és a megfelelő _technikák_ alkalmazása.

### Prompt mérnöki hozzáállás

A prompt mérnökség egy próbálkozás és hibázás folyamat, ezért három széles irányelvet tartsunk szem előtt:

1. **A terület ismerete számít.** A válasz pontossága és relevanciája az alkalmazás vagy felhasználó működési _területének_ függvénye. Használja intuícióját és szakértelmét a **technikák testreszabására**. Például határozzon meg _terület-specifikus személyiségeket_ a rendszer promptjaiban, vagy használjon _terület-specifikus sablonokat_ a felhasználói promptokban. Biztosítson másodlagos tartalmat, amely tükrözi a terület-specifikus kontextusokat, vagy használjon _terület-specifikus utalásokat és példákat_, hogy a modellt ismerős használati minták felé irányítsa.

2. **A modell ismerete számít.** Tudjuk, hogy a modellek sztochasztikusak. De a modell implementációk is eltérhetnek az általuk használt tanítási adathalmaz (előre tanított tudás), az általuk nyújtott képességek (pl. API vagy SDK révén) és az általuk optimalizált tartalom típusa (pl. kód vs. képek vs. szöveg) tekintetében. Értsük meg az általunk használt modell erősségeit és korlátait, és használjuk ezt a tudást a _feladatok prioritásának_ meghatározására vagy _testreszabott sablonok_ létrehozására, amelyek optimalizáltak a modell képességeihez.

3. **Iteráció és validáció számít.** A modellek gyorsan fejlődnek, és a prompt mérnökség technikái is. Mint területi szakértő, lehet, hogy van más kontextus vagy kritérium, amely _az Ön_ specifikus alkalmazására vonatkozik, és nem alkalmazható a szélesebb közösségre. Használja a prompt mérnökség eszközeit és technikáit a prompt konstrukció "beindítására", majd iterálja és validálja az eredményeket saját intuíciója és szakértelme alapján. Rögzítse meglátásait, és hozzon létre egy **tudásbázist** (pl. prompt könyvtárakat), amelyeket mások új alapként használhatnak a jövőbeli gyorsabb iterációkhoz.

## Legjobb gyakorlatok

Most nézzük meg a [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) és [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) szakemberek által ajánlott leggyakoribb legjobb gyakorlatokat.

| Mi                              | Miért                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Értékelje a legújabb modelleket.       | Az új modellgenerációk valószínűleg javított funkciókkal és minőséggel rendelkeznek - de magasabb költségekkel is járhatnak. Értékelje őket hatásuk alapján, majd hozzon döntést a migrációról.                                                                                |
| Válassza szét az utasításokat és a kontextust   | Ellenőrizze, hogy a modell/szolgáltató meghatároz-e _elválasztókat_, amelyek egyértelműbben megkülönböztetik az utasításokat, az elsődleges és másodlagos tartalmat. Ez segíthet a modelleknek pontosabban súlyozni a tokeneket.                                                         |
| Legyen specifikus és egyértelmű             | Adjon több részletet a kívánt kontextusról, eredményről, hosszúságról, formátumról, stílusról stb. Ez javítja a válaszok minőségét és következetességét. Rögzítse a recepteket újrafelhasználható sablonokban.                                                          |
| Legyen leíró, használjon példákat      | A modellek jobban reagálhatnak egy "mutasd és mondd" megközelítésre. Kezdje egy `zero-shot` megközelítéssel, ahol csak utasítást ad (de nincs példa), majd próbálja ki a `few-shot` finomítást, néhány példa biztosításával a kívánt kimenetre. Használjon analógiákat. |
| Használjon utalásokat a válaszok beindításához | Irányítsa a kívánt eredmény felé, ha megad néhány vezető szót vagy kifejezést, amelyeket a modell kiindulási pontként használhat a válaszhoz.                                                                                                               |
| Ismételje meg                       | Néha szükség lehet arra, hogy megismételje magát a modell számára. Adjon utasításokat az elsődleges tartalom előtt és után, használjon utasítást és utalást stb. Iterálja és validálja, hogy mi működik.                                                         |
| A sorrend számít                     | Az információk bemutatásának sorrendje a modell számára befolyásolhatja a kimenetet, még a tanulási példákban is, a frissességi torzítás miatt. Próbáljon ki különböző opciókat, hogy lássa, mi működik a legjobban.                                                               |
| Adjon a modellnek egy "kibúvót"           | Adjon a modellnek egy _visszaesési_ válaszlehetőséget, amelyet akkor adhat, ha valamilyen okból nem tudja teljesíteni a feladatot. Ez csökkentheti annak esélyét, hogy a modellek hamis vagy kitalált válaszokat generáljanak.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Mint minden legjobb gyakorlat esetében, ne feledje, hogy _az Ön tapasztalata eltérhet_ a modelltől, a feladattól és a területtől függően. Használja ezeket kiindulópontként, és iterálja, hogy megtalálja, mi működik a legjobban az Ön számára. Folyamatosan értékelje újra a prompt mérnökségi folyamatát, ahogy új modellek és eszközök válnak elérhetővé, a folyamat skálázhatóságára és a válaszok minőségére összpontosítva.

<!--
LECKE SABLON:
Zárja le a szakaszt egy összefoglalóval és önálló tanulási forrásokkal.
-->

## Tudásellenőrzés

Melyik a jó prompt a legjobb gyakorlatok alapján?

1. Mutass egy képet egy piros autóról
2. Mutass egy képet egy piros autóról, amely Volvo márkájú, XC90 modell, egy szikla mellett parkol, naplementében
3. Mutass egy képet egy piros autóról, amely Volvo márkájú, XC90 modell

A: 2, ez a legjobb prompt, mivel részleteket ad arról, hogy "mi" és konkrétumokba megy (nem csak bármilyen autó, hanem egy konkrét márka és modell), és leírja az általános környezetet is. A 3 a következő legjobb, mivel szintén sok leírást tartalmaz.

## 🚀 Kihívás

Próbálja ki az "utalás" technikát a következő prompttal: Fejezze be a mondatot "Mutass egy képet egy piros autóról, amely Volvo márkájú és ". Mit válaszol, és hogyan javítaná?

## Nagyszerű munka! Folytassa a tanulást

Szeretne többet megtudni a különböző Prompt mérnökségi fogalmakról? Látogasson el a [folytatott tanulási oldalra](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy további nagyszerű forrásokat találjon a témában.

Lépjen tovább az 5. leckére, ahol [haladó prompt technikákat](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) fogunk megvizsgálni!

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.