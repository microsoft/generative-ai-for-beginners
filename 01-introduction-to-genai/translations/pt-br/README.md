# Introdução à Inteligência Artificial Generativa e Grandes Modelos de Linguagem

[![Introduction to Generative AI and Large Language Models](../../images/01-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed.html?id=36c6795a-e63c-46dd-8d69-df8bbe6e7bc9?WT.mc_id=academic-105485-koreyst)

_(Clique na imagem acima para assistir ao vídeo desta lição)_

A Inteligência Artificial Generativa é uma forma de inteligência artificial capaz de gerar texto, imagens e outros tipos de conteúdo. O que a faz uma tecnologia fantástica é que ela democratiza a IA. Além disso, qualquer pessoa pode usá-la com apenas uma pequena frase, uma sentença escrita em uma linguagem natural. Não é necessário aprender uma linguagem como Java ou SQL para realizar algo significativo. Tudo o que você precisa fazer é usar sua própria linguagem, declarar o que deseja e uma sugestão de um modelo de IA será gerada. As aplicações e o impacto disso são enormes: você pode escrever ou compreender relatórios, criar aplicações e muito mais, tudo em questão de segundos.

Neste currículo, exploraremos como nossa startup aproveita a IA generativa para desbloquear novos cenários no mundo da educação e como lidamos com os desafios inevitáveis relacionados às implicações sociais de sua aplicação e às limitações tecnológicas.

## Introdução

Esta lição abordará:

- Introdução ao cenário de negócios: nossa ideia de startup e missão.
- Inteligência Artificial Generativa e como chegamos ao cenário tecnológico atual.
- Funcionamento interno de um grande modelo de linguagem.
- Principais capacidades e casos de uso práticos de Grandes Modelos de Linguagem.

## Objetivos de Aprendizado

Após completar esta lição, você entenderá:

- O que é a Inteligência Artificial Generativa e como os Grandes Modelos de Linguagem funcionam.
- Como você pode aproveitar os Grandes Modelos de Linguagem para diferentes casos de uso, com foco em cenários de educação.

## Cenário: nossa startup educacional

A Inteligência Artificial Generativa (IA) representa o auge da tecnologia de IA, ultrapassando os limites do que antes era considerado impossível. Modelos de IA generativa têm várias capacidades e aplicações. Porém, neste currículo, exploraremos como ela está revolucionando a educação por meio de uma startup fictícia. Nos referiremos a essa startup como _nossa startup_. `Nossa startup` atua no domínio da educação com a ambiciosa declaração de missão:

> _Melhorar a acessibilidade na aprendizagem, em escala global, garantindo acesso equitativo à educação e proporcionando experiências de aprendizagem personalizadas a cada aluno(a), de acordo com suas necessidades_.

A equipe de nossa startup está ciente de que não será capaz de alcançar esse objetivo sem aproveitar uma das ferramentas mais poderosas dos tempos modernos - Grandes Modelos de Linguagem (LLMs).

A IA generativa deve revolucionar a maneira como aprendemos e ensinamos hoje, com os(as) alunos(as) tendo à disposição professores(as) virtuais 24 horas por dia, que fornecem vastas quantidades de informações e exemplos, e professores(as) capazes de alavancar ferramentas inovadoras para avaliar seus/suas alunos(as) e fornecer feedback.

![Five young students looking at a monitor - image by DALLE2](../../images/students-by-DALLE2.png?WT.mc_id=academic-105485-koreyst)

Para começar, vamos definir alguns conceitos e terminologia básica que usaremos ao longo do currículo.

## Como surgiu a IA Generativa?

Apesar da extraordinária _hype_ criada recentemente com o anúncio de modelos de IA generativa, essa tecnologia está em desenvolvimento há décadas, com os primeiros esforços de pesquisa datando dos anos 60. Agora estamos em um ponto em que a IA possui capacidades cognitivas humanas como conversação, como mostrado por exemplo, no [OpenAI ChatGPT](https://openai.com/chatgpt?WT.mc_id=academic-105485-koreyst) ou no [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), que também utiliza um modelo GPT para a pesquisa na web e conversas do Bing.

Voltando um pouco, os primeiros protótipos de IA consistiam em chatbots datilografados, baseando-se em uma base de conhecimento extraída de um grupo de especialistas e representada em um computador. As respostas na base de conhecimento eram acionadas por palavras-chave que apareciam no texto de entrada.
No entanto, logo ficou claro que tal abordagem, usando chatbots datilografados, não se escalava bem.

### Uma abordagem estatística para a IA: Aprendizado de Máquina

Um ponto de virada ocorreu durante os anos 90, com a aplicação de uma abordagem estatística à análise de texto. Isso levou ao desenvolvimento de novos algoritmos - conhecidos com o nome de aprendizado de máquina - capazes de aprender padrões a partir de dados, sem serem programados explicitamente. Essa abordagem permite que uma máquina simule a compreensão da linguagem humana: um modelo estatístico é treinado em pares de texto e rótulo, permitindo que o modelo classifique um texto de entrada desconhecido com um rótulo predefinido que representa a intenção da mensagem.

### Redes neurais e assistentes virtuais modernos

Em tempos mais recentes, a evolução tecnológica do hardware, capaz de lidar com maiores quantidades de dados e cálculos mais complexos, encorajou a pesquisa nos campos de IA, levando ao desenvolvimento de algoritmos avançados de aprendizado de máquina - chamados de redes neurais ou algoritmos de aprendizado profundo.

As redes neurais (ou as Redes Neurais Recorrentes - `RNNs`) aprimoraram significativamente o processamento de linguagem natural, permitindo a representação do significado do texto de uma maneira mais significativa, valorizando o contexto de uma palavra em uma frase.

Essa é a tecnologia que impulsionou os assistentes virtuais nascidos na primeira década do novo século, muito proficientes na interpretação da linguagem humana, identificando uma necessidade e executando uma ação para satisfazê-la - como responder com um script predefinido ou consumir um serviço de terceiros.

### Atualmente, a IA Generativa

Foi assim que chegamos à IA Generativa de hoje, que pode ser vista como um subconjunto de aprendizado profundo.

![IA, ML, AP e IA Generativa](../../images/AI-diagram.png?WT.mc_id=academic-105485-koreyst)

Depois de décadas de pesquisa no campo da IA, uma nova arquitetura de modelo - chamada _Transformer_ - superou os limites das `RNNs`. Sendo capaz de receber sequências de texto muito mais longas como entrada. Os `Transformers` são baseados no mecanismo de atenção, permitindo que o modelo dê pesos diferentes às entradas que recebe, _prestando mais atenção_ onde as informações mais relevantes estão concentradas, independentemente de sua ordem na sequência de texto.

A maioria dos modelos recentes da IA generativa - também conhecidos como Grandes Modelos de Linguagem (LLMs), trabalham com entradas e saídas textuais e que, são de fato, baseados nessa arquitetura. O que é interessante sobre esses modelos - treinados em uma enorme quantidade de dados não rotulados de diversas fontes, como: livros, artigos e sites - é que eles podem ser adaptados para uma ampla variedade de tarefas e gerar texto gramaticalmente correto com uma semelhança de criatividade. Portanto, não apenas aumentaram incrivelmente a capacidade de uma máquina _entender_ um texto de entrada. Mas também habilitaram sua capacidade de gerar uma resposta original em linguagem humana.

## Como os Grandes Modelos de Linguagem funcionam?

No próximo capítulo, vamos explorar diferentes tipos de modelos de IA generativa. Por enquanto, vamos dar uma olhada em como os grandes modelos de linguagem funcionam, com foco nos modelos do OpenAI GPT (`Generative Pre-trained Transformer`).

- **Tokenizador, texto para números**: Grandes Modelos de Linguagem, recebem um texto como entrada e geram um texto como saída. No entanto, sendo modelos estatísticos, eles funcionam muito melhor com números do que sequências de texto. É por isso que cada entrada no modelo é processada por um `tokenizador` antes de ser usada pelo modelo principal. Um `token` é um pedaço de texto - consistindo em um número variável de caracteres, portanto, a principal tarefa do tokenizador é dividir a entrada em uma matriz de tokens. Em seguida, cada token é mapeado com um índice de token, que é a codificação inteira do trecho de texto original.

![Example of tokenization](../../images/tokenizer-example.png?WT.mc_id=academic-105485-koreyst)

- **Previsão de tokens de saída**: Dados `n` tokens como entrada (com o máximo `n` variando de um modelo para outro), o modelo é capaz de prever um token como saída. Esse token é então incorporado à entrada da próxima iteração em um padrão de janela expansiva. Possibilitando assim, uma melhor experiência do usuário em obter uma (ou várias) sentenças como resposta. Isso explica por que, se você já brincou com o ChatGPT, pode ter notado que às vezes parece que ele para no meio de uma frase.

- **Processo de seleção, distribuição de probabilidade**: O token de saída é escolhido pelo modelo de acordo com a probabilidade de ocorrer após a sequência de texto atual. Isso ocorre porque o modelo prevê uma distribuição de probabilidade sobre todos os possíveis _próximos tokens_ calculados com base em seu treinamento. No entanto, nem sempre o token com a maior probabilidade é escolhido na distribuição resultante. Um grau de aleatoriedade é adicionado a essa escolha, de forma que o modelo age de maneira não determinística - não obtemos a mesma saída exata para a mesma entrada. Esse grau de aleatoriedade é adicionado para simular o processo de pensamento criativo e pode ser ajustado usando um parâmetro do modelo chamado temperatura.

## Como nossa startup pode aproveitar os Grandes Modelos de Linguagem?

Agora que temos uma melhor compreensão de como os grandes modelos de linguagem funcionam, vamos ver alguns exemplos práticos das tarefas mais comuns que eles podem realizar muito bem, com foco em nosso cenário de negócios.
Dissemos que a principal capacidade de um Grande Modelo de Linguagem é: _gerar um texto do zero, a partir de uma entrada textual, escrita em linguagem natural_.

Mas que tipo de entrada e saída textual?
A entrada de um grande modelo de linguagem é conhecida como `prompt`. Enquanto a saída é conhecida como `completion`, termo que se refere ao mecanismo do modelo de gerar o próximo token para completar a entrada atual. Vamos nos aprofundar no que é um prompt e como projetá-lo de maneira a obter o máximo de nosso modelo. Agora, vamos apenas dizer que um prompt pode incluir:

- Uma **instrução** especificando o tipo de saída que esperamos do modelo. Essa instrução às vezes pode incorporar alguns exemplos ou alguns dados adicionais.

  1. Resumo de um artigo, livro, análises de produtos e muito mais. Juntamente com a extração de insights de dados não estruturados.
     ![Exemplo de resumo](../../images/summarization-example.png?WT.mc_id=academic-105485-koreyst)

  2. Ideação criativa e design de um artigo, uma redação, uma tarefa ou mais.
     ![Exemplo de escrita criativa](../../images/creative-writing-example.png?WT.mc_id=academic-105485-koreyst)

- Uma **pergunta** feita na forma de uma conversa com um agente.
  ![Exemplo de conversa](../../images/conversation-example.png?WT.mc_id=academic-105485-koreyst)

- Um trecho de **texto a ser completado** que implicitamente é um pedido de assistência na escrita.
  ![Exemplo de conclusão de texto](../../images/text-completion-example.png?WT.mc_id=academic-105485-koreyst)

- Um trecho de **código** juntamente com a solicitação de explicá-lo e documentá-lo ou um comentário pedindo para gerar um trecho de código que execute uma tarefa específica.
  ![Exemplo de programação](../../images/coding-example.png?WT.mc_id=academic-105485-koreyst)

Os exemplos acima são bastante simples e não pretendem ser uma demonstração exaustiva das capacidades dos Grandes Modelos de Linguagem. Eles apenas querem mostrar o potencial de uso da IA generativa, em particular, mas não limitado ao contexto educacional.

Além disso, a saída de um modelo de IA generativa não é perfeita e, às vezes, a criatividade do modelo pode funcionar contra ele, resultando em uma saída que é uma combinação de palavras que o usuário humano pode interpretar como uma mistificação da realidade ou pode ser ofensiva. A IA Generativa não é inteligente - pelo menos na definição mais abrangente de inteligência, incluindo o raciocínio crítico e criativo ou a inteligência emocional; ela não é determinística e não é confiável, uma vez que alucinações, como referências, conteúdo e declarações errôneas, podem ser combinadas com informações corretas e apresentadas de maneira persuasiva e confiante. Nas próximas lições, lidaremos com todas essas limitações e veremos o que podemos fazer para mitigá-las.

# Tarefa

Sua tarefa é estudar mais sobre [IA Generativa](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) e tentar identificar uma área onde você adicionaria IA Generativa hoje mas que ainda não a possui. Como o impacto seria diferente de fazer as coisas do "jeito antigo"? Você pode fazer algo que não era possível antes ou que seria mais rápido? Escreva um resumo de 300 palavras sobre como sua startup da IA dos sonhos seria e inclua cabeçalhos como:

- "Problema"
- "Como eu usaria a IA"
- "Impacto"
- E, como opção, um plano de negócios.

Se você fizer essa tarefa, poderá até estar pronto para se inscrever no [Microsoft's Incubator](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) para fundadores de startups. Eles oferecem créditos para Azure, OpenAI, mentoria e muito mais. Confira agora mesmo!

## Verificação de conhecimento

O que é verdade sobre Grandes Modelos de Linguagem?

1. Você obtém a mesma resposta exata toda vez.
2. Eles fazem as coisas perfeitamente. São ótimos em somar números, produzir código funcional etc.
3. A resposta pode variar, mesmo ao usar o mesmo prompt. Além disso, eles são ótimos em fornecer um primeiro rascunho de algo, seja texto ou código. Mas você precisa melhorar os resultados.

**Resposta:** 3, um `LLM` é _não-determinístico_. A resposta varia, em você controlar sua variação por meio de uma configuração de `temperatura`. Além disso, você não deve esperar que ele faça as coisas perfeitamente. Ele está aqui para fazer o trabalho pesado para você, o que muitas vezes significa que você obtém uma boa primeira tentativa de algo que precisa melhorar gradualmente.

## Ótimo trabalho! A Jornada Continua

Deseja aprender mais sobre diferentes conceitos de IA Generativa? Acesse a [página de Aprendizado Contínuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre este tópico.

Vá para a Lição 2, onde veremos como [Explorar e comparar diferentes tipos de LLM](../../../02-exploring-and-comparing-different-llms/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)!
