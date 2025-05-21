<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T09:09:17+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "br"
}
-->
# Introdução à IA Generativa e Modelos de Linguagem de Grande Porte

[![Introdução à IA Generativa e Modelos de Linguagem de Grande Porte](../../../translated_images/01-lesson-banner.f4869237c4117400e7a80dd1e19ba2929e1491e5dbe494ad705533362f402e81.br.png)](https://aka.ms/gen-ai-lesson-1-gh?WT.mc_id=academic-105485-koreyst)

_(Clique na imagem acima para ver o vídeo desta lição)_

A IA generativa é uma inteligência artificial capaz de gerar texto, imagens e outros tipos de conteúdo. O que a torna uma tecnologia fantástica é que ela democratiza a IA; qualquer pessoa pode usá-la com apenas um prompt de texto, uma frase escrita em linguagem natural. Não há necessidade de aprender uma linguagem como Java ou SQL para realizar algo significativo; basta usar sua linguagem, declarar o que você quer, e um modelo de IA sugere algo. As aplicações e o impacto disso são enormes; você pode escrever ou entender relatórios, criar aplicativos e muito mais, tudo em questão de segundos.

Neste currículo, vamos explorar como nossa startup utiliza a IA generativa para desbloquear novos cenários no mundo da educação e como enfrentamos os desafios inevitáveis associados às implicações sociais de sua aplicação e às limitações tecnológicas.

## Introdução

Esta lição abordará:

- Introdução ao cenário de negócios: nossa ideia de startup e missão.
- IA generativa e como chegamos ao panorama tecnológico atual.
- Funcionamento interno de um modelo de linguagem de grande porte.
- Principais capacidades e casos de uso práticos de Modelos de Linguagem de Grande Porte.

## Objetivos de Aprendizagem

Após concluir esta lição, você entenderá:

- O que é IA generativa e como funcionam os Modelos de Linguagem de Grande Porte.
- Como você pode utilizar modelos de linguagem de grande porte para diferentes casos de uso, com foco em cenários educacionais.

## Cenário: nossa startup educacional

A Inteligência Artificial (IA) Generativa representa o auge da tecnologia de IA, ultrapassando os limites do que antes era considerado impossível. Os modelos de IA generativa têm várias capacidades e aplicações, mas para este currículo vamos explorar como está revolucionando a educação através de uma startup fictícia. Vamos nos referir a esta startup como _nossa startup_. Nossa startup atua no domínio educacional com a ambiciosa missão de

> _melhorar a acessibilidade na aprendizagem, em escala global, garantindo acesso equitativo à educação e proporcionando experiências de aprendizagem personalizadas para cada aluno, de acordo com suas necessidades_.

Nossa equipe de startup está ciente de que não conseguiremos alcançar esse objetivo sem utilizar uma das ferramentas mais poderosas dos tempos modernos – Modelos de Linguagem de Grande Porte (LLMs).

A IA generativa deve revolucionar a maneira como aprendemos e ensinamos hoje, com estudantes tendo à disposição professores virtuais 24 horas por dia, que fornecem vastas quantidades de informações e exemplos, e professores capazes de usar ferramentas inovadoras para avaliar seus alunos e dar feedback.

![Cinco jovens estudantes olhando para um monitor - imagem por DALLE2](../../../translated_images/students-by-DALLE2.f0fce818ebbcca8f5f9e8733e3c67158a1162fe0089c498c35da405fc9e9ee4e.br.png)

Para começar, vamos definir alguns conceitos básicos e terminologia que usaremos ao longo do currículo.

## Como conseguimos a IA Generativa?

Apesar do extraordinário _hype_ criado recentemente pelo anúncio de modelos de IA generativa, essa tecnologia vem sendo desenvolvida há décadas, com os primeiros esforços de pesquisa datando dos anos 60. Estamos agora em um ponto em que a IA tem capacidades cognitivas humanas, como a conversa, como mostrado, por exemplo, pelo [OpenAI ChatGPT](https://openai.com/chatgpt) ou [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), que também usa um modelo GPT para as conversas de busca na web Bing.

Voltando um pouco, os primeiros protótipos de IA consistiam em chatbots datilografados, baseados em uma base de conhecimento extraída de um grupo de especialistas e representada em um computador. As respostas na base de conhecimento eram acionadas por palavras-chave que apareciam no texto de entrada.
No entanto, logo ficou claro que tal abordagem, usando chatbots datilografados, não escalava bem.

### Uma abordagem estatística para IA: Aprendizado de Máquina

Um ponto de virada chegou durante os anos 90, com a aplicação de uma abordagem estatística à análise de texto. Isso levou ao desenvolvimento de novos algoritmos – conhecidos como aprendizado de máquina – capazes de aprender padrões a partir de dados sem serem explicitamente programados. Essa abordagem permite que as máquinas simulem a compreensão da linguagem humana: um modelo estatístico é treinado em pares de texto-rotulo, permitindo que o modelo classifique o texto de entrada desconhecido com um rótulo pré-definido que representa a intenção da mensagem.

### Redes neurais e assistentes virtuais modernos

Nos últimos anos, a evolução tecnológica do hardware, capaz de lidar com maiores quantidades de dados e cálculos mais complexos, incentivou a pesquisa em IA, levando ao desenvolvimento de algoritmos avançados de aprendizado de máquina conhecidos como redes neurais ou algoritmos de aprendizado profundo.

Redes neurais (e em particular Redes Neurais Recorrentes – RNNs) melhoraram significativamente o processamento de linguagem natural, permitindo a representação do significado do texto de forma mais significativa, valorizando o contexto de uma palavra em uma sentença.

Essa é a tecnologia que alimentou os assistentes virtuais nascidos na primeira década do novo século, muito proficientes em interpretar a linguagem humana, identificar uma necessidade e realizar uma ação para satisfazê-la – como responder com um script pré-definido ou consumir um serviço de terceiros.

### Hoje em dia, IA Generativa

Então, foi assim que chegamos à IA Generativa hoje, que pode ser vista como um subconjunto do aprendizado profundo.

![IA, ML, DL e IA Generativa](../../../translated_images/AI-diagram.cab4093fe39583ffc0d19c22eab2ef79aaf4ef307ea91ac18f97aa008abeb45c.br.png)

Após décadas de pesquisa no campo da IA, uma nova arquitetura de modelo – chamada _Transformer_ – superou os limites das RNNs, sendo capaz de receber sequências de texto muito mais longas como entrada. Os Transformers são baseados no mecanismo de atenção, permitindo que o modelo atribua diferentes pesos às entradas que recebe, 'prestando mais atenção' onde as informações mais relevantes estão concentradas, independentemente de sua ordem na sequência de texto.

A maioria dos modelos de IA generativa recentes – também conhecidos como Modelos de Linguagem de Grande Porte (LLMs), já que trabalham com entradas e saídas textuais – são, de fato, baseados nesta arquitetura. O que é interessante sobre esses modelos – treinados em uma enorme quantidade de dados não rotulados de diversas fontes como livros, artigos e sites – é que eles podem ser adaptados a uma ampla variedade de tarefas e gerar texto gramaticalmente correto com uma aparência de criatividade. Portanto, não apenas melhoraram incrivelmente a capacidade de uma máquina de 'entender' um texto de entrada, mas também habilitaram sua capacidade de gerar uma resposta original em linguagem humana.

## Como funcionam os modelos de linguagem de grande porte?

No próximo capítulo, vamos explorar diferentes tipos de modelos de IA generativa, mas por enquanto, vamos dar uma olhada em como os modelos de linguagem de grande porte funcionam, com foco nos modelos GPT (Generative Pre-trained Transformer) da OpenAI.

- **Tokenizador, texto para números**: Modelos de Linguagem de Grande Porte recebem um texto como entrada e geram um texto como saída. No entanto, sendo modelos estatísticos, eles funcionam muito melhor com números do que com sequências de texto. É por isso que cada entrada no modelo é processada por um tokenizador, antes de ser usada pelo modelo principal. Um token é um pedaço de texto – consistindo em um número variável de caracteres, então a principal tarefa do tokenizador é dividir a entrada em um array de tokens. Em seguida, cada token é mapeado com um índice de token, que é a codificação inteira do pedaço de texto original.

![Exemplo de tokenização](../../../translated_images/tokenizer-example.09b30260020c3c1d21640d5729bf21332e179331bef6b8b6944627f6f722caf8.br.png)

- **Previsão de tokens de saída**: Dado n tokens como entrada (com max n variando de um modelo para outro), o modelo é capaz de prever um token como saída. Este token é então incorporado na entrada da próxima iteração, em um padrão de janela expansiva, permitindo uma melhor experiência do usuário ao receber uma (ou múltiplas) sentença como resposta. Isso explica por que, se você já brincou com o ChatGPT, pode ter notado que às vezes parece que ele para no meio de uma frase.

- **Processo de seleção, distribuição de probabilidade**: O token de saída é escolhido pelo modelo de acordo com sua probabilidade de ocorrer após a sequência de texto atual. Isso ocorre porque o modelo prevê uma distribuição de probabilidade sobre todos os possíveis 'próximos tokens', calculada com base em seu treinamento. No entanto, nem sempre o token com a maior probabilidade é escolhido da distribuição resultante. Um grau de aleatoriedade é adicionado a essa escolha, de forma que o modelo age de maneira não determinística - não obtemos exatamente a mesma saída para a mesma entrada. Esse grau de aleatoriedade é adicionado para simular o processo de pensamento criativo e pode ser ajustado usando um parâmetro de modelo chamado temperatura.

## Como nossa startup pode utilizar Modelos de Linguagem de Grande Porte?

Agora que temos uma melhor compreensão do funcionamento interno de um modelo de linguagem de grande porte, vamos ver alguns exemplos práticos das tarefas mais comuns que eles podem realizar muito bem, com um olhar para nosso cenário de negócios.
Dissemos que a principal capacidade de um Modelo de Linguagem de Grande Porte é _gerar um texto do zero, começando a partir de uma entrada textual, escrita em linguagem natural_.

Mas que tipo de entrada e saída textual?
A entrada de um modelo de linguagem de grande porte é conhecida como prompt, enquanto a saída é conhecida como completion, termo que se refere ao mecanismo do modelo de gerar o próximo token para completar a entrada atual. Vamos nos aprofundar no que é um prompt e como projetá-lo de forma a obter o máximo de nosso modelo. Mas por enquanto, vamos apenas dizer que um prompt pode incluir:

- Uma **instrução** especificando o tipo de saída que esperamos do modelo. Essa instrução às vezes pode incluir alguns exemplos ou alguns dados adicionais.

  1. Resumo de um artigo, livro, avaliações de produtos e mais, junto com a extração de insights de dados não estruturados.
    
    ![Exemplo de resumo](../../../translated_images/summarization-example.657a46c47f91b0bd88f66bff8ffe222aa191de2b57ca790b3791a29ad224a807.br.png)
  
  2. Ideação criativa e design de um artigo, ensaio, tarefa ou mais.
      
     ![Exemplo de escrita criativa](../../../translated_images/creative-writing-example.c739bb30fe99dc42dc039c166694fd644983376af24548793db26b582b149e7b.br.png)

- Uma **pergunta**, feita na forma de uma conversa com um agente.
  
  ![Exemplo de conversa](../../../translated_images/conversation-example.b2c7cda5634819bd2f67f36084e3cf38f867b18b6628b66d340398525fa9edb1.br.png)

- Um pedaço de **texto para completar**, que implicitamente é um pedido de assistência na escrita.
  
  ![Exemplo de conclusão de texto](../../../translated_images/text-completion-example.524a39b86473c6d85f9ad472e7c5ee569c040fa6f42f54b2a08e28118b9f13c2.br.png)

- Um pedaço de **código** juntamente com o pedido de explicar e documentar, ou um comentário pedindo para gerar um pedaço de código que realiza uma tarefa específica.
  
  ![Exemplo de codificação](../../../translated_images/coding-example.5c46e1eb38083c0fffad9a244a1fb53394d080fce299ec0d121f4263cacee014.br.png)

Os exemplos acima são bastante simples e não pretendem ser uma demonstração exaustiva das capacidades dos Modelos de Linguagem de Grande Porte. Eles têm o objetivo de mostrar o potencial do uso de IA generativa, em particular, mas não limitado a contextos educacionais.

Além disso, a saída de um modelo de IA generativa não é perfeita e às vezes a criatividade do modelo pode trabalhar contra ele, resultando em uma saída que é uma combinação de palavras que o usuário humano pode interpretar como uma mistificação da realidade, ou pode ser ofensiva. A IA generativa não é inteligente - pelo menos na definição mais abrangente de inteligência, incluindo raciocínio crítico e criativo ou inteligência emocional; não é determinística e não é confiável, pois fabricações, como referências errôneas, conteúdo e declarações, podem ser combinadas com informações corretas e apresentadas de maneira persuasiva e confiante. Nas lições seguintes, lidaremos com todas essas limitações e veremos o que podemos fazer para mitigá-las.

## Tarefa

Sua tarefa é ler mais sobre [IA generativa](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) e tentar identificar uma área onde você adicionaria IA generativa hoje que não a tem. Como o impacto seria diferente de fazê-lo da maneira "antiga", você pode fazer algo que não podia antes ou é mais rápido? Escreva um resumo de 300 palavras sobre como seria sua startup de IA dos sonhos e inclua cabeçalhos como "Problema", "Como eu usaria IA", "Impacto" e opcionalmente um plano de negócios.

Se você fez esta tarefa, pode até estar pronto para se candidatar ao incubador da Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) oferecemos créditos tanto para Azure quanto para OpenAI, mentoria e muito mais, confira!

## Verificação de conhecimento

O que é verdade sobre modelos de linguagem de grande porte?

1. Você recebe a mesma resposta exata todas as vezes.
1. Faz as coisas perfeitamente, ótimo em somar números, produzir código funcional, etc.
1. A resposta pode variar, apesar de usar o mesmo prompt. Também é ótimo para dar a você um primeiro rascunho de algo, seja texto ou código. Mas você precisa melhorar os resultados.

A: 3, um LLM é não determinístico, a resposta varia, no entanto, você pode controlar sua variação por meio de uma configuração de temperatura. Você também não deve esperar que ele faça as coisas perfeitamente, está aqui para fazer o trabalho pesado para você, o que muitas vezes significa que você obtém uma boa primeira tentativa de algo que precisa melhorar gradualmente.

## Ótimo trabalho! Continue a jornada

Após completar esta lição, confira nossa [coleção de aprendizado de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento sobre IA generativa!

Vá para a Lição 2, onde vamos explorar e comparar diferentes tipos de LLMs](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se uma tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.