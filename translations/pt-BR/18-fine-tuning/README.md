[![Modelos de Código Aberto](../../../translated_images/pt-BR/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Ajustando seu LLM

Usar grandes modelos de linguagem para construir aplicações de IA generativa traz novos desafios. Uma questão fundamental é garantir a qualidade das respostas (precisão e relevância) no conteúdo gerado pelo modelo para uma solicitação do usuário. Em lições anteriores, discutimos técnicas como engenharia de prompts e geração aumentada por recuperação que tentam resolver o problema modificando _a entrada do prompt_ para o modelo existente.

Na lição de hoje, discutimos uma terceira técnica, **fine-tuning** (ajuste fino), que tenta resolver o desafio ao _retreinar o próprio modelo_ com dados adicionais. Vamos detalhar.

## Objetivos de Aprendizagem

Esta lição introduz o conceito de ajuste fino para modelos de linguagem pré-treinados, explora os benefícios e desafios dessa abordagem, e fornece orientações sobre quando e como usar o fine-tuning para melhorar o desempenho dos seus modelos de IA generativa.

Ao final desta lição, você deverá ser capaz de responder às seguintes perguntas:

- O que é fine-tuning para modelos de linguagem?
- Quando e por que o fine-tuning é útil?
- Como posso fazer fine-tuning em um modelo pré-treinado?
- Quais são as limitações do fine-tuning?

Pronto? Vamos começar.

## Guia Ilustrado

Quer ter uma visão geral do que vamos cobrir antes de começar? Veja este guia ilustrado que descreve a jornada de aprendizado para esta lição — desde aprender os conceitos básicos e a motivação para o fine-tuning até entender o processo e as melhores práticas para executar esta tarefa. Este é um tema fascinante para exploração, então não esqueça de visitar a página de [Recursos](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) para links adicionais que apoiam sua jornada de aprendizado autodidata!

![Guia Ilustrado para Fine Tuning de Modelos de Linguagem](../../../translated_images/pt-BR/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## O que é fine-tuning para modelos de linguagem?

Por definição, grandes modelos de linguagem são _pré-treinados_ em grandes quantidades de textos oriundos de diversas fontes, incluindo a internet. Como aprendemos em lições anteriores, precisamos de técnicas como _engenharia de prompt_ e _geração aumentada por recuperação_ para melhorar a qualidade das respostas do modelo às perguntas dos usuários ("prompts").

Uma técnica popular de engenharia de prompt envolve dar ao modelo mais orientação sobre o que se espera na resposta, seja fornecendo _instruções_ (orientação explícita) ou _dando-lhe alguns exemplos_ (orientação implícita). Isso é referido como _aprendizado com poucos exemplos_ (few-shot learning), mas possui duas limitações:

- Limites de tokens do modelo podem restringir o número de exemplos que você pode fornecer, limitando a eficácia.
- Custos de tokens do modelo podem tornar caro adicionar exemplos a cada prompt, limitando a flexibilidade.

Fine-tuning é uma prática comum em sistemas de aprendizado de máquina na qual pegamos um modelo pré-treinado e o retreinamos com novos dados para melhorar seu desempenho em uma tarefa específica. No contexto de modelos de linguagem, podemos ajustar o modelo pré-treinado _com um conjunto selecionado de exemplos para uma tarefa ou domínio específico_ para criar um **modelo personalizado** que pode ser mais preciso e relevante para essa tarefa ou domínio. Um benefício adicional do fine-tuning é que ele também pode reduzir o número de exemplos necessários para o few-shot learning, diminuindo o uso de tokens e custos relacionados.

## Quando e por que devemos fazer fine-tuning em modelos?

Neste _contexto_, quando falamos de fine-tuning, nos referimos ao fine-tuning **supervisionado**, onde o retreinamento é feito **adicionando novos dados** que não faziam parte do conjunto de dados original. Isso é diferente de uma abordagem não supervisionada de fine-tuning, onde o modelo é retreinado nos dados originais, mas com hiperparâmetros diferentes.

O ponto principal a lembrar é que o fine-tuning é uma técnica avançada que requer um certo nível de expertise para obter os resultados desejados. Se feito de forma incorreta, pode não proporcionar as melhorias esperadas e até mesmo degradar o desempenho do modelo para seu domínio alvo.

Então, antes de aprender "como" fazer fine-tuning em modelos de linguagem, você precisa saber "por que" deve seguir esse caminho e "quando" iniciar o processo de fine-tuning. Comece fazendo a si mesmo estas perguntas:

- **Caso de Uso**: Qual é seu _caso de uso_ para fine-tuning? Qual aspecto do modelo pré-treinado atual você quer melhorar?
- **Alternativas**: Você já tentou _outras técnicas_ para alcançar os resultados desejados? Use-as para criar uma linha de base para comparação.
  - Engenharia de prompt: Tente técnicas como few-shot prompting com exemplos de respostas relevantes. Avalie a qualidade das respostas.
  - Geração Aumentada por Recuperação: Tente aumentar os prompts com resultados de consultas pesquisadas em seus dados. Avalie a qualidade das respostas.
- **Custos**: Você identificou os custos para fine-tuning?
  - Ajustabilidade – o modelo pré-treinado está disponível para fine-tuning?
  - Esforço – para preparar dados de treinamento, avaliar e refinar o modelo.
  - Computação – para executar trabalhos de fine-tuning e implantar o modelo ajustado.
  - Dados – acesso a exemplos de qualidade suficiente para impacto do fine-tuning.
- **Benefícios**: Você confirmou os benefícios do fine-tuning?
  - Qualidade – o modelo ajustado superou a linha de base?
  - Custo – ele reduz o uso de tokens ao simplificar os prompts?
  - Extensibilidade – você pode reutilizar o modelo base para novos domínios?

Respondendo a essas perguntas, você deve ser capaz de decidir se o fine-tuning é a abordagem certa para seu caso de uso. Idealmente, essa abordagem é válida somente se os benefícios superarem os custos. Uma vez decidido seguir adiante, é hora de pensar _como_ você pode ajustar o modelo pré-treinado.

Quer ter mais insights sobre o processo decisório? Assista [Fazer fine-tuning ou não fazer fine-tuning](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Como podemos fazer fine-tuning em um modelo pré-treinado?

Para fazer fine-tuning em um modelo pré-treinado, você precisa ter:

- um modelo pré-treinado para ajustar
- um conjunto de dados para usar no fine-tuning
- um ambiente de treinamento para executar o trabalho de fine-tuning
- um ambiente de hospedagem para implantar o modelo ajustado

## Fine-Tuning na Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) é onde você faz ajustes finos, implanta e gerencia modelos personalizados no Azure hoje (ele unifica o que antes era Azure OpenAI Studio e Azure AI Studio). Antes de iniciar um trabalho, é útil entender as opções que o Foundry oferece – e as melhores práticas recomendadas pela plataforma. Por trás dos panos, o Foundry usa **LoRA (adaptação de baixa complexidade)** para fazer fine-tuning de forma eficiente, mantendo o treinamento mais rápido e mais barato do que retreinar todos os pesos.

### Passo 1: Escolha uma técnica de treinamento

O Foundry suporta três técnicas de fine-tuning. **Comece com SFT** - ela cobre o maior número de cenários.

| Técnica | O que faz | Quando usar |
| --- | --- | --- |
| **Fine-Tuning Supervisionado (SFT)** | Treina em pares de exemplos de entrada/saída para que o modelo aprenda a produzir as respostas desejadas. | O padrão para a maioria das tarefas: especialização de domínio, desempenho da tarefa, estilo e tom, seguir instruções e adaptação linguística. |
| **Otimização Direta de Preferência (DPO)** | Aprende com pares de respostas preferidas vs. não preferidas para alinhar as saídas com preferências humanas. | Para melhorar qualidade, segurança e alinhamento das respostas quando você tem feedback comparativo. |
| **Fine-Tuning por Reforço (RFT)** | Usa sinais de recompensa de _avaliadores_ para otimizar comportamentos complexos com aprendizado por reforço. | Domínios objetivos e com raciocínios complexos (matemática, química, física) com respostas claras de certo/errado. Requer mais expertise em ML. |

### Passo 2: Escolha um nível de treinamento

O Foundry permite escolher como e onde o treinamento será executado:

- **Standard** – treina na região do seu recurso garantindo residência dos dados. Use quando os dados devem permanecer em uma região específica.
- **Global** – mais barato e mais rápido para enfileirar usando capacidade fora da sua região (dados e pesos são copiados para a região de treinamento). Uma boa opção padrão quando residência de dados não é exigida.
- **Desenvolvedor** – o menor custo, usando capacidade ociosa sem garantias de latência/SLA (jobs podem ser preemptados e retomados). Ideal para experimentação.

### Passo 3: Escolha um modelo base

Modelos ajustáveis incluem OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` e `gpt-4.1-nano` (SFT; as famílias 4o/4.1 também suportam DPO), os modelos de raciocínio `o4-mini` e `gpt-5` (RFT), além de modelos open-source como `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` e `gpt-oss-20b` (SFT em recursos Foundry). Sempre consulte a atual [Lista de modelos para fine-tuning](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) para métodos suportados, regiões e disponibilidade.

> O Foundry oferece duas modalidades: **serverless** (preços baseados em consumo, sem cota de GPU para gerenciar, OpenAI e modelos selecionados) e **computação gerenciada** (traga suas próprias VMs via Azure Machine Learning para a maior variedade de modelos). A maioria das pessoas deve começar com serverless.

### Melhores práticas do Foundry

- **Comece pela linha de base.** Meça o desempenho do modelo base com engenharia de prompt e RAG _antes_ do fine-tuning para comprovar o ganho.
- **Comece pequeno, depois escale.** Inicie com 50-100 exemplos de alta qualidade para validar a abordagem, depois cresça para 500+ para produção. Qualidade é mais importante que quantidade – elimine exemplos de baixa qualidade.
- **Formate os dados corretamente.** Arquivos de treinamento e validação devem ser JSONL, UTF-8 **com BOM**, menores que 512 MB, usando o formato de mensagens de chat completions. Sempre inclua um arquivo de validação para monitorar overfitting.
- **Mantenha o prompt do sistema durante a inferência.** Use a mesma mensagem do sistema ao chamar o modelo que você usou durante o treinamento.
- **Avalie os checkpoints – não lance o último sem análise.** O Foundry mantém os últimos três epochs como checkpoints implantáveis; escolha o que generaliza melhor ao observar `train_loss` / `valid_loss` e acurácia de tokens.
- **Meça custo de tokens junto com a qualidade** ao comparar o modelo ajustado com a linha de base.
- **Itere com fine-tuning contínuo.** Você pode ajustar um modelo já ajustado sobre novos dados (suportado para modelos OpenAI).
- **Atente-se aos custos de hospedagem.** Um modelo personalizado implantado é cobrado por hora, e uma implantação inativa é removida após 15 dias – limpe o que não precisar.

Execute o tutorial completo em [Personalize um modelo com fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), e veja os guias para [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) e [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) quando estiver pronto para as outras técnicas.

## Fine-Tuning na Prática

Os recursos a seguir oferecem tutoriais passo a passo que percorrem um exemplo real em um modelo suportado atualmente com um conjunto de dados selecionado. Para utilizá-los, você precisa de uma conta no provedor específico, além de acesso ao modelo e datasets relevantes.

| Provedor     | Tutorial                                                                                                                                                                       | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Como fazer fine-tuning em modelos de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Aprenda a ajustar um modelo recente de chat da OpenAI para um domínio específico ("assistente de receitas") preparando dados de treinamento, executando o trabalho de fine-tuning e usando o modelo ajustado para inferência.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Personalize um modelo com fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Aprenda a ajustar um modelo atualmente suportado, como `gpt-4.1-mini` **no Azure** com Microsoft Foundry: prepare e envie dados de treinamento e validação, execute o trabalho de fine-tuning, depois implante e use o novo modelo.                                                                                                                                                                                                                                                                 |

| Hugging Face | [Ajuste fino de LLMs com Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Este post no blog guia você pelo ajuste fino de um _LLM aberto_ (ex: `CodeLlama 7B`) usando a biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) com [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) abertos no Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Ajuste fino de LLMs com AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ou AutoTrain Advanced) é uma biblioteca Python desenvolvida pela Hugging Face que permite ajuste fino para muitas tarefas diferentes, incluindo ajuste fino de LLM. AutoTrain é uma solução sem código e o ajuste fino pode ser feito na sua própria nuvem, nos Hugging Face Spaces ou localmente. Suporta tanto GUI baseada na web, CLI e treinamento via arquivos de configuração yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Ajuste fino de LLMs com Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth é uma estrutura open-source que suporta ajuste fino de LLM e aprendizado por reforço (RL). Unsloth simplifica o treinamento local, avaliação e implantação com [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) prontos para uso. Também suporta texto para fala (TTS), BERT e modelos multimodais. Para começar, leia o passo a passo do [Guia para Ajuste Fino de LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tarefa

Selecione um dos tutoriais acima e experimente-o. _Podemos replicar uma versão desses tutoriais em Jupyter Notebooks neste repositório apenas para referência. Por favor, use diretamente as fontes originais para obter as versões mais recentes_.

## Ótimo Trabalho! Continue Seu Aprendizado.

Após completar esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Parabéns!! Você completou a lição final da série v2 deste curso! Não pare de aprender e construir. \*\*Confira a página de [RECURSOS](RESOURCES.md?WT.mc_id=academic-105485-koreyst) para uma lista de sugestões adicionais só para este tópico.

Nossa série de lições v1 também foi atualizada com mais tarefas e conceitos. Então tire um minuto para refrescar seu conhecimento - e por favor [compartilhe suas perguntas e feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) para nos ajudar a melhorar essas lições para a comunidade.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->