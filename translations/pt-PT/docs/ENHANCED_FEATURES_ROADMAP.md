# Roteiro de Funcionalidades Melhoradas e Melhorias

Este documento descreve as melhorias recomendadas para o currículo de IA Generativa para Iniciantes, com base numa revisão completa do código e análise das melhores práticas da indústria.

## Resumo Executivo

A base de código foi analisada em termos de segurança, qualidade de código e eficácia educativa. Este documento apresenta recomendações para correções imediatas, melhorias a curto prazo e aperfeiçoamentos futuros.

---

## 1. Melhorias de Segurança (Prioridade: Crítica)

### 1.1 Correções Imediatas (Concluídas)

| Problema | Ficheiros Afetados | Estado |
|-------|----------------|--------|
| SECRET_KEY codificado diretamente | `05-advanced-prompts/python/aoai-solution.py` | Corrigido |
| Falta de validação do ambiente | Vários ficheiros JS/TS | Corrigido |
| Chamadas de funções inseguras | `11-integrating-with-function-calling/js-githubmodels/app.js` | Corrigido |
| Fugas de handles de ficheiros | `08-building-search-applications/scripts/` | Corrigido |
| Falta de timeouts em requests | `09-building-image-applications/python/` | Corrigido |

### 1.2 Funcionalidades Adicionais de Segurança Recomendadas

1. **Exemplos de Limitação de Taxa**
   - Adicionar código de exemplo a mostrar como implementar limitação de taxa para chamadas API
   - Demonstrar padrões de recuo exponencial

2. **Rotação de Chaves API**
   - Incluir documentação sobre melhores práticas para rotação de chaves API
   - Incluir exemplos de utilização do Azure Key Vault ou serviços similares

3. **Integração de Segurança de Conteúdo**
   - Adicionar exemplos usando a API Azure Content Safety
   - Demonstrar padrões de moderação de entrada/saída

---

## 2. Melhorias na Qualidade do Código

### 2.1 Ficheiros de Configuração Adicionados

| Ficheiro | Finalidade |
|------|---------|
| `.eslintrc.json` | Regras de linting para JavaScript/TypeScript |
| `.prettierrc` | Padrões de formatação de código |
| `pyproject.toml` | Configuração de ferramentas Python (Black, Ruff, mypy) |

### 2.2 Utilitários Partilhados Criados

Novo módulo `shared/python/` com:
- `env_utils.py` - Gestão de variáveis de ambiente
- `input_validation.py` - Validação e sanitização de inputs
- `api_utils.py` - Wrappers seguros para pedidos API

### 2.3 Melhorias Recomendadas no Código

1. **Cobertura de Tipos**
   - Adicionar anotações de tipo a todos os ficheiros Python
   - Ativar modo estrito de TypeScript em todos os projetos TS

2. **Padrões de Documentação**
   - Adicionar docstrings a todas as funções Python
   - Adicionar comentários JSDoc a todas as funções JavaScript/TypeScript

3. **Framework de Testes**
   - Adicionar configuração pytest e testes de exemplo _(feito: configuração pytest no `pyproject.toml`; testes de exemplo para os utilitários partilhados em [`tests/`](../../../tests) executados em CI)_
   - Adicionar configuração Jest para JavaScript/TypeScript

---

## 3. Melhorias Educativas

### 3.1 Novos Tópicos de Aula

1. **Segurança em Aplicações de IA** (Proposta de Aula 22)
   - Ataques e defesas de injeção de prompt
   - Gestão de chaves API
   - Moderação de conteúdo
   - Limitação de taxa e prevenção de abusos

2. **Desdobramento em Produção** (Proposta de Aula 23)
   - Containarização com Docker
   - Pipelines CI/CD
   - Monitorização e registos
   - Gestão de custos

3. **Técnicas Avançadas de RAG** (Proposta de Aula 24)
   - Pesquisa híbrida (keyword + semântica)
   - Estratégias de re-ranking
   - RAG multimodal
   - Métricas de avaliação

### 3.2 Melhorias nas Aulas Existentes

| Aula | Melhoria Recomendada |
|--------|------------------------|
| 06 - Geração de Texto | Adicionar exemplos de respostas em streaming |
| 07 - Aplicações de Chat | Adicionar padrões de memória de conversa |
| 08 - Aplicações de Pesquisa | Adicionar comparação de bases de dados vetoriais |
| 09 - Geração de Imagem | Adicionar exemplos de edição/variação de imagem |
| 11 - Função de Chamada | Adicionar chamadas de função paralelas |
| 15 - RAG | Adicionar comparação de estratégias de chunking |
| 17 - Agentes IA | Adicionar orquestração multi-agentes |

---

## 4. Modernização da API

### 4.1 Padrões de API Obsoletos (Migração Concluída)

Todos os exemplos em Python e TypeScript de **chat** foram migrados da API Chat Completions para a **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Padrão Antigo | Novo Padrão | Estado |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Concluído |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Concluído |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | pacote `openai` `client.responses.create()` → `response.output_text` | Concluído |
| `df.append()` (pandas) | `pd.concat()` | Concluído |

> **Nota:** Os exemplos dos modelos Microsoft Foundry que usam o SDK `azure-ai-inference` / `@azure-rest/ai-inference` (`client.complete()`) permanecem na API Model Inference, que não suporta a Responses API. `AzureOpenAI()` é mantido intencionalmente onde ainda é válido (embeddings e geração de imagem).

### 4.2 Novas Funcionalidades de API a Demonstrar

1. **Saídas Estruturadas** (OpenAI)
   - Modo JSON
   - Chamada de funções com esquemas estritos

2. **Capacidades de Visão**
   - Análise de imagens com GPT-4o (visão)
   - Prompts multimodais

