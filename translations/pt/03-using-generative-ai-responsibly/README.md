<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d57fad773cbeb69c5dd62e65c34200d",
  "translation_date": "2025-10-18T00:39:11+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "pt"
}
-->
# Usar IA Generativa de Forma Responsável

[![Usar IA Generativa de Forma Responsável](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.pt.png)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Clique na imagem acima para assistir ao vídeo desta lição_

É fácil ficar fascinado com a IA, especialmente a IA generativa, mas é importante considerar como utilizá-la de forma responsável. É necessário pensar em como garantir que os resultados sejam justos, não prejudiciais e mais. Este capítulo tem como objetivo fornecer o contexto mencionado, o que considerar e como tomar medidas ativas para melhorar o uso da IA.

## Introdução

Esta lição abordará:

- Por que deve-se priorizar a IA Responsável ao construir aplicações de IA Generativa.
- Princípios fundamentais da IA Responsável e como eles se relacionam com a IA Generativa.
- Como colocar esses princípios de IA Responsável em prática através de estratégias e ferramentas.

## Objetivos de Aprendizagem

Após concluir esta lição, você saberá:

- A importância da IA Responsável ao construir aplicações de IA Generativa.
- Quando pensar e aplicar os princípios fundamentais da IA Responsável ao construir aplicações de IA Generativa.
- Quais ferramentas e estratégias estão disponíveis para colocar o conceito de IA Responsável em prática.

## Princípios da IA Responsável

O entusiasmo pela IA Generativa nunca foi tão grande. Esse entusiasmo trouxe muitos novos desenvolvedores, atenção e financiamento para este campo. Embora isso seja muito positivo para quem deseja construir produtos e empresas usando IA Generativa, também é importante avançar de forma responsável.

Ao longo deste curso, estamos focados em construir nossa startup e nosso produto educacional de IA. Usaremos os princípios da IA Responsável: Justiça, Inclusão, Confiabilidade/Segurança, Segurança e Privacidade, Transparência e Responsabilidade. Com esses princípios, exploraremos como eles se relacionam com o uso da IA Generativa em nossos produtos.

## Por que Priorizar a IA Responsável

Ao construir um produto, adotar uma abordagem centrada no ser humano, mantendo os melhores interesses do usuário em mente, leva aos melhores resultados.

A singularidade da IA Generativa está em sua capacidade de criar respostas úteis, informações, orientações e conteúdos para os usuários. Isso pode ser feito sem muitos passos manuais, o que pode levar a resultados muito impressionantes. Sem planejamento e estratégias adequados, isso também pode, infelizmente, levar a resultados prejudiciais para seus usuários, seu produto e a sociedade como um todo.

Vamos analisar alguns (mas não todos) desses resultados potencialmente prejudiciais:

### Alucinações

Alucinações são um termo usado para descrever quando um LLM produz conteúdo que é completamente sem sentido ou algo que sabemos ser factualmente incorreto com base em outras fontes de informação.

Por exemplo, suponha que criemos um recurso para nossa startup que permita aos estudantes fazer perguntas históricas a um modelo. Um estudante pergunta: `Quem foi o único sobrevivente do Titanic?`

O modelo produz uma resposta como a seguinte:

![Prompt dizendo "Quem foi o único sobrevivente do Titanic"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Fonte: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Esta é uma resposta muito confiante e detalhada. Infelizmente, está incorreta. Mesmo com uma pesquisa mínima, descobriríamos que houve mais de um sobrevivente do desastre do Titanic. Para um estudante que está começando a pesquisar este tópico, esta resposta pode ser persuasiva o suficiente para não ser questionada e tratada como fato. As consequências disso podem levar o sistema de IA a ser pouco confiável e impactar negativamente a reputação da nossa startup.

Com cada iteração de um determinado LLM, temos visto melhorias de desempenho na minimização de alucinações. Mesmo com essa melhoria, nós, como criadores e usuários de aplicações, ainda precisamos estar cientes dessas limitações.

### Conteúdo Prejudicial

Já abordamos na seção anterior o caso em que um LLM produz respostas incorretas ou sem sentido. Outro risco que precisamos estar atentos é quando um modelo responde com conteúdo prejudicial.

Conteúdo prejudicial pode ser definido como:

- Fornecer instruções ou encorajar autolesão ou danos a determinados grupos.
- Conteúdo odioso ou depreciativo.
- Orientar o planejamento de qualquer tipo de ataque ou atos violentos.
- Fornecer instruções sobre como encontrar conteúdo ilegal ou cometer atos ilegais.
- Exibir conteúdo sexualmente explícito.

Para nossa startup, queremos garantir que temos as ferramentas e estratégias certas para evitar que esse tipo de conteúdo seja visto pelos estudantes.

### Falta de Justiça

Justiça é definida como “garantir que um sistema de IA esteja livre de preconceitos e discriminação e que trate todos de forma justa e igualitária.” No mundo da IA Generativa, queremos garantir que visões de mundo excludentes de grupos marginalizados não sejam reforçadas pelos resultados do modelo.

Esses tipos de resultados não apenas prejudicam a construção de experiências positivas de produto para nossos usuários, mas também causam danos sociais adicionais. Como criadores de aplicações, devemos sempre ter em mente uma base de usuários ampla e diversificada ao construir soluções com IA Generativa.

## Como Usar IA Generativa de Forma Responsável

Agora que identificamos a importância da IA Generativa Responsável, vamos analisar 4 etapas que podemos seguir para construir nossas soluções de IA de forma responsável:

![Ciclo de Mitigação](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.pt.png)

### Medir Danos Potenciais

Nos testes de software, testamos as ações esperadas de um usuário em uma aplicação. Da mesma forma, testar um conjunto diversificado de prompts que os usuários provavelmente usarão é uma boa maneira de medir danos potenciais.

Como nossa startup está construindo um produto educacional, seria bom preparar uma lista de prompts relacionados à educação. Isso poderia abranger um determinado assunto, fatos históricos e prompts sobre a vida estudantil.

### Mitigar Danos Potenciais

Agora é hora de encontrar maneiras de prevenir ou limitar os danos potenciais causados pelo modelo e suas respostas. Podemos analisar isso em 4 camadas diferentes:

![Camadas de Mitigação](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.pt.png)

- **Modelo**. Escolher o modelo certo para o caso de uso certo. Modelos maiores e mais complexos, como o GPT-4, podem causar mais risco de conteúdo prejudicial quando aplicados a casos de uso menores e mais específicos. Usar seus dados de treinamento para ajuste fino também reduz o risco de conteúdo prejudicial.

- **Sistema de Segurança**. Um sistema de segurança é um conjunto de ferramentas e configurações na plataforma que serve o modelo e ajuda a mitigar danos. Um exemplo disso é o sistema de filtragem de conteúdo no serviço Azure OpenAI. Os sistemas também devem detectar ataques de jailbreak e atividades indesejadas, como solicitações de bots.

- **Metaprompt**. Metaprompts e grounding são maneiras de direcionar ou limitar o modelo com base em certos comportamentos e informações. Isso pode incluir usar entradas do sistema para definir certos limites do modelo. Além disso, fornecer resultados mais relevantes para o escopo ou domínio do sistema.

Também pode incluir o uso de técnicas como Geração Aumentada por Recuperação (RAG) para que o modelo obtenha informações apenas de uma seleção de fontes confiáveis. Há uma lição mais adiante neste curso sobre [construção de aplicações de busca](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Experiência do Usuário**. A camada final é onde o usuário interage diretamente com o modelo através da interface da nossa aplicação de alguma forma. Dessa forma, podemos projetar o UI/UX para limitar o usuário nos tipos de entradas que ele pode enviar ao modelo, bem como no texto ou imagens exibidos ao usuário. Ao implementar a aplicação de IA, também devemos ser transparentes sobre o que nossa aplicação de IA Generativa pode e não pode fazer.

Temos uma lição inteira dedicada a [Projetar UX para Aplicações de IA](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Avaliar o modelo**. Trabalhar com LLMs pode ser desafiador porque nem sempre temos controle sobre os dados nos quais o modelo foi treinado. Mesmo assim, devemos sempre avaliar o desempenho e os resultados do modelo. Ainda é importante medir a precisão, similaridade, fundamentação e relevância dos resultados do modelo. Isso ajuda a fornecer transparência e confiança para as partes interessadas e usuários.

### Operar uma solução de IA Generativa Responsável

Construir uma prática operacional em torno de suas aplicações de IA é a etapa final. Isso inclui fazer parcerias com outras partes da nossa startup, como Jurídico e Segurança, para garantir que estamos em conformidade com todas as políticas regulatórias. Antes de lançar, também queremos construir planos em torno da entrega, gerenciamento de incidentes e reversão para evitar qualquer dano aos nossos usuários.

## Ferramentas

Embora o trabalho de desenvolver soluções de IA Responsável possa parecer muito, é um esforço que vale a pena. À medida que a área de IA Generativa cresce, mais ferramentas para ajudar os desenvolvedores a integrar responsabilidade de forma eficiente em seus fluxos de trabalho irão amadurecer. Por exemplo, o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) pode ajudar a detectar conteúdo e imagens prejudiciais por meio de uma solicitação de API.

## Verificação de Conhecimento

Quais são algumas coisas que você precisa considerar para garantir o uso responsável da IA?

1. Que a resposta esteja correta.
1. Uso prejudicial, que a IA não seja usada para fins criminosos.
1. Garantir que a IA esteja livre de preconceitos e discriminação.

R: 2 e 3 estão corretas. A IA Responsável ajuda você a considerar como mitigar efeitos prejudiciais, preconceitos e mais.

## 🚀 Desafio

Leia sobre o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) e veja o que pode adotar para o seu uso.

## Excelente Trabalho, Continue Aprendendo

Após concluir esta lição, confira nossa [coleção de aprendizado sobre IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento sobre IA Generativa!

Avance para a Lição 4, onde exploraremos [Fundamentos de Engenharia de Prompts](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.