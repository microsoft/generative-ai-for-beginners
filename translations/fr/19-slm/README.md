# Introduction aux petits modèles de langage pour l'IA générative pour débutants
L'IA générative est un domaine fascinant de l'intelligence artificielle qui se concentre sur la création de systèmes capables de générer de nouveaux contenus. Ces contenus peuvent aller du texte et des images à la musique voire des environnements virtuels entiers. L’une des applications les plus passionnantes de l’IA générative se trouve dans le domaine des modèles de langage.

## Que sont les petits modèles de langage ?

Un petit modèle de langage (SLM) représente une variante réduite d’un grand modèle de langage (LLM), tirant parti de nombreux principes architecturaux et techniques des LLM, tout en affichant une empreinte computationnelle considérablement réduite.

Les SLM sont un sous-ensemble de modèles de langage conçus pour générer un texte ressemblant à celui des humains. Contrairement à leurs homologues plus grands, tels que GPT-4, les SLM sont plus compacts et efficaces, ce qui les rend idéaux pour les applications où les ressources informatiques sont limitées. Malgré leur taille réduite, ils peuvent encore effectuer diverses tâches. En général, les SLM sont construits en compressant ou en distillant des LLM, visant à conserver une grande partie des fonctionnalités et des capacités linguistiques du modèle original. Cette réduction de la taille du modèle diminue la complexité globale, rendant les SLM plus efficaces à la fois en termes d'utilisation de la mémoire et des besoins en calcul. Malgré ces optimisations, les SLM peuvent toujours effectuer un large éventail de tâches de traitement du langage naturel (NLP) :

- Génération de texte : création de phrases ou paragraphes cohérents et contextuellement pertinents.
- Complétion de texte : prédiction et complétion de phrases à partir d’une invite donnée.
- Traduction : conversion de texte d’une langue à une autre.
- Résumé : condensation de longs textes en résumés plus courts et faciles à digérer.

Bien qu’avec quelques compromis sur la performance ou la profondeur de compréhension comparé à leurs homologues plus grands.

## Comment fonctionnent les petits modèles de langage ?
Les SLM sont entraînés sur d’énormes quantités de données textuelles. Pendant l’entraînement, ils apprennent les patterns et la structure du langage, ce qui leur permet de générer un texte à la fois grammaticalement correct et contextuellement approprié. Le processus d’entraînement comprend :

- Collecte de données : rassemblement de grands ensembles de données textuelles issues de diverses sources.
- Prétraitement : nettoyage et organisation des données pour les rendre aptes à l’entraînement.
- Entraînement : utilisation d’algorithmes d’apprentissage automatique pour enseigner au modèle comment comprendre et générer du texte.
- Affinage : ajustement du modèle pour améliorer ses performances sur des tâches spécifiques.

Le développement des SLM répond à un besoin croissant de modèles pouvant être déployés dans des environnements aux ressources limitées, tels que les appareils mobiles ou les plateformes de calcul en périphérie, où les LLM à grande échelle peuvent s’avérer impraticables en raison de leurs lourdes exigences en ressources. En mettant l’accent sur l’efficacité, les SLM équilibrent performance et accessibilité, permettant une application plus large dans divers domaines.

