<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-06-25T22:14:32+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "fr"
}
-->
# Génération Augmentée par Récupération (RAG) et Bases de Données Vectorielles

Dans la leçon sur les applications de recherche, nous avons brièvement appris comment intégrer vos propres données dans les Modèles de Langage de Grande Taille (LLMs). Dans cette leçon, nous approfondirons les concepts de l'ancrage de vos données dans votre application LLM, la mécanique du processus et les méthodes de stockage des données, y compris les embeddings et le texte.

> **Vidéo à venir bientôt**

## Introduction

Dans cette leçon, nous couvrirons les points suivants :

- Une introduction à RAG, ce que c'est et pourquoi il est utilisé en intelligence artificielle (IA).

- Comprendre ce que sont les bases de données vectorielles et en créer une pour notre application.

- Un exemple pratique sur comment intégrer RAG dans une application.

## Objectifs d'apprentissage

Après avoir complété cette leçon, vous serez capable de :

- Expliquer l'importance de RAG dans la récupération et le traitement des données.

- Configurer une application RAG et ancrer vos données à un LLM.

- Intégration efficace de RAG et des Bases de Données Vectorielles dans les Applications LLM.

## Notre Scénario : améliorer nos LLMs avec nos propres données

Pour cette leçon, nous souhaitons ajouter nos propres notes dans la startup éducative, ce qui permet au chatbot d'obtenir plus d'informations sur les différents sujets. En utilisant les notes que nous avons, les apprenants pourront mieux étudier et comprendre les différents sujets, facilitant ainsi la révision de leurs examens. Pour créer notre scénario, nous utiliserons :

- `Azure OpenAI:` le LLM que nous utiliserons pour créer notre chatbot

- `AI for beginners' lesson on Neural Networks` : ce sera les données sur lesquelles nous ancrerons notre LLM

- `Azure AI Search` et `Azure Cosmos DB:` base de données vectorielle pour stocker nos données et créer un index de recherche

Les utilisateurs pourront créer des quiz pratiques à partir de leurs notes, des fiches de révision et les résumer en aperçus concis. Pour commencer, voyons ce qu'est RAG et comment cela fonctionne :

## Génération Augmentée par Récupération (RAG)

Un chatbot alimenté par un LLM traite les invites des utilisateurs pour générer des réponses. Il est conçu pour être interactif et engage les utilisateurs sur une large gamme de sujets. Cependant, ses réponses sont limitées au contexte fourni et à ses données d'entraînement de base. Par exemple, la date limite de connaissance de GPT-4 est septembre 2021, ce qui signifie qu'il manque de connaissances sur les événements survenus après cette période. De plus, les données utilisées pour entraîner les LLMs excluent les informations confidentielles telles que des notes personnelles ou le manuel de produit d'une entreprise.

### Comment fonctionnent les RAGs (Génération Augmentée par Récupération)

Supposons que vous vouliez déployer un chatbot qui crée des quiz à partir de vos notes, vous aurez besoin d'une connexion à la base de connaissances. C'est là que RAG vient à la rescousse. Les RAGs fonctionnent comme suit :

- **Base de connaissances :** Avant la récupération, ces documents doivent être ingérés et prétraités, généralement en décomposant de grands documents en plus petits morceaux, les transformant en embeddings de texte et les stockant dans une base de données.

- **Requête utilisateur :** l'utilisateur pose une question

- **Récupération :** Lorsqu'un utilisateur pose une question, le modèle d'embeddings récupère des informations pertinentes de notre base de connaissances pour fournir plus de contexte qui sera incorporé dans l'invite.

- **Génération augmentée :** le LLM améliore sa réponse en fonction des données récupérées. Cela permet à la réponse générée de ne pas être uniquement basée sur les données pré-entraînées mais aussi sur des informations pertinentes du contexte ajouté. Les données récupérées sont utilisées pour augmenter les réponses du LLM. Le LLM renvoie ensuite une réponse à la question de l'utilisateur.

L'architecture des RAGs est mise en œuvre en utilisant des transformateurs composés de deux parties : un encodeur et un décodeur. Par exemple, lorsqu'un utilisateur pose une question, le texte d'entrée est 'encodé' en vecteurs capturant le sens des mots et les vecteurs sont 'décodés' dans notre index de documents et génèrent un nouveau texte basé sur la requête de l'utilisateur. Le LLM utilise à la fois un modèle encodeur-décodeur pour générer la sortie.

