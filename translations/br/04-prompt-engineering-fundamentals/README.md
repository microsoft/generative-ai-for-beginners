<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:29:56+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "br"
}
-->
# Fundamentos de Engenharia de Prompt

## Introdução
Este módulo aborda conceitos e técnicas essenciais para criar prompts eficazes em modelos de IA generativa. A maneira como você escreve seu prompt para um LLM também importa. Um prompt cuidadosamente elaborado pode alcançar uma melhor qualidade de resposta. Mas o que exatamente significam termos como _prompt_ e _engenharia de prompt_? E como posso melhorar o _input_ do prompt que envio para o LLM? Essas são as perguntas que tentaremos responder neste capítulo e no próximo.

A _IA generativa_ é capaz de criar novo conteúdo (por exemplo, texto, imagens, áudio, código etc.) em resposta a solicitações do usuário. Ela alcança isso usando _Modelos de Linguagem de Grande Escala_, como a série GPT ("Generative Pre-trained Transformer") da OpenAI, que são treinados para usar linguagem natural e código.

Os usuários agora podem interagir com esses modelos usando paradigmas familiares, como chat, sem precisar de qualquer conhecimento técnico ou treinamento. Os modelos são baseados em _prompts_ - os usuários enviam uma entrada de texto (prompt) e recebem a resposta da IA (completamento). Eles podem então "conversar com a IA" de forma iterativa, em conversas de múltiplas rodadas, refinando seu prompt até que a resposta corresponda às suas expectativas.

"Prompts" agora se tornam a principal _interface de programação_ para aplicativos de IA generativa, dizendo aos modelos o que fazer e influenciando a qualidade das respostas retornadas. "Engenharia de Prompt" é um campo de estudo em rápido crescimento que se concentra no _design e otimização_ de prompts para fornecer respostas consistentes e de qualidade em escala.

## Objetivos de Aprendizagem

Nesta lição, aprenderemos o que é Engenharia de Prompt, por que é importante e como podemos elaborar prompts mais eficazes para um determinado modelo e objetivo de aplicação. Vamos entender os conceitos principais e as melhores práticas para engenharia de prompt - e aprender sobre um ambiente "sandbox" interativo de Jupyter Notebooks onde podemos ver esses conceitos aplicados a exemplos reais.

Ao final desta lição, seremos capazes de:

1. Explicar o que é engenharia de prompt e por que é importante.
2. Descrever os componentes de um prompt e como eles são usados.
3. Aprender melhores práticas e técnicas para engenharia de prompt.
4. Aplicar técnicas aprendidas a exemplos reais, usando um endpoint da OpenAI.

## Termos Chave

Engenharia de Prompt: A prática de projetar e refinar entradas para orientar modelos de IA na produção de saídas desejadas.
Tokenização: O processo de converter texto em unidades menores, chamadas tokens, que um modelo pode entender e processar.
LLMs Ajustados por Instrução: Modelos de Linguagem de Grande Escala (LLMs) que foram ajustados com instruções específicas para melhorar a precisão e relevância de suas respostas.

## Sandbox de Aprendizagem

A engenharia de prompt atualmente é mais arte do que ciência. A melhor maneira de melhorar nossa intuição para isso é _praticar mais_ e adotar uma abordagem de tentativa e erro que combine expertise no domínio de aplicação com técnicas recomendadas e otimizações específicas do modelo.

O Jupyter Notebook que acompanha esta lição fornece um ambiente _sandbox_ onde você pode experimentar o que aprende - conforme avança ou como parte do desafio de código no final. Para executar os exercícios, você precisará de:

1. **Uma chave de API do Azure OpenAI** - o endpoint de serviço para um LLM implantado.
2. **Um Runtime Python** - no qual o Notebook pode ser executado.
3. **Variáveis de Ambiente Locais** - _complete os passos de [CONFIGURAÇÃO](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) agora para se preparar_.

O notebook vem com exercícios _iniciantes_ - mas você é incentivado a adicionar suas próprias seções de _Markdown_ (descrição) e _Código_ (solicitações de prompt) para experimentar mais exemplos ou ideias - e construir sua intuição para design de prompt.

## Guia Ilustrado

Quer ter uma visão geral do que esta lição cobre antes de mergulhar? Confira este guia ilustrado, que dá uma ideia dos principais tópicos abordados e os principais aprendizados para você refletir em cada um. O roteiro da lição leva você do entendimento dos conceitos principais e desafios para abordá-los com técnicas de engenharia de prompt relevantes e melhores práticas. Note que a seção "Técnicas Avançadas" neste guia refere-se ao conteúdo abordado no _próximo_ capítulo deste currículo.

