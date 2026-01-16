<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-12-19T20:41:03+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "te"
}
-->
# చిత్రం సృష్టి అనువర్తనాలు నిర్మించడం

[![చిత్రం సృష్టి అనువర్తనాలు నిర్మించడం](../../../translated_images/te/09-lesson-banner.906e408c741f4411.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMs కేవలం టెక్స్ట్ ఉత్పత్తికి మాత్రమే కాదు. టెక్స్ట్ వివరణల నుండి చిత్రాలను కూడా సృష్టించవచ్చు. చిత్రాలను ఒక మోడ్‌గా కలిగి ఉండటం మెడటెక్, వాస్తుశిల్పం, పర్యాటకం, గేమ్ అభివృద్ధి మరియు మరెన్నో ప్రాంతాలలో చాలా ఉపయోగకరంగా ఉంటుంది. ఈ అధ్యాయంలో, రెండు అత్యంత ప్రాచుర్యం పొందిన చిత్రం సృష్టి మోడల్స్, DALL-E మరియు Midjourney గురించి తెలుసుకుందాం.

## పరిచయం

ఈ పాఠంలో, మనం కవర్ చేయబోతున్నవి:

- చిత్రం సృష్టి మరియు అది ఎందుకు ఉపయోగకరమో.
- DALL-E మరియు Midjourney, అవి ఏమిటి, మరియు అవి ఎలా పనిచేస్తాయి.
- మీరు ఎలా చిత్రం సృష్టి అనువర్తనం నిర్మించవచ్చు.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం పూర్తి చేసిన తర్వాత, మీరు చేయగలుగుతారు:

- చిత్రం సృష్టి అనువర్తనం నిర్మించడం.
- మీ అనువర్తనానికి మెటా ప్రాంప్ట్‌లతో సరిహద్దులను నిర్వచించడం.
- DALL-E మరియు Midjourney తో పని చేయడం.

## చిత్రం సృష్టి అనువర్తనం ఎందుకు నిర్మించాలి?

చిత్రం సృష్టి అనువర్తనాలు జనరేటివ్ AI సామర్థ్యాలను అన్వేషించడానికి అద్భుతమైన మార్గం. అవి, ఉదాహరణకు:

- **చిత్ర సవరణ మరియు సంశ్లేషణ**. మీరు వివిధ ఉపయోగాల కోసం చిత్రాలను సృష్టించవచ్చు, ఉదాహరణకు చిత్రం సవరణ మరియు చిత్రం సంశ్లేషణ.

- **వివిధ పరిశ్రమలకు వర్తించు**. అవి మెడటెక్, పర్యాటకం, గేమ్ అభివృద్ధి వంటి వివిధ పరిశ్రమలకు చిత్రాలను సృష్టించడానికి కూడా ఉపయోగించవచ్చు.

## సన్నివేశం: Edu4All

ఈ పాఠంలో భాగంగా, మనం Edu4All అనే స్టార్టప్‌తో కొనసాగుతాము. విద్యార్థులు తమ అసెస్మెంట్ల కోసం చిత్రాలను సృష్టిస్తారు, ఏ చిత్రాలు కావాలో విద్యార్థులపై ఆధారపడి ఉంటుంది, కానీ అవి తమ స్వంత కథ కోసం చిత్రాలు కావచ్చు లేదా తమ కథకు కొత్త పాత్రను సృష్టించవచ్చు లేదా తమ ఆలోచనలు మరియు భావనలను దృశ్యరూపంలో చూపించడంలో సహాయపడవచ్చు.

క్లాస్‌లో స్మారక చిహ్నాలపై పని చేస్తున్నప్పుడు Edu4All విద్యార్థులు ఉదాహరణకు సృష్టించగలిగే చిత్రాలు ఇక్కడ ఉన్నాయి:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/te/startup.94d6b79cc4bb3f5a.png)

ఈ ప్రాంప్ట్ ఉపయోగించి

> "ప్రారంభ ఉదయం సూర్యకాంతిలో ఎఫిల్ టవర్ పక్కన కుక్క"

## DALL-E మరియు Midjourney అంటే ఏమిటి?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) మరియు [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) రెండు అత్యంత ప్రాచుర్యం పొందిన చిత్రం సృష్టి మోడల్స్, ఇవి ప్రాంప్ట్‌లను ఉపయోగించి చిత్రాలను సృష్టించడానికి అనుమతిస్తాయి.

### DALL-E

ముందుగా DALL-E తో ప్రారంభిద్దాం, ఇది టెక్స్ట్ వివరణల నుండి చిత్రాలను సృష్టించే జనరేటివ్ AI మోడల్.

> [DALL-E అనేది రెండు మోడల్స్, CLIP మరియు diffused attention కలయిక](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, చిత్రాలు మరియు టెక్స్ట్ నుండి డేటా యొక్క సంఖ్యాత్మక ప్రాతినిధ్యాలు అయిన ఎంబెడ్డింగ్స్‌ను సృష్టించే మోడల్.

- **Diffused attention**, ఎంబెడ్డింగ్స్ నుండి చిత్రాలను సృష్టించే మోడల్. DALL-E చిత్రాలు మరియు టెక్స్ట్ డేటాసెట్‌పై శిక్షణ పొందింది మరియు టెక్స్ట్ వివరణల నుండి చిత్రాలను సృష్టించడానికి ఉపయోగించవచ్చు. ఉదాహరణకు, DALL-E టోపీ వేసుకున్న పిల్లి లేదా మొహాక్ ఉన్న కుక్క చిత్రాలను సృష్టించవచ్చు.

### Midjourney

Midjourney DALL-E లాగా పనిచేస్తుంది, ఇది టెక్స్ట్ ప్రాంప్ట్‌ల నుండి చిత్రాలను సృష్టిస్తుంది. Midjourney కూడా “టోపీ వేసుకున్న పిల్లి” లేదా “మోహాక్ ఉన్న కుక్క” వంటి ప్రాంప్ట్‌లను ఉపయోగించి చిత్రాలను సృష్టించవచ్చు.

![Midjourney ద్వారా సృష్టించబడిన చిత్రం, యాంత్రిక పావురం](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_చిత్ర క్రెడిట్ వికీపీడియా, Midjourney ద్వారా సృష్టించబడిన చిత్రం_

## DALL-E మరియు Midjourney ఎలా పనిచేస్తాయి

ముందుగా, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E అనేది ట్రాన్స్‌ఫార్మర్ ఆర్కిటెక్చర్ ఆధారిత జనరేటివ్ AI మోడల్, ఇది _ఆటోరెగ్రెసివ్ ట్రాన్స్‌ఫార్మర్_.

ఒక _ఆటోరెగ్రెసివ్ ట్రాన్స్‌ఫార్మర్_ మోడల్ టెక్స్ట్ వివరణల నుండి చిత్రాలను ఎలా సృష్టిస్తుందో నిర్వచిస్తుంది, ఇది ఒక్కో పిక్సెల్‌ను ఒకేసారి సృష్టించి, ఆ పిక్సెల్‌లను ఉపయోగించి తదుపరి పిక్సెల్‌ను సృష్టిస్తుంది. న్యూరల్ నెట్‌వర్క్‌లో అనేక లేయర్ల ద్వారా పాస్ అవుతుంది, చివరికి చిత్రం పూర్తవుతుంది.

ఈ ప్రక్రియతో, DALL-E సృష్టించే చిత్రంలో లక్షణాలు, వస్తువులు, లక్షణాలు మరియు మరెన్నో నియంత్రిస్తుంది. అయితే, DALL-E 2 మరియు 3 సృష్టించిన చిత్రంపై మరింత నియంత్రణ కలిగి ఉంటాయి.

## మీ మొదటి చిత్రం సృష్టి అనువర్తనం నిర్మించడం

అప్పుడు చిత్రం సృష్టి అనువర్తనం నిర్మించడానికి ఏమి అవసరం? మీరు ఈ క్రింది లైబ్రరీలను అవసరం:

- **python-dotenv**, మీ రహస్యాలను కోడ్ నుండి దూరంగా _.env_ ఫైల్‌లో ఉంచడానికి ఈ లైబ్రరీని ఉపయోగించడం చాలా సిఫార్సు చేయబడింది.
- **openai**, ఈ లైబ్రరీని మీరు OpenAI APIతో ఇంటరాక్ట్ చేయడానికి ఉపయోగిస్తారు.
- **pillow**, Pythonలో చిత్రాలతో పని చేయడానికి.
- **requests**, HTTP అభ్యర్థనలు చేయడానికి సహాయపడుతుంది.

## Azure OpenAI మోడల్ సృష్టించి డిప్లాయ్ చేయండి

ఇప్పటికే చేయకపోతే, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) పేజీలోని సూచనలను అనుసరించి Azure OpenAI వనరును మరియు మోడల్‌ను సృష్టించండి. మోడల్‌గా DALL-E 3 ఎంచుకోండి.

## అనువర్తనం సృష్టించండి

1. క్రింది కంటెంట్‌తో _.env_ ఫైల్ సృష్టించండి:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   ఈ సమాచారాన్ని Azure OpenAI Foundry పోర్టల్‌లో మీ వనరు "Deployments" విభాగంలో కనుగొనండి.

1. పై లైబ్రరీలను _requirements.txt_ అనే ఫైల్‌లో సేకరించండి:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. తరువాత, వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించి లైబ్రరీలను ఇన్‌స్టాల్ చేయండి:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows కోసం, వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించి యాక్టివేట్ చేయడానికి క్రింది కమాండ్లను ఉపయోగించండి:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ అనే ఫైల్‌లో క్రింది కోడ్ జోడించండి:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # dotenv ను దిగుమతి చేసుకోండి
    dotenv.load_dotenv()
    
    # Azure OpenAI సేవ క్లయింట్‌ను కాన్ఫిగర్ చేయండి
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # ఇమేజ్ జనరేషన్ API ఉపయోగించి చిత్రం సృష్టించండి
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # నిల్వ చేయబడిన చిత్రానికి డైరెక్టరీని సెట్ చేయండి
        image_dir = os.path.join(os.curdir, 'images')

        # డైరెక్టరీ లేకపోతే, దాన్ని సృష్టించండి
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # చిత్రం మార్గాన్ని ప్రారంభించండి (ఫైల్ రకం png కావాలి)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # సృష్టించబడిన చిత్రాన్ని పొందండి
        image_url = generation_response.data[0].url  # ప్రతిస్పందన నుండి చిత్రం URL ను తీసుకోండి
        generated_image = requests.get(image_url).content  # చిత్రాన్ని డౌన్లోడ్ చేయండి
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # డిఫాల్ట్ చిత్రం వీక్షకంలో చిత్రాన్ని ప్రదర్శించండి
        image = Image.open(image_path)
        image.show()

    # తప్పిదాలను పట్టుకోండి
    except openai.InvalidRequestError as err:
        print(err)
   ```

ఈ కోడ్‌ను వివరించుకుందాం:

- మొదట, మనం అవసరమైన లైబ్రరీలను దిగుమతి చేసుకుంటాము, అందులో OpenAI లైబ్రరీ, dotenv లైబ్రరీ, requests లైబ్రరీ, మరియు Pillow లైబ్రరీ ఉన్నాయి.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- తరువాత, _.env_ ఫైల్ నుండి ఎన్విరాన్‌మెంట్ వేరియబుల్స్‌ను లోడ్ చేస్తాము.

  ```python
  # డాట్‌ఎన్‌వి ని దిగుమతి చేసుకోండి
  dotenv.load_dotenv()
  ```

- ఆ తర్వాత, Azure OpenAI సర్వీస్ క్లయింట్‌ను కాన్ఫిగర్ చేస్తాము

  ```python
  # ఎండ్పాయింట్ మరియు కీని పర్యావరణ చరాలు నుండి పొందండి
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- తరువాత, చిత్రం సృష్టిస్తాము:

  ```python
  # ఇమేజ్ జనరేషన్ API ఉపయోగించి ఒక చిత్రం సృష్టించండి
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  పై కోడ్ సృష్టించిన చిత్ర URL కలిగిన JSON ఆబ్జెక్ట్‌తో స్పందిస్తుంది. ఆ URL ఉపయోగించి చిత్రాన్ని డౌన్లోడ్ చేసి ఫైల్‌గా సేవ్ చేయవచ్చు.

- చివరగా, చిత్రాన్ని తెరిచి సాధారణ చిత్రం వీక్షకుడిని ఉపయోగించి ప్రదర్శిస్తాము:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### చిత్రాన్ని సృష్టించే కోడ్ గురించి మరిన్ని వివరాలు

చిత్రాన్ని సృష్టించే కోడ్‌ను మరింత వివరంగా చూద్దాం:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, చిత్రం సృష్టించడానికి ఉపయోగించే టెక్స్ట్ ప్రాంప్ట్. ఈ సందర్భంలో, "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils" అనే ప్రాంప్ట్ ఉపయోగిస్తున్నాము.
- **size**, సృష్టించబడే చిత్ర పరిమాణం. ఈ సందర్భంలో, 1024x1024 పిక్సెల్స్ పరిమాణంలో చిత్రం సృష్టిస్తున్నాము.
- **n**, సృష్టించబడే చిత్రాల సంఖ్య. ఈ సందర్భంలో, రెండు చిత్రాలు సృష్టిస్తున్నాము.
- **temperature**, జనరేటివ్ AI మోడల్ అవుట్పుట్ యొక్క యాదృచ్ఛికతను నియంత్రించే పారామీటర్. టెంపరేచర్ 0 నుండి 1 మధ్య విలువ, 0 అంటే అవుట్పుట్ నిర్దిష్టంగా ఉంటుంది, 1 అంటే అవుట్పుట్ యాదృచ్ఛికంగా ఉంటుంది. డిఫాల్ట్ విలువ 0.7.

మరిన్ని చిత్రాలతో మీరు చేయగలిగే విషయాలను తదుపరి విభాగంలో కవర్ చేస్తాము.

## చిత్రం సృష్టి అదనపు సామర్థ్యాలు

ఇప్పటివరకు మనం Pythonలో కొన్ని లైన్లతో చిత్రం సృష్టించగలిగిన విధానం చూశాం. అయితే, చిత్రాలతో మరిన్ని పనులు చేయవచ్చు.

మీరు క్రింది పనులు కూడా చేయవచ్చు:

- **సవరణలు చేయండి**. ఇప్పటికే ఉన్న చిత్రానికి మాస్క్ మరియు ప్రాంప్ట్ ఇవ్వడం ద్వారా, మీరు చిత్రాన్ని మార్చవచ్చు. ఉదాహరణకు, చిత్రంలోని ఒక భాగానికి ఏదైనా జోడించవచ్చు. మన బన్నీ చిత్రాన్ని ఊహించండి, బన్నీకి టోపీ జోడించవచ్చు. మీరు ఎలా చేస్తారు అంటే, చిత్రం, మాస్క్ (మార్పు చేయవలసిన ప్రాంతాన్ని గుర్తించే) మరియు టెక్స్ట్ ప్రాంప్ట్ ఇవ్వడం ద్వారా.  
> గమనిక: ఇది DALL-E 3లో మద్దతు లేదు.

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

  ప్రాథమిక చిత్రం కేవలం పూల్ ఉన్న లౌంజ్ మాత్రమే ఉంటుంది కానీ తుది చిత్రంలో ఫ్లామింగో ఉంటుంది:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/te/sunlit_lounge.a75a0cb61749db0e.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/te/mask.1b2976ccec9e011e.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/te/sunlit_lounge_result.76ae02957c0bbeb8.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **వేరియేషన్లు సృష్టించండి**. మీరు ఇప్పటికే ఉన్న చిత్రాన్ని తీసుకుని వేరియేషన్లు సృష్టించాలని అడగవచ్చు. వేరియేషన్ సృష్టించడానికి, మీరు చిత్రం మరియు టెక్స్ట్ ప్రాంప్ట్ ఇస్తారు, మరియు క్రింది కోడ్ వంటిది ఉపయోగిస్తారు:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > గమనిక, ఇది కేవలం OpenAIలో మద్దతు పొందింది

## టెంపరేచర్

టెంపరేచర్ అనేది జనరేటివ్ AI మోడల్ అవుట్పుట్ యొక్క యాదృచ్ఛికతను నియంత్రించే పారామీటర్. టెంపరేచర్ 0 నుండి 1 మధ్య విలువ, 0 అంటే అవుట్పుట్ నిర్దిష్టంగా ఉంటుంది, 1 అంటే అవుట్పుట్ యాదృచ్ఛికంగా ఉంటుంది. డిఫాల్ట్ విలువ 0.7.

టెంపరేచర్ ఎలా పనిచేస్తుందో ఒక ఉదాహరణ చూద్దాం, ఈ ప్రాంప్ట్‌ను రెండు సార్లు నడిపించడం ద్వారా:

> ప్రాంప్ట్ : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![గాడిదపై బన్నీ, వెర్షన్ 1](../../../translated_images/te/v1-generated-image.a295cfcffa3c13c2.png)

ఇప్పుడు అదే ప్రాంప్ట్‌ను మరోసారి నడిపించి, రెండు సార్లు అదే చిత్రం రాదు అని చూద్దాం:

![గాడిదపై బన్నీ చిత్రం](../../../translated_images/te/v2-generated-image.33f55a3714efe61d.png)

మీరు చూడగలిగినట్లుగా, చిత్రాలు సమానంగా ఉన్నా, ఒకేలా లేవు. ఇప్పుడు టెంపరేచర్ విలువను 0.1కి మార్చి చూద్దాం:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # మీ ప్రాంప్ట్ టెక్స్ట్ ఇక్కడ నమోదు చేయండి
        size='1024x1024',
        n=2
    )
```

### టెంపరేచర్ మార్చడం

కాబట్టి ప్రతిస్పందన మరింత నిర్దిష్టంగా ఉండేలా ప్రయత్నిద్దాం. మనం సృష్టించిన రెండు చిత్రాల నుండి గమనించవచ్చు, మొదటి చిత్రంలో బన్నీ ఉంది, రెండవ చిత్రంలో గాడిద ఉంది, కాబట్టి చిత్రాలు చాలా భిన్నంగా ఉన్నాయి.

అందువల్ల మన కోడ్ మార్చి టెంపరేచర్‌ను 0గా సెట్ చేద్దాం:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # ఇక్కడ మీ ప్రాంప్ట్ టెక్స్ట్‌ను నమోదు చేయండి
        size='1024x1024',
        n=2,
        temperature=0
    )
```

ఇప్పుడు మీరు ఈ కోడ్ నడిపినప్పుడు, ఈ రెండు చిత్రాలు వస్తాయి:

- ![టెంపరేచర్ 0, వి1](../../../translated_images/te/v1-temp-generated-image.a4346e1d2360a056.png)
- ![టెంపరేచర్ 0, వి2](../../../translated_images/te/v2-temp-generated-image.871d0c920dbfb0f1.png)

ఇక్కడ మీరు స్పష్టంగా చూడవచ్చు, చిత్రాలు ఒకదానితో మరింత సమానంగా ఉన్నాయని.

## మీ అనువర్తనానికి సరిహద్దులను మెటాప్రాంప్ట్‌లతో ఎలా నిర్వచించాలి

మన డెమోతో, మనం ఇప్పటికే క్లయింట్ల కోసం చిత్రాలను సృష్టించగలుగుతున్నాము. అయితే, మన అనువర్తనానికి కొన్ని సరిహద్దులను సృష్టించాలి.

ఉదాహరణకు, పని కోసం సురక్షితంగా లేని లేదా పిల్లలకి అనుకూలంగా లేని చిత్రాలను సృష్టించకూడదు.

ఇది _మెటాప్రాంప్ట్‌లు_ తో చేయవచ్చు. మెటాప్రాంప్ట్‌లు జనరేటివ్ AI మోడల్ అవుట్పుట్‌ను నియంత్రించడానికి ఉపయోగించే టెక్స్ట్ ప్రాంప్ట్‌లు. ఉదాహరణకు, అవుట్పుట్‌ను నియంత్రించడానికి మరియు సృష్టించబడిన చిత్రాలు పని కోసం సురక్షితంగా లేదా పిల్లలకి అనుకూలంగా ఉండేలా నిర్ధారించడానికి మెటాప్రాంప్ట్‌లను ఉపయోగించవచ్చు.

### ఇది ఎలా పనిచేస్తుంది?

ఇప్పుడు, మెటాప్రాంప్ట్‌లు ఎలా పనిచేస్తాయి?

మెటాప్రాంప్ట్‌లు జనరేటివ్ AI మోడల్ అవుట్పుట్‌ను నియంత్రించడానికి ఉపయోగించే టెక్స్ట్ ప్రాంప్ట్‌లు, ఇవి టెక్స్ట్ ప్రాంప్ట్ ముందు ఉంచబడతాయి, మరియు మోడల్ అవుట్పుట్‌ను నియంత్రించడానికి ఉపయోగిస్తారు మరియు అనువర్తనాల్లో మోడల్ అవుట్పుట్‌ను నియంత్రించడానికి ఎంబెడ్ చేయబడతాయి. ప్రాంప్ట్ ఇన్‌పుట్ మరియు మెటాప్రాంప్ట్ ఇన్‌పుట్‌ను ఒకే టెక్స్ట్ ప్రాంప్ట్‌లో కప్పివేస్తాయి.

మెటాప్రాంప్ట్ యొక్క ఒక ఉదాహరణ క్రింది విధంగా ఉంటుంది:

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

# TODO చిత్రం సృష్టించడానికి అభ్యర్థన జోడించండి
```

పై ప్రాంప్ట్ నుండి, మీరు సృష్టించబడుతున్న అన్ని చిత్రాలు మెటాప్రాంప్ట్‌ను పరిగణలోకి తీసుకుంటున్నాయని చూడవచ్చు.

## అసైన్‌మెంట్ - విద్యార్థులను సక్రియం చేద్దాం

ఈ పాఠం ప్రారంభంలో Edu4All ను పరిచయం చేసాము. ఇప్పుడు విద్యార్థులు తమ అసెస్మెంట్ల కోసం చిత్రాలను సృష్టించగలిగేలా చేయాల్సిన సమయం వచ్చింది.

విద్యార్థులు తమ అసెస్మెంట్ల కోసం స్మారక చిహ్నాలు కలిగిన చిత్రాలను సృష్టిస్తారు, ఏ స్మారక చిహ్నాలు కావాలో విద్యార్థులపై ఆధారపడి ఉంటుంది. విద్యార్థులు ఈ పనిలో తమ సృజనాత్మకతను ఉపయోగించి ఈ స్మారక చిహ్నాలను వివిధ సందర్భాలలో ఉంచాలని అడుగుతారు.

## పరిష్కారం

ఇది ఒక సాధ్యమైన పరిష్కారం:
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# dotenv ను దిగుమతి చేసుకోండి
dotenv.load_dotenv()

# ఎండ్పాయింట్ మరియు కీని వాతావరణ చరాలు నుండి పొందండి
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
    # ఇమేజ్ జనరేషన్ API ఉపయోగించి ఒక చిత్రం సృష్టించండి
    generation_response = client.images.generate(
        prompt=prompt,    # మీ ప్రాంప్ట్ టెక్స్ట్ ఇక్కడ నమోదు చేయండి
        size='1024x1024',
        n=1,
    )
    # నిల్వ చేయబడిన చిత్రానికి డైరెక్టరీని సెట్ చేయండి
    image_dir = os.path.join(os.curdir, 'images')

    # డైరెక్టరీ లేకపోతే, దాన్ని సృష్టించండి
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # చిత్రం మార్గాన్ని ప్రారంభించండి (ఫైల్ టైపు png కావాలి)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # సృష్టించబడిన చిత్రాన్ని పొందండి
    image_url = generation_response.data[0].url  # ప్రతిస్పందన నుండి చిత్రం URL ను తీసుకోండి
    generated_image = requests.get(image_url).content  # చిత్రాన్ని డౌన్లోడ్ చేయండి
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # డిఫాల్ట్ చిత్రం వీక్షకంలో చిత్రాన్ని ప్రదర్శించండి
    image = Image.open(image_path)
    image.show()

# తప్పిదాలను పట్టుకోండి
except openai.BadRequestError as err:
    print(err)
```

## అద్భుతమైన పని! మీ అభ్యాసాన్ని కొనసాగించండి

ఈ పాఠం పూర్తి చేసిన తర్వాత, మా [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ను పరిశీలించి మీ Generative AI జ్ఞానాన్ని మరింత పెంచుకోండి!

పాఠం 10 కి వెళ్లండి, అక్కడ మేము [తక్కువ కోడ్‌తో AI అనువర్తనాలను ఎలా నిర్మించాలో](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) చూడబోతున్నాము.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->