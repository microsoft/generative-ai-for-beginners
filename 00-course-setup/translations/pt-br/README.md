# Iniciando com este curso

Estamos muito animados por você iniciar este curso e ver que se inspira em criar aplicações com IA Generativa!

Para tornar o seu tempo bem-sucedido(a), criamos esta página que descreve as etapas de configuração, requisitos técnicos e como obter ajuda quando precisar.

## Etapas de Configuração

Para começar este curso, você precisará concluir as seguintes etapas.

### 1. Faça um Fork deste Repositório

[Faça um fork deste repositório](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) para a sua própria conta no GitHub para que possa alterar qualquer código e concluir os desafios. Você também pode [marcar com uma (🌟) este repositório](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrar com mais facilidade esse repositório.

### 2. Crie um Codespaces

Para evitar problemas de dependência ao executar o código, recomendamos a execução deste curso em um Codespaces do GitHub.

Isso pode ser criado selecionando a opção `Code` na sua versão `birfucada` deste repositório e selecionando a opção **Codespaces**.

### 3. Armazenando Suas Chaves da API

Manter suas chaves da API seguras e protegidas é importante quando você cria qualquer tipo de aplicação. Recomendamos que você não armazene suas chaves da API diretamente no código com o qual está trabalhando. Pois a inclusão dessas informações num repositório público pode resultar em custos indesejados e problemas a você.

![Dialog showing buttons to create a codespace](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

## Como Executar Localmente no seu Computador

Para executar o código localmente no seu computador, você precisará ter alguma versão do [Python instalada](https://www.python.org/downloads?WT.mc_id=academic-105485-koreyst).

Para utilizar o repositório, você precisará clonar primeiramente:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Agora, você tem tudo configurado e pode começar a aprender e trabalhar com o código.

### Instalando o miniconda (etapa opcional)

Existem vantagens em instalar o **[miniconda](https://conda.io/en/latest/miniconda.html)** - que é uma instalação bastante leve que suporta o gerenciador de pacotes `conda` para diferentes **ambientes virtuais** do Python. O `conda` facilita a instalação e alternância entre diferentes versões e pacotes do Python e também a instalação de pacotes que não estão disponíveis via `pip`.

Depois de instalar o miniconda, você precisará clonar o repositório (se ainda não o fez) e criar um ambiente virtual a ser usado neste curso:

Antes de executar a etapa abaixo, tenha certeza de que você já possui um arquivo *environment.yml*. O arquivo *environment.yml* é usado para criar um ambiente conda com as dependências necessárias e que pode se parecer com isto:

```yml
name: <environment-name>
channels:  
 - defaults
dependencies:  
- python=<python-version>  
- openai  
- python-dotenv
```

Você pode substituir `<environment-name>` pelo nome do seu ambiente conda e `<python-version>` pela versão do Python que você deseja usar. Coloque o arquivo *environment.yml* criado na pasta *.devcontainer* do seu repositório.

Agora que você criou um arquivo *environment.yml*, você pode criar um ambiente conda com o seguinte comando:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

Se você tiver problemas, consulte este link sobre a criação de [ambientes conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Usando o Visual Studio Code com a Extensão do Python

Provavelmente a melhor maneira de usar o currículo é abrindo no [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst).

> **Observação**: Uma vez que você clonar e abrir o diretório no VS Code, ele automaticamente vai sugerir que você instale as extensões do Python. Você também precisará instalar o `Miniconda` conforme descrito acima.

> **Observação**: Se o VS Code sugerir que você reabra o repositório em um container, você precisará recusar isso para usar a instalação local do Python. 

### Usando o Jupyter no Navegador

Você também pode usar o ambiente Jupyter diretamente do navegador em seu próprio computador. Na verdade, tanto o Jupyter clássico quanto o Jupyter Hub proporcionam um ambiente de desenvolvimento bastante conveniente com autocompletamento, destaque de código, etc.

Para iniciar o Jupyter localmente, vá para o diretório do curso e execute:

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Você pode navegar para qualquer um dos arquivos `.ipynb`, abre esses arquivos e comece a trabalhar.

### Executando em um Contêiner

Uma alternativa à instalação do Python seria executar o código em um contêiner. Como nosso repositório contém uma pasta especial chamada `.devcontainer`, que instrui como criar um contêiner para este repositório, o VS Code oferecerá a opção de reabrir o código em um contêiner. Isso requer a instalação do Docker e é mais complexo. Assim sendo, recomendado para usuários mais experientes.

Uma das melhores maneiras de manter suas chaves da API seguras ao usar GitHub Codespaces é usando `Codespace Secrets`. Siga este guia sobre como [gerenciar segredos para seus Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Lições e Requisitos Técnicos

O curso possui 6 lições conceituais e 6 lições incluem codificações.

Para as lições de codificação, estamos usando o Serviço Azure OpenAI. Você precisará de acesso ao serviço do Azure OpenAI e de uma chave de API para executar o código. Você pode solicitar acesso ao [completar esta aplicação](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOFA5Qk1UWDRBMjg0WFhPMkIzTzhKQ1dWNyQlQCN0PWcu&culture=en-us&country=us?WT.mc_id=academic-105485-koreyst).

Enquanto aguarda o processamento da sua inscrição, cada lição que tenha codificação também inclui um arquivo `README.md` onde você pode visualizar o código e as suas respectivas saídas.

## Usando o Serviço Azure OpenAI pela Primeira Vez

Se esta for a primeira vez que você está trabalhando com o serviço Azure OpenAI, siga este guia sobre como [criar e implantar um recurso do Serviço Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## Conheça Outros Aprendizes

Criamos canais em nosso servidor oficial da [Comunidade de Inteligência Artificial no Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para que você possa conhecer outros aprendizes. Esta é uma ótima maneira de se conectar com outros empreendedores, pessoas desenvolvedoras, estudantes e qualquer pessoa que queira se aprofundar sobre Inteligência Artificial Generativa.

[![Participe do canal no Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

A equipe do projeto também estará presente neste servidor do Discord para ajudar à todos(as).

## Contribua

Este curso é uma iniciativa de Código Aberto. Se você identificar áreas de melhoria ou problemas, por favor crie um [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou registre uma [issue no Github](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

A equipe do projeto acompanhará todas as contribuições. Sem contar que, contribuir para o código aberto é uma maneira incrível de construir sua carreira em Inteligência Artificial Generativa.

A maioria das contribuições requer que você concorde com um Contrato de Licença de Contribuidor (CLA) declarando que você tem o direito e realmente nos concede os direitos de usar sua contribuição. Para mais detalhes, visite o site do [CLA, Contrato de Licença de Contribuidor](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: ao traduzir texto neste repositório, certifique-se de não utilizar tradução automática. Verificaremos as traduções por meio da comunidade. Portanto, se ofereça voluntariamente para traduzir apenas em idiomas nos quais você seja proficiente.

Quando você for enviar um Pull Request, um robô CLA automaticamente determinará se você precisa fornecer um CLA e decorará o PR adequadamente (por exemplo, etiqueta, comentário). Basta seguir as instruções fornecidas pelo robô. Você só precisará fazer isso uma vez em todos os repositórios que utilizam nosso CLA.

Este projeto adotou o Código de Conduta de Código Aberto da Microsoft. Para obter mais informações, leia o FAQ do Código de Conduta ou entre em contato com [Email opencode](opencode@microsoft.com) com quaisquer perguntas ou comentários adicionais.

## Vamos Começar?

Agora que você concluiu as etapas necessárias para concluir este curso, vamos começar com a lição [Introdução à Inteligência Artificial Generativa e Grandes Modelos de Linguagens (LLMs)](../../../01-introduction-to-genai/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst).

