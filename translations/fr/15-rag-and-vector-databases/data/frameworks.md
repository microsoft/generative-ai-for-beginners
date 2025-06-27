<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T22:52:17+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "fr"
}
-->
# Cadres de Réseaux Neuraux

Comme nous l'avons déjà appris, pour pouvoir entraîner des réseaux neuronaux efficacement, nous devons faire deux choses :

* Opérer sur des tenseurs, par exemple multiplier, additionner, et calculer certaines fonctions telles que sigmoid ou softmax
* Calculer les gradients de toutes les expressions, afin de réaliser l'optimisation par descente de gradient

Bien que la bibliothèque `numpy` puisse faire la première partie, nous avons besoin d'un mécanisme pour calculer les gradients. Dans notre cadre que nous avons développé dans la section précédente, nous devions programmer manuellement toutes les fonctions dérivées à l'intérieur de la méthode `backward`, qui fait la rétropropagation. Idéalement, un cadre devrait nous donner la possibilité de calculer les gradients de *n'importe quelle expression* que nous pouvons définir.

Un autre aspect important est de pouvoir effectuer des calculs sur GPU, ou sur tout autre unité de calcul spécialisée, telle que TPU. L'entraînement de réseaux neuronaux profonds nécessite *beaucoup* de calculs, et pouvoir paralléliser ces calculs sur les GPU est très important.

> ✅ Le terme 'paralléliser' signifie distribuer les calculs sur plusieurs appareils.

Actuellement, les deux cadres neuronaux les plus populaires sont : TensorFlow et PyTorch. Les deux fournissent une API de bas niveau pour opérer avec des tenseurs sur CPU et GPU. En plus de l'API de bas niveau, il existe également une API de haut niveau, appelée Keras et PyTorch Lightning respectivement.

API de Bas Niveau | TensorFlow| PyTorch
------------------|-------------------------------------|--------------------------------
API de Haut Niveau| Keras| Pytorch

**Les APIs de bas niveau** dans les deux cadres vous permettent de construire des **graphiques computationnels**. Ce graphique définit comment calculer la sortie (généralement la fonction de perte) avec des paramètres d'entrée donnés, et peut être envoyé pour calcul sur GPU, si disponible. Il existe des fonctions pour différencier ce graphique computationnel et calculer les gradients, qui peuvent ensuite être utilisés pour optimiser les paramètres du modèle.

**Les APIs de haut niveau** considèrent les réseaux neuronaux comme une **séquence de couches**, et rendent la construction de la plupart des réseaux neuronaux beaucoup plus facile. L'entraînement du modèle nécessite généralement de préparer les données puis d'appeler une fonction `fit` pour faire le travail.

L'API de haut niveau vous permet de construire des réseaux neuronaux typiques très rapidement sans vous soucier de nombreux détails. En même temps, l'API de bas niveau offre beaucoup plus de contrôle sur le processus d'entraînement, et est donc beaucoup utilisée en recherche, lorsque vous traitez de nouvelles architectures de réseaux neuronaux.

Il est également important de comprendre que vous pouvez utiliser les deux APIs ensemble, par exemple vous pouvez développer votre propre architecture de couche de réseau en utilisant l'API de bas niveau, puis l'utiliser à l'intérieur du réseau plus large construit et entraîné avec l'API de haut niveau. Ou vous pouvez définir un réseau en utilisant l'API de haut niveau comme une séquence de couches, puis utiliser votre propre boucle d'entraînement de bas niveau pour réaliser l'optimisation. Les deux APIs utilisent les mêmes concepts sous-jacents de base, et elles sont conçues pour bien fonctionner ensemble.

## Apprentissage

Dans ce cours, nous offrons la plupart du contenu à la fois pour PyTorch et TensorFlow. Vous pouvez choisir votre cadre préféré et ne parcourir que les carnets correspondants. Si vous n'êtes pas sûr de quel cadre choisir, lisez quelques discussions sur internet concernant **PyTorch vs. TensorFlow**. Vous pouvez également jeter un coup d'œil aux deux cadres pour mieux comprendre.

Dans la mesure du possible, nous utiliserons les APIs de haut niveau pour simplifier. Cependant, nous pensons qu'il est important de comprendre comment les réseaux neuronaux fonctionnent depuis le début, donc au départ, nous commençons par travailler avec l'API de bas niveau et les tenseurs. Cependant, si vous souhaitez avancer rapidement et ne pas passer beaucoup de temps à apprendre ces détails, vous pouvez les ignorer et passer directement aux carnets de l'API de haut niveau.

