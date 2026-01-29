# Escolher e Configurar um Provedor LLM 🔑

As tarefas **podem** também ser configuradas para funcionar com uma ou mais implementações de Modelos de Linguagem Grande (LLM) através de um provedor de serviço suportado como OpenAI, Azure ou Hugging Face. Estes fornecem um _endpoint hospedado_ (API) ao qual podemos aceder programaticamente com as credenciais corretas (chave API ou token). Neste curso, discutimos estes provedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) com modelos diversos incluindo a série principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI com foco em prontidão empresarial
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos open-source e servidor de inferência

**Vai precisar de usar as suas próprias contas para estes exercícios**. As tarefas são opcionais, por isso pode escolher configurar um, todos - ou nenhum - dos provedores conforme os seus interesses. Algumas orientações para inscrição:

| Inscrição | Custo | Chave API | Playground | Comentários |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preços](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Baseado em projeto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sem Código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Vários Modelos Disponíveis |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preços](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Início Rápido SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Início Rápido Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [É Necessário Solicitar Acesso](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preços](https://huggingface.co/pricing) | [Tokens de Acesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tem modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Siga as instruções abaixo para _configurar_ este repositório para uso com diferentes provedores. As tarefas que requerem um provedor específico conterão uma destas etiquetas no nome do ficheiro:

- `aoai` - requer endpoint e chave Azure OpenAI
- `oai` - requer endpoint e chave OpenAI
- `hf` - requer token Hugging Face

Pode configurar um, nenhum ou todos os provedores. As tarefas relacionadas simplesmente gerarão erro se as credenciais estiverem em falta.

## Criar ficheiro `.env`

Assumimos que já leu as orientações acima, inscreveu-se no provedor relevante e obteve as credenciais de autenticação necessárias (API_KEY ou token). No caso do Azure OpenAI, assumimos também que tem uma implementação válida de um Serviço Azure OpenAI (endpoint) com pelo menos um modelo GPT implementado para conclusão de chat.

O próximo passo é configurar as suas **variáveis de ambiente locais** da seguinte forma:

1. Procure na pasta raiz um ficheiro `.env.copy` que deverá ter um conteúdo como este:

   ```bash
   # Fornecedor OpenAI
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

2. Copie esse ficheiro para `.env` usando o comando abaixo. Este ficheiro está _gitignore-d_, mantendo os segredos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Preencha os valores (substitua os espaços reservados do lado direito do `=`) conforme descrito na secção seguinte.

4. (Opcional) Se usar GitHub Codespaces, tem a opção de guardar variáveis de ambiente como _segredos Codespaces_ associados a este repositório. Nesse caso, não precisará de configurar um ficheiro .env local. **No entanto, note que esta opção funciona apenas se usar GitHub Codespaces.** Ainda precisará de configurar o ficheiro .env se usar Docker Desktop.

## Preencher ficheiro `.env`

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

Nota: As duas últimas variáveis Azure OpenAI refletem um modelo padrão para conclusão de chat (geração de texto) e pesquisa vetorial (embeddings), respetivamente. As instruções para configurá-las serão definidas nas tarefas relevantes.

## Configurar Azure: Pelo Portal

Os valores do endpoint e chave Azure OpenAI serão encontrados no [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), por isso vamos começar por aí.

1. Vá ao [Portal Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clique na opção **Chaves e Endpoint** na barra lateral (menu à esquerda).
1. Clique em **Mostrar Chaves** - deverá ver o seguinte: CHAVE 1, CHAVE 2 e Endpoint.
1. Use o valor da CHAVE 1 para AZURE_OPENAI_API_KEY
1. Use o valor do Endpoint para AZURE_OPENAI_ENDPOINT

De seguida, precisamos dos endpoints para os modelos específicos que implementámos.

1. Clique na opção **Implementações de modelo** na barra lateral (menu à esquerda) para o recurso Azure OpenAI.
1. Na página de destino, clique em **Gerir Implementações**

Isto levará ao website Azure OpenAI Studio, onde encontraremos os outros valores conforme descrito abaixo.

## Configurar Azure: Pelo Studio

1. Navegue para o [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **a partir do seu recurso** conforme descrito acima.
1. Clique no separador **Implementações** (barra lateral, esquerda) para ver os modelos atualmente implementados.
1. Se o modelo desejado não estiver implementado, use **Criar nova implementação** para o implementar.
1. Vai precisar de um modelo de _geração de texto_ - recomendamos: **gpt-35-turbo**
1. Vai precisar de um modelo de _embedding de texto_ - recomendamos **text-embedding-ada-002**

Agora atualize as variáveis de ambiente para refletir o _Nome da implementação_ usado. Normalmente será o mesmo que o nome do modelo, a menos que o tenha alterado explicitamente. Por exemplo, poderá ter:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Não se esqueça de guardar o ficheiro .env quando terminar**. Pode agora sair do ficheiro e voltar às instruções para executar o notebook.

## Configurar OpenAI: Pelo Perfil

A sua chave API OpenAI pode ser encontrada na sua [conta OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se não tiver uma, pode inscrever-se para uma conta e criar uma chave API. Depois de ter a chave, pode usá-la para preencher a variável `OPENAI_API_KEY` no ficheiro `.env`.

## Configurar Hugging Face: Pelo Perfil

O seu token Hugging Face pode ser encontrado no seu perfil em [Tokens de Acesso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Não publique nem partilhe estes publicamente. Em vez disso, crie um novo token para uso neste projeto e copie-o para o ficheiro `.env` na variável `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente, isto não é uma chave API, mas é usado para autenticação, por isso mantemos essa convenção de nomenclatura para consistência.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->