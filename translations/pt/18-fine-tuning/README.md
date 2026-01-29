<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T17:45:46+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "pt"
}
-->
[![Open Source Models](../../../../../translated_images/pt-PT/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Ajuste Fino do Seu LLM

Usar grandes modelos de linguagem para construir aplicações de IA generativa traz novos desafios. Uma questão chave é garantir a qualidade da resposta (exatidão e relevância) no conteúdo gerado pelo modelo para um dado pedido do utilizador. Nas lições anteriores, discutimos técnicas como engenharia de prompts e geração aumentada por recuperação que tentam resolver o problema ao _modificar a entrada do prompt_ para o modelo existente.

Na lição de hoje, discutimos uma terceira técnica, o **ajuste fino**, que tenta abordar o desafio _re-treinando o próprio modelo_ com dados adicionais. Vamos entrar em detalhes.

## Objetivos de Aprendizagem

Esta lição introduz o conceito de ajuste fino para modelos de linguagem pré-treinados, explora os benefícios e desafios desta abordagem, e fornece orientações sobre quando e como usar o ajuste fino para melhorar o desempenho dos seus modelos de IA generativa.

No final desta lição, deverá ser capaz de responder às seguintes perguntas:

- O que é ajuste fino para modelos de linguagem?
- Quando, e porquê, o ajuste fino é útil?
- Como posso ajustar um modelo pré-treinado?
- Quais são as limitações do ajuste fino?

Pronto? Vamos começar.

## Guia Ilustrado

Quer ter uma visão geral do que vamos cobrir antes de começarmos? Veja este guia ilustrado que descreve a jornada de aprendizagem para esta lição - desde aprender os conceitos essenciais e a motivação para o ajuste fino, até entender o processo e as melhores práticas para executar a tarefa de ajuste fino. Este é um tópico fascinante para exploração, por isso não se esqueça de consultar a página de [Recursos](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) para links adicionais que apoiem a sua aprendizagem autónoma!

![Illustrated Guide to Fine Tuning Language Models](../../../../../translated_images/pt-PT/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## O que é ajuste fino para modelos de linguagem?

Por definição, grandes modelos de linguagem são _pré-treinados_ com grandes quantidades de texto provenientes de fontes diversas, incluindo a internet. Como aprendemos nas lições anteriores, precisamos de técnicas como _engenharia de prompts_ e _geração aumentada por recuperação_ para melhorar a qualidade das respostas do modelo às perguntas do utilizador ("prompts").

Uma técnica popular de engenharia de prompts envolve dar ao modelo mais orientação sobre o que é esperado na resposta, seja fornecendo _instruções_ (orientação explícita) ou _dando-lhe alguns exemplos_ (orientação implícita). Isto é referido como _few-shot learning_ mas tem duas limitações:

- Os limites de tokens do modelo podem restringir o número de exemplos que pode dar, limitando a eficácia.
- Os custos de tokens do modelo podem tornar caro adicionar exemplos a cada prompt, limitando a flexibilidade.

O ajuste fino é uma prática comum em sistemas de aprendizagem automática onde pegamos num modelo pré-treinado e re-treinamo-lo com novos dados para melhorar o seu desempenho numa tarefa específica. No contexto dos modelos de linguagem, podemos ajustar o modelo pré-treinado _com um conjunto selecionado de exemplos para uma dada tarefa ou domínio de aplicação_ para criar um **modelo personalizado** que pode ser mais preciso e relevante para essa tarefa ou domínio específico. Um benefício adicional do ajuste fino é que pode também reduzir o número de exemplos necessários para few-shot learning - reduzindo o uso de tokens e custos relacionados.

## Quando e porquê devemos ajustar os modelos?

Neste _contexto_, quando falamos de ajuste fino, referimo-nos ao ajuste fino **supervisionado** onde o re-treinamento é feito por **adicionar novos dados** que não faziam parte do conjunto de dados original de treino. Isto é diferente de uma abordagem não supervisionada de ajuste fino, onde o modelo é re-treinado nos dados originais, mas com hiperparâmetros diferentes.

A coisa importante a lembrar é que o ajuste fino é uma técnica avançada que requer um certo nível de especialização para obter os resultados desejados. Se feito incorretamente, pode não fornecer as melhorias esperadas, e até deteriorar o desempenho do modelo para o seu domínio alvo.

Por isso, antes de aprender "como" ajustar modelos de linguagem, precisa de saber "porquê" deve tomar este caminho, e "quando" iniciar o processo de ajuste fino. Comece por fazer a si mesmo estas perguntas:

- **Caso de Uso**: Qual é o seu _caso de uso_ para o ajuste fino? Que aspeto do modelo pré-treinado atual quer melhorar?
- **Alternativas**: Já experimentou _outras técnicas_ para alcançar os resultados desejados? Use-as para criar uma linha base de comparação.
  - Engenharia de prompts: Experimente técnicas como few-shot prompting com exemplos de respostas relevantes. Avalie a qualidade das respostas.
  - Geração Aumentada por Recuperação: Experimente aumentar os prompts com resultados de pesquisa do seu dado. Avalie a qualidade das respostas.
- **Custos**: Identificou os custos do ajuste fino?
  - Possibilidade de ajuste - o modelo pré-treinado está disponível para ajuste fino?
  - Esforço - para preparar dados de treino, avaliar e refinar o modelo.
  - Computação - para executar trabalhos de ajuste fino e implementar o modelo ajustado.
  - Dados - acesso a exemplos de qualidade suficiente para impacto do ajuste fino.
- **Benefícios**: Confirmou os benefícios do ajuste fino?
  - Qualidade - o modelo ajustado teve um desempenho superior à linha base?
  - Custo - reduz o uso de tokens simplificando os prompts?
  - Extensibilidade - pode reutilizar o modelo base para novos domínios?

Respondendo a estas perguntas, deverá ser capaz de decidir se o ajuste fino é a abordagem certa para o seu caso de uso. Idealmente, a abordagem é válida apenas se os benefícios superarem os custos. Depois de decidir avançar, é tempo de pensar _como_ pode ajustar o modelo pré-treinado.

Quer obter mais insights no processo de decisão? Veja [Ajustar ou não ajustar](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Como podemos ajustar um modelo pré-treinado?

Para ajustar um modelo pré-treinado, precisa de ter:

- um modelo pré-treinado para ajustar
- um conjunto de dados para usar no ajuste fino
- um ambiente de treino para executar a tarefa de ajuste fino
- um ambiente de implementação para alojar o modelo ajustado

## Ajuste Fino em Ação

Os recursos seguintes fornecem tutoriais passo a passo para o guiar por um exemplo real usando um modelo selecionado com um conjunto de dados selecionado. Para trabalhar estes tutoriais, precisa de uma conta no fornecedor específico, juntamente com acesso ao modelo e conjuntos de dados relevantes.

| Fornecedor   | Tutorial                                                                                                                                                                       | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Como ajustar modelos de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Aprenda a ajustar um `gpt-35-turbo` para um domínio específico ("assistente de receitas") preparando os dados de treino, executando o trabalho de ajuste fino, e usando o modelo ajustado para inferência.                                                                                                                                                                                                                          |
| Azure OpenAI | [Tutorial de ajuste fino GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Aprenda a ajustar um modelo `gpt-35-turbo-0613` **na Azure** seguindo os passos para criar e carregar os dados de treino, executar o trabalho de ajuste fino. Implementar e usar o novo modelo.                                                                                                                                                                                                                                      |
| Hugging Face | [Ajuste fino de LLMs com Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Este artigo guia o ajuste fino de um _LLM aberto_ (ex: `CodeLlama 7B`) usando a biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & o [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) com [conjuntos de dados](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) abertos no Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Ajuste fino de LLMs com AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ou AutoTrain Advanced) é uma biblioteca python desenvolvida pela Hugging Face que permite ajuste fino para muitas tarefas diferentes incluindo ajuste fino de LLMs. AutoTrain é uma solução sem código e o ajuste fino pode ser feito na sua própria cloud, no Hugging Face Spaces ou localmente. Suporta GUI web, CLI e treino via ficheiros de configuração yaml.                                                                |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Ajuste fino de LLMs com Unsloth](https://github.com/unslothai/unsloth)                                                         | Unsloth é um framework open-source que suporta ajuste fino de LLM e aprendizagem por reforço (RL). Unsloth simplifica treino local, avaliação, e implementação com [notebooks](https://github.com/unslothai/notebooks) prontos a usar. Suporta também text-to-speech (TTS), modelos BERT e multimodais. Para começar, leia o seu guia passo a passo [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                              |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tarefa

Selecione um dos tutoriais acima e siga-o passo a passo. _Podemos replicar uma versão destes tutoriais em Jupyter Notebooks neste repositório apenas para referência. Por favor, use as fontes originais diretamente para obter as versões mais recentes_.

## Excelente Trabalho! Continue a Sua Aprendizagem.

Depois de completar esta lição, confira a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a evoluir o seu conhecimento em IA Generativa!

Parabéns!! Concluiu a última lição da série v2 deste curso! Não pare de aprender e construir. \*\*Consulte a página [RECURSOS](RESOURCES.md?WT.mc_id=academic-105485-koreyst) para uma lista de sugestões adicionais sobre este tema.

A nossa série v1 de lições também foi atualizada com mais tarefas e conceitos. Reserve um minuto para refrescar o seu conhecimento - e por favor [partilhe as suas questões e feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) para nos ajudar a melhorar estas lições para a comunidade.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Apesar dos nossos esforços para garantir a precisão, por favor, tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->