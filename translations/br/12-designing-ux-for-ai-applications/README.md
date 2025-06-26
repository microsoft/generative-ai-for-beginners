<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-06-25T20:20:35+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "br"
}
-->
# Projetando UX para Aplicativos de IA

> _(Clique na imagem acima para ver o vídeo desta lição)_

A experiência do usuário é um aspecto muito importante na construção de aplicativos. Os usuários precisam ser capazes de usar seu aplicativo de maneira eficiente para realizar tarefas. Ser eficiente é uma coisa, mas você também precisa projetar aplicativos para que possam ser usados por todos, tornando-os _acessíveis_. Este capítulo focará nesta área para que você, com sorte, acabe projetando um aplicativo que as pessoas possam e queiram usar.

## Introdução

A experiência do usuário é como um usuário interage e utiliza um produto ou serviço específico, seja um sistema, ferramenta ou design. Ao desenvolver aplicativos de IA, os desenvolvedores não apenas se concentram em garantir que a experiência do usuário seja eficaz, mas também ética. Nesta lição, abordamos como construir aplicativos de Inteligência Artificial (IA) que atendam às necessidades dos usuários.

A lição abordará as seguintes áreas:

- Introdução à Experiência do Usuário e Compreensão das Necessidades dos Usuários
- Projetando Aplicativos de IA para Confiança e Transparência
- Projetando Aplicativos de IA para Colaboração e Feedback

## Objetivos de aprendizado

Após esta lição, você será capaz de:

- Compreender como construir aplicativos de IA que atendam às necessidades dos usuários.
- Projetar aplicativos de IA que promovam confiança e colaboração.

### Pré-requisito

