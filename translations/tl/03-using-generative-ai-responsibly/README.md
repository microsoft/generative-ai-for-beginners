<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:29:41+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "tl"
}
-->
# Paggamit ng Generative AI nang Responsable

> _I-click ang imahe sa itaas upang mapanood ang video ng araling ito_

Madaling mabighani sa AI at partikular na sa generative AI, ngunit kailangan mong isaalang-alang kung paano mo ito gagamitin nang responsable. Kailangan mong isaalang-alang ang mga bagay tulad ng kung paano masisiguro na patas at hindi nakasasama ang output at marami pang iba. Ang kabanatang ito ay naglalayong magbigay sa iyo ng nabanggit na konteksto, kung ano ang dapat isaalang-alang, at kung paano gumawa ng aktibong hakbang upang mapabuti ang paggamit mo ng AI.

## Panimula

Tatalakayin ng araling ito ang:

- Bakit dapat mong unahin ang Responsable AI kapag gumagawa ng mga Generative AI application.
- Mga pangunahing prinsipyo ng Responsable AI at kung paano ito nauugnay sa Generative AI.
- Paano ilalapat ang mga prinsipyo ng Responsable AI sa pamamagitan ng estratehiya at mga kagamitan.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo:

- Ang kahalagahan ng Responsable AI kapag gumagawa ng mga Generative AI application.
- Kailan dapat isipin at ilapat ang mga pangunahing prinsipyo ng Responsable AI kapag gumagawa ng mga Generative AI application.
- Anong mga kagamitan at estratehiya ang magagamit mo upang ilapat ang konsepto ng Responsable AI sa praktika.

## Mga Prinsipyo ng Responsable AI

Ang kasiyahan sa Generative AI ay hindi pa naging ganito kataas. Ang kasiyahang ito ay nagdala ng maraming bagong developer, atensyon, at pondo sa larangang ito. Habang ito ay napaka-positibo para sa sinumang nais bumuo ng mga produkto at kumpanya gamit ang Generative AI, mahalaga rin na magpatuloy tayo nang responsable.

Sa buong kursong ito, nakatuon tayo sa pagbuo ng aming startup at ng aming produktong pang-edukasyon sa AI. Gagamitin natin ang mga prinsipyo ng Responsable AI: Katarungan, Pagiging Inclusive, Pagiging Maaasahan/Kaligtasan, Seguridad at Pagkapribado, Transparency at Pananagutan. Sa mga prinsipyong ito, susuriin natin kung paano ito nauugnay sa paggamit natin ng Generative AI sa aming mga produkto.

## Bakit Dapat Mong Unahin ang Responsable AI

Kapag bumubuo ng isang produkto, ang paggamit ng human-centric na pamamaraan sa pamamagitan ng pag-iisip sa pinakamabuting interes ng iyong gumagamit ay nagdudulot ng pinakamahusay na resulta.

Ang pagiging natatangi ng Generative AI ay ang kakayahan nitong lumikha ng kapaki-pakinabang na mga sagot, impormasyon, gabay, at nilalaman para sa mga gumagamit. Maaari itong gawin nang walang maraming manu-manong hakbang na maaaring magdulot ng napaka-kahanga-hangang mga resulta. Kung walang tamang pagpaplano at mga estratehiya, maaari rin itong magdulot ng ilang nakakapinsalang resulta para sa iyong mga gumagamit, sa iyong produkto, at sa lipunan sa kabuuan.

Tingnan natin ang ilan (ngunit hindi lahat) ng mga potensyal na nakakapinsalang resulta:

### Hallucinations

Ang hallucinations ay isang termino na ginagamit upang ilarawan kapag ang isang LLM ay gumagawa ng nilalaman na alinman ay ganap na walang kabuluhan o isang bagay na alam nating mali ayon sa iba pang mga mapagkukunan ng impormasyon.

Halimbawa, gumawa tayo ng isang tampok para sa aming startup na nagpapahintulot sa mga mag-aaral na magtanong ng mga tanong tungkol sa kasaysayan sa isang modelo. Isang mag-aaral ang nagtanong ng tanong `Who was the sole survivor of Titanic?`

Ang modelo ay gumagawa ng sagot tulad ng nasa ibaba:

