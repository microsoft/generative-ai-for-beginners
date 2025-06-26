<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:20:43+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "pt"
}
-->
# Utilizar IA Generativa de Forma Responsável

> _Clique na imagem acima para ver o vídeo desta lição_

É fácil ficar fascinado com a IA e a IA generativa em particular, mas é necessário considerar como utilizá-la de forma responsável. É preciso pensar em como garantir que o resultado seja justo, não prejudicial e mais. Este capítulo visa fornecer o contexto mencionado, o que considerar e como tomar medidas ativas para melhorar o uso da IA.

## Introdução

Esta lição irá cobrir:

- Por que deve-se priorizar a IA Responsável ao construir aplicações de IA Generativa.
- Princípios fundamentais da IA Responsável e como eles se relacionam com a IA Generativa.
- Como colocar esses princípios de IA Responsável em prática através de estratégia e ferramentas.

## Objetivos de Aprendizagem

Após completar esta lição, você saberá:

- A importância da IA Responsável ao construir aplicações de IA Generativa.
- Quando pensar e aplicar os princípios fundamentais da IA Responsável ao construir aplicações de IA Generativa.
- Quais ferramentas e estratégias estão disponíveis para colocar o conceito de IA Responsável em prática.

## Princípios de IA Responsável

O entusiasmo pela IA Generativa nunca foi tão alto. Esse entusiasmo trouxe muitos novos desenvolvedores, atenção e financiamento para este espaço. Embora isso seja muito positivo para quem procura construir produtos e empresas usando IA Generativa, também é importante proceder de forma responsável.

Ao longo deste curso, estamos focando na construção da nossa startup e do nosso produto educacional de IA. Utilizaremos os princípios de IA Responsável: Justiça, Inclusão, Confiabilidade/Segurança, Segurança & Privacidade, Transparência e Responsabilidade. Com esses princípios, exploraremos como eles se relacionam com o uso da IA Generativa em nossos produtos.

## Por Que Deveria Priorizar a IA Responsável

Ao construir um produto, adotar uma abordagem centrada no ser humano, mantendo o melhor interesse do usuário em mente, leva aos melhores resultados.

A singularidade da IA Generativa é seu poder de criar respostas úteis, informações, orientações e conteúdo para os usuários. Isso pode ser feito sem muitos passos manuais, o que pode levar a resultados muito impressionantes. Sem planejamento e estratégias adequadas, também pode, infelizmente, levar a alguns resultados prejudiciais para seus usuários, seu produto e a sociedade como um todo.

Vamos olhar para alguns (mas não todos) desses resultados potencialmente prejudiciais:

### Alucinações

Alucinações são um termo usado para descrever quando um LLM produz conteúdo que é completamente sem sentido ou algo que sabemos ser factualmente errado com base em outras fontes de informação.

Vamos pegar, por exemplo, construímos um recurso para nossa startup que permite aos alunos fazer perguntas históricas a um modelo. Um aluno faz a pergunta `Who was the sole survivor of Titanic?`

O modelo produz uma resposta como a abaixo:

Esta é uma resposta muito confiante e completa. Infelizmente, está incorreta. Mesmo com uma quantidade mínima de pesquisa, alguém descobriria que houve mais de um sobrevivente do desastre do Titanic. Para um aluno que está apenas começando a pesquisar este tópico, esta resposta pode ser persuasiva o suficiente para não ser questionada e tratada como fato. As consequências disso podem levar ao sistema de IA ser pouco confiável e impactar negativamente a reputação da nossa startup.

Com cada iteração de um LLM dado, vimos melhorias de desempenho em torno da minimização de alucinações. Mesmo com essa melhoria, nós como construtores de aplicações e usuários ainda precisamos estar cientes dessas limitações.

### Conteúdo Prejudicial

Cobrimos na seção anterior quando um LLM produz respostas incorretas ou sem sentido. Outro risco que precisamos estar cientes é quando um modelo responde com conteúdo prejudicial.

Conteúdo prejudicial pode ser definido como:

- Fornecer instruções ou encorajar autoagressão ou agressão a certos grupos.
- Conteúdo odioso ou depreciativo.
- Orientar o planejamento de qualquer tipo de ataque ou atos violentos.
- Fornecer instruções sobre como encontrar conteúdo ilegal ou cometer atos ilegais.
- Exibir conteúdo sexualmente explícito.

Para nossa startup, queremos garantir que temos as ferramentas e estratégias certas em vigor para impedir que esse tipo de conteúdo seja visto pelos alunos.

### Falta de Justiça

Justiça é definida como “garantir que um sistema de IA esteja livre de preconceitos e discriminação e que trate todos de forma justa e igualitária.” No mundo da IA Generativa, queremos garantir que visões de mundo excludentes de grupos marginalizados não sejam reforçadas pela saída do modelo.

