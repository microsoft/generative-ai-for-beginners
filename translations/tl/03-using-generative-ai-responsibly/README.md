<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:46:49+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "tl"
}
-->
# Ang Responsableng Paggamit ng Generative AI

> _I-click ang larawan sa itaas para mapanood ang video ng araling ito_

Madaling mahumaling sa AI at sa generative AI lalo na, pero kailangan mong isaalang-alang kung paano mo ito gagamitin nang responsable. Kailangan mong isaalang-alang ang mga bagay tulad ng kung paano masisiguro na ang output ay patas, hindi nakakasama, at iba pa. Ang kabanatang ito ay naglalayong bigyan ka ng nabanggit na konteksto, kung ano ang dapat isaalang-alang, at kung paano gumawa ng aktibong hakbang upang mapabuti ang paggamit mo ng AI.

## Panimula

Saklaw ng araling ito ang:

- Bakit dapat mong bigyang-priyoridad ang Responsable AI kapag gumagawa ng mga aplikasyon ng Generative AI.
- Mga pangunahing prinsipyo ng Responsable AI at kung paano ito nauugnay sa Generative AI.
- Paano isagawa ang mga prinsipyong ito ng Responsable AI sa pamamagitan ng estratehiya at mga kagamitan.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo:

- Ang kahalagahan ng Responsable AI kapag gumagawa ng mga aplikasyon ng Generative AI.
- Kailan dapat isaalang-alang at ilapat ang mga pangunahing prinsipyo ng Responsable AI kapag gumagawa ng mga aplikasyon ng Generative AI.
- Anong mga kagamitan at estratehiya ang magagamit mo upang maisagawa ang konsepto ng Responsable AI.

## Mga Prinsipyo ng Responsable AI

Ang kasabikan sa Generative AI ay hindi pa naging mas mataas. Ang kasabikang ito ay nagdala ng maraming bagong developer, atensyon, at pondo sa puwang na ito. Habang ito ay napaka-positibo para sa sinumang nagnanais na bumuo ng mga produkto at kumpanya gamit ang Generative AI, mahalaga rin na tayo ay magpatuloy nang responsable.

Sa buong kursong ito, kami ay nakatuon sa pagbuo ng aming startup at aming produktong pang-edukasyon na AI. Gagamitin namin ang mga prinsipyo ng Responsable AI: Pagkapantay-pantay, Pagsasama, Kahusayan/Kaligtasan, Seguridad at Pagkapribado, Transparency at Pananagutan. Sa mga prinsipyong ito, susuriin namin kung paano sila nauugnay sa aming paggamit ng Generative AI sa aming mga produkto.

## Bakit Dapat Mong Bigyang-priyoridad ang Responsable AI

Kapag gumagawa ng isang produkto, ang pagkuha ng human-centric na diskarte sa pamamagitan ng pag-iisip ng pinakamabuting interes ng iyong gumagamit ay humahantong sa pinakamahusay na resulta.

Ang natatanging katangian ng Generative AI ay ang kapangyarihan nitong lumikha ng mga kapaki-pakinabang na sagot, impormasyon, gabay, at nilalaman para sa mga gumagamit. Maaari itong gawin nang walang maraming manu-manong hakbang na maaaring humantong sa napaka-impressive na mga resulta. Nang walang tamang pagpaplano at estratehiya, maaari rin itong sa kasamaang-palad humantong sa ilang nakakapinsalang resulta para sa iyong mga gumagamit, iyong produkto, at lipunan sa kabuuan.

Tingnan natin ang ilan (ngunit hindi lahat) ng mga potensyal na nakakapinsalang resulta:

### Hallucinations

Ang mga hallucinations ay isang terminong ginagamit upang ilarawan kapag ang isang LLM ay gumagawa ng nilalaman na alinman ay ganap na walang katuturan o isang bagay na alam nating mali batay sa ibang mga mapagkukunan ng impormasyon.

Halimbawa, gumawa tayo ng isang tampok para sa aming startup na nagpapahintulot sa mga estudyante na magtanong ng mga tanong sa kasaysayan sa isang modelo. Ang isang estudyante ay nagtatanong ng tanong `Who was the sole survivor of Titanic?`

Ang modelo ay gumagawa ng sagot tulad ng isa sa ibaba:

