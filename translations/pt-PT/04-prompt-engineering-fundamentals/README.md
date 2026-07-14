# Fundamentos de Engenharia de Prompts

[![Fundamentos de Engenharia de Prompts](../../../translated_images/pt-PT/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introdução
Este módulo abrange conceitos e técnicas essenciais para criar prompts eficazes em modelos de IA generativa. A forma como escreve o seu prompt para um LLM também importa. Um prompt cuidadosamente elaborado pode alcançar uma resposta de melhor qualidade. Mas o que significam exatamente termos como _prompt_ e _engenharia de prompt_? E como posso melhorar o _input_ do prompt que envio ao LLM? Estas são as perguntas que vamos tentar responder neste capítulo e no próximo.

_IA Generativa_ é capaz de criar novos conteúdos (por exemplo, texto, imagens, áudio, código etc.) em resposta a pedidos dos utilizadores. Ela consegue isso usando _Grandes Modelos de Linguagem_ como a série GPT da OpenAI ("Transformador Generativo Pré-treinado") que são treinados para usar linguagem natural e código.

Os utilizadores podem agora interagir com estes modelos usando paradigmas familiares como chat, sem necessidade de qualquer especialização técnica ou formação. Os modelos são _baseados em prompts_ - os utilizadores enviam um texto de entrada (prompt) e recebem a resposta da IA (completamento). Depois podem “conversar com a IA” iterativamente, em conversas com múltiplos turnos, refinando o seu prompt até que a resposta corresponda às suas expectativas.

Os “prompts” tornam-se agora a principal _interface de programação_ para aplicações de IA generativa, dizendo aos modelos o que fazer e influenciando a qualidade das respostas devolvidas. A “Engenharia de Prompts” é um campo de estudo em rápido crescimento que se foca no _design e otimização_ dos prompts para fornecer respostas consistentes e de qualidade em escala.

## Objetivos de Aprendizagem

Nesta lição, aprendemos o que é Engenharia de Prompts, por que é importante e como podemos criar prompts mais eficazes para um dado modelo e objetivo de aplicação. Compreenderemos conceitos básicos e boas práticas para engenharia de prompts - e aprenderemos sobre um ambiente interativo de Jupyter Notebooks “sandbox” onde podemos ver estes conceitos aplicados a exemplos reais.

No final desta lição seremos capazes de:

1. Explicar o que é engenharia de prompts e por que é importante.
2. Descrever os componentes de um prompt e como são usados.
3. Aprender boas práticas e técnicas para engenharia de prompts.
4. Aplicar as técnicas aprendidas a exemplos reais, usando um endpoint OpenAI.

## Termos-chave

Engenharia de Prompts: A prática de projetar e refinar entradas para orientar modelos de IA na produção de saídas desejadas.
Tokenização: O processo de converter texto em unidades menores, chamadas tokens, que um modelo pode entender e processar.
LLMs Ajustados por Instruções: Grandes Modelos de Linguagem (LLMs) que foram ajustados com instruções específicas para melhorar a precisão e relevância das respostas.

## Ambiente de Aprendizagem

A engenharia de prompts é atualmente mais arte do que ciência. A melhor forma de melhorar a nossa intuição para ela é _praticar mais_ e adotar uma abordagem de tentativa e erro que combine o conhecimento do domínio da aplicação com técnicas recomendadas e otimizações específicas para modelos.

O Jupyter Notebook que acompanha esta lição fornece um ambiente _sandbox_ onde pode experimentar o que aprende - à medida que avança ou como parte do desafio de código no final. Para executar os exercícios, vai precisar de:

1. **Uma chave de API Azure OpenAI** - o endpoint do serviço para um LLM implementado.
2. **Um ambiente de execução Python** - onde o Notebook possa ser executado.
3. **Variáveis de Ambiente Locais** - _complete as etapas do [CONFIGURAÇÃO](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) agora para ficar preparado_.

O notebook vem com exercícios _inicializadores_ - mas é encorajado a adicionar as suas próprias secções de _Markdown_ (descrição) e _Código_ (pedidos de prompt) para experimentar mais exemplos ou ideias - e desenvolver a sua intuição para o design de prompts.

## Guia Ilustrado

Quer ter uma visão geral do que esta lição cobre antes de se aprofundar? Veja este guia ilustrado, que lhe dá uma ideia dos principais tópicos abordados e das principais conclusões para refletir em cada um. O roteiro da lição leva-o desde a compreensão dos conceitos e desafios principais até a sua resolução com técnicas relevantes de engenharia de prompts e boas práticas. Note que a secção “Técnicas Avançadas” deste guia refere-se a conteúdo abordado no _próximo_ capítulo deste currículo.

![Guia Ilustrado para Engenharia de Prompts](../../../translated_images/pt-PT/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## A Nossa Startup

Agora, vamos falar sobre como _este tema_ se relaciona com a missão da nossa startup de [trazer inovação em IA para a educação](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicações de IA para _aprendizagem personalizada_ - por isso vamos pensar em como diferentes utilizadores da nossa aplicação poderão “desenhar” prompts:

- **Administradores** podem pedir à IA para _analisar dados curriculares para identificar lacunas na cobertura_. A IA pode resumir os resultados ou visualizá-los com código.
- **Educadores** podem pedir à IA para _gerar um plano de aula para um público-alvo e tema_. A IA pode construir o plano personalizado num formato especificado.
- **Estudantes** podem pedir à IA para _os ajudar numa disciplina difícil_. A IA pode agora guiar os estudantes com aulas, dicas e exemplos adaptados ao seu nível.

Isto é só a ponta do iceberg. Veja [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - uma biblioteca open-source de prompts curada por especialistas em educação - para ter uma noção mais ampla das possibilidades! _Experimente executar alguns destes prompts no sandbox ou usar o OpenAI Playground para ver o que acontece!_

<!--
MODELO DE LIÇÃO:
Esta unidade deve cobrir o conceito básico #1.
Reforçar o conceito com exemplos e referências.

CONCEITO #1:
Engenharia de Prompts.
Definir e explicar por que é necessária.
-->

## O que é Engenharia de Prompts?

Começámos esta lição por definir **Engenharia de Prompts** como o processo de _projetar e otimizar_ entradas de texto (prompts) para fornecer respostas consistentes e de qualidade (completamentos) para um dado objetivo de aplicação e modelo. Podemos pensar nisso como um processo em 2 etapas:

- _projetar_ o prompt inicial para um modelo e objetivo dados
- _refinar_ o prompt iterativamente para melhorar a qualidade da resposta

Este é necessariamente um processo de tentativa e erro que requer intuição e esforço do utilizador para obter resultados ótimos. Então, porque é importante? Para responder a essa pergunta, primeiro precisamos entender três conceitos:

- _Tokenização_ = como o modelo “vê” o prompt
- _LLMs Base_ = como o modelo base “processa” um prompt
- _LLMs Ajustados por Instrução_ = como o modelo pode agora ver “tarefas”

### Tokenização

Um LLM vê os prompts como uma _sequência de tokens_ onde diferentes modelos (ou versões de um modelo) podem tokenizar o mesmo prompt de maneiras diferentes. Como os LLMs são treinados em tokens (e não em texto bruto), a forma como os prompts são tokenizados tem um impacto direto na qualidade da resposta gerada.

Para ter uma intuição de como funciona a tokenização, experimente ferramentas como o [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abaixo. Copie o seu prompt - e veja como ele é convertido em tokens, prestando atenção a como os caracteres de espaço e os sinais de pontuação são tratados. Note que este exemplo mostra um LLM mais antigo (GPT-3) - por isso tentar isto com um modelo mais recente pode produzir um resultado diferente.

![Tokenização](../../../translated_images/pt-PT/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Conceito: Modelos Base

Uma vez que um prompt é tokenizado, a função principal do ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modelo base) é prever o token nessa sequência. Como os LLMs são treinados em enormes conjuntos de dados textuais, eles têm uma boa noção das relações estatísticas entre os tokens e podem fazer essa previsão com alguma confiança. Note que eles não compreendem o _significado_ das palavras no prompt ou token; eles apenas veem um padrão que podem “completar” com a sua próxima previsão. Podem continuar a prever a sequência até ser terminado por intervenção do utilizador ou alguma condição preestabelecida.

Quer ver como funciona um completamento baseado em prompt? Insira o prompt acima no [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) com as definições predefinidas. O sistema está configurado para tratar os prompts como pedidos de informação - por isso deve ver um completamento que satisfaz esse contexto.

Mas e se o utilizador quiser ver algo específico que cumpra certos critérios ou objetivos da tarefa? É aqui que os LLMs _ajustados por instrução_ entram em cena.

![Completamento de Chat LLM Base](../../../translated_images/pt-PT/04-playground-chat-base.65b76fcfde0caa67.webp)

### Conceito: LLMs Ajustados por Instruções

Um [LLM Ajustado por Instruções](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) começa com o modelo base e afina-o com exemplos ou pares entrada/saída (por exemplo, “mensagens” de múltiplos turnos) que podem conter instruções claras - e a resposta da IA tenta seguir essa instrução.

Isto usa técnicas como Aprendizagem por Reforço com Feedback Humano (RLHF) que podem treinar o modelo a _seguir instruções_ e _aprender com o feedback_ para que produza respostas mais adequadas a aplicações práticas e mais relevantes aos objetivos do utilizador.

Vamos experimentar - volte ao prompt acima, mas agora altere a _mensagem do sistema_ para fornecer a seguinte instrução como contexto:

> _Resuma o conteúdo que lhe é fornecido para um aluno do segundo ano. Mantenha o resultado num parágrafo com 3-5 pontos-chave._

Veja como o resultado está agora ajustado para refletir o objetivo e formato desejados? Um educador pode agora usar diretamente esta resposta nos seus slides para essa aula.

![Completamento de Chat LLM Ajustado por Instruções](../../../translated_images/pt-PT/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Porque precisamos de Engenharia de Prompts?

Agora que sabemos como os prompts são processados pelos LLMs, vamos falar sobre _porque_ precisamos de engenharia de prompts. A resposta está no facto de que os LLMs atuais apresentam vários desafios que tornam _conseguições fiáveis e consistentes_ mais difíceis de alcançar sem esforço na construção e otimização do prompt. Por exemplo:

1. **As respostas do modelo são estocásticas.** O _mesmo prompt_ provavelmente produzirá respostas diferentes com modelos diferentes ou versões do modelo. E pode até produzir resultados diferentes com o _mesmo modelo_ em diferentes momentos. _Técnicas de engenharia de prompt podem ajudar a minimizar estas variações ao fornecer melhores salvaguardas_.

1. **Os modelos podem fabricar respostas.** Os modelos são pré-treinados com _grandes mas finitos_ conjuntos de dados, o que significa que carecem de conhecimento sobre conceitos fora do âmbito do treino. Como resultado, podem produzir respostas incorretas, imaginárias ou diretamente contraditórias a factos conhecidos. _Técnicas de engenharia de prompt ajudam os utilizadores a identificar e mitigar tais fabricações, por exemplo ao pedir citações ou raciocínio à IA_.

1. **As capacidades dos modelos variarão.** Modelos mais recentes ou gerações de modelos terão capacidades mais ricas, mas também trazem peculiaridades e trocas únicas em custo e complexidade. _A engenharia de prompt pode ajudar a desenvolver boas práticas e fluxos de trabalho que abstraem diferenças e se adaptam aos requisitos específicos do modelo de forma escalável e fluida_.

Vamos ver isto em ação no OpenAI ou Azure OpenAI Playground:

- Use o mesmo prompt com diferentes implementações de LLM (por exemplo, OpenAI, Azure OpenAI, Hugging Face) - viu variações?
- Use o mesmo prompt repetidamente com a _mesma_ implementação de LLM (por exemplo, playground Azure OpenAI) - como é que estas variações diferiram?

### Exemplo de Fabricações

Neste curso, usamos o termo **“fabricação”** para referir o fenômeno em que os LLMs por vezes geram informações factualmente incorretas devido a limitações no treino ou outras restrições. Pode também ter ouvido este fenómeno referido como _“alucinações”_ em artigos populares ou artigos de pesquisa. No entanto, recomendamos fortemente usar _“fabricação”_ como termo para não antropomorfizar acidentalmente o comportamento ao atribuir uma característica humana a um resultado gerado por máquina. Isto também reforça as [diretrizes de IA Responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) do ponto de vista terminológico, eliminando termos que podem ser considerados ofensivos ou não inclusivos em alguns contextos.

Quer ter uma ideia de como as fabricações funcionam? Pense num prompt que instrua a IA a gerar conteúdo para um tópico inexistente (para garantir que não está incluído no conjunto de treino). Por exemplo - experimentei este prompt:

> **Prompt:** gerar um plano de aula sobre a Guerra Marciana de 2076.

Uma pesquisa na web mostrou-me que existem relatos fictícios (por exemplo, séries de televisão ou livros) sobre guerras marcianas - mas nenhum em 2076. O senso comum também nos diz que 2076 está _no futuro_ e, portanto, não pode estar associado a um evento real.


Então o que acontece quando executamos este prompt com diferentes fornecedores de LLM?

> **Resposta 1**: OpenAI Playground (GPT-35)

![Resposta 1](../../../translated_images/pt-PT/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Resposta 2**: Azure OpenAI Playground (GPT-35)

![Resposta 2](../../../translated_images/pt-PT/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Resposta 3**: : Hugging Face Chat Playground (LLama-2)

![Resposta 3](../../../translated_images/pt-PT/04-fabrication-huggingchat.faf82a0a51278956.webp)

Como esperado, cada modelo (ou versão do modelo) produz respostas ligeiramente diferentes devido ao comportamento estocástico e variações nas capacidades do modelo. Por exemplo, um modelo dirige-se a uma audiência de 8º ano enquanto o outro assume um estudante do ensino secundário. Mas os três modelos geraram respostas que poderiam convencer um utilizador desinformado de que o evento foi real.

Técnicas de engenharia de prompt como _metaprompting_ e _configuração de temperatura_ podem reduzir as fabricações do modelo até certo ponto. Novas _arquiteturas_ de engenharia de prompt também incorporam novas ferramentas e técnicas de forma fluida no fluxo do prompt, para mitigar ou reduzir alguns destes efeitos.

## Estudo de Caso: GitHub Copilot

Vamos encerrar esta seção dando uma ideia de como a engenharia de prompt é usada em soluções do mundo real, olhando para um Estudo de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

O GitHub Copilot é o seu "Programador de Par Inteligente de IA" - ele converte prompts de texto em completamentos de código e está integrado no seu ambiente de desenvolvimento (por exemplo, Visual Studio Code) para uma experiência de utilizador fluida. Como documentado na série de blogs abaixo, a versão mais antiga foi baseada no modelo OpenAI Codex – com engenheiros rapidamente percebendo a necessidade de ajustar o modelo e desenvolver melhores técnicas de engenharia de prompt para melhorar a qualidade do código. Em julho, eles [lançaram um modelo de IA melhorado que vai além do Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugestões ainda mais rápidas.

Leia as publicações por ordem, para acompanhar a jornada de aprendizagem deles.

- **Maio 2023** | [GitHub Copilot está a melhorar na compreensão do seu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maio 2023** | [Dentro do GitHub: a trabalhar com os LLMs por trás do GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Como escrever melhores prompts para o GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot vai além do Codex com modelo de IA melhorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Guia do programador para Engenharia de Prompt e LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Set 2023** | [Como construir uma aplicação de LLM empresarial: lições do GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Pode também explorar o [blog de Engenharia](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para mais publicações como [esta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que mostram como estes modelos e técnicas são _aplicados_ para alimentar aplicações do mundo real.

---

<!--
MODELO DE LIÇÃO:
Esta unidade deve cobrir o conceito principal #2.
Reforce o conceito com exemplos e referências.

CONCEITO #2:
Design de Prompt.
Ilustrado com exemplos.
-->

## Construção de Prompt

Já vimos porque a engenharia de prompt é importante - agora vamos entender como os prompts são _construídos_ para que possamos avaliar diferentes técnicas para um design de prompt mais eficaz.

### Prompt Básico

Vamos começar com o prompt básico: uma entrada de texto enviada ao modelo sem qualquer outro contexto. Aqui está um exemplo - quando enviamos as primeiras palavras do hino nacional dos EUA para a OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) ele instantaneamente _completa_ a resposta com as próximas linhas, ilustrando o comportamento básico de predição.

| Prompt (Entrada)   | Completação (Saída)                                                                                                                         |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Parece que está a começar a letra de "The Star-Spangled Banner", o hino nacional dos Estados Unidos. A letra completa é ...                |

### Prompt Complexo

Agora vamos adicionar contexto e instruções a esse prompt básico. A [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) permite construir um prompt complexo como uma coleção de _mensagens_ com:

- Pares de entrada/saída refletindo a entrada do _utilizador_ e a resposta do _assistente_.
- Mensagem do sistema definindo o contexto para o comportamento ou personalidade do assistente.

O pedido está agora na forma abaixo, onde a _tokenização_ captura efetivamente a informação relevante do contexto e da conversa. Agora, alterar o contexto do sistema pode ser tão impactante na qualidade das completions quanto as entradas do utilizador fornecidas.

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

Nos exemplos acima, o prompt do utilizador era uma simples questão de texto que pode ser interpretada como um pedido de informação. Com os prompts de _instrução_, podemos usar esse texto para especificar uma tarefa em mais detalhe, fornecendo melhor orientação à IA. Aqui está um exemplo:

| Prompt (Entrada)                                                                                                                                                                                                                         | Completação (Saída)                                                                                                        | Tipo de Instrução   |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Escreva uma descrição da Guerra Civil                                                                                                                                                                                                   | _retornou um parágrafo simples_                                                                                            | Simples             |
| Escreva uma descrição da Guerra Civil. Forneça datas e eventos chave e descreva a sua importância                                                                                                                                      | _retornou um parágrafo seguido de uma lista de datas chave com descrições_                                                 | Complexo            |
| Escreva uma descrição da Guerra Civil em 1 parágrafo. Forneça 3 pontos com datas chave e a sua importância. Forneça mais 3 pontos com figuras históricas importantes e as suas contribuições. Retorne a saída como um ficheiro JSON | _retorna detalhes mais extensos numa caixa de texto, formatados como JSON que pode copiar e colar para um ficheiro e validar conforme necessário_ | Complexo. Formatado. |

## Conteúdo Primário

Nos exemplos acima, o prompt ainda era bastante aberto, permitindo ao LLM decidir qual parte do seu conjunto de dados pré-treinado era relevante. Com o padrão de design de _conteúdo primário_, o texto de entrada é dividido em duas partes:

- uma instrução (ação)
- conteúdo relevante (que influencia a ação)

Aqui está um exemplo onde a instrução é "resuma isto em 2 frases".

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completação (Saída)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa milésima da massa do Sol, mas duas vezes e meia a soma de todas as outras massas dos planetas do Sistema Solar. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e tem sido conhecido pelas civilizações antigas desde antes da história registada. É nomeado em homenagem ao deus romano Júpiter.[19] Quando visto a partir da Terra, Júpiter pode ser brilhante o suficiente para projetar sombras visíveis,[20] e é em média o terceiro objeto natural mais brilhante no céu noturno depois da Lua e da Vénus. <br/> **Resuma isto em 2 frases curtas** | Júpiter, o quinto planeta a partir do Sol, é o maior no Sistema Solar e é conhecido por ser um dos objetos mais brilhantes no céu noturno. Nomeado em homenagem ao deus romano Júpiter, é um gigante gasoso cuja massa é duas vezes e meia a soma das massas dos outros planetas do Sistema Solar juntos. |

O segmento de conteúdo primário pode ser usado de várias maneiras para impulsionar instruções mais eficazes:

- **Exemplos** - em vez de dizer ao modelo o que fazer com uma instrução explícita, dê-lhe exemplos do que deve fazer e deixe-o inferir o padrão.
- **Indícios** - siga a instrução com um "indício" que prepara a completition, orientando o modelo para respostas mais relevantes.
- **Modelos** - estes são 'receitas' repetíveis para prompts com espaços reservados (variáveis) que podem ser personalizadas com dados para casos de uso específicos.

Vamos explorar estes em ação.

### Usando Exemplos

Esta é uma abordagem onde se usa o conteúdo primário para "alimentar o modelo" com alguns exemplos do resultado desejado para uma determinada instrução e deixar o modelo inferir o padrão para o resultado desejado. Com base no número de exemplos fornecidos, podemos ter zero-shot prompting, one-shot prompting, few-shot prompting, etc.

O prompt agora consiste em três componentes:

- Uma descrição da tarefa
- Alguns exemplos do resultado desejado
- O início de um novo exemplo (que se torna uma descrição implícita da tarefa)

| Tipo de Aprendizagem | Prompt (Entrada)                                                                                                                                        | Completação (Saída)    |
| :------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| Zero-shot            | "The Sun is Shining". Traduza para espanhol                                                                                                          | "El Sol está brillando". |
| One-shot             | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot             | O jogador corre pelas bases => Baseball <br/> O jogador fez um ás => Ténis <br/> O jogador fez um seis => Cricket <br/> O jogador fez uma enterrada =>  | Basquetebol           |
|                      |                                                                                                                                                       |                       |

Repare como tivemos que dar a instrução explícita ("Traduza para espanhol") no prompt zero-shot, mas que ela é inferida no exemplo one-shot. O exemplo few-shot mostra como adicionar mais exemplos permite que os modelos façam inferências mais precisas sem instruções adicionais.

### Indícios do Prompt

Outra técnica para usar o conteúdo primário é fornecer _indícios_ em vez de exemplos. Neste caso, estamos a dar ao modelo um empurrão na direção certa ao _começar_ com um fragmento que reflete o formato da resposta desejada. O modelo então "pega no indício" para continuar nesse formato.

| Número de Indícios | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completação (Saída)                                                                                                                                                                                                                                                                                       |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                  | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa milésima da massa do Sol, mas duas vezes e meia a soma de todas as outras massas dos planetas do Sistema Solar. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e tem sido conhecido pelas civilizações antigas desde antes da história registada. <br/>**Resuma Isto**                                       | Júpiter é o maior planeta no nosso Sistema Solar e o quinto a partir do Sol. É um gigante gasoso com uma massa 1/1000 da do Sol, mas é mais pesado que todos os outros planetas juntos. As civilizações antigas conhecem Júpiter há muito tempo, e ele é facilmente visível no céu noturno.. |
| 1                  | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa milésima da massa do Sol, mas duas vezes e meia a soma de todas as outras massas dos planetas do Sistema Solar. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e tem sido conhecido pelas civilizações antigas desde antes da história registada. <br/>**Resuma Isto** <br/> O que aprendemos é que Júpiter | é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa milésima da massa do Sol, mas duas vezes e meia a soma de todas as outras massas dos planetas juntos. É facilmente visível a olho nu e conhecido desde a antiguidade.                        |

| 2              | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa mil vezes menor que a do Sol, mas duas vezes e meia maior que a soma de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e tem sido conhecido pelas civilizações antigas desde antes da história registada. <br/>**Resuma Isto** <br/> Top 3 Factos Que Aprendemos:         | 1. Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. <br/> 2. É um gigante gasoso com uma massa mil vezes menor que a do Sol...<br/> 3. Júpiter tem sido visível a olho nu desde os tempos antigos ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Modelos de Prompt

Um modelo de prompt é uma _receita pré-definida para um prompt_ que pode ser armazenada e reutilizada conforme necessário, para criar experiências de utilizador mais consistentes em grande escala. Na sua forma mais simples, é simplesmente uma coleção de exemplos de prompt como [este da OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) que fornece tanto os componentes interativos do prompt (mensagens do utilizador e do sistema) como o formato de pedido conduzido pela API - para suportar a reutilização.

Na sua forma mais complexa, como [este exemplo da LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) contém _marcadores de substituição_ que podem ser substituídos por dados de várias fontes (entrada do utilizador, contexto do sistema, fontes de dados externas etc.) para gerar um prompt de forma dinâmica. Isto permite criar uma biblioteca de prompts reutilizáveis que podem ser usados para proporcionar experiências de utilizador consistentes **programaticamente** em grande escala.

Finalmente, o valor real dos modelos reside na capacidade de criar e publicar _bibliotecas de prompts_ para domínios de aplicação verticais - onde o modelo de prompt é agora _otimizado_ para refletir o contexto ou exemplos específicos da aplicação que tornam as respostas mais relevantes e precisas para o público-alvo pretendido. O repositório [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) é um excelente exemplo desta abordagem, curando uma biblioteca de prompts para o domínio da educação com ênfase em objetivos-chave como planeamento de aulas, design de currículo, tutoria de estudantes, etc.

## Conteúdo de Suporte

Se pensarmos na construção de um prompt como tendo uma instrução (tarefa) e um alvo (conteúdo principal), então o _conteúdo secundário_ é como um contexto adicional que fornecemos para **influenciar a saída de alguma forma**. Pode ser parâmetros de afinação, instruções de formatação, taxonomias de tópicos, etc., que ajudam o modelo a _ajustar_ a sua resposta para se adequar aos objetivos ou expectativas desejadas do utilizador.

Por exemplo: Dado um catálogo de cursos com metadados extensos (nome, descrição, nível, etiquetas de metadados, instrutor etc.) sobre todos os cursos disponíveis no currículo:

- podemos definir uma instrução para "resumir o catálogo de cursos para o Outono de 2023"
- podemos usar o conteúdo principal para fornecer alguns exemplos da saída desejada
- podemos usar o conteúdo secundário para identificar as 5 principais "etiquetas" de interesse.

Agora, o modelo pode fornecer um resumo no formato mostrado pelos poucos exemplos – mas se um resultado tiver múltiplas etiquetas, pode priorizar as 5 etiquetas identificadas no conteúdo secundário.

---

<!--
MODELO DE AULA:
Esta unidade deve cobrir o conceito principal #1.
Reforce o conceito com exemplos e referências.

CONCEITO #3:
Técnicas de Engenharia de Prompt.
Quais são algumas técnicas básicas para engenharia de prompt?
Ilustre com alguns exercícios.
-->

## Melhores Práticas de Prompting

Agora que sabemos como os prompts podem ser _construídos_, podemos começar a pensar em como _desenhá-los_ para refletir as melhores práticas. Podemos pensar nisso em duas partes – ter a _mentalidade_ certa e aplicar as _técnicas_ corretas.

### Mentalidade de Engenharia de Prompt

A Engenharia de Prompt é um processo de tentativa e erro, por isso mantenha três fatores orientadores amplos em mente:

1. **Compreensão do Domínio é Importante.** A precisão e relevância da resposta dependem do _domínio_ em que essa aplicação ou utilizador opera. Use a sua intuição e experiência no domínio para **personalizar ainda mais as técnicas**. Por exemplo, defina _personalidades específicas do domínio_ nos seus prompts do sistema, ou use _modelos específicos do domínio_ nos seus prompts de utilizador. Forneça conteúdo secundário que reflita contextos específicos do domínio, ou use _pistas e exemplos específicos do domínio_ para orientar o modelo para padrões de uso familiares.

2. **Compreensão do Modelo é Importante.** Sabemos que os modelos são estocásticos por natureza. Mas as implementações de modelos podem variar também em termos do conjunto de dados de treino que usam (conhecimento pré-treinado), as capacidades que fornecem (por exemplo, via API ou SDK) e o tipo de conteúdo para que estão otimizados (por exemplo, código vs. imagens vs. texto). Compreenda os pontos fortes e limitações do modelo que está a usar e use esse conhecimento para _priorizar tarefas_ ou construir _modelos personalizados_ que sejam otimizados para as capacidades do modelo.

3. **Iteração & Validação são Importantes.** Os modelos estão a evoluir rapidamente, bem como as técnicas para engenharia de prompt. Como especialista no domínio, pode ter outro contexto ou critérios para _a sua_ aplicação específica que podem não se aplicar à comunidade mais ampla. Use ferramentas e técnicas de engenharia de prompt para "dar o pontapé de saída" na construção do prompt, depois itere e valide os resultados usando a sua própria intuição e experiência no domínio. Registe os seus insights e crie uma **base de conhecimento** (por exemplo, bibliotecas de prompts) que podem ser usadas como nova base por outros, para iterações mais rápidas no futuro.

## Melhores Práticas

Agora vamos ver as práticas recomendadas comuns recomendadas por profissionais da [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e da [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| O Quê                            | Por Quê                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Avaliar os modelos mais recentes. | Novas gerações de modelos provavelmente têm funcionalidades e qualidade melhoradas - mas também podem implicar custos mais elevados. Avalie-os quanto ao impacto, e depois tome decisões de migração.                                                   |
| Separar instruções e contexto    | Verifique se o seu modelo/fornecedor define _delimitadores_ para distinguir instruções, conteúdo primário e secundário mais claramente. Isto pode ajudar os modelos a atribuir pesos de forma mais precisa aos tokens.                              |
| Seja específico e claro          | Dê mais detalhes sobre o contexto desejado, resultado, extensão, formato, estilo, etc. Isto irá melhorar tanto a qualidade como a consistência das respostas. Capture receitas em modelos reutilizáveis.                                               |
| Seja descritivo, use exemplos    | Os modelos podem responder melhor a uma abordagem de "mostrar e contar". Comece com uma abordagem `zero-shot` onde dá uma instrução (mas sem exemplos) e tente depois `few-shot` como refinamento, fornecendo alguns exemplos da saída desejada. Use analogias. |
| Use pistas para iniciar completions | Empurre-o em direção a um resultado desejado dando-lhe algumas palavras ou frases iniciais que podem ser usadas como ponto de partida para a resposta.                                                                                                |
| Reforce                        | Às vezes pode precisar de repetir-se ao modelo. Dê instruções antes e depois do conteúdo principal, use uma instrução e uma pista, etc. Itere e valide para ver o que resulta melhor.                                                               |
| A ordem importa                  | A ordem em que apresenta a informação ao modelo pode impactar a saída, mesmo nos exemplos de aprendizagem, devido ao viés de recência. Experimente opções diferentes para ver o que funciona melhor.                                                   |
| Dê uma “saída” ao modelo         | Dê ao modelo uma resposta _de recurso_ que possa fornecer caso não consiga completar a tarefa por qualquer motivo. Isto pode reduzir a probabilidade de os modelos gerarem respostas falsas ou fabricadas.                                          |
|                                 |                                                                                                                                                                                                                                                    |

Como em qualquer boa prática, lembre-se que _a sua experiência pode variar_ com base no modelo, na tarefa e no domínio. Use estas como ponto de partida e itere para encontrar o que funciona melhor para si. Reavalie constantemente o seu processo de engenharia de prompt à medida que novos modelos e ferramentas se tornam disponíveis, com foco na escalabilidade do processo e na qualidade da resposta.

<!--
MODELO DE AULA:
Esta unidade deve fornecer um desafio de código, se aplicável

DESAFIO:
Link para um Jupyter Notebook com apenas os comentários de código nas instruções (as secções de código estão vazias).

SOLUÇÃO:
Link para uma cópia desse Notebook com os prompts preenchidos e executados, mostrando um exemplo possível.
-->

## Tarefa

Parabéns! Chegou ao fim da lição! É hora de pôr alguns desses conceitos e técnicas à prova com exemplos reais!

Para a nossa tarefa, vamos usar um Jupyter Notebook com exercícios que pode completar interativamente. Também pode estender o Notebook com as suas próprias células Markdown e de Código para explorar ideias e técnicas por conta própria.

### Para começar, faça um fork do repo, depois

- (Recomendado) Lance o GitHub Codespaces
- (Alternativamente) Clone o repo para o seu dispositivo local e utilize-o com o Docker Desktop
- (Alternativamente) Abra o Notebook no seu ambiente de runtime preferido.

### Em seguida, configure as suas variáveis de ambiente

- Copie o ficheiro `.env.copy` na raiz do repo para `.env` e preencha os valores `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT`. Volte à [secção Learning Sandbox](#ambiente-de-aprendizagem) para aprender como.

### Em seguida, abra o Jupyter Notebook

- Selecione o kernel de runtime. Se usar as opções 1 ou 2, simplesmente selecione o kernel Python 3.10.x por defeito fornecido pelo contentor de desenvolvimento.

Está tudo pronto para executar os exercícios. Note que não há respostas _certas ou erradas_ aqui – é apenas explorar opções por tentativa e erro e criar intuição para o que funciona para um dado modelo e domínio de aplicação.

_Por esta razão, não há segmentos de solução de código nesta lição. Em vez disso, o Notebook terá células Markdown intituladas "A Minha Solução:" que mostram um exemplo de saída para referência._

 <!--
MODELO DE AULA:
Envolva a secção com um resumo e recursos para aprendizagem auto-guiada.
-->

## Verificação do Conhecimento

Qual dos seguintes é um bom prompt seguindo algumas práticas recomendadas razoáveis?

1. Mostra-me uma imagem de um carro vermelho
2. Mostra-me uma imagem de um carro vermelho da marca Volvo e modelo XC90 estacionado perto de um penhasco com o sol a pôr-se
3. Mostra-me uma imagem de um carro vermelho da marca Volvo e modelo XC90

A: 2, é o melhor prompt pois fornece detalhes sobre "o quê" e entra em especificidades (não qualquer carro, mas uma marca e modelo específicos) e também descreve o cenário geral. O 3 é a segunda melhor opção pois também contém muita descrição.

## 🚀 Desafio

Veja se consegue usar a técnica da "pista" com o prompt: Complete a frase "Mostra-me uma imagem de um carro vermelho da marca Volvo e ". Com que responde, e como o melhoraria?

## Ótimo Trabalho! Continue a Sua Aprendizagem

Quer aprender mais sobre diferentes conceitos de Engenharia de Prompt? Vá para a [página de aprendizagem contínua](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros excelentes recursos sobre este tema.

Dirija-se à Lição 5 onde vamos ver [técnicas avançadas de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->