Esses tipos de saídas não são apenas destrutivos para construir experiências de produto positivas para nossos usuários, mas também causam mais danos à sociedade. Como construtores de aplicações, devemos sempre manter uma base de usuários ampla e diversificada em mente ao construir soluções com IA Generativa.

## Como Usar IA Generativa de Forma Responsável

Agora que identificamos a importância da IA Generativa Responsável, vamos olhar para 4 passos que podemos tomar para construir nossas soluções de IA de forma responsável:

### Medir Potenciais Danos

Nos testes de software, testamos as ações esperadas de um usuário em uma aplicação. Da mesma forma, testar um conjunto diversificado de prompts que os usuários provavelmente usarão é uma boa maneira de medir danos potenciais.

Já que nossa startup está construindo um produto educacional, seria bom preparar uma lista de prompts relacionados à educação. Isso pode ser para cobrir um determinado assunto, fatos históricos e prompts sobre a vida estudantil.

### Mitigar Potenciais Danos

Agora é hora de encontrar maneiras de prevenir ou limitar o dano potencial causado pelo modelo e suas respostas. Podemos olhar para isso em 4 camadas diferentes:

- **Modelo**. Escolher o modelo certo para o caso de uso certo. Modelos maiores e mais complexos como o GPT-4 podem causar mais risco de conteúdo prejudicial quando aplicados a casos de uso menores e mais específicos. Usar seus dados de treinamento para ajuste fino também reduz o risco de conteúdo prejudicial.

- **Sistema de Segurança**. Um sistema de segurança é um conjunto de ferramentas e configurações na plataforma que serve o modelo que ajuda a mitigar danos. Um exemplo disso é o sistema de filtragem de conteúdo no serviço Azure OpenAI. Sistemas também devem detectar ataques de jailbreak e atividade indesejada como solicitações de bots.

- **Metaprompt**. Metaprompts e grounding são maneiras de direcionar ou limitar o modelo com base em certos comportamentos e informações. Isso poderia ser usar entradas do sistema para definir certos limites do modelo. Além disso, fornecer saídas que sejam mais relevantes para o escopo ou domínio do sistema.

Também pode ser usar técnicas como a Geração de Recuperação Aumentada (RAG) para que o modelo apenas obtenha informações de uma seleção de fontes confiáveis. Há uma lição mais adiante neste curso para [construir aplicações de busca](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Experiência do Usuário**. A camada final é onde o usuário interage diretamente com o modelo através da interface de nossa aplicação de alguma forma. Desta forma, podemos projetar a UI/UX para limitar o usuário nos tipos de entradas que ele pode enviar ao modelo, bem como texto ou imagens exibidas ao usuário. Ao implantar a aplicação de IA, também devemos ser transparentes sobre o que nossa aplicação de IA Generativa pode e não pode fazer.

Temos uma lição inteira dedicada a [Desenhar UX para Aplicações de IA](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Avaliar modelo**. Trabalhar com LLMs pode ser desafiador porque nem sempre temos controle sobre os dados nos quais o modelo foi treinado. Independentemente disso, devemos sempre avaliar o desempenho e as saídas do modelo. Ainda é importante medir a precisão do modelo, similaridade, fundamentação e relevância da saída. Isso ajuda a fornecer transparência e confiança aos stakeholders e usuários.

### Operar uma Solução de IA Generativa Responsável

Construir uma prática operacional em torno de suas aplicações de IA é a etapa final. Isso inclui fazer parceria com outras partes de nossa startup como Legal e Segurança para garantir que estamos em conformidade com todas as políticas regulatórias. Antes de lançar, também queremos construir planos em torno da entrega, gerenciamento de incidentes e rollback para evitar qualquer dano aos nossos usuários de crescer.

## Ferramentas

Embora o trabalho de desenvolver soluções de IA Responsável possa parecer muito, é um trabalho que vale a pena. À medida que a área de IA Generativa cresce, mais ferramentas para ajudar os desenvolvedores a integrar responsabilidade em seus fluxos de trabalho de forma eficiente amadurecerão. Por exemplo, o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) pode ajudar a detectar conteúdo e imagens prejudiciais via uma solicitação de API.

## Verificação de Conhecimento

Quais são algumas coisas que você precisa se preocupar para garantir o uso responsável da IA?

1. Que a resposta está correta.
1. Uso prejudicial, que a IA não seja usada para propósitos criminosos.
1. Garantir que a IA esteja livre de preconceitos e discriminação.

A: 2 e 3 estão corretos. A IA Responsável ajuda você a considerar como mitigar efeitos prejudiciais e preconceitos e mais.

## 🚀 Desafio

Leia sobre o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) e veja o que você pode adotar para seu uso.

## Ótimo Trabalho, Continue Seu Aprendizado

Após completar esta lição, confira nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento sobre IA Generativa!

Vá para a Lição 4 onde vamos olhar para [Fundamentos de Engenharia de Prompt](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.