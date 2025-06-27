<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T13:13:23+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "tl"
}
-->
# Mga Batayang Konsepto ng Prompt Engineering

## Panimula
Ang module na ito ay sumasaklaw sa mga mahahalagang konsepto at teknik para sa paglikha ng epektibong mga prompt sa mga generative AI models. Mahalaga rin ang paraan ng pagsusulat mo ng prompt sa isang LLM. Ang maingat na pagbuo ng prompt ay maaaring makamit ang mas mahusay na kalidad ng tugon. Ngunit ano nga ba ang kahulugan ng mga terminong _prompt_ at _prompt engineering_? At paano ko mapapabuti ang prompt _input_ na ipinapadala ko sa LLM? Ito ang mga tanong na susubukan nating sagutin sa kabanatang ito at sa susunod.

Ang _Generative AI_ ay may kakayahang lumikha ng bagong nilalaman (halimbawa, teksto, mga larawan, audio, code, atbp.) bilang tugon sa mga kahilingan ng gumagamit. Nakakamit ito gamit ang _Large Language Models_ tulad ng serye ng GPT ("Generative Pre-trained Transformer") ng OpenAI na sinanay para sa paggamit ng natural na wika at code.

Maaaring makipag-ugnayan ang mga gumagamit sa mga modelong ito gamit ang mga pamilyar na paradigma tulad ng chat, nang hindi nangangailangan ng anumang teknikal na kaalaman o pagsasanay. Ang mga modelo ay _prompt-based_ - ang mga gumagamit ay nagpapadala ng input na teksto (prompt) at bumabalik ang tugon ng AI (completion). Maaari silang "makipag-chat sa AI" nang paulit-ulit, sa multi-turn na mga pag-uusap, pinapino ang kanilang prompt hanggang sa ang tugon ay tumutugma sa kanilang mga inaasahan.

Ang "Prompts" ngayon ay nagiging pangunahing _programming interface_ para sa mga generative AI apps, nagsasabi sa mga modelo kung ano ang gagawin at nakakaapekto sa kalidad ng mga tugon na ibinabalik. Ang "Prompt Engineering" ay isang mabilis na lumalaking larangan ng pag-aaral na nakatuon sa _disenyo at pag-optimize_ ng mga prompt upang makapaghatid ng pare-pareho at kalidad na mga tugon sa malakihang saklaw.

## Mga Layunin sa Pag-aaral

Sa araling ito, matututunan natin kung ano ang Prompt Engineering, bakit ito mahalaga, at paano tayo makakagawa ng mas epektibong mga prompt para sa isang ibinigay na modelo at layunin ng aplikasyon. Mauunawaan natin ang mga pangunahing konsepto at pinakamahusay na kasanayan para sa prompt engineering - at matutunan ang tungkol sa isang interactive na "sandbox" environment ng Jupyter Notebooks kung saan natin makikita ang mga konseptong ito na inilalapat sa mga totoong halimbawa.

Sa pagtatapos ng araling ito, magagawa natin ang:

1. Ipaliwanag kung ano ang prompt engineering at bakit ito mahalaga.
2. Ilarawan ang mga bahagi ng isang prompt at paano ito ginagamit.
3. Matutunan ang pinakamahusay na kasanayan at teknik para sa prompt engineering.
4. Ilapat ang mga natutunang teknik sa mga totoong halimbawa, gamit ang isang OpenAI endpoint.

## Mga Pangunahing Termino

Prompt Engineering: Ang kasanayan ng pagdidisenyo at pagpino ng mga input upang gabayan ang mga AI models patungo sa paglikha ng mga nais na output.
Tokenization: Ang proseso ng pag-convert ng teksto sa mas maliliit na yunit, tinatawag na tokens, na maaaring maunawaan at ma-proseso ng isang modelo.
Instruction-Tuned LLMs: Mga Large Language Models (LLMs) na na-fine-tune gamit ang mga tiyak na instruksyon upang mapabuti ang kanilang katumpakan at kaugnayan ng tugon.

## Learning Sandbox

