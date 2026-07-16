# Registo de alterações

Todas as alterações importantes ao currículo Generative AI for Beginners estão documentadas neste ficheiro.

O formato baseia-se em [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Como este é um
currículo de aprendizagem em vez de um pacote de software com versões, as entradas estão agrupadas por data.

## [2026-07-06] — Atualização de Modernização do Conteúdo

Uma atualização abrangente para manter o currículo preciso para 2026: APIs modernas, nomes atuais de produtos e
modelos, orientação atualizada dos fornecedores, e novas ferramentas para a experiência do programador.

### Adicionado

- Secção **Microsoft Agent Framework** na lição `17-ai-agents` abrangendo agentes de chat únicos,
  ferramentas/chamada de funções, configuração Azure OpenAI (Microsoft Foundry), e orquestração
  de fluxo de trabalho multi-agente (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** documentado como fornecedor offline / no dispositivo (junto com Ollama) em
  `00-course-setup/03-providers.md` e na lição `19-slm`.
- **Fluxos de trabalho de integração contínua**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (aplicado no módulo mantido `shared/`
    e em aviso para o resto do currículo), uma passagem de aconselhamento ESLint, e um trabalho pytest.
  - `.github/workflows/security.yml` — análise CodeQL (Python + JavaScript/TypeScript) e
    revisão de dependências em pedidos de pull.
- **Conjunto de testes** sob `tests/` — 41 testes pytest abrangendo o módulo utilitário partilhado.
- **Habilidade de migração Azure OpenAI → Responses API** sob
  `.github/skills/azure-openai-to-responses/` usada para guiar a migração da API.

### Alterado

- **Chat Completions API → Responses API** em todos os exemplos de chat Python e TypeScript
  (`client.responses.create(...)` → `response.output_text`), incluindo as lições 04, 06, 07, 11,
  15 e 18, mais os respetivos READMEs.
- **GitHub Models → Microsoft Foundry Models** em toda a prosa, links e exemplos. GitHub Models
  é descontinuado no final de julho de 2026; os exemplos agora apontam para o catálogo de modelos Microsoft Foundry e usam
  as variáveis de ambiente `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- Atualizadas **`.env.copy`, `AGENTS.md` e documentação dos fornecedores** para refletir que o Azure OpenAI faz agora parte
  do Microsoft Foundry, e a versão padrão da API foi atualizada para `2024-10-21`.
- Exemplos **TypeScript** (lições 06, 07, 08, 11) migrados do SDK beta depreciado `@azure/openai`
  para o pacote `openai` (aplicações de chat usam a Responses API; a aplicação de pesquisa usa o
  cliente de embeddings).
- **Cadernos .NET** (`dotnet/*.dib`) padronizados na versão `Azure.AI.OpenAI` **2.1.0**: lições 06 e 07
  usam a API `ChatClient`, a lição 08 usa `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), e
  a lição 09 usa `ImageClient` (`GenerateImage`) com `gpt-image-1`, substituindo a antiga
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` da versão `1.0.0-beta.9`.
- **Modernização dos nomes dos produtos**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lições 14, 16, 17) e "Bing" → **Microsoft Copilot** (lição 12), onde essas referências indicavam os
  produtos atuais.
- **DevContainer** (`.devcontainer/`) agora inclui as extensões Pylance, Black, Ruff, ESLint, Prettier e Copilot,
  ativa a formatação ao guardar, e instala `ruff`, `black`, `mypy` e `pytest` para que as verificações CI
  possam ser reproduzidas localmente.
- **Geração de imagem** (lição 09) recomenda `gpt-image-1` para Azure (o catálogo Azure eliminou
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** atualizado para refletir o trabalho concluído (migração API, CI,
  DevContainer, testes) e factos atuais (as traduções são produzidas automaticamente pelo
  Azure Co-op Translator; a API Assistants foi substituída pela Responses API).

### Corrigido

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` agora retorna uma
  string vazia para entrada só com espaços em branco em vez de levantar um erro "muito curto" (consistente com o
  caso `None`). Encontrado e coberto pelo novo conjunto de testes.
- **Exemplos de imagem da lição 09** — corrigidos erros reais: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  e uma variável que ocultava o módulo `openai`.
- **Caderno RAG da lição 15** — reparada a configuração do cliente, substituído o removido `DataFrame.append`
  por `pd.concat`, e modernizado o uso legado do SDK.
- Nomes de modelos depreciados / descontinuados (`gpt-3.5-turbo`, `gpt-35-turbo`) substituídos por `gpt-4o-mini`
  em exemplos ativos; saídas históricas de fine-tuning na lição 18 foram preservadas e anotadas
  em vez de reescritas.

### Depreciado / Notas

- Exemplos de **Microsoft Foundry Models** que usam o SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — os exemplos `githubmodels-*` e `js-githubmodels` e as lições 19, 20,
  e 21 — mantêm-se na Model Inference API, que **não** suporta a Responses API. Estes são
  intencionalmente mantidos nesse SDK.
- `AzureOpenAI()` é mantido intencionalmente onde ainda apropriado (embeddings e geração de imagem),
  pois esses fluxos de trabalho não fazem parte da migração para a Responses API.
- Referências a `text-embedding-ada-002` são mantidas onde um índice embutido pré-calculado delas depende.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->