[![Modèles Open Source](../../../translated_images/16-lesson-banner.png?WT.a9a13a59f0350adb5846e88fb3aba98cd4c6cb3297e78cb7100938f45b7dac47.fr.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Introduction

Le monde des LLM open source est passionnant et en constante évolution. Cette leçon vise à fournir un aperçu approfondi des modèles open source. Si vous cherchez des informations sur la comparaison entre les modèles propriétaires et les modèles open source, rendez-vous à la leçon ["Exploration et comparaison des différents LLMs"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Cette leçon abordera également le sujet du réglage fin, mais une explication plus détaillée peut être trouvée dans la leçon ["Réglage fin des LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Objectifs d'apprentissage

- Comprendre les modèles open source
- Comprendre les avantages de travailler avec des modèles open source
- Explorer les modèles open disponibles sur Hugging Face et Azure AI Studio

## Qu'est-ce que les Modèles Open Source ?

Les logiciels open source ont joué un rôle crucial dans la croissance de la technologie dans divers domaines. L'Open Source Initiative (OSI) a défini [10 critères pour les logiciels](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) pour être classifiés comme open source. Le code source doit être partagé ouvertement sous une licence approuvée par l'OSI.

Bien que le développement des LLMs ait des éléments similaires au développement de logiciels, le processus n'est pas exactement le même. Cela a suscité de nombreuses discussions dans la communauté sur la définition de l'open source dans le contexte des LLMs. Pour qu'un modèle soit aligné avec la définition traditionnelle de l'open source, les informations suivantes doivent être publiquement disponibles :

- Ensembles de données utilisés pour entraîner le modèle.
- Poids complets du modèle dans le cadre de l'entraînement.
- Le code d'évaluation.
- Le code de réglage fin.
- Poids complets du modèle et métriques d'entraînement.

Il n'existe actuellement que quelques modèles qui répondent à ces critères. Le [modèle OLMo créé par l'Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) est l'un de ceux qui correspondent à cette catégorie.

Pour cette leçon, nous nous référerons aux modèles comme "modèles open" à l'avenir, car ils peuvent ne pas correspondre aux critères ci-dessus au moment de la rédaction.

## Avantages des Modèles Open

**Hautement personnalisable** - Étant donné que les modèles open sont publiés avec des informations d'entraînement détaillées, les chercheurs et développeurs peuvent modifier les internes du modèle. Cela permet de créer des modèles hautement spécialisés qui sont ajustés pour une tâche ou un domaine d'étude spécifique. Quelques exemples de cela incluent la génération de code, les opérations mathématiques et la biologie.

**Coût** - Le coût par token pour utiliser et déployer ces modèles est inférieur à celui des modèles propriétaires. Lors de la création d'applications d'IA générative, il est important de comparer la performance au prix lors de l'utilisation de ces modèles pour votre cas d'utilisation.

![Coût du Modèle](../../../translated_images/model-price.png?WT.473bad4fe5bdb7014798275047130c0949da1e4a3d6f379037bedf68ef1d5e42.fr.mc_id=academic-105485-koreyst)  
Source : Artificial Analysis

**Flexibilité** - Travailler avec des modèles open vous permet d'être flexible en termes d'utilisation de différents modèles ou de leur combinaison. Un exemple de cela est les [Assistants HuggingChat](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) où un utilisateur peut sélectionner le modèle utilisé directement dans l'interface utilisateur :

![Choisir le Modèle](../../../translated_images/choose-model.png?WT.50da8a7caba083003bcf9f71017d17715f032acff67359c11c9886597ca3efdc.fr.mc_id=academic-105485-koreyst)

## Explorer Différents Modèles Open

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), développé par Meta, est un modèle open optimisé pour les applications basées sur le chat. Cela est dû à sa méthode de réglage fin, qui inclut une grande quantité de dialogues et de retours humains. Avec cette méthode, le modèle produit plus de résultats alignés sur les attentes humaines, ce qui offre une meilleure expérience utilisateur.

Quelques exemples de versions ajustées de Llama incluent [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), qui se spécialise dans le japonais, et [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), qui est une version améliorée du modèle de base.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) est un modèle open avec un fort accent sur la haute performance et l'efficacité. Il utilise l'approche Mixture-of-Experts qui combine un groupe de modèles experts spécialisés en un seul système où, selon l'entrée, certains modèles sont sélectionnés pour être utilisés. Cela rend le calcul plus efficace car les modèles ne traitent que les entrées pour lesquelles ils sont spécialisés.

Quelques exemples de versions ajustées de Mistral incluent [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), qui se concentre sur le domaine médical, et [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), qui effectue des calculs mathématiques.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) est un LLM créé par le Technology Innovation Institute (**TII**). Le Falcon-40B a été entraîné sur 40 milliards de paramètres, ce qui a montré qu'il performe mieux que GPT-3 avec un budget de calcul moindre. Cela est dû à son utilisation de l'algorithme FlashAttention et de l'attention multi-query qui lui permet de réduire les exigences en mémoire lors de l'inférence. Avec ce temps d'inférence réduit, le Falcon-40B est adapté pour les applications de chat.

Quelques exemples de versions ajustées de Falcon sont [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), un assistant construit sur des modèles open, et [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), qui offre des performances supérieures au modèle de base.

## Comment Choisir

Il n'y a pas de réponse unique pour choisir un modèle open. Un bon point de départ est d'utiliser la fonction de filtre par tâche de l'Azure AI Studio. Cela vous aidera à comprendre quels types de tâches le modèle a été entraîné à réaliser. Hugging Face maintient également un classement des LLM qui vous montre les modèles les plus performants selon certains critères.

Lors de la comparaison des LLMs entre les différents types, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) est une autre excellente ressource :

![Qualité du Modèle](../../../translated_images/model-quality.png?WT.bffdb0b01a3f3205153df83585941f90a153017f607dbcfad9cde5369764f203.fr.mc_id=academic-105485-koreyst)  
Source : Artificial Analysis

Si vous travaillez sur un cas d'utilisation spécifique, rechercher des versions ajustées qui se concentrent sur le même domaine peut être efficace. Expérimenter avec plusieurs modèles open pour voir comment ils se comportent selon vos attentes et celles de vos utilisateurs est une autre bonne pratique.

## Prochaines Étapes

La meilleure partie des modèles open est que vous pouvez commencer à travailler avec eux assez rapidement. Consultez le [Catalogue de Modèles Azure AI Studio](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), qui propose une collection spécifique de Hugging Face avec les modèles que nous avons discutés ici.

## L'apprentissage ne s'arrête pas ici, continuez le Voyage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage de l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances en IA générative !

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.