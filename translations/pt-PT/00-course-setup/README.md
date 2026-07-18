# Começar com este curso

Estamos muito entusiasmados por começares este curso e veres com o que te inspires para construir com IA Generativa!

Para garantir o teu sucesso, esta página descreve os passos de configuração, os requisitos técnicos e onde obter ajuda, se necessário.

## Passos de Configuração

Para começares a frequentar este curso, precisarás de completar os seguintes passos.

### 1. Faz fork deste Repositório

[Faz fork deste repositório completo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para a tua própria conta GitHub para poderes alterar qualquer código e completar os desafios. Também podes [estrelar (🌟) este repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para o encontrar mais facilmente, assim como os repositórios relacionados.

### 2. Cria um codespace

Para evitar problemas de dependências ao executar o código, recomendamos que executes este curso num [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

No teu fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/pt-PT/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adiciona um segredo

1. ⚙️ Ícone da engrenagem -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nomeia como OPENAI_API_KEY, cola a tua chave, Guarda.

### 3. O que fazer a seguir?

| Quero…               | Ir para…                                                               |
|---------------------|-------------------------------------------------------------------------|
| Começar a Aula 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Trabalhar offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Configurar um Provedor LLM | [`providers.md`](03-providers.md)                                    |
| Conhecer outros alunos | [Junta-te ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Resolução de problemas


| Sintoma                                   | Solução                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| A construção do container está parada > 10 min            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal não foi anexado; clica **+** ➜ *bash*                    |
| `401 Unauthorized` da OpenAI            | `OPENAI_API_KEY` errada / expirada                               |
| VS Code mostra “Dev container mounting…”   | Atualiza a aba do browser—às vezes o Codespaces perde a conexão  |
| Kernel do notebook em falta                 | Menu do notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Sistemas baseados em Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edita o Ficheiro `.env`**: Abre o ficheiro `.env` num editor de texto (ex.: VS Code, Notepad++ ou outro). Adiciona as linhas seguintes no ficheiro, substituindo os espaços reservados pelo teu endpoint e chave reais dos Microsoft Foundry Models (consulta [`providers.md`](03-providers.md) para saber como obter estes dados):

   > **Nota:** O GitHub Models (e a sua variável `GITHUB_TOKEN`) será descontinuado no final de Julho de 2026. Usa antes os [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Guarda o Ficheiro**: Guarda as alterações e fecha o editor de texto.

5. **Instala o `python-dotenv`**: Se ainda não o fizeste, precisas instalar o pacote `python-dotenv` para carregar variáveis de ambiente do ficheiro `.env` para a tua aplicação Python. Podes instalar usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carrega as Variáveis de Ambiente no Script Python**: No teu script Python, usa o pacote `python-dotenv` para carregar as variáveis do ficheiro `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Carregar variáveis de ambiente do ficheiro .env
   load_dotenv()

   # Aceder às variáveis dos Modelos Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Está feito! Criaste com sucesso um ficheiro `.env`, adicionaste as credenciais dos Microsoft Foundry Models e carregaste-as na tua aplicação Python.

## Como executar localmente no teu computador

Para executar o código localmente no teu computador, precisas de ter alguma versão do [Python instalado](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para usar o repositório, precisas cloná-lo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Assim que tudo estiver checado, podes começar!

## Passos Opcionais

### Instalar Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, bem como alguns pacotes.
O Conda é um gestor de pacotes que facilita configurar e alternar entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacotes. Também é útil para instalar pacotes que não estão disponíveis pelo `pip`.

Podes seguir o [guia de instalação MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para o configurar.

Depois de instalares o Miniconda, precisas clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se ainda não o fizeste)

Em seguida, precisas criar um ambiente virtual. Para isso com Conda, cria um novo ficheiro de ambiente (_environment.yml_). Se estiveres a usar Codespaces, cria-o dentro do diretório `.devcontainer`, assim `.devcontainer/environment.yml`.

Preenche o teu ficheiro de ambiente com o snippet abaixo:

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

Se receberes erros ao usar o conda, podes instalar manualmente as Bibliotecas Microsoft AI com o seguinte comando no terminal.

```
conda install -c microsoft azure-ai-ml
```

O ficheiro de ambiente especifica as dependências necessárias. `<environment-name>` refere-se ao nome que queres usar para o teu ambiente Conda, e `<python-version>` é a versão do Python que queres usar, por exemplo, `3` é a última versão maior do Python.

Com isto feito, podes criar o teu ambiente Conda executando os comandos abaixo no terminal/linha de comandos

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # O subcaminho .devcontainer aplica-se apenas a configurações Codespace
conda activate ai4beg
```

Consulta o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se encontrares algum problema.

### Usar Visual Studio Code com extensão de suporte a Python

Recomendamos usar o editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [extensão de suporte a Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Isto é, no entanto, uma recomendação e não um requisito obrigatório.

> **Nota**: Ao abrir o repositório do curso no VS Code, tens a opção de configurar o projeto dentro de um container. Isto porque existe a pasta especial [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dentro do repositório do curso. Falar-se-á mais disto depois.

> **Nota**: Depois de clonares e abrires o diretório no VS Code, ele irá automaticamente sugerir que instales uma extensão de suporte a Python.

> **Nota**: Se o VS Code te sugerir reabrir o repositório num container, recusa essa solicitação para usares a versão localmente instalada do Python.

### Usar Jupyter no Browser

Também podes trabalhar no projeto usando o ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) diretamente no teu navegador. Tanto o Jupyter clássico quanto o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento bastante agradável com recursos como auto-completar, realce de código, etc.

Para iniciar o Jupyter localmente, vai ao terminal/linha de comandos, navega para o diretório do curso e executa:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isto irá iniciar uma instância do Jupyter e a URL para aceder será mostrada na janela do terminal.

Depois de acederes à URL, deverás ver o plano do curso e ser capaz de navegar por qualquer ficheiro `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Executar num container

Uma alternativa para configurar tudo no teu computador ou Codespace é usar um [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A pasta especial `.devcontainer` no repositório do curso torna possível ao VS Code configurar o projeto dentro de um container. Fora dos Codespaces, isto requer instalar o Docker, e francamente, envolve algum trabalho, por isso recomendamos isto apenas para quem tem experiência a trabalhar com containers.

Uma das melhores formas de manter as chaves API seguras ao usar GitHub Codespaces é usar os Segredos dos Codespaces. Por favor, segue o guia de [gestão de segredos em Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saber mais.


## Aulas e Requisitos Técnicos

O curso tem aulas "Aprender" que explicam conceitos de IA Generativa e aulas "Construir" com exemplos práticos de código em **Python** e **TypeScript** sempre que possível.

Para as aulas de programação, usamos o Azure OpenAI no Microsoft Foundry. Precisarás de uma subscrição Azure e uma chave API. O acesso está aberto - sem necessidade de candidatura - por isso podes [criar um recurso Microsoft Foundry e implantar um modelo](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) para obter o teu endpoint e chave.

Cada aula de programação também inclui um ficheiro `README.md` onde podes ver o código e os resultados sem executar nada.

## Usar o Serviço Azure OpenAI pela primeira vez

Se é a tua primeira vez a trabalhar com o serviço Azure OpenAI, segue este guia sobre como [criar e implantar um recurso Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usar a API OpenAI pela primeira vez

Se é a tua primeira vez a trabalhar com a API OpenAI, segue o guia de como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conhecer Outros Aprendizes

Criámos canais no nosso servidor oficial de [Comunidade de IA no Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para conheceres outros aprendizes. Esta é uma ótima forma de fazer networking com outros empreendedores, construtores, estudantes e qualquer pessoa interessada em evoluir em IA Generativa.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipa do projeto também estará neste servidor Discord para ajudar qualquer aprendiz.

## Contribuir

Este curso é uma iniciativa open-source. Se vires áreas para melhorar ou problemas, por favor cria um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou reporta um [issue no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipa do projeto irá acompanhar todas as contribuições. Contribuir para open source é uma excelente forma de desenvolver a tua carreira em IA Generativa.

A maioria das contribuições requer que concordes com um Acordo de Licença de Contribuidor (CLA) declarando que tens direito e efectivamente concedes-nos os direitos para usar a tua contribuição. Para detalhes, visita o [site do CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir texto neste repositório, assegura-te de que não usas tradução automática. Vamos verificar as traduções com a comunidade, por isso, por favor, só te voluntaries para traduzir em idiomas em que és proficiente.


Quando submete um pedido de pull, um bot CLA determinará automaticamente se precisa de fornecer uma CLA e decorará o PR de forma apropriada (por exemplo, etiqueta, comentário). Simplesmente siga as instruções fornecidas pelo bot. Só precisará de fazer isto uma vez em todos os repositórios que utilizam a nossa CLA.

Este projeto adotou o [Código de Conduta do Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações, leia as Perguntas Frequentes sobre o Código de Conduta ou contacte [Email opencode](opencode@microsoft.com) para quaisquer questões ou comentários adicionais.

## Vamos Começar

Agora que completou os passos necessários para concluir este curso, vamos começar com uma [introdução à IA Generativa e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->