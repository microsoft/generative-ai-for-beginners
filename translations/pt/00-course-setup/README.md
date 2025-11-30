<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T00:39:28+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pt"
}
-->
# Começar com este curso

Estamos muito entusiasmados para que inicie este curso e veja o que pode inspirar-se a criar com IA Generativa!

Para garantir o seu sucesso, esta página descreve os passos de configuração, os requisitos técnicos e onde obter ajuda, se necessário.

## Passos de Configuração

Para começar este curso, precisará de completar os seguintes passos.

### 1. Faça um Fork deste Repositório

[Fazendo um fork de todo este repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para a sua própria conta GitHub, poderá alterar qualquer código e completar os desafios. Também pode [adicionar uma estrela (🌟) a este repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrá-lo e outros repositórios relacionados mais facilmente.

### 2. Crie um Codespace

Para evitar problemas de dependência ao executar o código, recomendamos que execute este curso num [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

No seu fork: **Code -> Codespaces -> New on main**

![Diálogo mostrando botões para criar um codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Adicione um segredo

1. Ícone ⚙️ -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Nome OPENAI_API_KEY, cole a sua chave, guarde.

### 3. O que vem a seguir?

| Quero…              | Ir para…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Começar a Lição 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Trabalhar offline   | [`setup-local.md`](02-setup-local.md)                                   |
| Configurar um Provedor de LLM | [`providers.md`](03-providers.md)                                        |
| Conhecer outros alunos | [Junte-se ao nosso Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Resolução de Problemas

| Sintoma                                   | Solução                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Construção do container travada > 10 min  | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | O terminal não foi anexado; clique em **+** ➜ *bash*            |
| `401 Unauthorized` do OpenAI              | Chave `OPENAI_API_KEY` errada ou expirada                       |
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

3. **Edite o ficheiro `.env`**: Abra o ficheiro `.env` num editor de texto (por exemplo, VS Code, Notepad++ ou outro editor). Adicione a seguinte linha ao ficheiro, substituindo `your_github_token_here` pelo seu token GitHub real:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Guarde o ficheiro**: Guarde as alterações e feche o editor de texto.

5. **Instale `python-dotenv`**: Se ainda não o fez, precisará de instalar o pacote `python-dotenv` para carregar variáveis de ambiente do ficheiro `.env` na sua aplicação Python. Pode instalá-lo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carregue as variáveis de ambiente no seu script Python**: No seu script Python, use o pacote `python-dotenv` para carregar as variáveis de ambiente do ficheiro `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

E pronto! Criou com sucesso um ficheiro `.env`, adicionou o seu token GitHub e carregou-o na sua aplicação Python.

## Como executar localmente no seu computador

Para executar o código localmente no seu computador, precisará de ter alguma versão do [Python instalada](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para usar o repositório, precisará de cloná-lo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Depois de ter tudo configurado, pode começar!

## Passos Opcionais

### Instalar Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) é um instalador leve para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, bem como alguns pacotes.
O Conda é um gestor de pacotes que facilita a configuração e alternância entre diferentes [**ambientes virtuais**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) de Python e pacotes. Também é útil para instalar pacotes que não estão disponíveis via `pip`.

Pode seguir o [guia de instalação do MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurá-lo.

Com o Miniconda instalado, precisará de clonar o [repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (se ainda não o fez).

Em seguida, precisará de criar um ambiente virtual. Para fazer isso com o Conda, crie um novo ficheiro de ambiente (_environment.yml_). Se estiver a seguir o curso usando Codespaces, crie este ficheiro dentro do diretório `.devcontainer`, ou seja, `.devcontainer/environment.yml`.

Preencha o ficheiro de ambiente com o seguinte trecho:

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

Se encontrar erros ao usar o Conda, pode instalar manualmente as Bibliotecas de IA da Microsoft usando o seguinte comando num terminal.

```
conda install -c microsoft azure-ai-ml
```

O ficheiro de ambiente especifica as dependências necessárias. `<environment-name>` refere-se ao nome que gostaria de usar para o seu ambiente Conda, e `<python-version>` é a versão do Python que gostaria de usar, por exemplo, `3` é a última versão principal do Python.

Com isso feito, pode criar o seu ambiente Conda executando os comandos abaixo na linha de comando/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulte o [guia de ambientes Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) se encontrar problemas.

### Usar o Visual Studio Code com a extensão de suporte ao Python

Recomendamos usar o editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a extensão de suporte ao [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. No entanto, isto é mais uma recomendação e não um requisito obrigatório.

> **Nota**: Ao abrir o repositório do curso no VS Code, terá a opção de configurar o projeto dentro de um container. Isto é possível devido ao diretório especial [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) encontrado no repositório do curso. Mais sobre isso mais tarde.

> **Nota**: Assim que clonar e abrir o diretório no VS Code, ele sugerirá automaticamente que instale uma extensão de suporte ao Python.

> **Nota**: Se o VS Code sugerir que reabra o repositório num container, recuse esta solicitação para usar a versão localmente instalada do Python.

### Usar Jupyter no Navegador

Também pode trabalhar no projeto usando o ambiente [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) diretamente no seu navegador. Tanto o Jupyter clássico quanto o [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferecem um ambiente de desenvolvimento agradável com recursos como auto-completar, destaque de código, etc.

Para iniciar o Jupyter localmente, vá até ao terminal/linha de comando, navegue até ao diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Isto iniciará uma instância do Jupyter e o URL para acessá-lo será exibido na janela da linha de comando.

Assim que acessar o URL, deverá ver o plano do curso e poderá navegar para qualquer ficheiro `*.ipynb`. Por exemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Executar num container

Uma alternativa para configurar tudo no seu computador ou Codespace é usar um [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). A pasta especial `.devcontainer` dentro do repositório do curso torna possível para o VS Code configurar o projeto dentro de um container. Fora do Codespaces, isto exigirá a instalação do Docker e, francamente, envolve algum trabalho, por isso recomendamos esta opção apenas para quem tem experiência com containers.

Uma das melhores formas de manter as suas chaves de API seguras ao usar GitHub Codespaces é utilizando os Segredos do Codespace. Por favor, siga o [guia de gestão de segredos do Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para saber mais sobre isto.

## Lições e Requisitos Técnicos

O curso tem 6 lições de conceitos e 6 lições de codificação.

Para as lições de codificação, estamos a usar o Azure OpenAI Service. Precisará de acesso ao serviço Azure OpenAI e de uma chave de API para executar este código. Pode solicitar acesso [preenchendo esta aplicação](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Enquanto aguarda o processamento da sua aplicação, cada lição de codificação também inclui um ficheiro `README.md` onde pode visualizar o código e os resultados.

## Usar o Azure OpenAI Service pela primeira vez

Se esta for a sua primeira vez a trabalhar com o serviço Azure OpenAI, siga este guia sobre como [criar e implementar um recurso do Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usar a API OpenAI pela primeira vez

Se esta for a sua primeira vez a trabalhar com a API OpenAI, siga o guia sobre como [criar e usar a Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conheça Outros Alunos

Criámos canais no nosso servidor oficial [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para que possa conhecer outros alunos. Esta é uma ótima forma de fazer networking com outros empreendedores, criadores, estudantes e qualquer pessoa que queira evoluir na área de IA Generativa.

[![Junte-se ao canal do Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipa do projeto também estará neste servidor do Discord para ajudar os alunos.

## Contribua

Este curso é uma iniciativa de código aberto. Se identificar áreas de melhoria ou problemas, por favor crie um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou registe um [problema no GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipa do projeto estará a acompanhar todas as contribuições. Contribuir para projetos de código aberto é uma forma incrível de desenvolver a sua carreira em IA Generativa.

A maioria das contribuições requer que concorde com um Acordo de Licença de Contribuidor (CLA), declarando que tem o direito e realmente concede-nos os direitos de usar a sua contribuição. Para mais detalhes, visite o [site do Acordo de Licença de Contribuidor (CLA)](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir texto neste repositório, certifique-se de que não utiliza tradução automática. Verificaremos as traduções através da comunidade, por isso, por favor, só se ofereça para traduções em idiomas nos quais seja proficiente.

Quando submeter um pull request, um CLA-bot determinará automaticamente se precisa fornecer um CLA e decorará o PR de forma apropriada (por exemplo, etiqueta, comentário). Basta seguir as instruções fornecidas pelo bot. Só precisará fazer isso uma vez em todos os repositórios que utilizam o nosso CLA.

Este projeto adotou o [Código de Conduta de Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para mais informações, leia as FAQ do Código de Conduta ou entre em contacto com [Email opencode](opencode@microsoft.com) para quaisquer perguntas ou comentários adicionais.

## Vamos Começar
Agora que concluiu os passos necessários para completar este curso, vamos começar com uma [introdução à IA Generativa e aos LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.