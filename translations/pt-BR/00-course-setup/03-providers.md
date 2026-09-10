# Escolhendo e Configurando um Provedor de LLM 🔑

As tarefas **podem** também ser configuradas para funcionar com uma ou mais implantações de Modelos de Linguagem Grande (LLM) através de um provedor de serviço suportado como OpenAI, Azure ou Hugging Face. Estes fornecem um _endpoint hospedado_ (API) que podemos acessar programaticamente com as credenciais corretas (chave de API ou token). Neste curso, discutimos esses provedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com modelos diversos incluindo a série principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco em prontidão empresarial
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) para um único endpoint e chave de API para acessar centenas de modelos da OpenAI, Meta, Mistral, Cohere, Microsoft e mais (substitui GitHub Models, que será descontinuado no final de julho de 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos de código aberto e servidor de inferência
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ou [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) se preferir executar modelos totalmente offline no seu dispositivo, sem necessidade de assinatura na nuvem

**Você precisará usar suas próprias contas para esses exercícios**. As tarefas são opcionais para que você possa escolher configurar um, todos - ou nenhum - dos provedores com base em seus interesses. Algumas orientações para cadastro:

| Cadastro | Custo | Chave de API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Baseado em projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sem Código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Vários Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Início Rápido SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Início Rápido Studio](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Necessário Aplicar para Acesso](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Preços](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Página de Visão Geral do Projeto](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Playground Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Camada gratuita disponível; um endpoint + chave para vários provedores de modelos |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratuito (roda no seu dispositivo) | Não requerido | [CLI/SDK Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Endpoint totalmente offline, compatível com OpenAI |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes provedores. As tarefas que requerem um provedor específico conterão uma destas tags no nome do arquivo:

- `aoai` - requer endpoint e chave Azure OpenAI
- `oai` - requer endpoint e chave OpenAI
- `hf` - requer token Hugging Face
- `githubmodels` - requer endpoint e chave Microsoft Foundry Models (GitHub Models será descontinuado no final de julho de 2026)

Você pode configurar um, nenhum ou todos os provedores. As tarefas relacionadas irão simplesmente falhar se as credenciais estiverem faltando.

## Criar arquivo `.env`

Assumimos que você já leu as orientações acima e fez o cadastro com o provedor relevante, obtendo as credenciais necessárias de autenticação (API_KEY ou token). No caso do Azure OpenAI, assumimos que você também possui uma implantação válida de um Serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implantado para conclusão de chat.

O próximo passo é configurar suas **variáveis de ambiente locais** da seguinte forma:

1. Procure na pasta raiz um arquivo `.env.copy` que deve conter algo assim:

   ```bash
   # Provedor OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI no Microsoft Foundry
   ## (O Serviço Azure OpenAI agora faz parte do Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Padrão definido! (versão estável atual da API GA)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modelos Microsoft Foundry (catálogo de modelos multi-provedor, substitui modelos GitHub, que serão descontinuados no final de julho de 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copie este arquivo para `.env` usando o comando abaixo. Esse arquivo é _gitignore-do_, mantendo os segredos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os espaços reservados à direita do `=`) conforme descrito na próxima seção.

4. (Opcional) Se você usar GitHub Codespaces, tem a opção de salvar variáveis de ambiente como _segredos de Codespaces_ associados a este repositório. Nesse caso, não precisará configurar um arquivo .env local. **No entanto, note que essa opção funciona apenas se você usar GitHub Codespaces.** Você ainda precisará configurar o arquivo .env se usar Docker Desktop.

## Preencher arquivo `.env`

Vamos dar uma olhada rápida nos nomes das variáveis para entender o que representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do usuário que você configurou no seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço para endpoints OpenAI não-Azure |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para usar este serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implantado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implantação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implantação do modelo de _embeddings de texto_ |
| AZURE_INFERENCE_ENDPOINT | Este é o endpoint do seu projeto Microsoft Foundry, usado para Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Esta é a chave da API para seu projeto Microsoft Foundry |
| | |

Nota: As duas últimas variáveis do Azure OpenAI refletem um modelo padrão para conclusão de chat (geração de texto) e busca vetorial (embeddings), respectivamente. Instruções para configurá-las serão definidas nas tarefas relevantes.

## Configurar Azure OpenAI: Pelo Portal

> **Nota:** O Serviço Azure OpenAI agora faz parte do [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Recursos e implantações ainda aparecem no Portal Azure, mas a gestão diária dos modelos (implantações, playground, monitoramento) agora acontece no portal Foundry em vez do antigo "Azure OpenAI Studio" isolado.

Os valores do endpoint e chave do Azure OpenAI serão encontrados no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), então vamos começar por lá.

1. Vá ao [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clique na opção **Chaves e Endpoint** na barra lateral (menu à esquerda).
1. Clique em **Mostrar Chaves** - você deve ver o seguinte: CHAVE 1, CHAVE 2 e Endpoint.
1. Use o valor da CHAVE 1 para AZURE_OPENAI_API_KEY
1. Use o valor do Endpoint para AZURE_OPENAI_ENDPOINT

Em seguida, precisamos dos endpoints para os modelos específicos que implantamos.

1. Clique na opção **Implantações de modelo** na barra lateral (menu à esquerda) do recurso Azure OpenAI.
1. Na página de destino, clique em **Ir para o portal Microsoft Foundry** (ou **Gerenciar Implantações**, dependendo do tipo do seu recurso)

Isso o levará ao portal Microsoft Foundry, onde encontraremos os outros valores conforme descrito abaixo.

## Configurar Azure OpenAI: Pelo portal Microsoft Foundry

1. Navegue até o [portal Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do seu recurso** conforme descrito acima.
1. Clique na aba **Implantações** (barra lateral, à esquerda) para ver os modelos atualmente implantados.
1. Se o modelo desejado não estiver implantado, use **Implantar modelo** para implantá-lo a partir do [catálogo de modelos](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Você precisará de um modelo de _geração de texto_ - recomendamos: **gpt-5-mini**
1. Você precisará de um modelo de _embedding de texto_ - recomendamos **text-embedding-3-small**

Agora atualize as variáveis de ambiente para refletir o _nome da Implantação_ usado. Normalmente será o mesmo nome do modelo, a menos que você o tenha alterado explicitamente. Então, como exemplo, você pode ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Não esqueça de salvar o arquivo .env quando terminar**. Agora você pode sair do arquivo e retornar às instruções para executar o notebook.

## Configurar OpenAI: Pelo Perfil

Sua chave de API OpenAI pode ser encontrada na sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se não tiver uma, pode criar uma conta e gerar uma chave de API. Depois de obtê-la, use-a para preencher a variável `OPENAI_API_KEY` no arquivo `.env`.

## Configurar Hugging Face: Pelo Perfil

Seu token Hugging Face pode ser encontrado no seu perfil em [Tokens de Acesso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não publique ou compartilhe isso publicamente. Em vez disso, crie um token novo para uso neste projeto e copie-o no arquivo `.env` sob a variável `HUGGING_FACE_API_KEY`. _Nota:_ Isso tecnicamente não é uma chave de API, mas é usado para autenticação, então mantemos essa nomenclatura para consistência.

## Configurar Microsoft Foundry Models: Pelo Portal

> **Nota:** O GitHub Models será descontinuado no final de julho de 2026. O Microsoft Foundry Models é o substituto direto, oferecendo o mesmo catálogo de modelos gratuito para testar e a experiência SDK Azure AI Inference / OpenAI SDK.

1. Vá para o [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) e crie (ou abra) um projeto Foundry.
1. Explore o [catálogo de modelos](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) e implante um modelo, por exemplo `gpt-5-mini`.
1. Na página **Visão Geral** do projeto, copie o **endpoint** e a **chave da API**.
1. Use o valor do endpoint para `AZURE_INFERENCE_ENDPOINT` e o valor da chave para `AZURE_INFERENCE_CREDENTIAL` no seu arquivo `.env`.

## Provedores Offline / Locais

Se preferir não usar uma assinatura na nuvem, você pode rodar modelos compatíveis de código aberto diretamente no seu dispositivo:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - ambiente de execução local da Microsoft. Ele seleciona automaticamente o melhor provedor de execução (NPU, GPU ou CPU) e expõe um endpoint compatível com OpenAI, para que você possa reutilizar a maior parte do código exemplo deste curso com mudanças mínimas. Veja a [documentação Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para começar, ou instale com `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - uma alternativa popular para rodar modelos abertos como Llama, Phi, Mistral e Gemma localmente.


Veja [Lição 19: Construindo com SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) para exemplos práticos usando ambas as opções.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->