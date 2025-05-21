<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T23:02:28+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "tl"
}
-->
# Pag-secure sa Iyong Mga Aplikasyon ng Generative AI

## Panimula

Saklaw ng araling ito:

- Seguridad sa konteksto ng mga sistema ng AI.
- Karaniwang panganib at banta sa mga sistema ng AI.
- Mga pamamaraan at konsiderasyon para sa pag-secure ng mga sistema ng AI.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, magkakaroon ka ng kaalaman sa:

- Mga banta at panganib sa mga sistema ng AI.
- Karaniwang pamamaraan at praktis para sa pag-secure ng mga sistema ng AI.
- Paano ang pagsasagawa ng security testing ay makakapigil sa mga hindi inaasahang resulta at pagkawala ng tiwala ng mga gumagamit.

## Ano ang kahulugan ng seguridad sa konteksto ng generative AI?

Habang ang teknolohiya ng Artificial Intelligence (AI) at Machine Learning (ML) ay patuloy na humuhubog sa ating mga buhay, mahalaga na protektahan hindi lamang ang data ng mga customer kundi pati na rin ang mga sistema ng AI mismo. Ang AI/ML ay lalong ginagamit sa suporta ng mga proseso ng paggawa ng desisyon na may mataas na halaga sa mga industriya kung saan ang maling desisyon ay maaaring magdulot ng seryosong mga kahihinatnan.

Narito ang mga pangunahing punto na dapat isaalang-alang:

- **Epekto ng AI/ML**: May malaking epekto ang AI/ML sa pang-araw-araw na buhay at dahil dito, ang pagprotekta sa kanila ay naging mahalaga.
- **Mga Hamon sa Seguridad**: Ang epekto na ito ng AI/ML ay nangangailangan ng tamang atensyon upang matugunan ang pangangailangan na protektahan ang mga produktong AI mula sa mga sopistikadong pag-atake, maging mula sa mga troll o organisadong grupo.
- **Mga Problema sa Estratehiya**: Ang industriya ng teknolohiya ay dapat na maagap na tugunan ang mga hamon sa estratehiya upang masiguro ang pangmatagalang kaligtasan ng customer at seguridad ng data.

Dagdag pa rito, ang mga modelo ng Machine Learning ay kadalasang hindi makakakilala sa pagitan ng malisyosong input at benign anomalous data. Ang isang mahalagang pinagmulan ng data sa pagsasanay ay nagmumula sa hindi na-curate, hindi na-moderate, pampublikong datasets, na bukas sa kontribusyon ng ikatlong partido. Hindi kailangang i-kompromiso ng mga umaatake ang mga datasets kapag malaya silang makapag-ambag sa mga ito. Sa paglipas ng panahon, ang low-confidence na malisyosong data ay nagiging high-confidence na pinagkakatiwalaang data, kung ang istruktura/pag-format ng data ay nananatiling tama.

Ito ang dahilan kung bakit kritikal na tiyakin ang integridad at proteksyon ng mga data stores na ginagamit ng iyong mga modelo sa paggawa ng desisyon.

## Pag-unawa sa mga banta at panganib ng AI

Sa mga tuntunin ng AI at mga kaugnay na sistema, ang data poisoning ay namumukod-tangi bilang pinakamahalagang banta sa seguridad ngayon. Ang data poisoning ay kapag may sinadyang pagbabago sa impormasyong ginagamit sa pagsasanay ng AI, na nagiging sanhi ng paggawa nito ng mga pagkakamali. Ito ay dahil sa kawalan ng mga pamantayan sa pagtuklas at pag-iwas, kasabay ng ating pag-asa sa hindi mapagkakatiwalaan o hindi na-curate na pampublikong datasets para sa pagsasanay. Upang mapanatili ang integridad ng data at maiwasan ang isang depektibong proseso ng pagsasanay, mahalaga na subaybayan ang pinagmulan at pinagmulan ng iyong data. Kung hindi, ang lumang kasabihan na "garbage in, garbage out" ay nagiging totoo, na humahantong sa kompromisadong pagganap ng modelo.

Narito ang mga halimbawa kung paano maaaring makaapekto ang data poisoning sa iyong mga modelo:

1. **Pagbaliktad ng Label**: Sa isang binary classification task, sinadyang binabaliktad ng isang kalaban ang mga label ng isang maliit na subset ng training data. Halimbawa, ang benign samples ay nilalagyan ng label na malisyoso, na nagiging sanhi ng maling asosasyon ng modelo.\
   **Halimbawa**: Ang isang spam filter na maling nag-uuri ng lehitimong emails bilang spam dahil sa mga manipulated labels.