![Prompt na nagsasabing "Sino ang nag-iisang nakaligtas sa Titanic"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

Ito ay isang napaka-kumpiyansa at masusing sagot. Sa kasamaang palad, ito ay mali. Kahit na may kaunting pananaliksik, malalaman ng isang tao na mayroong higit sa isang nakaligtas sa sakuna ng Titanic. Para sa isang estudyante na nagsisimula pa lang magsaliksik sa paksang ito, ang sagot na ito ay maaaring maging sapat na kapani-paniwala upang hindi kuwestyunin at ituring bilang katotohanan. Ang mga kahihinatnan nito ay maaaring humantong sa sistema ng AI na hindi mapagkakatiwalaan at negatibong makaapekto sa reputasyon ng aming startup.

Sa bawat pag-ulit ng anumang naibigay na LLM, nakita namin ang mga pagpapabuti sa pagganap sa paligid ng pagpapaliit ng mga hallucinations. Kahit na may ganitong pagpapabuti, kami bilang mga tagabuo ng aplikasyon at mga gumagamit ay kailangan pa ring maging maalam sa mga limitasyong ito.

### Nakakapinsalang Nilalaman

Tinalakay namin sa naunang seksyon kapag ang isang LLM ay gumagawa ng mga maling o walang katuturang tugon. Isa pang panganib na kailangan nating malaman ay kapag ang isang modelo ay tumutugon sa nakakapinsalang nilalaman.

Ang nakakapinsalang nilalaman ay maaaring tukuyin bilang:

- Pagbibigay ng mga tagubilin o paghikayat sa pananakit sa sarili o pananakit sa ilang grupo.
- Mapoot o mapanghamak na nilalaman.
- Paggabay sa pagpaplano ng anumang uri ng pag-atake o marahas na kilos.
- Pagbibigay ng mga tagubilin kung paano makahanap ng ilegal na nilalaman o gumawa ng ilegal na mga gawain.
- Pagpapakita ng sekswal na tahasang nilalaman.

Para sa aming startup, nais naming tiyakin na mayroon kaming tamang mga kagamitan at estratehiya upang maiwasan ang ganitong uri ng nilalaman na makita ng mga estudyante.

### Kawalan ng Pagkapantay-pantay

Ang pagkapantay-pantay ay tinutukoy bilang “pagtiyak na ang isang sistema ng AI ay walang bias at diskriminasyon at na tinatrato nila ang lahat nang patas at pantay.” Sa mundo ng Generative AI, nais nating tiyakin na ang mga eksklusibong pananaw sa mundo ng mga marginalized na grupo ay hindi pinalalakas ng output ng modelo.

Ang mga ganitong uri ng output ay hindi lamang nakakasira sa pagbuo ng positibong karanasan ng produkto para sa aming mga gumagamit, ngunit nagdudulot din ng karagdagang pinsala sa lipunan. Bilang mga tagabuo ng aplikasyon, palagi naming dapat isaalang-alang ang isang malawak at magkakaibang base ng gumagamit kapag gumagawa ng mga solusyon gamit ang Generative AI.

## Paano Gamitin ang Generative AI nang Responsable

Ngayon na natukoy na natin ang kahalagahan ng Responsable Generative AI, tingnan natin ang 4 na hakbang na maaari nating gawin upang bumuo ng aming mga solusyon sa AI nang responsable:

### Sukatin ang mga Potensyal na Pinsala

Sa pagsubok ng software, sinusubukan natin ang mga inaasahang aksyon ng isang gumagamit sa isang aplikasyon. Katulad nito, ang pagsubok sa isang magkakaibang hanay ng mga prompt na malamang na gagamitin ng mga gumagamit ay isang magandang paraan upang sukatin ang potensyal na pinsala.

Dahil ang aming startup ay bumubuo ng isang produktong pang-edukasyon, magiging mabuting ihanda ang isang listahan ng mga prompt na may kaugnayan sa edukasyon. Maaari itong upang masaklaw ang isang tiyak na paksa, mga katotohanan sa kasaysayan, at mga prompt tungkol sa buhay estudyante.

### Pagaanin ang mga Potensyal na Pinsala

Panahon na upang maghanap ng mga paraan kung saan maaari nating pigilan o limitahan ang potensyal na pinsala na dulot ng modelo at ng mga tugon nito. Maaari nating tingnan ito sa 4 na iba't ibang layer:

- **Modelo**. Pagpili ng tamang modelo para sa tamang kaso ng paggamit. Ang mas malaki at mas kumplikadong mga modelo tulad ng GPT-4 ay maaaring magdulot ng mas mataas na panganib ng nakakapinsalang nilalaman kapag inilapat sa mas maliit at mas tiyak na mga kaso ng paggamit. Ang paggamit ng iyong data sa pagsasanay upang i-fine-tune ay nakapagbabawas din ng panganib ng nakakapinsalang nilalaman.

- **Sistema ng Kaligtasan**. Ang isang sistema ng kaligtasan ay isang hanay ng mga kagamitan at mga pagsasaayos sa platform na nagsisilbing modelo na tumutulong sa pagpapagaan ng pinsala. Ang isang halimbawa nito ay ang sistema ng pag-filter ng nilalaman sa serbisyo ng Azure OpenAI. Dapat ding matukoy ng mga sistema ang mga jailbreak na pag-atake at hindi kanais-nais na aktibidad tulad ng mga kahilingan mula sa mga bot.

- **Metaprompt**. Ang mga metaprompt at grounding ay mga paraan kung paano natin maaring idirekta o limitahan ang modelo batay sa ilang mga pag-uugali at impormasyon. Maaari itong paggamit ng mga input ng sistema upang tukuyin ang ilang mga limitasyon ng modelo. Bukod pa rito, ang pagbibigay ng mga output na mas may kaugnayan sa saklaw o domain ng sistema.

Maaari rin itong paggamit ng mga tekniko tulad ng Retrieval Augmented Generation (RAG) upang ang modelo ay makakuha lamang ng impormasyon mula sa isang seleksyon ng mga pinagkakatiwalaang mapagkukunan. Mayroon pang isang aralin sa kurso na ito para sa [pagbuo ng mga search application](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Karanasan ng Gumagamit**. Ang huling layer ay kung saan ang gumagamit ay direktang nakikipag-ugnayan sa modelo sa pamamagitan ng interface ng aming aplikasyon sa ilang paraan. Sa ganitong paraan maaari nating idisenyo ang UI/UX upang limitahan ang gumagamit sa mga uri ng input na maaari nilang ipadala sa modelo pati na rin ang teksto o mga larawang ipinapakita sa gumagamit. Kapag idine-deploy ang aplikasyon ng AI, dapat din tayong maging transparent tungkol sa kung ano ang kaya at hindi kayang gawin ng aming Generative AI application.

Mayroon kaming buong aralin na nakatuon sa [Pagdidisenyo ng UX para sa mga AI Application](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Pagsusuri ng modelo**. Ang pakikipagtulungan sa mga LLM ay maaaring maging hamon dahil hindi natin palaging kontrolado ang data kung saan sinanay ang modelo. Sa kabila nito, palagi nating dapat suriin ang pagganap at mga output ng modelo. Mahalaga pa ring sukatin ang katumpakan ng modelo, pagkakatulad, groundedness, at kaugnayan ng output. Ito ay nakakatulong magbigay ng transparency at tiwala sa mga stakeholder at gumagamit.

### Magpatakbo ng isang Responsable Generative AI na solusyon

Ang pagbuo ng isang operational practice sa paligid ng iyong mga aplikasyon ng AI ay ang huling yugto. Kabilang dito ang pakikipagtulungan sa iba pang bahagi ng aming startup tulad ng Legal at Seguridad upang matiyak na sumusunod kami sa lahat ng mga patakaran sa regulasyon. Bago ilunsad, nais din naming bumuo ng mga plano sa paligid ng paghahatid, paghawak ng mga insidente, at pag-rollback upang maiwasan ang anumang pinsala sa aming mga gumagamit mula sa paglaki.

## Mga Kagamitan

Habang ang gawain ng pagbuo ng mga Responsable AI na solusyon ay maaaring mukhang marami, ito ay gawain na sulit ang pagsisikap. Habang lumalaki ang larangan ng Generative AI, mas maraming mga kagamitan upang matulungan ang mga developer na mahusay na isama ang responsibilidad sa kanilang mga workflow ang uunlad. Halimbawa, ang [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) ay makakatulong sa pagtukoy ng nakakapinsalang nilalaman at mga larawan sa pamamagitan ng isang API request.

## Pagsusuri ng Kaalaman

Ano ang ilan sa mga bagay na kailangan mong alagaan upang matiyak ang responsableng paggamit ng AI?

1. Na ang sagot ay tama.
2. Nakakapinsalang paggamit, na ang AI ay hindi ginagamit para sa mga layuning kriminal.
3. Pagtitiyak na ang AI ay walang bias at diskriminasyon.

A: Ang 2 at 3 ay tama. Ang Responsable AI ay tumutulong sa iyo na isaalang-alang kung paano mapagaan ang mga nakakapinsalang epekto at bias at iba pa.

## 🚀 Hamon

Magbasa tungkol sa [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) at tingnan kung ano ang maaari mong gamitin para sa iyong paggamit.

## Mahusay na Trabaho, Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang patuloy na paunlarin ang iyong kaalaman sa Generative AI!

Pumunta sa Lesson 4 kung saan titingnan natin ang [Mga Pangunahing Kaalaman sa Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Pagtatatuwa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Habang sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpakan. Ang orihinal na dokumento sa sariling wika nito ay dapat ituring na mapagkakatiwalaang sanggunian. Para sa kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.