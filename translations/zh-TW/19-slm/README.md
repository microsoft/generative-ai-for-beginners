# 生成式 AI 初學者小型語言模型介紹
生成式 AI 是人工智慧的一個迷人領域，專注於創建能夠生成新內容的系統。這些內容可以涵蓋文字、圖像、音樂甚至整個虛擬環境。生成式 AI 最令人興奮的應用之一是語言模型領域。

## 什麼是小型語言模型？

小型語言模型（SLM）是大型語言模型（LLM）的縮減版本，利用了許多 LLM 的架構原則和技術，但計算資源需求顯著降低。

SLM 是設計用來生成類似人類文本的語言模型子集。與像 GPT-4 這樣的大型模型不同，SLM 更加小巧且高效，非常適合計算資源有限的應用場景。儘管體積較小，SLM 仍能執行多種任務。通常，SLM 是透過壓縮或蒸餾 LLM 建構的，旨在保留原始模型的大部分功能和語言能力。模型大小的減少降低了整體複雜性，使 SLM 在記憶體使用和計算需求上更有效率。儘管進行了這些優化，SLM 仍能完成廣泛的自然語言處理（NLP）任務：

- 文字生成：創建連貫且符合語境的句子或段落。
- 文字補全：根據給定提示預測並完成句子。
- 翻譯：將文字從一種語言轉換成另一種語言。
- 摘要：將冗長文本濃縮成較短、易於理解的摘要。

雖然在效能或理解深度上與大型模型相比可能有些權衡。

## 小型語言模型如何運作？
SLM 在大量文本資料上進行訓練。訓練期間，它們學習語言的模式和結構，使其能夠生成既文法正確又符合語境的文本。訓練過程包含：

- 資料收集：從各種來源收集大量文本數據。
- 預處理：清理並組織數據，使其適合訓練。
- 訓練：使用機器學習演算法教模型理解並生成文字。
- 微調：調整模型以提升其在特定任務的表現。

SLM 的發展符合對能在資源受限環境（如行動裝置或邊緣運算平台）中部署的模型日益增長的需求，因為在這些環境中，完整的 LLM 可能因資源消耗過大而不切實際。SLM 著眼於效率，在性能與可及性之間取得平衡，使其能在各領域廣泛應用。

![slm](../../../translated_images/zh-TW/slm.4058842744d0444a.webp)

## 學習目標

在本課程中，我們希望介紹 SLM 的知識，並結合 Microsoft Phi-3 學習文字內容、視覺和 MoE 的不同場景。

本課程結束時，您應能回答以下問題：

- 什麼是 SLM？
- SLM 與 LLM 有何不同？
- 什麼是 Microsoft Phi-3/3.5 系列？
- 如何使用 Microsoft Phi-3/3.5 系列進行推理？

準備好了嗎？讓我們開始吧。

## 大型語言模型（LLM）與小型語言模型（SLM）的區別

LLM 和 SLM 均基於機率機器學習的基礎原理，架構設計、訓練方法、數據生成過程和模型評估技術大致相似，然而有幾個關鍵因素將這兩類模型區隔開來。

## 小型語言模型的應用

SLM 有廣泛的應用，包括：

- 聊天機器人：提供客戶支援，與用戶進行對話互動。
- 內容創作：協助作家生成點子，甚至草擬整篇文章。
- 教育：幫助學生完成寫作作業或學習新語言。
- 無障礙：為有障礙人士創造工具，如文字轉語音系統。

<strong>規模</strong>
  
LLM 與 SLM 的主要區別在於模型規模。LLM，如 ChatGPT（GPT-4），參數估計約達 1.76 兆，而開源 SLM 如 Mistral 7B 約有 70 億參數。這種差異主要源於模型架構和訓練過程的不同。例如，ChatGPT 採用帶有自注意力機制的編碼器-解碼器框架，而 Mistral 7B 使用滑動窗口注意力，令解碼器模型的訓練更高效。此架構差異對模型的複雜度與性能有深遠影響。

<strong>理解力</strong>

SLM 通常優化於特定領域的效能，使其高度專門化，但在提供跨領域廣泛語境理解方面可能受限。相比之下，LLM 旨在模擬更全面的人類智慧，經過大量多樣化資料集訓練，設計能在各種領域表現良好，具備更大多樣性與適應性。因此，LLM 更適合用於自然語言處理和程式編寫等各類下游任務。

<strong>運算資源</strong>

