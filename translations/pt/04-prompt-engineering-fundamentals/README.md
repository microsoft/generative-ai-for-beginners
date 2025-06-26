<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:27:30+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "pt"
}
-->
# Fundamentos da Engenharia de Prompts

## Introdução
Este módulo aborda conceitos e técnicas essenciais para criar prompts eficazes em modelos de IA generativa. A forma como você escreve seu prompt para um LLM também importa. Um prompt cuidadosamente elaborado pode alcançar uma melhor qualidade de resposta. Mas o que exatamente significam termos como _prompt_ e _engenharia de prompts_? E como posso melhorar o _input_ do prompt que envio para o LLM? Estas são as perguntas que tentaremos responder neste capítulo e no próximo.

A _IA generativa_ é capaz de criar novo conteúdo (por exemplo, texto, imagens, áudio, código etc.) em resposta a solicitações dos usuários. Ela alcança isso usando _Modelos de Linguagem de Grande Escala_ como a série GPT ("Transformador Pré-treinado Generativo") da OpenAI, que são treinados para usar linguagem natural e código.

Os usuários agora podem interagir com esses modelos usando paradigmas familiares, como chat, sem precisar de qualquer conhecimento técnico ou treinamento. Os modelos são baseados em _prompts_ - os usuários enviam uma entrada de texto (prompt) e recebem de volta a resposta da IA (conclusão). Eles podem então "conversar com a IA" de forma iterativa, em conversas de múltiplas interações, refinando seu prompt até que a resposta corresponda às suas expectativas.

Os "prompts" agora se tornam a principal _interface de programação_ para aplicativos de IA generativa, dizendo aos modelos o que fazer e influenciando a qualidade das respostas retornadas. A "Engenharia de Prompts" é um campo de estudo em rápido crescimento que se concentra no _design e otimização_ de prompts para fornecer respostas consistentes e de qualidade em escala.

## Objetivos de Aprendizagem

Nesta lição, aprendemos o que é Engenharia de Prompts, por que ela importa e como podemos elaborar prompts mais eficazes para um determinado modelo e objetivo de aplicação. Vamos entender os conceitos centrais e as melhores práticas para a engenharia de prompts - e aprender sobre um ambiente interativo "sandbox" de Jupyter Notebooks onde podemos ver esses conceitos aplicados a exemplos reais.

Ao final desta lição, seremos capazes de:

1. Explicar o que é engenharia de prompts e por que ela importa.
2. Descrever os componentes de um prompt e como eles são usados.
3. Aprender melhores práticas e técnicas para engenharia de prompts.
4. Aplicar técnicas aprendidas a exemplos reais, usando um endpoint OpenAI.

## Termos Chave

Engenharia de Prompts: A prática de projetar e refinar entradas para guiar modelos de IA na produção de saídas desejadas.
Tokenização: O processo de converter texto em unidades menores, chamadas tokens, que um modelo pode entender e processar.
LLMs Ajustados por Instruções: Modelos de Linguagem de Grande Escala (LLMs) que foram ajustados com instruções específicas para melhorar a precisão e relevância de suas respostas.

## Sandbox de Aprendizagem

A engenharia de prompts é atualmente mais arte do que ciência. A melhor maneira de melhorar nossa intuição para isso é _praticar mais_ e adotar uma abordagem de tentativa e erro que combina expertise no domínio da aplicação com técnicas recomendadas e otimizações específicas de modelo.

O Jupyter Notebook que acompanha esta lição fornece um ambiente _sandbox_ onde você pode experimentar o que aprendeu - enquanto avança ou como parte do desafio de código no final. Para executar os exercícios, você precisará de:

1. **Uma chave de API do Azure OpenAI** - o endpoint de serviço para um LLM implantado.
2. **Um Runtime Python** - no qual o Notebook pode ser executado.
3. **Variáveis de Ambiente Locais** - _complete os passos do [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) agora para se preparar_.

