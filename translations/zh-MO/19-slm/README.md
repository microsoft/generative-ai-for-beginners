# 初學者生成式 AI 小型語言模型入門
生成式 AI 是人工智能中一個引人入勝的領域，專注於創建能夠生成新內容的系統。這些內容可以涵蓋文本、圖像、音樂，甚至整個虛擬環境。生成式 AI 最令人興奮的應用之一就是語言模型領域。

## 甚麼是小型語言模型？

小型語言模型（SLM）是大型語言模型（LLM）的縮小版本，利用很多 LLM 的架構原理和技術，同時展示出顯著降低的計算需求。 

SLM 是設計用來生成類似人類文本的語言模型子集。與其較大型的對應物如 GPT-4 不同，SLM 更加精簡高效，適合計算資源有限的應用場景。儘管尺寸較小，它們仍能執行多種任務。一般來說，SLM 是通過壓縮或蒸餾 LLM 而建構，旨在保留原模型大部分功能和語言能力。這種模型尺寸的縮減降低了整體複雜度，使 SLM 在記憶體使用和計算需求上更為高效。儘管經過此類優化，SLM 依然能執行廣泛的自然語言處理（NLP）任務：

- 文字生成：創造連貫且語境相關的句子或段落。
- 文字補全：根據提示預測並補全句子。
- 翻譯：將文本從一種語言轉換為另一種語言。
- 摘要：將長篇文字濃縮成更短、更易理解的摘要。

不過，相較於大型模型，性能或理解深度上會有某些權衡。

## 小型語言模型如何運作？
SLM 透過大量文本數據訓練。在訓練過程中，它們學習語言的模式和結構，使其能生成語法正確且語境適切的文本。訓練過程包括：

- 數據收集：從多種來源收集大量文本數據。
- 預處理：清理並整理數據，讓其適合訓練。
- 訓練：使用機器學習算法教模型如何理解和生成文本。
- 微調：調整模型以提升在特定任務上的表現。

SLM 的發展是響應在資源受限環境中部署模型的日益需求，比如行動裝置或邊緣運算平台，因為完全版的 LLM 由於資源消耗龐大往往不實用。透過聚焦效率，SLM 平衡了性能和可及性，使其能在不同領域更廣泛地應用。

![slm](../../../translated_images/zh-MO/slm.4058842744d0444a.webp)

## 學習目標

本課程希望介紹 SLM 的知識，並結合 Microsoft Phi-3 來學習文字內容、視覺與 MoE 等不同場景。

課程結束後，您應該能回答以下問題：

- 甚麼是 SLM？
- SLM 與 LLM 有何不同？
- 甚麼是 Microsoft Phi-3/3.5 系列？
- 如何使用 Microsoft Phi-3/3.5 系列進行推論？

準備好了嗎？讓我們開始吧。

## 大型語言模型（LLM）與小型語言模型（SLM）的區別

LLM 與 SLM 都建立在機率機器學習的基礎原理上，採用相似的架構設計、訓練方法、數據生成流程與模型評估技術。然而，這兩種模型有幾個關鍵差異。

## 小型語言模型的應用

SLM 有多種應用，包括：

- 聊天機器人：以對話方式提供客戶支持和與用戶互動。
- 內容創作：協助作家產生點子，甚至草擬整篇文章。
- 教育：協助學生完成寫作作業或學習新語言。
- 無障礙輔助：為殘障人士創建工具，如文字轉語音系統。

<strong>規模</strong>
  
LLM 與 SLM 的主要區別之一在於模型規模。LLM 如 ChatGPT（GPT-4）約有 1.76 兆參數，而開源 SLM 如 Mistral 7B 設計時參數數量明顯少得多，約 70 億。這種差異主要源於模型架構和訓練流程的不同。例如，ChatGPT 採用帶有自注意力機制的編碼器-解碼器架構，而 Mistral 7B 採用滑動窗口注意力，使其能在僅解碼器模型中更高效訓練。這種架構差異對模型的複雜度和性能有深遠影響。

<strong>理解力</strong>

SLM 通常針對特定領域進行優化，使其專門化程度高，但可能在多領域知識的廣泛語境理解方面有所限制。相比之下，LLM 旨在模擬更全面的人類智慧。LLM 在大量多元數據上訓練，能在多種領域展現良好表現，提供更高的多才多藝和適應性。因此，LLM 更適合用於廣泛的下游任務，如自然語言處理與程式設計。

<strong>運算需求</strong>

