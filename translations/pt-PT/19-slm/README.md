# Introdução aos Pequenos Modelos de Linguagem para IA Generativa para Iniciantes
A IA generativa é um campo fascinante da inteligência artificial que se concentra na criação de sistemas capazes de gerar novo conteúdo. Este conteúdo pode variar desde texto e imagens até música e até ambientes virtuais completos. Uma das aplicações mais empolgantes da IA generativa está no domínio dos modelos de linguagem.

## O que São Pequenos Modelos de Linguagem?

Um Pequeno Modelo de Linguagem (SLM) representa uma variante reduzida de um grande modelo de linguagem (LLM), aproveitando muitos dos princípios arquitetónicos e técnicas dos LLMs, ao mesmo tempo que apresenta uma pegada computacional significativamente reduzida. 

Os SLMs são um subconjunto de modelos de linguagem projetados para gerar texto semelhante ao humano. Ao contrário dos seus equivalentes maiores, como o GPT-4, os SLMs são mais compactos e eficientes, tornando-os ideais para aplicações onde os recursos computacionais são limitados. Apesar do seu tamanho menor, podem ainda realizar uma variedade de tarefas. Tipicamente, os SLMs são construídos através da compressão ou destilação de LLMs, com o objetivo de reter uma parte substancial da funcionalidade original e das capacidades linguísticas do modelo. Esta redução no tamanho do modelo diminui a complexidade geral, tornando os SLMs mais eficientes tanto em termos de uso da memória como dos requisitos computacionais. Apesar destas otimizações, os SLMs podem ainda desempenhar uma ampla gama de tarefas de processamento de linguagem natural (NLP):

- Geração de Texto: Criar frases ou parágrafos coerentes e contextualmente relevantes.
- Completação de Texto: Prever e completar frases com base num prompt dado.
- Tradução: Converter texto de uma língua para outra.
- Resumo: Condensar textos longos em resumos mais curtos e digestivos.

Embora com alguns compromissos em desempenho ou profundidade de entendimento em comparação com os seus equivalentes maiores.

## Como Funcionam os Pequenos Modelos de Linguagem?
Os SLMs são treinados numa vasta quantidade de dados textuais. Durante o treino, aprendem os padrões e estruturas da linguagem, permitindo-lhes gerar texto que seja gramaticalmente correto e contextualmente apropriado. O processo de treino envolve:

- Coleta de Dados: Recolher grandes conjuntos de dados textuais de várias fontes.
- Pré-processamento: Limpar e organizar os dados para torná-los adequados ao treino.
- Treino: Usar algoritmos de aprendizagem automática para ensinar o modelo a compreender e gerar texto.
- Ajuste Fino: Ajustar o modelo para melhorar o desempenho em tarefas específicas.

O desenvolvimento dos SLMs alinha-se com a crescente necessidade de modelos que possam ser implementados em ambientes com recursos limitados, como dispositivos móveis ou plataformas de computação na borda, onde os LLMs de grande escala podem ser impraticáveis devido à sua elevada exigência de recursos. Ao focar-se na eficiência, os SLMs equilibram desempenho com acessibilidade, permitindo uma aplicação mais ampla em diversos domínios.

![slm](../../../translated_images/pt-PT/slm.4058842744d0444a.webp)

## Objetivos de Aprendizagem

Nesta lição, esperamos introduzir o conhecimento sobre SLM e combiná-lo com o Microsoft Phi-3 para aprender diferentes cenários em conteúdo textual, visão e MoE.

No final desta lição, deverá ser capaz de responder às seguintes perguntas:

- O que é um SLM?
- Qual a diferença entre SLM e LLM?
- O que é a família Microsoft Phi-3/3.5?
- Como executar inferência com a família Microsoft Phi-3/3.5?

Pronto? Vamos começar.

## As Diferenças entre Grandes Modelos de Linguagem (LLMs) e Pequenos Modelos de Linguagem (SLMs)

Tanto os LLMs como os SLMs são construídos sobre princípios fundamentais da aprendizagem automática probabilística, seguindo abordagens semelhantes no seu design arquitetónico, metodologias de treino, processos de geração de dados e técnicas de avaliação de modelos. No entanto, vários fatores chave diferenciam estes dois tipos de modelos.

## Aplicações dos Pequenos Modelos de Linguagem

Os SLMs têm uma vasta gama de aplicações, incluindo:

