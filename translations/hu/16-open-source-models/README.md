<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85b754d4dc980f270f264d17116d9a5f",
  "translation_date": "2025-12-19T16:36:46+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "hu"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.hu.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Bevezetés

A nyílt forráskódú LLM-ek világa izgalmas és folyamatosan fejlődik. Ez a lecke célja, hogy mélyreható betekintést nyújtson a nyílt forráskódú modellekbe. Ha arra keres információt, hogy a zárt forráskódú modellek hogyan viszonyulnak a nyílt forráskódú modellekhez, látogasson el a ["Különböző LLM-ek felfedezése és összehasonlítása" leckéhez](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Ez a lecke a finomhangolás témáját is érinti, de részletesebb magyarázat található a ["LLM-ek finomhangolása" leckében](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Tanulási célok

- Megérteni a nyílt forráskódú modelleket
- Megérteni a nyílt forráskódú modellekkel való munka előnyeit
- Felfedezni a Hugging Face-en és az Azure AI Studioban elérhető nyílt modelleket

## Mik azok a nyílt forráskódú modellek?

A nyílt forráskódú szoftverek kulcsszerepet játszottak a technológia fejlődésében különböző területeken. Az Open Source Initiative (OSI) meghatározott [10 kritériumot a szoftverek](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) nyílt forráskódú besorolásához. A forráskódot nyíltan kell megosztani egy OSI által jóváhagyott licenc alatt.

Bár az LLM-ek fejlesztése hasonló elemeket tartalmaz, mint a szoftverfejlesztés, a folyamat nem teljesen azonos. Ez sok vitát váltott ki a közösségben az LLM-ek kontextusában a nyílt forráskód definíciójáról. Ahhoz, hogy egy modell megfeleljen a hagyományos nyílt forráskódú definíciónak, a következő információknak nyilvánosan elérhetőnek kell lennie:

- Az adatkészletek, amelyeket a modell betanításához használtak.
- A teljes modell súlyai a betanítás részeként.
- Az értékelő kód.
- A finomhangoló kód.
- A teljes modell súlyai és a betanítási metrikák.

Jelenleg csak néhány modell felel meg ennek a kritériumnak. Az [Allen Institute for Artificial Intelligence (AllenAI) által készített OLMo modell](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) egy ilyen kategóriába tartozik.

Ebben a leckében a modelleket a továbbiakban "nyílt modelleknek" fogjuk nevezni, mivel íráskori állapotukban nem feltétlenül felelnek meg a fenti kritériumoknak.

## A nyílt modellek előnyei

**Nagyon testreszabható** – Mivel a nyílt modelleket részletes betanítási információkkal adják ki, a kutatók és fejlesztők módosíthatják a modell belső részeit. Ez lehetővé teszi nagyon specializált modellek létrehozását, amelyek egy adott feladatra vagy tanulmányi területre vannak finomhangolva. Példák erre a kódgenerálás, matematikai műveletek és biológia.

**Költség** – Ezeknek a modelleknek a tokenenkénti használati és telepítési költsége alacsonyabb, mint a zárt forráskódú modelleké. Generatív AI alkalmazások építésekor érdemes figyelembe venni a teljesítmény és ár arányát az adott felhasználási esetben.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.hu.png)
Forrás: Artificial Analysis

**Rugalmasság** – A nyílt modellekkel való munka lehetővé teszi, hogy rugalmas legyen a különböző modellek használatában vagy azok kombinálásában. Erre példa a [HuggingChat Asszisztensek](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), ahol a felhasználó közvetlenül a felhasználói felületen választhatja ki a használt modellt:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.hu.png)

## Különböző nyílt modellek felfedezése

### Llama 2

A [Llama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), amelyet a Meta fejlesztett, egy nyílt modell, amelyet csevegés alapú alkalmazásokhoz optimalizáltak. Ennek oka a finomhangolási módszere, amely nagy mennyiségű párbeszédet és emberi visszajelzést tartalmazott. Ezzel a módszerrel a modell olyan eredményeket produkál, amelyek jobban megfelelnek az emberi elvárásoknak, így jobb felhasználói élményt nyújt.

Néhány finomhangolt Llama verzió például a [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), amely a japán nyelvre specializálódott, és a [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), amely a bázismodell továbbfejlesztett változata.

### Mistral

A [Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) egy nyílt modell, amely erősen a magas teljesítményre és hatékonyságra fókuszál. A Mixture-of-Experts megközelítést alkalmazza, amely egy csoport specializált szakértői modellt egyesít egy rendszerbe, ahol a bemenet alapján bizonyos modelleket választanak ki használatra. Ez hatékonyabbá teszi a számítást, mivel a modellek csak azokra a bemenetekre reagálnak, amelyekben specializáltak.

Néhány finomhangolt Mistral verzió például a [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), amely az orvosi területre fókuszál, és az [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), amely matematikai számításokat végez.

### Falcon

A [Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) egy LLM, amelyet a Technology Innovation Institute (**TII**) hozott létre. A Falcon-40B-t 40 milliárd paraméteren képezték, és bizonyítottan jobb teljesítményt nyújt, mint a GPT-3 kevesebb számítási költséggel. Ennek oka a FlashAttention algoritmus és a multiquery attention használata, amely csökkenti a memóriaigényt az inferencia során. Ezzel a csökkentett inferenciaidővel a Falcon-40B alkalmas csevegőalkalmazásokhoz.

Néhány finomhangolt Falcon verzió például az [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), egy nyílt modelleken alapuló asszisztens, és a [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), amely jobb teljesítményt nyújt, mint az alapmodell.

## Hogyan válasszunk?

Nincs egyetlen helyes válasz a nyílt modell kiválasztására. Jó kiindulópont az Azure AI Studio feladat szerinti szűrő funkciójának használata. Ez segít megérteni, hogy milyen típusú feladatokra képezték a modellt. A Hugging Face egy LLM ranglistát is fenntart, amely megmutatja a legjobban teljesítő modelleket bizonyos metrikák alapján.

Ha különböző típusú LLM-eket szeretne összehasonlítani, az [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) egy másik nagyszerű forrás:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.hu.png)
Forrás: Artificial Analysis

Ha egy adott felhasználási esetre dolgozik, hatékony lehet olyan finomhangolt verziókat keresni, amelyek ugyanarra a területre fókuszálnak. Több nyílt modellel való kísérletezés, hogy lássa, hogyan teljesítenek az Ön és felhasználói elvárásai szerint, szintén jó gyakorlat.

## Következő lépések

A nyílt modellek legjobb része, hogy viszonylag gyorsan elkezdheti velük a munkát. Nézze meg az [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) gyűjteményt, amely tartalmaz egy speciális Hugging Face kollekciót ezekkel a modellekkel, amelyeket itt tárgyaltunk.

## A tanulás itt nem ér véget, folytassa az utazást

A lecke elvégzése után nézze meg a [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejlessze generatív AI ismereteit!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->