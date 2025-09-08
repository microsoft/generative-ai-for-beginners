<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:23:39+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "sk"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.sk.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Úvod

Svet open-source LLM je vzrušujúci a neustále sa vyvíja. Táto lekcia si kladie za cieľ poskytnúť podrobný pohľad na open-source modely. Ak hľadáte informácie o porovnaní proprietárnych modelov s open-source modelmi, prejdite na lekciu ["Preskúmanie a porovnanie rôznych LLM"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Táto lekcia sa tiež zaoberá témou doladenia, ale podrobnejšie vysvetlenie nájdete v lekcii ["Doladenie LLM"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Ciele učenia

- Získať pochopenie open-source modelov
- Porozumieť výhodám práce s open-source modelmi
- Preskúmať dostupné open-source modely na Hugging Face a Azure AI Studio

## Čo sú Open Source Modely?

Open-source softvér zohral kľúčovú úlohu v rozvoji technológií v rôznych oblastiach. Open Source Initiative (OSI) definovala [10 kritérií pre softvér](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst), aby mohol byť klasifikovaný ako open-source. Zdrojový kód musí byť otvorene zdieľaný pod licenciou schválenou OSI.

Aj keď vývoj LLM má podobné prvky ako vývoj softvéru, proces nie je úplne rovnaký. To vyvolalo veľa diskusií v komunite o definícii open-source v kontexte LLM. Aby model zodpovedal tradičnej definícii open-source, mali by byť verejne dostupné nasledujúce informácie:

- Dátové súbory použité na trénovanie modelu.
- Plné váhy modelu ako súčasť tréningu.
- Kód na vyhodnotenie.
- Kód na doladenie.
- Plné váhy modelu a metriky tréningu.

V súčasnosti existuje len niekoľko modelov, ktoré spĺňajú tieto kritériá. [Model OLMo vytvorený Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) je jedným z nich.

Pre túto lekciu budeme ďalej označovať modely ako "open modely", pretože v čase písania nemusia spĺňať vyššie uvedené kritériá.

## Výhody Open Modelov

**Vysoká prispôsobiteľnosť** - Keďže open modely sú vydané s podrobnými informáciami o tréningu, výskumníci a vývojári môžu upravovať vnútorné časti modelu. To umožňuje vytváranie vysoko špecializovaných modelov, ktoré sú doladené na konkrétnu úlohu alebo oblasť štúdia. Niektoré príklady zahŕňajú generovanie kódu, matematické operácie a biológiu.

**Náklady** - Náklady na token pri používaní a nasadzovaní týchto modelov sú nižšie ako pri proprietárnych modeloch. Pri budovaní aplikácií generatívnej AI by sa mala vykonať analýza výkonu vs. cena pri práci s týmito modelmi na vašom prípade použitia.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.sk.png)  
Zdroj: Artificial Analysis

**Flexibilita** - Práca s open modelmi umožňuje flexibilitu pri používaní rôznych modelov alebo ich kombinovaní. Príkladom je [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), kde si používateľ môže priamo v rozhraní vybrať model, ktorý sa používa:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.sk.png)

## Preskúmanie rôznych Open Modelov

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), vyvinutý spoločnosťou Meta, je open model optimalizovaný pre aplikácie založené na chate. Je to vďaka metóde doladenia, ktorá zahŕňala veľké množstvo dialógov a ľudskej spätnej väzby. Táto metóda umožňuje modelu produkovať výsledky, ktoré sú viac v súlade s očakávaniami ľudí, čo poskytuje lepší používateľský zážitok.

Niektoré príklady doladených verzií Llama zahŕňajú [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), ktorý sa špecializuje na japončinu, a [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), ktorý je vylepšenou verziou základného modelu.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) je open model so silným zameraním na vysoký výkon a efektivitu. Používa prístup Mixture-of-Experts, ktorý kombinuje skupinu špecializovaných expertov do jedného systému, kde sa v závislosti od vstupu vyberajú určité modely na použitie. To robí výpočty efektívnejšími, pretože modely sa zaoberajú iba vstupmi, na ktoré sú špecializované.

Niektoré príklady doladených verzií Mistral zahŕňajú [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), ktorý sa zameriava na medicínsku oblasť, a [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), ktorý vykonáva matematické výpočty.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) je LLM vytvorený Technology Innovation Institute (**TII**). Falcon-40B bol trénovaný na 40 miliardách parametrov, čo sa ukázalo ako lepšie ako GPT-3 s menším výpočtovým rozpočtom. Je to vďaka použitiu algoritmu FlashAttention a multiquery attention, ktoré umožňujú znížiť požiadavky na pamäť počas inferencie. S týmto zníženým časom inferencie je Falcon-40B vhodný pre aplikácie založené na chate.

Niektoré príklady doladených verzií Falcon zahŕňajú [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asistenta postaveného na open modeloch, a [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), ktorý poskytuje vyšší výkon ako základný model.

## Ako si vybrať

Neexistuje jednoznačná odpoveď na výber open modelu. Dobré miesto na začiatok je použitie funkcie filtrovania podľa úlohy v Azure AI Studio. To vám pomôže pochopiť, na aké typy úloh bol model trénovaný. Hugging Face tiež udržiava LLM Leaderboard, ktorý vám ukáže najlepšie výkonné modely na základe určitých metrík.

Pri porovnávaní LLM naprieč rôznymi typmi je ďalším skvelým zdrojom [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst):

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.sk.png)  
Zdroj: Artificial Analysis

Ak pracujete na konkrétnom prípade použitia, hľadanie doladených verzií zameraných na rovnakú oblasť môže byť efektívne. Experimentovanie s viacerými open modelmi, aby ste videli, ako sa správajú podľa vašich očakávaní a očakávaní vašich používateľov, je ďalšou dobrou praxou.

## Ďalšie kroky

Najlepšia časť o open modeloch je, že s nimi môžete začať pracovať pomerne rýchlo. Pozrite si [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), ktorý obsahuje špecifickú kolekciu Hugging Face s modelmi, o ktorých sme tu diskutovali.

## Učenie nekončí, pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v rozširovaní svojich znalostí o generatívnej AI!

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.