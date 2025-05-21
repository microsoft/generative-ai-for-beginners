<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:07:05+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "mo"
}
-->
# Binaa ma'a Namoothajaat Usrat Meta

## Muqadima

Hadhihi al-dars satughati:

- Istikshaf al-namoothajayn al-ra'iseeyayn li-usrat Meta - Llama 3.1 wa Llama 3.2
- Fahm al-istekhdamaat wa al-sinariohaat likull namoothaj
- Namozaj code li-izhar al-mazaat al-fareeda likull namoothaj

## Usrat Namoothajaat Meta

Fi hadhihi al-dars, sanastakshif 2 namoothajaat min usrat Meta aw "Qati' Llama" - Llama 3.1 wa Llama 3.2.

Hadhihi al-namoothajaat tatia fi anwa' mukhtalifa wa tatawafar fi suq GitHub Model. Huna tafasil akthar hawl istikhdam Namoothajaat GitHub li [tashkil namoothajaat AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Anwa' al-Namoothajaat:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Mulahadha: Llama 3 aydaan mutawafar ala Namoothajaat GitHub walakin lan yughati fi hadhihi al-dars*

## Llama 3.1

Bi 405 milyar mu'addilat, Llama 3.1 yandam ila qism LLM al-maftooh al-masdar.

Al-namoothaj huwa tarqiya li-sadr as-sabiq Llama 3 bi-taqdeem:

- Nafitha siyaq akbar - 128k tokens muqabil 8k tokens
- Akbar Max Output Tokens - 4096 muqabil 2048
- Da'am afdal li-lughat muta'addida - bisabab ziyaada fi tokens at-ta'aleem

Hadhihi al-mazaat tamkin Llama 3.1 min ta'amul ma'a mustakhdamaat akthar taqeedan 'ind bina baramij GenAI bima fiha:
- Nadha al-funqiyaat al-asliya - al-qadra ala nadha alat wa funqiyaat kharij workflow LLM
- Ada' RAG afdal - bisabab nafitha siyaq akbar
- Tawleed bayanat sintetik - al-qadra ala insha bayanat mu'athira li-mahamaat mithla tadhil al-dala'ib

### Nadha al-funqiyaat al-asliya

Llama 3.1 qamat bi-tahseen li-takoon akthar fa'aliya fi nadha funqiyaat aw alat. Aydaan, ladayha alat mabniya fi al-namoothaj yumkin an yat'araf 'alayha ka-hajaat li-istikhdam bisabab al-tahadi min al-mustakhdim. Hadhihi al-alat hiya:

- **Brave Search** - yumkin istikhdamha li-hasool ala ma'lumaat muwakkata mithla al-taqs bi-tanfidh bahth ala al-internet
- **Wolfram Alpha** - yumkin istikhdamha li-hisabat riyadiya akthar taqeedan fa la yajib kataba funqiyaatak al-khas.

Yumkin aydaan insha alat khasat bi-ka yumkin nadha min LLM.

Fi namozaj code adna:

- Nu'arif al-alat al-muwafara (brave_search, wolfram_alpha) fi al-tahadi nitham.
- Nursil tahadi mustakhdim yas'al hawl al-taqs fi madina mu'ayyana.
- LLM sayarud bi-nadha alat li-alat Brave Search allati satabdu mithla hatha `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Mulahadha: Hadhihi al-namozaj yujri nadha al-alat faqat, idha turid al-hasool ala al-nata'ij, sa-yajib insha hesab majani fi safhat Brave API wa ta'arif al-funqiya binafsaha*

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

Raghma konha LLM, wahid min al-ma'ayib li-Llama 3.1 huwa al-tawajuh al-mutahaddid. Ay, al-qadra ala istikhdam anwa' mukhtalifa min al-madakhil mithla al-suwar ka-tahadiyat wa taqdeem radud. Hadhihi al-qadra hiya wahid min al-mazaat al-ra'iseeya li-Llama 3.2. Hadhihi al-mazaat aydaan tatawafor:

- Tawajuh mutahaddid - ladayha al-qadra ala taqdeer tahadiyat matn wa sura
- Anwa' sghira ila mutawassita (11B wa 90B) - hada yuqdeem khayarat tawthiq muruna
- Anwa' matn faqat (1B wa 3B) - hada yasmah li-namoothaj bil-tawthiq ala ajhiza al-hafa / ajhiza al-hatif wa yuqdeem khayarat low latency

Da'am mutahaddid yumathil qadam kabeer fi 'alam namoothajaat al-maftooh al-masdar. Namozaj code adna ya'thak wa tahadiyat matn wa sura li-hasool ala tahleel al-sura min Llama 3.2 90B.

### Da'am mutahaddid ma'a Llama 3.2

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

## Al-ta'aleem la yatwaqqaf huna, istamirr fi al-rahlah

Ba'ad ikmal hadhihi al-dars, itlaq nazhra ala [Majmu'at Ta'aleem AI al-Insha'](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) li-istimrar fi raf'a ma'arifatka fi AI al-Insha!

I'm sorry, but I can't assist with translating the text into "mo" as it doesn't appear to correspond to a specific language. Could you please clarify or specify the language you need the text translated into?