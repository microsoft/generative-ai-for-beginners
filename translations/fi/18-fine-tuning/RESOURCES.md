# Itseopiskelun resurssit

Opetusmateriaali on rakennettu käyttäen OpenAI:n ja Microsoft Foundryn ydintoteutuksia terminologian ja opetusohjeiden lähteinä. Tässä on ei-tyhjentävä lista omia itseopiskelumatkailujasi varten. Jokainen alla oleva linkki osoittaa ajantasaiseen ja tuettuun materiaaliin.

## 1. Ensisijaiset resurssit

| Otsikko/Linkki | Kuvaus |
| :--- | :--- |
| [Fine-tuning with OpenAI Models](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Fine-tuning parantaa few-shot-oppimista kouluttamalla paljon enemmän esimerkeillä kuin mitä mahtuu promptiin – säästäen kustannuksia, parantaen vastausten laatua ja mahdollistaen pienemmän viiveen pyyntöihin. **Tutustu OpenAI:n fine-tuning-yhteenvetoon.** |
| [When to use Microsoft Foundry fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Ymmärrä **mikä fine-tuning on (käsite)**, miksi sitä kannattaa harkita, mitä dataa käyttää ja kuinka mitata laatua – sekä milloin SFT, DPO tai RFT ovat oikea valinta. |
| [Customize a model with fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Kattava **ohje (prosessi)** fine-tuningiin Microsoft Foundryssa portaalin, OpenAI / Foundry Python SDK:n tai REST API:n avulla – kattaa datan valmistelun, koulutuksen, tarkistuspisteet ja käyttöönoton. |
| [Continuous fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Iteratiivinen prosessi, jossa jo valmiiksi hienosäädettyä mallia käytetään perusmallina ja **sitä hienosäädetään edelleen** uusilla koulutusesimerkeillä. |
| [Fine-tuning with tool (function) calling](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Mallin hienosäätö **työkalukutsuesimerkkien avulla** parantaa tuloksia – tarkempia, yhdenmukaisempia ja samankaltaiseen muotoon jäsenneltyjä vastauksia käyttäen vähemmän prompt-tokeneita. |
| [Fine-tuning models: Microsoft Foundry guidance](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Tutustu **mitkä mallit voi hienosäätää**, mitä menetelmiä ne tukevat (SFT / DPO / RFT) ja missä alueilla ne ovat saatavilla. |
| [Fine-tuning overview: techniques and modalities](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Vertaa kolmea koulutustekniikkaa (SFT, DPO, RFT) ja kahta käyttömuotoa (serverless vs. hallittu laskenta), ohjeet perusmallin valintaan ja aloitukseen. |
| **Tutorial**: [Fine-tune a model in Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Luo esimerkkiaineisto, valmistaudu hienosäätöön, käynnistä hienosäätötyö jollain tuetusta mallista kuten `gpt-4.1-mini` ja ota hienosäädetty malli käyttöön Azuren kautta. |
| **Tutorial**: [Fine-tune models with serverless API deployments](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Räätälöi avoimia ja partnerimalleja (Phi, Llama, Mistral ja muita) omiin aineistoihisi _käyttäen vähäkoodista, käyttöliittymäpohjaista työnkulku_ Microsoft Foundryssa. |
| **Tutorial**: [Fine-tune Hugging Face models on Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Hienosäädä Hugging Face -mallia `transformers`-kirjastolla yhdellä GPU:lla Azure Databricksilla ja Hugging Face Trainerilla. |
| **Training**: [Fine-tune a foundation model with Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learningin malliluettelosta löytyy monia avoimen lähdekoodin malleja jotka voit hienosäätää. Osa [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) -oppipolkua. |
| **Tutorial**: [Azure OpenAI fine-tuning with Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Seuraa ja analysoi hienosäätöajoja Azurella W&B:n avulla. Laajentaa OpenAI:n hienosäätöopasta Azure-spesifeillä vaiheilla ja kokeilujen seurannalla. |

## 2. Toissijaiset resurssit

Tämä osio sisältää lisäresursseja, joita kannattaa tutkia, mutta joita ei ehditty käsitellä oppitunnilla. Käytä niitä oman asiantuntemuksesi rakentamiseen tämän aiheen ympärillä.

| Otsikko/Linkki | Kuvaus |
| :--- | :--- |
| **OpenAI Cookbook**: [Datan valmistelu ja analyysi chat-mallin hienosäätöön](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Esikäsittele ja analysoi chat-aineisto ennen hienosäätöä: tarkista formaattivirheet, saa perusstatistiikkaa ja arvioi token-määrät (ja kustannukset). Yhdistä [OpenAI:n fine-tuning -oppaaseen](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Hienosäätö Retrieval Augmented Generationille (RAG) Qdrantin kanssa](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Kattava esimerkki OpenAI-mallien hienosäädöstä RAG:lle, Qdrantin ja few-shot-oppimisen integroiminen suorituskyvyn parantamiseksi ja keksintöjen vähentämiseksi. |
| **OpenAI Cookbook**: [GPT:n hienosäätö Weights & Biasesillä](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Käytä W&B:tä mallin koulutusten ja hienosäätöjen seurantaan. Lue heidän [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) opas ensin, kokeile sitten Cookbookin harjoitusta. |
| **Hugging Face Tutorial**: [Kuinka hienosäätää LLM:ää Hugging Face TRL:n avulla](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Hienosäädä avoimia LLM:iä käyttäen Hugging Face TRL:ää, Transformers-kirjastoa ja datasettejä: määrittele käyttötapaus, ota kehitysympäristö käyttöön, valmista aineisto, hienosäädä, arvioi ja ota käyttöön. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Facen no-code / low-code -kirjasto monien mallityyppien hienosäätöön. Aja se omassa pilvessäsi, Hugging Face Spacesissa tai paikallisesti GUI:n, CLI:n tai YAML-konfiguraation kautta. |
| **Unsloth**: [LLM:ien hienosäätöopas](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Avoimen lähdekoodin kehys, joka virtaviivaistaa paikallista LLM-hienosäätöä ja vahvistusoppimista, sisältäen valmiita [muistikirjoja](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->