<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T22:38:37+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "pt"
}
-->
# Protegendo Suas Aplicações de IA Generativa

## Introdução

Esta lição abordará:

- Segurança no contexto de sistemas de IA.
- Riscos e ameaças comuns aos sistemas de IA.
- Métodos e considerações para proteger sistemas de IA.

## Objetivos de Aprendizagem

Após completar esta lição, você entenderá:

- As ameaças e riscos aos sistemas de IA.
- Métodos e práticas comuns para proteger sistemas de IA.
- Como a implementação de testes de segurança pode prevenir resultados inesperados e a perda de confiança dos usuários.

## O que significa segurança no contexto da IA generativa?

À medida que as tecnologias de Inteligência Artificial (IA) e Aprendizado de Máquina (ML) moldam cada vez mais nossas vidas, é crucial proteger não apenas os dados dos clientes, mas também os próprios sistemas de IA. IA/ML é cada vez mais utilizada em processos de tomada de decisão de alto valor em indústrias onde uma decisão errada pode resultar em consequências graves.

Aqui estão pontos-chave a serem considerados:

- **Impacto da IA/ML**: IA/ML têm impactos significativos na vida diária e, como tal, protegê-los tornou-se essencial.
- **Desafios de Segurança**: Este impacto que a IA/ML tem precisa de atenção adequada para abordar a necessidade de proteger produtos baseados em IA de ataques sofisticados, seja por trolls ou grupos organizados.
- **Problemas Estratégicos**: A indústria de tecnologia deve abordar proativamente desafios estratégicos para garantir a segurança a longo prazo dos clientes e a segurança dos dados.

Além disso, modelos de Aprendizado de Máquina são em grande parte incapazes de discernir entre entradas maliciosas e dados anômalos benignos. Uma fonte significativa de dados de treinamento é derivada de conjuntos de dados públicos não curados e não moderados, que estão abertos a contribuições de terceiros. Os atacantes não precisam comprometer conjuntos de dados quando são livres para contribuir com eles. Com o tempo, dados maliciosos de baixa confiança tornam-se dados confiáveis de alta confiança, se a estrutura/formatação dos dados permanecer correta.

É por isso que é crítico garantir a integridade e proteção dos repositórios de dados que seus modelos usam para tomar decisões.

## Entendendo as ameaças e riscos da IA

Em termos de IA e sistemas relacionados, o envenenamento de dados destaca-se como a ameaça de segurança mais significativa hoje. O envenenamento de dados ocorre quando alguém intencionalmente altera as informações usadas para treinar uma IA, fazendo com que ela cometa erros. Isso se deve à ausência de métodos padronizados de detecção e mitigação, juntamente com nossa dependência de conjuntos de dados públicos não confiáveis ou não curados para treinamento. Para manter a integridade dos dados e prevenir um processo de treinamento falho, é crucial rastrear a origem e a linhagem dos seus dados. Caso contrário, o velho ditado "lixo entra, lixo sai" se aplica, levando a um desempenho comprometido do modelo.

Aqui estão exemplos de como o envenenamento de dados pode afetar seus modelos:

1. **Inversão de Rótulos**: Em uma tarefa de classificação binária, um adversário inverte intencionalmente os rótulos de um pequeno subconjunto de dados de treinamento. Por exemplo, amostras benignas são rotuladas como maliciosas, levando o modelo a aprender associações incorretas.\
   **Exemplo**: Um filtro de spam classificando erroneamente e-mails legítimos como spam devido a rótulos manipulados.
2. **Envenenamento de Características**: Um atacante modifica sutilmente características nos dados de treinamento para introduzir viés ou enganar o modelo.\
   **Exemplo**: Adicionar palavras-chave irrelevantes às descrições de produtos para manipular sistemas de recomendação.
3. **Injeção de Dados**: Injetar dados maliciosos no conjunto de treinamento para influenciar o comportamento do modelo.\
   **Exemplo**: Introduzir avaliações falsas de usuários para distorcer os resultados da análise de sentimentos.
4. **Ataques de Backdoor**: Um adversário insere um padrão oculto (backdoor) nos dados de treinamento. O modelo aprende a reconhecer esse padrão e se comporta maliciosamente quando ativado.\
   **Exemplo**: Um sistema de reconhecimento facial treinado com imagens com backdoor que identifica erroneamente uma pessoa específica.

