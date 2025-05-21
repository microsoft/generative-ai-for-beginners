<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2f686f2eb794941761252ac5e8e090b",
  "translation_date": "2025-05-19T09:17:14+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "br"
}
-->
# Explorando e comparando diferentes LLMs

[![Explorando e comparando diferentes LLMs](../../../translated_images/02-lesson-banner.722fb0fdf701564d4479112ef4c4fa964c98dce0c241decbe12aae32e9fb4659.br.png)](https://aka.ms/gen-ai-lesson2-gh?WT.mc_id=academic-105485-koreyst)

> _Clique na imagem acima para ver o vídeo desta lição_

Na lição anterior, vimos como a IA Generativa está mudando o cenário tecnológico, como os Modelos de Linguagem de Grande Escala (LLMs) funcionam e como uma empresa - como nossa startup - pode aplicá-los aos seus casos de uso e crescer! Neste capítulo, estamos buscando comparar e contrastar diferentes tipos de modelos de linguagem de grande escala (LLMs) para entender seus prós e contras.

O próximo passo na jornada da nossa startup é explorar o cenário atual dos LLMs e entender quais são adequados para o nosso caso de uso.

## Introdução

Esta lição irá cobrir:

- Diferentes tipos de LLMs no cenário atual.
- Testar, iterar e comparar diferentes modelos para o seu caso de uso no Azure.
- Como implantar um LLM.

## Objetivos de Aprendizagem

Após completar esta lição, você será capaz de:

- Selecionar o modelo certo para o seu caso de uso.
- Entender como testar, iterar e melhorar o desempenho do seu modelo.
- Saber como as empresas implantam modelos.

## Entenda diferentes tipos de LLMs

LLMs podem ter múltiplas categorizações baseadas em sua arquitetura, dados de treinamento e caso de uso. Entender essas diferenças ajudará nossa startup a selecionar o modelo certo para o cenário e entender como testar, iterar e melhorar o desempenho.

Existem muitos tipos diferentes de modelos LLM, sua escolha de modelo depende do que você pretende usar, dos seus dados, de quanto está disposto a pagar e mais.

Dependendo se você pretende usar os modelos para texto, áudio, vídeo, geração de imagens e assim por diante, você pode optar por um tipo diferente de modelo.

- **Reconhecimento de áudio e fala**. Para esse propósito, modelos do tipo Whisper são uma ótima escolha, pois são de uso geral e voltados para o reconhecimento de fala. Eles são treinados em áudio diverso e podem realizar reconhecimento de fala multilíngue. Saiba mais sobre [modelos do tipo Whisper aqui](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Geração de imagens**. Para geração de imagens, DALL-E e Midjourney são duas escolhas muito conhecidas. DALL-E é oferecido pela Azure OpenAI. [Leia mais sobre DALL-E aqui](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) e também no Capítulo 9 deste currículo.

- **Geração de texto**. A maioria dos modelos é treinada para geração de texto e você tem uma grande variedade de escolhas, de GPT-3.5 a GPT-4. Eles vêm com diferentes custos, sendo o GPT-4 o mais caro. Vale a pena explorar o [playground do Azure OpenAI](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) para avaliar quais modelos melhor se adequam às suas necessidades em termos de capacidade e custo.

- **Multi-modalidade**. Se você está procurando lidar com múltiplos tipos de dados na entrada e saída, pode querer explorar modelos como [gpt-4 turbo com visão ou gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) - os lançamentos mais recentes dos modelos OpenAI - que são capazes de combinar processamento de linguagem natural com compreensão visual, permitindo interações através de interfaces multi-modais.

Selecionar um modelo significa que você obtém algumas capacidades básicas, que podem não ser suficientes, no entanto. Muitas vezes você tem dados específicos da empresa que precisa de alguma forma informar ao LLM. Existem algumas escolhas diferentes sobre como abordar isso, mais sobre isso nas próximas seções.

### Modelos de Fundação versus LLMs

O termo Modelo de Fundação foi [cunhado por pesquisadores de Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) e definido como um modelo de IA que segue alguns critérios, como:

- **Eles são treinados usando aprendizado não supervisionado ou auto-supervisionado**, o que significa que são treinados em dados multimodais não rotulados, e não requerem anotação ou rotulagem humana dos dados para seu processo de treinamento.
- **Eles são modelos muito grandes**, baseados em redes neurais muito profundas treinadas em bilhões de parâmetros.
- **Eles são normalmente destinados a servir como uma ‘fundação’ para outros modelos**, o que significa que podem ser usados como ponto de partida para outros modelos serem construídos em cima, o que pode ser feito por ajuste fino.

![Modelos de Fundação versus LLMs](../../../translated_images/FoundationModel.1b89e9d94c6a60a9af557b1c0a10faa3a55c0cbc6bb357eb144512ab833d162c.br.png)

Fonte da imagem: [Guia Essencial para Modelos de Fundação e Modelos de Linguagem de Grande Escala | por Babar M Bhatti | Medium](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Para esclarecer ainda mais essa distinção, vamos usar o ChatGPT como exemplo. Para construir a primeira versão do ChatGPT, um modelo chamado GPT-3.5 serviu como o modelo de fundação. Isso significa que a OpenAI usou alguns dados específicos de chat para criar uma versão ajustada do GPT-3.5 que foi especializada em ter um bom desempenho em cenários de conversação, como chatbots.

![Modelo de Fundação](../../../translated_images/Multimodal.41df52bb0de979b80e9643ba34f8f1b53d7791cebd88bceedda6497241495f27.br.png)

Fonte da imagem: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modelos de Código Aberto versus Proprietários

Outra maneira de categorizar LLMs é se eles são de código aberto ou proprietários.

Modelos de código aberto são modelos que são disponibilizados ao público e podem ser usados por qualquer pessoa. Eles são frequentemente disponibilizados pela empresa que os criou ou pela comunidade de pesquisa. Esses modelos podem ser inspecionados, modificados e personalizados para os vários casos de uso em LLMs. No entanto, eles nem sempre são otimizados para uso em produção e podem não ser tão performáticos quanto os modelos proprietários. Além disso, o financiamento para modelos de código aberto pode ser limitado, e eles podem não ser mantidos a longo prazo ou podem não ser atualizados com as pesquisas mais recentes. Exemplos de modelos populares de código aberto incluem [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) e [LLaMA](https://llama.meta.com).

Modelos proprietários são modelos que são de propriedade de uma empresa e não são disponibilizados ao público. Esses modelos são frequentemente otimizados para uso em produção. No entanto, eles não podem ser inspecionados, modificados ou personalizados para diferentes casos de uso. Além disso, eles nem sempre estão disponíveis gratuitamente e podem exigir uma assinatura ou pagamento para serem usados. Além disso, os usuários não têm controle sobre os dados que são usados para treinar o modelo, o que significa que devem confiar no proprietário do modelo para garantir o compromisso com a privacidade dos dados e o uso responsável da IA. Exemplos de modelos proprietários populares incluem [modelos OpenAI](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) ou [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Embedding versus Geração de Imagem versus Geração de Texto e Código

LLMs também podem ser categorizados pelo tipo de saída que geram.

Embeddings são um conjunto de modelos que podem converter texto em uma forma numérica, chamada de embedding, que é uma representação numérica do texto de entrada. Embeddings facilitam para as máquinas entenderem as relações entre palavras ou frases e podem ser consumidos como entradas por outros modelos, como modelos de classificação ou modelos de agrupamento que têm melhor desempenho em dados numéricos. Modelos de embedding são frequentemente usados para aprendizado por transferência, onde um modelo é construído para uma tarefa substituta para a qual há uma abundância de dados, e então os pesos do modelo (embeddings) são reutilizados para outras tarefas subsequentes. Um exemplo dessa categoria é [embeddings da OpenAI](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/Embedding.fbf261f314681a51994056854fd928b69b253616bb313e68a9ce19a2b15c8768.br.png)

Modelos de geração de imagem são modelos que geram imagens. Esses modelos são frequentemente usados para edição de imagem, síntese de imagem e tradução de imagem. Modelos de geração de imagem são frequentemente treinados em grandes conjuntos de dados de imagens, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar novas imagens ou para editar imagens existentes com técnicas de inpainting, super-resolução e colorização. Exemplos incluem [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) e [modelos Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Geração de imagem](../../../translated_images/Image.fffee8e361cc35ed409975f6fc85502ae3d20b8eb01273cd327294e26318a049.br.png)

Modelos de geração de texto e código são modelos que geram texto ou código. Esses modelos são frequentemente usados para sumarização de texto, tradução e resposta a perguntas. Modelos de geração de texto são frequentemente treinados em grandes conjuntos de dados de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar novo texto ou para responder perguntas. Modelos de geração de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), são frequentemente treinados em grandes conjuntos de dados de código, como o GitHub, e podem ser usados para gerar novo código ou para corrigir bugs em código existente.

![Geração de texto e código](../../../translated_images/Text.35cfbe12e08d5b5615cf7db5174fe477bf96f45c5b82d53c29523bd8b94bdc17.br.png)

### Encoder-Decoder versus Apenas Decoder

Para falar sobre os diferentes tipos de arquiteturas de LLMs, vamos usar uma analogia.

Imagine que seu gerente lhe deu a tarefa de escrever um quiz para os alunos. Você tem dois colegas; um é responsável por criar o conteúdo e o outro por revisá-lo.

O criador de conteúdo é como um modelo apenas Decoder, ele pode olhar para o tópico e ver o que você já escreveu e então ele pode escrever um curso com base nisso. Eles são muito bons em escrever conteúdo envolvente e informativo, mas não são muito bons em entender o tópico e os objetivos de aprendizado. Alguns exemplos de modelos Decoder são os modelos da família GPT, como o GPT-3.

O revisor é como um modelo apenas Encoder, ele olha para o curso escrito e as respostas, percebendo a relação entre eles e entendendo o contexto, mas não é bom em gerar conteúdo. Um exemplo de modelo apenas Encoder seria o BERT.

Imagine que também podemos ter alguém que possa criar e revisar o quiz, este é um modelo Encoder-Decoder. Alguns exemplos seriam BART e T5.

### Serviço versus Modelo

Agora, vamos falar sobre a diferença entre um serviço e um modelo. Um serviço é um produto oferecido por um Provedor de Serviços em Nuvem e é frequentemente uma combinação de modelos, dados e outros componentes. Um modelo é o componente central de um serviço e é frequentemente um modelo de fundação, como um LLM.

Serviços são frequentemente otimizados para uso em produção e são frequentemente mais fáceis de usar do que modelos, via uma interface gráfica de usuário. No entanto, os serviços nem sempre estão disponíveis gratuitamente e podem exigir uma assinatura ou pagamento para serem usados, em troca de aproveitar o equipamento e os recursos do proprietário do serviço, otimizando despesas e escalando facilmente. Um exemplo de serviço é o [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), que oferece um plano de tarifa conforme o uso, significando que os usuários são cobrados proporcionalmente ao quanto usam o serviço. Além disso, o Azure OpenAI Service oferece segurança de nível empresarial e um framework de IA responsável em cima das capacidades dos modelos.

Modelos são apenas a Rede Neural, com os parâmetros, pesos e outros. Permitindo que empresas rodem localmente, no entanto, precisariam comprar equipamentos, construir uma estrutura para escalar e comprar uma licença ou usar um modelo de código aberto. Um modelo como LLaMA está disponível para ser usado, requerendo poder computacional para rodar o modelo.

## Como testar e iterar com diferentes modelos para entender o desempenho no Azure

Uma vez que nossa equipe tenha explorado o cenário atual dos LLMs e identificado alguns bons candidatos para seus cenários, o próximo passo é testá-los em seus dados e em sua carga de trabalho. Este é um processo iterativo, feito por experimentos e medidas. A maioria dos modelos que mencionamos nos parágrafos anteriores (modelos OpenAI, modelos de código aberto como Llama2 e transformadores Hugging Face) estão disponíveis no [Catálogo de Modelos](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) no [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) é uma plataforma em nuvem projetada para desenvolvedores construírem aplicações de IA generativa e gerenciarem todo o ciclo de desenvolvimento - da experimentação à avaliação - combinando todos os serviços de IA do Azure em um único hub com uma interface gráfica de usuário prática. O Catálogo de Modelos no Azure AI Studio permite ao usuário:

- Encontrar o Modelo de Fundação de interesse no catálogo - seja proprietário ou de código aberto, filtrando por tarefa, licença ou nome. Para melhorar a pesquisa, os modelos são organizados em coleções, como a coleção Azure OpenAI, coleção Hugging Face e mais.

![Catálogo de Modelos](../../../translated_images/AzureAIStudioModelCatalog.e34ac207ac348d31e74246c4f91d10086444783b72bbee3658e0453918aa5d22.br.png)

- Revisar o cartão do modelo, incluindo uma descrição detalhada do uso pretendido e dos dados de treinamento, exemplos de código e resultados de avaliação na biblioteca de avaliações internas.

![Cartão do Modelo](../../../translated_images/ModelCard.8b25784bb406028655a12ea87d1ef3d52302e5d692ae4ec559c2dce7682027c7.br.png)
- Compare benchmarks entre modelos e conjuntos de dados disponíveis na indústria para avaliar qual deles atende ao cenário de negócios, através do painel [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/ModelBenchmarks.b3b4182f762db04b59267af64ce77cc936d38adf40fb032f12acec9063578008.br.png)

- Ajuste o modelo em dados de treinamento personalizados para melhorar o desempenho do modelo em uma carga de trabalho específica, aproveitando as capacidades de experimentação e rastreamento do Azure AI Studio.

![Model fine-tuning](../../../translated_images/FineTuning.f93db4ecbdc85b4a20ff1198fb82f5e2daa3a1ee328733b17d603727db20f5c0.br.png)

- Implante o modelo pré-treinado original ou a versão ajustada para uma inferência remota em tempo real - computação gerenciada - ou endpoint de API sem servidor - [pague conforme o uso](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - para permitir que as aplicações o consumam.

![Model deployment](../../../translated_images/ModelDeploy.7c78c2c5841567abf820d5da8354be454d3f20b62168905645aeac99e50c2562.br.png)

> [!NOTE]
> Nem todos os modelos no catálogo estão atualmente disponíveis para ajuste fino e/ou implantação paga conforme o uso. Verifique o cartão do modelo para detalhes sobre as capacidades e limitações do modelo.

## Melhorando os resultados de LLM

Exploramos com nossa equipe de startup diferentes tipos de LLMs e uma Plataforma em Nuvem (Azure Machine Learning) que nos permite comparar diferentes modelos, avaliá-los em dados de teste, melhorar o desempenho e implantá-los em endpoints de inferência.

Mas quando eles devem considerar ajustar um modelo ao invés de usar um pré-treinado? Existem outras abordagens para melhorar o desempenho do modelo em cargas de trabalho específicas?

Existem várias abordagens que uma empresa pode usar para obter os resultados que precisa de um LLM. Você pode selecionar diferentes tipos de modelos com diferentes graus de treinamento ao implantar um LLM em produção, com diferentes níveis de complexidade, custo e qualidade. Aqui estão algumas abordagens diferentes:

- **Engenharia de prompt com contexto**. A ideia é fornecer contexto suficiente ao fazer um prompt para garantir que você obtenha as respostas necessárias.

- **Geração Aumentada por Recuperação, RAG**. Seus dados podem existir em um banco de dados ou endpoint web, por exemplo, para garantir que esses dados, ou um subconjunto deles, sejam incluídos no momento do prompt, você pode buscar os dados relevantes e torná-los parte do prompt do usuário.

- **Modelo ajustado**. Aqui, você treinou o modelo mais a fundo com seus próprios dados, o que levou o modelo a ser mais preciso e responsivo às suas necessidades, mas pode ser caro.

![LLMs deployment](../../../translated_images/Deploy.09224ecfe6a5ef47996fd0a44288772990139305451440c430662d43ac323ecd.br.png)

Fonte da imagem: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Engenharia de Prompt com Contexto

LLMs pré-treinados funcionam muito bem em tarefas de linguagem natural generalizadas, mesmo ao serem chamados com um prompt curto, como uma frase para completar ou uma pergunta – a chamada aprendizagem "zero-shot".

No entanto, quanto mais o usuário puder enquadrar sua consulta, com um pedido detalhado e exemplos – o Contexto – mais precisa e próxima das expectativas do usuário será a resposta. Neste caso, falamos sobre aprendizagem "one-shot" se o prompt incluir apenas um exemplo e "few-shot learning" se incluir múltiplos exemplos.
A engenharia de prompt com contexto é a abordagem mais econômica para começar.

### Geração Aumentada por Recuperação (RAG)

LLMs têm a limitação de que só podem usar os dados que foram usados durante seu treinamento para gerar uma resposta. Isso significa que eles não sabem nada sobre os fatos que aconteceram após seu processo de treinamento, e não podem acessar informações não públicas (como dados da empresa).
Isso pode ser superado através do RAG, uma técnica que aumenta o prompt com dados externos na forma de fragmentos de documentos, considerando os limites de comprimento do prompt. Isso é suportado por ferramentas de banco de dados vetorial (como [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) que recuperam os fragmentos úteis de fontes de dados variadas predefinidas e os adicionam ao Contexto do prompt.

Esta técnica é muito útil quando uma empresa não tem dados suficientes, tempo suficiente ou recursos para ajustar um LLM, mas ainda deseja melhorar o desempenho em uma carga de trabalho específica e reduzir os riscos de fabricações, ou seja, mistificação da realidade ou conteúdo prejudicial.

### Modelo Ajustado

O ajuste fino é um processo que aproveita o aprendizado por transferência para 'adaptar' o modelo a uma tarefa downstream ou resolver um problema específico. Diferentemente do aprendizado de poucos exemplos e RAG, resulta na geração de um novo modelo, com pesos e vieses atualizados. Requer um conjunto de exemplos de treinamento consistindo de uma única entrada (o prompt) e sua saída associada (a conclusão).
Esta seria a abordagem preferida se:

- **Usando modelos ajustados**. Uma empresa gostaria de usar modelos ajustados menos capazes (como modelos de incorporação) ao invés de modelos de alto desempenho, resultando em uma solução mais econômica e rápida.

- **Considerando latência**. A latência é importante para um caso de uso específico, então não é possível usar prompts muito longos ou o número de exemplos que devem ser aprendidos pelo modelo não se encaixa com o limite de comprimento do prompt.

- **Mantendo-se atualizado**. Uma empresa tem muitos dados de alta qualidade e rótulos de verdade fundamental e os recursos necessários para manter esses dados atualizados ao longo do tempo.

### Modelo Treinado

Treinar um LLM do zero é, sem dúvida, a abordagem mais difícil e complexa de adotar, exigindo quantidades massivas de dados, recursos qualificados e poder computacional adequado. Esta opção deve ser considerada apenas em um cenário onde uma empresa tem um caso de uso específico de domínio e uma grande quantidade de dados centrados no domínio.

## Verificação de conhecimento

Qual poderia ser uma boa abordagem para melhorar os resultados de conclusão de LLM?

1. Engenharia de prompt com contexto
1. RAG
1. Modelo ajustado

A:3, se você tem tempo, recursos e dados de alta qualidade, o ajuste fino é a melhor opção para se manter atualizado. No entanto, se você está procurando melhorar as coisas e está com falta de tempo, vale considerar o RAG primeiro.

## 🚀 Desafio

Leia mais sobre como você pode [usar RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para seu negócio.

## Ótimo trabalho, continue aprendendo

Após concluir esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Vá para a Lição 3, onde veremos como [construir com IA Generativa de forma responsável](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.