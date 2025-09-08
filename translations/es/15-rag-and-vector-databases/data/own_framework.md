<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:40:12+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "es"
}
-->
# Introducción a las Redes Neuronales. Perceptrón Multicapa

En la sección anterior, aprendiste sobre el modelo de red neuronal más simple: el perceptrón de una sola capa, un modelo lineal para clasificación binaria.

En esta sección ampliaremos este modelo hacia un marco más flexible, que nos permitirá:

* realizar **clasificación multiclase** además de clasificación binaria
* resolver **problemas de regresión** además de clasificación
* separar clases que no son linealmente separables

También desarrollaremos nuestro propio marco modular en Python que nos permitirá construir diferentes arquitecturas de redes neuronales.

## Formalización del Aprendizaje Automático

Comencemos formalizando el problema de Aprendizaje Automático. Supongamos que tenemos un conjunto de datos de entrenamiento **X** con etiquetas **Y**, y necesitamos construir un modelo *f* que haga predicciones lo más precisas posible. La calidad de las predicciones se mide mediante la **función de pérdida** ℒ. Las siguientes funciones de pérdida se usan con frecuencia:

* Para problemas de regresión, cuando necesitamos predecir un número, podemos usar el **error absoluto** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, o el **error cuadrático** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para clasificación, usamos la **pérdida 0-1** (que es esencialmente lo mismo que la **precisión** del modelo), o la **pérdida logística**.

Para el perceptrón de un solo nivel, la función *f* se definió como una función lineal *f(x)=wx+b* (aquí *w* es la matriz de pesos, *x* es el vector de características de entrada, y *b* es el vector de sesgo). Para diferentes arquitecturas de redes neuronales, esta función puede tomar una forma más compleja.

> En el caso de clasificación, a menudo es deseable obtener probabilidades de las clases correspondientes como salida de la red. Para convertir números arbitrarios en probabilidades (por ejemplo, para normalizar la salida), a menudo usamos la función **softmax** σ, y la función *f* se convierte en *f(x)=σ(wx+b)*

En la definición de *f* anterior, *w* y *b* se llaman **parámetros** θ=⟨*w,b*⟩. Dado el conjunto de datos ⟨**X**,**Y**⟩, podemos calcular un error total en todo el conjunto como función de los parámetros θ.

> ✅ **El objetivo del entrenamiento de la red neuronal es minimizar el error variando los parámetros θ**

## Optimización por Descenso de Gradiente

Existe un método conocido para la optimización de funciones llamado **descenso de gradiente**. La idea es que podemos calcular la derivada (en el caso multidimensional llamada **gradiente**) de la función de pérdida con respecto a los parámetros, y variar los parámetros de manera que el error disminuya. Esto se puede formalizar de la siguiente manera:

* Inicializar los parámetros con algunos valores aleatorios w<sup>(0)</sup>, b<sup>(0)</sup>
* Repetir el siguiente paso muchas veces:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Durante el entrenamiento, los pasos de optimización se calculan considerando todo el conjunto de datos (recuerda que la pérdida se calcula como suma sobre todas las muestras de entrenamiento). Sin embargo, en la práctica tomamos pequeñas porciones del conjunto llamadas **minibatches**, y calculamos los gradientes basándonos en un subconjunto de datos. Debido a que el subconjunto se toma aleatoriamente cada vez, este método se llama **descenso de gradiente estocástico** (SGD).

## Perceptrones Multicapa y Retropropagación

La red de una sola capa, como vimos antes, es capaz de clasificar clases linealmente separables. Para construir un modelo más rico, podemos combinar varias capas de la red. Matemáticamente esto significa que la función *f* tendrá una forma más compleja, y se calculará en varios pasos:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Aquí, α es una **función de activación no lineal**, σ es la función softmax, y los parámetros θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

El algoritmo de descenso de gradiente se mantiene igual, pero calcular los gradientes es más complicado. Dada la regla de la cadena para diferenciación, podemos calcular las derivadas como:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ La regla de la cadena se usa para calcular las derivadas de la función de pérdida con respecto a los parámetros.

Observa que la parte más a la izquierda de todas estas expresiones es la misma, por lo que podemos calcular las derivadas de manera eficiente comenzando desde la función de pérdida y yendo "hacia atrás" a través del grafo computacional. Por eso, el método para entrenar un perceptrón multicapa se llama **retropropagación**, o 'backprop'.

> TODO: cita de imagen

> ✅ Cubriremos la retropropagación con mucho más detalle en nuestro ejemplo del cuaderno.

## Conclusión

En esta lección, hemos construido nuestra propia biblioteca de redes neuronales y la hemos usado para una tarea simple de clasificación en dos dimensiones.

## 🚀 Desafío

En el cuaderno adjunto, implementarás tu propio marco para construir y entrenar perceptrones multicapa. Podrás ver en detalle cómo funcionan las redes neuronales modernas.

Continúa con el cuaderno OwnFramework y trabaja en él.

## Repaso y Autoestudio

La retropropagación es un algoritmo común en IA y ML, vale la pena estudiarlo con más detalle.

## Tarea

En este laboratorio, se te pide usar el marco que construiste en esta lección para resolver la clasificación de dígitos manuscritos MNIST.

* Instrucciones
* Cuaderno

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.