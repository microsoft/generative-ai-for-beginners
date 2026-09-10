# உரை உருவாக்கும் பயன்பாடுகளை உருவாக்குதல்

[![உரை உருவாக்கும் பயன்பாடுகளை உருவாக்குதல்](../../../translated_images/ta/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(இந்த பாடத்தின் வீடியோவை பார்ப்பதற்கு மேல் உள்ள படம்பைப்பை கிளிக் செய்க)_

இவ்வரிசையில் இதுவரை, உங்களுக்கு புரிந்து கொண்டிருப்பது போல், பூச்சிகள் போன்ற அடிப்படைக் கருத்துகள் உள்ளன, மற்றும் முழு ஒரு துறை "பூச்சி பொறியியல்" என்றே உள்ளது. ChatGPT, Office 365, Microsoft Power Platform மற்றும் பலவும் போன்ற பல கருவிகள், நீங்கள் எதையாவது செய்ய பூச்சிகளைப் பயன்படுத்த மகிழப்படுகின்றன.

ஒரு பயன்பாட்டுக்கு இத்தகைய அனுபவத்தைச் சேர்க்க, பூச்சிகள், முடிவுகள் போன்ற கருத்துக்களைப் புரிந்து கொண்டு, தேவையான நூலகத்தைத் தேர்ந்தெடுக்க வேண்டும். இதேதான் நீங்கள் இந்த அத்தியாயத்தில் கற்றுக்கொள்ளப்போகும் விஷயம்.

## அறிமுகம்

இந்த அத்தியாயத்தில், நீங்கள்:

- openai நூலகம் மற்றும் அதன் அடிப்படைக் கருத்துக்களை கற்றுக்கொள்ளுங்கள்.
- openai பயன்படுத்தி உரை உருவாக்கும் பயன்பாட்டை உருவாக்குங்கள்.
- பூச்சி, வெப்பநிலை, மற்றும் டோக்கன்கள் போன்ற கருத்துக்களை பயன்படுத்தி உரை உருவாக்கும் பயன்பாட்டை உருவாக்குவது எப்படி என்பதைக் அறிக.

## கற்றல் இலக்குகள்

இந்த பாடத்தின் முடிவில், நீங்கள்:

- ஒரு உரை உருவாக்கும் பயன்பாடு என்றால் என்ன என்பதை விளக்குங்கள்.
- openai பயன்படுத்தி உரை உருவாக்கும் பயன்பாட்டை உருவாக்குங்கள்.
- உங்கள் பயன்பாட்டை, அதிகமோ குறைவோ டோக்கன்களைப் பயன்படுத்துவதற்கு மற்றும் வெப்பநிலையை மாற்றுவதற்கு உள்ளமைக்கலாம், பலவகையான வெளிப்பாட்டுக்கு.

## உரை உருவாக்கும் பயன்பாடு என்றால் என்ன?

சாதாரணமாக, நீங்கள் ஒரு பயன்பாட்டை உருவாக்கும் போது அதற்கு பின்வரும் மாதிரியில் ஒரு இடைமுகம் இருக்கும்:

- கட்டளை அடிப்படையிலானது. கன்சோல் பயன்பாடுகள் என்பது நீங்கள் ஒரு கட்டளையை type செய்து அவை ஒரு செயல்பாட்டை செய்கிறன. உதாரணமாக, `git` என்பது கட்டளை அடிப்படையிலான பயன்பாடு.
- பயனர் இடைமுகம் (UI). சில பயன்பாடுகளுக்கு கிராபிகல் பயனர் இடைமுகங்கள் (GUIs) உண்டு, அவையில் நீங்கள் பொத்தான்களை சொடுக்க, உரையை உள்ளிட, விருப்பங்களை தேர்வு செய்யலாம்.

### கன்சோல் மற்றும் UI பயன்பாடுகள் வரம்புள்ளன

கட்டளை அடிப்படையிலான பயன்பாட்டைப் பார், நீங்கள் கட்டளையை type செய்யும் போது:

- **அது வரம்புப் பெற்றது**. நீங்கள் எந்த கட்டளையையும் எழுத முடியாது, பயன்பாடு ஆதரிக்கின்ற கட்டளையே மட்டும்.
- **மொழி சார்ந்தது**. சில பயன்பாடுகள் பல மொழிகளை ஆதரிக்கின்றன, ஆனால் இயல்பாக அந்த பயன்பாடு ஒரு குறிப்பிட்ட மொழிக்காக உருவாக்கப்பட்டுள்ளது, கூடுதலான மொழி ஆதரவை நீங்கள் சேர்க்கலாம்.

### உரை உருவாக்கும் பயன்பாடுகளின் நன்மைகள்

எனவே, உரை உருவாக்கும் பயன்பாடு எப்படி வேறுபடுகிறது?

உரை உருவாக்கும் பயன்பாட்டில், நீங்கள் அதிக சித்திரவதைகள் பெறலாம், கட்டளைகள் அல்லது குறிப்பிட்ட உள்ளீட்டு மொழிக்கு வரம்பாகவில்லை. பதிலுக்கு, நீங்கள் இயற்கை மொழியைப் பயன்படுத்தி பயன்பாட்டுடன் தொடர்பு கொள்ளலாம். மற்றொரு நன்மை, நீங்கள் ஏற்கனவே ஒரு பெரிய தகவல் நூலகத்தில் பயிற்சியளிக்கப்பட்ட தரவுத்தளத்துடன் தொடர்பு கொள்கிறீர்கள், அதே சமயம் பாரம்பரிய பயன்பாடு தரவுத்தளத்தில் உள்ளதையே மட்டுமே கொண்டிருக்கலாம்.

### நான் உரை உருவாக்கும் பயன்பாட்டுடன் என்ன செய்யலாம்?

நீங்கள் பலவகையானவற்றை உருவாக்கலாம். உதாரணம்:

- **ஒரு விமர்சனப்பாகம்**. ஒரு விமர்சனப்பாகம் உங்கள் நிறுவனம் மற்றும் அதன் தயாரிப்புகள் பற்றிய கேள்விகளுக்கு பதிலளிக்கலாம்.
- **உதவியாளர்**. LLMகள் உரையை சுருக்குதல், உரையிலிருந்து கருத்துக்களை பெறுதல், சராசரி மற்றும் பிற உரைகளை உருவாக்குதல் போன்றவற்றுக்கு சிறந்தவை.
- **குறியீடு உதவியாளர்**. நீங்கள் பயன்படுத்தும் மொழி முறைமையின் அடிப்படையில், நீங்கள் குறியீடு எழுத உதவும் குறியீடு உதவியாளரை உருவாக்கலாம். உதாரணமாக, GitHub Copilot போன்ற தயாரிப்போடு அல்லது ChatGPT உடன் குறியீடு எழுத உதவலாம்.

## எப்படி ஆரம்பிக்கலாம்?

உண்மையில், நீங்கள் LLM உடன் ஒருங்கிணைப்பது எப்படி என்பதை காண வேண்டும், பொதுவாக இரண்டு முறைகள் உள்ளன:

- API பயன்படுத்துக. இங்கே நீங்கள் உங்கள் பூச்சியுடன் வலை வேண்டுதல்களை கட்டமைத்து உருவாக்கப்பட்ட உரையை பெற்றுக்கொள்ளலாம்.
- நூலகம் பயன்படுத்துக. நூலகங்கள் API அழைப்புகளை இணைத்து அதை பயன்படுத்த எளிதாக்குகின்றன.

## நூலகங்கள்/SDKகள்

LLMக்களுடன் பணியாற்ற சில பரிச்சயமான நூலகங்கள் உள்ளன:

- **openai**, இந்த நூலகம் உங்கள் மாதிரியுடன் இணைந்து பூச்சிகளை அனுப்ப எளிதாக்குகிறது.

பிறகு மேல்நிலைப் பொருத்தமான நூலகங்கள் உள்ளன:

- **Langchain**. Langchain பிரபலம் மற்றும் Python ஐ ஆதரிக்கிறது.
- **Semantic Kernel**. Semantic Kernel என்பது Microsoft ஆல் உருவாக்கப்பட்ட நூலகம், அது C#, Python மற்றும் Java மொழிகளுக்கு ஆதரவளிக்கிறது.

## openai பயன்படுத்தி முதல் பயன்பாடு

நமது முதல் பயன்பாட்டை உருவாக்குவது எப்படி, எத்தனை நூலகங்கள் தேவை, பிற விவரங்கள் பார்க்கலாம்.

### openai ஐ நிறுவுக

OpenAI அல்லது Azure OpenAI உடன் தொடர்பு கொள்ள பல நூலகங்கள் உள்ளன. C#, Python, JavaScript, Java மற்றும் பல போன்ற பல மொழிகளில் பயன்படுத்தலாம். நாங்கள் `openai` Python நூலகத்தை தேர்ந்தெடுத்து `pip` மூலம் அதை நிறுவுவோம்.

```bash
pip install openai
```

### ஒரு வளத்தை உருவாக்குக

நீங்கள் பின்வரும் படிகள் செய்ய வேண்டும்:

- Azure இல் கணக்கு ஒன்றை உருவாக்குக [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI க்கு அணுகல் பெறுக. [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) செல்லுங்கள் மற்றும் அணுகலை கோருங்கள்.

  > [!NOTE]
  > எழுதும் சமயத்தில், Azure OpenAI க்கான அணுகலுக்கு விண்ணப்பிக்க வேண்டும்.

- Python ஐ நிறுவுக <https://www.python.org/>
- Azure OpenAI சேவை வளத்தை உருவாக்கி முடிந்திருப்பது. [வளம் உருவாக்குதல்](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) வழிகாட்டியை பார்.

### API விசை மற்றும் இசை இடத்தைக் கண்டறியுக

இப்போது, `openai` நூலகத்திற்கு எந்த API விசையைப் பயன்படுத்த வேண்டும் என கூற வேண்டும். உங்கள் API விசையை கண்டறிய, Azure OpenAI வளத்தின் "விசைகள் மற்றும் இசை இடம்" பகுதியில் சென்று "Key 1" மதிப்பை நகலெடுக்கவும்.

![Azure Portal இல் விசைகள் மற்றும் இசை இட வள பேலட்](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

இப்போது இதை நகலெடுத்துவிட்டீர்கள், நூலகங்களை இதைப் பயன்படுத்தச் சொல்லுவோம்.

> [!NOTE]
> உங்கள் API விசையை உங்கள் குறியீட்டிலிருந்து பிரிக்க வேண்டும். அதற்காக சுற்றுச்சூழல் மாறிலிகள் (environment variables) பயன்படுத்தலாம்.
>
> - `OPENAI_API_KEY` என்ற சுற்றுச்சூழல் மாறி உங்கள் API விசைக்கு அமைக்கவும்.
>   `export OPENAI_API_KEY='sk-...'`

### Azure அமைப்பு செட் செய்யுக

நீங்கள் Azure OpenAI (Microsoft Foundry இல் தற்போது) பயன்படுத்தினால், அமைப்பு செய்வது இங்கே. நாங்கள் `OpenAI` கிளையண்ட் பயன்படுத்துகிறோம் அது Azure OpenAI `/openai/v1/` இசை இடத்துக்கு சென்று Responses API உடன் வேலை செய்கிறது, `api_version` தேவையில்லை:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

மேலே நாம் பின்வருவன அமைக்கின்றோம்:

- `api_key`, இது உங்கள் API விசை Azure Portal அல்லது Microsoft Foundry போர்டலில் கிடைக்கிறது.
- `base_url`, இது உங்கள் Foundry வள இசை இடம் `/openai/v1/` appended உடன். நிலையான v1 endpoint OpenAI மற்றும் Azure OpenAI இரண்டிற்கும் வேலை செய்கிறது `api_version` இல்லாமல்.

> [!NOTE] > `os.environ` சுற்றுச்சூழல் மாறிலிகளை வாசிக்கிறது. இது `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` போன்ற சுற்றுச்சூழல் மாறிலிகளை வாசிக்க பயன்படுத்தலாம். அவற்றை உங்கள் டெர்மினல் அல்லது `dotenv` போன்ற நூலகம் மூலம் அமைக்கலாம்.

## உரை உருவாக்குக

உரை உருவாக்கும் வழி Responses API உடன் `responses.create` முறைமையை பயன்படுத்துதல். உதாரணம் கீழே:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # இது உங்கள் மாடல் விநியோகத்தின் பெயர்
    input=prompt,
    store=False,
)
print(response.output_text)
```

மேலேயுள்ள குறியீட்டில், நாம் ஒரு பதிலை உருவாக்கி உருவாக்க வேண்டிய மாதிரியும் பூச்சியையும் கொடுக்கின்றோம். பின்னர் `response.output_text` மூலமாக உருவாக்கப்பட்ட உரையை அச்சிடுகின்றோம்.

### பல முறை உரையாடல்கள்

Responses API ஒற்றை முறை உரை உருவாக்கும் மற்றும் பல முறை உரையாடல் விமர்சனப்பாகத்திற்கும் பொருந்தும் - நீங்கள் உரையாடலை கட்டமைக்க `input` இல் செய்தி பட்டியலை வழங்கலாம்:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

இந்த செயல்பாட்டின் மேலதிகம் வரும் அத்தியாயத்தில் பார்க்கலாம்.

## பயிற்சி - உங்கள் முதல் உரை உருவாக்கும் பயன்பாடு

இப்போது openai எவ்வாறு அமைக்க மற்றும் காரியநிறைவு செய்வது என்று கற்றுக்கொண்டோம், உங்கள் முதற் உரை உருவாக்கும் பயன்பாட்டை உருவாக்க நேரம்.

1. ஒரு மெய்நிகர் சூழலை உருவாக்கி openai நிறுவுக:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows பயன்படுத்தினால் `source venv/bin/activate` அல்லாமல் `venv\Scripts\activate` என்று type செய்யவும்.

   > [!NOTE]
   > உங்கள் Azure OpenAI விசையை கண்டறிய [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) சென்று `Open AI` தேடவும், `Open AI resource` தேர்ந்தெடுக்கவும், பின்னர் `Keys and Endpoint` கிளிக் செய்து `Key 1` மதிப்பை நகலெடுக்கவும்.

1. _app.py_ என்ற கோப்பினை உருவாக்கி பின்வரும் குறியீட்டை இடவும்:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # உங்கள் நிரல் குறியீட்டைக் கூட்டுக
   prompt = "Complete the following: Once upon a time there was a"

   # பதில்கள் API கொண்டு கோரிக்கையைச் செய்க
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # பதிலை அச்சிடுக
   print(response.output_text)
   ```

   > [!NOTE]
   > நீங்கள் சாதாரண OpenAI (Azure அல்ல) பயன்படுத்தினால், `client = OpenAI(api_key="<replace this value with your OpenAI key>")` இத்துடன் (base_url தேவையில்லை) deployment பெயர் பதிலாக மாதிரி பெயரைச் சேர்க்கவும், உதா. `gpt-5-mini`.

   கீழே போன்ற ஒரு வெளிப்பாடு பெறுவீர்கள்:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## வெவ்வேறு வகையான பூச்சிகள், வெவ்வேறு காரியங்களுக்காக

இப்போது நீங்கள் ஒரு பூச்சி மூலம் உரை உருவாக்குவது எப்படி என்பதைக் கண்டீர்கள். நீங்கள் மாற்றி பல வகையான உரைகளை உருவாக்கும் ஒரு நிரல் இயங்கச் செய்வதையும் கற்றுக்கொண்டீர்கள்.

பூச்சிகள் பலவகை காரியங்களுக்குப் பயன்படுத்தப்படலாம். உதாரணமாக:

- **ஒரு வகை உரையை உருவாக்குக**. உதா., கவிதை, ஒரு வினாடி வினா கேள்விகள் போன்றவை.
- **தகவல்களைத் தேடுக**. 'இணைய மேம்பாட்டில் CORS என்பதன் அர்த்தம் என்ன?' போன்ற தகவல்களைத் தேட பூச்சிகளைப் பயன்படுத்தலாம்.
- **குறியீடு உருவாக்குக**. மின்னஞ்சல்களை சரிபார்க்க ரெகுலர் எக்ஸ்பிரெஷன் போன்ற குறியீட்டை உருவாக்க பூச்சிகளைப் பயன்படுத்தலாம், அல்லது முழு ஒரு வெப் பயன்பாட்டைப் போல ஒரு நிரலை உருவாக்கலாம்.

## உண்மையான பயன்படுத்தும் நிலை: ஒரு உணவு செய்முறை உருவாக்கி

உங்கள் வீட்டில் பொருட்கள் உள்ளன என நினைத்துக் கொள்ளுங்கள், நீங்கள் ஒன்றுக்குப் பசியுள்ளீர்கள். அதற்குத் தேவையானது உணவு செய்முறை. அதனைத் தேட سرچியல் என்ஜின் அல்லது LLM பயன்படுத்தலாம்.

நீங்கள் ஒரு பூச்சி எழுதலாம்:

> "கோழி, உருளைக்கிழங்கு, மற்றும் காரட் கொண்டு ஒரு உணவுக்கான 5 செய்முறைகளை காண்பி. ஒவ்வொரு செய்முறைக்கும் அது உபயோகித்த அனைத்து பொருட்களையும் பட்டியலிடு"

மேலே உள்ள பூச்சிக்கான பதில் இதுபோல் இருக்கும்:

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

இந்த முடிவு சிறந்தது, என்ன சமைக்கலாம் என தெரிந்து கொண்டேன். இப்போது, பயனுள்ள மேம்பாடுகள் என்னவாக இருக்கலாம் என்பவை:

- நான் விரும்பாத அல்லது என்னை பாதிப்பவையாக இருக்கும் பொருட்களை வடிகட்டி நீக்குதல்.
- இல்லில் அல்லாத பொருட்களுக்கான கடை பொருட்கள் பட்டியலை உருவாக்குதல்.

மேலே கேள்விகளுக்காக கூடுதல் பூச்சியைச் சேர்ப்போம்:

> "எனக்கு வறட்சியானதால் பூண்டு உள்ள செய்முறைகளை நீக்கவும், அதையும் மற்றொரு பொருளால் மாற்றவும். மேலும், கடையில் வாங்க வேண்டிய பொருட்கள் பட்டியலையும் உருவாக்கவும், நான் ஏற்கனவே கோழி, உருளைக்கிழங்கு மற்றும் காரட் உள்ளேன்."

இப்போது புதிய முடிவு கிடைத்தது, அதாவது:

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

இவை உங்கள் ஐந்து செய்முறைகள், பூண்டு ஒன்று கூட இல்லை, உங்கள் வீட்டில் உள்ளவற்றை கருத்தில் கொண்டு கடை பொருட்கள் பட்டியலும் உண்டு.

## பயிற்சி - செய்முறை உருவாக்கி

இப்போது நாம் ஒரு நிலையை விளையாடியுள்ளோம், அதை பொருத்தும் குறியீட்டை எழுதுவோம். அதற்காக, பின்வரும் படிகள்:

1. தற்போதுள்ள _app.py_ கோப்பை ஆரம்பப் புள்ளியாக பயன்படுத்துக
1. `prompt` மாறியை கண்டறிந்து அதன் குறியீட்டை பின்வருமாறு மாற்றுக:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   இப்போது குறியீட்டை இயக்கினால், பின்வருமாறு வெளிப்பாடு இருக்கும்:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > குறிப்பு, உங்கள் LLM முடிவுத் திருட்டானது, அதனால் ஒவ்வொரு முறையும் இயக்கும் போது வெவ்வேறு முடிவுகள் வரும்.

   சிறந்தது, மேம்படுத்துவது எப்படி என்பதைப் பார்த்துக்கொள்வோம். மேம்படுத்த, குறியீட்டை சிரமமற்றதாக மாற்றி, பொருட்கள் மற்றும் செய்முறை எண்ணிக்கை மாற்றக்கூடியதாக செய்ய வேண்டும்.

1. குறியீட்டை பின்வருமாறு மாற்றுவோம்:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # செய்முறை மற்றும் உட்பொருள்களில் எண்ணிக்கையை இடைமாற்றுக
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ஒரு சோதனை இயக்கம் இவ்வாறு இருக்கும்:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### வடிகட்டும் மற்றும் கடை பட்டியலைச் சேர்க்க மேம்படுத்தல்

இப்போது நாம் செய்முறைகளை உருவாக்கும் ஒரு செயல்பாட்டைக் கொண்டுள்ளோம், அது பயனரின் உள்ளீடுகளின் அடிப்படையில் சுருக்கத்தையும் எண்ணிக்கையையும் மாற்றுவதாக இருக்கிறது.

மேலும் மேம்படுத்த, பின்வருவன சேர்க்க வேண்டும்:

- **பொருட்களை வடிகட்டி நீக்கு**. நாம் விரும்பாத அல்லது ஒவ்வாமை உள்ள பொருட்களை வடிகட்ட முடியும். இதற்கான மாற்றம், நமது உள்ளீட்டு பூச்சியோடு வாக்கியம் இறுதியில் `{filter}` சேர்க்கும்.

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  மேல், பூச்சியின் இறுதியில் `{filter}` சேர்க்கப்பட்டு, பயனரிடம் இருந்து வடிகட்டி மதிப்பும் பெறப்படுகிறது.

  இதோ ஒரு எடுத்துக்காட்டு இயக்கநிலை இப்படி இருக்கும்:

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

  நீங்கள் பார்க்கும் போல், பால் உள்ள எந்த செய்முறையும் நீக்கப்பட்டுள்ளது. ஆனால், நீங்கள் லேக்டோஸ் ஒவ்வாமை உள்ளவராக இருந்தால், பண்ணீர் பொருத்தியுள்ள செயல்முறைகளையும் நீக்க விரும்பலாம், அதனால் தெளிவாக இருக்க வேண்டும்.


- **ஒரு கடை பட்டியலை தயாரிக்கவும்**. வீட்டில் ஏற்கனவே உள்ளவற்றைப் பொருண்மையாக்கி, நாம் ஒரு கடை பட்டியலை தயாரிக்க வேண்டும்.

  இந்த செயல்திறக்கத்துக்காக, நாம் எல்லாவற்றையும் ஒரே ஒரு கேள்வியில் தீர்க்க முயற்சிக்கலாம் அல்லது அதை இரண்டு கேள்விகளாக பிரிக்கலாம். இரண்டாவது முறையை முயற்சிப்போம். இங்கே நாம்கூடுதல் ஒரு கேள்வியை சேர்க்க பரிந்துரைக்கிறோம், ஆனால் அது செயல்பட, முந்தைய கேள்வியிலிருந்து பெறப்பட்ட முடிவை அடுத்த கேள்விக்கான ஒத்திசைவு (context) ஆக சேர்க்க வேண்டும்.

  முதலில் கேள்வியிலிருந்து பெறப்பட்ட முடிவை அச்சிடும் பகுதியைக் கண்டறிந்து, அதற்குக் கீழே பின்வரும் குறியீட்டை சேர்க்கவும்:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # பதிலை அச்சிடு
  print("Shopping list:")
  print(response.output_text)
  ```

  பின்வருமாறு கவனிக்கவும்:

  1. முதல் கேள்வியின் முடிவை புதிய கேள்வியின் ஓர் பகுதியாக சேர்த்து புதிய கேள்வி உருவாக்கப்படுகிறோம்:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. நாம் புதிய கோரிக்கையை உருவாக்குகிறோம், இருந்தாலும் முதலில் கேள்வியில் கேட்ட டோக்கன்களின் எண்ணிக்கையையும் கருத்தில் கொண்டு, இதற்கு `max_output_tokens` 1200 என அமைக்கிறோம்.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     இந்த குறியீட்டை இயக்கி பார்க்கும்போது, பின்னர் கீழ்காணும் வெளியீடு கிடைக்கிறது:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## உங்கள் அமைப்பை மேம்படுத்துக

இப்போது எங்களிடம் வேலை செய்யும் சரியான குறியீடு உள்ளது, ஆனால் இன்னும் சில சீர்திருத்தங்களை செய்ய வேண்டும். நாம் செய்யவேண்டிய சில விஷயங்கள்:

- **நிரலிலிருந்து இரகசியங்களை பிரிக்கவும்**, உதாரணத்திற்கு API விசை போன்றவை. இரகசியங்கள் நிரலில் இருக்காமல் பாதுகாப்பான இடத்தில் சேமிக்கப்பட வேண்டும். இரகசியங்களை நிரலிலிருந்து பிரிக்க, நாம் சுற்றுப்புற மாறிலிகள் மற்றும் `python-dotenv` போன்ற நூலகங்களை பயன்படுத்தி அதை கோப்பிலிருந்து ஏற்றலாம். இதோ அது குறியீட்டில் எப்படி இருக்கும்:

  1. பின்வரும் உள்ளடக்கத்துடன் `.env` கோப்பை உருவாக்கவும்:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > கவனம், Microsoft Foundryயின் Azure OpenAIக்காக, இதற்கு பதிலாக பின்வரும் சுற்றுப்புற மாறிலிகளை அமைக்க வேண்டும்:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     குறியீட்டில், சுற்றுப்புற மாறிலிகளை பின்வருமாறு ஏற்றுவீர்கள்:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **டோக்கன் நீளம் குறித்து ஒரு வார்த்தை**. நாம் உருவாக்க வேண்டிய உரைக்காக எத்தனை டோக்கன்கள் தேவை என்பதைக் கருத்தில் கொள்ள வேண்டும். டோக்கன்கள் செலவு ஆகும், ஆகவே தேவையான அளவு டோக்கன்களை மட்டுமே பயன்படுத்த நாம் முயற்சிக்க வேண்டும். உதாரணமாக, டோக்கன் எண்ணிக்கையை குறைக்க கேள்வியை எப்படி அமைத்துக்கொள்ளலாம் என்பதை பார்க்கலாம்?

  டோக்கன்களின் எண்ணிக்கையை மாற்ற `max_output_tokens` என்ற அளவுருவைப் பயன்படுத்தலாம். உதாரணமாக, 100 டோக்கன் பயன்படுத்த வேண்டும் என்றால், நீங்கள் பின்வருமாறு செய்ய வேண்டும்:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **வெப்பநிலை (temperature) அம்சத்தை தேர்வு செய்தல்**. இப்போது வரை நாம் வெப்பநிலை பற்றி குறிப்பிடவில்லை, ஆனால் அது எவ்வாறு செயல்படும் என்பதில் முக்கிய பங்கு வகிக்கிறது. வெப்பநிலையின் மதிப்பும் அதிகமாக இருந்தால், வெளியீடு மிக அதிகம் சீரற்றதாக இருக்கும். குறைவான ஒரு மதிப்பில், வெளியீடு மிகவும் ஒன்றிருப்பானதாக இருக்கும். உங்கள் வெளியீட்டில் மாறுபாடு வேண்டுமா என்பதைக் கவனியுங்கள்.

  வெப்பநிலையை மாற்ற `temperature` என்ற அளவுருவைப் பயன்படுத்தலாம். உதாரணமாக, 0.5 என்ற வெப்பநிலையை பயன்படுத்த வேண்டும் என்றால்:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > கவனம், 1.0க்கு அருகில் உள்ளது என்பது திறம்பட மாறுபடும் வெளியீடு என்று அர்த்தம்.

- **தர்க்கம் செய்யும் (reasoning) மாதிரிகள் `temperature`-ஐ பயன்படுத்தாது**. இது 2026ஆம் ஆண்டு ஏற்பட்ட முக்கிய மாற்றம் ஆகும். Microsoft Foundryயின் தற்போதைய, பழுதுபார்க்கப்படாத மாதிரிகள் **தர்க்கம் செய்யும் மாதிரிகள்** (GPT-5 குடும்பம், o-series) - அவை `temperature` அல்லது `top_p`-ஐ ஆதரிக்காது (மேலும் `max_tokens` இல்லாமல், `max_output_tokens`-ஐ பயன்படுத்தவும்). `temperature`-ஐ `gpt-5-mini`-க்கு அனுப்பினால் "parameter not supported" என்ற பிழை வரும். அதனால் வெப்பநிலை உதாரணத்தை முயற்சிக்க, மாதிரிகளுள் இன்னும் மாதிரிமான கட்டுப்பாடுகளை ஆதரிக்கும் மாதிரியை பயன்படுத்துங்கள் - உதாரணமாக, [Microsoft Foundry மாதிரி பட்டியலில்](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) உள்ள திறந்த **Llama** மாதிரி `Llama-3.3-70B-Instruct` -ஐ பயன்படுத்தவும், இது Foundry Models / Azure AI Inference நுழைவாயிலால் அழைக்கப்படுகிறது (`githubmodels-*` மாதிரிகள் போலவே). GPT-5 போன்ற தர்க்கம் மாதிரிகளில் வெளியீட்டை வேறுபட செய்கிறீர்கள்:
  - **கேள்வி வடிவமைப்பு** - தெளிவான வழிமுறைகள், எடுத்துக்காட்டுகள் மற்றும் கட்டமைக்கப்பட்ட வெளியீடு (பாடம் [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) பார்க்கவும்) மாதிரிகளின் பயிற்சி சாளரங்களை மாற்றியது போல் செய்கிறது.
  - **தர்க்க கட்டுப்பாடுகள்** - reasoning effort/verbosity போன்ற அளவுருக்கள் வரையறுக்கப்பட்ட நேரம் மற்றும் செலவை மாற்றி தர்க்கத்தின் ஆழத்துடன் வர்த்தகம் செய்கிறது.

  சுருக்கமாக சொல்லும் போது: `temperature`/`top_p` இப்போது பல மாதிரியிலும் செல்லுபடியாகும் (Llama, Mistral, Phi மற்றும் GPT-4.x குடும்பம் - GPT-4.x தற்போது செயலிழக்கிறது), ஆனால் பயண திசை GPT-5 போன்ற reasoning models-க்கு prompt engineering + reasoning controls ஆகும்.

## பணியிடம்

இதற்கான பணியில், நீங்கள் என்ன உருவாக்க விரும்புகிறீர்கள் என்பதைக் தேர்வு செய்யலாம்.

சில பரிந்துரைகள்:

- உணவு ரெசிபி உருவாக்கும் செயலியை மேலும் மேம்படுத்த முயற்சி செய்யவும். வெப்பநிலைக் மதிப்புகளை மாற்றி, கேள்விகளை சாடிக்காட்டுங்கள், என்ன உருவாக்க முடியும் என்று பாருங்கள்.
- ஒரு "படிப்பு தோழன்" உருவாக்கவும். இது ஒரு விஷயத்தை பற்றி, எடுத்துக்காட்டாக Python பற்றி, கேள்விகளுக்கு பதிலளிக்க முடியும். "Pythonஇல் ஒரு குறிப்பிட்ட தலைப்பு என்ன?" போன்ற கேள்விகள் அல்லது வேறு தலைப்புகளுக்கான குறியீட்டை காட்டும் கேள்விகள் இருக்கலாம்.
- வரலாறு பட்டு, வரலாற்றை உயிரோட்டம் செலுத்துங்கள், குறிப்பிட்ட வரலாற்று கதாப்பாத்திரமாக செயல்பட்டு அதன் வாழ்க்கை மற்றும் காலங்களைப் பற்றி கேள்விகள் கேளுங்கள்.

## தீர்வு

### படிப்பு தோழன்

கீழே ஒரு ஆரம்பக் கேள்வி உள்ளது, அதை எவ்வாறு பயன்படுத்தி உங்கள் விருப்பத்திற்கு ஏற்ப மாற்றலாம் என்று பாருங்கள்.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### வரலாறு பட்டு

நீங்கள் பயன்படுத்தக்கூடிய சில கேள்விகள் இவை:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## அறிவு சோதனை

வெப்பநிலை என்ற கருத்து என்ன செய்கிறது?

1. வெளியீடு எவ்வளவு சீரற்றது என்பதை கட்டுப்படுத்துகிறது.
1. பதில் அளவு எவ்வளவு என்பது கட்டுப்படுத்துகிறது.
1. எத்தனை டோக்கன்கள் பயன்படுத்தப்படுகின்றன என்பதை கட்டுப்படுத்துகிறது.

## 🚀 சவால்

பணியின்போது, வெப்பநிலையை மாற்றி பார்க்கவும், 0, 0.5 மற்றும் 1 என அமைக்கவும். 0 என்பது குறைவான தன்மையை வழங்கி, 1 மிகவும் மாறுபடும் என்பதை நினைவில் வையுங்கள். உங்கள் செயலிக்கு எந்த மதிப்பு சிறந்தது?

## சிறந்த வேலை! உங்கள் கற்றலை தொடருங்கள்

இந்த பாடத்திற்குப் பிறகு, நமது [Generative AI பாடசாலை தொகுப்பை](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) பாருங்கள், உங்கள் Generative AI அறிவை மேலும் மேம்படுத்த!

பாடம் 7க்கு செல்லவும், அங்கே நாம் [சேட்டை செயலிகள் உருவாக்குவது எப்படி](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) என்பதைக் காணப்போகிறோம்!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->