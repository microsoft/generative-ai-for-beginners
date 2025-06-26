<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:22:40+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "br"
}
-->
# Introdução às Redes Neurais. Perceptron Multicamadas

Na seção anterior, você aprendeu sobre o modelo de rede neural mais simples - o perceptron de uma camada, um modelo linear de classificação de duas classes.

Nesta seção, vamos expandir esse modelo para uma estrutura mais flexível, permitindo-nos:

* realizar **classificação multiclasse** além de duas classes
* resolver **problemas de regressão** além de classificação
* separar classes que não são linearmente separáveis

Também desenvolveremos nosso próprio framework modular em Python que nos permitirá construir diferentes arquiteturas de redes neurais.

## Formalização de Aprendizado de Máquina

Vamos começar formalizando o problema de Aprendizado de Máquina. Suponha que temos um conjunto de dados de treinamento **X** com rótulos **Y**, e precisamos construir um modelo *f* que fará previsões mais precisas. A qualidade das previsões é medida pela **função de perda** ℒ. As seguintes funções de perda são frequentemente usadas:

* Para problema de regressão, quando precisamos prever um número, podemos usar **erro absoluto** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ou **erro quadrático** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para classificação, usamos **perda 0-1** (que é essencialmente o mesmo que **precisão** do modelo), ou **perda logística**.

Para o perceptron de uma camada, a função *f* foi definida como uma função linear *f(x)=wx+b* (aqui *w* é a matriz de pesos, *x* é o vetor de características de entrada, e *b* é o vetor de viés). Para diferentes arquiteturas de redes neurais, essa função pode assumir uma forma mais complexa.

> No caso de classificação, muitas vezes é desejável obter probabilidades das classes correspondentes como saída da rede. Para converter números arbitrários em probabilidades (por exemplo, para normalizar a saída), frequentemente usamos a função **softmax** σ, e a função *f* torna-se *f(x)=σ(wx+b)*

Na definição de *f* acima, *w* e *b* são chamados de **parâmetros** θ=⟨*w,b*⟩. Dado o conjunto de dados ⟨**X**,**Y**⟩, podemos calcular um erro geral em todo o conjunto de dados como uma função dos parâmetros θ.

> ✅ **O objetivo do treinamento de redes neurais é minimizar o erro variando os parâmetros θ**

## Otimização por Gradiente Descendente

Existe um método bem conhecido de otimização de funções chamado **gradiente descendente**. A ideia é que podemos calcular uma derivada (no caso multidimensional chamada **gradiente**) da função de perda em relação aos parâmetros, e variar os parâmetros de tal forma que o erro diminua. Isso pode ser formalizado da seguinte maneira:

* Inicializar parâmetros com alguns valores aleatórios w<sup>(0)</sup>, b<sup>(0)</sup>
* Repetir o seguinte passo várias vezes:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Durante o treinamento, os passos de otimização devem ser calculados considerando todo o conjunto de dados (lembre-se de que a perda é calculada como uma soma de todas as amostras de treinamento). No entanto, na vida real, tomamos pequenas porções do conjunto de dados chamadas **minibatches**, e calculamos gradientes com base em um subconjunto de dados. Como o subconjunto é escolhido aleatoriamente a cada vez, esse método é chamado de **gradiente descendente estocástico** (SGD).

## Perceptrons Multicamadas e Retropropagação

Uma rede de uma camada, como vimos acima, é capaz de classificar classes linearmente separáveis. Para construir um modelo mais rico, podemos combinar várias camadas da rede. Matematicamente, isso significaria que a função *f* teria uma forma mais complexa e seria computada em várias etapas:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Aqui, α é uma **função de ativação não linear**, σ é uma função softmax, e os parâmetros θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

O algoritmo de gradiente descendente permaneceria o mesmo, mas seria mais difícil calcular os gradientes. Dada a regra da diferenciação em cadeia, podemos calcular as derivadas como:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ A regra da diferenciação em cadeia é usada para calcular as derivadas da função de perda em relação aos parâmetros.

Note que a parte mais à esquerda de todas essas expressões é a mesma, e assim podemos efetivamente calcular as derivadas começando pela função de perda e indo "para trás" através do gráfico computacional. Assim, o método de treinamento de um perceptron multicamadas é chamado de **retropropagação**, ou 'backprop'.

> TODO: citação de imagem

> ✅ Cobriremos a retropropagação em muito mais detalhes em nosso exemplo de notebook.

## Conclusão

Nesta lição, construímos nossa própria biblioteca de redes neurais e a usamos para uma tarefa simples de classificação bidimensional.

## 🚀 Desafio

No notebook complementar, você implementará seu próprio framework para construir e treinar perceptrons multicamadas. Você poderá ver em detalhes como as redes neurais modernas operam.

Prossiga para o notebook OwnFramework e trabalhe nele.

## Revisão & Autoestudo

Retropropagação é um algoritmo comum usado em IA e ML, vale a pena estudá-lo em mais detalhes.

## Tarefa

Neste laboratório, você é solicitado a usar o framework que construiu nesta lição para resolver a classificação de dígitos manuscritos MNIST.

* Instruções
* Notebook

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.