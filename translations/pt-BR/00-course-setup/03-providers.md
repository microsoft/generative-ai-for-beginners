# Escolhendo e Configurando um Provedor LLM 🔑

As tarefas **podem** também ser configuradas para funcionar com uma ou mais implantações de Modelos de Linguagem Grande (LLM) por meio de um provedor de serviço suportado como OpenAI, Azure ou Hugging Face. Estes fornecem um _endpoint hospedado_ (API) que podemos acessar programaticamente com as credenciais corretas (chave API ou token). Neste curso, discutimos estes provedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com modelos diversos incluindo a série principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco em prontidão empresarial
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) para um endpoint único e chave API para acessar centenas de modelos da OpenAI, Meta, Mistral, Cohere, Microsoft e mais (substitui GitHub Models, que será descontinuado no final de julho de 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos open-source e servidor de inferência
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ou [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) se preferir rodar modelos totalmente offline no seu próprio dispositivo, sem necessidade de assinatura na nuvem

**Você precisará usar suas próprias contas para esses exercícios**. As tarefas são opcionais, então você pode escolher configurar um, todos - ou nenhum - dos provedores baseado nos seus interesses. Algumas orientações para cadastro:

| Cadastro | Custo | Chave API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Baseado em Projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sem Código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Múltiplos Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Início Rápido SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Início Rápido Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [É necessário solicitar acesso com antecedência](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Preços](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Página de Visão Geral do Projeto](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Playground Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Camada gratuita disponível; um endpoint + chave para muitos provedores de modelo |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Grátis (executa no seu dispositivo) | Não exigido | [CLI/SDK Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Endpoint totalmente offline, compatível com OpenAI |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes provedores. Tarefas que requerem um provedor específico conterão uma destas tags no nome do arquivo:

- `aoai` - requer endpoint Azure OpenAI, chave
- `oai` - requer endpoint OpenAI, chave
- `hf` - requer token Hugging Face
- `githubmodels` - requer endpoint Microsoft Foundry Models, chave (GitHub Models será descontinuado no final de julho de 2026)

Você pode configurar um, nenhum ou todos os provedores. Tarefas relacionadas simplesmente apresentarão erro se as credenciais estiverem faltando.

## Criar arquivo `.env`

Assumimos que você já leu as orientações acima, se cadastrou no provedor relevante e obteve as credenciais de autenticação necessárias (API_KEY ou token). No caso do Azure OpenAI, assumimos que você também tem uma implantação válida de um Serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implantado para finalização de chat.

O próximo passo é configurar suas **variáveis de ambiente locais** da seguinte forma:

1. Procure na raiz do projeto um arquivo `.env.copy` que deve conter algo assim:

   ```bash
   # Provedor OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI na Microsoft Foundry
   ## (O serviço Azure OpenAI agora faz parte do Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Padrão definido! (versão atual estável da API GA)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modelos Microsoft Foundry (catálogo de modelos multi-provedor, substitui os Modelos GitHub, que serão descontinuados no final de julho de 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copie esse arquivo para `.env` usando o comando abaixo. Este arquivo é _gitignore_, mantendo os segredos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os espaços reservados à direita do `=`) conforme descrito na seção seguinte.

4. (Opcional) Se você usa GitHub Codespaces, tem a opção de salvar variáveis de ambiente como _segredos Codespaces_ associados a este repositório. Nesse caso, não será necessário configurar um arquivo .env local. **No entanto, note que essa opção funciona apenas se usar GitHub Codespaces.** Você ainda precisará configurar o arquivo .env se usar Docker Desktop.

## Preencher arquivo `.env`

Vamos dar uma olhada rápida nos nomes das variáveis para entender o que elas representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do usuário que você configurou no seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço para endpoints OpenAI não Azure |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para usar esse serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implantado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implantação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implantação do modelo de _incorporações de texto_ |
| AZURE_INFERENCE_ENDPOINT | Este é o endpoint para seu projeto Microsoft Foundry, usado para Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Esta é a chave API para seu projeto Microsoft Foundry |
| | |

Nota: As duas últimas variáveis Azure OpenAI refletem um modelo padrão para finalização de chat (geração de texto) e busca vetorial (incorporações) respectivamente. Instruções para configurá-las serão definidas nas tarefas relevantes.

## Configurar Azure OpenAI: Pelo Portal

> **Nota:** O Serviço Azure OpenAI agora faz parte do [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Recursos e implantações ainda aparecem no Portal Azure, mas o gerenciamento diário dos modelos (implantações, playground, monitoramento) agora acontece no portal Foundry em vez do antigo "Azure OpenAI Studio" independente.

Os valores do endpoint e da chave Azure OpenAI podem ser encontrados no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), então vamos começar por lá.

1. Vá ao [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clique na opção **Chaves e Endpoint** na barra lateral (menu à esquerda).
1. Clique em **Mostrar Chaves** - você deverá ver o seguinte: CHAVE 1, CHAVE 2 e Endpoint.
1. Use o valor da CHAVE 1 para AZURE_OPENAI_API_KEY
1. Use o valor do Endpoint para AZURE_OPENAI_ENDPOINT

Agora, precisamos dos endpoints para os modelos específicos que implantamos.

1. Clique na opção **Implantações de modelo** na barra lateral (menu esquerdo) do recurso Azure OpenAI.
1. Na página de destino, clique em **Ir para portal Microsoft Foundry** (ou **Gerenciar Implantações**, dependendo do tipo do seu recurso)

Isso levará você ao portal Microsoft Foundry, onde encontraremos os outros valores conforme descrito abaixo.

## Configurar Azure OpenAI: Pelo portal Microsoft Foundry

1. Navegue até o [portal Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do seu recurso** conforme descrito acima.
1. Clique na guia **Implantações** (barra lateral, esquerda) para ver os modelos atualmente implantados.
1. Se o modelo desejado não estiver implantado, use **Implantar modelo** para implantá-lo do [catálogo de modelos](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Você precisará de um modelo de _geração de texto_ - recomendamos: **gpt-4o-mini**
1. Você precisará de um modelo de _incorporação de texto_ - recomendamos **text-embedding-3-small**

Agora atualize as variáveis de ambiente para refletir o _nome da implantação_ usado. Normalmente será igual ao nome do modelo, a menos que você tenha alterado explicitamente. Assim, como exemplo, você pode ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Não esqueça de salvar o arquivo .env ao terminar**. Você pode agora sair do arquivo e retornar às instruções para executar o notebook.

## Configurar OpenAI: Pelo Perfil

Sua chave API OpenAI pode ser encontrada na sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se você não tiver uma, pode criar uma conta e gerar uma chave API. Uma vez que tenha a chave, use-a para preencher a variável `OPENAI_API_KEY` no arquivo `.env`.

## Configurar Hugging Face: Pelo Perfil

Seu token Hugging Face pode ser encontrado no seu perfil na seção [Tokens de Acesso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não publique ou compartilhe esses tokens publicamente. Em vez disso, crie um token novo para o uso deste projeto e copie-o no arquivo `.env` na variável `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente, isso não é uma chave API, mas é usado para autenticação, então mantemos essa convenção de nomenclatura por consistência.

## Configurar Microsoft Foundry Models: Pelo Portal

> **Nota:** GitHub Models será descontinuado no final de julho de 2026. Microsoft Foundry Models é o substituto direto, oferecendo o mesmo catálogo de modelos para teste gratuito e experiência Azure AI Inference SDK / OpenAI SDK.

1. Vá para [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) e crie (ou abra) um projeto Foundry.
1. Navegue pelo [catálogo de modelos](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) e implante um modelo, por exemplo `gpt-4o-mini`.
1. Na página de **Visão Geral** do projeto, copie o **endpoint** e a **chave API**.
1. Use o valor do endpoint para `AZURE_INFERENCE_ENDPOINT` e o valor da chave para `AZURE_INFERENCE_CREDENTIAL` no seu arquivo `.env`.

## Provedores Offline / Locais

Se preferir não usar nenhuma assinatura na nuvem, você pode executar modelos open compatíveis diretamente no seu próprio dispositivo:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - runtime da Microsoft para execução local. Ele seleciona automaticamente o melhor provedor de execução (NPU, GPU ou CPU) e expõe um endpoint compatível com OpenAI, permitindo reutilizar a maior parte do código exemplo deste curso com mudanças mínimas. Veja a [documentação Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para começar, ou instale com `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - uma alternativa popular para executar modelos open como Llama, Phi, Mistral e Gemma localmente.


Veja [Lição 19: Construindo com SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) para exemplos práticos usando ambas as opções.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->