Ang prompt engineering ay kasalukuyang mas sining kaysa agham. Ang pinakamahusay na paraan upang mapabuti ang ating intuition para dito ay ang _mas maraming pagsasanay_ at pag-aampon ng trial-and-error na diskarte na pinagsasama ang kaalaman sa domain ng aplikasyon sa mga inirerekomendang teknik at mga partikular na pag-optimize ng modelo.

Ang Jupyter Notebook na kasama ng araling ito ay nagbibigay ng isang _sandbox_ environment kung saan maaari mong subukan ang iyong natutunan - habang ikaw ay nagpapatuloy o bilang bahagi ng code challenge sa dulo. Upang maisagawa ang mga ehersisyo, kakailanganin mo:

1. **Isang Azure OpenAI API key** - ang service endpoint para sa isang deployed LLM.
2. **Isang Python Runtime** - kung saan maaaring maisagawa ang Notebook.
3. **Mga Lokal na Env Variables** - _kumpletuhin ang [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) na mga hakbang ngayon upang maging handa_.

Ang notebook ay may kasamang _starter_ exercises - ngunit hinihikayat kang magdagdag ng sarili mong _Markdown_ (description) at _Code_ (prompt requests) na mga seksyon upang subukan ang mas maraming mga halimbawa o ideya - at bumuo ng iyong intuition para sa disenyo ng prompt.

## Illustrated Guide

Gusto mo bang makuha ang pangkalahatang ideya ng kung ano ang saklaw ng araling ito bago ka sumabak? Tingnan ang illustrated guide na ito, na nagbibigay sa iyo ng ideya ng mga pangunahing paksa na saklaw at ang mga pangunahing takeaway para sa iyo na pag-isipan sa bawat isa. Ang roadmap ng aralin ay dadalhin ka mula sa pag-unawa sa mga pangunahing konsepto at hamon patungo sa pagtugon sa mga ito gamit ang mga nauugnay na teknik sa prompt engineering at pinakamahusay na kasanayan. Tandaan na ang seksyong "Advanced Techniques" sa gabay na ito ay tumutukoy sa nilalaman na saklaw sa _susunod_ na kabanata ng kurikulum na ito.

## Ang aming Startup

