# Iniciar com este curso

Estamos muito entusiasmados por começar este curso e ver com o que se inspira para criar com IA Generativa!

Para garantir o seu sucesso, esta página descreve os passos de configuração, os requisitos técnicos e onde obter ajuda se necessário.

## Passos de Configuração

Para começar a fazer este curso, deverá completar os seguintes passos.

### 1. Faça fork deste repositório

[Faça fork deste repositório completo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para a sua própria conta GitHub para poder alterar qualquer código e completar os desafios. Pode também [colocar uma estrela (🌟) neste repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para o encontrar mais facilmente e os repositórios relacionados.

### 2. Crie um codespace

Para evitar problemas com dependências ao executar o código, recomendamos correr este curso num [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

No seu fork: **Code -> Codespaces -> New on main**

![Diálogo a mostrar botões para criar um codespace](../../../translated_images/pt-PT/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adicione um segredo

1. ⚙️ Ícone de engrenagem -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nomeie OPENAI_API_KEY, cole a sua chave, Guarde.

### 3. O que fazer a seguir?

| Quero…             | Ir para…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Começar a Aula 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Trabalhar offline  | [`setup-local.md`](02-setup-local.md)                                   |
| Configurar um fornecedor LLM | [`providers.md`](03-providers.md)                                        |
| Conhecer outros alunos | [Junte-se ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Resolução de Problemas


| Sintoma                                  | Solução                                                        |
|-----------------------------------------|-----------------------------------------------------------------|
| Construção do container travada > 10 min | **Codespaces ➜ “Rebuild Container”**                          |
| `python: command not found`              | Terminal não se conectou; clique em **+** ➜ *bash*            |
| `401 Unauthorized` da OpenAI             | `OPENAI_API_KEY` errada / expirada                             |
| VS Code mostra “Dev container mounting…” | Atualize a aba do browser — às vezes o Codespaces perde conexão |
| Kernel do notebook em falta              | Menu do notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**      |

   Sistemas baseados em Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Editar o ficheiro `.env`**: Abra o ficheiro `.env` num editor de texto (ex., VS Code, Notepad++, ou outro editor). Adicione as seguintes linhas ao ficheiro, substituindo os espaços reservados pelo seu endpoint real e pela chave dos Microsoft Foundry Models (veja [`providers.md`](03-providers.md) para saber como obter estes dados):

   > **Nota:** Os GitHub Models (e a sua variável `GITHUB_TOKEN`) serão descontinuados no final de julho de 2026. Utilize em vez disso os [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Guarde o Ficheiro**: Guarde as alterações e feche o editor de texto.

5. **Instale o `python-dotenv`**: Se ainda não o fez, precisa de instalar o pacote `python-dotenv` para carregar variáveis de ambiente do ficheiro `.env` para a sua aplicação Python. Pode instalá-lo usando o `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregar Variáveis de Ambiente no seu Script Python**: No seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do ficheiro `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Carregar variáveis de ambiente a partir do ficheiro .env
   load_dotenv()

   # Aceder às variáveis dos Modelos Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Está feito! Criou com sucesso o ficheiro `.env`, adicionou as credenciais dos Microsoft Foundry Models e carregou-as na sua aplicação Python.

## Como executar localmente no seu computador

Para executar o código localmente no seu computador, precisa de ter alguma versão do [Python instalado](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para usar o repositório, precisa de o clonar:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Assim que tiver tudo configurado, pode começar!

## Passos Opcionais

### Instalar Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar o [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, assim como alguns pacotes.
O Conda é um gestor de pacotes que facilita configurar e alternar entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python e pacotes. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

Pode seguir o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurá-lo.

Com o Miniconda instalado, precisa de clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (caso ainda não o tenha feito)

De seguida, precisa de criar um ambiente virtual. Para fazer isto com Conda, crie um novo ficheiro de ambiente (_environment.yml_). Se estiver a usar Codespaces, crie este ficheiro dentro do diretório `.devcontainer`, isto é, `.devcontainer/environment.yml`.

Crie o seu ficheiro de ambiente com o snippet abaixo:

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

Se encontrar erros com conda, pode instalar manualmente as Bibliotecas Microsoft AI usando o seguinte comando num terminal.

```
conda install -c microsoft azure-ai-ml
```

O ficheiro de ambiente especifica as dependências necessárias. `<environment-name>` é o nome que deseja usar para o seu ambiente Conda, e `<python-version>` é a versão do Python que quer usar, por exemplo, `3` é a última versão principal do Python.

Com isso feito, pode criar o seu ambiente Conda executando os comandos abaixo no terminal ou linha de comando

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # o subcaminho .devcontainer aplica-se apenas a configurações de Codespace
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se tiver algum problema.

### Usar o Visual Studio Code com a extensão de suporte a Python

Recomendamos usar o editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [extensão de suporte a Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Isto é, no entanto, uma recomendação e não um requisito obrigatório

> **Nota**: Ao abrir o repositório do curso no VS Code, tem a opção de configurar o projeto dentro de um contentor. Isto é possível devido à existência do diretório [especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) encontrado no repositório do curso. Mais sobre isto mais tarde.

> **Nota**: Assim que clonar e abrir o diretório no VS Code, ele sugerirá automaticamente que instale uma extensão de suporte a Python.

> **Nota**: Se o VS Code sugerir que reabra o repositório num contentor, recuse este pedido para usar a versão local do Python instalada.

### Usar Jupyter no Browser

Também pode trabalhar no projeto usando o [ambiente Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) diretamente no seu browser. Tanto o Jupyter clássico como o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento bastante agradável com funcionalidades como auto-completar, realce de código, etc.

Para iniciar o Jupyter localmente, abra o terminal/linha de comando, navegue até ao diretório do curso, e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isto irá iniciar uma instância Jupyter e a URL para aceder será mostrada na janela da linha de comandos.

Quando aceder à URL, deverá ver o plano do curso e conseguir navegar para qualquer ficheiro `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Executar num contentor

Uma alternativa a configurar tudo no seu computador ou Codespace é usar um [contentor](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A pasta especial `.devcontainer` dentro do repositório do curso permite ao VS Code configurar o projeto dentro de um contentor. Fora dos Codespaces, isto irá requerer a instalação do Docker e, francamente, envolve algum trabalho, pelo que recomendámos isto apenas a quem tenha experiência a trabalhar com contentores.

Uma das melhores formas de manter as suas chaves API seguras ao usar GitHub Codespaces é através dos Segredos dos Codespaces. Por favor siga o guia de [gestão de segredos nos Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saber mais sobre isto.


## Aulas e Requisitos Técnicos

O curso tem 6 aulas conceptuais e 6 aulas de programação.

Para as aulas de programação, usamos o Azure OpenAI Service. Será necessário ter acesso ao serviço Azure OpenAI e uma chave API para correr este código. Pode candidatar-se para obter acesso [completando esta aplicação](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Enquanto espera que a sua candidatura seja processada, cada aula de programação inclui também um ficheiro `README.md` onde poderá ver o código e os resultados.

## Usar o Azure OpenAI Service pela primeira vez

Se é a primeira vez que trabalha com o Azure OpenAI Service, siga este guia sobre como [criar e implementar um recurso Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usar a API OpenAI pela primeira vez

Se é a primeira vez que trabalha com a API OpenAI, siga o guia sobre como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conhecer Outros Alunos

Criámos canais no nosso servidor oficial [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para que possa conhecer outros alunos. Esta é uma ótima forma de fazer networking com outros empreendedores, construtores, estudantes, e qualquer pessoa que queira evoluir em IA Generativa.

[![Juntar-se ao canal discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipa do projeto também estará neste servidor Discord para ajudar quaisquer alunos.

## Contribuir

Este curso é uma iniciativa open-source. Se encontrar áreas para melhorar ou problemas, por favor crie um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou registe um [problema GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipa do projeto irá acompanhar todas as contribuições. Contribuir para open source é uma forma incrível de construir a sua carreira em IA Generativa.

A maioria das contribuições exige que aceite um Contrato de Licença do Contribuidor (CLA) declarando que tem o direito e efetivamente concede os direitos para usarmos a sua contribuição. Para mais detalhes, visite [site do CLA, Contrato de Licença do Contribuidor](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir texto neste repositório, por favor assegure-se que não usa tradução automática. Vamos verificar as traduções através da comunidade, pelo que por favor só se voluntarie para traduções em línguas nas quais tem proficiência.

Quando submeter um pull request, um bot CLA determinará automaticamente se precisa fornecer um CLA e etiquetará o PR apropriadamente (ex., etiqueta, comentário). Basta seguir as instruções do bot. Só precisará de o fazer uma vez em todos os repositórios que usem o nosso CLA.


Este projeto adotou o [Código de Conduta de Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações, leia as Perguntas Frequentes sobre o Código de Conduta ou contacte [Email opencode](opencode@microsoft.com) para quaisquer questões ou comentários adicionais.

## Vamos Começar

Agora que completou os passos necessários para concluir este curso, vamos começar com uma [introdução à IA Generativa e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->