LLM 的訓練和部署資源消耗龐大，通常需龐大的計算基礎設施，包括大規模 GPU 集群。例如，從零開始訓練 ChatGPT 可能需數千 GPU 持續多時。相比較，SLM 因參數數量較少，對計算資源需求更低。像 Mistral 7B 這類模型可在具備適中 GPU 能力的本地機器上訓練和運行，雖然訓練仍需多 GPU 並耗時數小時。

<strong>偏見</strong>

LLM 中存在偏見問題，主要因其訓練數據的特性。這些模型往往依賴網絡上開放的原始數據，這些數據可能對某些群體表述不足或錯誤標註，亦可能反映出語言方言、地域變異和語法規則引起的語言偏見。此外，LLM 複雜的架構可能無意中加劇偏見，若缺乏細心微調，偏見問題不容易被察覺。另一方面，SLM 因為訓練於較受限制、領域專一的數據集，本質上較不容易受到此類偏見影響，雖然仍然不能完全避免。

<strong>推論</strong>

SLM 的尺寸減少賦予它們推論速度上的顯著優勢，讓其能在本地硬件上高效產出結果，無需大量並行處理。相比之下，LLM 因規模和複雜度大多需要龐大量的並行計算資源才能達到可接受的推論時間。多用戶同時使用時，LLM 的響應速度尤為緩慢，尤其是在大規模部署時。

總結來說，雖然 LLM 和 SLM 都基於機器學習核心理論，但在模型尺寸、資源需求、語境理解、偏見影響及推論速度等方面存在顯著差異。這些差異反映了它們適應不同用例的能力，LLM 多才多藝但資源重，而 SLM 則在特定領域內兼顧效能與計算需求的降低。

***注意：本課程將以 Microsoft Phi-3 / 3.5 為例介紹 SLM。***

## 介紹 Phi-3 / Phi-3.5 系列

Phi-3 / 3.5 系列主要針對文字、視覺及代理（MoE）應用場景：

### Phi-3 / 3.5 指令模型

主要用於文本生成、聊天補全及內容資訊提取等。

**Phi-3-mini**

3.8B 語言模型可在 Microsoft Foundry、Hugging Face 與 Ollama 獲得。Phi-3 模型在多個關鍵基準測試中顯著優於相同或更大型語言模型（見下方基準數據，數值越高越好）。Phi-3-mini 的表現勝過其尺寸兩倍的模型，而 Phi-3-small 及 Phi-3-medium 則超越更大型模型，包括 GPT-3.5。

**Phi-3-small 與 medium**

Phi-3-small 僅用 7B 參數，便在多種語言、推理、程式碼及數學基準測試中擊敗 GPT-3.5T。

14B 參數的 Phi-3-medium 延續此趨勢，性能優於 Gemini 1.0 Pro。

**Phi-3.5-mini**

可視為 Phi-3-mini 的升級版。雖然參數保持不變，但提升了對多語言的支持（支持 20 多種語言：阿拉伯語、中文、捷克語、丹麥語、荷蘭語、英語、芬蘭語、法語、德語、希伯來語、匈牙利語、義大利語、日語、韓語、挪威語、波蘭語、葡萄牙語、俄語、西班牙語、瑞典語、泰語、土耳其語、烏克蘭語）並增強了長上下文支持。

3.8B 參數的 Phi-3.5-mini 表現優於同尺寸語言模型，並與兩倍參數量的模型相當。

### Phi-3 / 3.5 視覺模型

Phi-3/3.5 的指令模型可視為 Phi 的理解能力，而視覺模型則賦予 Phi 觀察世界的眼睛。


**Phi-3-Vision**

只有 4.2B 參數的 Phi-3-vision 延續表現優勢，在通用視覺推理、OCR、表格及圖表理解任務上超越更大型的 Claude-3 Haiku 與 Gemini 1.0 Pro V。


**Phi-3.5-Vision**

Phi-3.5-Vision 是 Phi-3-Vision 的升級版本，新增多圖像支持。可視為視覺能力提升，不僅能看圖片，還能理解影片。

Phi-3.5-vision 在 OCR、表格和圖表理解任務中優於大型模型如 Claude-3.5 Sonnet 及 Gemini 1.5 Flash，在一般視覺知識推理任務中相當。支持多幀輸入，即能對多張圖片進行推理。


### Phi-3.5-MoE

***混合專家模型 (MoE)*** 可使模型在更少計算下完成預訓練，意味著使用與密集模型相同的計算預算，可大幅擴展模型或數據集規模。具體來說，MoE 模型能在預訓練階段更快達到與密集模型相同的質量。

