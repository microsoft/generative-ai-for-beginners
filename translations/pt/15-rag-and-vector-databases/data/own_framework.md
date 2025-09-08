<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:45:10+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "pt"
}
-->
# Introdução às Redes Neurais. Perceptrão Multi-Camada

Na secção anterior, aprendeu sobre o modelo mais simples de rede neural - o perceptrão de uma camada, um modelo linear de classificação binária.

Nesta secção, vamos expandir este modelo para um quadro mais flexível, permitindo-nos:

* realizar **classificação multiclasse** além da classificação binária
* resolver **problemas de regressão** além da classificação
* separar classes que não são linearmente separáveis

Também iremos desenvolver o nosso próprio framework modular em Python que nos permitirá construir diferentes arquiteturas de redes neurais.

## Formalização do Aprendizado de Máquina

Vamos começar por formalizar o problema do Aprendizado de Máquina. Suponha que temos um conjunto de dados de treino **X** com etiquetas **Y**, e precisamos construir um modelo *f* que faça as previsões mais precisas possíveis. A qualidade das previsões é medida pela **função de perda** ℒ. As seguintes funções de perda são frequentemente usadas:

* Para problemas de regressão, quando precisamos prever um número, podemos usar o **erro absoluto** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ou o **erro quadrático** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para classificação, usamos a **perda 0-1** (que é essencialmente o mesmo que a **acurácia** do modelo), ou a **perda logística**.

Para o perceptrão de um nível, a função *f* foi definida como uma função linear *f(x)=wx+b* (aqui *w* é a matriz de pesos, *x* é o vetor de características de entrada, e *b* é o vetor de bias). Para diferentes arquiteturas de redes neurais, esta função pode assumir formas mais complexas.

> No caso da classificação, é frequentemente desejável obter probabilidades das classes correspondentes como saída da rede. Para converter números arbitrários em probabilidades (por exemplo, para normalizar a saída), usamos frequentemente a função **softmax** σ, e a função *f* torna-se *f(x)=σ(wx+b)*

Na definição de *f* acima, *w* e *b* são chamados de **parâmetros** θ=⟨*w,b*⟩. Dado o conjunto de dados ⟨**X**,**Y**⟩, podemos calcular o erro total no conjunto de dados como uma função dos parâmetros θ.

> ✅ **O objetivo do treino da rede neural é minimizar o erro variando os parâmetros θ**

## Otimização por Gradiente Descendente

Existe um método bem conhecido de otimização de funções chamado **gradiente descendente**. A ideia é que podemos calcular a derivada (no caso multidimensional chamada **gradiente**) da função de perda em relação aos parâmetros, e variar os parâmetros de forma a que o erro diminua. Isto pode ser formalizado da seguinte forma:

* Inicializar os parâmetros com alguns valores aleatórios w<sup>(0)</sup>, b<sup>(0)</sup>
* Repetir o seguinte passo várias vezes:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Durante o treino, os passos de otimização devem ser calculados considerando o conjunto de dados completo (lembre-se que a perda é calculada como uma soma por todas as amostras de treino). No entanto, na prática, usamos pequenas porções do conjunto de dados chamadas **minibatches**, e calculamos os gradientes com base num subconjunto dos dados. Como o subconjunto é escolhido aleatoriamente a cada vez, este método é chamado **gradiente descendente estocástico** (SGD).

## Perceptrões Multi-Camada e Backpropagation

A rede de uma camada, como vimos acima, é capaz de classificar classes linearmente separáveis. Para construir um modelo mais rico, podemos combinar várias camadas da rede. Matematicamente, isto significa que a função *f* terá uma forma mais complexa, e será calculada em vários passos:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Aqui, α é uma **função de ativação não linear**, σ é a função softmax, e os parâmetros θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

O algoritmo de gradiente descendente mantém-se o mesmo, mas o cálculo dos gradientes torna-se mais complexo. Dada a regra da diferenciação em cadeia, podemos calcular as derivadas como:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ A regra da diferenciação em cadeia é usada para calcular as derivadas da função de perda em relação aos parâmetros.

Note que a parte mais à esquerda de todas estas expressões é a mesma, e assim podemos calcular as derivadas de forma eficiente começando pela função de perda e indo "para trás" através do grafo computacional. Por isso, o método de treino de um perceptrão multi-camada é chamado **backpropagation**, ou simplesmente 'backprop'.

> TODO: citação da imagem

> ✅ Iremos abordar o backprop com muito mais detalhe no nosso exemplo no notebook.

## Conclusão

Nesta lição, construímos a nossa própria biblioteca de redes neurais, e usamos-a para uma tarefa simples de classificação bidimensional.

## 🚀 Desafio

No notebook que acompanha, irá implementar o seu próprio framework para construir e treinar perceptrões multi-camada. Poderá ver em detalhe como funcionam as redes neurais modernas.

Prossiga para o notebook OwnFramework e trabalhe nele.

## Revisão & Estudo Autónomo

Backpropagation é um algoritmo comum usado em IA e ML, vale a pena estudá-lo com mais detalhe.

## Tarefa

Neste laboratório, é pedido que use o framework que construiu nesta lição para resolver a classificação de dígitos manuscritos MNIST.

* Instruções
* Notebook

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.