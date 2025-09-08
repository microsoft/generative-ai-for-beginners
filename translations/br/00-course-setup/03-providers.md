<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T16:22:41+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "br"
}
-->
# Escolhendo e Configurando um Provedor de LLM 🔑

Os exercícios **podem** ser configurados para funcionar com uma ou mais implantações de Large Language Model (LLM) através de provedores de serviço suportados como OpenAI, Azure ou Hugging Face. Esses provedores oferecem um _endpoint hospedado_ (API) que podemos acessar programaticamente com as credenciais corretas (chave de API ou token). Neste curso, falamos sobre estes provedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com diversos modelos, incluindo a série principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco em uso corporativo
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos open-source e servidor de inferência

**Você precisará usar suas próprias contas para estes exercícios**. Os exercícios são opcionais, então você pode escolher configurar um, todos ou nenhum dos provedores, conforme seu interesse. Algumas orientações para cadastro:

| Cadastro | Custo | Chave de API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Por projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Vários modelos disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Necessário solicitar acesso antecipadamente](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes provedores. Os exercícios que exigem um provedor específico terão uma destas tags no nome do arquivo:

- `aoai` - requer endpoint e chave do Azure OpenAI
- `oai` - requer endpoint e chave do OpenAI
- `hf` - requer token do Hugging Face

Você pode configurar um, nenhum ou todos os provedores. Os exercícios relacionados simplesmente apresentarão erro caso as credenciais estejam ausentes.

## Criar arquivo `.env`

Assumimos que você já leu as orientações acima, fez o cadastro no provedor relevante e obteve as credenciais de autenticação necessárias (API_KEY ou token). No caso do Azure OpenAI, assumimos que você também já possui uma implantação válida do serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implantado para chat completion.

O próximo passo é configurar suas **variáveis de ambiente locais** da seguinte forma:

1. Procure na pasta raiz um arquivo chamado `.env.copy` que deve ter um conteúdo parecido com este:

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

2. Copie esse arquivo para `.env` usando o comando abaixo. Este arquivo está no _gitignore_, mantendo os segredos protegidos.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os placeholders à direita do `=`) conforme descrito na próxima seção.

4. (Opcional) Se você usa o GitHub Codespaces, é possível salvar variáveis de ambiente como _segredos do Codespaces_ associados a este repositório. Nesse caso, não será necessário configurar um arquivo .env local. **Porém, observe que essa opção só funciona se você usar o GitHub Codespaces.** Se você usar o Docker Desktop, ainda será necessário configurar o arquivo .env.

## Preencher o arquivo `.env`

Vamos dar uma olhada rápida nos nomes das variáveis para entender o que cada uma representa:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do usuário que você configura no seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para uso do serviço em endpoints OpenAI que não sejam Azure |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para uso desse serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implantado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implantação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implantação do modelo de _embeddings de texto_ |
| | |

Observação: As duas últimas variáveis do Azure OpenAI indicam o modelo padrão para chat completion (geração de texto) e busca vetorial (embeddings), respectivamente. As instruções para configurá-las serão detalhadas nos exercícios relevantes.

## Configurar Azure: Pelo Portal

Os valores de endpoint e chave do Azure OpenAI podem ser encontrados no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), então vamos começar por lá.

1. Acesse o [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clique na opção **Chaves e Endpoint** no menu lateral (à esquerda).
1. Clique em **Mostrar Chaves** - você verá: CHAVE 1, CHAVE 2 e Endpoint.
1. Use o valor da CHAVE 1 para AZURE_OPENAI_API_KEY
1. Use o valor do Endpoint para AZURE_OPENAI_ENDPOINT

Agora, precisamos dos endpoints dos modelos específicos que você implantou.

1. Clique na opção **Implantações de Modelo** no menu lateral (à esquerda) do recurso Azure OpenAI.
1. Na página de destino, clique em **Gerenciar Implantações**

Isso vai te levar ao site do Azure OpenAI Studio, onde encontraremos os outros valores conforme descrito abaixo.

## Configurar Azure: Pelo Studio

1. Acesse o [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do seu recurso** como descrito acima.
1. Clique na aba **Implantações** (menu lateral, à esquerda) para ver os modelos atualmente implantados.
1. Se o modelo desejado não estiver implantado, use **Criar nova implantação** para implantá-lo.
1. Você vai precisar de um modelo de _geração de texto_ - recomendamos: **gpt-35-turbo**
1. Você vai precisar de um modelo de _embeddings de texto_ - recomendamos **text-embedding-ada-002**

Agora, atualize as variáveis de ambiente para refletir o _nome da implantação_ utilizado. Normalmente, será o mesmo nome do modelo, a menos que você tenha alterado. Por exemplo, você pode ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Não esqueça de salvar o arquivo .env ao finalizar**. Agora você pode fechar o arquivo e voltar para as instruções de execução do notebook.

## Configurar OpenAI: Pelo Perfil

Sua chave de API do OpenAI pode ser encontrada na sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se ainda não tiver uma, cadastre-se e crie uma chave de API. Depois de obter a chave, use-a para preencher a variável `OPENAI_API_KEY` no arquivo `.env`.

## Configurar Hugging Face: Pelo Perfil

Seu token do Hugging Face pode ser encontrado no seu perfil em [Tokens de Acesso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não compartilhe esses tokens publicamente. Em vez disso, crie um novo token para uso neste projeto e copie-o para o arquivo `.env` na variável `HUGGING_FACE_API_KEY`. _Observação:_ Tecnicamente, isso não é uma chave de API, mas é usado para autenticação, então mantemos essa nomenclatura por consistência.

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.