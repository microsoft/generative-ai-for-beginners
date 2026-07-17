# Fundamentos de Engenharia de Prompts

[![Fundamentos de Engenharia de Prompts](../../../translated_images/pt-PT/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introdução
Este módulo cobre conceitos e técnicas essenciais para criar prompts eficazes em modelos de IA generativa. A forma como escreve o seu prompt para um LLM também é importante. Um prompt cuidadosamente elaborado pode alcançar uma melhor qualidade de resposta. Mas o que exatamente significam termos como _prompt_ e _engenharia de prompt_? E como posso melhorar o _input_ do prompt que envio para o LLM? Estas são as questões que vamos tentar responder neste capítulo e no seguinte.

_IA generativa_ é capaz de criar novos conteúdos (por exemplo, texto, imagens, áudio, código, etc.) em resposta a pedidos dos utilizadores. Isto é conseguido através de _Modelos de Linguagem Grandes_ como a série GPT da OpenAI ("Generative Pre-trained Transformer") que são treinados para usar linguagem natural e código.

Os utilizadores podem agora interagir com estes modelos usando paradigmas familiares como o chat, sem necessidade de conhecimento técnico ou formação. Os modelos são _baseados em prompts_ - os utilizadores enviam um texto (prompt) e recebem a resposta da IA (compleção). Depois podem "conversar com a IA" iterativamente, em diálogos multi-turno, refinando o prompt até que a resposta corresponda às suas expectativas.

Os "prompts" tornam-se agora a principal _interface de programação_ para aplicações de IA generativa, dizendo aos modelos o que fazer e influenciando a qualidade das respostas devolvidas. A "Engenharia de Prompts" é uma área de estudo em rápido crescimento que se foca no _desenho e otimização_ dos prompts para oferecer respostas consistentes e de qualidade em escala.

## Objetivos de Aprendizagem

Nesta lição, aprendemos o que é a Engenharia de Prompts, porque é importante, e como criar prompts mais eficazes para um dado modelo e objetivo de aplicação. Vamos entender os conceitos fundamentais e as melhores práticas para engenharia de prompts - e conhecer um ambiente interativo de Jupyter Notebooks "sandbox" onde podemos ver estes conceitos aplicados a exemplos reais.

No final desta lição seremos capazes de:

1. Explicar o que é engenharia de prompts e porque é importante.
2. Descrever os componentes de um prompt e como são usados.
3. Aprender as melhores práticas e técnicas para engenharia de prompts.
4. Aplicar as técnicas aprendidas a exemplos reais, usando um endpoint OpenAI.

## Termos-Chave

Engenharia de Prompts: A prática de desenhar e refinar inputs para guiar modelos de IA a produzirem outputs desejados.
Tokenização: O processo de converter texto em unidades menores, chamadas tokens, que um modelo pode compreender e processar.
LLMs Afinados por Instruções: Modelos de Linguagem Grandes (LLMs) que foram afinados com instruções específicas para melhorar a precisão e relevância das suas respostas.

## Sandbox de Aprendizagem

A engenharia de prompts é atualmente mais arte do que ciência. A melhor forma de melhorar a nossa intuição é _praticar mais_ e adotar uma abordagem de tentativa e erro que combine expertise no domínio da aplicação com técnicas recomendadas e otimizações específicas do modelo.

O Jupyter Notebook que acompanha esta lição fornece um ambiente _sandbox_ onde pode experimentar o que aprende – à medida que avança ou como parte do desafio de código no final. Para executar os exercícios, vai precisar de:

1. **Uma chave de API Azure OpenAI** - o endpoint do serviço para um LLM disponível.
2. **Um runtime Python** - onde o Notebook pode ser executado.
3. **Variáveis de Ambiente Locais** - _complete as etapas de [CONFIGURAÇÃO](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) para estar pronto_.

O notebook vem com exercícios _iniciantes_ - mas é incentivado a adicionar as suas próprias secções de _Markdown_ (descrição) e _Código_ (pedidos de prompt) para experimentar mais exemplos ou ideias - e desenvolver a sua intuição sobre o desenho de prompts.

## Guia Ilustrado

Quer ter uma visão geral do que esta lição cobre antes de começar? Veja este guia ilustrado, que lhe dá uma ideia dos principais tópicos abordados e os pontos-chave para refletir em cada um deles. O plano da lição leva-o desde o entendimento dos conceitos centrais e desafios até a abordagem deles com as técnicas e melhores práticas de engenharia de prompts relevantes. Note que a secção de "Técnicas Avançadas" neste guia refere-se a conteúdo abordado no _próximo_ capítulo deste currículo.

![Guia Ilustrado para Engenharia de Prompts](../../../translated_images/pt-PT/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## A Nossa Startup

Agora, vamos falar sobre como _este tema_ se relaciona com a missão da nossa startup de [trazer inovação em IA para a educação](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicações de IA para _aprendizagem personalizada_ – então vamos pensar em como diferentes utilizadores da nossa aplicação podem "desenhar" prompts:

- **Administradores** podem pedir à IA para _analisar dados curriculares para identificar lacunas na cobertura_. A IA pode resumir os resultados ou visualizá-los com código.
- **Educadores** podem pedir à IA para _gerar um plano de aula para um público e tema alvo_. A IA pode construir o plano personalizado num formato especificado.
- **Estudantes** podem pedir à IA para _tutorar numa matéria difícil_. A IA pode agora guiar os estudantes com aulas, dicas e exemplos ajustados ao seu nível.

Isto é só a ponta do iceberg. Veja [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – uma biblioteca open-source de prompts curada por especialistas em educação – para ter uma noção mais ampla das possibilidades! _Experimente executar alguns desses prompts no sandbox ou usar o OpenAI Playground para ver o que acontece!_

<!--
MODELO DE LIÇÃO:
Esta unidade deve cobrir o conceito central #1.
Reforçar o conceito com exemplos e referências.

CONCEITO #1:
Engenharia de Prompts.
Definição e explicação da sua necessidade.
-->

## O que é Engenharia de Prompts?

Começámos esta lição definindo **Engenharia de Prompts** como o processo de _desenhar e otimizar_ inputs de texto (prompts) para entregar respostas consistentes e de qualidade (compleções) para um dado objetivo de aplicação e modelo. Podemos pensar nisso como um processo em 2 etapas:

- _desenhar_ o prompt inicial para um dado modelo e objetivo
- _refinar_ o prompt iterativamente para melhorar a qualidade da resposta

Este é necessariamente um processo de tentativa e erro que requer intuição e esforço do utilizador para obter resultados ótimos. Então porque é que é importante? Para responder a essa questão, precisamos primeiro de entender três conceitos:

- _Tokenização_ = como o modelo "vê" o prompt
- _LLMs Base_ = como o modelo base trata um prompt
- _LLMs Afinados por Instruções_ = como o modelo consegue agora ver "tarefas"

### Tokenização

Um LLM vê os prompts como uma _sequência de tokens_ onde diferentes modelos (ou versões de um modelo) podem tokenizar o mesmo prompt de formas diferentes. Como os LLMs são treinados em tokens (e não em texto bruto), a forma como os prompts são tokenizados tem impacto direto na qualidade da resposta gerada.

Para obter uma intuição de como a tokenização funciona, experimente ferramentas como o [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abaixo. Copie o seu prompt – e veja como é convertido em tokens, prestando atenção a como são tratados caracteres de espaço e sinais de pontuação. Note que este exemplo mostra um LLM mais antigo (GPT-3) – portanto experimentar isto com um modelo mais recente pode produzir um resultado diferente.

![Tokenização](../../../translated_images/pt-PT/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Conceito: Modelos Fundação

Depois de um prompt ser tokenizado, a função principal do ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modelo Fundação) é prever o token seguinte nessa sequência. Como os LLMs são treinados em enormes conjuntos de dados textuais, eles têm uma boa perceção das relações estatísticas entre tokens e podem fazer essa previsão com alguma confiança. Note que eles não entendem o _significado_ das palavras ou tokens; eles veem apenas um padrão que podem "completar" com a próxima previsão. Podem continuar a prever a sequência até serem interrompidos pela intervenção do utilizador ou por uma condição pré-estabelecida.

Quer ver como funciona a compleção baseada em prompt? Introduza o prompt acima no [playground da Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) com as definições padrão. O sistema está configurado para tratar os prompts como pedidos de informação – por isso deve ver uma resposta que satisfaça este contexto.

Mas e se o utilizador quiser ver algo específico que cumpre certos critérios ou objetivos da tarefa? É aqui que os LLMs _afinados por instruções_ entram em cena.

![Compleção de Chat com LLM Base](../../../translated_images/pt-PT/04-playground-chat-base.65b76fcfde0caa67.webp)

### Conceito: LLMs Afinados por Instruções

Um [LLM Afinado por Instruções](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) começa com o modelo Fundação e é ajustado com exemplos ou pares input/output (por exemplo, mensagens multi-turno) que podem conter instruções claras – e a resposta da IA tenta seguir essa instrução.

Isto usa técnicas como o Aprendizagem por Reforço com Feedback Humano (RLHF) que podem treinar o modelo para _seguir instruções_ e _aprender com o feedback_, para produzir respostas mais adequadas a aplicações práticas e mais relevantes para os objetivos do utilizador.

Vamos experimentar – reveja o prompt acima, mas altere a _mensagem do sistema_ para fornecer a seguinte instrução como contexto:

> _Resuma o conteúdo que lhe for fornecido para um estudante do segundo ano. Mantenha o resultado num parágrafo com 3-5 pontos de tópicos._

Veja como o resultado está agora afinado para refletir o objetivo e formato desejados? Um educador pode agora usar diretamente esta resposta nos seus slides para essa aula.

![Compleção de Chat com LLM Afinado por Instruções](../../../translated_images/pt-PT/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Porque é que precisamos de Engenharia de Prompts?

Agora que sabemos como os prompts são processados pelos LLMs, vamos falar sobre o _porquê_ de precisarmos de engenharia de prompts. A resposta está no facto de que os LLMs atuais apresentam diversos desafios que tornam mais difícil obter _compleções fiáveis e consistentes_ sem esforço na construção e otimização do prompt. Por exemplo:

1. **As respostas dos modelos são estocásticas.** O _mesmo prompt_ provavelmente produzirá respostas diferentes em modelos ou versões de modelos diferentes. E pode mesmo produzir diferentes resultados no _mesmo modelo_ em momentos distintos. _Técnicas de engenharia de prompts podem ajudar a minimizar estas variações, fornecendo melhores guardrails_.

1. **Os modelos podem fabricar respostas.** Os modelos são pré-treinados com _conjuntos grandes, mas finitos_ de dados, o que significa que não têm conhecimento sobre conceitos fora do escopo de treino. Como resultado, podem produzir compleções incorretas, imaginárias ou diretamente contraditórias a factos conhecidos. _Técnicas de engenharia de prompts ajudam os utilizadores a identificar e mitigar essas fabricações, por exemplo, pedindo citações ou raciocínio à IA_.

1. **As capacidades dos modelos variam.** Modelos novos ou gerações de modelos terão capacidades mais ricas, mas também apresentam peculiaridades e trocas únicas em custo e complexidade. _A engenharia de prompts pode ajudar a desenvolver melhores práticas e fluxos de trabalho que abstraem diferenças e se adaptam a requisitos específicos do modelo de forma escalável e fluida_.

Vamos ver isto em ação no Playground OpenAI ou Azure OpenAI:

- Use o mesmo prompt em diferentes implementações de LLM (ex: OpenAI, Azure OpenAI, Hugging Face) – viu as variações?
- Use o mesmo prompt repetidamente na _mesma_ implementação de LLM (ex: playground Azure OpenAI) – como diferiram essas variações?

### Exemplo de Fabricações

Neste curso, usamos o termo **"fabricação"** para referir o fenómeno em que os LLMs por vezes geram informação incorreta factualmente devido a limitações no seu treino ou outras restrições. Pode também ter ouvido isto referido como _"alucinações"_ em artigos populares ou artigos científicos. Contudo, recomendamos fortemente usar _"fabricação"_ para não antropomorfizar acidentalmente o comportamento, atribuindo uma característica humana a um resultado gerado por máquina. Isto também reforça as [diretrizes de IA responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) do ponto de vista terminológico, removendo termos que podem ser considerados ofensivos ou não inclusivos em alguns contextos.

Quer ter uma noção de como funcionam as fabricações? Pense num prompt que instrua a IA a gerar conteúdo para um tema inexistente (para garantir que não está no conjunto de treino). Por exemplo - experimentei este prompt:

> **Prompt:** gera um plano de aula sobre a Guerra Marciana de 2076.

Uma pesquisa web mostrou-me que há relatos de ficção (ex: séries de televisão ou livros) sobre guerras marcianas - mas nenhuma em 2076. O bom senso também nos diz que 2076 está _no futuro_ e, portanto, não pode ser associado a um evento real.


Então, o que acontece quando executamos este prompt com diferentes fornecedores de LLM?

> **Resposta 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/pt-PT/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Resposta 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/pt-PT/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Resposta 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/pt-PT/04-fabrication-huggingchat.faf82a0a51278956.webp)

Como esperado, cada modelo (ou versão de modelo) produz respostas ligeiramente diferentes graças ao comportamento estocástico e às variações na capacidade do modelo. Por exemplo, um modelo tem como alvo um público do 8º ano enquanto o outro assume um estudante do ensino secundário. Mas os três modelos geraram respostas que poderiam convencer um utilizador desinformado de que o evento era real.

Técnicas de engenharia de prompts como _metaprompting_ e _configuração de temperatura_ podem reduzir as fabricações do modelo até certo ponto. Novas _arquiteturas_ de engenharia de prompt também incorporam novas ferramentas e técnicas de forma fluida no fluxo do prompt, para mitigar ou reduzir alguns destes efeitos.

## Estudo de Caso: GitHub Copilot

Vamos encerrar esta secção compreendendo como a engenharia de prompts é usada em soluções do mundo real, analisando um Estudo de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot é o seu "Programador de Par IA" – converte prompts de texto em compilações de código e está integrado no seu ambiente de desenvolvimento (ex: Visual Studio Code) para uma experiência de utilizador fluida. Conforme documentado na série de blogs abaixo, a versão inicial foi baseada no modelo OpenAI Codex – com engenheiros rapidamente a perceber a necessidade de ajustar finamente o modelo e desenvolver melhores técnicas de engenharia de prompts, para melhorar a qualidade do código. Em julho, eles [estrearam um modelo de IA melhorado que vai além do Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugestões ainda mais rápidas.

Leia os posts por ordem para seguir a sua jornada de aprendizagem.

- **Maio 2023** | [GitHub Copilot está a melhorar a compreensão do seu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maio 2023** | [Dentro do GitHub: Trabalhar com os LLMs por trás do GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Como escrever melhores prompts para GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot vai além do Codex com um modelo de IA melhorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Guia do Desenvolvedor para Engenharia de Prompts e LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Set 2023** | [Como construir uma app LLM empresarial: Lições do GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Pode também navegar pelo seu [blog de Engenharia](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para mais posts como [este](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que mostra como estes modelos e técnicas são _aplicados_ para conduzir aplicações do mundo real.

---

<!--
MODELO DE LIÇÃO:
Esta unidade deve cobrir o conceito central #2.
Reforce o conceito com exemplos e referências.

CONCEITO #2:
Design de Prompt.
Ilustrado com exemplos.
-->

## Construção de Prompt

Vimos porque a engenharia de prompts é importante – agora vamos entender como os prompts são _construídos_ para podermos avaliar diferentes técnicas para um design de prompt mais eficaz.

### Prompt Básico

Vamos começar com o prompt básico: uma entrada de texto enviada ao modelo sem outro contexto. Aqui está um exemplo – quando enviamos as primeiras palavras do hino nacional dos EUA para a OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), ela instantaneamente _completa_ a resposta com as próximas linhas, ilustrando o comportamento básico de previsão.

| Prompt (Entrada)    | Completação (Saída)                                                                                                                         |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Parece que está a começar as letras de "The Star-Spangled Banner", o hino nacional dos Estados Unidos. As letras completas são ...            |

### Prompt Complexo

Agora vamos adicionar contexto e instruções a esse prompt básico. A [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) permite-nos construir um prompt complexo como uma coleção de _mensagens_ com:

- Pares de entrada/saída refletindo a entrada do _utilizador_ e a resposta do _assistente_.
- Mensagem do sistema definindo o contexto para comportamento ou personalidade do assistente.

O pedido está agora na forma abaixo, onde a _tokenização_ capta eficazmente a informação relevante do contexto e da conversa. Agora, mudar o contexto do sistema pode ser tão impactante na qualidade das completions como as entradas do utilizador dadas.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt de Instrução

Nos exemplos acima, o prompt do utilizador foi uma simples query de texto que pode ser interpretada como um pedido de informação. Com prompts _de instrução_, podemos usar esse texto para especificar uma tarefa com mais detalhe, fornecendo uma melhor orientação para a IA. Aqui está um exemplo:

| Prompt (Entrada)                                                                                                                                                                                                                          | Completação (Saída)                                                                                                     | Tipo de Instrução  |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- | :----------------- |
| Escreva uma descrição da Guerra Civil                                                                                                                                                                                                  | _retornou um parágrafo simples_                                                                                         | Simples            |
| Escreva uma descrição da Guerra Civil. Forneça datas e eventos principais e descreva a sua importância                                                                                                                                 | _retornou um parágrafo seguido de uma lista de datas-chave dos eventos com descrições_                                  | Complexo           |
| Escreva uma descrição da Guerra Civil num parágrafo. Forneça 3 pontos com as datas principais e a sua importância. Forneça mais 3 pontos com figuras históricas importantes e as suas contribuições. Retorne a saída num ficheiro JSON | _retorna mais detalhes extensos numa caixa de texto, formatado como JSON que pode copiar e colar num ficheiro e validar_ | Complexo. Formatado.|

## Conteúdo Primário

Nos exemplos acima, o prompt ainda era bastante aberto, permitindo ao LLM decidir que parte do seu conjunto de dados pré-treinado era relevante. Com o padrão de design _conteúdo primário_, o texto de entrada é dividido em duas partes:

- uma instrução (ação)
- conteúdo relevante (que influencia a ação)

Aqui está um exemplo onde a instrução é "resuma isto em 2 frases".

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Completação (Saída)                                                                                                                                                                                                                                                                        |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa de um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e tem sido conhecido por civilizações antigas desde antes da história registada. É nomeado após o deus romano Júpiter.[19] Quando visto da Terra, Júpiter pode ser suficientemente brilhante para que a sua luz refletida projete sombras visíveis,[20] e é em média o terceiro objeto natural mais brilhante do céu noturno depois da Lua e Vénus. <br/> **Resuma isto em 2 frases curtas** | Júpiter, o quinto planeta a partir do Sol, é o maior do Sistema Solar e é conhecido por ser um dos objetos mais brilhantes do céu noturno. Nomeado após o deus romano Júpiter, é um gigante gasoso cuja massa é duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. |

O segmento de conteúdo primário pode ser usado de várias formas para conduzir instruções mais eficazes:

- **Exemplos** – em vez de dizer ao modelo o que fazer com uma instrução explícita, dê exemplos do que fazer e deixe-o inferir o padrão.
- **Indícios** – siga a instrução com um "indício" que prepare a conclusão, orientando o modelo para respostas mais relevantes.
- **Modelos** – são 'receitas' repetíveis para prompts com espaços reservados (variáveis) que podem ser personalizados com dados para casos específicos.

Vamos explorar estes em ação.

### Utilizando Exemplos

Esta é uma abordagem onde se usa o conteúdo primário para "alimentar o modelo" com alguns exemplos da saída desejada para uma dada instrução, e deixá-lo inferir o padrão para a saída desejada. Com base no número de exemplos fornecidos, podemos ter zero-shot prompting, one-shot prompting, few-shot prompting, etc.

O prompt agora consiste em três componentes:

- Uma descrição da tarefa
- Alguns exemplos da saída desejada
- O início de um novo exemplo (que se torna uma descrição implícita da tarefa)

| Tipo de Aprendizagem | Prompt (Entrada)                                                                                                                                          | Completação (Saída)      |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------- |
| Zero-shot            | "O Sol está a brilhar". Traduza para espanhol                                                                                                          | "El Sol está brillando". |
| One-shot             | "O Sol está a brilhar" => "El Sol está brillando". <br> "É um dia frio e ventoso" =>                                                                    | "Es un día frío y ventoso". |
| Few-shot             | O jogador correu as bases => Baseball <br/> O jogador fez um ás => Tennis <br/> O jogador fez um seis => Cricket <br/> O jogador fez um slam-dunk => | Basquetebol             |
|                      |                                                                                                                                                        |                          |

Note como tivemos que fornecer instrução explícita ("Traduza para espanhol") no zero-shot prompting, mas ela é inferida no exemplo de one-shot prompting. O exemplo few-shot mostra como adicionar mais exemplos permite inferências mais precisas pelo modelo sem instruções adicionais.

### Indícios no Prompt

Outra técnica para usar conteúdo primário é fornecer _indícios_ em vez de exemplos. Neste caso, damos ao modelo um empurrão na direção certa começando com um fragmento que reflete o formato desejado da resposta. O modelo então "usa o indício" para continuar nessa linha.

| Número de Indícios | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completação (Saída)                                                                                                                                                                                                                                                                                       |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                 | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e tem sido conhecido por civilizações antigas desde antes da história registada. <br/>**Resuma Isto**                                       | Júpiter é o maior planeta do nosso Sistema Solar e o quinto a partir do Sol. É um gigante gasoso com uma massa 1/1000 da do Sol, mas é mais pesado do que todos os outros planetas juntos. Civilizações antigas conhecem Júpiter há muito tempo, e ele é facilmente visível no céu noturno. |
| 1                 | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e tem sido conhecido por civilizações antigas desde antes da história registada. <br/>**Resuma Isto** <br/> O que aprendemos é que Júpiter | é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas juntos. É facilmente visível a olho nu e é conhecido desde os tempos antigos.                         |

| 2              | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa de um milésimo da massa do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e é conhecido pelas civilizações antigas desde antes da história registada. <br/>**Resuma Isto** <br/> Top 3 Factos Que Aprendemos:         | 1. Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. <br/> 2. É um gigante gasoso com uma massa de um milésimo da massa do Sol...<br/> 3. Júpiter tem sido visível a olho nu desde tempos antigos ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Modelos de Prompt

Um modelo de prompt é uma _receita pré-definida para um prompt_ que pode ser armazenada e reutilizada conforme necessário, para proporcionar experiências de utilizador mais consistentes em grande escala. Na sua forma mais simples, é simplesmente uma coleção de exemplos de prompt como [este da OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) que fornece tanto os componentes interativos do prompt (mensagens do utilizador e do sistema) quanto o formato do pedido via API - para suportar reutilização.

Na sua forma mais complexa, como [este exemplo da LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), contém _espaços reservados_ que podem ser substituídos por dados de várias fontes (entrada do utilizador, contexto do sistema, fontes de dados externas etc.) para gerar um prompt dinamicamente. Isto permite criar uma biblioteca de prompts reutilizáveis que podem ser usados para criar experiências de utilizador **programaticamente** consistentes em grande escala.

Finalmente, o verdadeiro valor dos modelos reside na capacidade de criar e publicar _bibliotecas de prompts_ para domínios de aplicação vertical - onde o modelo de prompt é agora _otimizado_ para refletir o contexto ou exemplos específicos da aplicação que tornam as respostas mais relevantes e precisas para o público-alvo. O repositório [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) é um ótimo exemplo desta abordagem, curando uma biblioteca de prompts para o domínio da educação com ênfase em objetivos chave como planeamento de aulas, design curricular, tutoria de alunos etc.

## Conteúdo de Apoio

Se pensarmos na construção de prompts como tendo uma instrução (tarefa) e um alvo (conteúdo primário), então o _conteúdo secundário_ é como contexto adicional que fornecemos para **influenciar a saída de alguma forma**. Pode ser parâmetros de ajuste, instruções de formatação, taxonomias de tópicos etc. que ajudam o modelo a _personalizar_ a sua resposta para corresponder aos objetivos ou expectativas do utilizador desejados.

Por exemplo: Dado um catálogo de cursos com metadados extensos (nome, descrição, nível, etiquetas de metadados, instrutor etc.) sobre todos os cursos disponíveis no currículo:

- podemos definir uma instrução para "resumir o catálogo de cursos para o Outono de 2023"
- podemos usar o conteúdo primário para fornecer alguns exemplos do resultado desejado
- podemos usar o conteúdo secundário para identificar as 5 principais "etiquetas" de interesse.

Agora, o modelo pode fornecer um resumo no formato mostrado pelos exemplos - mas se um resultado tiver múltiplas etiquetas, pode priorizar as 5 etiquetas identificadas no conteúdo secundário.

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

## Melhores Práticas de Prompting

Agora que sabemos como os prompts podem ser _construídos_, podemos começar a pensar em como _desenhá-los_ para refletir as melhores práticas. Podemos pensar nisso em duas partes - ter a _mentalidade_ certa e aplicar as _técnicas_ corretas.

### Mentalidade de Engenharia de Prompt

A Engenharia de Prompt é um processo de tentativa e erro, por isso mantenha três fatores orientadores em mente:

1. **O Entendimento do Domínio é Importante.** A precisão e relevância da resposta são uma função do _domínio_ em que a aplicação ou usuário opera. Aplique a sua intuição e conhecimento do domínio para **customizar técnicas** adicionais. Por exemplo, defina _personalidades específicas do domínio_ nos seus prompts do sistema, ou use _modelos específicos do domínio_ nos seus prompts do utilizador. Forneça conteúdo secundário que reflita contextos específicos do domínio, ou use _pistas e exemplos específicos do domínio_ para guiar o modelo em direções familiares.

2. **O Entendimento do Modelo é Importante.** Sabemos que os modelos são estocásticos por natureza. Mas as implementações do modelo também podem variar quanto ao conjunto de dados de treino que usam (conhecimento pré-treinado), as capacidades que oferecem (e.g., via API ou SDK) e ao tipo de conteúdo para o qual estão otimizados (e.g., código vs. imagens vs. texto). Compreenda os pontos fortes e limitações do modelo que está a usar, e use esse conhecimento para _priorizar tarefas_ ou construir _modelos customizados_ otimizados para as capacidades do modelo.

3. **A Iteração & Validação são Importantes.** Os modelos estão a evoluir rapidamente, assim como as técnicas para engenharia de prompt. Como especialista no domínio, pode ter outro contexto ou critérios para _a sua_ aplicação específica, que podem não se aplicar à comunidade mais ampla. Use ferramentas e técnicas de engenharia de prompt para “dar o arranque” à construção do prompt, depois itere e valide os resultados usando a sua própria intuição e conhecimento do domínio. Registe os seus insights e crie uma **base de conhecimento** (e.g., bibliotecas de prompts) que podem ser usadas como novo ponto de partida por outros, para iterações mais rápidas no futuro.

## Melhores Práticas

Vamos agora olhar para as melhores práticas comuns recomendadas pelos praticantes da [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| O quê                              | Porquê                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Avaliar os modelos mais recentes.       | As novas gerações de modelos provavelmente terão características e qualidade melhoradas - mas podem também implicar custos mais elevados. Avalie-os quanto ao impacto e depois decida sobre a migração.                                                                                |
| Separar instruções & contexto   | Verifique se o seu modelo/fornecedor define _delimitadores_ para distinguir instruções, conteúdo primário e secundário de forma mais clara. Isto pode ajudar os modelos a atribuir pesos mais precisos aos tokens.                                                         |
| Seja específico e claro             | Forneça mais detalhes sobre o contexto desejado, resultado, comprimento, formato, estilo etc. Isto irá melhorar tanto a qualidade como a consistência das respostas. Capture receitas em modelos reutilizáveis.                                                          |
| Seja descritivo, use exemplos      | Os modelos podem responder melhor a uma abordagem de "mostrar e contar". Comece com uma abordagem `zero-shot` onde dá uma instrução (mas sem exemplos) e depois tente um `few-shot` como refinamento, fornecendo alguns exemplos do resultado desejado. Use analogias. |
| Use pistas para iniciar respostas | Leve o modelo para um resultado desejado dando-lhe algumas palavras ou frases iniciais que possa usar como ponto de partida para a resposta.                                                                                                               |
| Reforce                         | Por vezes, pode precisar de se repetir para o modelo. Forneça instruções antes e depois do conteúdo primário, use uma instrução e uma pista, etc. Itere e valide para ver o que funciona.                                                         |
| A ordem importa                  | A ordem em que apresenta a informação ao modelo pode impactar a resposta, mesmo nos exemplos de aprendizagem, devido ao viés da recência. Experimente diferentes opções para ver o que funciona melhor.                                                               |
| Dê uma “escapatória” ao modelo           | Dê ao modelo uma resposta de _recuperação_ que possa fornecer se não conseguir completar a tarefa por qualquer motivo. Isto pode reduzir as hipóteses de o modelo gerar respostas falsas ou fabricadas.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Como em qualquer melhor prática, lembre-se que _a sua experiência pode variar_ dependendo do modelo, da tarefa e do domínio. Use estas como ponto de partida e itere para encontrar o que funciona melhor para si. Reavalie constantemente o seu processo de engenharia de prompt à medida que novos modelos e ferramentas ficam disponíveis, focando-se na escalabilidade do processo e na qualidade da resposta.

<!--
MODELO DE AULA:
Esta unidade deverá fornecer um desafio de código caso aplicável

DESAFIO:
Ligação para um Jupyter Notebook apenas com os comentários no código nas instruções (as secções de código estão vazias).

SOLUÇÃO:
Ligação para uma cópia desse Notebook com os prompts preenchidos e executados, mostrando um exemplo de saída.
-->

## Tarefa

Parabéns! Chegaste ao fim da lição! É hora de pôr alguns desses conceitos e técnicas à prova com exemplos reais!

Para a nossa tarefa, usaremos um Jupyter Notebook com exercícios que podes completar interativamente. Também podes expandir o Notebook com as tuas próprias células Markdown e de Código para explorar ideias e técnicas por tua conta.

### Para começar, fork o repositório e depois

- (Recomendado) Lança GitHub Codespaces
- (Alternativamente) Clona o repositório para o teu dispositivo local e usa-o com Docker Desktop
- (Alternativamente) Abre o Notebook com o teu ambiente de runtime preferido.

### A seguir, configura as tuas variáveis de ambiente

- Copia o ficheiro `.env.copy` na raiz do repositório para `.env` e preenche os valores de `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT`. Volta à [secção Learning Sandbox](#sandbox-de-aprendizagem) para aprender como.

### A seguir, abre o Jupyter Notebook

- Seleciona o kernel de runtime. Se usares as opções 1 ou 2, basta selecionar o kernel padrão Python 3.10.x fornecido pelo contentor de desenvolvimento.

Estás pronto para executar os exercícios. Nota que não há _respostas certas e erradas_ aqui - é apenas a exploração de opções por tentativa e erro e construção de intuição para o que funciona para um dado modelo e domínio de aplicação.

_Por esta razão, não há segmentos de Solução de Código nesta lição. Em vez disso, o Notebook terá células Markdown intituladas "A Minha Solução:" que mostra um exemplo de saída para referência._

 <!--
MODELO DE AULA:
Encerre a secção com um resumo e recursos para aprendizagem autónoma.
-->

## Verificação de Conhecimento

Qual dos seguintes é um bom prompt seguindo algumas práticas recomendadas razoáveis?

1. Mostra-me uma imagem de carro vermelho
2. Mostra-me uma imagem de um carro vermelho da marca Volvo e modelo XC90 estacionado junto a um penhasco com o sol a pôr-se
3. Mostra-me uma imagem de carro vermelho da marca Volvo e modelo XC90

A: 2, é o melhor prompt pois fornece detalhes sobre o "quê" e vai para detalhes específicos (não um carro qualquer, mas uma marca e modelo específicos) e também descreve o cenário geral. 3 é o segundo melhor pois também contém muita descrição.

## 🚀 Desafio

Vê se consegues usar a técnica da “pista” com o prompt: Completa a frase "Mostra-me uma imagem de carro vermelho da marca Volvo e ". O que responde e como melhorarias?

## Excelente Trabalho! Continua a Aprender

Queres aprender mais sobre diferentes conceitos de Engenharia de Prompt? Vai à [página de aprendizagem continuada](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre este tema.

Avança para a Lição 5 onde vamos explorar [técnicas avançadas de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->