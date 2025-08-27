<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T14:30:10+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "zh"
}
-->
# 云端设置 ☁️ – GitHub Codespaces

**如果你不想在本地安装任何东西，请使用本指南。**  
Codespaces 为你提供了一个免费的、基于浏览器的 VS Code 实例，所有依赖都已预装。

---

## 1.  为什么选择 Codespaces？

| 优势 | 对你的意义 |
|---------|----------------------|
| ✅ 零安装 | 可在 Chromebook、iPad、学校机房电脑等设备上使用 |
| ✅ 预构建开发容器 | 已内置 Python 3、Node.js、.NET、Java 等环境 |
| ✅ 免费额度 | 个人账户每月可获得 **120 核心小时 / 60 GB 小时** |

> 💡 **提示**  
> 通过**停止**或**删除**空闲的 codespace 来保持你的额度充足  
> （查看 ▸ 命令面板 ▸ *Codespaces: Stop Codespace*）。

---

## 2.  创建 Codespace（一步到位）

1. **Fork** 此仓库（右上角的 **Fork** 按钮）。  
2. 在你的 fork 中，点击 **Code ▸ Codespaces ▸ Create codespace on main**。  
   ![显示创建 codespace 按钮的对话框](../../../00-course-setup/images/who-will-pay.webp)

✅ 浏览器会打开 VS Code 窗口，并开始构建开发容器。
首次启动大约需要 **2 分钟**。

## 3. 添加你的 API 密钥（安全方式）

### 方案 A Codespaces Secrets — 推荐

1. ⚙️ 齿轮图标 -> 命令面板 -> Codespaces : Manage user secret -> Add a new secret。
2. 名称：OPENAI_API_KEY
3. 值：粘贴你的密钥 → Add secret

就这样——我们的代码会自动读取它。

### 方案 B .env 文件（如果你确实需要）

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。我们尽力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文件应视为权威来源。对于关键信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。