<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T08:56:22+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "br"
}
-->
# Começando com este curso

Estamos muito animados para que você comece este curso e veja o que você se inspira a construir com a IA Generativa!

Para garantir seu sucesso, esta página descreve os passos de configuração, requisitos técnicos e onde obter ajuda, se necessário.

## Passos de Configuração

Para começar a fazer este curso, você precisará completar os seguintes passos.

### 1. Fork deste Repositório

[Fork todo este repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para sua própria conta do GitHub para poder alterar qualquer código e completar os desafios. Você também pode [dar estrela (🌟) neste repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrá-lo e repositórios relacionados mais facilmente.

### 2. Criar um Codespace

Para evitar quaisquer problemas de dependência ao executar o código, recomendamos executar este curso em um [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Isso pode ser criado selecionando a opção `Code` na versão que você fez fork deste repositório e selecionando a opção **Codespaces**.

![Diálogo mostrando botões para criar um codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Armazenando Suas Chaves de API

Manter suas chaves de API seguras e protegidas é importante ao construir qualquer tipo de aplicação. Recomendamos não armazenar nenhuma chave de API diretamente no seu código. Cometer esses detalhes para um repositório público pode resultar em problemas de segurança e até custos indesejados se usados por um agente mal-intencionado.
Aqui está um guia passo a passo sobre como criar um arquivo `.env` para Python e adicionar o `GITHUB_TOKEN`:

1. **Navegue até o Diretório do Seu Projeto**: Abra seu terminal ou prompt de comando e navegue até o diretório raiz do seu projeto onde você deseja criar o arquivo `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crie o Arquivo `.env`**: Use seu editor de texto preferido para criar um novo arquivo chamado `.env`. Se você estiver usando a linha de comando, pode usar `touch` (on Unix-based systems) or `echo` (no Windows):

   Sistemas baseados em Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Edite o Arquivo `.env`**: Abra o arquivo `.env` em um editor de texto (por exemplo, VS Code, Notepad++, ou qualquer outro editor). Adicione a seguinte linha ao arquivo, substituindo `your_github_token_here` pelo seu token real do GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salve o Arquivo**: Salve as alterações e feche o editor de texto.

5. **Instale o pacote `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` para carregar variáveis de ambiente do arquivo `.env` em sua aplicação Python. Você pode instalá-lo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregue Variáveis de Ambiente em Seu Script Python**: Em seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do arquivo `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Isso é tudo! Você criou com sucesso um arquivo `.env`, adicionou seu token do GitHub e o carregou em sua aplicação Python.

## Como Executar Localmente em Seu Computador

Para executar o código localmente em seu computador, você precisará ter alguma versão do [Python instalada](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para então usar o repositório, você precisa cloná-lo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Uma vez que você tenha tudo verificado, pode começar!

## Passos Opcionais

### Instalando Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, assim como alguns pacotes.
Conda em si é um gerenciador de pacotes, que facilita a configuração e alternância entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacotes. Ele também é útil para instalar pacotes que não estão disponíveis via `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Vá em frente e preencha seu arquivo de ambiente com o trecho abaixo:

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

Se você encontrar erros usando conda, pode instalar manualmente as Bibliotecas de IA da Microsoft usando o seguinte comando em um terminal.

```
conda install -c microsoft azure-ai-ml
```

O arquivo de ambiente especifica as dependências que precisamos. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` é a última versão principal do Python.

Com isso feito, você pode ir em frente e criar seu ambiente Conda executando os comandos abaixo em sua linha de comando/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se encontrar algum problema.

### Usando o Visual Studio Code com a extensão de suporte ao Python

Recomendamos usar o editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [extensão de suporte ao Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Isso, no entanto, é mais uma recomendação e não um requisito definitivo.

> **Nota**: Ao abrir o repositório do curso no VS Code, você tem a opção de configurar o projeto dentro de um container. Isso é por causa do diretório [especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) encontrado dentro do repositório do curso. Mais sobre isso mais tarde.

> **Nota**: Uma vez que você clona e abre o diretório no VS Code, ele automaticamente sugere que você instale uma extensão de suporte ao Python.

> **Nota**: Se o VS Code sugerir que você reabra o repositório em um container, recuse essa solicitação para usar a versão local instalada do Python.

### Usando Jupyter no Navegador

Você também pode trabalhar no projeto usando o ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) diretamente no seu navegador. Tanto o Jupyter clássico quanto o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento bastante agradável com recursos como auto-completar, destaque de código, etc.

Para iniciar o Jupyter localmente, vá até o terminal/linha de comando, navegue até o diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isso iniciará uma instância do Jupyter e o URL para acessá-lo será mostrado na janela da linha de comando.

Uma vez que você acessa o URL, deve ver o esboço do curso e ser capaz de navegar para qualquer arquivo `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` onde pode visualizar o código e os resultados.

## Usando o Serviço Azure OpenAI pela primeira vez

Se esta é sua primeira vez trabalhando com o serviço Azure OpenAI, por favor siga este guia sobre como [criar e implantar um recurso do Serviço Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando a API OpenAI pela primeira vez

Se esta é sua primeira vez trabalhando com a API OpenAI, por favor siga o guia sobre como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conheça Outros Aprendizes

Criamos canais em nosso servidor oficial [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para conhecer outros aprendizes. Esta é uma ótima maneira de fazer networking com outros empreendedores, construtores, estudantes e qualquer pessoa que esteja buscando se aprimorar em IA Generativa.

[![Junte-se ao canal do discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipe do projeto também estará neste servidor Discord para ajudar os aprendizes.

## Contribua

Este curso é uma iniciativa de código aberto. Se você ver áreas de melhoria ou problemas, por favor, crie um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou registre um [problema no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipe do projeto estará acompanhando todas as contribuições. Contribuir para o código aberto é uma maneira incrível de construir sua carreira em IA Generativa.

A maioria das contribuições exige que você concorde com um Acordo de Licença de Contribuidor (CLA) declarando que você tem o direito de e realmente concede-nos os direitos de usar sua contribuição. Para detalhes, visite [CLA, site do Acordo de Licença de Contribuidor](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir texto neste repositório, por favor, certifique-se de não usar tradução automática. Vamos verificar as traduções através da comunidade, então, por favor, só se voluntarie para traduções em idiomas nos quais você é proficiente.

Quando você enviar um pull request, um CLA-bot irá automaticamente determinar se você precisa fornecer um CLA e decorar o PR adequadamente (por exemplo, etiqueta, comentário). Basta seguir as instruções fornecidas pelo bot. Você só precisará fazer isso uma vez em todos os repositórios usando nosso CLA.

Este projeto adotou o [Código de Conduta de Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações, leia as Perguntas Frequentes do Código de Conduta ou entre em contato com [Email opencode](opencode@microsoft.com) com quaisquer perguntas ou comentários adicionais.

## Vamos Começar

Agora que você completou os passos necessários para completar este curso, vamos começar com uma [introdução à IA Generativa e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.