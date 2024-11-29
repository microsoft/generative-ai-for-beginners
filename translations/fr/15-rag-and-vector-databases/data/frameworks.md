# Cadres de Réseaux Neuraux

Comme nous l'avons déjà appris, pour pouvoir entraîner des réseaux neuronaux efficacement, nous devons faire deux choses :

* Opérer sur des tenseurs, par exemple pour multiplier, additionner et calculer certaines fonctions telles que sigmoid ou softmax
* Calculer les gradients de toutes les expressions, afin de réaliser l'optimisation par descente de gradient

Bien que la bibliothèque `numpy` puisse faire la première partie, nous avons besoin d'un mécanisme pour calculer les gradients. Dans notre cadre que nous avons développé dans la section précédente, nous devions programmer manuellement toutes les fonctions dérivées à l'intérieur de la méthode `backward`, qui effectue la rétropropagation. Idéalement, un cadre devrait nous offrir la possibilité de calculer les gradients de *n'importe quelle expression* que nous pouvons définir.

Un autre aspect important est de pouvoir effectuer des calculs sur GPU, ou sur toute autre unité de calcul spécialisée, comme le TPU. L'entraînement de réseaux neuronaux profonds nécessite *beaucoup* de calculs, et pouvoir paralléliser ces calculs sur les GPU est très important.

> ✅ Le terme 'paralléliser' signifie distribuer les calculs sur plusieurs dispositifs.

Actuellement, les deux cadres neuronaux les plus populaires sont : TensorFlow et PyTorch. Les deux fournissent une API de bas niveau pour opérer avec des tenseurs à la fois sur CPU et GPU. En plus de l'API de bas niveau, il existe également une API de plus haut niveau, appelée Keras et PyTorch Lightning respectivement.

API de Bas Niveau | TensorFlow| PyTorch
-------------------|-------------------------------------|--------------------------------
API de Haut Niveau | Keras| Pytorch

**Les API de bas niveau** dans les deux cadres vous permettent de construire ce qu'on appelle des **graphes computationnels**. Ce graphe définit comment calculer la sortie (généralement la fonction de perte) avec des paramètres d'entrée donnés, et peut être envoyé pour calcul sur GPU, si disponible. Il existe des fonctions pour différencier ce graphe computationnel et calculer les gradients, qui peuvent ensuite être utilisés pour optimiser les paramètres du modèle.

**Les API de haut niveau** considèrent essentiellement les réseaux neuronaux comme une **séquence de couches**, et facilitent la construction de la plupart des réseaux neuronaux. L'entraînement du modèle nécessite généralement de préparer les données puis d'appeler une fonction `fit` pour faire le travail.

L'API de haut niveau vous permet de construire des réseaux neuronaux typiques très rapidement sans vous soucier de nombreux détails. En même temps, les API de bas niveau offrent beaucoup plus de contrôle sur le processus d'entraînement, et sont donc beaucoup utilisées en recherche, lorsque vous travaillez avec de nouvelles architectures de réseaux neuronaux.

Il est également important de comprendre que vous pouvez utiliser les deux API ensemble, par exemple, vous pouvez développer votre propre architecture de couche de réseau en utilisant l'API de bas niveau, puis l'utiliser à l'intérieur du réseau plus large construit et entraîné avec l'API de haut niveau. Ou vous pouvez définir un réseau en utilisant l'API de haut niveau comme une séquence de couches, puis utiliser votre propre boucle d'entraînement de bas niveau pour effectuer l'optimisation. Les deux API utilisent les mêmes concepts de base sous-jacents, et elles sont conçues pour bien fonctionner ensemble.

## Apprentissage

Dans ce cours, nous proposons la plupart du contenu à la fois pour PyTorch et TensorFlow. Vous pouvez choisir votre cadre préféré et parcourir uniquement les notebooks correspondants. Si vous n'êtes pas sûr de quel cadre choisir, lisez quelques discussions sur Internet concernant **PyTorch vs. TensorFlow**. Vous pouvez également jeter un œil aux deux cadres pour mieux comprendre.

Dans la mesure du possible, nous utiliserons les API de haut niveau pour plus de simplicité. Cependant, nous pensons qu'il est important de comprendre comment fonctionnent les réseaux neuronaux depuis la base, donc au début, nous commençons par travailler avec l'API de bas niveau et les tenseurs. Cependant, si vous souhaitez avancer rapidement et ne pas passer beaucoup de temps à apprendre ces détails, vous pouvez les ignorer et passer directement aux notebooks de l'API de haut niveau.

