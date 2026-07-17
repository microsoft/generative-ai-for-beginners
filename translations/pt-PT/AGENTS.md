# AGENTS.md

## Visão Geral do Projeto

Este repositório contém um currículo abrangente de 21 lições que ensina os fundamentos da IA Generativa e desenvolvimento de aplicações. O curso é dirigido a iniciantes e cobre desde conceitos básicos até a construção de aplicações prontas para produção.

**Tecnologias principais:**
- Python 3.9+ com bibliotecas: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript com Node.js e bibliotecas: `openai` (Azure OpenAI via endpoint v1 + API de respostas), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Serviço Azure OpenAI, API OpenAI e Microsoft Foundry Models (GitHub Models será descontinuado no final de julho de 2026)
- Jupyter Notebooks para aprendizagem interativa
- Contêineres de desenvolvimento para ambiente consistente

**Estrutura do Repositório:**
- 21 diretórios numerados de lições (00-21) contendo READMEs, exemplos de código e tarefas
- Múltiplas implementações: exemplos em Python, TypeScript e por vezes .NET
- Diretório de traduções com 40+ versões em diferentes idiomas
- Configuração centralizada via ficheiro `.env` (use `.env.copy` como modelo)

## Comandos de Configuração

### Configuração Inicial do Repositório

```bash
# Clonar o repositório
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copiar o modelo de ambiente
cp .env.copy .env
# Editar o .env com as suas chaves API e endpoints
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
# Instalar dependências ao nível da root (para ferramentas de documentação)
npm install

# Para exemplos individuais em TypeScript de cada lição, navegue até à lição específica:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configuração do Contêiner de Desenvolvimento (Recomendado)

O repositório inclui uma configuração `.devcontainer` para GitHub Codespaces ou VS Code Dev Containers:

1. Abra o repositório no GitHub Codespaces ou VS Code com a extensão Dev Containers
2. O Contêiner de Desenvolvimento irá automaticamente:
   - Instalar dependências Python do `requirements.txt`
   - Executar o script post-create (`.devcontainer/post-create.sh`)
   - Configurar o kernel Jupyter

## Fluxo de Trabalho de Desenvolvimento

### Variáveis de Ambiente

Todas as lições que necessitam de acesso à API usam variáveis de ambiente definidas em `.env`:

- `OPENAI_API_KEY` - Para API OpenAI
- `AZURE_OPENAI_API_KEY` - Para Azure OpenAI no Microsoft Foundry (Azure OpenAI Service faz agora parte do Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL do endpoint Azure OpenAI (endpoint do recurso Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nome do deployment do modelo de chat completion (default do curso: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nome do deployment do modelo embeddings (default do curso: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Versão da API (default: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Para modelos Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint Microsoft Foundry Models (catálogo de modelos multi-fornecedor)
- `AZURE_INFERENCE_CREDENTIAL` - Chave API Microsoft Foundry Models (substitui o `GITHUB_TOKEN` que será descontinuado)
- `AZURE_INFERENCE_CHAT_MODEL` - Modelo sem capacidades de raciocínio (ex.: `Llama-3.3-70B-Instruct`) usado nos exemplos de `temperature`, já que modelos de raciocínio não suportam controlos de sampling

### Convenções dos Modelos (importante)

- **Modelo de chat padrão é `gpt-5-mini`** - um modelo de **raciocínio** atual, não descontinuado. A partir de 2026, os modelos "mini" mais antigos com suporte a temperature (`gpt-4o-mini`, `gpt-4.1-mini`) estão a *ser descontinuados*, portanto o currículo padroniza a família GPT-5.
- **Modelos de raciocínio rejeitam `temperature` e `top_p`**, e usam `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) em vez de `max_tokens`. Não adicione `temperature`/`top_p`/`max_tokens` a exemplos que chamem `gpt-5-mini`.
- **Para demonstrar `temperature`**, os exemplos usam um modelo **Llama** (`Llama-3.3-70B-Instruct`) via endpoint Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). Controle os modelos de raciocínio com engenharia de prompt + controlos de raciocínio em vez de controlos de sampling.
- **Fine-tuning (lição 18)** mantém `gpt-4.1-mini`: GPT-5 suporta apenas fine-tuning por reforço (RFT), não o fine-tuning supervisionado (SFT) mostrado lá.
- Lições 20 (Mistral) e 21 (Meta) mantêm `temperature`/`max_tokens` pois miram modelos Mistral/Llama, que os suportam.

