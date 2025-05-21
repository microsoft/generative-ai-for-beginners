<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T16:04:21+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "tl"
}
-->
# Mga Batayang Kaalaman sa Prompt Engineering

## Panimula
Tinutukoy ng modyul na ito ang mahahalagang konsepto at teknik sa paglikha ng epektibong mga prompt sa mga generative AI models. Mahalaga rin ang paraan ng pagsulat mo ng iyong prompt sa isang LLM. Ang maingat na pagkakagawa ng prompt ay maaaring makamit ang mas mahusay na kalidad ng tugon. Pero ano nga ba ang ibig sabihin ng mga terminong _prompt_ at _prompt engineering_? At paano ko mapapahusay ang _input_ ng prompt na ipinapadala ko sa LLM? Ito ang mga tanong na susubukan nating sagutin sa kabanatang ito at sa susunod.

Ang _Generative AI_ ay may kakayahang lumikha ng bagong nilalaman (hal., teksto, larawan, audio, code, atbp.) bilang tugon sa mga kahilingan ng gumagamit. Nakakamit ito gamit ang _Large Language Models_ tulad ng serye ng GPT ("Generative Pre-trained Transformer") ng OpenAI na sinanay para sa paggamit ng natural na wika at code.

Ngayon, maaaring makipag-ugnayan ang mga gumagamit sa mga modelong ito gamit ang mga pamilyar na paradigma tulad ng chat, nang hindi nangangailangan ng anumang teknikal na kadalubhasaan o pagsasanay. Ang mga modelo ay _prompt-based_ - nagpapadala ang mga gumagamit ng isang text input (prompt) at bumabalik ang tugon ng AI (completion). Maaari nilang "makipag-chat sa AI" nang paulit-ulit, sa mga multi-turn na pag-uusap, pinapahusay ang kanilang prompt hanggang sa ang tugon ay tumugma sa kanilang inaasahan.

Ang "Prompts" ngayon ay nagiging pangunahing _programming interface_ para sa mga generative AI apps, nagsasabi sa mga modelo kung ano ang gagawin at nakakaimpluwensya sa kalidad ng mga tugon. Ang "Prompt Engineering" ay isang mabilis na lumalagong larangan ng pag-aaral na nakatuon sa _disenyo at pag-optimize_ ng mga prompt upang maghatid ng pare-pareho at kalidad na mga tugon sa malawakang saklaw.

## Mga Layunin sa Pagkatuto

Sa leksyon na ito, matutunan natin kung ano ang Prompt Engineering, kung bakit ito mahalaga, at kung paano tayo makakagawa ng mas epektibong mga prompt para sa isang ibinigay na modelo at layunin ng aplikasyon. Mauunawaan natin ang mga pangunahing konsepto at pinakamahusay na kasanayan para sa prompt engineering - at matutunan ang tungkol sa isang interactive na kapaligiran ng "sandbox" ng Jupyter Notebooks kung saan makikita natin ang mga konseptong ito na inilalapat sa mga totoong halimbawa.

Sa pagtatapos ng leksyon na ito, magagawa natin ang:

1. Ipaliwanag kung ano ang prompt engineering at kung bakit ito mahalaga.
2. Ilarawan ang mga bahagi ng isang prompt at kung paano ito ginagamit.
3. Matutunan ang pinakamahusay na kasanayan at teknik para sa prompt engineering.
4. Ilapat ang mga natutunang teknik sa mga totoong halimbawa, gamit ang isang OpenAI endpoint.

## Mga Pangunahing Termino

Prompt Engineering: Ang pagsasanay ng pagdidisenyo at pagpapahusay ng mga input upang gabayan ang mga AI models patungo sa paggawa ng mga ninanais na output.
Tokenization: Ang proseso ng pag-convert ng teksto sa mas maliliit na yunit, na tinatawag na mga token, na maaaring maunawaan at maproseso ng isang modelo.
Instruction-Tuned LLMs: Malalaking Modelo ng Wika (LLMs) na na-fine-tune na may mga tiyak na tagubilin upang mapabuti ang katumpakan at kaugnayan ng kanilang mga tugon.

