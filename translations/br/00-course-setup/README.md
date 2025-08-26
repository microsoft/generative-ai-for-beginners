<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T16:23:13+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "br"
}
-->
# Começando com este curso

Estamos muito animados para que você comece este curso e veja o que vai se inspirar a construir com IA Generativa!

Para garantir seu sucesso, esta página apresenta os passos de configuração, requisitos técnicos e onde buscar ajuda, se necessário.

## Passos de Configuração

Para começar este curso, você precisará seguir os passos abaixo.

### 1. Faça um Fork deste Repositório

[Faça um fork deste repositório inteiro](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para sua própria conta do GitHub para poder alterar qualquer código e completar os desafios. Você também pode [dar uma estrela (🌟) neste repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrá-lo e outros repositórios relacionados mais facilmente.

### 2. Crie um codespace

Para evitar problemas de dependências ao rodar o código, recomendamos que você faça este curso em um [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

No seu fork: **Code -> Codespaces -> New on main**

![Diálogo mostrando botões para criar um codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Adicione um segredo

1. ⚙️ Ícone de engrenagem -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nomeie como OPENAI_API_KEY, cole sua chave, Salve.

### 3.  E agora?

| Quero…               | Ir para…                                                                 |
|----------------------|--------------------------------------------------------------------------|
| Começar a Lição 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Trabalhar offline    | [`setup-local.md`](02-setup-local.md)                                    |
| Configurar um Provedor LLM | [`providers.md`](providers.md)                                    |
| Conhecer outros alunos | [Entre no nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Solução de Problemas

| Sintoma                                   | Solução                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| Build do container travado > 10 min       | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`               | Terminal não conectou; clique em **+** ➜ *bash*                |
| `401 Unauthorized` do OpenAI              | `OPENAI_API_KEY` errado ou expirado                            |
| VS Code mostra “Dev container mounting…”  | Atualize a aba do navegador—às vezes o Codespaces perde conexão|
| Kernel do notebook ausente                | Menu do notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

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

4. **Salve o arquivo**: Salve as alterações e feche o editor de texto.

5. **Instale o `python-dotenv`**: Se ainda não instalou, você precisará instalar o pacote `python-dotenv` para carregar as variáveis de ambiente do arquivo `.env` na sua aplicação Python. Você pode instalar usando o `pip`:

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

Pronto! Você criou um arquivo `.env`, adicionou seu token do GitHub e o carregou na sua aplicação Python.

## Como rodar localmente no seu computador

Para rodar o código localmente no seu computador, você precisa ter alguma versão do [Python instalada](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Depois, para usar o repositório, você precisa cloná-lo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Depois de tudo baixado, você já pode começar!

## Passos Opcionais

### Instalando o Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar o [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python e alguns pacotes.
O Conda em si é um gerenciador de pacotes, que facilita a configuração e troca entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) e pacotes Python. Ele também é útil para instalar pacotes que não estão disponíveis via `pip`.

Você pode seguir o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurá-lo.

Com o Miniconda instalado, você precisa clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (caso ainda não tenha feito isso).

Depois, você precisa criar um ambiente virtual. Para fazer isso com o Conda, crie um novo arquivo de ambiente (_environment.yml_). Se estiver acompanhando pelo Codespaces, crie isso dentro do diretório `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

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

Se você encontrar erros usando o conda, pode instalar manualmente as bibliotecas de IA da Microsoft usando o comando abaixo no terminal.

```
conda install -c microsoft azure-ai-ml
```

O arquivo de ambiente especifica as dependências que precisamos. `<environment-name>` é o nome que você quer dar ao seu ambiente Conda, e `<python-version>` é a versão do Python que você quer usar, por exemplo, `3` é a versão principal mais recente do Python.

Feito isso, você pode criar seu ambiente Conda rodando os comandos abaixo no seu terminal/linha de comando

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se tiver algum problema.

### Usando o Visual Studio Code com a extensão de suporte ao Python

Recomendamos o uso do editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [extensão de suporte ao Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Porém, isso é apenas uma recomendação, não uma exigência.

> **Note**: Ao abrir o repositório do curso no VS Code, você tem a opção de configurar o projeto dentro de um container. Isso é possível por causa do [diretório especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) presente no repositório do curso. Mais sobre isso adiante.

> **Note**: Assim que você clonar e abrir o diretório no VS Code, ele vai sugerir automaticamente a instalação da extensão de suporte ao Python.

> **Note**: Se o VS Code sugerir reabrir o repositório em um container, recuse essa solicitação para usar a versão do Python instalada localmente.

### Usando o Jupyter no Navegador

Você também pode trabalhar no projeto usando o [ambiente Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direto do seu navegador. Tanto o Jupyter clássico quanto o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento agradável, com recursos como auto-completar, destaque de código, etc.

Para iniciar o Jupyter localmente, vá até o terminal/linha de comando, navegue até o diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isso vai iniciar uma instância do Jupyter e a URL para acessá-la será mostrada no terminal.

Ao acessar a URL, você verá o sumário do curso e poderá navegar para qualquer arquivo `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Rodando em um container

Uma alternativa para configurar tudo no seu computador ou Codespace é usar um [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A pasta especial `.devcontainer` dentro do repositório do curso permite que o VS Code configure o projeto dentro de um container. Fora do Codespaces, isso vai exigir a instalação do Docker e, sinceramente, envolve um pouco mais de trabalho, então recomendamos isso apenas para quem já tem experiência com containers.

Uma das melhores formas de manter suas chaves de API seguras ao usar o GitHub Codespaces é usando os Segredos do Codespace. Siga o [guia de gerenciamento de segredos do Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saber mais.

## Lições e Requisitos Técnicos

O curso possui 6 lições conceituais e 6 lições práticas de código.

Para as lições de código, estamos usando o Azure OpenAI Service. Você vai precisar de acesso ao serviço Azure OpenAI e de uma chave de API para rodar este código. Você pode solicitar acesso [preenchendo este formulário](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Enquanto aguarda o processamento do seu pedido, cada lição de código também inclui um arquivo `README.md` onde você pode ver o código e os resultados.

## Usando o Azure OpenAI Service pela primeira vez

Se esta é sua primeira vez usando o serviço Azure OpenAI, siga este guia de como [criar e implantar um recurso do Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando a API do OpenAI pela primeira vez

Se esta é sua primeira vez usando a API do OpenAI, siga o guia de como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conheça outros alunos

Criamos canais no nosso [servidor oficial do Discord da Comunidade de IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para você conhecer outros alunos. É uma ótima forma de fazer networking com outros empreendedores, desenvolvedores, estudantes e qualquer pessoa interessada em se aprofundar em IA Generativa.

[![Entrar no canal do discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipe do projeto também estará neste servidor do Discord para ajudar os alunos.

## Contribua

Este curso é uma iniciativa open-source. Se você encontrar pontos de melhoria ou problemas, por favor, crie um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou registre uma [issue no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipe do projeto irá acompanhar todas as contribuições. Contribuir com open source é uma ótima maneira de construir sua carreira em IA Generativa.

A maioria das contribuições exige que você concorde com um Contributor License Agreement (CLA), declarando que você tem o direito de, e de fato, nos conceder os direitos de uso da sua contribuição. Para mais detalhes, acesse o [site do CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir textos neste repositório, por favor, não utilize tradução automática. Vamos verificar as traduções via comunidade, então só se voluntarie para traduções em idiomas nos quais você é proficiente.

Quando você enviar um pull request, um CLA-bot irá automaticamente determinar se você precisa fornecer um CLA e marcar o PR de acordo (ex: rótulo, comentário). Basta seguir as instruções fornecidas pelo bot. Você só precisará fazer isso uma vez para todos os repositórios que usam nosso CLA.

Este projeto adotou o [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações, leia o FAQ do Código de Conduta ou entre em contato pelo [Email opencode](opencode@microsoft.com) para dúvidas ou comentários adicionais.

## Vamos Começar
Agora que você concluiu as etapas necessárias para finalizar este curso, vamos começar conhecendo uma [introdução à IA Generativa e LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.