LLM 的訓練與部署需耗費大量資源，通常需要大型 GPU 叢集。例如，從零開始訓練 ChatGPT 可能需數千 GPU 並持續長時間。相比之下，SLM 由於參數量較少，對運算資源的要求較低。像 Mistral 7B 這種模型可以在配備中等 GPU 的本地機器上訓練和運行，但訓練仍需數小時且使用多張 GPU。

<strong>偏見</strong>

偏見是 LLM 的已知問題，主要由訓練資料性質引起。這些模型多依賴來自網路的原始公開數據，可能對某些群體代表性不足或誤導，導致標籤錯誤，或反映方言、地理變異及文法規則等語言偏見。此外，LLM 結構的複雜性可能無意中加劇偏見，若缺乏細心微調可能不易察覺。另一方面，SLM 通常在較有限且特定領域的數據集上訓練，因此較不易受到此類偏見影響，但仍非完全免疫。

<strong>推理速度</strong>

SLM 體積較小，在推理速度上具顯著優勢，能在本地硬體上高效產出結果，無須大量平行計算。相較之下，LLM 由於規模與複雜度高，通常需大量並行運算資源才能達到可接受的推理時間。多用戶並行使用時，LLM 的反應速度尤其在大規模部署時會顯著放慢。

總結而言，雖然 LLM 與 SLM 基於相同的機器學習基礎，但在模型大小、資源需求、語境理解能力、偏見敏感度及推理速度等方面存在重大差異。這些差異反映出兩者適用的場景不同，LLM 多功能但資源消耗大，SLM 則在特定領域內效率更高且計算需求較少。

***注意：本課程將以 Microsoft Phi-3 / 3.5 為例介紹 SLM。***

## Phi-3 / Phi-3.5 系列介紹

Phi-3 / 3.5 系列主要針對文字、視覺及 Agent（MoE）應用場景：

### Phi-3 / 3.5 Instruct

主要用於文字生成、對話補全及內容資訊提取等。

**Phi-3-mini**

3.8B 參數語言模型可在 Microsoft Foundry、Hugging Face 與 Ollama 上取得。Phi-3 模型在主要基准測試上大幅超越同尺寸及更大規模的語言模型（請參考下方基準分數，數值越高越好）。Phi-3-mini 表現優於體積為其兩倍的模型，Phi-3-small 和 Phi-3-medium 甚至超越包括 GPT-3.5 在內的更大模型。

**Phi-3-small 與 medium**

Phi-3-small 只有 7B 參數，在語言、推理、編碼與數學基準上勝過 GPT-3.5T。

而 14B 參數的 Phi-3-medium 延續這一趨勢，表現優於 Gemini 1.0 Pro。

**Phi-3.5-mini**

可視為 Phi-3-mini 的升級版。參數不變，但提升了多語言支持能力（支援 20 多種語言：阿拉伯語、中文、捷克語、丹麥語、荷蘭語、英語、芬蘭語、法語、德語、希伯來語、匈牙利語、義大利語、日語、韓語、挪威語、波蘭語、葡萄牙語、俄語、西班牙語、瑞典語、泰語、土耳其語、烏克蘭語）並強化長上下文支持。

3.8B 參數的 Phi-3.5-mini 超越同規模語言模型，並達到體積為其兩倍模型的水準。

### Phi-3 / 3.5 視覺

可將 Phi-3/3.5 的 Instruct 模型視為 Phi 的理解能力，而 Vision 則是賦予 Phi「眼睛」以理解世界。


**Phi-3-Vision**

Phi-3-Vision 僅 4.2B 參數，持續延續此趨勢，於通用視覺推理、OCR 及表格和圖表理解任務中表現超越更大模型如 Claude-3 Haiku 與 Gemini 1.0 Pro V。


**Phi-3.5-Vision**

Phi-3.5-Vision 是 Phi-3-Vision 的升級版，新增多圖像支持。可視為視覺能力的提升，除了看圖片，還能理解影片。

Phi-3.5-Vision 在 OCR、表格及圖表理解任務中，表現超越更大模型如 Claude-3.5 Sonnet 與 Gemini 1.5 Flash，在通用視覺知識推理任務中表現相當。支持多畫面輸入，即可對多張圖像進行推理。


### Phi-3.5-MoE

***MoE（專家混合模型）*** 讓模型在更低計算量下完成預訓練，意味著能使用與密集模型相同的計算資源大幅擴展模型或資料集規模。尤其是，MoE 模型在預訓練期間能更快達到與密集模型同等質量水平。

Phi-3.5-MoE 包含 16 個 3.8B 參數的專家模組。Phi-3.5-MoE 活躍參數僅 6.6B，卻在推理、語言理解與數學能力上達到大幅更大模型的水平。