Ngayon, pag-usapan natin kung paano _ang paksang ito_ ay nauugnay sa aming misyon sa startup na [magdala ng AI innovation sa edukasyon](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Nais naming bumuo ng mga AI-powered na aplikasyon ng _personalized learning_ - kaya't isipin natin kung paano maaaring "magdisenyo" ng mga prompt ang iba't ibang mga gumagamit ng aming aplikasyon:

- **Mga Administrator** ay maaaring hilingin sa AI na _i-analyze ang data ng kurikulum upang matukoy ang mga puwang sa saklaw_. Maaaring ibuod ng AI ang mga resulta o i-visualize ang mga ito gamit ang code.
- **Mga Edukador** ay maaaring hilingin sa AI na _bumuo ng isang lesson plan para sa target na audience at paksa_. Maaaring bumuo ang AI ng personalized na plano sa isang tinukoy na format.
- **Mga Mag-aaral** ay maaaring hilingin sa AI na _tutor sila sa isang mahirap na paksa_. Maaaring gabayan ngayon ng AI ang mga mag-aaral sa mga aralin, pahiwatig, at mga halimbawa na naiaangkop sa kanilang antas.

Iyan ay ang simula pa lamang. Tingnan ang [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - isang open-source na prompts library na na-curate ng mga eksperto sa edukasyon - upang makakuha ng mas malawak na ideya ng mga posibilidad! _Subukang patakbuhin ang ilan sa mga prompt na iyon sa sandbox o gamitin ang OpenAI Playground upang makita kung ano ang mangyayari!_

## Ano ang Prompt Engineering?

Sinimulan natin ang araling ito sa pamamagitan ng pag-defina ng **Prompt Engineering** bilang proseso ng _pagdidisenyo at pag-optimize_ ng mga input na teksto (prompts) upang makapaghatid ng pare-pareho at kalidad na mga tugon (completions) para sa isang ibinigay na layunin ng aplikasyon at modelo. Maaari nating isipin ito bilang isang 2-step na proseso:

- _pagdidisenyo_ ng paunang prompt para sa isang ibinigay na modelo at layunin
- _pagpino_ ng prompt nang paulit-ulit upang mapabuti ang kalidad ng tugon

Ito ay kinakailangang isang proseso ng trial-and-error na nangangailangan ng intuition at pagsisikap ng gumagamit upang makamit ang optimal na resulta. Kaya't bakit ito mahalaga? Upang masagot ang tanong na iyon, kailangan muna nating maunawaan ang tatlong konsepto:

- _Tokenization_ = kung paano "nakikita" ng modelo ang prompt
- _Base LLMs_ = kung paano "pinoproseso" ng foundation model ang isang prompt
- _Instruction-Tuned LLMs_ = kung paano maaaring makita ng modelo ang "mga gawain"

### Tokenization

Nakikita ng isang LLM ang mga prompt bilang isang _sequence ng tokens_ kung saan ang iba't ibang mga modelo (o bersyon ng isang modelo) ay maaaring mag-tokenize ng parehong prompt sa iba't ibang paraan. Dahil ang mga LLMs ay sinanay sa mga tokens (at hindi sa raw na teksto), ang paraan ng pag-tokenize ng mga prompt ay may direktang epekto sa kalidad ng generated na tugon.

Upang makakuha ng intuition para sa kung paano gumagana ang tokenization, subukan ang mga tool tulad ng [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) na ipinapakita sa ibaba. Kopyahin ang iyong prompt - at tingnan kung paano iyon nagiging mga tokens, bigyang-pansin kung paano hinahawakan ang mga whitespace characters at punctuation marks. Tandaan na ang halimbawang ito ay nagpapakita ng mas lumang LLM (GPT-3) - kaya't ang pagsubok nito sa mas bagong modelo ay maaaring makagawa ng ibang resulta.

### Konsepto: Foundation Models

Kapag ang isang prompt ay na-tokenize, ang pangunahing function ng ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o Foundation model) ay hulaan ang token sa sequence na iyon. Dahil ang mga LLMs ay sinanay sa malalaking text datasets, mayroon silang mahusay na kaalaman sa statistical relationships sa pagitan ng mga tokens at maaaring gawin ang prediction na iyon nang may kumpiyansa. Tandaan na hindi nila naiintindihan ang _kahulugan_ ng mga salita sa prompt o token; nakikita lang nila ang pattern na maaari nilang "kumpletuhin" sa kanilang susunod na prediction. Maaari silang magpatuloy sa pag-predict ng sequence hanggang sa ihinto ng user intervention o ilang pre-established condition.

Gusto mo bang makita kung paano gumagana ang prompt-based completion? Ipasok ang prompt sa itaas sa Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) gamit ang default na mga setting. Ang sistema ay naka-configure upang tratuhin ang mga prompt bilang mga kahilingan para sa impormasyon - kaya't dapat mong makita ang isang completion na nakakatugon sa kontekstong ito.

Ngunit paano kung ang user ay nais makakita ng isang partikular na bagay na tumutugma sa ilang criteria o layunin ng gawain? Dito pumapasok ang _instruction-tuned_ LLMs.

### Konsepto: Instruction Tuned LLMs

Ang [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) ay nagsisimula sa foundation model at fine-tunes ito gamit ang mga halimbawa o input/output pairs (halimbawa, multi-turn "messages") na maaaring maglaman ng malinaw na mga instruksyon - at ang tugon mula sa AI ay sinusubukan na sundan ang instruksyon na iyon.

Gumagamit ito ng mga teknik tulad ng Reinforcement Learning with Human Feedback (RLHF) na maaaring sanayin ang modelo upang _sundin ang mga instruksyon_ at _matuto mula sa feedback_ upang makagawa ng mga tugon na mas angkop para sa praktikal na mga aplikasyon at mas nauugnay sa mga layunin ng user.

