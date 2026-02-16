# Roteiro de Funcionalidades Avançadas e Melhorias

Este documento descreve as melhorias e avanços recomendados para o currículo Generative AI for Beginners, baseado numa revisão abrangente do código e análise das melhores práticas da indústria.

## Resumo Executivo

A base de código foi analisada em termos de segurança, qualidade do código e eficácia educativa. Este documento fornece recomendações para correções imediatas, melhorias a curto prazo e avanços futuros.

---

## 1. Melhorias de Segurança (Prioridade: Crítico)

### 1.1 Correções Imediatas (Concluídas)

| Problema | Ficheiros Afetados | Estado |
|----------|--------------------|--------|
| SECRET_KEY codificada | `05-advanced-prompts/python/aoai-solution.py` | Corrigido |
| Falta validação de ambiente | Vários ficheiros JS/TS | Corrigido |
| Chamadas de função inseguras | `11-integrating-with-function-calling/js-githubmodels/app.js` | Corrigido |
| Fugas de handles de ficheiro | `08-building-search-applications/scripts/` | Corrigido |
| Falta de timeouts em requests | `09-building-image-applications/python/` | Corrigido |

### 1.2 Funcionalidades de Segurança Adicionais Recomendadas

1. **Exemplos de Rate Limiting**
   - Adicionar código exemplo mostrando como implementar limitação de taxa para chamadas API
   - Demonstrar padrões de retrocesso exponencial

2. **Rotação de Chaves API**
   - Adicionar documentação sobre melhores práticas para rotação de chaves API
   - Incluir exemplos de uso do Azure Key Vault ou serviços similares

3. **Integração com Segurança de Conteúdo**
   - Adicionar exemplos utilizando Azure Content Safety API
   - Demonstrar padrões de moderação de entrada/saída

---

## 2. Melhorias na Qualidade do Código

### 2.1 Ficheiros de Configuração Adicionados

| Ficheiro | Propósito |
|----------|-----------|
| `.eslintrc.json` | Regras de linting para JavaScript/TypeScript |
| `.prettierrc` | Padrões de formatação de código |
| `pyproject.toml` | Configuração de ferramentas Python (Black, Ruff, mypy) |

### 2.2 Utilitários Partilhados Criados

Novo módulo `shared/python/` com:
- `env_utils.py` - Gestão de variáveis de ambiente
- `input_validation.py` - Validação e sanitização de input
- `api_utils.py` - Envoltorios seguros para pedidos API

### 2.3 Melhorias de Código Recomendadas

1. **Cobertura de Anotações de Tipo**
   - Adicionar anotações de tipo a todos os ficheiros Python
   - Ativar modo estrito no TypeScript em todos os projetos TS

2. **Padrões de Documentação**
   - Adicionar docstrings a todas as funções Python
   - Adicionar comentários JSDoc em todas as funções JavaScript/TypeScript

3. **Frameworks de Testes**
   - Adicionar configuração pytest e exemplos de testes
   - Adicionar configuração Jest para JavaScript/TypeScript

---

## 3. Melhorias Educativas

### 3.1 Novos Tópicos de Aula

1. **Segurança em Aplicações de IA** (Aula Proposta 22)
   - Ataques e defesas contra prompt injection
   - Gestão de chaves API
   - Moderação de conteúdo
   - Limitação de taxa e prevenção de abusos

2. **Deploy em Produção** (Aula Proposta 23)
   - Containerização com Docker
   - Pipelines CI/CD
   - Monitorização e logging
   - Gestão de custos

3. **Técnicas Avançadas de RAG** (Aula Proposta 24)
   - Pesquisa híbrida (palavra-chave + semântica)
   - Estratégias de re-ranqueamento
   - RAG multimodal
   - Métricas de avaliação

### 3.2 Melhorias em Aulas Existentes

| Aula | Melhoria Recomendada |
|-------|---------------------|
| 06 - Geração de Texto | Adicionar exemplos de resposta em streaming |
| 07 - Aplicações de Chat | Adicionar padrões de memória de conversação |
| 08 - Aplicações de Pesquisa | Adicionar comparação de bases de dados vetoriais |
| 09 - Geração de Imagem | Adicionar exemplos de edição/variação de imagem |
| 11 - Function Calling | Adicionar chamadas de função paralelas |
| 15 - RAG | Adicionar comparação de estratégias de chunking |
| 17 - Agentes IA | Adicionar orquestração multi-agente |

---

## 4. Modernização da API

### 4.1 Padrões API Obsoletos a Atualizar

