<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T22:10:31+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "fr"
}
-->
# Sécuriser vos applications d'IA générative

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

Alors que les technologies d'Intelligence Artificielle (IA) et d'Apprentissage Machine (ML) façonnent de plus en plus nos vies, il est crucial de protéger non seulement les données des clients mais aussi les systèmes d'IA eux-mêmes. L'IA/ML est de plus en plus utilisée pour soutenir des processus décisionnels de grande valeur dans des industries où une mauvaise décision peut avoir de graves conséquences.

Voici des points clés à considérer :

- **Impact de l'IA/ML** : L'IA/ML a des impacts significatifs sur la vie quotidienne et il est donc essentiel de les protéger.
- **Défis de sécurité** : Cet impact nécessite une attention appropriée pour protéger les produits basés sur l'IA contre des attaques sophistiquées, qu'elles proviennent de trolls ou de groupes organisés.
- **Problèmes stratégiques** : L'industrie technologique doit aborder de manière proactive les défis stratégiques pour assurer la sécurité à long terme des clients et la sécurité des données.

De plus, les modèles d'apprentissage machine sont en grande partie incapables de discerner entre les entrées malveillantes et les données anormales bénignes. Une source importante de données d'entraînement provient de jeux de données publics non modérés, ouverts aux contributions de tiers. Les attaquants n'ont pas besoin de compromettre les jeux de données lorsqu'ils peuvent y contribuer librement. Avec le temps, les données malveillantes à faible confiance deviennent des données de haute confiance, si la structure/le format des données reste correct.

C'est pourquoi il est crucial de garantir l'intégrité et la protection des magasins de données que vos modèles utilisent pour prendre des décisions.

## Comprendre les menaces et les risques de l'IA

En termes de systèmes d'IA et connexes, l'empoisonnement des données se distingue comme la menace de sécurité la plus importante aujourd'hui. L'empoisonnement des données se produit lorsque quelqu'un modifie intentionnellement les informations utilisées pour entraîner une IA, provoquant ainsi des erreurs. Cela est dû à l'absence de méthodes standardisées de détection et d'atténuation, combinée à notre dépendance à l'égard de jeux de données publics non fiables ou non modérés pour l'entraînement. Pour maintenir l'intégrité des données et éviter un processus d'entraînement défectueux, il est crucial de suivre l'origine et la lignée de vos données. Sinon, le vieil adage "garbage in, garbage out" s'applique, entraînant une performance compromise du modèle.

Voici des exemples de la manière dont l'empoisonnement des données peut affecter vos modèles :

1. **Renversement d'étiquettes** : Dans une tâche de classification binaire, un adversaire renverse intentionnellement les étiquettes d'un petit sous-ensemble de données d'entraînement. Par exemple, des échantillons bénins sont étiquetés comme malveillants, amenant le modèle à apprendre des associations incorrectes.\
   **Exemple** : Un filtre anti-spam classant à tort des e-mails légitimes comme spam en raison d'étiquettes manipulées.
2. **Empoisonnement de caractéristiques** : Un attaquant modifie subtilement les caractéristiques des données d'entraînement pour introduire un biais ou tromper le modèle.\
   **Exemple** : Ajouter des mots-clés non pertinents aux descriptions de produits pour manipuler les systèmes de recommandation.
3. **Injection de données** : Injecter des données malveillantes dans le jeu d'entraînement pour influencer le comportement du modèle.\
   **Exemple** : Introduire de faux avis d'utilisateurs pour fausser les résultats d'analyse de sentiment.
4. **Attaques par porte dérobée** : Un adversaire insère un motif caché (porte dérobée) dans les données d'entraînement. Le modèle apprend à reconnaître ce motif et adopte un comportement malveillant lorsqu'il est déclenché.\
   **Exemple** : Un système de reconnaissance faciale entraîné avec des images contenant des portes dérobées qui identifie à tort une personne spécifique.

