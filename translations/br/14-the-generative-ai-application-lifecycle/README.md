<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b9d32511b27373a1b21b5789d4fda057",
  "translation_date": "2025-10-17T16:00:59+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "br"
}
-->
[![Integrando com chamadas de função](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.br.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# O Ciclo de Vida de Aplicações de IA Generativa

Uma questão importante para todas as aplicações de IA é a relevância dos recursos de IA, já que este é um campo que evolui rapidamente. Para garantir que sua aplicação permaneça relevante, confiável e robusta, é necessário monitorá-la, avaliá-la e melhorá-la continuamente. É aqui que entra o ciclo de vida da IA generativa.

O ciclo de vida da IA generativa é um framework que orienta você pelas etapas de desenvolvimento, implantação e manutenção de uma aplicação de IA generativa. Ele ajuda a definir seus objetivos, medir seu desempenho, identificar desafios e implementar soluções. Também auxilia a alinhar sua aplicação com os padrões éticos e legais do seu domínio e das partes interessadas. Ao seguir o ciclo de vida da IA generativa, você garante que sua aplicação esteja sempre entregando valor e satisfazendo seus usuários.

## Introdução

Neste capítulo, você irá:

- Compreender a Mudança de Paradigma de MLOps para LLMOps
- O Ciclo de Vida de LLM
- Ferramentas para o Ciclo de Vida
- Métricas e Avaliação do Ciclo de Vida

## Compreender a Mudança de Paradigma de MLOps para LLMOps

Os LLMs são uma nova ferramenta no arsenal da Inteligência Artificial. Eles são incrivelmente poderosos em tarefas de análise e geração para aplicações, mas esse poder traz algumas consequências na forma como otimizamos tarefas de IA e Aprendizado de Máquina Clássico.

Com isso, precisamos de um novo paradigma para adaptar essa ferramenta de maneira dinâmica, com os incentivos corretos. Podemos categorizar as aplicações de IA mais antigas como "Apps de ML" e as mais recentes como "Apps de IA Generativa" ou simplesmente "Apps de IA", refletindo a tecnologia e as técnicas predominantes na época. Isso muda nossa narrativa de várias maneiras. Veja a comparação abaixo.

![Comparação entre LLMOps e MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.br.png)

Note que no LLMOps estamos mais focados nos desenvolvedores de aplicativos, utilizando integrações como ponto-chave, usando "Modelos como Serviço" e pensando nos seguintes pontos para métricas:

- Qualidade: Qualidade das respostas
- Prejuízo: IA responsável
- Honestidade: Fundamentação das respostas (Faz sentido? Está correto?)
- Custo: Orçamento da solução
- Latência: Tempo médio para resposta de tokens

## O Ciclo de Vida de LLM

Primeiro, para entender o ciclo de vida e as modificações, vamos observar o infográfico a seguir.

![Infográfico de LLMOps](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.br.png)

Como você pode notar, isso é diferente dos ciclos de vida usuais do MLOps. Os LLMs têm muitos novos requisitos, como engenharia de prompts, diferentes técnicas para melhorar a qualidade (Fine-Tuning, RAG, Meta-Prompts), diferentes avaliações e responsabilidade com IA responsável, e, por fim, novas métricas de avaliação (Qualidade, Prejuízo, Honestidade, Custo e Latência).

Por exemplo, veja como ideamos. Usamos engenharia de prompts para experimentar com vários LLMs e explorar possibilidades para testar se suas hipóteses podem estar corretas.

Note que isso não é linear, mas sim ciclos integrados, iterativos e com um ciclo abrangente.

Como podemos explorar essas etapas? Vamos detalhar como construir um ciclo de vida.

![Fluxo de trabalho de LLMOps](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.br.png)

Isso pode parecer um pouco complicado, então vamos focar nos três grandes passos primeiro.

1. Ideação/Exploração: Exploração. Aqui podemos explorar de acordo com as necessidades do negócio. Prototipar, criar um [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) e testar se é eficiente o suficiente para nossa hipótese.
2. Construção/Aprimoramento: Implementação. Agora começamos a avaliar conjuntos de dados maiores, implementar técnicas como Fine-Tuning e RAG para verificar a robustez da solução. Se não funcionar, reimplementar, adicionar novos passos no fluxo ou reestruturar os dados pode ajudar. Após testar nosso fluxo e escala, se funcionar e atender às métricas, está pronto para o próximo passo.
3. Operacionalização: Integração. Agora adicionamos sistemas de monitoramento e alertas ao sistema, implantação e integração da aplicação ao nosso aplicativo.

Depois, temos o ciclo abrangente de Gestão, focando em segurança, conformidade e governança.

Parabéns, agora sua aplicação de IA está pronta para ser operacionalizada. Para uma experiência prática, confira o [Demo do Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Agora, quais ferramentas podemos usar?

## Ferramentas para o Ciclo de Vida

Para ferramentas, a Microsoft oferece a [Plataforma Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) e o [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) para facilitar e tornar seu ciclo fácil de implementar e pronto para uso.

A [Plataforma Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) permite que você use o [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). O AI Studio é um portal web que permite explorar modelos, exemplos e ferramentas. Gerenciar seus recursos, fluxos de desenvolvimento de UI e opções de SDK/CLI para desenvolvimento orientado por código.

![Possibilidades do Azure AI](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.br.png)

O Azure AI permite que você utilize múltiplos recursos para gerenciar suas operações, serviços, projetos, busca vetorial e necessidades de banco de dados.

![LLMOps com Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.br.png)

Construa, desde Provas de Conceito (POC) até aplicações em larga escala com o PromptFlow:

- Projete e construa aplicativos no VS Code, com ferramentas visuais e funcionais
- Teste e ajuste seus aplicativos para IA de qualidade, com facilidade
- Use o Azure AI Studio para integrar e iterar com a nuvem, fazer push e deploy para integração rápida

![LLMOps com PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.br.png)

## Ótimo! Continue Aprendendo!

Incrível! Agora aprenda mais sobre como estruturamos uma aplicação para usar os conceitos com o [App Contoso Chat](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), para ver como a Advocacia na Nuvem aplica esses conceitos em demonstrações. Para mais conteúdo, confira nossa [sessão de breakout no Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Agora, confira a Lição 15 para entender como [Geração Aumentada por Recuperação e Bancos de Dados Vetoriais](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) impactam a IA Generativa e ajudam a criar aplicações mais envolventes!

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.