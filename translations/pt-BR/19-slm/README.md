# Introdução a Modelos de Linguagem Pequenos para IA Generativa para Iniciantes
A IA generativa é um campo fascinante da inteligência artificial que se concentra em criar sistemas capazes de gerar novos conteúdos. Esse conteúdo pode variar desde texto e imagens até música e até ambientes virtuais inteiros. Uma das aplicações mais empolgantes da IA generativa está no campo dos modelos de linguagem.

## O Que São Modelos de Linguagem Pequenos?

Um Modelo de Linguagem Pequeno (SLM) representa uma variante reduzida de um grande modelo de linguagem (LLM), aproveitando muitos dos princípios arquitetônicos e técnicas dos LLMs, enquanto exibe uma pegada computacional significativamente reduzida.

SLMs são um subconjunto de modelos de linguagem projetados para gerar texto semelhante ao humano. Ao contrário de seus equivalentes maiores, como o GPT-4, os SLMs são mais compactos e eficientes, tornando-os ideais para aplicações onde os recursos computacionais são limitados. Apesar de seu tamanho menor, eles ainda podem realizar uma variedade de tarefas. Tipicamente, os SLMs são construídos comprimindo ou destilando os LLMs, visando reter uma parte substancial da funcionalidade e das capacidades linguísticas do modelo original. Essa redução no tamanho do modelo diminui a complexidade geral, tornando os SLMs mais eficientes tanto em termos de uso de memória quanto de requisitos computacionais. Apesar dessas otimizações, os SLMs ainda podem realizar uma ampla gama de tarefas de processamento de linguagem natural (PLN):

- Geração de Texto: Criar sentenças ou parágrafos coerentes e contextualmente relevantes.
- Completação de Texto: Prever e completar sentenças com base em um prompt dado.
- Tradução: Converter texto de uma língua para outra.
- Resumo: Condensar textos longos em resumos mais curtos e digestíveis.

Embora com alguns compromissos de desempenho ou profundidade de entendimento comparados aos seus equivalentes maiores.

## Como Funcionam os Modelos de Linguagem Pequenos?
Os SLMs são treinados com grandes quantidades de dados textuais. Durante o treinamento, aprendem os padrões e estruturas da linguagem, permitindo-lhes gerar textos que sejam gramaticalmente corretos e contextualmente apropriados. O processo de treinamento envolve:

- Coleta de Dados: Reunir grandes conjuntos de dados textuais de várias fontes.
- Pré-processamento: Limpar e organizar os dados para torná-los adequados ao treinamento.
- Treinamento: Utilizar algoritmos de aprendizado de máquina para ensinar o modelo a entender e gerar texto.
- Ajuste fino: Ajustar o modelo para melhorar seu desempenho em tarefas específicas.

O desenvolvimento de SLMs está alinhado à crescente necessidade de modelos que possam ser implantados em ambientes com recursos limitados, como dispositivos móveis ou plataformas de computação na borda, onde os LLMs em escala total podem ser impraticáveis devido a suas altas demandas de recursos. Focando na eficiência, os SLMs equilibram desempenho com acessibilidade, permitindo uma aplicação mais ampla em vários domínios.

![slm](../../../translated_images/pt-BR/slm.4058842744d0444a.webp)

## Objetivos de Aprendizagem

Nesta lição, esperamos introduzir o conhecimento sobre SLM e combiná-lo com o Microsoft Phi-3 para aprender diferentes cenários em conteúdo de texto, visão e MoE.

Ao final desta lição, você deverá ser capaz de responder às seguintes perguntas:

- O que é um SLM?
- Qual a diferença entre SLM e LLM?
- O que é a Família Microsoft Phi-3/3.5?
- Como executar inferência com a Família Microsoft Phi-3/3.5?

Pronto? Vamos começar.

## As Diferenças entre Grandes Modelos de Linguagem (LLMs) e Modelos de Linguagem Pequenos (SLMs)

Tanto os LLMs quanto os SLMs são construídos com base em princípios fundamentais de aprendizado de máquina probabilístico, seguindo abordagens semelhantes em seu design arquitetônico, metodologias de treinamento, processos de geração de dados e técnicas de avaliação de modelos. No entanto, vários fatores-chave diferenciam esses dois tipos de modelos.

## Aplicações dos Modelos de Linguagem Pequenos

Os SLMs têm uma ampla gama de aplicações, incluindo:

