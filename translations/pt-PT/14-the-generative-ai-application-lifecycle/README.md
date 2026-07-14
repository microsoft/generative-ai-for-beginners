[![Integração com chamada de função](../../../translated_images/pt-PT/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# O Ciclo de Vida da Aplicação de IA Generativa

Uma questão importante para todas as aplicações de IA é a relevância das funcionalidades de IA, uma vez que a IA é um campo de rápida evolução. Para garantir que a sua aplicação permanece relevante, fiável e robusta, é necessário monitorizá-la, avaliá-la e melhorá-la continuamente. É aqui que o ciclo de vida da IA generativa entra em ação.

O ciclo de vida da IA generativa é uma estrutura que o orienta através das etapas de desenvolvimento, implementação e manutenção de uma aplicação de IA generativa. Ajuda-o a definir os seus objetivos, medir o seu desempenho, identificar os seus desafios e implementar as suas soluções. Também ajuda a alinhar a sua aplicação com os padrões éticos e legais do seu domínio e dos seus intervenientes. Seguindo o ciclo de vida da IA generativa, pode assegurar que a sua aplicação está sempre a entregar valor e a satisfazer os seus utilizadores.

## Introdução

Neste capítulo, irá:

- Compreender a mudança de paradigma de MLOps para LLMOps
- O Ciclo de Vida dos LLM
- Ferramentas do Ciclo de Vida
- Metrificação e Avaliação do Ciclo de Vida

## Compreender a mudança de paradigma de MLOps para LLMOps

Os LLM são uma nova ferramenta no arsenal da Inteligência Artificial, sendo incrivelmente poderosos em tarefas de análise e geração para aplicações, contudo este poder tem algumas consequências na forma como simplificamos as tarefas de IA clássica e Aprendizagem Automática.

Por isso, precisamos de um novo paradigma para adaptar esta ferramenta de forma dinâmica, com os incentivos corretos. Podemos categorizar as aplicações de IA antigas como "Apps de ML" e as aplicações de IA mais recentes como "Apps de GenAI" ou simplesmente "Apps de IA", refletindo a tecnologia e as técnicas predominantes na altura. Isto altera a nossa narrativa de várias formas, veja a seguinte comparação.

![Comparação LLMOps vs. MLOps](../../../translated_images/pt-PT/01-llmops-shift.29bc933cb3bb0080.webp)

Note que em LLMOps o foco está mais nos Desenvolvedores de Aplicações, usando integrações como ponto-chave, utilizando "Modelos-como-serviço" e considerando os seguintes pontos para métricas.

- Qualidade: Qualidade da resposta
- Dano: IA responsável
- Honestidade: Fundamentação da resposta (Faz sentido? Está correta?)
- Custo: Orçamento da solução
- Latência: Tempo médio para resposta do token

## O Ciclo de Vida dos LLM

Primeiro, para compreender o ciclo de vida e as modificações, vejamos a próxima infografia.

![Infografia LLMOps](../../../translated_images/pt-PT/02-llmops.70a942ead05a7645.webp)

Como pode notar, isto é diferente dos Ciclos de Vida habituais de MLOps. Os LLM têm muitos novos requisitos, como Prompting, diferentes técnicas para melhorar a qualidade (Fine-Tuning, RAG, Meta-Prompts), avaliação diferente e responsabilidade com IA responsável, e, por fim, novas métricas de avaliação (Qualidade, Dano, Honestidade, Custo e Latência).

Por exemplo, veja como ideamos. Usando engenharia de prompt para experimentar com vários LLMs para explorar possibilidades e testar se a sua hipótese pode ser correta.

Note que isto não é linear, mas sim loops integrados, iterativos e com um ciclo abrangente.

Como poderíamos explorar essas etapas? Vamos entrar em pormenor de como construir um ciclo de vida.

![Fluxo de trabalho LLMOps](../../../translated_images/pt-PT/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Isto pode parecer um pouco complicado, vamos focar primeiramente nos três grandes passos.

1. Ideação/Exploração: Exploração, aqui podemos explorar de acordo com as necessidades do nosso negócio. Prototipagem, criando um [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) e testando se é suficientemente eficiente para a nossa hipótese.
1. Construção/Aumento: Implementação, agora começamos a avaliar para conjuntos de dados maiores, implementamos técnicas como Fine-Tuning e RAG para verificar a robustez da nossa solução. Se não for adequada, reimplementar, adicionar novos passos no nosso fluxo ou reestruturar os dados pode ajudar. Após testar o nosso fluxo e a escala, se funcionar e as métricas estiverem ok, está pronto para o próximo passo.
1. Operacionalização: Integração, agora adicionamos Sistemas de Monitorização e Alertas ao sistema, assim como o deployment e a integração da aplicação.

Depois, temos o ciclo abrangente de Gestão, focando em segurança, conformidade e governação.

Parabéns, agora tem a sua aplicação de IA pronta e operacional. Para uma experiência prática, dê uma vista de olhos no [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Agora, que ferramentas podemos usar?

## Ferramentas do Ciclo de Vida

Para ferramentas, a Microsoft disponibiliza a [Plataforma Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) e o [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) para facilitar e tornar o seu ciclo fácil de implementar e pronto a usar.

A [Plataforma Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst), permite usar o [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). O Microsoft Foundry (anteriormente Azure AI Studio) é um portal web que o deixa explorar modelos, exemplos e ferramentas, gerir os seus recursos e usar fluxos de desenvolvimento UI, bem como opções SDK/CLI para desenvolvimento orientado a código.

![Possibilidades do Azure AI](../../../translated_images/pt-PT/04-azure-ai-platform.80203baf03a12fa8.webp)

O Azure AI permite que utilize múltiplos recursos para gerir as suas operações, serviços, projetos, pesquisa vetorial e necessidades de bases de dados.

![LLMOps com Azure AI](../../../translated_images/pt-PT/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Construa, desde o Proof-of-Concept (POC) até aplicações em larga escala com PromptFlow:

- Desenhe e construa apps a partir do VS Code, com ferramentas visuais e funcionais
- Teste e ajuste as suas apps para IA de qualidade, com facilidade.
- Use o Microsoft Foundry para integrar e iterar com a cloud, push e deployment para integração rápida.

![LLMOps com PromptFlow](../../../translated_images/pt-PT/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Ótimo! Continue a aprender!

Fantástico, agora aprenda mais sobre como estruturamos uma aplicação para usar os conceitos com a [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), para ver como a Cloud Advocacy incorpora esses conceitos em demonstrações. Para mais conteúdos, confira a nossa [sessão breakout do Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Agora, veja a Lição 15, para compreender como [Retrieval Augmented Generation e Bases de Dados Vetoriais](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) impactam a IA Generativa e para criar aplicações mais envolventes!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->