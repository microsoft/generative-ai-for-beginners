# AGENTS.md

## Visão Geral do Projeto

Este repositório contém um currículo abrangente de 21 aulas ensinando fundamentos de IA Generativa e desenvolvimento de aplicações. O curso é projetado para iniciantes e cobre tudo, desde conceitos básicos até a construção de aplicações prontas para produção.

**Tecnologias Principais:**
- Python 3.9+ com bibliotecas: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript com Node.js e bibliotecas: `openai` (Azure OpenAI via o endpoint v1 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, e Microsoft Foundry Models (GitHub Models será aposentado no final de julho de 2026)
- Jupyter Notebooks para aprendizado interativo
- Dev Containers para ambiente de desenvolvimento consistente

**Estrutura do Repositório:**
- 21 diretórios numerados de lições (00-21) contendo READMEs, exemplos de código e tarefas
- Múltiplas implementações: exemplos em Python, TypeScript e às vezes .NET
- Diretório de traduções com versões em mais de 40 idiomas
- Configuração centralizada via arquivo `.env` (use `.env.copy` como modelo)

## Comandos de Configuração

### Configuração Inicial do Repositório

```bash
# Clone o repositório
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copie o modelo de ambiente
cp .env.copy .env
# Edite o .env com suas chaves de API e endpoints
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
# Instale dependências no nível raiz (para ferramentas de documentação)
npm install

# Para exemplos individuais de TypeScript de lições, navegue até a lição específica:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configuração do Dev Container (Recomendado)

O repositório inclui uma configuração `.devcontainer` para GitHub Codespaces ou VS Code com Dev Containers:

1. Abra o repositório no GitHub Codespaces ou no VS Code com a extensão Dev Containers
2. O Dev Container automaticamente irá:
   - Instalar dependências Python do `requirements.txt`
   - Executar script pós-criação (`.devcontainer/post-create.sh`)
   - Configurar o kernel do Jupyter

## Fluxo de Trabalho de Desenvolvimento

### Variáveis de Ambiente

Todas as lições que requerem acesso à API usam variáveis de ambiente definidas em `.env`:

- `OPENAI_API_KEY` - Para OpenAI API
- `AZURE_OPENAI_API_KEY` - Para Azure OpenAI no Microsoft Foundry (Azure OpenAI Service agora faz parte do Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL do endpoint Azure OpenAI (endpoint do recurso Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nome do deployment do modelo para chat completions
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nome do deployment do modelo de embeddings
- `AZURE_OPENAI_API_VERSION` - Versão da API (padrão: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Para modelos Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint do Microsoft Foundry Models (catálogo multi-provedor)
- `AZURE_INFERENCE_CREDENTIAL` - Chave da API do Microsoft Foundry Models (substitui o `GITHUB_TOKEN` que será aposentado)

### Executando Exemplos em Python

```bash
# Navegar até o diretório da lição
cd 06-text-generation-apps/python

# Executar um script Python
python aoai-app.py
```

### Executando Exemplos em TypeScript

```bash
# Navegue até o diretório do aplicativo TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Compile o código TypeScript
npm run build

# Execute a aplicação
npm start
```

### Executando Jupyter Notebooks

```bash
# Inicie o Jupyter na raiz do repositório
jupyter notebook

# Ou use o VS Code com a extensão Jupyter
```

### Trabalhando com Diferentes Tipos de Lições

- **Lições "Learn"**: Foco na documentação README.md e nos conceitos
- **Lições "Build"**: Incluem exemplos de código funcionais em Python e TypeScript
- Cada lição tem um README.md com teoria, explicações de código e links para vídeos

## Diretrizes de Estilo de Código

### Python

- Use `python-dotenv` para gerenciamento das variáveis de ambiente
- Importe a biblioteca `openai` para interações com a API
- Use `pylint` para linting (alguns exemplos incluem `# pylint: disable=all` para simplicidade)
- Siga as convenções de nomenclatura PEP 8
- Armazene credenciais da API no arquivo `.env`, nunca no código

### TypeScript

- Use o pacote `dotenv` para variáveis de ambiente
- Configuração do TypeScript em `tsconfig.json` para cada aplicação
- Use o pacote `openai` para Azure OpenAI (aponte o cliente para o endpoint `/openai/v1/` e chame `client.responses.create`); use `@azure-rest/ai-inference` para Microsoft Foundry Models
- Use `nodemon` para desenvolvimento com recarregamento automático
- Compile antes de rodar: `npm run build` e depois `npm start`

### Convenções Gerais

- Mantenha os exemplos de código simples e educacionais
- Inclua comentários explicando conceitos-chave
- O código de cada lição deve ser autocontido e executável
- Use nomenclatura consistente: prefixo `aoai-` para Azure OpenAI, `oai-` para OpenAI API, `githubmodels-` para Microsoft Foundry Models (prefixo legado do período GitHub Models)

## Diretrizes para Documentação

### Estilo Markdown

- Todas as URLs devem estar no formato `[texto](../../url)` sem espaços extras
- Links relativos devem começar com `./` ou `../`
- Todos os links para domínios Microsoft devem incluir ID de rastreamento: `?WT.mc_id=academic-105485-koreyst`
- Não use locais específicos por país nas URLs (evite `/en-us/`)
- Imagens armazenadas na pasta `./images` com nomes descritivos
- Use caracteres em inglês, números e hifens nos nomes dos arquivos

### Suporte a Tradução

- O repositório suporta mais de 40 idiomas via GitHub Actions automatizados
- Traduções armazenadas no diretório `translations/`
- Não envie traduções parciais
- Traduções automáticas não são aceitas
- Imagens traduzidas armazenadas no diretório `translated_images/`

## Testes e Validação

### Verificações Pré-envio

Este repositório usa GitHub Actions para validação. Antes de enviar PRs:

1. **Verifique Links em Markdown**:
   ```bash
   # O fluxo de trabalho validate-markdown.yml verifica:
   # - Caminhos relativos quebrados
   # - IDs de rastreamento ausentes em caminhos
   # - IDs de rastreamento ausentes em URLs
   # - URLs com localidade de país
   # - URLs externas quebradas
   ```

2. **Testes Manuais**:
   - Teste exemplos em Python: Ative venv e execute os scripts
   - Teste exemplos em TypeScript: `npm install`, `npm run build`, `npm start`
   - Verifique se as variáveis de ambiente estão configuradas corretamente
   - Confira se as chaves da API funcionam com os exemplos de código

3. **Exemplos de Código**:
   - Garanta que todo código rode sem erros
   - Teste com Azure OpenAI e OpenAI API quando aplicável
   - Verifique exemplos com Microsoft Foundry Models onde suportado

### Sem Testes Automatizados

Este é um repositório educacional focado em tutoriais e exemplos. Não há testes unitários ou de integração para executar. A validação é primariamente:
- Testes manuais dos exemplos de código
- GitHub Actions para validação do Markdown
- Revisão comunitária do conteúdo educativo

## Diretrizes para Pull Requests

### Antes de Submeter

1. Teste as mudanças de código em Python e TypeScript quando aplicável
2. Execute a validação do Markdown (acionada automaticamente no PR)
3. Assegure que as IDs de rastreamento estejam presentes em todas URLs Microsoft
4. Verifique se links relativos são válidos
5. Confira se as imagens são referenciadas corretamente

### Formato do Título do PR

- Use títulos descritivos: `[Lição 06] Corrigir erro de digitação no exemplo Python` ou `Atualizar README da lição 08`
- Referencie números de issues quando aplicável: `Fixes #123`

### Descrição do PR

- Explique o que foi alterado e por quê
- Link para issues relacionadas
- Para mudanças de código, especifique quais exemplos foram testados
- Para PRs de tradução, inclua todos os arquivos para tradução completa

### Requisitos para Contribuição

- Assine o CLA da Microsoft (automático no primeiro PR)
- Faça fork do repositório para sua conta antes de modificar
- Um PR por mudança lógica (não combine correções não relacionadas)
- Mantenha PRs focados e pequenos quando possível

## Fluxos de Trabalho Comuns

### Adicionando um Novo Exemplo de Código

1. Navegue até o diretório da lição apropriada
2. Crie o exemplo no subdiretório `python/` ou `typescript/`
3. Siga a convenção de nomenclatura: `{provider}-{nome-do-exemplo}.{py|ts|js}`
4. Teste com credenciais reais da API
5. Documente quaisquer novas variáveis de ambiente no README da lição

### Atualizando Documentação

1. Edite o README.md no diretório da lição
2. Siga as diretrizes de Markdown (IDs de rastreamento, links relativos)
3. Atualizações de tradução são feitas pelo GitHub Actions (não edite manualmente)
4. Teste se todos os links são válidos

### Trabalhando com Dev Containers

1. O repositório inclui `.devcontainer/devcontainer.json`
2. Script pós-criação instala dependências Python automaticamente
3. Extensões para Python e Jupyter estão pré-configuradas
4. Ambiente é baseado em `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Implantação e Publicação

Este é um repositório de aprendizado - não há processo de implantação. O currículo é consumido por:

1. **Repositório GitHub**: Acesso direto a código e documentação
2. **GitHub Codespaces**: Ambiente de desenvolvimento instantâneo com configuração prévia
3. **Microsoft Learn**: Conteúdo pode ser disponibilizado na plataforma oficial de aprendizado
4. **docsify**: Site de documentação gerado a partir de Markdown (veja `docsifytopdf.js` e `package.json`)

### Construindo o Site de Documentação

```bash
# Gerar PDF da documentação (se necessário)
npm run convert
```

## Solução de Problemas

### Problemas Comuns

**Erros de Importação em Python**:
- Certifique-se que o ambiente virtual esteja ativado
- Execute `pip install -r requirements.txt`
- Verifique se a versão do Python é 3.9+

**Erros de Build em TypeScript**:
- Execute `npm install` no diretório da aplicação específica
- Verifique se a versão do Node.js é compatível
- Limpe `node_modules` e reinstale se necessário

**Erros de Autenticação da API**:
- Verifique se o arquivo `.env` existe e tem os valores corretos
- Confira se as chaves da API são válidas e não expiraram
- Confirme se as URLs dos endpoints estão corretas para sua região

**Variáveis de Ambiente Faltando**:
- Copie `.env.copy` para `.env`
- Preencha todos os valores necessários para a lição que está trabalhando
- Reinicie sua aplicação após atualizar `.env`

## Recursos Adicionais

- [Guia de Configuração do Curso](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Diretrizes de Contribuição](./CONTRIBUTING.md)
- [Código de Conduta](./CODE_OF_CONDUCT.md)
- [Política de Segurança](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Coleção de Exemplos Avançados de Código](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notas Específicas do Projeto

- Este é um **repositório educacional** focado em aprendizado, não em código para produção
- Exemplos são intencionalmente simples e focados no ensino de conceitos
- A qualidade do código é balanceada com clareza educacional
- Cada lição é autocontida e pode ser completada independentemente
- O repositório suporta múltiplos provedores de API: Azure OpenAI, OpenAI, Microsoft Foundry Models e provedores offline como Foundry Local e Ollama
- O conteúdo é multilíngue com workflows automatizados de tradução
- Comunidade ativa no Discord para dúvidas e suporte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->