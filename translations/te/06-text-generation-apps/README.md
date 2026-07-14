# టెక్స్ట్ జనరేషన్ అనువర్తనాలు నిర్మించడం

[![టెక్స్ట్ జనరేషన్ అనువర్తనాలు నిర్మించడం](../../../translated_images/te/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ఈ పాఠం వీడియోను చూడడానికి పై చిత్రం క్లిక్ చేయండి)_

మీరు ఇప్పటి వరకు ఈ పాఠ్యক্রমం ద్వారా చూసినట్లుగా, ప్రాంప్ట్స్ లాంటి మూలభూత భావనలు మరియు "ప్రాంప్ట్ ఇంజనీరింగ్" అని పిలవబడే ఒక పూర్తి శాస్త్రం కూడా ఉంది. మీరు ఇంటరాక్ట్ అయ్యే అనేక టూల్స్, ఉదాహరణకు ChatGPT, Office 365, Microsoft Power Platform మరియు మరిన్ని, మీరు ఏదైనా సాధించడానికి ప్రాంప్ట్స్ వాడటానికి మద్దతు ఇస్తాయి.

మీరు ఒక అనువర్తనంలో ఈ అనుభవాన్ని జోడించాలంటే, ప్రాంప్ట్స్, కంప్లీషన్స్ వంటి భావనలను అర్థం చేసుకోవాలి మరియు పని చేసుకునేందుకు ఒక లైబ్రరీను ఎంచుకోవాలి. ఇదే ఈ అధ్యాయంలో మీరు నేర్చుకునేది.

## పరిచయం

ఈ అధ్యాయంలో, మీరు:

- openai లైబ్రరీ మరియు దాని మూల భావనలు గురించి నేర్చుకుంటారు.
- openai వాడి టెక్స్ట్ జనరేషన్ అనువర్తనం నిర్మిస్తారు.
- ప్రాంప్ట్, టెంపరేచర్, టోకెన్లు వంటి భావనలను టెక్స్ట్ జనరేషన్ అనువర్తనం నిర్మించే విధంగా ఎలా ఉపయోగించాలో అర్థం చేసుకుంటారు.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం చివరికి, మీరు చేయగలుగుతారు:

- టెక్స్ట్ జనరేషన్ అనువర్తనం అంటే ఏమిటో వివరించండి.
- openai ఉపయోగించి టెక్స్ట్ జనరేషన్ అనువర్తనం నిర్మించండి.
- మీ అనువర్తనంలో ఎక్కువ లేదా తక్కువ టోకెన్లు వాడటానికి, మరియు టెంపరేచర్ మార్చటానికి సర్దుబాటు చేయండి, ఫలితాన్ని విభిన్నంగా చేయండి.

## టెక్స్ట్ జనరేషన్ అనువర్తనం అంటే ఏమిటి?

సాధారణంగా మీరు అనువర్తనం నిర్మించినప్పుడు, దానికి క్రింది విధమైన ఇన్టర్‌ఫేస్ ఉంటాయి:

- క‌మాండ్-ఆధారిత. కన్సోల్ అనువర్తనాలు సాధారణంగా క‌మాండ్ టైప్ చేసి టాస్క్ చేయించే అనువర్తనాలు. ఉదాహరణకు, `git` ఒక క‌మాండ్-ఆధారిత అనువర్తనం.
- ఉపయోగకర్త ఇంటర్‌ఫేస్ (UI). కొన్ని అనువర్తనాలు గ్రాఫికల్ యూజర్ ఇంటర్‌ఫేస్ (GUIs) కలిగి ఉంటాయి, అక్కడ మీరు బటన్లు క్లిక్ చేసి, టెక్స్ట్ ఇన్‌పుట్ చేసి, ఎంపికలు ఎంచుకుని మరిన్ని చేస్తారు.

### కన్సోల్ మరియు UI అనువర్తనాలు పరిమితముగా ఉంటాయి

క‌మాండ్ టైప్ చేసే అనువర్తనంతో పోల్చండి:

- **పరిమితముగా ఉంటాయి**. మీరు ఏదైనా క‌మాండ్ టైప్ చేయలేరు, కేవలం ఆ అనువర్తనం మద్దతు ఇచ్చే క‌మాండ్లు మాత్రమే.
- **భాష-ప్రత్యేకం**. కొన్ని అనువర్తనాలు అనేక భాషలను మద్దతు ఇస్తాయి, కానీ సాధారణంగా అనువర్తనం ఒక ప్రత్యేక భాషకి నిర్మించబడుతుంది, మీరు మరిన్ని భాషల మద్దతు ఇవ్వగలిగినా.

### టెక్స్ట్ జనరేషన్ అనువర్తనాల ప్రయోజనాలు

అప్పుడు టెక్స్ట్ జనరేషన్ అనువర్తనం ఎలా వేరుగా ఉంటుంది?

టెక్స్ట్ జనరేషన్ అనువర్తనంలో, మీరు ఎక్కువ స్వేచ్ఛ కలిగి ఉంటారు, మీరు క‌మాండ్‌ల సెట్ లేదా ప్రత్యేక ఇన్‌పుట్ భాషతో పరిమితం కాదు. బదులుగా, మీరు సహజ భాషను వాడి అనువర్తనంతో ఇంటరాక్ట్ చేయవచ్చు. మరో ప్రయోజనం ఏమిటంటే, మీరు ఇప్పటికే భారీ సమాచారం సేకరణపై శిక్షణ పొందిన డేటా మూలంతో ఇంటరాక్ట్ అవుతారు, అయితే సాంప్రదాయ అనువర్తనం డేటాబేస్‌లో ఏమి ఉన్నదో పరిమితం కావచ్చు.

### టెక్స్ట్ జనరేషన్ అనువర్తనంతో నేను ఏమి నిర్మించగలను?

మీరు ఎన్నో విషయాలు నిర్మించవచ్చు. ఉదాహరణకు:

- **చాట్‌బోటు**. మీ కంపెనీ మరియు దాని ఉత్పత్తులు గురించి ప్రశ్నలకు సమాధానం ఇస్తున్న చాట్‌బోటు మంచిది.
- **సహాయకుడు**. LLMలు టెక్స్ట్ సారాంశం, టెక్స్ట్ నుండి సమాచారం సేకరణ, రిజ్యూమె లాంటి టెక్స్ట్ తయారీలో మంచి‌ని.
- **కోడ్ అసిస్టెంట్**. మీరు ఉపయోగించే భాషా నమూనాను ఆధారంగా, మీరు కోడ్ రాయడంలో సహాయం చేసే కోడ్ అసిస్టెంట్‌ను నిర్మించవచ్చు. ఉదాహరణకు, GitHub Copilot లేదా ChatGPT వంటివి కోడ్ రాయడంలో సహాయం చేస్తాయి.

## ఎలా ప్రారంభించాలి?

సరే, LLMతో ఇంటిగ్రేట్ కావడానికి మీరు సాధారణంగా ఈ రెండు విధానాలను అనుసరించాలి:

- API ఉపయోగించండి. ఇక్కడ మీరు మీ ప్రాంప్ట్‌తో వెబ్ రిక్వెస్ట్‌లు నిర్మించి, జనరేట్ చేసిన టెక్స్ట్‌ను పొందుతారు.
- లైబ్రరీ ఉపయోగించండి. లైబ్రరీలు API కాల్స్‌ను క్లోజ్ చేసి సులభంగా వాడుటకు సహాయపడతాయి.

## లైబ్రరీలు/SDKలు

LLMsతో పని చేసే కొన్ని ప్రసిద్ధ లైబ్రరీలు ఉన్నాయి:

- **openai**, ఈ లైబ్రరీ మీరు మీ మోడల్‌ను కలుపుకొని ప్రాంప్ట్‌లు పంపడం సులభతరం చేస్తుంది.

ఇంకా ఉన్నత స్థాయిలో చెలామణి చేసే లైబ్రరీలు:

- **Langchain**. Langchain ప్రసిద్ధి మరియు Python మద్దతు ఇస్తుంది.
- **Semantic Kernel**. Semantic Kernel మైక్రోసాఫ్ట్ ద్వారా రూపొందించబడిన లైబ్రరీ, ఇది C#, Python, మరియు Javaను మద్దతు ఇస్తుంది.

## openai ఉపయోగించి మొదటి అనువర్తనం

మన మొదటి అనువర్తనం ఎలా నిర్మించాలో చూద్దాం, ఏ లైబ్రరీలు అవసరం, ఎంత అవసరం అని.

### openaiని ఇన్స్టాల్ చేయండి

OpenAI లేదా Azure OpenAIతో ఇంటరాక్ట్ చేయడానికి ఎన్నో లైబ్రరీలు ఉన్నాయి. మీరు C#, Python, JavaScript, Java మరియు మరిన్ని ప్రోగ్రామింగ్ భాషలతో పనిచేయవచ్చు. మనం `openai` Python లైబ్రరీని ఎంచుకున్నాము, కాబట్టి `pip` తో దాన్ని ఇన్స్టాల్ చేస్తాం.

```bash
pip install openai
```

### ఒక వనరు సృష్టించండి

మీరు ఈ క్రింది దశలను అనుసరించాలి:

- Azureలో ఖాతా సృష్టించండి [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAIకి ప్రాప్తి పొందండి. [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) కి వెళ్ళి ప్రాప్తి తేర్పుకోండి.

  > [!NOTE]
  > వ్రాసే సమయానికి, Azure OpenAIకి ప్రాప్తి కొరకు అప్లై చేయాలి.

- Pythonని ఇన్స్టాల్ చేయండి <https://www.python.org/>
- Azure OpenAI సేవ వనరును సృష్టించుకున్నట్లు చూడండి. అది ఎలా చదవాలో ఈ గైడ్ చూడండి [వనరు సృష్టించడం](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API కీ మరియు ఎండ్‌పాయింట్‌ను కనుగొనండి

ఇప్పుడు, మీరు మీ `openai` లైబ్రరీకి ఏ API కీ వాడాలో చెప్పాలి. మీ API కీ కోసం, Azure OpenAI వనరు యొక్క "Keys and Endpoint" విభాగానికి వెళ్ళి "Key 1" విలువను కాపీ చేసుకోండి.

![Azure పోర్టల్‌లో Keys మరియు Endpoint వనరు బ్లేడ్](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ఇప్పుడున్న ఈ సమాచారాన్ని కాపీ చేసుకున్నారంటే, లైబ్రరీలకు దాన్ని ఉపయోగించమని సూచిద్దాం.

> [!NOTE]
> మీ API కీని కోడుతో వేరుగా ఉంచటం మంచిది. మీరు ముందు పరిసర వేరియబుల్స్ వాడి ఇది చేయవచ్చు.
>
> - పరిసర వేరియబుల్ `OPENAI_API_KEY` కి మీ API కీని అసైన్ చేయండి.
>   `export OPENAI_API_KEY='sk-...'`

### Azure కాన్ఫిగరేషన్ సెట్టప్ చేయండి

మీరు Azure OpenAI (ఇప్పుడు Microsoft Foundry భాగం) వాడుతున్నట్లయితే, ఇలా సెట్టప్ చేయండి. మేము ప్రామాణిక `OpenAI` క్లయింట్‌ను Azure OpenAI `/openai/v1/` ఎండ్‌పాయింట్ వైపు దృష్టిపెట్టుతాం, ఇది Responses APIతో పని చేస్తుంది మరియు `api_version` అవసరం లేదు:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

పైన మనం ఈ వాటిని సెట్ చేస్తున్నాము:

- `api_key`, ఇది Azure పోర్టల్ లేదా Microsoft Foundry పోర్టల్‌లో మీ API కీ.
- `base_url`, ఇది మీ Foundry వనరు ఎండ్‌పాయింట్ `/openai/v1/` తో కూడినది. స్థిరమైన v1 ఎండ్‌పాయింట్ OpenAI మరియు Azure OpenAI రెండింటితో పని చేస్తుంది, `api_version` అవసరం లేదు.

> [!NOTE] > `os.environ` పరిసర వేరియబుల్స్ చదవడానికి వాడుతారు. మీరు `AZURE_OPENAI_API_KEY` మరియు `AZURE_OPENAI_ENDPOINT` వంటి వేరియబుల్స్‌ను టెర్మినల్‌లో లేదా `dotenv` లైబ్రరీ వాడి సెట్ చేయండి.

## టెక్స్ట్ జనరేట్ చేయండి

టెక్స్ట్ జనరేట్ చేయడానికి Responses APIని `responses.create` మెథడ్ ద్వారా ఉపయోగించాలి. ఇది ఉదాహరణ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # ఇది మీ మోడల్ పంపిణీ పేరు
    input=prompt,
    store=False,
)
print(response.output_text)
```

పై కోడ్‌లో, మేము ఒక ప్రతిస్పందన తయారుచేసి, ఆ మోడల్ మరియు ప్రాంప్ట్‌ను పంపిస్తున్నాము. తరువాత `response.output_text` ద్వారా జనరేట్ చేసిన టెక్స్ట్‌ను ప్రింట్ చేస్తాం.

### బహుళ ద్విముఖ సంభాషణలు

Responses API ఒంటి ద్విముఖ టెక్స్ట్ జనరేషన్ మరియు బహుళ-ద్విముఖ చాట్‌బోట్ల కోసం బాగా సరిపోతుంది - మీరు సంభాషణ నిర్మించడానికి `input`లో సందేశాల జాబితాను ఇస్తారు:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

ఈ ఫంక్షనాలిటీపై మరింత సమాచారం వచ్చే అధ్యాయంలో.

## వ్యాయామం - మీ మొదటి టెక్స్ట్ జనరేషన్ అనువర్తనం

ఇప్పుడు మనం openaiను సెటప్ చేసి కాన్ఫిగర్ చేయడానికి నేర్చుకున్నాం, మళ్లీ మీ మొదటి టెక్స్ట్ జనరేషన్ అనువర్తనాన్ని నిర్మిద్దాం. అందుకోసం ఈ దశలను అనుసరించండి:

1. వర్చువల్ ఎన్విరాన్మెంట్ సృష్టించి openai ఇన్స్టాల్ చేయండి:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > మీరు Windows వాడుతున్నట్లయితే `venv\Scripts\activate` టైప్ చేయండి, `source venv/bin/activate` కాకుండా.

   > [!NOTE]
   > మీ Azure OpenAI కీని కనుగొనడానికి [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst)కు వెళ్లి `Open AI` సెర్చ్ చేసి `Open AI resource` ఎంచుకుని, అటు `Keys and Endpoint` మరియు `Key 1` విలువను కాపీ చేయండి.

1. ఒక _app.py_ ఫైల్ సృష్టించి అందులో క్రింది కోడ్ ఇన్సర్ట్ చేయండి:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # మీ పూర్తి కోడ్‌ను జోడించండి
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API ఉపయోగించి ఒక అభ్యర్థన చేయండి
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # ప్రతిస్పందనను ముద్రించండి
   print(response.output_text)
   ```

   > [!NOTE]
   > మీరు సాధారణ OpenAI (Azure కాకుండా) వాడితే `client = OpenAI(api_key="<ఇక్కడ మీ OpenAI కీ పెడండి>")` (ఏ `base_url` అవసరం లేదు) మరియు మోడల్ పేరు `gpt-4o-mini` వంటి పేరు ఇవ్వండి, deployment పేరు కాకుండా.

   మీరు ఆవుట్పుట్‌ను ఈ విధంగా చూడగలరు:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## విభిన్న రకాల ప్రాంప్ట్స్, విభిన్న పనులకు

ఇప్పుడు మీరు ప్రాంప్ట్ ఉపయోగించి టెక్స్ట్ జనరేట్ చేయడం ఎలా అనేది చూశారు. మీరు ఒక ప్రోగ్రామ్ కూడా పొందారు, దాన్ని మార్చి, వేర్వేరు రకాల టెక్స్ట్ జనరేట్ చేయవచ్చు.

ప్రాంప్ట్‌లు అన్న విధాల పనులకోసం ఉపయోగించవచ్చు. ఉదాహరణకు:

- **ఒక రకమైన టెక్స్ట్ జనరేట్ చేయండి**. ఉదాహరణకు, మీరు ఒక కవిత, క్విజ్ ప్రశ్నలు మొదలైనవి రూపొందించవచ్చు.
- **సమాచారం వెతకు**. మీరు ప్రాంప్ట్‌లను ఉపయోగించి సమాచారం వెతుక్కోవచ్చు, ఉదాహరణకు 'వెబ్ డెవలప్మెంట్‌లో CORS అంటే ఏమిటి?'.
- **కోడ్ జనరేట్ చేయండి**. మీరు ప్రాంప్ట్‌లను ఉపయోగించి కోడ్ తయారుచేయవచ్చు, ఉదాహరణకు ఇమెయిల్స్‌ను వెరిఫై చేసే రెగ్యులర్ ఎక్స్‌ప్రెషన్ లేదా మొత్తం ప్రోగ్రామ్, వంటి వెబ్ యాప్.

## మరొక చేసే పనికి అనువైన సందర్భం: ఒక రెసిపీ జనరేటర్

మీరు ఇంట్లో మూలపదార్థాలు ఉన్నట్టు ఊహించండి, మీరు విందు చేయాలనుకుంటున్నారు. దానికి మీకు ఒక రెసిపీ అవసరం. రెసిపీలు వెతకడానికి ఒక శోధన యంత్రం వాడవచ్చు లేదా LLM వాడవచ్చు.

మీరు ఇలా ఒక ప్రాంప్ట్ రాయవచ్చు:

> "క్రింది మూలపదార్థాలతో వంటకానికి 5 రెసిపీలు చూపించండి: కోడి, ఉర్రి మరియు క్యారెట్‌లు. ప్రతి రెసిపీకి ఉపయోగించిన అన్ని మూలపదార్థాలను జాబితా చేయండి"

పై ప్రాంప్ట్ ఇచ్చినపుడు, మీరు ఇలాంటి సమాధానం పొందవచ్చు:

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

ఇది చాలా మంచిది, నాకు వండుకోవడానికి స్పష్టత ఉన్నది. ఇపుడు, ఉపయోగకరంగా ఉండే మెరుగుదలలు ఏవి?

- నాకు ఇష్టంలేని లేదా అలెర్జీ ఉన్న ఆహార పదార్థాలు వడకట్టడం.
- నేను ఇంట్లో అన్ని పదార్థాలు లేనివరకు షాపింగ్ జాబితా తయారుచేయడం.

ఈ కేసులకు, మరొక ప్రాంప్ట్ జోడిద్దాం:

> "దయచేసి రెసిపీల్లో ఉండే వెల్లుల్లి తీసివేయండి, ఎందుకంటే నాకు అలెర్జీ ఉంది, దాన్ని మరోలా మార్చండి. అలాగే, నాకు ఇప్పటికే కోడి, ఉర్రి, క్యారెట్‌లు ఉన్ననిది పరిగణించి షాపింగ్ జాబితా తయారుచేయండి."

ఇప్పుడు మీకు కొత్త ఫలితం వచ్చింది, ఇది:

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

ఇవి మీ ఐదు రెసిపీలు, వెల్లుల్లి పడకుండా, ఇంట్లో ఉన్న పదార్థాలను పరిగణించి షాపింగ్ జాబితా కూడా ఉంది.

## వ్యాయామం - రెసిపీ జనరేటర్ తయారు చేయండి

ఇప్పుడు మేము ఒక సన్నివేశం ఆడుకున్నాం, ఇపుడు ఆ సన్నివేశానికి సరిపడే కోడ్ రాయాలంటే ఈ దశలను అనుసరించండి:

1. ప్రస్తుత _app.py_ ఫైల్‌ను ప్రారంభ బిందువుగా వాడండి
1. `prompt` వేరియబుల్‌ను కనుగొని దాని కోడ్‌ను క్రిందివిధంగా మార్చండి:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   మీరు ఇప్పుడే కోడ్‌ను రన్ చేస్తే, ఈ విధమైన అవుట్పుట్ చూస్తారు:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > గమనిక, మీ LLM వ్యత్యాసాత్మక స్వభావం కలిగి ఉంటుంది, కాబట్టి ప్రతి సారి రన్ చేసినప్పుడు ఫలితాలు భిన్నంగా ఉండవచ్చు.

   చక్కటి విషయం, ఇప్పుడు ఎలా మెరుగుపరచాలో చూద్దాం. మెరుగుదలకు కోడ్ సడలింపుగా ఉండాలి, అందుకే పదార్థాల సంఖ్య మరియు రెసిపీల సంఖ్య మార్చడానికి వీలుగా ఉండాలి.

1. కోడ్‌ను ఈ విధంగా మార్చండి:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # రెసిపీల సంఖ్యను ప్రాంప్ట్ మరియు పదార్థాలలో అంతరించు
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   టెస్ట్ రన్ కోసం కోడ్ ఇలా ఉండవచ్చు:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ఫిల్టర్ మరియు షాపింగ్ లిస్ట్ జోడించడం ద్వారా మెరుగుదల

మనకు ఇప్పుడు రెసిపీలు ఉత్పత్తి చేయగల ఒక పని చేసే అనువర్తనం ఉంది మరియు ఇది సడలింపుగా ఉంది, ఎందుకంటే ఇది వినియోగదారుడి ఇన్‌పుట్లపై ఆధారపడి ఉంటుంది, రెసిపీల సంఖ్య మరియు ఉపయోగించిన పదార్థాలు రెండింటిలో కూడా.

మరింత మెరుగుపరచడానికి, కింది అంశాలను జోడించాలి:

- **పదార్థాలను వడకట్టండి**. మనకి ఇష్టంలేని లేదా అలెర్జీ ఉన్న పదార్థాలను వడకట్టగలరు కావాలి. దీన్ని సాధించేందుకు మన ప్రస్తుత ప్రాంప్ట్‌ను మార్చి చివరలో ఫిల్టర్ పరిస్థితిని జోడించవచ్చు:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  పైన `{filter}` ను ప్రాంప్ట్ చివర చేర్చాము మరియు వాడుకరి నుండి ఫిల్టర్ విలువను కూడా క్యాప్చర్ చేస్తున్నాము.

  ప్రోగ్రామ్ రన్ చేయడంలో ఉదాహరణ ఇన్‌పుట్ ఇలా ఉండవచ్చు:

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

  మీరు చూడగలిగింది ఏమిటంటే, పాల ఉన్న రెసిపీలు వడకట్టబడ్డాయి. కానీ మీరు లాక్టోజ్ అసహ్యంతో ఉంటే, చెడ్డి కలిగిన రెసిపీలను కూడా వడకట్టాలనుకోవచ్చు, కాబట్టి స్పష్టత అవసరం.


- **షాపింగ్ జాబితా తయారు చేయండి**. మనం ఇక్కడ మన ఇంటిలో ఇప్పటికే ఉన్న వాటిని పరిగణనలోకి తీసుకుని షాపింగ్ జాబితాను తయారు చేయాలని ఉంది.

  ఈ ఫంక్షనాలిటీ కోసం, మనం ఒకే ప్రాంప్ట్‌లో అన్ని సమస్యలను పరిష్కరించాలని ప్రయత్నించవచ్చు లేదా రెండు ప్రాంప్ట్‌లుగా విభజించవచ్చు. తర్వాతి దృక్పథాన్ని ప్రయత్నిద్దాం. ఇక్కడ మేము అదనపు ప్రాంప్ట్‌ను జోడించాలని సూచిస్తున్నాము, కానీ అది పని చేసేందుకు, ముందటి ప్రాంప్ట్ ఫలితాన్ని తర్వాతి ప్రాంప్ట్‌కు సందర్భంగా జోడించాలి.

  మొదటి ప్రాంప్ట్ ఫలితాన్ని ప్రింట్ చేసే కోడ్ భాగాన్ని కనుగొని క్రింది కోడ్‌ను క్రింద జోడించండి:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # ప్రతిస్పందనను ముద్రించండి
  print("Shopping list:")
  print(response.output_text)
  ```

  క్రింది విషయాలను గమనించండి:

  1. మొదటి ప్రాంప్ట్ ఫలితాన్ని కొత్త ప్రాంప్ట్‌కు జోడించడం ద్వారా కొత్త ప్రాంప్ట్ తయారు చేస్తున్నాము:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. మేము కొత్త అభ్యర్థన చేస్తాము, అయితే మొదటి ప్రాంప్ట్‌లో అడిగిన టోకెన్ల సంఖ్యను పరిగణలోకి తీసుకుంటూ, ఈసారి `max_output_tokens` ని 1200 గా సూచిస్తాము.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ఈ కోడ్‌ని అమల్లో పెట్టి చూస్తే, మనం క్రింది ఫలితానికి వస్తాము:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## మీ సెటప్‌ను మెరుగుపరచండి

మన దగ్గర ఇప్పటి వరకు పనిచేసే కోడ్ ఉంది, కానీ మరింత మెరుగుపరచడానికి కొన్ని మార్పులు చేయాలి. కొంత మార్పులు చేయవలసినవి:

- **గోప్య విషయాలను కోడ్ నుండి వేరుచేయండి**, ఉదాహరణకు API కీ. గోప్య విషయాలు కోడ్‌లో ఉండకూడదు మరియు వాటిని సురక్షిత స్థలంలో నిల్వ చేయాలి. కోడ్ నుండి గోప్య విషయాలను వేరుచేయడానికి, మేము environment variables మరియు `python-dotenv` లాంటి లైబ్రరీలను ఉపయోగించి ఫైల్ నుంచి లోడ్ చేయవచ్చు. కోడ్‌లో ఇలా కనిపిస్తుంది:

  1. క్రింది విషయములతో `.env` ఫైల్ సృష్టించండి:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > గమనిక, Microsoft Foundryలో Azure OpenAI కోసం, మీరు క్రింది environment variables సెట్ చేయాలి:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     కోడ్‌లో environment variables ఆ విధంగా లోడ్ చేస్తారు:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **టోకెన్ పొడవు గురించి ఒక మాట**. మనం ఎంత టోకెన్లు అవసరమో పరిగణలోకి తీసుకోవాలి. టోకెన్లు ఖర్చు రోజుతుంటాయి, అందువల్ల సాధ్యమైనంత తక్కువ టోకెన్లను ఉపయోగించినప్పుడు ఆర్థికంగా ఉంటుంది. ఉదాహరణకు, ప్రాంప్ట్‌ను ఇలా రాస్తే తక్కువ టోకెన్లు ఉపయోగించవచ్చు?

  టోకెన్లను మార్చడానికైతే, `max_output_tokens` పరామితిని ఉపయోగించవచ్చు. ఉదాహరణకు 100 టోకెన్లు ఉపయోగించాలని ఉంటే, ఇలా చేస్తారు:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **తాపనతో ప్రయోగించండి**. తాపనం మన ప్రోగ్రామ్ ప్రదర్శనకు సంబంధించిన ముఖ్యమైన కోన్సెప్టు. తాపనం విలువు ఎక్కువగా ఉంటే అవుట్పుట్ రాండమ్ ఎక్కువగా ఉంటుంది. తాపనం విలువు తక్కువగా ఉంటే అవుట్పుట్ మరింత ఊహించదగినది అవుతుంది. మీరు అవుట్పుట్‌లో శ్రేణి కావాలా చూడండి.

  తాపనను మార్చాలంటే, `temperature` పరామితిని ఉపయోగించండి. ఉదాహరణకు, 0.5 తాపనం కావాలంటే ఇలా చేస్తారు:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > గమనిక, 1.0 కి చేరువగా ఉన్నప్పుడు అవుట్పుట్ మరింత వైవిధ్యంగా ఉంటుంది.

## అసైన్‌మెంట్

ఈ అసైన్‌మెంట్‌లో మీరు ఏదైనా నిర్మించవచ్చు.

కొన్ని సూచనలు:

- రిసిపీ జనరేటర్ యాప్‌ను ఇంకా మెరుగుపరచడానికి తాపన విలువలు, ప్రాంప్ట్‌లు మార్చి చూడండి.
- "స్టడీ బడీ" ని నిర్మించండి. ఈ యాప్ ఒక విషయం గురించి ప్రశ్నలకు సమాధానం చెప్పగలగాలి, ఉదాహరణకు Python గురించి, "Python లో ఒక విషయం ఏమిటి?" లాంటి ప్రాంప్ట్‌లు ఉండవచ్చు లేదా "ఒక విషయం కోడ్ చూపించు" లాంటి ప్రాంప్ట్ గల యాప్.
- ఇది స్టార్లు చరిత్ర బాట్, చరిత్రను ప్రాణం తెచ్చేలా, బాట్‌ను ఒక చారిత్రక పాత్రలోకి పెట్టి ఆ పాత్ర జీవితం, కాలాల గురించి ప్రశ్నలు అడగండి.

## పరిష్కారం

### స్టడీ బడీ

దిగువ స్టార్టర్ ప్రాంప్ట్ ఉంది, మీరు దీన్ని ఎలా ఉపయోగించి మీ ఇష్టానికి అనుగుణంగా మార్చుకోవచ్చో చూడండి.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### చరిత్ర బాట్

మీరు ఉపయోగించదగిన కొన్ని ప్రాంప్ట్‌లు:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## జ్ఞాన పరీక్ష

తాపనం కాన్సెప్ట్ ఏమి చేస్తుంది?

1. ఇది అవుట్పుట్ ఎంత రాండమ్ అవుతుందో నియంత్రిస్తుంది.
1. ఇది సమాధానం ఎంత పెద్దది అవుతుందో నియంత్రిస్తుంది.
1. ఇది ఎన్ని టోకెన్లు ఉపయోగించబడతాయో నియంత్రిస్తుంది.

## 🚀 చ్యాలెంజ్

అసైన్‌మెంట్ పై పని చేస్తుంటే, తాపనను మార్చి 0, 0.5, 1 విలువలు ప్రయత్నించండి. గుర్తుంచుకోండి 0 అనేది తక్కువ వైవిధ్యమైనది, 1 అనేది ఎక్కువ వైవిధ్యమైనది. మీ యాప్‌కు ఏ విలువు ఉత్తమం?

## శుభకార్యాలు! మీ అభ్యాసాన్ని కొనసాగించండి

ఈ పాఠం పూర్తిచేసిన తర్వాత, మా [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ని చూడండి, మీ Generative AI జ్ఞానాన్ని ఇంకా అభివృద్ధి చేసుకోండి!

లెస్సన్ 7 కి వెళ్లండి, అక్కడ మనం [చాట్ అప్లికేషన్లు ఎలా నిర్మించాలో](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) చూసే కోవళ్లు!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->