<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:59:50+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pt"
}
-->
# AGENTS.md

## Visão Geral do Projeto

Este repositório contém um currículo abrangente de 21 lições que ensina os fundamentos de IA Generativa e desenvolvimento de aplicações. O curso foi projetado para iniciantes e cobre desde conceitos básicos até a criação de aplicações prontas para produção.

**Principais Tecnologias:**
- Python 3.9+ com bibliotecas: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript com Node.js e bibliotecas: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API e Modelos do GitHub
- Jupyter Notebooks para aprendizagem interativa
- Dev Containers para um ambiente de desenvolvimento consistente

**Estrutura do Repositório:**
- 21 diretórios numerados de lições (00-21) contendo READMEs, exemplos de código e tarefas
- Múltiplas implementações: exemplos em Python, TypeScript e, ocasionalmente, .NET
- Diretório de traduções com versões em mais de 40 idiomas
- Configuração centralizada via ficheiro `.env` (use `.env.copy` como modelo)

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

### Configuração de Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configuração de Dev Container (Recomendado)

O repositório inclui uma configuração `.devcontainer` para GitHub Codespaces ou Dev Containers no VS Code:

1. Abra o repositório no GitHub Codespaces ou no VS Code com a extensão Dev Containers
2. O Dev Container configurará automaticamente:
   - Instalar dependências Python a partir de `requirements.txt`
   - Executar o script pós-criação (`.devcontainer/post-create.sh`)
   - Configurar o kernel do Jupyter

## Fluxo de Trabalho de Desenvolvimento

### Variáveis de Ambiente

Todas as lições que requerem acesso à API utilizam variáveis de ambiente definidas em `.env`:

