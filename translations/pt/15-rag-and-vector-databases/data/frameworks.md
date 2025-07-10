<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:30:25+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "pt"
}
-->
# Frameworks de Redes Neuronais

Como já aprendemos, para conseguir treinar redes neuronais de forma eficiente precisamos de fazer duas coisas:

* Operar sobre tensores, por exemplo multiplicar, somar e calcular algumas funções como sigmoid ou softmax
* Calcular gradientes de todas as expressões, para realizar a otimização por descida do gradiente

Embora a biblioteca `numpy` consiga fazer a primeira parte, precisamos de algum mecanismo para calcular gradientes. No nosso framework que desenvolvemos na secção anterior, tivemos de programar manualmente todas as funções derivadas dentro do método `backward`, que faz a retropropagação. Idealmente, um framework deveria dar-nos a possibilidade de calcular gradientes de *qualquer expressão* que possamos definir.

Outra coisa importante é conseguir realizar cálculos em GPU, ou em qualquer outra unidade de cálculo especializada, como TPU. O treino de redes neuronais profundas requer *muitos* cálculos, e conseguir paralelizar esses cálculos em GPUs é muito importante.

> ✅ O termo 'paralelizar' significa distribuir os cálculos por vários dispositivos.

Atualmente, os dois frameworks de redes neuronais mais populares são: TensorFlow e PyTorch. Ambos fornecem uma API de baixo nível para operar com tensores tanto em CPU como em GPU. Por cima da API de baixo nível, existe também uma API de alto nível, chamada Keras e PyTorch Lightning, respetivamente.

API de Baixo Nível | TensorFlow | PyTorch
-------------------|------------|---------
API de Alto Nível  | Keras      | PyTorch

As **APIs de baixo nível** em ambos os frameworks permitem construir os chamados **grafos computacionais**. Este grafo define como calcular a saída (normalmente a função de perda) com os parâmetros de entrada dados, e pode ser enviado para cálculo em GPU, se estiver disponível. Existem funções para diferenciar este grafo computacional e calcular gradientes, que depois podem ser usados para otimizar os parâmetros do modelo.

As **APIs de alto nível** consideram as redes neuronais como uma **sequência de camadas**, facilitando muito a construção da maioria das redes neuronais. O treino do modelo normalmente requer preparar os dados e depois chamar uma função `fit` para fazer o trabalho.

A API de alto nível permite construir redes neuronais típicas muito rapidamente sem se preocupar com muitos detalhes. Ao mesmo tempo, a API de baixo nível oferece muito mais controlo sobre o processo de treino, sendo por isso muito usada em investigação, quando se trabalha com novas arquiteturas de redes neuronais.

É também importante perceber que se podem usar ambas as APIs em conjunto, por exemplo, pode desenvolver a sua própria arquitetura de camada de rede usando a API de baixo nível, e depois usá-la dentro de uma rede maior construída e treinada com a API de alto nível. Ou pode definir uma rede usando a API de alto nível como uma sequência de camadas, e depois usar o seu próprio ciclo de treino de baixo nível para realizar a otimização. Ambas as APIs usam os mesmos conceitos básicos subjacentes e foram desenhadas para funcionar bem em conjunto.

## Aprendizagem

Neste curso, oferecemos a maior parte do conteúdo tanto para PyTorch como para TensorFlow. Pode escolher o framework que preferir e seguir apenas os notebooks correspondentes. Se não tiver a certeza de qual escolher, leia algumas discussões na internet sobre **PyTorch vs. TensorFlow**. Pode também explorar ambos os frameworks para obter uma melhor compreensão.

Sempre que possível, usaremos APIs de alto nível pela simplicidade. No entanto, acreditamos que é importante entender como as redes neuronais funcionam desde a base, por isso no início começamos a trabalhar com a API de baixo nível e tensores. Contudo, se quiser avançar rapidamente e não quiser perder muito tempo a aprender estes detalhes, pode saltar diretamente para os notebooks da API de alto nível.

## ✍️ Exercícios: Frameworks

Continue a sua aprendizagem nos seguintes notebooks:

