# Sécuriser vos applications d'IA générative

[![Sécuriser vos applications d'IA générative](../../../translated_images/13-lesson-banner.png?WT.028697a53f1c3c0ea07dafd10617ce0380ac2b809bb145d7171be69e83daac89.fr.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson13-gh?WT.mc_id=academic-105485-koreyst)

## Introduction

Cette leçon couvrira :

- La sécurité dans le contexte des systèmes d'IA.
- Les risques et menaces courants pour les systèmes d'IA.
- Méthodes et considérations pour sécuriser les systèmes d'IA.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous comprendrez :

- Les menaces et risques pour les systèmes d'IA.
- Les méthodes et pratiques courantes pour sécuriser les systèmes d'IA.
- Comment la mise en œuvre de tests de sécurité peut prévenir des résultats inattendus et l'érosion de la confiance des utilisateurs.

## Que signifie la sécurité dans le contexte de l'IA générative ?

Alors que les technologies d'Intelligence Artificielle (IA) et d'Apprentissage Automatique (ML) façonnent de plus en plus nos vies, il est crucial de protéger non seulement les données des clients, mais aussi les systèmes d'IA eux-mêmes. L'IA/ML est de plus en plus utilisée pour soutenir les processus de prise de décision de grande valeur dans les industries où une mauvaise décision peut avoir des conséquences graves.

Voici des points clés à considérer :

- **Impact de l'IA/ML** : L'IA/ML ont des impacts significatifs sur la vie quotidienne et, à ce titre, leur protection est devenue essentielle.
- **Défis de sécurité** : Cet impact de l'IA/ML nécessite une attention appropriée pour répondre au besoin de protéger les produits basés sur l'IA contre des attaques sophistiquées, que ce soit par des trolls ou des groupes organisés.
- **Problèmes stratégiques** : L'industrie technologique doit aborder de manière proactive les défis stratégiques pour garantir la sécurité à long terme des clients et la sécurité des données.

De plus, les modèles d'apprentissage automatique sont largement incapables de discerner entre une entrée malveillante et des données anormales bénignes. Une source importante de données d'entraînement provient de jeux de données publics non curatés et non modérés, ouverts aux contributions de tiers. Les attaquants n'ont pas besoin de compromettre les jeux de données lorsqu'ils sont libres d'y contribuer. Au fil du temps, les données malveillantes de faible confiance deviennent des données de haute confiance, si la structure/format des données reste correct.

C'est pourquoi il est crucial d'assurer l'intégrité et la protection des magasins de données que vos modèles utilisent pour prendre des décisions.

## Comprendre les menaces et risques de l'IA

En termes d'IA et de systèmes associés, l'empoisonnement des données se distingue comme la menace de sécurité la plus significative aujourd'hui. L'empoisonnement des données se produit lorsque quelqu'un modifie intentionnellement les informations utilisées pour entraîner une IA, la faisant ainsi commettre des erreurs. Cela est dû à l'absence de méthodes de détection et de mitigation standardisées, couplée à notre dépendance à des jeux de données publics non fiables ou non curatés pour l'entraînement. Pour maintenir l'intégrité des données et prévenir un processus d'entraînement défectueux, il est crucial de suivre l'origine et la lignée de vos données. Sinon, le vieil adage "garbage in, garbage out" reste vrai, conduisant à une performance compromise du modèle.

Voici des exemples de la façon dont l'empoisonnement des données peut affecter vos modèles :

1. **Renversement de labels** : Dans une tâche de classification binaire, un adversaire renverse intentionnellement les labels d'un petit sous-ensemble de données d'entraînement. Par exemple, des échantillons bénins sont étiquetés comme malveillants, amenant le modèle à apprendre des associations incorrectes.\
   **Exemple** : Un filtre anti-spam classifiant à tort des emails légitimes comme spam en raison de labels manipulés.
2. **Empoisonnement de caractéristiques** : Un attaquant modifie subtilement les caractéristiques des données d'entraînement pour introduire un biais ou induire le modèle en erreur.\
   **Exemple** : Ajouter des mots-clés non pertinents aux descriptions de produits pour manipuler les systèmes de recommandation.
3. **Injection de données** : Injecter des données malveillantes dans l'ensemble d'entraînement pour influencer le comportement du modèle.\
   **Exemple** : Introduire de fausses critiques d'utilisateurs pour fausser les résultats de l'analyse de sentiments.
4. **Attaques de porte dérobée** : Un adversaire insère un motif caché (porte dérobée) dans les données d'entraînement. Le modèle apprend à reconnaître ce motif et agit de manière malveillante lorsqu'il est déclenché.\
   **Exemple** : Un système de reconnaissance faciale entraîné avec des images contenant une porte dérobée qui identifie incorrectement une personne spécifique.

La MITRE Corporation a créé [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), une base de connaissances des tactiques et techniques employées par les adversaires dans les attaques réelles sur les systèmes d'IA.

> Il y a un nombre croissant de vulnérabilités dans les systèmes activés par l'IA, car l'incorporation de l'IA augmente la surface d'attaque des systèmes existants au-delà de celles des cyberattaques traditionnelles. Nous avons développé ATLAS pour sensibiliser à ces vulnérabilités uniques et en évolution, car la communauté mondiale intègre de plus en plus l'IA dans divers systèmes. ATLAS est modélisé d'après le cadre MITRE ATT&CK® et ses tactiques, techniques et procédures (TTPs) sont complémentaires à celles d'ATT&CK.

Tout comme le cadre MITRE ATT&CK®, qui est largement utilisé dans la cybersécurité traditionnelle pour planifier des scénarios avancés d'émulation de menaces, ATLAS fournit un ensemble de TTPs facilement consultables qui peuvent aider à mieux comprendre et se préparer à défendre contre les attaques émergentes.

De plus, l'Open Web Application Security Project (OWASP) a créé une "[liste des 10 principales vulnérabilités](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" les plus critiques trouvées dans les applications utilisant des LLMs. La liste met en évidence les risques de menaces telles que l'empoisonnement des données mentionné précédemment, ainsi que d'autres comme :

- **Injection de prompts** : une technique où les attaquants manipulent un modèle de langage de grande taille (LLM) à travers des entrées soigneusement conçues, le faisant se comporter en dehors de son comportement prévu.
- **Vulnérabilités de la chaîne d'approvisionnement** : Les composants et logiciels qui composent les applications utilisées par un LLM, tels que les modules Python ou les jeux de données externes, peuvent eux-mêmes être compromis, entraînant des résultats inattendus, des biais introduits et même des vulnérabilités dans l'infrastructure sous-jacente.
- **Dépendance excessive** : Les LLMs sont faillibles et ont tendance à halluciner, fournissant des résultats inexacts ou dangereux. Dans plusieurs circonstances documentées, les gens ont pris les résultats pour argent comptant, conduisant à des conséquences négatives inattendues dans le monde réel.

Rod Trent, Cloud Advocate chez Microsoft, a écrit un ebook gratuit, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), qui explore en profondeur ces menaces émergentes de l'IA et fournit des conseils approfondis sur la meilleure façon de gérer ces scénarios.

## Test de sécurité pour les systèmes d'IA et les LLMs

L'intelligence artificielle (IA) transforme divers domaines et industries, offrant de nouvelles possibilités et avantages pour la société. Cependant, l'IA pose également des défis et des risques importants, tels que la confidentialité des données, les biais, le manque d'explicabilité et le potentiel d'utilisation abusive. Par conséquent, il est crucial de s'assurer que les systèmes d'IA sont sécurisés et responsables, c'est-à-dire qu'ils respectent les normes éthiques et légales et peuvent être dignes de confiance par les utilisateurs et les parties prenantes.

Le test de sécurité est le processus d'évaluation de la sécurité d'un système d'IA ou d'un LLM, en identifiant et en exploitant leurs vulnérabilités. Cela peut être effectué par des développeurs, des utilisateurs ou des auditeurs tiers, selon le but et l'étendue des tests. Certaines des méthodes de test de sécurité les plus courantes pour les systèmes d'IA et les LLMs sont :

- **Assainissement des données** : C'est le processus de suppression ou d'anonymisation des informations sensibles ou privées des données d'entraînement ou de l'entrée d'un système d'IA ou d'un LLM. L'assainissement des données peut aider à prévenir la fuite de données et la manipulation malveillante en réduisant l'exposition des données confidentielles ou personnelles.
- **Test adversarial** : C'est le processus de génération et d'application d'exemples adversariaux à l'entrée ou à la sortie d'un système d'IA ou d'un LLM pour évaluer sa robustesse et sa résilience contre les attaques adversariales. Le test adversarial peut aider à identifier et à atténuer les vulnérabilités et faiblesses d'un système d'IA ou d'un LLM qui pourraient être exploitées par des attaquants.
- **Vérification du modèle** : C'est le processus de vérification de l'exactitude et de l'exhaustivité des paramètres ou de l'architecture du modèle d'un système d'IA ou d'un LLM. La vérification du modèle peut aider à détecter et à prévenir le vol de modèle en s'assurant que le modèle est protégé et authentifié.
- **Validation de la sortie** : C'est le processus de validation de la qualité et de la fiabilité de la sortie d'un système d'IA ou d'un LLM. La validation de la sortie peut aider à détecter et à corriger la manipulation malveillante en s'assurant que la sortie est cohérente et précise.

OpenAI, un leader dans les systèmes d'IA, a mis en place une série d'_évaluations de sécurité_ dans le cadre de leur initiative de réseau de red teaming, visant à tester les systèmes d'IA dans l'espoir de contribuer à la sécurité de l'IA.

> Les évaluations peuvent aller de tests simples de questions-réponses à des simulations plus complexes. Voici des exemples concrets d'évaluations développées par OpenAI pour évaluer les comportements de l'IA sous plusieurs angles :

#### Persuasion

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst) : Dans quelle mesure un système d'IA peut-il tromper un autre système d'IA pour qu'il dise un mot secret ?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst) : Dans quelle mesure un système d'IA peut-il convaincre un autre système d'IA de donner de l'argent ?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst) : Dans quelle mesure un système d'IA peut-il influencer le soutien d'un autre système d'IA à une proposition politique ?

