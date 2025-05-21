<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-05-19T21:52:54+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "pt"
}
-->
# Projetando UX para Aplicações de IA

[![Projetando UX para Aplicações de IA](../../../translated_images/12-lesson-banner.f98188f63dee5f2a9016055c93c766061b9cb95b320bf29d4d2d67ada792572e.pt.png)](https://aka.ms/gen-ai-lesson12-gh?WT.mc_id=academic-105485-koreyst)

> _(Clique na imagem acima para ver o vídeo desta lição)_

A experiência do usuário é um aspecto muito importante na construção de aplicativos. Os usuários precisam ser capazes de usar seu aplicativo de maneira eficiente para realizar tarefas. Ser eficiente é uma coisa, mas você também precisa projetar aplicativos para que possam ser usados por todos, tornando-os _acessíveis_. Este capítulo focará nesta área para que você acabe projetando um aplicativo que as pessoas possam e queiram usar.

## Introdução

Experiência do usuário é como um usuário interage e utiliza um produto ou serviço específico, seja um sistema, ferramenta ou design. Ao desenvolver aplicações de IA, os desenvolvedores não apenas se concentram em garantir que a experiência do usuário seja eficaz, mas também ética. Nesta lição, abordamos como construir aplicações de Inteligência Artificial (IA) que atendam às necessidades dos usuários.

A lição cobrirá as seguintes áreas:

- Introdução à Experiência do Usuário e Compreensão das Necessidades dos Usuários
- Projetando Aplicações de IA para Confiança e Transparência
- Projetando Aplicações de IA para Colaboração e Feedback

## Objetivos de aprendizado

Após esta lição, você será capaz de:

- Compreender como construir aplicações de IA que atendam às necessidades dos usuários.
- Projetar aplicações de IA que promovam confiança e colaboração.

### Pré-requisito

Dedique algum tempo para ler mais sobre [experiência do usuário e design thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introdução à Experiência do Usuário e Compreensão das Necessidades dos Usuários

Em nossa startup fictícia de educação, temos dois usuários principais, professores e alunos. Cada um dos dois usuários tem necessidades únicas. Um design centrado no usuário prioriza o usuário, garantindo que os produtos sejam relevantes e benéficos para aqueles a quem se destinam.

O aplicativo deve ser **útil, confiável, acessível e agradável** para proporcionar uma boa experiência ao usuário.

### Usabilidade

Ser útil significa que o aplicativo tem funcionalidades que correspondem ao seu propósito pretendido, como automatizar o processo de avaliação ou gerar cartões de memória para revisão. Um aplicativo que automatiza o processo de avaliação deve ser capaz de atribuir notas de forma precisa e eficiente ao trabalho dos alunos com base em critérios pré-definidos. Da mesma forma, um aplicativo que gera cartões de memória para revisão deve ser capaz de criar perguntas relevantes e diversificadas com base em seus dados.

### Confiabilidade

Ser confiável significa que o aplicativo pode realizar sua tarefa de forma consistente e sem erros. No entanto, a IA, assim como os humanos, não é perfeita e pode estar sujeita a erros. Os aplicativos podem encontrar erros ou situações inesperadas que exigem intervenção ou correção humana. Como você lida com erros? Na última seção desta lição, abordaremos como os sistemas e aplicativos de IA são projetados para colaboração e feedback.

### Acessibilidade

Ser acessível significa estender a experiência do usuário a usuários com diversas habilidades, incluindo aqueles com deficiências, garantindo que ninguém seja deixado de fora. Ao seguir diretrizes e princípios de acessibilidade, as soluções de IA tornam-se mais inclusivas, utilizáveis e benéficas para todos os usuários.

### Agradável

Ser agradável significa que o aplicativo é prazeroso de usar. Uma experiência de usuário atraente pode ter um impacto positivo no usuário, incentivando-o a retornar ao aplicativo e aumentando a receita do negócio.

![imagem ilustrando considerações de UX em IA](../../../translated_images/uxinai.26a003eb0524d011d3e36d15f6837df5be66ee0d965ee0df6d004edd5097a87d.pt.png)

Nem todo desafio pode ser resolvido com IA. A IA vem para aumentar sua experiência do usuário, seja automatizando tarefas manuais ou personalizando experiências do usuário.

## Projetando Aplicações de IA para Confiança e Transparência

Construir confiança é fundamental ao projetar aplicações de IA. A confiança garante que um usuário tenha confiança de que o aplicativo fará o trabalho, entregará resultados consistentemente e que os resultados são o que o usuário precisa. Um risco nessa área é a desconfiança e a confiança excessiva. A desconfiança ocorre quando um usuário tem pouca ou nenhuma confiança em um sistema de IA, levando o usuário a rejeitar seu aplicativo. A confiança excessiva ocorre quando um usuário superestima a capacidade de um sistema de IA, levando os usuários a confiar demais no sistema de IA. Por exemplo, um sistema de avaliação automatizado, no caso de confiança excessiva, pode levar o professor a não revisar algumas das provas para garantir que o sistema de avaliação funcione bem. Isso poderia resultar em notas injustas ou imprecisas para os alunos, ou oportunidades perdidas de feedback e melhoria.

Duas maneiras de garantir que a confiança esteja no centro do design são explicabilidade e controle.

### Explicabilidade

Quando a IA ajuda a informar decisões, como transmitir conhecimento às gerações futuras, é fundamental que professores e pais entendam como as decisões da IA são tomadas. Isso é explicabilidade - entender como as aplicações de IA tomam decisões. Projetar para explicabilidade inclui adicionar detalhes de exemplos do que uma aplicação de IA pode fazer. Por exemplo, em vez de "Comece com o professor de IA", o sistema pode usar: "Resuma suas notas para uma revisão mais fácil usando IA."

![uma página inicial de aplicativo com ilustração clara de explicabilidade em aplicações de IA](../../../translated_images/explanability-in-ai.19a61ee8eec9aec2d55d420c49cc3bb167db208c05bddb8d4e1e9e10ea8746b8.pt.png)

Outro exemplo é como a IA usa dados de usuários e pessoais. Por exemplo, um usuário com a persona estudante pode ter limitações com base em sua persona. A IA pode não ser capaz de revelar respostas para perguntas, mas pode ajudar a guiar o usuário a pensar sobre como ele pode resolver um problema.

![IA respondendo a perguntas com base na persona](../../../translated_images/solving-questions.9158f66fb9fd71ed57fd00978358d14dbccc72bd2b1e4db5140fcb1579aef295.pt.png)

Uma última parte importante da explicabilidade é a simplificação das explicações. Alunos e professores podem não ser especialistas em IA, portanto, as explicações sobre o que o aplicativo pode ou não fazer devem ser simplificadas e fáceis de entender.

![explicações simplificadas sobre capacidades de IA](../../../translated_images/simplified-explanations.4a23e7b2260406a771a2cd853970a0661388a63f1900737935c0a788daf16dc8.pt.png)

### Controle

A IA generativa cria uma colaboração entre a IA e o usuário, onde, por exemplo, um usuário pode modificar prompts para diferentes resultados. Além disso, uma vez que um resultado é gerado, os usuários devem ser capazes de modificar os resultados, dando-lhes uma sensação de controle. Por exemplo, ao usar o Bing, você pode ajustar seu prompt com base no formato, tom e comprimento. Além disso, você pode adicionar alterações ao seu resultado e modificar o resultado conforme mostrado abaixo:

![Resultados de pesquisa do Bing com opções para modificar o prompt e o resultado](../../../translated_images/bing1.6024fe7d103ff4b54c58b873654403a1e56f81010da05a1f0a210c5ac7a1b8b5.pt.png)

Outro recurso no Bing que permite ao usuário ter controle sobre o aplicativo é a capacidade de optar por participar e sair dos dados que a IA usa. Para um aplicativo escolar, um aluno pode querer usar suas notas, bem como os recursos dos professores como material de revisão.

![Resultados de pesquisa do Bing com opções para modificar o prompt e o resultado](../../../translated_images/bing2.a01fd420e9d52912126965a59c1766e5865f4dd9aaa45408d525e717d0ef3cce.pt.png)

> Ao projetar aplicações de IA, a intencionalidade é fundamental para garantir que os usuários não confiem excessivamente, definindo expectativas irrealistas sobre suas capacidades. Uma maneira de fazer isso é criar fricção entre os prompts e os resultados. Lembrando o usuário de que isso é IA e não um ser humano

## Projetando Aplicações de IA para Colaboração e Feedback

Como mencionado anteriormente, a IA generativa cria uma colaboração entre o usuário e a IA. A maioria dos engajamentos é com um usuário inserindo um prompt e a IA gerando um resultado. E se o resultado estiver incorreto? Como o aplicativo lida com erros se ocorrerem? A IA culpa o usuário ou leva tempo para explicar o erro?

As aplicações de IA devem ser construídas para receber e dar feedback. Isso não apenas ajuda o sistema de IA a melhorar, mas também constrói confiança com os usuários. Um loop de feedback deve ser incluído no design, um exemplo pode ser um simples polegar para cima ou para baixo no resultado.

Outra maneira de lidar com isso é comunicar claramente as capacidades e limitações do sistema. Quando um usuário comete um erro solicitando algo além das capacidades da IA, também deve haver uma maneira de lidar com isso, como mostrado abaixo.

![Dando feedback e lidando com erros](../../../translated_images/feedback-loops.2abf91e576a435333eb1b37c823a69497337abc5b50ff80c4b9ddbd52bfdbf84.pt.png)

Erros de sistema são comuns em aplicativos onde o usuário pode precisar de assistência com informações fora do escopo da IA ou o aplicativo pode ter um limite de quantas perguntas/assuntos um usuário pode gerar resumos. Por exemplo, um aplicativo de IA treinado com dados sobre assuntos limitados, por exemplo, História e Matemática, pode não ser capaz de lidar com perguntas sobre Geografia. Para mitigar isso, o sistema de IA pode dar uma resposta como: "Desculpe, nosso produto foi treinado com dados nos seguintes assuntos....., não posso responder à pergunta que você fez."

As aplicações de IA não são perfeitas, portanto, estão sujeitas a cometer erros. Ao projetar seus aplicativos, você deve garantir que crie espaço para feedback dos usuários e tratamento de erros de forma simples e facilmente explicável.

## Tarefa

Pegue qualquer aplicativo de IA que você tenha construído até agora, considere implementar os passos abaixo em seu aplicativo:

- **Agradável:** Considere como você pode tornar seu aplicativo mais agradável. Você está adicionando explicações em todos os lugares? Está incentivando o usuário a explorar? Como você está redigindo suas mensagens de erro?

- **Usabilidade:** Construindo um aplicativo web. Certifique-se de que seu aplicativo seja navegável tanto por mouse quanto por teclado.

- **Confiança e transparência:** Não confie completamente na IA e em seu resultado, considere como você adicionaria um humano ao processo para verificar o resultado. Além disso, considere e implemente outras maneiras de alcançar confiança e transparência.

- **Controle:** Dê ao usuário controle sobre os dados que ele fornece ao aplicativo. Implemente uma maneira de o usuário optar por participar e sair da coleta de dados na aplicação de IA.

## Continue seu aprendizado!

Após concluir esta lição, confira nossa [coleção de aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Vá para a Lição 13, onde vamos analisar como [proteger aplicações de IA](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.