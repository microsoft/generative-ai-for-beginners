# छवि निर्माण अनुप्रयोग बनाना

[![छवि निर्माण अनुप्रयोग बनाना](../../../translated_images/hi/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs सिर्फ़ पाठ निर्माण तक सीमित नहीं हैं। आप पाठ वर्णनों से छवियाँ भी बना सकते हैं। छवियाँ एक माध्य के रूप में चिकित्सा प्रौद्योगिकी, वास्तुकला, पर्यटन, गेम विकास, विपणन, और अन्य क्षेत्रों में उपयोगी हैं। इस पाठ में हम आज के **GPT Image** मॉडलों को देखते हैं और एक छवि निर्माण अनुप्रयोग बनाते हैं।

## परिचय

छवि निर्माण आपको प्राकृतिक भाषा प्रॉम्प्ट को एक चित्र में बदलने की अनुमति देता है। इस पाठ में हम OpenAI के **`gpt-image`** मॉडल परिवार के साथ काम करते हैं - जो Microsoft Foundry और OpenAI प्लेटफ़ॉर्म पर उपलब्ध वर्तमान पीढ़ी के छवि मॉडल हैं। ये मॉडल पुराने DALL·E मॉडल (DALL·E 2/3 विरासत हैं) की जगह लेते हैं।

पूरे पाठ में हम एक कल्पित स्टार्टअप, **Edu4All**, का उपयोग करते हैं जो सीखने के उपकरण बनाता है। टीम असाइनमेंट और अध्ययन सामग्री के लिए चित्र तैयार करना चाहती है।

## सीखने के लक्ष्य

इस पाठ के अंत तक आप सक्षम होंगे:

- यह समझाएं कि छवि निर्माण क्या है और यह कहाँ उपयोगी है।
- `gpt-image` मॉडल परिवार को समझें और यह पुराने DALL·E मॉडलों से कैसे भिन्न है।
- Python (और TypeScript / .NET) में एक छवि निर्माण अनुप्रयोग बनाएं।
- छवियों को संपादित करें और मेटाप्रॉम्प्ट्स के साथ सुरक्षा गार्डरेल लगाएं।

## छवि निर्माण क्या है?

छवि निर्माण मॉडल एक टेक्स्ट प्रॉम्प्ट से छवियाँ बनाते हैं। आधुनिक मॉडल जैसे `gpt-image` ट्रांसफॉर्मर + डिफ्यूजन तकनीकों पर आधारित हैं: मॉडल प्रशिक्षण के दौरान टेक्स्ट और छवियों के बीच संबंध सीखता है, फिर प्रॉम्प्ट मिलने पर वह यादृच्छिक शोर को चरणबद्ध तरीके से "डिनोइस" करता है ताकि वर्णन के अनुरूप छवि बने।

दो प्रसिद्ध छवि मॉडल परिवार हैं:

- **`gpt-image` (OpenAI)** - वर्तमान पीढ़ी, जिसका इस पाठ में उपयोग होता है। यह टेक्स्ट-से-छवि निर्माण और छवि संपादन (मास्क के साथ इनपेंटिंग) का समर्थन करता है।
- **Midjourney** - एक लोकप्रिय तृतीय-पक्ष मॉडल है जिसकी अपनी सेवा और Discord-आधारित वर्कफ़्लो है।

> पुराने OpenAI छवि मॉडल - **DALL·E 2** और **DALL·E 3** - विरासत हैं। DALL·E 3 नए परिनियोजन के लिए उपलब्ध नहीं है, और `create_variation` जैसी विशेषताएँ केवल DALL·E 2 में थीं। नए अनुप्रयोगों के लिए `gpt-image` मॉडल का उपयोग करें।

### मुझे कौन सा `gpt-image` मॉडल उपयोग करना चाहिए?

Microsoft Foundry पर निम्नलिखित **सामान्यत: उपलब्ध** हैं:

| मॉडल | विवरण |
| --- | --- |
| **`gpt-image-2`** | नवीनतम और सबसे सक्षम छवि मॉडल - अनुशंसित डिफ़ॉल्ट। |
| `gpt-image-1.5` | सामान्यत: उपलब्ध; कम लागत पर अच्छी गुणवत्ता। |
| `gpt-image-1-mini` | सामान्यत: उपलब्ध; सबसे तेज / सबसे कम लागत। |
| `gpt-image-1` | केवल पूर्वावलोकन। |

उपलब्धता और क्षेत्रों के लिए हमेशा वर्तमान [Foundry छवि मॉडल सूची](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) देखें।

> **महत्वपूर्ण:** `gpt-image` मॉडल उत्पन्न छवि को **base64** (`b64_json`) के रूप में लौटाते हैं, URL के रूप में नहीं। आपका कोड base64 स्ट्रिंग को बाइट्स में डीकोड करता है और सहेजता है - डाउनलोड करने के लिए कोई छवि URL नहीं होता।

## सेटअप

आप नमूनों को **Microsoft Foundry में Azure OpenAI** (`aoai-*` नमूने) या **OpenAI प्लेटफ़ॉर्म** (`oai-*` नमूने) के विरुद्ध चला सकते हैं।

### 1. एक मॉडल बनाएं और तैनात करें

Microsoft Foundry संसाधन बनाने के लिए [create a resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) गाइड का पालन करें, फिर एक छवि मॉडल तैनात करें - **`gpt-image-2`** अनुशंसित है।

### 2. अपना `.env` कॉन्फ़िगर करें

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

ये मान आपके संसाधन के [Foundry पोर्टल](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) के **Deployments** पेज पर मिलेंगे।

### 3. लाइब्रेरीज़ स्थापित करें

`requirements.txt` बनाएं:

```text
python-dotenv
openai
pillow
```

फिर एक वर्चुअल एनवायरनमेंट बनाएं और सक्रिय करें तथा निम्न स्थापित करें:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## एप्लिकेशन बनाएं

निम्न कोड के साथ `app.py` बनाएं। यह एक छवि उत्पन्न करता है और उसे PNG के रूप में सहेजता है।

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# क्लाइंट को आपके Azure OpenAI (Microsoft Foundry) संसाधन की ओर निर्देशित करें।
# छवि मॉडल को हाल की API संस्करण की आवश्यकता होती है - अपने मॉडल के लिए आवश्यक संस्करण के लिए Foundry दस्तावेज़ देखें।
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # उदा. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # इसके अलावा 1536x1024 (लैंडस्केप), 1024x1536 (पोर्ट्रेट), या "ऑटो"
    n=1,
)

# gpt-image मॉडल बेस64 (b64_json) लौटाते हैं, URL नहीं - इसे बाइट्स में डिकोड करें।
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

इसे `python app.py` से चलाएं। `images/` में एक PNG सहेजा जाएगा।

> `images.generate` को हर कॉल में एक ही प्रॉम्प्ट के लिए अलग छवि मिलती है - छवि मॉडल में `temperature` पैरामीटर नहीं होता (यह टेक्स्ट निर्माण नियंत्रण है)। विविधता पाने के लिए API को फिर से कॉल करें; विविधता कम करने के लिए अपने प्रॉम्प्ट को अधिक विशिष्ट बनाएं।

## छवि संपादन

`gpt-image` मॉडल एक मौजूदा छवि को **संपादित** कर सकते हैं: छवि, वैकल्पिक **मास्क** (जो बदलाव क्षेत्र को चिह्नित करता है), और बदलाव का वर्णन करने वाला प्रॉम्प्ट दें। निर्माण की तरह, संपादन भी base64 में लौटते हैं।

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/hi/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/hi/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/hi/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## मेटाप्रॉम्प्ट्स के साथ सीमाएँ निर्धारित करना

एक बार जब आप छवियाँ बना सकते हैं, तो आपको गार्डरेल की जरूरत होती है ताकि आपका ऐप असुरक्षित या ऑफ-ब्रांड सामग्री न उत्पन्न करे। एक **मेटाप्रॉम्प्ट** वह पाठ है जिसे आप उपयोगकर्ता के प्रॉम्प्ट से पहले जोड़ते हैं ताकि मॉडल के आउटपुट को सीमित किया जा सके।

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# `prompt` को client.images.generate(...) में पास करें
```

प्रत्येक छवि अब मेटाप्रॉम्प्ट द्वारा निर्धारित सीमाओं के भीतर उत्पन्न होती है। इसे Microsoft Foundry में अंतर्निहित सामग्री फिल्टरों के साथ मिलाएं ताकि सुरक्षा को गहरा किया जा सके।

## असाइनमेंट - छात्रों के लिए सक्षम बनाएं

Edu4All के छात्रों को उनके आकलनों के लिए छवियों की जरूरत है। एक ऐसा ऐप बनाएं जो **स्मारकों** की छवियाँ उत्पन्न करे (कौन से स्मारक आप तय करें) विभिन्न और रचनात्मक संदर्भों में - उदाहरण के लिए, सूर्यास्त पर एक प्रसिद्ध स्थलाकृति और एक बच्चा उसे देख रहा हो।

स्वयं प्रयास करें, फिर संदर्भ समाधानों से तुलना करें:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) पूर्ण निर्माण ऐप: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

साथ ही [python/](../../../09-building-image-applications/python) में नोटबुक का उपयोग करें (`aoai-assignment.ipynb` Azure के लिए, `oai-assignment.ipynb` OpenAI के लिए)।

## शानदार काम! अपनी सीख जारी रखें

इस पाठ को पूरा करने के बाद, हमारे [Generative AI Learning संग्रह](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) को देखें ताकि आप अपने जनरेटिव AI ज्ञान को और बढ़ा सकें!

आगे के सीखने के लिए पाठ 10 पर जाएँ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->