La MITRE Corporation a créé [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), une base de connaissances des tactiques et techniques employées par les adversaires dans des attaques réelles sur des systèmes d'IA.

> Il existe un nombre croissant de vulnérabilités dans les systèmes dotés d'IA, car l'incorporation de l'IA augmente la surface d'attaque des systèmes existants au-delà de celles des cyberattaques traditionnelles. Nous avons développé ATLAS pour sensibiliser à ces vulnérabilités uniques et en évolution, alors que la communauté mondiale intègre de plus en plus l'IA dans divers systèmes. ATLAS est modelé d'après le cadre MITRE ATT&CK® et ses tactiques, techniques et procédures (TTPs) sont complémentaires de celles de ATT&CK.

Tout comme le cadre MITRE ATT&CK®, largement utilisé dans la cybersécurité traditionnelle pour planifier des scénarios d'émulation de menaces avancées, ATLAS fournit un ensemble de TTPs facilement consultable qui peut aider à mieux comprendre et se préparer à défendre contre les attaques émergentes.

De plus, le projet Open Web Application Security Project (OWASP) a créé une "[liste des 10 principales](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" vulnérabilités les plus critiques trouvées dans les applications utilisant des LLMs. La liste met en évidence les risques de menaces telles que l'empoisonnement des données mentionné précédemment ainsi que d'autres comme :

- **Injection de prompts** : une technique où les attaquants manipulent un modèle de langage à grande échelle (LLM) par des entrées soigneusement conçues, le faisant se comporter en dehors de son comportement prévu.
- **Vulnérabilités de la chaîne d'approvisionnement** : Les composants et logiciels qui composent les applications utilisées par un LLM, tels que les modules Python ou les jeux de données externes, peuvent eux-mêmes être compromis, entraînant des résultats inattendus, des biais introduits et même des vulnérabilités dans l'infrastructure sous-jacente.
- **Dépendance excessive** : Les LLMs sont faillibles et ont tendance à halluciner, fournissant des résultats inexacts ou dangereux. Dans plusieurs circonstances documentées, les gens ont pris les résultats pour argent comptant, entraînant des conséquences négatives imprévues dans le monde réel.

L'Advocate Cloud de Microsoft, Rod Trent, a écrit un ebook gratuit, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), qui plonge profondément dans ces menaces émergentes de l'IA et fournit des conseils approfondis sur la meilleure façon de traiter ces scénarios.

## Tests de sécurité pour les systèmes d'IA et les LLMs

L'intelligence artificielle (IA) transforme divers domaines et industries, offrant de nouvelles possibilités et avantages pour la société. Cependant, l'IA pose également des défis et des risques importants, tels que la confidentialité des données, le biais, le manque d'explicabilité et une utilisation potentielle abusive. Par conséquent, il est crucial de garantir que les systèmes d'IA sont sécurisés et responsables, c'est-à-dire qu'ils respectent les normes éthiques et légales et peuvent être dignes de confiance pour les utilisateurs et les parties prenantes.

Les tests de sécurité sont le processus d'évaluation de la sécurité d'un système d'IA ou d'un LLM, en identifiant et en exploitant leurs vulnérabilités. Cela peut être effectué par des développeurs, des utilisateurs ou des auditeurs tiers, en fonction de l'objectif et de la portée des tests. Certaines des méthodes de test de sécurité les plus courantes pour les systèmes d'IA et les LLMs sont :

