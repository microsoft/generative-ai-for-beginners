# Projetando UX para aplicativos de IA

[![Designing UX for AI Applications](../../images/12-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson12-gh?WT.mc_id=academic-105485-koreyst)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

A experiência do usuário é um aspecto muito importante na criação de aplicativos. Os usuários precisam poder usar seu aplicativo de maneira eficiente para realizar tarefas. Ser eficiente é uma coisa, mas você também precisa projetar aplicativos para que possam ser usados por todos, tornando-os _acessíveis_. Este capítulo se concentrará nessa área para que você termine projetando um aplicativo que as pessoas possam e queiram usar.

## Introdução

A experiência do usuário é como um usuário interage e utiliza um produto ou serviço específico, seja um sistema, ferramenta ou design. Ao desenvolver aplicativos de IA, os desenvolvedores não apenas se concentram em garantir que a experiência do usuário seja eficaz, mas também ética. Nesta lição, abordamos como construir aplicativos de Inteligência Artificial (IA) que atendem às necessidades do usuário.

A lição abordará as seguintes áreas:

- Introdução à Experiência do Usuário e Compreensão das Necessidades do Usuário
- Projeto de Aplicações de IA para Confiança e Transparência
- Projeto de Aplicações de IA para Colaboração e Feedback

## Metas de Aprendizado

Após esta lição, você será capaz de:

- Compreender como construir aplicativos de IA que atendam às necessidades do usuário.
- Projetar aplicativos de IA que promovam confiança e colaboração.

### Pré-requisito

Dedique um tempo para ler mais sobre [experiência do usuário e design thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introdução à Experiência do Usuário e Compreensão das Necessidades do Usuário

Em nossa fictícia startup de educação, temos dois usuários principais, professores e alunos. Cada um dos dois usuários tem necessidades únicas. Um design centrado no usuário prioriza o usuário, garantindo que os produtos sejam relevantes e benéficos para quem se destina.

A aplicação deve ser **útil, confiável, acessível e agradável** para proporcionar uma boa experiência do usuário.

### Usabilidade

Ser útil significa que a aplicação possui funcionalidades que correspondem ao seu propósito, como automatizar o processo de avaliação ou gerar flashcards para revisão. Uma aplicação que automatiza o processo de avaliação deve ser capaz de atribuir notas com precisão e eficiência ao trabalho dos alunos com base em critérios predefinidos. Da mesma forma, uma aplicação que gera flashcards de revisão deve ser capaz de criar perguntas relevantes e diversas com base em seus dados.

### Confiabilidade

Ser confiável significa que a aplicação pode realizar sua tarefa de forma consistente e sem erros. No entanto, a IA, assim como os humanos, não é perfeita e pode estar sujeita a erros. As aplicações podem encontrar erros ou situações inesperadas que exigem intervenção ou correção humana. Como lidar com erros? Na última seção desta lição, abordaremos como os sistemas e aplicações de IA são projetados para colaboração e feedback.

### Acessibilidade

Ser acessível significa estender a experiência do usuário a usuários com várias habilidades, incluindo aqueles com deficiências, garantindo que ninguém seja deixado de fora. Seguindo diretrizes e princípios de acessibilidade, as soluções de IA se tornam mais inclusivas, utilizáveis e benéficas para todos os usuários.

### Agradável

Ser agradável significa que a aplicação é agradável de usar. Uma experiência do usuário atraente pode ter um impacto positivo no usuário, incentivando-os a retornar à aplicação e aumentando a receita do negócio.

![imagem ilustrando considerações de UX em IA](../../images/uxinai.png?WT.mc_id=academic-105485-koreyst)

Nem todo desafio pode ser resolvido com IA. A IA entra para aprimorar sua experiência do usuário, seja automatizando tarefas manuais ou personalizando experiências do usuário.

# Projetando Aplicações de IA para Confiança e Transparência

Criar confiança é crucial ao projetar aplicações de IA. A confiança garante que o usuário tenha confiança de que o aplicativo concluirá o trabalho, entregará resultados consistentes e que os resultados são o que o usuário precisa. Um risco nessa área é a desconfiança e a confiança excessiva. A desconfiança ocorre quando um usuário tem pouca ou nenhuma confiança em um sistema de IA, o que leva o usuário a rejeitar seu aplicativo. A confiança excessiva ocorre quando um usuário superestima a capacidade de um sistema de IA, levando os usuários a confiarem demais no sistema de IA. Por exemplo, um sistema de avaliação automatizada, no caso de confiança excessiva, pode levar o professor a não revisar alguns trabalhos para garantir que o sistema de avaliação funcione bem. Isso poderia resultar em notas injustas ou imprecisas para os alunos, ou oportunidades perdidas de feedback e melhoria.

Duas maneiras de garantir que a confiança esteja no centro do design são explicabilidade e controle.

### Explicabilidade

Quando a IA ajuda a informar decisões, como transmitir conhecimento às futuras gerações, é fundamental que professores e pais entendam como as decisões da IA são tomadas. Isso é explicabilidade - entender como as aplicações de IA tomam decisões. Projetar para explicabilidade inclui adicionar detalhes de exemplos do que uma aplicação de IA pode fazer. Por exemplo, em vez de "Comece com o professor de IA", o sistema pode usar: "Resuma suas anotações para uma revisão mais fácil usando a IA."

![uma página inicial do aplicativo com uma ilustração clara da explicabilidade em aplicações de IA](../../images/explanability-in-ai.png?WT.mc_id=academic-105485-koreyst)

Outro exemplo é como a IA usa dados pessoais do usuário. Por exemplo, um usuário com a persona "aluno" pode ter limitações com base em sua persona. A IA pode não ser capaz de revelar respostas a perguntas, mas pode ajudar o usuário a pensar em como resolver um problema.

![IA respondendo a perguntas com base na persona](../../images/solving-questions.png?WT.mc_id=academic-105485-koreyst)

A última parte importante da explicabilidade é a simplificação das explicações. Alunos e professores podem não ser especialistas em IA, portanto, as explicações do que a aplicação pode ou não pode fazer devem ser simplificadas e fáceis de entender.

![explicações simplificadas sobre as capacidades da IA](../../images/simplified-explanations.png?WT.mc_id=academic-105485-koreyst)

### Controle

A IA generativa cria uma colaboração entre a IA e o usuário, onde, por exemplo, um usuário pode modificar prompts para obter resultados diferentes. Além disso, uma vez que uma saída é gerada, os usuários devem poder modificar os resultados, dando-lhes uma sensação de controle. Por exemplo, ao usar o Bing, você pode personalizar seu prompt com base no formato, tom e comprimento. Além disso, você pode fazer alterações em sua saída e modificar o resultado, conforme mostrado abaixo:

![resultados da pesquisa no Bing com opções para modificar o prompt e a saída](../../images/bing1.png?WT.mc_id=academic-105485-koreyst "Resultados da pesquisa no Bing com opções para modificar o prompt e a saída")

Outro recurso no Bing que permite ao usuário ter controle sobre o aplicativo é a capacidade de escolher participar ou sair dos dados que a IA usa. Para um aplicativo escolar, um aluno pode querer usar suas anotações, bem como os recursos dos professores como material de revisão.

![resultados da pesquisa no Bing com opções para modificar o prompt e a saída](../../images/bing2.png?WT.mc_id=academic-105485-koreyst "Resultados da pesquisa no Bing com opções para modificar o prompt e a saída")

> Ao projetar aplicações de IA, a intencionalidade é fundamental para garantir que os usuários não confiem demais, estabelecendo expectativas irreais de suas capacidades. Uma maneira de fazer isso é criar atrito entre os prompts e os resultados, lembrando ao usuário que isso é IA e não um ser humano colega.

# Projetando Aplicações de IA para Colaboração e Feedback

Como mencionado anteriormente, a IA generativa cria uma colaboração entre o usuário e a IA. A maioria das interações envolve um usuário inserindo um prompt e a IA gerando uma saída. E se a saída estiver incorreta? Como o aplicativo lida com erros, se ocorrerem? A IA culpa o usuário ou se dá ao trabalho de explicar o erro?

As aplicações de IA devem ser construídas para receber e fornecer feedback. Isso não apenas ajuda o sistema de IA a melhorar, mas também constrói confiança com os usuários. Um ciclo de feedback deve ser incluído no design, um exemplo pode ser um simples polegar para cima ou para baixo na saída.

Outra maneira de lidar com isso é comunicar claramente as capacidades e limitações do sistema. Quando um usuário comete um erro solicitando algo além das capacidades da IA, também deve haver uma maneira de lidar com isso, como mostrado abaixo.

![Dar feedback e lidar com erros](../../images/feedback-loops.png?WT.mc_id=academic-105485-koreyst)

Erros do sistema são comuns em aplicativos nos quais o usuário pode precisar de assistência com informações fora do escopo da IA ou o aplicativo pode ter um limite de quantas perguntas/assuntos um usuário pode gerar resumos. Por exemplo, um aplicativo de IA treinado com dados em assuntos limitados, como História e Matemática, pode não conseguir lidar com perguntas sobre Geografia. Para mitigar isso, o sistema de IA pode dar uma resposta como: "Desculpe, nosso produto foi treinado com dados nos seguintes assuntos..., não consigo responder à pergunta que você fez."

As aplicações de IA não são perfeitas, portanto, estão sujeitas a cometer erros. Ao projetar suas aplicações, certifique-se de criar espaço para feedback dos usuários e tratamento de erros de maneira simples e facilmente explicável.

## Tarefa

# Implementando Melhorias na sua Aplicação de IA

Ao considerar a implementação dos passos abaixo na sua aplicação de IA, você pode aprimorar a experiência do usuário:

- **Agradável:** Pense em como tornar sua aplicação mais agradável. Você está adicionando explicações em todos os lugares? Está incentivando o usuário a explorar? Como você está redigindo suas mensagens de erro?

- **Usabilidade:** Se estiver construindo um aplicativo web, certifique-se de que ele seja navegável tanto pelo mouse quanto pelo teclado.

- **Confiança e Transparência:** Não confie completamente na saída da IA. Considere como adicionar um ser humano ao processo para verificar a saída. Além disso, pense e implemente outras maneiras de alcançar confiança e transparência.

- **Controle:** Dê ao usuário controle sobre os dados que fornecem à aplicação. Implemente uma maneira de o usuário consentir ou recusar a coleta de dados na aplicação de IA.

<!-- ## [Post-lecture quiz](quiz-url) -->

## Parabéns! Você concluiu este curso

Após concluir esta lição, confira nossa [coleção de aprendizado de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar seus conhecimentos sobre IA generativa!

Parabéns! Você concluiu este curso! A criação de aplicações em IA Generativa não deve parar por aqui. Esperançosamente, você foi inspirado a começar a criar sua própria startup de IA generativa. Vá para o [Microsoft Founders Hub](https://aka.ms/genai-foundershub?WT.mc_id=academic-105485-koreyst) e inscreva-se no programa para receber suporte em sua jornada.
