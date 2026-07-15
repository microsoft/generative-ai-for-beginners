# 雲端設置 ☁️ – GitHub Codespaces

**如果你不想在本地安裝任何東西，請使用此指南。**  
Codespaces 為你提供一個免費的、基於瀏覽器的 VS Code 實例，所有相依性已預先安裝。

---

## 1. 為什麼選擇 Codespaces？

| 優點 | 對你來說的意義 |
|---------|----------------------|
| ✅ 零安裝 | 可在 Chromebook、iPad、學校實驗室電腦上運作… |
| ✅ 預設開發容器 | 內建 Python 3、Node.js、.NET、Java 等環境 |
| ✅ 免費配額 | 個人帳戶每月可使用 **120 核心小時 / 60 GB 小時** |

> 💡 <strong>小提示</strong>  
> 保持你的配額健康，請 <strong>停止</strong> 或 <strong>刪除</strong> 空閒的 codespaces  
> (檢視 ▸ 命令面板 ▸ *Codespaces: Stop Codespace*)。

---

## 2. 建立 Codespace（一步驟）

1. **Fork** 此倉庫（右上角 **Fork** 按鈕）。  
2. 在你的 fork 裡，點選 **Code ▸ Codespaces ▸ Create codespace on main**。  
   ![Dialog showing buttons to create a codespace](../../../translated_images/zh-TW/who-will-pay.4c0609b1c7780f44.webp)

✅ 會打開瀏覽器中的 VS Code 視窗，並開始建立開發容器。
第一次使用約需 **~2 分鐘**。

## 3. 新增你的 API 金鑰（安全方式）

### 選項 A Codespaces Secrets — 推薦

1. ⚙️ 齒輪圖示 -> 命令面板 -> Codespaces : Manage user secret -> 新增私密資料。
2. 名稱：OPENAI_API_KEY
3. 值：貼上你的金鑰 → 新增私密資料

就這樣—我們的程式碼會自動使用它。

### 選項 B .env 檔案（如果你真的需要）

```bash
cp .env.copy .env
code .env         # 填寫 OPENAI_API_KEY=你的金鑰在此
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->