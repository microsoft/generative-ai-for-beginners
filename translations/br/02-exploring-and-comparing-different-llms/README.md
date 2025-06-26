<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2f686f2eb794941761252ac5e8e090b",
  "translation_date": "2025-06-25T10:36:18+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "br"
}
-->
# Explorando e comparando diferentes LLMs

> _Clique na imagem acima para assistir ao vídeo desta lição_

Na lição anterior, vimos como a IA Generativa está mudando o cenário tecnológico, como os Modelos de Linguagem de Grande Escala (LLMs) funcionam e como uma empresa - como nossa startup - pode aplicá-los aos seus casos de uso e crescer! Neste capítulo, estamos buscando comparar e contrastar diferentes tipos de modelos de linguagem de grande escala (LLMs) para entender seus prós e contras.

O próximo passo na jornada da nossa startup é explorar o cenário atual dos LLMs e entender quais são adequados para nosso caso de uso.

## Introdução

Esta lição abordará:

- Diferentes tipos de LLMs no cenário atual.
- Testar, iterar e comparar diferentes modelos para seu caso de uso no Azure.
- Como implantar um LLM.

## Objetivos de Aprendizagem

Após completar esta lição, você será capaz de:

- Selecionar o modelo certo para seu caso de uso.
- Entender como testar, iterar e melhorar o desempenho do seu modelo.
- Saber como as empresas implantam modelos.

## Compreender diferentes tipos de LLMs

LLMs podem ter múltiplas categorizações com base em sua arquitetura, dados de treinamento e caso de uso. Compreender essas diferenças ajudará nossa startup a selecionar o modelo certo para o cenário e entender como testar, iterar e melhorar o desempenho.

Existem muitos tipos diferentes de modelos LLM, e sua escolha de modelo depende do que você pretende usar, seus dados, quanto está disposto a pagar e mais.

Dependendo se você pretende usar os modelos para geração de texto, áudio, vídeo, imagem e assim por diante, você pode optar por um tipo diferente de modelo.

