# Construire des applications de recherche

[![Introduction à l'IA générative et aux grands modèles de langage](../../../translated_images/08-lesson-banner.png?WT.38007baa37b3809836fefd9caf72cba7434d1d1e82074d170c2b066e3c7aa2d0.fr.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

> > _Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon_

Les LLMs ne se limitent pas aux chatbots et à la génération de texte. Il est également possible de créer des applications de recherche en utilisant les Embeddings. Les Embeddings sont des représentations numériques de données également connues sous le nom de vecteurs, et peuvent être utilisées pour la recherche sémantique de données.

Dans cette leçon, vous allez construire une application de recherche pour notre startup éducative. Notre startup est une organisation à but non lucratif qui fournit une éducation gratuite aux étudiants des pays en développement. Elle dispose d'un grand nombre de vidéos YouTube que les étudiants peuvent utiliser pour apprendre l'IA. Notre startup souhaite créer une application de recherche qui permette aux étudiants de rechercher une vidéo YouTube en tapant une question.

Par exemple, un étudiant pourrait taper 'Qu'est-ce que les Jupyter Notebooks ?' ou 'Qu'est-ce qu'Azure ML' et l'application de recherche renverra une liste de vidéos YouTube pertinentes à la question, et mieux encore, l'application de recherche fournira un lien vers l'endroit dans la vidéo où se trouve la réponse à la question.

## Introduction

Dans cette leçon, nous aborderons :

- Recherche sémantique vs recherche par mots-clés.
- Qu'est-ce que les Text Embeddings.
- Création d'un index de Text Embeddings.
- Recherche dans un index de Text Embeddings.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous serez capable de :

- Faire la différence entre la recherche sémantique et par mots-clés.
- Expliquer ce que sont les Text Embeddings.
- Créer une application utilisant les Embeddings pour rechercher des données.

## Pourquoi créer une application de recherche ?

Créer une application de recherche vous aidera à comprendre comment utiliser les Embeddings pour rechercher des données. Vous apprendrez également à créer une application de recherche que les étudiants pourront utiliser pour trouver rapidement des informations.

La leçon inclut un Index d'Embeddings des transcriptions YouTube de la chaîne [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) de Microsoft. Le AI Show est une chaîne YouTube qui vous enseigne l'IA et l'apprentissage automatique. L'Index d'Embeddings contient les Embeddings de chaque transcription YouTube jusqu'en octobre 2023. Vous utiliserez cet Index d'Embeddings pour construire une application de recherche pour notre startup. L'application de recherche renvoie un lien vers l'endroit dans la vidéo où se trouve la réponse à la question. C'est un excellent moyen pour les étudiants de trouver rapidement les informations dont ils ont besoin.

Voici un exemple de requête sémantique pour la question 'can you use rstudio with azure ml?'. Consultez l'url YouTube, vous verrez que l'url contient un horodatage qui vous amène à l'endroit dans la vidéo où se trouve la réponse à la question.

![Requête sémantique pour la question "can you use rstudio with Azure ML"](../../../translated_images/query-results.png?WT.c2bcab091b108e899efca56b2cd996ea8f95145c049888f52ef7495a2b7df665.fr.mc_id=academic-105485-koreyst)

## Qu'est-ce que la recherche sémantique ?

Vous vous demandez peut-être ce qu'est la recherche sémantique ? La recherche sémantique est une technique de recherche qui utilise la sémantique, ou le sens, des mots dans une requête pour renvoyer des résultats pertinents.

Voici un exemple de recherche sémantique. Disons que vous cherchez à acheter une voiture, vous pourriez chercher 'ma voiture de rêve', la recherche sémantique comprend que vous ne parlez pas de rêve à propos d'une voiture, mais que vous cherchez à acheter votre voiture de rêve. La recherche sémantique comprend votre intention et renvoie des résultats pertinents. L'alternative est une recherche littérale qui chercherait littéralement des rêves à propos de voitures et renverrait souvent des résultats non pertinents.

## Qu'est-ce que les Text Embeddings ?

[Les Text Embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) sont une technique de représentation de texte utilisée dans le [traitement du langage naturel](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Les Text Embeddings sont des représentations numériques sémantiques de texte. Les Embeddings sont utilisés pour représenter des données d'une manière facile à comprendre pour une machine. Il existe de nombreux modèles pour créer des Text Embeddings, dans cette leçon, nous nous concentrerons sur la génération d'embeddings en utilisant le modèle OpenAI Embedding.

Voici un exemple, imaginez que le texte suivant se trouve dans une transcription de l'un des épisodes de la chaîne YouTube AI Show :

```text
Today we are going to learn about Azure Machine Learning.
```

Nous passerions le texte à l'API OpenAI Embedding et elle renverrait l'embedding suivant composé de 1536 nombres, également appelé un vecteur. Chaque nombre dans le vecteur représente un aspect différent du texte. Pour plus de concision, voici les dix premiers nombres du vecteur.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Comment l'index d'Embedding est-il créé ?

L'index d'Embedding pour cette leçon a été créé avec une série de scripts Python. Vous trouverez les scripts ainsi que les instructions dans le [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) dans le dossier 'scripts' pour cette leçon. Vous n'avez pas besoin d'exécuter ces scripts pour compléter cette leçon car l'index d'Embedding est fourni pour vous.

Les scripts effectuent les opérations suivantes :

1. La transcription de chaque vidéo YouTube dans la playlist [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) est téléchargée.
2. En utilisant les [Fonctions OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), une tentative est faite pour extraire le nom de l'orateur des trois premières minutes de la transcription YouTube. Le nom de l'orateur pour chaque vidéo est stocké dans l'index d'Embedding nommé `embedding_index_3m.json`.
3. Le texte de la transcription est ensuite divisé en **segments de texte de 3 minutes**. Le segment inclut environ 20 mots se chevauchant du segment suivant pour s'assurer que l'Embedding pour le segment n'est pas coupé et pour fournir un meilleur contexte de recherche.
4. Chaque segment de texte est ensuite passé à l'API OpenAI Chat pour résumer le texte en 60 mots. Le résumé est également stocké dans l'index d'Embedding `embedding_index_3m.json`.
5. Enfin, le texte du segment est passé à l'API OpenAI Embedding. L'API Embedding renvoie un vecteur de 1536 nombres qui représentent le sens sémantique du segment. Le segment ainsi que le vecteur d'Embedding OpenAI sont stockés dans un index d'Embedding `embedding_index_3m.json`.

### Bases de données vectorielles

Pour simplifier la leçon, l'index d'Embedding est stocké dans un fichier JSON nommé `embedding_index_3m.json` et chargé dans un DataFrame Pandas. Cependant, en production, l'index d'Embedding serait stocké dans une base de données vectorielle telle que [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), pour n'en nommer que quelques-unes.

## Comprendre la similarité cosinus

Nous avons appris les embeddings de texte, l'étape suivante est d'apprendre comment utiliser les embeddings de texte pour rechercher des données et en particulier trouver les embeddings les plus similaires à une requête donnée en utilisant la similarité cosinus.

### Qu'est-ce que la similarité cosinus ?

La similarité cosinus est une mesure de similarité entre deux vecteurs, vous entendrez également cela appelé `nearest neighbor search`. Pour effectuer une recherche de similarité cosinus, vous devez _vectoriser_ le texte de la _requête_ en utilisant l'API OpenAI Embedding. Ensuite, calculez la _similarité cosinus_ entre le vecteur de requête et chaque vecteur dans l'index d'Embedding. Rappelez-vous, l'index d'Embedding a un vecteur pour chaque segment de texte de transcription YouTube. Enfin, triez les résultats par similarité cosinus et les segments de texte avec la plus haute similarité cosinus sont les plus similaires à la requête.

D'un point de vue mathématique, la similarité cosinus mesure le cosinus de l'angle entre deux vecteurs projetés dans un espace multidimensionnel. Cette mesure est bénéfique, car si deux documents sont éloignés par la distance euclidienne en raison de leur taille, ils pourraient encore avoir un angle plus petit entre eux et donc une similarité cosinus plus élevée. Pour plus d'informations sur les équations de similarité cosinus, consultez [Similarité cosinus](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Construire votre première application de recherche

Ensuite, nous allons apprendre à construire une application de recherche en utilisant les Embeddings. L'application de recherche permettra aux étudiants de rechercher une vidéo en tapant une question. L'application de recherche renverra une liste de vidéos pertinentes à la question. L'application de recherche renverra également un lien vers l'endroit dans la vidéo où se trouve la réponse à la question.

Cette solution a été construite et testée sur Windows 11, macOS et Ubuntu 22.04 en utilisant Python 3.10 ou une version ultérieure. Vous pouvez télécharger Python depuis [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Devoir - construire une application de recherche, pour permettre aux étudiants

Nous avons présenté notre startup au début de cette leçon. Il est maintenant temps de permettre aux étudiants de construire une application de recherche pour leurs évaluations.

Dans ce devoir, vous allez créer les Services Azure OpenAI qui seront utilisés pour construire l'application de recherche. Vous allez créer les Services Azure OpenAI suivants. Vous aurez besoin d'un abonnement Azure pour compléter ce devoir.

### Démarrer le Cloud Shell Azure

1. Connectez-vous au [portail Azure](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Sélectionnez l'icône Cloud Shell dans le coin supérieur droit du portail Azure.
3. Sélectionnez **Bash** pour le type d'environnement.

#### Créer un groupe de ressources

> Pour ces instructions, nous utilisons le groupe de ressources nommé "semantic-video-search" dans East US.
> Vous pouvez changer le nom du groupe de ressources, mais lorsque vous changez l'emplacement des ressources,
> vérifiez le [tableau de disponibilité des modèles](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Créer une ressource de Service Azure OpenAI

Depuis le Cloud Shell Azure, exécutez la commande suivante pour créer une ressource de Service Azure OpenAI.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Obtenir le point de terminaison et les clés pour utilisation dans cette application

Depuis le Cloud Shell Azure, exécutez les commandes suivantes pour obtenir le point de terminaison et les clés pour la ressource de Service Azure OpenAI.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Déployer le modèle d'Embedding OpenAI

Depuis le Cloud Shell Azure, exécutez la commande suivante pour déployer le modèle d'Embedding OpenAI.

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## Solution

Ouvrez le [notebook de solution](../../../08-building-search-applications/python/aoai-solution.ipynb) dans GitHub Codespaces et suivez les instructions dans le Jupyter Notebook.

Lorsque vous exécutez le notebook, vous serez invité à entrer une requête. La boîte de saisie ressemblera à ceci :

![Boîte de saisie pour que l'utilisateur saisisse une requête](../../../translated_images/notebook-search.png?WT.2910e3d34815aab8d713050521ac5fcb2436defe66fed016f56b95867eb12fbd.fr.mc_id=academic-105485-koreyst)

## Bon travail ! Continuez votre apprentissage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à développer vos connaissances en IA générative !

Rendez-vous à la leçon 9 où nous verrons comment [créer des applications de génération d'images](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst) !

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée par intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.