# Introduction aux réseaux neuronaux : Perceptron

L'une des premières tentatives pour implémenter quelque chose de similaire à un réseau neuronal moderne a été réalisée par Frank Rosenblatt du Cornell Aeronautical Laboratory en 1957. Il s'agissait d'une implémentation matérielle appelée "Mark-1", conçue pour reconnaître des figures géométriques primitives, telles que des triangles, des carrés et des cercles.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='Le Perceptron Mark 1' />|

> Images de Wikipedia

Une image d'entrée était représentée par un réseau de 20x20 photorécepteurs, de sorte que le réseau neuronal avait 400 entrées et une sortie binaire. Un réseau simple contenait un neurone, également appelé une **unité logique seuil**. Les poids du réseau neuronal agissaient comme des potentiomètres nécessitant un ajustement manuel pendant la phase d'apprentissage.

> ✅ Un potentiomètre est un dispositif qui permet à l'utilisateur de régler la résistance d'un circuit.

> Le New York Times a écrit à propos du perceptron à cette époque : *l'embryon d'un ordinateur électronique que [la Marine] espère capable de marcher, parler, voir, écrire, se reproduire et être conscient de son existence.*

## Modèle de Perceptron

Supposons que nous ayons N caractéristiques dans notre modèle, auquel cas le vecteur d'entrée serait un vecteur de taille N. Un perceptron est un modèle de **classification binaire**, c'est-à-dire qu'il peut distinguer entre deux classes de données d'entrée. Nous supposerons que pour chaque vecteur d'entrée x, la sortie de notre perceptron serait soit +1, soit -1, selon la classe. La sortie sera calculée en utilisant la formule :

y(x) = f(w<sup>T</sup>x)

où f est une fonction d'activation de seuil

## Entraînement du Perceptron

Pour entraîner un perceptron, nous devons trouver un vecteur de poids w qui classe correctement la plupart des valeurs, c'est-à-dire qui aboutit à l'erreur la plus faible. Cette erreur est définie par le **critère de perceptron** de la manière suivante :

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

où :

* la somme est effectuée sur les points de données d'entraînement i qui aboutissent à une mauvaise classification
* x<sub>i</sub> est la donnée d'entrée, et t<sub>i</sub> est soit -1 soit +1 pour les exemples négatifs et positifs respectivement.

Ce critère est considéré comme une fonction des poids w, et nous devons le minimiser. Souvent, une méthode appelée **descente de gradient** est utilisée, dans laquelle nous commençons avec des poids initiaux w<sup>(0)</sup>, puis à chaque étape, nous mettons à jour les poids selon la formule :

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

## Révision & Auto-apprentissage

Pour voir comment nous pouvons utiliser le perceptron pour résoudre un problème simple ainsi que des problèmes réels, et pour continuer à apprendre - rendez-vous sur le notebook Perceptron.

Voici également un article intéressant sur les perceptrons.

## Devoir

Dans cette leçon, nous avons implémenté un perceptron pour une tâche de classification binaire, et nous l'avons utilisé pour classer entre deux chiffres manuscrits. Dans ce laboratoire, il vous est demandé de résoudre entièrement le problème de classification des chiffres, c'est-à-dire de déterminer quel chiffre est le plus susceptible de correspondre à une image donnée.

* Instructions
* Notebook

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée par IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.