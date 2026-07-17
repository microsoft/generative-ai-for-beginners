# ಮೇಟಾ ಕುಟುಂಬ ಮಾದರಿಗಳೊಂದಿಗೆ ನಿರ್ಮಾಣ 

## ಪರಿಚಯ 

ಈ ಪಾಠದಲ್ಲಿ ಒಳಗೊಂಡಿರುತ್ತದೆ: 

- ಎರಡು ಮುಖ್ಯ ಮೇಟಾ ಕುಟುಂಬ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು - ಲಾಮಾ 3.1 ಮತ್ತು ಲಾಮಾ 3.2 
- ಪ್ರತಿ ಮಾದರಿಯ ಬಳಕೆ-ಪ್ರಕರಣಗಳು ಮತ್ತು ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು 
- ಪ್ರತಿ ಮಾದರಿಯ ವಿಶಿಷ್ಟ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ತೋರಿಸುವ ಕೋಡ್ ಉದಾಹರಣೆ 


## ಮೇಟಾ ಕುಟುಂಬದ ಮಾದರಿಗಳು 

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು ಮೇಟಾ ಕುಟುಂಬ ಅಥವಾ "ಲಾಮಾ ಹೆರ್ಡ್" ನಿಂದ 2 ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸೋಣ - ಲಾಮಾ 3.1 ಮತ್ತು ಲಾಮಾ 3.2.

