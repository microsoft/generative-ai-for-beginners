<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T14:32:17+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "pt"
}
-->
# Configuração Local 🖥️

**Use este guia se preferir executar tudo no seu próprio portátil.**  
Tem duas opções: **(A) Python nativo + virtual-env** ou **(B) Contêiner de Desenvolvimento VS Code com Docker**.  
Escolha a que lhe parecer mais fácil—ambas conduzem às mesmas lições.

## 1.  Pré-requisitos

| Ferramenta          | Versão / Notas                                                                      |
|---------------------|------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (obtenha em <https://python.org>)                                           |
| **Git**             | Última versão (vem com Xcode / Git para Windows / gestor de pacotes Linux)          |
| **VS Code**         | Opcional mas recomendado <https://code.visualstudio.com>                           |
| **Docker Desktop**  | *Apenas* para a Opção B. Instalação gratuita: <https://docs.docker.com/desktop/>    |

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
python -m venv .venv          # fazer um
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ O prompt deve agora começar com (.venv)—isso significa que está dentro do ambiente.

### Passo 3 Instale as dependências

```bash
pip install -r requirements.txt
```

Passe para a Secção 3 sobre [Chaves API](../../../00-course-setup)

## 2. Opção B – Contêiner de Desenvolvimento VS Code (Docker)

Configurámos este repositório e curso com um [contêiner de desenvolvimento](https://containers.dev?WT.mc_id=academic-105485-koreyst) que tem um runtime Universal que suporta desenvolvimento em Python3, .NET, Node.js e Java. A configuração relacionada está definida no ficheiro `devcontainer.json` localizado na pasta `.devcontainer/` na raiz deste repositório.

>**Porquê escolher isto?**  
>Ambiente idêntico ao Codespaces; sem deriva de dependências.

### Passo 0 Instale os extras

Docker Desktop – confirme que ```docker --version``` funciona.  
Extensão VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Passo 1 Abra o repositório no VS Code

Ficheiro ▸ Abrir Pasta…  → generative-ai-for-beginners

O VS Code deteta .devcontainer/ e mostra um prompt.

### Passo 2 Reabra no contêiner

Clique em “Reopen in Container”. O Docker constrói a imagem (≈ 3 min na primeira vez).  
Quando o prompt do terminal aparecer, está dentro do contêiner.

## 2.  Opção C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, bem como alguns pacotes.  
O Conda é um gestor de pacotes que facilita configurar e alternar entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacotes. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

### Passo 0  Instale o Miniconda

Siga o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurá-lo.

```bash
conda --version
```

### Passo 1 Crie um ambiente virtual

Crie um novo ficheiro de ambiente (*environment.yml*). Se estiver a seguir usando Codespaces, crie-o dentro da diretoria `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

### Passo 2  Preencha o seu ficheiro de ambiente

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

### Passo 3 Crie o seu ambiente Conda

Execute os comandos abaixo na linha de comando/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # O subcaminho .devcontainer aplica-se apenas a configurações Codespace
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se encontrar algum problema.

## 2  Opção D – Jupyter Clássico / Jupyter Lab (no seu navegador)

> **Para quem é isto?**  
> Para quem adora a interface clássica do Jupyter ou quer executar notebooks sem VS Code.  

### Passo 1  Certifique-se que o Jupyter está instalado

Para iniciar o Jupyter localmente, abra o terminal/linha de comando, navegue até à pasta do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isto iniciará uma instância do Jupyter e a URL para aceder será mostrada na janela da linha de comando.

Quando aceder à URL, deverá ver o índice do curso e poderá navegar para qualquer ficheiro `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Adicione as Suas Chaves API

Manter as suas chaves API seguras é importante ao construir qualquer tipo de aplicação. Recomendamos não armazenar chaves API diretamente no seu código. Cometer esses detalhes num repositório público pode resultar em problemas de segurança e até custos indesejados se usados por um agente malicioso.  
Aqui está um guia passo a passo sobre como criar um ficheiro `.env` para Python e adicionar o `GITHUB_TOKEN`:

1. **Navegue até à Pasta do Seu Projeto**: Abra o terminal ou prompt de comando e navegue até à raiz do seu projeto onde quer criar o ficheiro `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crie o Ficheiro `.env`**: Use o seu editor de texto preferido para criar um novo ficheiro chamado `.env`. Se estiver a usar a linha de comando, pode usar `touch` (em sistemas Unix) ou `echo` (no Windows):

   Sistemas Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edite o Ficheiro `.env`**: Abra o ficheiro `.env` num editor de texto (ex: VS Code, Notepad++, ou outro editor). Adicione a seguinte linha ao ficheiro, substituindo `your_github_token_here` pelo seu token GitHub real:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Guarde o Ficheiro**: Guarde as alterações e feche o editor de texto.

5. **Instale o `python-dotenv`**: Se ainda não o fez, precisará de instalar o pacote `python-dotenv` para carregar variáveis de ambiente do ficheiro `.env` para a sua aplicação Python. Pode instalá-lo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregue as Variáveis de Ambiente no Seu Script Python**: No seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do ficheiro `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Carregar variáveis de ambiente a partir do ficheiro .env
   load_dotenv()

   # Aceder à variável GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

É tudo! Criou com sucesso um ficheiro `.env`, adicionou o seu token GitHub e carregou-o na sua aplicação Python.

🔐 Nunca cometa o .env—ele já está no .gitignore.  
Instruções completas do fornecedor estão em [`providers.md`](03-providers.md).

## 4. O que vem a seguir?

| Quero…              | Ir para…                                                               |
|---------------------|------------------------------------------------------------------------|
| Começar a Lição 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Configurar um Provedor LLM | [`providers.md`](03-providers.md)                                  |
| Conhecer outros aprendizes | [Junte-se ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Resolução de Problemas

| Sintoma                                   | Solução                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Adicione Python ao PATH ou reabra o terminal após a instalação  |
| `pip` não consegue construir wheels (Windows) | `pip install --upgrade pip setuptools wheel` e tente novamente. |
| `ModuleNotFoundError: dotenv`             | Execute `pip install -r requirements.txt` (o ambiente não foi instalado). |
| Falha na construção Docker *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → aumente o espaço em disco. |
| VS Code continua a pedir para reabrir     | Pode ter ambas as opções ativas; escolha uma (venv **ou** contêiner) |
| Erros OpenAI 401 / 429                    | Verifique o valor de `OPENAI_API_KEY` / limites de taxa de pedidos. |
| Erros ao usar Conda                       | Instale bibliotecas Microsoft AI usando `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->