- **Reconhecimento de áudio e fala**. Para este propósito, modelos do tipo Whisper são uma ótima escolha, pois são de propósito geral e voltados para reconhecimento de fala. São treinados em áudio diversificado e podem realizar reconhecimento de fala multilíngue. Saiba mais sobre [modelos do tipo Whisper aqui](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Geração de imagem**. Para geração de imagem, DALL-E e Midjourney são duas escolhas bem conhecidas. DALL-E é oferecido pelo Azure OpenAI. [Leia mais sobre DALL-E aqui](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) e também no Capítulo 9 deste currículo.

- **Geração de texto**. A maioria dos modelos é treinada para geração de texto e você tem uma grande variedade de escolhas, desde GPT-3.5 até GPT-4. Eles têm custos diferentes, sendo o GPT-4 o mais caro. Vale a pena conferir o [playground do Azure OpenAI](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) para avaliar quais modelos melhor se adequam às suas necessidades em termos de capacidade e custo.

- **Multi-modalidade**. Se você está procurando lidar com vários tipos de dados na entrada e saída, pode querer explorar modelos como [gpt-4 turbo com visão ou gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) - os últimos lançamentos de modelos OpenAI - que são capazes de combinar processamento de linguagem natural com compreensão visual, permitindo interações através de interfaces multi-modais.

Selecionar um modelo significa obter algumas capacidades básicas, que podem não ser suficientes, no entanto. Muitas vezes, você tem dados específicos da empresa que precisa informar ao LLM de alguma forma. Existem algumas escolhas diferentes sobre como abordar isso, mais sobre isso nas seções seguintes.

### Modelos de Fundação versus LLMs

O termo Modelo de Fundação foi [criado por pesquisadores de Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) e definido como um modelo de IA que segue alguns critérios, como:

- **São treinados usando aprendizado não supervisionado ou aprendizado auto-supervisionado**, o que significa que são treinados em dados multi-modais não rotulados e não requerem anotação ou rotulagem humana de dados para seu processo de treinamento.
- **São modelos muito grandes**, baseados em redes neurais muito profundas treinadas em bilhões de parâmetros.
- **Normalmente são destinados a servir como uma 'fundação' para outros modelos**, o que significa que podem ser usados como ponto de partida para outros modelos serem construídos sobre eles, o que pode ser feito por ajuste fino.

Para esclarecer ainda mais essa distinção, vamos tomar o ChatGPT como exemplo. Para construir a primeira versão do ChatGPT, um modelo chamado GPT-3.5 serviu como modelo de fundação. Isso significa que a OpenAI usou alguns dados específicos de chat para criar uma versão ajustada do GPT-3.5 que foi especializada em ter um bom desempenho em cenários conversacionais, como chatbots.

### Modelos de Código Aberto versus Proprietários

Outra maneira de categorizar LLMs é se são de código aberto ou proprietários.

Modelos de código aberto são modelos que estão disponíveis ao público e podem ser usados por qualquer pessoa. Eles geralmente são disponibilizados pela empresa que os criou ou pela comunidade de pesquisa. Esses modelos podem ser inspecionados, modificados e personalizados para os vários casos de uso em LLMs. No entanto, nem sempre são otimizados para uso em produção e podem não ser tão performáticos quanto modelos proprietários. Além disso, o financiamento para modelos de código aberto pode ser limitado, e eles podem não ser mantidos a longo prazo ou não serem atualizados com as pesquisas mais recentes. Exemplos de modelos de código aberto populares incluem [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) e [LLaMA](https://llama.meta.com).

Modelos proprietários são modelos que são de propriedade de uma empresa e não são disponibilizados ao público. Esses modelos geralmente são otimizados para uso em produção. No entanto, não podem ser inspecionados, modificados ou personalizados para diferentes casos de uso. Além disso, nem sempre estão disponíveis gratuitamente e podem exigir uma assinatura ou pagamento para serem usados. Além disso, os usuários não têm controle sobre os dados usados para treinar o modelo, o que significa que devem confiar no proprietário do modelo para garantir o compromisso com a privacidade dos dados e o uso responsável da IA. Exemplos de modelos proprietários populares incluem [modelos OpenAI](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) ou [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Embedding versus Geração de Imagem versus Geração de Texto e Código

LLMs também podem ser categorizados pelo tipo de saída que geram.

Embeddings são um conjunto de modelos que podem converter texto em uma forma numérica, chamada embedding, que é uma representação numérica do texto de entrada. Embeddings facilitam para as máquinas entenderem as relações entre palavras ou frases e podem ser consumidos como entradas por outros modelos, como modelos de classificação ou de agrupamento que têm melhor desempenho em dados numéricos. Modelos de embedding são frequentemente usados para aprendizado por transferência, onde um modelo é construído para uma tarefa substituta para a qual há uma abundância de dados, e então os pesos do modelo (embeddings) são reutilizados para outras tarefas subsequentes. Um exemplo dessa categoria é [embeddings OpenAI](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

Modelos de geração de imagem são modelos que geram imagens. Esses modelos são frequentemente usados para edição de imagem, síntese de imagem e tradução de imagem. Modelos de geração de imagem são frequentemente treinados em grandes conjuntos de dados de imagens, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar novas imagens ou editar imagens existentes com técnicas de inpainting, super-resolução e colorização. Exemplos incluem [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) e [modelos Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

Modelos de geração de texto e código são modelos que geram texto ou código. Esses modelos são frequentemente usados para sumarização de texto, tradução e resposta a perguntas. Modelos de geração de texto são frequentemente treinados em grandes conjuntos de dados de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar novo texto ou responder perguntas. Modelos de geração de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), são frequentemente treinados em grandes conjuntos de dados de código, como o GitHub, e podem ser usados para gerar novo código ou corrigir bugs em código existente.

### Encoder-Decoder versus Somente Decoder

Para falar sobre os diferentes tipos de arquiteturas de LLMs, vamos usar uma analogia.

Imagine que seu gerente lhe deu a tarefa de escrever um questionário para os alunos. Você tem dois colegas; um é responsável por criar o conteúdo e o outro por revisá-lo.

O criador de conteúdo é como um modelo somente Decoder, ele pode olhar para o tópico e ver o que você já escreveu e, em seguida, escrever um curso com base nisso. Eles são muito bons em escrever conteúdo envolvente e informativo, mas não são muito bons em entender o tópico e os objetivos de aprendizagem. Alguns exemplos de modelos Decoder são os modelos da família GPT, como o GPT-3.

O revisor é como um modelo somente Encoder, ele olha para o curso escrito e as respostas, notando a relação entre eles e entendendo o contexto, mas não é bom em gerar conteúdo. Um exemplo de modelo somente Encoder seria o BERT.

Imagine que também podemos ter alguém que poderia criar e revisar o questionário, este é um modelo Encoder-Decoder. Alguns exemplos seriam BART e T5.

### Serviço versus Modelo

Agora, vamos falar sobre a diferença entre um serviço e um modelo. Um serviço é um produto oferecido por um Provedor de Serviços em Nuvem e é frequentemente uma combinação de modelos, dados e outros componentes. Um modelo é o componente central de um serviço e é frequentemente um modelo de fundação, como um LLM.

Os serviços são frequentemente otimizados para uso em produção e geralmente são mais fáceis de usar do que os modelos, através de uma interface gráfica de usuário. No entanto, os serviços nem sempre estão disponíveis gratuitamente e podem exigir uma assinatura ou pagamento para serem usados, em troca de aproveitar o equipamento e recursos do proprietário do serviço, otimizando despesas e escalando facilmente. Um exemplo de serviço é o [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), que oferece um plano de pagamento conforme o uso, o que significa que os usuários são cobrados proporcionalmente ao quanto usam o serviço. Além disso, o Azure OpenAI Service oferece segurança de nível empresarial e um framework de IA responsável em cima das capacidades dos modelos.

Os modelos são apenas a Rede Neural, com os parâmetros, pesos e outros. Permitindo que as empresas executem localmente, no entanto, precisariam comprar equipamentos, construir uma estrutura para escalar e comprar uma licença ou usar um modelo de código aberto. Um modelo como o LLaMA está disponível para ser usado, exigindo poder computacional para executar o modelo.

## Como testar e iterar com diferentes modelos para entender o desempenho no Azure

Uma vez que nossa equipe tenha explorado o cenário atual dos LLMs e identificado alguns bons candidatos para seus cenários, o próximo passo é testá-los em seus dados e em sua carga de trabalho. Este é um processo iterativo, realizado por experimentos e medidas. A maioria dos modelos que mencionamos nos parágrafos anteriores (modelos OpenAI, modelos de código aberto como Llama2 e transformadores Hugging Face) estão disponíveis no [Catálogo de Modelos](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) no [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) é uma Plataforma em Nuvem projetada para desenvolvedores construírem aplicativos de IA generativa e gerenciarem todo o ciclo de desenvolvimento - da experimentação à avaliação - combinando todos os serviços de IA do Azure em um único hub com uma interface gráfica de usuário prática. O Catálogo de Modelos no Azure AI Studio permite ao usuário:

- Encontrar o Modelo de Fundação de interesse no catálogo - seja proprietário ou de código aberto, filtrando por tarefa, licença ou nome. Para melhorar a pesquisa, os modelos são organizados em coleções, como coleção Azure OpenAI, coleção Hugging Face e mais.

- Revisar o cartão do modelo, incluindo uma descrição detalhada do uso pretendido e dados de treinamento, exemplos de código e resultados de avaliação na biblioteca de avaliações internas.
- Compare benchmarks entre modelos e conjuntos de dados disponíveis na indústria para avaliar qual atende ao cenário de negócios, através do painel [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.br.png)

- Ajuste fino do modelo em dados de treinamento personalizados para melhorar o desempenho do modelo em uma carga de trabalho específica, aproveitando as capacidades de experimentação e rastreamento do Azure AI Studio.

![Model fine-tuning](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.br.png)

- Implante o modelo pré-treinado original ou a versão ajustada para uma inferência remota em tempo real - computação gerenciada - ou ponto de extremidade de API sem servidor - [pague conforme o uso](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - para permitir que aplicações o consumam.

![Model deployment](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.br.png)

> [!NOTE]
> Nem todos os modelos no catálogo estão atualmente disponíveis para ajuste fino e/ou implantação paga conforme o uso. Verifique o cartão do modelo para detalhes sobre as capacidades e limitações do modelo.

## Melhorando resultados de LLM

Exploramos com nossa equipe de startup diferentes tipos de LLMs e uma Plataforma de Nuvem (Azure Machine Learning) que nos permite comparar diferentes modelos, avaliá-los em dados de teste, melhorar o desempenho e implantá-los em pontos de extremidade de inferência.

Mas quando eles devem considerar ajustar um modelo em vez de usar um pré-treinado? Existem outras abordagens para melhorar o desempenho do modelo em cargas de trabalho específicas?

Existem várias abordagens que uma empresa pode usar para obter os resultados que precisa de um LLM. Você pode selecionar diferentes tipos de modelos com diferentes graus de treinamento ao implantar um LLM em produção, com diferentes níveis de complexidade, custo e qualidade. Aqui estão algumas abordagens diferentes:

- **Engenharia de prompts com contexto**. A ideia é fornecer contexto suficiente quando você faz um prompt para garantir que obtenha as respostas necessárias.

- **Geração Aumentada por Recuperação, RAG**. Seus dados podem existir em um banco de dados ou ponto de extremidade web, por exemplo, para garantir que esses dados, ou um subconjunto deles, sejam incluídos no momento do prompt, você pode buscar os dados relevantes e fazer disso parte do prompt do usuário.

- **Modelo ajustado**. Aqui, você treinou o modelo ainda mais com seus próprios dados, o que levou o modelo a ser mais preciso e responsivo às suas necessidades, mas pode ser caro.

![LLMs deployment](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.br.png)

Fonte da imagem: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Engenharia de Prompts com Contexto

LLMs pré-treinados funcionam muito bem em tarefas de linguagem natural generalizadas, mesmo chamando-os com um prompt curto, como uma frase a ser completada ou uma pergunta – a chamada aprendizagem "zero-shot".

No entanto, quanto mais o usuário puder enquadrar sua consulta, com uma solicitação detalhada e exemplos – o Contexto – mais precisa e próxima das expectativas do usuário será a resposta. Nesse caso, falamos sobre aprendizagem "one-shot" se o prompt incluir apenas um exemplo e "few-shot learning" se incluir vários exemplos. A engenharia de prompts com contexto é a abordagem mais econômica para começar.

### Geração Aumentada por Recuperação (RAG)

LLMs têm a limitação de que só podem usar os dados que foram usados durante seu treinamento para gerar uma resposta. Isso significa que eles não sabem nada sobre os fatos que aconteceram após seu processo de treinamento, e não podem acessar informações não públicas (como dados de empresa). Isso pode ser superado através do RAG, uma técnica que aumenta o prompt com dados externos na forma de fragmentos de documentos, considerando os limites de comprimento do prompt. Isso é suportado por ferramentas de banco de dados de vetores (como [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) que recuperam os fragmentos úteis de várias fontes de dados pré-definidas e os adicionam ao Contexto do prompt.

Essa técnica é muito útil quando uma empresa não tem dados suficientes, tempo suficiente ou recursos para ajustar um LLM, mas ainda deseja melhorar o desempenho em uma carga de trabalho específica e reduzir riscos de fabricações, ou seja, mistificação da realidade ou conteúdo prejudicial.

### Modelo Ajustado

O ajuste fino é um processo que aproveita o aprendizado de transferência para 'adaptar' o modelo a uma tarefa downstream ou para resolver um problema específico. Diferentemente da aprendizagem few-shot e do RAG, resulta em um novo modelo sendo gerado, com pesos e vieses atualizados. Requer um conjunto de exemplos de treinamento consistindo de uma única entrada (o prompt) e sua saída associada (a conclusão). Essa seria a abordagem preferida se:

- **Usando modelos ajustados**. Uma empresa gostaria de usar modelos ajustados menos capazes (como modelos de incorporação) em vez de modelos de alto desempenho, resultando em uma solução mais econômica e rápida.

- **Considerando a latência**. A latência é importante para um caso de uso específico, então não é possível usar prompts muito longos ou o número de exemplos que devem ser aprendidos pelo modelo não cabe no limite de comprimento do prompt.

- **Mantendo-se atualizado**. Uma empresa tem muitos dados de alta qualidade e rótulos de verdadeiros e os recursos necessários para manter esses dados atualizados ao longo do tempo.

### Modelo Treinado

Treinar um LLM do zero é, sem dúvida, a abordagem mais difícil e complexa de adotar, exigindo quantidades massivas de dados, recursos qualificados e poder computacional adequado. Esta opção deve ser considerada apenas em um cenário onde uma empresa tem um caso de uso específico de domínio e uma grande quantidade de dados centrados no domínio.

## Verificação de Conhecimento

Qual poderia ser uma boa abordagem para melhorar os resultados de conclusão de LLM?

1. Engenharia de prompts com contexto
1. RAG
1. Modelo ajustado

A:3, se você tem tempo e recursos e dados de alta qualidade, o ajuste fino é a melhor opção para se manter atualizado. No entanto, se você está procurando melhorar as coisas e está com falta de tempo, vale a pena considerar o RAG primeiro.

## 🚀 Desafio

Leia mais sobre como você pode [usar RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para o seu negócio.

## Ótimo Trabalho, Continue Seu Aprendizado

Após concluir esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Vá para a Lição 3, onde veremos como [construir com IA Generativa de forma Responsável](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se uma tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.