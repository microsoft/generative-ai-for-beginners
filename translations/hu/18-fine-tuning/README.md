[![Nyílt Forráskódú Modellek](../../../translated_images/hu/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# LLM finomhangolása

Nagy nyelvi modellek használata generatív MI alkalmazások építéséhez új kihívásokat hoz magával. Egy kulcsfontosságú kérdés a válaszok minőségének (pontosság és relevancia) biztosítása az adott felhasználói kérésre a modell által generált tartalomban. Az előző leckékben olyan technikákat beszéltünk meg, mint a prompt tervezés és a visszakereséssel kiegészített generálás, amelyek megpróbálják a problémát a meglévő modell bemenetének _módosításával_ megoldani.

A mai leckében egy harmadik technikát, a **finomhangolást** tárgyaljuk, amely a kihívást azáltal próbálja kezelni, hogy a modellt _magát újratanítja_ kiegészítő adatokkal. Mélyedjünk el a részletekben.

## Tanulási célok

Ez a lecke bevezeti a finomhangolás fogalmát az előre betanított nyelvi modellek esetében, megvizsgálja a megközelítés előnyeit és kihívásait, valamint útmutatást ad arra, mikor és hogyan érdemes finomhangolást alkalmazni generatív MI modelljei teljesítményének javítására.

A lecke végére képes leszel megválaszolni a következő kérdéseket:

- Mi a finomhangolás a nyelvi modellek esetében?
- Mikor és miért hasznos a finomhangolás?
- Hogyan tudok egy előre betanított modellt finomhangolni?
- Milyen korlátai vannak a finomhangolásnak?

Készen állsz? Kezdjük.

## Illusztrált útmutató

Szeretnéd átlátni a főbb témákat, mielőtt belevágunk? Nézd meg ezt az illusztrált útmutatót, amely leírja a tanulási utat a finomhangolás főfogalmaitól és motivációjától kezdve a folyamat és a bevált gyakorlatok megértéséig. Ez egy lenyűgöző téma a felfedezésre, ezért ne felejtsd el felkeresni a [Források](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) oldalt további, önálló tanulást támogató anyagokért!

![Illusztrált útmutató a nyelvi modellek finomhangolásához](../../../translated_images/hu/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Mi a finomhangolás a nyelvi modellek esetében?

Definíció szerint a nagy nyelvi modelleket _előre betanítják_ nagy mennyiségű szövegre, amely különféle forrásokból, például az internetről származik. Ahogy az előző leckékből megtanultuk, szükségünk van olyan technikákra, mint a _prompt tervezés_ és a _visszakereséssel kiegészített generálás_, hogy javítsuk a modell válaszainak minőségét a felhasználói kérdésekre ("promptokra").

Egy népszerű prompt tervezési technika az, hogy a modell számára több útmutatást adunk arról, mit várunk el a válaszban, akár _utasításokkal_ (explicit útmutatás), akár _néhány példával_ (implicit útmutatás). Ezt nevezik _few-shot tanulásnak_, de ennek két korlátja van:

- A modell felhasználható token limitek korlátozhatják, hány példát adhatsz meg, és csökkenthetik a hatékonyságot.
- A tokenköltségek miatt drága lehet minden prompthoz példákat hozzáadni, ami korlátozza a rugalmasságot.

A finomhangolás egy gyakori gyakorlat a gépi tanulásban, amikor egy előre betanított modellt új adatokkal újratanítunk, hogy javítsuk a teljesítményét egy adott feladaton. A nyelvi modellek esetében finomhangolhatjuk az előre betanított modellt _egy adott feladathoz vagy alkalmazási területhez kiválasztott példák halmazával_, hogy létrehozzunk egy **egyedi modellt**, amely az adott feladat vagy terület számára pontosabb és relevánsabb lehet. A finomhangolás mellékhatásaként csökkentheti a few-shot tanuláshoz szükséges példák számát is – ezáltal csökkentve a tokenhasználatot és a költségeket.

## Mikor és miért érdemes finomhangolni a modelleket?

Ebben a _kontextusban_, amikor finomhangolásról beszélünk, az **felügyelt** finomhangolásra gondolunk, ahol az újratanítás az eredeti tanítóadatok részét nem képező **új adatok hozzáadásával** történik. Ez eltér a felügyelet nélküli finomhangolástól, amikor a modellt az eredeti adatokon újratanítják, de eltérő hiperparaméterekkel.

A legfontosabb emlékezni rá, hogy a finomhangolás egy fejlett technika, amely bizonyos szintű szakértelmet igényel a kívánt eredmények eléréséhez. Helytelen végrehajtás esetén nem biztos, hogy hozza a várt javulásokat, sőt ronthatja is a modell teljesítményét a célozni kívánt területen.

Ezért mielőtt megtanulnád "hogyan" finomhangold a nyelvi modelleket, tudnod kell, "miért" érdemes ezt az utat választani, és "mikor" érdemes elkezdeni a finomhangolási folyamatot. Kezdd azzal, hogy megválaszolod magadnak ezeket a kérdéseket:

- **Használati eset**: Mi a finomhangolás _használati esete_? Melyik aspektusát akarod javítani a jelenlegi előre betanított modellnek?
- **Alternatívák**: Próbáltál _más technikákat_ a kívánt eredmények elérésére? Használd őket az összehasonlításhoz.
  - Prompt tervezés: Próbáld ki például a few-shot promptokat releváns válaszpéldákkal. Értékeld a válaszok minőségét.
  - Visszakereséssel kiegészített generálás: Próbáld ki a promptok kiegészítését olyan lekérdezési eredményekkel, amelyeket az adataid keresésével nyersz. Értékeld a válaszok minőségét.
- **Költségek**: Azonosítottad a finomhangolás költségeit?
  - Hangolhatóság - elérhető az előre betanított modell finomhangolásra?
  - Erőfeszítés - az adatok előkészítéséhez, a modell értékeléséhez és finomításához
  - Számítási kapacitás - a finomhangolási feladatok futtatásához és a finomhangolt modell üzemeltetéséhez
  - Adatok - elegendő és megfelelő minőségű példa a finomhangoláshoz
- **Előnyök**: Megerősítetted a finomhangolás előnyeit?
  - Minőség - a finomhangolt modell felülmúlta az alapmodellt?
  - Költség - csökkenti-e a tokenhasználatot az egyszerűsített promptokkal?
  - Kiterjeszthetőség - új területekre tudod-e áthangolni az alapmodellt?

Ezekre a kérdésekre válaszolva eldöntheted, hogy a finomhangolás a megfelelő megközelítés-e az adott használati esetedhez. Ideális esetben a megközelítés csak akkor érvényes, ha az előnyök meghaladják a költségeket. Ha eldöntöd, hogy folytatod, ideje elgondolkodni azon, _hogyan_ tudod finomhangolni az előre betanított modellt.

Több információt szeretnél a döntéshozatali folyamatról? Nézd meg a [Finomhangolni vagy nem finomhangolni](https://www.youtube.com/watch?v=0Jo-z-MFxJs) videót.

## Hogyan tudunk finomhangolni egy előre betanított modellt?

Az előre betanított modell finomhangolásához szükséged van:

- egy előre betanított modellre, amit finomhangolhatsz
- egy adathalmazra, amit a finomhangoláshoz használsz
- egy tanulási környezetre, ahol a finomhangolási feladat futtatható
- egy hoszting környezetre, ahol a finomhangolt modellt deployolhatod

## Finomhangolás a gyakorlatban

> **Megjegyzés:** A `gpt-35-turbo` / `gpt-3.5-turbo`, amelyet az alábbi oktatóanyagokban hivatkoznak, lekerült a forgalomból mind az inferencia, mind a finomhangolás területén. Ha ma kezdesz új finomhangolási munkát, célzottan egy jelenleg támogatott modellt válassz – például a `gpt-4o-mini` vagy a `gpt-4.1-mini` modellek valamelyikét. Lásd a [Finomhangolható modellek listája](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) oldalát a jelenleg elérhető finomhangolható modellekért. A koncepciók és lépések ezekben az oktatóanyagokban továbbra is érvényesek.

Az alábbi források lépésről lépésre vezetnek végig egy valós példán, ahol egy kiválasztott modellt finomhangolunk egy kiválogatott adathalmazon. Ezeknek az oktatóanyagoknak az elvégzéséhez szükséged lesz egy adott szolgáltatónál regisztrált fiókra, valamint hozzáférésre a releváns modellekhez és adathalmazokhoz.

| Szolgáltató  | Oktatóanyag                                                                                                                                                                   | Leírás                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Hogyan finomhangoljuk a chat modelleket](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)        | Tanulj meg finomhangolni egy `gpt-35-turbo` modellt egy adott területre („recept asszisztens”) azzal, hogy elkészíted a tanító adatokat, lefuttatod a finomhangolási feladatot, és használod a finomhangolt modellt az inferenciához.                                                                                                                                                                                         |
| Azure OpenAI | [GPT 3.5 Turbo finomhangolási oktatóanyag](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Tanulj meg finomhangolni egy `gpt-35-turbo-0613` modellt **az Azure-on**, lépésről lépésre létrehozva és feltöltve a tanító adatokat, lefuttatva a finomhangolási munkát. Telepítsd és használd az új modelledet.                                                                                                                                                                                                                         |
| Hugging Face | [LLM-ek finomhangolása a Hugging Face segítségével](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                               | Ez a blogposzt végigvezet az _open LLM_ (pl.: `CodeLlama 7B`) finomhangolásán a [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) könyvtárral és a [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) használatával, nyílt [adathalmazokon](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) a Hugging Face-en.                    |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 🤗 AutoTrain | [LLM-ek finomhangolása az AutoTrain-nel](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                   | Az AutoTrain (vagy AutoTrain Advanced) egy Python könyvtár a Hugging Face fejlesztése, amely sokféle feladathoz teszi lehetővé a finomhangolást, beleértve az LLM finomhangolást is. Az AutoTrain kódmentes megoldás, és a finomhangolás végezhető a saját felhődben, a Hugging Face Spaces-en vagy helyben. Támogatja a webes GUI-t, parancssort és yaml konfigurációs fájlokat a képzéshez.                                                                 |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 🦥 Unsloth  | [LLM-ek finomhangolása az Unsloth segítségével](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Az Unsloth egy nyílt forráskódú keretrendszer, amely támogatja az LLM-ek finomhangolását és megerősítéses tanulást (RL). Az Unsloth egyszerűsíti a helyi tanítást, értékelést és telepítést előre elkészített [notebookokkal](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Támogat szövegfelolvasást (TTS), BERT-et és multimodális modelleket is. Kezdj a lépésről lépésre [Finomhangolási Útmutatójukban](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide). |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                               |
## Feladat

Válassz ki egyet a fenti oktatóanyagok közül és haladj végig rajta. _Előfordulhat, hogy ezekből oktatóanyagokból egy verziót reprodukálunk Jupyter Notebookokban ebben a tárházban csak referenciaként. Kérjük, a legfrissebb verziókért közvetlenül az eredeti forrásokat használd!_

## Szép munka! Folytasd a tanulást.

A lecke elvégzése után nézd meg a [Generatív MI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd a generatív MI tudásodat!

Gratulálunk!! Teljesítetted ennek a tanfolyamnak a v2-es sorozatából az utolsó leckét! Ne állj meg a tanulásban és az építésben. \*\*Nézd meg a [FORRÁSOK](RESOURCES.md?WT.mc_id=academic-105485-koreyst) oldalt további javaslatokért kizárólag erre a témára.

A v1-es sorozatunkat is frissítettük további feladatokkal és fogalmakkal. Szánj egy percet a tudásod felfrissítésére – és kérjük, [oszd meg kérdéseidet és visszajelzéseidet](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), hogy a közösség érdekében tovább fejlesszük ezeket a leckéket.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->