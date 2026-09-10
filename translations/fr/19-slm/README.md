# Introduction aux petits modèles de langage pour l'IA générative à destination des débutants
L'IA générative est un domaine fascinant de l'intelligence artificielle qui se concentre sur la création de systèmes capables de générer de nouveaux contenus. Ces contenus peuvent aller du texte et des images à la musique, voire même à des environnements virtuels entiers. L'une des applications les plus passionnantes de l'IA générative se trouve dans le domaine des modèles de langage.

## Qu'est-ce que les petits modèles de langage ?

Un petit modèle de langage (SLM) représente une variante réduite d'un grand modèle de langage (LLM), exploitant de nombreux principes architecturaux et techniques des LLM, tout en affichant une empreinte informatique significativement réduite.

Les SLM sont une sous-catégorie de modèles de langage conçus pour générer du texte semblable à celui produit par des humains. Contrairement à leurs homologues plus grands, tels que GPT-4, les SLM sont plus compacts et efficaces, ce qui les rend idéaux pour des applications où les ressources informatiques sont limitées. Malgré leur taille réduite, ils peuvent encore accomplir divers types de tâches. Typiquement, les SLM sont construits par compression ou distillation des LLM, visant à conserver une part substantielle des fonctionnalités et capacités linguistiques du modèle original. Cette réduction de taille diminue la complexité globale, rendant les SLM plus efficaces en termes de mémoire et d'exigences computationnelles. Malgré ces optimisations, les SLM sont capables de réaliser un large éventail de tâches en traitement automatique du langage naturel (TALN) :

- Génération de texte : création de phrases ou paragraphes cohérents et contextuellement pertinents.
- Complétion de texte : prédiction et complétion de phrases à partir d'une requête donnée.
- Traduction : conversion de texte d'une langue à une autre.
- Résumé : condensation de longs textes en résumés plus courts et faciles à digérer.

Bien sûr, avec quelques compromis sur la performance ou la profondeur de compréhension comparé à leurs homologues plus grands.

## Comment fonctionnent les petits modèles de langage ?
Les SLM sont entraînés sur de grandes quantités de données textuelles. Lors de l'entraînement, ils apprennent les modèles et structures du langage, ce qui leur permet de générer un texte à la fois grammaticalement correct et contextuellement approprié. Le processus d'entraînement comprend :

- Collecte de données : rassemblement de larges ensembles de données textuelles provenant de diverses sources.
- Prétraitement : nettoyage et organisation des données pour les rendre adaptées à l'entraînement.
- Entraînement : utilisation d'algorithmes d'apprentissage automatique pour enseigner au modèle comment comprendre et générer du texte.
- Ajustement fin : réglage du modèle pour améliorer ses performances sur des tâches spécifiques.

Le développement des SLM répond au besoin croissant de modèles pouvant être déployés dans des environnements aux ressources limitées, tels que les appareils mobiles ou les plateformes de calcul en périphérie, où les LLM à grande échelle peuvent être impraticables à cause de leurs fortes demandes en ressources. En se concentrant sur l'efficacité, les SLM équilibrent performance et accessibilité, permettant une application plus large dans divers domaines.

![slm](../../../translated_images/fr/slm.4058842744d0444a.webp)

## Objectifs d'apprentissage

Dans cette leçon, nous espérons introduire la connaissance des SLM et la combiner avec Microsoft Phi-3 afin d'explorer différents scénarios dans les contenus textuels, la vision et MoE.

À la fin de cette leçon, vous devriez être capable de répondre aux questions suivantes :

- Qu'est-ce qu'un SLM ?
- Quelle est la différence entre un SLM et un LLM ?
- Qu'est-ce que la famille Microsoft Phi-3/3.5 ?
- Comment exécuter une inférence avec la famille Microsoft Phi-3/3.5 ?

Prêt ? Commençons.

## Les distinctions entre grands modèles de langage (LLM) et petits modèles de langage (SLM)

