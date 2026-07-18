# Mga Pangunahing Kaalaman sa Prompt Engineering

[![Prompt Engineering Fundamentals](../../../translated_images/tl/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Panimula
Tinatalakay ng modyulong ito ang mahahalagang konsepto at teknik para sa paglikha ng epektibong mga prompt sa mga generative AI na modelo. Mahalaga rin kung paano mo isinusulat ang iyong prompt sa isang LLM. Ang maingat na ginawa na prompt ay maaaring maghatid ng mas mataas na kalidad ng tugon. Pero ano ba talaga ang ibig sabihin ng mga terminong _prompt_ at _prompt engineering_? At paano ko mapapabuti ang prompt _input_ na ipinapadala ko sa LLM? Ito ang mga tanong na susubukan nating sagutin sa kabanatang ito at sa susunod.

_Generative AI_ ay may kakayahang lumikha ng bagong nilalaman (hal., teksto, mga larawan, audio, code, atbp.) bilang tugon sa mga kahilingan ng gumagamit. Nagagawa ito gamit ang _Large Language Models_ tulad ng serye ng OpenAI na GPT ("Generative Pre-trained Transformer") na sinanay para gamitin ang natural na wika at code.

Maaari nang makipag-ugnayan ang mga gumagamit sa mga modelong ito gamit ang mga pamilyar na paradigma tulad ng chat, nang hindi kinakailangan ng teknikal na kasanayan o pagsasanay. Ang mga modelo ay _prompt-based_ - nagpapadala ang mga gumagamit ng text input (prompt) at nakakakuha ng tugon mula sa AI (completion). Maaari silang "makipag-chat sa AI" nang paulit-ulit, sa multi-turn na pag-uusap, pinapahusay ang kanilang prompt hanggang ang tugon ay tumugma sa kanilang inaasahan.

Ang mga "Prompt" ay nagiging pangunahing _programming interface_ para sa mga generative AI app, na nagsasabi sa mga modelo kung ano ang gagawin at nakakaapekto sa kalidad ng mga ibinalik na tugon. Ang "Prompt Engineering" ay isang mabilis na lumalaking larangan na nakatuon sa _disenyo at pag-optimize_ ng mga prompt upang maghatid ng consistent at de-kalidad na mga tugon sa malaking sukat.

## Mga Layunin ng Pagkatuto

Sa araling ito, malalaman natin kung ano ang Prompt Engineering, bakit ito mahalaga, at paano tayo makakagawa ng mas epektibong mga prompt para sa isang partikular na modelo at layunin ng aplikasyon. Mauunawaan natin ang mga pangunahing konsepto at pinakamahusay na kasanayan sa prompt engineering - at matututo tungkol sa isang interactive na kapaligiran ng Jupyter Notebooks "sandbox" kung saan makikita natin ang mga konseptong ito na inilalapat sa mga totoong halimbawa.

Sa pagtatapos ng araling ito, magagawa natin ang mga sumusunod:

1. Ipaliwanag kung ano ang prompt engineering at bakit ito mahalaga.
2. Ilarawan ang mga bahagi ng isang prompt at kung paano ito ginagamit.
3. Matutunan ang mga pinakamahusay na kasanayan at teknik para sa prompt engineering.
4. Iaplay ang mga natutunang teknik sa mga totoong halimbawa, gamit ang OpenAI endpoint.

## Mga Pangunahing Terminolohiya

Prompt Engineering: Ang pagsasanay ng pagdisenyo at pagpino ng mga input upang gabayan ang mga AI model tungo sa paggawa ng mga nais na output.
Tokenization: Proseso ng pag-convert ng teksto sa mas maliliit na yunit, tinatawag na token, na mauunawaan at mapoproseso ng modelo.
Instruction-Tuned LLMs: Mga Large Language Models (LLMs) na pina-fine-tune gamit ang mga partikular na instruksyon upang mapabuti ang katumpakan at kaugnayan ng kanilang tugon.

## Learning Sandbox

Sa kasalukuyan, ang prompt engineering ay higit na sining kaysa agham. Ang pinakamahusay na paraan upang mapabuti ang ating intuwisyon dito ay ang _mas maraming praktis_ at pag-aampon ng trial-and-error na paraan na pinagsasama ang dalubhasang kaalaman sa larangan ng aplikasyon at mga inirerekomendang teknik pati na rin ang mga model-specific optimization.

Ang Jupyter Notebook na kalakip ng araling ito ay nagbibigay ng _sandbox_ na kapaligiran kung saan maaari mong subukan ang iyong mga natutunan - habang nagpapatuloy o bilang bahagi ng code challenge sa dulo. Upang maisagawa ang mga ehersisyo, kakailanganin mo ng:

1. **Isang Azure OpenAI API key** - ang service endpoint para sa isang deployed na LLM.
2. **Isang Python Runtime** - kung saan maaaring patakbuhin ang Notebook.
3. **Mga Lokal na Env Variables** - _kumpletuhin ang mga hakbang sa [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) ngayon upang maging handa_.

Ang notebook ay may kasamang mga _starter_ na ehersisyo - ngunit hinihikayat kang magdagdag ng sarili mong _Markdown_ (paglalarawan) at _Code_ (mga kahilingan sa prompt) na seksyon upang subukan ang higit pang mga halimbawa o ideya - at palawakin ang iyong intuwisyon para sa disenyo ng prompt.

## Gabay na May Ilustrasyon

Nais mo bang makita ang kabuuang larawan ng mga tinatalakay sa araling ito bago ka magsimula? Tignan ang gabay na may ilustrasyon, na nagbibigay sa iyo ng ideya tungkol sa mga pangunahing paksa at mahahalagang puntos na dapat mong pag-isipan sa bawat isa. Ang roadmap ng aralin ay nagsisimula sa pag-unawa sa mga pangunahing konsepto at hamon hanggang sa pagtugon nito gamit ang mga kaugnay na teknik at pinakamahusay na kasanayan sa prompt engineering. Tandaan na ang seksyong "Advanced Techniques" sa gabay na ito ay tumutukoy sa nilalaman na tatalakayin sa _susunod_ na kabanata ng kurikulum na ito.

![Illustrated Guide to Prompt Engineering](../../../translated_images/tl/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Ang Aming Startup

Ngayon, pag-usapan natin kung paano kaugnay ang _paksang ito_ sa aming mission sa startup na [magdala ng AI innovation sa edukasyon](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Nais naming bumuo ng mga AI-powered na aplikasyon para sa _personalized learning_ - kaya pag-isipan natin kung paano maaaring "idisenyo" ng iba't ibang gumagamit ng aming aplikasyon ang mga prompt:

- Maaaring hilingin ng **Mga Administrator** sa AI na _suriin ang data ng kurikulum upang tuklasin ang mga kakulangan sa saklaw_. Maaari nitong buodin ang mga resulta o ipakita ito gamit ang code.
- Maaaring hilingin ng **Mga Guro** sa AI na _gumawa ng lesson plan para sa isang tiyak na target audience at paksa_. Maaari nitong buuin ang personalized na plano sa isang tinakdang format.
- Maaaring hilingin ng **Mga Mag-aaral** sa AI na _magturo sa kanila sa isang mahirap na asignatura_. Maaari na ngayong gabayan ng AI ang mga estudyante gamit ang mga leksyon, mga pahiwatig, at mga halimbawa na angkop sa kanilang antas.

Iyan ay simpleng simula pa lamang. Tignan ang [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - isang open-source na library ng mga prompt na inasikaso ng mga eksperto sa edukasyon - upang magkaroon ng mas malawak na ideya tungkol sa mga posibilidad! _Subukan mong patakbuhin ang ilan sa mga prompt na iyon sa sandbox o gamit ang OpenAI Playground upang makita ang nangyayari!_

<!--
LESSON TEMPLATE:
Dapat talakayin ng unit na ito ang pangunahing konsepto #1.
Patatagin ang konsepto gamit ang mga halimbawa at sanggunian.

KONSEPTO #1:
Prompt Engineering.
Ilarawan ito at ipaliwanag kung bakit ito kailangan.
-->

## Ano ang Prompt Engineering?

Sinimulan natin ang araling ito sa pagdeklara ng **Prompt Engineering** bilang proseso ng _pagdidisenyo at pag-optimize_ ng mga tekstwal na input (mga prompt) upang maghatid ng consistent at de-kalidad na mga tugon (completions) para sa isang layuning aplikasyon at modelo. Maaari natin itong isipin bilang isang dalawang-hakbang na proseso:

- _pagdidisenyo_ ng paunang prompt para sa isang modelo at layunin
- _pagpino_ ng prompt nang paulit-ulit upang mapabuti ang kalidad ng tugon

Ito ay kailangang gawin sa trial-and-error na paraan na nangangailangan ng intuwisyon at pagsisikap ng gumagamit upang makamit ang pinakamainam na resulta. Kaya bakit ito mahalaga? Upang sagutin ang tanong na iyon, kailangan muna nating maunawaan ang tatlong konsepto:

- _Tokenization_ = kung paano "nakikita" ng modelo ang prompt
- _Base LLMs_ = kung paano "pinoproseso" ng foundational na modelo ang prompt
- _Instruction-Tuned LLMs_ = kung paano ngayon "nakikita" ng modelo ang mga "gawain"

### Tokenization

Nakikita ng isang LLM ang mga prompt bilang _sunod-sunod na mga token_ kung saan maaaring i-tokenize ng iba't ibang mga modelo (o mga bersyon ng isang modelo) ang parehong prompt sa iba't ibang paraan. Dahil ang mga LLM ay sinanay gamit ang mga token (hindi raw na teksto), ang paraan ng pag-tokenize sa mga prompt ay may direktang epekto sa kalidad ng nabubuong tugon.

Para magkaroon ng intuwisyon kung paano gumagana ang tokenization, subukan ang mga tool tulad ng [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) na ipinakita sa ibaba. Kopyahin ang iyong prompt - at tingnan kung paano ito na-convert sa tokens, pagtuunan ng pansin kung paano hinahawakan ang mga whitespace character at mga tandang pang-interogasyon. Tandaan na ang halimbawang ito ay nagpapakita ng isang mas lumang LLM (GPT-3) - kaya maaaring magbunga ng ibang resulta kung susubukan sa mas bagong modelo.

![Tokenization](../../../translated_images/tl/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Konsepto: Foundation Models

Kapag ang prompt ay na-tokenize na, ang pangunahing tungkulin ng ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o Foundation model) ay hulaan ang susunod na token sa pagkakasunod-sunod. Dahil sinanay ang mga LLM sa malalaking dataset ng teksto, may sapat na kaalaman sila sa estadistikal na relasyon ng mga token at maaaring gawin ang hula nang may kumpiyansa. Tandaan na hindi nila nauunawaan ang _kahulugan_ ng mga salita sa prompt o token; nakikita lang nila ang isang pattern na maaari nilang "kumpletuhin" sa kanilang susunod na hula. Maaari silang magpatuloy sa paghula ng pagkakasunod-sunod hanggang ito ay ihinto ng gumagamit o ng ilang paunang takdang kondisyon.

Nais mo bang makita kung paano gumagana ang prompt-based completion? Ipasok ang prompt sa itaas sa [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) gamit ang default na mga setting. Nakalagay ang sistema upang ituring ang mga prompt bilang mga kahilingan para sa impormasyon - kaya dapat makakita ka ng completion na naaayon sa kontekstong ito.

Pero paano kung nais ng gumagamit na makita ang isang partikular na bagay na sumusunod sa ilang pamantayan o layunin ng gawain? Dito pumapasok ang mga _instruction-tuned_ na LLM.

![Base LLM Chat Completion](../../../translated_images/tl/04-playground-chat-base.65b76fcfde0caa67.webp)

### Konsepto: Instruction Tuned LLMs

Ang isang [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) ay nagsisimula sa foundation model at pina-fine-tune gamit ang mga halimbawa o pares ng input/output (hal., multi-turn na "mga mensahe") na maaaring naglalaman ng malinaw na mga instruksyon - at sinusubukan ng tugon mula sa AI na sundin ang instruksyon na iyon.

Ginagamit nito ang mga teknik tulad ng Reinforcement Learning with Human Feedback (RLHF) na maaaring sanayin ang modelo upang _sumunod sa mga instruksyon_ at _matuto mula sa feedback_ upang makabuo ng mga tugon na mas angkop sa praktikal na aplikasyon at mas may kaugnayan sa mga layunin ng gumagamit.

Subukan natin ito - balikan ang prompt sa itaas, ngunit palitan ang _system message_ upang magbigay ng sumusunod na instruksyon bilang konteksto:

> _Ibuod ang nilalaman na ibinigay para sa isang estudyante sa ikalawang baitang. Panatilihin ang resulta sa isang talata na may 3-5 na bullet points._

Nakikita mo ba kung paano ngayon naka-tune ang resulta upang ipakita ang nais na layunin at format? Maaari nang direktang gamitin ng guro ang tugon na ito sa kanilang mga slides para sa klase na iyon.

![Instruction Tuned LLM Chat Completion](../../../translated_images/tl/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Bakit Kailangan ang Prompt Engineering?

Ngayon na alam na natin kung paano pinoproseso ng mga LLM ang mga prompt, pag-usapan naman natin kung _bakit_ kailangan natin ng prompt engineering. Ang sagot ay nakasalalay sa katotohanang maraming hamon ang kasalukuyang LLM na nagpapahirap makamit ang _mapagkakatiwalaan at tuloy-tuloy na mga completion_ nang hindi nagsisikap sa pagbuo at pag-optimize ng prompt. Halimbawa:

1. **Ang mga tugon ng modelo ay stochastic.** Ang _parehong prompt_ ay maaaring magbigay ng magkakaibang mga tugon gamit ang iba't ibang mga modelo o bersyon ng modelo. At maaaring magbigay ito ng iba't ibang resulta sa _parehong modelo_ sa iba't ibang oras. _Makakatulong ang mga teknik sa prompt engineering upang mabawasan ang mga pagkakaibang ito sa pamamagitan ng pagbibigay ng mas mahusay na mga guardrails_.

1. **Maaaring gumawa ng mga pekeng tugon ang mga modelo.** Ang mga modelo ay sinanay sa _malalaki ngunit limitado_ na mga dataset, ibig sabihin ay kulang sila sa kaalaman tungkol sa mga konseptong wala sa saklaw ng pagsasanay. Dahil dito, maaari silang makabuo ng mga completion na hindi tama, kathang-isip, o direktang salungat sa mga kilalang katotohanan. _Tinutulungan ng prompt engineering ang mga gumagamit na tuklasin at mabawasan ang mga ganitong fabrication, hal., sa pamamagitan ng pagtatanong sa AI ng mga citation o paliwanag_.

1. **Magkakaiba ang kakayahan ng mga modelo.** Ang mga bagong modelo o bagong henerasyon ng mga modelo ay magkakaroon ng mas malawak na kakayahan ngunit may mga kakaibang katangian at mga tradeoff sa gastos at kumplikasyon. _Makakatulong ang prompt engineering sa pagbuo ng pinakamahusay na kasanayan at mga workflow na nag-aabstra sa mga pagkakaiba at umaangkop sa mga partikular na pangangailangan ng modelo sa scalable at seamless na mga paraan_.

Tingnan natin ito sa aksyon sa OpenAI o Azure OpenAI Playground:

- Gamitin ang parehong prompt sa iba't ibang deployment ng LLM (hal., OpenAI, Azure OpenAI, Hugging Face) - nakita mo ba ang mga pagkakaiba?
- Gamitin paulit-ulit ang parehong prompt sa _parehong_ deployment ng LLM (hal., Azure OpenAI playground) - paano nagkaiba ang mga pagkakaibang ito?

### Halimbawa ng Fabrications

Sa kursong ito, ginagamit namin ang terminong **"fabrication"** upang ilarawan ang phenomenon kung saan minsan ang mga LLM ay nagpapalabas ng mga impormasyong hindi totoo dahil sa mga limitasyon sa pagsasanay o iba pang mga pagsasaalang-alang. Maaring narinig mo na rin itong tawaging _"hallucinations"_ sa mga popular na artikulo o pananaliksik. Gayunpaman, mariin naming inirerekomenda ang paggamit ng _"fabrication"_ bilang termino upang hindi natin aksidenteng pagbibigay-tao sa asal ng makina. Pinalalakas nito ang [Responsible AI guidelines](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) mula sa pananaw ng terminolohiya, na tinatanggal ang mga salitang maaaring ituring na nakasasakit o hindi inclusive sa ilang konteksto.

Nais mo bang makita kung paano gumagana ang mga fabrication? Isipin ang isang prompt na nag-uutos sa AI na gumawa ng nilalaman para sa isang di-umiiral na paksa (upang matiyak na wala ito sa training dataset). Halimbawa - sinubukan ko ang prompt na ito:

> **Prompt:** gumawa ng lesson plan tungkol sa Martian War ng 2076.

Pinakita sa akin ng isang web search na may mga kathang-isip na accounts (hal., TV series o mga libro) tungkol sa mga Martian war - ngunit wala sa taong 2076. Sinasabi rin ng commonsense na ang 2076 ay _sa hinaharap_ kaya hindi ito maiuugnay sa isang totoong pangyayari.


Ano ang nangyayari kapag pinatakbo natin ang prompt na ito gamit ang iba't ibang mga LLM provider?

> **Tugon 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/tl/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Tugon 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/tl/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Tugon 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/tl/04-fabrication-huggingchat.faf82a0a51278956.webp)

Tulad ng inaasahan, bawat modelo (o bersyon ng modelo) ay naglalabas ng bahagyang magkakaibang mga tugon dahil sa stochastic na pag-uugali at mga pagkakaiba sa kakayahan ng modelo. Halimbawa, ang isang modelo ay nakatuon sa isang 8th grade na madla habang ang isa naman ay inaakala ang isang estudyante sa high school. Pero lahat ng tatlong modelo ay nakabuo ng mga tugon na maaaring makumbinsi ang isang hindi pinalamang gumagamit na tunay ang pangyayari.

Maaaring mabawasan ng mga teknik sa prompt engineering tulad ng _metaprompting_ at _temperature configuration_ ang mga peke ng modelo sa ilang antas. Ang mga bagong _arkitektura_ ng prompt engineering ay nagpapaloob din ng mga bagong kasangkapan at teknik nang maayos sa daloy ng prompt, upang mapagaan o mabawasan ang ilan sa mga epekto nito.

## Pag-aaral ng Kaso: GitHub Copilot

Tapusin natin ang seksyong ito sa pamamagitan ng pagkuha ng ideya kung paano ginagamit ang prompt engineering sa mga totoong solusyon sa pamamagitan ng pagtingin sa isang Pag-aaral ng Kaso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

Ang GitHub Copilot ay ang iyong "AI Pair Programmer" - ito ay nagko-convert ng mga text prompt sa mga kompletong code at naka-integrate sa iyong development environment (hal., Visual Studio Code) para sa isang tuloy-tuloy na karanasan ng gumagamit. Tulad ng naidokumento sa serye ng mga blog sa ibaba, ang pinakaunang bersyon ay nakabase sa OpenAI Codex na modelo - kung saan mabilis na naunawaan ng mga engineer ang pangangailangan na i-fine-tune ang modelo at bumuo ng mas magagandang teknik sa prompt engineering, para mapabuti ang kalidad ng code. Noong Hulyo, kanilang [ipinakilala ang isang pinabuting AI model na lampas sa Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sa mas mabilis na mga suhestiyon.

Basahin ang mga post nang sunud-sunod, para masundan ang kanilang paglalakbay sa pagkatuto.

- **Mayo 2023** | [Mas Ginagaling ng GitHub Copilot ang Pag-unawa sa Iyong Code](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mayo 2023** | [Sa Loob ng GitHub: Pagtatrabaho sa mga LLMs sa likod ng GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Hunyo 2023** | [Paano sumulat ng mas magagandang prompt para sa GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Hulyo 2023** | [.. Ang GitHub Copilot ay lampas sa Codex gamit ang pinahusay na AI model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Hulyo 2023** | [Isang Gabay ng Developer sa Prompt Engineering at LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Setyembre 2023** | [Paano bumuo ng enterprise LLM app: Mga Aral mula sa GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Maaari ka ring mag-browse sa kanilang [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para sa iba pang mga post tulad ng [ito](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) na nagpapakita kung paano _ina-aplay_ ang mga modelong ito at teknik para itulak ang mga totoong aplikasyon.

---

<!--
LESSON TEMPLATE:
Ang yunit na ito ay dapat sumaklaw sa core concept #2.
Patibayin ang konsepto gamit ang mga halimbawa at sanggunian.

KONCEPTO #2:
Disenyo ng Prompt.
Ipinakita sa pamamagitan ng mga halimbawa.
-->

## Pagbuo ng Prompt

Nakita na natin kung bakit mahalaga ang prompt engineering - ngayon, unawain natin kung paano _binubuo_ ang mga prompt para masuri natin ang iba't ibang teknik para sa mas epektibong disenyo ng prompt.

### Pangunahing Prompt

Magsimula tayo sa pangunahing prompt: isang text input na ipinapadala sa modelo na walang ibang konteksto. Narito ang isang halimbawa - kapag ipinadala natin ang unang ilang salita ng US national anthem sa OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) ito ay agad na _kinukumpleto_ ang tugon ng mga susunod na linya, na nagpapakita ng pangunahing pag-uugali ng prediksyon.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Mukhang sinisimulan mo ang mga liriko ng "The Star-Spangled Banner," ang pambansang awit ng Estados Unidos. Ang buong liriko ay ...       |

### Masalimuot na Prompt

Ngayon dagdagan natin ng konteksto at mga tagubilin ang pangunahing prompt na iyon. Pinahihintulutan tayo ng [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) na bumuo ng masalimuot na prompt bilang isang koleksyon ng mga _mensaheng_ may:

- mga pares ng input/output na sumasalamin sa input ng _user_ at tugon ng _assistant_.
- Mensahe ng system na nagse-set ng konteksto para sa pagkilos o personalidad ng assistant.

Ang request ay nasa anyo ngayon sa ibaba, kung saan ang _tokenization_ ay epektibong kinukuha ang kaugnay na impormasyon mula sa konteksto at pag-uusap. Ngayon, ang pagbabago sa konteksto ng sistema ay maaaring kasing epektibo sa kalidad ng mga kompletong tugon, gaya ng ibinigay na mga input ng user.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instruction Prompt

Sa mga halimbawa sa itaas, ang user prompt ay isang simpleng text query na maaaring bigyang-kahulugan bilang isang kahilingan para sa impormasyon. Sa _instruction_ prompts, maaari nating gamitin ang text na iyon upang tukuyin ang isang gawain nang mas detalyado, na nagbibigay ng mas mahusay na gabay sa AI. Narito ang isang halimbawa:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Uri ng Tagubilin   |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Isulat ang isang paglalarawan tungkol sa Civil War                                                                                                                                                                                    | _nagbalik ng isang simpleng talata_                                                                                        | Simple              |
| Isulat ang isang paglalarawan tungkol sa Civil War. Ibigay ang mga susi na petsa at pangyayari at ilarawan ang kanilang kahalagahan                                                                                                     | _nagbalik ng talata na sinundan ng listahan ng mga susi na petsa ng pangyayari na may mga paglalarawan_                      | Masalimuot           |
| Isulat ang isang paglalarawan tungkol sa Civil War sa 1 talata. Magbigay ng 3 bullet points na may mga susi na petsa at kanilang kahalagahan. Magbigay ng 3 pang bullet points na may mga susi na tauhan sa kasaysayan at kanilang mga kontribusyon. Ibalik ang output bilang JSON file | _nagbabalik ng mas detalyadong nilalaman sa isang kahon ng teksto, naka-format bilang JSON na maaari mong kopyahin at i-paste sa file at i-validate kung kinakailangan_ | Masalimuot. Naka-format. |

## Pangunahing Nilalaman

Sa mga halimbawa sa itaas, ang prompt ay medyo bukas pa rin, pinapahintulutan ang LLM na magpasya kung aling bahagi ng pre-trained na dataset nito ang kaugnay. Sa _primary content_ na disenyo, ang input na teksto ay hinahati sa dalawang bahagi:

- isang tagubilin (gawain)
- kaugnay na nilalaman (na nakaaapekto sa gawain)

Narito ang isang halimbawa kung saan ang tagubilin ay "buodin ito sa 2 pangungusap".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ang Jupiter ay ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Solar System. Isa itong gas giant na may mass na isang libong bahagi ng mass ng Araw, ngunit dalawang-kalahati beses ng kabuuan ng mga iba pang planeta sa Solar System. Ang Jupiter ay isa sa mga pinakamaliwanag na bagay na nakikita ng hubad na mata sa gabi, at kilala na ng mga sinaunang sibilisasyon bago pa man ang nakatala na kasaysayan. Pinangalanan ito mula sa Roman god na Jupiter.[19] Kapag tinitingnan mula sa Earth, ang Jupiter ay maaaring sapat ang liwanag para magbali ng mga anino, [20] at karaniwang ang pangatlong pinakamaliwanag na bagay sa kalangitan sa gabi pagkatapos ng Buwan at Venus. <br/> **Buodin ito sa 2 pinaikling pangungusap** | Ang Jupiter, ang ikalimang planeta mula sa Araw, ay ang pinakamalaki sa Solar System at kilala bilang isa sa mga pinakamaliwanag na bagay sa kalangitan sa gabi. Pinangalanan ito sa Roman god na Jupiter, ito ay isang gas giant na ang mass ay dalawang-kalahating beses ng lahat ng ibang planeta sa Solar System na pinagsama-sama. |

Ang pangunahing bahagi ng nilalaman ay maaaring gamitin sa iba't ibang paraan para makagawa ng mas epektibong mga tagubilin:

- **Mga Halimbawa** - sa halip na sabihin sa modelo kung ano ang gagawin gamit ang isang hayagang tagubilin, bigyan ito ng mga halimbawa kung ano ang gagawin at hayaan itong tuklasin ang pattern.
- **Mga Cue** - sundan ang tagubilin ng isang "cue" na pinasisigla ang kompletong tugon, ginagabayan ang modelo patungo sa mga mas kaugnay na tugon.
- **Mga Template** - ito ang mga paulit-ulit na 'recipe' para sa mga prompt na may mga placeholder (variable) na maaaring baguhin gamit ang datos para sa tiyak na mga gamit.

Tingnan natin ang mga ito sa aksyon.

### Paggamit ng Mga Halimbawa

Ito ay isang pamamaraan kung saan ginagamit mo ang pangunahing nilalaman para "pakainin ang modelo" ng ilang mga halimbawa ng nais na output para sa isang tagubilin, at hayaan itong tuklasin ang pattern para sa nais na output. Batay sa bilang ng mga ibinigay na halimbawa, maaari tayong magkaroon ng zero-shot prompting, one-shot prompting, few-shot prompting, atbp.

Ang prompt ay binubuo na ngayon ng tatlong bahagi:

- Isang deskripsyon ng gawain
- Ilang halimbawa ng nais na output
- Simula ng isang bagong halimbawa (na nagiging implicit na deskripsyon ng gawain)

| Uri ng Pagkatuto | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "Ang Araw ay Nagniningning". Isalin sa Spanish                                                                                                      | "El Sol está brillando".    |
| One-shot      | "Ang Araw ay Nagniningning" => ""El Sol está brillando". <br> "Ito ay Malamig at Maalimpung Araw" =>                                                  | "Es un día frío y ventoso". |
| Few-shot      | Tumakbo ang manlalaro sa mga base => Baseball <br/> Tumama ang manlalaro ng ace => Tennis <br/> Tumama ang manlalaro ng six => Cricket <br/> Nagslam-dunk ang manlalaro => | Basketball                  |
|               |                                                                                                                                                       |                             |

Pansinin kung paano kailangang magbigay ng hayagang tagubilin ("Isalin sa Spanish") sa zero-shot prompting, ngunit ito ay natutuklasan sa halimbawa ng one-shot prompting. Ipinakita ng halimbawa ng few-shot kung paano ang pagdagdag ng mas maraming halimbawa ay nagpapahintulot sa mga modelo na gumawa ng mas tumpak na mga konklusyon nang walang dagdag na mga tagubilin.

### Mga Cue sa Prompt

Isa pang teknik para sa paggamit ng pangunahing nilalaman ay ang magbigay ng _mga cue_ sa halip na mga halimbawa. Sa kasong ito, binibigyan natin ang modelo ng isang panimulang pahiwatig sa tamang direksyon sa pamamagitan ng _pagsisimula nito_ sa isang snippet na nagpapakita ng nais na uri ng tugon. Pagkatapos, "kinukuha ng modelo ang cue" para ipagpatuloy sa ganoong estilo.

| Bilang ng Cue | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Ang Jupiter ay ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Solar System. Isa itong gas giant na may mass na isang libong bahagi ng mass ng Araw, ngunit dalawang-kalahati beses ng kabuuan ng mga iba pang planeta sa Solar System. Ang Jupiter ay isa sa mga pinakamaliwanag na bagay na nakikita ng hubad na mata sa gabi, at kilala na ng mga sinaunang sibilisasyon bago pa man ang nakatala na kasaysayan. <br/>**Buodin Ito**                                       | Ang Jupiter ang pinakamalaking planeta sa ating Solar System at ang ikalimang planeta mula sa Araw. Ito ay isang gas giant na may mass na 1/1000 ng mass ng Araw, ngunit mas mabigat kaysa sa lahat ng iba pang mga planeta na pinagsama-sama. Matagal nang alam ito ng mga sinaunang sibilisasyon, at madali itong makita sa kalangitan sa gabi. |
| 1              | Ang Jupiter ay ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Solar System. Isa itong gas giant na may mass na isang libong bahagi ng mass ng Araw, ngunit dalawang-kalahati beses ng kabuuan ng mga iba pang planeta sa Solar System. Ang Jupiter ay isa sa mga pinakamaliwanag na bagay na nakikita ng hubad na mata sa gabi, at kilala na ng mga sinaunang sibilisasyon bago pa man ang nakatala na kasaysayan. <br/>**Buodin Ito** <br/> Ang natutunan namin ay ang Jupiter | ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Solar System. Isa itong gas giant na may mass na isang libong bahagi ng mass ng Araw, ngunit dalawang-kalahati beses ng kabuuan ng mga iba pang planeta na pinagsama-sama. Madali itong makita ng hubad na mata at kilala na mula pa noong sinaunang panahon.                       |

| 2              | Ang Jupiter ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Solar System. Isa itong gas giant na may masa na isang libong bahagi ng masa ng Araw, ngunit dalawang beses at kalahati ng masa ng lahat ng iba pang mga planeta sa Solar System na pinagsama. Ang Jupiter ay isa sa mga pinakamaliwanag na bagay na nakikita ng hubad na mata sa kalangitan sa gabi, at kilala na ito ng mga sinaunang sibilisasyon bago pa man ang nakasulat na kasaysayan. <br/>**Buod ng Ito** <br/> Nangungunang 3 Katotohanang Natutunan:         | 1. Ang Jupiter ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Solar System. <br/> 2. Isa itong gas giant na may masa na isang libong bahagi ng masa ng Araw...<br/> 3. Nakikita ang Jupiter ng hubad na mata mula pa sa sinaunang panahon ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Mga Template ng Prompt

Ang isang prompt template ay isang _pre-defined na resipi para sa isang prompt_ na maaaring itago at magamit muli ayon sa pangangailangan, upang maghatid ng mas consistent na karanasan ng gumagamit sa malakihang paraan. Sa pinakasimpleng anyo, ito ay isang koleksyon ng mga halimbawa ng prompt tulad ng [ito mula sa OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) na nagbibigay ng parehong bahagi ng interactive prompt (mga mensahe ng user at sistema) at ang format ng kahilingan na pinapatakbo ng API - upang suportahan ang muling paggamit.

Sa mas kumplikadong anyo nito tulad ng [halimbawa mula sa LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), naglalaman ito ng _mga placeholder_ na maaaring palitan ng datos mula sa iba't ibang pinagkukunan (input ng user, konteksto ng sistema, panlabas na pinagkukunan ng datos, atbp.) upang makabuo ng prompt nang dinamiko. Pinapayagan tayo nitong bumuo ng isang library ng mga reusable na prompt na maaaring gamitin upang magdala ng consistent na karanasan ng gumagamit **programmatically** sa malakihang paraan.

Sa huli, ang tunay na halaga ng mga template ay nasa kakayahan nitong lumikha at maglathala ng mga _prompt library_ para sa mga partikular na larangan ng aplikasyon - kung saan ang prompt template ay ngayon _optimized_ upang ipakita ang konteksto o mga halimbawa na partikular sa aplikasyon na nagpapahusay sa pagiging angkop at katumpakan ng mga sagot para sa target na audience na gumagamit. Ang [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository ay isang magandang halimbawa ng ganitong paraan, na nag-aayos ng isang library ng mga prompt para sa larangan ng edukasyon na may diin sa mga pangunahing layunin tulad ng pagplano ng aralin, disenyo ng kurikulum, pagtuturo sa estudyante, atbp.

## Sumusuportang Nilalaman

Kung ituturing natin ang konstruksyon ng prompt bilang pagkakaroon ng isang instruksiyon (gawain) at isang target (pangunahing nilalaman), ang _pangalawang nilalaman_ ay parang karagdagang konteksto na ibinibigay natin upang **impluwensyahan ang output sa isang paraan**. Maaaring ito ay mga setting para sa tuning, mga tagubilin sa pag-format, taxonomy ng mga paksa, atbp. na makakatulong sa modelo upang _ayusin_ ang tugon nito upang umangkop sa nais na layunin o inaasahan ng gumagamit.

Halimbawa: Given ang isang katalogo ng kurso na may malawak na metadata (pangalan, paglalarawan, antas, metadata tags, instruktor, atbp.) sa lahat ng magagamit na kurso sa kurikulum:

- maaari tayong magtakda ng instruksiyon na "buodin ang katalogo ng kurso para sa Fall 2023"
- maaari nating gamitin ang pangunahing nilalaman upang magbigay ng ilang halimbawa ng nais na output
- maaari nating gamitin ang pangalawang nilalaman upang tukuyin ang nangungunang 5 "tag" na interesado.

Ngayon, maaring magbigay ang modelo ng buod sa format na ipinakita ng ilang halimbawa - ngunit kung ang resulta ay may maraming tag, maaaring unahin nito ang 5 tag na tinukoy sa pangalawang nilalaman.

---

<!--
TEMPLATE NG ARALIN:
Dapat saklawin ng yunit na ito ang pangunahing konsepto #1.
Patatagin ang konsepto sa pamamagitan ng mga halimbawa at reperensya.

KONSEPTONG #3:
Mga Teknik sa Prompt Engineering.
Ano ang ilang mga pangunahing teknik para sa prompt engineering?
Ilahad ito sa pamamagitan ng ilang mga ehersisyo.
-->

## Mga Pinakamahusay na Gawain sa Prompting

Ngayon na alam na natin kung paano _buoin_ ang mga prompt, maaari na nating simulan isipin kung paano _idisenyo_ ang mga ito upang ipakita ang pinakamahusay na gawain. Maaari nating isipin ito sa dalawang bahagi - pagkakaroon ng tamang _mindset_ at paggamit ng tamang _mga teknik_.

### Mindset sa Prompt Engineering

Ang Prompt Engineering ay isang proseso ng pagsubok at pagwawasto kaya't panatilihin ang tatlong malawak na gabay na mga salik sa isip:

1. **Mahalaga ang Pag-unawa sa Domain.** Ang katumpakan at pagiging angkop ng tugon ay isang function ng _domain_ kung saan gumagana ang aplikasyon o gumagamit. I-apply ang iyong intuwisyon at kadalubhasaan sa domain upang **i-customize pa ang mga teknik**. Halimbawa, tukuyin ang _mga personalidad na partikular sa domain_ sa iyong mga system prompt, o gamitin ang _mga template na partikular sa domain_ sa iyong mga user prompt. Magbigay ng pangalawang nilalaman na nagpapakita ng mga kontekstong partikular sa domain, o gamitin ang _mga palatandaan at halimbawa na partikular sa domain_ upang gabayan ang modelo patungo sa pamilyar na mga pattern ng paggamit.

2. **Mahalaga ang Pag-unawa sa Modelo.** Alam natin na ang mga modelo ay stochastic sa kalikasan. Ngunit ang mga implementasyon ng modelo ay maaari ring magkakaiba sa paggamit ng dataset ng pagsasanay nila (pre-trained na kaalaman), sa mga kakayahan na kanilang ibinibigay (hal., sa pamamagitan ng API o SDK) at uri ng nilalamang kanilang pinagpapahusay (hal., code vs. mga larawan vs. teksto). Unawain ang mga kalakasan at limitasyon ng modelong iyong ginagamit, at gamitin ang kaalamang iyon upang _unahin ang mga gawain_ o bumuo ng _customized na mga template_ na optimized para sa mga kakayahan ng modelo.

3. **Mahalaga ang Iterasyon at Pagsusuri.** Ang mga modelo ay mabilis na nagbabago, gayundin ang mga teknik para sa prompt engineering. Bilang isang dalubhasa sa domain, maaaring mayroon kang ibang konteksto o mga pamantayan para sa _iyong_ partikular na aplikasyon, na maaaring hindi naaangkop sa mas malawak na komunidad. Gamitin ang mga kagamitan at teknik sa prompt engineering upang "umpisahan agad" ang konstruksyon ng prompt, pagkatapos ay ulitin at suriin ang mga resulta gamit ang iyong sariling intuwisyon at kadalubhasaan sa domain. Itala ang iyong mga pananaw at lumikha ng isang **kaalaman base** (hal., mga library ng prompt) na maaaring gamitin bilang bagong panimulang punto ng iba, para sa mas mabilis na mga iterasyon sa hinaharap.

## Pinakamahusay na Gawain

Tingnan natin ngayon ang mga karaniwang pinakamahusay na gawain na inirerekomenda ng mga practitioner mula sa [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) at [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Ano                               | Bakit                                                                                                                                                                                                                                             |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Suriin ang mga pinakabagong modelo. | Ang mga bagong henerasyon ng modelo ay malamang na may pinahusay na mga tampok at kalidad - ngunit maaaring magdulot din ng mas mataas na mga gastusin. Suriin ang mga ito para sa epekto, pagkatapos gumawa ng mga desisyon sa paglipat.             |
| Paghiwalayin ang mga instruksiyon at konteksto  | Tingnan kung ang iyong modelo/provider ay nagtatakda ng _mga delimiter_ upang mas malinaw na maibangon ang mga instruksiyon, pangunahing nilalaman at pangalawang nilalaman. Makakatulong ito sa mga modelo na magtalaga ng mga bigat nang mas tama sa mga token. |
| Maging tiyak at malinaw             | Magbigay ng higit pang detalye tungkol sa nais na konteksto, kinalabasan, haba, format, istilo, atbp. Ito ay magpapabuti sa parehong kalidad at pagiging consistent ng mga tugon. Itala ang mga resipi sa mga reusable na template.                   |
| Maging mahahabong paglalarawan, gumamit ng mga halimbawa | Maaaring mas mahusay tumugon ang mga modelo sa isang "ipakita at ikuwento" na pamamaraan. Simulan sa `zero-shot` na pamamaraan kung saan bibigyan mo ito ng isang instruksiyon (ngunit walang mga halimbawa) pagkatapos subukang `few-shot` bilang pagpipino, magbigay ng ilang mga halimbawa ng nais na output. Gumamit ng mga analohiya. |
| Gumamit ng mga palatandaan upang pasimulan ang mga kompletong tugon| Itulak ito patungo sa nais na kinalabasan sa pamamagitan ng pagbibigay ng ilang mga unang salita o parirala na maaari nitong gamitin bilang panimulang punto ng tugon.                                                                       |
| Ulitin                          | Minsan maaaring kailanganin mong ulitin ang iyong sarili sa modelo. Magbigay ng mga tagubilin bago at pagkatapos ng iyong pangunahing nilalaman, gumamit ng isang instruksiyon at isang palatandaan, atbp. Ulitin at suriin kung ano ang gumagana. |
| Mahalaga ang pagkakasunod-sunod     | Ang pagkakasunod-sunod ng pagpapakita ng impormasyon sa modelo ay maaaring makaapekto sa output, kahit sa mga halimbawa ng pagkatuto, dahil sa recency bias. Subukan ang iba't ibang mga opsyon upang makita kung ano ang pinakaepektibo.              |
| Bigyan ang modelo ng “labasan”       | Bigyan ang modelo ng isang _fallback_ na tugon na maaari nitong magamit kung hindi ito makumpleto ang gawain sa anumang dahilan. Makakatulong ito upang mabawasan ang posibilidad na makabuo ang mga modelo ng maling o gawa-gawang mga sagot.           |
|                                   |                                                                                                                                                                                                                                                 |

Tulad ng anumang pinakamahusay na gawain, tandaan na _maaaring mag-iba ang iyong karanasan_ base sa modelo, gawain at domain. Gamitin ang mga ito bilang panimulang punto, at ulitin upang mahanap kung ano ang pinakamainam para sa iyo. Patuloy na suriin muli ang iyong proseso ng prompt engineering habang may mga bagong modelo at mga kasangkapan na nagiging magagamit, na nakatuon sa scalability ng proseso at kalidad ng tugon.

<!--
TEMPLATE NG ARALIN:
Dapat magbigay ang yunit na ito ng hamon sa code kung naaangkop

HAMON:
Link sa isang Jupyter Notebook na may mga komento lang sa code sa mga instruksiyon (walang laman ang mga bahagi ng code).

SOLUSYON:
Link sa kopya ng Notebook na iyon na may mga punong prompt at na-run, na nagpapakita kung ano ang isang halimbawa.
-->

## Takdang Aralin

Congratulations! Nakaraos ka sa dulo ng aralin! Panahon na para subukan ang ilan sa mga konsepto at teknik na iyon gamit ang mga totoong halimbawa!

Para sa ating takdang aralin, gagamit tayo ng isang Jupyter Notebook na may mga ehersisyo na maaari mong tapusin nang interaktibo. Maaari mo ring palawakin ang Notebook gamit ang iyong sariling mga Markdown at Code cell upang tuklasin ang mga ideya at teknik nang mag-isa.

### Upang makapagsimula, i-fork ang repo, pagkatapos

- (Inirerekomenda) Ilunsad ang GitHub Codespaces
- (Opsyonal) I-clone ang repo sa iyong lokal na device at gamitin ito sa Docker Desktop
- (Opsyonal) Buksan ang Notebook gamit ang paborito mong Notebook runtime environment.

### Sunod, i-configure ang iyong mga environment variable

- Kopyahin ang `.env.copy` na file sa root ng repo papuntang `.env` at punan ang mga halaga ng `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` at `AZURE_OPENAI_DEPLOYMENT`. Bumalik sa [Learning Sandbox section](#learning-sandbox) para malaman kung paano.

### Sunod, buksan ang Jupyter Notebook

- Piliin ang runtime kernel. Kung gamit ang opsyon 1 o 2, piliin lang ang default na Python 3.10.x kernel na ibinibigay ng dev container.

Handa ka nang patakbuhin ang mga ehersisyo. Tandaan na walang _tama at maling_ sagot dito - pagtuklas lang ng mga opsyon sa pamamagitan ng trial-and-error at pagbuo ng intuwisyon kung ano ang gumagana para sa isang tiyak na modelo at domain ng aplikasyon.

_Dahil dito, walang mga Segment ng Solusyon sa Code sa araling ito. Sa halip, ang Notebook ay magkakaroon ng mga Markdown cell na may pamagat na "My Solution:" na nagpapakita ng isang halimbawa ng output para sa sanggunian._

 <!--
TEMPLATE NG ARALIN:
Balutin ang seksyon ng isang buod at mga resources para sa sariling pag-aaral.
-->

## Pagsusuri ng Kaalaman

Alin sa mga sumusunod ang isang magandang prompt na sumusunod sa ilang makatuwirang mga pinakamahusay na gawain?

1. Ipakita sa akin ang larawan ng pulang kotse
2. Ipakita sa akin ang larawan ng pulang kotse na may make na Volvo at modelong XC90 na nakaparada sa tabi ng bangin habang lumulubog ang araw
3. Ipakita sa akin ang larawan ng pulang kotse na may make na Volvo at modelong XC90

A: 2, ito ang pinakamahusay na prompt dahil nagbibigay ito ng detalye sa "ano" at pumapasok sa mga partikular (hindi lang basta kotse kundi isang tiyak na make at modelo) at inilarawan din ang pangkalahatang setting. Ang 3 ang pangalawa sa ganda dahil naglalaman din ito ng maraming paglalarawan.

## 🚀 Hamon

Tingnan kung magagamit mo ang teknik na "cue" sa prompt: Kumpletuhin ang pangungusap "Ipakita sa akin ang larawan ng pulang kotse na may make na Volvo at ". Ano ang sasagot nito, at paano mo ito mapapabuti?

## Mahusay na Trabaho! Ipagpatuloy ang Iyong Pag-aaral

Gusto mo bang matuto nang higit pa tungkol sa iba't ibang konsepto ng Prompt Engineering? Pumunta sa [patuloy na pahina ng pag-aaral](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para makahanap ng iba pang magagandang resources tungkol sa paksang ito.

Pumunta sa Lesson 5 kung saan titingnan natin ang [advanced na mga teknik sa prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->