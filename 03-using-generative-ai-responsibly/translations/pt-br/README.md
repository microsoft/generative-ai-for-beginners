# Usando a IA Generativa de Forma Responsável

[![Usando a IA Generativa de Forma Responsável](../../images/03-lesson-banner.png?WT.mc_id=academic-105485-koreyst)]()

> **Vídeo em Breve**

É fácil se encantar com a IA e a IA generativa em particular. Mas é preciso considerar como você a usará de forma responsável. Você precisa considerar coisas como como garantir que a saída seja justa, não prejudicial e muito mais. Este capítulo tem como objetivo fornecer o contexto mencionado, o que considerar e como tomar medidas ativas para melhorar o uso de sua IA.

## Introdução

Esta lição abordará:

- Por que você deve priorizar a IA Responsável ao criar aplicações de IA Generativa.
- Princípios fundamentais da IA Responsável e como eles se relacionam com a IA Generativa.
- Como colocar esses princípios de IA Responsável em prática por meio de estratégias e ferramentas.

## Metas de Aprendizado

Após completar esta lição, você saberá:

- A importância da IA Responsável ao criar aplicações de IA Generativa.
- Quando pensar e aplicar os princípios fundamentais da IA Responsável ao criar aplicações de IA Generativa.
- Quais ferramentas e estratégias estão disponíveis para você colocar o conceito de IA Responsável em prática.

## Princípios de IA Responsável

A empolgação em torno da IA Generativa nunca foi tão alta. Essa empolgação trouxe muitos novas pessoas desenvolvedoras, atenção e financiamento para esse espaço. Embora isso seja muito positivo para quem deseja construir produtos e empresas usando a IA Generativa, também é importante que procedamos de forma responsável.

Ao longo deste curso, estamos nos concentrando em criar nossa startup e nosso produto de educação em IA. Usaremos os princípios da IA Responsável: Justiça, Inclusão, Confiabilidade/Segurança, Segurança e Privacidade, Transparência e Responsabilidade. Com esses princípios, exploraremos como eles se relacionam com o nosso uso da IA Generativa em nossos produtos.

## Por Que Você Deve Priorizar a IA Responsável

Ao criar um produto, adotar uma abordagem centrada no ser humano, mantendo o melhor interesse de seus usuários em mente, sempre leva aos melhores resultados.

A singularidade da IA Generativa está em seu poder de criar respostas úteis, informações, orientações e conteúdo para os usuários. Isso pode ser feito sem muitas etapas manuais, o que pode levar a resultados muito impressionantes. Sem um planejamento adequado e estratégias, também pode infelizmente levar a alguns resultados prejudiciais para seus usuários, seu produto e a sociedade como um todo.

Vamos dar uma olhada em alguns (mas não todos) desses resultados potencialmente prejudiciais:

### Alucinações

Alucinações é um termo usado para descrever quando um LLM produz conteúdo que é completamente sem sentido ou algo que sabemos ser factualmente incorreto com base em outras fontes de informação.

Vamos dar, por exemplo, a criação de um recurso para nossa startup que permite aos estudantes fazer perguntas históricas a um modelo. Um estudante faz a pergunta `Quem foi o único sobrevivente do Titanic?`

O modelo produz uma resposta como a que está abaixo:

![Prompt dizendo "Quem foi o único sobrevivente do Titanic"](<../../../03-using-generative-ai-responsibly/images/2135-ChatGPT(1)_11zon.webp?WT.mc_id=academic-105485-koreyst>)

