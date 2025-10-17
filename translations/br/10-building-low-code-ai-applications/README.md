<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "846ac8e3b7dcfb697d3309fec05f0fea",
  "translation_date": "2025-10-17T15:59:54+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "br"
}
-->
# Construindo Aplicações de IA com Baixo Código

[![Construindo Aplicações de IA com Baixo Código](../../../translated_images/10-lesson-banner.a01ac8fe3fd86310c2e4065c0b3c584879f33b8ce797311821a636992f8a5b2f.br.png)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

## Introdução

Agora que aprendemos como criar aplicações de geração de imagens, vamos falar sobre baixo código. A IA generativa pode ser usada em diversas áreas, incluindo baixo código, mas o que é baixo código e como podemos adicionar IA a ele?

Criar aplicativos e soluções tornou-se mais fácil para desenvolvedores tradicionais e não desenvolvedores por meio do uso de Plataformas de Desenvolvimento de Baixo Código. Essas plataformas permitem que você crie aplicativos e soluções com pouco ou nenhum código. Isso é possível graças a um ambiente de desenvolvimento visual que permite arrastar e soltar componentes para construir aplicativos e soluções. Isso possibilita criar aplicativos e soluções mais rapidamente e com menos recursos. Nesta lição, vamos explorar como usar baixo código e como aprimorar o desenvolvimento de baixo código com IA usando o Power Platform.

O Power Platform oferece às organizações a oportunidade de capacitar suas equipes para criar suas próprias soluções por meio de um ambiente intuitivo de baixo código ou sem código. Esse ambiente ajuda a simplificar o processo de criação de soluções. Com o Power Platform, soluções podem ser criadas em dias ou semanas, em vez de meses ou anos. O Power Platform é composto por cinco produtos principais: Power Apps, Power Automate, Power BI, Power Pages e Copilot Studio.

Esta lição aborda:

- Introdução à IA generativa no Power Platform
- Introdução ao Copilot e como utilizá-lo
- Usando IA generativa para criar aplicativos e fluxos no Power Platform
- Compreendendo os Modelos de IA no Power Platform com o AI Builder

## Objetivos de Aprendizagem

Ao final desta lição, você será capaz de:

- Compreender como o Copilot funciona no Power Platform.

- Criar um aplicativo de rastreamento de tarefas de estudantes para nossa startup educacional.

- Criar um fluxo de processamento de faturas que utiliza IA para extrair informações de faturas.

- Aplicar melhores práticas ao usar o modelo de IA "Create Text with GPT".

As ferramentas e tecnologias que você usará nesta lição são:

- **Power Apps**, para o aplicativo de rastreamento de tarefas de estudantes, que oferece um ambiente de desenvolvimento de baixo código para criar aplicativos que rastreiam, gerenciam e interagem com dados.

- **Dataverse**, para armazenar os dados do aplicativo de rastreamento de tarefas de estudantes, onde o Dataverse fornecerá uma plataforma de dados de baixo código para armazenar os dados do aplicativo.

- **Power Automate**, para o fluxo de processamento de faturas, onde você terá um ambiente de desenvolvimento de baixo código para criar fluxos de trabalho que automatizam o processo de processamento de faturas.

- **AI Builder**, para o modelo de IA de processamento de faturas, onde você usará modelos de IA pré-construídos para processar as faturas da nossa startup.

## IA Generativa no Power Platform

Aprimorar o desenvolvimento e as aplicações de baixo código com IA generativa é uma área de foco importante para o Power Platform. O objetivo é permitir que todos criem aplicativos, sites, dashboards e automatizem processos com IA, _sem exigir qualquer expertise em ciência de dados_. Esse objetivo é alcançado integrando IA generativa na experiência de desenvolvimento de baixo código no Power Platform na forma de Copilot e AI Builder.

### Como isso funciona?

Copilot é um assistente de IA que permite criar soluções no Power Platform descrevendo seus requisitos em uma série de etapas conversacionais usando linguagem natural. Por exemplo, você pode instruir o assistente de IA a indicar quais campos seu aplicativo usará, e ele criará tanto o aplicativo quanto o modelo de dados subjacente, ou você pode especificar como configurar um fluxo no Power Automate.

Você pode usar funcionalidades orientadas pelo Copilot como um recurso nas telas do seu aplicativo para permitir que os usuários descubram insights por meio de interações conversacionais.

AI Builder é uma capacidade de IA de baixo código disponível no Power Platform que permite usar modelos de IA para ajudar a automatizar processos e prever resultados. Com o AI Builder, você pode trazer IA para seus aplicativos e fluxos que se conectam aos seus dados no Dataverse ou em várias fontes de dados na nuvem, como SharePoint, OneDrive ou Azure.

O Copilot está disponível em todos os produtos do Power Platform: Power Apps, Power Automate, Power BI, Power Pages e Power Virtual Agents. O AI Builder está disponível no Power Apps e no Power Automate. Nesta lição, focaremos em como usar o Copilot e o AI Builder no Power Apps e no Power Automate para criar uma solução para nossa startup educacional.

### Copilot no Power Apps

Como parte do Power Platform, o Power Apps oferece um ambiente de desenvolvimento de baixo código para criar aplicativos que rastreiam, gerenciam e interagem com dados. É um conjunto de serviços de desenvolvimento de aplicativos com uma plataforma de dados escalável e a capacidade de se conectar a serviços na nuvem e dados locais. O Power Apps permite criar aplicativos que funcionam em navegadores, tablets e celulares, e podem ser compartilhados com colegas de trabalho. O Power Apps facilita o desenvolvimento de aplicativos com uma interface simples, para que qualquer usuário empresarial ou desenvolvedor profissional possa criar aplicativos personalizados. A experiência de desenvolvimento de aplicativos também é aprimorada com IA generativa por meio do Copilot.

O recurso de assistente de IA Copilot no Power Apps permite que você descreva o tipo de aplicativo que precisa e as informações que deseja que seu aplicativo rastreie, colete ou exiba. O Copilot então gera um aplicativo Canvas responsivo com base na sua descrição. Você pode personalizar o aplicativo para atender às suas necessidades. O Copilot também gera e sugere uma tabela do Dataverse com os campos necessários para armazenar os dados que você deseja rastrear e alguns dados de exemplo. Veremos o que é o Dataverse e como você pode usá-lo no Power Apps mais adiante nesta lição. Você pode personalizar a tabela para atender às suas necessidades usando o recurso de assistente Copilot por meio de etapas conversacionais. Esse recurso está disponível diretamente na tela inicial do Power Apps.

### Copilot no Power Automate

Como parte do Power Platform, o Power Automate permite que os usuários criem fluxos de trabalho automatizados entre aplicativos e serviços. Ele ajuda a automatizar processos repetitivos de negócios, como comunicação, coleta de dados e aprovações de decisões. Sua interface simples permite que usuários de todos os níveis técnicos (de iniciantes a desenvolvedores experientes) automatizem tarefas de trabalho. A experiência de desenvolvimento de fluxos de trabalho também é aprimorada com IA generativa por meio do Copilot.

O recurso de assistente de IA Copilot no Power Automate permite que você descreva o tipo de fluxo que precisa e as ações que deseja que seu fluxo execute. O Copilot então gera um fluxo com base na sua descrição. Você pode personalizar o fluxo para atender às suas necessidades. O Copilot também gera e sugere as ações necessárias para realizar a tarefa que você deseja automatizar. Veremos o que são fluxos e como você pode usá-los no Power Automate mais adiante nesta lição. Você pode personalizar as ações para atender às suas necessidades usando o recurso de assistente Copilot por meio de etapas conversacionais. Esse recurso está disponível diretamente na tela inicial do Power Automate.

## Tarefa: Gerenciar tarefas de estudantes e faturas para nossa startup, usando Copilot

Nossa startup oferece cursos online para estudantes. A startup cresceu rapidamente e agora está lutando para acompanhar a demanda por seus cursos. A startup contratou você como desenvolvedor do Power Platform para ajudá-los a criar uma solução de baixo código para gerenciar as tarefas dos estudantes e as faturas. A solução deve ser capaz de ajudar a rastrear e gerenciar as tarefas dos estudantes por meio de um aplicativo e automatizar o processo de processamento de faturas por meio de um fluxo de trabalho. Você foi solicitado a usar IA generativa para desenvolver a solução.

Ao começar a usar o Copilot, você pode usar a [Biblioteca de Prompts do Copilot do Power Platform](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) para começar com os prompts. Esta biblioteca contém uma lista de prompts que você pode usar para criar aplicativos e fluxos com o Copilot. Você também pode usar os prompts da biblioteca para ter uma ideia de como descrever seus requisitos ao Copilot.

### Criar um Aplicativo de Rastreamento de Tarefas de Estudantes para Nossa Startup

Os educadores da nossa startup têm enfrentado dificuldades para acompanhar as tarefas dos estudantes. Eles têm usado uma planilha para rastrear as tarefas, mas isso se tornou difícil de gerenciar à medida que o número de estudantes aumentou. Eles pediram que você criasse um aplicativo que os ajudasse a rastrear e gerenciar as tarefas dos estudantes. O aplicativo deve permitir que eles adicionem novas tarefas, visualizem tarefas, atualizem tarefas e excluam tarefas. O aplicativo também deve permitir que educadores e estudantes visualizem as tarefas que foram avaliadas e as que ainda não foram.

Você criará o aplicativo usando o Copilot no Power Apps seguindo os passos abaixo:

1. Navegue até a [tela inicial do Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Use a área de texto na tela inicial para descrever o aplicativo que deseja criar. Por exemplo, **_Quero criar um aplicativo para rastrear e gerenciar tarefas de estudantes_**. Clique no botão **Enviar** para enviar o prompt ao Copilot.

![Descreva o aplicativo que deseja criar](../../../translated_images/copilot-chat-prompt-powerapps.84250f341d060830a296b68512e6b3b3aa3a4559f4f1c2d7bafeba8ad3fcd17a.br.png)

1. O Copilot sugerirá uma tabela do Dataverse com os campos necessários para armazenar os dados que você deseja rastrear e alguns dados de exemplo. Você pode personalizar a tabela para atender às suas necessidades usando o recurso de assistente Copilot por meio de etapas conversacionais.

   > **Importante**: O Dataverse é a plataforma de dados subjacente do Power Platform. É uma plataforma de dados de baixo código para armazenar os dados do aplicativo. É um serviço totalmente gerenciado que armazena dados com segurança na nuvem da Microsoft e é provisionado dentro do seu ambiente do Power Platform. Ele vem com recursos integrados de governança de dados, como classificação de dados, linhagem de dados, controle de acesso detalhado e mais. Você pode aprender mais sobre o Dataverse [aqui](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Campos sugeridos na sua nova tabela](../../../translated_images/copilot-dataverse-table-powerapps.f4cc07b5d5f9327bd3783dd288debb2a959ce3320107512e235137aebd8a1a4c.br.png)

1. Os educadores querem enviar e-mails aos estudantes que enviaram suas tarefas para mantê-los atualizados sobre o progresso de suas tarefas. Você pode usar o Copilot para adicionar um novo campo à tabela para armazenar o e-mail do estudante. Por exemplo, você pode usar o seguinte prompt para adicionar um novo campo à tabela: **_Quero adicionar uma coluna para armazenar o e-mail do estudante_**. Clique no botão **Enviar** para enviar o prompt ao Copilot.

![Adicionando um novo campo](../../../translated_images/copilot-new-column.35e15ff21acaf2745965d427b130f2be772f0484835b44fe074d496b1a455f2a.br.png)

1. O Copilot gerará um novo campo e você poderá personalizar o campo para atender às suas necessidades.

1. Quando terminar de configurar a tabela, clique no botão **Criar aplicativo** para criar o aplicativo.

1. O Copilot gerará um aplicativo Canvas responsivo com base na sua descrição. Você poderá personalizar o aplicativo para atender às suas necessidades.

1. Para que os educadores enviem e-mails aos estudantes, você pode usar o Copilot para adicionar uma nova tela ao aplicativo. Por exemplo, você pode usar o seguinte prompt para adicionar uma nova tela ao aplicativo: **_Quero adicionar uma tela para enviar e-mails aos estudantes_**. Clique no botão **Enviar** para enviar o prompt ao Copilot.

![Adicionando uma nova tela via instrução de prompt](../../../translated_images/copilot-new-screen.2e0bef7132a173928bc621780b39799e03982d315cb5a9ff75a34b08054641d4.br.png)

1. O Copilot gerará uma nova tela e você poderá personalizar a tela para atender às suas necessidades.

1. Quando terminar de configurar o aplicativo, clique no botão **Salvar** para salvar o aplicativo.

1. Para compartilhar o aplicativo com os educadores, clique no botão **Compartilhar** e, em seguida, clique novamente no botão **Compartilhar**. Você poderá compartilhar o aplicativo com os educadores inserindo os endereços de e-mail deles.

> **Sua tarefa de casa**: O aplicativo que você acabou de criar é um bom começo, mas pode ser melhorado. Com o recurso de e-mail, os educadores só podem enviar e-mails aos estudantes manualmente, tendo que digitar os e-mails. Você pode usar o Copilot para criar uma automação que permita aos educadores enviar e-mails automaticamente aos estudantes quando eles enviarem suas tarefas? Sua dica é que, com o prompt certo, você pode usar o Copilot no Power Automate para criar isso.

### Criar uma Tabela de Informações de Faturas para Nossa Startup

A equipe financeira da nossa startup tem enfrentado dificuldades para acompanhar as faturas. Eles têm usado uma planilha para rastrear as faturas, mas isso se tornou difícil de gerenciar à medida que o número de faturas aumentou. Eles pediram que você criasse uma tabela que os ajudasse a armazenar, rastrear e gerenciar as informações das faturas recebidas. A tabela deve ser usada para criar uma automação que extraia todas as informações das faturas e as armazene na tabela. A tabela também deve permitir que a equipe financeira visualize as faturas que foram pagas e as que ainda não foram pagas.

O Power Platform possui uma plataforma de dados subjacente chamada Dataverse que permite armazenar os dados para seus aplicativos e soluções. O Dataverse fornece uma plataforma de dados de baixo código para armazenar os dados do aplicativo. É um serviço totalmente gerenciado que armazena dados com segurança na nuvem da Microsoft e é provisionado dentro do seu ambiente do Power Platform. Ele vem com recursos integrados de governança de dados, como classificação de dados, linhagem de dados, controle de acesso detalhado e mais. Você pode aprender mais [sobre o Dataverse aqui](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).
Por que devemos usar o Dataverse na nossa startup? As tabelas padrão e personalizadas dentro do Dataverse oferecem uma opção segura e baseada na nuvem para armazenar seus dados. As tabelas permitem armazenar diferentes tipos de dados, semelhante ao uso de várias planilhas em um único arquivo do Excel. Você pode usar tabelas para armazenar dados específicos das necessidades da sua organização ou negócio. Alguns dos benefícios que nossa startup terá ao usar o Dataverse incluem, mas não se limitam a:

- **Fácil de gerenciar**: Tanto os metadados quanto os dados são armazenados na nuvem, então você não precisa se preocupar com os detalhes de como eles são armazenados ou gerenciados. Você pode focar em construir seus aplicativos e soluções.

- **Seguro**: O Dataverse oferece uma opção segura e baseada na nuvem para armazenar seus dados. Você pode controlar quem tem acesso aos dados nas suas tabelas e como eles podem acessá-los usando segurança baseada em funções.

- **Metadados ricos**: Tipos de dados e relacionamentos são usados diretamente no Power Apps.

- **Lógica e validação**: Você pode usar regras de negócios, campos calculados e regras de validação para aplicar lógica de negócios e manter a precisão dos dados.

Agora que você sabe o que é o Dataverse e por que deve usá-lo, vamos ver como você pode usar o Copilot para criar uma tabela no Dataverse que atenda aos requisitos da nossa equipe financeira.

> **Nota**: Você usará esta tabela na próxima seção para criar uma automação que extrairá todas as informações de faturas e as armazenará na tabela.

Para criar uma tabela no Dataverse usando o Copilot, siga os passos abaixo:

1. Acesse a tela inicial do [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Na barra de navegação à esquerda, selecione **Tabelas** e clique em **Descrever nova tabela**.

![Selecionar nova tabela](../../../translated_images/describe-new-table.0792373eb757281e3c5f542f84cad3b5208bfe0e5c4a7786dd2bd31aa848a23c.br.png)

3. Na tela **Descrever nova tabela**, use a área de texto para descrever a tabela que você deseja criar. Por exemplo, **_Quero criar uma tabela para armazenar informações de faturas_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

![Descrever a tabela](../../../translated_images/copilot-chat-prompt-dataverse.feb2f81e5872b9d2b05d45d11bb6830e0f2ef6a2d4742413bc9a1e50a45bbb89.br.png)

4. O AI Copilot sugerirá uma tabela do Dataverse com os campos necessários para armazenar os dados que você deseja acompanhar e alguns dados de exemplo. Você pode personalizar a tabela conforme suas necessidades usando o recurso de assistente do AI Copilot por meio de etapas conversacionais.

![Tabela sugerida pelo Dataverse](../../../translated_images/copilot-dataverse-table.b3bc936091324d9db1e943d640df1c7a7df598e66d30f5b8a2999048e26a5073.br.png)

5. A equipe financeira quer enviar um e-mail ao fornecedor para atualizá-lo sobre o status atual da fatura. Você pode usar o Copilot para adicionar um novo campo à tabela para armazenar o e-mail do fornecedor. Por exemplo, você pode usar o seguinte comando para adicionar um novo campo à tabela: **_Quero adicionar uma coluna para armazenar o e-mail do fornecedor_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

6. O AI Copilot gerará um novo campo e você poderá personalizá-lo conforme suas necessidades.

7. Quando terminar de configurar a tabela, clique no botão **Criar** para criar a tabela.

## Modelos de IA no Power Platform com AI Builder

O AI Builder é uma funcionalidade de IA de baixo código disponível no Power Platform que permite usar modelos de IA para ajudar a automatizar processos e prever resultados. Com o AI Builder, você pode trazer IA para seus aplicativos e fluxos que se conectam aos seus dados no Dataverse ou em várias fontes de dados na nuvem, como SharePoint, OneDrive ou Azure.

## Modelos de IA pré-construídos vs Modelos de IA personalizados

O AI Builder oferece dois tipos de modelos de IA: Modelos de IA pré-construídos e Modelos de IA personalizados. Os modelos de IA pré-construídos são modelos prontos para uso, treinados pela Microsoft e disponíveis no Power Platform. Eles ajudam você a adicionar inteligência aos seus aplicativos e fluxos sem precisar reunir dados e, em seguida, construir, treinar e publicar seus próprios modelos. Você pode usar esses modelos para automatizar processos e prever resultados.

Alguns dos modelos de IA pré-construídos disponíveis no Power Platform incluem:

- **Extração de Frases-Chave**: Este modelo extrai frases-chave de textos.
- **Detecção de Idioma**: Este modelo detecta o idioma de um texto.
- **Análise de Sentimento**: Este modelo detecta sentimentos positivos, negativos, neutros ou mistos em textos.
- **Leitor de Cartões de Visita**: Este modelo extrai informações de cartões de visita.
- **Reconhecimento de Texto**: Este modelo extrai texto de imagens.
- **Detecção de Objetos**: Este modelo detecta e extrai objetos de imagens.
- **Processamento de Documentos**: Este modelo extrai informações de formulários.
- **Processamento de Faturas**: Este modelo extrai informações de faturas.

Com os modelos de IA personalizados, você pode trazer seu próprio modelo para o AI Builder para que ele funcione como qualquer modelo personalizado do AI Builder, permitindo que você treine o modelo usando seus próprios dados. Você pode usar esses modelos para automatizar processos e prever resultados tanto no Power Apps quanto no Power Automate. Ao usar seu próprio modelo, existem limitações que se aplicam. Leia mais sobre essas [limitações](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![Modelos do AI Builder](../../../translated_images/ai-builder-models.8069423b84cfc47f6bb989bc3cd0584b5b2471c80fad80bf504d356928a08c9c.br.png)

## Tarefa #2 - Criar um Fluxo de Processamento de Faturas para Nossa Startup

A equipe financeira tem enfrentado dificuldades para processar faturas. Eles têm usado uma planilha para acompanhar as faturas, mas isso se tornou difícil de gerenciar à medida que o número de faturas aumentou. Eles pediram para você criar um fluxo de trabalho que os ajude a processar faturas usando IA. O fluxo de trabalho deve permitir que eles extraiam informações de faturas e armazenem essas informações em uma tabela do Dataverse. O fluxo de trabalho também deve permitir que eles enviem um e-mail para a equipe financeira com as informações extraídas.

Agora que você sabe o que é o AI Builder e por que deve usá-lo, vamos ver como você pode usar o modelo de IA de Processamento de Faturas no AI Builder, que abordamos anteriormente, para criar um fluxo de trabalho que ajudará a equipe financeira a processar faturas.

Para criar um fluxo de trabalho que ajudará a equipe financeira a processar faturas usando o modelo de IA de Processamento de Faturas no AI Builder, siga os passos abaixo:

1. Acesse a tela inicial do [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Use a área de texto na tela inicial para descrever o fluxo de trabalho que você deseja criar. Por exemplo, **_Processar uma fatura quando ela chegar na minha caixa de entrada_**. Clique no botão **Enviar** para enviar o comando ao AI Copilot.

   ![Copilot power automate](../../../translated_images/copilot-chat-prompt-powerautomate.f377e478cc8412de4394fab09e5b72f97b3fc9312526b516ded426102f51c30d.br.png)

3. O AI Copilot sugerirá as ações necessárias para realizar a tarefa que você deseja automatizar. Você pode clicar no botão **Próximo** para seguir para as próximas etapas.

4. Na próxima etapa, o Power Automate solicitará que você configure as conexões necessárias para o fluxo. Quando terminar, clique no botão **Criar fluxo** para criar o fluxo.

5. O AI Copilot gerará um fluxo e você poderá personalizá-lo conforme suas necessidades.

6. Atualize o gatilho do fluxo e defina a **Pasta** para a pasta onde as faturas serão armazenadas. Por exemplo, você pode definir a pasta como **Caixa de Entrada**. Clique em **Mostrar opções avançadas** e defina **Somente com Anexos** como **Sim**. Isso garantirá que o fluxo só seja executado quando um e-mail com um anexo for recebido na pasta.

7. Remova as seguintes ações do fluxo: **HTML para texto**, **Compor**, **Compor 2**, **Compor 3** e **Compor 4**, pois você não as usará.

8. Remova a ação **Condição** do fluxo, pois você não a usará. Deve ficar como na captura de tela a seguir:

   ![power automate, remover ações](../../../translated_images/powerautomate-remove-actions.7216392fe684ceba4b73c6383edd1cc5e7ded11afd0ca812052a11487d049ef8.br.png)

9. Clique no botão **Adicionar uma ação** e procure por **Dataverse**. Selecione a ação **Adicionar uma nova linha**.

10. Na ação **Extrair Informações de Faturas**, atualize o **Arquivo da Fatura** para apontar para o **Conteúdo do Anexo** do e-mail. Isso garantirá que o fluxo extraia informações do anexo da fatura.

11. Selecione a **Tabela** que você criou anteriormente. Por exemplo, você pode selecionar a tabela **Informações de Faturas**. Escolha o conteúdo dinâmico da ação anterior para preencher os seguintes campos:

    - ID
    - Valor
    - Data
    - Nome
    - Status - Defina o **Status** como **Pendente**.
    - E-mail do Fornecedor - Use o conteúdo dinâmico **De** do gatilho **Quando um novo e-mail chegar**.

    ![power automate adicionar linha](../../../translated_images/powerautomate-add-row.5edce45e5dd3d51e5152688dc140ad43e1423e7a9fef9a206f82a7965ea68d73.br.png)

12. Quando terminar de configurar o fluxo, clique no botão **Salvar** para salvar o fluxo. Você pode testar o fluxo enviando um e-mail com uma fatura para a pasta que você especificou no gatilho.

> **Sua tarefa**: O fluxo que você acabou de criar é um bom começo, agora você precisa pensar em como pode criar uma automação que permitirá à equipe financeira enviar um e-mail ao fornecedor para atualizá-lo sobre o status atual da fatura. Sua dica: o fluxo deve ser executado quando o status da fatura mudar.

## Usar um Modelo de IA de Geração de Texto no Power Automate

O modelo de IA Criar Texto com GPT no AI Builder permite gerar texto com base em um comando e é alimentado pelo Microsoft Azure OpenAI Service. Com essa funcionalidade, você pode incorporar a tecnologia GPT (Generative Pre-Trained Transformer) em seus aplicativos e fluxos para criar uma variedade de fluxos automatizados e aplicativos perspicazes.

Os modelos GPT passam por um treinamento extenso em grandes volumes de dados, permitindo que produzam textos que se assemelham muito à linguagem humana quando recebem um comando. Quando integrados à automação de fluxos de trabalho, modelos de IA como o GPT podem ser aproveitados para simplificar e automatizar uma ampla gama de tarefas.

Por exemplo, você pode criar fluxos para gerar automaticamente textos para diversos casos de uso, como: rascunhos de e-mails, descrições de produtos e muito mais. Você também pode usar o modelo para gerar textos para diversos aplicativos, como chatbots e aplicativos de atendimento ao cliente que permitem que agentes de atendimento respondam de forma eficaz e eficiente às consultas dos clientes.

![criar um comando](../../../translated_images/create-prompt-gpt.69d429300c2e870a12ec95556cda9bacf6a173e452cdca02973c90df5f705cee.br.png)

Para aprender como usar este modelo de IA no Power Automate, acesse o módulo [Adicionar inteligência com AI Builder e GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Ótimo trabalho! Continue aprendendo

Depois de concluir esta lição, confira nossa [coleção de aprendizado sobre IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento sobre IA generativa!

Avance para a Lição 11, onde veremos como [integrar IA generativa com chamadas de função](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.