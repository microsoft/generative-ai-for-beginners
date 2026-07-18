# 新手入門：生成式 AI 的小型語言模型簡介
生成式 AI 是人工智能中的一個迷人領域，專注於創建能夠生成新內容的系統。這些內容可以從文字、圖片到音樂，甚至整個虛擬環境。生成式 AI 最令人興奮的應用之一是在語言模型領域。

## 什麼是小型語言模型？

小型語言模型（SLM）代表大語言模型（LLM）的縮小版本，採用許多 LLM 的架構原理和技術，同時大幅降低計算資源需求。

SLM 是設計用來生成類似人類文本的語言模型子集。與其較大的對應模型如 GPT-4 不同，SLM 更小巧且高效，非常適合計算資源有限的應用。儘管模型規模較小，它們仍能執行多種任務。典型的 SLM 是通過對 LLM 進行壓縮或蒸餾建構，旨在保留原始模型的大部分功能和語言能力。模型尺寸的縮小降低了整體複雜度，令 SLM 在記憶體使用和計算需求上更有效率。儘管如此，SLM 仍能執行各種自然語言處理（NLP）任務：

- 文字生成：創建連貫且具語境相關性的句子或段落。
- 文字補全：根據提示預測並完成句子。
- 翻譯：將文本從一種語言轉換到另一種語言。
- 摘要：將長篇文本濃縮成較短且易理解的摘要。

雖然在性能或理解深度上，與大型模型相比有所取捨。

## 小型語言模型如何運作？
SLM 通過大量文本數據進行訓練。在訓練過程中，它們學習語言的模式和結構，使其生成的文本既文法正確又符合語境適宜。訓練流程包括：

- 數據收集：從各種來源收集大量文本數據。
- 預處理：清洗和組織數據，使其適合訓練使用。
- 訓練：利用機器學習算法教模型理解並生成文本。
- 微調：調整模型以提升特定任務的表現。

SLM 的發展契合了在資源受限環境部署模型的需求，例如行動裝置或邊緣計算平台，因為大型 LLM 由於其龐大資源需求可能不切實際。透過集中於效率，SLM 在性能與可及性之間取得平衡，使其能夠廣泛應用於各個領域。

![slm](../../../translated_images/zh-HK/slm.4058842744d0444a.webp)

## 學習目標

本課程希望介紹 SLM 的知識，並結合 Microsoft Phi-3 探討文字內容、視覺及 MoE 的不同場景。

在課程結束時，您應該能回答以下問題：

- 什麼是 SLM？
- SLM 與 LLM 有何不同？
- 什麼是 Microsoft Phi-3/3.5 系列？
- 如何使用 Microsoft Phi-3/3.5 系列進行推論？

準備好了嗎？讓我們開始吧。

## 大型語言模型（LLMs）與小型語言模型（SLMs）的區別

LLM 與 SLM 都基於機率機器學習的基本原理，且在架構設計、訓練方法、數據生成過程和模型評估技術上採用相似方法。然而，兩者存在幾個關鍵的區分因素。

## 小型語言模型的應用

SLM 適用於多種應用場合，包括：

- 聊天機器人：提供客戶支持，與用戶進行對話式互動。
- 內容創建：協助寫作者生成創意，甚至草擬整篇文章。
- 教育：幫助學生完成寫作作業或學習新語言。
- 無障礙：為殘疾人士創建工具，如文字轉語音系統。

<strong>規模</strong>
  
LLM 與 SLM 的主要區別在於模型規模。LLM，如 ChatGPT（GPT-4），可能包含約 1.76 兆個參數，而開源 SLM 如 Mistral 7B 則設計有明顯較少參數——約 70 億。這種差異主要源於模型架構和訓練過程的不同。例如，ChatGPT 採用編碼器-解碼器架構中的自注意力機制，而 Mistral 7B 使用滑動窗口注意力，使其能在解碼器專用模型中更有效訓練。此架構差異對模型的複雜度和性能有深遠影響。

<strong>理解能力</strong>

SLM 通常針對特定領域優化，專精但可能難以提供跨多領域的廣泛語境理解。相比之下，LLM 致力模擬更全面的人類智能。LLM 在海量多樣化數據上訓練，旨在多領域表現出色，具更高多功能性及適應力。因而，LLM 更適合多種下游任務，如自然語言處理和程式設計。

<strong>計算需求</strong>

