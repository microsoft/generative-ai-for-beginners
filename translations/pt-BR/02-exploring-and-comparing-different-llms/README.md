# Explorando e comparando diferentes LLMs

[![Explorando e comparando diferentes LLMs](../../../translated_images/pt-BR/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Clique na imagem acima para assistir ao vídeo desta lição_

Com a lição anterior, vimos como a IA Generativa está mudando o cenário tecnológico, como os Grandes Modelos de Linguagem (LLMs) funcionam e como uma empresa - como nossa startup - pode aplicá-los aos seus casos de uso e crescer! Neste capítulo, vamos comparar e contrastar diferentes tipos de grandes modelos de linguagem (LLMs) para entender seus prós e contras.

O próximo passo na jornada da nossa startup é explorar o cenário atual dos LLMs e entender quais são adequados para nosso caso de uso.

## Introdução

Esta lição abordará:

- Diferentes tipos de LLMs no cenário atual.
- Testar, iterar e comparar diferentes modelos para seu caso de uso no Azure.
- Como implantar um LLM.

## Objetivos de Aprendizagem

Após concluir esta lição, você será capaz de:

- Selecionar o modelo adequado para seu caso de uso.
- Entender como testar, iterar e melhorar o desempenho do seu modelo.
- Saber como as empresas implantam modelos.

## Entender diferentes tipos de LLMs

LLMs podem ter múltiplas categorização com base em sua arquitetura, dados de treinamento e caso de uso. Entender essas diferenças ajudará nossa startup a selecionar o modelo certo para o cenário e a entender como testar, iterar e melhorar o desempenho.

Existem muitos tipos diferentes de modelos LLM, a escolha do modelo depende do que você deseja usar, seus dados, quanto está disposto a pagar e mais.

Dependendo se você pretende usar os modelos para texto, áudio, vídeo, geração de imagens e assim por diante, pode optar por um tipo diferente de modelo.

- **Reconhecimento de áudio e fala**. Modelos do tipo Whisper ainda são úteis como modelos gerais de reconhecimento de fala, mas opções de produção agora também incluem modelos mais recentes de fala para texto, como `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` e variantes de diarização. Avalie cobertura de idiomas, diarização, suporte em tempo real, latência e custo para seu cenário. Saiba mais na [documentação de fala para texto da OpenAI](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Geração de imagens**. DALL-E e Midjourney são opções bem conhecidas para geração de imagens, mas as APIs atuais da OpenAI para imagens se concentram em modelos GPT Image como `gpt-image-2`, enquanto Stable Diffusion, Imagen, Flux e outras famílias de modelos também são escolhas comuns. Compare aderência ao prompt, suporte a edição, controle de estilo, requisitos de segurança e licenciamento. Saiba mais na [guia de geração de imagens da OpenAI](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) e no Capítulo 9 deste currículo.

- **Geração de texto**. Modelos de texto abrangem atualmente modelos de ponta, modelos de raciocínio, modelos menores e de baixa latência, e modelos de código aberto. Exemplos atuais incluem modelos OpenAI GPT-5.x, Anthropic Claude 4.x, Google Gemini 3.x, Meta Llama 4 e Mistral. Não escolha apenas pela data de lançamento ou preço; compare qualidade da tarefa, latência, janela de contexto, uso de ferramentas, comportamento de segurança, disponibilidade regional e custo total. O [catálogo de modelos Microsoft Foundry](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) é um bom lugar para comparar modelos disponíveis no Azure.

- **Multi-modalidade**. Muitos modelos atuais podem processar mais que texto. Alguns aceitam entrada de imagem, áudio ou vídeo; alguns podem chamar ferramentas; e modelos especializados podem gerar imagens, áudio ou vídeo. Por exemplo, modelos atuais da OpenAI suportam entrada de texto e imagem, modelos Gemini podem suportar texto, código, imagem, áudio e vídeo dependendo da variante, e Llama 4 Scout e Maverick são modelos nativamente multimodais de código aberto. Sempre verifique as modalidades de entrada e saída suportadas em cada ficha de modelo antes de construir um fluxo de trabalho ao redor dele.

Selecionar um modelo significa que você terá algumas capacidades básicas, que podem não ser suficientes, porém. Frequentemente, você tem dados específicos da empresa que precisam ser informados ao LLM de alguma forma. Existem algumas opções diferentes para abordar isso, que veremos nas próximas seções.

### Modelos Fundação versus LLMs

O termo Modelo Fundação foi [criado por pesquisadores de Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) e definido como um modelo de IA que segue alguns critérios, tais como:

- **São treinados utilizando aprendizado não supervisionado ou auto-supervisionado**, significando que são treinados com dados multimodais não rotulados, e não requerem anotação humana ou rotulagem de dados para seu processo de treinamento.
- **São modelos muito grandes**, baseados em redes neurais profundas treinadas em bilhões de parâmetros.
- **Geralmente destinam-se a servir como uma ‘fundação’ para outros modelos**, ou seja, podem ser usados como ponto de partida para que outros modelos sejam construídos por cima deles, o que pode ser feito através do fine-tuning.

![Modelos Fundação versus LLMs](../../../translated_images/pt-BR/FoundationModel.e4859dbb7a825c94.webp)

Fonte da imagem: [Guia Essencial para Modelos Fundação e Grandes Modelos de Linguagem | por Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Para clarificar ainda mais essa distinção, vamos usar o ChatGPT como exemplo histórico. Versões iniciais do ChatGPT usavam GPT-3.5 como modelo fundação. A OpenAI então utilizou dados específicos de chat e técnicas de alinhamento para criar uma versão ajustada que performava melhor em cenários de conversação, como chatbots. Serviços modernos de IA frequentemente roteiam entre várias variantes de modelo, então o nome do serviço e o nome do modelo subjacente nem sempre são a mesma coisa.

![Modelo Fundação](../../../translated_images/pt-BR/Multimodal.2c389c6439e0fc51.webp)

Fonte da imagem: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modelos Open-Weight/Open-Source versus Proprietários

Outra forma de categorizar LLMs é considerar se são open-weight, open-source ou proprietários.

Modelos open-source e open-weight disponibilizam artefatos do modelo para inspeção, download ou personalização, mas suas licenças diferem. Alguns são totalmente open source, enquanto outros são modelos open-weight com restrições de uso. Podem ser úteis quando uma empresa precisa de mais controle sobre implantação, localização de dados, custo ou personalização. Contudo, equipes ainda precisam revisar termos de licença, custos de serviço, manutenção, atualizações de segurança e qualidade de avaliação antes de usá-los em produção. Exemplos incluem [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), alguns [modelos Mistral](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) e muitos modelos hospedados no [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Modelos proprietários são de propriedade e hospedados por um provedor. Esses modelos são geralmente otimizados para uso gerenciado em produção e podem oferecer suporte forte, sistemas de segurança, integração com ferramentas e escalabilidade. Entretanto, clientes geralmente não podem inspecionar ou modificar os pesos do modelo, e devem revisar os termos do provedor para privacidade, retenção, conformidade e uso aceitável. Exemplos incluem [modelos OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) e [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding versus Geração de Imagem versus Geração de Texto e Código

LLMs também podem ser categorizados pelo tipo de saída que geram.

Embeddings são um conjunto de modelos que podem converter texto em uma forma numérica, chamada embedding, que é uma representação numérica do texto de entrada. Embeddings facilitam que máquinas compreendam relacionamentos entre palavras ou sentenças e podem ser usados como entrada por outros modelos, como modelos de classificação ou agrupamento que têm melhor desempenho com dados numéricos. Modelos de embedding são frequentemente usados para transferência de aprendizado, onde um modelo é construído para uma tarefa substituta com abundância de dados, e então os pesos do modelo (embeddings) são reaproveitados para outras tarefas posteriores. Um exemplo dessa categoria é [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/pt-BR/Embedding.c3708fe988ccf760.webp)

Modelos de geração de imagens são modelos que geram imagens. Esses modelos são usados frequentemente para edição de imagens, síntese de imagens e tradução de imagens. Eles geralmente são treinados em grandes conjuntos de dados de imagens, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar novas imagens ou para editar imagens existentes com técnicas de inpainting, super-resolução e colorização. Exemplos incluem [modelos GPT Image](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [modelos Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) e modelos Imagen.

![Geração de imagens](../../../translated_images/pt-BR/Image.349c080266a763fd.webp)

Modelos de geração de texto e código são modelos que geram texto ou código. Eles são usados frequentemente para sumarização de texto, tradução e respostas a perguntas. Modelos de geração de texto são frequentemente treinados em grandes conjuntos de dados de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), e podem ser usados para gerar texto novo ou para responder perguntas. Modelos de geração de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), são treinados em grandes conjuntos de dados de código, como GitHub, e podem ser usados para gerar novo código ou corrigir bugs em código existente.

![Geração de texto e código](../../../translated_images/pt-BR/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus Somente Decoder

Para falar sobre os diferentes tipos de arquiteturas dos LLMs, vamos usar uma analogia.

Imagine que seu gerente lhe deu a tarefa de escrever um quiz para os alunos. Você tem dois colegas; um cuida de criar o conteúdo e o outro de revisá-lo.

O criador de conteúdo é como um modelo somente decoder: ele pode olhar para o tópico, ver o que você já escreveu e então continuar gerando conteúdo baseado nesse contexto. Ele é muito bom em escrever conteúdo envolvente e informativo, mas nem sempre é a melhor escolha quando a tarefa é apenas classificar, recuperar ou codificar informações. Exemplos de famílias de modelos somente decoder incluem GPT e Llama.

O revisor é como um modelo somente encoder, ele olha o material escrito e as respostas, percebendo a relação entre eles e entendendo o contexto, mas não é bom em gerar conteúdo. Um exemplo de modelo somente encoder seria o BERT.

Imagine que também temos alguém que pode criar e revisar o quiz, este é um modelo Encoder-Decoder. Alguns exemplos seriam BART e T5.

### Serviço versus Modelo

Agora, vamos falar sobre a diferença entre um serviço e um modelo. Um serviço é um produto oferecido por um Provedor de Serviços em Nuvem, e geralmente é uma combinação de modelos, dados e outros componentes. Um modelo é o componente central de um serviço, frequentemente um modelo fundação, como um LLM.

Serviços são frequentemente otimizados para uso em produção e geralmente são mais fáceis de usar que modelos, via interface gráfica. Contudo, serviços nem sempre são gratuitos e podem requerer assinatura ou pagamento para uso, em troca da utilização dos equipamentos e recursos do proprietário do serviço, otimizando despesas e escalabilidade facilmente. Um exemplo de serviço é o [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), que oferece um plano pay-as-you-go, significando que os usuários são cobrados proporcionalmente ao uso do serviço. O Azure OpenAI Service também oferece segurança em nível empresarial e um framework de IA responsável sobre as capacidades dos modelos.

Modelos são os artefatos da rede neural: parâmetros, pesos, arquitetura, tokenizer e configuração de suporte. Executar um modelo localmente ou em ambiente privado requer hardware adequado, infraestrutura de serviço, monitoramento e licença open-source/open-weight compatível ou licença comercial. Modelos open-weight como Llama 4 ou Mistral podem ser auto-hospedados, mas ainda exigem poder computacional e expertise operacional.

## Como testar e iterar com diferentes modelos para entender o desempenho no Azure


Depois que nossa equipe explorou o cenário atual dos LLMs e identificou alguns bons candidatos para seus cenários, o próximo passo é testá-los em seus dados e em sua carga de trabalho. Este é um processo iterativo, feito por meio de experimentos e medições.
A maioria dos modelos que mencionamos nos parágrafos anteriores (modelos da OpenAI, modelos de peso aberto como Llama 4 e Mistral, e modelos da Hugging Face) estão disponíveis em [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), anteriormente Azure AI Studio/Azure AI Foundry, é uma plataforma unificada do Azure para construir aplicativos e agentes de IA. Ela ajuda os desenvolvedores a gerenciar o ciclo de vida desde experimentação e avaliação até implantação, monitoramento e governança. O catálogo de modelos no Microsoft Foundry permite ao usuário:

- Encontrar o modelo fundamental de interesse no catálogo, incluindo modelos vendidos pela Azure e modelos de parceiros e provedores da comunidade. Usuários podem filtrar por tarefa, provedor, licença, opção de implantação ou nome.

![Catálogo de modelos](../../../translated_images/pt-BR/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Revisar a ficha do modelo, incluindo uma descrição detalhada do uso pretendido e dos dados de treinamento, exemplos de código e resultados de avaliação na biblioteca interna de avaliações.

![Ficha do modelo](../../../translated_images/pt-BR/ModelCard.598051692c6e400d.webp)

- Comparar benchmarks entre modelos e conjuntos de dados disponíveis na indústria para avaliar qual atende ao cenário de negócio, através do painel [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Benchmarks de modelos](../../../translated_images/pt-BR/ModelBenchmarks.254cb20fbd06c03a.webp)

- Fazer fine-tuning em modelos suportados com dados de treinamento personalizados para melhorar o desempenho do modelo em uma carga de trabalho específica, aproveitando as capacidades de experimentação e rastreamento do Microsoft Foundry.

![Fine-tuning de modelo](../../../translated_images/pt-BR/FineTuning.aac48f07142e36fd.webp)

- Implantar o modelo pré-treinado original ou a versão fine-tuned em um endpoint remoto de inferência em tempo real, usando opções de computação gerenciada ou implantação serverless, para permitir que aplicações o consumam.

![Implantação do modelo](../../../translated_images/pt-BR/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Nem todos os modelos no catálogo estão atualmente disponíveis para fine-tuning e/ou implantação pay-as-you-go. Verifique a ficha do modelo para detalhes sobre as capacidades e limitações dele.

## Melhorando os resultados dos LLMs

Exploramos com nossa equipe de startup diferentes tipos de LLMs e uma plataforma na nuvem (Microsoft Foundry) que nos permite comparar diferentes modelos, avaliá-los com dados de teste, melhorar desempenho e implantá-los em endpoints de inferência.

Mas quando eles devem considerar fazer fine-tuning de um modelo em vez de usar um pré-treinado? Existem outras abordagens para melhorar o desempenho do modelo em cargas de trabalho específicas?

Existem várias abordagens que uma empresa pode usar para obter os resultados necessários de um LLM. Você pode selecionar diferentes tipos de modelos com diferentes graus de treinamento ao implantar um LLM em produção, com diferentes níveis de complexidade, custo e qualidade. Aqui estão algumas abordagens diferentes:

- **Engenharia de prompt com contexto**. A ideia é fornecer contexto suficiente quando você fizer a solicitação para garantir que obtenha as respostas desejadas.

- **Retrieval Augmented Generation, RAG**. Seus dados podem existir em um banco de dados ou endpoint web, por exemplo; para garantir que esses dados, ou um subconjunto deles, sejam incluídos no momento da solicitação, você pode buscar os dados relevantes e tornar isso parte do prompt do usuário.

- **Modelo fine-tuned**. Aqui, você treinou o modelo mais profundamente com seus próprios dados, o que fez com que o modelo fosse mais preciso e responsivo às suas necessidades, mas pode ser custoso.

![Implantação de LLMs](../../../translated_images/pt-BR/Deploy.18b2d27412ec8c02.webp)

Fonte da imagem: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Engenharia de Prompt com Contexto

LLMs pré-treinados funcionam muito bem em tarefas de linguagem natural generalizadas, mesmo quando chamados com um prompt curto, como uma frase para completar ou uma pergunta – o chamado aprendizado "zero-shot".

Contudo, quanto mais o usuário puder enquadrar sua consulta, com um pedido detalhado e exemplos – o Contexto – mais precisa e próxima das expectativas do usuário a resposta será. Neste caso, chamamos de aprendizado “one-shot” se o prompt inclui apenas um exemplo, e “few-shot learning” se inclui múltiplos exemplos.
Engenharia de prompt com contexto é a abordagem mais custo-efetiva para começar.

### Retrieval Augmented Generation (RAG)

LLMs possuem a limitação de que podem usar apenas os dados que foram utilizados durante seu treinamento para gerar uma resposta. Isso significa que eles não sabem nada sobre fatos que ocorreram depois do processo de treinamento e não podem acessar informações não públicas (como dados da empresa).
Isso pode ser superado por meio do RAG, uma técnica que aumenta o prompt com dados externos na forma de fragmentos de documentos, considerando os limites de tamanho do prompt. Isso é suportado por ferramentas de banco de dados vetoriais (como [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) que recuperam os fragmentos úteis de fontes de dados variadas e pré-definidas e os adicionam ao contexto do prompt.

Essa técnica é muito útil quando a empresa não tem dados suficientes, tempo suficiente ou recursos para fazer fine-tuning de um LLM, mas ainda deseja melhorar o desempenho em uma carga de trabalho específica e reduzir riscos de respostas alucinadas, desatualizadas ou sem suporte.

### Modelo fine-tuned

Fine-tuning é um processo que aproveita o transfer learning para ‘adaptar’ o modelo a uma tarefa específica ou para resolver um problema específico. Diferente do few-shot learning e do RAG, resulta na geração de um novo modelo, com pesos e vieses atualizados. Requer um conjunto de exemplos de treinamento consistente em uma única entrada (o prompt) e sua saída associada (a conclusão).
Esta seria a abordagem preferida se:

- **Usando modelos menores específicos para a tarefa**. Uma empresa gostaria de fazer fine-tuning em um modelo menor para uma tarefa estreita em vez de constantemente solicitar um modelo maior na fronteira, resultando em uma solução mais custo-efetiva e rápida.

- **Considerando a latência**. A latência é importante para um caso de uso específico, então não é possível usar prompts muito longos ou o número de exemplos que deveriam ser aprendidos não se encaixa no limite de tamanho do prompt.

- **Adaptando comportamento estável**. A empresa possui muitos exemplos de alta qualidade e quer que o modelo siga consistentemente um padrão de tarefa, formato de saída, tom ou estilo específico do domínio. Se o problema principal são fatos recentes ou conhecimento privado que muda frequentemente, use RAG em vez de confiar somente no fine-tuning.

### Modelo treinado

Treinar um LLM desde o início é sem dúvida a abordagem mais difícil e complexa de se adotar, requerendo enormes quantidades de dados, recursos qualificados e poder computacional apropriado. Esta opção deve ser considerada apenas em um cenário onde a empresa tem um caso de uso específico de domínio e uma grande quantidade de dados centrados no domínio.

## Verificação de conhecimento

Qual poderia ser uma boa abordagem para melhorar os resultados de conclusão de LLM?

1. Engenharia de prompt com contexto
1. RAG
1. Modelo fine-tuned

R: Todos os três podem ajudar. Comece com engenharia de prompt e contexto para melhorias rápidas, e use RAG quando o modelo precisar de fatos atuais ou dados empresariais privados. Escolha fine-tuning quando você tiver exemplos de alta qualidade suficientes e precisar que o modelo siga consistentemente uma tarefa, formato, tom ou padrão do domínio.

## 🚀 Desafio

Leia mais sobre como você pode [usar RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para seu negócio.

## Excelente trabalho, continue seu aprendizado

Depois de completar esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Vá para a Lição 3 onde veremos como [construir com IA Generativa Responsavelmente](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->