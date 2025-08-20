<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:14:30+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "fr"
}
-->
# Créer des applications de génération d’images

[![Créer des applications de génération d’images](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.fr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Les LLM ne servent pas uniquement à générer du texte. Il est également possible de créer des images à partir de descriptions textuelles. Disposer d’images comme modalité peut être très utile dans de nombreux domaines, de la MedTech à l’architecture, en passant par le tourisme, le développement de jeux, et bien plus encore. Dans ce chapitre, nous allons explorer les deux modèles de génération d’images les plus populaires : DALL-E et Midjourney.

## Introduction

Dans cette leçon, nous aborderons :

- La génération d’images et son utilité.
- DALL-E et Midjourney : ce qu’ils sont et comment ils fonctionnent.
- Comment créer une application de génération d’images.

## Objectifs d’apprentissage

À l’issue de cette leçon, vous serez capable de :

- Créer une application de génération d’images.
- Définir les limites de votre application avec des méta-prompts.
- Travailler avec DALL-E et Midjourney.

## Pourquoi créer une application de génération d’images ?

Les applications de génération d’images sont un excellent moyen d’explorer les capacités de l’IA générative. Elles peuvent être utilisées, par exemple, pour :

- **L’édition et la synthèse d’images**. Vous pouvez générer des images pour divers cas d’usage, comme l’édition ou la synthèse d’images.

- **Appliquées à différents secteurs**. Elles peuvent aussi servir à créer des images pour divers secteurs tels que la MedTech, le tourisme, le développement de jeux, et plus encore.

## Scénario : Edu4All

Dans le cadre de cette leçon, nous continuerons à travailler avec notre startup Edu4All. Les étudiants créeront des images pour leurs évaluations ; le choix des images leur revient, mais il pourrait s’agir d’illustrations pour leur propre conte, de la création d’un nouveau personnage pour leur histoire, ou d’une aide à la visualisation de leurs idées et concepts.

Voici ce que les étudiants d’Edu4All pourraient générer, par exemple, s’ils travaillent en classe sur des monuments :

![Edu4All startup, classe sur les monuments, Tour Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.fr.png)

avec un prompt comme

> "Chien à côté de la Tour Eiffel au lever du soleil"

## Qu’est-ce que DALL-E et Midjourney ?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) et [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sont deux des modèles de génération d’images les plus populaires, ils permettent d’utiliser des prompts pour créer des images.

### DALL-E

Commençons par DALL-E, un modèle d’IA générative qui crée des images à partir de descriptions textuelles.

> [DALL-E est une combinaison de deux modèles, CLIP et diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** est un modèle qui génère des embeddings, c’est-à-dire des représentations numériques des données, à partir d’images et de textes.

- **Diffused attention** est un modèle qui génère des images à partir de ces embeddings. DALL-E est entraîné sur un ensemble de données d’images et de textes et peut être utilisé pour créer des images à partir de descriptions textuelles. Par exemple, DALL-E peut générer une image d’un chat avec un chapeau, ou d’un chien avec une crête.

### Midjourney

Midjourney fonctionne de manière similaire à DALL-E, il génère des images à partir de prompts textuels. Midjourney peut aussi être utilisé pour créer des images avec des prompts comme « un chat avec un chapeau » ou « un chien avec une crête ».

![Image générée par Midjourney, pigeon mécanique](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)  
_Crédit image Wikipedia, image générée par Midjourney_

## Comment fonctionnent DALL-E et Midjourney

Commençons par [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E est un modèle d’IA générative basé sur l’architecture transformer avec un _transformer autorégressif_.

Un _transformer autorégressif_ définit comment un modèle génère des images à partir de descriptions textuelles : il génère un pixel à la fois, puis utilise les pixels générés pour créer le pixel suivant. Le processus passe par plusieurs couches dans un réseau de neurones, jusqu’à ce que l’image soit complète.

Grâce à ce procédé, DALL-E contrôle les attributs, objets, caractéristiques, et plus encore dans l’image qu’il génère. Cependant, DALL-E 2 et 3 offrent un contrôle encore plus précis sur l’image générée.

## Créer votre première application de génération d’images

Alors, que faut-il pour créer une application de génération d’images ? Vous aurez besoin des bibliothèques suivantes :

- **python-dotenv**, il est fortement recommandé d’utiliser cette bibliothèque pour garder vos secrets dans un fichier _.env_ séparé du code.
- **openai**, cette bibliothèque vous permettra d’interagir avec l’API OpenAI.
- **pillow**, pour manipuler les images en Python.
- **requests**, pour faciliter les requêtes HTTP.

1. Créez un fichier _.env_ avec le contenu suivant :

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Vous trouverez ces informations dans le portail Azure pour votre ressource, dans la section « Keys and Endpoint ».

1. Rassemblez les bibliothèques ci-dessus dans un fichier nommé _requirements.txt_ comme suit :

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Ensuite, créez un environnement virtuel et installez les bibliothèques :

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Sous Windows, utilisez les commandes suivantes pour créer et activer votre environnement virtuel :

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Ajoutez le code suivant dans un fichier nommé _app.py_ :

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.InvalidRequestError as err:
       print(err)

   ```

Expliquons ce code :

- Tout d’abord, nous importons les bibliothèques nécessaires, y compris OpenAI, dotenv, requests et Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Ensuite, nous chargeons les variables d’environnement depuis le fichier _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Puis, nous configurons l’endpoint, la clé pour l’API OpenAI, la version et le type.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Ensuite, nous générons l’image :

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Le code ci-dessus répond avec un objet JSON contenant l’URL de l’image générée. Nous pouvons utiliser cette URL pour télécharger l’image et la sauvegarder dans un fichier.

- Enfin, nous ouvrons l’image et utilisons le visualiseur d’images standard pour l’afficher :

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Plus de détails sur la génération d’image

Examinons plus en détail le code qui génère l’image :

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** est le texte utilisé pour générer l’image. Ici, nous utilisons le prompt « Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils ».
- **size** correspond à la taille de l’image générée. Ici, nous créons une image de 1024x1024 pixels.
- **n** est le nombre d’images générées. Ici, nous en générons deux.
- **temperature** est un paramètre qui contrôle l’aléa dans la sortie d’un modèle d’IA générative. La température varie entre 0 et 1, où 0 signifie que la sortie est déterministe et 1 que la sortie est aléatoire. La valeur par défaut est 0,7.

Il y a encore plus de choses que vous pouvez faire avec les images, que nous aborderons dans la section suivante.

## Capacités supplémentaires de la génération d’images

Vous avez vu jusqu’ici comment générer une image avec quelques lignes en Python. Cependant, il existe d’autres possibilités avec les images.

Vous pouvez également :

- **Effectuer des modifications**. En fournissant une image existante, un masque et un prompt, vous pouvez modifier une image. Par exemple, vous pouvez ajouter un élément à une partie de l’image. Imaginez notre image du lapin, vous pouvez lui ajouter un chapeau. Pour cela, vous fournissez l’image, un masque (identifiant la zone à modifier) et un prompt textuel indiquant ce qui doit être fait.

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  L’image de base ne contiendrait que le lapin, mais l’image finale aurait le chapeau sur le lapin.

- **Créer des variations**. L’idée est de prendre une image existante et de demander la création de variations. Pour créer une variation, vous fournissez une image, un prompt textuel et un code comme suit :

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Note : cette fonctionnalité est uniquement prise en charge par OpenAI.

## Température

La température est un paramètre qui contrôle l’aléa dans la sortie d’un modèle d’IA générative. La température varie entre 0 et 1, où 0 signifie que la sortie est déterministe et 1 que la sortie est aléatoire. La valeur par défaut est 0,7.

Voyons un exemple de fonctionnement de la température, en lançant ce prompt deux fois :

> Prompt : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Lapin sur un cheval tenant une sucette, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.fr.png)

Maintenant, lançons le même prompt une seconde fois pour voir que nous n’obtiendrons pas la même image deux fois :

![Image générée d’un lapin sur un cheval](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.fr.png)

Comme vous pouvez le voir, les images sont similaires, mais pas identiques. Essayons de changer la valeur de la température à 0,1 et observons ce qui se passe :

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Modifier la température

Essayons donc de rendre la réponse plus déterministe. Nous avons pu constater avec les deux images générées que la première montre un lapin et la seconde un cheval, donc les images varient beaucoup.

Modifions donc notre code pour fixer la température à 0, comme ceci :

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Lorsque vous exécutez ce code, vous obtenez ces deux images :

- ![Température 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.fr.png)
- ![Température 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.fr.png)

Ici, vous pouvez clairement voir que les images se ressemblent beaucoup plus.

## Comment définir les limites de votre application avec des méta-prompts

Avec notre démo, nous pouvons déjà générer des images pour nos clients. Cependant, il est nécessaire de définir certaines limites pour notre application.

Par exemple, nous ne voulons pas générer d’images inappropriées pour le travail ou pour les enfants.

Nous pouvons faire cela avec des _méta-prompts_. Les méta-prompts sont des prompts textuels utilisés pour contrôler la sortie d’un modèle d’IA générative. Par exemple, nous pouvons utiliser des méta-prompts pour garantir que les images générées sont sûres pour le travail ou adaptées aux enfants.

### Comment ça fonctionne ?

Alors, comment fonctionnent les méta-prompts ?

Les méta-prompts sont des prompts textuels placés avant le prompt principal, utilisés pour contrôler la sortie du modèle. Ils sont intégrés dans les applications pour encadrer la sortie du modèle, en encapsulant à la fois le prompt principal et le méta-prompt dans un seul prompt textuel.

Un exemple de méta-prompt serait le suivant :

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Voyons maintenant comment utiliser les méta-prompts dans notre démo.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO add request to generate image
```

À partir du prompt ci-dessus, vous pouvez voir que toutes les images générées prennent en compte le méta-prompt.

## Exercice – donnons aux étudiants les moyens d’agir

Nous avons présenté Edu4All au début de cette leçon. Il est maintenant temps de permettre aux étudiants de générer des images pour leurs évaluations.

Les étudiants créeront des images pour leurs évaluations contenant des monuments, le choix des monuments leur revenant. Ils sont invités à faire preuve de créativité pour placer ces monuments dans différents contextes.

## Solution

Voici une solution possible :

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.InvalidRequestError as err:
    print(err)
```

## Bravo ! Continuez à apprendre

Après avoir terminé cette leçon, consultez notre [collection d’apprentissage sur l’IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances en IA générative !

Rendez-vous à la leçon 10 où nous verrons comment [créer des applications IA avec peu de code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.