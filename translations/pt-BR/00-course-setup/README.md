# Começando com este curso

Estamos muito animados para que você comece este curso e veja o que você vai se inspirar a construir com IA Generativa!

Para garantir seu sucesso, esta página descreve os passos para configuração, requisitos técnicos e onde obter ajuda, se necessário.

## Passos para Configuração

Para começar a fazer este curso, você precisará completar os seguintes passos.

### 1. Faça um fork deste repositório

[Faça um fork de todo este repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para sua própria conta do GitHub para poder alterar qualquer código e completar os desafios. Você também pode [dar uma estrela (🌟) a este repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrá-lo e encontrar repositórios relacionados com mais facilidade.

### 2. Crie um codespace

Para evitar quaisquer problemas de dependência ao executar o código, recomendamos executar este curso em um [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

No seu fork: **Code -> Codespaces -> Novo em main**

![Dialog mostrando botões para criar um codespace](../../../translated_images/pt-BR/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adicione um segredo

1. ⚙️ Ícone de engrenagem -> Paleta de Comandos -> Codespaces : Gerenciar segredo do usuário -> Adicionar um novo segredo.
2. Nomeie como OPENAI_API_KEY, cole sua chave e salve.

### 3. O que vem a seguir?

| Eu quero…           | Vá para…                                                               |
|---------------------|------------------------------------------------------------------------|
| Começar a Aula 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Trabalhar offline   | [`setup-local.md`](02-setup-local.md)                                  |
| Configurar um Provedor LLM | [`providers.md`](03-providers.md)                                  |
| Conhecer outros alunos | [Junte-se ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Solução de Problemas


| Sintoma                                   | Solução                                                      |
|-------------------------------------------|--------------------------------------------------------------|
| Construção do container travada > 10 min | **Codespaces ➜ “Reconstruir Container”**                     |
| `python: command not found`                | Terminal não anexado; clique em **+** ➜ *bash*               |
| `401 Unauthorized` do OpenAI               | `OPENAI_API_KEY` incorreto ou expirado                        |
| VS Code mostra “Dev container mounting…”  | Atualize a aba do navegador — às vezes Codespaces perde conexão |
| Kernel do notebook ausente                | Menu do notebook ➜ **Kernel ▸ Selecionar Kernel ▸ Python 3** |

   Sistemas baseados em Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edite o arquivo `.env`**: Abra o arquivo `.env` em um editor de texto (por exemplo, VS Code, Notepad++ ou outro editor). Adicione a seguinte linha ao arquivo, substituindo `your_github_token_here` pelo seu token real do GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salve o arquivo**: Salve as alterações e feche o editor de texto.

5. **Instale o `python-dotenv`**: Se ainda não instalou, você precisará instalar o pacote `python-dotenv` para carregar variáveis de ambiente do arquivo `.env` em sua aplicação Python. Você pode instalá-lo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregue as variáveis de ambiente no seu script Python**: No seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do arquivo `.env`:

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

## Como Executar localmente no seu computador

Para executar o código localmente no seu computador, você precisará ter alguma versão do [Python instalado](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Depois, para usar o repositório, você precisa cloná-lo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Quando terminar de configurar tudo, você pode começar!

## Passos Opcionais

### Instalando Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, assim como alguns pacotes.
O próprio Conda é um gerenciador de pacotes, que facilita configurar e alternar entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) do Python e pacotes. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

Você pode seguir o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurá-lo.

Com o Miniconda instalado, você precisa clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (caso ainda não tenha feito)

Depois, você precisa criar um ambiente virtual. Para isso, crie um arquivo de ambiente (_environment.yml_). Se você estiver seguindo com Codespaces, crie dentro do diretório `.devcontainer`, portanto `.devcontainer/environment.yml`.

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

Se tiver erros usando conda, você pode instalar manualmente as Bibliotecas Microsoft AI usando o comando abaixo no terminal.

```
conda install -c microsoft azure-ai-ml
```

O arquivo de ambiente especifica as dependências necessárias. `<environment-name>` se refere ao nome que você quer usar para seu ambiente Conda, e `<python-version>` é a versão do Python que deseja usar, por exemplo, `3` é a maior versão atual do Python.

Com isso feito, você pode criar seu ambiente Conda rodando os comandos abaixo na linha de comando/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # O subcaminho .devcontainer se aplica somente a configurações do Codespace
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se encontrar qualquer problema.

### Usando Visual Studio Code com a extensão de suporte a Python

Recomendamos o uso do editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [extensão de suporte a Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Porém, isso é uma recomendação e não um requisito obrigatório.

> **Nota**: Ao abrir o repositório do curso no VS Code, você tem a opção de configurar o projeto dentro de um container. Isso porque há o [diretório especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dentro do repositório do curso. Falaremos mais sobre isso depois.

> **Nota**: Assim que você clonar e abrir o diretório no VS Code, ele irá sugerir automaticamente que você instale uma extensão de suporte a Python.

> **Nota**: Caso o VS Code sugira que você reabra o repositório em um container, recuse este pedido para poder utilizar a versão localmente instalada do Python.

### Usando Jupyter no Navegador

Você também pode trabalhar no projeto usando o ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) diretamente no seu navegador. Tanto o Jupyter clássico quanto o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento bastante agradável com funcionalidades como auto-completar, destaque de código, etc.

Para iniciar o Jupyter localmente, vá até o terminal/linha de comando, navegue até o diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isso iniciará uma instância do Jupyter e a URL para acessá-la será exibida na janela do terminal.

Ao acessar a URL, você verá o roteiro do curso e poderá navegar para qualquer arquivo `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Executando em um container

Uma alternativa para configurar tudo no seu computador ou Codespace é usar um [container](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst). A pasta especial `.devcontainer` dentro do repositório do curso possibilita que o VS Code configure o projeto dentro de um container. Fora dos Codespaces, isso exigirá a instalação do Docker e, sinceramente, envolve um pouco de trabalho, então recomendamos isso apenas para quem tem experiência trabalhando com containers.

Uma das melhores maneiras de manter suas chaves API seguras ao usar GitHub Codespaces é usando os Segredos do Codespace. Por favor, siga o guia de [gerenciamento de segredos nos Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saber mais sobre isso.


## Aulas e Requisitos Técnicos

O curso tem 6 aulas conceituais e 6 aulas de codificação.

Para as aulas de codificação, estamos usando o Azure OpenAI Service. Você precisará de acesso ao serviço Azure OpenAI e uma chave API para executar este código. Você pode solicitar o acesso [preenchendo esta aplicação](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Enquanto aguarda o processamento da sua inscrição, cada aula de codificação também inclui um arquivo `README.md` onde você pode ver o código e as saídas.

## Usando o Azure OpenAI Service pela primeira vez

Se esta é sua primeira vez trabalhando com o serviço Azure OpenAI, siga este guia sobre como [criar e implantar um recurso do Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando a API OpenAI pela primeira vez

Se esta é sua primeira vez trabalhando com a API OpenAI, siga o guia sobre como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conheça outros alunos

Criamos canais em nosso servidor oficial do [Discord da Comunidade de IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para você conhecer outros alunos. Esta é uma ótima forma de fazer networking com outros empreendedores, construtores, estudantes e qualquer pessoa que queira se aprimorar em IA Generativa.

[![Entrar no canal do discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

O time do projeto também estará neste servidor Discord para ajudar qualquer aluno.

## Contribua

Este curso é uma iniciativa open-source. Se você ver áreas para melhoria ou problemas, por favor, crie um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou registre um [issue no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

O time do projeto acompanhará todas as contribuições. Contribuir com open source é uma forma incrível de construir sua carreira em IA Generativa.

A maioria das contribuições exige que você aceite um Acordo de Licença de Contribuidor (CLA) declarando que você tem o direito e realmente concede os direitos para usarmos sua contribuição. Para detalhes, visite o site do [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir texto neste repositório, certifique-se de não usar tradução automática. Verificaremos as traduções pela comunidade, então por favor, se voluntarie apenas para traduzir idiomas nos quais você é proficiente.

Quando você enviar um pull request, um bot do CLA determinará automaticamente se você precisa fornecer um CLA e decorará o PR adequadamente (por exemplo, etiqueta, comentário). Apenas siga as instruções fornecidas pelo bot. Você só precisará fazer isso uma vez para todos os repositórios que usam nosso CLA.

Este projeto adotou o [Código de Conduta Open Source da Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações, leia o FAQ do Código de Conduta ou entre em contato pelo [Email opencode](opencode@microsoft.com) para qualquer dúvida ou comentário adicional.

## Vamos Começar
Agora que você completou as etapas necessárias para concluir este curso, vamos começar com uma [introdução à IA Generativa e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->