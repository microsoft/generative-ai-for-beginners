[![Intégration avec l'appel de fonction](../../../translated_images/fr/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Le cycle de vie des applications d'IA générative

Une question importante pour toutes les applications d'IA est la pertinence des fonctionnalités IA, puisqu'il s'agit d'un domaine en rapide évolution. Pour garantir que votre application reste pertinente, fiable et robuste, vous devez la surveiller, l'évaluer et l'améliorer continuellement. C’est là qu’intervient le cycle de vie de l’IA générative.

Le cycle de vie de l’IA générative est un cadre qui vous guide à travers les étapes de développement, de déploiement et de maintenance d'une application d'IA générative. Il vous aide à définir vos objectifs, mesurer vos performances, identifier vos défis et mettre en œuvre vos solutions. Il aide également à aligner votre application avec les normes éthiques et juridiques de votre domaine et de vos parties prenantes. En suivant ce cycle de vie, vous pouvez vous assurer que votre application délivre toujours de la valeur et satisfait vos utilisateurs.

## Introduction

Dans ce chapitre, vous allez :

- Comprendre le changement de paradigme de MLOps à LLMOps
- Le cycle de vie des LLM
- Outils du cycle de vie
- Mesure et évaluation dans le cycle de vie

## Comprendre le changement de paradigme de MLOps à LLMOps

Les LLM sont un nouvel outil dans l'arsenal de l’Intelligence Artificielle, ils sont incroyablement puissants pour les tâches d'analyse et de génération pour les applications, cependant cette puissance a des conséquences sur la manière dont nous optimisons les tâches d’IA et d’apprentissage automatique classique.

Avec cela, nous avons besoin d'un nouveau paradigme pour adapter cet outil de façon dynamique, avec les bons incitatifs. Nous pouvons catégoriser les anciennes applications IA comme "applications ML" et les nouveautés comme "applications GenAI" ou simplement "applications IA", reflétant la technologie et les techniques principales utilisées à l'époque. Cela change notre narrative de plusieurs façons, regardez la comparaison suivante.

![Comparaison LLMOps vs. MLOps](../../../translated_images/fr/01-llmops-shift.29bc933cb3bb0080.webp)

Notez que dans LLMOps, nous sommes plus centrés sur les développeurs d'applications, utilisant les intégrations comme point clé, exploitant « Modèles en tant que service » et en pensant aux points suivants pour les métriques.

- Qualité : Qualité de la réponse
- Risque : IA responsable
- Honnêteté : Fondement de la réponse (Est-ce cohérent ? Est-ce correct ?)
- Coût : Budget de la solution
- Latence : Temps moyen de réponse par token

## Le cycle de vie des LLM

D’abord, pour comprendre le cycle de vie et ses modifications, notons l’infographie suivante.

![Infographie LLMOps](../../../translated_images/fr/02-llmops.70a942ead05a7645.webp)

Comme vous pouvez le constater, cela diffère des cycles de vie habituels de MLOps. Les LLM ont de nombreuses nouvelles exigences, telles que le prompt engineering, les différentes techniques pour améliorer la qualité (Fine-Tuning, RAG, Métaprompts), des évaluations différentes et la responsabilité liée à l’IA responsable, enfin, de nouvelles métriques d’évaluation (Qualité, Risque, Honnêteté, Coût et Latence).

Par exemple, regardez comment nous générons des idées. En utilisant le prompt engineering pour expérimenter avec divers LLMs afin d’explorer les possibilités et tester si leur hypothèse pourrait être correcte.

Notez que ce cycle n’est pas linéaire, mais constitué de boucles intégrées, itératives et avec un cycle global.

Comment pourrions-nous explorer ces étapes ? Entrons dans le détail pour construire un cycle de vie.

![Flux de travail LLMOps](../../../translated_images/fr/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Cela peut sembler un peu compliqué, concentrons-nous d'abord sur les trois grandes étapes.

1. Idéation/Exploration : Exploration, ici nous pouvons explorer selon nos besoins métier. Prototypage, création d’un [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) et test de son efficacité pour notre hypothèse.
1. Construction/Augmentation : Mise en œuvre, nous commençons maintenant à évaluer sur des jeux de données plus grands et à appliquer des techniques telles que le Fine-tuning et RAG pour vérifier la robustesse de notre solution. Si ce n’est pas le cas, une réimplémentation, ajout de nouvelles étapes dans notre flux ou restructuration des données peut aider. Après avoir testé notre flux et notre échelle, si cela fonctionne et que nos métriques sont validées, nous passons à l’étape suivante.
1. Opérationnalisation : Intégration, maintenant on ajoute des systèmes de surveillance et d’alertes au système, déploiement et intégration à notre application.

Ensuite, nous avons le cycle global de gestion, concentré sur la sécurité, la conformité et la gouvernance.

Félicitations, vous avez maintenant votre application IA prête et opérationnelle. Pour une expérience pratique, consultez la [Démo Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Maintenant, quels outils pouvons-nous utiliser ?

## Outils du cycle de vie

Pour les outils, Microsoft propose la [plateforme Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) et [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) facilite et rend votre cycle facile à implémenter et prêt à l’emploi.

La [plateforme Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) vous permet d’utiliser [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (anciennement Azure AI Studio) est un portail web qui vous permet d'explorer des modèles, des exemples et des outils, de gérer vos ressources, d'utiliser des flux de développement UI ainsi que des options SDK/CLI pour un développement avec code.

![Possibilités Azure AI](../../../translated_images/fr/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI vous permet d’utiliser plusieurs ressources pour gérer vos opérations, services, projets, recherches vectorielles et besoins en bases de données.

![LLMOps avec Azure AI](../../../translated_images/fr/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Construisez, du Proof-of-Concept (POC) aux applications à grande échelle avec PromptFlow :

- Concevez et construisez des applications depuis VS Code, avec des outils visuels et fonctionnels
- Testez et affinez vos applications pour une IA de qualité, facilement.
- Utilisez Microsoft Foundry pour intégrer et itérer avec le cloud, pousser et déployer pour une intégration rapide.

![LLMOps avec PromptFlow](../../../translated_images/fr/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Super ! Continuez votre apprentissage !

Incroyable, apprenez maintenant comment nous structurons une application pour utiliser les concepts avec l'[application Contoso Chat](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), pour voir comment Cloud Advocacy ajoute ces concepts dans les démonstrations. Pour plus de contenu, regardez notre [session Ignite !
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Maintenant, consultez la leçon 15, pour comprendre comment [la génération augmentée par récupération et les bases de données vectorielles](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) impactent l’IA générative et permettent de créer des applications plus engageantes !

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->