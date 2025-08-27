<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T16:13:48+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "pt"
}
-->
# Escolher e Configurar um Fornecedor de LLM 🔑

Os exercícios **podem** ser configurados para funcionar com uma ou mais implementações de Large Language Model (LLM) através de um fornecedor de serviços suportado, como OpenAI, Azure ou Hugging Face. Estes fornecedores disponibilizam um _endpoint alojado_ (API) ao qual podemos aceder programaticamente com as credenciais certas (chave API ou token). Neste curso, abordamos os seguintes fornecedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com vários modelos, incluindo a série principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco em soluções empresariais
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos open-source e servidor de inferência

**Terás de usar as tuas próprias contas nestes exercícios**. Os exercícios são opcionais, por isso podes escolher configurar um, todos - ou nenhum - dos fornecedores, conforme o teu interesse. Algumas indicações para o registo:

| Registo | Custo | Chave API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Por projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sem código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Vários modelos disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [É necessário pedir acesso antecipadamente](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [O Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Segue as instruções abaixo para _configurar_ este repositório para utilização com diferentes fornecedores. Os exercícios que exigem um fornecedor específico terão um destes identificadores no nome do ficheiro:

- `aoai` - requer endpoint e chave do Azure OpenAI
- `oai` - requer endpoint e chave do OpenAI
- `hf` - requer token do Hugging Face

Podes configurar um, nenhum ou todos os fornecedores. Os exercícios relacionados vão simplesmente dar erro se faltar alguma credencial.

## Criar ficheiro `.env`

Assumimos que já leste as indicações acima, te registaste no fornecedor relevante e obtiveste as credenciais de autenticação necessárias (API_KEY ou token). No caso do Azure OpenAI, assumimos também que tens uma implementação válida do serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implementado para chat completion.

O próximo passo é configurar as **variáveis de ambiente locais** da seguinte forma:

1. Procura na pasta raiz um ficheiro `.env.copy` que deverá ter um conteúdo semelhante a este:

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

2. Copia esse ficheiro para `.env` usando o comando abaixo. Este ficheiro está _gitignore-d_, mantendo os segredos protegidos.

   ```bash
   cp .env.copy .env
   ```

3. Preenche os valores (substitui os espaços reservados à direita do `=`) conforme descrito na secção seguinte.

4. (Opcional) Se usares o GitHub Codespaces, tens a opção de guardar variáveis de ambiente como _Codespaces secrets_ associados a este repositório. Nesse caso, não precisas de configurar o ficheiro .env localmente. **No entanto, esta opção só funciona se usares o GitHub Codespaces.** Se usares o Docker Desktop, terás de configurar o ficheiro .env na mesma.

## Preencher o ficheiro `.env`

Vamos analisar rapidamente os nomes das variáveis para perceber o que representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do utilizador que configuras no teu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço em endpoints OpenAI que não sejam Azure |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para usar esse serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implementado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implementação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implementação do modelo de _embeddings de texto_ |
| | |

Nota: As duas últimas variáveis do Azure OpenAI referem-se ao modelo predefinido para chat completion (geração de texto) e pesquisa vetorial (embeddings), respetivamente. As instruções para as definir serão dadas nos exercícios relevantes.

## Configurar Azure: A partir do Portal

Os valores do endpoint e da chave do Azure OpenAI encontram-se no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), por isso vamos começar por aí.

1. Vai ao [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clica na opção **Keys and Endpoint** na barra lateral (menu à esquerda).
1. Clica em **Show Keys** - deves ver: KEY 1, KEY 2 e Endpoint.
1. Usa o valor de KEY 1 para AZURE_OPENAI_API_KEY
1. Usa o valor de Endpoint para AZURE_OPENAI_ENDPOINT

De seguida, precisamos dos endpoints para os modelos específicos que implementaste.

1. Clica na opção **Model deployments** na barra lateral (menu à esquerda) do recurso Azure OpenAI.
1. Na página de destino, clica em **Manage Deployments**

Isto leva-te ao site do Azure OpenAI Studio, onde vais encontrar os outros valores conforme descrito abaixo.

## Configurar Azure: A partir do Studio

1. Vai ao [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do teu recurso** como descrito acima.
1. Clica no separador **Deployments** (barra lateral, à esquerda) para ver os modelos atualmente implementados.
1. Se o modelo que queres não estiver implementado, usa **Create new deployment** para o implementar.
1. Vais precisar de um modelo de _geração de texto_ - recomendamos: **gpt-35-turbo**
1. Vais precisar de um modelo de _embeddings de texto_ - recomendamos **text-embedding-ada-002**

Agora atualiza as variáveis de ambiente para refletir o _nome da implementação_ usado. Normalmente será igual ao nome do modelo, a menos que o tenhas alterado. Por exemplo, podes ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Não te esqueças de guardar o ficheiro .env quando terminares**. Podes agora sair do ficheiro e voltar às instruções para executar o notebook.

## Configurar OpenAI: A partir do Perfil

A tua chave API do OpenAI pode ser encontrada na tua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se ainda não tens uma, podes criar uma conta e gerar uma chave API. Depois de teres a chave, podes usá-la para preencher a variável `OPENAI_API_KEY` no ficheiro `.env`.

## Configurar Hugging Face: A partir do Perfil

O teu token do Hugging Face encontra-se no teu perfil em [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não partilhes nem publiques estes tokens. Em vez disso, cria um novo token para este projeto e copia-o para o ficheiro `.env` na variável `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente isto não é uma chave API, mas é usado para autenticação, por isso mantemos essa convenção de nome para consistência.

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.