# Começando com este curso

Estamos muito animados para você começar este curso e ver o que você se inspira a construir com IA Generativa!

Para garantir seu sucesso, esta página descreve as etapas de configuração, requisitos técnicos e onde obter ajuda, se necessário.

## Etapas de Configuração

Para começar a fazer este curso, você precisará completar as seguintes etapas.

### 1. Faça um fork deste repositório

[Faça fork deste repositório inteiro](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para sua própria conta do GitHub para poder modificar qualquer código e completar os desafios. Você também pode [dar uma estrela (🌟) neste repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrá-lo e repositórios relacionados mais facilmente.

### 2. Crie um codespace

Para evitar problemas de dependência ao executar o código, recomendamos executar este curso em um [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

No seu fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/pt-BR/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adicione um segredo

1. ⚙️ Ícone de engrenagem -> Command Pallete-> Codespaces : Gerenciar segredo do usuário -> Adicionar um novo segredo.
2. Nomeie como OPENAI_API_KEY, cole sua chave, Salvar.

### 3. E agora?

| Eu quero…          | Vá para…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Começar a Aula 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Trabalhar offline        | [`setup-local.md`](02-setup-local.md)                                   |
| Configurar um Provedor de LLM | [`providers.md`](03-providers.md)                                        |
| Conhecer outros aprendizes | [Junte-se ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Solução de Problemas


| Sintoma                                   | Correção                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Construção do container travada > 10 min            | **Codespaces ➜ “Reconstruir Container”**                            |
| `python: command not found`               | Terminal não se anexou; clique em **+** ➜ *bash*                    |
| `401 Unauthorized` da OpenAI            | `OPENAI_API_KEY` incorreto/expirado                               |
| VS Code mostra “Dev container mounting…”   | Atualize a aba do navegador — Codespaces às vezes perde conexão   |
| Kernel do notebook ausente                   | Menu do notebook ➜ **Kernel ▸ Selecionar Kernel ▸ Python 3**           |

   Sistemas baseados em Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edite o arquivo `.env`**: Abra o arquivo `.env` em um editor de texto (por exemplo, VS Code, Notepad++ ou qualquer outro editor). Adicione as seguintes linhas ao arquivo, substituindo os espaços reservados pelo seu endpoint e chave reais dos Modelos Microsoft Foundry (veja [`providers.md`](03-providers.md) para saber como obter esses):

   > **Nota:** Os Modelos GitHub (e sua variável `GITHUB_TOKEN`) serão descontinuados no final de julho de 2026. Use os [Modelos Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) em vez disso.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Salve o Arquivo**: Salve as alterações e feche o editor de texto.

5. **Instale o `python-dotenv`**: Se ainda não o fez, você precisará instalar o pacote `python-dotenv` para carregar variáveis de ambiente do arquivo `.env` em sua aplicação Python. Você pode instalá-lo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregue Variáveis de Ambiente no seu Script Python**: No seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do arquivo `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Carregar variáveis de ambiente do arquivo .env
   load_dotenv()

   # Acessar as variáveis do Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

É isso! Você criou com sucesso um arquivo `.env`, adicionou suas credenciais dos Modelos Microsoft Foundry e as carregou em sua aplicação Python.

## Como executar localmente no seu computador

Para executar o código localmente no seu computador, você precisará ter alguma versão do [Python instalada](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para então usar o repositório, você precisa cloná-lo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Uma vez que você tenha tudo clonado, você pode começar!

## Etapas opcionais

### Instalando Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar o [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, bem como alguns pacotes.
O Conda em si é um gerenciador de pacotes, que facilita configurar e alternar entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) de Python e pacotes. Ele também é útil para instalar pacotes que não estão disponíveis via `pip`.

Você pode seguir o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurá-lo.

Com o Miniconda instalado, você precisa clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se ainda não o fez)

Em seguida, você precisa criar um ambiente virtual. Para fazer isso com o Conda, crie um novo arquivo de ambiente (_environment.yml_). Se você está acompanhando usando Codespaces, crie este arquivo dentro do diretório `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

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

Se você estiver enfrentando erros usando o conda, pode instalar manualmente as Bibliotecas Microsoft AI usando o seguinte comando no terminal.

```
conda install -c microsoft azure-ai-ml
```

O arquivo de ambiente especifica as dependências que precisamos. `<environment-name>` refere-se ao nome que você gostaria de usar para seu ambiente Conda, e `<python-version>` é a versão do Python que você deseja usar, por exemplo, `3` é a última versão principal do Python.

Com isso feito, você pode criar seu ambiente Conda executando os comandos abaixo na sua linha de comando/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # O subcaminho .devcontainer se aplica apenas a configurações de Codespace
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se tiver algum problema.

### Usando Visual Studio Code com a extensão de suporte a Python

Recomendamos usar o editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [extensão de suporte a Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Esta é, no entanto, mais uma recomendação do que um requisito definitivo.

> **Nota**: Ao abrir o repositório do curso no VS Code, você tem a opção de configurar o projeto dentro de um container. Isso é possível graças ao diretório especial [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) encontrado no repositório do curso. Falaremos mais sobre isso mais adiante.

> **Nota**: Assim que você clonar e abrir o diretório no VS Code, ele sugerirá automaticamente que instale uma extensão de suporte a Python.

> **Nota**: Se o VS Code sugerir que você reabra o repositório em um container, recuse esse pedido para usar a versão local instalada do Python.

### Usando Jupyter no navegador

Você também pode trabalhar no projeto usando o [ambiente Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) diretamente dentro do seu navegador. Tanto o Jupyter clássico quanto o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento bastante agradável com recursos como autocompletar, destaque de código, etc.

Para iniciar o Jupyter localmente, vá até o terminal/linha de comando, navegue até o diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isso iniciará uma instância do Jupyter e a URL para acessá-la será mostrada na janela do terminal.

Uma vez que você acesse a URL, deverá ver o conteúdo do curso e poderá navegar para qualquer arquivo `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Executando em um container

Uma alternativa para configurar tudo no seu computador ou Codespace é usar um [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A pasta especial `.devcontainer` dentro do repositório do curso permite que o VS Code configure o projeto dentro de um container. Fora dos Codespaces, isso exigirá a instalação do Docker e, francamente, envolve um pouco de trabalho, então recomendamos isso apenas para quem tem experiência com containers.

Uma das melhores maneiras de manter suas chaves API seguras ao usar GitHub Codespaces é usando Segredos do Codespace. Por favor, siga o guia de [gerenciamento de segredos do Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saber mais.


## Aulas e Requisitos Técnicos

O curso tem 6 aulas conceituais e 6 aulas de codificação.

Para as aulas de codificação, estamos usando o Azure OpenAI Service. Você precisará de acesso ao serviço Azure OpenAI e de uma chave API para executar este código. Você pode solicitar acesso [completando esta aplicação](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Enquanto aguarda o processamento da sua aplicação, cada aula de codificação também inclui um arquivo `README.md` onde você pode visualizar o código e os resultados.

## Usando o Azure OpenAI Service pela primeira vez

Se esta é a sua primeira vez trabalhando com o serviço Azure OpenAI, por favor siga este guia sobre como [criar e implantar um recurso do Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando a API OpenAI pela primeira vez

Se esta é a sua primeira vez trabalhando com a API OpenAI, por favor siga o guia sobre como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conheça outros aprendizes

Criamos canais no nosso servidor oficial [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para conhecer outros aprendizes. Esta é uma ótima forma de fazer networking com outros empreendedores, construtores, estudantes e qualquer pessoa que deseja avançar em IA Generativa.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipe do projeto também estará neste servidor Discord para ajudar qualquer aprendiz.

## Contribua

Este curso é uma iniciativa de código aberto. Se você identificar áreas para melhorias ou problemas, por favor crie um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou registre um [issue no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipe do projeto estará acompanhando todas as contribuições. Contribuir para código aberto é uma forma incrível de construir sua carreira em IA Generativa.

A maioria das contribuições exige que você concorde com um Acordo de Licença de Contribuição (CLA) declarando que você tem o direito e de fato concede a nós os direitos para usar sua contribuição. Para detalhes, visite o site do [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir texto neste repositório, por favor tenha certeza de não usar tradução automática. Nós verificaremos as traduções pela comunidade, portanto, por favor voluntarie-se apenas para traduções em idiomas nos quais você é proficiente.

Quando você enviar um pull request, um bot CLA determinará automaticamente se você precisa fornecer um CLA e decorará o PR apropriadamente (por exemplo, etiqueta, comentário). Basta seguir as instruções fornecidas pelo bot. Você precisará fazer isso apenas uma vez em todos os repositórios que usam nosso CLA.


Este projeto adotou o [Código de Conduta de Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações, leia o FAQ do Código de Conduta ou entre em contato com [Email opencode](opencode@microsoft.com) para quaisquer perguntas ou comentários adicionais.

## Vamos Começar

Agora que você completou as etapas necessárias para concluir este curso, vamos começar com uma [introdução à IA Generativa e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->