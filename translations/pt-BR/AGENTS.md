# AGENTS.md

## Visão Geral do Projeto

Este repositório contém um currículo abrangente de 21 aulas ensinando fundamentos de IA Generativa e desenvolvimento de aplicações. O curso é projetado para iniciantes e cobre desde conceitos básicos até a construção de aplicações prontas para produção.

**Principais Tecnologias:**
- Python 3.9+ com bibliotecas: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript com Node.js e bibliotecas: `openai` (Azure OpenAI via o endpoint v1 + API Responses), `@azure-rest/ai-inference` (Modelos Microsoft Foundry)
- Azure OpenAI Service, OpenAI API e Microsoft Foundry Models (GitHub Models encerrando em julho de 2026)
- Jupyter Notebooks para aprendizado interativo
- Dev Containers para ambiente de desenvolvimento consistente

**Estrutura do Repositório:**
- 21 diretórios numerados de aulas (00-21) contendo READMEs, exemplos de código e tarefas
- Múltiplas implementações: exemplos em Python, TypeScript e às vezes .NET
- Diretório de traduções com versões em mais de 40 idiomas
- Configuração centralizada via arquivo `.env` (use `.env.copy` como modelo)

## Comandos de Configuração

### Configuração Inicial do Repositório

```bash
# Clone o repositório
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copie o template do ambiente
cp .env.copy .env
# Edite o .env com suas chaves API e endpoints
```

### Configuração do Ambiente Python

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# No macOS/Linux:
source venv/bin/activate
# No Windows:
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### Configuração Node.js/TypeScript

```bash
# Instale as dependências no nível root (para ferramentas de documentação)
npm install

# Para exemplos de TypeScript de lições individuais, navegue até a lição específica:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configuração do Dev Container (Recomendado)

O repositório inclui uma configuração `.devcontainer` para GitHub Codespaces ou VS Code Dev Containers:

1. Abra o repositório no GitHub Codespaces ou no VS Code com a extensão Dev Containers
2. O Dev Container automaticamente:
   - Instala dependências Python do `requirements.txt`
   - Executa o script pós-criação (`.devcontainer/post-create.sh`)
   - Configura o kernel do Jupyter

## Fluxo de Desenvolvimento

### Variáveis de Ambiente

Todas as aulas que requerem acesso à API usam variáveis de ambiente definidas no `.env`:

- `OPENAI_API_KEY` - Para OpenAI API
- `AZURE_OPENAI_API_KEY` - Para Azure OpenAI no Microsoft Foundry (Azure OpenAI Service agora faz parte do Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL do endpoint Azure OpenAI (endpoint do recurso Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nome do deployment do modelo de chat completion (padrão do curso: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nome do deployment do modelo de embeddings (padrão do curso: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Versão da API (padrão: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Para modelos Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint dos Microsoft Foundry Models (catálogo de modelos multi-provedor)
- `AZURE_INFERENCE_CREDENTIAL` - Chave API Microsoft Foundry Models (substitui o `GITHUB_TOKEN` que será descontinuado)
- `AZURE_INFERENCE_CHAT_MODEL` - Modelo sem capacidades de raciocínio (ex: `Llama-3.3-70B-Instruct`) usado nos exemplos de `temperature`, pois modelos de raciocínio não suportam controle de amostragem

### Convenções de Modelos (importante)

- **Modelo de chat padrão é `gpt-5-mini`** - um modelo atual e não depreciado de **raciocínio**. A partir de 2026, os modelos antigos "mini" que suportam temperatura (`gpt-4o-mini`, `gpt-4.1-mini`) estão *depreciando*, então o currículo padroniza na família GPT-5.
- **Modelos de raciocínio rejeitam `temperature` e `top_p`**, e usam `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) ao invés de `max_tokens`. Não adicione `temperature`/`top_p`/`max_tokens` em exemplos que chamem o `gpt-5-mini`.
- **Para demonstrar `temperature`**, os exemplos usam um modelo **Llama** (`Llama-3.3-70B-Instruct`) via o endpoint Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). Controle modelos de raciocínio com engenharia de prompt + controles de raciocínio em vez de botões de amostragem.
- **Fine-tuning (aula 18)** mantém o `gpt-4.1-mini`: GPT-5 só suporta fine-tuning por reforço (RFT), não o fine-tuning supervisionado (SFT) mostrado nessa aula.
- As aulas 20 (Mistral) e 21 (Meta) mantêm o uso de `temperature`/`max_tokens` pois são focadas em modelos Mistral/Llama que os suportam.

