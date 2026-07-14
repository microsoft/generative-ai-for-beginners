# Construindo Aplicações de IA Low Code

[![Construindo Aplicações de IA Low Code](../../../translated_images/pt-BR/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_

## Introdução

Agora que aprendemos a construir aplicações geradoras de imagens, vamos falar sobre low code. IA generativa pode ser usada em várias áreas diferentes, incluindo low code, mas o que é low code e como podemos adicionar IA a ele?

Construir aplicativos e soluções tornou-se mais fácil tanto para desenvolvedores tradicionais quanto para não desenvolvedores através do uso das Plataformas de Desenvolvimento Low Code. Plataformas de Desenvolvimento Low Code permitem que você crie aplicativos e soluções com pouco ou nenhum código. Isto é alcançado fornecendo um ambiente de desenvolvimento visual que permite arrastar e soltar componentes para construir aplicativos e soluções. Isso possibilita construir aplicativos e soluções mais rápido e com menos recursos. Nesta lição, mergulharemos profundamente em como usar Low Code e como aprimorar o desenvolvimento low code com IA usando Power Platform.

A Power Platform oferece às organizações a oportunidade de capacitar suas equipes para construir suas próprias soluções através de um ambiente intuitivo low-code ou no-code. Este ambiente ajuda a simplificar o processo de construção de soluções. Com Power Platform, as soluções podem ser construídas em dias ou semanas em vez de meses ou anos. A Power Platform consiste em cinco produtos principais: Power Apps, Power Automate, Power BI, Power Pages e Copilot Studio.

Esta lição aborda:

- Introdução à IA Generativa na Power Platform
- Introdução ao Copilot e como usá-lo
- Usando IA Generativa para construir apps e fluxos na Power Platform
- Entendendo os Modelos de IA na Power Platform com AI Builder
- Construindo agentes inteligentes com Microsoft Copilot Studio

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Entender como o Copilot funciona na Power Platform.

- Construir um App de Rastreamento de Tarefas dos Estudantes para nossa startup educacional.

- Construir um Fluxo de Processamento de Faturas que utiliza IA para extrair informações das faturas.

- Aplicar as melhores práticas ao usar o Modelo de IA Criar Texto com GPT.

- Entender o que é o Microsoft Copilot Studio e como construir agentes inteligentes com ele.

As ferramentas e tecnologias que você usará nesta lição são:

- **Power Apps**, para o app de Rastreamento de Tarefas dos Estudantes, que fornece um ambiente de desenvolvimento low-code para construir apps para rastrear, gerenciar e interagir com dados.

- **Dataverse**, para armazenar os dados do app de Rastreamento de Tarefas dos Estudantes onde o Dataverse fornecerá uma plataforma de dados low-code para armazenar os dados do app.

- **Power Automate**, para o fluxo de Processamento de Faturas onde você terá um ambiente de desenvolvimento low-code para construir workflows para automatizar o processo de Processamento de Faturas.

- **AI Builder**, para o Modelo de IA de Processamento de Faturas onde você usará Modelos de IA pré-construídos para processar as faturas para nossa startup.

## IA Generativa na Power Platform

Aprimorar o desenvolvimento low-code e aplicação com IA generativa é uma área de foco chave para Power Platform. O objetivo é capacitar todos a construir apps, sites, dashboards e automatizar processos com IA, _sem exigir qualquer expertise em ciência de dados_. Este objetivo é alcançado integrando a IA generativa na experiência de desenvolvimento low-code da Power Platform na forma do Copilot e do AI Builder.

### Como isso funciona?

Copilot é um assistente de IA que permite construir soluções na Power Platform descrevendo suas necessidades em uma série de passos conversacionais usando linguagem natural. Você pode, por exemplo, instruir seu assistente de IA a dizer quais campos seu app vai usar e ele criará tanto o app quanto o modelo de dados subjacente ou você pode especificar como configurar um fluxo no Power Automate.

Você pode usar funcionalidades orientadas por Copilot como um recurso nas telas do seu app para permitir que usuários descubram insights através de interações conversacionais.

AI Builder é uma capacidade de IA low-code disponível na Power Platform que permite usar Modelos de IA para ajudar a automatizar processos e prever resultados. Com AI Builder você pode trazer IA para seus apps e fluxos que se conectam aos seus dados no Dataverse ou em várias fontes de dados na nuvem, como SharePoint, OneDrive ou Azure.

Copilot está disponível em todos os produtos da Power Platform: Power Apps, Power Automate, Power BI, Power Pages e Copilot Studio (antigo Power Virtual Agents). AI Builder está disponível em Power Apps e Power Automate. Nesta lição, vamos focar em como usar Copilot e AI Builder em Power Apps e Power Automate para construir uma solução para nossa startup educacional.

### Copilot no Power Apps

Como parte da Power Platform, o Power Apps oferece um ambiente de desenvolvimento low-code para construir apps para rastrear, gerenciar e interagir com dados. É um conjunto de serviços de desenvolvimento de apps com uma plataforma de dados escalável e a capacidade de conectar a serviços na nuvem e dados locais. Power Apps permite construir apps que rodam em navegadores, tablets e celulares, e podem ser compartilhados com colegas. Power Apps facilita o desenvolvimento para usuários com uma interface simples, para que todo usuário de negócios ou desenvolvedor profissional possa criar apps personalizados. A experiência de desenvolvimento do app também é aprimorada com IA Generativa através do Copilot.

O recurso assistente de IA Copilot no Power Apps permite que você descreva que tipo de app precisa e quais informações você quer que seu app rastreie, colete ou mostre. O Copilot então gera um app Canvas responsivo com base na sua descrição. Você pode então personalizar o app para atender suas necessidades. O Copilot de IA também gera e sugere uma Tabela do Dataverse com os campos que você precisa para armazenar os dados que quer rastrear e alguns dados de exemplo. Vamos ver o que é o Dataverse e como você pode usá-lo no Power Apps nesta lição mais adiante. Você pode então personalizar a tabela para atender suas necessidades usando o recurso assistente do AI Copilot através de passos conversacionais. Este recurso está prontamente disponível na tela inicial do Power Apps.

### Copilot no Power Automate

Como parte da Power Platform, Power Automate permite que usuários criem fluxos automatizados entre aplicações e serviços. Ele ajuda a automatizar processos empresariais repetitivos, como comunicação, coleta de dados e aprovações de decisões. Sua interface simples permite que usuários de todos os níveis técnicos (do iniciante ao desenvolvedor experiente) automatizem tarefas de trabalho. A experiência de desenvolvimento de fluxo também é aprimorada com IA Generativa através do Copilot.

O recurso assistente de IA Copilot no Power Automate permite que você descreva que tipo de fluxo precisa e quais ações você quer que seu fluxo execute. O Copilot então gera um fluxo com base na sua descrição. Você pode então personalizar o fluxo para atender suas necessidades. O AI Copilot também gera e sugere as ações que você precisa para realizar a tarefa que quer automatizar. Vamos ver o que são fluxos e como você pode usá-los no Power Automate nesta lição mais adiante. Você pode então personalizar as ações para atender suas necessidades usando o recurso assistente AI Copilot através de passos conversacionais. Este recurso está prontamente disponível na tela inicial do Power Automate.

## Construindo Agentes Inteligentes com Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (antigo Power Virtual Agents) é o membro low-code da Power Platform para construir **agentes de IA** — copilotos conversacionais que podem responder perguntas, realizar ações e automatizar tarefas em nome dos seus usuários. Assim como o restante da Power Platform, você constrói esses agentes numa experiência visual, com linguagem natural em primeiro lugar: você descreve o que quer que o agente faça, e o Copilot Studio ajuda a estruturar suas instruções, conhecimento e ações.

Para nossa startup educacional, você poderia construir um agente que responda perguntas dos estudantes sobre cursos, verifique prazos de tarefas e até email um instrutor — tudo isso sem escrever código.

Aqui estão algumas das capacidades mais recentes que tornam o Copilot Studio poderoso:

- **Respostas generativas a partir do seu conhecimento**. Em vez de criar manualmente cada conversa, você pode conectar **fontes de conhecimento** — sites públicos, SharePoint, OneDrive, Dataverse, arquivos enviados ou dados empresariais via conectores — e o agente gera respostas fundamentadas a partir delas.

- **Orquestração generativa**. Em vez de depender de frases disparadoras rígidas, o agente usa IA para entender uma solicitação e decidir dinamicamente qual conhecimento, tópicos e ações combinar para cumpri-la, inclusive encadeando vários passos juntos.

- **Ações e conectores**. Os agentes podem *fazer* coisas, não só conversar. Você pode dar a um agente ações suportadas pelos 1.500+ conectores pré-construídos da Power Platform, fluxos Power Automate, APIs REST personalizadas, prompts ou servidores **Model Context Protocol (MCP)**.

- **Agentes autônomos**. Agentes não estão limitados a responder em uma janela de chat. Você pode construir **agentes autônomos** que são acionados por eventos — como um novo email, um novo registro no Dataverse ou um arquivo sendo enviado — e que atuam em segundo plano para completar uma tarefa.

- **Orquestração multiagentes**. Agentes podem chamar outros agentes. Um agente do Copilot Studio pode passar para, ou ser estendido por, outros agentes, inclusive agentes publicados no Microsoft 365 Copilot e agentes construídos no Microsoft Foundry.

- **Escolha do modelo**. Além dos modelos embutidos, você pode trazer modelos do catálogo de modelos do Microsoft Foundry para personalizar como seu agente raciocina e responde.

- **Publicar em qualquer lugar**. Uma vez construído, um agente pode ser publicado em múltiplos canais — Microsoft Teams, Microsoft 365 Copilot, um site ou app personalizado, e mais — com segurança, autenticação e análises gerenciadas pela experiência administrativa da Power Platform.

Você pode começar a construir seu primeiro agente em [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) e aprender mais na [documentação do Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Tarefa: Gerenciar tarefas dos estudantes e faturas para nossa startup, usando Copilot

Nossa startup oferece cursos online para estudantes. A startup cresceu rapidamente e agora está com dificuldades para acompanhar a demanda pelos seus cursos. A startup contratou você como desenvolvedor Power Platform para ajudar a construir uma solução low code que ajude a gerenciar as tarefas dos estudantes e as faturas. A solução deve ser capaz de ajudar a rastrear e gerenciar as tarefas dos estudantes via um app e automatizar o processo de processamento de faturas via um fluxo. Foi solicitado que você usasse IA Generativa para desenvolver a solução.

Quando estiver começando a usar o Copilot, você pode usar a [Biblioteca de Prompts do Power Platform Copilot](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) para iniciar com os prompts. Esta biblioteca contém uma lista de prompts que você pode usar para construir apps e fluxos com Copilot. Você também pode usar os prompts na biblioteca para ter uma ideia de como descrever suas necessidades ao Copilot.

### Construir um App de Rastreamento de Tarefas dos Estudantes para Nossa Startup

Os educadores da nossa startup têm tido dificuldades para acompanhar as tarefas dos estudantes. Eles têm usado uma planilha para rastrear as tarefas, mas isso se tornou difícil de gerenciar com o aumento do número de estudantes. Eles pediram que você construísse um app que os ajude a rastrear e gerenciar as tarefas dos estudantes. O app deve permitir que adicionem novas tarefas, visualizem as tarefas, atualizem tarefas e excluam tarefas. O app também deve permitir que educadores e estudantes visualizem as tarefas que foram avaliadas e as que ainda não foram avaliadas.

Você construirá o app usando o Copilot no Power Apps seguindo os passos abaixo:

1. Navegue até a tela inicial do [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Use a área de texto na tela inicial para descrever o app que deseja construir. Por exemplo, **_Eu quero construir um app para rastrear e gerenciar as tarefas dos estudantes_**. Clique no botão **Enviar** para mandar o prompt ao AI Copilot.

![Descreva o app que você quer construir](../../../translated_images/pt-BR/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. O AI Copilot sugerirá uma Tabela do Dataverse com os campos que você precisa para armazenar os dados que deseja rastrear e alguns dados de exemplo. Você pode então personalizar a tabela para atender suas necessidades usando o recurso assistente do AI Copilot através de passos conversacionais.

   > **Importante**: Dataverse é a plataforma de dados subjacente para a Power Platform. É uma plataforma de dados low-code para armazenar os dados do app. É um serviço totalmente gerenciado que armazena dados com segurança na nuvem da Microsoft e é provisionado dentro do seu ambiente Power Platform. Vem com capacidades embutidas de governança de dados, como classificação de dados, linhagem de dados, controle de acesso refinado e mais. Você pode aprender mais sobre o Dataverse [aqui](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Campos sugeridos na sua nova tabela](../../../translated_images/pt-BR/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Educadores querem enviar emails para os estudantes que submeteram suas tarefas para mantê-los atualizados sobre o progresso das suas tarefas. Você pode usar o Copilot para adicionar um novo campo à tabela para armazenar o email do estudante. Por exemplo, você pode usar o seguinte prompt para adicionar uma nova coluna à tabela: **_Quero adicionar uma coluna para armazenar o email dos estudantes_**. Clique no botão **Enviar** para mandar o prompt ao AI Copilot.

![Adicionando um novo campo](../../../translated_images/pt-BR/copilot-new-column.35e15ff21acaf274.webp)

1. O AI Copilot gerará um novo campo e você poderá personalizar o campo para atender suas necessidades.


1. Depois de terminar com a tabela, clique no botão **Criar aplicativo** para criar o aplicativo.

1. O AI Copilot gerará um aplicativo Canvas responsivo baseado na sua descrição. Você poderá então personalizar o aplicativo para atender às suas necessidades.

1. Para educadores enviarem e-mails para os alunos, você pode usar o Copilot para adicionar uma nova tela ao aplicativo. Por exemplo, você pode usar o seguinte comando para adicionar uma nova tela ao aplicativo: **_Quero adicionar uma tela para enviar e-mails aos alunos_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

![Adicionando uma nova tela via instrução por comando](../../../translated_images/pt-BR/copilot-new-screen.2e0bef7132a17392.webp)

1. O AI Copilot gerará uma nova tela e você poderá então personalizá-la para atender às suas necessidades.

1. Quando terminar o aplicativo, clique no botão **Salvar** para salvar o aplicativo.

1. Para compartilhar o aplicativo com os educadores, clique no botão **Compartilhar** e depois clique no botão **Compartilhar** novamente. Você poderá compartilhar o aplicativo com os educadores inserindo os endereços de e-mail deles.

> **Sua tarefa de casa**: O aplicativo que você acabou de criar é um bom começo, mas pode ser melhorado. Com o recurso de e-mail, os educadores só podem enviar e-mails aos alunos manualmente, digitando seus e-mails. Você pode usar o Copilot para construir uma automação que permita aos educadores enviar e-mails aos alunos automaticamente quando eles enviarem suas tarefas? A dica é que com o comando certo você pode usar o Copilot no Power Automate para criar isso.

### Crie uma Tabela de Informações de Faturas para Nossa Startup

A equipe financeira da nossa startup tem tido dificuldades para acompanhar as faturas. Eles têm usado uma planilha para controlar as faturas, mas isso se tornou difícil de gerenciar à medida que o número de faturas aumentou. Eles pediram que você criasse uma tabela que os ajude a armazenar, rastrear e gerenciar as informações das faturas que receberam. A tabela deve ser usada para criar uma automação que extraia todas as informações das faturas e armazene na tabela. A tabela também deve permitir que a equipe financeira visualize as faturas que foram pagas e as que ainda não foram pagas.

A Power Platform possui uma plataforma de dados subjacente chamada Dataverse que permite armazenar os dados dos seus aplicativos e soluções. O Dataverse fornece uma plataforma de dados de baixo código para armazenar os dados do aplicativo. É um serviço totalmente gerenciado que armazena dados com segurança na nuvem Microsoft e é provisionado dentro do seu ambiente Power Platform. Ele vem com recursos incorporados de governança de dados, como classificação de dados, linhagem de dados, controle de acesso detalhado, e mais. Você pode saber mais [sobre o Dataverse aqui](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Por que devemos usar o Dataverse para nossa startup? As tabelas padrão e personalizadas dentro do Dataverse oferecem uma opção segura e baseada na nuvem para o armazenamento dos seus dados. As tabelas permitem armazenar diferentes tipos de dados, parecido com como você usaria várias planilhas em um único arquivo do Excel. Você pode usar tabelas para armazenar dados específicos para sua organização ou necessidades de negócio. Alguns dos benefícios que nossa startup obterá ao usar o Dataverse incluem, mas não estão limitados a:

- **Fácil de gerenciar**: Tanto os metadados quanto os dados são armazenados na nuvem, então você não precisa se preocupar com os detalhes de como são armazenados ou gerenciados. Você pode se concentrar em construir seus aplicativos e soluções.

- **Seguro**: O Dataverse fornece uma opção segura e baseada na nuvem para o armazenamento dos seus dados. Você pode controlar quem tem acesso aos dados nas suas tabelas e como eles podem acessá-los usando segurança baseada em funções.

- **Metadados ricos**: Tipos de dados e relacionamentos são usados diretamente dentro do Power Apps.

- **Lógica e validação**: Você pode usar regras de negócio, campos calculados, e regras de validação para impor lógica de negócio e manter a precisão dos dados.

Agora que você sabe o que é o Dataverse e por que deve usá-lo, vamos ver como você pode usar o Copilot para criar uma tabela no Dataverse para atender aos requisitos da nossa equipe financeira.

> **Nota** : Você usará esta tabela na próxima seção para criar uma automação que extraia todas as informações das faturas e as armazene na tabela.

Para criar uma tabela no Dataverse usando o Copilot, siga os passos abaixo:

1. Navegue até a tela inicial do [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Na barra de navegação lateral esquerda, selecione **Tabelas** e depois clique em **Descreva a nova Tabela**.

![Selecionar nova tabela](../../../translated_images/pt-BR/describe-new-table.0792373eb757281e.webp)

1. Na tela **Descreva a nova Tabela**, use a área de texto para descrever a tabela que deseja criar. Por exemplo, **_Quero criar uma tabela para armazenar informações de faturas_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

![Descrever a tabela](../../../translated_images/pt-BR/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. O AI Copilot sugerirá uma Tabela Dataverse com os campos que você precisa para armazenar os dados que deseja rastrear e alguns dados exemplos. Você poderá então personalizar a tabela para atender às suas necessidades usando o recurso assistente do AI Copilot por etapas conversacionais.

![Tabela Dataverse sugerida](../../../translated_images/pt-BR/copilot-dataverse-table.b3bc936091324d9d.webp)

1. A equipe financeira quer enviar um e-mail ao fornecedor para atualizá-lo sobre o status atual da fatura. Você pode usar o Copilot para adicionar um novo campo à tabela para armazenar o e-mail do fornecedor. Por exemplo, você pode usar o seguinte comando para adicionar um novo campo à tabela: **_Quero adicionar uma coluna para armazenar e-mail do fornecedor_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

1. O AI Copilot gerará um novo campo e você poderá então personalizar o campo para atender às suas necessidades.

1. Quando terminar a tabela, clique no botão **Criar** para criar a tabela.

## Modelos de IA na Power Platform com AI Builder

O AI Builder é um recurso de IA low-code disponível na Power Platform que permite usar Modelos de IA para ajudar a automatizar processos e prever resultados. Com o AI Builder, você pode levar IA para seus aplicativos e fluxos que se conectam aos seus dados no Dataverse ou em várias fontes de dados na nuvem, como SharePoint, OneDrive ou Azure.

## Modelos de IA Pré-construídos vs Modelos de IA Personalizados

O AI Builder fornece dois tipos de Modelos de IA: Modelos de IA Pré-construídos e Modelos de IA Personalizados. Modelos de IA Pré-construídos são modelos prontos para uso, treinados pela Microsoft e disponíveis na Power Platform. Eles ajudam a adicionar inteligência aos seus aplicativos e fluxos sem precisar coletar dados e construir, treinar e publicar seus próprios modelos. Você pode usar esses modelos para automatizar processos e prever resultados.

Alguns dos Modelos de IA Pré-construídos disponíveis na Power Platform incluem:

- **Extração de Frases-chave**: Este modelo extrai frases-chave do texto.
- **Detecção de Idioma**: Este modelo detecta o idioma de um texto.
- **Análise de Sentimentos**: Este modelo detecta sentimentos positivos, negativos, neutros ou mistos em textos.
- **Leitor de Cartões de Visita**: Este modelo extrai informações de cartões de visita.
- **Reconhecimento de Texto**: Este modelo extrai texto de imagens.
- **Detecção de Objetos**: Este modelo detecta e extrai objetos de imagens.
- **Processamento de Documentos**: Este modelo extrai informações de formulários.
- **Processamento de Faturas**: Este modelo extrai informações de faturas.

Com Modelos de IA Personalizados, você pode trazer seu próprio modelo para o AI Builder para que ele funcione como qualquer modelo personalizado do AI Builder, permitindo que você treine o modelo usando seus próprios dados. Você pode usar esses modelos para automatizar processos e prever resultados tanto no Power Apps quanto no Power Automate. Ao usar seu próprio modelo, existem limitações que se aplicam. Leia mais sobre estas [limitações](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![modelos do AI builder](../../../translated_images/pt-BR/ai-builder-models.8069423b84cfc47f.webp)

## Tarefa #2 - Crie um fluxo de processamento de faturas para nossa startup

A equipe financeira tem enfrentado dificuldades para processar faturas. Eles têm usado uma planilha para controlar as faturas, mas isso se tornou difícil de gerenciar à medida que o número de faturas aumentou. Eles pediram que você criasse um fluxo de trabalho que os ajude a processar faturas usando IA. O fluxo de trabalho deve permitir extrair informações das faturas e armazenar essas informações em uma tabela do Dataverse. O fluxo de trabalho também deve permitir que eles enviem um e-mail para a equipe financeira com as informações extraídas.

Agora que você sabe o que é o AI Builder e por que usá-lo, vamos ver como você pode usar o Modelo de IA de Processamento de Faturas do AI Builder, que abordamos anteriormente, para criar um fluxo que ajudará a equipe financeira a processar faturas.

Para criar um fluxo que ajude a equipe financeira a processar faturas usando o Modelo de IA de Processamento de Faturas do AI Builder, siga os passos abaixo:

1. Navegue até a tela inicial do [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Use a área de texto na tela inicial para descrever o fluxo que deseja criar. Por exemplo, **_Processar uma fatura quando ela chegar na minha caixa de entrada_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

   ![Copilot power automate](../../../translated_images/pt-BR/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. O AI Copilot sugerirá as ações necessárias para realizar a tarefa que você deseja automatizar. Você pode clicar no botão **Próximo** para passar para as próximas etapas.

4. Na próxima etapa, o Power Automate solicitará que você configure as conexões necessárias para o fluxo. Quando terminar, clique no botão **Criar fluxo** para criar o fluxo.

5. O AI Copilot gerará um fluxo e você poderá personalizá-lo para atender às suas necessidades.

6. Atualize o gatilho do fluxo e defina a **Pasta** para a pasta onde as faturas serão armazenadas. Por exemplo, você pode definir a pasta para **Caixa de entrada**. Clique em **Mostrar opções avançadas** e defina **Somente com anexos** como **Sim**. Isso garantirá que o fluxo só será executado quando um e-mail com anexo for recebido na pasta.

7. Remova as seguintes ações do fluxo: **HTML para texto**, **Compor**, **Compor 2**, **Compor 3** e **Compor 4** porque você não irá usá-las.

8. Remova a ação **Condição** do fluxo porque você não irá usá-la. Deve ficar como mostrado na captura de tela a seguir:

   ![power automate, remover ações](../../../translated_images/pt-BR/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Clique no botão **Adicionar uma ação** e procure por **Dataverse**. Selecione a ação **Adicionar uma nova linha**.

10. Na ação **Extrair informações das faturas**, atualize o **Arquivo da Fatura** para apontar para o **Conteúdo do Anexo** do e-mail. Isso garantirá que o fluxo extraia informações do anexo da fatura.

11. Selecione a **Tabela** que você criou anteriormente. Por exemplo, você pode selecionar a tabela **Informações de Faturas**. Escolha o conteúdo dinâmico da ação anterior para preencher os seguintes campos:

    - ID
    - Valor
    - Data
    - Nome
    - Status - Defina o **Status** como **Pendente**.
    - E-mail do Fornecedor - Use o conteúdo dinâmico **De** do gatilho **Quando um novo e-mail chega**.

    ![power automate adicionar linha](../../../translated_images/pt-BR/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Quando terminar o fluxo, clique no botão **Salvar** para salvar o fluxo. Você pode testá-lo enviando um e-mail com uma fatura para a pasta que especificou no gatilho.

> **Sua tarefa de casa**: O fluxo que você acabou de construir é um bom começo, agora você precisa pensar em como criar uma automação que permita à nossa equipe financeira enviar um e-mail ao fornecedor para atualizá-lo sobre o status atual da fatura. Sua dica: o fluxo deve ser executado quando o status da fatura mudar.

## Use um Modelo de IA de Geração de Texto no Power Automate

O modelo AI Criar Texto com GPT no AI Builder permite que você gere texto baseado em um comando e é alimentado pelo Microsoft Azure OpenAI Service. Com essa capacidade, você pode incorporar a tecnologia GPT (Generative Pre-Trained Transformer) aos seus aplicativos e fluxos para criar uma variedade de fluxos automáticos e aplicações inteligentes.

Modelos GPT passam por um extenso treinamento em grandes volumes de dados, permitindo que produzam textos que se assemelham muito à linguagem humana ao receberem um comando. Integrados à automação de fluxos de trabalho, modelos de IA como o GPT podem ser usados para simplificar e automatizar uma ampla gama de tarefas.

Por exemplo, você pode construir fluxos para gerar automaticamente textos para diversos casos de uso, como: rascunhos de e-mails, descrições de produtos e mais. Você também pode usar o modelo para gerar textos para vários aplicativos, como chatbots e apps de atendimento ao cliente que permitam que os agentes respondam de forma eficaz e eficiente às perguntas dos clientes.

![criar um comando](../../../translated_images/pt-BR/create-prompt-gpt.69d429300c2e870a.webp)


Para aprender como usar este Modelo de IA no Power Automate, passe pelo módulo [Adicionar inteligência com AI Builder e GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Ótimo trabalho! Continue seu aprendizado

Depois de concluir esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Quer personalizar e aproveitar mais do Copilot? Explore o [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — uma coleção contribuída pela comunidade de instruções, agentes, habilidades e configurações para ajudar você a aproveitar ao máximo o GitHub Copilot.

Vá para a Lição 11, onde veremos como [integrar IA Generativa com Chamada de Função](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->