> _(Fonte: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Esta é uma resposta muito confiante e completa. Infelizmente, está incorreta. Mesmo com uma quantidade mínima de pesquisa, alguém descobriria que houve mais de um sobrevivente do Titanic. Para um estudante que está começando a pesquisar esse tópico, essa resposta pode ser persuasiva o suficiente para não ser questionada e tratada como fato. As consequências disso podem levar ao sistema de IA sendo pouco confiável e impactar negativamente a reputação de nossa startup.

Com cada iteração de qualquer LLM dado, vimos melhorias de desempenho na minimização de alucinações. Mesmo com essa melhoria, nós, como construtores e usuários de aplicativos, ainda precisamos estar cientes dessas limitações.

### Conteúdo Prejudicial

Nós cobrimos na seção anterior quando um LLM produz respostas incorretas ou sem sentido. Outro risco que precisamos estar cientes é quando um modelo responde com conteúdo prejudicial.

Conteúdo prejudicial pode ser definido como:

- Fornecer instruções ou incentivar autolesão ou dano a certos grupos.
- Conteúdo odioso ou humilhante.
- Orientar o planejamento de qualquer tipo de ataque ou atos violentos.
- Fornecer instruções sobre como encontrar conteúdo ilegal ou cometer atos ilegais.
- Exibir conteúdo sexualmente explícito.

Para nossa startup, queremos garantir que tenhamos as ferramentas e estratégias certas em vigor para impedir que esse tipo de conteúdo seja visto pelos estudantes.

### Falta de Equidade

A equidade é definida como "garantir que um sistema de IA esteja livre de viés e discriminação e que trate todos de forma justa e igual". No mundo da IA Generativa, queremos garantir que visões de mundo excludentes de grupos marginalizados não sejam reforçadas pela saída do modelo.

Esses tipos de saídas não são apenas destrutivos para a criação de experiências de produtos positivas para nossos usuários. Mas também causam mais danos à sociedade. Como criadores de aplicações, devemos sempre ter em mente uma base de usuários ampla e diversificada ao criar soluções com IA Generativa.

## Como Usar a IA Generativa de Forma Responsável

Agora que identificamos a importância da IA Generativa Responsável, vamos ver 4 etapas que podemos seguir para construir nossas soluções de IA de forma responsável:

![Ciclo de Mitigação](../../images/mitigate-cycle.png?WT.mc_id=academic-105485-koreyst)

### Medir Danos Potenciais

Na área de testes de software, testamos as ações esperadas de um usuário em um aplicativo. Da mesma forma, testar um conjunto diversificado de prompts que os usuários provavelmente usarão é uma boa maneira de medir o dano potencial.

Como nossa startup está criando um produto de educação, seria bom preparar uma lista de prompts relacionados à educação. Isso poderia ser para cobrir um certo assunto, fatos históricos e prompts sobre a vida dos estudantes.

### Mitigar Danos Potenciais

Agora é hora de encontrar maneiras de prevenir ou limitar o dano potencial causado pelo modelo e suas respostas. Podemos analisar isso em 4 camadas diferentes:

![Camadas de Mitigação](../../images/mitigation-layers.png?WT.mc_id=academic-105485-koreyst)

- **Modelo**: escolher o modelo certo para o caso de uso certo. Modelos maiores e mais complexos, como o GPT-4, podem causar mais risco de conteúdo prejudicial quando aplicados a casos de uso menores e mais específicos. Usar seus dados de treinamento para ajuste fino também reduz o risco de conteúdo prejudicial.

- **Sistema de Segurança**: um sistema de segurança é um conjunto de ferramentas e configurações na plataforma que serve o modelo e ajuda a mitigar o dano. Um exemplo disso é o sistema de filtragem de conteúdo no serviço Azure OpenAI. Os sistemas também devem detectar ataques de jailbreak e atividades indesejadas, como solicitações de bots.

- **Metaprompt**: metaprompts e fundamentação são maneiras de direcionar ou limitar o modelo com base em determinados comportamentos e informações. Isso poderia ser o uso de entradas do sistema para definir certos limites do modelo. Além disso, fornecer saídas mais relevantes para o escopo ou domínio do sistema.

Também pode ser o uso de técnicas como a Recuperação de Geração Aumentada (RAG) para fazer com que o modelo obtenha informações apenas de uma seleção de fontes confiáveis. Há uma lição posterior neste curso para [criar aplicações de busca](../../../08-building-search-applications/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)

- **Experiência do Usuário**: a camada final é onde o usuário interage diretamente com o modelo por meio da interface de nosso aplicativo de alguma forma. Dessa forma, podemos projetar a UI/UX para limitar o usuário quanto aos tipos de entradas que podem enviar ao modelo, bem como ao texto ou imagens exibidos ao usuário. Ao implantar o aplicativo de IA, também devemos ser transparentes sobre o que nossa aplicação de IA Generativa pode e não pode fazer.

Temos uma lição inteira dedicada a [Projetar UX para Aplicações de IA](../../../12-designing-ux-for-ai-applications/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)

- **Avaliar o modelo**: trabalhar com LLMs pode ser desafiador porque nem sempre temos controle sobre os dados em que o modelo foi treinado. Independentemente disso, sempre devemos avaliar o desempenho e as saídas do modelo. Ainda é importante medir a precisão, similaridade, fundamentação e relevância do modelo de saída. Isso ajuda a fornecer transparência e confiança aos interessados e usuários.

### Operar uma Solução de IA Generativa Responsável

Criar uma prática operacional em torno de suas aplicações de IA é a etapa final. Isso inclui a parceria com outras partes de nossa startup, como Jurídico e Segurança, para garantir que estejamos em conformidade com todas as políticas regulatórias. Antes do lançamento, também queremos criar planos em torno da entrega, tratamento de incidentes e retorno para evitar qualquer dano crescente aos nossos usuários.

## Ferramentas

Embora o trabalho de desenvolver soluções de IA Responsável possa parecer muito, porém é um trabalho que vale a pena. À medida que a área de IA Generativa cresce, mais ferramentas para ajudar os desenvolvedores a integrar eficientemente a responsabilidade em seus fluxos de trabalho amadurecerão. Por exemplo, o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) pode ajudar a detectar conteúdo e imagens prejudiciais por meio de uma solicitação de API.

## Verificação de Conhecimento

Quais são algumas coisas das quais você precisa se preocupar para garantir o uso responsável da IA?

1. Que a resposta esteja correta.
2. Uso prejudicial, para que a IA não seja usada para fins criminosos.
3. Garantir que a IA esteja livre de viés e discriminação.

R: 2 e 3 estão corretas. A IA Responsável ajuda a considerar como mitigar efeitos prejudiciais e vieses, entre outros.

## 🚀 Desafio

Leia sobre o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) e veja o que você pode adotar para o seu uso.

## Ótimo Trabalho, Continue Sua Aprendizagem

Quer aprender mais sobre como construir com IA Generativa de forma responsável? Acesse a [página de aprendizado contínuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre esse tópico.

Vamos agora para a Lição 4, onde exploraremos os [Fundamentos da Engenharia de Prompt](../../../04-prompt-engineering-fundamentals/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)!