Les LLM et les SLM reposent tous deux sur des principes fondamentaux d'apprentissage automatique probabiliste, suivant des approches similaires dans leur conception architecturale, leurs méthodologies d'entraînement, leurs processus de génération de données et leurs techniques d'évaluation des modèles. Toutefois, plusieurs facteurs clés différencient ces deux types de modèles.

## Applications des petits modèles de langage

Les SLM ont un large éventail d'applications, notamment :

- Chatbots : fournir un support client et interagir avec les utilisateurs de manière conversationnelle.
- Création de contenu : assister les écrivains en générant des idées ou même en rédigeant des articles entiers.
- Éducation : aider les étudiants dans leurs travaux d’écriture ou l’apprentissage de nouvelles langues.
- Accessibilité : créer des outils pour les personnes en situation de handicap, tels que les systèmes de synthèse vocale.

**Taille**
  
Une distinction principale entre LLM et SLM réside dans l'échelle des modèles. Les LLM, tels que ChatGPT (GPT-4), peuvent comporter un nombre estimé à 1,76 trillion de paramètres, tandis que des SLM open source comme Mistral 7B sont conçus avec beaucoup moins de paramètres — environ 7 milliards. Cette disparité provient principalement des différences d’architecture de modèle et des processus d'entraînement. Par exemple, ChatGPT utilise un mécanisme d'attention auto-référente dans une architecture encodeur-décodeur, alors que Mistral 7B utilise une attention à fenêtre coulissante, permettant un entraînement plus efficace dans un modèle uniquement décodeur. Cette variance architecturale a des implications profondes sur la complexité et la performance de ces modèles.

**Compréhension**

Les SLM sont généralement optimisés pour des performances dans des domaines spécifiques, ce qui les rend très spécialisés mais potentiellement limités dans leur capacité à fournir une compréhension contextuelle large couvrant plusieurs champs de connaissance. En revanche, les LLM visent à simuler une intelligence humaine plus complète. Entraînés sur de vastes ensembles de données diversifiés, les LLM sont conçus pour bien performer dans une variété de domaines, offrant une plus grande polyvalence et adaptabilité. Par conséquent, les LLM conviennent mieux à un éventail plus large de tâches en aval, comme le traitement du langage naturel et la programmation.

**Calcul**

L’entraînement et le déploiement des LLM sont des processus gourmands en ressources, nécessitant souvent une infrastructure informatique importante, comprenant de vastes grappes de GPU. Par exemple, l’entraînement d'un modèle comme ChatGPT à partir de zéro peut nécessiter des milliers de GPU sur de longues périodes. En revanche, les SLM, avec un nombre moindre de paramètres, sont plus accessibles en termes de ressources informatiques. Des modèles comme Mistral 7B peuvent être entraînés et utilisés sur des machines locales équipées de GPU modérés, bien que l’entraînement demande toujours plusieurs heures sur plusieurs GPU.

**Biais**

Le biais est un problème connu chez les LLM, principalement à cause de la nature des données d’entraînement. Ces modèles se basent souvent sur des données brutes, librement disponibles sur Internet, qui peuvent sous-représenter ou mal représenter certains groupes, introduire des étiquetages erronés, ou refléter des biais linguistiques influencés par des dialectes, des variations géographiques et des règles grammaticales. De plus, la complexité des architectures LLM peut involontairement exacerber ces biais, qui peuvent passer inaperçus sans un ajustement fin minutieux. D’un autre côté, les SLM, étant entraînés sur des ensembles de données plus restreints et spécifiques à un domaine, sont naturellement moins susceptibles à ces biais, bien qu’ils ne soient pas complètement exempts.

**Inférence**

