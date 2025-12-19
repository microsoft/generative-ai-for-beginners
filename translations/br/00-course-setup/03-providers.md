<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T14:36:52+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "br"
}
-->
# Escolhendo e Configurando um Provedor de LLM 🔑

As tarefas **podem** também ser configuradas para funcionar com uma ou mais implantações de Large Language Model (LLM) por meio de um provedor de serviço suportado como OpenAI, Azure ou Hugging Face. Estes fornecem um _endpoint hospedado_ (API) que podemos acessar programaticamente com as credenciais corretas (chave API ou token). Neste curso, discutimos esses provedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com diversos modelos incluindo a série principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco em prontidão empresarial
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos open-source e servidor de inferência

**Você precisará usar suas próprias contas para esses exercícios**. As tarefas são opcionais, então você pode escolher configurar um, todos - ou nenhum - dos provedores com base em seus interesses. Algumas orientações para cadastro:

| Cadastro | Custo | Chave API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Baseado em projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sem código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Múltiplos Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Início rápido SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Início rápido Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [É necessário solicitar acesso antecipadamente](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes provedores. As tarefas que requerem um provedor específico conterão uma dessas tags no nome do arquivo:

- `aoai` - requer endpoint e chave Azure OpenAI
- `oai` - requer endpoint e chave OpenAI
- `hf` - requer token Hugging Face

Você pode configurar um, nenhum ou todos os provedores. As tarefas relacionadas simplesmente apresentarão erro se as credenciais estiverem ausentes.

## Criar arquivo `.env`

Assumimos que você já leu as orientações acima, se cadastrou no provedor relevante e obteve as credenciais de autenticação necessárias (API_KEY ou token). No caso do Azure OpenAI, assumimos também que você possui uma implantação válida de um Serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implantado para conclusão de chat.

O próximo passo é configurar suas **variáveis de ambiente locais** da seguinte forma:

1. Procure na pasta raiz um arquivo `.env.copy` que deve conter algo assim:

   ```bash
   # Provedor OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Padrão definido!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copie esse arquivo para `.env` usando o comando abaixo. Este arquivo está _gitignore-d_, mantendo os segredos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os espaços reservados à direita do `=`) conforme descrito na próxima seção.

4. (Opcional) Se você usar GitHub Codespaces, tem a opção de salvar variáveis de ambiente como _segredos do Codespaces_ associados a este repositório. Nesse caso, não será necessário configurar um arquivo .env local. **No entanto, note que essa opção funciona apenas se você usar GitHub Codespaces.** Você ainda precisará configurar o arquivo .env se usar Docker Desktop.

## Preencher arquivo `.env`

Vamos dar uma olhada rápida nos nomes das variáveis para entender o que representam:

| Variável  | Descrição  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este é o token de acesso do usuário que você configurou no seu perfil |
| OPENAI_API_KEY | Esta é a chave de autorização para usar o serviço em endpoints OpenAI não Azure |
| AZURE_OPENAI_API_KEY | Esta é a chave de autorização para usar esse serviço |
| AZURE_OPENAI_ENDPOINT | Este é o endpoint implantado para um recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este é o endpoint de implantação do modelo de _geração de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este é o endpoint de implantação do modelo de _embeddings de texto_ |
| | |

Nota: As duas últimas variáveis do Azure OpenAI refletem um modelo padrão para conclusão de chat (geração de texto) e busca vetorial (embeddings), respectivamente. As instruções para configurá-las serão definidas nas tarefas relevantes.

## Configurar Azure: Pelo Portal

Os valores do endpoint e da chave Azure OpenAI serão encontrados no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), então vamos começar por lá.

1. Acesse o [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clique na opção **Chaves e Endpoint** na barra lateral (menu à esquerda).
1. Clique em **Mostrar Chaves** - você deverá ver o seguinte: CHAVE 1, CHAVE 2 e Endpoint.
1. Use o valor da CHAVE 1 para AZURE_OPENAI_API_KEY
1. Use o valor do Endpoint para AZURE_OPENAI_ENDPOINT

Em seguida, precisamos dos endpoints para os modelos específicos que implantamos.

1. Clique na opção **Implantações de modelo** na barra lateral (menu à esquerda) do recurso Azure OpenAI.
1. Na página de destino, clique em **Gerenciar Implantações**

Isso o levará ao site Azure OpenAI Studio, onde encontraremos os outros valores conforme descrito abaixo.

## Configurar Azure: Pelo Studio

1. Navegue até o [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do seu recurso** conforme descrito acima.
1. Clique na aba **Implantações** (barra lateral, à esquerda) para ver os modelos atualmente implantados.
1. Se o modelo desejado não estiver implantado, use **Criar nova implantação** para implantá-lo.
1. Você precisará de um modelo de _geração de texto_ - recomendamos: **gpt-35-turbo**
1. Você precisará de um modelo de _embedding de texto_ - recomendamos **text-embedding-ada-002**

Agora atualize as variáveis de ambiente para refletir o _Nome da implantação_ usado. Isso normalmente será o mesmo nome do modelo, a menos que você tenha alterado explicitamente. Então, como exemplo, você pode ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Não esqueça de salvar o arquivo .env quando terminar**. Agora você pode sair do arquivo e retornar às instruções para executar o notebook.

## Configurar OpenAI: Pelo Perfil

Sua chave API OpenAI pode ser encontrada na sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se você não tiver uma, pode se cadastrar e criar uma chave API. Depois de obter a chave, você pode usá-la para preencher a variável `OPENAI_API_KEY` no arquivo `.env`.

## Configurar Hugging Face: Pelo Perfil

Seu token Hugging Face pode ser encontrado no seu perfil em [Tokens de Acesso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não publique ou compartilhe esses tokens publicamente. Em vez disso, crie um novo token para uso neste projeto e copie-o no arquivo `.env` sob a variável `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente, isso não é uma chave API, mas é usado para autenticação, então mantemos essa convenção de nomenclatura para consistência.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->