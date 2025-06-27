<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:33:30+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "tl"
}
-->
# Pag-secure ng Iyong Generative AI Applications

## Panimula

Saklaw ng leksyong ito:

- Seguridad sa konteksto ng mga AI system.
- Karaniwang panganib at banta sa mga AI system.
- Mga pamamaraan at konsiderasyon para sa pag-secure ng mga AI system.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang leksyong ito, magkakaroon ka ng kaalaman tungkol sa:

- Mga banta at panganib sa mga AI system.
- Karaniwang mga pamamaraan at kasanayan para sa pag-secure ng mga AI system.
- Paano makakatulong ang pagpapatupad ng security testing sa pag-iwas sa hindi inaasahang resulta at pagkawala ng tiwala ng gumagamit.

## Ano ang kahulugan ng seguridad sa konteksto ng generative AI?

Habang ang mga teknolohiya ng Artificial Intelligence (AI) at Machine Learning (ML) ay patuloy na humuhubog sa ating buhay, mahalagang protektahan hindi lamang ang data ng mga customer kundi pati na rin ang mga AI system mismo. Ang AI/ML ay lalong ginagamit sa suporta ng mga proseso ng paggawa ng desisyon sa mga industriya kung saan ang maling desisyon ay maaaring magresulta sa seryosong kahihinatnan.

Narito ang mga pangunahing puntong dapat isaalang-alang:

- **Epekto ng AI/ML**: Ang AI/ML ay may makabuluhang epekto sa pang-araw-araw na buhay at dahil dito, ang pagprotekta sa kanila ay naging mahalaga.
- **Mga Hamon sa Seguridad**: Ang epekto ng AI/ML ay nangangailangan ng wastong atensyon upang matugunan ang pangangailangang protektahan ang mga produktong batay sa AI mula sa mga sopistikadong pag-atake, maging ito ay mula sa mga trolls o organisadong grupo.
- **Mga Estratehikong Problema**: Dapat maagap na tugunan ng industriya ng teknolohiya ang mga estratehikong hamon upang matiyak ang pangmatagalang kaligtasan ng customer at seguridad ng data.

Bukod pa rito, karamihan sa mga Machine Learning model ay hindi makilala ang pagkakaiba sa pagitan ng mapanlinlang na input at benign anomalous data. Isang makabuluhang pinagmumulan ng training data ay nagmumula sa hindi naayos, hindi na-moderate, pampublikong datasets, na bukas sa kontribusyon ng mga third-party. Hindi kailangang i-kompromiso ng mga umaatake ang datasets kapag malaya silang makapag-ambag dito. Sa paglipas ng panahon, ang mababang kumpiyansang mapanlinlang na data ay nagiging mataas na kumpiyansang pinagkakatiwalaang data, kung ang istruktura/pag-format ng data ay nananatiling tama.

Ito ang dahilan kung bakit kritikal na tiyakin ang integridad at proteksyon ng mga data store na ginagamit ng iyong mga modelo sa paggawa ng desisyon.

## Pag-unawa sa mga banta at panganib ng AI

Sa mga tuntunin ng AI at mga kaugnay na sistema, ang data poisoning ay namumukod-tangi bilang pinaka-makabuluhang banta sa seguridad sa ngayon. Ang data poisoning ay kapag may sadyang binabago ang impormasyon na ginagamit sa pag-train ng isang AI, na nagiging sanhi ng paggawa nito ng mga pagkakamali. Ito ay dahil sa kawalan ng mga standardized na pamamaraan sa pagtuklas at pag-iwas, kasabay ng ating pag-asa sa hindi mapagkakatiwalaan o hindi naayos na pampublikong datasets para sa pag-train. Upang mapanatili ang integridad ng data at maiwasan ang isang may depektong proseso ng pag-train, mahalagang subaybayan ang pinagmulan at pinagmulan ng iyong data. Kung hindi, ang lumang kasabihan na "garbage in, garbage out" ay totoo, na nagreresulta sa kompromisadong pagganap ng modelo.

Narito ang mga halimbawa kung paano maaaring maapektuhan ng data poisoning ang iyong mga modelo:

1. **Label Flipping**: Sa isang binary classification task, sadyang binabaligtad ng isang kalaban ang mga label ng isang maliit na subset ng training data. Halimbawa, ang mga benign sample ay nilalagyan ng label bilang mapanlinlang, na nagiging sanhi ng maling pagkatuto ng modelo.\
   **Halimbawa**: Ang isang spam filter na maling nag-uuri ng mga lehitimong email bilang spam dahil sa mga manipuladong label.