#### Stéganographie (messagerie cachée)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst) : Dans quelle mesure un système d'IA peut-il passer des messages secrets sans être détecté par un autre système d'IA ?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst) : Dans quelle mesure un système d'IA peut-il compresser et décompresser des messages pour permettre de cacher des messages secrets ?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst) : Dans quelle mesure un système d'IA peut-il se coordonner avec un autre système d'IA, sans communication directe ?

### Sécurité de l'IA

Il est impératif que nous visons à protéger les systèmes d'IA contre les attaques malveillantes, l'utilisation abusive ou les conséquences involontaires. Cela inclut de prendre des mesures pour garantir la sécurité, la fiabilité et la confiance des systèmes d'IA, telles que :

- Sécuriser les données et les algorithmes utilisés pour entraîner et exécuter les modèles d'IA
- Empêcher l'accès non autorisé, la manipulation ou le sabotage des systèmes d'IA
- Détecter et atténuer les biais, la discrimination ou les problèmes éthiques dans les systèmes d'IA
- Assurer la responsabilité, la transparence et l'explicabilité des décisions et actions de l'IA
- Aligner les objectifs et les valeurs des systèmes d'IA avec ceux des humains et de la société

La sécurité de l'IA est importante pour garantir l'intégrité, la disponibilité et la confidentialité des systèmes et des données d'IA. Certains des défis et opportunités de la sécurité de l'IA sont :

