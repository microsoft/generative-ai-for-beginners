# Building Generative AI-Powered Chat Applications

## Criando Aplicações Chat com IA Generativa

[![Building Generative AI-Powered Chat Applications](../../images/07-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed.html?id=57a31949-67c5-4020-8c85-91e4995589f3?WT.mc_id=academic-105485-koreyst)

> _(Clique na imagem acima para ver o vídeo da lição)_

Agora que vimos como podemos criar aplicativos de geração de texto, vamos dar uma olhada nos aplicativos de bate-papo.

Aplicativos de chat (bate-papo) tornaram-se integrados em nossas vidas diárias, oferecendo mais do que apenas um meio de conversa casual. Eles são partes integrantes do atendimento ao cliente, suporte técnico e até mesmo sistemas de consultoria sofisticados. É provável que você tenha recebido alguma ajuda de um aplicativo de bate-papo não há muito tempo. À medida que integramos tecnologias mais avançadas, como a IA generativa, nessas plataformas, a complexidade aumenta e, com ela, os desafios.

Algumas perguntas que precisamos responder são:

- **Criação de um aplicativo**: Como podemos criar de forma eficiente e integrar de maneira transparente esses aplicativos impulsionados por IA para casos de uso específicos?

- **Monitoramento**: Uma vez implantados, como podemos monitorar e garantir que os aplicativos estejam operando no mais alto nível de qualidade, tanto em termos de funcionalidade quanto na aderência aos [seis princípios de IA responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

À medida que avançamos para uma era definida pela automação e interações homem-máquina sem emendas, entender como a IA generativa transforma o escopo, a profundidade e a adaptabilidade dos aplicativos de chat torna-se essencial. Esta lição investigará os aspectos da arquitetura que suportam esses sistemas intricados, explorará as metodologias para ajustá-los para tarefas específicas de domínio e avaliará as métricas e considerações pertinentes para garantir a implantação responsável de IA.

## Introdução

Esta lição abrange:

- Técnicas para criar e integrar eficientemente aplicativos de chat.
- Como aplicar personalização e ajuste fino a aplicativos.
- Estratégias e considerações para monitorar efetivamente aplicativos de chat.

## Metas de Aprendizado

Até o final desta lição, você será capaz de:

- Descrever considerações para construir e integrar aplicativos de chat em sistemas existentes.
- Personalizar aplicativos de chat para casos de uso específicos.
- Identificar métricas-chave e considerações para monitorar e manter a qualidade de aplicativos de chat impulsionados por IA.
- Garantir que os aplicativos de chat utilizem a IA de maneira responsável.

## Integrando IA Generativa em Aplicativos de Chat

Elevar aplicativos de chat por meio de IA generativa não se concentra apenas em torná-los mais inteligentes; trata-se de otimizar sua arquitetura, desempenho e interface do usuário para oferecer uma experiência de usuário de qualidade. Isso envolve investigar as bases arquitetônicas, integrações de API e considerações de interface do usuário. Esta seção visa oferecer a você um roteiro abrangente para navegar por essas paisagens complexas, seja você integrando-os em sistemas existentes ou construindo-os como plataformas independentes.

Ao final desta seção, você estará equipado com a experiência necessária para construir e incorporar eficientemente aplicativos de chat.

### Chatbot ou Aplicação de Chat?

Antes de nos aprofundarmos na criação de aplicativos de chat, vamos comparar 'chatbots' com 'aplicações de chat impulsionadas por IA', que desempenham papéis e funcionalidades distintas. O principal propósito de um chatbot é automatizar tarefas conversacionais específicas, como responder a perguntas frequentes ou rastrear um pacote. Normalmente, ele é governado por lógica baseada em regras ou algoritmos complexos de IA. Em contraste, uma aplicação de chat impulsionada por IA é um ambiente muito mais expansivo projetado para facilitar várias formas de comunicação digital, como chats de texto, voz e vídeo entre usuários humanos. Sua característica definidora é a integração de um modelo de IA generativa que simula conversas matizadas e semelhantes às humanas, gerando respostas com base em uma ampla variedade de entradas e indicações contextuais. Uma aplicação de chat impulsionada por IA generativa pode participar de discussões em domínio aberto, adaptar-se a contextos conversacionais em evolução e até mesmo produzir diálogos criativos ou complexos.

A tabela abaixo destaca as principais diferenças e semelhanças para nos ajudar a entender seus papéis únicos na comunicação digital.

| Chatbot                                     | Aplicação de Chat Impulsionada por IA Generativa |
| ------------------------------------------- | ------------------------------------------------ |
| Focado em tarefas e baseado em regras       | Consciente do contexto                           |
| Frequentemente integrado a sistemas maiores | Pode hospedar um ou vários chatbots              |
| Limitado a funções programadas              | Incorpora modelos de IA generativa               |
| Interações especializadas e estruturadas    | Capaz de discussões em domínio aberto            |

### Alavancando funcionalidades pré-criadas com SDKs e APIs

Ao criar uma aplicação de chat, um ótimo primeiro passo é avaliar o que já está disponível. Utilizar SDKs e APIs para construir aplicações de chat é uma estratégia vantajosa por várias razões. Ao integrar SDKs e APIs bem documentados, você posiciona estrategicamente sua aplicação para o sucesso a longo prazo, abordando preocupações de escalabilidade e manutenção.

- **Acelera o processo de desenvolvimento e reduz o overhead**: Contar com funcionalidades pré-construídas, em vez do processo caro de construí-las, permite que você se concentre em outros aspectos da sua aplicação que possam ser mais importantes, como a lógica de negócios.

- **Melhor desempenho**: Ao construir funcionalidades do zero, eventualmente você se perguntará "Como ela escala? Esta aplicação é capaz de lidar com um aumento repentino de usuários?" SDKs e APIs bem mantidos frequentemente têm soluções embutidas para essas preocupações.

- **Manutenção mais fácil**: Atualizações e melhorias são mais fáceis de gerenciar, pois a maioria das APIs e SDKs simplesmente requer uma atualização de biblioteca quando uma versão mais recente é lançada.

- **Acesso a tecnologia de ponta**: Alavancar modelos que foram ajustados e treinados em conjuntos de dados extensivos proporciona à sua aplicação capacidades de linguagem natural.

Acesso à funcionalidade de um SDK ou API geralmente envolve a obtenção de permissão para usar os serviços fornecidos, frequentemente por meio do uso de uma chave única ou token de autenticação. Utilizaremos a Biblioteca Python da OpenAI para explorar como isso é feito. Você também pode experimentar por conta própria no seguinte [notebook para OpenAI](../../python/oai-assigment-simple.ipynb?WT.mc_id=academic-105485-koreyst) ou [Notebook para Serviços Azure OpenAI](../../python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) para esta lição.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

No exemplo acima é usado o modelo GPT-3.5 Turbo para completar o prompt. Mas observe que a chave da API é definida antes de fazê-lo. Você receberia o seguinte erro se não definisse a chave.

```output
AuthenticationError: No API key provided. You can set your API key in code using 'openai.api_key = <API-KEY>', or you can set the environment variable OPENAI_API_KEY=<API-KEY>). If your API key is stored in a file, you can point the openai module at it with 'openai.api_key_path = <PATH>'. You can generate API keys in the OpenAI web interface. See https://platform.openai.com/account/api-keys for details.
```

## Experiência do Usuário (UX)

Os princípios gerais de UX se aplicam aos aplicativos de chat. Porém, aqui estão algumas considerações adicionais que se tornam particularmente importantes devido aos componentes de aprendizado de máquina envolvidos.

- **Mecanismo para lidar com ambiguidade**: Modelos de IA generativa ocasionalmente geram respostas ambíguas. Uma funcionalidade que permite aos usuários solicitar esclarecimentos pode ser útil caso se deparem com esse problema.

- **Retenção de contexto**: Modelos avançados de IA generativa têm a capacidade de lembrar o contexto dentro de uma conversa, o que pode ser um ativo necessário para a experiência do usuário. Dar aos usuários a capacidade de controlar e gerenciar o contexto melhora a experiência do usuário, mas introduz o risco de retenção de informações sensíveis do usuário. Considerações sobre por quanto tempo essas informações são armazenadas, como a introdução de uma política de retenção, podem equilibrar a necessidade de contexto contra a privacidade.

- **Personalização**: Com a capacidade de aprender e se adaptar, os modelos de IA oferecem uma experiência individualizada para o usuário. Personalizar a experiência do usuário por meio de recursos como perfis de usuário não apenas faz com que o usuário se sinta compreendido, mas também auxilia na busca por respostas específicas, criando uma interação mais eficiente e satisfatória.

Um exemplo de personalização é o ajuste de "Instruções Personalizadas" no ChatGPT da OpenAI. Ele permite que você forneça informações sobre si mesmo que podem ser um contexto importante para seus prompts. Aqui está um exemplo de uma instrução personalizada.

![Custom Instructions Settings in ChatGPT](../../images/custom-instructions.png?WT.mc_id=academic-105485-koreyst)

Esse prompt "perfil" faz com que o ChatGPT crie um plano de aula sobre listas vinculadas. Observe que o ChatGPT leva em consideração que o usuário pode querer um plano de aula mais aprofundado com base em sua experiência.

![A prompt in ChatGPT for a lesson plan about linked lists](../../images/lesson-plan-prompt.png?WT.mc_id=academic-105485-koreyst)

### Estrutura de Mensagens do Sistema da Microsoft para Grandes Modelos de Linguagem

[Microsoft has provided guidance](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) para escrever mensagens de sistema eficazes ao gerar respostas de LLMs divididas em 4 áreas:

1. Definindo para quem o modelo se destina, assim como suas capacidades e limitações.
2. Definindo o formato de saída do modelo.
3. Fornecendo exemplos específicos que demonstrem o comportamento pretendido do modelo.
4. Estabelecendo barreiras comportamentais adicionais.

### Acessibilidade

Seja o usuário portador de deficiência visual, auditiva, motora ou cognitiva, uma aplicação de chat bem projetada deve ser utilizável por todos. A lista a seguir detalha características específicas destinadas a aprimorar a acessibilidade para várias deficiências de usuários.

- **Recursos para Deficiência Visual**: Temas de alto contraste e texto redimensionável, compatibilidade com leitores de tela.
- **Recursos para Deficiência Auditiva**: Funções de texto para fala e fala para texto, indicações visuais para notificações sonoras.
- **Recursos para Deficiência Motora**: Suporte à navegação por teclado, comandos de voz.
- **Recursos para Deficiência Cognitiva**: Opções de linguagem simplificada.

## Customização e Ajuste Fino para Modelos de Linguagem Específicos de Domínio

Imagine uma aplicação de chat que compreende o jargão da sua empresa e antecipa as consultas específicas que sua base de usuários comumente faz. Existem algumas abordagens que valem a pena mencionar:

- **Alavancar modelos DSL**. DSL significa linguagem específica de domínio. Você pode aproveitar um modelo chamado DSL treinado em um domínio específico para entender seus conceitos e cenários.
- **Aplicar ajuste fino**. O ajuste fino é o processo de treinar ainda mais seu modelo com dados específicos.

## Customização: Usando um DSL

Aproveitar modelos de linguagem específicos de domínio (Modelos DSL) pode aprimorar o engajamento do usuário ao fornecer interações especializadas e contextualmente relevantes. É um modelo treinado ou ajustado para entender e gerar texto relacionado a um campo, indústria ou assunto específico. As opções para usar um modelo DSL podem variar desde treiná-lo do zero até usar modelos pré-existentes por meio de SDKs e APIs. Outra opção é o ajuste fino, que envolve pegar um modelo pré-treinado existente e adaptá-lo para um domínio específico.

## Customização: Aplicar Ajuste Fino

O ajuste fino é frequentemente considerado quando um modelo pré-treinado não atende a um domínio especializado ou tarefa específica.

Por exemplo, consultas médicas são complexas e exigem muito contexto. Quando um profissional de saúde faz um diagnóstico, isso se baseia em uma variedade de fatores, como estilo de vida ou condições pré-existentes, e pode até depender de periódicos médicos recentes para validar o diagnóstico. Em cenários tão nuances, um aplicativo de chat de IA de propósito geral não pode ser uma fonte confiável.

### Cenário: um aplicativo médico

Considere um aplicativo de chat projetado para auxiliar profissionais de saúde, fornecendo referências rápidas a diretrizes de tratamento, interações medicamentosas ou descobertas recentes de pesquisas.

Um modelo de propósito geral pode ser adequado para responder a perguntas médicas básicas ou fornecer conselhos gerais, mas pode ter dificuldades com o seguinte:

- **Casos altamente específicos ou complexos**. Por exemplo, um neurologista pode perguntar ao aplicativo: "Quais são as melhores práticas atuais para o manejo da epilepsia resistente a medicamentos em pacientes pediátricos?"
- **Falta de avanços recentes**. Um modelo de propósito geral pode ter dificuldade em fornecer uma resposta atualizada que incorpore os avanços mais recentes em neurologia e farmacologia.

Em casos como esses, o ajuste fino do modelo com um conjunto de dados médicos especializados pode melhorar significativamente sua capacidade de lidar com essas consultas médicas intrincadas de maneira mais precisa e confiável. Isso requer acesso a um conjunto de dados grande e relevante que represente os desafios e perguntas específicos do domínio que precisam ser abordados.

## Considerações para uma Experiência de Chat Impulsionada por IA de Alta Qualidade

Esta seção delineia os critérios para aplicações de chat consideradas "de alta qualidade", que incluem a captura de métricas acionáveis e a adesão a um framework que utiliza de forma responsável a tecnologia de IA.

### Métricas-Chave

Para manter o desempenho de alta qualidade de uma aplicação, é essencial acompanhar métricas-chave e considerações. Essas medições não apenas garantem a funcionalidade da aplicação, mas também avaliam a qualidade do modelo de IA e a experiência do usuário. Abaixo está uma lista que abrange métricas básicas, de IA e de experiência do usuário a serem consideradas.

| Métrica                               | Definição                                                                                                       | Considerações para o Desenvolvedor de Chat                                                  |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Tempo de Atividade (Uptime)**       | Mede o tempo em que a aplicação está operacional e acessível pelos usuários.                                    | Como você irá minimizar o tempo de inatividade?                                             |
| **Tempo de Resposta**                 | O tempo que a aplicação leva para responder a uma consulta do usuário.                                          | Como você pode otimizar o processamento de consultas para melhorar o tempo de resposta?     |
| **Precisão**                          | A razão entre previsões verdadeiras positivas e o número total de previsões positivas.                          | Como você irá validar a precisão do seu modelo?                                             |
| **Revocação (Sensibilidade)**         | A razão entre previsões verdadeiras positivas e o número real de positivos.                                     | Como você irá medir e melhorar a revocação?                                                 |
| **Escore F1**                         | A média harmônica de precisão e revocação, que equilibra o compromisso entre ambos.                             | Qual é o seu Escore F1 alvo? Como você irá equilibrar precisão e revocação?                 |
| **Perplexidade**                      | Mede quão bem a distribuição de probabilidade prevista pelo modelo se alinha com a distribuição real dos dados. | Como você irá minimizar a perplexidade?                                                     |
| **Métricas de Satisfação do Usuário** | Mede a percepção do usuário em relação à aplicação. Frequentemente capturado por meio de pesquisas.             | Com que frequência você irá coletar feedback do usuário? Como você irá se adaptar a isso?   |
| **Taxa de Erro**                      | A taxa na qual o modelo comete erros na compreensão ou saída.                                                   | Quais estratégias você tem para reduzir as taxas de erro?                                   |
| **Ciclos de Retreinamento**           | A frequência com que o modelo é atualizado para incorporar novos dados e insights.                              | Com que frequência você irá retrainer o modelo? O que desencadeia um ciclo de retratamento? |
| **Detecção de Anomalias**             | Ferramentas e técnicas para identificar padrões incomuns que não seguem o comportamento esperado.               | Como você irá responder a anomalias?                                                        |
|  |

### Implementando Práticas de IA Responsável em Aplicações de Chat

A abordagem da Microsoft para a IA Responsável identificou seis princípios que devem orientar o desenvolvimento e uso de IA. Abaixo estão os princípios, suas definições e o que um desenvolvedor de chat deve considerar e por que deve levar isso a sério.

| Princípios                 | Definição pela Microsoft                                     | Considerações para o Desenvolvedor de Chat                                     | Por que é Importante                                                                                          |
| -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Justiça                    | Sistemas de IA devem tratar todas as pessoas de forma justa. | Garantir que a aplicação de chat não discrimine com base nos dados do usuário. | Construir confiança e inclusividade entre os usuários; evita ramificações legais.                             |
| Confiabilidade e Segurança | Sistemas de IA devem ter desempenho confiável e seguro.      | Implementar testes e mecanismos de segurança para minimizar erros e riscos.    | Garante satisfação do usuário e evita possíveis danos.                                                        |
| Privacidade e Segurança    | Sistemas de IA devem ser seguros e respeitar a privacidade.  | Implementar criptografia forte e medidas de proteção de dados.                 | Proteger dados sensíveis do usuário e cumprir leis de privacidade.                                            |
| Inclusividade              | Sistemas de IA devem capacitar todos e envolver as pessoas.  | Projetar uma interface acessível e fácil de usar para diversos públicos.       | Garante que uma variedade maior de pessoas possa usar a aplicação de forma eficaz.                            |
| Transparência              | Sistemas de IA devem ser compreensíveis.                     | Fornecer documentação clara e justificativa para as respostas da IA.           | Os usuários têm mais probabilidade de confiar em um sistema se puderem entender como são tomadas as decisões. |
| Responsabilidade           | As pessoas devem ser responsáveis pelos sistemas de IA.      | Estabelecer um processo claro para auditoria e melhoria das decisões de IA.    | Possibilita melhorias contínuas e medidas corretivas em caso de erros.                                        |

## Tarefa

Veja a [tarefa](../../python?WT.mc_id=academic-105485-koreyst) que o levará por uma série de exercícios, desde a execução de seus primeiros prompts de chat até a classificação e resumo de texto e muito mais.

## Excelente Trabalho! Continue no Aprendizado!

Depois de concluir esta lição, confira nossa [coleção de aprendizado de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar seus conhecimentos sobre IA generativa!

Agora, vamos seguir para a Lição 8 para ver como você pode começar a [criar aplicativos de pesquisa](../../../08-building-search-applications/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)!