A MITRE Corporation criou o [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), um banco de dados de táticas e técnicas empregadas por adversários em ataques reais a sistemas de IA.

> Há um número crescente de vulnerabilidades em sistemas habilitados para IA, à medida que a incorporação de IA aumenta a superfície de ataque de sistemas existentes além dos ataques cibernéticos tradicionais. Desenvolvemos o ATLAS para aumentar a conscientização sobre essas vulnerabilidades únicas e em evolução, à medida que a comunidade global incorpora cada vez mais IA em vários sistemas. O ATLAS é modelado após o framework MITRE ATT&CK® e suas táticas, técnicas e procedimentos (TTPs) são complementares aos do ATT&CK.

Muito parecido com o framework MITRE ATT&CK®, que é amplamente utilizado em segurança cibernética tradicional para planejar cenários avançados de emulação de ameaças, o ATLAS fornece um conjunto de TTPs facilmente pesquisável que pode ajudar a entender melhor e se preparar para defender contra ataques emergentes.

Além disso, o Open Web Application Security Project (OWASP) criou uma "[lista dos 10 principais](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" das vulnerabilidades mais críticas encontradas em aplicações que utilizam LLMs. A lista destaca os riscos de ameaças como o envenenamento de dados mencionado anteriormente, juntamente com outros, como:

- **Injeção de Prompt**: uma técnica em que atacantes manipulam um Modelo de Linguagem Grande (LLM) através de entradas cuidadosamente elaboradas, fazendo com que ele se comporte fora do comportamento pretendido.
- **Vulnerabilidades na Cadeia de Suprimentos**: Os componentes e softwares que compõem as aplicações usadas por um LLM, como módulos Python ou conjuntos de dados externos, podem ser comprometidos, levando a resultados inesperados, introdução de vieses e até mesmo vulnerabilidades na infraestrutura subjacente.
- **Dependência Excessiva**: LLMs são falíveis e têm tendência a alucinar, fornecendo resultados imprecisos ou inseguros. Em várias circunstâncias documentadas, pessoas aceitaram os resultados como verdadeiros, levando a consequências negativas não intencionais no mundo real.

O Microsoft Cloud Advocate Rod Trent escreveu um ebook gratuito, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), que aprofunda essas e outras ameaças emergentes de IA e fornece orientações extensivas sobre como melhor lidar com esses cenários.

## Testes de Segurança para Sistemas de IA e LLMs

A inteligência artificial (IA) está transformando vários domínios e indústrias, oferecendo novas possibilidades e benefícios para a sociedade. No entanto, a IA também apresenta desafios e riscos significativos, como privacidade de dados, viés, falta de explicabilidade e uso indevido potencial. Portanto, é crucial garantir que os sistemas de IA sejam seguros e responsáveis, ou seja, que adiram a padrões éticos e legais e possam ser confiáveis por usuários e partes interessadas.

O teste de segurança é o processo de avaliar a segurança de um sistema de IA ou LLM, identificando e explorando suas vulnerabilidades. Isso pode ser realizado por desenvolvedores, usuários ou auditores terceirizados, dependendo do propósito e escopo do teste. Alguns dos métodos de teste de segurança mais comuns para sistemas de IA e LLMs são:

- **Sanitização de Dados**: Este é o processo de remover ou anonimizar informações sensíveis ou privadas dos dados de treinamento ou da entrada de um sistema de IA ou LLM. A sanitização de dados pode ajudar a prevenir vazamento de dados e manipulação maliciosa, reduzindo a exposição de dados confidenciais ou pessoais.
- **Teste Adversário**: Este é o processo de gerar e aplicar exemplos adversários à entrada ou saída de um sistema de IA ou LLM para avaliar sua robustez e resiliência contra ataques adversários. O teste adversário pode ajudar a identificar e mitigar as vulnerabilidades e fraquezas de um sistema de IA ou LLM que podem ser exploradas por atacantes.
- **Verificação de Modelo**: Este é o processo de verificar a correção e a completude dos parâmetros do modelo ou da arquitetura de um sistema de IA ou LLM. A verificação de modelo pode ajudar a detectar e prevenir o roubo de modelos, garantindo que o modelo esteja protegido e autenticado.
- **Validação de Saída**: Este é o processo de validar a qualidade e a confiabilidade da saída de um sistema de IA ou LLM. A validação de saída pode ajudar a detectar e corrigir manipulações maliciosas, garantindo que a saída seja consistente e precisa.

