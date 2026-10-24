# Introdução aos Pequenos Modelos de Linguagem para IA Generativa para Iniciantes
IA Generativa é um campo fascinante da inteligência artificial que se concentra na criação de sistemas capazes de gerar novos conteúdos. Esse conteúdo pode variar desde texto e imagens até música e até ambientes virtuais inteiros. Uma das aplicações mais empolgantes da IA generativa está no campo dos modelos de linguagem.

## O que São Pequenos Modelos de Linguagem?

Um Pequeno Modelo de Linguagem (SLM) representa uma variante reduzida de um grande modelo de linguagem (LLM), aproveitando muitos dos princípios arquitetônicos e técnicas dos LLMs, ao mesmo tempo em que apresenta uma pegada computacional significativamente menor.

Os SLMs são um subconjunto de modelos de linguagem projetados para gerar texto semelhante ao humano. Diferentemente de seus equivalentes maiores, como o GPT-4, os SLMs são mais compactos e eficientes, tornando-os ideais para aplicações onde os recursos computacionais são limitados. Apesar do tamanho menor, ainda podem realizar uma variedade de tarefas. Tipicamente, os SLMs são construídos comprimindo ou destilando LLMs, com o objetivo de reter uma parte substancial da funcionalidade original e das capacidades linguísticas do modelo. Essa redução no tamanho do modelo diminui a complexidade geral, tornando os SLMs mais eficientes tanto em termos de uso de memória quanto de requisitos computacionais. Apesar dessas otimizações, os SLMs ainda podem executar uma ampla gama de tarefas de processamento de linguagem natural (PLN):

- Geração de Texto: Criar sentenças ou parágrafos coerentes e contextualmente relevantes.
- Completação de Texto: Prever e completar sentenças com base em um prompt fornecido.
- Tradução: Converter texto de um idioma para outro.
- Resumo: Condensar textos longos em resumos mais curtos e compreensíveis.

Embora com algumas compensações em desempenho ou profundidade de entendimento em comparação com seus equivalentes maiores.

## Como Funcionam os Pequenos Modelos de Linguagem?
Os SLMs são treinados com grandes quantidades de dados de texto. Durante o treinamento, eles aprendem os padrões e estruturas da linguagem, permitindo gerar textos tanto gramaticalmente corretos quanto contextualmente apropriados. O processo de treinamento envolve:

- Coleta de Dados: Reunir grandes conjuntos de dados de texto de várias fontes.
- Pré-processamento: Limpar e organizar os dados para torná-los adequados para o treinamento.
- Treinamento: Utilizar algoritmos de aprendizado de máquina para ensinar o modelo a compreender e gerar texto.
- Ajuste Fino: Ajustar o modelo para melhorar seu desempenho em tarefas específicas.

O desenvolvimento dos SLMs está alinhado com a crescente necessidade por modelos que possam ser implantados em ambientes com recursos limitados, como dispositivos móveis ou plataformas de computação na borda, onde LLMs em grande escala podem ser impraticáveis devido à sua alta demanda por recursos. Ao focar na eficiência, os SLMs equilibram desempenho com acessibilidade, possibilitando uma aplicação mais ampla em diversos domínios.