![slm](../../../translated_images/fr/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Objectifs d'apprentissage

Dans cette leçon, nous espérons introduire les connaissances sur les SLM et les combiner avec Microsoft Phi-3 pour apprendre différents scénarios dans le contenu textuel, la vision et MoE.

À la fin de cette leçon, vous devriez être capable de répondre aux questions suivantes :

- Qu’est-ce qu’un SLM ?
- Quelle est la différence entre SLM et LLM ?
- Qu’est-ce que la famille Microsoft Phi-3/3.5 ?
- Comment effectuer une inférence avec la famille Microsoft Phi-3/3.5 ?

Prêt ? Commençons.

## Les distinctions entre les grands modèles de langage (LLM) et les petits modèles de langage (SLM)

Les LLM et les SLM reposent tous deux sur des principes fondamentaux d’apprentissage machine probabiliste, suivant des approches similaires dans leur conception architecturale, leurs méthodologies d'entraînement, leurs processus de génération de données et leurs techniques d'évaluation des modèles. Cependant, plusieurs facteurs clés différencient ces deux types de modèles.

## Applications des petits modèles de langage

Les SLM ont un large éventail d’applications, notamment :

- Chatbots : fournir un support client et interagir avec les utilisateurs de manière conversationnelle.
- Création de contenu : aider les rédacteurs en générant des idées ou même en rédigeant des articles entiers.
- Éducation : aider les étudiants avec des devoirs écrits ou l’apprentissage de nouvelles langues.
- Accessibilité : créer des outils pour les personnes en situation de handicap, tels que des systèmes de synthèse vocale.

**Taille**
  
Une distinction principale entre les LLM et les SLM réside dans l’échelle des modèles. Les LLM, tels que ChatGPT (GPT-4), peuvent comprendre environ 1,76 trillion de paramètres, tandis que les SLM open-source comme Mistral 7B sont conçus avec beaucoup moins de paramètres — environ 7 milliards. Cette disparité est principalement liée aux différences d’architecture et de processus d’entraînement. Par exemple, ChatGPT utilise un mécanisme d’attention autonome dans un cadre encodeur-décodeur, tandis que Mistral 7B emploie une attention à fenêtre coulissante, ce qui permet un entraînement plus efficace dans un modèle uniquement décodeur. Cette variation architecturale a des implications profondes sur la complexité et la performance de ces modèles.

**Compréhension**

Les SLM sont généralement optimisés pour des performances dans des domaines spécifiques, ce qui les rend très spécialisés mais potentiellement limités dans leur capacité à fournir une compréhension contextuelle large sur plusieurs champs de connaissances. En revanche, les LLM visent à simuler une intelligence humaine plus complète. Entraînés sur des ensembles de données immenses et diversifiés, les LLM sont conçus pour bien performer dans divers domaines, offrant une plus grande polyvalence et adaptabilité. Par conséquent, les LLM sont plus adaptés à une gamme étendue de tâches en aval, telles que le traitement du langage naturel et la programmation.

**Calcul**

L’entraînement et le déploiement des LLM sont des processus gourmands en ressources, nécessitant souvent une infrastructure informatique importante, incluant des grappes GPU à grande échelle. Par exemple, entraîner un modèle comme ChatGPT depuis zéro peut nécessiter des milliers de GPU sur des périodes prolongées. En comparaison, les SLM, grâce à leur nombre réduit de paramètres, sont plus accessibles en termes de ressources informatiques. Des modèles comme Mistral 7B peuvent être entraînés et exécutés sur des machines locales équipées de capacités GPU modérées, bien que l’entraînement demande encore plusieurs heures sur plusieurs GPU.

**Biais**

Le biais est un problème connu dans les LLM, principalement dû à la nature des données d’entraînement. Ces modèles s’appuient souvent sur des données brutes, librement disponibles sur Internet, qui peuvent sous-représenter ou mal représenter certains groupes, introduire des étiquetages erronés, ou refléter des biais linguistiques influencés par le dialecte, les variations géographiques et les règles grammaticales. De plus, la complexité des architectures LLM peut involontairement exacerber ces biais, qui peuvent passer inaperçus sans un ajustement précis. En revanche, les SLM, étant entraînés sur des ensembles de données plus contraints et spécifiques à un domaine, sont moins susceptibles à ces biais, bien qu’ils n’y soient pas totalement insensibles.

**Inférence**

La taille réduite des SLM leur confère un avantage significatif en termes de vitesse d’inférence, leur permettant de générer efficacement des sorties sur du matériel local sans besoin de traitement parallèle étendu. À l’inverse, les LLM, en raison de leur taille et complexité, nécessitent souvent d’importantes ressources parallèles pour obtenir des temps d’inférence acceptables. La présence de nombreux utilisateurs simultanés ralentit encore les temps de réponse des LLM, surtout lorsqu’ils sont déployés à grande échelle.

En résumé, bien que les LLM et les SLM partagent une base fondamentale en apprentissage automatique, ils diffèrent considérablement en termes de taille de modèle, besoins en ressources, compréhension contextuelle, susceptibilité aux biais et vitesse d’inférence. Ces distinctions reflètent leur pertinence respective pour différents cas d’usage, les LLM étant plus polyvalents mais gourmands en ressources, tandis que les SLM offrent une efficacité plus spécifique à un domaine avec des besoins computationnels réduits.

***Note : Dans cette leçon, nous introduirons les SLM en utilisant Microsoft Phi-3 / 3.5 comme exemple.***

## Présentation de la famille Phi-3 / Phi-3.5

La famille Phi-3 / 3.5 cible principalement les scénarios d’application liés au texte, à la vision et à l’Agent (MoE) :

### Phi-3 / 3.5 Instruct

Principalement pour la génération de texte, la complétion de dialogues et l'extraction d'informations de contenu, etc.

**Phi-3-mini**

Le modèle de langage 3,8B est disponible sur Microsoft Foundry, Hugging Face et Ollama. Les modèles Phi-3 surpassent significativement les modèles de langage de taille égale ou supérieure sur des benchmarks clés (voir les chiffres de benchmark ci-dessous, des chiffres plus élevés sont meilleurs). Phi-3-mini surpasse des modèles deux fois plus gros, tandis que Phi-3-small et Phi-3-medium surpassent des modèles plus grands, y compris GPT-3.5.

**Phi-3-small & medium**

Avec seulement 7 milliards de paramètres, Phi-3-small bat GPT-3.5T sur une variété de benchmarks de langage, de raisonnement, de codage et de mathématiques.

Le Phi-3-medium avec 14 milliards de paramètres poursuit cette tendance et surpasse le Gemini 1.0 Pro.

**Phi-3.5-mini**

On peut le considérer comme une mise à niveau de Phi-3-mini. Alors que le nombre de paramètres reste inchangé, il améliore la capacité à supporter plusieurs langues (prise en charge de plus de 20 langues : arabe, chinois, tchèque, danois, néerlandais, anglais, finnois, français, allemand, hébreu, hongrois, italien, japonais, coréen, norvégien, polonais, portugais, russe, espagnol, suédois, thaï, turc, ukrainien) et ajoute un support renforcé pour les contextes longs.

Phi-3.5-mini avec ses 3,8 milliards de paramètres dépasse les modèles de même taille et rivalise avec des modèles deux fois plus gros.

### Phi-3 / 3.5 Vision

On peut considérer le modèle Instruct de Phi-3/3.5 comme la capacité de Phi à comprendre, et Vision comme ce qui donne à Phi les yeux pour comprendre le monde.


**Phi-3-Vision**

Phi-3-vision, avec seulement 4,2 milliards de paramètres, continue cette tendance et surpasse des modèles plus grands tels que Claude-3 Haiku et Gemini 1.0 Pro V sur des tâches générales de raisonnement visuel, OCR, et de compréhension de tableaux et diagrammes.


**Phi-3.5-Vision**

Phi-3.5-Vision est également une mise à niveau de Phi-3-Vision, ajoutant la prise en charge de plusieurs images. Vous pouvez le considérer comme une amélioration de la vision, non seulement vous pouvez voir des images, mais aussi des vidéos.

Phi-3.5-vision dépasse les modèles plus grands tels que Claude-3.5 Sonnet et Gemini 1.5 Flash sur les tâches OCR, de compréhension de tableaux et graphiques, et est équivalent sur les tâches générales de raisonnement visuel. Il supporte les entrées multi-cadres, c’est-à-dire réalise le raisonnement sur plusieurs images d’entrée.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** permet aux modèles d’être pré-entraînés avec beaucoup moins de calcul, ce qui signifie que vous pouvez considérablement augmenter la taille du modèle ou du jeu de données avec le même budget de calcul qu’un modèle dense. En particulier, un modèle MoE devrait atteindre la même qualité que son homologue dense beaucoup plus rapidement durant la pré-formation.

Phi-3.5-MoE comprend 16 modules experts de 3,8 milliards chacun. Phi-3.5-MoE avec seulement 6,6 milliards de paramètres actifs atteint un niveau similaire de raisonnement, compréhension du langage et mathématiques que des modèles beaucoup plus grands.

Nous pouvons utiliser le modèle de la famille Phi-3/3.5 selon différents scénarios. Contrairement aux LLM, vous pouvez déployer Phi-3/3.5-mini ou Phi-3/3.5-Vision sur des appareils en périphérie.


## Comment utiliser les modèles de la famille Phi-3/3.5

Nous espérons utiliser Phi-3/3.5 dans différents scénarios. Ensuite, nous utiliserons Phi-3/3.5 selon différents scénarios.

![phi3](../../../translated_images/fr/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inférence via APIs Cloud

**Modèles Microsoft Foundry**

> **Note :** GitHub Models sera retiré fin juillet 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) est le remplacement direct.

Microsoft Foundry Models est la méthode la plus directe. Vous pouvez rapidement accéder au modèle Phi-3/3.5-Instruct via le catalogue de modèles Foundry. Combiné avec Azure AI Inference SDK / OpenAI SDK, vous pouvez accéder à l’API par code pour réaliser l’appel Phi-3/3.5-Instruct. Vous pouvez également tester différents effets via le Playground.

- Démo : comparaison des effets de Phi-3-mini et Phi-3.5-mini dans des scénarios chinois

![phi3](../../../translated_images/fr/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/fr/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Ou si vous souhaitez utiliser les modèles vision et MoE, vous pouvez utiliser Microsoft Foundry pour effectuer l’appel. Si vous êtes intéressé, vous pouvez lire le Phi-3 Cookbook pour apprendre comment appeler Phi-3/3.5 Instruct, Vision, MoE via Microsoft Foundry [Cliquez sur ce lien](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

En plus du catalogue basé sur le cloud Microsoft Foundry Models, vous pouvez également utiliser [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) pour réaliser les appels associés. Vous pouvez visiter NVIDIA NIM pour effectuer les appels API de la famille Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) est un ensemble de microservices d’inférence accélérée conçus pour aider les développeurs à déployer efficacement des modèles IA sur divers environnements, y compris les clouds, centres de données et postes de travail.

Voici quelques caractéristiques clés de NVIDIA NIM :

- **Facilité de déploiement :** NIM permet le déploiement de modèles IA avec une seule commande, rendant l’intégration dans les flux de travail existants très simple.
- **Performance optimisée :** Il exploite les moteurs d’inférence pré-optimisés de NVIDIA, tels que TensorRT et TensorRT-LLM, pour assurer une faible latence et un débit élevé.
- **Scalabilité :** NIM supporte l’autoscaling sur Kubernetes, ce qui lui permet de gérer efficacement des charges de travail variables.
- **Sécurité et contrôle :** Les organisations peuvent garder le contrôle sur leurs données et applications en auto-hébergeant les microservices NIM sur leur propre infrastructure gérée.
- **APIs standard :** NIM fournit des APIs standard de l'industrie, ce qui facilite la création et l'intégration d'applications IA telles que les chatbots, assistants IA, et plus encore.

NIM fait partie de NVIDIA AI Enterprise, qui vise à simplifier le déploiement et l'opérationnalisation des modèles IA, en garantissant qu'ils fonctionnent efficacement sur les GPU NVIDIA.

- Démo : Utiliser NVIDIA NIM pour appeler Phi-3.5-Vision-API  [[Cliquez sur ce lien](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Exécuter Phi-3/3.5 localement
L'inférence en rapport avec Phi-3, ou tout modèle de langage comme GPT-3, fait référence au processus de génération de réponses ou de prédictions basées sur l'entrée qu'il reçoit. Lorsque vous fournissez une invite ou une question à Phi-3, il utilise son réseau neuronal entraîné pour inférer la réponse la plus probable et pertinente en analysant les motifs et relations dans les données sur lesquelles il a été entraîné.

**Hugging Face Transformer**
Hugging Face Transformers est une bibliothèque puissante conçue pour le traitement du langage naturel (NLP) et d'autres tâches d'apprentissage automatique. Voici quelques points clés à son sujet :

1. **Modèles pré-entraînés** : Elle propose des milliers de modèles pré-entraînés utilisables pour diverses tâches telles que classification de texte, reconnaissance d'entités nommées, réponses aux questions, résumé, traduction, et génération de texte.

2. **Interopérabilité des frameworks** : La bibliothèque supporte plusieurs frameworks d'apprentissage profond, dont PyTorch, TensorFlow et JAX. Cela vous permet d'entraîner un modèle dans un framework et de l'utiliser dans un autre.

3. **Capacités multimodales** : En plus du NLP, Hugging Face Transformers soutient également des tâches en vision par ordinateur (ex : classification d'images, détection d'objets) et traitement audio (ex : reconnaissance vocale, classification audio).

4. **Simplicité d'utilisation** : La bibliothèque offre des APIs et outils pour télécharger et affiner facilement les modèles, la rendant accessible aux débutants comme aux experts.

5. **Communauté et ressources** : Hugging Face dispose d'une communauté dynamique et d'une documentation étendue, tutoriels, et guides pour aider les utilisateurs à démarrer et tirer le meilleur de la bibliothèque.
[documentation officielle](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ou leur [dépôt GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

C’est la méthode la plus couramment utilisée, mais elle nécessite aussi une accélération GPU. Après tout, des scénarios tels que Vision et MoE requièrent beaucoup de calculs, ce qui sera très lent sur CPU s’ils ne sont pas quantifiés.


- Démo : Utiliser Transformer pour appeler Phi-3.5-Instruct [Cliquez sur ce lien](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Démo : Utiliser Transformer pour appeler Phi-3.5-Vision [Cliquez sur ce lien](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Démo : Utiliser Transformer pour appeler Phi-3.5-MoE [Cliquez sur ce lien](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) est une plateforme conçue pour faciliter l’exécution locale de grands modèles de langage (LLMs) sur votre machine. Elle supporte divers modèles comme Llama 3.1, Phi 3, Mistral, et Gemma 2, parmi d’autres. La plateforme simplifie le processus en regroupant poids du modèle, configuration, et données dans un seul package, rendant plus accessible la personnalisation et la création de vos propres modèles. Ollama est disponible pour macOS, Linux et Windows. C’est un excellent outil si vous souhaitez expérimenter ou déployer des LLM sans dépendre des services cloud. Ollama est la voie la plus directe, il vous suffit d’exécuter la commande suivante.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) est l’environnement d’exécution hors ligne et sur appareil de Microsoft pour exécuter des modèles comme Phi entièrement sur votre propre matériel - aucune souscription Azure, clé API, ou connexion réseau requise. Il sélectionne automatiquement le meilleur fournisseur d’exécution disponible (NPU, GPU, ou CPU) et expose un endpoint compatible OpenAI, pour que le code existant `openai`/Azure AI Inference SDK puisse s’y connecter avec des modifications minimales. Voir la [documentation Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pour démarrer.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Ou utilisez le SDK directement en Python :

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime pour GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) est un accélérateur multiplateforme d’inférence et d'entraînement en apprentissage automatique. ONNX Runtime pour l’Intelligence Artificielle Générative (GENAI) est un outil puissant qui vous aide à exécuter efficacement des modèles d’IA générative sur diverses plateformes.

## Qu’est-ce qu’ONNX Runtime ?
ONNX Runtime est un projet open source qui permet une inférence haute performance des modèles d’apprentissage automatique. Il supporte les modèles au format Open Neural Network Exchange (ONNX), qui est une norme pour représenter les modèles d’apprentissage automatique. L’inférence ONNX Runtime peut offrir une expérience client plus rapide et réduire les coûts, en supportant des modèles issus de frameworks de deep learning comme PyTorch et TensorFlow/Keras ainsi que des bibliothèques d’apprentissage automatique classiques telles que scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime est compatible avec différents matériels, pilotes et systèmes d’exploitation, et offre une performance optimale en tirant parti des accélérateurs matériels lorsque c’est possible, en plus des optimisations et transformations de graphe.

## Qu’est-ce que l’IA générative ?
L’IA générative désigne les systèmes d’IA capables de générer du contenu nouveau, comme du texte, des images ou de la musique, à partir des données sur lesquelles ils ont été entraînés. Des exemples incluent des modèles de langage comme GPT-3 et des modèles de génération d’images comme Stable Diffusion. La bibliothèque ONNX Runtime pour GenAI fournit la boucle d’IA générative pour les modèles ONNX, incluant l’inférence avec ONNX Runtime, le traitement des logits, la recherche et l’échantillonnage, ainsi que la gestion du cache KV.

## ONNX Runtime pour GENAI
ONNX Runtime pour GENAI étend les capacités d'ONNX Runtime pour prendre en charge les modèles d’IA générative. Voici quelques fonctionnalités clés :

- **Large prise en charge plateforme :** Il fonctionne sur diverses plateformes, y compris Windows, Linux, macOS, Android et iOS.
- **Support des modèles :** Il supporte de nombreux modèles populaires d’IA générative, tels que LLaMA, GPT-Neo, BLOOM, et plus encore.
- **Optimisation des performances :** Il inclut des optimisations pour différents accélérateurs matériels comme les GPU NVIDIA, AMD GPU, et plus2.
- **Facilité d’utilisation :** Il fournit des APIs pour une intégration facile dans les applications, vous permettant de générer du texte, des images et d’autres contenus avec un minimum de code.
- Les utilisateurs peuvent appeler une méthode generate() de haut niveau, ou exécuter chaque itération du modèle dans une boucle, générant un token à la fois, et mettant éventuellement à jour les paramètres de génération dans la boucle.
- ONNX runtime supporte aussi la recherche gloutonne/au faisceau et l’échantillonnage TopP, TopK pour générer des séquences de tokens ainsi que le traitement intégré des logits comme les pénalités de répétition. Vous pouvez également ajouter facilement un scoring personnalisé.

## Pour commencer
Pour débuter avec ONNX Runtime pour GENAI, vous pouvez suivre ces étapes :

### Installer ONNX Runtime :
```Python
pip install onnxruntime
```
### Installer les extensions d’IA générative :
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
### Démo : Utiliser ONNX Runtime GenAI pour appeler Phi-3.5-Vision


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

En plus des méthodes de référence ONNX Runtime, Ollama, et Foundry Local, nous pouvons également compléter la référence des modèles quantitatifs basés sur les méthodes de référence fournies par différents fabricants. Par exemple Apple MLX framework avec Apple Metal, Qualcomm QNN avec NPU, Intel OpenVINO avec CPU/GPU, etc. Vous pouvez également obtenir plus de contenu dans le [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Plus

Nous avons appris les bases de la famille Phi-3/3.5, mais pour en savoir plus sur SLM nous avons besoin de plus de connaissances. Vous pouvez trouver les réponses dans le Phi-3 Cookbook. Si vous souhaitez en apprendre davantage, veuillez visiter le [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->