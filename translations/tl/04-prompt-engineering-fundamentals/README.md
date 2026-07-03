# Mga Pangunahing Kaalaman sa Prompt Engineering

[![Mga Pangunahing Kaalaman sa Prompt Engineering](../../../translated_images/tl/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Panimula
Sinasaklaw ng yugtong ito ang mahahalagang konsepto at pamamaraan para sa paggawa ng epektibong mga prompt sa mga modelong generative AI. Mahalaga rin ang paraan ng pagsulat mo ng prompt para sa isang LLM. Ang maingat na ginawa na prompt ay maaaring makamit ang mas mahusay na kalidad ng tugon. Ngunit ano nga ba ang ibig sabihin ng mga terminong tulad ng _prompt_ at _prompt engineering_? At paano ko mapapabuti ang prompt _input_ na ipinapadala ko sa LLM? Ito ang mga tanong na susubukan nating sagutin sa kabanatang ito at sa susunod.

Ang _Generative AI_ ay may kakayahang lumikha ng bagong nilalaman (hal., teksto, imahe, audio, code, atbp.) bilang tugon sa mga kahilingan ng gumagamit. Nagagawa ito gamit ang _Large Language Models_ tulad ng OpenAI's GPT ("Generative Pre-trained Transformer") series na sinanay para gumamit ng natural na wika at code.

Maaaring makipag-ugnayan na ang mga gumagamit sa mga modelong ito gamit ang mga pamilyar na pamamaraan tulad ng chat, nang hindi nangangailangan ng anumang teknikal na kasanayan o pagsasanay. Ang mga modelo ay _prompt-based_ - nagpapadala ang mga gumagamit ng text input (prompt) at nakakakuha ng tugon mula sa AI (completion). Maaari silang makipag-chat sa AI nang paulit-ulit, sa mga multi-turn na pag-uusap, na pinapino ang kanilang prompt hanggang ang tugon ay tumugma sa kanilang inaasahan.

Ngayon, ang mga "Prompt" ay naging pangunahing _programming interface_ para sa mga aplikasyong generative AI, na nagsasabi sa mga modelo kung ano ang gagawin at nakakaapekto sa kalidad ng mga tugon na ibinabalik. Ang "Prompt Engineering" ay isang mabilis na lumalaking larangan ng pag-aaral na nakatuon sa _disenyo at pag-optimize_ ng mga prompt upang makapaghatid ng pare-pareho at mataas na kalidad na mga tugon sa malawakang aplikasyon.

## Mga Layunin ng Pagkatuto

Sa araling ito, matututuhan natin kung ano ang Prompt Engineering, bakit ito mahalaga, at kung paano tayo makapaggagawa ng mas epektibong mga prompt para sa isang partikular na modelo at layunin ng aplikasyon. Mauunawaan natin ang mga pangunahing konsepto at pinakamahusay na kasanayan sa prompt engineering - at matututuhan ang tungkol sa isang interaktibong kapaligiran sa Jupyter Notebooks na "sandbox" kung saan makikita natin ang mga konseptong ito na inilalapat sa mga totoong halimbawa.

Sa pagtatapos ng araling ito, magagawa nating:

1. Ipaliwanag kung ano ang prompt engineering at bakit ito mahalaga.
2. Ilarawan ang mga bahagi ng prompt at kung paano ito ginagamit.
3. Matutunan ang mga pinakamahusay na kasanayan at pamamaraan sa prompt engineering.
4. Ilapat ang mga natutunang pamamaraan sa mga totoong halimbawa, gamit ang endpoint ng OpenAI.

## Mga Pangunahing Terminolohiya

Prompt Engineering: Ang pagsasanay ng pagdidisenyo at pagpino ng mga input upang gabayan ang mga AI model tungo sa paggawa ng nais na mga output.  
Tokenization: Ang proseso ng pag-convert ng teksto sa mas maliliit na yunit, na tinatawag na mga token, na mauunawaan at mapoproseso ng modelo.  
Instruction-Tuned LLMs: Mga Large Language Models (LLMs) na na-fine-tune gamit ang mga partikular na instruksyon upang mapabuti ang katumpakan at kaugnayan ng mga tugon.

## Learning Sandbox

Ang prompt engineering ay kasalukuyang mas sining kaysa agham. Ang pinakamahusay na paraan upang mapalalim ang ating intuwisyon dito ay ang _mas maraming pagsasanay_ at paggamit ng pamamaraan ng trial-and-error na pinagsasama ang kaalaman sa larangan ng aplikasyon at mga inirerekomendang pamamaraan pati na rin ang mga pag-optimize na partikular sa modelo.

Ang Jupyter Notebook na kasama ng araling ito ay nagbibigay ng isang _sandbox_ na kapaligiran kung saan maaari mong subukan ang iyong mga natutunan - habang nagpapatuloy o bilang bahagi ng hamon sa pag-code sa dulo. Upang maisagawa ang mga pagsasanay, kakailanganin mo:

1. **Isang Azure OpenAI API key** - ang serbisyo endpoint para sa isang naka-deploy na LLM.  
2. **Isang Python Runtime** - kung saan maaaring maisagawa ang Notebook.  
3. **Local Env Variables** - _kumpletuhin ang mga hakbang sa [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) ngayon upang maging handa_.

May mga _starter_ na pagsasanay ang notebook - ngunit hinihikayat ka na magdagdag ng sarili mong _Markdown_ (paglalarawan) at _Code_ (mga kahilingan sa prompt) na mga seksyon upang subukan ang higit pang mga halimbawa o ideya - at buuin ang iyong intuwisyon sa disenyo ng prompt.

## Ilustradong Gabay

Gusto mo bang makita ang pangkalahatang larawan ng mga saklaw ng araling ito bago ka sumugod? Tingnan ang ilustradong gabay na ito, na nagbibigay sa iyo ng ideya ng mga pangunahing paksa at mahahalagang punto na dapat pag-isipan sa bawat isa. Dinadala ka ng roadmap ng aralin mula sa pag-unawa sa mga pangunahing konsepto at hamon hanggang sa pagtugon sa mga ito gamit ang mga nauugnay na teknik at pinakamahusay na kasanayan sa prompt engineering. Tandaan na ang seksyong "Advanced Techniques" sa gabay na ito ay tumutukoy sa nilalaman na saklaw sa _susunod_ na kabanata ng kurikulong ito.

![Illustrated Guide to Prompt Engineering](../../../translated_images/tl/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Ang Aming Startup

Ngayon, pag-usapan natin kung paano nauugnay ang _paksang ito_ sa misyon ng aming startup na [magdala ng inobasyon ng AI sa edukasyon](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Nais nating bumuo ng mga AI-powered na aplikasyon ng _personalized learning_ – kaya isipin natin kung paano "idisensyo" ng iba't ibang gumagamit ng aming aplikasyon ang mga prompt:

- Maaaring hilingin ng **Mga Administrator** sa AI na _analysahin ang datos ng kurikulum upang tukuyin ang mga kakulangan sa saklaw_. Maaaring ibuod ng AI ang mga resulta o ipakita ito gamit ang code.
- Maaaring hilingin ng **Mga Guro** sa AI na _gumawa ng lesson plan para sa isang target na audience at paksa_. Maaari ng AI na bumuo ng personalized na plano sa isang tinukoy na format.
- Maaaring hilingin ng **Mga Mag-aaral** sa AI na _turuan sila sa isang mahirap na asignatura_. Maaari na ngayong gabayan ng AI ang mga estudyante gamit ang mga leksyon, mga pahiwatig, at mga halimbawa na angkop sa kanilang antas.

Iyan ang simula lamang. Tingnan ang [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - isang open-source na library ng mga prompt na inakda ng mga eksperto sa edukasyon - upang magkaroon ng mas malawak na ideya ng mga posibilidad! _Subukan patakbuhin ang ilan sa mga prompt na iyon sa sandbox o gamit ang OpenAI Playground upang makita ang nangyayari!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Ano ang Prompt Engineering?

Sinimulan natin ang araling ito sa pagde-define ng **Prompt Engineering** bilang proseso ng _pagdidisenyo at pag-optimize_ ng mga text input (prompt) upang makapaghatid ng pare-pareho at mataas na kalidad na tugon (completions) para sa isang layunin ng aplikasyon at modelo. Maaari nating isipin ito bilang isang proseso na may 2 hakbang:

- _pagdidisenyo_ ng panimulang prompt para sa isang modelo at layunin  
- _pagpino_ ng prompt nang paulit-ulit upang mapabuti ang kalidad ng tugon  

Ito ay kailangang proseso ng trial-and-error na nangangailangan ng intuwisyon at pagsisikap ng gumagamit upang makamit ang pinakamainam na resulta. Bakit nga ba ito mahalaga? Upang sagutin ang tanong na iyon, kailangan muna nating maunawaan ang tatlong konsepto:

- _Tokenization_ = kung paano "nakikita" ng modelo ang prompt  
- _Base LLMs_ = kung paano "pinoproseso" ng pundasyong modelo ang prompt  
- _Instruction-Tuned LLMs_ = kung paano na ngayon "nakikita" ng modelo ang mga gawain  

### Tokenization

Isinasaalang-alang ng isang LLM ang mga prompt bilang _sunod-sunod na token_ kung saan maaaring i-tokenize ng iba't ibang mga modelo (o mga bersyon ng isang modelo) ang parehong prompt sa iba't ibang paraan. Dahil ang mga LLM ay sinanay sa mga token (hindi sa raw na teksto), ang paraan kung paano i-tokenize ang mga prompt ay may direktang epekto sa kalidad ng nalikhang tugon.

Upang magkaroon ng intuwisyon kung paano gumagana ang tokenization, subukan ang mga kasangkapan tulad ng [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) na ipinakita sa ibaba. Kopyahin ang iyong prompt - at tingnan kung paano ito na-convert sa mga token, bigyang-pansin kung paano hinahawakan ang mga whitespace character at mga tandang bantas. Tandaan na ipinapakita ng halimbawang ito ang isang mas lumang LLM (GPT-3) - kaya kung susubukan ito sa mas bagong modelo maaaring magbunga ito ng ibang resulta.

![Tokenization](../../../translated_images/tl/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Konsepto: Mga Foundation Model

Kapag na-tokenize na ang prompt, ang pangunahing tungkulin ng ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o Foundation model) ay hulaan ang token sa nasabing sunod-sunod. Dahil ang mga LLM ay sinanay sa malalaking dataset ng teksto, may mahusay silang pag-unawa sa mga estadistikal na ugnayan sa pagitan ng mga token at maaaring hulaan iyon nang may tiwala. Tandaan na hindi nila naiintindihan ang _kahulugan_ ng mga salita sa prompt o token; nakikita lang nila ang isang pattern na maaari nilang "kumpletuhin" sa susunod nilang hula. Maaari nilang ipagpatuloy ang paghula ng sunod hanggang ito ay itigil ng gumagamit o ng isang itinalagang kondisyon.

Gusto mo bang makita kung paano gumagana ang prompt-based completion? Ipasok ang prompt na nasa itaas sa Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) gamit ang default na mga setting. Nakakonpigure ang sistema upang ituring ang mga prompt bilang mga kahilingan para sa impormasyon - kaya makakakita ka ng tugon na tumutugon sa kontekstong ito.

Ngunit paano kung nais ng gumagamit na makita ang isang partikular na bagay na tumutugon sa ilang pamantayan o layunin ng gawain? Dito pumapasok ang _instruction-tuned_ LLMs.

![Base LLM Chat Completion](../../../translated_images/tl/04-playground-chat-base.65b76fcfde0caa67.webp)

### Konsepto: Instruction Tuned LLMs

Ang isang [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) ay nagsisimula sa foundation model at ini-fine tune ito gamit ang mga halimbawa o pares ng input/output (hal., mga multi-turn na "mensahe") na maaaring maglaman ng malinaw na mga instruksyon - at sinusubukan ng tugon ng AI na sundin ang instruksyong iyon.

Gumagamit ito ng mga teknik tulad ng Reinforcement Learning with Human Feedback (RLHF) na siyang nagsasanay sa modelo na _sumunod sa mga instruksyon_ at _matuto mula sa feedback_ upang makagawa ng mga tugon na mas angkop sa mga praktikal na aplikasyon at mas kaugnay sa layunin ng gumagamit.

Subukan natin ito - balikan ang prompt na nasa itaas, ngunit ngayon palitan ang _system message_ upang magbigay ng sumusunod na instruksyon bilang konteksto:

> _Buodin ang nilalaman na ibinigay mo para sa isang mag-aaral sa ikalawang baitang. Panatilihin ang resulta sa isang talata na may 3-5 puntong bullet._

Makikita mo kung paano naitono ang resulta upang ipakita ang nais na layunin at format. Maaaring direkta nang gamitin ng isang guro ang tugong ito sa kanilang mga slide sa klase.

![Instruction Tuned LLM Chat Completion](../../../translated_images/tl/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Bakit Kailangan ang Prompt Engineering?

Ngayon na alam na natin kung paano pinoproseso ang mga prompt ng LLMs, pag-usapan natin _bakit_ kailangan ang prompt engineering. Ang sagot ay nakasalalay sa katotohanan na ang kasalukuyang mga LLM ay may ilang hamon na nagpapahirap para magkaroon ng _maaasahan at pare-parehong mga tugon_ nang hindi ginagawang pagsisikap ang pagbuo at pag-optimize ng prompt. Halimbawa:

1. **Ang mga tugon ng modelo ay stochastic.** Ang _parehong prompt_ ay maaaring magbigay ng magkaibang tugon sa iba't ibang modelo o bersyon ng modelo. At maaaring makabuo rin ito ng magkaibang resulta gamit ang _parehong modelo_ sa iba't ibang pagkakataon. _Makakatulong ang mga teknik sa prompt engineering upang mabawasan ang mga pagkakaibang ito sa pamamagitan ng pagbibigay ng mas mahusay na mga guardrail_.

1. **Maaaring gawing gawa-gawa lang ng mga modelo ang mga tugon.** Ang mga modelo ay sinanay gamit ang _malaki ngunit limitadong_ mga dataset, kaya kulang sila sa kaalaman tungkol sa mga konseptong wala sa saklaw ng pagsasanay. Dahil dito, maaari silang gumawa ng mga tugon na hindi tama, imbento, o direktang salungat sa mga kilalang katotohanan. _Tinutulungan ng prompt engineering ang mga gumagamit na matukoy at mabawasan ang mga ganitong paggawa, hal., sa pamamagitan ng pagtatanong sa AI para sa mga sanggunian o paliwanag_.

1. **Nagkakaiba-iba ang mga kakayahan ng mga modelo.** Ang mga mas bagong modelo o henerasyon ng modelo ay may mas maraming kakayahan ngunit may kanya-kanyang kakaibang ugali at mga kompromiso sa gastos at pagiging kumplikado. _Makakatulong ang prompt engineering upang maka-develop tayo ng mga pinakamahusay na kasanayan at workflows na nag-aalis ng pagkakaiba at nag-aangkop sa mga partikular na pangangailangan ng modelo sa scalable at seamless na paraan_.

Subukan natin itong makita sa OpenAI o Azure OpenAI Playground:

- Gamitin ang parehong prompt sa iba't ibang deployment ng LLM (hal., OpenAI, Azure OpenAI, Hugging Face) - nakita mo ba ang mga pagkakaiba?  
- Gamitin ang parehong prompt nang paulit-ulit sa _parehong_ deployment ng LLM (hal., Azure OpenAI playground) - paano nagkaiba-iba ang mga resulta?

### Halimbawa ng Mga Paggawa

Sa kursong ito, ginagamit namin ang terminong **"fabrication"** bilang pagtukoy sa phenomenon kung saan minsan ay gumagawa ang mga LLM ng hindi tama sa katotohanang impormasyon dahil sa mga limitasyon sa kanilang pagsasanay o ibang mga hadlang. Maaaring narinig mo rin ito bilang _"hallucinations"_ sa mga popular na artikulo o research papers. Gayunpaman, malakas naming inirerekomenda ang paggamit ng _"fabrication"_ bilang termino upang hindi natin hindi sinasadyang bigyan ng katangiang tao ang pag-uugali sa pamamagitan ng pag-aatribut ng isang human-like trait sa resulta ng makina. Pinapalakas din nito ang alituntunin ng [Responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) mula sa perspektibo ng terminolohiya, na inaalis ang mga terminong maaaring ituring na nakakasakit o hindi inklusibo sa ilang konteksto.

Gusto mo bang maramdaman kung paano gumagana ang mga fabrication? Isipin ang prompt na nag-uutos sa AI na lumikha ng nilalaman para sa isang di-umiiral na paksa (upang matiyak na wala ito sa dataset ng pagsasanay). Halimbawa - sinubukan ko itong prompt:

> **Prompt:** gumawa ng lesson plan tungkol sa Martian War of 2076.
Ipinakita sa akin ng isang web search na mayroong mga kathang-isip na kwento (hal., serye sa telebisyon o mga libro) tungkol sa mga digmaan sa Mars - ngunit wala sa 2076. Sinasabi rin ng karaniwang kaalaman na ang 2076 ay _sa hinaharap_ kaya hindi ito maaaring iugnay sa isang totoong pangyayari.

Kaya ano ang mangyayari kapag pinatakbo natin ang prompt na ito sa iba't ibang provider ng LLM?

> **Tugon 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/tl/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Tugon 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/tl/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Tugon 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/tl/04-fabrication-huggingchat.faf82a0a51278956.webp)

Tulad ng inaasahan, bawat modelo (o bersyon ng modelo) ay nagbibigay ng bahagyang magkakaibang mga tugon dahil sa stochastic na pag-uugali at mga pagkakaiba sa kakayahan ng modelo. Halimbawa, ang isang modelo ay layuning para sa isang audience ng ika-8 na baitang habang ang isa naman ay inaasahan ang isang mag-aaral sa mataas na paaralan. Ngunit lahat ng tatlong modelo ay nagbuo ng mga tugon na maaaring kumbinsihin ang isang hindi nakakaalam na user na ang pangyayari ay totoo.

Ang mga teknik sa prompt engineering gaya ng _metaprompting_ at _temperature configuration_ ay maaaring magpababa ng mga paglikha ng maling sagot ng modelo sa ilang lawak. Ang mga bagong _architectures_ ng prompt engineering ay nagsasama rin ng mga bagong gamit at teknik nang tuloy-tuloy sa daloy ng prompt, upang mapagaan o mabawasan ang ilan sa mga epekto na ito.

## Pag-aaral ng Kaso: GitHub Copilot

Tapusin natin ang bahaging ito sa pamamagitan ng pagkuha ng ideya kung paano ginagamit ang prompt engineering sa mga totoong solusyon sa pamamagitan ng pagtingin sa isang Pag-aaral ng Kaso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

Ang GitHub Copilot ang iyong "AI Pair Programmer" - ito ay nagko-convert ng mga text prompt sa mga kumpletong code at naka-integrate sa iyong development environment (hal., Visual Studio Code) para sa isang seamless na karanasan ng user. Tulad ng naidokumento sa serye ng mga blog sa ibaba, ang pinakaunang bersyon ay batay sa OpenAI Codex na modelo - kung saan mabilis na napagtanto ng mga engineer ang pangangailangang i-fine-tune ang modelo at paunlarin ang mas mahusay na prompt engineering na mga teknik, para mapabuti ang kalidad ng code. Noong Hulyo, kanilang [inilunsad ang isang pinahusay na AI model na lampas sa Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sa mas mabilis na mga suhestiyon.

Basahin ang mga post nang sunod-sunod, para masundan ang kanilang paglalakbay sa pagkatuto.

- **Mayo 2023** | [GitHub Copilot ay Nagpapabuti sa Pag-unawa ng Iyong Code](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mayo 2023** | [Sa Loob ng GitHub: Pagtatrabaho sa mga LLM sa Likod ng GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Hunyo 2023** | [Paano Magsulat ng Mas Mabuting Mga Prompt para sa GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Hulyo 2023** | [.. GitHub Copilot Lampas sa Codex gamit ang Pinahusay na AI Model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Hulyo 2023** | [Isang Gabay para sa Prompt Engineering at LLMs para sa mga Developer](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Setyembre 2023** | [Paano Gumawa ng Enterprise LLM App: Mga Aral mula sa GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Maaari ka ring mag-browse sa kanilang [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para sa iba pang mga post tulad ng [ito](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) na nagpapakita kung paano _inaaplay_ ang mga modelong ito at teknik para sa mga totoong aplikasyon.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Konstruksyon ng Prompt

Nakita na natin kung bakit mahalaga ang prompt engineering - ngayon unawain natin kung paano ang mga prompt ay _binubuo_ upang masuri natin ang iba't ibang teknik para sa mas epektibong disenyo ng prompt.

### Pangunahing Prompt

Magsimula tayo sa pangunahing prompt: isang text input na ipinapadala sa modelo nang walang iba pang konteksto. Narito ang isang halimbawa - kapag ipinadala natin ang unang ilang salita ng pambansang awit ng US sa OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), agad nitong _kompletuhin_ ang tugon gamit ang susunod na mga linya, na nagpapakita ng pangunahing asal sa prediksyon.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Parang sinisimulan mo ang mga liriko ng "The Star-Spangled Banner," ang pambansang awit ng Estados Unidos. Ang buong liriko ay ... |

### Kumplikadong Prompt

Ngayon magdagdag tayo ng konteksto at mga tagubilin sa pangunahing prompt na iyon. Pinapayagan tayo ng [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) na bumuo ng kumplikadong prompt bilang koleksyon ng mga _mensaheng_ may:

- Mga pares ng input/output na sumasalamin sa input ng _user_ at tugon ng _assistant_.
- Mensaheng pang-sistema na nagtatakda ng konteksto para sa asal o personalidad ng assistant.

Ang request ay nasa anyo sa ibaba, kung saan ang _tokenization_ ay epektibong sumasaklaw sa kaugnay na impormasyon mula sa konteksto at usapan. Ngayon, ang pagbabago ng kontekstong sistema ay maaaring magkaroon ng kapantay na epekto sa kalidad ng mga kumpletong tugon, gaya ng mga ipinagkaloob na input ng user.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt ng Tagubilin

Sa mga halimbawa sa itaas, ang prompt ng user ay isang simpleng text query na maaaring ipakahulugan bilang isang kahilingan para sa impormasyon. Sa _instruction_ prompts, maaari nating gamitin ang text upang tukuyin ang isang gawain nang mas detalyado, nagbibigay ng mas mahusay na gabay sa AI. Heto ang isang halimbawa:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Uri ng Tagubilin    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Sumulat ng paglalarawan tungkol sa Digmaang Sibil                                                                                                                                                                                     | _nagbalik ng simpleng talata_                                                                                            | Simple              |
| Sumulat ng paglalarawan tungkol sa Digmaang Sibil. Magbigay ng mga mahahalagang petsa at pangyayari at ilarawan ang kabuluhan nila                                                                                                   | _nagbalik ng talata na sinundan ng listahan ng mahahalagang petsa ng mga pangyayari na may mga paglalarawan_               | Kumplikado          |
| Sumulat ng paglalarawan tungkol sa Digmaang Sibil sa 1 talata. Magbigay ng 3 bullets na may mahahalagang petsa at ang kabuluhan nito. Magbigay ng 3 pang bullets na may mahahalagang tao sa kasaysayan at kanilang kontribusyon. Ibalik ang output bilang JSON file | _nagbabalik ng mas malawak na detalye sa isang text box, naka-format bilang JSON na maaari mong kopyahin-paste sa file at i-validate kung kailangan_ | Kumplikado. Naka-format. |

## Pangunahing Nilalaman

Sa mga halimbawa sa itaas, ang prompt ay medyo bukas pa rin, na nagpapahintulot sa LLM na magpasya kung alin sa pre-trained dataset nito ang kaugnay. Sa _primary content_ na disenyo, ang input na teksto ay hinahati sa dalawang bahagi:

- isang tagubilin (aksiyon)
- kaugnay na nilalaman (na nakaaapekto sa aksiyon)

Heto ang isang halimbawa kung saan ang tagubilin ay "buodin ito sa 2 pangungusap".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ang Jupiter ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Sistema ng Araw. Isa itong gas giant na may mass na isa-sa-mil mula sa Araw, ngunit dalawang kalahati beses na mas malaki kaysa sa lahat ng iba pang mga planeta sa Sistema ng Araw na pinagsama-sama. Ang Jupiter ay isa sa mga pinaka-maliwanag na bagay na makikita ng hubad na mata sa kalangitan sa gabi, at kilala na ito ng mga sinaunang kabihasnan bago pa man ang nakasulat na kasaysayan. Ito ay ipinangalan kay Jupiter, ang diyos ng mga Romano.[19] Kapag tiningnan mula sa Earth, maaaring maging sapat na maliwanag ang Jupiter para ang kanyang naipikong ilaw ay makalikha ng nakikitang mga anino,[20] at karaniwang ito ang pangatlong pinaka-maliwanag na natural na bagay sa kalangitan sa gabi pagkatapos ng Buwan at Venus. <br/> **Buodin ito sa 2 maiikling pangungusap** | Ang Jupiter, ang ikalimang planeta mula sa Araw, ang pinakamalaki sa Sistema ng Araw at kilala bilang isa sa mga pinakamaliwanag na bagay sa kalangitan sa gabi. Ipinangalan sa diyos na Romano na si Jupiter, ito ay isang gas giant na may mass na dalawang kalahati beses ng lahat ng ibang planeta sa Sistema ng Araw na pinagsama-sama. |

Maaaring gamitin ang segment ng pangunahing nilalaman sa iba't ibang paraan para maghatid ng mas epektibong mga tagubilin:

- **Mga Halimbawa** - sa halip na sabihin sa modelo kung ano ang gagawin gamit ang isang tahasang tagubilin, bigyan ito ng mga halimbawa kung ano ang gagawin at hayaan itong hulaan ang pattern.
- **Mga Cue** - sundan ang tagubilin ng isang "cue" na nagpapahiwatig sa completion, ginagabayan ang modelo patungo sa mas kaugnay na mga sagot.
- **Mga Template** - ito ay mga paulit-ulit na 'recipe' para sa mga prompt na may mga placeholder (mga variable) na maaaring i-customize gamit ang data para sa mga partikular na gamit.

Tuklasin natin ang mga ito sa aksyon.

### Paggamit ng Mga Halimbawa

Ito ay isang pamamaraan kung saan ginagamit mo ang pangunahing nilalaman upang "pakainin ang modelo" ng ilang mga halimbawa ng nais na output para sa isang tiyak na tagubilin, at hayaan itong hulaan ang pattern para sa nais na output. Batay sa dami ng halimbawa na ibinigay, maaari tayong magkaroon ng zero-shot prompting, one-shot prompting, few-shot prompting, atbp.

Binubuo ang prompt ngayon ng tatlong bahagi:

- Isang paglalarawan ng gawain
- Ilang halimbawa ng nais na output
- Ang simula ng bagong halimbawa (na nagiging implicit na paglalarawan ng gawain)

| Uri ng Pagkatuto | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot         | "The Sun is Shining". Isalin sa Espanyol                                                                                                            | "El Sol está brillando".    |
| One-shot          | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot          | Tumakbo ang manlalaro ng mga base => Baseball <br/> Ang manlalaro ay nag-serve ng ace => Tennis <br/> Ang manlalaro ay nakatama ng six => Cricket <br/> Ang manlalaro ay gumawa ng slam-dunk => | Basketball                  |
|                   |                                                                                                                                                       |                             |

Pansinin kung paano kailangang magbigay tayo ng tahasang tagubilin ("Isalin sa Espanyol") sa zero-shot prompting, ngunit nahuhulaan ito sa one-shot na halimbawa. Ipinapakita ng few-shot na halimbawa kung paano ang pagdaragdag ng mas maraming halimbawa ay nagbibigay-daan sa mga modelo na makagawa ng mas tumpak na mga hulaan nang walang dagdag na mga tagubilin.

### Mga Cue sa Prompt

Isa pang teknik sa paggamit ng pangunahing nilalaman ay magbigay ng _cue_ sa halip na mga halimbawa. Sa kasong ito, binibigyan natin ang modelo ng isang tulong na panimulang bahagi na nagpapakita ng nais na format ng sagot. Pagkatapos ay "tinatanggap ng modelo ang cue" para magpatuloy sa ganoong paraan.

| Bilang ng Cue | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Ang Jupiter ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Sistema ng Araw. Isa itong gas giant na may mass na isa-sa-mil mula sa Araw, ngunit dalawang kalahati beses na mas malaki kaysa sa lahat ng iba pang mga planeta sa Sistema ng Araw na pinagsama-sama. Ang Jupiter ay isa sa mga pinaka-maliwanag na bagay na makikita ng hubad na mata sa kalangitan sa gabi, at kilala na ito ng mga sinaunang kabihasnan bago pa man ang nakasulat na kasaysayan. <br/>**Buodin Ito**                                       | Ang Jupiter ang pinakamalaking planeta sa ating Sistema ng Araw at ang ikalimang planeta mula sa Araw. Isa itong gas giant na may mass na 1/1000 ng masa ng Araw, ngunit mas mabigat kaysa sa lahat ng iba pang mga planeta na pinagsama-sama. Matagal na itong kilala ng mga sinaunang kabihasnan at madaling makita sa kalangitan sa gabi. |
| 1              | Ang Jupiter ay ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Solar System. Isa itong gas giant na may masa isang-palahibog na bahagi ng Araw, ngunit dalawang at kalahating beses na mas malaki kaysa sa lahat ng ibang planeta sa Solar System na pinagsama-sama. Ang Jupiter ay isa sa mga pinakamaliwanag na bagay na nakikita ng hubad na mata sa gabi, at kilala na ito sa mga sinaunang sibilisasyon bago pa man magsimulang itala ang kasaysayan. <br/>**Buodin Ito** <br/> Ang natutunan natin ay na ang Jupiter | ay ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Solar System. Isa itong gas giant na may masa isang-palahibog na bahagi ng Araw, ngunit dalawang at kalahating beses na mas malaki kaysa sa lahat ng ibang planeta na pinagsama-sama. Madali itong makita ng hubad na mata at kilala na mula pa noong sinaunang panahon.                        |
| 2              | Ang Jupiter ay ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Solar System. Isa itong gas giant na may masa isang-palahibog na bahagi ng Araw, ngunit dalawang at kalahating beses na mas malaki kaysa sa lahat ng ibang planeta sa Solar System na pinagsama-sama. Ang Jupiter ay isa sa mga pinakamaliwanag na bagay na nakikita ng hubad na mata sa gabi, at kilala na ito sa mga sinaunang sibilisasyon bago pa man magsimulang itala ang kasaysayan. <br/>**Buodin Ito** <br/> Nangungunang 3 Katotohanan na Natutunan:         | 1. Ang Jupiter ay ang ikalimang planeta mula sa Araw at ang pinakamalaki sa Solar System. <br/> 2. Isa itong gas giant na may masa isang-palahibog na bahagi ng Araw...<br/> 3. Ang Jupiter ay nakikita ng hubad na mata mula pa noong sinaunang panahon ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

Ang prompt template ay isang _naunang natukoy na recipe para sa isang prompt_ na maaaring itago at gamitin muli kung kinakailangan, upang maghatid ng mas consistent na karanasan sa mga gumagamit sa mas malaking saklaw. Sa pinakapayak nitong anyo, ito ay simpleng koleksyon ng mga halimbawa ng prompt tulad ng [ito mula sa OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) na nagbibigay ng parehong mga bahagi ng interactive prompt (mga mensahe ng user at system) at ang format ng kahilingan na pinapatakbo ng API - upang suportahan ang muling paggamit.

Sa mas komplikadong anyo nito tulad ng [halimbawa mula sa LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) ito ay naglalaman ng mga _placeholder_ na maaaring palitan ng data mula sa iba't ibang mapagkukunan (input ng user, konteksto ng system, panlabas na mga mapagkukunan ng data, atbp.) upang dinamiko na makagawa ng prompt. Pinapayagan tayo nitong lumikha ng isang library ng mga reusable prompt na maaaring gamitin upang maghatid ng consistent na karanasan ng user **programmatically** sa malawakang sukat.

Sa huli, ang tunay na halaga ng mga template ay nakasalalay sa kakayahang lumikha at maglathala ng mga _prompt libraries_ para sa mga vertikal na larangan ng aplikasyon - kung saan ang prompt template ay ngayon _na-optimize_ upang ipakita ang konteksto o mga halimbawang espesipiko sa aplikasyon na ginagawang mas kaugnay at tumpak ang mga sagot para sa target na user audience. Ang repository na [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) ay isang mahusay na halimbawa ng ganitong pamamaraan, na nag-aayos ng isang library ng mga prompt para sa larangan ng edukasyon na may diin sa mga pangunahing layunin tulad ng pagpaplano ng aralin, disenyo ng kurikulum, pagtuturo sa estudyante, atbp.

## Supporting Content

Kung iisipin natin ang prompt construction bilang isang instruction (gawain) at isang target (pangunahing nilalaman), ang _sekondaryang nilalaman_ ay parang karagdagang konteksto na ibinibigay natin upang **impluwensyahan ang output sa isang paraan**. Maaaring ito ay tuning parameters, mga instruksiyon sa pag-format, mga taxonomy ng paksa, atbp., na tumutulong sa modelo upang _iangkop_ ang tugon nito upang umangkop sa nais na layunin o inaasahan ng user.

Halimbawa: Kung bibigyan ng katalogo ng kurso na may malawak na metadata (pangalan, paglalarawan, antas, mga metadata tag, instruktor, atbp.) sa lahat ng mga available na kurso sa kurikulum:

- maaari nating idefine ang isang instruction na "buodin ang katalogo ng kurso para sa Fall 2023"
- maaari nating gamitin ang pangunahing nilalaman para magbigay ng ilang halimbawa ng nais na output
- maaari nating gamitin ang sekondaryang nilalaman para tukuyin ang nangungunang 5 "tag" na interes.

Ngayon, maaaring magbigay ang modelo ng buod sa format na ipinakita ng ilang halimbawa - ngunit kung ang isang resulta ay may maraming tag, maaaring unahin nito ang 5 tag na tinukoy sa sekondaryang nilalaman.

---

<!--
LESSON TEMPLATE:
Ang yunit na ito ay dapat sumaklaw sa pangunahing konsepto #1.
Patatagin ang konsepto gamit ang mga halimbawa at sanggunian.

KONSEPTO #3:
Mga Teknik sa Prompt Engineering.
Ano ang ilang mga pangunahing teknik para sa prompt engineering?
Ilarawan ito sa pamamagitan ng ilang mga pagsasanay.
-->

## Prompting Best Practices

Ngayon na alam na natin kung paano maaaring _ilikha_ ang mga prompt, maaari na tayong magsimulang mag-isip kung paano _idisain_ ang mga ito upang ipakita ang pinakamahusay na mga kasanayan. Maaaring hatiin natin ito sa dalawang bahagi - ang pagkakaroon ng tamang _pag-iisip_ at paglalapat ng tamang _teknik_.

### Prompt Engineering Mindset

Ang Prompt Engineering ay isang proseso ng trial-and-error kaya't tandaan ang tatlong malalawak na gabay:

1. **Mahalaga ang Pag-unawa sa Domain.** Ang katumpakan at kaugnayan ng tugon ay nakasalalay sa _domain_ kung saan gumagana ang aplikasyon o user. Iaplay ang iyong intuwisyon at kadalubhasaan sa domain upang **i-customize ang mga teknik** nang higit pa. Halimbawa, idefine ang _domain-specific personalities_ sa iyong mga system prompt, o gumamit ng _domain-specific templates_ sa iyong mga user prompt. Magbigay ng sekondaryang nilalaman na sumasalamin sa mga kontekstong espesipiko ng domain, o gumamit ng _domain-specific cues at mga halimbawa_ upang gabayan ang modelo patungo sa pamilyar na mga pattern ng paggamit.

2. **Mahalaga ang Pag-unawa sa Modelo.** Alam natin na ang mga modelo ay stochastic sa kanilang likas na katangian. Ngunit maaaring mag-iba rin ang mga implementasyon ng modelo depende sa dataset ng pagsasanay na ginamit nila (pre-trained na kaalaman), ang mga kakayahan na ibinibigay nila (hal., sa pamamagitan ng API o SDK) at ang uri ng nilalang na kanilang ina-optimize (hal., code kumpara sa mga imahe kumpara sa teksto). Unawain ang mga kalakasan at limitasyon ng modelong iyong ginagamit, at gamitin ang kaalamang iyon upang _bigyang-prayoridad ang mga gawain_ o bumuo ng _customized templates_ na naaangkop sa mga kakayahan ng modelo.

3. **Mahalaga ang Iterasyon at Validasyon.** Ang mga modelo ay mabilis na umuunlad, gayundin ang mga teknik para sa prompt engineering. Bilang isang eksperto sa domain, maaaring mayroon kang iba pang konteksto o mga pamantayan para sa _iyong_ espesipikong aplikasyon, na maaaring hindi naaangkop sa mas malaking komunidad. Gumamit ng mga tool at teknik sa prompt engineering upang "mag-umpisa" ng prompt construction, pagkatapos ay i-iterate at i-validate ang mga resulta gamit ang iyong sariling intuwisyon at kadalubhasaan sa domain. Irekord ang iyong mga insight at lumikha ng isang **knowledge base** (hal., mga prompt libraries) na maaaring gamitin bilang bagong baseline ng iba, para sa mas mabilis na iteration sa hinaharap.

## Best Practices

Ngayon, tingnan natin ang mga karaniwang pinakamahusay na kasanayan na inirerekomenda ng [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) at mga practitioner ng [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Ano                               | Bakit                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Suriin ang pinakabagong mga modelo.       | Malamang na may pinabuting mga tampok at kalidad ang mga bagong henerasyon ng modelo - ngunit maaaring magdulot din ng mas mataas na gastos. Suriin ang mga ito para sa epekto, pagkatapos ay gumawa ng mga desisyon para sa migrasyon.               |
| Hiwalayin ang mga tagubilin at konteksto   | Suriin kung ang iyong modelo/provider ay nagtatakda ng mga _delimiter_ upang malinaw na maiba ang tagubilin, pangunahing at sekondaryang nilalaman. Makakatulong ito sa mga modelo na maglaan ng mas tumpak na bigat sa mga token.                    |
| Maging tiyak at malinaw             | Magbigay ng higit pang detalye tungkol sa nais na konteksto, resulta, haba, format, estilo, atbp. Mapapabuti nito ang kalidad at konsistensya ng mga tugon. I-record ang mga recipe sa mga reusable template.                                         |
| Maging deskriptibo, gumamit ng mga halimbawa      | Mas maganda ang tugon ng mga modelo sa "ipakita at sabihin" na pamamaraan. Magsimula sa isang `zero-shot` na paraan kung saan bibigyan mo ng tagubilin (ngunit walang mga halimbawa) at subukan ang `few-shot` bilang refinement, na nagbibigay ng ilang halimbawa ng nais na output. Gumamit ng mga analogiya. |
| Gumamit ng mga cues upang pagsimulan ang mga kompletong sagot | Pasilipin ito patungo sa isang nais na resulta sa pamamagitan ng pagbibigay ng mga pangungusap o pariralang maaring gamitin bilang panimulang punto sa tugon.                                                                                               |
| Ulitin kung kinakailangan                       | Minsan kailangan mong ulitin ang iyong sarili sa modelo. Magbigay ng mga tagubilin bago at pagkatapos ng iyong pangunahing nilalaman, gumamit ng tagubilin at cue, atbp. Ulitin at i-validate upang makita kung ano ang gumagana.                   |
| Mahalaga ang pagkakasunod-sunod                     | Ang pagkakasunod-sunod ng pag-presenta ng impormasyon sa modelo ay maaaring makaapekto sa output, kahit sa mga halimbawang panturo, dahil sa recency bias. Subukan ang iba't ibang mga opsyon upang makita kung ano ang pinakamahusay.                  |
| Bigyan ang modelo ng “out” na opsyon           | Bigyan ang modelo ng isang _fallback_ na tugon na maaari nitong ibigay kung hindi nito makumpleto ang gawain sa anumang kadahilanan. Makakatulong ito upang mabawasan ang pagkakataon na lumikha ng mga maling o gawa-gawang sagot ang mga modelo.    |
|                                   |                                                                                                                                                                                                                                                   |

Tulad ng anumang pinakamahusay na kasanayan, tandaan na _maaaring magkaiba ang iyong karanasan_ depende sa modelo, gawain at domain. Gamitin ang mga ito bilang panimulang punto, at ulitin upang hanapin kung ano ang pinakamahusay para sa iyo. Patuloy na suriin muli ang iyong proseso sa prompt engineering habang may mga bagong modelo at tool na lumalabas, na may pokus sa scalability ng proseso at kalidad ng tugon.

<!--
LESSON TEMPLATE:
Dapat magbigay ang yunit na ito ng hamon sa code kung naaangkop

HAMON:
Link sa isang Jupyter Notebook na may mga komentaryo lamang sa code bilang mga instruksiyon (mga seksyon ng code ay walang laman).

SOLUSYON:
Link sa isang kopya ng Notebook na may mga prompt na napunan at naipatupad, na nagpapakita ng isang halimbawa ng output.
-->

## Assignment

Binabati kita! Nakamit mo ang dulo ng aralin! Panahon na upang isubok ang ilan sa mga konsepto at teknik gamit ang mga totoong halimbawa!

Para sa ating assignment, gagamit tayo ng isang Jupyter Notebook na may mga pagsasanay na maaari mong gawin nang interaktibo. Maaari mo ring dagdagan ang Notebook ng iyong sariling mga Markdown at Code cells upang tuklasin ang mga ideya at teknik nang mag-isa.

### Upang makapagsimula, i-fork ang repo, pagkatapos ay

- (Inirerekomenda) Ilunsad ang GitHub Codespaces
- (Alternatibo) I-clone ang repo sa iyong lokal na aparato at gamitin ito sa Docker Desktop
- (Alternatibo) Buksan ang Notebook gamit ang iyong paboritong Notebook runtime environment.

### Susunod, i-configure ang iyong mga environment variable

- Kopyahin ang `.env.copy` na file sa root ng repo papuntang `.env` at punan ang mga halaga ng `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, at `AZURE_OPENAI_DEPLOYMENT`. Bumisita muli sa [Learning Sandbox section](#learning-sandbox) para matutunan kung paano.

### Susunod, buksan ang Jupyter Notebook

- Piliin ang runtime kernel. Kung gagamitin ang opsyon 1 o 2, piliin lamang ang default na Python 3.10.x kernel na ibinibigay ng dev container.

Handa ka nang patakbuhin ang mga pagsasanay. Tandaan na walang mga _tama o maling_ sagot dito - ito ay tungkol sa pagsubok ng mga opsyon gamit ang trial-and-error at pagbuo ng intuwisyon kung ano ang gumagana para sa isang partikular na modelo at domain ng aplikasyon.

_Dahil dito, walang mga Code Solution segments sa araling ito. Sa halip, ang Notebook ay magkakaroon ng mga Markdown cells na may titulong "My Solution:" na nagpapakita ng isang halimbawa ng output bilang sanggunian._

<!--
LESSON TEMPLATE:
Balutin ang seksyon ng buod at mga mapagkukunan para sa sariling pag-aaral.
-->

## Pagsusuri ng Kaalaman

Alin sa mga sumusunod ang isang magandang prompt na sumusunod sa makatuwirang pinakamahusay na mga kasanayan?

1. Ipakita sa akin ang larawan ng pulang kotse
2. Ipakita sa akin ang larawan ng pulang kotse na make Volvo at model XC90 na nakaparada sa tabi ng bangin habang lumulubog ang araw
3. Ipakita sa akin ang larawan ng pulang kotse na make Volvo at model XC90

Sagot: 2, ito ang pinakamahusay na prompt dahil ito ay nagbibigay ng detalye tungkol sa "ano" at naglalahad ng espesipiko (hindi basta kotse kundi isang partikular na make at model) at inilalarawan din ang kabuuang eksena. Ang 3 ang kasunod na pinakamaganda dahil naglalaman din ito ng maraming paglalarawan.

## 🚀 Hamon

Subukan kung magagamit mo ang teknik ng "cue" gamit ang prompt: Kumpletuhin ang pangungusap "Ipakita sa akin ang larawan ng pulang kotse na make Volvo at ". Ano ang sagot nito, at paano mo ito pagbutihin?

## Mahusay na Gawain! Ipagpatuloy ang Iyong Pag-aaral

Nais mo bang matuto nang higit pa tungkol sa iba't ibang konsep ng Prompt Engineering? Pumunta sa [pahina ng patuloy na pag-aaral](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang makita ang iba pang magagandang mapagkukunan tungkol sa paksang ito.

Pumunta sa Lesson 5 kung saan tatalakayin natin ang [advanced prompting techniques](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->