O notebook vem com exercícios _iniciais_ - mas você é incentivado a adicionar suas próprias seções de _Markdown_ (descrição) e _Código_ (solicitações de prompt) para experimentar mais exemplos ou ideias - e construir sua intuição para o design de prompts.

## Guia Ilustrado

Quer ter uma visão geral do que esta lição cobre antes de mergulhar? Confira este guia ilustrado, que dá uma ideia dos principais tópicos abordados e dos principais pontos para você pensar em cada um. O roteiro da lição leva você desde a compreensão dos conceitos e desafios centrais até abordá-los com técnicas relevantes de engenharia de prompts e melhores práticas. Note que a seção "Técnicas Avançadas" neste guia refere-se ao conteúdo abordado no _próximo_ capítulo deste currículo.

## Nossa Startup

Agora, vamos falar sobre como _este tópico_ se relaciona com nossa missão de startup de [trazer inovação em IA para a educação](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicativos de aprendizado personalizado com IA - então vamos pensar em como diferentes usuários de nosso aplicativo podem "projetar" prompts:

- **Administradores** podem pedir à IA para _analisar dados do currículo para identificar lacunas na cobertura_. A IA pode resumir os resultados ou visualizá-los com código.
- **Educadores** podem pedir à IA para _gerar um plano de aula para um público-alvo e tópico específico_. A IA pode construir o plano personalizado em um formato especificado.
- **Estudantes** podem pedir à IA para _tutorá-los em um assunto difícil_. A IA agora pode orientar os alunos com lições, dicas e exemplos adaptados ao seu nível.

Isso é apenas a ponta do iceberg. Confira [Prompts Para Educação](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - uma biblioteca de prompts de código aberto curada por especialistas em educação - para ter uma ideia mais ampla das possibilidades! _Experimente executar alguns desses prompts no sandbox ou usando o OpenAI Playground para ver o que acontece!_

## O que é Engenharia de Prompts?

Começamos esta lição definindo **Engenharia de Prompts** como o processo de _projetar e otimizar_ entradas de texto (prompts) para fornecer respostas consistentes e de qualidade (conclusões) para um determinado objetivo de aplicação e modelo. Podemos pensar nisso como um processo de 2 etapas:

- _projetar_ o prompt inicial para um determinado modelo e objetivo
- _refinar_ o prompt iterativamente para melhorar a qualidade da resposta

Este é necessariamente um processo de tentativa e erro que exige intuição e esforço do usuário para obter resultados ótimos. Então, por que isso é importante? Para responder a essa pergunta, primeiro precisamos entender três conceitos:

- _Tokenização_ = como o modelo "vê" o prompt
- _Base LLMs_ = como o modelo base "processa" um prompt
- _LLMs Ajustados por Instruções_ = como o modelo agora pode ver "tarefas"

### Tokenização

Um LLM vê prompts como uma _sequência de tokens_ onde diferentes modelos (ou versões de um modelo) podem tokenizar o mesmo prompt de maneiras diferentes. Como os LLMs são treinados em tokens (e não em texto bruto), a forma como os prompts são tokenizados tem um impacto direto na qualidade da resposta gerada.

Para ter uma intuição de como a tokenização funciona, experimente ferramentas como o [Tokenizador da OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abaixo. Copie seu prompt - e veja como ele é convertido em tokens, prestando atenção em como os caracteres de espaço em branco e os sinais de pontuação são tratados. Note que este exemplo mostra um LLM mais antigo (GPT-3) - então tentar isso com um modelo mais novo pode produzir um resultado diferente.

### Conceito: Modelos de Fundação

Uma vez que um prompt é tokenizado, a função principal do ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modelo de fundação) é prever o token naquela sequência. Como os LLMs são treinados em conjuntos de dados massivos de texto, eles têm uma boa noção das relações estatísticas entre tokens e podem fazer essa previsão com alguma confiança. Note que eles não entendem o _significado_ das palavras no prompt ou token; eles apenas veem um padrão que podem "completar" com sua próxima previsão. Eles podem continuar prevendo a sequência até serem interrompidos por intervenção do usuário ou alguma condição pré-estabelecida.

Quer ver como funciona a conclusão baseada em prompt? Insira o prompt acima no [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) do Azure OpenAI Studio com as configurações padrão. O sistema está configurado para tratar prompts como solicitações de informação - então você deve ver uma conclusão que satisfaz esse contexto.

Mas e se o usuário quisesse ver algo específico que atendesse a algum critério ou objetivo de tarefa? É aí que entram os LLMs ajustados por instruções.

### Conceito: LLMs Ajustados por Instruções

Um [LLM Ajustado por Instruções](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) começa com o modelo de fundação e o ajusta com exemplos ou pares de entrada/saída (por exemplo, "mensagens" de múltiplas interações) que podem conter instruções claras - e a resposta da IA tenta seguir essa instrução.

Isso usa técnicas como Aprendizado por Reforço com Feedback Humano (RLHF) que podem treinar o modelo para _seguir instruções_ e _aprender com feedback_ para que ele produza respostas mais adequadas a aplicações práticas e mais relevantes aos objetivos do usuário.

Vamos experimentar - revise o prompt acima, mas agora altere a _mensagem do sistema_ para fornecer a seguinte instrução como contexto:

> _Resuma o conteúdo que lhe é fornecido para um aluno de segunda série. Mantenha o resultado em um parágrafo com 3-5 pontos._

Veja como o resultado agora é ajustado para refletir o objetivo e formato desejados? Um educador agora pode usar diretamente essa resposta em seus slides para aquela aula.

## Por que precisamos de Engenharia de Prompts?

Agora que sabemos como os prompts são processados pelos LLMs, vamos falar sobre _por que_ precisamos de engenharia de prompts. A resposta está no fato de que os LLMs atuais apresentam uma série de desafios que tornam _conclusões confiáveis e consistentes_ mais difíceis de alcançar sem colocar esforço na construção e otimização de prompts. Por exemplo:

1. **As respostas do modelo são estocásticas.** O _mesmo prompt_ provavelmente produzirá respostas diferentes com modelos diferentes ou versões de modelo diferentes. E pode até produzir resultados diferentes com o _mesmo modelo_ em momentos diferentes. _Técnicas de engenharia de prompts podem nos ajudar a minimizar essas variações, fornecendo melhores limites_.

2. **Os modelos podem fabricar respostas.** Os modelos são pré-treinados com _conjuntos de dados grandes, mas finitos_, o que significa que eles não têm conhecimento sobre conceitos fora desse escopo de treinamento. Como resultado, eles podem produzir conclusões que são imprecisas, imaginárias ou diretamente contraditórias a fatos conhecidos. _Técnicas de engenharia de prompts ajudam os usuários a identificar e mitigar essas fabricações, por exemplo, pedindo à IA por citações ou raciocínio_.

3. **As capacidades dos modelos variam.** Modelos mais novos ou gerações de modelos terão capacidades mais ricas, mas também trazem peculiaridades únicas e compensações em custo e complexidade. _A engenharia de prompts pode nos ajudar a desenvolver melhores práticas e fluxos de trabalho que abstraem diferenças e se adaptam a requisitos específicos de modelo de maneiras escaláveis e contínuas_.

Vamos ver isso em ação no OpenAI ou Azure OpenAI Playground:

- Use o mesmo prompt com diferentes implantações de LLM (por exemplo, OpenAI, Azure OpenAI, Hugging Face) - você viu as variações?
- Use o mesmo prompt repetidamente com a _mesma_ implantação de LLM (por exemplo, playground do Azure OpenAI) - como essas variações diferiram?

### Exemplo de Fabricações

Neste curso, usamos o termo **"fabricação"** para referenciar o fenômeno onde os LLMs às vezes geram informações factualmente incorretas devido a limitações em seu treinamento ou outras restrições. Você também pode ter ouvido isso referido como _"alucinações"_ em artigos populares ou trabalhos de pesquisa. No entanto, recomendamos fortemente o uso de _"fabricação"_ como termo para não antropomorfizar o comportamento atribuindo uma característica humana a um resultado impulsionado por máquina. Isso também reforça as [diretrizes de IA Responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) do ponto de vista da terminologia, removendo termos que também podem ser considerados ofensivos ou não inclusivos em alguns contextos.

Quer ter uma ideia de como as fabricações funcionam? Pense em um prompt que instrua a IA a gerar conteúdo para um tópico inexistente (para garantir que não seja encontrado no conjunto de dados de treinamento). Por exemplo - eu tentei este prompt:

> **Prompt:** gerar um plano de aula sobre a Guerra Marciana de 2076.

Uma pesquisa na web me mostrou que havia relatos fictícios (por exemplo, séries de televisão ou livros) sobre guerras marcianas - mas nenhum em 2076. O senso comum também nos diz que 2076 está _no futuro_ e, portanto, não pode estar associado a um evento real.

Então, o que acontece quando executamos este prompt com diferentes provedores de LLM?

> **Resposta 1**: OpenAI Playground (GPT-35)

> **Resposta 2**: Azure OpenAI Playground (GPT-35)

> **Resposta 3**: Hugging Face Chat Playground (LLama-2)

Como esperado, cada modelo (ou versão de modelo) produz respostas ligeiramente diferentes devido ao comportamento estocástico e às variações de capacidade do modelo. Por exemplo, um modelo direciona um público de 8ª série enquanto o outro assume um estudante do ensino médio. Mas todos os três modelos geraram respostas que poderiam convencer um usuário desinformado de que o evento era real.

Técnicas de engenharia de prompts como _metaprompting_ e _configuração de temperatura_ podem reduzir fabricações de modelo até certo ponto. Novas _arquiteturas_ de engenharia de prompts também incorporam novas ferramentas e técnicas de forma contínua no fluxo de prompts, para mitigar ou reduzir alguns desses efeitos.

## Estudo de Caso: GitHub Copilot

Vamos encerrar esta seção obtendo uma ideia de como a engenharia de prompts é usada em soluções do mundo real, olhando para um Estudo de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

O GitHub Copilot é seu "Programador de Pareia com IA" - ele converte prompts de texto em conclusões de código e está integrado em seu ambiente de desenvolvimento (por exemplo, Visual Studio Code) para uma experiência de usuário contínua. Conforme documentado na série de blogs abaixo, a versão mais antiga foi baseada no modelo Codex da OpenAI - com engenheiros rapidamente percebendo a necessidade de ajustar o modelo e desenvolver melhores técnicas de engenharia de prompts, para melhorar a qualidade do código. Em julho, eles [estrearam um modelo de IA melhorado que vai além do Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugestões ainda mais rápidas.

Leia os posts na ordem, para acompanhar sua jornada de aprendizado.

- **Maio de 2023** | [GitHub Copilot está Melhorando na Compreensão do Seu Código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maio de 2023** | [Dentro do GitHub: Trabalhando com os LLMs por trás do GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junho de 2023** | [Como escrever melhores prompts para o GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julho de 2023** | [.. GitHub Copilot vai além do Codex com modelo de IA melhorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julho de 2023** | [Um Guia do Desenvolvedor para Engenharia de Prompts e LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Setembro de 2023** | [Como construir um aplicativo de LLM empresarial: Lições do GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Você também pode navegar pelo blog de [Engenharia](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) deles para mais posts como [este](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que mostra como esses modelos e técnicas são _aplicados_ para impulsionar aplicativos do mundo real.

---

## Construção de Prompts

Vimos por que a engenharia de prompts é importante - agora vamos entender como os prompts são _construídos_ para que possamos avaliar diferentes técnicas para um design de prompt mais eficaz.

### Prompt Básico

Vamos começar com o prompt básico: uma entrada de texto enviada ao modelo sem outro contexto. Aqui está um exemplo - quando enviamos as primeiras palavras do hino nacional dos EUA para a [API de Conclusão](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) da OpenAI,
Finalmente, o verdadeiro valor dos modelos reside na capacidade de criar e publicar _bibliotecas de prompts_ para domínios de aplicação vertical - onde o modelo de prompt é agora _otimizado_ para refletir o contexto ou exemplos específicos da aplicação que tornam as respostas mais relevantes e precisas para o público-alvo. O repositório [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) é um ótimo exemplo desta abordagem, curando uma biblioteca de prompts para o domínio educacional com ênfase em objetivos chave como planeamento de aulas, design curricular, tutoria de estudantes, etc.

## Conteúdo de Apoio

Se pensarmos na construção de prompts como tendo uma instrução (tarefa) e um alvo (conteúdo principal), então o _conteúdo secundário_ é como um contexto adicional que fornecemos para **influenciar o resultado de alguma forma**. Pode ser afinar parâmetros, instruções de formatação, taxonomias de tópicos, etc., que podem ajudar o modelo a _personalizar_ a sua resposta para se adequar aos objetivos ou expectativas desejadas pelo utilizador.

Por exemplo: Dado um catálogo de cursos com extensa metadados (nome, descrição, nível, etiquetas de metadados, instrutor, etc.) sobre todos os cursos disponíveis no currículo:

- podemos definir uma instrução para "resumir o catálogo de cursos para o Outono de 2023"
- podemos usar o conteúdo principal para fornecer alguns exemplos do resultado desejado
- podemos usar o conteúdo secundário para identificar as 5 principais "etiquetas" de interesse.

Agora, o modelo pode fornecer um resumo no formato mostrado pelos poucos exemplos - mas se um resultado tiver várias etiquetas, pode priorizar as 5 etiquetas identificadas no conteúdo secundário.

---

<!--
LESSON TEMPLATE:
Esta unidade deve cobrir o conceito central #1.
Reforce o conceito com exemplos e referências.

CONCEITO #3:
Técnicas de Engenharia de Prompt.
Quais são algumas técnicas básicas para engenharia de prompt?
Ilustre com alguns exercícios.
-->

## Melhores Práticas de Prompting

Agora que sabemos como os prompts podem ser _construídos_, podemos começar a pensar em como _desenhá-los_ para refletir as melhores práticas. Podemos pensar nisso em duas partes - ter a _mentalidade_ certa e aplicar as _técnicas_ certas.

### Mentalidade de Engenharia de Prompt

A Engenharia de Prompt é um processo de tentativa e erro, por isso mantenha três fatores orientadores amplos em mente:

1. **Compreensão do Domínio é Importante.** A precisão e relevância das respostas é uma função do _domínio_ em que essa aplicação ou utilizador opera. Aplique a sua intuição e experiência no domínio para **personalizar técnicas** ainda mais. Por exemplo, defina _personalidades específicas do domínio_ nos seus prompts do sistema ou use _modelos específicos do domínio_ nos seus prompts do utilizador. Forneça conteúdo secundário que reflita contextos específicos do domínio, ou use _pistas e exemplos específicos do domínio_ para guiar o modelo em direção a padrões de uso familiares.

2. **Compreensão do Modelo é Importante.** Sabemos que os modelos são estocásticos por natureza. Mas as implementações de modelos também podem variar em termos do conjunto de dados de treino que utilizam (conhecimento pré-treinado), as capacidades que fornecem (por exemplo, via API ou SDK) e o tipo de conteúdo para o qual são otimizados (por exemplo, código vs. imagens vs. texto). Compreenda os pontos fortes e as limitações do modelo que está a usar e utilize esse conhecimento para _priorizar tarefas_ ou construir _modelos personalizados_ otimizados para as capacidades do modelo.

3. **Iteração e Validação são Importantes.** Os modelos estão a evoluir rapidamente, e também as técnicas para engenharia de prompt. Como especialista em domínio, pode ter outro contexto ou critérios _da sua_ aplicação específica, que podem não se aplicar à comunidade mais ampla. Use ferramentas e técnicas de engenharia de prompt para "dar o pontapé inicial" na construção de prompts, depois itere e valide os resultados usando a sua própria intuição e experiência no domínio. Registe os seus insights e crie uma **base de conhecimento** (por exemplo, bibliotecas de prompts) que pode ser usada como um novo ponto de partida por outros, para iterações mais rápidas no futuro.

## Melhores Práticas

Agora vamos olhar para práticas comuns recomendadas por [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praticantes.

| O quê                              | Porquê                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Avalie os modelos mais recentes.       | Novas gerações de modelos provavelmente terão características e qualidade melhoradas - mas também podem incorrer em custos mais elevados. Avalie-os para impacto, depois tome decisões de migração.                                                                                |
| Separe instruções e contexto   | Verifique se o seu modelo/provedor define _delimitadores_ para distinguir instruções, conteúdo principal e secundário de forma mais clara. Isso pode ajudar os modelos a atribuir pesos mais precisamente aos tokens.                                                         |
| Seja específico e claro             | Dê mais detalhes sobre o contexto desejado, resultado, comprimento, formato, estilo, etc. Isso irá melhorar tanto a qualidade quanto a consistência das respostas. Capture receitas em modelos reutilizáveis.                                                          |
| Seja descritivo, use exemplos      | Os modelos podem responder melhor a uma abordagem de "mostrar e contar". Comece com uma `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` valores. Volte para a [secção de Sandbox de Aprendizagem](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) para aprender como.

### Em seguida, abra o Jupyter Notebook

- Selecione o kernel de runtime. Se estiver a usar as opções 1 ou 2, basta selecionar o kernel padrão Python 3.10.x fornecido pelo contêiner de desenvolvimento.

Está tudo pronto para executar os exercícios. Note que não há respostas _certas ou erradas_ aqui - apenas explorando opções por tentativa e erro e construindo intuição sobre o que funciona para um determinado modelo e domínio de aplicação.

_Por esta razão, não há segmentos de Solução de Código nesta lição. Em vez disso, o Notebook terá células Markdown intituladas "Minha Solução:" que mostram um exemplo de resultado para referência._

 <!--
LESSON TEMPLATE:
Envolva a seção com um resumo e recursos para aprendizagem autónoma.
-->

## Verificação de Conhecimento

Qual das seguintes é um bom prompt seguindo algumas práticas razoáveis?

1. Mostra-me uma imagem de carro vermelho
2. Mostra-me uma imagem de carro vermelho da marca Volvo e modelo XC90 estacionado junto a um penhasco com o sol a pôr-se
3. Mostra-me uma imagem de carro vermelho da marca Volvo e modelo XC90

A: 2, é o melhor prompt pois fornece detalhes sobre "o quê" e entra em especificidades (não apenas qualquer carro, mas uma marca e modelo específicos) e também descreve o cenário geral. 3 é o próximo melhor pois também contém muita descrição.

## 🚀 Desafio

Veja se consegue aproveitar a técnica de "pista" com o prompt: Complete a frase "Mostra-me uma imagem de carro vermelho da marca Volvo e ". Com o que responde, e como melhoraria?

## Ótimo Trabalho! Continue a Aprender

Quer aprender mais sobre diferentes conceitos de Engenharia de Prompt? Vá para a [página de aprendizagem contínua](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre este tópico.

Dirija-se à Lição 5 onde iremos olhar para [técnicas avançadas de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.