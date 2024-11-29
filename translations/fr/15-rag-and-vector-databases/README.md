# Génération Augmentée par Récupération (RAG) et Bases de Données Vectorielles

[![Génération Augmentée par Récupération (RAG) et Bases de Données Vectorielles](../../../translated_images/15-lesson-banner.png?WT.ae1ec4b596c9c2b74121dd24c30143380d4789a9ef381276dbbc9fd5d7abc3d5.fr.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson15-gh?WT.mc_id=academic-105485-koreyst)

Dans la leçon sur les applications de recherche, nous avons brièvement appris à intégrer vos propres données dans les modèles de langage de grande taille (LLM). Dans cette leçon, nous allons approfondir les concepts de base de vos données dans votre application LLM, la mécanique du processus et les méthodes de stockage des données, y compris les embeddings et le texte.

> **Vidéo à venir bientôt**

## Introduction

Dans cette leçon, nous aborderons les points suivants :

- Une introduction à RAG, ce que c'est et pourquoi il est utilisé en intelligence artificielle (IA).

- Comprendre ce que sont les bases de données vectorielles et en créer une pour notre application.

- Un exemple pratique sur la façon d'intégrer RAG dans une application.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous serez capable de :

- Expliquer l'importance de RAG dans la récupération et le traitement des données.

- Configurer une application RAG et ancrer vos données à un LLM.

- Intégration efficace de RAG et des bases de données vectorielles dans les applications LLM.

## Notre scénario : améliorer nos LLMs avec nos propres données

Pour cette leçon, nous voulons ajouter nos propres notes dans la startup éducative, ce qui permet au chatbot d'obtenir plus d'informations sur les différents sujets. En utilisant les notes que nous avons, les apprenants pourront mieux étudier et comprendre les différents sujets, ce qui facilitera la révision pour leurs examens. Pour créer notre scénario, nous utiliserons :

- `Azure OpenAI:` le LLM que nous utiliserons pour créer notre chatbot

- `AI for beginners' lesson on Neural Networks` : ce sera les données sur lesquelles nous baserons notre LLM

- `Azure AI Search` et `Azure Cosmos DB:` base de données vectorielle pour stocker nos données et créer un index de recherche

Les utilisateurs pourront créer des quiz de pratique à partir de leurs notes, des fiches de révision et les résumer en aperçus concis. Pour commencer, regardons ce qu'est RAG et comment cela fonctionne :

## Génération Augmentée par Récupération (RAG)

Un chatbot alimenté par un LLM traite les invites des utilisateurs pour générer des réponses. Il est conçu pour être interactif et engage les utilisateurs sur une large gamme de sujets. Cependant, ses réponses sont limitées au contexte fourni et à ses données de formation de base. Par exemple, la coupure de connaissance de GPT-4 est septembre 2021, ce qui signifie qu'il n'a pas connaissance des événements survenus après cette période. De plus, les données utilisées pour entraîner les LLMs excluent les informations confidentielles telles que des notes personnelles ou le manuel produit d'une entreprise.

### Comment fonctionnent les RAGs (Génération Augmentée par Récupération)

![schéma montrant comment fonctionnent les RAGs](../../../translated_images/how-rag-works.png?WT.fde75879826c169b53e16dc0d0d6691172c75b314400f380d40a9f31244eba0e.fr.mc_id=academic-105485-koreyst)

Supposons que vous souhaitiez déployer un chatbot qui crée des quiz à partir de vos notes, vous aurez besoin d'une connexion à la base de connaissances. C'est là que RAG vient à la rescousse. Les RAGs fonctionnent comme suit :

- **Base de connaissances :** Avant la récupération, ces documents doivent être ingérés et prétraités, généralement en décomposant de grands documents en morceaux plus petits, en les transformant en embeddings de texte et en les stockant dans une base de données.

- **Requête utilisateur :** l'utilisateur pose une question

- **Récupération :** Lorsqu'un utilisateur pose une question, le modèle d'embedding récupère des informations pertinentes de notre base de connaissances pour fournir plus de contexte qui sera incorporé dans l'invite.

- **Génération augmentée :** le LLM améliore sa réponse en fonction des données récupérées. Cela permet à la réponse générée de ne pas seulement se baser sur les données pré-entraînées mais aussi sur des informations pertinentes du contexte ajouté. Les données récupérées sont utilisées pour augmenter les réponses du LLM. Le LLM retourne ensuite une réponse à la question de l'utilisateur.

![schéma montrant l'architecture des RAGs](../../../translated_images/encoder-decode.png?WT.80c3c9669a10e85d1f7e9dc7f7f0d416a71e16d2f8a6da93267e55cbfbddbf9f.fr.mc_id=academic-105485-koreyst)

L'architecture des RAGs est mise en œuvre en utilisant des transformers composés de deux parties : un encodeur et un décodeur. Par exemple, lorsqu'un utilisateur pose une question, le texte d'entrée est 'encodé' en vecteurs capturant le sens des mots et les vecteurs sont 'décodés' dans notre index de documents et génèrent un nouveau texte basé sur la requête utilisateur. Le LLM utilise à la fois un modèle encodeur-décodeur pour générer la sortie.

Deux approches lors de l'implémentation de RAG selon le document proposé : [Génération Augmentée par Récupération pour les tâches NLP intensives en connaissances](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sont :

- **_RAG-Sequence_** en utilisant des documents récupérés pour prédire la meilleure réponse possible à une requête utilisateur

- **RAG-Token** en utilisant des documents pour générer le prochain token, puis les récupérer pour répondre à la requête de l'utilisateur

### Pourquoi utiliseriez-vous les RAGs ? 

- **Richesse de l'information :** garantit que les réponses textuelles sont à jour et actuelles. Il améliore donc la performance sur les tâches spécifiques au domaine en accédant à la base de connaissances interne.

- Réduit la fabrication en utilisant des **données vérifiables** dans la base de connaissances pour fournir un contexte aux requêtes des utilisateurs.

- Il est **rentable** car ils sont plus économiques par rapport à l'ajustement fin d'un LLM.

## Création d'une base de connaissances

Notre application est basée sur nos données personnelles, c'est-à-dire, la leçon sur les réseaux neuronaux du curriculum AI For Beginners.

### Bases de données vectorielles

Une base de données vectorielle, contrairement aux bases de données traditionnelles, est une base de données spécialisée conçue pour stocker, gérer et rechercher des vecteurs intégrés. Elle stocke des représentations numériques de documents. Décomposer les données en embeddings numériques facilite la compréhension et le traitement des données par notre système d'IA.

Nous stockons nos embeddings dans des bases de données vectorielles car les LLMs ont une limite du nombre de tokens qu'ils acceptent en entrée. Comme vous ne pouvez pas passer l'intégralité des embeddings à un LLM, nous devrons les décomposer en morceaux et lorsqu'un utilisateur pose une question, les embeddings les plus proches de la question seront retournés avec l'invite. Le découpage réduit également les coûts sur le nombre de tokens passés à travers un LLM.

Parmi les bases de données vectorielles populaires, on trouve Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant et DeepLake. Vous pouvez créer un modèle Azure Cosmos DB en utilisant Azure CLI avec la commande suivante :

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Du texte aux embeddings

Avant de stocker nos données, nous devrons les convertir en embeddings vectoriels avant qu'elles ne soient stockées dans la base de données. Si vous travaillez avec de grands documents ou de longs textes, vous pouvez les découper en fonction des requêtes que vous attendez. Le découpage peut se faire au niveau de la phrase ou au niveau du paragraphe. Comme le découpage dérive le sens des mots autour d'eux, vous pouvez ajouter un autre contexte à un morceau, par exemple, en ajoutant le titre du document ou en incluant du texte avant ou après le morceau. Vous pouvez découper les données comme suit :

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Une fois découpé, nous pouvons alors intégrer notre texte en utilisant différents modèles d'embedding. Certains modèles que vous pouvez utiliser incluent : word2vec, ada-002 par OpenAI, Azure Computer Vision et bien d'autres. Le choix du modèle à utiliser dépendra des langues que vous utilisez, du type de contenu encodé (texte/images/audio), de la taille de l'entrée qu'il peut encoder et de la longueur de la sortie d'embedding.

Un exemple de texte intégré en utilisant le modèle `text-embedding-ada-002` d'OpenAI est :
![un embedding du mot chat](../../../translated_images/cat.png?WT.6f67a41409b2174c6f543273f4a9f8c38b227112a12831da3070e52f13e03818.fr.mc_id=academic-105485-koreyst)

## Récupération et recherche vectorielle

Lorsqu'un utilisateur pose une question, le récupérateur la transforme en un vecteur en utilisant l'encodeur de requête, il recherche ensuite dans notre index de recherche de documents les vecteurs pertinents dans le document qui sont liés à l'entrée. Une fois terminé, il convertit à la fois le vecteur d'entrée et les vecteurs de documents en texte et les passe à travers le LLM.

### Récupération

La récupération se produit lorsque le système essaie de trouver rapidement les documents de l'index qui satisfont les critères de recherche. L'objectif du récupérateur est d'obtenir des documents qui seront utilisés pour fournir un contexte et ancrer le LLM sur vos données.

Il existe plusieurs façons de réaliser une recherche dans notre base de données, telles que :

- **Recherche par mot-clé** - utilisée pour les recherches textuelles

- **Recherche sémantique** - utilise le sens sémantique des mots

- **Recherche vectorielle** - convertit les documents de texte en représentations vectorielles en utilisant des modèles d'embedding. La récupération sera effectuée en interrogeant les documents dont les représentations vectorielles sont les plus proches de la question de l'utilisateur.

- **Hybride** - une combinaison de recherche par mot-clé et de recherche vectorielle.

Un défi avec la récupération survient lorsqu'il n'y a pas de réponse similaire à la requête dans la base de données, le système renverra alors les meilleures informations qu'il peut obtenir, cependant, vous pouvez utiliser des tactiques telles que définir la distance maximale pour la pertinence ou utiliser une recherche hybride qui combine à la fois les mots-clés et la recherche vectorielle. Dans cette leçon, nous utiliserons la recherche hybride, une combinaison de recherche vectorielle et par mot-clé. Nous stockerons nos données dans un dataframe avec des colonnes contenant les morceaux ainsi que les embeddings.

### Similarité vectorielle

Le récupérateur recherchera dans la base de connaissances les embeddings qui sont proches les uns des autres, le voisin le plus proche, car ce sont des textes qui sont similaires. Dans le scénario où un utilisateur pose une requête, elle est d'abord intégrée puis associée à des embeddings similaires. La mesure courante utilisée pour trouver à quel point différents vecteurs sont similaires est la similarité cosinus, qui est basée sur l'angle entre deux vecteurs.

Nous pouvons mesurer la similarité en utilisant d'autres alternatives que nous pouvons utiliser, telles que la distance euclidienne qui est la ligne droite entre les points d'extrémité des vecteurs et le produit scalaire qui mesure la somme des produits des éléments correspondants de deux vecteurs.

### Index de recherche

Lors de la récupération, nous devrons construire un index de recherche pour notre base de connaissances avant d'effectuer une recherche. Un index stockera nos embeddings et pourra rapidement récupérer les morceaux les plus similaires, même dans une grande base de données. Nous pouvons créer notre index localement en utilisant :

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Reclassement

Une fois que vous avez interrogé la base de données, vous pourriez avoir besoin de trier les résultats des plus pertinents. Un LLM de reclassement utilise l'apprentissage automatique pour améliorer la pertinence des résultats de recherche en les ordonnant des plus pertinents. En utilisant Azure AI Search, le reclassement est effectué automatiquement pour vous en utilisant un reclassement sémantique. Un exemple de fonctionnement du reclassement en utilisant les voisins les plus proches :

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Tout rassembler

La dernière étape consiste à ajouter notre LLM dans le mélange pour pouvoir obtenir des réponses qui sont ancrées sur nos données. Nous pouvons l'implémenter comme suit :

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Évaluation de notre application

### Métriques d'évaluation

- Qualité des réponses fournies en veillant à ce qu'elles sonnent naturelles, fluides et humaines

- Enracinement des données : évaluation si la réponse provient des documents fournis

- Pertinence : évaluation si la réponse correspond et est liée à la question posée

- Fluidité - si la réponse a un sens grammatical

## Cas d'utilisation pour l'utilisation de RAG (Génération Augmentée par Récupération) et des bases de données vectorielles

Il existe de nombreux cas d'utilisation différents où les appels de fonction peuvent améliorer votre application, tels que :

- Questions et réponses : ancrer les données de votre entreprise à un chat qui peut être utilisé par les employés pour poser des questions.

- Systèmes de recommandation : où vous pouvez créer un système qui correspond aux valeurs les plus similaires, par exemple, films, restaurants et bien plus encore.

- Services de chatbot : vous pouvez stocker l'historique des conversations et personnaliser la conversation en fonction des données de l'utilisateur.

- Recherche d'images basée sur les embeddings vectoriels, utile lors de la reconnaissance d'images et de la détection d'anomalies.

## Résumé

Nous avons couvert les domaines fondamentaux de RAG, de l'ajout de nos données à l'application, la requête utilisateur et la sortie. Pour simplifier la création de RAG, vous pouvez utiliser des frameworks tels que Semanti Kernel, Langchain ou Autogen.

## Devoir

Pour poursuivre votre apprentissage de la Génération Augmentée par Récupération (RAG), vous pouvez construire :

- Construire un front-end pour l'application en utilisant le framework de votre choix

- Utiliser un framework, soit LangChain ou Semantic Kernel, et recréer votre application.

Félicitations pour avoir terminé la leçon 👏.

## L'apprentissage ne s'arrête pas ici, continuez le voyage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à améliorer vos connaissances en IA générative !

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations cruciales, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.