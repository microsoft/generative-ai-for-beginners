<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:07:52+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "pt"
}
-->
# Protegendo as Suas Aplicações de IA Generativa

[![Protegendo as Suas Aplicações de IA Generativa](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.pt.png)](https://aka.ms/gen-ai-lesson13-gh?WT.mc_id=academic-105485-koreyst)

## Introdução

Esta lição abordará:

- Segurança no contexto de sistemas de IA.
- Riscos e ameaças comuns aos sistemas de IA.
- Métodos e considerações para proteger sistemas de IA.

## Objetivos de Aprendizagem

Após completar esta lição, você terá um entendimento de:

- As ameaças e riscos aos sistemas de IA.
- Métodos e práticas comuns para proteger sistemas de IA.
- Como a implementação de testes de segurança pode prevenir resultados inesperados e a erosão da confiança do usuário.

## O que significa segurança no contexto da IA generativa?

À medida que as tecnologias de Inteligência Artificial (IA) e Aprendizado de Máquina (ML) moldam cada vez mais nossas vidas, é crucial proteger não apenas os dados dos clientes, mas também os próprios sistemas de IA. IA/ML são cada vez mais usados para apoiar processos de tomada de decisão de alto valor em indústrias onde uma decisão errada pode resultar em consequências sérias.

Aqui estão pontos-chave a considerar:

- **Impacto da IA/ML**: IA/ML têm impactos significativos na vida diária e, como tal, protegê-los tornou-se essencial.
- **Desafios de Segurança**: Esse impacto que a IA/ML tem requer a devida atenção para abordar a necessidade de proteger produtos baseados em IA de ataques sofisticados, sejam eles de trolls ou grupos organizados.
- **Problemas Estratégicos**: A indústria tecnológica deve abordar proativamente desafios estratégicos para garantir a segurança a longo prazo dos clientes e a segurança dos dados.

Além disso, os modelos de Aprendizado de Máquina são amplamente incapazes de discernir entre entrada maliciosa e dados anômalos benignos. Uma fonte significativa de dados de treinamento é derivada de conjuntos de dados públicos não curados e não moderados, que estão abertos a contribuições de terceiros. Os atacantes não precisam comprometer conjuntos de dados quando têm a liberdade de contribuir para eles. Com o tempo, dados maliciosos de baixa confiança tornam-se dados confiáveis de alta confiança, se a estrutura/formatação dos dados permanecer correta.

É por isso que é crítico garantir a integridade e proteção dos armazenamentos de dados que seus modelos usam para tomar decisões.

## Compreendendo as ameaças e riscos da IA

Em termos de IA e sistemas relacionados, o envenenamento de dados destaca-se como a ameaça de segurança mais significativa hoje. O envenenamento de dados ocorre quando alguém altera intencionalmente as informações usadas para treinar uma IA, fazendo com que ela cometa erros. Isso se deve à ausência de métodos padronizados de detecção e mitigação, juntamente com nossa dependência de conjuntos de dados públicos não confiáveis ou não curados para treinamento. Para manter a integridade dos dados e evitar um processo de treinamento falho, é crucial rastrear a origem e a linhagem dos seus dados. Caso contrário, o velho ditado "lixo entra, lixo sai" se mantém verdadeiro, levando a um desempenho comprometido do modelo.

Aqui estão exemplos de como o envenenamento de dados pode afetar seus modelos:

1. **Inversão de Rótulos**: Em uma tarefa de classificação binária, um adversário inverte intencionalmente os rótulos de um pequeno subconjunto de dados de treinamento. Por exemplo, amostras benignas são rotuladas como maliciosas, levando o modelo a aprender associações incorretas.\
   **Exemplo**: Um filtro de spam classificando erroneamente e-mails legítimos como spam devido a rótulos manipulados.
2. **Envenenamento de Características**: Um atacante modifica sutilmente características nos dados de treinamento para introduzir viés ou enganar o modelo.\
   **Exemplo**: Adicionar palavras-chave irrelevantes a descrições de produtos para manipular sistemas de recomendação.
3. **Injeção de Dados**: Injetar dados maliciosos no conjunto de treinamento para influenciar o comportamento do modelo.\
   **Exemplo**: Introduzir avaliações falsas de usuários para distorcer resultados de análise de sentimento.
4. **Ataques de Backdoor**: Um adversário insere um padrão oculto (backdoor) nos dados de treinamento. O modelo aprende a reconhecer esse padrão e se comporta de forma maliciosa quando acionado.\
   **Exemplo**: Um sistema de reconhecimento facial treinado com imagens com backdoor que identifica erroneamente uma pessoa específica.

A MITRE Corporation criou o [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), um banco de dados de táticas e técnicas empregadas por adversários em ataques reais a sistemas de IA.

> Há um número crescente de vulnerabilidades em sistemas habilitados para IA, à medida que a incorporação de IA aumenta a superfície de ataque dos sistemas existentes além daqueles dos ataques cibernéticos tradicionais. Desenvolvemos o ATLAS para aumentar a conscientização sobre essas vulnerabilidades únicas e em evolução, à medida que a comunidade global incorpora cada vez mais a IA em vários sistemas. O ATLAS é modelado após o framework MITRE ATT&CK® e suas táticas, técnicas e procedimentos (TTPs) são complementares aos do ATT&CK.

Assim como o framework MITRE ATT&CK®, que é amplamente utilizado na cibersegurança tradicional para planejar cenários avançados de emulação de ameaças, o ATLAS fornece um conjunto de TTPs facilmente pesquisável que pode ajudar a entender melhor e se preparar para defender contra ataques emergentes.

Além disso, o Open Web Application Security Project (OWASP) criou uma "[Lista Top 10](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" das vulnerabilidades mais críticas encontradas em aplicações que utilizam LLMs. A lista destaca os riscos de ameaças como o envenenamento de dados mencionado, juntamente com outras como:

- **Injeção de Prompt**: uma técnica onde os atacantes manipulam um Modelo de Linguagem de Grande Porte (LLM) através de entradas cuidadosamente elaboradas, fazendo com que ele se comporte fora do seu comportamento pretendido.
- **Vulnerabilidades na Cadeia de Suprimentos**: Os componentes e softwares que compõem as aplicações usadas por um LLM, como módulos Python ou conjuntos de dados externos, podem ser comprometidos, levando a resultados inesperados, introdução de vieses e até mesmo vulnerabilidades na infraestrutura subjacente.
- **Superdependência**: LLMs são falíveis e têm tendência a alucinar, fornecendo resultados imprecisos ou inseguros. Em várias circunstâncias documentadas, as pessoas aceitaram os resultados sem questionar, levando a consequências negativas não intencionais no mundo real.

O Microsoft Cloud Advocate Rod Trent escreveu um ebook gratuito, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), que explora profundamente essas e outras ameaças emergentes de IA e fornece orientações extensas sobre como melhor lidar com esses cenários.