Deux approches lors de la mise en œuvre de RAG selon le document proposé : [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sont :

- **_RAG-Sequence_** utilisant des documents récupérés pour prédire la meilleure réponse possible à une requête utilisateur

- **RAG-Token** utilisant des documents pour générer le prochain token, puis les récupérer pour répondre à la requête de l'utilisateur

### Pourquoi utiliseriez-vous les RAGs ?

- **Richesse de l'information :** assure que les réponses textuelles sont à jour et actuelles. Il améliore donc les performances sur les tâches spécifiques au domaine en accédant à la base de connaissances interne.

- Réduit la fabrication en utilisant des **données vérifiables** dans la base de connaissances pour fournir un contexte aux requêtes des utilisateurs.

- Il est **rentable** car ils sont plus économiques comparés à l'affinage d'un LLM

## Créer une base de connaissances

Notre application est basée sur nos données personnelles, c'est-à-dire la leçon sur le Réseau Neuronal du curriculum AI For Beginners.

### Bases de Données Vectorielles

Une base de données vectorielle, contrairement aux bases de données traditionnelles, est une base de données spécialisée conçue pour stocker, gérer et rechercher des vecteurs intégrés. Elle stocke des représentations numériques de documents. Décomposer les données en embeddings numériques facilite la compréhension et le traitement des données par notre système d'IA.

Nous stockons nos embeddings dans des bases de données vectorielles car les LLMs ont une limite du nombre de tokens qu'ils acceptent en entrée. Comme vous ne pouvez pas passer l'ensemble des embeddings à un LLM, nous devrons les décomposer en morceaux et lorsqu'un utilisateur pose une question, les embeddings les plus proches de la question seront retournés avec l'invite. Le découpage réduit également les coûts sur le nombre de tokens passés à travers un LLM.

Quelques bases de données vectorielles populaires incluent Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant et DeepLake. Vous pouvez créer un modèle Azure Cosmos DB en utilisant Azure CLI avec la commande suivante :

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Du texte aux embeddings

Avant de stocker nos données, nous devrons les convertir en embeddings vectoriels avant qu'elles ne soient stockées dans la base de données. Si vous travaillez avec de grands documents ou de longs textes, vous pouvez les découper en fonction des requêtes que vous attendez. Le découpage peut être fait au niveau de la phrase ou au niveau du paragraphe. Comme le découpage dérive des significations des mots qui les entourent, vous pouvez ajouter un autre contexte à un morceau, par exemple, en ajoutant le titre du document ou en incluant un texte avant ou après le morceau. Vous pouvez découper les données comme suit :

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

Une fois découpé, nous pouvons ensuite intégrer notre texte en utilisant différents modèles d'embeddings. Certains modèles que vous pouvez utiliser incluent : word2vec, ada-002 par OpenAI, Azure Computer Vision et bien d'autres. Le choix d'un modèle dépendra des langues que vous utilisez, du type de contenu encodé (texte/images/audio), de la taille de l'entrée qu'il peut encoder et de la longueur de la sortie d'embedding.

Un exemple de texte intégré en utilisant le modèle `text-embedding-ada-002` d'OpenAI est :
![un embedding du mot chat](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.fr.png)

## Récupération et Recherche Vectorielle

Lorsqu'un utilisateur pose une question, le récupérateur la transforme en vecteur à l'aide de l'encodeur de requêtes, il recherche ensuite dans notre index de recherche de documents les vecteurs pertinents dans le document qui sont liés à l'entrée. Une fois terminé, il convertit à la fois le vecteur d'entrée et les vecteurs de documents en texte et les passe à travers le LLM.

### Récupération

La récupération se produit lorsque le système essaie de trouver rapidement les documents de l'index qui satisfont aux critères de recherche. Le but du récupérateur est d'obtenir des documents qui seront utilisés pour fournir un contexte et ancrer le LLM sur vos données.

Il existe plusieurs façons d'effectuer une recherche dans notre base de données telles que :

- **Recherche par mots-clés** - utilisée pour les recherches textuelles

- **Recherche sémantique** - utilise le sens sémantique des mots

- **Recherche vectorielle** - convertit les documents de texte en représentations vectorielles à l'aide de modèles d'embeddings. La récupération sera effectuée en interrogeant les documents dont les représentations vectorielles sont les plus proches de la question de l'utilisateur.

- **Hybride** - une combinaison de recherche par mots-clés et recherche vectorielle.

Un défi avec la récupération survient lorsqu'il n'y a pas de réponse similaire à la requête dans la base de données, le système retournera alors la meilleure information qu'il peut obtenir, cependant, vous pouvez utiliser des tactiques comme définir la distance maximale pour la pertinence ou utiliser une recherche hybride qui combine à la fois des mots-clés et une recherche vectorielle. Dans cette leçon, nous utiliserons la recherche hybride, une combinaison de recherche vectorielle et de recherche par mots-clés. Nous stockerons nos données dans un dataframe avec des colonnes contenant les morceaux ainsi que les embeddings.

### Similarité Vectorielle

Le récupérateur recherchera dans la base de données de connaissances des embeddings qui sont proches les uns des autres, le plus proche voisin, car ce sont des textes similaires. Dans le scénario où un utilisateur pose une requête, elle est d'abord intégrée puis assortie avec des embeddings similaires. La mesure courante utilisée pour trouver à quel point différents vecteurs sont similaires est la similarité cosinus qui est basée sur l'angle entre deux vecteurs.

Nous pouvons mesurer la similarité en utilisant d'autres alternatives que nous pouvons utiliser sont la distance euclidienne qui est la ligne droite entre les points d'extrémité du vecteur et le produit scalaire qui mesure la somme des produits des éléments correspondants de deux vecteurs.

### Index de Recherche

Lors de la récupération, nous devrons construire un index de recherche pour notre base de connaissances avant d'effectuer une recherche. Un index stockera nos embeddings et pourra rapidement récupérer les morceaux les plus similaires même dans une grande base de données. Nous pouvons créer notre index localement en utilisant :

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Réordonnancement

Une fois que vous avez interrogé la base de données, vous devrez peut-être trier les résultats du plus pertinent. Un LLM de réordonnancement utilise l'apprentissage automatique pour améliorer la pertinence des résultats de recherche en les classant du plus pertinent. En utilisant Azure AI Search, le réordonnancement est effectué automatiquement pour vous à l'aide d'un réordonnateur sémantique. Un exemple de la façon dont le réordonnancement fonctionne en utilisant les plus proches voisins :

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

## Mettre tout ensemble

La dernière étape consiste à ajouter notre LLM dans le mélange pour pouvoir obtenir des réponses qui sont ancrées sur nos données. Nous pouvons le mettre en œuvre comme suit :

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

### Indicateurs d'Évaluation

- Qualité des réponses fournies en s'assurant qu'elles semblent naturelles, fluides et humaines

- Ancrage des données : évaluation si la réponse provient des documents fournis

- Pertinence : évaluation si la réponse correspond et est liée à la question posée

- Fluidité - si la réponse a un sens grammatical

## Cas d'Utilisation pour l'utilisation de RAG (Génération Augmentée par Récupération) et des bases de données vectorielles

Il existe de nombreux cas d'utilisation différents où les appels de fonction peuvent améliorer votre application comme :

- Questions et Réponses : ancrer les données de votre entreprise à un chat qui peut être utilisé par les employés pour poser des questions.

- Systèmes de Recommandation : où vous pouvez créer un système qui correspond aux valeurs les plus similaires, par exemple, films, restaurants et bien plus encore.

- Services de Chatbot : vous pouvez stocker l'historique des conversations et personnaliser la conversation en fonction des données utilisateur.

- Recherche d'images basée sur les embeddings vectoriels, utile lors de la reconnaissance d'images et de la détection d'anomalies.

## Résumé

Nous avons couvert les domaines fondamentaux de RAG depuis l'ajout de nos données à l'application, la requête utilisateur et la sortie. Pour simplifier la création de RAG, vous pouvez utiliser des frameworks tels que Semanti Kernel, Langchain ou Autogen.

## Devoir

Pour continuer votre apprentissage de la Génération Augmentée par Récupération (RAG), vous pouvez construire :

- Créer un front-end pour l'application en utilisant le framework de votre choix

- Utiliser un framework, soit LangChain ou Semantic Kernel, et recréer votre application.

Félicitations pour avoir terminé la leçon 👏.

## L'apprentissage ne s'arrête pas ici, continuez le voyage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage en IA Générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à améliorer vos connaissances en IA Générative !

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.