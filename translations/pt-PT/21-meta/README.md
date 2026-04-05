# Construir com os Modelos da Família Meta

## Introdução

Esta lição irá cobrir:

- Exploração dos dois principais modelos da família Meta - Llama 3.1 e Llama 3.2
- Compreensão dos casos de uso e cenários para cada modelo
- Exemplo de código para mostrar as características únicas de cada modelo

## A Família de Modelos Meta

Nesta lição, exploraremos 2 modelos da família Meta ou "Llama Herd" - Llama 3.1 e Llama 3.2.

Estes modelos vêm em diferentes variantes e estão disponíveis no mercado de modelos do GitHub. Aqui estão mais detalhes sobre o uso dos Modelos GitHub para [protótipos com modelos de IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Variantes do Modelo:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Nota: Llama 3 também está disponível nos Modelos GitHub, mas não será abordado nesta lição*

## Llama 3.1

Com 405 Mil Milhões de Parâmetros, o Llama 3.1 encaixa-se na categoria de LLMs de código aberto.

O modelo é uma atualização do lançamento anterior Llama 3, oferecendo:

- Janela de contexto maior - 128k tokens vs 8k tokens
- Máximo de Tokens de Saída maior - 4096 vs 2048
- Melhor Suporte Multilingue - devido ao aumento dos tokens de treino

Estas características permitem ao Llama 3.1 lidar com casos de uso mais complexos ao construir aplicações GenAI, incluindo:  
- Chamada Nativa de Funções - a capacidade de chamar ferramentas e funções externas fora do fluxo de trabalho do LLM  
- Melhor Performance em RAG - devido à maior janela de contexto  
- Geração de Dados Sintéticos - a capacidade de criar dados eficazes para tarefas como o fine-tuning  

### Chamada Nativa de Funções

O Llama 3.1 foi ajustado para ser mais eficaz ao fazer chamadas de funções ou ferramentas. Também possui duas ferramentas incorporadas que o modelo pode identificar como necessárias com base no prompt do utilizador. Essas ferramentas são:

- **Brave Search** - Pode ser usada para obter informações atualizadas como o tempo, realizando uma pesquisa na web
- **Wolfram Alpha** - Pode ser usada para cálculos matemáticos mais complexos, assim não é necessário escrever suas próprias funções.

Também pode criar as suas próprias ferramentas personalizadas que o LLM pode chamar.

No exemplo de código abaixo:

- Definimos as ferramentas disponíveis (brave_search, wolfram_alpha) no prompt do sistema.
- Enviamos um prompt do utilizador a perguntar sobre o tempo numa determinada cidade.
- O LLM responderá com uma chamada de ferramenta para o Brave Search, que ficará assim `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Nota: Este exemplo apenas realiza a chamada à ferramenta; se quiser obter os resultados, precisará de criar uma conta gratuita na página da API Brave e definir a função propriamente dita.*

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

Apesar de ser um LLM, uma limitação do Llama 3.1 é a ausência de multimodalidade. Ou seja, a incapacidade de usar diferentes tipos de entrada como imagens como prompts e fornecer respostas. Esta capacidade é uma das principais características do Llama 3.2. Estas características também incluem:

- Multimodalidade - capacidade de avaliar tanto prompts de texto como de imagem
- Variações de tamanho pequeno a médio (11B e 90B) - fornece opções flexíveis de implantação,
- Variações só de texto (1B e 3B) - permite que o modelo seja implantado em dispositivos edge/móveis e oferece baixa latência

O suporte multimodal representa um grande avanço no mundo dos modelos de código aberto. O exemplo de código abaixo utiliza tanto uma imagem como um prompt de texto para obter uma análise da imagem do Llama 3.2 90B.

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


## A aprendizagem não termina aqui, continue a viagem

Após concluir esta lição, consulte a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar os seus conhecimentos em IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->