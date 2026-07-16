# ಮೆಟಾ ಕುಟುಂಬ ಮಾದರಿಗಳೊಂದಿಗೆ ನಿರ್ಮಾಣ 

## ಪರಿಚಯ 

ಈ ಪಾಠದಲ್ಲಿ ಕವರ್ ಮಾಡಲಾಗುವುದು: 

- ಎರಡು ಪ್ರಮುಖ ಮೆಟಾ ಕುಟುಂಬ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸಲಾಗುವುದು - ಲ್ಲಾಮಾ 3.1 ಮತ್ತು ಲ್ಲಾಮಾ 3.2 
- ಪ್ರತಿಯೊಂದು ಮಾದರಿಗೆ ಬಳಕೆಯ ಸಂದರ್ಭಗಳು ಮತ್ತು ದೃಶ್ಯಗಳ ಅರಿವು 
- ಪ್ರತಿಯೊಂದು ಮಾದರಿಯ ವಿಶಿಷ್ಟ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ತೋರಿಸಲು ಕೋಡ್ ಉದಾಹರಣೆ 


## ಮೆಟಾ ಕುಟುಂಬದ ಮಾದರಿಗಳು 

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು ಮೆಟಾ ಕುಟುಂಬದಿಂದ ಅಥವಾ "ಲ್ಲಾಮಾ ಹರ್ಡ್" - ಲ್ಲಾಮಾ 3.1 ಮತ್ತು ಲ್ಲಾಮಾ 3.2 ಎಂಬ 2 ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸುತ್ತೇವೆ.

