<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:29:06+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "fr"
}
-->
# Introduction aux réseaux neuronaux : Perceptron

L'une des premières tentatives pour implémenter quelque chose de similaire à un réseau neuronal moderne a été réalisée par Frank Rosenblatt du Cornell Aeronautical Laboratory en 1957. Il s'agissait d'une implémentation matérielle appelée "Mark-1", conçue pour reconnaître des figures géométriques primitives, telles que des triangles, des carrés et des cercles.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='Le Perceptron Mark 1' />|

> Images de Wikipedia

Une image d'entrée était représentée par une matrice de 20x20 photorécepteurs, de sorte que le réseau neuronal avait 400 entrées et une sortie binaire. Un réseau simple contenait un neurone, également appelé une **unité logique seuil**. Les poids du réseau neuronal fonctionnaient comme des potentiomètres nécessitant un ajustement manuel pendant la phase d'entraînement.

> ✅ Un potentiomètre est un dispositif qui permet à l'utilisateur d'ajuster la résistance d'un circuit.

> Le New York Times écrivait à propos du perceptron à l'époque : *l'embryon d'un ordinateur électronique que [la Marine] espère capable de marcher, parler, voir, écrire, se reproduire et être conscient de son existence.*

## Modèle de Perceptron

Supposons que nous ayons N caractéristiques dans notre modèle, auquel cas le vecteur d'entrée serait un vecteur de taille N. Un perceptron est un modèle de **classification binaire**, c'est-à-dire qu'il peut distinguer entre deux classes de données d'entrée. Nous supposerons que pour chaque vecteur d'entrée x, la sortie de notre perceptron serait soit +1 soit -1, selon la classe. La sortie sera calculée à l'aide de la formule :

y(x) = f(w<sup>T</sup>x)

où f est une fonction d'activation en escalier

## Entraînement du Perceptron

Pour entraîner un perceptron, nous devons trouver un vecteur de poids w qui classe la plupart des valeurs correctement, c'est-à-dire qui résulte en la plus petite **erreur**. Cette erreur est définie par le **critère du perceptron** de la manière suivante :

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

où :

* la somme est prise sur ces points de données d'entraînement i qui entraînent une mauvaise classification
* x<sub>i</sub> est la donnée d'entrée, et t<sub>i</sub> est soit -1 soit +1 pour les exemples négatifs et positifs respectivement.

Ce critère est considéré comme une fonction des poids w, et nous devons le minimiser. Souvent, une méthode appelée **descente de gradient** est utilisée, dans laquelle nous commençons avec certains poids initiaux w<sup>(0)</sup>, puis à chaque étape, nous mettons à jour les poids selon la formule :

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Ici, η est ce qu'on appelle le **taux d'apprentissage**, et ∇E(w) désigne le **gradient** de E. Après avoir calculé le gradient, nous obtenons

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

L'algorithme en Python ressemble à ceci :

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Conclusion

Dans cette leçon, vous avez appris ce qu'est un perceptron, qui est un modèle de classification binaire, et comment l'entraîner en utilisant un vecteur de poids.

## 🚀 Défi

Si vous souhaitez essayer de construire votre propre perceptron, essayez ce laboratoire sur Microsoft Learn qui utilise le concepteur Azure ML.

## Révision & Auto-étude

Pour voir comment nous pouvons utiliser le perceptron pour résoudre un problème simple ainsi que des problèmes réels, et pour continuer à apprendre - allez au cahier Perceptron.

Voici également un article intéressant sur les perceptrons.

## Devoir

Dans cette leçon, nous avons implémenté un perceptron pour une tâche de classification binaire, et nous l'avons utilisé pour classer entre deux chiffres manuscrits. Dans ce laboratoire, il vous est demandé de résoudre entièrement le problème de classification des chiffres, c'est-à-dire de déterminer quel chiffre correspond le plus probablement à une image donnée.

* Instructions
* Cahier

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.