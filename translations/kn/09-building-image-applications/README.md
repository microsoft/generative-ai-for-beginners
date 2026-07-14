# ಚಿತ್ರ ಉತ್ಪಾದನಾ ಅಪ್ಲಿಕೇಶನ್ಗಳ ನಿರ್ಮಾಣ

[![ಚಿತ್ರ ಉತ್ಪಾದನಾ ಅಪ್ಲಿಕೇಶನ್ಗಳ ನಿರ್ಮಾಣ](../../../translated_images/kn/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

ಪಠ್ಯದ ತಯಾರಿಕೆಯಿಗಿಂತ LLMಗಳಿಗೆ ಇನ್ನೂ ಹೆಚ್ಚಿನ ಪ್ರಮುಖತೆ ಇದೆ. ಪಠ್ಯ ವಿವರಣೆಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ಕೂಡಾ ತಯಾರಿಸಬಹುದು. ಚಿತ್ರಗಳನ್ನು ಮಾಧ್ಯಮವಾಗಿ ಹೊಂದಿರುವುದು ಮೆಡ್ ಟೆಕ್, ವಾಸ್ತುಕಲೆ, ಪ್ರವಾಸೋದ್ಯಮ, ಆಟಗಳ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ಇನ್ನೂ ಅನೇಕ ಕ್ಷೇತ್ರಗಳಲ್ಲಿ ಬಹು ಉಪಯುಕ್ತವಾಗಬಹುದು. ಈ ಅಧ್ಯಾಯದಲ್ಲಿ, ನಾವು ಪ್ರಧಾನವಾಗಿ ಬಳಸಲ್ಪಡುವ ಎರಡು ಜನರೇಟಿವ್ ಚಿತ್ರ ಮಾದರಿಗಳಾದ DALL-E ಮತ್ತು Midjourney ಅನ್ನು ಪರಿಶೀಲಿಸೋಣ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ನಾವು ಚರ್ಚಿಸುವುದು:

- ಚಿತ್ರ ಉತ್ಪಾದನೆ ಮತ್ತು ಅದರ ಉಪಯುಕ್ತತೆ.
- DALL-E ಮತ್ತು Midjourney, ಅವುಗಳು ಏನು ಮತ್ತು ಅವು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತವೆ.
- ನೀವು ಚಿತ್ರ ಉತ್ಪಾದನಾ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸಬಹುದು.

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ಮೇಲೆ, ನೀವು:

- ಚಿತ್ರ ಉತ್ಪಾದನಾ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸಬಹುದು.
- ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ಗೆ ಮಿತಿಗಳನ್ನು ಮೆಟಾ ಪ್ರಾಂಪ್ಟ್‌ಗಳಿಂದ ನಿರ್ಧರಿಸಬಹುದು.
- DALL-E ಮತ್ತು Midjourney ಸಹ ಕಾರ್ಯನಿರ್ವಹಿಸಬಹುದು.

## ಚಿತ್ರ ಉತ್ಪಾದನಾ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಏಕೆ ನಿರ್ಮಿಸಬೇಕು?

ಚಿತ್ರ ಉತ್ಪಾದನಾ ಅಪ್ಲಿಕೇಶನ್ಗಳು ಜನರೇಟಿವ್ AI ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಅನ್ವೇಷಿಸಲು ಅತ್ಯುತ್ತಮ ಮಾರ್ಗವಾಗಿದೆ. ಉದಾಹರಣೆಗೆ, ಅವುಗಳನ್ನು ಬಳಸಬಹುದು:

- **ಚಿತ್ರ ಸಂಪಾದನೆ ಮತ್ತು ಸಂಶ್ಲೇಷಣೆ**. ಚಿತ್ರ ಸಂಪಾದನೆ ಮತ್ತು ಚಿತ್ರ ಸಂಶ್ಲೇಷಣೆಗೆ ವಿಭಿನ್ನ ಉಪಯೋಗಗಳಿಗೆ ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸಬಹುದು.

- **वಿಭಿನ್ನ ಉದ್ಯಮಗಳಿಗೆ ಅನ್ವಯಿಸಬಹುದು**. ಮೆಡ್ ಟೆಕ್, ಪ್ರವಾಸೋದ್ಯಮ, ಆಟಗಳ ಅಭಿವೃದ್ಧಿ ಮುಂತಾದ ವಿವಿಧ ಉದ್ಯಮಗಳಿಗೆ ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸಲು ಬಳಸಬಹುದು.

## ಸನ್ನಿವೇಶ: Edu4All

ಈ ಪಾಠದ ಭಾಗವಾಗಿ, ನಾವು ನಮ್ಮ ಸ್ಟಾರ್ಟ್‌ಅಪ್ Edu4All ಜೊತೆ ಮುಂದುವರೆಯುವೆವು. ವಿದ್ಯಾರ್ಥಿಗಳು ತಮ್ಮ ಮೌಲ್ಯಮಾಪನಗಳಿಗೆ ಚಿತ್ರಗಳನ್ನು ಸೃಷ್ಟಿಸುವರು, ಯಾವ ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸುವುದು ಎಂಬುದನ್ನು ವಿದ್ಯಾರ್ಥಿಗಳು ನಿರ್ಧರಿಸುವರು, ಆದರೆ ಅವು ತಮ್ಮ ಸ್ವಂತ ಜನಶಿಕ್ಷಣದ ಹಂತ ಅಥವಾ ತಮ್ಮ ಕಥೆಯ ಹೊಸ ಪಾತ್ರ ರಚನೆ ಅಥವಾ ತಮ್ಮ ಕಲ್ಪನೆಗಳನ್ನು ದೃಶ್ಯಾತ್ಮಕವಾಗಿ ಮಾಡುವ ಅವಶ್ಯಕತೆಗಳಿಗೆ ಸಹಾಯ ಮಾಡಬಹುದು.

Edu4All ವಿದ್ಯಾರ್ಥಿಗಳು ತರಗತಿಯಲ್ಲಿ ಸ್ಮಾರಕಗಳ ಮೇಲೆ ಕೆಲಸ ಮಾಡುತ್ತಿದ್ದರೆ ಉದಾಹರಣೆಗೆ ಅವರು ತಯಾರಿಸಬಹುದಾದ ಚಿತ್ರಗಳು ಇದಂತಿವೆ:

![Edu4All ಸ್ಟಾರ್ಟ್‌ಅಪ್, ಸ್ಮಾರಕಗಳ ಕ್ಲಾಸ್, ಐಫಲ್ ಟವರ್](../../../translated_images/kn/startup.94d6b79cc4bb3f5a.webp)

ಅಂತಹ ಪ್ರಾಂಪ್ಟ್ ಬಳಸಿ

> "ಪ್ರಭಾತ ಸೂರ್ಯಕಿರಣಗಳಲ್ಲಿ ಐಫಲ್ ಟವರ್ ಬಳಿ ನಾಯಿ"

## DALL-E ಮತ್ತು Midjourney ಎಂದರೆ ಏನು?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ಮತ್ತು [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ಜನರೇಟಿವ್ ಚಿತ್ರ ಉತ್ಪಾದನಾ ಮಾದರಿಗಳಲ್ಲಿ ಅತ್ಯಂತ ಜನಪ್ರಿಯವಾಗಿವೆ, ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಚಿತ್ರಗಳನ್ನು ಉತ್ಪಾದಿಸಲು ಅನುಮತಿಸುತ್ತವೆ.

### DALL-E

DALL-E ನಿಂದ ಆರಂಭಿಸೋಣ, ಇದು ಪಠ್ಯ ವಿವರಣೆಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸುವ ಒಂದು ಜನರೇಟಿವ್ AI ಮಾದರಿಯಾಗಿದೆ.

> [DALL-E ಎರಡು ಮಾದರಿಗಳ ಸಂಯೋಜನೆಯಾಗಿದೆ, CLIP ಮತ್ತು ಡಿಫ್ಯೂಸ್ ಅಟೆನ್‌ಷನ್](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, ಚಿತ್ರಗಳು ಮತ್ತು ಪಠ್ಯಗಳಿಂದ ಸಂಖ್ಯಾತ್ಮಕ ಪ್ರತಿನಿಧಾನಗಳಾದ ಎম্বೆಡಿಂಗ್‌ಗಳನ್ನು ತಯಾರಿಸುವ ಮಾದರಿ.

- **ಡಿಫ್ಯೂಸ್ ಅಟೆನ್‌ಷನ್**, ಎంబೆಡಿಂಗ್‌ಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸುವ ಮಾದರಿ. DALL-E ಚಿತ್ರಗಳು ಮತ್ತು ಪಠ್ಯಗಳ ಡೇಟಾಸೆಟ್ ಮೇಲೆ ತರಬೇತಿ ಪಡೆದಿದ್ದು, ಪಠ್ಯ ವಿವರಣೆಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸಲು ಬಳಸಬಹುದು. ಉದಾಹರಣೆಗೆ, DALL-E ಹ್ಯಾಟ್ ಹಾಕಿದ ಬೆಕ್ಕಿನ ಚಿತ್ರ ಅಥವಾ ಮೊಹೋಕ್ ಹಾಕಿದ ನಾಯಿ ಚಿತ್ರವನ್ನು ತಯಾರಿಸಲು ಬಳಸಬಹುದು.

### Midjourney

Midjourney ಕೂಡಲೇ DALL-E ತರಹ ಕೆಲಸ ಮಾಡುತ್ತದೆ, ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್‌ಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸುತ್ತದೆ. Midjourney ಕೂಡ "ಹ್ಯಾಟ್ ಹಾಕಿದ ಬೆಕ್ಕು" ಅಥವಾ "ಮೊಹೋಕ್ ಹಾಕಿದ ನಾಯಿ" ಎಂಬ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಿ ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸಲು ಬಳಸಬಹುದು.

![Midjourney ನಿಂದ ತಯಾರ್ ಆದ ಚಿತ್ರ, ಮೆಕ್ಯಾನಿಕಲ್ ಪರಿಪಕ್ಷಿ](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_ಚಿತ್ರ ಕ್ರೆಡಿಟ್ ವಿಕಿಪೀಡಿಯಾ, Midjourney ನಿಂದ ತಯಾರ್ ಆದ ಚಿತ್ರ_

## DALL-E ಮತ್ತು Midjourney ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತವೆ

ಮೊದಲಿಗೆ, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್ ಆರ್ಕಿಟೆಕ್ಚರ್ ಆಧಾರಿತ ಜನರೇಟಿವ್ AI ಮಾದರಿಯಾಗಿದೆ, ಇದರಲ್ಲಿ _ಆಟೊರೆಗ್ರೆಸಿವ್ ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್_ ಬಳಸಿ.

_ಆಟೊರೆಗ್ರೆಸಿವ್ ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್_ ಎನ್ನುವುದು ಮಾದರಿ ಪಠ್ಯ ವಿವರಣೆಗಳಿಂದ ಚಿತ್ರ ತಯಾರಿಸುವ ವಿಧಾನವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ, ಅದು ಒಂದೊಂದು ಪಿಕ್ಸೆಲ್ ಅನ್ನು ಕ್ರಮವಾಗಿ ರಚಿಸಿ ಮುಂದಿನ ಪಿಕ್ಸೆಲ್ ಭೇಟಿ ಮಾಡುತ್ತದೆ. ಇವು ಹಲವು ನ್ಯೂರಲ್ ನೆಟ್‌ವರ್ಕ್ ಲೇಯರ್‌ಗಳನ್ನು ದಾಟಿ ಇಮೇಜ್ ಪೂರ್ಣಗೊಳ್ಳುತ್ತದೆ.

ಈ ಪ್ರಕ್ರಿಯೆಯಲ್ಲಿ, DALL-E ಚಿತ್ರದಲ್ಲಿ ಲಕ್ಷಣಗಳನ್ನು, ವಸ್ತುಗಳನ್ನು, ಗುಣಲಕ್ಷಣಗಳನ್ನು ಮತ್ತು ಇನ್ನೂ ಹಲವಾರು ನಿಯಂತ್ರಿಸುತ್ತದೆ. ಆದಾಗ್ಯೂ, DALL-E 2 ಮತ್ತು 3 ಹೆಚ್ಚು ನಿಯಂತ್ರಣ ಹೊಂದಿವೆ.

## ನಿಮ್ಮ ಮೊದಲ ಚಿತ್ರ ಉತ್ಪಾದನಾ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ನಿರ್ಮಿಸುವುದು

ಚಿತ್ರ ಉತ್ಪಾದನಾ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸಲು ಏನು ಬೇಕು? ನೀವು ಈ ಕೆಳಗಿನ ಲೈಬ್ರರಿಗಳನ್ನು ಅವಶ್ಯಕತೆ ಇರುತ್ತದೆ:

- **python-dotenv**, ನಿಮ್ಮ ಸೀಕ್ರೆಟ್‌ಗಳನ್ನು _.env_ ಫೈಲ್‌ನಲ್ಲಿ ಸಂರಕ್ಷಿಸಲು ಶಿಫಾರಸು.
- **openai**, OpenAI API ನೊಂದಿಗೆ ಸಂವಹನಕ್ಕೆ ಬಳಸುವ ಲೈಬ್ರರಿ.
- **pillow**, Python ನಲ್ಲಿ ಚಿತ್ರಗಳೊಂದಿಗೆ ಕೆಲಸ ಮಾಡಲು.
- **requests**, HTTP ವಿನಂತಿಗಳನ್ನು ಮಾಡಲು ಸಹಾಯ.

## Azure OpenAI ಮಾದರಿಯನ್ನು ರಚಿಸಿ ಮತ್ತು ನಿಯೋಜಿಸಿ

ಇನ್ನೂ ಮಾಡದಿದ್ದಲ್ಲಿ, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ಪುಟದಲ್ಲಿ ನೀಡಲಾದ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ
Azure OpenAI ಸಂಪನ್ಮೂಲ ಮತ್ತು ಮಾದರಿಯನ್ನು ರಚಿಸಿ. ಮಾದರಿಯಾಗಿ **gpt-image-1** ಆಯ್ಕೆಮಾಡಿ (ಈಗಿನ ಜನರೇಶನ್ Azure OpenAI ಚಿತ್ರ ಮಾದರಿ; DALL-E 3 ಚಿರಂತನ ಇಲ್ಲ ಮತ್ತು ಹೊಸ ನಿಯೋಜನೆಗಳಿಗೆ ಲಭ್ಯವಿಲ್ಲ).

## ಅಪ್ಲಿಕೇಶನ್ ರಚನೆ

1. _.env_ ಎಂಬ ಫೈಲ್ ರಚಿಸಿ ಮತ್ತು ಈ ಕೆಳಗಿನ ವಿಷಯವನ್ನು ಸೇರಿಸಿ:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   ನಿಮ್ಮ ಸಂಪನ್ಮೂಲದ "Deployments" ವಿಭಾಗದಲ್ಲಿ ನೀವು ಈ ಮಾಹಿತಿ ಹುಡುಕಬಹುದು.

1. ಮೇಲಿನ ಲೈಬ್ರರಿಗಳನ್ನು _requirements.txt_ ಫೈಲ್‌ನಲ್ಲಿ ಸೇರಿಸಿ ಹೀಗೆ:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. ನಂತರ, ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ ಮತ್ತು ಲೈಬ್ರರಿ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   ವಿಂಡೋಸ್‌ನಲ್ಲಿ, ನಿಮ್ಮ ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ ಮತ್ತು ಸಕ್ರಿಯಗೊಳಿಸಲು ಈ ಆಜ್ಞೆಗಳನ್ನು ಬಳಸಿ:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ ಎಂಬ ಫೈಲ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # ಡೊಟ್‌ಎನ್‌ವಿ ಅನ್ನು импорт ಮಾಡಿ
    dotenv.load_dotenv()
    
    # Azure OpenAI ಸೇವಾ ಗ್ರಾಹಕರನ್ನು ಸಂರಚಿಸಿ
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # ಇಮೇಜ್‌ ಜೆನೆರೆಷನ್ API ಬಳಸಿ ಚಿತ್ರವನ್ನು ರಚಿಸಿ
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # ಸಂಗ್ರಹಿತ ಚಿತ್ರಕ್ಕಾಗಿ ತಾಣವನ್ನು ಹೊಂದಿಸಿ
        image_dir = os.path.join(os.curdir, 'images')

        # ತಾಣದಿದ್ದರೆ ಇಲ್ಲದಿದ್ದರೆ, ಅದನ್ನು ರಚಿಸಿ
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # ಚಿತ್ರ ಮಾರ್ಗವನ್ನು ಪ್ರಾರಂಭಿಸಿ (ಫೈಲ್ ಪ್ರಕಾರ ಪಿಎನ್‌ಜಿ ಆಗಿರಬೇಕೆಂಬುದು ಗಮನಿಸಿ)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # ರಚಿತ ಚಿತ್ರವನ್ನು ಪಡೆದುಕಿರಿ
        image_url = generation_response.data[0].url  # ಪ್ರತಿಕ್ರಿಯೆಯಿಂದ ಚಿತ್ರ URL ಹೊರತೆಗೆಯಿರಿ
        generated_image = requests.get(image_url).content  # ಚಿತ್ರವನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # ಡೀಫಾಲ್ಟ್ ಚಿತ್ರ ವೀಕ್ಷಕದಲ್ಲಿ ಚಿತ್ರವನ್ನು ಪ್ರದರ್ಶಿಸಿ
        image = Image.open(image_path)
        image.show()

    # исключенияಗಳನ್ನು ಹಿಡಿದುಕೊಳ್ಳಿ
    except openai.BadRequestError as err:
        print(err)
   ```

ಈ ಕೋಡ್ ಅನ್ನು ವಿವರಿಸೋಣ:

- ಮೊದಲು, ನಾವು ಅಗತ್ಯವಿರುವ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳುತ್ತೇವೆ, ಇದರಲ್ಲಿ OpenAI, dotenv, requests, ಮತ್ತು Pillow ಲೈಬ್ರರಿಗಳು ಇವೆ.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- ನಂತರ, _.env_ ಫೈಲ್‌ನಿಂದ ಪರಿಸರ ಚರಗಳನ್ನು ಲೋಡ್ ಮಾಡುತ್ತೇವೆ.

  ```python
  # ಡಾಟ್‌ಎನ್ವಿ ಆಮದುಮಾಡಿ
  dotenv.load_dotenv()
  ```

- ನಂತರ, Azure OpenAI ಸೇವಾ ಕ್ಲೈಂಟ್ ಅನ್ನು ಸಂರಚಿಸುತ್ತೇವೆ.

  ```python
  # ಪರಿಸರ ಚರಗಳಿಂದ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು ಕೀಲಿಯನ್ನು ಪಡೆಯಿರಿ
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- ನಂತರ, ಚಿತ್ರವನ್ನು ತಯಾರಿಸುತ್ತೇವೆ:

  ```python
  # ಇमೇಜ್ ಜನರೇಷನ್ API ಬಳಸಿಕೊಂಡು ಚಿತ್ರವನ್ನು ರಚಿಸಿ
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  ಮೇಲಿನ ಕೋಡ್ ಜನರೇಟು ಮಾಡಿದ ಚಿತ್ರ URL ಒಳಗೊಂಡ JSON ವಸ್ತುವಿಗೆ ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತದೆ. ಆ URL ಬಳಸಿ ಚಿತ್ರವನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ಫೈಲ್‌ಗೆ ಉಳಿಸಬಹುದು.

- ಕೊನೆಗೆ, ಚಿತ್ರವನ್ನು ತೆರೆಯಬೇಕು ಮತ್ತು ಸಾಮಾನ್ಯ ಚಿತ್ರ ವೀಕ್ಷಕವನ್ನು ಬಳಸಿ ಪ್ರದರ್ಶಿಸಬೇಕು:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ಚಿತ್ರವನ್ನು ತಯಾರಿಸುವ ಬಗ್ಗೆ ಹೆಚ್ಚಿನ ವಿವರಗಳು

ಚಿತ್ರವನ್ನು ತಯಾರಿಸುವ ಕೋಡ್‌ನ್ನು ಹೆಚ್ಚು ವಿವರವಾಗಿ ನೋಡೋಣ:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, ಚಿತ್ರದ ತಯಾರಿಕೆಗೆ ಬಳಸಿ текст ಪರಿಕಲ್ಪನೆ. ಇಲ್ಲಿ " ಪೋನಿಯಲ್ಲಿ ಭೂತದಾಟುತ್ತಿರುವ್ಕೊಳ ಹುಡುಗಿ, ಲಾಲಿಪೋಪ್ ಹಿಡಿದಂತೆ, ಹೊತ್ತಿಗೆ ಹೊತ್ತಿತ್ತಿದೆ" ಎಂಬ ಪ್ರಾಂಪ್ಟ್ ಬಳಸಲಾಗಿದೆ.
- **size**, ತಯಾರಾಗುವ ಚಿತ್ರದ ಗಾತ್ರ. ಇಲ್ಲಿ 1024x1024 ಪಿಕ್ಸೆಲ್ ಗಾತ್ರ.
- **n**, ತಯಾರಾಗುವ ಚಿತ್ರಗಳ ಸಂಖ್ಯೆ. ಇಲ್ಲಿ ಎರಡು ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸಲಾಗುತ್ತಿದೆ.
- **temperature**, ಜನರೇಟಿವ್ AI ಮಾದರಿಯ ಉತ್ಪಾದನೆಯ ಯಾದೃಚ್ಛಿಕತೆಯನ್ನು ನಿಯಂತ್ರಿಸುವ ಪರಿಕರ. 0 ರಿಂದ 1 ರವರೆಗೆ ಮೌಲ್ಯ, 0 ಅನಿವಾರ್ಯ ಮತ್ತು 1 ಯಾದೃಚ್ಛಿಕ. ಡೀಫಾಲ್ಟ್ ಮೌಲ್ಯ 0.7.

ಮುಂದಿನ ವಿಭಾಗದಲ್ಲಿ ಚಿತ್ರಗಳೊಂದಿಗೆ ಮಾಡಬಹುದಾದ ಇನ್ನಷ್ಟು ವಿಷಯಗಳನ್ನು ನಾವು ನೋಡುತ್ತೇವೆ.

## ಚಿತ್ರ ಉತ್ಪಾದನೆಯ ಹೆಚ್ಚುವರಿ ಸಾಮರ್ಥ್ಯಗಳು

Python ನಲ್ಲಿ ಕೆಲವೇ ಸಾಲುಗಳ ಮೂಲಕ ಚಿತ್ರವನ್ನು ಉತ್ಪಾದಿಸುವ ನಮಗೆ ಸಾಧ್ಯವಾಯಿತು. ಆದರೆ ಇನ್ನುತರ ಸಹ ಆಲ್ಪ ನಿಮಿಷಗಳು ಇದ್ದವೆ.

ನೀವು ಈ ಕೆಳಕಂಡವುಗಳನ್ನೂ ಮಾಡಬಹುದು:

- **ಸಂಪಾದನೆ ಮಾಡುವುದು**. ಇರುತ್ತಿದ್ದ ಚಿತ್ರದ ಮೇಲೆ ಮಾಸ್ಕ್ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್ ಒದಗಿಸಿ, ಚಿತ್ರವನ್ನು ಬದಲಾಯಿಸಬಹುದು. ಉದಾಹರಣೆಗೆ, ಬನ್ನಿಯನ್ನು ಹಾಕಿೆಎಂ ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್ ಮೂಲಕ ಸೃಷ್ಟಿಸಬಹುದು. ಬನ್ನಿಗೇ ಹ್ಯಾಟ್ ಹಾಕಿ ಬಯಸಿದರೆ ಆ ಭಾಗವನ್ನು ಗುರುತಿಸಿ, ಚಿತ್ರ ಮತ್ತು ಮಾಸ್ಕ್ ನೀಡಬೇಕು.
> ಗಮನಿಸಿ: DALL-E 3 ನಲ್ಲಿ ಇದನ್ನು ಬೆಂಬಲಿಸಲಾಗಿಲ್ಲ.
 
GPT ಚಿತ್ರ ಬಳಸಿ ಇದಕ್ಕೆ ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

 ಆಧಾರ ಚಿತ್ರದಲ್ಲಿ ಲಾಂಜ್ ಮತ್ತು ಪುಲ್ ಮಾತ್ರ ಇರುತ್ತದೆ ಆದರೆ ಅಂತಿಮ ಚಿತ್ರದಲ್ಲಿ ಫ್ಲೇಮಿಂಗೋ ಇದ್ದಂತೆ:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/kn/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/kn/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/kn/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **ವಿವಿಧತೆ ಸೃಷ್ಟಿಸಿ**. ಈಗಿರುವ ಚಿತ್ರವನ್ನು ತೆಗೆದುಕೊಂಡು, ವಿಭಿನ್ನ варианты ಸೃಷ್ಟಿಸುವಂತೆ ಕೇಳಬಹುದು. ವಿಭಿನ್ನತೆ ಮಾಡಲು, ಚಿತ್ರದೊಂದಿಗೆ ಪ್ರಾಂಪ್ಟ್ ನೀಡಿ ಮತ್ತು ಕೆಳಗಿನಂತಿರುವ ಕೋಡ್ ಬಳಸಿ:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > ಗಮನಿಸಿ, ಇದು OpenAI ನ DALL-E 2 ಮಾದರಿಯಲ್ಲಿ ಮಾತ್ರ ಬೆಂಬಲವಾಗಿದೆ, gpt-image-1 ನಲ್ಲಿ ಅಲ್ಲ.

## ತಾಪಮಾನ (Temperature)

ತಾಪಮಾನ ಜನರೇಟಿವ್ AI ಮಾದರಿಯ ಉತ್ಪಾದನೆಯ ಯಾದೃಚ್ಛಿಕತೆಯನ್ನು ನಿಯಂತ್ರಿಸುವ ಪರಿಕರ. ಮೌಲ್ಯ 0 ರಿಂದ 1, 0 ಅನಿವಾರ್ಯ ಮತ್ತು 1 ಯಾದೃಚ್ಛಿಕ. ಡೀಫಾಲ್ಟ್ 0.7.

ತಾಪಮಾನ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಎಂಬ ಉದಾಹರಣೆಗೆ, ಈ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಇಬ್ಬರಸಾರಿಗೆ ನಡೆಸಿ ನೋಡೋಣ:

> ಪ್ರಾಂಪ್ಟ್ : "ಹತ್ತು ಕುದುರೆ ಮೇಲೆ ಕುಳಿತ, ಲಾಲಿಪೋಪ್ ಹಿಡಿದಿರುವ, ಕು ಮಹಡಿಯಲ್ಲಿ ಹೂಗಳು ಬೆಳೆಯುತ್ತಿರುವ ನಾಯಿ"

![ಕುದುರೆ ಮೇಲೆ ಕುಳಿತ, ಲಾಲಿಪೋಪ್ ಹಿಡಿದಿರುವ ನಾಯಿ, ಆವೃತ್ತಿ 1](../../../translated_images/kn/v1-generated-image.a295cfcffa3c13c2.webp)

ಈಗ ಅದೇ ಪ್ರಾಂಪ್ಟ್ ಮತ್ತೆ ಓಡಿಸಿ, ಇದೇ ಚಿತ್ರ ಎರಡು ಬಾರಿ ಬರುತ್ತದೆ ಎಂದು ನೋಡೋಣ:

![ಕುದುರೆ ಮೇಲೆ ಕುಳಿತ ನಾಯಿಯ ಚಿತ್ರ](../../../translated_images/kn/v2-generated-image.33f55a3714efe61d.webp)

ಕಾಣಬಹುದಾದಂತೆ, ಚಿತ್ರಗಳು ಸಮಾನವಾಗಿವೆ ಆದರೆ ಆವೃತ್ತಿಯಲ್ಲಿವು ಬೇರೆ. ಈಗ ತಾಪಮಾನ ಮೌಲ್ಯವನ್ನು 0.1 ಗೆ ಬದಲಾಯಿಸಿ ನೋಡೋಣ:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # ಇಲ್ಲಿ ನಿಮ್ಮ ಪ್ರಾಂಪ್ಟ್ ಪಠ್ಯವನ್ನು ನಮೂದಿಸಿ
        size='1024x1024',
        n=2
    )
```

### ತಾಪಮಾನ ಬದಲಾವಣೆ

ಆದ್ದರಿಂದ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಹೆಚ್ಚು ನಿರ್ಧಾರಾತ್ಮಕವಾಗಿ ಮಾಡೋಣ. ಮೊದಲ ಚಿತ್ರದಲ್ಲಿ ಬನ್ನಿ ಇದೆ ಮತ್ತು ಎರಡನೇ ಚಿತ್ರದಲ್ಲಿ ಕುದುರೆ ಇದೆ ಎಂದು ಗಮನಿಸಿದಾಗ, ಚಿತ್ರಗಳು ಬಹಳ ವ್ಯತ್ಯಾಸವಿರುವುದು ತೋರಿಸುತ್ತದೆ.

ನಮ್ಮ ಕೋಡ್‌ನಲ್ಲಿ ತಾಪಮಾನವನ್ನು 0 ಕ್ಕೆ ಬದಲಾಯಿಸಿ, ಹೀಗಾಗಬಹುದು:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # ನಿಮ್ಮ ಪ್ರಾಂಪ್ಟ್ ಪಠ್ಯವನ್ನು ಇಲ್ಲಿ ನಮೂದಿಸಿ
        size='1024x1024',
        n=2,
        temperature=0
    )
```

ಈಗ ನೀವು ಈ ಕೋಡ್ ಓಡಿಸಿದಾಗ, ಈ ಎರಡು ಚಿತ್ರಗಳನ್ನು ಪಡೆಯುತ್ತೀರಿ:

- ![ತಾಪಮಾನ 0, ಆವೃತ್ತಿ 1](../../../translated_images/kn/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![ತಾಪಮಾನ 0 , ಆವೃತ್ತಿ 2](../../../translated_images/kn/v2-temp-generated-image.871d0c920dbfb0f1.webp)

ಇಲ್ಲಿ ಚಿತ್ರಗಳು ಸ್ಪಷ್ಟವಾಗಿ ಇನ್ನಷ್ಟು ಸಮಾನವಾಗಿವೆ ಎಂದು ಕಾಣಬಹುದು.

## ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಗಾಗಿ ಮಿತಿಗಳನ್ನು ಹೇಗೆ ನಿರ್ಧರಿಸುವುದು ಮೆಟಾ ಪ್ರಾಂಪ್ಟ್‌ಗಳ ಮೂಲಕ

ನಮ್ಮ ಡೆಮೋದಲ್ಲಿ ಈಗಾಗಲೇ ಗ್ರಾಹಕರಿಗೆ ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸಬಹುದು. ಆದರೆ, ಅಪ್ಲಿಕೇಶನ್ಗೆ ಕೆಲವು ಮಿತಿಗಳನ್ನು ರಚಿಸಬೇಕಾಗಿದೆ.

ಉದಾಹರಣೆಗೆ, ಕೆಲಸಕ್ಕೆ ಅನರ್ಹವಾದ, ಮಕ್ಕಳಿಗೆ ಸೂಕ್ತವಲ್ಲದ ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸುವುದನ್ನು ನಾವು ಬಯಸುವುದಿಲ್ಲ.

ಇದನ್ನು _ಮೆಟಾಪ್ರಾಂಪ್ಟ್_ ಗಳು ಮೂಲಕ ಮಾಡಬಹುದು. ಮೆಟಾಪ್ರಾಂಪ್ಟ್‌ಗಳು ಜನರೇಟಿವ್ AI ಮಾದರಿಯ output ನಿಯಂತ್ರಿಸುವ ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್‌ಗಳು. ಉದಾಹರಣೆಗೆ, ನಾವು ಮೆಟಾಪ್ರಾಂಪ್ಟ್ ಬಳಸಿ ಚಿತ್ರಗಳು ಕೆಲಸಕ್ಕೆ ಅನರ್ಹವಾಗದ ಅಥವಾ ಮಕ್ಕಳಿಗೆ ಸೂಕ್ತವಾಗಿರುವಂತೆ ಖಚಿತಪಡಿಸಬಹುದು.

### ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ?

ಇದೀಗ, ಮೆಟಾಪ್ರಾಂಪ್ಟ್ ಗಳ ಕಾರ್ಯಪದ್ಧತಿ?

ಮೆಟಾಪ್ರಾಂಪ್ಟ್‌ಗಳು ಜನರೇಟಿವ್ AI ಮಾದರಿಯ output ನಿಯಂತ್ರಿಸಲು text prompt ಗಳಾಗಿ, ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್ ಮುಂಚೆಯೆ ಇರಿಸಲಾಗುತ್ತದೆ, ಮತ್ತು ಈ ಪ್ರಾಂಪ್ಟ್ ಅಪ್ಲಿಕೇಶನ್ಗಳಲ್ಲಿ ಮದ್ಯವರ್ತಿಯಾಗಿ ಸೇರಿಸಿ ಮಾದರಿಯಲ್ಲಿ output ನಿಯಂತ್ರಣ ಮಾಡುತ್ತದೆ. ಪ್ರಾಂಪ್ಟ್ ಇರುವ ಸingle texte promptನಲ್ಲಿ ಪ್ರಾಂಪ್ಟ್ ಮತ್ತು ಮೆಟಾ ಪ್ರಾಂಪ್ಟ್ ಒಂದಾಗಿ ಸೇರಿರುತ್ತವೆ.

ಒಂದು ಮೆಟಾಪ್ರಾಂಪ್ಟ್ ಉದಾಹರಣೆ ಹೀಗೆ ಇರಬಹುದು:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

ಈಗ, ಡೆಮೋದಲ್ಲಿ ಮೆಟಾಪ್ರಾಂಪ್ಟ್ ಗಳನ್ನು ಹೇಗೆ ಬಳಸಬಹುದೆಂಬುದನ್ನ ನೋಡೋಣ.

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

ಮೇಲಿನ ಪ್ರಾಂಪ್ಟ್‌ಗಳಿಂದ, ನಿರ್ಮಿಸುತ್ತಿರುವ ಎಲ್ಲಾ ಚಿತ್ರಗಳು ಮೆಟಾಪ್ರಾಂಪ್ಟ್ ಪರಿಗಣಿಸುತ್ತವೆ ಎಂದು ಕಾಣಬಹುದು.

## ಕಾರ್ಯ - ವಿದ್ಯಾರ್ಥಿಗಳನ್ನು ಸಬಲೀಕರಿಸೋಣ

ಈ ಪಾಠ ಆರಂಭದಲ್ಲಿ Edu4All ಅನ್ನು ಪರಿಚಯಿಸಿದ್ದೇವೆ. ಇದೀಗ ವಿದ್ಯಾರ್ಥಿಗಳನ್ನು ತಮ್ಮ ಮೌಲ್ಯಮಾಪನಗಳಿಗಾಗಿ ಚಿತ್ರಗಳನ್ನು ತಯಾರಿಸಲು ಸಬಲೀಕರಿಸುವ ಸಮಯವಾಗಿದೆ.


ವಿದ್ಯಾರ್ಥಿಗಳು ಅವರ ಮೌಲ್ಯಮಾಪನಗಳಿಗೆ ಸ್ಮಾರಕಗಳನ್ನು ಒಳಗೊಂಡ ಚಿತ್ರಗಳನ್ನು ರಚಿಸುವರು, ಯಾವ ಸ್ಮಾರಕಗಳು ಎಂಬುದನ್ನು ವಿದ್ಯಾರ್ಥಿಗಳು ತಾವು ನಿರ್ಧರಿಸುವರು. ಈ ಕಾರ್ಯದಲ್ಲಿ ವಿದ್ಯಾರ್ಥಿಗಳ ಸೃಜನಶೀಲತೆ ಬಳಸಿ, ವಿವಿಧ ಸಂದರ್ಭಗಳಲ್ಲಿ ಈ ಸ್ಮಾರಕಗಳನ್ನು ಇರಿಸಲು ಕೇಳಲಾಗಿದೆ.

## ಪರಿಹಾರ

ಇದೊಂದು ಸಾಧ್ಯವಾದ ಪರಿಹಾರವಾಗಿದೆ:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# ಪರಿಸರ ಚರಗಳುಂದಿನಿಂದ ಅಂತಿಮ ಬಿಂದುವನ್ನು ಮತ್ತು ಕೀ ಅನ್ನು ಪಡೆಯండి
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
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
"""

try:
    # ಚಿತ್ರ ಉತ್ಪಾದನೆ API ಬಳಸಿ ಚಿತ್ರವನ್ನು ರಚಿಸಿ
    generation_response = client.images.generate(
        prompt=prompt,    # ನಿಮ್ಮ ಪ್ರಾಂಪ್ಟ್ ಪಠ್ಯವನ್ನು ಇಲ್ಲಿ ನಮೂದಿಸಿ
        size='1024x1024',
        n=1,
    )
    # ಸಂಗ್ರಹಿಸಲಾದ ಚಿತ್ರದ ಡೈರೆಕ್ಟರಿಯನ್ನು ಸೆಟ್ ಮಾಡಿ
    image_dir = os.path.join(os.curdir, 'images')

    # ಡೈರೆಕ್ಟರಿ ಇಲ್ಲದಿದ್ದರೆ, ಅದನ್ನು ರಚಿಸಿ
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # ಚಿತ್ರ ಪಥವನ್ನು ಪ್ರಾರಂಭಿಸಿ (ಕಾಯ್ದುಹಿಡಿಯಬೇಕಾದ ಫೈಲಿನ ಪ್ರಕಾರ png ಆಗಿರಬೇಕು)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # ಉತ್ಪಾದಿತ ಚಿತ್ರವನ್ನು ಪಡೆದುಕೊಳ್ಳಿ
    image_url = generation_response.data[0].url  # ಪ್ರತಿಕ್ರಿಯಿಂದ ಚಿತ್ರ URL ಅನ್ನು ಹೊರತೆಗೆಯಿರಿ
    generated_image = requests.get(image_url).content  # ಚಿತ್ರವನ್ನು ಡೌನ್ಲೋಡ್ ಮಾಡಿ
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # ಡೀಫಾಲ್ಟ್ ಚಿತ್ರ ವೀಕ್ಷಕರಲ್ಲಿ ಚಿತ್ರವನ್ನು ಪ್ರದರ್ಶಿಸಿ
    image = Image.open(image_path)
    image.show()

# ದೋಷಗಳನ್ನು ಹಿಡಿಯಿರಿ
except openai.BadRequestError as err:
    print(err)
```

## ಅತ್ಯುತ್ತಮ ಕೆಲಸ! ನಿಮ್ಮ ಕಲಿಕೆಯನ್ನು ಮುಂದುವರೆಸಿ

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನಮ್ಮ [ಜನರೇಟಿವ್ ಏಐ ಕಲಿಕಾ ಸಂಗ್ರಹವನ್ನು](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ಪರಿಶೀಲಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಜನರೇಟಿವ್ ಏಐ ಜ್ಞಾನವನ್ನು ಮುಂದುವರೆಯಿಸಿ!

ಪಾಠ 10 ಗೆ ಹೋಗಿ, ಅಲ್ಲಿ ನಾವು [ಕಡಿಮೆ-ಕೋಡ್ ಮೂಲಕ ಏಐ ಅಪლಿಕೇಶನ್ ಗಳನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸುವುದು](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) ಎಂಬುದನ್ನು ನೋಡೋಣ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->