2. **Pagkalason ng Feature**: Ang isang umaatake ay palihim na binabago ang mga feature sa training data upang magpakilala ng bias o iligaw ang modelo.\
   **Halimbawa**: Ang pagdaragdag ng mga hindi kaugnay na keywords sa mga paglalarawan ng produkto upang manipulahin ang mga sistema ng rekomendasyon.
3. **Pag-inject ng Data**: Pag-inject ng malisyosong data sa training set upang impluwensyahan ang pag-uugali ng modelo.\
   **Halimbawa**: Ang pagpapakilala ng pekeng user reviews upang baguhin ang mga resulta ng sentiment analysis.
4. **Backdoor Attacks**: Ang isang kalaban ay naglalagay ng nakatagong pattern (backdoor) sa training data. Natutunan ng modelo na kilalanin ang pattern na ito at kumikilos nang malisyoso kapag na-trigger.\
   **Halimbawa**: Ang isang face recognition system na sinanay sa mga backdoored images na maling kinikilala ang isang partikular na tao.

Ang MITRE Corporation ay lumikha ng [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), isang knowledgebase ng mga taktika at teknolohiya na ginagamit ng mga kalaban sa mga tunay na pag-atake sa mga sistema ng AI.

> Mayroong lumalaking bilang ng mga kahinaan sa mga sistemang pinagana ng AI, dahil ang pagsasama ng AI ay nagpapalawak sa attack surface ng mga umiiral na sistema sa kabila ng mga tradisyunal na cyber-attacks. Binuo namin ang ATLAS upang itaas ang kamalayan sa mga natatangi at umuusbong na mga kahinaan na ito, habang ang pandaigdigang komunidad ay lalong isinasama ang AI sa iba't ibang sistema. Ang ATLAS ay naka-modelo sa MITRE ATT&CK® framework at ang mga taktika, teknolohiya, at pamamaraan (TTPs) nito ay komplementaryo sa mga nasa ATT&CK.

Katulad ng MITRE ATT&CK® framework, na malawakang ginagamit sa tradisyunal na cybersecurity para sa pagpaplano ng advanced threat emulation scenarios, nagbibigay ang ATLAS ng madaling ma-search na set ng TTPs na makakatulong sa mas mahusay na pag-unawa at paghahanda sa depensa laban sa mga umuusbong na pag-atake.

Dagdag pa rito, ang Open Web Application Security Project (OWASP) ay lumikha ng isang "[Top 10 list](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" ng mga pinaka-kritikal na kahinaan na natagpuan sa mga aplikasyon na gumagamit ng LLMs. Ang listahan ay nagha-highlight sa mga panganib ng mga banta tulad ng nabanggit na data poisoning kasama ang iba pa tulad ng:

- **Prompt Injection**: Isang teknik kung saan ang mga umaatake ay manipulahin ang isang Large Language Model (LLM) sa pamamagitan ng maingat na crafted inputs, na nagiging sanhi ng pag-uugali nito sa labas ng inaasahang pag-uugali.
- **Supply Chain Vulnerabilities**: Ang mga komponent at software na bumubuo sa mga aplikasyon na ginagamit ng isang LLM, tulad ng mga Python modules o external datasets, ay maaaring ma-kompromiso na nagreresulta sa hindi inaasahang mga resulta, ipinakilala ang mga biases at maging mga kahinaan sa ilalim na imprastraktura.
- **Overreliance**: Ang mga LLMs ay mahina at may tendensiyang mag-hallucinate, nagbibigay ng hindi tumpak o hindi ligtas na mga resulta. Sa ilang dokumentadong pagkakataon, ang mga tao ay kinuha ang mga resulta nang literal na nagreresulta sa hindi inaasahang mga negatibong kahihinatnan sa tunay na mundo.

Si Microsoft Cloud Advocate Rod Trent ay sumulat ng isang libreng ebook, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), na naglalalim sa mga ito at iba pang umuusbong na banta ng AI at nagbibigay ng malawak na gabay sa kung paano pinakamahusay na harapin ang mga sitwasyong ito.

## Security Testing para sa mga Sistema ng AI at LLMs

