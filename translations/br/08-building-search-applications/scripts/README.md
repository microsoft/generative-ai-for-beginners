<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T10:26:21+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "br"
}
-->
# Preparação de dados de transcrição

Os scripts de preparação de dados de transcrição baixam transcrições de vídeos do YouTube e as preparam para uso com o exemplo de Pesquisa Semântica com Embeddings e Funções do OpenAI.

Os scripts de preparação de dados de transcrição foram testados nas últimas versões do Windows 11, macOS Ventura e Ubuntu 22.04 (e superiores).

## Criar os recursos necessários do Azure OpenAI Service

> [!IMPORTANT]
> Sugerimos que você atualize o Azure CLI para a versão mais recente para garantir a compatibilidade com o OpenAI
> Veja [Documentação](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Crie um grupo de recursos

> [!NOTE]
> Para estas instruções, estamos usando o grupo de recursos chamado "semantic-video-search" no Leste dos EUA.
> Você pode mudar o nome do grupo de recursos, mas ao mudar a localização dos recursos,
> verifique a [tabela de disponibilidade de modelos](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Crie um recurso do Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Obtenha o endpoint e as chaves para uso nesta aplicação

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Implante os seguintes modelos:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

```console
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name gpt-35-turbo \
    --model-name gpt-35-turbo \
    --model-version "0613"  \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Software necessário

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ou superior

## Variáveis de ambiente

As seguintes variáveis de ambiente são necessárias para executar os scripts de preparação de dados de transcrição do YouTube.

### No Windows

Recomendamos adicionar as variáveis ao seu `usuário` environment variables.
`Iniciar Windows` > `Editar as variáveis de ambiente do sistema` > `Variáveis de Ambiente` > `Variáveis do usuário` for [USER] > `Novo`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### No Linux e macOS

Recomendamos adicionar as seguintes exportações ao seu arquivo `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalar as bibliotecas Python necessárias

1. Instale o [cliente git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) se ainda não estiver instalado.
1. A partir de uma janela do `Terminal`, clone o exemplo para a pasta de repositório de sua preferência.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navegue até a pasta `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Crie um ambiente virtual Python.

    No Windows:

    ```powershell
    python -m venv .venv
    ```

    No macOS e Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Ative o ambiente virtual Python.

   No Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   No macOS e Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Instale as bibliotecas necessárias.

   No Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   No macOS e Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Execute os scripts de preparação de dados de transcrição do YouTube

### No Windows

```powershell
.\transcripts_prepare.ps1
```

### No macOS e Linux

```bash
./transcripts_prepare.sh
```

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para alcançar precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.