| Padrão Antigo | Novo Padrão | Ficheiros Afetados |
|---------------|-------------|--------------------|
| `openai.api_type = "azure"` | Cliente `AzureOpenAI()` | Vários scripts em `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Vários notebooks |
| `df.append()` (pandas) | `pd.concat()` | Notebook RAG |

### 4.2 Novas Funcionalidades API a Demonstrar

1. **Saídas Estruturadas** (OpenAI)
   - Modo JSON
   - Function calling com esquemas restritivos

2. **Capacidades Visuais**
   - Análise de imagens com GPT-4V
   - Prompts multimodais

3. **API Assistentes**
   - Interpretador de código
   - Pesquisa em ficheiros
   - Ferramentas personalizadas

---

## 5. Melhorias de Infraestrutura

### 5.1 Melhorias CI/CD

Os workflows atuais validam markdown. Recomenda-se adicionar:

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

Atualize `.devcontainer/devcontainer.json`:

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

### 6.2 Ambiente Interativo

Considerar adicionar:
- Notebooks Jupyter com chaves API pré-configuradas (via ambiente)
- Demos Gradio/Streamlit para alunos visuais
- Questionários interativos para avaliação de conhecimentos

---

## 7. Suporte Multi-Linguagem

### 7.1 Cobertura Atual de Linguagens

| Tecnologia | Aulas Abrangidas | Estado |
|------------|------------------|--------|
| Python | Todas | Completo |
| TypeScript | 06-09, 11 | Parcial |
| JavaScript | 06-08, 11 | Parcial |
| .NET/C# | Algumas | Parcial |

### 7.2 Adições Recomendadas

1. **Go** - Em crescimento nas ferramentas IA/ML
2. **Rust** - Aplicações com requisitos críticos de performance
3. **Java/Kotlin** - Aplicações empresariais

---

## 8. Otimizações de Desempenho

### 8.1 Otimizações a Nível de Código

1. **Padrões Async/Await**
   - Adicionar exemplos async para processamento em lote
   - Demonstrar chamadas API concorrentes

2. **Estratégias de Cache**
   - Adicionar exemplos de cache de embeddings
   - Demonstrar padrões de cache de respostas

3. **Otimização de Tokens**
   - Adicionar exemplos de uso do tiktoken
   - Demonstrar técnicas de compressão de prompts

### 8.2 Exemplos de Otimização de Custos

Adicionar exemplos demonstrando:
- Seleção de modelo baseada na complexidade da tarefa
- Engenharia de prompts para eficiência de tokens
- Processamento em lote para operações em massa

---

## 9. Acessibilidade e Internacionalização

### 9.1 Estado Atual da Tradução

| Língua | Estado |
|--------|--------|
| Inglês | Completo |
| Chinês (Simplificado) | Completo |
| Japonês | Completo |
| Coreano | Completo |
| Espanhol | Parcial |
| Português | Parcial |
| Turco | Parcial |
| Polaco | Parcial |

### 9.2 Melhorias de Acessibilidade

1. Adicionar texto alt a todas as imagens
2. Garantir destaque de sintaxe adequado nos exemplos de código
3. Adicionar transcrições a todos os conteúdos em vídeo
4. Garantir contraste de cores conforme as diretrizes WCAG

---

## 10. Prioridade de Implementação

### Fase 1: Imediato (Semanas 1-2)
- [x] Corrigir problemas críticos de segurança
- [x] Adicionar configuração para qualidade de código
- [x] Criar utilitários compartilhados
- [x] Documentar linhas orientadoras de segurança

### Fase 2: Curto prazo (Semanas 3-4)
- [ ] Atualizar padrões API obsoletos
- [ ] Adicionar anotações de tipo a todos os ficheiros Python
- [ ] Adicionar workflows CI/CD para qualidade de código
- [ ] Criar workflow de análise de segurança

### Fase 3: Médio prazo (Mês 2-3)
- [ ] Adicionar nova aula de segurança
- [ ] Adicionar aula de deploy em produção
- [ ] Melhorar configuração do DevContainer
- [ ] Adicionar demos interativos

### Fase 4: Longo prazo (Mês 4+)
- [ ] Adicionar aula avançada de RAG
- [ ] Expandir cobertura linguística
- [ ] Adicionar suite abrangente de testes
- [ ] Criar programa de certificação

---

## Conclusão

Este roteiro fornece uma abordagem estruturada para melhorar o currículo Generative AI for Beginners. Ao abordar questões de segurança, modernizar APIs e adicionar conteúdos educativos, o curso preparará melhor os alunos para o desenvolvimento de aplicações reais de IA.

Para dúvidas ou contribuições, por favor crie uma issue no repositório GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->