## Learning Sandbox

Ang prompt engineering ay kasalukuyang mas sining kaysa agham. Ang pinakamahusay na paraan upang mapabuti ang ating intuwisyon para dito ay ang _mas marami pang pagsasanay_ at ang paggamit ng isang trial-and-error na diskarte na pinagsasama ang kadalubhasaan sa domain ng aplikasyon sa mga inirerekomendang teknik at mga pag-optimize na partikular sa modelo.

Ang Jupyter Notebook na kasama ng leksyon na ito ay nagbibigay ng isang _sandbox_ na kapaligiran kung saan maaari mong subukan ang iyong natutunan - habang nag-aaral o bilang bahagi ng hamon sa code sa dulo. Upang maisagawa ang mga pagsasanay, kakailanganin mo ng:

1. **Isang Azure OpenAI API key** - ang service endpoint para sa isang na-deploy na LLM.
2. **Isang Python Runtime** - kung saan maaaring isagawa ang Notebook.
3. **Mga Lokal na Variable ng Kapaligiran** - _kumpletuhin ang mga hakbang sa [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) ngayon upang maging handa_.

Ang notebook ay may kasamang _starter_ na mga pagsasanay - ngunit hinihikayat kang magdagdag ng iyong sariling _Markdown_ (paglalarawan) at _Code_ (mga kahilingan sa prompt) na mga seksyon upang subukan ang higit pang mga halimbawa o ideya - at bumuo ng iyong intuwisyon para sa disenyo ng prompt.

## Gabay na May Larawan

Nais bang makuha ang kabuuang larawan ng sakop ng leksyon na ito bago ka sumisid? Tingnan ang gabay na may larawan na ito, na nagbibigay sa iyo ng ideya ng mga pangunahing paksa na sakop at ang mga pangunahing punto na dapat mong isaalang-alang sa bawat isa. Ang roadmap ng leksyon ay nagdadala sa iyo mula sa pag-unawa sa mga pangunahing konsepto at hamon hanggang sa pagtugon sa mga ito gamit ang mga nauugnay na teknik at pinakamahusay na kasanayan sa prompt engineering. Tandaan na ang seksyon ng "Advanced Techniques" sa gabay na ito ay tumutukoy sa nilalamang sakop sa _susunod_ na kabanata ng kurikulum na ito.

## Ang Aming Startup