2. **Feature Poisoning**: Ang isang umaatake ay maingat na binabago ang mga tampok sa training data upang magpakilala ng bias o linlangin ang modelo.\
   **Halimbawa**: Pagdaragdag ng mga hindi kaugnay na keyword sa mga paglalarawan ng produkto upang manipulahin ang mga sistema ng rekomendasyon.
3. **Data Injection**: Pag-inject ng mapanlinlang na data sa training set upang maimpluwensyahan ang pag-uugali ng modelo.\
   **Halimbawa**: Pagpapakilala ng pekeng mga pagsusuri ng gumagamit upang i-skew ang mga resulta ng pagsusuri ng damdamin.
4. **Backdoor Attacks**: Ang isang kalaban ay naglalagay ng nakatagong pattern (backdoor) sa training data. Natututo ang modelo na kilalanin ang pattern na ito at kumikilos ng mapanlinlang kapag na-trigger.\
   **Halimbawa**: Isang sistema ng pagkilala ng mukha na na-train sa mga backdoored na imahe na maling kinikilala ang isang partikular na tao.

Ang MITRE Corporation ay lumikha ng [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), isang knowledgebase ng mga taktika at pamamaraan na ginagamit ng mga kalaban sa mga totoong pag-atake sa mga AI system.

> Dumarami ang bilang ng mga kahinaan sa mga AI-enabled system, habang ang pagsasama ng AI ay nagpapalawak ng attack surface ng mga umiiral na sistema higit pa sa mga tradisyunal na cyber-attacks. Binuo namin ang ATLAS upang itaas ang kamalayan sa mga natatangi at umuusbong na kahinaang ito, habang ang pandaigdigang komunidad ay lalong nagsasama ng AI sa iba't ibang sistema. Ang ATLAS ay ginaya mula sa MITRE ATT&CK® framework at ang mga taktika, pamamaraan, at pamamaraan (TTPs) nito ay komplementaryo sa mga nasa ATT&CK.

Katulad ng MITRE ATT&CK® framework, na malawakang ginagamit sa tradisyunal na cybersecurity para sa pagpaplano ng mga advanced na senaryo ng emulasyon ng banta, ang ATLAS ay nagbibigay ng isang madaling masiyasat na hanay ng TTPs na makakatulong upang mas maunawaan at maghanda para sa pagtatanggol laban sa mga umuusbong na pag-atake.

Bukod pa rito, ang Open Web Application Security Project (OWASP) ay lumikha ng isang "[Top 10 list](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" ng mga pinaka-kritikal na kahinaan na matatagpuan sa mga application na gumagamit ng LLMs. Ang listahan ay nagha-highlight ng mga panganib ng mga banta tulad ng nabanggit na data poisoning kasama ang iba pang tulad ng:

- **Prompt Injection**: isang pamamaraan kung saan ang mga umaatake ay manipulahin ang isang Large Language Model (LLM) sa pamamagitan ng maingat na binalangkas na input, na nagiging sanhi ng pag-uugali nito sa labas ng nilalayong pag-uugali.
- **Supply Chain Vulnerabilities**: Ang mga bahagi at software na bumubuo sa mga application na ginagamit ng isang LLM, tulad ng mga module ng Python o panlabas na datasets, ay maaari ring ma-kompromiso na nagreresulta sa hindi inaasahang resulta, ipinakilala ang mga bias at kahit mga kahinaan sa pinagbabatayang imprastraktura.
- **Overreliance**: Ang LLMs ay may kakulangan at may posibilidad na mag-hallucinate, na nagbibigay ng hindi tumpak o hindi ligtas na mga resulta. Sa ilang naitalang pagkakataon, ang mga tao ay tumanggap ng mga resulta sa halaga ng mukha na nagreresulta sa hindi inaasahang negatibong kahihinatnan sa totoong mundo.

Si Microsoft Cloud Advocate Rod Trent ay nagsulat ng isang libreng ebook, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), na malalim na sumisid sa mga ito at iba pang umuusbong na banta sa AI at nagbibigay ng malawak na gabay kung paano pinakamahusay na tugunan ang mga senaryong ito.

## Security Testing para sa AI Systems at LLMs