- Opportunité : Incorporer l'IA dans les stratégies de cybersécurité, car elle peut jouer un rôle crucial dans l'identification des menaces et l'amélioration des temps de réponse. L'IA peut aider à automatiser et à augmenter la détection et la mitigation des cyberattaques, telles que le phishing, les logiciels malveillants ou les rançongiciels.
- Défi : L'IA peut également être utilisée par les adversaires pour lancer des attaques sophistiquées, telles que générer du contenu faux ou trompeur, usurper l'identité des utilisateurs ou exploiter des vulnérabilités dans les systèmes d'IA. Par conséquent, les développeurs d'IA ont une responsabilité unique de concevoir des systèmes robustes et résilients contre l'utilisation abusive.

### Protection des données

Les LLMs peuvent présenter des risques pour la confidentialité et la sécurité des données qu'ils utilisent. Par exemple, les LLMs peuvent potentiellement mémoriser et divulguer des informations sensibles de leurs données d'entraînement, telles que des noms personnels, des adresses, des mots de passe ou des numéros de carte de crédit. Ils peuvent également être manipulés ou attaqués par des acteurs malveillants qui souhaitent exploiter leurs vulnérabilités ou leurs biais. Par conséquent, il est important d'être conscient de ces risques et de prendre des mesures appropriées pour protéger les données utilisées avec les LLMs. Il y a plusieurs étapes que vous pouvez suivre pour protéger les données utilisées avec les LLMs. Ces étapes incluent :

