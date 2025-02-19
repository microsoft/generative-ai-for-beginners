# Création d'applications d'IA à faible code

[![Création d'applications d'IA à faible code](../../../translated_images/10-lesson-banner.png?WT.03212fed0693cf8837c727edc800942dbc5ef3a3036a8f7f399c6c08f6f59b92.fr.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

## Introduction

Maintenant que nous avons appris à créer des applications de génération d'images, parlons du faible code. L'IA générative peut être utilisée dans de nombreux domaines différents, y compris le faible code, mais qu'est-ce que le faible code et comment pouvons-nous y ajouter de l'IA ?

La création d'applications et de solutions est devenue plus facile pour les développeurs traditionnels et les non-développeurs grâce à l'utilisation des plateformes de développement à faible code. Ces plateformes permettent de créer des applications et des solutions avec peu ou pas de code, en fournissant un environnement de développement visuel qui permet de glisser-déposer des composants pour créer des applications et des solutions. Cela permet de créer des applications et des solutions plus rapidement et avec moins de ressources. Dans cette leçon, nous allons explorer en profondeur comment utiliser le faible code et comment améliorer le développement à faible code avec l'IA en utilisant Power Platform.

La Power Platform offre aux organisations la possibilité de donner à leurs équipes les moyens de créer leurs propres solutions à travers un environnement intuitif à faible code ou sans code. Cet environnement aide à simplifier le processus de création de solutions. Avec Power Platform, les solutions peuvent être créées en quelques jours ou semaines au lieu de mois ou années. Power Platform se compose de cinq produits clés : Power Apps, Power Automate, Power BI, Power Pages et Copilot Studio.

Cette leçon couvre :

- Introduction à l'IA générative dans Power Platform
- Introduction à Copilot et comment l'utiliser
- Utilisation de l'IA générative pour créer des applications et des flux dans Power Platform
- Compréhension des modèles d'IA dans Power Platform avec AI Builder

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Comprendre comment fonctionne Copilot dans Power Platform.

- Créer une application de suivi des devoirs pour notre startup éducative.

- Créer un flux de traitement de factures qui utilise l'IA pour extraire des informations des factures.

- Appliquer les meilleures pratiques lors de l'utilisation du modèle d'IA Create Text with GPT.

Les outils et technologies que vous utiliserez dans cette leçon sont :

- **Power Apps**, pour l'application de suivi des devoirs, qui offre un environnement de développement à faible code pour créer des applications permettant de suivre, gérer et interagir avec les données.

- **Dataverse**, pour stocker les données de l'application de suivi des devoirs où Dataverse fournira une plateforme de données à faible code pour stocker les données de l'application.

- **Power Automate**, pour le flux de traitement des factures où vous aurez un environnement de développement à faible code pour créer des flux de travail afin d'automatiser le processus de traitement des factures.

- **AI Builder**, pour le modèle d'IA de traitement des factures où vous utiliserez des modèles d'IA préconstruits pour traiter les factures de notre startup.

## L'IA générative dans Power Platform

Améliorer le développement et les applications à faible code avec l'IA générative est un axe clé pour Power Platform. L'objectif est de permettre à tout le monde de créer des applications, sites, tableaux de bord alimentés par l'IA et d'automatiser les processus avec l'IA, _sans nécessiter d'expertise en science des données_. Cet objectif est atteint en intégrant l'IA générative dans l'expérience de développement à faible code dans Power Platform sous la forme de Copilot et AI Builder.

### Comment cela fonctionne-t-il ?

Copilot est un assistant IA qui vous permet de créer des solutions Power Platform en décrivant vos exigences dans une série d'étapes conversationnelles en langage naturel. Vous pouvez par exemple demander à votre assistant IA de préciser quels champs votre application utilisera et il créera à la fois l'application et le modèle de données sous-jacent ou vous pourriez spécifier comment configurer un flux dans Power Automate.

Vous pouvez utiliser les fonctionnalités pilotées par Copilot comme une caractéristique dans les écrans de votre application pour permettre aux utilisateurs de découvrir des informations à travers des interactions conversationnelles.

AI Builder est une capacité d'IA à faible code disponible dans Power Platform qui vous permet d'utiliser des modèles d'IA pour vous aider à automatiser des processus et à prédire des résultats. Avec AI Builder, vous pouvez intégrer l'IA dans vos applications et flux qui se connectent à vos données dans Dataverse ou dans diverses sources de données cloud, telles que SharePoint, OneDrive ou Azure.

Copilot est disponible dans tous les produits de Power Platform : Power Apps, Power Automate, Power BI, Power Pages et Power Virtual Agents. AI Builder est disponible dans Power Apps et Power Automate. Dans cette leçon, nous nous concentrerons sur l'utilisation de Copilot et AI Builder dans Power Apps et Power Automate pour créer une solution pour notre startup éducative.

### Copilot dans Power Apps

Dans le cadre de Power Platform, Power Apps offre un environnement de développement à faible code pour créer des applications permettant de suivre, gérer et interagir avec les données. C'est une suite de services de développement d'applications avec une plateforme de données évolutive et la capacité de se connecter aux services cloud et aux données locales. Power Apps vous permet de créer des applications qui fonctionnent sur les navigateurs, les tablettes et les téléphones, et qui peuvent être partagées avec des collègues. Power Apps simplifie le développement d'applications avec une interface simple, de sorte que chaque utilisateur d'entreprise ou développeur professionnel peut créer des applications personnalisées. L'expérience de développement d'applications est également améliorée avec l'IA générative grâce à Copilot.

La fonction d'assistant IA Copilot dans Power Apps vous permet de décrire le type d'application dont vous avez besoin et les informations que vous souhaitez que votre application suive, collecte ou affiche. Copilot génère ensuite une application Canvas réactive basée sur votre description. Vous pouvez ensuite personnaliser l'application pour répondre à vos besoins. L'AI Copilot génère également et suggère une table Dataverse avec les champs nécessaires pour stocker les données que vous souhaitez suivre et quelques données d'exemple. Nous verrons ce qu'est Dataverse et comment vous pouvez l'utiliser dans Power Apps dans cette leçon plus tard. Vous pouvez ensuite personnaliser la table pour répondre à vos besoins en utilisant la fonction d'assistant AI Copilot à travers des étapes conversationnelles. Cette fonctionnalité est disponible directement depuis l'écran d'accueil de Power Apps.

### Copilot dans Power Automate

Dans le cadre de Power Platform, Power Automate permet aux utilisateurs de créer des flux de travail automatisés entre applications et services. Il aide à automatiser les processus métier répétitifs tels que la communication, la collecte de données et les approbations de décisions. Son interface simple permet aux utilisateurs de toutes compétences techniques (des débutants aux développeurs expérimentés) d'automatiser les tâches de travail. L'expérience de développement de flux de travail est également améliorée avec l'IA générative grâce à Copilot.

La fonction d'assistant IA Copilot dans Power Automate vous permet de décrire le type de flux dont vous avez besoin et les actions que vous souhaitez que votre flux effectue. Copilot génère ensuite un flux basé sur votre description. Vous pouvez ensuite personnaliser le flux pour répondre à vos besoins. L'AI Copilot génère également et suggère les actions nécessaires pour effectuer la tâche que vous souhaitez automatiser. Nous verrons ce que sont les flux et comment vous pouvez les utiliser dans Power Automate dans cette leçon plus tard. Vous pouvez ensuite personnaliser les actions pour répondre à vos besoins en utilisant la fonction d'assistant AI Copilot à travers des étapes conversationnelles. Cette fonctionnalité est disponible directement depuis l'écran d'accueil de Power Automate.

## Affectation : gérer les devoirs des étudiants et les factures pour notre startup, en utilisant Copilot

Notre startup propose des cours en ligne aux étudiants. La startup a connu une croissance rapide et a maintenant du mal à répondre à la demande pour ses cours. La startup vous a engagé en tant que développeur Power Platform pour les aider à créer une solution à faible code pour les aider à gérer les devoirs des étudiants et les factures. Leur solution devrait être capable de les aider à suivre et gérer les devoirs des étudiants via une application et à automatiser le processus de traitement des factures via un flux de travail. On vous a demandé d'utiliser l'IA générative pour développer la solution.

Lorsque vous commencez à utiliser Copilot, vous pouvez utiliser la [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) pour commencer avec les invites. Cette bibliothèque contient une liste d'invites que vous pouvez utiliser pour créer des applications et des flux avec Copilot. Vous pouvez également utiliser les invites de la bibliothèque pour avoir une idée de la façon de décrire vos exigences à Copilot.

### Créer une application de suivi des devoirs pour notre startup

Les éducateurs de notre startup ont du mal à suivre les devoirs des étudiants. Ils utilisaient une feuille de calcul pour suivre les devoirs, mais cela est devenu difficile à gérer à mesure que le nombre d'étudiants a augmenté. Ils vous ont demandé de créer une application qui les aidera à suivre et gérer les devoirs des étudiants. L'application devrait leur permettre d'ajouter de nouveaux devoirs, de voir les devoirs, de mettre à jour les devoirs et de supprimer les devoirs. L'application devrait également permettre aux éducateurs et aux étudiants de voir les devoirs qui ont été notés et ceux qui ne l'ont pas été.

Vous créerez l'application en utilisant Copilot dans Power Apps en suivant les étapes ci-dessous :

1. Accédez à l'écran d'accueil de [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Utilisez la zone de texte sur l'écran d'accueil pour décrire l'application que vous souhaitez créer. Par exemple, **_Je veux créer une application pour suivre et gérer les devoirs des étudiants_**. Cliquez sur le bouton **Envoyer** pour envoyer l'invite à l'AI Copilot.

![Décrire l'application que vous voulez créer](../../../translated_images/copilot-chat-prompt-powerapps.png?WT.30e5da1eee18fc179cbbe27b088aaa20d89624eaaed11a7750372ee8feb61af6.fr.mc_id=academic-105485-koreyst)

1. L'AI Copilot suggérera une table Dataverse avec les champs nécessaires pour stocker les données que vous souhaitez suivre et quelques données d'exemple. Vous pouvez ensuite personnaliser la table pour répondre à vos besoins en utilisant la fonction d'assistant AI Copilot à travers des étapes conversationnelles.

   > **Important** : Dataverse est la plateforme de données sous-jacente pour Power Platform. C'est une plateforme de données à faible code pour stocker les données de l'application. C'est un service entièrement géré qui stocke les données en toute sécurité dans le cloud Microsoft et est provisionné dans votre environnement Power Platform. Il est doté de capacités de gouvernance des données intégrées, telles que la classification des données, la traçabilité des données, le contrôle d'accès granulaire, et plus encore. Vous pouvez en savoir plus sur Dataverse [ici](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Champs suggérés dans votre nouvelle table](../../../translated_images/copilot-dataverse-table-powerapps.png?WT.d0158f12f6f02fdf31b4a056b0efbf5a64f49a2c2b6b9ea09b0f3a17d1189579.fr.mc_id=academic-105485-koreyst)

1. Les éducateurs veulent envoyer des emails aux étudiants qui ont soumis leurs devoirs pour les tenir informés de l'avancement de leurs devoirs. Vous pouvez utiliser Copilot pour ajouter un nouveau champ à la table pour stocker l'email de l'étudiant. Par exemple, vous pouvez utiliser l'invite suivante pour ajouter un nouveau champ à la table : **_Je veux ajouter une colonne pour stocker l'email de l'étudiant_**. Cliquez sur le bouton **Envoyer** pour envoyer l'invite à l'AI Copilot.

![Ajout d'un nouveau champ](../../../translated_images/copilot-new-column.png?WT.18e16fce13f73236f484dc1b59e3d8e83a80c1cdf40854077a3dc800df76c560.fr.mc_id=academic-105485-koreyst)

1. L'AI Copilot générera un nouveau champ et vous pourrez ensuite personnaliser le champ pour répondre à vos besoins.

1. Une fois que vous avez terminé avec la table, cliquez sur le bouton **Créer une application** pour créer l'application.

1. L'AI Copilot générera une application Canvas réactive basée sur votre description. Vous pouvez ensuite personnaliser l'application pour répondre à vos besoins.

1. Pour que les éducateurs envoient des emails aux étudiants, vous pouvez utiliser Copilot pour ajouter un nouvel écran à l'application. Par exemple, vous pouvez utiliser l'invite suivante pour ajouter un nouvel écran à l'application : **_Je veux ajouter un écran pour envoyer des emails aux étudiants_**. Cliquez sur le bouton **Envoyer** pour envoyer l'invite à l'AI Copilot.

![Ajout d'un nouvel écran via une instruction d'invite](../../../translated_images/copilot-new-screen.png?WT.afdf65429e4ef7b2eb58038fe91de6a3ebe7ca1d85e89c584efcb6da12abfdeb.fr.mc_id=academic-105485-koreyst)

1. L'AI Copilot générera un nouvel écran et vous pourrez ensuite personnaliser l'écran pour répondre à vos besoins.

1. Une fois que vous avez terminé avec l'application, cliquez sur le bouton **Enregistrer** pour enregistrer l'application.

1. Pour partager l'application avec les éducateurs, cliquez sur le bouton **Partager** puis cliquez à nouveau sur le bouton **Partager**. Vous pouvez ensuite partager l'application avec les éducateurs en saisissant leurs adresses email.

> **Votre devoir** : L'application que vous venez de créer est un bon début mais peut être améliorée. Avec la fonction email, les éducateurs peuvent uniquement envoyer des emails aux étudiants manuellement en devant saisir leurs emails. Pouvez-vous utiliser Copilot pour créer une automatisation qui permettra aux éducateurs d'envoyer automatiquement des emails aux étudiants lorsqu'ils soumettent leurs devoirs ? Votre indice est qu'avec la bonne invite, vous pouvez utiliser Copilot dans Power Automate pour créer cela.

### Créer une table d'informations sur les factures pour notre startup

L'équipe financière de notre startup a du mal à suivre les factures. Ils utilisaient une feuille de calcul pour suivre les factures, mais cela est devenu difficile à gérer à mesure que le nombre de factures a augmenté. Ils vous ont demandé de créer une table qui les aidera à stocker, suivre et gérer les informations des factures qu'ils ont reçues. La table devrait être utilisée pour créer une automatisation qui extraira toutes les informations des factures et les stockera dans la table. La table devrait également permettre à l'équipe financière de voir les factures qui ont été payées et celles qui ne l'ont pas été.

La Power Platform dispose d'une plateforme de données sous-jacente appelée Dataverse qui vous permet de stocker les données de vos applications et solutions. Dataverse fournit une plateforme de données à faible code pour stocker les données de l'application. C'est un service entièrement géré qui stocke les données en toute sécurité dans le cloud Microsoft et est provisionné dans votre environnement Power Platform. Il est doté de capacités de gouvernance des données intégrées, telles que la classification des données, la traçabilité des données, le contrôle d'accès granulaire, et plus encore. Vous pouvez en savoir plus [sur Dataverse ici](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Pourquoi devrions-nous utiliser Dataverse pour notre startup ? Les tables standard et personnalisées dans Dataverse offrent une option de stockage sécurisée et basée sur le cloud pour vos données. Les tables vous permettent de stocker différents types de données, de la même manière que vous pourriez utiliser plusieurs feuilles de calcul dans un seul classeur Excel. Vous pouvez utiliser des tables pour stocker des données spécifiques à votre organisation ou à vos besoins professionnels. Certains des avantages que notre startup obtiendra en utilisant Dataverse incluent, mais ne sont pas limités à :

- **Facile à gérer** : Les métadonnées et les données sont stockées dans le cloud, vous n'avez donc pas à vous soucier des détails de leur stockage ou gestion. Vous pouvez vous concentrer sur la création de vos applications et solutions.

- **Sécurisé** : Dataverse offre une option de stockage sécurisée et basée sur le cloud pour vos données. Vous pouvez contrôler qui a accès aux données dans vos tables et comment ils peuvent y accéder en utilisant la sécurité basée sur les rôles.

- **Métadonnées riches** : Les types de données et les relations sont utilisés directement dans Power Apps

- **Logique et validation** : Vous pouvez utiliser des règles métier, des champs calculés et des règles de validation pour appliquer la logique métier et maintenir l'exactitude des données.

Maintenant que vous savez ce qu'est Dataverse et pourquoi vous devriez l'utiliser, voyons comment vous pouvez utiliser Copilot pour créer une table dans Dataverse pour répondre aux exigences de notre équipe financière.

> **Note** : Vous utiliserez cette table dans la section suivante pour créer une automatisation qui extraira toutes les informations des factures et les stockera dans la table.
Pour créer une table dans Dataverse en utilisant Copilot, suivez les étapes ci-dessous : 1. Accédez à l'écran d'accueil de [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst). 2. Dans la barre de navigation de gauche, sélectionnez **Tables** puis cliquez sur **Décrire la nouvelle table**. ![Sélectionner nouvelle table](../../../translated_images/describe-new-table.png?WT.1934e0de36f3fb613a023df3dcca89ba55f5d8d118e59b997d3f58e346f9e5db.fr.mc_id=academic-105485-koreyst) 1. Sur l'écran **Décrire la nouvelle table**, utilisez la zone de texte pour décrire la table que vous souhaitez créer. Par exemple, **_Je veux créer une table pour stocker les informations des factures_**. Cliquez sur le bouton **Envoyer** pour envoyer l'invite à l'AI Copilot. ![Décrire la table](../../../translated_images/copilot-chat-prompt-dataverse.png?WT.07979e2dd2a5c59cdd535f61e0dc2e0ce9d964189f70230e2a39ebb574a877cd.fr.mc_id=academic-105485-koreyst) 1. L'AI Copilot suggérera une table Dataverse avec les champs nécessaires pour stocker les données que vous souhaitez suivre et quelques données d'exemple. Vous pouvez ensuite personnaliser la table pour répondre à vos besoins en utilisant la fonction d'assistant AI Copilot à travers des étapes conversationnelles. ![Table Dataverse suggérée](../../../translated_images/copilot-dataverse-table.png?WT.45e9dc11cec7f53431fef3c849a45a5a0e52bdd3d621de57ff591f9af23aae38.fr.mc_id=academic-105485-koreyst) 1. L'équipe financière souhaite envoyer un email au fournisseur pour les mettre à jour sur l'état actuel de leur facture. Vous pouvez utiliser Copilot pour ajouter un nouveau champ à la table pour stocker l'email du fournisseur. Par exemple, vous pouvez utiliser l'invite suivante pour ajouter un nouveau champ à la table : **_Je veux ajouter une colonne pour stocker l'email du fournisseur_**. Cliquez sur
of a text. - **Analyse de Sentiment** : Ce modèle détecte les sentiments positifs, négatifs, neutres ou mixtes dans le texte. - **Lecteur de Cartes de Visite** : Ce modèle extrait des informations des cartes de visite. - **Reconnaissance de Texte** : Ce modèle extrait du texte à partir d'images. - **Détection d'Objets** : Ce modèle détecte et extrait des objets à partir d'images. - **Traitement de Documents** : Ce modèle extrait des informations à partir de formulaires. - **Traitement de Factures** : Ce modèle extrait des informations à partir de factures. Avec les Modèles IA Personnalisés, vous pouvez intégrer votre propre modèle dans AI Builder afin qu'il fonctionne comme tout autre modèle personnalisé d'AI Builder, vous permettant de former le modèle avec vos propres données. Vous pouvez utiliser ces modèles pour automatiser des processus et prédire des résultats dans Power Apps et Power Automate. Lorsque vous utilisez votre propre modèle, certaines limitations s'appliquent. Lisez plus sur ces [limitations](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst). ![Modèles AI builder](../../../translated_images/ai-builder-models.png?WT.6c2f6abc64cc07d27103364f2cd8c4689956e168da9f58cf75e6ca3fb459ec20.fr.mc_id=academic-105485-koreyst)

## Devoir #2 - Construire un Flux de Traitement de Factures pour Notre Startup

L'équipe financière a du mal à traiter les factures. Elle utilise un tableur pour suivre les factures, mais cela devient difficile à gérer à mesure que le nombre de factures augmente. Elle vous a demandé de créer un flux de travail qui l'aidera à traiter les factures en utilisant l'IA. Le flux de travail devrait leur permettre d'extraire des informations des factures et de stocker ces informations dans une table Dataverse. Le flux de travail devrait également leur permettre d'envoyer un email à l'équipe financière avec les informations extraites.

Maintenant que vous savez ce qu'est AI Builder et pourquoi vous devriez l'utiliser, voyons comment vous pouvez utiliser le Modèle de Traitement de Factures d'AI Builder, que nous avons couvert plus tôt, pour construire un flux de travail qui aidera l'équipe financière à traiter les factures.

Pour construire un flux de travail qui aidera l'équipe financière à traiter les factures en utilisant le Modèle de Traitement de Factures d'AI Builder, suivez les étapes ci-dessous :

1. Accédez à l'écran d'accueil de [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).
2. Utilisez la zone de texte sur l'écran d'accueil pour décrire le flux de travail que vous souhaitez construire. Par exemple, **_Traiter une facture lorsqu'elle arrive dans ma boîte mail_**. Cliquez sur le bouton **Envoyer** pour envoyer l'invite au Copilot AI. ![Copilot power automate](../../../translated_images/copilot-chat-prompt-powerautomate.png?WT.f6341b68d42f7c600e636c97f6874ec548ea3575906434e5caa9b7fbabd1c284.fr.mc_id=academic-105485-koreyst)
3. Le Copilot AI vous proposera les actions nécessaires pour réaliser la tâche que vous souhaitez automatiser. Vous pouvez cliquer sur le bouton **Suivant** pour passer aux étapes suivantes.
4. À l'étape suivante, Power Automate vous demandera de configurer les connexions nécessaires pour le flux. Une fois terminé, cliquez sur le bouton **Créer un flux** pour créer le flux.
5. Le Copilot AI générera un flux et vous pourrez ensuite personnaliser le flux pour répondre à vos besoins.
6. Mettez à jour le déclencheur du flux et définissez le **Dossier** vers le dossier où les factures seront stockées. Par exemple, vous pouvez définir le dossier sur **Boîte de réception**. Cliquez sur **Afficher les options avancées** et réglez **Seulement avec pièces jointes** sur **Oui**. Cela garantira que le flux ne s'exécute que lorsqu'un email avec une pièce jointe est reçu dans le dossier.
7. Supprimez les actions suivantes du flux : **HTML vers texte**, **Composer**, **Composer 2**, **Composer 3** et **Composer 4** car vous ne les utiliserez pas.
8. Supprimez l'action **Condition** du flux car vous ne l'utiliserez pas. Cela devrait ressembler à la capture d'écran suivante : ![power automate, remove actions](../../../translated_images/powerautomate-remove-actions.png?WT.b7f06c5f7f24ed173de29f405e580c0bb414655560859cdbdf97b8c1803fe4c7.fr.mc_id=academic-105485-koreyst)
9. Cliquez sur le bouton **Ajouter une action** et recherchez **Dataverse**. Sélectionnez l'action **Ajouter une nouvelle ligne**.
10. Sur l'action **Extraire les informations des factures**, mettez à jour le **Fichier de Facture** pour pointer vers le **Contenu de la Pièce Jointe** de l'email. Cela garantira que le flux extrait les informations de la pièce jointe de la facture.
11. Sélectionnez la **Table** que vous avez créée précédemment. Par exemple, vous pouvez sélectionner la table **Informations sur la Facture**. Choisissez le contenu dynamique de l'action précédente pour remplir les champs suivants : - ID - Montant - Date - Nom - Statut - Réglez le **Statut** sur **En attente**. - Email du Fournisseur - Utilisez le contenu dynamique **De** du déclencheur **Lorsqu'un nouvel email arrive**. ![power automate add row](../../../translated_images/powerautomate-add-row.png?WT.05f8f2c79ce95248eb173d6644436a1220f143991a5f0e647e15b922a0e1a290.fr.mc_id=academic-105485-koreyst)
12. Une fois que vous avez terminé avec le flux, cliquez sur le bouton **Enregistrer** pour enregistrer le flux. Vous pouvez ensuite tester le flux en envoyant un email avec une facture au dossier que vous avez spécifié dans le déclencheur.

> **Votre devoir** : Le flux que vous venez de construire est un bon début, maintenant vous devez réfléchir à la façon dont vous pouvez construire une automatisation qui permettra à notre équipe financière d'envoyer un email au fournisseur pour les mettre à jour sur le statut actuel de leur facture. Votre indice : le flux doit s'exécuter lorsque le statut de la facture change.

## Utiliser un Modèle d'IA de Génération de Texte dans Power Automate

Le Modèle de Création de Texte avec GPT dans AI Builder vous permet de générer du texte basé sur une invite et est alimenté par le Microsoft Azure OpenAI Service. Avec cette capacité, vous pouvez incorporer la technologie GPT (Generative Pre-Trained Transformer) dans vos applications et flux pour construire une variété de flux automatisés et d'applications perspicaces.

Les modèles GPT subissent une formation intensive sur d'énormes quantités de données, leur permettant de produire du texte qui ressemble étroitement au langage humain lorsqu'on leur fournit une invite. Lorsqu'ils sont intégrés à l'automatisation des flux de travail, les modèles d'IA comme GPT peuvent être exploités pour rationaliser et automatiser un large éventail de tâches.

Par exemple, vous pouvez construire des flux pour générer automatiquement du texte pour une variété de cas d'utilisation, tels que : des brouillons d'emails, des descriptions de produits, et plus encore. Vous pouvez également utiliser le modèle pour générer du texte pour une variété d'applications, telles que des chatbots et des applications de service client qui permettent aux agents de service client de répondre efficacement et efficacement aux demandes des clients.

![create a prompt](../../../translated_images/create-prompt-gpt.png?WT.7838e7bf32dee9636286569283c29f2a7cd58f2e2e093cee611dfa66db61a6ca.fr.mc_id=academic-105485-koreyst)

Pour apprendre comment utiliser ce Modèle d'IA dans Power Automate, parcourez le module [Ajouter de l'intelligence avec AI Builder et GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Bon Travail ! Continuez Votre Apprentissage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage de l'IA Générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances en IA Générative !

Rendez-vous à la Leçon 11 où nous verrons comment [intégrer l'IA Générative avec l'Appel de Fonction](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst) !

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée par intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.