- `OPENAI_API_KEY` - Para OpenAI API
- `AZURE_OPENAI_API_KEY` - Para Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL do endpoint Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Nome da implementação do modelo de conclusão de chat
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nome da implementação do modelo de embeddings
- `AZURE_OPENAI_API_VERSION` - Versão da API (padrão: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Para modelos Hugging Face
- `GITHUB_TOKEN` - Para Modelos do GitHub

### Executar Exemplos em Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Executar Exemplos em TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Executar Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Trabalhar com Diferentes Tipos de Lição

- **Lições "Learn"**: Focam na documentação README.md e conceitos
- **Lições "Build"**: Incluem exemplos de código funcionais em Python e TypeScript
- Cada lição tem um README.md com teoria, explicações de código e links para conteúdo em vídeo

## Diretrizes de Estilo de Código

### Python

- Utilize `python-dotenv` para gestão de variáveis de ambiente
- Importe a biblioteca `openai` para interações com a API
- Utilize `pylint` para linting (alguns exemplos incluem `# pylint: disable=all` para simplicidade)
- Siga as convenções de nomenclatura do PEP 8
- Armazene credenciais de API no ficheiro `.env`, nunca no código

### TypeScript

- Utilize o pacote `dotenv` para variáveis de ambiente
- Configuração TypeScript em `tsconfig.json` para cada aplicação
- Utilize `@azure/openai` ou `@azure-rest/ai-inference` para serviços Azure
- Utilize `nodemon` para desenvolvimento com recarregamento automático
- Compile antes de executar: `npm run build` e depois `npm start`

### Convenções Gerais

- Mantenha os exemplos de código simples e educativos
- Inclua comentários explicando conceitos-chave
- O código de cada lição deve ser autónomo e executável
- Utilize nomenclatura consistente: prefixo `aoai-` para Azure OpenAI, `oai-` para OpenAI API, `githubmodels-` para Modelos do GitHub

## Diretrizes de Documentação

### Estilo Markdown

- Todos os URLs devem estar no formato `[texto](../../url)` sem espaços extras
- Links relativos devem começar com `./` ou `../`
- Todos os links para domínios da Microsoft devem incluir ID de rastreamento: `?WT.mc_id=academic-105485-koreyst`
- Evite locais específicos de país nos URLs (não use `/en-us/`)
- Imagens armazenadas na pasta `./images` com nomes descritivos
- Utilize caracteres em inglês, números e hífens nos nomes dos ficheiros

### Suporte a Traduções

- O repositório suporta mais de 40 idiomas via GitHub Actions automatizadas
- Traduções armazenadas no diretório `translations/`
- Não envie traduções parciais
- Traduções automáticas não são aceites
- Imagens traduzidas armazenadas no diretório `translated_images/`

## Testes e Validação

### Verificações Antes da Submissão

Este repositório utiliza GitHub Actions para validação. Antes de submeter PRs:

1. **Verificar Links Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Testes Manuais**:
   - Testar exemplos em Python: Ativar venv e executar scripts
   - Testar exemplos em TypeScript: `npm install`, `npm run build`, `npm start`
   - Verificar se as variáveis de ambiente estão configuradas corretamente
   - Confirmar que as chaves de API funcionam com os exemplos de código

3. **Exemplos de Código**:
   - Garantir que todo o código executa sem erros
   - Testar com Azure OpenAI e OpenAI API quando aplicável
   - Verificar se os exemplos funcionam com Modelos do GitHub onde suportado

### Sem Testes Automatizados

Este é um repositório educacional focado em tutoriais e exemplos. Não há testes unitários ou de integração para executar. A validação é principalmente:
- Testes manuais dos exemplos de código
- GitHub Actions para validação de Markdown
- Revisão comunitária do conteúdo educacional

## Diretrizes para Pull Requests

### Antes de Submeter

1. Testar alterações de código em Python e TypeScript quando aplicável
2. Executar validação de Markdown (acionada automaticamente no PR)
3. Garantir que IDs de rastreamento estão presentes em todos os URLs da Microsoft
4. Verificar que links relativos são válidos
5. Confirmar que as imagens estão referenciadas corretamente

### Formato do Título do PR

- Utilize títulos descritivos: `[Lição 06] Corrigir erro de exemplo em Python` ou `Atualizar README para a lição 08`
- Referencie números de problemas quando aplicável: `Fixes #123`

### Descrição do PR

- Explique o que foi alterado e por quê
- Link para problemas relacionados
- Para alterações de código, especifique quais exemplos foram testados
- Para PRs de tradução, inclua todos os ficheiros para uma tradução completa

### Requisitos de Contribuição

- Assinar o Microsoft CLA (automático no primeiro PR)
- Fazer fork do repositório na sua conta antes de realizar alterações
- Um PR por alteração lógica (não combine correções não relacionadas)
- Mantenha os PRs focados e pequenos quando possível

## Fluxos de Trabalho Comuns

### Adicionar um Novo Exemplo de Código

1. Navegue até o diretório da lição apropriada
2. Crie o exemplo no subdiretório `python/` ou `typescript/`
3. Siga a convenção de nomenclatura: `{provider}-{example-name}.{py|ts|js}`
4. Teste com credenciais reais de API
5. Documente quaisquer novas variáveis de ambiente no README da lição

### Atualizar Documentação

1. Edite o README.md no diretório da lição
2. Siga as diretrizes de Markdown (IDs de rastreamento, links relativos)
3. Atualizações de traduções são tratadas por GitHub Actions (não edite manualmente)
4. Teste todos os links para garantir que são válidos

### Trabalhar com Dev Containers

1. O repositório inclui `.devcontainer/devcontainer.json`
2. O script pós-criação instala automaticamente dependências Python
3. Extensões para Python e Jupyter estão pré-configuradas
4. O ambiente é baseado em `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Implantação e Publicação

Este é um repositório de aprendizagem - não há processo de implantação. O currículo é consumido por:

1. **Repositório GitHub**: Acesso direto ao código e documentação
2. **GitHub Codespaces**: Ambiente de desenvolvimento instantâneo com configuração pré-definida
3. **Microsoft Learn**: O conteúdo pode ser sindicado para a plataforma oficial de aprendizagem
4. **docsify**: Site de documentação construído a partir de Markdown (veja `docsifytopdf.js` e `package.json`)

### Construir o Site de Documentação

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Resolução de Problemas

### Problemas Comuns

**Erros de Importação em Python**:
- Certifique-se de que o ambiente virtual está ativado
- Execute `pip install -r requirements.txt`
- Verifique se a versão do Python é 3.9+

**Erros de Compilação em TypeScript**:
- Execute `npm install` no diretório específico da aplicação
- Verifique se a versão do Node.js é compatível
- Limpe `node_modules` e reinstale, se necessário

**Erros de Autenticação na API**:
- Verifique se o ficheiro `.env` existe e tem valores corretos
- Confirme que as chaves de API são válidas e não expiraram
- Certifique-se de que os URLs dos endpoints estão corretos para sua região

**Variáveis de Ambiente Ausentes**:
- Copie `.env.copy` para `.env`
- Preencha todos os valores necessários para a lição em que está a trabalhar
- Reinicie sua aplicação após atualizar `.env`

## Recursos Adicionais

- [Guia de Configuração do Curso](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Diretrizes de Contribuição](./CONTRIBUTING.md)
- [Código de Conduta](./CODE_OF_CONDUCT.md)
- [Política de Segurança](./SECURITY.md)
- [Discord do Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Coleção de Exemplos de Código Avançados](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notas Específicas do Projeto

- Este é um **repositório educacional** focado em aprendizagem, não em código de produção
- Os exemplos são intencionalmente simples e focados em ensinar conceitos
- A qualidade do código é equilibrada com a clareza educacional
- Cada lição é autónoma e pode ser concluída independentemente
- O repositório suporta múltiplos fornecedores de API: Azure OpenAI, OpenAI e Modelos do GitHub
- O conteúdo é multilíngue com fluxos de trabalho de tradução automatizados
- Comunidade ativa no Discord para perguntas e suporte

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.