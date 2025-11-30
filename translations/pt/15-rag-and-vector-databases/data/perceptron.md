<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:56:53+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "pt"
}
-->
# Introdução às Redes Neurais: Perceptron

Uma das primeiras tentativas de implementar algo semelhante a uma rede neural moderna foi feita por Frank Rosenblatt, do Cornell Aeronautical Laboratory, em 1957. Foi uma implementação em hardware chamada "Mark-1", projetada para reconhecer figuras geométricas primitivas, como triângulos, quadrados e círculos.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Imagens da Wikipedia

Uma imagem de entrada era representada por uma matriz de 20x20 fotocélulas, pelo que a rede neural tinha 400 entradas e uma saída binária. Uma rede simples continha um neurónio, também chamado de **unidade lógica de limiar**. Os pesos da rede neural funcionavam como potenciômetros que exigiam ajuste manual durante a fase de treino.

> ✅ Um potenciômetro é um dispositivo que permite ao utilizador ajustar a resistência de um circuito.

> O New York Times escreveu sobre o perceptron na altura: *o embrião de um computador eletrónico que [a Marinha] espera que seja capaz de andar, falar, ver, escrever, reproduzir-se e estar consciente da sua existência.*

## Modelo do Perceptron

Suponha que temos N características no nosso modelo, caso em que o vetor de entrada seria um vetor de tamanho N. Um perceptron é um modelo de **classificação binária**, ou seja, pode distinguir entre duas classes de dados de entrada. Assumiremos que para cada vetor de entrada x a saída do nosso perceptron será +1 ou -1, dependendo da classe. A saída será calculada usando a fórmula:

y(x) = f(w<sup>T</sup>x)

onde f é uma função de ativação do tipo degrau

## Treino do Perceptron

Para treinar um perceptron precisamos encontrar um vetor de pesos w que classifique corretamente a maioria dos valores, ou seja, que resulte no menor **erro**. Este erro é definido pelo **critério do perceptron** da seguinte forma:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

onde:

* a soma é feita sobre os pontos de dados de treino i que resultam numa classificação errada
* x<sub>i</sub> é o dado de entrada, e t<sub>i</sub> é -1 ou +1 para exemplos negativos e positivos, respetivamente.

Este critério é considerado uma função dos pesos w, e precisamos minimizá-lo. Frequentemente, é usado um método chamado **descida do gradiente**, no qual começamos com alguns pesos iniciais w<sup>(0)</sup>, e depois, em cada passo, atualizamos os pesos de acordo com a fórmula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Aqui, η é a chamada **taxa de aprendizagem**, e ∇E(w) denota o **gradiente** de E. Depois de calcular o gradiente, obtemos

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

O algoritmo em Python é assim:

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

## Conclusão

Nesta lição, aprendeu sobre o perceptron, que é um modelo de classificação binária, e como treiná-lo usando um vetor de pesos.

## 🚀 Desafio

Se quiser tentar construir o seu próprio perceptron, experimente este laboratório no Microsoft Learn que usa o Azure ML designer


## Revisão & Estudo Autónomo

Para ver como podemos usar o perceptron para resolver um problema simples, bem como problemas do mundo real, e para continuar a aprender - vá para o notebook Perceptron.

Aqui está também um artigo interessante sobre perceptrons.

## Tarefa

Nesta lição, implementámos um perceptron para uma tarefa de classificação binária, e usamos para classificar entre dois dígitos manuscritos. Neste laboratório, é pedido que resolva o problema da classificação de dígitos na totalidade, ou seja, determinar qual o dígito que é mais provável corresponder a uma dada imagem.

* Instruções
* Notebook

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.