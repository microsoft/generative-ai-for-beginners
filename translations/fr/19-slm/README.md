```markdown
# Introduction aux petits modèles de langage pour l'IA générative pour les débutants

L'IA générative est un domaine fascinant de l'intelligence artificielle qui se concentre sur la création de systèmes capables de générer de nouveaux contenus. Ce contenu peut aller du texte et des images à la musique et même à des environnements virtuels entiers. L'une des applications les plus passionnantes de l'IA générative se trouve dans le domaine des modèles de langage.

## Que sont les petits modèles de langage ?

Un petit modèle de langage (SLM) représente une variante réduite d'un grand modèle de langage (LLM), exploitant de nombreux principes architecturaux et techniques des LLM, tout en affichant une empreinte computationnelle significativement réduite. Les SLM sont un sous-ensemble de modèles de langage conçus pour générer du texte ressemblant à celui des humains. Contrairement à leurs homologues plus grands, tels que GPT-4, les SLM sont plus compacts et efficaces, ce qui les rend idéaux pour des applications où les ressources informatiques sont limitées. Malgré leur taille plus petite, ils peuvent encore accomplir une variété de tâches. Typiquement, les SLM sont construits en compressant ou en distillant des LLM, dans le but de conserver une partie substantielle des fonctionnalités et des capacités linguistiques du modèle original. Cette réduction de la taille du modèle diminue la complexité globale, rendant les SLM plus efficaces en termes d'utilisation de la mémoire et de besoins informatiques. Malgré ces optimisations, les SLM peuvent encore accomplir une large gamme de tâches de traitement du langage naturel (NLP) :

- Génération de texte : Création de phrases ou de paragraphes cohérents et contextuellement pertinents.
- Complétion de texte : Prédiction et complétion de phrases à partir d'une invite donnée.
- Traduction : Conversion de texte d'une langue à une autre.
- Résumé : Condensation de longs textes en résumés plus courts et plus digestes.

Bien qu'avec quelques compromis en termes de performance ou de profondeur de compréhension par rapport à leurs homologues plus grands.

## Comment fonctionnent les petits modèles de langage ?

Les SLM sont entraînés sur de vastes quantités de données textuelles. Pendant l'entraînement, ils apprennent les motifs et structures du langage, leur permettant de générer du texte à la fois grammaticalement correct et contextuellement approprié. Le processus d'entraînement implique :

- Collecte de données : Rassembler de grands ensembles de données textuelles à partir de diverses sources.
- Prétraitement : Nettoyer et organiser les données pour les rendre adaptées à l'entraînement.
- Entraînement : Utiliser des algorithmes d'apprentissage automatique pour enseigner au modèle comment comprendre et générer du texte.
- Ajustement fin : Ajuster le modèle pour améliorer sa performance sur des tâches spécifiques.

Le développement des SLM s'aligne sur le besoin croissant de modèles pouvant être déployés dans des environnements à ressources limitées, tels que les appareils mobiles ou les plateformes de calcul en périphérie, où les LLM à grande échelle peuvent être peu pratiques en raison de leurs lourdes exigences en ressources. En se concentrant sur l'efficacité, les SLM équilibrent performance et accessibilité, permettant une application plus large à travers divers domaines.

![slm](../../../translated_images/slm.png?WT.85221b66c3ce1b5e21e84c783c7ba31848501cd5c9557bb7fdf13173edafd675.fr.mc_id=academic-105485-koreyst)

## Objectifs d'apprentissage

Dans cette leçon, nous espérons introduire la connaissance des SLM et la combiner avec Microsoft Phi-3 pour explorer différents scénarios dans le contenu textuel, la vision et MoE. À la fin de cette leçon, vous devriez être capable de répondre aux questions suivantes :

- Qu'est-ce qu'un SLM
- Quelle est la différence entre SLM et LLM
- Qu'est-ce que la famille Microsoft Phi-3/3.5
- Comment inférer la famille Microsoft Phi-3/3.5

Prêt ? Commençons.

## Les distinctions entre les grands modèles de langage (LLM) et les petits modèles de langage (SLM)

Les LLM et les SLM sont tous deux construits sur des principes fondamentaux de l'apprentissage automatique probabiliste, suivant des approches similaires dans leur conception architecturale, leurs méthodologies d'entraînement, leurs processus de génération de données et leurs techniques d'évaluation de modèles. Cependant, plusieurs facteurs clés différencient ces deux types de modèles.

## Applications des petits modèles de langage

Les SLM ont une large gamme d'applications, notamment :

- Chatbots : Fournir un support client et interagir avec les utilisateurs de manière conversationnelle.
- Création de contenu : Aider les écrivains en générant des idées ou même en rédigeant des articles entiers.
- Éducation : Aider les étudiants avec des devoirs d'écriture ou l'apprentissage de nouvelles langues.
- Accessibilité : Créer des outils pour les personnes handicapées, tels que les systèmes de synthèse vocale.

**Taille**

Une distinction principale entre les LLM et les SLM réside dans l'échelle des modèles. Les LLM, tels que ChatGPT (GPT-4), peuvent comprendre environ 1,76 trillion de paramètres, tandis que les SLM open-source comme Mistral 7B sont conçus avec un nombre de paramètres significativement inférieur — environ 7 milliards. Cette disparité est principalement due à des différences dans l'architecture des modèles et les processus d'entraînement. Par exemple, ChatGPT utilise un mécanisme d'auto-attention dans un cadre encodeur-décodeur, tandis que Mistral 7B utilise une attention à fenêtre glissante, ce qui permet un entraînement plus efficace dans un modèle uniquement décodeur. Cette variance architecturale a des implications profondes pour la complexité et la performance de ces modèles.

**Compréhension**

Les SLM sont généralement optimisés pour la performance dans des domaines spécifiques, ce qui les rend très spécialisés mais potentiellement limités dans leur capacité à fournir une compréhension contextuelle large à travers de multiples domaines de connaissance. En revanche, les LLM visent à simuler une intelligence semblable à celle des humains à un niveau plus complet. Entraînés sur de vastes ensembles de données diversifiées, les LLM sont conçus pour bien performer à travers une variété de domaines, offrant une plus grande polyvalence et adaptabilité. Par conséquent, les LLM sont plus adaptés à une gamme plus large de tâches en aval, telles que le traitement du langage naturel et la programmation.

**Calcul**

L'entraînement et le déploiement des LLM sont des processus gourmands en ressources, nécessitant souvent une infrastructure informatique significative, y compris des clusters de GPU à grande échelle. Par exemple, entraîner un modèle comme ChatGPT à partir de zéro peut nécessiter des milliers de GPU sur de longues périodes. En revanche, les SLM, avec leur nombre de paramètres plus petit, sont plus accessibles en termes de ressources informatiques. Des modèles comme Mistral 7B peuvent être entraînés et exécutés sur des machines locales équipées de capacités GPU modérées, bien que l'entraînement nécessite encore plusieurs heures sur plusieurs GPU.

**Biais**

Le biais est un problème connu dans les LLM, principalement en raison de la nature des données d'entraînement. Ces modèles s'appuient souvent sur des données brutes et librement disponibles sur Internet, qui peuvent sous-représenter ou mal représenter certains groupes, introduire un étiquetage erroné ou refléter des biais linguistiques influencés par des dialectes, des variations géographiques et des règles grammaticales. De plus, la complexité des architectures LLM peut involontairement exacerber le biais, qui peut passer inaperçu sans un ajustement fin attentif. D'un autre côté, les SLM, étant entraînés sur des ensembles de données plus restreints et spécifiques à un domaine, sont intrinsèquement moins susceptibles à de tels biais, bien qu'ils n'en soient pas immunisés.

**Inférence**

La taille réduite des SLM leur confère un avantage significatif en termes de vitesse d'inférence, leur permettant de générer des sorties efficacement sur du matériel local sans avoir besoin d'un traitement parallèle étendu. En revanche, les LLM, en raison de leur taille et de leur complexité, nécessitent souvent des ressources de calcul parallèles substantielles pour atteindre des temps d'inférence acceptables. La présence de plusieurs utilisateurs simultanés ralentit encore les temps de réponse des LLM, surtout lorsqu'ils sont déployés à grande échelle.

En résumé, bien que les LLM et les SLM partagent une base fondamentale dans l'apprentissage automatique, ils diffèrent significativement en termes de taille de modèle, de besoins en ressources, de compréhension contextuelle, de susceptibilité au biais et de vitesse d'inférence. Ces distinctions reflètent leur aptitude respective à différents cas d'utilisation, les LLM étant plus polyvalents mais gourmands en ressources, et les SLM offrant une efficacité plus spécifique au domaine avec des exigences computationnelles réduites.

***Note : Dans ce chapitre, nous introduirons les SLM en utilisant Microsoft Phi-3 / 3.5 comme exemple.***

## Présentation de la famille Phi-3 / Phi-3.5

La famille Phi-3 / 3.5 cible principalement les scénarios d'application de texte, de vision et d'agent (MoE) :

### Phi-3 / 3.5 Instruct

Principalement pour la génération de texte, la complétion de chat et l'extraction d'informations de contenu, etc.

**Phi-3-mini**

Le modèle de langage 3.8B est disponible sur Microsoft Azure AI Studio, Hugging Face et Ollama. Les modèles Phi-3 surpassent significativement les modèles de langage de taille égale et supérieure sur des critères clés (voir les chiffres de référence ci-dessous, des chiffres plus élevés sont meilleurs). Phi-3-mini surpasse des modèles deux fois plus grands, tandis que Phi-3-small et Phi-3-medium surpassent des modèles plus grands, y compris GPT-3.5

**Phi-3-small & medium**

Avec seulement 7 milliards de paramètres, Phi-3-small bat GPT-3.5T sur une variété de critères de langage, de raisonnement, de codage et de mathématiques. Le Phi-3-medium avec 14 milliards de paramètres continue cette tendance et surpasse le Gemini 1.0 Pro.

**Phi-3.5-mini**

Nous pouvons le considérer comme une mise à niveau de Phi-3-mini. Bien que les paramètres restent inchangés, il améliore la capacité à prendre en charge plusieurs langues (Prise en charge de plus de 20 langues : arabe, chinois, tchèque, danois, néerlandais, anglais, finnois, français, allemand, hébreu, hongrois, italien, japonais, coréen, norvégien, polonais, portugais, russe, espagnol, suédois, thaï, turc, ukrainien) et ajoute un support plus fort pour le long contexte. Phi-3.5-mini avec 3.8 milliards de paramètres surpasse les modèles de langage de même taille et est à égalité avec des modèles deux fois plus grands.

### Phi-3 / 3.5 Vision

Nous pouvons considérer le modèle Instruct de Phi-3/3.5 comme la capacité de Phi à comprendre, et Vision est ce qui donne à Phi les yeux pour comprendre le monde.

**Phi-3-Vision**

Phi-3-vision, avec seulement 4.2 milliards de paramètres, continue cette tendance et surpasse des modèles plus grands tels que Claude-3 Haiku et Gemini 1.0 Pro V sur les tâches de raisonnement visuel général, OCR, et de compréhension de tableaux et de diagrammes.

**Phi-3.5-Vision**

Phi-3.5-Vision est également une mise à niveau de Phi-3-Vision, ajoutant la prise en charge de plusieurs images. Vous pouvez le considérer comme une amélioration de la vision, non seulement vous pouvez voir des images, mais aussi des vidéos. Phi-3.5-vision surpasse des modèles plus grands tels que Claude-3.5 Sonnet et Gemini 1.5 Flash sur les tâches de compréhension OCR, de tableaux et de graphiques et est à égalité sur les tâches de raisonnement en connaissances visuelles générales. Prise en charge de l'entrée multi-images, c'est-à-dire effectuer un raisonnement sur plusieurs images d'entrée

### Phi-3.5-MoE

***Mixture of Experts (MoE)*** permet aux modèles d'être préentraînés avec beaucoup moins de calcul, ce qui signifie que vous pouvez considérablement augmenter la taille du modèle ou de l'ensemble de données avec le même budget de calcul qu'un modèle dense. En particulier, un modèle MoE devrait atteindre la même qualité que son homologue dense beaucoup plus rapidement pendant le préentraînement. Phi-3.5-MoE comprend 16 modules d'experts de 3.8 milliards. Phi-3.5-MoE avec seulement 6.6 milliards de paramètres actifs atteint un niveau similaire de raisonnement, de compréhension du langage et de mathématiques que des modèles beaucoup plus grands

Nous pouvons utiliser le modèle de la famille Phi-3/3.5 en fonction de différents scénarios. Contrairement aux LLM, vous pouvez déployer Phi-3/3.5-mini ou Phi-3/3.5-Vision sur des appareils en périphérie.

## Comment utiliser les modèles de la famille Phi-3/3.5

Nous espérons utiliser Phi-3/3.5 dans différents scénarios. Ensuite, nous utiliserons Phi-3/3.5 en fonction de différents scénarios.

![phi3](../../../translated_images/phi3.png?WT.0d1077c4470f7b6eef536aba4426fa8df26762844164cc3883d455ab5251bad1.fr.mc_id=academic-105485-koreyst)

### Différence d'inférence

API du Cloud

**Modèles GitHub**

Modèles GitHub
```


**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations cruciales, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.