Phi-3.5-MoE 包含 16 個 3.8B 專家模組。只用 6.6B 活躍參數的 Phi-3.5-MoE 在推理、語言理解與數學能力方面達到與更大型模型相當的水平。

我們可以根據不同場景使用 Phi-3/3.5 家族模型。與 LLM 不同，Phi-3/3.5-mini 或 Phi-3/3.5-Vision 可部署於邊緣設備。


## 如何使用 Phi-3/3.5 家族模型

我們希望將 Phi-3/3.5 應用於不同場景。接下來，我們將根據不同場景使用 Phi-3/3.5。

![phi3](../../../translated_images/zh-MO/phi3.655208c3186ae381.webp)

### 通過雲端 API 進行推論

**Microsoft Foundry 模型**

> **注意：** GitHub Models 將於 2026 年 7 月底退役。[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 為直接替代方案。

Microsoft Foundry Models 是最直接的方式。您可以透過 Foundry 模型目錄快速存取 Phi-3/3.5-Instruct 模型。結合 Azure AI 推論 SDK / OpenAI SDK，您可透過程式碼調用 API 完成 Phi-3/3.5-Instruct。您也可通過 Playground 測試不同效果。

- 示範：Phi-3-mini 與 Phi-3.5-mini 在中文場景下的效果比較

![phi3](../../../translated_images/zh-MO/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/zh-MO/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

如果想使用視覺和 MoE 模型，也可以利用 Microsoft Foundry 完成調用。若有興趣，您可以閱讀 Phi-3 食譜，了解如何通過 Microsoft Foundry 調用 Phi-3/3.5 Instruct、Vision、MoE [請點此連結](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

除了基於雲端的 Microsoft Foundry Models 目錄外，您也可以使用 [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) 完成相關調用。您可以訪問 NVIDIA NIM 進行 Phi-3/3.5 家族的 API 調用。NVIDIA NIM（NVIDIA 推論微服務）是一套加速推論微服務，旨在幫助開發者在各種環境中有效部署 AI 模型，包括雲端、數據中心和工作站。

以下是 NVIDIA NIM 的一些主要特點：

- **部署簡易：** NIM 允許使用單條命令部署 AI 模型，便於整合進現有工作流程。

- **優化的效能：** 它利用 NVIDIA 預先優化的推理引擎，如 TensorRT 和 TensorRT-LLM，以確保低延遲和高吞吐量。
- **可擴展性：** NIM 支援 Kubernetes 上的自動擴展，使其能有效處理多變的工作負載。
- **安全性與控制：** 組織可透過在自有管理的基礎設施上自託管 NIM 微服務，維持對其數據和應用程式的控制權。
- **標準 API：** NIM 提供行業標準的 API，使構建和整合如聊天機器人、AI 助理等 AI 應用更為簡便。

NIM 是 NVIDIA AI Enterprise 的一部分，旨在簡化 AI 模型的部署和運行，確保其在 NVIDIA GPU 上高效運行。

- 示範：使用 NVIDIA NIM 呼叫 Phi-3.5-Vision-API  [[點擊此鏈接](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### 本地運行 Phi-3/3.5
與 Phi-3 或任何類似 GPT-3 的語言模型相關的推理，是指基於輸入來生成回應或預測的過程。當你向 Phi-3 提供提示或問題時，它會利用其訓練好的神經網絡，透過分析訓練數據中的模式和關聯，推斷出最可能且相關的回應。

**Hugging Face Transformer**
Hugging Face Transformers 是一個強大的函式庫，設計用於自然語言處理（NLP）和其他機器學習任務。以下是其一些重點：

1. <strong>預訓練模型</strong>：提供數千個預訓練模型，可用於文字分類、命名實體識別、問答、摘要、翻譯和文本生成等多種任務。

2. <strong>框架互通性</strong>：此函式庫支援多種深度學習框架，包括 PyTorch、TensorFlow 和 JAX，使你能在一個框架中訓練模型，並在另一個框架中使用它。

3. <strong>多模態能力</strong>：除了 NLP，Hugging Face Transformers 還支援計算機視覺（例如影像分類、物體檢測）和音頻處理（例如語音識別、音頻分類）任務。

4. <strong>易用性</strong>：函式庫提供 API 和工具，方便下載和微調模型，適合初學者和專家使用。

5. <strong>社群和資源</strong>：Hugging Face 擁有活躍的社群，以及豐富的文檔、教學和指南，幫助使用者快速上手並充分利用函式庫。
[官方文件](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 或其 [GitHub 倉庫](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)。

這是最常用的方法，但也需要 GPU 加速。畢竟視覺和 MoE 等場景需求大量計算，如果未量化，CPU 會非常慢。


- 示範：使用 Transformer 呼叫 Phi-3.5-Instruct [點擊此鏈接](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 示範：使用 Transformer 呼叫 Phi-3.5-Vision [點擊此鏈接](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 示範：使用 Transformer 呼叫 Phi-3.5-MoE [點擊此鏈接](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) 是一個平台，設計讓使用者更容易在本地機器上運行大型語言模型（LLM）。它支援多種模型，如 Llama 3.1、Phi 3、Mistral 和 Gemma 2 等。該平台通過將模型權重、設定和數據打包成一個整合包，簡化了自訂和建立模型的流程，讓使用者更易上手。Ollama 支援 macOS、Linux 及 Windows。如果你想試驗或部署 LLM 但不想依賴雲服務，這是最佳工具。Ollama 是最直接的方式，只需執行以下命令。


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 是微軟的離線本地運行時環境，可在你自己的硬件上完全本地運行如 Phi 之類的模型 — 無需 Azure 訂閱、API 金鑰或網絡連接。它會自動選擇最佳的執行提供者（NPU、GPU 或 CPU），並提供 OpenAI 相容的端點，讓現有的 `openai`/Azure AI 推理 SDK 代碼只需少量變更即可切換使用。請參閱 [Foundry Local 文檔](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 開始使用。

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

或直接在 Python 中使用 SDK：

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) 是一款跨平台機器學習推理與訓練加速器。ONNX Runtime for Generative AI (GENAI) 是一個強大的工具，幫助你高效運行生成式 AI 模型，跨越各種平台。

## 什麼是 ONNX Runtime？
ONNX Runtime 是一個開源項目，支持機器學習模型的高性能推理。它支援 Open Neural Network Exchange (ONNX) 格式的模型，該格式是機器學習模型表示的標準。ONNX Runtime 的推理能提升客戶體驗並降低成本，支援來自深度學習框架如 PyTorch 和 TensorFlow/Keras，以及經典機器學習庫如 scikit-learn、LightGBM、XGBoost 等的模型。ONNX Runtime 相容不同硬件、驅動和作業系統，透過利用硬件加速器與圖優化和轉換實現最佳效能。

## 什麼是生成式 AI？
生成式 AI 指能基於所訓練數據生成新內容（如文本、圖像、音樂）的 AI 系統。示例包括語言模型 GPT-3 和圖像生成模型 Stable Diffusion。ONNX Runtime for GenAI 函式庫提供生成式 AI 迴圈，涵蓋 ONNX Runtime 的推理、logits 處理、搜尋與取樣及 KV 快取管理。

## ONNX Runtime for GENAI
ONNX Runtime for GENAI 擴展 ONNX Runtime 的功能，支持生成式 AI 模型。以下是一些主要特點：

- **廣泛的平台支援：** 它可在多種平台上運行，包括 Windows、Linux、macOS、Android 和 iOS。
- **模型支援：** 支持多種流行的生成式 AI 模型，如 LLaMA、GPT-Neo、BLOOM 及其他。
- **效能優化：** 包含對各種硬件加速器（如 NVIDIA GPU、AMD GPU 等）的優化。
- **易用性：** 提供 API，方便整合進應用程式，可用最少的程式碼生成文字、圖像和其他內容。
- 使用者可以調用高階的 generate() 方法，或在迴圈中逐一產生 token，且可選擇在迴圈內更新生成參數。
- ONNX Runtime 亦支援貪婪/束搜尋和 TopP、TopK 取樣來生成 token 序列，以及內建的 logits 處理如重複懲罰。你也能輕鬆加入自訂評分。

## 快速開始
要開始使用 ONNX Runtime for GENAI，可依照以下步驟：

### 安裝 ONNX Runtime：
```Python
pip install onnxruntime
```
### 安裝生成式 AI 擴展：
```Python
pip install onnxruntime-genai
```

### 運行模型：以下是 Python 的簡單範例：
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### 示範：使用 ONNX Runtime GenAI 呼叫 Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


<strong>其他</strong>

除了 ONNX Runtime、Ollama 和 Foundry Local 參考方法外，我們還可以根據不同廠商提供的模型參考方法完成量化模型的參考。例如 Apple MLX 框架結合 Apple Metal、Qualcomm QNN 配合 NPU、Intel OpenVINO 配合 CPU/GPU 等。更多內容可參考 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## 更多

我們已學習 Phi-3/3.5 家族的基礎知識，但要深入了解 SLM，我們需要更多知識。你可在 Phi-3 Cookbook 中找到答案。如想了解更多，請訪問 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->