ಈ ಮಾದರಿಗಳು ವಿಭಿನ್ನ ಪ್ರಕಾರಗಳಲ್ಲಿ ಬರುತ್ತವೆ ಮತ್ತು [Microsoft Foundry Models ಕ್ಯಾಟಲಾಗ್](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ನಲ್ಲಿ ಲಭ್ಯವಿವೆ.

> **ಟಿಪ್ಪಣಿ:** GitHub Models ಜುಲೈ 2026 ಕೊನೆಯಲ್ಲಿ ನಿವೃತ್ತಿಯಾಗುತ್ತಿದೆ. [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ನ್ನು AI ಮಾದರಿಗಳೊಂದಿಗೆ ಪ್ರೋಟೋಟೈಪ್ ಮಾಡಲು ಬಳಸುವ ಬಗ್ಗೆ ಹೆಚ್ಚುವರಿ ವಿವರಗಳು ಇಲ್ಲಿವೆ.

ಮಾದರಿಗೆ ವಿಭಿನ್ನ ಪ್ರಕಾರಗಳು: 
- ಲ್ಲಾಮಾ 3.1 - 70B ಸೂಚನೆ 
- ಲ್ಲಾಮಾ 3.1 - 405B ಸೂಚನೆ 
- ಲ್ಲಾಮಾ 3.2 - 11B ದೃಷ್ಟಿ ಸೂಚನೆ 
- ಲ್ಲಾಮಾ 3.2 - 90B ದೃಷ್ಟಿ ಸೂಚನೆ 

*ಟಿಪ್ಪಣಿ: ಲ್ಲಾಮಾ 3 ಕೂಡ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಮಾದರಿಗಳಲ್ಲಿ ಲಭ್ಯವಿದೆ ಆದರೆ ಈ ಪಾಠದಲ್ಲಿ ಆ ಕುರಿತು ಚರ್ಚಿಸುವುದಿಲ್ಲ*

## ಲ್ಲಾಮಾ 3.1 

405 ಬಿಲಿಯನ್ ಪ್ಯಾರಾಮೀಟರ್ ಗಳುಳ್ಳ ಲ್ಲಾಮಾ 3.1 ಓಪನ್ ಸೋರ್ಸ್ LLM श्रೇಣಿಗೆ ಸೇರಿದೆ. 

ಈ ಮಾದರಿ ಮೊದಲಿನ ಬಿಡುಗಡೆಯಾದ ಲ್ಲಾಮಾ 3 ನ್ನು upgrಹಾದುದಾಗಿದೆ: 

- ಹೆಚ್ಚು context ವಿಂಡೊ - 128k ಟೋಕನ್ಗಳು ವಿರುದ್ಧ 8k ಟೋಕನ್ಗಳು 
- ಹೆಚ್ಚಿದ ಗರಿಷ್ಠ output ಟೋಕನ್ಗಳು - 4096 ವಿರುದ್ಧ 2048 
- ಉತ್ತಮ ಬಹುಭಾಷಾ ಬೆಂಬಲ - ತರಬೇತಿ ಟೋಕನ್ಗಳ ಹೆಚ್ಚಳದಿಂದ 

ಈವುಗಳು ಲ್ಲಾಮಾ 3.1 ಅನ್ನು GenAI ಅಪ್ಲಿಕೇಶನ್‌ಗಳ ನಿರ್ಮಾಣದಲ್ಲಿ ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಬಳಕೆ ಪ್ರಕರಣಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಸಿದ್ಧಪಡಿಸುತ್ತವೆ: 
- ನೆಟಿವ್ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ - LLM ಕಾರ್ಯಪದ್ಧತಿಯ ಹೊರಗಿನ ಹೊರಗಿನ ಸಾಧನಗಳು ಮತ್ತು ಕಾರ್ಯಗಳನ್ನು ಕರೆಸುವ ಸಾಮರ್ಥ್ಯ 
- ಉತ್ತಮ RAG ಕಾರ್ಯಕ್ಷಮತೆ - ಹೆಚ್ಚಿದ context ವಿಂಡೊವಿನಿಂದ 
- ಬೆಲೆಕ್ರಮದ ಅನುಕರಣೆ ಉತ್ಪಾದನೆ - ಸೂಕ್ಷ್ಮFine Tune ಗಾಗಿ ಪರಿಣಾಮಕಾರಿಯಾದ ಡೇಟಾ ಸೃಷ್ಟಿಸುವ ಸಾಮರ್ಥ್ಯ 

### ನೆಟಿವ್ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ 

ಲ್ಲಾಮಾ 3.1 ಅನ್ನು ಕಾರ್ಯವಿಧಾನ ಅಥವಾ ಸಾಧನ ಕರೆಯನ್ನು ಮಾಡಲು ಹೆಚ್ಚು ಪರಿಣಾಮಕಾರಿಯಾಗಿ ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡಲಾಗಿದೆ. ಇದು ಎರಡು ಒಳಗಿನ ಸಾಧನಗಳನ್ನು ಕೂಡ ಹೊಂದಿದ್ದು, istifadəೃಕರält prompt ಆಧಾರಿತವಾಗಿ ಈ ಸಾಧನಗಳ ಬಳಕೆ ಅಗತ್ಯವಿದೆ ಎಂದು ಮಾದರಿ ಗುರುತಿಸಬಹುದು. ಈ ಸಾಧನಗಳು: 

- **Brave Search** - ವೆಬ್ ಶೋಧನೆ ನಡೆಸಿ ಹವಾಮಾನಂತಹ ನವೀನ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯಲು ಬಳಸಬಹುದು 
- **Wolfram Alpha** - ಸ್ವತಃ ಕಾರ್ಯಗಳನ್ನು ಬರೆಯದೇ, ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಗಣಿತೀಯ ಲೆಕ್ಕಾಚಾರಗಳಿಗಾಗಿ ಬಳಸಬಹುದು. 

ನೀವು ಸ್ವಂತ ಕಸ್ಟಮ್ ಸಾಧನಗಳನ್ನು ಕೂಡ ರಚಿಸಬಹುದು, LLM ಅವುಗಳನ್ನು ಕರೆತರಬಹುದು. 

ಕೆಳಗಿನ ಕೋಡ್ ಉದಾಹರಣೆಯಲ್ಲಿ: 

- ನಾವು ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು (brave_search, wolfram_alpha) ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ವ್ಯಾಖ್ಯಾನಿಸುತ್ತೇವೆ. 
- ನಿರ್ದಿಷ್ಟ ನಗರದಲ್ಲಿ ಹವಾಮಾನ ವಿಚಾರಿಸುವ user prompt ಕಳುಹಿಸುತ್ತೇವೆ. 
- LLM Brave Search ಸಾಧನಕ್ಕೆ ಕಾಲ್ ನೀಡುತ್ತದೆ, ಇದು ಈ ರೀತಿ ಕಾಣುತ್ತದೆ `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*ಟಿಪ್ಪಣಿ: ಈ ಉದಾಹರಣೆ ಕೇವಲ ಸಾಧನಕ್ಕೆ ಕಾಲ್ ನೀಡುತ್ತದೆ, ಫಲಿತಾಂಶಗಳನ್ನು ಪಡೆಯಲು Brave API ಪುಟದಲ್ಲಿ ಉಚಿತ ಖಾತೆಯನ್ನು ರಚಿಸಿ ಮತ್ತು ಕಾರ್ಯವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಬೇಕಾಗುತ್ತದೆ.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# ನಿಮ್ಮ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಯೋಜನೆಯ "ಸಮುಚ್ಚಯ" ಪುಟದಿಂದ ಈಗಳನ್ನು ಪಡೆಯಿ
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

## ಲ್ಲಾಮಾ 3.2 

LLM ಆಗಿದ್ದರೂ, ಲ್ಲಾಮಾ 3.1 ಯೊಂದಿಷ್ಟು ಸಡಿಲತೆಗಳು ಒಂದಾಗಿದೆ ಬಹು ಮಾದರಿತ್ವದಿಲ್ಲದಿರಲು. ಅಂದರೆ, ಚಿತ್ರಗಳನ್ನು ಪ್ರಾಂಪ್ಟ್‌ಗಳಾಗಿ ಬಳಸುವುದಕ್ಕೆ ಮತ್ತು ಉತ್ತರ ನೀಡುವುದಕ್ಕೆ ಸಾಧ್ಯವಿಲ್ಲ. ಈ ಸಾಮರ್ಥ್ಯವು ಲ್ಲಾಮಾ 3.2 ಯ ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳಲ್ಲಿ ಒಂದಾಗಿದೆ. ಇವುಗಳಲ್ಲಿ ಚಾಲನೆಯಲ್ಲಿರುತ್ತಾರೆ: 

- ಬಹುಮಾನದೃಷ್ಟಿ - ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಎರಡನ್ನೂ ಮೌಲ್ಯಮಾಪನ ಮಾಡಲು ಸಾಮರ್ಥ್ಯ 
- ಸಣ್ಣ ಮತ್ತು ಮಧ್ಯಮ ಗಾತ್ರದ ವಿಭಿನ್ನ ಮಾದರಿಗಳು (11B ಮತ್ತು 90B) - ಇದು ಲವಚಿಕ ನಿಯೋಜನೆ ಆಯ್ಕೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ, 
- ಪಠ್ಯ ಮಾತ್ರ ಮಾದರಿಗಳು (1B ಮತ್ತು 3B) - ಇವು ಮಾದರಿಯನ್ನು ಎಡ್ಜ್ / ಮೊಬೈಲ್ ಸಾಧನಗಳಲ್ಲಿ ನಿಯೋಜಿಸಲು ಮತ್ತು ಕಡಿಮೆ ವಿಳಂಬವನ್ನು ಒದಗಿಸುತ್ತದೆ 

ಈ ಬಹುವಿಧ ಬೆಂಬಲವು ಓಪನ್ ಸೋರ್ಸ್ ಮಾದರಿಗಳ ಪ್ರಪಂಚದಲ್ಲಿ ದೊಡ್ಡ ಹೆಜ್ಜೆಯಾಗಿದ್ದು, ಕೆಳಗಿನ ಕೋಡ್ ಉದಾಹರಣೆ ಚಿತ್ರ ಮತ್ತು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್ ಎರಡನ್ನೂ ತೆಗೆದು ಲ್ಲಾಮಾ 3.2 90B ನಿಂದ ಚಿತ್ರ ವಿಶ್ಲೇಷಣೆ ಪಡೆಯುತ್ತದೆ. 


### ಲ್ಲಾಮಾ 3.2 ನೊಂದಿಗೆ ಬಹುವಿಧ ಬೆಂಬಲ

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

# ನಿಮ್ಮ Microsoft Foundry ಪ್ರಾಜೆಕ್ಟ್‌ನ "ಸಾರಾಂಶ" ಪುಟದಿಂದ ಇದನ್ನು ಪಡೆದುಕೊಳ್ಳಿ
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

## ಕಲಿಕೆ ಇಲ್ಲಿ ಇಳಿಯೋದಿಲ್ಲ, ಪ್ರಯಾಣವನ್ನು ಮುಂದುವರಿಸಿ

ಈ ಪಾಠ ಪೂರ್ಣಗೊಂಡ ನಂತರ, ನಮ್ಮ [ಸೃಜನಾತ್ಮಕ AI ಕಲಿಕೆ ಸಂಗ್ರಹ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ನೋಡಿ ನಿಮ್ಮ ಸೃಜನಾತ್ಮಕ AI ಜ್ಞಾನವನ್ನು ಮತ್ತಷ್ಟು ಹೆಚ್ಚಿಸಿ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->