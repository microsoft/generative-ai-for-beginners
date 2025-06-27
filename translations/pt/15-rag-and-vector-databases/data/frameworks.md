<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:01:08+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "pt"
}
-->
# Frameworks de Redes Neurais

Como já aprendemos, para conseguir treinar redes neurais de forma eficiente precisamos fazer duas coisas:

* Operar em tensores, por exemplo, multiplicar, somar e calcular algumas funções como sigmoid ou softmax
* Calcular gradientes de todas as expressões, para realizar a otimização por descida de gradiente

Enquanto a biblioteca `numpy` pode fazer a primeira parte, precisamos de algum mecanismo para calcular gradientes. No nosso framework que desenvolvemos na seção anterior, tivemos que programar manualmente todas as funções derivadas dentro do método `backward`, que faz a retropropagação. Idealmente, um framework deveria nos dar a oportunidade de calcular gradientes de *qualquer expressão* que possamos definir.

Outra coisa importante é poder realizar cálculos na GPU, ou em outras unidades de computação especializadas, como TPU. O treinamento de redes neurais profundas requer *muitos* cálculos, e ser capaz de paralelizar esses cálculos em GPUs é muito importante.

> ✅ O termo 'paralelizar' significa distribuir os cálculos por vários dispositivos.

Atualmente, os dois frameworks neurais mais populares são: TensorFlow e PyTorch. Ambos fornecem uma API de baixo nível para operar com tensores tanto em CPU quanto em GPU. Além da API de baixo nível, há também uma API de alto nível, chamada Keras e PyTorch Lightning, respectivamente.

API de Baixo Nível | TensorFlow| PyTorch
-------------------|-------------------------------------|--------------------------------
API de Alto Nível  | Keras| Pytorch

**APIs de baixo nível** em ambos os frameworks permitem que você construa os chamados **gráficos computacionais**. Este gráfico define como calcular a saída (geralmente a função de perda) com parâmetros de entrada dados, e pode ser enviado para cálculo na GPU, se estiver disponível. Existem funções para diferenciar este gráfico computacional e calcular gradientes, que podem então ser usados para otimizar os parâmetros do modelo.

**APIs de alto nível** consideram redes neurais como uma **sequência de camadas**, e tornam a construção da maioria das redes neurais muito mais fácil. Treinar o modelo geralmente requer preparar os dados e então chamar uma função `fit` para fazer o trabalho.

A API de alto nível permite que você construa redes neurais típicas muito rapidamente, sem se preocupar com muitos detalhes. Ao mesmo tempo, a API de baixo nível oferece muito mais controle sobre o processo de treinamento, e por isso é muito utilizada em pesquisa, quando se está lidando com novas arquiteturas de redes neurais.

Também é importante entender que você pode usar ambas as APIs juntas, por exemplo, pode desenvolver sua própria arquitetura de camada de rede usando a API de baixo nível, e então usá-la dentro da rede maior construída e treinada com a API de alto nível. Ou pode definir uma rede usando a API de alto nível como uma sequência de camadas, e então usar seu próprio loop de treinamento de baixo nível para realizar a otimização. Ambas as APIs usam os mesmos conceitos básicos subjacentes, e são projetadas para funcionar bem juntas.

## Aprendizagem

Neste curso, oferecemos a maior parte do conteúdo tanto para PyTorch quanto para TensorFlow. Você pode escolher seu framework preferido e apenas passar pelos notebooks correspondentes. Se não tiver certeza de qual framework escolher, leia algumas discussões na internet sobre **PyTorch vs. TensorFlow**. Você também pode dar uma olhada em ambos os frameworks para obter uma melhor compreensão.

Sempre que possível, usaremos APIs de Alto Nível pela simplicidade. No entanto, acreditamos que é importante entender como as redes neurais funcionam desde o início, portanto, no começo, começamos trabalhando com API de baixo nível e tensores. No entanto, se você quiser começar rapidamente e não quiser gastar muito tempo aprendendo esses detalhes, pode pular esses e ir direto para os notebooks de API de alto nível.

## ✍️ Exercícios: Frameworks

Continue seu aprendizado nos seguintes notebooks:

