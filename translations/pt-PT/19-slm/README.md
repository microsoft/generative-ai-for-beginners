# Introdução aos Pequenos Modelos de Linguagem para IA Generativa para Iniciantes
A IA generativa é um campo fascinante da inteligência artificial que se concentra na criação de sistemas capazes de gerar novo conteúdo. Este conteúdo pode variar desde texto e imagens a música e até ambientes virtuais inteiros. Uma das aplicações mais empolgantes da IA generativa é no domínio dos modelos de linguagem.

## O Que São Pequenos Modelos de Linguagem?

Um Pequeno Modelo de Linguagem (SLM) representa uma variante reduzida de um grande modelo de linguagem (LLM), aproveitando muitos dos princípios arquitetónicos e técnicas dos LLMs, ao mesmo tempo que apresenta uma pegada computacional significativamente reduzida.

Os SLMs são um subconjunto de modelos de linguagem projetados para gerar texto semelhante ao humano. Ao contrário dos seus pares maiores, como o GPT-4, os SLMs são mais compactos e eficientes, tornando-os ideais para aplicações onde os recursos computacionais são limitados. Apesar do seu tamanho menor, ainda podem executar uma variedade de tarefas. Normalmente, os SLMs são construídos através da compressão ou destilação de LLMs, visando reter uma parte substancial da funcionalidade original e das capacidades linguísticas do modelo. Esta redução no tamanho do modelo diminui a complexidade geral, tornando os SLMs mais eficientes em termos tanto de uso de memória quanto de requisitos computacionais. Apesar destas otimizações, os SLMs ainda podem desempenhar uma ampla gama de tarefas de processamento de linguagem natural (NLP):

- Geração de Texto: Criar frases ou parágrafos coerentes e contextualmente relevantes.
- Completação de Texto: Prever e completar frases com base num prompt dado.
- Tradução: Converter texto de uma língua para outra.
- Resumo: Condensar textos longos em resumos mais curtos e digestíveis.

Embora com alguns compromissos em desempenho ou profundidade de compreensão comparados com os seus equivalentes maiores.

## Como Funcionam os Pequenos Modelos de Linguagem?
Os SLMs são treinados com grandes quantidades de dados textuais. Durante o treino, aprendem os padrões e estruturas da língua, permitindo-lhes gerar texto que é gramaticalmente correto e contextualmente adequado. O processo de treino envolve:

- Recolha de Dados: Acumular grandes conjuntos de dados textuais de diversas fontes.
- Pré-processamento: Limpar e organizar os dados para os tornar adequados para o treino.
- Treino: Usar algoritmos de aprendizagem automática para ensinar o modelo a compreender e gerar texto.
- Afinamento: Ajustar o modelo para melhorar o seu desempenho em tarefas específicas.

O desenvolvimento dos SLMs está alinhado com a crescente necessidade de modelos que possam ser implementados em ambientes com recursos limitados, como dispositivos móveis ou plataformas de computação de ponta, onde LLMs de escala total podem ser impraticáveis devido às suas elevadas exigências de recursos. Ao focar na eficiência, os SLMs equilibram desempenho com acessibilidade, possibilitando uma aplicação mais ampla em vários domínios.

![slm](../../../translated_images/pt-PT/slm.4058842744d0444a.webp)

## Objetivos de Aprendizagem

Nesta lição, esperamos introduzir o conhecimento sobre SLM e combiná-lo com Microsoft Phi-3 para aprender diferentes cenários em conteúdo de texto, visão e MoE.

No final desta lição, deverá ser capaz de responder às seguintes perguntas:

- O que é um SLM?
- Qual é a diferença entre SLM e LLM?
- O que é a Família Microsoft Phi-3/3.5?
- Como realizar inferência com a Família Microsoft Phi-3/3.5?

Pronto? Vamos começar.

## As Distinções entre Grandes Modelos de Linguagem (LLMs) e Pequenos Modelos de Linguagem (SLMs)

Tanto os LLMs como os SLMs baseiam-se em princípios fundamentais de aprendizagem automática probabilística, seguindo abordagens similares no seu desenho arquitetónico, metodologias de treino, processos de geração de dados e técnicas de avaliação de modelos. No entanto, vários fatores-chave diferenciam estes dois tipos de modelos.

## Aplicações dos Pequenos Modelos de Linguagem

Os SLMs têm uma vasta gama de aplicações, incluindo:

