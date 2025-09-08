<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:09:13+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "br"
}
-->
# Construindo com os Modelos da Família Meta

## Introdução

Esta lição abordará:

- Exploração dos dois principais modelos da família Meta - Llama 3.1 e Llama 3.2
- Compreensão dos casos de uso e cenários para cada modelo
- Exemplo de código para mostrar as características únicas de cada modelo

## A Família de Modelos Meta

Nesta lição, exploraremos 2 modelos da família Meta ou "Llama Herd" - Llama 3.1 e Llama 3.2

Esses modelos vêm em diferentes variantes e estão disponíveis no marketplace de Modelos do GitHub. Aqui estão mais detalhes sobre como usar os Modelos do GitHub para [prototipar com modelos de IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Variantes dos Modelos:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Nota: Llama 3 também está disponível nos Modelos do GitHub, mas não será abordado nesta lição*

## Llama 3.1

Com 405 bilhões de parâmetros, o Llama 3.1 se enquadra na categoria de LLMs open source.

O modelo é uma atualização do lançamento anterior Llama 3, oferecendo:

- Janela de contexto maior - 128k tokens contra 8k tokens  
- Máximo de tokens de saída maior - 4096 contra 2048  
- Melhor suporte multilíngue - devido ao aumento no número de tokens de treinamento  

Isso permite que o Llama 3.1 lide com casos de uso mais complexos ao construir aplicações GenAI, incluindo:  
- Chamada Nativa de Funções - a capacidade de chamar ferramentas e funções externas fora do fluxo de trabalho do LLM  
- Melhor desempenho em RAG - devido à janela de contexto maior  
- Geração de Dados Sintéticos - a capacidade de criar dados eficazes para tarefas como fine-tuning  

### Chamada Nativa de Funções

O Llama 3.1 foi ajustado para ser mais eficiente ao fazer chamadas de funções ou ferramentas. Ele também possui duas ferramentas integradas que o modelo pode identificar como necessárias com base no prompt do usuário. Essas ferramentas são:

- **Brave Search** - Pode ser usada para obter informações atualizadas, como o clima, realizando uma busca na web  
- **Wolfram Alpha** - Pode ser usada para cálculos matemáticos mais complexos, eliminando a necessidade de escrever suas próprias funções  

Você também pode criar suas próprias ferramentas personalizadas que o LLM pode chamar.

No exemplo de código abaixo:

- Definimos as ferramentas disponíveis (brave_search, wolfram_alpha) no prompt do sistema.  
- Enviamos um prompt do usuário que pergunta sobre o clima em uma determinada cidade.  
- O LLM responderá com uma chamada para a ferramenta Brave Search, que ficará assim `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Nota: Este exemplo apenas realiza a chamada da ferramenta; se quiser obter os resultados, será necessário criar uma conta gratuita na página da API do Brave e definir a função em si*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

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

Apesar de ser um LLM, uma limitação do Llama 3.1 é a multimodalidade. Ou seja, a capacidade de usar diferentes tipos de entrada, como imagens, como prompts e fornecer respostas. Essa habilidade é uma das principais características do Llama 3.2. Essas características também incluem:

- Multimodalidade - capacidade de avaliar prompts de texto e imagem  
- Variações de tamanho pequeno a médio (11B e 90B) - isso oferece opções flexíveis de implantação  
- Variações apenas de texto (1B e 3B) - permite que o modelo seja implantado em dispositivos edge / móveis e oferece baixa latência  

O suporte multimodal representa um grande avanço no mundo dos modelos open source. O exemplo de código abaixo utiliza tanto uma imagem quanto um prompt de texto para obter uma análise da imagem pelo Llama 3.2 90B.

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

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
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

Após concluir esta lição, confira nossa [coleção de Aprendizado em IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.