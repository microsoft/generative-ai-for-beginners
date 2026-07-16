# Construindo com os Modelos da Família Meta 

## Introdução 

Esta lição cobrirá: 

- Explorando os dois principais modelos da família Meta - Llama 3.1 e Llama 3.2 
- Entendendo os casos de uso e cenários para cada modelo 
- Exemplo de código para mostrar os recursos exclusivos de cada modelo 


## A Família de Modelos Meta 

Nesta lição, exploraremos 2 modelos da família Meta ou "Rebanho Llama" - Llama 3.1 e Llama 3.2.

Esses modelos vêm em diferentes variantes e estão disponíveis no [catálogo de Modelos Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Nota:** O GitHub Models será descontinuado no final de julho de 2026. Aqui estão mais detalhes sobre como usar os [Modelos Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) para prototipar com modelos de IA.

Variantes do Modelo: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Nota: Llama 3 também está disponível nos Modelos Microsoft Foundry, mas não será abordado nesta lição*

## Llama 3.1 

Com 405 bilhões de parâmetros, Llama 3.1 se enquadra na categoria LLM de código aberto. 

O modelo é uma atualização da versão anterior Llama 3, oferecendo: 

- Janela de contexto maior - 128k tokens vs 8k tokens 
- Máximo de tokens de saída maior - 4096 vs 2048 
- Melhor suporte multilíngue - devido ao aumento nos tokens de treinamento 

Isso permite que o Llama 3.1 lide com casos de uso mais complexos ao construir aplicações GenAI, incluindo: 
- Chamadas nativas de funções - a capacidade de chamar ferramentas e funções externas fora do fluxo de trabalho do LLM
- Melhor desempenho RAG - devido à janela de contexto maior 
- Geração de dados sintéticos - a capacidade de criar dados eficazes para tarefas como fine-tuning 

### Chamadas nativas de funções 

O Llama 3.1 foi ajustado para ser mais eficaz em fazer chamadas de função ou ferramenta. Ele também possui duas ferramentas embutidas que o modelo pode identificar como necessárias para uso com base na solicitação do usuário. Essas ferramentas são: 

- **Brave Search** - Pode ser usada para obter informações atualizadas, como o clima, realizando uma busca na web 
- **Wolfram Alpha** - Pode ser usado para cálculos matemáticos mais complexos, então não é necessário escrever suas próprias funções. 

Você também pode criar suas próprias ferramentas personalizadas que o LLM pode chamar. 

No exemplo de código abaixo: 

- Definimos as ferramentas disponíveis (brave_search, wolfram_alpha) no prompt do sistema. 
- Enviamos um prompt do usuário perguntando sobre o tempo em uma certa cidade. 
- O LLM responderá com uma chamada de ferramenta para o Brave Search, que se parecerá com `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Nota: Este exemplo apenas realiza a chamada da ferramenta, se quiser obter os resultados, será necessário criar uma conta gratuita na página da API do Brave e definir a função em si.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Obtenha estes da página "Visão geral" do seu projeto Microsoft Foundry
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2 

Apesar de ser um LLM, uma limitação do Llama 3.1 é sua falta de multimodalidade. Isto é, a incapacidade de usar diferentes tipos de entrada, como imagens, como prompts e fornecer respostas. Essa habilidade é uma das principais características do Llama 3.2. Essas características também incluem: 

- Multimodalidade - tem a capacidade de avaliar tanto prompts de texto quanto de imagem 
- Variações de tamanho pequeno a médio (11B e 90B) - isso proporciona opções flexíveis de implantação, 
- Variações somente texto (1B e 3B) - isso permite que o modelo seja implantado em dispositivos edge / móveis e proporciona baixa latência 

O suporte multimodal representa um grande avanço no mundo dos modelos de código aberto. O exemplo de código abaixo recebe tanto uma imagem quanto um prompt de texto para obter uma análise da imagem pelo Llama 3.2 90B. 


### Suporte Multimodal com Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

# Obtenha estes da página "Visão Geral" do seu projeto Microsoft Foundry
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## O aprendizado não para aqui, continue a jornada

Após concluir esta lição, confira nossa [coleção de Aprendizado de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->