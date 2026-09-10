# Começando com este curso

Estamos muito animados para você começar este curso e ver com o que você vai se inspirar para construir com IA Generativa!

Para garantir seu sucesso, esta página descreve os passos de configuração, os requisitos técnicos e onde pedir ajuda, se necessário.

## Passos para Configuração

Para começar a fazer este curso, você precisará completar os seguintes passos.

### 1. Faça um Fork deste Repositório

[Faça um fork deste repositório inteiro](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para sua própria conta no GitHub para poder alterar qualquer código e completar os desafios. Você também pode [dar uma estrela (🌟) neste repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrá-lo e os repositórios relacionados mais facilmente.

### 2. Crie um codespace

Para evitar qualquer problema de dependência ao executar o código, recomendamos rodar este curso em um [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

No seu fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/pt-BR/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adicione um segredo

1. ⚙️ Ícone de engrenagem -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Nomeie como OPENAI_API_KEY, cole sua chave, Salvar.

### 3. O que vem a seguir?

| Eu quero…           | Ir para…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Começar a Lição 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Trabalhar offline   | [`setup-local.md`](02-setup-local.md)                                   |
| Configurar um Provedor LLM | [`providers.md`](03-providers.md)                                        |
| Conhecer outros alunos | [Junte-se ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Solução de Problemas


| Sintoma                                    | Correção                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Build do container travado > 10 min       | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                 | Terminal não abriu; clique em **+** ➜ *bash*                    |
| `401 Unauthorized` da OpenAI                | `OPENAI_API_KEY` errada ou expirada                             |
| VS Code mostra “Dev container mounting…”    | Atualize a aba do navegador – Codespaces às vezes perde conexão |
| Kernel do notebook ausente                  | Menu do notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Sistemas baseados em Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edite o arquivo `.env`**: Abra o arquivo `.env` em um editor de texto (ex.: VS Code, Notepad++ ou qualquer outro editor). Adicione as seguintes linhas ao arquivo, substituindo os espaços reservados pelo seu endpoint e chave reais do Microsoft Foundry Models (veja [`providers.md`](03-providers.md) para saber como conseguir):

   > **Nota:** Os Modelos GitHub (e sua variável `GITHUB_TOKEN`) serão descontinuados no final de julho de 2026. Use os [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) no lugar.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Salve o arquivo**: Salve as alterações e feche o editor de texto.

5. **Instale `python-dotenv`**: Se você ainda não o fez, precisará instalar o pacote `python-dotenv` para carregar variáveis de ambiente do arquivo `.env` na sua aplicação Python. Você pode instalá-lo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregue as Variáveis de Ambiente no seu Script Python**: No seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do arquivo `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Carregar variáveis de ambiente do arquivo .env
   load_dotenv()

   # Acessar as variáveis dos Modelos Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

É isso! Você criou com sucesso um arquivo `.env`, adicionou suas credenciais do Microsoft Foundry Models e as carregou na sua aplicação Python.

## Como rodar localmente no seu computador

Para rodar o código localmente em seu computador, você precisará ter alguma versão do [Python instalado](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para então usar o repositório, você precisa cloná-lo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Depois que tudo estiver baixado, você pode começar!

## Passos Opcionais

### Instalando Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, assim como alguns pacotes.
O próprio Conda é um gerenciador de pacotes, que facilita configurar e alternar entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) e pacotes do Python. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

Você pode seguir o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurá-lo.

Com o Miniconda instalado, você precisa clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se ainda não tiver feito isso)

Em seguida, você precisa criar um ambiente virtual. Para fazer isso com Conda, crie um novo arquivo de ambiente (_environment.yml_). Se estiver usando Codespaces, crie-o dentro do diretório `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

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

Se você estiver recebendo erros ao usar conda, pode instalar manualmente as Bibliotecas AI da Microsoft usando o comando seguinte no terminal.

```
conda install -c microsoft azure-ai-ml
```

O arquivo de ambiente especifica as dependências que precisamos. `<environment-name>` refere-se ao nome que você quer usar para seu ambiente Conda, e `<python-version>` é a versão do Python que deseja usar, por exemplo, `3` é a última versão principal do Python.

Feito isso, você pode criar seu ambiente Conda executando os comandos abaixo na linha de comando/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # O subcaminho .devcontainer se aplica apenas a configurações do Codespace
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se encontrar qualquer problema.

### Usando Visual Studio Code com a extensão de suporte a Python

Recomendamos usar o editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [extensão de suporte a Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Isso é, no entanto, mais uma recomendação do que um requisito obrigatório.

> **Nota**: Ao abrir o repositório do curso no VS Code, você pode configurar o projeto dentro de um container. Isso é possível por causa do [diretório especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) encontrado no repositório do curso. Mais sobre isso depois.

> **Nota**: Assim que você clona e abre o diretório no VS Code, ele automaticamente sugerirá que instale a extensão de suporte a Python.

> **Nota**: Se o VS Code sugerir que você reabra o repositório em um container, recuse esse pedido para usar a versão do Python instalada localmente.

### Usando Jupyter no Navegador

Você também pode trabalhar no projeto usando o [ambiente Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) diretamente no seu navegador. Tanto o Jupyter clássico quanto o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) fornecem um ambiente de desenvolvimento agradável com recursos como auto-completação, realce de código, etc.

Para iniciar o Jupyter localmente, vá até o terminal/linha de comando, navegue para o diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isso iniciará uma instância do Jupyter e a URL para acessá-la será exibida na janela do terminal.

Ao acessar a URL, você verá o sumário do curso e poderá navegar para qualquer arquivo `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Executando em um container

Uma alternativa para configurar tudo no seu computador ou Codespace é usar um [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A pasta especial `.devcontainer` no repositório do curso permite que o VS Code configure o projeto dentro de um container. Fora dos Codespaces, isso requer a instalação do Docker e, para falar a verdade, envolve um pouco de trabalho, então recomendamos isso apenas para quem tem experiência com containers.

Uma das melhores formas de manter suas chaves de API seguras ao usar GitHub Codespaces é usando Secrets do Codespace. Por favor, siga o guia de [gerenciamento de segredos do Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saber mais sobre isso.


## Lições e Requisitos Técnicos

O curso possui lições "Learn" que explicam conceitos de IA Generativa e lições "Build" com exemplos práticos de código em **Python** e **TypeScript** onde possível.

Para as lições de código, usamos Azure OpenAI no Microsoft Foundry. Você precisará de uma assinatura Azure e uma chave API. O acesso está aberto – não é necessário aplicar – então você pode [criar um recurso Microsoft Foundry e implantar um modelo](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) para obter seu endpoint e chave.

Cada lição de código também inclui um arquivo `README.md` onde você pode ver o código e os resultados sem rodar nada.

## Usando o Azure OpenAI Service pela primeira vez

Se esta for sua primeira vez trabalhando com o serviço Azure OpenAI, por favor siga este guia sobre como [criar e implantar um recurso do Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando a API do OpenAI pela primeira vez

Se esta for sua primeira vez trabalhando com a API do OpenAI, por favor siga o guia de como [criar e usar a interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conheça Outros Alunos

Criamos canais em nosso servidor oficial da comunidade [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para você conhecer outros alunos. Esta é uma ótima maneira de se conectar com outros empreendedores, desenvolvedores, estudantes e qualquer pessoa que queira evoluir em IA Generativa.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipe do projeto também estará neste servidor Discord para ajudar os alunos.

## Contribua

Este curso é uma iniciativa open-source. Se você perceber áreas para melhorias ou problemas, por favor crie um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou registre um [issue no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipe do projeto acompanhará todas as contribuições. Contribuir para open source é uma maneira incrível de construir sua carreira em IA Generativa.

A maioria das contribuições exige que você concorde com um Acordo de Licença de Contribuinte (CLA) declarando que você tem o direito e de fato concede os direitos para usarmos sua contribuição. Para detalhes, visite o site [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir textos neste repositório, por favor, assegure-se de não usar tradução automática. Verificaremos as traduções com a comunidade, então se ofereça para traduzir apenas idiomas nos quais você é proficiente.


Quando você enviar um pull request, um bot de CLA determinará automaticamente se você precisa fornecer um CLA e decorará o PR apropriadamente (por exemplo, etiqueta, comentário). Basta seguir as instruções fornecidas pelo bot. Você precisará fazer isso apenas uma vez em todos os repositórios que usam nosso CLA.

Este projeto adotou o [Código de Conduta de Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações, leia o FAQ do Código de Conduta ou entre em contato com [Email opencode](opencode@microsoft.com) para quaisquer perguntas ou comentários adicionais.

## Vamos Começar

Agora que você completou as etapas necessárias para concluir este curso, vamos começar com uma [introdução à IA Generativa e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->