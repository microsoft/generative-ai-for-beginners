# 云端设置 ☁️ – GitHub Codespaces

**如果你不想在本地安装任何东西，请使用本指南。**  
Codespaces 为你提供一个免费的、基于浏览器的 VS Code 实例，所有依赖项已预装。

---

## 1. 为什么选择 Codespaces？

| 优势 | 对你的意义 |
|---------|----------------------|
| ✅ 零安装 | 适用于 Chromebook、iPad、学校实验室电脑… |
| ✅ 预构建开发容器 | 内置 Python 3、Node.js、.NET、Java |
| ✅ 免费配额 | 个人账号每月获得 **120 核小时 / 60 GB 小时** |

> 💡 <strong>提示</strong>  
> 通过<strong>停止</strong>或<strong>删除</strong>空闲的 codespaces 保持配额健康  
> （查看 ▸ 命令面板 ▸ *Codespaces: Stop Codespace*）。

---

## 2. 创建 Codespace（一步完成）

1. **Fork** 这个仓库（右上角 **Fork** 按钮）。  
2. 在你的 Fork 中，点击 **Code ▸ Codespaces ▸ Create codespace on main**。  
   ![Dialog showing buttons to create a codespace](../../../translated_images/zh-CN/who-will-pay.4c0609b1c7780f44.webp)

✅ 一个浏览器 VS Code 窗口打开，开发容器开始构建。
第一次大约需要 **~2 分钟**。

## 3. 添加你的 API 密钥（安全方式）

### 方案 A Codespaces Secrets — 推荐

1. ⚙️ 齿轮图标 -> 命令面板 -> Codespaces : Manage user secret -> 添加新的密钥。
2. 名称：OPENAI_API_KEY
3. 值：粘贴你的密钥 → 添加密钥

就这么简单——我们的代码会自动读取它。

### 方案 B .env 文件（如果你真的需要）

```bash
cp .env.copy .env
code .env         # 填写 OPENAI_API_KEY=your_key_here
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->