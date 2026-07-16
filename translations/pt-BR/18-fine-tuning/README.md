[![Modelos Open Source](../../../translated_images/pt-BR/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Ajustando Seu LLM

Usar grandes modelos de linguagem para construir aplicações de IA generativa traz novos desafios. Uma questão chave é garantir a qualidade da resposta (precisão e relevância) no conteúdo gerado pelo modelo para uma determinada solicitação do usuário. Em lições anteriores, discutimos técnicas como engenharia de prompts e geração aumentada por recuperação que tentam resolver o problema modificando a entrada do prompt para o modelo existente.

Na lição de hoje, discutimos uma terceira técnica, **ajuste fino**, que tenta enfrentar o desafio re-treinando o próprio modelo com dados adicionais. Vamos mergulhar nos detalhes.

## Objetivos de Aprendizagem

Esta lição introduz o conceito de ajuste fino para modelos de linguagem pré-treinados, explora os benefícios e desafios dessa abordagem, e fornece orientações sobre quando e como usar ajuste fino para melhorar o desempenho dos seus modelos de IA generativa.

Ao final desta lição, você deverá ser capaz de responder às seguintes perguntas:

- O que é ajuste fino para modelos de linguagem?
- Quando e por que o ajuste fino é útil?
- Como posso ajustar finamente um modelo pré-treinado?
- Quais são as limitações do ajuste fino?

Pronto? Vamos começar.

## Guia Ilustrado

Quer ter uma visão geral do que vamos cobrir antes de começar? Confira este guia ilustrado que descreve a jornada de aprendizagem para esta lição — desde aprender os conceitos principais e a motivação para o ajuste fino, até entender o processo e as melhores práticas para executar a tarefa de ajuste fino. Este é um tópico fascinante para exploração, então não esqueça de visitar a página de [Recursos](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) para links adicionais que apoiem sua jornada de aprendizado autodirigido!

![Guia Ilustrado para Ajuste Fino de Modelos de Linguagem](../../../translated_images/pt-BR/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## O que é ajuste fino para modelos de linguagem?

Por definição, grandes modelos de linguagem são _pré-treinados_ com grandes quantidades de texto provenientes de fontes diversas, incluindo a internet. Como aprendemos em lições anteriores, precisamos de técnicas como _engenharia de prompts_ e _geração aumentada por recuperação_ para melhorar a qualidade das respostas do modelo às perguntas dos usuários ("prompts").

Uma técnica popular de engenharia de prompts envolve dar ao modelo mais orientação sobre o que se espera na resposta, seja fornecendo _instruções_ (orientação explícita) ou _dando alguns exemplos_ (orientação implícita). Isso é chamado de _few-shot learning_, mas possui duas limitações:

- Limites de tokens do modelo podem restringir o número de exemplos que você pode fornecer e limitar a eficácia.
- Custos de tokens do modelo podem tornar caro adicionar exemplos a cada prompt e limitar a flexibilidade.

Ajuste fino é uma prática comum em sistemas de aprendizado de máquina, onde pegamos um modelo pré-treinado e o re-treinamos com novos dados para melhorar seu desempenho em uma tarefa específica. No contexto dos modelos de linguagem, podemos ajustar finamente o modelo pré-treinado _com um conjunto selecionado de exemplos para uma tarefa ou domínio específico_ para criar um **modelo customizado** que pode ser mais preciso e relevante para essa tarefa ou domínio específico. Um benefício adicional do ajuste fino é que ele pode reduzir o número de exemplos necessários para few-shot learning — reduzindo o uso de tokens e custos relacionados.

## Quando e por que devemos ajustar finamente modelos?

Neste _contexto_, quando falamos de ajuste fino, estamos nos referindo ao ajuste fino **supervisionado**, onde o re-treinamento é feito **adicionando novos dados** que não faziam parte do conjunto original de treinamento. Isso é diferente da abordagem de ajuste fino não supervisionado, onde o modelo é re-treinado nos dados originais, mas com hiperparâmetros diferentes.

O ponto chave a lembrar é que ajuste fino é uma técnica avançada que requer um certo nível de expertise para alcançar os resultados desejados. Se feito incorretamente, pode não fornecer as melhorias esperadas e até degradar o desempenho do modelo para seu domínio específico.

Então, antes de aprender "como" ajustar finamente modelos de linguagem, você precisa saber "por que" deve seguir esse caminho e "quando" iniciar o processo de ajuste fino. Comece perguntando a si mesmo estas questões:

- **Caso de Uso**: Qual é seu _caso de uso_ para ajuste fino? Que aspecto do modelo pré-treinado atual você quer melhorar?
- **Alternativas**: Você já tentou _outras técnicas_ para alcançar os resultados desejados? Use-as para criar uma base de comparação.
  - Engenharia de prompts: Experimente técnicas como few-shot prompting com exemplos relevantes. Avalie a qualidade das respostas.
  - Geração aumentada por recuperação: Experimente aumentar os prompts com resultados de consultas recuperados dos seus dados. Avalie a qualidade das respostas.
- **Custos**: Você já identificou os custos para ajuste fino?
  - Ajustabilidade — o modelo pré-treinado está disponível para ajuste fino?
  - Esforço — para preparar dados de treinamento, avaliar e refinar o modelo.
  - Computação — para executar os trabalhos de ajuste fino e implantar o modelo ajustado.
  - Dados — acesso a exemplos de qualidade suficiente para o impacto do ajuste fino.
- **Benefícios**: Você confirmou os benefícios do ajuste fino?
  - Qualidade — o modelo ajustado superou a linha de base?
  - Custo — ele reduz o uso de tokens ao simplificar os prompts?
  - Extensibilidade — você pode reaproveitar o modelo base para novos domínios?

Respondendo a essas perguntas, você deve ser capaz de decidir se o ajuste fino é a abordagem certa para seu caso de uso. Idealmente, essa abordagem é válida apenas se os benefícios superarem os custos. Depois de decidir seguir em frente, é hora de pensar _como_ ajustar finamente o modelo pré-treinado.

Quer mais insights sobre o processo de tomada de decisão? Assista a [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Como podemos ajustar finamente um modelo pré-treinado?

Para ajustar finamente um modelo pré-treinado, você precisa ter:

- um modelo pré-treinado para ajustar
- um conjunto de dados para usar no ajuste fino
- um ambiente de treinamento para executar o trabalho de ajuste fino
- um ambiente de hospedagem para implantar o modelo ajustado

## Ajuste fino em ação

> **Nota:** `gpt-35-turbo` / `gpt-3.5-turbo`, referenciado em alguns dos tutoriais abaixo, foi descontinuado para inferência e ajuste fino. Se você está começando um novo trabalho de ajuste fino hoje, escolha um modelo atualmente suportado — por exemplo `gpt-4o-mini` ou `gpt-4.1-mini`. Veja a [lista de modelos ajustáveis](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) para o conjunto atual de modelos que podem ser ajustados. Os conceitos e passos nesses tutoriais ainda são válidos.

Os recursos seguintes fornecem tutoriais passo a passo para guiá-lo por um exemplo real usando um modelo selecionado com um conjunto de dados selecionado. Para seguir esses tutoriais, você precisa de uma conta no provedor específico, junto com acesso ao modelo relevante e aos conjuntos de dados.

| Provedor    | Tutorial                                                                                                                                                                       | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI      | [Como ajustar modelos de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Aprenda a ajustar finamente um `gpt-35-turbo` para um domínio específico ("assistente de receitas") preparando dados de treinamento, executando o trabalho de ajuste fino e usando o modelo ajustado para inferência.                                                                                                                                                                                                                  |
| Azure OpenAI| [Tutorial de ajuste fino GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Aprenda a ajustar finamente um modelo `gpt-35-turbo-0613` **no Azure** realizando os passos para criar & carregar os dados de treinamento, executar o trabalho de ajuste fino. Implante & utilize o novo modelo.                                                                                                                                                                                                                       |
| Hugging Face| [Ajuste fino de LLMs com Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Este post no blog guia você pelo ajuste fino de um _LLM aberto_ (ex: `CodeLlama 7B`) usando a biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) com [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) abertos no Hugging Face.          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Ajuste fino de LLMs com AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ou AutoTrain Advanced) é uma biblioteca Python desenvolvida pela Hugging Face que permite ajuste fino para várias tarefas, incluindo ajuste fino de LLMs. AutoTrain é uma solução sem código e o ajuste pode ser feito na sua própria nuvem, no Hugging Face Spaces ou localmente. Suporta interface web, CLI e treinamento via arquivos de configuração yaml.                                                                 |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Ajuste fino de LLMs com Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth é uma estrutura open-source que suporta ajuste fino de LLMs e aprendizado por reforço (RL). Unsloth simplifica o treinamento local, avaliação e implantação com [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) prontos para uso. Também suporta conversão texto-fala (TTS), modelos BERT e multimodais. Para começar, leia o passo a passo no [Guia de Ajuste Fino para LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tarefa

Selecione um dos tutoriais acima e siga os passos. _Podemos replicar uma versão desses tutoriais em Jupyter Notebooks neste repositório apenas para referência. Use as fontes originais diretamente para obter as versões mais recentes_.

## Excelente trabalho! Continue seu aprendizado.

Após completar esta lição, confira nossa [coleção de Aprendizagem em IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Parabéns!! Você completou a última lição da série v2 deste curso! Não pare de aprender e construir. \*\*Veja a página de [RECURSOS](RESOURCES.md?WT.mc_id=academic-105485-koreyst) para uma lista de sugestões adicionais apenas sobre este tema.

Nossa série v1 de lições também foi atualizada com mais tarefas e conceitos. Então tire um minuto para refrescar seu conhecimento — e por favor [compartilhe suas dúvidas e feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) para nos ajudar a melhorar essas lições para a comunidade.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->