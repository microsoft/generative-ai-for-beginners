# Zdroje pre samostatné učenie

Lekcia bola vytvorená s použitím základných zdrojov od OpenAI a Microsoft Foundry ako referencií pre terminológiu a návody. Tu je neúplný zoznam pre vaše vlastné samostatné učenie. Každý odkaz nižšie vedie na aktuálny, podporovaný materiál.

## 1. Primárne zdroje

| Názov/Odkaz | Popis |
| :--- | :--- |
| [Doladenie modelov OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Doladenie zlepšuje učenie na pár príkladoch tým, že sa trénuje na oveľa väčšom množstve príkladov, než sa zmestí do promptu - šetrenie nákladov, zlepšenie kvality odpovedí a umožnenie požiadaviek s nižšou latenciou. **Prehľad doladenia od OpenAI.** |
| [Kedy použiť doladenie v Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Pochopte **čo je doladenie (koncept)**, prečo by ste ho mali zvážiť, aké údaje použiť a ako merať kvalitu - plus kedy je vhodné SFT, DPO alebo RFT. |
| [Prispôsobenie modelu pomocou doladenia](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Kompletný **návod (proces)** pre doladenie v Microsoft Foundry pomocou portálu, OpenAI / Foundry Python SDK alebo REST API - zahŕňa prípravu dát, trénovanie, kontrolné body a nasadenie. |
| [Kontinuálne doladenie](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Iteračný proces výberu už doladeného modelu ako základného a **jeho ďalšie doladenie** na nových sadách výcvikových príkladov. |
| [Doladenie s volaním nástrojov (funkcií)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Doladenie modelu **s príkladmi volania nástrojov** zlepšuje výstup - presnejšie, konzistentnejšie, podobne formátované odpovede s použitím menej tokenov v prompte. |
| [Doladenie modelov: usmernenia Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Zistite, **ktoré modely je možné doladiť**, metódy, ktoré podporujú (SFT / DPO / RFT) a regióny, kde sú dostupné. |
| [Prehľad doladenia: techniky a modality](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Porovnajte tri trénovacie techniky (SFT, DPO, RFT) a dve modality (serverless vs. riadený výpočet) s usmerneniami pre výber základného modelu a štart. |
| **Návod**: [Doladte model v Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Vytvorte ukážkovú dátovú sadu, pripravte sa na doladenie, spustite doladenie na aktuálne podporovanom modeli ako `gpt-4.1-mini` a nasadte doladený model na Azure. |
| **Návod**: [Doladenie modelov s nasadeniami serverless API](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Prispôsobte open a partnerské modely (Phi, Llama, Mistral a ďalšie) vašim dátovým sadám _použitím nízkokódového UI workflow_ v Microsoft Foundry. |
| **Návod**: [Doladenie Hugging Face modelov na Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Doladte Hugging Face model s knižnicou `transformers` na jedinom GPU pomocou Azure Databricks a Hugging Face Trainer. |
| **Školenie**: [Doladenie základného modelu s Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Katalóg modelov Azure Machine Learning ponúka mnoho open-source modelov, ktoré môžete doladiť. Súčasť [učebnej cesty Azure ML Generative AI](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Návod**: [Doladenie Azure OpenAI s Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Sledujte a analyzujte behy doladenia na Azure s W&B. Rozširuje OpenAI príručku doladenia o kroky a sledovanie experimentov špecifické pre Azure. |

## 2. Sekundárne zdroje

Táto sekcia obsahuje ďalšie zdroje, ktoré stojí za to preskúmať, ale nemali sme čas ich pokryť v lekcii. Použite ich na budovanie vlastnej odbornosti o tejto téme.

| Názov/Odkaz | Popis |
| :--- | :--- |
| **OpenAI Cookbook**: [Príprava a analýza dát pre doladenie chat modelu](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Predspracovanie a analýza chat datasetu pred doladením: kontrola formátovacích chýb, základné štatistiky a odhad počtu tokenov (a nákladov). Párované s [OpenAI príručkou doladenia](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Doladenie pre Retrieval Augmented Generation (RAG) s Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Komplexný príklad doladenia modelov OpenAI pre RAG, integrujúce Qdrant a učenie na pár príkladoch pre zvýšenie výkonu a zníženie vymýšľania. |
| **OpenAI Cookbook**: [Doladenie GPT s Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Použite W&B na sledovanie trénovania a doladenia modelu. Najprv prečítajte ich [OpenAI doladenie](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) príručku a potom vyskúšajte cvičenie z Cookbooku. |
| **Hugging Face návod**: [Ako doladiť LLM s Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Doladte open LLM pomocou Hugging Face TRL, Transformers a datasetov: definujte prípad použitia, pripravte vývojové prostredie, dataset, doladte, vyhodnoťte a nasadte. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Bez-kódová / nízkokódová knižnica od Hugging Face pre doladenie mnohých typov modelov. Spustite ju vo svojom cloude, na Hugging Face Spaces alebo lokálne cez GUI, CLI alebo YAML konfiguráciu. |
| **Unsloth**: [Sprievodca doladením LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Open-source rámec, ktorý zjednodušuje lokálne doladenie LLM a posilňovacie učenie, s pripravenými [notebookmi](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->