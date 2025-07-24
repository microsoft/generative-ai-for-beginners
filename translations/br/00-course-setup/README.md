<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:07:37+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "br"
}
-->
# Começando com este curso

Estamos muito animados para você começar este curso e ver o que vai se inspirar a criar com IA Generativa!

Para garantir seu sucesso, esta página descreve os passos de configuração, os requisitos técnicos e onde obter ajuda, se necessário.

## Passos de Configuração

Para começar a fazer este curso, você precisará completar os seguintes passos.

### 1. Faça um fork deste repositório

[Fork este repositório completo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para sua própria conta no GitHub para poder alterar qualquer código e completar os desafios. Você também pode [dar uma estrela (🌟) neste repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrá-lo e encontrar repositórios relacionados com mais facilidade.

### 2. Crie um codespace

Para evitar problemas de dependência ao executar o código, recomendamos rodar este curso em um [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Isso pode ser criado selecionando a opção `Code` na sua versão forkada deste repositório e escolhendo a opção **Codespaces**.

![Diálogo mostrando botões para criar um codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Armazenando suas chaves de API

Manter suas chaves de API seguras é importante ao construir qualquer tipo de aplicação. Recomendamos não armazenar nenhuma chave de API diretamente no seu código. Cometer esses detalhes em um repositório público pode resultar em problemas de segurança e até custos indesejados se usados por alguém mal-intencionado.  
Aqui está um guia passo a passo de como criar um arquivo `.env` para Python e adicionar o `GITHUB_TOKEN`:

1. **Navegue até o diretório do seu projeto**: Abra seu terminal ou prompt de comando e navegue até o diretório raiz do seu projeto onde deseja criar o arquivo `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crie o arquivo `.env`**: Use seu editor de texto preferido para criar um novo arquivo chamado `.env`. Se estiver usando a linha de comando, você pode usar `touch` (em sistemas baseados em Unix) ou `echo` (no Windows):

   Sistemas baseados em Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edite o arquivo `.env`**: Abra o arquivo `.env` em um editor de texto (ex: VS Code, Notepad++ ou qualquer outro editor). Adicione a seguinte linha no arquivo, substituindo `your_github_token_here` pelo seu token real do GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salve o arquivo**: Salve as alterações e feche o editor de texto.

5. **Instale o `python-dotenv`**: Se ainda não instalou, será necessário instalar o pacote `python-dotenv` para carregar variáveis de ambiente do arquivo `.env` para sua aplicação Python. Você pode instalá-lo usando o `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregue as variáveis de ambiente no seu script Python**: No seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do arquivo `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Pronto! Você criou com sucesso um arquivo `.env`, adicionou seu token do GitHub e o carregou na sua aplicação Python.

## Como rodar localmente no seu computador

Para rodar o código localmente no seu computador, você precisará ter alguma versão do [Python instalado](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para usar o repositório, você precisa cloná-lo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Depois de ter tudo configurado, você pode começar!

## Passos Opcionais

### Instalando Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar o [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, além de alguns pacotes.  
O Conda é um gerenciador de pacotes que facilita configurar e alternar entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) e pacotes Python. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

Você pode seguir o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurá-lo.

Com o Miniconda instalado, você precisa clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se ainda não fez isso).

Em seguida, você precisa criar um ambiente virtual. Para isso, com o Conda, crie um novo arquivo de ambiente (_environment.yml_). Se estiver acompanhando usando Codespaces, crie este arquivo dentro do diretório `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

Preencha seu arquivo de ambiente com o trecho abaixo:

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

Se você encontrar erros usando conda, pode instalar manualmente as Bibliotecas Microsoft AI usando o seguinte comando no terminal.

```
conda install -c microsoft azure-ai-ml
```

O arquivo de ambiente especifica as dependências que precisamos. `<environment-name>` se refere ao nome que você deseja usar para seu ambiente Conda, e `<python-version>` é a versão do Python que você quer usar, por exemplo, `3` é a última versão principal do Python.

Com isso feito, você pode criar seu ambiente Conda executando os comandos abaixo no seu terminal/linha de comando:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se tiver algum problema.

### Usando Visual Studio Code com a extensão de suporte a Python

Recomendamos usar o editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [extensão de suporte a Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Isso é mais uma recomendação do que uma exigência definitiva.

> **Nota**: Ao abrir o repositório do curso no VS Code, você tem a opção de configurar o projeto dentro de um container. Isso é possível graças ao [diretório especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) presente no repositório do curso. Falaremos mais sobre isso depois.

> **Nota**: Assim que você clonar e abrir o diretório no VS Code, ele sugerirá automaticamente que você instale a extensão de suporte a Python.

> **Nota**: Se o VS Code sugerir que você reabra o repositório em um container, recuse essa solicitação para usar a versão do Python instalada localmente.

### Usando Jupyter no navegador

Você também pode trabalhar no projeto usando o ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) diretamente no seu navegador. Tanto o Jupyter clássico quanto o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento bastante agradável, com recursos como auto-completar, realce de código, etc.

Para iniciar o Jupyter localmente, vá até o terminal/linha de comando, navegue até o diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isso iniciará uma instância do Jupyter e a URL para acessá-la será exibida na janela do terminal.

Ao acessar a URL, você verá o sumário do curso e poderá navegar para qualquer arquivo `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Rodando em um container

Uma alternativa para configurar tudo no seu computador ou Codespace é usar um [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A pasta especial `.devcontainer` dentro do repositório do curso permite que o VS Code configure o projeto dentro de um container. Fora dos Codespaces, isso exigirá a instalação do Docker e, sinceramente, envolve um pouco de trabalho, então recomendamos isso apenas para quem tem experiência com containers.

Uma das melhores formas de manter suas chaves de API seguras ao usar GitHub Codespaces é utilizando os Secrets do Codespace. Por favor, siga o guia de [gerenciamento de secrets no Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saber mais.

## Aulas e Requisitos Técnicos

O curso tem 6 aulas conceituais e 6 aulas de programação.

Para as aulas de programação, usamos o Azure OpenAI Service. Você precisará de acesso ao serviço Azure OpenAI e uma chave de API para rodar este código. Você pode solicitar acesso [preenchendo esta aplicação](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Enquanto aguarda a aprovação da sua solicitação, cada aula de programação também inclui um arquivo `README.md` onde você pode ver o código e os resultados.

## Usando o Azure OpenAI Service pela primeira vez

Se esta é sua primeira vez trabalhando com o Azure OpenAI service, siga este guia de como [criar e implantar um recurso do Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando a API OpenAI pela primeira vez

Se esta é sua primeira vez trabalhando com a API OpenAI, siga o guia de como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conheça outros aprendizes

Criamos canais no nosso servidor oficial do [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para você conhecer outros aprendizes. Esta é uma ótima forma de fazer networking com outros empreendedores, desenvolvedores, estudantes e qualquer pessoa que queira evoluir em IA Generativa.

[![Entrar no canal do discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipe do projeto também estará neste servidor Discord para ajudar os aprendizes.

## Contribua

Este curso é uma iniciativa open-source. Se você encontrar áreas para melhorar ou problemas, por favor crie um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou registre uma [issue no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipe do projeto acompanhará todas as contribuições. Contribuir para open source é uma forma incrível de construir sua carreira em IA Generativa.

A maioria das contribuições exige que você concorde com um Acordo de Licença de Contribuidor (CLA) declarando que você tem o direito e realmente concede a nós os direitos de usar sua contribuição. Para detalhes, visite o site do [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir textos neste repositório, por favor, não use tradução automática. Verificaremos as traduções pela comunidade, então só se ofereça para traduzir idiomas nos quais você seja proficiente.

Quando você enviar um pull request, um bot CLA determinará automaticamente se você precisa fornecer um CLA e marcará o PR adequadamente (ex: label, comentário). Basta seguir as instruções do bot. Você precisará fazer isso apenas uma vez para todos os repositórios que usam nosso CLA.

Este projeto adotou o [Código de Conduta Open Source da Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações, leia as FAQs do Código de Conduta ou entre em contato pelo [Email opencode](opencode@microsoft.com) para dúvidas ou comentários adicionais.

## Vamos Começar

Agora que você completou os passos necessários para fazer este curso, vamos começar com uma [introdução à IA Generativa e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.