Dedique algum tempo e leia mais sobre [experiência do usuário e design thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introdução à Experiência do Usuário e Compreensão das Necessidades dos Usuários

Em nossa startup fictícia de educação, temos dois usuários principais, professores e alunos. Cada um dos dois usuários tem necessidades únicas. Um design centrado no usuário prioriza o usuário, garantindo que os produtos sejam relevantes e benéficos para aqueles a quem se destinam.

O aplicativo deve ser **útil, confiável, acessível e agradável** para proporcionar uma boa experiência ao usuário.

### Usabilidade

Ser útil significa que o aplicativo possui funcionalidades que correspondem ao seu propósito pretendido, como automatizar o processo de correção ou gerar cartões de estudo para revisão. Um aplicativo que automatiza o processo de correção deve ser capaz de atribuir notas com precisão e eficiência ao trabalho dos alunos com base em critérios predefinidos. Da mesma forma, um aplicativo que gera cartões de estudo deve ser capaz de criar perguntas relevantes e diversificadas com base em seus dados.

### Confiabilidade

Ser confiável significa que o aplicativo pode realizar sua tarefa de forma consistente e sem erros. No entanto, a IA, assim como os humanos, não é perfeita e pode estar sujeita a erros. Os aplicativos podem encontrar erros ou situações inesperadas que exigem intervenção ou correção humana. Como você lida com erros? Na última seção desta lição, abordaremos como sistemas e aplicativos de IA são projetados para colaboração e feedback.

### Acessibilidade

Ser acessível significa estender a experiência do usuário a usuários com várias habilidades, incluindo aqueles com deficiências, garantindo que ninguém seja deixado de fora. Ao seguir diretrizes e princípios de acessibilidade, as soluções de IA tornam-se mais inclusivas, utilizáveis e benéficas para todos os usuários.

### Agradável

Ser agradável significa que o aplicativo é agradável de usar. Uma experiência do usuário atraente pode ter um impacto positivo no usuário, incentivando-o a retornar ao aplicativo e aumentando a receita do negócio.

Não é todo desafio que pode ser resolvido com IA. A IA entra para aumentar sua experiência do usuário, seja automatizando tarefas manuais ou personalizando experiências de usuário.

## Projetando Aplicativos de IA para Confiança e Transparência

Construir confiança é fundamental ao projetar aplicativos de IA. A confiança garante que um usuário tenha confiança de que o aplicativo realizará o trabalho, entregará resultados de forma consistente e os resultados serão o que o usuário precisa. Um risco nessa área é a desconfiança e a superconfiança. A desconfiança ocorre quando um usuário tem pouca ou nenhuma confiança em um sistema de IA, o que leva o usuário a rejeitar seu aplicativo. A superconfiança ocorre quando um usuário superestima a capacidade de um sistema de IA, levando os usuários a confiarem demais no sistema de IA. Por exemplo, um sistema de correção automatizado, no caso de superconfiança, pode levar o professor a não revisar alguns dos trabalhos para garantir que o sistema de correção funcione bem. Isso poderia resultar em notas injustas ou imprecisas para os alunos, ou oportunidades perdidas de feedback e melhoria.

Duas maneiras de garantir que a confiança esteja no centro do design são a explicabilidade e o controle.

### Explicabilidade

Quando a IA ajuda a informar decisões, como transmitir conhecimento para gerações futuras, é fundamental que professores e pais entendam como as decisões da IA são feitas. Isso é explicabilidade - entender como os aplicativos de IA tomam decisões. Projetar para a explicabilidade inclui adicionar detalhes de exemplos do que um aplicativo de IA pode fazer. Por exemplo, em vez de "Comece com o professor de IA", o sistema pode usar: "Resuma suas notas para uma revisão mais fácil usando IA."

Outro exemplo é como a IA usa dados de usuários e pessoais. Por exemplo, um usuário com a persona estudante pode ter limitações com base em sua persona. A IA pode não ser capaz de revelar respostas para perguntas, mas pode ajudar a guiar o usuário a pensar em como resolver um problema.

Uma última parte importante da explicabilidade é a simplificação das explicações. Alunos e professores podem não ser especialistas em IA, portanto, as explicações sobre o que o aplicativo pode ou não fazer devem ser simplificadas e fáceis de entender.

### Controle

A IA generativa cria uma colaboração entre a IA e o usuário, onde, por exemplo, um usuário pode modificar prompts para diferentes resultados. Além disso, uma vez que um resultado é gerado, os usuários devem ser capazes de modificar os resultados, dando-lhes uma sensação de controle. Por exemplo, ao usar o Bing, você pode adaptar seu prompt com base no formato, tom e comprimento. Além disso, você pode fazer alterações no seu resultado e modificar o resultado conforme mostrado abaixo:

Outro recurso no Bing que permite ao usuário ter controle sobre o aplicativo é a capacidade de optar por participar ou não dos dados que a IA usa. Para um aplicativo escolar, um aluno pode querer usar suas notas, bem como os recursos dos professores como material de revisão.

> Ao projetar aplicativos de IA, a intencionalidade é fundamental para garantir que os usuários não superestimem, estabelecendo expectativas irrealistas de suas capacidades. Uma maneira de fazer isso é criando atrito entre os prompts e os resultados. Lembrando o usuário de que esta é uma IA e não um ser humano

## Projetando Aplicativos de IA para Colaboração e Feedback

Como mencionado anteriormente, a IA generativa cria uma colaboração entre o usuário e a IA. A maioria dos engajamentos ocorre com um usuário inserindo um prompt e a IA gerando um resultado. E se o resultado estiver incorreto? Como o aplicativo lida com erros se eles ocorrerem? A IA culpa o usuário ou leva tempo para explicar o erro?

Os aplicativos de IA devem ser construídos para receber e dar feedback. Isso não apenas ajuda o sistema de IA a melhorar, mas também constrói confiança com os usuários. Um ciclo de feedback deve ser incluído no design, um exemplo pode ser um simples polegar para cima ou para baixo no resultado.

Outra maneira de lidar com isso é comunicar claramente as capacidades e limitações do sistema. Quando um usuário comete um erro solicitando algo além das capacidades da IA, também deve haver uma maneira de lidar com isso, como mostrado abaixo.

Erros de sistema são comuns em aplicativos onde o usuário pode precisar de assistência com informações fora do escopo da IA ou o aplicativo pode ter um limite sobre quantas perguntas/assuntos um usuário pode gerar resumos. Por exemplo, um aplicativo de IA treinado com dados em assuntos limitados, por exemplo, História e Matemática, pode não ser capaz de lidar com perguntas sobre Geografia. Para mitigar isso, o sistema de IA pode dar uma resposta como: "Desculpe, nosso produto foi treinado com dados nos seguintes assuntos....., não posso responder à pergunta que você fez."

Os aplicativos de IA não são perfeitos, portanto, estão sujeitos a erros. Ao projetar seus aplicativos, você deve garantir que crie espaço para feedback dos usuários e tratamento de erros de uma maneira simples e facilmente explicável.

## Tarefa

Pegue qualquer aplicativo de IA que você tenha construído até agora, considere implementar os passos abaixo em seu aplicativo:

- **Agradável:** Considere como você pode tornar seu aplicativo mais agradável. Você está adicionando explicações em todos os lugares? Você está incentivando o usuário a explorar? Como você está redigindo suas mensagens de erro?

- **Usabilidade:** Construindo um aplicativo web. Certifique-se de que seu aplicativo seja navegável tanto por mouse quanto por teclado.

- **Confiança e transparência:** Não confie completamente na IA e em seu resultado, considere como você adicionaria um humano ao processo para verificar o resultado. Além disso, considere e implemente outras maneiras de alcançar confiança e transparência.

- **Controle:** Dê ao usuário controle sobre os dados que ele fornece ao aplicativo. Implemente uma maneira de o usuário optar por participar ou não da coleta de dados no aplicativo de IA.

## Continue seu aprendizado!

Após concluir esta lição, confira nossa [coleção de aprendizado de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA generativa!

Vá para a Lição 13, onde veremos como [proteger aplicativos de IA](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para alcançar precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, é recomendada a tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.