A OpenAI, líder em sistemas de IA, configurou uma série de _avaliações de segurança_ como parte de sua iniciativa de rede de equipe vermelha, destinada a testar a saída de sistemas de IA na esperança de contribuir para a segurança da IA.

> As avaliações podem variar de testes simples de perguntas e respostas a simulações mais complexas. Como exemplos concretos, aqui estão avaliações de amostra desenvolvidas pela OpenAI para avaliar comportamentos de IA de várias perspectivas:

#### Persuasão

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode enganar outro sistema de IA para dizer uma palavra secreta?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode convencer outro sistema de IA a doar dinheiro?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode influenciar o apoio de outro sistema de IA a uma proposta política?

#### Esteganografia (mensagens ocultas)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode passar mensagens secretas sem ser pego por outro sistema de IA?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode comprimir e descomprimir mensagens para permitir a ocultação de mensagens secretas?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode coordenar-se com outro sistema de IA, sem comunicação direta?

### Segurança da IA

É imperativo que visemos proteger sistemas de IA de ataques maliciosos, uso indevido ou consequências não intencionais. Isso inclui tomar medidas para garantir a segurança, confiabilidade e confiança dos sistemas de IA, tais como:

- Proteger os dados e algoritmos usados para treinar e executar modelos de IA
- Prevenir acesso não autorizado, manipulação ou sabotagem de sistemas de IA
- Detectar e mitigar viés, discriminação ou questões éticas em sistemas de IA
- Garantir a responsabilidade, transparência e explicabilidade das decisões e ações da IA
- Alinhar os objetivos e valores dos sistemas de IA com os dos humanos e da sociedade

A segurança da IA é importante para garantir a integridade, disponibilidade e confidencialidade dos sistemas e dados de IA. Alguns dos desafios e oportunidades da segurança da IA são:

- Oportunidade: Incorporar a IA em estratégias de cibersegurança, pois ela pode desempenhar um papel crucial na identificação de ameaças e melhoria dos tempos de resposta. A IA pode ajudar a automatizar e aumentar a detecção e mitigação de ataques cibernéticos, como phishing, malware ou ransomware.
- Desafio: A IA também pode ser usada por adversários para lançar ataques sofisticados, como gerar conteúdo falso ou enganoso, personificar usuários ou explorar vulnerabilidades em sistemas de IA. Portanto, os desenvolvedores de IA têm uma responsabilidade única de projetar sistemas que sejam robustos e resilientes contra uso indevido.

### Proteção de Dados

LLMs podem representar riscos à privacidade e segurança dos dados que utilizam. Por exemplo, LLMs podem potencialmente memorizar e vazar informações sensíveis de seus dados de treinamento, como nomes pessoais, endereços, senhas ou números de cartão de crédito. Eles também podem ser manipulados ou atacados por atores maliciosos que desejam explorar suas vulnerabilidades ou vieses. Portanto, é importante estar ciente desses riscos e tomar medidas adequadas para proteger os dados usados com LLMs. Existem várias etapas que você pode seguir para proteger os dados usados com LLMs. Essas etapas incluem:

- **Limitar a quantidade e o tipo de dados que compartilham com LLMs**: Compartilhe apenas os dados que são necessários e relevantes para os propósitos pretendidos e evite compartilhar qualquer dado que seja sensível, confidencial ou pessoal. Os usuários também devem anonimizar ou criptografar os dados que compartilham com LLMs, como removendo ou mascarando qualquer informação identificável ou usando canais de comunicação seguros.
- **Verificar os dados que LLMs geram**: Sempre verifique a precisão e qualidade da saída gerada por LLMs para garantir que não contenham informações indesejadas ou inadequadas.
- **Relatar e alertar sobre qualquer violação de dados ou incidentes**: Esteja atento a quaisquer atividades ou comportamentos suspeitos ou anormais de LLMs, como gerar textos que sejam irrelevantes, imprecisos, ofensivos ou prejudiciais. Isso pode ser um indicativo de uma violação de dados ou incidente de segurança.

