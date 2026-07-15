# 小型語言模型入門：生成式 AI 初學者指南
生成式 AI 是人工智能中一個迷人的領域，專注於創建能夠生成新內容的系統。這些內容可以涵蓋文字、圖片、音樂甚至整個虛擬環境。生成式 AI 最令人興奮的應用之一就是語言模型領域。

## 甚麼是小型語言模型？

小型語言模型（SLM）代表大型語言模型（LLM）的縮小版本，採用許多 LLM 的架構原理和技術，但計算資源需求大幅降低。

SLM 是專為生成類人文本而設計的語言模型子集。與其大型對手如 GPT-4 不同，SLM 體積更小且更高效，適用於計算資源有限的應用環境。儘管體積較小，它們仍能執行多種任務。SLM 通常透過壓縮或蒸餾 LLM 來構建，目標是保留原始模型大部分功能和語言能力。縮小模型規模降低了整體複雜性，令 SLM 在記憶體使用量和計算需求方面更具效率。這些優化使得 SLM 仍能完成各種自然語言處理 (NLP) 任務：

- 文字生成：創造連貫且符合語境的句子或段落。
- 文字補全：根據給定提示預測並完成句子。
- 翻譯：將文字從一種語言轉換成另一種語言。
- 摘要：將長文本濃縮成更精簡且易於理解的摘要。

雖然相比大型模型在表現或理解深度上有所折衷。

## 小型語言模型如何運作？
SLM 在大量文本數據上訓練，學習語言的結構和模式，使其能生成語法正確且符合語境的文本。訓練過程包括：

- 數據收集：從各種來源收集大規模文本數據集。
- 預處理：清理並組織數據，使其適合訓練。
- 訓練：使用機器學習算法教授模型理解和生成文本。
- 微調：調整模型以提升其在特定任務上的表現。

SLM 的發展符合在資源有限環境（如移動設備或邊緣計算平台）部署模型的日益增長需求，因為全面的 LLM 由於資源需求龐大可能不切實際。透過強調效率，SLM 在性能與易獲得性之間取得平衡，使其能在多個領域更廣泛應用。

![slm](../../../translated_images/zh-HK/slm.4058842744d0444a.webp)

## 學習目標

本課程希望介紹 SLM 知識，並結合 Microsoft Phi-3 來學習文本內容、視覺和 MoE 的不同場景。

在課程結束時，你應能回答以下問題：

- 甚麼是 SLM？
- SLM 與 LLM 有何不同？
- 甚麼是 Microsoft Phi-3/3.5 家族？
- 如何使用 Microsoft Phi-3/3.5 家族進行推理？

準備好了嗎？讓我們開始吧。

## 大型語言模型（LLMs）與小型語言模型（SLMs）的區別

LLM 與 SLM 都基於概率機器學習的基本原理，在架構設計、訓練方法、數據生成流程及模型評估技術上採取相似方式。但有幾個關鍵因素區分這兩種模型。

## 小型語言模型的應用

SLM 有廣泛的應用，包括：

- 聊天機器人：提供客戶支持並以對話方式與用戶互動。
- 內容創作：協助作者生成創意或草擬整篇文章。
- 教育：幫助學生完成寫作作業或學習新語言。
- 無障礙功能：為殘障人士創建工具，如文字轉語音系統。

<strong>模型大小</strong>
  
LLM 與 SLM 最大的區別之一在於模型規模。LLM（如 ChatGPT GPT-4）估計擁有 1.76 萬億參數，而開源 SLM（如 Mistral 7B）設計時參數顯著較少，約 70 億。此差異主要源於模型架構和訓練過程的不同。例如，ChatGPT 使用編碼器-解碼器架構中的自注意力機制，而 Mistral 7B 採用滑動窗口注意力機制，使其能在僅解碼器模型中更有效進行訓練。這種架構差異對模型的複雜度和性能有深遠影響。

<strong>理解能力</strong>

SLM 通常針對特定領域優化，專業性強但可能限制了跨領域的廣泛語境理解能力。相對而言，LLM 旨在模擬更全面的人類智能。LLM 在龐大且多元數據集上訓練，設計成能在多種領域表現良好，更具多功能性和適應力。因此，LLM 更適用於各種下游任務，如自然語言處理和程式設計。

<strong>計算需求</strong>

LLM 的訓練與部署資源密集，往往需要龐大的計算基礎設施，包括大規模 GPU 集群。例如，從零開始訓練 ChatGPT 可能需要數千個 GPU 持續長時間運算。相比之下，SLM 參數較少，計算資源需求較低。像 Mistral 7B 這樣的模型可在具備中等 GPU 功能的本地機器上訓練和運行，儘管訓練依然需要多張 GPU 多小時運行。

