# Ressursid iseseisvaks õppimiseks

Õppetund on koostatud kasutades peamisi allikaid OpenAI ja Microsoft Foundry-st terminoloogia ja juhendite jaoks. Siin on mittetäielik nimekiri teie enda iseseisvate õppeteekondade jaoks. Iga alljärgnev link viitab ajakohasele ja toetatud materjalile.

## 1. Peamised ressursid

| Pealkiri/Link | Kirjeldus |
| :--- | :--- |
| [Fine-tuneiimimine OpenAI mudelitega](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Fine-tuneiimimine täiustab väheste näidete õppimist, treenides palju rohkem näidiseid kui mahub viitesse – säästes kulusid, parandades vastuste kvaliteeti ja võimaldades madalama latentsusajaga päringuid. **Saage ülevaade OpenAI fine-tuneiimisest.** |
| [Millal kasutada Microsoft Foundry fine-tuneimist](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Mõistke **mis on fine-tuneimine (kontseptsioon)**, miks peaksite seda kaaluma, milliseid andmeid kasutada ja kuidas kvaliteeti mõõta – pluss millal sobib SFT, DPO või RFT. |
| [Mudeli kohandamine fine-tuneimisega](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Lõpp-lõpuni **kuidas teha (protsess)** Microsoft Foundry's fine-tuneimist kasutades portaali, OpenAI / Foundry Python SDK või REST API – hõlmates andmete ettevalmistust, koolitust, kontrollpunkte ja juurutamist. |
| [Jätkuv fine-tuneimine](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Iteratiivne protsess, kus põhimalmuna valitakse juba fine-tuneitud mudel ja **fine-tuneitakse seda edasi** uute koolitusnäidiste komplektide peal. |
| [Fine-tuneimine tööriista (funktsiooni) kutsumisega](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Mudeli fine-tuneimine **tööriista kutsete näidetega** parandab väljundit – täpsemad, järjepidevamad, sarnase vorminguga vastused, kasutades vähem viite tokeneid. |
| [Fine-tuneimise mudelid: Microsoft Foundry juhised](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Vaadake, **milliseid mudeleid saab fine-tuneerida**, milliseid meetodeid nad toetavad (SFT / DPO / RFT) ja millistes regioonides need kättesaadavad on. |
| [Fine-tuneimise ülevaade: tehnikad ja modaliteedid](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Võrrelge kolme koolitustehnikat (SFT, DPO, RFT) ja kahte modaliteeti (serverivaba vs haldatud arvutus), koos juhistega, kuidas valida baas-mudel ja alustada. |
| **Juhend**: [Fine-tuneeri mudel Microsoft Foundry's](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Loo näidisandmestik, valmista ette fine-tuneimiseks, käivita fine-tuneimise töö aktuaalselt toetatavale mudelile nagu `gpt-4.1-mini` ja juuruta fine-tuneeritud mudel Azure'is. |
| **Juhend**: [Fine-tuneeri mudeleid serverivabade API juurutustega](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Kohanda avatud ja partnerite mudeleid (Phi, Llama, Mistral jm) oma andmestike jaoks _kasutades madala koodiga, kasutajaliidese-põhist töövoogu_ Microsoft Foundry's. |
| **Juhend**: [Fine-tuneeri Hugging Face mudeleid Azure Databricks'is](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Fine-tuneeri Hugging Face mudelit `transformers` teegiga ühe GPU peal, kasutades Azure Databricks'i ja Hugging Face Trainerit. |
| **Koolitus**: [Fine-tuneeri põhjalik mudel Azure Machine Learninguga](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning mudelikataloog pakub palju avatud lähtekoodiga mudeleid, mida saate fine-tuneerida. Osa [Azure ML Generative AI õpitee](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Juhend**: [Azure OpenAI fine-tuneimine Weights & Biases abil](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Jälgi ja analüüsi fine-tuneimise käike Azure'is W&B abil. Laiendab OpenAI fine-tuneimise juhendit Azure-spetsiifiliste sammude ja eksperimendi jälgimisega. |

## 2. Teisene ressursid

See sektsioon sisaldab täiendavaid ressursse, mida tasub uurida, kuid mida meil ei olnud aega õppetunnis käsitleda. Kasutage neid, et ise selle teema kohta teadmisi koguda.

| Pealkiri/Link | Kirjeldus |
| :--- | :--- |
| **OpenAI Cookbook**: [Andmete ettevalmistus ja analüüs vestlusmudeli fine-tuneimiseks](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Eeltöödelge ja analüüsige vestlusandmestikku enne fine-tuneimist: kontrollige formaadivigu, hankige põhistatistikat ja hinnake tokenite arvu (ja kulusid). Siduge [OpenAI fine-tuneimise juhendiga](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Fine-tuneimine Retrieval Augmented Generation (RAG) jaoks Qdrantiga](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Ulatuslik näide OpenAI mudelite fine-tuneimisest RAG jaoks, ühendades Qdrant ja väheste näidete õppimise, et parandada jõudlust ja vähendada väljamõeldisi. |
| **OpenAI Cookbook**: [Fine-tuneimine GPT Weights & Biases abil](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Kasutage W&B mudeli koolituse ja fine-tuneimise jälgimiseks. Loe esmalt nende [OpenAI fine-tuneimise](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) juhendit, seejärel proovige Cookbooki harjutust. |
| **Hugging Face juhend**: [Kuidas fine-tuneerida LLM-e Hugging Face TRL abil](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Fine-tuneeri avatud LLM-e kasutades Hugging Face TRL, Transformers ja andmestikke: määratle kasutusjuht, seadista arenduskeskkond, valmista andmestik, fine-tuneeri, hinda ja juuruta. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Madala koodi / koodita teek Hugging Face'ilt erinevat tüüpi mudelite fine-tuneimiseks. Käivitage see oma pilves, Hugging Face Spaces'is või lokaalselt GUI, CLI või YAML konfiguratsiooni kaudu. |
| **Unsloth**: [LLMe fine-tuneimise juhend](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Avatud lähtekoodiga raamistik, mis lihtsustab lokaalset LLM fine-tuneimist ja tugevdamisõpet, koos kasutusvalmis [märkmikega](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->