![slm](../../../translated_images/pt-BR/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Objetivos de Aprendizagem

Nesta lição, esperamos apresentar o conhecimento sobre SLM e combiná-lo com o Microsoft Phi-3 para aprender diferentes cenários em conteúdo de texto, visão e MoE.

Ao final desta lição, você deverá conseguir responder às seguintes perguntas:

- O que é SLM?
- Qual a diferença entre SLM e LLM?
- O que é a Família Microsoft Phi-3/3.5?
- Como executar inferência com a Família Microsoft Phi-3/3.5?

Pronto? Vamos começar.

## As Diferenças entre Grandes Modelos de Linguagem (LLMs) e Pequenos Modelos de Linguagem (SLMs)

Tanto LLMs quanto SLMs são baseados em princípios fundamentais de aprendizado de máquina probabilístico, seguindo abordagens semelhantes em seu design arquitetônico, metodologias de treinamento, processos de geração de dados e técnicas de avaliação de modelos. Contudo, vários fatores-chave distinguem esses dois tipos de modelos.

## Aplicações dos Pequenos Modelos de Linguagem

Os SLMs têm uma ampla variedade de aplicações, incluindo:

- Chatbots: Fornecer suporte ao cliente e interagir com usuários de forma conversacional.
- Criação de Conteúdo: Auxiliar escritores gerando ideias ou até mesmo rascunhando artigos inteiros.
- Educação: Ajudar estudantes em tarefas de escrita ou aprendizado de novos idiomas.
- Acessibilidade: Criar ferramentas para pessoas com deficiências, como sistemas de texto para fala.

**Tamanho**
  
A principal distinção entre LLMs e SLMs está na escala dos modelos. LLMs, como ChatGPT (GPT-4), podem conter aproximadamente 1,76 trilhão de parâmetros, enquanto SLMs de código aberto como Mistral 7B são projetados com um número significativamente menor de parâmetros—aproximadamente 7 bilhões. Essa disparidade é principalmente devido a diferenças na arquitetura do modelo e processos de treinamento. Por exemplo, o ChatGPT emprega um mecanismo de autoatenção dentro de uma estrutura encoder-decoder, enquanto o Mistral 7B usa atenção de janela deslizante, o que permite um treinamento mais eficiente dentro de um modelo apenas decodificador. Essa variação arquitetônica tem implicações profundas na complexidade e desempenho desses modelos.

**Compreensão**

Os SLMs geralmente são otimizados para desempenho em domínios específicos, tornando-os altamente especializados, mas potencialmente limitados em sua capacidade de fornecer entendimento contextual amplo em múltiplos campos do conhecimento. Em contraste, os LLMs visam simular uma inteligência semelhante à humana em um nível mais abrangente. Treinados em vastos e diversos conjuntos de dados, os LLMs são projetados para ter bom desempenho em vários domínios, oferecendo maior versatilidade e adaptabilidade. Consequentemente, os LLMs são mais adequados para uma gama mais ampla de tarefas posteriores, como processamento de linguagem natural e programação.

**Computação**

O treinamento e a implantação dos LLMs são processos intensivos em recursos, frequentemente requerendo infraestrutura computacional significativa, incluindo clusters de GPU em larga escala. Por exemplo, treinar um modelo como o ChatGPT do zero pode necessitar de milhares de GPUs ao longo de períodos extensos. Em contraste, os SLMs, com seu número menor de parâmetros, são mais acessíveis em termos de recursos computacionais. Modelos como o Mistral 7B podem ser treinados e executados em máquinas locais equipadas com GPUs de capacidade moderada, embora o treinamento ainda demande várias horas distribuídas em múltiplas GPUs.

**Viés**

O viés é um problema conhecido nos LLMs, principalmente devido à natureza dos dados de treinamento. Esses modelos frequentemente dependem de dados brutos, disponíveis abertamente na internet, que podem sub-representar ou representar erroneamente certos grupos, introduzir rotulações incorretas ou refletir vieses linguísticos influenciados por dialeto, variações geográficas e regras gramaticais. Além disso, a complexidade das arquiteturas dos LLMs pode inadvertidamente exacerbar o viés, o que pode passar despercebido sem um ajuste fino cuidadoso. Por outro lado, os SLMs, por serem treinados em conjuntos de dados mais restritos e específicos por domínio, são inerentemente menos suscetíveis a tais vieses, embora não sejam imunes a eles.

**Inferência**

O tamanho reduzido dos SLMs lhes confere uma vantagem significativa em termos de velocidade de inferência, permitindo gerar saídas de forma eficiente em hardware local sem a necessidade de processamento paralelo extensivo. Em contraste, os LLMs, devido ao seu tamanho e complexidade, frequentemente requerem recursos computacionais paralelos substanciais para alcançar tempos de inferência aceitáveis. A presença de múltiplos usuários concorrentes ainda reduz os tempos de resposta dos LLMs, especialmente quando implantados em larga escala.

Em resumo, embora LLMs e SLMs compartilhem uma base fundamental em aprendizado de máquina, diferem significativamente em termos de tamanho do modelo, requisitos de recursos, compreensão contextual, suscetibilidade a vieses e velocidade de inferência. Essas distinções refletem sua adequação respectiva para diferentes casos de uso, com os LLMs sendo mais versáteis, porém mais exigentes em recursos, e os SLMs oferecendo eficiência mais específica ao domínio com menores exigências computacionais.

***Nota: Nesta lição, apresentaremos os SLM usando Microsoft Phi-3 / 3.5 como exemplo.***

## Apresentação da Família Phi-3 / Phi-3.5

A Família Phi-3 / 3.5 foca principalmente em cenários de aplicação de texto, visão e Agente (MoE):

### Phi-3 / 3.5 Instruct

Principalmente para geração de texto, conclusão de chat e extração de informações de conteúdo, entre outros.

**Phi-3-mini**

O modelo de linguagem com 3.8B está disponível no Microsoft Foundry, Hugging Face e Ollama. Os modelos Phi-3 superam significativamente modelos de linguagem de tamanhos iguais e maiores em benchmarks-chave (veja os números dos benchmarks abaixo, números maiores são melhores). O Phi-3-mini supera modelos com o dobro de seu tamanho, enquanto o Phi-3-small e Phi-3-medium superam modelos maiores, incluindo o GPT-3.5.

**Phi-3-small & medium**

Com apenas 7B parâmetros, o Phi-3-small supera o GPT-3.5T em vários benchmarks de linguagem, raciocínio, codificação e matemática.

O Phi-3-medium, com 14B parâmetros, continua essa tendência e supera o Gemini 1.0 Pro.

**Phi-3.5-mini**

Podemos considerá-lo como uma atualização do Phi-3-mini. Embora os parâmetros permaneçam inalterados, ele melhora a capacidade de suporte a múltiplos idiomas (suporta mais de 20 idiomas: Árabe, Chinês, Tcheco, Dinamarquês, Holandês, Inglês, Finlandês, Francês, Alemão, Hebraico, Húngaro, Italiano, Japonês, Coreano, Norueguês, Polonês, Português, Russo, Espanhol, Sueco, Tailandês, Turco, Ucraniano) ​​e adiciona suporte mais forte para contexto longo.

O Phi-3.5-mini, com 3.8B parâmetros, supera modelos de linguagem do mesmo tamanho e está no mesmo nível de modelos com o dobro do seu tamanho.

### Phi-3 / 3.5 Vision

Podemos pensar no modelo Instruct do Phi-3/3.5 como a habilidade do Phi de entender, e Vision é o que dá ao Phi olhos para entender o mundo.


**Phi-3-Vision**

O Phi-3-vision, com apenas 4.2B parâmetros, continua essa tendência e supera modelos maiores como Claude-3 Haiku e Gemini 1.0 Pro V em tarefas gerais de raciocínio visual, OCR, e compreensão de tabelas e diagramas.


**Phi-3.5-Vision**

O Phi-3.5-Vision também é uma atualização do Phi-3-Vision, adicionando suporte para múltiplas imagens. Podemos pensar nisso como uma melhoria na visão: não apenas pode ver imagens, mas também vídeos.

O Phi-3.5-vision supera modelos maiores como Claude-3.5 Sonnet e Gemini 1.5 Flash em tarefas de OCR, compreensão de tabelas e gráficos, e está no mesmo nível em tarefas gerais de raciocínio visual. Suporta entrada de múltiplos quadros, ou seja, realiza raciocínio em múltiplas imagens de entrada.


### Phi-3.5-MoE

***Mistura de Especialistas (MoE)*** permite que os modelos sejam pré-treinados com muito menos computação, o que significa que você pode ampliar dramaticamente o tamanho do modelo ou do conjunto de dados com o mesmo orçamento computacional de um modelo denso. Em particular, um modelo MoE deve alcançar a mesma qualidade de seu equivalente denso muito mais rápido durante o pré-treinamento.

O Phi-3.5-MoE é composto por 16 módulos especialistas de 3.8B cada. O Phi-3.5-MoE, com apenas 6.6B parâmetros ativos, alcança um nível semelhante de raciocínio, compreensão de linguagem e matemática que modelos muito maiores.

Podemos usar o modelo da Família Phi-3/3.5 baseado em diferentes cenários. Diferente do LLM, você pode implantar Phi-3/3.5-mini ou Phi-3/3.5-Vision em dispositivos na borda.


## Como usar os modelos da Família Phi-3/3.5

Esperamos usar o Phi-3/3.5 em diferentes cenários. A seguir, usaremos o Phi-3/3.5 baseado em diferentes cenários.

![phi3](../../../translated_images/pt-BR/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferência via APIs na Nuvem

**Modelos Microsoft Foundry**

> **Nota:** O GitHub Models será descontinuado no final de julho de 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) é o substituto direto.

O Microsoft Foundry Models é a forma mais direta. Você pode acessar rapidamente o modelo Phi-3/3.5-Instruct através do catálogo de modelos Foundry. Combinado com o Azure AI Inference SDK / OpenAI SDK, você pode acessar a API via código para realizar chamadas ao Phi-3/3.5-Instruct. Você também pode testar diferentes efeitos por meio do Playground.

- Demonstração: Comparação dos efeitos do Phi-3-mini e Phi-3.5-mini em cenários chineses

![phi3](../../../translated_images/pt-BR/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/pt-BR/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Ou se quisermos usar os modelos de visão e MoE, você pode usar o Microsoft Foundry para realizar a chamada. Se estiver interessado, pode ler o Phi-3 Cookbook para aprender como chamar Phi-3/3.5 Instruct, Vision, MoE através do Microsoft Foundry [Clique neste link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Além do catálogo de modelos Microsoft Foundry baseado na nuvem, você também pode usar [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) para realizar chamadas relacionadas. Você pode visitar o NVIDIA NIM para completar as chamadas API da Família Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) é um conjunto de microserviços acelerados de inferência projetados para ajudar desenvolvedores a implantar modelos de IA de forma eficiente em diversos ambientes, incluindo nuvens, datacenters e estações de trabalho.

Aqui estão alguns recursos chave do NVIDIA NIM:

- **Facilidade de Implantação:** O NIM permite a implantação de modelos de IA com um único comando, facilitando a integração em fluxos de trabalho existentes.
- **Desempenho Otimizado:** Ele aproveita os motores de inferência pré-otimizados da NVIDIA, como TensorRT e TensorRT-LLM, para garantir baixa latência e alta taxa de transferência.
- **Escalabilidade:** O NIM suporta autoescalonamento no Kubernetes, permitindo lidar eficazmente com cargas de trabalho variáveis.
- **Segurança e Controle:** As organizações podem manter o controle sobre seus dados e aplicativos auto-hospedando os microserviços NIM em sua própria infraestrutura gerenciada.
- **APIs Padrão:** NIM oferece APIs padrão do setor, facilitando a criação e integração de aplicações de IA como chatbots, assistentes de IA e mais.

NIM é parte do NVIDIA AI Enterprise, que tem como objetivo simplificar a implantação e operacionalização de modelos de IA, garantindo que eles rodem de forma eficiente em GPUs NVIDIA.

- Demo: Usando NVIDIA NIM para chamar Phi-3.5-Vision-API  [[Clique neste link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Executando Phi-3/3.5 Localmente
Inferência em relação ao Phi-3, ou qualquer modelo de linguagem como o GPT-3, refere-se ao processo de gerar respostas ou previsões baseadas na entrada que recebe. Quando você fornece um prompt ou pergunta ao Phi-3, ele utiliza sua rede neural treinada para inferir a resposta mais provável e relevante, analisando padrões e relações nos dados nos quais foi treinado.

**Hugging Face Transformer**
Hugging Face Transformers é uma biblioteca poderosa projetada para processamento de linguagem natural (NLP) e outras tarefas de aprendizado de máquina. Aqui estão alguns pontos-chave sobre ela:

1. **Modelos Pré-treinados**: Ela oferece milhares de modelos pré-treinados que podem ser usados para várias tarefas, como classificação de texto, reconhecimento de entidades nomeadas, perguntas e respostas, sumarização, tradução e geração de texto.

2. **Interoperabilidade de Frameworks**: A biblioteca suporta múltiplos frameworks de aprendizado profundo, incluindo PyTorch, TensorFlow e JAX. Isso permite treinar um modelo em um framework e usá-lo em outro.

3. **Capacidades Multimodais**: Além de NLP, Hugging Face Transformers também suporta tarefas em visão computacional (ex: classificação de imagem, detecção de objetos) e processamento de áudio (ex: reconhecimento de fala, classificação de áudio).

4. **Facilidade de Uso**: A biblioteca oferece APIs e ferramentas para baixar e ajustar modelos facilmente, tornando-a acessível tanto para iniciantes quanto para especialistas.

5. **Comunidade e Recursos**: Hugging Face possui uma comunidade vibrante e extensa documentação, tutoriais e guias para ajudar os usuários a começar e aproveitar ao máximo a biblioteca.
[documentação oficial](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ou seu [repositório no GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Este é o método mais comumente usado, mas ele também requer aceleração por GPU. Afinal, cenários como Vision e MoE exigem muitos cálculos, que serão muito lentos na CPU se não forem quantizados.


- Demo: Usando Transformer para chamar Phi-3.5-Instruct [Clique neste link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Usando Transformer para chamar Phi-3.5-Vision [Clique neste link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Usando Transformer para chamar Phi-3.5-MoE [Clique neste link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) é uma plataforma projetada para facilitar a execução local de grandes modelos de linguagem (LLMs) na sua máquina. Ela suporta vários modelos como Llama 3.1, Phi 3, Mistral e Gemma 2, entre outros. A plataforma simplifica o processo ao agrupar pesos do modelo, configuração e dados em um único pacote, tornando mais acessível para os usuários customizar e criar seus próprios modelos. Ollama está disponível para macOS, Linux e Windows. É uma ótima ferramenta se você deseja experimentar ou implantar LLMs sem depender de serviços na nuvem. Ollama é o caminho mais direto, você só precisa executar o seguinte comando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) é o runtime off-line e local da Microsoft para executar modelos como Phi totalmente no seu próprio hardware - sem necessidade de assinatura Azure, chave de API ou conexão de rede. Ele seleciona automaticamente o melhor provedor de execução disponível (NPU, GPU ou CPU) e expõe um endpoint compatível com OpenAI, para que códigos existentes `openai`/Azure AI Inference SDK possam apontar para ele com mudanças mínimas. Veja a [documentação do Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para começar.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) é um acelerador de aprendizado de máquina multiplataforma para inferência e treinamento. ONNX Runtime para Generative AI (GENAI) é uma ferramenta poderosa que ajuda você a rodar modelos de IA generativa de forma eficiente em várias plataformas.

## O que é ONNX Runtime?
ONNX Runtime é um projeto open-source que possibilita inferência de alto desempenho para modelos de aprendizado de máquina. Ele suporta modelos no formato Open Neural Network Exchange (ONNX), que é um padrão para representar modelos de aprendizado de máquina. A inferência com ONNX Runtime pode viabilizar experiências mais rápidas para o cliente e custos mais baixos, suportando modelos de frameworks de deep learning como PyTorch e TensorFlow/Keras, além de bibliotecas clássicas de aprendizado de máquina como scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime é compatível com diferentes hardwares, drivers e sistemas operacionais, e oferece desempenho ideal aproveitando aceleradores de hardware quando aplicável junto a otimizações e transformações de gráfico.

## O que é IA Generativa?
IA Generativa refere-se a sistemas de IA capazes de gerar novos conteúdos, como texto, imagens ou música, baseados nos dados em que foram treinados. Exemplos incluem modelos de linguagem como GPT-3 e modelos de geração de imagem como Stable Diffusion. A biblioteca ONNX Runtime para GenAI fornece o loop de IA generativa para modelos ONNX, incluindo inferência com ONNX Runtime, processamento dos logits, busca e amostragem, e gerenciamento do cache KV.

## ONNX Runtime para GENAI
ONNX Runtime para GENAI amplia as capacidades do ONNX Runtime para suportar modelos de IA generativa. Aqui estão algumas características principais:

- **Suporte Amplo a Plataformas:** Funciona em várias plataformas, incluindo Windows, Linux, macOS, Android e iOS.
- **Suporte a Modelos:** Suporta muitos modelos populares de IA generativa, como LLaMA, GPT-Neo, BLOOM e mais.
- **Otimização de Desempenho:** Inclui otimizações para diferentes aceleradores de hardware como GPUs NVIDIA, GPUs AMD e mais2.
- **Facilidade de Uso:** Fornece APIs para fácil integração em aplicações, permitindo gerar texto, imagens e outros conteúdos com código mínimo.
- Usuários podem chamar um método generate() de alto nível, ou rodar cada iteração do modelo em loop, gerando um token por vez, e opcionalmente atualizando parâmetros de geração dentro do loop.
- ONNX Runtime também suporta busca gulosa/beam search e amostragem TopP, TopK para gerar sequências de tokens e possui processamento integrado de logits como penalidades de repetição. Você também pode facilmente adicionar pontuação customizada.

## Começando
Para começar com ONNX Runtime para GENAI, você pode seguir estes passos:

### Instale o ONNX Runtime:
```Python
pip install onnxruntime
```
### Instale as Extensões de IA Generativa:
```Python
pip install onnxruntime-genai
```

### Rode um Modelo: Aqui está um exemplo simples em Python:
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
### Demo: Usando ONNX Runtime GenAI para chamar Phi-3.5-Vision


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

Além dos métodos de referência ONNX Runtime, Ollama e Foundry Local, também podemos completar a referência de modelos quantitativos com base nos métodos de referência de modelos fornecidos por diferentes fabricantes. Como o framework Apple MLX com Apple Metal, Qualcomm QNN com NPU, Intel OpenVINO com CPU/GPU, etc. Você também pode obter mais conteúdo no [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mais

Aprendemos o básico da Família Phi-3/3.5, mas para aprender mais sobre SLM precisamos de mais conhecimento. Você pode encontrar as respostas no Phi-3 Cookbook. Se quiser saber mais, por favor visite o [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->