# Fundamentos de Engenharia de Prompt

[![Fundamentos de Engenharia de Prompt](../../../translated_images/pt-BR/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introdução
Este módulo aborda conceitos e técnicas essenciais para criar prompts eficazes em modelos de IA generativa. A forma como você escreve seu prompt para um LLM também importa. Um prompt cuidadosamente elaborado pode alcançar uma melhor qualidade de resposta. Mas o que exatamente significam termos como _prompt_ e _engenharia de prompt_? E como melhorar o _input_ do prompt que envio ao LLM? Essas são as perguntas que tentaremos responder neste capítulo e no próximo.

_IA Generativa_ é capaz de criar novos conteúdos (ex.: texto, imagens, áudio, código etc.) em resposta a solicitações dos usuários. Isso é feito usando _Modelos de Linguagem de Grande Porte_ como a série GPT da OpenAI ("Generative Pre-trained Transformer"), treinados para usar linguagem natural e código.

Agora os usuários podem interagir com esses modelos usando paradigmas familiares como chat, sem precisar de qualquer especialização técnica ou treinamento. Os modelos são _baseados em prompt_ – os usuários enviam um texto (prompt) e recebem a resposta da IA (completação). Eles podem "conversar com a IA" iterativamente, em diálogos de múltiplas interações, refinando o prompt até que a resposta atenda às suas expectativas.

"Prompts" tornam-se a principal _interface de programação_ para aplicativos de IA generativa, dizendo aos modelos o que fazer e influenciando a qualidade das respostas retornadas. "Engenharia de Prompt" é um campo de estudo em rápido crescimento que foca no _design e otimização_ dos prompts para fornecer respostas consistentes e de qualidade em escala.

## Objetivos de Aprendizagem

Nesta lição, aprenderemos o que é Engenharia de Prompt, por que ela importa e como criar prompts mais eficazes para um modelo e objetivo de aplicação específicos. Entenderemos conceitos fundamentais e melhores práticas para engenharia de prompt – além de conhecer um ambiente interativo de Jupyter Notebooks, um "sandbox" onde poderemos ver esses conceitos aplicados a exemplos reais.

Ao final desta lição, seremos capazes de:

1. Explicar o que é engenharia de prompt e por que ela é importante.
2. Descrever os componentes de um prompt e como são usados.
3. Aprender melhores práticas e técnicas para engenharia de prompt.
4. Aplicar as técnicas aprendidas a exemplos reais, usando um endpoint OpenAI.

## Termos Chave

Engenharia de Prompt: A prática de projetar e refinar entradas para guiar modelos de IA a produzir saídas desejadas.
Tokenização: O processo de converter texto em unidades menores, chamadas tokens, que um modelo pode entender e processar.
LLMs Ajustados por Instrução: Modelos de Linguagem de Grande Porte que foram ajustados com instruções específicas para melhorar a precisão e relevância das respostas.

## Sandbox de Aprendizado

A engenharia de prompt é atualmente mais arte do que ciência. A melhor maneira de melhorar nossa intuição é _praticar mais_ e adotar uma abordagem de tentativa e erro que combine expertise no domínio da aplicação com técnicas recomendadas e otimizações específicas do modelo.

O Jupyter Notebook que acompanha esta lição oferece um ambiente _sandbox_ onde você pode testar o que aprendeu – conforme for aprendendo ou como parte do desafio de código no final. Para executar os exercícios, você precisará de:

1. **Uma chave de API Azure OpenAI** – o endpoint do serviço para um LLM implantado.
2. **Um ambiente Python Runtime** – para executar o Notebook.
3. **Variáveis de ambiente locais** – _complete os passos [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) agora para se preparar_.

O notebook vem com exercícios _iniciais_ – mas você é incentivado a adicionar suas próprias seções de _Markdown_ (descrição) e _Código_ (solicitações de prompt) para experimentar mais exemplos ou ideias – e construir sua intuição para o design de prompts.

## Guia Ilustrado

Quer ter uma visão geral do que esta lição cobre antes de se aprofundar? Veja este guia ilustrado, que dá uma noção dos principais tópicos abordados e os pontos-chave para você refletir em cada um. O roteiro da lição leva você de entender conceitos e desafios fundamentais até abordá-los com técnicas relevantes de engenharia de prompt e melhores práticas. Note que a seção "Técnicas Avançadas" neste guia refere-se ao conteúdo coberto no _próximo_ capítulo deste currículo.

![Guia Ilustrado para Engenharia de Prompt](../../../translated_images/pt-BR/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Nossa Startup

Agora, vamos falar sobre como _este tema_ se relaciona com nossa missão de startup para [trazer inovação em IA para a educação](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicações de IA para _aprendizagem personalizada_ – então vamos pensar em como diferentes usuários do nosso aplicativo podem "projetar" prompts:

- **Administradores** podem pedir à IA para _analisar dados do currículo para identificar lacunas no conteúdo_. A IA pode resumir os resultados ou visualizá-los com código.
- **Educadores** podem pedir à IA para _gerar um plano de aula para um público-alvo e tema específicos_. A IA pode construir um plano personalizado em um formato especificado.
- **Estudantes** podem pedir à IA para _tutorar em uma matéria difícil_. A IA pode orientar os estudantes com aulas, dicas e exemplos adaptados ao nível deles.

Isso é só a ponta do iceberg. Veja [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – uma biblioteca open source de prompts curada por especialistas em educação – para ter uma visão mais ampla das possibilidades! _Tente rodar alguns desses prompts no sandbox ou no OpenAI Playground para ver o que acontece!_

<!--
MODELO DE LIÇÃO:
Esta unidade deve cobrir o conceito fundamental #1.
Reforce o conceito com exemplos e referências.

CONCEITO #1:
Engenharia de Prompt.
Defina e explique por que é necessária.
-->

## O que é Engenharia de Prompt?

Começamos esta lição definindo **Engenharia de Prompt** como o processo de _projetar e otimizar_ entradas de texto (prompts) para fornecer respostas consistentes e de qualidade (completions) para um dado objetivo de aplicação e modelo. Podemos pensar nisso como um processo em 2 etapas:

- _projetar_ o prompt inicial para um determinado modelo e objetivo
- _refinar_ o prompt iterativamente para melhorar a qualidade da resposta

Este é necessariamente um processo de tentativa e erro que requer intuição do usuário e esforço para obter resultados ótimos. Então por que é importante? Para responder a essa pergunta, primeiro precisamos entender três conceitos:

- _Tokenização_ = como o modelo "vê" o prompt
- _LLMs Base_ = como o modelo fundamental "processa" um prompt
- _LLMs Ajustados por Instrução_ = como o modelo agora pode ver "tarefas"

### Tokenização

Um LLM vê prompts como uma _sequência de tokens_, onde diferentes modelos (ou versões de um modelo) podem tokenizar o mesmo prompt de formas diferentes. Como LLMs são treinados com tokens (e não com texto bruto), a forma como os prompts são tokenizados impacta diretamente a qualidade da resposta gerada.

Para ter uma intuição de como a tokenização funciona, experimente ferramentas como o [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abaixo. Cole seu prompt – e veja como ele é convertido em tokens, prestando atenção em como espaços em branco e pontuações são tratados. Note que este exemplo mostra um LLM mais antigo (GPT-3) – então testar com um modelo mais novo pode produzir resultado diferente.

![Tokenização](../../../translated_images/pt-BR/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Conceito: Modelos Fundamentais

Depois que o prompt é tokenizado, a função principal do ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modelo fundamental) é prever o próximo token na sequência. Como os LLMs são treinados em grandes conjuntos de texto, eles têm uma boa noção das relações estatísticas entre tokens e conseguem fazer essa previsão com alguma confiança. Note que eles não entendem o _significado_ das palavras no prompt ou token; apenas enxergam um padrão que podem "completar" com sua próxima previsão. Podem continuar prevendo a sequência até serem interrompidos pelo usuário ou alguma condição pré-estabelecida.

Quer ver como funciona a completude baseada em prompt? Insira o prompt acima no [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) com as configurações padrão. O sistema está configurado para tratar prompts como pedidos de informação – então você deve ver uma resposta que satisfaça esse contexto.

Mas e se o usuário quiser ver algo específico que cumpra alguns critérios ou objetivo de tarefa? É aqui que os LLMs _ajustados por instrução_ entram em cena.

![Completude Baseada em Chat de LLM Base](../../../translated_images/pt-BR/04-playground-chat-base.65b76fcfde0caa67.webp)

### Conceito: LLMs Ajustados por Instrução

Um [LLM Ajustado por Instrução](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) parte do modelo fundamental e o refina com exemplos ou pares de entrada/saída (ex.: "mensagens" de múltiplas interações) que contêm instruções claras – e a resposta da IA tenta seguir essas instruções.

Isso usa técnicas como Aprendizado por Reforço com Feedback Humano (RLHF) que treinam o modelo para _seguir instruções_ e _aprender com o feedback_ de modo a gerar respostas mais adequadas a aplicações práticas e mais relevantes aos objetivos do usuário.

Vamos experimentar – reveja o prompt acima, mas agora altere a _mensagem do sistema_ para fornecer a seguinte instrução como contexto:

> _Resuma o conteúdo fornecido para um aluno da segunda série. Mantenha o resultado em um parágrafo com 3-5 tópicos em forma de lista._

Veja como o resultado agora está ajustado para refletir o objetivo e formato desejados? Um educador pode usar essa resposta diretamente em seus slides para a aula.

![Completude de Chat de LLM Ajustado por Instrução](../../../translated_images/pt-BR/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Por que precisamos de Engenharia de Prompt?

Agora que sabemos como os prompts são processados pelos LLMs, vamos falar sobre _por que_ precisamos de engenharia de prompt. A resposta está no fato de que os LLMs atuais apresentam diversos desafios que dificultam alcançar _completudes confiáveis e consistentes_ sem dedicar esforço à construção e otimização do prompt. Por exemplo:

1. **As respostas do modelo são estocásticas.** O _mesmo prompt_ provavelmente produzirá respostas diferentes com modelos ou versões diferentes. E pode até produzir resultados distintos com o _mesmo modelo_ em momentos diferentes. _Técnicas de engenharia de prompt podem ajudar a minimizar essas variações ao fornecer melhores guias_.

1. **Modelos podem fabricar respostas.** Modelos são pré-treinados com conjuntos de dados _grandes porém finitos_, ou seja, não possuem conhecimento sobre conceitos fora desse escopo. Como resultado, podem gerar respostas imprecisas, imaginárias ou diretamente contraditórias a fatos conhecidos. _Técnicas de engenharia de prompt ajudam os usuários a identificar e mitigar essas fabricações, por exemplo, pedindo citações ou raciocínios da IA_.

1. **As capacidades dos modelos variam.** Modelos mais novos ou gerações distintas trarão capacidades mais ricas, mas também características e trade-offs únicos em custo e complexidade. _A engenharia de prompt pode nos ajudar a desenvolver melhores práticas e fluxos de trabalho que abstraem essas diferenças e se adaptam a requisitos específicos do modelo de forma escalável e transparente_.

Vamos ver isso em ação no OpenAI ou Azure OpenAI Playground:

- Use o mesmo prompt com diferentes implantações de LLM (ex.: OpenAI, Azure OpenAI, Hugging Face) – você percebeu as variações?
- Use o mesmo prompt repetidamente na _mesma_ implantação de LLM (ex.: playground Azure OpenAI) – como essas variações foram diferentes?

### Exemplo de Fabricações

Neste curso, usamos o termo **"fabricação"** para referir o fenômeno em que LLMs às vezes geram informações factualmente incorretas devido a limitações no treinamento ou outras restrições. Você pode ter ouvido isso referido como _"alucinações"_ em artigos populares ou trabalhos acadêmicos. No entanto, recomendamos fortemente usar _"fabricação"_ para não antropomorfizar o comportamento atribuindo uma característica humana a um resultado gerado por máquina. Isso também reforça as [diretrizes de IA Responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) do ponto de vista terminológico, eliminando termos que podem ser ofensivos ou não inclusivos em determinados contextos.

Quer entender como funcionam as fabricações? Pense em um prompt que instrui a IA a gerar conteúdo sobre um tema inexistente (garantindo que não esteja no conjunto de treinamento). Por exemplo – experimentei este prompt:

> **Prompt:** gere um plano de aula sobre a Guerra Marciana de 2076.

Uma busca na web me mostrou que há relatos fictícios (ex.: séries de TV ou livros) sobre guerras marcianas – mas nenhuma datada de 2076. O senso comum também indica que 2076 é _no futuro_ e, portanto, não pode ser associado a um evento real.


O que acontece quando executamos este prompt com diferentes provedores de LLM?

> **Resposta 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/pt-BR/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Resposta 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/pt-BR/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Resposta 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/pt-BR/04-fabrication-huggingchat.faf82a0a51278956.webp)

Como esperado, cada modelo (ou versão de modelo) produz respostas ligeiramente diferentes graças ao comportamento estocástico e variações nas capacidades do modelo. Por exemplo, um modelo direciona seu resultado para um público de 8ª série enquanto o outro assume um estudante do ensino médio. Mas os três modelos geraram respostas que poderiam convencer um usuário desinformado de que o evento era real.

Técnicas de engenharia de prompt como _metaprompting_ e _configuração de temperatura_ podem reduzir fabricacões do modelo até certo ponto. Novas _arquiteturas_ de engenharia de prompt também incorporam ferramentas e técnicas novas diretamente no fluxo do prompt, para mitigar ou reduzir alguns desses efeitos.

## Estudo de Caso: GitHub Copilot

Vamos encerrar esta seção entendendo como a engenharia de prompt é usada em soluções do mundo real, analisando um Estudo de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot é seu "Programador Par AI" - ele converte prompts de texto em códigos completos e está integrado ao seu ambiente de desenvolvimento (ex: Visual Studio Code) para proporcionar uma experiência de usuário sem interrupções. Conforme documentado na série de blogs abaixo, a versão inicial foi baseada no modelo OpenAI Codex - com os engenheiros rapidamente percebendo a necessidade de ajustar o modelo e desenvolver melhores técnicas de engenharia de prompt para melhorar a qualidade do código. Em julho, eles [lançaram um modelo AI melhorado que vai além do Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugestões ainda mais rápidas.

Leia os posts na ordem para acompanhar a jornada de aprendizado deles.

- **Maio 2023** | [GitHub Copilot está melhorando o entendimento do seu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maio 2023** | [Dentro do GitHub: Trabalhando com os LLMs por trás do GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junho 2023** | [Como escrever melhores prompts para o GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julho 2023** | [.. GitHub Copilot vai além do Codex com modelo AI melhorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julho 2023** | [Guia do desenvolvedor para engenharia de prompt e LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Set 2023** | [Como construir um app LLM empresarial: Lições do GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Você também pode explorar o [blog de Engenharia deles](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para mais posts como [este](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que mostra como esses modelos e técnicas são _aplicados_ para impulsionar aplicações do mundo real.

---

<!--
MODELO DE LIÇÃO:
Esta unidade deve cobrir o conceito fundamental #2.
Reforce o conceito com exemplos e referências.

CONCEITO #2:
Design de Prompt.
Ilustrado com exemplos.
-->

## Construção de Prompt

Vimos por que a engenharia de prompt é importante - agora vamos entender como os prompts são _construídos_ para que possamos avaliar diferentes técnicas para um design de prompt mais eficaz.

### Prompt Básico

Vamos começar com o prompt básico: um texto enviado ao modelo sem outro contexto. Aqui está um exemplo - quando enviamos as primeiras palavras do hino nacional dos EUA para o OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) ele instantaneamente _completa_ a resposta com as próximas linhas, ilustrando o comportamento básico de predição.

| Prompt (Entrada)    | Compleção (Saída)                                                                                                                         |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Parece que você está começando a letra de "The Star-Spangled Banner", o hino nacional dos Estados Unidos. A letra completa é ...           |

### Prompt Complexo

Agora vamos adicionar contexto e instruções a esse prompt básico. O [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nos permite construir um prompt complexo como uma coleção de _mensagens_ com:

- Pares de entrada/saída refletindo a entrada do _usuário_ e resposta do _assistente_.
- Mensagem do sistema definindo o contexto para comportamento ou personalidade do assistente.

A requisição agora tem o formato abaixo, onde a _tokenização_ captura efetivamente informações relevantes do contexto e da conversa. Agora, mudar o contexto do sistema pode impactar a qualidade das completions tanto quanto as entradas do usuário fornecidas.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt de Instrução

Nos exemplos acima, o prompt do usuário foi uma simples consulta de texto que pode ser interpretada como um pedido de informação. Com prompts de _instrução_, podemos usar esse texto para especificar uma tarefa com mais detalhe, proporcionando uma melhor orientação para a IA. Aqui está um exemplo:

| Prompt (Entrada)                                                                                                                                                                                                                          | Compleção (Saída)                                                                                                | Tipo de Instrução  |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :----------------- |
| Escreva uma descrição da Guerra Civil                                                                                                                                                                                                   | _retornou um parágrafo simples_                                                                                 | Simples            |
| Escreva uma descrição da Guerra Civil. Forneça datas e eventos chave e descreva sua importância                                                                                                                                          | _retornou um parágrafo seguido por uma lista de datas dos eventos chave com descrições_                          | Complexa           |
| Escreva uma descrição da Guerra Civil em 1 parágrafo. Forneça 3 tópicos com datas importantes e sua importância. Forneça mais 3 tópicos com figuras históricas importantes e suas contribuições. Retorne a saída como um arquivo JSON | _retorna detalhes mais extensos em uma caixa de texto, formatados como JSON que você pode copiar e colar em um arquivo e validar conforme necessário_ | Complexa. Formatada. |

## Conteúdo Principal

Nos exemplos acima, o prompt ainda era bastante aberto, permitindo que o LLM decidisse qual parte do seu conjunto de dados pré-treinado era relevante. Com o padrão de design _conteúdo principal_, o texto de entrada é dividido em duas partes:

- uma instrução (ação)
- conteúdo relevante (que influencia a ação)

Aqui está um exemplo onde a instrução é "resuma isto em 2 sentenças".

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Compleção (Saída)                                                                                                                                                                                                                                                                            |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa de um milésimo da massa do Sol, mas duas vezes e meia a massa de todos os outros planetas do Sistema Solar combinados. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e tem sido conhecido por civilizações antigas desde antes da história registrada. É nomeado em homenagem ao deus romano Júpiter.[19] Quando visto da Terra, Júpiter pode ser brilhante o suficiente para sua luz refletida lançar sombras visíveis,[20] e é em média o terceiro objeto natural mais brilhante no céu noturno depois da Lua e Vênus. <br/> **Resuma isto em 2 frases curtas** | Júpiter, o quinto planeta a partir do Sol, é o maior do Sistema Solar e é conhecido por ser um dos objetos mais brilhantes do céu noturno. Nomeado em homenagem ao deus romano Júpiter, é um gigante gasoso cuja massa é duas vezes e meia a massa de todos os outros planetas do Sistema Solar combinados. |

O segmento de conteúdo principal pode ser usado de várias formas para guiar instruções mais eficazes:

- **Exemplos** - em vez de dizer ao modelo o que fazer com uma instrução explícita, dê exemplos do que fazer e deixe-o inferir o padrão.
- **Indícios** - siga a instrução com uma "dica" que estimule a completude, guiando o modelo para respostas mais relevantes.
- **Modelos** - são 'receitas' repetíveis para prompts com espaços reservados (variáveis) que podem ser customizados com dados para casos de uso específicos.

Vamos explorar estes em ação.

### Usando Exemplos

Essa é uma abordagem onde você usa o conteúdo principal para "alimentar o modelo" com alguns exemplos do resultado desejado para uma dada instrução, e deixa-o inferir o padrão do resultado pedido. Com base no número de exemplos fornecidos, podemos ter zero-shot prompting, one-shot prompting, few-shot prompting etc.

O prompt agora consiste em três componentes:

- Uma descrição da tarefa
- Alguns exemplos do resultado desejado
- O início de um novo exemplo (que se torna uma descrição implícita da tarefa)

| Tipo de Aprendizado | Prompt (Entrada)                                                                                           | Compleção (Saída)         |
| :------------------ | :------------------------------------------------------------------------------------------------------- | :------------------------- |
| Zero-shot           | "The Sun is Shining". Traduza para o espanhol                                                          | "El Sol está brillando".   |
| One-shot            | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                     | "Es un día frío y ventoso". |
| Few-shot            | O jogador correu pelas bases => Baseball <br/> O jogador fez um ace => Tênis <br/> O jogador fez um seis => Cricket <br/> O jogador fez uma enterrada => | Basquete                  |
|                    |                                                                                                         |                            |

Note como tivemos que fornecer uma instrução explícita ("Traduza para o espanhol") no zero-shot prompting, mas ela é inferida no exemplo de one-shot prompting. O exemplo few-shot mostra como adicionar mais exemplos permite que os modelos façam inferências mais precisas sem instruções adicionais.

### Indícios no Prompt

Outra técnica para usar o conteúdo principal é fornecer _indícios_ ao invés de exemplos. Neste caso, damos ao modelo um empurrão na direção correta ao _começar_ com um trecho que reflete o formato de resposta desejado. O modelo então "pega a dica" para continuar nessa linha.

| Número de Indícios | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                    | Compleção (Saída)                                                                                                                                                                                                                                                                                         |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                  | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa de um milésimo da massa do Sol, mas duas vezes e meia a massa de todos os outros planetas do Sistema Solar combinados. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e tem sido conhecido por civilizações antigas desde antes da história registrada. <br/>**Resuma Isto**                                  | Júpiter é o maior planeta do nosso Sistema Solar e o quinto a partir do Sol. É um gigante gasoso com uma massa de 1/1000 da do Sol, mas é mais pesado que todos os outros planetas juntos. Civilizações antigas já conhecem Júpiter há muito tempo, e ele é facilmente visível no céu noturno.. |
| 1                  | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa de um milésimo da massa do Sol, mas duas vezes e meia a massa de todos os outros planetas do Sistema Solar combinados. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e tem sido conhecido por civilizações antigas desde antes da história registrada. <br/>**Resuma Isto** <br/> O que aprendemos é que Júpiter | é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa de um milésimo da massa do Sol, mas duas vezes e meia a massa de todos os outros planetas juntos. É facilmente visível a olho nu e é conhecido desde os tempos antigos.                       |

| 2              | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa mil vezes menor que a do Sol, mas duas vezes e meia a soma da massa de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e é conhecido pelas civilizações antigas desde antes da história registrada. <br/>**Resuma Isto** <br/> Top 3 Fatos Que Aprendemos:         | 1. Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. <br/> 2. É um gigante gasoso com uma massa mil vezes menor que a do Sol...<br/> 3. Júpiter tem sido visível a olho nu desde os tempos antigos ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Modelos de Prompt

Um modelo de prompt é uma _receita pré-definida para um prompt_ que pode ser armazenada e reutilizada conforme necessário, para impulsionar experiências de usuário mais consistentes em escala. Em sua forma mais simples, é simplesmente uma coleção de exemplos de prompt como [este da OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) que fornece tanto os componentes interativos do prompt (mensagens de usuário e sistema) quanto o formato de solicitação via API - para suportar a reutilização.

Em sua forma mais complexa, como [este exemplo do LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), ele contém _espaços reservados_ que podem ser substituídos por dados de várias fontes (entrada do usuário, contexto do sistema, fontes de dados externas etc.) para gerar um prompt dinamicamente. Isso nos permite criar uma biblioteca de prompts reutilizáveis que podem ser usados para gerar experiências de usuário consistentes **programaticamente** em escala.

Finalmente, o verdadeiro valor dos modelos está na capacidade de criar e publicar _bibliotecas de prompts_ para domínios verticais específicos - onde o modelo de prompt é agora _otimizado_ para refletir o contexto ou exemplos específicos da aplicação que tornam as respostas mais relevantes e precisas para o público-alvo. O repositório [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) é um ótimo exemplo dessa abordagem, compilando uma biblioteca de prompts para o domínio da educação com ênfase em objetivos chave como planejamento de aulas, design curricular, tutoria de alunos etc.

## Conteúdo de Apoio

Se considerarmos a construção do prompt como tendo uma instrução (tarefa) e um alvo (conteúdo primário), então o _conteúdo secundário_ é como um contexto adicional que fornecemos para **influenciar a saída de alguma forma**. Pode ser parâmetros de ajuste, instruções de formatação, taxonomias de tópicos etc. que ajudam o modelo a _ajustar_ sua resposta para adequar-se aos objetivos ou expectativas desejadas do usuário.

Por exemplo: Dado um catálogo de cursos com metadados extensos (nome, descrição, nível, tags de metadados, instrutor etc.) de todos os cursos disponíveis no currículo:

- podemos definir uma instrução para "resumir o catálogo de cursos para o outono de 2023"
- podemos usar o conteúdo primário para fornecer alguns exemplos do resultado desejado
- podemos usar o conteúdo secundário para identificar as 5 principais "tags" de interesse.

Agora, o modelo pode fornecer um resumo no formato mostrado pelos poucos exemplos - mas se um resultado tiver múltiplas tags, ele pode priorizar as 5 tags identificadas no conteúdo secundário.

---

<!--
MODELO DE AULA:
Esta unidade deve cobrir o conceito central #1.
Reforce o conceito com exemplos e referências.

CONCEITO #3:
Técnicas de Engenharia de Prompt.
Quais são algumas técnicas básicas para engenharia de prompt?
Ilustre com alguns exercícios.
-->

## Melhores Práticas para Prompting

Agora que sabemos como os prompts podem ser _construídos_, podemos começar a pensar em como _projetá-los_ para refletir as melhores práticas. Podemos pensar nisso em duas partes - ter a _mentalidade_ certa e aplicar as _técnicas_ corretas.

### Mentalidade de Engenharia de Prompt

Engenharia de Prompt é um processo de tentativa e erro, então mantenha três fatores amplos de orientação em mente:

1. **Compreensão do Domínio é Importante.** A precisão e relevância da resposta são uma função do _domínio_ no qual essa aplicação ou usuário opera. Aplique sua intuição e expertise de domínio para **customizar técnicas** ainda mais. Por exemplo, defina _personalidades específicas do domínio_ em seus prompts de sistema, ou use _modelos específicos do domínio_ em seus prompts de usuário. Forneça conteúdo secundário que reflita contextos específicos do domínio, ou use _pistas e exemplos específicos do domínio_ para guiar o modelo para padrões de uso familiares.

2. **Compreensão do Modelo é Importante.** Sabemos que os modelos são estocásticos por natureza. Mas as implementações de modelos também podem variar em termos do conjunto de dados de treinamento que usam (conhecimento pré-treinado), as capacidades que fornecem (e.g., via API ou SDK) e o tipo de conteúdo para o qual são otimizados (e.g., código vs. imagens vs. texto). Compreenda os pontos fortes e limitações do modelo que você está usando, e use esse conhecimento para _priorizar tarefas_ ou construir _modelos customizados_ que sejam otimizados para as capacidades do modelo.

3. **Iteração & Validação são Importantes.** Os modelos estão evoluindo rapidamente, e as técnicas para engenharia de prompt também. Como especialista em domínio, você pode ter outro contexto ou critérios para _sua_ aplicação específica, que podem não se aplicar para a comunidade mais ampla. Use ferramentas e técnicas de engenharia de prompt para “dar o pontapé inicial” na construção de prompts, depois itere e valide os resultados usando sua própria intuição e expertise de domínio. Registre seus insights e crie uma **base de conhecimento** (e.g, bibliotecas de prompt) que possam ser usadas como nova referência por outros, para iterações mais rápidas no futuro.

## Melhores Práticas

Agora vamos olhar para as melhores práticas comuns recomendadas pelos praticantes da [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e da [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| O que                              | Por que                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Avalie os modelos mais recentes.  | As novas gerações de modelos provavelmente terão recursos e qualidade aprimorados - mas também podem incorrer em custos mais altos. Avalie-os pelo impacto e então tome decisões de migração.                                                         |
| Separe instruções e contexto      | Verifique se seu modelo/provedor define _delimitadores_ para distinguir claramente instruções, conteúdo primário e secundário. Isso pode ajudar os modelos a atribuirem pesos com mais precisão aos tokens.                                         |
| Seja específico e claro           | Forneça mais detalhes sobre o contexto desejado, resultado, comprimento, formato, estilo etc. Isso melhorará tanto a qualidade quanto a consistência das respostas. Capture receitas em modelos reutilizáveis.                                      |
| Seja descritivo, use exemplos     | Os modelos podem responder melhor a uma abordagem de "mostrar e contar". Comece com uma abordagem `zero-shot` onde você dá uma instrução (mas sem exemplos) e depois tente `few-shot` como refinamento, fornecendo alguns exemplos do resultado desejado. Use analogias. |
| Use pistas para iniciar as respostas | Incentive-o a um resultado desejado dando algumas palavras ou frases iniciais que ele possa usar como ponto de partida para a resposta.                                                                                                             |
| Reforce                          | Às vezes você pode precisar se repetir para o modelo. Dê instruções antes e depois do conteúdo primário, use uma instrução e uma pista, etc. Itere e valide para ver o que funciona.                                                              |
| A ordem importa                   | A ordem em que você apresenta a informação ao modelo pode impactar a saída, mesmo nos exemplos de aprendizado, devido ao viés de recência. Experimente diferentes opções para ver o que funciona melhor.                                              |
| Dê uma “saída” ao modelo          | Dê ao modelo uma resposta de _fallback_ que ele possa fornecer se não conseguir completar a tarefa por alguma razão. Isso pode reduzir as chances de o modelo gerar respostas falsas ou fabricadas.                                                |
|                                   |                                                                                                                                                                                                                                                   |

Como em qualquer melhor prática, lembre-se que _seu resultado pode variar_ dependendo do modelo, da tarefa e do domínio. Use estas como ponto de partida e itere para descobrir o que funciona melhor para você. Reavalie constantemente seu processo de engenharia de prompt conforme novos modelos e ferramentas se tornam disponíveis, com foco na escalabilidade do processo e qualidade da resposta.

<!--
MODELO DE AULA:
Esta unidade deve fornecer um desafio de código, se aplicável

DESAFIO:
Link para um Jupyter Notebook com apenas os comentários de código nas instruções (as seções de código estão vazias).

SOLUÇÃO:
Link para uma cópia desse Notebook com os prompts preenchidos e executados, mostrando como pode ser um exemplo.
-->

## Tarefa

Parabéns! Você chegou ao final da aula! É hora de colocar alguns desses conceitos e técnicas à prova com exemplos reais!

Para nossa tarefa, usaremos um Jupyter Notebook com exercícios que você pode completar interativamente. Você também pode estender o Notebook com suas próprias células Markdown e de Código para explorar ideias e técnicas por conta própria.

### Para começar, faça um fork do repositório, depois

- (Recomendado) Inicie o GitHub Codespaces
- (Alternativamente) Clone o repositório para seu dispositivo local e use com Docker Desktop
- (Alternativamente) Abra o Notebook com seu ambiente preferido de runtime para Notebooks.

### Em seguida, configure suas variáveis de ambiente

- Copie o arquivo `.env.copy` na raiz do repositório para `.env` e preencha os valores de `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT`. Volte para a [seção Learning Sandbox](#sandbox-de-aprendizado) para aprender como.

### Em seguida, abra o Jupyter Notebook

- Selecione o kernel de runtime. Se usar a opção 1 ou 2, basta selecionar o kernel Python 3.10.x padrão fornecido pelo container dev.

Você está pronto para executar os exercícios. Note que não existem respostas _certas e erradas_ aqui - apenas explorar opções por tentativa e erro e construir intuição do que funciona para um dado modelo e domínio de aplicação.

_Por essa razão, não há segmentos de Código de Solução nesta aula. Em vez disso, o Notebook terá células Markdown intituladas "Minha Solução:" que mostram um exemplo de saída para referência._

 <!--
MODELO DE AULA:
Encerre a seção com um resumo e recursos para aprendizado autodirigido.
-->

## Verificação de conhecimento

Qual dos seguintes é um bom prompt seguindo algumas melhores práticas razoáveis?

1. Mostre-me uma imagem de um carro vermelho
2. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90 estacionado perto de um penhasco com o sol se pondo
3. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90

R: 2, é o melhor prompt pois fornece detalhes sobre "o quê" e entra em especificidades (não qualquer carro, mas uma marca e modelo específicos) e também descreve o cenário geral. 3 fica em segundo lugar pois também contém muita descrição.

## 🚀 Desafio

Veja se você consegue aproveitar a técnica de "pista" com o prompt: Complete a frase "Mostre-me uma imagem de um carro vermelho da marca Volvo e ". Com o que ele responde, e como você melhoraria?

## Ótimo Trabalho! Continue Sua Aprendizagem

Quer aprender mais sobre diferentes conceitos de Engenharia de Prompt? Vá para a [página de aprendizado continuado](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre este tema.

Vá para a Aula 5 onde vamos ver [técnicas avançadas de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->