### Executando Exemplos em Python

```bash
# Navegue até o diretório da lição
cd 06-text-generation-apps/python

# Execute um script Python
python aoai-app.py
```

### Executando Exemplos em TypeScript

```bash
# Navegue até o diretório do aplicativo TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Compile o código TypeScript
npm run build

# Execute o aplicativo
npm start
```

### Executando Jupyter Notebooks

```bash
# Inicie o Jupyter na raiz do repositório
jupyter notebook

# Ou use o VS Code com a extensão Jupyter
```

### Trabalhando com Diferentes Tipos de Aula

- Aulas **"Aprender"**: Foco na documentação README.md e conceitos
- Aulas **"Construir"**: Incluem exemplos funcionais em Python e TypeScript
- Cada aula possui README.md com teoria, explicações de código e links para conteúdo em vídeo

## Diretrizes de Estilo de Código

### Python

- Use `python-dotenv` para gerenciamento de variáveis de ambiente
- Importe a biblioteca `openai` para interações com a API
- Use `pylint` para linting (alguns exemplos incluem `# pylint: disable=all` para simplicidade)
- Siga as convenções de nomenclatura PEP 8
- Guarde credenciais da API no arquivo `.env`, nunca no código

### TypeScript

- Use o pacote `dotenv` para variáveis de ambiente
- Configuração TypeScript em `tsconfig.json` para cada app
- Use o pacote `openai` para Azure OpenAI (apontar cliente para endpoint `/openai/v1/` e chamar `client.responses.create`); use `@azure-rest/ai-inference` para Microsoft Foundry Models
- Use `nodemon` para desenvolvimento com recarregamento automático
- Compile antes de rodar: `npm run build` e logo após `npm start`

### Convenções Gerais

- Mantenha exemplos simples e educacionais
- Inclua comentários explicando conceitos-chave
- Código de cada aula deve ser autocontido e executável
- Use nomenclatura consistente: prefixo `aoai-` para Azure OpenAI, `oai-` para OpenAI API, `githubmodels-` para Microsoft Foundry Models (prefixo legado do tempo GitHub Models)

## Diretrizes de Documentação

### Estilo Markdown

- Todas as URLs devem estar no formato `[texto](../../url)` sem espaços extras
- Links relativos devem começar com `./` ou `../`
- Todos os links para domínios Microsoft devem incluir o ID de rastreamento: `?WT.mc_id=academic-105485-koreyst`
- Não use locais específicos de países nas URLs (evite `/en-us/`)
- Imagens armazenadas na pasta `./images` com nomes descritivos
- Use caracteres ingleses, números e traços nos nomes dos arquivos

### Suporte a Tradução

- Repositório suporta mais de 40 idiomas via GitHub Actions automatizadas
- Traduções armazenadas no diretório `translations/`
- Não envie traduções parciais
- Traduções automáticas por máquina não são aceitas
- Imagens traduzidas armazenadas no diretório `translated_images/`

## Testes e Validação

### Verificações antes do envio

Este repositório usa GitHub Actions para validação. Antes de enviar Pull Requests:

1. **Verifique links em Markdown**:
   ```bash
   # O fluxo de trabalho validate-markdown.yml verifica:
   # - Caminhos relativos quebrados
   # - IDs de rastreamento ausentes nos caminhos
   # - IDs de rastreamento ausentes nas URLs
   # - URLs com localidade do país
   # - URLs externas quebradas
   ```

2. **Testes manuais**:
   - Teste exemplos Python: Ative venv e execute scripts
   - Teste exemplos TypeScript: `npm install`, `npm run build`, `npm start`
   - Verifique se variáveis de ambiente estão configuradas corretamente
   - Confirme que chaves API funcionam com os exemplos de código

3. **Exemplos de Código**:
   - Assegure que todo código rode sem erros
   - Teste com Azure OpenAI e OpenAI API quando aplicável
   - Verifique se os exemplos funcionam com Microsoft Foundry Models onde suportado

### Sem Testes Automatizados

Este é um repositório educacional focado em tutoriais e exemplos. Não existem testes unitários ou de integração para rodar. A validação é principalmente:
- Testes manuais dos exemplos de código
- GitHub Actions para validação de Markdown
- Revisão comunitária do conteúdo educacional

