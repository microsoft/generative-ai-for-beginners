<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:00:22+00:00",
  "source_file": "AGENTS.md",
  "language_code": "br"
}
-->
# AGENTS.md

## Visão Geral do Projeto

Este repositório contém um currículo abrangente de 21 lições que ensina os fundamentos de IA Generativa e desenvolvimento de aplicações. O curso foi projetado para iniciantes e cobre desde conceitos básicos até a construção de aplicações prontas para produção.

**Principais Tecnologias:**
- Python 3.9+ com bibliotecas: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript com Node.js e bibliotecas: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Serviço Azure OpenAI, API OpenAI e Modelos GitHub
- Jupyter Notebooks para aprendizado interativo
- Dev Containers para ambiente de desenvolvimento consistente

**Estrutura do Repositório:**
- 21 diretórios de lições numerados (00-21) contendo READMEs, exemplos de código e tarefas
- Múltiplas implementações: Python, TypeScript e, às vezes, exemplos em .NET
- Diretório de traduções com versões em mais de 40 idiomas
- Configuração centralizada via arquivo `.env` (use `.env.copy` como modelo)

## Comandos de Configuração

### Configuração Inicial do Repositório

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Configuração do Ambiente Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuração do Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configuração do Dev Container (Recomendado)

O repositório inclui uma configuração `.devcontainer` para GitHub Codespaces ou Dev Containers no VS Code:

1. Abra o repositório no GitHub Codespaces ou no VS Code com a extensão Dev Containers
2. O Dev Container configurará automaticamente:
   - Instalação de dependências Python a partir de `requirements.txt`
   - Execução do script pós-criação (`.devcontainer/post-create.sh`)
   - Configuração do kernel Jupyter

## Fluxo de Trabalho de Desenvolvimento

### Variáveis de Ambiente

Todas as lições que requerem acesso à API utilizam variáveis de ambiente definidas em `.env`:

