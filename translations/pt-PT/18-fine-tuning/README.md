[![Modelos Open Source](../../../translated_images/pt-PT/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Ajustar Fintamente o Seu LLM

Utilizar grandes modelos de linguagem para construir aplicações de IA generativa traz novos desafios. Uma questão chave é garantir a qualidade da resposta (exatidão e relevância) no conteúdo gerado pelo modelo para um dado pedido do utilizador. Em lições anteriores, discutimos técnicas como engenharia de prompts e geração aumentada por recuperação, que tentam resolver o problema ao _modificar a entrada do prompt_ para o modelo existente.

Na lição de hoje, discutimos uma terceira técnica, o **ajuste fino (fine-tuning)**, que tenta abordar o desafio ao _retreinar o próprio modelo_ com dados adicionais. Vamos mergulhar nos detalhes.

## Objetivos de Aprendizagem

Esta lição introduz o conceito de ajuste fino para modelos de linguagem pré-treinados, explora os benefícios e desafios desta abordagem, e fornece orientações sobre quando e como usar o ajuste fino para melhorar o desempenho dos seus modelos de IA generativa.

Ao final desta lição, deverá ser capaz de responder às seguintes perguntas:

- O que é ajuste fino para modelos de linguagem?
- Quando, e porquê, o ajuste fino é útil?
- Como posso ajustar finamente um modelo pré-treinado?
- Quais são as limitações do ajuste fino?

Pronto? Vamos começar.

## Guia Ilustrado

Quer obter uma visão geral do que vamos cobrir antes de começar? Consulte este guia ilustrado que descreve a jornada de aprendizagem para esta lição — desde aprender os conceitos centrais e a motivação para o ajuste fino, até compreender o processo e as melhores práticas para executar a tarefa de ajuste fino. Este é um tema fascinante para explorar, por isso não se esqueça de consultar a página [Recursos](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) para links adicionais que apoiem a sua aprendizagem autónoma!

![Guia Ilustrado para Ajuste Fino de Modelos de Linguagem](../../../translated_images/pt-PT/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## O que é ajuste fino para modelos de linguagem?

Por definição, grandes modelos de linguagem são _pré-treinados_ em grandes quantidades de texto provenientes de fontes diversas, incluindo a internet. Como aprendemos em lições anteriores, precisamos de técnicas como _engenharia de prompts_ e _geração aumentada por recuperação_ para melhorar a qualidade das respostas do modelo às perguntas do utilizador ("prompts").

Uma técnica popular de engenharia de prompts envolve dar ao modelo mais orientação sobre o que se espera na resposta, seja fornecendo _instruções_ (orientação explícita) ou _dando-lhe alguns exemplos_ (orientação implícita). Isto é referido como _aprendizagem com poucos exemplos (few-shot learning)_, mas tem duas limitações:

- Limites de tokens do modelo podem restringir o número de exemplos que pode fornecer e limitar a eficácia.
- Custos por token do modelo podem tornar caro adicionar exemplos a cada prompt e limitar a flexibilidade.

O ajuste fino é uma prática comum em sistemas de machine learning onde pegamos num modelo pré-treinado e o retreinamos com novos dados para melhorar o seu desempenho numa tarefa específica. No contexto dos modelos de linguagem, podemos ajustar finamente o modelo pré-treinado _com um conjunto selecionado de exemplos para uma dada tarefa ou domínio de aplicação_ para criar um **modelo personalizado** que pode ser mais exato e relevante para essa tarefa ou domínio específico. Um benefício secundário do ajuste fino é que também pode reduzir o número de exemplos necessários para o few-shot learning — reduzindo o uso de tokens e custos relacionados.

## Quando e porquê devemos ajustar finamente modelos?

Neste _contexto_, quando falamos em ajuste fino, estamos a referir-nos ao ajuste fino **supervisionado**, onde o retreinamento é feito por **adicionar novos dados** que não faziam parte do conjunto de dados original. Isto é diferente da abordagem de ajuste fino não supervisionado onde o modelo é retreinado com os dados originais, mas com hiperparâmetros diferentes.

O ponto principal a lembrar é que o ajuste fino é uma técnica avançada que requer um certo nível de especialização para obter os resultados desejados. Se feito incorretamente, pode não proporcionar as melhorias esperadas, e até pode degradar o desempenho do modelo para o seu domínio alvo.

Então, antes de aprender "como" ajustar finamente modelos de linguagem, precisa de saber "porquê" deve seguir este caminho, e "quando" iniciar o processo de ajuste fino. Comece por se perguntar estas perguntas:

- **Caso de Uso**: Qual é o seu _caso de uso_ para ajuste fino? Que aspeto do modelo pré-treinado atual quer melhorar?
- **Alternativas**: Já tentou _outras técnicas_ para atingir os resultados desejados? Use-as para criar uma base de comparação.
  - Engenharia de Prompt: Tente técnicas como few-shot prompting com exemplos de respostas relevantes. Avalie a qualidade das respostas.
  - Geração Aumentada por Recuperação: Tente aumentar os prompts com resultados de consultas obtidas pela pesquisa dos seus dados. Avalie a qualidade das respostas.
- **Custos**: Já identificou os custos do ajuste fino?
  - Tunabilidade - o modelo pré-treinado está disponível para ajuste fino?
  - Esforço - para preparar dados de treino, avaliar e refinar o modelo.
  - Computação - para correr trabalhos de ajuste fino e implementar o modelo ajustado.
  - Dados - acesso a exemplos de qualidade suficiente para impacto do ajuste fino.
- **Benefícios**: Já confirmou os benefícios do ajuste fino?
  - Qualidade - o modelo ajustado teve desempenho melhor que a linha de base?
  - Custo - reduz o uso de tokens ao simplificar os prompts?
  - Extensibilidade - pode reutilizar o modelo base para novos domínios?

Ao responder a estas perguntas, deverá ser capaz de decidir se o ajuste fino é a abordagem correta para o seu caso de uso. Idealmente, a abordagem é válida somente se os benefícios superarem os custos. Depois de decidir avançar, é hora de pensar _como_ pode ajustar finamente o modelo pré-treinado.

Quer obter mais insights sobre o processo de decisão? Veja [Ajustar finamente ou não ajustar finamente](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Como podemos ajustar finamente um modelo pré-treinado?

Para ajustar finamente um modelo pré-treinado, precisa de:

- um modelo pré-treinado para ajustar
- um conjunto de dados para usar no ajuste fino
- um ambiente de treino para executar o trabalho de ajuste fino
- um ambiente de hospedagem para implementar o modelo ajustado

## Ajuste Fino na Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) é onde ajusta finamente, implementa e gere modelos personalizados na Azure hoje (reúne o que antes era Azure OpenAI Studio e Azure AI Studio). Antes de iniciar um trabalho, é útil compreender as escolhas que a Foundry lhe oferece — e as melhores práticas recomendadas pela plataforma. Por trás das cortinas, a Foundry usa **LoRA (low-rank adaptation)** para ajustar modelos eficientemente, o que mantém o treino mais rápido e mais acessível que retreinar cada peso.

### Passo 1: Escolher uma técnica de treino

A Foundry suporta três técnicas de ajuste fino. **Comece com SFT** — cobre a maior variedade de cenários.

| Técnica | O que faz | Quando usar |
| --- | --- | --- |
| **Ajuste Fino Supervisionado (SFT)** | Treina em pares exemplo de entrada/saída para que o modelo aprenda a produzir as respostas que deseja. | O padrão para a maioria das tarefas: especialização de domínio, desempenho em tarefas, estilo e tom, seguir instruções, e adaptação linguística. |
| **Otimização Direta por Preferência (DPO)** | Aprende a partir de pares de resposta _preferida vs. não preferida_ para alinhar saídas com preferências humanas. | Melhorar a qualidade da resposta, segurança e alinhamento quando tem feedback comparativo. |
| **Ajuste Fino por Reforço (RFT)** | Usa sinais de recompensa de _avaliadores_ para otimizar comportamentos complexos com aprendizagem por reforço. | Domínios objetivos e de raciocínio pesado (matemática, química, física) com respostas claras certas/erradas. Requer mais especialização em ML. |

### Passo 2: Escolher um nível de treino

A Foundry deixa-o escolher como e onde o treino corre:

- **Standard** - treina na região do seu recurso e garante residência dos dados. Use quando os dados devem permanecer numa região específica.
- **Global** - mais barato e rápido na fila ao usar capacidade para além da sua região (dados e pesos são copiados para a região de treino). Boa opção padrão quando residência de dados não é um requisito.
- **Developer** - o custo mais baixo, usando capacidade livre sem garantias de latência/SLA (os trabalhos podem ser preteridos e retomados). Ideal para experimentação.

### Passo 3: Escolher um modelo base

Modelos ajustáveis incluem OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` e `gpt-4.1-nano` (SFT; a família 4o/4.1 também suporta DPO), os modelos de raciocínio `o4-mini` e `gpt-5` (RFT), além de modelos open-source como `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct`, e `gpt-oss-20b` (SFT em recursos Foundry). Consulte sempre a atual [Lista de modelos para ajuste fino](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) para métodos suportados, regiões e disponibilidade.

> A Foundry oferece duas modalidades: **serverless** (preços baseados no consumo, sem quota GPU para gerir, OpenAI e modelos selecionados) e **computação gerida** (traga suas próprias VMs via Azure Machine Learning para a maior variedade de modelos). A maioria das pessoas deve começar pelo serverless.

### Melhores práticas da Foundry

- **Primeiro a linha de base.** Meça o modelo base com engenharia de prompt e RAG _antes_ de ajustar finamente, para provar a melhoria.
- **Comece pequeno, depois escale.** Comece com 50-100 exemplos de alta qualidade para validar a abordagem, depois aumente para 500+ para produção. Qualidade vence quantidade — elimine exemplos de baixa qualidade.
- **Formate os dados corretamente.** Os ficheiros de treino e validação devem ser JSONL, UTF-8 **com BOM**, abaixo de 512 MB, usando o formato de mensagem chat-completions. Inclua sempre um ficheiro de validação para monitorizar o sobreajuste.
- **Mantenha o prompt de sistema no treino durante a inferência.** Use a mesma mensagem de sistema quando chamar o modelo que usou no treino.
- **Avalie checkpoints — não implemente cegamente o último.** A Foundry guarda os últimos três epochs como checkpoints implementáveis; escolha aquele que generaliza melhor observando `train_loss` / `valid_loss` e acurácia de token.
- **Meça custo em tokens juntamente com qualidade** ao comparar o modelo ajustado com a linha de base.
- **Itere com ajuste fino contínuo.** Pode ajustar finamente um modelo já ajustado em novos dados (suportado para modelos OpenAI).
- **Tenha atenção aos custos de hospedagem.** Um modelo personalizado implementado cobra por hora, e uma implementação inativa é removida após 15 dias — limpe o que não precisa.

Percorra o tutorial completo em [Personalizar um modelo com ajuste fino](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), e veja os guias para [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) e [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) quando estiver pronto para as outras técnicas.

## Ajuste Fino em Ação

Os seguintes recursos fornecem tutoriais passo-a-passo que o guiam através de um exemplo real num modelo atualmente suportado com um conjunto de dados selecionado. Para os seguir, precisa de uma conta no fornecedor específico, junto com acesso ao modelo e conjuntos de dados relevantes.

| Fornecedor     | Tutorial                                                                                                                                                                       | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Como ajustar finamente modelos de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Aprenda a ajustar finamente um modelo de chat recente da OpenAI para um domínio específico ("assistente de receitas") preparando dados de treino, executando o trabalho de ajuste fino e usando o modelo ajustado para inferência.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Personalizar um modelo com ajuste fino](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Aprenda a ajustar finamente um modelo atualmente suportado como `gpt-4.1-mini` **na Azure** com a Microsoft Foundry: prepare e carregue dados de treino e validação, execute o trabalho de ajuste fino, depois implemente e use o novo modelo.                                                                                                                                                                                                                                                                 |

| Hugging Face | [Ajuste fino de LLMs com Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Esta publicação do blog guia-te no ajuste fino de um _LLM aberto_ (ex: `CodeLlama 7B`) utilizando a biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) e o [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) com [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) abertos na Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Ajuste fino de LLMs com AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ou AutoTrain Advanced) é uma biblioteca python desenvolvida pela Hugging Face que permite o ajuste fino para muitas tarefas diferentes incluindo ajuste fino de LLM. O AutoTrain é uma solução sem código e o ajuste fino pode ser feito na tua própria cloud, nos Hugging Face Spaces ou localmente. Suporta uma GUI baseada na web, CLI e também treino via ficheiros de configuração yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Ajuste fino de LLMs com Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | O Unsloth é um framework open-source que suporta ajuste fino de LLM e aprendizagem por reforço (RL). O Unsloth simplifica o treino local, avaliação e deployment com [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) prontos a usar. Suporta também modelos de texto para fala (TTS), BERT e modelos multimodais. Para começar, lê o seu guia passo a passo de [Ajuste fino de LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tarefa

Seleciona um dos tutoriais acima e segue-o. _Podemos replicar uma versão destes tutoriais em Jupyter Notebooks neste repositório apenas para referência. Por favor, usa as fontes originais diretamente para obter as versões mais recentes_.

## Excelente Trabalho! Continua a Aprender.

Depois de completares esta lição, consulta a nossa [coleção de Aprendizagem sobre IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuares a aumentar os teus conhecimentos em IA Generativa!

Parabéns!! Concluíste a última lição da série v2 deste curso! Não pares de aprender e construir. \*\*Consulta a página [RECURSOS](RESOURCES.md?WT.mc_id=academic-105485-koreyst) para uma lista de sugestões adicionais exclusivamente sobre este tema.

A nossa série de lições v1 também foi atualizada com mais tarefas e conceitos. Por isso, dedica um minuto para refrescar os teus conhecimentos – e por favor [partilha as tuas perguntas e feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) para nos ajudar a melhorar estas lições para toda a comunidade.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->