- Chatbots: Fornecimento de suporte ao cliente e interação com utilizadores de forma conversacional.
- Criação de Conteúdo: Ajudar escritores a gerar ideias ou mesmo redigir artigos completos.
- Educação: Ajudar estudantes em trabalhos escritos ou na aprendizagem de novas línguas.
- Acessibilidade: Criar ferramentas para pessoas com deficiência, como sistemas de texto para voz.

**Tamanho**
  
Uma distinção principal entre LLMs e SLMs reside na escala dos modelos. Os LLMs, como o ChatGPT (GPT-4), podem conter aproximadamente 1.76 triliões de parâmetros, enquanto os SLMs open-source como o Mistral 7B são projetados com significativamente menos parâmetros — aproximadamente 7 mil milhões. Esta disparidade deve-se principalmente às diferenças na arquitetura do modelo e nos processos de treino. Por exemplo, o ChatGPT emprega um mecanismo de autoatenção dentro de um framework encoder-decoder, enquanto o Mistral 7B usa atenção em janela deslizante, o que permite um treino mais eficiente num modelo apenas decoder. Esta variação arquitetónica tem implicações profundas na complexidade e desempenho destes modelos.

**Compreensão**

Os SLMs são tipicamente otimizados para desempenho em domínios específicos, tornando-os altamente especializados mas potencialmente limitados na sua capacidade de proporcionar uma compreensão contextual ampla em múltiplos campos de conhecimento. Em contraste, os LLMs procuram simular uma inteligência semelhante à humana de forma mais abrangente. Treinados em conjuntos de dados vastos e diversificados, os LLMs são concebidos para ter bom desempenho em vários domínios, oferecendo maior versatilidade e adaptabilidade. Consequentemente, os LLMs são mais adequados para uma ampla gama de tarefas downstream, como processamento de linguagem natural e programação.

**Computação**

O treino e a implementação dos LLMs são processos intensivos em recursos, frequentemente a exigir infraestruturas computacionais significativas, incluindo clusters de GPUs de grande escala. Por exemplo, treinar um modelo como o ChatGPT do zero pode necessitar de milhares de GPUs ao longo de períodos prolongados. Em contraste, os SLMs, com os seus números menores de parâmetros, são mais acessíveis em termos de recursos computacionais. Modelos como o Mistral 7B podem ser treinados e executados em máquinas locais equipadas com GPUs moderadas, embora o treino ainda demande várias horas em múltiplas GPUs.

**Viés**

O viés é uma questão conhecida nos LLMs, principalmente devido à natureza dos dados de treino. Estes modelos frequentemente dependem de dados brutos e disponíveis abertamente na internet, que podem sub-representar ou deturpar certos grupos, introduzir rotulagem errada ou refletir vieses linguísticos influenciados por dialetos, variações geográficas e regras gramaticais. Adicionalmente, a complexidade das arquiteturas dos LLMs pode inadvertidamente exacerbar o viés, o qual pode passar despercebido sem um ajuste fino cuidadoso. Por outro lado, os SLMs, sendo treinados em conjuntos de dados mais restritos e específicos a domínios, são inerentemente menos suscetíveis a esses vieses, embora não sejam imunes aos mesmos.

**Inferência**

O tamanho reduzido dos SLMs oferece uma vantagem significativa em termos de velocidade de inferência, permitindo-lhes gerar resultados eficientemente em hardware local sem necessidade de processamento paralelo extenso. Em contraste, os LLMs, devido ao seu tamanho e complexidade, frequentemente requerem recursos computacionais paralelos substanciais para atingir tempos de inferência aceitáveis. A presença de múltiplos utilizadores concorrentes também retarda os tempos de resposta dos LLMs, especialmente quando implementados em larga escala.

Em resumo, embora tanto os LLMs como os SLMs partilhem uma base fundamental em aprendizagem automática, diferem significativamente em termos de tamanho do modelo, requisitos de recursos, compreensão contextual, suscetibilidade ao viés e velocidade de inferência. Estas distinções refletem a sua adequação respeitante para diferentes casos de uso, sendo os LLMs mais versáteis mas exigentes em recursos, e os SLMs oferecendo maior eficiência específica a domínios com menores exigências computacionais.

***Nota: Nesta lição, iremos introduzir o SLM usando o Microsoft Phi-3 / 3.5 como exemplo.***

## Introdução à Família Phi-3 / Phi-3.5

A família Phi-3 / 3.5 foca-se principalmente em cenários de aplicação de texto, visão e agente (MoE):

### Phi-3 / 3.5 Instruct

