# Registo de alterações

Todas as alterações notáveis ao currículo de IA Generativa para Iniciantes estão documentadas neste ficheiro.

O formato baseia-se em [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Como se trata de um
currículo de aprendizagem e não de um pacote de software versionado, as entradas estão agrupadas por data.

## [2026-07-16] — Validação de Conteúdo + Recursos de Imagem da Aula 09

### Alterado

- **Aula 10 (apps de IA low-code):** atualizados dois links desatualizados `docs.microsoft.com/powerapps/...` do Dataverse
  para o atual `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (verificado ao vivo).
- **Aula 17 (agentes de IA):** modernizado um exemplo de modelo datado (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, e Llama 3.3`) e o nome placeholder de implementação no exemplo do Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **README.md raiz:** adicionado o ID de rastreamento em falta `?WT.mc_id=academic-105485-koreyst` no link
  *Microsoft for Startups*.
- **Recursos de imagem da Aula 09** regenerados com o modelo `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, e
  `images/startup.png` (o par antes/depois do exemplo de edição foi produzido via uma chamada real
  `client.images.edit` com uma máscara gerada).

### Validado

- Auditadas as READMEs das aulas 01, 03, 05, 12, 14, e 16 — todas atualizadas (nomenclatura e links corretos do Microsoft Foundry);
  nenhuma alteração necessária.
- Realizada uma validação completa do markdown em todos os 41 ficheiros markdown no repositório (excluindo traduções) à procura
  de caminhos de documentação obsoletos, locais Microsoft `/en-us/`, nomes de produtos/modelos desatualizados, IDs de rastreio em falta,
  e links/imagens relativos partidos. Apenas a lacuna do ID de rastreamento no *Microsoft for Startups* foi
  passível de ação; todas as outras marcações foram confirmadas como falsos positivos (links de tradução gerados automaticamente,
  placeholders comentados, e URLs estruturais terceiros `/en/`).

## [2026-07-15] — Reescrita da Aula 09 (Aplicações de Imagem) para Modelos GPT Image

### Alterado

- **Reescrita da aula 09 "Construindo Aplicações de Geração de Imagens"** em torno da família de modelos **`gpt-image`**
  atual (padrão **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` também GA), substituindo o
  conteúdo legado DALL·E 2/3. Correções principais:
  - os modelos `gpt-image` retornam a imagem em **base64 (`b64_json`)**, não uma URL. Atualizados todos os exemplos para
    `base64.b64decode(...)` em vez de descarregar uma `url` com `requests`.
  - Atualizada a versão da API de imagem para `2025-04-01-preview`.

  - Substituída a seção inventada "temperature" (os modelos de imagem não utilizam `temperature`) e o
    conteúdo de **variações** de imagem exclusivo do DALL·E-2 por uma seção de **edição de imagem** (máscara/pintura).
  - Atualizados `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, ambos
    cadernos de tarefas (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), e o caderno .NET `.dib`.

### Removido

- Foram eliminados os exemplos obsoletos `python/aoai-app-variation.py` e `python/oai-app-variation.py`
  (`images.create_variation` é exclusivo do DALL·E-2 e não suportado pelo `gpt-image`).
- Eliminados 4 recursos de imagem órfãos ligados à seção removida de comparação de temperatura
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Removida a dependência desnecessária `requests` dos exemplos Python e dos requisitos da lição.

### Validado

- Executado `aoai-app.py` de ponta a ponta contra um modelo `gpt-image-1.5` em produção e confirmado que o fluxo de
  decodificação/salvamento base64 gera um PNG. Cadernos confirmados como JSON válido.

## [2026-07-14] — Atualização do Modelo Padrão + Orientação para Modelo de Raciocínio

### Alterado

- **Modelo padrão de chat `gpt-4o-mini` → `gpt-5-mini`** em todos os exemplos executáveis da ementa,
  documentação e configuração. Esta alteração deve-se ao ciclo de vida dos modelos: na Microsoft Foundry,
  `gpt-4o-mini` (aposenta a 2026-10-01) e toda a família `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, aposenta a 2026-10-14) estão a **Ser Preteridos**, enquanto que a **Família GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) está Geralmente Disponível** (aposenta a 2027-02-06). Atualizados:
  - `.env.copy`, `00-course-setup/03-providers.md` (implantação recomendada e comandos `az cognitiveservices`
    para deploy), e os README das lições 04, 06, 07 e 15.
  - Exemplos Python na lição 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) e scripts da lição 08.
  - Exemplos TypeScript / JavaScript nas lições 06, 07 e 11, e os cadernos .NET `.dib` para
    as lições 06 e 07.
  - Cadernos de tarefas nas lições 04, 06, 07 e 11 (células de código), além dos exemplos em docstring de `shared/python/api_utils.py`.
    .