- **Assainissement des données** : C'est le processus de suppression ou d'anonymisation des informations sensibles ou privées des données d'entraînement ou de l'entrée d'un système d'IA ou d'un LLM. L'assainissement des données peut aider à prévenir la fuite de données et la manipulation malveillante en réduisant l'exposition de données confidentielles ou personnelles.
- **Tests adversaires** : C'est le processus de génération et d'application d'exemples adversaires à l'entrée ou à la sortie d'un système d'IA ou d'un LLM pour évaluer sa robustesse et sa résilience contre les attaques adversaires. Les tests adversaires peuvent aider à identifier et atténuer les vulnérabilités et faiblesses d'un système d'IA ou d'un LLM qui pourraient être exploitées par des attaquants.
- **Vérification du modèle** : C'est le processus de vérification de l'exactitude et de l'exhaustivité des paramètres ou de l'architecture du modèle d'un système d'IA ou d'un LLM. La vérification du modèle peut aider à détecter et prévenir le vol de modèles en garantissant que le modèle est protégé et authentifié.
- **Validation de la sortie** : C'est le processus de validation de la qualité et de la fiabilité de la sortie d'un système d'IA ou d'un LLM. La validation de la sortie peut aider à détecter et corriger la manipulation malveillante en garantissant que la sortie est cohérente et précise.

OpenAI, un leader dans les systèmes d'IA, a mis en place une série d'_évaluations de sécurité_ dans le cadre de leur initiative de réseau de red teaming, visant à tester la sortie des systèmes d'IA dans l'espoir de contribuer à la sécurité de l'IA.

### Sécurité de l'IA

Il est impératif que nous visons à protéger les systèmes d'IA contre les attaques malveillantes, les abus ou les conséquences imprévues. Cela inclut de prendre des mesures pour assurer la sécurité, la fiabilité et la confiance des systèmes d'IA, telles que :

- Sécuriser les données et les algorithmes utilisés pour entraîner et exécuter les modèles d'IA
- Empêcher l'accès non autorisé, la manipulation ou le sabotage des systèmes d'IA
- Détecter et atténuer les biais, la discrimination ou les problèmes éthiques dans les systèmes d'IA
- Assurer la responsabilité, la transparence et l'explicabilité des décisions et actions de l'IA
- Aligner les objectifs et les valeurs des systèmes d'IA avec ceux des humains et de la société

La sécurité de l'IA est importante pour assurer l'intégrité, la disponibilité et la confidentialité des systèmes d'IA et des données. Certains des défis et opportunités de la sécurité de l'IA sont :

- Opportunité : Incorporer l'IA dans les stratégies de cybersécurité car elle peut jouer un rôle crucial dans l'identification des menaces et l'amélioration des temps de réponse. L'IA peut aider à automatiser et augmenter la détection et l'atténuation des cyberattaques, telles que le phishing, les logiciels malveillants ou les ransomwares.
- Défi : L'IA peut également être utilisée par des adversaires pour lancer des attaques sophistiquées, telles que générer du contenu faux ou trompeur, usurper l'identité des utilisateurs ou exploiter les vulnérabilités des systèmes d'IA. Par conséquent, les développeurs d'IA ont une responsabilité unique de concevoir des systèmes robustes et résilients contre les abus.

### Protection des données

Les LLMs peuvent poser des risques pour la confidentialité et la sécurité des données qu'ils utilisent. Par exemple, les LLMs peuvent potentiellement mémoriser et divulguer des informations sensibles de leurs données d'entraînement, telles que des noms personnels, des adresses, des mots de passe ou des numéros de carte de crédit. Ils peuvent également être manipulés ou attaqués par des acteurs malveillants qui veulent exploiter leurs vulnérabilités ou biais. Par conséquent, il est important d'être conscient de ces risques et de prendre des mesures appropriées pour protéger les données utilisées avec les LLMs. Il existe plusieurs étapes que vous pouvez suivre pour protéger les données utilisées avec les LLMs. Ces étapes incluent :

