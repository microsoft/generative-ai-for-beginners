# 為初學者介紹生成式 AI 的小型語言模型
生成式 AI 是人工智慧中一個迷人的領域，專注於創造能夠生成新內容的系統。這些內容可以涵蓋從文字、圖片到音樂，甚至是整個虛擬環境。生成式 AI 最令人興奮的應用之一，就是語言模型的領域。

## 什麼是小型語言模型？

小型語言模型（SLM）代表著大型語言模型（LLM）的縮減版本，利用了許多大型語言模型的架構原理和技術，但計算資源使用顯著降低。

SLM 是設計用來生成類似人類文字的語言模型子集。與 GPT-4 等較大型模型不同，SLM 較為精簡和高效，適用於計算資源有限的應用。儘管規模較小，它們仍能執行多種任務。通常，SLM 是透過壓縮或蒸餾大型語言模型構建，目標是保留原模型功能和語言能力的大部分。模型規模的縮減減少了整體複雜度，使 SLM 在記憶體使用和計算需求上更有效率。即使經過此類優化，SLM 仍能執行廣泛的自然語言處理（NLP）任務：

- 文字生成：創建連貫且語境相關的句子或段落。
- 文字補全：基於給定提示預測和完成句子。
- 翻譯：將文字從一種語言轉換到另一種語言。
- 摘要：將冗長的文字凝練成較短易懂的摘要。

儘管在性能或理解深度上與大型模型相比有所權衡。

## 小型語言模型如何運作？
SLM 在大量文本數據上進行訓練。訓練過程中，它們學習語言的模式和結構，使其能夠生成語法正確且語境恰當的文字。訓練過程包含：

- 數據收集：從各種來源收集大量文本資料。
- 預處理：清理並整理資料，使其適合訓練。
- 訓練：利用機器學習算法教導模型如何理解和生成文字。
- 微調：調整模型以提升其在特定任務上的表現。

SLM 的發展符合在資源有限環境（如行動裝置或邊緣運算平台）部署模型的需求，這類環境中，由於資源使用大，完整大型語言模型通常不切實際。透過強調效率，SLM 平衡了性能與可用性，使其能在各種領域中更廣泛地應用。

![slm](../../../translated_images/zh-TW/slm.4058842744d0444a.webp)

## 學習目標

本課程希望介紹 SLM 的相關知識，並結合 Microsoft Phi-3，學習不同場景下的文字內容、視覺和 MoE 應用。

課程結束時，您應能回答以下問題：

- 什麼是 SLM？
- SLM 與 LLM 有何不同？
- 什麼是 Microsoft Phi-3/3.5 系列？
- 如何使用 Microsoft Phi-3/3.5 系列進行推論？

準備好了嗎？讓我們開始吧。

## 大型語言模型 (LLM) 與小型語言模型 (SLM) 的差異

LLM 與 SLM 都建立在機率機器學習的基礎原理上，其架構設計、訓練方法、數據生成流程和模型評估技術皆相似。然而，兩種模型間存在幾個關鍵差異。

## 小型語言模型的應用

SLM 的應用範圍廣泛，包括：

- 聊天機器人：提供客戶支援並與用戶進行對話互動。
- 內容創作：協助作家生成創意或草擬整篇文章。
- 教育：幫助學生完成寫作作業或學習新語言。
- 無障礙輔助：製作為身障者提供幫助的工具，如文字轉語音系統。

<strong>規模大小</strong>
  
LLM 與 SLM 的主要區別之一在於模型規模。像 ChatGPT (GPT-4) 的 LLM 可包含約 1.76 兆參數，而如 Mistral 7B 等開源 SLM 則設計為大約 70 億參數。差距主因在於模型架構與訓練過程差異。例如，ChatGPT 採用編碼器-解碼器架構中的自注意力機制，而 Mistral 7B 則採用滑動視窗注意力，能在僅解碼器模型中實現更高效的訓練。此架構差異對模型的複雜度與性能影響甚鉅。

<strong>理解能力</strong>

SLM 通常針對特定領域優化，因此高度專精，但對多領域知識的廣泛語境理解能力可能有限。而 LLM 旨在模擬更全面的人類般智能。LLM 在大量多樣數據集上訓練，能在多個領域表現良好，具更高的多功能性和適應性，因此更適合用於廣泛的下游任務，如自然語言處理和程序設計。

<strong>計算需求</strong>