Ngayon, pag-usapan natin kung paano nauugnay ang _paksang ito_ sa aming misyon na [dalhin ang inobasyon ng AI sa edukasyon](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Nais naming bumuo ng mga AI-powered na aplikasyon ng _personalized learning_ - kaya't isipin natin kung paano maaaring "magdisenyo" ng mga prompt ang iba't ibang mga gumagamit ng aming aplikasyon:

- **Mga Administrator** ay maaaring humiling sa AI na _suriiin ang data ng kurikulum upang tukuyin ang mga puwang sa saklaw_. Maaaring ibuod ng AI ang mga resulta o ipakita ito sa code.
- **Mga Guro** ay maaaring humiling sa AI na _lumikha ng isang plano ng aralin para sa isang target na madla at paksa_. Maaaring bumuo ang AI ng personalized na plano sa isang tinukoy na format.
- **Mga Mag-aaral** ay maaaring humiling sa AI na _turuan sila sa isang mahirap na paksa_. Ngayon ay maaaring gabayan ng AI ang mga mag-aaral sa mga aralin, pahiwatig at mga halimbawa na angkop sa kanilang antas.

Iyan ay isang maliit na bahagi lamang ng kabuuan. Tingnan ang [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - isang open-source na library ng mga prompt na pinili ng mga eksperto sa edukasyon - upang makakuha ng mas malawak na pag-unawa sa mga posibilidad! _Subukan ang ilang mga prompt na iyon sa sandbox o gamit ang OpenAI Playground upang makita kung ano ang mangyayari!_

## Ano ang Prompt Engineering?

Sinimulan natin ang leksyon na ito sa pamamagitan ng pagtukoy sa **Prompt Engineering** bilang proseso ng _pagdidisenyo at pag-optimize_ ng mga text input (prompt) upang maghatid ng pare-pareho at kalidad na mga tugon (completions) para sa isang ibinigay na layunin ng aplikasyon at modelo. Maaari nating isipin ito bilang isang 2-hakbang na proseso:

- _pagdidisenyo_ ng paunang prompt para sa isang ibinigay na modelo at layunin
- _pagpapahusay_ ng prompt nang paulit-ulit upang mapabuti ang kalidad ng tugon

Ito ay kinakailangang proseso ng trial-and-error na nangangailangan ng intuwisyon at pagsisikap ng gumagamit upang makamit ang pinakamainam na resulta. Kaya't bakit ito mahalaga? Upang sagutin ang tanong na iyon, kailangan muna nating maunawaan ang tatlong konsepto:

- _Tokenization_ = paano "nakikita" ng modelo ang prompt
- _Base LLMs_ = paano "pinoproseso" ng foundation model ang isang prompt
- _Instruction-Tuned LLMs_ = paano nakikita ng modelo ngayon ang "mga gawain"

### Tokenization

Nakikita ng isang LLM ang mga prompt bilang isang _sunod-sunod na mga token_ kung saan ang iba't ibang mga modelo (o bersyon ng isang modelo) ay maaaring mag-tokenize ng parehong prompt sa iba't ibang paraan. Dahil ang mga LLM ay sinanay sa mga token (at hindi sa raw text), ang paraan ng pag-tokenize ng mga prompt ay may direktang epekto sa kalidad ng na-generate na tugon.

Upang makakuha ng intuwisyon para sa kung paano gumagana ang tokenization, subukan ang mga tool tulad ng [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) na ipinapakita sa ibaba. Kopyahin ang iyong prompt - at tingnan kung paano ito na-convert sa mga token, pansinin kung paano hinahawakan ang mga whitespace character at punctuation marks. Tandaan na ang halimbawang ito ay nagpapakita ng mas lumang LLM (GPT-3) - kaya't ang pagsubok nito sa mas bagong modelo ay maaaring makagawa ng ibang resulta.

### Konsepto: Foundation Models

Kapag na-tokenize na ang isang prompt, ang pangunahing tungkulin ng ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o Foundation model) ay hulaan ang token sa sunod-sunod na iyon. Dahil ang mga LLM ay sinanay sa malalaking text datasets, mayroon silang magandang pag-unawa sa mga statistical na relasyon sa pagitan ng mga token at maaaring gawin ang hulang iyon nang may ilang kumpiyansa. Tandaan na hindi nila nauunawaan ang _kahulugan_ ng mga salita sa prompt o token; nakikita lang nila ang isang pattern na maaari nilang "kumpletuhin" sa kanilang susunod na hula. Maaari nilang ipagpatuloy ang paghula sa sunod-sunod na ito hanggang sa wakasan ng interbensyon ng gumagamit o ilang pre-established na kondisyon.

Nais bang makita kung paano gumagana ang prompt-based na completion? Ipasok ang prompt sa itaas sa Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) gamit ang default na mga setting. Ang sistema ay naka-configure upang ituring ang mga prompt bilang mga kahilingan para sa impormasyon - kaya dapat kang makakita ng completion na nakakatugon sa kontekstong ito.

Ngunit paano kung nais ng gumagamit na makakita ng isang bagay na partikular na nakakatugon sa ilang pamantayan o layunin ng gawain? Dito pumapasok ang mga _instruction-tuned_ na LLMs.

### Konsepto: Instruction Tuned LLMs

Ang isang [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) ay nagsisimula sa foundation model at fine-tune ito gamit ang mga halimbawa o input/output pairs (hal., multi-turn "messages") na maaaring maglaman ng malinaw na mga tagubilin - at ang tugon mula sa AI ay nagsisikap na sundin ang tagubiling iyon.