Subukan natin ito - balikan ang prompt sa itaas, ngunit ngayon baguhin ang _system message_ upang magbigay ng sumusunod na instruksyon bilang konteksto:

> _I-summarize ang nilalaman na ibinigay para sa isang mag-aaral sa ikalawang baitang. Panatilihin ang resulta sa isang talata na may 3-5 bullet points._

Makikita mo kung paano ang resulta ay ngayon na-tune upang ipakita ang nais na layunin at format? Ang isang edukador ay maaari nang direktang gamitin ang tugon na ito sa kanilang mga slides para sa klase na iyon.

## Bakit natin kailangan ang Prompt Engineering?

Ngayon na alam natin kung paano pinoproseso ng mga LLMs ang mga prompt, pag-usapan natin kung _bakit_ natin kailangan ang prompt engineering. Ang sagot ay nakasalalay sa katotohanan na ang kasalukuyang mga LLMs ay nagdudulot ng ilang mga hamon na ginagawang mas mahirap makamit ang _maaasahan at pare-parehong mga completions_ nang hindi inilalagay ang pagsisikap sa pagbuo at pag-optimize ng prompt. Halimbawa:

1. **Ang mga tugon ng modelo ay stochastic.** Ang _parehong prompt_ ay malamang na mag-produce ng iba't ibang mga tugon sa iba't ibang mga modelo o bersyon ng modelo. At maaari itong mag-produce ng iba't ibang mga resulta sa _parehong modelo_ sa iba't ibang oras. _Ang mga teknik sa prompt engineering ay makakatulong sa atin na mabawasan ang mga variation na ito sa pamamagitan ng pagbibigay ng mas mahusay na mga guardrails_.

2. **Ang mga modelo ay maaaring mag-fabricate ng mga tugon.** Ang mga modelo ay pre-trained sa _malalaki ngunit limitadong_ datasets, ibig sabihin ay kulang sila ng kaalaman tungkol sa mga konsepto sa labas ng saklaw ng training. Bilang resulta, maaari silang mag-produce ng completions na hindi tumpak, imahinasyon, o direktang kontradiksyon sa mga kilalang katotohanan. _Ang mga teknik sa prompt engineering ay tumutulong sa mga gumagamit na matukoy at mabawasan ang mga fabrication na ito hal., sa pamamagitan ng pagtatanong sa AI para sa mga citations o reasoning_.

3. **Ang mga kakayahan ng modelo ay mag-iiba.** Ang mas bagong mga modelo o henerasyon ng modelo ay magkakaroon ng mas mayamang kakayahan ngunit nagdadala rin ng mga natatanging quirks at tradeoffs sa gastos at kumplikado. _Ang prompt engineering ay makakatulong sa atin na bumuo ng pinakamahusay na kasanayan at workflows na nag-aabstract ng mga pagkakaiba at umaangkop sa mga partikular na kinakailangan ng modelo sa scalable, seamless na paraan_.

Tingnan natin ito sa aksyon sa OpenAI o Azure OpenAI Playground:

- Gamitin ang parehong prompt sa iba't ibang LLM deployments (hal., OpenAI, Azure OpenAI, Hugging Face) - nakita mo ba ang mga variation?
- Gamitin ang parehong prompt nang paulit-ulit sa _parehong_ LLM deployment (hal., Azure OpenAI playground) - paano nag-iba ang mga variation na ito?

### Halimbawa ng Fabrications

Sa kursong ito, ginagamit natin ang terminong **"fabrication"** upang tukuyin ang phenomenon kung saan ang mga LLMs minsan ay nag-generate ng factually incorrect information dahil sa mga limitasyon sa kanilang training o iba pang constraints. Maaaring narinig mo rin ito na tinutukoy bilang _"hallucinations"_ sa mga popular na artikulo o mga research papers. Gayunpaman, mariing inirerekumenda namin ang paggamit ng _"fabrication"_ bilang terminong ito upang hindi natin aksidenteng i-anthropomorphize ang pag-uugali sa pamamagitan ng pag-aatribute ng isang human-like trait sa isang machine-driven na kinalabasan. Pinatitibay din nito ang [Responsible AI guidelines](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) mula sa perspektibo ng terminolohiya, inaalis ang mga terminong maaaring ituring na nakakasakit o hindi inclusive sa ilang konteksto.

