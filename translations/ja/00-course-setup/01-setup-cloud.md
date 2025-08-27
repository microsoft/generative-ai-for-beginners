<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T15:04:11+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "ja"
}
-->
# クラウドセットアップ ☁️ – GitHub Codespaces

**何もローカルにインストールしたくない場合はこのガイドを使ってください。**  
Codespacesは、すべての依存関係が事前インストールされた、無料のブラウザベースのVS Code環境を提供します。

---

## 1. なぜCodespaces？

| 利点 | あなたにとっての意味 |
|------|----------------------|
| ✅ インストール不要 | Chromebook、iPad、学校のPCなどでも動作 |
| ✅ 開発コンテナが事前構築済み | Python 3、Node.js、.NET、Javaがすでに入っている |
| ✅ 無料枠あり | 個人アカウントは**月120コア時間 / 60GB時間**まで無料 |

> 💡 **ヒント**  
> 使っていないcodespaceは**停止**または**削除**して、無料枠を節約しましょう  
> （表示 ▸ コマンドパレット ▸ *Codespaces: Stop Codespace*）。

---

## 2. Codespaceを作成する（ワンクリック）

1. このリポジトリを**フォーク**します（右上の**Fork**ボタン）。  
2. フォークしたリポジトリで、**Code ▸ Codespaces ▸ Create codespace on main**をクリック。  
   ![Codespace作成ボタンのダイアログ](../../../00-course-setup/images/who-will-pay.webp)

✅ ブラウザのVS Codeウィンドウが開き、開発コンテナの構築が始まります。  
初回は**約2分**かかります。

## 3. APIキーを追加する（安全な方法）

### オプションA Codespaces Secrets — 推奨

1. ⚙️ ギアアイコン -> コマンドパレット -> Codespaces : Manage user secret -> Add a new secret
2. 名前: OPENAI_API_KEY
3. 値: キーを貼り付け → Add secret

これで完了です—コードが自動的にキーを認識します。

### オプションB .envファイル（どうしても必要な場合）

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**免責事項**：  
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合があります。原文（元の言語の文書）が正式な情報源として扱われるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤認についても、当方は責任を負いかねます。