<strong>偏見問題</strong>

偏見是 LLM 中已知的問題，主要源於訓練數據的性質。這些模型通常依賴來自網絡的原始公開數據，可能存在對某些群體的代表性不足或錯誤標籤，也可能反映語言偏見，如方言、地理變異與語法規則差異。此外，LLM 的複雜架構可能無意中加劇偏見，若無仔細微調，偏見問題可能不易察覺。相對而言，SLM 訓練於較受限的領域特定數據集，本質上較不易受此類偏見影響，儘管也非完全免疫。

<strong>推理速度</strong>

由於體積較小，SLM 在推理速度上具有顯著優勢，可在本地硬件上高效產生輸出，無需大量並行處理。相比之下，LLM 因模型規模與複雜度，通常需要大量並行計算資源以達到可接受的推理速度。多用戶同時使用時，LLM 的回應時間進一步放慢，尤其在大規模部署時更為明顯。

總結而言，儘管 LLM 和 SLM 均基於機器學習基礎，但在模型規模、資源需求、語境理解、偏見敏感性及推理速度等方面存在顯著差異。這些差異反映了它們在不同使用案例中的適用性：LLM 更通用但資源消耗大，SLM 則提供領域特定的效率並降低計算需求。

***注意：本課程將以 Microsoft Phi-3 / 3.5 為例介紹 SLM。***

## 介紹 Phi-3 / Phi-3.5 系列

Phi-3 / 3.5 系列主要針對文本、視覺及 Agent（MoE）應用場景：

### Phi-3 / 3.5 指令模型

主要用於文字生成、聊天補全及內容信息提取等。

**Phi-3-mini**

3.8B 參數語言模型可在 Microsoft Foundry、Hugging Face 和 Ollama 上使用。Phi-3 模型在主要基準測試中大幅超越相同及較大規模語言模型（見下方基準數據，數值越高越好）。Phi-3-mini 的表現優於其兩倍參數模型，而 Phi-3-small 與 Phi-3-medium 則超越包括 GPT-3.5 在內的更大模型。

**Phi-3-small 與 medium**

Phi-3-small 僅擁有 7B 參數，卻在多項語言、推理、程式碼及數學基準中勝過 GPT-3.5T。

Phi-3-medium 擁有 14B 參數，延續此趨勢，性能優於 Gemini 1.0 Pro。

**Phi-3.5-mini**

可視為 Phi-3-mini 的升級版。儘管參數保持不變，但增強了對多語言的支持（超過 20 種語言，包括阿拉伯語、中文、捷克語、丹麥語、荷蘭語、英語、芬蘭語、法語、德語、希伯來語、匈牙利語、義大利語、日語、韓語、挪威語、波蘭語、葡萄牙語、俄語、西班牙語、瑞典語、泰語、土耳其語、烏克蘭語）並強化長上下文支持。

3.8B 參數的 Phi-3.5-mini 其性能超越相同尺寸語言模型，媲美參數量為其兩倍的模型。

### Phi-3 / 3.5 視覺模型

可將 Phi-3/3.5 的指令模型視為 Phi 的理解能力，而 Vision 則賦予 Phi 觀察和理解世界的眼睛。


**Phi-3-Vision**

Phi-3-vision 只有 4.2B 參數，仍繼續優勢，在通用視覺推理、OCR 以及表格和圖表理解任務中優於更大模型，如 Claude-3 Haiku 和 Gemini 1.0 Pro V。


**Phi-3.5-Vision**

Phi-3.5-Vision 是 Phi-3-Vision 的升級版，新增多圖像支持。可理解為視覺能力提升，不僅能看圖片，還能處理影片。

Phi-3.5-vision 在 OCR、表格及圖表理解任務中勝過 Claude-3.5 Sonnet 和 Gemini 1.5 Flash 等更大模型，且在通用視覺知識推理任務達到同等表現。支持多幀輸入，即能對多張輸入圖片進行推理。


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** 使模型可使用更少計算資源進行預訓練，這意味著在相同計算預算下，你可以大幅擴大模型或數據集規模。具體來說，MoE 模型在預訓練期間能更快達到與其密集模型對應品質。

Phi-3.5-MoE 包含 16 個 3.8B 參數的專家模組。Phi-3.5-MoE 活躍參數僅有 6.6B，卻達到與更大型模型相似的推理、語言理解及數學能力。