Gumagamit ito ng mga teknik tulad ng Reinforcement Learning with Human Feedback (RLHF) na maaaring sanayin ang modelo na _sumunod sa mga tagubilin_ at _matuto mula sa feedback_ upang makabuo ito ng mga tugon na mas angkop sa mga praktikal na aplikasyon at mas may kaugnayan sa mga layunin ng gumagamit.

Subukan natin ito - balikan ang prompt sa itaas, ngunit ngayon baguhin ang _system message_ upang magbigay ng sumusunod na tagubilin bilang konteksto:

> _Ibuod ang nilalaman na ibinibigay sa iyo para sa isang estudyante ng ikalawang baitang. Panatilihin ang resulta sa isang talata na may 3-5 bullet points._

Tingnan kung paano ang resulta ay na-tune ngayon upang ipakita ang ninanais na layunin at format? Maaaring direktang gamitin ng isang guro ang tugon na ito sa kanilang mga slide para sa klase na iyon.

## Bakit natin kailangan ang Prompt Engineering?

Ngayon na alam natin kung paano pinoproseso ng mga LLM ang mga prompt, pag-usapan natin kung _bakit_ natin kailangan ang prompt engineering. Ang sagot ay nakasalalay sa katotohanan na ang kasalukuyang mga LLM ay nagdadala ng ilang mga hamon na ginagawang mas mahirap makamit ang _maaasahan at pare-parehong completions_ nang hindi nagsisikap sa pagbuo at pag-optimize ng prompt. Halimbawa:

1. **Ang mga tugon ng modelo ay stochastic.** Ang _parehong prompt_ ay malamang na makabuo ng iba't ibang tugon sa iba't ibang mga modelo o bersyon ng modelo. At maaari rin itong makabuo ng iba't ibang resulta sa _parehong modelo_ sa iba't ibang oras. _Makakatulong sa atin ang mga teknik sa prompt engineering na mabawasan ang mga pagkakaiba-iba sa pamamagitan ng pagbibigay ng mas mahusay na mga gabay_.

2. **Maaaring gumawa ng mga pekeng tugon ang mga modelo.** Ang mga modelo ay pre-trained na may _malaki ngunit limitadong_ mga datasets, ibig sabihin kulang sila ng kaalaman tungkol sa mga konsepto sa labas ng saklaw ng pagsasanay na iyon. Bilang resulta, maaari silang makabuo ng mga completions na hindi tama, haka-haka, o direktang taliwas sa mga kilalang katotohanan. _Ang mga teknik sa prompt engineering ay tumutulong sa mga gumagamit na tukuyin at bawasan ang mga ganitong pekeng impormasyon hal., sa pamamagitan ng paghingi ng mga citation o pangangatwiran mula sa AI_.

3. **Magkakaiba ang mga kakayahan ng mga modelo.** Ang mas bagong mga modelo o henerasyon ng modelo ay magkakaroon ng mas mayamang kakayahan ngunit nagdadala rin ng mga natatanging quirks at tradeoffs sa gastos at kumplikado. _Makakatulong sa atin ang prompt engineering na bumuo ng pinakamahusay na mga kasanayan at mga workflow na nag-aalis ng mga pagkakaiba at umaangkop sa mga kinakailangan ng partikular sa modelo sa isang scalable at seamless na paraan_.

Tingnan natin ito sa aksyon sa OpenAI o Azure OpenAI Playground:

- Gamitin ang parehong prompt sa iba't ibang mga deployment ng LLM (hal., OpenAI, Azure OpenAI, Hugging Face) - nakita mo ba ang mga pagkakaiba-iba?
- Gamitin ang parehong prompt nang paulit-ulit sa _parehong_ deployment ng LLM (hal., Azure OpenAI playground) - paano nagkaiba-iba ang mga pagkakaiba-iba?

### Halimbawa ng Pekeng Impormasyon