- Chatbots: Fornecer suporte ao cliente e interagir com usuários de forma conversacional.
- Criação de Conteúdo: Ajudar escritores a gerar ideias ou até redigir artigos inteiros.
- Educação: Auxiliar estudantes com tarefas de escrita ou no aprendizado de novos idiomas.
- Acessibilidade: Criar ferramentas para pessoas com deficiência, como sistemas de texto para fala.

**Tamanho**
  
Uma distinção primordial entre LLMs e SLMs está na escala dos modelos. LLMs, como o ChatGPT (GPT-4), podem conter cerca de 1,76 trilhão de parâmetros, enquanto os SLMs de código aberto, como o Mistral 7B, são projetados com significativamente menos parâmetros — aproximadamente 7 bilhões. Essa disparidade ocorre principalmente devido a diferenças na arquitetura do modelo e nos processos de treinamento. Por exemplo, o ChatGPT emprega um mecanismo de autoatenção dentro de uma arquitetura de codificador-decodificador, enquanto o Mistral 7B usa atenção em janela deslizante, o que permite um treinamento mais eficiente dentro de um modelo somente decodificador. Essa variação arquitetônica tem implicações profundas na complexidade e desempenho desses modelos.

**Compreensão**

Os SLMs geralmente são otimizados para desempenho em domínios específicos, tornando-os altamente especializados, mas potencialmente limitados em sua capacidade de oferecer compreensão contextual ampla em múltiplos campos do conhecimento. Em contraste, os LLMs visam simular uma inteligência semelhante à humana em um nível mais abrangente. Treinados com grandes e diversos conjuntos de dados, os LLMs são projetados para ter bom desempenho em uma variedade de domínios, oferecendo maior versatilidade e adaptabilidade. Consequentemente, os LLMs são mais adequados para uma ampla gama de tarefas subsequentes, como processamento de linguagem natural e programação.

**Computação**

O treinamento e a implantação dos LLMs são processos que demandam muitos recursos, frequentemente requerendo infraestrutura computacional significativa, incluindo grandes clusters de GPUs. Por exemplo, treinar um modelo como o ChatGPT do zero pode necessitar de milhares de GPUs por períodos prolongados. Em contraste, os SLMs, com suas contagens menores de parâmetros, são mais acessíveis em termos de recursos computacionais. Modelos como o Mistral 7B podem ser treinados e executados em máquinas locais equipadas com capacidades moderadas de GPU, embora o treinamento ainda demande várias horas em múltiplas GPUs.

**Viés**

O viés é um problema conhecido nos LLMs, principalmente devido à natureza dos dados de treinamento. Esses modelos frequentemente dependem de dados crus disponíveis abertamente na internet, que podem sub-representar ou deturpar certos grupos, introduzir rotulagens incorretas ou refletir viéses linguísticos influenciados por dialetos, variações geográficas e regras gramaticais. Além disso, a complexidade da arquitetura dos LLMs pode inadvertidamente exacerbar o viés, o qual pode passar despercebido sem um ajuste fino cuidadoso. Por outro lado, os SLMs, treinados em conjuntos de dados mais restritos e específicos de domínio, são inerentemente menos suscetíveis a tais viéses, embora não sejam imunes a eles.

**Inferência**

O tamanho reduzido dos SLMs lhes confere uma vantagem significativa em termos de velocidade de inferência, permitindo gerar saídas de forma eficiente em hardware local sem necessidade de processamento paralelo extensivo. Em contraste, os LLMs, devido ao seu tamanho e complexidade, frequentemente requerem recursos computacionais paralelos substanciais para alcançar tempos de inferência aceitáveis. A presença de múltiplos usuários concorrentes ainda diminui os tempos de resposta dos LLMs, especialmente quando implantados em larga escala.

Em resumo, embora tanto os LLMs quanto os SLMs compartilhem uma base fundamental em aprendizado de máquina, eles diferem significativamente em termos de tamanho do modelo, requisitos de recursos, compreensão contextual, suscetibilidade a viés e velocidade de inferência. Essas distinções refletem sua adequação para diferentes casos de uso, onde os LLMs são mais versáteis, porém exigentes em recursos, enquanto os SLMs oferecem maior eficiência específica para domínio com demandas computacionais reduzidas.

***Nota: Nesta lição, apresentaremos SLM usando Microsoft Phi-3 / 3.5 como exemplo.***

## Apresentando a Família Phi-3 / Phi-3.5

A Família Phi-3 / 3.5 visa principalmente cenários de aplicação em texto, visão e Agente (MoE):

### Phi-3 / 3.5 Instruct

