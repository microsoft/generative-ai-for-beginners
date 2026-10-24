# உரை உருவாக்கும் செயலிகளை கட்டமைத்தல்

[![உரை உருவாக்கும் செயலிகளை கட்டமைத்தல்](../../../translated_images/ta/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(இந்த பாடத்தின் வீடியோவைப் பார்க்க மேலுள்ள படத்தை கிளிக் செய்யவும்)_

இதுவரை இந்த பாடத்திட்டம் மூலம் நீங்கள் கண்டுபிடித்துள்ளீர்கள் பிரதானக் கருத்துக்கள் என்றால் முன்மொழிவுகள் மற்றும் "prompt engineering" என்கிற ஒரு முழு துறை. ChatGPT, Office 365, Microsoft Power Platform போன்ற பல கருவிகள், ஏதையாவது போர்த்துமுடிவை அடைய உதவ முன்மொழிவுகளை பயன்படுத்த ஆதரவு வழங்குகின்றன.

உங்களுக்கு ஒரு செயலியில் இப்படிப்பட்ட அனுபவத்தைச் சேர்க்க, முன்மொழிவு, நிறைவு போன்ற கருத்துக்களை புரிந்து கொண்டு செயல்பட தேவையான நூலகத்தை தேர்ந்தெடுக்க வேண்டும். இதுவே இந்த அதிகாரத்தில் நீங்கள் கற்க இருப்பது.

## அறிமுகம்

இந்த அதிகாரத்தில் நீங்கள்:

- openai நூலகம் மற்றும் அதன் அடிப்படை கருத்துக்களை கற்கப்போகிறீர்கள்.
- openai ကို பயன்படுத்தி ஒரு உரை உருவாக்கும் செயலியை கட்டமைக்கப்போகிறீர்கள்.
- முன்மொழிவு, வெப்பநிலை மற்றும் டோக்கன்கள் போன்ற கருத்துக்களை எப்படி பயன்படுத்தி உரை உருவாக்கும் செயலி கட்டமைக்கலாம் என்பதைக் கற்றுக்கொள்வீர்கள்.

## கற்கும் இலக்குகள்

இந்த பாடம் முடிந்தவுடன், நீங்கள்:

- ஒரு உரை உருவாக்கும் செயலி என்ன என்பதை விளக்க முடியும்.
- openai பயன்படுத்தி உரை உருவாக்கும் செயலியை கட்டமைக்க முடியும்.
- உங்கள் செயலியில் அதிகம் அல்லது குறைவாக டோக்கன்களை மற்றும் வெப்பநிலையை மாற்றுவதன் மூலம் பல்வகை விளைவுகளை உருவாக்க முடியும்.

## உரை உருவாக்கும் செயலி என்றால் என்ன?

பொதுவாக, ஒரு செயலி கட்டும்போது அதன் கீழ்க்காணும் வகை இடைமுகம் ஒன்று இருக்கும்:

- கட்டளை அடிப்படையிலானது. கமாண்டு நுழைத்து அதை செயல்படுத்தும் Console செயலிகள் பொதுவாக இருக்கின்றன. உதாரணமாக, `git` என்பது கட்டளை அடிப்படையிலான செயலி.
- பயனர் இடைமுகம் (UI). சில செயலிகளில் கிளிக் செய்யும் பொத்தான்கள், உரை உள்ளீடு, விருப்பத் தேர்வு போன்ற கொண்டிருப்புகள் உள்ளன.

### Console மற்றும் UI செயலிகள் வரம்புடையவை

ஒரு கட்டளை அடிப்படையிலான செயலியுடன் அதனை ஒப்பிடுக:

- **வரம்புடையது**. நீங்கள் எந்த கட்டளையையும் தட்டச்சு செய்ய முடியாது, செயலி ஆதரிக்கும் கட்டளைகளிடமே வரம்பு.
- **மொழி சார்ந்தது**. சில செயலிகள் பல மொழிகளை ஆதரிக்கின்றன, ஆனால் இயல்பாக ஒரு குறிப்பிட்ட மொழிக்கு மட்டுமே இயங்கும்.

### உரை உருவாக்கும் செயலிகளின் நன்மைகள்

எப்படி உரை உருவாக்கும் செயலி வேறுபடுகிறது?

உரை உருவாக்கும் செயலியில், நீங்கள் அதிக சக்தி வாய்ந்ததாக செயல்படுகிறீர்கள், கட்டளை தொகுப்போ அல்லது ஒரு விசேஷ மொழி நிரந்தரமாக கட்டுப்படுத்துவது இல்லை. நீங்கள் இயற்கை மொழியை பயன்படுத்தி செயலியுடன் தொடர்பு கொள்ள முடியும். மேலும், பழமையான செயலியில் தரவுத்தளத்தில் உள்ளதுதான் வரம்பு, ஆனால் இந்த செயலி கோபுரமான தகவல் தொகுப்பில் பயிற்சி பெற்ற தரவுகளை இயக்குகிறது.

### எனது உரை உருவாக்கும் செயலியுடன் என்ன உருவாக்கலாம்?

பலவிதமான செயலிகளை உருவாக்க முடியும். உதாரணமாக:

- **சாட்பாட்**. உங்கள் நிறுவனம் மற்றும் அதன் தயாரிப்புகள் பற்றி கேள்விகள் பதிலளிக்கும் சாட்பாட் நல்ல பொருத்தமாக இருக்கும்.
- **உதவி தானியங்கி**. LLM-க்கள் உரை சுருக்கம், கருத்துக் கண்டறிதல், ரெஸுமே போன்ற உரைகளை உருவாக்கும் செயல்களில் சிறந்தவை.
- **கோடு உதவியாளர்**. நீங்கள் பயன்படுத்தும் முறைமொழி நூலைப் பொறுத்து, கோடு எழுத உதவும் உதவியாளரை உருவாக்கலாம். உதாரணமாக, GitHub Copilot போன்ற தயாரிப்புகள் மற்றும் ChatGPT மற்றும் கோடு எழுத உதவுகின்றன.

## எப்படி துவங்குவது?

பொதுவாக, LLM உடன் ஒருங்கிணைக்க கட்டளைகள் இரண்டு வழி முறைகள் உள்ளன:

- API ஒன்றைப் பயன்படுத்துக. இதில் நீங்கள் நுழைவு முன்மொழிவை கொண்டு இணைய கோரிக்கையை உருவாக்கி உருவான உரையை பெறுவீர்கள்.
- நூலகத்தை பயன்படுத்துக. நூலகங்கள் API அழைப்புகளை ஒழுங்குபடுத்தி அனுக அன்ரியேல் செய்கின்றன.

## நூலகங்கள்/SDKகள்

LLMகளுடன் பணியாற்றும் பிரசித்தி பெற்ற சில நூலகங்கள் உள்ளன:

- **openai**, இந்த நூலகம் உங்கள் மாடலை இணைத்து முன்மொழிவுகளை அனுப்ப எளிதாக்குகிறது.

மேல்நிலை நூலகங்களும் உள்ளன:

- **Langchain**. Langchain பிரசித்தி பெற்ற நூலகம் மற்றும் Python ஐ ஆதரிக்கிறது.
- **Semantic Kernel**. Semantic Kernel என்பது Microsoft உருவாக்கிய நூலகம், இது C#, Python, மற்றும் Java மொழிகளை ஆதரிக்கிறது.

## openai பயன்படுத்தி முதல் செயலி

முதலில் நாம் எவ்வாறு செயலி கட்டுகிறோம், தேவையான நூலகங்கள் என்ன என்பதைக் காண்போம்.

### openai ஐ நிறுவுக

OpenAI அல்லது Azure OpenAI உடன் தொடர்பு கொள்ள பல நூலகங்கள் உள்ளன. C#, Python, JavaScript, Java உள்ளிட்ட பல மொழிகளையும் பயன்படுத்தலாம். இங்கே, நாம் `openai` என்ற Python நூலகத்தை தேர்வு செய்து `pip` மூலம் நிறுவப்போகிறோம்.

```bash
pip install openai
```

### ஒரு வளத்தை உருவாக்குக

நீங்கள் பின்வரும் படிகள் செய்ய வேண்டும்:

- Azure இல் கணக்கு ஒன்றை உருவாக்குக [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)].
- Azure OpenAIயில் அணுகல் பெறுக. [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst)] சென்று அணுகலுக்கு விண்ணப்பிக்கவும்.

  > [!NOTE]
  > எழுதும் காலத்திலிருந்து, Azure OpenAIக்கு அணுகலுக்கு விண்ணப்பிக்க வேண்டும்.