La taille réduite des SLM leur confère un avantage important en termes de rapidité d'inférence, leur permettant de générer des sorties efficacement sur des machines locales sans nécessiter de traitement parallèle étendu. En revanche, les LLM, en raison de leur taille et complexité, requièrent souvent d’importantes ressources parallèles pour atteindre des temps d’inférence acceptables. La présence de plusieurs utilisateurs simultanés ralentit encore davantage les temps de réponse des LLM, surtout lorsqu’ils sont déployés à grande échelle.

En résumé, bien que les LLM et les SLM partagent une base fondamentale en apprentissage automatique, ils diffèrent significativement en termes de taille de modèle, exigences en ressources, compréhension contextuelle, susceptibilité aux biais et vitesse d’inférence. Ces distinctions reflètent leur adéquation respective à différents cas d’usage, les LLM étant plus polyvalents mais gourmands en ressources, tandis que les SLM offrent une efficacité plus ciblée avec des besoins informatiques réduits.

***Note : Dans cette leçon, nous introduirons les SLM en utilisant Microsoft Phi-3 / 3.5 comme exemple.***

## Présentation de la famille Phi-3 / Phi-3.5

La famille Phi-3 / 3.5 cible principalement les scénarios d'applications en texte, vision et Agent (MoE) :

### Phi-3 / 3.5 Instruct

Principalement pour la génération de texte, la complétion de chat et l'extraction d'informations de contenu, etc.

**Phi-3-mini**

Le modèle de langage à 3,8 milliards de paramètres est disponible sur Microsoft Foundry, Hugging Face, et Ollama. Les modèles Phi-3 surpassent significativement les modèles de langage de tailles similaires et plus grandes sur des benchmarks clés (voir les chiffres des benchmarks ci-dessous, des chiffres plus élevés sont meilleurs). Phi-3-mini surpasse des modèles deux fois plus grands, tandis que Phi-3-small et Phi-3-medium surpassent des modèles plus volumineux, y compris GPT-3.5.

**Phi-3-small & medium**

Avec seulement 7 milliards de paramètres, Phi-3-small bat GPT-3.5T sur une variété de benchmarks en langage, raisonnement, codage et mathématiques.

Le Phi-3-medium avec 14 milliards de paramètres poursuit cette tendance et dépasse Gemini 1.0 Pro.

**Phi-3.5-mini**

On peut le considérer comme une mise à niveau de Phi-3-mini. Bien que le nombre de paramètres reste inchangé, il améliore la capacité à supporter plusieurs langues (plus de 20 langues prises en charge : arabe, chinois, tchèque, danois, néerlandais, anglais, finnois, français, allemand, hébreu, hongrois, italien, japonais, coréen, norvégien, polonais, portugais, russe, espagnol, suédois, thaï, turc, ukrainien) et ajoute un meilleur support pour les contextes longs.

Phi-3.5-mini avec 3,8 milliards de paramètres dépasse les modèles de même taille et est à égalité avec des modèles deux fois plus grands.

### Phi-3 / 3.5 Vision

On peut considérer le modèle Instruct de Phi-3/3.5 comme la capacité de Phi à comprendre, et Vision, comme ce qui donne à Phi des yeux pour comprendre le monde.


**Phi-3-Vision**

Phi-3-vision, avec seulement 4,2 milliards de paramètres, poursuit cette tendance et surpasse des modèles plus grands tels que Claude-3 Haiku et Gemini 1.0 Pro V sur les tâches générales de raisonnement visuel, OCR, ainsi que la compréhension de tableaux et diagrammes.


**Phi-3.5-Vision**

Phi-3.5-Vision est également une mise à niveau de Phi-3-Vision, ajoutant la prise en charge de plusieurs images. On peut le voir comme une amélioration en vision : non seulement il peut voir les images, mais aussi les vidéos.

