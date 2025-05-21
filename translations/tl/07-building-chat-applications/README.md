<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea4bbe640847aafbbba14dae4625e9af",
  "translation_date": "2025-05-19T18:02:43+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "tl"
}
-->
# Paggawa ng Mga Chat Application na Pinapagana ng Generative AI

> _(I-click ang imahe sa itaas upang panoorin ang video ng araling ito)_

Ngayong nakita na natin kung paano bumuo ng mga app para sa pagbuo ng teksto, tingnan natin ang mga chat application.

Ang mga chat application ay naging bahagi na ng ating pang-araw-araw na buhay, na nag-aalok ng higit pa sa isang paraan ng kaswal na pag-uusap. Mahalaga ang mga ito sa customer service, teknikal na suporta, at maging sa mga sopistikadong advisory system. Malamang na nakatanggap ka ng tulong mula sa isang chat application kamakailan lamang. Habang isinasama natin ang mas advanced na teknolohiya tulad ng generative AI sa mga platform na ito, tumataas ang kumplikasyon at gayundin ang mga hamon.

Ilan sa mga tanong na kailangan nating sagutin ay:

- **Pagbuo ng app**. Paano natin mahusay na mabubuo at seamless na maisasama ang mga AI-powered na application para sa mga partikular na kaso ng paggamit?
- **Pagsubaybay**. Kapag nailunsad na, paano natin masusubaybayan at masisiguro na ang mga application ay gumagana sa pinakamataas na antas ng kalidad, kapwa sa mga tuntunin ng pag-andar at pagsunod sa [anim na prinsipyo ng responsableng AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Habang tayo ay patungo sa isang panahon na tinukoy ng automation at seamless na pakikipag-ugnayan ng tao at makina, nagiging mahalaga ang pag-unawa sa kung paano binabago ng generative AI ang saklaw, lalim, at kakayahang umangkop ng mga chat application. Ang araling ito ay susuri sa mga aspeto ng arkitektura na sumusuporta sa mga masalimuot na sistemang ito, sisiyasatin ang mga pamamaraan para sa pag-fine-tune sa mga ito para sa mga gawain na tiyak sa domain, at susuriin ang mga sukatan at pagsasaalang-alang na may kaugnayan sa pagtiyak ng responsableng pag-deploy ng AI.

## Panimula

Saklaw ng araling ito ang:

- Mga pamamaraan para sa mahusay na pagbuo at pagsasama ng mga chat application.
- Paano mag-apply ng pag-customize at pag-fine-tune sa mga application.
- Mga estratehiya at pagsasaalang-alang para sa epektibong pagsubaybay sa mga chat application.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Ilarawan ang mga pagsasaalang-alang para sa pagbuo at pagsasama ng mga chat application sa mga umiiral na sistema.
- I-customize ang mga chat application para sa mga partikular na kaso ng paggamit.
- Tukuyin ang mga pangunahing sukatan at pagsasaalang-alang para sa epektibong pagsubaybay at pagpapanatili ng kalidad ng mga AI-powered na chat application.
- Tiyakin na ang mga chat application ay gumagamit ng AI nang responsable.

## Pagsasama ng Generative AI sa Mga Chat Application

Ang pagpapahusay ng mga chat application sa pamamagitan ng generative AI ay hindi lamang nakatuon sa pagpapatalino sa kanila; ito ay tungkol sa pag-optimize ng kanilang arkitektura, pagganap, at user interface upang makapaghatid ng isang kalidad na karanasan ng gumagamit. Kasama rito ang pagsisiyasat sa mga pundasyong arkitektura, pagsasama ng API, at mga pagsasaalang-alang sa user interface. Ang seksyong ito ay naglalayong mag-alok sa iyo ng isang komprehensibong roadmap para sa pag-navigate sa mga kumplikadong landscape na ito, maging ikaw ay nagsasaksak sa kanila sa mga umiiral na sistema o bumubuo sa kanila bilang mga stand-alone na platform.

Sa pagtatapos ng seksyong ito, magiging handa ka sa kaalaman na kailangan upang mahusay na makabuo at maisama ang mga chat application.

### Chatbot o Chat application?

Bago tayo sumisid sa pagbuo ng mga chat application, ikumpara natin ang 'chatbots' laban sa 'AI-powered chat applications,' na may magkakaibang tungkulin at pag-andar. Ang pangunahing layunin ng isang chatbot ay upang i-automate ang mga tiyak na gawain sa pag-uusap, tulad ng pagsagot sa mga madalas itanong o pagsubaybay sa isang package. Karaniwan itong pinamamahalaan ng rule-based na lohika o mga kumplikadong AI algorithm. Sa kabaligtaran, ang isang AI-powered chat application ay isang mas malawak na kapaligiran na idinisenyo upang mapadali ang iba't ibang anyo ng digital na komunikasyon, tulad ng text, boses, at video chats sa mga gumagamit na tao. Ang pangunahing tampok nito ay ang pagsasama ng isang generative AI model na gumagaya sa mga masalimuot, human-like na pag-uusap, na bumubuo ng mga tugon batay sa iba't ibang input at mga pahiwatig sa konteksto. Ang isang generative AI powered chat application ay maaaring makipag-ugnayan sa mga open-domain na talakayan, umangkop sa mga umuusbong na konteksto ng pag-uusap, at maging makabuo ng malikhaing o kumplikadong diyalogo.

Ang talahanayan sa ibaba ay nagbabalangkas ng mga pangunahing pagkakaiba at pagkakatulad upang matulungan tayong maunawaan ang kanilang natatanging tungkulin sa digital na komunikasyon.

| Chatbot                               | Generative AI-Powered Chat Application |
| ------------------------------------- | -------------------------------------- |
| Nakatutok sa gawain at batay sa patakaran | Nakakaalam sa konteksto                |
| Madalas na isinama sa mas malalaking sistema | Maaaring mag-host ng isa o maraming chatbots |
| Limitado sa mga naka-program na function | May kasamang generative AI models     |
| Dalubhasa at nakabalangkas na pakikipag-ugnayan | May kakayahang makipag-usap sa open-domain |

### Paggamit ng mga pre-built na functionality gamit ang SDKs at APIs

Kapag bumubuo ng isang chat application, isang magandang unang hakbang ay suriin kung ano ang mayroon na sa labas. Ang paggamit ng SDKs at APIs upang bumuo ng mga chat application ay isang kapaki-pakinabang na estratehiya para sa iba't ibang mga dahilan. Sa pamamagitan ng pagsasama ng mahusay na dokumentadong SDKs at APIs, estratehikong inilalagay mo ang iyong aplikasyon para sa pangmatagalang tagumpay, tinutugunan ang mga alalahanin sa scalability at maintenance.

- **Pinapabilis ang proseso ng pag-unlad at binabawasan ang overhead**: Ang pag-asa sa mga pre-built na functionality sa halip na ang magastos na proseso ng pagbuo ng mga ito sa iyong sarili ay nagbibigay-daan sa iyo na tumuon sa iba pang mga aspeto ng iyong aplikasyon na maaaring mas mahalaga sa iyo, tulad ng business logic.
- **Mas mahusay na pagganap**: Kapag bumubuo ng functionality mula sa simula, sa kalaunan ay tatanungin mo ang iyong sarili "Paano ito nag-scale? May kakayahan ba ang application na ito na humawak ng biglaang pagdagsa ng mga gumagamit?" Ang mga mahusay na pinapanatili na SDK at API ay madalas na may built-in na mga solusyon para sa mga alalahanin na ito.
- **Mas madaling maintenance**: Ang mga update at pagpapabuti ay mas madaling pamahalaan dahil ang karamihan sa mga API at SDK ay nangangailangan lamang ng update sa isang library kapag inilabas ang isang mas bagong bersyon.
- **Pag-access sa pinakabagong teknolohiya**: Ang paggamit ng mga modelong pinino at sinanay sa malawak na mga dataset ay nagbibigay sa iyong aplikasyon ng natural na kakayahan sa wika.

Ang pag-access sa functionality ng isang SDK o API ay karaniwang nagsasangkot ng pagkuha ng pahintulot upang gamitin ang mga ibinigay na serbisyo, na kadalasang sa pamamagitan ng paggamit ng isang natatanging key o authentication token. Gagamitin natin ang OpenAI Python Library upang tuklasin kung ano ang hitsura nito. Maaari mo rin itong subukan sa iyong sarili sa sumusunod na [notebook para sa OpenAI](../../../07-building-chat-applications/python/oai-assignment.ipynb) o [notebook para sa Azure OpenAI Services](../../../07-building-chat-applications/python/aoai-assignment.ipynb) para sa araling ito.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Gumagamit ang halimbawa sa itaas ng GPT-3.5 Turbo model upang makumpleto ang prompt, ngunit pansinin na ang API key ay itinakda bago ito gawin. Makakatanggap ka ng error kung hindi mo itinakda ang key.

## Karanasan ng Gumagamit (UX)

Ang mga pangkalahatang prinsipyo ng UX ay nalalapat sa mga chat application, ngunit narito ang ilang karagdagang pagsasaalang-alang na nagiging partikular na mahalaga dahil sa mga sangkap ng machine learning na kasangkot.

- **Mekanismo para sa pagtugon sa kalabuan**: Paminsan-minsan ay bumubuo ang mga generative AI model ng mga hindi malinaw na sagot. Ang isang tampok na nagbibigay-daan sa mga gumagamit na humingi ng paglilinaw ay maaaring maging kapaki-pakinabang kung sakaling makatagpo sila ng problemang ito.
- **Pagpapanatili ng konteksto**: Ang mga advanced na generative AI model ay may kakayahang tandaan ang konteksto sa loob ng isang pag-uusap, na maaaring maging isang kinakailangang asset sa karanasan ng gumagamit. Ang pagbibigay sa mga gumagamit ng kakayahang kontrolin at pamahalaan ang konteksto ay nagpapabuti sa karanasan ng gumagamit, ngunit nagpapakilala ng panganib ng pagpapanatili ng sensitibong impormasyon ng gumagamit. Ang mga pagsasaalang-alang kung gaano katagal ang impormasyong ito ay naka-imbak, tulad ng pagpapakilala ng isang retention policy, ay maaaring balansehin ang pangangailangan para sa konteksto laban sa privacy.
- **Pag-personalize**: Sa kakayahang matuto at umangkop, nag-aalok ang mga AI model ng isang indibidwal na karanasan para sa isang gumagamit. Ang pag-tailor sa karanasan ng gumagamit sa pamamagitan ng mga tampok tulad ng mga profile ng gumagamit ay hindi lamang nagpaparamdam sa gumagamit na naiintindihan, ngunit nakakatulong din ito sa kanilang paghahanap ng mga tiyak na sagot, na lumilikha ng isang mas mahusay at kasiya-siyang pakikipag-ugnayan.

Ang isang halimbawa ng pag-personalize ay ang "Custom instructions" settings sa OpenAI's ChatGPT. Pinapayagan ka nitong magbigay ng impormasyon tungkol sa iyong sarili na maaaring mahalagang konteksto para sa iyong mga prompt. Narito ang isang halimbawa ng isang custom na instruction.

Ang "profile" na ito ay nag-uudyok sa ChatGPT na lumikha ng isang lesson plan sa mga linked list. Pansinin na isinasaalang-alang ng ChatGPT na maaaring gusto ng gumagamit ng mas detalyadong lesson plan batay sa kanyang karanasan.

### Microsoft's System Message Framework para sa Malalaking Language Models

[Nagbigay ang Microsoft ng gabay](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) para sa pagsusulat ng epektibong mga mensahe ng sistema kapag bumubuo ng mga tugon mula sa LLMs na nahahati sa 4 na mga lugar:

1. Pagpapakahulugan kung sino ang modelo ay para kanino, pati na rin ang mga kakayahan at limitasyon nito.
2. Pagpapakahulugan ng format ng output ng modelo.
3. Pagbibigay ng mga tiyak na halimbawa na nagpapakita ng nilalayong pag-uugali ng modelo.
4. Pagbibigay ng karagdagang mga bantay na kaugalian.

### Accessibility

Kung ang isang gumagamit ay may kapansanan sa paningin, pandinig, motor, o kognitibo, ang isang mahusay na dinisenyong chat application ay dapat na magamit ng lahat. Ang sumusunod na listahan ay nagbabalangkas ng mga partikular na tampok na naglalayong mapahusay ang accessibility para sa iba't ibang mga kapansanan ng gumagamit.

- **Mga Tampok para sa Kapansanan sa Paningin**: Mataas na contrast na mga tema at nare-re-size na teksto, pagiging tugma sa screen reader.
- **Mga Tampok para sa Kapansanan sa Pandinig**: Mga pag-andar ng text-to-speech at speech-to-text, mga visual na pahiwatig para sa mga audio notification.
- **Mga Tampok para sa Kapansanan sa Motor**: Suporta sa nabigasyon ng keyboard, mga utos ng boses.
- **Mga Tampok para sa Kapansanan sa Kognitibo**: Mga opsyon sa pinasimpleng wika.

## Pag-customize at Fine-tuning para sa Mga Modelong Wika na Tiyak sa Domain

Isipin ang isang chat application na nakakaintindi sa jargon ng iyong kumpanya at inaasahan ang mga tiyak na query na karaniwang mayroon ang base ng gumagamit nito. Mayroong ilang mga diskarte na karapat-dapat banggitin:

- **Paggamit ng mga modelong DSL**. Ang DSL ay nangangahulugang domain specific language. Maaari mong gamitin ang isang tinatawag na DSL model na sinanay sa isang tiyak na domain upang maunawaan ang mga konsepto at senaryo nito.
- **Mag-apply ng fine-tuning**. Ang fine-tuning ay ang proseso ng karagdagang pagsasanay sa iyong modelo gamit ang mga partikular na data.

## Pag-customize: Paggamit ng isang DSL

Ang paggamit ng mga domain-specific language models (DSL Models) ay maaaring mapahusay ang pakikipag-ugnayan ng gumagamit at sa pamamagitan ng pagbibigay ng espesyal na mga pakikipag-ugnayan na may konteksto. Ito ay isang modelo na sinanay o pinino upang maunawaan at bumuo ng teksto na may kaugnayan sa isang tiyak na larangan, industriya, o paksa. Ang mga opsyon para sa paggamit ng isang DSL model ay maaaring mag-iba mula sa pagsasanay ng isa mula sa simula, hanggang sa paggamit ng mga umiiral na sa pamamagitan ng SDKs at APIs. Ang isa pang opsyon ay fine-tuning, na kinabibilangan ng pagkuha ng isang umiiral na pre-trained na modelo at pag-angkop nito para sa isang tiyak na domain.

## Pag-customize: Mag-apply ng fine-tuning

Ang fine-tuning ay madalas na isinasaalang-alang kapag ang isang pre-trained na modelo ay kulang sa isang espesyal na domain o tiyak na gawain.

Halimbawa, ang mga query sa medikal ay kumplikado at nangangailangan ng maraming konteksto. Kapag ang isang medikal na propesyonal ay nag-diagnose ng isang pasyente, ito ay batay sa iba't ibang mga kadahilanan tulad ng pamumuhay o umiiral na mga kondisyon, at maaaring umasa pa sa mga kamakailang medikal na journal upang mapatunayan ang kanilang diagnosis. Sa mga ganoong masalimuot na senaryo, ang isang general-purpose na AI chat application ay hindi maaaring maging maaasahang mapagkukunan.

### Scenario: isang medikal na aplikasyon

Isaalang-alang ang isang chat application na idinisenyo upang tulungan ang mga medikal na practitioner sa pamamagitan ng pagbibigay ng mabilis na mga sanggunian sa mga alituntunin sa paggamot, mga interaksyon ng gamot, o mga kamakailang natuklasan sa pananaliksik.

Maaaring sapat ang isang general-purpose na modelo para sa pagsagot sa mga pangunahing tanong sa medisina o pagbibigay ng pangkalahatang payo, ngunit maaari itong mag-struggle sa mga sumusunod:

- **Lubos na tiyak o kumplikadong mga kaso**. Halimbawa, maaaring itanong ng isang neurologist sa application, "Ano ang kasalukuyang pinakamahusay na mga kasanayan para sa pamamahala ng drug-resistant epilepsy sa mga pasyenteng pediatric?"
- **Kulang sa mga kamakailang pagsulong**. Maaaring mag-struggle ang isang general-purpose na modelo na magbigay ng kasalukuyang sagot na nagsasama ng mga pinakabagong pagsulong sa neurology at pharmacology.

Sa mga pagkakataon tulad nito, ang fine-tuning sa modelo gamit ang isang espesyal na medikal na dataset ay maaaring makabuluhang mapabuti ang kakayahan nito na hawakan ang mga masalimuot na medikal na katanungan nang mas tumpak at maaasahan. Nangangailangan ito ng access sa isang malaking at may-kaugnayang dataset na kumakatawan sa mga hamon at tanong na tiyak sa domain na kailangang tugunan.

## Mga Pagsasaalang-alang para sa isang Mataas na Kalidad na Karanasan sa AI-Driven Chat

Ang seksyong ito ay naglalarawan ng mga pamantayan para sa "mataas na kalidad" na mga chat application, na kinabibilangan ng pagkuha ng mga actionable na sukatan at pagsunod sa isang balangkas na responsable na gumagamit ng teknolohiya ng AI.

### Mga Pangunahing Sukatan

Upang mapanatili ang mataas na kalidad ng pagganap ng isang aplikasyon, mahalaga na subaybayan ang mga pangunahing sukatan at pagsasaalang-alang. Ang mga sukatang ito ay hindi lamang tinitiyak ang pag-andar ng aplikasyon kundi sinusuri rin ang kalidad ng modelo ng AI at karanasan ng gumagamit. Nasa ibaba ang isang listahan na sumasaklaw sa mga pangunahing, AI, at sukatan ng karanasan ng gumagamit na dapat isaalang-alang.

| Sukatan                     | Kahulugan                                                                                                          | Mga Pagsasaalang-alang para sa Chat Developer                                 |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Uptime**                  | Sinusukat ang oras na ang aplikasyon ay gumagana at naa-access ng mga gumagamit.                                  | Paano mo babawasan ang downtime?                                             |
| **Response Time**           | Ang oras na kinuha ng aplikasyon upang tumugon sa query ng isang gumagamit.                                       | Paano mo ma-optimize ang pagproseso ng query upang mapabuti ang response time?|
| **Precision**               | Ang ratio ng mga tunay na positibong prediksyon sa kabuuang bilang ng positibong prediksyon                       | Paano mo mapapatunayan ang precision ng iyong modelo?                         |


**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Habang sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpakan. Ang orihinal na dokumento sa sarili nitong wika ang dapat ituring na mapagkakatiwalaang sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-wika ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.