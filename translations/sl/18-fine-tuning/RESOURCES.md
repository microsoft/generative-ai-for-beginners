# Viri za samostojno učenje

Lekcija je bila zasnovana z uporabo osnovnih virov OpenAI in Microsoft Foundry kot referenc za terminologijo in vadnice. Tukaj je neizčrpen seznam za vaše lastne poti samostojnega učenja. Vsaka spodnja povezava vodi do trenutno podprtega gradiva.

## 1. Primarni viri

| Naslov/Povezava | Opis |
| :--- | :--- |
| [Prilagajanje modelov z OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Prilagajanje izboljšuje učenje na majhnem številu primerov z usposabljanjem na veliko več primerih, kot jih lahko sprejme poziv - kar znižuje stroške, izboljšuje kakovost odgovorov in omogoča zahtevke z nižjo zakasnitvijo. **Pridobite pregled prilagajanja v OpenAI.** |
| [Kdaj uporabiti Microsoft Foundry prilagajanje](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Razumite **kaj je prilagajanje (koncept)**, zakaj ga je vredno upoštevati, katere podatke uporabiti in kako meriti kakovost - plus kdaj izbrati SFT, DPO ali RFT. |
| [Prilagodite model s prilagajanjem](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Celoten **postopek (how-to)** za prilagajanje v Microsoft Foundry z uporabo portala, OpenAI / Foundry Python SDK ali REST API - pokriva pripravo podatkov, usposabljanje, kontrolne točke in implementacijo. |
| [Neprestano prilagajanje](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Iterativni postopek izbora že prilagojenega modela kot osnovnega in **dodatnega prilagajanja** na novih naborih učnih primerov. |
| [Prilagajanje z orodjem (klic funkcije)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Prilagajanje vašega modela **s primeri klicev orodij** izboljša izhod - natančnejši, dosledni, enako oblikovani odgovori z uporabo manj tokenov v pozivu. |
| [Prilagajanje modelov: smernice Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Poiščite **katere modele je mogoče prilagoditi**, podprte metode (SFT / DPO / RFT) in regije, kjer so na voljo. |
| [Pregled prilagajanja: tehnike in modalitete](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Primerjajte tri tehnike usposabljanja (SFT, DPO, RFT) in dve modaliteti (brezstrežniške proti upravljanemu računanju) z navodili za izbor osnovnega modela in začetek. |
| **Vadnica**: [Prilagodite model v Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Ustvarite vzorčni podatkovni niz, pripravite se na prilagajanje, zaženite prilagoditveno opravilo na trenutno podprtem modelu, kot je `gpt-4.1-mini`, ter implementirajte prilagojen model v Azure. |
| **Vadnica**: [Prilagodite modele z brezstrežniško API implementacijo](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Prilagodite odprte in partnerske modele (Phi, Llama, Mistral in več) vašim podatkovnim nizom _z uporabo nizko-kodne, UI-osredotočene delovne poti_ v Microsoft Foundry. |
| **Vadnica**: [Prilagodite Hugging Face modele na Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Prilagodite Hugging Face model z knjižnico `transformers` na enem GPU z uporabo Azure Databricks in Hugging Face trenerja. |
| **Usposabljanje**: [Prilagodite temeljni model z Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Katalog modelov Azure Machine Learning ponuja številne odprtokodne modele, ki jih lahko prilagodite. Del poti učenja [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Vadnica**: [Azure OpenAI prilagajanje z Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Spremljajte in analizirajte prilagoditvena opravila na Azure z W&B. Razširja OpenAI vodnik za prilagajanje z Azure-specifičnimi koraki in sledenjem eksperimentov. |

## 2. Sekundarni viri

Ta oddelek zajema dodatne vire, ki jih je vredno raziskati, vendar jih nismo uspeli vključiti v lekcijo. Uporabite jih za gradnjo lastnega strokovnega znanja o tej temi.

| Naslov/Povezava | Opis |
| :--- | :--- |
| **OpenAI Cookbook**: [Priprava podatkov in analiza za prilagajanje klepetalnega modela](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Predobdelava in analiza podatkovnega niza za klepet pred prilagajanjem: preverite napake v formatu, pridobite osnovne statistike in ocenite število tokenov (in stroške). Povezan z [OpenAI vodičem za prilagajanje](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Prilagajanje za Retrieval Augmented Generation (RAG) z Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Obsežen primer prilagajanja OpenAI modelov za RAG, integracijo Qdrant in učenje na majhnem številu primerov za izboljšanje zmogljivosti in zmanjševanje izmišljotin. |
| **OpenAI Cookbook**: [Prilagajanje GPT z Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Uporabite W&B za spremljanje usposabljanja modelov in prilagajanja. Najprej preberite njihov [OpenAI vodič za prilagajanje](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst), nato preizkusite vajo iz Cookbooka. |
| **Hugging Face vadnica**: [Kako prilagoditi LLM z Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Prilagodite odprte LLM z uporabo Hugging Face TRL, Transformers in podatkovnih nizov: določite primere uporabe, nastavite razvojno okolje, pripravite podatkovni niz, prilagodite, ocenite in implementirajte. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Knjižnica brez kode / z nizko kodo od Hugging Face za prilagajanje številnih vrst modelov. Zaženite jo v lastnem oblaku, na Hugging Face Spaces ali lokalno prek GUI, CLI ali YAML konfiguracije. |
| **Unsloth**: [Vodnik za prilagajanje LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Odprtokodni okvir, ki poenostavlja lokalno prilagajanje LLM in okrepljeno učenje, z vnaprej pripravljenimi [zvezki](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->