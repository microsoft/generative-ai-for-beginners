<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-12-19T20:43:19+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "kn"
}
-->
# ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು

[![ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು](../../../translated_images/kn/09-lesson-banner.906e408c741f4411.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM ಗಳು ಪಠ್ಯ ರಚನೆಗೆ ಮಾತ್ರವಲ್ಲ. ಪಠ್ಯ ವಿವರಣೆಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ರಚಿಸುವುದೂ ಸಾಧ್ಯ. ಚಿತ್ರಗಳನ್ನು ಮಾಧ್ಯಮವಾಗಿ ಹೊಂದಿರುವುದು ಮೆಡ್‌ಟೆಕ್, ವಾಸ್ತುಶಿಲ್ಪ, ಪ್ರವಾಸೋದ್ಯಮ, ಆಟ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ಇನ್ನಷ್ಟು ಕ್ಷೇತ್ರಗಳಲ್ಲಿ ಬಹಳ ಉಪಯುಕ್ತವಾಗಬಹುದು. ಈ ಅಧ್ಯಾಯದಲ್ಲಿ, ನಾವು ಅತ್ಯಂತ ಜನಪ್ರಿಯ ಚಿತ್ರ ರಚನೆ ಮಾದರಿಗಳಾದ DALL-E ಮತ್ತು Midjourney ಅನ್ನು ನೋಡೋಣ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು ಈ ವಿಷಯಗಳನ್ನು ಆವರಿಸುವೆವು:

- ಚಿತ್ರ ರಚನೆ ಮತ್ತು ಅದು ಯಾಕೆ ಉಪಯುಕ್ತವಾಗಿದೆ.
- DALL-E ಮತ್ತು Midjourney, ಅವು ಏನು ಮತ್ತು ಅವು ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ.
- ನೀವು ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸುವಿರಿ.

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು:

- ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ನಿರ್ಮಿಸಬಹುದು.
- ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಗಾಗಿ ಮेटಾ ಪ್ರಾಂಪ್ಟ್‌ಗಳೊಂದಿಗೆ ಗಡಿಗಳನ್ನು ನಿರ್ಧರಿಸಬಹುದು.
- DALL-E ಮತ್ತು Midjourney ಜೊತೆಗೆ ಕೆಲಸ ಮಾಡಬಹುದು.

## ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಏಕೆ ನಿರ್ಮಿಸಬೇಕು?

ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು ಜನರೇಟಿವ್ AI ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಅನ್ವೇಷಿಸಲು ಉತ್ತಮ ಮಾರ್ಗವಾಗಿದೆ. ಅವು ಉದಾಹರಣೆಗೆ ಈ ಕೆಳಗಿನ ಕಾರ್ಯಗಳಿಗೆ ಬಳಸಬಹುದು:

- **ಚಿತ್ರ ಸಂಪಾದನೆ ಮತ್ತು ಸಂಶ್ಲೇಷಣೆ**. ನೀವು ಚಿತ್ರ ಸಂಪಾದನೆ ಮತ್ತು ಚಿತ್ರ ಸಂಶ್ಲೇಷಣೆಯಂತಹ ವಿವಿಧ ಬಳಕೆ ಪ್ರಕರಣಗಳಿಗೆ ಚಿತ್ರಗಳನ್ನು ರಚಿಸಬಹುದು.

- **ವಿವಿಧ ಉದ್ಯಮಗಳಿಗೆ ಅನ್ವಯಿಸುವುದು**. ಅವು ಮೆಡ್‌ಟೆಕ್, ಪ್ರವಾಸೋದ್ಯಮ, ಆಟ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ಇನ್ನಷ್ಟು ಉದ್ಯಮಗಳಿಗೆ ಚಿತ್ರಗಳನ್ನು ರಚಿಸಲು ಬಳಸಬಹುದು.

## ದೃಶ್ಯ: Edu4All

ಈ ಪಾಠದ ಭಾಗವಾಗಿ, ನಾವು ನಮ್ಮ ಸ್ಟಾರ್ಟ್ಅಪ್ Edu4All ಜೊತೆಗೆ ಕೆಲಸ ಮುಂದುವರಿಸುವೆವು. ವಿದ್ಯಾರ್ಥಿಗಳು ತಮ್ಮ ಮೌಲ್ಯಮಾಪನಗಳಿಗೆ ಚಿತ್ರಗಳನ್ನು ರಚಿಸುವರು, ಯಾವ ಚಿತ್ರಗಳು ಎಂಬುದು ವಿದ್ಯಾರ್ಥಿಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿದೆ, ಆದರೆ ಅವು ತಮ್ಮ ಸ್ವಂತ ಕಥೆಯ ಚಿತ್ರಣಗಳು ಅಥವಾ ತಮ್ಮ ಕಥೆಗೆ ಹೊಸ ಪಾತ್ರವನ್ನು ಸೃಷ್ಟಿಸುವುದು ಅಥವಾ ತಮ್ಮ ಕಲ್ಪನೆಗಳು ಮತ್ತು ಸಂಪ್ರದಾಯಗಳನ್ನು ದೃಶ್ಯೀಕರಿಸುವುದಕ್ಕೆ ಸಹಾಯ ಮಾಡಬಹುದು.

ವಿದ್ಯಾರ್ಥಿಗಳು ತರಗತಿಯಲ್ಲಿ ಸ್ಮಾರಕಗಳ ಮೇಲೆ ಕೆಲಸ ಮಾಡುತ್ತಿದ್ದರೆ Edu4All ವಿದ್ಯಾರ್ಥಿಗಳು ಉದಾಹರಣೆಗೆ ಏನನ್ನು ರಚಿಸಬಹುದು:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/kn/startup.94d6b79cc4bb3f5a.png)

ಈ ರೀತಿಯ ಪ್ರಾಂಪ್ಟ್ ಬಳಸಿ

> "ಬೆಳಗಿನ ಸೂರ್ಯನ ಬೆಳಕಿನಲ್ಲಿ ಐಫೆಲ್ ಟವರ್ ಬಳಿ ನಾಯಿ"

## DALL-E ಮತ್ತು Midjourney ಎಂದರೆ ಏನು?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ಮತ್ತು [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ಅತ್ಯಂತ ಜನಪ್ರಿಯ ಚಿತ್ರ ರಚನೆ ಮಾದರಿಗಳಾಗಿವೆ, ಅವು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಿ ಚಿತ್ರಗಳನ್ನು ರಚಿಸಲು ಅನುಮತಿಸುತ್ತವೆ.

### DALL-E

DALL-E ನಿಂದ ಪ್ರಾರಂಭಿಸೋಣ, ಇದು ಪಠ್ಯ ವಿವರಣೆಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ರಚಿಸುವ ಜನರೇಟಿವ್ AI ಮಾದರಿಯಾಗಿದೆ.

> [DALL-E ಎರಡು ಮಾದರಿಗಳ ಸಂಯೋಜನೆ, CLIP ಮತ್ತು ಡಿಫ್ಯೂಸ್‌ಡ್ ಅಟೆಂಶನ್](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, ಚಿತ್ರಗಳು ಮತ್ತು ಪಠ್ಯದಿಂದ ಡೇಟಾದ ಸಂಖ್ಯಾತ್ಮಕ ಪ್ರತಿನಿಧಾನಗಳಾದ ಎम्बೆಡ್ಡಿಂಗ್‌ಗಳನ್ನು ರಚಿಸುವ ಮಾದರಿ.

- **ಡಿಫ್ಯೂಸ್‌ಡ್ ಅಟೆಂಶನ್**, ಎम्बೆಡ್ಡಿಂಗ್‌ಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ರಚಿಸುವ ಮಾದರಿ. DALL-E ಚಿತ್ರಗಳು ಮತ್ತು ಪಠ್ಯದ ಡೇಟಾಸೆಟ್‌ನಲ್ಲಿ ತರಬೇತಿಗೊಂಡಿದ್ದು, ಪಠ್ಯ ವಿವರಣೆಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ರಚಿಸಲು ಬಳಸಬಹುದು. ಉದಾಹರಣೆಗೆ, DALL-E ಟೋಪಿ ಧರಿಸಿರುವ ಬೆಕ್ಕಿನ ಚಿತ್ರ ಅಥವಾ ಮೊಹಾಕ್ ಹೊಂದಿರುವ ನಾಯಿಯ ಚಿತ್ರವನ್ನು ರಚಿಸಬಹುದು.

### Midjourney

Midjourney ಕೂಡ DALL-E ಹಾಗೆಯೇ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ, ಇದು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್‌ಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ರಚಿಸುತ್ತದೆ. Midjourney ಕೂಡ “ಟೋಪಿ ಧರಿಸಿರುವ ಬೆಕ್ಕು” ಅಥವಾ “ಮೊಹಾಕ್ ಹೊಂದಿರುವ ನಾಯಿ” ಎಂಬಂತಹ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಿ ಚಿತ್ರಗಳನ್ನು ರಚಿಸಲು ಬಳಸಬಹುದು.

![Midjourney ಮೂಲಕ ರಚಿಸಲಾದ ಚಿತ್ರ, ಮೆಕ್ಯಾನಿಕಲ್ ಪಿಜನ್](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_ಚಿತ್ರ ಕ್ರೆಡಿಟ್ ವಿಕಿಪೀಡಿಯಾ, Midjourney ಮೂಲಕ ರಚಿಸಲಾದ ಚಿತ್ರ_

## DALL-E ಮತ್ತು Midjourney ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ

ಮೊದಲು, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ಒಂದು ಜನರೇಟಿವ್ AI ಮಾದರಿ ಆಗಿದ್ದು, ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್ ವಾಸ್ತುಶಿಲ್ಪದ ಮೇಲೆ ಆಧಾರಿತವಾಗಿದೆ ಮತ್ತು _ಆಟೋರೆಗ್ರೆಸಿವ್ ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್_ ಅನ್ನು ಹೊಂದಿದೆ.

ಆಟೋರೆಗ್ರೆಸಿವ್ ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್ ಒಂದು ಮಾದರಿ ಪಠ್ಯ ವಿವರಣೆಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ಹೇಗೆ ರಚಿಸುತ್ತದೆ ಎಂದು ನಿರ್ಧರಿಸುತ್ತದೆ, ಇದು ಒಂದೊಂದು ಪಿಕ್ಸೆಲ್ ಅನ್ನು ಕ್ರಮವಾಗಿ ರಚಿಸಿ, ನಂತರ ರಚಿಸಿದ ಪಿಕ್ಸೆಲ್‌ಗಳನ್ನು ಬಳಸಿ ಮುಂದಿನ ಪಿಕ್ಸೆಲ್ ಅನ್ನು ರಚಿಸುತ್ತದೆ. ನ್ಯೂರಲ್ ನೆಟ್‌ವರ್ಕ್‌ನ ಅನೇಕ ಪದರಗಳ ಮೂಲಕ ಪಾಸ್ ಆಗಿ, ಚಿತ್ರ ಪೂರ್ಣಗೊಳ್ಳುವವರೆಗೆ.

ಈ ಪ್ರಕ್ರಿಯೆಯಿಂದ, DALL-E ಚಿತ್ರದಲ್ಲಿ ಗುಣಲಕ್ಷಣಗಳು, ವಸ್ತುಗಳು, ಲಕ್ಷಣಗಳು ಮತ್ತು ಇನ್ನಷ್ಟು ನಿಯಂತ್ರಿಸುತ್ತದೆ. ಆದಾಗ್ಯೂ, DALL-E 2 ಮತ್ತು 3 ರಲ್ಲಿ ರಚಿಸಲಾದ ಚಿತ್ರಗಳ ಮೇಲೆ ಹೆಚ್ಚು ನಿಯಂತ್ರಣವಿದೆ.

## ನಿಮ್ಮ ಮೊದಲ ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸುವುದು

ಆದ್ದರಿಂದ ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸಲು ಏನು ಬೇಕಾಗುತ್ತದೆ? ನಿಮಗೆ ಕೆಳಗಿನ ಲೈಬ್ರರಿಗಳು ಬೇಕಾಗಿವೆ:

- **python-dotenv**, ನಿಮ್ಮ ರಹಸ್ಯಗಳನ್ನು ಕೋಡ್‌ನಿಂದ ದೂರದಲ್ಲಿರುವ _.env_ ಫೈಲ್‌ನಲ್ಲಿ ಇಡಲು ಈ ಲೈಬ್ರರಿ ಬಳಸಲು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ.
- **openai**, OpenAI API ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಲು ಈ ಲೈಬ್ರರಿ ಬಳಸಲಾಗುತ್ತದೆ.
- **pillow**, Python ನಲ್ಲಿ ಚಿತ್ರಗಳೊಂದಿಗೆ ಕೆಲಸ ಮಾಡಲು.
- **requests**, HTTP ವಿನಂತಿಗಳನ್ನು ಮಾಡಲು ಸಹಾಯ ಮಾಡಲು.

## Azure OpenAI ಮಾದರಿಯನ್ನು ರಚಿಸಿ ಮತ್ತು ನಿಯೋಜಿಸಿ

ಇನ್ನೂ ಮಾಡದಿದ್ದರೆ, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) ಪುಟದಲ್ಲಿ ನೀಡಲಾದ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ
Azure OpenAI ಸಂಪನ್ಮೂಲ ಮತ್ತು ಮಾದರಿಯನ್ನು ರಚಿಸಿ. ಮಾದರಿಯಾಗಿ DALL-E 3 ಆಯ್ಕೆಮಾಡಿ.

## ಅಪ್ಲಿಕೇಶನ್ ರಚಿಸಿ

1. ಕೆಳಗಿನ ವಿಷಯವನ್ನು ಹೊಂದಿರುವ _.env_ ಫೈಲ್ ರಚಿಸಿ:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   ನಿಮ್ಮ ಸಂಪನ್ಮೂಲದ "Deployments" ವಿಭಾಗದಲ್ಲಿ ಈ ಮಾಹಿತಿಯನ್ನು Azure OpenAI Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಹುಡುಕಿ.

1. ಮೇಲಿನ ಲೈಬ್ರರಿಗಳನ್ನು _requirements.txt_ ಎಂಬ ಫೈಲ್‌ನಲ್ಲಿ ಸಂಗ್ರಹಿಸಿ:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. ನಂತರ, ವರ್ಚುವಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ರಚಿಸಿ ಮತ್ತು ಲೈಬ್ರರಿಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   ವಿಂಡೋಸ್‌ನಲ್ಲಿ, ನಿಮ್ಮ ವರ್ಚುವಲ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್ ರಚಿಸಲು ಮತ್ತು ಸಕ್ರಿಯಗೊಳಿಸಲು ಕೆಳಗಿನ ಆಜ್ಞೆಗಳನ್ನು ಬಳಸಿ:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ ಎಂಬ ಫೈಲ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # dotenv ಅನ್ನು ಆಮದುಮಾಡಿ
    dotenv.load_dotenv()
    
    # Azure OpenAI ಸೇವಾ ಕ್ಲೈಂಟ್ ಅನ್ನು ಸಂರಚಿಸಿ
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # ಚಿತ್ರ ರಚನೆ API ಬಳಸಿ ಚಿತ್ರವನ್ನು ರಚಿಸಿ
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # ಸಂಗ್ರಹಿಸಲಾದ ಚಿತ್ರಕ್ಕಾಗಿ ಡೈರೆಕ್ಟರಿಯನ್ನು ಸೆಟ್ ಮಾಡಿ
        image_dir = os.path.join(os.curdir, 'images')

        # ಡೈರೆಕ್ಟರಿ ಇಲ್ಲದಿದ್ದರೆ, ಅದನ್ನು ರಚಿಸಿ
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # ಚಿತ್ರ ಮಾರ್ಗವನ್ನು ಪ್ರಾರಂಭಿಸಿ (ಫೈಲ್ ಪ್ರಕಾರ png ಆಗಿರಬೇಕು ಎಂದು ಗಮನಿಸಿ)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # ರಚಿಸಲಾದ ಚಿತ್ರವನ್ನು ಪಡೆಯಿರಿ
        image_url = generation_response.data[0].url  # ಪ್ರತಿಕ್ರಿಯೆಯಿಂದ ಚಿತ್ರ URL ಅನ್ನು ಹೊರತೆಗೆಯಿರಿ
        generated_image = requests.get(image_url).content  # ಚಿತ್ರವನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # ಡೀಫಾಲ್ಟ್ ಚಿತ್ರ ವೀಕ್ಷಕದಲ್ಲಿ ಚಿತ್ರವನ್ನು ಪ್ರದರ್ಶಿಸಿ
        image = Image.open(image_path)
        image.show()

    # исключенияಗಳನ್ನು ಹಿಡಿಯಿರಿ
    except openai.InvalidRequestError as err:
        print(err)
   ```

ಈ ಕೋಡ್ ಅನ್ನು ವಿವರಿಸೋಣ:

- ಮೊದಲು, ನಾವು ಬೇಕಾದ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳುತ್ತೇವೆ, ಇದರಲ್ಲಿ OpenAI ಲೈಬ್ರರಿ, dotenv ಲೈಬ್ರರಿ, requests ಲೈಬ್ರರಿ ಮತ್ತು Pillow ಲೈಬ್ರರಿ ಸೇರಿವೆ.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- ನಂತರ, _.env_ ಫೈಲ್‌ನಿಂದ ಪರಿಸರ ಚರಗಳನ್ನು ಲೋಡ್ ಮಾಡುತ್ತೇವೆ.

  ```python
  # ಡಾಟ್‌ಎನ್‌ವಿಯನ್ನು ಆಮದುಮಾಡಿ
  dotenv.load_dotenv()
  ```

- ನಂತರ, Azure OpenAI ಸೇವಾ ಕ್ಲೈಂಟ್ ಅನ್ನು ಸಂರಚಿಸುತ್ತೇವೆ

  ```python
  # ಪರಿಸರ ಚರಗಳಿಂದ ಎಂಡ್ಪಾಯಿಂಟ್ ಮತ್ತು ಕೀ ಪಡೆಯಿರಿ
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- ನಂತರ, ಚಿತ್ರವನ್ನು ರಚಿಸುತ್ತೇವೆ:

  ```python
  # ಚಿತ್ರ ರಚಿಸಲು ಚಿತ್ರ ಉತ್ಪಾದನೆ API ಅನ್ನು ಬಳಸಿ
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  ಮೇಲಿನ ಕೋಡ್ ರಚಿಸಲಾದ ಚಿತ್ರದ URL ಅನ್ನು ಹೊಂದಿರುವ JSON ವಸ್ತುವನ್ನು ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತದೆ. ನಾವು URL ಅನ್ನು ಬಳಸಿಕೊಂಡು ಚಿತ್ರವನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ಫೈಲ್‌ಗೆ ಉಳಿಸಬಹುದು.

- ಕೊನೆಗೆ, ಚಿತ್ರವನ್ನು ತೆರೆಯುತ್ತೇವೆ ಮತ್ತು ಸಾಮಾನ್ಯ ಚಿತ್ರ ವೀಕ್ಷಕವನ್ನು ಬಳಸಿ ಅದನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತೇವೆ:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ಚಿತ್ರ ರಚನೆ ಕುರಿತು ಹೆಚ್ಚಿನ ವಿವರಗಳು

ಚಿತ್ರವನ್ನು ರಚಿಸುವ ಕೋಡ್ ಅನ್ನು ಹೆಚ್ಚಿನ ವಿವರದಲ್ಲಿ ನೋಡೋಣ:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, ಚಿತ್ರವನ್ನು ರಚಿಸಲು ಬಳಸುವ ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್. ಈ ಪ್ರಕರಣದಲ್ಲಿ, ನಾವು "ಮೇಡೆಯಲ್ಲಿ ಲಾಲಿಪಾಪ್ ಹಿಡಿದಿರುವ ಕುದುರೆ ಮೇಲೆ ಖರಗಿ, ಅಲ್ಲಿ ಡಾಫೋಡಿಲ್ಸ್ ಬೆಳೆಯುತ್ತವೆ" ಎಂಬ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಬಳಸುತ್ತಿದ್ದೇವೆ.
- **size**, ರಚಿಸಲಾದ ಚಿತ್ರದ ಗಾತ್ರ. ಈ ಪ್ರಕರಣದಲ್ಲಿ, ನಾವು 1024x1024 ಪಿಕ್ಸೆಲ್ ಗಾತ್ರದ ಚಿತ್ರವನ್ನು ರಚಿಸುತ್ತಿದ್ದೇವೆ.
- **n**, ರಚಿಸಲಾದ ಚಿತ್ರಗಳ ಸಂಖ್ಯೆ. ಈ ಪ್ರಕರಣದಲ್ಲಿ, ನಾವು ಎರಡು ಚಿತ್ರಗಳನ್ನು ರಚಿಸುತ್ತಿದ್ದೇವೆ.
- **temperature**, ಜನರೇಟಿವ್ AI ಮಾದರಿಯ ಔಟ್‌ಪುಟ್‌ನ ಯಾದೃಚ್ಛಿಕತೆಯನ್ನು ನಿಯಂತ್ರಿಸುವ ಪರಿಮಾಣ. ತಾಪಮಾನವು 0 ಮತ್ತು 1 ನಡುವಿನ ಮೌಲ್ಯವಾಗಿದ್ದು, 0 ಅಂದರೆ ಔಟ್‌ಪುಟ್ ನಿರ್ಧಾರಾತ್ಮಕವಾಗಿದ್ದು, 1 ಅಂದರೆ ಔಟ್‌ಪುಟ್ ಯಾದೃಚ್ಛಿಕವಾಗಿದೆ. ಡೀಫಾಲ್ಟ್ ಮೌಲ್ಯ 0.7.

ಚಿತ್ರಗಳೊಂದಿಗೆ ನೀವು ಇನ್ನಷ್ಟು ಮಾಡಬಹುದಾದ ವಿಷಯಗಳನ್ನು ಮುಂದಿನ ವಿಭಾಗದಲ್ಲಿ ನಾವು ಆವರಿಸುವೆವು.

## ಚಿತ್ರ ರಚನೆಯ ಹೆಚ್ಚುವರಿ ಸಾಮರ್ಥ್ಯಗಳು

ನೀವು ಈಗಾಗಲೇ Python ನಲ್ಲಿ ಕೆಲವು ಸಾಲುಗಳ ಮೂಲಕ ಚಿತ್ರವನ್ನು ರಚಿಸುವುದನ್ನು ನೋಡಿದ್ದೀರಿ. ಆದರೆ, ಚಿತ್ರಗಳೊಂದಿಗೆ ನೀವು ಇನ್ನಷ್ಟು ಮಾಡಬಹುದು.

ನೀವು ಕೆಳಗಿನವುಗಳನ್ನು ಸಹ ಮಾಡಬಹುದು:

- **ಸಂಪಾದನೆಗಳನ್ನು ನಿರ್ವಹಿಸು**. ಈಗಾಗಿರುವ ಚಿತ್ರಕ್ಕೆ ಮಾಸ್ಕ್ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್ ಒದಗಿಸುವ ಮೂಲಕ, ನೀವು ಚಿತ್ರವನ್ನು ಬದಲಾಯಿಸಬಹುದು. ಉದಾಹರಣೆಗೆ, ಚಿತ್ರದ ಒಂದು ಭಾಗಕ್ಕೆ ಏನಾದರೂ ಸೇರಿಸಬಹುದು. ನಮ್ಮ ಖರಗಿ ಚಿತ್ರವನ್ನು ಕಲ್ಪಿಸಿ, ನೀವು ಖರಗಿಗೆ ಟೋಪಿ ಸೇರಿಸಬಹುದು. ನೀವು ಅದನ್ನು ಹೇಗೆ ಮಾಡುತ್ತೀರಿ ಎಂದರೆ, ಚಿತ್ರ, ಬದಲಾವಣೆಗಾಗಿ ಭಾಗವನ್ನು ಗುರುತಿಸುವ ಮಾಸ್ಕ್ ಮತ್ತು ಏನು ಮಾಡಬೇಕು ಎಂಬ ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್ ಒದಗಿಸುವ ಮೂಲಕ.
> ಗಮನಿಸಿ: ಇದು DALL-E 3 ನಲ್ಲಿ ಬೆಂಬಲಿತವಲ್ಲ.

ಇದು GPT ಚಿತ್ರ ಬಳಸಿ ಉದಾಹರಣೆ:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  ಮೂಲ ಚಿತ್ರದಲ್ಲಿ ಕೇವಲ ಲಾಂಜ್ ಮತ್ತು ಪೂಲ್ ಇರುತ್ತದೆ ಆದರೆ ಅಂತಿಮ ಚಿತ್ರದಲ್ಲಿ ಫ್ಲಾಮಿಂಗೋ ಇರುತ್ತದೆ:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/kn/sunlit_lounge.a75a0cb61749db0e.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/kn/mask.1b2976ccec9e011e.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/kn/sunlit_lounge_result.76ae02957c0bbeb8.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **ವೈವಿಧ್ಯಗಳನ್ನು ರಚಿಸು**. ನೀವು ಈಗಾಗಿರುವ ಚಿತ್ರವನ್ನು ತೆಗೆದುಕೊಂಡು, ವೈವಿಧ್ಯಗಳನ್ನು ರಚಿಸುವಂತೆ ಕೇಳಬಹುದು. ವೈವಿಧ್ಯವನ್ನು ರಚಿಸಲು, ನೀವು ಚಿತ್ರ ಮತ್ತು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್ ಒದಗಿಸಿ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಬಳಸಬಹುದು:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > ಗಮನಿಸಿ, ಇದು OpenAI ನಲ್ಲಿ ಮಾತ್ರ ಬೆಂಬಲಿತವಾಗಿದೆ

## ತಾಪಮಾನ

ತಾಪಮಾನವು ಜನರೇಟಿವ್ AI ಮಾದರಿಯ ಔಟ್‌ಪುಟ್‌ನ ಯಾದೃಚ್ಛಿಕತೆಯನ್ನು ನಿಯಂತ್ರಿಸುವ ಪರಿಮಾಣ. ತಾಪಮಾನವು 0 ಮತ್ತು 1 ನಡುವಿನ ಮೌಲ್ಯವಾಗಿದ್ದು, 0 ಅಂದರೆ ಔಟ್‌ಪುಟ್ ನಿರ್ಧಾರಾತ್ಮಕವಾಗಿದ್ದು, 1 ಅಂದರೆ ಔಟ್‌ಪುಟ್ ಯಾದೃಚ್ಛಿಕವಾಗಿದೆ. ಡೀಫಾಲ್ಟ್ ಮೌಲ್ಯ 0.7.

ತಾಪಮಾನ ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ ಎಂಬುದರ ಉದಾಹರಣೆಯನ್ನು ನೋಡೋಣ, ಈ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಎರಡು ಬಾರಿ ಚಲಾಯಿಸುವ ಮೂಲಕ:

> ಪ್ರಾಂಪ್ಟ್ : "ಮೇಡೆಯಲ್ಲಿ ಲಾಲಿಪಾಪ್ ಹಿಡಿದಿರುವ ಕುದುರೆ ಮೇಲೆ ಖರಗಿ, ಅಲ್ಲಿ ಡಾಫೋಡಿಲ್ಸ್ ಬೆಳೆಯುತ್ತವೆ"

![ಲಾಲಿಪಾಪ್ ಹಿಡಿದಿರುವ ಕುದುರೆ ಮೇಲೆ ಖರಗಿ, ಆವೃತ್ತಿ 1](../../../translated_images/kn/v1-generated-image.a295cfcffa3c13c2.png)

ಈಗ ಅದೇ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಮತ್ತೆ ಚಲಾಯಿಸಿ, ನಾವು ಎರಡು ಬಾರಿ ಅದೇ ಚಿತ್ರವನ್ನು ಪಡೆಯುವುದಿಲ್ಲ ಎಂದು ನೋಡೋಣ:

![ಖರಗಿ ಮೇಲೆ ಕುದುರೆ ಚಿತ್ರ ರಚನೆ](../../../translated_images/kn/v2-generated-image.33f55a3714efe61d.png)

ನೀವು ನೋಡಬಹುದು, ಚಿತ್ರಗಳು ಸಮಾನವಾಗಿವೆ, ಆದರೆ ಒಂದೇ ಅಲ್ಲ. ತಾಪಮಾನ ಮೌಲ್ಯವನ್ನು 0.1 ಗೆ ಬದಲಾಯಿಸಿ ಏನಾಗುತ್ತದೆ ಎಂದು ನೋಡೋಣ:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # ನಿಮ್ಮ ಪ್ರಾಂಪ್ಟ್ ಪಠ್ಯವನ್ನು ಇಲ್ಲಿ ನಮೂದಿಸಿ
        size='1024x1024',
        n=2
    )
```

### ತಾಪಮಾನ ಬದಲಾವಣೆ

ಆದ್ದರಿಂದ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಹೆಚ್ಚು ನಿರ್ಧಾರಾತ್ಮಕವಾಗಿಸಲು ಪ್ರಯತ್ನಿಸೋಣ. ನಾವು ರಚಿಸಿದ ಎರಡು ಚಿತ್ರಗಳಿಂದ ಗಮನಿಸಿದರೆ, ಮೊದಲ ಚಿತ್ರದಲ್ಲಿ ಖರಗಿ ಇದೆ ಮತ್ತು ಎರಡನೇ ಚಿತ್ರದಲ್ಲಿ ಕುದುರೆ ಇದೆ, ಆದ್ದರಿಂದ ಚಿತ್ರಗಳು ಬಹಳ ವ್ಯತ್ಯಾಸ ಹೊಂದಿವೆ.

ಆದ್ದರಿಂದ ನಮ್ಮ ಕೋಡ್ ಬದಲಾಯಿಸಿ ತಾಪಮಾನವನ್ನು 0 ಗೆ ಸೆಟ್ ಮಾಡೋಣ, ಹೀಗೆ:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # ನಿಮ್ಮ ಪ್ರಾಂಪ್ಟ್ ಪಠ್ಯವನ್ನು ಇಲ್ಲಿ ನಮೂದಿಸಿ
        size='1024x1024',
        n=2,
        temperature=0
    )
```

ಈ ಕೋಡ್ ಅನ್ನು ಚಲಾಯಿಸಿದಾಗ, ನೀವು ಈ ಎರಡು ಚಿತ್ರಗಳನ್ನು ಪಡೆಯುತ್ತೀರಿ:

- ![ತಾಪಮಾನ 0, ಆವೃತ್ತಿ 1](../../../translated_images/kn/v1-temp-generated-image.a4346e1d2360a056.png)
- ![ತಾಪಮಾನ 0 , ಆವೃತ್ತಿ 2](../../../translated_images/kn/v2-temp-generated-image.871d0c920dbfb0f1.png)

ಇಲ್ಲಿ ನೀವು ಸ್ಪಷ್ಟವಾಗಿ ಚಿತ್ರಗಳು ಪರಸ್ಪರ ಹೆಚ್ಚು ಹೋಲಿಕೆ ಹೊಂದಿರುವುದನ್ನು ನೋಡಬಹುದು.

## ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಗಾಗಿ ಮेटಾಪ್ರಾಂಪ್ಟ್‌ಗಳೊಂದಿಗೆ ಗಡಿಗಳನ್ನು ಹೇಗೆ ನಿರ್ಧರಿಸಬೇಕು

ನಮ್ಮ ಡೆಮೊ ಮೂಲಕ, ನಾವು ಈಗಾಗಲೇ ನಮ್ಮ ಗ್ರಾಹಕರಿಗಾಗಿ ಚಿತ್ರಗಳನ್ನು ರಚಿಸಬಹುದು. ಆದಾಗ್ಯೂ, ನಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಗಾಗಿ ಕೆಲವು ಗಡಿಗಳನ್ನು ರಚಿಸುವ ಅಗತ್ಯವಿದೆ.

ಉದಾಹರಣೆಗೆ, ನಾವು ಕೆಲಸಕ್ಕೆ ಸೂಕ್ತವಲ್ಲದ ಅಥವಾ ಮಕ್ಕಳಿಗೆ ಅನುವು ಮಾಡಿಕೊಡದ ಚಿತ್ರಗಳನ್ನು ರಚಿಸಲು ಬಯಸುವುದಿಲ್ಲ.

ನಾವು ಇದನ್ನು _ಮೆಟಾಪ್ರಾಂಪ್ಟ್‌ಗಳು_ ಮೂಲಕ ಮಾಡಬಹುದು. ಮೆಟಾಪ್ರಾಂಪ್ಟ್‌ಗಳು ಜನರೇಟಿವ್ AI ಮಾದರಿಯ ಔಟ್‌ಪುಟ್ ಅನ್ನು ನಿಯಂತ್ರಿಸಲು ಬಳಸುವ ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್‌ಗಳಾಗಿವೆ. ಉದಾಹರಣೆಗೆ, ನಾವು ಮೆಟಾಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಔಟ್‌ಪುಟ್ ಅನ್ನು ನಿಯಂತ್ರಿಸಿ, ರಚಿಸಲಾದ ಚಿತ್ರಗಳು ಕೆಲಸಕ್ಕೆ ಸುರಕ್ಷಿತವಾಗಿರಲಿ ಅಥವಾ ಮಕ್ಕಳಿಗೆ ಸೂಕ್ತವಾಗಿರಲಿ ಎಂದು ಖಚಿತಪಡಿಸಬಹುದು.

### ಇದು ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ?

ಮೆಟಾಪ್ರಾಂಪ್ಟ್‌ಗಳು ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತವೆ?

ಮೆಟಾಪ್ರಾಂಪ್ಟ್‌ಗಳು ಜನರೇಟಿವ್ AI ಮಾದರಿಯ ಔಟ್‌ಪುಟ್ ಅನ್ನು ನಿಯಂತ್ರಿಸಲು ಬಳಸುವ ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್‌ಗಳಾಗಿವೆ, ಅವು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್‌ಗಿಂತ ಮುಂಚಿತವಾಗಿ ಇರಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ಮಾದರಿಯ ಔಟ್‌ಪುಟ್ ಅನ್ನು ನಿಯಂತ್ರಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ ಮತ್ತು ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ ಸಂಯೋಜಿಸಲಾಗುತ್ತದೆ. ಪ್ರಾಂಪ್ಟ್ ಇನ್‌ಪುಟ್ ಮತ್ತು ಮೆಟಾ ಪ್ರಾಂಪ್ಟ್ ಇನ್‌ಪುಟ್ ಅನ್ನು ಒಂದೇ ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್‌ನಲ್ಲಿ ಒಳಗೊಂಡಿರುತ್ತದೆ.

ಮೆಟಾ ಪ್ರಾಂಪ್ಟ್‌ನ ಒಂದು ಉದಾಹರಣೆ ಕೆಳಗಿನಂತಿದೆ:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

ಈಗ, ನಮ್ಮ ಡೆಮೊದಲ್ಲಿ ನಾವು ಮೆಟಾಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು ನೋಡೋಣ.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO ಚಿತ್ರವನ್ನು ರಚಿಸಲು ವಿನಂತಿಯನ್ನು ಸೇರಿಸಿ
```

ಮೇಲಿನ ಪ್ರಾಂಪ್ಟ್‌ನಿಂದ, ನೀವು ರಚಿಸಲಾದ ಎಲ್ಲಾ ಚಿತ್ರಗಳು ಮೆಟಾಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಪರಿಗಣಿಸುತ್ತಿರುವುದನ್ನು ನೋಡಬಹುದು.

## ಕಾರ್ಯ - ವಿದ್ಯಾರ್ಥಿಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸೋಣ

ಈ ಪಾಠದ ಆರಂಭದಲ್ಲಿ Edu4All ಅನ್ನು ಪರಿಚಯಿಸಿದ್ದೇವೆ. ಈಗ ವಿದ್ಯಾರ್ಥಿಗಳು ತಮ್ಮ ಮೌಲ್ಯಮಾಪನಗಳಿಗೆ ಚಿತ್ರಗಳನ್ನು ರಚಿಸಲು ಸಕ್ರಿಯಗೊಳ್ಳುವ ಸಮಯ.

ವಿದ್ಯಾರ್ಥಿಗಳು ತಮ್ಮ ಮೌಲ್ಯಮಾಪನಗಳಿಗೆ ಸ್ಮಾರಕಗಳನ್ನು ಒಳಗೊಂಡ ಚಿತ್ರಗಳನ್ನು ರಚಿಸುವರು, ಯಾವ ಸ್ಮಾರಕಗಳು ಎಂಬುದು ವಿದ್ಯಾರ್ಥಿಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿದೆ. ವಿದ್ಯಾರ್ಥಿಗಳು ಈ ಕಾರ್ಯದಲ್ಲಿ ತಮ್ಮ ಸೃಜನಶೀಲತೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಈ ಸ್ಮಾರಕಗಳನ್ನು ವಿಭಿನ್ನ ಸಂದರ್ಭಗಳಲ್ಲಿ ಇರಿಸುವಂತೆ ಕೇಳಲಾಗುತ್ತದೆ.

## ಪರಿಹಾರ

ಇದು ಒಂದು ಸಾಧ್ಯ ಪರಿಹಾರ:
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# dotenv ಅನ್ನು ಆಮದುಮಾಡಿ
dotenv.load_dotenv()

# ಪರಿಸರ ಚರಗಳನ್ನು ಬಳಸಿ ಎಂಡ್ಪಾಯಿಂಟ್ ಮತ್ತು ಕೀ ಪಡೆಯಿರಿ
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # ಚಿತ್ರ ರಚನೆ API ಬಳಸಿ ಚಿತ್ರವನ್ನು ರಚಿಸಿ
    generation_response = client.images.generate(
        prompt=prompt,    # ನಿಮ್ಮ ಪ್ರಾಂಪ್ಟ್ ಪಠ್ಯವನ್ನು ಇಲ್ಲಿ ನಮೂದಿಸಿ
        size='1024x1024',
        n=1,
    )
    # ಸಂಗ್ರಹಿಸಲಾದ ಚಿತ್ರಕ್ಕಾಗಿ ಡೈರೆಕ್ಟರಿಯನ್ನು ಸೆಟ್ ಮಾಡಿ
    image_dir = os.path.join(os.curdir, 'images')

    # ಡೈರೆಕ್ಟರಿ ಇಲ್ಲದಿದ್ದರೆ, ಅದನ್ನು ರಚಿಸಿ
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # ಚಿತ್ರ ಮಾರ್ಗವನ್ನು ಪ್ರಾರಂಭಿಸಿ (ಫೈಲ್ ಪ್ರಕಾರ png ಆಗಿರಬೇಕು ಎಂದು ಗಮನಿಸಿ)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # ರಚಿಸಲಾದ ಚಿತ್ರವನ್ನು ಪಡೆಯಿರಿ
    image_url = generation_response.data[0].url  # ಪ್ರತಿಕ್ರಿಯೆಯಿಂದ ಚಿತ್ರ URL ಅನ್ನು ಹೊರತೆಗೆಯಿರಿ
    generated_image = requests.get(image_url).content  # ಚಿತ್ರವನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # ಡೀಫಾಲ್ಟ್ ಚಿತ್ರ ವೀಕ್ಷಕದಲ್ಲಿ ಚಿತ್ರವನ್ನು ಪ್ರದರ್ಶಿಸಿ
    image = Image.open(image_path)
    image.show()

# исключенияಗಳನ್ನು ಹಿಡಿಯಿರಿ
except openai.BadRequestError as err:
    print(err)
```

## ಅದ್ಭುತ ಕೆಲಸ! ನಿಮ್ಮ ಅಧ್ಯಯನವನ್ನು ಮುಂದುವರೆಸಿ

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನಮ್ಮ [ಜನರೇಟಿವ್ AI ಅಧ್ಯಯನ ಸಂಗ್ರಹ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ಅನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಜನರೇಟಿವ್ AI ಜ್ಞಾನವನ್ನು ಮುಂದುವರೆಸಿ!

ಪಾಠ 10ಕ್ಕೆ ಹೋಗಿ, ಅಲ್ಲಿ ನಾವು [ಕಡಿಮೆ-ಕೋಡ್ ಬಳಸಿ AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದನ್ನು](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) ನೋಡೋಣ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->