[![開放原始碼模型](../../images/16-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## 簡介

開放原始碼 LLMs 的世界令人興奮且不斷演變。本課程旨在深入了解開放原始碼模型。如果您正在尋找有關專有模型與開放原始碼模型比較的資訊，請參閱["探索和比較不同的 LLMs" 課程](../../../02-exploring-and-comparing-different-llms/translations/tw/README.md?WT.mc_id=academic-105485-koreyst)。本課程還將涵蓋微調的主題，但更詳細的解釋可以在["微調 LLMs" 課程](../../../18-fine-tuning/translations/tw/README.md?WT.mc_id=academic-105485-koreyst)中找到。

## 學習目標

- 瞭解開放原始碼模型
- 瞭解使用開放原始碼模型的好處
- 探索 Hugging Face 和 Azure AI Studio 上可用的開放模型

## 什麼是開放原始碼模型？

開放原始碼軟體在各個領域的技術發展中扮演了至關重要的角色。開放原始碼倡議（OSI）已經定義了[軟體的10個標準](https://opensource.org/osd?WT.mc_id=academic-105485-koreyst)，以將其歸類為開放原始碼。源程式碼必須在OSI批准的許可下公開共享。

雖然 LLMs 的開發與軟體開發有相似的元素，但過程並不完全相同。這在社群中引發了許多關於 LLMs 背景下開放原始碼定義的討論。要使模型符合傳統的開放原始碼定義，以下資訊應該公開可用：

- 用於訓練模型的數據集。
- 作為訓練的一部分的完整模型權重。
- 評估程式碼。
- 微調程式碼。
- 完整模型權重和訓練指標。

目前只有少數模型符合此標準。[由Allen Institute for Artificial Intelligence (AllenAI) 創建的OLMo模型](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) 就是其中之一。

在本課程中，我們將這些模型稱為「開放模型」，因為在撰寫時它們可能不符合上述標準。

## 開放模型的好處

**高度可定制** - 由於開放模型發布時附有詳細的訓練資訊，研究人員和開發人員可以修改模型的內部結構。這使得能夠建立即高度專門化的模型，針對特定任務或研究領域進行微調。一些範例包括程式碼產生器、數學運算和生物學。

**成本** - 使用和部署這些模型的每個 token 成本低於專有模型。在建構生成式 AI 應用程式時，應該在您的使用案例中考量這些模型的性能與價格。

![Model Cost](../../images/model-price.png?WT.mc_id=academic-105485-koreyst)
來源: 人工分析

**靈活性** - 使用開放模型使您在使用不同模型或結合它們方面更加靈活。一個範例是 [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst)，用戶可以直接在使用者介面中選擇所使用的模型:

![選擇模型](../../images/choose-model.png?WT.mc_id=academic-105485-koreyst)

## 探索不同的開放模型

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), 由 Meta 開發，是一個針對聊天應用程式最佳化的開放模型。這是由於其微調方法，包括大量的對話和人類反饋。通過這種方法，模型產生更多符合人類期望的結果，從而提供更好的用戶體驗。

一些經過微調的Llama版本範例包括專門用於日語的[Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst)和增強版基礎模型的[Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst)。

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst)是一個專注於高效能和效率的開放模型。它使用專家混合方法，將一組專門的專家模型組合成一個系統，根據輸入選擇特定的模型來使用。這使得計算更加有效，因為模型只處理它們專門的輸入。

一些微調版本的Mistral範例包括專注於醫療領域的[BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst)和進行數學計算的[OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst)。

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) 是由技術創新研究所（**TII**）創建的 LLM。Falcon-40B 在 400 億個參數上進行了訓練，已顯示出在較少計算預算下比 GPT-3 表現更好。這是由於其使用了 FlashAttention 演算法和多查詢注意力，使其能夠在推論時減少記憶體需求。由於這種減少的推論時間，Falcon-40B 適用於聊天應用程式。

一些 Falcon 微調版本的範例包括 [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst)，一個基於開放模型的助手和 [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst)，其性能高於基礎模型。

## 如何選擇

選擇開放模型沒有唯一的答案。一個好的開始是使用 Azure AI Studio 的任務篩選功能。這將幫助你了解模型已經被訓練用於哪些類型的任務。Hugging Face 也維護了一個 LLM 排行榜，顯示基於某些指標的最佳表現模型。

在比較不同類型的LLM時，[Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) 是另一個很好的資源:

![模型品質](../../images/model-quality.png?WT.mc_id=academic-105485-koreyst)
來源: 人工分析

如果處理特定用例，搜尋專注於相同領域的微調版本可能會很有效。嘗試多個開放模型，看看它們如何根據你和你的用戶的期望表現，也是另一個好做法。

## 下一步

開放模型最棒的部分是你可以很快地開始使用它們。查看 [Azure AI Studio Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)，其中包含我們在此討論的特定 Hugging Face 集合。

## 學習不止於此，繼續旅程

完成本課程後，請查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以繼續提升您的生成式 AI 知識！