Gusto mo bang makakuha ng ideya kung paano gumagana ang fabrications? Mag-isip ng isang prompt na nag-uutos sa AI na mag-generate ng nilalaman para sa isang hindi umiiral na paksa (upang matiyak na hindi ito matatagpuan sa training dataset). Halimbawa - sinubukan ko ang prompt na ito:

> **Prompt:** mag-generate ng lesson plan sa Martian War ng 2076.

Ang isang paghahanap sa web ay nagpakita sa akin na may mga fictional accounts (hal., serye sa telebisyon o mga libro) sa mga Martian wars - ngunit wala sa 2076. Ang common sense din ay nagsasabi sa atin na ang 2076 ay _sa hinaharap_ at sa gayon, hindi maaaring maiugnay sa isang tunay na kaganapan.

Kaya ano ang mangyayari kapag patakbuhin natin ang prompt na ito sa iba't ibang LLM providers?

> **Tugon 1**: OpenAI Playground (GPT-35)

> **Tugon 2**: Azure OpenAI Playground (GPT-35)

> **Tugon 3**: : Hugging Face Chat Playground (LLama-2)

Tulad ng inaasahan, bawat modelo (o bersyon ng modelo) ay nag-produce ng bahagyang iba't ibang mga tugon salamat sa stochastic na pag-uugali at mga pagkakaiba sa kakayahan ng modelo. Halimbawa, ang isang modelo ay nagta-target sa isang audience sa ika-8 baitang habang ang iba ay nag-aakala ng isang high-school student. Ngunit ang lahat ng tatlong mga modelo ay nag-generate ng mga tugon na maaaring makumbinsi ang isang hindi alam na gumagamit na ang kaganapan ay totoo.

Ang mga teknik sa prompt engineering tulad ng _metaprompting_ at _temperature configuration_ ay maaaring mabawasan ang mga fabrications ng modelo sa ilang antas. Ang mga bagong arkitektura sa prompt engineering ay isinasama rin ang mga bagong tool at teknik nang seamless sa prompt flow, upang mabawasan o mabawasan ang ilan sa mga epekto.

## Case Study: GitHub Copilot

Tapusin natin ang seksyong ito sa pamamagitan ng pagkakaroon ng ideya kung paano ginagamit ang prompt engineering sa mga solusyon sa totoong mundo sa pamamagitan ng pagtingin sa isang Case Study
Sa wakas, ang tunay na halaga ng mga template ay nakasalalay sa kakayahang lumikha at maglathala ng _prompt libraries_ para sa mga tiyak na application domains - kung saan ang prompt template ay _na-optimize_ upang ipakita ang konteksto o mga halimbawa na tiyak sa application na nagpapahusay sa kaugnayan at kawastuhan ng mga tugon para sa tinutukoy na mga gumagamit. Ang repository na [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) ay isang mahusay na halimbawa ng ganitong pamamaraan, na nag-aayos ng isang library ng mga prompt para sa larangan ng edukasyon na may diin sa mga pangunahing layunin tulad ng pagpaplano ng aralin, disenyo ng kurikulum, pagtuturo sa mga mag-aaral, atbp.

## Suportang Nilalaman

Kung iisipin natin ang pagbuo ng prompt bilang pagkakaroon ng isang instruksiyon (gawain) at isang target (pangunahing nilalaman), kung gayon ang _pangalawang nilalaman_ ay tulad ng karagdagang konteksto na ibinibigay natin upang **impluwensyahan ang output sa ilang paraan**. Maaari itong maging mga parameter ng pag-tune, mga tagubilin sa pag-format, mga taksonomiya ng paksa, atbp. na makakatulong sa modelong _i-akma_ ang tugon nito upang umayon sa mga nais na layunin o inaasahan ng gumagamit.

