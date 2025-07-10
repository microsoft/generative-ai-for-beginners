<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:28:20+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "pt"
}
-->
# Configurar o Seu Ambiente de Desenvolvimento

Configurámos este repositório e curso com um [contentor de desenvolvimento](https://containers.dev?WT.mc_id=academic-105485-koreyst) que possui um runtime Universal capaz de suportar desenvolvimento em Python3, .NET, Node.js e Java. A configuração relacionada está definida no ficheiro `devcontainer.json` localizado na pasta `.devcontainer/` na raiz deste repositório.

Para ativar o contentor de desenvolvimento, inicie-o no [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (para um runtime alojado na cloud) ou no [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (para um runtime alojado localmente). Leia [esta documentação](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) para mais detalhes sobre como funcionam os contentores de desenvolvimento no VS Code.

> [!TIP]  
> Recomendamos usar o GitHub Codespaces para um início rápido com esforço mínimo. Ele oferece uma generosa [quota de uso gratuita](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) para contas pessoais. Configure [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) para parar ou eliminar codespaces inativos e assim maximizar a utilização da sua quota.

## 1. Execução de Trabalhos

Cada aula terá trabalhos _opcionais_ que podem ser fornecidos numa ou mais linguagens de programação, incluindo: Python, .NET/C#, Java e JavaScript/TypeScript. Esta secção fornece orientações gerais relacionadas com a execução desses trabalhos.

### 1.1 Trabalhos em Python

Os trabalhos em Python são fornecidos como aplicações (`.py`) ou notebooks Jupyter (`.ipynb`).  
- Para executar o notebook, abra-o no Visual Studio Code, clique em _Select Kernel_ (no canto superior direito) e selecione a opção padrão Python 3 apresentada. Pode agora clicar em _Run All_ para executar o notebook.  
- Para executar aplicações Python a partir da linha de comandos, siga as instruções específicas do trabalho para garantir que seleciona os ficheiros corretos e fornece os argumentos necessários.

## 2. Configuração dos Fornecedores

Os trabalhos **podem** também estar configurados para funcionar com uma ou mais implementações de Large Language Models (LLM) através de um fornecedor de serviços suportado como OpenAI, Azure ou Hugging Face. Estes fornecem um _endpoint alojado_ (API) que podemos aceder programaticamente com as credenciais corretas (chave API ou token). Neste curso, abordamos estes fornecedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com diversos modelos, incluindo a série principal GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco em prontidão empresarial  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos open-source e servidor de inferência

**Vai precisar de usar as suas próprias contas para estes exercícios**. Os trabalhos são opcionais, por isso pode escolher configurar um, todos - ou nenhum - dos fornecedores conforme os seus interesses. Algumas orientações para registo:

| Registo | Custo | Chave API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Baseado em projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sem código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Vários Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Início rápido SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Início rápido Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [É necessário solicitar acesso antecipadamente](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes fornecedores. Os trabalhos que requerem um fornecedor específico terão uma destas etiquetas no nome do ficheiro:  
 - `aoai` - requer endpoint e chave Azure OpenAI  
 - `oai` - requer endpoint e chave OpenAI  
 - `hf` - requer token Hugging Face

Pode configurar um, nenhum ou todos os fornecedores. Os trabalhos relacionados simplesmente apresentarão erro se faltarem credenciais.

###  2.1. Criar ficheiro `.env`

Assumimos que já leu as orientações acima, registou-se no fornecedor relevante e obteve as credenciais de autenticação necessárias (API_KEY ou token). No caso do Azure OpenAI, assumimos também que tem uma implementação válida de um Serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implementado para chat completion.

O próximo passo é configurar as suas **variáveis de ambiente locais** da seguinte forma:

1. Procure na pasta raiz um ficheiro `.env.copy` que deverá ter um conteúdo semelhante a este:

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

2. Copie esse ficheiro para `.env` usando o comando abaixo. Este ficheiro está _gitignore-d_, mantendo os segredos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os espaços reservados à direita do `=`) conforme descrito na secção seguinte.

3. (Opcional) Se usar GitHub Codespaces, tem a opção de guardar as variáveis de ambiente como _segredos do Codespaces_ associados a este repositório. Nesse caso, não precisará de configurar um ficheiro .env local. **No entanto, note que esta opção funciona apenas se usar GitHub Codespaces.** Ainda precisará de configurar o ficheiro .env se usar Docker Desktop.

### 2.2. Preencher o ficheiro `.env`

Vamos dar uma vista rápida aos nomes das variáveis para entender o que representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do utilizador que configurou no seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço para endpoints OpenAI não Azure |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para usar esse serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implementado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implementação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implementação do modelo de _embeddings de texto_ |
| | |

Nota: As duas últimas variáveis do Azure OpenAI refletem um modelo padrão para chat completion (geração de texto) e pesquisa vetorial (embeddings), respetivamente. As instruções para configurá-las serão definidas nos trabalhos relevantes.

### 2.3 Configurar Azure: Pelo Portal

Os valores do endpoint e da chave Azure OpenAI serão encontrados no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), por isso vamos começar por aí.

1. Aceda ao [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Clique na opção **Keys and Endpoint** na barra lateral (menu à esquerda).  
1. Clique em **Show Keys** - deverá ver o seguinte: KEY 1, KEY 2 e Endpoint.  
1. Use o valor de KEY 1 para AZURE_OPENAI_API_KEY  
1. Use o valor do Endpoint para AZURE_OPENAI_ENDPOINT

De seguida, precisamos dos endpoints para os modelos específicos que implementámos.

1. Clique na opção **Model deployments** na barra lateral (menu à esquerda) do recurso Azure OpenAI.  
1. Na página de destino, clique em **Manage Deployments**

Isto levará ao website Azure OpenAI Studio, onde encontraremos os outros valores conforme descrito abaixo.

### 2.4 Configurar Azure: Pelo Studio

1. Navegue para o [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do seu recurso** conforme descrito acima.  
1. Clique no separador **Deployments** (barra lateral, à esquerda) para ver os modelos atualmente implementados.  
1. Se o modelo desejado não estiver implementado, use **Create new deployment** para o implementar.  
1. Vai precisar de um modelo de _text-generation_ - recomendamos: **gpt-35-turbo**  
1. Vai precisar de um modelo de _text-embedding_ - recomendamos **text-embedding-ada-002**

Agora atualize as variáveis de ambiente para refletir o _nome da implementação_ usado. Normalmente será o mesmo nome do modelo, a menos que o tenha alterado explicitamente. Por exemplo, poderá ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Não se esqueça de guardar o ficheiro .env quando terminar**. Pode agora sair do ficheiro e voltar às instruções para executar o notebook.

### 2.5 Configurar OpenAI: Pelo Perfil

A sua chave API OpenAI pode ser encontrada na sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se não tiver uma, pode criar uma conta e gerar uma chave API. Depois de obter a chave, pode usá-la para preencher a variável `OPENAI_API_KEY` no ficheiro `.env`.

### 2.6 Configurar Hugging Face: Pelo Perfil

O seu token Hugging Face pode ser encontrado no seu perfil em [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não publique nem partilhe estes publicamente. Em vez disso, crie um novo token para uso neste projeto e copie-o para o ficheiro `.env` na variável `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente, isto não é uma chave API, mas é usado para autenticação, por isso mantemos esta convenção de nomes para consistência.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.