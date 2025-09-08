<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcbaaae026cb50fee071e690685b5843",
  "translation_date": "2025-08-26T16:26:18+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "br"
}
-->
# Fundamentos de Engenharia de Prompt

[![Fundamentos de Engenharia de Prompt](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.br.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Introdução
Este módulo aborda conceitos e técnicas essenciais para criar prompts eficazes em modelos de IA generativa. A forma como você escreve seu prompt para um LLM também faz diferença. Um prompt bem elaborado pode gerar respostas de melhor qualidade. Mas o que exatamente significam termos como _prompt_ e _engenharia de prompt_? E como posso melhorar o _input_ do prompt que envio para o LLM? Essas são as perguntas que vamos tentar responder neste capítulo e no próximo.

A _IA generativa_ é capaz de criar novos conteúdos (por exemplo, texto, imagens, áudio, código etc.) em resposta a solicitações dos usuários. Ela faz isso usando _Modelos de Linguagem de Grande Escala_ como a série GPT ("Generative Pre-trained Transformer") da OpenAI, que são treinados para usar linguagem natural e código.

Agora, os usuários podem interagir com esses modelos usando paradigmas familiares como chat, sem precisar de conhecimento técnico ou treinamento. Os modelos são _baseados em prompt_ – os usuários enviam um texto (prompt) e recebem a resposta da IA (completion). Eles podem então "conversar com a IA" de forma iterativa, em conversas de múltiplas rodadas, refinando o prompt até que a resposta atenda às suas expectativas.

Os "prompts" agora se tornam a principal _interface de programação_ para aplicativos de IA generativa, dizendo aos modelos o que fazer e influenciando a qualidade das respostas retornadas. "Engenharia de Prompt" é um campo de estudo em rápido crescimento que foca no _design e otimização_ de prompts para entregar respostas consistentes e de qualidade em escala.

## Objetivos de Aprendizagem

Nesta lição, vamos aprender o que é Engenharia de Prompt, por que ela é importante e como podemos criar prompts mais eficazes para um determinado modelo e objetivo de aplicação. Vamos entender conceitos fundamentais e boas práticas para engenharia de prompt – e conhecer um ambiente interativo de "sandbox" em Jupyter Notebooks onde podemos ver esses conceitos aplicados em exemplos reais.

Ao final desta lição, seremos capazes de:

1. Explicar o que é engenharia de prompt e por que ela é importante.
2. Descrever os componentes de um prompt e como eles são usados.
3. Aprender boas práticas e técnicas para engenharia de prompt.
4. Aplicar as técnicas aprendidas em exemplos reais, usando um endpoint da OpenAI.

## Termos-Chave

Engenharia de Prompt: Prática de projetar e refinar entradas para guiar modelos de IA a produzirem saídas desejadas.
Tokenização: Processo de converter texto em unidades menores, chamadas tokens, que um modelo pode entender e processar.
LLMs Ajustados por Instrução: Modelos de Linguagem de Grande Escala (LLMs) que foram ajustados com instruções específicas para melhorar a precisão e relevância das respostas.

## Sandbox de Aprendizagem

A engenharia de prompt atualmente é mais uma arte do que uma ciência. A melhor forma de aprimorar nossa intuição sobre o tema é _praticar mais_ e adotar uma abordagem de tentativa e erro que combine conhecimento do domínio de aplicação com técnicas recomendadas e otimizações específicas do modelo.

O Jupyter Notebook que acompanha esta lição oferece um ambiente _sandbox_ onde você pode experimentar o que aprender – durante a lição ou como parte do desafio de código ao final. Para executar os exercícios, você vai precisar de:

1. **Uma chave de API do Azure OpenAI** – o endpoint do serviço para um LLM implantado.
2. **Um ambiente Python** – onde o Notebook possa ser executado.
3. **Variáveis de ambiente locais** – _complete agora os passos do [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) para se preparar_.

O notebook já vem com exercícios _iniciais_ – mas você é incentivado a adicionar suas próprias seções de _Markdown_ (descrição) e _Código_ (requisições de prompt) para testar mais exemplos ou ideias – e desenvolver sua intuição para o design de prompts.

## Guia Ilustrado

Quer ter uma visão geral do que esta lição cobre antes de começar? Confira este guia ilustrado, que mostra os principais tópicos abordados e os pontos-chave para você refletir em cada um deles. O roteiro da lição leva você do entendimento dos conceitos e desafios centrais até como abordá-los com técnicas e boas práticas relevantes de engenharia de prompt. Note que a seção "Técnicas Avançadas" neste guia se refere ao conteúdo que será abordado no _próximo_ capítulo deste curso.

![Guia Ilustrado de Engenharia de Prompt](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.br.png)

## Nossa Startup

Agora, vamos falar sobre como _este tema_ se relaciona com a missão da nossa startup de [levar inovação em IA para a educação](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicações de _aprendizagem personalizada_ com IA – então vamos pensar em como diferentes usuários do nosso aplicativo podem "criar" prompts:

- **Administradores** podem pedir para a IA _analisar dados do currículo para identificar lacunas de cobertura_. A IA pode resumir os resultados ou visualizá-los com código.
- **Educadores** podem pedir para a IA _gerar um plano de aula para um público e tema específicos_. A IA pode montar o plano personalizado em um formato definido.
- **Estudantes** podem pedir para a IA _ajudá-los em uma matéria difícil_. A IA pode orientar os alunos com aulas, dicas e exemplos adaptados ao seu nível.

Isso é só o começo. Confira o [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – uma biblioteca open-source de prompts curada por especialistas em educação – para ter uma ideia mais ampla das possibilidades! _Experimente rodar alguns desses prompts no sandbox ou usando o OpenAI Playground para ver o que acontece!_

<!--
MODELO DE LIÇÃO:
Esta unidade deve cobrir o conceito central #1.
Reforce o conceito com exemplos e referências.

CONCEITO #1:
Engenharia de Prompt.
Defina e explique por que ela é necessária.
-->

## O que é Engenharia de Prompt?

Começamos esta lição definindo **Engenharia de Prompt** como o processo de _criar e otimizar_ entradas de texto (prompts) para entregar respostas consistentes e de qualidade (completions) para um determinado objetivo de aplicação e modelo. Podemos pensar nisso como um processo em 2 etapas:

- _criar_ o prompt inicial para um modelo e objetivo específicos
- _refinar_ o prompt de forma iterativa para melhorar a qualidade da resposta

Esse é necessariamente um processo de tentativa e erro que exige intuição e esforço do usuário para obter os melhores resultados. Mas por que isso é importante? Para responder a essa pergunta, primeiro precisamos entender três conceitos:

- _Tokenização_ = como o modelo "enxerga" o prompt
- _LLMs Base_ = como o modelo de base "processa" um prompt
- _LLMs Ajustados por Instrução_ = como o modelo agora pode ver "tarefas"

### Tokenização

Um LLM enxerga prompts como uma _sequência de tokens_, onde diferentes modelos (ou versões de um modelo) podem tokenizar o mesmo prompt de maneiras diferentes. Como os LLMs são treinados em tokens (e não no texto bruto), a forma como os prompts são tokenizados tem impacto direto na qualidade da resposta gerada.

Para entender como a tokenização funciona, experimente ferramentas como o [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abaixo. Cole seu prompt e veja como ele é convertido em tokens, prestando atenção em como espaços em branco e pontuações são tratados. Note que este exemplo mostra um LLM mais antigo (GPT-3) – então testar com um modelo mais novo pode gerar um resultado diferente.

![Tokenização](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.br.png)

### Conceito: Modelos de Base

Depois que um prompt é tokenizado, a principal função do ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (ou modelo de base) é prever o próximo token nessa sequência. Como os LLMs são treinados em grandes volumes de texto, eles têm uma boa noção das relações estatísticas entre tokens e conseguem fazer essa previsão com certa confiança. Note que eles não entendem o _significado_ das palavras no prompt ou token; eles apenas enxergam um padrão que podem "completar" com a próxima previsão. Eles podem continuar prevendo a sequência até serem interrompidos pelo usuário ou por alguma condição pré-estabelecida.

Quer ver como funciona a conclusão baseada em prompt? Insira o prompt acima no [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) do Azure OpenAI Studio com as configurações padrão. O sistema está configurado para tratar prompts como solicitações de informação – então você deve ver uma resposta que atenda a esse contexto.

Mas e se o usuário quiser ver algo específico que atenda a certos critérios ou objetivos de tarefa? É aí que entram os LLMs _ajustados por instrução_.

![Conclusão de Chat com LLM Base](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.br.png)

### Conceito: LLMs Ajustados por Instrução

Um [LLM Ajustado por Instrução](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) parte do modelo de base e o ajusta com exemplos ou pares de entrada/saída (por exemplo, "mensagens" de múltiplas rodadas) que podem conter instruções claras – e a resposta da IA tenta seguir essa instrução.

Isso usa técnicas como Aprendizado por Reforço com Feedback Humano (RLHF), que treinam o modelo para _seguir instruções_ e _aprender com feedback_, de modo que ele produza respostas mais adequadas para aplicações práticas e mais relevantes para os objetivos do usuário.

Vamos testar – volte ao prompt acima, mas agora altere a _mensagem do sistema_ para fornecer a seguinte instrução como contexto:

> _Resuma o conteúdo fornecido para um aluno do segundo ano. Mantenha o resultado em um parágrafo com 3-5 tópicos em bullet points._

Veja como o resultado agora está ajustado para refletir o objetivo e formato desejados? Um educador pode usar essa resposta diretamente em seus slides para aquela turma.

![Conclusão de Chat com LLM Ajustado por Instrução](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.br.png)

## Por que precisamos de Engenharia de Prompt?

Agora que sabemos como os prompts são processados pelos LLMs, vamos falar sobre _por que_ precisamos de engenharia de prompt. A resposta está no fato de que os LLMs atuais apresentam vários desafios que tornam _completions confiáveis e consistentes_ mais difíceis de alcançar sem investir na construção e otimização dos prompts. Por exemplo:

1. **As respostas dos modelos são estocásticas.** O _mesmo prompt_ provavelmente vai gerar respostas diferentes em modelos ou versões de modelos diferentes. E pode até gerar resultados diferentes com o _mesmo modelo_ em momentos distintos. _Técnicas de engenharia de prompt podem nos ajudar a minimizar essas variações fornecendo melhores direcionamentos_.

1. **Modelos podem fabricar respostas.** Os modelos são pré-treinados com conjuntos de dados _grandes, mas finitos_, o que significa que não têm conhecimento sobre conceitos fora desse escopo de treinamento. Como resultado, podem gerar respostas imprecisas, inventadas ou até contraditórias com fatos conhecidos. _Técnicas de engenharia de prompt ajudam os usuários a identificar e mitigar essas fabricações, por exemplo, pedindo citações ou justificativas para a IA_.

1. **As capacidades dos modelos vão variar.** Modelos mais novos ou gerações diferentes terão mais recursos, mas também trazem peculiaridades e trade-offs em custo e complexidade. _A engenharia de prompt pode nos ajudar a desenvolver boas práticas e fluxos de trabalho que abstraem diferenças e se adaptam a requisitos específicos de cada modelo de forma escalável e fluida_.

Vamos ver isso na prática no OpenAI ou Azure OpenAI Playground:

- Use o mesmo prompt com diferentes implantações de LLM (por exemplo, OpenAI, Azure OpenAI, Hugging Face) – você percebeu as variações?
- Use o mesmo prompt repetidamente com a _mesma_ implantação de LLM (por exemplo, Azure OpenAI playground) – como essas variações se comportaram?

### Exemplo de Fabricação

Neste curso, usamos o termo **"fabricação"** para nos referirmos ao fenômeno em que LLMs às vezes geram informações factualmente incorretas devido a limitações no treinamento ou outras restrições. Você também pode ter ouvido esse fenômeno ser chamado de _"alucinação"_ em artigos ou pesquisas. No entanto, recomendamos fortemente o uso do termo _"fabricação"_ para evitar atribuir características humanas a um resultado gerado por máquina. Isso também reforça as [diretrizes de IA Responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) do ponto de vista da terminologia, eliminando termos que podem ser considerados ofensivos ou não inclusivos em alguns contextos.

Quer entender como funcionam as fabricações? Pense em um prompt que instrua a IA a gerar conteúdo sobre um tema inexistente (para garantir que não esteja no conjunto de treinamento). Por exemplo – eu tentei este prompt:
> **Prompt:** crie um plano de aula sobre a Guerra Marciana de 2076.

# Plano de Aula: A Guerra Marciana de 2076

## Objetivo da Aula

Explorar os principais eventos, causas e consequências da Guerra Marciana de 2076, incentivando os alunos a analisar o impacto desse conflito na história interplanetária.

## Materiais Necessários

- Quadro branco e marcadores
- Projetor ou tela para apresentação
- Cópias do artigo “A Guerra Marciana de 2076: Uma Visão Geral”
- Folhas para anotações

## Introdução (15 minutos)

- Apresente o contexto histórico: colonização de Marte, tensões entre colônias terrestres e marcianas.
- Explique brevemente o que foi a Guerra Marciana de 2076.
- Pergunte aos alunos o que eles já sabem sobre conflitos interplanetários.

## Desenvolvimento (30 minutos)

### 1. Causas da Guerra

- Discuta os principais motivos que levaram ao conflito, como disputas por recursos, autonomia política e avanços tecnológicos.
- Analise os interesses das diferentes facções envolvidas.

### 2. Principais Eventos

- Apresente uma linha do tempo dos acontecimentos mais importantes durante a guerra.
- Destaque batalhas decisivas, tratados e mudanças de liderança.

### 3. Consequências

- Explore os efeitos da guerra para Marte, Terra e outras colônias.
- Debata as mudanças sociais, políticas e tecnológicas resultantes do conflito.

## Atividade em Grupo (20 minutos)

- Divida a turma em grupos e peça que cada um analise um aspecto da guerra (causas, eventos ou consequências).
- Cada grupo deve apresentar suas conclusões para a classe.

## Discussão e Reflexão (15 minutos)

- Promova um debate sobre como a Guerra Marciana de 2076 influenciou as relações interplanetárias.
- Incentive os alunos a pensar em possíveis paralelos com conflitos históricos da Terra.

## Avaliação

- Solicite uma redação curta sobre o impacto da Guerra Marciana de 2076 na sociedade marciana.
- Avalie a participação nas discussões e apresentações em grupo.

## Encerramento

- Recapitule os principais pontos da aula.
- Indique leituras complementares sobre história interplanetária e conflitos futuros.
Uma pesquisa na web mostrou que existem relatos fictícios (por exemplo, séries de TV ou livros) sobre guerras em Marte – mas nenhum em 2076. O bom senso também nos diz que 2076 está _no futuro_ e, portanto, não pode estar associado a um evento real.

Então, o que acontece quando executamos esse prompt com diferentes provedores de LLM?

> **Resposta 1**: OpenAI Playground (GPT-35)

![Resposta 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.br.png)

> **Resposta 2**: Azure OpenAI Playground (GPT-35)

![Resposta 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.br.png)

> **Resposta 3**: : Hugging Face Chat Playground (LLama-2)

![Resposta 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.br.png)

Como esperado, cada modelo (ou versão do modelo) produz respostas um pouco diferentes devido ao comportamento estocástico e variações de capacidade. Por exemplo, um modelo direciona a resposta para um público de 8ª série, enquanto outro assume um estudante do ensino médio. Mas todos os três modelos geraram respostas que poderiam convencer um usuário desinformado de que o evento era real.

Técnicas de engenharia de prompt como _metaprompting_ e _configuração de temperatura_ podem reduzir as fabricações do modelo até certo ponto. Novas _arquiteturas_ de engenharia de prompt também incorporam novas ferramentas e técnicas de forma transparente no fluxo do prompt, para mitigar ou reduzir alguns desses efeitos.

## Estudo de Caso: GitHub Copilot

Vamos encerrar esta seção entendendo como a engenharia de prompt é usada em soluções do mundo real, analisando um Estudo de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

O GitHub Copilot é seu "par de programação com IA" – ele converte prompts de texto em sugestões de código e é integrado ao seu ambiente de desenvolvimento (por exemplo, Visual Studio Code) para uma experiência fluida. Como documentado na série de blogs abaixo, a versão inicial era baseada no modelo OpenAI Codex – com os engenheiros rapidamente percebendo a necessidade de ajustar o modelo e desenvolver melhores técnicas de engenharia de prompt para melhorar a qualidade do código. Em julho, eles [lançaram um modelo de IA aprimorado que vai além do Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugestões ainda mais rápidas.

Leia as postagens na ordem para acompanhar a jornada de aprendizado deles.

- **Maio 2023** | [O GitHub Copilot está ficando melhor em entender seu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maio 2023** | [Por dentro do GitHub: Trabalhando com os LLMs por trás do GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Como escrever prompts melhores para o GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot vai além do Codex com modelo de IA aprimorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Guia do desenvolvedor para engenharia de prompt e LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Set 2023** | [Como construir um app empresarial com LLM: Lições do GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Você também pode navegar pelo [blog de Engenharia](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) deles para mais postagens como [esta aqui](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que mostra como esses modelos e técnicas são _aplicados_ para impulsionar aplicações reais.

---

## Construção de Prompts

Já vimos por que a engenharia de prompt é importante – agora vamos entender como os prompts são _construídos_ para que possamos avaliar diferentes técnicas para um design de prompt mais eficaz.

### Prompt Básico

Vamos começar com o prompt básico: uma entrada de texto enviada ao modelo sem nenhum outro contexto. Veja um exemplo – quando enviamos as primeiras palavras do hino nacional dos EUA para a [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) da OpenAI, ela imediatamente _completa_ a resposta com as próximas linhas, ilustrando o comportamento básico de previsão.

| Prompt (Entrada)     | Completamento (Saída)                                                                                                                        |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see   | Parece que você está começando a letra de "The Star-Spangled Banner", o hino nacional dos Estados Unidos. A letra completa é ...             |

### Prompt Complexo

Agora vamos adicionar contexto e instruções a esse prompt básico. A [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) permite construir um prompt complexo como uma coleção de _mensagens_ com:

- Pares de entrada/saída refletindo a entrada do _usuário_ e a resposta do _assistente_.
- Mensagem de sistema definindo o contexto para o comportamento ou personalidade do assistente.

A requisição agora tem o formato abaixo, onde a _tokenização_ captura efetivamente as informações relevantes do contexto e da conversa. Agora, mudar o contexto do sistema pode impactar tanto a qualidade das respostas quanto as entradas fornecidas pelo usuário.

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

Nos exemplos acima, o prompt do usuário era uma consulta de texto simples que pode ser interpretada como um pedido de informação. Com prompts de _instrução_, podemos usar esse texto para especificar uma tarefa com mais detalhes, fornecendo uma orientação melhor para a IA. Veja um exemplo:

| Prompt (Entrada)                                                                                                                                                                                                                         | Completamento (Saída)                                                                                                        | Tipo de Instrução   |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Escreva uma descrição da Guerra Civil                                                                                                                                                                                                   | _retornou um parágrafo simples_                                                                                              | Simples             |
| Escreva uma descrição da Guerra Civil. Forneça datas e eventos importantes e descreva sua importância                                                                                             | _retornou um parágrafo seguido de uma lista de datas de eventos importantes com descrições_                                  | Complexa            |
| Escreva uma descrição da Guerra Civil em 1 parágrafo. Forneça 3 tópicos com datas importantes e sua importância. Forneça mais 3 tópicos com figuras históricas e suas contribuições. Retorne a saída como um arquivo JSON                | _retorna detalhes mais extensos em uma caixa de texto, formatados como JSON que você pode copiar e validar conforme necessário_ | Complexa. Formatada.|

## Conteúdo Primário

Nos exemplos acima, o prompt ainda era bastante aberto, permitindo que o LLM decidisse qual parte do seu conjunto de dados pré-treinado era relevante. Com o padrão de design de _conteúdo primário_, o texto de entrada é dividido em duas partes:

- uma instrução (ação)
- conteúdo relevante (que influencia a ação)

Veja um exemplo onde a instrução é "resuma isso em 2 frases".

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completamento (Saída)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa de um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e é conhecido pelas civilizações antigas desde antes da história registrada. Ele recebe o nome do deus romano Júpiter.[19] Quando visto da Terra, Júpiter pode ser brilhante o suficiente para que sua luz refletida projete sombras visíveis,[20] e é em média o terceiro objeto natural mais brilhante no céu noturno depois da Lua e de Vênus. <br/> **Resuma isso em 2 frases curtas** | Júpiter, o quinto planeta a partir do Sol, é o maior do Sistema Solar e é conhecido por ser um dos objetos mais brilhantes no céu noturno. Nomeado em homenagem ao deus romano Júpiter, é um gigante gasoso cuja massa é duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. |

O segmento de conteúdo primário pode ser usado de várias formas para gerar instruções mais eficazes:

- **Exemplos** – em vez de dizer explicitamente ao modelo o que fazer, forneça exemplos do que fazer e deixe-o inferir o padrão.
- **Cues (Dicas)** – siga a instrução com uma "dica" que prepara a resposta, guiando o modelo para respostas mais relevantes.
- **Templates (Modelos)** – são 'receitas' repetíveis de prompts com espaços reservados (variáveis) que podem ser personalizados com dados para casos de uso específicos.

Vamos explorar essas abordagens na prática.

### Usando Exemplos

Essa é uma abordagem em que você usa o conteúdo primário para "alimentar o modelo" com exemplos do resultado desejado para uma determinada instrução, e deixa que ele infira o padrão para a saída desejada. Dependendo do número de exemplos fornecidos, podemos ter prompting zero-shot, one-shot, few-shot etc.

O prompt agora consiste em três componentes:

- Uma descrição da tarefa
- Alguns exemplos do resultado desejado
- O início de um novo exemplo (que se torna uma descrição implícita da tarefa)

| Tipo de Aprendizado | Prompt (Entrada)                                                                                                                                        | Completamento (Saída)         |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------- |
| Zero-shot           | "The Sun is Shining". Translate to Spanish                                                                                                              | "El Sol está brillando".      |
| One-shot            | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                   | "Es un día frío y ventoso".   |
| Few-shot            | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk =>   | Basketball                    |
|                     |                                                                                                                                                         |                               |

Note como tivemos que fornecer uma instrução explícita ("Translate to Spanish") no prompting zero-shot, mas ela é inferida no exemplo one-shot. O exemplo few-shot mostra como adicionar mais exemplos permite que os modelos façam inferências mais precisas sem instruções adicionais.

### Dicas no Prompt (Prompt Cues)

Outra técnica para usar o conteúdo primário é fornecer _dicas_ em vez de exemplos. Nesse caso, estamos dando ao modelo um empurrão na direção certa _começando_ com um trecho que reflete o formato de resposta desejado. O modelo então "pega a dica" e continua nesse estilo.

| Número de Dicas | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completamento (Saída)                                                                                                                                                                                                                                                                                       |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0               | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa de um milésimo da do Sol, mas duas vezes e meia a de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e é conhecido pelas civilizações antigas desde antes da história registrada.

**Resuma Isso**                                       | Júpiter é o maior planeta do nosso Sistema Solar e o quinto a partir do Sol. É um gigante gasoso com uma massa equivalente a 1/1000 da massa do Sol, mas é mais pesado que todos os outros planetas juntos. Civilizações antigas já conheciam Júpiter há muito tempo, e ele é facilmente visível no céu noturno. |
| 1              | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da massa do Sol, mas duas vezes e meia a massa de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e é conhecido pelas civilizações antigas desde antes da história registrada. <br/>**Resuma Isso** <br/> O que aprendemos é que Júpiter | é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da massa do Sol, mas duas vezes e meia a massa de todos os outros planetas juntos. É facilmente visível a olho nu e conhecido desde os tempos antigos.                        |
| 2              | Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. É um gigante gasoso com uma massa equivalente a um milésimo da massa do Sol, mas duas vezes e meia a massa de todos os outros planetas do Sistema Solar juntos. Júpiter é um dos objetos mais brilhantes visíveis a olho nu no céu noturno, e é conhecido pelas civilizações antigas desde antes da história registrada. <br/>**Resuma Isso** <br/> Top 3 Fatos Que Aprendemos:         | 1. Júpiter é o quinto planeta a partir do Sol e o maior do Sistema Solar. <br/> 2. É um gigante gasoso com uma massa equivalente a um milésimo da massa do Sol...<br/> 3. Júpiter é visível a olho nu desde os tempos antigos ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Modelos de Prompt

Um modelo de prompt é uma _receita pré-definida para um prompt_ que pode ser armazenada e reutilizada conforme necessário, para garantir experiências de usuário mais consistentes em escala. Na forma mais simples, é apenas uma coleção de exemplos de prompt como [este da OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) que fornece tanto os componentes interativos do prompt (mensagens de usuário e sistema) quanto o formato de requisição via API - para facilitar a reutilização.

Em uma forma mais avançada, como [este exemplo da LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), ele contém _espaços reservados_ que podem ser substituídos por dados de várias fontes (entrada do usuário, contexto do sistema, fontes externas de dados etc.) para gerar um prompt de forma dinâmica. Isso permite criar uma biblioteca de prompts reutilizáveis que podem ser usados para garantir experiências de usuário consistentes **programaticamente** em escala.

Por fim, o verdadeiro valor dos modelos está na capacidade de criar e publicar _bibliotecas de prompts_ para domínios de aplicação específicos - onde o modelo de prompt é _otimizado_ para refletir o contexto ou exemplos do aplicativo, tornando as respostas mais relevantes e precisas para o público-alvo. O repositório [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) é um ótimo exemplo dessa abordagem, reunindo uma biblioteca de prompts para o setor educacional com foco em objetivos como planejamento de aulas, elaboração de currículo, tutoria de alunos etc.

## Conteúdo de Apoio

Se pensarmos na construção de prompts como tendo uma instrução (tarefa) e um alvo (conteúdo principal), então o _conteúdo secundário_ é como um contexto adicional que fornecemos para **influenciar a saída de alguma forma**. Pode ser parâmetros de ajuste, instruções de formatação, taxonomias de tópicos etc. que ajudam o modelo a _personalizar_ sua resposta para atender aos objetivos ou expectativas do usuário.

Por exemplo: Dado um catálogo de cursos com metadados extensos (nome, descrição, nível, tags, instrutor etc.) sobre todos os cursos disponíveis no currículo:

- podemos definir uma instrução para "resumir o catálogo de cursos para o semestre de Outono de 2023"
- podemos usar o conteúdo principal para fornecer alguns exemplos do formato desejado
- podemos usar o conteúdo secundário para identificar as 5 principais "tags" de interesse.

Assim, o modelo pode fornecer um resumo no formato mostrado pelos exemplos - mas se um resultado tiver várias tags, ele pode priorizar as 5 tags identificadas no conteúdo secundário.

---

<!--
MODELO DE LIÇÃO:
Esta unidade deve abordar o conceito central #1.
Reforce o conceito com exemplos e referências.

CONCEITO #3:
Técnicas de Engenharia de Prompt.
Quais são algumas técnicas básicas de engenharia de prompt?
Ilustre com alguns exercícios.
-->

## Melhores Práticas de Prompt

Agora que sabemos como prompts podem ser _construídos_, podemos começar a pensar em como _desenhá-los_ para refletir as melhores práticas. Podemos pensar nisso em duas partes - ter a _mentalidade_ certa e aplicar as _técnicas_ corretas.

### Mentalidade de Engenharia de Prompt

Engenharia de Prompt é um processo de tentativa e erro, então mantenha três fatores amplos em mente:

1. **Entendimento do Domínio é Importante.** A precisão e relevância da resposta dependem do _domínio_ em que o aplicativo ou usuário opera. Use sua intuição e experiência para **personalizar técnicas**. Por exemplo, defina _personalidades específicas do domínio_ nos prompts de sistema, ou use _modelos específicos do domínio_ nos prompts de usuário. Forneça conteúdo secundário que reflita contextos do domínio, ou use _dicas e exemplos específicos_ para guiar o modelo para padrões de uso familiares.

2. **Entendimento do Modelo é Importante.** Sabemos que os modelos são estocásticos por natureza. Mas as implementações também podem variar quanto ao conjunto de dados de treinamento (conhecimento pré-treinado), às capacidades oferecidas (por exemplo, via API ou SDK) e ao tipo de conteúdo para o qual são otimizados (código, imagens, texto etc.). Entenda os pontos fortes e limitações do modelo que está usando, e use esse conhecimento para _priorizar tarefas_ ou criar _modelos personalizados_ otimizados para as capacidades do modelo.

3. **Iteração & Validação são Importantes.** Os modelos estão evoluindo rapidamente, assim como as técnicas de engenharia de prompt. Como especialista no domínio, você pode ter outros contextos ou critérios para _sua_ aplicação específica, que talvez não se apliquem à comunidade em geral. Use ferramentas e técnicas de engenharia de prompt para "dar o pontapé inicial" na construção do prompt, depois itere e valide os resultados usando sua própria intuição e experiência. Registre seus aprendizados e crie uma **base de conhecimento** (por exemplo, bibliotecas de prompts) que possa ser usada como novo ponto de partida por outros, acelerando futuras iterações.

## Melhores Práticas

Agora vamos ver algumas práticas recomendadas por profissionais da [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| O quê                              | Por quê                                                                                                                                                                                                                                               |
| :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avalie os modelos mais recentes.   | Novas gerações de modelos tendem a ter recursos e qualidade aprimorados - mas podem ter custos maiores. Avalie o impacto e decida sobre migração.                                                                                                     |
| Separe instruções e contexto       | Verifique se seu modelo/provedor define _delimitadores_ para distinguir instruções, conteúdo principal e secundário de forma mais clara. Isso pode ajudar o modelo a atribuir pesos mais precisos aos tokens.                                         |
| Seja específico e claro            | Dê mais detalhes sobre o contexto desejado, resultado, tamanho, formato, estilo etc. Isso melhora tanto a qualidade quanto a consistência das respostas. Capture receitas em modelos reutilizáveis.                                                   |
| Seja descritivo, use exemplos      | Os modelos podem responder melhor a uma abordagem de "mostrar e contar". Comece com uma abordagem `zero-shot` (só instrução, sem exemplos) e depois tente `few-shot` como refinamento, fornecendo alguns exemplos do resultado desejado. Use analogias. |
| Use dicas para iniciar respostas   | Direcione para o resultado desejado dando algumas palavras ou frases iniciais que o modelo pode usar como ponto de partida para a resposta.                                                                                                            |
| Reforce instruções                 | Às vezes é preciso repetir para o modelo. Dê instruções antes e depois do conteúdo principal, use instrução e dica, etc. Itere e valide para ver o que funciona.                                                                                      |
| A ordem importa                    | A ordem em que você apresenta as informações ao modelo pode impactar a saída, até nos exemplos de aprendizado, devido ao viés de recência. Teste diferentes opções para ver o que funciona melhor.                                                    |
| Dê uma “saída” ao modelo           | Dê ao modelo uma resposta de _fallback_ que ele pode fornecer se não conseguir completar a tarefa por algum motivo. Isso pode reduzir as chances de respostas falsas ou inventadas.                                                                  |
|                                   |                                                                                                                                                                                                                                                      |

Como toda boa prática, lembre-se que _os resultados podem variar_ dependendo do modelo, da tarefa e do domínio. Use essas dicas como ponto de partida e itere para encontrar o que funciona melhor para você. Reavalie constantemente seu processo de engenharia de prompt conforme novos modelos e ferramentas surgem, focando em escalabilidade e qualidade das respostas.

<!--
MODELO DE LIÇÃO:
Esta unidade deve propor um desafio de código, se aplicável

DESAFIO:
Link para um Jupyter Notebook com apenas os comentários de código nas instruções (seções de código estão vazias).

SOLUÇÃO:
Link para uma cópia desse Notebook com os prompts preenchidos e executados, mostrando um exemplo de saída.
-->

## Atividade

Parabéns! Você chegou ao final da lição! Agora é hora de colocar alguns desses conceitos e técnicas em prática com exemplos reais!

Para nossa atividade, vamos usar um Jupyter Notebook com exercícios que você pode completar de forma interativa. Você também pode estender o Notebook com suas próprias células de Markdown e Código para explorar ideias e técnicas por conta própria.

### Para começar, faça um fork do repositório, então

- (Recomendado) Inicie o GitHub Codespaces
- (Alternativamente) Clone o repositório para seu dispositivo local e use com Docker Desktop
- (Alternativamente) Abra o Notebook no ambiente de execução de sua preferência.

### Depois, configure suas variáveis de ambiente

- Copie o arquivo `.env.copy` da raiz do repositório para `.env` e preencha os valores de `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT`. Volte à [seção Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) para aprender como.

### Em seguida, abra o Jupyter Notebook

- Selecione o kernel de execução. Se estiver usando as opções 1 ou 2, basta selecionar o kernel padrão Python 3.10.x fornecido pelo dev container.

Pronto! Agora é só rodar os exercícios. Lembre-se que não há respostas _certas ou erradas_ aqui - o objetivo é explorar opções por tentativa e erro e construir intuição sobre o que funciona para cada modelo e domínio de aplicação.

_Por isso, não há segmentos de Solução de Código nesta lição. Em vez disso, o Notebook terá células de Markdown intituladas "Minha Solução:" mostrando um exemplo de saída para referência._

 <!--
MODELO DE LIÇÃO:
Encerre a seção com um resumo e recursos para autoaprendizagem.
-->

## Checagem de Conhecimento

Qual dos prompts abaixo segue boas práticas recomendadas?

1. Mostre uma imagem de carro vermelho
2. Mostre uma imagem de carro vermelho da marca Volvo e modelo XC90 estacionado perto de um penhasco com o sol se pondo
3. Mostre uma imagem de carro vermelho da marca Volvo e modelo XC90

A: 2, é o melhor prompt pois traz detalhes sobre "o quê" e vai além (não é qualquer carro, mas uma marca e modelo específicos) e também descreve o cenário. O 3 é o próximo melhor, pois também contém bastante descrição.

## 🚀 Desafio

Veja se você consegue usar a técnica de "dica" com o prompt: Complete a frase "Mostre uma imagem de carro vermelho da marca Volvo e ". O que o modelo responde, e como você melhoraria isso?

## Muito Bem! Continue Aprendendo

Quer aprender mais sobre diferentes conceitos de Engenharia de Prompt? Acesse a [página de aprendizado contínuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre o tema.

Vá para a Lição 5 onde veremos [técnicas avançadas de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.