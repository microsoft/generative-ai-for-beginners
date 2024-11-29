# Introducción a Redes Neuronales. Perceptrón Multicapa

En la sección anterior, aprendiste sobre el modelo de red neuronal más simple: el perceptrón de una sola capa, un modelo lineal de clasificación de dos clases.

En esta sección extenderemos este modelo a un marco más flexible, permitiéndonos:

* realizar **clasificación multiclase** además de la clasificación de dos clases
* resolver **problemas de regresión** además de clasificación
* separar clases que no son linealmente separables

También desarrollaremos nuestro propio marco modular en Python que nos permitirá construir diferentes arquitecturas de redes neuronales.

## Formalización del Aprendizaje Automático

Comencemos formalizando el problema del Aprendizaje Automático. Supongamos que tenemos un conjunto de datos de entrenamiento **X** con etiquetas **Y**, y necesitamos construir un modelo *f* que haga las predicciones más precisas. La calidad de las predicciones se mide mediante la **función de pérdida** ℒ. Las siguientes funciones de pérdida se utilizan a menudo:

* Para problemas de regresión, cuando necesitamos predecir un número, podemos usar **error absoluto** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, o **error cuadrático** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para clasificación, usamos **pérdida 0-1** (que es esencialmente lo mismo que la **precisión** del modelo), o **pérdida logística**.

Para un perceptrón de un nivel, la función *f* se definía como una función lineal *f(x)=wx+b* (aquí *w* es la matriz de pesos, *x* es el vector de características de entrada, y *b* es el vector de sesgo). Para diferentes arquitecturas de redes neuronales, esta función puede tomar una forma más compleja.

> En el caso de la clasificación, a menudo es deseable obtener probabilidades de las clases correspondientes como salida de la red. Para convertir números arbitrarios en probabilidades (por ejemplo, para normalizar la salida), a menudo usamos la función **softmax** σ, y la función *f* se convierte en *f(x)=σ(wx+b)*

En la definición de *f* anterior, *w* y *b* se llaman **parámetros** θ=⟨*w,b*⟩. Dado el conjunto de datos ⟨**X**,**Y**⟩, podemos calcular un error general en todo el conjunto de datos como una función de los parámetros θ.

> ✅ **El objetivo del entrenamiento de redes neuronales es minimizar el error variando los parámetros θ**

## Optimización por Descenso de Gradiente

Hay un método conocido de optimización de funciones llamado **descenso de gradiente**. La idea es que podemos calcular una derivada (en el caso multidimensional llamada **gradiente**) de la función de pérdida con respecto a los parámetros, y variar los parámetros de tal manera que el error disminuya. Esto se puede formalizar de la siguiente manera:

* Inicializar los parámetros con algunos valores aleatorios w<sup>(0)</sup>, b<sup>(0)</sup>
* Repetir el siguiente paso muchas veces:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Durante el entrenamiento, se supone que los pasos de optimización se calculan considerando todo el conjunto de datos (recuerda que la pérdida se calcula como una suma a través de todas las muestras de entrenamiento). Sin embargo, en la vida real tomamos pequeñas porciones del conjunto de datos llamadas **minibatches**, y calculamos gradientes basados en un subconjunto de datos. Debido a que el subconjunto se toma aleatoriamente cada vez, este método se llama **descenso de gradiente estocástico** (SGD).

## Perceptrones Multicapa y Retropropagación

Una red de una sola capa, como hemos visto anteriormente, es capaz de clasificar clases linealmente separables. Para construir un modelo más rico, podemos combinar varias capas de la red. Matemáticamente, esto significaría que la función *f* tendría una forma más compleja y se calcularía en varios pasos:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Aquí, α es una **función de activación no lineal**, σ es una función softmax, y los parámetros θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

El algoritmo de descenso de gradiente seguiría siendo el mismo, pero sería más difícil calcular los gradientes. Dado el principio de diferenciación en cadena, podemos calcular las derivadas como:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ La regla de diferenciación en cadena se utiliza para calcular las derivadas de la función de pérdida con respecto a los parámetros.

Observa que la parte más a la izquierda de todas estas expresiones es la misma, por lo que podemos calcular de manera efectiva las derivadas comenzando desde la función de pérdida y yendo "hacia atrás" a través del grafo computacional. Por lo tanto, el método de entrenamiento de un perceptrón multicapa se llama **retropropagación**, o 'backprop'.

> TODO: cita de la imagen

> ✅ Cubriremos la retropropagación con mucho más detalle en nuestro ejemplo de notebook.

## Conclusión

En esta lección, hemos construido nuestra propia biblioteca de redes neuronales y la hemos utilizado para una tarea simple de clasificación bidimensional.

## 🚀 Desafío

En el notebook adjunto, implementarás tu propio marco para construir y entrenar perceptrones multicapa. Podrás ver en detalle cómo operan las redes neuronales modernas.

Procede al notebook OwnFramework y trabaja en él.

## Revisión y Autoestudio

La retropropagación es un algoritmo común utilizado en IA y ML, vale la pena estudiarlo con más detalle.

## Asignación

En este laboratorio, se te pide que utilices el marco que construiste en esta lección para resolver la clasificación de dígitos escritos a mano MNIST.

* Instrucciones
* Notebook

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.