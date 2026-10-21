# టెక్స్ట్ ఉత్పత్తి అప్లికేషన్ల నిర్మాణం

[![టెక్స్ట్ ఉత్పత్తి అప్లికేషన్ల నిర్మాణం](../../../translated_images/te/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ఈ పాఠంలోని వీడియోను వీక్షించడానికి పై చిత్రం మీద క్లిక్ చేయండి)_

మీరు ఇప్పటివరకు ఈ పాఠ్యాంశంలో చూసినట్లుగానే ప్రాంప్ట్‌లు వంటి ప్రధాన భావనలు మరియు "ప్రాంప్ట్ ఇంజనీరింగ్" అనే పూర్తి శాస్త్రం కూడా ఉంది. మీరు ChatGPT, Office 365, Microsoft Power Platform వంటి అనేక టూల్‌లతో ప్రాంప్ట్‌లను ఉపయోగించి సహకరించవచ్చు.

మీరు ఒక అప్లికేషన్‌లో ఇలాంటి అనుభవాన్ని చేర్చాలంటే, ప్రాంప్ట్‌లు, కంప్లీషన్స్ వంటి భావనలను అర్థం చేసుకుని, పనిచేయడానికి ఒక లైబ్రరీ ఎంచుకోవాలి. ఇదే మీరు ఈ అధ్యాయంలో నేర్చుకునేది.

## పరిచయం

ఈ అధ్యాయంలో, మీరు:

- openai లైబ్రరీ మరియు దాని ప్రధాన భావనలను గురించి నేర్చుకుంటారు.
- openai ఉపయోగించి టెక్స్ట్ ఉత్పత్తి అప్లికేషన్ తయారు చేయడం.
- ప్రాంప్ట్, టెంపరేచర్ మరియు టోకెన్లు వంటి భావనలను ఉపయోగించి టెక్స్ట్ ఉత్పత్తి అప్లికేషన్ ఎలా తయారు చేయాలో అర్థం చేసుకోవడం.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం చివరికి, మీరు చేయగలుగుతారు:

- టెక్స్ట్ ఉత్పత్తి అప్లికేషన్ అంటే ఏమిటో వివరించండి.
- openai ఉపయోగించి టెక్స్ట్ ఉత్పత్తి అప్లికేషన్ తయారు చేయండి.
- మీ అప్లికేషన్‌లో టోకెన్లను తగ్గించడము లేక పెంచడం, అలాగే టెంపరేచర్ మార్చడం ద్వారా ఫలితాలను విభిన్నంగా మార్చడం.

## టెక్స్ట్ ఉత్పత్తి అప్లికేషన్ అంటే ఏమిటి?

సాధారణంగా మీరు ఒక అప్లికేషన్ నిర్మించినప్పుడు, దానికి ఈ క్రింది వాటిలా ఎలాంటి ఇంటర్‌ఫేస్ ఉంటుంది:

- కమాండ్ ఆధారిత. కన్సోల్ అప్లికేషన్లు సాధారణంగా మీరు కమాండ్ టైప్ చేసి పని చేయి చేస్తాయి. ఉదాహరణకు, `git` ఒక కమాండ్ ఆధారిత అప్లికేషన్.
- యూజర్ ఇంటర్‌ఫేస్ (UI). కొన్ని అప్లికేషన్లకు గ్రాఫికల్ యూజర్ ఇంటర్‌ఫేస్ (GUIs) ఉండి, మీరు బటన్లు క్లిక్ చేసి, టెక్స్ట్ ఇన్పుట్ చేసి, ఆప్షన్లు ఎంచుకొని వంటివి చేస్తారు.

### కన్సోల్ మరియు UI అప్లికేషన్లు పరిమితంగా ఉంటాయి

మీరు ఒక కమాండ్ టైప్ చేసే కమాండ్ ఆధారిత అప్లికేషన్‌తో దీన్ని పోల్చండి:

- **పరిమితం ఉంది**. మీరు ఏ కమాండ్‌ అయినా టైప్ చేయలేరు, కేవలం అప్లికేషన్ మద్దతు ఇచ్చే కమాండ్‌లే.
- **భాషాపరిమితి**. కొన్ని అప్లికేషన్లు అనేక భాషలను మద్దతిస్తాయి, కానీ డిఫాల్ట్‌గా అప్లికేషన్ ఒక నిర్దిష్ట భాష కోసం తయారైంది, మీరు మరిన్ని భాషల మద్దతు జోడించినా.

### టెక్స్ట్ ఉత్పత్తి అప్లికేషన్ల లాభాలు

టెక్స్ట్ ఉత్పత్తి అప్లికేషన్ ఎలా వేరుగా ఉంటుంది?

టెక్స్ట్ ఉత్పత్తి అప్లికేషన్‌లో మీరు ఎక్కువ సరళత కలిగి ఉంటారు, మీరు నిర్దిష్ట కమాండ్‌లు లేదా ఇన్‌పుట్ భాషతో పరిమితం కాదు. మీరు సహజ భాష ఉపయోగించి అప్లికేషన్‌తో సంభాషించవచ్చు. మరో లాభం ఏమిటంటే, మీరు ఇప్పటికే విస్తృత సమాచారం సంగ్రహంపై శిక్షణ పొందిన డేటాస్రోత్తుతో పనిచేస్తున్నారు, ఇది సాంప్రదాయ అప్లికేషన్లలో ఉండే డేటాబేస్ పరిమితి ఉండదు.

### టెక్స్ట్ ఉత్పత్తి అప్లికేషన్‌తో నేను ఏమి తయారు చేయగలను?

మీరు ఎన్నో דברים తయారు చేయవచ్చు. ఉదాహరణకు:

- **చాట్‌బాట్**. మీ కంపెనీ మరియు దాని ఉత్పత్తుల గురించి ప్రశ్నలకు జవాబివ్వగల చాట్‌బాట్ మంచి సరిపోతుంది.
- **సహాయకుడు**. LLMs టెక్స్ట్ సారాంశం తయారు చేయడం, టెక్స్ట్ నుండి అంతర్దృష్టి పొందడం, రిజ్యూమేలు వంటివాటిని తయారు చేయడంలో చాలా చక్కగా ఉంటాయి.
- **కోడ్ అసిస్టెంట్**. మీరు ఉపయోగించే భాషా మోడెల్ మీద ఆధారపడి, కోడ్ రాయడంలో సహాయం చేసే కోడ్ అసిస్టెంట్ తయారు చేయవచ్చు. ఉదాహరణకు, GitHub Copilot లేదా ChatGPT లాంటి ఉత్పత్తులు కోడ్ రాయడంలో మీకు సహాయం చేస్తాయి.

## నేను ఎలా మొదలు పెట్టగలను?

మీరు సాధారణంగా LLMతో ఇంటిగ్రేట్ అయ్యే రెండు దారులను అనుసరించాలి:

- API ఉపయోగించండి. ఇక్కడ మీరు మీ ప్రాంప్ట్‌తో వెబ్ రిక్వెస్ట్‌లు నిర్మించి, జనరేట్ చేసిన టెక్స్ట్‌ను పొందుతారు.
- లైబ్రరీ ఉపయోగించండి. లైబ్రరీలు API కాల్స్‌ను ముగ్గురించి, వాటిని సులభంగా ఉపయోగించేందుకు సహాయపడతాయి.

## లైబ్రరీలు/SDKs

LLMsతో పనిచేసేందుకు ప్రసిద్ధి గాంచిన కొన్ని లైబ్రరీలు ఉన్నాయి:

- **openai**, ఈ లైబ్రరీ మీ మోడల్‌తో సులభంగా కనెక్ట్ అయి ప్రాంప్ట్‌లు పంపటానికి అనుకూలం.

తర్వాత ఉన్నత స్థాయిలో పనిచేసే కింది లైబ్రరీలు ఉన్నాయి:

- **Langchain**. Langchain చాలా ప్రసిద్ధి కలిగి ఉంది మరియు Python మద్దతు ఇస్తుంది.
- **Semantic Kernel**. Semantic Kernel Microsoft నుంచి లైబ్రరీ, ఇది C#, Python, మరియు Java భాషలను మద్దతిస్తుంది.

## openai ఉపయోగించే మొదటి అప్లికేషన్

మన మొదటి అప్లికేషన్ ఎలా రూపొందించగలమో, ఏ లైబ్రరీలు అవసరమో, ఎంత అవసరమో చూద్దాం.

### openai ఇన్‌స్టాల్ చేస్తే ఎలా ఉంటుంది

OpenAI లేదా Azure OpenAIతో ఇంటరాక్ట్ అయ్యేందుకు అనేక లైబ్రరీలు ఉన్నాయి. C#, Python, JavaScript, Java మరియు ఇతర అనేక ప్రోగ్రామింగ్ భాషలను ఉపయోగించవచ్చు. మేము Python లైబ్రరీ అయిన `openai`ను ఎంచుకున్నాము, కాబట్టి దాన్ని ఇన్‌స్టాల్ చేయడానికి `pip` ఉపయోగించ겠습니다.

```bash
pip install openai
```

### ఆదాయం సృష్టించండి

మీరు ఈ క్రింది దశలను త antisaca:

- Azureలో ఒక ఖాతాను సృష్టించండి [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)].
- Azure OpenAIకి యాక్సెస్ పొందండి. [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst)] వెక్కి యాక్సెస్ కోసం అభ్యర్థించండి.

  > [!NOTE]
  > ఇదివరకు రాసేటప్పుడు, Azure OpenAIకి యాక్సెస్ కోసం আবেদন చేయాలి.