Principalmente para geração de texto, completamento de chat e extração de informação de conteúdo, entre outros.

**Phi-3-mini**

O modelo de linguagem de 3.8B está disponível no Microsoft Foundry, Hugging Face e Ollama. Os modelos Phi-3 superam significativamente os modelos de linguagem de igual e maior tamanho em benchmarks chave (ver números dos benchmarks abaixo, números maiores são melhores). O Phi-3-mini supera modelos com o dobro do seu tamanho, enquanto o Phi-3-small e Phi-3-medium superam modelos maiores, incluindo o GPT-3.5.

**Phi-3-small e medium**

Com apenas 7B parâmetros, o Phi-3-small supera o GPT-3.5T numa variedade de benchmarks de linguagem, raciocínio, codificação e matemática.

O Phi-3-medium com 14B parâmetros continua esta tendência e supera o Gemini 1.0 Pro.

**Phi-3.5-mini**

Podemos considerá-lo uma atualização do Phi-3-mini. Embora os parâmetros permaneçam inalterados, melhora a capacidade de suportar múltiplas línguas (suporta mais de 20 línguas: Árabe, Chinês, Checo, Dinamarquês, Holandês, Inglês, Finlandês, Francês, Alemão, Hebraico, Húngaro, Italiano, Japonês, Coreano, Norueguês, Polaco, Português, Russo, Espanhol, Sueco, Tailandês, Turco, Ucraniano) e adiciona suporte mais forte para contextos longos.

O Phi-3.5-mini com 3.8B parâmetros supera modelos de linguagem do mesmo tamanho e está ao nível de modelos com o dobro do seu tamanho.

### Phi-3 / 3.5 Vision

Podemos pensar no modelo Instruct do Phi-3/3.5 como a capacidade do Phi para compreender, e a Visão é o que dá ao Phi olhos para entender o mundo.


**Phi-3-Vision**

O Phi-3-vision, com apenas 4.2B parâmetros, continua esta tendência e supera modelos maiores como Claude-3 Haiku e Gemini 1.0 Pro V em tarefas gerais de raciocínio visual, OCR e compreensão de tabelas e diagramas.


**Phi-3.5-Vision**

O Phi-3.5-Vision é também uma atualização do Phi-3-Vision, adicionando suporte para múltiplas imagens. Pode ser visto como uma melhoria em visão, onde não só pode ver imagens, mas também vídeos.

O Phi-3.5-vision supera modelos maiores como Claude-3.5 Sonnet e Gemini 1.5 Flash em tarefas de OCR, compreensão de tabelas e gráficos, estando igualado em tarefas gerais de raciocínio visual. Suporta entrada multi-frame, ou seja, raciocina sobre múltiplas imagens de entrada.


### Phi-3.5-MoE

***Mistura de Peritos (MoE)*** permite que os modelos sejam pré-treinados com muito menos cálculo, o que significa que pode escalar dramaticamente o tamanho do modelo ou do conjunto de dados com o mesmo orçamento computacional que um modelo denso. Em particular, um modelo MoE deve atingir a mesma qualidade que o seu equivalente denso muito mais rapidamente durante o pré-treinamento.

O Phi-3.5-MoE compreende 16 módulos especialistas de 3.8B. O Phi-3.5-MoE com apenas 6.6B parâmetros ativos alcança um nível semelhante de raciocínio, compreensão de linguagem e matemática como modelos muito maiores.

Podemos usar o modelo da família Phi-3/3.5 em diferentes cenários. Ao contrário dos LLM, pode implementar o Phi-3/3.5-mini ou Phi-3/3.5-Vision em dispositivos edge.


## Como usar os modelos da família Phi-3/3.5

Esperamos usar o Phi-3/3.5 em diferentes cenários. Seguidamente, iremos usar o Phi-3/3.5 dependendo do cenário.

![phi3](../../../translated_images/pt-PT/phi3.655208c3186ae381.webp)

### Inferência via APIs Cloud

**Modelos Microsoft Foundry**

> **Nota:** O GitHub Models será descontinuado no final de julho de 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) é o substituto direto.

O Microsoft Foundry Models é a forma mais direta. Pode aceder rapidamente ao modelo Phi-3/3.5-Instruct através do catálogo de modelos Foundry. Combinado com o SDK Azure AI Inference / OpenAI SDK, pode aceder à API por código para realizar chamadas ao Phi-3/3.5-Instruct. Também pode testar diferentes efeitos através do Playground.