### Execução de Exemplos Python

```bash
# Navegar para o diretório da lição
cd 06-text-generation-apps/python

# Executar um script Python
python aoai-app.py
```

### Execução de Exemplos TypeScript

```bash
# Navegar para o diretório da aplicação TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Compilar o código TypeScript
npm run build

# Executar a aplicação
npm start
```

### Execução de Jupyter Notebooks

```bash
# Inicie o Jupyter na raiz do repositório
jupyter notebook

# Ou use o VS Code com a extensão Jupyter
```

### Trabalhar com Diferentes Tipos de Lição

- **Lições "Learn"**: Foco na documentação README.md e conceitos
- **Lições "Build"**: Incluem exemplos de código funcionais em Python e TypeScript
- Cada lição tem um README.md com teoria, walkthroughs de código e links para vídeos

## Diretrizes de Estilo de Código

### Python

- Use `python-dotenv` para gestão de variáveis de ambiente
- Importe a biblioteca `openai` para interações com API
- Use `pylint` para linting (alguns exemplos incluem `# pylint: disable=all` para simplicidade)
- Siga as convenções de nomeação PEP 8
- Guarde credenciais API em ficheiro `.env`, nunca no código

### TypeScript

- Use o pacote `dotenv` para variáveis de ambiente
- Configuração TypeScript em `tsconfig.json` para cada app
- Use `openai` para Azure OpenAI (aponte o cliente ao endpoint `/openai/v1/` e chame `client.responses.create`); use `@azure-rest/ai-inference` para Microsoft Foundry Models
- Use `nodemon` para desenvolvimento com reload automático
- Compile antes de correr: `npm run build` depois `npm start`

### Convenções Gerais

- Mantenha exemplos de código simples e educativos
- Inclua comentários explicando conceitos chave
- Cada código da lição deve ser autónomo e executável
- Use nomenclatura consistente: prefixo `aoai-` para Azure OpenAI, `oai-` para API OpenAI, `githubmodels-` para Microsoft Foundry Models (prefixo legado do GitHub Models)

## Diretrizes de Documentação

### Estilo Markdown

- Todas as URLs devem estar no formato `[text](../../url)` sem espaços extra
- Links relativos devem começar com `./` ou `../`
- Todos os links para domínios Microsoft devem incluir ID de rastreio: `?WT.mc_id=academic-105485-koreyst`
- Evite locais específicos de país nas URLs (evite `/en-us/`)
- Imagens armazenadas na pasta `./images` com nomes descritivos
- Use caracteres ingleses, números e hífens nos nomes dos ficheiros

### Suporte a Traduções

- Repositório suporta 40+ idiomas via GitHub Actions automatizados
- Traduções guardadas no diretório `translations/`
- Não submeta traduções parciais
- Traduções automáticas por máquina não são aceites
- Imagens traduzidas armazenadas no diretório `translated_images/`

## Testes e Validação

### Verificações Pré-submissão

Este repositório usa GitHub Actions para validação. Antes de submeter PRs:

1. **Verificar Links Markdown**:
   ```bash
   # O fluxo de trabalho validate-markdown.yml verifica:
   # - Caminhos relativos quebrados
   # - IDs de acompanhamento em falta nos caminhos
   # - IDs de acompanhamento em falta nas URLs
   # - URLs com locale de país
   # - URLs externas quebradas
   ```

2. **Testes Manuais**:
   - Testar exemplos Python: ativar venv e correr scripts
   - Testar exemplos TypeScript: `npm install`, `npm run build`, `npm start`
   - Verificar que variáveis de ambiente estão corretamente configuradas
   - Confirmar que chaves API funcionam com os exemplos de código

3. **Exemplos de Código**:
   - Garantir que todo o código corre sem erros
   - Testar com Azure OpenAI e API OpenAI quando aplicável
   - Verificar que exemplos funcionam com Microsoft Foundry Models onde suportado

### Sem Testes Automatizados

Este é um repositório educativo focado em tutoriais e exemplos. Não existem testes unitários ou de integração. A validação é principalmente:
- Testes manuais dos exemplos de código
- GitHub Actions para validação Markdown
- Revisão comunitária do conteúdo educativo

## Diretrizes para Pull Requests

