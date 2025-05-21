<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T09:26:42+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "br"
}
-->
# Usando IA Generativa de Forma Responsável

> _Clique na imagem acima para ver o vídeo desta lição_

É fácil se fascinar com IA e, em particular, com IA generativa, mas é preciso considerar como usá-la de forma responsável. Você deve pensar em coisas como garantir que o resultado seja justo, não prejudicial e mais. Este capítulo tem como objetivo fornecer o contexto mencionado, o que considerar e como tomar medidas ativas para melhorar o uso da IA.

## Introdução

Esta lição abordará:

- Por que você deve priorizar IA Responsável ao construir aplicações de IA Generativa.
- Princípios fundamentais de IA Responsável e como eles se relacionam com IA Generativa.
- Como colocar esses princípios de IA Responsável em prática por meio de estratégia e ferramentas.

## Objetivos de Aprendizagem

Após completar esta lição, você saberá:

- A importância da IA Responsável ao construir aplicações de IA Generativa.
- Quando pensar e aplicar os princípios fundamentais de IA Responsável ao construir aplicações de IA Generativa.
- Quais ferramentas e estratégias estão disponíveis para você colocar o conceito de IA Responsável em prática.

## Princípios de IA Responsável

A empolgação com IA Generativa nunca esteve tão alta. Essa empolgação trouxe muitos novos desenvolvedores, atenção e financiamento para este espaço. Embora isso seja muito positivo para quem busca construir produtos e empresas usando IA Generativa, também é importante prosseguirmos de forma responsável.

Ao longo deste curso, estamos focando na construção de nossa startup e nosso produto de educação em IA. Usaremos os princípios de IA Responsável: Justiça, Inclusão, Confiabilidade/Segurança, Segurança e Privacidade, Transparência e Responsabilidade. Com esses princípios, exploraremos como eles se relacionam com nosso uso de IA Generativa em nossos produtos.

## Por que Priorizar IA Responsável

Ao construir um produto, adotar uma abordagem centrada no ser humano, mantendo o melhor interesse do usuário em mente, leva aos melhores resultados.

A singularidade da IA Generativa é seu poder de criar respostas úteis, informações, orientações e conteúdo para os usuários. Isso pode ser feito sem muitos passos manuais, o que pode levar a resultados muito impressionantes. Sem planejamento e estratégias adequados, isso também pode, infelizmente, levar a resultados prejudiciais para seus usuários, seu produto e a sociedade como um todo.

Vamos analisar alguns (mas não todos) desses resultados potencialmente prejudiciais:

### Alucinações

Alucinações são um termo usado para descrever quando um LLM produz conteúdo que é completamente sem sentido ou algo que sabemos ser factualmente errado com base em outras fontes de informação.

Vamos tomar como exemplo que construímos um recurso para nossa startup que permite que os alunos façam perguntas históricas a um modelo. Um aluno faz a pergunta `Who was the sole survivor of Titanic?`

O modelo produz uma resposta como a abaixo:

Esta é uma resposta muito confiante e completa. Infelizmente, está incorreta. Mesmo com uma quantidade mínima de pesquisa, alguém descobriria que houve mais de um sobrevivente do desastre do Titanic. Para um aluno que está começando a pesquisar este tópico, esta resposta pode ser persuasiva o suficiente para não ser questionada e tratada como fato. As consequências disso podem levar o sistema de IA a ser pouco confiável e impactar negativamente a reputação de nossa startup.

Com cada iteração de qualquer LLM dado, vimos melhorias de desempenho em torno da minimização de alucinações. Mesmo com essa melhoria, nós, como construtores de aplicativos e usuários, ainda precisamos estar cientes dessas limitações.

### Conteúdo Prejudicial

Cobrimos na seção anterior quando um LLM produz respostas incorretas ou sem sentido. Outro risco que precisamos estar cientes é quando um modelo responde com conteúdo prejudicial.

Conteúdo prejudicial pode ser definido como:

- Fornecer instruções ou encorajar autolesão ou dano a certos grupos.
- Conteúdo odioso ou depreciativo.
- Orientar o planejamento de qualquer tipo de ataque ou atos violentos.
- Fornecer instruções sobre como encontrar conteúdo ilegal ou cometer atos ilegais.
- Exibir conteúdo sexualmente explícito.

Para nossa startup, queremos garantir que temos as ferramentas e estratégias certas em vigor para impedir que esse tipo de conteúdo seja visto pelos alunos.

### Falta de Justiça

Justiça é definida como “garantir que um sistema de IA esteja livre de preconceitos e discriminação e que trate todos de forma justa e igualitária.” No mundo da IA Generativa, queremos garantir que visões de mundo excludentes de grupos marginalizados não sejam reforçadas pela saída do modelo.

