# LLM ಪ್ರొವೈಡರ್ ಆಯ್ಕೆ ಮತ್ತು ಸಂರಚನೆ 🔑

ಅಸೈನ್ಮೆಂಟ್ಗಳು ಹೆಚ್ಚಿನದಾಗಿ ಒನ್ ಅಥವಾ ಹೆಚ್ಚಿನ ಲಾರ್ಜ್ ಲ್ಯಾಂಗ್ವೇಜ್ ಮಾದರಿ (LLM) ಡಿಪ್ಲಾಯ್ಮೆಂಟ್‌ಗಳ ವಿರುದ್ಧ ಕೆಲಸ ಮಾಡಲು ಸಹ ಹೊಂದಿಸಲಾಗಬಹುದು, ಉದಾಹರಣೆಗೆ OpenAI, Azure ಅಥವಾ Hugging Face ಹಾಗು ಇತರ ಬೆಂಬಲಿತ ಸೇವೆ ಪ್ರೊವೈಡರ್‌ಗಳು. ಇವು ಒಂದು _ಹೋಸ್ಟ್ ಮಾಡಿದ ಎಂಡ್‌ಪಾಯಿಂಟ್_ (API) ಒದಗಿಸುತ್ತವೆ, ಅದನ್ನು ನಾವು ಸರಿಯಾದ ಪ್ರಮಾಣೀಕರಣ (API ಕೀ ಅಥವಾ ಟೋಕನ್) ಮೂಲಕ ಪ್ರೋಗ್ರಾಮ್ ರೀತಿಯಲ್ಲಿ ಪ್ರವೇಶಿಸಬಹುದು. ಈ ಕೋರ್ಸ್‌ನಲ್ಲಿ ನಾವು ಈ ಪ್ರೊವೈಡರ್ ಗಳ ಬಗ್ಗೆ ಚರ್ಚಿಸುತ್ತೇವೆ:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ವಿವಿಧ ಮಾದರಿಗಳ ಜೊತೆಗೆ, ಮೂಲ GPT ಸರಣಿಯನ್ನು ಒಳಗೊಂಡಂತೆ.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI ಮಾದರಿಗಳಿಗಾಗಿ, ಎಂಟರ್‌ಪ್ರೈಸ್ ಸಿದ್ಧತೆಯನ್ನು ಗಮನದಲ್ಲಿ ಇಟ್ಟುಕೊಂಡು
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ಒಂದು ಏಕ(endpoint) ಮತ್ತು API ಕೀ ಮೂಲಕ OpenAI, Meta, Mistral, Cohere, Microsoft ಮತ್ತು ಇನ್ನಿತರನಿಂದ ನೂರ Kannada ಜನರಿಗೆ ಮಾದರಿಗಳನ್ನು ಪ್ರವೇಶಿಸಲು (GitHub Models ಅನ್ನು ಬದಲಾಗಿಸುತ್ತದೆ, ಇದು ಜುಲೈ 2026 ರ ಅಂತ್ಯದಲ್ಲಿ ನಿವೃತ್ತಿಯಾಗುತ್ತದೆ)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ಮುಕ್ತ ಮೂಲ ಮಾದರಿಗಳು ಮತ್ತು ಇನ್ಫರೆನ್ಸ್ ಸರ್ವರ್
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ಅಥವಾ [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ನೀವು ನಿಮ್ಮ ಸ್ವಂತ ಸಾಧನದಲ್ಲಿ ಪೂರ್ವನಿಗದಿತವಾಗಿ ಮಾದರಿಗಳನ್ನು ಸಂಪೂರ್ಣ ಆಫ್‌ಲೈನ್‌ನಲ್ಲಿ ಚಾಲನೆ ಮಾಡಲು ಬಯಸುವುದಾದರೆ, ಯಾವುದೇ ಕ್ಲೌಡ್ ಚಂದಾದಾರಿಕೆ ಅಗತ್ಯವಿಲ್ಲ.

**ಈ ಅಭ್ಯಾಸಗಳಿಗೆ ನೀವು ನಿಮ್ಮದೇ ಖಾತೆಗಳನ್ನು ಬಳಸಬೇಕಾಗುತ್ತದೆ**. ಅಸೈನ್ಮೆಂಟ್‌ಗಳು ಆಯ್ಕೆಯಾದ್ದರಿಂದ ನೀವು ಒಂದನ್ನು, ಎಲ್ಲವನ್ನೂ ಅಥವಾ ಯಾವುದೇ ಪ್ರೊವೈಡರ್ ಆಯ್ಕೆಯನ್ನು ನಿಮ್ಮ ಆಸಕ್ತಿಯ ಮೇಲೆ ಆಧರಿಸಿ ಮಾಡಬಹುದು. ಕೆಲವು ಸಹಾಯಕ ಮಾಹಿತಿ ಕೆಳಗಿನಂತಿವೆ:

| ಸೈನ್ ಅಪ್ | ವೆಚ್ಚ | API ಕೀ | ಪ್ಲೇಗ್ರೌಂಡ್ | ಟಿಪ್ಪಣಿಗಳು |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ದರ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ಪ್ರಾಜೆಕ್ಟ್ ಆಧಾರಿತ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ನೋ-ಕೋಡ್, ವೆಬ್](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | ಹಲವು ಮಾದರಿಗಳು ಲಭ್ಯವಿದೆ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ದರ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK ಕ್ವಿಕ್‌ಸ್ಟಾರ್ಟ್](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [ಸ್ಟುಡಿಯೋ ಕ್ವಿಕ್‌ಸ್ಟಾರ್ಟ್](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ಪ್ರವೇಶಕ್ಕಾಗಿ ಮುಂಗಡ ಅರ್ಜಿ ಹಾಕಬೇಕು](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [ದರ](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [ಪ್ರಾಜೆಕ್ಟ್ ಅವಲೋಕನ ಪೇಜ್](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry ಪ್ಲೇಗ್ರೌಂಡ್](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | ಉಚಿತ ಮಟ್ಟ ಲಭ್ಯ; ಹಲವು ಮಾದರಿ ಪ್ರೊವೈಡರುಗಳಿಗೆ ಒಂದು ಎಂಡ್‌ಪಾಯಿಂಟ್ + ಕೀ |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ದರ](https://huggingface.co/pricing) | [ಪ್ರವೇಶ ಟೋಕನ್ಸ್](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ಕೆಲವು ಸಾಧಾರಣ ಮಾದರಿಗಳನ್ನು ಹೊಂದಿದೆ](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ಉಚಿತ (ನಿಮ್ಮ ಸಾಧನದಲ್ಲಿ ಚಾಲನೆ) | ಅಗತ್ಯವಿಲ್ಲ | [ಸ್ಥಳೀಯ CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | ಸಂಪೂರ್ಣ ಆಫ್‌ಲೈನ್, OpenAI-ಸಮ್ಮತಿತ ಎండ్‌ಪಾಯಿಂಟ್ |
| | | | | |

ವಿಭಿನ್ನ ಪ್ರೊವೈಡರ್‌ಗಳೊಂದಿಗೆ ಬಳಸಲು ಈ ರೆಪೊಸಿಟೋರಿಯನ್ನು _ಕಾನ್ಫಿಗರ್_ ಮಾಡಲು ಕೆಳಗಿನ ಸೂಚನೆಯನ್ನು ಅನುಸರಿಸಿ. ಒಂದು ನಿರ್ದಿಷ್ಟ ಪ್ರೊವೈಡರ್ ಅಗತ್ಯವಿರುವ ಅಸೈನ್ಮೆಂಟ್‌ಗಳು ತಮ್ಮ ಫೈಲ್‌ನಾಮದಲ್ಲಿ ಈ ಟ್ಯಾಗ್‌ಗಳನ್ನು ಹೊಂದಿರುತ್ತವೆ:

- `aoai` - ಅಗತ್ಯವಿರುವುದು Azure OpenAI ಎಂಡ್‌ಪಾಯಿಂಟ್, ಕೀ
- `oai` - ಅಗತ್ಯವಿರುವುದು OpenAI ಎಂಡ್‌ಪಾಯಿಂಟ್, ಕೀ
- `hf` - ಅಗತ್ಯವಿರುವುದು Hugging Face ಟೋಕನ್
- `githubmodels` - ಅಗತ್ಯವಿರುವುದು Microsoft Foundry Models ಎಂಡ್‌ಪಾಯಿಂಟ್, ಕೀ (GitHub Models ಜುಲೈ 2026ರ ಕೊನೆಯಲ್ಲಿ ನಿವೃತ್ತಿಯಾಗುತ್ತಿದ್ದರೆ)

ನೀವು ಒಂದು ಅಥವಾ ಎಲ್ಲ ಪ್ರೊವೈಡರ್‌ಗಳನ್ನು ಸಂರಚಿಸಬಹುದು ಅಥವಾ ಒಂದು ಪ್ರಮಾಣಪತ್ರ ಇಲ್ಲದೇ ಇರಬಹುದು. ಸಂಬಂಧಿಸಿದ ಅಸೈನ್ಮೆಂಟ್‌ಗಳು ಸರಿಯಾದ ಪ್ರಮಾಣಪತ್ರಗಳಿಲ್ಲದಿದ್ದಲ್ಲಿ ದೋಷ ತೋರಿಸುತ್ತವೆ.

## `.env` ಫೈಲ್ ರಚನೆ

ಮೊದಲು ನೀವು ಮೇಲಿನ ಮಾರ್ಗದರ್ಶನವನ್ನು ಓದಿ ಸಂಬಂಧಪಟ್ಟ ಪ್ರೊವೈಡರ್ ಜೊತೆ ಸೈನ್ ಅಪ್ ಮಾಡಿಕೊಂಡಿದ್ದೀರಾ ಮತ್ತು ಅಗತ್ಯವಿರುವ ಪ್ರಮಾಣೀಕರಣ (API_KEY ಅಥವಾ ಟೋಕನ್) ಪಡೆದಿದ್ದೀರಾ ಎಂದು ನಾವು ಊಹಿಸುತ್ತೇವೆ. Azure OpenAI ಬಗ್ಗೆ ಮಾತನಾಡಿದರೆ, ನಿಮಗೆ ಕನಿಷ್ಟ ಒಂದು GPT ಮಾದರಿಯನ್ನು ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸಲು ಡಿಪ್ಲಾಯ್ ಮಾಡಿರುವ Azure OpenAI ಸೇವೆಯ ಪ್ರಾಮಾಣಿಕ ಡಿಪ್ಲಾಯ್ಮೆಂಟ್ (ಎಂಡ್‌ಪಾಯಿಂಟ್) ಇದೆಯೆಂದು ನಾವು ಊಹಿಸುತ್ತೇವೆ.

ಮುಂದಿನ ಹಂತವೆಂದರೆ ನಿಮ್ಮ **ಸ್ಥಳೀಯ ಪರಿಸರ ಚರ (environment variable) ಗಳನ್ನು** ಕೆಳಗಿನಂತೆ ಕಾನ್ಫಿಗರ್ ಮಾಡುವುದು:

1. ರೂಟ್ ಫೋಲ್ಡರ್‌ನಲ್ಲಿ `.env.copy` ಫೈಲ್ ಇರುತ್ತದೆ, ಅದರಲ್ಲಿ ಈ ರೀತಿ ವಿಷಯ ಇರುತ್ತದೆ ಎಂಬುದನ್ನು ನೋಡಿ:

   ```bash
   # OpenAI ಒದಗಿಸುವವರು
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯಲ್ಲಿ ಆಜೂರ್ OpenAI
   ## (ಆಜೂರ್ OpenAI ಸೇವೆ ಈಗ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯ ಭಾಗವಾಗಿದೆ: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ಡೀಫಾಲ್ಟ್ ಸೆಟ್ ಮಾಡಲಾಗಿದೆ! (ಪ್ರಸ್ತುತ ಸ್ಥಿರ GA API ಆವೃತ್ತಿ)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಮಾದರಿಗಳು (ಬಹು-ಒದಗಿಸುವವರ ಮಾದರಿ ಕ್ಯಾಟಲಾಗ್, ಗಿಥಬ್ ಮಾದರಿಗಳನ್ನು ಬದಲಿಸುತ್ತದೆ, ಜುಲೈ 2026 ಅಂತ್ಯದಲ್ಲಿ ನಿವೃತ್ತಿಯಾಗುತ್ತದೆ)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## ಹಗ್ಗಿಂಗ್ ಫೇಸ್
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. ಈ ಫೈಲ್ ಅನ್ನು ಕೆಳಗಿನ ಆಜ್ಞೆ ಬಳಸಿ `.env` ಗೆ ನಕಲಿಸಿಕೊಳ್ಳಿ. ಈ ಫೈಲ್ _gitignore_ ಆಗಿದ್ದು, ರಹಸ್ಯಗಳನ್ನು ಸುರಕ್ಷಿತವಾಗಿರಿಸುತ್ತದೆ.

   ```bash
   cp .env.copy .env
   ```

3. ಮುಂದಿನ ವಿಭಾಗದಲ್ಲಿ ವಿವರಿಸಿರುವಂತೆ ವಾಲುಗಳನ್ನು (`=` ಬಲ ಭಾಗದಲ್ಲಿರುವ ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್‌ಗಳನ್ನು) ಭರ್ತಿ ಮಾಡಿ.

4. (ಐಚ್ಛಿಕ) ನೀವು GitHub Codespaces ಬಳಸದಿದ್ದರೆ, ನೀವು ಈ ರೆಪೊಸಿಟರಿಯಿಂದ ಸಂಬಂಧಿಸಿದ _Codespaces ರಹಸ್ಯಗಳು_ ಆಗಿ ಪರಿಸರ ಚರಗಳನ್ನು ಉಳಿಸುವ ಆಯ್ಕೆ ಇದೆ. ಆ ಸಂದರ್ಭದಲ್ಲಿ ನೀವು ಸ್ಥಳೀಯ `.env` ಫೈಲ್ ಕಾನ್ಫಿಗರ್ ಮಾಡಬೇಕಾಗುವುದಿಲ್ಲ. **ಆದರೆ, ಈ ಆಯ್ಕೆ GitHub Codespaces ಬಳಸುತ್ತಿದ್ದಾಗ ಮಾತ್ರ ಸಕ್ರೀಯವಾಗಿರುತ್ತದೆ ಎಂದು ಗಮನಿಸಿ.** ನೀವು Docker Desktop ಬಳಸಿದರೆ ಇನ್ನೂ `.env` ಫೈಲ್ ಸೆಟ್ ಅಪ್ ಮಾಡಬೇಕಾಗುತ್ತದೆ.

## `.env` ಫೈಲ್ ಭರ್ತಿ ಮಾಡುವುದು

ನಾವು ಈಗ ವೇರಿಯಬಲ್ ಹೆಸರುಗಳೆಂದರೆ ಏನು ಅರ್ಥ ತಂದೆಯೋ ಅವುಗಳ ಮೇಲೆ ಸಂಕ್ಷಿಪ್ತವಾಗಿ ಒಂದು ನೋಟ ಹಿಡಿಯೋಣ:

| ವೇರಿಯಬಲ್  | ವಿವರ  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ನೀವು ನಿಮ್ಮ ಪ್ರೊಫೈಲ್‌ನಲ್ಲಿ ಸಜ್ಜುಗೊಳಿಸಿದ ಬಳಕೆದಾರ ಪ್ರವೇಶ ಟೋಕನ್ |
| OPENAI_API_KEY | ಕ್ಲೌಡ್ OpenAI ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಬಳಸಲು ಅಗತ್ಯವಿರುವ ಪ್ರಾಧಿಕಾರ ಕೀ |
| AZURE_OPENAI_API_KEY | ಅದೇ ಸೇವೆಗೆ ಒಳಪಟ್ಟ ಪ್ರಾಧಿಕಾರ ಕೀ |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI ಸಂಪನ್ಮೂಲದ ವೀಕ್ಷಿತ ಎಂಡ್‌ಪಾಯಿಂಟ್ |
| AZURE_OPENAI_DEPLOYMENT | _ಪಠ್ಯ ಉತ್ಪಾದನೆ_ ಮಾದರಿ ಡಿಪ್ಲಾಯ್ಮೆಂಟ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _ಪಠ್ಯ ಎంబೆಡ್ಡಿಂಗ್‌ಗಳು_ ಮಾದರಿ ಡಿಪ್ಲಾಯ್ಮೆಂಟ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ |
| AZURE_INFERENCE_ENDPOINT | ನಿಮ್ಮ Microsoft Foundry ಪ್ರಾಜೆಕ್ಟ್‌ನ ಎಂಡ್‌ಪಾಯಿಂಟ್, Microsoft Foundry Models ಬಳಕೆಗಾಗಿ |
| AZURE_INFERENCE_CREDENTIAL | ನಿಮ್ಮ Microsoft Foundry ಪ್ರಾಜೆಕ್ಟ್‌ಗೆ API ಕೀ |
| | |

ಟಿಪ್ಪಣಿ: ಕೊನೆಯ ಎರಡು Azure OpenAI ವೇರಿಯಬಲ್‌ಗಳು ಪ್ರತಿ ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸಲು (ಪಠ್ಯ ಉತ್ಪಾದನೆ) ಮತ್ತು ವೆಕ್ಟರ್ ಅನ್ವೇಷಣೆಗೆ (ಎಂಬೆಡ್ಡಿಂಗ್‌ಗಳು) ಡೀಫಾಲ್ಟ್ ಮಾದರಿಯನ್ನು ಪ್ರತಿಬಿಂಬಿಸುತ್ತವೆ. ಅವುಗಳನ್ನು ಹೊಂದಿಸುವ ಸೂಚನೆ ಆಗಬೇಕಾದ ವೃತ್ತಾಂತಗಳಿಗೆ ವಿಶೇಷ ಅಸೈನ್ಮೆಂಟ್ಗಳಲ್ಲಿ ನೀಡಲಾಗುತ್ತದೆ.

## Azure OpenAI ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡುವುದು: ಪೋರ್ಟಲ್ ಬಳಸಿ

> **ಟಿಪ್ಪಣಿ:** Azure OpenAI ಸೇವೆ ಈಗ [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ಭಾಗವಾಗಿದೆ. ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಡಿಪ್ಲಾಯ್ಮೆಂಟ್‌ಗಳು ಇನ್ನೂ Azure ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಕಾಣಿಸುತ್ತವೆ, ಆದರೆ ದಿನನಿತ್ಯದ ಮಾದರಿ ನಿರ್ವಹಣೆ (ಡಿಪ್ಲಾಯ್ಮೆಂಟ್ಗಳು, ಪ್ಲೇಗ್ರೌಂಡ್, ಗಮನಿಕೆ) ಹೆಚ್ಚು Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಡೀತು, ಹಳೆಯ ಪ್ರತ್ಯೇಕ "Azure OpenAI ಸ್ಟುಡಿಯೋ" ಅನ್ನು ಬಿಟ್ಟು.

Azure OpenAI ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು ಕೀ ಮೌಲ್ಯಗಳನ್ನು [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ನಲ್ಲಿ ನೋಡಬಹುದು, ಆದ್ದರಿಂದ ಅದರಿಂದ ಪ್ರಾರಂಭಿಸೋಣ.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ಗೆ ಹೋಗಿ
1. ಬಾಗದಲ್ಲಿ (ಎಡ ಮೆನು) **ಕೀಲಿಗಳು ಮತ್ತು ಎಂಡ್‌ಪಾಯಿಂಟ್** ಆಯ್ಕೆ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ.
1. **ಕೀಲಿಗಳನ್ನು ತೋರಿಸಿ** ಕ್ಲಿಕ್ ಮಾಡಿ - ನೀವು ಕೆಳಗಿನವುಗಳನ್ನು ನೋಡಬೇಕು: KEY 1, KEY 2 ಮತ್ತು ಎಂಡ್‌ಪಾಯಿಂಟ್.
1. KEY 1 ಮೌಲ್ಯವನ್ನು `AZURE_OPENAI_API_KEY` ಗಾಗಿ ಬಳಸಿ
1. ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮೌಲ್ಯವನ್ನು `AZURE_OPENAI_ENDPOINT` ಗಾಗಿ ಬಳಸಿ

ಮುಂದಕ್ಕೆ, ನಾವು ಡಿಪ್ಲಾಯ್ ಮಾಡಿದ ನಿರ್ದಿಷ್ಟ ಮಾದರಿಗಳ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಬೇಕಾಗುತ್ತದೆ.

1. ಬಾಗದಲ್ಲಿರುವ **ಮಾದರಿ ಡಿಪ್ಲಾಯ್ಮೆಂಟ್‌ಗಳು** ಆಯ್ಕೆಗೆ ಕ್ಲಿಕ್ ಮಾಡಿ (ಎಡ ಮೆನು, Azure OpenAI ಸಂಪನ್ಮೂಲಕ್ಕಾಗಿ).
1. ಗಮ್ಯಸ್ಥಳ ಪುಟದಲ್ಲಿ, **Microsoft Foundry ಪೋರ್ಟಲ್ ಗೆ ಹೋಗಿ** (ಅಥವಾ ಸಂಪನ್ಮೂಲ ಪ್ರಕಾರದ ಮೇರೆಗೆ **ಡಿಪ್ಲಾಯ್ಮೆಂಟ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸಿ**) ಕ್ಲಿಕ್ ಮಾಡಿ

ಇದರಿಂದ ನೀವು Microsoft Foundry ಪೋರ್ಟಲ್ ಗೆ ಹೋಗುತ್ತೀರಿ, ಅಲ್ಲಿ ಕೆಳಗಿನಂತೆ ಬೇರೆ ಮೌಲ್ಯಗಳನ್ನು ಹುಡುಕುತ್ತೇವೆ.

## Azure OpenAI ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡುವುದು: Microsoft Foundry ಪೋರ್ಟಲ್ ಬಳಸಿ

1. ಮೇಲ್ಕಾಣಿಸಿದಂತೆ ನಿಮ್ಮ ಸಂಪನ್ಮೂಲದಿಂದ [Microsoft Foundry ಪೋರ್ಟಲ್](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ಗೆ ತಲುಪಿರಿ.
1. ಡಿಪ್ಲಾಯ್ ಮಾಡಿದ ಮಾದರಿಗಳನ್ನು ನೋಡಲು ಎಡ ಬಾಗದ **Deployments** ಪರವಾನಗಿ ಕ್ಲಿಕ್ ಮಾಡಿ.
1. ನಿಮ್ಮ ಬಯಸುವ ಮಾದರಿ ಡಿಪ್ಲಾಯ್ ಮಾಡದಿದ್ದರೆ, ಅದನ್ನು [ಮಾದರಿatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ನಿಂದ **Deploy model** ಬಳಸಿ ಡಿಪ್ಲಾಯ್ ಮಾಡಿ.
1. ನೀವು _ಪಠ್ಯ ಉತ್ಪಾದನೆ_ ಮಾದರಿಯನ್ನು ಬೇಕಾಗುತ್ತದೆ - ನಾವು ಶಿಫಾರಸು ಮಾಡಿದ್ದು: **gpt-4o-mini**
1. ನೀವು _ಪಠ್ಯ ಎಂಬೆಡ್ಡಿಂಗ್_ ಮಾದರಿಯನ್ನು ಬೇಕಾಗುತ್ತದೆ - ನಾವು ಶಿಫಾರಸು ಮಾಡಿದ್ದು **text-embedding-3-small**

ಈಗ ವಾತಾವರಣ ಚರಗಳನ್ನು ಡಿಪ್ಲಾಯ್ ಮಾಡಿದ _Deployment name_ ಯಂತೆ ನವೀಕರಿಸಿ. ಇದು ಸಾಮಾನ್ಯವಾಗಿ ಮಾದರಿ ಹೆಸರಿನಂತೆಯೇ ಇರುತ್ತದೆ, ಅಥವಾ ನೀವು ಸ್ಪಷ್ಟವಾಗಿ ಬದಲಾಯಿಸಿದರೆ ಬೇರೆ ಆಗಿರಬಹುದು. ಆದ್ದರಿಂದ ಉದಾಹರಣೆಗೆ, ನೀವು ಹೀಗೆ ಇರುತ್ತದೆ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**ಮುಗಿದ ನಂತರ .env ಫೈಲ್ ಉಳಿಸುವ 것을 ಮಿಸ್ ಮಾಡಿಕೊಳ್ಳಬೇಡಿ**. ನೀವು ಈಗ ಫೈಲ್ ನಿಂದ ಹೊರಬಂದು ನೋಟುಗಳ ನಿರ್ದೇಶನಗಳಿಗೆ ಹಿಂತಿರುಗಬಹುದು.

## OpenAI ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡುವುದು: ಪ್ರೊಫೈಲ್ ಬಳಸಿ

ನಿಮ್ಮ OpenAI API ಕೀ ನಿಮ್ಮ [OpenAI ಖಾತೆಯಲ್ಲಿ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) ದೊರೆಯಾಗುತ್ತದೆ. ಇಲ್ಲದಿದ್ದರೆ, ನೀವು ಖಾತೆ ಸೃಷ್ಟಿಸಿ API ಕೀ ರಚಿಸಬಹುದು. ಕೀ ಸಿಕ್ಕ ನಂತರ, ನಿಮಗೆ `.env` ಫೈಲ್‌ನಲ್ಲಿ `OPENAI_API_KEY` ಪರಿವರ್ತಕ ಭರ್ತಿ ಮಾಡಬಹುದು.

## Hugging Face ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡುವುದು: ಪ್ರೊಫೈಲ್ ಬಳಸಿ

ನಿಮ್ಮ Hugging Face ಟೋಕನ್ ನಿಮ್ಮ ಪ್ರೊಫೈಲ್‌ನಲ್ಲಿ [ಪ್ರವೇಶ ಟೋಕನ್ಸ್](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) ಅಡಿಯಲ್ಲಿ ದೊರೆಯುತ್ತದೆ. ಇವುಗಳನ್ನು ಸಾರ್ವಜನಿಕವಾಗಿ ಪ್ರಕಟಿಸಬೇಡಿ ಅಥವಾ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ. ಬದಲಿಗೆ, ಈ ಪ್ರಾಜೆಕ್ಟ್ ಬಳಕೆಗೆ ಹೊಸ ಟೋಕನ್ ರಚಿಸಿ ಮತ್ತು ಅದನ್ನು `.env` ಫೈಲ್‌ನಲ್ಲಿ `HUGGING_FACE_API_KEY` ಪರಿವರ್ತಕ ಅಡಿಯಲ್ಲಿ ನಕಲಿಸಿ. _ಸೂಚನೆ:_ ಇದು ತಾಂತ್ರಿಕವಾಗಿ API ಕೀ ಅಲ್ಲ, ಆದರೆ ಪ್ರಮಾಣೀಕರಣಕ್ಕೆ ಬಳಸಲಾಗುತ್ತದೆ ಆದ್ದರಿಂದ ನಾವು ಹೆಸರಿನ ಅನುಸರಣೆಯಾಗಿ ಅದರಿಂದ ಬಳಸುತ್ತಿದ್ದೇವೆ.

## Microsoft Foundry Models ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡುವುದು: ಪೋರ್ಟಲ್ ಬಳಸಿ

> **ಟಿಪ್ಪಣಿ:** GitHub Models ಜುಲೈ 2026 ರ ಕೊನೆಯಲ್ಲಿ ನಿವೃತ್ತಿ ಪಡೆಯಲಿದೆ. Microsoft Foundry Models ನೇರ ಬದಲಾವಣೆ ಆಗಿದ್ದು, ಅದೇ ಉಚಿತ ಪ್ರಯತ್ನ ಮಾದರಿ ಕೋಷ್ಟಕ ಮತ್ತು Azure AI Inference SDK / OpenAI SDK ಅನುಭವವನ್ನು ಒದಗಿಸುತ್ತದೆ.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ಗೆ ಹೋಗಿ ಮತ್ತು Foundry ಪ್ರಾಜೆಕ್ಟ್ ಒಂದು ರಚಿಸಿ (ಅಥವಾ ತೆರೆಯಿರಿ).
1. [ಮಾದರಿatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ನಲ್ಲಿ ಸುತ್ತಡಿ ಮತ್ತು ಮಾದರಿ ನಿದರ್ಶಿನವಾಗಿ `gpt-4o-mini` ಅನ್ನು ಡಿಪ್ಲಾಯ್ ಮಾಡಿ.
1. ಪ್ರಾಜೆಕ್ಟ್‌ನ **ಅವಲೋಕನ** ಪುಟದಲ್ಲಿ, **ಎಂಡ್‌ಪಾಯಿಂಟ್** ಮತ್ತು **API ಕೀ** ನಕಲಿಸಿ.
1. `.env` ಫೈಲ್‌ನಲ್ಲಿ `AZURE_INFERENCE_ENDPOINT` ಗೆ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮೌಲ್ಯವನ್ನು, `AZURE_INFERENCE_CREDENTIAL` ಗೆ ಕೀ ಮೌಲ್ಯವನ್ನು ಬಳಸಿ.

## ಆಫ್‌ಲೈನ್ / ಸ್ಥಳೀಯ ಪ್ರೊವೈಡರ್‌ಗಳು

ನೀವು ಕ್ಲೌಡ್ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ ಬಳಸದಹಾಗೂ, ಹೊಂದಿಕೆಯಾಗುವ ಮುಕ್ತ ಮಾದರಿಗಳನ್ನು ನಿಮ್ಮ ಸ್ವಂತ ಸಾಧನದಲ್ಲಿ ನೇರವಾಗಿ ಚಲಾಯಿಸಬಹುದು:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - ಮೈಕ್ರೋಸಾಫ್ಟ್‌ನ ಸಾಧನದ-runtime. ಅದು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಉತ್ತಮ ಕಾರ್ಯಾಚರಣೆ ಪ್ರೊವೈಡರ್ (NPU, GPU ಅಥವಾ CPU) ಆಯ್ಕೆ ಮಾಡುತ್ತದೆ ಮತ್ತು OpenAIಸಮ್ಮತಿತ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ಒದಗಿಸುತ್ತದೆ, ಹೀಗಾಗಿ ನೀವು ಈ ಕೋರ್ಸ್‌ನ ಉದಾಹರಣೆ ಕೋಡ್‌ಗಳ ಬಹುತೇಕ ಭಾಗವನ್ನು ಕನಿಷ್ಠ ಬದಲಾಯಿಸುವ ಮೂಲಕ ಮರುಬಳಸಿ ಮಾಡಬಹುದು. ಪ್ರಾರಂಭಿಸಲು [Foundry Local ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) ನೋಡಿ, ಅಥವಾ `winget install Microsoft.FoundryLocal` (ವಿಂಡೋಸ್) / `brew install microsoft/foundrylocal/foundrylocal` (ಮ್ಯಾಕ್) ಆಜ್ಞೆಗಳೊಂದಿಗೆ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral ಮತ್ತು Gemma ಮುಂತಾದ ಮುಕ್ತ ಮಾದರಿಗಳನ್ನು ಸ್ಥಳೀಯವಾಗಿ ಚಾಲನೆಯಲ್ಲಿರಿಸಲು ಜನಪ್ರಿಯ ಬದಲಿ.


ಎರಡೂ ಆಯ್ಕೆಗಳನ್ನು ಬಳಸಿ ಕೈಯಲ್ಲಿ ಕಲಿಕೆಯ ಉದಾಹರಣೆಗಳಿಗಾಗಿ [ಪಾಠ ೧೯: SLMs ಉಪಯೋಗಿಸಿ ನಿರ್ಮಿಸಲು](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) ಅನ್ನು ನೋಡಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->