Sa kursong ito, ginagamit natin ang terminong **"pekeng impormasyon"** upang tukuyin ang phenomenon kung saan minsang bumubuo ang mga LLM ng impormasyon na hindi tama sa katotohanan dahil sa mga limitasyon sa kanilang pagsasanay o iba pang mga hadlang. Maaaring narinig mo rin ito bilang _"hallucinations"_ sa mga popular na artikulo o mga research paper. Gayunpaman, mas inirerekomenda naming gamitin ang _"pekeng impormasyon"_ bilang termino upang hindi natin aksidenteng ma-anthropomorphize ang pag-uugali sa pamamagitan ng pag-uugnay ng katangiang parang tao sa isang kinalabasang pinapatakbo ng makina. Pinatitibay din nito ang [Mga Alituntunin ng Responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) mula sa perspektibo ng terminolohiya, inaalis ang mga termino na maaaring ituring na nakakasakit o hindi kasama sa ilang konteksto.

Nais bang makakuha ng ideya kung paano gumagana ang pekeng impormasyon? Mag-isip ng prompt na nag-uutos sa AI na bumuo ng nilalaman para sa isang hindi umiiral na paksa (upang matiyak na hindi ito matatagpuan sa dataset ng pagsasanay). Halimbawa - sinubukan ko ang prompt na ito:

> **Prompt:** bumuo ng isang plano ng aralin tungkol sa Digmaang Martian noong 2076.

Ipinakita sa akin ng isang paghahanap sa web na may mga kathang-isip na kwento (hal., serye sa telebisyon o mga libro) tungkol sa mga digmaang Martian - ngunit wala noong 2076. Sinasabi rin ng karaniwang pag-iisip na ang 2076 ay _sa hinaharap_ at sa gayon, hindi maaaring maiugnay sa isang tunay na kaganapan.

Kaya ano ang mangyayari kapag pinatakbo natin ang prompt na ito sa iba't ibang mga provider ng LLM?

> **Tugon 1**: OpenAI Playground (GPT-35)

> **Tugon 2**: Azure OpenAI Playground (GPT-35)

> **Tugon 3**: Hugging Face Chat Playground (LLama-2)

Gaya ng inaasahan, ang bawat modelo (o bersyon ng modelo) ay gumagawa ng bahagyang magkakaibang mga tugon salamat sa stochastic na pag-uugali at pagkakaiba-iba ng kakayahan ng modelo. Halimbawa, ang isang modelo ay nagta-target sa isang audience ng ika-8 baitang habang ang isa ay inaakala na isang estudyante sa high-school. Ngunit ang lahat ng tatlong modelo ay bumuo ng mga tugon na maaaring makumbinsi ang isang hindi alam na gumagamit na ang kaganapan ay totoo.

