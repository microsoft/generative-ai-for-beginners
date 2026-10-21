# Introdução aos Modelos de Linguagem Pequenos para IA Generativa para Iniciantes
A IA Generativa é um campo fascinante da inteligência artificial que se centra na criação de sistemas capazes de gerar novo conteúdo. Este conteúdo pode variar desde texto e imagens até música e até ambientes virtuais completos. Uma das aplicações mais entusiasmantes da IA generativa é no domínio dos modelos de linguagem.

## O que são Modelos de Linguagem Pequenos?

Um Modelo de Linguagem Pequeno (SLM) representa uma variante reduzida de um modelo de linguagem grande (LLM), utilizando muitos dos princípios arquitetónicos e técnicas dos LLMs, enquanto apresenta uma pegada computacional significativamente reduzida. 

Os SLMs são um subconjunto de modelos de linguagem projetados para gerar texto semelhante ao humano. Ao contrário dos seus homólogos maiores, como o GPT-4, os SLMs são mais compactos e eficientes, tornando-os ideais para aplicações onde os recursos computacionais são limitados. Apesar de seu tamanho menor, eles ainda podem executar uma variedade de tarefas. Normalmente, os SLMs são construídos comprimindo ou destilando LLMs, com o objetivo de reter uma porção substancial da funcionalidade e capacidades linguísticas do modelo original. Esta redução no tamanho do modelo diminui a complexidade geral, tornando os SLMs mais eficientes em termos de uso de memória e necessidades computacionais. Apesar destas otimizações, os SLMs ainda podem realizar uma ampla gama de tarefas de processamento de linguagem natural (PLN):

- Geração de Texto: Criar frases ou parágrafos coerentes e contextualmente relevantes.
- Complemento de Texto: Prever e completar frases com base num prompt dado.
- Tradução: Converter texto de uma língua para outra.
- Resumo: Condensar textos longos em resumos mais curtos e fáceis de digerir.

Embora com alguns compromissos em desempenho ou profundidade de compreensão em comparação com os seus homólogos maiores. 

## Como Funcionam os Modelos de Linguagem Pequenos?
Os SLMs são treinados com grandes quantidades de dados textuais. Durante o treino, aprendem os padrões e estruturas da língua, permitindo-lhes gerar texto que seja ao mesmo tempo gramaticalmente correto e contextualmente apropriado. O processo de treino envolve:

- Recolha de Dados: Reunir grandes conjuntos de dados de texto de várias fontes.
- Pré-processamento: Limpar e organizar os dados para os tornar adequados para treino.
- Treino: Utilizar algoritmos de aprendizagem automática para ensinar o modelo a compreender e gerar texto.
- Ajuste Fino: Ajustar o modelo para melhorar o seu desempenho em tarefas específicas.

O desenvolvimento dos SLMs está alinhado com a necessidade crescente de modelos que possam ser implementados em ambientes com recursos limitados, como dispositivos móveis ou plataformas de computação na periferia (edge computing), onde os LLMs de grande escala podem ser impraticáveis devido à sua elevada necessidade de recursos. Ao focar na eficiência, os SLMs equilibram desempenho com acessibilidade, permitindo uma aplicação mais ampla em vários domínios.

