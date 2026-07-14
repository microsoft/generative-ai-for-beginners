# AGENTS.md

## Visão Geral do Projeto

Este repositório contém um currículo abrangente de 21 lições ensinando os fundamentos da IA Generativa e desenvolvimento de aplicações. O curso é destinado a iniciantes e cobre desde conceitos básicos até a construção de aplicações prontas para produção.

**Tecnologias Principais:**
- Python 3.9+ com bibliotecas: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript com Node.js e bibliotecas: `openai` (Azure OpenAI via o endpoint v1 + API Responses), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, e Microsoft Foundry Models (GitHub Models será descontinuado no final de julho de 2026)
- Jupyter Notebooks para aprendizagem interativa
- Dev Containers para ambiente de desenvolvimento consistente

**Estrutura do Repositório:**
- 21 diretórios numerados de lições (00-21) contendo README, exemplos de código e tarefas
- Múltiplas implementações: exemplos em Python, TypeScript, e às vezes .NET
- Diretório de traduções com versões para mais de 40 idiomas
- Configuração centralizada via ficheiro `.env` (usar `.env.copy` como modelo)

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
# Instale as dependências ao nível root (para ferramentas de documentação)
npm install

# Para exemplos individuais de TypeScript das lições, navegue até à lição específica:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configuração do Dev Container (Recomendado)

O repositório inclui uma configuração `.devcontainer` para GitHub Codespaces ou VS Code Dev Containers:

1. Abra o repositório no GitHub Codespaces ou no VS Code com a extensão Dev Containers
2. O Dev Container irá automaticamente:
   - Instalar dependências Python do `requirements.txt`
   - Executar o script post-create (`.devcontainer/post-create.sh`)
   - Configurar o kernel do Jupyter

## Fluxo de Desenvolvimento

### Variáveis de Ambiente

Todas as lições que requerem acesso à API usam variáveis de ambiente definidas no `.env`:

