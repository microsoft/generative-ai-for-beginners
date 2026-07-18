# Ressurser for Selvstyrt Læring

Leksjonen ble bygget med kjerne ressurser fra OpenAI og Microsoft Foundry som referanser for terminologi og veiledninger. Her er en ikke-uttømmende liste for dine egen selvstyrte læringsreiser. Hver lenke under peker til aktuelt, støttet materiale.

## 1. Primære Ressurser

| Tittel/Lenke | Beskrivelse |
| :--- | :--- |
| [Finjustering med OpenAI-modeller](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Finjustering forbedrer på få-skudd-læring ved å trene på mange flere eksempler enn det som får plass i prompten – sparer kostnader, forbedrer responskvaliteten, og muliggjør lavere ventetid ved forespørsler. **Få en oversikt over finjustering fra OpenAI.** |
| [Når du skal bruke Microsoft Foundry finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Forstå **hva finjustering er (konsept)**, hvorfor du bør vurdere det, hvilken data som skal brukes, og hvordan måle kvalitet – pluss når SFT, DPO eller RFT er riktig valg. |
| [Tilpass en modell med finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Slutt-til-slutt **hvordan (prosess)** for finjustering i Microsoft Foundry ved bruk av portalen, OpenAI / Foundry Python SDK, eller REST API – dekker datapreparering, trening, sjekkpunkter, og utrulling. |
| [Kontinuerlig finjustering](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Den iterative prosessen med å velge en allerede finjustert modell som basis og **finjustere den videre** på nye sett med trenings-eksempler. |
| [Finjustering med verktøy (funksjons)anrop](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Finjustering av modellen din **med verktøy-anrops-eksempler** forbedrer output – mer nøyaktige, konsistente, likt formaterte svar ved bruk av færre prompt-tokener. |
| [Finjustering av modeller: Microsoft Foundry veiledning](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Se opp **hvilke modeller som kan finjusteres**, metodene de støtter (SFT / DPO / RFT), og regionene de er tilgjengelige i. |
| [Oversikt over finjustering: teknikker og modaliteter](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Sammenlign de tre treningsmetodene (SFT, DPO, RFT) og de to modalitetene (serverløs vs. administrert beregning), med veiledning for valg av basismodell og hvordan komme i gang. |
| **Veiledning**: [Finjuster en modell i Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Lag et eksempel datasett, forbered for finjustering, kjør en finjusteringsjobb på en aktuelt støttet modell som `gpt-4.1-mini`, og implementer den finjusterte modellen på Azure. |
| **Veiledning**: [Finjuster modeller med serverløse API-distribusjoner](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Skreddersy åpne og partner-modeller (Phi, Llama, Mistral, og flere) til dine datasett _ved hjelp av en lavkode, UI-basert arbeidsflyt_ i Microsoft Foundry. |
| **Veiledning**: [Finjuster Hugging Face-modeller på Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Finjuster en Hugging Face-modell med `transformers`-biblioteket på en enkelt GPU ved bruk av Azure Databricks og Hugging Face Trainer. |
| **Trening**: [Finjuster en grunnmodell med Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning modellkatalog tilbyr mange open source-modeller du kan finjustere. En del av [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Veiledning**: [Azure OpenAI finjustering med Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Spor og analyser finjusteringskjøringer på Azure med W&B. Utvider OpenAI finjusteringsveiledningen med Azure-spesifikke steg og eksperimentsporingsfunksjoner. |

## 2. Sekundære Ressurser

Denne seksjonen fanger opp tilleggressurser verdt å utforske som vi ikke hadde tid til å dekke i leksjonen. Bruk dem for å bygge din egen ekspertise rundt dette temaet.

| Tittel/Lenke | Beskrivelse |
| :--- | :--- |
| **OpenAI Cookbook**: [Datapreparering og analyse for chatmodell finjustering](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Forbehandle og analyser et chat-datasett før finjustering: sjekk for formatfeil, hent grunnleggende statistikk, og estimer antall token (og kostnad). Parer med [OpenAI finjusteringsguide](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Finjustering for Retrieval Augmented Generation (RAG) med Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Et omfattende eksempel på finjustering av OpenAI-modeller for RAG, integrerer Qdrant og få-skudd læring for å øke ytelse og redusere feilinformasjon. |
| **OpenAI Cookbook**: [Finjustering av GPT med Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Bruk W&B til å spore modelltrening og finjustering. Les deres [OpenAI finjustering](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst)-guide først, prøv deretter cookbook-øvelsen. |
| **Hugging Face Veiledning**: [Slik finjusterer du LLM-er med Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Finjuster åpne LLM-er ved hjelp av Hugging Face TRL, Transformers, og datasett: definér et brukstilfelle, sett opp et utviklingsmiljø, forbered datasett, finjuster, evaluer, og distribuer. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Et kodefritt / lavkode bibliotek fra Hugging Face for finjustering av mange modelltyper. Kjør det i egen sky, på Hugging Face Spaces, eller lokalt via GUI, CLI, eller YAML-konfigurasjon. |
| **Unsloth**: [Finjustering av LLM-er Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Et open source-rammeverk som effektiviserer lokal LLM finjustering og forsterkningslæring, med ferdiglagde [notatbøker](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->