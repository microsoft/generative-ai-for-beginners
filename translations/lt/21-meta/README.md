# Konstravimas su Meta šeimos modeliais 

## Įvadas 

Ši pamoka apims: 

- Dviejų pagrindinių Meta šeimos modelių tyrinėjimą - Llama 3.1 ir Llama 3.2, taip pat šiuo metu prieinamus alternatyvius modelius, naudojamus kodo pavyzdžiuose (Llama 3.3 ir Llama 4) 
- Kiekvieno modelio naudojimo atvejų ir scenarijų supratimą 
- Kodo pavyzdį, rodantį kiekvieno modelio unikalius bruožus 


## Meta šeimos modeliai 

Šioje pamokoje išnagrinėsime 2 modelius iš Meta šeimos arba "Llama Bandos" - Llama 3.1 ir Llama 3.2. Vykdomi kodo pavyzdžiai naudoja Llama 3.3 ir Llama 4, tai šiuo metu prieinami alternatyvūs modeliai Microsoft Foundry Models kataloge.

Šie modeliai yra įvairių variantų ir yra prieinami [Microsoft Foundry Models kataloge](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Pastaba:** GitHub Models bus nutrauktas 2026 m. liepos pabaigoje. Daugiau informacijos apie [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) naudojimą dirbant su AI modeliais rasite čia.

> **Pastaba:** Šioje pamokoje iš pradžių naudoti specifiniai modelių versijos (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) nuo tada buvo pašalinti iš Microsoft Foundry Models katalogo. Žemiau pateikti kodo pavyzdžiai naudoja `Llama-3.3-70B-Instruct` ir `Llama-4-Scout-17B-16E-Instruct` kaip šiuo metu prieinamus alternatyvius modelius Microsoft Foundry Models kataloge, tad jie vis dar veikia šiandien.

Modelių variantai (kaip iš pradžių aptarta šioje pamokoje): 
- Llama 3.1 - 70B Instruct (nutrauktas) 
- Llama 3.1 - 405B Instruct (nutrauktas) 
- Llama 3.2 - 11B Vision Instruct (nutrauktas) 
- Llama 3.2 - 90B Vision Instruct (nutrauktas) 

Šiuo metu prieinami alternatyvūs modeliai, naudojami kodo pavyzdžiuose: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Pastaba: Aukščiau aptarti Llama 3 variantai yra pateikti tik istoriniam kontekstui ir nebeprieinami Microsoft Foundry Models kataloge.*

## Llama 3.1 

Su 405 milijardais parametrų, Llama 3.1 priklauso atvirojo kodo LLM kategorijai. 

Modelis yra atnaujinimas ankstesnio leidimo Llama 3, siūlantis: 

- Didesnį konteksto langą – 128k žodžių prieš 8k žodžių 
- Didesnį maksimalų išvesties žodžių skaičių - 4096 prieš 2048 
- Geresnę daugiakalbę palaikymą – dėl didesnio mokymo žodžių kiekio 

Tai leidžia Llama 3.1 spręsti sudėtingesnius naudojimo atvejus kuriant GenAI programas, įskaitant: 
- Vietinį funkcijų kvietimą - galimybę kvieti išorinius įrankius ir funkcijas už LLM darbo srauto ribų
- Geresnį RAG našumą - dėl didesnio konteksto lango 
- Sintetinį duomenų generavimą - galimybę sukurti efektyvius duomenis tokiems užduotims kaip tobulinimas 

### Vietinis funkcijų kvietimas 

Llama 3.1 buvo specialiai išmokytas efektyviau kvieti funkcijas ar įrankius. Jame taip pat yra du įtaisytieji įrankiai, kuriuos modelis gali atpažinti kaip reikalingus naudoti pagal vartotojo pateiktą komandą. Šie įrankiai yra: 

- **Brave Search** - gali būti naudojamas gauti naujausią informaciją, pvz., orų, atliekant internetinę paiešką 
- **Wolfram Alpha** - gali būti naudojamas sudėtingesniems matematiniams skaičiavimams, tad nereikia rašyti savo funkcijų. 

Jūs taip pat galite sukurti savo pasirinktinius įrankius, kuriuos LLM gali kvieti. 

Žemiau pateiktame kodo pavyzdyje: 

- Mes apibrėžiame galimus įrankius (brave_search, wolfram_alpha) sistemos užklausoje. 
- Siunčiame vartotojo užklausą, klausiant apie orus tam tikrame mieste. 
- LLM atsakys įrankio kvietimu Brave Search įrankiui, kuris atrodys taip `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Pastaba: Šis pavyzdys tik sukuria įrankio kvietimą, jei norite gauti rezultatus, turėsite susikurti nemokamą paskyrą Brave API puslapyje ir apibrėžti funkciją patys.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2 

Nors tai yra LLM, viena Llama 3.1 trūkumų yra jos multimodalumo stoka. Tai reiškia, kad ji negali naudoti skirtingų įvesties tipų, tokių kaip paveikslėliai, kaip užklausas ir teikti atsakymus. Ši galimybė yra viena pagrindinių Llama 3.2 funkcijų. Šios funkcijos taip pat apima: 

- Multimodalumą - gebėjimą vertinti tiek tekstines, tiek paveikslėlių užklausas 
- Mažo ir vidutinio dydžio variacijas (11B ir 90B) - tai suteikia lanksčias diegimo galimybes, 
- Tik tekstui skirtus variantus (1B ir 3B) - tai leidžia modelį diegti kraštinėse/mobiliuose įrenginiuose ir suteikia mažą vėlavimą 

Multimodalumo palaikymas žymi didelį žingsnį atvirojo kodo modelių pasaulyje. Žemiau pateiktame kodo pavyzdyje naudojamos tiek paveikslėlio, tiek teksto užklausos, kad būtų gauta paveikslėlio analizė. Kadangi Llama 3.2 90B Vision Instruct buvo nutrauktas, pavyzdyje naudojamas `Llama-4-Scout-17B-16E-Instruct`, šiuo metu prieinamas natūraliai multimodalis alternatyva. 


### Multimodalumo palaikymas su Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## Mokymasis čia nesibaigia, tęskite kelionę

Baigę šią pamoką, peržiūrėkite mūsų [Generatyvios AI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau tobulintumėte savo žinias apie generatyviąją dirbtinį intelektą!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->