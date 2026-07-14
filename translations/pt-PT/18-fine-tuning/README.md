[![Modelos Open Source](../../../translated_images/pt-PT/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Afinar o Seu LLM

Utilizar grandes modelos de linguagem para construir aplicações de IA generativa traz novos desafios. Uma questão fundamental é garantir a qualidade da resposta (exatidão e relevância) no conteúdo gerado pelo modelo para um determinado pedido do utilizador. Nas lições anteriores, discutimos técnicas como engenharia de prompts e geração aumentada por recuperação que tentam resolver o problema _modificando a entrada do prompt_ para o modelo existente.

Na lição de hoje, discutimos uma terceira técnica, o **ajuste fino**, que tenta resolver o desafio _re-treinando o próprio modelo_ com dados adicionais. Vamos explorar os detalhes.

## Objetivos de Aprendizagem

Esta lição apresenta o conceito de ajuste fino para modelos de linguagem pré-treinados, explora os benefícios e desafios desta abordagem, e fornece orientações sobre quando e como usar o ajuste fino para melhorar o desempenho dos seus modelos de IA generativa.

No final desta lição, deverá ser capaz de responder às seguintes questões:

- O que é o ajuste fino para modelos de linguagem?
- Quando e por que é útil o ajuste fino?
- Como posso afinar um modelo pré-treinado?
- Quais são as limitações do ajuste fino?

Pronto? Vamos começar.

## Guia Ilustrado

Quer ter uma visão geral do que vamos abordar antes de começar? Confira este guia ilustrado que descreve a jornada de aprendizagem desta lição - desde aprender os conceitos básicos e a motivação para o ajuste fino, até entender o processo e as melhores práticas para executar a tarefa de ajuste fino. Este é um tópico fascinante para explorar, por isso não se esqueça de consultar a página de [Recursos](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) para links adicionais que apoiem a sua aprendizagem autoguiada!

![Guia Ilustrado para Afinar Modelos de Linguagem](../../../translated_images/pt-PT/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## O que é o ajuste fino para modelos de linguagem?

Por definição, grandes modelos de linguagem são _pré-treinados_ em grandes quantidades de texto provenientes de diversas fontes, incluindo a internet. Como aprendemos nas lições anteriores, precisamos de técnicas como _engenharia de prompts_ e _geração aumentada por recuperação_ para melhorar a qualidade das respostas do modelo às perguntas do utilizador ("prompts").

Uma técnica popular de engenharia de prompts envolve dar ao modelo mais orientação sobre o que se espera na resposta, quer fornecendo _instruções_ (orientação explícita) ou _dando-lhe alguns exemplos_ (orientação implícita). Isto é referido como _few-shot learning_, mas tem duas limitações:

- Limites de tokens do modelo podem restringir o número de exemplos que pode fornecer, limitando a eficácia.
- Custos de tokens do modelo podem tornar caro adicionar exemplos a cada prompt, limitando a flexibilidade.

O ajuste fino é uma prática comum em sistemas de aprendizagem automática onde pegamos num modelo pré-treinado e o retreinamos com novos dados para melhorar o seu desempenho numa tarefa específica. No contexto dos modelos de linguagem, podemos afinar o modelo pré-treinado _com um conjunto selecionado de exemplos para uma dada tarefa ou domínio de aplicação_ para criar um **modelo personalizado** que pode ser mais preciso e relevante para essa tarefa ou domínio específico. Um benefício adicional do ajuste fino é que pode também reduzir o número de exemplos necessários para few-shot learning - reduzindo o uso de tokens e os custos relacionados.

## Quando e por que devemos afinar modelos?

Neste _contexto_, quando falamos de ajuste fino, referimo-nos ao ajuste fino **supervisionado**, onde o re-treinamento é feito adicionando novos dados que não faziam parte do conjunto de treino original. Isto é diferente de uma abordagem de ajuste fino não supervisionado, onde o modelo é retreinado nos dados originais, mas com diferentes hiperparâmetros.

A coisa essencial a lembrar é que o ajuste fino é uma técnica avançada que requer um certo nível de especialização para obter os resultados desejados. Se for feito incorretamente, pode não fornecer as melhorias esperadas, e pode até degradar o desempenho do modelo para o domínio alvo.

Por isso, antes de aprender "como" afinar modelos de linguagem, precisa de saber "porquê" deve seguir este caminho, e "quando" iniciar o processo de ajuste fino. Comece por fazer a si mesmo estas perguntas:

- **Caso de Uso**: Qual é o seu _caso de uso_ para ajuste fino? Que aspeto do modelo pré-treinado atual quer melhorar?
- **Alternativas**: Já experimentou _outras técnicas_ para alcançar os resultados desejados? Use-as para criar uma linha base para comparação.
  - Engenharia de prompts: Experimente técnicas como few-shot prompting com exemplos de respostas relevantes. Avalie a qualidade das respostas.
  - Geração Aumentada por Recuperação: Experimente aumentar os prompts com resultados de consultas obtidos pela pesquisa nos seus dados. Avalie a qualidade das respostas.
- **Custos**: Já identificou os custos para o ajuste fino?
  - Capacidade de ajuste - o modelo pré-treinado está disponível para ajuste fino?
  - Esforço - para preparar os dados de treino, avaliar e refinar o modelo.
  - Computação - para executar os trabalhos de ajuste fino, e para implementar o modelo ajustado
  - Dados - acesso a exemplos de qualidade suficiente para impacto do ajuste fino
- **Benefícios**: Já confirmou os benefícios do ajuste fino?
  - Qualidade - o modelo ajustado superou a linha base?
  - Custo - reduz o uso de tokens simplificando os prompts?
  - Extensibilidade - pode reaproveitar o modelo base para novos domínios?

Respondendo a estas questões, deverá ser capaz de decidir se o ajuste fino é a abordagem correta para o seu caso de uso. Idealmente, a abordagem é válida apenas se os benefícios superarem os custos. Uma vez decidido avançar, é hora de pensar em _como_ pode afinar o modelo pré-treinado.

Quer obter mais insights sobre o processo de tomada de decisão? Veja [Afinar ou não afinar](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Como podemos afinar um modelo pré-treinado?

Para afinar um modelo pré-treinado, precisa de ter:

- um modelo pré-treinado para afinar
- um conjunto de dados para usar no ajuste fino
- um ambiente de treino para executar o trabalho de ajuste fino
- um ambiente de hospedagem para implementar o modelo afinado

## Ajuste Fino em Ação

> **Nota:** `gpt-35-turbo` / `gpt-3.5-turbo`, referenciados em alguns dos tutoriais abaixo, foram descontinuados tanto para inferência como para ajuste fino. Se está a começar um novo trabalho de ajuste fino hoje, direcione para um modelo atualmente suportado – por exemplo `gpt-4o-mini` ou `gpt-4.1-mini`. Veja a [lista de modelos para ajuste fino](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) para o conjunto atual de modelos afináveis. Os conceitos e passos nestes tutoriais continuam a ser aplicáveis.

Os recursos seguintes fornecem tutoriais passo a passo para lhe ensinar com um exemplo real utilizando um modelo selecionado com um conjunto de dados selecionado. Para seguir estes tutoriais, precisa de ter uma conta no fornecedor específico, junto com acesso ao modelo e conjuntos de dados relevantes.

| Fornecedor  | Tutorial                                                                                                                                                                   | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI      | [Como afinar modelos de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)              | Aprenda a afinar um `gpt-35-turbo` para um domínio específico ("assistente de receitas") preparando os dados de treino, executando o trabalho de ajuste fino, e usando o modelo afinado para inferência.                                                                                                                                                                                                                                |
| Azure OpenAI| [Tutorial de ajuste fino GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Aprenda a afinar um modelo `gpt-35-turbo-0613` **na Azure** seguindo os passos para criar e carregar os dados de treino, executar o trabalho de ajuste fino, implementar e usar o novo modelo.                                                                                                                                                                                                                                         |
| Hugging Face| [Afinar LLMs com Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Esta publicação de blog explica como afinar um _LLM aberto_ (ex: `CodeLlama 7B`) usando a biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) com [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) abertos na Hugging Face.                   |
|             |                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Afinar LLMs com AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ou AutoTrain Advanced) é uma biblioteca python desenvolvida pela Hugging Face que permite ajuste fino para muitas tarefas diferentes incluindo ajuste fino de LLMs. AutoTrain é uma solução sem código e o ajuste fino pode ser feito no seu próprio ambiente cloud, nos Hugging Face Spaces ou localmente. Suporta GUI web, CLI e treino via ficheiros de configuração yaml.                                                                               |
|             |                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth  | [Afinar LLMs com Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                                        | Unsloth é um framework open-source que suporta ajuste fino de LLM e aprendizagem por reforço (RL). Unsloth simplifica treino local, avaliação e implementação com [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) prontos a usar. Suporta também modelos TTS, BERT e multimodais. Para começar, leia o seu guia passo a passo [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                          |
|             |                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tarefa

Selecione um dos tutoriais acima e faça-o passo a passo. _Podemos replicar uma versão destes tutoriais em Jupyter Notebooks neste repositório apenas para referência. Por favor, use as fontes originais diretamente para obter as versões mais recentes_.

## Excelente Trabalho! Continue a Sua Aprendizagem.

Depois de completar esta lição, confira a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprofundar o seu conhecimento em IA Generativa!

Parabéns!! Concluiu a última lição da série v2 deste curso! Não pare de aprender e construir. \*\*Consulte a página de [RECURSOS](RESOURCES.md?WT.mc_id=academic-105485-koreyst) para uma lista de sugestões adicionais só para este tópico.

A nossa série v1 de lições também foi atualizada com mais tarefas e conceitos. Por isso, reserve um minuto para rever os seus conhecimentos - e por favor [partilhe as suas questões e feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) para nos ajudar a melhorar estas lições para a comunidade.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->