- **Limiter la quantité et le type de données qu'ils partagent avec les LLMs** : Ne partagez que les données nécessaires et pertinentes pour les objectifs prévus, et évitez de partager des données sensibles, confidentielles ou personnelles. Les utilisateurs doivent également anonymiser ou crypter les données qu'ils partagent avec les LLMs, par exemple en supprimant ou en masquant toute information d'identification, ou en utilisant des canaux de communication sécurisés.
- **Vérifier les données générées par les LLMs** : Vérifiez toujours l'exactitude et la qualité de la sortie générée par les LLMs pour vous assurer qu'elles ne contiennent pas d'informations indésirables ou inappropriées.
- **Signaler et alerter toute violation de données ou incident** : Soyez vigilant face à toute activité ou comportement suspect ou anormal des LLMs, comme générer des textes qui sont hors sujet, inexacts, offensants ou nuisibles. Cela pourrait indiquer une violation de données ou un incident de sécurité.

La sécurité, la gouvernance et la conformité des données sont essentielles pour toute organisation qui souhaite tirer parti de la puissance des données et de l'IA dans un environnement multi-cloud. Sécuriser et gouverner toutes vos données est une entreprise complexe et à multiples facettes. Vous devez sécuriser et gouverner différents types de données (structurées, non structurées et générées par l'IA) dans différents emplacements à travers plusieurs clouds, et vous devez tenir compte des réglementations existantes et futures en matière de sécurité, de gouvernance et d'IA. Pour protéger vos données, vous devez adopter certaines meilleures pratiques et précautions, telles que :

- Utilisez des services ou des plateformes cloud qui offrent des fonctionnalités de protection et de confidentialité des données.
- Utilisez des outils de qualité et de validation des données pour vérifier vos données afin de détecter des erreurs, des incohérences ou des anomalies.
- Utilisez des cadres de gouvernance et d'éthique des données pour garantir que vos données sont utilisées de manière responsable et transparente.

### Émuler les menaces du monde réel - Red teaming de l'IA

L'émulation des menaces du monde réel est désormais considérée comme une pratique standard dans la construction de systèmes d'IA résilients en employant des outils, des tactiques et des procédures similaires pour identifier les risques pour les systèmes et tester la réponse des défenseurs.

> La pratique du red teaming de l'IA a évolué pour prendre un sens plus large : elle couvre non seulement la recherche de vulnérabilités de sécurité, mais inclut également la recherche d'autres défaillances du système, telles que la génération de contenu potentiellement nuisible. Les systèmes d'IA présentent de nouveaux risques, et le red teaming est essentiel pour comprendre ces risques nouveaux, tels que l'injection de prompts et la production de contenu non fondé. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

Voici une liste de lectures supplémentaires qui peuvent vous aider à mieux comprendre comment le red teaming peut aider à identifier et atténuer les risques dans vos systèmes d'IA :

- [Planification du red teaming pour les modèles de langage à grande échelle (LLMs) et leurs applications](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Qu'est-ce que le réseau de red teaming d'OpenAI ?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - Une pratique clé pour construire des solutions d'IA plus sûres et plus responsables](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), une base de connaissances des tactiques et techniques employées par les adversaires dans des attaques réelles sur des systèmes d'IA.

## Vérification des connaissances

Quelle pourrait être une bonne approche pour maintenir l'intégrité des données et prévenir les abus ?

1. Avoir des contrôles stricts basés sur les rôles pour l'accès et la gestion des données
1. Mettre en œuvre et auditer l'étiquetage des données pour éviter la mauvaise représentation ou l'abus des données
1. S'assurer que votre infrastructure d'IA prend en charge le filtrage de contenu

R:1, Bien que les trois soient d'excellentes recommandations, s'assurer que vous attribuez les privilèges d'accès aux données appropriés aux utilisateurs contribuera grandement à prévenir la manipulation et la mauvaise représentation des données utilisées par les LLMs.

## 🚀 Défi

Renseignez-vous davantage sur la manière dont vous pouvez [gouverner et protéger les informations sensibles](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) à l'ère de l'IA.

## Bon travail, continuez votre apprentissage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à améliorer vos connaissances en IA générative !

Passez à la leçon 14 où nous examinerons [le cycle de vie des applications d'IA générative](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst) !

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.