# Kūrimas su Meta šeimos modeliais 

## Įvadas 

Ši pamoka apims: 

- Du pagrindinius Meta šeimos modelius – Llama 3.1 ir Llama 3.2 
- Supratimą apie kiekvieno modelio panaudojimo atvejus ir scenarijus 
- Kodo pavyzdį, parodantį kiekvieno modelio unikalius bruožus 


## Meta šeimos modeliai 

Šioje pamokoje nagrinėsime 2 modelius iš Meta šeimos arba „Llama Herd“ – Llama 3.1 ir Llama 3.2.

Šie modeliai yra įvairių variantų ir yra prieinami [Microsoft Foundry Models kataloge](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Pastaba:** GitHub Models bus nutrauktas 2026 m. liepos pabaigoje. Daugiau informacijos apie [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) naudojimą AI modelių prototipavimui rasite čia.

Modelių variantai: 
- Llama 3.1 – 70B Instruct 
- Llama 3.1 – 405B Instruct 
- Llama 3.2 – 11B Vision Instruct 
- Llama 3.2 – 90B Vision Instruct 

*Pastaba: Llama 3 taip pat yra Microsoft Foundry Models kataloge, tačiau ši pamoka jo neapims*

## Llama 3.1 

Turint 405 milijardus parametrų, Llama 3.1 patenka į atvirojo kodo LLM kategoriją. 

Modelis yra ankstesnio Llama 3 leidimo atnaujinimas, siūlantis: 

- Didesnį konteksto langą – 128 tūkst. žetonų prieš 8 tūkst. žetonų 
- Didesnį Maksimalų Išvesties Žetonų skaičių – 4096 prieš 2048 
- Geresnę daugiakalbę palaikymą – dėl padidinto mokymo žetonų kiekio 

Tai leidžia Llama 3.1 spręsti sudėtingesnius panaudojimo atvejus kuriant GenAI programas, įskaitant: 
- Vietinį funkcijų kvietimą – galimybę iškviesti išorines priemones ir funkcijas už LLM darbo eigą 
- Geresnį RAG našumą – dėl didesnio konteksto lango 
- Sintetinį duomenų generavimą – galimybę kurti efektyvius duomenis tokioms užduotims kaip tobulinimas 

### Vietinis funkcijų kvietimas 

Llama 3.1 buvo tobulinamas, kad veiksmingiau atliktų funkcijų ar priemonių kvietimus. Jis taip pat turi dvi integruotas priemones, kurias modelis gali atpažinti, kad reikia naudoti pagal vartotojo užklausą. Šios priemonės yra: 

- **Brave Search** – gali būti naudojama norint gauti naujausią informaciją, pvz., orų prognozę, atliekant interneto paiešką 
- **Wolfram Alpha** – gali būti naudojama sudėtingesniems matematiniams skaičiavimams, todėl nereikia rašyti savo funkcijų. 

Taip pat galite sukurti savo pasirinktas priemones, kurias LLM gali iškviesti. 

Žemiau pateiktame kodo pavyzdyje: 

- Apibrėžiame prieinamas priemones (brave_search, wolfram_alpha) sistemos užklausoje. 
- Išsiunčiame vartotojo užklausą, kuri klausia apie orą tam tikrame mieste. 
- LLM atsakys naudodamas funkcijos kvietimą į Brave Search priemonę, kuris atrodys taip `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Pastaba: šis pavyzdys tik atlieka funkcijos kvietimą, jei norite gauti rezultatus, turėsite sukurti nemokamą paskyrą Brave API puslapyje ir apibrėžti funkciją patys.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Gaukite juos iš savo Microsoft Foundry projekto „Apžvalgos“ puslapio
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

Nors Llama 3.1 yra LLM, viena iš jo ribotumų yra multimodališkumo trūkumas. Tai reiškia, kad negalima naudoti skirtingų įvesties tipų, tokių kaip vaizdai, kaip užklausos ir pateikti atsakymus. Ši galimybė yra viena pagrindinių Llama 3.2 funkcijų. Šios funkcijos taip pat apima: 

- Multimodališkumą – gebėjimą įvertinti tiek teksto, tiek vaizdų užklausas 
- Mažo ir vidutinio dydžio variantus (11B ir 90B) – tai suteikia lankstumo diegimo galimybes, 
- Tik teksto variantus (1B ir 3B) – tai leidžia modelį diegti periferiniuose / mobiliuosiuose įrenginiuose ir užtikrina mažą vėlavimą 

Multimodalinė parama reiškia didelį žingsnį atvirojo kodo modelių pasaulyje. Žemiau pateiktas kodo pavyzdys naudoja tiek vaizdą, tiek teksto užklausą, kad gautų analizę iš Llama 3.2 90B. 


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

# Gaukite juos iš jūsų Microsoft Foundry projekto „Apžvalga“ puslapio
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

## Mokymasis nesibaigia čia, tęskite kelionę

Baigę šią pamoką, peržiūrėkite mūsų [Generatyvinio AI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte savo žinias apie generatyvinį dirbtinį intelektą!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->