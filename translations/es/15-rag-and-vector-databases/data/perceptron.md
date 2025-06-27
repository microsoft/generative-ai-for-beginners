<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:33:57+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "es"
}
-->
# Introducción a las Redes Neuronales: Perceptrón

Uno de los primeros intentos de implementar algo similar a una red neuronal moderna fue realizado por Frank Rosenblatt del Laboratorio Aeronáutico de Cornell en 1957. Fue una implementación de hardware llamada "Mark-1", diseñada para reconocer figuras geométricas primitivas, como triángulos, cuadrados y círculos.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='El Perceptrón Mark 1' />|

> Imágenes de Wikipedia

Una imagen de entrada se representaba mediante una matriz de fotoceldas de 20x20, por lo que la red neuronal tenía 400 entradas y una salida binaria. Una red simple contenía una neurona, también llamada **unidad lógica de umbral**. Los pesos de la red neuronal actuaban como potenciómetros que requerían ajuste manual durante la fase de entrenamiento.

> ✅ Un potenciómetro es un dispositivo que permite al usuario ajustar la resistencia de un circuito.

> The New York Times escribió sobre el perceptrón en ese momento: *el embrión de una computadora electrónica que [la Marina] espera que pueda caminar, hablar, ver, escribir, reproducirse y ser consciente de su existencia.*

## Modelo de Perceptrón

Supongamos que tenemos N características en nuestro modelo, en cuyo caso el vector de entrada sería un vector de tamaño N. Un perceptrón es un modelo de **clasificación binaria**, es decir, puede distinguir entre dos clases de datos de entrada. Asumiremos que para cada vector de entrada x, la salida de nuestro perceptrón será +1 o -1, dependiendo de la clase. La salida se calculará usando la fórmula:

y(x) = f(w<sup>T</sup>x)

donde f es una función de activación de paso

## Entrenamiento del Perceptrón

Para entrenar un perceptrón necesitamos encontrar un vector de pesos w que clasifique la mayoría de los valores correctamente, es decir, que resulte en el menor **error**. Este error se define por el **criterio del perceptrón** de la siguiente manera:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

donde:

* la suma se toma sobre aquellos puntos de datos de entrenamiento i que resultan en una clasificación incorrecta
* x<sub>i</sub> es el dato de entrada, y t<sub>i</sub> es -1 o +1 para ejemplos negativos y positivos respectivamente.

Este criterio se considera como una función de los pesos w, y necesitamos minimizarlo. A menudo, se utiliza un método llamado **descenso de gradiente**, en el cual comenzamos con algunos pesos iniciales w<sup>(0)</sup>, y luego en cada paso actualizamos los pesos según la fórmula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Aquí η es la llamada **tasa de aprendizaje**, y ∇E(w) denota el **gradiente** de E. Después de calcular el gradiente, terminamos con

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

El algoritmo en Python se ve así:

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

## Conclusión

En esta lección, aprendiste sobre un perceptrón, que es un modelo de clasificación binaria, y cómo entrenarlo usando un vector de pesos.

## 🚀 Desafío

Si deseas intentar construir tu propio perceptrón, prueba este laboratorio en Microsoft Learn que utiliza el diseñador de Azure ML

## Revisión y Autoestudio

Para ver cómo podemos usar el perceptrón para resolver un problema sencillo así como problemas de la vida real, y para continuar aprendiendo - ve al cuaderno de Perceptrón.

Aquí hay un artículo interesante sobre los perceptrones también.

## Tarea

En esta lección, hemos implementado un perceptrón para la tarea de clasificación binaria, y lo hemos usado para clasificar entre dos dígitos escritos a mano. En este laboratorio, se te pide resolver el problema de clasificación de dígitos completamente, es decir, determinar qué dígito es más probable que corresponda a una imagen dada.

* Instrucciones
* Cuaderno

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.