# Resursi Za Samostalno Učenje

Lekcija je izrađena koristeći osnovne resurse iz OpenAI i Microsoft Foundry kao reference za terminologiju i tutorijale. Ovdje je nekompletan popis za vaša vlastita samostalna putovanja učenja. Svaka poveznica ispod vodi na aktualni, podržani materijal.

## 1. Primarni Resursi

| Naslov/Poveznica | Opis |
| :--- | :--- |
| [Fino podešavanje s OpenAI modelima](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Fino podešavanje poboljšava učenje na nekoliko primjera treniranjem na mnogo više primjera nego što može stati u prompt - štedi troškove, poboljšava kvalitetu odgovora i omogućuje upite s manjim kašnjenjem. **Dobijte pregled fino podešavanja od OpenAI-ja.** |
| [Kada koristiti Microsoft Foundry fino podešavanje](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Razumijte **što je fino podešavanje (koncept)**, zašto biste ga trebali razmotriti, koje podatke koristiti i kako mjeriti kvalitetu - plus kada su SFT, DPO ili RFT pravi izbor. |
| [Prilagodite model fino podešavanjem](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Cjelokupni **kako (proces)** za fino podešavanje u Microsoft Foundry koristeći portal, OpenAI / Foundry Python SDK ili REST API - obuhvaća pripremu podataka, treniranje, kontrolne točke i implementaciju. |
| [Kontinuirano fino podešavanje](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Iterativni proces odabira već fino podešenog modela kao osnovnog modela i **dodatnog fino podešavanja** na novim skupovima primjera za treniranje. |
| [Fino podešavanje s pozivanjem funkcija (alati)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Fino podešavanje modela **primjerima pozivanja alata** poboljšava izlaz - preciznije, dosljednije, sličnog formata odgovore koristeći manje tokena u promptu. |
| [Fino podešavanje modela: Microsoft Foundry upute](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Provjerite **koji modeli se mogu fino podešavati**, koje metode podržavaju (SFT / DPO / RFT) i u kojim su regijama dostupni. |
| [Pregled fino podešavanja: tehnike i modaliteti](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Usporedite tri tehnike treniranja (SFT, DPO, RFT) i dva modaliteta (serverless vs. upravljani računarski resursi), uz smjernice o izboru osnovnog modela i početku rada. |
| **Tutorijal**: [Fino podesite model u Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Kreirajte uzorak dataseta, pripremite se za fino podešavanje, pokrenite posao fino podešavanja na trenutno podržanom modelu poput `gpt-4.1-mini` i implementirajte fino podešeni model na Azure. |
| **Tutorijal**: [Fino podesite modele s implementacijama serverless API-ja](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Prilagodite otvorene i partnerske modele (Phi, Llama, Mistral i više) vašim skupovima podataka _koristeći nizak kod, UI bazirani tijek rada_ u Microsoft Foundry. |
| **Tutorijal**: [Fino podesite Hugging Face modele na Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Fino podesite model Hugging Face s knjižnicom `transformers` na jednom GPU koristeći Azure Databricks i Hugging Face Trainer. |
| **Trening**: [Fino podesite osnovni model s Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning katalog modela nudi mnoge open-source modele koje možete fino podesiti. Dio je [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Tutorijal**: [Azure OpenAI fino podešavanje s Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Pratite i analizirajte izvedbe fino podešavanja na Azure uz W&B. Proširuje OpenAI vodič za fino podešavanje s koracima specifičnim za Azure i praćenje eksperimenata. |

## 2. Sekundarni Resursi

Ovaj odjeljak sadrži dodatne resurse vrijedne istraživanja koje nismo stigli obraditi u lekciji. Koristite ih za razvoj vlastite stručnosti o ovoj temi.

| Naslov/Poveznica | Opis |
| :--- | :--- |
| **OpenAI Cookbook**: [Priprema i analiza podataka za fino podešavanje chat modela](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Predobrada i analiza chat dataseta prije fino podešavanja: provjera formata, osnovne statistike i procjena broja tokena (i troškova). Usklađeno s [OpenAI vodičem za fino podešavanje](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Fino podešavanje za Retrieval Augmented Generation (RAG) s Qdrantom](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Sveobuhvatan primjer fino podešavanja OpenAI modela za RAG, integrirajući Qdrant i few-shot učenje za poboljšanje performansi i smanjenje izmišljotina. |
| **OpenAI Cookbook**: [Fino podešavanje GPT-a s Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Koristite W&B za praćenje treninga i fino podešavanje modela. Prvo pročitajte njihov [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) vodič, zatim isprobajte Cookbook vježbu. |
| **Hugging Face Tutorijal**: [Kako fino podesiti LLM-ove s Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Fino podesite otvorene LLM modele koristeći Hugging Face TRL, Transformers i datasets: definirajte slučaj korištenja, postavite razvojno okruženje, pripremite dataset, fino podesite, evaluirajte i implementirajte. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Knjižnica bez / s malo kodiranja od Hugging Face za fino podešavanje mnogih tipova modela. Pokrenite je u vlastitom oblaku, na Hugging Face Spaces ili lokalno putem GUI, CLI ili YAML konfiguracije. |
| **Unsloth**: [Vodič za fino podešavanje LLM-ova](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Open-source okvir koji pojednostavljuje lokalno fino podešavanje LLM-ova i učenje putem povratnih informacija, s gotovim [notebook-ima](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->