# Zdroje pro samostatné učení

Lekce byla vytvořena s použitím základních zdrojů OpenAI a Microsoft Foundry jako reference pro terminologii a návody. Zde je nevyčerpávající seznam pro vaše vlastní samostatné studijní cesty. Každý níže uvedený odkaz směřuje na aktuální, podporovaný materiál.

## 1. Primární zdroje

| Název/Odkaz | Popis |
| :--- | :--- |
| [Doladění modelů OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Doladění zlepšuje učení na několika příkladech tím, že trénuje na mnohem větším počtu příkladů než jich může být v promptu – šetří náklady, zlepšuje kvalitu odpovědí a umožňuje požadavky s nižší latencí. **Získejte přehled o doladění od OpenAI.** |
| [Kdy použít doladění v Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Pochopte **co doladění znamená (koncept)**, proč byste ho měli zvážit, jaká data použít a jak měřit kvalitu – a kdy je vhodné použít SFT, DPO nebo RFT. |
| [Přizpůsobení modelu doladěním](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Kompletní **návod (proces)** doladění v Microsoft Foundry pomocí portálu, OpenAI / Foundry Python SDK nebo REST API – zahrnuje přípravu dat, trénink, kontrolní body a nasazení. |
| [Kontinuální doladění](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Iterační proces výběru již doladěného modelu jako základního modelu a jeho **dalšího doladění** na nových sadách tréninkových příkladů. |
| [Doladění s voláním nástrojů (funkcí)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Doladění modelu **pomocí příkladů s voláním nástrojů** zlepšuje výstupy – přesnější, konzistentnější, podobně formátované odpovědi s využitím menšího počtu tokenů v promptu. |
| [Doladění modelů: doporučení Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Podívejte se, **které modely lze doladit**, jaké metody podporují (SFT / DPO / RFT) a ve kterých regionech jsou dostupné. |
| [Přehled doladění: techniky a modality](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Porovnejte tři tréninkové techniky (SFT, DPO, RFT) a dvě modality (serverless vs. spravovaný výpočet) s doporučením, jak vybrat základní model a jak začít. |
| **Návod**: [Doladění modelu v Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Vytvořte ukázkovou datovou sadu, připravte se na doladění, spusťte úlohu doladění na aktuálně podporovaném modelu jako `gpt-4.1-mini` a nasaďte doladěný model na Azure. |
| **Návod**: [Doladění modelů s nasazením API bez serveru](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Přizpůsobte otevřené a partnerské modely (Phi, Llama, Mistral a další) svým datasetům _pomocí nízko-kódového, UI založeného workflow_ v Microsoft Foundry. |
| **Návod**: [Doladění modelů Hugging Face na Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Doladění modelu Hugging Face s knihovnou `transformers` na jednom GPU pomocí Azure Databricks a Hugging Face Trainer. |
| **Školení**: [Doladění základního modelu s Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Katalog modelů Azure Machine Learning nabízí mnoho open-source modelů, které můžete doladit. Součást [výukové cesty Azure ML Generative AI](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Návod**: [Doladění Azure OpenAI s Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Sledujte a analyzujte běhy doladění na Azure pomocí W&B. Rozšiřuje průvodce doladěním OpenAI o kroky specifické pro Azure a sledování experimentů. |

## 2. Sekundární zdroje

Tato sekce zachycuje další zdroje, které stojí za prozkoumání, ale na které jsme v lekci neměli čas. Použijte je k vybudování vlastní odbornosti na toto téma.

| Název/Odkaz | Popis |
| :--- | :--- |
| **OpenAI Cookbook**: [Příprava a analýza dat pro doladění chat modelu](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Předzpracujte a analyzujte chatovou datovou sadu před doladěním: zkontrolujte formátovací chyby, získejte základní statistiky a odhadněte počet tokenů (a náklady). Spárujte s [průvodcem doladěním OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Doladění pro Retrieval Augmented Generation (RAG) s Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Komplexní příklad doladění modelů OpenAI pro RAG, integrující Qdrant a učení s několika příklady ke zvýšení výkonu a snížení nepřesností. |
| **OpenAI Cookbook**: [Doladění GPT s Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Použijte W&B ke sledování tréninku a doladění modelu. Nejprve si přečtěte jejich průvodce [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst), pak vyzkoušejte cvičení v Cookbooku. |
| **Hugging Face Tutorial**: [Jak doladit velké jazykové modely s Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Doladění otevřených LLM pomocí Hugging Face TRL, Transformers a datasetů: definujte případ použití, nastavte vývojové prostředí, připravte datovou sadu, doladěte, vyhodnoťte a nasazujte. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Knihovna bez kódu / s nízkým kódem od Hugging Face pro doladění mnoha typů modelů. Spusťte ji ve vlastním cloudu, na Hugging Face Spaces nebo lokálně přes GUI, CLI či YAML konfiguraci. |
| **Unsloth**: [Průvodce doladěním LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Open-source framework, který usnadňuje lokální doladění LLM a reinforcement learning, s připravenými [notebooky](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->