<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:25:42+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "fr"
}
-->
# Créer des applications de génération d'images

[![Créer des applications de génération d'images](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.fr.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Les LLM ne se limitent pas à la génération de texte. Il est également possible de générer des images à partir de descriptions textuelles. Avoir des images comme modalité peut être très utile dans de nombreux domaines tels que la MedTech, l'architecture, le tourisme, le développement de jeux et bien plus encore. Dans ce chapitre, nous examinerons les deux modèles de génération d'images les plus populaires, DALL-E et Midjourney.

## Introduction

Dans cette leçon, nous aborderons :

- La génération d'images et pourquoi elle est utile.
- DALL-E et Midjourney, ce qu'ils sont et comment ils fonctionnent.
- Comment créer une application de génération d'images.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous serez capable de :

- Créer une application de génération d'images.
- Définir des limites pour votre application avec des méta-prompts.
- Travailler avec DALL-E et Midjourney.

## Pourquoi créer une application de génération d'images ?

Les applications de génération d'images sont un excellent moyen d'explorer les capacités de l'IA générative. Elles peuvent être utilisées, par exemple :

- **Édition et synthèse d'images**. Vous pouvez générer des images pour divers cas d'utilisation, tels que l'édition et la synthèse d'images.

- **Application dans divers secteurs**. Elles peuvent également être utilisées pour générer des images dans divers secteurs comme la MedTech, le tourisme, le développement de jeux et bien plus encore.

## Scénario : Edu4All

Dans le cadre de cette leçon, nous continuerons à travailler avec notre startup, Edu4All. Les étudiants créeront des images pour leurs évaluations, le choix des images leur appartient, mais elles pourraient être des illustrations pour leur propre conte de fées, la création d'un nouveau personnage pour leur histoire ou les aider à visualiser leurs idées et concepts.

Voici ce que les étudiants d'Edu4All pourraient générer, par exemple, s'ils travaillent en classe sur les monuments :

![Startup Edu4All, classe sur les monuments, Tour Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.fr.png)

en utilisant un prompt comme :

> "Chien à côté de la Tour Eiffel au lever du soleil"

## Qu'est-ce que DALL-E et Midjourney ?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) et [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) sont deux des modèles de génération d'images les plus populaires, permettant d'utiliser des prompts pour générer des images.

### DALL-E

Commençons par DALL-E, qui est un modèle d'IA générative capable de créer des images à partir de descriptions textuelles.

> [DALL-E est une combinaison de deux modèles, CLIP et attention diffusée](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, est un modèle qui génère des embeddings, des représentations numériques de données, à partir d'images et de texte.

- **Attention diffusée**, est un modèle qui génère des images à partir d'embeddings. DALL-E est entraîné sur un ensemble de données d'images et de texte et peut être utilisé pour générer des images à partir de descriptions textuelles. Par exemple, DALL-E peut être utilisé pour générer des images d'un chat avec un chapeau ou d'un chien avec une crête.

### Midjourney

Midjourney fonctionne de manière similaire à DALL-E, générant des images à partir de prompts textuels. Midjourney peut également être utilisé pour générer des images avec des prompts comme "un chat avec un chapeau" ou "un chien avec une crête".

![Image générée par Midjourney, pigeon mécanique](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédit image Wikipedia, image générée par Midjourney_

## Comment fonctionnent DALL-E et Midjourney

Tout d'abord, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E est un modèle d'IA générative basé sur l'architecture des transformateurs avec un _transformateur autorégressif_.

Un _transformateur autorégressif_ définit comment un modèle génère des images à partir de descriptions textuelles, en générant un pixel à la fois, puis en utilisant les pixels générés pour générer le pixel suivant. Ce processus passe par plusieurs couches d'un réseau neuronal jusqu'à ce que l'image soit complète.

Avec ce processus, DALL-E contrôle les attributs, objets, caractéristiques et plus encore dans l'image qu'il génère. Cependant, DALL-E 2 et 3 offrent un contrôle accru sur l'image générée.

## Créer votre première application de génération d'images

Alors, que faut-il pour créer une application de génération d'images ? Vous aurez besoin des bibliothèques suivantes :

- **python-dotenv**, il est fortement recommandé d'utiliser cette bibliothèque pour conserver vos secrets dans un fichier _.env_ séparé du code.
- **openai**, cette bibliothèque vous permettra d'interagir avec l'API OpenAI.
- **pillow**, pour travailler avec des images en Python.
- **requests**, pour vous aider à effectuer des requêtes HTTP.

## Créer et déployer un modèle Azure OpenAI

Si ce n'est pas encore fait, suivez les instructions sur la page [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) pour créer une ressource et un modèle Azure OpenAI. Sélectionnez DALL-E 3 comme modèle.

## Créer l'application

1. Créez un fichier _.env_ avec le contenu suivant :

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Trouvez ces informations dans le portail Azure OpenAI Foundry pour votre ressource dans la section "Déploiements".

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

   Pour Windows, utilisez les commandes suivantes pour créer et activer votre environnement virtuel :

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

- Tout d'abord, nous importons les bibliothèques nécessaires, y compris la bibliothèque OpenAI, la bibliothèque dotenv, la bibliothèque requests et la bibliothèque Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Ensuite, nous chargeons les variables d'environnement du fichier _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Après cela, nous configurons le client du service Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Ensuite, nous générons l'image :

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Le code ci-dessus répond avec un objet JSON contenant l'URL de l'image générée. Nous pouvons utiliser l'URL pour télécharger l'image et l'enregistrer dans un fichier.

- Enfin, nous ouvrons l'image et utilisons le visualiseur d'images standard pour l'afficher :

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Plus de détails sur la génération de l'image

Examinons le code qui génère l'image plus en détail :

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, est le prompt textuel utilisé pour générer l'image. Dans ce cas, nous utilisons le prompt "Lapin sur un cheval, tenant une sucette, dans une prairie brumeuse où poussent des jonquilles".
- **size**, est la taille de l'image générée. Dans ce cas, nous générons une image de 1024x1024 pixels.
- **n**, est le nombre d'images générées. Dans ce cas, nous générons deux images.
- **temperature**, est un paramètre qui contrôle la randomisation de la sortie d'un modèle d'IA générative. La température est une valeur entre 0 et 1 où 0 signifie que la sortie est déterministe et 1 signifie que la sortie est aléatoire. La valeur par défaut est 0,7.

Il y a plus de choses que vous pouvez faire avec les images, que nous aborderons dans la section suivante.

## Capacités supplémentaires de la génération d'images

Vous avez vu jusqu'à présent comment nous avons pu générer une image avec quelques lignes de code en Python. Cependant, il y a plus de choses que vous pouvez faire avec les images.

Vous pouvez également faire ce qui suit :

- **Effectuer des modifications**. En fournissant une image existante, un masque et un prompt, vous pouvez modifier une image. Par exemple, vous pouvez ajouter quelque chose à une partie de l'image. Imaginez notre image de lapin, vous pouvez ajouter un chapeau au lapin. Pour ce faire, vous fournissez l'image, un masque (identifiant la partie de la zone à modifier) et un prompt textuel pour indiquer ce qui doit être fait. 
> Note : cela n'est pas pris en charge dans DALL-E 3.

Voici un exemple utilisant GPT Image :

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  L'image de base ne contiendrait que le salon avec piscine, mais l'image finale inclurait un flamant rose :

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.fr.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.fr.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.fr.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Créer des variations**. L'idée est de prendre une image existante et de demander que des variations soient créées. Pour créer une variation, vous fournissez une image et un prompt textuel, et utilisez un code comme celui-ci :

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Note : cela est uniquement pris en charge par OpenAI.

## Température

La température est un paramètre qui contrôle la randomisation de la sortie d'un modèle d'IA générative. La température est une valeur entre 0 et 1 où 0 signifie que la sortie est déterministe et 1 signifie que la sortie est aléatoire. La valeur par défaut est 0,7.

Examinons un exemple de fonctionnement de la température en exécutant ce prompt deux fois :

> Prompt : "Lapin sur un cheval, tenant une sucette, dans une prairie brumeuse où poussent des jonquilles"

![Lapin sur un cheval tenant une sucette, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.fr.png)

Maintenant, exécutons ce même prompt pour voir que nous n'obtiendrons pas deux fois la même image :

![Image générée de lapin sur un cheval](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.fr.png)

Comme vous pouvez le voir, les images sont similaires, mais pas identiques. Essayons de changer la valeur de la température à 0,1 et voyons ce qui se passe :

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Changer la température

Essayons donc de rendre la réponse plus déterministe. Nous avons pu observer à partir des deux images générées que dans la première image, il y a un lapin et dans la deuxième image, il y a un cheval, donc les images varient considérablement.

Changeons donc notre code et réglons la température à 0, comme suit :

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Maintenant, lorsque vous exécutez ce code, vous obtenez ces deux images :

- ![Température 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.fr.png)
- ![Température 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.fr.png)

Ici, vous pouvez clairement voir comment les images se ressemblent davantage.

## Comment définir des limites pour votre application avec des méta-prompts

Avec notre démonstration, nous pouvons déjà générer des images pour nos clients. Cependant, nous devons créer certaines limites pour notre application.

Par exemple, nous ne voulons pas générer des images qui ne sont pas adaptées au travail ou qui ne sont pas appropriées pour les enfants.

Nous pouvons faire cela avec des _méta-prompts_. Les méta-prompts sont des prompts textuels utilisés pour contrôler la sortie d'un modèle d'IA générative. Par exemple, nous pouvons utiliser des méta-prompts pour contrôler la sortie et garantir que les images générées sont adaptées au travail ou appropriées pour les enfants.

### Comment cela fonctionne-t-il ?

Alors, comment fonctionnent les méta-prompts ?

Les méta-prompts sont des prompts textuels utilisés pour contrôler la sortie d'un modèle d'IA générative. Ils sont positionnés avant le prompt textuel et sont utilisés pour contrôler la sortie du modèle, intégrés dans les applications pour contrôler la sortie du modèle. Ils encapsulent l'entrée du prompt et celle du méta-prompt dans un seul prompt textuel.

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

Voyons maintenant comment nous pouvons utiliser les méta-prompts dans notre démonstration.

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

À partir du prompt ci-dessus, vous pouvez voir comment toutes les images créées tiennent compte du méta-prompt.

## Devoir - permettons aux étudiants de créer

Nous avons présenté Edu4All au début de cette leçon. Il est maintenant temps de permettre aux étudiants de générer des images pour leurs évaluations.

Les étudiants créeront des images pour leurs évaluations contenant des monuments, le choix des monuments leur appartient. Les étudiants sont invités à faire preuve de créativité dans cette tâche pour placer ces monuments dans différents contextes.

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

## Excellent travail ! Continuez votre apprentissage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances sur l'IA générative !

Rendez-vous à la leçon 10 où nous verrons comment [créer des applications d'IA avec peu de code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.