- `OPENAI_API_KEY` - Para API OpenAI
- `AZURE_OPENAI_API_KEY` - Para Serviço Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL do endpoint Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Nome da implantação do modelo de conclusão de chat
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nome da implantação do modelo de embeddings
- `AZURE_OPENAI_API_VERSION` - Versão da API (padrão: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Para modelos Hugging Face
- `GITHUB_TOKEN` - Para Modelos GitHub

### Executando Exemplos em Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Executando Exemplos em TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Executando Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Trabalhando com Diferentes Tipos de Lição

- **Lições "Learn"**: Foco na documentação README.md e conceitos
- **Lições "Build"**: Incluem exemplos de código funcionais em Python e TypeScript
- Cada lição possui um README.md com teoria, explicações de código e links para conteúdo em vídeo

## Diretrizes de Estilo de Código

### Python

- Use `python-dotenv` para gerenciamento de variáveis de ambiente
- Importe a biblioteca `openai` para interações com a API
- Utilize `pylint` para linting (alguns exemplos incluem `# pylint: disable=all` para simplicidade)
- Siga as convenções de nomenclatura do PEP 8
- Armazene credenciais de API no arquivo `.env`, nunca no código

### TypeScript

- Use o pacote `dotenv` para variáveis de ambiente
- Configuração TypeScript em `tsconfig.json` para cada aplicativo
- Utilize `@azure/openai` ou `@azure-rest/ai-inference` para serviços Azure
- Use `nodemon` para desenvolvimento com recarregamento automático
- Compile antes de executar: `npm run build` e depois `npm start`

### Convenções Gerais

- Mantenha os exemplos de código simples e educativos
- Inclua comentários explicando conceitos-chave
- O código de cada lição deve ser autossuficiente e executável
- Use nomenclatura consistente: prefixo `aoai-` para Azure OpenAI, `oai-` para API OpenAI, `githubmodels-` para Modelos GitHub

## Diretrizes de Documentação

### Estilo de Markdown

- Todos os URLs devem estar no formato `[texto](../../url)` sem espaços extras
- Links relativos devem começar com `./` ou `../`
- Todos os links para domínios da Microsoft devem incluir ID de rastreamento: `?WT.mc_id=academic-105485-koreyst`
- Evite locais específicos de país nos URLs (não use `/en-us/`)
- Imagens armazenadas na pasta `./images` com nomes descritivos
- Use caracteres em inglês, números e hífens nos nomes dos arquivos

### Suporte a Traduções

- O repositório suporta mais de 40 idiomas via GitHub Actions automatizadas
- Traduções armazenadas no diretório `translations/`
- Não envie traduções parciais
- Traduções automáticas não são aceitas
- Imagens traduzidas armazenadas no diretório `translated_images/`

## Testes e Validação

### Verificações Pré-Envio

Este repositório utiliza GitHub Actions para validação. Antes de enviar PRs:

1. **Verificar Links em Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Testes Manuais**:
   - Teste exemplos em Python: Ative o venv e execute os scripts
   - Teste exemplos em TypeScript: `npm install`, `npm run build`, `npm start`
   - Verifique se as variáveis de ambiente estão configuradas corretamente
   - Certifique-se de que as chaves de API funcionam com os exemplos de código

3. **Exemplos de Código**:
   - Certifique-se de que todo o código seja executado sem erros
   - Teste com Azure OpenAI e API OpenAI quando aplicável
   - Verifique se os exemplos funcionam com Modelos GitHub onde suportado

### Sem Testes Automatizados

Este é um repositório educacional focado em tutoriais e exemplos. Não há testes unitários ou de integração para executar. A validação é principalmente:
- Testes manuais dos exemplos de código
- GitHub Actions para validação de Markdown
- Revisão comunitária do conteúdo educacional

## Diretrizes para Pull Requests

### Antes de Enviar

1. Teste alterações de código em Python e TypeScript quando aplicável
2. Execute a validação de Markdown (acionada automaticamente no PR)
3. Certifique-se de que os IDs de rastreamento estão presentes em todos os URLs da Microsoft
4. Verifique se os links relativos são válidos
5. Confirme que as imagens estão referenciadas corretamente

### Formato do Título do PR

- Use títulos descritivos: `[Lição 06] Corrigir erro de digitação no exemplo Python` ou `Atualizar README para a lição 08`
- Referencie números de problemas quando aplicável: `Fixes #123`

### Descrição do PR

- Explique o que foi alterado e por quê
- Link para problemas relacionados
- Para alterações de código, especifique quais exemplos foram testados
- Para PRs de tradução, inclua todos os arquivos para uma tradução completa

### Requisitos de Contribuição

- Assine o Microsoft CLA (automático no primeiro PR)
- Faça fork do repositório na sua conta antes de fazer alterações
- Um PR por alteração lógica (não combine correções não relacionadas)
- Mantenha os PRs focados e pequenos quando possível

## Fluxos de Trabalho Comuns

### Adicionando um Novo Exemplo de Código

1. Navegue até o diretório da lição apropriada
2. Crie o exemplo no subdiretório `python/` ou `typescript/`
3. Siga a convenção de nomenclatura: `{provider}-{example-name}.{py|ts|js}`
4. Teste com credenciais reais de API
5. Documente quaisquer novas variáveis de ambiente no README da lição

### Atualizando Documentação

1. Edite o README.md no diretório da lição
2. Siga as diretrizes de Markdown (IDs de rastreamento, links relativos)
3. Atualizações de traduções são tratadas por GitHub Actions (não edite manualmente)
4. Teste todos os links para garantir que são válidos

### Trabalhando com Dev Containers

1. O repositório inclui `.devcontainer/devcontainer.json`
2. O script pós-criação instala dependências Python automaticamente
3. Extensões para Python e Jupyter estão pré-configuradas
4. O ambiente é baseado em `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Implantação e Publicação

Este é um repositório de aprendizado - não há processo de implantação. O currículo é consumido por:

1. **Repositório GitHub**: Acesso direto ao código e documentação
2. **GitHub Codespaces**: Ambiente de desenvolvimento instantâneo com configuração pré-definida
3. **Microsoft Learn**: O conteúdo pode ser distribuído na plataforma oficial de aprendizado
4. **docsify**: Site de documentação construído a partir de Markdown (veja `docsifytopdf.js` e `package.json`)

### Construindo o Site de Documentação

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Solução de Problemas

### Problemas Comuns

**Erros de Importação no Python**:
- Certifique-se de que o ambiente virtual está ativado
- Execute `pip install -r requirements.txt`
- Verifique se a versão do Python é 3.9+

**Erros de Build no TypeScript**:
- Execute `npm install` no diretório específico do aplicativo
- Verifique se a versão do Node.js é compatível
- Limpe `node_modules` e reinstale, se necessário

**Erros de Autenticação na API**:
- Verifique se o arquivo `.env` existe e possui valores corretos
- Confirme se as chaves de API são válidas e não expiraram
- Certifique-se de que os URLs dos endpoints estão corretos para sua região

**Variáveis de Ambiente Ausentes**:
- Copie `.env.copy` para `.env`
- Preencha todos os valores necessários para a lição em que você está trabalhando
- Reinicie sua aplicação após atualizar `.env`

## Recursos Adicionais

- [Guia de Configuração do Curso](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Diretrizes de Contribuição](./CONTRIBUTING.md)
- [Código de Conduta](./CODE_OF_CONDUCT.md)
- [Política de Segurança](./SECURITY.md)
- [Discord do Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Coleção de Exemplos de Código Avançados](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notas Específicas do Projeto

- Este é um repositório **educacional** focado em aprendizado, não em código de produção
- Os exemplos são intencionalmente simples e focados em ensinar conceitos
- A qualidade do código é equilibrada com a clareza educacional
- Cada lição é autossuficiente e pode ser concluída de forma independente
- O repositório suporta múltiplos provedores de API: Azure OpenAI, OpenAI e Modelos GitHub
- O conteúdo é multilíngue com fluxos de trabalho de tradução automatizados
- Comunidade ativa no Discord para perguntas e suporte

---

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.