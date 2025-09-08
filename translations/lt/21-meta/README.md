<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-08-25T12:46:22+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "lt"
}
-->
# Darbas su Meta šeimos modeliais

## Įvadas

Šioje pamokoje aptarsime:

- Dviejų pagrindinių Meta šeimos modelių – Llama 3.1 ir Llama 3.2 – apžvalgą
- Kiekvieno modelio naudojimo atvejus ir scenarijus
- Kodo pavyzdį, parodantį kiekvieno modelio unikalius bruožus

## Meta modelių šeima

Šioje pamokoje apžvelgsime 2 modelius iš Meta šeimos, dar vadinamos „Llama banda“ – Llama 3.1 ir Llama 3.2

Šie modeliai turi skirtingas versijas ir yra prieinami GitHub Model marketplace. Daugiau informacijos apie GitHub Models naudojimą [AI modelių prototipavimui](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modelių variantai:
- Llama 3.1 – 70B Instruct
- Llama 3.1 – 405B Instruct
- Llama 3.2 – 11B Vision Instruct
- Llama 3.2 – 90B Vision Instruct

*Pastaba: Llama 3 taip pat prieinamas GitHub Models, tačiau šioje pamokoje nebus aptariamas*

## Llama 3.1

Turėdamas 405 milijardus parametrų, Llama 3.1 patenka į atvirojo kodo LLM kategoriją.

Šis modelis yra ankstesnės Llama 3 versijos patobulinimas, siūlantis:

- Didesnį konteksto langą – 128k žodžių vietoj 8k
- Didesnį maksimalų išvesties žodžių skaičių – 4096 vietoj 2048
- Geresnę daugiakalbę paramą – dėl padidėjusio mokymo duomenų kiekio

Tai leidžia Llama 3.1 spręsti sudėtingesnius atvejus kuriant GenAI programas, įskaitant:
- Gimtą funkcijų iškvietimą – galimybę kviesti išorinius įrankius ir funkcijas už LLM ribų
- Geresnį RAG našumą – dėl didesnio konteksto lango
- Sintetinių duomenų generavimą – galimybę kurti efektyvius duomenis, pvz., modelio patobulinimui

### Gimtasis funkcijų iškvietimas

Llama 3.1 buvo papildomai apmokytas, kad efektyviau kviestų funkcijas ar įrankius. Jame taip pat yra du integruoti įrankiai, kuriuos modelis gali atpažinti kaip reikalingus naudoti pagal vartotojo užklausą. Šie įrankiai:

- **Brave Search** – gali būti naudojamas gauti naujausią informaciją, pvz., orus, atliekant paiešką internete
- **Wolfram Alpha** – gali būti naudojamas sudėtingesniems matematiniams skaičiavimams, todėl nereikia rašyti savo funkcijų

Taip pat galite susikurti savo pasirinktinius įrankius, kuriuos LLM galės kviesti.

Žemiau pateiktame kodo pavyzdyje:

- Sistemos užklausoje apibrėžiame galimus įrankius (brave_search, wolfram_alpha)
- Vartotojo užklausa klausia apie orus tam tikrame mieste
- LLM atsakys įrankio iškvietimu Brave Search įrankiui, kuris atrodys taip: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Pastaba: Šiame pavyzdyje įrankis tik iškviečiamas, jei norite gauti rezultatus, turėsite susikurti nemokamą paskyrą Brave API puslapyje ir apibrėžti pačią funkciją*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

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

Nors Llama 3.1 yra LLM, viena iš jo ribojimų – multimodalumas. Tai reiškia, kad jis negali naudoti skirtingų įvesties tipų, pavyzdžiui, vaizdų, kaip užklausų ir pateikti atsakymų. Ši galimybė yra vienas pagrindinių Llama 3.2 bruožų. Kiti šio modelio privalumai:

- Multimodalumas – gali apdoroti tiek tekstines, tiek vaizdines užklausas
- Mažos ir vidutinės apimties variantai (11B ir 90B) – suteikia lankstumo diegiant
- Tik tekstiniai variantai (1B ir 3B) – leidžia modelį diegti kraštiniuose / mobiliuosiuose įrenginiuose ir užtikrina mažą delsą

Multimodalinė parama yra didelis žingsnis atvirojo kodo modelių pasaulyje. Žemiau pateiktame kodo pavyzdyje naudojamas ir vaizdas, ir tekstinė užklausa, kad Llama 3.2 90B pateiktų vaizdo analizę.

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

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
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

## Mokymasis čia nesibaigia – tęskite kelionę

Baigę šią pamoką, apsilankykite mūsų [Generatyvaus AI mokymosi kolekcijoje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte žinias apie generatyvųjį AI!

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.