Voltado principalmente para geração de texto, completamento de chat e extração de informações de conteúdo, etc.

**Phi-3-mini**

O modelo de linguagem 3.8B está disponível no Microsoft Foundry, Hugging Face e Ollama. Os modelos Phi-3 superam significativamente modelos de linguagem de tamanhos iguais e maiores em benchmarks-chave (veja os números dos benchmarks abaixo, números maiores são melhores). O Phi-3-mini supera modelos com o dobro de seu tamanho, enquanto o Phi-3-small e Phi-3-medium superam modelos maiores, incluindo o GPT-3.5.

**Phi-3-small & medium**

Com apenas 7B parâmetros, o Phi-3-small supera o GPT-3.5T em uma variedade de benchmarks de linguagem, raciocínio, codificação e matemática.

O Phi-3-medium com 14B parâmetros continua essa tendência e supera o Gemini 1.0 Pro.

**Phi-3.5-mini**

Podemos considerá-lo como uma atualização do Phi-3-mini. Embora os parâmetros permaneçam inalterados, melhora a capacidade de suportar múltiplos idiomas (suporte a 20+ idiomas: Árabe, Chinês, Tcheco, Dinamarquês, Holandês, Inglês, Finlandês, Francês, Alemão, Hebraico, Húngaro, Italiano, Japonês, Coreano, Norueguês, Polonês, Português, Russo, Espanhol, Sueco, Tailandês, Turco, Ucraniano) e adiciona suporte mais robusto para contexto longo.

O Phi-3.5-mini com 3.8B parâmetros supera modelos de linguagem do mesmo tamanho e está no mesmo nível que modelos com o dobro do tamanho.

### Phi-3 / 3.5 Vision

Podemos pensar no modelo Instruct do Phi-3/3.5 como a capacidade do Phi de entender, e a Visão é o que dá a Phi olhos para compreender o mundo.


**Phi-3-Vision**

O Phi-3-vision, com apenas 4.2B parâmetros, continua essa tendência e supera modelos maiores como Claude-3 Haiku e Gemini 1.0 Pro V em tarefas gerais de raciocínio visual, OCR, e compreensão de tabelas e diagramas.


**Phi-3.5-Vision**

O Phi-3.5-Vision também é uma atualização do Phi-3-Vision, adicionando suporte para múltiplas imagens. Você pode considerá-lo uma melhoria na visão, agora pode ver não apenas imagens, mas também vídeos.

O Phi-3.5-vision supera modelos maiores como Claude-3.5 Sonnet e Gemini 1.5 Flash em tarefas de OCR, compreensão de tabelas e gráficos, e está no mesmo nível em tarefas gerais de raciocínio visual. Suporta entrada de múltiplos quadros, ou seja, realiza raciocínio em múltiplas imagens de entrada.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** permite que modelos sejam pré-treinados com muito menos computação, o que significa que você pode ampliar dramaticamente o tamanho do modelo ou do conjunto de dados com o mesmo orçamento computacional que um modelo denso. Em particular, um modelo MoE deve atingir a mesma qualidade que seu equivalente denso muito mais rápido durante o pré-treinamento.

O Phi-3.5-MoE compreende 16 módulos especialistas de 3.8B cada. O Phi-3.5-MoE com apenas 6.6B parâmetros ativos alcança um nível similar de raciocínio, compreensão de linguagem e matemática que modelos muito maiores.

Podemos usar o modelo da Família Phi-3/3.5 com base em diferentes cenários. Ao contrário dos LLMs, você pode implantar o Phi-3/3.5-mini ou Phi-3/3.5-Vision em dispositivos de borda.


## Como usar os modelos da Família Phi-3/3.5

Esperamos usar o Phi-3/3.5 em diferentes cenários. A seguir, usaremos o Phi-3/3.5 baseado em diferentes cenários.

![phi3](../../../translated_images/pt-BR/phi3.655208c3186ae381.webp)

### Inferência via APIs de Nuvem

**Modelos Microsoft Foundry**

> **Nota:** GitHub Models será descontinuado no final de julho de 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) é o substituto direto.

O Microsoft Foundry Models é a forma mais direta. Você pode acessar rapidamente o modelo Phi-3/3.5-Instruct através do catálogo de modelos Foundry. Combinado com o Azure AI Inference SDK / OpenAI SDK, você pode acessar a API via código para realizar chamadas Phi-3/3.5-Instruct. Também pode testar diferentes efeitos através do Playground.

- Demonstração: Comparação dos efeitos do Phi-3-mini e Phi-3.5-mini em cenários chineses