## Nossa Startup

Agora, vamos falar sobre como _este tópico_ se relaciona com nossa missão de startup de [trazer inovação de IA para a educação](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicativos impulsionados por IA de _aprendizado personalizado_ - então vamos pensar sobre como diferentes usuários de nosso aplicativo podem "projetar" prompts:

- **Administradores** podem pedir à IA para _analisar dados de currículo para identificar lacunas na cobertura_. A IA pode resumir resultados ou visualizá-los com código.
- **Educadores** podem pedir à IA para _gerar um plano de aula para um público-alvo e tópico_. A IA pode construir o plano personalizado em um formato especificado.
- **Estudantes** podem pedir à IA para _tutorar eles em um assunto difícil_. A IA agora pode guiar os estudantes com lições, dicas e exemplos adaptados ao seu nível.

Isso é apenas a ponta do iceberg. Confira [Prompts Para Educação](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - uma biblioteca de prompts de código aberto curada por especialistas em educação - para ter uma ideia mais ampla das possibilidades! _Tente executar alguns desses prompts no sandbox ou usando o OpenAI Playground para ver o que acontece!_

## O que é Engenharia de Prompt?

Começamos esta lição definindo **Engenharia de Prompt** como o processo de _projetar e otimizar_ entradas de texto (prompts) para fornecer respostas consistentes e de qualidade (completamentos) para um determinado objetivo de aplicação e modelo. Podemos pensar nisso como um processo de 2 etapas:

- _projetar_ o prompt inicial para um determinado modelo e objetivo
- _refinar_ o prompt iterativamente para melhorar a qualidade da resposta

Este é necessariamente um processo de tentativa e erro que requer intuição e esforço do usuário para obter resultados ótimos. Então, por que é importante? Para responder a essa pergunta, primeiro precisamos entender três conceitos:

- _Tokenização_ = como o modelo "vê" o prompt
- _LLMs Base_ = como o modelo de fundação "processa" um prompt
- _LLMs Ajustados por Instrução_ = como o modelo agora pode ver "tarefas"

### Tokenização

Um LLM vê prompts como uma _sequência de tokens_ onde diferentes modelos (ou versões de um modelo) podem tokenizar o mesmo prompt de maneiras diferentes. Como os LLMs são treinados em tokens (e não em texto bruto), a maneira como os prompts são tokenizados tem um impacto direto na qualidade da resposta gerada.

Para ter uma intuição de como a tokenização funciona, experimente ferramentas como o [Tokenizador OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abaixo. Copie seu prompt - e veja como isso é convertido em tokens, prestando atenção em como caracteres de espaço em branco e sinais de pontuação são tratados. Note que este exemplo mostra um LLM mais antigo (GPT-3) - então tentar isso com um modelo mais novo pode produzir um resultado diferente.

### Conceito: Modelos de Fundação

Uma vez que um prompt é tokenizado, a função principal do ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modelo de fundação) é prever o token naquela sequência. Como os LLMs são treinados em conjuntos de dados massivos de texto, eles têm uma boa noção das relações estatísticas entre tokens e podem fazer essa previsão com alguma confiança. Note que eles não entendem o _significado_ das palavras no prompt ou token; eles apenas veem um padrão que podem "completar" com sua próxima previsão. Eles podem continuar prevendo a sequência até serem interrompidos por intervenção do usuário ou alguma condição pré-estabelecida.

Quer ver como funciona a conclusão baseada em prompt? Insira o prompt acima no [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) do Azure OpenAI Studio com as configurações padrão. O sistema está configurado para tratar prompts como solicitações de informações - então você deve ver um completamento que satisfaz esse contexto.

Mas e se o usuário quisesse ver algo específico que atendesse a alguns critérios ou objetivo de tarefa? É aqui que os LLMs _ajustados por instrução_ entram em cena.

### Conceito: LLMs Ajustados por Instrução

Um [LLM Ajustado por Instrução](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) começa com o modelo de fundação e o ajusta com exemplos ou pares de entrada/saída (por exemplo, "mensagens" de múltiplas rodadas) que podem conter instruções claras - e a resposta da IA tenta seguir essa instrução.

Isso usa técnicas como Aprendizado por Reforço com Feedback Humano (RLHF) que podem treinar o modelo para _seguir instruções_ e _aprender com feedback_ para que produza respostas mais adequadas a aplicações práticas e mais relevantes aos objetivos do usuário.

Vamos experimentar - revisite o prompt acima, mas agora mude a _mensagem do sistema_ para fornecer a seguinte instrução como contexto:

> _Resuma o conteúdo que você recebeu para um aluno de segundo grau. Mantenha o resultado em um parágrafo com 3-5 pontos de destaque._

Veja como o resultado agora é ajustado para refletir o objetivo e formato desejados? Um educador agora pode usar diretamente essa resposta em seus slides para aquela aula.

## Por que precisamos de Engenharia de Prompt?

Agora que sabemos como os prompts são processados pelos LLMs, vamos falar sobre _por que_ precisamos de engenharia de prompt. A resposta está no fato de que os LLMs atuais apresentam uma série de desafios que tornam _completamentos confiáveis e consistentes_ mais difíceis de alcançar sem colocar esforço na construção e otimização de prompts. Por exemplo:

1. **Respostas do modelo são estocásticas.** O _mesmo prompt_ provavelmente produzirá respostas diferentes com modelos diferentes ou versões de modelos. E pode até produzir resultados diferentes com o _mesmo modelo_ em momentos diferentes. _Técnicas de engenharia de prompt podem nos ajudar a minimizar essas variações fornecendo melhores diretrizes_.

1. **Modelos podem fabricar respostas.** Modelos são pré-treinados com _conjuntos de dados grandes, mas finitos_, o que significa que eles não têm conhecimento sobre conceitos fora desse escopo de treinamento. Como resultado, eles podem produzir completamentos que são imprecisos, imaginários ou diretamente contraditórios a fatos conhecidos. _Técnicas de engenharia de prompt ajudam os usuários a identificar e mitigar tais fabricações, por exemplo, pedindo à IA por citações ou raciocínio_.

1. **Capacidades dos modelos variam.** Modelos mais novos ou gerações de modelos terão capacidades mais ricas, mas também trazem peculiaridades únicas e trade-offs em custo e complexidade. _A engenharia de prompt pode nos ajudar a desenvolver melhores práticas e fluxos de trabalho que abstraem diferenças e se adaptam a requisitos específicos do modelo de maneiras escaláveis e contínuas_.

Vamos ver isso em ação no OpenAI ou Azure OpenAI Playground:

- Use o mesmo prompt com diferentes implantações de LLM (por exemplo, OpenAI, Azure OpenAI, Hugging Face) - você viu as variações?
- Use o mesmo prompt repetidamente com a _mesma_ implantação de LLM (por exemplo, playground do Azure OpenAI) - como essas variações diferiram?

### Exemplo de Fabricações

Neste curso, usamos o termo **"fabricação"** para referenciar o fenômeno em que LLMs às vezes geram informações factualmente incorretas devido a limitações em seu treinamento ou outras restrições. Você também pode ter ouvido isso ser referido como _"alucinações"_ em artigos populares ou trabalhos de pesquisa. No entanto, recomendamos fortemente o uso de _"fabricação"_ como termo para não antropomorfizar acidentalmente o comportamento atribuindo uma característica humana a um resultado impulsionado por máquina. Isso também reforça as [diretrizes de IA Responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) do ponto de vista da terminologia, removendo termos que também podem ser considerados ofensivos ou não inclusivos em alguns contextos.

Quer ter uma ideia de como funcionam as fabricações? Pense em um prompt que instrua a IA a gerar conteúdo para um tópico inexistente (para garantir que não seja encontrado no conjunto de dados de treinamento). Por exemplo - eu tentei este prompt:

> **Prompt:** gerar um plano de aula sobre a Guerra Marciana de 2076.

Uma pesquisa na web me mostrou que havia relatos fictícios (por exemplo, séries de televisão ou livros) sobre guerras marcianas - mas nenhum em 2076. O bom senso também nos diz que 2076 é _no futuro_ e, portanto, não pode estar associado a um evento real.

Então, o que acontece quando executamos este prompt com diferentes provedores de LLM?

Como esperado, cada modelo (ou versão do modelo) produz respostas ligeiramente diferentes graças ao comportamento estocástico e variações de capacidade do modelo. Por exemplo, um modelo direciona um público de oitava série enquanto o outro assume um estudante de ensino médio. Mas todos os três modelos geraram respostas que poderiam convencer um usuário desinformado de que o evento era real.

Técnicas de engenharia de prompt como _metaprompting_ e _configuração de temperatura_ podem reduzir fabricações de modelos até certo ponto. Novas _arquiteturas_ de engenharia de prompt também incorporam novas ferramentas e técnicas de forma contínua no fluxo de prompt, para mitigar ou reduzir alguns desses efeitos.

## Estudo de Caso: GitHub Copilot

Vamos encerrar esta seção obtendo uma noção de como a engenharia de prompt é usada em soluções do mundo real, olhando para um Estudo de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot é seu "Programador Pareado com IA" - ele converte prompts de texto em completamentos de código e é integrado ao seu ambiente de desenvolvimento (por exemplo, Visual Studio Code) para uma experiência de usuário contínua. Conforme documentado na série de blogs abaixo, a versão mais antiga foi baseada no modelo Codex da OpenAI - com engenheiros rapidamente percebendo a necessidade de ajustar o modelo e desenvolver melhores técnicas de engenharia de prompt, para melhorar a qualidade do código. Em julho, eles [estrearam um modelo de IA aprimorado que vai além do Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugestões ainda mais rápidas.

Leia os posts na ordem, para seguir a jornada de aprendizado deles.

- **Maio 2023** | [GitHub Copilot está ficando melhor em entender seu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maio 2023** | [Dentro do GitHub: Trabalhando com os LLMs por trás do GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junho 2023** | [Como escrever melhores prompts para GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julho 2023** | [.. GitHub Copilot vai além do Codex com modelo de IA aprimorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julho 2023** | [Um Guia do Desenvolvedor para Engenharia de Prompt e LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Setembro 2023** | [Como construir um aplicativo empresarial de LLM: Lições do GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Você também pode navegar no [blog de Engenharia](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) deles para mais posts como [este](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que mostra como esses modelos e técnicas são _aplicados_ para impulsionar aplicativos do mundo real.

## Construção de Prompt

Vimos por que a engenharia de prompt é importante - agora vamos entender como os prompts são _construídos_ para que possamos avaliar diferentes técnicas para um design de prompt mais eficaz.

### Prompt Básico

Vamos começar com o prompt básico: uma entrada de texto enviada ao modelo sem outro contexto. Aqui está um exemplo - quando enviamos as primeiras palavras do hino nacional dos EUA para a [API de Completamento](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) da OpenAI, ele instantaneamente _completa_ a resposta com as próximas linhas, ilustrando o comportamento básico de previsão.

### Prompt Complexo

Agora vamos adicionar contexto e instruções a esse prompt básico. A [API de Completamento de Chat](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc
Finalmente, o verdadeiro valor dos modelos está na capacidade de criar e publicar _bibliotecas de prompts_ para domínios de aplicação vertical - onde o modelo de prompt agora é _otimizado_ para refletir o contexto ou exemplos específicos da aplicação que tornam as respostas mais relevantes e precisas para o público-alvo. O repositório [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) é um ótimo exemplo dessa abordagem, organizando uma biblioteca de prompts para o domínio educacional com ênfase em objetivos-chave como planejamento de aulas, design curricular, tutoria de alunos, etc.

## Conteúdo de Apoio

Se pensarmos na construção de prompts como tendo uma instrução (tarefa) e um alvo (conteúdo principal), então o _conteúdo secundário_ é como um contexto adicional que fornecemos para **influenciar a saída de alguma forma**. Pode ser ajustes de parâmetros, instruções de formatação, taxonomias de tópicos, etc., que podem ajudar o modelo a _adaptar_ sua resposta para atender aos objetivos ou expectativas desejadas do usuário.

Por exemplo: Dado um catálogo de cursos com metadados extensivos (nome, descrição, nível, tags de metadados, instrutor, etc.) sobre todos os cursos disponíveis no currículo:

- podemos definir uma instrução para "resumir o catálogo de cursos para o outono de 2023"
- podemos usar o conteúdo principal para fornecer alguns exemplos do resultado desejado
- podemos usar o conteúdo secundário para identificar as 5 principais "tags" de interesse.

Agora, o modelo pode fornecer um resumo no formato mostrado pelos poucos exemplos - mas se um resultado tiver várias tags, ele pode priorizar as 5 tags identificadas no conteúdo secundário.

---

## Melhores Práticas de Prompting

Agora que sabemos como os prompts podem ser _construídos_, podemos começar a pensar em como _projetá-los_ para refletir as melhores práticas. Podemos pensar nisso em duas partes - ter a _mentalidade_ certa e aplicar as _técnicas_ certas.

### Mentalidade de Engenharia de Prompts

A Engenharia de Prompts é um processo de tentativa e erro, então mantenha três fatores amplos em mente:

1. **Entendimento do Domínio Importa.** A precisão e relevância da resposta são uma função do _domínio_ em que a aplicação ou usuário opera. Aplique sua intuição e expertise no domínio para **personalizar técnicas** ainda mais. Por exemplo, defina _personalidades específicas do domínio_ em seus prompts de sistema, ou use _modelos específicos do domínio_ em seus prompts de usuário. Forneça conteúdo secundário que reflita contextos específicos do domínio ou use _dicas e exemplos específicos do domínio_ para guiar o modelo em padrões de uso familiares.

2. **Entendimento do Modelo Importa.** Sabemos que os modelos são estocásticos por natureza. Mas as implementações de modelo também podem variar em termos do conjunto de dados de treinamento que usam (conhecimento pré-treinado), das capacidades que fornecem (por exemplo, via API ou SDK) e do tipo de conteúdo para o qual são otimizados (por exemplo, código vs. imagens vs. texto). Entenda os pontos fortes e limitações do modelo que você está usando e use esse conhecimento para _priorizar tarefas_ ou construir _modelos personalizados_ que são otimizados para as capacidades do modelo.

3. **Iteração e Validação Importam.** Os modelos estão evoluindo rapidamente, assim como as técnicas de engenharia de prompts. Como especialista no domínio, você pode ter outro contexto ou critérios para _sua_ aplicação específica, que podem não se aplicar à comunidade mais ampla. Use ferramentas e técnicas de engenharia de prompts para "dar o pontapé inicial" na construção de prompts, depois itere e valide os resultados usando sua própria intuição e expertise no domínio. Registre seus insights e crie uma **base de conhecimento** (por exemplo, bibliotecas de prompts) que pode ser usada como um novo ponto de partida por outros, para iterações mais rápidas no futuro.

## Melhores Práticas

Agora vamos olhar para as práticas recomendadas comuns que são recomendadas por [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e praticantes do [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| O que                              | Por que                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Avalie os modelos mais recentes.       | As novas gerações de modelos provavelmente terão recursos e qualidade aprimorados - mas também podem incorrer em custos mais altos. Avalie-os para impacto e depois tome decisões de migração.                                                                                |
| Separe instruções e contexto   | Verifique se seu modelo/provedor define _delimitadores_ para distinguir instruções, conteúdo primário e secundário de forma mais clara. Isso pode ajudar os modelos a atribuir pesos mais precisos aos tokens.                                                         |
| Seja específico e claro             | Dê mais detalhes sobre o contexto desejado, resultado, comprimento, formato, estilo, etc. Isso melhorará tanto a qualidade quanto a consistência das respostas. Capture receitas em modelos reutilizáveis.                                                          |
| Seja descritivo, use exemplos      | Os modelos podem responder melhor a uma abordagem de "mostrar e contar". Comece com um `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` valores. Volte para a [seção de Sandbox de Aprendizado](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) para aprender como.

### Em seguida, abra o Jupyter Notebook

- Selecione o kernel de tempo de execução. Se estiver usando as opções 1 ou 2, basta selecionar o kernel Python 3.10.x padrão fornecido pelo contêiner de desenvolvimento.

Você está pronto para executar os exercícios. Observe que não há respostas _certas e erradas_ aqui - apenas explorando opções por tentativa e erro e construindo intuição sobre o que funciona para um determinado modelo e domínio de aplicação.

_Por esse motivo, não há segmentos de Solução de Código nesta lição. Em vez disso, o Notebook terá células Markdown intituladas "Minha Solução:" que mostram um exemplo de saída para referência._

## Verificação de Conhecimento

Qual das seguintes é um bom prompt seguindo algumas práticas recomendadas razoáveis?

1. Mostre-me uma imagem de um carro vermelho
2. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90 estacionado à beira de um penhasco com o sol se pondo
3. Mostre-me uma imagem de um carro vermelho da marca Volvo e modelo XC90

A: 2, é o melhor prompt pois fornece detalhes sobre "o quê" e entra em especificidades (não apenas qualquer carro, mas uma marca e modelo específicos) e também descreve o cenário geral. 3 é o próximo melhor, pois também contém muita descrição.

## 🚀 Desafio

Veja se você consegue aproveitar a técnica de "dica" com o prompt: Complete a frase "Mostre-me uma imagem de um carro vermelho da marca Volvo e ". Com o que ele responde e como você melhoraria isso?

## Ótimo Trabalho! Continue Seu Aprendizado

Quer aprender mais sobre diferentes conceitos de Engenharia de Prompts? Acesse a [página de aprendizado contínuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre este tópico.

Vá para a Lição 5, onde vamos olhar para [técnicas avançadas de prompts](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.