<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T16:22:24+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "br"
}
-->
# Configuração Local 🖥️

**Use este guia se você prefere rodar tudo no seu próprio laptop.**  
Você tem dois caminhos: **(A) Python nativo + virtual-env** ou **(B) Dev Container do VS Code com Docker**.  
Escolha o que achar mais fácil—ambos levam às mesmas aulas.

## 1.  Pré-requisitos

| Ferramenta           | Versão / Observações                                                                |
|----------------------|------------------------------------------------------------------------------------|
| **Python**           | 3.10 + (baixe em <https://python.org>)                                             |
| **Git**              | Última versão (vem com Xcode / Git para Windows / gerenciador de pacotes do Linux) |
| **VS Code**          | Opcional, mas recomendado <https://code.visualstudio.com>                          |
| **Docker Desktop**   | *Somente* para a Opção B. Instalação gratuita: <https://docs.docker.com/desktop/>  |

> 💡 **Dica** – Verifique as ferramentas no terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opção A – Python Nativo (mais rápido)

### Passo 1  Clone este repositório

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Passo 2 Crie e ative um ambiente virtual

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ O prompt agora deve começar com (.venv)—isso significa que você está dentro do ambiente.

### Passo 3 Instale as dependências

```bash
pip install -r requirements.txt
```

Pule para a Seção 3 sobre [chaves de API](../../../00-course-setup)

## 2. Opção B – Dev Container do VS Code (Docker)

Preparamos este repositório e curso com um [container de desenvolvimento](https://containers.dev?WT.mc_id=academic-105485-koreyst) que tem um runtime universal, suportando Python3, .NET, Node.js e Java. A configuração está definida no arquivo `devcontainer.json` localizado na pasta `.devcontainer/` na raiz do repositório.

>**Por que escolher isso?**
>Ambiente idêntico ao Codespaces; sem divergência de dependências.

### Passo 0 Instale os extras

Docker Desktop – confirme que ```docker --version``` funciona.
Extensão VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Passo 1 Abra o repositório no VS Code

Arquivo ▸ Abrir Pasta…  → generative-ai-for-beginners

O VS Code detecta o .devcontainer/ e exibe um aviso.

### Passo 2 Reabra no container

Clique em “Reopen in Container”. O Docker constrói a imagem (≈ 3 min na primeira vez).
Quando o prompt do terminal aparecer, você está dentro do container.

## 2.  Opção C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python e alguns pacotes.
O Conda é um gerenciador de pacotes que facilita criar e alternar entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) e pacotes Python. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

### Passo 0  Instale o Miniconda

Siga o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurar.

```bash
conda --version
```

### Passo 1 Crie um ambiente virtual

Crie um novo arquivo de ambiente (*environment.yml*). Se estiver acompanhando pelo Codespaces, crie dentro do diretório `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

### Passo 2  Preencha seu arquivo de ambiente

Adicione o trecho abaixo ao seu `environment.yml`

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

### Passo 3 Crie seu ambiente Conda

Execute os comandos abaixo no seu terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se tiver problemas.

## 2  Opção D – Jupyter Clássico / Jupyter Lab (no navegador)

> **Para quem é?**  
> Quem gosta da interface clássica do Jupyter ou quer rodar notebooks sem VS Code.  

### Passo 1  Certifique-se que o Jupyter está instalado

Para iniciar o Jupyter localmente, abra o terminal, navegue até o diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isso vai iniciar uma instância do Jupyter e a URL para acesso será exibida no terminal.

Ao acessar a URL, você verá o sumário do curso e poderá navegar para qualquer arquivo `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Adicione suas chaves de API

Manter suas chaves de API seguras é fundamental ao criar qualquer aplicação. Recomendamos não armazenar chaves de API diretamente no código. Se você enviar esses dados para um repositório público, pode ter problemas de segurança e até custos indesejados se alguém mal-intencionado usar.
Veja um passo a passo de como criar um arquivo `.env` para Python e adicionar o `GITHUB_TOKEN`:

1. **Navegue até o diretório do seu projeto**: Abra o terminal e vá até a raiz do projeto onde deseja criar o arquivo `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crie o arquivo `.env`**: Use seu editor de texto favorito para criar um arquivo chamado `.env`. Se estiver no terminal, pode usar `touch` (em sistemas Unix) ou `echo` (no Windows):

   Sistemas Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edite o arquivo `.env`**: Abra o `.env` em um editor de texto (VS Code, Notepad++, ou outro). Adicione a linha abaixo, trocando `your_github_token_here` pelo seu token do GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salve o arquivo**: Salve as alterações e feche o editor.

5. **Instale o `python-dotenv`**: Se ainda não instalou, você precisa do pacote `python-dotenv` para carregar variáveis do `.env` no seu app Python. Instale com `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregue as variáveis de ambiente no seu script Python**: No seu script, use o pacote `python-dotenv` para carregar as variáveis do `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Pronto! Você criou o arquivo `.env`, adicionou seu token do GitHub e carregou ele no seu app Python.

🔐 Nunca envie o .env—ele já está no .gitignore.
Instruções completas dos provedores estão em [`providers.md`](03-providers.md).

## 4. E agora?

| Quero…               | Ir para…                                                                 |
|----------------------|--------------------------------------------------------------------------|
| Começar a Aula 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Configurar um provedor LLM | [`providers.md`](03-providers.md)                                  |
| Conhecer outros alunos | [Entre no nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Solução de problemas

| Sintoma                                   | Solução                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| `python not found`                        | Adicione Python ao PATH ou reabra o terminal após instalar     |
| `pip` não consegue construir wheels (Windows) | `pip install --upgrade pip setuptools wheel` e tente novamente |
| `ModuleNotFoundError: dotenv`             | Execute `pip install -r requirements.txt` (ambiente não instalado)|
| Falha ao construir Docker *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → aumente o espaço em disco |
| VS Code fica pedindo para reabrir         | Você pode estar com duas opções ativas; escolha uma (venv **ou** container)|
| Erros 401 / 429 do OpenAI                 | Verifique o valor de `OPENAI_API_KEY` / limites de requisição  |
| Erros ao usar Conda                       | Instale as bibliotecas de IA da Microsoft com `conda install -c microsoft azure-ai-ml`|

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.