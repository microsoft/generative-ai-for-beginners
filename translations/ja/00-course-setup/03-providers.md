<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T13:43:15+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "ja"
}
-->
# LLMプロバイダーの選択と設定 🔑

課題は、OpenAI、Azure、Hugging Faceなどのサポートされているサービスプロバイダーを通じて、1つ以上の大規模言語モデル（LLM）展開に対して動作するように設定することも**可能**です。これらは、適切な認証情報（APIキーまたはトークン）を使ってプログラム的にアクセスできる_ホストされたエンドポイント_（API）を提供します。このコースでは、以下のプロバイダーについて説明します：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) は、コアのGPTシリーズを含む多様なモデルを提供。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) は、エンタープライズ対応に重点を置いたOpenAIモデル。
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) は、オープンソースモデルと推論サーバーを提供。

**これらの演習にはご自身のアカウントを使用する必要があります**。課題は任意なので、興味に応じて1つ、すべて、またはどれも設定しないことができます。サインアップのためのガイダンスは以下の通りです：

| サインアップ | 料金 | APIキー | プレイグラウンド | コメント |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [料金](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [プロジェクトベース](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ノーコード、Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 複数モデル利用可能 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [料金](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDKクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [スタジオクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [アクセスには事前申請が必要](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [料金](https://huggingface.co/pricing) | [アクセストークン](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatはモデルが限定的](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

以下の指示に従って、このリポジトリを異なるプロバイダーで使用するために_設定_してください。特定のプロバイダーを必要とする課題は、ファイル名に以下のタグのいずれかが含まれます：

- `aoai` - Azure OpenAIのエンドポイントとキーが必要
- `oai` - OpenAIのエンドポイントとキーが必要
- `hf` - Hugging Faceのトークンが必要

1つ、またはすべて、あるいはどれも設定可能です。関連する課題は認証情報が不足しているとエラーになります。

## `.env`ファイルの作成

上記のガイダンスを読み、該当するプロバイダーにサインアップし、必要な認証情報（API_KEYまたはトークン）を取得済みであることを前提とします。Azure OpenAIの場合は、少なくとも1つのGPTモデルがチャット完了用に展開されたAzure OpenAIサービス（エンドポイント）が有効であることも前提とします。

次のステップは、**ローカル環境変数**を以下のように設定することです：

1. ルートフォルダーにある`.env.copy`ファイルを探します。内容は以下のようになっています：

   ```bash
   # OpenAI プロバイダー
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # デフォルトが設定されています！
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 下記コマンドでそのファイルを`.env`にコピーします。このファイルは_gitignore_されており、秘密情報を安全に保ちます。

   ```bash
   cp .env.copy .env
   ```

3. 次のセクションで説明するように、値を入力してください（`=`の右側のプレースホルダーを置き換えます）。

4. （オプション）GitHub Codespacesを使用している場合、このリポジトリに関連付けられた_Codespacesシークレット_として環境変数を保存することもできます。その場合、ローカルの.envファイルを設定する必要はありません。**ただし、このオプションはGitHub Codespacesを使用している場合のみ有効です。** Docker Desktopを使用している場合は、引き続き.envファイルの設定が必要です。

## `.env`ファイルの内容

変数名が何を表しているか簡単に見てみましょう：

| 変数名  | 説明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | プロファイルで設定したユーザーアクセストークン |
| OPENAI_API_KEY | 非Azure OpenAIエンドポイント用の認証キー |
| AZURE_OPENAI_API_KEY | Azure OpenAIサービス用の認証キー |
| AZURE_OPENAI_ENDPOINT | Azure OpenAIリソースの展開済みエンドポイント |
| AZURE_OPENAI_DEPLOYMENT | _テキスト生成_モデルの展開エンドポイント |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _テキスト埋め込み_モデルの展開エンドポイント |
| | |

注：最後の2つのAzure OpenAI変数は、それぞれチャット完了（テキスト生成）とベクトル検索（埋め込み）用のデフォルトモデルを反映しています。設定方法は関連課題で説明されます。

## Azureの設定：ポータルから

Azure OpenAIのエンドポイントとキーは[Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)で確認できるので、まずはそこから始めましょう。

1. [Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)にアクセス
1. サイドバー（左メニュー）の**キーとエンドポイント**をクリック
1. **キーの表示**をクリックすると、KEY 1、KEY 2、エンドポイントが表示されます
1. KEY 1の値をAZURE_OPENAI_API_KEYに使用
1. エンドポイントの値をAZURE_OPENAI_ENDPOINTに使用

次に、展開した特定モデルのエンドポイントを取得します。

1. Azure OpenAIリソースのサイドバー（左メニュー）で**モデル展開**をクリック
1. 表示されたページで**展開の管理**をクリック

これによりAzure OpenAI Studioのウェブサイトに移動し、以下で説明する他の値を確認できます。

## Azureの設定：Studioから

1. 上記のように[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)に**リソースから**アクセス
1. サイドバー（左）で**展開**タブをクリックし、現在展開されているモデルを表示
1. 希望のモデルが展開されていなければ、**新しい展開の作成**で展開
1. _テキスト生成_モデルが必要です - 推奨は **gpt-35-turbo**
1. _テキスト埋め込み_モデルが必要です - 推奨は **text-embedding-ada-002**

環境変数を、使用した_展開名_に合わせて更新します。通常はモデル名と同じですが、明示的に変更している場合はその名前を使います。例としては：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**設定後は.envファイルを保存するのを忘れないでください**。ファイルを閉じてノートブック実行の指示に戻れます。

## OpenAIの設定：プロフィールから

OpenAIのAPIキーは[OpenAIアカウント](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)で確認できます。アカウントがなければサインアップしてAPIキーを作成してください。取得したキーを`.env`ファイルの`OPENAI_API_KEY`変数に設定します。

## Hugging Faceの設定：プロフィールから

Hugging Faceのトークンはプロフィールの[アクセストークン](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)で確認できます。これらを公開したり共有したりしないでください。代わりに、このプロジェクト用に新しいトークンを作成し、`.env`ファイルの`HUGGING_FACE_API_KEY`変数にコピーしてください。_注意：_ これは技術的にはAPIキーではありませんが、認証に使うため一貫性を保つためにこの名前を使っています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->