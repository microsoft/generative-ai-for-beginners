<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:24:30+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "fr"
}
-->
# Frameworks de réseaux de neurones

Comme nous l'avons déjà vu, pour pouvoir entraîner efficacement des réseaux de neurones, il faut faire deux choses :

* Opérer sur des tenseurs, par exemple multiplier, additionner, et calculer certaines fonctions comme sigmoid ou softmax
* Calculer les gradients de toutes les expressions, afin de réaliser une optimisation par descente de gradient

Alors que la bibliothèque `numpy` peut gérer la première partie, nous avons besoin d’un mécanisme pour calculer les gradients. Dans notre framework développé dans la section précédente, nous devions programmer manuellement toutes les fonctions dérivées dans la méthode `backward`, qui réalise la rétropropagation. Idéalement, un framework devrait nous permettre de calculer les gradients de *n’importe quelle expression* que nous pouvons définir.

Un autre point important est de pouvoir effectuer les calculs sur GPU, ou toute autre unité de calcul spécialisée, comme TPU. L’entraînement des réseaux de neurones profonds nécessite *beaucoup* de calculs, et pouvoir paralléliser ces calculs sur des GPU est très important.

> ✅ Le terme « paralléliser » signifie répartir les calculs sur plusieurs dispositifs.

Actuellement, les deux frameworks de réseaux de neurones les plus populaires sont : TensorFlow et PyTorch. Les deux fournissent une API bas niveau pour manipuler les tenseurs à la fois sur CPU et GPU. Au-dessus de cette API bas niveau, il existe aussi une API plus haut niveau, appelée respectivement Keras et PyTorch Lightning.

API bas niveau | TensorFlow | PyTorch  
--------------|------------|---------  
API haut niveau | Keras | PyTorch Lightning

Les **API bas niveau** dans les deux frameworks permettent de construire ce qu’on appelle des **graphes de calcul**. Ce graphe définit comment calculer la sortie (généralement la fonction de perte) à partir des paramètres d’entrée, et peut être envoyé pour calcul sur GPU, si disponible. Il existe des fonctions pour différencier ce graphe de calcul et calculer les gradients, qui peuvent ensuite être utilisés pour optimiser les paramètres du modèle.

Les **API haut niveau** considèrent essentiellement les réseaux de neurones comme une **séquence de couches**, et facilitent grandement la construction de la plupart des réseaux. L’entraînement du modèle nécessite généralement de préparer les données puis d’appeler une fonction `fit` pour lancer le processus.

L’API haut niveau permet de construire rapidement des réseaux typiques sans se soucier de nombreux détails. En même temps, l’API bas niveau offre beaucoup plus de contrôle sur le processus d’entraînement, et est donc très utilisée en recherche, lorsque l’on travaille sur de nouvelles architectures de réseaux.

Il est aussi important de comprendre que vous pouvez utiliser les deux API ensemble, par exemple en développant votre propre architecture de couche réseau avec l’API bas niveau, puis en l’intégrant dans un réseau plus large construit et entraîné avec l’API haut niveau. Ou bien vous pouvez définir un réseau avec l’API haut niveau comme une séquence de couches, puis utiliser votre propre boucle d’entraînement bas niveau pour optimiser. Les deux API partagent les mêmes concepts fondamentaux et sont conçues pour bien fonctionner ensemble.

## Apprentissage

Dans ce cours, nous proposons la plupart du contenu à la fois pour PyTorch et TensorFlow. Vous pouvez choisir votre framework préféré et ne suivre que les notebooks correspondants. Si vous ne savez pas quel framework choisir, lisez quelques discussions sur internet à propos de **PyTorch vs. TensorFlow**. Vous pouvez aussi explorer les deux frameworks pour mieux comprendre.

Dans la mesure du possible, nous utiliserons les API haut niveau pour plus de simplicité. Cependant, nous pensons qu’il est important de comprendre le fonctionnement des réseaux de neurones depuis les bases, donc au début nous commençons par travailler avec l’API bas niveau et les tenseurs. Toutefois, si vous souhaitez avancer rapidement sans passer trop de temps sur ces détails, vous pouvez les sauter et aller directement aux notebooks avec l’API haut niveau.

## ✍️ Exercices : Frameworks

Poursuivez votre apprentissage dans les notebooks suivants :