我們可以根據不同場景使用 Phi-3/3.5 系列模型。與 LLM 不同，您可以在邊緣設備上部署 Phi-3/3.5-mini 或 Phi-3/3.5-Vision。


## 如何使用 Phi-3/3.5 系列模型

我們期望在不同場景中使用 Phi-3/3.5 系列。接下來將根據不同場景介紹如何使用 Phi-3/3.5。

![phi3](../../../translated_images/zh-TW/phi3.655208c3186ae381.webp)

### 透過雲端 API 進行推理

**Microsoft Foundry 模型**

> **注意：** GitHub Models 將於 2026 年 7 月底退役。[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 是直接替代方案。

Microsoft Foundry 模型是最直接的方式。您可以透過 Foundry 模型目錄快速取得 Phi-3/3.5-Instruct 模型。結合 Azure AI 推理 SDK / OpenAI SDK，您可以透過程式碼調用 API 完成 Phi-3/3.5-Instruct 呼叫，也可透過 Playground 測試不同效果。

- 示範：Phi-3-mini 與 Phi-3.5-mini 在中文場景下的效果比較

![phi3](../../../translated_images/zh-TW/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/zh-TW/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

若您想使用視覺與 MoE 模型，也可使用 Microsoft Foundry 完成呼叫。若有興趣，可閱讀 Phi-3 Cookbook，了解如何透過 Microsoft Foundry 呼叫 Phi-3/3.5 Instruct、Vision、MoE [點此連結](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

除了雲端 Microsoft Foundry 模型目錄外，您也可以使用 [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) 完成相關呼叫。您可以訪問 NVIDIA NIM 以完成 Phi-3/3.5 系列的 API 呼叫。NVIDIA NIM（NVIDIA 推理微服務）是一套加速推理微服務，幫助開發者高效部署 AI 模型至多種環境，包括雲端、資料中心和工作站。

這裡是 NVIDIA NIM 的一些主要特點：

- **部署簡易性：** NIM 允許以一條命令部署 AI 模型，方便整合至現有工作流程。

- **優化效能：** 它利用 NVIDIA 預先優化的推理引擎，如 TensorRT 和 TensorRT-LLM，以確保低延遲和高吞吐量。
- **可擴展性：** NIM 支援 Kubernetes 自動擴展，使其能有效處理不同負載。
- **安全與控制：** 組織可以通過在自有管理的基礎設施上自行部署 NIM 微服務，來維持對其資料和應用的控制。
- **標準 API：** NIM 提供產業標準的 API，使構建和整合聊天機器人、AI 助理等 AI 應用變得容易。

NIM 是 NVIDIA AI Enterprise 的一部分，旨在簡化 AI 模型的部署與運維，確保它們能在 NVIDIA GPU 上高效運行。

- 範例演示：使用 NVIDIA NIM 呼叫 Phi-3.5-Vision-API [[點此連結](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### 本地執行 Phi-3/3.5
關於 Phi-3 或任何像 GPT-3 的語言模型的推理，是指根據模型接收到的輸入生成回應或預測的過程。當你向 Phi-3 提供提示或問題時，它會利用其訓練好的神經網路，通過分析其訓練數據中的模式和關聯，推斷出最可能且相關的回應。

**Hugging Face Transformer**
Hugging Face Transformers 是一個強大的庫，專為自然語言處理（NLP）及其他機器學習任務設計。以下是一些重點：

1. <strong>預訓練模型</strong>：它提供數千個可用於文本分類、命名實體識別、問答、摘要、翻譯和文本生成等多種任務的預訓練模型。

2. <strong>框架互操作性</strong>：該庫支援多個深度學習框架，包括 PyTorch、TensorFlow 和 JAX，允許你在一種框架中訓練模型，並在另一種框架中使用它。

3. <strong>多模態能力</strong>：除了 NLP，Hugging Face Transformers 還支援計算機視覺（如影像分類、目標檢測）和音訊處理（如語音識別、音訊分類）任務。

4. <strong>易用性</strong>：該庫提供 API 和工具，方便下載和微調模型，讓初學者和專家皆能輕鬆使用。

5. <strong>社群與資源</strong>：Hugging Face 擁有活躍的社群和豐富的文件、教學與指南，幫助使用者快速上手並充分利用庫的功能。
[官方文件](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 或其 [GitHub 儲存庫](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)。

這是最常用的方法，但同時也需要 GPU 加速。畢竟，像視覺和 Mixture of Experts（MoE）等場景需要大量計算，若未量化，在 CPU 上會非常緩慢。


- 範例演示：使用 Transformer 呼叫 Phi-3.5-Instruct [點此連結](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 範例演示：使用 Transformer 呼叫 Phi-3.5-Vision [點此連結](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 範例演示：使用 Transformer 呼叫 Phi-3.5-MoE [點此連結](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) 是一個讓你能更方便在本機運行大型語言模型（LLM）的平台。它支援多種模型，如 Llama 3.1、Phi 3、Mistral 及 Gemma 2 等。該平台將模型權重、配置及資料打包成單一套件，簡化使用者定制和建立自己模型的流程。Ollama 支援 macOS、Linux 和 Windows。如果你想嘗試或部署 LLM 而不依賴雲端服務，這是個很棒的工具。Ollama 是最直接的方式，你只需要執行以下指令。


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 是微軟的離線本地裝置執行環境，可在你自己的硬體上完全運行像 Phi 這樣的模型——無需 Azure 訂閱、API 金鑰或網路連線。它會自動選擇最佳的執行提供者（NPU、GPU 或 CPU），並提供相容 OpenAI 的端點，使現有的 `openai`/Azure AI Inference SDK 程式碼只需少量修改即可指向該端點。請參閱 [Foundry Local 文件](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 開始使用。

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) 是一個跨平台的推理與訓練機器學習加速器。ONNX Runtime for Generative AI (GENAI) 是一個強大的工具，幫助你高效運行各種平台上的生成式 AI 模型。

## 什麼是 ONNX Runtime？
ONNX Runtime 是一個開源專案，用於高效推理機器學習模型。它支援 Open Neural Network Exchange (ONNX) 格式，這是表達機器學習模型的標準。ONNX Runtime 推理能提升用戶體驗並降低成本，支援包括 PyTorch、TensorFlow/Keras 等深度學習框架的模型，也支援像 scikit-learn、LightGBM、XGBoost 等經典機器學習庫。ONNX Runtime 相容於不同硬體、驅動和作業系統，並結合硬體加速器、圖優化與轉換提供最佳效能。

## 什麼是生成式 AI？
生成式 AI 指的是能基於訓練資料創造新內容的 AI 系統，如文字、影像或音樂。例子包括 GPT-3 這樣的語言模型，以及 Stable Diffusion 這樣的影像生成模型。ONNX Runtime for GenAI 提供了生成式 AI 的循環支援，包括使用 ONNX Runtime 推理、logits 處理、搜索與採樣，以及 KV 快取管理。

## ONNX Runtime for GENAI
ONNX Runtime for GENAI 拓展了 ONNX Runtime 的功能，以支援生成式 AI 模型。以下是一些關鍵特性：

- **廣泛平臺支援：** 支援 Windows、Linux、macOS、Android 和 iOS 等多種平臺。
- **模型支援：** 支援多種熱門生成式 AI 模型，如 LLaMA、GPT-Neo、BLOOM 等等。
- **效能優化：** 包括針對 NVIDIA GPU、AMD GPU 等各類硬體加速器的優化。
- **易於使用：** 提供 API 方便應用整合，讓你以最少程式碼生成文字、圖片等內容。
- 使用者可以呼叫高階的 generate() 方法，或在迴圈中逐步執行模型生成每個詞元，並可選擇在迴圈中更新生成參數。
- ONNX Runtime 也支援貪婪搜尋、束搜索、TopP 和 TopK 採樣以生成詞元序列，並內建類似重複懲罰的 logits 處理。你也可以輕鬆新增自訂評分。

## 快速開始
若要開始使用 ONNX Runtime for GENAI，可以依照以下步驟：

### 安裝 ONNX Runtime：
```Python
pip install onnxruntime
```
### 安裝生成式 AI 擴充套件：
```Python
pip install onnxruntime-genai
```

### 運行模型：以下是 Python 的簡單示例：
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
### 範例演示：使用 ONNX Runtime GenAI 呼叫 Phi-3.5-Vision


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


<strong>其他方法</strong>

除了 ONNX Runtime、Ollama 和 Foundry Local 等參考方法外，我們也能根據不同廠商提供的模型參考方式完成量化模型的參考，如 Apple MLX 框架搭配 Apple Metal、Qualcomm QNN 搭配 NPU、Intel OpenVINO 搭配 CPU/GPU 等。你也能從 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) 獲得更多內容。


## 更多資訊

我們已經了解了 Phi-3/3.5 家族的基礎，但若要深入學習 SLM 需要更多知識。你可以在 Phi-3 Cookbook 找到答案。如想了解更多，請訪問 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->