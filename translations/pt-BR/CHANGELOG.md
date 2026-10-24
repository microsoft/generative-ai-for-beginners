# Registro de alterações

Todas as mudanças notáveis no currículo de IA Generativa para Iniciantes estão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Como este é um
currículo de aprendizado em vez de um pacote de software versionado, as entradas são agrupadas por data.

## [2026-07-16] — Validação de Conteúdo + Recursos de Imagem da Aula 09

### Alterado

- **Aula 10 (apps de IA low-code):** atualizados dois links aposentados `docs.microsoft.com/powerapps/...` Dataverse
  para o atual `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (verificado ao vivo).
- **Aula 17 (agentes de IA):** modernizado um exemplo de modelo desatualizado (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) e um nome de implantação placeholder na amostra do Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Raiz `README.md`:** adicionou o ID de rastreamento `?WT.mc_id=academic-105485-koreyst` faltante ao
  link *Microsoft for Startups*.
- **Recursos de imagem da Aula 09** regenerados com o modelo `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, e
  `images/startup.png` (o par antes/depois do exemplo de edição foi produzido via uma chamada real
  `client.images.edit` com uma máscara gerada).

### Validado

- Auditaram os READMEs das aulas 01, 03, 05, 12, 14 e 16 — todos atuais (nomes e links corretos do Microsoft Foundry);
  nenhuma mudança requerida.
- Realizada uma validação completa de markdown em todos os 41 arquivos markdown do repositório (excluindo traduções) para
  caminhos de documentação depreciados, `/en-us/` locais Microsoft, nomes de produtos/modelos desatualizados, IDs de rastreamento faltantes
  e links/imagens relativos quebrados. Apenas a lacuna do ID de rastreamento do *Microsoft for Startups* foi
  acionável; todas as outras sinalizações foram confirmadas como falso positivo (links de tradução auto-gerados,
  placeholders comentados e URLs estruturais de terceiros `/en/`).

## [2026-07-15] — Reescrita da Aula 09 (Aplicações de Imagem) para Modelos de Imagem GPT

### Alterado

- **Reescreveu a lição 09 "Construindo Aplicações de Geração de Imagens"** em torno da família atual de modelos **`gpt-image`**  
  (padrão **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` também GA), substituindo o  
  conteúdo legado do DALL·E 2/3. Correções principais:  
  - modelos `gpt-image` retornam a imagem como **base64 (`b64_json`)**, não uma URL. Atualizados todos os exemplos para  
    `base64.b64decode(...)` em vez de baixar um `url` com `requests`.  
  - Atualizada a versão da API de imagem para `2025-04-01-preview`.  
  - Substituída a seção fabricada "temperatura" (modelos de imagem não usam `temperature`) e o  
    conteúdo de **variações** de imagem exclusivo do DALL·E-2 por uma seção de **edição de imagem** (máscara/pintura).  
  - Atualizados `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, ambos  
    cadernos de atribuição (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),  
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), e o caderno .NET `.dib`.  

### Removido  

- Excluídos os exemplos obsoletos `python/aoai-app-variation.py` e `python/oai-app-variation.py`
  (`images.create_variation` é só para DALL·E-2 e não é suportado pelo `gpt-image`).
- Excluídos 4 ativos de imagem órfãos ligados à seção removida de comparação de temperatura
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Removida a dependência desnecessária `requests` dos exemplos Python e requisitos da lição.

### Validado

- Executado `aoai-app.py` de ponta a ponta contra um modelo `gpt-image-1.5` implantado e confirmado que o fluxo de
  decodificação/salvamento base64 produz um PNG. Notebooks confirmados como JSON válido.

## [2026-07-14] — Atualização do Modelo Padrão + Orientação para Modelos de Raciocínio

### Alterado