- Chatbots: Fornecimento de suporte ao cliente e interação com os utilizadores de forma conversacional.
- Criação de Conteúdo: Assistência a escritores gerando ideias ou mesmo elaborando artigos inteiros.
- Educação: Ajudar estudantes com trabalhos escritos ou na aprendizagem de novas línguas.
- Acessibilidade: Criar ferramentas para pessoas com deficiências, como sistemas de texto para fala.

**Tamanho**
  
Uma distinção primária entre LLMs e SLMs reside na escala dos modelos. LLMs, como o ChatGPT (GPT-4), podem conter cerca de 1,76 triliões de parâmetros, enquanto SLMs open-source como o Mistral 7B são projetados com um número significativamente menor de parâmetros — aproximadamente 7 mil milhões. Esta disparidade deve-se principalmente a diferenças na arquitetura do modelo e nos processos de treino. Por exemplo, o ChatGPT usa um mecanismo de autoatenção dentro de uma estrutura codificador-decodificador, enquanto o Mistral 7B utiliza atenção de janela deslizante, o que permite um treino mais eficiente num modelo apenas decodificador. Esta variação arquitetónica tem implicações profundas na complexidade e desempenho destes modelos.

**Compreensão**

Os SLMs são tipicamente otimizados para desempenho em domínios específicos, tornando-os altamente especializados, mas potencialmente limitados na sua capacidade de fornecer uma compreensão contextual ampla em múltiplos campos do conhecimento. Em contraste, os LLMs visam simular uma inteligência similar à humana num nível mais abrangente. Treinados com grandes e diversificados conjuntos de dados, os LLMs são desenhados para ter bom desempenho em diversos domínios, oferecendo maior versatilidade e adaptabilidade. Consequentemente, os LLMs são mais indicados para uma ampla gama de tarefas finais, como processamento de linguagem natural e programação.

**Computação**

O treino e implementação dos LLMs são processos que consomem muitos recursos, frequentemente requerendo infraestruturas computacionais significativas, incluindo grandes clusters de GPUs. Por exemplo, o treino de um modelo como o ChatGPT do zero pode necessitar de milhares de GPUs durante períodos prolongados. Em contraste, os SLMs, com o seu número menor de parâmetros, são mais acessíveis em termos de recursos computacionais. Modelos como o Mistral 7B podem ser treinados e executados em máquinas locais equipadas com GPUs moderadas, embora o treino ainda demande várias horas distribuídas por múltiplas GPUs.

**Viés**

O viés é um problema conhecido nos LLMs, principalmente devido à natureza dos dados de treino. Estes modelos frequentemente dependem de dados brutos disponíveis abertamente na internet, que podem sub-representar ou deturpar certos grupos, introduzir rotulagem incorreta ou refletir preconceitos linguísticos influenciados por dialetos, variações geográficas e regras gramaticais. Adicionalmente, a complexidade das arquiteturas LLM pode inadvertidamente agravar o viés, que pode passar despercebido sem um afinamento cuidadoso. Por outro lado, os SLMs, treinados em conjuntos de dados mais restritos e específicos de domínio, são inerentemente menos suscetíveis a tais preconceitos, embora não lhes sejam completamente imunes.

**Inferência**

O tamanho reduzido dos SLMs confere-lhes uma vantagem significativa em termos de velocidade de inferência, permitindo gerar saídas de forma eficiente em hardware local sem necessidade de processamento paralelo extenso. Em contraste, os LLMs, devido ao seu tamanho e complexidade, frequentemente requerem substanciais recursos computacionais paralelos para alcançar tempos aceitáveis de inferência. A presença de múltiplos utilizadores simultâneos ainda desacelera os tempos de resposta dos LLMs, especialmente quando implementados em escala.

Em resumo, apesar de ambos os LLMs e SLMs compartilharem uma base fundamental em aprendizagem automática, diferem significativamente em termos de tamanho do modelo, requisitos de recursos, compreensão contextual, suscetibilidade a viés e velocidade de inferência. Estas distinções refletem a sua adequação para diferentes casos de uso, com os LLMs sendo mais versáteis mas exigentes em recursos, e os SLMs oferecendo maior eficiência específica para domínios com menores exigências computacionais.

***Nota: Nesta lição, iremos apresentar o SLM utilizando o Microsoft Phi-3 / 3.5 como exemplo.***

## Apresentação da Família Phi-3 / Phi-3.5

A Família Phi-3 / 3.5 direciona-se principalmente a cenários de aplicação em texto, visão e Agente (MoE):

### Phi-3 / 3.5 Instruct

Principalmente para geração de texto, completamento de conversas e extração de informação de conteúdo, entre outros.

**Phi-3-mini**

