[![Intégration avec appel de fonction](../../../translated_images/14-lesson-banner.png?WT.833a8de2ff3806528caaf839db4385f00ff7c9f92ccdd38d886f4d662fc72f2a.fr.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson14-gh?WT.mc_id=academic-105485-koreyst)

# Le Cycle de Vie d'une Application d'IA Générative

Une question importante pour toutes les applications d'IA est la pertinence des fonctionnalités d'IA, car le domaine de l'IA évolue rapidement. Pour garantir que votre application reste pertinente, fiable et robuste, vous devez la surveiller, l'évaluer et l'améliorer en continu. C'est là qu'intervient le cycle de vie de l'IA générative.

Le cycle de vie de l'IA générative est un cadre qui vous guide à travers les étapes de développement, de déploiement et de maintenance d'une application d'IA générative. Il vous aide à définir vos objectifs, à mesurer vos performances, à identifier vos défis et à mettre en œuvre vos solutions. Il vous aide également à aligner votre application avec les normes éthiques et légales de votre domaine et de vos parties prenantes. En suivant le cycle de vie de l'IA générative, vous pouvez vous assurer que votre application apporte toujours de la valeur et satisfait vos utilisateurs.

## Introduction

Dans ce chapitre, vous allez :

- Comprendre le changement de paradigme de MLOps à LLMOps
- Le cycle de vie des LLM
- Les outils du cycle de vie
- La métrification et l'évaluation du cycle de vie

## Comprendre le Changement de Paradigme de MLOps à LLMOps

Les LLM sont un nouvel outil dans l'arsenal de l'Intelligence Artificielle, ils sont incroyablement puissants dans les tâches d'analyse et de génération pour les applications. Cependant, cette puissance a des conséquences sur la façon dont nous rationalisons les tâches d'IA et d'apprentissage automatique classique.

Avec cela, nous avons besoin d'un nouveau paradigme pour adapter cet outil de manière dynamique, avec les incitations appropriées. Nous pouvons catégoriser les anciennes applications d'IA comme des "Applications ML" et les nouvelles applications d'IA comme des "Applications GenAI" ou simplement "Applications IA", reflétant la technologie et les techniques courantes utilisées à l'époque. Cela modifie notre récit de plusieurs manières, regardez la comparaison suivante.

![Comparaison LLMOps vs. MLOps](../../../translated_images/01-llmops-shift.png?WT.38bc3eca81f659d83b17070d0a766bc3a9f13284b92c307e296915db4e683fcf.fr.mc_id=academic-105485-koreys)

Remarquez que dans LLMOps, nous nous concentrons davantage sur les développeurs d'applications, en utilisant les intégrations comme point clé, en utilisant "Models-as-a-Service" et en pensant aux points suivants pour les métriques.

- Qualité : Qualité de la réponse
- Dommage : IA Responsable
- Honnêteté : Ancrage de la réponse (Cela a-t-il du sens ? Est-ce correct ?)
- Coût : Budget de la solution
- Latence : Temps moyen de réponse par jeton

## Le Cycle de Vie des LLM

Tout d'abord, pour comprendre le cycle de vie et les modifications, notons l'infographie suivante.

![Infographie LLMOps](../../../translated_images/02-llmops.png?WT.32553adc9de4d89bb1d6a2f1f99d985457158a3be863e8e5dddc5e3dd074558a.fr.mc_id=academic-105485-koreys)

Comme vous pouvez le constater, cela diffère des cycles de vie habituels de MLOps. Les LLM ont de nombreuses nouvelles exigences, comme le Prompting, différentes techniques pour améliorer la qualité (Fine-Tuning, RAG, Meta-Prompts), une évaluation et une responsabilité différentes avec l'IA responsable, enfin, de nouvelles métriques d'évaluation (Qualité, Dommage, Honnêteté, Coût et Latence).

Par exemple, regardez comment nous concevons. En utilisant l'ingénierie des prompts pour expérimenter avec divers LLM afin d'explorer les possibilités de tester si leurs hypothèses pourraient être correctes.

Notez que ce n'est pas linéaire, mais des boucles intégrées, itératives et avec un cycle global.

Comment pourrions-nous explorer ces étapes ? Entrons dans le détail de la manière dont nous pourrions construire un cycle de vie.

![Flux de travail LLMOps](../../../translated_images/03-llm-stage-flows.png?WT.118920c8fd638f0879fe06c5e6eb9d91536e8b9c6bc56808ebed8706812f5391.fr.mc_id=academic-105485-koreys)

Cela peut sembler un peu compliqué, concentrons-nous d'abord sur les trois grandes étapes.

1. Idéation/Exploration : Exploration, ici nous pouvons explorer en fonction de nos besoins commerciaux. Prototypage, création d'un [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) et tester s'il est suffisamment efficace pour notre hypothèse.
2. Construction/Augmentation : Mise en œuvre, maintenant, nous commençons à évaluer pour des ensembles de données plus importants en mettant en œuvre des techniques, comme le Fine-tuning et le RAG, pour vérifier la robustesse de notre solution. Si ce n'est pas le cas, la réimplémentation, l'ajout de nouvelles étapes dans notre flux ou la restructuration des données, pourrait aider. Après avoir testé notre flux et notre échelle, si cela fonctionne et que nous vérifions nos métriques, il est prêt pour l'étape suivante.
3. Opérationnalisation : Intégration, maintenant ajout de systèmes de surveillance et d'alertes à notre système, déploiement et intégration de l'application à notre application.

Ensuite, nous avons le cycle global de gestion, axé sur la sécurité, la conformité et la gouvernance.

Félicitations, vous avez maintenant votre application IA prête à être utilisée et opérationnelle. Pour une expérience pratique, jetez un œil à la [Démo Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Maintenant, quels outils pourrions-nous utiliser ?

## Outils du Cycle de Vie

Pour les outils, Microsoft fournit la [Plateforme Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) et [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) pour faciliter et rendre votre cycle facile à mettre en œuvre et prêt à l'emploi.

La [Plateforme Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys), vous permet d'utiliser [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio est un portail web qui vous permet d'explorer des modèles, des exemples et des outils. Gérer vos ressources, les flux de développement UI et les options SDK/CLI pour le développement Code-First.

![Possibilités Azure AI](../../../translated_images/04-azure-ai-platform.png?WT.a39053c2efd7670298a79282658a9f5bf903dec5c1938b1a08cf45f1284e6ac0.fr.mc_id=academic-105485-koreys)

Azure AI, vous permet d'utiliser plusieurs ressources, pour gérer vos opérations, services, projets, besoins de recherche vectorielle et de bases de données.

![LLMOps avec Azure AI](../../../translated_images/05-llm-azure-ai-prompt.png?WT.9189130ce4f2e7c8667fc7c83c6b89236ce5c6361150f47104c27c105f04b487.fr.mc_id=academic-105485-koreys)

Construire, du Proof-of-Concept(POC) jusqu'aux applications à grande échelle avec PromptFlow :

- Concevoir et construire des applications depuis VS Code, avec des outils visuels et fonctionnels
- Tester et affiner vos applications pour une IA de qualité, en toute simplicité.
- Utiliser Azure AI Studio pour intégrer et itérer avec le cloud, pousser et déployer pour une intégration rapide.

![LLMOps avec PromptFlow](../../../translated_images/06-llm-promptflow.png?WT.e479dfedaa5f6ef7d36a11edbff74ac5579c3121ba0be0ee32eb5fc3eb17bd77.fr.mc_id=academic-105485-koreys)

## Super ! Continuez votre apprentissage !

Génial, apprenez maintenant comment nous structurons une application pour utiliser les concepts avec l'[Application Contoso Chat](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), pour voir comment le Cloud Advocacy ajoute ces concepts dans les démonstrations. Pour plus de contenu, consultez notre [session de présentation Ignite !
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Maintenant, consultez la leçon 15, pour comprendre comment [la génération augmentée par récupération et les bases de données vectorielles](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) impactent l'IA générative et permettent de créer des applications plus engageantes !

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.