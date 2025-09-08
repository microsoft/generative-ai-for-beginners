<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T16:14:14+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pt"
}
-->
# Começar este curso

Estamos muito entusiasmados por te veres a começar este curso e descobrir o que te vais inspirar a criar com IA Generativa!

Para garantir o teu sucesso, esta página apresenta os passos de configuração, os requisitos técnicos e onde podes pedir ajuda, caso precises.

## Passos de Configuração

Para começares este curso, precisas de completar os seguintes passos.

### 1. Faz um fork deste repositório

[Faz fork deste repositório completo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para a tua conta do GitHub para poderes alterar o código e completar os desafios. Podes também [adicionar uma estrela (🌟) a este repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para o encontrares mais facilmente, assim como outros repositórios relacionados.

### 2. Cria um codespace

Para evitar problemas de dependências ao correr o código, recomendamos que utilizes um [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) para este curso.

No teu fork: **Code -> Codespaces -> New on main**

![Diálogo a mostrar botões para criar um codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Adiciona um segredo

1. ⚙️ Ícone de engrenagem -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nomeia como OPENAI_API_KEY, cola a tua chave, e guarda.

### 3.  O que se segue?

| Quero…               | Ir para…                                                                 |
|----------------------|--------------------------------------------------------------------------|
| Começar a Lição 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Trabalhar offline    | [`setup-local.md`](02-setup-local.md)                                    |
| Configurar um fornecedor LLM | [`providers.md`](providers.md)                                   |
| Conhecer outros alunos | [Junta-te ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Resolução de Problemas

| Sintoma                                   | Solução                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Construção do container bloqueada > 10 min| **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | O terminal não foi ligado; clica em **+** ➜ *bash*              |
| `401 Unauthorized` do OpenAI              | `OPENAI_API_KEY` errado ou expirado                             |
| VS Code mostra “Dev container mounting…”  | Atualiza o separador do browser—o Codespaces por vezes perde ligação |
| Kernel do notebook em falta               | Menu do notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Sistemas baseados em Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edita o ficheiro `.env`**: Abre o ficheiro `.env` num editor de texto (por exemplo, VS Code, Notepad++ ou outro). Adiciona a seguinte linha ao ficheiro, substituindo `your_github_token_here` pelo teu token do GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Guarda o ficheiro**: Guarda as alterações e fecha o editor de texto.

5. **Instala o `python-dotenv`**: Se ainda não o fizeste, precisas de instalar o pacote `python-dotenv` para carregar as variáveis de ambiente do ficheiro `.env` para a tua aplicação Python. Podes instalá-lo com o `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carrega as variáveis de ambiente no teu script Python**: No teu script Python, usa o pacote `python-dotenv` para carregar as variáveis de ambiente do ficheiro `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

E está feito! Criaste com sucesso um ficheiro `.env`, adicionaste o teu token do GitHub e carregaste-o na tua aplicação Python.

## Como correr localmente no teu computador

Para correr o código localmente no teu computador, precisas de ter alguma versão do [Python instalada](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Depois, para usares o repositório, precisas de o clonar:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Assim que tiveres tudo pronto, já podes começar!

## Passos Opcionais

### Instalar o Miniconda

O [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar o [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python e alguns pacotes.
O Conda é um gestor de pacotes que facilita a configuração e troca entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) de Python e pacotes. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

Podes seguir o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para o configurar.

Com o Miniconda instalado, precisas de clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (caso ainda não o tenhas feito).

De seguida, precisas de criar um ambiente virtual. Para isso, com o Conda, cria um novo ficheiro de ambiente (_environment.yml_). Se estiveres a seguir os passos usando Codespaces, cria-o dentro da diretoria `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

Preenche o teu ficheiro de ambiente com o seguinte excerto:

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

Se tiveres erros ao usar o conda, podes instalar manualmente as Microsoft AI Libraries com o seguinte comando no terminal.

```
conda install -c microsoft azure-ai-ml
```

O ficheiro de ambiente especifica as dependências necessárias. `<environment-name>` é o nome que queres dar ao teu ambiente Conda, e `<python-version>` é a versão do Python que queres usar, por exemplo, `3` é a versão principal mais recente do Python.

Depois disto, podes criar o teu ambiente Conda executando os comandos abaixo na linha de comandos/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulta o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se tiveres algum problema.

### Usar o Visual Studio Code com a extensão de suporte a Python

Recomendamos o uso do editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [extensão de suporte a Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. No entanto, isto é apenas uma recomendação e não um requisito obrigatório.

> **Nota**: Ao abrires o repositório do curso no VS Code, tens a opção de configurar o projeto dentro de um container. Isto é possível devido à [diretoria especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) que existe no repositório do curso. Mais sobre isto à frente.

> **Nota**: Assim que clonares e abrires a diretoria no VS Code, será sugerida automaticamente a instalação da extensão de suporte a Python.

> **Nota**: Se o VS Code sugerir reabrir o repositório num container, recusa para usares a versão de Python instalada localmente.

### Usar o Jupyter no browser

Também podes trabalhar no projeto usando o [ambiente Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) diretamente no teu browser. Tanto o Jupyter clássico como o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento agradável, com funcionalidades como auto-completar, realce de código, etc.

Para iniciar o Jupyter localmente, abre o terminal/linha de comandos, navega até à diretoria do curso e executa:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isto irá iniciar uma instância do Jupyter e o URL para aceder será mostrado na janela da linha de comandos.

Depois de acederes ao URL, deves ver a estrutura do curso e poder navegar para qualquer ficheiro `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Correr num container

Uma alternativa a configurar tudo no teu computador ou Codespace é usar um [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A pasta especial `.devcontainer` no repositório do curso permite ao VS Code configurar o projeto dentro de um container. Fora do Codespaces, isto requer a instalação do Docker e, para ser honesto, envolve algum trabalho, por isso recomendamos apenas para quem já tem experiência com containers.

Uma das melhores formas de manter as tuas chaves de API seguras ao usar GitHub Codespaces é através dos Codespace Secrets. Consulta o guia de [gestão de segredos do Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saberes mais.

## Lições e Requisitos Técnicos

O curso tem 6 lições de conceitos e 6 lições de programação.

Para as lições de programação, estamos a usar o Azure OpenAI Service. Vais precisar de acesso ao serviço Azure OpenAI e de uma chave API para correr este código. Podes pedir acesso [preenchendo este formulário](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Enquanto esperas que o teu pedido seja processado, cada lição de programação inclui também um ficheiro `README.md` onde podes ver o código e os resultados.

## Usar o Azure OpenAI Service pela primeira vez

Se é a tua primeira vez a trabalhar com o serviço Azure OpenAI, segue este guia sobre como [criar e implementar um recurso Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usar a API do OpenAI pela primeira vez

Se é a tua primeira vez a trabalhar com a API do OpenAI, segue o guia sobre como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conhece outros alunos

Criámos canais no nosso [servidor oficial de Discord da Comunidade de IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para conheceres outros alunos. É uma ótima forma de fazer networking com outros empreendedores, criadores, estudantes e qualquer pessoa interessada em evoluir na área da IA Generativa.

[![Junta-te ao canal do discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipa do projeto também estará neste servidor Discord para ajudar os alunos.

## Contribuir

Este curso é uma iniciativa open-source. Se vires áreas a melhorar ou problemas, cria um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou regista um [issue no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipa do projeto irá acompanhar todas as contribuições. Contribuir para open source é uma excelente forma de desenvolver a tua carreira em IA Generativa.

A maioria das contribuições requer que concordes com um Contributor License Agreement (CLA), declarando que tens o direito de, e de facto, nos conceder os direitos de usar a tua contribuição. Para mais detalhes, visita o [site do CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir texto neste repositório, certifica-te de que não usas tradução automática. Vamos verificar as traduções através da comunidade, por isso só te voluntaria para traduções em línguas que dominas.

Quando submeteres um pull request, um CLA-bot irá determinar automaticamente se precisas de fornecer um CLA e irá marcar o PR em conformidade (por exemplo, etiqueta, comentário). Basta seguires as instruções fornecidas pelo bot. Só precisas de fazer isto uma vez em todos os repositórios que usam o nosso CLA.

Este projeto adoptou o [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações lê o FAQ do Código de Conduta ou contacta [Email opencode](opencode@microsoft.com) para questões ou comentários adicionais.

## Vamos Começar
Agora que já concluíste os passos necessários para terminar este curso, vamos começar com uma [introdução à IA Generativa e aos LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.