Ang artificial intelligence (AI) ay nagbabago sa iba't ibang larangan at industriya, nag-aalok ng mga bagong posibilidad at benepisyo para sa lipunan. Gayunpaman, ang AI ay nagdadala rin ng mahahalagang hamon at panganib, tulad ng privacy ng data, bias, kawalan ng paliwanag, at potensyal na maling paggamit. Samakatuwid, mahalaga na tiyakin na ang mga sistema ng AI ay ligtas at responsable, nangangahulugang sumusunod sila sa mga pamantayan sa etika at batas at maaasahan ng mga gumagamit at stakeholder.

Ang security testing ay ang proseso ng pag-evaluate ng seguridad ng isang sistema ng AI o LLM, sa pamamagitan ng pagtukoy at pagsasamantala sa kanilang mga kahinaan. Ito ay maaaring isagawa ng mga developer, gumagamit, o third-party auditors, depende sa layunin at saklaw ng testing. Ang ilan sa mga pinaka-karaniwang pamamaraan ng security testing para sa mga sistema ng AI at LLMs ay:

- **Data sanitization**: Ito ang proseso ng pagtanggal o pag-anonymize ng sensitibo o pribadong impormasyon mula sa training data o input ng isang sistema ng AI o LLM. Ang data sanitization ay makakatulong sa pag-iwas sa pagtagas ng data at malisyosong manipulasyon sa pamamagitan ng pagbabawas ng exposure ng kumpidensyal o personal na data.
- **Adversarial testing**: Ito ang proseso ng pagbuo at pag-aaplay ng mga adversarial examples sa input o output ng isang sistema ng AI o LLM upang i-evaluate ang tibay at katatagan nito laban sa mga adversarial attacks. Ang adversarial testing ay makakatulong sa pagtukoy at pag-iwas sa mga kahinaan at kahinaan ng isang sistema ng AI o LLM na maaaring samantalahin ng mga umaatake.
- **Model verification**: Ito ang proseso ng pag-verify sa tama at kumpleto ng mga parameter ng modelo o arkitektura ng isang sistema ng AI o LLM. Ang model verification ay makakatulong sa pagtuklas at pag-iwas sa pagnanakaw ng modelo sa pamamagitan ng pagtiyak na ang modelo ay protektado at authenticated.
- **Output validation**: Ito ang proseso ng pag-validate sa kalidad at pagiging maaasahan ng output ng isang sistema ng AI o LLM. Ang output validation ay makakatulong sa pagtukoy at pagwasto ng malisyosong manipulasyon sa pamamagitan ng pagtiyak na ang output ay pare-pareho at tumpak.

Ang OpenAI, isang lider sa mga sistema ng AI, ay nag-set up ng isang serye ng _safety evaluations_ bilang bahagi ng kanilang red teaming network initiative, na naglalayong i-test ang output ng mga sistema ng AI sa pag-asa na makapag-ambag sa AI safety.

> Ang mga evaluation ay maaaring saklaw mula sa simpleng Q&A tests hanggang sa mas kumplikadong simulations. Bilang mga konkretong halimbawa, narito ang mga sample evaluations na binuo ng OpenAI para sa pag-evaluate ng mga pag-uugali ng AI mula sa iba't ibang anggulo:

#### Persuasion

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay ang isang sistema ng AI na makapagpabago sa isa pang sistema ng AI na sabihin ang isang lihim na salita?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay ang isang sistema ng AI na makapagpabago sa isa pang sistema ng AI na mag-donate ng pera?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay ang isang sistema ng AI na makapagpabago sa suporta ng isa pang sistema ng AI sa isang proposisyon sa politika?

#### Steganography (nakatagong mensahe)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay ang isang sistema ng AI na makapagpasa ng lihim na mensahe nang hindi nahuhuli ng isa pang sistema ng AI?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay ang isang sistema ng AI na makapag-compress at decompress ng mga mensahe, upang makapagbigay-daan sa pagtatago ng lihim na mensahe?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay ang isang sistema ng AI na makipag-ugnayan sa isa pang sistema ng AI, nang walang direktang komunikasyon?

### Seguridad ng AI

Mahalaga na layunin nating protektahan ang mga sistema ng AI mula sa malisyosong pag-atake, maling paggamit, o hindi inaasahang mga kahihinatnan. Kasama rito ang pagkuha ng mga hakbang upang masiguro ang kaligtasan, pagiging maaasahan, at tiwala sa mga sistema ng AI, tulad ng:

- Pag-secure ng data at algorithms na ginagamit sa pagsasanay at pagpapatakbo ng mga modelo ng AI
- Pag-iwas sa hindi awtorisadong pag-access, manipulasyon, o pagsabotahe ng mga sistema ng AI
- Pagtukoy at pag-iwas sa bias, diskriminasyon, o isyu sa etika sa mga sistema ng AI
- Pagtiyak sa accountability, transparency, at explainability ng mga desisyon at aksyon ng AI
- Pag-align ng mga layunin at halaga ng mga sistema ng AI sa mga ng tao at lipunan

