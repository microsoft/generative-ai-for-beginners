<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T15:04:45+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "ja"
}
-->
# LLMプロバイダーの選択と設定 🔑

課題は、OpenAI、Azure、Hugging Faceなどのサポートされているサービスプロバイダーを通じて、1つ以上の大規模言語モデル（LLM）デプロイメントで動作するように設定することもできます。これらは、適切な認証情報（APIキーやトークン）を使ってプログラムからアクセスできる_ホスト型エンドポイント_（API）を提供します。本コースでは、以下のプロバイダーについて説明します。

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)：GPTシリーズをはじめとする多様なモデルを提供
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)：エンタープライズ向けに特化したOpenAIモデル
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)：オープンソースモデルや推論サーバー

**これらの演習を行うには、ご自身のアカウントが必要です。** 課題は任意なので、興味に応じて1つだけ、すべて、またはどれも設定しなくても構いません。サインアップの参考情報は以下の通りです。

| サインアップ | 料金 | APIキー | プレイグラウンド | コメント |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [料金表](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [プロジェクト単位](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ノーコード・Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 複数モデル利用可 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [料金表](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDKクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studioクイックスタート](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [事前申請が必要](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [料金表](https://huggingface.co/pricing) | [アクセストークン](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatは利用できるモデルが限定的](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

以下の手順に従って、このリポジトリを各プロバイダーで使えるように_設定_してください。特定のプロバイダーが必要な課題には、ファイル名に次のいずれかのタグが含まれています。

- `aoai` - Azure OpenAIのエンドポイントとキーが必要
- `oai` - OpenAIのエンドポイントとキーが必要
- `hf` - Hugging Faceのトークンが必要

どれか1つ、すべて、またはどれも設定しなくても構いません。関連する課題は、認証情報がない場合はエラーになります。

## `.env`ファイルの作成

上記の案内を読んで、該当するプロバイダーにサインアップし、必要な認証情報（API_KEYやトークン）を取得していることを前提とします。Azure OpenAIの場合は、少なくとも1つのGPTモデルがチャット補完用にデプロイされたAzure OpenAIサービス（エンドポイント）が有効であることも前提とします。

次のステップは、**ローカル環境変数**を以下のように設定することです。

1. ルートフォルダーにある`.env.copy`ファイルを探してください。内容は次のようになっています。

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 下記のコマンドでそのファイルを`.env`にコピーします。このファイルは_gitignore_されているため、秘密情報が安全に保たれます。

   ```bash
   cp .env.copy .env
   ```

3. 次のセクションの説明に従い、値（`=`の右側のプレースホルダー）を入力してください。

4. （オプション）GitHub Codespacesを使う場合は、環境変数をこのリポジトリに紐づく_Codespaces secrets_として保存することもできます。その場合、ローカルの.envファイルを設定する必要はありません。**ただし、この方法はGitHub Codespacesを使う場合のみ有効です。** Docker Desktopを使う場合は、.envファイルの設定が必要です。

## `.env`ファイルの値を入力

変数名が何を表しているか、簡単に確認しましょう。

| 変数  | 説明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | プロフィールで設定したユーザーアクセストークン |
| OPENAI_API_KEY | 非Azure OpenAIエンドポイント用の認証キー |
| AZURE_OPENAI_API_KEY | Azure OpenAIサービス用の認証キー |
| AZURE_OPENAI_ENDPOINT | Azure OpenAIリソースのデプロイ済みエンドポイント |
| AZURE_OPENAI_DEPLOYMENT | _テキスト生成_モデルのデプロイメント名 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _テキスト埋め込み_モデルのデプロイメント名 |
| | |

※最後の2つのAzure OpenAI変数は、それぞれチャット補完（テキスト生成）とベクトル検索（埋め込み）のデフォルトモデルを表します。設定方法は該当する課題で案内します。

## Azureの設定：ポータルから

Azure OpenAIのエンドポイントとキーは[Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)で確認できます。手順は以下の通りです。

1. [Azureポータル](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)にアクセス
1. サイドバー（左メニュー）から**キーとエンドポイント**をクリック
1. **キーの表示**をクリックすると、KEY 1、KEY 2、エンドポイントが表示されます
1. AZURE_OPENAI_API_KEYにはKEY 1の値を使用
1. AZURE_OPENAI_ENDPOINTにはエンドポイントの値を使用

次に、デプロイした特定モデルのエンドポイントが必要です。

1. Azure OpenAIリソースのサイドバー（左メニュー）から**モデルのデプロイ**をクリック
1. 遷移先ページで**デプロイの管理**をクリック

これでAzure OpenAI StudioのWebサイトに移動し、以下の値を確認できます。

## Azureの設定：Studioから

1. 上記の手順で[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)に**リソースから**アクセス
1. サイドバー（左）で**デプロイ**タブをクリックし、現在デプロイされているモデルを確認
1. 希望するモデルがデプロイされていない場合は、**新しいデプロイの作成**でデプロイ
1. _テキスト生成_モデルが必要です（推奨：**gpt-35-turbo**）
1. _テキスト埋め込み_モデルが必要です（推奨：**text-embedding-ada-002**）

環境変数には、_デプロイメント名_を入力してください。特に変更していなければ、モデル名と同じになっているはずです。例として、次のようになります。

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**.envファイルの保存を忘れずに！** 設定が終わったらファイルを閉じ、ノートブック実行の手順に戻ってください。

## OpenAIの設定：プロフィールから

OpenAIのAPIキーは[OpenAIアカウント](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)で確認できます。まだ持っていない場合は、アカウントを作成してAPIキーを発行してください。取得したキーを`.env`ファイルの`OPENAI_API_KEY`変数に入力します。

## Hugging Faceの設定：プロフィールから

Hugging Faceのトークンは、プロフィールの[アクセストークン](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)で確認できます。これらを公開したり共有したりしないでください。このプロジェクト用に新しいトークンを作成し、`.env`ファイルの`HUGGING_FACE_API_KEY`変数にコピーしてください。_注：_ これは厳密にはAPIキーではありませんが、認証に使うため、命名規則を統一しています。

---

**免責事項**：  
本書類はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合があります。原文（元の言語の文書）が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用によって生じたいかなる誤解や誤認についても、当方は責任を負いかねます。