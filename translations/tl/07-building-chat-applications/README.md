<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5308963a56cfbad2d73b0fa99fe84b3",
  "translation_date": "2025-10-18T01:10:45+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "tl"
}
-->
# Paggawa ng Mga Chat Application na Pinapagana ng Generative AI

[![Paggawa ng Mga Chat Application na Pinapagana ng Generative AI](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.tl.png)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(I-click ang imahe sa itaas upang mapanood ang video ng araling ito)_

Ngayon na nakita na natin kung paano gumawa ng mga text-generation apps, tingnan naman natin ang mga chat application.

Ang mga chat application ay naging bahagi na ng ating pang-araw-araw na buhay, na nagbibigay ng higit pa sa simpleng paraan ng pakikipag-usap. Sila ay mahalagang bahagi ng customer service, technical support, at maging ng mga sopistikadong advisory systems. Malamang na nakatanggap ka na ng tulong mula sa isang chat application kamakailan lamang. Habang isinasama natin ang mas advanced na teknolohiya tulad ng generative AI sa mga platform na ito, tumataas ang antas ng pagiging kumplikado gayundin ang mga hamon.

Ilan sa mga tanong na kailangang sagutin ay:

- **Paggawa ng app**. Paano natin epektibong magagawa at ma-integrate ang mga AI-powered application para sa partikular na mga layunin?
- **Pagmo-monitor**. Kapag nailunsad na, paano natin masisiguro na ang mga application ay gumagana sa pinakamataas na antas ng kalidad, parehong sa aspeto ng functionality at pagsunod sa [anim na prinsipyo ng responsableng AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Habang patuloy tayong pumapasok sa panahon ng automation at seamless na interaksyon sa pagitan ng tao at makina, nagiging mahalaga ang pag-unawa kung paano binabago ng generative AI ang saklaw, lalim, at adaptability ng mga chat application. Ang araling ito ay mag-iimbestiga sa mga aspeto ng arkitektura na sumusuporta sa mga masalimuot na sistema, susuriin ang mga metodolohiya para sa fine-tuning sa mga domain-specific na gawain, at tatalakayin ang mga metrics at konsiderasyon na mahalaga upang masiguro ang responsableng pag-deploy ng AI.

## Panimula

Ang araling ito ay sumasaklaw sa:

- Mga teknik para sa epektibong paggawa at pag-integrate ng mga chat application.
- Paano mag-apply ng customization at fine-tuning sa mga application.
- Mga estratehiya at konsiderasyon para sa epektibong pagmo-monitor ng mga chat application.

## Mga Layunin sa Pag-aaral

Sa pagtatapos ng araling ito, magagawa mong:

- Ilarawan ang mga konsiderasyon sa paggawa at pag-integrate ng mga chat application sa mga umiiral na sistema.
- I-customize ang mga chat application para sa partikular na mga layunin.
- Tukuyin ang mga pangunahing metrics at konsiderasyon para sa epektibong pagmo-monitor at pagpapanatili ng kalidad ng mga AI-powered chat application.
- Siguraduhing ang mga chat application ay gumagamit ng AI nang responsable.

## Pag-integrate ng Generative AI sa Mga Chat Application

Ang pagpapahusay sa mga chat application gamit ang generative AI ay hindi lamang tungkol sa pagpapatalino sa kanila; ito ay tungkol sa pag-optimize ng kanilang arkitektura, performance, at user interface upang magbigay ng de-kalidad na karanasan sa gumagamit. Kasama dito ang pagsisiyasat sa mga pundasyon ng arkitektura, API integrations, at mga konsiderasyon sa user interface. Ang seksyong ito ay naglalayong magbigay sa iyo ng komprehensibong roadmap para sa pag-navigate sa mga masalimuot na aspeto, maging ito man ay pag-integrate sa mga umiiral na sistema o paggawa ng mga stand-alone na platform.

Sa pagtatapos ng seksyong ito, magkakaroon ka ng kaalaman na kinakailangan upang epektibong makagawa at ma-incorporate ang mga chat application.

### Chatbot o Chat Application?

Bago tayo sumabak sa paggawa ng mga chat application, ikumpara muna natin ang 'chatbots' sa 'AI-powered chat applications,' na may magkakaibang papel at functionality. Ang pangunahing layunin ng chatbot ay ang awtomatikong pagsagot sa mga partikular na tanong, tulad ng mga madalas itanong o pagsubaybay sa isang package. Karaniwan itong pinapatakbo ng rule-based logic o masalimuot na AI algorithms. Sa kabilang banda, ang AI-powered chat application ay mas malawak na platform na idinisenyo upang mapadali ang iba't ibang anyo ng digital na komunikasyon, tulad ng text, voice, at video chats sa pagitan ng mga tao. Ang pangunahing katangian nito ay ang integrasyon ng generative AI model na gumagaya sa masalimuot, parang tao na mga pag-uusap, na gumagawa ng mga sagot batay sa iba't ibang input at konteksto.

Ang talahanayan sa ibaba ay naglalarawan ng mga pangunahing pagkakaiba at pagkakatulad upang mas maunawaan natin ang kanilang natatanging papel sa digital na komunikasyon.

| Chatbot                               | Generative AI-Powered Chat Application |
| ------------------------------------- | -------------------------------------- |
| Nakatuon sa tiyak na gawain at rule-based | May kamalayan sa konteksto             |
| Madalas na naka-integrate sa mas malalaking sistema | Maaaring mag-host ng isa o maraming chatbots |
| Limitado sa mga naka-program na function | May integrasyon ng generative AI models |
| Espesyalista at may istrukturang interaksyon | Kayang makipag-usap sa open-domain     |

### Paggamit ng Pre-built Functionalities gamit ang SDKs at APIs

Kapag gumagawa ng chat application, magandang simula ang suriin kung ano ang mga umiiral na solusyon. Ang paggamit ng SDKs at APIs sa paggawa ng chat applications ay isang kapaki-pakinabang na estratehiya para sa iba't ibang dahilan. Sa pamamagitan ng pag-integrate ng maayos na dokumentadong SDKs at APIs, inilalagay mo ang iyong application sa tamang posisyon para sa pangmatagalang tagumpay, na tinutugunan ang mga isyu sa scalability at maintenance.

- **Pinapabilis ang proseso ng paggawa at binabawasan ang gastos**: Ang pag-asa sa mga pre-built functionalities sa halip na gumastos sa paggawa ng sarili ay nagbibigay-daan sa iyo na mag-focus sa iba pang aspeto ng iyong application na mas mahalaga, tulad ng business logic.
- **Mas mahusay na performance**: Kapag gumagawa ng functionality mula sa simula, darating ang tanong na "Paano ito mag-scale? Kaya ba ng application na ito ang biglaang pagdami ng mga gumagamit?" Ang maayos na pinapanatili na SDK at APIs ay madalas may built-in na solusyon para sa mga ganitong isyu.
- **Mas madaling maintenance**: Ang mga update at pagpapabuti ay mas madaling pamahalaan dahil ang karamihan sa mga APIs at SDKs ay nangangailangan lamang ng pag-update sa library kapag may bagong bersyon.
- **Access sa cutting-edge na teknolohiya**: Ang paggamit ng mga modelong na fine-tune at na-train sa malawak na datasets ay nagbibigay sa iyong application ng natural language capabilities.

Ang pag-access sa functionality ng isang SDK o API ay karaniwang nangangailangan ng pahintulot upang magamit ang mga serbisyong ibinibigay, na kadalasang ginagawa sa pamamagitan ng paggamit ng isang natatanging key o authentication token. Gagamitin natin ang OpenAI Python Library upang suriin kung paano ito ginagawa. Maaari mo rin itong subukan sa iyong sarili sa sumusunod na [notebook para sa OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) o [notebook para sa Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) para sa araling ito.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Ang halimbawa sa itaas ay gumagamit ng GPT-3.5 Turbo model upang kumpletuhin ang prompt, ngunit mapapansin na ang API key ay na-set bago ito gawin. Magkakaroon ka ng error kung hindi mo na-set ang key.

## User Experience (UX)

Ang mga pangkalahatang prinsipyo ng UX ay naaangkop sa mga chat application, ngunit narito ang ilang karagdagang konsiderasyon na nagiging partikular na mahalaga dahil sa mga sangkap ng machine learning na kasangkot.

- **Mekanismo para sa pag-aaddress ng ambiguity**: Ang mga generative AI models ay paminsan-minsan gumagawa ng mga sagot na hindi malinaw. Ang isang feature na nagbibigay-daan sa mga gumagamit na humingi ng paglilinaw ay maaaring maging kapaki-pakinabang kung sakaling maharap sila sa problemang ito.
- **Pagpapanatili ng konteksto**: Ang mga advanced generative AI models ay may kakayahang tandaan ang konteksto sa loob ng isang pag-uusap, na maaaring maging mahalagang asset sa karanasan ng gumagamit. Ang pagbibigay sa mga gumagamit ng kakayahang kontrolin at pamahalaan ang konteksto ay nagpapabuti sa karanasan ng gumagamit, ngunit nagdadala ng panganib ng pag-iimbak ng sensitibong impormasyon ng gumagamit. Ang mga konsiderasyon kung gaano katagal dapat itago ang impormasyong ito, tulad ng pagpapakilala ng retention policy, ay maaaring magbalanse sa pangangailangan para sa konteksto laban sa privacy.
- **Personalization**: Sa kakayahang matuto at mag-adapt, ang mga AI models ay nag-aalok ng isang indibidwal na karanasan para sa isang gumagamit. Ang pag-tailor sa karanasan ng gumagamit sa pamamagitan ng mga feature tulad ng user profiles ay hindi lamang nagpaparamdam sa gumagamit na naiintindihan siya, ngunit nakakatulong din sa kanyang paghahanap ng partikular na sagot, na lumilikha ng mas epektibo at kasiya-siyang interaksyon.

Isang halimbawa ng personalization ay ang "Custom instructions" settings sa ChatGPT ng OpenAI. Pinapayagan ka nitong magbigay ng impormasyon tungkol sa iyong sarili na maaaring mahalagang konteksto para sa iyong mga prompt. Narito ang isang halimbawa ng custom instruction.

![Custom Instructions Settings sa ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.tl.png)

Ang "profile" na ito ay nag-uudyok sa ChatGPT na gumawa ng lesson plan tungkol sa linked lists. Mapapansin na isinasaalang-alang ng ChatGPT na maaaring gusto ng user ng mas malalim na lesson plan batay sa kanyang karanasan.

![Isang prompt sa ChatGPT para sa lesson plan tungkol sa linked lists](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.tl.png)

### Microsoft's System Message Framework para sa Malalaking Language Models

[Ang Microsoft ay nagbigay ng gabay](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) para sa epektibong pagsulat ng system messages kapag gumagawa ng mga sagot mula sa LLMs na hinati sa 4 na bahagi:

1. Tukuyin kung para kanino ang model, pati na rin ang mga kakayahan at limitasyon nito.
2. Tukuyin ang format ng output ng model.
3. Magbigay ng mga partikular na halimbawa na nagpapakita ng intended behavior ng model.
4. Magbigay ng karagdagang behavioral guardrails.

### Accessibility

Kung ang isang gumagamit ay may visual, auditory, motor, o cognitive impairments, ang isang maayos na disenyo ng chat application ay dapat magamit ng lahat. Ang sumusunod na listahan ay nagbabalangkas ng mga partikular na feature na naglalayong pahusayin ang accessibility para sa iba't ibang uri ng impairments.

- **Mga Feature para sa Visual Impairment**: High contrast themes at resizable text, screen reader compatibility.
- **Mga Feature para sa Auditory Impairment**: Text-to-speech at speech-to-text functions, visual cues para sa audio notifications.
- **Mga Feature para sa Motor Impairment**: Keyboard navigation support, voice commands.
- **Mga Feature para sa Cognitive Impairment**: Simplified language options.

## Customization at Fine-tuning para sa Domain-Specific Language Models

Isipin ang isang chat application na nauunawaan ang jargon ng iyong kumpanya at inaasahan ang mga partikular na tanong na madalas itanong ng mga gumagamit nito. Mayroong ilang mga approach na dapat banggitin:

- **Paggamit ng DSL models**. Ang DSL ay nangangahulugang domain specific language. Maaari kang gumamit ng tinatawag na DSL model na na-train sa isang partikular na domain upang maunawaan ang mga konsepto at senaryo nito.
- **Pag-apply ng fine-tuning**. Ang fine-tuning ay ang proseso ng karagdagang pag-train sa iyong model gamit ang partikular na data.

## Customization: Paggamit ng DSL

Ang paggamit ng domain-specific language models (DSL Models) ay maaaring pahusayin ang engagement ng gumagamit sa pamamagitan ng pagbibigay ng espesyalista, kontekstwal na may kaugnayang interaksyon. Ito ay isang model na na-train o na-fine-tune upang maunawaan at makabuo ng teksto na may kaugnayan sa isang partikular na larangan, industriya, o paksa. Ang mga opsyon para sa paggamit ng DSL model ay maaaring mag-iba mula sa pag-train ng isa mula sa simula, hanggang sa paggamit ng mga umiiral na sa pamamagitan ng SDKs at APIs. Isa pang opsyon ay ang fine-tuning, na kinabibilangan ng pag-adapt sa isang umiiral na pre-trained model para sa isang partikular na domain.

## Customization: Pag-apply ng Fine-tuning

Ang fine-tuning ay madalas na isinasaalang-alang kapag ang isang pre-trained model ay hindi sapat para sa isang espesyalistang domain o partikular na gawain.

Halimbawa, ang mga medikal na tanong ay masalimuot at nangangailangan ng maraming konteksto. Kapag ang isang medikal na propesyonal ay nag-diagnose ng isang pasyente, ito ay batay sa iba't ibang mga salik tulad ng lifestyle o pre-existing conditions, at maaaring umasa pa sa mga kamakailang medikal na journal upang ma-validate ang kanilang diagnosis. Sa ganitong mga masalimuot na senaryo, ang isang general-purpose AI chat application ay hindi maaaring maging maaasahang source.

### Senaryo: isang medikal na application

Isipin ang isang chat application na idinisenyo upang tulungan ang mga medikal na practitioner sa pamamagitan ng pagbibigay ng mabilis na reference sa mga treatment guidelines, drug interactions, o mga kamakailang research findings.

Ang isang general-purpose model ay maaaring sapat para sa pagsagot sa mga pangunahing medikal na tanong o pagbibigay ng pangkalahatang payo, ngunit maaaring magkulang sa mga sumusunod:

- **Napaka-espesipiko o masalimuot na mga kaso**. Halimbawa, maaaring itanong ng isang neurologist sa application, "Ano ang kasalukuyang pinakamahusay na mga pamamaraan para sa pamamahala ng drug-resistant epilepsy sa mga pediatric na pasyente?"
- **Kakulangan sa mga kamakailang advancements**. Ang isang general-purpose model ay maaaring mahirapan magbigay ng kasalukuyang sagot na isinasaalang-alang ang pinakabagong advancements sa neurology at pharmacology.

Sa mga ganitong pagkakataon, ang fine-tuning sa model gamit ang isang espesyalistang medikal na dataset ay maaaring lubos na pahusayin ang kakayahan nitong tugunan ang mga masalimuot na medikal na tanong nang mas tumpak at maaasahan. Nangangailangan ito ng access sa isang malaki at may kaugnayang dataset na kumakatawan sa mga domain-specific na hamon at tanong na kailangang tugunan.

## Mga Konsiderasyon para sa Mataas na Kalidad na AI-Driven Chat Experience

Ang seksyong ito ay nagbabalangkas ng mga pamantayan para sa "mataas na kalidad" na chat applications, na kinabibilangan ng pagkuha ng actionable metrics at pagsunod sa isang framework na responsable sa paggamit ng teknolohiyang AI.

### Mga Pangunahing Metrics

Upang mapanatili ang mataas na kalidad na performance ng isang application, mahalaga na subaybayan ang mga pangunahing metrics at konsiderasyon. Ang mga sukat na ito ay hindi lamang nagsisiguro sa functionality ng application kundi sinusuri rin ang kalidad ng AI model at karanasan ng gumagamit. Narito ang isang listahan na sumasaklaw sa mga pangunahing metrics ng AI at user experience na dapat isaalang-alang.

| Metric                        | Kahulugan                                                                                                             | Mga Konsiderasyon para sa Developer ng Chat                              |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Uptime**                    | Sinusukat ang oras na operational at accessible ang application ng mga gumagamit.                                      | Paano mo mababawasan ang downtime?                                        |
| **Response Time**             | Ang oras na ginugol ng application upang sumagot sa tanong ng gumagamit.                                               | Paano mo ma-optimize ang query processing upang mapabuti ang response time? |
| **Precision**                 | Ang ratio ng tamang positibong prediksyon sa kabuuang bilang ng positibong prediksyon.                                  | Paano mo ma-validate ang precision ng iyong model?                        |
| **Recall (Sensitivity)**      | Ang ratio ng tamang positibong prediksyon sa aktwal na bilang ng positibo.                                             | Paano mo susukatin at pahuhusayin ang recall?                             |
| **F1 Score**                  | Ang harmonic mean ng precision at recall, na nagbabalanse sa trade-off sa pagitan ng dalawa.                          | Ano ang target mong F1 Score? Paano mo babalansehin ang precision at recall? |
| **Perplexity**                | Sinusukat kung gaano kahusay ang probability distribution na hinulaan ng model na tumutugma sa aktwal na distribution ng data. | Paano mo mababawasan ang perplexity?                                      |
| **User Satisfaction Metrics** | Sinusukat ang perception ng gumagamit sa application. Madalas na kinukuha sa pamamagitan ng surveys.                   | Gaano kadalas ka mangangalap ng feedback mula sa gumagamit? Paano mo ito gagamitin? |
| **Error Rate**                | Ang rate kung saan nagkakamali ang model sa pag-unawa o output.                                                        | Anong mga estratehiya ang mayroon ka upang mabawasan ang error rates?     |
| **Retraining Cycles**         | Ang dalas kung saan ina-update ang model upang isama ang bagong data at insights.                                      | Gaano kadalas mo ire-retrain ang model? Ano ang magti-trigger ng retraining cycle? |
| **Pag-detect ng Anomalya**         | Mga kasangkapan at teknik para matukoy ang mga hindi pangkaraniwang pattern na hindi umaayon sa inaasahang pag-uugali.                        | Paano mo tutugunan ang mga anomalya?                                        |

### Pagpapatupad ng Responsableng Praktika ng AI sa Mga Chat Application

Ang diskarte ng Microsoft sa Responsableng AI ay nagtataguyod ng anim na prinsipyo na dapat gabayan ang pag-develop at paggamit ng AI. Narito ang mga prinsipyo, ang kanilang kahulugan, at mga bagay na dapat isaalang-alang ng isang chat developer at kung bakit mahalaga ang mga ito.

| Mga Prinsipyo           | Kahulugan ng Microsoft                                | Mga Dapat Isaalang-alang ng Chat Developer                              | Bakit Ito Mahalaga                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Pagkamakatarungan      | Ang mga sistema ng AI ay dapat tratuhin nang patas ang lahat ng tao. | Siguraduhing ang chat application ay hindi nagdidiskrimina batay sa datos ng user. | Upang makabuo ng tiwala at inclusivity sa mga user; maiwasan ang legal na problema.     |
| Kahusayan at Kaligtasan | Ang mga sistema ng AI ay dapat gumana nang maayos at ligtas. | Magpatupad ng testing at mga fail-safe upang mabawasan ang mga error at panganib. | Tinitiyak ang kasiyahan ng user at pinipigilan ang posibleng pinsala.                  |
| Privacy at Seguridad    | Ang mga sistema ng AI ay dapat maging ligtas at igalang ang privacy. | Magpatupad ng malakas na encryption at mga hakbang sa proteksyon ng datos. | Upang mapangalagaan ang sensitibong datos ng user at sumunod sa mga batas sa privacy.   |
| Inclusiveness           | Ang mga sistema ng AI ay dapat magbigay kapangyarihan sa lahat at makipag-ugnayan sa mga tao. | Magdisenyo ng UI/UX na accessible at madaling gamitin para sa iba't ibang audience. | Tinitiyak na mas maraming tao ang makakagamit ng application nang epektibo.            |
| Transparency            | Ang mga sistema ng AI ay dapat madaling maunawaan.    | Magbigay ng malinaw na dokumentasyon at paliwanag para sa mga tugon ng AI. | Mas malamang na magtiwala ang mga user sa sistema kung nauunawaan nila kung paano ginagawa ang mga desisyon. |
| Pananagutan             | Ang mga tao ay dapat managot para sa mga sistema ng AI. | Magtatag ng malinaw na proseso para sa pag-audit at pagpapabuti ng mga desisyon ng AI. | Nagbibigay-daan sa patuloy na pagpapabuti at pagwawasto sa kaso ng mga pagkakamali.     |

## Takdang-Aralin

Tingnan ang [takdang-aralin](../../../07-building-chat-applications/python). Dadalhin ka nito sa serye ng mga ehersisyo mula sa pag-run ng iyong unang chat prompts, hanggang sa pag-classify at pag-summarize ng teksto at iba pa. Pansinin na ang mga takdang-aralin ay available sa iba't ibang programming languages!

## Magaling! Ipagpatuloy ang Paglalakbay

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang patuloy na mapalawak ang iyong kaalaman sa Generative AI!

Pumunta sa Lesson 8 upang makita kung paano ka makakapagsimula sa [pagbuo ng mga search application](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.