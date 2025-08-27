<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T13:32:41+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "fr"
}
-->
# Créer des applications de génération d’images

[![Créer des applications de génération d’images](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.fr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Les LLM ne se limitent pas à la génération de texte. Il est aussi possible de générer des images à partir de descriptions textuelles. Disposer d’images comme modalité peut s’avérer très utile dans de nombreux domaines, comme la MedTech, l’architecture, le tourisme, le développement de jeux, et bien d’autres. Dans ce chapitre, nous allons explorer les deux modèles de génération d’images les plus populaires : DALL-E et Midjourney.

## Introduction

Dans cette leçon, nous allons aborder :

- La génération d’images et son utilité.
- DALL-E et Midjourney : ce qu’ils sont et comment ils fonctionnent.
- Comment créer une application de génération d’images.

## Objectifs d’apprentissage

Après avoir terminé cette leçon, vous serez capable de :

- Créer une application de génération d’images.
- Définir des limites pour votre application grâce aux métaprompts.
- Travailler avec DALL-E et Midjourney.

## Pourquoi créer une application de génération d’images ?

Les applications de génération d’images sont un excellent moyen d’explorer les capacités de l’IA générative. Elles peuvent être utilisées, par exemple, pour :

- **Édition et synthèse d’images**. Vous pouvez générer des images pour de nombreux cas d’usage, comme l’édition ou la synthèse d’images.

- **Utilisation dans divers secteurs**. Elles peuvent aussi servir à générer des images pour différents secteurs comme la MedTech, le tourisme, le développement de jeux, etc.

## Scénario : Edu4All

Dans le cadre de cette leçon, nous allons continuer à travailler avec notre startup, Edu4All. Les élèves vont créer des images pour leurs évaluations ; le choix des images leur appartient, mais il peut s’agir d’illustrations pour leur propre conte, de la création d’un nouveau personnage pour leur histoire, ou encore d’illustrations pour visualiser leurs idées et concepts.

Voici, par exemple, ce que les élèves d’Edu4All pourraient générer s’ils travaillent en classe sur les monuments :

![Startup Edu4All, cours sur les monuments, Tour Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.fr.png)

en utilisant une consigne comme

> « Chien à côté de la Tour Eiffel au lever du soleil »

## Qu’est-ce que DALL-E et Midjourney ?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) et [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sont deux des modèles de génération d’images les plus populaires. Ils permettent de générer des images à partir de consignes textuelles.

### DALL-E

Commençons par DALL-E, qui est un modèle d’IA générative capable de créer des images à partir de descriptions textuelles.

> [DALL-E est une combinaison de deux modèles, CLIP et attention diffusée](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** est un modèle qui génère des embeddings, c’est-à-dire des représentations numériques de données, à partir d’images et de texte.

- **Attention diffusée** est un modèle qui génère des images à partir d’embeddings. DALL-E est entraîné sur un jeu de données d’images et de textes, et peut être utilisé pour générer des images à partir de descriptions textuelles. Par exemple, DALL-E peut générer des images d’un chat avec un chapeau, ou d’un chien avec une crête.

### Midjourney

Midjourney fonctionne de façon similaire à DALL-E : il génère des images à partir de consignes textuelles. Midjourney peut aussi être utilisé pour générer des images avec des prompts comme « un chat avec un chapeau » ou « un chien avec une crête ».

![Image générée par Midjourney, pigeon mécanique](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédit image Wikipedia, image générée par Midjourney_

## Comment fonctionnent DALL-E et Midjourney

Commençons par [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E est un modèle d’IA générative basé sur l’architecture transformer avec un _transformer autorégressif_.

Un _transformer autorégressif_ définit la façon dont un modèle génère des images à partir de descriptions textuelles : il génère un pixel à la fois, puis utilise les pixels générés pour produire le pixel suivant. Ce processus passe par plusieurs couches d’un réseau de neurones, jusqu’à ce que l’image soit complète.

Grâce à ce procédé, DALL-E contrôle les attributs, objets, caractéristiques, etc. dans l’image générée. Cependant, DALL-E 2 et 3 offrent un contrôle encore plus poussé sur l’image produite.

## Créer votre première application de génération d’images

Alors, que faut-il pour créer une application de génération d’images ? Vous aurez besoin des bibliothèques suivantes :

- **python-dotenv** : il est fortement recommandé d’utiliser cette bibliothèque pour conserver vos secrets dans un fichier _.env_ séparé du code.
- **openai** : cette bibliothèque vous permet d’interagir avec l’API OpenAI.
- **pillow** : pour manipuler des images en Python.
- **requests** : pour effectuer des requêtes HTTP.

## Créer et déployer un modèle Azure OpenAI

Si ce n’est pas déjà fait, suivez les instructions sur la page [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)
pour créer une ressource et un modèle Azure OpenAI. Sélectionnez DALL-E 3 comme modèle.  

## Créer l’application

1. Créez un fichier _.env_ avec le contenu suivant :

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Vous trouverez ces informations dans le portail Azure OpenAI Foundry, section « Deployments » de votre ressource.

1. Rassemblez les bibliothèques ci-dessus dans un fichier _requirements.txt_ comme ceci :

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
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
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

Explications du code :

- D’abord, on importe les bibliothèques nécessaires, dont OpenAI, dotenv, requests et Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Ensuite, on charge les variables d’environnement depuis le fichier _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Après cela, on configure le client du service Azure OpenAI 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Puis, on génère l’image :

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Le code ci-dessus renvoie un objet JSON contenant l’URL de l’image générée. On peut utiliser cette URL pour télécharger l’image et l’enregistrer dans un fichier.

- Enfin, on ouvre l’image et on l’affiche avec la visionneuse d’images standard :

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Détails supplémentaires sur la génération d’image

Regardons de plus près le code qui génère l’image :

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** : c’est la consigne textuelle utilisée pour générer l’image. Ici, on utilise « Lapin sur un cheval, tenant une sucette, dans une prairie brumeuse où poussent des jonquilles ».
- **size** : c’est la taille de l’image générée. Ici, on génère une image de 1024x1024 pixels.
- **n** : c’est le nombre d’images générées. Ici, on en génère deux.
- **temperature** : c’est un paramètre qui contrôle le degré d’aléa dans la sortie du modèle d’IA générative. La température est une valeur entre 0 et 1 : 0 signifie que la sortie est déterministe, 1 qu’elle est aléatoire. La valeur par défaut est 0,7.

Il existe d’autres possibilités avec les images, que nous verrons dans la section suivante.

## Capacités supplémentaires de la génération d’images

Vous avez vu comment générer une image en quelques lignes de Python. Mais il y a bien d’autres choses à faire avec les images.

Vous pouvez aussi :

- **Faire des modifications**. En fournissant une image existante, un masque et une consigne, vous pouvez modifier une image. Par exemple, vous pouvez ajouter un élément à une partie de l’image. Imaginez notre image de lapin : vous pouvez ajouter un chapeau au lapin. Pour cela, il faut fournir l’image, un masque (qui identifie la zone à modifier) et une consigne textuelle pour décrire la modification.
> Note : ceci n’est pas pris en charge dans DALL-E 3.
 
Voici un exemple avec GPT Image :

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  L’image de base ne contient que le salon avec la piscine, mais l’image finale aura un flamant rose :

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Créer des variations**. L’idée est de prendre une image existante et de demander la création de variantes. Pour cela, il suffit de fournir une image, une consigne textuelle et un code comme ceci :

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Note : ceci n’est pris en charge que sur OpenAI

## Température

La température est un paramètre qui contrôle le degré d’aléa dans la sortie d’un modèle d’IA générative. La température est une valeur comprise entre 0 et 1 : 0 signifie que la sortie est déterministe, 1 qu’elle est aléatoire. La valeur par défaut est 0,7.

Voyons un exemple de fonctionnement de la température, en lançant cette consigne deux fois :

> Consigne : « Lapin sur un cheval, tenant une sucette, dans une prairie brumeuse où poussent des jonquilles »

![Lapin sur un cheval tenant une sucette, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.fr.png)

Relançons la même consigne pour voir que nous n’obtenons pas deux fois la même image :

![Image générée de lapin sur un cheval](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.fr.png)

Comme vous pouvez le voir, les images se ressemblent, mais ne sont pas identiques. Essayons maintenant de changer la valeur de température à 0,1 et voyons ce qui se passe :

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Modifier la température

Essayons de rendre la réponse plus déterministe. On a pu observer que dans la première image, il y a un lapin, et dans la seconde, un cheval, donc les images varient beaucoup.

Modifions donc notre code et fixons la température à 0, comme ceci :

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

En lançant ce code, vous obtenez ces deux images :

- ![Température 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.fr.png)
- ![Température 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.fr.png)

On voit clairement que les images se ressemblent beaucoup plus.

## Comment définir des limites pour votre application avec des métaprompts

Avec notre démo, nous pouvons déjà générer des images pour nos clients. Mais il est important de définir des limites pour notre application.

Par exemple, nous ne voulons pas générer d’images inappropriées ou non adaptées à un public jeune.

Pour cela, on peut utiliser des _métaprompts_. Les métaprompts sont des consignes textuelles qui servent à contrôler la sortie d’un modèle d’IA générative. Par exemple, on peut utiliser des métaprompts pour s’assurer que les images générées sont adaptées à un usage professionnel ou à des enfants.

### Comment ça marche ?

Alors, comment fonctionnent les métaprompts ?

Les métaprompts sont des consignes textuelles placées avant la consigne principale, qui servent à contrôler la sortie du modèle et sont intégrées dans les applications pour encadrer la génération. On encapsule la consigne utilisateur et le métaprompt dans une seule consigne textuelle.

Un exemple de métaprompt serait :

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Voyons maintenant comment utiliser les métaprompts dans notre démo.

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

Dans la consigne ci-dessus, on voit que toutes les images créées tiennent compte du métaprompt.

## Exercice – à vous de jouer !

Nous avons présenté Edu4All au début de cette leçon. Il est maintenant temps de permettre aux élèves de générer des images pour leurs évaluations.

Les élèves vont créer des images pour leurs évaluations sur les monuments ; le choix des monuments leur appartient. Ils sont invités à faire preuve de créativité en plaçant ces monuments dans différents contextes.

## Solution

Voici une solution possible :

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## Bravo ! Continuez votre apprentissage
Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l’IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à développer vos connaissances en IA générative !

Passez à la leçon 10 où nous verrons comment [créer des applications d’IA avec peu de code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent comporter des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.