Ang artificial intelligence (AI) ay nagbabago ng iba't ibang domain at industriya, nag-aalok ng mga bagong posibilidad at benepisyo para sa lipunan. Gayunpaman, ang AI ay nagdadala rin ng mga makabuluhang hamon at panganib, tulad ng data privacy, bias, kakulangan ng explainability, at potensyal na maling paggamit. Samakatuwid, mahalagang tiyakin na ang mga AI system ay secure at responsable, nangangahulugan na sumusunod sila sa mga pamantayang etikal at legal at maaaring pagkatiwalaan ng mga gumagamit at stakeholder.

Ang security testing ay ang proseso ng pagsusuri ng seguridad ng isang AI system o LLM, sa pamamagitan ng pagtukoy at pagsasamantala sa kanilang mga kahinaan. Ito ay maaaring isagawa ng mga developer, gumagamit, o third-party auditors, depende sa layunin at saklaw ng pagsubok. Ang ilan sa mga pinaka-karaniwang paraan ng security testing para sa mga AI system at LLMs ay:

- **Data sanitization**: Ito ang proseso ng pagtanggal o pag-anonymize ng sensitibo o pribadong impormasyon mula sa training data o input ng isang AI system o LLM. Ang data sanitization ay makakatulong sa pag-iwas sa pagtagas ng data at mapanlinlang na manipulasyon sa pamamagitan ng pagbabawas ng exposure ng kumpidensyal o personal na data.
- **Adversarial testing**: Ito ang proseso ng pagbuo at paglalapat ng mga adversarial na halimbawa sa input o output ng isang AI system o LLM upang suriin ang katatagan at katatagan nito laban sa mga adversarial na pag-atake. Ang adversarial testing ay makakatulong sa pagtukoy at pag-mitigate ng mga kahinaan at kahinaan ng isang AI system o LLM na maaaring pagsamantalahan ng mga umaatake.
- **Model verification**: Ito ang proseso ng pag-verify ng tamang at kumpletong model parameters o architecture ng isang AI system o LLM. Ang model verification ay makakatulong sa pagtuklas at pag-iwas sa pagnanakaw ng modelo sa pamamagitan ng pagtiyak na ang modelo ay protektado at na-authenticate.
- **Output validation**: Ito ang proseso ng pag-validate ng kalidad at pagiging maaasahan ng output ng isang AI system o LLM. Ang output validation ay makakatulong sa pagtukoy at pagwawasto ng mapanlinlang na manipulasyon sa pamamagitan ng pagtiyak na ang output ay pare-pareho at tumpak.

Ang OpenAI, isang lider sa mga AI system, ay nag-setup ng serye ng _safety evaluations_ bilang bahagi ng kanilang red teaming network initiative, na naglalayong subukan ang output AI systems sa pag-asang makapag-ambag sa AI safety.

> Ang mga pagsusuri ay maaaring mula sa simpleng Q&A tests hanggang sa mas kumplikadong mga simulation. Bilang mga kongkretong halimbawa, narito ang mga sample evaluations na binuo ng OpenAI para sa pagsusuri ng mga pag-uugali ng AI mula sa iba't ibang anggulo:

#### Persuasion

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay maaring lokohin ng isang AI system ang isa pang AI system para sabihin ang isang lihim na salita?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay maaring hikayatin ng isang AI system ang isa pang AI system na mag-donate ng pera?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay maaring impluwensyahan ng isang AI system ang suporta ng isa pang AI system sa isang political proposition?

#### Steganography (hidden messaging)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay maaring magpasa ng lihim na mensahe ang isang AI system nang hindi nahuhuli ng isa pang AI system?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay maaring i-compress at i-decompress ng isang AI system ang mga mensahe, upang makapag-enable ng pagtatago ng lihim na mensahe?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Gaano kahusay maaring makipag-coordinate ang isang AI system sa isa pang AI system, nang walang direktang komunikasyon?

### AI Security

Mahalaga na layunin nating protektahan ang mga AI system mula sa mapanlinlang na pag-atake, maling paggamit, o hindi inaasahang kahihinatnan. Kasama rito ang pagkuha ng mga hakbang upang matiyak ang kaligtasan, pagiging maaasahan, at pagtitiwala sa mga AI system, tulad ng:

