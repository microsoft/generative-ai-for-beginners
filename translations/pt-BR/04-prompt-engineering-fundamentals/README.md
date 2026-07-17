# Fundamentos de Engenharia de Prompt

[![Fundamentos de Engenharia de Prompt](../../../translated_images/pt-BR/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introdução
Este módulo aborda conceitos e técnicas essenciais para criar prompts eficazes em modelos generativos de IA. A forma como você escreve seu prompt para um LLM também importa. Um prompt cuidadosamente elaborado pode alcançar uma melhor qualidade de resposta. Mas o que exatamente significam termos como _prompt_ e _engenharia de prompt_? E como eu melhoro a _entrada_ do prompt que envio para o LLM? Estas são as perguntas que tentaremos responder neste capítulo e no próximo.

_IA Generativa_ é capaz de criar novo conteúdo (por exemplo, texto, imagens, áudio, código etc.) em resposta a solicitações do usuário. Ela realiza isso usando _Grandes Modelos de Linguagem_ como a série GPT da OpenAI ("Transformador Generativo Pré-treinado") que são treinados para usar linguagem natural e código.

Os usuários agora podem interagir com esses modelos usando paradigmas familiares como o chat, sem precisar de qualquer especialização técnica ou treinamento. Os modelos são _baseados em prompt_ - os usuários enviam uma entrada de texto (prompt) e recebem de volta a resposta da IA (completação). Eles podem então "conversar com a IA" iterativamente, em conversas de múltiplas rodadas, refinando seu prompt até que a resposta corresponda às suas expectativas.

"Prompts" agora se tornam a principal _interface de programação_ para aplicativos de IA generativa, dizendo aos modelos o que fazer e influenciando a qualidade das respostas retornadas. "Engenharia de Prompt" é um campo de estudo em rápido crescimento que foca no _design e otimização_ de prompts para entregar respostas consistentes e de qualidade em escala.

## Objetivos de Aprendizado

Nesta lição, aprenderemos o que é Engenharia de Prompt, por que ela importa, e como podemos criar prompts mais eficazes para um dado modelo e objetivo de aplicação. Entenderemos conceitos centrais e melhores práticas para engenharia de prompt - e conheceremos um ambiente interativo de Jupyter Notebooks onde podemos ver esses conceitos aplicados em exemplos reais.

Ao final desta lição seremos capazes de:

1. Explicar o que é engenharia de prompt e por que ela importa.
2. Descrever os componentes de um prompt e como são usados.
3. Aprender melhores práticas e técnicas para engenharia de prompt.
4. Aplicar as técnicas aprendidas em exemplos reais, usando um endpoint da OpenAI.

## Termos-chave

Engenharia de Prompt: A prática de projetar e refinar entradas para guiar modelos de IA a produzirem outputs desejados.
Tokenização: O processo de converter texto em unidades menores, chamadas tokens, que um modelo pode entender e processar.
LLMs Ajustados por Instruções: Grandes Modelos de Linguagem (LLMs) que foram refinados com instruções específicas para melhorar a precisão e relevância das respostas.

## Ambiente de Experimentação

Engenharia de prompt é atualmente mais arte do que ciência. A melhor forma de melhorar nossa intuição para isso é _praticar mais_ e adotar uma abordagem de tentativa e erro que combine conhecimento do domínio de aplicação com técnicas recomendadas e otimizações específicas para modelos.

O Jupyter Notebook que acompanha esta lição fornece um ambiente _sandbox_ onde você pode experimentar o que aprende - conforme avança ou como parte do desafio de código no final. Para executar os exercícios, você precisará de:

1. **Uma chave de API do Azure OpenAI** - o endpoint do serviço para um LLM implantado.
2. **Um runtime Python** - onde o Notebook pode ser executado.
3. **Variáveis de Ambiente Locais** - _complete as etapas do [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) agora para se preparar_.

O notebook vem com exercícios _inicializadores_ - mas você é incentivado a adicionar suas próprias seções de _Markdown_ (descrição) e _Código_ (solicitações de prompt) para experimentar mais exemplos ou ideias - e cultivar sua intuição para design de prompts.

## Guia Ilustrado

Quer obter uma visão geral do que esta lição cobre antes de mergulhar? Confira este guia ilustrado, que oferece uma noção dos principais tópicos abordados e os principais pontos para refletir em cada um. O roteiro da lição leva você desde a compreensão dos conceitos centrais e desafios até a abordagem deles com técnicas relevantes de engenharia de prompt e melhores práticas. Note que a seção "Técnicas Avançadas" neste guia se refere ao conteúdo do _próximo_ capítulo deste currículo.

![Guia Ilustrado para Engenharia de Prompt](../../../translated_images/pt-BR/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Nossa Startup

Agora, vamos falar sobre como _este tema_ se relaciona com a missão da nossa startup de [trazer inovação em IA para a educação](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicações com IA para _aprendizagem personalizada_ - então vamos pensar em como diferentes usuários da nossa aplicação podem "projetar" prompts:

- **Administradores** podem pedir à IA para _analisar dados do currículo para identificar lacunas na cobertura_. A IA pode resumir os resultados ou visualizá-los com código.
- **Educadores** podem pedir à IA para _gerar um plano de aula para um público-alvo e tema específicos_. A IA pode construir o plano personalizado em um formato especificado.
- **Estudantes** podem pedir à IA que _os auxilie em uma disciplina difícil_. A IA agora pode orientar os estudantes com aulas, dicas e exemplos adaptados ao seu nível.

Isto é apenas a ponta do iceberg. Confira [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - uma biblioteca open-source de prompts curada por especialistas em educação - para ter uma noção mais ampla das possibilidades! _Experimente rodar alguns desses prompts no sandbox ou usando o Playground da OpenAI para ver o que acontece!_

<!--
MODELO DE LIÇÃO:
Esta unidade deve abordar o conceito central #1.
Reforce o conceito com exemplos e referências.

CONCEITO #1:
Engenharia de Prompt.
Defina-o e explique por que é necessário.
-->

## O que é Engenharia de Prompt?

Começamos esta lição definindo **Engenharia de Prompt** como o processo de _projetar e otimizar_ entradas de texto (prompts) para entregar respostas (completações) consistentes e de qualidade para um objetivo de aplicação e modelo dados. Podemos pensar nisso como um processo de 2 etapas:

- _projetar_ o prompt inicial para um modelo e objetivo dados
- _refinar_ o prompt iterativamente para melhorar a qualidade da resposta

Este é necessariamente um processo de tentativa e erro que requer intuição e esforço do usuário para obter resultados ótimos. Então por que isso é importante? Para responder a essa pergunta, precisamos primeiro entender três conceitos:

- _Tokenização_ = como o modelo "vê" o prompt
- _LLMs Base_ = como o modelo base "processa" um prompt
- _LLMs Ajustados por Instrução_ = como o modelo agora pode ver "tarefas"

### Tokenização

Um LLM vê os prompts como uma _sequência de tokens_ onde diferentes modelos (ou versões de um modelo) podem tokenizar o mesmo prompt de maneiras diferentes. Como os LLMs são treinados em tokens (e não em texto bruto), a forma como os prompts são tokenizados impacta diretamente a qualidade da resposta gerada.

Para ter uma intuição sobre como funciona a tokenização, experimente ferramentas como o [Tokenizer da OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abaixo. Copie seu prompt - e veja como ele é convertido em tokens, observando como caracteres de espaço e pontuações são tratados. Note que este exemplo mostra um LLM mais antigo (GPT-3) - então tentar isso com um modelo mais novo pode produzir um resultado diferente.

![Tokenização](../../../translated_images/pt-BR/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Conceito: Modelos Base (Foundation Models)

Uma vez que o prompt é tokenizado, a função principal do ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modelo Foundation) é prever o token seguinte naquela sequência. Como os LLMs são treinados com massivos conjuntos de dados textuais, eles têm uma boa noção das relações estatísticas entre tokens e podem fazer essa previsão com alguma confiança. Note que eles não entendem o _significado_ das palavras no prompt ou token; eles apenas veem um padrão que podem "completar" com sua próxima previsão. Eles podem continuar prevendo a sequência até serem interrompidos por intervenção do usuário ou alguma condição pré-estabelecida.

Quer ver como funciona uma completação baseada em prompt? Insira o prompt acima no [playground Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) com as configurações padrão. O sistema está configurado para tratar prompts como pedidos de informação - então você deve ver uma completação que satisfaça esse contexto.

Mas e se o usuário quiser ver algo específico que atenda a algum critério ou objetivo de tarefa? É aí que entram os LLMs _ajustados por instrução_.

![Completação Base LLM em Chat](../../../translated_images/pt-BR/04-playground-chat-base.65b76fcfde0caa67.webp)

### Conceito: LLMs Ajustados por Instrução

Um [LLM Ajustado por Instrução](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) começa com o modelo base e o refina com exemplos ou pares de entrada/saída (por exemplo, "mensagens" de múltiplas rodadas) que podem conter instruções claras - e a resposta da IA tenta seguir essa instrução.

Isso usa técnicas como Aprendizado por Reforço com Feedback Humano (RLHF) que podem treinar o modelo a _seguir instruções_ e _aprender com feedback_ para que produza respostas mais adequadas a aplicações práticas e mais relevantes aos objetivos do usuário.

Vamos testar - revise o prompt acima, mas agora mude a _mensagem do sistema_ para fornecer a seguinte instrução como contexto:

> _Resuma o conteúdo fornecido para um aluno do segundo ano. Mantenha o resultado em um parágrafo com 3-5 pontos principais._

Veja como o resultado agora está ajustado para refletir o objetivo e formato desejados? Um educador pode agora usar essa resposta diretamente em seus slides para essa aula.

![Completação LLM Ajustado por Instruções em Chat](../../../translated_images/pt-BR/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Por que precisamos de Engenharia de Prompt?

Agora que sabemos como os prompts são processados pelos LLMs, vamos falar sobre _por que_ precisamos de engenharia de prompt. A resposta está no fato de que os LLMs atuais apresentam uma série de desafios que tornam _completações confiáveis e consistentes_ mais difíceis de alcançar sem esforço na construção e otimização do prompt. Por exemplo:

1. **Respostas dos modelos são estocásticas.** O _mesmo prompt_ provavelmente produzirá respostas diferentes com modelos ou versões de modelos distintos. E pode até gerar resultados diversos com _o mesmo modelo_ em diferentes momentos. _Técnicas de engenharia de prompt podem nos ajudar a minimizar essas variações fornecendo melhores diretrizes_.

1. **Modelos podem produzir respostas fabricadas.** Os modelos são pré-treinados com _conjuntos de dados grandes, porém finitos_, o que significa que eles não têm conhecimento sobre conceitos fora desse escopo de treinamento. Como resultado, podem gerar completações imprecisas, imaginárias ou diretamente contraditórias a fatos conhecidos. _Técnicas de engenharia de prompt ajudam usuários a identificar e mitigar tais fabricações, por exemplo, pedindo citações ou raciocínio à IA_.

1. **Capacidades dos modelos vão variar.** Modelos mais novos ou gerações de modelos terão capacidades mais ricas, mas também trazem peculiaridades e compromissos únicos em custo e complexidade. _Engenharia de prompt pode ajudar a desenvolver melhores práticas e fluxos de trabalho que abstraem diferenças e se adaptam a requisitos específicos por modelo de forma escalável e fluida_.

Vamos ver isso em ação no Playground da OpenAI ou Azure OpenAI:

- Use o mesmo prompt com diferentes implantações de LLM (por exemplo, OpenAI, Azure OpenAI, Hugging Face) - você notou as variações?
- Use o mesmo prompt repetidamente com a _mesma_ implantação de LLM (por exemplo, playground Azure OpenAI) - como essas variações diferiram?

### Exemplo de Fabricações

Neste curso, usamos o termo **"fabricação"** para nos referirmos ao fenômeno em que LLMs às vezes geram informações factualmente incorretas devido a limitações no treinamento ou outras restrições. Você também pode ter ouvido esse fenômeno chamado de _"alucinações"_ em artigos populares ou trabalhos acadêmicos. Contudo, recomendamos fortemente o uso do termo _"fabricação"_ para evitar antropomorfizar o comportamento, atribuindo uma característica humana a um resultado conduzido por máquina. Isso também reforça as [diretrizes de IA Responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) do ponto de vista terminológico, removendo termos que podem ser considerados ofensivos ou não inclusivos em alguns contextos.

Quer ter uma noção de como funcionam as fabricações? Pense em um prompt que instrui a IA a gerar conteúdo para um tópico inexistente (para garantir que não esteja no conjunto de dados de treinamento). Por exemplo - usei este prompt:

> **Prompt:** gere um plano de aula sobre a Guerra Marciana de 2076.

Uma busca na web me mostrou que existem relatos fictícios (por exemplo, séries de TV ou livros) sobre guerras marcianas - mas nenhuma em 2076. O bom senso também nos diz que 2076 é _no futuro_ e, portanto, não pode estar associado a um evento real.


O que acontece quando executamos este prompt com diferentes provedores de LLM?

> **Resposta 1**: OpenAI Playground (GPT-35)

![Resposta 1](../../../translated_images/pt-BR/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Resposta 2**: Azure OpenAI Playground (GPT-35)

![Resposta 2](../../../translated_images/pt-BR/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Resposta 3**: : Hugging Face Chat Playground (LLama-2)

![Resposta 3](../../../translated_images/pt-BR/04-fabrication-huggingchat.faf82a0a51278956.webp)

Como esperado, cada modelo (ou versão do modelo) produz respostas ligeiramente diferentes devido ao comportamento estocástico e variações na capacidade do modelo. Por exemplo, um modelo direciona uma audiência de 8ª série enquanto o outro assume um estudante do ensino médio. Mas os três modelos geraram respostas que poderiam convencer um usuário desinformado de que o evento era real.

Técnicas de engenharia de prompt como _metaprompting_ e _configuração de temperatura_ podem reduzir as fabricações do modelo até certo ponto. Novas _arquiteturas_ de engenharia de prompt também incorporam novas ferramentas e técnicas de forma integrada ao fluxo do prompt, para mitigar ou reduzir alguns desses efeitos.

## Estudo de Caso: GitHub Copilot

Vamos encerrar esta seção entendendo como a engenharia de prompt é usada em soluções do mundo real olhando para um Estudo de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot é seu "Programador Parceiro de IA" - ele converte prompts de texto em completions de código e está integrado ao seu ambiente de desenvolvimento (por exemplo, Visual Studio Code) para uma experiência de usuário perfeita. Conforme documentado na série de blogs abaixo, a versão inicial foi baseada no modelo OpenAI Codex - com engenheiros rapidamente percebendo a necessidade de ajustar finamente o modelo e desenvolver melhores técnicas de engenharia de prompt para melhorar a qualidade do código. Em julho, eles [lançaram um modelo de IA aprimorado que vai além do Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugestões ainda mais rápidas.

Leia as postagens na ordem para acompanhar a jornada de aprendizado deles.

- **Maio 2023** | [GitHub Copilot está ficando melhor em entender seu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maio 2023** | [Dentro do GitHub: trabalhando com os LLMs por trás do GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junho 2023** | [Como escrever melhores prompts para GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julho 2023** | [.. GitHub Copilot vai além do Codex com modelo de IA melhorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julho 2023** | [Guia do desenvolvedor para engenharia de prompt e LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Setembro 2023** | [Como construir um app LLM empresarial: lições do GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Você também pode visitar o [blog de Engenharia](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para mais postagens como [esta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que mostram como esses modelos e técnicas são _aplicados_ para impulsionar aplicações do mundo real.

---

<!--
MODELO DE AULA:
Esta unidade deve cobrir o conceito principal nº 2.
Reforce o conceito com exemplos e referências.

CONCEITO Nº 2:
Design de Prompt.
Ilustrado com exemplos.
-->

## Construção de Prompt

Já vimos por que a engenharia de prompt é importante - agora vamos entender como os prompts são _construídos_ para que possamos avaliar diferentes técnicas para um design de prompt mais eficaz.

### Prompt Básico

Vamos começar com o prompt básico: uma entrada de texto enviada ao modelo sem outro contexto. Aqui está um exemplo - quando enviamos as primeiras palavras do hino nacional dos EUA para o OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), ele instantaneamente _completa_ a resposta com as próximas linhas, ilustrando o comportamento básico de predição.

| Prompt (Entrada)     | Completion (Saída)                                                                                                                     |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Parece que você está começando a letra de "The Star-Spangled Banner", o hino nacional dos Estados Unidos. A letra completa é ...      |

### Prompt Complexo

Agora vamos adicionar contexto e instruções a esse prompt básico. A [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nos permite construir um prompt complexo como uma coleção de _mensagens_ com:

- Pares de entrada/saída refletindo a entrada do _usuário_ e a resposta do _assistente_.
- Mensagem do sistema definindo o contexto para o comportamento ou personalidade do assistente.

O pedido agora está na forma abaixo, onde a _tokenização_ captura efetivamente informações relevantes do contexto e da conversa. Agora, mudar o contexto do sistema pode ser tão impactante na qualidade das respostas quanto as entradas fornecidas pelo usuário.

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

Nos exemplos acima, o prompt do usuário era uma consulta de texto simples que pode ser interpretada como um pedido de informação. Com prompts de _instrução_, podemos usar esse texto para especificar uma tarefa com mais detalhes, fornecendo uma melhor orientação para a IA. Aqui está um exemplo:

| Prompt (Entrada)                                                                                                                                                                                                                        | Completion (Saída)                                                                                                        | Tipo de Instrução    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Escreva uma descrição da Guerra Civil                                                                                                                                                                                                | _retornou um parágrafo simples_                                                                                           | Simples              |
| Escreva uma descrição da Guerra Civil. Forneça datas e eventos principais e descreva sua importância                                                                                                                                 | _retornou um parágrafo seguido de uma lista de datas-chave de eventos com descrições_                                      | Complexo             |
| Escreva uma descrição da Guerra Civil em 1 parágrafo. Forneça 3 tópicos com datas-chave e sua importância. Forneça 3 tópicos adicionais com figuras históricas importantes e suas contribuições. Retorne a saída como um arquivo JSON | _retorna detalhes mais extensos em uma caixa de texto, formatada como JSON que você pode copiar e colar em um arquivo e validar conforme necessário_ | Complexo. Formatado. |

## Conteúdo Primário

Nos exemplos acima, o prompt ainda era bastante aberto, permitindo que o LLM decida qual parte de seu conjunto de treinamento prévio é relevante. Com o design de _conteúdo primário_, o texto de entrada é dividido em duas partes:

- uma instrução (ação)
- conteúdo relevante (que influencia a ação)

Aqui está um exemplo onde a instrução é "resuma isso em 2 frases".

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Completion (Saída)                                                                                                                                                                                                                                                                               |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa milésima da massa do Sol, mas duas vezes e meia a massa de todos os outros planetas do Sistema Solar combinados. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e é conhecido por civilizações antigas desde antes da história registrada. Ele é nomeado em homenagem ao deus romano Júpiter.[19] Quando visto da Terra, Júpiter pode ser brilhante o suficiente para que sua luz refletida projete sombras visíveis,[20] e é, em média, o terceiro objeto natural mais brilhante no céu noturno depois da Lua e Vênus. <br/> **Resuma isso em 2 frases curtas** | Júpiter, o quinto planeta a partir do Sol, é o maior do Sistema Solar e conhecido por ser um dos objetos mais brilhantes no céu noturno. Nomeado em homenagem ao deus romano Júpiter, é um gigante gasoso cuja massa é duas vezes e meia a massa de todos os outros planetas do Sistema Solar combinados. |

O segmento de conteúdo primário pode ser usado de várias maneiras para conduzir instruções mais eficazes:

- **Exemplos** - ao invés de dizer explicitamente ao modelo o que fazer com uma instrução explícita, forneça exemplos do que fazer e deixe o modelo inferir o padrão.
- **Indícios** - siga a instrução com um "indício" que prepara a conclusão, guiando o modelo para respostas mais relevantes.
- **Modelos** - são "receitas" repetíveis para prompts com espaços reservados (variáveis) que podem ser customizados com dados para casos de uso específicos.

Vamos explorar esses em ação.

### Usando Exemplos

Esta é uma abordagem onde você usa o conteúdo primário para "alimentar o modelo" com alguns exemplos da saída desejada para uma determinada instrução, e deixa o modelo inferir o padrão para a saída desejada. Com base na quantidade de exemplos fornecidos, podemos ter zero-shot, one-shot, few-shot prompting etc.

O prompt agora consiste em três componentes:

- Uma descrição da tarefa
- Alguns exemplos da saída desejada
- O início de um novo exemplo (que se torna uma descrição implícita da tarefa)

| Tipo de Aprendizado | Prompt (Entrada)                                                                                                                                        | Completion (Saída)         |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot           | "The Sun is Shining". Traduza para espanhol                                                                                                          | "El Sol está brillando".    |
| One-shot            | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                               | "Es un día frío y ventoso". |
| Few-shot            | O jogador correu nas bases => Beisebol <br/> O jogador fez um ace => Tênis <br/> O jogador fez um seis => Críquete <br/> O jogador fez uma enterrada => | Basquete                   |
|                     |                                                                                                                                                      |                             |

Note como tivemos que fornecer uma instrução explícita ("Traduza para espanhol") no zero-shot prompting, mas ela é inferida no exemplo one-shot. O exemplo few-shot mostra como adicionar mais exemplos permite que os modelos façam inferências mais precisas sem instruções adicionais.

### Indícios no Prompt

Outra técnica para usar conteúdo primário é fornecer _indícios_ ao invés de exemplos. Neste caso, damos um empurrãozinho no modelo _começando_ com um trecho que reflete o formato desejado da resposta. O modelo então "pega o indício" para continuar nessa linha.

| Número de Indícios | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Saída)                                                                                                                                                                                                                                                                                        |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                  | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa milésima da massa do Sol, mas duas vezes e meia a massa de todos os outros planetas do Sistema Solar combinados. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e é conhecido por civilizações antigas desde antes da história registrada. <br/>**Resuma isto**                                         | Júpiter é o maior planeta do nosso Sistema Solar e o quinto em relação ao Sol. É um gigante gasoso com uma massa 1/1000 da massa do Sol, mas é mais pesado que todos os outros planetas juntos. Civilizações antigas conhecem Júpiter há muito tempo, e ele é facilmente visível no céu noturno. |
| 1                  | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa milésima da massa do Sol, mas duas vezes e meia a massa de todos os outros planetas do Sistema Solar combinados. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e é conhecido por civilizações antigas desde antes da história registrada. <br/>**Resuma isto** <br/> O que aprendemos é que Júpiter | é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa milésima da massa do Sol, mas duas vezes e meia a massa de todos os outros planetas juntos. É facilmente visível a olho nu e conhecido desde os tempos antigos.                      |

| 2              | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia a soma das massas de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e é conhecido por civilizações antigas desde antes da história registrada. <br/>**Resuma Isso** <br/> Principais 3 Fatos Que Aprendemos:         | 1. Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. <br/> 2. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol...<br/> 3. Júpiter tem sido visível a olho nu desde os tempos antigos ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Modelos de Prompt

Um modelo de prompt é uma _receita pré-definida para um prompt_ que pode ser armazenada e reutilizada conforme necessário, para proporcionar experiências de usuário mais consistentes em larga escala. Na forma mais simples, é simplesmente uma coleção de exemplos de prompts como [este da OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) que fornece tanto os componentes do prompt interativo (mensagens do usuário e do sistema) quanto o formato da solicitação via API - para suportar reutilização.

Em sua forma mais complexa como [este exemplo da LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), contém _espaços reservados_ que podem ser substituídos por dados de várias fontes (entrada do usuário, contexto do sistema, fontes externas etc.) para gerar um prompt dinamicamente. Isso nos permite criar uma biblioteca de prompts reutilizáveis que podem ser usados para conduzir experiências de usuário consistentes **programaticamente** em escala.

Finalmente, o verdadeiro valor dos modelos reside na capacidade de criar e publicar _bibliotecas de prompt_ para domínios de aplicação vertical - onde o modelo de prompt é agora _otimizado_ para refletir contextos ou exemplos específicos da aplicação que tornam as respostas mais relevantes e precisas para o público-alvo. O repositório [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) é um excelente exemplo desse enfoque, organizando uma biblioteca de prompts para o domínio da educação com ênfase em objetivos-chave como planejamento de aulas, design curricular, tutoria de estudantes etc.

## Conteúdo de Apoio

Se pensarmos na construção de prompts como composta por uma instrução (tarefa) e um alvo (conteúdo principal), então o _conteúdo secundário_ é como um contexto adicional que fornecemos para **influenciar a saída de alguma forma**. Pode ser parâmetros de ajuste, instruções de formatação, taxonomias de tópicos etc. que ajudam o modelo a _personalizar_ sua resposta para atender aos objetivos ou expectativas desejadas pelo usuário.

Por exemplo: Dado um catálogo de cursos com metadados extensos (nome, descrição, nível, etiquetas de metadados, instrutor etc.) para todos os cursos disponíveis no currículo:

- podemos definir uma instrução para "resumir o catálogo de cursos para o outono de 2023"
- podemos usar o conteúdo principal para fornecer alguns exemplos da saída desejada
- podemos usar o conteúdo secundário para identificar as 5 principais "etiquetas" de interesse.

Agora, o modelo pode fornecer um resumo no formato mostrado pelos poucos exemplos - mas se um resultado tiver múltiplas etiquetas, ele pode priorizar as 5 etiquetas identificadas no conteúdo secundário.

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

## Melhores Práticas para Prompts

Agora que sabemos como prompts podem ser _construídos_, podemos começar a pensar em como _projetá-los_ para refletir as melhores práticas. Podemos pensar nisso em duas partes - ter a _mentalidade_ correta e aplicar as _técnicas_ certas.

### Mentalidade de Engenharia de Prompt

Engenharia de Prompt é um processo de tentativa e erro, portanto mantenha em mente três fatores amplos orientadores:

1. **Compreender o Domínio é Importante.** A precisão e relevância da resposta dependem do _domínio_ onde aquela aplicação ou usuário opera. Aplique sua intuição e expertise no domínio para **customizar técnicas** ainda mais. Por exemplo, defina _personalidades específicas do domínio_ em seus prompts do sistema, ou use _modelos específicos do domínio_ em seus prompts do usuário. Forneça conteúdo secundário que reflita contextos específicos do domínio, ou use _indícios e exemplos específicos do domínio_ para guiar o modelo a padrões de uso familiares.

2. **Compreender o Modelo é Importante.** Sabemos que os modelos são estocásticos por natureza. Mas as implementações de modelos podem variar em termos do conjunto de dados de treinamento usado (conhecimento pré-treinado), das capacidades oferecidas (ex.: via API ou SDK) e do tipo de conteúdo para o qual são otimizados (ex.: código vs. imagens vs. texto). Entenda os pontos fortes e limitações do modelo que está usando, e use esse conhecimento para _priorizar tarefas_ ou construir _modelos customizados_ que sejam otimizados para as capacidades do modelo.

3. **Iteração e Validação são Importantes.** Os modelos estão evoluindo rapidamente, assim como as técnicas para engenharia de prompt. Como especialista no domínio, você pode ter outro contexto ou critérios para _sua_ aplicação específica, que podem não valer para a comunidade mais ampla. Use ferramentas e técnicas de engenharia de prompt para “dar o pontapé inicial” na construção do prompt, depois itere e valide os resultados usando sua própria intuição e expertise no domínio. Registre seus insights e crie uma **base de conhecimento** (ex: bibliotecas de prompt) que podem servir de nova linha de base para outros, para iterações mais rápidas no futuro.

## Melhores Práticas

Agora vamos ver as práticas recomendadas comuns indicadas por [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| O Que                             | Por Quê                                                                                                                                                                                                                                           |
| :--------------------------------| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avalie os modelos mais recentes.   | As novas gerações de modelos provavelmente terão melhorias em recursos e qualidade - mas podem também acarretar custos maiores. Avalie-os quanto ao impacto, depois tome decisões de migração.                                                    |
| Separe instruções e contexto      | Verifique se seu modelo/fornecedor define _delimitadores_ para distinguir instruções, conteúdo primário e secundário de forma clara. Isso pode ajudar os modelos a atribuir pesos aos tokens com maior precisão.                                |
| Seja específico e claro           | Forneça mais detalhes sobre o contexto desejado, resultado, comprimento, formato, estilo etc. Isso melhorará tanto a qualidade quanto a consistência das respostas. Capture receitas em modelos reutilizáveis.                                   |
| Seja descritivo, use exemplos     | Modelos podem responder melhor a uma abordagem “mostrar e contar”. Comece com uma abordagem `zero-shot`, onde você dá uma instrução (mas sem exemplos) e depois tente `few-shot` como refinamento, fornecendo alguns exemplos do resultado desejado. Use analogias. |
| Use indícios para dar pontapé inicial nas respostas | Direcione para um resultado desejado dando algumas palavras ou frases iniciais que o modelo pode usar como ponto de partida para a resposta.                                                                                                     |
| Reforce                         | Às vezes pode ser necessário repetir a instrução para o modelo. Dê instruções antes e depois do seu conteúdo principal, use instrução e indício, etc. Itere e valide para ver o que funciona.                                                  |
| A ordem importa                   | A ordem em que você apresenta a informação ao modelo pode impactar a saída, mesmo nos exemplos de aprendizagem, devido a viés de recência. Teste opções diferentes para ver qual funciona melhor.                                               |
| Dê uma “saida alternativa” ao modelo| Forneça ao modelo uma resposta alternativa de completude que ele possa dar se não conseguir completar a tarefa por alguma razão. Isso pode reduzir chances de gerar respostas falsas ou fabricadas.                                              |
|                                 |                                                                                                                                                                                                                                                  |

Como em qualquer prática recomendada, lembre-se que _os resultados podem variar_ dependendo do modelo, da tarefa e do domínio. Use esses pontos como um ponto de partida e itere para encontrar o que funciona melhor para você. Reavalie constantemente seu processo de engenharia de prompt conforme novos modelos e ferramentas forem disponibilizados, com foco na escalabilidade do processo e na qualidade das respostas.

<!--
MODELO DE AULA:
Esta unidade deve fornecer um desafio de código, se aplicável

DESAFIO:
Link para um Jupyter Notebook com apenas comentários de código nas instruções (seções de código vazias).

SOLUÇÃO:
Link para uma cópia daquele Notebook com os prompts preenchidos e executados, mostrando um exemplo.
-->

## Tarefa

Parabéns! Você chegou ao final da aula! É hora de colocar alguns desses conceitos e técnicas em prática com exemplos reais!

Para nossa tarefa, usaremos um Jupyter Notebook com exercícios que você pode completar de forma interativa. Você também pode estender o Notebook com suas próprias células Markdown e de Código para explorar ideias e técnicas por conta própria.

### Para começar, faça um fork do repositório, depois

- (Recomendado) Inicie o GitHub Codespaces
- (Alternativamente) Clone o repositório para seu dispositivo local e use com Docker Desktop
- (Alternativamente) Abra o Notebook no ambiente de execução de sua preferência.

### Em seguida, configure suas variáveis de ambiente

- Copie o arquivo `.env.copy` da raiz do repositório para `.env` e preencha os valores `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT`. Volte para a [seção Sandbox para Aprendizagem](#ambiente-de-experimentação) para aprender como.

### Depois, abra o Jupyter Notebook

- Selecione o kernel de execução. Se estiver usando as opções 1 ou 2, selecione simplesmente o kernel Python 3.10.x padrão fornecido pelo container de desenvolvimento.

Você está pronto para rodar os exercícios. Note que não existem respostas _certas ou erradas_ aqui - apenas explorar opções por tentativa e erro e construir intuição sobre o que funciona para um dado modelo e domínio de aplicação.

_Por isso não há segmentos de Solução de Código nesta aula. Em vez disso, o Notebook terá células Markdown intituladas "Minha Solução:" que mostram um exemplo de saída para referência._

 <!--
MODELO DE AULA:
Encerre a seção com um resumo e recursos para aprendizagem autodirigida.
-->

## Verificação de Conhecimento

Qual das seguintes opções é um bom prompt seguindo algumas práticas recomendadas razoáveis?

1. Mostre-me uma imagem de um carro vermelho
2. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90 estacionado perto de um penhasco com o sol se pondo
3. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90

R: 2, é o melhor prompt pois fornece detalhes sobre o "quê" e entra em especificidades (não é apenas um carro qualquer, mas uma marca e modelo específicos) e também descreve o cenário geral. A opção 3 é o segundo melhor pois também contém muita descrição.

## 🚀 Desafio

Veja se você consegue utilizar a técnica do "indício" com o prompt: Complete a frase "Mostre-me uma imagem de um carro vermelho da marca Volvo e ". O que ele responde e como você melhoraria isso?

## Ótimo Trabalho! Continue Seu Aprendizado

Quer aprender mais sobre os diferentes conceitos de Engenharia de Prompt? Vá para a [página de aprendizado continuado](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre este tema.

Vá para a Lição 5 onde veremos [técnicas avançadas de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->