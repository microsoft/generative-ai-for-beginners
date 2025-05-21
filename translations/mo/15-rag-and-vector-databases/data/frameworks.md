<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T01:51:29+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "mo"
}
-->
# Frameworks for Neural Networks

Como hemos aprendido, para entrenar redes neuronales de manera eficiente necesitamos hacer dos cosas:

* Operar sobre tensores, por ejemplo, multiplicar, sumar y calcular algunas funciones como sigmoid o softmax.
* Calcular los gradientes de todas las expresiones para realizar la optimización por descenso de gradiente.

Mientras que la biblioteca `numpy` puede hacer la primera parte, necesitamos algún mecanismo para calcular gradientes. En nuestro marco que hemos desarrollado en la sección anterior tuvimos que programar manualmente todas las funciones derivadas dentro del método `backward`, que realiza la retropropagación. Idealmente, un marco debería darnos la oportunidad de calcular gradientes de *cualquier expresión* que podamos definir.

Otra cosa importante es poder realizar cálculos en GPU, u otras unidades de cómputo especializadas, como TPU. El entrenamiento de redes neuronales profundas requiere *muchos* cálculos, y poder paralelizar esos cálculos en GPUs es muy importante.

> ✅ El término 'paralelizar' significa distribuir los cálculos en múltiples dispositivos.

Actualmente, los dos marcos neuronales más populares son: TensorFlow y PyTorch. Ambos proporcionan una API de bajo nivel para operar con tensores tanto en CPU como en GPU. Además de la API de bajo nivel, también hay una API de alto nivel, llamada Keras y PyTorch Lightning respectivamente.

API de Bajo Nivel | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
API de Alto Nivel| Keras| Pytorch

Las **APIs de bajo nivel** en ambos marcos te permiten construir los llamados **gráficos computacionales**. Este gráfico define cómo calcular la salida (usualmente la función de pérdida) con los parámetros de entrada dados, y puede ser enviado para cálculo en GPU, si está disponible. Hay funciones para diferenciar este gráfico computacional y calcular gradientes, que luego pueden ser usados para optimizar los parámetros del modelo.

Las **APIs de alto nivel** consideran las redes neuronales como una **secuencia de capas**, y hacen que la construcción de la mayoría de las redes neuronales sea mucho más fácil. Entrenar el modelo usualmente requiere preparar los datos y luego llamar a una función `fit` para hacer el trabajo.

La API de alto nivel te permite construir redes neuronales típicas muy rápidamente sin preocuparte por muchos detalles. Al mismo tiempo, la API de bajo nivel ofrece mucho más control sobre el proceso de entrenamiento, y por lo tanto se utilizan mucho en investigación, cuando se trata de nuevas arquitecturas de redes neuronales.

También es importante entender que puedes usar ambas APIs juntas, por ejemplo, puedes desarrollar tu propia arquitectura de capa de red usando la API de bajo nivel, y luego usarla dentro de la red más grande construida y entrenada con la API de alto nivel. O puedes definir una red usando la API de alto nivel como una secuencia de capas, y luego usar tu propio ciclo de entrenamiento de bajo nivel para realizar la optimización. Ambas APIs utilizan los mismos conceptos básicos subyacentes, y están diseñadas para funcionar bien juntas.

## Aprendizaje

En este curso, ofrecemos la mayoría del contenido tanto para PyTorch como para TensorFlow. Puedes elegir tu marco preferido y solo pasar por los cuadernos correspondientes. Si no estás seguro de qué marco elegir, lee algunas discusiones en internet sobre **PyTorch vs. TensorFlow**. También puedes echar un vistazo a ambos marcos para tener una mejor comprensión.

Donde sea posible, utilizaremos APIs de alto nivel por simplicidad. Sin embargo, creemos que es importante entender cómo funcionan las redes neuronales desde cero, por lo tanto, al principio comenzamos trabajando con la API de bajo nivel y tensores. Sin embargo, si deseas avanzar rápidamente y no quieres pasar mucho tiempo aprendiendo estos detalles, puedes omitirlos e ir directamente a los cuadernos de API de alto nivel.

## ✍️ Ejercicios: Frameworks

Continúa tu aprendizaje en los siguientes cuadernos:

API de Bajo Nivel | Cuaderno de TensorFlow+Keras | PyTorch
--------------|-------------------------------------|--------------------------------
API de Alto Nivel| Keras | *PyTorch Lightning*

