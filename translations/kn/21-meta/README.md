# ಮೆಟಾ ಫ್ಯಾಮಿಲಿ ಮಾದರಿಗಳೊಂದಿಗೆ ನಿರ್ಮಾಣ

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ನಾವು ಚರ್ಚಿಸುವುದು:

- ಎರಡು ಪ್ರಮುಖ ಮೆಟಾ ಫ್ಯಾಮಿಲಿ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು - ಲ್ಲಾಮಾ 3.1 ಮತ್ತು ಲ್ಲಾಮಾ 3.2
- ಪ್ರತಿ ಮಾದರಿಯ ಬಳಕೆ ಪ್ರಕರಣಗಳು ಮತ್ತು ಸಂದರ್ಭಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು
- ಪ್ರತಿ ಮಾದರಿಯ ವಿಶಿಷ್ಟ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ತೋರಿಸುವ ಕೋಡ್ ಉದಾಹರಣೆ

## ಮೆಟಾ ಫ್ಯಾಮಿಲಿ ಮಾದರಿಗಳು

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು ಮೆಟಾ ಫ್ಯಾಮಿಲಿ ಅಥವಾ "ಲ್ಲಾಮಾ ಹರ್ಡ್" ನಿಂದ 2 ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸುವೆವು - ಲ್ಲಾಮಾ 3.1 ಮತ್ತು ಲ್ಲಾಮಾ 3.2