- Python ఇన్‌స్టాల్ చేయండి <https://www.python.org/>
- Azure OpenAI సర్వీస్ వనరును సృష్టించండి. [వనరును సృష్టించడం ఎలా](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) అనే గైడ్‌ను చూడండి.

### API కీ మరియు ఎండ్‌పాయింట్‌ని కనుగొన్నది

ఇప్పుడు, మీ `openai` లైబ్రరీకి ఏ API కీ ఉపయోగించాలో చెప్పాలి. మీ API కీ కనుగొనడానికి, మీ Azure OpenAI వనరు "Keys and Endpoint" విభాగానికి వెళ్లి "Key 1" విలువను కాపీ చేసుకోండి.

![Azure Portalలో Keys and Endpoint వనరు బ్లేడ్](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ఇప్పుడు మీరు ఈ సమాచారాన్ని కాపీ చేసుకున్నందున, లైబ్రరీలను దీన్ని ఉపయోగించమని సూచిద్దాం.

> [!NOTE]
> మీ API కీని కోడ్ నుండి వేరుగా ఉంచడం మంచిదే. మీరు పర్యావరణ ఫలకాలుగా (environment variables) దీన్ని చేయవచ్చు.
>
> - పర్యావరణ ఫలకం `OPENAI_API_KEY` ను మీ API కీకి సెట్ చేయండి.
>   `export OPENAI_API_KEY='sk-...'`

### Azure కాన్ఫిగరేషన్ సెటప్ చేయడం

మీరు Azure OpenAI (ఇప్పుడు Microsoft Foundry భాగం) ఉపయోగిస్తుంటే, ఇలా కాన్ఫిగరేషన్ సెటప్ చేయాలి. మేము సాధారణ `OpenAI` క్లయింట్ ఉపయోగిస్తాము, ఇది Azure OpenAI `/openai/v1/` ఎండ్‌పాయింట్‌కి చూపిస్తుంది. ఇది Responses APIతో పనిచేస్తుంది మరియు `api_version` అవసరం లేదు:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

పైన మేము ఈ క్రింది దశలను సెటప్ చేస్తున్నాము:

- `api_key`, ఇది మీ API కీ, Azure Portal లేదా Microsoft Foundry పోర్టల్‌లో కనబడుతుంది.
- `base_url`, ఇది మీ Foundry వనరు ఎండ్‌పాయింట్, అందులో `/openai/v1/` జోడించబడింది. స్ధిరమైన v1 ఎండ్‌పాయింట్ OpenAI మరియు Azure OpenAI రెండింటిలోనూ `api_version` నిర్వహణ అవసరం లేకుండా పనిచేస్తుంది.

> [!NOTE] > `os.environ` పర్యావరణ ఫలకాలను చదువుతుంది. మీరు దీన్ని ఉపయోగించి `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` వంటి పర్యావరణ ఫలకాలను చదవవచ్చు. ఈ పర్యావరణ ఫలకాలను మీ టెర్మినల్‌లో లేదా `dotenv` లాంటి లైబ్రరీ ద్వారా సెట్ చేయండి.

## టెక్స్ట్ ఉత్పత్తి చేయడం

టెక్స్ట్ రూపొందించడానికి Responses APIలోని `responses.create` పద్ధతిని ఉపయోగించాలి. ఉదాహరణ ఇది:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

పైన కోడ్‌లో మేము ప్రతిస్పందన సృష్టించి, ఉపయోగించదలచిన మోడల్ మరియు ప్రాంప్ట్‌ను అందిస్తాము. తర్వాత `response.output_text` ద్వారా ఉత్పన్నమైన టెక్స్ట్‌ను ప్రింట్ చేస్తాము.

### బహుళ-తరం సంభాషణలు

Responses API ఒక్కసారి టెక్స్ట్ ఉత్పత్తికి మాత్రమే కాకుండా బహుళ-తరం చాట్‌బాట్లకూ బాగా సరిపోతుంది - మీరు `input`లో సందేశాల జాబితాను అందించి సంభాషణను నిర్మిస్తారు:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

ఈ కార్యాచరణపై మరింత సమాచారం ఒక రాబోయే అధ్యాయంలో.

## వ్యాయామం - మీ మొదటి టెక్స్ట్ ఉత్పత్తి అప్లికేషన్

ఇప్పుడు మీరు openai సెటప్ మరియు కాన్ఫిగర్ చేయడం నేర్చుకున్నందున, మీ మొదటి టెక్స్ట్ ఉత్పత్తి అప్లికేషన్ తయారుచేసే సమయం వచ్చింది. మీ అప్లికేషన్ కోసం క్రింద פעולה చేయండి:

1. వర్చువల్ ఎన్విరాన్మెంట్ సృష్టించి openai ని ఇన్‌స్టాల్ చేయండి:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > మీరు Windows వాడుతున్నట్లయితే `venv\Scripts\activate` ను `source venv/bin/activate` కంటె ఉపయోగించండి.

   > [!NOTE]
   > మీ Azure OpenAI కీని కనుగొనండి [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst)లోకి వెళ్లి `Open AI` కోసం శోధించి, `Open AI resource` ఎంచుకుని, తరువాత `Keys and Endpoint` ఎంచుకుని `Key 1` విలువను కాపీ చేయండి.

1. _app.py_ ఫైల్ సృష్టించి క్రింది కోడ్ ఇవ్వండి:

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
   > మీరు సాధారణ OpenAI (Azure కాదు) ఉపయోగిస్తుంటే, `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (ఎటువంటి `base_url` కాదని) మరియు deployment పేరు కాకుండా మోడల్ పేరును `gpt-5-mini` లాగా ఇవ్వండి.

   మీరు క్రింది అ.Outputను చూడవచ్చు:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## భిన్న రకాల ప్రాంప్ట్‌లు, వివిధ పనులకోసం

ఇప్పుడు మీరు ప్రాంప్ట్ ఉపయోగించి టెక్స్ట్ ఎలా తయారు చేసుకోవచ్చో చూశారు. మీరు మీ కోడ్కి మార్పులు చేసి, వివిధ రకాల టెక్స్ట్‌లను ఉత్పత్తి చేయవచ్చు.

ప్రాంప్ట్‌లు అనేక పనులకోసం ఉపయోగించవచ్చు. ఉదాహరణకు:

- **ఒక రకమైన టెక్స్ట్‌ను ఉత్పత్తి చేయండి**. ఉదాహరణకు, మీరు ఒక కవిత, క్విజ్ ప్రశ్నలు మొదలైనవి తయారు చేయవచ్చు.
- **సూచనలను వెతకండి**. మీరు ప్రాంప్ట్‌లను ఉపయోగించి సమాచారం వెతకవచ్చు, ఉదాహరణకు 'Web developmentలో CORS అంటే ఏమిటి?'.
- **కోడ్ ఉత్పత్తి చేయండి**. మీరు ప్రాంప్ట్ ఉపయోగించి కోడ్ కూడా తయారు చేయవచ్చు, ఉదాహరణకు ఇమెయిల్స్ చెక్ చేసే రెగ్యుల్ లెక్స్ప్రెషన్ కోడ్ రూపొందించడం లేదా ఒక పూర్తి ప్రోగ్రామ్, వెబ్ అప్లికేషన్ వంటి దానిని.

## ఒక మరింత ఉపయోగకరమైన ఉదాహరణ: రెసిపీ జనరేటర్

మీరు ఇంట్లో పదార్థాలు ఉన్నాయని అనుకోండి, మీరు దేనవదైనా వంట చేయాలనుకుంటున్నారు. అర్థం కోసం, మీరు రెసిపీ అవసరం. రెసిపీల కోసం వెతకడానికి సెర్చ్ ఇంజిన్ లేదా LLM ఉపయోగించవచ్చు.

మీరు క్రింది విధంగా ప్రాంప్ట్ రాయవచ్చు:

> "కాబ chicken, బంగాళాదుంపా మరియు క్యారెట్లు ఉన్న వంటకానికి 5 రెసిపీలను చూపించండి. ప్రతి రెసిపీలో ఉపయోగించిన పదార్థాల జాబితా ఇవ్వండి"

పై ప్రాంప్ట్ ఇచ్చిన తర్వాత ఇంతేలా సమాధానం రావచ్చు:

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

ఈ ఫలితం ఎంతగానో ఉపయుక్తం, నాకు వంటకి ఏం చేయాలో తెలుసు. ఈ సమయంలో ఉపయోగకరమైన మార్పులు ఏమిటంటే:

- నాకు ఇష్టం లేని లేదా అలెర్జీ ఉన్న పదార్థాలను తొలగించడం.
- నేను ఇంట్లో అన్ని పదార్థాలు లేకపోతే, షాపింగ్ లిస్ట్ తయారు చేయడం.

పై సందర్భాలకు, అదనపు ప్రాంప్ట్‌ ఇవ్వండి:

> "దయచేసి నేను అలెర్జీ కలిగిన గార్లిక్ ఉన్న రెసిపీలను తీసేయండి మరియు దానికి ప్రత్యామ్నాయం ఇవ్వండి. అలాగే, ఈ రెసిపీల కోసం షాపింగ్ లిస్ట్ ఇవ్వండి, నేను ఇప్పటికే chicken, బంగాళాదుంప మరియు క్యారెట్లు ఇంట్లో ఉన్నాయని పరిగణనలోకి తీసుకుని."

ఇప్పుడు మీరు కొత్త ఫలితాన్ని పొందారు, అంటే:

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

ఇది మీ 5 రెసిపీలు, గార్లిక్ లేకుండా మరియు మీరు ఇంట్లో ఇప్పటికే ఉన్న పదార్థాలను పరిగణించి షాపింగ్ లిస్ట్ కూడా ఉంది.

## వ్యాయామం - రెసిపీ జనరేటర్ తయారు చేయండి

ఇప్పుడు మీరు ఒక సన్నివేశం ఆడిన తర్వాత, మీరు దానికి సరిపోయే కోడ్ రాయాలి. దానికి క్రింది దశలను అనుసరించండి:

1. ఇప్పటికే ఉన్న _app.py_ ఫైల్ను షురుగా ఉపయోగించండి
1. `prompt` వేరియబుల్‌ని కనుగొని దాని కోడ్‌ను క్రిందివిధంగా మార్చండి:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ఇప్పుడు మీరు కోడ్ నడిపిస్తే, క్రింది ఫలితాన్ని చూడవచ్చు:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > గమనిక, మీ LLM అనిశ్చితంగా ఉంటుంది, కాబట్టి ప్రతి సారి ప్రోగ్రామ్ నడిపినప్పుడు ఫలితాలు వేరుగా రావచ్చు.

   బాగుండి, కోడ్ ఇంకా మెరుగుపడడానికి మేము చూడదలిచాము. మెరుగుపరచడం కోసం, కోడ్ సరళతగలదిగా ఉండాలి, అంటే రెసిపీల సంఖ్య మరియు పదార్థాలు మార్చటంకూ సౌకర్యం ఉండాలి.

1. కోడ్‌ను క్రింది విధంగా మార్చండి:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ఈ కోడ్‌ను పరీక్షింతదిగా పరిగణించవచ్చు:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ఫిల్టర్ మరియు షాపింగ్ లిస్ట్ జోడించి మెరుగుపరచండి

ఇప్పుడు మన దగ్గర రెసిపీలు తయారు చేయగల పని చేసే అప్లికేషన్ ఉంది మరియు ఇది వినియోగదారుకు సంబంధించిన ఇన్‌పుట్లపై ఆధారపడి సరళమైనది, రెసిపీల సంఖ్య మరియు పదార్థాలు ఇన్పుట్‌ను మార్చుకోవచ్చు.

ఇంకో మెరుగుదల కోసం, క్రింది విధంగా జోడించదలచాము:

- **ఇష్ట ఆనాది పదార్థాలను ఫిల్టర్ చేయండి**. మాకు నచ్చని లేదా అలెర్జీ కలిగిన పదార్థాలను వదిలివేయగల సమర్థత కావాలి. దీని కోసం మన ప్రాంప్ట్‌ను మార్చి చివరలో ఫిల్టర్ శరతును ఈ విధంగా జోడించవచ్చు:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  పై కోడ్‌లో మనం ప్రాంప్ట్ చివర `{filter}` జోడించి, వినియోగదారుని నుండి ఫిల్టర్ విలువను కూడా పొందుతాము.

  ప్రోగ్రామ్ నడపినప్పుడు ఇలాంటిది ఇన్‌పుట్ ఉండవచ్చు:

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

  మీరు గమనిస్తే, milk ఉన్న రెసిపీలన్నీ ఫిల్టర్ అయ్యాయి. కానీ మీరు లాక్టోజ్ అసహనం ఉంటే cheese ఉన్న రెసిపీలను కూడా తొలగించాలనుకుంటారు, కాబట్టి నిర్దిష్టత అవసరం.

- **షాపింగ్ లిస్ట్ ఉత్పత్తి చేయండి**. మీ దగ్గర ఇప్పటికే ఉన్న పదార్థాలను పరిగణించి షాపింగ్ లిస్ట్ తయారు చేయాలి.

  దీని కోసం, మనం ఒకే ప్రాంప్ట్‌లోనే అంతా చేయవచ్చు లేదా రెండింటి ప్రక్రియను విడగొట్టి చేయవచ్చు. మనం రెండవ విధానాన్ని ప్రయత్నిద్దాం. ఇక్కడ అదనపు ప్రాంప్ట్ జోడిస్తున్నాము, కానీ అది పనిచేయడానికి తొలవ ప్రాంప్ట్ ఫలితాన్ని రెండవ ప్రాంప్ట్‌కు సందర్భంగా జోడించాలి.

  కోడ్‌లో మొదటి ప్రాంప్ట్ ఫలితాన్ని ప్రింట్ చేస్తున్న భాగాన్ని కనుగొని క్రింద ఇచ్చిన కోడ్‌ను జోడించండి:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  ఈ విషయాలు గమనించండి:

  1. మనం కొత్త ప్రాంప్ట్‌ను నిర్మిస్తోంది, తొల వ ప్రాంప్ట్ ఫలితాన్ని కొత్త ప్రాంప్ట్‌లో చేర్చడం:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. కొత్త అభ్యర్థన పంపుతున్నాము, కానీ మొదటి ప్రాంప్ట్‌లో అడిగిన టోకెన్ల సంఖ్యను పరిగణిస్తున్నాము, అంటే ఈ సారి `max_output_tokens` ను 1200గా చెబుతున్నాము.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ఈ కోడ్‌ను నడిపితే, ఇప్పుడు ఈ క్రింది అవుట్‌పుట్ వస్తుంది:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## మీ సెటప్ మెరుగుపరచండి

ఇప్పటివరగా మన వద్ద ఉన్నది పని చేసే కోడ్, కానీ విషయాలను మరింత మెరుగుపర్చడానికి కొన్ని సవరింపులు చేయాలి. మనం చేయవలసిన కొన్ని విషయాలు:

- **రహస్యాలను కోడ్ నుండి వేరుగా ఉంచండి**, ఉదాహరణకు API కీ. రహస్యాలు కోడ్‌లో ఉండకూడదు మరియు భద్రతగల స్థానంలో నిల్వ చేయాలి. రహస్యాలను కోడ్ నుండి వేరుగా ఉంచడానికి, మనం వాతావరణ చారాలు మరియు `python-dotenv` లాంటి గ్రంథాలయాలను ఫైల్ నుండి లోడ్ చేయడానికి ఉపయోగించవచ్చు. ఇలా కోడ్‌లో కనిపిస్తుంది:

  1. క్రింది కంటెంట్‌తో `.env` ఫైల్ సృష్టించండి:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > గమనిక, Microsoft Foundryలో Azure OpenAIకు, మీకు క్రింది వాతావరణ చారాలను సెటప్ చేయాల్సి ఉంటుంది:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     కోడ్‌లో, మీరు వాతావరణ చారాలను ఇలా లోడ్ చేస్తారు:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **టోకెన్ పొడవు గురించి మాట**. మనం కావలసిన వచనం సృష్టించడానికి ఎంత మంది టోకెన్లు అవసరమో తేల్చుకోవాలి. టోకెన్లకు ఖర్చు వస్తుంది, కావున ఎక్కడ మంచిదైతే, మనం ఉపయోగించే టోకెన్ల సంఖ్య గురించి ఆర్థికంగా ఉండాలి. ఉదాహరణకి, మనం ప్రాంప్ట్ను ఇలా ఏర్పాటు చేయగలమా, టోకెన్లు తక్కువగా ఉపయోగించడానికి?

  టోకెన్లు మార్చేందుకు, మీరు `max_output_tokens` పారామితిని ఉపయోగించవచ్చు. ఉదాహరణకి, మీరు 100 టోకెన్లు ఉపయోగించాలనుకుంటే, ఇలా చేస్తారు:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **తాపం (temperature) తో ప్రయోగం**. తాపం అనేది ఇప్పటివరకు మనం పేర్కొనలేదు కానీ ఇది మన ప్రోగ్రాం వ్యవహారానికి ముఖ్యమైన సందర్భం. తాపం విలువ ఎక్కువగా ఉంటే అవుట్పుట్ ఎక్కువగా యాదృచ్ఛికంగా ఉంటుంది. తాపం విలువ తక్కువగా ఉంటే అవుట్పుట్ ఎక్కువగా అంచనాకారంగా ఉంటుంది. మీరు మీ అవుట్పుట్‌లో వైవిధ్యం కావాలా, లేదా అన్నదానిపై ఆలోచించండి.

  తాపాన్ని మార్చేందుకు, మీరు `temperature` పారామితిని ఉపయోగించవచ్చు. ఉదాహరణకి, మీరు 0.5 తాపం ఉపయోగించాలనుకుంటే, ఇలా చేస్తారు:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > గమనిక, 1.0కి càng దగ్గరగా ఉంటే, అవుట్పుట్ మరింత విభిన్నంగా ఉంటుంది.

- **కారణం మోడళ్లు `temperature` ఉపయోగించవు**. ఇది 2026 లో ఒక ముఖ్యమైన మార్పు. Microsoft Foundryపై ప్రస్తుతం, డిప్రికేటెడ్ కాని మోడళ్లు **కారణం మోడళ్లు** (GPT-5 కుటుంబం, o-శ్రేణి) - మరియు అవి **`temperature` లేదా `top_p` ను మద్దతు ఇవ్వవు** (మరియు `max_tokens` కూడా కాదు; దానికి`max_output_tokens` ఉపయోగించండి). మీరు `temperature` ను `gpt-5-mini` కు పంపితే మీరు "పారామీటర్ మద్దతు ఇవ్వబడలేదు" అనే పొరపాటు వస్తుంది. కాబట్టి పై ఉదాహరణలోని తాపనాన్ని పరీక్షించాలంటే, మరింత సమర్థించే మోడల్ తీసుకోండి - ఉదాహరణకి ఓపెన్ **Llama** మోడల్ అయిన `Llama-3.3-70B-Instruct` ని [Microsoft Foundry మోడల్ క్యాటలాగ్](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) నుండి తీసుకోండి, దీన్ని Foundry Models / Azure AI Inference ఎండ్పాయింట్ ద్వారా పిలవండి (అందే విధంగా `githubmodels-*` నమూనాలు పిలువబడతాయి). GPT-5 వంటి కారణం మోడళ్లకు మీరు ఆউట్‌పుట్‌ను వేరుగా నియంత్రిస్తారు:
  - **ప్రాంప్ట్ ఇంజనీరింగ్** - స్పష్టమైన సూచనలు, ఉదాహరణలు, మరియు నిర్మిత ఆవుట్పుట్ (పాఠం [04 - ప్రాంప్ట్ ఇంజనీరింగ్](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) చూడండి) నంప_sampling రాత్రికి పనిచేస్తాయి.
  - **కారణ నియంత్రణలు** - కారణ ప్రయత్నం/వాయిస్‌ఫుల్‌నెస్ వంటి పారామితులు కారణం లోతును ఆలస్యం మరియు ఖర్చుతో ప్రతిస్పర్ధించేలా సూచిస్తాయి.

  సంక్షిప్తంగా: `temperature`/`top_p` చాలా మోడళ్లపై ఇంకా చెలామణీ అవుతాయి (Llama, Mistral, Phi, మరియు GPT-4.x కుటుంబం - అయితే GPT-4.x డిప్రికేటింగ్ అవుతోంది), కానీ ప్రయాణ దిశ ప్రాంప్ట్ ఇంజనీరింగ్ + కారణ నియంత్రణలు GPT-5 వంటి కారణం మోడళ్లపై అనుసరించబడుతోంది.

## అసైన్‌మెంట్

ఈ అసైన్‌మెంట్ కోసం, మీరు ఏది నిర్మించాలనుకుంటున్నారో ఎంచుకోవచ్చు.

కొన్ని సూచనలు ఇక్కడ ఉన్నాయి:

- రెసిపీ జనరేటర్ యాప్ మరింత మెరుగుపర్చడానికి, టెంపరేచర్ విలువలతో, మరియు ప్రాంప్ట్‌లతో ఆడుతూ చూడు, నువ్వు ఏం రాబట్టగలవో చూడండిని.
- "స్టడీ బడీ"ను రూపొందించు. ఈ యాప్ ఒక అంశం గురించి ప్రశ్నలకు సమాధానం చెప్పగలిగినట్టు ఉండాలి. ఉదాహరణకు Python గురించి ఉంటే, "Python లో ఒక నిర్దిష్ట అంశం ఏమిటి?" వంటి ప్రాంప్ట్‌లు ఉండవచ్చు, లేక "నాకు ఒక నిర్దిష్ట అంశానికి సంబంధించిన కోడ్ చూపించు" అనే ప్రాంప్ట్ కూడా ఉండవచ్చు.
- చరిత్ర బాట్, చరిత్రని జీవంతం చేయించు, బాట్‌ని ఒక నిర్దిష్ట చారిత్రాత్మక పాత్రను ఆడించమని సూచించి, దాని జీవితం మరియు కాలాలు గురించి ప్రశ్నలు అడుగు.

## పరిష్కారం

### స్టడీ బడీ

క్రింద ఒక స్టార్టర్ ప్రాంప్ట్ ఉంది, ఇది ఎలా ఉపయోగించుకోవచ్చో మరియు నీ ఇష్టానికి సరిపడ도록 ఎలా మార్చుకోవచ్చో చూడండి.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### చరిత్ర బాట్

కొన్ని ప్రాంప్ట్‌లు ఇక్కడ ఉన్నాయి, మీరు వీటిని ఉపయోగించవచ్చు:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## జ్ఞాన పరిశీలన

టెంపరేచర్ కాన్సెప్టు ఏమి చేస్తుంది?

1. అవుట్‌పుట్ ఎంత రాండమై ఉండాలో నియంత్రిస్తుంది.
1. సమాధానం ఎంత పెద్దదో నియంత్రిస్తుంది.
1. ఎన్ని టోకెన్లు ఉపయోగించాలో నియంత్రిస్తుంది.

## 🚀 సవాలు

అసైన్మెంట్ మీద పని చేస్తుంటే, టెంపరేచర్ వేరే వేరే విలువలకు ప్రయత్నించండి, దాన్ని 0, 0.5, మరియు 1 గా సెట్ చేసి చూడండి. 0 అంటే తక్కువ రకం మార్పులు, 1 అంటే ఎక్కువ మార్పులు. మీ యాప్‌కు ఏ విలువు ఉత్తమమో తెలుసుకోండి.

## అద్భుతమైన పని! మీ నేర్చుకోవడాన్ని కొనసాగించండి

ఈ పాఠం పూర్తి చేసిన తరువాత, మా [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)ని చూసి మీ Generative AI జ్ఞానాన్ని మరింత పెంచుకోండి!

లెస్సన్ 7 కి వెళ్లండి, అక్కడ మేము [చాట్ అప్లికేషన్లు ఎలా తయారు చేయాలో](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) చూద్దాం!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->