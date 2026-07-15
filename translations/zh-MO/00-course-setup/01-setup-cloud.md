# 雲端設定 ☁️ – GitHub Codespaces

**如果你不想在本地安裝任何東西，請使用此指南。**  
Codespaces 為你提供一個免費的瀏覽器版 VS Code 實例，內置所有依賴。

---

## 1. 為什麼選擇 Codespaces？

| 優點 | 對你的意義 |
|---------|----------------------|
| ✅ 零安裝 | 適用於 Chromebook、iPad、學校實驗室電腦… |
| ✅ 預建開發容器 | 已包含 Python 3、Node.js、.NET、Java |
| ✅ 免費配額 | 個人帳號每月可獲得 **120 核心小時 / 60 GB 小時** |

> 💡 <strong>提示</strong>  
> 保持配額健康，記得 <strong>停止</strong> 或 <strong>刪除</strong> 閒置的 codespaces  
> (查看 ▸ 命令面板 ▸ *Codespaces: Stop Codespace*)。

---

## 2. 創建 Codespace（一步到位）

1. **Fork** 此倉庫（右上角 **Fork** 按鈕）。  
2. 在你的 fork 中，點擊 **Code ▸ Codespaces ▸ Create codespace on main**。  
   ![Dialog showing buttons to create a codespace](../../../translated_images/zh-MO/who-will-pay.4c0609b1c7780f44.webp)

✅ 一個瀏覽器版的 VS Code 窗口會打開，並開始構建開發容器。
首次大約需要 **~2 分鐘**。

## 3. 添加你的 API 鍵（安全方法）

### 選項 A Codespaces Secrets — 推薦

1. ⚙️ 齒輪圖示 -> 命令面板 -> Codespaces : 管理使用者密鑰 -> 新增密鑰。
2. 名稱：OPENAI_API_KEY
3. 數值：貼上你的鑰匙 → 新增密鑰

就這樣—我們的程式碼會自動讀取它。

### 選項 B .env 檔案（如你真的需要）

```bash
cp .env.copy .env
code .env         # 填寫 OPENAI_API_KEY=your_key_here
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->