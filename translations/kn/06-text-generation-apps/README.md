# ಪಠ್ಯ ತಯಾರಿಕೆಯ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಾಣ ಮಾಡಿ

[![ಪಠ್ಯ ತಯಾರಿಕೆಯ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಾಣ ಮಾಡುವುದು](../../../translated_images/kn/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ಈ ಪಾಠದ ವೀಡಿಯೋವನ್ನು ನೋಡಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

ಈ ಪಠ್ಯಕ್ರಮದ ಮೂಲಕ ನೀವು ಇದುವರೆಗೆ ನೋಡಿರುವಂತೆ, ಪ್ರಾಂಪ್ಟ್ಗಳು ಎಂಬ ಮೂಲಭೂತ ಪರಿಕಲ್ಪನೆಗಳು ಮತ್ತು "ಪ್ರಾಂಪ್ಟ್ ಇಂಜಿನಿಯರಿಂಗ್" ಎನ್ನುವ ಸಂಪೂರ್ಣ ಶಿಸ್ತಿನೂ ಇವೆ. ನೀವು ಸಂವಹನ ಮಾಡಬಲ್ಲ ಅನೇಕ ಟೂಲ್ಗಳು ಇದೆ, ಉದಾಹರಣೆಗೆ ChatGPT, Office 365, Microsoft Power Platform ಮುಂತಾದವುಗಳು ನಿಮಗೆ ಯಾವುದೋ ಕೆಲಸ ಮಾಡಲು ಪ್ರಾಂಪ್ಟ್ ಬಳಸಲು ನೆರವಾಗುತ್ತವೆ.

ನೀವು ಒಂದು ಆಪ್‌ಗೆ ಅಂತಹ ಅನುಭವವನ್ನು ಸೇರಿಸಲು, ಪ್ರಾಂಪ್ಟ್ಗಳು, ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳು (completions) ಮತ್ತು ಕೆಲಸ ಮಾಡಲು ಲೈಬ್ರರಿ ಆಯ್ಕೆಮಾಡುವುದು ಜ್ಞಾನದ ಅಗತ್ಯವಿದೆ. ಅದೇನು ನೀವು ಈ ಅಧ್ಯಾಯದಲ್ಲಿ ಕಲಿಯುವಿರಿ.

## ಪರಿಚಯ

ಈ ಅಧ್ಯಾಯದಲ್ಲಿ ನೀವು:

- openai ಲೈಬ್ರರಿ ಮತ್ತು ಅದರ ಮೂಲಭೂತ ಪರಿಕಲ್ಪನೆಗಳನ್ನು ಕಲಿಯಿರಿ.
- openai ಬಳಸಿ ಪಠ್ಯ ತಯಾರಿಕೆಯ ಆಪ್ ನಿರ್ಮಿಸಿ.
- ಪಠ್ಯ ತಯಾರಿಕೆಯ ಆಪ್ ನಿರ್ಮಿಸಲು ಪ್ರಾಂಪ್ಟ್, ತಾಪಮಾನ (temperature), ಟೋಕನ್ಗಳ ಬಳಸಿಕೊಳ್ಳುವ ವಿಧಾನವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ.

## ಕಲಿಕಾ ಗುರಿಗಳು

ಈ ಪಾಠದ ನಂತರ, ನೀವು ಸಾಧ್ಯವಾಗುವುದು:

- ಪಠ್ಯ ತಯಾರಿಕೆಯ ಆಪ್ ಎಂದರೇನು ಎಂಬುದನ್ನು ವಿವರಿಸಬಹುದು.
- openai ಬಳಸಿ ಪಠ್ಯ ತಯಾರಿಕೆಯ ಆಪ್ ನಿರ್ಮಿಸಬಹುದು.
- ನಿಮ್ಮ ಆಪ್‌ಗಾಗಿ ಹೆಚ್ಚು ಅಥವಾ ಕಡಿಮೆ ಟೋಕನ್ಗಳನ್ನು ಬಳಸಲು ಹಾಗೂ ತಾಪಮಾನವನ್ನು ಬದಲಾಯಿಸಲು ತಯಾರು ಮಾಡಬಹುದು, ಬದಲಾಗುವ output ಗಾಗಿ.

## ಪಠ್ಯ ತಯಾರಿಕೆಯ ಆಪ್ ಎಂದರೇನು?

ಸಾಮಾನ್ಯವಾಗಿ ನೀವು ಒಂದು ಆಪ್ ನಿರ್ಮಿಸುವಾಗ, ಅದರಲ್ಲಿ ಕೆಳಗಿನಂತಹ ಯಾವುದೋ ಇಂಟರ್ಫೇಸ್ ಇದೆಯೇ:

- ಕಮಾಂಡ್ ಆಧಾರಿತ. ಕಾನ್ಸೋಲ್ ಆಪ್‌ಗಳು ಸಾಮಾನ್ಯವಾಗಿವೆ, ನೀವು ಕಮಾಂಡ್ ಟೈಪ್ ಮಾಡಿ ಒಂದು ಕೆಲಸವನ್ನು ನಿರ್ವಹಿಸುತ್ತವೆ. ಉದಾಹರಣೆಗಾಗಿ, `git` ಒಂದು ಕಮಾಂಡ್ ಆಧಾರಿತ ಆಪ್.
- ಬಳಕೆದಾರ ಇಂಟರ್ಫೇಸ್ (UI). ಕೆಲವು ಆಪ್‌ಗಳಿಗೆ ಗ್ರಾಫಿಕಲ್ ಯೂಸರ್ ಇಂಟರ್ಫೇಸ್ (GUI) ಇರುತ್ತದೆ, ಅಲ್ಲಿ ನೀವು ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ, ಪಠ್ಯ ನಮೂದಿಸಿ, ಆಯ್ಕೆಗಳನ್ನು ಮಾಡುತ್ತೀರಿ.

### ಕಾನ್ಸೋಲ್ ಮತ್ತು UI ಆಪ್‌ಗಳಿಗೆ ಸೀಮಿತತೆ ಇದೆ

ನೀವು ಕಮಾಂಡ್ ಆಧಾರಿತ ಆಪ್‌ಗೆ ಹೋಲಿಸಿದರೆ, ನೀವು ಕಮಾಂಡ್ ಟೈಪ್ ಮಾಡುತ್ತೀರಿ:

- **ಇದು ಸೀಮಿತವಾಗಿದೆ**. ನೀವು ಯಾವದೇ ಕಮಾಂಡ್ ಟೈಪ್ ಮಾಡಲಾಗುವುದಿಲ್ಲ, ಆಪ್ ಬೆಂಬಲಿಸಿದ ಕಮಾಂಡ್‌ಗಳೇ ಮಾತ್ರ.
- **ಭಾಷಾ ನిఖರಿತ**. ಕೆಲವು ಆಪ್‌ಗಳು ಹಲವಾರು ಭಾಷೆಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತವೆ, ಆದರೆ ಡೀಫಾಲ್ಟ್‌ನಲ್ಲಿ ಆಪ್ ಸ್ಪೆಸಿಫಿಕ್ ಭಾಷೆಗೆ ಮಾತ್ರ.

### ಪಠ್ಯ ತಯಾರಿಕೆಯ ಆಪ್‌ಗಳ ಲಾಭಗಳು

ಹಾಗಾದರೆ ಪಠ್ಯ ತಯಾರಿಕೆಯ ಆಪ್ ಹೇಗೆ ವಿಭಿನ್ನ?

ಪಠ್ಯ ತಯಾರಿಕೆಯ ಆಪ್‌ನಲ್ಲಿ, ನೀವು ಹೆಚ್ಚು ಲವಚಿಕತೆ ಹೊಂದಿದ್ದೀರಿ, ಕಮಾಂಡ್‌ಗಳ ನಿಯಮಕ್ಕೆ ಬಾರದಿರುವಿರಿ ಮತ್ತು ನೈಸರ್ಗಿಕ ಭಾಷೆಯನ್ನು ಬಳಸಿ ಆಪ್ನೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಬಹುದು. ಇನ್ನೊಂದು ಲಾಭವೆಂದರೆ ನೀವು ದತ್ತಾಂಶ ಮೂಲದ ಮೇಲೆ already ತರಬೇತುಗೊಂಡಿರುವಿರಿ, ಪರಂಪರائي ಆಪ್ ಮೂರು ಡೇಟಾಬೇಸಿನಲ್ಲಿರುವದ್ದಕ್ಕೆ ಸೀಮಿತವಾಗಿರುತ್ತಿತ್ತು.

### ಪಠ್ಯ ತಯಾರಿಕೆಯ ಆಪ್‌ನೊಂದಿಗೆ ನಾನು ಏನು ನಿರ್ಮಿಸಬಹುದು?

ಬಹುತೇಕ ಅನೇಕ ಅಂಶಗಳನ್ನು ನೀವು ನಿರ್ಮಿಸಬಹುದು. ಉದಾಹರಣೆಗಾಗಿ:

- **ಚಾಟ್‌ಬಾಟ್**. ನಿಮ್ಮ ಕಂಪನಿ ಮತ್ತು ಉತ್ಪನ್ನಗಳ ಕುರಿತು ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸುವ ಚಾಟ್‌ಬಾಟ್ ಒಳ್ಳೆಯ ಆಯ್ಕೆಯಾಗಬಹುದು.
- **ಸಹಾಯಗಾರ**. LLM ಗಳು ಪಠ್ಯ ಸಾರಾಂಶ ಹಾಕಲು, ವಿವರ ಸಂಗ್ರಹಿಸಲು, ಪಠ್ಯ ರಚಿಸಲು (ಉದಾಹರಣೆ, ರೆಸ್ಯೂಮ್) ಸುಲಭ.
- **ಕೋಡ್ ಸಹಾಯಕ**. ನೀವು ಬಳಸುತ್ತಿರುವ ಭಾಷಾ ಮಾದರಿಯ ಆಧಾರದಲ್ಲಿ, ನೀವು ಕೋಡ್ ಸಹಾಯಕವನ್ನು ಕಾಣಬಹುದು, ಉದಾಹರಣೆಗಾಗಿ GitHub Copilot ಅಥವಾ ChatGPT ಸಹಾಯ.

## ನಾನು ಹೇಗೆ ಪ್ರಾರಂಭಿಸಬಹುದು?

ಸಾಮಾನ್ಯವಾಗಿ LLM ಜೊತೆ ಸಂಯೋಜಿಸಲು ಎರಡು ವಿಧಾನಗಳಿವೆ:

- API ಬಳಸುವುದು. ಇಲ್ಲಿ ನೀವು ನಿಮ್ಮ ಪ್ರಾಂಪ್ಟ್‌ನೊಂದಿಗೆ ವೆಬ್ ವಿನಂತಿಗಳನ್ನು ರಚಿಸಿ ತಯಾರಿಸಲಾದ ಪಠ್ಯವನ್ನು ಪಡೆಯುತ್ತೀರಿ.
- ಲೈಬ್ರರಿ ಬಳಸುವುದು. ಲೈಬ್ರರಿಗಳು API ಕರೆಗಳನ್ನು ಒಳಗೊಂಡು, ಸುಲಭವಾಗಿ ಉಪಯೋಗಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ.

## ಲೈಬ್ರರಿಗಳು/SDK ಗಳು

LLM ಗಳೊಂದಿಗೆ ಕೆಲಸ ಮಾಡಲು ಕೆಲವು ಪ್ರಸಿದ್ಧ ಲೈಬ್ರರಿಗಳು ಇವೆ:

- **openai**, ಈ ಲೈಬ್ರರಿ ನಿಮ್ಮ ಮಾದರಿಯನ್ನು ಸಂಪರ್ಕಿಸಲು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್ ಕಳುಹಿಸಲು ಸುಲಭ.

ನಂತರ ಹೆಚ್ಚಿನ ಮಟ್ಟದ ಲೈಬ್ರರಿಗಳು ಇವೆ:

- **Langchain**. Langchain ಅವರನ್ನು Python ಗೆ ಬೆಂಬಲಿಸುವ ಪ್ರಸಿದ್ದ ಲೈಬ್ರರಿ.
- **Semantic Kernel**. Semantic Kernel ಎಂಬುದು Microsoft ರಿಂದ ಲೈಬ್ರರಿ, C#, Python ಮತ್ತು Java ಭಾಷೆಗಳಿಗೆ ಬೆಂಬಲ.

## openai ಬಳಸಿ ಮೊದಲ ಆಪ್

ಹೇಗೆ ನಾವು ನಮ್ಮ ಮೊದಲ ಆಪ್ ನಿರ್ಮಿಸುವುದು, ಯಾವ ಲೈಬ್ರರಿಗಳನ್ನು ಬೇಕಾಗುತ್ತದೆ, ಮತ್ತು ಇತರ ವಿವರಗಳನ್ನು ನೋಡೋಣ.

### openai ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ

OpenAI ಅಥವಾ Azure OpenAI ಜೊತೆ ಸಂವಹನಕ್ಕೆ ಅನೇಕ ಲೈಬ್ರರಿಗಳಿವೆ. C#, Python, JavaScript, Java ಸೇರಿದಂತೆ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಗಳು ಇವೆ. ನಾವು `openai` Python ಲೈಬ್ರರಿಯನ್ನು ఎంపికಮಾಡಿದ್ದೇವೆ, ಹಾಗಾಗಿ ನಾವು `pip` ಬಳಸಿ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡುತ್ತೇವೆ.

```bash
pip install openai
```

### ರಿಸೋರ್ಸ್ ಸೃಷ್ಟಿಸಿ

ನೀವು ಕೆಳಗಿನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಬೇಕು:

- [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst) ನಲ್ಲಿ ಅಕೌಂಟ್ ಸೃಷ್ಟಿಸಿ.
- Azure OpenAI ಗೆ ಪ್ರವೇಶ ಪಡೆಯಿರಿ. [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ಗೆ ಭೇಟಿ ನೀಡಿ ಪ್ರವೇಶ ಕೇಳಿ.

  > [!NOTE]
  > ಬರೆದಿರುವ ಸಂದರ್ಭದಲ್ಲಿ, ನೀವು Azure OpenAI ಗೆ ಪ್ರವೇಶಕ್ಕಾಗಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕಾಗಿದೆ.

- Python ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ <https://www.python.org/>
- Azure OpenAI ಸೇವಾ ಸಂಪನ್ಮೂಲ ಸೃಷ್ಟಿಸಿ. ಈ ಮಾರ್ಗದರ್ಶಿಯಲ್ಲಿ [create a resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) ನೋಡಿ.

### API ಕ್ಯೀ ಮತ್ತು ಎન્ડ್‌ಪಾಯಿಂಟ್ ಕಂಡುಹಿಡಿಯಿರಿ

ಈಗ, ನೀವು ನಿಮ್ಮ `openai` ಲೈಬ್ರರಿ ಯಾವ API ಕೀ ಬಳಸಬೇಕು ಎಂದು ಹೇಳಬೇಕು. API ಕೀ ಕಂಡುಹಿಡಿಯಲು, ನಿಮ್ಮ Azure OpenAI ಸಂಪನ್ಮೂಲದಲ್ಲಿ "Keys and Endpoint" ವಿಭಾಗಕ್ಕೆ ಹೋಗಿ "Key 1" ಅನ್ನು ನಕಲಿಸಿ.

![Azure Portal ನ Keys and Endpoint ಸಂಪನ್ಮೂಲ ಬ್ಲೇಡ್](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ಈಗ ನೀವು ಈ ಮಾಹಿತಿಯನ್ನು ನಕಲಿಸಿದ್ದೀರಿ, ಲೈಬ್ರರಿಗಳನ್ನು ಇದನ್ನು ಬಳಸುವಂತೆ ಸೂಚಿಸೋಣ.

> [!NOTE]
> ನಿಮ್ಮ API ಕೀ ಅನ್ನು ನಿಮ್ಮ ಕೋಡ್‌ನಿಂದ ವಿಭಜಿಸುವುದು ಬೆಲೆಗೆ ತಕ್ಕದ್ದು. ನೀವು ಪರಿಸರ ಪರಿವರ್ತಕರು ಬಳಸಿ ಹಾಗೆ ಮಾಡಬಹುದು.
>
> - ಪರಿಸರ ಪರಿವರ್ತಕ `OPENAI_API_KEY` ಅನ್ನು ನಿಮ್ಮ API ಕೀಗೆ ಸೆಟ್ ಮಾಡಿ.
>   `export OPENAI_API_KEY='sk-...'`

### Azure ಸಂರಚನೆ ಸ್ಥಾಪನೆ

ನೀವು Azure OpenAI (ಈಗ Microsoft Foundry ಭಾಗ) ಬಳಸುತ್ತಿದ್ದರೆ, ಈ ರೀತಿ ಸಂರಚನೆ ಮಾಡಿರಿ. ನಾವು ಮಾನ್ಯ `OpenAI` ಕ್ಲೈಂಟ್‌ನೊಂದಿಗೆ Azure OpenAI `/openai/v1/` ಎಂಡ್‌ಪಾಯಿಂಟ್‌ ಗೆ ಸೂಚಿಸುತ್ತೇವೆ, ಇದು Responses API ಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಮತ್ತು `api_version` ಬೇಕಾಗಿಲ್ಲ:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

ಮೇಲಿನಂತೆಯೇ ನಾವಿಂದು ಮುಂದಿನ ಅಂಶಗಳನ್ನು ಸೆಟ್ ಮಾಡುತ್ತೇವೆ:

- `api_key`, ಇದು ನಿಮ್ಮ API ಕೀ, Azure ಪೋರ್ಟಲ್ ಅಥವಾ Microsoft Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿರುವುದು.
- `base_url`, ಇದು ನೀವು ಹೊಂದಿರುವ Foundry ಸಂಪನ್ಮೂಲ ಎಂಡ್‌ಪಾಯಿಂಟ್, `/openai/v1/` ಸೇರಿಸಲಾಗಿದೆ. ಸ್ಥಿರ v1 ಎಂಡ್‌ಪಾಯಿಂಟ್ OpenAI ಹಾಗೂ Azure OpenAI ಎರಡರಲ್ಲಿಯೂ ಕೆಲಸ ಮಾಡುತ್ತದೆ, `api_version` ಹೊಂದಾಣಿಕೆಯಾಗುವುದಿಲ್ಲ.

> [!NOTE] > `os.environ` ಪರಿಸರ ಪರಿವರ್ತಕಗಳನ್ನು ಓದಿ ಬಹುದು. ಉದಾಹರಣೆಗೆ `AZURE_OPENAI_API_KEY` ಮತ್ತು `AZURE_OPENAI_ENDPOINT`. ಈ ಪರಿಸರ ಮೌಲ್ಯಗಳನ್ನು ಟೆರ್ಮಿನಲ್‌ನಲ್ಲಿ ಅಥವಾ `dotenv` ಲೈಬ್ರರಿ ಮೂಲಕ ಸೆಟ್ ಮಾಡಿ.

## ಪಠ್ಯ ರಚನೆ

ಪಠ್ಯ ರಚಿಸಲು Responses API ಅನ್ನು `responses.create` ವಿಧಾನದಿಂದ ಉಪಯೋಗಿಸಬಹುದು. ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # ಇದು ನಿಮ್ಮ ಮಾದರಿ ನಿಯೋಜನೆಯ ಹೆಸರು
    input=prompt,
    store=False,
)
print(response.output_text)
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ, ನಾವು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ರಚಿಸಿ ಬಳಸಲು ಬೇಕಾದ ಮಾದರಿ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್ ಪಾಸು ಮಾಡುತ್ತೇವೆ. ನಂತರ `response.output_text` ಮೂಲಕ ರಚಿಸಿದ ಪಠ್ಯವನ್ನು ಮುದ್ರಿಸುತ್ತದೆ.

### ಅನೇಕರ ಚರ್ಚೆಗಳು

Responses API ಒಂದು ಬಾರಿ ಪಠ್ಯ ರಚನೆಗೆ ಮತ್ತು ಬಹು-ಮೂಲೆ ಚಾಟ್ ಬಾಟ್‌ಗಳಿಗೆ ಒಳ್ಳೆಯದು - ನೀವು ಸಂಭಾಷಣೆ ನಿರ್ಮಿಸಲು `input` ನಲ್ಲಿ ಸಂದೇಶಗಳ ಪಟ್ಟಿ ನೀಡುತ್ತೀರಿ:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

ಈ ಕಾರ್ಯಚಟುವಟಿಕೆಗಳ ಬಗ್ಗೆ ಮುಂದಿನ ಅಧ್ಯಾಯದಲ್ಲಿ ಹೆಚ್ಚು ವಿವರ.

## ವ್ಯಾಯಾಮ - ನಿಮ್ಮ ಪ್ರಥಮ ಪಠ್ಯ ತಯಾರಿಕೆಯ ಆಪ್

openai ಅನ್ನು ಹೇಗೆ ಸಂರಚಿಸುವುದು ಮತ್ತು ಸ್ಥಾಪಿಸುವುದು ಕಲಿತ ನಂತರ, ನಿಮ್ಮ ಪ್ರಥಮ ಪಠ್ಯ ತಯಾರಿಕೆಯ ಆಪ್ ನಿರ್ಮಿಸುವ ಸಮಯ ಬಂದಿದೆ. ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ:

1. ವರ್ಚುವಲ್ ಪರಿಸರ ಸೃಷ್ಟಿಸಿ ಮತ್ತು openai ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > ನೀವು Windows ಬಳಸುತ್ತಿದ್ದರೆ `source venv/bin/activate` ಬದಲು `venv\Scripts\activate` ಟೈಪ್ ಮಾಡಿ.

   > [!NOTE]
   > ನಿಮ್ಮ Azure OpenAI ಕೀ ಹುಡುಕಲು [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ಗೆ ಹೋಗಿ, `Open AI` ಹುಡುಕಿ, `Open AI resource` ಆಯ್ಕೆಮಾಡಿ, ನಂತರ `Keys and Endpoint` ನಲ್ಲಿ `Key 1` ನಕಲಿಸಿ.

1. _app.py_ ಫೈಲ್ ಸೃಷ್ಟಿಸಿ ಮತ್ತು ಕೆಳಗಿನ ಕೋಡ್ ನೀಡಿರಿ:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # ನಿಮ್ಮ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API ಬಳಸಿ ವಿನಂತಿಯನ್ನು ಮಾಡಿ
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಮುದ್ರಿಸಿ
   print(response.output_text)
   ```

   > [!NOTE]
   > ನೀವು ಸಾದಾಸುಲಭ OpenAI ಬಳಸುತ್ತಿದ್ದರೆ (Azure ಅಲ್ಲ), `client = OpenAI(api_key="<replace this value with your OpenAI key>")` ( `base_url` ಇಲ್ಲ) ಬಳಸಿ, ಮತ್ತು ಮಾದರಿ ಹೆಸರಾಗಿ `gpt-4o-mini` ಅಥವಾ ಇತರ ನೇಮಿಸಿ.

   ನೀವು ಕೆಳಗಿನಂತೆ output ಕಾಣಬಹುದು:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ವಿವಿಧ ರೀತಿಯ ಪ್ರಾಂಪ್ಟ್ಗಳು, ವಿಭಿನ್ನ ಕಾರ್ಯಗಳಿಗಾಗಿ

ಈಗ ನೀವು ಪ್ರಾಂಪ್ಟ್ ಬಳಸಿ ಪಠ್ಯ ರಚಿಸುವುದು ಹೇಗೆ ಎಂಬುದನ್ನು ನೋಡಿದ್ದೀರಿ. ನೀವು ಈ ಪ್ರೋಗ್ರಾಂ ಅನ್ನು ಬದಲಾಯಿಸಿ ವಿಭಿನ್ನ ವಿಧದ ಪಠ್ಯ ತಯಾರಿಸಬಹುದು.

ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಎಲ್ಲಾ ರೀತಿಯ ಕಾರ್ಯಗಳಿಗಾಗಿ ಬಳಸಬಹುದು. ಉದಾಹರಣೆಗಾಗಿ:

- **ಪಠ್ಯದ ಒಂದು ವಿಧ ರಚಿಸಿ**. ಉದಾಹರಣೆಗೆ, ಕವಿತೆ, ಪ್ರಶ್ನೆ ಪತ್ರಿಕೆ.
- **ಮಾಹಿತಿ ಹುಡುಕಿ**. ಉದಾಹರಣೆಗೆ, 'ವೆಬ್ ಡೆವಲಪ್‌ಮೆಂಟ್ನಲ್ಲಿ CORS ಎಂದರೇನು?' ಎಂದು.
- **ಕೋಡ್ ರಚಿಸಿ**. ಉದಾಹರಣೆಗೆ, ಇಮೇಲ್ ಪರಿಶೀಲನೆಗೆ ನಿಯಮಬದ್ಧ ಅಭಿವ್ಯಕ್ತಿ ಬರೆಯುವುದು ಅಥವಾ ಸಂಪೂರ್ಣ ವೆಬ್ ಆಪ್ ರಚಿಸುವುದು.

## ಹೆಚ್ಚು ಪ್ರಾಯೋಗಿಕ ಬಳಕೆ: ಒಂದು ರೆಸಿಪಿ ಜನರೇಟರ್

ನೀವು ಮನೆಯಲ್ಲಿರುವ ಪದಾರ್ಥಗಳನ್ನು ಹೊಂದಿದ್ದೀರಾ ಮತ್ತು ಬೇಕಾದರೆ ಯಾವುದಾದರೂ ವಾಂಕ್ಷಿತ ಅಡುಗೆ ಮಾಡಿ ನೋಡಬೇಕೆಂದುಕೊಳ್ಳಿ. ಅದಕ್ಕಾಗಿ ನಿಮಗೆ ರೆಸಿಪಿ ಬೇಕಾಗುತ್ತದೆ. ರೆಸಿಪಿಗಳನ್ನು ಹುಡುಕಲು ಸರ್ಚ್ ಎಂಜಿನ್ ಬಳಸಬಹುದು ಅಥವಾ LLM ಬಳಸಿ.

ನೀವು ಈ ರೀತಿಯ ಪ್ರಾಂಪ್ಟ್ ಬರೆಯಬಹುದು:

> "ಈ ಪದಾರ್ಥಗಳೊಂದಿಗೆ (ಕೋಳಿ, ಬಟಾಟೆ, ಕ್ಯಾರೆಟ್) 5 ರೆಸಿಪಿಗಳನ್ನು ತೋರಿಸಿ. ಪ್ರತಿಯೊಂದು ರೆಸಿಪಿಗೂ ಬಳಕೆಯಾದ ಎಲ್ಲ ಪದಾರ್ಥಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ"

ಮೇಲಿನ ಪ್ರಾಂಪ್ಟ್ ಆಧಾರವಾಗಿ ನೀವು ಈಂತಹ ಉತ್ತರ ಪಡೆಯಬಹುದು:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

ಇದು ಅದ್ಭುತ. ನಾನು ಏನು ಅಡುಗೆ ಮಾಡಬೇಕು ಎಂದು ಗೊತ್ತಾಯಿತು. ಈಗ ಉತ್ತಮಗೊಳಿಸಲು ಏನು ಬೇಕು ಎಂದರೆ:

- ನಾನು ಇಚ್ಛಿಸುವ ಅಥವಾ ಅಲರ್ಜಿ ಇರುವ ಪದಾರ್ಥಗಳನ್ನು ತೊರೆಯುವುದು.
- ಹೀಗಾದರೆ, ಮನೆಯಲ್ಲಿಲ್ಲದ ಪದಾರ್ಥಗಳಿಗೆ ಶಾಪಿಂಗ್ ಪಟ್ಟಿಯನ್ನು ರಚಿಸುವುದು.

ಈ ಪ್ರಕರಣಗಳಿಗೆ ಮತ್ತೆ ಒಂದು ಪ್ರಾಂಪ್ಟ್ ಸೇರಿಸಿ:

> "ನನಗೆ ಅಲರ್ಜಿ ಇರುವ ಕಾರಣ, ಲೂಳುಹಣಿಯನ್ನು ಹೊಂದಿರುವ ರೆಸಿಪಿಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ಬದಲಿಗೆ ಬೇರೆ ಏನಾದರೂ ಸೇರಿಸಿ. ಹೆಚ್ಚಾಗಿ, ದಯವಿಟ್ಟು ರೆಸಿಪಿಗಳಿಗಾಗಿ ಶಾಪಿಂಗ್ ಪಟ್ಟಿಯನ್ನು ರಚಿಸಿ, ನಾನು ಈಗಾಗಲೇ ಕೋಳಿ, ಬಟಾಟೆ ಮತ್ತು ಕ್ಯಾರೆಟ್‌ಗಳನ್ನು ಹೊಂದಿದ್ದೇನೆ."

ಇಗೋ ಹೊಸ ಫಲಿತಾಂಶ ಈ ಕೆಳಗಿನಂತೆ:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

ಅದು ನಿಮ್ಮ ಐದು ರೆಸಿಪಿಗಳು, ಲೂಳಿಹಣಿ ತೆಗೆದುಹಾಕಲಾಗಿದ್ದು, ಮೀಸಲಾಗಿರುವ ಪದಾರ್ಥಗಳ ಮಾಹಿತಿ ಹಾಗು ಶಾಪಿಂಗ್ ಪಟ್ಟಿಯೊಂದಿಗೆ.

## ವ್ಯಾಯಾಮ - ರೆಸಿಪಿ ಜನರೇಟರ್ ನಿರ್ಮಿಸಿ

ಈಗ ನಾವು ಸನ್ನಿವೇಶ ನಡೆಸಿದಂತೆ, ಅದಕ್ಕೆ ಹೊಂದುವ ಕೋಡ್ ಬರೆದುಕೊಳ್ಳೋಣ. ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ:

1. ಇದ್ದ _app.py_ ಫೈಲ್ ಅನ್ನು ಪ್ರಾರಂಭಿಕ ಸ್ಥಾನವಾಗಿ ಉಪಯೋಗಿಸಿ
1. `prompt` ಎಂದು ಹೆಸರಿಸಲಾದ ವ್ಯತ್ಯಯದ ಕೋಡ್ ಅನ್ನು ಕೆಳಗಿನಂತೆ ಬದಲಾಯಿಸಿ:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ಈಗ ನೀವು ಈ ಕೋಡ್ ರನ್ ಮಾಡಿದರೆ, ಇದೇಂತಹ output ಕಾಣಬಹುದು:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ಗಮನಿಸಿ, ನಿಮ್ಮ LLM ನಿರ್ದಿಷ್ಟವಾಗಿಲ್ಲದದ್ದು, ಪ್ರತಿ ಬಾರಿ ವಿಭಿನ್ನ ಫಲಿತಾಂಶ ಬರುತ್ತದೆ.

   ಅದ್ಭುತ, ನಾವು ಇನ್ನಷ್ಟು ಸುಧಾರಿಸೋಣ. ಸುಧಾರಿಸಲು, ಕೋಡ್ ಲವಚಿಕವಾಗಿರುವುದು ಮುಖ್ಯ, ಅಂದರೆ ಪದಾರ್ಥಗಳು ಮತ್ತು ರೆಸಿಪಿಗಳ ಸಂಖ್ಯೆ ಬದಲಾಯಿಸಬಹುದು.

1. ಮುಂದಿನ ರೀತಿಯಲ್ಲಿ ಕೋಡ್ ಬದಲಾಯಿಸೋಣ:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # ಪಾಕವಿಧಾನಗಳ ಸಂಖ್ಯೆಯನ್ನು ಪ್ರಾಂಪ್ಟ್ ಮತ್ತು ಪದಾರ್ಥಗಳಲ್ಲಿ ಅಂತರಪ್ರವೇಸಿಸಲು
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ಈ ಕೋಡ್‌ನೊಂದಿಗೆ ಪರೀಕ್ಷಾ ಚಲಾವಣೆ ಇಂಥದ್ದಾಗಬಹುದು:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ಫಿಲ್ಟರ್ ಹಾಗೂ ಶಾಪಿಂಗ್ ಲಿಸ್ಟ್ சேரಿಸುವ ಮೂಲಕ ಸುಧಾರಣೆ

ಈಗ ನಮ್ಮ ಬಳಿ ಒಂದು ಕಾರ್ಯನಿರತ ಆಪ್ ಇದೆ, ಇದು ರೆಸಿಪಿಗಳನ್ನು ರಚಿಸಲು ಸಹಾಯಕವಾಗಿದೆ ಮತ್ತು ಬಳಕೆದಾರನಿಂದ ಪದಾರ್ಥ ಹಾಗೂ ರೆಸಿಪಿಗಳ ಸಂಖ್ಯೆ ಪಡೆಯುತ್ತಾ ಲವಚಿಕವಾಗಿದೆ.

ಇನ್ನಷ್ಟು ಸುಧಾರಣೆಗಾಗಿ, ನಾವು ಕೆಳಗಿನ ಅಂಶಗಳನ್ನು ಸೇರಿಸಬೇಕು:

- **ಪದಾರ್ಥಗಳನ್ನು ಫಿಲ್ಟರ್ ಮಾಡಿ**. ನಾವು ಇಚ್ಛಿಸದ ಅಥವಾ ಅಲರ್ಜಿ ಇರುವ ಪದಾರ್ಥಗಳನ್ನು ಬೇಡ, ಅದಕ್ಕಾಗಿ ಪ್ರಾಂಪ್ಟ್‌ನ ಕೊನೆಯಲ್ಲಿ ಫಿಲ್ಟರ್ ಅರ್ಹತೆಯನ್ನು ಸೇರಿಸೋಣ.

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ಮೇಲ್ನೋಟದಲ್ಲಿ, ನಾವು ಪ್ರಾಂಪ್ಟ್ ಕೊನೆಯಲ್ಲಿ `{filter}` ಸೇರಿಸಿದ್ದೇವೆ ಮತ್ತು ಬಳಕೆದಾರನಿಂದ ಫಿಲ್ಟರ್ ಮೌಲ್ಯವನ್ನು ಏರಿಸಿಕೊಂಡಿದ್ದೇವೆ.

  ಕಾರ್ಯಕ್ರಮ ಚಲಾಯಿಸಿದ ಉದಾಹರಣೆಯೊಂದು ಇಂತೇ:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  ನೀವು ನೋಡುತ್ತೀರಿ, ಹಾಲು ಬಳಕೆಯಾದ ಯಾವುದೇ ರೆಸಿಪಿಯನ್ನು ಫಿಲ್ಟರ್ ಮಾಡಲಾಗಿದೆ. ಆದರೆ, ನೀವು ಲ್ಯಾಕ್ಟೋಸ್ ಅಸಹಿಷ್ಣುತೆಯಿದ್ದರೆ, ಚೀಸ್ ಇರುವ ರೆಸಿಪಿಗಳನ್ನು ಕೂಡ ತೆಗೆದುಹಾಕಬೇಕಾಗಬಹುದು; ಆದ್ದರಿಂದ ಸ್ಪಷ್ಟತೆ ಬೇಕಾಗುತ್ತದೆ.


- **ಖರೀದಿ ಪಟ್ಟಿ ತಯಾರು ಮಾಡು**. ನಾವು ಮನೆಯಲ್ಲಿರುವುದನ್ನು ಪರಿಗಣಿಸಿ ಖರೀದಿ ಪಟ್ಟಿಯನ್ನು ತಯಾರಿಸಲು ಬಯಸುತ್ತೇವೆ.

  ಈ ಕಾರ್ಯक्षमತೆಯಿಗಾಗಿ, ನಾವು ಎಲ್ಲವನ್ನೂ ಒಂದು ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ಪರಿಹರಿಸಲು ಪ್ರಯತ್ನಿಸಬಹುದು ಅಥವಾ ಎರಡು ಪ್ರಾಂಪ್ಟ್‌ಗಳಾಗಿ ವಿಭಜಿಸಬಹುದು. ಎರಡನೆದನ್ನು ಪ್ರಯತ್ನಿಸೋಣ. ಇಲ್ಲಿ ನಾವು ಹೆಚ್ಚುವರಿ ಪ್ರಾಂಪ್ಟ್ ಸೇರಿಸುವುದಾಗಿ ಸೂಚಿಸುತ್ತಿದ್ದೇವೆ, ಆದರೆ ಅದಕ್ಕಾಗಿ, ನಾವು ಮೊದಲ ಪ್ರಾಂಪ್ಟ್‌ನ ಫಲಿತಾಂಶವನ್ನು ನಂತರದ ಪ್ರಾಂಪ್ಟ್‌ಗೆ ಪ್ರಸಂಗವಾಗಿ ಸೇರಿಸಬೇಕಾಗುತ್ತದೆ.

  ಮೊದಲ ಪ್ರಾಂಪ್ಟ್‌ನ ಫಲಿತಾಂಶವನ್ನು ಮುದ್ರಿಸುವ ಭಾಗವನ್ನು ಕೋಡ್‌ನೊಳಗೆ ಹುಡುಕಿ ಮತ್ತು ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಮುದ್ರಿಸಿ
  print("Shopping list:")
  print(response.output_text)
  ```

  ಕೆಳಗಿನ ಕುರಿತು ಗಮನಿಸಿ:

  1. ನಾವು ಮೊದಲ ಪ್ರಾಂಪ್ಟ್‌ನ ಫಲಿತಾಂಶವನ್ನು ಹೊಸ ಪ್ರಾಂಪ್ಟ್‌ಗೆ ಸೇರಿಸುವ ಮೂಲಕ ಹೊಸ ಪ್ರಾಂಪ್ಟ್ ರಚಿಸುತ್ತಿದ್ದೇವೆ:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. ನಾವು ಹೊಸ ವಿನಂತಿ ಮಾಡುತ್ತೇವೆ, ಆದರೆ ಮೊದಲ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ನಾವು ಕೇಳಿದ ಟೋಕನ್ ಗಳ ಸಂಖ್ಯೆಯನ್ನೂ ಪರಿಗಣಿಸುತ್ತೇವೆ, ಆದ್ದರಿಂದ ಈ ಬಾರಿ ನಮಗೆ `max_output_tokens` 1200 ಎಂದು ಹೇಳಲಾಗಿದೆ.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ಈ ಕೋಡ್ ಅನ್ನು ಚಲಾಯಿಸಿ, ನಾವು ಕೆಳಗಿನ output ಅನ್ನು ಪಡೆಯುತ್ತೇವೆ:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## ನಿಮ್ಮ ವ್ಯವಸ್ಥೆಯನ್ನು ಸುಧಾರಿಸಿ

ಇದുവരെ ನಾವು ಹೊಂದಿರುವ ಕೋಡ್ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ, ಆದರೆ ಇನ್ನಷ್ಟು ಸುಧಾರಣೆ ಮಾಡಲು ಕೆಲವು ಸಲಹೆಗಳು ಇರುತ್ತವೆ. ಕೆಲವು ಕಾರ್ಯಗಳನ್ನು ನಾವು ಮಾಡಬೇಕು:

- **ರಹಸ್ಯಗಳನ್ನು ಕೋಡ್‌ನಿಂದ ಬೇರ್ಪಡಿಸಿ**, ಉದಾಹರಣೆಗೆ API ಕೀ. ರಹಸ್ಯಗಳು ಕೋಡ್‌ನಲ್ಲಿ ಇರಬಾರದು ಮತ್ತು ಸುರಕ್ಷಿತ ವಾತಾವರಣದಲ್ಲಿ ಉಳಿಸಬೇಕು. ರಹಸ್ಯಗಳನ್ನು ಕೋಡ್‌ನಿಂದ ಬೇರ್ಪಡಿಸಲು ನಾವು ಪರಿಸರ ಚರಗಳನ್ನು (environment variables) ಮತ್ತು `python-dotenv` ತರಹದ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಬಳಸಬಹುದು. ಇದರ ಉದಾಹರಣೆ ಹೀಗಿರಬಹುದು:

  1. `.env` ಎಂಬ ಫೈಲ್ ಅನ್ನು ಕೆಳಗಿನ ವಿಷಯದೊಂದಿಗೆ ರಚಿಸಿ:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Microsoft Foundry ನ Azure OpenAI ಗೆ, ನೀವು ಬದಲಾಗಿ ಕೆಳಗಿನ ಪರಿಸರ ಚರಗಳನ್ನು ಹೊಂದಿಸಬೇಕು:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     ಕೋಡ್‌ನಲ್ಲಿ, ನೀವು ಪರಿಸರ ಚರಗಳನ್ನು ಹೀಗೆ ಲೋಡ್ ಮಾಡುತ್ತೀರಿ:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **ಟೋಕನ್ ಉದ್ದದ ಬಗ್ಗೆ ಒಂದು ಮಾತು**. ನಾವು ಬೇಕಾದ ಪಠ್ಯವನ್ನು ಉತ್ಪಾದಿಸಲು ಎಷ್ಟು ಟೋಕನ್ ಅಗತ್ಯವಿದೆ ಎಂಬುದನ್ನು ಪರಿಗಣಿಸಬೇಕು. ಟೋಕನ್‌ಗಳು ಖರ್ಚಾಗುತ್ತವೆ, ಆದ್ದರಿಂದ ಸಾಧ್ಯವಾದಷ್ಟು ಕಡಿಮೆ ಟೋಕನ್ ಬಳಿಸಬೇಕು. ಉದಾಹರಣೆಗೆ, ನಾವು ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಇಷ್ಟು ಸರಳವಾಗಿ ಬರೆಯಬಹುದೆಂದು ಪರಿಶೀಲಿಸಿ.

  ಟೋಕನ್‌ಗಳ ಬಳಕೆಯನ್ನು ಬದಲಾಯಿಸಲು, ನೀವು `max_output_tokens` ಪರಿಮಾಣವನ್ನು ಬಳಸಬಹುದು. ಉದಾಹರಣೆಗೆ, ನೀವು 100 ಟೋಕನ್ ಬಳಸಲು ಬಯಸಿದರೆ, ನೀವು ಹೀಗೆ ಮಾಡಬಹುದು:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **ತೆಂಪರೇಚರ್‌ನಲ್ಲಿ ಪ್ರಯೋಗಗಳು**. ತೆಂಪರೇಚರ್ ಎಂದರೆ ನಾವು ಈಗಾಗಲೇ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳದ ಸಂಗತಿಯಾಗಿದೆ ಆದರೆ ನಮ್ಮ ಕಾರ್ಯಕ್ರಮ ಪ್ರದರ್ಶನದ ಪಾರ್ಶ್ವಭಾಗವಾಗಿದೆ. ಹೆಚ್ಚಿನ ತೆಂಪರೇಚರ್ ಮೌಲ್ಯವು ಹೆಚ್ಚು ಅನಿಯಮಿತ ಫಲಿತಾಂಶವನ್ನು ನೀಡುತ್ತದೆ. ಕಡಿಮೆ ತೆಂಪರೇಚರ್ ಮೌಲ್ಯವು ಹೆಚ್ಚು ಮುಂಬರುವ ಫಲಿತಾಂಶ ನೀಡುತ್ತದೆ. ನಿಮ್ಮ output ನಲ್ಲಿ ವ್ಯತ್ಯಾಸ ಬೇಕೋ ಇಲ್ಲವೋ ಎಂಬುದನ್ನು ಪರಿಗಣಿಸಿ.

  ತೆಂಪರೇಚರ್ ನಂವನ್ನು ಬದಲಾಯಿಸಲು, ನೀವು `temperature` ಪರಿಮಾಣವನ್ನು ಬಳಸಬಹುದು. ಉದಾಹರಣೆಗೆ, 0.5 ತೆಂಪರೇಚರ್ ಬಳಸಲು ಬಯಸಿದರೆ, ನೀವು ಹೀಗೆ ಮಾಡಬಹುದು:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ಗಮನಿಸಿ, 1.0 ಗೆ càng ಸರಿಯುತ್ತಿದ್ದಂತೆ, output ಹೆಚ್ಚು ವೈವಿಧ್ಯತೆಯಾಗುತ್ತದೆ.

## ಹಂಚಿಕೆ

ಈ ಹಂಚಿಕೆಗೆ, ನೀವು ಏನು ನಿರ್ಮಿಸಬೇಕೆಂದು ಆರಿಸಬಹುದು.

ಇಲ್ಲಿವೆ ಕೆಲವು ಸಲಹೆಗಳು:

- ರೆಸಿಪಿ ಜನರೇಟರ್ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಇನ್ನಷ್ಟು ಸುಧಾರಿಸಿ; ತೆರಂಪರೆಚಾರ್ ಮೌಲ್ಯಗಳೊಂದಿಗೆ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳೊಂದಿಗೆ ಆಟವಾಡಿ, ನೀವು ಏನು ಮಾಡಬಹುದು ನೋಡಿ.
- "ಸ್ಟಡಿ ಬಡ್ಡಿ" ತಯಾರಿಸಿ. ಈ ಅಪ್ಪ್ ಒಂದು ವಿಷಯದ ಬಗ್ಗೆ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರವಿಡಲು ಸಾಧ್ಯವಾಗಬೇಕು, ಉದಾಹರಣೆಗೆ Python. ನೀವು "Python ನಲ್ಲಿ ಕೆಲ ಪ್ರಮುಖ ವಿಷಯವೇನು?" ಫೋರ್ ಇತ್ಯಾದಿ ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಇರಬಹುದು, ಅಥವಾ ನಿಮಗೆ ಒಂದು ಸಂಗತಿಯಿಂದ ಸಂಬಂಧಿಸಿದ ಕೋಡ್ ತೋರಿಸು ಎಂದು ಕೇಳಬಹುದು.
- ಹಿಸ್ಟರಿ ಬಾಟ್, ಇತಿಹಾಸವನ್ನು ಜೀವಂತಗೊಳಿಸು, ಬಾಟ್‌ಗೆ ಒಂದು ಇತಿಹಾಸಮಯ ವ್ಯಕ್ತಿತ್ವವನ್ನು ವಿಧಿಸಿ ಮತ್ತು ಅದರ ಜೀವನ ಮತ್ತು ಕಾಲದ ಬಗ್ಗೆ ಪ್ರಶ್ನೆ ಕೇಳಿ.

## ಪರಿಹಾರ

### ಸ್ಟಡಿ ಬಡ್ಡಿ

ಕೆಳಗೆ ಸ್ಟಾರ್ಟರ್ ಪ್ರಾಂಪ್ಟ್ ಇದೆ, ಅದನ್ನು ನೀವು ಹೇಗೆ ಉಪಯೋಗಿಸಬಹುದು ಮತ್ತು ನಿಮ್ಮ ಇಚ್ಛೆಯಂತೆ ಹೇಗೆ ಬದಲಾಯಿಸಬಹುದು ನೋಡಿ.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ಹಿಸ್ಟರಿ ಬಾಟ್

ನೀವು ಬಳಸಬಲ್ಲ ಕೆಲ ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಇಲ್ಲಿವೆ:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ತಿಳುವಳಿಕೆ ಪರೀಕ್ಷೆ

ತೆಂಪರೇಚರ್ ಸಂಯೋಜನೆಯು ಏನು ಮಾಡುತ್ತದೆ?

1. ಇದು output ಎಷ್ಟು ಅನಿಯಮಿತವಾಗಿರುತ್ತದೆಯೆಂಬುದನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ.
1. ಇದು ಪ್ರತಿಕ್ರಿಯೆ ಎಷ್ಟು ದೊಡ್ಡದಾಗಿರುತ್ತದೆಯೆನ್ನುವುದನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ.
1. ಇದು ಎಷ್ಟು ಟೋಕನ್‌ಗಳು ಬಳಕೆಯಾಗುತ್ತವೆಂಬುದನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ.

## 🚀 ಸವಾಲ್

ಹಂಚಿಕೆಯನ್ನು ಕೆಲಸ ಮಾಡುವಾಗ, ತೆಂಪರೇಚರ್ ಮೌಲ್ಯವನ್ನು ಬದಲಾಯಿಸುವುದನ್ನು ಪ್ರಯತ್ನಿಸಿ, 0, 0.5, ಮತ್ತು 1 ಗೆ ಹೊಂದಿಸುವುದನ್ನು ಪ್ರಯತ್ನಿಸಿ. 0 ಕನಿಷ್ಠ ವೈವಿಧ್ಯಮಯ ಮತ್ತು 1 ಅತ್ಯಧಿಕ ವೈವಿಧ್ಯಮಯ. ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ಯಾವ ಮೌಲ್ಯ ಉತ್ತಮ ಕೆಲಸ ಮಾಡುತ್ತದೆ ನೋಡಿ.

## ಒಳ್ಳೆಯ ಕೆಲಸ! ನಿಮ್ಮ ಕಲಿಕೆಯನ್ನು ಮುಂದುವರೆಸಿ

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನಮ್ಮ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ಅನ್ನು ಪರಿಶೀಲಿಸಿ ನಿಮ್ಮ ಜನರೇಟಿವ್ AI ಜ್ಞಾನವನ್ನು ಮುಂದುವರೆಸಿ!

ಪಾಠ 7 ಗೆ ಹೋಗಿ ನಾವು ಹೇಗೆ [ಚಾಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) ನೋಡೋಣ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->