O modelo de linguagem de 3.8B está disponível na Microsoft Foundry, Hugging Face e Ollama. Os modelos Phi-3 superam significativamente modelos de linguagem com tamanhos iguais ou maiores em benchmarks chave (veja os números dos benchmarks abaixo, números maiores são melhores). O Phi-3-mini supera modelos com o dobro do seu tamanho, enquanto o Phi-3-small e o Phi-3-medium superam modelos maiores, incluindo o GPT-3.5.

**Phi-3-small & medium**

Com apenas 7B parâmetros, o Phi-3-small vence o GPT-3.5T em vários benchmarks de linguagem, raciocínio, codificação e matemática.

O Phi-3-medium com 14B parâmetros continua esta tendência e supera o Gemini 1.0 Pro.

**Phi-3.5-mini**

Podemos vê-lo como uma atualização do Phi-3-mini. Embora os parâmetros permaneçam inalterados, melhora a capacidade de suportar múltiplas línguas (suporte para mais de 20 línguas: Árabe, Chinês, Checo, Dinamarquês, Holandês, Inglês, Finlandês, Francês, Alemão, Hebraico, Húngaro, Italiano, Japonês, Coreano, Norueguês, Polaco, Português, Russo, Espanhol, Sueco, Tailandês, Turco, Ucraniano) e acrescenta suporte mais forte para contextos longos.

O Phi-3.5-mini com 3.8B parâmetros supera modelos de linguagem do mesmo tamanho e está ao nível de modelos com o dobro do seu tamanho.

### Phi-3 / 3.5 Vision

Podemos considerar o modelo Instruct do Phi-3/3.5 como a capacidade do Phi de compreender, e a Visão é o que dá ao Phi "olhos" para entender o mundo.


**Phi-3-Vision**

O Phi-3-vision, com apenas 4.2B parâmetros, continua esta tendência e supera modelos maiores como Claude-3 Haiku e Gemini 1.0 Pro V em tarefas gerais de raciocínio visual, OCR e compreensão de tabelas e diagramas.


**Phi-3.5-Vision**

O Phi-3.5-Vision é também uma atualização do Phi-3-Vision, adicionando suporte para múltiplas imagens. Pode ser visto como uma melhoria na visão: não só pode ver imagens, mas também vídeos.

O Phi-3.5-vision supera modelos maiores como Claude-3.5 Sonnet e Gemini 1.5 Flash nas tarefas de OCR, compreensão de tabelas e gráficos e está ao nível em tarefas de raciocínio geral do conhecimento visual. Suporta entrada multi-frame, ou seja, realiza raciocínio sobre múltiplas imagens de entrada.


### Phi-3.5-MoE

***Mistura de Especialistas (MoE)*** permite que os modelos sejam pré-treinados com muito menos computação, o que significa que pode escalar dramaticamente o tamanho do modelo ou do conjunto de dados com o mesmo orçamento computacional que um modelo denso. Em particular, um modelo MoE deve alcançar a mesma qualidade que o seu equivalente denso muito mais rapidamente durante o pré-treinamento.

O Phi-3.5-MoE compreende 16 módulos especialistas de 3.8B. O Phi-3.5-MoE com apenas 6.6B parâmetros ativos alcança um nível semelhante de raciocínio, compreensão de linguagem e matemática comparado com modelos muito maiores.

Podemos usar o modelo da Família Phi-3/3.5 baseado em diferentes cenários. Ao contrário dos LLMs, pode implementar o Phi-3/3.5-mini ou Phi-3/3.5-Vision em dispositivos de borda.


## Como usar os modelos da Família Phi-3/3.5

Esperamos usar o Phi-3/3.5 em diferentes cenários. A seguir, usaremos o Phi-3/3.5 baseado em diferentes cenários.

![phi3](../../../translated_images/pt-PT/phi3.655208c3186ae381.webp)

### Inferência via APIs na Cloud

**Modelos da Microsoft Foundry**

> **Nota:** Os Modelos do GitHub serão descontinuados no final de julho de 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) é o substituto direto.

O catálogo de modelos Microsoft Foundry é a forma mais direta. Pode aceder rapidamente ao modelo Phi-3/3.5-Instruct através do catálogo de modelos Foundry. Em conjunto com o Azure AI Inference SDK / OpenAI SDK, pode aceder à API via código para completar a chamada do Phi-3/3.5-Instruct. Também pode testar diferentes resultados através do Playground.

- Demonstração: Comparação dos efeitos do Phi-3-mini e Phi-3.5-mini em cenários chineses

