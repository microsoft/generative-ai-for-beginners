<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T16:13:30+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "pt"
}
-->
# Configuração Local 🖥️

**Segue este guia se preferes trabalhar tudo no teu próprio portátil.**  
Tens duas opções: **(A) Python nativo + virtual-env** ou **(B) Dev Container do VS Code com Docker**.  
Escolhe a que te parecer mais simples—ambas levam às mesmas aulas.

## 1.  Pré-requisitos

| Ferramenta           | Versão / Notas                                                                       |
|----------------------|--------------------------------------------------------------------------------------|
| **Python**           | 3.10 + (obtém em <https://python.org>)                                               |
| **Git**              | Última versão (vem com Xcode / Git para Windows / gestor de pacotes Linux)           |
| **VS Code**          | Opcional mas recomendado <https://code.visualstudio.com>                             |
| **Docker Desktop**   | *Só* para a Opção B. Instalação gratuita: <https://docs.docker.com/desktop/>         |

> 💡 **Dica** – Verifica as ferramentas no terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opção A – Python Nativo (mais rápido)

### Passo 1  Clona este repositório

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Passo 2 Cria & ativa um ambiente virtual

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ O prompt deve agora começar com (.venv)—isso significa que estás dentro do ambiente.

### Passo 3 Instala as dependências

```bash
pip install -r requirements.txt
```

Avança para a Secção 3 sobre [chaves de API](../../../00-course-setup)

## 2. Opção B – Dev Container do VS Code (Docker)

Este repositório e curso estão preparados com um [container de desenvolvimento](https://containers.dev?WT.mc_id=academic-105485-koreyst) que tem um runtime universal capaz de suportar Python3, .NET, Node.js e Java. A configuração está definida no ficheiro `devcontainer.json` na pasta `.devcontainer/` na raiz deste repositório.

>**Porquê escolher isto?**
>Ambiente idêntico ao Codespaces; sem divergências de dependências.

### Passo 0 Instala os extras

Docker Desktop – confirma que ```docker --version``` funciona.
Extensão VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Passo 1 Abre o repositório no VS Code

Ficheiro ▸ Abrir Pasta…  → generative-ai-for-beginners

O VS Code deteta .devcontainer/ e mostra um aviso.

### Passo 2 Reabre no container

Clica em “Reopen in Container”. O Docker constrói a imagem (≈ 3 min na primeira vez).
Quando aparecer o prompt do terminal, já estás dentro do container.

## 2.  Opção C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python e alguns pacotes.
O Conda é um gestor de pacotes que facilita a criação e troca entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) e pacotes Python. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

### Passo 0  Instala o Miniconda

Segue o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurar.

```bash
conda --version
```

### Passo 1 Cria um ambiente virtual

Cria um novo ficheiro de ambiente (*environment.yml*). Se estiveres a seguir com Codespaces, cria-o dentro da pasta `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

### Passo 2  Preenche o ficheiro de ambiente

Adiciona o seguinte bloco ao teu `environment.yml`

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

### Passo 3 Cria o teu ambiente Conda

Executa os comandos abaixo na linha de comandos/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulta o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se tiveres problemas.

## 2  Opção D – Jupyter Clássico / Jupyter Lab (no navegador)

> **Para quem é?**  
> Quem prefere a interface clássica do Jupyter ou quer correr notebooks sem VS Code.  

### Passo 1  Garante que o Jupyter está instalado

Para iniciar o Jupyter localmente, vai ao terminal/linha de comandos, navega até à pasta do curso e executa:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isto vai iniciar uma instância do Jupyter e o URL para aceder será mostrado na janela do terminal.

Depois de aceder ao URL, deves ver o índice do curso e poder navegar para qualquer ficheiro `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Adiciona as tuas Chaves de API

Manter as tuas chaves de API seguras é fundamental ao criar qualquer aplicação. Recomendamos que não guardes chaves de API diretamente no código. Se as colocares num repositório público, podes ter problemas de segurança e até custos indesejados se alguém mal-intencionado as usar.
Aqui tens um guia passo-a-passo para criar um ficheiro `.env` para Python e adicionar o `GITHUB_TOKEN`:

1. **Navega até à pasta do teu projeto**: Abre o terminal ou linha de comandos e vai até à raiz do projeto onde queres criar o ficheiro `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Cria o ficheiro `.env`**: Usa o teu editor de texto preferido para criar um novo ficheiro chamado `.env`. Se estiveres na linha de comandos, podes usar `touch` (em sistemas Unix) ou `echo` (no Windows):

   Sistemas Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edita o ficheiro `.env`**: Abre o ficheiro `.env` num editor de texto (por exemplo, VS Code, Notepad++, ou outro). Adiciona a seguinte linha ao ficheiro, substituindo `your_github_token_here` pelo teu token real do GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Guarda o ficheiro**: Guarda as alterações e fecha o editor.

5. **Instala o `python-dotenv`**: Se ainda não tens, precisas de instalar o pacote `python-dotenv` para carregar as variáveis de ambiente do ficheiro `.env` na tua aplicação Python. Instala com `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carrega as variáveis de ambiente no teu script Python**: No teu script Python, usa o pacote `python-dotenv` para carregar as variáveis do ficheiro `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Pronto! Criaste o ficheiro `.env`, adicionaste o teu token do GitHub e já o carregaste na tua aplicação Python.

🔐 Nunca faças commit do .env—já está no .gitignore.
Instruções completas dos fornecedores estão em [`providers.md`](03-providers.md).

## 4. E agora?

| Quero…               | Vai para…                                                                 |
|----------------------|--------------------------------------------------------------------------|
| Começar a Lição 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Configurar um fornecedor LLM | [`providers.md`](03-providers.md)                                 |
| Conhecer outros alunos | [Junta-te ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Resolução de Problemas

| Sintoma                                   | Solução                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Adiciona Python ao PATH ou reabre o terminal após instalar      |
| `pip` não consegue construir wheels (Windows) | `pip install --upgrade pip setuptools wheel` e tenta novamente.|
| `ModuleNotFoundError: dotenv`             | Executa `pip install -r requirements.txt` (o ambiente não foi instalado).|
| Falha na construção do Docker *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → aumenta o espaço em disco.|
| VS Code pede sempre para reabrir          | Podes ter ambas as opções ativas; escolhe uma (venv **ou** container)|
| Erros 401 / 429 da OpenAI                 | Verifica o valor de `OPENAI_API_KEY` / limites de pedidos.      |
| Erros ao usar Conda                       | Instala as bibliotecas de IA da Microsoft com `conda install -c microsoft azure-ai-ml`|

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua nativa, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.