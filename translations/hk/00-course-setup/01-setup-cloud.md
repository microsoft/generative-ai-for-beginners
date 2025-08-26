<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T14:46:56+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "hk"
}
-->
# 雲端設定 ☁️ – GitHub Codespaces

**如果你唔想喺本機安裝任何嘢，可以用呢個教學。**  
Codespaces 會俾你一個免費、用瀏覽器開嘅 VS Code，所有依賴都已經裝好。

---

## 1.  點解用 Codespaces？

| 優點 | 對你有咩意思 |
|------|--------------|
| ✅ 唔使安裝 | Chromebook、iPad、學校電腦都用得 |
| ✅ 已預設好開發環境 | Python 3、Node.js、.NET、Java 已經有齊 |
| ✅ 免費配額 | 個人帳戶每月有 **120 核心小時 / 60 GB 小時** |

> 💡 **提示**  
> 記住**停止**或者**刪除**冇用緊嘅 codespace，咁先唔會用晒配額  
> （檢視 ▸ 指令面板 ▸ *Codespaces: Stop Codespace*）。

---

## 2.  建立 Codespace（只需一 click）

1. **Fork** 呢個 repo（右上角 **Fork** 按鈕）。  
2. 喺你 fork 咗嘅 repo，撳 **Code ▸ Codespaces ▸ Create codespace on main**。  
   ![顯示建立 codespace 按鈕嘅對話框](../../../00-course-setup/images/who-will-pay.webp)

✅ 會自動開一個瀏覽器版 VS Code 視窗，開發環境會開始建構。
第一次大約要 **2 分鐘**。

## 3. 加入你嘅 API key（安全做法）

### 方法 A Codespaces Secrets — 推薦

1. ⚙️ 齒輪圖示 -> 指令面板 -> Codespaces : Manage user secret -> Add a new secret。
2. 名稱：OPENAI_API_KEY
3. 值：貼上你嘅 key → Add secret

搞掂—我哋嘅程式會自動搵到。

### 方法 B .env 檔案（如果你真係需要）

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**免責聲明**：  
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能會出現錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。如涉及重要資訊，建議尋求專業人手翻譯。本翻譯所引致的任何誤解或錯誤，我們概不負責。