LLM 的訓練和部署過程資源密集，通常需要龐大的計算架構，如大型 GPU 叢集。舉例而言，從零開始訓練像 ChatGPT 這樣的模型，可能需要數千 GPU 長時間運算。相比之下，參數較少的 SLM 在計算資源需求上更親民。例如 Mistral 7B 可在配備中等 GPU 運算能力的本地機器上訓練和執行，儘管訓練仍需數小時並使用多 GPU。

<strong>偏見問題</strong>

偏見是 LLM 的已知問題，主要源於訓練資料的性質。這些模型大量仰賴來自網路的原始公開數據，其中可能對某些群體呈現不足、誤導性標注或反映方言、地理變異及語法規則影響下的語言偏見。此外，LLM 複雜架構也可能無意中加劇偏見且不易被察覺，需透過細心微調加以修正。相較之下，SLM 基於更受限制、領域特定的數據集訓練，天生較不易受此類偏見影響，但並非完全免疫。

<strong>推論速度</strong>

較小的 SLM 在推論速度上具顯著優勢，允許其在本地硬體上高效地產生輸出，無需大量並行計算。而 LLM 由於規模和複雜度，通常須仰賴大量並行計算資源才能達到可接受的推論時間。在多名用戶同時使用的狀況下，LLM 的回應速度會進一步變慢，尤其是在大規模部署時。

總結來說，雖然 LLM 和 SLM 共基於機器學習的基礎，但在模型規模、資源需求、語境理解能力、偏見敏感度和推論速度等方面有顯著差異。這些差異反映兩者在不同使用場景上的適用性：LLM 功能多元但資源消耗大；SLM 則提供更符合特定領域需求的效能和較低計算負擔。

***注意：本課程將以 Microsoft Phi-3 / 3.5 作為介紹 SLM 的範例。***

## 介紹 Phi-3 / Phi-3.5 系列

Phi-3 / 3.5 系列主要針對文字、視覺及智能代理（MoE）應用場景：

### Phi-3 / 3.5 指令型

主要用於文字生成、聊天補全及內容資訊抽取等。

**Phi-3-mini**

3.8B 參數的語言模型可在 Microsoft Foundry、Hugging Face 和 Ollama 上取得。Phi-3 模型在核心基準測試中大幅超越同等或更大規模的語言模型（見下方基準數據，數字越高越好）。Phi-3-mini 的表現超越了兩倍規模的模型，Phi-3-small 和 Phi-3-medium 則勝過包括 GPT-3.5 在內的更大型模型。

**Phi-3-small 與 medium**

Phi-3-small 僅有 7B 參數，在多種語言、推理、程式碼和數學基準上打敗 GPT-3.5T。

擁有 14B 參數的 Phi-3-medium 延續此趨勢，表現超越 Gemini 1.0 Pro。

**Phi-3.5-mini**

可視為 Phi-3-mini 的升級版。雖然參數未變，但提升了多語言支持（支持 20 多種語言：阿拉伯語、中文、捷克語、丹麥語、荷蘭語、英語、芬蘭語、法語、德語、希伯來語、匈牙利語、義大利語、日語、韓語、挪威語、波蘭語、葡萄牙語、俄語、西班牙語、瑞典語、泰語、土耳其語、烏克蘭語）並增強了長上下文支持能力。

3.8B 參數的 Phi-3.5-mini 表現優於同等規模語言模型，且能與兩倍規模模型媲美。

### Phi-3 / 3.5 視覺

我們可以將 Phi-3/3.5 的指令型模型視為 Phi 的理解能力，而 Vision 則讓 Phi 有「眼睛」來理解世界。


**Phi-3-Vision**

僅有 4.2B 參數的 Phi-3-vision 持續此趨勢，其在普通視覺推理任務、OCR，以及表格與圖表理解任務中，表現優於 Claude-3 Haiku 和 Gemini 1.0 Pro 等較大型模型。


**Phi-3.5-Vision**

Phi-3.5-Vision 是 Phi-3-Vision 的升級版，新增支持多張圖像。你可以把它視為視覺能力的提升，不只可以看圖片，也能理解影片。

Phi-3.5-vision 在 OCR、表格與圖表理解任務中，表現優於 Claude-3.5 Sonnet 和 Gemini 1.5 Flash 等較大型模型，在一般視覺知識推理任務上不相上下。支持多幀輸入，對多張輸入圖像進行推理。


### Phi-3.5-MoE

***專家混合模型（Mixture of Experts，MoE）*** 使模型在訓練階段所需計算量大幅減少，意即可在相同計算預算下，顯著擴大模型或數據集規模。具體而言，MoE 模型應能比其密集模型（dense model）對應版本更快達成同等品質的預訓練效果。

