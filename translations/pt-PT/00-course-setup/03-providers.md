# Escolher e Configurar um Fornecedor de LLM 🔑

As tarefas **podem** também ser configuradas para funcionar com uma ou mais implementações de Grandes Modelos de Linguagem (LLM) através de um fornecedor de serviço suportado, como OpenAI, Azure ou Hugging Face. Estes fornecem um _endpoint alojado_ (API) que podemos aceder programaticamente com as credenciais corretas (chave API ou token). Neste curso, abordamos estes fornecedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com modelos diversos incluindo a série principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco em prontidão empresarial
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) para um único endpoint e chave API para aceder a centenas de modelos da OpenAI, Meta, Mistral, Cohere, Microsoft e mais (substitui o GitHub Models, que será descontinuado no final de julho de 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos open-source e servidor de inferência
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ou [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) se preferir correr modelos completamente offline no seu próprio dispositivo, sem necessidade de subscrição na cloud

**Terá de usar as suas próprias contas para estes exercícios**. As tarefas são opcionais, pelo que pode escolher configurar um, todos - ou nenhum - dos fornecedores com base nos seus interesses. Algumas orientações para registo:

| Registo | Custo | Chave API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Baseado em projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sem Código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Múltiplos Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [É necessário solicitar acesso antecipadamente](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Preços](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Página de visão geral do projeto](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Camada gratuita disponível; um endpoint + chave para muitos fornecedores de modelos |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratuito (corre no seu dispositivo) | Não é necessário | [CLI/SDK local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Endpoint totalmente offline, compatível com OpenAI |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes fornecedores. As tarefas que requerem um fornecedor específico conterão uma destas etiquetas no nome do ficheiro:

- `aoai` - requer endpoint Azure OpenAI, chave
- `oai` - requer endpoint OpenAI, chave
- `hf` - requer token Hugging Face
- `githubmodels` - requer endpoint Microsoft Foundry Models, chave (GitHub Models será descontinuado no final de julho de 2026)

Pode configurar um, nenhum ou todos os fornecedores. As tarefas relacionadas simplesmente falharão se as credenciais estiverem em falta.

## Criar ficheiro `.env`

Assume-se que já leu as orientações acima, registou-se no fornecedor relevante e obteve as credenciais necessárias de autenticação (API_KEY ou token). No caso do Azure OpenAI, assume-se também que tem uma implementação válida de um Serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implantado para completamento de chat.

O próximo passo é configurar as suas **variáveis de ambiente locais** da seguinte forma:

1. Procure na pasta raiz um ficheiro `.env.copy` que deverá ter conteúdo semelhante a este:

   ```bash
   # Fornecedor OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI na Microsoft Foundry
   ## (O Serviço Azure OpenAI faz agora parte da Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Padrão definido! (versão atual estável da API GA)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modelos Microsoft Foundry (catálogo de modelos multi-fornecedor, substitui os Modelos GitHub, que serão descontinuados no final de julho de 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copie esse ficheiro para `.env` usando o comando abaixo. Este ficheiro está _ignorável pelo git_, mantendo os segredos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os espaços reservados à direita do `=`) conforme descrito na próxima secção.

4. (Opcional) Se usar GitHub Codespaces, pode guardar as variáveis de ambiente como _segredos do Codespaces_ associados a este repositório. Nesse caso, não precisará de configurar um ficheiro .env local. **Note que esta opção funciona apenas se usar GitHub Codespaces.** Ainda precisará de configurar o ficheiro .env se usar Docker Desktop em alternativa.

## Preencher ficheiro `.env`

Vamos olhar rapidamente para os nomes das variáveis para perceber o que representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do utilizador que configurou no seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço para endpoints OpenAI não Azure |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para usar esse serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implantado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint da implementação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint da implementação do modelo de _incorporações de texto_ |
| AZURE_INFERENCE_ENDPOINT | Este é o endpoint para o seu projeto Microsoft Foundry, usado para Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Esta é a chave API para o seu projeto Microsoft Foundry |
| | |

Nota: As duas últimas variáveis Azure OpenAI representam um modelo padrão para completamento de chat (geração de texto) e pesquisa vetorial (incorporações) respetivamente. As instruções para configurá-las serão definidas em tarefas relevantes.

## Configurar Azure OpenAI: A partir do Portal

> **Nota:** O Serviço Azure OpenAI faz agora parte do [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Os recursos e implementações ainda aparecem no Portal Azure, mas a gestão diária dos modelos (implementações, playground, monitorização) acontece agora no portal Foundry em vez do antigo "Azure OpenAI Studio" autónomo.

Os valores do endpoint Azure OpenAI e chave podem ser encontrados no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), por isso vamos começar por aí.

1. Aceda ao [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clique na opção **Chaves e Endpoint** na barra lateral (menu à esquerda).
1. Clique em **Mostrar Chaves** - deverá ver o seguinte: CHAVE 1, CHAVE 2 e Endpoint.
1. Use o valor da CHAVE 1 para AZURE_OPENAI_API_KEY
1. Use o valor do Endpoint para AZURE_OPENAI_ENDPOINT

A seguir, precisamos dos endpoints para os modelos específicos que implementámos.

1. Clique na opção **Implementações de modelo** na barra lateral (menu à esquerda) para o recurso Azure OpenAI.
1. Na página destino, clique em **Ir para o portal Microsoft Foundry** (ou **Gerir Implementações**, dependendo do tipo de recurso)

Isto levará ao portal Microsoft Foundry, onde encontraremos os outros valores conforme descrito abaixo.

## Configurar Azure OpenAI: A partir do portal Microsoft Foundry

1. Navegue para o [portal Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do seu recurso** conforme descrito acima.
1. Clique na aba **Implementações** (barra lateral, esquerda) para ver os modelos atualmente implantados.
1. Se o modelo desejado não estiver implementado, use **Implementar modelo** para o implantar a partir do [catálogo de modelos](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Vai precisar de um modelo de _geração de texto_ - recomendamos: **gpt-4o-mini**
1. Vai precisar de um modelo de _incorporação de texto_ - recomendamos **text-embedding-3-small**

Agora atualize as variáveis de ambiente para refletir o _Nome da implementação_ usado. Tipicamente será o mesmo nome do modelo, a menos que o tenha alterado explicitamente. Por exemplo, pode ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Não se esqueça de guardar o ficheiro .env quando terminar**. Pode agora sair do ficheiro e retornar às instruções para correr o notebook.

## Configurar OpenAI: A partir do Perfil

A sua chave API OpenAI pode ser encontrada na sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se não tiver uma, pode inscrever-se e criar uma chave API. Depois de a ter, pode usá-la para preencher a variável `OPENAI_API_KEY` no ficheiro `.env`.

## Configurar Hugging Face: A partir do Perfil

O seu token Hugging Face pode ser encontrado no seu perfil, em [Tokens de Acesso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não publique nem partilhe estes publicamente. Em vez disso, crie um novo token para uso neste projeto e copie-o para o ficheiro `.env` sob a variável `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente isto não é uma chave API, mas é usado para autenticação, pelo que mantemos esta convenção de nomes para consistência.

## Configurar Microsoft Foundry Models: A partir do Portal

> **Nota:** O GitHub Models será descontinuado no final de julho de 2026. O Microsoft Foundry Models é a substituição direta, oferecendo o mesmo catálogo de modelos gratuitos para experimentar e a experiência do Azure AI Inference SDK / OpenAI SDK.

1. Aceda ao [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) e crie (ou abra) um projeto Foundry.
1. Navegue pelo [catálogo de modelos](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) e implemente um modelo, por exemplo `gpt-4o-mini`.
1. Na página de **Visão Geral** do projeto, copie o **endpoint** e a **chave API**.
1. Use o valor do endpoint para `AZURE_INFERENCE_ENDPOINT` e o valor da chave para `AZURE_INFERENCE_CREDENTIAL` no seu ficheiro `.env`.

## Fornecedores Offline / Locais

Se preferir não usar de todo uma subscrição na cloud, pode correr modelos abertos compatíveis diretamente no seu dispositivo:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - runtime local da Microsoft. Seleciona automaticamente o melhor fornecedor de execução (NPU, GPU ou CPU) e expõe um endpoint compatível com OpenAI, para que possa reutilizar a maior parte do código de exemplo deste curso com alterações mínimas. Veja a [documentação Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para começar, ou instale com `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - uma alternativa popular para correr localmente modelos abertos como Llama, Phi, Mistral, e Gemma.


Veja a [Lição 19: Construir com SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) para exemplos práticos usando ambas as opções.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->