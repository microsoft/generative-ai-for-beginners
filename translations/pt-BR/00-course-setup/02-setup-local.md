# Configuração Local 🖥️

**Use este guia se preferir executar tudo no seu próprio laptop.**  
Você tem dois caminhos: **(A) Python nativo + virtual-env** ou **(B) VS Code Dev Container com Docker**.  
Escolha o que parecer mais fácil—ambos levam às mesmas lições.

## 1.  Pré-requisitos

| Ferramenta          | Versão / Notas                                                                      |
|---------------------|------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (obtenha em <https://python.org>)                                           |
| **Git**             | Última versão (vem com Xcode / Git para Windows / gerenciador de pacotes Linux)    |
| **VS Code**         | Opcional, mas recomendado <https://code.visualstudio.com>                          |
| **Docker Desktop**  | *Somente* para a Opção B. Instalação gratuita: <https://docs.docker.com/desktop/>  |

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
python -m venv .venv          # faça um
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ O prompt agora deve começar com (.venv)—isso significa que você está dentro do ambiente.

### Passo 3 Instale as dependências

```bash
pip install -r requirements.txt
```

Vá para a Seção 3 sobre [chaves de API](../../../00-course-setup)

## 2. Opção B – VS Code Dev Container (Docker)

Configuramos este repositório e curso com um [container de desenvolvimento](https://containers.dev?WT.mc_id=academic-105485-koreyst) que possui um runtime Universal que suporta desenvolvimento em Python3, .NET, Node.js e Java. A configuração relacionada está definida no arquivo `devcontainer.json` localizado na pasta `.devcontainer/` na raiz deste repositório.

>**Por que escolher isso?**  
>Ambiente idêntico ao Codespaces; sem deriva de dependências.

### Passo 0 Instale os extras

Docker Desktop – confirme que ```docker --version``` funciona.  
Extensão VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Passo 1 Abra o repositório no VS Code

Arquivo ▸ Abrir Pasta…  → generative-ai-for-beginners

O VS Code detecta .devcontainer/ e exibe um prompt.

### Passo 2 Reabra no container

Clique em “Reopen in Container”. O Docker constrói a imagem (≈ 3 min na primeira vez).  
Quando o prompt do terminal aparecer, você estará dentro do container.

## 2.  Opção C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, assim como alguns pacotes.  
O Conda em si é um gerenciador de pacotes, que facilita configurar e alternar entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) e pacotes Python. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

### Passo 0  Instale o Miniconda

Siga o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurá-lo.

```bash
conda --version
```

### Passo 1 Crie um ambiente virtual

Crie um novo arquivo de ambiente (*environment.yml*). Se estiver acompanhando usando Codespaces, crie este dentro do diretório `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

### Passo 2  Preencha seu arquivo de ambiente

Adicione o seguinte trecho ao seu `environment.yml`

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

Execute os comandos abaixo no seu terminal/linha de comando

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # O subcaminho .devcontainer se aplica apenas a configurações do Codespace
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se encontrar algum problema.

## 2  Opção D – Jupyter Clássico / Jupyter Lab (no seu navegador)

> **Para quem é isso?**  
> Para quem ama a interface clássica do Jupyter ou quer rodar notebooks sem VS Code.  

### Passo 1  Certifique-se que o Jupyter está instalado

Para iniciar o Jupyter localmente, vá ao terminal/linha de comando, navegue até o diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isso iniciará uma instância do Jupyter e a URL para acessá-la será mostrada na janela do terminal.

Ao acessar a URL, você deverá ver o sumário do curso e poderá navegar para qualquer arquivo `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Adicione Suas Chaves de API

Manter suas chaves de API seguras é importante ao construir qualquer tipo de aplicação. Recomendamos não armazenar nenhuma chave de API diretamente no seu código. Cometer esses detalhes em um repositório público pode resultar em problemas de segurança e até custos indesejados se usados por um agente malicioso.  
Aqui está um guia passo a passo sobre como criar um arquivo `.env` para Python e adicionar o `GITHUB_TOKEN`:

1. **Navegue até o Diretório do Seu Projeto**: Abra seu terminal ou prompt de comando e navegue até o diretório raiz do seu projeto onde deseja criar o arquivo `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crie o Arquivo `.env`**: Use seu editor de texto preferido para criar um novo arquivo chamado `.env`. Se estiver usando a linha de comando, você pode usar `touch` (em sistemas baseados em Unix) ou `echo` (no Windows):

   Sistemas baseados em Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edite o Arquivo `.env`**: Abra o arquivo `.env` em um editor de texto (ex: VS Code, Notepad++, ou qualquer outro editor). Adicione a seguinte linha ao arquivo, substituindo `your_github_token_here` pelo seu token real do GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salve o Arquivo**: Salve as alterações e feche o editor de texto.

5. **Instale o `python-dotenv`**: Se ainda não instalou, será necessário instalar o pacote `python-dotenv` para carregar variáveis de ambiente do arquivo `.env` para sua aplicação Python. Você pode instalá-lo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregue as Variáveis de Ambiente no Seu Script Python**: No seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do arquivo `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Carregar variáveis de ambiente do arquivo .env
   load_dotenv()

   # Acessar a variável GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

É isso! Você criou com sucesso um arquivo `.env`, adicionou seu token do GitHub e o carregou na sua aplicação Python.

🔐 Nunca comite o .env—ele já está no .gitignore.  
Instruções completas do provedor estão em [`providers.md`](03-providers.md).

## 4. E agora?

| Quero…              | Ir para…                                                               |
|---------------------|------------------------------------------------------------------------|
| Começar a Lição 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Configurar um Provedor LLM | [`providers.md`](03-providers.md)                                  |
| Conhecer outros alunos | [Junte-se ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Solução de Problemas

| Sintoma                                   | Solução                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Adicione Python ao PATH ou reabra o terminal após a instalação  |
| `pip` não consegue construir wheels (Windows) | `pip install --upgrade pip setuptools wheel` e tente novamente. |
| `ModuleNotFoundError: dotenv`             | Execute `pip install -r requirements.txt` (ambiente não instalado). |
| Falha na build do Docker *No space left*  | Docker Desktop ▸ *Configurações* ▸ *Recursos* → aumente o espaço em disco. |
| VS Code continua pedindo para reabrir     | Você pode ter ambas as Opções ativas; escolha uma (venv **ou** container) |
| Erros 401 / 429 do OpenAI                  | Verifique o valor de `OPENAI_API_KEY` / limites de taxa de requisição. |
| Erros usando Conda                         | Instale bibliotecas Microsoft AI usando `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->