API de Baixo Nível | Notebook TensorFlow+Keras | PyTorch
-------------------|----------------------------|---------
API de Alto Nível  | Keras                      | *PyTorch Lightning*

Depois de dominar os frameworks, vamos recapitular o conceito de overfitting.

# Overfitting

Overfitting é um conceito extremamente importante em machine learning, e é fundamental compreendê-lo bem!

Considere o seguinte problema de aproximar 5 pontos (representados por `x` nos gráficos abaixo):

!linear | overfit
-------------------------|--------------------------
**Modelo linear, 2 parâmetros** | **Modelo não linear, 7 parâmetros**
Erro de treino = 5.3 | Erro de treino = 0
Erro de validação = 5.1 | Erro de validação = 20

* À esquerda, vemos uma boa aproximação por uma linha reta. Como o número de parâmetros é adequado, o modelo percebe corretamente a distribuição dos pontos.
* À direita, o modelo é demasiado poderoso. Como só temos 5 pontos e o modelo tem 7 parâmetros, ele consegue ajustar-se de forma a passar por todos os pontos, fazendo o erro de treino ser 0. No entanto, isto impede o modelo de compreender o padrão correto por trás dos dados, pelo que o erro de validação é muito elevado.

É muito importante encontrar um equilíbrio correto entre a complexidade do modelo (número de parâmetros) e o número de amostras de treino.

## Por que ocorre overfitting

  * Dados de treino insuficientes
  * Modelo demasiado complexo
  * Muito ruído nos dados de entrada

## Como detetar overfitting

Como pode ver no gráfico acima, o overfitting pode ser detetado por um erro de treino muito baixo e um erro de validação elevado. Normalmente, durante o treino, veremos tanto o erro de treino como o de validação a diminuir, e depois, em algum ponto, o erro de validação pode deixar de diminuir e começar a aumentar. Este será um sinal de overfitting, e um indicador de que provavelmente devemos parar o treino nesse momento (ou pelo menos guardar uma cópia do modelo).

overfitting

## Como prevenir overfitting

Se perceber que está a ocorrer overfitting, pode fazer uma das seguintes coisas:

 * Aumentar a quantidade de dados de treino
 * Diminuir a complexidade do modelo
 * Usar alguma técnica de regularização, como Dropout, que iremos considerar mais tarde.

## Overfitting e o compromisso Bias-Variância

Overfitting é na verdade um caso de um problema mais genérico em estatística chamado compromisso Bias-Variância. Se considerarmos as possíveis fontes de erro no nosso modelo, podemos ver dois tipos de erros:

* **Erros de bias** são causados pelo nosso algoritmo não conseguir captar corretamente a relação entre os dados de treino. Pode resultar do facto de o nosso modelo não ser suficientemente poderoso (**underfitting**).
* **Erros de variância**, que são causados pelo modelo a aproximar o ruído nos dados de entrada em vez de uma relação significativa (**overfitting**).

Durante o treino, o erro de bias diminui (à medida que o modelo aprende a aproximar os dados), e o erro de variância aumenta. É importante parar o treino – manualmente (quando detetamos overfitting) ou automaticamente (introduzindo regularização) – para evitar overfitting.

## Conclusão

Nesta lição, aprendeu sobre as diferenças entre as várias APIs dos dois frameworks de IA mais populares, TensorFlow e PyTorch. Além disso, aprendeu sobre um tema muito importante, o overfitting.

## 🚀 Desafio

Nos notebooks que acompanham esta lição, encontrará 'tarefas' no final; trabalhe nos notebooks e complete as tarefas.

## Revisão & Estudo Autónomo

Faça alguma pesquisa sobre os seguintes tópicos:

- TensorFlow
- PyTorch
- Overfitting

Pergunte a si mesmo as seguintes questões:

- Qual é a diferença entre TensorFlow e PyTorch?
- Qual é a diferença entre overfitting e underfitting?

## Trabalho Prático

Neste laboratório, é pedido que resolva dois problemas de classificação usando redes totalmente conectadas de camada única e múltiplas camadas, utilizando PyTorch ou TensorFlow.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.