# Fundamentos de Engenharia de Prompt

[![Prompt Engineering Fundamentals](../../images/04-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed.html?id=d54c0c69-b183-4a6c-80ed-8b1a8f299cff?WT.mc_id=academic-105485-koreyst)

A forma como você escreve seu prompt para o LLM importa. Um prompt cuidadosamente elaborado pode alcançar um resultado melhor do que um que não é. Mas o que são esses conceitos, prompt, Engenharia de Prompt e como posso melhorar o que envio para o LLM? Perguntas como essas são o que este capítulo e o próximo estão procurando responder.

_A IA Generativa_ é capaz de criar novo conteúdo (por exemplo, texto, imagens, áudio, código etc.) em resposta a solicitações do usuário. Isso é alcançado usando _Modelos de Linguagem Grandes_ (LLMs) como a série GPT ("Generative Pre-trained Transformer") da OpenAI, que são treinados para usar linguagem natural e código.

Os usuários agora podem interagir com esses modelos usando paradigmas familiares como chat, sem precisar de nenhuma experiência técnica ou treinamento. Os modelos são _baseados em prompt_ - os usuários enviam uma entrada de texto (prompt) e recebem a resposta da IA (completação). Eles podem então "conversar com a IA" de forma iterativa, em conversas de várias rodadas, refinando seu prompt até que a resposta atenda às suas expectativas.

"Prompts" agora se tornam a principal _interface de programação_ para aplicativos de IA generativa, indicando aos modelos o que fazer e influenciando a qualidade das respostas retornadas. "Engenharia de Prompt" é um campo de estudo em rápido crescimento que se concentra no _design e otimização_ de prompts para fornecer respostas consistentes e de qualidade em escala.

## Metas de Aprendizado

Nesta lição, aprenderemos o que é Engenharia de Prompt, por que isso é importante e como podemos criar prompts mais eficazes para um modelo e objetivo de aplicativo específicos. Compreenderemos os conceitos centrais e as melhores práticas para a Engenharia de Prompt - e conheceremos um ambiente interativo de Jupyter Notebooks "sandbox" onde podemos ver esses conceitos aplicados a exemplos reais.

Ao final desta lição, seremos capazes de:

1. Explicar o que é Engenharia de Prompt e por que isso importa.
2. Descrever os componentes de um prompt e como eles são usados.
3. Aprender melhores práticas e técnicas para a Engenharia de Prompt.
4. Aplicar técnicas aprendidas a exemplos reais, usando um endpoint da OpenAI.

## Sandbox de Aprendizado

A Engenharia de Prompt é atualmente mais uma arte do que uma ciência. A melhor maneira de aprimorar nossa intuição é _praticar mais_ e adotar uma abordagem de tentativa e erro que combine experiência no domínio de aplicação com técnicas recomendadas e otimizações específicas do modelo.

O Jupyter Notebook que acompanha esta lição, fornece um ambiente _sandbox_ onde você pode experimentar o que aprende - à medida que avança ou como parte do desafio de código no final. Para executar os exercícios, você precisará de:

1. Uma chave de API da OpenAI - o endpoint de serviço para um LLM implantado.

2. Um tempo de execução Python - no qual o Notebook pode ser executado.

Nós instrumentamos este repositório com um _contêiner de desenvolvimento_ (_dev container_) que vem com um tempo de execução Python 3. Abra simplesmente o repositório no GitHub Codespaces ou no seu Docker Desktop localmente para ativar o tempo de execução automaticamente. Em seguida, abra o notebook e selecione o kernel Python 3.x para preparar o Notebook para execução.

O notebook padrão está configurado para uso com uma chave de API da OpenAI. Basta copiar o arquivo `.env.copy` na raiz da pasta para `.env` e atualizar a linha `OPENAI_API_KEY=` com sua chave de API - e você estará pronto.

O notebook vem com exercícios _iniciais_, mas você é incentivado a adicionar suas próprias seções de _Markdown_ (descrição) e _Código_ (solicitações de prompt) para experimentar mais exemplos ou ideias - e construir sua intuição para o design de prompt.

## Nossa Startup

Agora, vamos falar sobre como _esse tópico_ se relaciona com a missão de nossa startup de [trazer inovação de IA para a educação](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos criar aplicações de aprendizado personalizado impulsionados por IA. Então, vamos pensar em como diferentes usuários da nossa aplicação podem "projetar" prompts:

- **Administradores** podem pedir à IA para _analisar dados do currículo para identificar lacunas na cobertura_. A IA pode resumir os resultados ou visualizá-los com código.
- **Educadores** podem pedir à IA para _gerar um plano de aula para um público-alvo e tópico_. A IA pode criar o plano personalizado em um formato especificado.
- **Alunos** podem pedir à IA para _ajudá-los em uma disciplina difícil_. A IA pode orientar os alunos com lições, dicas e exemplos adaptados ao seu nível.

Isso é apenas a ponta do iceberg. Confira [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - uma biblioteca de prompts de código aberto curada por especialistas em educação - para ter uma visão mais ampla das possibilidades! _Experimente executar alguns desses prompts na sandbox ou usando o OpenAI Playground para ver o que acontece!_

<!--
MODELO DE LIÇÃO:
Esta unidade deve abordar o conceito principal #1.
Reforce o conceito com exemplos e referências.

CONCEITO #1:
Engenharia de Prompt.
Defina-o e explique por que é necessário.
-->

## O que é Engenharia de Prompt?

Começamos esta lição definindo **Engenharia de Prompt** como o processo de _projetar e otimizar_ entradas de texto (prompts) para fornecer respostas consistentes e de qualidade (completions) para um objetivo de aplicativo e modelo específicos. Podemos pensar nisso como um processo de 2 etapas:

- _projetar_ o prompt inicial para um modelo e objetivo específicos
- _refinar_ iterativamente o prompt para melhorar a qualidade da resposta

Isso é necessariamente um processo de tentativa e erro que requer intuição do usuário e esforço para obter resultados ótimos. Então, por que é importante? Para responder a essa pergunta, primeiro precisamos entender três conceitos:

- _Tokenização_ = como o modelo "enxerga" o prompt
- _Base LLMs_ = como o modelo fundamental "processa" um prompt
- _Instruction-Tuned LLMs_ = como o modelo agora pode ver "tarefas"

### Tokenização

Um LLM vê prompts como uma _sequência de tokens_ onde diferentes modelos (ou versões de um modelo) podem tokenizar o mesmo prompt de maneiras diferentes. Como os LLMs são treinados em tokens (não em texto bruto), a forma como os prompts são tokenizados tem um impacto direto na qualidade da resposta gerada.

Para ter uma intuição de como a tokenização funciona, experimente ferramentas como o [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abaixo. Copie seu prompt e veja como ele é convertido em tokens, prestando atenção em como caracteres de espaço em branco e pontuações são tratados. Note que este exemplo mostra um LLM mais antigo (GPT-3) - então, tentar isso com um modelo mais recente pode produzir um resultado diferente.

![Tokenization](../../images/04-tokenizer-example.png?WT.mc_id=academic-105485-koreyst)

### Conceito: Modelos Fundamentais

Uma vez que um prompt é tokenizado, a função principal do ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modelo fundamental) é prever o token nessa sequência. Como os LLMs são treinados em conjuntos massivos de dados de texto, eles têm uma boa compreensão das relações estatísticas entre tokens e podem fazer essa previsão com alguma confiança.

> Observação: eles não compreendem o _significado_ das palavras no prompt ou token; eles apenas veem um padrão que podem "completar" com sua próxima previsão. Eles podem continuar prevendo a sequência até serem interrompidos pela intervenção do usuário ou alguma condição preestabelecida.

Desejam ver como a conclusão baseada em prompts funciona? Insira o prompt acima no [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) do Azure OpenAI Studio com as configurações padrão. O sistema está configurado para tratar prompts como solicitações de informação - então, você deve ver uma conclusão que atende a esse contexto.

Mas e se o usuário quiser ver algo específico que atenda a alguns critérios ou objetivos de tarefa? É aqui que os LLMs _instruídos_ entram em cena.

![Base LLM Chat Completion](../../images/04-playground-chat-base.png?WT.mc_id=academic-105485-koreyst)

### Conceito: LLMs Instruídos

Um [LLM Instruído](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) começa com o modelo fundamental e o ajusta com exemplos ou pares de entrada/saída (por exemplo, "mensagens" de várias rodadas) que podem conter instruções claras - e a resposta da IA tenta seguir essa instrução.

Isso usa técnicas como Aprendizado por Reforço com Feedback Humano (ARFH) que podem treinar o modelo a _seguir instruções_ e _aprender com feedback_ para que produza respostas mais adequadas a aplicações práticas e mais relevantes para objetivos do usuário.

Vamos experimentar - revisite o prompt acima, mas agora altere a _mensagem do sistema_ para fornecer a seguinte instrução como contexto:

> _Summarize content you are provided with for a second-grade student. Keep the result to one paragraph with 3-5 bullet points._

Veja como o resultado agora está ajustado para refletir o objetivo desejado e o formato? Um educador pode agora usar diretamente essa resposta em seus slides para aquela aula.

![Instruction Tuned LLM Chat Completion](../../images/04-playground-chat-instructions.png?WT.mc_id=academic-105485-koreyst)

## Por que precisamos de Engenharia de Prompt?

Agora que sabemos como os prompts são processados pelos LLMs, vamos falar sobre _por que_ precisamos de Engenharia de Prompt. A resposta está no fato de que os LLMs atuais apresentam uma série de desafios que tornam as _completions confiáveis e consistentes_ mais difíceis de alcançar sem esforço na criação e otimização do prompt. Por exemplo:

1. **As respostas do modelo são estocásticas.** O _mesmo prompt_ provavelmente produzirá respostas diferentes com modelos ou versões diferentes do modelo. E pode até mesmo produzir resultados diferentes com o _mesmo modelo_ em momentos diferentes. _Técnicas de Wngenharia de Prompt podem nos ajudar a minimizar essas variações fornecendo melhores diretrizes_.

1. **Os modelos podem criar respostas imaginárias.** Os modelos são pré-treinados com conjuntos de dados _grandes, mas finitos_, o que significa que eles não têm conhecimento sobre conceitos fora desse escopo de treinamento. Como resultado, podem produzir completions imprecisas, imaginárias ou diretamente contraditórias aos fatos conhecidos. _Técnicas de Engenharia de Prompt ajudam os usuários a identificar e mitigar alucinações, por exemplo, pedindo à IA por citações ou raciocínio_.

1. **As capacidades dos modelos variarão.** Modelos ou gerações de modelos mais recentes terão capacidades mais ricas, mas também trarão peculiaridades e compensações únicas em termos de custo e complexidade. _A Engenharia de Prompt pode nos ajudar a desenvolver melhores práticas e fluxos de trabalho que abstraem diferenças e se adaptam aos requisitos específicos do modelo de maneira escalável e contínua_.

Vamos ver isso em ação no OpenAI ou Azure OpenAI Playground:

- Use o mesmo prompt com diferentes implantações de LLM (por exemplo, OpenAI, Azure OpenAI, Hugging Face) - você viu as variações?
- Use o mesmo prompt repetidamente com a _mesma_ implantação de LLM (por exemplo, Azure OpenAI Playground) - como essas variações diferiram?

### Exemplo de Alucinações

Quer ter uma ideia de como as alucinações funcionam? Pense em um prompt que instrua a IA a gerar conteúdo para um tópico inexistente (para garantir que não seja encontrado no conjunto de dados de treinamento). Por exemplo - eu tentei este prompt:

> **Prompt:** generate a lesson plan on the Martian War of 2076.

Uma busca na web mostrou que havia relatos fictícios (por exemplo, séries de televisão ou livros) sobre guerras marcianas - mas nenhuma em 2076. O bom senso também nos diz que 2076 está _no futuro_ e, portanto, não pode ser associado a um evento real.

Então, o que acontece quando executamos este prompt com diferentes provedores de LLM?

> **Resposta 1**: OpenAI Playground (GPT-35)

![Resposta 1](../../images/04-fabrication-aoai.png?WT.mc_id=academic-105485-koreyst)

> **Resposta 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../images/04-fabrication-aoai.png?WT.mc_id=academic-105485-koreyst)

> **Resposta 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../images/04-fabrication-huggingchat.png?WT.mc_id=academic-105485-koreyst)

Como esperado, cada modelo (ou versão do modelo) produz respostas ligeiramente diferentes devido ao comportamento estocástico e variações nas capacidades do modelo. Por exemplo, um modelo tem como alvo uma audiência do 8º ano, enquanto o outro assume um estudante do ensino médio. Mas os três modelos geraram respostas que poderiam convencer um usuário desinformado de que o evento era real.

Técnicas de engenharia de prompt como _metaprompting_ e _configuração de temperatura_ podem reduzir as alucinações do modelo em certa medida. Novas _arquiteturas_ de engenharia de prompt também incorporam novas ferramentas e técnicas de maneira contínua no fluxo do prompt, para mitigar ou reduzir alguns desses efeitos.

## Estudo de Caso: GitHub Copilot

Vamos concluir esta seção entendendo como a engenharia de prompt é utilizada em soluções do mundo real ao analisar um Estudo de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

O GitHub Copilot é seu "Programador de Par IA" - ele converte prompts de texto em conclusões de código e está integrado ao seu ambiente de desenvolvimento (por exemplo, Visual Studio Code) para uma experiência do usuário sem interrupções. Como documentado na série de blogs abaixo, a versão mais antiga era baseada no modelo OpenAI Codex - com os engenheiros percebendo rapidamente a necessidade de ajustar o modelo e desenvolver técnicas melhores de engenharia de prompt para melhorar a qualidade do código. Em julho, eles [apresentaram um modelo de IA aprimorado que vai além do Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugestões ainda mais rápidas.

Leia as postagens na ordem para seguir a jornada de aprendizado deles.

- **Maio de 2023** | [GitHub Copilot está Melhorando na Compreensão do Seu Código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maio de 2023** | [Dentro do GitHub: Trabalhando com os LLMs por trás do GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junho de 2023** | [Como Escrever Melhores Prompts para o GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julho de 2023** | [.. GitHub Copilot vai além do Codex com modelo de IA aprimorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julho de 2023** | [Guia do Desenvolvedor para Engenharia de Prompt e LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Setembro de 2023** | [Como construir um aplicativo empresarial LLM: Lições do GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Você também pode navegar pelo [blog de Engenharia deles](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para mais postagens como [esta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que mostra como esses modelos e técnicas são _aplicados_ para impulsionar aplicações do mundo real.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Construção de Prompt

Vimos por que a Engenharia de Prompt é importante - agora vamos entender como os prompts são _construídos_ para que possamos avaliar diferentes técnicas para um design de prompt mais eficaz.

### Prompt Básico

Vamos começar com o prompt básico: uma entrada de texto enviada ao modelo sem nenhum outro contexto. Aqui está um exemplo - quando enviamos as primeiras palavras do hino nacional dos EUA para a [API de Completions da OpenAI](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), ela instantaneamente _completa_ a resposta com as próximas linhas, ilustrando o comportamento básico de previsão.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | It sounds like you're starting the lyrics to "The Star-Spangled Banner," the national anthem of the United States. The full lyrics are ... |

### Prompt Complexo

Agora, vamos adicionar contexto e instruções a esse prompt básico. A [API de Completions de Chat](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nos permite construir um prompt complexo como uma coleção de _mensagens_ com:

- Pares de entrada/saída refletindo a entrada do _usuário_ e a resposta do _assistente_.
- Mensagem do sistema definindo o contexto para o comportamento ou personalidade do assistente.

A solicitação agora está na forma abaixo, onde a _tokenização_ captura efetivamente informações relevantes do contexto e da conversa. Agora, alterar o contexto do sistema pode ter um impacto significativo na qualidade dos completamentos, assim como as entradas do usuário fornecidas.

```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um assistente prestativo."},
        {"role": "user", "content": "Quem ganhou a série mundial em 2020?"},
        {"role": "assistant", "content": "O Los Angeles Dodgers venceu a Série Mundial em 2020."},
        {"role": "user", "content": "Onde foi jogado?"}
    ]
)
```

### Prompt de Instrução

Nos exemplos acima, o prompt do usuário era uma simples consulta de texto que pode ser interpretada como uma solicitação de informações. Com prompts de _instrução_, podemos usar esse texto para especificar uma tarefa de maneira mais detalhada, fornecendo orientações melhores para a IA. Aqui está um exemplo:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruction Type    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _returned a simple paragraph_                                                                                              | Simple              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _returned a paragraph followed by a list of key event dates with descriptions_                                             | Complex             |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _returns more extensive details in a text box, formatted as JSON that you can copy-paste to a file and validate as needed_ | Complex. Formatted. |

## Conteúdo Primário

Nos exemplos acima, o prompt ainda era bastante aberto, permitindo que o LLM decidisse qual parte de seu conjunto de dados pré-treinado era relevante. Com o padrão de design de _conteúdo primário_, o texto de entrada é dividido em duas partes:

- uma instrução (ação)
- conteúdo relevante (que influencia a ação)

Aqui está um exemplo em que a instrução é: "resuma isso em 2 frases".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus. <br/> **Summarize this in 2 short sentences** | Jupiter, the fifth planet from the Sun, is the largest in the Solar System and is known for being one of the brightest objects in the night sky. Named after the Roman god Jupiter, it's a gas giant whose mass is two-and-a-half times that of all other planets in the Solar System combined. |

O segmento de conteúdo primário pode ser usado de várias maneiras para impulsionar instruções mais eficazes:

- **Exemplos** - em vez de dizer explicitamente ao modelo o que fazer com uma instrução explícita, dê a ele exemplos do que fazer e deixe-o inferir o padrão.
- **Dicas** - siga a instrução com uma "dica" que prepara o completamento, orientando o modelo para respostas mais relevantes.
- **Modelos** - são 'receitas' repetíveis de prompts com espaços reservados (variáveis) que podem ser personalizados com dados para casos de uso específicos.

Vamos explorar esses conceitos na prática.

### Usando Exemplos

Esta é uma abordagem em que você usa o conteúdo primário para "alimentar o modelo" com alguns exemplos da saída desejada para uma determinada instrução e permite que ele infera o padrão para a saída desejada. Com base no número de exemplos fornecidos, podemos ter prompting de `zero-shot`, `one-shot`, `few-shot`, etc.

O prompt agora consiste em três componentes:

- Uma descrição da tarefa
- Alguns exemplos da saída desejada
- O início de um novo exemplo (que se torna uma descrição implícita da tarefa)

  | Learning Type | Prompt (Input)                                                                                                                                        | Completion (Output)         |
  | :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
  | Zero-shot     | "The Sun is Shining". Translate to Spanish                                                                                                            | "El Sol está brillando".    |
  | One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
  | Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                  |
  |               |                                                                                                                                                       |                             |

Observe como tivemos que fornecer instruções explícitas ("Traduza para o espanhol") no prompting de `zero-shot`, mas isso é inferido no exemplo de `one-shot`. O exemplo `few-shot` mostra como adicionar mais exemplos permite que os modelos façam inferências mais precisas sem instruções adicionais.

### Dicas de Prompt

Outra técnica para usar conteúdo primário é fornecer _dicas_ em vez de exemplos. Neste caso, estamos dando ao modelo um empurrão na direção certa ao _iniciá-lo_ com um trecho que reflete o formato da resposta desejada. O modelo então "pega a dica" para continuar nessa linha.

| Number of Cues | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. <br/>**Summarize This**                                       | Jupiter is the largest planet in our Solar System and the fifth one from the Sun. It is a gas giant with a mass 1/1000th of the Sun's, but it is heavier than all the other planets combined. Ancient civilizations have known about Jupiter for a long time, and it is easily visible in the night sky.. |
| 1              | Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. <br/>**Summarize This** <br/> What we learned is that Jupiter | is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets combined. It is easily visible to the naked eye and has been known since ancient times.                        |
| 2              | Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. <br/>**Summarize This** <br/> Top 3 Facts We Learned:         | 1. Jupiter is the fifth planet from the Sun and the largest in the Solar System. <br/> 2. It is a gas giant with a mass one-thousandth that of the Sun...<br/> 3. Jupiter has been visible to the naked eye since ancient times ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

Observe como tivemos que fornecer uma instrução explícita ("Resuma Isso") no exemplo de zero dicas, mas isso é inferido no exemplo de uma dica. O exemplo de duas dicas mostra como adicionar mais dicas permite que os modelos façam inferências mais precisas sem instruções adicionais.

### Modelos de Prompt

Um modelo de prompt é uma _receita pré-definida para um prompt_ que pode ser armazenada e reutilizada conforme necessário, para proporcionar experiências do usuário mais consistentes em escala. Em sua forma mais simples, é apenas uma coleção de exemplos de prompt como [este da OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) que fornece tanto os componentes interativos do prompt (mensagens do usuário e do sistema) quanto o formato de solicitação impulsionado por API - para suportar a reutilização.

Em sua forma mais complexa, como [este exemplo em LangChain](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/?WT.mc_id=academic-105485-koreyst), contém _placeholders_ que podem ser substituídos por dados de diversas fontes (entrada do usuário, contexto do sistema, fontes de dados externas etc.) para gerar um prompt dinamicamente. Isso nos permite criar uma biblioteca de prompts reutilizáveis que podem ser usados para impulsionar experiências do usuário consistentes **programaticamente** em escala.

Finalmente, o real valor dos modelos está na capacidade de criar e publicar _bibliotecas de prompts_ para domínios de aplicação verticais - onde o modelo de prompt é agora _otimizado_ para refletir o contexto ou exemplos específicos do domínio da aplicação que tornam as respostas mais relevantes e precisas para o público-alvo.

A [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) é um ótimo exemplo dessa abordagem, criando uma biblioteca de prompts para o domínio da educação com ênfase em objetivos-chave como planejamento de aulas, design de currículo, tutoria de estudantes etc.

## Conteúdo de Suporte

Se pensarmos na criação do prompt como tendo uma instrução (tarefa) e um alvo (conteúdo principal), então o _conteúdo secundário_ é como um contexto adicional que fornecemos para **influenciar a saída de alguma forma**. Pode ser parâmetros de ajuste, instruções de formatação, taxonomias de tópicos etc. que podem ajudar o modelo a _adequar_ sua resposta para atender aos objetivos ou expectativas desejados do usuário.

Por exemplo: Dado um catálogo de cursos com metadados extensivos (nome, descrição, nível, tags de metadados, instrutor etc.) de todos os cursos disponíveis no currículo:

- podemos definir uma instrução para "resumir o catálogo de cursos para o outono de 2023"
- podemos usar o conteúdo principal para fornecer alguns exemplos da saída desejada
- podemos usar o conteúdo secundário para identificar as 5 principais "tags" de interesse.

Agora, o modelo pode fornecer um resumo no formato mostrado pelos poucos exemplos - mas se um resultado tiver várias tags, pode priorizar as 5 tags identificadas no conteúdo secundário.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
What are some basic techniques for prompt engineering?
Illustrate it with some exercises.
-->

## Melhores Práticas para Prompts

Agora que sabemos como os prompts podem ser _construídos_, podemos começar a pensar em como _projetá-los_ para refletir as melhores práticas. Podemos pensar nisso em duas partes - ter a _mentalidade_ certa e aplicar as _técnicas_ certas.

### Mentalidade de Engenharia de Prompt

A Engenharia de Prompt é um processo de tentativa e erro, então tenha em mente três fatores amplos:

1. **Entender o Domínio é Importante.** A precisão e relevância da resposta é uma função do _domínio_ no qual a aplicação ou usuário opera. Aplique sua intuição e experiência de domínio para **personalizar técnicas** ainda mais. Por exemplo, defina _personalidades específicas do domínio_ em seus prompts de sistema, ou use _modelos específicos do domínio_ em seus prompts de usuário. Forneça conteúdo secundário que reflita contextos específicos do domínio, ou use _cues e exemplos específicos do domínio_ para orientar o modelo em direção a padrões de uso familiares.

2. **Entender o Modelo é Importante.** Sabemos que os modelos são estocásticos por natureza. Mas as implementações do modelo também podem variar em termos do conjunto de dados de treinamento que eles usam (conhecimento pré-treinado), as capacidades que eles fornecem (por exemplo, via API ou SDK) e o tipo de conteúdo para o qual são otimizados (por exemplo, código vs. imagens vs. texto). Compreenda as forças e limitações do modelo que você está usando e use esse conhecimento para _priorizar tarefas_ ou construir _modelos personalizados_ otimizados para as capacidades do modelo.

3. **Iteração e Validação São Importantes.** Os modelos estão evoluindo rapidamente, e as técnicas de engenharia de prompt também. Como especialista no domínio, você pode ter outros contextos ou critérios _específicos de sua_ aplicação, que podem não se aplicar à comunidade em geral. Use ferramentas e técnicas de engenharia de prompt para "iniciar" a construção do prompt, depois itere e valide os resultados usando sua própria intuição e experiência de domínio. Registre suas percepções e crie uma **base de conhecimento** (por exemplo, bibliotecas de prompts) que pode ser usada como uma nova linha de base por outras pessoas, para iterações mais rápidas no futuro.

## Melhores Práticas

Agora, vamos dar uma olhada nas práticas recomendadas comuns pela [Open AI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e pelos praticantes da [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| What                              | Why                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluate the latest models.       | New model generations are likely to have improved features and quality - but may also incur higher costs. Evaluate them for impact, then make migration decisions.                                                                                |
| Separate instructions & context   | Check if your model/provider defines _delimiters_ to distinguish instructions, primary and secondary content more clearly. This can help models assign weights more accurately to tokens.                                                         |
| Be specific and clear             | Give more details about the desired context, outcome, length, format, style etc. This will improve both the quality and consistency of responses. Capture recipes in reusable templates.                                                          |
| Be descriptive, use examples      | Models may respond better to a "show and tell" approach. Start with a `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or hallucinatory responses.                                                      |
|                                   |                                                                                                                                                                                                                                                   |

Como em qualquer prática recomendada, lembre-se de que _seus resultados podem variar_ com base no modelo, na tarefa e no domínio. Use essas práticas como ponto de partida e itere para encontrar o que funciona melhor para você. Reavalie constantemente seu processo de engenharia de prompt à medida que novos modelos e ferramentas se tornam disponíveis, com foco na escalabilidade do processo e na qualidade das respostas.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Tarefa

Parabéns! Você chegou ao final da lição! É hora de colocar alguns desses conceitos e técnicas à prova com exemplos reais!

Para a nossa tarefa, usaremos um Jupyter Notebook com exercícios que você pode completar interativamente. Você também pode estender o Notebook com suas próprias células de Markdown e código para explorar ideias e técnicas por conta própria.

### Para começar, faça um fork do repositório, depois

- (Recomendado) Inicie o GitHub Codespaces
- (Opcional) Clone o repositório em seu dispositivo local e use-o com o Docker Desktop
- (Opcional) Abra o Notebook com seu ambiente de execução de notebook preferido.

### Em seguida, configure suas variáveis de ambiente

- Copie o arquivo `.env.copy` na raiz do repositório para `.env` e preencha o valor `OPENAI_API_KEY`. Você pode encontrar sua chave de API em seu [OpenAI Dashboard](https://beta.openai.com/account/api-keys?WT.mc_id=academic-105485-koreyst).

### Em seguida, abra o Jupyter Notebook

- Selecione o kernel de execução. Se estiver usando as opções 1 ou 2, basta selecionar o kernel Python 3.10.x padrão fornecido pelo contêiner de desenvolvimento.

Você está pronto para executar os exercícios. Lembre-se de que não há respostas _certas ou erradas_ aqui - apenas explorando opções por tentativa e erro e construindo intuição sobre o que funciona para um determinado modelo e domínio de aplicação.

_Por esse motivo, não há segmentos de Solução de Código nesta lição. Em vez disso, o Notebook terá células de Markdown intituladas "Minha Solução:" que mostram um exemplo de saída para referência._

<!--
LESSON TEMPLATE:
Wrap the section with a summary and resources for self-guided learning.
-->

## Verificação de Conhecimento

Qual das seguintes opções seria uma boa instrução seguindo as melhores práticas razoáveis?

1. Mostre-me uma imagem de um carro vermelho.
2. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90 estacionado à beira de um penhasco com o sol se pondo.
3. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90.

**Resposta:** 2, é a melhor instrução, pois fornece detalhes sobre "o que" e vai para especificidades (não apenas qualquer carro, mas uma marca e modelo específicos) e também descreve o ambiente geral. A opção 3 é a próxima melhor, pois também contém muita descrição.

## 🚀 Desafio

Veja se você consegue aproveitar a técnica de "dica" com a instrução: Complete a frase "Mostre-me uma imagem de um carro vermelho da marca Volvo e ". O que ela responde e como você melhoraria?

## Ótimo Trabalho! Continue Sua Aprendizagem

Quer aprender mais sobre diferentes conceitos de Engenharia de Instruções? Vá para a [página de aprendizado contínuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre este tema.

Agora, vamos para a Lição 5, onde exploraremos [técnicas avançadas de instrução](../../../05-advanced-prompts/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)!