Phi-3.5-vision surpasse des modèles plus grands comme Claude-3.5 Sonnet et Gemini 1.5 Flash sur les tâches OCR, compréhension des tableaux et graphiques, et est à égalité sur les tâches générales de raisonnement visuel. Il supporte l’entrée multi-frames, c'est-à-dire effectuer du raisonnement sur plusieurs images en entrée.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** permet aux modèles d’être préentraînés avec beaucoup moins de calcul, ce qui signifie que vous pouvez augmenter radicalement la taille du modèle ou du jeu de données avec le même budget de calcul qu’un modèle dense. En particulier, un modèle MoE devrait atteindre la même qualité que son homologue dense beaucoup plus rapidement durant le préentraînement.

Phi-3.5-MoE comprend 16 modules experts de 3,8 milliards chacun. Phi-3.5-MoE avec seulement 6,6 milliards de paramètres actifs atteint un niveau similaire de raisonnement, compréhension du langage et mathématiques que des modèles beaucoup plus volumineux.

On peut utiliser le modèle de la famille Phi-3/3.5 selon différents scénarios. Contrairement aux LLM, vous pouvez déployer Phi-3/3.5-mini ou Phi-3/3.5-Vision sur des appareils en périphérie.


## Comment utiliser les modèles de la famille Phi-3/3.5

Nous espérons utiliser Phi-3/3.5 dans différents scénarios. Ensuite, nous utiliserons Phi-3/3.5 selon les différents scénarios.

![phi3](../../../translated_images/fr/phi3.655208c3186ae381.webp)

### Inférence via APIs Cloud

**Modèles Microsoft Foundry**

> **Note :** Les modèles GitHub seront retirés fin juillet 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) en est le remplacement direct.

Microsoft Foundry Models est la manière la plus directe. Vous pouvez accéder rapidement au modèle Phi-3/3.5-Instruct via le catalogue de modèles Foundry. Combiné avec le SDK Azure AI Inference / SDK OpenAI, vous pouvez accéder à l’API via du code pour effectuer l’appel Phi-3/3.5-Instruct. Vous pouvez également tester différents effets via le Playground.

- Démo : comparaison des effets de Phi-3-mini et Phi-3.5-mini dans des scénarios en chinois

