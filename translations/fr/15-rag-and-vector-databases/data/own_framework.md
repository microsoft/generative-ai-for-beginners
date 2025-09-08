<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:39:56+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "fr"
}
-->
# Introduction aux réseaux de neurones. Perceptron multicouche

Dans la section précédente, vous avez découvert le modèle de réseau de neurones le plus simple : le perceptron à une couche, un modèle linéaire de classification binaire.

Dans cette section, nous allons étendre ce modèle vers un cadre plus flexible, nous permettant de :

* réaliser une **classification multi-classes** en plus de la classification binaire
* résoudre des **problèmes de régression** en plus de la classification
* séparer des classes qui ne sont pas linéairement séparables

Nous allons également développer notre propre framework modulaire en Python, qui nous permettra de construire différentes architectures de réseaux de neurones.

## Formalisation de l’apprentissage automatique

Commençons par formaliser le problème d’apprentissage automatique. Supposons que nous disposons d’un jeu de données d’entraînement **X** avec des étiquettes **Y**, et que nous devons construire un modèle *f* qui fera les prédictions les plus précises possibles. La qualité des prédictions est mesurée par une **fonction de perte** ℒ. Les fonctions de perte suivantes sont souvent utilisées :

* Pour un problème de régression, lorsque l’on doit prédire un nombre, on peut utiliser l’**erreur absolue** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ou l’**erreur quadratique** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pour la classification, on utilise la **perte 0-1** (qui correspond essentiellement à la **précision** du modèle), ou la **perte logistique**.

Pour le perceptron à une couche, la fonction *f* était définie comme une fonction linéaire *f(x)=wx+b* (ici *w* est la matrice de poids, *x* le vecteur des caractéristiques d’entrée, et *b* le vecteur de biais). Pour différentes architectures de réseaux de neurones, cette fonction peut prendre une forme plus complexe.

> Dans le cas de la classification, il est souvent souhaitable d’obtenir des probabilités des classes correspondantes en sortie du réseau. Pour convertir des nombres arbitraires en probabilités (par exemple pour normaliser la sortie), on utilise souvent la fonction **softmax** σ, et la fonction *f* devient *f(x)=σ(wx+b)*

Dans la définition de *f* ci-dessus, *w* et *b* sont appelés **paramètres** θ=⟨*w,b*⟩. Étant donné le jeu de données ⟨**X**,**Y**⟩, on peut calculer une erreur globale sur l’ensemble du jeu de données en fonction des paramètres θ.

> ✅ **L’objectif de l’entraînement du réseau de neurones est de minimiser l’erreur en faisant varier les paramètres θ**

## Optimisation par descente de gradient

Il existe une méthode bien connue d’optimisation de fonction appelée **descente de gradient**. L’idée est que l’on peut calculer une dérivée (dans le cas multidimensionnel appelée **gradient**) de la fonction de perte par rapport aux paramètres, et faire varier ces paramètres de manière à réduire l’erreur. Cela peut se formaliser ainsi :

* Initialiser les paramètres avec des valeurs aléatoires w<sup>(0)</sup>, b<sup>(0)</sup>
* Répéter l’étape suivante plusieurs fois :
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Pendant l’entraînement, les étapes d’optimisation sont censées être calculées en considérant l’ensemble du jeu de données (rappelez-vous que la perte est calculée comme une somme sur tous les échantillons d’entraînement). Cependant, dans la pratique, on prend de petites portions du jeu de données appelées **minibatchs**, et on calcule les gradients sur un sous-ensemble des données. Comme ce sous-ensemble est choisi aléatoirement à chaque fois, cette méthode s’appelle **descente de gradient stochastique** (SGD).

## Perceptrons multicouches et rétropropagation

Un réseau à une couche, comme nous l’avons vu, est capable de classer des classes linéairement séparables. Pour construire un modèle plus riche, on peut combiner plusieurs couches du réseau. Mathématiquement, cela signifie que la fonction *f* aura une forme plus complexe, et sera calculée en plusieurs étapes :
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Ici, α est une **fonction d’activation non linéaire**, σ est une fonction softmax, et les paramètres θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

L’algorithme de descente de gradient reste le même, mais il devient plus difficile de calculer les gradients. En appliquant la règle de dérivation en chaîne, on peut calculer les dérivées comme suit :

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ La règle de dérivation en chaîne est utilisée pour calculer les dérivées de la fonction de perte par rapport aux paramètres.

Notez que la partie la plus à gauche de toutes ces expressions est la même, ce qui nous permet de calculer efficacement les dérivées en partant de la fonction de perte et en remontant « à rebours » dans le graphe de calcul. C’est pourquoi la méthode d’entraînement d’un perceptron multicouche s’appelle **rétropropagation**, ou 'backprop'.

> TODO: image citation

> ✅ Nous aborderons la rétropropagation en beaucoup plus de détails dans notre exemple de notebook.

## Conclusion

Dans cette leçon, nous avons construit notre propre bibliothèque de réseaux de neurones, et nous l’avons utilisée pour une tâche simple de classification bidimensionnelle.

## 🚀 Défi

Dans le notebook associé, vous allez implémenter votre propre framework pour construire et entraîner des perceptrons multicouches. Vous pourrez ainsi voir en détail comment fonctionnent les réseaux de neurones modernes.

Passez au notebook OwnFramework et suivez-le pas à pas.

## Révision & Auto-apprentissage

La rétropropagation est un algorithme courant en IA et en apprentissage automatique, qui mérite d’être étudié plus en profondeur.

## Exercice

Dans ce laboratoire, vous êtes invité à utiliser le framework que vous avez construit dans cette leçon pour résoudre la classification des chiffres manuscrits MNIST.

* Instructions
* Notebook

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.