![slm](../../../translated_images/pt-PT/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Objetivos de Aprendizagem

Nesta lição, esperamos introduzir o conhecimento sobre SLM e combiná-lo com o Microsoft Phi-3 para aprender diferentes cenários em conteúdo textual, visão e MoE.

No final desta lição, deverá ser capaz de responder às seguintes perguntas:

- O que é um SLM?
- Qual é a diferença entre SLM e LLM?
- O que é a Família Microsoft Phi-3/3.5?
- Como fazer inferência com a Família Microsoft Phi-3/3.5?

Pronto? Vamos começar.

## As Distinções entre Modelos de Linguagem Grandes (LLMs) e Modelos de Linguagem Pequenos (SLMs)

Tanto os LLMs como os SLMs baseiam-se em princípios fundamentais de aprendizagem automática probabilística, seguindo abordagens similares na sua concepção arquitetónica, metodologias de treino, processos de geração de dados e técnicas de avaliação de modelos. No entanto, vários fatores importantes diferenciam estes dois tipos de modelos.

## Aplicações dos Modelos de Linguagem Pequenos

Os SLMs têm uma ampla gama de aplicações, incluindo:

- Chatbots: Fornecer suporte ao cliente e interagir com os utilizadores de forma conversacional.
- Criação de Conteúdo: Ajudar escritores gerando ideias ou até mesmo redigindo artigos inteiros.
- Educação: Ajudar estudantes em trabalhos escritos ou na aprendizagem de novas línguas.
- Acessibilidade: Criar ferramentas para pessoas com deficiências, como sistemas de texto para fala.

**Tamanho**
  
Uma distinção primordial entre LLMs e SLMs reside na escala dos modelos. LLMs, como o ChatGPT (GPT-4), podem compreender aproximadamente 1,76 biliões de parâmetros, enquanto os SLMs open-source como o Mistral 7B são projetados com significativamente menos parâmetros — aproximadamente 7 mil milhões. Esta disparidade deve-se principalmente às diferenças na arquitetura do modelo e nos processos de treino. Por exemplo, o ChatGPT emprega um mecanismo de self-attention num quadro encoder-decoder, enquanto o Mistral 7B usa atenção com janela deslizante, que permite um treino mais eficiente dentro de um modelo apenas decodificador. Esta variação arquitetónica tem implicações profundas na complexidade e desempenho destes modelos.

**Compreensão**

Os SLMs são tipicamente otimizados para desempenho em domínios específicos, tornando-os altamente especializados mas potencialmente limitados na capacidade de fornecer uma compreensão contextual ampla através de múltiplos campos de conhecimento. Em contraste, os LLMs visam simular inteligência semelhante à humana num nível mais abrangente. Treinados em conjuntos de dados vastos e diversificados, os LLMs são projetados para atuar bem em vários domínios, oferecendo maior versatilidade e adaptabilidade. Consequentemente, os LLMs são mais adequados para uma gama mais ampla de tarefas descendentes, como processamento de linguagem natural e programação.

**Computação**

O treino e a implementação dos LLMs são processos que consomem muitos recursos, frequentemente requerendo infraestruturas computacionais significativas, incluindo clusters de GPUs em grande escala. Por exemplo, treinar um modelo como o ChatGPT do zero pode necessitar de milhares de GPUs ao longo de períodos prolongados. Em contraste, os SLMs, com seus contagens de parâmetros menores, são mais acessíveis em termos de recursos computacionais. Modelos como o Mistral 7B podem ser treinados e executados em máquinas locais equipadas com GPUs moderadas, embora o treino ainda exija várias horas em múltiplas GPUs.

**Viés**

O viés é um problema conhecido nos LLMs, principalmente devido à natureza dos dados de treino. Estes modelos frequentemente dependem de dados brutos disponibilizados publicamente na internet, que podem sub-representar ou deturpar certos grupos, introduzir rotulagem errónea ou refletir vieses linguísticos influenciados por dialectos, variações geográficas e regras gramaticais. Adicionalmente, a complexidade das arquiteturas dos LLMs pode inadvertidamente exacerbar o viés, que pode passar despercebido sem ajuste fino cuidadoso. Por outro lado, os SLMs, sendo treinados em conjuntos de dados mais restritos e específicos de domínio, são inerentemente menos suscetíveis a tais vieses, embora não sejam imunes a eles.

**Inferência**

O tamanho reduzido dos SLMs proporciona-lhes uma vantagem significativa em termos de velocidade de inferência, permitindo-lhes gerar saídas de forma eficiente em hardware local sem a necessidade de processamento paralelo extenso. Em contraste, os LLMs, devido ao seu tamanho e complexidade, frequentemente requerem recursos computacionais paralelos substanciais para atingir tempos de inferência aceitáveis. A presença de múltiplos utilizadores concorrentes ainda diminui os tempos de resposta dos LLMs, especialmente quando implementados em grande escala.

Em resumo, embora tanto os LLMs como os SLMs partilhem uma base fundamental em aprendizagem automática, diferem significativamente em termos de tamanho do modelo, requisitos de recursos, compreensão contextual, suscetibilidade a viés e velocidade de inferência. Estas distinções refletem a sua adequação relativa para diferentes casos de uso, com os LLMs sendo mais versáteis mas pesados em recursos, e os SLMs oferecendo uma eficiência mais específica de domínio com menor exigência computacional.

***Nota: Nesta lição, iremos introduzir o SLM usando o Microsoft Phi-3 / 3.5 como exemplo.***

## Introdução à Família Phi-3 / Phi-3.5

A família Phi-3 / 3.5 direciona principalmente cenários de aplicação de texto, visão e Agente (MoE):

### Phi-3 / 3.5 Instruct

Principalmente para geração de texto, conclusão de chat e extração de informação de conteúdo, etc.

**Phi-3-mini**

O modelo de linguagem 3.8B está disponível na Microsoft Foundry, Hugging Face e Ollama. Os modelos Phi-3 superam significativamente modelos de linguagem de tamanhos iguais e maiores em benchmarks principais (ver números de benchmark abaixo, números mais altos são melhores). O Phi-3-mini supera modelos com o dobro do seu tamanho, enquanto o Phi-3-small e o Phi-3-medium superam modelos maiores, incluindo o GPT-3.5.

**Phi-3-small e medium**

Com apenas 7B parâmetros, o Phi-3-small vence o GPT-3.5T numa variedade de benchmarks de linguagem, raciocínio, codificação e matemática.

O Phi-3-medium com 14B parâmetros continua esta tendência e supera o Gemini 1.0 Pro.

**Phi-3.5-mini**

Podemos considerá-lo um upgrade do Phi-3-mini. Embora os parâmetros permaneçam inalterados, melhora a capacidade de suportar múltiplas línguas (suporta 20+ línguas: Árabe, Chinês, Checo, Dinamarquês, Holandês, Inglês, Finlandês, Francês, Alemão, Hebraico, Húngaro, Italiano, Japonês, Coreano, Norueguês, Polaco, Português, Russo, Espanhol, Sueco, Tailandês, Turco, Ucraniano) e adiciona suporte mais forte para contextos longos.

O Phi-3.5-mini com 3.8B parâmetros supera modelos de linguagem do mesmo tamanho e está ao nível de modelos com o dobro do seu tamanho.

### Phi-3 / 3.5 Vision

Podemos pensar no modelo Instruct do Phi-3/3.5 como a capacidade do Phi de compreender, e a Visão é o que dá ao Phi olhos para entender o mundo.


**Phi-3-Vision**

O Phi-3-vision, com apenas 4.2B parâmetros, continua esta tendência e supera modelos maiores como Claude-3 Haiku e Gemini 1.0 Pro V em tarefas gerais de raciocínio visual, OCR e compreensão de tabelas e diagramas.


**Phi-3.5-Vision**

O Phi-3.5-Vision é também uma atualização do Phi-3-Vision, adicionando suporte para múltiplas imagens. Pode considerá-lo uma melhoria na visão, não só pode ver imagens, mas também vídeos.

O Phi-3.5-vision supera modelos maiores como Claude-3.5 Sonnet e Gemini 1.5 Flash em tarefas de OCR, compreensão de tabelas e gráficos e iguala modelos em tarefas gerais de raciocínio visual. Suporta entrada multi-frame, ou seja, realiza raciocínio sobre múltiplas imagens de entrada.


### Phi-3.5-MoE

***Mistura de Especialistas (MoE)*** permite que os modelos sejam pré-treinados com muito menos computação, o que significa que pode escalar dramaticamente o tamanho do modelo ou do conjunto de dados com o mesmo orçamento computacional que um modelo denso. Em particular, um modelo MoE deve alcançar a mesma qualidade que o seu homólogo denso muito mais rapidamente durante o pré-treinamento.

O Phi-3.5-MoE compreende 16 módulos especialistas de 3.8B cada. O Phi-3.5-MoE com apenas 6.6B parâmetros ativos alcança um nível similar de raciocínio, compreensão de linguagem e matemática que modelos muito maiores.

Podemos usar o modelo da Família Phi-3/3.5 baseado em diferentes cenários. Ao contrário do LLM, pode implementar Phi-3/3.5-mini ou Phi-3/3.5-Vision em dispositivos edge.


## Como usar modelos da Família Phi-3/3.5

Esperamos usar o Phi-3/3.5 em diferentes cenários. Seguidamente, usaremos Phi-3/3.5 baseado em diferentes cenários.

![phi3](../../../translated_images/pt-PT/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferência via APIs na Cloud

**Modelos Microsoft Foundry**

> **Nota:** Os Modelos GitHub serão descontinuados no final de julho de 2026. [Modelos Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) são o substituto direto.

Os Modelos Microsoft Foundry são a forma mais direta. Pode aceder rapidamente ao modelo Phi-3/3.5-Instruct através do catálogo de modelos Foundry. Combinado com o Azure AI Inference SDK / OpenAI SDK, pode aceder à API através de código para completar a chamada Phi-3/3.5-Instruct. Também pode testar diferentes efeitos através do Playground.

- Demonstração: Comparação dos efeitos do Phi-3-mini e Phi-3.5-mini em cenários chineses

![phi3](../../../translated_images/pt-PT/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/pt-PT/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Ou se quiser usar os modelos de visão e MoE, pode usar o Microsoft Foundry para completar a chamada. Se estiver interessado, pode ler o Livro de Receitas do Phi-3 para aprender como chamar Phi-3/3.5 Instruct, Vision, MoE através do Microsoft Foundry [Clique neste link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Para além do catálogo de Modelos Microsoft Foundry baseado na cloud, também pode usar [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) para completar chamadas relacionadas. Pode visitar o NVIDIA NIM para completar as chamadas API da Família Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) é um conjunto de microserviços de inferência acelerados projetados para ajudar desenvolvedores a implementar modelos de IA de forma eficiente em vários ambientes, incluindo clouds, data centers e estações de trabalho.

Aqui estão algumas características chave do NVIDIA NIM:

- **Facilidade de Implementação:** O NIM permite a implementação de modelos de IA com um único comando, tornando fácil a integração em fluxos de trabalho existentes.
- **Desempenho Otimizado:** Usa motores de inferência pré-otimizados da NVIDIA, como TensorRT e TensorRT-LLM, para garantir baixa latência e alto débito.
- **Escalabilidade:** O NIM suporta autoscaling no Kubernetes, permitindo lidar eficazmente com cargas de trabalho variáveis.
- **Segurança e Controlo:** As organizações podem manter controlo sobre os seus dados e aplicações ao hospedar os microserviços NIM na sua própria infraestrutura gerida.
- **APIs Standard:** O NIM fornece APIs padrão da indústria, facilitando a construção e integração de aplicações de IA como chatbots, assistentes de IA e muito mais.

O NIM faz parte do NVIDIA AI Enterprise, que visa simplificar a implementação e operacionalização dos modelos de IA, garantindo que funcionem de forma eficiente nas GPUs da NVIDIA.

- Demonstração: Usar o NVIDIA NIM para chamar a Phi-3.5-Vision-API  [[Clique neste link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Executar Phi-3/3.5 Localmente
Inferência em relação à Phi-3, ou qualquer modelo de linguagem como o GPT-3, refere-se ao processo de gerar respostas ou previsões com base na entrada que recebe. Quando fornece um prompt ou questão à Phi-3, esta usa a sua rede neural treinada para inferir a resposta mais provável e relevante, analisando padrões e relações nos dados em que foi treinada.

**Hugging Face Transformer**
Hugging Face Transformers é uma biblioteca poderosa concebida para processamento de linguagem natural (NLP) e outras tarefas de machine learning. Aqui estão alguns pontos chave sobre ela:

1. **Modelos Pré-treinados**: Disponibiliza milhares de modelos pré-treinados que podem ser usados para várias tarefas, como classificação de texto, reconhecimento de entidades nomeadas, resposta a perguntas, sumarização, tradução e geração de texto.

2. **Interoperabilidade de Frameworks**: A biblioteca suporta múltiplos frameworks de deep learning, incluindo PyTorch, TensorFlow e JAX. Isto permite treinar um modelo num framework e usá-lo noutro.

3. **Capacidades Multimodais**: Para além de NLP, Hugging Face Transformers também suporta tarefas em visão computacional (ex.: classificação de imagens, deteção de objetos) e processamento de áudio (ex.: reconhecimento de fala, classificação de áudio).

4. **Facilidade de Uso**: A biblioteca oferece APIs e ferramentas para descarregar e afinar modelos com facilidade, tornando-a acessível tanto para iniciantes como para especialistas.

5. **Comunidade e Recursos**: A Hugging Face tem uma comunidade vibrante e documentação extensa, tutoriais e guias para ajudar os utilizadores a começar e tirar o máximo proveito da biblioteca.
[documentação oficial](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ou o seu [repositório no GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Este é o método mais utilizado, mas também requer aceleração por GPU. Afinal, cenários como Visão e MoE requerem muitos cálculos, que serão muito lentos na CPU se não forem quantizados.


- Demonstração: Usar Transformer para chamar Phi-3.5-Instruct [Clique neste link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstração: Usar Transformer para chamar Phi-3.5-Vision [Clique neste link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstração: Usar Transformer para chamar Phi-3.5-MoE [Clique neste link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) é uma plataforma concebida para facilitar a execução de grandes modelos de linguagem (LLMs) localmente no seu computador. Suporta vários modelos como Llama 3.1, Phi 3, Mistral e Gemma 2, entre outros. A plataforma simplifica o processo ao agrupar pesos dos modelos, configuração e dados num único pacote, tornando mais acessível para os utilizadores personalizar e criar os seus próprios modelos. Ollama está disponível para macOS, Linux e Windows. É uma ótima ferramenta se pretende experimentar ou implementar LLMs sem depender de serviços na nuvem. Ollama é o método mais direto, só precisa de executar o seguinte comando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) é o runtime offline e no dispositivo da Microsoft para correr modelos como a Phi completamente no seu próprio hardware - não é necessário subscrição Azure, chave API ou ligação de rede. Ele escolhe automaticamente o melhor fornecedor de execução disponível (NPU, GPU ou CPU) e expõe um endpoint compatível com OpenAI, para que o código existente `openai`/Azure AI Inference SDK possa apontar para ele com mudanças mínimas. Veja a [documentação do Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para começar.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Ou use o SDK diretamente em Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime para GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) é um acelerador de aprendizagem automática para inferência e treino multiplataforma. ONNX Runtime para Inteligência Artificial Generativa (GENAI) é uma ferramenta poderosa que ajuda a executar modelos de IA generativa de forma eficiente em várias plataformas.

## O que é o ONNX Runtime?
ONNX Runtime é um projeto open-source que permite inferência de alto desempenho de modelos de machine learning. Suporta modelos no formato Open Neural Network Exchange (ONNX), que é um padrão para representar modelos de machine learning. A inferência ONNX Runtime pode permitir experiências mais rápidas para os clientes e custos mais baixos, suportando modelos de frameworks de deep learning como PyTorch e TensorFlow/Keras, bem como bibliotecas clássicas de machine learning como scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime é compatível com diferentes hardware, drivers e sistemas operativos, e proporciona desempenho ótimo ao aproveitar aceleradores de hardware se aplicável juntamente com otimizações e transformações de gráficos.

## O que é a IA Generativa?
IA Generativa refere-se a sistemas de IA que podem gerar novo conteúdo, como texto, imagens ou música, baseado nos dados em que foram treinados. Exemplos incluem modelos de linguagem como o GPT-3 e modelos de geração de imagens como o Stable Diffusion. A biblioteca ONNX Runtime para GenAI fornece o ciclo de IA generativa para modelos ONNX, incluindo inferência com ONNX Runtime, processamento de logits, pesquisa e amostragem, e gestão do cache KV.

## ONNX Runtime para GENAI
ONNX Runtime para GENAI estende as capacidades do ONNX Runtime para suportar modelos de IA generativa. Aqui estão algumas funcionalidades principais:

- **Suporte a Diversas Plataformas:** Funciona em várias plataformas, incluindo Windows, Linux, macOS, Android e iOS.
- **Suporte a Modelos:** Suporta muitos modelos populares de IA generativa, como LLaMA, GPT-Neo, BLOOM, e mais.
- **Otimização de Desempenho:** Inclui otimizações para diferentes aceleradores de hardware como GPUs NVIDIA, GPUs AMD, e mais2.
- **Facilidade de Uso:** Disponibiliza APIs para integração fácil em aplicações, permitindo gerar texto, imagens e outro conteúdo com código mínimo.
- Os utilizadores podem chamar um método generate() de alto nível, ou executar cada iteração do modelo num ciclo, gerando um token de cada vez, e opcionalmente atualizando parâmetros de geração dentro do ciclo.
- O runtime ONNX também suporta pesquisa gulosa/beam search e amostragem TopP, TopK para gerar sequências de tokens e processamento de logits incorporado como penalizações de repetição. Pode também adicionar facilmente pontuações personalizadas.

## Começar
Para começar com ONNX Runtime para GENAI, pode seguir estes passos:

### Instalar ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalar as Extensões de IA Generativa:
```Python
pip install onnxruntime-genai
```

### Executar um Modelo: Aqui está um exemplo simples em Python:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demonstração: Usar ONNX Runtime GenAI para chamar Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Outros**

Para além do ONNX Runtime, Ollama e métodos de referência Foundry Local, podemos também completar a referência de modelos quantitativos baseados nos métodos de referência fornecidos por diferentes fabricantes, como o framework Apple MLX com Apple Metal, Qualcomm QNN com NPU, Intel OpenVINO com CPU/GPU, etc. Pode também obter mais conteúdos do [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mais

Aprendemos os fundamentos da Família Phi-3/3.5, mas para aprender mais sobre SLM precisamos de mais conhecimento. Pode encontrar as respostas no Phi-3 Cookbook. Se quiser aprender mais, por favor visite o [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->