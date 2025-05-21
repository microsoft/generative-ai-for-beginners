<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:37:52+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "pt"
}
-->
# Usando IA Generativa de Forma Responsável

> _Clique na imagem acima para ver o vídeo desta lição_

É fácil se fascinar com IA e, em particular, com IA generativa, mas é preciso considerar como usá-la de forma responsável. É necessário pensar em como garantir que o resultado seja justo, não prejudicial e mais. Este capítulo visa fornecer o contexto mencionado, o que considerar e como tomar medidas ativas para melhorar o uso da IA.

## Introdução

Esta lição abordará:

- Por que você deve priorizar a IA Responsável ao construir aplicações de IA Generativa.
- Princípios fundamentais da IA Responsável e como eles se relacionam com a IA Generativa.
- Como colocar esses princípios de IA Responsável em prática por meio de estratégia e ferramentas.

## Objetivos de Aprendizagem

Após completar esta lição, você saberá:

- A importância da IA Responsável ao construir aplicações de IA Generativa.
- Quando pensar e aplicar os princípios fundamentais da IA Responsável ao construir aplicações de IA Generativa.
- Quais ferramentas e estratégias estão disponíveis para você colocar o conceito de IA Responsável em prática.

## Princípios da IA Responsável

O entusiasmo pela IA Generativa nunca foi tão grande. Esse entusiasmo trouxe muitos novos desenvolvedores, atenção e financiamento para este espaço. Embora isso seja muito positivo para quem deseja construir produtos e empresas usando IA Generativa, também é importante proceder de forma responsável.

Ao longo deste curso, estamos focando na construção de nossa startup e nosso produto de educação em IA. Usaremos os princípios da IA Responsável: Justiça, Inclusão, Confiabilidade/Segurança, Segurança & Privacidade, Transparência e Responsabilidade. Com esses princípios, exploraremos como eles se relacionam com nosso uso de IA Generativa em nossos produtos.

## Por que Você Deve Priorizar a IA Responsável

Ao construir um produto, adotar uma abordagem centrada no ser humano, mantendo em mente o melhor interesse do usuário, leva aos melhores resultados.

A singularidade da IA Generativa é seu poder de criar respostas úteis, informações, orientações e conteúdo para os usuários. Isso pode ser feito sem muitos passos manuais, o que pode levar a resultados muito impressionantes. Sem o planejamento e as estratégias adequadas, isso também pode, infelizmente, levar a alguns resultados prejudiciais para seus usuários, seu produto e a sociedade como um todo.

Vamos examinar alguns (mas não todos) desses resultados potencialmente prejudiciais:

### Alucinações

Alucinações são um termo usado para descrever quando um LLM produz conteúdo que é completamente sem sentido ou algo que sabemos estar factualmente errado com base em outras fontes de informação.

Vamos supor que construímos um recurso para nossa startup que permite que os alunos façam perguntas históricas a um modelo. Um aluno faz a pergunta `Who was the sole survivor of Titanic?`

O modelo produz uma resposta como a abaixo:

Esta é uma resposta muito confiante e completa. Infelizmente, está incorreta. Mesmo com uma quantidade mínima de pesquisa, descobriríamos que houve mais de um sobrevivente do desastre do Titanic. Para um aluno que está apenas começando a pesquisar este tópico, essa resposta pode ser persuasiva o suficiente para não ser questionada e tratada como fato. As consequências disso podem levar o sistema de IA a ser pouco confiável e impactar negativamente a reputação de nossa startup.

Com cada iteração de um determinado LLM, vimos melhorias de desempenho em torno da minimização de alucinações. Mesmo com essa melhoria, nós, como construtores de aplicações e usuários, ainda precisamos estar cientes dessas limitações.

### Conteúdo Prejudicial

Cobrimos na seção anterior quando um LLM produz respostas incorretas ou sem sentido. Outro risco do qual precisamos estar cientes é quando um modelo responde com conteúdo prejudicial.

Conteúdo prejudicial pode ser definido como:

- Fornecer instruções ou encorajar autolesão ou dano a certos grupos.
- Conteúdo odioso ou depreciativo.
- Orientar o planejamento de qualquer tipo de ataque ou atos violentos.
- Fornecer instruções sobre como encontrar conteúdo ilegal ou cometer atos ilegais.
- Exibir conteúdo sexualmente explícito.

Para nossa startup, queremos garantir que temos as ferramentas e estratégias certas em vigor para impedir que esse tipo de conteúdo seja visto pelos alunos.

### Falta de Justiça

Justiça é definida como "garantir que um sistema de IA esteja livre de preconceitos e discriminação e que trate todos de forma justa e igualitária." No mundo da IA Generativa, queremos garantir que visões de mundo excludentes de grupos marginalizados não sejam reforçadas pela saída do modelo.

