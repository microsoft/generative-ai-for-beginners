# ಮೆಟಾ ಕುಟುಂಬ ಮಾದರಿಗಳೊಂದಿಗೆ ನಿರ್ಮಾಣ 

## ಪರಿಚಯ 

ಈ ಪಾಠವು ಒಳಗೊಂಡಿದೆ: 

- ಮುಖ್ಯ ಮೆಟಾ ಕುಟುಂಬ ಮಾದರಿಗಳಾದ ಲ್ಲಾಮಾ 3.1 ಮತ್ತು ಲ್ಲಾಮಾ 3.2 ಅನ್ವೇಷಣೆಯು 
- ಪ್ರತಿ ಮಾದರಿಯ ಬಳಕೆಯ ಪರಿಹಾರಗಳು ಮತ್ತು ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು 
- ಪ್ರತಿ ಮಾದರಿಯ ಅನನ್ಯ বৈಶಿಷ್ಟ್ಯಗಳನ್ನು ತೋರಿಸುವ ಕೋಡ್ ಉದಾಹರಣೆ 


## ಮೆಟಾ ಕುಟುಂಬದ ಮಾದರಿಗಳು 

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು ಮೆಟಾ ಕುಟುಂಬ ಅಥವಾ "ಲ್ಲಾಮಾ ಹರ್ಡ್" ಎಂಬ ಎರಡು ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಷಿಸೋಣ - ಲ್ಲಾಮಾ 3.1 ಮತ್ತು ಲ್ಲಾಮಾ 3.2.