Ang mga teknik sa prompt engineering tulad ng _metaprompting_
Sa wakas, ang tunay na halaga ng mga template ay nasa kakayahan na lumikha at mag-publish ng _prompt libraries_ para sa mga vertical na domain ng aplikasyon - kung saan ang prompt template ay ngayon _na-optimize_ upang ipakita ang konteksto o mga halimbawa na partikular sa aplikasyon na nagpapaganda sa mga tugon na mas nauugnay at tumpak para sa target na user audience. Ang [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository ay isang mahusay na halimbawa ng ganitong diskarte, na nagkukulekta ng isang library ng mga prompts para sa domain ng edukasyon na may diin sa mga pangunahing layunin tulad ng pagplano ng aralin, disenyo ng kurikulum, pagtuturo sa estudyante, atbp.

## Sumusuportang Nilalaman

Kung iisipin natin ang pagbuo ng prompt bilang pagkakaroon ng isang instruksyon (gawain) at isang target (pangunahing nilalaman), kung gayon ang _pangalawang nilalaman_ ay parang karagdagang konteksto na ibinibigay natin upang **impluwensyahan ang output sa ilang paraan**. Ito ay maaaring mga tuning parameter, mga instruksyon sa pag-format, mga taxonomy ng paksa, atbp. na makakatulong sa modelo na _iayon_ ang tugon nito upang umangkop sa ninanais na mga layunin o inaasahan ng user.

Halimbawa: Ibinigay ang isang katalogo ng kurso na may malawak na metadata (pangalan, paglalarawan, antas, mga metadata tag, instruktor, atbp.) sa lahat ng magagamit na kurso sa kurikulum:

- maaari nating tukuyin ang isang instruksyon upang "ibuod ang katalogo ng kurso para sa Fall 2023"
- maaari nating gamitin ang pangunahing nilalaman upang magbigay ng ilang mga halimbawa ng ninanais na output
- maaari nating gamitin ang pangalawang nilalaman upang tukuyin ang nangungunang 5 "tag" ng interes.

Ngayon, maaaring magbigay ang modelo ng isang buod sa format na ipinakita ng ilang mga halimbawa - ngunit kung ang isang resulta ay may maraming tag, maaari nitong unahin ang 5 tag na natukoy sa pangalawang nilalaman.

---

## Mga Pinakamahusay na Kasanayan sa Prompting

Ngayon na alam natin kung paano maaaring _buuhin_ ang mga prompt, maaari nating simulang isipin kung paano _idisensyo_ ang mga ito upang ipakita ang pinakamahusay na kasanayan. Maaari nating isipin ito sa dalawang bahagi - pagkakaroon ng tamang _mindset_ at paggamit ng tamang _teknika_.

### Mindset sa Prompt Engineering

Ang Prompt Engineering ay isang proseso ng pagsubok at pagkakamali kaya't isaisip ang tatlong malawak na mga gabay na salik:

1. **Mahalaga ang Pag-unawa sa Domain.** Ang kawastuhan at kaugnayan ng tugon ay isang function ng _domain_ kung saan ang aplikasyon o user ay gumagana. I-apply ang iyong intuwisyon at kadalubhasaan sa domain upang **i-customize ang mga teknika** nang higit pa. Halimbawa, tukuyin ang _mga personalidad na partikular sa domain_ sa iyong mga system prompt, o gumamit ng _mga template na partikular sa domain_ sa iyong mga user prompt. Magbigay ng pangalawang nilalaman na sumasalamin sa mga konteksto na partikular sa domain, o gumamit ng _mga cue at halimbawa na partikular sa domain_ upang gabayan ang modelo patungo sa mga pamilyar na pattern ng paggamit.

2. **Mahalaga ang Pag-unawa sa Modelo.** Alam natin na ang mga modelo ay stochastic sa kalikasan. Ngunit ang mga implementasyon ng modelo ay maaari ding mag-iba sa mga tuntunin ng dataset na ginagamit nila sa pagsasanay (pre-trained knowledge), ang mga kakayahan na ibinibigay nila (hal. sa pamamagitan ng API o SDK) at ang uri ng nilalaman na na-optimize para sa kanila (hal. code vs. mga imahe vs. teksto). Unawain ang mga lakas at limitasyon ng modelong ginagamit mo, at gamitin ang kaalaman na iyon upang _unahin ang mga gawain_ o bumuo ng _mga customized na template_ na na-optimize para sa kakayahan ng modelo.

3. **Mahalaga ang Iterasyon at Pagpapatunay.** Ang mga modelo ay mabilis na umuusbong, gayundin ang mga teknika para sa prompt engineering. Bilang isang domain expert, maaari kang magkaroon ng iba pang konteksto o pamantayan para sa _iyong_ partikular na aplikasyon, na maaaring hindi naaangkop sa mas malawak na komunidad. Gamitin ang mga tool at teknika sa prompt engineering upang "simulan" ang pagbuo ng prompt, pagkatapos ay ulitin at patunayan ang mga resulta gamit ang iyong sariling intuwisyon at kadalubhasaan sa domain. I-record ang iyong mga pananaw at lumikha ng isang **knowledge base** (hal. mga prompt libraries) na maaaring magamit bilang isang bagong baseline ng iba, para sa mas mabilis na mga iterasyon sa hinaharap.

## Mga Pinakamahusay na Kasanayan

Ngayon tingnan natin ang mga karaniwang pinakamahusay na kasanayan na inirerekomenda ng mga practitioner ng [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) at [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Ano                                | Bakit                                                                                                                                                                                                                                              |
| :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Suriin ang pinakabagong mga modelo. | Ang mga bagong henerasyon ng modelo ay malamang na magkaroon ng pinahusay na mga tampok at kalidad - ngunit maaari ring magdulot ng mas mataas na gastos. Suriin ang mga ito para sa epekto, pagkatapos ay gumawa ng mga desisyon sa migration.                                        |
| Paghiwalayin ang mga instruksyon at konteksto | Tingnan kung ang iyong modelo/provider ay tumutukoy ng _mga delimiter_ upang mas malinaw na makilala ang mga instruksyon, pangunahing at pangalawang nilalaman. Maaari itong makatulong sa mga modelo na magtalaga ng timbang nang mas tumpak sa mga token.                           |
| Maging tiyak at malinaw             | Magbigay ng higit pang mga detalye tungkol sa ninanais na konteksto, kinalabasan, haba, format, istilo, atbp. Mapapabuti nito ang parehong kalidad at pagkakapare-pareho ng mga tugon. I-capture ang mga recipe sa mga reusable na template.                                                |
| Maging deskriptibo, gumamit ng mga halimbawa | Maaaring mas mahusay na tumugon ang mga modelo sa isang "show and tell" na diskarte. Simulan sa isang `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` values. Bumalik sa [Learning Sandbox section](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) para matutunan kung paano.

### Susunod, buksan ang Jupyter Notebook

- Piliin ang runtime kernel. Kung gumagamit ng mga opsyon 1 o 2, piliin lamang ang default na Python 3.10.x kernel na ibinigay ng dev container.

Handa ka na upang patakbuhin ang mga ehersisyo. Tandaan na walang _tama at mali_ na mga sagot dito - simpleng pag-explore ng mga opsyon sa pamamagitan ng pagsubok at pagkakamali at pagbuo ng intuwisyon para sa kung ano ang gumagana para sa isang ibinigay na modelo at domain ng aplikasyon.

_Sa kadahilanang ito, walang mga segment ng Solusyon sa Code sa araling ito. Sa halip, ang Notebook ay magkakaroon ng mga Markdown cell na may pamagat na "My Solution:" na nagpapakita ng isang halimbawa ng output para sa sanggunian._

## Pagsusuri ng Kaalaman

Alin sa mga sumusunod ang isang magandang prompt na sumusunod sa ilang makatwirang pinakamahusay na kasanayan?

1. Ipakita mo sa akin ang larawan ng pulang kotse
2. Ipakita mo sa akin ang larawan ng pulang kotse na gawa ng Volvo at model XC90 na nakaparada sa tabi ng bangin na may lumulubog na araw
3. Ipakita mo sa akin ang larawan ng pulang kotse na gawa ng Volvo at model XC90

A: 2, ito ang pinakamahusay na prompt dahil nagbibigay ito ng mga detalye sa "ano" at nagiging tiyak (hindi lamang anumang kotse kundi isang tiyak na make at model) at inilalarawan din nito ang pangkalahatang setting. Ang 3 ay susunod na pinakamahusay dahil naglalaman din ito ng maraming paglalarawan.

## 🚀 Hamon

Tingnan kung maaari mong gamitin ang "cue" na teknika sa prompt: Kumpletuhin ang pangungusap na "Ipakita mo sa akin ang larawan ng pulang kotse na gawa ng Volvo at ". Ano ang tugon nito, at paano mo ito mapapabuti?

## Mahusay na Trabaho! Ipagpatuloy ang Iyong Pag-aaral

Gusto mo bang matuto nang higit pa tungkol sa iba't ibang mga konsepto ng Prompt Engineering? Pumunta sa [continued learning page](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang makahanap ng iba pang mahusay na mga mapagkukunan sa paksang ito.

Pumunta sa Aralin 5 kung saan titingnan natin ang [mga advanced na teknika sa prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Pagtatatuwa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Habang nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkaka-tugma. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na mapagkakatiwalaang sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.