![phi3](../../../translated_images/pt-PT/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/pt-PT/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ou, se quiser usar os modelos de visão e MoE, pode utilizar o Microsoft Foundry para completar a chamada. Se estiver interessado, pode ler o Phi-3 Cookbook para aprender como chamar Phi-3/3.5 Instruct, Vision, MoE através do Microsoft Foundry [Clique neste link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Além do catálogo de modelos na cloud Microsoft Foundry, também pode utilizar o [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) para fazer chamadas relacionadas. Pode visitar o NVIDIA NIM para realizar chamadas API da Família Phi-3/3.5. O NVIDIA NIM (NVIDIA Inference Microservices) é um conjunto de microserviços acelerados de inferência concebido para ajudar desenvolvedores a implementar modelos de IA de forma eficiente em vários ambientes, incluindo clouds, centros de dados e estações de trabalho.

Aqui estão algumas características chave do NVIDIA NIM:

- **Facilidade de Implementação:** O NIM permite a implementação de modelos de IA com um único comando, tornando a integração em fluxos de trabalho existentes simples.

- **Desempenho Otimizado:** Aproveita os motores de inferência pré-otimizados da NVIDIA, como TensorRT e TensorRT-LLM, para garantir baixa latência e alto débito.
- **Escalabilidade:** O NIM suporta escalamento automático no Kubernetes, permitindo lidar com cargas de trabalho variáveis de forma eficaz.
- **Segurança e Controlo:** As organizações podem manter controlo sobre os seus dados e aplicações ao hospedar os microserviços NIM numa infraestrutura gerida própria.
- **APIs Standard:** O NIM fornece APIs padrão da indústria, facilitando a construção e integração de aplicações de IA como chatbots, assistentes de IA, entre outros.

O NIM faz parte do NVIDIA AI Enterprise, que visa simplificar a implementação e operacionalização de modelos de IA, garantindo que funcionem de forma eficiente em GPUs NVIDIA.

- Demo: Usar NVIDIA NIM para chamar Phi-3.5-Vision-API  [[Clique neste link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Executar Phi-3/3.5 Localmente
Inferência em relação ao Phi-3, ou qualquer modelo de linguagem como o GPT-3, refere-se ao processo de gerar respostas ou previsões com base na entrada que recebe. Quando fornece um prompt ou pergunta ao Phi-3, ele usa a sua rede neural treinada para inferir a resposta mais provável e relevante, analisando padrões e relações nos dados em que foi treinado.

**Hugging Face Transformer**
Hugging Face Transformers é uma biblioteca poderosa projetada para processamento de linguagem natural (NLP) e outras tarefas de machine learning. Aqui estão alguns pontos-chave sobre ela:

1. **Modelos Pré-treinados**: Fornece milhares de modelos pré-treinados que podem ser usados para várias tarefas como classificação de texto, reconhecimento de entidades nomeadas, respostas a perguntas, sumarização, tradução e geração de texto.

2. **Interoperabilidade de Frameworks**: A biblioteca suporta múltiplos frameworks de deep learning, incluindo PyTorch, TensorFlow e JAX. Isso permite treinar um modelo num framework e usá-lo noutro.

3. **Capacidades Multimodais**: Para além do NLP, Hugging Face Transformers também suporta tarefas em visão computacional (ex., classificação de imagens, deteção de objetos) e processamento de áudio (ex., reconhecimento de voz, classificação de áudio).

4. **Facilidade de Uso**: A biblioteca oferece APIs e ferramentas para descarregar e ajustar modelos facilmente, tornando-a acessível para iniciantes e especialistas.

5. **Comunidade e Recursos**: Hugging Face tem uma comunidade vibrante e documentação extensiva, tutoriais e guias para ajudar os utilizadores a começar e tirar o máximo da biblioteca.
[documentação oficial](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ou o seu [repositório GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Este é o método mais utilizado, mas também requer aceleração GPU. Afinal, cenários como Vision e MoE necessitam de muitos cálculos, que serão muito lentos em CPU se não forem quantizados.


- Demo: Usar Transformer para chamar Phi-3.5-Instruct [Clique neste link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Usar Transformer para chamar Phi-3.5-Vision [Clique neste link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Usar Transformer para chamar Phi-3.5-MoE [Clique neste link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) é uma plataforma concebida para facilitar a execução de grandes modelos de linguagem (LLMs) localmente na sua máquina. Suporta vários modelos como Llama 3.1, Phi 3, Mistral e Gemma 2, entre outros. A plataforma simplifica o processo ao agrupar pesos do modelo, configuração e dados num único pacote, tornando mais acessível para os utilizadores personalizar e criar os seus próprios modelos. Ollama está disponível para macOS, Linux e Windows. É uma ótima ferramenta caso queira experimentar ou implementar LLMs sem depender de serviços na nuvem. Ollama é o método mais direto, só precisa de executar o seguinte comando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) é o runtime offline da Microsoft para execução de modelos como Phi inteiramente no seu próprio hardware - não necessita de subscrição Azure, chave de API ou ligação de rede. Seleciona automaticamente o melhor fornecedor de execução disponível (NPU, GPU ou CPU) e expõe um endpoint compatível com OpenAI, para que o código existente do SDK `openai`/Azure AI Inference possa apontar para ele com alterações mínimas. Consulte a [documentação do Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para começar.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) é um acelerador multi-plataforma para inferência e treino de machine learning. O ONNX Runtime para Generative AI (GENAI) é uma ferramenta poderosa que ajuda a correr modelos de IA generativa de forma eficiente em diversas plataformas.

## O que é o ONNX Runtime?
O ONNX Runtime é um projeto open-source que permite inferência de alto desempenho de modelos de machine learning. Suporta modelos no formato Open Neural Network Exchange (ONNX), que é um padrão para representar modelos de machine learning. A inferência do ONNX Runtime pode proporcionar experiências de cliente mais rápidas e custos mais baixos, suportando modelos de frameworks de deep learning como PyTorch e TensorFlow/Keras, assim como bibliotecas clássicas de machine learning como scikit-learn, LightGBM, XGBoost, etc. O ONNX Runtime é compatível com diferentes hardwares, drivers e sistemas operativos, e fornece desempenho ótimo ao aproveitar aceleradores de hardware quando aplicável, juntamente com otimizações e transfornações de grafos.

## O que é IA Generativa?
IA generativa refere-se a sistemas de IA capazes de gerar conteúdo novo, como texto, imagens ou música, com base nos dados em que foram treinados. Exemplos incluem modelos de linguagem como o GPT-3 e modelos de geração de imagem como o Stable Diffusion. A biblioteca ONNX Runtime para GenAI fornece o ciclo de IA generativa para modelos ONNX, incluindo inferência com ONNX Runtime, processamento de logits, busca e amostragem, e gestão de cache KV.

## ONNX Runtime para GENAI
O ONNX Runtime para GENAI estende as capacidades do ONNX Runtime para suportar modelos de IA generativa. Aqui estão algumas características principais:

- **Suporte Abrangente a Plataformas:** Funciona em várias plataformas, incluindo Windows, Linux, macOS, Android e iOS.
- **Suporte a Modelos:** Suporta muitos modelos populares de IA generativa, como LLaMA, GPT-Neo, BLOOM e mais.
- **Otimização de Desempenho:** Inclui otimizações para diferentes aceleradores de hardware como GPUs NVIDIA, GPUs AMD, e mais2.
- **Facilidade de Uso:** Fornece APIs para integração fácil em aplicações, permitindo gerar texto, imagens e outro conteúdo com código mínimo.
- Os utilizadores podem chamar um método de alto nível generate(), ou executar cada iteração do modelo num ciclo, gerando um token de cada vez, e opcionalmente atualizar parâmetros de geração dentro do ciclo.
- O runtime ONNX também suporta pesquisa gulosa/de feixe e amostragem TopP, TopK para gerar sequências de tokens e processamento interno de logits como penalizações de repetição. Também pode adicionar facilmente pontuações personalizadas.

## Começar
Para começar com o ONNX Runtime para GENAI, pode seguir estes passos:

### Instale o ONNX Runtime:
```Python
pip install onnxruntime
```
### Instale as Extensões de IA Generativa:
```Python
pip install onnxruntime-genai
```

### Execute um Modelo: Aqui está um exemplo simples em Python:
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
### Demo: Usar ONNX Runtime GenAI para chamar Phi-3.5-Vision


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

Para além dos métodos de referência ONNX Runtime, Ollama e Foundry Local, também podemos completar a referência de modelos quantitativos baseando-nos nos métodos de referência de modelo fornecidos por diferentes fabricantes. Como o framework Apple MLX com Apple Metal, Qualcomm QNN com NPU, Intel OpenVINO com CPU/GPU, etc. Pode ainda obter mais conteúdo no [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mais

Aprendemos os conceitos básicos da Família Phi-3/3.5, mas para aprender mais sobre SLM precisamos de mais conhecimento. Pode encontrar as respostas no Phi-3 Cookbook. Se quiser saber mais, visite o [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->