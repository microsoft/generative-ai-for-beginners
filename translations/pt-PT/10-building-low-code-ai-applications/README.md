# Construir Aplicações de IA Low Code

[![Construir Aplicações de IA Low Code](../../../translated_images/pt-PT/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Clique na imagem acima para ver o vídeo desta aula)_

## Introdução

Agora que aprendemos a construir aplicações de geração de imagem, vamos falar sobre low code. A IA generativa pode ser usada para várias áreas diferentes, incluindo low code, mas o que é low code e como podemos adicionar IA a isso?

Construir apps e soluções tornou-se mais fácil para desenvolvedores tradicionais e não desenvolvedores através do uso de Plataformas de Desenvolvimento Low Code. Plataformas Low Code permitem que construa apps e soluções com pouco ou nenhum código. Isto é alcançado fornecendo um ambiente de desenvolvimento visual que permite arrastar e largar componentes para construir apps e soluções. Isto permite construir apps e soluções mais rapidamente e com menos recursos. Nesta lição, exploramos profundamente como usar Low Code e como melhorar o desenvolvimento low code com IA usando a Power Platform.

A Power Platform oferece às organizações a oportunidade de capacitar as suas equipas para construírem as suas próprias soluções através de um ambiente intuitivo de low-code ou no-code. Este ambiente ajuda a simplificar o processo de construção de soluções. Com a Power Platform, as soluções podem ser construídas em dias ou semanas em vez de meses ou anos. A Power Platform consiste em cinco produtos chave: Power Apps, Power Automate, Power BI, Power Pages e Copilot Studio.

Esta lição abrange:

- Introdução à IA Generativa na Power Platform
- Introdução ao Copilot e como usá-lo
- Usar IA Generativa para construir apps e fluxos na Power Platform
- Compreender os Modelos de IA na Power Platform com o AI Builder
- Construção de agentes inteligentes com o Microsoft Copilot Studio

## Objetivos de Aprendizagem

Ao final desta lição, será capaz de:

- Compreender como o Copilot funciona na Power Platform.

- Construir uma App de Gestão de Tarefas para Estudantes para a nossa startup de educação.

- Construir um Fluxo de Processamento de Faturas que utiliza IA para extrair informação das faturas.

- Aplicar as melhores práticas ao usar o Modelo de IA Create Text com GPT.

- Compreender o que é o Microsoft Copilot Studio e como construir agentes inteligentes com ele.

As ferramentas e tecnologias que irá usar nesta lição são:

- **Power Apps**, para a app Student Assignment Tracker, que fornece um ambiente de desenvolvimento low-code para construir apps para seguir, gerir e interagir com dados.

- **Dataverse**, para armazenar os dados da app Student Assignment Tracker onde o Dataverse fornece uma plataforma de dados low-code para armazenar os dados da app.

- **Power Automate**, para o fluxo de Processamento de Faturas onde terá um ambiente de desenvolvimento low-code para construir fluxos de trabalho para automatizar o processo de Processamento de Faturas.

- **AI Builder**, para o Modelo de IA de Processamento de Faturas onde usará Modelos de IA pré-construídos para processar as faturas para a nossa startup.

## IA Generativa na Power Platform

A melhoria do desenvolvimento low-code e da aplicação com IA generativa é uma área chave da Power Platform. O objetivo é permitir a todos construir apps, sites, dashboards e automatizar processos com IA, _sem necessitar de qualquer expertise em ciência de dados_. Este objetivo é alcançado integrando IA generativa na experiência de desenvolvimento low-code na Power Platform na forma de Copilot e AI Builder.

### Como funciona isto?

O Copilot é um assistente de IA que permite construir soluções Power Platform descrevendo os seus requisitos numa série de passos conversacionais usando linguagem natural. Pode, por exemplo, instruir o seu assistente de IA para dizer quais os campos que a sua app vai usar e ele irá criar tanto a app como o modelo de dados subjacente ou pode especificar como configurar um fluxo no Power Automate.

Pode usar funcionalidades impulsionadas pelo Copilot como uma funcionalidade nos seus ecrãs de app para permitir que os utilizadores descubram insights através de interações conversacionais.

O AI Builder é uma capacidade de IA low-code disponível na Power Platform que permite usar Modelos de IA para ajudar a automatizar processos e prever resultados. Com o AI Builder pode levar IA às suas apps e fluxos que se liguem aos seus dados no Dataverse ou em várias fontes de dados na cloud, como SharePoint, OneDrive ou Azure.

O Copilot está disponível em todos os produtos da Power Platform: Power Apps, Power Automate, Power BI, Power Pages e Copilot Studio (antigo Power Virtual Agents). O AI Builder está disponível no Power Apps e Power Automate. Nesta lição, vamos focar-nos em como usar Copilot e AI Builder no Power Apps e Power Automate para construir uma solução para a nossa startup de educação.

### Copilot no Power Apps

Como parte da Power Platform, o Power Apps fornece um ambiente de desenvolvimento low-code para construir apps para seguir, gerir e interagir com dados. É uma suíte de serviços de desenvolvimento de apps com uma plataforma de dados escalável e a capacidade de se conectar a serviços de cloud e dados on-premises. O Power Apps permite construir apps que correm em browsers, tablets e telemóveis, e podem ser partilhados com colegas. O Power Apps facilita aos utilizadores o desenvolvimento de apps com uma interface simples, para que cada utilizador de negócio ou programador possa construir apps personalizadas. A experiência de desenvolvimento de apps é também melhorada com IA Generativa através do Copilot.

A funcionalidade de assistente de IA Copilot no Power Apps permite-lhe descrever que tipo de app precisa e que informação quer que a sua app acompanhe, recolha, ou mostre. O Copilot gera então uma app Canvas responsiva baseada na sua descrição. Pode depois personalizar a app para satisfazer as suas necessidades. O Copilot de IA também gera e sugere uma Tabela Dataverse com os campos que precisa para armazenar os dados que quer acompanhar e alguns dados de exemplo. Vamos ver o que é o Dataverse e como pode usá-lo no Power Apps mais adiante nesta lição. Pode depois personalizar a tabela para as suas necessidades usando a funcionalidade de assistente AI Copilot através de passos conversacionais. Esta funcionalidade está facilmente disponível no ecrã inicial do Power Apps.

### Copilot no Power Automate

Como parte da Power Platform, o Power Automate permite aos utilizadores criar fluxos automáticos entre aplicações e serviços. Ajuda a automatizar processos de negócio repetitivos, tais como comunicação, recolha de dados, e aprovações de decisões. A sua interface simples permite aos utilizadores de todos os níveis técnicos (desde iniciantes a programadores experientes) automatizar tarefas de trabalho. A experiência de desenvolvimento de fluxos é também melhorada com IA Generativa através do Copilot.

A funcionalidade de assistente de IA Copilot no Power Automate permite-lhe descrever que tipo de fluxo precisa e que ações quer que o seu fluxo execute. O Copilot gera então um fluxo baseado na sua descrição. Pode depois personalizar o fluxo para as suas necessidades. O Copilot de IA também gera e sugere as ações que precisa para executar a tarefa que quer automatizar. Vamos ver o que são fluxos e como pode usá-los no Power Automate mais adiante nesta lição. Pode depois personalizar as ações para as suas necessidades usando a funcionalidade de assistente AI Copilot através de passos conversacionais. Esta funcionalidade está facilmente disponível no ecrã inicial do Power Automate.

## Construir Agentes Inteligentes com o Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (antigo Power Virtual Agents) é o membro low-code da Power Platform para construir **agentes de IA** — copilotos conversacionais que podem responder a perguntas, executar ações e automatizar tarefas em nome dos seus utilizadores. Tal como o resto da Power Platform, constrói estes agentes numa experiência visual, priorizando linguagem natural: descreve o que quer que o agente faça, e o Copilot Studio ajuda a estruturar as suas instruções, conhecimentos e ações.

Para a nossa startup de educação, pode construir um agente que responda a perguntas dos estudantes sobre os cursos, verifique prazos de tarefas, e até envie emails a um instrutor — tudo sem escrever código.

Aqui estão algumas das últimas capacidades que tornam o Copilot Studio poderoso:

- **Respostas generativas do seu conhecimento**. Em vez de escrever manualmente cada conversa, pode ligar **fontes de conhecimento** — websites públicos, SharePoint, OneDrive, Dataverse, ficheiros carregados, ou dados empresariais através de conectores — e o agente gera respostas fundamentadas a partir deles.

- **Orquestração generativa**. Em vez de depender de frases de ativação rígidas, o agente usa IA para entender um pedido e decidir dinamicamente qual o conhecimento, tópicos e ações a combinar para o satisfazer, incluindo encadear vários passos.

- **Ações e conectores**. Os agentes podem *fazer* coisas, não só conversar. Pode fornecer a um agente ações suportadas pelos mais de 1.500 conectores pré-construídos da Power Platform, fluxos Power Automate, APIs REST personalizadas, prompts ou servidores **Model Context Protocol (MCP)**.

- **Agentes autónomos**. Os agentes não estão limitados a responder numa janela de chat. Pode construir **agentes autónomos** que são ativados por eventos — como um novo email, um novo registo no Dataverse, ou um ficheiro a ser carregado — e depois atuam em segundo plano para completar uma tarefa.

- **Orquestração multiagente**. Os agentes podem chamar outros agentes. Um agente do Copilot Studio pode passar para, ou ser extendido por, outros agentes, incluindo agentes publicados no Microsoft 365 Copilot e agentes construídos no Microsoft Foundry.

- **Escolha do modelo**. Para além dos modelos integrados, pode trazer modelos do catálogo de modelos Microsoft Foundry para personalizar como o seu agente raciocina e responde.

- **Publicar em qualquer lugar**. Uma vez construído, um agente pode ser publicado em vários canais — Microsoft Teams, Microsoft 365 Copilot, um website ou app personalizada, e mais — com segurança, autenticação e análises geridas através da experiência de administração da Power Platform.

Pode começar a construir o seu primeiro agente em [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) e aprender mais na [documentação do Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Exercício: Gerir tarefas de estudantes e faturas para a nossa startup, usando o Copilot

A nossa startup oferece cursos online para estudantes. A startup cresceu rapidamente e agora está a ter dificuldades em acompanhar a procura pelos seus cursos. A startup contratou-o como desenvolvedor da Power Platform para ajudar a construir uma solução low code para os ajudar a gerir as tarefas dos estudantes e as faturas. A solução deve ser capaz de os ajudar a seguir e gerir as tarefas através de uma app e automatizar o processo de processamento de faturas através de um fluxo de trabalho. Foi-lhe pedido usar IA generativa para desenvolver a solução.

Quando começar a usar o Copilot, pode usar a [Biblioteca de Prompts do Power Platform Copilot](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) para começar com os prompts. Esta biblioteca contém uma lista de prompts que pode usar para construir apps e fluxos com o Copilot. Também pode usar os prompts na biblioteca para ter uma ideia de como descrever os seus requisitos ao Copilot.

### Construir uma App de Gestão de Tarefas para Estudantes para a Nossa Startup

Os educadores da nossa startup têm tido dificuldades em acompanhar as tarefas dos estudantes. Eles têm usado uma folha de cálculo para acompanhar as tarefas, mas isso tornou-se difícil de gerir à medida que o número de estudantes aumentou. Pediram-lhe que construísse uma app que os ajude a acompanhar e gerir as tarefas dos estudantes. A app deve permitir adicionar novas tarefas, ver tarefas, atualizar tarefas e eliminar tarefas. A app também deverá permitir que educadores e estudantes vejam as tarefas que foram avaliadas e aquelas que ainda não foram avaliadas.

Vai construir a app usando o Copilot no Power Apps seguindo os passos abaixo:

1. Navegue até ao ecrã inicial do [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Use a área de texto no ecrã inicial para descrever a app que quer construir. Por exemplo, **_Quero construir uma app para acompanhar e gerir tarefas de estudantes_**. Clique no botão **Enviar** para enviar o prompt ao AI Copilot.

![Descrever a app que quer construir](../../../translated_images/pt-PT/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. O AI Copilot irá sugerir uma Tabela Dataverse com os campos que precisa para armazenar os dados que quer acompanhar e alguns dados de amostra. Pode depois personalizar a tabela para satisfazer as suas necessidades usando a funcionalidade de assistente AI Copilot através de passos conversacionais.

   > **Importante**: Dataverse é a plataforma de dados subjacente para a Power Platform. É uma plataforma de dados low-code para armazenar os dados da app. É um serviço totalmente gerido que armazena dados de forma segura na Microsoft Cloud e é provisionado dentro do seu ambiente Power Platform. Vem com capacidades integradas de governança de dados, tais como classificação de dados, linhagem de dados, controlo de acesso detalhado, e mais. Pode aprender mais acerca do Dataverse [aqui](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Campos sugeridos na sua nova tabela](../../../translated_images/pt-PT/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Os educadores querem enviar emails aos estudantes que entregaram as suas tarefas para os manter atualizados sobre o progresso das tarefas. Pode usar o Copilot para adicionar um novo campo à tabela para armazenar o email do estudante. Por exemplo, pode usar o seguinte prompt para adicionar uma nova coluna à tabela: **_Quero adicionar uma coluna para armazenar email do estudante_**. Clique no botão **Enviar** para enviar o prompt ao AI Copilot.

![Adicionando um novo campo](../../../translated_images/pt-PT/copilot-new-column.35e15ff21acaf274.webp)

1. O AI Copilot irá gerar um novo campo e pode depois personalizar esse campo para satisfazer as suas necessidades.


1. Depois de terminar com a tabela, clique no botão **Criar app** para criar a aplicação.

1. O AI Copilot irá gerar uma aplicação Canvas responsiva com base na sua descrição. Pode depois personalizar a aplicação para satisfazer as suas necessidades.

1. Para que os educadores possam enviar emails aos alunos, pode usar o Copilot para adicionar um novo ecrã à aplicação. Por exemplo, pode usar o seguinte prompt para adicionar um novo ecrã à aplicação: **_Quero adicionar um ecrã para enviar emails aos alunos_**. Clique no botão **Enviar** para enviar o prompt ao AI Copilot.

![Adding a new screen via a prompt instruction](../../../translated_images/pt-PT/copilot-new-screen.2e0bef7132a17392.webp)

1. O AI Copilot irá gerar um novo ecrã e pode depois personalizar o ecrã para satisfazer as suas necessidades.

1. Depois de terminar a aplicação, clique no botão **Guardar** para salvar a aplicação.

1. Para partilhar a aplicação com os educadores, clique no botão **Partilhar** e depois clique novamente no botão **Partilhar**. Pode então partilhar a aplicação com os educadores introduzindo os seus endereços de email.

> **O seu trabalho de casa**: A aplicação que acabou de construir é um bom começo, mas pode ser melhorada. Com a funcionalidade de email, os educadores só podem enviar emails aos alunos manualmente ao terem de digitar os seus emails. Consegue usar o Copilot para construir uma automação que permita aos educadores enviar emails aos alunos automaticamente quando estes entregam os seus trabalhos? A sua dica é que com o prompt certo pode usar o Copilot no Power Automate para construir isto.

### Construir uma Tabela de Informação de Faturas para a Nossa Startup

A equipa financeira da nossa startup tem tido dificuldades em acompanhar as faturas. Têm usado uma folha de cálculo para acompanhar as faturas, mas isto tornou-se difícil de gerir à medida que o número de faturas aumentou. Pediram-lhe para construir uma tabela que os ajude a armazenar, acompanhar e gerir a informação das faturas que receberam. A tabela deve ser usada para construir uma automação que extraia toda a informação das faturas e a armazene na tabela. A tabela deve também permitir à equipa financeira visualizar as faturas que foram pagas e aquelas que ainda não foram pagas.

A Power Platform tem uma plataforma de dados subjacente chamada Dataverse que lhe permite armazenar os dados das suas aplicações e soluções. O Dataverse fornece uma plataforma de dados low-code para armazenar os dados da aplicação. É um serviço totalmente gerido que armazena dados com segurança na Nuvem da Microsoft e é provisionado dentro do seu ambiente Power Platform. Vem com capacidades incorporadas de governação de dados, tais como classificação de dados, linhagem de dados, controlo de acesso detalhado, e mais. Pode aprender mais [sobre o Dataverse aqui](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Porque é que devemos usar o Dataverse para a nossa startup? As tabelas padrão e personalizadas dentro do Dataverse fornecem uma opção segura e baseada na nuvem para armazenar os seus dados. As tabelas permitem-lhe armazenar diferentes tipos de dados, parecido com a forma como usaria múltiplas folhas numa única pasta de trabalho Excel. Pode usar tabelas para armazenar dados que são específicos para a sua organização ou necessidades comerciais. Alguns dos benefícios que a nossa startup obterá ao usar o Dataverse incluem, mas não se limitam a:

- **Fácil de gerir**: Tanto os metadados como os dados são armazenados na nuvem, por isso não precisa de se preocupar com os detalhes de como são armazenados ou geridos. Pode concentrar-se em construir as suas aplicações e soluções.

- **Seguro**: O Dataverse fornece uma opção segura e baseada na nuvem para armazenar os seus dados. Pode controlar quem tem acesso aos dados nas suas tabelas e como podem aceder a eles utilizando segurança baseada em funções.

- **Metadados ricos**: Tipos de dados e relações são usados diretamente dentro das Power Apps

- **Lógica e validação**: Pode usar regras de negócio, campos calculados e regras de validação para impor a lógica de negócio e manter a precisão dos dados.

Agora que sabe o que é o Dataverse e porque deve usá-lo, vamos ver como pode usar o Copilot para criar uma tabela no Dataverse para satisfazer os requisitos da nossa equipa financeira.

> **Nota** : Vai usar esta tabela na próxima secção para construir uma automação que irá extrair toda a informação das faturas e armazená-la na tabela.

Para criar uma tabela no Dataverse usando o Copilot, siga os passos abaixo:

1. Navegue até ao ecrã inicial do [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Na barra de navegação à esquerda, selecione **Tabelas** e depois clique em **Descrever a nova Tabela**.

![Select new table](../../../translated_images/pt-PT/describe-new-table.0792373eb757281e.webp)

1. No ecrã **Descrever a nova Tabela**, use a área de texto para descrever a tabela que deseja criar. Por exemplo, **_Quero criar uma tabela para armazenar informação de faturas_**. Clique no botão **Enviar** para enviar o prompt ao AI Copilot.

![Describe the table](../../../translated_images/pt-PT/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. O AI Copilot irá sugerir uma Tabela Dataverse com os campos necessários para armazenar os dados que deseja acompanhar e alguns dados de exemplo. Pode depois personalizar a tabela para satisfazer as suas necessidades usando o assistente AI Copilot através de passos conversacionais.

![Suggested Dataverse table](../../../translated_images/pt-PT/copilot-dataverse-table.b3bc936091324d9d.webp)

1. A equipa financeira quer enviar um email ao fornecedor para os atualizar sobre o estado atual da sua fatura. Pode usar o Copilot para adicionar um novo campo na tabela para armazenar o email do fornecedor. Por exemplo, pode usar o seguinte prompt para adicionar um novo campo à tabela: **_Quero adicionar uma coluna para armazenar o email do fornecedor_**. Clique no botão **Enviar** para enviar o prompt ao AI Copilot.

1. O AI Copilot irá gerar um novo campo e pode depois personalizar o campo para satisfazer as suas necessidades.

1. Depois de terminar com a tabela, clique no botão **Criar** para criar a tabela.

## Modelos de IA na Power Platform com AI Builder

O AI Builder é uma capacidade de IA low-code disponível na Power Platform que lhe permite usar Modelos de IA para o ajudar a automatizar processos e prever resultados. Com o AI Builder pode trazer IA para as suas aplicações e fluxos que estão ligados aos seus dados no Dataverse ou em várias fontes de dados na nuvem, como SharePoint, OneDrive ou Azure.

## Modelos de IA Pré-construídos vs Modelos de IA Personalizados

O AI Builder fornece dois tipos de Modelos de IA: Modelos de IA Pré-construídos e Modelos de IA Personalizados. Os Modelos de IA Pré-construídos são modelos prontos a usar que são treinados pela Microsoft e disponíveis na Power Platform. Estes ajudam-no a adicionar inteligência às suas aplicações e fluxos sem ter de recolher dados e depois construir, treinar e publicar os seus próprios modelos. Pode usar estes modelos para automatizar processos e prever resultados.

Alguns dos Modelos de IA Pré-construídos disponíveis na Power Platform incluem:

- **Extração de Frases-Chave**: Este modelo extrai frases-chave de texto.
- **Deteção de Língua**: Este modelo deteta a língua de um texto.
- **Análise de Sentimentos**: Este modelo deteta sentimentos positivos, negativos, neutros ou mistos no texto.
- **Leitor de Cartões de Visita**: Este modelo extrai informações de cartões de visita.
- **Reconhecimento de Texto**: Este modelo extrai texto das imagens.
- **Deteção de Objetos**: Este modelo deteta e extrai objetos das imagens.
- **Processamento de Documentos**: Este modelo extrai informações de formulários.
- **Processamento de Faturas**: Este modelo extrai informações de faturas.

Com os Modelos de IA Personalizados pode trazer o seu próprio modelo para o AI Builder para que funcione como qualquer modelo personalizado do AI Builder, permitindo-lhe treinar o modelo usando os seus próprios dados. Pode usar estes modelos para automatizar processos e prever resultados tanto nas Power Apps como no Power Automate. Quando usar o seu próprio modelo existem limitações que se aplicam. Leia mais sobre essas [limitações](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/pt-PT/ai-builder-models.8069423b84cfc47f.webp)

## Trabalho de Casa #2 - Construir um Fluxo de Processamento de Faturas para a Nossa Startup

A equipa financeira tem tido dificuldades em processar faturas. Têm usado uma folha de cálculo para acompanhar as faturas, mas isto tornou-se difícil de gerir à medida que o número de faturas aumentou. Pediram-lhe para construir um fluxo de trabalho que os ajude a processar faturas usando IA. O fluxo de trabalho deve permitir-lhes extrair informações das faturas e armazenar essa informação numa tabela do Dataverse. O fluxo de trabalho deve também permitir-lhes enviar um email à equipa financeira com a informação extraída.

Agora que sabe o que é o AI Builder e porque deve usá-lo, vejamos como pode usar o Modelo de IA de Processamento de Faturas no AI Builder, que abordámos anteriormente, para construir um fluxo de trabalho que ajude a equipa financeira a processar faturas.

Para construir um fluxo de trabalho que ajude a equipa financeira a processar faturas usando o Modelo de IA de Processamento de Faturas no AI Builder, siga os passos abaixo:

1. Navegue até ao ecrã inicial do [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Use a área de texto no ecrã inicial para descrever o fluxo de trabalho que deseja construir. Por exemplo, **_Processar uma fatura quando esta chegar à minha caixa de correio_**. Clique no botão **Enviar** para enviar o prompt ao AI Copilot.

   ![Copilot power automate](../../../translated_images/pt-PT/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. O AI Copilot irá sugerir as ações que precisa para realizar a tarefa que deseja automatizar. Pode clicar no botão **Seguinte** para avançar para os passos seguintes.

4. No passo seguinte, o Power Automate irá pedir que configure as ligações necessárias para o fluxo. Depois de terminar, clique no botão **Criar fluxo** para criar o fluxo.

5. O AI Copilot irá gerar um fluxo e pode depois personalizar o fluxo para satisfazer as suas necessidades.

6. Atualize o desencadeador do fluxo e defina a **Pasta** para a pasta onde as faturas serão armazenadas. Por exemplo, pode definir a pasta para **Caixa de Entrada**. Clique em **Mostrar opções avançadas** e defina **Apenas com Anexos** para **Sim**. Isto assegurará que o fluxo só seja executado quando um email com anexo for recebido na pasta.

7. Remova as seguintes ações do fluxo: **HTML para texto**, **Compor**, **Compor 2**, **Compor 3** e **Compor 4**, porque não irá usá-las.

8. Remova a ação **Condição** do fluxo porque não irá usá-la. Deverá parecer com o seguinte ecrã:

   ![power automate, remove actions](../../../translated_images/pt-PT/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Clique no botão **Adicionar uma ação** e pesquise por **Dataverse**. Selecione a ação **Adicionar uma nova linha**.

10. Na ação **Extrair Informação das faturas**, atualize o **Ficheiro da Fatura** para apontar para o **Conteúdo do Anexo** do email. Isto assegurará que o fluxo extrai informação do anexo da fatura.

11. Selecione a **Tabela** que criou anteriormente. Por exemplo, pode selecionar a tabela **Informação de Faturas**. Escolha o conteúdo dinâmico da ação anterior para preencher os seguintes campos:

    - ID
    - Valor
    - Data
    - Nome
    - Estado - Defina o **Estado** como **Pendente**.
    - Email do Fornecedor - Use o conteúdo dinâmico **De** do desencadeador **Quando um novo email chega**.

    ![power automate add row](../../../translated_images/pt-PT/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Depois de terminar o fluxo, clique no botão **Guardar** para salvar o fluxo. Pode então testar o fluxo enviando um email com uma fatura para a pasta que especificou no desencadeador.

> **O seu trabalho de casa**: O fluxo que acabou de construir é um bom começo, agora precisa de pensar como pode construir uma automação que permita à nossa equipa financeira enviar um email ao fornecedor para os atualizar sobre o estado atual da sua fatura. A sua dica: o fluxo deve ser executado quando o estado da fatura mudar.

## Use um Modelo de IA de Geração de Texto no Power Automate

O Modelo de IA Criar Texto com GPT no AI Builder permite-lhe gerar texto com base num prompt e é alimentado pelo Microsoft Azure OpenAI Service. Com esta capacidade, pode incorporar a tecnologia GPT (Generative Pre-Trained Transformer) nas suas aplicações e fluxos para construir uma variedade de fluxos automatizados e aplicações informativas.

Os modelos GPT passam por um treino extensivo com grandes quantidades de dados, permitindo-lhes produzir texto que se assemelha de forma próxima à linguagem humana quando recebem um prompt. Quando integrado com a automação de fluxos de trabalho, modelos de IA como o GPT podem ser usados para simplificar e automatizar uma ampla gama de tarefas.

Por exemplo, pode construir fluxos para gerar texto automaticamente para vários casos de uso, como: rascunhos de emails, descrições de produtos, e mais. Pode também usar o modelo para gerar texto para várias aplicações, como chatbots e aplicações de serviço ao cliente que permitem aos agentes responder de forma eficaz e eficiente às consultas dos clientes.

![create a prompt](../../../translated_images/pt-PT/create-prompt-gpt.69d429300c2e870a.webp)


Para aprender a usar este Modelo de IA no Power Automate, consulte o módulo [Adicionar inteligência com AI Builder e GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Excelente trabalho! Continue a sua aprendizagem

Após completar esta lição, consulte a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar o seu conhecimento em IA Generativa!

Quer personalizar e tirar mais proveito do Copilot? Explore o [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — uma coleção contribuída pela comunidade de instruções, agentes, competências e configurações para o ajudar a aproveitar ao máximo o GitHub Copilot.

Vá para a Lição 11 onde vamos ver como [integrar IA Generativa com Function Calling](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->