## Testes de Segurança para Sistemas de IA e LLMs

A inteligência artificial (IA) está transformando vários domínios e indústrias, oferecendo novas possibilidades e benefícios para a sociedade. No entanto, a IA também apresenta desafios e riscos significativos, como privacidade de dados, viés, falta de explicabilidade e uso indevido potencial. Portanto, é crucial garantir que os sistemas de IA sejam seguros e responsáveis, ou seja, que eles atendam a padrões éticos e legais e possam ser confiáveis por usuários e partes interessadas.

O teste de segurança é o processo de avaliar a segurança de um sistema de IA ou LLM, identificando e explorando suas vulnerabilidades. Isso pode ser realizado por desenvolvedores, usuários ou auditores terceirizados, dependendo do propósito e escopo do teste. Alguns dos métodos de teste de segurança mais comuns para sistemas de IA e LLMs são:

- **Sanitização de Dados**: Este é o processo de remover ou anonimizar informações sensíveis ou privadas dos dados de treinamento ou da entrada de um sistema de IA ou LLM. A sanitização de dados pode ajudar a prevenir vazamento de dados e manipulação maliciosa, reduzindo a exposição de dados confidenciais ou pessoais.
- **Teste Adversarial**: Este é o processo de gerar e aplicar exemplos adversariais à entrada ou saída de um sistema de IA ou LLM para avaliar sua robustez e resiliência contra ataques adversariais. O teste adversarial pode ajudar a identificar e mitigar as vulnerabilidades e fraquezas de um sistema de IA ou LLM que podem ser exploradas por atacantes.
- **Verificação de Modelo**: Este é o processo de verificar a correção e completude dos parâmetros ou arquitetura do modelo de um sistema de IA ou LLM. A verificação de modelo pode ajudar a detectar e prevenir o roubo de modelos, garantindo que o modelo esteja protegido e autenticado.
- **Validação de Saída**: Este é o processo de validar a qualidade e confiabilidade da saída de um sistema de IA ou LLM. A validação de saída pode ajudar a detectar e corrigir manipulações maliciosas, garantindo que a saída seja consistente e precisa.

