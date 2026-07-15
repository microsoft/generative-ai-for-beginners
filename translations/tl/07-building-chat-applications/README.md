# Pagbuo ng Generative AI-Powered Chat Applications

[![Pagbuo ng Generative AI-Powered Chat Applications](../../../translated_images/tl/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

Ngayon na nakita na natin kung paano tayo makakagawa ng mga text-generation apps, tingnan naman natin ang tungkol sa mga chat applications.

Ang mga chat applications ay naging bahagi na ng ating pang-araw-araw na buhay, hindi lamang bilang paraan ng kaswal na pag-uusap. Mahalaga sila sa customer service, technical support, at maging sa mga sopistikadong advisory systems. Malamang na nakatanggap ka ng tulong mula sa isang chat application kamakailan lamang. Habang iniintegrate natin ang mas advanced na mga teknolohiya tulad ng generative AI sa mga platform na ito, tumataas ang komplikasyon at gayundin ang mga hamon.

Ilan sa mga tanong na kailangan nating masagot ay:

- **Pagtatayo ng app**. Paano tayo magtatayo nang mahusay at seamless na maiiintegrate ang mga AI-powered applications para sa mga partikular na kaso ng paggamit?
- **Pagsubaybay**. Kapag na-deploy na, paano natin masusubaybayan at matitiyak na gumagana ang mga application sa pinakamataas na kalidad, sa aspeto ng functionality at pagsunod sa [anim na prinsipyo ng responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Sa pagpasok natin sa panahon na tinutukoy ng automation at seamless na interaksyon ng tao-at-makina, mahalagang maintindihan kung paano binabago ng generative AI ang saklaw, lalim, at kakayahang umangkop ng mga chat applications. Susuriin ng araling ito ang mga aspeto ng arkitektura na sumusuporta sa mga masalimuot na sistemang ito, tatalakayin ang mga pamamaraan para sa fine-tuning nila para sa mga domain-specific na gawain, at susuriin ang mga sukatan at konsiderasyon para sa responsableng deployment ng AI.

## Panimula

Tinatalakay ng araling ito ang:

- Mga teknik para sa mahusay na pagbuo at integrasyon ng chat applications.
- Paano gamitin ang customization at fine-tuning sa mga aplikasyon.
- Mga estratehiya at konsiderasyon upang epektibong masubaybayan ang mga chat applications.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Ilahad ang mga konsiderasyon para sa pagbuo at pag-integrate ng mga chat applications sa mga umiiral na sistema.
- Mag-customize ng chat applications para sa mga partikular na kaso ng paggamit.
- Tukuyin ang mga pangunahing sukatan at konsiderasyon upang epektibong masubaybayan at mapanatili ang kalidad ng mga AI-powered chat applications.
- Tiyakin na responsableng nagagamit ang AI sa chat applications.

## Integrasyon ng Generative AI sa mga Chat Applications

Ang pagpapataas ng antas ng mga chat applications gamit ang generative AI ay hindi lang tungkol sa pagiging mas matalino; ito ay tungkol sa pag-optimize ng kanilang arkitektura, performance, at user interface upang makapaghatid ng kalidad na karanasan sa gumagamit. Kasama dito ang pagsisiyasat sa mga pundasyon ng arkitektura, integrasyon ng API, at mga konsiderasyon para sa user interface. Layunin ng seksyong ito na magbigay sa iyo ng komprehensibong roadmap para mag-navigate sa mga komplikadong larangan na ito, maging ito’y pagdudugtong sa mga umiiral na sistema o paggawa ng standalone na mga platform.

Sa pagtatapos ng seksyong ito, magkakaroon ka ng kasanayan na kailangan upang mahusay na bumuo at mag-integrate ng mga chat applications.

### Chatbot o Chat application?

Bago tayo sumabak sa paggawa ng chat applications, ikumpara muna natin ang 'chatbots' sa 'AI-powered chat applications,' na may mga magkakaibang papel at gamit. Ang pangunahing layunin ng isang chatbot ay i-automate ang mga partikular na gawain sa pag-uusap, tulad ng pagsagot sa madalas itanong o pagsubaybay ng isang package. Karaniwan itong pinamamahalaan ng rule-based logic o komplikadong AI algorithms. Samantalang ang AI-powered chat application ay mas malawak na kapaligiran na dinisenyo upang magpatakbo ng iba’t ibang anyo ng digital na komunikasyon, tulad ng text, boses, at video chats sa pagitan ng mga tao. Ang kanyang pangunahing katangian ay ang pagsasama ng isang generative AI model na nagsisimula ng mga mas detalyado at parang tunay na pag-uusap, na bumubuo ng mga tugon batay sa malawak na klase ng input at konteksto. Ang generative AI-powered chat application ay maaaring makipag-usap sa open-domain na mga talakayan, umangkop sa nagbabagong konteksto ng pag-uusap, at makabuo ng malikhaing o masalimuot na diyalogo.

Ang talahanayan sa ibaba ay naglalahad ng mga pangunahing pagkakaiba at pagkakatulad upang matulungan tayong maunawaan ang kanilang natatanging mga papel sa digital na komunikasyon.

| Chatbot                               | Generative AI-Powered Chat Application |
| ------------------------------------- | -------------------------------------- |
| Nakatuon sa gawain at base sa patakaran | May kamalayan sa konteksto               |
| Kadalasang nakapaloob sa mas malalaking sistema | Maaaring mag-host ng isa o maraming chatbot |
| Limitado sa mga programadong function    | Nagsasama ng mga generative AI models     |
| Espesyalisado at estrukturadong interaksyon | Kayang mag-open-domain na talakayan        |

### Paggamit ng mga pre-built na functionality gamit ang SDKs at APIs

Kapag bumubuo ng isang chat application, isang magandang unang hakbang ang suriin kung ano ang mayroon na sa merkado. Ang paggamit ng SDKs at APIs sa pagtatayo ng mga chat application ay kapaki-pakinabang sa maraming dahilan. Sa pamamagitan ng integrasyon ng mga maayos na dokumentadong SDK at API, inilalagay mo ang iyong aplikasyon para sa pangmatagalang tagumpay, tinutugunan ang mga usapin sa scalability at maintenance.

- **Pinapabilis ang proseso ng pag-develop at binabawasan ang gastos**: Ang pag-asa sa mga pre-built na functionality kaysa sa mamahaling paggawa nito mula sa simula ay nagbibigay-daan sa iyo na magpokus sa iba pang aspeto ng iyong aplikasyon na maaaring mas mahalaga, tulad ng business logic.
- **Mas magandang performance**: Kapag ginawa ang functionality mula sa simula, madalas mong tatanungin ang sarili mo, "Paano ito mags-scale? Kaya ba ng app na ito ang biglaan pagdagsa ng mga user?" Mahalaga, ang mga maintenadong SDK at API ay madalas may mga built-in na solusyon para sa mga usaping ito.
- **Mas madaling maintenance**: Mas madali ang pag-manage ng mga update at pagpapabuti dahil karamihan sa mga API at SDK ay nangangailangan lang ng pag-update ng library kapag may bagong bersyon.
- **Access sa pinakabagong teknolohiya**: Ang paggamit ng mga modelong fine-tuned at sinanay sa malawak na dataset ay nagbibigay sa iyong aplikasyon ng natural language capabilities.

Ang pag-access sa functionality ng SDK o API ay karaniwang nangangailangan ng permiso sa paggamit ng mga serbisyong ibinibigay, madalas sa pamamagitan ng paggamit ng unique key o authentication token. Gagamitin natin ang OpenAI Python Library upang tingnan kung paano ito ginagawa. Maaari mo rin itong subukan sa sarili mo gamit ang [notebook para sa OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) o [notebook para sa Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) para sa araling ito.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-4o-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Ang halimbawa sa itaas ay gumagamit ng GPT-4o mini model gamit ang Responses API upang kumpletuhin ang prompt, ngunit mapapansin na itinakda muna ang API key bago gawin iyon. Makakatanggap ka ng error kung hindi mo itinakda ang key.

## Karanasan ng Gumagamit (UX)

Ang pangkalahatang prinsipyo ng UX ay nalalapat sa mga chat application, ngunit narito ang ilan pang dagdag na konsiderasyon na nagiging mahalaga dahil sa mga sangkap ng machine learning na sangkot.

- **Mekanismo para sa paglilinaw sa mga ambigwidad**: Paminsan-minsan ang mga generative AI model ay gumagawa ng malabong sagot. Ang isang tampok na nagpapahintulot sa mga user na humiling ng paglilinaw ay maaaring makatulong kung makatagpo sila ng problemang ito.
- **Pagpapanatili ng konteksto**: Ang mga advanced na generative AI model ay may kakayahang tandaan ang konteksto sa loob ng pag-uusap, na maaaring maging mahalagang asset para sa karanasan ng gumagamit. Ang pagbibigay ng kakayahan sa mga user na kontrolin at pamahalaan ang konteksto ay nagpapabuti ng karanasan ng gumagamit, ngunit nagdadala ng panganib sa pagpapanatili ng sensitibong impormasyon ng user. Ang mga konsiderasyon kung gaano katagal itatago ang impormasyong ito, tulad ng pagpapakilala ng retention policy, ay maaaring balansehin ang pangangailangan para sa konteksto laban sa privacy.
- **Pag-personalize**: Sa kakayahang matuto at umangkop, ang mga AI model ay nag-aalok ng indibidwal na karanasan para sa isang gumagamit. Ang pag-tailor ng user experience sa pamamagitan ng mga tampok tulad ng user profiles ay hindi lamang nagpaparamdam sa user na siya ay nauunawaan, kundi tumutulong din sa kanyang paghahanap ng mga tiyak na sagot, na lumilikha ng mas epektibo at kasiya-siyang interaksyon.

Isang halimbawa ng personalisasyon ay ang "Custom instructions" settings sa ChatGPT ng OpenAI. Pinapayagan kang magbigay ng impormasyon tungkol sa iyong sarili na maaaring mahalagang konteksto para sa iyong mga prompt. Narito ang isang halimbawa ng custom instruction.

![Custom Instructions Settings in ChatGPT](../../../translated_images/tl/custom-instructions.b96f59aa69356fcf.webp)

Ang "profile" na ito ay nagpaprompt sa ChatGPT na gumawa ng lesson plan tungkol sa linked lists. Napapansin na isinasaalang-alang ng ChatGPT na maaaring gusto ng user ng mas malalim na lesson plan base sa kanyang karanasan.

![A prompt in ChatGPT for a lesson plan about linked lists](../../../translated_images/tl/lesson-plan-prompt.cc47c488cf1343df.webp)

### Framework ng Microsoft para sa System Message sa Malalaking Language Model

[Nagbigay ang Microsoft ng gabay](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) para sa pagsulat ng epektibong system messages kapag bumubuo ng mga tugon mula sa LLMs na hinati sa 4 na bahagi:

1. Pagpapakilala kung para kanino ang modelo, pati na ang mga kakayahan at limitasyon nito.
2. Paglalarawan ng output format ng modelo.
3. Pagbibigay ng mga partikular na halimbawa na nagpapakita ng inaasahang ugali ng modelo.
4. Pagbibigay ng mga karagdagang behavioral guardrails.

### Accessibility

Kahit may visual, auditory, motor, o cognitive impairments ang isang user, ang maayos na disenyo ng chat application ay dapat magamit ng lahat. Ang sumusunod na listahan ay naglalaman ng mga partikular na tampok upang mapabuti ang accessibility para sa iba’t ibang kapansanan ng gumagamit.

- **Mga Tampok para sa Visual Impairment**: Mataas na contrast na themes at resizable na teksto, compatibility sa screen reader.
- **Mga Tampok para sa Auditory Impairment**: Text-to-speech at speech-to-text na mga function, mga visual cue para sa mga audio notification.
- **Mga Tampok para sa Motor Impairment**: Supporta sa keyboard navigation, voice commands.
- **Mga Tampok para sa Cognitive Impairment**: Pinadaling mga opsyon sa wika.

## Customization at Fine-tuning para sa Mga Domain-Specific Language Models

Isipin ang isang chat application na nakakaintindi ng jargon ng iyong kumpanya at inaasahan ang mga partikular na tanong na karaniwang tinatanong ng mga gumagamit nito. May ilang paraan na nararapat banggitin:

- **Paggamit ng DSL models**. Ang DSL ay nangangahulugang domain specific language. Maaari kang gumamit ng tinatawag na DSL model na sinanay sa isang partikular na domain upang maunawaan ang mga konsepto at senaryo nito.
- **Paglalapat ng fine-tuning**. Ang fine-tuning ay ang proseso ng karagdagang pagsasanay sa iyong modelo gamit ang partikular na data.

## Customization: Paggamit ng DSL

Ang paggamit ng domain-specific language models (DSL Models) ay maaaring mapabuti ang pakikipag-ugnayan ng user sa pamamagitan ng pagbibigay ng espesyalisado at kontekstwal na mga kaugnay na interaksyon. Ito ay isang modelo na sinanay o fine-tuned upang maunawaan at makabuo ng teksto na may kaugnayan sa isang partikular na larangan, industriya, o paksa. Ang mga opsyon ng paggamit ng DSL model ay maaaring mag-iba mula sa pagsasanay mula sa simula, hanggang sa paggamit ng mga umiiral na modelo sa pamamagitan ng SDKs at APIs. Isa pang opsyon ang fine-tuning, na kinabibilangan ng pag-adapt ng umiiral na pre-trained na modelo para sa isang partikular na domain.

## Customization: Paglalapat ng fine-tuning

Madalas isinaalang-alang ang fine-tuning kapag ang isang pre-trained model ay hindi sapat para sa isang espesyalisadong domain o partikular na gawain.

Halimbawa, ang mga medikal na tanong ay kumplikado at nangangailangan ng maraming konteksto. Kapag ang isang medical professional ay nag-diagnose ng pasyente, ito ay batay sa iba’t ibang salik tulad ng lifestyle o mga pre-existing na kondisyon, at maaaring umaasa pa sa mga kamakailang medical journals para patunayan ang diagnosis. Sa mga ganitong masalimuot na senaryo, hindi maaaring pagkatiwalaan ang isang pangkalahatang AI chat application.

### Senaryo: isang medikal na aplikasyon

Isipin ang isang chat application na dinisenyo upang tulungan ang mga medical practitioners sa pamamagitan ng pagbibigay ng mabilisang references sa treatment guidelines, drug interactions, o mga kamakailang research findings.

Maaring sapat ang isang general-purpose model para sa pagsagot sa mga batayang medikal na tanong o pagbibigay ng pangkalahatang payo, ngunit maaaring mapahirapan siya sa mga sumusunod:

- **Lubhang espesipiko o masalimuot na kaso**. Halimbawa, maaaring itanong ng isang neurologist sa aplikasyon, "Ano ang mga kasalukuyang pinakamahusay na gawi para sa pamamahala ng drug-resistant epilepsy sa mga pediatric patient?"
- **Kulang sa mga pinakabagong pag-unlad**. Maaaring mahirapan ang general-purpose model na magbigay ng kasalukuyang sagot na lumalahok sa mga pinakabagong pag-unlad sa neurology at pharmacology.

Sa mga ganitong pagkakataon, ang fine-tuning sa modelo gamit ang isang espesyalisadong medical dataset ay maaaring malaki ang itulong upang mapabuti ang kakayahan nito na hawakan nang tama at maaasahan ang mga komplikadong medikal na tanong. Kailangan nito ng access sa isang malaki at may kaugnayang dataset na kumakatawan sa mga espesyalisadong hamon at tanong na kailangang tugunan.

## Mga Konsiderasyon para sa Mataas na Kalidad na AI-Driven Chat Experience

Inilalahad ng seksyong ito ang mga pamantayan para sa "mataas na kalidad" na mga chat application, kabilang ang pagsukat ng mga actionable metrics at pagsunod sa isang framework na responsableng gumagamit ng AI technology.

### Mga Pangunahing Sukatan

Upang mapanatili ang mataas na kalidad na performance ng aplikasyon, mahalagang subaybayan ang mga pangunahing sukatan at konsiderasyon. Ang mga pagsukat na ito ay hindi lamang nagsisiguro ng functionality ng aplikasyon kundi sinusuri rin ang kalidad ng AI modelo at karanasan ng gumagamit. Narito ang listahan ng mga batayang sukatan, AI sukatan, at sukatan ng karanasang gumagamit na dapat isaalang-alang.

| Sukatan                       | Kahulugan                                                                                                             | Mga Konsiderasyon para sa Developer ng Chat                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Uptime**                    | Sinusukat ang oras na gumagana at naa-access ng mga gumagamit ang aplikasyon.                                          | Paano mo mapapababa ang downtime?                                  |
| **Response Time**             | Oras na kinakailangan ng aplikasyon upang sumagot sa tanong ng user.                                                  | Paano mo maa-optimize ang pagproseso para mapabilis ang tugon?     |
| **Precision**                 | Ratio ng mga tamang positibong prediksyon sa kabuuan ng positibong prediksyon.                                       | Paano mo iko-confirm ang precision ng iyong modelo?                |
| **Recall (Sensitivity)**      | Ratio ng mga tamang positibong prediksyon sa aktwal na bilang ng mga positibo.                                       | Paano mo susukatin at pahuhusayin ang recall?                      |
| **F1 Score**                  | Harmonic mean ng precision at recall, na bumabalanse sa trade-off ng dalawa.                                          | Ano ang target mong F1 Score? Paano mo babalansehin ang precision at recall? |
| **Perplexity**                | Sinusukat kung gaano kahusay ang pagkakatugma ng probabilidad na prediction ng modelo sa aktwal na distribusyon ng data. | Paano mo babawasan ang perplexity?                                 |
| **User Satisfaction Metrics** | Sinusukat ang persepsyon ng user sa aplikasyon. Kadalasang kinukuha mula sa mga survey.                              | Gaano kadalas kang mangongolekta ng feedback? Paano mo ito gagamitin? |
| **Error Rate**                | Bilang ng pagkakamali ng modelo sa pag-unawa o output.                                                               | Anong mga estratehiya ang mayroon ka upang mabawasan ang error rate? |
| **Retraining Cycles**         | Dami ng beses na nire-retrain ang modelo upang isama ang bagong datos at kaalaman.                                   | Gaano kadalas mo ire-retrain ang modelo? Ano ang nagti-trigger ng retraining cycle? |

| **Pagkilala sa Anomalya**         | Mga kasangkapan at teknik para matukoy ang mga hindi pangkaraniwang pattern na hindi umaayon sa inaasahang pag-uugali.                        | Paano ka tutugon sa mga anomalya?                                        |

### Pagpapatupad ng Responsableng AI na mga Praktis sa Mga Chat Application

Nakilala ng pamamaraan ng Microsoft sa Responsableng AI ang anim na prinsipyo na dapat gabayan ang pagbuo at paggamit ng AI. Narito ang mga prinsipyo, ang kanilang depinisyon, at mga bagay na dapat isaalang-alang ng isang chat developer at kung bakit ito dapat nilang seryosohin.

| Mga Prinsipyo             | Depinisyon ng Microsoft                                | Mga Dapat Isaalang-alang ng Chat Developer                                      | Bakit ito Mahalaga                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Katarungan               | Dapat patas ang pagtrato ng mga AI system sa lahat ng tao.            | Siguraduhing hindi nakikiling ang chat application base sa datos ng gumagamit.  | Upang makabuo ng tiwala at pagiging inklusibo sa mga gumagamit; iwasan ang mga legal na problema.                |
| Pagkakatiwalaan at Kaligtasan | Dapat magpakita ng maasahan at ligtas na pagganap ang mga AI system.        | Magpatupad ng pagsusuri at mga mekanismo ng fail-safe upang mabawasan ang mga error at panganib.         | Nagpapasiguro ng kasiyahan ng gumagamit at pumipigil sa posibleng pinsala.                                 |
| Privacy at Seguridad   | Dapat ligtas at iginagalang ang privacy ng mga AI system.      | Magpatupad ng malakas na encryption at mga hakbang sa proteksyon ng datos.              | Upang maprotektahan ang sensitibong datos ng gumagamit at sumunod sa mga batas sa privacy.                         |
| Inclusiveness          | Dapat palakasin ng mga AI system ang lahat at hikayatin silang makilahok. | Disenyuhin ang UI/UX na madaling ma-access at gamitin ng magkakaibang audiencia. | Nagpapasiguro na mas maraming tao ang mabisang makagamit ng aplikasyon.                   |
| Transparency           | Dapat maintindihan ang mga AI system.                  | Magbigay ng malinaw na dokumentasyon at paliwanag sa mga sagot ng AI.            | Mas madaling pagkatiwalaan ng mga gumagamit ang isang sistema kung naiintindihan nila kung paano ginagawa ang mga desisyon. |
| Pananagutan         | Dapat may pananagutan ang mga tao para sa mga AI system.          | Magtatag ng malinaw na proseso para sa pag-audit at pagpapabuti ng mga desisyon ng AI.     | Nagpapahintulot ng patuloy na pagpapabuti at mga korektibong hakbang sa kaso ng mga pagkakamali.               |

## Takdang Aralin

Tingnan ang [assignment](../../../07-building-chat-applications/python). Dadalhin ka nito sa isang serye ng mga ehersisyo mula sa pagsisimula ng iyong unang chat prompts, hanggang sa pag-uuri at pagbubuod ng teksto at iba pa. Pansinin na ang mga takdang aralin ay available sa iba't ibang programming languages!

## Mahusay na Gawain! Ipagpatuloy ang Paglalakbay

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

Pumunta sa Lesson 8 upang makita kung paano ka makapagsisimula sa [pagbuo ng mga application sa paghahanap](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->