API bas niveau | Notebook TensorFlow+Keras | PyTorch  
--------------|----------------------------|---------  
API haut niveau | Keras | *PyTorch Lightning*

Après avoir maîtrisé les frameworks, récapitulons la notion de surapprentissage.

# Surapprentissage

Le surapprentissage est un concept extrêmement important en apprentissage automatique, et il est crucial de bien le comprendre !

Considérons le problème suivant d’approximation de 5 points (représentés par des `x` sur les graphiques ci-dessous) :

!linear | overfit  
-------------------------|--------------------------  
**Modèle linéaire, 2 paramètres** | **Modèle non-linéaire, 7 paramètres**  
Erreur d’entraînement = 5.3 | Erreur d’entraînement = 0  
Erreur de validation = 5.1 | Erreur de validation = 20

* À gauche, on voit une bonne approximation par une droite. Comme le nombre de paramètres est adéquat, le modèle saisit correctement la distribution des points.
* À droite, le modèle est trop puissant. Comme nous n’avons que 5 points et que le modèle a 7 paramètres, il peut s’ajuster pour passer par tous les points, ce qui fait que l’erreur d’entraînement est nulle. Cependant, cela empêche le modèle de comprendre le vrai motif derrière les données, d’où une erreur de validation très élevée.

Il est très important de trouver un bon équilibre entre la richesse du modèle (nombre de paramètres) et le nombre d’échantillons d’entraînement.

## Pourquoi le surapprentissage se produit

  * Pas assez de données d’entraînement  
  * Modèle trop puissant  
  * Trop de bruit dans les données d’entrée

## Comment détecter le surapprentissage

Comme on peut le voir sur le graphique ci-dessus, le surapprentissage se détecte par une erreur d’entraînement très faible, et une erreur de validation élevée. Normalement, pendant l’entraînement, on observe que les erreurs d’entraînement et de validation diminuent toutes les deux, puis à un certain moment l’erreur de validation peut cesser de diminuer et commencer à augmenter. C’est un signe de surapprentissage, et un indicateur qu’il faudrait probablement arrêter l’entraînement à ce moment-là (ou au moins sauvegarder un instantané du modèle).

surapprentissage

## Comment prévenir le surapprentissage

Si vous constatez qu’un surapprentissage se produit, vous pouvez faire l’une des choses suivantes :

 * Augmenter la quantité de données d’entraînement  
 * Réduire la complexité du modèle  
 * Utiliser une technique de régularisation, comme le Dropout, que nous verrons plus tard.

## Surapprentissage et compromis biais-variance

Le surapprentissage est en fait un cas particulier d’un problème plus général en statistiques appelé compromis biais-variance. Si l’on considère les sources possibles d’erreur dans notre modèle, on peut distinguer deux types d’erreurs :

* Les **erreurs de biais** sont causées par notre algorithme qui n’arrive pas à capturer correctement la relation dans les données d’entraînement. Cela peut venir du fait que notre modèle n’est pas assez puissant (**sous-apprentissage**).
* Les **erreurs de variance**, qui sont causées par le modèle qui approxime le bruit dans les données d’entrée au lieu de la relation significative (**surapprentissage**).

Pendant l’entraînement, l’erreur de biais diminue (car notre modèle apprend à approximer les données), tandis que l’erreur de variance augmente. Il est important d’arrêter l’entraînement – soit manuellement (lorsqu’on détecte un surapprentissage), soit automatiquement (en introduisant une régularisation) – pour éviter le surapprentissage.

## Conclusion

Dans cette leçon, vous avez appris les différences entre les différentes API des deux frameworks d’IA les plus populaires, TensorFlow et PyTorch. Vous avez également découvert un sujet très important : le surapprentissage.

## 🚀 Défi

Dans les notebooks associés, vous trouverez des « tâches » en bas de page ; travaillez-les et complétez les exercices.

## Révision & Auto-apprentissage

Faites des recherches sur les sujets suivants :

- TensorFlow  
- PyTorch  
- Surapprentissage

Posez-vous les questions suivantes :

- Quelle est la différence entre TensorFlow et PyTorch ?  
- Quelle est la différence entre surapprentissage et sous-apprentissage ?

## Travail à faire

Dans ce laboratoire, vous êtes invité à résoudre deux problèmes de classification en utilisant des réseaux entièrement connectés à une ou plusieurs couches, avec PyTorch ou TensorFlow.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.