ಈ ಮಾದರಿಗಳು ವಿಭಿನ್ನ ಬೇರಿಯಂಟ್‌ಗಳಲ್ಲಿ ಲಭ್ಯವಿದ್ದು [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ನಲ್ಲಿ ದೊರೆಯುತ್ತವೆ.

> **ಗಮನಿಸಿ:** GitHub Models ಜುಲೈ 2026ರೆಗೂ ನಿವೃತ್ತಿ ಹೊಂದಲಿದೆ. AI ಮಾದರಿಗಳೊಂದಿಗೆ ಪ್ರೋಟೋಟೈಪಿಂಗ್ ಮಾಡಲು [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ಬಳಕೆಯ ಕುರಿತು ಹೆಚ್ಚಿನ ವಿವರಗಳು ಇಲ್ಲಿವೆ.

ಮಾದರಿ ಬೇರಿಯಂಟ್‌ಗಳು: 
- ಲಾಮಾ 3.1 - 70B ಸೂಚನೆ 
- ಲಾಮಾ 3.1 - 405B ಸೂಚನೆ 
- ಲಾಮಾ 3.2 - 11B ದೃಶ್ಯ ಸೂಚನೆ 
- ಲಾಮಾ 3.2 - 90B ದೃಶ್ಯ ಸೂಚನೆ 

*ಗಮನಿಸಿ: ಲಾಮಾ 3 ಕೂಡ Microsoft Foundry Models ನಲ್ಲಿ ಲಭ್ಯವಿದೆ ಆದರೆ ಈ ಪಾಠದಲ್ಲಿ ಒಳಗೊಂಡಿಲ್ಲ*

## ಲಾಮಾ 3.1 

405 ಬಿಲ್ಲಿಯನ್ ಪ್ಯಾರಾಮಿಟರ್‌ಗಳೊಂದಿಗೆ, ಲಾಮಾ 3.1 ತೆರೆಯಾರಂಭದ LLM ವರ್ಗಕ್ಕೆ ಸೇರಿದೆ. 

ಈ ಮಾದರಿ ಪೂರ್ವ ಪ್ರಸಾರವಾದ ಲಾಮಾ 3ಗೆ ಹಾಳು ಮಾಡಲಾಗಿದೆ: 

- ದೊಡ್ಡದಾದ ಸಾಂದರ್ಭಿಕ ಕಿಟಕಿ - 128k ಟೋಕನ್ಗಳು ವಿರುದ್ಧ 8k ಟೋಕನ್ಗಳು 
- ಹೆಚ್ಚಿನ ಗರಿಷ್ಠ_OUTPUT_ ಟೋಕನ್ಗಳು - 4096 ವಿರುದ್ಧ 2048 
- ಉತ್ತಮ ಬಹುಭಾಷಾ ಬೆಂಬಲ - ತರಬೆತಿಯ ಟೋಕನ್ಗಳ വർಧನೆಯಿಂದ 

ಈವುಗಳು ಲಾಮಾ 3.1ಗೆ ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಬಳಕೆ ಪ್ರಕರಣಗಳನ್ನು ವಹಿಸುವಿಕೆಗೆ ಸಾಧ್ಯಮಾಡುತ್ತವೆ, ಸೇರಿಸಿ: 
- ನೇಟಿವ್ ಫಂಕ್ಷನ್ ಕರೆ - LLM ಕಾರ್ಯಪಟ್ಲದಿಂದ ಹೊರಗಿನ ಹಾರ್ಡ್‌ವೇರ್ ಮತ್ತು ಕಾರ್ಯಗಳನ್ನು ಕರೆ ಮಾಡಲು ಸಾಧ್ಯತೆ 
- ಉತ್ತಮ RAG ಪ್ರದರ್ಶನ - ಹೆಚ್ಚಿನ ಸಾಂದರ್ಭಿಕ ಕಿಟಕಿಯ ಕಾರಣದಿಂದ 
- ಕಲ್ಪಿತ ಡೇಟಾ ಉತ್ಪಾದನೆ - ಸೂಕ್ಷ್ಮ ಟ್ಯೂನಿಂಗ್ ಕಾರ್ಯಗಳಿಗಾಗಿ ಪರಿಣಾಮಕಾರಿ ಡೇಟಾ ಸೃಷ್ಟಿಸಲು ಸಾಧ್ಯತೆ 

### ನೇಟಿವ್ ಫಂಕ್ಷನ್ ಕರೆ 

ಲಾಮಾ 3.1 ಕಾರ್ಯ ಅಥವಾ ಉಪಕರಣ ಕರೆಗಳಲ್ಲಿ ಹೆಚ್ಚು ಪರಿಣಾಮಕಾರಿ ಆಗಿದೆ ಎಂದು ಸೂಕ್ಷ್ಮವಾಗಿ ತರಬೇತಿಗೆ ಒಳಪಡಿಸಲಾಗಿದೆ. ಇದರಲ್ಲಿ ಎರಡು ನಿರ್ಮಿತ ಉಪಕರಣಗಳಿವೆ, ಮಾದರಿ ಬಳಕೆದಾರರಿಂದ ಬಂದ ಪ್ರಾಂಪ್ಟ್ ಆಧಾರದ ಮೇಲೆ ಬಳಕೆ ಮಾಡಲು ಅಗತ್ಯವಿರುವಂತೆ ಗುರುತಿಸಬಲ್ಲದು. ಈ ಉಪಕರಣಗಳು ಇವು: 

- **ಬ್ರೇವ್ ಸೆರ್ಚ್** - ವೆಬ್ ಸರ್ಚ್ ಮಾಡಿ ತಾಳ್ಮೆಯ ಮಾಹಿತಿ ಪಡೆಯಬಹುದು, ಉದಾಹರಣೆಗೆ ಹವಾಮಾನ 
- **ವೊಲ್ಫ್ರಾಂ ಆಲ್ಫಾ** - ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಗಣಿತಗತ ಲೆಕ್ಕಾಚಾರಗಳಿಗೆ, ಸ್ವ-ಲೇಖನ ಕಾರ್ಯಗಳನ್ನು ಬರೆಯಬೇಕಾಗದು. 

ನೀವು ಸ್ವಂತ ಕಸ್ಟಮ್ ಉಪಕರಣಗಳನ್ನು ಕೂಡ ರಚಿಸಬಹುದು, LLM ಅವುಗಳನ್ನು ಕರೆ ಮಾಡಬಲ್ಲದು. 

ಕೆಳಗಿನ ಕೋಡ್ ಉದಾಹರಣೆಯಲ್ಲಿ: 

- ನಮಗೆ ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳನ್ನು (brave_search, wolfram_alpha) ವ್ಯವಸ್ಥೆ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ವ್ಯಾಖ್ಯಾನಿಸುತ್ತೇವೆ. 
- ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್ ಒಂದು ನಗರದಲ್ಲಿ ಹವಾಮಾನವನ್ನು ಕೇಳುತ್ತದೆ. 
- LLM ಬ್ರೇವ್ ಸೆರ್ಚ್ ಉಪಕರಣವನ್ನು ಕರೆಮಾಡುತ್ತದೆ, ಇದು ಹೀಗಿರಬಹುದು `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*ಗಮನಿಸಿ: ಈ ಉದಾಹರಣೆಯು ಕೇವಲ ಉಪಕರಣ ಕರೆಮಾಡುತ್ತದೆ, ಫಲಿತಾಂಶ ಪಡೆಯಲು ನೀವು ಬ್ರೇವ್ API ಪುಟದಲ್ಲಿ ಉಚಿತ ಖಾತೆ ಸೃಷ್ಟಿಸಿ ಫಂಕ್ಷನ್ ಪರिभಾಷೆ ಮಾಡಬೇಕಾಗುತ್ತದೆ.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# ಇವನ್ನು ನಿಮ್ಮ ಮൈಕ್ರೊಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಪ್ರಾಜೆಕ್ಟ್‌ನ "ಒವರವ್ಯೂ" ಪುಟದಿಂದ ಪಡೆಯಿರಿ
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

## ಲಾಮಾ 3.2 

LLM ಆಗಿದೆಯಾದರೂ, ಲಾಮಾ 3.1ನ ಒಂದು ಮಿತಿಯೇ ಬಹುಮಾಧ್ಯಮ ಸಮರ್ಥನೆಯ ಕೊರತೆ. ಅಂದರೆ, ಚಿತ್ರಗಳಂತಹ ವಿವಿಧ ರೀತಿಯ ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ಪ್ರಾಂಪ್ಟ್‌ಗಳಾಗಿ ಉಪಯೋಗಿಸಲು ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನೀಡಲು ಅಸಾಧ್ಯ. ಈ ಸಾಮರ್ಥ್ಯ ಲಾಮಾ 3.2 ರ ಪ್ರಮುಖ ಲಕ್ಷಣವಾಗಿದೆ. ಇವುಗಳಲ್ಲಿ ಇತರವು: 

- ಬಹುಮಾಧ್ಯಮತೆ - ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರದ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಲು ಸಾಧ್ಯತೆ 
- ಸಣ್ಣದಿಂದ ಮಧ್ಯಮ ಗಾತ್ರದ ಬೇರಿಯಂಟ್‌ಗಳು (11B ಮತ್ತು 90B) - ಸ್ಥಳಾಂತರಕ್ಕೆ ಅನುಕೂಲಕರ ಆಯ್ಕೆಗಳು, 
- ಕೇವಲ ಪಠ್ಯ ಬೇರಿಯಂಟ್‌ಗಳು (1B ಮತ್ತು 3B) - ಇದರಿಂದ ಮಾದರಿ ಎಡ್ಜ್ / ಮೊಬೈಲ್ ಸಾಧನಗಳಲ್ಲಿ ನಿಯೋಜಿಸಲು ಸಾಧ್ಯ ಮತ್ತು ಕಡಿಮೆ ವಿಳಂಬ 

ಬಹುಮಾಧ್ಯಮ ಬೆಂಬಲವು ಮುಕ್ತ ಮೂಲ ಮಾದರಿಗಳ ಲೋಕದಲ್ಲಿ ದೊಡ್ಡ ಹೆಜ್ಜೆ. ಕೆಳಗಿನ ಕೋಡ್ ಉದಾಹರಣೆ ಚಿತ್ರ ಮತ್ತು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್ ತೆಗೆದುಕೊಂಡು ಲಾಮಾ 3.2 90Bರಿಂದ ಚಿತ್ರ ವಿಶ್ಲೇಷಣೆಯನ್ನು ಪಡೆಯುತ್ತದೆ. 


### ಲಾಮಾ 3.2 ಜೊತೆ ಬಹುಮಾಧ್ಯಮ ಬೆಂಬಲ

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

# ನಿಮ್ಮ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಯೋಜನೆಯ "ಸಾರಾಂಶ" ಪುಟದಿಂದ ಇದನ್ನು ಪಡೆಯಿರಿ
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

## ಕಲಿಕೆ ಇಲ್ಲಿ ನಿಲ್ಲದು, ಪ್ರಯಾಣವನ್ನು ಮುಂದುವರೆಸಿರಿ

ಈ ಪಾಠವನ್ನು ಮುಗಿಸಿದ ಮೇಲೆ, ನಮ್ಮ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ಅನ್ನು ಪರಿಶೀಲಿಸಿ ನಿಮ್ಮ ಜನರೇಟಿವ್ AI ಜ್ಞಾನವನ್ನು ಮುಂದುವರೆಸಿಕೊಳ್ಳಿ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->