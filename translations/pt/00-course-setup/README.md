<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:07:15+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pt"
}
-->
# Começar este curso

Estamos muito entusiasmados por começar este curso e ver o que vais criar com IA Generativa!

Para garantir o teu sucesso, esta página descreve os passos de configuração, os requisitos técnicos e onde obter ajuda, se necessário.

## Passos de Configuração

Para começar este curso, precisas de completar os seguintes passos.

### 1. Fazer fork deste repositório

[Faz fork de todo este repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para a tua conta GitHub para poderes alterar qualquer código e completar os desafios. Também podes [dar estrela (🌟) a este repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para o encontrares mais facilmente, assim como repositórios relacionados.

### 2. Criar um codespace

Para evitar problemas de dependências ao executar o código, recomendamos que corras este curso num [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Podes criar um selecionando a opção `Code` na tua versão forkada deste repositório e escolhendo a opção **Codespaces**.

![Diálogo a mostrar botões para criar um codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Armazenar as tuas chaves API

Manter as tuas chaves API seguras é importante ao construir qualquer tipo de aplicação. Recomendamos que não guardes as chaves API diretamente no código. Cometer esses dados num repositório público pode causar problemas de segurança e até custos indesejados se forem usados por terceiros mal-intencionados.  
Aqui tens um guia passo a passo para criar um ficheiro `.env` para Python e adicionar o `GITHUB_TOKEN`:

1. **Navega até à pasta do teu projeto**: Abre o terminal ou prompt de comando e vai até à raiz do teu projeto onde queres criar o ficheiro `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Cria o ficheiro `.env`**: Usa o teu editor de texto preferido para criar um novo ficheiro chamado `.env`. Se estiveres a usar a linha de comandos, podes usar `touch` (em sistemas Unix) ou `echo` (no Windows):

   Sistemas Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edita o ficheiro `.env`**: Abre o ficheiro `.env` num editor de texto (ex: VS Code, Notepad++, ou outro). Adiciona a seguinte linha, substituindo `your_github_token_here` pelo teu token GitHub real:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Guarda o ficheiro**: Guarda as alterações e fecha o editor de texto.

5. **Instala o `python-dotenv`**: Se ainda não o fizeste, precisas de instalar o pacote `python-dotenv` para carregar as variáveis de ambiente do ficheiro `.env` para a tua aplicação Python. Podes instalar com `pip`:

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

E está feito! Criaste com sucesso um ficheiro `.env`, adicionaste o teu token GitHub e carregaste-o na tua aplicação Python.

## Como executar localmente no teu computador

Para executar o código localmente no teu computador, precisas de ter alguma versão do [Python instalado](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para usar o repositório, precisas de o clonar:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Depois de teres tudo configurado, podes começar!

## Passos Opcionais

### Instalar Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar o [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, e alguns pacotes.  
O Conda é um gestor de pacotes que facilita a criação e alternância entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacotes. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

Podes seguir o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para o configurar.

Com o Miniconda instalado, precisas de clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se ainda não o fizeste).

De seguida, precisas de criar um ambiente virtual. Para isso, cria um ficheiro de ambiente (_environment.yml_). Se estiveres a usar Codespaces, cria este ficheiro dentro da pasta `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

Preenche o ficheiro de ambiente com o seguinte snippet:

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

Se encontrares erros ao usar o conda, podes instalar manualmente as Bibliotecas Microsoft AI com o seguinte comando no terminal.

```
conda install -c microsoft azure-ai-ml
```

O ficheiro de ambiente especifica as dependências necessárias. `<environment-name>` é o nome que queres dar ao teu ambiente Conda, e `<python-version>` é a versão do Python que queres usar, por exemplo, `3` é a versão principal mais recente do Python.

Com isso feito, podes criar o teu ambiente Conda executando os comandos abaixo na linha de comandos/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulta o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se encontrares algum problema.

### Usar o Visual Studio Code com a extensão de suporte a Python

Recomendamos usar o editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [extensão de suporte a Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. No entanto, isto é apenas uma recomendação e não um requisito obrigatório.

> **Nota**: Ao abrir o repositório do curso no VS Code, tens a opção de configurar o projeto dentro de um contentor. Isto é possível graças à [pasta especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) presente no repositório do curso. Falaremos mais sobre isto mais à frente.

> **Nota**: Assim que clonares e abrires a pasta no VS Code, ele irá sugerir automaticamente que instales a extensão de suporte a Python.

> **Nota**: Se o VS Code sugerir que reabras o repositório num contentor, recusa este pedido para usares a versão local do Python instalada no teu computador.

### Usar Jupyter no navegador

Também podes trabalhar no projeto usando o ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) diretamente no teu navegador. Tanto o Jupyter clássico como o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento agradável com funcionalidades como auto-completar, realce de código, etc.

Para iniciar o Jupyter localmente, abre o terminal/linha de comandos, navega até à pasta do curso e executa:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isto irá iniciar uma instância do Jupyter e a URL para aceder será mostrada na janela do terminal.

Quando acederes à URL, deverás ver o índice do curso e poderás navegar para qualquer ficheiro `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Executar num contentor

Uma alternativa a configurar tudo no teu computador ou Codespace é usar um [contentor](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A pasta especial `.devcontainer` dentro do repositório do curso permite que o VS Code configure o projeto dentro de um contentor. Fora dos Codespaces, isto requer a instalação do Docker e, sinceramente, envolve algum trabalho, por isso recomendamos esta opção apenas a quem tem experiência com contentores.

Uma das melhores formas de manter as tuas chaves API seguras ao usar GitHub Codespaces é através dos Codespace Secrets. Por favor, segue o guia de [gestão de segredos nos Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saberes mais.

## Aulas e Requisitos Técnicos

O curso tem 6 aulas conceptuais e 6 aulas de programação.

Para as aulas de programação, usamos o Azure OpenAI Service. Vais precisar de acesso ao serviço Azure OpenAI e de uma chave API para executar este código. Podes candidatar-te para obter acesso [completando esta candidatura](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Enquanto esperas pela aprovação da tua candidatura, cada aula de programação inclui também um ficheiro `README.md` onde podes ver o código e os resultados.

## Usar o Azure OpenAI Service pela primeira vez

Se é a tua primeira vez a trabalhar com o Azure OpenAI service, segue este guia sobre como [criar e implementar um recurso Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usar a API OpenAI pela primeira vez

Se é a tua primeira vez a trabalhar com a API OpenAI, segue o guia sobre como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conhecer outros aprendizes

Criámos canais no nosso servidor oficial [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para conheceres outros aprendizes. Esta é uma ótima forma de fazer networking com outros empreendedores, construtores, estudantes e qualquer pessoa que queira evoluir em IA Generativa.

[![Junta-te ao canal discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipa do projeto também estará neste servidor Discord para ajudar os aprendizes.

## Contribuir

Este curso é uma iniciativa open-source. Se encontrares áreas para melhorar ou problemas, por favor cria um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou regista um [issue no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipa do projeto irá acompanhar todas as contribuições. Contribuir para open source é uma excelente forma de desenvolver a tua carreira em IA Generativa.

A maioria das contribuições requer que concordes com um Acordo de Licença de Contribuidor (CLA) declarando que tens o direito e efetivamente concedeste os direitos para usarmos a tua contribuição. Para mais detalhes, visita o [site do CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir texto neste repositório, certifica-te de que não usas tradução automática. Vamos verificar as traduções através da comunidade, por isso só te voluntaries para traduções em línguas que domines bem.

Quando submeteres um pull request, um bot CLA irá automaticamente determinar se precisas de fornecer um CLA e marcar o PR adequadamente (ex: etiqueta, comentário). Basta seguir as instruções do bot. Só precisas de fazer isto uma vez em todos os repositórios que usam o nosso CLA.

Este projeto adotou o [Código de Conduta Open Source da Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações, lê as FAQ do Código de Conduta ou contacta [Email opencode](opencode@microsoft.com) para quaisquer dúvidas ou comentários adicionais.

## Vamos Começar

Agora que completaste os passos necessários para este curso, vamos começar com uma [introdução à IA Generativa e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.