![phi3](../../../translated_images/pt-BR/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/pt-BR/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ou, se quisermos usar os modelos de visão e MoE, podemos usar o Microsoft Foundry para realizar a chamada. Se estiver interessado, você pode ler o Phi-3 Cookbook para aprender como chamar Phi-3/3.5 Instruct, Vision, MoE pelo Microsoft Foundry [Clique neste link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Além do catálogo Microsoft Foundry Models baseado em nuvem, também é possível usar o [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) para realizar chamadas relacionadas. Você pode visitar o NVIDIA NIM para concluir as chamadas API da Família Phi-3/3.5. O NVIDIA NIM (NVIDIA Inference Microservices) é um conjunto de microserviços de inferência acelerada projetados para ajudar desenvolvedores a implantar modelos de IA de forma eficiente em vários ambientes, incluindo nuvens, data centers e estações de trabalho.

Aqui estão algumas características chave do NVIDIA NIM:

- **Facilidade de Implantação:** O NIM permite o deploy de modelos de IA com um único comando, tornando a integração em fluxos de trabalho existentes simples.

- **Desempenho Otimizado:** Ele aproveita os motores de inferência pré-otimizados da NVIDIA, como TensorRT e TensorRT-LLM, para garantir baixa latência e alta taxa de transferência.
- **Escalabilidade:** NIM suporta autoscaling no Kubernetes, permitindo lidar de forma eficaz com cargas de trabalho variáveis.
- **Segurança e Controle:** Organizações podem manter o controle sobre seus dados e aplicativos hospedando os microsserviços NIM em sua própria infraestrutura gerenciada.
- **APIs Padrão:** NIM fornece APIs padrão da indústria, tornando fácil construir e integrar aplicações de IA como chatbots, assistentes de IA e mais.

NIM faz parte da NVIDIA AI Enterprise, que visa simplificar a implantação e operacionalização de modelos de IA, garantindo que eles sejam executados eficientemente nas GPUs da NVIDIA.

- Demonstração: Usando NVIDIA NIM para chamar Phi-3.5-Vision-API [[Clique neste link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Executando Phi-3/3.5 Localmente
Inferência em relação ao Phi-3, ou qualquer modelo de linguagem como GPT-3, refere-se ao processo de gerar respostas ou previsões com base na entrada recebida. Quando você fornece um prompt ou pergunta ao Phi-3, ele usa sua rede neural treinada para inferir a resposta mais provável e relevante analisando padrões e relacionamentos nos dados com os quais foi treinado.

**Hugging Face Transformer**
Hugging Face Transformers é uma biblioteca poderosa projetada para processamento de linguagem natural (PLN) e outras tarefas de aprendizado de máquina. Aqui estão alguns pontos-chave sobre ela:

1. **Modelos Pré-treinados**: Oferece milhares de modelos pré-treinados que podem ser usados para várias tarefas, como classificação de texto, reconhecimento de entidades nomeadas, resposta a perguntas, sumarização, tradução e geração de texto.

2. **Interoperabilidade entre Frameworks**: A biblioteca suporta múltiplos frameworks de aprendizado profundo, incluindo PyTorch, TensorFlow e JAX. Isso permite treinar um modelo em um framework e usá-lo em outro.

3. **Capacidades Multimodais**: Além de PLN, Hugging Face Transformers também suporta tarefas em visão computacional (por exemplo, classificação de imagens, detecção de objetos) e processamento de áudio (por exemplo, reconhecimento de fala, classificação de áudio).

4. **Facilidade de Uso**: A biblioteca oferece APIs e ferramentas para baixar e ajustar modelos facilmente, tornando-a acessível para iniciantes e especialistas.

5. **Comunidade e Recursos**: Hugging Face possui uma comunidade vibrante e extensa documentação, tutoriais e guias para ajudar os usuários a começar e aproveitar ao máximo a biblioteca.
[documentação oficial](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ou seu [repositório GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Este é o método mais comumente usado, mas também requer aceleração por GPU. Afinal, cenários como Vision e MoE exigem muitos cálculos, que serão muito lentos na CPU se não estiverem quantizados.


- Demonstração: Usando Transformer para chamar Phi-3.5-Instruct [Clique neste link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstração: Usando Transformer para chamar Phi-3.5-Vision [Clique neste link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstração: Usando Transformer para chamar Phi-3.5-MoE [Clique neste link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) é uma plataforma projetada para facilitar a execução de grandes modelos de linguagem (LLMs) localmente na sua máquina. Ela suporta vários modelos como Llama 3.1, Phi 3, Mistral e Gemma 2, entre outros. A plataforma simplifica o processo ao agrupar pesos do modelo, configuração e dados em um único pacote, tornando-o mais acessível para os usuários personalizarem e criarem seus próprios modelos. Ollama está disponível para macOS, Linux e Windows. É uma ótima ferramenta se você quer experimentar ou implantar LLMs sem depender de serviços em nuvem. Ollama é a maneira mais direta, você só precisa executar o seguinte comando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) é o ambiente de execução offline e local da Microsoft para rodar modelos como Phi inteiramente no seu próprio hardware - sem necessidade de assinatura Azure, chave de API ou conexão de rede. Ele seleciona automaticamente o melhor provedor de execução disponível (NPU, GPU ou CPU) e expõe um endpoint compatível com OpenAI, para que códigos existentes do SDK de Inferência `openai`/Azure AI possam apontar para ele com mudanças mínimas. Veja a [documentação do Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para começar.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) é um acelerador de inferência e treinamento de aprendizado de máquina multiplataforma. ONNX Runtime para Inteligência Artificial Generativa (GENAI) é uma ferramenta poderosa que ajuda a executar modelos de IA generativa de forma eficiente em várias plataformas.

## O que é ONNX Runtime?
ONNX Runtime é um projeto de código aberto que permite inferência de alto desempenho de modelos de aprendizado de máquina. Ele suporta modelos no formato Open Neural Network Exchange (ONNX), que é um padrão para representar modelos de aprendizado de máquina. A inferência do ONNX Runtime pode habilitar experiências de cliente mais rápidas e custos menores, suportando modelos de frameworks de deep learning como PyTorch e TensorFlow/Keras, bem como bibliotecas clássicas de aprendizado de máquina como scikit-learn, LightGBM, XGBoost, etc. O ONNX Runtime é compatível com diferentes hardwares, drivers e sistemas operacionais, e oferece desempenho ideal aproveitando aceleradores de hardware quando aplicável juntamente com otimizações e transformações de grafo.

## O que é Inteligência Artificial Generativa?
Inteligência Artificial Generativa refere-se a sistemas de IA que podem gerar novo conteúdo, como texto, imagens ou música, com base nos dados com que foram treinados. Exemplos incluem modelos de linguagem como GPT-3 e modelos de geração de imagens como Stable Diffusion. A biblioteca ONNX Runtime para GenAI fornece o ciclo de IA generativa para modelos ONNX, incluindo inferência com ONNX Runtime, processamento de logits, busca e amostragem, e gerenciamento de cache KV.

## ONNX Runtime para GENAI
ONNX Runtime para GENAI amplia as capacidades do ONNX Runtime para suportar modelos de IA generativa. Aqui estão algumas características principais:

- **Suporte Amplo para Plataformas:** Funciona em várias plataformas, incluindo Windows, Linux, macOS, Android e iOS.
- **Suporte a Modelos:** Suporta muitos modelos populares de IA generativa, como LLaMA, GPT-Neo, BLOOM e mais.
- **Otimização de Desempenho:** Inclui otimizações para diferentes aceleradores de hardware como GPUs NVIDIA, GPUs AMD e outros2.
- **Facilidade de Uso:** Fornece APIs para integração fácil em aplicativos, permitindo gerar texto, imagens e outros conteúdos com código mínimo.
- Usuários podem chamar um método generate() de alto nível, ou executar cada iteração do modelo em um loop, gerando um token por vez, e opcionalmente atualizando parâmetros de geração dentro do loop.
- O runtime ONNX também suporta busca gananciosa/beam search e amostragem TopP, TopK para gerar sequências de tokens e processamento interno de logits, como penalidades por repetição. Você também pode facilmente adicionar pontuação personalizada.

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
### Demonstração: Usando ONNX Runtime GenAI para chamar Phi-3.5-Vision


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

Além dos métodos de referência ONNX Runtime, Ollama e Foundry Local, também podemos completar a referência de modelos quantitativos baseados nos métodos de referência fornecidos por diferentes fabricantes. Como o framework Apple MLX com Apple Metal, Qualcomm QNN com NPU, Intel OpenVINO com CPU/GPU, etc. Você também pode obter mais conteúdo no [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mais

Aprendemos o básico da Família Phi-3/3.5, mas para aprender mais sobre SLM precisamos de mais conhecimento. Você pode encontrar as respostas no Phi-3 Cookbook. Se quiser aprender mais, por favor visite o [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->