![phi3](../../../translated_images/fr/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/fr/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ou si vous souhaitez utiliser les modèles vision et MoE, vous pouvez utiliser Microsoft Foundry pour effectuer l’appel. Si vous êtes intéressé, vous pouvez lire le Phi-3 Cookbook pour apprendre comment appeler Phi-3/3.5 Instruct, Vision, MoE via Microsoft Foundry [Cliquez sur ce lien](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

En plus du catalogue Microsoft Foundry Models basé sur le cloud, vous pouvez également utiliser [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) pour effectuer les appels correspondants. Vous pouvez visiter NVIDIA NIM pour effectuer les appels API de la famille Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) est un ensemble de microservices d'inférence accélérés conçus pour aider les développeurs à déployer efficacement des modèles d'IA dans divers environnements, y compris les clouds, les centres de données et les stations de travail.

Voici quelques caractéristiques clés de NVIDIA NIM :

- **Facilité de déploiement :** NIM permet le déploiement de modèles d'IA en une seule commande, facilitant son intégration dans les flux de travail existants.

- **Performance Optimisée :** Il exploite les moteurs d'inférence pré-optimisés de NVIDIA, tels que TensorRT et TensorRT-LLM, pour garantir une faible latence et un débit élevé.
- **Scalabilité :** NIM prend en charge l'autoscaling sur Kubernetes, lui permettant de gérer efficacement des charges de travail variables.
- **Sécurité et Contrôle :** Les organisations peuvent conserver le contrôle de leurs données et applications en hébergeant elles-mêmes les microservices NIM sur leur propre infrastructure gérée.
- **APIs Standard :** NIM fournit des APIs standard de l'industrie, facilitant la création et l'intégration d'applications d'IA telles que les chatbots, assistants IA, et plus encore.

NIM fait partie de NVIDIA AI Enterprise, qui vise à simplifier le déploiement et l'opérationnalisation des modèles d'IA, en garantissant qu'ils fonctionnent efficacement sur les GPU NVIDIA.

- Démo : Utilisation de NVIDIA NIM pour appeler Phi-3.5-Vision-API  [[Cliquez sur ce lien](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Exécuter Phi-3/3.5 Localement
L'inférence en lien avec Phi-3, ou tout modèle de langage comme GPT-3, fait référence au processus de génération de réponses ou prédictions basées sur l'entrée reçue. Lorsque vous fournissez une invite ou une question à Phi-3, il utilise son réseau neuronal entraîné pour déduire la réponse la plus probable et pertinente en analysant les motifs et relations dans les données sur lesquelles il a été formé.

**Hugging Face Transformer**
Hugging Face Transformers est une bibliothèque puissante conçue pour le traitement du langage naturel (NLP) et d'autres tâches d'apprentissage automatique. Voici quelques points clés à son sujet :

1. **Modèles Préentraînés** : Elle fournit des milliers de modèles préentraînés pouvant être utilisés pour diverses tâches telles que la classification de texte, la reconnaissance d'entités nommées, la réponse à des questions, le résumé, la traduction, et la génération de texte.

2. **Interopérabilité des Frameworks** : La bibliothèque supporte plusieurs frameworks de deep learning, notamment PyTorch, TensorFlow, et JAX. Cela vous permet d'entraîner un modèle dans un framework et de l'utiliser dans un autre.

3. **Capacités Multimodales** : En plus du NLP, Hugging Face Transformers prend également en charge des tâches en vision par ordinateur (ex. classification d'images, détection d'objets) et traitement audio (ex. reconnaissance vocale, classification audio).

4. **Facilité d'Utilisation** : La bibliothèque offre des APIs et outils pour télécharger et affiner facilement les modèles, la rendant accessible aux débutants comme aux experts.

5. **Communauté et Ressources** : Hugging Face dispose d'une communauté dynamique et d'une documentation étendue, tutoriels et guides pour aider les utilisateurs à démarrer et maximiser l'usage de la bibliothèque.
[documentation officielle](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ou leur [dépôt GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

C'est la méthode la plus couramment utilisée, mais elle nécessite également une accélération GPU. En effet, des scénarios comme Vision et MoE nécessitent beaucoup de calculs, ce qui sera très lent sur CPU s'ils ne sont pas quantifiés.


- Démo : Utilisation de Transformer pour appeler Phi-3.5-Instruct [Cliquez sur ce lien](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Démo : Utilisation de Transformer pour appeler Phi-3.5-Vision [Cliquez sur ce lien](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Démo : Utilisation de Transformer pour appeler Phi-3.5-MoE [Cliquez sur ce lien](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) est une plateforme conçue pour faciliter l'exécution locale de grands modèles de langage (LLM) sur votre machine. Elle prend en charge divers modèles comme Llama 3.1, Phi 3, Mistral, et Gemma 2, entre autres. La plateforme simplifie le processus en regroupant poids du modèle, configuration, et données dans un seul package, rendant la personnalisation et la création de vos propres modèles plus accessibles. Ollama est disponible pour macOS, Linux, et Windows. C'est un excellent outil si vous souhaitez expérimenter ou déployer des LLM sans dépendre des services cloud. Ollama est la méthode la plus directe, il vous suffit d'exécuter la commande suivante.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) est l’environnement d’exécution hors ligne sur appareil de Microsoft pour exécuter des modèles comme Phi entièrement sur votre propre matériel - aucune souscription Azure, clé API, ou connexion réseau requise. Il choisit automatiquement le meilleur fournisseur d’exécution disponible (NPU, GPU ou CPU) et expose un point d’entrée compatible OpenAI, permettant au code existant `openai`/Azure AI Inference SDK de pointer vers lui avec un minimum de changements. Consultez la [documentation Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pour démarrer.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Ou utilisez directement le SDK en Python :

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime pour GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) est un accélérateur d’inférence et d’entraînement machine learning multiplateforme. ONNX Runtime pour Generative AI (GENAI) est un outil puissant qui vous aide à exécuter efficacement des modèles d’IA générative sur diverses plateformes.

## Qu'est-ce que ONNX Runtime ?
ONNX Runtime est un projet open-source qui permet une inférence haute performance des modèles d’apprentissage automatique. Il supporte les modèles au format Open Neural Network Exchange (ONNX), qui est une norme pour représenter les modèles d’apprentissage automatique. L’inférence ONNX Runtime peut offrir une expérience client plus rapide et des coûts réduits, supportant les modèles issus de frameworks de deep learning tels que PyTorch et TensorFlow/Keras ainsi que des bibliothèques classiques de machine learning comme scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime est compatible avec divers matériels, pilotes et systèmes d’exploitation, offrant des performances optimales en exploitant les accélérateurs matériels lorsque cela est possible ainsi que des optimisations et transformations de graphes.

## Qu'est-ce que l'IA générative ?
L'IA générative désigne des systèmes d’IA capables de générer du contenu nouveau, tel que du texte, des images, ou de la musique, basé sur les données sur lesquelles ils ont été entraînés. Des exemples incluent des modèles de langage comme GPT-3 et des modèles de génération d’images comme Stable Diffusion. La bibliothèque ONNX Runtime pour GenAI fournit la boucle d’IA générative pour les modèles ONNX, incluant l’inférence avec ONNX Runtime, traitement des logits, recherche et échantillonnage, et gestion du cache KV.

## ONNX Runtime pour GENAI
ONNX Runtime pour GENAI étend les capacités d’ONNX Runtime pour supporter les modèles d’IA générative. Voici quelques fonctionnalités clés :

- **Support étendu des plateformes :** Il fonctionne sur diverses plateformes, y compris Windows, Linux, macOS, Android, et iOS.
- **Support des modèles :** Il supporte de nombreux modèles populaires d’IA générative, tels que LLaMA, GPT-Neo, BLOOM, et plus encore.
- **Optimisation des performances :** Il inclut des optimisations pour différents accélérateurs matériels comme les GPU NVIDIA, GPU AMD, et plus2.
- **Facilité d'utilisation :** Il fournit des APIs pour une intégration facile dans les applications, vous permettant de générer du texte, des images, et autres contenus avec un minimum de code.
- Les utilisateurs peuvent appeler une méthode de haut niveau generate(), ou exécuter chaque itération du modèle dans une boucle, générant un token à la fois, et éventuellement mise à jour des paramètres de génération dans la boucle.
- ONNX Runtime supporte aussi la recherche gloutonne/à faisceaux et l’échantillonnage TopP, TopK pour générer des séquences de tokens ainsi que le traitement intégré des logits comme les pénalités de répétition. Vous pouvez aussi facilement ajouter un scoring personnalisé.

## Pour commencer
Pour commencer avec ONNX Runtime pour GENAI, vous pouvez suivre ces étapes :

### Installer ONNX Runtime :
```Python
pip install onnxruntime
```
### Installer les extensions Generative AI :
```Python
pip install onnxruntime-genai
```

### Exécuter un modèle : Voici un exemple simple en Python :
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Démo : Utilisation d’ONNX Runtime GenAI pour appeler Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Autres**

En plus d'ONNX Runtime, Ollama et Foundry Local comme méthodes de référence, nous pouvons aussi compléter la référence des modèles quantitatifs basés sur les méthodes de référence des différents fabricants. Comme le framework Apple MLX avec Apple Metal, Qualcomm QNN avec NPU, Intel OpenVINO avec CPU/GPU, etc. Vous pouvez également obtenir plus de contenu dans le [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Plus

Nous avons appris les bases de la famille Phi-3/3.5, mais pour en savoir plus sur SLM, nous avons besoin de connaissances supplémentaires. Vous pouvez trouver les réponses dans le Phi-3 Cookbook. Si vous souhaitez en apprendre davantage, veuillez consulter le [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->