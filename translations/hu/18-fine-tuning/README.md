<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T18:52:51+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "hu"
}
-->
[![Open Source Models](../../../../../translated_images/hu/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# LLM finomhangolása

A nagy nyelvi modellek alkalmazása generatív MI alkalmazások építéséhez új kihívásokkal jár. Egy kulcskérdés a válaszok minőségének (pontosság és relevancia) biztosítása a modell által egy adott felhasználói kérésre generált tartalomban. Korábbi leckékben olyan technikákat tárgyaltunk, mint a prompt mérnöki munka és a visszakereséssel bővített generálás, amelyek a problémát a _meglévő modell prompt bemenetének módosításával_ próbálják megoldani.

A mai leckében egy harmadik technikát, a **finomhangolást** tárgyaljuk, amely a kihívást úgy próbálja megoldani, hogy _magát a modellt újradolgozza_ további adatokkal. Merüljünk el a részletekben.

## Tanulási célok

Ez a lecke bevezeti a finomhangolás fogalmát az előre betanított nyelvi modellek esetén, feltárja ennek az eljárásnak az előnyeit és kihívásait, valamint útmutatást ad arra, mikor és hogyan érdemes finomhangolást alkalmazni generatív MI modelljei teljesítményének javítására.

A lecke végére képesnek kell lenned az alábbi kérdések megválaszolására:

- Mi a finomhangolás nyelvi modelleknél?
- Mikor és miért hasznos a finomhangolás?
- Hogyan lehet finomhangolni egy előre betanított modellt?
- Melyek a finomhangolás korlátai?

Készen állsz? Kezdjünk hozzá.

## Illusztrált útmutató

Szeretnéd látni a teljes képét annak, amit tárgyalni fogunk, mielőtt belemerülnénk? Nézd meg ezt az illusztrált útmutatót, amely bemutatja a lecke tanulási útját – a finomhangolás alapvető fogalmának és motivációjának megértésétől a finomhangolási folyamat és a legjobb gyakorlatok megértéséig. Ez egy lenyűgöző témakör, ezért ne feledd megnézni a [Források](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) oldalt is, ahol további linkeket találsz az önálló tanuláshoz!

![Illusztrált útmutató a nyelvi modellek finomhangolásához](../../../../../translated_images/hu/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Mi a finomhangolás nyelvi modelleknél?

Definíció szerint a nagy nyelvi modellek _előre betanítottak_ nagy mennyiségű szövegen, amelyek különböző forrásokból, köztük az internetről származnak. Ahogy korábbi leckéinkből megtanultuk, olyan technikákra van szükségünk, mint a _prompt mérnöki munka_ és a _visszakereséssel bővített generálás_, hogy javítsuk a modell válaszainak minőségét a felhasználói kérdésekre („promptokra”).

Egy népszerű prompt-mérnöki technika, hogy a modellt több iránymutatással látjuk el a válasz tekintetében, akár _utasításokkal_ (explicit iránymutatás), akár _néhány példával_ (implicit iránymutatás). Ezt nevezik _few-shot learningnek_, de ennek két korlátja van:

- A modell token-korlátai korlátozhatják az adható példák számát, és csökkenthetik hatékonyságát.
- A modell token költségei megdrágíthatják, ha minden promptba példákat teszünk, és korlátozzák a rugalmasságot.

A finomhangolás egy széles körben használt eljárás gépi tanulási rendszerekben, ahol egy előre betanított modellt új adatokkal újra tanítunk annak érdekében, hogy javítsuk a teljesítményét egy specifikus feladatban. A nyelvi modellek esetén az előre betanított modellt finomhangolhatjuk _egy szelektált példagyűjteménnyel egy adott feladatra vagy alkalmazási területre_, hogy egy **egyedi modellt** hozzunk létre, amely pontosabb és relevánsabb lehet az adott feladat vagy terület számára. A finomhangolás egyik mellékhatása az is, hogy csökkentheti a few-shot learninghez szükséges példák számát – így kevesebb token használatával és az azzal járó költségek csökkentésével jár.

## Mikor és miért érdemes finomhangolni a modelleket?

Ebben az összefüggésben, amikor finomhangolásról beszélünk, **felügyelt** finomhangolásról van szó, ahol az újratanítás úgy történik, hogy **új adatokat adunk hozzá**, amelyek nem voltak részei az eredeti tanuló adatkészletnek. Ez különbözik az unsupervised (felügyelet nélküli) finomhangolástól, ahol a modellt az eredeti adatokon tanítják újra, de eltérő hiperparaméterekkel.

A legfontosabb, amit meg kell jegyezni: a finomhangolás egy fejlett technika, amely bizonyos fokú szakértelmet igényel a kívánt eredmények eléréséhez. Hibás alkalmazás esetén nem hozhatja a várt javulást, sőt ronthatja a modell teljesítményét a céltartományban.

Ezért mielőtt megtanulnád, "hogyan" kell finomhangolni a nyelvi modelleket, tudnod kell, "miért" érdemes ezt az utat választani, és "mikor" kell elkezdeni a finomhangolási folyamatot. Tedd fel magadnak a következő kérdéseket:

- **Használati eset**: Mi az a _használati eset_, amelyhez finomhangolni szeretnéd? Mely aspektusát akarod javítani a jelenlegi előre betanított modellnek?
- **Alternatívák**: Kipróbáltál _más technikákat_ a kívánt eredmények elérésére? Használd őket kiindulási alapnak az összehasonlításhoz.
  - Prompt mérnöki munka: Próbáld ki például a few-shot promptolást példákkal a releváns válaszokról. Értékeld a válaszok minőségét.
  - Visszakeresés-alapú generálás: Próbáld meg bővíteni a promptokat lekérdezési eredményekkel, amelyeket a saját adatbázisodból keresel ki. Értékeld a válaszok minőségét.
- **Költségek**: Felmértél minden finomhangolással járó költséget?
  - Finomhangolhatóság – elérhető-e az előre betanított modell a finomhangoláshoz?
  - Erőfeszítés – az adatok előkészítése, a modell értékelése és finomítása
  - Számítástechnikai erőforrások – a finomhangolási feladatok futtatásához és a finomhangolt modell telepítéséhez
  - Adatok – elegendő minőségű példa biztosítása a finomhangolás hatásához
- **Előnyök**: Megerősítetted a finomhangolás előnyeit?
  - Minőség – a finomhangolt modell jobb lett-e a kiindulási alapnál?
  - Költség – csökkenti-e a tokenhasználatot a promptok egyszerűsítésével?
  - Kiterjeszthetőség – új tartományokra is átalakítható az alapmodell?

E kérdések megválaszolásával el tudod dönteni, hogy a finomhangolás megfelelő megközelítés-e az adott használati esethez. Ideális esetben ezt a módszert csak akkor alkalmazd, ha az előnyök meghaladják a költségeket. Ha úgy döntesz, hogy folytatod, itt az ideje átgondolni, _hogyan_ finomhangold az előre betanított modellt.

Szeretnél további betekintést nyerni a döntési folyamatba? Nézd meg a [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs) videót.

## Hogyan lehet finomhangolni egy előre betanított modellt?

Ahhoz, hogy finomhangolj egy előre betanított modellt, szükséged van:

- egy előre betanított modellre finomhangoláshoz
- egy adatkészletre a finomhangoláshoz
- egy tréning környezetre a finomhangoló feladat futtatásához
- egy hoszting környezetre a finomhangolt modell telepítéséhez

## Finomhangolás a gyakorlatban

Az alábbi források lépésről lépésre mutatnak be oktatóanyagokat, amelyek egy kiválasztott modell és egy gondosan összeállított adathalmaz felhasználásával vezetik végig a finomhangolás folyamatát. Ezeknek az oktatóanyagoknak a végigviteléhez rendelkezni kell fiókkal az adott szolgáltatónál, valamint hozzáféréssel a releváns modellhez és adathalmazokhoz.

| Szolgáltató  | Oktatóanyag                                                                                                                                                                   | Leírás                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Chat modellek finomhangolása](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)              | Tanuld meg, hogyan finomhangolj egy `gpt-35-turbo` modellt egy adott területre („recept asszisztens”), az adatok előkészítésétől a finomhangoló feladat futtatásán át egészen a finomhangolt modell használatáig az inferenciához.                                                                                                                                                                                                |
| Azure OpenAI | [GPT 3.5 Turbo finomhangolási oktatóanyag](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Tanuld meg, hogyan finomhangolj egy `gpt-35-turbo-0613` modellt **az Azure-on** az adatok előkészítésétől és feltöltésétől, a finomhangoló folyamat futtatásán keresztül a modell telepítéséig és használatáig.                                                                                                                                                                                                                    |
| Hugging Face | [LLM-ek finomhangolása Hugging Face-szel](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                       | Ez a blogbejegyzés végigvezet egy _nyílt LLM_ (pl. `CodeLlama 7B`) finomhangolásán a [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) könyvtár és a [Transformer megerősítéses tanulás (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) használatával, valamint nyílt [adatkészleteken](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) a Hugging Face-en. |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🤗 AutoTrain | [LLM-ek finomhangolása AutoTrain segítségével](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                         | Az AutoTrain (vagy AutoTrain Advanced) egy python könyvtár a Hugging Face-től, amely sokféle feladathoz teszi lehetővé a finomhangolást, beleértve az LLM finomhangolást is. Az AutoTrain egy kód nélküli megoldás; a finomhangolás történhet a saját felhődben, a Hugging Face Spaces-en vagy lokálisan. Támogat webes GUI-t, parancssori felületet (CLI) és yaml konfigurációs fájlokon alapuló tréninget.                                           |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🦥 Unsloth      | [LLM-ek finomhangolása Unsloth segítségével](https://github.com/unslothai/unsloth)                                                                             | Az Unsloth egy nyílt forráskódú keretrendszer, amely támogatja az LLM finomhangolást és megerősítéses tanulást (RL). Az Unsloth leegyszerűsíti a helyi tréninget, értékelést és telepítést kész notebookok segítségével. Továbbá támogatja a szöveg-beszéd konverziót (TTS), BERT és multimodális modelleket is. Kezdéshez olvasd el az általuk készített lépésről lépésre szóló [Finomhangolás LLM-ekhez útmutatót](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
## Feladat

Válassz ki egy fenti oktatóanyagot és dolgozd végig. _Ezekből az oktatóanyagokból előfordulhat, hogy készítünk egy verziót Jupyter Notebook formátumban ebben a repóban csak tájékoztatásul. Azonban a legfrissebb változatokért mindig az eredeti forrásokat használd._

## Remek munka! Folytasd a tanulást.

A lecke elvégzése után nézd meg a [Generatív MI tanulási gyűjteményt](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd generatív MI ismereteidet!

Gratulálunk!! Teljesítetted a kurzus v2 sorozatának utolsó leckéjét! Ne hagyd abba a tanulást és az építkezést. \*\*Nézd meg a [FORRÁSOK](RESOURCES.md?WT.mc_id=academic-105485-koreyst) oldalt, ahol további ajánlásokat találsz kizárólag ehhez a témakörhöz.

A v1 sorozatunk is frissült több feladattal és fogalommal. Szánj egy percet, hogy felfrissítsd a tudásod – és kérjük, [oszd meg kérdéseidet és visszajelzéseidet](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), hogy segíts fejlődni ezeket a leckéket a közösség számára.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítószolgáltatás segítségével fordítottuk. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvű dokumentum tekintendő a hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->