## Diretrizes para Pull Requests

### Antes de Enviar

1. Teste mudanças de código em Python e TypeScript quando aplicável
2. Rode validação Markdown (disparado automaticamente no PR)
3. Garanta que IDs de rastreamento estão presentes em todas URLs Microsoft
4. Verifique se links relativos são válidos
5. Confirme que imagens estão corretamente referenciadas

### Formato do Título do PR

- Use títulos descritivos: `[Lesson 06] Corrige erro de digitação no exemplo Python` ou `Atualiza README para aula 08`
- Referencie números de issues quando aplicável: `Corrige #123`

### Descrição do PR

- Explique o que foi alterado e por quê
- Link para issues relacionadas
- Para mudanças de código, especifique quais exemplos foram testados
- Para PRs de tradução, inclua todos os arquivos para tradução completa

### Requisitos para Contribuição

- Assine o Microsoft CLA (automático no primeiro PR)
- Faça fork do repositório para sua conta antes de modificar
- Um PR por mudança lógica (não combine correções não relacionadas)
- Mantenha PRs focados e pequenos quando possível

## Fluxos Comuns de Trabalho

### Adicionando um Novo Exemplo de Código

1. Navegue até o diretório da aula apropriada
2. Crie o exemplo na subpasta `python/` ou `typescript/`
3. Siga a convenção de nomes: `{provider}-{nome-exemplo}.{py|ts|js}`
4. Teste com credenciais reais da API
5. Documente novas variáveis de ambiente no README da aula

### Atualizando Documentação

1. Edite README.md no diretório da aula
2. Siga diretrizes Markdown (IDs de rastreamento, links relativos)
3. Atualizações em traduções são feitas por GitHub Actions (não edite manualmente)
4. Teste se todos os links são válidos

### Trabalhando com Dev Containers

1. Repositório inclui `.devcontainer/devcontainer.json`
2. Script pós-criação instala dependências Python automaticamente
3. Extensões para Python e Jupyter pré-configuradas
4. Ambiente baseado em `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Implantação e Publicação

Este é um repositório de aprendizado - não existe processo de implantação. O currículo é consumido por:

1. **Repositório GitHub**: Acesso direto ao código e documentação
2. **GitHub Codespaces**: Ambiente de desenvolvimento instantâneo com configuração prévia
3. **Microsoft Learn**: Conteúdo pode ser distribuído para plataforma oficial de aprendizado
4. **docsify**: Site de documentação gerado a partir de Markdown (veja `docsifytopdf.js` e `package.json`)

### Construindo Site de Documentação

```bash
# Gerar PDF da documentação (se necessário)
npm run convert
```

## Solução de Problemas

### Problemas Comuns

**Erros de Importação em Python**:
- Certifique-se que o ambiente virtual está ativado
- Rode `pip install -r requirements.txt`
- Verifique se a versão do Python é 3.9+

**Erros de Build em TypeScript**:
- Rode `npm install` no diretório da app específica
- Verifique se a versão do Node.js é compatível
- Limpe `node_modules` e reinstale se necessário

**Erros de Autenticação da API**:
- Verifique se o arquivo `.env` existe e possui valores corretos
- Cheque se as chaves API são válidas e não expiradas
- Certifique-se que URLs dos endpoints estão corretos para sua região

**Variáveis de Ambiente Faltando**:
- Copie `.env.copy` para `.env`
- Preencha todos os valores requeridos para a aula em que você está trabalhando
- Reinicie sua aplicação após atualizar `.env`

## Recursos Adicionais

- [Guia de Configuração do Curso](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Diretrizes de Contribuição](./CONTRIBUTING.md)
- [Código de Conduta](./CODE_OF_CONDUCT.md)
- [Política de Segurança](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Coleção de Exemplos Avançados de Código](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notas Específicas do Projeto

- Este é um **repositório educacional** focado em aprendizado, não código de produção
- Exemplos são intencionalmente simples e focados em ensino de conceitos
- Qualidade de código é equilibrada com clareza educacional
- Cada aula é autocontida e pode ser concluída de forma independente
- O repositório suporta múltiplos provedores de API: Azure OpenAI, OpenAI, Microsoft Foundry Models e provedores offline como Foundry Local e Ollama
- Conteúdo é multilíngue com fluxos automáticos de tradução
- Comunidade ativa no Discord para perguntas e suporte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->