![Prompt na nagsasabing "Sino ang nag-iisang nakaligtas sa Titanic"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

Ito ay isang napaka-kumpiyansa at detalyadong sagot. Sa kasamaang palad, ito ay mali. Kahit na may kaunting pananaliksik, malalaman ng isa na higit sa isang tao ang nakaligtas sa sakuna ng Titanic. Para sa isang mag-aaral na nagsisimula pa lamang sa pagsasaliksik ng paksang ito, ang sagot na ito ay maaaring maging kapani-paniwala na hindi na kuwestyunin at ituring bilang katotohanan. Ang mga kahihinatnan nito ay maaaring humantong sa pagiging hindi maaasahan ng AI system at negatibong makaapekto sa reputasyon ng aming startup.

Sa bawat pag-ulit ng anumang ibinigay na LLM, nakita natin ang mga pagpapabuti sa pagganap sa paligid ng pag-minimize ng mga hallucinations. Kahit na may ganitong pagpapabuti, tayo bilang mga tagabuo ng aplikasyon at mga gumagamit ay kailangan pa ring manatiling mulat sa mga limitasyong ito.

### Nakakapinsalang Nilalaman

Tinalakay natin sa nakaraang seksyon kung kailan ang isang LLM ay gumagawa ng mali o walang kabuluhang mga tugon. Isa pang panganib na kailangan nating malaman ay kapag ang isang modelo ay tumugon ng nakakapinsalang nilalaman.

Ang nakakapinsalang nilalaman ay maaaring tukuyin bilang:

- Pagbibigay ng mga tagubilin o paghikayat sa pananakit sa sarili o pananakit sa ilang mga grupo.
- Mapoot o mapanirang nilalaman.
- Paggabay sa pagpaplano ng anumang uri ng pag-atake o marahas na gawain.
- Pagbibigay ng mga tagubilin kung paano makahanap ng ilegal na nilalaman o magsagawa ng ilegal na gawain.
- Pagpapakita ng sekswal na tahasang nilalaman.

Para sa aming startup, nais naming tiyakin na mayroon kaming tamang mga kagamitan at estratehiya upang maiwasan ang ganitong uri ng nilalaman na makita ng mga mag-aaral.

### Kawalan ng Katarungan

Ang katarungan ay tinukoy bilang “pagtiyak na ang isang AI system ay walang kinikilingan at diskriminasyon at na tinatrato nila ang lahat ng pantay-pantay at makatarungan.” Sa mundo ng Generative AI, nais nating tiyakin na ang mga pananaw na nagbubukod sa mga marginalized na grupo ay hindi pinagtitibay ng output ng modelo.

Ang mga ganitong uri ng output ay hindi lamang nakakasira sa pagbuo ng positibong karanasan ng produkto para sa aming mga gumagamit, ngunit nagdudulot din ito ng karagdagang pinsala sa lipunan. Bilang mga tagabuo ng aplikasyon, dapat palagi nating isaisip ang isang malawak at magkakaibang base ng gumagamit kapag gumagawa ng mga solusyon gamit ang Generative AI.

## Paano Gamitin ang Generative AI nang Responsable

Ngayon na natukoy na natin ang kahalagahan ng Responsable Generative AI, tingnan natin ang 4 na hakbang na maaari nating gawin upang bumuo ng ating mga AI solution nang responsable:

### Sukatin ang Potensyal na Pinsala

Sa pagsusuri ng software, sinusubukan natin ang mga inaasahang aksyon ng isang gumagamit sa isang aplikasyon. Katulad nito, ang pagsubok sa isang magkakaibang hanay ng mga prompt na malamang na gagamitin ng mga gumagamit ay isang magandang paraan upang sukatin ang potensyal na pinsala.

Dahil ang aming startup ay gumagawa ng isang produktong pang-edukasyon, magiging maganda na maghanda ng listahan ng mga prompt na may kaugnayan sa edukasyon. Maaari itong sumaklaw sa isang tiyak na paksa, mga katotohanan sa kasaysayan, at mga prompt tungkol sa buhay ng estudyante.

### Bawasan ang Potensyal na Pinsala

Panahon na upang makahanap ng mga paraan kung saan maaari nating maiwasan o limitahan ang potensyal na pinsala na dulot ng modelo at mga tugon nito. Maaari nating tingnan ito sa 4 na magkakaibang layer:

- **Modelo**. Pagpili ng tamang modelo para sa tamang paggamit. Ang mas malalaki at mas kumplikadong mga modelo tulad ng GPT-4 ay maaaring magdulot ng mas maraming panganib ng nakakapinsalang nilalaman kapag inilapat sa mas maliit at mas tiyak na mga paggamit. Ang paggamit ng iyong data sa pagsasanay upang ma-fine-tune ay binabawasan din ang panganib ng nakakapinsalang nilalaman.

- **Sistema ng Kaligtasan**. Ang isang sistema ng kaligtasan ay isang hanay ng mga kagamitan at mga configuration sa platform na nagsisilbi sa modelo na tumutulong na mabawasan ang pinsala. Halimbawa nito ay ang sistema ng pag-filter ng nilalaman sa Azure OpenAI service. Dapat ding makita ng mga sistema ang mga jailbreak attack at hindi gustong aktibidad tulad ng mga kahilingan mula sa mga bot.

- **Metaprompt**. Ang metaprompts at grounding ay mga paraan kung paano natin maaaring idirekta o limitahan ang modelo batay sa ilang mga pag-uugali at impormasyon. Maaari itong maging paggamit ng mga input ng sistema upang tukuyin ang ilang mga limitasyon ng modelo. Bilang karagdagan, pagbibigay ng mga output na mas nauugnay sa saklaw o domain ng sistema.

Maaari rin itong paggamit ng mga teknik tulad ng Retrieval Augmented Generation (RAG) upang ang modelo ay kumuha lamang ng impormasyon mula sa isang seleksyon ng mga pinagkakatiwalaang mapagkukunan. Mayroong isang aralin sa ibang bahagi ng kursong ito para sa [pagbuo ng mga search application](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Karanasan ng Gumagamit**. Ang huling layer ay kung saan ang gumagamit ay direktang nakikipag-ugnayan sa modelo sa pamamagitan ng interface ng aming aplikasyon sa ilang paraan. Sa ganitong paraan, maaari nating idisenyo ang UI/UX upang limitahan ang gumagamit sa mga uri ng input na maaari nilang ipadala sa modelo pati na rin ang teksto o mga imahe na ipinapakita sa gumagamit. Kapag nagde-deploy ng AI application, kailangan din nating maging transparent tungkol sa kung ano ang kaya at hindi kaya ng ating Generative AI application.

Mayroon kaming buong aralin na nakatuon sa [Pagdidisenyo ng UX para sa AI Applications](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Pagsusuri ng modelo**. Ang pagtatrabaho sa mga LLM ay maaaring maging hamon dahil hindi palagi nating kontrolado ang data kung saan sinanay ang modelo. Sa kabila nito, palagi nating dapat suriin ang pagganap at mga output ng modelo. Mahalaga pa ring sukatin ang katumpakan ng modelo, pagkakatulad, grounding, at kaugnayan ng output. Nakakatulong ito upang magbigay ng transparency at tiwala sa mga stakeholder at mga gumagamit.

### Patakbuhin ang isang Responsable Generative AI na solusyon

Ang pagbuo ng isang operational practice sa paligid ng iyong mga AI application ay ang huling yugto. Kasama dito ang pakikipagtulungan sa iba pang bahagi ng aming startup tulad ng Legal at Seguridad upang matiyak na sumusunod tayo sa lahat ng mga patakaran sa regulasyon. Bago ilunsad, nais din naming bumuo ng mga plano sa paligid ng paghahatid, paghawak ng mga insidente, at rollback upang maiwasan ang anumang pinsala sa aming mga gumagamit mula sa paglago.

## Mga Kagamitan

Habang ang gawain ng pagbuo ng mga Responsable AI na solusyon ay maaaring mukhang marami, ito ay gawain na sulit ang pagsisikap. Habang lumalaki ang larangan ng Generative AI, mas maraming kagamitan upang matulungan ang mga developer na mahusay na maisama ang responsibilidad sa kanilang mga workflow ang magiging mas mature. Halimbawa, ang [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) ay makakatulong na matukoy ang nakakapinsalang nilalaman at mga imahe sa pamamagitan ng isang API request.

## Pagsusuri ng Kaalaman

Ano ang ilang mga bagay na kailangan mong pagtuunan ng pansin upang matiyak ang responsable paggamit ng AI?

1. Na tama ang sagot.
2. Nakakapinsalang paggamit, na hindi ginagamit ang AI para sa mga layuning kriminal.
3. Pagtiyak na ang AI ay walang kinikilingan at diskriminasyon.

A: 2 at 3 ay tama. Ang Responsable AI ay tumutulong sa iyo na isaalang-alang kung paano mabawasan ang mga nakakapinsalang epekto at mga bias at marami pa.

## 🚀 Hamon

Magbasa tungkol sa [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) at tingnan kung ano ang maaari mong i-adopt para sa iyong paggamit.

## Magaling na Trabaho, Ipagpatuloy ang Iyong Pagkatuto

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang patuloy na paunlarin ang iyong kaalaman sa Generative AI!

Pumunta sa Aralin 4 kung saan titingnan natin ang [Pangunahing Konsepto ng Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Pagtatatuwa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga error o kamalian. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.