- **Modelo de chat padrão `gpt-4o-mini` → `gpt-5-mini`** em todos os exemplos executáveis do currículo,
  documentação e configuração. Isso foi motivado pelo status do ciclo de vida do modelo: no Microsoft Foundry,
  `gpt-4o-mini` (aposenta em 2026-10-01) e toda a família `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, se aposentam em 2026-10-14) estão **Descontinuando**, enquanto a **família GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) está Geralmente Disponível** (aposenta em 2027-02-06). Atualizado:
  - `.env.copy`, `00-course-setup/03-providers.md` (comandos recomendados de implantação e `az cognitiveservices`),
    e os READMEs das lições 04, 06, 07 e 15.
  - Exemplos Python na lição 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) e scripts da lição 08.
  - Exemplos TypeScript / JavaScript nas lições 06, 07 e 11, e os notebooks `.dib` .NET para
    lições 06 e 07.
  - Notebooks das tarefas nas lições 04, 06, 07 e 11 (células de código), mais exemplos de `shared/python/api_utils.py`
    em docstrings.
- **Orientação para parâmetros de modelos de raciocínio (novo).** `gpt-5-mini` é um modelo de *raciocínio*: ele **não**
  suporta `temperature`/`top_p`, e usa `max_completion_tokens` (completions de chat) /
  `max_output_tokens` (API Responses) em vez de `max_tokens`. Assim:
  - Removidos `temperature`/`top_p`/`max_tokens` dos exemplos que agora usam `gpt-5-mini` por padrão
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, README da lição 15 RAG).
  - Adicionada a nota **"Modelos de raciocínio não usam `temperature`"** na lição 06, explicando que
    modelos de raciocínio são controlados por **engenharia de prompt + controles de raciocínio** em vez dos
    botões de amostragem, enquanto `temperature`/`top_p` continuam válidos em modelos sem raciocínio
    (GPT-4.x, Mistral, Llama, Phi, modelos abertos).
- **`gpt-5-mini` não é usado no tutorial de fine-tuning (lição 18).** GPT-5 suporta só
  fine-tuning por reforço (RFT); o tutorial de fine-tuning supervisionado (SFT) da lição 18 mantém
  `gpt-4.1-mini`, que suporta SFT/DPO.
- **Demos de temperatura usam um modelo Llama.** Para continuar ensinando `temperature` (que os modelos de raciocínio
  rejeitam), um modelo `Llama-3.3-70B-Instruct` é usado via o endpoint de Modelos Foundry. Adicionada uma nova
  variável `AZURE_INFERENCE_CHAT_MODEL` ao `.env.copy`; os notebooks `githubmodels` das lições 04/06 e
  o exemplo `06` `js-githubmodels` a lêem (retornando para `Llama-3.3-70B-Instruct`) e mantêm seus
  demos `temperature`/`top_p`/`max_tokens`.
- **Exemplos JS / .NET atualizados para GPT-5.** Removidos `temperature`/`top_p`/`max_tokens` dos exemplos GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - que também
  levanta `MaxOutputTokenCount` para que a saída de raciocínio não seja truncada). O exemplo `06` `js-githubmodels`
  agora usa Llama para manter sua demo de temperatura. A `.dib` observa que `Azure.AI.Inference` + um modelo Llama é o jeito
  de demonstrar `Temperature` em .NET.
- Mantidos `gpt-4o-mini` / `gpt-5-mini` onde permanecem precisos: referências de tokenização `tiktoken`,
  listas de disponibilidade no catálogo de modelos e modelos de fala da lição 02 (`gpt-4o-transcribe`).
- As amostras da lição 20 (Mistral) e 21 (Meta) mantêm `temperature`/`max_tokens` porque elas se destinam
  a modelos Mistral/Llama, que suportam esses parâmetros.

## [2026-07-06] — Atualização de Modernização de Conteúdo

Uma atualização ampla para manter o currículo preciso para 2026: APIs modernas, nomes atuais de produtos e
nomes de modelos, orientação atualizada de provedores e novas ferramentas de experiência do desenvolvedor.

### Adicionado

- Seção **Microsoft Agent Framework** na lição `17-ai-agents` cobrindo agentes de chat únicos,
  chamada de ferramenta/função, configuração Azure OpenAI (Microsoft Foundry) e orquestração de
  fluxo de trabalho multi-agente (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** documentado como provedor offline / on-device (junto com Ollama) em
  `00-course-setup/03-providers.md` e lição `19-slm`.
- **Workflows de integração contínua**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (exigido no módulo `shared/` mantido,
    orientação para o restante do currículo), passagem ESLint opcional e trabalho pytest.
  - `.github/workflows/security.yml` — análise CodeQL (Python + JavaScript/TypeScript) e
    revisão de dependências em pull requests.
- **Suite de teste** sob `tests/` — 41 testes pytest cobrindo o módulo utilitário compartilhado.
- **Habilidade de migração Azure OpenAI → Responses API** sob
  `.github/skills/azure-openai-to-responses/` usada para guiar a migração da API.

### Alterado

- **Chat Completions API → Responses API** em todos os exemplos de chat Python e TypeScript
  (`client.responses.create(...)` → `response.output_text`), incluindo as lições 04, 06, 07, 11,
  15 e 18, além dos seus READMEs.
- **Modelos GitHub → Modelos Microsoft Foundry** em toda a prosa, links e exemplos. Modelos GitHub
  serão descontinuados no final de julho de 2026; exemplos agora apontam para o catálogo de modelos Microsoft Foundry e utilizam
  as variáveis de ambiente `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` e documentação do provedor** atualizadas para refletir que o Azure OpenAI agora faz parte
  do Microsoft Foundry, e a versão padrão da API foi atualizada para `2024-10-21`.
- **Exemplos TypeScript** (lições 06, 07, 08, 11) migrados do SDK beta descontinuado `@azure/openai`
  para o pacote `openai` (aplicativos de chat usam a API Responses; o aplicativo de busca usa o
  client embeddings).
- **Notebooks .NET** (`dotnet/*.dib`) padronizados na versão `Azure.AI.OpenAI` **2.1.0**: lições 06 e 07
  usam a API `ChatClient`, lição 08 usa `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), e
  lição 09 usa `ImageClient` (`GenerateImage`) com `gpt-image-1`, substituindo o legado
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` do `1.0.0-beta.9`.
- **Modernização dos nomes dos produtos**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lições 14, 16, 17) e "Bing" → **Microsoft Copilot** (lição 12), onde esses se referiam aos
  produtos atuais.
- **DevContainer** (`.devcontainer/`) agora inclui as extensões Pylance, Black, Ruff, ESLint, Prettier e Copilot,
  ativa formatação ao salvar e instala `ruff`, `black`, `mypy` e `pytest` para que checagens CI
  possam ser reproduzidas localmente.
- **Geração de imagens** (lição 09) recomenda `gpt-image-1` para Azure (o catálogo Azure removeu
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** atualizado para refletir o trabalho concluído (migração da API, CI,
  DevContainer, testes) e fatos atuais (traduções são produzidas automaticamente pelo
  Azure Co-op Translator; a API Assistants foi substituída pela API Responses).

### Corrigido

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` agora retorna uma
  string vazia para entrada contendo somente espaços em branco, em vez de gerar um erro de "muito curto" (consistente com o
  caso `None`). Encontrado e coberto pela nova suíte de testes.
- **Amostras de imagens da Aula 09** — corrigidos bugs reais: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  e uma variável que sombreava o módulo `openai`.
- **Notebook RAG da Aula 15** — reparada a configuração do cliente, substituído `DataFrame.append` removido
  por `pd.concat`, e modernizado o uso do SDK legado.
- Nomes de modelos descontinuados/aposentados (`gpt-3.5-turbo`, `gpt-35-turbo`) substituídos por `gpt-4o-mini`
  nas amostras ativas; resultados históricos de fine-tuning na aula 18 foram preservados e anotados
  ao invés de reescritos.

### Descontinuado / Notas

- **Amostras dos Modelos Microsoft Foundry** que usam o SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — as amostras `githubmodels-*` e `js-githubmodels` e as aulas 19, 20,
  e 21 — permanecem na API Model Inference, que **não** suporta a API Responses. Estas ficam
  intencionalmente naquela SDK.
- `AzureOpenAI()` é mantido intencionalmente onde ainda apropriado (embeddings e geração de imagens),
  pois esses fluxos de trabalho não fazem parte da migração para a API Responses.
- Referências `text-embedding-ada-002` são mantidas onde um índice de embedding pré-calculado depende delas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->