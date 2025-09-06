<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:16:04+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "pt"
}
-->
[![Modelos Open Source](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.pt.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Introdução

O mundo dos LLMs open source é empolgante e está em constante evolução. Esta lição tem como objetivo oferecer uma visão aprofundada sobre modelos open source. Se procura informações sobre como os modelos proprietários se comparam aos modelos open source, consulte a lição ["Explorando e Comparando Diferentes LLMs"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Esta lição também abordará o tema de ajuste fino, mas uma explicação mais detalhada pode ser encontrada na lição ["Ajuste Fino de LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Objetivos de aprendizagem

- Compreender os Modelos Open Source
- Entender os benefícios de trabalhar com Modelos Open Source
- Explorar os modelos disponíveis no Hugging Face e no Azure AI Studio

## O que são Modelos Open Source?

O software open source desempenhou um papel crucial no crescimento da tecnologia em diversos campos. A Open Source Initiative (OSI) definiu [10 critérios para software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) ser classificado como open source. O código-fonte deve ser compartilhado abertamente sob uma licença aprovada pela OSI.

Embora o desenvolvimento de LLMs tenha elementos semelhantes ao desenvolvimento de software, o processo não é exatamente o mesmo. Isso gerou muitas discussões na comunidade sobre a definição de open source no contexto dos LLMs. Para que um modelo esteja alinhado com a definição tradicional de open source, as seguintes informações devem estar publicamente disponíveis:

- Conjuntos de dados usados para treinar o modelo.
- Pesos completos do modelo como parte do treinamento.
- O código de avaliação.
- O código de ajuste fino.
- Pesos completos do modelo e métricas de treinamento.

Atualmente, existem poucos modelos que atendem a esses critérios. O [modelo OLMo criado pelo Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) é um exemplo que se enquadra nessa categoria.

Para esta lição, referiremos os modelos como "modelos abertos" daqui em diante, pois podem não atender aos critérios acima no momento da escrita.

## Benefícios dos Modelos Abertos

**Altamente Personalizáveis** - Como os modelos abertos são lançados com informações detalhadas de treinamento, pesquisadores e desenvolvedores podem modificar os componentes internos do modelo. Isso permite a criação de modelos altamente especializados ajustados para uma tarefa ou área de estudo específica. Alguns exemplos incluem geração de código, operações matemáticas e biologia.

**Custo** - O custo por token para usar e implementar esses modelos é menor do que o dos modelos proprietários. Ao construir aplicações de IA Generativa, é importante avaliar o desempenho versus o preço ao trabalhar com esses modelos para o seu caso de uso.

![Custo do Modelo](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.pt.png)  
Fonte: Artificial Analysis

**Flexibilidade** - Trabalhar com modelos abertos permite flexibilidade em termos de usar diferentes modelos ou combiná-los. Um exemplo disso é o [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), onde o utilizador pode selecionar o modelo diretamente na interface:

![Escolher Modelo](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.pt.png)

## Explorando Diferentes Modelos Abertos

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), desenvolvido pela Meta, é um modelo aberto otimizado para aplicações baseadas em chat. Isso deve-se ao seu método de ajuste fino, que incluiu uma grande quantidade de diálogos e feedback humano. Com este método, o modelo produz resultados mais alinhados às expectativas humanas, proporcionando uma melhor experiência ao utilizador.

Alguns exemplos de versões ajustadas do Llama incluem [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), que se especializa em japonês, e [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), que é uma versão aprimorada do modelo base.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) é um modelo aberto com forte foco em alto desempenho e eficiência. Ele utiliza a abordagem Mixture-of-Experts, que combina um grupo de modelos especializados em um sistema onde, dependendo da entrada, certos modelos são selecionados para uso. Isso torna a computação mais eficaz, pois os modelos abordam apenas as entradas nas quais são especializados.

Alguns exemplos de versões ajustadas do Mistral incluem [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), focado na área médica, e [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), que realiza cálculos matemáticos.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) é um LLM criado pelo Technology Innovation Institute (**TII**). O Falcon-40B foi treinado com 40 bilhões de parâmetros, demonstrando desempenho superior ao GPT-3 com menor orçamento computacional. Isso deve-se ao uso do algoritmo FlashAttention e da atenção multiquery, que reduz os requisitos de memória durante a inferência. Com este tempo de inferência reduzido, o Falcon-40B é adequado para aplicações de chat.

Alguns exemplos de versões ajustadas do Falcon incluem o [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), um assistente baseado em modelos abertos, e o [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), que oferece desempenho superior ao modelo base.

## Como Escolher

Não há uma resposta única para escolher um modelo aberto. Um bom ponto de partida é usar o recurso de filtro por tarefa do Azure AI Studio. Isso ajudará a entender os tipos de tarefas para os quais o modelo foi treinado. O Hugging Face também mantém um LLM Leaderboard que mostra os modelos com melhor desempenho com base em certas métricas.

Ao comparar LLMs de diferentes tipos, o [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) é outro ótimo recurso:

![Qualidade do Modelo](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.pt.png)  
Fonte: Artificial Analysis

Se estiver a trabalhar num caso de uso específico, procurar versões ajustadas focadas na mesma área pode ser eficaz. Experimentar múltiplos modelos abertos para ver como eles se comportam de acordo com as suas expectativas e as dos seus utilizadores é outra boa prática.

## Próximos Passos

A melhor parte dos modelos abertos é que pode começar a trabalhar com eles rapidamente. Confira o [Catálogo de Modelos do Azure AI Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), que apresenta uma coleção específica do Hugging Face com os modelos discutidos aqui.

## O aprendizado não termina aqui, continue a jornada

Após concluir esta lição, explore a nossa [coleção de aprendizagem sobre IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprofundar os seus conhecimentos sobre IA Generativa!

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante ter em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.