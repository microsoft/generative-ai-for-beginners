<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5308963a56cfbad2d73b0fa99fe84b3",
  "translation_date": "2025-10-18T00:46:16+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "br"
}
-->
# Construindo Aplicativos de Chat com IA Generativa

[![Construindo Aplicativos de Chat com IA Generativa](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.br.png)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

Agora que vimos como podemos construir aplicativos de geração de texto, vamos explorar os aplicativos de chat.

Os aplicativos de chat tornaram-se parte integrante de nossas vidas diárias, oferecendo mais do que apenas um meio de conversa casual. Eles são partes essenciais do atendimento ao cliente, suporte técnico e até mesmo sistemas de consultoria sofisticados. É provável que você tenha recebido ajuda de um aplicativo de chat recentemente. À medida que integramos tecnologias mais avançadas, como IA generativa, a complexidade aumenta, assim como os desafios.

Algumas perguntas que precisamos responder são:

- **Construção do aplicativo**. Como podemos construir e integrar de forma eficiente esses aplicativos com IA para casos de uso específicos?
- **Monitoramento**. Uma vez implantados, como podemos monitorar e garantir que os aplicativos estejam operando no mais alto nível de qualidade, tanto em termos de funcionalidade quanto de conformidade com os [seis princípios de IA responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

À medida que avançamos em uma era definida pela automação e interações perfeitas entre humanos e máquinas, entender como a IA generativa transforma o escopo, a profundidade e a adaptabilidade dos aplicativos de chat torna-se essencial. Esta lição investigará os aspectos da arquitetura que sustentam esses sistemas complexos, explorará as metodologias para ajustá-los a tarefas específicas de domínio e avaliará as métricas e considerações pertinentes para garantir a implantação responsável da IA.

## Introdução

Esta lição aborda:

- Técnicas para construir e integrar aplicativos de chat de forma eficiente.
- Como aplicar personalização e ajustes aos aplicativos.
- Estratégias e considerações para monitorar efetivamente os aplicativos de chat.

## Objetivos de Aprendizado

Ao final desta lição, você será capaz de:

- Descrever considerações para construir e integrar aplicativos de chat em sistemas existentes.
- Personalizar aplicativos de chat para casos de uso específicos.
- Identificar métricas-chave e considerações para monitorar e manter a qualidade dos aplicativos de chat com IA.
- Garantir que os aplicativos de chat utilizem a IA de forma responsável.

## Integrando IA Generativa em Aplicativos de Chat

Elevar os aplicativos de chat por meio da IA generativa não se trata apenas de torná-los mais inteligentes; é sobre otimizar sua arquitetura, desempenho e interface do usuário para oferecer uma experiência de qualidade. Isso envolve investigar os fundamentos arquitetônicos, integrações de API e considerações de interface do usuário. Esta seção tem como objetivo oferecer um roteiro abrangente para navegar nesses cenários complexos, seja integrando-os a sistemas existentes ou construindo-os como plataformas independentes.

Ao final desta seção, você estará equipado com o conhecimento necessário para construir e incorporar aplicativos de chat de forma eficiente.

### Chatbot ou Aplicativo de Chat?

Antes de mergulharmos na construção de aplicativos de chat, vamos comparar 'chatbots' com 'aplicativos de chat com IA', que possuem papéis e funcionalidades distintas. O principal objetivo de um chatbot é automatizar tarefas específicas de conversação, como responder perguntas frequentes ou rastrear um pacote. Ele geralmente é governado por lógica baseada em regras ou algoritmos de IA complexos. Em contraste, um aplicativo de chat com IA é um ambiente muito mais amplo, projetado para facilitar várias formas de comunicação digital, como texto, voz e vídeo entre usuários humanos. Sua característica definidora é a integração de um modelo de IA generativa que simula conversas humanas detalhadas, gerando respostas com base em uma ampla variedade de entradas e pistas contextuais. Um aplicativo de chat com IA generativa pode engajar-se em discussões de domínio aberto, adaptar-se a contextos conversacionais em evolução e até mesmo produzir diálogos criativos ou complexos.

A tabela abaixo descreve as principais diferenças e semelhanças para nos ajudar a entender seus papéis únicos na comunicação digital.

| Chatbot                               | Aplicativo de Chat com IA Generativa   |
| ------------------------------------- | -------------------------------------- |
| Focado em tarefas e baseado em regras | Consciente do contexto                 |
| Frequentemente integrado a sistemas maiores | Pode hospedar um ou vários chatbots    |
| Limitado a funções programadas        | Incorpora modelos de IA generativa     |
| Interações especializadas e estruturadas | Capaz de discussões de domínio aberto  |

### Aproveitando funcionalidades pré-construídas com SDKs e APIs

Ao construir um aplicativo de chat, um ótimo primeiro passo é avaliar o que já está disponível. Usar SDKs e APIs para construir aplicativos de chat é uma estratégia vantajosa por vários motivos. Ao integrar SDKs e APIs bem documentados, você posiciona estrategicamente seu aplicativo para o sucesso a longo prazo, abordando preocupações de escalabilidade e manutenção.

- **Acelera o processo de desenvolvimento e reduz custos**: Confiar em funcionalidades pré-construídas em vez do processo caro de construí-las você mesmo permite que você se concentre em outros aspectos do seu aplicativo que podem ser mais importantes, como lógica de negócios.
- **Melhor desempenho**: Ao construir funcionalidades do zero, você eventualmente se perguntará "Como isso escala? Este aplicativo é capaz de lidar com um influxo repentino de usuários?" SDKs e APIs bem mantidos frequentemente têm soluções integradas para essas preocupações.
- **Manutenção mais fácil**: Atualizações e melhorias são mais fáceis de gerenciar, já que a maioria das APIs e SDKs simplesmente requer uma atualização na biblioteca quando uma nova versão é lançada.
- **Acesso à tecnologia de ponta**: Aproveitar modelos que foram ajustados e treinados em extensos conjuntos de dados fornece ao seu aplicativo capacidades de linguagem natural.

Acessar a funcionalidade de um SDK ou API geralmente envolve obter permissão para usar os serviços fornecidos, o que geralmente é feito por meio do uso de uma chave única ou token de autenticação. Usaremos a Biblioteca Python do OpenAI para explorar como isso funciona. Você também pode experimentar por conta própria no seguinte [notebook para OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) ou [notebook para Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) desta lição.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

O exemplo acima usa o modelo GPT-3.5 Turbo para completar o prompt, mas observe que a chave da API é configurada antes de fazer isso. Você receberia um erro se não configurasse a chave.

## Experiência do Usuário (UX)

Princípios gerais de UX se aplicam a aplicativos de chat, mas aqui estão algumas considerações adicionais que se tornam particularmente importantes devido aos componentes de aprendizado de máquina envolvidos.

- **Mecanismo para lidar com ambiguidades**: Modelos de IA generativa ocasionalmente geram respostas ambíguas. Um recurso que permite aos usuários pedir esclarecimentos pode ser útil caso encontrem esse problema.
- **Retenção de contexto**: Modelos avançados de IA generativa têm a capacidade de lembrar o contexto dentro de uma conversa, o que pode ser um ativo necessário para a experiência do usuário. Dar aos usuários a capacidade de controlar e gerenciar o contexto melhora a experiência do usuário, mas introduz o risco de reter informações sensíveis do usuário. Considerações sobre quanto tempo essas informações são armazenadas, como a introdução de uma política de retenção, podem equilibrar a necessidade de contexto com a privacidade.
- **Personalização**: Com a capacidade de aprender e se adaptar, os modelos de IA oferecem uma experiência individualizada para o usuário. Personalizar a experiência do usuário por meio de recursos como perfis de usuário não apenas faz o usuário se sentir compreendido, mas também ajuda em sua busca por respostas específicas, criando uma interação mais eficiente e satisfatória.

Um exemplo de personalização é a configuração de "Instruções Personalizadas" no ChatGPT da OpenAI. Isso permite que você forneça informações sobre si mesmo que podem ser um contexto importante para seus prompts. Aqui está um exemplo de uma instrução personalizada.

![Configurações de Instruções Personalizadas no ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.br.png)

Este "perfil" solicita ao ChatGPT que crie um plano de aula sobre listas ligadas. Observe que o ChatGPT leva em conta que o usuário pode querer um plano de aula mais detalhado com base em sua experiência.

![Um prompt no ChatGPT para um plano de aula sobre listas ligadas](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.br.png)

### Framework de Mensagem de Sistema da Microsoft para Modelos de Linguagem Extensa

[A Microsoft forneceu orientações](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) para escrever mensagens de sistema eficazes ao gerar respostas de LLMs, divididas em 4 áreas:

1. Definir para quem o modelo é destinado, bem como suas capacidades e limitações.
2. Definir o formato de saída do modelo.
3. Fornecer exemplos específicos que demonstrem o comportamento pretendido do modelo.
4. Fornecer diretrizes adicionais de comportamento.

### Acessibilidade

Seja um usuário com deficiência visual, auditiva, motora ou cognitiva, um aplicativo de chat bem projetado deve ser utilizável por todos. A lista a seguir divide recursos específicos destinados a melhorar a acessibilidade para várias deficiências dos usuários.

- **Recursos para Deficiência Visual**: Temas de alto contraste e texto redimensionável, compatibilidade com leitores de tela.
- **Recursos para Deficiência Auditiva**: Funções de texto para fala e fala para texto, sinais visuais para notificações de áudio.
- **Recursos para Deficiência Motora**: Suporte para navegação por teclado, comandos de voz.
- **Recursos para Deficiência Cognitiva**: Opções de linguagem simplificada.

## Personalização e Ajuste para Modelos de Linguagem Específicos de Domínio

Imagine um aplicativo de chat que entende o jargão da sua empresa e antecipa as consultas específicas que sua base de usuários geralmente tem. Existem algumas abordagens que valem a pena mencionar:

- **Aproveitar modelos DSL**. DSL significa linguagem específica de domínio. Você pode aproveitar um modelo DSL treinado em um domínio específico para entender seus conceitos e cenários.
- **Aplicar ajuste fino**. O ajuste fino é o processo de treinar ainda mais seu modelo com dados específicos.

## Personalização: Usando um DSL

Aproveitar modelos de linguagem específicos de domínio (Modelos DSL) pode melhorar o engajamento do usuário ao fornecer interações especializadas e contextualmente relevantes. É um modelo que é treinado ou ajustado para entender e gerar texto relacionado a um campo, indústria ou assunto específico. As opções para usar um modelo DSL podem variar desde treinar um do zero até usar modelos pré-existentes por meio de SDKs e APIs. Outra opção é o ajuste fino, que envolve pegar um modelo pré-treinado existente e adaptá-lo para um domínio específico.

## Personalização: Aplicar ajuste fino

O ajuste fino é frequentemente considerado quando um modelo pré-treinado não atende às necessidades de um domínio especializado ou tarefa específica.

Por exemplo, consultas médicas são complexas e exigem muito contexto. Quando um profissional médico diagnostica um paciente, isso é baseado em uma variedade de fatores, como estilo de vida ou condições pré-existentes, e pode até depender de revistas médicas recentes para validar seu diagnóstico. Em cenários tão detalhados, um aplicativo de chat com IA de propósito geral não pode ser uma fonte confiável.

### Cenário: um aplicativo médico

Considere um aplicativo de chat projetado para ajudar profissionais médicos fornecendo referências rápidas a diretrizes de tratamento, interações medicamentosas ou descobertas de pesquisas recentes.

Um modelo de propósito geral pode ser adequado para responder a perguntas médicas básicas ou fornecer conselhos gerais, mas pode ter dificuldades com o seguinte:

- **Casos altamente específicos ou complexos**. Por exemplo, um neurologista pode perguntar ao aplicativo: "Quais são as melhores práticas atuais para gerenciar epilepsia resistente a medicamentos em pacientes pediátricos?"
- **Falta de avanços recentes**. Um modelo de propósito geral pode ter dificuldades para fornecer uma resposta atual que incorpore os avanços mais recentes em neurologia e farmacologia.

Em casos como esses, ajustar o modelo com um conjunto de dados médicos especializado pode melhorar significativamente sua capacidade de lidar com essas consultas médicas complexas de forma mais precisa e confiável. Isso requer acesso a um conjunto de dados grande e relevante que represente os desafios e perguntas específicas do domínio que precisam ser abordados.

## Considerações para uma Experiência de Chat com IA de Alta Qualidade

Esta seção descreve os critérios para aplicativos de chat "de alta qualidade", que incluem a captura de métricas acionáveis e a adesão a um framework que utiliza a tecnologia de IA de forma responsável.

### Métricas-Chave

Para manter o desempenho de alta qualidade de um aplicativo, é essencial acompanhar métricas e considerações-chave. Essas medições não apenas garantem a funcionalidade do aplicativo, mas também avaliam a qualidade do modelo de IA e a experiência do usuário. Abaixo está uma lista que cobre métricas básicas, de IA e de experiência do usuário a serem consideradas.

| Métrica                      | Definição                                                                                   | Considerações para o Desenvolvedor de Chat                                |
| ---------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| **Tempo de Atividade**       | Mede o tempo em que o aplicativo está operacional e acessível pelos usuários.              | Como você minimizará o tempo de inatividade?                              |
| **Tempo de Resposta**        | O tempo que o aplicativo leva para responder à consulta de um usuário.                     | Como você pode otimizar o processamento de consultas para melhorar o tempo de resposta? |
| **Precisão**                 | A proporção de previsões verdadeiras positivas em relação ao número total de previsões positivas. | Como você validará a precisão do seu modelo?                              |
| **Recall (Sensibilidade)**   | A proporção de previsões verdadeiras positivas em relação ao número real de positivos.      | Como você medirá e melhorará o recall?                                    |
| **Pontuação F1**             | A média harmônica de precisão e recall, que equilibra o trade-off entre ambos.             | Qual é sua pontuação F1 alvo? Como você equilibrará precisão e recall?    |
| **Perplexidade**             | Mede o quão bem a distribuição de probabilidade prevista pelo modelo se alinha com a distribuição real dos dados. | Como você minimizará a perplexidade?                                      |
| **Métricas de Satisfação do Usuário** | Mede a percepção do usuário sobre o aplicativo. Frequentemente capturada por meio de pesquisas. | Com que frequência você coletará feedback dos usuários? Como você se adaptará com base nele? |
| **Taxa de Erro**             | A taxa na qual o modelo comete erros na compreensão ou saída.                              | Quais estratégias você tem em mente para reduzir as taxas de erro?        |
| **Ciclos de Re-treinamento** | A frequência com que o modelo é atualizado para incorporar novos dados e insights.         | Com que frequência você re-treinará o modelo? O que desencadeia um ciclo de re-treinamento? |
| **Detecção de Anomalias**     | Ferramentas e técnicas para identificar padrões incomuns que não correspondem ao comportamento esperado.                | Como você responderá às anomalias?                                         |

### Implementando Práticas de IA Responsável em Aplicativos de Chat

A abordagem da Microsoft para IA Responsável identificou seis princípios que devem orientar o desenvolvimento e uso da IA. Abaixo estão os princípios, suas definições e o que um desenvolvedor de chat deve considerar, além de por que eles são importantes.

| Princípios             | Definição da Microsoft                                | Considerações para o Desenvolvedor de Chat                              | Por que é importante                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Justiça                | Sistemas de IA devem tratar todas as pessoas de forma justa. | Certifique-se de que o aplicativo de chat não discrimine com base nos dados do usuário. | Para construir confiança e inclusão entre os usuários; evita implicações legais.        |
| Confiabilidade e Segurança | Sistemas de IA devem funcionar de forma confiável e segura. | Implemente testes e mecanismos de segurança para minimizar erros e riscos. | Garante a satisfação do usuário e previne possíveis danos.                              |
| Privacidade e Segurança | Sistemas de IA devem ser seguros e respeitar a privacidade. | Implemente medidas robustas de criptografia e proteção de dados.       | Para proteger dados sensíveis dos usuários e cumprir as leis de privacidade.            |
| Inclusão               | Sistemas de IA devem capacitar todos e engajar as pessoas. | Projete interfaces (UI/UX) acessíveis e fáceis de usar para públicos diversos. | Garante que uma ampla gama de pessoas possa usar o aplicativo de forma eficaz.          |
| Transparência          | Sistemas de IA devem ser compreensíveis.              | Forneça documentação clara e explicações para as respostas da IA.      | Os usuários têm mais probabilidade de confiar em um sistema se entenderem como as decisões são tomadas. |
| Responsabilidade       | As pessoas devem ser responsáveis pelos sistemas de IA. | Estabeleça um processo claro para auditar e melhorar as decisões da IA. | Permite melhorias contínuas e medidas corretivas em caso de erros.                      |

## Tarefa

Veja [tarefa](../../../07-building-chat-applications/python). Ela o levará por uma série de exercícios, desde executar seus primeiros prompts de chat até classificar e resumir textos e muito mais. Observe que as tarefas estão disponíveis em diferentes linguagens de programação!

## Ótimo Trabalho! Continue a Jornada

Após concluir esta lição, confira nossa [coleção de aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Vá para a Lição 8 para ver como você pode começar [a construir aplicativos de busca](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.