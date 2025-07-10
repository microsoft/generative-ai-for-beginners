<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:28:45+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "br"
}
-->
# Configure Seu Ambiente de Desenvolvimento

Configuramos este repositório e curso com um [container de desenvolvimento](https://containers.dev?WT.mc_id=academic-105485-koreyst) que possui um runtime Universal capaz de suportar desenvolvimento em Python3, .NET, Node.js e Java. A configuração relacionada está definida no arquivo `devcontainer.json` localizado na pasta `.devcontainer/` na raiz deste repositório.

Para ativar o container de desenvolvimento, inicie-o no [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (para um runtime hospedado na nuvem) ou no [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (para um runtime hospedado localmente). Leia [esta documentação](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) para mais detalhes sobre como containers de desenvolvimento funcionam dentro do VS Code.

> [!TIP]  
> Recomendamos usar o GitHub Codespaces para um início rápido com esforço mínimo. Ele oferece uma generosa [cota de uso gratuita](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) para contas pessoais. Configure [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) para parar ou excluir codespaces inativos e assim maximizar o uso da sua cota.

## 1. Executando as Tarefas

Cada aula terá tarefas _opcionais_ que podem ser fornecidas em uma ou mais linguagens de programação, incluindo: Python, .NET/C#, Java e JavaScript/TypeScript. Esta seção oferece orientações gerais relacionadas à execução dessas tarefas.

### 1.1 Tarefas em Python

As tarefas em Python são fornecidas como aplicações (`.py`) ou notebooks Jupyter (`.ipynb`).  
- Para executar o notebook, abra-o no Visual Studio Code, clique em _Select Kernel_ (no canto superior direito) e selecione a opção padrão Python 3 exibida. Agora você pode usar _Run All_ para executar o notebook.  
- Para executar aplicações Python via linha de comando, siga as instruções específicas da tarefa para garantir que você selecione os arquivos corretos e forneça os argumentos necessários.

## 2. Configurando os Providers

As tarefas **podem** também ser configuradas para funcionar com uma ou mais implantações de Large Language Models (LLM) através de um provedor de serviço suportado como OpenAI, Azure ou Hugging Face. Estes fornecem um _endpoint hospedado_ (API) que podemos acessar programaticamente com as credenciais corretas (chave API ou token). Neste curso, discutimos os seguintes providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com diversos modelos, incluindo a série principal GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco em prontidão empresarial.  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos open-source e servidor de inferência.

**Você precisará usar suas próprias contas para esses exercícios**. As tarefas são opcionais, então você pode escolher configurar um, todos ou nenhum dos providers conforme seu interesse. Algumas orientações para cadastro:

| Cadastro | Custo | Chave API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Baseado em projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sem código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Vários Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [É necessário solicitar acesso antecipadamente](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes providers. Tarefas que exigem um provider específico terão uma destas tags no nome do arquivo:  
 - `aoai` - requer endpoint e chave Azure OpenAI  
 - `oai` - requer endpoint e chave OpenAI  
 - `hf` - requer token Hugging Face

Você pode configurar um, nenhum ou todos os providers. Tarefas relacionadas simplesmente apresentarão erro se as credenciais estiverem ausentes.

###  2.1. Criar arquivo `.env`

Assumimos que você já leu as orientações acima, se cadastrou no provider relevante e obteve as credenciais de autenticação necessárias (API_KEY ou token). No caso do Azure OpenAI, assumimos também que você possui uma implantação válida de um serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implantado para chat completion.

O próximo passo é configurar suas **variáveis de ambiente locais** da seguinte forma:

1. Procure na pasta raiz um arquivo `.env.copy` que deve conter algo assim:

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

2. Copie esse arquivo para `.env` usando o comando abaixo. Este arquivo está _gitignore-d_, mantendo os segredos protegidos.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os placeholders à direita do `=`) conforme descrito na próxima seção.

3. (Opcional) Se você usar GitHub Codespaces, tem a opção de salvar variáveis de ambiente como _segredos do Codespaces_ associados a este repositório. Nesse caso, não será necessário configurar um arquivo .env local. **Porém, note que essa opção funciona apenas se você usar GitHub Codespaces.** Você ainda precisará configurar o arquivo .env se usar Docker Desktop.

### 2.2. Preencher arquivo `.env`

Vamos dar uma olhada rápida nos nomes das variáveis para entender o que representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do usuário que você configurou no seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço em endpoints OpenAI não Azure |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implantado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implantação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implantação do modelo de _embeddings de texto_ |
| | |

Observação: As duas últimas variáveis do Azure OpenAI refletem um modelo padrão para chat completion (geração de texto) e busca vetorial (embeddings), respectivamente. As instruções para configurá-las serão definidas nas tarefas relevantes.

### 2.3 Configurar Azure: Pelo Portal

Os valores do endpoint e da chave do Azure OpenAI podem ser encontrados no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), então vamos começar por lá.

1. Acesse o [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Clique na opção **Keys and Endpoint** na barra lateral (menu à esquerda).  
1. Clique em **Show Keys** - você verá o seguinte: KEY 1, KEY 2 e Endpoint.  
1. Use o valor da KEY 1 para AZURE_OPENAI_API_KEY  
1. Use o valor do Endpoint para AZURE_OPENAI_ENDPOINT

Agora, precisamos dos endpoints para os modelos específicos que implantamos.

1. Clique na opção **Model deployments** na barra lateral (menu à esquerda) do recurso Azure OpenAI.  
1. Na página de destino, clique em **Manage Deployments**

Isso levará você ao site do Azure OpenAI Studio, onde encontraremos os outros valores conforme descrito abaixo.

### 2.4 Configurar Azure: Pelo Studio

1. Navegue até o [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do seu recurso**, conforme descrito acima.  
1. Clique na aba **Deployments** (barra lateral, à esquerda) para ver os modelos atualmente implantados.  
1. Se o modelo desejado não estiver implantado, use **Create new deployment** para implantá-lo.  
1. Você precisará de um modelo de _text-generation_ - recomendamos: **gpt-35-turbo**  
1. Você precisará de um modelo de _text-embedding_ - recomendamos **text-embedding-ada-002**

Agora atualize as variáveis de ambiente para refletir o _nome da implantação_ usado. Normalmente será o mesmo nome do modelo, a menos que você tenha alterado explicitamente. Por exemplo, você pode ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Não esqueça de salvar o arquivo .env ao terminar**. Agora você pode fechar o arquivo e voltar às instruções para executar o notebook.

### 2.5 Configurar OpenAI: Pelo Perfil

Sua chave API do OpenAI pode ser encontrada na sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se você não tiver uma, pode se cadastrar e criar uma chave API. Depois de obter a chave, use-a para preencher a variável `OPENAI_API_KEY` no arquivo `.env`.

### 2.6 Configurar Hugging Face: Pelo Perfil

Seu token Hugging Face pode ser encontrado no seu perfil em [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não publique ou compartilhe esses tokens publicamente. Em vez disso, crie um token novo para uso neste projeto e copie-o para o arquivo `.env` na variável `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente, isso não é uma chave API, mas é usado para autenticação, então mantemos essa nomenclatura para consistência.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.