- Pag-secure ng data at mga algorithm na ginagamit sa pag-train at pagpatakbo ng mga AI model
- Pag-iwas sa hindi awtorisadong pag-access, manipulasyon, o sabotahe ng mga AI system
- Pagtukoy at pag-mitigate ng bias, diskriminasyon, o mga isyu sa etika sa mga AI system
- Pagtitiyak ng accountability, transparency, at explainability ng mga desisyon at aksyon ng AI
- Pag-align ng mga layunin at halaga ng mga AI system sa mga tao at lipunan

Ang AI security ay mahalaga para sa pagtitiyak ng integridad, availability, at pagiging kumpidensyal ng mga AI system at data. Ang ilan sa mga hamon at pagkakataon ng AI security ay:

- Pagkakataon: Pagsasama ng AI sa mga estratehiya sa cybersecurity dahil maaari itong maglaro ng mahalagang papel sa pagtukoy ng mga banta at pagpapabuti ng mga oras ng pagtugon. Makakatulong ang AI na i-automate at palakasin ang pagtukoy at pag-mitigate ng mga cyberattacks, tulad ng phishing, malware, o ransomware.
- Hamon: Ang AI ay maaari ring gamitin ng mga kalaban upang maglunsad ng sopistikadong pag-atake, tulad ng pagbuo ng pekeng o mapanlinlang na nilalaman, pagpapanggap sa mga gumagamit, o pagsasamantala sa mga kahinaan sa mga AI system. Samakatuwid, ang mga AI developer ay may natatanging responsibilidad na magdisenyo ng mga system na matatag at matatag laban sa maling paggamit.

### Data Protection

Ang LLMs ay maaaring magdala ng mga panganib sa privacy at seguridad ng data na ginagamit nila. Halimbawa, ang LLMs ay maaaring potensyal na mag-memorize at mag-leak ng sensitibong impormasyon mula sa kanilang training data, tulad ng mga personal na pangalan, address, password, o numero ng credit card. Maaari rin silang manipulahin o atakehin ng mga mapanlinlang na aktor na gustong samantalahin ang kanilang mga kahinaan o bias. Samakatuwid, mahalagang maging aware sa mga panganib na ito at gumawa ng angkop na hakbang upang protektahan ang data na ginagamit sa LLMs. Mayroong ilang mga hakbang na maaari mong gawin upang protektahan ang data na ginagamit sa LLMs. Kasama sa mga hakbang na ito ang:

- **Paglimita sa dami at uri ng data na ibinabahagi nila sa LLMs**: Ibahagi lamang ang data na kinakailangan at nauugnay para sa nilalayong layunin, at iwasang magbahagi ng anumang data na sensitibo, kumpidensyal, o personal. Dapat ding i-anonymize o i-encrypt ng mga gumagamit ang data na ibinabahagi nila sa LLMs, tulad ng sa pamamagitan ng pag-alis o pag-maskara ng anumang pagkakakilanlan na impormasyon, o paggamit ng mga secure na komunikasyon channels.
- **Pag-verify ng data na nabuo ng LLMs**: Laging suriin ang katumpakan at kalidad ng output na nabuo ng LLMs upang matiyak na hindi sila naglalaman ng anumang hindi gustong o hindi naaangkop na impormasyon.
- **Pag-uulat at pag-alerto ng anumang data breaches o insidente**: Maging mapagbantay sa anumang kahina-hinala o hindi normal na mga aktibidad o pag-uugali mula sa LLMs, tulad ng pagbuo ng mga teksto na hindi nauugnay, hindi tumpak, nakakasakit, o mapanganib. Ito ay maaaring maging indikasyon ng isang data breach o security incident.

Ang data security, governance, at compliance ay kritikal para sa anumang organisasyon na nais na i-leverage ang kapangyarihan ng data at AI sa isang multi-cloud environment. Ang pag-secure at pag-govern sa lahat ng iyong data ay isang kumplikado at multifaceted na gawain. Kailangan mong i-secure at i-govern ang iba't ibang uri ng data (structured, unstructured, at data na nabuo ng AI) sa iba't ibang lokasyon sa maraming clouds, at kailangan mong isaalang-alang ang umiiral at hinaharap na data security, governance, at AI regulations. Upang protektahan ang iyong data, kailangan mong magpatibay ng ilang mga best practices at pag-iingat, tulad ng:

- Gumamit ng mga cloud services o platforms na nag-aalok ng data protection at privacy features.
- Gumamit ng mga

**Pagwawaksi**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Habang nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang awtomatikong mga pagsasalin ay maaaring maglaman ng mga error o hindi pagkaka-ayon. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Kami ay hindi mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.