Halimbawa: Ibinigay ang isang katalogo ng kurso na may malawak na metadata (pangalan, paglalarawan, antas, mga tag ng metadata, instruktor, atbp.) sa lahat ng magagamit na kurso sa kurikulum:

- maaari tayong magtakda ng isang instruksiyon upang "ibuod ang katalogo ng kurso para sa Fall 2023"
- maaari nating gamitin ang pangunahing nilalaman upang magbigay ng ilang mga halimbawa ng nais na output
- maaari nating gamitin ang pangalawang nilalaman upang tukuyin ang nangungunang 5 "tag" ng interes.

Ngayon, maibibigay ng modelo ang isang buod sa format na ipinakita ng ilang mga halimbawa - ngunit kung ang isang resulta ay may maraming mga tag, maaari nitong unahin ang 5 tag na nakilala sa pangalawang nilalaman.

---

## Pinakamahusay na Kasanayan sa Prompting

Ngayon na alam natin kung paano maaring _buoin_ ang mga prompt, maaari nating simulan ang pag-iisip kung paano ito _idisenyo_ upang ipakita ang pinakamahusay na kasanayan. Maaari nating isipin ito sa dalawang bahagi - pagkakaroon ng tamang _mindset_ at paglalapat ng tamang _teknika_.

### Mindset sa Prompt Engineering

Ang Prompt Engineering ay isang proseso ng pagsubok at pagkakamali kaya't tandaan ang tatlong malawak na gabay na salik:

1. **Mahalaga ang Pag-unawa sa Domain.** Ang kawastuhan at kaugnayan ng tugon ay isang function ng _domain_ kung saan gumagana ang aplikasyon o gumagamit. I-apply ang iyong intuwisyon at kadalubhasaan sa domain upang **i-customize ang mga teknika**. Halimbawa, tukuyin ang _mga personalidad na tiyak sa domain_ sa iyong mga system prompt, o gumamit ng _mga template na tiyak sa domain_ sa iyong mga user prompt. Magbigay ng pangalawang nilalaman na sumasalamin sa mga konteksto na tiyak sa domain, o gumamit ng _mga cue at halimbawa na tiyak sa domain_ upang gabayan ang modelo patungo sa mga pamilyar na pattern ng paggamit.

2. **Mahalaga ang Pag-unawa sa Modelo.** Alam natin na ang mga modelo ay stochastic sa kalikasan. Ngunit ang mga implementasyon ng modelo ay maaari ring mag-iba sa mga tuntunin ng dataset ng pagsasanay na ginagamit nila (pre-trained knowledge), ang mga kakayahan na ibinibigay nila (hal., sa pamamagitan ng API o SDK) at ang uri ng nilalaman na na-optimize nila (hal., code vs. images vs. text). Unawain ang mga kalakasan at limitasyon ng modelong ginagamit mo, at gamitin ang kaalamang iyon upang _unahin ang mga gawain_ o bumuo ng _mga customized na template_ na na-optimize para sa mga kakayahan ng modelo.

3. **Mahalaga ang Iteration at Validation.** Ang mga modelo ay mabilis na umuunlad, gayundin ang mga teknika para sa prompt engineering. Bilang isang eksperto sa domain, maaaring mayroon kang iba pang konteksto o pamantayan sa iyong partikular na aplikasyon, na maaaring hindi naaangkop sa mas malawak na komunidad. Gamitin ang mga tool at teknika ng prompt engineering upang "i-jump start" ang pagbuo ng prompt, pagkatapos ay ulitin at i-validate ang mga resulta gamit ang iyong sariling intuwisyon at kadalubhasaan sa domain. I-record ang iyong mga insight at lumikha ng isang **knowledge base** (hal., mga library ng prompt) na maaaring magamit bilang isang bagong baseline ng iba, para sa mas mabilis na mga iteration sa hinaharap.

## Pinakamahusay na Kasanayan