Segurança de dados, governança e conformidade são críticas para qualquer organização que deseja aproveitar o poder dos dados e da IA em um ambiente de múltiplas nuvens. Proteger e governar todos os seus dados é uma tarefa complexa e multifacetada. Você precisa proteger e governar diferentes tipos de dados (estruturados, não estruturados e dados gerados por IA) em diferentes locais em várias nuvens, e precisa considerar as regulamentações de segurança de dados, governança e IA existentes e futuras. Para proteger seus dados, você precisa adotar algumas práticas recomendadas e precauções, como:

- Usar serviços ou plataformas de nuvem que ofereçam recursos de proteção e privacidade de dados.
- Usar ferramentas de qualidade e validação de dados para verificar seus dados em busca de erros, inconsistências ou anomalias.
- Usar frameworks de governança e ética de dados para garantir que seus dados sejam usados de maneira responsável e transparente.

### Emulando ameaças do mundo real - equipe vermelha de IA

Emular ameaças do mundo real é agora considerado uma prática padrão na construção de sistemas de IA resilientes, empregando ferramentas, táticas e procedimentos semelhantes para identificar os riscos aos sistemas e testar a resposta dos defensores.

> A prática de equipe vermelha de IA evoluiu para assumir um significado mais expandido: ela não cobre apenas a busca por vulnerabilidades de segurança, mas também inclui a busca por outras falhas do sistema, como a geração de conteúdo potencialmente prejudicial. Os sistemas de IA vêm com novos riscos, e a equipe vermelha é fundamental para entender esses riscos novos, como a injeção de prompt e a produção de conteúdo sem fundamento. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

Abaixo estão insights-chave que moldaram o programa de equipe vermelha de IA da Microsoft.

1. **Escopo Expansivo da Equipe Vermelha de IA:**
   A equipe vermelha de IA agora abrange tanto resultados de segurança quanto de IA Responsável (RAI). Tradicionalmente, a equipe vermelha focava em aspectos de segurança, tratando o modelo como um vetor (por exemplo, roubo do modelo subjacente). No entanto, sistemas de IA introduzem vulnerabilidades de segurança novas (por exemplo, injeção de prompt, envenenamento), necessitando de atenção especial. Além da segurança, a equipe vermelha de IA também investiga questões de equidade (por exemplo, estereótipos) e conteúdo prejudicial (por exemplo, glorificação da violência). A identificação precoce dessas questões permite a priorização de investimentos em defesa.
2. **Falhas Maliciosas e Benignas:**
   A equipe vermelha de IA considera falhas de perspectivas tanto maliciosas quanto benignas. Por exemplo, ao testar o novo Bing, exploramos não apenas como adversários maliciosos podem subverter o sistema, mas também como usuários regulares podem encontrar conteúdo problemático ou prejudicial. Ao contrário da equipe vermelha de segurança tradicional, que foca principalmente em atores maliciosos, a equipe vermelha de IA leva em conta uma gama mais ampla de personas e falhas potenciais.
3. **Natureza Dinâmica dos Sistemas de IA:**
   Aplicações de IA estão em constante evolução. Em aplicações de modelos de linguagem grande, os desenvolvedores se adaptam a requisitos em mudança. A equipe vermelha contínua garante vigilância e adaptação contínuas aos riscos em evolução.

A equipe vermelha de IA não é abrangente e deve ser considerada uma ação complementar a controles adicionais, como [controle de acesso baseado em função (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) e soluções abrangentes de gerenciamento de dados. Ela é destinada a complementar uma estratégia de segurança que se concentra em empregar soluções de IA seguras e responsáveis que consideram privacidade e segurança, enquanto aspiram a minimizar vieses, conteúdo prejudicial e desinformação que podem minar a confiança do usuário.

Aqui está uma lista de leituras adicionais que podem ajudá-lo a entender melhor como a equipe vermelha pode ajudar a identificar e mitigar riscos em seus sistemas de IA:

- [Planejamento de equipe vermelha para modelos de linguagem grande (LLMs) e suas aplicações](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [O que é a Rede de Equipe Vermelha da OpenAI?](

**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, é recomendada a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.