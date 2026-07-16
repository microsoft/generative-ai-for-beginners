# 建立低程式碼 AI 應用程式

[![建立低程式碼 AI 應用程式](../../../translated_images/zh-HK/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(點擊上方圖片觀看本課程影片)_

## 介紹

現在我們已經學會如何建立圖片生成應用程式，接著讓我們談談低程式碼。生成式 AI 可以應用於多個不同領域，包括低程式碼，但什麼是低程式碼，我們如何將 AI 加入其中呢？

傳統開發人員及非開發人員利用低程式碼開發平台，建構應用程式和解決方案變得更輕鬆。低程式碼開發平台使您能夠以極少或不用撰寫程式碼的方式來建立應用程式和解決方案。這是透過提供一個視覺化開發環境，讓您拖放元件來組合應用程式和解決方案來實現的。這使您能更快、以較少資源完成開發。在本課程，我們深入探討如何使用低程式碼，並如何使用 Power Platform 加入 AI 來強化低程式碼開發。

Power Platform 為組織提供機會，使其團隊能夠通過直觀的低程式碼或無程式碼環境自行建立解決方案。該環境幫助簡化建立解決方案的流程。利用 Power Platform，解決方案可在數日或數週內建成，而非數月甚至數年。Power Platform 包含五個主要產品：Power Apps、Power Automate、Power BI、Power Pages 和 Copilot Studio。

本課程涵蓋：

- Power Platform 中生成式 AI 的介紹
- Copilot 介紹及如何使用
- 使用生成式 AI 來建立 Power Platform 內的應用程式和流程
- 了解 Power Platform 中 AI Builder 的 AI 模型
- 使用 Microsoft Copilot Studio 建立智能代理

## 學習目標

完成本課程後，您將能夠：

- 了解 Copilot 在 Power Platform 中的運作方式。

- 為我們的教育新創公司建立學生作業追蹤應用程式。

- 建立運用 AI 從發票中擷取資訊的發票處理流程。

- 使用 Create Text 與 GPT AI 模型時應用最佳實踐。

- 了解 Microsoft Copilot Studio 是什麼以及如何利用它建立智能代理。

本課程中您將使用的工具與技術有：

- **Power Apps**，用於建立學生作業追蹤應用程式，提供建立應用程式來追蹤、管理及互動資料的低程式碼開發環境。

- **Dataverse**，存放學生作業追蹤應用程式的資料，提供低程式碼資料平台來儲存應用程式資料。

- **Power Automate**，用於建立發票處理流程，提供低程式碼開發環境來建構自動化發票處理的工作流程。

- **AI Builder**，用於發票處理的 AI 模型，使用預建的 AI 模型來協助我們的新創公司處理發票。

## Power Platform 中的生成式 AI

強化低程式碼開發與應用的生成式 AI 是 Power Platform 的重點方向。目標是讓所有人都能建立具 AI 功能的應用程式、網站、儀表板，並利用 AI 自動化流程，_不需任何資料科學的專業知識_。此目標透過在 Power Platform 低程式碼開發體驗中整合生成式 AI，以 Copilot 和 AI Builder 的形式實現。

### 這是如何運作的？

Copilot 是一個 AI 助理，可以讓您透過自然語言描述需求，在一系列會話式步驟中建立 Power Platform 解決方案。例如，您可以指示 AI 助理說明應用程式需要的欄位，它將建立應用程式及其背後的資料模型，或者您可以說明如何在 Power Automate 中設定流程。

您可以將 Copilot 驅動的功能當成應用程式畫面中的功能，讓使用者透過會話互動發掘洞見。

AI Builder 是 Power Platform 中的低程式碼 AI 功能，使您能利用 AI 模型幫助自動化流程及預測結果。借助 AI Builder，您可以將 AI 功能帶入與 Dataverse 或各種雲端資料來源（例如 SharePoint、OneDrive 或 Azure）連接的應用程式和流程中。

Copilot 可在 Power Platform 所有產品中使用：Power Apps、Power Automate、Power BI、Power Pages 及 Copilot Studio（前身為 Power Virtual Agents）。AI Builder 可於 Power Apps 和 Power Automate 中使用。在本課程，我們將聚焦於如何在 Power Apps 和 Power Automate 中使用 Copilot 及 AI Builder，為我們的教育新創公司開發解決方案。

### Power Apps 中的 Copilot

作為 Power Platform 的一部分，Power Apps 提供低程式碼開發環境來建置用於追蹤、管理和交互資料的應用程式。這是一套應用程式開發服務，包含可擴充的資料平台及連接雲端服務與本地資料的能力。Power Apps 允許您建置可在瀏覽器、平板和手機上執行並可與同事分享的應用程式。Power Apps 以簡易介面讓每位商務用戶或專業開發人員都能打造自訂應用程式。生成式 AI 與 Copilot 的整合進一步提升應用程式開發體驗。

Power Apps 中的 Copilot AI 助理功能讓您描述您需要的應用程式類型以及您希望應用程式追蹤、收集或顯示哪些資訊。Copilot 會基於您的描述生成響應式 Canvas 應用程式。然後您可以根據需求自訂應用程式。AI Copilot 也會生成並建議 Dataverse 資料表，包含您需要的欄位來存放想追蹤的資料及一些範例資料。我們稍後會在本課程探討 Dataverse 是什麼以及如何在 Power Apps 中使用。您可透過 Copilot 助理的會話式步驟自訂資料表以符合需求。此功能可在 Power Apps 首頁輕鬆使用。

### Power Automate 中的 Copilot

作為 Power Platform 的一部分，Power Automate 讓用戶在應用程式和服務之間建立自動化工作流程。它有助於自動化重複的商務流程，如通訊、資料收集和決策審批。其簡單介面讓不同技術程度的用戶（從初學者到資深開發者）皆能自動化工作任務。生成式 AI 與 Copilot 整合亦提升了流程開發體驗。

Power Automate 中的 Copilot AI 助理功能讓您描述需要的流程類型及該流程需要執行的動作。Copilot 根據您的描述生成流程，然後您可依需求自訂流程。AI Copilot 也會建議完成任務所需的動作。我們稍後會在本課程詳細說明工作流程及如何在 Power Automate 中使用它們。您可透過 Copilot 助理的會話式步驟自訂動作以符合需求。此功能可自 Power Automate 首頁輕鬆存取。

## 使用 Microsoft Copilot Studio 建立智能代理

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst)（前身為 Power Virtual Agents）是 Power Platform 中的低程式碼成員，用於建立<strong>AI 代理</strong>—能夠回答問題、執行動作並代替使用者自動完成任務的對話式副手。與 Power Platform 其他部分一樣，您透過視覺化且以自然語言為先的體驗來建立這些代理：您描述想要讓代理執行的內容，Copilot Studio 協助搭建指令、知識和動作。

對於我們的教育新創公司，您可以建立一個能回答學生課程問題、檢查作業截止日期，甚至寄送電子郵件給講師的代理—全部不需撰寫程式碼。

以下是使 Copilot Studio 強大的最新功能：

- <strong>從您的知識中生成回答</strong>。不用手動撰寫每段對話，您可以連結<strong>知識來源</strong>—公共網站、SharePoint、OneDrive、Dataverse、上傳的檔案或透過連接器存取的企業資料—代理會從中生成有根據的回答。

- <strong>生成式編排</strong>。代理不依賴僵硬的觸發語句，而是利用 AI 理解請求，動態決定結合哪些知識、主題與動作來完成請求，包含串聯多步驟。

- <strong>動作與連接器</strong>。代理不只是聊天。您可授予代理由 1,500+ 預建 Power Platform 連接器、Power Automate 流程、自訂 REST API、提示語及<strong>模型上下文協議 (MCP)</strong> 伺服器所支持的動作能力。

- <strong>自主代理</strong>。代理不僅限於聊天視窗回應。您可以建立透過事件觸發的<strong>自主代理</strong>—例如收到新郵件、Dataverse 中新增記錄或檔案上傳—然後在背景執行任務。

- <strong>多代理編排</strong>。代理可以呼叫其他代理。Copilot Studio 的代理可交接給或由其他代理擴展，包括已發佈至 Microsoft 365 Copilot 及在 Microsoft Foundry 建立的代理。

- <strong>模型選擇</strong>。除了內建模型，您可使用 Microsoft Foundry 模型目錄中的模型，定制代理的推理及回應方式。

- <strong>隨處發佈</strong>。建立完成後，代理可以發佈到多個通道—Microsoft Teams、Microsoft 365 Copilot、網站或自訂應用程式等—其安全性、身份驗證與分析由 Power Platform 管理員體驗管理。

您可以在 [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) 開始建立您的第一個代理，並在 [Microsoft Copilot Studio 文件](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst) 中了解更多。

## 作業：使用 Copilot 為我們的新創公司管理學生作業和發票

我們的新創公司提供線上課程給學生。公司迅速成長，現在難以應付課程需求。公司聘請您作為 Power Platform 開發人員，協助他們建立低程式碼解決方案，以管理學生作業和發票。該解決方案應能透過應用程式追蹤和管理學生作業，並透過工作流程自動化發票處理流程。要求您使用生成式 AI 來開發該解決方案。

剛開始使用 Copilot 時，您可以利用 [Power Platform Copilot 提示庫](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) 來取得提示。該庫包含您可用於與 Copilot 建立應用程式和流程的提示列表。您也可以利用庫中的提示，理解如何向 Copilot 描述需求。

### 為我們的新創公司建立學生作業追蹤應用程式

我們的新創公司的教育者一直在努力追蹤學生作業。原先使用試算表追蹤作業，但隨著學生人數增加，管理變得困難。他們要求您建立一個應用程式，協助追蹤和管理學生作業。此應用程式應允許他們新增作業、查看作業、更新作業及刪除作業。應用程式亦應允許教育者和學生查看已評分及未評分的作業。

您將依照以下步驟，使用 Power Apps 中的 Copilot 建立此應用程式：

1. 前往 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 首頁。

1. 使用首頁上的文字區描述您要建立的應用程式。例如，**_我想建立一個用來追蹤和管理學生作業的應用程式_**。點擊<strong>發送</strong>按鈕，將提示發送給 AI Copilot。

![描述您想建立的應用程式](../../../translated_images/zh-HK/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot 會建議一個 Dataverse 資料表，包含您需用來存放追蹤資料的欄位及一些範例資料。然後您可以透過 AI Copilot 助理功能，以會話形式步驟自訂該資料表來符合需求。

   > <strong>重要</strong>：Dataverse 是 Power Platform 的基礎資料平台。它是一個低程式碼資料平台，用於儲存應用程式資料。它是一項由微軟雲端完全管理的服務，部署於您的 Power Platform 環境中。它帶有內建的資料治理功能，如資料分類、資料血緣、細粒度存取控制等。您可在[此處](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)了解更多關於 Dataverse 的資訊。

   ![新資料表中建議的欄位](../../../translated_images/zh-HK/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. 教育者希望寄送電子郵件給已提交作業的學生，以通知他們作業進度。您可以使用 Copilot 為資料表新增一個欄位以儲存學生電子郵件。例如，您可以使用以下提示來新增欄位：**_我想新增一欄以儲存學生電子郵件_**。點擊<strong>發送</strong>按鈕，將提示發送給 AI Copilot。

![新增欄位](../../../translated_images/zh-HK/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot 將生成新欄位，您之後可以依需求自訂該欄位。


1. 完成表格後，點擊 **Create app** 按鈕以建立應用程式。

1. AI 助理會根據您的描述生成一個響應式 Canvas 應用程式。您之後可以自訂應用程式以符合您的需求。

1. 教育工作者若想發送電子郵件給學生，可以使用 Copilot 為應用程式新增一個螢幕。例如，您可以使用以下提示詞新增一個螢幕：**_我想新增一個螢幕來發送電子郵件給學生_**。點擊 **Send** 按鈕將提示發送給 AI 助理。

![添加新螢幕的提示指令](../../../translated_images/zh-HK/copilot-new-screen.2e0bef7132a17392.webp)

1. AI 助理會生成一個新螢幕，您可以自訂該螢幕以符合您的需求。

1. 完成應用程式後，點擊 **Save** 按鈕以保存應用程式。

1. 若要與教育工作者分享該應用程式，點擊 **Share** 按鈕，然後再次點擊 **Share** 按鈕。接著，您可以輸入教育工作者的電子郵件地址以分享應用程式。

> <strong>您的作業</strong>：剛建立的應用程式是一個良好的開始，但仍有改進空間。使用電子郵件功能時，教育工作者只能手動輸入學生的電子郵件。您能否利用 Copilot 建立一個自動化功能，使教育工作者在學生提交作業時能自動發送郵件給學生？提示是您可以使用 Power Automate 裡的 Copilot 來建立此功能，只需輸入正確的提示詞。

### 為我們的新創公司建立發票資訊表

我們新創公司的財務團隊一直在努力追蹤發票。過去他們使用活頁簿來追蹤發票，但隨著發票數量增加，管理變得困難。他們請您建立一個表格，幫助他們儲存、追蹤和管理收到的發票資訊。該表格應用於建立一個自動化流程，提取所有發票資訊並儲存到表格中。該表格還應能讓財務團隊查看已付款與尚未付款的發票。

Power Platform 擁有一個底層的資料平台稱為 Dataverse，能讓您為應用程式和解決方案儲存資料。Dataverse 提供低程式碼的資料平台，存放應用程式的資料。它是完全管理的服務，安全地在 Microsoft 雲端儲存資料，並在您的 Power Platform 環境中提供。它具備內建的資料治理功能，如資料分類、資料血緣、細粒度權限控制等。您可以在[此處了解更多關於 Dataverse](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko)。

為什麼我們的新創公司要使用 Dataverse？Dataverse 內的標準和自訂表格提供安全且基於雲端的資料儲存選項。表格讓您能儲存不同類型的資料，就像在一個 Excel 活頁簿中使用多個工作表一樣。您可以使用表格儲存公司或業務特定的資料。我們新創公司使用 Dataverse 獲得的部分好處包括但不限於：

- <strong>易於管理</strong>：元資料與資料皆存於雲端，您不必擔心它們的儲存或管理細節，您可以專注於建立您的應用程式和解決方案。

- <strong>安全</strong>：Dataverse 提供安全且基於雲端的資料儲存選項。您可以使用基於角色的安全性控制誰能訪問資料，以及如何訪問資料。

- <strong>豐富的元資料</strong>：資料類型和關聯可直接在 Power Apps 中使用

- <strong>邏輯與驗證</strong>：您可以使用商業規則、計算欄位和驗證規則來實施商業邏輯並維護資料的準確性。

現在您已了解 Dataverse 是什麼及為何應該使用它，接下來看如何用 Copilot 在 Dataverse 中建立一個表格以滿足財務團隊的需求。

> <strong>注意</strong>：您將在下一節中使用此表格，建立一個自動化流程以提取所有發票資訊並儲存到該表格中。

使用 Copilot 在 Dataverse 建立表格，請依下列步驟操作：

1. 前往 [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) 主畫面。

2. 在左邊導覽列選擇 **Tables**，然後點擊 **Describe the new Table**。

![選擇新表格](../../../translated_images/zh-HK/describe-new-table.0792373eb757281e.webp)

1. 在 **Describe the new Table** 頁面中的文字區域，描述您要建立的表格。例如，**_我想建立一個表格用來存放發票資訊_**。點擊 **Send** 按鈕將提示發送給 AI 助理。

![描述表格](../../../translated_images/zh-HK/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI 助理會建議一個包含您需要用來追蹤資料欄位以及一些範例資料的 Dataverse 表格。您可以使用 AI 助理的對話功能進一步自訂該表格以符合需求。

![建議的 Dataverse 表格](../../../translated_images/zh-HK/copilot-dataverse-table.b3bc936091324d9d.webp)

1. 財務團隊希望發送電子郵件給供應商，以更新其發票的目前狀態。您可以使用 Copilot 為表格新增一個欄位來存放供應商電子郵件。例如，您可以使用以下提示詞：**_我想新增一欄用於存放供應商電子郵件_**。點擊 **Send** 按鈕將提示發送給 AI 助理。

1. AI 助理會生成一個新欄位，您可以自訂該欄位以符合需求。

1. 完成表格設計後，點擊 **Create** 按鈕建立表格。

## Power Platform 中的 AI 模型與 AI Builder

AI Builder 是 Power Platform 中的低程式碼 AI 能力，讓您使用 AI 模型來協助自動化流程和預測結果。藉由 AI Builder，您可以將 AI 功能帶入連接 Dataverse 或各種雲端資料來源（如 SharePoint、OneDrive 或 Azure）的應用程式和流程中。

## 預建 AI 模型與自訂 AI 模型

AI Builder 提供兩種類型的 AI 模型：預建 AI 模型和自訂 AI 模型。預建 AI 模型是由 Microsoft 訓練並且已可在 Power Platform 中直接使用的模型。這些模型幫助您為應用程式和流程新增智慧功能，無需自行蒐集資料、建立、訓練和發布模型。您可以使用這些模型來自動化流程和預測結果。

Power Platform 中可用的部分預建 AI 模型包括：

- <strong>關鍵詞萃取</strong>：萃取文本中的關鍵字詞。
- <strong>語言偵測</strong>：偵測文本所使用的語言。
- <strong>情感分析</strong>：分析文本的正面、負面、中立或混合情感。
- <strong>名片閱讀器</strong>：從名片中萃取資訊。
- <strong>文字辨識</strong>：從圖片中萃取文字。
- <strong>物件偵測</strong>：偵測及萃取圖片中的物件。
- <strong>文件處理</strong>：從表單中萃取資訊。
- <strong>發票處理</strong>：從發票中萃取資訊。

使用自訂 AI 模型，您可將自有模型整合至 AI Builder，使它像任何 AI Builder 自訂模型一樣運作，並可使用自有資料訓練模型。您可以使用這些模型在 Power Apps 和 Power Automate 中自動化流程與預測結果。自帶模型時會有某些限制，請參閱這些[限制說明](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst)。

![AI Builder 模型](../../../translated_images/zh-HK/ai-builder-models.8069423b84cfc47f.webp)

## 作業 #2 - 為我們的新創公司建立一個發票處理流程

財務團隊一直在努力處理發票，過去使用活頁簿追蹤發票，但隨著發票量增加，管理困難。他們請您建立一個使用 AI 的工作流程，幫助他們處理發票。工作流程應能從發票提取資訊，並將資訊儲存在 Dataverse 表格中。此外，工作流程應能發送包含提取資訊的電子郵件給財務團隊。

現在您已了解 AI Builder 是什麼及為什麼應該使用它，接著看如何使用先前介紹的 AI Builder 中的發票處理 AI 模型，來建立一個協助財務團隊處理發票的工作流程。

要使用 AI Builder 的發票處理 AI 模型來建立工作流程，請依照下列步驟操作：

1. 前往 [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) 主頁面。

2. 在主頁面的文字區域中描述您想建立的工作流程。例如，**_當發票到達我的郵箱時處理該發票_**。點擊 **Send** 按鈕將提示發送給 AI 助理。

   ![Copilot power automate](../../../translated_images/zh-HK/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI 助理會建議完成該自動化任務所需的動作。您可以點擊 **Next** 按鈕瀏覽後續步驟。

4. 下一步，Power Automate 會提示您設置流程所需的連線。完成後，點擊 **Create flow** 按鈕建立流程。

5. AI 助理會生成一個流程，您可以自訂流程以符合您的需求。

6. 更新流程的觸發條件，將 **Folder** 設定為存放發票的資料夾。例如，您可以設為 **Inbox**。點擊 **Show advanced options**，將 **Only with Attachments** 設定為 **Yes**。這將確保流程僅在收到帶有附件的電子郵件時執行。

7. 從流程中刪除以下動作：**HTML to text**、**Compose**、**Compose 2**、**Compose 3** 及 **Compose 4**，因為您不會使用它們。

8. 從流程中刪除 **Condition** 動作，因為您不會使用它。流程應如以下截圖所示：

   ![power automate, remove actions](../../../translated_images/zh-HK/powerautomate-remove-actions.7216392fe684ceba.webp)

9. 點擊 **Add an action** 按鈕並搜尋 **Dataverse**。選擇 **Add a new row** 動作。

10. 在 **Extract Information from invoices** 動作中，將 **Invoice File** 設定為來自電子郵件的 **Attachment Content**。這將確保流程從發票附件中提取資訊。

11. 選擇您之前建立的 **Table**，例如 **Invoice Information** 表格。使用上一個動作的動態內容填充以下欄位：

    - ID
    - Amount
    - Date
    - Name
    - 狀態 - 將 **Status** 設定為 **Pending**。
    - 供應商電郵 - 使用 **When a new email arrives** 觸發器中的 **From** 動態內容。

    ![power automate add row](../../../translated_images/zh-HK/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. 完成流程設計後，點擊 **Save** 按鈕保存流程。您可以透過將帶有發票的電子郵件寄送到觸發器指定的資料夾，來測試流程。

> <strong>您的作業</strong>：剛建立的流程是個良好開始，接下來請思考如何建立一個自動化流程，使財務團隊能在發票狀態變更時，自動發送電郵通知供應商其發票的當前狀態。提示：流程必須在發票狀態更改時執行。

## 在 Power Automate 中使用文字生成 AI 模型

AI Builder 中的 Create Text with GPT AI 模型能根據提示生成文字，此模型由 Microsoft Azure OpenAI 服務提供技術支持。透過此能力，您可以將 GPT（生成式預訓練轉換器）技術整合到應用程式和流程中，建構各種自動化流程和智慧應用程式。

GPT 模型經過大量訓練資料的學習，能根據提示產生接近人類語言的文字。當與工作流程自動化結合時，GPT 等 AI 模型能用來簡化和自動化廣泛的任務。

例如，您可以建立流程自動生成各種用途的文字，如電子郵件草稿、產品描述等。您也可利用該模型為聊天機器人和客戶服務應用生成文字，協助客服人員有效且高效地回應客戶查詢。

![建立提示](../../../translated_images/zh-HK/create-prompt-gpt.69d429300c2e870a.webp)


如要學習如何在 Power Automate 中使用此 AI 模型，請瀏覽 [利用 AI Builder 和 GPT 新增智能](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) 模組。

## 做得好！繼續你的學習之旅

完成本課程後，查看我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

想自訂並充分發揮 Copilot 的功能？探索 [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — 一個由社群貢獻的指令、代理、技能和配置合集，助你最大化利用 GitHub Copilot。

前往第 11 課，我們將探討如何[結合生成式 AI 與函數調用](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->