Phi-3.5-MoE 由 16 個 3.8B 參數的專家模組組成。Phi-3.5-MoE 活躍參數僅 6.6B，卻能達到與更大型模型類似的推理、語言理解和數學能力。

我們可根據不同場景使用 Phi-3/3.5 系列模型。與 LLM 不同，Phi-3/3.5-mini 或 Phi-3/3.5-Vision 可部署於邊緣設備。


## 如何使用 Phi-3/3.5 系列模型

我們希望在不同應用場景使用 Phi-3/3.5。接下來將展示基於不同場景的 Phi-3/3.5 應用。

![phi3](../../../translated_images/zh-TW/phi3.655208c3186ae381.webp)

### 透過雲端 API 進行推論

**Microsoft Foundry 模型**

> **注意:** GitHub Models 將於 2026 年 7 月底退役。[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 是其直接替代方案。

Microsoft Foundry Models 是最直接的使用方式。您可以透過 Foundry 模型目錄快速存取 Phi-3/3.5-Instruct 模型。結合 Azure AI 推論 SDK / OpenAI SDK，您可以透過程式碼調用 API，完成 Phi-3/3.5-Instruct 的調用。也可透過 Playground 測試不同效果。

- 示範：Phi-3-mini 與 Phi-3.5-mini 在中文場景下的效果比較

![phi3](../../../translated_images/zh-TW/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/zh-TW/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

如果想使用視覺或 MoE 模型，也可以透過 Microsoft Foundry 完成調用。若有興趣，可閱讀 Phi-3 食譜，了解如何透過 Microsoft Foundry 調用 Phi-3/3.5 的 Instruct、Vision、MoE 模型 [點此連結](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

除了基於雲端的 Microsoft Foundry 模型目錄，您也可以使用 [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) 完成相關調用。您可訪問 NVIDIA NIM 以完成 Phi-3/3.5 系列的 API 調用。NVIDIA NIM（NVIDIA 推論微服務）是一套加速推論微服務，旨在幫助開發者高效部署 AI 模型於雲端、數據中心及工作站等多種環境。

以下是 NVIDIA NIM 的一些主要特點：

- **部署簡便：** NIM 只需一條命令即可部署 AI 模型，方便整合現有工作流程。

- **優化效能：** 它利用 NVIDIA 預先優化的推論引擎，如 TensorRT 和 TensorRT-LLM，以確保低延遲和高吞吐量。
- **可擴展性：** NIM 支援 Kubernetes 上的自動擴展，使其能有效處理不同工作負載。
- **安全與控制：** 組織可透過在自有管理基礎設施上自我託管 NIM 微服務，來維持對其數據和應用程式的控制權。
- **標準 API：** NIM 提供業界標準 API，使構建和整合聊天機器人、AI 助理及其他 AI 應用變得簡單。

NIM 是 NVIDIA AI Enterprise 的一部分，旨在簡化 AI 模型的部署與運營，確保它們在 NVIDIA GPU 上高效執行。

- 範例：使用 NVIDIA NIM 調用 Phi-3.5-Vision-API  [[點擊此連結](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### 本地運行 Phi-3/3.5
Phi-3 或任何語言模型如 GPT-3 的推論，指的是根據接收到的輸入生成回應或預測的過程。在您提供提示或問題給 Phi-3 時，它使用其訓練好的神經網路，通過分析訓練資料中的模式及關聯，推斷最可能且相關的回應。

**Hugging Face Transformer**
Hugging Face Transformers 是一個強大的庫，專為自然語言處理（NLP）及其他機器學習任務設計。以下是主要特點：

1. <strong>預訓練模型</strong>：提供數千個預訓練模型，可用於文本分類、命名實體識別、問答、摘要、翻譯和文本生成等多種任務。

2. <strong>框架互操作性</strong>：該庫支援多個深度學習框架，包括 PyTorch、TensorFlow 與 JAX。這使您能在一個框架中訓練模型，並在另一個框架中使用。

3. <strong>多模態能力</strong>：除了 NLP，Hugging Face Transformers 還支援電腦視覺任務（如圖像分類、目標檢測）和音訊處理（如語音識別、音訊分類）。

4. <strong>易用性</strong>：該庫提供 API 和工具，輕鬆下載和微調模型，讓初學者和專家都能輕鬆使用。

5. <strong>社群與資源</strong>：Hugging Face 擁有活躍的社群及豐富的文件、教學和指南，幫助使用者快速上手並充分利用該庫。
[官方文件](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 或其 [GitHub 倉庫](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)。

這是最常用的方法，但它同時需要 GPU 加速。畢竟像 Vision 和 MoE 這種場景需進行大量計算，若無量化，在 CPU 上會非常緩慢。


- 範例：使用 Transformer 調用 Phi-3.5-Instruct [點擊此連結](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 範例：使用 Transformer 調用 Phi-3.5-Vision [點擊此連結](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 範例：使用 Transformer 調用 Phi-3.5-MoE [點擊此連結](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) 是一個平台，旨在讓您更容易在本機運行大型語言模型（LLM）。它支援多種模型，如 Llama 3.1、Phi 3、Mistral 和 Gemma 2 等。該平台將模型權重、配置及數據打包成單一套件，簡化流程，使使用者更易自訂並建立自己的模型。Ollama 支援 macOS、Linux 和 Windows，是一款若想實驗或部署 LLM 但不依賴雲端服務的絕佳工具。Ollama 是最直接的方式，您只需執行以下指令。


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 是微軟的離線、裝置內執行環境，讓您能完全在自有硬體上運行像 Phi 這樣的模型——無需 Azure 訂閱、API 金鑰或網路連接。它會自動挑選最佳執行供應者（NPU、GPU 或 CPU），並提供兼容 OpenAI 的端點，讓現有的 `openai`/Azure AI 推論 SDK 程式碼幾乎無需修改即可指向它。請參閱 [Foundry Local 文件](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 以開始使用。

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) 是一個跨平台的推論和訓練機器學習加速器。ONNX Runtime for Generative AI (GENAI) 是一個強大工具，幫助您在多種平台上高效運行生成式 AI 模型。

## 什麼是 ONNX Runtime？
ONNX Runtime 是一個開源專案，可實現機器學習模型的高效推論。它支援 Open Neural Network Exchange (ONNX) 格式的模型，該格式是機器學習模型的標準。ONNX Runtime 的推論可促進更快的用戶體驗與降低成本，支援來自深度學習框架如 PyTorch 與 TensorFlow/Keras，以及傳統機器學習庫如 scikit-learn、LightGBM、XGBoost 等的模型。ONNX Runtime 相容於不同硬體、驅動及作業系統，並透過硬體加速器、圖形優化與轉換，提供最佳效能。

## 什麼是生成式 AI？
生成式 AI 指能根據訓練數據生成新內容（如文本、圖像或音樂）的 AI 系統。如 GPT-3 之類的語言模型和 Stable Diffusion 這類的圖像生成模型即為例子。ONNX Runtime for GenAI 庫為 ONNX 模型提供生成式 AI 迴圈，包括使用 ONNX Runtime 推論、logits 處理、搜尋與抽樣，以及 KV 快取管理。

## ONNX Runtime for GENAI
ONNX Runtime for GENAI 擴展了 ONNX Runtime 的功能，使其支援生成式 AI 模型。以下是其主要特點：

- **廣泛的平臺支援：** 它支援 Windows、Linux、macOS、Android 和 iOS 等多種平台。
- **模型支持：** 支援多種流行生成式 AI 模型，如 LLaMA、GPT-Neo、BLOOM 等。
- **效能優化：** 包含針對不同硬體加速器的優化，如 NVIDIA GPU、AMD GPU 等。
- **易用性：** 提供 API，便於應用整合，允許您以最少代碼生成文本、圖像及其他內容。
- 使用者可呼叫高階的 generate() 方法，或遍歷模型迴圈，每次生成一個標記，並可選擇在迴圈中更新生成參數。
- ONNX Runtime 亦支援貪婪搜尋、束搜尋及 TopP、TopK 抽樣以生成標記序列，並內建類似重複懲罰的 logits 處理。您也可以輕鬆新增自訂評分。

## 入門指引
若要開始使用 ONNX Runtime for GENAI，您可以遵循以下步驟：

### 安裝 ONNX Runtime：
```Python
pip install onnxruntime
```
### 安裝生成式 AI 擴充套件：
```Python
pip install onnxruntime-genai
```

### 執行模型：此為 Python 簡單範例：
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
### 範例：使用 ONNX Runtime GenAI 調用 Phi-3.5-Vision


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

除了 ONNX Runtime、Ollama 與 Foundry Local 參考方法外，我們也可以基於不同廠商提供的模型參考方法完成量化模型參考，例如 Apple 的 MLX 框架搭配 Apple Metal、Qualcomm QNN 搭配 NPU、Intel OpenVINO 搭配 CPU/GPU 等。您也可以從 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) 獲取更多內容。


## 更多

我們已學習 Phi-3/3.5 系列的基礎知識，但若要深入了解 SLM，則需要更多相關知識。您可在 Phi-3 Cookbook 中找到答案。如想了解更多，請訪問 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->