- `OPENAI_API_KEY` - Para OpenAI API
- `AZURE_OPENAI_API_KEY` - Para Azure OpenAI no Microsoft Foundry (Azure OpenAI Service agora faz parte do Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL do endpoint Azure OpenAI (endpoint do recurso Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nome do deployment do modelo de conclusão de chat
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nome do deployment do modelo de embeddings
- `AZURE_OPENAI_API_VERSION` - Versão da API (padrão: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Para modelos Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint dos Microsoft Foundry Models (catálogo de modelos multi-fornecedor)
- `AZURE_INFERENCE_CREDENTIAL` - Chave API dos Microsoft Foundry Models (substitui o `GITHUB_TOKEN` que será descontinuado)

### Executar Exemplos Python

```bash
# Navegar para o diretório da lição
cd 06-text-generation-apps/python

# Executar um script Python
python aoai-app.py
```

### Executar Exemplos TypeScript

```bash
# Navegar para o diretório da aplicação TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Construir o código TypeScript
npm run build

# Executar a aplicação
npm start
```

### Executar Jupyter Notebooks

```bash
# Iniciar o Jupyter na raiz do repositório
jupyter notebook

# Ou usar o VS Code com a extensão Jupyter
```

### Trabalhar com Diferentes Tipos de Lições

- **Lições "Learn"**: Foco na documentação README.md e conceitos
- **Lições "Build"**: Incluem exemplos de código funcionais em Python e TypeScript
- Cada lição tem um README.md com teoria, explicações do código e links para conteúdos em vídeo

## Diretrizes de Estilo de Código

### Python

- Usar `python-dotenv` para gestão de variáveis de ambiente
- Importar a biblioteca `openai` para interações com a API
- Usar `pylint` para linting (alguns exemplos incluem `# pylint: disable=all` para simplificação)
- Seguir convenções de nomenclatura PEP 8
- Guardar credenciais API no ficheiro `.env`, nunca no código

### TypeScript

- Usar o pacote `dotenv` para variáveis de ambiente
- Configuração TypeScript em `tsconfig.json` para cada aplicação
- Usar o pacote `openai` para Azure OpenAI (apontar cliente ao endpoint `/openai/v1/` e usar `client.responses.create`); usar `@azure-rest/ai-inference` para Microsoft Foundry Models
- Usar `nodemon` para desenvolvimento com recarga automática
- Construir antes de executar: `npm run build` depois `npm start`

### Convenções Gerais

- Manter exemplos de código simples e educativos
- Incluir comentários explicativos dos conceitos chave
- O código de cada lição deve ser auto-contido e executável
- Usar nomenclaturas consistentes: prefixo `aoai-` para Azure OpenAI, `oai-` para OpenAI API, `githubmodels-` para Microsoft Foundry Models (prefixo legado do período GitHub Models)

## Diretrizes de Documentação

### Estilo Markdown

- Todos os URLs devem estar no formato `[texto](../../url)` sem espaços adicionais
- Links relativos devem iniciar com `./` ou `../`
- Todos os links para domínios Microsoft devem incluir ID de rastreamento: `?WT.mc_id=academic-105485-koreyst`
- Evitar localidades específicas por país em URLs (evitar `/en-us/`)
- Imagens armazenadas na pasta `./images` com nomes descritivos
- Usar caracteres ingleses, números e hífens em nomes dos ficheiros

### Suporte à Tradução

- O repositório suporta mais de 40 idiomas via GitHub Actions automatizadas
- Traduções armazenadas no diretório `translations/`
- Não submeter traduções parciais
- Traduções automáticas não são aceites
- Imagens traduzidas armazenadas no diretório `translated_images/`

## Testes e Validação

### Verificações Pré-Submissão

Este repositório usa GitHub Actions para validação. Antes de submeter PRs:

1. **Verificar Links Markdown**:
   ```bash
   # O fluxo de trabalho validate-markdown.yml verifica:
   # - Caminhos relativos quebrados
   # - IDs de rastreamento em falta nos caminhos
   # - IDs de rastreamento em falta nas URLs
   # - URLs com localização por país
   # - URLs externas quebradas
   ```

2. **Testes Manuais**:
   - Testar exemplos Python: ativar venv e executar scripts
   - Testar exemplos TypeScript: `npm install`, `npm run build`, `npm start`
   - Verificar que as variáveis de ambiente estão configuradas corretamente
   - Confirmar que as chaves API funcionam com os exemplos de código

3. **Exemplos de Código**:
   - Garantir que todo o código corre sem erros
   - Testar com Azure OpenAI e OpenAI API quando aplicável
   - Confirmar que os exemplos funcionam com Microsoft Foundry Models onde suportado

### Sem Testes Automatizados

Este é um repositório educativo focado em tutoriais e exemplos. Não há testes unitários ou de integração a executar. A validação é principalmente:
- Teste manual dos exemplos de código
- GitHub Actions para validação Markdown
- Revisão da comunidade para conteúdos educativos

## Diretrizes para Pull Requests

### Antes de Submeter

1. Testar alterações de código em Python e TypeScript quando aplicável
2. Executar validação Markdown (ativa automaticamente no PR)
3. Garantir que IDs de rastreamento estão presentes em todas URLs Microsoft
4. Verificar que links relativos são válidos
5. Confirmar referências corretas a imagens

### Formato do Título do PR

- Usar títulos descritivos: `[Lesson 06] Corrigir erro no exemplo Python` ou `Atualizar README da lição 08`
- Referenciar números de issues quando aplicável: `Resolve #123`

### Descrição do PR

- Explicar o que foi alterado e porquê
- Linkar para issues relacionadas
- Para mudanças de código, especificar quais exemplos foram testados
- Para PRs de tradução, incluir todos os ficheiros para uma tradução completa

### Requisitos de Contribuição

- Assinar o Microsoft CLA (automático no primeiro PR)
- Fazer fork do repositório para a sua conta antes de fazer alterações
- Um PR por alteração lógica (não combinar correções não relacionadas)
- Manter PRs focados e pequenos sempre que possível

## Fluxos de Trabalho Comuns

### Adicionar Um Novo Exemplo de Código

1. Navegar para o diretório da lição apropriada
2. Criar exemplo na subpasta `python/` ou `typescript/`
3. Seguir convenção de nomes: `{provider}-{nome-exemplo}.{py|ts|js}`
4. Testar com credenciais API reais
5. Documentar quaisquer novas variáveis de ambiente no README da lição

### Atualizar Documentação

1. Editar README.md no diretório da lição
2. Seguir diretrizes Markdown (IDs de rastreamento, links relativos)
3. Atualizações das traduções são geridas por GitHub Actions (não editar manualmente)
4. Testar que todos os links são válidos

### Trabalhar com Dev Containers

1. Repositório inclui `.devcontainer/devcontainer.json`
2. Script post-create instala dependências Python automaticamente
3. Extensões para Python e Jupyter vêm pré-configuradas
4. Ambiente baseia-se em `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment e Publicação

Este é um repositório educacional - não existe processo de deployment. O currículo é consumido por:

1. **Repositório GitHub**: Acesso direto ao código e documentação
2. **GitHub Codespaces**: Ambiente de desenvolvimento instantâneo com configuração prévia
3. **Microsoft Learn**: Conteúdo pode ser replicado na plataforma oficial de aprendizagem
4. **docsify**: Site de documentação construído a partir de Markdown (ver `docsifytopdf.js` e `package.json`)

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
- Executar `npm install` no diretório da aplicação específica
- Confirmar que a versão do Node.js é compatível
- Limpar `node_modules` e reinstalar se necessário

**Erros de Autenticação API**:
- Verificar que o ficheiro `.env` existe e contém valores corretos
- Confirmar que as chaves API são válidas e não expiradas
- Assegurar que as URLs dos endpoints estão corretas para a sua região

**Variáveis de Ambiente em Falta**:
- Copiar `.env.copy` para `.env`
- Preencher todos os valores requeridos para a lição em que está a trabalhar
- Reiniciar a aplicação após atualizar o `.env`

## Recursos Adicionais

- [Guia de Configuração do Curso](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Diretrizes de Contribuição](./CONTRIBUTING.md)
- [Código de Conduta](./CODE_OF_CONDUCT.md)
- [Política de Segurança](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Coleção de Exemplos Avançados de Código](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notas Específicas do Projeto

- Este é um **repositório educativo** focado em aprendizagem, não em código para produção
- Exemplos são intencionalmente simples e focados no ensino de conceitos
- A qualidade do código é equilibrada com a clareza educativa
- Cada lição é auto-contida e pode ser realizada independentemente
- O repositório suporta múltiplos provedores API: Azure OpenAI, OpenAI, Microsoft Foundry Models, e provedores offline como Foundry Local e Ollama
- O conteúdo é multilingue com fluxos de trabalho automatizados de tradução
- Comunidade ativa no Discord para dúvidas e suporte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->