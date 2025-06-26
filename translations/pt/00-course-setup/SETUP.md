<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:16:11+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "pt"
}
-->
# Configure o Seu Ambiente de Desenvolvimento

Configurámos este repositório e curso com um [contentor de desenvolvimento](https://containers.dev?WT.mc_id=academic-105485-koreyst) que tem um runtime universal que pode suportar desenvolvimento em Python3, .NET, Node.js e Java. A configuração relacionada está definida no ficheiro `devcontainer.json` localizado na pasta `.devcontainer/` na raiz deste repositório.

Para ativar o contentor de desenvolvimento, lance-o no [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (para um runtime hospedado na nuvem) ou no [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (para um runtime hospedado localmente). Leia [esta documentação](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) para mais detalhes sobre como os contentores de desenvolvimento funcionam dentro do VS Code.

> [!TIP]  
> Recomendamos usar o GitHub Codespaces para um início rápido com mínimo esforço. Oferece uma [quota de uso gratuita](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) generosa para contas pessoais. Configure [tempos limite](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) para parar ou eliminar codespaces inativos para maximizar o uso da sua quota.

## 1. Executando Tarefas

Cada lição terá tarefas _opcionais_ que podem ser fornecidas em uma ou mais linguagens de programação, incluindo: Python, .NET/C#, Java e JavaScript/TypeScript. Esta seção fornece orientações gerais relacionadas à execução dessas tarefas.

### 1.1 Tarefas em Python

As tarefas em Python são fornecidas como aplicações (ficheiros `.py`) ou notebooks Jupyter (ficheiros `.ipynb`).
- Para executar o notebook, abra-o no Visual Studio Code, clique em _Select Kernel_ (no canto superior direito) e selecione a opção padrão Python 3 mostrada. Agora pode clicar em _Run All_ para executar o notebook.
- Para executar aplicações Python a partir da linha de comando, siga as instruções específicas da tarefa para garantir que seleciona os ficheiros corretos e fornece os argumentos necessários.

## 2. Configurando Provedores

As tarefas **podem** também ser configuradas para funcionar contra uma ou mais implementações de Modelos de Linguagem Grande (LLM) através de um provedor de serviços suportado como OpenAI, Azure ou Hugging Face. Estes fornecem um _endpoint hospedado_ (API) que podemos acessar programaticamente com as credenciais corretas (chave API ou token). Neste curso, discutimos estes provedores:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com modelos diversos, incluindo a série principal GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco na prontidão empresarial.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos de código aberto e servidor de inferência.

**Você precisará usar suas próprias contas para estes exercícios**. As tarefas são opcionais, então pode escolher configurar um, todos - ou nenhum - dos provedores com base nos seus interesses. Algumas orientações para inscrição:

| Inscrição | Custo | Chave API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Baseado em Projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sem Código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Vários Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Início Rápido SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Início Rápido Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Deve Solicitar Acesso Antecipadamente](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes provedores. As tarefas que exigem um provedor específico conterão uma destas etiquetas no seu nome de ficheiro:
- `aoai` - requer endpoint Azure OpenAI, chave
- `oai` - requer endpoint OpenAI, chave
- `hf` - requer token Hugging Face

Pode configurar um, nenhum, ou todos os provedores. As tarefas relacionadas simplesmente darão erro por falta de credenciais.

### 2.1. Criar ficheiro `.env`

Assumimos que já leu as orientações acima e inscreveu-se no provedor relevante, obtendo as credenciais de autenticação necessárias (API_KEY ou token). No caso do Azure OpenAI, assumimos que também tem uma implementação válida de um Serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implementado para conclusão de chat.

O próximo passo é configurar as suas **variáveis de ambiente locais** da seguinte forma:

1. Procure na pasta raiz um ficheiro `.env.copy` que deve ter conteúdo semelhante a este:

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

2. Copie esse ficheiro para `.env` usando o comando abaixo. Este ficheiro é _gitignore-d_, mantendo os segredos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os espaços reservados no lado direito do `=`) conforme descrito na próxima seção.

3. (Opcional) Se usar o GitHub Codespaces, tem a opção de salvar variáveis de ambiente como _segredos de Codespaces_ associados a este repositório. Nesse caso, não precisará configurar um ficheiro .env local. **No entanto, note que esta opção funciona apenas se usar o GitHub Codespaces.** Ainda precisará configurar o ficheiro .env se usar o Docker Desktop em vez disso.

### 2.2. Preencher ficheiro `.env`

Vamos dar uma olhada rápida nos nomes das variáveis para entender o que representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do usuário que configurou no seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço para endpoints OpenAI não-Azure |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para usar esse serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implementado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implementação do modelo _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implementação do modelo _text embeddings_ |
| | |

Nota: As duas últimas variáveis Azure OpenAI refletem um modelo padrão para conclusão de chat (geração de texto) e busca vetorial (embeddings) respectivamente. Instruções para configurá-los serão definidas em tarefas relevantes.

### 2.3 Configurar Azure: A partir do Portal

Os valores de endpoint e chave do Azure OpenAI serão encontrados no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), então vamos começar por lá.

1. Vá para o [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clique na opção **Keys and Endpoint** na barra lateral (menu à esquerda).
1. Clique em **Show Keys** - deve ver o seguinte: KEY 1, KEY 2 e Endpoint.
1. Use o valor KEY 1 para AZURE_OPENAI_API_KEY
1. Use o valor Endpoint para AZURE_OPENAI_ENDPOINT

Em seguida, precisamos dos endpoints para os modelos específicos que implementámos.

1. Clique na opção **Model deployments** na barra lateral (menu à esquerda) para o recurso Azure OpenAI.
1. Na página de destino, clique em **Manage Deployments**

Isso o levará ao site Azure OpenAI Studio, onde encontraremos os outros valores conforme descrito abaixo.

### 2.4 Configurar Azure: A partir do Studio

1. Navegue até o [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do seu recurso** conforme descrito acima.
1. Clique na aba **Deployments** (barra lateral, esquerda) para visualizar os modelos atualmente implementados.
1. Se o seu modelo desejado não estiver implementado, use **Create new deployment** para implementá-lo.
1. Você precisará de um modelo _text-generation_ - recomendamos: **gpt-35-turbo**
1. Você precisará de um modelo _text-embedding_ - recomendamos **text-embedding-ada-002**

Agora atualize as variáveis de ambiente para refletir o _nome da implementação_ usado. Este será tipicamente o mesmo que o nome do modelo, a menos que o tenha alterado explicitamente. Então, como exemplo, pode ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Não se esqueça de salvar o ficheiro .env quando terminar**. Agora pode sair do ficheiro e retornar às instruções para executar o notebook.

### 2.5 Configurar OpenAI: A partir do Perfil

Sua chave API OpenAI pode ser encontrada na sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se não tiver uma, pode inscrever-se para uma conta e criar uma chave API. Assim que tiver a chave, pode usá-la para preencher a variável `OPENAI_API_KEY` no ficheiro `.env`.

### 2.6 Configurar Hugging Face: A partir do Perfil

Seu token Hugging Face pode ser encontrado no seu perfil sob [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não publique ou compartilhe estes publicamente. Em vez disso, crie um novo token para uso neste projeto e copie-o para o ficheiro `.env` sob a variável `HUGGING_FACE_API_KEY`. _Nota:_ Este tecnicamente não é uma chave API, mas é usado para autenticação, então estamos mantendo essa convenção de nomenclatura para consistência.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.