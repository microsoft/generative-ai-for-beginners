# 雲端設定 ☁️ – GitHub Codespaces

**如果你不想在本地安裝任何東西，請使用本指南。**  
Codespaces 提供免費的瀏覽器版 VS Code 實例，並預先安裝所有相依套件。

---

## 1. 為何選擇 Codespaces？

| 優點 | 對你的意義 |
|---------|----------------------|
| ✅ 無須安裝 | 適用於 Chromebook、iPad、校園實驗室電腦… |
| ✅ 預建開發容器 | Python 3、Node.js、.NET、Java 已內建 |
| ✅ 免費配額 | 個人帳戶每月享 **120 核心小時 / 60 GB 小時** |

> 💡 <strong>提示</strong>  
> 透過 <strong>停止</strong> 或 <strong>刪除</strong> 閒置的 codespaces，保持配額充足  
> （查看 ▸ 指令面板 ▸ *Codespaces: Stop Codespace*）。

---

## 2. 建立 Codespace（單擊完成）

1. **Fork** 這個倉庫（右上角的 **Fork** 按鈕）。  
2. 在你的 fork 中，點擊 **Code ▸ Codespaces ▸ 在 main 建立 codespace**。  
   ![Dialog showing buttons to create a codespace](../../../translated_images/zh-HK/who-will-pay.4c0609b1c7780f44.webp)

✅ 瀏覽器版 VS Code 視窗將打開，且開發容器開始建置。
第一次大約需要 **2 分鐘**。

## 3. 新增你的 API 金鑰（安全方式）

### 選項 A Codespaces Secrets — 推薦

1. ⚙️ 齒輪圖示 -> 指令面板 -> Codespaces : 管理使用者密碼 -> 新增密碼。
2. 名稱: OPENAI_API_KEY
3. 值: 貼上你的金鑰 → 新增密碼

完成了 — 我們的程式碼會自動讀取它。

### 選項 B .env 檔案（如果你真的需要）

```bash
cp .env.copy .env
code .env         # 填寫 OPENAI_API_KEY=你的金鑰
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->