API de Baixo Nível | Notebook TensorFlow+Keras | PyTorch
-------------------|-------------------------------------|--------------------------------
API de Alto Nível  | Keras | *PyTorch Lightning*

Após dominar os frameworks, vamos recapitular a noção de overfitting.

# Overfitting

Overfitting é um conceito extremamente importante em aprendizado de máquina, e é muito importante acertá-lo!

Considere o seguinte problema de aproximar 5 pontos (representados por `x` nos gráficos abaixo):

!linear | overfit
-------------------------|--------------------------
**Modelo Linear, 2 parâmetros** | **Modelo Não-linear, 7 parâmetros**
Erro de treinamento = 5.3 | Erro de treinamento = 0
Erro de validação = 5.1 | Erro de validação = 20

* À esquerda, vemos uma boa aproximação por linha reta. Porque o número de parâmetros é adequado, o modelo entende corretamente a distribuição dos pontos.
* À direita, o modelo é muito poderoso. Como temos apenas 5 pontos e o modelo tem 7 parâmetros, ele pode ajustar-se de forma a passar por todos os pontos, fazendo com que o erro de treinamento seja 0. No entanto, isso impede o modelo de entender o padrão correto por trás dos dados, portanto o erro de validação é muito alto.

É muito importante encontrar um equilíbrio correto entre a riqueza do modelo (número de parâmetros) e o número de amostras de treinamento.

## Por que o overfitting ocorre

  * Não há dados de treinamento suficientes
  * Modelo muito poderoso
  * Muito ruído nos dados de entrada

## Como detectar overfitting

Como você pode ver no gráfico acima, o overfitting pode ser detectado por um erro de treinamento muito baixo e um erro de validação alto. Normalmente, durante o treinamento, veremos os erros de treinamento e validação começarem a diminuir, e então em algum ponto o erro de validação pode parar de diminuir e começar a aumentar. Isso será um sinal de overfitting e o indicador de que provavelmente deveríamos parar o treinamento neste ponto (ou pelo menos fazer uma captura do modelo).

## Como prevenir o overfitting

Se você perceber que o overfitting está ocorrendo, pode fazer uma das seguintes ações:

 * Aumentar a quantidade de dados de treinamento
 * Diminuir a complexidade do modelo
 * Usar alguma técnica de regularização, como Dropout, que consideraremos mais tarde.

## Overfitting e o Tradeoff Viés-Variância

Overfitting é na verdade um caso de um problema mais genérico em estatísticas chamado Tradeoff Viés-Variância. Se considerarmos as possíveis fontes de erro em nosso modelo, podemos ver dois tipos de erros:

* **Erros de viés** são causados pelo nosso algoritmo não conseguir capturar corretamente a relação entre os dados de treinamento. Pode resultar do fato de que nosso modelo não é poderoso o suficiente (**underfitting**).
* **Erros de variância**, que são causados pelo modelo aproximando o ruído nos dados de entrada em vez de uma relação significativa (**overfitting**).

Durante o treinamento, o erro de viés diminui (à medida que nosso modelo aprende a aproximar os dados), e o erro de variância aumenta. É importante parar o treinamento - seja manualmente (quando detectamos overfitting) ou automaticamente (introduzindo regularização) - para prevenir o overfitting.

## Conclusão

Nesta lição, você aprendeu sobre as diferenças entre as várias APIs para os dois frameworks de IA mais populares, TensorFlow e PyTorch. Além disso, aprendeu sobre um tópico muito importante, o overfitting.

## 🚀 Desafio

Nos notebooks que acompanham, você encontrará 'tarefas' no final; percorra os notebooks e complete as tarefas.

## Revisão & Autoestudo

Faça algumas pesquisas sobre os seguintes tópicos:

- TensorFlow
- PyTorch
- Overfitting

Faça a si mesmo as seguintes perguntas:

- Qual é a diferença entre TensorFlow e PyTorch?
- Qual é a diferença entre overfitting e underfitting?

## Tarefa

Neste laboratório, você é solicitado a resolver dois problemas de classificação usando redes totalmente conectadas de camada única e multicamada, utilizando PyTorch ou TensorFlow.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se uma tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.