## ✍️ Exercices : Cadres

Continuez votre apprentissage dans les carnets suivants :

API de Bas Niveau | Carnet TensorFlow+Keras | PyTorch
------------------|-------------------------------------|--------------------------------
API de Haut Niveau| Keras | *PyTorch Lightning*

Après avoir maîtrisé les cadres, récapitulons la notion de surapprentissage.

# Surapprentissage

Le surapprentissage est un concept extrêmement important en apprentissage automatique, et il est très important de le comprendre correctement !

Considérons le problème suivant d'approximation de 5 points (représentés par `x` sur les graphiques ci-dessous) :

!linéaire | surajustement
-------------------------|--------------------------
**Modèle linéaire, 2 paramètres** | **Modèle non-linéaire, 7 paramètres**
Erreur d'entraînement = 5.3 | Erreur d'entraînement = 0
Erreur de validation = 5.1 | Erreur de validation = 20

* À gauche, nous voyons une bonne approximation par une ligne droite. Parce que le nombre de paramètres est adéquat, le modèle comprend correctement la distribution des points.
* À droite, le modèle est trop puissant. Parce que nous n'avons que 5 points et que le modèle a 7 paramètres, il peut s'ajuster de manière à passer par tous les points, rendant l'erreur d'entraînement à 0. Cependant, cela empêche le modèle de comprendre le bon schéma derrière les données, donc l'erreur de validation est très élevée.

Il est très important de trouver un bon équilibre entre la richesse du modèle (nombre de paramètres) et le nombre d'échantillons d'entraînement.

## Pourquoi le surapprentissage se produit-il

  * Pas assez de données d'entraînement
  * Modèle trop puissant
  * Trop de bruit dans les données d'entrée

## Comment détecter le surapprentissage

Comme vous pouvez le voir sur le graphique ci-dessus, le surapprentissage peut être détecté par une erreur d'entraînement très basse, et une erreur de validation élevée. Normalement, pendant l'entraînement, nous verrons les erreurs d'entraînement et de validation commencer à diminuer, puis à un moment donné l'erreur de validation pourrait arrêter de diminuer et commencer à augmenter. Ce sera un signe de surapprentissage, et l'indicateur que nous devrions probablement arrêter l'entraînement à ce stade (ou au moins faire une capture du modèle).

surapprentissage

## Comment prévenir le surapprentissage

Si vous voyez que le surapprentissage se produit, vous pouvez faire l'une des choses suivantes :

 * Augmenter la quantité de données d'entraînement
 * Diminuer la complexité du modèle
 * Utiliser une technique de régularisation, telle que Dropout, que nous considérerons plus tard.

## Surapprentissage et Compromis Biais-Variance

Le surapprentissage est en fait un cas d'un problème plus général en statistiques appelé Compromis Biais-Variance. Si nous considérons les sources possibles d'erreur dans notre modèle, nous pouvons voir deux types d'erreurs :

* **Erreurs de biais** causées par notre algorithme n'étant pas capable de capturer correctement la relation entre les données d'entraînement. Cela peut résulter du fait que notre modèle n'est pas assez puissant (**sous-apprentissage**).
* **Erreurs de variance**, qui sont causées par le modèle approximant le bruit dans les données d'entrée au lieu de la relation significative (**surapprentissage**).

Pendant l'entraînement, l'erreur de biais diminue (car notre modèle apprend à approximer les données), et l'erreur de variance augmente. Il est important d'arrêter l'entraînement - soit manuellement (lorsque nous détectons le surapprentissage) soit automatiquement (en introduisant la régularisation) - pour prévenir le surapprentissage.

## Conclusion

Dans cette leçon, vous avez appris les différences entre les diverses APIs pour les deux cadres d'IA les plus populaires, TensorFlow et PyTorch. De plus, vous avez appris sur un sujet très important, le surapprentissage.

## 🚀 Défi

Dans les carnets d'accompagnement, vous trouverez des 'tâches' en bas ; parcourez les carnets et complétez les tâches.

## Revue & Auto-étude

Faites des recherches sur les sujets suivants :

- TensorFlow
- PyTorch
- Surapprentissage

Posez-vous les questions suivantes :

- Quelle est la différence entre TensorFlow et PyTorch ?
- Quelle est la différence entre surapprentissage et sous-apprentissage ?

## Assignation

Dans ce laboratoire, vous êtes invité à résoudre deux problèmes de classification en utilisant des réseaux entièrement connectés à une seule couche et à plusieurs couches en utilisant PyTorch ou TensorFlow.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.