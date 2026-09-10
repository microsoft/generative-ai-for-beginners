# Ресурси за самостално учење

Учење је засновано на основним ресурсима OpenAI и Microsoft Foundry као референцама за терминологију и туторијале. Ево непотпуног списка за ваше самостално учење. Сваки линк испод води ка актуелном и подржаном материјалу.

## 1. Примарни ресурси

| Назив/Линк | Опис |
| :--- | :--- |
| [Фајн-тијун са OpenAI моделима](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Фајн-тијун унапређује учење са неколико примера тако што се тренира на много више примера него што може да стане у промпт - штеди трошкове, побољшава квалитет одговора и омогућава брже захтеве. **Погледајте преглед фајн-тијуна од OpenAI.** |
| [Када користити Microsoft Foundry фајн-тијун](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Разумите **шта је фајн-тијун (појам)**, зашто би требало да га размотрите, које податке користити и како мерити квалитет - као и када је право решење SFT, DPO или RFT. |
| [Прилагодите модел фајн-тијуном](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Цео **поступак (процес)** фајн-тијуна у Microsoft Foundry користећи портал, OpenAI / Foundry Python SDK или REST API - укључујући припрему података, тренинг, чекпойнтове и распоређивање. |
| [Континуирани фајн-тијун](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Итеративни процес избора већ фајн-тијунираног модела као базног и **даљег фајн-тијуна** на новим скупова примера за тренинг. |
| [Фајн-тијун са позивом алата (функције)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Фајн-тијун вашег модела **са примерима позива алата** побољшава излаз - тачније, доследније, и одговоре сличног формата користећи мање токена у промпту. |
| [Фајн-тијун модели: Упутство Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Проверите **који модели се могу фајн-тијуновати**, које методе подржавају (SFT / DPO / RFT) и регије у којима су доступни. |
| [Преглед фајн-тијуна: технике и модалитети](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Упоредите три методе тренинга (SFT, DPO, RFT) и два модалитета (serverless против управљаног рачунара), са смерницама за избор базног модела и почетак. |
| **Туторијал**: [Фајн-тијун модела у Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Креирајте пример сета података, припремите за фајн-тијун, покрените посао фајн-тијуна на тренутном подржаном моделу као што је `gpt-4.1-mini` и распоредите фајн-тијунирани модел на Azure. |
| **Туторијал**: [Фајн-тијун модела са serverless API распоређивањем](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Прилагодите отворене и партнерске моделе (Phi, Llama, Mistral и више) вашим скупом података _користећи низак код, UI базиран ток рада_ у Microsoft Foundry. |
| **Туторијал**: [Фајн-тијун Hugging Face модела на Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Фајн-тијун Hugging Face модела са `transformers` библиотеком на једном GPU-у користећи Azure Databricks и Hugging Face Trainer. |
| **Тренирање**: [Фајн-тијун основног модела са Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Каталог Azure Machine Learning нуди многе open-source моделе које можете да фајн-тијунujete. Део је [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Туторијал**: [Azure OpenAI фајн-тијун са Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Пратите и анализирајте фајн-тијун покрете на Azure помоћу W&B. Допуњује OpenAI фајн-тијун вођство са Azure специфичним корацима и праћењем експеримената. |

## 2. Секундарни ресурси

Овај одељак садржи додатне ресурсе вредне истраживања које нисмо имали времена да обрадимо у лекцији. Користите их да изградите своје знање о овој теми.

| Назив/Линк | Опис |
| :--- | :--- |
| **OpenAI Cookbook**: [Припрема и анализа података за фајн-тијун чет модела](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Препроцесирајте и анализирајте скуп података за чет пре фајн-тијуна: проверите грешке формата, добијте основну статистику и процените број токена (и трошкове). Упарено са [OpenAI водичем за фајн-тијун](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Фајн-тијун за Retrieval Augmented Generation (RAG) са Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Свеобухватан пример фајн-тијуна OpenAI модела за RAG, интегришући Qdrant и учење са неколико примера за побољшање перформанси и смањење измишљања. |
| **OpenAI Cookbook**: [Фајн-тијун GPT са Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Користите W&B за праћење тренинга и фајн-тијуна модела. Прво прочитајте њихов [OpenAI фајн-тијун водич](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst), затим испробајте задатак из Cookbook. |
| **Хагинг Фејс Туторијал**: [Како фајн-тијуновати LLM-ове са Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Фајн-тијун отворене LLM-ове користећи Hugging Face TRL, Transformers и скупове података: дефиниши употребу, постави окружење, припреми скуп података, фајн-тијун, евалуирај и распореди. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Либрарy без кода / са мало кода од Hugging Face за фајн-тијун многих типова модела. Покрените га на свом облаку, Hugging Face Spaces или локално преко GUI, CLI или YAML конфигурације. |
| **Unsloth**: [Водич за фајн-тијун LLM-ова](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Open-source оквир који поједностављује локални фајн-тијун LLM-ова и појачано учење, са готовим за коришћење [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->