- **Orientação de parâmetro para modelo de raciocínio (novo).** `gpt-5-mini` é um modelo de *raciocínio*: não suporta `temperature`/`top_p`, e usa `max_completion_tokens` (completamentos de chat) / 
  `max_output_tokens` (API de Respostas) em vez de `max_tokens`. Em conformidade:
  

  - Removido `temperature`/`top_p`/`max_tokens` das amostras que agora usam por defeito `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, lesson 15 RAG README).
  - Adicionada uma nota **"Modelos de raciocínio não usam `temperature`"** na lição 06, explicando que
    os modelos de raciocínio são orientados com **engenharia de prompt + controlos de raciocínio** em vez de
    controlos de amostragem, enquanto `temperature`/`top_p` continuam válidos em modelos não racionais
    (GPT-4.x, Mistral, Llama, Phi, modelos open).
- **`gpt-5-mini` não é usado no tutorial de fine-tuning (lição 18).** O GPT-5 suporta apenas
  fine-tuning por reforço (RFT); o walkthrough da lição 18 para fine-tuning supervisionado (SFT) mantém
  `gpt-4.1-mini`, que suporta SFT/DPO.
- **As demos de Temperature usam um modelo Llama.** Para continuar a ensinar `temperature` (que os modelos de raciocínio
  rejeitam), é usado um modelo `Llama-3.3-70B-Instruct` via o endpoint Foundry Models. Adicionada uma nova variável
  `AZURE_INFERENCE_CHAT_MODEL` ao `.env.copy`; os notebooks `githubmodels` das lições 04/06 e a amostra
  `06` `js-githubmodels` lêem-na (recuando para `Llama-3.3-70B-Instruct`) e mantêm as suas demos de
  `temperature`/`top_p`/`max_tokens`.
- **Amostras JS / .NET atualizadas para GPT-5.** Removido `temperature`/`top_p`/`max_tokens` das amostras GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - que também eleva o `MaxOutputTokenCount`
  para que a saída do raciocínio não seja truncada). A amostra `06` `js-githubmodels` agora usa Llama para manter a sua
  demo de temperature. O `.dib` indica que `Azure.AI.Inference` + um modelo Llama é a forma de
  demonstrar `Temperature` em .NET.
- Mantidos `gpt-4o-mini` / `gpt-5-mini` onde permanecem precisos: referências de codificação de tokens `tiktoken`,
  listas de disponibilidade no catálogo de modelos e modelos de fala da lição 02 (`gpt-4o-transcribe`).
- As amostras da lição 20 (Mistral) e 21 (Meta) mantêm `temperature`/`max_tokens` porque visam
  modelos Mistral/Llama, que suportam esses parâmetros.

## [2026-07-06] — Atualização da Modernização de Conteúdo

Uma atualização abrangente para manter o currículo preciso para 2026: APIs modernas, nomes atuais de produtos e
nomes de modelos, orientações atualizadas para provedores e novas ferramentas para a experiência do desenvolvedor.

### Adicionado

- Seção **Microsoft Agent Framework** na lição `17-ai-agents` cobrindo agentes de chat único,
  ferramentas/chamada de funções, configuração do Azure OpenAI (Microsoft Foundry) e orquestração
  de fluxos multi-agentes (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** documentado como provedor offline / local (junto com Ollama) em
  `00-course-setup/03-providers.md` e na lição `19-slm`.
- **Workflows de integração contínua**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (aplicado ao módulo mantido `shared/`
    , passagem consultiva ESLint pelo restante do currículo), e um job pytest.
  - `.github/workflows/security.yml` — análise CodeQL (Python + JavaScript/TypeScript) e
    revisão de dependências em pull requests.
- **Suite de testes** sob `tests/` — 41 testes pytest cobrindo o módulo utilitário compartilhado.
- **Skill de migração Azure OpenAI → Responses API** sob
  `.github/skills/azure-openai-to-responses/` usada para orientar a migração da API.

### Alterado

- **Chat Completions API → Responses API** em todas as amostras de chat Python e TypeScript
  (`client.responses.create(...)` → `response.output_text`), incluindo as lições 04, 06, 07, 11,
  15 e 18, mais os seus READMEs.
- **GitHub Models → Microsoft Foundry Models** em toda a prosa, links e amostras. O GitHub Models
  será descontinuado no final de julho de 2026; as amostras agora apontam para o catálogo do Microsoft Foundry
  e usam as variáveis de ambiente `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` e docs de provedores** atualizados para refletir que Azure OpenAI agora faz parte do
  Microsoft Foundry, e a versão API padrão atualizada para `2024-10-21`.
- **Amostras TypeScript** (lições 06, 07, 08, 11) migradas do SDK beta obsoleto `@azure/openai`
  para o pacote `openai` (apps de chat usam a Responses API; o app de pesquisa usa o
  cliente de embeddings).
- **Notebooks .NET** (`dotnet/*.dib`) padronizados para `Azure.AI.OpenAI` **2.1.0**: lições 06 e 07
  usam a API `ChatClient`, lição 08 usa `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), e
  lição 09 usa `ImageClient` (`GenerateImage`) com `gpt-image-1`, substituindo a legado
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` da `1.0.0-beta.9`.
- **Modernização dos nomes de produtos**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lições 14, 16, 17) e "Bing" → **Microsoft Copilot** (lição 12), onde esses nomes se referiam aos
  produtos atuais.
- **DevContainer** (`.devcontainer/`) agora inclui Pylance, Black, Ruff, ESLint, Prettier e Copilot
  como extensões, ativa formatação ao salvar, e instala `ruff`, `black`, `mypy` e `pytest` para que as verificações CI
  possam ser reproduzidas localmente.
- **Geração de imagens** (lição 09) recomenda `gpt-image-1` para Azure (o catálogo Azure retirou
  o `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** atualizado para refletir o trabalho concluído (migração da API, CI,
  DevContainer, testes) e factos atuais (as traduções são produzidas automaticamente pelo
  Azure Co-op Translator; a API Assistants foi substituída pela API Responses).

### Corrigido

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` agora retorna uma
  cadeia vazia para entradas compostas apenas por espaços em branco em vez de lançar um erro de "muito curto" (consistente com o
  caso `None`). Encontrado e coberto pela nova suite de testes.
- **Exemplos de imagens da Aula 09** — corrigidos erros reais: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  e uma variável que sombreava o módulo `openai`.
- **Notebook RAG da Aula 15** — reparada a configuração do cliente, substituído `DataFrame.append`
  removido por `pd.concat`, e modernizado o uso da SDK legada.
- Nomes de modelos descontinuados / retirados (`gpt-3.5-turbo`, `gpt-35-turbo`) substituídos por `gpt-4o-mini`
  em exemplos ativos; saídas históricas de fine-tuning na aula 18 foram preservadas e anotadas
  em vez de reescritas.

### Obsoleto / Notas

- **Exemplos dos Modelos Microsoft Foundry** que usam o SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — os exemplos `githubmodels-*` e `js-githubmodels` e as aulas 19, 20,
  e 21 — permanecem na Model Inference API, que **não** suporta a API Responses. Estes mantêm-se
  intencionalmente nesse SDK.
- `AzureOpenAI()` é mantido intencionalmente onde ainda é apropriado (embedding e geração de imagens),
  pois esses fluxos de trabalho não fazem parte da migração para a API Responses.
- Referências a `text-embedding-ada-002` são mantidas onde um índice de embeddings pré-computado depende delas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->