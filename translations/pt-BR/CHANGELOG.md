# Registro de Alterações

Todas as mudanças notáveis no currículo Generative AI for Beginners estão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Como este é um
currículo de aprendizado em vez de um pacote de software versionado, as entradas são agrupadas por data.

## [2026-07-06] — Atualização de Modernização de Conteúdo

Uma atualização ampla para manter o currículo preciso para 2026: APIs modernas, nomes atuais de produtos e
nomes de modelos, orientação atualizada do provedor e novas ferramentas para experiência do desenvolvedor.

### Adicionado

- Seção **Microsoft Agent Framework** na lição `17-ai-agents` cobrindo agentes de chat únicos,
  ferramentas/chamada de função, configuração Azure OpenAI (Microsoft Foundry) e orquestração de fluxo de trabalho
  multi-agente (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** documentado como um provedor offline / no dispositivo (junto com Ollama) em
  `00-course-setup/03-providers.md` e na lição `19-slm`.
- **Fluxos de trabalho de integração contínua**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (aplicados no módulo `shared/` mantido,
    orientação no restante do currículo), uma passagem de ESLint consultiva e uma tarefa pytest.
  - `.github/workflows/security.yml` — Análise CodeQL (Python + JavaScript/TypeScript) e
    revisão de dependências em pull requests.
- **Suite de testes** em `tests/` — 41 testes pytest cobrindo o módulo utilitário compartilhado.
- **Habilidade de migração Azure OpenAI → Responses API** em
  `.github/skills/azure-openai-to-responses/` usada para guiar a migração da API.

### Alterado

- **Chat Completions API → Responses API** em todos os exemplos de chat em Python e TypeScript
  (`client.responses.create(...)` → `response.output_text`), incluindo as lições 04, 06, 07, 11,
  15 e 18, além de seus READMEs.
- **Modelos GitHub → Modelos Microsoft Foundry** em todo o texto, links e exemplos. O GitHub Models
  será descontinuado no final de julho de 2026; os exemplos agora apontam para o catálogo de modelos Microsoft Foundry e usam
  as variáveis de ambiente `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` e documentação dos provedores** atualizados para refletir que o Azure OpenAI agora faz parte
  do Microsoft Foundry, e a versão padrão da API foi atualizada para `2024-10-21`.
- **Exemplos TypeScript** (lições 06, 07, 08, 11) migrados do SDK beta obsoleto `@azure/openai`
  para o pacote `openai` (aplicativos de chat usam a Responses API; o app de busca usa o
  cliente de embeddings).
- **Notebooks .NET** (`dotnet/*.dib`) padronizados na versão `Azure.AI.OpenAI` **2.1.0**: lições 06 e 07
  usam a API `ChatClient`, lição 08 usa `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), e
  lição 09 usa `ImageClient` (`GenerateImage`) com `gpt-image-1`, substituindo o legado
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` da versão `1.0.0-beta.9`.
- **Modernização de nomes de produtos**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lições 14, 16, 17) e "Bing" → **Microsoft Copilot** (lição 12), quando se referiam aos
  produtos atuais.
- **DevContainer** (`.devcontainer/`) agora inclui as extensões Pylance, Black, Ruff, ESLint, Prettier e Copilot,
  ativa formatação ao salvar e instala `ruff`, `black`, `mypy` e `pytest` para que as verificações de CI
  possam ser reproduzidas localmente.
- **Geração de imagens** (lição 09) recomenda `gpt-image-1` para Azure (o catálogo Azure removeu
  o `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** atualizado para refletir trabalho concluído (migração da API, CI,
  DevContainer, testes) e fatos atuais (as traduções são produzidas automaticamente pelo
  Azure Co-op Translator; a Assistants API foi substituída pela Responses API).

### Corrigido

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` agora retorna uma
  string vazia para entrada contendo apenas espaços em branco em vez de gerar um erro de "texto muito curto" (consistente com o
  caso `None`). Encontrado e coberto pela nova suite de testes.
- **Exemplos de imagens da lição 09** — correção de bugs reais: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  e uma variável que sobrescrevia o módulo `openai`.
- **Notebook RAG da lição 15** — corrigida a configuração do cliente, substituído o `DataFrame.append`
  removido por `pd.concat` e modernizado o uso do SDK legado.
- Nomes de modelos descontinuados / aposentados (`gpt-3.5-turbo`, `gpt-35-turbo`) substituídos por `gpt-4o-mini`
  nos exemplos ativos; os outputs históricos de fine-tuning da lição 18 foram preservados e anotados
  em vez de reescritos.

### Obsoleto / Notas

- Exemplos de Modelos Microsoft Foundry que usam o SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — os exemplos `githubmodels-*` e `js-githubmodels` e as lições 19, 20,
  e 21 — permanecem na Model Inference API, que **não** suporta a Responses API. Estes são
  intencionalmente mantidos neste SDK.
- `AzureOpenAI()` é mantido intencionalmente onde ainda apropriado (embeddings e geração de imagens),
  pois esses fluxos não fazem parte da migração para Responses API.
- Referências a `text-embedding-ada-002` são mantidas onde um índice de embedding pré-calculado depende delas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->