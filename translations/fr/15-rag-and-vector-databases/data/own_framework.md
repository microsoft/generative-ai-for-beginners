<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:14:48+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "fr"
}
-->
# Introduction aux réseaux de neurones. Perceptron multi-couches

Dans la section précédente, vous avez appris le modèle de réseau de neurones le plus simple - le perceptron à une couche, un modèle de classification linéaire à deux classes.

Dans cette section, nous allons étendre ce modèle à un cadre plus flexible, nous permettant de :

* effectuer une **classification multi-classes** en plus de la classification à deux classes
* résoudre des **problèmes de régression** en plus de la classification
* séparer des classes qui ne sont pas linéairement séparables

Nous développerons également notre propre cadre modulaire en Python qui nous permettra de construire différentes architectures de réseaux de neurones.

## Formalisation de l'apprentissage automatique

Commençons par formaliser le problème de l'apprentissage automatique. Supposons que nous ayons un jeu de données d'entraînement **X** avec des étiquettes **Y**, et que nous devions construire un modèle *f* qui fera les prédictions les plus précises. La qualité des prédictions est mesurée par la **fonction de perte** ℒ. Les fonctions de perte suivantes sont souvent utilisées :

* Pour un problème de régression, lorsque nous devons prédire un nombre, nous pouvons utiliser **l'erreur absolue** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ou **l'erreur quadratique** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pour la classification, nous utilisons la **perte 0-1** (qui est essentiellement la même que l'**exactitude** du modèle), ou la **perte logistique**.

Pour le perceptron à une couche, la fonction *f* était définie comme une fonction linéaire *f(x)=wx+b* (ici *w* est la matrice de poids, *x* est le vecteur des caractéristiques d'entrée, et *b* est le vecteur de biais). Pour différentes architectures de réseaux de neurones, cette fonction peut prendre une forme plus complexe.

> Dans le cas de la classification, il est souvent souhaitable d'obtenir les probabilités des classes correspondantes en sortie du réseau. Pour convertir des nombres arbitraires en probabilités (par exemple pour normaliser la sortie), nous utilisons souvent la fonction **softmax** σ, et la fonction *f* devient *f(x)=σ(wx+b)*

Dans la définition de *f* ci-dessus, *w* et *b* sont appelés **paramètres** θ=⟨*w,b*⟩. Étant donné le jeu de données ⟨**X**,**Y**⟩, nous pouvons calculer une erreur globale sur l'ensemble du jeu de données en fonction des paramètres θ.

> ✅ **L'objectif de l'entraînement d'un réseau de neurones est de minimiser l'erreur en faisant varier les paramètres θ**

## Optimisation par descente de gradient

Il existe une méthode bien connue d'optimisation de fonction appelée **descente de gradient**. L'idée est que nous pouvons calculer une dérivée (dans le cas multidimensionnel appelée **gradient**) de la fonction de perte par rapport aux paramètres, et faire varier les paramètres de manière à ce que l'erreur diminue. Cela peut être formalisé comme suit :

* Initialiser les paramètres avec des valeurs aléatoires w<sup>(0)</sup>, b<sup>(0)</sup>
* Répéter l'étape suivante plusieurs fois :
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Pendant l'entraînement, les étapes d'optimisation sont censées être calculées en considérant l'ensemble du jeu de données (rappelez-vous que la perte est calculée comme une somme à travers tous les échantillons d'entraînement). Cependant, dans la vie réelle, nous prenons de petites portions du jeu de données appelées **mini-lots**, et calculons les gradients sur la base d'un sous-ensemble de données. Parce que le sous-ensemble est pris au hasard chaque fois, cette méthode est appelée **descente de gradient stochastique** (SGD).

## Perceptrons multi-couches et rétropropagation

Un réseau à une couche, comme nous l'avons vu ci-dessus, est capable de classer des classes linéairement séparables. Pour construire un modèle plus riche, nous pouvons combiner plusieurs couches du réseau. Mathématiquement, cela signifierait que la fonction *f* aurait une forme plus complexe, et serait calculée en plusieurs étapes :
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Ici, α est une **fonction d'activation non linéaire**, σ est une fonction softmax, et les paramètres θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

L'algorithme de descente de gradient resterait le même, mais il serait plus difficile de calculer les gradients. Étant donné la règle de différenciation en chaîne, nous pouvons calculer les dérivées comme suit :

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ La règle de différenciation en chaîne est utilisée pour calculer les dérivées de la fonction de perte par rapport aux paramètres.

Notez que la partie la plus à gauche de toutes ces expressions est la même, et ainsi nous pouvons calculer efficacement les dérivées en partant de la fonction de perte et en allant "en arrière" à travers le graphe de calcul. Ainsi, la méthode d'entraînement d'un perceptron multi-couches est appelée **rétropropagation**, ou 'backprop'.

> TODO: citation d'image

> ✅ Nous aborderons la rétropropagation de manière beaucoup plus détaillée dans notre exemple de notebook.  

## Conclusion

Dans cette leçon, nous avons construit notre propre bibliothèque de réseaux de neurones, et nous l'avons utilisée pour une tâche de classification bidimensionnelle simple.

## 🚀 Défi

Dans le notebook accompagnant, vous allez implémenter votre propre cadre pour construire et entraîner des perceptrons multi-couches. Vous pourrez voir en détail comment fonctionnent les réseaux de neurones modernes.

Passez au notebook OwnFramework et travaillez dessus.

## Révision et auto-étude

La rétropropagation est un algorithme courant utilisé en IA et en ML, qui mérite d'être étudié plus en détail.

## Devoir

Dans ce laboratoire, vous êtes invité à utiliser le cadre que vous avez construit dans cette leçon pour résoudre la classification des chiffres manuscrits MNIST.

* Instructions
* Notebook

**Avertissement** :  
Ce document a été traduit en utilisant le service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.