Ngayon tingnan natin ang mga karaniwang pinakamahusay na kasanayan na inirerekomenda ng [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) at mga practitioner ng [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Ano                                | Bakit                                                                                                                                                                                                                                              |
| :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Suriin ang pinakabagong mga modelo. | Ang mga bagong henerasyon ng modelo ay malamang na may mga pinahusay na tampok at kalidad - ngunit maaari ring magdulot ng mas mataas na gastos. Suriin ang mga ito para sa epekto, pagkatapos ay gumawa ng mga desisyon sa paglipat.                                                        |
| Ihiwalay ang mga instruksiyon at konteksto | Suriin kung ang iyong modelo/provider ay nagtatakda ng _delimiters_ upang mas malinaw na makilala ang mga instruksiyon, pangunahing at pangalawang nilalaman. Makakatulong ito sa mga modelo na mas tumpak na magtalaga ng mga timbang sa mga token. |
| Maging tiyak at malinaw             | Magbigay ng higit pang mga detalye tungkol sa nais na konteksto, kinalabasan, haba, format, istilo, atbp. Mapapabuti nito ang parehong kalidad at pagkakapare-pareho ng mga tugon. I-capture ang mga recipe sa mga reusable na template.                                           |
| Maging mapaglarawan, gumamit ng mga halimbawa | Maaaring mas mahusay na tumugon ang mga modelo sa isang "ipakita at sabihin" na diskarte. Magsimula sa isang `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` values. Bumalik sa [Learning Sandbox section](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) upang matutunan kung paano.

### Susunod, buksan ang Jupyter Notebook

- Piliin ang runtime kernel. Kung gumagamit ng mga opsyon 1 o 2, piliin lamang ang default na Python 3.10.x kernel na ibinigay ng dev container.

Handa ka nang patakbuhin ang mga ehersisyo. Tandaan na walang _tama at mali_ na mga sagot dito - nag-eeksperimento lamang sa mga opsyon sa pamamagitan ng pagsubok at pagkakamali at pagbuo ng intuwisyon para sa kung ano ang gumagana para sa isang naibigay na modelo at domain ng aplikasyon.

_Sa kadahilanang ito, walang mga Code Solution segment sa araling ito. Sa halip, ang Notebook ay magkakaroon ng mga Markdown cell na pinamagatang "My Solution:" na nagpapakita ng isang halimbawa ng output para sa sanggunian._

## Pagsusuri ng Kaalaman

Alin sa mga sumusunod ang isang mahusay na prompt na sumusunod sa ilang makatwirang pinakamahusay na kasanayan?

1. Ipakita mo sa akin ang larawan ng pulang kotse
2. Ipakita mo sa akin ang larawan ng pulang kotse ng tatak na Volvo at modelong XC90 na nakaparada sa tabi ng bangin habang lumulubog ang araw
3. Ipakita mo sa akin ang larawan ng pulang kotse ng tatak na Volvo at modelong XC90

A: 2, ito ang pinakamahusay na prompt dahil nagbibigay ito ng mga detalye sa "ano" at pumapasok sa mga tiyak (hindi lang kahit anong kotse kundi isang tiyak na tatak at modelo) at inilalarawan din nito ang pangkalahatang setting. Ang 3 ay susunod na pinakamahusay dahil naglalaman din ito ng maraming paglalarawan.

## 🚀 Hamon

Tingnan kung magagamit mo ang "cue" na teknika sa prompt: Kumpletuhin ang pangungusap "Ipakita mo sa akin ang larawan ng pulang kotse ng tatak na Volvo at ". Ano ang magiging tugon nito, at paano mo ito mapapabuti?

## Mahusay na Trabaho! Ipagpatuloy ang Iyong Pag-aaral

Nais mo bang matuto nang higit pa tungkol sa iba't ibang konsepto ng Prompt Engineering? Pumunta sa [continued learning page](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang makahanap ng iba pang mahusay na mga mapagkukunan sa paksang ito.

Pumunta sa Lesson 5 kung saan titingnan natin ang [advanced prompting techniques](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Habang sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasaling-wika ng tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.