## ✍️ Exercices : Cadres

Poursuivez votre apprentissage dans les notebooks suivants :

API de Bas Niveau | Notebook TensorFlow+Keras | PyTorch
-------------------|-------------------------------------|--------------------------------
API de Haut Niveau | Keras | *PyTorch Lightning*

Après avoir maîtrisé les cadres, récapitulons la notion de surapprentissage.

# Surapprentissage

Le surapprentissage est un concept extrêmement important en apprentissage automatique, et il est très important de bien le comprendre !

Considérons le problème suivant d'approximation de 5 points (représentés par `x` sur les graphiques ci-dessous) :

!linéaire | surajusté
-------------------------|--------------------------
**Modèle linéaire, 2 paramètres** | **Modèle non-linéaire, 7 paramètres**
Erreur d'entraînement = 5.3 | Erreur d'entraînement = 0
Erreur de validation = 5.1 | Erreur de validation = 20

* À gauche, nous voyons une bonne approximation par ligne droite. Parce que le nombre de paramètres est adéquat, le modèle comprend correctement la distribution des points.
* À droite, le modèle est trop puissant. Parce que nous n'avons que 5 points et que le modèle a 7 paramètres, il peut s'ajuster de manière à passer par tous les points, rendant l'erreur d'entraînement égale à 0. Cependant, cela empêche le modèle de comprendre le bon schéma derrière les données, d'où l'erreur de validation très élevée.

Il est très important de trouver un bon équilibre entre la richesse du modèle (nombre de paramètres) et le nombre d'échantillons d'entraînement.

## Pourquoi le surapprentissage se produit-il ?

  * Pas assez de données d'entraînement
  * Modèle trop puissant
  * Trop de bruit dans les données d'entrée

## Comment détecter le surapprentissage

Comme vous pouvez le voir sur le graphique ci-dessus, le surapprentissage peut être détecté par une erreur d'entraînement très faible et une erreur de validation élevée. Normalement, pendant l'entraînement, nous verrons à la fois les erreurs d'entraînement et de validation commencer à diminuer, puis à un moment donné, l'erreur de validation pourrait cesser de diminuer et commencer à augmenter. Ce sera un signe de surapprentissage, et l'indicateur que nous devrions probablement arrêter l'entraînement à ce moment-là (ou au moins faire une capture du modèle).

## Comment prévenir le surapprentissage

Si vous constatez que le surapprentissage se produit, vous pouvez faire l'une des choses suivantes :

 * Augmenter la quantité de données d'entraînement
 * Réduire la complexité du modèle
 * Utiliser une technique de régularisation, telle que Dropout, que nous examinerons plus tard.

## Surapprentissage et Compromis Biais-Variance

Le surapprentissage est en fait un cas d'un problème plus général en statistiques appelé Compromis Biais-Variance. Si nous considérons les sources possibles d'erreur dans notre modèle, nous pouvons voir deux types d'erreurs :

* **Erreurs de biais** causées par notre algorithme qui n'est pas capable de capturer correctement la relation entre les données d'entraînement. Cela peut résulter du fait que notre modèle n'est pas assez puissant (**sous-ajustement**).
* **Erreurs de variance**, qui sont causées par le modèle qui approxime le bruit dans les données d'entrée au lieu d'une relation significative (**surajustement**).

Pendant l'entraînement, l'erreur de biais diminue (car notre modèle apprend à approximer les données), et l'erreur de variance augmente. Il est important d'arrêter l'entraînement - soit manuellement (lorsque nous détectons le surapprentissage) soit automatiquement (en introduisant une régularisation) - pour prévenir le surapprentissage.

## Conclusion

Dans cette leçon, vous avez appris les différences entre les différentes API pour les deux cadres d'IA les plus populaires, TensorFlow et PyTorch. De plus, vous avez appris un sujet très important, le surapprentissage.

## 🚀 Défi

Dans les notebooks qui accompagnent, vous trouverez des 'tâches' en bas ; parcourez les notebooks et complétez les tâches.

## Révision & Auto-Étude

Faites des recherches sur les sujets suivants :

- TensorFlow
- PyTorch
- Surapprentissage

Posez-vous les questions suivantes :

- Quelle est la différence entre TensorFlow et PyTorch ?
- Quelle est la différence entre surapprentissage et sous-ajustement ?

## Devoir

Dans ce laboratoire, il vous est demandé de résoudre deux problèmes de classification en utilisant des réseaux entièrement connectés à une ou plusieurs couches en utilisant PyTorch ou TensorFlow.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisés par intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations cruciales, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.