A OpenAI, líder em sistemas de IA, configurou uma série de _avaliações de segurança_ como parte de sua iniciativa de rede de red teaming, visando testar a saída de sistemas de IA na esperança de contribuir para a segurança da IA.

> As avaliações podem variar de testes simples de perguntas e respostas a simulações mais complexas. Como exemplos concretos, aqui estão avaliações de amostra desenvolvidas pela OpenAI para avaliar comportamentos de IA de vários ângulos:

#### Persuasão

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode enganar outro sistema de IA para dizer uma palavra secreta?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode convencer outro sistema de IA a doar dinheiro?
- [Proposta de Votação](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode influenciar o apoio de outro sistema de IA a uma proposta política?

#### Esteganografia (mensagens ocultas)

- [Esteganografia](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode passar mensagens secretas sem ser pego por outro sistema de IA?
- [Compressão de Texto](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode comprimir e descomprimir mensagens para permitir a ocultação de mensagens secretas?
- [Ponto de Schelling](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Quão bem um sistema de IA pode coordenar com outro sistema de IA, sem comunicação direta?

### Segurança de IA

É imperativo que busquemos proteger os sistemas de IA contra ataques maliciosos, uso indevido ou consequências não intencionais. Isso inclui tomar medidas para garantir a segurança, confiabilidade e confiabilidade dos sistemas de IA, como:

- Proteger os dados e algoritmos usados para treinar e executar modelos de IA
- Prevenir o acesso não autorizado, manipulação ou sabotagem de sistemas de IA
- Detectar e mitigar viés, discriminação ou questões éticas em sistemas de IA
- Garantir a responsabilidade, transparência e explicabilidade das decisões e ações da IA
- Alinhar os objetivos e valores dos sistemas de IA com os de humanos e da sociedade

A segurança de IA é importante para garantir a integridade, disponibilidade e confidencialidade dos sistemas de IA e dados. Alguns dos desafios e oportunidades da segurança de IA são:

- Oportunidade: Incorporar a IA em estratégias de cibersegurança, já que ela pode desempenhar um papel crucial na identificação de ameaças e na melhoria dos tempos de resposta. A IA pode ajudar a automatizar e aumentar a detecção e mitigação de ataques cibernéticos, como phishing, malware ou ransomware.
- Desafio: A IA também pode ser usada por adversários para lançar ataques sofisticados, como gerar conteúdo falso ou enganoso, personificar usuários ou explorar vulnerabilidades em sistemas de IA. Portanto, os desenvolvedores de IA têm uma responsabilidade única de projetar sistemas que sejam robustos e resilientes contra o uso indevido.

### Proteção de Dados

LLMs podem representar riscos para a privacidade e segurança dos dados que utilizam. Por exemplo, LLMs podem potencialmente memorizar e vazar informações sensíveis de seus dados de treinamento, como nomes pessoais, endereços, senhas ou números de cartão de crédito. Eles também podem ser manipulados ou atacados por atores maliciosos que desejam explorar suas vulnerabilidades ou vieses. Portanto, é importante estar ciente desses riscos e tomar medidas apropriadas para proteger os dados usados com LLMs. Existem várias etapas que você pode seguir para proteger os dados usados com LLMs. Essas etapas incluem:

- **Limitar a quantidade e tipo de dados que compartilham com LLMs**: Compartilhe apenas os dados que são necessários e relevantes para os propósitos pretendidos, e evite compartilhar quaisquer dados que sejam sensíveis, confidenciais ou pessoais. Os usuários também devem anonimizar ou criptografar os dados que compartilham com LLMs, como removendo ou mascarando qualquer informação identificável, ou usando canais de comunicação seguros.
- **Verificar os dados que os LLMs geram**: Sempre verifique a precisão e a qualidade da saída gerada pelos LLMs para garantir que não contenham nenhuma informação indesejada ou inadequada.
- **Relatar e alertar sobre quaisquer violações de dados ou incidentes**: Esteja atento a quaisquer atividades ou comportamentos suspeitos ou anormais dos LLMs, como gerar textos que sejam irrelevantes, imprecisos, ofensivos ou prejudiciais. Isso pode ser um indicativo de uma violação de dados ou incidente de segurança.

Segurança de dados, governança e conformidade são críticas para qualquer organização que deseja aproveitar o poder dos dados e da IA em um ambiente multi-nuvem. Proteger e governar todos os seus dados é uma tarefa complexa e multifacetada. Você precisa proteger e governar diferentes tipos de dados (estruturados, não estruturados e dados gerados por IA) em diferentes locais em várias nuvens, e precisa levar em conta as regulamentações de segurança de dados, governança e IA existentes e futuras. Para proteger seus dados, você precisa adotar algumas práticas recomendadas e precauções, como:

- Usar serviços ou plataformas em nuvem que ofereçam recursos de proteção de dados e privacidade.
- Usar ferramentas de qualidade e validação de dados para verificar seus dados em busca de erros, inconsistências ou anomalias.
- Usar frameworks de governança e ética de dados para garantir que seus dados sejam usados de maneira responsável e transparente.

### Emulação de ameaças do mundo real - Red teaming de IA

A emulação de ameaças do mundo real é agora considerada uma prática padrão na construção de sistemas de IA resilientes, empregando ferramentas, táticas e procedimentos semelhantes para identificar os riscos aos sistemas e testar a resposta dos defensores.

> A prática de red teaming de IA evoluiu para assumir um significado mais expandido: ela não apenas cobre a busca por vulnerabilidades de segurança, mas também inclui a busca por outras falhas do sistema, como a geração de conteúdo potencialmente prejudicial. Os sistemas de IA vêm com novos riscos, e o red teaming é fundamental para entender esses riscos novos, como a injeção de prompt e a produção de conteúdo não fundamentado. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Orientações e recursos para red teaming](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.pt.png)]()

Abaixo estão insights-chave que moldaram o programa de Red Team da Microsoft para IA.

1. **Escopo Expansivo do Red Teaming de IA**:
   O red teaming de IA agora abrange tanto os resultados de segurança quanto os de IA Responsável (RAI). Tradicionalmente, o red teaming focava nos aspectos de segurança, tratando o modelo como um vetor (por exemplo, roubo do modelo subjacente). No entanto, os sistemas de IA introduzem novas vulnerabilidades de segurança (por exemplo, injeção de prompt, envenenamento), exigindo atenção especial. Além da segurança, o red teaming de IA também investiga questões de equidade (por exemplo, estereótipos) e conteúdo prejudicial (por exemplo, glorificação da violência). A identificação precoce dessas questões permite a priorização dos investimentos em defesa.
2. **Falhas Maliciosas e Benignas**:
   O red teaming de IA considera falhas tanto de perspectivas maliciosas quanto benignas. Por exemplo, ao fazer red teaming do novo Bing, exploramos não apenas como adversários maliciosos podem subverter o sistema, mas também como usuários regulares podem encontrar conteúdo problemático ou prejudicial. Ao contrário do red teaming de segurança tradicional, que foca principalmente em atores maliciosos, o red teaming de IA leva em conta uma gama mais ampla de personas e falhas potenciais.
3. **Natureza Dinâmica dos Sistemas de IA**:
   As aplicações de IA estão em constante evolução. Em aplicações de modelos de linguagem de grande porte, os desenvolvedores se adaptam a requisitos em mudança. O red teaming contínuo garante vigilância contínua e adaptação aos riscos em evolução.

O red teaming de IA não é abrangente e deve ser considerado um movimento complementar a controles adicionais, como [controle de acesso baseado em funções (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) e soluções abrangentes de gerenciamento de dados. Ele é destinado a complementar uma estratégia de segurança que foca em empregar soluções de IA seguras e responsáveis que considerem privacidade e segurança, enquanto aspiram a minimizar vieses, conteúdo prejudicial

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.