3. **Ferramentas Integradas da Responses API** (substitui a antiga Assistants API)
   - Interpretador de código
   - Pesquisa em ficheiros
   - Pesquisa web e ferramentas personalizadas

---

## 5. Melhorias na Infraestrutura

### 5.1 Melhorias CI/CD

Implementadas em [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): linting/formatção Python (Ruff + Black) é **aplicado obrigatoriamente** no módulo de utilitários `shared/` mantido e é executado em modo **consultivo** no restante do currículo, além de uma passagem ESLint consultiva para JavaScript/TypeScript. A linha base ilustrativa foi:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Análise de Segurança

Implementada em [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): análise CodeQL para Python e JavaScript/TypeScript (ao fazer push, pull request e semanalmente) além de revisão de dependências em pull requests. A linha base ilustrativa foi:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Melhorias na Experiência do Desenvolvedor

### 6.1 Melhorias no DevContainer

Implementado em [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) e [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): o container agora inclui as extensões Pylance, o formatador Black, Ruff, ESLint, Prettier e Copilot, ativa a formatação ao guardar ligada à configuração Black/Prettier do repositório e instala as ferramentas de desenvolvimento (`ruff`, `black`, `mypy`, `pytest`) para que o workflow de [code-quality](../../../.github/workflows/code-quality.yml) possa ser reproduzido localmente. A imagem base `mcr.microsoft.com/devcontainers/universal` já inclui Python e Node, pelo que não são necessárias funcionalidades adicionais. A linha base ilustrativa foi:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Playground Interativo

Considerar adicionar:
- Notebooks Jupyter com chaves API pré-preenchidas (via ambiente)
- Demos Gradio/Streamlit para aprendizes visuais
- Questionários interativos para avaliação de conhecimento

---

## 7. Suporte Multilíngue

### 7.1 Cobertura Atual de Linguagens

| Tecnologia | Aulas Cobertas | Estado |
|------------|-----------------|--------|
| Python | Todas | Completo |
| TypeScript | 06-09, 11 | Parcial |
| JavaScript | 06-08, 11 | Parcial |
| .NET/C# | Algumas | Parcial |

### 7.2 Adições Recomendadas

1. **Go** - Em crescimento para ferramentas IA/ML
2. **Rust** - Aplicações com criticidade de performance
3. **Java/Kotlin** - Aplicações empresariais

---

## 8. Otimizações de Performance

### 8.1 Otimizações ao Nível do Código

1. **Padrões Async/Await**
   - Adicionar exemplos async para processamento em lote
   - Demonstrar chamadas concorrentes à API

2. **Estratégias de Cache**
   - Adicionar exemplos de cache de embeddings
   - Demonstrar padrões de cache de respostas

3. **Otimização de Tokens**
   - Adicionar exemplos de uso do tiktoken
   - Demonstrar técnicas de compressão de prompts

### 8.2 Exemplos de Otimização de Custos

Adicionar exemplos a demonstrar:
- Seleção de modelo com base na complexidade da tarefa
- Engenharia de prompt para eficiência de tokens
- Processamento em lote para operações em massa

---

## 9. Acessibilidade e Internacionalização

### 9.1 Estado Atual da Tradução

Todas as traduções estão **completas** e geradas automaticamente pelo [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), que produz e mantém mais de 50 versões linguísticas do currículo sincronizadas com a fonte em inglês. O conteúdo traduzido encontra-se em `translations/` e as imagens localizadas em `translated_images/`; a lista completa das línguas disponíveis é publicada no topo do README do repositório.

| Aspeto | Estado |
|--------|--------|
| Cobertura da tradução | Completa — 50+ línguas, todas as aulas |
| Método de tradução | Automatizado via [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Mantido sincronizado com a fonte em inglês | Sim — regenerado automaticamente |

### 9.2 Melhorias de Acessibilidade

1. Adicionar texto alt a todas as imagens
2. Garantir realce de sintaxe adequado nos exemplos de código
3. Adicionar transcrições de vídeo para todo o conteúdo vídeo
4. Garantir contraste de cor conforme as diretrizes WCAG

---

## 10. Prioridade de Implementação

### Fase 1: Imediata (Semana 1-2)
- [x] Corrigir problemas críticos de segurança
- [x] Adicionar configuração de qualidade de código
- [x] Criar utilitários partilhados
- [x] Documentar diretrizes de segurança

### Fase 2: Curto prazo (Semana 3-4)
- [x] Atualizar padrões de API obsoletos (Chat Completions → Responses API, Python + TypeScript)
- [ ] Adicionar anotações de tipo a todos os ficheiros Python (feito para o módulo mantido `shared/`; exemplos das aulas mantidos simples)
- [x] Adicionar workflows CI/CD para qualidade de código
- [x] Criar workflow de análise de segurança

### Fase 3: Médio prazo (Mês 2-3)
- [ ] Adicionar nova aula de segurança
- [ ] Adicionar aula de desdobramento em produção
- [x] Melhorar configuração do DevContainer
- [ ] Adicionar demos interativos

### Fase 4: Longo prazo (Mês 4+)
- [ ] Adicionar aula avançada de RAG
- [ ] Expandir cobertura linguística
- [ ] Adicionar suíte completa de testes
- [ ] Criar programa de certificação

---

## Conclusão

Este roteiro providencia uma abordagem estruturada para melhorar o currículo IA Generativa para Iniciantes. Ao abordar questões de segurança, modernizar APIs e adicionar conteúdo educativo, o curso irá preparar melhor os estudantes para o desenvolvimento de aplicações de IA no mundo real.

Para perguntas ou contribuições, por favor abra um issue no repositório GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->