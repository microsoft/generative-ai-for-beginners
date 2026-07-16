# クラウドセットアップ ☁️ – GitHub Codespaces

**ローカルに何もインストールしたくない場合は、このガイドをお使いください。**  
Codespacesは、すべての依存関係が事前にインストールされた無料のブラウザベースのVS Codeインスタンスを提供します。

---

## 1. なぜCodespaces?

| 利点 | あなたにとっての意味 |
|---------|----------------------|
| ✅ インストール不要 | Chromebook、iPad、学校のラボPCでも動作します… |
| ✅ 事前構築された開発コンテナ | Python 3、Node.js、.NET、Javaがすでに含まれています |
| ✅ 無料のクォータ | 個人アカウントは<strong>月あたり120コア時間 / 60 GB時間</strong>を取得します |

> 💡 <strong>ヒント</strong>  
> クォータを健全に保つために、アイドル状態のcodespacesは<strong>停止</strong>または<strong>削除</strong>してください  
> (表示 ▸ コマンドパレット ▸ *Codespaces: Stop Codespace*)。

---

## 2. Codespace の作成（ワンクリック）

1. このリポジトリを **Fork** します（右上の **Fork** ボタン）。  
2. フォークしたリポジトリで、**Code ▸ Codespaces ▸ Create codespace on main** をクリックします。  
   ![コードスペースの作成ボタンを示すダイアログ](../../../translated_images/ja/who-will-pay.4c0609b1c7780f44.webp)

✅ ブラウザのVS Codeウィンドウが開き、開発コンテナのビルドが開始されます。
初回は<strong>約2分</strong>かかります。

## 3. APIキーの追加（安全な方法）

### オプションA Codespaces Secrets — 推奨

1. ⚙️ ギアアイコン -> コマンドパレット -> Codespaces : ユーザーシークレットの管理 -> 新しいシークレットを追加。
2. 名前: OPENAI_API_KEY
3. 値: キーを貼り付け → シークレットを追加

これで完了です—コードが自動的に取得します。

### オプションB .envファイル（どうしても必要な場合）

```bash
cp .env.copy .env
code .env         # OPENAI_API_KEY=your_key_here を入力してください
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->