你可根據不同場景使用 Phi-3/3.5 系列模型。與 LLM 不同，你可在邊緣設備上部署 Phi-3/3.5-mini 或 Phi-3/3.5-Vision。


## 如何使用 Phi-3/3.5 系列模型

希望能在不同場景下使用 Phi-3/3.5。接下來，我們將根據不同情境使用 Phi-3/3.5。

![phi3](../../../translated_images/zh-HK/phi3.655208c3186ae381.webp)

### 透過雲端 API 進行推理

**Microsoft Foundry 模型**

> **注意：** GitHub Models 將於 2026 年 7 月底退役。[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 是直接替代方案。

Microsoft Foundry Models 是最直接的方式。你可透過 Foundry 模型目錄快速訪問 Phi-3/3.5-Instruct 模型。結合 Azure AI 推理 SDK / OpenAI SDK，你能通過程式碼調用 API 完成 Phi-3/3.5-Instruct 的呼叫。你亦可透過 Playground 測試不同效果。

- 範例：在中文場景中比較 Phi-3-mini 與 Phi-3.5-mini 的效果

![phi3](../../../translated_images/zh-HK/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/zh-HK/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

若想使用視覺與 MoE 模型，亦可使用 Microsoft Foundry 完成呼叫。如有興趣，可閱讀 Phi-3 Cookbook 深入了解如何通過 Microsoft Foundry 呼叫 Phi-3/3.5 Instruct、Vision、MoE [點此連結](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

除了基於雲端的 Microsoft Foundry Models 目錄外，你亦可使用 [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) 完成相關呼叫。你可訪問 NVIDIA NIM 執行 Phi-3/3.5 系列的 API 呼叫。NVIDIA NIM（NVIDIA 推理微服務）是一套加速的推理微服務，旨在幫助開發者高效部署 AI 模型，適用於多種環境，包括雲端、數據中心及工作站。

以下是 NVIDIA NIM 的一些主要特點：

- **部署簡便性：** NIM 支持一鍵部署 AI 模型，方便集成到現有工作流中。

- **優化效能：** 它利用 NVIDIA 預先優化的推理引擎，例如 TensorRT 和 TensorRT-LLM，以確保低延遲和高吞吐量。
- **可擴展性：** NIM 支援 Kubernetes 自動擴展，使其能有效應對不同的工作負載。
- **安全性與控制：** 組織可以通過在自主管理的基礎設施上自我托管 NIM 微服務，來保持對其數據和應用程序的控制。
- **標準 API：** NIM 提供業界標準的 API，便於構建和整合如聊天機器人、AI 助手等 AI 應用。

NIM 是 NVIDIA AI Enterprise 的一部分，旨在簡化 AI 模型的部署和運行，確保其在 NVIDIA GPU 上高效運行。

- 示範：使用 NVIDIA NIM 調用 Phi-3.5-Vision-API [[點擊此連結](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### 在本地運行 Phi-3/3.5
與 Phi-3 或任何語言模型如 GPT-3 相關的推理，指的是根據接收到的輸入生成回應或預測的過程。當你向 Phi-3 提供提示或問題時，它會利用其訓練過的神經網絡通過分析訓練數據中的模式和關係，推斷出最有可能且相關的回應。

**Hugging Face Transformer**
Hugging Face Transformers 是一個功能強大的庫，設計用於自然語言處理（NLP）及其他機器學習任務。以下是它的一些重點：

1. <strong>預訓練模型</strong>：它提供數千個可用於各種任務的預訓練模型，如文本分類、命名實體識別、問答系統、摘要、翻譯和文本生成。

2. <strong>框架互通性</strong>：該庫支援多種深度學習框架，包括 PyTorch、TensorFlow 和 JAX。這讓你可以在一個框架中訓練模型，並在另一個框架中使用它。

3. <strong>多模態能力</strong>：除了 NLP，Hugging Face Transformers 還支援計算機視覺（如圖像分類、物件偵測）和語音處理（如語音識別、音頻分類）任務。

4. <strong>易用性</strong>：該庫提供 API 和工具，方便下載和微調模型，讓初學者和專家都能輕鬆使用。

5. <strong>社群與資源</strong>：Hugging Face 擁有活躍的社群及豐富的文檔、教學和指南，協助用戶快速上手並最大化利用該庫。
[官方文檔](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 或他們的 [GitHub 儲存庫](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)。

這是最常用的方法，但它也需要 GPU 加速。畢竟，如視覺和 MoE 這類場景需要大量計算，如果沒有量化，CPU 運算會非常緩慢。


- 示範：使用 Transformer 調用 Phi-3.5-Instruct [點擊此連結](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 示範：使用 Transformer 調用 Phi-3.5-Vision [點擊此連結](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 示範：使用 Transformer 調用 Phi-3.5-MoE [點擊此連結](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) 是一個旨在讓你更輕鬆在本地機器上運行大型語言模型（LLMs）的平台。它支援多種模型如 Llama 3.1、Phi 3、Mistral 和 Gemma 2 等。該平台通過將模型權重、配置和數據打包成一個單一套件，簡化了過程，讓用戶更容易自定義和創建自己的模型。Ollama 支援 macOS、Linux 和 Windows。如果你想要實驗或部署 LLM 而不依賴雲端服務，它是一個非常好的工具。Ollama 是最直接的方式，你只需執行以下命令。


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 是微軟的離線設備端運行時環境，可讓你完全在自己的硬件上運行例如 Phi 這類模型 — 無需 Azure 訂閱、API 金鑰或網絡連接。它會自動選擇可用的最佳執行提供者（NPU、GPU 或 CPU），並暴露一個與 OpenAI 兼容的端點，讓現有的 `openai`/Azure AI 推理 SDK 程式碼只需少量修改便可使用。詳見 [Foundry Local 文件](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 以開始使用。

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) 是跨平台的機器學習推理與訓練加速器。ONNX Runtime for Generative AI (GENAI) 是一個強大的工具，幫助你在各種平台上高效運行生成式 AI 模型。

## 什麼是 ONNX Runtime？
ONNX Runtime 是一個開源專案，可實現機器學習模型的高效推理。它支援以 Open Neural Network Exchange (ONNX) 格式表示的模型，該格式是表示機器學習模型的標準。ONNX Runtime 推理能提升用戶體驗並降低成本，支援來自深度學習框架如 PyTorch 和 TensorFlow/Keras 以及經典機器學習庫如 scikit-learn、LightGBM、XGBoost 等模型。ONNX Runtime 相容於不同硬件、驅動和作業系統，通過利用硬件加速器和圖優化轉換提供最佳效能。

## 什麼是生成式 AI？
生成式 AI 指的是能根據所訓練數據生成新內容的 AI 系統，如文本、圖片或音樂。例子包括語言模型如 GPT-3 和圖像生成模型如 Stable Diffusion。ONNX Runtime for GenAI 函式庫為 ONNX 模型提供生成式 AI 迴圈，涵蓋使用 ONNX Runtime 推理、對數處理、搜索與採樣及 KV 快取管理。

## ONNX Runtime for GENAI
ONNX Runtime for GENAI 擴展了 ONNX Runtime 的功能以支援生成式 AI 模型。以下是一些主要特色：

- **廣泛平台支援：** 它可在多種平台上運行，包括 Windows、Linux、macOS、Android 和 iOS。
- **模型支援：** 支援許多熱門生成式 AI 模型，如 LLaMA、GPT-Neo、BLOOM 等。
- **效能優化：** 包含針對不同硬體加速器的優化，如 NVIDIA GPU、AMD GPU 等。
- **易用性：** 提供 API 方便整合至應用，讓你可用最少程式碼生成文本、圖片及其他內容。
- 使用者可以調用高階的 generate() 方法，或在迴圈中逐次運行模型，每次生成一個詞元，並可選擇性地在迴圈內更新生成參數。
- ONNX runtime 亦支援貪婪/波束搜索及 TopP、TopK 採樣來生成詞元序列，並內建對數處理如重複懲罰。你也可以輕鬆添加自訂評分。

## 入門指南
若要開始使用 ONNX Runtime for GENAI，可以按照以下步驟：

### 安裝 ONNX Runtime：
```Python
pip install onnxruntime
```
### 安裝生成式 AI 擴充：
```Python
pip install onnxruntime-genai
```

### 運行模型：以下是一個簡單的 Python 範例：
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
### 示範：使用 ONNX Runtime GenAI 調用 Phi-3.5-Vision


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

除了 ONNX Runtime、Ollama 和 Foundry Local 參考方法外，我們也可根據不同廠商提供的模型參考方法，完成量化模型的參考。例如搭配 Apple Metal 的 Apple MLX 框架、搭配 NPU 的 Qualcomm QNN、搭配 CPU/GPU 的 Intel OpenVINO 等。你也可以從 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) 獲取更多內容。


## 更多

我們已學習了 Phi-3/3.5 系列的基礎，但要進一步了解 SLM，我們需要更多知識。你可以在 Phi-3 Cookbook 中找到答案。若想深入學習，請參閱 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->