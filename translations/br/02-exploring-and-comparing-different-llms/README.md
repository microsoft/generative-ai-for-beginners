<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6b7629b8ee4d7d874a27213e903d86a7",
  "translation_date": "2025-10-17T15:59:14+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "br"
}
-->
# Explorando e comparando diferentes LLMs

[![Explorando e comparando diferentes LLMs](../../../translated_images/02-lesson-banner.ef94c84979f97f60f07e27d905e708cbcbdf78707120553ccab27d91c947805b.br.png)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Clique na imagem acima para assistir ao vídeo desta lição_

Na lição anterior, vimos como a IA Generativa está transformando o cenário tecnológico, como os Modelos de Linguagem de Grande Escala (LLMs) funcionam e como uma empresa - como nossa startup - pode aplicá-los em seus casos de uso e crescer! Neste capítulo, vamos comparar e contrastar diferentes tipos de modelos de linguagem de grande escala (LLMs) para entender seus prós e contras.

O próximo passo na jornada da nossa startup é explorar o cenário atual dos LLMs e entender quais são adequados para nosso caso de uso.

## Introdução

Esta lição abordará:

- Diferentes tipos de LLMs no cenário atual.
- Testar, iterar e comparar diferentes modelos para seu caso de uso no Azure.
- Como implantar um LLM.

## Objetivos de Aprendizagem

Após concluir esta lição, você será capaz de:

- Selecionar o modelo certo para seu caso de uso.
- Entender como testar, iterar e melhorar o desempenho do seu modelo.
- Saber como as empresas implantam modelos.

## Entenda os diferentes tipos de LLMs

Os LLMs podem ter várias categorizações com base em sua arquitetura, dados de treinamento e caso de uso. Compreender essas diferenças ajudará nossa startup a selecionar o modelo certo para o cenário e entender como testar, iterar e melhorar o desempenho.

Existem muitos tipos diferentes de modelos LLM, e sua escolha depende do que você pretende usar, dos seus dados, de quanto está disposto a pagar e outros fatores.

Dependendo se você pretende usar os modelos para texto, áudio, vídeo, geração de imagens e assim por diante, pode optar por um tipo diferente de modelo.

- **Reconhecimento de áudio e fala**. Para esse propósito, modelos do tipo Whisper são uma ótima escolha, pois são de uso geral e voltados para reconhecimento de fala. Eles são treinados em áudio diversificado e podem realizar reconhecimento de fala multilíngue. Saiba mais sobre [modelos do tipo Whisper aqui](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Geração de imagens**. Para geração de imagens, DALL-E e Midjourney são duas escolhas bem conhecidas. DALL-E é oferecido pelo Azure OpenAI. [Leia mais sobre DALL-E aqui](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) e também no Capítulo 9 deste currículo.

- **Geração de texto**. A maioria dos modelos é treinada para geração de texto, e você tem uma grande variedade de escolhas, desde GPT-3.5 até GPT-4. Eles têm custos diferentes, sendo o GPT-4 o mais caro. Vale a pena explorar o [Azure OpenAI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) para avaliar quais modelos melhor atendem às suas necessidades em termos de capacidade e custo.

- **Multimodalidade**. Se você está procurando lidar com múltiplos tipos de dados na entrada e saída, pode querer explorar modelos como [gpt-4 turbo com visão ou gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) - os lançamentos mais recentes dos modelos OpenAI - que são capazes de combinar processamento de linguagem natural com compreensão visual, permitindo interações por meio de interfaces multimodais.

Selecionar um modelo significa obter algumas capacidades básicas, que podem não ser suficientes. Muitas vezes, você tem dados específicos da empresa que precisa informar ao LLM de alguma forma. Existem algumas abordagens diferentes para isso, mais sobre isso nas próximas seções.

### Modelos Fundamentais versus LLMs

O termo Modelo Fundamental foi [cunhado por pesquisadores de Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) e definido como um modelo de IA que segue alguns critérios, como:

- **Eles são treinados usando aprendizado não supervisionado ou aprendizado auto-supervisionado**, o que significa que são treinados em dados multimodais não rotulados e não requerem anotação ou rotulagem humana de dados para seu processo de treinamento.
- **Eles são modelos muito grandes**, baseados em redes neurais muito profundas treinadas em bilhões de parâmetros.
- **Eles são normalmente destinados a servir como uma ‘fundação’ para outros modelos**, ou seja, podem ser usados como ponto de partida para outros modelos serem construídos sobre eles, o que pode ser feito por meio de ajuste fino.

![Modelos Fundamentais versus LLMs](../../../translated_images/FoundationModel.e4859dbb7a825c94b284f17eae1c186aabc21d4d8644331f5b007d809cf8d0f2.br.png)

Fonte da imagem: [Essential Guide to Foundation Models and Large Language Models | por Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Para esclarecer ainda mais essa distinção, vamos usar o ChatGPT como exemplo. Para construir a primeira versão do ChatGPT, um modelo chamado GPT-3.5 serviu como modelo fundamental. Isso significa que a OpenAI usou alguns dados específicos de chat para criar uma versão ajustada do GPT-3.5 que foi especializada em ter um bom desempenho em cenários de conversação, como chatbots.

![Modelo Fundamental](../../../translated_images/Multimodal.2c389c6439e0fc51b0b7b226d95d7d900d372ae66902d71b8ce5ec4951b8efbe.br.png)

Fonte da imagem: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modelos Open Source versus Proprietários

Outra forma de categorizar os LLMs é se eles são open source ou proprietários.

Modelos open source são modelos disponibilizados ao público e podem ser usados por qualquer pessoa. Eles são frequentemente disponibilizados pela empresa que os criou ou pela comunidade de pesquisa. Esses modelos podem ser inspecionados, modificados e personalizados para os diversos casos de uso em LLMs. No entanto, nem sempre são otimizados para uso em produção e podem não ter o mesmo desempenho que modelos proprietários. Além disso, o financiamento para modelos open source pode ser limitado, e eles podem não ser mantidos a longo prazo ou atualizados com as pesquisas mais recentes. Exemplos de modelos open source populares incluem [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) e [LLaMA](https://llama.meta.com).

Modelos proprietários são modelos que pertencem a uma empresa e não são disponibilizados ao público. Esses modelos são frequentemente otimizados para uso em produção. No entanto, não podem ser inspecionados, modificados ou personalizados para diferentes casos de uso. Além disso, nem sempre estão disponíveis gratuitamente e podem exigir uma assinatura ou pagamento para serem usados. Também, os usuários não têm controle sobre os dados usados para treinar o modelo, o que significa que devem confiar no proprietário do modelo para garantir o compromisso com a privacidade dos dados e o uso responsável da IA. Exemplos de modelos proprietários populares incluem [Modelos OpenAI](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) ou [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Embedding versus Geração de Imagens versus Geração de Texto e Código

Os LLMs também podem ser categorizados pelo tipo de saída que geram.

Embeddings são um conjunto de modelos que podem converter texto em uma forma numérica, chamada embedding, que é uma representação numérica do texto de entrada. Embeddings facilitam para as máquinas entenderem as relações entre palavras ou frases e podem ser consumidos como entradas por outros modelos, como modelos de classificação ou modelos de agrupamento que têm melhor desempenho com dados numéricos. Modelos de embedding são frequentemente usados para aprendizado por transferência, onde um modelo é construído para uma tarefa substituta para a qual há uma abundância de dados, e então os pesos do modelo (embeddings) são reutilizados para outras tarefas subsequentes. Um exemplo dessa categoria é [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/Embedding.c3708fe988ccf76073d348483dbb7569f622211104f073e22e43106075c04800.br.png)

Modelos de geração de imagens são modelos que geram imagens. Esses modelos são frequentemente usados para edição de imagens, síntese de imagens e tradução de imagens. Modelos de geração de imagens são frequentemente treinados em grandes conjuntos de dados de imagens, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar novas imagens ou editar imagens existentes com técnicas de inpainting, super-resolução e colorização. Exemplos incluem [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) e [Modelos Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Geração de Imagens](../../../translated_images/Image.349c080266a763fd255b840a921cd8fc526ed78dc58708fa569ff1873d302345.br.png)

Modelos de geração de texto e código são modelos que geram texto ou código. Esses modelos são frequentemente usados para sumarização de texto, tradução e resposta a perguntas. Modelos de geração de texto são frequentemente treinados em grandes conjuntos de dados de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar novo texto ou responder perguntas. Modelos de geração de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), são frequentemente treinados em grandes conjuntos de dados de código, como GitHub, e podem ser usados para gerar novo código ou corrigir bugs em código existente.

![Geração de Texto e Código](../../../translated_images/Text.a8c0cf139e5cc2a0cd3edaba8d675103774e6ddcb3c9fc5a98bb17c9a450e31d.br.png)

### Encoder-Decoder versus Apenas Decoder

Para falar sobre os diferentes tipos de arquiteturas de LLMs, vamos usar uma analogia.

Imagine que seu gerente lhe deu a tarefa de escrever um quiz para os alunos. Você tem dois colegas; um é responsável por criar o conteúdo e o outro por revisá-lo.

O criador de conteúdo é como um modelo Apenas Decoder, ele pode olhar para o tópico e ver o que você já escreveu e então criar um curso com base nisso. Ele é muito bom em escrever conteúdo envolvente e informativo, mas não é muito bom em entender o tópico e os objetivos de aprendizado. Alguns exemplos de modelos Apenas Decoder são os modelos da família GPT, como GPT-3.

O revisor é como um modelo Apenas Encoder, ele olha para o curso escrito e as respostas, percebendo a relação entre eles e entendendo o contexto, mas não é bom em gerar conteúdo. Um exemplo de modelo Apenas Encoder seria o BERT.

Imagine que também podemos ter alguém que possa criar e revisar o quiz, este é um modelo Encoder-Decoder. Alguns exemplos seriam BART e T5.

### Serviço versus Modelo

Agora, vamos falar sobre a diferença entre um serviço e um modelo. Um serviço é um produto oferecido por um Provedor de Serviços em Nuvem e é frequentemente uma combinação de modelos, dados e outros componentes. Um modelo é o componente central de um serviço e é frequentemente um modelo fundamental, como um LLM.

Serviços são frequentemente otimizados para uso em produção e geralmente mais fáceis de usar do que modelos, por meio de uma interface gráfica. No entanto, serviços nem sempre estão disponíveis gratuitamente e podem exigir uma assinatura ou pagamento para serem usados, em troca de aproveitar os equipamentos e recursos do proprietário do serviço, otimizando despesas e escalando facilmente. Um exemplo de serviço é o [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), que oferece um plano de pagamento conforme o uso, ou seja, os usuários são cobrados proporcionalmente ao quanto utilizam o serviço. Além disso, o Azure OpenAI Service oferece segurança de nível empresarial e um framework de IA responsável sobre as capacidades dos modelos.

Modelos são apenas a Rede Neural, com os parâmetros, pesos e outros. Permitem que empresas os executem localmente, porém, seria necessário comprar equipamentos, construir uma estrutura para escalar e adquirir uma licença ou usar um modelo open source. Um modelo como o LLaMA está disponível para uso, exigindo poder computacional para executar o modelo.

## Como testar e iterar com diferentes modelos para entender o desempenho no Azure

Depois que nossa equipe explorou o cenário atual dos LLMs e identificou alguns bons candidatos para seus cenários, o próximo passo é testá-los com seus dados e em sua carga de trabalho. Este é um processo iterativo, realizado por meio de experimentos e medições.
A maioria dos modelos mencionados nos parágrafos anteriores (modelos da OpenAI, modelos de código aberto como Llama2 e transformers da Hugging Face) estão disponíveis no [Catálogo de Modelos](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) no [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) é uma plataforma em nuvem projetada para desenvolvedores criarem aplicações de IA generativa e gerenciarem todo o ciclo de desenvolvimento - desde a experimentação até a avaliação - combinando todos os serviços de IA do Azure em um único hub com uma interface gráfica prática. O Catálogo de Modelos no Azure AI Studio permite ao usuário:

- Encontrar o Modelo Base de interesse no catálogo - seja proprietário ou de código aberto, filtrando por tarefa, licença ou nome. Para melhorar a busca, os modelos estão organizados em coleções, como a coleção Azure OpenAI, coleção Hugging Face e outras.

![Catálogo de modelos](../../../translated_images/AzureAIStudioModelCatalog.3cf8a499aa8ba0314f2c73d4048b3225d324165f547525f5b7cfa5f6c9c68941.br.png)

- Revisar o cartão do modelo, incluindo uma descrição detalhada do uso pretendido e dados de treinamento, exemplos de código e resultados de avaliação na biblioteca interna de avaliações.

![Cartão do modelo](../../../translated_images/ModelCard.598051692c6e400d681a713ba7717e8b6e5e65f08d12131556fcec0f1789459b.br.png)

- Comparar benchmarks entre modelos e conjuntos de dados disponíveis na indústria para avaliar qual atende ao cenário de negócios, através do painel [Benchmarks de Modelos](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Benchmarks de modelos](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.br.png)

- Ajustar o modelo com dados de treinamento personalizados para melhorar o desempenho do modelo em uma carga de trabalho específica, aproveitando as capacidades de experimentação e rastreamento do Azure AI Studio.

![Ajuste de modelo](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.br.png)

- Implantar o modelo pré-treinado original ou a versão ajustada para uma inferência remota em tempo real - computação gerenciada - ou endpoint de API sem servidor - [pagamento conforme o uso](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - para permitir que as aplicações o consumam.

![Implantação de modelo](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.br.png)

> [!NOTE]
> Nem todos os modelos no catálogo estão atualmente disponíveis para ajuste e/ou implantação com pagamento conforme o uso. Verifique o cartão do modelo para detalhes sobre as capacidades e limitações do modelo.

## Melhorando os resultados de LLM

Exploramos com nossa equipe de startup diferentes tipos de LLMs e uma plataforma em nuvem (Azure Machine Learning) que nos permite comparar diferentes modelos, avaliá-los em dados de teste, melhorar o desempenho e implantá-los em endpoints de inferência.

Mas quando eles devem considerar ajustar um modelo em vez de usar um pré-treinado? Existem outras abordagens para melhorar o desempenho do modelo em cargas de trabalho específicas?

Existem várias abordagens que uma empresa pode usar para obter os resultados necessários de um LLM. Você pode selecionar diferentes tipos de modelos com diferentes graus de treinamento ao implantar um LLM em produção, com diferentes níveis de complexidade, custo e qualidade. Aqui estão algumas abordagens diferentes:

- **Engenharia de prompts com contexto**. A ideia é fornecer contexto suficiente ao fazer o prompt para garantir que você obtenha as respostas necessárias.

- **Geração Aumentada por Recuperação, RAG**. Seus dados podem estar em um banco de dados ou endpoint web, por exemplo. Para garantir que esses dados, ou um subconjunto deles, sejam incluídos no momento do prompt, você pode buscar os dados relevantes e torná-los parte do prompt do usuário.

- **Modelo ajustado**. Aqui, você treinou o modelo adicionalmente com seus próprios dados, o que levou o modelo a ser mais preciso e responsivo às suas necessidades, mas pode ser caro.

![Implantação de LLMs](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.br.png)

Fonte da imagem: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Engenharia de Prompts com Contexto

LLMs pré-treinados funcionam muito bem em tarefas gerais de linguagem natural, mesmo sendo chamados com um prompt curto, como uma frase para completar ou uma pergunta – o chamado aprendizado “zero-shot”.

No entanto, quanto mais o usuário puder enquadrar sua consulta, com uma solicitação detalhada e exemplos – o Contexto – mais precisa e próxima das expectativas do usuário será a resposta. Nesse caso, falamos de aprendizado “one-shot” se o prompt incluir apenas um exemplo e “few-shot learning” se incluir vários exemplos. A engenharia de prompts com contexto é a abordagem mais econômica para começar.

### Geração Aumentada por Recuperação (RAG)

LLMs têm a limitação de que só podem usar os dados que foram utilizados durante seu treinamento para gerar uma resposta. Isso significa que eles não sabem nada sobre fatos que ocorreram após seu processo de treinamento e não podem acessar informações não públicas (como dados da empresa). 

Isso pode ser superado através do RAG, uma técnica que aumenta o prompt com dados externos na forma de fragmentos de documentos, considerando os limites de comprimento do prompt. Isso é suportado por ferramentas de banco de dados vetorial (como [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) que recuperam os fragmentos úteis de fontes de dados pré-definidas variadas e os adicionam ao Contexto do prompt.

Essa técnica é muito útil quando uma empresa não tem dados suficientes, tempo suficiente ou recursos para ajustar um LLM, mas ainda deseja melhorar o desempenho em uma carga de trabalho específica e reduzir os riscos de fabricações, ou seja, distorções da realidade ou conteúdo prejudicial.

### Modelo Ajustado

O ajuste é um processo que aproveita o aprendizado por transferência para ‘adaptar’ o modelo a uma tarefa específica ou resolver um problema específico. Diferentemente do aprendizado few-shot e do RAG, resulta em um novo modelo sendo gerado, com pesos e vieses atualizados. Ele requer um conjunto de exemplos de treinamento consistindo em uma única entrada (o prompt) e sua saída associada (a conclusão). 

Essa seria a abordagem preferida se:

- **Usando modelos ajustados**. Uma empresa gostaria de usar modelos ajustados menos capazes (como modelos de incorporação) em vez de modelos de alto desempenho, resultando em uma solução mais econômica e rápida.

- **Considerando latência**. A latência é importante para um caso de uso específico, então não é possível usar prompts muito longos ou o número de exemplos que devem ser aprendidos pelo modelo não se encaixa no limite de comprimento do prompt.

- **Mantendo-se atualizado**. Uma empresa tem muitos dados de alta qualidade e rótulos de verdade base e os recursos necessários para manter esses dados atualizados ao longo do tempo.

### Modelo Treinado

Treinar um LLM do zero é, sem dúvida, a abordagem mais difícil e complexa de adotar, exigindo quantidades massivas de dados, recursos qualificados e poder computacional adequado. Essa opção deve ser considerada apenas em um cenário onde uma empresa tem um caso de uso específico para o domínio e uma grande quantidade de dados centrados no domínio.

## Verificação de conhecimento

Qual poderia ser uma boa abordagem para melhorar os resultados de conclusão de LLM?

1. Engenharia de prompts com contexto  
1. RAG  
1. Modelo ajustado  

A:3, se você tiver tempo, recursos e dados de alta qualidade, o ajuste é a melhor opção para se manter atualizado. No entanto, se você está buscando melhorias e não tem tempo, vale considerar o RAG primeiro.

## 🚀 Desafio

Leia mais sobre como você pode [usar RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para sua empresa.

## Ótimo trabalho, continue aprendendo

Após concluir esta lição, confira nossa [coleção de aprendizado de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA generativa!

Vá para a Lição 3, onde veremos como [construir com IA generativa de forma responsável](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.