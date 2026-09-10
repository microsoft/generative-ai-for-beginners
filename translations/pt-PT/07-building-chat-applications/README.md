# Construção de Aplicações de Chat com IA Generativa

[![Construção de Aplicações de Chat com IA Generativa](../../../translated_images/pt-PT/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Clique na imagem acima para ver o vídeo desta lição)_

Agora que vimos como podemos construir aplicações de geração de texto, vamos explorar aplicações de chat.

As aplicações de chat tornaram-se integradas nas nossas vidas diárias, oferecendo mais do que uma simples conversa casual. São partes integrantes do serviço ao cliente, suporte técnico e até sistemas consultivos sofisticados. É provável que tenha recebido alguma ajuda de uma aplicação de chat não há muito tempo. À medida que integramos tecnologias mais avançadas como a IA generativa nestas plataformas, a complexidade aumenta e também os desafios.

Algumas perguntas que precisamos esclarecer são:

- **Construção da aplicação**. Como podemos construir eficientemente e integrar sem falhas estas aplicações alimentadas por IA para casos de uso específicos?
- **Monitorização**. Depois de implementadas, como podemos monitorizar e garantir que as aplicações estão a funcionar com a mais alta qualidade, tanto em termos de funcionalidade como de conformidade com os [seis princípios da IA responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

À medida que avançamos para uma era definida pela automação e interações humano-máquina fluidas, compreender como a IA generativa transforma o alcance, profundidade e adaptabilidade das aplicações de chat torna-se essencial. Esta lição irá investigar os aspetos arquitetónicos que suportam estes sistemas complexos, explorar as metodologias para o seu ajuste fino para tarefas específicas de domínio, e avaliar as métricas e considerações pertinentes para assegurar uma implementação responsável da IA.

## Introdução

Esta lição cobre:

- Técnicas para construir e integrar aplicações de chat eficientemente.
- Como aplicar personalização e ajuste fino às aplicações.
- Estratégias e considerações para monitorizar eficazmente aplicações de chat.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Descrever considerações para construir e integrar aplicações de chat em sistemas existentes.
- Personalizar aplicações de chat para casos de uso específicos.
- Identificar métricas-chave e considerações para monitorizar e manter eficazmente a qualidade das aplicações de chat alimentadas por IA.
- Garantir que as aplicações de chat utilizam IA de forma responsável.

## Integração de IA Generativa em Aplicações de Chat

Elevar aplicações de chat através de IA generativa não se centra apenas em torná-las mais inteligentes; trata-se de otimizar a sua arquitetura, desempenho e interface de utilizador para oferecer uma experiência de qualidade. Isto envolve investigar as fundações arquitetónicas, integrações de API e considerações de interface do utilizador. Esta secção pretende oferecer-lhe um roteiro abrangente para navegar estes complexos cenários, seja integrando-os em sistemas existentes ou construindo-os como plataformas autónomas.

No final desta secção, estará equipado com a perícia necessária para construir e incorporar aplicações de chat eficientemente.

### Chatbot ou aplicação de chat?

Antes de mergulharmos na construção de aplicações de chat, vamos comparar 'chatbots' com 'aplicações de chat alimentadas por IA', que têm papéis e funcionalidades distintas. O principal propósito de um chatbot é automatizar tarefas conversacionais específicas, como responder a perguntas frequentes ou rastrear uma encomenda. É normalmente regido por lógica baseada em regras ou algoritmos complexos de IA. Em contraste, uma aplicação de chat alimentada por IA é um ambiente muito mais abrangente, concebido para facilitar várias formas de comunicação digital, como chats de texto, voz e vídeo entre utilizadores humanos. A sua característica definidora é a integração de um modelo de IA generativa que simula conversas subtis e semelhantes às humanas, gerando respostas baseadas numa grande variedade de entradas e pistas contextuais. Uma aplicação de chat potenciada por IA generativa pode envolver-se em discussões de domínio aberto, adaptar-se a contextos conversacionais em evolução, e até produzir diálogos criativos ou complexos.

A tabela abaixo delineia as principais diferenças e semelhanças para nos ajudar a entender seus papéis únicos na comunicação digital.

| Chatbot                               | Aplicação de Chat com IA Generativa       |
| ------------------------------------- | ----------------------------------------- |
| Focado em tarefas e baseado em regras  | Sensível ao contexto                      |
| Frequentemente integrado em sistemas maiores | Pode hospedar um ou múltiplos chatbots |
| Limitado a funções programadas         | Incorpora modelos de IA generativa         |
| Interações especializadas e estruturadas | Capaz de discussões de domínio aberto      |

### Aproveitar funcionalidades pré-construídas com SDKs e APIs

Ao construir uma aplicação de chat, um ótimo primeiro passo é avaliar o que já existe. Usar SDKs e APIs para construir aplicações de chat é uma estratégia vantajosa por várias razões. Ao integrar SDKs e APIs bem documentados, está a posicionar estrategicamente a sua aplicação para sucesso a longo prazo, abordando preocupações de escalabilidade e manutenção.

- **Acelera o processo de desenvolvimento e reduz a sobrecarga**: Confiar em funcionalidades pré-construídas em vez do processo dispendioso de construí-las você mesmo permite que se foque noutras partes da sua aplicação que possa considerar mais importantes, como a lógica de negócio.
- **Melhor desempenho**: Ao construir a funcionalidade a partir do zero, eventualmente perguntará "Como escala? Esta aplicação consegue lidar com um súbito aumento de utilizadores?" SDKs e APIs bem mantidas frequentemente têm soluções incorporadas para estas preocupações.
- **Manutenção facilitada**: Atualizações e melhorias são mais fáceis de gerir, visto que a maioria das APIs e SDKs apenas requer a atualização de uma biblioteca quando é lançada uma nova versão.
- **Acesso à tecnologia de ponta**: Aproveitar modelos que foram fino afinados e treinados em conjuntos de dados extensivos proporciona capacidades avançadas de linguagem natural à sua aplicação.

Aceder à funcionalidade de um SDK ou API envolve normalmente obter permissão para usar os serviços fornecidos, frequentemente através do uso de uma chave única ou token de autenticação. Usaremos a Biblioteca Python OpenAI para explorar como isto funciona. Também pode experimentar por si mesmo nos seguintes [notebook para OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) ou [notebook para Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) desta lição.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

O exemplo acima usa o modelo GPT-5 mini com a API Responses para completar o prompt, mas note que a chave da API é configurada previamente. Receberia um erro se não configurasse a chave.

## Experiência do Utilizador (UX)

Princípios gerais de UX aplicam-se às aplicações de chat, mas aqui estão algumas considerações adicionais que se tornam particularmente importantes devido aos componentes de aprendizagem automática envolvidos.

- **Mecanismo para resolver ambiguidades**: Os modelos de IA generativa ocasionalmente geram respostas ambíguas. Uma funcionalidade que permite aos utilizadores pedir esclarecimentos pode ser útil caso encontrem este problema.
- **Retenção de contexto**: Modelos avançados de IA generativa têm a capacidade de lembrar o contexto dentro de uma conversa, o que pode ser um ativo necessário para a experiência do utilizador. Dar aos utilizadores a capacidade de controlar e gerir o contexto melhora a experiência, mas introduz o risco de reter informação sensível. Considerações sobre o tempo de armazenamento desses dados, como a introdução de uma política de retenção, podem equilibrar a necessidade de contexto com a privacidade.
- **Personalização**: Com a capacidade de aprender e adaptar-se, os modelos de IA oferecem uma experiência individualizada para o utilizador. Adaptar a experiência do utilizador através de funcionalidades como perfis de utilizador não só faz com que o utilizador se sinta compreendido, como também ajuda na sua procura por respostas específicas, criando uma interação mais eficiente e satisfatória.

Um exemplo dessa personalização são as definições "Instruções Personalizadas" no ChatGPT da OpenAI. Permitem-lhe fornecer informações sobre si que podem ser um contexto importante para os seus prompts. Aqui está um exemplo de uma instrução personalizada.

![Definições de Instruções Personalizadas no ChatGPT](../../../translated_images/pt-PT/custom-instructions.b96f59aa69356fcf.webp)

Este "perfil" pede ao ChatGPT para criar um plano de aula sobre listas ligadas. Note que o ChatGPT tem em conta que o utilizador pode querer um plano de aula mais aprofundado baseado na sua experiência.

![Um prompt no ChatGPT para um plano de aula sobre listas ligadas](../../../translated_images/pt-PT/lesson-plan-prompt.cc47c488cf1343df.webp)

### Estrutura de Mensagens de Sistema da Microsoft para Grandes Modelos de Linguagem

[A Microsoft forneceu orientações](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) para escrever mensagens de sistema eficazes ao gerar respostas de LLMs, divididas em 4 áreas:

1. Definir para quem é o modelo, bem como as suas capacidades e limitações.
2. Definir o formato da saída do modelo.
3. Fornecer exemplos específicos que demonstrem o comportamento pretendido do modelo.
4. Fornecer salvaguardas comportamentais adicionais.

### Acessibilidade

Quer um utilizador tenha deficiências visuais, auditivas, motoras ou cognitivas, uma aplicação de chat bem concebida deve ser utilizável por todos. A lista a seguir detalha funcionalidades específicas destinadas a melhorar a acessibilidade para diversas deficiências dos utilizadores.

- **Funcionalidades para Deficiência Visual**: Temas de alto contraste e texto redimensionável, compatibilidade com leitores de ecrã.
- **Funcionalidades para Deficiência Auditiva**: Funções de texto para fala e fala para texto, indicações visuais para notificações áudio.
- **Funcionalidades para Deficiência Motora**: Suporte para navegação por teclado, comandos de voz.
- **Funcionalidades para Deficiência Cognitiva**: Opções de linguagem simplificada.

## Personalização e Ajuste Fino para Modelos de Linguagem Específicos de Domínio

Imagine uma aplicação de chat que compreende a linguagem técnica da sua empresa e antecipa as consultas específicas que a sua base de utilizadores tem habitualmente. Existem algumas abordagens que vale a pena mencionar:

- **Aproveitar modelos DSL**. DSL significa linguagem específica de domínio. Pode aproveitar um modelo chamado DSL treinado num domínio específico para entender os seus conceitos e cenários.
- **Aplicar ajuste fino**. Ajuste fino é o processo de treinar ainda mais o seu modelo com dados específicos.

## Personalização: Usar um DSL

Aproveitar modelos de linguagem específicos de domínio (Modelos DSL) pode aumentar o engajamento do utilizador ao fornecer interações especializadas e contextualmente relevantes. É um modelo treinado ou ajustado para entender e gerar texto relacionado a um campo, indústria ou assunto específico. As opções para usar um modelo DSL podem variar desde treinar um do zero até usar modelos pré-existentes através de SDKs e APIs. Outra opção é o ajuste fino, que envolve pegar um modelo pré-treinado existente e adaptá-lo para um domínio específico.

## Personalização: Aplicar Ajuste Fino

O ajuste fino é frequentemente considerado quando um modelo pré-treinado não é suficiente para um domínio especializado ou tarefa específica.

Por exemplo, consultas médicas são complexas e requerem muito contexto. Quando um profissional de saúde diagnostica um paciente, baseia-se numa variedade de fatores como estilo de vida ou condições pré-existentes, e pode até confiar em jornais médicos recentes para validar o seu diagnóstico. Em cenários tão pormenorizados, uma aplicação de chat de IA para propósito geral não pode ser uma fonte fiável.

### Cenário: uma aplicação médica

Considere uma aplicação de chat concebida para ajudar profissionais médicos, fornecendo referências rápidas a diretrizes de tratamento, interações medicamentosas ou descobertas de investigação recentes.

Um modelo para propósito geral pode ser adequado para responder a perguntas médicas básicas ou fornecer conselhos gerais, mas pode ter dificuldades com o seguinte:

- **Casos altamente específicos ou complexos**. Por exemplo, um neurologista pode perguntar à aplicação: "Quais são as melhores práticas atuais para gerir epilepsia resistente a medicamentos em pacientes pediátricos?"
- **Falta de avanços recentes**. Um modelo para propósito geral pode ter dificuldade em fornecer uma resposta atualizada que incorpore os avanços mais recentes em neurologia e farmacologia.

Nesses casos, ajustar finamente o modelo com um conjunto de dados médicos especializado pode melhorar significativamente a sua capacidade de lidar com essas questões médicas complexas de forma mais precisa e fiável. Isto requer acesso a um conjunto de dados grande e relevante que represente os desafios e perguntas específicas do domínio que precisam ser abordados.

## Considerações para uma Experiência de Chat de Alta Qualidade com IA

Esta secção delineia os critérios para aplicações de chat de "alta qualidade", que incluem a captura de métricas acionáveis e a adesão a um quadro que utiliza a tecnologia de IA de forma responsável.

### Métricas-Chave

Para manter o desempenho de alta qualidade de uma aplicação, é essencial acompanhar métricas e considerações chave. Estas medidas não só garantem a funcionalidade da aplicação, mas também avaliam a qualidade do modelo de IA e a experiência do utilizador. Abaixo está uma lista que cobre métricas básicas, de IA e de experiência do utilizador a considerar.

| Métrica                       | Definição                                                                                                          | Considerações para o Desenvolvedor de Chat                           |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Tempo de atividade**         | Mede o tempo em que a aplicação está operacional e acessível aos utilizadores.                                     | Como minimizará o tempo de inatividade?                            |
| **Tempo de resposta**          | O tempo levado pela aplicação para responder à consulta de um utilizador.                                          | Como pode otimizar o processamento de consultas para melhorar o tempo de resposta? |
| **Precisão**                  | A proporção de previsões verdadeiramente positivas em relação ao total de previsões positivas.                     | Como validará a precisão do seu modelo?                            |
| **Recall (Sensibilidade)**     | A proporção de previsões verdadeiramente positivas em relação ao número real de positivos.                         | Como medirá e melhorará o recall?                                  |
| **Pontuação F1**              | A média harmónica da precisão e do recall, que equilibra o compromisso entre ambos.                                | Qual é a sua meta de Pontuação F1? Como equilibrará precisão e recall? |
| **Perplexidade**              | Mede o quão bem a distribuição de probabilidade prevista pelo modelo se alinha com a distribuição real dos dados. | Como minimizará a perplexidade?                                   |
| **Métricas de Satisfação do Utilizador** | Mede a perceção do utilizador sobre a aplicação. Frequentemente capturadas através de inquéritos.              | Com que frequência recolherá feedback dos utilizadores? Como irá adaptar-se com base nisso? |
| **Taxa de Erro**              | A taxa com que o modelo comete erros na compreensão ou saída.                                                      | Que estratégias tem para reduzir as taxas de erro?                |
| **Ciclos de Re-treinamento** | A frequência com que o modelo é atualizado para incorporar novos dados e insights.                                | Com que frequência fará re-treinamento do modelo? O que desencadeará um ciclo de re-treinamento? |

| **Detecção de Anomalias**     | Ferramentas e técnicas para identificar padrões invulgares que não se conformam com o comportamento esperado.               | Como irá responder às anomalias?                                           |

### Implementar Práticas de IA Responsável em Aplicações de Chat

A abordagem da Microsoft para a IA Responsável identificou seis princípios que devem orientar o desenvolvimento e uso da IA. Abaixo estão os princípios, a sua definição, e aspetos que um programador de chat deve considerar e porque devem levá-los a sério.

| Princípios             | Definição da Microsoft                               | Considerações para o Programador de Chat                                  | Porque é Importante                                                                   |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| Equidade               | Os sistemas de IA devem tratar todas as pessoas de forma justa. | Assegurar que a aplicação de chat não discrimine com base em dados dos utilizadores. | Para construir confiança e inclusão entre os utilizadores; evita implicações legais.  |
| Fiabilidade e Segurança | Os sistemas de IA devem operar de forma fiável e segura. | Implementar testes e mecanismos de segurança para minimizar erros e riscos. | Garante a satisfação dos utilizadores e evita potenciais danos.                      |
| Privacidade e Segurança | Os sistemas de IA devem ser seguros e respeitar a privacidade. | Implementar encriptação robusta e medidas de proteção dos dados.         | Para proteger dados sensíveis dos utilizadores e cumprir as leis de privacidade.     |
| Inclusividade          | Os sistemas de IA devem capacitar todos e envolver as pessoas. | Projetar UI/UX acessível e fácil de usar para públicos diversos.         | Assegura que um maior número de pessoas possa usar a aplicação de forma eficaz.      |
| Transparência           | Os sistemas de IA devem ser compreensíveis.           | Fornecer documentação clara e justificação para as respostas de IA.      | Os utilizadores tendem a confiar mais num sistema se puderem entender como as decisões são tomadas. |
| Responsabilização       | As pessoas devem ser responsabilizáveis pelos sistemas de IA. | Estabelecer um processo claro para auditoria e melhoria das decisões de IA. | Permite melhorias contínuas e medidas corretivas em caso de erros.                   |

## Tarefa

Veja a [tarefa](../../../07-building-chat-applications/python). Ela irá guiá-lo(a) por uma série de exercícios, desde executar os seus primeiros prompts de chat, a classificar e resumir texto e mais. Note que as tarefas estão disponíveis em diferentes linguagens de programação!

## Excelente Trabalho! Continue a Jornada

Após completar esta lição, consulte a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar os seus conhecimentos em IA Generativa!

Dirija-se à Lição 8 para ver como pode começar a [construir aplicações de pesquisa](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->