- Python ஐ நிறுவுக <https://www.python.org/>
- Azure OpenAI சேவை வளத்தை உருவாக்கியிருக்க வேண்டும். இதைப் பற்றி இந்த வழிகாட்டியைப் பார்க்கவும் [வளம் உருவாக்க](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API விசையும் இடைவெளியையும் காண்க

இப்போது, உங்கள் `openai` நூலகத்திற்கு எந்த API விசை பயன்படுத்துவது என்று சொல்ல வேண்டும். உங்கள் API விசை தெரிந்துகொள்ள, Azure OpenAI வளத்தின் "Keys and Endpoint" பிரிவிற்கு சென்று "Key 1" என்ற மதிப்பை நகலெடுக்கவும்.

![Azure போர்டலில் Keys and Endpoint வளம்](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

இப்போது இந்த தகவலை நகலெடுக்கும்படியே நாம் நூலகங்களுக்கு பயன்படுத்தச் சொல்கிறோம்.

> [!NOTE]
> உங்கள் API விசையை உங்கள் கோடிலிருந்து பிரித்து வைக்க வேண்டும். இதற்கு சூழல் மாறிலிகள் பயன்படுத்தலாம்.
>
> - சூழல் மாறி `OPENAI_API_KEY` உங்கள் API விசைக்காக அமைக்கவும்.
>   `export OPENAI_API_KEY='sk-...'`

### Azure அமைப்பை அமைக்கவும்

நீங்கள் Azure OpenAI (இப்போது Microsoft Foundry உட்பட்டது) பயன்படுத்தினால், எப்படி அமைக்கலாம் என்பதைக் காண்போம். நாங்கள் `OpenAI` வாடிக்கையாளரை Azure OpenAI `/openai/v1/` இடைவெளிக்குக் குறிப்பிடும் முறையில் பயன்படுத்துகிறோம், இது Responses API உடன் வேலை செய்யும் மற்றும் `api_version` தேவையில்லை:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

மேற்கொண்டிருக்கும் அமைப்பில்:

- `api_key`, இது Azure போர்டல் அல்லது Microsoft Foundry போர்டலில் காணப்படும் உங்கள் API விசை.
- `base_url`, இது உங்கள் Foundry வள இடைவெளி அதனுடன் `/openai/v1/` இணைக்கப்பட்டுள்ளது. வினைக்குட்பட்ட v1 இடைவெளி OpenAI மற்றும் Azure OpenAI உடன் `api_version` மேலாண்மையின்றி வேலை செய்யும்.

> [!NOTE] > `os.environ` சூழல் மாறிலிகளை வாசிக்கிறது. நீங்கள் `AZURE_OPENAI_API_KEY` மற்றும் `AZURE_OPENAI_ENDPOINT` போன்றவை வாசிக்கக்கூடியது. உங்கள் டெர்மினலில் இவற்றை அமைக்கலாம் அல்லது `dotenv` போன்ற நூலகத்தைப் பயன்படுத்தலாம்.

## உரை உருவாக்குதல்

உரையை உருவாக்கும் வழி, Responses API-ஐ `responses.create` முறை மூலம் பயன்படுத்துவது. உதாரணமாக:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

மேலுள்ளக் கோடில், ஒரு பதில் உருவாக்கி பயன்படுத்த வேண்டிய மாடல் மற்றும் முன்மொழிவை கொடுக்கின்றோம். பின்னர் `response.output_text` மூலம் உருவாக்கப்பட்ட உரையை அச்சிடுகின்றோம்.

### பல சுற்று உரையாடல்கள்

Responses API ஒரே சுற்று உரை உருவாக்கவும் பல சுற்று உரையாடல் சாட்பாடுகளுக்கும் ஏற்றது - நீங்கள் உரையாடல் உருவாக்க `input` உள்ள பட்டியலை வழங்குவீர்கள்:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

இதன் மேலான செயல்பாட்டை அடுத்த அதிகாரத்தில் காண்போம்.

## பயிற்சி - உங்கள் முதல் உரை உருவாக்கும் செயலி

இப்போது நாம் openai கையாண்டு அமைக்கும் முறையை கற்றுள்ளோம், உங்கள் முதல் உரை உருவாக்கும் செயலியை கட்டியெடுக்க நேரம். இதற்கான படிகள்:

1. ஒரு மெய்நிகர் சூழலை உருவாக்கி openai ஐ நிறுவுக:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows பயன்படுத்தினால் `venv\Scripts\activate` என்றதை பயன்படுத்தவும், `source venv/bin/activate` அல்ல.

   > [!NOTE]
   > Azure OpenAI விசையை [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) செல்க மற்றும் `Open AI` தேடவும், `Open AI resource` தேர்வு செய்து பின்னர் `Keys and Endpoint` சென்று `Key 1` மதிப்பை நகலெடுக்கவும்.

1. _app.py_ என்ற கோப்பை உருவாக்கி அதில் பின்வரும் கோடை இடுக:

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
   > நேரடி OpenAI பயன்படுத்தினால் (Azure அல்லை), `client = OpenAI(api_key="<replace this value with your OpenAI key>")` பயன்படுத்தவும் ( `base_url` இல்லை) மற்றும் deployment பெயருக்கு பதிலாக `gpt-5-mini` போன்ற மாடல் பெயரை கொடுக்கவும்.

   நீங்கள் பின்வரும் விளைவைக் காண்பீர்கள்:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## பலவித முன்மொழிவுகள், பலவித பயன்கள்

இப்போது நீங்கள் முன்மொழிவை பயன்படுத்தி உரையை உருவாக்கும் முறையை பார்த்துள்ளீர்கள். நீங்கள் உருவாக்கி இயக்கும் ஒரு செயலி கொண்டிருக்கிறீர்கள், இதனை மாற்றி வெவ்வேறு வகையான உரைகள் உருவாக்கலாம்.

முன்மொழிவுகள் எல்லா பணிகளுக்கும் பயன்படலாம். உதாரணமாக:

- **ஒரு வகையான உரையை உருவாக்குக**. உதாரணமாக, கவிதை, வினா தொகுப்பு போன்றவை உருவாக்கலாம்.
- **தகவல் தேடுக**. முன்மொழிவுகளைப் பயன்படுத்தி 'என்பா வலை அபிவிருத்தியில் CORS என்றால் என்ன?' போன்ற தகவலைத் தேட முடியும்.
- **கோடு உருவாக்குக**. மின்னஞ்சல் சரிபார்க்கும் தனிச்சொற்கள் (regular expressions) எழுதுதல், அல்லது முழு இணைய செயலி போன்ற கோடுகளை உருவாக்க முடியும்.

## ஒரு நடைமுறை பயன்பாடு: சமையல் செயல் உருவாக்கி

உங்கள் வீட்டில் உள்ள பொருட்கள் கொண்டு நீங்கள் ஏதாவது சமையல் செய்ய விரும்பினால், சமையலுக்கான செயலை தேவைப்படும். இது தேடுபொறியை பயன்படுத்தி அல்லது LLM இணைத்து செய்யலாம்.

நீங்கள் கீழ் போன்று ஒரு முன்மொழிவை எழுதலாம்:

> "கீழ்க்கண்ட பொருட்களுடன் செய்யக்கூடிய 5 சமையல் செயல் காட்டவும்: கோழி, உருளைக்கிழங்கு மற்றும் காரட். ஒவ்வொரு செயலுக்கும் பதிலாக பயன்படுத்தப்பட்ட பொருட்களை பட்டியலிடவும்"

மேலே கூறிய முன்மொழிவு வழியாக, பெறக்கூடிய பதில்:

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

இது நல்ல முடிவாக உள்ளது, என்ன சமையல் செய்வதென்று தெரிகிறது. இவ்விலையில், பேசலாக மாற்றங்கள் வேண்டியவை:

- நான் விரும்பாத அல்லது அலெர்ஜி உள்ள பொருட்களை அகற்றுதல்.
- இல்லையென்றால் இல்லாத பொருட்களை வாங்குவதற்கான பட்டியலை உருவாக்குவது.

மேலே பணிக்க, கூடுதல் முன்மொழிவை சேர்ப்போம்:

> "சேர்க்கவேண்டாத பொருளாக பூண்டு சேர்க்கப்பட்ட சமையல் செயல் நீக்கவும், நான் அதற்கு அலெர்ஜி. மாற்றாக வேறு ஏதாவது சேர்க்கவும். மேலும, நான் வீட்டில் கோழி, உருளைக்கிழங்கு மற்றும் காரட் இருக்கின்றன என்பதை கருத்தில் கொண்டு வாங்கும் பட்டியலை உருவாக்கவும்."

இப்போது நீங்கள் புதிய முடிவை பெற்றுள்ளீர்கள்:

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

உங்கள் ஐந்து சமையல் செயல் பூண்டு இல்லாமல் உருவாக்கப்பட்டு, வீட்டில் இருப்பதை கருத்தில் கொண்டு வாங்கும் பட்டியலும் உள்ளது.

## பயிற்சி - சமையல் செயல் உருவாக்கி உருவாக்குக

இதுவரை செயல்பட்ட நிலையை விளக்கியுள்ளோம், அதற்கான குறியீட்டை எழுதுவோம். அதற்கான படிகள்:

1. தற்போதைய _app.py_ கோப்பை தொடக்கமாக பயன்படுத்துக
1. `prompt` மாறியை தேடி அந்தக் கோடியை கீழ்க்கண்டவாறு மாற்றுக:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   இப்போது நீங்கள் இந்த கோடியை இயக்கினால் பின்வரும் விளைவைக் காண்பீர்கள்:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > கவனிக்கவும், உங்கள் LLM தானாக மாறுபடும், செயலியை ஒவ்வொரு முறையும் இயக்கும் போது வேறுபட்ட முடிவுகள் வரும்.

   அருமை, இப்போது எப்படி மேம்படுத்தலாம் என்று பார்ப்போம். மேம்படுத்த, கோடு நெகிழ்வாக இருக்க வேண்டும், பொருட்கள் மற்றும் சமையல் செயல் எண்ணிக்கை மாற்றத்தக்கதாக.

1. கோட்டை கீழ்க்கண்டபடி மாற்றுவோம்:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   இதையாவது சோதனைக்காக ஓட்டினால்:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### வடிகட்டி மற்றும் வாங்கும் பட்டியலைச் சேர்த்து மேம்படுத்து

இப்போது நாம் ஒரு செயலியை கொண்டிருக்கிறோம், இது recipes உருவாக்குகிறது மற்றும் பயனர் உள்ளீட்டுக்கு அமைவாக எண்ணிக்கையும் பொருட்களையும் மாற்றக்கூடியது.

இதை மேலும் மேம்படுத்த, பின்வருவனச் சேர்க்க வேண்டும்:

- **பொருட்களை வடிகட்டி அகற்று**. விரும்பாத அல்லது அலெர்ஜி உள்ள பொருட்களை வடிகட்டி அகற்ற விரும்புகிறோம். இதற்கு, நாம் முன்மொழிவை மாற்றி கீழ்க்காணும் விளக்கத்தைச் சேர்க்கலாம்:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  மேலே, நாம் முன்மொழிவின் இறுதியில் `{filter}` சேர்க்கிறோம் மற்றும் பயனர் கொடுத்த வடிகட்டு மதிப்பையும் எடுத்துக்கொள்கின்றோம்.

  இப்போது செயலை இயக்கும் ஒரு உதாரண உள்ளீடு:

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

  நீங்கள் பார்க்கும் போல, பால் கொண்ட recipes அகற்றப்பட்டுள்ளன. ஆனால் வெண்ணெய் பதிக்குள் ஒவ்வொருவரும் விருப்பமான பாடுமாறு, சிலர் சீஸுக்கு அலெர்ஜி உள்ளார்கள், அதுவும் வடிகட்டப்படவேண்டும் என்பதற்கு தெளிவுசெய்ய வேண்டும்.

- **வாங்கும் பட்டியலை உருவாக்குக**. வீட்டில் உள்ளதை கருத்தில் கொண்டு வாங்க வேண்டிய பொருட்கள் பட்டியலை உருவாக்கவேண்டும்.

  இது ஒன்றே முன்மொழிவில் செய்ய முடியாததனால், இரண்டு முன்மொழிவாக பிரித்து செய்கிறோம். புதிய முன்மொழிவிற்கு முதல் முன்மொழிவின் முடிவை கருத்தாக்கமாகச் சேர்க்க வேண்டும்.

  முதன்மை முன்மொழிவின் முடிவை அச்சிடும் பகுதிக்கு கீழ்க்கண்ட கோடுகளை சேர்க்குக:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  கவனிக்கவேண்டியது:

  1. புதிய முன்மொழிவைப் புது முறையில் முதல் முன்மொழிவின் முடிவுடன் சேர்க்கின்றோம்:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. புதிய கோரிக்கையை செய்கிறோம், ஆனால் முதல் முறையிலே கேட்ட டோக்கன்கள் எண்ணிக்கையை கருத்தில் கொண்டு, இப்போதும் `max_output_tokens` ஐ 1200 என்கிறோம்.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     இந்தக் கோடியை இயக்கி பின்வரும் விளைவிற்கு வருகிறோம்:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## உங்கள் அமைப்பைக் கையாளவும்

இதுவரை நமக்கு உள்ளதாகும் பணி செயல்படும் குறியீடு தான், ஆனால் இன்னும் மேம்படுத்த சில மாற்றங்கள் செய்ய வேண்டும். செய்ய வேண்டிய சில விஷயங்கள்:

- **எண்ணாக்களைக் குறியிடப்பட்ட கோடுகளிலிருந்து பிரிக்கவும்**, API திறவுகோல் போன்றவை. ரகசியங்கள் குறியீடுகளில் சேர்க்கக்கூடாது மற்றும் அவற்றை பாதுகாப்பான இடத்தில் சேமிக்க வேண்டும். ரகசியங்களை குறியீடுகளில் இருந்து பிரிக்க, நாங்கள் சூழல் மாறிலிகளை மற்றும் `python-dotenv` போன்ற நூலகங்களை கோப்பிலிருந்து ஏற்ற பயன்படுத்தலாம். குறியீடில் அது இப்படி காணப்படும்:

  1. கீழே குறிப்பிட்ட உள்ளடக்கம் கொண்ட `.env` கோப்பை உருவாக்கவும்:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > குறிப்பு, Microsoft Foundry இல் Azure OpenAIக்காக, கீழ்க்காணும் சூழல் மாறிலிகளை அமைக்க வேண்டும்:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     குறியீட்டில், சூழல் மாறிலிகளை மேலும் இவ்வாறு ஏற்றுகொள்ளலாம்:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **டோக்கன்கள் நீளத்தைக் குறித்து ஒரு வார்த்தை**. உங்களால் தேவையான உரையை உருவாக்க எத்தனை டோக்கன்கள் தேவை என்பதை நாம் கவனிக்க வேண்டும். டோக்கன்கள் பணம் செலவாகும், ஆகவே, இயலுமானால், பயன்படுத்தும் டோக்கன்களின் எண்ணிக்கையில் மிதமாக இருக்க உதவ வேண்டும். உதாரணமாக, குறுந்தொகுப்பு வரைபடத்தை குறைத்து டோக்கன்கள் குறைவாக பயன்படுத்த இயலும்தாக அமைக்க முடியுமா என்று பாருங்கள்.

  டோக்கன்களின் எண்ணிக்கையை மாற்ற, நீங்கள் `max_output_tokens` என்ற அளவுருவைப் பயன்படுத்தலாம். உதாரணமாக, 100 டோக்கன்கள் பயன்படுத்த வேண்டும் என்றால், நீங்கள் இதுபோல செய்வீர்கள்:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **வெயிலுருவான மாற்றங்களை முயற்சித்தல்**. வெயிலுரு என்பது இன்றுவரை குறிப்பிடப்படவில்லை, ஆனால் நமது செயலிக்கு முக்கியமான சூழல். வெயிலுரு மதிப்பு அதிகமானால் வெளியீடு அதிக அளவிலான சீரற்றமாக இருக்கும். குறைந்த வெயிலுரு மதிப்பு அதிகமாக எதிர்பார்க்கக்கூடிய முறையில் இருக்கும். உங்கள் வெளிப்பாட்டில் மாற்றம் வேண்டும் எனில் கவனியுங்கள்.

  வெயிலுருவை மாற்ற, நீங்கள் `temperature` என்ற அளவுருவைப் பயன்படுத்தலாம். உதாரணமாக, 0.5 வெயிலுரு விரும்பினால், இப்போல் செய்யுங்கள்:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > குறிப்பு, 1.0 இற்கு அருகிலிருப்பது வேறுபாடுகளை அதிகரிக்கும்.

- **காரணம்செய்யும் மாதிரிகள் `temperature` ஐ பயன்படுத்துவதில்லை**. இது ஒரு முக்கியமான 2026 மாற்றம். Microsoft Foundry இல் தற்போதைய, ஆவணப்படுத்தப்படாத மாதிரிகள் **காரணம்செய்யும் மாதிரிகள்** (GPT-5 குடும்பம், o-சீர்கள்) - மற்றும் அவை **`temperature` அல்லது `top_p` ஐ ஆதரிக்காது** (மேலும் `max_tokens`; பயன்பாட்டுக்கு `max_output_tokens` ஐப் பயன்படுத்தவும்). நீங்கள் `temperature` ஐ `gpt-5-mini` க்கு அனுப்பினால் "parameter not supported" பிழை வரும். எனவே, வெயிலுரு எடுத்துக்காட்டை முயற்சிக்க, மாதிரிSampling மதிப்புகளை ஆதரிக்கும் மாதிரியைப் பயன்படுத்துங்கள் - உதாரணமாக திறந்த **Llama** மாதிரி `Llama-3.3-70B-Instruct` இல் இருந்து [Microsoft Foundry மாதிரி தொகுப்பு](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), Foundry Models / Azure AI Inference இடைமுகத்துடன் அழைக்கப்படுகிறது (அதேவிதமாக `githubmodels-*` எடுத்துக் காட்டுகள்). GPT-5 போன்ற காரணம்செய்யும் மாதிரிகளுக்குப் பிறகு வெளிப்பாட்டை மாற்றுவது வேறுபாடாகும்:
  - **குறுந்தொகுப்பு பொறியியலாளர்ச்சி** - தெளிவான வழிகாட்டல்கள், எடுத்துக்காட்டுகள், மற்றும் கட்டமைக்கப்பட்ட வெளிப்பாடு (காட்சி [04 - குறுந்தொகுப்பு பொறியியலாளர்ச்சி](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) என்பது முன்பு மாதிரிகள் பயன்படுத்திய கட்டுப்பாடுகளை மாற்றுகிறது.
  - **காரணப்படுத்தும் கட்டுப்பாடுகள்** - காரண முயற்சி / விரிவாக்கம் போன்ற அளவுருக்கள் காரண ஆழத்தையும் தாமதத்தையும் மற்றும் செலவையும் சமன்செய்கிறது.

  சுருக்கமாக: `temperature`/`top_p` பல மாதிரிகளில் (Llama, Mistral, Phi மற்றும் GPT-4.x குடும்பம் - GPT-4.x குறைவடைகிறது) இன்னும் செல்லுபடியாகும், ஆனால் பயணம் திசை குறுந்தொகுப்பு பொறியியலாளர்ச்சி + காரணப்படுத்தும் கட்டுப்பாடுகளில் (GPT-5 போன்ற காரணம்செய்யும் மாதிரிகளில்) ஆகிறது.

## பணியொற்று

இந்த பணியில் நீங்கள் என்ன உருவாக்க வேண்டும் என்று தேர்ந்தெடுக்கலாம்.

சில பரிந்துரைகள்:

- செய்முறையாளர் ஆப்பை மேலும் மேம்படுத்த மாற்றங்கள் செய்து பாருங்கள். வெயிலுரு மதிப்புகளுடன் மற்றும் குறுந்தொகுப்புகளுடன் விளையாடி பாருங்கள்.
- ஒரு "பயிற்சி துணை" உருவாக்குங்கள். இந்த ஆப் ஒரு பாடத்தினை பற்றி கேள்விகளுக்கு பதிலளிக்கக்கூடியதாக இருக்க வேண்டும். உதாரணமாக Python பற்றி, நீங்கள் "Python இல் ஒரு குறிப்பிட்ட பாடம் என்ன?" அல்லது "ஒரு குறிப்பிட்ட பாடத்திற்கான குறியீடு காட்டு" போன்ற குறுந்தொகுப்புகள் வைத்திருக்கலாம்.
- வரலாறு பாஸ், வரலாற்றை உயிரோட்டமாக்குங்கள், பாஸை ஒரு வரலாற்றுப் பாத்திரம் ஆக நடிக்க சொல்லி, அதன் வாழ்க்கை மற்றும் காலங்களை பற்றி கேட்குங்கள்.

## தீர்வு

### பயிற்சி துணை

கீழே ஒரு துவக்க குறுந்தொகுப்பு உள்ளது, அதை எப்படி பயன்படுத்தி நீங்கள் விரும்பியபடி மாற்றலாம் என்பதைப் பாருங்கள்.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### வரலாறு பாஸ்

இங்கே நீங்கள் பயன்படுத்தக்கூடிய சில குறுந்தொகுப்புகள் உள்ளன:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## அறிவு சோதனை

வெயிலுரு என்ன செய்கிறது?

1. வெளியீடு எவ்வளவு சீரற்றமாக இருக்கும் என்பதை கட்டுப்படுத்துகிறது.
1. பதில் எவ்வளவு பெரியதாக இருக்கும் என்பதை கட்டுப்படுத்துகிறது.
1. எத்தனை டோக்கன்கள் பயன்படுத்தப்பட வேண்டும் என்பதைக் கட்டுப்படுத்துகிறது.

## 🚀 சவால்

பணியில் பணியாற்றும் பொழுது வெயிலுருவை மாறவைத்து பார்த்து, அதைக் 0, 0.5 மற்றும் 1 என அமைத்துப் பாருங்கள். 0 குறைவான வேறுபாடானதும் 1 அதிகமானவேறுபாடானதும் ஆகும். உங்களுடைய ஆப்புக்கு எது சிறந்த மதிப்பாகும்?

## அருமையாக செய்தீர்கள்! உங்கள் கற்றலை தொடருங்கள்

இந்த பாடத்தைக் முடித்த பிறகு, எங்கள் [உருவாக்கும் AI கற்றல் தொகுப்பு](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)வைக் பாருங்கள், உங்கள் உருவாக்கும் AI அறிவை மேலும் உயர்த்த!

பாடம் 7க்குத் திரும்பி, எவ்வாறு [செய்தி அனுப்பும் பயன்பாடுகளை உருவாக்குவது](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) என்பதைப் பார்ப்போம்!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->