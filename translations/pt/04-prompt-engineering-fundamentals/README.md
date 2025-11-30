<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0135e6c271f3ece8699050d4debbce88",
  "translation_date": "2025-10-18T00:43:03+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "pt"
}
-->
# Fundamentos de Engenharia de Prompts

[![Fundamentos de Engenharia de Prompts](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.pt.png)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introdução
Este módulo aborda conceitos e técnicas essenciais para criar prompts eficazes em modelos de IA generativa. A forma como você escreve o seu prompt para um LLM também é importante. Um prompt cuidadosamente elaborado pode alcançar uma resposta de melhor qualidade. Mas o que exatamente significam termos como _prompt_ e _engenharia de prompts_? E como posso melhorar o _input_ do prompt que envio para o LLM? Estas são as perguntas que tentaremos responder neste capítulo e no próximo.

A _IA generativa_ é capaz de criar novos conteúdos (por exemplo, texto, imagens, áudio, código etc.) em resposta a solicitações dos utilizadores. Ela faz isso utilizando _Modelos de Linguagem de Grande Escala_ como a série GPT ("Transformador Pré-treinado Generativo") da OpenAI, que são treinados para usar linguagem natural e código.

Os utilizadores agora podem interagir com esses modelos usando paradigmas familiares, como chat, sem necessidade de conhecimentos técnicos ou formação. Os modelos são _baseados em prompts_ - os utilizadores enviam um texto de entrada (prompt) e recebem de volta a resposta da IA (completação). Eles podem então "conversar com a IA" de forma iterativa, em conversas de múltiplas etapas, refinando o prompt até que a resposta atenda às suas expectativas.

Os "prompts" tornam-se agora a principal _interface de programação_ para aplicações de IA generativa, dizendo aos modelos o que fazer e influenciando a qualidade das respostas retornadas. A "Engenharia de Prompts" é um campo de estudo em rápido crescimento que se concentra no _design e otimização_ de prompts para fornecer respostas consistentes e de qualidade em escala.

## Objetivos de Aprendizagem

Nesta lição, aprenderemos o que é Engenharia de Prompts, por que ela é importante e como podemos criar prompts mais eficazes para um modelo e objetivo de aplicação específicos. Vamos entender os conceitos principais e as melhores práticas para engenharia de prompts - e aprender sobre um ambiente interativo de "sandbox" em Jupyter Notebooks onde podemos ver esses conceitos aplicados a exemplos reais.

Ao final desta lição, seremos capazes de:

1. Explicar o que é engenharia de prompts e por que ela é importante.
2. Descrever os componentes de um prompt e como eles são usados.
3. Aprender melhores práticas e técnicas para engenharia de prompts.
4. Aplicar as técnicas aprendidas a exemplos reais, usando um endpoint da OpenAI.

## Termos-Chave

Engenharia de Prompts: A prática de projetar e refinar entradas para guiar modelos de IA a produzir os resultados desejados.  
Tokenização: O processo de converter texto em unidades menores, chamadas tokens, que um modelo pode entender e processar.  
LLMs Ajustados por Instrução: Modelos de Linguagem de Grande Escala (LLMs) que foram ajustados com instruções específicas para melhorar a precisão e relevância das respostas.

## Sandbox de Aprendizagem

A engenharia de prompts é atualmente mais arte do que ciência. A melhor maneira de melhorar nossa intuição sobre isso é _praticar mais_ e adotar uma abordagem de tentativa e erro que combine expertise no domínio da aplicação com técnicas recomendadas e otimizações específicas do modelo.

O Jupyter Notebook que acompanha esta lição fornece um ambiente _sandbox_ onde você pode experimentar o que aprende - à medida que avança ou como parte do desafio de código no final. Para executar os exercícios, você precisará de:

1. **Uma chave de API do Azure OpenAI** - o endpoint de serviço para um LLM implantado.  
2. **Um ambiente de execução Python** - no qual o Notebook pode ser executado.  
3. **Variáveis de ambiente locais** - _complete os passos de [CONFIGURAÇÃO](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) agora para se preparar_.  

O notebook vem com exercícios _iniciais_ - mas você é incentivado a adicionar suas próprias seções de _Markdown_ (descrição) e _Código_ (solicitações de prompts) para experimentar mais exemplos ou ideias - e construir sua intuição para o design de prompts.

## Guia Ilustrado

Quer ter uma visão geral do que esta lição cobre antes de mergulhar? Confira este guia ilustrado, que dá uma ideia dos principais tópicos abordados e os principais pontos para você refletir em cada um. O roteiro da lição leva você desde a compreensão dos conceitos e desafios principais até abordá-los com técnicas relevantes de engenharia de prompts e melhores práticas. Note que a seção "Técnicas Avançadas" neste guia refere-se ao conteúdo abordado no _próximo_ capítulo deste currículo.

![Guia Ilustrado para Engenharia de Prompts](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.pt.png)

## Nossa Startup

Agora, vamos falar sobre como _este tema_ se relaciona com a nossa missão de startup de [trazer inovação em IA para a educação](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicações de aprendizagem personalizada baseadas em IA - então vamos pensar em como diferentes utilizadores da nossa aplicação podem "projetar" prompts:

- **Administradores** podem pedir à IA para _analisar dados curriculares para identificar lacunas na cobertura_. A IA pode resumir os resultados ou visualizá-los com código.  
- **Educadores** podem pedir à IA para _gerar um plano de aula para um público-alvo e tópico específicos_. A IA pode criar o plano personalizado em um formato especificado.  
- **Estudantes** podem pedir à IA para _tutorar em uma matéria difícil_. A IA pode orientar os estudantes com lições, dicas e exemplos adaptados ao seu nível.  

Isso é apenas a ponta do iceberg. Confira [Prompts para Educação](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - uma biblioteca de prompts de código aberto curada por especialistas em educação - para ter uma ideia mais ampla das possibilidades! _Experimente executar alguns desses prompts no sandbox ou usando o OpenAI Playground para ver o que acontece!_

<!--
MODELO DE LIÇÃO:
Esta unidade deve cobrir o conceito principal #1.
Reforce o conceito com exemplos e referências.

CONCEITO #1:
Engenharia de Prompts.
Defina e explique por que é necessária.
-->

## O que é Engenharia de Prompts?

Começamos esta lição definindo **Engenharia de Prompts** como o processo de _projetar e otimizar_ entradas de texto (prompts) para fornecer respostas consistentes e de qualidade (completações) para um objetivo de aplicação e modelo específicos. Podemos pensar nisso como um processo de 2 etapas:

- _projetar_ o prompt inicial para um modelo e objetivo específicos  
- _refinar_ o prompt de forma iterativa para melhorar a qualidade da resposta  

Este é necessariamente um processo de tentativa e erro que exige intuição e esforço do utilizador para obter resultados ótimos. Então, por que isso é importante? Para responder a essa pergunta, primeiro precisamos entender três conceitos:

- _Tokenização_ = como o modelo "enxerga" o prompt  
- _LLMs Base_ = como o modelo base "processa" um prompt  
- _LLMs Ajustados por Instrução_ = como o modelo pode agora entender "tarefas"  

### Tokenização

Um LLM enxerga prompts como uma _sequência de tokens_, onde diferentes modelos (ou versões de um modelo) podem tokenizar o mesmo prompt de maneiras diferentes. Como os LLMs são treinados em tokens (e não em texto bruto), a forma como os prompts são tokenizados tem um impacto direto na qualidade da resposta gerada.

Para ter uma ideia de como a tokenização funciona, experimente ferramentas como o [Tokenizador da OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abaixo. Copie o seu prompt - e veja como ele é convertido em tokens, prestando atenção em como os caracteres de espaço e os sinais de pontuação são tratados. Note que este exemplo mostra um LLM mais antigo (GPT-3) - então tentar isso com um modelo mais recente pode produzir um resultado diferente.

![Tokenização](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.pt.png)

### Conceito: Modelos Base

Uma vez que um prompt é tokenizado, a função principal do ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modelo base) é prever o próximo token nessa sequência. Como os LLMs são treinados em conjuntos de dados massivos de texto, eles têm uma boa noção das relações estatísticas entre os tokens e podem fazer essa previsão com alguma confiança. Note que eles não entendem o _significado_ das palavras no prompt ou token; eles apenas veem um padrão que podem "completar" com sua próxima previsão. Eles podem continuar prevendo a sequência até serem interrompidos pela intervenção do utilizador ou por alguma condição pré-estabelecida.

Quer ver como funciona a completação baseada em prompts? Insira o prompt acima no [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) do Azure OpenAI Studio com as configurações padrão. O sistema está configurado para tratar prompts como solicitações de informação - então você deve ver uma completação que satisfaça esse contexto.

Mas e se o utilizador quiser ver algo específico que atenda a alguns critérios ou objetivos de tarefa? É aqui que os LLMs _ajustados por instrução_ entram em cena.

![Completação de Chat com LLM Base](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.pt.png)

### Conceito: LLMs Ajustados por Instrução

Um [LLM Ajustado por Instrução](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) começa com o modelo base e o ajusta com exemplos ou pares de entrada/saída (por exemplo, "mensagens" de múltiplas etapas) que podem conter instruções claras - e a resposta da IA tenta seguir essa instrução.

Isso utiliza técnicas como Aprendizagem por Reforço com Feedback Humano (RLHF) que podem treinar o modelo para _seguir instruções_ e _aprender com feedback_, de modo que ele produza respostas mais adequadas para aplicações práticas e mais relevantes para os objetivos do utilizador.

Vamos experimentar - revisite o prompt acima, mas agora altere a _mensagem do sistema_ para fornecer a seguinte instrução como contexto:

> _Resuma o conteúdo fornecido para um aluno do segundo ano. Mantenha o resultado em um parágrafo com 3-5 tópicos._

Veja como o resultado agora está ajustado para refletir o objetivo e o formato desejados? Um educador pode agora usar diretamente essa resposta em seus slides para aquela aula.

![Completação de Chat com LLM Ajustado por Instrução](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.pt.png)

## Por que precisamos de Engenharia de Prompts?

Agora que sabemos como os prompts são processados pelos LLMs, vamos falar sobre _por que_ precisamos de engenharia de prompts. A resposta está no fato de que os LLMs atuais apresentam uma série de desafios que tornam _completações confiáveis e consistentes_ mais difíceis de alcançar sem esforço na construção e otimização de prompts. Por exemplo:

1. **As respostas dos modelos são estocásticas.** O _mesmo prompt_ provavelmente produzirá respostas diferentes com diferentes modelos ou versões de modelos. E pode até produzir resultados diferentes com o _mesmo modelo_ em momentos diferentes. _As técnicas de engenharia de prompts podem nos ajudar a minimizar essas variações, fornecendo melhores diretrizes_.  

1. **Os modelos podem fabricar respostas.** Os modelos são pré-treinados com _conjuntos de dados grandes, mas finitos_, o que significa que eles não têm conhecimento sobre conceitos fora desse escopo de treinamento. Como resultado, podem produzir completações que são imprecisas, imaginárias ou diretamente contraditórias aos fatos conhecidos. _As técnicas de engenharia de prompts ajudam os utilizadores a identificar e mitigar essas fabricações, por exemplo, pedindo citações ou raciocínios à IA_.  

1. **As capacidades dos modelos variam.** Modelos mais recentes ou gerações de modelos terão capacidades mais ricas, mas também trarão peculiaridades únicas e compensações em custo e complexidade. _A engenharia de prompts pode nos ajudar a desenvolver melhores práticas e fluxos de trabalho que abstraem as diferenças e se adaptam aos requisitos específicos do modelo de maneiras escaláveis e eficientes_.  

Vamos ver isso em ação no OpenAI ou no Azure OpenAI Playground:

- Use o mesmo prompt com diferentes implantações de LLM (por exemplo, OpenAI, Azure OpenAI, Hugging Face) - você percebeu as variações?  
- Use o mesmo prompt repetidamente com a _mesma_ implantação de LLM (por exemplo, playground do Azure OpenAI) - como essas variações diferiram?  

### Exemplo de Fabricações

Neste curso, usamos o termo **"fabricação"** para nos referirmos ao fenômeno em que os LLMs às vezes geram informações factualmente incorretas devido a limitações no seu treinamento ou outras restrições. Você também pode ter ouvido isso ser chamado de _"alucinações"_ em artigos populares ou trabalhos de pesquisa. No entanto, recomendamos fortemente o uso do termo _"fabricação"_ para que não antropomorfizemos o comportamento, atribuindo uma característica humana a um resultado gerado por máquina. Isso também reforça as [diretrizes de IA responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) do ponto de vista terminológico, removendo termos que podem ser considerados ofensivos ou não inclusivos em alguns contextos.

Quer ter uma ideia de como as fabricações funcionam? Pense em um prompt que instrua a IA a gerar conteúdo para um tópico inexistente (para garantir que não seja encontrado no conjunto de dados de treinamento). Por exemplo - eu tentei este prompt:

> **Prompt:** gere um plano de aula sobre a Guerra Marciana de 2076.
Uma pesquisa na web mostrou-me que existem relatos fictícios (por exemplo, séries de televisão ou livros) sobre guerras em Marte - mas nenhum em 2076. O senso comum também nos diz que 2076 está _no futuro_ e, portanto, não pode estar associado a um evento real.

Então, o que acontece quando usamos este prompt com diferentes provedores de LLM?

> **Resposta 1**: OpenAI Playground (GPT-35)

![Resposta 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.pt.png)

> **Resposta 2**: Azure OpenAI Playground (GPT-35)

![Resposta 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.pt.png)

> **Resposta 3**: Hugging Face Chat Playground (LLama-2)

![Resposta 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.pt.png)

Como esperado, cada modelo (ou versão de modelo) produz respostas ligeiramente diferentes devido ao comportamento estocástico e às variações nas capacidades dos modelos. Por exemplo, um modelo direciona-se a um público de 8º ano, enquanto outro assume um estudante do ensino secundário. Mas todos os três modelos geraram respostas que poderiam convencer um utilizador desinformado de que o evento era real.

Técnicas de engenharia de prompts, como _metaprompting_ e _configuração de temperatura_, podem reduzir as fabricações dos modelos até certo ponto. Novas arquiteturas de engenharia de prompts também incorporam novas ferramentas e técnicas de forma integrada no fluxo de prompts, para mitigar ou reduzir alguns desses efeitos.

## Estudo de Caso: GitHub Copilot

Vamos encerrar esta seção entendendo como a engenharia de prompts é usada em soluções do mundo real, analisando um Estudo de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

O GitHub Copilot é o seu "Programador Parceiro de IA" - ele converte prompts de texto em sugestões de código e está integrado no seu ambiente de desenvolvimento (por exemplo, Visual Studio Code) para uma experiência de utilizador fluida. Conforme documentado na série de blogs abaixo, a versão mais antiga foi baseada no modelo OpenAI Codex - com os engenheiros rapidamente percebendo a necessidade de ajustar o modelo e desenvolver melhores técnicas de engenharia de prompts para melhorar a qualidade do código. Em julho, eles [lançaram um modelo de IA aprimorado que vai além do Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugestões ainda mais rápidas.

Leia os posts na ordem indicada para acompanhar a jornada de aprendizado deles.

- **Maio de 2023** | [GitHub Copilot está a melhorar na compreensão do seu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maio de 2023** | [Por dentro do GitHub: Trabalhando com os LLMs por trás do GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junho de 2023** | [Como escrever melhores prompts para o GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julho de 2023** | [.. GitHub Copilot vai além do Codex com modelo de IA aprimorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julho de 2023** | [Guia do Desenvolvedor para Engenharia de Prompts e LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Setembro de 2023** | [Como construir uma aplicação empresarial com LLM: Lições do GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Também pode explorar o [blog de engenharia](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para mais posts como [este](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), que mostra como esses modelos e técnicas são _aplicados_ para impulsionar aplicações do mundo real.

---

## Construção de Prompts

Já vimos por que a engenharia de prompts é importante - agora vamos entender como os prompts são _construídos_ para que possamos avaliar diferentes técnicas para um design de prompts mais eficaz.

### Prompt Básico

Vamos começar com o prompt básico: uma entrada de texto enviada ao modelo sem nenhum outro contexto. Aqui está um exemplo - quando enviamos as primeiras palavras do hino nacional dos EUA para a [API Completion](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) da OpenAI, ela completa instantaneamente a resposta com as próximas linhas, ilustrando o comportamento básico de previsão.

| Prompt (Entrada) | Resposta (Saída)                                                                                                                        |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Parece que está a começar a letra de "The Star-Spangled Banner", o hino nacional dos Estados Unidos. A letra completa é... |

### Prompt Complexo

Agora vamos adicionar contexto e instruções ao prompt básico. A [API Chat Completion](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) permite-nos construir um prompt complexo como uma coleção de _mensagens_ com:

- Pares de entrada/saída refletindo a entrada do _utilizador_ e a resposta do _assistente_.
- Mensagem do sistema que define o contexto para o comportamento ou personalidade do assistente.

A solicitação agora tem o formato abaixo, onde a _tokenização_ captura efetivamente informações relevantes do contexto e da conversa. Alterar o contexto do sistema pode ser tão impactante na qualidade das respostas quanto as entradas fornecidas pelo utilizador.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt de Instrução

Nos exemplos acima, o prompt do utilizador era uma consulta de texto simples que pode ser interpretada como um pedido de informação. Com prompts de _instrução_, podemos usar esse texto para especificar uma tarefa com mais detalhes, fornecendo orientações melhores para a IA. Aqui está um exemplo:

| Prompt (Entrada)                                                                                                                                                                                                                         | Resposta (Saída)                                                                                                        | Tipo de Instrução   |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Escreva uma descrição da Guerra Civil                                                                                                                                                                                                   | _retornou um parágrafo simples_                                                                                        | Simples             |
| Escreva uma descrição da Guerra Civil. Forneça datas e eventos importantes e descreva sua relevância                                                                                                                                     | _retornou um parágrafo seguido por uma lista de datas importantes com descrições_                                       | Complexo            |
| Escreva uma descrição da Guerra Civil em 1 parágrafo. Forneça 3 tópicos com datas importantes e sua relevância. Forneça mais 3 tópicos com figuras históricas importantes e suas contribuições. Retorne a saída como um ficheiro JSON. | _retornou detalhes mais extensos em uma caixa de texto, formatados como JSON que pode ser copiado e validado conforme necessário_ | Complexo. Formatado.|

## Conteúdo Principal

Nos exemplos acima, o prompt ainda era bastante aberto, permitindo que o LLM decidisse qual parte do seu conjunto de dados pré-treinado era relevante. Com o padrão de design de _conteúdo principal_, o texto de entrada é dividido em duas partes:

- uma instrução (ação)
- conteúdo relevante (que influencia a ação)

Aqui está um exemplo onde a instrução é "resuma isto em 2 frases".

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Resposta (Saída)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia maior que a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e é conhecido pelas civilizações antigas desde antes da história registrada. Ele recebeu o nome do deus romano Júpiter.[19] Quando visto da Terra, Júpiter pode ser brilhante o suficiente para que sua luz refletida projete sombras visíveis,[20] e é, em média, o terceiro objeto natural mais brilhante no céu noturno, depois da Lua e de Vênus. <br/> **Resuma isto em 2 frases curtas** | Júpiter, o quinto planeta a partir do Sol, é o maior do Sistema Solar e conhecido por ser um dos objetos mais brilhantes no céu noturno. Nomeado em homenagem ao deus romano Júpiter, é um gigante gasoso cuja massa é duas vezes e meia maior que a de todos os outros planetas juntos. |

O segmento de conteúdo principal pode ser usado de várias maneiras para orientar instruções mais eficazes:

- **Exemplos** - em vez de dizer ao modelo o que fazer com uma instrução explícita, forneça exemplos do que fazer e deixe-o inferir o padrão.
- **Dicas** - siga a instrução com uma "dica" que prepara a resposta, orientando o modelo para respostas mais relevantes.
- **Templates** - são 'receitas' repetíveis para prompts com espaços reservados (variáveis) que podem ser personalizados com dados para casos de uso específicos.

Vamos explorar essas técnicas em ação.

### Usando Exemplos

Esta é uma abordagem onde você usa o conteúdo principal para "alimentar o modelo" com alguns exemplos do resultado desejado para uma determinada instrução e deixa-o inferir o padrão para o resultado desejado. Com base no número de exemplos fornecidos, podemos ter prompts zero-shot, one-shot, few-shot, etc.

O prompt agora consiste em três componentes:

- Uma descrição da tarefa
- Alguns exemplos do resultado desejado
- O início de um novo exemplo (que se torna uma descrição implícita da tarefa)

| Tipo de Aprendizado | Prompt (Entrada)                                                                                                                                        | Resposta (Saída)         |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------- |
| Zero-shot           | "O Sol está a brilhar". Traduza para espanhol                                                                                                          | "El Sol está brillando". |
| One-shot            | "O Sol está a brilhar" => ""El Sol está brillando". <br> "Está um dia frio e ventoso" =>                                                               | "Es un día frío y ventoso". |
| Few-shot            | O jogador correu as bases => Basebol <br/> O jogador acertou um ace => Ténis <br/> O jogador acertou um seis => Críquete <br/> O jogador fez um slam-dunk => | Basquetebol             |
|                     |                                                                                                                                                       |                          |

Note como tivemos que fornecer uma instrução explícita ("Traduza para espanhol") no exemplo de zero-shot, mas ela é inferida no exemplo de one-shot. O exemplo de few-shot mostra como adicionar mais exemplos permite que os modelos façam inferências mais precisas sem instruções adicionais.

### Dicas de Prompt

Outra técnica para usar o conteúdo principal é fornecer _dicas_ em vez de exemplos. Neste caso, estamos a dar ao modelo uma orientação na direção certa ao _iniciar_ com um trecho que reflete o formato de resposta desejado. O modelo então "segue a dica" para continuar nesse formato.

| Número de Dicas | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Resposta (Saída)                                                                                                                                                                                                                                                                                       |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0               | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia maior que a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e é conhecido pelas civilizações antigas desde antes da história registrada. <br/>**Resuma Isto**                                       | Júpiter é o maior planeta do nosso Sistema Solar e o quinto a partir do Sol. É um gigante gasoso com uma massa 1/1000 da do Sol, mas é mais pesado que todos os outros planetas juntos. Civilizações antigas já conheciam Júpiter há muito tempo, e ele é facilmente visível no céu noturno. |
| 1              | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia maior que a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e é conhecido pelas civilizações antigas desde antes da história registrada. <br/>**Resuma Isto** <br/> O que aprendemos é que Júpiter | é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia maior que a de todos os outros planetas juntos. É facilmente visível a olho nu e é conhecido desde os tempos antigos.                        |
| 2              | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia maior que a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e é conhecido pelas civilizações antigas desde antes da história registrada. <br/>**Resuma Isto** <br/> Os 3 principais factos que aprendemos:         | 1. Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. <br/> 2. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol...<br/> 3. Júpiter é visível a olho nu desde os tempos antigos ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Modelos de Prompt

Um modelo de prompt é uma _receita pré-definida para um prompt_ que pode ser armazenada e reutilizada conforme necessário, para proporcionar experiências de utilizador mais consistentes em larga escala. Na sua forma mais simples, é apenas uma coleção de exemplos de prompts como [este da OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) que fornece tanto os componentes interativos do prompt (mensagens do utilizador e do sistema) quanto o formato de solicitação via API - para suportar a reutilização.

Na sua forma mais complexa, como [este exemplo da LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), contém _espaços reservados_ que podem ser substituídos por dados de várias fontes (entrada do utilizador, contexto do sistema, fontes de dados externas, etc.) para gerar um prompt dinamicamente. Isso permite criar uma biblioteca de prompts reutilizáveis que podem ser usados para proporcionar experiências de utilizador consistentes **programaticamente** em larga escala.

Finalmente, o verdadeiro valor dos modelos reside na capacidade de criar e publicar _bibliotecas de prompts_ para domínios de aplicação específicos - onde o modelo de prompt é agora _otimizado_ para refletir contextos ou exemplos específicos da aplicação, tornando as respostas mais relevantes e precisas para o público-alvo. O repositório [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) é um ótimo exemplo dessa abordagem, ao curar uma biblioteca de prompts para o domínio da educação com ênfase em objetivos-chave como planeamento de aulas, design curricular, tutoria de estudantes, etc.

## Conteúdo de Apoio

Se pensarmos na construção de prompts como tendo uma instrução (tarefa) e um alvo (conteúdo principal), então o _conteúdo secundário_ é como um contexto adicional que fornecemos para **influenciar a saída de alguma forma**. Pode incluir parâmetros de ajuste, instruções de formatação, taxonomias de tópicos, etc., que ajudam o modelo a _personalizar_ sua resposta para atender aos objetivos ou expectativas do utilizador.

Por exemplo: Dado um catálogo de cursos com metadados extensivos (nome, descrição, nível, etiquetas de metadados, instrutor, etc.) sobre todos os cursos disponíveis no currículo:

- podemos definir uma instrução para "resumir o catálogo de cursos para o Outono de 2023"
- podemos usar o conteúdo principal para fornecer alguns exemplos do formato desejado para a saída
- podemos usar o conteúdo secundário para identificar as 5 principais "etiquetas" de interesse.

Agora, o modelo pode fornecer um resumo no formato mostrado pelos exemplos fornecidos - mas se um resultado tiver várias etiquetas, pode priorizar as 5 etiquetas identificadas no conteúdo secundário.

---

<!--
MODELO DE LIÇÃO:
Esta unidade deve abordar o conceito principal #1.
Reforce o conceito com exemplos e referências.

CONCEITO #3:
Técnicas de Engenharia de Prompt.
Quais são algumas técnicas básicas de engenharia de prompt?
Ilustre com alguns exercícios.
-->

## Melhores Práticas de Prompting

Agora que sabemos como os prompts podem ser _construídos_, podemos começar a pensar em como _desenhá-los_ para refletir as melhores práticas. Podemos pensar nisso em duas partes - ter a _mentalidade_ certa e aplicar as _técnicas_ certas.

### Mentalidade de Engenharia de Prompt

A Engenharia de Prompt é um processo de tentativa e erro, então mantenha três fatores orientadores amplos em mente:

1. **Compreensão do Domínio é Importante.** A precisão e relevância da resposta são uma função do _domínio_ em que essa aplicação ou utilizador opera. Aplique sua intuição e experiência no domínio para **personalizar técnicas** ainda mais. Por exemplo, defina _personalidades específicas do domínio_ nos seus prompts de sistema ou use _modelos específicos do domínio_ nos seus prompts de utilizador. Forneça conteúdo secundário que reflita contextos específicos do domínio ou use _pistas e exemplos específicos do domínio_ para guiar o modelo em padrões de uso familiares.

2. **Compreensão do Modelo é Importante.** Sabemos que os modelos são estocásticos por natureza. Mas as implementações de modelos também podem variar em termos do conjunto de dados de treino que utilizam (conhecimento pré-treinado), as capacidades que fornecem (por exemplo, via API ou SDK) e o tipo de conteúdo para o qual são otimizados (por exemplo, código vs. imagens vs. texto). Compreenda os pontos fortes e as limitações do modelo que está a usar e utilize esse conhecimento para _priorizar tarefas_ ou construir _modelos personalizados_ otimizados para as capacidades do modelo.

3. **Iteração e Validação são Importantes.** Os modelos estão a evoluir rapidamente, e o mesmo acontece com as técnicas de engenharia de prompt. Como especialista no domínio, pode ter outros contextos ou critérios específicos da sua aplicação que podem não se aplicar à comunidade em geral. Use ferramentas e técnicas de engenharia de prompt para "dar o pontapé inicial" na construção de prompts, depois itere e valide os resultados usando sua própria intuição e experiência no domínio. Registe os seus insights e crie uma **base de conhecimento** (por exemplo, bibliotecas de prompts) que podem ser usadas como um novo ponto de partida por outros, para iterações mais rápidas no futuro.

## Melhores Práticas

Agora vamos olhar para as melhores práticas comuns recomendadas pelos profissionais da [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e da [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| O quê                             | Porquê                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Avalie os modelos mais recentes.  | As novas gerações de modelos provavelmente terão recursos e qualidade aprimorados - mas também podem acarretar custos mais elevados. Avalie o impacto e tome decisões de migração.                                                                  |
| Separe instruções e contexto      | Verifique se o seu modelo/provedor define _delimitadores_ para distinguir instruções, conteúdo principal e secundário de forma mais clara. Isso pode ajudar os modelos a atribuir pesos mais precisos aos tokens.                                   |
| Seja específico e claro           | Dê mais detalhes sobre o contexto desejado, resultado, comprimento, formato, estilo, etc. Isso melhorará tanto a qualidade quanto a consistência das respostas. Capture receitas em modelos reutilizáveis.                                         |
| Seja descritivo, use exemplos     | Os modelos podem responder melhor a uma abordagem de "mostrar e contar". Comece com uma abordagem `zero-shot`, onde dá uma instrução (mas sem exemplos), depois experimente `few-shot` como refinamento, fornecendo alguns exemplos do resultado desejado. Use analogias. |
| Use pistas para iniciar respostas | Direcione o modelo para um resultado desejado dando-lhe algumas palavras ou frases iniciais que ele pode usar como ponto de partida para a resposta.                                                                                               |
| Reforce                           | Às vezes, pode ser necessário repetir-se para o modelo. Dê instruções antes e depois do conteúdo principal, use uma instrução e uma pista, etc. Itere e valide para ver o que funciona.                                                           |
| A ordem importa                   | A ordem em que apresenta as informações ao modelo pode impactar a saída, mesmo nos exemplos de aprendizagem, devido ao viés de recência. Experimente diferentes opções para ver o que funciona melhor.                                               |
| Dê ao modelo uma "saída"          | Dê ao modelo uma resposta de _reserva_ que ele pode fornecer se não conseguir completar a tarefa por algum motivo. Isso pode reduzir as chances de o modelo gerar respostas falsas ou fabricadas.                                                  |
|                                   |                                                                                                                                                                                                                                                   |

Como em qualquer melhor prática, lembre-se de que _os resultados podem variar_ dependendo do modelo, da tarefa e do domínio. Use estas práticas como ponto de partida e itere para descobrir o que funciona melhor para si. Reavalie constantemente o seu processo de engenharia de prompt à medida que novos modelos e ferramentas se tornam disponíveis, com foco na escalabilidade do processo e na qualidade das respostas.

<!--
MODELO DE LIÇÃO:
Esta unidade deve fornecer um desafio de código, se aplicável.

DESAFIO:
Link para um Jupyter Notebook com apenas os comentários de código nas instruções (as seções de código estão vazias).

SOLUÇÃO:
Link para uma cópia desse Notebook com os prompts preenchidos e executados, mostrando um exemplo de como poderia ser.
-->

## Tarefa

Parabéns! Chegou ao fim da lição! É hora de colocar alguns desses conceitos e técnicas à prova com exemplos reais!

Para a nossa tarefa, usaremos um Jupyter Notebook com exercícios que pode completar interativamente. Também pode expandir o Notebook com suas próprias células de Markdown e Código para explorar ideias e técnicas por conta própria.

### Para começar, faça um fork do repositório e, em seguida:

- (Recomendado) Inicie o GitHub Codespaces
- (Alternativamente) Clone o repositório para o seu dispositivo local e use-o com o Docker Desktop
- (Alternativamente) Abra o Notebook com o seu ambiente de execução de Notebook preferido.

### Em seguida, configure as variáveis de ambiente

- Copie o ficheiro `.env.copy` na raiz do repositório para `.env` e preencha os valores de `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT`. Volte à [secção Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) para saber como.

### Depois, abra o Jupyter Notebook

- Selecione o kernel de execução. Se estiver a usar as opções 1 ou 2, basta selecionar o kernel padrão Python 3.10.x fornecido pelo contêiner de desenvolvimento.

Está tudo pronto para executar os exercícios. Note que não há respostas _certas ou erradas_ aqui - apenas explorar opções por tentativa e erro e construir intuição sobre o que funciona para um determinado modelo e domínio de aplicação.

_Por essa razão, não há segmentos de Soluções de Código nesta lição. Em vez disso, o Notebook terá células de Markdown intituladas "Minha Solução:" que mostram um exemplo de saída para referência._

 <!--
MODELO DE LIÇÃO:
Encerre a secção com um resumo e recursos para aprendizagem autodirigida.
-->

## Verificação de Conhecimento

Qual das seguintes opções é um bom prompt seguindo algumas práticas recomendadas razoáveis?

1. Mostre-me uma imagem de um carro vermelho
2. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90 estacionado junto a um penhasco com o sol a pôr-se
3. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90

R: 2, é o melhor prompt, pois fornece detalhes sobre "o quê" e entra em especificidades (não apenas qualquer carro, mas uma marca e modelo específicos) e também descreve o cenário geral. 3 é o próximo melhor, pois também contém muitas descrições.

## 🚀 Desafio

Veja se consegue aproveitar a técnica de "pista" com o prompt: Complete a frase "Mostre-me uma imagem de um carro vermelho da marca Volvo e ". O que ele responde e como melhoraria isso?

## Excelente Trabalho! Continue a Aprender

Quer saber mais sobre diferentes conceitos de Engenharia de Prompt? Vá para a [página de aprendizagem contínua](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre este tema.

Siga para a Lição 5, onde vamos explorar [técnicas avançadas de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.