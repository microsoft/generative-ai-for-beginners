# Introduction aux petits modèles de langage pour l'IA générative pour débutants
L'IA générative est un domaine fascinant de l'intelligence artificielle qui se concentre sur la création de systèmes capables de générer de nouveaux contenus. Ces contenus peuvent aller du texte et des images à la musique et même à des environnements virtuels entiers. L'une des applications les plus passionnantes de l'IA générative est dans le domaine des modèles de langage.

## Qu'est-ce que les petits modèles de langage ?

Un petit modèle de langage (SLM) représente une version réduite d'un grand modèle de langage (LLM), tirant parti de nombreux principes architecturaux et techniques des LLM, tout en affichant une empreinte computationnelle nettement réduite.

Les SLM sont un sous-ensemble de modèles de langage conçus pour générer du texte humainement plausible. Contrairement à leurs homologues plus grands, tels que GPT-4, les SLM sont plus compacts et efficaces, ce qui les rend idéaux pour des applications où les ressources informatiques sont limitées. Malgré leur taille réduite, ils peuvent accomplir une variété de tâches. En général, les SLM sont construits en compressant ou distillant des LLM, dans le but de conserver une grande partie de la fonctionnalité originale et des capacités linguistiques du modèle. Cette réduction de la taille du modèle diminue la complexité globale, rendant les SLM plus efficaces en termes d'utilisation mémoire et d'exigences computationnelles. Malgré ces optimisations, les SLM peuvent encore réaliser une large gamme de tâches de traitement du langage naturel (NLP) :

- Génération de texte : création de phrases ou paragraphes cohérents et contextuellement pertinents.
- Complétion de texte : prédiction et complétion de phrases à partir d'une invite donnée.
- Traduction : conversion de texte d'une langue à une autre.
- Résumé : condensation de longs textes en résumés plus courts et digestes.

Bien entendu avec quelques compromis en termes de performance ou de profondeur de compréhension comparés à leurs homologues plus grands.

## Comment fonctionnent les petits modèles de langage ?
Les SLM sont entraînés sur d'immenses quantités de données textuelles. Pendant l'entraînement, ils apprennent les schémas et structures du langage, leur permettant de générer du texte qui est à la fois grammaticalement correct et contextuellement approprié. Le processus d’entraînement comprend :

- Collecte de données : assemblage de larges ensembles de textes provenant de diverses sources.
- Prétraitement : nettoyage et organisation des données pour les rendre adaptées à la formation.
- Formation : utilisation d’algorithmes d’apprentissage automatique pour enseigner au modèle comment comprendre et générer du texte.
- Ajustement fin (fine-tuning) : adaptation du modèle pour améliorer sa performance sur des tâches spécifiques.

Le développement des SLM répond au besoin croissant de modèles déployables dans des environnements à ressources limitées, tels que les appareils mobiles ou les plateformes de calcul en périphérie (edge computing), où les LLM à pleine échelle peuvent être impraticables en raison de leurs fortes exigences en ressources. En se concentrant sur l'efficacité, les SLM équilibrent performance et accessibilité, permettant une application plus large dans différents domaines.