Esses tipos de saídas não são apenas destrutivos para construir experiências de produto positivas para nossos usuários, mas também causam mais danos sociais. Como construtores de aplicações, devemos sempre ter em mente uma base de usuários ampla e diversa ao construir soluções com IA Generativa.

## Como Usar a IA Generativa de Forma Responsável

Agora que identificamos a importância da IA Generativa Responsável, vamos examinar 4 etapas que podemos seguir para construir nossas soluções de IA de forma responsável:

### Medir Potenciais Danos

Nos testes de software, testamos as ações esperadas de um usuário em uma aplicação. Da mesma forma, testar um conjunto diversificado de prompts que os usuários provavelmente usarão é uma boa maneira de medir danos potenciais.

Como nossa startup está construindo um produto educacional, seria bom preparar uma lista de prompts relacionados à educação. Isso poderia cobrir um determinado assunto, fatos históricos e prompts sobre a vida estudantil.

### Mitigar Potenciais Danos

Agora é hora de encontrar maneiras de prevenir ou limitar o potencial dano causado pelo modelo e suas respostas. Podemos olhar para isso em 4 camadas diferentes:

- **Modelo**. Escolher o modelo certo para o caso de uso certo. Modelos maiores e mais complexos, como o GPT-4, podem causar mais risco de conteúdo prejudicial quando aplicados a casos de uso menores e mais específicos. Usar seus dados de treinamento para ajuste fino também reduz o risco de conteúdo prejudicial.

- **Sistema de Segurança**. Um sistema de segurança é um conjunto de ferramentas e configurações na plataforma que serve o modelo e ajuda a mitigar danos. Um exemplo disso é o sistema de filtragem de conteúdo no serviço Azure OpenAI. Os sistemas também devem detectar ataques de jailbreak e atividades indesejadas, como solicitações de bots.

- **Metaprompt**. Metaprompts e grounding são maneiras de direcionar ou limitar o modelo com base em certos comportamentos e informações. Isso pode ser usando entradas do sistema para definir certos limites do modelo. Além disso, fornecer saídas mais relevantes para o escopo ou domínio do sistema.

Também pode ser usando técnicas como Geração Aumentada por Recuperação (RAG) para que o modelo apenas busque informações de uma seleção de fontes confiáveis. Há uma lição mais adiante neste curso para [construir aplicações de busca](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Experiência do Usuário**. A camada final é onde o usuário interage diretamente com o modelo através da interface de nossa aplicação de alguma forma. Dessa forma, podemos projetar a UI/UX para limitar o usuário nos tipos de entradas que podem ser enviadas ao modelo, bem como textos ou imagens exibidos ao usuário. Ao implantar a aplicação de IA, também devemos ser transparentes sobre o que nossa aplicação de IA Generativa pode e não pode fazer.

Temos uma lição inteira dedicada a [Projetar UX para Aplicações de IA](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Avaliar modelo**. Trabalhar com LLMs pode ser desafiador porque nem sempre temos controle sobre os dados nos quais o modelo foi treinado. Independentemente disso, devemos sempre avaliar o desempenho e as saídas do modelo. Ainda é importante medir a precisão, similaridade, fundamentação e relevância da saída do modelo. Isso ajuda a fornecer transparência e confiança para as partes interessadas e usuários.

### Operar uma Solução de IA Generativa Responsável

Construir uma prática operacional em torno de suas aplicações de IA é a etapa final. Isso inclui parcerias com outras partes de nossa startup, como Jurídico e Segurança, para garantir que estamos em conformidade com todas as políticas regulatórias. Antes do lançamento, também queremos construir planos em torno da entrega, gerenciamento de incidentes e rollback para evitar qualquer dano aos nossos usuários à medida que crescemos.

## Ferramentas

Embora o trabalho de desenvolver soluções de IA Responsável possa parecer muito, é um trabalho que vale a pena o esforço. À medida que a área de IA Generativa cresce, mais ferramentas para ajudar os desenvolvedores a integrar a responsabilidade em seus fluxos de trabalho de forma eficiente amadurecerão. Por exemplo, o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) pode ajudar a detectar conteúdo e imagens prejudiciais por meio de uma solicitação de API.

## Verificação de Conhecimento

Quais são algumas coisas que você precisa se preocupar para garantir o uso responsável da IA?

1. Que a resposta esteja correta.
1. Uso prejudicial, que a IA não seja usada para fins criminosos.
1. Garantir que a IA esteja livre de preconceitos e discriminação.

A: 2 e 3 estão corretas. A IA Responsável ajuda você a considerar como mitigar efeitos prejudiciais e preconceitos e mais.

## 🚀 Desafio

Leia sobre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) e veja o que você pode adotar para seu uso.

## Ótimo Trabalho, Continue Seu Aprendizado

Após completar esta lição, confira nossa [coleção de aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento sobre IA Generativa!

Vá para a Lição 4, onde analisaremos [Fundamentos de Engenharia de Prompt](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.