### Antes de Submeter

1. Testar alterações de código tanto em Python quanto em TypeScript quando aplicável
2. Executar validação Markdown (disparada automaticamente no PR)
3. Assegurar que os IDs de rastreio estão presentes em todas URLs Microsoft
4. Verificar que os links relativos são válidos
5. Confirmar que imagens estão corretamente referenciadas

### Formato do Título do PR

- Usar títulos descritivos: `[Lesson 06] Fix Python example typo` ou `Update README for lesson 08`
- Referenciar números de issues quando aplicável: `Fixes #123`

### Descrição do PR

- Explicar o que foi alterado e porquê
- Linkar issues relacionadas
- Para alterações de código, especificar quais exemplos foram testados
- Para PRs de tradução, incluir todos ficheiros para tradução completa

### Requisitos de Contribuição

- Assinar o CLA Microsoft (automático no primeiro PR)
- Fazer fork do repositório para sua conta antes de fazer alterações
- Um PR por alteração lógica (não combinar correções não relacionadas)
- Manter PRs focados e pequenos quando possível

## Fluxos de Trabalho Comuns

### Adicionar Novo Exemplo de Código

1. Navegar para o diretório da lição apropriada
2. Criar exemplo na subpasta `python/` ou `typescript/`
3. Seguir convenção de nomeação: `{provider}-{example-name}.{py|ts|js}`
4. Testar com credenciais reais de API
5. Documentar quaisquer novas variáveis de ambiente no README da lição

### Atualizar Documentação

1. Editar README.md no diretório da lição
2. Seguir diretrizes Markdown (IDs de rastreio, links relativos)
3. Atualização das traduções é feita via GitHub Actions (não editar manualmente)
4. Testar se todos os links são válidos

### Trabalhar com Dev Containers

1. Repositório inclui `.devcontainer/devcontainer.json`
2. Script post-create instala automaticamente dependências Python
3. Extensões para Python e Jupyter estão pré-configuradas
4. Ambiente baseado em `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deploy e Publicação

Este é um repositório de aprendizagem - não há processo de deploy. O currículo é consumido por:

1. **Repositório GitHub**: acesso direto ao código e documentação
2. **GitHub Codespaces**: ambiente dev instantâneo com configuração prévia
3. **Microsoft Learn**: conteúdo pode ser sindicado para plataforma oficial de aprendizagem
4. **docsify**: site de documentação gerado a partir de Markdown (ver `docsifytopdf.js` e `package.json`)

### Construir Site de Documentação

```bash
# Gerar PDF a partir da documentação (se necessário)
npm run convert
```

## Resolução de Problemas

### Problemas Comuns

**Erros de Importação Python**:
- Assegurar que o ambiente virtual está ativado
- Executar `pip install -r requirements.txt`
- Verificar que a versão do Python é 3.9+

**Erros de Build TypeScript**:
- Executar `npm install` no diretório específico da app
- Verificar que a versão do Node.js é compatível
- Limpar `node_modules` e reinstalar se necessário

**Erros de Autenticação API**:
- Verificar que o ficheiro `.env` existe e tem valores corretos
- Confirmar que chaves API são válidas e não expiraram
- Assegurar que URLs dos endpoints estão corretas para a sua região

**Variáveis de Ambiente em Falta**:
- Copiar `.env.copy` para `.env`
- Preencher todos os valores requeridos para a lição que está a trabalhar
- Reiniciar aplicação após atualizar `.env`

## Recursos Adicionais

- [Guia de Configuração do Curso](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Diretrizes para Contribuição](./CONTRIBUTING.md)
- [Código de Conduta](./CODE_OF_CONDUCT.md)
- [Política de Segurança](./SECURITY.md)
- [Discord Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Coleção de Exemplos de Código Avançados](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notas Específicas do Projeto

- Este é um **repositório educativo** focado em aprendizagem, não código de produção
- Exemplos são intencionalmente simples e focados no ensino de conceitos
- Qualidade do código é equilibrada com clareza educativa
- Cada lição é autónoma e pode ser completada independentemente
- O repositório suporta múltiplos provedores de API: Azure OpenAI, OpenAI, Microsoft Foundry Models, e provedores offline como Foundry Local e Ollama
- Conteúdo é multilíngue com fluxos de trabalho de tradução automatizada
- Comunidade ativa no Discord para questões e apoio

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->