ಈ ಮಾದರಿಗಳು ವಿಭಿನ್ನ ರೂಪಗಳಲ್ಲಿ ಲಭ್ಯವಿದ್ದು ಮತ್ತು GitHub ಮಾದರಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ದೊರೆಯುತ್ತವೆ. GitHub ಮಾದರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು [AI ಮಾದರಿಗಳೊಂದಿಗೆ ಪ್ರೋಟೋಟೈಪ್ ಮಾಡುವ ಬಗ್ಗೆ](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ಇವುಗಳ ಬಗ್ಗೆ ಹೆಚ್ಚು ವಿವರಗಳು ಇಲ್ಲಿವೆ.

ಮಾದರಿ ರೂಪಗಳು: 
- ಲ್ಲಾಮಾ 3.1 - 70B ಸೂಚನೆ 
- ಲ್ಲಾಮಾ 3.1 - 405B ಸೂಚನೆ 
- ಲ್ಲಾಮಾ 3.2 - 11B ದೃಷ್ಟಿ ಸೂಚನೆ 
- ಲ್ಲಾಮಾ 3.2 - 90B ದೃಷ್ಟಿ ಸೂಚನೆ 

*ಸೂಚನೆ: ಲ್ಲಾಮಾ 3 ಕೂಡ GitHub Models ನಲ್ಲಿ ಲಭ್ಯವಿದೆ ಆದರೆ ಈ ಪಾಠದಲ್ಲಿ ಅದನ್ನು ಒಳಗೊಂಡಿಲ್ಲ* 

## ಲ್ಲಾಮಾ 3.1 

405 ಬಿಲಿಯನ್ ಪರಿಮಾಣಗಳೊಂದಿಗೆ, ಲ್ಲಾಮಾ 3.1 ತೆರೆದ소스 LLM ವರ್ಗಕ್ಕೆ ಸೇರಿದೆ. 

ಈ ಮಾದರಿ ಮೊದಲಿನ ಲ್ಲಾಮಾ 3 ಬಿಡುಗಡೆಗೆ ಹೋಲಿಕೆಯಲ್ಲಿ ಅಪ್‌ಗ್ರೇಡ್ ಆಗಿದೆ: 

- ದೊಡ್ಡ ಸನ್ನಿವೇಶ ವಿಂಡೋ - 128k ಟೋಕನ್ಸ್ ವಿರುದ್ಧ 8k ಟೋಕನ್ಸ್ 
- ಗರಿಷ್ಟ ಔಟ್‌ಪುಟ್ ಟೋಕನ್ಸ್ - 4096 ವಿರುದ್ಧ 2048 
- ಉತ್ತಮ ಬಹುಭಾಷಾ ಬೆಂಬಲ - ತರಬೇತಿ ಟೋಕನ್ಸ್ ಹೆಚ್ಚಳದ ಮೇರೆಗೆ 

ಇವು ಲ್ಲಾಮಾ 3.1 ಗೆ ಸುಕ್ಷ್ಮವಾದ ಬಳಸಲುಕೊಂಡ ಅಪ್ಲಿಕೇಶನ್‌ಗಳ ನಿರ್ಮಾಣ ಸಮಯದಲ್ಲಿ ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಬಳಕೆಗಳನ್ನು ನಿರ್ವಹಿಸಲು ನೆರವಾಗುತ್ತವೆ: 
- ಸ್ಥಳೀಯ ಕಾರ್ಯವಿಧಾನ ಕರೆ - LLM ವರ್ಕ್ಫ್ಲೋ ಹೊರಗಿನ ಬಾಹ್ಯ ಸಾಧನಗಳು ಮತ್ತು ಕಾರ್ಯಗಳನ್ನು ಕರೆ ಮಾಡುವ ಸಾಮರ್ಥ್ಯ 
- ಉತ್ತಮ RAG ಕಾರ್ಯಕ್ಷಮತೆ - ಹೆಚ್ಚಿನ ಸನ್ನಿವೇಶ ವಿಂಡೋಯಿಂದಾಗಿ 
- ಕೃಕೃತಿಯಾದ ದತ್ತಾಂಶ ರಚನೆ - ಸೂಕ್ಷ್ಮ-ಸಂವರ್ಧನೆಗೆ ಸೂಕ್ತವಾದ ದತ್ತಾಂಶವನ್ನು ಸೃಷ್ಟಿಸುವ ಸಾಮರ್ಥ್ಯ 

### ಸ್ಥಳೀಯ ಕಾರ್ಯವಿಧಾನ ಕರೆ 

ಲ್ಲಾಮಾ 3.1 ಅನ್ನು ಕಾರ್ಯವಿಧಾನ ಅಥವಾ ಸಾಧನ ಕರೆಗಳನ್ನು ಹೆಚ್ಚು ಪರಿಣಾಮಕಾರಿಯಾಗಿ ಮಾಡಬಹುದಾಗಿಸಲು ಸೂಕ್ಷ್ಮ-ಸಂವರ್ಧಿಸಲಾಗಿದೆ. ಇದು ರೂಢಿಪಡಿಸಿಕೊಂಡ ಎರಡು ಸಿದ್ಧ ಸಾಧನಗಳನ್ನೂ ಹೊಂದಿದೆ, ಪ್ರತಿಯೊಂದು ಬಳಕೆದಾರನ ಪ್ರಾಂಪ್ಟ್ ಆಧಾರದ ಮೇಲೆ ಅಂದಾಜು ಕಟ್ಟಿ ಬಳಸಲು ಬೇಕಾದವು ಎಂದು ಗುರುತಿಸಬಹುದು. ಈ ಸಾಧನಗಳು: 

- **ಬ್ರೇವ್ ಸರ್ಚ್** - ವೆಬ್ ಹುಡುಕಾಟ ಮಾಡುವ ಮೂಲಕ ಹವಾಮಾನ ಮುಂತಾದ ನವೀನ ಮಾಹಿತಿಗಳನ್ನು ಪಡೆಯಲು ಉಪಯೋಗಿಸಬಹುದು 
- **ವೋಲ್ಫ್ರಾಮ್ ಆಲ್ಫಾ** - ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಗಣಿತ ಲೆಕ್ಕಾಚಾರಗಳನ್ನು ಪರಿಹರಿಸಲು ಬಳಸಬಹುದು; ನಿಮ್ಮದೇ ಕಾರ್ಯಗಳನ್ನು ಬರೆಯಬೇಕಾಗಿಲ್ಲ 

ನೀವು ನಿಮ್ಮದೇ ಕಸ್ಟಮ್ ಸಾಧನಗಳನ್ನು ರಚಿಸಬಹುದು, ಅವುಗಳನ್ನು LLM ಕರೆಮಾಡಿ ಬಳಸಬಹುದು.

 ಕೆಳಗಿನ ಕೋಡ್ ಉದಾಹರಣೆಯಲ್ಲಿ: 

- ನಾವು ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು (brave_search, wolfram_alpha) ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ವ್ಯಾಖ್ಯಾನಿಸುತ್ತೇವೆ. 
- ನಿರ್ದಿಷ್ಟ ನಗರದ ಹವಾಮಾನ ಬಗ್ಗೆ ವಿಚಾರಿಸುವ ಬಳಕೆದಾರನ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಕಳುಹಿಸುತ್ತೇವೆ. 
- LLM ಬ್ರೇವ್ ಸರ್ಚ್ ಸಾಧನಕ್ಕೆ ಕರೆಯನ್ನು ಈ ರೀತಿ ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತದೆ `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*ಸೂಚನೆ: ಈ ಉದಾಹರಣೆ ಕೇವಲ ಸಾಧನ ಕರೆಯನ್ನು ಮಾಡುತ್ತದೆ, ನೀವು ಫಲಿತಾಂಶಗಳನ್ನು ಪಡೆಯಲು, ಬ್ರೇವ್ API ಪುಟದಲ್ಲಿ ಉಚಿತ ಖಾತೆ ರಚಿಸಿ ಮತ್ತು ಕಾರ್ಯವಿಧಾನವನ್ನು ನಿಯೋಜಿಸಬೇಕಾಗುತ್ತದೆ.*

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

ಒಂದು LLM ಆಗಿರ despite, ಲ್ಲಾಮಾ 3.1 ನ ಒಂದು ಸೀಮಿತತೆ ಅಂದರೆ ಅದರ ಬಹುಮಾದರಿತೋಟೆಯ ಕೊರತೆ. ಅಂದರೆ, ಚಿತ್ರಗಳನ್ನು ಪ್ರಾಂಪ್ಟ್‌ಗಳಾಗಿ ಬಳಸಿಕೊಂಡು ಉತ್ತರಗಳನ್ನು ನೀಡುವ ಸಾಮರ್ಥ್ಯ ಇಲ್ಲದೇ ಇರುವುದಾಗಿದೆ. ಇದು ಲ್ಲಾಮಾ 3.2 ನ ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳಲ್ಲಿ ಒಂದಾಗಿದೆ. ಇವುಗಳಲ್ಲಿವೆ: 

- ಬಹುಮಾದರಿತೋಟೆ - ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಎರಡನ್ನೂ ಪ್ರಮಾಣೀಕರಿಸುವ ಸಾಮರ್ಥ್ಯ 
- ಸಣ್ಣದಿಂದ ಮಧ್ಯಮ ಗಾತ್ರದ ರೂಪಾಂತರಗಳು (11B ಮತ್ತು 90B) - ಸಂವೇದಿ ನಿಯೋಜನೆ ಆಯ್ಕೆಯನ್ನು ನೀಡುತ್ತದೆ 
- ಪಠ್ಯಮಾತ್ರ ರೂಪಾಂತರಗಳು (1B ಮತ್ತು 3B) - ಏಜ್ / ಮೊಬೈಲ್ ಸಾಧನಗಳಲ್ಲಿ ನಿಯೋಜನೆಗೆ ಮತ್ತು ಕಡಿಮೆ ವಿಳಂಬಕ್ಕೆ ಅನುಕೂಲವಾಗುತ್ತದೆ 

ಬಹುಮಾದರಿತೋಟೆ ಬೆಂಬಲವು ತೆರೆಯಲಾದ ಮೂಲದ ಮಾದರಿಗಳ ಪ್ರಪಂಚದಲ್ಲಿ ದೊಡ್ಡ ಹೆಜ್ಜೆಯನ್ನು ಸೂಚಿಸುತ್ತದೆ. ಕೆಳಗಿನ ಕೋಡ್ ಉದಾಹರಣೆ ಲ್ಲಾಮಾ 3.2 90B ಯಿಂದ ಚಿತ್ರ ಮತ್ತು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಸ್ವೀಕರಿಸಿ ಚಿತ್ರ ವಿಶ್ಲೇಷಣೆಯನ್ನು ಪಡೆಯುತ್ತದೆ. 


### ಲ್ಲಾಮಾ 3.2 ಸಹಿತ ಬಹುಮಾದರಿತೋಟೆ ಬೆಂಬಲ

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

## ಕಲಿಕೆ ಇಲ್ಲಿಯೇ ನಿಂತಿಲ್ಲ, ಯಾತ್ರೆಯನ್ನು ಮುಂದುವರೆಸಿ

ಈ ಪಾಠವನ್ನು ಮುಗಿಸಿದ ನಂತರ, ನಮದಿನ [ಜನನೆ AI ಕಲಿಕಾ ಸಂಗ್ರಹ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ಅನ್ನು ನೋಡಿ ನಿಮ್ಮ ಜನನೆ AI ಜ್ಞಾನವನ್ನು ಮುಂದುವರೆಸಿ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅರ್ಥಾತ್**:
ಈ ದಾಖಲೆಯನ್ನು ಏಐ ಭಾಷಾಂತರ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಭಾಷಾಂತರಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಗುರಿಯಾಗಿಸಿಕೊಂಡಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಭಾಷಾಂತರಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಶುದ್ಧತೆಗಳು ಇರಬಹುದಾಗಿ ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ದಾಖಲೆ ಅದರ ದೇಶೀಯ ಭಾಷೆಯಲ್ಲಿ ಪ್ರಾಮಾಣಿಕ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಲಾಗಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಭಾಷಾಂತರ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನದ ಹೊಣೆಗಾರಿಕೆ ನಾವು ವಹಿಸುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->