LLM 的訓練和部署資源需求龐大，通常需大量計算基礎設施，包括大規模 GPU 群集。例如，從零開始訓練 ChatGPT 需數千 GPU 長時間運行。相較之下，SLM 參數較少，使得計算資源更容易取得。像 Mistral 7B 可運行於配備適中 GPU 的本地設備，但仍需多 GPU 並行訓練數小時。

<strong>偏見問題</strong>

偏見是 LLM 的已知問題，主要來自其訓練數據的性質。這些模型多依賴公開網路原始數據，可能低估或誤表達特定群體，引入錯誤標註，或反映方言、地理差異及語法規則帶來的語言偏見。此外，LLM 結構複雜，若無細心微調，偏見問題可能被放大而不易察覺。相較之下，SLM 由於基於較受限、特定領域數據集訓練，天生較少受此類偏見影響，但並非完全免疫。

<strong>推論速度</strong>

較小的模型規模賦予 SLM 顯著推論速度優勢，能在本地硬體上高效生成結果，無需大量平行計算。LLM 由於體積和複雜度大，常需巨量平行計算資源以達到可接受的推論時間。多用戶同時在線時，LLM 的響應速度會更慢，特別是大規模部署時。

總結而言，LLM 與 SLM 雖同基於機器學習，卻在模型大小、資源需求、語境理解能力、偏見敏感度及推論速度等方面大相逕庭。這些差異反映出它們對不同應用場景的適用性：LLM 功能更廣但資源消耗更大；SLM 則在特定領域提供更高效的運算表現和降低計算成本。

***注意：本課程將以 Microsoft Phi-3 / 3.5 作為介紹 SLM 的範例。***

## 介紹 Phi-3 / Phi-3.5 系列

Phi-3 / 3.5 系列主要針對文字、視覺及 Agent（MoE）應用場景：

### Phi-3 / 3.5 指令版

主要用於文字生成、對話補全及內容信息提取等。

**Phi-3-mini**

這款 3.8B 參數的語言模型可在 Microsoft Foundry、Hugging Face 和 Ollama 使用。Phi-3 系列在關鍵基準測試中顯著超越同級甚至更大型語言模型（以下為基準數字，數字越大越好）。Phi-3-mini 表現優於其參數數量兩倍的模型，而 Phi-3-small 和 Phi-3-medium 表現更勝包括 GPT-3.5 的大型模型。

**Phi-3-small & medium**

Phi-3-small 僅有 7B 參數，已能在多種語言、推理、編碼及數學基準中擊敗 GPT-3.5T。

Phi-3-medium 配備 14B 參數，持續保持優勢，且表現超越 Gemini 1.0 Pro。

**Phi-3.5-mini**

可視為 Phi-3-mini 的升級版本。參數數量不變，但提升了多語言支持能力（支持 20 多種語言：阿拉伯語、中文、捷克語、丹麥語、荷蘭語、英語、芬蘭語、法語、德語、希伯來語、匈牙利語、義大利語、日語、韓語、挪威語、波蘭語、葡萄牙語、俄語、西班牙語、瑞典語、泰語、土耳其語、烏克蘭語），並增強了對長上下文的支持。

Phi-3.5-mini 擁有 3.8B 參數，表現優於同尺寸語言模型，與兩倍大小的模型旗鼓相當。

### Phi-3 / 3.5 視覺版

可以將 Phi-3/3.5 的指令版視為 Phi 的理解力，視覺版則是賦予 Phi 觀察世界的眼睛。


**Phi-3-Vision**

Phi-3-vision 僅 4.2B 參數，延續前述趨勢，在一般視覺推理、光學字符識別（OCR）、表格及圖表理解任務上超越大型模型如 Claude-3 Haiku 和 Gemini 1.0 Pro V。


**Phi-3.5-Vision**

Phi-3.5-Vision 也是 Phi-3-Vision 的升級版，增添了多張影像支持。可視為視覺能力的提升，不僅能看圖片，還能觀察影片。

Phi-3.5-vision 在 OCR、表格與圖表理解任務上優於大型模型如 Claude-3.5 Sonnet 和 Gemini 1.5 Flash，並在一般視覺知識推理任務上不遑多讓。支持多幀輸入，即對多張輸入圖片進行推理。


### Phi-3.5-MoE

***專家混合（Mixture of Experts, MoE）*** 可使用更少計算資源完成預訓練，使模型或數據集規模在相同計算預算下大幅擴展。MoE 模型特別能在預訓練階段更快達到與其密集模型對應版相同質量。

