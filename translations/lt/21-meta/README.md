# Kūrimas su Meta šeimos modeliais 

## Įvadas 

Ši pamoka apims: 

- Dvejų pagrindinių Meta šeimos modelių - Llama 3.1 ir Llama 3.2 - tyrinėjimą 
- Kiekvieno modelio naudojimo atvejų ir scenarijų supratimą 
- Kodo pavyzdį, demonstruojantį kiekvieno modelio unikalių savybių panaudojimą 


## Meta šeimos modeliai 

Šioje pamokoje išnagrinėsime 2 modelius iš Meta šeimos arba „Llama Herd“ - Llama 3.1 ir Llama 3.2.

Šie modeliai yra įvairių variantų ir yra prieinami [Microsoft Foundry Models kataloge](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Pastaba:** GitHub Models bus uždaromas 2026 metų liepos pabaigoje. Čia rasite daugiau informacijos apie [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst), skirtų AI modelių prototipavimui.

Modelių variantai: 
- Llama 3.1 - 70B Instrukcija 
- Llama 3.1 - 405B Instrukcija 
- Llama 3.2 - 11B Vision Instrukcija 
- Llama 3.2 - 90B Vision Instrukcija 

*Pastaba: Llama 3 taip pat yra prieinamas Microsoft Foundry Models, bet ši pamoka jo neapims*

## Llama 3.1 

Turėdamas 405 milijardus parametrų, Llama 3.1 patenka į atviro kodo LLM kategoriją. 

Modelis yra ankstesnio Llama 3 leidimo atnaujinimas, siūlantis: 

- Didesnį konteksto langą - 128 tūkst. žetonų priešingai nei 8 tūkst. žetonų 
- Didesnį maksimalų išvesties žetonų skaičių - 4096 prieš 2048 
- Geresnę daugiakalbę paramą - dėl padidėjusio treniravimo žetonų skaičiaus 

Tai leidžia Llama 3.1 tvarkyti sudėtingesnius naudojimo atvejus, kuriant GenAI programas, įskaitant: 
- Vietinį funkcijų kvietimą - galimybę kviesti išorinius įrankius ir funkcijas už LLM darbo eigos ribų
- Geresnį RAG veikimą - dėl didesnio konteksto lango 
- Sintetinį duomenų generavimą - galimybę kurti efektyvius duomenis užduotims, tokioms kaip tobulinimas 

### Vietinis funkcijų kvietimas 

Llama 3.1 buvo tobulinamas, kad efektyviau atliktų funkcijų ar įrankių kvietimus. Taip pat turi du įmontuotus įrankius, kuriuos modelis gali atpažinti kaip reikalingus naudoti pagal vartotojo užklausą. Šie įrankiai yra: 

- **Brave Search** - galima naudoti norint gauti aktualią informaciją, pavyzdžiui, orą atliekant interneto paiešką 
- **Wolfram Alpha** - galima naudoti sudėtingesniems matematikos skaičiavimams, todėl nereikia rašyti savo funkcijų. 

Taip pat galite sukurti savo individualius įrankius, kuriuos LLM gali kviesti. 

Žemiau pateiktame kodo pavyzdyje: 

- Sistemos užklausoje apibrėžiame prieinamus įrankius (brave_search, wolfram_alpha). 
- Išsiunčiame vartotojo užklausą, kuri klausia apie orą tam tikrame mieste. 
- LLM atsakys įrankio kvietimu į Brave Search įrankį, kuris atrodys taip `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Pastaba: šis pavyzdys tik atlieka įrankio kvietimą, jei norite gauti rezultatus, turėsite sukurti nemokamą paskyrą Brave API puslapyje ir apibrėžti pačią funkciją.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Gaukite juos iš savo Microsoft Foundry projekto puslapio „Apžvalga“
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

Nors Llama 3.1 yra LLM, vienas iš jos trūkumų yra multimodalumo stoka. Tai reiškia, kad ji negali naudoti skirtingų įvesties tipų, tokių kaip vaizdai kaip užklausos, ir teikti atsakymus. Ši galimybė yra viena pagrindinių Llama 3.2 funkcijų. Šios funkcijos taip pat apima: 

- Multimodalumą - gebėjimą vertinti tiek teksto, tiek vaizdų užklausas 
- Mažų ir vidutinių dydžių variantai (11B ir 90B) - tai suteikia lankstumo diegimo galimybėms, 
- Tik tekstiniai variantai (1B ir 3B) - leidžia modelį diegti krašte / mobiliuosiuose įrenginiuose ir suteikia mažą delsą 

Multimodalinė parama yra didelis žingsnis atvirojo kodo modelių pasaulyje. Žemiau pateiktas kodo pavyzdys priima tiek vaizdą, tiek teksto užklausą, norint gauti Llama 3.2 90B vaizdo analizę. 


### Multimodalinė parama su Llama 3.2

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

# Gautus iš savo Microsoft Foundry projekto „Apžvalgos“ puslapio
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Llama-3.2-90B-Vision-Instruct"

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

Baigę šią pamoką, apsilankykite mūsų [Generatyvios AI mokymosi kolekcijoje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau keltumėte savo žinias apie Generatyviąją AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->