- Demonstração: Comparação dos efeitos do Phi-3-mini e Phi-3.5-mini em cenários em chinês

![phi3](../../../translated_images/pt-PT/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/pt-PT/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ou se quiser usar os modelos de visão e MoE, pode utilizar o Microsoft Foundry para completar a chamada. Se estiver interessado, pode ler o Phi-3 Cookbook para aprender a chamar Phi-3/3.5 Instruct, Vision, MoE através do Microsoft Foundry [Clique neste link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Para além do catálogo de modelos Microsoft Foundry baseado na cloud, pode também usar o [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) para realizar chamadas relacionadas. Pode visitar o NVIDIA NIM para completar as chamadas API da família Phi-3/3.5. O NVIDIA NIM (NVIDIA Inference Microservices) é um conjunto de microserviços de inferência acelerada projetados para ajudar os desenvolvedores a implementar modelos de IA eficientemente em vários ambientes, incluindo clouds, data centers e estações de trabalho.

Aqui estão algumas características-chave do NVIDIA NIM:

- **Facilidade de Implementação:** O NIM permite a implementação de modelos de IA com um único comando, facilitando a integração em fluxos de trabalho existentes.

- **Desempenho Otimizado:** Aproveita os motores de inferência pré-otimizados da NVIDIA, como TensorRT e TensorRT-LLM, para garantir baixa latência e alto rendimento.
- **Escalabilidade:** O NIM suporta auto-escalamento no Kubernetes, permitindo lidar eficazmente com cargas de trabalho variadas.
- **Segurança e Controlo:** As organizações podem manter o controlo sobre os seus dados e aplicações ao alojar elas próprias os microserviços NIM na sua infraestrutura gerida.
- **APIs padrão:** O NIM fornece APIs padrão da indústria, facilitando a criação e integração de aplicações de IA como chatbots, assistentes de IA, e mais.

O NIM faz parte do NVIDIA AI Enterprise, que visa simplificar a implementação e operacionalização de modelos de IA, garantindo que funcionem eficientemente em GPUs NVIDIA.

- Demonstração: Utilizando o NVIDIA NIM para chamar a Phi-3.5-Vision-API  [[Clique neste link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Executar Phi-3/3.5 Localmente
Inferência em relação à Phi-3, ou qualquer modelo de linguagem como o GPT-3, refere-se ao processo de geração de respostas ou previsões com base no input que recebe. Quando fornece um prompt ou pergunta à Phi-3, esta usa a sua rede neuronal treinada para inferir a resposta mais provável e relevante ao analisar padrões e relações nos dados em que foi treinada.

**Hugging Face Transformer**
Hugging Face Transformers é uma biblioteca poderosa concebida para processamento de linguagem natural (PLN) e outras tarefas de aprendizagem automática. Aqui estão alguns pontos-chave sobre ela:

1. **Modelos Pré-treinados**: Disponibiliza milhares de modelos pré-treinados que podem ser usados para várias tarefas, como classificação de texto, reconhecimento de entidade nomeada, resposta a perguntas, sumarização, tradução e geração de texto.

2. **Interoperabilidade de Frameworks**: A biblioteca suporta múltiplos frameworks de deep learning, incluindo PyTorch, TensorFlow e JAX. Isso permite que treine um modelo num framework e o use noutro.

3. **Capacidades Multimodais**: Além do PLN, o Hugging Face Transformers suporta também tarefas em visão computacional (por exemplo, classificação de imagens, deteção de objetos) e processamento de áudio (por exemplo, reconhecimento de voz, classificação de áudio).

4. **Facilidade de Uso**: A biblioteca oferece APIs e ferramentas para descarregar e afinar modelos facilmente, tornando-a acessível tanto para iniciantes quanto para especialistas.

5. **Comunidade e Recursos**: Hugging Face tem uma comunidade vibrante e documentação extensa, tutoriais e guias para ajudar os utilizadores a começar e tirar o máximo partido da biblioteca.
[documentação oficial](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ou o seu [repositório GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Este é o método mais utilizado, mas também requer aceleração por GPU. Afinal, cenários como Vision e MoE requerem muitos cálculos, o que será muito lento em CPU se não forem quantificados.


- Demonstração: Utilizando Transformer para chamar Phi-3.5-Instruct [Clique neste link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstração: Utilizando Transformer para chamar Phi-3.5-Vision [Clique neste link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstração: Utilizando Transformer para chamar Phi-3.5-MoE [Clique neste link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) é uma plataforma desenhada para facilitar a execução de modelos de linguagem grandes (LLMs) localmente na sua máquina. Suporta vários modelos como Llama 3.1, Phi 3, Mistral e Gemma 2, entre outros. A plataforma simplifica o processo ao empacotar pesos do modelo, configuração e dados num único pacote, tornando mais acessível para os utilizadores personalizar e criar os seus próprios modelos. Ollama está disponível para macOS, Linux e Windows. É uma ótima ferramenta se pretende experimentar ou implantar LLMs sem depender de serviços cloud. Ollama é o modo mais direto, só precisa de executar o seguinte comando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) é o runtime offline e local da Microsoft para executar modelos como Phi inteiramente no seu próprio hardware - não requer subscrição Azure, chave API, ou ligação à rede. Seleciona automaticamente o melhor fornecedor de execução disponível (NPU, GPU ou CPU) e expõe um endpoint compatível com OpenAI, para que o código existente com `openai`/Azure AI Inference SDK possa usá-lo com alterações mínimas. Veja a [documentação do Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para começar.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) é um acelerador multiplataforma para inferência e treino de machine learning. ONNX Runtime para Inteligência Artificial Generativa (GENAI) é uma ferramenta poderosa que ajuda a executar modelos generativos de IA de forma eficiente em várias plataformas.

## O que é ONNX Runtime?
ONNX Runtime é um projeto open-source que permite inferência de alta performance de modelos de machine learning. Suporta modelos no formato Open Neural Network Exchange (ONNX), que é um padrão para representar modelos de machine learning. A inferência ONNX Runtime pode permitir experiências mais rápidas para os clientes e custos mais baixos, suportando modelos de frameworks de deep learning como PyTorch e TensorFlow/Keras, bem como bibliotecas clássicas de machine learning como scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime é compatível com diferentes hardwares, drivers e sistemas operativos, e fornece desempenho ótimo tirando partido de aceleradores de hardware quando aplicável, juntamente com otimizações e transformações de grafos.

## O que é Inteligência Artificial Generativa?
A Inteligência Artificial Generativa refere-se a sistemas de IA que podem gerar novo conteúdo, como texto, imagens ou música, com base nos dados em que foram treinados. Exemplos incluem modelos de linguagem como GPT-3 e modelos de geração de imagem como Stable Diffusion. A biblioteca ONNX Runtime para GenAI disponibiliza o ciclo generativo para modelos ONNX, incluindo inferência com ONNX Runtime, processamento de logits, busca e amostragem, e gestão do cache KV.

## ONNX Runtime para GENAI
ONNX Runtime para GENAI estende as capacidades do ONNX Runtime para suportar modelos de IA generativa. Aqui estão algumas funcionalidades principais:

- **Suporte Amplo de Plataformas:** Funciona em várias plataformas, incluindo Windows, Linux, macOS, Android e iOS.
- **Suporte a Modelos:** Suporta muitos modelos populares de IA generativa, como LLaMA, GPT-Neo, BLOOM, e mais.
- **Otimização de Performance:** Inclui otimizações para diferentes aceleradores de hardware como GPUs NVIDIA, GPUs AMD, e mais2.
- **Facilidade de Uso:** Fornece APIs para integração fácil em aplicações, permitindo gerar texto, imagens, e outros conteúdos com código mínimo.
- Os utilizadores podem chamar um método de topo generate(), ou executar cada iteração do modelo num ciclo, gerando um token de cada vez, atualizando opcionalmente os parâmetros de geração dentro do ciclo.
- O ONNX Runtime também suporta busca gulosa/beam e amostragem TopP, TopK para gerar sequências de tokens e processamento embutido de logits como penalizações de repetição. Também pode adicionar pontuações personalizadas facilmente.

## Começar
Para começar a usar ONNX Runtime para GENAI, pode seguir estes passos:

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

Para além dos métodos de referência ONNX Runtime, Ollama, e Foundry Local, podemos também completar a referência de modelos quantificados baseados nos métodos de referência fornecidos por diferentes fabricantes. Como o framework Apple MLX com Apple Metal, Qualcomm QNN com NPU, Intel OpenVINO com CPU/GPU, etc. Pode também obter mais conteúdo a partir do [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Mais

Aprendemos o básico da Família Phi-3/3.5, mas para aprender mais sobre SLM precisamos de mais conhecimento. Pode encontrar as respostas no Phi-3 Cookbook. Se quiser saber mais, visite o [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->