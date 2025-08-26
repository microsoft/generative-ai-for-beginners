<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T14:37:29+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "mo"
}
-->
# 雲端設定 ☁️ – GitHub Codespaces

**如果你不想在本機安裝任何東西，請參考這份指南。**  
Codespaces 提供免費、基於瀏覽器的 VS Code 環境，所有相依套件都已預先安裝好。

---

## 1.  為什麼選擇 Codespaces？

| 優點 | 對你的好處 |
|------|------------|
| ✅ 免安裝 | Chromebook、iPad、學校電腦教室…都能用 |
| ✅ 預設開發容器 | 已內建 Python 3、Node.js、.NET、Java |
| ✅ 免費額度 | 個人帳號每月有 **120 核心小時 / 60 GB 小時** |

> 💡 **提示**  
> 保持額度充足，記得**停止**或**刪除**閒置的 codespace  
> （檢視 ▸ 指令面板 ▸ *Codespaces: Stop Codespace*）。

---

## 2.  建立 Codespace（只要一鍵）

1. **Fork** 這個 repo（右上角的 **Fork** 按鈕）。  
2. 在你的 fork 裡，點選 **Code ▸ Codespaces ▸ Create codespace on main**。  
   ![顯示建立 codespace 按鈕的對話框](../../../00-course-setup/images/who-will-pay.webp)

✅ 會自動開啟一個瀏覽器版 VS Code 視窗，並開始建置開發容器。
第一次大約需要 **2 分鐘**。

## 3. 加入你的 API 金鑰（安全做法）

### 選項 A Codespaces Secrets — 建議使用

1. ⚙️ 齒輪圖示 -> 指令面板 -> Codespaces : Manage user secret -> Add a new secret。
2. 名稱：OPENAI_API_KEY
3. 值：貼上你的金鑰 → Add secret

這樣就完成了—我們的程式會自動讀取。

### 選項 B .env 檔案（如果你真的需要）

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為最具權威性的來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。