Phi-3.5-MoE 包含 16 個 3.8B 參數的專家模組。僅使用 6.6B 活躍參數的 Phi-3.5-MoE，能達到與更大模型相似的推理、語言理解及數學水平。

我們可以根據不同場景使用 Phi-3/3.5 系列模型。與 LLM 不同，Phi-3/3.5-mini 或 Phi-3/3.5-Vision 可部署於邊緣設備。


## 如何使用 Phi-3/3.5 系列模型

我們希望在不同場景下使用 Phi-3/3.5。接下來會根據不同場景展示 Phi-3/3.5 的使用方式。

![phi3](../../../translated_images/zh-HK/phi3.655208c3186ae381.webp)

### 透過雲端 API 進行推論

**Microsoft Foundry 模型**

> **注意：** GitHub 模型將於 2026 年 7 月底退役。[Microsoft Foundry 模型](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 是其直接替代方案。

Microsoft Foundry 模型是最直接的方式。您可通過 Foundry 模型目錄快速訪問 Phi-3/3.5-Instruct 模型。結合 Azure AI 推論 SDK 或 OpenAI SDK，您可通過程式碼調用 API 來完成 Phi-3/3.5-Instruct 的呼叫，也能透過 Playground 測試不同效果。

- 示範：Phi-3-mini 與 Phi-3.5-mini 在中文場景下效果比較

![phi3](../../../translated_images/zh-HK/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/zh-HK/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

若想使用視覺和 MoE 模型，也可使用 Microsoft Foundry 完成呼叫。若有興趣，可閱讀 Phi-3 Cookbook 了解如何透過 Microsoft Foundry 調用 Phi-3/3.5 指令、視覺、MoE 模型[點此連結](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

除基於雲端的 Microsoft Foundry 模型目錄外，您也可利用[NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst)完成相關呼叫。您可造訪 NVIDIA NIM 完成 Phi-3/3.5 系列的 API 呼叫。NVIDIA NIM（NVIDIA 推論微服務）是一套加速推論微服務，協助開發者高效部署 AI 模型於各種環境，包括雲端、資料中心及工作站。

NVIDIA NIM 的一些主要特點：

- **易於部署：** NIM 允許一條命令部署 AI 模型，讓整合現有工作流程變得簡單直觀。

- **優化性能：** 它利用 NVIDIA 預先優化的推理引擎，如 TensorRT 和 TensorRT-LLM，確保低延遲和高吞吐量。
- **可擴展性：** NIM 支援 Kubernetes 的自動擴展，使其能有效處理不同工作負載。
- **安全和控制：** 組織可以通過在自家管理的基礎設施上自托管 NIM 微服務來保持對數據和應用程式的控制。
- **標準 API：** NIM 提供行業標準的 API，使構建和整合聊天機器人、AI 助手等 AI 應用變得容易。

NIM 是 NVIDIA AI Enterprise 的一部分，旨在簡化 AI 模型的部署和運行，確保其在 NVIDIA GPU 上高效運行。

- 演示：使用 NVIDIA NIM 調用 Phi-3.5-Vision-API [[點此連結](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### 在本地運行 Phi-3/3.5
推理指的是基於輸入生成回應或預測的過程，與 Phi-3 或任何類似 GPT-3 的語言模型相關。當你向 Phi-3 提供提示或問題時，它會利用其訓練好的神經網絡通過分析訓練數據中的模式和關聯推斷出最有可能和相關的回答。

**Hugging Face Transformer**
Hugging Face Transformers 是一個強大的庫，專為自然語言處理（NLP）及其他機器學習任務設計。以下是一些重點：

1. **預訓練模型：** 它提供數千個可用於文本分類、命名實體識別、問答、摘要、翻譯及文本生成等任務的預訓練模型。

2. **框架互通性：** 該庫支援多種深度學習框架，包括 PyTorch、TensorFlow 和 JAX，使你能在一個框架中訓練模型並在另一個框架中使用。

3. **多模態能力：** 除了 NLP，Hugging Face Transformers 還支援計算機視覺（如圖像分類、目標檢測）和音訊處理（如語音識別、音訊分類）的任務。

4. **易於使用：** 該庫提供簡單的 API 和工具來下載和微調模型，讓初學者和專家都能方便使用。

5. **社群與資源：** Hugging Face 擁有活躍的社區，以及豐富的文檔、教程和指南，幫助用戶快速上手並充分利用該庫。
[官方文檔](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 或他們的 [GitHub 倉庫](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)。

這是最常用的方法，但它也需要 GPU 加速。畢竟，像 Vision 和 MoE 這樣的場景需要大量計算，未經量化的情況下在 CPU 上運行會非常慢。


- 演示：使用 Transformer 調用 Phi-3.5-Instruct [點此連結](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 演示：使用 Transformer 調用 Phi-3.5-Vision [點此連結](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 演示：使用 Transformer 調用 Phi-3.5-MoE [點此連結](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) 是一個旨在簡化您在本機運行大型語言模型（LLM）的平台。它支援 Llama 3.1、Phi 3、Mistral 和 Gemma 2 等多種模型。該平台通過將模型權重、配置和數據打包成一個單一包，讓用戶更容易自訂和創建自己的模型。Ollama 支援 macOS、Linux 和 Windows。如果您想在不依賴雲服務的情況下實驗或部署 LLM，這是一個非常好的工具。Ollama 是最直接的方式，您只需執行以下命令。


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 是微軟的離線本地模型運行時，可讓你完全在自家硬體上運行像 Phi 這樣的模型—無需 Azure 訂閱、API 金鑰或網路連接。它會自動選擇最佳的執行提供者（NPU、GPU 或 CPU），並暴露 OpenAI 兼容的端點，因此現有 `openai`/Azure AI 推理 SDK 代碼只需極少修改即可指向它。請參閱 [Foundry Local 文檔](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 以開始使用。

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) 是一個跨平台的機器學習推理及訓練加速器。ONNX Runtime for Generative AI (GENAI) 是一款強大的工具，可幫助您在多種平台上高效運行生成式 AI 模型。

## 什麼是 ONNX Runtime？
ONNX Runtime 是一個開源專案，使機器學習模型的高性能推理成為可能。它支援模型採用 Open Neural Network Exchange (ONNX) 格式，這是一種用於表示機器學習模型的標準。ONNX Runtime 推理能加速用戶體驗並降低成本，支援來自深度學習框架如 PyTorch 和 TensorFlow/Keras，也包括傳統機器學習庫如 scikit-learn、LightGBM、XGBoost 等的模型。ONNX Runtime 兼容不同硬體、驅動與操作系統，並通過運用硬體加速器配合圖優化和轉換來提供最佳性能。

## 什麼是生成式 AI？
生成式 AI 指的是能基於其訓練數據生成新內容（如文本、圖像或音樂）的 AI 系統。範例包括 GPT-3 這樣的語言模型和 Stable Diffusion 這樣的圖像生成模型。ONNX Runtime for GenAI 庫為 ONNX 模型提供生成式 AI 的全流程，包括使用 ONNX Runtime 進行推理、logits 處理、搜尋和採樣，以及 KV 緩存管理。

## ONNX Runtime for GENAI
ONNX Runtime for GENAI 擴展了 ONNX Runtime 的功能以支援生成式 AI 模型。以下是一些主要特點：

- **廣泛的平台支援：** 適用於 Windows、Linux、macOS、Android 和 iOS 等多種平台。
- **模型支援：** 支援多種流行的生成式 AI 模型，如 LLaMA、GPT-Neo、BLOOM 等。
- **性能優化：** 針對不同硬體加速器（如 NVIDIA GPU、AMD GPU 等）進行優化。
- **易於使用：** 提供便利的 API，方便應用程式整合，令文本、圖像及其他內容的生成只需少量代碼。
- 使用者可調用高階的 generate() 方法，或在迴圈中一個個生成 token，並選擇性地在迴圈內更新生成參數。
- ONNX runtime 還支持貪婪/束搜索和 TopP、TopK 採樣來生成序列，內建重複懲罰等 logits 處理，亦可輕鬆新增自訂評分機制。

## 入門指南
若要開始使用 ONNX Runtime for GENAI，您可以參考以下步驟：

### 安裝 ONNX Runtime：
```Python
pip install onnxruntime
```
### 安裝生成式 AI 擴展：
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
### 演示：使用 ONNX Runtime GenAI 調用 Phi-3.5-Vision


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

除了 ONNX Runtime、Ollama 和 Foundry Local 參考方法外，我們還可基於不同廠商提供的模型參考方法完成量化模型的參考，如 Apple MLX 框架搭配 Apple Metal、Qualcomm QNN 搭配 NPU、Intel OpenVINO 搭配 CPU/GPU 等。更多內容可見 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## 更多

我們已了解 Phi-3/3.5 家族的基礎，但要深入瞭解 SLM 需要更多知識。你可以在 Phi-3 Cookbook 中找到答案。若想深入學習，請造訪 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->