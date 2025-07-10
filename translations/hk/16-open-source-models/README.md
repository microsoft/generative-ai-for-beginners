<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0bba96e53ab841d99db731892a51fab8",
  "translation_date": "2025-07-09T17:05:29+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "hk"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.hk.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## 介紹

開源大型語言模型（LLM）的世界充滿活力且不斷演進。本課程旨在深入介紹開源模型。如果你想了解專有模型與開源模型的比較，請參考[「探索與比較不同的LLM」課程](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)。本課程也會涵蓋微調的主題，但更詳細的說明可見於[「微調LLM」課程](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst)。

## 學習目標

- 了解開源模型的基本概念
- 理解使用開源模型的優勢
- 探索 Hugging Face 與 Azure AI Studio 上可用的開源模型

## 什麼是開源模型？

開源軟件在各個技術領域的發展中扮演了關鍵角色。開源倡議組織（OSI）定義了[軟件成為開源的10項標準](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst)，其中源代碼必須在OSI認可的授權下公開分享。

雖然大型語言模型的開發與軟件開發有相似之處，但過程並不完全相同。這也引發了社群對於LLM中「開源」定義的討論。若要符合傳統開源定義，模型應公開以下資訊：

- 用於訓練的數據集
- 作為訓練一部分的完整模型權重
- 評估代碼
- 微調代碼
- 完整模型權重與訓練指標

目前符合這些標準的模型並不多，[由 Allen Institute for Artificial Intelligence (AllenAI) 開發的 OLMo 模型](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) 是其中之一。

在本課程中，我們將統稱這些模型為「開源模型」，因為它們在撰寫時可能尚未完全符合上述標準。

## 開源模型的優勢

**高度可定制** — 由於開源模型附帶詳細的訓練資訊，研究人員和開發者可以修改模型內部結構，打造針對特定任務或領域的專門模型。例如程式碼生成、數學運算和生物學等領域。

**成本** — 使用和部署這些模型的每個 token 成本通常低於專有模型。在開發生成式 AI 應用時，應根據你的使用案例評估性能與價格的平衡。

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.hk.png)  
來源：Artificial Analysis

**彈性** — 使用開源模型讓你能靈活選擇不同模型或將它們結合使用。例如，[HuggingChat 助理](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) 允許用戶直接在介面中選擇使用的模型：

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.hk.png)

## 探索不同的開源模型

### Llama 2

[Meta 開發的 Llama 2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst) 是一款針對聊天應用優化的開源模型。這得益於其微調方法，包含大量對話數據和人類反饋，使模型產出的結果更符合人類期望，提升使用體驗。

Llama 的微調版本包括專注於日語的[Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst)，以及基礎模型的強化版[Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst)。

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) 是一款注重高效能與效率的開源模型。它採用專家混合（Mixture-of-Experts）方法，將多個專門模型組合成一個系統，根據輸入選擇特定模型進行處理，提升計算效率。

Mistral 的微調版本包括專注醫療領域的[BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst)，以及擅長數學運算的[OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst)。

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) 是由 Technology Innovation Institute（**TII**）開發的 LLM。Falcon-40B 擁有 400 億參數，據稱在較低計算資源下表現優於 GPT-3。這得益於其使用的 FlashAttention 演算法和多查詢注意力機制，降低推理時的記憶體需求。推理時間縮短使 Falcon-40B 適合用於聊天應用。

Falcon 的微調版本包括基於開源模型打造的[OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst)，以及性能優於基礎模型的[GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst)。

## 如何選擇

選擇開源模型沒有唯一答案。建議先利用 Azure AI Studio 的任務篩選功能，了解模型訓練的任務類型。Hugging Face 也維護一個 LLM 排行榜，根據特定指標展示表現最佳的模型。

若想跨類型比較 LLM，[Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) 是另一個很好的資源：

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.hk.png)  
來源：Artificial Analysis

針對特定使用案例，尋找專注該領域的微調版本會更有效。嘗試多款開源模型，觀察它們是否符合你和用戶的期望，也是很好的做法。

## 下一步

開源模型的最大優點是你可以很快開始使用。請參考[Azure AI Studio 模型目錄](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)，其中包含我們在此討論的 Hugging Face 模型合集。

## 學習不止於此，繼續前行

完成本課程後，歡迎瀏覽我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。