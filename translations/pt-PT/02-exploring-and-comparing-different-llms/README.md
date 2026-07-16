# Explorar e comparar diferentes LLMs

[![Explorar e comparar diferentes LLMs](../../../translated_images/pt-PT/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Clique na imagem acima para ver o vídeo desta lição_

Na lição anterior, vimos como a IA Generativa está a mudar o panorama tecnológico, como funcionam os Grandes Modelos de Linguagem (LLMs) e como um negócio - como a nossa startup - pode aplicá-los nos seus casos de uso e crescer! Neste capítulo, vamos comparar e contrastar diferentes tipos de grandes modelos de linguagem (LLMs) para compreender as suas vantagens e desvantagens.

O próximo passo na jornada da nossa startup é explorar o panorama atual dos LLMs e entender quais são adequados para o nosso caso de uso.

## Introdução

Esta lição irá abordar:

- Diferentes tipos de LLMs no panorama atual.
- Testar, iterar e comparar diferentes modelos para o seu caso de uso no Azure.
- Como implementar um LLM.

## Objetivos de Aprendizagem

Após completar esta lição, será capaz de:

- Selecionar o modelo certo para o seu caso de uso.
- Compreender como testar, iterar e melhorar o desempenho do seu modelo.
- Saber como as empresas implementam modelos.

## Compreender diferentes tipos de LLMs

Os LLMs podem ter múltiplas categorização baseadas na sua arquitetura, dados de treino e caso de uso. Compreender estas diferenças ajudará a nossa startup a selecionar o modelo certo para o cenário e a entender como testar, iterar e melhorar o desempenho.

Existem muitos tipos diferentes de modelos LLM, a sua escolha depende do que pretende usar, dos seus dados, do quanto está disposto a pagar e outros fatores.

Dependendo se pretende usar os modelos para texto, áudio, vídeo, geração de imagens e assim por diante, poderá optar por um tipo diferente de modelo.

- **Reconhecimento de áudio e fala**. Modelos estilo Whisper ainda são modelos úteis e gerais para reconhecimento de fala, mas as opções de produção incluem agora modelos mais recentes de fala-para-texto, como `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` e variantes de diarização. Avalie a cobertura linguística, diarização, suporte em tempo real, latência e custo para o seu cenário. Saiba mais na [documentação de fala-para-texto da OpenAI](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Geração de imagens**. DALL-E e Midjourney são opções bem conhecidas para geração de imagens, mas as atuais APIs de imagem da OpenAI focam nos modelos GPT Image, como `gpt-image-2`, enquanto Stable Diffusion, Imagen, Flux e outras famílias de modelos também são escolhas comuns. Compare aderência a prompts, suporte à edição, controlo de estilo, requisitos de segurança e licenciamento. Saiba mais no [guia de geração de imagens da OpenAI](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) e no Capítulo 9 deste currículo.

- **Geração de texto**. Modelos de texto cobrem modelos de ponta, modelos de raciocínio, modelos menores de baixa latência e modelos de pesos abertos. Exemplos atuais incluem os modelos GPT-5.x da OpenAI, os modelos Claude 4.x da Anthropic, os modelos Gemini 3.x do Google, os modelos Llama 4 da Meta e os modelos Mistral. Não escolha apenas pela data de lançamento ou preço; compare qualidade em tarefas, latência, janela de contexto, uso de ferramentas, comportamento de segurança, disponibilidade regional e custo total. O [catálogo de modelos Microsoft Foundry](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) é um bom local para comparar modelos disponíveis no Azure.

- **Multimodalidade**. Muitos modelos atuais podem processar mais do que texto. Alguns aceitam entradas de imagem, áudio ou vídeo; outros podem chamar ferramentas; e modelos especializados podem gerar imagens, áudio ou vídeo. Por exemplo, os modelos atuais da OpenAI suportam entrada de texto e imagem, os modelos Gemini podem suportar texto, código, imagem, áudio e vídeo dependendo da variante, e Llama 4 Scout e Maverick são modelos multimodais de pesos abertos nativos. Verifique sempre cada ficha técnica para as modalidades suportadas de entrada e saída antes de construir um fluxo de trabalho em torno dele.

Selecionar um modelo significa que se obtém algumas capacidades básicas, que podem não ser suficientes. Frequentemente tem dados específicos da empresa que de algum modo precisa de comunicar ao LLM. Existem algumas escolhas diferentes de como abordar isso, que serão abordadas nas próximas secções.

### Modelos Fundamentais versus LLMs

O termo Modelo Fundamental foi [criado por investigadores de Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) e definido como um modelo de IA que segue alguns critérios, tais como:

- **São treinados usando aprendizagem não supervisionada ou auto-supervisionada**, ou seja, são treinados em dados multimodais não rotulados, e não exigem anotação humana ou rotulagem de dados para o seu processo de treino.
- **São modelos muito grandes**, baseados em redes neurais muito profundas treinadas com bilhões de parâmetros.
- **Normalmente destinam-se a servir como ‘fundamento’ para outros modelos**, significando que podem ser usados como ponto de partida para construir outros modelos em cima, o que pode ser feito através de fine-tuning.

![Modelos Fundamentais versus LLMs](../../../translated_images/pt-PT/FoundationModel.e4859dbb7a825c94.webp)

Fonte da imagem: [Guia Essencial para Modelos Fundamentais e Grandes Modelos de Linguagem | por Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Para clarificar ainda mais esta distinção, tomemos o ChatGPT como exemplo histórico. As versões iniciais do ChatGPT usaram o GPT-3.5 como modelo fundamental. A OpenAI depois usou dados específicos de chat e técnicas de alinhamento para criar uma versão afinada que teve melhor desempenho em cenários conversacionais, como chatbots. Serviços modernos de IA frequentemente alternam entre várias variantes de modelos, por isso o nome do serviço e o nome do modelo subjacente nem sempre coincidem.

![Modelo Fundamental](../../../translated_images/pt-PT/Multimodal.2c389c6439e0fc51.webp)

Fonte da imagem: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modelos Open-Weight/Open-Source versus Proprietários

Outra forma de categorizar os LLMs é se são open-weight, open-source ou proprietários.

Modelos open-source e open-weight disponibilizam artefatos do modelo para inspeção, download ou personalização, mas as suas licenças diferem. Alguns são totalmente open source, enquanto outros são modelos open-weight com restrições de uso. Podem ser úteis quando uma empresa precisa de mais controlo sobre a implementação, localização dos dados, custo ou personalização. Contudo, as equipas ainda precisam de rever os termos de licença, custos de serviço, manutenção, atualizações de segurança e qualidade da avaliação antes de os usar em produção. Exemplos incluem [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), alguns [modelos Mistral](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) e muitos modelos hospedados no [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Modelos proprietários são propriedade e hospedados por um fornecedor. Estes modelos são frequentemente otimizados para uso gerido em produção e podem oferecer suporte robusto, sistemas de segurança, integração de ferramentas e escala. Contudo, os clientes geralmente não podem inspecionar nem modificar os pesos do modelo, devendo rever os termos do fornecedor relativos a privacidade, retenção, conformidade e uso aceitável. Exemplos incluem os [modelos OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) e [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding versus Geração de Imagens versus Geração de Texto e Código

Os LLMs também podem ser categorizados pelo tipo de output que geram.

Embeddings são um conjunto de modelos que convertem texto para uma forma numérica, chamada embedding, que é uma representação numérica do texto de entrada. Embeddings facilitam para as máquinas entender as relações entre palavras ou frases e podem ser usados como inputs por outros modelos, como modelos de classificação ou de clusterização, que têm melhor desempenho em dados numéricos. Modelos de embedding são frequentemente usados para transferência de aprendizagem, onde um modelo é construído para uma tarefa substituta para a qual existem muitos dados, e depois os pesos do modelo (embeddings) são reutilizados para outras tarefas posteriores. Um exemplo desta categoria é [embeddings da OpenAI](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/pt-PT/Embedding.c3708fe988ccf760.webp)

Modelos de geração de imagens são modelos que geram imagens. Estes modelos são frequentemente usados para edição de imagem, síntese de imagem e tradução de imagem. Modelos de geração de imagens são normalmente treinados em grandes conjuntos de imagens, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar novas imagens ou para editar imagens existentes com técnicas de inpainting, super-resolução e colorização. Exemplos incluem [modelos GPT Image](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [modelos Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) e modelos Imagen.

![Geração de imagens](../../../translated_images/pt-PT/Image.349c080266a763fd.webp)

Modelos de geração de texto e código são modelos que geram texto ou código. Estes modelos são frequentemente usados para sumarização de texto, tradução e resposta a perguntas. Modelos de geração de texto são frequentemente treinados em grandes conjuntos de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar novo texto ou responder a perguntas. Modelos de geração de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), são frequentemente treinados em grandes conjuntos de código, como GitHub, e podem ser usados para gerar novo código ou para corrigir bugs em código existente.

![Geração de texto e código](../../../translated_images/pt-PT/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus Decoder-only

Para falar dos diferentes tipos de arquiteturas dos LLMs, vamos usar uma analogia.

Imagine que o seu gerente lhe deu uma tarefa para escrever um questionário para os estudantes. Tem dois colegas; um supervisiona a criação do conteúdo e o outro supervisiona a revisão.

O criador de conteúdo é como um modelo apenas-decoder: pode ver o tema, o que já escreveu e continuar a gerar conteúdo com base nesse contexto. São muito bons a escrever conteúdo envolvente e informativo, mas nem sempre são a melhor escolha quando a tarefa é apenas classificar, recuperar ou codificar informação. Exemplos de famílias de modelos apenas-decoder incluem os modelos GPT e Llama.

O revisor é como um modelo apenas-encoder, olha para o curso escrito e as respostas, nota a relação entre eles e entende o contexto, mas não é bom a gerar conteúdo. Um exemplo de modelo apenas-encoder seria o BERT.

Imagine que pudéssemos ter alguém que criasse e revisasse o questionário, esse é um modelo Encoder-Decoder. Alguns exemplos seriam BART e T5.

### Serviço versus Modelo

Agora, vamos falar sobre a diferença entre um serviço e um modelo. Um serviço é um produto oferecido por um Provedor de Serviços Cloud, e é frequentemente uma combinação de modelos, dados e outros componentes. Um modelo é o componente central de um serviço, e é frequentemente um modelo fundamental, como um LLM.

Os serviços são muitas vezes otimizados para uso em produção e são frequentemente mais fáceis de usar do que modelos, via uma interface gráfica. Contudo, os serviços nem sempre estão disponíveis gratuitamente, podendo requerer uma subscrição ou pagamento para usar, em troca da utilização dos equipamentos e recursos do proprietário do serviço, otimizando despesas e escalando facilmente. Um exemplo de serviço é o [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), que oferece um plano de tarifa pay-as-you-go, significando que os utilizadores são cobrados proporcionalmente ao uso do serviço. O Azure OpenAI Service oferece também segurança empresarial e um quadro de IA responsável em cima das capacidades dos modelos.

Os modelos são os artefatos da rede neural: parâmetros, pesos, arquitetura, tokenizador e configuração de suporte. Executar um modelo localmente ou num ambiente privado requer hardware adequado, infraestrutura de serviço, monitorização e uma licença compatível open-source/open-weight ou comercial. Modelos open-weight como Llama 4 ou Mistral podem ser alojados autonomamente, mas ainda requerem capacidade computacional e experiência operacional.

## Como testar e iterar com diferentes modelos para entender o desempenho no Azure


Depois da nossa equipa explorar o panorama atual dos LLMs e identificar alguns bons candidatos para os seus cenários, o próximo passo é testá-los nos seus dados e na sua carga de trabalho. Este é um processo iterativo, realizado por experiências e medições.
A maioria dos modelos mencionados nos parágrafos anteriores (modelos OpenAI, modelos de peso aberto como Llama 4 e Mistral, e modelos Hugging Face) estão disponíveis no [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), anteriormente Azure AI Studio/Azure AI Foundry, é uma plataforma Azure unificada para construir aplicações e agentes de IA. Ajuda os desenvolvedores a gerir o ciclo de vida desde a experimentação e avaliação até à implementação, monitorização e governação. O catálogo de modelos no Microsoft Foundry permite ao utilizador:

- Encontrar o modelo base de interesse no catálogo, incluindo modelos vendidos pela Azure e modelos de parceiros e fornecedores comunitários. Os utilizadores podem filtrar por tarefa, fornecedor, licença, opção de implementação ou nome.

![Catálogo de modelos](../../../translated_images/pt-PT/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Rever o cartão do modelo, incluindo uma descrição detalhada do uso pretendido e dados de treino, exemplos de código e resultados da avaliação na biblioteca interna de avaliações.

![Cartão de modelo](../../../translated_images/pt-PT/ModelCard.598051692c6e400d.webp)

- Comparar benchmarks entre modelos e conjuntos de dados disponíveis na indústria para avaliar qual cumpre o cenário de negócio, através do painel [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Benchmarks de modelos](../../../translated_images/pt-PT/ModelBenchmarks.254cb20fbd06c03a.webp)

- Ajustar modelos suportados em dados de treino personalizados para melhorar o desempenho do modelo numa carga de trabalho específica, aproveitando as capacidades de experimentação e rastreamento do Microsoft Foundry.

![Ajuste fino do modelo](../../../translated_images/pt-PT/FineTuning.aac48f07142e36fd.webp)

- Implementar o modelo pré-treinado original ou a versão ajustada num endpoint remoto de inferência em tempo real, usando opções de computação gerida ou serverless, para permitir que aplicações o consumam.

![Implementação do modelo](../../../translated_images/pt-PT/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Nem todos os modelos do catálogo estão atualmente disponíveis para ajuste fino e/ou implementação pay-as-you-go. Verifique o cartão do modelo para detalhes sobre as capacidades e limitações do modelo.

## Melhorar resultados de LLM

Explorámos com a nossa equipa de startup diferentes tipos de LLMs e uma plataforma na cloud (Microsoft Foundry) que nos permite comparar diferentes modelos, avaliá-los em dados de teste, melhorar o desempenho e implementá-los em endpoints de inferência.

Mas quando devem considerar ajustar um modelo em vez de usar um pré-treinado? Existem outras abordagens para melhorar o desempenho do modelo em cargas de trabalho específicas?

Existem várias abordagens que uma empresa pode usar para obter os resultados que necessita de um LLM. Podemos selecionar diferentes tipos de modelos com diferentes graus de treino ao implementar um LLM em produção, com diferentes níveis de complexidade, custo e qualidade. Aqui estão algumas abordagens distintas:

- **Engenharia de prompt com contexto**. A ideia é fornecer contexto suficiente ao dar o comando para garantir que obtém as respostas necessárias.

- **Generação Aumentada por Recuperação, RAG**. Os seus dados podem existir numa base de dados ou endpoint web, por exemplo, para garantir que esses dados, ou um subconjunto deles, são incluídos no momento do prompt, pode buscar os dados relevantes e torná-los parte do prompt do utilizador.

- **Modelo ajustado**. Aqui, treinou o modelo adicionalmente nos seus próprios dados, o que levou o modelo a ser mais exato e responsivo às suas necessidades, mas pode ser dispendioso.

![Implementação de LLMs](../../../translated_images/pt-PT/Deploy.18b2d27412ec8c02.webp)

Fonte da imagem: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Engenharia de Prompt com Contexto

Os LLMs pré-treinados funcionam muito bem em tarefas generalizadas de linguagem natural, mesmo usando um prompt curto, como uma frase a completar ou uma pergunta – a chamada aprendizagem “zero-shot”.

No entanto, quanto mais o utilizador conseguir enquadrar a sua consulta, com um pedido detalhado e exemplos – o Contexto – mais precisa e próxima das expectativas do utilizador será a resposta. Neste caso, falamos em aprendizagem “one-shot” se o prompt incluir apenas um exemplo e “few-shot learning” se incluir múltiplos exemplos.
A engenharia de prompt com contexto é a abordagem mais económica para começar.

### Geração Aumentada por Recuperação (RAG)

Os LLMs têm a limitação de que podem usar apenas os dados que foram usados durante o seu treino para gerar uma resposta. Isto significa que não sabem nada sobre factos que ocorreram após o seu processo de treino, e não podem aceder a informações não públicas (como dados da empresa).
Isto pode ser ultrapassado através do RAG, uma técnica que amplia o prompt com dados externos na forma de fragmentos de documentos, considerando os limites de comprimento do prompt. Isto é suportado por ferramentas de base de dados Vetoriais (como o [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) que recuperam os fragmentos úteis de variadas fontes de dados pré-definidas e adicionam-nos ao Contexto do prompt.

Esta técnica é muito útil quando uma empresa não tem dados suficientes, tempo suficiente ou recursos para ajustar um LLM, mas ainda assim deseja melhorar o desempenho numa carga de trabalho específica e reduzir riscos de respostas alucinadas, desatualizadas ou sem suporte.

### Modelo ajustado

O ajuste fino é um processo que tira partido da aprendizagem por transferência para ‘adaptar’ o modelo a uma tarefa descendente ou para resolver um problema específico. Diferente da aprendizagem few-shot e do RAG, resulta na geração de um novo modelo, com pesos e biases atualizados. Requer um conjunto de exemplos de treino consistindo numa única entrada (o prompt) e o seu output associado (a conclusão).
Esta seria a abordagem preferida se:

- **Usar modelos menores específicos de tarefa**. Uma empresa gostaria de ajustar um modelo menor para uma tarefa específica em vez de usar repetidamente prompts num modelo maior mais avançado, resultando numa solução mais económica e rápida.

- **Considerar a latência**. A latência é importante para um caso de uso específico, então não é possível usar prompts muito longos ou o número de exemplos que o modelo deve aprender não se encaixa no limite de comprimento do prompt.

- **Adaptar comportamento estável**. Uma empresa tem muitos exemplos de alta qualidade e quer que o modelo siga consistentemente um padrão de tarefa, formato de output, tom ou estilo específico do domínio. Se o principal problema forem factos recentes ou conhecimento privado que mudam frequentemente, use RAG em vez de confiar apenas no ajuste fino.

### Modelo treinado

Treinar um LLM do zero é, sem dúvida, a abordagem mais difícil e mais complexa de adotar, exigindo uma enorme quantidade de dados, recursos especializados e poder computacional apropriado. Esta opção deve ser considerada apenas num cenário onde uma empresa tem um caso de uso específico de domínio e uma grande quantidade de dados centrados no domínio.

## Verificação de Conhecimento

Qual poderia ser uma boa abordagem para melhorar os resultados das conclusões de um LLM?

1. Engenharia de prompt com contexto
1. RAG
1. Modelo ajustado

R: Os três podem ajudar. Comece com engenharia de prompt e contexto para melhorias rápidas, e use RAG quando o modelo precisar de factos atuais ou dados privados da empresa. Escolha ajuste fino quando tiver exemplos de alta qualidade suficientes e precisar que o modelo siga consistentemente uma tarefa, formato, tom ou padrão de domínio.

## 🚀 Desafio

Leia mais sobre como pode [usar RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para o seu negócio.

## Excelente Trabalho, Continue a Sua Aprendizagem

Depois de concluir esta lição, consulte a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a melhorar o seu conhecimento em IA Generativa!

Dirija-se à Lição 3 onde veremos como [construir com IA Generativa de forma Responsável](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->