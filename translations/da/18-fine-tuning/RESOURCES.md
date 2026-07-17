# Ressourcer til Selvstyret Læring

Lektionen blev opbygget med kerneressourcer fra OpenAI og Microsoft Foundry som referencer for terminologi og vejledninger. Her er en ikke-udtømmende liste til dine egne selvstyrede læringsrejser. Hvert link nedenfor peger på aktuelt, supporteret materiale.

## 1. Primære Ressourcer

| Titel/Link | Beskrivelse |
| :--- | :--- |
| [Finjustering med OpenAI-modeller](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Finjustering forbedrer få-skud læring ved at træne på mange flere eksempler, end hvad der kan være i prompten - sparer omkostninger, forbedrer responskvalitet og muliggør lavere ventetid på forespørgsler. **Få et overblik over finjustering fra OpenAI.** |
| [Hvornår man skal bruge Microsoft Foundry finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Forstå **hvad finjustering er (konceptet)**, hvorfor du bør overveje det, hvilke data der skal bruges, og hvordan man måler kvalitet - plus hvornår SFT, DPO eller RFT er den rigtige løsning. |
| [Tilpas en model med finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Den end-to-end **hvordan-man-gør (proces)** for finjustering i Microsoft Foundry ved brug af portalen, OpenAI / Foundry Python SDK eller REST API - dækker dataklargøring, træning, checkpoints og udrulning. |
| [Kontinuerlig finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Den iterative proces med at vælge en allerede finjusteret model som basismodel og **finjustere den yderligere** på nye sæt træningseksempler. |
| [Finjustering med værktøj (funktions) kald](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Finjustering af din model **med eksempler på værktøjskald** forbedrer output - mere præcise, konsistente, ensartet formaterede svar med brug af færre prompt-tokens. |
| [Finjustering af modeller: Microsoft Foundry vejledning](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Se op **hvilke modeller der kan finjusteres**, hvilke metoder de understøtter (SFT / DPO / RFT), og i hvilke regioner de er tilgængelige. |
| [Finjustering oversigt: teknikker og modaliteter](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Sammenlign de tre træningsteknikker (SFT, DPO, RFT) og de to modaliteter (serverløs vs. administreret compute), med vejledning i valg af basismodel og komme i gang. |
| **Vejledning**: [Finjuster en model i Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Opret et prøve-datasæt, forbered til finjustering, kør et finjusteringsjob på en aktuelt supporteret model såsom `gpt-4.1-mini`, og udrul den finjusterede model på Azure. |
| **Vejledning**: [Finjuster modeller med serverløse API-udrulninger](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Tilpas åbne og partnermodeller (Phi, Llama, Mistral og flere) til dine datasæt _ved hjælp af en low-code, UI-baseret arbejdsgang_ i Microsoft Foundry. |
| **Vejledning**: [Finjuster Hugging Face modeller på Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Finjuster en Hugging Face-model med `transformers`-biblioteket på et enkelt GPU ved hjælp af Azure Databricks og Hugging Face Trainer. |
| **Træning**: [Finjuster en foundationsmodel med Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning modelkataloget tilbyder mange open source-modeller, du kan finjustere. En del af [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Vejledning**: [Azure OpenAI finjustering med Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Følg og analyser finjusteringskørsler på Azure med W&B. Udvider OpenAI's finjusteringsguide med Azure-specifikke trin og eksperimenttracking. |

## 2. Sekundære Ressourcer

Dette afsnit samler yderligere ressourcer, som er værd at udforske, men som vi ikke nåede at dække i lektionen. Brug dem til at opbygge din egen ekspertise omkring dette emne.

| Titel/Link | Beskrivelse |
| :--- | :--- |
| **OpenAI Cookbook**: [Dataklargøring og analyse til chatmodel finjustering](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Forbehandl og analysér et chatdatasæt før finjustering: tjek for formatfejl, få grundlæggende statistikker og estimer antal tokens (og omkostninger). Passer med [OpenAI finjusteringsguide](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Finjustering til Retrieval Augmented Generation (RAG) med Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Et omfattende eksempel på finjustering af OpenAI-modeller til RAG, integrerer Qdrant og få-skuds læring for at øge ydeevne og reducere fabrikerede svar. |
| **OpenAI Cookbook**: [Finjustering af GPT med Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Brug W&B til at følge modeltræning og finjustering. Læs først deres [OpenAI Finjustering](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) guide, og prøv så Cookbook øvelsen. |
| **Hugging Face Vejledning**: [Hvordan man finjusterer LLM'er med Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Finjuster åbne LLM'er ved brug af Hugging Face TRL, Transformers og datasæt: definér et brugsscenarie, sæt et udviklingsmiljø op, forbered et datasæt, finjuster, evaluer og udrul. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Et no-code / low-code bibliotek fra Hugging Face til finjustering af mange modeltyper. Kør det i din egen sky, på Hugging Face Spaces eller lokalt via GUI, CLI eller YAML-konfiguration. |
| **Unsloth**: [Guide til finjustering af LLM'er](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Et open source-rammeværk, der forenkler lokal finjustering af LLM'er og forstærkningslæring, med færdiglavede [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->