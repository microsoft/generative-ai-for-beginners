<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T09:02:52+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "br"
}
-->
# Configure seu ambiente de desenvolvimento

Configuramos este repositório e curso com um [container de desenvolvimento](https://containers.dev?WT.mc_id=academic-105485-koreyst) que possui um runtime Universal que pode suportar desenvolvimento em Python3, .NET, Node.js e Java. A configuração relacionada é definida no arquivo `devcontainer.json` localizado na pasta `.devcontainer/` na raiz deste repositório.

Para ativar o container de desenvolvimento, inicie-o no [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (para um runtime hospedado na nuvem) ou no [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (para um runtime hospedado em dispositivo local). Leia [esta documentação](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) para mais detalhes sobre como os containers de desenvolvimento funcionam dentro do VS Code.

> [!TIP]  
> Recomendamos usar o GitHub Codespaces para um início rápido com mínimo esforço. Ele fornece uma [cota de uso gratuito](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) generosa para contas pessoais. Configure [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) para parar ou excluir codespaces inativos e maximizar seu uso de cota.


## 1. Executando Tarefas

Cada aula terá tarefas _opcionais_ que podem ser fornecidas em uma ou mais linguagens de programação, incluindo: Python, .NET/C#, Java e JavaScript/TypeScript. Esta seção fornece orientações gerais relacionadas à execução dessas tarefas.

### 1.1 Tarefas de Python

As tarefas de Python são fornecidas como aplicativos (arquivos `.py`) ou notebooks Jupyter (arquivos `.ipynb`).
- Para executar o notebook, abra-o no Visual Studio Code e clique em _Select Kernel_ (no canto superior direito) e selecione a opção padrão Python 3 exibida. Agora você pode clicar em _Run All_ para executar o notebook.
- Para executar aplicativos Python a partir da linha de comando, siga as instruções específicas da tarefa para garantir que você selecione os arquivos corretos e forneça os argumentos necessários.

## 2. Configurando Provedores

As tarefas **podem** também ser configuradas para funcionar contra uma ou mais implantações de Modelos de Linguagem de Grande Escala (LLM) através de um provedor de serviços suportado como OpenAI, Azure ou Hugging Face. Esses provedores oferecem um _endpoint hospedado_ (API) que podemos acessar programaticamente com as credenciais corretas (chave de API ou token). Neste curso, discutimos esses provedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com modelos diversos incluindo a série GPT principal.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco em prontidão empresarial.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos de código aberto e servidor de inferência.

**Você precisará usar suas próprias contas para esses exercícios**. As tarefas são opcionais, então você pode escolher configurar um, todos - ou nenhum - dos provedores com base em seus interesses. Algumas orientações para inscrição:

| Inscrição | Custo | Chave de API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Baseado em Projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sem Código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Múltiplos Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Início Rápido SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Início Rápido Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Deve Aplicar Antecipadamente Para Acesso](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes provedores. As tarefas que exigem um provedor específico conterão uma destas tags em seu nome de arquivo:
 - `aoai` - requer endpoint e chave do Azure OpenAI
 - `oai` - requer endpoint e chave do OpenAI
 - `hf` - requer token do Hugging Face

Você pode configurar um, nenhum ou todos os provedores. As tarefas relacionadas simplesmente apresentarão erro na ausência de credenciais.

###  2.1. Criar arquivo `.env`

Assumimos que você já leu as orientações acima e se inscreveu com o provedor relevante, e obteve as credenciais de autenticação necessárias (API_KEY ou token). No caso do Azure OpenAI, assumimos que você também tem uma implantação válida de um Serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implantado para conclusão de chat.

O próximo passo é configurar suas **variáveis de ambiente locais** da seguinte forma:


1. Procure na pasta raiz um arquivo `.env.copy` que deve ter conteúdos como este:

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

2. Copie esse arquivo para `.env` usando o comando abaixo. Este arquivo é _gitignore-d_, mantendo segredos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os placeholders do lado direito do `=`) conforme descrito na próxima seção.

3. (Opção) Se você usar o GitHub Codespaces, você tem a opção de salvar variáveis de ambiente como _segredos do Codespaces_ associados a este repositório. Nesse caso, você não precisará configurar um arquivo .env local. **No entanto, observe que esta opção funciona apenas se você usar o GitHub Codespaces.** Você ainda precisará configurar o arquivo .env se usar o Docker Desktop.


### 2.2. Preencher arquivo `.env`

Vamos dar uma olhada rápida nos nomes das variáveis para entender o que elas representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do usuário que você configurou em seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço para endpoints não-Azure OpenAI |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para usar esse serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implantado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implantação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implantação do modelo de _text embeddings_ |
| | |

Nota: As duas últimas variáveis do Azure OpenAI refletem um modelo padrão para conclusão de chat (geração de texto) e busca vetorial (embeddings), respectivamente. Instruções para configurá-las serão definidas nas tarefas relevantes.


### 2.3 Configurar Azure: Do Portal

Os valores do endpoint e da chave do Azure OpenAI serão encontrados no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), então vamos começar por lá.

1. Acesse o [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clique na opção **Keys and Endpoint** na barra lateral (menu à esquerda).
1. Clique em **Show Keys** - você deve ver o seguinte: KEY 1, KEY 2 e Endpoint.
1. Use o valor KEY 1 para AZURE_OPENAI_API_KEY
1. Use o valor do Endpoint para AZURE_OPENAI_ENDPOINT

Em seguida, precisamos dos endpoints para os modelos específicos que implantamos.

1. Clique na opção **Model deployments** na barra lateral (menu à esquerda) para o recurso Azure OpenAI.
1. Na página de destino, clique em **Manage Deployments**

Isso levará você ao site do Azure OpenAI Studio, onde encontraremos os outros valores conforme descrito abaixo.

### 2.4 Configurar Azure: Do Studio

1. Navegue até [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do seu recurso** conforme descrito acima.
1. Clique na aba **Deployments** (barra lateral, à esquerda) para visualizar os modelos atualmente implantados.
1. Se o modelo desejado não estiver implantado, use **Create new deployment** para implantá-lo.
1. Você precisará de um modelo de _geração de texto_ - recomendamos: **gpt-35-turbo**
1. Você precisará de um modelo de _text-embedding_ - recomendamos **text-embedding-ada-002**

Agora atualize as variáveis de ambiente para refletir o nome de _Implantação_ usado. Isso normalmente será o mesmo que o nome do modelo, a menos que você o tenha alterado explicitamente. Então, como exemplo, você pode ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Não se esqueça de salvar o arquivo .env quando terminar**. Agora você pode sair do arquivo e retornar às instruções para executar o notebook.

### 2.5 Configurar OpenAI: Do Perfil

Sua chave de API OpenAI pode ser encontrada em sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se você não tiver uma, pode se inscrever para uma conta e criar uma chave de API. Depois de ter a chave, você pode usá-la para preencher a variável `OPENAI_API_KEY` no arquivo `.env`.

### 2.6 Configurar Hugging Face: Do Perfil

Seu token Hugging Face pode ser encontrado em seu perfil em [Tokens de Acesso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não publique ou compartilhe isso publicamente. Em vez disso, crie um novo token para uso neste projeto e copie-o para o arquivo `.env` na variável `HUGGING_FACE_API_KEY`. _Nota:_ Este tecnicamente não é uma chave de API, mas é usado para autenticação, então estamos mantendo essa convenção de nomenclatura para consistência.

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.