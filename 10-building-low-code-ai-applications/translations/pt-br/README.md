# Criando Aplication de IA com Low Code

[![Building Low Code AI Applications](../../images/10-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(Clique na imagem acima para ver o vídeo desta lição)_

## Introdução

Agora que aprendemos como criar aplicações geradoras de imagens, vamos falar sobre low code. A IA generativa pode ser usada em diversas áreas, incluindo low code. Mas o que é low code e como podemos adicionar IA nisso?

A criação de aplicativos e soluções tornou-se mais fácil para desenvolvedores tradicionais e não desenvolvedores por meio do uso de Plataformas de Desenvolvimento Low Code. Essas plataformas possibilitam a criação de aplicativos e soluções com pouco ou nenhum código. Isso é alcançado fornecendo um ambiente visual de desenvolvimento que permite arrastar e soltar componentes para criar aplicativos e soluções. Isso permite que você construa aplicativos e soluções mais rapidamente e com menos recursos. Nesta lição, vamos aprofundar como usar o Low Code e como aprimorar o desenvolvimento de low code com IA usando a Power Platform.

A Power Platform oferece às organizações a oportunidade de capacitar suas equipes a criar suas próprias soluções por meio de um ambiente intuitivo de low-code ou no-code. Esse ambiente ajuda a simplificar o processo de construção de soluções. Com a Power Platform, as soluções podem ser construídas em dias ou semanas, em vez de meses ou anos. A Power Platform consiste em cinco produtos-chave: Power Apps, Power Automate, Power BI, Power Pages e Power Virtual Agents.

### Metas de Aprendizagem

Ao final desta lição, você será capaz de:

- Entender como Copilot funciona na Power Platform.
- Criar um aplicativo de rastreamento de atribuições de estudantes para nossa startup.
- Criar um fluxo de processamento de faturas que usa IA para extrair informações de faturas.
- Aplicar as melhores práticas ao usar o Modelo de IA Create Text with GPT.

As ferramentas e tecnologias que você usará nesta lição são:

- **Power Apps**, para o aplicativo de rastreamento de atribuições de estudantes, que fornece um ambiente de desenvolvimento de low-code para criar aplicativos para rastrear, gerenciar e interagir com dados.
- **Dataverse**, para armazenar os dados do aplicativo de rastreamento de atribuições de estudantes, onde o Dataverse fornecerá uma plataforma de dados de baixo código para armazenar os dados do aplicativo.
- **Power Automate**, para o fluxo de processamento de faturas, onde você terá um ambiente de desenvolvimento de low-code para criar fluxos de trabalho para automatizar o processo de processamento de faturas.
- **AI Builder**, para o Modelo de IA de processamento de faturas, onde você usará modelos de IA predefinidos para processar as faturas para nossa startup.

## IA Generativa na Power Platform

O aprimoramento do desenvolvimento de low-code e aplicativos com IA generativa é uma área-chave para a Power Platform. O objetivo é permitir que todos criam aplicativos, sites, painéis e automatizem processos com IA, _sem exigir qualquer conhecimento em ciência de dados_. Esse objetivo é alcançado integrando a IA generativa na experiência de desenvolvimento de low-code na Power Platform na forma de Copilot e AI Builder.

### Como isso funciona?

Copilot é um assistente de IA que permite que você crie soluções da Power Platform descrevendo seus requisitos em uma série de etapas de conversação usando linguagem natural. Você pode, por exemplo, instruir seu assistente de IA a declarar quais campos seu aplicativo usará e ele criará tanto o aplicativo quanto o modelo de dados subjacente, ou você poderia especificar como configurar um fluxo no Power Automate.

Você pode usar as funcionalidades orientadas pelo Copilot como um recurso nas telas do seu aplicativo para permitir que os usuários descubram insights por meio de interações conversacionais.

O AI Builder é uma capacidade de IA de baixo código disponível na Power Platform que permite que você use Modelos de IA para ajudá-lo a automatizar processos e prever resultados. Com o AI Builder, você pode trazer IA para seus aplicativos e fluxos que se conectam aos seus dados no Dataverse ou em várias fontes de dados em nuvem, como SharePoint, OneDrive ou Azure.

O Copilot está disponível em todos os produtos da Power Platform: Power Apps, Power Automate, Power BI, Power Pages e Power Virtual Agents. O AI Builder está disponível no Power Apps e Power Automate. Nesta lição, vamos nos concentrar em como usar Copilot e AI Builder no Power Apps e Power Automate para criar uma solução para nossa startup educacional.

### Copilot no Power Apps

Como parte da Power Platform, o Power Apps fornece um ambiente de desenvolvimento de low-code para criar aplicativos para rastrear, gerenciar e interagir com dados. É uma suíte de serviços de desenvolvimento de aplicativos com uma plataforma de dados escalável e a capacidade de se conectar a serviços em nuvem e dados locais. O Power Apps permite que você construa aplicativos que são executados em navegadores, tablets e telefones, e podem ser compartilhados com colegas. O Power Apps facilita os usuários no desenvolvimento de aplicativos com uma interface simples, para que cada usuário de negócios ou desenvolvedor profissional possa criar aplicativos personalizados. A experiência de desenvolvimento de aplicativos também é aprimorada com IA generativa por meio do Copilot.

O recurso de assistente de IA Copilot no Power Apps permite que você descreva que tipo de aplicativo você precisa e que informações deseja que seu aplicativo rastreie, colete ou exiba. O Copilot então gera um aplicativo Canvas responsivo com base na sua descrição. Você pode personalizar o aplicativo conforme suas necessidades. O AI Copilot também gera e sugere uma Tabela Dataverse com os campos que você precisa para armazenar os dados que deseja rastrear e alguns dados de exemplo. Vamos examinar o que é o Dataverse e como você pode usá-lo no Power Apps nesta lição mais tarde. Você pode, então, personalizar a tabela para atender às suas necessidades usando o AI Copilot por meio de etapas de conversação. Este recurso está prontamente disponível na tela inicial do Power Apps.

### Copilot no Power Automate

Como parte da Power Platform, o Power Automate permite que os usuários criem fluxos de trabalho automatizados entre aplicativos e serviços. Ele ajuda a automatizar processos de negócios repetitivos, como comunicação, coleta de dados e aprovações de decisões. Sua interface simples permite que usuários com qualquer competência técnica (de iniciantes a desenvolvedores experientes) automatizem tarefas de trabalho. A experiência de desenvolvimento de fluxo de trabalho também é aprimorada com IA generativa por meio do Copilot.

O recurso de assistente de IA Copilot no Power Automate permite que você descreva que tipo de fluxo você precisa e quais ações deseja que seu fluxo execute. O Copilot, então, gera um fluxo com base na sua descrição. Você pode personalizar o fluxo conforme suas necessidades. O AI Copilot também gera e sugere as ações necessárias para realizar a tarefa que você deseja automatizar. Vamos examinar o que são os fluxos e como você pode usá-los no Power Automate nesta lição mais tarde. Você pode, então, personalizar as ações para atender às suas necessidades usando o AI Copilot por meio de etapas de conversação. Este recurso está prontamente disponível na tela inicial do Power Automate.

## Atribuição: gerenciar atribuições de estudantes e faturas para nossa startup, usando Copilot

Nossa startup fornece cursos online para estudantes. A startup cresceu rapidamente e está enfrentando dificuldades para acompanhar a demanda por seus cursos. A startup contratou você como desenvolvedor da Power Platform para ajudá-los a criar uma solução de baixo código para ajudá-los a gerenciar suas atribuições de estudantes e faturas. Sua solução deve ser capaz de ajudá-los a rastrear e gerenciar as atribuições de estudantes por meio de um aplicativo e automatizar o processo de processamento de faturas por meio de um fluxo. Foi solicitado a você que use a IA generativa para desenvolver a solução.

Quando estiver começando a usar o Copilot, você pode usar a [Biblioteca de Prompts do Power Platform Copilot](https://pnp.github.io/powerplatform-prompts/?WT.mc_id=academic-109639-somelezediko) para começar com os prompts. Esta biblioteca contém uma lista de prompts que você pode usar para criar aplicativos e fluxos com Copilot. Você também pode usar os prompts na biblioteca para ter uma ideia de como descrever seus requisitos para o Copilot.

### Criando um Aplicativo de Rastreamento de Atribuições de Estudantes para Nossa Startup

Os educadores em nossa startup têm tido dificuldades para acompanhar as atribuições de estudantes. Eles têm usado uma planilha para rastrear as atribuições, mas isso tem se tornado difícil de gerenciar à medida que o número de estudantes aumentou. Eles pediram a você que construa um aplicativo que os ajude a rastrear e gerenciar as atribuições de estudantes. O aplicativo deve permitir que eles adicionem novas atribuições, vejam atribuições, atualizem atribuições e excluam atribuições. O aplicativo também deve permitir que educadores e estudantes vejam as atribuições que foram avaliadas e aquelas que ainda não foram avaliadas.

Você criará o aplicativo usando Copilot no Power Apps seguindo as etapas abaixo:

1. Acesse a [tela inicial do Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Use a área de texto na tela inicial para descrever o aplicativo que deseja criar. Por exemplo, **_Quero criar um aplicativo para rastrear e gerenciar as atribuições de estudantes_**. Clique no botão **Enviar** para enviar o prompt ao AI Copilot.

![Descreva o aplicativo que deseja criar](../../images/copilot-chat-prompt-powerapps.png?WT.mc_id=academic-105485-koreyst)

1. The AI Copilot will suggest a Dataverse Table with the fields you need to store the data you want to track and some sample data. You can then customize the table to meet your needs using the AI Copilot assistant feature through conversational steps.

   > **Important**: Dataverse is the underlying data platform for Power Platform. It is a low-code data platform for storing the app's data. It is a fully managed service that securely stores data in the Microsoft Cloud and is provisioned within your Power Platform environment. It comes with built-in data governance capabilities, such as data classification, data lineage, fine-grained access control, and more. You can learn more about Dataverse [here](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Suggested fields in your new table](../../images/copilot-dataverse-table-powerapps.png?WT.mc_id=academic-105485-koreyst)

1. Os educadores desejam enviar e-mails aos alunos que enviaram suas atribuições para mantê-los atualizados sobre o progresso de suas tarefas. Você pode usar o Copilot para adicionar um novo campo à tabela para armazenar o e-mail do aluno. Por exemplo, você pode usar o seguinte comando para adicionar um novo campo à tabela: **_Quero adicionar uma coluna para armazenar o e-mail do aluno_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

![Adicionando um novo campo](../../images/copilot-new-column.png?WT.mc_id=academic-105485-koreyst)

1. O AI Copilot gerará um novo campo e você poderá personalizá-lo conforme suas necessidades.

1. Quando terminar com a tabela, clique no botão **Criar aplicativo** para criar o aplicativo.

1. O AI Copilot gerará um aplicativo Canvas responsivo com base na sua descrição. Você pode, então, personalizar o aplicativo conforme suas necessidades.

1. Para que os educadores possam enviar e-mails aos alunos, você pode usar o Copilot para adicionar uma nova tela ao aplicativo. Por exemplo, você pode usar o seguinte comando para adicionar uma nova tela ao aplicativo: **_Quero adicionar uma tela para enviar e-mails aos alunos_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

![Adicionando uma nova tela via comando](../../images/copilot-new-screen.png?WT.mc_id=academic-105485-koreyst)

1. O AI Copilot gerará uma nova tela e você poderá personalizá-la conforme suas necessidades.

1. Quando terminar com o aplicativo, clique no botão **Salvar** para salvar o aplicativo.

1. Para compartilhar o aplicativo com os educadores, clique no botão **Compartilhar** e depois clique novamente no botão **Compartilhar**. Você pode, então, compartilhar o aplicativo com os educadores inserindo seus endereços de e-mail.

> **Dever de Casa**: O aplicativo que você acabou de criar é um bom começo, mas pode ser melhorado. Com o recurso de e-mail, os educadores só podem enviar e-mails aos alunos manualmente digitando seus e-mails. Você pode usar o Copilot para criar uma automação que permitirá aos educadores enviar e-mails aos alunos automaticamente quando eles enviarem suas atribuições? Sua dica é que, com o comando certo, você pode usar o Copilot no Power Automate para criar isso.

### Criar uma Tabela de Informações de Faturas para Nossa Startup

A equipe financeira de nossa startup tem tido dificuldades para acompanhar as faturas. Eles têm usado uma planilha para rastrear as faturas, mas isso tem se tornado difícil de gerenciar à medida que o número de faturas aumentou. Eles pediram a você que construa uma tabela que os ajude a armazenar, rastrear e gerenciar as informações das faturas que receberam. A tabela deve ser usada para criar uma automação que extrairá todas as informações da fatura e as armazenará na tabela. A tabela também deve permitir que a equipe financeira veja as faturas que foram pagas e aquelas que ainda não foram pagas.

A Power Platform possui uma plataforma de dados subjacente chamada Dataverse que permite armazenar os dados para seus aplicativos e soluções. O Dataverse fornece uma plataforma de dados de baixo código para armazenar os dados do aplicativo. É um serviço totalmente gerenciado que armazena dados com segurança na nuvem da Microsoft e é provisionado dentro do seu ambiente Power Platform. Ele vem com capacidades integradas de governança de dados, como classificação de dados, linhagem de dados, controle de acesso fino e muito mais. Você pode aprender mais [sobre o Dataverse aqui](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Por que devemos usar o Dataverse para nossa startup? As tabelas padrão e personalizadas dentro do Dataverse fornecem uma opção de armazenamento segura e baseada na nuvem para seus dados. Tabelas permitem que você armazene diferentes tipos de dados, semelhante a como você pode usar várias planilhas em uma única pasta de trabalho do Excel. Você pode usar tabelas para armazenar dados específicos da sua organização ou necessidade de negócios. Alguns dos benefícios que nossa startup obterá ao usar o Dataverse incluem, mas não estão limitados a:

- **Fácil de gerenciar**: Tanto os metadados quanto os dados são armazenados na nuvem, então você não precisa se preocupar com os detalhes de como eles são armazenados ou gerenciados. Você pode se concentrar em criar seus aplicativos e soluções.

- **Seguro**: O Dataverse fornece uma opção de armazenamento segura e baseada na nuvem para seus dados. Você pode controlar quem tem acesso aos dados em suas tabelas e como podem acessá-los usando segurança baseada em funções.

- **Metadados ricos**: Tipos de dados e relacionamentos são usados diretamente dentro do Power Apps

- **Lógica e validação**: Você pode usar regras de negócios, campos calculados e regras de validação para impor lógica de negócios e manter a precisão dos dados.

Agora que você sabe o que é o Dataverse e por que deve usá-lo, vamos ver como você pode usar o Copilot para criar uma tabela no Dataverse para atender aos requisitos de nossa equipe financeira.

> **Nota** : Você usará esta tabela na próxima seção para criar uma automação que extrairá todas as informações da fatura e as armazenará na tabela.

Para criar uma tabela no Dataverse usando o Copilot, siga as etapas abaixo:

1. Acesse a [tela inicial do Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Na barra de navegação à esquerda, selecione **Tabelas** e, em seguida, clique em **Descrever a nova tabela**.

![Selecionar nova tabela](../../images/describe-new-table.png?WT.mc_id=academic-105485-koreyst)

1. Na tela **Descrever a nova tabela**, use a área de texto para descrever a tabela que deseja criar. Por exemplo, **_Quero criar uma tabela para armazenar informações de fatura_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

![Descrever a tabela](../../images/copilot-chat-prompt-dataverse.png?WT.mc_id=academic-105485-koreyst)

1. O AI Copilot sugerirá uma Tabela Dataverse com os campos necessários para armazenar os dados que você deseja rastrear e alguns dados de exemplo. Você pode, então, personalizar a tabela para atender às suas necessidades usando o recurso de assistente AI Copilot por meio de etapas de conversação.

![Tabela Dataverse sugerida](../../images/copilot-dataverse-table.png?WT.mc_id=academic-105485-koreyst)

1. A equipe financeira deseja enviar um e-mail ao fornecedor para atualizá-lo com o status atual de sua fatura. Você pode usar o Copilot para adicionar um novo campo à tabela para armazenar o e-mail do fornecedor. Por exemplo, você pode usar o seguinte comando para adicionar um novo campo à tabela: **_Quero adicionar uma coluna para armazenar o e-mail do fornecedor_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

1. O AI Copilot gerará um novo campo e você poderá personalizá-lo conforme suas necessidades.

1. Quando terminar com a tabela, clique no botão **Criar** para criar a tabela.

## Modelos de IA na Power Platform com o AI Builder

O AI Builder é uma capacidade de IA de baixo código disponível na Power Platform que permite que você use Modelos de IA para automatizar processos e prever resultados. Com o AI Builder, você pode adicionar IA aos seus aplicativos e fluxos que se conectam aos seus dados no Dataverse ou em várias fontes de dados em nuvem, como SharePoint, OneDrive ou Azure.

## Modelos de IA Pré-Criados vs Modelos de IA Personalizados

O AI Builder fornece dois tipos de Modelos de IA: Modelos de IA Pré-Construídos e Modelos de IA Personalizados. Os Modelos de IA Pré-Construídos estão prontos para uso, treinados pela Microsoft e disponíveis na Power Platform. Eles ajudam a adicionar inteligência aos seus aplicativos e fluxos sem a necessidade de coletar dados e, em seguida, criar, treinar e publicar seus próprios modelos. Você pode usar esses modelos para automatizar processos e prever resultados.

Alguns dos Modelos de IA Pré-Construídos disponíveis na Power Platform incluem:

- **Extração de Frases-Chave**: Este modelo extrai frases-chave de texto.
- **Detecção de Idioma**: Este modelo detecta o idioma de um texto.
- **Análise de Sentimento**: Este modelo detecta sentimento positivo, negativo, neutro ou misto em texto.
- **Leitor de Cartões de Visita**: Este modelo extrai informações de cartões de visita.
- **Reconhecimento de Texto**: Este modelo extrai texto de imagens.
- **Detecção de Objetos**: Este modelo detecta e extrai objetos de imagens.
- **Processamento de Formulários**: Este modelo extrai informações de formulários.
- **Processamento de Faturas**: Este modelo extrai informações de faturas.

Com Modelos de IA Personalizados, você pode trazer seu próprio modelo para o AI Builder, permitindo que ele funcione como qualquer modelo personalizado do AI Builder, permitindo que você treine o modelo usando seus próprios dados. Você pode usar esses modelos para automatizar processos e prever resultados tanto no Power Apps quanto no Power Automate. Ao usar seu próprio modelo, existem limitações que se aplicam. Leia mais sobre essas [limitações](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![Modelos do AI Builder](../../images/ai-builder-models.png?WT.mc_id=academic-105485-koreyst)

## Tarefa #2 - Criar um Fluxo de Processamento de Faturas para Nossa Startup

A equipe financeira tem tido dificuldades para processar faturas. Eles têm usado uma planilha para rastrear as faturas, mas isso tem se tornado difícil de gerenciar à medida que o número de faturas aumentou. Eles pediram a você que construa um fluxo que os ajudará a processar faturas usando IA. O fluxo deve permitir que eles extraiam informações das faturas e armazenem as informações em uma tabela do Dataverse. O fluxo também deve permitir que eles enviem um e-mail à equipe financeira com as informações extraídas.

Agora que você sabe o que é o AI Builder e por que deve usá-lo, vamos ver como você pode usar o Modelo de IA de Processamento de Faturas no AI Builder, que cobrimos anteriormente, para criar um fluxo que ajudará a equipe financeira a processar faturas.

Para criar um fluxo que ajudará a equipe financeira a processar faturas usando o Modelo de IA de Processamento de Faturas no AI Builder, siga as etapas abaixo:

1. Acesse a [tela inicial do Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Use a área de texto na tela inicial para descrever o fluxo que você deseja criar. Por exemplo, **_Processar uma fatura quando ela chegar à minha caixa de correio_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

   ![Copilot power automate](../../images/copilot-chat-prompt-powerautomate.png?WT.mc_id=academic-105485-koreyst)

3. O AI Copilot sugerirá as ações que você precisa realizar para a tarefa que deseja automatizar. Você pode clicar no botão **Próximo** para passar para as próximas etapas.

4. Na próxima etapa, o Power Automate solicitará que você configure as conexões necessárias para o fluxo. Quando terminar, clique no botão **Criar fluxo** para criar o fluxo.

5. O AI Copilot gerará um fluxo e você poderá personalizá-lo para atender às suas necessidades.

6. Atualize o acionador do fluxo e defina a **Pasta** para a pasta onde as faturas serão armazenadas. Por exemplo, você pode definir a pasta como **Caixa de entrada**. Clique em **Mostrar opções avançadas** e defina **Apenas com Anexos** como **Sim**. Isso garantirá que o fluxo só seja executado quando um e-mail com um anexo for recebido na pasta.

7. Remova as seguintes ações do fluxo: **HTML para texto**, **Compor**, **Compor 2**, **Compor 3** e **Compor 4**, pois você não as usará.

8. Remova a ação **Condição** do fluxo, pois você não a usará. Deve se parecer com a captura de tela a seguir:

   ![Power Automate, remover ações](../../images/powerautomate-remove-actions.png?WT.mc_id=academic-105485-koreyst)

9. Clique no botão **Adicionar uma ação** e pesquise por **Dataverse**. Selecione a ação **Adicionar uma nova linha**.

10. Na ação **Extrair informações das faturas**, atualize o **Arquivo da Fatura** para apontar para o **Conteúdo do Anexo** do e-mail. Isso garantirá que o fluxo extraia informações do anexo da fatura.

11. Selecione a **Tabela** que você criou anteriormente. Por exemplo, você pode selecionar a tabela **Informações da Fatura**. Escolha o conteúdo dinâmico da ação anterior para preencher os seguintes campos:

    - ID
    - Valor
    - Data
    - Nome
    - Status - Defina o **Status** como **Pendente**.
    - E-mail do Fornecedor - Use o conteúdo dinâmico do **Quando um novo e-mail chega** para o gatilho.

    ![Power Automate, adicionar linha](../../images/powerautomate-add-row.png?WT.mc_id=academic-105485-koreyst)

12. Quando terminar o fluxo, clique no botão **Salvar** para salvar o fluxo. Você pode testar o fluxo enviando um e-mail com uma fatura para a pasta que você especificou no gatilho.

> **Dever de casa**: O fluxo que você acabou de criar é um bom começo. Agora, você precisa pensar em como pode criar uma automação que permitirá que nossa equipe financeira envie um e-mail ao fornecedor para atualizá-lo com o status atual de sua fatura. Sua dica: o fluxo deve ser executado quando o status da fatura mudar.

## Utilize um Modelo de IA de Geração de Texto no Power Automate

O Modelo de IA Criar Texto com GPT no AI Builder permite que você gere texto com base em um prompt e é alimentado pelo Serviço Microsoft Azure OpenAI. Com essa capacidade, você pode incorporar a tecnologia GPT (Generative Pre-Trained Transformer) em seus aplicativos e fluxos para criar uma variedade de fluxos automatizados e aplicativos perspicazes.

Os modelos GPT passam por treinamento extensivo em grandes quantidades de dados, permitindo que eles produzam texto que se assemelha de perto à linguagem humana quando fornecidos com um prompt. Quando integrados à automação de fluxo de trabalho, modelos de IA como o GPT podem ser aproveitados para simplificar e automatizar uma ampla variedade de tarefas.

Por exemplo, você pode criar fluxos para gerar automaticamente texto para uma variedade de casos de uso, como rascunhos de e-mails, descrições de produtos e muito mais. Você também pode usar o modelo para gerar texto para vários aplicativos, como chatbots e aplicativos de atendimento ao cliente que permitem que os agentes de atendimento ao cliente respondam de forma eficaz e eficiente às perguntas dos clientes.

![create a prompt](../../images/create-prompt-gpt.png?WT.mc_id=academic-105485-koreyst)

Para aprender a usar este modelo de IA no Power Automate, passe pelo módulo [Adicionar inteligência com o AI Builder e GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Excelente trabalho! Vamos continuar com o Apredizado!

Após concluir esta lição, confira nossa [coleção de aprendizado de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar seu conhecimento em IA generativa!

Vamos avançar para a Lição 11, onde veremos como [Integrando a IA generativa com chamada de função](../../../11-integrating-with-function-calling/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)!
