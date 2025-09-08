<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:22:49+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "hu"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.hu.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Bevezetés

A nyílt forráskódú LLM-ek világa izgalmas és folyamatosan fejlődik. Ez a lecke célja, hogy mélyreható betekintést nyújtson a nyílt forráskódú modellekbe. Ha arra keresel információt, hogy a zárt modellek hogyan viszonyulnak a nyílt forráskódú modellekhez, látogass el az ["Különböző LLM-ek felfedezése és összehasonlítása" leckéhez](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Ez a lecke a finomhangolás témáját is érinti, de részletesebb magyarázatot a ["LLM-ek finomhangolása" leckében](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst) találhatsz.

## Tanulási célok

- Megérteni a nyílt forráskódú modelleket
- Megérteni a nyílt forráskódú modellekkel való munka előnyeit
- Felfedezni a Hugging Face és az Azure AI Studio által kínált nyílt modelleket

## Mik azok a nyílt forráskódú modellek?

A nyílt forráskódú szoftverek kulcsszerepet játszottak a technológia fejlődésében számos területen. A Nyílt Forráskódú Kezdeményezés (OSI) [10 kritériumot határozott meg](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) ahhoz, hogy egy szoftver nyílt forráskódúnak minősüljön. A forráskódot nyíltan kell megosztani egy OSI által jóváhagyott licenc alatt.

Bár az LLM-ek fejlesztése hasonló elemeket tartalmaz, mint a szoftverfejlesztés, a folyamat nem teljesen ugyanaz. Ez sok vitát váltott ki a közösségben arról, hogy mit jelent a nyílt forráskód az LLM-ek kontextusában. Ahhoz, hogy egy modell megfeleljen a hagyományos nyílt forráskódú definíciónak, a következő információknak nyilvánosan elérhetőnek kell lenniük:

- Az adathalmazok, amelyeket a modell tanításához használtak.
- A teljes modell súlyai a tanítás részeként.
- Az értékelési kód.
- A finomhangolási kód.
- A teljes modell súlyai és tanítási metrikái.

Jelenleg csak néhány modell felel meg ezeknek a kritériumoknak. Az [OLMo modell, amelyet az Allen Institute for Artificial Intelligence (AllenAI) hozott létre](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst), egy ilyen példa.

Ebben a leckében a modelleket "nyílt modelleknek" fogjuk nevezni, mivel a jelen írás idején lehet, hogy nem felelnek meg a fenti kritériumoknak.

## A nyílt modellek előnyei

**Magas szintű testreszabhatóság** - Mivel a nyílt modellek részletes tanítási információkkal kerülnek kiadásra, a kutatók és fejlesztők módosíthatják a modell belső működését. Ez lehetővé teszi rendkívül specializált modellek létrehozását, amelyek egy adott feladatra vagy tanulmányi területre vannak finomhangolva. Példák erre: kódgenerálás, matematikai műveletek és biológia.

**Költség** - A tokenenkénti költség ezeknek a modelleknek a használatára és telepítésére alacsonyabb, mint a zárt modellek esetében. Generatív AI alkalmazások építésekor érdemes megvizsgálni a teljesítmény és ár arányát az adott felhasználási esethez.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.hu.png)  
Forrás: Artificial Analysis

**Rugalmasság** - A nyílt modellekkel való munka lehetővé teszi a rugalmasságot különböző modellek használatában vagy kombinálásában. Példa erre a [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), ahol a felhasználó közvetlenül az interfészben választhatja ki a használt modellt:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.hu.png)

## Különböző nyílt modellek felfedezése

### Llama 2

A [LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), amelyet a Meta fejlesztett, egy nyílt modell, amelyet chat-alapú alkalmazásokhoz optimalizáltak. Ez a finomhangolási módszerének köszönhető, amely nagy mennyiségű párbeszédet és emberi visszajelzést tartalmazott. Ezzel a módszerrel a modell olyan eredményeket produkál, amelyek jobban megfelelnek az emberi elvárásoknak, így jobb felhasználói élményt nyújt.

A Llama finomhangolt verziói közé tartozik például a [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), amely a japán nyelvre specializálódott, és a [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), amely a bázismodell továbbfejlesztett verziója.

### Mistral

A [Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) egy nyílt modell, amely nagy teljesítményre és hatékonyságra összpontosít. A Mixture-of-Experts megközelítést alkalmazza, amely egy csoport specializált szakértői modellt kombinál egy rendszerbe, ahol a bemenettől függően bizonyos modellek kerülnek kiválasztásra. Ez hatékonyabbá teszi a számítást, mivel a modellek csak azokra a bemenetekre reagálnak, amelyekre specializálódtak.

A Mistral finomhangolt verziói közé tartozik például a [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), amely az orvosi területre összpontosít, és az [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), amely matematikai számításokat végez.

### Falcon

A [Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) egy LLM, amelyet a Technology Innovation Institute (**TII**) hozott létre. A Falcon-40B-t 40 milliárd paraméterrel tanították, ami kevesebb számítási költséggel jobb teljesítményt nyújt, mint a GPT-3. Ez a FlashAttention algoritmus és a multiquery attention használatának köszönhető, amely csökkenti a memóriaigényt az inferencia során. A csökkentett inferencia idővel a Falcon-40B alkalmas chat alkalmazásokhoz.

A Falcon finomhangolt verziói közé tartozik például az [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), amely egy nyílt modellekre épülő asszisztens, és a [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), amely jobb teljesítményt nyújt, mint az alapmodell.

## Hogyan válasszunk?

Nincs egyetlen helyes válasz a nyílt modell kiválasztására. Jó kiindulópont lehet az Azure AI Studio feladat szerinti szűrő funkciójának használata. Ez segít megérteni, hogy milyen típusú feladatokra tanították a modellt. A Hugging Face egy LLM Leaderboard-ot is fenntart, amely megmutatja a legjobban teljesítő modelleket bizonyos metrikák alapján.

Ha az LLM-ek különböző típusait szeretnéd összehasonlítani, az [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) egy másik remek forrás:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.hu.png)  
Forrás: Artificial Analysis

Ha egy adott felhasználási eseten dolgozol, érdemes olyan finomhangolt verziókat keresni, amelyek ugyanarra a területre összpontosítanak. Több nyílt modell kipróbálása, hogy lássuk, hogyan teljesítenek a te és a felhasználóid elvárásai szerint, szintén jó gyakorlat.

## Következő lépések

A nyílt modellek legjobb része, hogy gyorsan elkezdhetsz velük dolgozni. Nézd meg az [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) oldalt, amely egy speciális Hugging Face gyűjteményt tartalmaz az itt tárgyalt modellekkel.

## A tanulás itt nem ér véget, folytasd az utazást

A lecke befejezése után nézd meg a [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd a Generatív AI tudásodat!

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.