# 建構低程式碼 AI 應用程式

[![建構低程式碼 AI 應用程式](../../images/10-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(點擊上方圖片以觀看本課的影片)_

## 簡介

現在我們已經學會如何建構影像生成應用程式，讓我們來談談低程式碼。生成式 AI 可以用於包括低程式碼在內的各種不同領域，但什麼是低程式碼，我們如何將 AI 添加到其中呢？

建構應用程式和解決方案對於傳統開發者和非開發者來說變得更加容易，這要歸功於低程式碼開發平台。低程式碼開發平台使您能夠用很少甚至不需要程式碼來建構應用程式和解決方案。這是通過提供一個可視化的開發環境來實現的，該環境使您能夠拖放元件來建構應用程式和解決方案。這使您能夠更快地建構應用程式和解決方案，並且需要更少的資源。在本課程中，我們將深入探討如何使用低程式碼以及如何使用 Power Platform 與 AI 增強低程式碼開發。

Power Platform 為組織提供了一個機會，讓他們的團隊能夠通過直觀的低程式碼或無程式碼環境來建構自己的解決方案。這個環境有助於簡化建構解決方案的過程。使用 Power Platform，解決方案可以在幾天或幾週內建構完成，而不是幾個月或幾年。Power Platform 包含五個主要產品：Power Apps、Power Automate、Power BI、Power Pages 和 Copilot Studio。

本課程涵蓋:

- 介紹 Power Platform 中的生成式 AI
- 介紹 Copilot 及其使用方法
- 使用生成式 AI 在 Power Platform 中建構應用程式和流程
- 使用 AI Builder 了解 Power Platform 中的 AI 模型

## 學習目標

在這節課結束時，你將能夠：

- 了解 Copilot 在 Power Platform 中的運作方式。

- 為我們的教育初創公司建構一個學生作業追蹤應用程式。

- 建構一個使用 AI 從發票中提取資訊的發票處理流程。

- 在使用 GPT AI 模型建立文字時應用最佳實踐。

這節課中你將使用的工具和技術有:

- **Power Apps**, 用於學生作業追蹤應用程式，提供低程式碼開發環境來建構應用程式以追蹤、管理和互動資料。

- **Dataverse**, 用於儲存學生作業追蹤應用程式的資料，Dataverse 將提供低程式碼資料平台來儲存應用程式的資料。

- **Power Automate**, 用於發票處理流程，你將擁有低程式碼開發環境來建構工作流程以自動化發票處理過程。

- **AI Builder**, 用於發票處理 AI 模型，你將使用預建的 AI 模型來處理我們新創公司的發票。

## 生成式 AI 在 Power Platform

提升低程式碼開發和應用與生成式 AI 是 Power Platform 的一個關鍵重點領域。目標是讓每個人都能建構 AI 驅動的應用程式、網站、儀表板並自動化流程，_無需任何資料科學專業知識_。這個目標是通過將生成式 AI 以 Copilot 和 AI Builder 的形式整合到 Power Platform 的低程式碼開發體驗中來實現的。

### 這是如何運作的？

Copilot 是一個 AI 助手，通過使用自然語言在一系列對話步驟中描述您的需求，使您能夠建構 Power Platform 解決方案。例如，您可以指示您的 AI 助手說明您的應用程式將使用哪些欄位，它將建立應用程式和基礎資料模型，或者您可以指定如何在 Power Automate 中設定流程。

您可以在您的應用程式畫面中使用由 Copilot 驅動的功能，讓使用者透過對話互動來發掘見解。

AI Builder 是一種在 Power Platform 中提供的低程式碼 AI 功能，使您能夠使用 AI 模型來幫助自動化流程和預測結果。使用 AI Builder，您可以將 AI 引入您的應用程式和連接到 Dataverse 或各種雲端資料來源（如 SharePoint、OneDrive 或 Azure）的流程。

Copilot 可用於所有 Power Platform 產品: Power Apps、Power Automate、Power BI、Power Pages 和 Power Virtual Agents。AI Builder 可用於 Power Apps 和 Power Automate。在本課程中，我們將重點介紹如何在 Power Apps 和 Power Automate 中使用 Copilot 和 AI Builder 來為我們的教育初創公司建構解決方案。

### Copilot in Power Apps

作為 Power Platform 的一部分，Power Apps 提供了一個低程式碼開發環境，用於建構應用程式以追蹤、管理和互動資料。這是一套應用程式開發服務，具有可延展的資料平台，並能連接到雲端服務和內部部署資料。Power Apps 允許您建構可在瀏覽器、平板電腦和手機上執行的應用程式，並能與同事共享。Power Apps 透過簡單的介面讓使用者輕鬆進入應用程式開發，讓每個商業使用者或專業開發者都能建構自訂應用程式。透過 Copilot，應用程式開發體驗也因生成式 AI 而得到增強。

Power Apps 中的 copilot AI 助手功能使您能夠描述您需要什麼樣的應用程式以及您希望應用程式追蹤、收集或顯示哪些資訊。Copilot 然後根據您的描述生成一個響應式 Canvas 應用程式。然後您可以自訂應用程式以滿足您的需求。AI Copilot 還會生成並建議一個包含您需要的欄位來儲存您想要追蹤的資料的 Dataverse 表格和一些範例資料。我們將在本課程後面介紹什麼是 Dataverse 以及如何在 Power Apps 中使用它。然後您可以使用 AI Copilot 助手功能通過對話步驟來自訂表格以滿足您的需求。此功能可以從 Power Apps 主畫面中輕鬆使用。

### Copilot in Power Automate

作為 Power Platform 的一部分，Power Automate 讓使用者在應用程式和服務之間建立自動化工作流程。它有助於自動化重複的業務流程，例如通信、資料收集和決策批准。其簡單的介面允許每個技術能力層級的使用者（從初學者到經驗豐富的開發人員）自動化工作任務。透過 Copilot，生成式 AI 也增強了工作流程開發體驗。

Power Automate 中的副駕駛 AI 助手功能使您能夠描述您需要的流程類型以及希望流程執行的操作。副駕駛然後根據您的描述生成一個流程。然後您可以自訂流程以滿足您的需求。AI 副駕駛還會生成並建議您需要執行的操作來完成您想要自動化的任務。我們將在本課程的後面部分查看什麼是流程以及如何在 Power Automate 中使用它們。然後，您可以使用 AI 副駕駛助手功能通過對話步驟來自訂操作以滿足您的需求。此功能可從 Power Automate 主畫面中隨時使用。

## 作業: 使用 Copilot 管理我們新創公司的學生作業和發票

我們的初創公司為學生提供線上課程。該初創公司發展迅速，現在難以應對課程的需求。該初創公司聘請了你作為 Power Platform 開發人員，幫助他們建構一個低程式碼解決方案，以幫助他們管理學生作業和發票。他們的解決方案應能通過應用程式幫助他們追蹤和管理學生作業，並通過工作流程自動化發票處理過程。你被要求使用生成式 AI 開發該解決方案。

當你開始使用 Copilot 時，你可以使用 [Power Platform Copilot Prompt Library](https://pnp.github.io/powerplatform-prompts/?WT.mc_id=academic-109639-somelezediko) 來開始使用提示。此函式庫包含一系列提示，你可以用來與 Copilot 一起建構應用程式和流程。你也可以使用函式庫中的提示來了解如何向 Copilot 描述你的需求。

### 建構我們新創公司的學生作業追蹤應用程式

我們新創公司的教育工作者一直在努力跟蹤學生的作業。他們一直使用電子表格來跟蹤作業，但隨著學生數量的增加，這變得難以管理。他們要求你建構一個應用程式來幫助他們跟蹤和管理學生作業。該應用程式應允許他們新增作業、查看作業、更新作業和刪除作業。該應用程式還應允許教育工作者和學生查看已評分和未評分的作業。

您將使用 Power Apps 中的 Copilot 按照以下步驟建構應用程式:

1. 導航到 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 主畫面。

1. 使用主畫面上的文字區域描述您想要建構的應用程式。例如，**_我想建構一個應用程式來追蹤和管理學生作業_**。點擊 **Send** 按鈕將提示發送給 AI Copilot。

![描述你想要建構的應用程式](../../images/copilot-chat-prompt-powerapps.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot 會建議一個 Dataverse 表格，其中包含您需要儲存想要追蹤的資料的欄位和一些範例資料。然後，您可以使用 AI Copilot 助手功能，通過對話步驟來自訂表格以滿足您的需求。

   > **重要**: Dataverse 是 Power Platform 的基礎資料平台。它是一個低程式碼的資料平台，用於儲存應用程式的資料。它是一個完全管理的服務，安全地將資料儲存在 Microsoft Cloud 中，並在您的 Power Platform 環境中配置。它具有內建的資料治理功能，例如資料分類、資料譜系、細粒度存取控制等。您可以在[此處](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)了解更多關於 Dataverse 的資訊。

   ![在您的新表格中建議的欄位](../../images/copilot-dataverse-table-powerapps.png?WT.mc_id=academic-105485-koreyst)

1. 教育工作者希望向已提交作業的學生發送電子郵件，以便讓他們了解作業的進度。您可以使用 Copilot 向表格添加一個新欄位來儲存學生的電子郵件。例如，您可以使用以下提示來向表格添加新欄位: **_我想添加一個欄位來儲存學生的電子郵件_**。點擊 **發送** 按鈕將提示發送給 AI Copilot。

![新增一個新欄位](../../images/copilot-new-column.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot 會生成一個新欄位，然後您可以自訂該欄位以滿足您的需求。

1. 完成表格後，點擊 **Create app** 按鈕來建立應用程式。

1. AI Copilot 會根據您的描述生成一個響應式 Canvas 應用程式。然後您可以自訂應用程式以滿足您的需求。

1. 對於教育者發送電子郵件給學生，您可以使用 Copilot 向應用程式添加一個新螢幕。例如，您可以使用以下提示來向應用程式添加新螢幕：**_我想添加一個螢幕來發送電子郵件給學生_**。點擊 **Send** 按鈕將提示發送給 AI Copilot。

![通過提示指令添加新螢幕](../../images/copilot-new-screen.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot 會生成一個新畫面，然後您可以自訂畫面以滿足您的需求。

1. 完成應用程式後，點擊 **Save** 按鈕來保存應用程式。

1. 要與教育工作者分享應用程式，點擊 **Share** 按鈕，然後再次點擊 **Share** 按鈕。您可以通過輸入他們的電子郵件地址來與教育工作者分享應用程式。

> **你的作業**: 你剛建構的應用程式是一個好的開始，但可以進一步改進。使用電子郵件功能時，教育者只能手動輸入學生的電子郵件地址來發送郵件。你能使用Copilot來建構一個自動化功能，使教育者在學生提交作業時自動發送電子郵件嗎？提示：使用正確的提示，你可以在Power Automate中使用Copilot來建構這個功能。

### 建構我們新創公司的發票資訊表格

我們初創公司的財務團隊一直在努力追蹤發票。他們一直在使用電子表格來追蹤發票，但隨著發票數量的增加，這變得難以管理。他們要求你建立一個表格，幫助他們存儲、追蹤和管理收到的發票資訊。該表格應用於建構一個自動化系統，將所有發票資訊提取並存儲在表格中。該表格還應使財務團隊能夠查看已支付和未支付的發票。

Power Platform 有一個名為 Dataverse 的底層資料平台，可讓您儲存應用程式和解決方案的資料。Dataverse 提供一個低程式碼的資料平台來儲存應用程式的資料。這是一個完全受管理的服務，能夠安全地將資料儲存在 Microsoft Cloud 中，並在您的 Power Platform 環境中配置。它具有內建的資料治理功能，例如資料分類、資料沿革、細粒度存取控制等。您可以在[此處了解更多關於 Dataverse 的資訊](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)。

為什麼我們的初創公司應該使用 Dataverse？Dataverse 中的標準和自訂表格為您的數據提供了一個安全且基於雲端的存儲選項。表格讓您可以存儲不同類型的數據，類似於您在單個 Excel 工作簿中使用多個工作表的方式。您可以使用表格來存儲特定於您的組織或業務需求的數據。我們的初創公司使用 Dataverse 所獲得的一些好處包括但不限於：

- **易於管理**: Metadata 和資料都存儲在雲端，因此您不必擔心它們如何存儲或管理。您可以專注於建構您的應用程式和解決方案。

- **安全**: Dataverse 為您的資料提供安全且基於雲端的存儲選項。您可以使用基於角色的安全性控制誰可以訪問表中的資料以及他們如何訪問。

- **豐富的 Metadata**: 資料類型和關係直接在 Power Apps 中使用。

- **邏輯和驗證**: 您可以使用業務規則、計算欄位和驗證規則來強制執行業務邏輯並保持資料準確性。

現在你已經知道什麼是 Dataverse 以及為什麼應該使用它，讓我們來看看如何使用 Copilot 在 Dataverse 中建立一個表格以滿足我們財務團隊的需求。

> **注意** : 您將在下一節中使用此表來建構一個自動化流程，該流程將提取所有發票資訊並將其存儲在表中。

要使用 Copilot 在 Dataverse 中建立表格，請按照以下步驟操作:

1. 導航到 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 主畫面。

2. 在左側導航欄中，選擇 **Tables**，然後點擊 **Describe the new Table**。

![選擇新表格](../../images/describe-new-table.png?WT.mc_id=academic-105485-koreyst)

1. 在 **描述新表格** 畫面上，使用文字區域描述您想要建立的表格。例如，**_我想建立一個表格來儲存發票資訊_**。點擊 **送出** 按鈕將提示發送給 AI Copilot。

![描述此表格](../../images/copilot-chat-prompt-dataverse.png?WT.mc_id=academic-105485-koreyst)

1. AI Copilot 將建議一個 Dataverse 表格，包含您需要儲存您想追蹤的資料的欄位和一些範例資料。然後，您可以使用 AI Copilot 助手功能通過對話步驟自訂表格以滿足您的需求。

![建議的Dataverse表格](../../images/copilot-dataverse-table.png?WT.mc_id=academic-105485-koreyst)

1. 財務團隊希望發送電子郵件給供應商，以更新他們的發票當前狀態。你可以使用Copilot向表格添加一個新欄位來存儲供應商電子郵件。例如，你可以使用以下提示來向表格添加新欄位: **_我想添加一個欄位來存儲供應商電子郵件_**。點擊**發送**按鈕將提示發送給AI Copilot。

1. AI Copilot會生成一個新欄位，然後你可以自定義該欄位以滿足你的需求。

1. 完成表格後，點擊**建立**按鈕來建立表格。

## AI 模型在 Power Platform 中的應用與 AI Builder

AI Builder 是一種在 Power Platform 中提供的低程式碼 AI 功能，使您能夠使用 AI 模型來幫助自動化流程和預測結果。使用 AI Builder，您可以將 AI 引入您的應用程式和連接到 Dataverse 或各種雲端資料來源（如 SharePoint、OneDrive 或 Azure）的流程。

## 預建 AI 模型 vs 自訂 AI 模型

AI Builder 提供兩種類型的 AI 模型: 預建 AI 模型和自訂 AI 模型。預建 AI 模型是由 Microsoft 訓練並在 Power Platform 中可用的即用型 AI 模型。這些模型幫助你為應用程式和流程添加智能，而無需收集資料並建構、訓練和發佈你自己的模型。你可以使用這些模型來自動化流程並預測結果。

Power Platform 中可用的一些預建 AI 模型包括:

- **關鍵詞提取**: 此模型從文本中提取關鍵詞。
- **語言檢測**: 此模型檢測文本的語言。
- **情感分析**: 此模型檢測文本中的正面、負面、中立或混合情感。
- **名片讀取器**: 此模型從名片中提取資訊。
- **文本識別**: 此模型從圖像中提取文本。
- **物件檢測**: 此模型檢測並從圖像中提取物件。
- **文件處理**: 此模型從表單中提取資訊。
- **發票處理**: 此模型從發票中提取資訊。

使用自訂 AI 模型，您可以將自己的模型引入 AI Builder，使其能像任何 AI Builder 自訂模型一樣運作，允許您使用自己的資料訓練模型。您可以使用這些模型在 Power Apps 和 Power Automate 中自動化流程並預測結果。使用您自己的模型時，有一些限制適用。閱讀更多關於這些[限制](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst)。

![AI 建構模型](../../images/ai-builder-models.png?WT.mc_id=academic-105485-koreyst)

## 作業 #2 - 為我們的創業公司建構發票處理流程

財務團隊一直在努力處理發票。他們一直在使用電子表格來追蹤發票，但隨著發票數量的增加，這變得難以管理。他們要求你建構一個工作流程，幫助他們使用 AI 處理發票。該工作流程應能讓他們從發票中提取資訊並將資訊存儲在 Dataverse 表中。該工作流程還應能讓他們將提取的資訊發送電子郵件給財務團隊。

現在你已經知道什麼是 AI Builder 以及為什麼應該使用它，讓我們來看看如何在 AI Builder 中使用我們之前提到的發票處理 AI 模型，來建構一個幫助財務團隊處理發票的工作流程。

要建構一個工作流程，以幫助財務團隊使用 AI Builder 中的發票處理 AI 模型處理發票，請按照以下步驟操作:

1. 導航到[Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst)主畫面。

2. 使用主畫面上的文字區域描述您想要建構的工作流程。例如，**_處理到達郵箱的發票_**。點擊**發送**按鈕將提示發送給AI Copilot。

   ![Copilot power automate](../../images/copilot-chat-prompt-powerautomate.png?WT.mc_id=academic-105485-koreyst)

3. AI Copilot會建議您需要執行的動作來完成您想要自動化的任務。您可以點擊**下一步**按鈕進行下一步。

4. 在下一步中，Power Automate會提示您設定流程所需的連接。完成後，點擊**建立流程**按鈕來建立流程。

5. AI Copilot會生成一個流程，然後您可以自訂流程以符合您的需求。

6. 更新流程的觸發器並將**資料夾**設置為存放發票的資料夾。例如，您可以將資料夾設置為**收件箱**。點擊**顯示進階選項**並將**僅限附件**設置為**是**。這將確保流程僅在收到帶有附件的電子郵件時執行。

7. 從流程中移除以下動作：**HTML轉文字**、**撰寫**、**撰寫2**、**撰寫3**和**撰寫4**，因為您不會使用它們。

8. 從流程中移除**條件**動作，因為您不會使用它。應該如下圖所示：

   ![power automate, remove actions](../../images/powerautomate-remove-actions.png?WT.mc_id=academic-105485-koreyst)

9. 點擊**新增動作**按鈕並搜索**Dataverse**。選擇**新增一行**動作。

10. 在**從發票中提取資訊**動作中，更新**發票檔案**以指向電子郵件中的**附件內容**。這將確保流程從發票附件中提取資訊。

11. 選擇您之前建立的**表格**。例如，您可以選擇**發票資訊**表格。選擇前一動作中的動態內容來填充以下欄位：

    - ID
    - 金額
    - 日期
    - 名稱
    - 狀態 - 將**狀態**設置為**待處理**。
    - 供應商電子郵件 - 使用**當新郵件到達時**觸發器中的**寄件者**動態內容。

    ![power automate add row](../../images/powerautomate-add-row.png?WT.mc_id=academic-105485-koreyst)

12. 完成流程後，點擊**儲存**按鈕來儲存流程。然後，您可以通過向觸發器中指定的資料夾發送帶有發票的電子郵件來測試流程。

> **你的作業**: 你剛剛建構的流程是一個好的開始，現在你需要思考如何建構一個自動化流程，使我們的財務團隊能夠發送電子郵件給供應商，更新他們的發票當前狀態。提示: 當發票狀態變更時，流程必須執行。

## 在 Power Automate 中使用文本生成 AI 模型

在 AI Builder 中使用 GPT AI 模型建立文字，讓你能夠根據提示生成文字，並由 Microsoft Azure OpenAI 服務提供支持。利用這項功能，你可以將 GPT（生成式預訓練轉換器）技術整合到你的應用程式和流程中，以建構各種自動化流程和具洞察力的應用程式。

GPT 模型經過大量數據的廣泛訓練，使其在提供提示時能夠生成與人類語言非常相似的文本。當與工作流程自動化集成時，像 GPT 這樣的 AI 模型可以用來簡化和自動化各種任務。

例如，你可以建構流程來自動生成各種用例的文本，例如: 電子郵件草稿、產品描述等。你也可以使用該模型為各種應用程式生成文本，例如聊天機器人和客服應用程式，使客服人員能夠有效且高效地回應客戶查詢。

![建立提示](../../images/create-prompt-gpt.png?WT.mc_id=academic-105485-koreyst)

要學習如何在 Power Automate 中使用此 AI 模型，請參閱[使用 AI Builder 和 GPT 增加智慧](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko)模組。

## 很棒的工作！繼續學習

完成本課程後，請查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以繼續提升您的生成式 AI 知識！

前往第11課，我們將探討如何[將生成式AI與函式呼叫整合](../../../11-integrating-with-function-calling/translations/tw/README.md?WT.mc_id=academic-105485-koreyst)！

