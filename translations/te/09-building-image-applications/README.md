# ఇమేజ్ జనరేషన్ అప్లికేషన్లు తయారు చేయడం

[![ఇమేజ్ జనరేషన్ అప్లికేషన్లు తయారు చేయడం](../../../translated_images/te/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMలు కేవలం టెక్స్ట్ జనరేషన్‌కు మాత్రమే పరిమితం కాదు. టెక్స్ట్ వివరణల నుండి కూడా చిత్రాలను సృష్టించడం సాధ్యం. చిత్రాలు ఒక మోడ్ గా ఉండటం మెడటెక్, ఆర్కిటెక్చర్, టూరిజం, గేమ్ డెవలప్‌మెంట్ మొదలైన అనేక రంగాల్లో అత్యంత ఉపయోగకరంగా ఉంటుంది. ఈ అధ్యాయంలో, రెండు అత్యంత ప్రాచుర్యం పొందిన చిత్ర జనరేషన్ మోడల్స్ అయిన DALL-E మరియు Midjourneyని పరిశీలిస్తాము.

## పరిచయం

ఈ పాఠంలో మనం కవర్ చేయబోతున్నవి:

- చిత్ర జనరేషన్ మరియు అది ఎందుకు ఉపయోగకరమో.
- DALL-E మరియు Midjourney అంటే ఏమిటి, అవి ఎలా పనిచేస్తాయి.
- మీరు చిత్ర జనరేషన్ యాప్‌ను ఎలా నిర్మించగలరో.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం పూర్తయ్యాక, మీరు చేయగలరని:

- ఒక చిత్ర జనరేషన్ అప్లికేషన్‌ను నిర్మించండి.
- మీ అప్లికేషన్ boundaryలను మెటా ప్రాంప్ట్‌లతో నిర్వచించండి.
- DALL-E మరియు Midjourneyతో పని చేయండి.

## చిత్ర జనరేషన్ అప్లికేషన్ ఎందుకు తయారు చేయాలి?

చిత్ర జనరేషన్ అప్లికేషన్లు జనరేటివ్ AI సామర్థ్యాలను అన్వేషించడానికి అద్భుతమైన మార్గం. వాటిని, ఉదాహరణకి:

- **చిత్ర సంస్కరణ మరియు సంయోజన**. మీరు వివిధ వినియోగాల కోసం చిత్రాలను సృష్టించవచ్చు, ఉదాహరణకు చిత్రం ఎడిట్ చేయడం మరియు చిత్రం సంయోజనం.

- **వివిధ పరిశ్రమలకు వర్తించు**. అవి మెడటెక్, టూరిజం, గేమ్ డెవలప్‌మెంట్ మరియు మరింత పరిశ్రమల కోసం చిత్రాలు సృష్టించడానికి కూడా ఉపయోగపడతాయి.

## పరిస్థితి: Edu4All

ఈ పాఠం భాగంగా, మనం Edu4All స్టార్ట్‌అప్‌తో కొనసాగుతాము. విద్యార్థులు తమ అసెస్మెంట్ల కోసం చిత్రాలను సృష్టిస్తారు, ఆ చిత్రాలు ఏవి కావాలో విద్యార్థులపై ఆధారపడుతుంది: వారికి వారి స్వంత పుంజ కథ కోసం చిత్రణలు కావచ్చు లేదా వారి కథకు కొత్త کردارాన్ని సృష్టించవచ్చు లేదా వారి ఆలోచనలు మరియు సూత్రాలు దృశ్యరూపంలో కనిపించడానికి సహాయపడవచ్చు.

ఉదాహరణగా, క్లాసులో స్మారక చిహ్నాలపై పని చేస్తుంటే Edu4All విద్యార్థులు సృష్టించగల చిత్రాలు:

![Edu4All స్టార్ట్‌అప్, క్లాస్ ఆన్ మోన్యుమెంట్లు, ఎఫిల్ టవర్](../../../translated_images/te/startup.94d6b79cc4bb3f5a.webp)

ఈ ప్రాంప్ట్ వలె ఉపయోగిస్తూ

> "ఎఫిల్ టవర్ పక్కన ఉదయపు సూర్యరశ్మిలో కుక్క"

## DALL-E మరియు Midjourney అంటే ఏమిటి?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) మరియు [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) రెండు అత్యంత ప్రాచుర్యం పొందిన చిత్ర జనరేషన్ మోడల్స్, ఇవి ప్రాంప్ట్‌లను ఉపయోగించి చిత్రాలను సృష్టించడానికి అనుమతిస్తాయి.

### DALL-E

DALL-Eతో ప్రారంభిద్దాం, ఇది ఒక జనరేటివ్ AI మోడల్, ఇది టెక్స్ట్ వివరణల నుండి చిత్రాలను సృష్టిస్తుంది.

> [DALL-E అనేది రెండు మోడల్స్, CLIP మరియు diffused attention కలయిక](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, ఒక మోడల్‌, ఇది చిత్రాలు మరియు టెక్స్ట్ నుంచి ఎంబెడ్డింగ్స్ (సంఖ్యాత్మక ప్రాతినిధ్యాలు) ఉత్పత్తి చేస్తుంది.

- **Diffused attention**, ఒక మోడల్‌, ఇది ఎంబెడ్డింగ్స్ నుంచి చిత్రాలను సృష్టిస్తుంది. DALL-E చిత్రాలు మరియు టెక్స్ట్ డేటాసెట్‌పై శిక్షణ పొందింది మరియు టెక్స్ట్ వివరణల నుండి చిత్రాల్ని సృష్టించడానికి ఉపయోగించవచ్చు. ఉదాహరణకి, DALL-E ఒక టోపీ తగిలిన పిల్లి లేదా మొహాక్ తో ఉన్న కుక్క చిత్రాన్ని సృష్టించవచ్చు.

### Midjourney

Midjourney DALL-E తో సారూప్యంగా పనిచేస్తుంది, ఇది టెక్స్ట్ ప్రాంప్ట్‌ల నుంచి చిత్రాలను సృష్టిస్తుంది. Midjourney కూడా "టోపీ తాగి ఉన్న పిల్లి" లేదా "మోహాక్ ఉన్న కుక్క" లాంటి ప్రాంప్ట్‌ల ఉపయోగించి చిత్రాలను సృష్టించవచ్చు.

![Midjourney ద్వారా సృష్టించిన చిత్రం, యాంత్రిక పావురం](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_చిత్ర క్రెడిట్ వికీపీడియా, Midjourney ద్వారా సృష్టించిన చిత్రం_

## DALL-E మరియు Midjourney ఎలా పని చేస్తాయి

మొదట, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ఒక జనరేటివ్ AI మోడల్, ఇది ట్రాన్స్‌ఫార్మర్ ఆर्कిటెక్చర్ ఆధారంగా ఉంటుంది, ఒక _ఆటోరిజ్రెసివ్ ట్రాన్స్‌ఫార్మర్_ తో.

ఒక _ఆటోరిజ్రెసివ్ ట్రాన్స్‌ఫార్మర్_ డిఫైన్ చేస్తుంది ఏ విధంగా ఒక మోడల్ టెక్స్ట్ వివరణల నుంచి చిత్రాలను సృష్టిస్తుందో, ఇది ఒక్కో పిక్సెల్ ని ఒక్క పుడుతి జనరేట్ చేస్తుంది, తర్వాత ఆ పిక్సెల్స్ ని ఉపయోగించి తదుపరి పిక్సెల్ ని సృష్టిస్తుంది. న్యూరల్ నెట్‌వర్క్ లో పలు లేయర్స్ ని దాటుకుంటూ, ఆఖరికి చిత్రం పూర్తవుతుంది.

ఈ ప్రక్రియతో DALL-E, ఇది సృష్టించే చిత్రంలో లక్షణాలు, వస్తువులు, విశేషణాలు ఇత్యాది నియంత్రిస్తుంది. అయినప్పటికీ, DALL-E 2 మరియు 3కి ఆ చిత్రంపై మరింత నియంత్రణ ఉంటుంది.

## మీ మొదటి చిత్ర జనరేషన్ అప్లికేషన్‌ను నిర్మించడం

మరి చిత్ర జనరేషన్ అప్లికేషన్ నిర్మించడానికి ఏం అవసరం? మీరు ఈ పైన లైబ్రరీలు అవసరం:

- **python-dotenv**, మీ సీక్రెట్లను కోడ్ నుంచి దూరంగా _.env_ ఫైల్‌లో ఉంచడానికి ఈ లైబ్రరీని ఉపయోగించటం చాలా మంచిది.
- **openai**, ఈ లైబ్రరీ OpenAI APIతో ఇంటరాక్ట్ చేయడానికి ఉపయోగపడుతుంది.
- **pillow**, Pythonలో చిత్రాలతో పని చేయడానికి.
- **requests**, HTTP అడుగులు చేయడానికి సహాయపడుతుంది.

## Azure OpenAI మోడల్‌ను సృష్టించి అమలు చేయండి

ఇంకా చేయని ఉంటే, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) పేజీపై సూచనలను అనుసరించండి
Azure OpenAI రిసోర్స్ మరియు మోడల్ సృష్టించడానికి. మోడల్‌గా **gpt-image-1**ను ఎంచుకోండి (ప్రస్తుత తరంగం Azure OpenAI చిత్ర మోడల్; DALL-E 3 పాతది మరియు కొత్త అమలులకు అందుబాటులో లేదు).

## యాప్ సృష్టించండి

1. ఈ కింది కంటెంట్‌తో _.env_ ఫైల్‌ను సృష్టించండి:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   ఈ సమాచారం Azure OpenAI Foundry పోర్టల్ లో మీ రిసోర్స్ "Deployments" విభాగంలో చూడవచ్చు.

1. పై లైబ్రరీలను _requirements.txt_ అనే ఫైల్‌లో సేకరించండి, ఇలా:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. తర్వాత, వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించి లైబ్రరీలను ఇన్స్టాల్ చేయండి:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows కోసం, క్రింది ఆదేశాలు ఉపయోగించి వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించండి మరియు క్రియాశీలం చేయండి:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ అనే ఫైల్‌లో ఈ క్రింది కోడ్ జత చేయండి:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # dotenv ను దిగుమతి చేయండి
    dotenv.load_dotenv()
    
    # Azure OpenAI సేవ క్లయింట్‌ను కాన్ఫిగర్ చేయండి
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # చిత్రాన్ని జనరేట్ చేయడానికి చిత్రం సృష్టింపు API ని ఉపయోగించండి
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # నిల్వ చేయబడిన చిత్రానికి డైరెక్టరీని సెట్ చేయండి
        image_dir = os.path.join(os.curdir, 'images')

        # డైరెక్టరీ లేనిపక్షంలో దాన్ని సృష్టించండి
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # చిత్రం మార్గాన్ని ప్రారంభించండి (ఫైల్ రకం png అవ్వాలి)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # సృష్టించబడిన చిత్రాన్ని పొందండి
        image_url = generation_response.data[0].url  # ప్రతిస్పందన నుండి చిత్రం URL ను తీయండి
        generated_image = requests.get(image_url).content  # చిత్రాన్ని డౌన్లోడ్ చేయండి
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # డిఫాల్ట్ చిత్రం వీయర్‌లో చిత్రాన్ని ప్రదర్శించండి
        image = Image.open(image_path)
        image.show()

    # తప్పిదాలను పట్టుకోండి
    except openai.BadRequestError as err:
        print(err)
   ```

ఈ కోడ్‌ను వివరించుదాం:

- ముందుగా, అవసరమైన లైబ్రరీలు తీసుకువచ్చాము, అందులో OpenAI లైబ్రరీ, dotenv లైబ్రరీ, requests లైబ్రరీ మరియు Pillow లైబ్రరీ ఉన్నాయి.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- తరువాత, _.env_ ఫైల్ నుండి ఎన్విరాన్‌మెంట్ వేరియబుల్స్‌ను లోడ్ చేస్తాము.

  ```python
  # dotenv ను దిగుమతి చేసుకోండి
  dotenv.load_dotenv()
  ```

- ఆ తర్వాత, Azure OpenAI సర్వీస్ క్లయింట్‌ను కాన్ఫిగర్ చేస్తున్నాము

  ```python
  # పరిసర చారల్లో నుండి ఎండ్పాయింట్ మరియు కీ ను పొందండి
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- తరువాత, చిత్రం సృష్టిస్తున్నాము:

  ```python
  # ఇమేజ్ జనరేషన్ API ఉపయోగించి ఒక చిత్రం సృష్టించండి
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  పై కోడ్ జవాబులో JSON ఆబ్జెక్ట్ రూపంలో సృష్టించిన చిత్ర URL ను ఇస్తుంది. ఆ URLని ఉపయోగించి చిత్రాన్ని డౌన్లోడ్ చేసి ఫైల్‌గా సేవ్ చేయవచ్చు.

- చివరగా, చిత్రాన్ని తెరుచుకుని సాధారణ చిత్ర వీవర్లో ప్రదర్శిస్తాము:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### చిత్రాన్ని సృష్టించే వివరాలను మరింతగా

చిత్రాన్ని సృష్టించే కోడ్ను మరింత వివరణగా చూడుదాం:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, చిత్రాన్ని సృష్టించడానికి ఉపయోగించే టెక్స్ట్ ప్రాంప్ట్. ఇక్కడ, మనం "లోలి‌పాప్ పట్టుకుని గుర్రంపై ఉన్న బన్నీ, మబ్బురమైన మైదానం మీద అక్కడ పూలు పెరుగుతున్నాయి" అన్న ప్రాంప్ట్ ఉపయోగిస్తున్నాం.
- **size**, సృష్టించబోయే చిత్ర పరిమాణం. ఈ సందర్భంలో, మనం 1024x1024 పిక్సెల్స్ పరిమాణంలో చిత్రాన్ని సృష్టిస్తున్నాం.
- **n**, సృష్టించబోయే చిత్రాల సంఖ్య. ఇక్కడ, మనం రెండు చిత్రాలను సృష్టిస్తున్నాం.
- **temperature**, ఒక పారామీటర్, ఇది జనరేటివ్ AI మోడల్ యొక్క అవుట్‌పుట్ రాండమ్నెస్‌ను నియంత్రిస్తుంది. టెంపరేచర్ 0 మరియు 1 మధ్య విలువ, 0 అంటే అవుట్‌పుట్ డిటర్మినిస్టిక్ మరియు 1 అంటే అరిఎండం అవుట్‌పుట్. డిఫాల్ట్ విలువ 0.7.

చిత్రాలతో మీరు చేయగల మరిన్ని పనులు తదుపరి సెక్షన్లో చూస్తాము.

## చిత్ర జనరేషన్ అదనపు సామర్థ్యాలు

ఇప్పుడు వరకు, మనం కొన్ని Python పంక్తులతో చిత్రాన్ని ఎలా సృష్టించవచ్చో చూసాము. అయినప్పటికీ, చిత్రాలతో మీరు చేయగల మరిన్ని పనులు ఉన్నాయి.

మీరు క్రింది విధంగా కూడా చేయవచ్చు:

- **మార్పులు చేయండి**. ఉన్న చిత్రానికి మాస్క్ మరియు ప్రాంప్ట్ ఇచ్చి, మీరు చిత్రాన్ని మార్చవచ్చు. ఉదాహరణకి, మన బన్నీ చిత్రంలో హ్యాట్ పెడతారు. మీరు ఈ పనిని చేయాలంటే, చిత్రం, మార్పుకు సంబంధించిన భాగాన్ని గుర్తించే మాస్క్ మరియు టెక్స్ట్ ప్రాంప్ట్ ఇవ్వాలి.
> గమనిక: ఇది DALL-E 3లో మద్దతు ఇవ్వబడలేదు. 
 
ఇక్కడ GPT Image ఉపయోగించి ఒక ఉదాహరణ ఉంది:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  బేసిక్ చిత్రం కేవలం లౌంజ్ మరియు స్విమ్మింగ్ పూల్ ఉంటే, చివరి చిత్రంలో ఫ్లామింగో ఉంటుంది:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/te/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/te/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/te/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **వేరియేషన్స్ సృష్టించండి**. మీరు ఉన్న చిత్రాన్ని తీసుకుని వేరియేషన్లు కావాలని అడగవచ్చు. వేరియేషన్ సృష్టించడానికి, మీరు చిత్రం మరియు టెక్స్ట్ ప్రాంప్ట్ ఇస్తారు, మరియు కింది కోడ్ వంటిది:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > గమనిక, ఇది OpenAI DALL-E 2 మోడల్‌లో మాత్రమే మద్దతు ఇస్తుంది, gpt-image-1 లో కాదు

## టెంపరేచర్

టెంపరేచర్ ఒక పారామీటర్, ఇది జనరేటివ్ AI మోడల్ అవుట్‌పుట్ రాండమ్నెస్ ను నియంత్రిస్తుంది. ఇది 0 మరియు 1 మధ్య విలువ, 0 అంటే అవుట్‌పుట్ నిర్దిష్టం (డిటర్మినిస్టిక్) మరియు 1 అంటే అవుట్‌పుట్ సరసమైనది (రాండమ్). డిఫాల్ట్ విలువ 0.7.

టెంపరేచర్ ఎలా పనిచేస్తుందో ఉదాహరణ చూసేందుకు, ఈ ప్రాంప్ట్‌ను రెండు సార్లు రన్ చేద్దాం:

> ప్రాంప్ట్ : "లోలి‌పాప్ పట్టుకుని గుర్రంపై ఉన్న బన్నీ, మబ్బురమైన మైదానం మీద అక్కడ పూలు పెరుగుతున్నాయి"

![లోలి‌పాప్ పట్టుకుని గుర్రంపై ఉన్న బన్నీ, సంచిక 1](../../../translated_images/te/v1-generated-image.a295cfcffa3c13c2.webp)

ఇప్పుడు అదే ప్రాంప్ట్ రెండుసార్లు చేయడం ద్వారా చిత్రాలు భిన్నంగా వస్తాయని చూద్దాం:

![గుర్రంపై ఉన్న బన్నీ చిత్రం](../../../translated_images/te/v2-generated-image.33f55a3714efe61d.webp)

చూడండి, చిత్రాలు సమానంగా ఉన్నప్పటికీ పూర్తిగా సరిగ్గా చేయబడలేదు. టెంపరేచర్ విలువను 0.1కి మార్చి చూడండి:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # ఇక్కడ మీ ప్రాంప్ట్ టెక్స్ట్‌ను నమోదు చేయండి
        size='1024x1024',
        n=2
    )
```

### టెంపరేచర్ మార్పు

కాబట్టి సమాధానం మరింత నిర్దిష్టంగా చేయడానికి ప్రయత్నిద్దాం. మనం సృష్టించిన రెండు చిత్రాలు చూస్తే, మొదటి చిత్రంలో బన్నీ ఉంది, రెండవ చిత్రంలో గుర్రం ఉంది, అందువల్ల చిత్రాలు అధికంగా భిన్నంగా ఉన్నాయి.

కాబట్టి మన కోడ్‌ను మార్చి టెంపరేచర్ విలువను 0 గా నిర్ధారిద్దాం, ఇలా:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # మీ ప్రాంప్ట్ టెక్స్ట్ ఇక్కడ ఎంటర్ చేయండి
        size='1024x1024',
        n=2,
        temperature=0
    )
```

ఈ కోడ్ నడిపినపుడు మీరు ఈ రెండు చిత్రాలను పొందుతారు:

- ![టెంపరేచర్ 0, సంచిక 1](../../../translated_images/te/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![టెంపరేచర్ 0 , సంచిక 2](../../../translated_images/te/v2-temp-generated-image.871d0c920dbfb0f1.webp)

ఇక్కడ స్పష్టంగా చిత్రాలు మరింత సమానంగా ఉంటాయని చూడవచ్చు.

## మీ అప్లికేషన్ కోసం మెటాప్రాంప్ట్‌లతో సరిహద్దులను ఎలా నిర్వచించేందుకు

మన డెమోలో ఇప్పటికే మనం కస్టమర్ల కోసం చిత్రాలను సృష్టించవచ్చు. అయితే, మన అప్లికేషన్‌కు కొన్ని సరిహద్దులు సృష్టించాలి.

ఉదాహరణకి, పనికి అనువైనది కాని లేదా పిల్లలకు అనుకూలం కాని చిత్రాలను సృష్టించకూడదు.

మనం దీన్ని _మెటాప్రాంప్ట్‌లు_తో చేయవచ్చు. మెటాప్రాంప్ట్‌లు జనరేటివ్ AI మోడల్ అవుట్‌పుట్‌ను నియంత్రించడానికి ఉపయోగించే టెక్స్ట్ ప్రాంప్ట్‌లు. ఉదాహరణకి, మేము మెటాప్రాంప్ట్‌లను ఉపయోగించి అవుట్‌పుట్‌ను నియంత్రించి, సృష్టించబడ్డ చిత్రాలు పనికి సరిపోయే లేదా పిల్లలకు అనుకూలంగా ఉండేలా చూసుకోవచ్చు.

### ఇది ఎలా పని చేస్తుంది?

ఇప్పుడు, మెటాప్రాంప్ట్‌లు ఎలా పని చేస్తాయో చూద్దాం.

మెటాప్రాంప్ట్‌లు జనరేటివ్ AI మోడల్ అవుట్‌పుట్ నియంత్రించడానికి ఉపయోగించే టెక్స్ట్ ప్రాంప్ట్‌లు, అవి ప్రధాన టెక్స్ట్ ప్రాంప్ట్ ముందు ఉంచబడతాయి, అవుట్‌పుట్‌ను నియంత్రించడానికి మరియు అప్లికేషన్లలో ప్రవేశపెట్టబడతాయి. ప్రధాన ప్రాంప్ట్ మరియు మెటా ప్రాంప్ట్‌ను ఒకే టెక్స్ట్ ప్రాంప్ట్‌లో జత చేస్తాయి.

మెటాప్రాంప్ట్ ఒక ఉదాహరణ:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

ఇప్పుడు, మన డెమోలో మెటాప్రాంప్ట్‌లను ఎలా ఉపయోగించవచ్చో చూద్దాం.

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

# TODO చిత్రం సృష్టించేందుకు అభ్యర్థనను జోడించాలి
```

పై ప్రాంప్ట్‌ ద్వారా సృష్టించబడే అన్ని చిత్రాలు మెటాప్రాంప్ట్‌ను పరిగణనలోకి తీసుకుంటాయనే విషయం మీరు గమనించవచ్చు.

## అసైన్‌మెంట్ - విద్యార్థులను సాధ్యపడిద్దాం

ఈ పాఠం ప్రారంభంలో మనం పరిచయమైన Edu4All ని మరింతగా అభివృద్ధి చేద్దాం. ఇప్పుడైనా విద్యార్థులు తమ అసెస్మెంట్ల కోసం చిత్రాలు సృష్టించగలరని సూత్రం.


విద్యార్థులు వారి మూల్యాంకనాలకు స్మారక చిహ్నాలను కలిగి ఉన్న చిత్రాలను సృష్టిస్తారు, స్మారక చిహ్నాలు ఏంటో నిర్ణయం విద్యార్థుల మీద ఉంటుంది. ఈ పనిలో విద్యార్థులు తమ సృజనాత్మకతను ఉపయోగించి ఈ స్మారక చిహ్నాలను వేర్వేరు సందర్భాలలో ఉంచమని అడిగారు.

## పరిష్కారం

ఒక సాధ్యమైన పరిష్కారం ఇక్కడ ఉంది:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# dotenv ను దిగుమతి చేసుకోండి
dotenv.load_dotenv()

# ఎండ్‌పాయింట్ మరియు కీని పర్యావరణ చరాలు నుంచి పొందండి
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
    # ఇమేజ్ జనరేషన్ API ఉపయోగించి చిత్రం రూపొందించండి
    generation_response = client.images.generate(
        prompt=prompt,    # ఇక్కడ మీ ప్రాంప్ట్ టెక్స్ట్ ఎంటర్ చేయండి
        size='1024x1024',
        n=1,
    )
    # నిల్వ చేసిన చిత్రానికి డైరెక్టరీని సెటప్ చేయండి
    image_dir = os.path.join(os.curdir, 'images')

    # డైరెక్టరీ లేకపోతే, దాన్ని సృష్టించండి
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # చిత్రం మార్గాన్ని ప్రారంభించండి (ఫైల్ టైప్ pngగా ఉండాలి గమనిక)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # రూపొందించిన చిత్రాన్ని పొందండి
    image_url = generation_response.data[0].url  # ప్రతిస్పందన నుండి చిత్రం URLను పొందండి
    generated_image = requests.get(image_url).content  # చిత్రాన్ని డౌన్లోడ్ చేయండి
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # డిఫాల్ట్ చిత్రం వీక్షణంలో చిత్రాన్ని ప్రదర్శించండి
    image = Image.open(image_path)
    image.show()

# తప్పిదాలను పట్టుకోండి
except openai.BadRequestError as err:
    print(err)
```

## అద్భుత పని! మీ అభ్యాసాన్ని కొనసాగించండి

ఈ పాఠాన్ని పూర్తిచేసిన తర్వాత, మా [జెనరేటివ్ ఏఐ లెర్నింగ్ సేకరణ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)ను చూడండి మరియు మీ జెనరేటివ్ ఏఐ జ్ఞానాన్ని ఇంకా పెంచుకోండి!

పదవిరోజు పాఠానికి వెళ్లండి, అక్కడ మేము [తక్కువ కోడ్‌తో ఏఐ అనువర్తనాలను ఎలా నిర్మించాలో](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) చూస్తాము

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->