Después de dominar los marcos, recapitulemos la noción de sobreajuste.

# Sobreajuste

El sobreajuste es un concepto extremadamente importante en el aprendizaje automático, ¡y es muy importante hacerlo bien!

Considera el siguiente problema de aproximar 5 puntos (representados por `x` en los gráficos a continuación):

!lineal | sobreajuste
-------------------------|--------------------------
**Modelo lineal, 2 parámetros** | **Modelo no lineal, 7 parámetros**
Error de entrenamiento = 5.3 | Error de entrenamiento = 0
Error de validación = 5.1 | Error de validación = 20

* A la izquierda, vemos una buena aproximación de línea recta. Debido a que el número de parámetros es adecuado, el modelo capta la idea detrás de la distribución de puntos correctamente.
* A la derecha, el modelo es demasiado poderoso. Debido a que solo tenemos 5 puntos y el modelo tiene 7 parámetros, puede ajustarse de tal manera que pase por todos los puntos, haciendo que el error de entrenamiento sea 0. Sin embargo, esto impide que el modelo entienda el patrón correcto detrás de los datos, por lo tanto, el error de validación es muy alto.

Es muy importante encontrar un equilibrio correcto entre la riqueza del modelo (número de parámetros) y el número de muestras de entrenamiento.

## Por qué ocurre el sobreajuste

  * No hay suficientes datos de entrenamiento
  * Modelo demasiado poderoso
  * Demasiado ruido en los datos de entrada

## Cómo detectar el sobreajuste

Como puedes ver en el gráfico anterior, el sobreajuste puede detectarse por un error de entrenamiento muy bajo y un error de validación alto. Normalmente durante el entrenamiento veremos que tanto los errores de entrenamiento como de validación comienzan a disminuir, y luego en algún punto el error de validación podría dejar de disminuir y comenzar a aumentar. Esto será una señal de sobreajuste, y el indicador de que probablemente deberíamos detener el entrenamiento en este punto (o al menos hacer una captura del modelo).

## Cómo prevenir el sobreajuste

Si puedes ver que ocurre el sobreajuste, puedes hacer una de las siguientes cosas:

 * Aumentar la cantidad de datos de entrenamiento
 * Disminuir la complejidad del modelo
 * Usar alguna técnica de regularización, como Dropout, que consideraremos más adelante.

## Sobreajuste y Compensación Sesgo-Varianza

El sobreajuste es en realidad un caso de un problema más genérico en estadística llamado Compensación Sesgo-Varianza. Si consideramos las posibles fuentes de error en nuestro modelo, podemos ver dos tipos de errores:

* **Errores de sesgo** son causados por nuestro algoritmo al no poder capturar correctamente la relación entre los datos de entrenamiento. Puede resultar del hecho de que nuestro modelo no es lo suficientemente poderoso (**subajuste**).
* **Errores de varianza**, que son causados por el modelo al aproximar el ruido en los datos de entrada en lugar de una relación significativa (**sobreajuste**).

Durante el entrenamiento, el error de sesgo disminuye (a medida que nuestro modelo aprende a aproximar los datos) y el error de varianza aumenta. Es importante detener el entrenamiento, ya sea manualmente (cuando detectamos sobreajuste) o automáticamente (introduciendo regularización), para prevenir el sobreajuste.

## Conclusión

En esta lección, aprendiste sobre las diferencias entre las diversas APIs para los dos marcos de IA más populares, TensorFlow y PyTorch. Además, aprendiste sobre un tema muy importante, el sobreajuste.

## 🚀 Desafío

En los cuadernos acompañantes, encontrarás 'tareas' al final; trabaja en los cuadernos y completa las tareas.

## Revisión y Autoestudio

Investiga sobre los siguientes temas:

- TensorFlow
- PyTorch
- Sobreajuste

Pregúntate las siguientes preguntas:

- ¿Cuál es la diferencia entre TensorFlow y PyTorch?
- ¿Cuál es la diferencia entre sobreajuste y subajuste?

## Asignación

En este laboratorio, se te pide resolver dos problemas de clasificación utilizando redes completamente conectadas de una y varias capas usando PyTorch o TensorFlow.

I'm sorry, but it seems there might be a misunderstanding. Could you please clarify what language you mean by "mo"? If you meant a specific language, such as Montenegrin, Mongolian, or another, please specify so I can assist you accurately.