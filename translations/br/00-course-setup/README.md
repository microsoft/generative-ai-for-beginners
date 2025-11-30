<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T00:45:54+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "br"
}
-->
# Começando com este curso

Estamos muito animados para que você comece este curso e veja o que você se inspira a criar com IA Generativa!

Para garantir seu sucesso, esta página descreve os passos de configuração, requisitos técnicos e onde obter ajuda, se necessário.

## Passos de Configuração

Para começar este curso, você precisará completar os seguintes passos.

### 1. Faça um Fork deste Repositório

[Fork este repositório inteiro](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para sua própria conta do GitHub para poder alterar qualquer código e completar os desafios. Você também pode [dar uma estrela (🌟) neste repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrá-lo e outros repositórios relacionados mais facilmente.

### 2. Crie um Codespace

Para evitar problemas de dependência ao executar o código, recomendamos executar este curso em um [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

No seu fork: **Code -> Codespaces -> New on main**

![Diálogo mostrando botões para criar um codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Adicione um segredo

1. ⚙️ Ícone de engrenagem -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Nomeie como OPENAI_API_KEY, cole sua chave, Salve.

### 3. O que vem a seguir?

| Eu quero...         | Vá para...                                                              |
|---------------------|-------------------------------------------------------------------------|
| Começar a Aula 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Trabalhar offline   | [`setup-local.md`](02-setup-local.md)                                   |
| Configurar um Provedor de LLM | [`providers.md`](03-providers.md)                                        |
| Conhecer outros alunos | [Junte-se ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Solução de Problemas

| Sintoma                                   | Solução                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Construção do container travada > 10 min  | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | O terminal não foi anexado; clique **+** ➜ *bash*               |
| `401 Unauthorized` do OpenAI              | `OPENAI_API_KEY` incorreta ou expirada                          |
| VS Code mostra “Dev container mounting…”  | Atualize a aba do navegador—às vezes o Codespaces perde conexão |
| Kernel do Notebook ausente                | Menu do Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Sistemas baseados em Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edite o arquivo `.env`**: Abra o arquivo `.env` em um editor de texto (por exemplo, VS Code, Notepad++ ou qualquer outro editor). Adicione a seguinte linha ao arquivo, substituindo `your_github_token_here` pelo seu token real do GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salve o Arquivo**: Salve as alterações e feche o editor de texto.

5. **Instale `python-dotenv`**: Caso ainda não tenha feito isso, você precisará instalar o pacote `python-dotenv` para carregar variáveis de ambiente do arquivo `.env` em sua aplicação Python. Você pode instalá-lo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregue as Variáveis de Ambiente no Seu Script Python**: No seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do arquivo `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Pronto! Você criou com sucesso um arquivo `.env`, adicionou seu token do GitHub e o carregou em sua aplicação Python.

## Como Executar Localmente no Seu Computador

Para executar o código localmente no seu computador, você precisará ter alguma versão do [Python instalada](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para então usar o repositório, você precisa cloná-lo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Depois de ter tudo configurado, você pode começar!

## Passos Opcionais

### Instalando o Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, bem como alguns pacotes.
Conda é um gerenciador de pacotes que facilita a configuração e troca entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) e pacotes Python. Ele também é útil para instalar pacotes que não estão disponíveis via `pip`.

Você pode seguir o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurá-lo.

Com o Miniconda instalado, você precisa clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se ainda não tiver feito isso).

Em seguida, você precisa criar um ambiente virtual. Para fazer isso com o Conda, crie um novo arquivo de ambiente (_environment.yml_). Se você estiver acompanhando usando Codespaces, crie isso dentro do diretório `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

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

Se você encontrar erros ao usar o Conda, pode instalar manualmente as Bibliotecas de IA da Microsoft usando o seguinte comando em um terminal.

```
conda install -c microsoft azure-ai-ml
```

O arquivo de ambiente especifica as dependências necessárias. `<environment-name>` refere-se ao nome que você gostaria de usar para seu ambiente Conda, e `<python-version>` é a versão do Python que você gostaria de usar, por exemplo, `3` é a versão mais recente do Python.

Com isso feito, você pode criar seu ambiente Conda executando os comandos abaixo na sua linha de comando/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se encontrar algum problema.

### Usando o Visual Studio Code com a extensão de suporte ao Python

Recomendamos usar o editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a extensão de [suporte ao Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. No entanto, isso é mais uma recomendação e não um requisito obrigatório.

> **Nota**: Ao abrir o repositório do curso no VS Code, você tem a opção de configurar o projeto dentro de um container. Isso é possível devido ao [diretório especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) encontrado no repositório do curso. Mais sobre isso depois.

> **Nota**: Assim que você clonar e abrir o diretório no VS Code, ele automaticamente sugerirá que você instale uma extensão de suporte ao Python.

> **Nota**: Se o VS Code sugerir que você reabra o repositório em um container, recuse essa solicitação para usar a versão local instalada do Python.

### Usando Jupyter no Navegador

Você também pode trabalhar no projeto usando o ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) diretamente no seu navegador. Tanto o Jupyter clássico quanto o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento bastante agradável com recursos como autocompletar, destaque de código, etc.

Para iniciar o Jupyter localmente, vá até o terminal/linha de comando, navegue até o diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isso iniciará uma instância do Jupyter e o URL para acessá-lo será exibido na janela da linha de comando.

Assim que acessar o URL, você verá o conteúdo do curso e poderá navegar para qualquer arquivo `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Executando em um container

Uma alternativa para configurar tudo no seu computador ou Codespace é usar um [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A pasta especial `.devcontainer` dentro do repositório do curso torna possível para o VS Code configurar o projeto dentro de um container. Fora do Codespaces, isso exigirá a instalação do Docker e, francamente, envolve um pouco de trabalho, então recomendamos isso apenas para aqueles com experiência em trabalhar com containers.

Uma das melhores maneiras de manter suas chaves de API seguras ao usar GitHub Codespaces é utilizando os Segredos do Codespace. Por favor, siga o [guia de gerenciamento de segredos do Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saber mais sobre isso.

## Aulas e Requisitos Técnicos

O curso possui 6 aulas conceituais e 6 aulas de codificação.

Para as aulas de codificação, estamos utilizando o Azure OpenAI Service. Você precisará de acesso ao serviço Azure OpenAI e uma chave de API para executar este código. Você pode solicitar acesso [preenchendo este formulário](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Enquanto aguarda o processamento da sua solicitação, cada aula de codificação também inclui um arquivo `README.md` onde você pode visualizar o código e os resultados.

## Usando o Azure OpenAI Service pela primeira vez

Se esta for sua primeira vez trabalhando com o serviço Azure OpenAI, siga este guia sobre como [criar e implantar um recurso do serviço Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando a API OpenAI pela primeira vez

Se esta for sua primeira vez trabalhando com a API OpenAI, siga o guia sobre como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conheça Outros Alunos

Criamos canais em nosso servidor oficial do [Discord da Comunidade de IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para conhecer outros alunos. Esta é uma ótima maneira de fazer networking com outros empreendedores, criadores, estudantes e qualquer pessoa que esteja buscando se aprimorar em IA Generativa.

[![Entre no canal do Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipe do projeto também estará neste servidor do Discord para ajudar os alunos.

## Contribua

Este curso é uma iniciativa de código aberto. Se você identificar áreas de melhoria ou problemas, por favor, crie um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou registre um [issue no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipe do projeto estará acompanhando todas as contribuições. Contribuir para código aberto é uma maneira incrível de construir sua carreira em IA Generativa.

A maioria das contribuições exige que você concorde com um Acordo de Licença de Contribuidor (CLA) declarando que você tem o direito e realmente concede a nós os direitos de usar sua contribuição. Para mais detalhes, visite o site do [Acordo de Licença de Contribuidor (CLA)](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir texto neste repositório, por favor, certifique-se de não usar tradução automática. Verificaremos as traduções por meio da comunidade, então, por favor, só se voluntarie para traduções em idiomas nos quais você seja proficiente.

Quando você enviar um pull request, um CLA-bot determinará automaticamente se você precisa fornecer um CLA e decorará o PR apropriadamente (por exemplo, etiqueta, comentário). Basta seguir as instruções fornecidas pelo bot. Você só precisará fazer isso uma vez em todos os repositórios que utilizam nosso CLA.

Este projeto adotou o [Código de Conduta de Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações, leia as Perguntas Frequentes sobre o Código de Conduta ou entre em contato com [Email opencode](opencode@microsoft.com) para quaisquer perguntas ou comentários adicionais.

## Vamos Começar
Agora que você concluiu as etapas necessárias para completar este curso, vamos começar com uma [introdução à IA Generativa e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.