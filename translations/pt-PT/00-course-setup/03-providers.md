# Escolher e Configurar um Provedor de LLM 🔑

As tarefas **podem** também ser configuradas para funcionar com uma ou mais implementações de Large Language Model (LLM) através de um provedor de serviço suportado como OpenAI, Azure ou Hugging Face. Estes fornecem um _endpoint alojado_ (API) ao qual podemos aceder programaticamente com as credenciais corretas (chave de API ou token). Neste curso, discutimos estes provedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com modelos diversos incluindo a série principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco em prontidão empresarial.
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) para um único endpoint e chave de API para aceder a centenas de modelos da OpenAI, Meta, Mistral, Cohere, Microsoft e mais (substitui GitHub Models, que será descontinuado no final de Julho de 2026).
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos open-source e servidor de inferência.
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ou [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) se preferir correr modelos totalmente offline no seu próprio dispositivo, sem subscrição na cloud.

**Necessitará de usar as suas próprias contas para estes exercícios**. As tarefas são opcionais para que possa escolher configurar um, todos - ou nenhum - dos provedores consoante os seus interesses. Aqui fica alguma orientação para inscrição:

| Inscrição | Custo | Chave API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Por projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sem código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Vários Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [É necessário solicitar acesso previamente](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Preços](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Página de Visão Geral do Projeto](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Camada gratuita disponível; um endpoint + chave para vários provedores de modelo |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratuito (corre no seu dispositivo) | Não requerido | [Local CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Endpoint OpenAI-compatible totalmente offline |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes provedores. As tarefas que requerem um provedor específico terão uma destas etiquetas no nome do ficheiro:

- `aoai` - requer endpoint e chave Azure OpenAI
- `oai` - requer endpoint e chave OpenAI
- `hf` - requer token Hugging Face
- `githubmodels` - requer endpoint e chave Microsoft Foundry Models (GitHub Models será descontinuado no final de Julho 2026)

Pode configurar um, nenhum ou todos os provedores. As tarefas relacionadas irão simplesmente falhar se as credenciais estiverem em falta.

## Criar ficheiro `.env`

Assume-se que já leu a orientação acima, registou-se com o provedor relevante e obteve as credenciais de autenticação necessárias (API_KEY ou token). No caso do Azure OpenAI, assume-se também que possui uma implementação válida de um Azure OpenAI Service (endpoint) com pelo menos um modelo GPT implementado para completamento de chat.

O passo seguinte é configurar as suas **variáveis de ambiente locais** da seguinte forma:

1. Procure na pasta raiz um ficheiro `.env.copy` que deve ter conteúdo semelhante a este:

   ```bash
   # Provedor OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI no Microsoft Foundry
   ## (O serviço Azure OpenAI faz agora parte do Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # O padrão está definido! (versão estável atual da API GA)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modelos Microsoft Foundry (catálogo de modelos multi-provedor, substitui modelos GitHub, que será descontinuado no final de julho de 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copie esse ficheiro para `.env` usando o comando abaixo. Este ficheiro está _gitignore-d_, mantendo os segredos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os espaços reservados no lado direito do `=`) conforme descrito na secção seguinte.

4. (Opcional) Se usar GitHub Codespaces, tem a opção de guardar variáveis de ambiente como _segredos do Codespaces_ associados a este repositório. Nesse caso, não precisará de configurar um ficheiro .env local. **No entanto, note que esta opção funciona apenas se usar GitHub Codespaces.** Ainda precisará de configurar o ficheiro .env se usar Docker Desktop.

## Preencher o ficheiro `.env`

Vamos dar uma rápida vista de olhos aos nomes das variáveis para compreender o que representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do utilizador que configurou no seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço em endpoints OpenAI não-Azure |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para usar esse serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implementado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implementação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implementação do modelo de _incorporações de texto_ |
| AZURE_INFERENCE_ENDPOINT | Este é o endpoint para o seu projeto Microsoft Foundry, usado para Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Esta é a chave API para o seu projeto Microsoft Foundry |
| | |

Nota: As duas últimas variáveis Azure OpenAI representam um modelo padrão para completamento de chat (geração de texto) e pesquisa vetorial (incorporações) respetivamente. As instruções para configurá-las serão definidas nas tarefas relevantes.

## Configurar Azure OpenAI: A partir do Portal

> **Nota:** O Azure OpenAI Service faz agora parte do [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Recursos e implementações continuam a aparecer no Portal Azure, mas a gestão diária de modelos (implementações, playground, monitorização) ocorre agora no portal Foundry em vez do antigo "Azure OpenAI Studio" independente.

O endpoint Azure OpenAI e os valores das chaves serão encontrados no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), então vamos começar por aí.

1. Vá ao [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clique na opção **Keys and Endpoint** na barra lateral (menu à esquerda).
1. Clique em **View Keys** - deverá ver o seguinte: KEY 1, KEY 2 e Endpoint.
1. Use o valor da KEY 1 para AZURE_OPENAI_API_KEY
1. Use o valor do Endpoint para AZURE_OPENAI_ENDPOINT

A seguir, precisamos dos endpoints para os modelos específicos que implementámos.

1. Clique na opção **Model deployments** na barra lateral (menu à esquerda) para o recurso Azure OpenAI.
1. Na página de destino, clique em **Go to Microsoft Foundry portal** (ou **Manage Deployments**, dependendo do tipo do recurso)

Isto irá levá-lo ao portal Microsoft Foundry, onde encontraremos os outros valores como está descrito abaixo.

## Configurar Azure OpenAI: A partir do portal Microsoft Foundry

1. Navegue para o [portal Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do seu recurso** conforme descrito acima.
1. Clique no separador **Deployments** (barra lateral, esquerda) para ver os modelos implementados atualmente.
1. Se o modelo desejado não estiver implementado, use **Deploy model** para o implementar a partir do [catálogo de modelos](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Vai precisar de um modelo de _geração de texto_ – recomendamos: **gpt-5-mini**
1. Vai precisar de um modelo de _incorporação de texto_ – recomendamos **text-embedding-3-small**

Agora atualize as variáveis de ambiente para refletir o _nome da implementação_ usado. Normalmente será o mesmo que o nome do modelo, salvo se o tiver alterado explicitamente. Por exemplo, pode ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Não se esqueça de guardar o ficheiro .env quando terminar**. Pode agora sair do ficheiro e regressar às instruções para executar o notebook.

## Configurar OpenAI: A partir do Perfil

A sua chave API OpenAI pode ser encontrada na sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se ainda não tiver uma, pode registar-se e criar uma chave API. Depois de obter a chave, pode usá-la para preencher a variável `OPENAI_API_KEY` no ficheiro `.env`.

## Configurar Hugging Face: A partir do Perfil

O seu token Hugging Face pode ser encontrado no seu perfil em [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não publique nem partilhe estes publicamente. Em vez disso, crie um novo token para uso neste projeto e copie-o para o ficheiro `.env` na variável `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente isto não é uma chave API, mas é usado para autenticação, pelo que mantemos esta nomenclatura por consistência.

## Configurar Microsoft Foundry Models: A partir do Portal

> **Nota:** GitHub Models será descontinuado no final de Julho 2026. Microsoft Foundry Models é o substituto direto, oferecendo o mesmo catálogo de modelos gratuito para testar e a experiência Azure AI Inference SDK / OpenAI SDK.

1. Vá a [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) e crie (ou abra) um projeto Foundry.
1. Navegue pelo [catálogo de modelos](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) e implemente um modelo, por exemplo `gpt-5-mini`.
1. Na página de **Visão Geral** do projeto, copie o **endpoint** e a **chave API**.
1. Use o valor do endpoint para `AZURE_INFERENCE_ENDPOINT` e a chave para `AZURE_INFERENCE_CREDENTIAL` no seu ficheiro `.env`.

## Provedores Offline / Locais

Se preferir não usar nenhuma subscrição cloud, pode correr modelos compatíveis abertos diretamente no seu dispositivo:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - runtime da Microsoft no dispositivo. Seleciona automaticamente o melhor provedor de execução (NPU, GPU ou CPU) e expõe um endpoint compatível com OpenAI, para que possa reutilizar a maioria do código de exemplo neste curso com mudanças mínimas. Veja a [documentação Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para começar ou instale com `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - uma alternativa popular para correr modelos abertos como Llama, Phi, Mistral e Gemma localmente.


Veja [Lição 19: Construir com SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) para exemplos práticos a usar ambas as opções.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->