ಈ ಮಾದರಿಗಳು ವಿಭಿನ್ನ ರೂಪಾಂತರಗಳಲ್ಲಿ ಲಭ್ಯವಿದ್ದು GitHub ಮಾದರಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಲಭ್ಯವಿವೆ. GitHub ಮಾದರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು [AI ಮಾದರಿಗಳೊಂದಿಗೆ ಪ್ರೋಟೋಟೈಪಿಂಗ್](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ಕುರಿತು ಹೆಚ್ಚಿನ ವಿವರಗಳು ಇಲ್ಲಿವೆ.

ಮಾದರಿ ರೂಪಾಂತರಗಳು:
- ಲ್ಲಾಮಾ 3.1 - 70B ಸೂಚನೆ
- ಲ್ಲಾಮಾ 3.1 - 405B ಸೂಚನೆ
- ಲ್ಲಾಮಾ 3.2 - 11B ದೃಶ್ಯ ಸೂಚನೆ
- ಲ್ಲಾಮಾ 3.2 - 90B ದೃಶ್ಯ ಸೂಚನೆ

*ಗಮನಿಸಿ: ಲ್ಲಾಮಾ 3 ಕೂಡ GitHub ಮಾದರಿಗಳಲ್ಲಿ ಲಭ್ಯವಿದೆ ಆದರೆ ಈ ಪಾಠದಲ್ಲಿ ಚರ್ಚಿಸಲಾಗುವುದಿಲ್ಲ*

## ಲ್ಲಾಮಾ 3.1

405 ಬಿಲಿಯನ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳೊಂದಿಗೆ, ಲ್ಲಾಮಾ 3.1 ಮುಕ್ತ ಮೂಲ LLM ವರ್ಗಕ್ಕೆ ಸೇರಿದೆ.

ಈ ಮಾದರಿ ಹಿಂದಿನ ಬಿಡುಗಡೆ ಲ್ಲಾಮಾ 3 ಗೆ ಹೋಲಿಸಿದರೆ ಈ ಸುಧಾರಣೆಗಳನ್ನು ನೀಡುತ್ತದೆ:

- ದೊಡ್ಡ ಕಾನ್ಟೆಕ್ಸ್ಟ್ ವಿಂಡೋ - 128k ಟೋಕನ್ಸ್ ವಿರುದ್ಧ 8k ಟೋಕನ್ಸ್
- ಹೆಚ್ಚಿನ ಗರಿಷ್ಠ ಔಟ್‌ಪುಟ್ ಟೋಕನ್ಸ್ - 4096 ವಿರುದ್ಧ 2048
- ಉತ್ತಮ ಬಹುಭಾಷಾ ಬೆಂಬಲ - ತರಬೇತಿ ಟೋಕನ್ಸ್ ಹೆಚ್ಚಳದಿಂದ

ಇವು ಲ್ಲಾಮಾ 3.1 ಗೆ GenAI ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವಾಗ ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಬಳಕೆ ಪ್ರಕರಣಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ, ಉದಾಹರಣೆಗೆ:
- ನೇಟಿವ್ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ - LLM ಕಾರ್ಯಪ್ರವಾಹದ ಹೊರಗಿನ ಬಾಹ್ಯ ಸಾಧನಗಳು ಮತ್ತು ಕಾರ್ಯಗಳನ್ನು ಕರೆಸಿಕೊಳ್ಳುವ ಸಾಮರ್ಥ್ಯ
- ಉತ್ತಮ RAG ಕಾರ್ಯಕ್ಷಮತೆ - ಹೆಚ್ಚಿನ ಕಾನ್ಟೆಕ್ಸ್ಟ್ ವಿಂಡೋ ಕಾರಣದಿಂದ
- ಸಿಂಥೆಟಿಕ್ ಡೇಟಾ ಉತ್ಪಾದನೆ - ಸೂಕ್ಷ್ಮ-ಟ್ಯೂನಿಂಗ್ ಮುಂತಾದ ಕಾರ್ಯಗಳಿಗೆ ಪರಿಣಾಮಕಾರಿ ಡೇಟಾ ಸೃಷ್ಟಿಸುವ ಸಾಮರ್ಥ್ಯ

### ನೇಟಿವ್ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್

ಲ್ಲಾಮಾ 3.1 ಅನ್ನು ಕಾರ್ಯ ಅಥವಾ ಸಾಧನ ಕರೆಗಳನ್ನು ಹೆಚ್ಚು ಪರಿಣಾಮಕಾರಿಯಾಗಿ ಮಾಡಲು ಸೂಕ್ಷ್ಮ-ಟ್ಯೂನ್ ಮಾಡಲಾಗಿದೆ. ಇದರಲ್ಲಿ ಎರಡು ಒಳಗೊಂಡಿರುವ ಸಾಧನಗಳಿವೆ, ಅವುಗಳನ್ನು ಬಳಕೆದಾರನ ಪ್ರಾಂಪ್ಟ್ ಆಧಾರದ ಮೇಲೆ ಬಳಸಬೇಕೆಂದು ಮಾದರಿ ಗುರುತಿಸಬಹುದು. ಈ ಸಾಧನಗಳು:

- **ಬ್ರೇವ್ ಸರ್ಚ್** - ವೆಬ್ ಹುಡುಕಾಟ ನಡೆಸಿ ಹವಾಮಾನ ಮುಂತಾದ ನವೀಕೃತ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯಲು ಬಳಸಬಹುದು
- **ವೋಲ್ಫ್ರಾಮ್ ಆಲ್ಫಾ** - ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಗಣಿತೀಯ ಲೆಕ್ಕಾಚಾರಗಳಿಗೆ ಬಳಸಬಹುದು, ನಿಮ್ಮದೇ ಕಾರ್ಯಗಳನ್ನು ಬರೆಯಬೇಕಾಗಿಲ್ಲ

ನೀವು ನಿಮ್ಮದೇ ಕಸ್ಟಮ್ ಸಾಧನಗಳನ್ನು ಸೃಷ್ಟಿಸಬಹುದು, ಅವನ್ನು LLM ಕರೆ ಮಾಡಬಹುದು.

ಕೆಳಗಿನ ಕೋಡ್ ಉದಾಹರಣೆಯಲ್ಲಿ:

- ನಾವು ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು (brave_search, wolfram_alpha) ವ್ಯಾಖ್ಯಾನಿಸುತ್ತೇವೆ.
- ನಿರ್ದಿಷ್ಟ ನಗರದಲ್ಲಿ ಹವಾಮಾನ ಕುರಿತು ಕೇಳುವ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಕಳುಹಿಸುತ್ತೇವೆ.
- LLM ಬ್ರೇವ್ ಸರ್ಚ್ ಸಾಧನಕ್ಕೆ `<|python_tag|>brave_search.call(query="Stockholm weather")` ಎಂಬ ಸಾಧನ ಕರೆ ಮೂಲಕ ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತದೆ.

*ಗಮನಿಸಿ: ಈ ಉದಾಹರಣೆ ಕೇವಲ ಸಾಧನ ಕರೆ ಮಾಡುತ್ತದೆ, ಫಲಿತಾಂಶಗಳನ್ನು ಪಡೆಯಲು ನೀವು ಬ್ರೇವ್ API ಪುಟದಲ್ಲಿ ಉಚಿತ ಖಾತೆಯನ್ನು ಸೃಷ್ಟಿಸಿ ಕಾರ್ಯವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಬೇಕಾಗುತ್ತದೆ*

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

## ಲ್ಲಾಮಾ 3.2

LLM ಆಗಿದ್ದರೂ, ಲ್ಲಾಮಾ 3.1 ಗೆ ಇರುವ ಒಂದು ಮಿತಿ ಬಹುಮಾಧ್ಯಮತೆ. ಅಂದರೆ, ಚಿತ್ರಗಳು ಮುಂತಾದ ವಿಭಿನ್ನ ರೀತಿಯ ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ಪ್ರಾಂಪ್ಟ್ ಆಗಿ ಬಳಸಿಕೊಂಡು ಪ್ರತಿಕ್ರಿಯೆ ನೀಡುವ ಸಾಮರ್ಥ್ಯ. ಈ ಸಾಮರ್ಥ್ಯ ಲ್ಲಾಮಾ 3.2 ನ ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳಲ್ಲಿ ಒಂದಾಗಿದೆ. ಇವುಗಳಲ್ಲಿ ಇನ್ನು ಕೆಲವು:

- ಬಹುಮಾಧ್ಯಮತೆ - ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಎರಡನ್ನೂ ಮೌಲ್ಯಮಾಪನ ಮಾಡಲು ಸಾಮರ್ಥ್ಯ
- ಸಣ್ಣದಿಂದ ಮಧ್ಯಮ ಗಾತ್ರದ ರೂಪಾಂತರಗಳು (11B ಮತ್ತು 90B) - ಇದು ಲವಚಿಕ ನಿಯೋಜನೆ ಆಯ್ಕೆಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ
- ಪಠ್ಯ ಮಾತ್ರದ ರೂಪಾಂತರಗಳು (1B ಮತ್ತು 3B) - ಇದು ಮಾದರಿಯನ್ನು ಎಡ್ಜ್ / ಮೊಬೈಲ್ ಸಾಧನಗಳಲ್ಲಿ ನಿಯೋಜಿಸಲು ಮತ್ತು ಕಡಿಮೆ ವಿಳಂಬವನ್ನು ಒದಗಿಸುತ್ತದೆ

ಬಹುಮಾಧ್ಯಮ ಬೆಂಬಲವು ಮುಕ್ತ ಮೂಲ ಮಾದರಿಗಳ ಜಗತ್ತಿನಲ್ಲಿ ದೊಡ್ಡ ಹೆಜ್ಜೆಯಾಗಿದೆ. ಕೆಳಗಿನ ಕೋಡ್ ಉದಾಹರಣೆ ಚಿತ್ರ ಮತ್ತು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್ ಎರಡನ್ನೂ ತೆಗೆದುಕೊಂಡು ಲ್ಲಾಮಾ 3.2 90B ನಿಂದ ಚಿತ್ರ ವಿಶ್ಲೇಷಣೆಯನ್ನು ಪಡೆಯುತ್ತದೆ.

### ಲ್ಲಾಮಾ 3.2 ಜೊತೆಗೆ ಬಹುಮಾಧ್ಯಮ ಬೆಂಬಲ

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

## ಕಲಿಕೆ ಇಲ್ಲಿ ನಿಲ್ಲುವುದಿಲ್ಲ, ಪ್ರಯಾಣವನ್ನು ಮುಂದುವರೆಸಿ

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನಮ್ಮ [ಜನರೇಟಿವ್ AI ಕಲಿಕೆ ಸಂಗ್ರಹ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ಅನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಜನರೇಟಿವ್ AI ಜ್ಞಾನವನ್ನು ಮುಂದುವರೆಸಿ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->