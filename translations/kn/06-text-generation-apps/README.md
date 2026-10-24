# ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್ಗಳ ನಿರ್ಮಾಣ

[![ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್ಗಳ ನಿರ್ಮಾಣ](../../../translated_images/kn/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ಈ ಪಾಠದ ವಿಡಿಯೋವನ್ನು ನೋಡಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

ಈ ಪಠ್ಯಕ್ರಮದ ಮೂಲಕ ನೀವು ಇದುವರೆಗೆ ಕಂಡಿರುವುದು ಪ್ರಾಂಪ್ಟ್ಗಳು ಮತ್ತು "ಪ್ರಾಂಪ್ಟ್ ಇಂಜಿನಿಯರಿಂಗ್" ಎಂಬ ಒಂದು ಸಂಪೂರ್ಣ ಶಾಖೆಯಂತಹ ಮೂಲಭೌತ ಕಲ್ಪನೆಗಳು ಇದ್ದವೆ. ನೀವು ಚಾಟ್‌ಜಿಪಿಟಿ, ಆಫೀಸ್ 365, ಮೈಕ್ರೋಸಾಫ್ಟ್ ಪವರ್ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಮತ್ತು ಇತರ ಹಲವಾರು ಸಾಧನಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಬಹುದು, ಅವು ಪ್ರಾಂಪ್ಟ್ಗಳನ್ನು ಬಳಸಿ ಏನಾದರು ಸಾಧಿಸಲು ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತವೆ.

ನೀವು ಇಂತಹ ಅನುಭವವನ್ನು ಯಾವುದೇ ಅಪ್ಪಿಗೆ ಸೇರಿಸಲು, ಪ್ರಾಂಪ್ಟ್, ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಗಳಂತಹ ಕಲ್ಪನೆಗಳನ್ನು ತಿಳಿದುಕೊಳ್ಳಬೇಕು ಮತ್ತು ಕಾರ್ಯನಿರ್ವಹಿಸಲು ಒಂದು ಲೈಬ್ರರಿ ಆಯ್ಕೆ ಮಾಡಬೇಕು. ಇದೇ ನಿಮಗೆಈ ಅಧ್ಯಾಯದಲ್ಲಿ ಕಲಿಯಬೇಕಾಗಿರುವುದು.

## ಪರಿಚಯ

ಈ ಅಧ್ಯಾಯದಲ್ಲಿ, ನೀವು:

- openai ಲೈಬ್ರರಿ ಮತ್ತು ಅದರ ಮೂಲಭೂತ ಕಲ್ಪನೆಗಳ ಬಗ್ಗೆ ತಿಳಿಯಿರಿ.
- openai ಬಳಸಿ ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್ ರಚನೆಯು ಮಾಡಿ.
- ಪ್ರಾಂಪ್ಟ್, ತಾಪಮಾನ ಮತ್ತು ಟೋಕನ್ಸ್ (tokens)ಗಳಂತಹ ಕಲ್ಪನೆಗಳನ್ನು ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸಲು ಹೇಗೆ ಬಳಸಬೇಕೆಂದು ತಿಳಿಯಿರಿ.

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠದ ಕೊನೆಯಲ್ಲಿ, ನೀವು:

- ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್ ಎಂದರೇನು ಎಂಬುದನ್ನು ವಿವರಿಸಬಹುದು.
- openai ಬಳಸಿ ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸಬಹುದು.
- ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಹೆಚ್ಚುವರಿ ಅಥವಾ ಕಡಿಮೆ ಟೋಕನ್ಸ್ ಬಳಸಿ ಮತ್ತು ತಾಪಮಾನ ಬದಲಾಯಿಸಿ ವಿವಿಧ ಫಲಿತಾಂಶಗಳಿಗಾಗಿ ಹೊಂದಿಸಬಹುದು.

## ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್ ಎಂದರೇನು?

ಸಾಮಾನ್ಯವಾಗಿ ನೀವು ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸುವಾಗ, ಅದು ಕೆಲ ರೀತಿ ಇಂಟರ್ಫೇಸ್ ಇರುತ್ತದೆ, ಹೀಗಿದೆ:

- ಕಮಾಂಡ್ ಆಧಾರಿತ. ಕನ್ಸೋಲ್ ಅಪ್ಲಿಕೇಶನ್ಗಳು ಸಾಮಾನ್ಯವಾಗಿದ್ದು ನೀವು ಕಮಾಂಡ್ ಟೈಪ್ ಮಾಡಿದರೆ ಅದು ಕಾರ್ಯವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. ಉದಾಹರಣೆಗೆ, `git` ಒಂದು ಕಮಾಂಡ್ ಆಧಾರಿತ ಅಪ್ಲಿಕೇಶನ್.
- ಬಳಕೆದಾರ ಇಂಟರ್ಫೇಸ್ (UI). ಕೆಲವು ಅಪ್ಲಿಕೇಶನ್ಗಳಿಗೆ ಗ್ರಾಫಿಕಲ್ ಬಳಕೆದಾರ ಇಂಟರ್ಫೇಸ್ (GUI) ಇರುತ್ತವೆ, ಅಲ್ಲಿ ನೀವು ಬಟನ್ಗಳನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ, ಪಠ್ಯವನ್ನು ನಮೂದಿಸಿ, ಆಯ್ಕೆಮಾಡಿ ಇತ್ಯಾದಿ ಮಾಡಬಹುದು.

### ಕನ್ಸೋಲ್ ಮತ್ತು UI ಅಪ್ಲಿಕೇಶನ್ಗಳು ಸೀಮಿತವಾಗಿವೆ

ನೀವು ಕಮಾಂಡ್ ಆಧಾರಿತ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ಮಾತ್ರ ಬರೆಸಿದಂತೆ ಕಮಾಂಡ್ ಬಳಸಬಹುದು ಎಂದು ಹೋಲಿಸಿ:

- **ಇದು ಸೀಮಿತವಾಗಿದೆ**. ನೀವು ಯಾವುದೇ ಕಮಾಂಡ್ type ಪಡೆದಿರಿ, ಅದನ್ನು ಅಪ್ಲಿಕೇಶನ್ ಬೆಂಬಲಿಸುವುದಲ್ಲ.
- **ಭಾಷಾ ನಿಗದಿತ**. ಕೆಲವು ಅಪ್ಲಿಕೇಶನ್ಗಳು ಹಲವಾರು ಭಾಷೆಗಳನ್ನು ಬೆಂಬಲಿಸಿದರೂ ಆಗಾ ಅಪ್ಲಿಕೇಶನ್ ಸ್ವಾಭಾವಿಕವಾಗಿ ಒಂದು ನಿರ್ದಿಷ್ಟ ಭಾಷೆಗಾಗಿ ನಿರ್ಮಿತವಾಗಿರುತ್ತದೆ, ಜತೆಗೆ ನೀವು ಹೆಚ್ಚು ಭಾಷೆಗಳ ಬೆಂಬಲವನ್ನು ಸೇರಿಸಬಹುದು.

### ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್ಗಳ ಲಾಭಗಳು

ಆದರೆ, ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್ ಹೇಗೆ ವಿಭಿನ್ನ?

ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ, ನೀವು ಹೆಚ್ಚು ಸ್ವಲ್ಪ ಲವಚಿಕತೆಯನ್ನು ಹೊಂದಿದ್ದೀರಿ, ನೀವು ಕಮಾಂಡ್‌ಗಳ ಸರಣಿಗೆ ಅಥವಾ ನಿರ್ದಿಷ್ಟ ಇನ್‌ಪುಟ್ ಭಾಷೆಗೆ ಸೀಮಿತರಾಗಿಲ್ಲ. ಬದಲಾಗಿ, ನೀವು ನೈಸರ್ಗಿಕ ಭಾಷೆಯನ್ನು ಬಳಸಿ ಅಪ್ಲಿಕೇಶನ್ ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಬಹುದು. ಮತ್ತೊಂದು ಲಾಭವೆಂದರೆ ನೀವು ಈಗಾಗಲೇ ವಿಶಾಲ ಮಾಹಿತಿ ಸಂಗ್ರಹದ ಮೇಲ್ಭಾಗದಲ್ಲಿರುವ ಡೇಟಾ ಮೂಲದೊಂದಿಗೆ ಸಂವಹನ ಮಾಡುತ್ತಿದ್ದೀರೇ, ಆದರೆ ಸಾಂಪ್ರದಾಯಕ ಅಪ್ಲಿಕೇಶನ್ معمولವಾಗಿ ಡೇಟಾಬೇಸ್‌ನಲ್ಲಿರುವ ಮೌಲ್ಯದಷ್ಟರಲ್ಲಿ ಸೀಮಿತವಾಗಿರಬಹುದು.

### ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್ ಬಳಸಿ ನಾನು ಏನು ನಿರ್ಮಿಸಬಹುದೆ?

ನೀವು ಹಲವಾರು ವಿಧವಾದವುಗಳನ್ನು ನಿರ್ಮಿಸಬಹುದು. ಉದಾಹರಣೆಗೆ:

- **ಚಾಟ್‌ಬಾಟ್**. ನಿಮ್ಮ ಕಂಪನಿಯ ಬಗ್ಗೆ ಮತ್ತು ಅದರ ಉತ್ಪನ್ನಗಳ ಬಗ್ಗೆ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸುವ ಚಾಟ್‌ಬಾಟ್ ಉತ್ತಮ ಹೊಂದಾಣಿಕೆಯಾಗಬಹುದು.
- **ಸಹಾಯಕ**. LLMಗಳು ಪಠ್ಯವನ್ನು ಸಂಗ್ರಹಿಸುವಲ್ಲಿ, ಪಠ್ಯದಿಂದ ಒಳನೋಟಗಳನ್ನು ಪಡೆಯುವಲ್ಲಿ, ಮತ್ತೆ ಮುಂದುವರೆಯುವ ಪಠ್ಯಗಳೆಂತಿವೆ ಎಂಬುದರಲ್ಲಿ ಉತ್ತಮವಾಗಿದೆ.
- **ಕೋಡ್ ಸಹಾಯಕ**. ನೀವು ಬಳಸುವ ಭಾಷಾ ಮಾದರಿಯ ಮೇಲೆ ಅವಲಂಬಿಸಿ, ನೀವು ಕೋಡ್ ಬರೆಯಲು ಸಹಾಯ ಮಾಡುವ ಕೋಡ್ ಸಹಾಯಕರನ್ನು ನಿರ್ಮಿಸಬಹುದು. ಉದಾಹರಣೆಗೆ, GitHub Copilot ಅಥವಾ ChatGPT ಅನ್ನು ನೀವು ಕೋಡ್ ಬರೆಯಲು ಸಹಾಯಕ್ಕಾಗಿ ಬಳಸಬಹುದು.

## ನಾನು ಹೇಗೆ ಪ್ರಾರಂಭಿಸಬಹುದು?

ನೀವು ಸಾಮಾನ್ಯವಾಗಿ LLM-ನೊಂದಿಗೆ ಏಕೀಕರಣ ಮಾಡಲು ಎರಡು ವಿಧಾನಗಳನ್ನು ಹುಡುಕಬೇಕು:

- API ಬಳಸುವುದು. ಇಲ್ಲಿ ನಿಮ್ಮ ಪ್ರಾಂಪ್ಟ್‌ಗಳೊಂದಿಗೆ ವೆಬ್ ವಿನಂತಿಗಳನ್ನು ನಿರ್ಮಿಸಿ ಮತ್ತು ಉತ್ಪಾದಿತ ಪಠ್ಯವನ್ನು ಪಡೆಯುತ್ತೀರಿ.
- ಲೈಬ್ರರಿ ಬಳಸುವುದು. ಲೈಬ್ರರಿಗಳು API ಕರೆಗಳನ್ನು ಎಣಕೆಯನ್ನು ನೆರವುಮಾಡುತ್ತವೆ ಮತ್ತು ಬಳಸಲು ಸುಲಭ ಮಾಡುತ್ತವೆ.

## ಲೈಬ್ರರಿಗಳು/SDKಗಳು

LLMಜೊತೆಗೆ ಕೆಲಸ ಮಾಡಲು ಕೆಲವು ಪ್ರಸಿದ್ಧ ಲೈಬ್ರರಿಗಳು ಇವೆ:

- **openai**, ಈ ಲೈಬ್ರರಿ ನಿಮ್ಮ ಮಾದರಿಯನ್ನು ಸಂಪರ್ಕಿಸಲು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್ಗಳನ್ನು ಕಳುಹಿಸಲು ಸುಲಭ ಮಾಡುತ್ತದೆ.

ನಂತರ, ಹೆಚ್ಚಿನ ಮಟ್ಟದಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಲೈಬ್ರರಿಗಳಿವೆ:

- **Langchain**. Langchain ಪ್ರಸಿದ್ಧವಾಗಿದೆ ಮತ್ತು Python ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.
- **Semantic Kernel**. Semantic Kernel ಮೈಕ್ರೋಸಾಫ್ಟ್‌ನ ಲೈಬ್ರರಿ, ಇದು C#, Python ಮತ್ತು ಜಾವಾಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.

## openai ಬಳಸಿ ಮೊದಲು ಅಪ್ಲಿಕೇಶನ್

ನಾವು ಹೇಗೆ ನಮ್ಮ ಮೊದಲ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸಬಹುದು, ಯಾವ ಲೈಬ್ರರಿಗಳು ಬೇಕಾಗಿವೆ, ಎಷ್ಟು ಅಗತ್ಯವಿದೆ ಎಂಬುದನ್ನು ನೋಡೋಣ.

### openai ಇನ್ಸ್ಟಾಲ್ ಮಾಡಿ

OpenAI ಅಥವಾ Azure OpenAI ಜೊತೆಗೆ ಸಂವಹನಕ್ಕಾಗಿ ಹಲವಾರು ಲೈಬ್ರರಿಗಳು ಇವೆ. C#, Python, JavaScript, ಜಾವಾ ಮತ್ತು ಇನ್ನಿತರ ವಿವಿಧ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಗಳೊಂದಿಗೆ ಬಳಸಬಹುದಾಗಿದೆ. ನಾವು Python ಲೈಬ್ರರಿ `openai` ಅನ್ನು ಆರಿಸಿಕೊಂಡಿದ್ದೇವೆ, ಅದನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಲು ನಾವು `pip` ಬಳಸುುತ್ತೇವೆ.

```bash
pip install openai
```

### ಸಂಪನ್ಮೂಲ ರಚನೆ ಮಾಡಿ

ನೀವು ಈ ಕೆಳಗಿನ ಹಂತಗಳನ್ನು ಮಾಡಬೇಕು:

- ಆಜೂರ್(Account) ಖಾತೆಯನ್ನು ರಚಿಸಿ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI ಗೆ ಪ್ರವೇಶ ಪಡೆಯಿರಿ. [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst)ಗೆ ಹೋಗಿ ಮತ್ತು ಪ್ರವೇಶದ ಮನವಿ ಮಾಡಿ.

  > [!NOTE]
  > ಬರೆಯುವ ಸಮಯದಲ್ಲಿ, ನೀವು Azure OpenAI ಗೆ ಪ್ರವೇಶಕ್ಕಾಗಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕಾಗುತ್ತದೆ.

- Python ಇನ್ಸ್ಟಾಲ್ ಮಾಡಿ <https://www.python.org/>
- Azure OpenAI ಸೇವಾ ಸಂಪನ್ಮೂಲ ರಚನೆ ಮಾಡಿರಬೇಕು. ಸಂಪನ್ಮೂಲ ರಚಿಸುವ ಕುರಿತು ಮಾರ್ಗದರ್ಶನ ಈ ಲಿಂಕ್ ನಲ್ಲಿ ಇರುತ್ತದೆ [create a resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API ಕೀ ಮತ್ತು ಎಂಡ್ಪಾಯಿಂಟ್ ಕಂಡುಹಿಡಿದುಕೊಳ್ಳಿ

ಈಗ, ನಿಮ್ಮ `openai` ಲೈಬ್ರರಿಗೆ ಯಾವ API ಕೀ ಬಳಸಬೇಕು ಎಂದು ತಿಳಿಸಬೇಕು. API ಕೀ ಕಂಡುಹಿಡಿಯಲು, ನಿಮ್ಮ Azure OpenAI ಸಂಪನ್ಮೂಲದ "ಕೀಗಳು ಮತ್ತು ಎಂಡ್ಪಾಯಿಂಟ್" ವಿಭಾಗಕ್ಕೆ ಹೋಗಿ "ಕೀ 1" ಮೌಲ್ಯವನ್ನು ನಕಲಿಸಿ.

![Azure ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಕೀಗಳು ಮತ್ತು ಎಂಡ್ಪಾಯಿಂಟ್ ಸಂಪನ್ಮೂಲ ಬ್ಲೇಡ್](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ಈಗ ನೀವು ಈ ಮಾಹಿತಿಯನ್ನು ಕಾಪಿ ಮಾಡಿಕೊಂಡಿದ್ದೀರಿ, ಲೈಬ್ರರಿಗಳನ್ನು ಇದನ್ನು ಬಳಸಲು ಮಾರ್ಗದರ್ಶನ ಮಾಡೋಣ.

> [!NOTE]
> ನಿಮ್ಮ API ಕೀ ನಿಮ್ಮ ಕೋಡ್‌ಗಿಂತ ಬೇರ್ಪಡಿಸುವುದು ಉತ್ತಮ. ನೀವು ಅದನ್ನು ಪರಿಸರ변ಗಳು (environment variables) ಬಳಸಿಕೊಂಡು ಮಾಡಬಹುದು.
>
> - ಪರಿಸರ변 `OPENAI_API_KEY` ಅನ್ನು ನಿಮ್ಮ API ಕೀಗೆ ಹೊಂದಿಸಿ.
>   `export OPENAI_API_KEY='sk-...'`

### Azure ಅಂಗೀಕಾರ ಕಾನ್ಫಿಗರೇಶನ್ ಸೆಟ್‌ಅಪ್

ನೀವು Azure OpenAI (ಈಗ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯ ಭಾಗ) ಬಳಸುತ್ತಿದ್ದರೆ, ಹೀಗೆ ಸೆಟ್‌ಅಪ್ ಮಾಡಬಹುದು. ನಾವು ಸಾಮಾನ್ಯ `OpenAI` ಕ್ಲಯಿಂಟ್ ಅನ್ನು Azure OpenAI `/openai/v1/` ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಾಗಿ ಸೂಚಿಸಲಾಗುತ್ತದೆ, ಇದು Responses API ಜೊತೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಮತ್ತು ಯಾವುದೇ `api_version` ಅಗತ್ಯವಿಲ್ಲ:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು ಕೆಳಕಂಡವುಗಳನ್ನು ಸೆಟ್ ಮಾಡುತ್ತಿದ್ದೇವೆ:

- `api_key`, ಇದು Azure ಪೋರ್ಟಲ್ ಅಥವಾ Microsoft Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಕಂಡುಬರುವ ನಿಮ್ಮ API ಕೀ.
- `base_url`, ಇದು ನಿಮ್ಮ Foundry ಸಂಪನ್ಮೂಲ ಎಂಡ್ಪಾಯಿಂಟ್, `/openai/v1/` ಸೇರಿಸಲಾಗಿದೆ. ಸ್ಥಿರವಾದ v1 ಎಂಡ್ಪಾಯಿಂಟ್ OpenAI ಮತ್ತು Azure OpenAI ಎರಡಲ್ಲೂ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಮತ್ತು ಯಾವುದೇ `api_version` ನಿರ್ವಹಣೆಯ ಅಗತ್ಯವಿಲ್ಲ.

> [!NOTE] > `os.environ` ಪರಿಸರ변ಗಳನ್ನು ಓದುತ್ತದೆ. ನೀವು ಅದನ್ನು `AZURE_OPENAI_API_KEY` ಮತ್ತು `AZURE_OPENAI_ENDPOINT` ನಂತಹ ಪರಿಸರ변ಗಳನ್ನು ಓದುವಂತೆ ಬಳಸಬಹುದು. ಈ ಪರಿಸರ변ಗಳನ್ನು ನಿಮ್ಮ ಟರ್ಮಿನಲ್ ನಲ್ಲಿ ಅಥವಾ `dotenv` ಲೈಬ್ರರಿ ಬಳಸಿ ಸೆಟ್ ಮಾಡಬಹುದು.

## ಪಠ್ಯವನ್ನು ಉತ್ಪಾದಿಸಿ

ಪಠ್ಯವನ್ನು ಉತ್ಪಾದಿಸುವ ಮಾರ್ಗವೆಂದರೆ Responses API ನಲ್ಲಿ `responses.create` ವಿಧಾನವನ್ನು ಬಳಸುವುದು. ಇಲ್ಲಿದೆ ಉದಾಹರಣೆ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ, ನಾವು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ರಚಿಸಿ ನಾವು ಬಳಸಲು ಬಯಸುವ ಮಾದರಿಯನ್ನು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಪಾಸು ಮಾಡುತ್ತೇವೆ. ನಂತರ, ಉತ್ಪಾದಿತ ಪಠ್ಯವನ್ನು `response.output_text` ಮೂಲಕ ಮುದ್ರಿಸುತ್ತೇವೆ.

### ಬಹು-ತಿರುಗು ಸಂಭಾಷಣೆಗಳು

Responses API ಒಂದೇ ತಿರುವಿನ ಪಠ್ಯ ಉತ್ಪಾದನೆಗೆ ಮತ್ತು ಬಹು-ತಿರುವು ಚಾಟ್‌ಬಾಟ್‌ಗಳಿಗೂ ಸೂಕ್ತವಾಗಿದೆ - ನೀವು `input` ನಲ್ಲಿ ಸಂಭಾಷಣೆ ಕಟ್ಟಲು ಸಂದೇಶಗಳ ಪಟ್ಟಿ ಒದಗಿಸುತ್ತೀರಿ:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

ಈ ಕಾರ್ಯಾಚರಣೆಯ ಬಗ್ಗೆ ಮತ್ತಷ್ಟು ತಿಳಿವಳಿಕೆ ಮುಂದಿನ ಅಧ್ಯಾಯದಲ್ಲಿ ಇದೆ.

## ವ್ಯಾಯಾಮ - ನಿಮ್ಮ ಮೊದಲ ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್

ಈಗ openai ಅನ್ನು ಹೇಗೆ ಸೆಟ್‌ಅಪ್ ಮಾಡಬೇಕೆಂದು ತಿಳಿದುಕೊಂಡಿದ್ದೀರಿ, ನಿಮ್ಮ ಮೊದಲ ಪಠ್ಯ ಉತ್ಪಾದನೆ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸುವ ಸಮಯ ಬಂದಿದೆ. ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸಲು ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ:

1. ವರ್ಚುವಲ್ ಎನ್ವೈರನ್ಮೆಂಟ್ ರಚಿಸಿ ಮತ್ತು openai ಅನ್ನು ಇನ್ಸ್ಟಾಲ್ ಮಾಡಿ:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > ನೀವು Windows ಬಳಸುತ್ತಿದ್ದರೆ `venv\Scripts\activate` ಅನ್ನು ಬಳಸಿ, `source venv/bin/activate` ಬದಲು.

   > [!NOTE]
   > ನಿಮ್ಮ Azure OpenAI ಕೀ ಅನ್ನು [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ಗೆ ಹೋಗಿ, `Open AI` ಹುಡುಕಿ, ಮತ್ತು `Open AI resource` ಆಯ್ಕೆ ಮಾಡಿ ನಂತರ `Keys and Endpoint` ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು `Key 1` ಮೌಲ್ಯವನ್ನು ನಕಲಿ ಮಾಡಿ.

2. _app.py_ ಫೈಲ್ ರಚಿಸಿ ಮತ್ತು ಕೆಳಗಿನ ಕೋಡ್ ನೀಡಿ:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > ನೀವು ಸ್ವಚ್ಛ OpenAI ಬಳಸುತ್ತಿದ್ದರೆ (Azure ಅಲ್ಲ), `client = OpenAI(api_key="<replace this value with your OpenAI key>")` ಬಳಸಿ (ಯಾವುದೇ `base_url` ಇಲ್ಲ) ಮತ್ತು ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಹೆಸರಿನ ಬದಲು `gpt-5-mini` ಮಾದರಿ ಹೆಸರನ್ನು ಪಾಸು ಮಾಡಿ.

   ನಿಮಗೆ ಕೆಳಗಿನಂತಿದಂತೆ ನಿಷ್ಪತ್ತಿ ಕಾಣಿಸಿಕೊಳ್ಳಬಹುದು:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ವಿವಿಧ ರೀತಿಯ ಪ್ರಾಂಪ್ಟ್ಗಳು, ವಿಭಿನ್ನ ಕೆಲಸಗಳಿಗೆ

ಈಗ ನೀವು ಪ್ರಾಂಪ್ಟ್ ಬಳಸಿ ಪಠ್ಯವನ್ನು ಉತ್ಪಾದಿಸುವುದನ್ನು ನೋಡಿದ್ದೀರಿ. ನಿಮ್ಮ ಬಳಿ ಒಂದು ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿರುವ ಪ್ರೋಗ್ರಾಮ್ ಇದೆ, ನೀವು ಅದನ್ನು ಬದಲಾಯಿಸಿ ವಿಭಿನ್ನ ರೀತಿಯ ಪಠ್ಯಗಳನ್ನು ಉತ್ಪಾದಿಸಬಹುದು.

ಪ್ರಾಂಪ್ಟ್‌ಗಳ ಬಳಕೆ ಎಲ್ಲಾ ರೀತಿಯ ಕೆಲಸಗಳಿಗೆ ಆಗುತ್ತದೆ, ಉದಾಹರಣೆಗೆ:

- **ಒಂದು ವಿಧದ ಪಠ್ಯವನ್ನು ಉತ್ಪಾದಿಸಿ**. ಉದಾಹರಣೆಗೆ, ನೀವು ಒಂದು ಕವಿತೆ, ಪ್ರಶ್ನೆಗಳು ಇತ್ಯಾದಿಯನ್ನು ರಚಿಸಬಹುದು.
- **ಮಾಹಿತಿಯನ್ನು ಹುಡುಕಿ**. ನೀವು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಮಾಹಿತಿ ಹುಡುಕಲು ಬಳಸಬಹುದು, ಉದಾಹರಣೆಗೆ 'ವೆಬ್ ಅಭಿವೃದ್ಧಿಯಲ್ಲಿ CORS ಎಂದರೇನು?' ಎಂಬ ಪ್ರಶ್ನೆ.
- **ಕೋಡ್ ಉತ್ಪಾದಿಸಿ**. ನೀವು ಕೋಡ್ ಉತ್ಪಾದಿಸಲು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಬಹುದು, ಉದಾಹರಣೆಗೆ ಇಮೇಲ್ ಗಳ ಮಾನ್ಯತೆಗಾಗಿ регуляр ಅಭಿವ್ಯಕ್ತಿಯನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸುವುದು ಅಥವಾ ಸಂಪೂರ್ಣ ವೆಬ್ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ರಚಿಸುವುದು.

## ಒಂದು ಹೆಚ್ಚು ಪ್ರಾಯೋಗಿಕ ಉಪಯೋಗ: ರೆಸಿಪಿ ಜನರೆಟರ್

ನೀವು ಇನ್ಗ್ರೆಡಿಯೆಂಟ್ಸ್ ಹೊಂದಿದ್ದೀರಿ ಮತ್ತು ಏನಾದರು ರೆಸಿಪಿ ಬೇಕು ಎಂದು ಕಲ್ಪಿಸಿ. ರೆಸಿಪಿಗಳನ್ನು ಹುಡುಕಲು ಸರ್ಚ್ ಎಂಜಿನ್ ಬಳಸಿ, ಅಥವಾ LLM ಬಳಸಬಹುದು.

ನೀವು ಹೀಗೊಂದು ಪ್ರಾಂಪ್ಟ್ ಬರೆಯಬಹುದು:

> "ಕೋಳಿ, ಆಲೂಗಡ್ಡೆ ಮತ್ತು ಗಾಜರಿನೊಂದಿಗೆ ರೆಸಿಪಿಗಳು 5 ತೋರಿಸಿ. ಪ್ರತಿ ರೆಸಿಪಿಗಾಗಿ ಬಳಸಲಾದ ಎಲ್ಲಾ ಇನ್ಗ್ರೆಡಿಯೆಂಟ್ಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ"

ಮೇಲಿನ ಪ್ರಾಂಪ್ಟ್ ನೀಡಿದರೆ, ನೀವು ಹೀಗೊಂದು ಪ್ರತಿಕ್ರಿಯೆ ಸಿಗಬಹುದು:

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

ಈ ಫಲಿತಾಂಶ ಉತ್ತಮವಾಗಿದೆ, ನನಗೆ ಏನು ರುಚಿಸುತ್ತದೋ ಗೊತ್ತಾಗಿದೆ. ಈಗ ಏನು ಉಪಯುಕ್ತದಾಗಬಹುದು ಎಂದರೆ:

- ನಾನು ಇಷ್ಟಪಡುವುದಿಲ್ಲದ ಅಥವಾ ಅಲರ್ಜಿ ಇರುವ ಇನ್ಗ್ರೆಡಿಯೆಂಟ್ಸ್ ಅನ್ನು ವಿಲ್ಕೆದಿಸಿ.
- ನನ್ನ ಬಳಿ ಎಲ್ಲಾ ಇನ್ಗ್ರೆಡಿಯೆಂಟ್ಸ್ ಇಲ್ಲದಿದ್ದರೆ ಸಹ ಸರಕಗಳ ಪಟ್ಟಿ (ಶಾಪಿಂಗ್ ಲಿಸ್ಟ್) ಉತ್ಪಾದಿಸಿ.

ಮೇಲಿನ ಸಂದರ್ಭಗಳಿಗೆ, ನಾವು ಇನ್ನೊಂದು ಪ್ರಾಂಪ್ಟ್ ಸೇರಿಸೋಣ:

> "ದಯವಿಟ್ಟು ನನ್ನ ಅಲರ್ಜಿಯಿರುವ ಬೆಳ್ಳುಳ್ಳಿ ಇರುವ ರೆಸಿಪಿಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ಬದಲಾಗಿ ಬೇರೆ ಏನಾದರೂ ನೀಡಿ. ಮತ್ತು ದಯವಿಟ್ಟು ರೆಸಿಪಿಗಳಿಗೆ ಸರಕಗಳ ಪಟ್ಟಿಯನ್ನು ತಯಾರಿಸಿ, ನಾನು ಆಗಾಗಲೇ ಕೋಳಿ, ಆಲೂಗಡ್ಡೆ ಮತ್ತು ಗಾಜರಿ ಹೊಂದಿದ್ದೇನೆ ಎಂದು ಪರಿಗಣಿಸಿ."

ಈಗ ನೀವು ಹೊಸ ಫಲಿತಾಂಶ ಪಡೆದಿದ್ದೀರಿ:

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

ಇದು ನಿಮ್ಮ ಐದು ರೆಸಿಪಿಗಳು, ಬೆಳ್ಳುಳ್ಳಿ ಇಲ್ಲದೆ ಇದೆ ಮತ್ತು ಇನ್ಗ್ರೆಡಿಯೆಂಟ್ಸ್ಗಳ ಪಟ್ಟಿ ಇದೆ, ಯಾಕೆಂದರೆ ನೀವು ಅಲ್ಲಿನ ಇನ್ಗ್ರೆಡಿಯೆಂಟ್ಸ್ ಈಗಾಗಲೇ ಹೊಂದಿದ್ದೀರಿ.

## ವ್ಯಾಯಾಮ - ರೆಸಿಪಿ ಜನರೆಟರ್ ನಿರ್ಮಿಸಿ

ನಾವು ಒಂದು ಸಂದರ್ಭವನ್ನು ಆಟವಾಡಿದ ಬಳಿಕ, ಅದಕ್ಕೆ ಹೊಂದಿಕೊಂಡ ಕೋಡ್ ಬರೆದುಕೊಳ್ಳೋಣ. ಇದಕ್ಕಾಗಿ ಇವುಗಳನ್ನು ಅನುಸರಿಸಿ:

1. विद्यमान _app.py_ ಫೈಲ್ ಅನ್ನು ಪ್ರಾರಂಭ ಬಿಂದುವಾಗಿ ಬಳಸಿ
2. `prompt` ಚರವನ್ನು ಹುಡುಕಿ ಮತ್ತು ಇದರ ಕೋಡ್ ಅನ್ನು ಕೆಳಗಿನಂತಾಗಿಸಿರಿ:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ಈಗ ನೀವು ಕೋಡ್ ರನ್ ಮಾಡಿದರೆ, ಹೀಗೊಂದು ನಿಷ್ಪತ್ತಿ ಕಾಣಬಹುದು:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ಗಮನಿಸಿರಿ, ನಿಮ್ಮ LLM ಅಸ್ಥಿರವಾಗಿದೆ, ಆದ್ದರಿಂದ ಪ್ರತಿ ಬಾರಿ ರನ್ ಮಾಡಿದಾಗ ಬೇರೆ ಫಲಿತಾಂಶಗಳಾಗಬಹುದು.

   ಅದ್ಭುತ, ಇನ್ನಷ್ಟು ಉತ್ತಮಗೊಳಿಸುವುದಕ್ಕೆ ನೋಡಿ. ಈ ಕೋಡ್ ಸುಗಮವಾಗಿರಬೇಕು, ಹಾಗು ಇನ್ಗ್ರೆಡಿಯೆಂಟ್ಸ್ ಮತ್ತು ರೆಸಿಪಿಗಳ ಸಂಖ್ಯೆಯನ್ನು ಬದಲಾಯಿಸಬಹುದು.

3. ಕೋಡ್ ಅನ್ನು ಕೆಳಗಿನ ರೀತಿಯಲ್ಲಿ ಬದಲಾಯಿಸೋಣ:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ಪರೀಕ್ಷೆಯಾಗಿ ಈ ಕೋಡ್ ಬಳಸಬಹುದು ಹೀಗೆಳ:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ಫಿಲ್ಟರ್ ಮತ್ತು ಶಾಪಿಂಗ್ ಲಿಸ್ಟ್ ಸೇರಿಸಿ ಸುಧಾರಣೆ ಮಾಡುವುದು

ಈಗ ನಮಗೂ ರೆಸಿಪಿಗಳನ್ನು ಉತ್ಪಾದಿಸುವ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಅಪ್ಲಿಕೇಶನ್ ಇದೆ, ಇದು ಬಳಕೆದಾರರಿಂದ ಇನ್ಗ್ರೆಡಿಯೆಂಟ್ಸ್ ಮತ್ತು ರೆಸಿಪಿಗಳ ಸಂಖ್ಯೆಯ ಇನ್‌ಪುಟ್ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿದೆ.

ಅದನ್ನೂ ಹೆಚ್ಚು ಸುಧಾರಿಸಲು, ನಾವು ಕೆಳಗಿನವನ್ನು ಸೇರಿಸಬಹುದು:

- **ಇನ್ಗ್ರೆಡಿಯೆಂಟ್ಸ್ ಅನ್ನು ಫಿಲ್ಟರ್ ಮಾಡಿ**. ನಾವು ಇಷ್ಟಪಡುವುದಿಲ್ಲದ ಅಥವಾ ಅಲರ್ಜಿಯ 있는 ಇನ್ಗ್ರೆಡಿಯೆಂಟ್ಸ್ ಅನ್ನು ತೆಗೆದುಹಾಕಲು ಬಯಸುತ್ತೇವೆ. ಇದಕ್ಕಾಗಿ, ನಾವು ನಮ್ಮ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ತಿದ್ದುಪಡಿ ಮಾಡಿ, ಕೊನೆಯಲ್ಲಿ ಫಿಲ್ಟರ್ ಶರತ್ತು ಸೇರಿಸಬಹುದು ಹೀಗೆ:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ಮೇಲಿನ, ನಾವು ಕೊನೆಯಲ್ಲಿ `{filter}` ಅನ್ನು ಸೇರಿಸಿದ್ದೇವೆ ಮತ್ತು ಬಳಕೆದಾರರಿಂದ ಫಿಲ್ಟರ್ ಮೌಲ್ಯವನ್ನು ಹಿಡಿದಿಟ್ಟುಕೊಂಡಿದ್ದೇವೆ.

  ಕಾರ್ಯಕ್ರಮವನ್ನು.executeUpdate ಮಾಡಿಱಕೊಂಡಿದ್ದೇವೆ:

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

  ನೀವು ನೋಡಬಹುದಾಗಿದೆ, ಹಾಲನ್ನು ಸೇರಿದ ರೆಸಿಪಿಗಳು***ಕು***ಳಿಸಲಾಗಿದೆ. ಆದರೆ ನೀವು ಲ್ಯಾಕ್ಟೋಸ್ ಅಸಹಿಷ್ಣುತನ ಇದ್ದರೆ, ಪನೀರ್ ಸೇರಿರುವ ರೆಸಿಪುಗಳನ್ನು ಕೂಡ ಫಿಲ್ಟರ್ ಮಾಡಬೇಕು ಎಂದಾದರೆ ಸ್ಪಷ್ಟತೆ ಅಗತ್ಯ.

- **ಶಾಪಿಂಗ್ ಲಿಸ್ಟ್ ಉತ್ಪಾದಿಸಿ**. ನಾವು ಈಗಾಗಲೇ ಹೊಂದಿರುವ ಇನ್ಗ್ರೆಡಿಯೆಂಟ್ಸ್ ನ್ನು ಪರಿಗಣಿಸಿ ಶಾಪಿಂಗ್ ಲಿಸ್ಟ್ ರಚಿಸಲು ಬಯಸುತ್ತೇವೆ.

  ಈ ಕಾರ್ಯಕ್ಕಾಗಿ, ನಾವು ಒಂದೇ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ಎಲ್ಲಾ ಸಮಸ್ಯೆಯನ್ನು ಪರಿಹರಿಸಬಹುದು ಅಥವಾ ಎರಡನೆ ಪ್ರಾಂಪ್ಟ್ ಆಗಿ ವಿಭಜಿಸಬಹುದು. ಎರಡನೆಯ ವಿಧಾನ ಪ್ರಯತ್ನಿಸೋಣ. ಇಲ್ಲಿ ನಾವು ಮತ್ತೊಂದು ಪ್ರಾಂಪ್ಟ್ ಸೇರಿಸೋಣ ಎಂದು ಉಲ್ಲೇಖಿಸುತ್ತಿದ್ದೇವೆ, ಆದರೆ ಅದಕ್ಕೆ ಮುಂಚಿನ ಪ್ರಾಂಪ್ಟ್ ಫಲಿತಾಂಶವನ್ನು ನೀಡುವ ಮೂಲಕ ಸನ್ನಿವೇಶ (context) ನೀಡಬೇಕು.

  ಮೊದಲ ಪ್ರಾಂಪ್ಟ್ ಫಲಿತಾಂಶವನ್ನು ಮುದ್ರಿಸುವ ಸ್ಥಳವನ್ನು ಹುಡುಕಿ ಮತ್ತು ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿರಿ:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  ಗಮನಿಸಿ:

  1. ಮೊದಲ ಪ್ರಾಂಪ್ಟ್‌ನ ಫಲಿತಾಂಶವನ್ನು ಹೊಸ ಪ್ರಾಂಪ್ಟ್‌ಗೆ ಸೇರಿಸಿ ಹೊಸ ಪ್ರಾಂಪ್ಟ್ ರಚಿಸುತ್ತಿದ್ದೇವೆ:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. ನಾವು ಹೊಸ ವಿನಂತಿಯನ್ನು ಮಾಡುತ್ತಿದ್ದೇವೆ, ಆದರೆ ಮೊದಲ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ಕೇಳಿದ ಟೋಕನ್ಸ್ ಸಂಖ್ಯೆಯನ್ನು ಗಮನಿಸುತ್ತಾ, ಈ ಬಾರಿ `max_output_tokens` 1200 ಎಂದು ಹೇಳುತ್ತಿದ್ದೇವೆ.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ಈ ಕೋಡ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿದಾಗ, ನಾವು ಈ ಕೆಳಗಿನ ಫಲಿತಾಂಶ ಪಡೆಯುತ್ತೇವೆ:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## ನಿಮ್ಮ ಸೆಟ್‌ಅಪ್ ಅನ್ನು ಸುಧಾರಿಸಿ

ನಾವು ಇದುವರೆಗೆ ಹೊಂದಿರುವುದು ಕೆಲಸ ಮಾಡುವ ಕೋಡ್ ಆಗಿದೆ, ಆದರೆ ಇನ್ನಷ್ಟು ಸುಧಾರಿಸಲು ನಾವು ಕೆಲವೊಂದು ಬದಲಾವಣೆಗಳನ್ನು ಮಾಡಬೇಕು. ನಾವು ಮಾಡಬೇಕಾದ ಕೆಲವು ಕಾರ್ಯಗಳು ಇವು:

- **ರಹಸ್ಯಗಳನ್ನು ಕೋಡ್‌ನಿಂದ ಪ್ರತ್ಯೇಕಿಸುವುದು**, ಉದಾಹರಣೆಗೆ API ಕೀ. ರಹಸ್ಯಗಳು ಕೋಡ್‌ನಲ್ಲಿ ಇರಬಾರದು ಮತ್ತು ಅವುಗಳನ್ನು ಸುರಕ್ಷಿತ ಸ್ಥಳದಲ್ಲಿ ಸಂಗ್ರಹಿಸಬೇಕು. ರಹಸ್ಯಗಳನ್ನು ಕೋಡ್‌ನಿಂದ ಪ್ರತ್ಯೇಕಿಸಲು, ನಾವು ಪರಿಸರ ಚರಗಳು ಮತ್ತು `python-dotenv`ಂತಹ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಬಳಸಬಹುದು ಅವುಗಳನ್ನು ಫೈಲ್‌ನಿಂದ ಲೋಡ್ ಮಾಡುವುದಕ್ಕೆ. ಕೋಡ್‌ನಲ್ಲಿ ಇದು ಹೀಗೆ ಕಾಣುತ್ತದೆ:

  1. ಕೆಳಗಿನ ವಿಷಯದೊಂದಿಗೆ ಒಂದು `.env` ಫೈಲ್ ರಚಿಸಿ:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ಗಮನಿಸಿ, Microsoft Foundry ಯಲ್ಲಿನ Azure OpenAIಗೆ, ನೀವು ಬದಲಿ ಪರಿಸರ ಚರಗಳನ್ನು ಇವೆಂದು ಹೊಂದಿಸಬೇಕಾಗುತ್ತದೆ:

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

- **ಟೋಕನ್ ಉದ್ದದ ಬಗ್ಗೆ ಒಂದು ಮಾತು**. ನಾವು ಬೇಕಾದ ಪಠ್ಯವನ್ನು ಉತ್ಪತ್ತಿ ಮಾಡಲು ಎಷ್ಟು ಟೋಕನೀಗಳು ಬೇಕೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಟೋಕನ್ಗಳು ಹಣದ ಚಾರ್ಜ್ ಆಗುತ್ತವೆ, ಆದ್ದರಿಂದ ಸಾಧ್ಯವಿದ್ದಷ್ಟೂ, ನಾವು ಬಳಸುವ ಟೋಕನ್ಗಳ ಸಂಖ್ಯೆಯನ್ನು ಅರ್ಥಪೂರ್ಣವಾಗಿ ಮಾಡಬೇಕು. ಉದಾಹರಣೆಗೆ, ನಾವು.promptನ್ನು ಹೀಗೆ ಬದಲಾಗಿದೆ ಎಂದರೆ ಕಡಿಮೆ ಟೋಕನ್ಗಳನ್ನು ಬಳಸಬಹುದು?

  ನಾವು ಬಳಸುವ ಟೋಕನ್ಗಳನ್ನು ಬದಲಾಯಿಸಲು, ನೀವು `max_output_tokens` ಪ್ಯಾರامیಟರ್ ಅನ್ನು ಬಳಸಬಹುದು. ಉದಾಹರಣೆಗೆ, ನೀವು 100 ಟೋಕನ್ಗಳನ್ನು ಬಳಸಲು ಬಯಸಿದರೆ, ನೀವು ಹೀಯಾಗಿ ಮಾಡಬೇಕು:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **ತਾਪಮಾನವನ್ನು ಪ್ರಯೋಗಿಸುವುದು**. ನಾವು ಇದುವರೆಗೆ ಮಾತಾಡಲಿಲ್ಲ ಆದರೆ ತಾಪಮಾನವು ನಮ್ಮ ಕಾರ್ಯಕ್ರಮ ಕಾರ್ಯಕ್ಷಮತೆಯ ಪ್ರಮುಖ ಸ೦ದರ್ಭವಾಗಿದೆ. ತಾಪಮಾನ ಮೌಲ್ಯ ಹೆಚ್ಚು ಇದ್ದರೆ ಔಟ್‌ಪುಟ್ ಹೆಚ್ಚು ಯಾದೃಚ್ಛಿಕವಾಗುತ್ತದೆ. ಕಡಿಮೆ ಇದ್ದರೆ ಔಟ್‌ಪುಟ್ ಹೆಚ್ಚು ನಿರೀಕ್ಷಣೀಯವಾಗುತ್ತದೆ. ನೀವು ಔಟ್‌ಪುಟ್‌ನಲ್ಲಿ ಬದಲಾವಣೆ ಇಚ್ಛಿಸುತ್ತೀರಾ ಅಥವಾ ಇಲ್ಲವೇ ಎಂದು ಪರಿಗಣಿಸಿ.

  ತಾಪಮಾನವನ್ನು ಬದಲಾಯಿಸಲು, ನೀವು `temperature` ಪ್ಯಾರامیಟರ್ ಅನ್ನು ಬಳಸಬಹುದು. ಉದಾಹರಣೆಗೆ, ನೀವು 0.5 ತಾಪಮಾನ ಇಚ್ಛಿಸಿದರೆ, ನೀವು ಹೀಗೆ ಮಾಡಬಹುದು:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ಗಮನಿಸಿ, 1.0 ಗೆ όσο ಹೋಗುತ್ತದೊ ಆಷ್ಟು ಔಟ್‌ಪುಟ್ ವಿಭಿನ್ನವಾಗುತ್ತದೆ.

- **ಕಾರಣಮೂಲ ಮಾದರಿಗಳು `temperature` ಬಳಸುವುದಿಲ್ಲ**. ಇದು 2026ರ ಪ್ರಮುಖ ಬದಲಾವಣೆ. Microsoft Foundryಯಲ್ಲಿನ ಪ್ರಸ್ತುತ, ಸಕ್ರಿಯ ಮಾದರಿಗಳು **ಕಾರಣಮೂಲ ಮಾದರಿಗಳು** (GPT-5 ಕುಟುಂಬ, o-ಸಂಖ್ಯೆ) - ಮತ್ತು ಅವು **`temperature` ಅಥವಾ `top_p`** (ಮತ್ತು `max_tokens` ಅಲ್ಲ; ಸೌಲಭ್ಯಕ್ಕಾಗಿ `max_output_tokens` ಬಳಸಿ) ಬೆಂಬಲಿಸುವುದಿಲ್ಲ. ನೀವು `temperature` ಅನ್ನು `gpt-5-mini` ಗೆ ಕಳುಹಿಸಿದರೆ "ಪ್ಯಾರامیಟರ್ ಬೆಂಬಲಿಸುವುದಿಲ್ಲ" ಎಂಬ ದೋಷ ಬರುತ್ತದೆ. ಆದ್ದರಿಂದ ಮೇಲಿನ ತಾಪಮಾನ ಉದಾಹರಣೆಯನ್ನು ಪ್ರಯತ್ನಿಸಲು, ನಿದರ್ಶನ নিয়ಂತ್ರಣಗಳನ್ನು ಇನ್ನೂ ಬೆಂಬಲಿಸುವ ಮಾದರಿಯನ್ನು ಬಳಸಿ - ಉದಾಹರಣೆಗೆ ಮುಕ್ತ **Llama** ಮಾದರಿ `Llama-3.3-70B-Instruct` [Microsoft Foundry ಮಾದರಿ ಕ್ಯಾಟಾಲಾಗ್](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ನಿಂದ ಆಗಿದ್ದು, Foundry Models / Azure AI Inference ಎಂಟಿಪಾಯಿಂಟ್ ಮೂಲಕ (`githubmodels-*` ಮಾದರಿಗಳಂತೆ) ಕರೆಮಾಡಬಹುದು. GPT-5ರಂತಹ ಕಾರಣಮೂಲ ಮಾದರಿಗಳಲ್ಲಿ ಔಟ್‌ಪುಟ್ ನ್ನು ಬೇರೆ ರೀತಿಯಲ್ಲಿ ನಿಯಂತ್ರಿಸಲಾಗುತ್ತದೆ:
  - **ಪ್ರಾಂಪ್ಟ್ ಎಂಜಿನಿಯರಿಂಗ್** - ಸ್ಪಷ್ಟ ನಿರ್ದೇಶನಗಳು, ಉದಾಹರಣೆಗಳು, ಮತ್ತು ರಚನಾತ್ಮಕ ಔಟ್‌ಪುಟ್ (ಪಾಠ [04 - ಪ್ರಾಂಪ್ಟ್ ಎಂಜಿನಿಯರಿಂಗ್](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) ನೋಡಿ) ನಿದರ್ಶನ ನಿಯಂತ್ರಣಗಳನ್ನು ಅಲಂಕರಿಸುತ್ತವೆ.
  - **ಕಾರಣಮೂಲ ನಿಯಂತ್ರಣಗಳು** - ಕಾರಣಮೂಲ ಶ್ರಮ/ವ verbosity ತರತಮ್ಯದಲ್ಲಿ ಕಾರಣಮೂಲದ ಆಳದ ವಿರುದ್ಧ ತಡತೆ ಮತ್ತು ವೆಚ್ಚದ ಲೆಕ್ಕಾಚಾರ ಮಾಡುತ್ತವೆ.

  ಸಣ್ಣಸಂಗ್ರಹ: `temperature`/`top_p` ಹಲವಾರು ಮಾದರಿಗಳಲ್ಲಿ ಇನ್ನೂ ಪ್ರಚಲಿತವಿದೆ (Llama, Mistral, Phi, ಮತ್ತು GPT-4.x ಕುಟುಂಬ - ಆದರೂ GPT-4.x ದೈತ್ಯವಾಗುತ್ತಿದೆ), ಆದರೆ ದಿಕ್ಕು ಸ್ಪಷ್ಟವಾಗುತ್ತಿದೆ - GPT-5 ರಂತಹ ಕಾರಣಮೂಲ ಮಾದರಿಗಳಲ್ಲಿ ಪ್ರಾಂಪ್ಟ್ ಎಂಜಿನಿಯರಿಂಗ್ + ಕಾರಣಮೂಲ ನಿಯಂತ್ರಣಗಳ ಕಡೆಗೆ.

## ಅಸೈನ್ಮೆಂಟ್

ಈ ಅಸೈನ್ಮೆಂಟ್‌ಗೆ, ನೀವು ಏನು ನಿರ್ಮಿಸಬೇಕೆಂದು ಆಯ್ಕೆ ಮಾಡಬಹುದು.

ಕೆಲವು ಸಲಹೆಗಳು:

- ರೆಸಿಪಿ ಜನರೇಟರ್ ಆಪ್ ಅನ್ನು ಇನ್ನಷ್ಟು ಸುಧಾರಿಸಲು ತಿದ್ದುಪಡಿ ಮಾಡಿ. ತಾಪಮಾನ ಮೌಲ್ಯಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್ಗಳೊಂದಿಗೆ ಆಟವಾಡಿ ನಿಮ್ಮದೇ ಆದ ಪ್ರಯುಕ್ತಗಳನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.
- "ಅಧ್ಯಯನ ಸಹಯೋಗಿ" ಅನ್ನು ನಿರ್ಮಿಸಿ. ಈ ಆಪ್ ಒಂದು ವಿಷಯದ ಗುರಿಯಾಗಿರುವ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ನೀಡಬಲ್ಲದು, ಉದಾಹರಣೆಗೆ Python. ನೀವು "Python ನಲ್ಲಿ ಒಬ್ಬ ವಿಶೇಷ ವಿಷಯವೇನು?", ಅಥವಾ "ಒಂದು ವಿಷಯಕ್ಕೆ ಕೋಡ್ ತೋರಿಸು" ಎಂಬಂತಹ ಪ್ರಾಂಪ್ಟ್ಗಳನ್ನು ಹೊಂದಬಹುದು ಇತ್ಯಾದಿ.
- ಇತಿಹಾಸ ಬಾಟ್, ಇತಿಹಾಸವನ್ನು ಜೀವಂತಗೊಳಿಸಿ, ಬಾಟ್‌ಗೆ ನಿಗದಿತ ಇತಿಹಾಸದಲ್ಲಿನ ಪಾತ್ರವನ್ನು ಆಡಲು ಸೂಚಿಸಿ ಮತ್ತು ಅದರ ಜೀವನ ಮತ್ತು ಕಾಲಗಳ ಬಗ್ಗೆ ಪ್ರಶ್ನೆಗಳು ಕೇಳಿ.

## ಪರಿಹಾರ

### ಅಧ್ಯಯನ ಸಹಯೋಗಿ

ಕೆಳಗಿನವು ಆರಂಭಿಕ ಪ್ರಾಂಪ್ಟ್, ನೀವು ಇದನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು ಮತ್ತು ನಿಮ್ಮ ಇಷ್ಟಕ್ಕೆ ಹೊಂದಿಸುವುದನ್ನು ನೋಡಿ.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ಇತಿಹಾಸ ಬಾಟ್

ನೀವು ಬಳಸಬಹುದಾದ ಕೆಲವು ಪ್ರಾಂಪ್ಟ್‌ಗಳು:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ಜ್ಞಾನ ಪರೀಕ್ಷೆ

ತಾಪಮಾನ ಸಂ概念 ಏನು ಮಾಡುತ್ತದೆ?

1. ಅದು ಔಟ್‌ಪುಟ್ ಎಷ್ಟು ಯಾದೃಚ್ಛಿಕವಾಗುತ್ತದೆ ಎಂದು ನಿಯಂತ್ರಿಸುತ್ತದೆ.
1. ಅದು ಪ್ರತಿಕ್ರಿಯೆಯ ಗಾತ್ರವನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ.
1. ಅದು ಎಷ್ಟು ಟೋಕನ್ಗಳನ್ನು ಬಳಸಲಾಗುತ್ತದೆ ಎಂದು ನಿಯಂತ್ರಿಸುತ್ತದೆ.

## 🚀 ಸವಾಲು

ಅಸೈನ್ಮೆಂಟ್‌ನಲ್ಲಿ ಕೆಲಸ ಮಾಡುವಾಗ, ತಾಪಮಾನವನ್ನು ವಿಭಿನ್ನಗೊಳಿಸಲು ಪ್ರಯತ್ನಿಸಿ, 0, 0.5, ಮತ್ತು 1 ಗೆ ಹೊಂದಿಸಿ. 0 ಕನಿಷ್ಟ ವಿಭಿನ್ನತೆಯನ್ನು ಮತ್ತು 1 ಅತ್ಯಂತ ವಿಭಿನ್ನತೆಯನ್ನು ಸೂಚಿಸುತ್ತದೆ. ನಿಮ್ಮ ಆಪ್‌ಗೆ ಯಾವ ಮೌಲ್ಯ ಕೆಲಸ ಮಾಡುತ್ತದೆ?

## ಅದ್ಭುತ ಕೆಲಸ! ನಿಮ್ಮ ಅಧ್ಯಯನವನ್ನು ಮುಂದುವರಿಸಿ

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನಮ್ಮ [ಜನರೇಟಿವ್ AI ಅಧ್ಯಯನ ಸಂಗ್ರಹ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)ನ್ನು ನೋಡಿ ನಿಮ್ಮ ಜನರೇಟಿವ್ AI ಜ್ಞಾನವನ್ನು ಹೆಚ್ಚಿಸಿ!

ಪಾಠ 7ಕ್ಕೆ ಹೋಗಿ ನಾವು ಹೇಗೆ [ಚಾಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) ಎಂಬುದನ್ನು ನೋಡ್ಕೋಣ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->