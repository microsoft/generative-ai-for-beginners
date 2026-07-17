# LLM ಪ್ರೊವೈಡರ್ ಆಯ್ಕೆ ಮಾಡುವುದು ಮತ್ತು ಸಂರಚಿಸುವುದು 🔑

ಪ್ರೌಢಶಾಲಾ ಕಾರ್ಯಗಳು OpenAI, Azure ಅಥವಾ Hugging Face ಎಂಬ ಬೆಂಬಲಿತ ಸೇವಾ ಪ್ರೊವೈಡರ್ ಮೂಲಕ ಒಂದನೇ ಅಥವಾ ಹೆಚ್ಚು ಲಾರ್ಜ್ ಲ್ಯಾಂಗ್ವೇಜ್ ಮಾದರಿ (LLM) ನಿಯೋಜನೆಗಳೊಂದಿಗೆ ಕೆಲಸ ಮಾಡಲು **ಸಿದ್ಧಗೊಳಿಸಬಹುದು**. ಇವುಗಳು ನಮಗೆ ಸರಿಯಾದ ಪ್ರಮಾಣಪತ್ರಗಳೊಂದಿಗೆ (API ಪ್ರಮುಖ ಅಥವಾ ಟೋಕನ್) ಪ್ರೋಗ್ರಾಮ್ಯಾಟಿಕಾಗಿ ಪ್ರವೇಶಿಸಲು ಸಾಧ್ಯವಾಗುವ _ಹೋಸ್ಟೆಡ್ ಎಂಡ್‌ಪಾಯಿಂಟ್_ (API) ಒದಗಿಸುತ್ತವೆ. ಈ ಕೋರ್ಸ್ನಲ್ಲಿ, ನಾವು ಈ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಚರ್ಚಿಸುತ್ತೇವೆ:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ವಿವಿಧ ಮಾದರಿಗಳನ್ನು ಒಳಗೊಂಡಿದೆ, ಅದರಲ್ಲಿಯೂ ಮುಖ್ಯ GPT ಸರಣಿ.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) ಸಂಸ್ಥೆಗಳ ಸಿದ್ಧತೆ ತೀವ್ರವಾಗಿ ಗಮನದಲ್ಲಿಟ್ಟಿರುವ OpenAI ಮಾದರಿಗಳಿಗೆ
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) OpenAI, ಮೆಟಾ, ಮಿಸ್ಟ್ರಲ್, ಕೋಹೆಯರ್, ಮೈಕ್ರೋಸಾಫ್ಟ್ ಮತ್ತು ಇತರೆಗಳಿಂದ ನೂರಾರು ಮಾದರಿಗಳನ್ನು ಪ್ರವೇಶಿಸಲು ಒಂದು ಏಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು API ಕೀ (GitHub Models ಸ್ಥಳಾಂತರಗೊಳ್ಳುತ್ತಿದೆ, ಅದು ಜುಲೈ 2026 ಕೊನೆಯಲ್ಲಿ ನಿವೃತ್ತವಾಗಲಿದೆ)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ಮುಕ್ತ ಮಾದರಿಗಳು ಮತ್ತು ಇನ್ಫರೆನ್ಸ್ ಸರ್ವರ್‌ಗಾಗಿ
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ಅಥವಾ [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ನೀವು ನಿಮ್ಮ ಸಾಧನದಲ್ಲಿ ಪೂರ್ಣವಾಗಿ ಆನ್‌ಲೈನ್ ಇಲ್ಲದೆ ಮಾದರಿಗಳನ್ನು ಸಂಚಾಲಿಸಲು ಇಚ್ಛಿಸಿದರೆ, ಕ್ಲೌಡ್ ಸಬ್ಸಕ್ರಿಪ್‌ಷನ್ ಅಗತ್ಯವಿಲ್ಲದೆ

**ನೀವು ಈ ವ್ಯಾಯಾಮಗಳಿಗೆ ನಿಮ್ಮ ಸ್ವಂತ ಖಾತೆಗಳನ್ನು ಬಳಸಬೇಕಾಗುತ್ತದೆ**. ಪ್ರೌಢಶಾಲಾ ಕಾರ್ಯಗಳು ಆಯ್ಕೆಮಾಡುವವರೆಗೆ ಸಂಪರ್ಕಗಳು ಆದ್ದರಿಂದ ನೀವು ಇಚ್ಛೆಯಾದಂತೆ ಒಂದು, ಎಲ್ಲಾ - ಅಥವಾ ಯಾವುದೇ - ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಸಿದ್ಧಗೊಳಿಸಬಹುದು. ಸೈನ್ ಅಪ್‌ಗಾಗಿ ಕೆಲವು ಮಾರ್ಗದರ್ಶಿಗಳು:

| ಸೈನ್ ಅಪ್ | ವೆಚ್ಚ | API ಕೀ | ಪ್ಲೇಗ್ರೌಂಡ್ | ಟೀಕೆಗಳು |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ಬೆಲೆಪಟ್ಟಿ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ಪ್ರಾಜೆಕ್ಟ್ ಆಧಾರಿತ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ನೋ-ಕೋಡ್, ವೆಬ್](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | ಹಲವು ಮಾದರಿಗಳು ಲಭ್ಯವಿವೆ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ಬೆಲೆಪಟ್ಟಿ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK ಕ್ವಿಕ್‌ಸ್ಟಾರ್ಟ್](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [ಸ್ಟುಡಿಯೋ ಕ್ವಿಕ್‌ಸ್ಟಾರ್ಟ್](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ಅಕ್ಸೆಸ್‌ಗೆ ಮುಂಚಿತ ಅರ್ಜಿ ಹಾಕಬೇಕು](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [ಬೆಲೆಪಟ್ಟಿ](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [ಪ್ರಾಜೆಕ್ಟ್ ಅವಲೋಕನ ಪುಟ](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry ಪ್ಲೇಗ್ರೌಂಡ್](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | ಉಚಿತ ಮಟ್ಟ ಲಭ್ಯವಿದೆ; ಹಲವಾರು ಮಾದರಿ ಪ್ರೊವೈಡರ್‌ಗಳಿಗೆ ಒಂದು ಏಂಡ್‌ಪಾಯಿಂಟ್ + ಕೀ |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ವೆಚ್ಚ](https://huggingface.co/pricing) | [ಪ್ರವೇಶ ಟೋಕನ್‌ಗಳು](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging ಚಾಟ್](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging ಚಾಟ್‌ಗೆ ಸೀಮಿತ ಮಾದರಿಗಳು ಲಭ್ಯ](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ಉಚಿತ (ನಿಮ್ಮ ಸಾಧನದಲ್ಲಿ ಚಲಿಸುತ್ತದೆ) | ಅಗತ್ಯವಿಲ್ಲ | [ಲೋಕಲ್ CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | ಪೂರ್ಣವಾಗಿ ಆಫ್‌ಲೈನ್, OpenAI-ಸಂಯೋಜಿತ ಏಂಡ್‌ಪಾಯಿಂಟ್ |
| | | | | |

ವಿವಿಧ ಪ್ರೊವೈಡರ್‌ಗಳೊಂದಿಗೆ ಈ ರೆಪೊಸಿಟ್ ಅನ್ನು _ಕಾನ್ಫಿಗರ್_ ಮಾಡಲು ಕೆಳಗಿನ ನಿರ್ದೇಶನಗಳನ್ನು ಅನುಸರಿಸಿ. ನಿರ್ದಿಷ್ಟ ಪ್ರೊವೈಡರ್ ಅಗತ್ಯವಿರುವ ಪ್ರೌಢಶಾಲಾ ಕಾರ್ಯಗಳು ಅವರ ಫೈಲ್‌ನಾಮದಲ್ಲಿ ಈ ಟ್ಯಾಗ್‌ಗಳನ್ನು ಹೊಂದಿರುತ್ತವೆ:

- `aoai` - Azure OpenAI ಏಂಡ್‌ಪಾಯಿಂಟ್, ಕೀ ಅಗತ್ಯ
- `oai` - OpenAI ಏಂಡ್‌ಪಾಯಿಂಟ್, ಕೀ ಅಗತ್ಯ
- `hf` - Hugging Face ಟೋಕನ್ ಅಗತ್ಯ
- `githubmodels` - Microsoft Foundry Models ಏಂಡ್‌ಪಾಯಿಂಟ್, ಕೀ ಅಗತ್ಯ (GitHub Models ಜುಲೈ 2026 ಕೊನೆಯಲ್ಲಿ ನಿವೃತ್ತವಾಗುತ್ತಿದೆ)

ನೀವು ಒಂದನ್ನೂ, ಯಾವುದನ್ನೂ, ಅಥವಾ ಎಲ್ಲ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನೂ ಸಂರಚಿಸಬಹುದು. ಸಂಬಂಧಿತ ಪ್ರೌಢಶಾಲಾ ಕಾರ್ಯಗಳು ಅನುಪಲಭ್ಯ ಪ್ರಮಾಣಪತ್ರಗಳಿದ್ದರೆ ದೋಷಸೂಚನೆ ತೋರಿಸುತ್ತದೆ.

## `.env` ಫೈಲ್ ರಚಿಸಿ

ನೀವು ಮೇಲಿನ ಮಾರ್ಗದರ್ಶನ ಓದಿರುವಿರಿ ಎಂದು ನಾವು ಊಹಿಸುತ್ತೇವೆ ಮತ್ತು ಸಂಬಂಧಿತ ಪ್ರೊವೈಡರ್ ಜೊತೆ ಸೈನ್ ಅಪ್ ಆಗಿ ಅಗತ್ಯ ಪ್ರಮಾಣೀಕರಣ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು (API_KEY ಅಥವಾ ಟೋಕನ್) ಪಡೆದಿರುವಿರಿ. Azure OpenAI ಉಪಯೋಗಿಸುವ ಸಂದರ್ಭದಲ್ಲಿ, ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆಯಿಗಾಗಿ ಕನಿಷ್ಠ ಒಂದು GPT ಮಾದರಿ ನಿಯೋಜಿತ ಇರುವ Azure OpenAI ಸೇವೆಯ (ಎಂಡ್‌ಪಾಯಿಂಟ್) ಮಾನ್ಯ ನಿಯೋಜನೆ ಇರುತ್ತದೆ ಎಂದು ನಾವು ನಂಬುತ್ತೇವೆ.

ಮುಂದಿನ ಹಂತವೆಂದರೆ ನಿಮ್ಮ **ಸ್ಥಳೀಯ ವಾತಾವರಣ ಚರ**ಗಳನ್ನು ಕೆಳಗಿನಂತೆ ಸಂರಚಿಸುವುದು:

1. ಮಾಲಿಕರ ಫೋಲ್ಡರ್‌ನಲ್ಲಿ `.env.copy` ಫೈಲ್ ಅನ್ನು ಹುಡುಕಿ, ಅದರ ಅಂಶಗಳು ಹೀಗೆ ಇರಬೇಕು:

   ```bash
   # ಓಪನ್‌ಎಐ ಒದಗಿಸುವವರು
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯಲ್ಲಿ ಅಝುರ್ ಓಪನ್‌ಎಐ
   ## (ಅಝುರ್ ಓಪನ್‌ಎಐ ಸೇವೆ ಈಗ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯ ಭಾಗವಾಗಿದೆ: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ಡೀಫಾಲ್ಟ್ ಸೆಟ್ ಆಗಿದೆ! (ಪ್ರಸ್ತುತ ಸ್ಥಿರ GA API ಆವೃತ್ತಿ)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಮಾದರಿಗಳು (ಬಹು-ಒದಗಿಸುವವರು ಮಾದರಿ ಕ್ಯಾಲೋಗ್, ಗಿಟ್‌ಹಬ್ ಮಾದರಿಗಳನ್ನು ಬದಲಿ ಮಾಡುತ್ತದೆ, ಇದು ಜುಲೈ 2026 ಕೊನೆಯ ಭಾಗಿ ನಿವೃತ್ತಿ ಹೊಂದಿದೆ)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## ಹಗ್ಗಿಂಗ್ ಫೇಸ್
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. ಕಡತವನ್ನು ಕೆಳಗಿನ ಆಜ್ಞೆಯಿಂದ `.env` ಗೆ ನಕಲಿಸಿ. ಈ ಫೈಲ್ _gitignore-ಡ್ಅಡ್_, ರಹಸ್ಯಗಳನ್ನು ಸುರಕ್ಷಿತವಾಗಿರಿಸಲು.

   ```bash
   cp .env.copy .env
   ```

3. ಮೌಲ್ಯಗಳನ್ನು (ಬಲಭಾಗದಲ್ಲಿ ಇರುವ ಪ್ಲೇಸ್ಹೋಲ್ಡರ್‌ಗಳನ್ನು ಬದಲಿಸಿ) ಮುಂದಿನ ವಿಭಾಗದಲ್ಲಿ ವಿವರಿಸಿದಂತೆ ತುಂಬಿ.

4. (ಐಚ್ಛಿಕ) ನೀವು GitHub Codespaces ಬಳಸಿದರೆ, ಈ ರೆಪೊಸಿಟರಿ ಸಂಬಂಧಿಸಿದ _Codespaces ರಹಸ್ಯಗಳು_ ರೂಪದಲ್ಲಿ ವಾತಾವರಣ ಚರಗಳನ್ನು ಉಳಿಸುವ ಆಯ್ಕೆ ನಿಮಗೆ ಇದೆ. ಇಂತಹಲ್ಲಿ, ಸ್ಥಳೀಯ .env ಫೈಲ್‍ನ್ನು ಸಿದ್ಧಪಡಿಸಲು ಅಗತ್ಯವಿಲ್ಲ. **ಆದರೆ, ಈ ಆಯ್ಕೆ GitHub Codespaces ಬಳಸಿದಾಗ ಮಾತ್ರ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ**. ನೀವು Docker Desktop ಬಳಸುವಾಗ .env ಫೈಲ್ ಇನ್ನೂ ಸಿದ್ಧಪಡಿಸಬೇಕಾಗುತ್ತದೆ.

## `.env` ಫೈಲ್ ತುಂಬಿ

ನಾವು ಚರ ಹೆಸರುಗಳನ್ನು ತ್ವರಿತವಾಗಿ ಪರಿಶೀಲಿಸಿ ಅವುಗಳ ಅರ್ಥ ಏನೆಂದು ತಿಳಿಯೋಣ:

| ಚರ ಹೆಸರು  | ವಿವರಣೆ  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ನಿಮ್ಮ ಪ್ರೊಫೈಲ್‌ನಲ್ಲಿ ನೀವು ಸಿದ್ಧಪಡಿಸಿದ ಬಳಕೆದಾರ ಪ್ರವೇಶ ಟೋಕನ್ |
| OPENAI_API_KEY | ನಾನ್-Azure OpenAI ಏಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಬಳಸಲು ಅನುಮತಿಸುವ ಕೀ |
| AZURE_OPENAI_API_KEY | ಆ ಸೇವೆಯನ್ನು ಬಳಸಲು ಅನುಮತಿಸುವ ಕೀ |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI ಸಂಪನ್ಮೂಲಕ್ಕೆ ನಿಯೋಜಿಸಿದ ಏಂಡ್‌ಪಾಯಿಂಟ್ |
| AZURE_OPENAI_DEPLOYMENT | _ಟೆಕ್ಸ್ಟ್ ಜನರೇಶನ್_ ಮಾದರಿ ನಿಯೋಜನೆ ಏಂಡ್‌ಪಾಯಿಂಟ್ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _ಟೆಕ್ಸ್ಟ್ ಇಮ್ಬೆಡ್ಡಿಂಗ್_ ಮಾದರಿ ನಿಯೋಜನೆ ಏಂಡ್‌ಪಾಯಿಂಟ್ |
| AZURE_INFERENCE_ENDPOINT | ನಿಮ್ಮ Microsoft Foundry ಪ್ರಾಜೆಕ್ಟ್‌ಗೆ ಇರುವ ಏಂಡ್‌ಪಾಯಿಂಟ್, Microsoft Foundry Models‌ಗೆ ಉಪಯುಕ್ತ |
| AZURE_INFERENCE_CREDENTIAL | ನಿಮ್ಮ Microsoft Foundry ಪ್ರಾಜೆಕ್ಟ್‌ಗೆ API ಕೀ |
| | |

ಟಿಪ್ಪಣಿ: ಕೊನೆಯ ಎರಡು Azure OpenAI ಚರಗಳು ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ (ಟೆಕ್ಸ್ಟ್ ಜನರೇಶನ್) ಮತ್ತು ವೆಕ್ಟರ್ ಹುಡುಕು (ಇಮ್ಬೆಡ್ಡಿಂಗ್‌ಗಳು)ಕ್ಕಾಗಿ ಡಿಫಾಲ್ಟ್ ಮಾದರಿಯನ್ನು ಪ್ರತಿಬಿಂಬಿಸುತ್ತವೆ. ಅವುಗಳನ್ನು ಸಂರಚಿಸುವ ಸೂಚನೆಗಳನ್ನು ಸಂಬಂಧಿತ ಪ್ರೌಢಶಾಲಾ ಕಾರ್ಯಗಳಲ್ಲಿ ನೀಡಲಾಗುತ್ತದೆ.

## Azure OpenAI ಅನ್ನು ಸಂರಚಿಸಿ: ಪೋರ್ಟಲ್‌ನಿಂದ

> **ಟಿಪ್ಪಣಿ:** ಈಗ Azure OpenAI ಸೇವೆ [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ಭಾಗವಾಗಿದೆ. ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ನಿಯೋಜನೆಗಳು ಇನ್ನೂ Azure ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಕಾಣಿಸುತ್ತವೆ, ಆದರೆ ಪ್ರತಿದಿನದ ಮಾದರಿ ನಿರ್ವಹಣೆ (ನಿಯೋಜನೆ, ಪ್ಲೇಗ್ರೌಂಡ್, ಮಾನಿಟರಿಂಗ್) ಈಗ ಹಳೆಯ "Azure OpenAI Studio" ಬದಲಿಗೆ Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿದೆ.

Azure OpenAI ಏಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು ಕೀ ಮೌಲ್ಯಗಳನ್ನು ನಾವು [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)ನಲ್ಲಿ ಕಂಡುಕೊಳ್ಳಬಹುದು, ಆದ್ದರಿಂದ ಅಲ್ಲಿ ಪ್ರಾರಂಭಿಸೋಣ.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ಗೆ ಹೋಗಿ
1. ಸೈಡ್‌ಬಾರ್‌ನಲ್ಲಿ (ಎಡ ಪರ ಮেন್ಯೂ) **Keys and Endpoint** ಆಯ್ಕೆಮಾಡಿ.
1. **Show Keys** ಕ್ಲಿಕ್ ಮಾಡಿ - KEY 1, KEY 2 ಮತ್ತು Endpoint ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತವೆ.
1. AZURE_OPENAI_API_KEY ಗೆ KEY 1 ಮೌಲ್ಯವನ್ನು ಉಪಯೋಗಿಸಿ
1. AZURE_OPENAI_ENDPOINT ಗೆ Endpoint ಮೌಲ್ಯವನ್ನು ಉಪಯೋಗಿಸಿ

ನಂತರ, ನಾವು ನಿಯೋಜಿಸಿರುವ ನಿರ್ದಿಷ್ಟ ಮಾದರಿಗಳ ಏಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಬೇಕಾಗಿವೆ.

1. Azure OpenAI ಸಂಪನ್ಮೂಲಕ್ಕೆ ಸೈಡ್‌ಬಾರ್‌ನಲ್ಲಿ (ಎಡ ಮেন್ಯೂ) **Model deployments** ಆಯ್ಕೆ ಮಾಡಿ.
1. ಗಮ್ಯಸ್ಥಳ ಪುಟದಲ್ಲಿ **Go to Microsoft Foundry portal** (ಅಥವಾ ನಿಮ್ಮ ಸಂಪನ್ಮೂಲ ಪ್ರಕಾರಕ್ಕೆ ಆಹಾರವಾಗುವಂತೆ **Manage Deployments**) ಕ್ಲಿಕ್ ಮಾಡಿ

ಇದು ನಿಮ್ಮನ್ನು Microsoft Foundry ಪೋರ್ಟಲ್‌ಗೆ ತರುತ್ತದೆ, ಅಲ್ಲಿ ಮುಂದಿನಂತೆ ಮೌಲ್ಯಗಳನ್ನು ಕಂಡುಹಿಡಿಯುತ್ತೇವೆ.

## Azure OpenAI ಅನ್ನು ಸಂರಚಿಸಿ: Microsoft Foundry ಪೋರ್ಟಲ್‌ನಿಂದ

1. ಮೇಲಿನಂತೆ ನಿಮ್ಮ ಸಂಪನ್ಮೂಲದಿಂದ [Microsoft Foundry ಪೋರ್ಟಲ್](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ಗೆ ಹೋಗಿ.
1. **Deployments** ಟ್ಯಾಬ್‌ ಅನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ (ಎಡಪಟ್ಟಿ) - ಇದರಲ್ಲಿ ಈಗ ನಿಯೋಜಿಸಿದ ಮಾದರಿಗಳು ಕಾಣಿಸುತ್ತವೆ.
1. ನೀವು ಬೇಕಾದ ಮಾದರಿ ನಿಯೋಜಿಸದಿದ್ದರೆ, [ಮಾದರಿ ಕ್ಯಾಟಲಾಗ್](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ನಿಂದ ಅದನ್ನು ನಿಯೋಜಿಸಲು **Deploy model** ಬಳಸಿ.
1. ನೀವು _ಟೆಕ್ಸ್ಟ್-ಜನರೇಶನ್_ ಮಾದರಿಯ ಅವಶ್ಯಕತೆ ಇದೆ - ನಾವು ಶಿಫಾರಸು ಮಾಡೋದು: **gpt-5-mini**
1. ನೀವು _ಟೆಕ್ಸ್ಟ್-ಇಮ್ಬೆಡ್ಡಿಂಗ್_ ಮಾದರಿಯ ಅವಶ್ಯಕತೆ ಇದೆ - ನಾವು ಶಿಫಾರಸು ಮಾಡೋದು **text-embedding-3-small**

ಈಗ ವಾತಾವರಣ ಚರಗಳನ್ನು _ನಿಯೋಜನೆ ನಾಮ_ ಅನ್ನು ಪ್ರತಿಬಿಂಬಿಸುವಂತೆ ನವೀಕರಿಸಿ. ನೀವು ಸ್ಪಷ್ಟವಾಗಿ ಬದಲಾಯಿಸದಿದ್ದರೆ, ಇದು ಸಾಮಾನ್ಯವಾಗಿ ಮಾದರಿ ಹೆಸರಿನಷ್ಟೇ ಆಗಿರುತ್ತದೆ. ಉದಾಹರಣೆಗೆ, ನೀವು ಹೊಂದಿರಬಹುದು:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**ಅಂತಿಮವಾಗಿ .env ಫೈಲ್ ಉಳಿಸಲು ಮರೆಯಬೇಡಿ**. ನೀವು ಈಗ ಫೈಲ್ ನಿಂದ ನಿರ್ಗಮಿಸಿ ನೋಟ್ಬುಕ್ ಚಲಿಸಲು ಸೂಚನೆಗಳಿಗೆ ಹಿಂತಿರುಗಬಹುದು.

## OpenAI ಅನ್ನು ಸಂರಚಿಸಿ: ಪ್ರೊಫೈಲ್‌ನಿಂದ

ನಿಮ್ಮ OpenAI API ಕೀ [OpenAI ಖಾತೆಯಲ್ಲಿ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) ದೊರಕಬಹುದು. ನಿಮ್ಮ ಬಳಿ ಇಲ್ಲದಿದ್ದರೆ, ಖಾತೆ ಪಡೆಯಲು ಸಹಿ ಮಾಡಿ ಮತ್ತು API ಕೀ ರಚಿಸಿ. ನೀವು ಕೀ ಪಡೆದ ಬಳಿಕ `.env` ಫೈಲ್‌ನಲ್ಲಿರುವ `OPENAI_API_KEY` ಚರವನ್ನು ತುಂಬಿಕೊಳ್ಳಬಹುದು.

## Hugging Face ಅನ್ನು ಸಂರಚಿಸಿ: ಪ್ರೊಫೈಲ್‌ನಿಂದ

ನಿಮ್ಮ Hugging Face ಟೋಕನ್ ನಿಮ್ಮ ಪ್ರೊಫೈಲ್‌ನ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) ಅಡಿಯಲ್ಲಿ ಸಿಗುತ್ತದೆ. ಇದನ್ನು ಸಾರ್ವಜನಿಕವಾಗಿ ಪೋಸ್ಟ್ ಅಥವಾ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ. ಬದಲಿಗೆ, ಈ ಪ್ರಾಜೆಕ್ಟ್ ಬಳಕೆಗೆ ಹೊಸ ಟೋಕನ್ ರಚಿಸಿ ಅದನ್ನು `.env` ಫೈಲ್‌ನ `HUGGING_FACE_API_KEY` ಚರದೊಳಗೆ ನಕಲಿಸಿ. _ಟಿಪ್:_ ಇದು ತಾಂತ್ರಿಕವಾಗಿ API ಕೀ ಅಲ್ಲ, ಆದರೆ ಪ್ರಮಾಣೀಕರಣಕ್ಕಾಗಿ ಕೂಡ ಉಪಯೋಗಿಸಲಾಗುತ್ತದೆ, ಆದ್ದರಿಂದ ಸಮ್ಮಿಲನಕ್ಕೆ ಆ ಹೆಸರು ಬಳಸಲಾಗುತ್ತಿದೆ.

## Microsoft Foundry Models ಅನ್ನು ಸಂರಚಿಸಿ: ಪೋರ್ಟಲ್‌ನಿಂದ

> **ಟಿಪ್ಪಣಿ:** GitHub Models ಜುಲೈ 2026 ಕೊನೆಯಲ್ಲಿ ನಿವೃತ್ತವಾಗುತ್ತಿದೆ. ಅದರ ನೇರ ಬದಲಾವಣೆ Microsoft Foundry Models ಆಗಿದ್ದು, ಅದೇ ಉಚಿತ ಪ್ರಯೋಗ ಮಾದರಿ ಕ್ಯಾಟಲಾಗ್ ಮತ್ತು Azure AI ಇನ್ಫರೆನ್ಸ್ SDK / OpenAI SDK ಅನುಭವವನ್ನು ನೀಡುತ್ತದೆ.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ಗೆ ಹೋಗಿ ಮತ್ತು Foundry ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಿ (ಅಥವಾ ತೆರೆಯಿರಿ).
1. [ಮಾದರಿ ಕ್ಯಾಟಲಾಗ್](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)  ಬ್ರೌಸ್ ಮಾಡಿ ಮತ್ತು ಒಂದು ಮಾದರಿ ನಿಯೋಜಿಸಿ, ಉದಾಹರಣೆಗೆ `gpt-5-mini`.
1. ಪ್ರಾಜೆಕ್ಟಿನ **ಅವಲೋಕನ** ಪುಟದಲ್ಲಿ, **ಎಂಡ್‌ಪಾಯಿಂಟ್** ಮತ್ತು **API ಕೀ** ನಕಲಿಸಿ.
1. ನಿಮ್ಮ `.env` ಫೈಲ್‌ನಲ್ಲಿ `AZURE_INFERENCE_ENDPOINT` ಗೆ ಏಂಡ್‌ಪಾಯಿಂಟ್ ಮೌಲ್ಯ ಮತ್ತು `AZURE_INFERENCE_CREDENTIAL` ಗೆ ಕೀ ಮೌಲ್ಯ ಬಳಸಿರಿ.

## ಆಫ್‌ಲೈನ್ / ಸ್ಥಳೀಯ ಪ್ರೊವೈಡರ್‌ಗಳು

ನೀವು ಕ್ಲೌಡ್ ಸಬ್ಸಕ್ರಿಪ್‌ಷನ್ ಬಳಸಬಯಸದಿದ್ದರೆ, ನೀವು ಹೊಂದಿರುವ ಸಾಧನದಲ್ಲಿ ಹೊಂದಿಕೊಂಡ ಮುಕ್ತ ಮಾದರಿಗಳನ್ನು ನೇರವಾಗಿ ಸಂಚಾಲಿಸಬಹುದು:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - ಮೈಕ್ರೋಸಾಫ್ಟ್‌ನ ಸಾಧನಾಧಾರಿತ ರನ್‌ಟೈಮ್. ಇದು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅತ್ಯುತ್ತಮ ನಿರ್ವಹಣಾ ಪ್ರೊವೈಡರ್ (NPU, GPU ಅಥವಾ CPU) ಆಯ್ಕೆಮಾಡುತ್ತದೆ ಮತ್ತು OpenAI-ಅನುಕೂಲ ಏಂಡ್‌ಪಾಯಿಂಟ್ ಒದಗಿಸುತ್ತದೆ, ಅದರಿಂದ ನೀವು ಈ ಕೋರ್ಸಿನ ಉದಾಹರಣಾ ಕೋಡ್ ಅತ್ಯಲ್ಪ ಬದಲಾವಣೆಗಳೊಂದಿಗೆ ಮತ್ತೆ ಬಳಸಬಹುದು. ಪ್ರಾರಂಭಿಸಲು [Foundry Local ಡಾಕ್ಯುಮೆಂಟೇಷನ್](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) ನೋಡಿ ಅಥವಾ `winget install Microsoft.FoundryLocal` (ವಿಂಡೋಸ್) / `brew install microsoft/foundrylocal/foundrylocal` (ಮ್ಯಾಕ್‌ಒಎಸ್) ಮೂಲಕ ಇನ್ಸ್ಟಾಲ್ ಮಾಡಿಕೊಳ್ಳಿ.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral ಮತ್ತು Gemma ಮುಂತಾದ ಮುಕ್ತ ಮಾದರಿಗಳನ್ನು ಸ್ಥಳೀಯವಾಗಿ ಚಲಾಯಿಸಲು ಜನಪ್ರಿಯ ಪರ್ಯಾಯ.


ಎರಡೂ ಆಯ್ಕೆಗಳನ್ನು ಬಳಸಿಕೊಂಡಿರುವ ಪ್ರಾಯೋಗಿಕ ಉದಾಹರಣೆಗಳಿಗೆ [ಪಾಠ 19: SLMs ಜೊತೆ ಶಿಲ್ಪಕಲೆ](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) ನೋಡಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->