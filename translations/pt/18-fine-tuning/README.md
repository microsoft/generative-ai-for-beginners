<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-18T00:41:54+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "pt"
}
-->
[![Modelos Open Source](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.pt.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Ajuste Fino do Seu LLM

Utilizar modelos de linguagem de grande escala para construir aplicações de IA generativa traz novos desafios. Um dos principais problemas é garantir a qualidade das respostas (precisão e relevância) no conteúdo gerado pelo modelo para uma solicitação específica do utilizador. Nas lições anteriores, discutimos técnicas como engenharia de prompts e geração aumentada por recuperação, que tentam resolver o problema _modificando a entrada do prompt_ para o modelo existente.

Na lição de hoje, discutimos uma terceira técnica, **ajuste fino**, que tenta abordar o desafio _re-treinando o próprio modelo_ com dados adicionais. Vamos explorar os detalhes.

## Objetivos de Aprendizagem

Esta lição introduz o conceito de ajuste fino para modelos de linguagem pré-treinados, explora os benefícios e desafios dessa abordagem e fornece orientações sobre quando e como usar o ajuste fino para melhorar o desempenho dos seus modelos de IA generativa.

Ao final desta lição, deverá ser capaz de responder às seguintes perguntas:

- O que é ajuste fino para modelos de linguagem?
- Quando e por que o ajuste fino é útil?
- Como posso ajustar um modelo pré-treinado?
- Quais são as limitações do ajuste fino?

Pronto? Vamos começar.

## Guia Ilustrado

Quer ter uma visão geral do que vamos abordar antes de mergulhar nos detalhes? Confira este guia ilustrado que descreve a jornada de aprendizagem desta lição - desde os conceitos principais e a motivação para o ajuste fino, até entender o processo e as melhores práticas para executar a tarefa de ajuste fino. Este é um tópico fascinante para explorar, então não se esqueça de conferir a página de [Recursos](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) para links adicionais que apoiarão a sua jornada de aprendizagem autônoma!

![Guia Ilustrado para Ajuste Fino de Modelos de Linguagem](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.pt.png)

## O que é ajuste fino para modelos de linguagem?

Por definição, os modelos de linguagem de grande escala são _pré-treinados_ em grandes quantidades de texto provenientes de diversas fontes, incluindo a internet. Como aprendemos em lições anteriores, precisamos de técnicas como _engenharia de prompts_ e _geração aumentada por recuperação_ para melhorar a qualidade das respostas do modelo às perguntas dos utilizadores ("prompts").

Uma técnica popular de engenharia de prompts envolve dar ao modelo mais orientação sobre o que é esperado na resposta, seja fornecendo _instruções_ (orientação explícita) ou _dando alguns exemplos_ (orientação implícita). Isso é chamado de _aprendizagem com poucos exemplos_ (few-shot learning), mas tem duas limitações:

- Os limites de tokens do modelo podem restringir o número de exemplos que pode fornecer e limitar a eficácia.
- Os custos de tokens do modelo podem tornar caro adicionar exemplos a cada prompt e limitar a flexibilidade.

O ajuste fino é uma prática comum em sistemas de aprendizagem automática, onde pegamos um modelo pré-treinado e o re-treinamos com novos dados para melhorar seu desempenho em uma tarefa específica. No contexto de modelos de linguagem, podemos ajustar o modelo pré-treinado _com um conjunto selecionado de exemplos para uma determinada tarefa ou domínio de aplicação_ para criar um **modelo personalizado** que pode ser mais preciso e relevante para essa tarefa ou domínio específico. Um benefício adicional do ajuste fino é que ele também pode reduzir o número de exemplos necessários para a aprendizagem com poucos exemplos - reduzindo o uso de tokens e os custos relacionados.

## Quando e por que devemos ajustar os modelos?

Neste contexto, quando falamos de ajuste fino, estamos nos referindo ao ajuste fino **supervisionado**, onde o re-treinamento é feito **adicionando novos dados** que não faziam parte do conjunto de dados original de treinamento. Isso é diferente de uma abordagem de ajuste fino não supervisionado, onde o modelo é re-treinado nos dados originais, mas com diferentes hiperparâmetros.

O ponto principal a lembrar é que o ajuste fino é uma técnica avançada que requer um certo nível de especialização para obter os resultados desejados. Se feito incorretamente, pode não fornecer as melhorias esperadas e até mesmo prejudicar o desempenho do modelo para o seu domínio-alvo.

Portanto, antes de aprender "como" ajustar modelos de linguagem, precisa saber "por que" deve seguir esse caminho e "quando" iniciar o processo de ajuste fino. Comece fazendo a si mesmo estas perguntas:

- **Caso de Uso**: Qual é o seu _caso de uso_ para o ajuste fino? Que aspecto do modelo pré-treinado atual deseja melhorar?
- **Alternativas**: Já tentou _outras técnicas_ para alcançar os resultados desejados? Use-as para criar uma linha de base para comparação.
  - Engenharia de prompts: Experimente técnicas como prompts com poucos exemplos de respostas relevantes. Avalie a qualidade das respostas.
  - Geração Aumentada por Recuperação: Experimente aumentar os prompts com resultados de consulta recuperados ao pesquisar os seus dados. Avalie a qualidade das respostas.
- **Custos**: Já identificou os custos do ajuste fino?
  - Ajustabilidade - o modelo pré-treinado está disponível para ajuste fino?
  - Esforço - para preparar os dados de treinamento, avaliar e refinar o modelo.
  - Computação - para executar os trabalhos de ajuste fino e implementar o modelo ajustado.
  - Dados - acesso a exemplos de qualidade suficientes para impactar o ajuste fino.
- **Benefícios**: Confirmou os benefícios do ajuste fino?
  - Qualidade - o modelo ajustado superou a linha de base?
  - Custo - reduz o uso de tokens simplificando os prompts?
  - Extensibilidade - pode reutilizar o modelo base para novos domínios?

Ao responder a essas perguntas, deverá ser capaz de decidir se o ajuste fino é a abordagem certa para o seu caso de uso. Idealmente, a abordagem é válida apenas se os benefícios superarem os custos. Depois de decidir prosseguir, é hora de pensar em _como_ pode ajustar o modelo pré-treinado.

Quer obter mais informações sobre o processo de tomada de decisão? Assista [Ajustar ou não ajustar](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Como podemos ajustar um modelo pré-treinado?

Para ajustar um modelo pré-treinado, precisa ter:

- um modelo pré-treinado para ajustar
- um conjunto de dados para usar no ajuste fino
- um ambiente de treinamento para executar o trabalho de ajuste fino
- um ambiente de hospedagem para implementar o modelo ajustado

## Ajuste Fino em Ação

Os seguintes recursos fornecem tutoriais passo a passo para guiá-lo por um exemplo real usando um modelo selecionado com um conjunto de dados curado. Para trabalhar nesses tutoriais, precisa de uma conta no provedor específico, juntamente com acesso ao modelo e conjuntos de dados relevantes.

| Provedor     | Tutorial                                                                                                                                                                       | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Como ajustar modelos de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Aprenda a ajustar um `gpt-35-turbo` para um domínio específico ("assistente de receitas") preparando dados de treinamento, executando o trabalho de ajuste fino e usando o modelo ajustado para inferência.                                                                                                                                                                                                                       |
| Azure OpenAI | [Tutorial de ajuste fino do GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Aprenda a ajustar um modelo `gpt-35-turbo-0613` **no Azure** seguindo os passos para criar e carregar dados de treinamento, executar o trabalho de ajuste fino. Implemente e use o novo modelo.                                                                                                                                                                                                                                   |
| Hugging Face | [Ajuste fino de LLMs com Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Este post no blog guia-o no ajuste fino de um _LLM aberto_ (ex: `CodeLlama 7B`) usando a biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) e [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) com [conjuntos de dados abertos](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) no Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Ajuste fino de LLMs com AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ou AutoTrain Advanced) é uma biblioteca Python desenvolvida pela Hugging Face que permite o ajuste fino para muitas tarefas diferentes, incluindo ajuste fino de LLM. AutoTrain é uma solução sem código e o ajuste fino pode ser feito na sua própria nuvem, no Hugging Face Spaces ou localmente. Ele suporta tanto uma interface gráfica baseada na web, quanto CLI e treinamento via arquivos de configuração yaml.              |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Tarefa

Selecione um dos tutoriais acima e siga os passos. _Podemos replicar uma versão desses tutoriais em Jupyter Notebooks neste repositório apenas para referência. Por favor, use as fontes originais diretamente para obter as versões mais recentes_.

## Excelente Trabalho! Continue a Aprender.

Depois de concluir esta lição, confira a nossa [coleção de aprendizagem sobre IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a expandir o seu conhecimento sobre IA generativa!

Parabéns!! Concluiu a última lição da série v2 deste curso! Não pare de aprender e construir. **Confira a página de [RECURSOS](RESOURCES.md?WT.mc_id=academic-105485-koreyst) para uma lista de sugestões adicionais sobre este tema.

A nossa série de lições v1 também foi atualizada com mais tarefas e conceitos. Então, reserve um momento para refrescar o seu conhecimento - e por favor [partilhe as suas perguntas e feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) para nos ajudar a melhorar estas lições para a comunidade.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.