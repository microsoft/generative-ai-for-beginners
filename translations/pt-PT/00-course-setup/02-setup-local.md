# Configuração Local 🖥️

**Use este guia se preferir correr tudo no seu próprio portátil.**   
Tem dois caminhos: **(A) Python nativo + virtual-env** ou **(B) Contêiner de Desenvolvimento VS Code com Docker**.  
Escolha o que parecer mais fácil — ambos levam às mesmas lições.

## 1.  Pré-requisitos

| Ferramenta          | Versão / Notas                                                                      |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (obtenha em <https://python.org>)                                            |
| **Git**             | Última versão (vem com Xcode / Git para Windows / gestor de pacotes Linux)          |
| **VS Code**         | Opcional mas recomendado <https://code.visualstudio.com>                            |
| **Docker Desktop**  | *Só* para a Opção B. Instalação gratuita: <https://docs.docker.com/desktop/>        |

> 💡 **Dica** – Verifique as ferramentas num terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opção A – Python Nativo (mais rápido)

### Passo 1  Clone este repositório

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Passo 2 Crie e ative um ambiente virtual

```bash
python -m venv .venv          # criar um
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ O prompt deve agora começar com (.venv) — isso significa que está dentro do ambiente.

### Passo 3 Instale as dependências

```bash
pip install -r requirements.txt
```

Pule para a Secção 3 sobre [chaves API](#3-adicione-as-suas-chaves-api)

## 2. Opção B – Contêiner de Desenvolvimento VS Code (Docker)

Configurámos este repositório e curso com um [contenedor de desenvolvimento](https://containers.dev?WT.mc_id=academic-105485-koreyst) que tem uma runtime universal que pode suportar desenvolvimento em Python3, .NET, Node.js e Java. A configuração relacionada está definida no ficheiro `devcontainer.json` localizado na pasta `.devcontainer/` na raiz deste repositório.

> **Porquê escolher isto?**
> Ambiente idêntico ao Codespaces; sem deriva de dependências.

### Passo 0 Instale os extras

Docker Desktop – confirme que ```docker --version``` funciona.
Extensão VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Passo 1 Abra o repositório no VS Code

Ficheiro ▸ Abrir Pasta…  → generative-ai-for-beginners

VS Code deteta .devcontainer/ e mostra um prompt.

### Passo 2 Reabra no contêiner

Clique em “Reabrir no Contêiner”. O Docker constrói a imagem (≈ 3 min na primeira vez).
Quando o prompt do terminal aparecer, está dentro do contêiner.

## 2.  Opção C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, assim como alguns pacotes.
O Conda é um gestor de pacotes, que facilita configurar e alternar entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacotes. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

### Passo 0  Instale o Miniconda

Siga o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurar.

```bash
conda --version
```

### Passo 1 Crie um ambiente virtual

Crie um novo ficheiro de ambiente (*environment.yml*). Se estiver a acompanhar usando Codespaces, crie este no diretório `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

### Passo 2  Preencha o seu ficheiro de ambiente

Adicione o seguinte excerto ao seu `environment.yml`

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

### Passo 3 Crie o seu ambiente Conda

Execute os comandos abaixo na sua linha de comandos/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # O subcaminho .devcontainer aplica-se apenas a configurações do Codespace
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se encontrar algum problema.

## 2  Opção D – Jupyter Clássico / Jupyter Lab (no seu navegador)

> **Para quem é isto?**  
> Para quem adora a interface clássica do Jupyter ou quer correr notebooks sem VS Code.  

### Passo 1  Certifique-se que o Jupyter está instalado

Para arrancar o Jupyter localmente, abra o terminal/linha de comandos, navegue até ao diretório do curso, e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isto irá iniciar uma instância do Jupyter e a URL para aceder será mostrada na janela da linha de comandos.

Depois de acessar a URL, deve ver a estrutura do curso e pode navegar para qualquer ficheiro `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Adicione as Suas Chaves API

Manter as suas chaves API seguras é importante ao criar qualquer tipo de aplicação. Recomendamos não guardar quaisquer chaves API diretamente no seu código. Fazer commit desses detalhes num repositório público pode resultar em problemas de segurança e até em custos indesejados se usados por pessoas mal-intencionadas.
Aqui está um guia passo a passo sobre como criar um ficheiro `.env` para Python e adicionar as suas credenciais dos Modelos Microsoft Foundry:

> **Nota:** Os Modelos GitHub (e a variável `GITHUB_TOKEN`) serão desativados no fim de Julho de 2026. Este guia usa [Modelos Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) em alternativa. Prefere trabalhar completamente offline? Veja [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Navegue até ao Diretório do Seu Projeto**: Abra o terminal ou prompt de comando e vá até ao diretório raiz do seu projeto onde pretende criar o ficheiro `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crie o Ficheiro `.env`**: Use o seu editor de texto preferido para criar um novo ficheiro chamado `.env`. Se estiver usando linha de comando, pode usar `touch` (em sistemas baseados em Unix) ou `echo` (no Windows):

   Sistemas baseados em Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edite o Ficheiro `.env`**: Abra o ficheiro `.env` num editor de texto (ex: VS Code, Notepad++, ou outro editor). Adicione as seguintes linhas no ficheiro, substituindo os espaços reservados pelo seu endpoint do projeto Microsoft Foundry e chave API reais:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Guarde o Ficheiro**: Guarde as alterações e feche o editor de texto.

5. **Instale `python-dotenv`**: Se ainda não o fez, terá de instalar o pacote `python-dotenv` para carregar as variáveis de ambiente do ficheiro `.env` na sua aplicação Python. Pode instalá-lo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregue as Variáveis de Ambiente no Seu Script Python**: No seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do ficheiro `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Carregar variáveis de ambiente a partir do ficheiro .env
   load_dotenv()

   # Aceder às variáveis dos Modelos Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

É tudo! Criou com sucesso um ficheiro `.env`, adicionou as credenciais dos Modelos Microsoft Foundry, e carregou-as na sua aplicação Python.

🔐 Nunca faça commit do .env — ele já está no .gitignore.
As instruções completas do provedor estão em [`providers.md`](03-providers.md).

## 4. O que fazer a seguir?

| Quero…             | Ir para…                                                                |
|--------------------|-------------------------------------------------------------------------|
| Começar a Lição 1  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Configurar um Provedor LLM | [`providers.md`](03-providers.md)                                       |
| Conhecer outros alunos | [Junte-se ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Resolução de Problemas

| Sintoma                                 | Solução                                                         |
|----------------------------------------|-----------------------------------------------------------------|
| `python not found`                     | Adicione Python ao PATH ou reabra o terminal após a instalação  |
| `pip` não consegue construir wheels (Windows) | `pip install --upgrade pip setuptools wheel` e tente novamente. |
| `ModuleNotFoundError: dotenv`           | Execute `pip install -r requirements.txt` (o ambiente não foi instalado). |
| Falha no build Docker *No space left*   | Docker Desktop ▸ *Settings* ▸ *Resources* → aumente o tamanho do disco. |
| O VS Code continua a pedir reabertura   | Pode ter ambas as Opções ativas; escolha uma (venv **ou** contêiner)|
| Erros 401 / 429 OpenAI                  | Verifique o valor de `OPENAI_API_KEY` / limites de taxa de pedido. |
| Erros usando Conda                      | Instale as bibliotecas Microsoft AI usando `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->