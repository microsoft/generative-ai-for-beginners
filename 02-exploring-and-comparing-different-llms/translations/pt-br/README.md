# Explorando e comparando diferentes LLMs

[![Exploring and comparing different LLMs](../../images/02-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson2-gh?WT.mc_id=academic-105485-koreystt)

> _Clique na imagem acima para ver o vídeo desta lição_

Na lição anterior, vimos como a IA generativa está mudando o cenário tecnológico, como os Grandes Modelos de Linguagens (LLMs) funcionam e como uma empresa - como nossa startup - pode aplicá-los aos seus casos de uso e crescer! Neste capítulo, estamos procurando comparar e contrastar diferentes tipos de modelos de linguagem grandes, LLMs para entender seus prós e contras.

O próximo passo na jornada de nossa startup é explorar o cenário atual dos Grandes Modelos de Linguagem (LLMs) e entender quais são adequados para nosso caso de uso.

## Introdução

Esta lição abordará:

- Diferentes tipos de LLMs no cenário atual.
- Testar, iterar e comparar diferentes modelos para seu caso de uso no Azure.
- Como implantar um LLM.

## Objetivos de aprendizagem

Após a conclusão desta lição, você será capaz de:

- Selecionar o modelo certo para seu caso de uso.
- Entender como testar, iterar e melhorar o desempenho do seu modelo.
- Saber como as empresas implantam modelos.

## Entenda diferentes tipos de LLMs

Os Grandes Modelos de Linguagem (LLMs) podem ter várias categorizações com base em sua arquitetura, dados de treinamento e caso de uso. Entender essas diferenças ajudará nossa startup a selecionar o modelo certo para o cenário e entender como testar, iterar e melhorar o desempenho.

Existem muitos tipos diferentes de modelos LLM, sua escolha de modelo depende do que você pretende usá-los, seus dados, quanto você está pronto para pagar e muito mais.

Dependendo se você pretende usar os modelos para geração de texto, áudio, vídeo ou imagem você pode optar por um tipo diferente de modelo.

- **Reconhecimento de áudio e fala**: para esse fim, os modelos do tipo Whisper são uma ótima escolha. Pois são de propósito geral e destinados ao reconhecimento de fala. Ele é treinado em áudio diversificado e pode realizar reconhecimento de fala multilíngue. Saiba mais sobre [modelos do tipo Whisper aqui](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Geração de Imagem**: para geração de imagem, DALL-E e Midjourney são duas escolhas muito conhecidas. DALL-E é oferecido pelo Azure OpenAI. [Leia mais sobre DALL-E aqui](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) e também no Capítulo 9 deste currículo.

- **Geração de texto**: a maioria dos modelos é treinada na geração de texto e você tem uma grande variedade de escolhas, desde GPT-3.5 até GPT-4. Eles vêm a custos diferentes, sendo o GPT-4 o mais caro. Vale a pena dar uma olhada no [Azure Open AI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) para avaliar quais modelos se adequam melhor às suas necessidades em termos de capacidade e custo.

Escolher um modelo significa que você obtém algumas capacidades básicas, que podem não ser suficientes. Muitas vezes, você tem dados específicos da empresa que precisa informar ao LLM. Existem algumas opções diferentes sobre como abordar isso, abordaremos mais sobre isso nas próximas seções.

### Modelos de base versus LLMs

O termo Modelo de Fundação foi [criado por pesquisadores de Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) e definido como um modelo de IA que segue alguns critérios, como:

- **Eles são treinandos usando aprendizado não supervisionado ou aprendizado auto-supervisionado**, o que significa que são treinados em dados multimodais não rotulados e não requerem anotação humana ou rotulagem de dados para seu processo de treinamento.

- **Eles são modelos muito grandes**, baseados em redes neurais muito profundas treinadas em bilhões de parâmetros.

- **Normalmente, eles são destinados a servir como uma ‘base’ para outros modelos**, o que significa que podem ser usados como ponto de partida para outros modelos serem construídos em cima, o que pode ser feito por ajuste fino.

![Foundation Models versus LLMs](../../images/FoundationModel.png?WT.mc_id=academic-105485-koreyst)

Fonte da imagem: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404?WT.mc_id=academic-105485-koreyst)

Para esclarecer ainda mais essa distinção, vamos usar o ChatGPT como exemplo. Para criar a primeira versão do ChatGPT, um modelo chamado GPT-3.5 serviu como modelo fundamental. Isso significa que a OpenAI utilizou alguns dados específicos de conversação para criar uma versão ajustada do GPT-3.5 que foi especializada em se sair bem em cenários de conversação, como chatbots.

![Foundation Model](../../images/Multimodal.png?WT.mc_id=academic-105485-koreyst)

Fonte da imagem: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modelos de Código Aberto versus Modelos Proprietários

Outra maneira de categorizar os Modelos de Linguagem de Grande Escala (LLMs) é se eles são de código aberto ou proprietários.

Os modelos de código aberto são modelos que são disponibilizados ao público e podem ser usados por qualquer pessoa. Eles são frequentemente disponibilizados pela empresa que os criou ou pela comunidade de pesquisa. Esses modelos podem ser inspecionados, modificados e personalizados para diversos casos de uso em LLMs. No entanto, nem sempre são otimizados para uso em produção e podem não ser tão eficientes quanto os modelos proprietários. Além disso, o financiamento para modelos de código aberto pode ser limitado, e eles podem não ser mantidos a longo prazo ou não ser atualizados com as pesquisas mais recentes. Exemplos de modelos de código aberto populares incluem [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://sapling.ai/llm/bloom?WT.mc_id=academic-105485-koreyst) e [LLaMA](https://sapling.ai/llm/llama?WT.mc_id=academic-105485-koreyst).

Os modelos proprietários são modelos de propriedade de uma empresa e não são disponibilizados ao público. Esses modelos são frequentemente otimizados para uso em produção. No entanto, não podem ser inspecionados, modificados ou personalizados para diferentes casos de uso. Além disso, nem sempre estão disponíveis gratuitamente e podem exigir uma assinatura ou pagamento para uso. Além disso, os usuários não têm controle sobre os dados usados para treinar o modelo, o que significa que devem confiar ao proprietário do modelo o compromisso com a privacidade dos dados e o uso responsável da IA. Exemplos de modelos proprietários populares incluem [modelos da OpenAI](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) ou [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Embeddings versus Geração de Imagem versus Geração de Texto e Código

Os LLMs também podem ser categorizados com base na saída que geram.

Os `embeddings` são um conjunto de modelos que podem converter texto em uma forma numérica, chamada `embedding`, que é uma representação numérica do texto de entrada. Os `embeddings` facilitam a compreensão das relações entre palavras ou frases por máquinas e podem ser usadas como entradas por outros modelos, como modelos de classificação ou modelos de agrupamento que têm um melhor desempenho com dados numéricos. Modelos de incorporação são frequentemente usados para aprendizado por transferência, onde um modelo é construído para uma tarefa substituta para a qual há uma abundância de dados, e em seguida, os pesos do modelo (`embeddings`) são reutilizados para outras tarefas subsequentes. Um exemplo desta categoria é [Embeddings no OpenAI](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../images/Embedding.png?WT.mc_id=academic-105485-koreyst)

Modelos de geração de imagem são modelos que geram imagens. Esses modelos são frequentemente usados para edição de imagens, síntese de imagens e tradução de imagens. Modelos de geração de imagem são frequentemente treinados em grandes conjuntos de dados de imagens, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar novas imagens ou editar imagens existentes com técnicas de inpainting, super-resolução e colorização. Exemplos incluem [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) e [modelos do Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Image Generation](../../images/Image.png?WT.mc_id=academic-105485-koreyst)

Modelos de geração de texto e código são modelos que geram texto ou código. Esses modelos são frequentemente usados para resumir texto, traduzir e responder a perguntas. Modelos de geração de texto são frequentemente treinados em grandes conjuntos de dados de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar novo texto ou responder a perguntas. Modelos de geração de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), são frequentemente treinados em grandes conjuntos de dados de código, como o GitHub, e podem ser usados para gerar novo código ou corrigir bugs em código existente.

![Text and code generation](../../images/Text.png?WT.mc_id=academic-105485-koreyst)

### Encoder-Decoder versus Decoder-only

Para falar sobre os diferentes tipos de arquiteturas de Grandes Modelos de Linguagem (LLMs), vamos usar uma analogia.

Imagine que seu gerente te deu uma tarefa de escrever um questionário para os alunos. Você tem dois colegas; um supervisiona a criação do conteúdo e o outro supervisiona a revisão.

O criador de conteúdo é como um modelo somente `Decoder`, ele pode olhar para o tópico e ver o que você já escreveu e então ele pode escrever um curso com base nisso. Eles são muito bons em escrever conteúdo envolvente e informativo, mas não são muito bons em entender o tópico e os objetivos de aprendizado. Alguns exemplos de modelos Decodificadores são os modelos da família GPT, como o GPT-3.

O revisor é como um modelo somente `Encoder`, eles olham para o curso escrito e as respostas, percebendo a relação entre eles e entendendo o contexto, mas não são bons em gerar conteúdo. Um exemplo de modelo somente Codificador seria o BERT.

Imagine que também podemos ter alguém que possa criar e revisar o questionário, este é um modelo `Encoder-Decoder`. Alguns exemplos seriam `BART` e `T5`.

### Serviço versus Modelo

Agora, vamos falar sobre a diferença entre um serviço e um modelo. Um serviço é um produto oferecido por um Provedor de Serviços em Nuvem e é frequentemente uma combinação de modelos, dados e outros componentes. Um modelo é o componente central de um serviço e é frequentemente um modelo fundamental, como um LLM.

Os serviços são frequentemente otimizados para uso em produção e muitas vezes são mais fáceis de usar do que os modelos, por meio de uma interface gráfica de usuário. No entanto, os serviços nem sempre estão disponíveis gratuitamente e podem exigir uma assinatura ou pagamento para uso, em troca de aproveitar os recursos e equipamentos do proprietário do serviço, otimizando despesas e escalando facilmente. Um exemplo de serviço é o [Serviço do Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), que oferece um plano de tarifas pay-as-you-go, o que significa que os usuários são cobrados de acordo com o quanto usam o serviço. Além disso, o serviço do Azure OpenAI oferece segurança de nível empresarial e um framework de IA responsável sobre as capacidades dos modelos.

Os modelos são apenas as Redes Neurais, com parâmetros, pesos e outros. Isso permite que as empresas os executem localmente. No entanto, elas precisariam comprar equipamentos, criar uma estrutura para escalar e adquirir uma licença ou usar um modelo de código aberto. Um modelo como o `LLaMA` está disponível para uso, exigindo poder computacional para executar o modelo.

## Como testar e iterar com diferentes modelos para entender o desempenho no Azure

Depois que nossa equipe explorou o cenário atual dos LLMs e identificou alguns bons candidatos para seus cenários, o próximo passo é testá-los em seus dados e carga de trabalho. Isso é um processo iterativo, feito por meio de experimentos e medições.
A maioria dos modelos mencionados nos parágrafos anteriores (modelos da OpenAI, modelos de código aberto como `Llama2` e `Hugging Face transformers`) está disponível no [Foundation Models](https://learn.microsoft.com/azure/machine-learning/concept-foundation-models?WT.mc_id=academic-105485-koreyst) no [Azure Machine Learning studio](https://ml.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure Machine Learning](https://azure.microsoft.com/products/machine-learning/?WT.mc_id=academic-105485-koreyst) é um serviço em nuvem projetado para Cientistas de Dados e Engenheiros de Machine Learning que gerenciam o ciclo completo de Aprendizado de Máquina (treinamento, teste, implantação e gerenciamento de MLOps) em uma única plataforma. O Machine Learning Studio oferece uma interface gráfica de usuário para este serviço e permite ao usuário:

- Encontrar o Foundation Model de interesse no catálogo, filtrando por tarefa, licença ou nome. Também é possível importar novos modelos que ainda não estejam incluídos no catálogo.
- Analisar o cartão do modelo, incluindo uma descrição detalhada e exemplos de código, e testá-lo com o widget de Inferência de Amostra, fornecendo um prompt de amostra para testar o resultado.

![Cartão do Modelo](../../images/Llama1.png?WT.mc_id=academic-105485-koreyst)

- Avaliar o desempenho do modelo com métricas de avaliação objetivas em uma carga de trabalho específica e um conjunto de dados específico fornecido como entrada.

![Avaliação do Modelo](../../images/Llama2.png?WT.mc_id=academic-105485-koreyst)

- Ajustar o modelo com dados de treinamento personalizados para melhorar o desempenho do modelo em uma carga de trabalho específica, aproveitando as capacidades de experimentação e rastreamento do Aprendizado de Máquina do Azure.

![Ajuste do Modelo](../../images/Llama3.png?WT.mc_id=academic-105485-koreyst)

- Implante o modelo pré-treinado original ou a versão ajustada a um ponto de extremidade remoto em tempo real ou por lote, para permitir que aplicativos o consumam.

![Implantação do Modelo](../../images/Llama4.png?WT.mc_id=academic-105485-koreyst)

## Melhorando os Resultados dos LLMs

Exploramos com nossa equipe de startup diferentes tipos de Modelos de Linguagem de Grande Escala (LLMs) e uma Plataforma em Nuvem (Azure Machine Learning) que nos permite comparar diferentes modelos, avaliá-los em dados de teste, melhorar o desempenho e implantá-los em pontos de extremidade de inferência.

Mas quando eles devem considerar o ajuste fino de um modelo em vez de usar um pré-treinado? Existem outras abordagens para melhorar o desempenho do modelo em cargas de trabalho específicas?

Existem várias abordagens que uma empresa pode usar para obter os resultados desejados de um LLM, você pode selecionar diferentes tipos de modelos com diferentes graus de treinamento.

Implantar um LLM em produção, com diferentes níveis de complexidade, custo e qualidade. Aqui estão algumas abordagens diferentes:

- **Engenharia de prompts com contexto**: a ideia é fornecer contexto suficiente ao formular o prompt para garantir que você obtenha as respostas de que precisa.

- **Geração Aprimorada com Recuperação, RAG**: seus dados podem existir em um banco de dados ou ponto de extremidade da web, por exemplo. Para garantir que esses dados, ou um subconjunto deles, estejam incluídos no momento do prompt, você pode buscar os dados relevantes e torná-los parte do prompt do usuário.

- **Modelo ajustado fino**: nesse caso, você treinou o modelo ainda mais com seus próprios dados, o que torna o modelo mais preciso e responsivo às suas necessidades, mas pode ser custoso.

![Implantação de LLMs](../../images/Deploy.png?WT.mc_id=academic-105485-koreyst)

Fonte da imagem: [Quatro Maneiras de Empresas Implatarem LLMs | Blog Fiddler AI](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Engenharia de Prompts com Contexto

Os LLMs pré-treinados funcionam muito bem em tarefas de linguagem natural generalizadas, mesmo quando chamados com um prompt curto, como uma frase a ser completada ou uma pergunta - o chamado "aprendizado de zero-shot".

No entanto, quanto mais o usuário puder estruturar sua consulta, com uma solicitação detalhada e exemplos (o Contexto) mais precisa e próxima das expectativas do usuário será a resposta. Nesse caso, falamos de "aprendizado de um único exemplo" se o prompt incluir apenas um exemplo e "aprendizado de alguns exemplos" se incluir vários exemplos.
A Engenharia de Prompts com contexto é a abordagem mais econômica para começar.

### Recuperação de Geração Aumentada (RAG)

Os LLMs têm a limitação de que só podem usar os dados que foram usados durante seu treinamento para gerar uma resposta. Isso significa que eles não sabem nada sobre os fatos que ocorreram após seu processo de treinamento e não podem acessar informações não públicas (como dados de uma empresa).
Isso pode ser superado por meio do `RAG`, uma técnica que amplia o prompt com dados externos na forma de trechos de documentos, considerando limites de comprimento do prompt. Isso é suportado por ferramentas de banco de dados vetoriais (como [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) que recuperam trechos úteis de várias fontes de dados predefinidas e os adicionam ao Contexto do prompt.

Essa técnica é muito útil quando uma empresa não possui dados suficientes, tempo suficiente ou recursos para ajustar finamente um LLM, mas ainda deseja melhorar o desempenho em uma carga de trabalho específica e reduzir os riscos de alucinações. Ou seja, mistificação da realidade ou conteúdo prejudicial.

### Modelo Ajustado Fino

O ajuste fino é um processo que alavanca a aprendizagem por transferência para 'adaptar' o modelo a uma tarefa subsequente ou para resolver um problema específico. Diferentemente do aprendizado de alguns exemplos e do RAG, ele resulta na geração de um novo modelo, com pesos e vieses atualizados. Isso requer um conjunto de exemplos de treinamento consistindo de uma única entrada (o prompt) e sua saída associada (a conclusão).
Essa seria a abordagem preferida se:

- **Usando modelos ajustados finamente**: Uma empresa deseja usar modelos menos capazes ajustados finamente (como modelos de incorporação) em vez de modelos de alto desempenho, resultando em uma solução mais econômica e rápida.

- **Considerando a latência**: A latência é importante para um caso de uso específico, portanto, não é possível usar prompts muito longos ou o número de exemplos que devem ser aprendidos a partir do modelo não se encaixa no limite de comprimento do prompt.

- **Mantendo-se atualizado**: Uma empresa possui muitos dados de alta qualidade e rótulos de verdade fundamentais e os recursos necessários para manter esses dados atualizados ao longo do tempo.

### Modelo Treinado

Treinar um LLM a partir do zero é, sem dúvida, a abordagem mais difícil e complexa de adotar, exigindo enormes quantidades de dados, recursos qualificados e poder computacional adequado. Essa opção deve ser considerada apenas em um cenário em que uma empresa possui um caso de uso específico de domínio e uma grande quantidade de dados centrados no domínio.

## Verificação de Conhecimento

Qual poderia ser uma boa abordagem para melhorar os resultados de completude do LLM?

1. Engenharia de prompts com contexto
1. RAG
1. Modelo ajustado fino

R: 3 Pois, se você tem o tempo, os recursos e dados de alta qualidade, o ajuste fino é a melhor opção para se manter atualizado. No entanto, se você está procurando melhorar as coisas e está com pouco tempo, vale a pena considerar o RAG primeiro.

## 🚀 Desafio

Saiba mais sobre como você pode [usar o RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para o seu negócio.

## Ótimo Trabalho, Continue com Seu Aprendizado

Deseja aprender mais sobre diferentes conceitos de IA Generativa? Acesse a [página de aprendizado contínuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar outros ótimos recursos sobre este tópico.

Vamos para a Lição 3, onde veremos como podemos [Criar IA Generativa de forma Responsável](../../../03-using-generative-ai-responsibly/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)!
