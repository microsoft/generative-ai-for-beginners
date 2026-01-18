<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T17:48:25+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "br"
}
-->
[![Modelos Open Source](../../../../../translated_images/br/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Ajustando Seu LLM

Usar grandes modelos de linguagem para construir aplicações de IA generativa traz novos desafios. Uma questão chave é garantir a qualidade da resposta (precisão e relevância) no conteúdo gerado pelo modelo para uma determinada solicitação do usuário. Em lições anteriores, discutimos técnicas como engenharia de prompts e geração aumentada por recuperação que tentam resolver o problema modificando a entrada do prompt para o modelo existente.

Na lição de hoje, discutimos uma terceira técnica, **ajuste fino (fine-tuning)**, que tenta resolver o desafio ao re-treinar o próprio modelo com dados adicionais. Vamos mergulhar nos detalhes.

## Objetivos de Aprendizagem

Esta lição introduz o conceito de ajuste fino para modelos de linguagem pré-treinados, explora os benefícios e desafios dessa abordagem e fornece orientações sobre quando e como usar ajuste fino para melhorar o desempenho de seus modelos de IA generativa.

Ao final desta lição, você deverá ser capaz de responder às seguintes perguntas:

- O que é ajuste fino para modelos de linguagem?
- Quando, e por que, o ajuste fino é útil?
- Como posso ajustar finamente um modelo pré-treinado?
- Quais são as limitações do ajuste fino?

Pronto? Vamos começar.

## Guia Ilustrado

Quer ter uma visão geral do que vamos cobrir antes de começar? Confira este guia ilustrado que descreve a jornada de aprendizagem para esta lição - desde aprender os conceitos principais e motivação para o ajuste fino, até entender o processo e as melhores práticas para executar a tarefa de ajuste fino. Este é um tópico fascinante para explorar, então não deixe de visitar a página de [Recursos](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) para links adicionais que apoiem sua jornada de aprendizado autodidata!

![Guia Ilustrado para Ajuste Fino de Modelos de Linguagem](../../../../../translated_images/br/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## O que é ajuste fino para modelos de linguagem?

Por definição, grandes modelos de linguagem são _pré-treinados_ em grandes quantidades de texto obtidas de diversas fontes, incluindo a internet. Como aprendemos em lições anteriores, precisamos de técnicas como _engenharia de prompt_ e _geração aumentada por recuperação_ para melhorar a qualidade das respostas do modelo às perguntas do usuário ("prompts").

Uma técnica popular de engenharia de prompt é dar mais orientação ao modelo sobre o que se espera na resposta, seja fornecendo _instruções_ (orientação explícita) ou _dando alguns exemplos_ (orientação implícita). Isso é chamado de _few-shot learning_, mas possui duas limitações:

- Limites de tokens do modelo podem restringir o número de exemplos que você pode fornecer e limitar a eficácia.
- Custos em tokens podem tornar caro adicionar exemplos em todos os prompts, limitando a flexibilidade.

Ajuste fino é uma prática comum em sistemas de aprendizado de máquina onde pegamos um modelo pré-treinado e o re-treinamos com novos dados para melhorar seu desempenho em uma tarefa específica. No contexto dos modelos de linguagem, podemos ajustar finamente o modelo pré-treinado _com um conjunto selecionado de exemplos para uma dada tarefa ou domínio de aplicação_ para criar um **modelo personalizado** que pode ser mais preciso e relevante para essa tarefa ou domínio específico. Um benefício adicional do ajuste fino é que ele pode também reduzir o número de exemplos necessários para few-shot learning - reduzindo o uso de tokens e os custos relacionados.

## Quando e por que devemos ajustar finamente os modelos?

Neste _contexto_, quando falamos de ajuste fino estamos nos referindo ao ajuste fino **supervisionado**, onde o re-treinamento é feito **adicionando novos dados** que não faziam parte do conjunto de dados original de treinamento. Isso é diferente de uma abordagem de ajuste fino não supervisionado, onde o modelo é re-treinado sobre os dados originais, mas com hiperparâmetros diferentes.

O ponto principal é que ajuste fino é uma técnica avançada que requer um certo nível de especialização para alcançar os resultados desejados. Se feito incorretamente, pode não trazer as melhorias esperadas, e pode até degradar o desempenho do modelo para o domínio alvo.

Portanto, antes de aprender "como" ajustar finamente modelos de linguagem, você precisa saber "por que" deve seguir esse caminho, e "quando" iniciar o processo de ajuste fino. Comece fazendo a si mesmo essas perguntas:

- **Caso de Uso**: Qual é o seu _caso de uso_ para ajuste fino? Qual aspecto do modelo pré-treinado atual você deseja melhorar?
- **Alternativas**: Você já tentou _outras técnicas_ para alcançar os resultados desejados? Utilize-as para criar uma base de comparação.
  - Engenharia de prompt: Experimente técnicas como few-shot prompting com exemplos relevantes de respostas. Avalie a qualidade das respostas.
  - Geração Aumentada por Recuperação: Experimente aumentar os prompts com resultados de buscas em seus dados. Avalie a qualidade das respostas.
- **Custos**: Você identificou os custos do ajuste fino?
  - Capacidade de ajuste - o modelo pré-treinado está disponível para ajuste fino?
  - Esforço - para preparação dos dados de treinamento, avaliação e refinamento do modelo.
  - Computação - para rodar os jobs de ajuste fino e implantar o modelo ajustado
  - Dados - acesso a exemplos de qualidade suficientes para impacto do ajuste fino
- **Benefícios**: Você confirmou os benefícios do ajuste fino?
  - Qualidade - o modelo ajustado superou a linha de base?
  - Custo - ele reduz o uso de tokens ao simplificar os prompts?
  - Extensibilidade - você pode reutilizar o modelo base para novos domínios?

Respondendo a essas perguntas, você poderá decidir se o ajuste fino é a abordagem correta para seu caso de uso. Idealmente, a abordagem é válida apenas se os benefícios superarem os custos. Uma vez decidido seguir adiante, é hora de pensar _como_ você pode ajustar finamente o modelo pré-treinado.

Quer mais insights sobre o processo de tomada de decisão? Assista a [Ajustar fino ou não ajustar fino](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Como podemos ajustar finamente um modelo pré-treinado?

Para ajustar finamente um modelo pré-treinado, você precisa ter:

- um modelo pré-treinado para ajuste fino
- um conjunto de dados para usar no ajuste fino
- um ambiente de treinamento para executar o job de ajuste fino
- um ambiente de hospedagem para implantar o modelo ajustado

## Ajuste Fino em Ação

Os recursos a seguir fornecem tutoriais passo a passo para guiá-lo por um exemplo real usando um modelo selecionado com um conjunto de dados curado. Para seguir esses tutoriais, você precisa de uma conta no provedor específico, juntamente com acesso ao modelo relevante e conjuntos de dados.

| Provedor    | Tutorial                                                                                                                                                                        | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI      | [Como ajustar finamente modelos chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)           | Aprenda a ajustar finamente um `gpt-35-turbo` para um domínio específico ("assistente de receita") preparando dados de treinamento, executando o job de ajuste fino e usando o modelo ajustado para inferência.                                                                                                                                                                                                                  |
| Azure OpenAI| [Tutorial de ajuste fino GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst)  | Aprenda a ajustar finamente um modelo `gpt-35-turbo-0613` **no Azure** realizando os passos para criar e fazer upload dos dados de treinamento, executar o job de ajuste fino, implantar e usar o novo modelo.                                                                                                                                                                                                                 |
| Hugging Face| [Ajustando finamente LLMs com Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                         | Este post no blog mostra como ajustar finamente um _LLM aberto_ (ex: `CodeLlama 7B`) usando a biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) e o [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) com conjuntos de [dados abertos](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) no Hugging Face.|
|             |                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 🤗 AutoTrain| [Ajustando finamente LLMs com AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                    | AutoTrain (ou AutoTrain Advanced) é uma biblioteca python desenvolvida pela Hugging Face que permite ajuste fino para muitas tarefas diferentes incluindo ajuste fino de LLMs. AutoTrain é uma solução sem código e o ajuste fino pode ser feito na sua própria nuvem, no Hugging Face Spaces ou localmente. Suporta interface gráfica web, CLI e treinamento via arquivos de configuração yaml.                                                                                       |
|             |                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 🦥 Unsloth  | [Ajustando finamente LLMs com Unsloth](https://github.com/unslothai/unsloth)                                                                                                   | Unsloth é um framework open-source que suporta ajuste fino de LLMs e aprendizado por reforço (RL). Unsloth facilita treinamento local, avaliação e implantação com [notebooks prontos](https://github.com/unslothai/notebooks). Também suporta texto para voz (TTS), BERT e modelos multimodais. Para começar, leia o guia passo a passo [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                        |
|             |                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                               |
## Tarefa

Escolha um dos tutoriais acima e siga-o. _Podemos replicar uma versão desses tutoriais em Jupyter Notebooks neste repositório apenas para referência. Por favor, use as fontes originais diretamente para obter as versões mais recentes_.

## Ótimo Trabalho! Continue Seu Aprendizado.

Após completar esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Parabéns!! Você completou a lição final da série v2 deste curso! Não pare de aprender e construir. \*\*Confira a página de [RECURSOS](RESOURCES.md?WT.mc_id=academic-105485-koreyst) para uma lista de sugestões adicionais só sobre esse tópico.

Nossa série v1 de lições também foi atualizada com mais tarefas e conceitos. Então, reserve um minuto para relembrar seus conhecimentos - e por favor [compartilhe suas dúvidas e feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) para nos ajudar a melhorar essas lições para a comunidade.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->