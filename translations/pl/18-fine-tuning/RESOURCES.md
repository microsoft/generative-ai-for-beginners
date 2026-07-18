# Zasoby do samodzielnej nauki

Lekcja została opracowana na podstawie podstawowych zasobów OpenAI i Microsoft Foundry jako odniesienia dla terminologii i samouczków. Poniżej znajduje się niekompletna lista do samodzielnej nauki. Każdy z poniższych linków prowadzi do bieżących, wspieranych materiałów.

## 1. Zasoby podstawowe

| Tytuł/Link | Opis |
| :--- | :--- |
| [Dostrajanie modeli OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Dostrajanie poprawia uczenie się na podstawie kilku przykładów przez trenowanie na znacznie większej liczbie przykładów niż można zmieścić w promptcie - obniżając koszty, poprawiając jakość odpowiedzi i umożliwiając żądania o niższej latencji. **Zapoznaj się z przeglądem dostrajania od OpenAI.** |
| [Kiedy używać dostrajania Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Zrozum **czym jest dostrajanie (koncepcja)**, dlaczego warto je rozważyć, jakie dane wykorzystać oraz jak mierzyć jakość – oraz kiedy odpowiednie są SFT, DPO lub RFT. |
| [Dostosuj model za pomocą dostrajania](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Kompletny **przewodnik (proces)** dostrajania w Microsoft Foundry przy użyciu portalu, OpenAI / Foundry Python SDK lub REST API – obejmuje przygotowanie danych, trening, punkty kontrolne i wdrożenie. |
| [Ciągłe dostrajanie](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Iteracyjny proces wyboru już dostrojonego modelu jako modelu bazowego i **dalszego dostrajania** na nowych zestawach przykładów treningowych. |
| [Dostrajanie z wywoływaniem narzędzi (funkcji)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Dostrajanie modelu **przykładami wywołań narzędzi** poprawia wyniki – bardziej precyzyjne, spójne, podobnie sformatowane odpowiedzi z mniejszą liczbą tokenów używanych w promptcie. |
| [Dostrajanie modeli: wskazówki Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Sprawdź, **które modele można dostroić**, jakich metod używają (SFT / DPO / RFT) oraz w jakich regionach są dostępne. |
| [Przegląd dostrajania: techniki i formy](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Porównaj trzy techniki treningu (SFT, DPO, RFT) i dwa tryby (serverless vs. zarządzana moc obliczeniowa), z poradami jak wybrać model bazowy i jak zacząć. |
| **Samouczek**: [Dostrajanie modelu w Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Stwórz przykładowy zestaw danych, przygotuj się do dostrajania, uruchom zadanie dostrajania na aktualnie wspieranym modelu, takim jak `gpt-4.1-mini`, i wdroż dostrojony model na Azure. |
| **Samouczek**: [Dostrajanie modeli z wdrożeniami API bezserwerowymi](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Dostosuj modele open i partnerskie (Phi, Llama, Mistral i inne) do swoich zestawów danych _stosując niskokodowy, oparty na interfejsie użytkownika workflow_ w Microsoft Foundry. |
| **Samouczek**: [Dostrajanie modeli Hugging Face na Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Dostrój model Hugging Face z biblioteką `transformers` na pojedynczym GPU wykorzystując Azure Databricks i narzędzie Hugging Face Trainer. |
| **Szkolenie**: [Dostrajanie modelu podstawowego z Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Katalog modeli Azure Machine Learning oferuje wiele modeli open-source, które możesz dostroić. Część [ścieżki nauki Azure ML Generative AI](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Samouczek**: [Dostrajanie Azure OpenAI z Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Śledź i analizuj przebieg dostrajania na Azure za pomocą W&B. Rozszerza przewodnik dostrajania OpenAI o kroki specyficzne dla Azure i śledzenie eksperymentów. |

## 2. Zasoby uzupełniające

Ta sekcja zawiera dodatkowe zasoby warte zapoznania, których nie udało się omówić podczas lekcji. Wykorzystaj je, aby rozwijać swoją wiedzę na ten temat.

| Tytuł/Link | Opis |
| :--- | :--- |
| **OpenAI Cookbook**: [Przygotowanie i analiza danych do dostrajania modelu czatu](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Przetwórz i przeanalizuj zestaw danych czatu przed dostrajaniem: sprawdź błędy formatowania, uzyskaj podstawowe statystyki i oszacuj liczbę tokenów (i koszt). W połączeniu z [przewodnikiem OpenAI do dostrajania](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Dostrajanie do Retrieval Augmented Generation (RAG) z Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Kompleksowy przykład dostrajania modeli OpenAI do RAG, integrujący Qdrant i few-shot learning, aby zwiększyć wydajność i zmniejszyć błędy. |
| **OpenAI Cookbook**: [Dostrajanie GPT z Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Użyj W&B do śledzenia treningu i dostrajania modeli. Najpierw przeczytaj ich [przewodnik po dostrajaniu OpenAI](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst), następnie wypróbuj ćwiczenie z Cookbook. |
| **Samouczek Hugging Face**: [Jak dostroić LLM-y za pomocą Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Dostrajanie otwartych LLM z wykorzystaniem Hugging Face TRL, Transformers i datasets: określ przypadek użycia, skonfiguruj środowisko developerskie, przygotuj zestaw danych, dostrój, oceń i wdroż. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Biblioteka no-code / low-code od Hugging Face do dostrajania wielu typów modeli. Uruchom na własnej chmurze, w Hugging Face Spaces lub lokalnie przez GUI, CLI albo YAML. |
| **Unsloth**: [Przewodnik po dostrajaniu LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Open-source’owy framework usprawniający lokalne dostrajanie LLM i uczenie przez wzmacnianie, z gotowymi [notatnikami](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->