<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T21:30:19+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "hu"
}
-->
[![Nyílt forráskódú modellek](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.hu.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# LLM finomhangolása

A nagy nyelvi modellek használata generatív AI alkalmazások építéséhez új kihívásokkal jár. Az egyik kulcsfontosságú kérdés az, hogy biztosítsuk a modell által generált tartalom válaszainak minőségét (pontosság és relevancia) egy adott felhasználói kérésre. Az előző leckékben olyan technikákról beszéltünk, mint a prompt engineering és a retrieval-augmented generation, amelyek a problémát a meglévő modell _prompt inputjának módosításával_ próbálják megoldani.

A mai leckében egy harmadik technikáról, a **finomhangolásról** beszélünk, amely a kihívást a modell _újratanításával_ próbálja kezelni további adatokkal. Merüljünk el a részletekben.

## Tanulási célok

Ez a lecke bemutatja a finomhangolás fogalmát az előre betanított nyelvi modellek esetében, feltárja ennek az eljárásnak az előnyeit és kihívásait, valamint útmutatást nyújt arra vonatkozóan, hogy mikor és hogyan használjuk a finomhangolást a generatív AI modellek teljesítményének javítására.

A lecke végére képes leszel megválaszolni a következő kérdéseket:

- Mi az a finomhangolás a nyelvi modellek esetében?
- Mikor és miért hasznos a finomhangolás?
- Hogyan lehet finomhangolni egy előre betanított modellt?
- Milyen korlátai vannak a finomhangolásnak?

Készen állsz? Kezdjük el.

## Illusztrált útmutató

Szeretnéd átlátni, miről lesz szó, mielőtt belevágunk? Nézd meg ezt az illusztrált útmutatót, amely bemutatja a tanulási folyamatot ebben a leckében – az alapfogalmak és a finomhangolás motivációjának megismerésétől kezdve a folyamat és a legjobb gyakorlatok megértéséig a finomhangolási feladat végrehajtásához. Ez egy izgalmas téma a felfedezéshez, ezért ne felejtsd el megnézni a [Források](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) oldalt további linkekért, amelyek támogatják az önálló tanulási utadat!

![Illusztrált útmutató a nyelvi modellek finomhangolásához](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.hu.png)

## Mi az a finomhangolás a nyelvi modellek esetében?

Definíció szerint a nagy nyelvi modellek _előre betanítottak_, és hatalmas mennyiségű szövegen alapulnak, amelyeket különböző forrásokból, például az internetről gyűjtöttek. Ahogy az előző leckékben tanultuk, olyan technikákra van szükségünk, mint a _prompt engineering_ és a _retrieval-augmented generation_, hogy javítsuk a modell válaszainak minőségét a felhasználói kérdésekre ("prompts").

Egy népszerű prompt engineering technika az, hogy a modellnek több útmutatást adunk arról, hogy mi várható el a válaszban, akár _utasítások_ (egyértelmű útmutatás), akár _néhány példa_ (közvetett útmutatás) megadásával. Ezt _few-shot learningnek_ nevezzük, de két korlátja van:

- A modell tokenkorlátai korlátozhatják a megadható példák számát, és csökkenthetik a hatékonyságot.
- A modell tokenköltségei drágává tehetik a példák hozzáadását minden prompthoz, és csökkenthetik a rugalmasságot.

A finomhangolás egy általános gyakorlat a gépi tanulási rendszerekben, amely során egy előre betanított modellt új adatokkal újratanítunk, hogy javítsuk a teljesítményét egy adott feladaton. A nyelvi modellek kontextusában a finomhangolás során az előre betanított modellt _egy adott feladathoz vagy alkalmazási területhez gondosan kiválasztott példák halmazával_ tanítjuk újra, hogy egy **egyedi modellt** hozzunk létre, amely pontosabb és relevánsabb lehet az adott feladathoz vagy területhez. A finomhangolás egyik mellékhatása, hogy csökkentheti a few-shot learninghez szükséges példák számát – csökkentve a tokenhasználatot és a kapcsolódó költségeket.

## Mikor és miért kell finomhangolni a modelleket?

Ebben a kontextusban, amikor finomhangolásról beszélünk, a **felügyelt** finomhangolásra utalunk, ahol az újratanítás **új adatok hozzáadásával** történik, amelyek nem voltak részei az eredeti tanítási adathalmaznak. Ez különbözik a nem felügyelt finomhangolási megközelítéstől, ahol a modellt az eredeti adatokon tanítják újra, de eltérő hiperparaméterekkel.

A legfontosabb, hogy a finomhangolás egy haladó technika, amely bizonyos szintű szakértelmet igényel a kívánt eredmények eléréséhez. Ha helytelenül végezzük, nem biztos, hogy a várt javulásokat hozza, sőt, akár ronthatja is a modell teljesítményét a célzott területen.

Tehát mielőtt megtanulnád, "hogyan" kell finomhangolni a nyelvi modelleket, tudnod kell, "miért" érdemes ezt az utat választani, és "mikor" érdemes elkezdeni a finomhangolás folyamatát. Kezdd azzal, hogy felteszed magadnak ezeket a kérdéseket:

- **Felhasználási eset**: Mi a _felhasználási eseted_ a finomhangolásra? Mit szeretnél javítani az aktuális előre betanított modellen?
- **Alternatívák**: Kipróbáltál már _más technikákat_ a kívánt eredmények eléréséhez? Használd ezeket összehasonlítási alapként.
  - Prompt engineering: Próbálj ki olyan technikákat, mint a few-shot prompting releváns promptválaszok példáival. Értékeld a válaszok minőségét.
  - Retrieval Augmented Generation: Próbáld meg kiegészíteni a promtokat az adataid keresésével nyert lekérdezési eredményekkel. Értékeld a válaszok minőségét.
- **Költségek**: Azonosítottad a finomhangolás költségeit?
  - Finomhangolhatóság – elérhető-e az előre betanított modell finomhangolásra?
  - Erőfeszítés – az adatok előkészítésére, a modell értékelésére és finomítására fordított munka.
  - Számítási kapacitás – a finomhangolási feladatok futtatásához és a finomhangolt modell telepítéséhez szükséges erőforrások.
  - Adatok – elegendő minőségi példa áll rendelkezésre a finomhangolás hatásához.
- **Előnyök**: Megerősítetted a finomhangolás előnyeit?
  - Minőség – a finomhangolt modell felülmúlta az alapmodellt?
  - Költség – csökkenti a tokenhasználatot az egyszerűsített promtok révén?
  - Kiterjeszthetőség – új területekre is alkalmazható az alapmodell?

Ezekre a kérdésekre válaszolva el tudod dönteni, hogy a finomhangolás megfelelő megközelítés-e a felhasználási esetedhez. Ideális esetben a megközelítés csak akkor érvényes, ha az előnyök meghaladják a költségeket. Ha úgy döntesz, hogy folytatod, itt az ideje átgondolni, _hogyan_ finomhangolhatod az előre betanított modellt.

Szeretnél többet megtudni a döntéshozatali folyamatról? Nézd meg: [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Hogyan finomhangolhatunk egy előre betanított modellt?

Egy előre betanított modell finomhangolásához szükséged lesz:

- egy előre betanított modellre, amelyet finomhangolhatsz
- egy adathalmazra a finomhangoláshoz
- egy tanítási környezetre a finomhangolási feladat futtatásához
- egy hosztoló környezetre a finomhangolt modell telepítéséhez

## Finomhangolás a gyakorlatban

Az alábbi források lépésről lépésre bemutatják, hogyan végezheted el a finomhangolást egy kiválasztott modellen egy gondosan összeállított adathalmazzal. Ezeknek a bemutatóknak az elvégzéséhez szükséged lesz egy fiókra az adott szolgáltatónál, valamint hozzáférésre a releváns modellhez és adathalmazokhoz.

| Szolgáltató  | Bemutató                                                                                                                                                                       | Leírás                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Hogyan finomhangoljuk a chat modelleket](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)     | Tanuld meg, hogyan finomhangolj egy `gpt-35-turbo` modellt egy adott területre ("recept asszisztens") az adatok előkészítésével, a finomhangolási feladat futtatásával és a finomhangolt modell használatával.                                                                                                                                                                                                                     |
| Azure OpenAI | [GPT 3.5 Turbo finomhangolási bemutató](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Tanuld meg, hogyan finomhangolj egy `gpt-35-turbo-0613` modellt **az Azure-on** az adatok létrehozásával és feltöltésével, a finomhangolási feladat futtatásával. Telepítsd és használd az új modellt.                                                                                                                                                                                                                              |
| Hugging Face | [Nyelvi modellek finomhangolása a Hugging Face segítségével](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                        | Ez a blogbejegyzés bemutatja, hogyan finomhangolj egy _nyílt LLM_-et (pl.: `CodeLlama 7B`) a [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) könyvtár és a [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) segítségével, nyílt [adathalmazokkal](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) a Hugging Face-en. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Nyelvi modellek finomhangolása az AutoTrain segítségével](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                 | Az AutoTrain (vagy AutoTrain Advanced) egy Python könyvtár, amelyet a Hugging Face fejlesztett ki, és amely lehetővé teszi számos különböző feladat, köztük a nyelvi modellek finomhangolását. Az AutoTrain egy kódmentes megoldás, és a finomhangolás elvégezhető saját felhőben, a Hugging Face Spaces-en vagy helyileg. Támogatja a webalapú GUI-t, a CLI-t és a yaml konfigurációs fájlokon keresztüli tanítást. |

## Feladat

Válassz ki egyet a fenti bemutatók közül, és végezd el. _Előfordulhat, hogy ezeknek a bemutatóknak egy verzióját replikáljuk a Jupyter Notebookokban ebben a repóban csak referenciaként. Kérjük, használd közvetlenül az eredeti forrásokat a legfrissebb verziók eléréséhez_.

## Szép munka! Folytasd a tanulást.

A lecke elvégzése után nézd meg a [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd a generatív AI ismereteidet!

Gratulálunk!! Befejezted a kurzus v2 sorozatának utolsó leckéjét! Ne hagyd abba a tanulást és az építést. **Nézd meg a [FORRÁSOK](RESOURCES.md?WT.mc_id=academic-105485-koreyst) oldalt további javaslatokért csak ehhez a témához.

Az első verziójú lecke sorozatunkat is frissítettük több feladattal és fogalommal. Szánj egy percet a tudásod felfrissítésére – és kérjük, [oszd meg kérdéseidet és visszajelzéseidet](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), hogy segíts nekünk javítani ezeket a leckéket a közösség számára.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelven tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.