Esses tipos de saídas não são apenas destrutivos para construir experiências positivas de produtos para nossos usuários, mas também causam mais danos à sociedade. Como construtores de aplicativos, devemos sempre ter em mente uma base de usuários ampla e diversificada ao construir soluções com IA Generativa.

## Como Usar IA Generativa de Forma Responsável

Agora que identificamos a importância da IA Generativa Responsável, vamos analisar 4 passos que podemos tomar para construir nossas soluções de IA de forma responsável:

### Medir Danos Potenciais

Nos testes de software, testamos as ações esperadas de um usuário em um aplicativo. Da mesma forma, testar um conjunto diversificado de prompts que os usuários provavelmente usarão é uma boa maneira de medir danos potenciais.

Como nossa startup está construindo um produto educacional, seria bom preparar uma lista de prompts relacionados à educação. Isso poderia ser para cobrir um determinado assunto, fatos históricos e prompts sobre a vida estudantil.

### Mitigar Danos Potenciais

Agora é hora de encontrar maneiras de prevenir ou limitar o dano potencial causado pelo modelo e suas respostas. Podemos analisar isso em 4 camadas diferentes:

- **Modelo**. Escolher o modelo certo para o caso de uso certo. Modelos maiores e mais complexos como o GPT-4 podem causar mais risco de conteúdo prejudicial quando aplicados a casos de uso menores e mais específicos. Usar seus dados de treinamento para ajuste fino também reduz o risco de conteúdo prejudicial.

- **Sistema de Segurança**. Um sistema de segurança é um conjunto de ferramentas e configurações na plataforma que serve o modelo que ajuda a mitigar danos. Um exemplo disso é o sistema de filtragem de conteúdo no serviço Azure OpenAI. Os sistemas também devem detectar ataques de jailbreak e atividades indesejadas como solicitações de bots.

- **Metaprompt**. Metaprompts e grounding são maneiras de direcionar ou limitar o modelo com base em certos comportamentos e informações. Isso pode ser usar entradas do sistema para definir certos limites do modelo. Além disso, fornecer saídas que são mais relevantes para o escopo ou domínio do sistema.

Também pode ser usar técnicas como Geração Aumentada por Recuperação (RAG) para fazer o modelo puxar informações apenas de uma seleção de fontes confiáveis. Há uma lição mais adiante neste curso para [construir aplicativos de busca](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Experiência do Usuário**. A camada final é onde o usuário interage diretamente com o modelo por meio da interface de nosso aplicativo de alguma forma. Dessa forma, podemos projetar o UI/UX para limitar o usuário nos tipos de entradas que podem enviar ao modelo, bem como texto ou imagens exibidas ao usuário. Ao implantar o aplicativo de IA, também devemos ser transparentes sobre o que nosso aplicativo de IA Generativa pode e não pode fazer.

Temos uma lição inteira dedicada a [Projetar UX para Aplicações de IA](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Avaliar o modelo**. Trabalhar com LLMs pode ser desafiador porque nem sempre temos controle sobre os dados com os quais o modelo foi treinado. Independentemente disso, devemos sempre avaliar o desempenho e as saídas do modelo. Ainda é importante medir a precisão, similaridade, fundamentação e relevância da saída do modelo. Isso ajuda a fornecer transparência e confiança aos stakeholders e usuários.

### Operar uma solução de IA Generativa Responsável

Construir uma prática operacional em torno de suas aplicações de IA é a etapa final. Isso inclui fazer parceria com outras partes de nossa startup como Legal e Segurança para garantir que estamos em conformidade com todas as políticas regulatórias. Antes de lançar, também queremos construir planos em torno de entrega, tratamento de incidentes e rollback para evitar qualquer dano aos nossos usuários ao crescer.

## Ferramentas

Embora o trabalho de desenvolver soluções de IA Responsável possa parecer muito, é um trabalho que vale a pena o esforço. À medida que a área de IA Generativa cresce, mais ferramentas para ajudar os desenvolvedores a integrar responsabilidade em seus fluxos de trabalho de forma eficiente amadurecerão. Por exemplo, o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) pode ajudar a detectar conteúdo e imagens prejudiciais por meio de uma solicitação de API.

## Verificação de Conhecimento

Quais são algumas coisas que você precisa se preocupar para garantir o uso responsável de IA?

1. Que a resposta esteja correta.
2. Uso prejudicial, que a IA não seja usada para fins criminosos.
3. Garantir que a IA esteja livre de preconceitos e discriminação.

A: 2 e 3 estão corretos. IA Responsável ajuda você a considerar como mitigar efeitos prejudiciais e preconceitos e mais.

## 🚀 Desafio

Leia sobre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) e veja o que você pode adotar para seu uso.

## Ótimo Trabalho, Continue Seu Aprendizado

Após completar esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Vá para a Lição 4 onde veremos [Fundamentos de Engenharia de Prompt](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora busquemos precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.