# Rasilimali Kwa Kujifunza Kujiongoza

Somo hili limejengwa kwa kutumia rasilimali kuu kutoka OpenAI na Microsoft Foundry kama marejeleo kwa istilahi na mafunzo. Hapa kuna orodha isiyo kamili kwa ajili ya safari zako za kujifunza mwenyewe. Kila kiungo hapa chini kinaelekeza kwenye nyenzo za sasa, zinazotegemeka.

## 1. Rasilimali za Msingi

| Kichwa/Kiungo | Maelezo |
| :--- | :--- |
| [Kufinyanga na Mifano ya OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Kufinyanga kuboresha ujifunzaji wa few-shot kwa kufundisha kwa mifano mingi zaidi kuliko inavyoweza kufunikwa katika amri - kuokoa gharama, kuboresha ubora wa majibu, na kuwezesha maombi yenye ucheleweshaji mdogo. **Pata muhtasari wa kufinyanga kutoka OpenAI.** |
| [Wakati wa kutumia kufinyanga Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Elewa **kufinyanga ni nini (dhana)**, kwa nini unapaswa kuzingatia, data gani ya kutumia, na jinsi ya kupima ubora - pamoja na wakati SFT, DPO, au RFT inafaa. |
| [Binafsisha mfano kwa kufinyanga](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Mwisho-mwisho **jinsi-ya (mchakato)** wa kufinyanga katika Microsoft Foundry kwa kutumia lango, OpenAI / Foundry Python SDK, au REST API - inajumuisha maandalizi ya data, mafunzo, sehemu za ukaguzi, na usambazaji. |
| [Kufinyanga kuendelea](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Mchakato wa kurudia wa kuchagua mfano ambao tayari umefinyangwa kama mfano wa msingi na **kuufinyanga zaidi** kwa seti mpya za mifano ya mafunzo. |
| [Kufinyanga na mwito wa zana (kazi)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Kufinyanga mfano wako **kwa kutumia mifano ya mwito wa zana** kuboresha matokeo - majibu sahihi zaidi, ya uthabiti, na yenye muundo unaofanana kwa kutumia tokeni chache za amri. |
| [Miongozo ya kufinyanga mifano: Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Angalia **mifano gani inaweza kufinyangwa**, mbinu wanazounga mkono (SFT / DPO / RFT), na maeneo wanayopatikana. |
| [Muhtasari wa kufinyanga: mbinu na aina](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Linganisha mbinu tatu za mafunzo (SFT, DPO, RFT) na aina mbili (serverless dhidi ya managed compute), na mwongozo wa kuchagua mfano wa msingi na kuanza. |
| **Mafunzo**: [Finyanga mfano katika Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Tengeneza seti ya sampuli, jiandae kwa kufinyanga,endesha kazi ya kufinyanga kwenye mfano unaoungwa mkono sasa kama `gpt-4.1-mini`, na sambaza mfano uliobinafsishwa kwenye Azure. |
| **Mafunzo**: [Finyanga mifano kwa usambazaji wa API zisizo na server](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Binafsisha mifano wazi na ya wapenzi (Phi, Llama, Mistral, na mengine) kwa seti zako za data _kutumia mtiririko wa kazi wa UI wa nambari fupi_ katika Microsoft Foundry. |
| **Mafunzo**: [Finyanga mifano ya Hugging Face kwenye Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Finyanga mfano wa Hugging Face kwa maktaba ya `transformers` kwenye GPU moja kwa kutumia Azure Databricks na Mwalimu wa Hugging Face. |
| **Mafunzo**: [Finyanga mfano wa msingi kwa Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Katalogi ya mfano wa Azure Machine Learning inatoa mifano mingi ya chanzo huru unayoweza kufinyanga. Sehemu ya [Njia ya Kujifunza AI ya Azure ML Generative](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Mafunzo**: [Kufinyanga Azure OpenAI na Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Fuata na chambua mizunguko ya kufinyanga kwenye Azure kwa W&B. Inaongeza mwongozo wa kufinyanga OpenAI kwa hatua maalum za Azure na ufuatiliaji wa majaribio. |

## 2. Rasilimali za Sekondari

Sehemu hii inakamata rasilimali za ziada zinazostahili kuchunguzwa ambazo hatukuwa na muda wa kuzifunika katika somo hili. Zitumie kujijengea utaalam kuhusu mada hii.

| Kichwa/Kiungo | Maelezo |
| :--- | :--- |
| **Jikokotoo la OpenAI**: [Maandalizi na uchambuzi wa data kwa kufinyanga mfano wa mazungumzo](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Tengeneza na chambua seti ya data ya mazungumzo kabla ya kufinyanga: angalia makosa ya muundo, pata takwimu za msingi, na kisiwa hesabu za tokeni (na gharama). Inalingana na [mwongozo wa kufinyanga OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **Jikokotoo la OpenAI**: [Kufinyanga kwa Uzalishaji wa Kurudisha Taarifa (RAG) na Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Mfano kamili wa kufinyanga mifano ya OpenAI kwa RAG, kuingiza Qdrant na ujifunzaji wa few-shot ili kuongeza utendaji na kupunguza udanganyifu. |
| **Jikokotoo la OpenAI**: [Kufinyanga GPT na Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Tumia W&B kufuatilia mafunzo ya mfano na kufinyanga. Soma mwongozo wao wa [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) kwanza, kisha jaribu mazoezi ya Jikokotoo. |
| **Mafunzo ya Hugging Face**: [Jinsi ya Kufinyanga LLMs na Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Finyanga LLMs wazi kwa kutumia Hugging Face TRL, Transformers, na seti za data: fafanua matumizi, andaa mazingira ya maendeleo, andaa seti ya data, finyanga, tathmini, na sambaza. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Maktaba isiyo na nambari / yenye nambari chache kutoka Hugging Face kwa kufinyanga aina nyingi za mifano. Endesha kwenye wingu lako, Hugging Face Spaces, au ndani ya eneo kupitia GUI, CLI, au usanidi wa YAML. |
| **Unsloth**: [Mwongozo wa Kufinyanga LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Mfumo wa chanzo huria unaorahisisha kufinyanga LLMs za ndani na ujifunzaji wa kurejesha, na [daftari](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) tayari kutumika. |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->