Ang seguridad ng AI ay mahalaga para sa pagtiyak ng integridad, availability, at confidentiality ng mga sistema ng AI at data. Ang ilan sa mga hamon at oportunidad ng seguridad ng AI ay:

- Oportunidad: Pagsasama ng AI sa mga estratehiya sa cybersecurity dahil maaari itong maglaro ng mahalagang papel sa pagtukoy ng mga banta at pagpapabuti ng mga oras ng pagtugon. Ang AI ay makakatulong sa pag-automate at pag-augment ng pagtukoy at pag-iwas sa mga cyberattacks, tulad ng phishing, malware, o ransomware.
- Hamon: Ang AI ay maaari ring gamitin ng mga kalaban upang maglunsad ng sopistikadong pag-atake, tulad ng pagbuo ng pekeng o nakaliligaw na nilalaman, paggaya sa mga gumagamit, o pagsasamantala sa mga kahinaan sa mga sistema ng AI. Samakatuwid, ang mga developer ng AI ay may natatanging responsibilidad na magdisenyo ng mga sistema na matibay at matatag laban sa maling paggamit.

### Proteksyon ng Data

Ang mga LLMs ay maaaring magdulot ng panganib sa privacy at seguridad ng data na kanilang ginagamit. Halimbawa, ang mga LLMs ay maaaring potensyal na mag-memorize at mag-leak ng sensitibong impormasyon mula sa kanilang training data, tulad ng mga personal na pangalan, address, password, o numero ng credit card. Maaari rin silang manipulahin o atakehin ng mga malisyosong aktor na gustong samantalahin ang kanilang mga kahinaan o biases. Samakatuwid, mahalaga na maging maalam sa mga panganib na ito at kumuha ng mga naaangkop na hakbang upang protektahan ang data na ginagamit sa mga LLMs. Mayroong ilang mga hakbang na maaari mong gawin upang protektahan ang data na ginagamit sa mga LLMs. Kasama sa mga hakbang na ito ang:

- **Paglilimita sa dami at uri ng data na kanilang ibinabahagi sa mga LLMs**: Ibahagi lamang ang data na kinakailangan at nauugnay para sa mga inaasahang layunin, at iwasan ang pagbabahagi ng anumang data na sensitibo, kumpidensyal, o personal. Ang mga gumagamit ay dapat ding i-anonymize o i-encrypt ang data na kanilang ibinabahagi sa mga LLMs, tulad ng sa pamamagitan ng pagtanggal o pag-mask sa anumang impormasyon na nagpapakilala, o paggamit ng mga secure na komunikasyon channels.
- **Pag-verify sa data na binuo ng mga LLMs**: Palaging i-check ang katumpakan at kalidad ng output na binuo ng mga LLMs upang masiguro na wala silang hindi nais o hindi angkop na impormasyon.
- **Pag-uulat at pag-alerto sa anumang paglabag sa data o insidente**: Maging mapagbantay sa anumang kahina-hinala o abnormal na mga aktibidad o pag-uugali mula sa mga LLMs, tulad ng pagbuo ng mga teksto na hindi nauugnay, hindi tama, nakakasakit, o nakakapinsala. Ito ay maaaring maging indikasyon ng paglabag sa data o insidente sa seguridad.

Ang seguridad ng data, pamamahala, at pagsunod ay kritikal para sa anumang organisasyon na nais na magamit ang kapangyarihan ng data at AI sa isang multi-cloud na kapaligiran. Ang pag-secure at pamamahala sa lahat ng iyong data ay isang kumplikado at maraming aspeto na gawain. Kailangan mong i-secure at pamahalaan ang iba't ibang uri ng data (structured, unstructured, at data na binuo ng AI) sa iba't ibang lokasyon sa maraming ulap, at kailangan mong isaalang-alang ang umiiral at hinaharap na seguridad ng data, pamamahala, at regulasyon ng AI. Upang protektahan ang iyong data, kailangan mong magpatibay ng ilang mga pinakamahusay na praktis at pag-iingat

**Pagtanggi**:  
Ang dokumentong ito ay isinalin gamit ang AI na serbisyo sa pagsasalin [Co-op Translator](https://github.com/Azure/co-op-translator). Habang nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang mapagkukunan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.