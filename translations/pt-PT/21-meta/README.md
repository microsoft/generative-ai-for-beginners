# Construir com os Modelos da Família Meta 

## Introdução 

Esta lição irá cobrir: 

- Explorar os dois principais modelos da família Meta - Llama 3.1 e Llama 3.2 
- Compreender os casos de uso e cenários para cada modelo 
- Exemplo de código para mostrar as características únicas de cada modelo 


## A Família de Modelos Meta 

Nesta lição, vamos explorar 2 modelos da família Meta ou "Llama Herd" - Llama 3.1 e Llama 3.2.

Estes modelos vêm em diferentes variantes e estão disponíveis no [catálogo Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Nota:** O GitHub Models será descontinuado no final de julho de 2026. Aqui estão mais detalhes sobre como usar [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) para prototipar com modelos de IA.

Variantes de Modelo: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Nota: Llama 3 também está disponível no Microsoft Foundry Models mas não será abordado nesta lição*

## Llama 3.1 

Com 405 Mil Milhões de Parâmetros, Llama 3.1 enquadra-se na categoria de LLM de código aberto. 

O modelo é uma atualização da versão anterior Llama 3, oferecendo: 

- Janela de contexto maior - 128k tokens vs 8k tokens 
- Máximo de tokens de saída maior - 4096 vs 2048 
- Melhor suporte multilíngue - devido ao aumento dos tokens de treino 

Estes permitem que o Llama 3.1 lide com casos de uso mais complexos ao construir aplicações GenAI incluindo: 
- Chamada nativa de funções - a capacidade de chamar ferramentas externas e funções fora do fluxo de trabalho do LLM
- Melhor desempenho RAG - devido à maior janela de contexto 
- Geração de dados sintéticos - a capacidade de criar dados eficazes para tarefas como fine-tuning 

### Chamada Nativa de Funções 

O Llama 3.1 foi ajustado para ser mais eficaz em fazer chamadas de funções ou ferramentas. Também tem duas ferramentas integradas que o modelo pode identificar como necessárias para usar com base no prompt do utilizador. Essas ferramentas são: 

- **Brave Search** - Pode ser usado para obter informações atualizadas como o tempo ao realizar uma pesquisa na web 
- **Wolfram Alpha** - Pode ser usado para cálculos matemáticos mais complexos, pelo que não é necessário escrever as tuas próprias funções. 

Também podes criar as tuas próprias ferramentas personalizadas que o LLM pode chamar. 

No exemplo de código abaixo: 

- Definimos as ferramentas disponíveis (brave_search, wolfram_alpha) no prompt do sistema. 
- Enviamos um prompt de utilizador que pergunta sobre o tempo numa determinada cidade. 
- O LLM responderá com uma chamada de ferramenta para a ferramenta Brave Search que terá esta aparência `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Nota: Este exemplo apenas faz a chamada à ferramenta, se quiseres obter os resultados, precisarás de criar uma conta gratuita na página da API Brave e definir a função ela mesma.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Obtenha-os a partir da página "Visão Geral" do seu projeto Microsoft Foundry
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

Apesar de ser um LLM, uma limitação do Llama 3.1 é a sua falta de multimodalidade. Ou seja, a incapacidade de usar diferentes tipos de entrada como imagens como prompts e fornecer respostas. Esta capacidade é uma das principais características do Llama 3.2. Estas características incluem também: 

- Multimodalidade - capacidade de avaliar prompts tanto de texto como de imagem 
- Variações de tamanho pequeno a médio (11B e 90B) - isto proporciona opções flexíveis de implantação, 
- Variações apenas de texto (1B e 3B) - permite que o modelo seja implantado em dispositivos móveis / edge e oferece baixa latência 

O suporte multimodal representa um grande passo no mundo dos modelos open source. O exemplo de código abaixo utiliza tanto uma imagem como um prompt de texto para obter uma análise da imagem do Llama 3.2 90B. 


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

# Obtenha estes da página "Visão geral" do seu projeto Microsoft Foundry
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

## A aprendizagem não termina aqui, continua a jornada

Após completar esta lição, explora a nossa [coleção de Aprendizagem em IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuares a evoluir no teu conhecimento em IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->