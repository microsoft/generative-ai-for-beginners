<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcbaaae026cb50fee071e690685b5843",
  "translation_date": "2025-08-26T16:18:12+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "pt"
}
-->
# Fundamentos da Engenharia de Prompts

[![Fundamentos da Engenharia de Prompts](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.pt.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Introdução
Este módulo aborda conceitos e técnicas essenciais para criar prompts eficazes em modelos de IA generativa. A forma como escreves o teu prompt para um LLM também faz diferença. Um prompt bem elaborado pode garantir uma resposta de melhor qualidade. Mas afinal, o que significam termos como _prompt_ e _engenharia de prompts_? E como posso melhorar o _input_ do prompt que envio para o LLM? São estas as perguntas que vamos tentar responder neste capítulo e no seguinte.

A _IA generativa_ consegue criar novos conteúdos (por exemplo, texto, imagens, áudio, código, etc.) em resposta a pedidos dos utilizadores. Isto é possível graças a _Modelos de Linguagem de Grande Escala_ como a série GPT ("Generative Pre-trained Transformer") da OpenAI, treinados para trabalhar com linguagem natural e código.

Os utilizadores podem agora interagir com estes modelos através de interfaces familiares como o chat, sem precisarem de conhecimentos técnicos ou formação específica. Os modelos são _baseados em prompts_ – o utilizador envia um texto (prompt) e recebe uma resposta da IA (completion). Pode depois "conversar com a IA" de forma iterativa, em várias voltas, ajustando o prompt até que a resposta corresponda ao que pretende.

Os "prompts" tornam-se assim a principal _interface de programação_ para aplicações de IA generativa, indicando aos modelos o que fazer e influenciando a qualidade das respostas. A "Engenharia de Prompts" é uma área de estudo em rápido crescimento, focada no _design e otimização_ de prompts para garantir respostas consistentes e de qualidade em larga escala.

## Objetivos de Aprendizagem

Nesta lição, vamos aprender o que é Engenharia de Prompts, porque é importante e como podemos criar prompts mais eficazes para um determinado modelo e objetivo de aplicação. Vamos perceber os conceitos fundamentais e as melhores práticas para engenharia de prompts – e conhecer um ambiente interativo em Jupyter Notebooks onde podemos ver estes conceitos aplicados a exemplos reais.

No final desta lição seremos capazes de:

1. Explicar o que é engenharia de prompts e porque é relevante.
2. Descrever os componentes de um prompt e como são utilizados.
3. Aprender boas práticas e técnicas para engenharia de prompts.
4. Aplicar as técnicas aprendidas a exemplos reais, usando um endpoint da OpenAI.

## Termos-Chave

Engenharia de Prompts: Prática de desenhar e aperfeiçoar inputs para orientar modelos de IA a produzir os resultados desejados.
Tokenização: Processo de converter texto em unidades mais pequenas, chamadas tokens, que o modelo consegue compreender e processar.
LLMs Ajustados por Instruções: Modelos de Linguagem de Grande Escala (LLMs) que foram ajustados com instruções específicas para melhorar a precisão e relevância das respostas.

## Sandbox de Aprendizagem

A engenharia de prompts é, para já, mais uma arte do que uma ciência. A melhor forma de desenvolver intuição para esta área é _praticar bastante_ e adotar uma abordagem de tentativa e erro, combinando conhecimento do domínio de aplicação com técnicas recomendadas e otimizações específicas do modelo.

O Jupyter Notebook que acompanha esta lição oferece um ambiente _sandbox_ onde podes experimentar o que aprendes – à medida que avanças ou como parte do desafio de código no final. Para executar os exercícios, vais precisar de:

1. **Uma chave de API do Azure OpenAI** – o endpoint do serviço para um LLM implementado.
2. **Um ambiente de execução Python** – onde o Notebook pode ser executado.
3. **Variáveis de ambiente locais** – _conclui agora os passos de [CONFIGURAÇÃO](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) para te preparares_.

O notebook inclui exercícios _iniciais_ – mas és incentivado a acrescentar as tuas próprias secções de _Markdown_ (descrição) e _Código_ (pedidos de prompt) para experimentar mais exemplos ou ideias – e desenvolver a tua intuição para o design de prompts.

## Guia Ilustrado

Queres ter uma visão geral do que esta lição cobre antes de começares? Consulta este guia ilustrado, que te dá uma ideia dos principais tópicos abordados e dos pontos-chave para refletires em cada um. O roteiro da lição leva-te desde a compreensão dos conceitos e desafios fundamentais até à sua resolução com técnicas e boas práticas relevantes de engenharia de prompts. Repara que a secção "Técnicas Avançadas" neste guia refere-se a conteúdos que serão abordados no _próximo_ capítulo deste curso.

![Guia Ilustrado para Engenharia de Prompts](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.pt.png)

## A Nossa Startup

Agora, vamos falar sobre como _este tema_ se relaciona com a nossa missão de startup de [trazer inovação em IA para a educação](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos criar aplicações de _aprendizagem personalizada_ com IA – por isso, vamos pensar em como diferentes utilizadores da nossa aplicação podem "desenhar" prompts:

- **Administradores** podem pedir à IA para _analisar dados curriculares e identificar lacunas de cobertura_. A IA pode resumir os resultados ou visualizá-los com código.
- **Educadores** podem pedir à IA para _gerar um plano de aula para um público-alvo e tema específico_. A IA pode construir o plano personalizado num formato definido.
- **Alunos** podem pedir à IA para _os ajudar numa disciplina difícil_. A IA pode orientar os alunos com lições, dicas e exemplos adaptados ao seu nível.

Isto é apenas o início. Vê [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – uma biblioteca open-source de prompts, curada por especialistas em educação – para teres uma ideia mais ampla das possibilidades! _Experimenta alguns desses prompts no sandbox ou no OpenAI Playground para ver o que acontece!_

<!--
MODELO DE LIÇÃO:
Esta unidade deve cobrir o conceito fundamental #1.
Reforça o conceito com exemplos e referências.

CONCEITO #1:
Engenharia de Prompts.
Define e explica porque é necessária.
-->

## O que é Engenharia de Prompts?

Começámos esta lição por definir **Engenharia de Prompts** como o processo de _desenhar e otimizar_ inputs de texto (prompts) para garantir respostas consistentes e de qualidade (completions) para um determinado objetivo de aplicação e modelo. Podemos pensar nisto como um processo em 2 etapas:

- _desenhar_ o prompt inicial para um modelo e objetivo específicos
- _refinar_ o prompt de forma iterativa para melhorar a qualidade da resposta

Este é inevitavelmente um processo de tentativa e erro que exige intuição e esforço do utilizador para obter os melhores resultados. Mas porque é importante? Para responder, precisamos primeiro de perceber três conceitos:

- _Tokenização_ = como o modelo "vê" o prompt
- _LLMs Base_ = como o modelo de base "processa" um prompt
- _LLMs Ajustados por Instruções_ = como o modelo consegue agora ver "tarefas"

### Tokenização

Um LLM vê os prompts como uma _sequência de tokens_, e diferentes modelos (ou versões de um modelo) podem tokenizar o mesmo prompt de formas distintas. Como os LLMs são treinados com tokens (e não com texto bruto), a forma como os prompts são tokenizados tem impacto direto na qualidade da resposta gerada.

Para perceberes como funciona a tokenização, experimenta ferramentas como o [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abaixo. Cola o teu prompt – e vê como é convertido em tokens, prestando atenção ao tratamento de espaços e pontuação. Nota que este exemplo mostra um LLM mais antigo (GPT-3) – se experimentares com um modelo mais recente, podes obter resultados diferentes.

![Tokenização](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.pt.png)

### Conceito: Modelos de Base

Depois de tokenizado o prompt, a principal função do ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modelo de base) é prever o próximo token nessa sequência. Como os LLMs são treinados com enormes conjuntos de dados de texto, têm uma boa noção das relações estatísticas entre tokens e conseguem fazer essa previsão com alguma confiança. Repara que não compreendem o _significado_ das palavras ou tokens do prompt; apenas identificam padrões que podem "completar" com a próxima previsão. Podem continuar a prever a sequência até serem interrompidos pelo utilizador ou por alguma condição pré-definida.

Queres ver como funciona a conclusão baseada em prompts? Introduz o prompt acima no [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) do Azure OpenAI Studio com as definições padrão. O sistema está configurado para tratar prompts como pedidos de informação – por isso deves ver uma resposta que se enquadra nesse contexto.

Mas e se o utilizador quiser ver algo específico que cumpra certos critérios ou objetivos de tarefa? É aqui que entram os LLMs _ajustados por instruções_.

![Conclusão de Chat com LLM Base](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.pt.png)

### Conceito: LLMs Ajustados por Instruções

Um [LLM Ajustado por Instruções](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) parte do modelo de base e é ajustado com exemplos ou pares de input/output (por exemplo, "mensagens" em várias voltas) que podem conter instruções claras – e a resposta da IA tenta seguir essa instrução.

Isto recorre a técnicas como Aprendizagem por Reforço com Feedback Humano (RLHF), que treinam o modelo para _seguir instruções_ e _aprender com o feedback_, produzindo respostas mais adequadas a aplicações práticas e mais relevantes para os objetivos do utilizador.

Vamos experimentar – volta ao prompt acima, mas agora altera a _mensagem do sistema_ para fornecer a seguinte instrução como contexto:

> _Resume o conteúdo que te for fornecido para um aluno do segundo ano. Mantém o resultado num parágrafo com 3-5 pontos-chave._

Vê como o resultado agora está ajustado para refletir o objetivo e formato pretendidos? Um educador pode usar diretamente esta resposta nos seus slides para essa aula.

![Conclusão de Chat com LLM Ajustado por Instruções](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.pt.png)

## Porque precisamos de Engenharia de Prompts?

Agora que sabemos como os prompts são processados pelos LLMs, vamos falar sobre _porque_ precisamos de engenharia de prompts. A resposta está no facto de que os LLMs atuais apresentam vários desafios que tornam _completions fiáveis e consistentes_ mais difíceis de obter sem investir no design e otimização dos prompts. Por exemplo:

1. **As respostas dos modelos são estocásticas.** O _mesmo prompt_ provavelmente vai gerar respostas diferentes em modelos ou versões de modelos distintos. E pode até produzir resultados diferentes com o _mesmo modelo_ em momentos diferentes. _As técnicas de engenharia de prompts ajudam a minimizar estas variações, fornecendo melhores limites e orientações_.

1. **Os modelos podem inventar respostas.** Os modelos são pré-treinados com _conjuntos de dados grandes mas finitos_, o que significa que não têm conhecimento sobre conceitos fora desse âmbito. Como resultado, podem gerar respostas que são imprecisas, inventadas ou até contraditórias com factos conhecidos. _A engenharia de prompts ajuda os utilizadores a identificar e mitigar estas invenções, por exemplo, pedindo à IA citações ou justificações_.

1. **As capacidades dos modelos variam.** Modelos mais recentes ou gerações diferentes têm capacidades mais avançadas, mas também trazem particularidades e compromissos em termos de custo e complexidade. _A engenharia de prompts permite desenvolver boas práticas e fluxos de trabalho que abstraem diferenças e se adaptam a requisitos específicos de cada modelo de forma escalável e fluida_.

Vamos ver isto em ação no OpenAI ou Azure OpenAI Playground:

- Usa o mesmo prompt com diferentes implementações de LLM (por exemplo, OpenAI, Azure OpenAI, Hugging Face) – reparaste nas variações?
- Usa o mesmo prompt várias vezes com a _mesma_ implementação de LLM (por exemplo, Azure OpenAI playground) – como diferiram essas variações?

### Exemplo de Fabricações

Neste curso, usamos o termo **"fabricação"** para referir o fenómeno em que os LLMs por vezes geram informação factualmente incorreta devido a limitações no seu treino ou outros fatores. Também podes ter ouvido este fenómeno chamado de _"alucinações"_ em artigos ou estudos. No entanto, recomendamos fortemente o uso do termo _"fabricação"_ para evitar atribuir características humanas a um resultado gerado por máquina. Isto também reforça as [diretrizes de IA Responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) do ponto de vista da terminologia, eliminando termos que podem ser considerados ofensivos ou não inclusivos em certos contextos.

Queres perceber como funcionam as fabricações? Pensa num prompt que instrua a IA a gerar conteúdo sobre um tema inexistente (para garantir que não está no conjunto de treino). Por exemplo – experimentei este prompt:
# Plano de Aula: A Guerra Marciana de 2076

## Objetivos de Aprendizagem

- Compreender as causas e consequências da Guerra Marciana de 2076.
- Analisar o impacto do conflito na sociedade marciana e terrestre.
- Discutir as estratégias militares e diplomáticas utilizadas durante a guerra.
- Refletir sobre as lições aprendidas e possíveis implicações para o futuro.

## Introdução

A Guerra Marciana de 2076 foi um dos eventos mais marcantes do século XXI, alterando profundamente as relações entre Marte e a Terra. Neste plano de aula, vamos explorar os principais acontecimentos, os protagonistas e as consequências deste conflito histórico.

## Conteúdo

### 1. Contexto Histórico

- Colonização de Marte e tensões iniciais com a Terra.
- Disputas por recursos naturais e autonomia marciana.
- Eventos que levaram ao início da guerra em 2076.

### 2. Principais Fases do Conflito

- Início das hostilidades e ataques estratégicos.
- Intervenção de alianças internacionais.
- Uso de tecnologia avançada e armas inovadoras.

### 3. Protagonistas

- Líderes marcianos e terrestres.
- Papel das organizações civis e militares.
- Influência de empresas privadas e cientistas.

### 4. Consequências

- Mudanças políticas e sociais em Marte e na Terra.
- Tratados de paz e reconstrução pós-guerra.
- Impacto na exploração espacial e nas futuras colónias.

## Atividades

- Debate em grupo sobre as causas da guerra.
- Análise de fontes históricas e testemunhos de sobreviventes.
- Simulação de negociações de paz entre Marte e Terra.

## Avaliação

- Participação nas discussões e atividades.
- Elaboração de um relatório sobre as consequências da guerra.
- Apresentação de propostas para evitar futuros conflitos interplanetários.

## Recursos

- Documentos históricos e artigos científicos.
- Mapas das batalhas e movimentações militares.
- Entrevistas com especialistas em história marciana.

## Conclusão

A Guerra Marciana de 2076 serve como um exemplo importante dos desafios e oportunidades que surgem com a expansão humana para outros planetas. Ao estudar este conflito, podemos aprender a promover a cooperação e evitar os erros do passado.
Uma pesquisa na web mostrou-me que existem relatos fictícios (por exemplo, séries de televisão ou livros) sobre guerras em Marte – mas nenhum em 2076. O senso comum também nos diz que 2076 é _no futuro_ e, por isso, não pode estar associado a um evento real.

Então, o que acontece quando executamos este prompt com diferentes fornecedores de LLM?

> **Resposta 1**: OpenAI Playground (GPT-35)

![Resposta 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.pt.png)

> **Resposta 2**: Azure OpenAI Playground (GPT-35)

![Resposta 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.pt.png)

> **Resposta 3**: : Hugging Face Chat Playground (LLama-2)

![Resposta 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.pt.png)

Como era de esperar, cada modelo (ou versão do modelo) produz respostas ligeiramente diferentes devido ao comportamento estocástico e às variações de capacidade dos modelos. Por exemplo, um modelo dirige-se a um público do 8.º ano, enquanto outro assume um estudante do ensino secundário. Mas todos os três modelos geraram respostas que poderiam convencer um utilizador desinformado de que o evento era real.

Técnicas de engenharia de prompts como _metaprompting_ e _configuração de temperatura_ podem reduzir as fabricações dos modelos até certo ponto. Novas _arquiteturas_ de engenharia de prompts também incorporam novas ferramentas e técnicas de forma integrada no fluxo do prompt, para mitigar ou reduzir alguns destes efeitos.

## Caso de Estudo: GitHub Copilot

Vamos terminar esta secção percebendo como a engenharia de prompts é usada em soluções reais, analisando um Caso de Estudo: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

O GitHub Copilot é o teu "Programador Parceiro de IA" – converte prompts de texto em sugestões de código e está integrado no teu ambiente de desenvolvimento (por exemplo, Visual Studio Code) para uma experiência de utilização fluida. Como documentado na série de blogs abaixo, a versão inicial baseava-se no modelo OpenAI Codex – com os engenheiros a perceberem rapidamente a necessidade de afinar o modelo e desenvolver melhores técnicas de engenharia de prompts para melhorar a qualidade do código. Em julho, [lançaram um modelo de IA melhorado que vai além do Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugestões ainda mais rápidas.

Lê os artigos por ordem para acompanhar a evolução do seu conhecimento.

- **Maio 2023** | [O GitHub Copilot está a ficar melhor a compreender o teu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maio 2023** | [Por dentro do GitHub: Trabalhar com os LLMs por trás do GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Como escrever melhores prompts para o GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. O GitHub Copilot vai além do Codex com um modelo de IA melhorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Guia do Programador para Engenharia de Prompts e LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Set 2023** | [Como construir uma app empresarial com LLM: Lições do GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Também podes explorar o [blog de Engenharia](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para mais artigos como [este](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que mostra como estes modelos e técnicas são _aplicados_ para impulsionar aplicações reais.

---

## Construção de Prompts

Já vimos porque é que a engenharia de prompts é importante – agora vamos perceber como os prompts são _construídos_ para podermos avaliar diferentes técnicas para um design de prompts mais eficaz.

### Prompt Básico

Comecemos pelo prompt básico: um texto enviado ao modelo sem qualquer outro contexto. Eis um exemplo – quando enviamos as primeiras palavras do hino nacional dos EUA à [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) da OpenAI, esta _completa_ imediatamente a resposta com as linhas seguintes, ilustrando o comportamento básico de previsão.

| Prompt (Entrada)     | Completamento (Saída)                                                                                                                        |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see   | Parece que estás a começar a letra de "The Star-Spangled Banner", o hino nacional dos Estados Unidos. A letra completa é ...                |

### Prompt Complexo

Agora vamos adicionar contexto e instruções a esse prompt básico. A [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) permite-nos construir um prompt complexo como um conjunto de _mensagens_ com:

- Pares de entrada/saída que refletem a entrada do _utilizador_ e a resposta do _assistente_.
- Mensagem de sistema que define o contexto para o comportamento ou personalidade do assistente.

O pedido tem agora o formato abaixo, onde a _tokenização_ capta eficazmente a informação relevante do contexto e da conversa. Agora, alterar o contexto do sistema pode ter tanto impacto na qualidade das respostas como as entradas do utilizador fornecidas.

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

Nos exemplos acima, o prompt do utilizador era uma simples consulta de texto que pode ser interpretada como um pedido de informação. Com prompts de _instrução_, podemos usar esse texto para especificar uma tarefa com mais detalhe, dando uma orientação mais clara à IA. Eis um exemplo:

| Prompt (Entrada)                                                                                                                                                                                                                         | Completamento (Saída)                                                                                                        | Tipo de Instrução   |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Escreve uma descrição da Guerra Civil                                                                                                                                                                                                   | _devolveu um parágrafo simples_                                                                                              | Simples             |
| Escreve uma descrição da Guerra Civil. Indica datas e eventos importantes e descreve a sua relevância                                                                                             | _devolveu um parágrafo seguido de uma lista de datas de eventos importantes com descrições_                                  | Complexa            |
| Escreve uma descrição da Guerra Civil num parágrafo. Indica 3 pontos-chave com datas e a sua relevância. Indica mais 3 pontos-chave com figuras históricas e as suas contribuições. Devolve o resultado em formato JSON                   | _devolve detalhes mais extensos numa caixa de texto, formatados em JSON que podes copiar para um ficheiro e validar se necessário_ | Complexa. Formatada. |

## Conteúdo Principal

Nos exemplos acima, o prompt ainda era bastante aberto, permitindo ao LLM decidir que parte do seu conjunto de dados pré-treinado era relevante. Com o padrão de design de _conteúdo principal_, o texto de entrada é dividido em duas partes:

- uma instrução (ação)
- conteúdo relevante (que influencia a ação)

Eis um exemplo em que a instrução é "resume isto em 2 frases".

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completamento (Saída)                                                                                                                                                                                                                                                                             |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter é o quinto planeta a contar do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa mil vezes menor que a do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e é conhecido pelas civilizações antigas desde antes da história registada. O seu nome vem do deus romano Júpiter.[19] Visto da Terra, Júpiter pode ser suficientemente brilhante para a sua luz refletida projetar sombras visíveis,[20] e é, em média, o terceiro objeto natural mais brilhante no céu noturno, depois da Lua e de Vénus. <br/> **Resume isto em 2 frases curtas** | Júpiter, o quinto planeta a contar do Sol, é o maior do Sistema Solar e é conhecido por ser um dos objetos mais brilhantes no céu noturno. Com o nome do deus romano Júpiter, é um gigante gasoso cuja massa é duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. |

O segmento de conteúdo principal pode ser usado de várias formas para tornar as instruções mais eficazes:

- **Exemplos** – em vez de dizer ao modelo o que fazer com uma instrução explícita, dá-lhe exemplos do que fazer e deixa-o inferir o padrão.
- **Cues (Indícios)** – segue a instrução com um "indício" que prepara a resposta, guiando o modelo para respostas mais relevantes.
- **Templates (Modelos)** – são 'receitas' repetíveis para prompts com espaços reservados (variáveis) que podem ser personalizados com dados para casos de uso específicos.

Vamos ver estes casos em ação.

### Usar Exemplos

Esta é uma abordagem em que usas o conteúdo principal para "alimentar o modelo" com exemplos do resultado desejado para uma determinada instrução, deixando-o inferir o padrão para a saída pretendida. Dependendo do número de exemplos fornecidos, podemos ter zero-shot prompting, one-shot prompting, few-shot prompting, etc.

O prompt passa a ter três componentes:

- Uma descrição da tarefa
- Alguns exemplos do resultado desejado
- O início de um novo exemplo (que se torna uma descrição implícita da tarefa)

| Tipo de Aprendizagem | Prompt (Entrada)                                                                                                                                        | Completamento (Saída)         |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------- |
| Zero-shot            | "The Sun is Shining". Translate to Spanish                                                                                                              | "El Sol está brillando".      |
| One-shot             | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                   | "Es un día frío y ventoso".   |
| Few-shot             | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk =>   | Basketball                    |
|                      |                                                                                                                                                         |                               |

Repara como tivemos de dar uma instrução explícita ("Translate to Spanish") no zero-shot prompting, mas ela é inferida no exemplo one-shot. O exemplo few-shot mostra como, ao adicionar mais exemplos, os modelos conseguem fazer inferências mais precisas sem instruções adicionais.

### Indícios no Prompt (Prompt Cues)

Outra técnica para usar o conteúdo principal é fornecer _indícios_ em vez de exemplos. Neste caso, estamos a dar ao modelo um empurrão na direção certa, _começando_ com um excerto que reflete o formato de resposta desejado. O modelo depois "segue o indício" e continua nesse registo.

| Número de Indícios | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completamento (Saída)                                                                                                                                                                                                                                                                                       |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                  | Júpiter é o quinto planeta a contar do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa mil vezes menor que a do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e é conhecido pelas civilizações antigas desde antes da história registada.

**Resumir Isto**                                       | Júpiter é o maior planeta do nosso Sistema Solar e o quinto a contar do Sol. É um gigante gasoso com uma massa equivalente a 1/1000 da do Sol, mas é mais pesado do que todos os outros planetas juntos. As civilizações antigas já conheciam Júpiter há muito tempo, e é facilmente visível no céu noturno. |
| 1              | Júpiter é o quinto planeta a contar do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e é conhecido pelas civilizações antigas desde antes da história registada. <br/>**Resumir Isto** <br/> O que aprendemos é que Júpiter | é o quinto planeta a contar do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas juntos. É facilmente visível a olho nu e é conhecido desde a Antiguidade.                        |
| 2              | Júpiter é o quinto planeta a contar do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e é conhecido pelas civilizações antigas desde antes da história registada. <br/>**Resumir Isto** <br/> Top 3 Factos Aprendidos:         | 1. Júpiter é o quinto planeta a contar do Sol e o maior do Sistema Solar. <br/> 2. É um gigante gasoso com uma massa equivalente a um milésimo da do Sol...<br/> 3. Júpiter é visível a olho nu desde a Antiguidade ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Modelos de Prompt

Um modelo de prompt é uma _receita pré-definida para um prompt_ que pode ser guardada e reutilizada conforme necessário, para garantir experiências de utilizador mais consistentes em larga escala. Na sua forma mais simples, é apenas uma coleção de exemplos de prompts como [este da OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) que fornece tanto os componentes interativos do prompt (mensagens do utilizador e do sistema) como o formato de pedido orientado por API - para facilitar a reutilização.

Numa forma mais complexa, como [este exemplo do LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), contém _espaços reservados_ que podem ser substituídos por dados de várias fontes (entrada do utilizador, contexto do sistema, fontes de dados externas, etc.) para gerar um prompt de forma dinâmica. Isto permite criar uma biblioteca de prompts reutilizáveis que podem ser usados para garantir experiências de utilizador consistentes **programaticamente** em escala.

Por fim, o verdadeiro valor dos modelos está na capacidade de criar e publicar _bibliotecas de prompts_ para domínios de aplicação verticalizados - onde o modelo de prompt é agora _optimizado_ para refletir o contexto ou exemplos específicos da aplicação, tornando as respostas mais relevantes e precisas para o público-alvo. O repositório [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) é um excelente exemplo desta abordagem, ao reunir uma biblioteca de prompts para o domínio da educação com ênfase em objetivos-chave como planeamento de aulas, desenho curricular, tutoria de alunos, etc.

## Conteúdo de Apoio

Se pensarmos na construção de prompts como tendo uma instrução (tarefa) e um alvo (conteúdo principal), então o _conteúdo secundário_ é como contexto adicional que fornecemos para **influenciar a resposta de alguma forma**. Pode ser parâmetros de afinação, instruções de formatação, taxonomias de tópicos, etc., que ajudam o modelo a _ajustar_ a sua resposta para se adequar aos objetivos ou expectativas do utilizador.

Por exemplo: Dado um catálogo de cursos com metadados extensos (nome, descrição, nível, etiquetas, instrutor, etc.) sobre todos os cursos disponíveis no currículo:

- podemos definir uma instrução para "resumir o catálogo de cursos para o Outono de 2023"
- podemos usar o conteúdo principal para fornecer alguns exemplos do resultado desejado
- podemos usar o conteúdo secundário para identificar as 5 principais "etiquetas" de interesse.

Agora, o modelo pode fornecer um resumo no formato mostrado pelos exemplos - mas se um resultado tiver várias etiquetas, pode dar prioridade às 5 identificadas no conteúdo secundário.

---

<!--
MODELO DE LIÇÃO:
Esta unidade deve cobrir o conceito central #1.
Reforçar o conceito com exemplos e referências.

CONCEITO #3:
Técnicas de Engenharia de Prompts.
Quais são algumas técnicas básicas de engenharia de prompts?
Ilustre com alguns exercícios.
-->

## Boas Práticas de Prompting

Agora que já sabemos como os prompts podem ser _construídos_, podemos começar a pensar em como _desenhá-los_ para refletir as melhores práticas. Podemos pensar nisto em duas partes - ter a _mentalidade_ certa e aplicar as _técnicas_ certas.

### Mentalidade de Engenharia de Prompts

A Engenharia de Prompts é um processo de tentativa e erro, por isso mantenha três grandes fatores orientadores em mente:

1. **Compreensão do Domínio é Importante.** A precisão e relevância das respostas depende do _domínio_ em que a aplicação ou utilizador opera. Use a sua intuição e experiência no domínio para **personalizar técnicas** ainda mais. Por exemplo, defina _personalidades específicas do domínio_ nos seus prompts de sistema, ou use _modelos específicos do domínio_ nos seus prompts de utilizador. Forneça conteúdo secundário que reflita contextos do domínio, ou use _pistas e exemplos do domínio_ para guiar o modelo para padrões de uso familiares.

2. **Compreensão do Modelo é Importante.** Sabemos que os modelos são estocásticos por natureza. Mas as implementações dos modelos também podem variar em termos do conjunto de dados de treino que usam (conhecimento pré-treinado), das capacidades que oferecem (por exemplo, via API ou SDK) e do tipo de conteúdo para o qual estão otimizados (por exemplo, código vs. imagens vs. texto). Compreenda os pontos fortes e limitações do modelo que está a usar, e use esse conhecimento para _priorizar tarefas_ ou construir _modelos personalizados_ otimizados para as capacidades do modelo.

3. **Iteração & Validação são Importantes.** Os modelos estão a evoluir rapidamente, tal como as técnicas de engenharia de prompts. Como especialista no domínio, pode ter outro contexto ou critérios para _a sua_ aplicação específica, que podem não se aplicar à comunidade em geral. Use ferramentas e técnicas de engenharia de prompts para "dar o pontapé de saída" na construção de prompts, depois itere e valide os resultados usando a sua própria intuição e experiência. Registe os seus insights e crie uma **base de conhecimento** (por exemplo, bibliotecas de prompts) que possa ser usada como novo ponto de partida por outros, para iterações mais rápidas no futuro.

## Boas Práticas

Vejamos agora algumas boas práticas recomendadas por profissionais da [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e da [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| O quê                              | Porquê                                                                                                                                                                                                                                               |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avalie os modelos mais recentes.   | Novas gerações de modelos tendem a ter melhores funcionalidades e qualidade - mas também podem ter custos mais elevados. Avalie o impacto e só depois decida migrar.                                                                                |
| Separe instruções e contexto       | Verifique se o seu modelo/fornecedor define _delimitadores_ para distinguir instruções, conteúdo principal e secundário de forma mais clara. Isto pode ajudar os modelos a atribuir pesos mais precisos aos tokens.                                 |
| Seja específico e claro            | Dê mais detalhes sobre o contexto desejado, resultado, comprimento, formato, estilo, etc. Isto melhora a qualidade e consistência das respostas. Guarde receitas em modelos reutilizáveis.                                                          |
| Seja descritivo, use exemplos      | Os modelos podem responder melhor a uma abordagem de "mostrar e explicar". Comece com uma abordagem `zero-shot` onde dá apenas uma instrução (sem exemplos) e depois tente `few-shot` como refinamento, fornecendo alguns exemplos do resultado. Use analogias. |
| Use pistas para iniciar respostas  | Dê um empurrão na direção do resultado desejado, fornecendo algumas palavras ou frases iniciais que o modelo possa usar como ponto de partida para a resposta.                                                                                       |
| Reforce a instrução                | Por vezes pode ser necessário repetir a instrução ao modelo. Dê instruções antes e depois do conteúdo principal, use uma instrução e uma pista, etc. Itere e valide para ver o que resulta melhor.                                                  |
| A ordem importa                    | A ordem em que apresenta a informação ao modelo pode influenciar o resultado, mesmo nos exemplos de aprendizagem, devido ao viés de recência. Experimente diferentes opções para ver o que funciona melhor.                                         |
| Dê ao modelo uma “escapatória”     | Dê ao modelo uma resposta de _reserva_ que possa fornecer caso não consiga completar a tarefa por algum motivo. Isto pode reduzir a probabilidade de respostas falsas ou inventadas.                                                               |
|                                   |                                                                                                                                                                                                                                                     |

Como em qualquer boa prática, lembre-se que _os resultados podem variar_ consoante o modelo, a tarefa e o domínio. Use estas recomendações como ponto de partida e itere para encontrar o que funciona melhor para si. Reavalie constantemente o seu processo de engenharia de prompts à medida que surgem novos modelos e ferramentas, com foco na escalabilidade do processo e na qualidade das respostas.

<!--
MODELO DE LIÇÃO:
Esta unidade deve fornecer um desafio de código, se aplicável

DESAFIO:
Ligue para um Jupyter Notebook apenas com os comentários de código nas instruções (as secções de código estão vazias).

SOLUÇÃO:
Ligue para uma cópia desse Notebook com os prompts preenchidos e executados, mostrando um exemplo possível.
-->

## Exercício

Parabéns! Chegou ao fim da lição! Está na altura de pôr alguns destes conceitos e técnicas à prova com exemplos reais!

Para o nosso exercício, vamos usar um Jupyter Notebook com exercícios que pode completar de forma interativa. Também pode estender o Notebook com as suas próprias células Markdown e de Código para explorar ideias e técnicas por si.

### Para começar, faça fork do repositório, depois

- (Recomendado) Inicie o GitHub Codespaces
- (Em alternativa) Clone o repositório para o seu dispositivo local e use-o com o Docker Desktop
- (Em alternativa) Abra o Notebook no seu ambiente de execução de Notebooks preferido.

### De seguida, configure as variáveis de ambiente

- Copie o ficheiro `.env.copy` na raiz do repositório para `.env` e preencha os valores `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT`. Volte à [secção Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) para saber como.

### Depois, abra o Jupyter Notebook

- Selecione o kernel de execução. Se usar as opções 1 ou 2, basta selecionar o kernel Python 3.10.x por defeito fornecido pelo dev container.

Está tudo pronto para executar os exercícios. Note que aqui não há respostas _certas ou erradas_ - trata-se apenas de explorar opções por tentativa e erro e construir intuição sobre o que funciona para um determinado modelo e domínio de aplicação.

_Por este motivo, não há segmentos de Solução de Código nesta lição. Em vez disso, o Notebook terá células Markdown intituladas "A Minha Solução:" que mostram um exemplo de saída para referência._

 <!--
MODELO DE LIÇÃO:
Envolva a secção com um resumo e recursos para autoaprendizagem.
-->

## Verificação de Conhecimentos

Qual dos seguintes é um bom prompt seguindo algumas boas práticas razoáveis?

1. Mostra-me uma imagem de um carro vermelho
2. Mostra-me uma imagem de um carro vermelho da marca Volvo e modelo XC90 estacionado junto a uma falésia com o sol a pôr-se
3. Mostra-me uma imagem de um carro vermelho da marca Volvo e modelo XC90

R: 2, é o melhor prompt pois fornece detalhes sobre o "quê" e vai ao pormenor (não é apenas um carro qualquer, mas uma marca e modelo específicos) e também descreve o cenário geral. O 3 é o seguinte melhor, pois também contém bastante descrição.

## 🚀 Desafio

Vê se consegues usar a técnica da "pista" com o prompt: Completa a frase "Mostra-me uma imagem de um carro vermelho da marca Volvo e ". O que responde o modelo, e como o melhorarias?

## Excelente Trabalho! Continua a Aprender

Queres aprender mais sobre diferentes conceitos de Engenharia de Prompts? Vai à [página de aprendizagem contínua](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrares outros ótimos recursos sobre este tema.

Segue para a Lição 5 onde vamos explorar [técnicas avançadas de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.