![slm](../../../translated_images/fr/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Objectifs d'apprentissage

Dans cette leçon, nous espérons introduire les connaissances sur les SLM et les combiner avec Microsoft Phi-3 pour apprendre différents scénarios dans le contenu texte, la vision et MoE.

À la fin de cette leçon, vous devriez être capable de répondre aux questions suivantes :

- Qu'est-ce que le SLM ?
- Quelle est la différence entre SLM et LLM ?
- Qu'est-ce que la famille Microsoft Phi-3/3.5 ?
- Comment exécuter une inférence avec la famille Microsoft Phi-3/3.5 ?

Prêt ? Commençons.

## Les distinctions entre les grands modèles de langage (LLM) et les petits modèles de langage (SLM)

Les LLM et les SLM reposent tous deux sur les principes fondamentaux de l'apprentissage automatique probabiliste, suivant des approches similaires dans leur conception architecturale, leurs méthodologies de formation, leurs processus de génération de données et leurs techniques d’évaluation des modèles. Cependant, plusieurs facteurs clés différencient ces deux types de modèles.

## Applications des petits modèles de langage

Les SLM ont une large gamme d'applications, notamment :

- Chatbots : fourniture d'un support client et interaction avec les utilisateurs de manière conversationnelle.
- Création de contenu : assistance aux rédacteurs en générant des idées ou même en rédigeant des articles entiers.
- Éducation : aide aux étudiants pour leurs travaux d’écriture ou l’apprentissage de nouvelles langues.
- Accessibilité : création d’outils pour les personnes en situation de handicap, tels que les systèmes de synthèse vocale.

**Taille**
  
Une distinction principale entre les LLM et les SLM réside dans l'échelle des modèles. Les LLM, comme ChatGPT (GPT-4), peuvent comprendre environ 1,76 trillion de paramètres, tandis que les SLM open-source comme Mistral 7B sont conçus avec beaucoup moins de paramètres – environ 7 milliards. Ce décalage est principalement dû à des différences dans l'architecture du modèle et les processus de formation. Par exemple, ChatGPT utilise un mécanisme d’attention auto-régressive dans une architecture encodeur-décodeur, tandis que Mistral 7B utilise une attention par fenêtre coulissante, ce qui permet une formation plus efficace dans un modèle uniquement décodeur. Cette différence architecturale a des implications profondes sur la complexité et la performance de ces modèles.

**Compréhension**

Les SLM sont typiquement optimisés pour la performance dans des domaines spécifiques, ce qui les rend très spécialisés mais potentiellement limités dans leur capacité à fournir une compréhension contextuelle large à travers plusieurs champs de connaissances. En revanche, les LLM visent à simuler une intelligence humaine sur un niveau plus global. Formés sur des ensembles de données vastes et diversifiés, les LLM sont conçus pour bien fonctionner dans divers domaines, offrant ainsi plus de polyvalence et d'adaptabilité. Par conséquent, les LLM conviennent mieux à une gamme plus large de tâches en aval, comme le traitement du langage naturel et la programmation.

**Calcul**

L'entraînement et le déploiement des LLM sont des processus gourmands en ressources, nécessitant souvent des infrastructures informatiques importantes, incluant des clusters GPU à grande échelle. Par exemple, entraîner un modèle comme ChatGPT depuis zéro peut nécessiter des milliers de GPU sur de longues périodes. En revanche, les SLM, avec leur nombre plus faible de paramètres, sont plus accessibles en termes de ressources informatiques. Des modèles comme Mistral 7B peuvent être entraînés et exécutés sur des machines locales équipées de capacités GPU modérées, bien que la formation nécessite encore plusieurs heures sur plusieurs GPU.

**Biais**

Le biais est un problème connu dans les LLM, principalement dû à la nature des données d'entraînement. Ces modèles s’appuient souvent sur des données brutes, disponibles librement sur internet, qui peuvent sous-représenter ou déformer certains groupes, introduire des erreurs d'étiquetage, ou refléter des biais linguistiques influencés par des dialectes, des variations géographiques et des règles grammaticales. De plus, la complexité des architectures LLM peut involontairement accentuer ces biais, qui peuvent passer inaperçus sans un ajustement fin rigoureux. En revanche, les SLM, formés sur des ensembles de données plus restreints et spécifiques au domaine, sont intrinsèquement moins susceptibles à ces biais, bien qu'ils n'en soient pas exempts.

**Inférence**

La taille réduite des SLM leur confère un avantage significatif en termes de vitesse d'inférence, leur permettant de générer des résultats efficacement sur du matériel local sans nécessiter un traitement parallèle étendu. En revanche, les LLM, en raison de leur taille et complexité, requièrent souvent des ressources de calcul parallèles importantes pour obtenir des temps d'inférence acceptables. La présence de nombreux utilisateurs simultanés ralentit encore davantage les temps de réponse des LLM, surtout déployés à grande échelle.

En résumé, bien que LLM et SLM partagent une base fondamentale en apprentissage automatique, ils diffèrent significativement en termes de taille du modèle, exigences en ressources, compréhension contextuelle, susceptibilité aux biais, et vitesse d'inférence. Ces distinctions reflètent leur adéquation respective à différents cas d'utilisation, les LLM étant plus polyvalents mais gourmands en ressources, tandis que les SLM offrent une efficacité plus ciblée sur le domaine avec des exigences de calcul réduites.

***Note : Dans cette leçon, nous présenterons les SLM en utilisant Microsoft Phi-3 / 3.5 comme exemple.***

## Présentation de la famille Phi-3 / Phi-3.5

La famille Phi-3 / 3.5 cible principalement les scénarios d’application texte, vision et Agent (MoE) :

### Phi-3 / 3.5 Instruct

Principalement pour la génération de texte, la complétion de conversations, et l'extraction d'informations de contenu, etc.

**Phi-3-mini**

Le modèle de langage de 3.8B paramètres est disponible sur Microsoft Foundry, Hugging Face, et Ollama. Les modèles Phi-3 surpassent nettement les modèles de langage de tailles égales et supérieures sur les principaux benchmarks (voir les chiffres des benchmarks ci-dessous, des chiffres plus élevés sont meilleurs). Phi-3-mini dépasse des modèles deux fois plus grands, tandis que Phi-3-small et Phi-3-medium surpassent des modèles plus grands, y compris GPT-3.5.

**Phi-3-small & medium**

Avec seulement 7 milliards de paramètres, Phi-3-small bat GPT-3.5T sur diverses évaluations en langue, raisonnement, codage, et mathématiques.

Le Phi-3-medium avec 14 milliards de paramètres poursuit cette tendance et dépasse le Gemini 1.0 Pro.

**Phi-3.5-mini**

On peut le considérer comme une mise à jour du Phi-3-mini. Bien que le nombre de paramètres reste inchangé, il améliore la capacité à supporter plusieurs langues (prise en charge de plus de 20 langues : arabe, chinois, tchèque, danois, néerlandais, anglais, finnois, français, allemand, hébreu, hongrois, italien, japonais, coréen, norvégien, polonais, portugais, russe, espagnol, suédois, thaï, turc, ukrainien) et ajoute un meilleur support pour les longs contextes.

Phi-3.5-mini avec 3.8 milliards de paramètres dépasse les modèles de même taille et est comparable aux modèles deux fois plus grands.

### Phi-3 / 3.5 Vision

On peut considérer le modèle Instruct de Phi-3/3.5 comme la capacité de Phi à comprendre, et la Vision comme ce qui donne à Phi des yeux pour comprendre le monde.


**Phi-3-Vision**

Phi-3-vision, avec seulement 4.2 milliards de paramètres, poursuit cette tendance et dépasse des modèles plus grands tels que Claude-3 Haiku et Gemini 1.0 Pro V sur des tâches générales de raisonnement visuel, OCR, ainsi qu’à la compréhension de tableaux et diagrammes.


**Phi-3.5-Vision**

Phi-3.5-Vision est aussi une mise à jour du Phi-3-Vision, ajoutant le support pour plusieurs images. On peut le voir comme une amélioration en vision, non seulement vous pouvez voir des images, mais aussi des vidéos.

Phi-3.5-vision dépasse des modèles plus grands tels que Claude-3.5 Sonnet et Gemini 1.5 Flash sur les tâches OCR, compréhension de tableaux et graphiques, et est équivalent sur des tâches générales de raisonnement de connaissances visuelles. Supporte les entrées multi-images, c’est-à-dire peut effectuer un raisonnement sur plusieurs images d'entrée.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** permet aux modèles d’être pré-entraînés avec beaucoup moins de calcul, ce qui signifie que vous pouvez augmenter considérablement la taille du modèle ou du dataset avec le même budget de calcul qu’un modèle dense. En particulier, un modèle MoE devrait atteindre la même qualité que son homologue dense beaucoup plus rapidement durant le pré-entraînement.

Phi-3.5-MoE comprend 16 modules experts de 3.8 milliards chacun. Phi-3.5-MoE, avec seulement 6.6 milliards de paramètres actifs, atteint un niveau semblable de raisonnement, de compréhension du langage, et de mathématiques que des modèles beaucoup plus grands.

Nous pouvons utiliser le modèle de la famille Phi-3/3.5 selon différents scénarios. Contrairement aux LLM, vous pouvez déployer Phi-3/3.5-mini ou Phi-3/3.5-Vision sur des appareils en périphérie.


## Comment utiliser les modèles de la famille Phi-3/3.5

Nous espérons utiliser Phi-3/3.5 dans différents scénarios. Ensuite, nous utiliserons Phi-3/3.5 selon différents scénarios.

![phi3](../../../translated_images/fr/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inférence via les APIs Cloud

**Microsoft Foundry Models**

> **Note :** GitHub Models sera retiré fin juillet 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) est le remplaçant direct.

> **Note :** Toute la famille Phi-3/3.5 (variantes Instruct, Vision, et MoE) a été retirée du catalogue Microsoft Foundry Models le 30-08-2025. Utilisez `Phi-4` (Instruct) ou `Phi-4-mini-instruct` là-bas à la place — les exemples Phi-3/3.5 ci-dessous fonctionnent toujours via Hugging Face, Ollama, ONNX Runtime, et NVIDIA NIM.

Microsoft Foundry Models fournit désormais les successeurs Phi-4. Utilisez `Phi-4` ou `Phi-4-mini-instruct` au lieu des modèles Phi-3/3.5 retirés lorsque vous suivez les exemples d'API cloud.

- Démo : comparaison des effets de Phi-3-mini et Phi-3.5-mini dans des scénarios en chinois

![phi3](../../../translated_images/fr/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/fr/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Si vous souhaitez utiliser des modèles vision (multimodaux) dans le cloud, utilisez `Phi-4-multimodal-instruct` actuellement disponible via Microsoft Foundry au lieu des modèles Phi-3/3.5 Vision retirés ; pour les tâches de texte, utilisez `Phi-4` ou `Phi-4-mini-instruct`. Le modèle Phi-3.5 MoE a été retiré de Microsoft Foundry, utilisez donc les autres options décrites dans cette leçon (par exemple Hugging Face) si vous souhaitez l'expérimenter. Si cela vous intéresse, vous pouvez lire le Phi Cookbook pour apprendre comment appeler les modèles Phi via Microsoft Foundry [Cliquez sur ce lien](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

En plus du catalogue Microsoft Foundry Models basé sur le cloud, vous pouvez également utiliser [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) pour effectuer les appels associés. Vous pouvez visiter NVIDIA NIM pour réaliser les appels API de la famille Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) est un ensemble de microservices d'inférence accélérée conçus pour aider les développeurs à déployer efficacement des modèles IA dans divers environnements, y compris les clouds, les centres de données, et les stations de travail.

Voici quelques fonctionnalités clés de NVIDIA NIM :

- **Facilité de déploiement :** NIM permet le déploiement de modèles d'IA avec une seule commande, ce qui facilite son intégration dans les flux de travail existants.
- **Performance optimisée :** Il exploite les moteurs d'inférence pré-optimisés de NVIDIA, tels que TensorRT et TensorRT-LLM, pour garantir une faible latence et un débit élevé.
- **Scalabilité :** NIM prend en charge l'autoscaling sur Kubernetes, lui permettant de gérer efficacement des charges de travail variables.
- **Sécurité et contrôle :** Les organisations peuvent garder le contrôle sur leurs données et applications en hébergeant elles-mêmes les microservices NIM sur leur propre infrastructure gérée.
- **API standard :** NIM fournit des API standards de l'industrie, facilitant la création et l'intégration d'applications IA comme les chatbots, assistants IA, et plus encore.

NIM fait partie de NVIDIA AI Enterprise, qui vise à simplifier le déploiement et l'opérationnalisation des modèles IA, en garantissant leur fonctionnement efficace sur les GPU NVIDIA.

- Démo : Utilisation de NVIDIA NIM pour appeler Phi-3.5-Vision-API  [[Cliquez sur ce lien](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Exécuter Phi-3/3.5 localement
L'inférence en relation avec Phi-3, ou tout modèle linguistique comme GPT-3, fait référence au processus de génération de réponses ou de prédictions basées sur les entrées reçues. Lorsque vous fournissez une invite ou une question à Phi-3, il utilise son réseau neuronal entraîné pour déduire la réponse la plus probable et pertinente en analysant les motifs et les relations dans les données sur lesquelles il a été formé.

**Hugging Face Transformer**
Hugging Face Transformers est une bibliothèque puissante conçue pour le traitement du langage naturel (NLP) et autres tâches d'apprentissage automatique. Voici quelques points clés à son sujet :

1. **Modèles pré-entraînés** : Elle fournit des milliers de modèles pré-entraînés pouvant être utilisés pour diverses tâches telles que la classification de texte, la reconnaissance d'entités nommées, la réponse à des questions, le résumé, la traduction et la génération de texte.

2. **Interopérabilité des frameworks** : La bibliothèque prend en charge plusieurs frameworks d'apprentissage profond, notamment PyTorch, TensorFlow, et JAX. Cela vous permet d'entraîner un modèle dans un framework et de l'utiliser dans un autre.

3. **Capacités multimodales** : En plus du NLP, Hugging Face Transformers prend également en charge des tâches en vision par ordinateur (par exemple classification d'images, détection d'objets) et en traitement audio (par exemple reconnaissance vocale, classification audio).

4. **Facilité d'utilisation** : La bibliothèque offre des API et des outils pour télécharger facilement et affiner des modèles, la rendant accessible aussi bien aux débutants qu'aux experts.

5. **Communauté et ressources** : Hugging Face dispose d'une communauté dynamique ainsi que d'une documentation, de tutoriels et de guides étendus pour aider les utilisateurs à démarrer et à tirer le meilleur parti de la bibliothèque.
[documentation officielle](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ou leur [dépôt GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

C'est la méthode la plus courante, mais elle nécessite aussi une accélération GPU. Après tout, des scénarios tels que Vision et MoE demandent beaucoup de calculs, ce qui sera très lent sur CPU s'ils ne sont pas quantifiés.


- Démo : Utilisation de Transformer pour appeler Phi-3.5-Instruct [Cliquez sur ce lien](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Démo : Utilisation de Transformer pour appeler Phi-3.5-Vision [Cliquez sur ce lien](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Démo : Utilisation de Transformer pour appeler Phi-3.5-MoE [Cliquez sur ce lien](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) est une plateforme conçue pour faciliter l'exécution locale de grands modèles de langage (LLM) sur votre machine. Elle prend en charge divers modèles comme Llama 3.1, Phi 3, Mistral, et Gemma 2, entre autres. La plateforme simplifie le processus en regroupant les poids du modèle, la configuration et les données en un seul paquet, ce qui la rend plus accessible pour les utilisateurs souhaitant personnaliser et créer leurs propres modèles. Ollama est disponible pour macOS, Linux et Windows. C’est un excellent outil si vous souhaitez expérimenter ou déployer des LLM sans dépendre des services cloud. Ollama est la manière la plus directe, il vous suffit d'exécuter la commande suivante.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) est l'environnement d'exécution hors ligne, sur appareil, de Microsoft pour exécuter des modèles comme Phi entièrement sur votre propre matériel - pas d'abonnement Azure, ni clé API, ni connexion réseau requise. Il choisit automatiquement le meilleur fournisseur d'exécution disponible (NPU, GPU ou CPU) et expose un point de terminaison compatible OpenAI, de sorte que le code existant `openai`/Azure AI Inference SDK puisse y pointer avec un minimum de modifications. Voir la [documentation Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pour démarrer.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) est un accélérateur multiplateforme d'inférence et d'entraînement pour l'apprentissage automatique. ONNX Runtime pour Generative AI (GENAI) est un outil puissant qui vous aide à exécuter efficacement des modèles d'IA générative sur diverses plateformes.

## Qu'est-ce que ONNX Runtime ?
ONNX Runtime est un projet open-source qui permet l'inférence haute performance de modèles d'apprentissage automatique. Il prend en charge les modèles au format Open Neural Network Exchange (ONNX), qui est une norme pour représenter les modèles d'apprentissage automatique. L'inférence avec ONNX Runtime peut permettre des expériences client plus rapides et des coûts réduits, prenant en charge des modèles issus de frameworks d'apprentissage profond comme PyTorch et TensorFlow/Keras ainsi que des bibliothèques classiques d'apprentissage automatique comme scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime est compatible avec différents matériels, pilotes et systèmes d'exploitation, et offre des performances optimales en exploitant les accélérateurs matériels lorsque cela est possible, conjointement avec des optimisations et transformations des graphes.

## Qu'est-ce que l'IA générative ?
L'IA générative désigne les systèmes d'IA capables de générer de nouveaux contenus, tels que du texte, des images ou de la musique, à partir des données sur lesquelles ils ont été entraînés. Les exemples incluent les modèles de langage comme GPT-3 et les modèles de génération d'images comme Stable Diffusion. La bibliothèque ONNX Runtime pour GenAI fournit la boucle d'IA générative pour les modèles ONNX, y compris l'inférence avec ONNX Runtime, le traitement des logits, la recherche et l'échantillonnage, ainsi que la gestion du cache KV.

## ONNX Runtime pour GENAI
ONNX Runtime pour GENAI étend les capacités d'ONNX Runtime pour supporter les modèles d'IA générative. Voici quelques fonctionnalités clés :

- **Support étendu des plateformes :** Il fonctionne sur diverses plateformes, notamment Windows, Linux, macOS, Android et iOS.
- **Support des modèles :** Il prend en charge de nombreux modèles populaires d'IA générative, tels que LLaMA, GPT-Neo, BLOOM, et d'autres.
- **Optimisation des performances :** Il inclut des optimisations pour différents accélérateurs matériels comme les GPU NVIDIA, GPU AMD, et plus encore2.
- **Facilité d'utilisation :** Il fournit des API pour une intégration facile dans les applications, vous permettant de générer du texte, des images et d'autres contenus avec un code minimal
- Les utilisateurs peuvent appeler une méthode generate() de haut niveau, ou exécuter chaque itération du modèle dans une boucle, générant un jeton à la fois, et en mettant éventuellement à jour les paramètres de génération dans la boucle.
- ONNX runtime prend également en charge la recherche gourmande/à faisceaux et l'échantillonnage TopP, TopK pour générer des séquences de jetons ainsi que le traitement intégré des logits comme les pénalités de répétition. Vous pouvez aussi facilement ajouter un scoring personnalisé.

## Pour commencer
Pour commencer avec ONNX Runtime pour GENAI, vous pouvez suivre ces étapes :

### Installer ONNX Runtime :
```Python
pip install onnxruntime
```
### Installer les extensions d'IA générative :
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

En plus d'ONNX Runtime, Ollama, et Foundry Local comme méthodes de référence, nous pouvons également compléter la référence des modèles quantitatifs basés sur les méthodes de référence des modèles fournies par différents fabricants. Par exemple le framework Apple MLX avec Apple Metal, Qualcomm QNN avec NPU, Intel OpenVINO avec CPU/GPU, etc. Vous pouvez également obtenir plus de contenu dans le [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Plus

Nous avons appris les bases de la famille Phi-3/3.5, mais pour en savoir plus sur SLM, nous avons besoin de plus de connaissances. Vous pouvez trouver les réponses dans le Phi-3 Cookbook. Si vous souhaitez en savoir plus, veuillez visiter le [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->