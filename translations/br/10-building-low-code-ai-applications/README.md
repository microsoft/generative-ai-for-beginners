<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5ff3b6204a695a117d6f452403c95f7",
  "translation_date": "2025-06-25T18:33:44+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "br"
}
-->
# Construindo Aplicações de IA com Baixo Código

[![Construindo Aplicações de IA com Baixo Código](../../../translated_images/10-lesson-banner.a01ac8fe3fd86310c2e4065c0b3c584879f33b8ce797311821a636992f8a5b2f.br.png)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

## Introdução

Agora que aprendemos a construir aplicações de geração de imagens, vamos falar sobre baixo código. A IA generativa pode ser usada em várias áreas diferentes, incluindo baixo código, mas o que é baixo código e como podemos adicionar IA a ele?

Construir aplicativos e soluções tornou-se mais fácil para desenvolvedores tradicionais e não desenvolvedores através do uso de Plataformas de Desenvolvimento de Baixo Código. As Plataformas de Desenvolvimento de Baixo Código permitem que você construa aplicativos e soluções com pouco ou nenhum código. Isso é alcançado fornecendo um ambiente de desenvolvimento visual que permite arrastar e soltar componentes para construir aplicativos e soluções. Isso permite que você construa aplicativos e soluções mais rapidamente e com menos recursos. Nesta lição, mergulhamos fundo em como usar o Baixo Código e como aprimorar o desenvolvimento de baixo código com IA usando o Power Platform.

O Power Platform oferece às organizações a oportunidade de capacitar suas equipes a construir suas próprias soluções através de um ambiente intuitivo de baixo código ou sem código. Este ambiente ajuda a simplificar o processo de construção de soluções. Com o Power Platform, soluções podem ser construídas em dias ou semanas em vez de meses ou anos. O Power Platform é composto por cinco produtos principais: Power Apps, Power Automate, Power BI, Power Pages e Copilot Studio.

Esta lição cobre:

- Introdução à IA Generativa no Power Platform
- Introdução ao Copilot e como usá-lo
- Usando IA Generativa para construir aplicativos e fluxos no Power Platform
- Compreendendo os Modelos de IA no Power Platform com o AI Builder

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Compreender como o Copilot funciona no Power Platform.

- Construir um Aplicativo de Rastreamento de Tarefas de Alunos para nossa startup educacional.

- Construir um Fluxo de Processamento de Faturas que usa IA para extrair informações de faturas.

- Aplicar melhores práticas ao usar o Modelo de IA de Criação de Texto com GPT.

As ferramentas e tecnologias que você usará nesta lição são:

- **Power Apps**, para o aplicativo de Rastreamento de Tarefas de Alunos, que fornece um ambiente de desenvolvimento de baixo código para construir aplicativos para rastrear, gerenciar e interagir com dados.

- **Dataverse**, para armazenar os dados do aplicativo de Rastreamento de Tarefas de Alunos onde o Dataverse fornecerá uma plataforma de dados de baixo código para armazenar os dados do aplicativo.

- **Power Automate**, para o fluxo de Processamento de Faturas onde você terá um ambiente de desenvolvimento de baixo código para construir fluxos de trabalho para automatizar o processo de Processamento de Faturas.

- **AI Builder**, para o Modelo de IA de Processamento de Faturas onde você usará Modelos de IA pré-construídos para processar as faturas para nossa startup.

## IA Generativa no Power Platform

Aprimorar o desenvolvimento e aplicação de baixo código com IA generativa é uma área de foco chave para o Power Platform. O objetivo é permitir que todos construam aplicativos, sites, painéis e automatizem processos com IA, _sem exigir qualquer expertise em ciência de dados_. Esse objetivo é alcançado integrando a IA generativa na experiência de desenvolvimento de baixo código no Power Platform na forma de Copilot e AI Builder.

### Como isso funciona?

O Copilot é um assistente de IA que permite que você construa soluções no Power Platform descrevendo seus requisitos em uma série de etapas conversacionais usando linguagem natural. Você pode, por exemplo, instruir seu assistente de IA a indicar quais campos seu aplicativo usará e ele criará tanto o aplicativo quanto o modelo de dados subjacente ou você poderia especificar como configurar um fluxo no Power Automate.

Você pode usar funcionalidades dirigidas pelo Copilot como um recurso em suas telas de aplicativos para permitir que os usuários descubram insights através de interações conversacionais.

O AI Builder é uma capacidade de IA de baixo código disponível no Power Platform que permite que você use Modelos de IA para ajudá-lo a automatizar processos e prever resultados. Com o AI Builder você pode trazer IA para seus aplicativos e fluxos que se conectam aos seus dados no Dataverse ou em várias fontes de dados na nuvem, como SharePoint, OneDrive ou Azure.

O Copilot está disponível em todos os produtos do Power Platform: Power Apps, Power Automate, Power BI, Power Pages e Power Virtual Agents. O AI Builder está disponível no Power Apps e Power Automate. Nesta lição, focaremos em como usar o Copilot e o AI Builder no Power Apps e Power Automate para construir uma solução para nossa startup educacional.

### Copilot no Power Apps

Como parte do Power Platform, o Power Apps fornece um ambiente de desenvolvimento de baixo código para construir aplicativos para rastrear, gerenciar e interagir com dados. É um conjunto de serviços de desenvolvimento de aplicativos com uma plataforma de dados escalável e a capacidade de se conectar a serviços na nuvem e dados locais. O Power Apps permite que você construa aplicativos que funcionem em navegadores, tablets e telefones, e podem ser compartilhados com colegas de trabalho. O Power Apps facilita para os usuários o desenvolvimento de aplicativos com uma interface simples, para que todo usuário de negócios ou desenvolvedor profissional possa construir aplicativos personalizados. A experiência de desenvolvimento de aplicativos também é aprimorada com a IA Generativa através do Copilot.

O recurso de assistente de IA do copilot no Power Apps permite que você descreva que tipo de aplicativo você precisa e que informações você quer que seu aplicativo rastreie, colete ou mostre. O Copilot então gera um aplicativo Canvas responsivo com base na sua descrição. Você pode então personalizar o aplicativo para atender às suas necessidades. O AI Copilot também gera e sugere uma Tabela do Dataverse com os campos necessários para armazenar os dados que você quer rastrear e alguns dados de amostra. Vamos ver o que é o Dataverse e como você pode usá-lo no Power Apps nesta lição mais adiante. Você pode então personalizar a tabela para atender às suas necessidades usando o recurso de assistente AI Copilot através de etapas conversacionais. Este recurso está prontamente disponível na tela inicial do Power Apps.

### Copilot no Power Automate

Como parte do Power Platform, o Power Automate permite que os usuários criem fluxos de trabalho automatizados entre aplicativos e serviços. Ele ajuda a automatizar processos de negócios repetitivos, como comunicação, coleta de dados e aprovações de decisões. Sua interface simples permite que usuários com qualquer competência técnica (de iniciantes a desenvolvedores experientes) automatizem tarefas de trabalho. A experiência de desenvolvimento de fluxo de trabalho também é aprimorada com a IA Generativa através do Copilot.

O recurso de assistente de IA do copilot no Power Automate permite que você descreva que tipo de fluxo você precisa e quais ações você quer que seu fluxo execute. O Copilot então gera um fluxo com base na sua descrição. Você pode então personalizar o fluxo para atender às suas necessidades. O AI Copilot também gera e sugere as ações necessárias para executar a tarefa que você quer automatizar. Vamos ver o que são fluxos e como você pode usá-los no Power Automate nesta lição mais adiante. Você pode então personalizar as ações para atender às suas necessidades usando o recurso de assistente AI Copilot através de etapas conversacionais. Este recurso está prontamente disponível na tela inicial do Power Automate.

## Tarefa: Gerenciar tarefas de alunos e faturas para nossa startup, usando o Copilot

Nossa startup oferece cursos online para estudantes. A startup cresceu rapidamente e agora está lutando para acompanhar a demanda por seus cursos. A startup contratou você como desenvolvedor do Power Platform para ajudá-los a construir uma solução de baixo código para ajudá-los a gerenciar suas tarefas de alunos e faturas. A solução deles deve ser capaz de ajudá-los a rastrear e gerenciar as tarefas dos alunos através de um aplicativo e automatizar o processo de processamento de faturas através de um fluxo de trabalho. Você foi solicitado a usar IA Generativa para desenvolver a solução.

Quando você está começando a usar o Copilot, pode usar a [Biblioteca de Prompts do Copilot do Power Platform](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) para começar com os prompts. Esta biblioteca contém uma lista de prompts que você pode usar para construir aplicativos e fluxos com o Copilot. Você também pode usar os prompts na biblioteca para ter uma ideia de como descrever seus requisitos para o Copilot.

### Construir um Aplicativo de Rastreamento de Tarefas de Alunos para Nossa Startup

Os educadores da nossa startup têm lutado para manter o controle das tarefas dos alunos. Eles têm usado uma planilha para rastrear as tarefas, mas isso se tornou difícil de gerenciar à medida que o número de alunos aumentou. Eles pediram para você construir um aplicativo que os ajude a rastrear e gerenciar as tarefas dos alunos. O aplicativo deve permitir que eles adicionem novas tarefas, visualizem tarefas, atualizem tarefas e excluam tarefas. O aplicativo também deve permitir que educadores e alunos visualizem as tarefas que foram avaliadas e as que não foram avaliadas.

Você construirá o aplicativo usando o Copilot no Power Apps seguindo as etapas abaixo:

1. Navegue até a tela inicial do [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Use a área de texto na tela inicial para descrever o aplicativo que você quer construir. Por exemplo, **_Quero construir um aplicativo para rastrear e gerenciar tarefas de alunos_**. Clique no botão **Enviar** para enviar o prompt para o AI Copilot.

![Descreva o aplicativo que você quer construir](../../../translated_images/copilot-chat-prompt-powerapps.84250f341d060830a296b68512e6b3b3aa3a4559f4f1c2d7bafeba8ad3fcd17a.br.png)

1. O AI Copilot sugerirá uma Tabela do Dataverse com os campos necessários para armazenar os dados que você quer rastrear e alguns dados de amostra. Você pode então personalizar a tabela para atender às suas necessidades usando o recurso de assistente AI Copilot através de etapas conversacionais.

   > **Importante**: O Dataverse é a plataforma de dados subjacente para o Power Platform. É uma plataforma de dados de baixo código para armazenar os dados do aplicativo. É um serviço totalmente gerenciado que armazena dados de forma segura na Nuvem Microsoft e é provisionado dentro do seu ambiente do Power Platform. Ele vem com capacidades de governança de dados embutidas, como classificação de dados, linhagem de dados, controle de acesso detalhado, e mais. Você pode saber mais sobre o Dataverse [aqui](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Campos sugeridos na sua nova tabela](../../../translated_images/copilot-dataverse-table-powerapps.f4cc07b5d5f9327bd3783dd288debb2a959ce3320107512e235137aebd8a1a4c.br.png)

1. Os educadores querem enviar e-mails para os alunos que enviaram suas tarefas para mantê-los atualizados sobre o progresso de suas tarefas. Você pode usar o Copilot para adicionar um novo campo à tabela para armazenar o e-mail do aluno. Por exemplo, você pode usar o seguinte prompt para adicionar um novo campo à tabela: **_Quero adicionar uma coluna para armazenar o e-mail do aluno_**. Clique no botão **Enviar** para enviar o prompt para o AI Copilot.

![Adicionando um novo campo](../../../translated_images/copilot-new-column.35e15ff21acaf2745965d427b130f2be772f0484835b44fe074d496b1a455f2a.br.png)

1. O AI Copilot gerará um novo campo e você poderá então personalizar o campo para atender às suas necessidades.

1. Depois de terminar com a tabela, clique no botão **Criar aplicativo** para criar o aplicativo.

1. O AI Copilot gerará um aplicativo Canvas responsivo com base na sua descrição. Você pode então personalizar o aplicativo para atender às suas necessidades.

1. Para que os educadores enviem e-mails para os alunos, você pode usar o Copilot para adicionar uma nova tela ao aplicativo. Por exemplo, você pode usar o seguinte prompt para adicionar uma nova tela ao aplicativo: **_Quero adicionar uma tela para enviar e-mails para os alunos_**. Clique no botão **Enviar** para enviar o prompt para o AI Copilot.

![Adicionando uma nova tela via uma instrução de prompt](../../../translated_images/copilot-new-screen.2e0bef7132a173928bc621780b39799e03982d315cb5a9ff75a34b08054641d4.br.png)

1. O AI Copilot gerará uma nova tela e você poderá então personalizar a tela para atender às suas necessidades.

1. Depois de terminar com o aplicativo, clique no botão **Salvar** para salvar o aplicativo.

1. Para compartilhar o aplicativo com os educadores, clique no botão **Compartilhar** e depois clique novamente no botão **Compartilhar**. Você poderá então compartilhar o aplicativo com os educadores inserindo seus endereços de e-mail.

> **Seu dever de casa**: O aplicativo que você acabou de construir é um bom começo, mas pode ser melhorado. Com o recurso de e-mail, os educadores só podem enviar e-mails para os alunos manualmente, tendo que digitar seus e-mails. Você pode usar o Copilot para construir uma automação que permitirá que os educadores enviem e-mails automaticamente para os alunos quando eles enviarem suas tarefas? Sua dica é que com o prompt certo você pode usar o Copilot no Power Automate para construir isso.

### Construir uma Tabela de Informações de Faturas para Nossa Startup

A equipe financeira da nossa startup tem tido dificuldades para manter o controle das faturas. Eles têm usado uma planilha para rastrear as faturas, mas isso se tornou difícil de gerenciar à medida que o número de faturas aumentou. Eles pediram para você construir uma tabela que os ajude a armazenar, rastrear e gerenciar as informações das faturas que receberam. A tabela deve ser usada para construir uma automação que extrairá todas as informações das faturas e as armazenará na tabela. A tabela também deve permitir que a equipe financeira visualize as faturas que foram pagas e as que não foram pagas.

O Power Platform possui uma plataforma de dados subjacente chamada Dataverse que permite armazenar os dados dos seus aplicativos e soluções. O Dataverse fornece uma plataforma de dados de baixo código para armazenar os dados do aplicativo. É um serviço totalmente gerenciado que armazena dados de forma segura na Nuvem Microsoft e é provisionado dentro do seu ambiente do Power Platform. Ele vem com capacidades de governança de dados embutidas, como classificação de dados, linhagem de dados, controle de acesso detalhado, e mais. Você pode saber mais [sobre o Dataverse aqui](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Por que devemos usar o Dataverse para nossa startup? As tabelas padrão e personalizadas dentro do Dataverse fornecem uma opção de armazenamento segura e baseada na nuvem para seus dados. As tabelas permitem que você armazene diferentes tipos de dados, semelhante a como você pode usar várias planilhas em uma única pasta de trabalho do Excel. Você pode usar tabelas para armazenar dados que são específicos para as necessidades da sua organização ou negócios. Alguns dos benefícios que nossa startup obterá ao usar o Dataverse incluem, mas não se limitam a:

- **Fácil de gerenciar**: Tanto os metadados quanto os dados são armazenados na nuvem, então você não precisa se preocupar com os detalhes de como eles são armazenados ou gerenciados. Você pode se concentrar em construir seus aplicativos e soluções.

- **Seguro**: O Dataverse fornece uma opção de armazenamento segura e baseada na nuvem para seus dados. Você pode controlar quem tem acesso aos dados em suas tabelas e como eles podem acessá-los usando segurança baseada em função.

- **Metadados ricos**: Tipos de dados e relacionamentos são usados diretamente dentro do Power Apps.

- **Lógica e validação**: Você pode usar regras de negócios, campos calculados e regras de validação para impor lógica de negócios e manter a precisão dos dados.

Agora que você sabe o que é o Dataverse e por que deve usá-lo, vamos ver como você pode usar o Copilot para criar uma tabela no Dataverse para atender aos requisitos da nossa equipe financeira.

> **Nota**: Você usará esta tabela na próxima seção para construir uma automação que extrairá todas as informações das faturas e as armazenará na tabela.
Para criar uma tabela no Dataverse usando o Copilot, siga os passos abaixo: 1. Navegue até a tela inicial do [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst). 2. Na barra de navegação à esquerda, selecione **Tabelas** e depois clique em **Descrever a nova Tabela**. ![Selecione nova tabela](../../../translated_images/describe-new-table.0792373eb757281e3c5f542f84cad3b5208bfe0e5c4a7786dd2bd31aa848a23c.br.png) 1. Na tela **Descrever a nova Tabela**, use a área de texto para descrever a tabela que você quer criar. Por exemplo, **_Quero criar uma tabela para armazenar informações de faturas_**. Clique no botão **Enviar** para enviar o prompt para o AI Copilot. ![Descreva a tabela](../../../translated_images/copilot-chat-prompt-dataverse.feb2f81e5872b9d2b05d45d11bb6830e0f2ef6a2d4742413bc9a1e50a45bbb89.br.png) 1. O AI Copilot sugerirá uma Tabela do Dataverse com os campos necessários para armazenar os dados que você quer rastrear e alguns dados de amostra. Você pode então personalizar a tabela para atender às suas necessidades usando o recurso de assistente AI Copilot através de etapas conversacionais. ![Tabela do Dataverse sugerida](../../../translated_images/copilot-dataverse-table.b3bc936091324d9db1e943d640df1c7a7df598e66d30f5b8a2999048e26a5073.br.png) 1. A equipe financeira quer enviar um e-mail para o fornecedor para atualizá-los com o status atual de sua fatura. Você pode usar o Copilot para adicionar um novo campo à tabela para armazenar o e-mail do fornecedor. Por exemplo, você pode usar o seguinte prompt para adicionar um novo campo à tabela: **_Quero adicionar uma coluna para armazenar o e-mail do fornecedor_**. Clique no botão **Enviar** para enviar o prompt para o AI Copilot. 1. O AI Copilot gerará um novo campo e você poderá então personalizar o campo para atender às suas necessidades. 1. Depois de terminar com a tabela, clique no botão **Criar** para criar a tabela. ## Modelos de IA no Power Platform com AI Builder O AI Builder é uma capacidade de IA de baixo código disponível no Power Platform que permite que você use Modelos de IA para ajudá-lo a automatizar processos e prever resultados. Com o AI Builder você pode trazer IA para seus aplicativos e fluxos que se conect
um texto. - **Análise de Sentimento**: Este modelo detecta sentimento positivo, negativo, neutro ou misto em texto. - **Leitor de Cartões de Visita**: Este modelo extrai informações de cartões de visita. - **Reconhecimento de Texto**: Este modelo extrai texto de imagens. - **Detecção de Objetos**: Este modelo detecta e extrai objetos de imagens. - **Processamento de Documentos**: Este modelo extrai informações de formulários. - **Processamento de Faturas**: Este modelo extrai informações de faturas. Com Modelos de IA Personalizados, você pode trazer seu próprio modelo para o AI Builder para que ele funcione como qualquer modelo personalizado do AI Builder, permitindo que você treine o modelo usando seus próprios dados. Você pode usar esses modelos para automatizar processos e prever resultados tanto no Power Apps quanto no Power Automate. Ao usar seu próprio modelo, existem limitações que se aplicam. Leia mais sobre essas [limitações](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst). ![Modelos do AI Builder](../../../translated_images/ai-builder-models.8069423b84cfc47f6bb989bc3cd0584b5b2471c80fad80bf504d356928a08c9c.br.png)

## Tarefa #2 - Criar um Fluxo de Processamento de Faturas para Nossa Startup

A equipe financeira tem tido dificuldades para processar faturas. Eles estavam usando uma planilha para acompanhar as faturas, mas isso se tornou difícil de gerenciar à medida que o número de faturas aumentou. Eles pediram que você criasse um fluxo de trabalho que os ajude a processar faturas usando IA. O fluxo de trabalho deve permitir que eles extraiam informações das faturas e armazenem as informações em uma tabela do Dataverse. O fluxo de trabalho também deve permitir que eles enviem um e-mail para a equipe financeira com as informações extraídas.

Agora que você sabe o que é o AI Builder e por que deve usá-lo, vamos ver como você pode usar o Modelo de IA de Processamento de Faturas no AI Builder, que abordamos anteriormente, para criar um fluxo de trabalho que ajude a equipe financeira a processar faturas.

Para criar um fluxo de trabalho que ajude a equipe financeira a processar faturas usando o Modelo de IA de Processamento de Faturas no AI Builder, siga os passos abaixo:

1. Navegue até a tela inicial do [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).
2. Use a área de texto na tela inicial para descrever o fluxo de trabalho que você deseja criar. Por exemplo, **_Processar uma fatura quando ela chegar na minha caixa de entrada_**. Clique no botão **Enviar** para enviar o prompt para o AI Copilot. ![Copilot power automate](../../../translated_images/copilot-chat-prompt-powerautomate.f377e478cc8412de4394fab09e5b72f97b3fc9312526b516ded426102f51c30d.br.png)
3. O AI Copilot sugerirá as ações que você precisa realizar para a tarefa que deseja automatizar. Você pode clicar no botão **Próximo** para passar para as próximas etapas.
4. Na próxima etapa, o Power Automate solicitará que você configure as conexões necessárias para o fluxo. Quando terminar, clique no botão **Criar fluxo** para criar o fluxo.
5. O AI Copilot gerará um fluxo e você poderá personalizar o fluxo para atender às suas necessidades.
6. Atualize o gatilho do fluxo e defina a **Pasta** para a pasta onde as faturas serão armazenadas. Por exemplo, você pode definir a pasta como **Caixa de Entrada**. Clique em **Mostrar opções avançadas** e defina **Apenas com Anexos** como **Sim**. Isso garantirá que o fluxo só seja executado quando um e-mail com um anexo for recebido na pasta.
7. Remova as seguintes ações do fluxo: **HTML para texto**, **Compor**, **Compor 2**, **Compor 3** e **Compor 4** porque você não usará elas.
8. Remova a ação **Condição** do fluxo porque você não a usará. Deve ficar como na captura de tela a seguir: ![power automate, remover ações](../../../translated_images/powerautomate-remove-actions.7216392fe684ceba4b73c6383edd1cc5e7ded11afd0ca812052a11487d049ef8.br.png)
9. Clique no botão **Adicionar uma ação** e procure por **Dataverse**. Selecione a ação **Adicionar uma nova linha**.
10. Na ação **Extrair Informações de faturas**, atualize o **Arquivo de Fatura** para apontar para o **Conteúdo do Anexo** do e-mail. Isso garantirá que o fluxo extraia informações do anexo da fatura.
11. Selecione a **Tabela** que você criou anteriormente. Por exemplo, você pode selecionar a tabela **Informações da Fatura**. Escolha o conteúdo dinâmico da ação anterior para preencher os seguintes campos:
   - ID
   - Valor
   - Data
   - Nome
   - Status
   - Defina o **Status** como **Pendente**.
   - E-mail do Fornecedor
   - Use o conteúdo dinâmico **De** do gatilho **Quando um novo e-mail chegar**. ![power automate adicionar linha](../../../translated_images/powerautomate-add-row.5edce45e5dd3d51e5152688dc140ad43e1423e7a9fef9a206f82a7965ea68d73.br.png)
12. Quando terminar o fluxo, clique no botão **Salvar** para salvar o fluxo. Você pode então testar o fluxo enviando um e-mail com uma fatura para a pasta que você especificou no gatilho.

> **Seu dever de casa**: O fluxo que você acabou de construir é um bom começo, agora você precisa pensar em como pode construir uma automação que permita que nossa equipe financeira envie um e-mail ao fornecedor para atualizá-lo com o status atual de sua fatura. Sua dica: o fluxo deve ser executado quando o status da fatura mudar.

## Use um Modelo de IA de Geração de Texto no Power Automate

O Modelo de IA Criar Texto com GPT no AI Builder permite que você gere texto com base em um prompt e é alimentado pelo Microsoft Azure OpenAI Service. Com essa capacidade, você pode incorporar a tecnologia GPT (Transformador Generativo Pré-Treinado) em seus aplicativos e fluxos para construir uma variedade de fluxos automatizados e aplicativos perspicazes.

Os modelos GPT passam por um treinamento extenso em grandes quantidades de dados, permitindo que produzam texto que se assemelha muito à linguagem humana quando fornecidos com um prompt. Quando integrados à automação de fluxos de trabalho, modelos de IA como o GPT podem ser aproveitados para agilizar e automatizar uma ampla gama de tarefas.

Por exemplo, você pode construir fluxos para gerar automaticamente texto para uma variedade de casos de uso, como: rascunhos de e-mails, descrições de produtos e mais. Você também pode usar o modelo para gerar texto para uma variedade de aplicativos, como chatbots e aplicativos de atendimento ao cliente que permitem que agentes de atendimento respondam de forma eficaz e eficiente às consultas dos clientes.

![criar um prompt](../../../translated_images/create-prompt-gpt.69d429300c2e870a12ec95556cda9bacf6a173e452cdca02973c90df5f705cee.br.png)

Para aprender como usar este Modelo de IA no Power Automate, percorra o módulo [Adicionar inteligência com AI Builder e GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Bom Trabalho! Continue Seu Aprendizado

Após concluir esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Vá para a Lição 11, onde veremos como [integrar IA Generativa com Chamada de Função](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.