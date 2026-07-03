# Começar com este curso

Estamos muito entusiasmados por começar este curso consigo e ver com o que se vai inspirar para criar com a IA Generativa!

Para garantir o seu sucesso, esta página descreve os passos de configuração, requisitos técnicos e onde obter ajuda se necessário.

## Passos de Configuração

Para começar a fazer este curso, terá de completar os seguintes passos.

### 1. Fazer fork deste repositório

[Fazer fork de todo este repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para a sua própria conta GitHub para poder alterar qualquer código e completar os desafios. Pode também [favoritar (🌟) este repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para o encontrar e encontrar repositórios relacionados mais facilmente.

### 2. Criar um codespace

Para evitar problemas de dependências ao executar o código, recomendamos executar este curso num [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

No seu fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/pt-PT/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adicionar um segredo

1. ⚙️ Ícone de engrenagem -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Nomear OPENAI_API_KEY, colar a sua chave, Guardar.

### 3.  E agora?

| Quero…              | Ir para…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Começar a Lição 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Trabalhar offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Configurar um Provedor LLM | [`providers.md`](03-providers.md)                                        |
| Conhecer outros aprendizes | [Juntar-se ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Resolução de Problemas


| Sintoma                                   | Solução                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Construção do container bloqueada > 10 min | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal não foi conectado; clicar em **+** ➜ *bash*            |
| `401 Unauthorized` do OpenAI              | `OPENAI_API_KEY` errada / expirou                               |
| VS Code mostra “Dev container mounting…” | Atualize a aba do navegador — por vezes o Codespaces perde ligação |
| Kernel do notebook em falta                | Menu do notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Sistemas Unix-based:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Editar o Ficheiro `.env`**: Abra o ficheiro `.env` num editor de texto (ex: VS Code, Notepad++ ou outro editor). Adicione a seguinte linha ao ficheiro, substituindo `your_github_token_here` pelo seu token GitHub real:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Guardar o Ficheiro**: Guarde as alterações e feche o editor de texto.

5. **Instalar `python-dotenv`**: Se ainda não o fez, terá de instalar o pacote `python-dotenv` para carregar variáveis de ambiente do ficheiro `.env` para a aplicação Python. Pode instalar isso usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregar Variáveis de Ambiente no seu Script Python**: No seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do ficheiro `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Carregar variáveis de ambiente a partir do ficheiro .env
   load_dotenv()

   # Aceder à variável GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Está feito! Criou com sucesso um ficheiro `.env`, adicionou o seu token GitHub, e carregou-o na sua aplicação Python.

## Como executar localmente no seu computador

Para executar o código localmente no seu computador, precisa de ter alguma versão do [Python instalado](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para depois usar o repositório, tem de o clonar:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Depois de fazer o checkout de tudo, pode começar!

## Passos Opcionais

### Instalar Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, assim como alguns pacotes.
O Conda em si é um gestor de pacotes que facilita a configuração e a troca entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) de Python e pacotes. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

Pode seguir o [guia de instalação MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurá-lo.

Com o Miniconda instalado, precisa de clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se ainda não o fez).

De seguida, precisa de criar um ambiente virtual. Para isso com Conda, crie um novo ficheiro de ambiente (_environment.yml_). Se está a seguir usando Codespaces, crie-o dentro do diretório `.devcontainer`, assim `.devcontainer/environment.yml`.

Preencha o seu ficheiro de ambiente com o trecho abaixo:

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

Se encontrar erros ao usar conda pode instalar manualmente as Bibliotecas AI da Microsoft usando o seguinte comando no terminal.

```
conda install -c microsoft azure-ai-ml
```

O arquivo de ambiente especifica as dependências necessárias. `<environment-name>` refere-se ao nome que deseja usar para o seu ambiente Conda, e `<python-version>` é a versão do Python que deseja usar, por exemplo, `3` é a versão principal mais recente do Python.

Com isso, pode criar o seu ambiente Conda executando os comandos abaixo na linha de comando/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # O subcaminho .devcontainer aplica-se apenas a configurações Codespace
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) caso encontre algum problema.

### Usar o Visual Studio Code com a extensão de suporte Python

Recomendamos o uso do editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [extensão de suporte Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Contudo, isto é mais uma recomendação do que um requisito obrigatório.

> **Nota**: Ao abrir o repositório do curso no VS Code, tem a opção de configurar o projeto dentro de um contêiner. Isto deve-se ao [diretório especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) encontrado no repositório do curso. Falaremos mais sobre isso posteriormente.

> **Nota**: Depois de clonar e abrir o diretório no VS Code, este irá sugerir automaticamente que instale a extensão de suporte Python.

> **Nota**: Se o VS Code sugerir que reabra o repositório dentro de um contêiner, recuse este pedido para usar a versão de Python instalada localmente.

### Usar o Jupyter no navegador

Também pode trabalhar no projeto usando o ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direto no seu navegador. Tanto o Jupyter clássico como o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento agradável com funcionalidades como preenchimento automático, realce de código, etc.

Para iniciar o Jupyter localmente, abra o terminal/linha de comando, navegue até ao diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isto inicia uma instância do Jupyter e a URL para aceder vai aparecer na janela da linha de comando.

Quando aceder à URL, deverá ver o índice do curso e poderá navegar para qualquer ficheiro `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Executar num contêiner

Uma alternativa para configurar tudo no seu computador ou Codespace é usar um [contêiner](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst). A pasta especial `.devcontainer` dentro do repositório do curso permite que o VS Code configure o projeto dentro de um contêiner. Fora dos Codespaces, isto requer a instalação do Docker e, francamente, envolve algum trabalho, por isso recomendamos isto apenas para quem tenha experiência prévia a trabalhar com contêineres.

Uma das melhores formas de manter as suas chaves API seguras ao usar GitHub Codespaces é utilizando os Segredos do Codespace. Por favor, siga o guia [Gestão de segredos dos Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saber mais.

## Lições e Requisitos Técnicos

O curso tem 6 lições conceituais e 6 lições de codificação.

Para as lições de codificação, usamos o Azure OpenAI Service. Vai precisar de acesso ao serviço Azure OpenAI e de uma chave de API para executar este código. Pode candidatar-se para obter acesso [completando esta aplicação](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Enquanto espera que a sua candidatura seja processada, cada lição de codificação inclui também um ficheiro `README.md` onde pode ver o código e os resultados.

## Usar o Azure OpenAI Service pela primeira vez

Se for a sua primeira vez a trabalhar com o serviço Azure OpenAI, por favor siga este guia sobre como [criar e implementar um recurso Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usar a API OpenAI pela primeira vez

Se for a sua primeira vez a trabalhar com a API OpenAI, por favor siga o guia sobre como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conhecer Outros Aprendizes

Criámos canais no nosso servidor oficial do [Discord da Comunidade de IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para conhecer outros aprendizes. Esta é uma ótima forma de fazer networking com outros empreendedores, construtores, estudantes e qualquer pessoa que queira evoluir em IA Generativa.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipa do projeto também estará neste servidor Discord para ajudar os aprendizes.

## Contribuir

Este curso é uma iniciativa open-source. Se encontrar áreas para melhorar ou problemas, por favor crie um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou registe uma [issue no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipa do projeto irá acompanhar todas as contribuições. Contribuir para open source é uma forma incrível de construir a sua carreira em IA Generativa.

A maioria das contribuições requer que concorde com um Acordo de Licença de Contribuidor (CLA) declarando que tem o direito de e efetivamente nos concede os direitos para usar a sua contribuição. Para detalhes, visite o [site CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir texto neste repositório, por favor assegure-se de não usar tradução automática. Vamos verificar as traduções através da comunidade, por isso ofereça-se apenas para traduções nas línguas em que seja proficiente.

Ao submeter um pull request, um CLA-bot determina automaticamente se precisa de fornecer um CLA e decora o PR adequadamente (ex: etiqueta, comentário). Basta seguir as instruções dadas pelo bot. Só precisará de fazer isto uma vez em todos os repositórios que usam o nosso CLA.

Este projeto adotou o [Código de Conduta Open Source da Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações leia as perguntas frequentes sobre o Código de Conduta ou contacte [Email opencode](opencode@microsoft.com) com quaisquer dúvidas ou comentários adicionais.

## Vamos Começar
Agora que concluiu os passos necessários para completar este curso, vamos começar com uma [introdução à IA Generativa e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte oficial. Para informação crítica, recomenda-se a tradução profissional por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->