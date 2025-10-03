<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b3cb38518cf4fe7714d2f5e74dfa3eb",
  "translation_date": "2025-10-03T09:10:00+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "pt"
}
-->
# Fundamentos de Engenharia de Prompts

[![Fundamentos de Engenharia de Prompts](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.pt.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Introdução
Este módulo aborda conceitos e técnicas essenciais para criar prompts eficazes em modelos de IA generativa. A forma como escreves o teu prompt para um LLM também é importante. Um prompt cuidadosamente elaborado pode alcançar uma melhor qualidade de resposta. Mas o que exatamente significam termos como _prompt_ e _engenharia de prompts_? E como posso melhorar o _input_ do prompt que envio para o LLM? Estas são as perguntas que tentaremos responder neste capítulo e no próximo.

A _IA generativa_ é capaz de criar novos conteúdos (por exemplo, texto, imagens, áudio, código, etc.) em resposta a pedidos dos utilizadores. Consegue isso utilizando _Modelos de Linguagem de Grande Escala_ como a série GPT ("Generative Pre-trained Transformer") da OpenAI, que são treinados para usar linguagem natural e código.

Os utilizadores podem agora interagir com estes modelos utilizando paradigmas familiares, como chat, sem necessidade de conhecimentos técnicos ou formação. Os modelos são baseados em _prompts_ - os utilizadores enviam um input de texto (prompt) e recebem a resposta da IA (completação). Podem então "conversar com a IA" de forma iterativa, em conversas de múltiplas interações, refinando o prompt até que a resposta corresponda às suas expectativas.

Os "prompts" tornam-se agora a principal _interface de programação_ para aplicações de IA generativa, dizendo aos modelos o que fazer e influenciando a qualidade das respostas retornadas. A "Engenharia de Prompts" é um campo de estudo em rápido crescimento que se concentra no _design e otimização_ de prompts para fornecer respostas consistentes e de qualidade em escala.

## Objetivos de Aprendizagem

Nesta lição, aprendemos o que é Engenharia de Prompts, por que é importante e como podemos criar prompts mais eficazes para um modelo e objetivo de aplicação específicos. Vamos compreender os conceitos principais e as melhores práticas para engenharia de prompts - e aprender sobre um ambiente interativo de "sandbox" em Jupyter Notebooks onde podemos ver esses conceitos aplicados a exemplos reais.

No final desta lição, seremos capazes de:

1. Explicar o que é engenharia de prompts e por que é importante.
2. Descrever os componentes de um prompt e como são utilizados.
3. Aprender melhores práticas e técnicas para engenharia de prompts.
4. Aplicar as técnicas aprendidas a exemplos reais, utilizando um endpoint da OpenAI.

## Termos-Chave

Engenharia de Prompts: A prática de projetar e refinar inputs para orientar modelos de IA a produzir os resultados desejados.  
Tokenização: O processo de converter texto em unidades menores, chamadas tokens, que um modelo pode entender e processar.  
LLMs Ajustados por Instruções: Modelos de Linguagem de Grande Escala (LLMs) que foram ajustados com instruções específicas para melhorar a precisão e relevância das respostas.

## Sandbox de Aprendizagem

A engenharia de prompts é atualmente mais arte do que ciência. A melhor forma de melhorar a nossa intuição sobre isso é _praticar mais_ e adotar uma abordagem de tentativa e erro que combine expertise no domínio da aplicação com técnicas recomendadas e otimizações específicas do modelo.

O Jupyter Notebook que acompanha esta lição fornece um ambiente de _sandbox_ onde podes experimentar o que aprendes - à medida que avanças ou como parte do desafio de código no final. Para executar os exercícios, vais precisar de:

1. **Uma chave de API do Azure OpenAI** - o endpoint de serviço para um LLM implementado.  
2. **Um Runtime Python** - no qual o Notebook pode ser executado.  
3. **Variáveis de Ambiente Locais** - _completa os passos de [CONFIGURAÇÃO](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) agora para te preparares_.  

O notebook vem com exercícios _iniciais_ - mas és encorajado a adicionar as tuas próprias seções de _Markdown_ (descrição) e _Código_ (pedidos de prompt) para experimentar mais exemplos ou ideias - e construir a tua intuição para design de prompts.

## Guia Ilustrado

Queres ter uma visão geral do que esta lição cobre antes de mergulhares? Consulta este guia ilustrado, que te dá uma ideia dos principais tópicos abordados e os pontos-chave para refletires em cada um. O roteiro da lição leva-te desde a compreensão dos conceitos e desafios principais até abordá-los com técnicas relevantes de engenharia de prompts e melhores práticas. Nota que a seção "Técnicas Avançadas" neste guia refere-se ao conteúdo abordado no _próximo_ capítulo deste currículo.

![Guia Ilustrado para Engenharia de Prompts](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.pt.png)

## A Nossa Startup

Agora, vamos falar sobre como _este tópico_ se relaciona com a nossa missão de startup de [trazer inovação em IA para a educação](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicações de aprendizagem personalizada alimentadas por IA - então vamos pensar em como diferentes utilizadores da nossa aplicação podem "projetar" prompts:

- **Administradores** podem pedir à IA para _analisar dados curriculares e identificar lacunas na cobertura_. A IA pode resumir os resultados ou visualizá-los com código.  
- **Educadores** podem pedir à IA para _gerar um plano de aula para um público-alvo e tópico específico_. A IA pode criar o plano personalizado num formato especificado.  
- **Estudantes** podem pedir à IA para _tutorar-lhes numa matéria difícil_. A IA pode agora orientar os estudantes com lições, dicas e exemplos adaptados ao seu nível.  

Isso é apenas a ponta do iceberg. Consulta [Prompts Para Educação](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - uma biblioteca de prompts open-source curada por especialistas em educação - para ter uma ideia mais ampla das possibilidades! _Experimenta executar alguns desses prompts no sandbox ou no OpenAI Playground para ver o que acontece!_

## O que é Engenharia de Prompts?

Começámos esta lição definindo **Engenharia de Prompts** como o processo de _projetar e otimizar_ inputs de texto (prompts) para fornecer respostas consistentes e de qualidade (completações) para um objetivo de aplicação e modelo específicos. Podemos pensar nisso como um processo de 2 etapas:

- _projetar_ o prompt inicial para um modelo e objetivo específicos  
- _refinar_ o prompt de forma iterativa para melhorar a qualidade da resposta  

Este é necessariamente um processo de tentativa e erro que requer intuição e esforço do utilizador para obter resultados ótimos. Então, por que é importante? Para responder a essa pergunta, primeiro precisamos entender três conceitos:

- _Tokenização_ = como o modelo "vê" o prompt  
- _LLMs Base_ = como o modelo base "processa" um prompt  
- _LLMs Ajustados por Instruções_ = como o modelo pode agora ver "tarefas"  

### Tokenização

Um LLM vê prompts como uma _sequência de tokens_, onde diferentes modelos (ou versões de um modelo) podem tokenizar o mesmo prompt de maneiras diferentes. Como os LLMs são treinados em tokens (e não em texto bruto), a forma como os prompts são tokenizados tem um impacto direto na qualidade da resposta gerada.

Para ter uma intuição de como a tokenização funciona, experimenta ferramentas como o [Tokenizador da OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abaixo. Copia o teu prompt - e vê como ele é convertido em tokens, prestando atenção em como os caracteres de espaço e os sinais de pontuação são tratados. Nota que este exemplo mostra um LLM mais antigo (GPT-3) - então experimentar isso com um modelo mais recente pode produzir um resultado diferente.

![Tokenização](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.pt.png)

### Conceito: Modelos Base

Uma vez que um prompt é tokenizado, a função principal do ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modelo base) é prever o próximo token nessa sequência. Como os LLMs são treinados em conjuntos de dados massivos de texto, eles têm uma boa noção das relações estatísticas entre tokens e podem fazer essa previsão com alguma confiança. Nota que eles não entendem o _significado_ das palavras no prompt ou token; eles apenas veem um padrão que podem "completar" com a sua próxima previsão. Eles podem continuar prevendo a sequência até serem interrompidos por intervenção do utilizador ou alguma condição pré-estabelecida.

Queres ver como funciona a completação baseada em prompts? Insere o prompt acima no [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) do Azure OpenAI Studio com as configurações padrão. O sistema está configurado para tratar prompts como pedidos de informação - então deverás ver uma completação que satisfaça este contexto.

Mas e se o utilizador quisesse ver algo específico que atendesse a alguns critérios ou objetivos de tarefa? É aqui que os LLMs _ajustados por instruções_ entram em cena.

![Completação de Chat com LLM Base](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.pt.png)

### Conceito: LLMs Ajustados por Instruções

Um [LLM Ajustado por Instruções](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) começa com o modelo base e ajusta-o com exemplos ou pares de input/output (por exemplo, "mensagens" de múltiplas interações) que podem conter instruções claras - e a resposta da IA tenta seguir essa instrução.

Isso utiliza técnicas como Aprendizagem por Reforço com Feedback Humano (RLHF) que podem treinar o modelo para _seguir instruções_ e _aprender com feedback_, de modo que produza respostas mais adequadas a aplicações práticas e mais relevantes para os objetivos do utilizador.

Vamos experimentar - revisita o prompt acima, mas agora altera a _mensagem do sistema_ para fornecer a seguinte instrução como contexto:

> _Resume o conteúdo que te é fornecido para um aluno do segundo ano. Mantém o resultado em um parágrafo com 3-5 pontos principais._

Vê como o resultado agora está ajustado para refletir o objetivo e formato desejados? Um educador pode agora usar diretamente esta resposta nos seus slides para essa aula.

![Completação de Chat com LLM Ajustado por Instruções](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.pt.png)

## Por que precisamos de Engenharia de Prompts?

Agora que sabemos como os prompts são processados pelos LLMs, vamos falar sobre _por que_ precisamos de engenharia de prompts. A resposta está no fato de que os LLMs atuais apresentam vários desafios que tornam _completações confiáveis e consistentes_ mais difíceis de alcançar sem esforço na construção e otimização de prompts. Por exemplo:

1. **As respostas dos modelos são estocásticas.** O _mesmo prompt_ provavelmente produzirá respostas diferentes com diferentes modelos ou versões de modelos. E pode até produzir resultados diferentes com o _mesmo modelo_ em momentos diferentes. _As técnicas de engenharia de prompts podem ajudar-nos a minimizar essas variações fornecendo melhores limites_.  

2. **Os modelos podem fabricar respostas.** Os modelos são pré-treinados com _conjuntos de dados grandes, mas finitos_, o que significa que eles não têm conhecimento sobre conceitos fora desse escopo de treino. Como resultado, podem produzir completações que são imprecisas, imaginárias ou diretamente contraditórias a fatos conhecidos. _As técnicas de engenharia de prompts ajudam os utilizadores a identificar e mitigar essas fabricações, por exemplo, pedindo à IA citações ou raciocínio_.  

3. **As capacidades dos modelos variam.** Modelos mais recentes ou gerações de modelos terão capacidades mais ricas, mas também trazem peculiaridades únicas e compensações em custo e complexidade. _A engenharia de prompts pode ajudar-nos a desenvolver melhores práticas e fluxos de trabalho que abstraem diferenças e se adaptam a requisitos específicos de modelos de forma escalável e contínua_.  

Vamos ver isso em ação no OpenAI ou Azure OpenAI Playground:

- Usa o mesmo prompt com diferentes implementações de LLM (por exemplo, OpenAI, Azure OpenAI, Hugging Face) - viste as variações?  
- Usa o mesmo prompt repetidamente com a _mesma_ implementação de LLM (por exemplo, playground do Azure OpenAI) - como essas variações diferiram?  

### Exemplo de Fabricações

Neste curso, usamos o termo **"fabricação"** para referenciar o fenómeno em que os LLMs às vezes geram informações factualmente incorretas devido a limitações no seu treino ou outras restrições. Também podes ter ouvido isso referido como _"alucinações"_ em artigos populares ou trabalhos de pesquisa. No entanto, recomendamos fortemente usar o termo _"fabricação"_ para que não antropomorfizemos o comportamento ao atribuir uma característica humana a um resultado gerado por máquina. Isso também reforça as [diretrizes de IA Responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) do ponto de vista da terminologia, removendo termos que podem ser considerados ofensivos ou não inclusivos em alguns contextos.

Queres ter uma ideia de como funcionam as fabricações? Pensa num prompt que instrua a IA a gerar conteúdo para um tópico inexistente (para garantir que não seja encontrado no conjunto de dados de treino). Por exemplo - experimentei este prompt:

> **Prompt:** gera um plano de aula sobre a Guerra Marciana de 2076.
Uma pesquisa na web mostrou-me que existem relatos fictícios (por exemplo, séries de televisão ou livros) sobre guerras em Marte - mas nenhum em 2076. O senso comum também nos diz que 2076 está _no futuro_ e, portanto, não pode estar associado a um evento real.

Então, o que acontece quando executamos este prompt com diferentes fornecedores de LLM?

> **Resposta 1**: OpenAI Playground (GPT-35)

![Resposta 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.pt.png)

> **Resposta 2**: Azure OpenAI Playground (GPT-35)

![Resposta 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.pt.png)

> **Resposta 3**: Hugging Face Chat Playground (LLama-2)

![Resposta 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.pt.png)

Como esperado, cada modelo (ou versão de modelo) produz respostas ligeiramente diferentes devido ao comportamento estocástico e às variações de capacidade do modelo. Por exemplo, um modelo direciona-se a um público de 8º ano, enquanto outro assume um estudante do ensino secundário. Mas todos os três modelos geraram respostas que poderiam convencer um utilizador desinformado de que o evento era real.

Técnicas de engenharia de prompts, como _metaprompting_ e _configuração de temperatura_, podem reduzir as fabricações do modelo até certo ponto. Novas _arquiteturas_ de engenharia de prompts também incorporam novas ferramentas e técnicas de forma integrada no fluxo de prompts, para mitigar ou reduzir alguns desses efeitos.

## Caso de Estudo: GitHub Copilot

Vamos encerrar esta secção compreendendo como a engenharia de prompts é utilizada em soluções reais, analisando um caso de estudo: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

O GitHub Copilot é o seu "Programador Parceiro de IA" - converte prompts de texto em sugestões de código e está integrado no seu ambiente de desenvolvimento (por exemplo, Visual Studio Code) para uma experiência de utilizador fluida. Conforme documentado na série de blogs abaixo, a versão inicial baseava-se no modelo OpenAI Codex - com os engenheiros rapidamente percebendo a necessidade de ajustar o modelo e desenvolver melhores técnicas de engenharia de prompts para melhorar a qualidade do código. Em julho, [estrearam um modelo de IA melhorado que vai além do Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugestões ainda mais rápidas.

Leia os posts na ordem indicada para acompanhar a jornada de aprendizagem deles.

- **Maio 2023** | [GitHub Copilot está a melhorar na compreensão do seu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maio 2023** | [Por dentro do GitHub: Trabalhando com os LLMs por trás do GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junho 2023** | [Como escrever melhores prompts para o GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julho 2023** | [.. GitHub Copilot vai além do Codex com um modelo de IA melhorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julho 2023** | [Guia do Desenvolvedor para Engenharia de Prompts e LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Setembro 2023** | [Como construir uma aplicação empresarial com LLM: Lições do GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Também pode explorar o [blog de engenharia deles](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para mais posts como [este](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), que mostra como esses modelos e técnicas são _aplicados_ para impulsionar aplicações reais.

---

## Construção de Prompts

Já vimos porque a engenharia de prompts é importante - agora vamos entender como os prompts são _construídos_ para que possamos avaliar diferentes técnicas para um design de prompts mais eficaz.

### Prompt Básico

Comecemos com o prompt básico: uma entrada de texto enviada ao modelo sem qualquer outro contexto. Aqui está um exemplo - quando enviamos as primeiras palavras do hino nacional dos EUA para a [API Completion da OpenAI](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), ela completa instantaneamente a resposta com as próximas linhas, ilustrando o comportamento básico de previsão.

| Prompt (Entrada) | Conclusão (Saída)                                                                                                                        |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Parece que está a começar a letra de "The Star-Spangled Banner", o hino nacional dos Estados Unidos. A letra completa é ...             |

### Prompt Complexo

Agora vamos adicionar contexto e instruções ao prompt básico. A [API Chat Completion](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) permite-nos construir um prompt complexo como uma coleção de _mensagens_ com:

- Pares de entrada/saída refletindo a entrada do _utilizador_ e a resposta do _assistente_.
- Mensagem do sistema definindo o contexto para o comportamento ou personalidade do assistente.

A solicitação agora tem o formato abaixo, onde a _tokenização_ captura efetivamente informações relevantes do contexto e da conversa. Alterar o contexto do sistema pode ser tão impactante na qualidade das conclusões quanto as entradas fornecidas pelo utilizador.

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

Nos exemplos acima, o prompt do utilizador era uma consulta de texto simples que pode ser interpretada como um pedido de informação. Com prompts de _instrução_, podemos usar esse texto para especificar uma tarefa com mais detalhes, fornecendo uma orientação melhor à IA. Aqui está um exemplo:

| Prompt (Entrada)                                                                                                                                                                                                                         | Conclusão (Saída)                                                                                                        | Tipo de Instrução   |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Escreva uma descrição da Guerra Civil                                                                                                                                                                                                   | _retornou um parágrafo simples_                                                                                         | Simples             |
| Escreva uma descrição da Guerra Civil. Forneça datas e eventos importantes e descreva a sua relevância                                                                                                                                  | _retornou um parágrafo seguido por uma lista de datas de eventos importantes com descrições_                            | Complexo            |
| Escreva uma descrição da Guerra Civil em 1 parágrafo. Forneça 3 pontos com datas importantes e a sua relevância. Forneça mais 3 pontos com figuras históricas importantes e as suas contribuições. Retorne o resultado como um ficheiro JSON | _retornou detalhes mais extensos numa caixa de texto, formatados como JSON que pode copiar-colar num ficheiro e validar conforme necessário_ | Complexo. Formatado.|

## Conteúdo Principal

Nos exemplos acima, o prompt ainda era bastante aberto, permitindo ao LLM decidir qual parte do seu conjunto de dados pré-treinado era relevante. Com o padrão de design de _conteúdo principal_, o texto de entrada é dividido em duas partes:

- uma instrução (ação)
- conteúdo relevante (que influencia a ação)

Aqui está um exemplo onde a instrução é "resuma isto em 2 frases".

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Conclusão (Saída)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa mil vezes menor que a do Sol, mas duas vezes e meia maior que a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e é conhecido pelas civilizações antigas desde antes da história registrada. É nomeado em homenagem ao deus romano Júpiter.[19] Quando visto da Terra, Júpiter pode ser brilhante o suficiente para que sua luz refletida projete sombras visíveis,[20] e é, em média, o terceiro objeto natural mais brilhante no céu noturno depois da Lua e de Vénus. <br/> **Resuma isto em 2 frases curtas** | Júpiter, o quinto planeta a partir do Sol, é o maior do Sistema Solar e é conhecido por ser um dos objetos mais brilhantes no céu noturno. Nomeado em homenagem ao deus romano Júpiter, é um gigante gasoso cuja massa é duas vezes e meia maior que a de todos os outros planetas do Sistema Solar juntos. |

O segmento de conteúdo principal pode ser usado de várias formas para impulsionar instruções mais eficazes:

- **Exemplos** - em vez de dizer ao modelo o que fazer com uma instrução explícita, forneça exemplos do que fazer e deixe-o inferir o padrão.
- **Dicas** - siga a instrução com uma "dica" que prepara a conclusão, orientando o modelo para respostas mais relevantes.
- **Templates** - são 'receitas' repetíveis para prompts com espaços reservados (variáveis) que podem ser personalizados com dados para casos de uso específicos.

Vamos explorar estas abordagens em ação.

### Usando Exemplos

Esta é uma abordagem onde se utiliza o conteúdo principal para "alimentar o modelo" com alguns exemplos do resultado desejado para uma determinada instrução e deixá-lo inferir o padrão para o resultado desejado. Com base no número de exemplos fornecidos, podemos ter prompts zero-shot, one-shot, few-shot, etc.

O prompt agora consiste em três componentes:

- Uma descrição da tarefa
- Alguns exemplos do resultado desejado
- O início de um novo exemplo (que se torna uma descrição implícita da tarefa)

| Tipo de Aprendizagem | Prompt (Entrada)                                                                                                                                        | Conclusão (Saída)         |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------ |
| Zero-shot            | "O Sol está a brilhar". Traduza para espanhol                                                                                                          | "El Sol está brillando".  |
| One-shot             | "O Sol está a brilhar" => ""El Sol está brillando". <br> "Está um dia frio e ventoso" =>                                                               | "Es un día frío y ventoso". |
| Few-shot             | O jogador correu as bases => Basebol <br/> O jogador fez um ace => Ténis <br/> O jogador fez um seis => Críquete <br/> O jogador fez um afundanço =>   | Basquetebol              |
|                      |                                                                                                                                                       |                           |

Repare como tivemos de fornecer uma instrução explícita ("Traduza para espanhol") no exemplo zero-shot, mas ela é inferida no exemplo one-shot. O exemplo few-shot mostra como adicionar mais exemplos permite que os modelos façam inferências mais precisas sem instruções adicionais.

### Dicas no Prompt

Outra técnica para usar o conteúdo principal é fornecer _dicas_ em vez de exemplos. Neste caso, estamos a dar ao modelo um empurrão na direção certa ao _iniciar_ com um trecho que reflete o formato de resposta desejado. O modelo então "segue a dica" para continuar nesse estilo.

| Número de Dicas | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Conclusão (Saída)                                                                                                                                                                                                                                                                                       |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0               | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa mil vezes menor que a do Sol, mas duas vezes e meia maior que a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e é conhecido pelas civilizações antigas desde antes da história registrada. <br/>**Resuma Isto**                                       | Júpiter é o maior planeta do nosso Sistema Solar e o quinto a partir do Sol. É um gigante gasoso com uma massa 1/1000 da do Sol, mas é mais pesado que todos os outros planetas juntos. Civilizações antigas conhecem Júpiter há muito tempo, e ele é facilmente visível no céu noturno. |
| 1              | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e é conhecido pelas civilizações antigas desde antes da história registrada. <br/>**Resumir Isto** <br/> O que aprendemos é que Júpiter | é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas juntos. É facilmente visível a olho nu e conhecido desde os tempos antigos.                        |
| 2              | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno e é conhecido pelas civilizações antigas desde antes da história registrada. <br/>**Resumir Isto** <br/> Top 3 Factos que Aprendemos:         | 1. Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. <br/> 2. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol...<br/> 3. Júpiter é visível a olho nu desde os tempos antigos ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Modelos de Templates de Prompt

Um template de prompt é uma _receita pré-definida para um prompt_ que pode ser armazenada e reutilizada conforme necessário, para proporcionar experiências de utilizador mais consistentes em escala. Na sua forma mais simples, é apenas uma coleção de exemplos de prompts como [este da OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) que fornece tanto os componentes interativos do prompt (mensagens do utilizador e do sistema) quanto o formato de solicitação orientado por API - para suportar reutilização.

Na sua forma mais complexa, como [este exemplo da LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), contém _espaços reservados_ que podem ser substituídos por dados de várias fontes (entrada do utilizador, contexto do sistema, fontes de dados externas, etc.) para gerar um prompt dinamicamente. Isto permite criar uma biblioteca de prompts reutilizáveis que podem ser usados para proporcionar experiências de utilizador consistentes **programaticamente** em escala.

Finalmente, o verdadeiro valor dos templates reside na capacidade de criar e publicar _bibliotecas de prompts_ para domínios de aplicação vertical - onde o template de prompt é agora _otimizado_ para refletir o contexto ou exemplos específicos da aplicação, tornando as respostas mais relevantes e precisas para o público-alvo. O repositório [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) é um ótimo exemplo desta abordagem, curando uma biblioteca de prompts para o domínio da educação com ênfase em objetivos-chave como planeamento de aulas, design curricular, tutoria de estudantes, etc.

## Conteúdo de Apoio

Se pensarmos na construção de prompts como tendo uma instrução (tarefa) e um alvo (conteúdo principal), então o _conteúdo secundário_ é como um contexto adicional que fornecemos para **influenciar a saída de alguma forma**. Pode ser parâmetros de ajuste, instruções de formatação, taxonomias de tópicos, etc., que ajudam o modelo a _personalizar_ a sua resposta para atender aos objetivos ou expectativas do utilizador.

Por exemplo: Dado um catálogo de cursos com metadados extensivos (nome, descrição, nível, etiquetas de metadados, instrutor, etc.) sobre todos os cursos disponíveis no currículo:

- podemos definir uma instrução para "resumir o catálogo de cursos para o Outono de 2023"
- podemos usar o conteúdo principal para fornecer alguns exemplos do formato desejado
- podemos usar o conteúdo secundário para identificar as 5 principais "etiquetas" de interesse.

Agora, o modelo pode fornecer um resumo no formato mostrado pelos exemplos fornecidos - mas se um resultado tiver várias etiquetas, pode priorizar as 5 etiquetas identificadas no conteúdo secundário.

---

<!--
TEMPLATE DE LIÇÃO:
Esta unidade deve cobrir o conceito principal #1.
Reforce o conceito com exemplos e referências.

CONCEITO #3:
Técnicas de Engenharia de Prompt.
Quais são algumas técnicas básicas para engenharia de prompt?
Ilustre com alguns exercícios.
-->

## Melhores Práticas de Prompting

Agora que sabemos como os prompts podem ser _construídos_, podemos começar a pensar em como _desenhá-los_ para refletir as melhores práticas. Podemos pensar nisso em duas partes - ter a _mentalidade_ certa e aplicar as _técnicas_ certas.

### Mentalidade de Engenharia de Prompt

A Engenharia de Prompt é um processo de tentativa e erro, por isso mantenha três fatores amplos em mente:

1. **Compreensão do Domínio é Importante.** A precisão e relevância da resposta são uma função do _domínio_ em que essa aplicação ou utilizador opera. Aplique a sua intuição e experiência no domínio para **personalizar técnicas** ainda mais. Por exemplo, defina _personalidades específicas do domínio_ nos seus prompts de sistema ou use _templates específicos do domínio_ nos seus prompts de utilizador. Forneça conteúdo secundário que reflita contextos específicos do domínio ou use _pistas e exemplos específicos do domínio_ para orientar o modelo em direção a padrões de uso familiares.

2. **Compreensão do Modelo é Importante.** Sabemos que os modelos são estocásticos por natureza. Mas as implementações de modelos também podem variar em termos do conjunto de dados de treino que utilizam (conhecimento pré-treinado), as capacidades que fornecem (por exemplo, via API ou SDK) e o tipo de conteúdo para o qual estão otimizados (por exemplo, código vs. imagens vs. texto). Compreenda os pontos fortes e limitações do modelo que está a usar e utilize esse conhecimento para _priorizar tarefas_ ou construir _templates personalizados_ otimizados para as capacidades do modelo.

3. **Iteração e Validação são Importantes.** Os modelos estão a evoluir rapidamente, assim como as técnicas de engenharia de prompt. Como especialista no domínio, pode ter outros contextos ou critérios específicos da sua aplicação que podem não se aplicar à comunidade em geral. Use ferramentas e técnicas de engenharia de prompt para "dar início" à construção de prompts, depois itere e valide os resultados usando a sua própria intuição e experiência no domínio. Registe os seus insights e crie uma **base de conhecimento** (por exemplo, bibliotecas de prompts) que pode ser usada como um novo ponto de partida por outros, para iterações mais rápidas no futuro.

## Melhores Práticas

Agora vamos analisar práticas recomendadas comuns que são recomendadas por [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e por profissionais da [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| O quê                              | Porquê                                                                                                                                                                                                                                               |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avaliar os modelos mais recentes.  | As novas gerações de modelos provavelmente terão recursos e qualidade melhorados - mas também podem incorrer em custos mais elevados. Avalie o impacto e tome decisões de migração.                                                                   |
| Separar instruções e contexto.     | Verifique se o seu modelo/provedor define _delimitadores_ para distinguir instruções, conteúdo principal e secundário mais claramente. Isso pode ajudar os modelos a atribuir pesos mais precisos aos tokens.                                         |
| Ser específico e claro.            | Dê mais detalhes sobre o contexto desejado, resultado, comprimento, formato, estilo, etc. Isso melhorará tanto a qualidade quanto a consistência das respostas. Capture receitas em templates reutilizáveis.                                         |
| Ser descritivo, usar exemplos.     | Os modelos podem responder melhor a uma abordagem de "mostrar e contar". Comece com uma abordagem `zero-shot`, onde dá uma instrução (mas sem exemplos), depois experimente `few-shot` como refinamento, fornecendo alguns exemplos do resultado desejado. Use analogias. |
| Usar pistas para iniciar respostas | Oriente o modelo em direção a um resultado desejado dando-lhe algumas palavras ou frases iniciais que ele pode usar como ponto de partida para a resposta.                                                                                           |
| Reforçar.                          | Às vezes, pode ser necessário repetir-se para o modelo. Dê instruções antes e depois do conteúdo principal, use uma instrução e uma pista, etc. Itere e valide para ver o que funciona.                                                             |
| A ordem importa.                   | A ordem em que apresenta informações ao modelo pode impactar a saída, mesmo nos exemplos de aprendizagem, devido ao viés de recência. Experimente diferentes opções para ver o que funciona melhor.                                                  |
| Dê ao modelo uma "saída".          | Dê ao modelo uma resposta de _fallback_ que ele pode fornecer se não conseguir completar a tarefa por qualquer motivo. Isso pode reduzir as chances de o modelo gerar respostas falsas ou fabricadas.                                                |
|                                   |                                                                                                                                                                                                                                                     |

Como em qualquer prática recomendada, lembre-se de que _os seus resultados podem variar_ dependendo do modelo, da tarefa e do domínio. Use estas práticas como ponto de partida e itere para descobrir o que funciona melhor para si. Reavalie constantemente o seu processo de engenharia de prompt à medida que novos modelos e ferramentas se tornam disponíveis, com foco na escalabilidade do processo e na qualidade das respostas.

<!--
TEMPLATE DE LIÇÃO:
Esta unidade deve fornecer um desafio de código, se aplicável.

DESAFIO:
Link para um Jupyter Notebook com apenas os comentários de código nas instruções (as secções de código estão vazias).

SOLUÇÃO:
Link para uma cópia desse Notebook com os prompts preenchidos e executados, mostrando um exemplo de solução.
-->

## Tarefa

Parabéns! Chegou ao fim da lição! É hora de colocar alguns desses conceitos e técnicas à prova com exemplos reais!

Para a nossa tarefa, usaremos um Jupyter Notebook com exercícios que pode completar interativamente. Também pode estender o Notebook com as suas próprias células de Markdown e Código para explorar ideias e técnicas por conta própria.

### Para começar, faça um fork do repositório e depois:

- (Recomendado) Inicie o GitHub Codespaces
- (Alternativamente) Clone o repositório para o seu dispositivo local e use-o com o Docker Desktop
- (Alternativamente) Abra o Notebook com o seu ambiente de execução de Notebook preferido.

### Em seguida, configure as suas variáveis de ambiente

- Copie o ficheiro `.env.copy` na raiz do repositório para `.env` e preencha os valores `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT`. Volte à [secção de Sandbox de Aprendizagem](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) para aprender como.

### Depois, abra o Jupyter Notebook

- Selecione o kernel de execução. Se estiver a usar as opções 1 ou 2, basta selecionar o kernel padrão Python 3.10.x fornecido pelo contêiner de desenvolvimento.

Está tudo pronto para executar os exercícios. Note que não há _respostas certas ou erradas_ aqui - apenas explorar opções por tentativa e erro e construir intuição sobre o que funciona para um determinado modelo e domínio de aplicação.

_Por esta razão, não há segmentos de Solução de Código nesta lição. Em vez disso, o Notebook terá células de Markdown intituladas "Minha Solução:" que mostram um exemplo de saída para referência._

 <!--
TEMPLATE DE LIÇÃO:
Envolva a secção com um resumo e recursos para aprendizagem autodirigida.
-->

## Verificação de Conhecimento

Qual das seguintes é um bom prompt seguindo algumas práticas recomendadas razoáveis?

1. Mostre-me uma imagem de um carro vermelho
2. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90 estacionado junto a um penhasco com o sol a pôr-se
3. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90

R: 2, é o melhor prompt, pois fornece detalhes sobre "o quê" e entra em especificidades (não apenas qualquer carro, mas uma marca e modelo específicos) e também descreve o cenário geral. 3 é o próximo melhor, pois também contém muita descrição.

## 🚀 Desafio

Veja se consegue aproveitar a técnica de "pista" com o prompt: Complete a frase "Mostre-me uma imagem de um carro vermelho da marca Volvo e ". O que ele responde e como melhoraria isso?

## Excelente Trabalho! Continue a Aprender

Quer aprender mais sobre diferentes conceitos de Engenharia de Prompt? Vá para a [página de aprendizagem contínua](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre este tópico.

Avance para a Lição 5, onde exploraremos [técnicas avançadas de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.