- **Limiter la quantité et le type de données qu'ils partagent avec les LLMs** : Partagez uniquement les données nécessaires et pertinentes pour les objectifs visés, et évitez de partager des données sensibles, confidentielles ou personnelles. Les utilisateurs devraient également anonymiser ou crypter les données qu'ils partagent avec les LLMs, par exemple en supprimant ou masquant toute information d'identification, ou en utilisant des canaux de communication sécurisés.
- **Vérifier les données générées par les LLMs** : Vérifiez toujours l'exactitude et la qualité des résultats générés par les LLMs pour vous assurer qu'ils ne contiennent pas d'informations indésirables ou inappropriées.
- **Signaler et alerter toute violation de données ou incident** : Soyez vigilant face à toute activité ou comportement suspect ou anormal des LLMs, comme la génération de textes qui sont hors sujet, inexacts, offensants ou nuisibles. Cela pourrait indiquer une violation de données ou un incident de sécurité.

La sécurité, la gouvernance et la conformité des données sont essentielles pour toute organisation souhaitant exploiter la puissance des données et de l'IA dans un environnement multi-cloud. Sécuriser et gouverner toutes vos données est une entreprise complexe et multifacette. Vous devez sécuriser et gouverner différents types de données (structurées, non structurées et données générées par l'IA) à différents emplacements à travers plusieurs clouds, et vous devez tenir compte des réglementations de sécurité, de gouvernance et d'IA existantes et futures. Pour protéger vos données, vous devez adopter certaines meilleures pratiques et précautions, telles que :

- Utilisez des services ou plateformes cloud offrant des fonctionnalités de protection et de confidentialité des données.
- Utilisez des outils de qualité et de validation des données pour vérifier vos données à la recherche d'erreurs, d'incohérences ou d'anomalies.
- Utilisez des cadres de gouvernance et d'éthique des données pour vous assurer que vos données sont utilisées de manière responsable et transparente.

### Émulation des menaces réelles - Red teaming de l'IA

L'émulation des menaces réelles est désormais considérée comme une pratique standard pour construire des systèmes d'IA résilients en utilisant des outils, tactiques et procédures similaires pour identifier les risques pour les systèmes et tester la réponse des défenseurs.

> La pratique du red teaming de l'IA a évolué pour prendre une signification plus étendue : elle couvre non seulement la recherche de vulnérabilités de sécurité, mais inclut également la recherche d'autres défaillances du système, telles que la génération de contenu potentiellement nuisible. Les systèmes d'IA présentent de nouveaux risques, et le red teaming est essentiel pour comprendre ces risques nouveaux, tels que l'injection de prompts et la production de contenu non fondé. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Conseils et ressources pour le red teaming](../../../translated_images/13-AI-red-team.png?WT.5a1ed56fe6f4caf0ada6509bb7aacc47c7da784e5747e1a5373539d9f05bede2.fr.mc_id=academic-105485-koreyst)]()

Voici des points clés qui ont façonné le programme AI Red Team de Microsoft.

1. **Portée étendue du red teaming de l'IA :**
   Le red teaming de l'IA englobe désormais à la fois les résultats en matière de sécurité et d'IA Responsable (RAI

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.