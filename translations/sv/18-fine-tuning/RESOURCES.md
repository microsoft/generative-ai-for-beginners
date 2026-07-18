# Resurser för Självstyrt Lärande

Lektionen byggdes med hjälp av kärnresurser från OpenAI och Microsoft Foundry som referenser för terminologi och handledningar. Här är en icke-uttömmande lista för dina egna självstyrda läranderesor. Varje länk nedan pekar på aktuellt, stödjat material.

## 1. Primära Resurser

| Titel/Länk | Beskrivning |
| :--- | :--- |
| [Fine-tuning med OpenAI-modeller](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Fine-tuning förbättrar few-shot learning genom att träna på många fler exempel än vad som ryms i prompten – sparar kostnader, förbättrar svarskvaliteten och möjliggör låg latens i förfrågningar. **Få en översikt över fine-tuning från OpenAI.** |
| [När man ska använda Microsoft Foundry fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Förstå **vad fine-tuning är (konceptet)**, varför du bör överväga det, vilken data som ska användas och hur man mäter kvalitet – plus när SFT, DPO eller RFT är rätt val. |
| [Anpassa en modell med fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Det kompletta **hur man gör (processen)** för fine-tuning i Microsoft Foundry med portalen, OpenAI / Foundry Python SDK eller REST API – täcker dataförberedelse, träning, checkpoints och distribution. |
| [Kontinuerlig fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Den iterativa processen att välja en redan fine-tunad modell som basmodell och **fine-tuna den ytterligare** på nya träningsdataset. |
| [Fine-tuning med verktygsanrop (funktion calls)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Fine-tuning av din modell **med verktygsanropsexempel** förbättrar output – mer exakta, konsekventa och liknande formaterade svar med färre prompt-tokens. |
| [Fine-tuning modeller: Microsoft Foundry vägledning](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Se upp **vilka modeller som kan fine-tunas**, vilka metoder de stödjer (SFT / DPO / RFT) och i vilka regioner de är tillgängliga. |
| [Översikt över fine-tuning: tekniker och modaliteter](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Jämför de tre träningsmetoderna (SFT, DPO, RFT) och de två modaliteterna (serverless vs. managed compute), med vägledning för val av basmodell och att komma igång. |
| **Handledning**: [Fine-tuna en modell i Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Skapa ett exempel-dataset, förbered för fine-tuning, kör ett fine-tuning-jobb på en aktuell stödjad modell som `gpt-4.1-mini`, och distribuera den fine-tunade modellen på Azure. |
| **Handledning**: [Fine-tuna modeller med serverlösa API-distributioner](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Anpassa öppna och partner-modeller (Phi, Llama, Mistral med flera) till dina dataset _med en lågnivå / UI-baserad arbetsflöde_ i Microsoft Foundry. |
| **Handledning**: [Fine-tuna Hugging Face-modeller på Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Fine-tuna en Hugging Face-modell med `transformers`-biblioteket på en enda GPU med Azure Databricks och Hugging Face Trainer. |
| **Utbildning**: [Fine-tuna en grundmodell med Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learnings modellekatalog erbjuder många open-source modeller som du kan fine-tuna. Del av [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Handledning**: [Azure OpenAI fine-tuning med Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Följ och analysera fine-tuning körningar på Azure med W&B. Utökar OpenAI:s fine-tuning-guide med Azure-specifika steg och experiment-spårning. |

## 2. Sekundära Resurser

Den här sektionen innehåller ytterligare resurser värda att utforska som vi inte hann täcka i lektionen. Använd dem för att bygga din egen expertis kring ämnet.

| Titel/Länk | Beskrivning |
| :--- | :--- |
| **OpenAI Cookbook**: [Dataförberedelse och analys för chat-modell fine-tuning](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Förbehandla och analysera ett chatt-dataset före fine-tuning: kontrollera formatfel, få grundläggande statistik, och uppskatta token-räkning (och kostnad). Tillsammans med [OpenAI fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Fine-tuning för Retrieval Augmented Generation (RAG) med Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Ett omfattande exempel på fine-tuning av OpenAI-modeller för RAG, som integrerar Qdrant och few-shot learning för att öka prestanda och minska fabriceringar. |
| **OpenAI Cookbook**: [Fine-tuning GPT med Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Använd W&B för att spåra modellträning och fine-tuning. Läs först deras [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) guide, och prova sedan Cookbook-övningen. |
| **Hugging Face-handledning**: [Hur man fine-tunar LLMs med Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Fine-tuna öppna LLMs med Hugging Face TRL, Transformers och dataset: definiera ett användningsfall, sätt upp en utvecklingsmiljö, förbered dataset, fine-tuna, utvärdera och distribuera. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Ett no-code / low-code bibliotek från Hugging Face för fine-tuning av många modelltyper. Körs i din egen molnmiljö, på Hugging Face Spaces eller lokalt via GUI, CLI eller YAML-konfiguration. |
| **Unsloth**: [Guide för fine-tuning av LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Ett open-source ramverk som förenklar lokal fine-tuning av LLM och förstärkningsinlärning, med färdiga [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->