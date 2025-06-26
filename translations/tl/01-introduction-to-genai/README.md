<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T10:01:49+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "tl"
}
-->
# Panimula sa Generative AI at Malalaking Modelo ng Wika

_(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

Ang Generative AI ay isang uri ng artipisyal na intelihensiya na kayang bumuo ng teksto, mga imahe, at iba pang uri ng nilalaman. Ang kahanga-hanga sa teknolohiyang ito ay ang kakayahan nitong gawing mas accessible ang AI sa lahat; kahit sino ay maaaring gumamit nito gamit lamang ang isang text prompt o isang pangungusap na isinulat sa natural na wika. Hindi mo na kailangan pang matutunan ang mga wikang gaya ng Java o SQL para makagawa ng makabuluhang bagay, kailangan mo lamang gamitin ang iyong wika, sabihin kung ano ang gusto mo at bibigyan ka ng mungkahi ng isang AI model. Ang mga aplikasyon at epekto nito ay napakalawak, mula sa pagsulat o pag-unawa ng mga ulat, pagsulat ng mga aplikasyon, at marami pang iba, lahat sa loob ng ilang segundo.

Sa kurikulum na ito, tatalakayin natin kung paano ginagamit ng aming startup ang generative AI upang buksan ang mga bagong senaryo sa mundo ng edukasyon at kung paano namin hinaharap ang mga hindi maiiwasang hamon na kaakibat ng mga implikasyong panlipunan ng aplikasyon nito at mga limitasyon ng teknolohiya.

## Panimula

Tatalakayin sa araling ito:

- Panimula sa senaryong pang-negosyo: ang ideya at misyon ng aming startup.
- Generative AI at kung paano namin narating ang kasalukuyang tanawin ng teknolohiya.
- Ang panloob na pag-andar ng isang malaking modelo ng wika.
- Pangunahing kakayahan at praktikal na mga kaso ng paggamit ng Malalaking Modelo ng Wika.

## Mga Layunin sa Pag-aaral

Pagkatapos makumpleto ang araling ito, maiintindihan mo:

- Ano ang generative AI at paano gumagana ang Malalaking Modelo ng Wika.
- Paano mo magagamit ang malalaking modelo ng wika para sa iba't ibang mga kaso ng paggamit, na may pokus sa mga senaryo ng edukasyon.

## Senaryo: ang aming startup sa edukasyon

Ang Generative Artificial Intelligence (AI) ay kumakatawan sa rurok ng teknolohiyang AI, na nagtatakda ng mga hangganan ng mga dating imposible. Maraming kakayahan at aplikasyon ang mga generative AI models, ngunit para sa kurikulum na ito, susuriin natin kung paano nito binabago ang edukasyon sa pamamagitan ng isang kathang-isip na startup. Tatawagin natin ang startup na ito bilang _ang aming startup_. Ang aming startup ay gumagana sa larangan ng edukasyon na may ambisyosong pahayag ng misyon na

> _pagpapabuti ng accessibility sa pag-aaral, sa pandaigdigang saklaw, tinitiyak ang patas na access sa edukasyon at pagbibigay ng mga personalized na karanasan sa pag-aaral sa bawat mag-aaral, ayon sa kanilang mga pangangailangan_.

Alam ng aming koponan na hindi namin makakamit ang layuning ito nang hindi ginagamit ang isa sa pinakamakapangyarihang kasangkapan ng modernong panahon – Malalaking Modelo ng Wika (LLMs).

Inaasahan na ang Generative AI ay babaguhin ang paraan ng ating pag-aaral at pagtuturo ngayon, kung saan ang mga estudyante ay mayroong virtual na mga guro na magagamit 24 oras sa isang araw na nagbibigay ng napakaraming impormasyon at halimbawa, at ang mga guro ay maaaring gumamit ng mga makabagong kasangkapan upang suriin ang kanilang mga estudyante at magbigay ng feedback.

Upang magsimula, tukuyin natin ang ilang mga pangunahing konsepto at terminolohiya na gagamitin natin sa buong kurikulum.

## Paano natin nakuha ang Generative AI?

Sa kabila ng kamangha-manghang _hype_ na nilikha kamakailan ng anunsyo ng mga generative AI models, ang teknolohiyang ito ay dekada nang ginagawa, na ang mga unang pagsisikap sa pananaliksik ay nagsimula noong 60s. Ngayon ay nasa punto na tayo kung saan ang AI ay may kakayahang kognitibo ng tao, tulad ng pakikipag-usap gaya ng ipinapakita ng halimbawa [OpenAI ChatGPT](https://openai.com/chatgpt) o [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), na gumagamit din ng GPT model para sa web search Bing conversations.

Balikan natin ng kaunti, ang mga pinakaunang prototype ng AI ay binubuo ng mga typewritten chatbots, na umaasa sa isang knowledge base na kinuha mula sa isang grupo ng mga eksperto at kinatawan sa isang computer. Ang mga sagot sa knowledge base ay na-trigger ng mga keyword na lumalabas sa input text. Gayunpaman, agad na naging malinaw na ang ganitong pamamaraan, gamit ang typewritten chatbots, ay hindi maganda ang pag-scale.

### Isang istatistikal na pamamaraan sa AI: Machine Learning

Isang mahalagang punto ang dumating noong 90s, sa pamamagitan ng aplikasyon ng isang istatistikal na pamamaraan sa pagsusuri ng teksto. Ito ay humantong sa pag-unlad ng mga bagong algorithm – na kilala bilang machine learning – na may kakayahang matuto ng mga pattern mula sa data nang hindi direktang naiprograma. Ang pamamaraang ito ay nagbibigay-daan sa mga makina na gayahin ang pag-unawa ng wika ng tao: ang isang istatistikal na modelo ay sinasanay sa mga text-label pairings, na nagpapahintulot sa modelo na ikategorya ang hindi kilalang input text gamit ang isang paunang natukoy na label na kumakatawan sa intensyon ng mensahe.

### Neural networks at mga modernong virtual na katulong

Sa mga nakaraang taon, ang teknolohikal na ebolusyon ng hardware, na may kakayahang humawak ng mas malalaking dami ng data at mas kumplikadong mga komputasyon, ay nag-udyok sa pananaliksik sa AI, na nagresulta sa pag-unlad ng mga advanced na machine learning algorithm na kilala bilang neural networks o deep learning algorithms.

Malaki ang naitulong ng neural networks (at partikular na Recurrent Neural Networks – RNNs) sa natural language processing, na nagbibigay-daan sa mas makabuluhang representasyon ng kahulugan ng teksto, na pinahahalagahan ang konteksto ng isang salita sa isang pangungusap.

Ito ang teknolohiya na nagpatakbo sa mga virtual na katulong na ipinanganak sa unang dekada ng bagong siglo, na napakahusay sa pagpapakahulugan ng wika ng tao, pagkilala sa isang pangangailangan, at paggawa ng isang aksyon upang matugunan ito – tulad ng pagsagot gamit ang isang paunang natukoy na script o paggamit ng isang 3rd party na serbisyo.

### Kasalukuyang araw, Generative AI

Kaya't ganito tayo nakarating sa Generative AI ngayon, na maaaring makita bilang isang subset ng deep learning.

Pagkatapos ng mga dekada ng pananaliksik sa larangan ng AI, isang bagong arkitektura ng modelo – tinatawag na _Transformer_ – ang nakatalo sa mga limitasyon ng RNNs, na may kakayahang kumuha ng mas mahabang mga pagkakasunud-sunod ng teksto bilang input. Ang mga Transformers ay batay sa mekanismo ng atensyon, na nagbibigay-daan sa modelo na magbigay ng iba't ibang timbang sa mga input na natatanggap nito, 'mas nagbibigay pansin' kung saan ang pinaka-kaugnay na impormasyon ay nakatuon, kahit na ano ang kanilang pagkakasunod-sunod sa teksto.

Karamihan sa mga kamakailang generative AI models – na kilala rin bilang Malalaking Modelo ng Wika (LLMs), dahil sila ay nagtatrabaho sa mga input at output ng teksto – ay talagang batay sa arkitekturang ito. Ang interesante sa mga modelong ito – na sinanay sa napakalaking dami ng hindi naka-label na data mula sa iba't ibang pinagmumulan tulad ng mga libro, artikulo at mga website – ay maaari silang iakma sa iba't ibang uri ng mga gawain at bumuo ng tekstong grammatically correct na may anyo ng pagkamalikhain. Kaya, hindi lamang nila napabuti nang husto ang kakayahan ng isang makina na 'maunawaan' ang isang input na teksto, ngunit pinagana nila ang kanilang kakayahang bumuo ng isang orihinal na tugon sa wika ng tao.

## Paano gumagana ang malalaking modelo ng wika?

Sa susunod na kabanata, susuriin natin ang iba't ibang uri ng mga Generative AI models, ngunit sa ngayon tingnan natin kung paano gumagana ang malalaking modelo ng wika, na may pokus sa mga modelo ng OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizer, teksto sa mga numero**: Ang Malalaking Modelo ng Wika ay tumatanggap ng isang teksto bilang input at bumubuo ng isang teksto bilang output. Gayunpaman, bilang mga istatistikal na modelo, mas mahusay silang gumagana sa mga numero kaysa sa mga pagkakasunud-sunod ng teksto. Iyon ang dahilan kung bakit ang bawat input sa modelo ay pinoproseso ng isang tokenizer, bago gamitin ng pangunahing modelo. Ang isang token ay isang bahagi ng teksto – na binubuo ng isang variable na bilang ng mga karakter, kaya ang pangunahing gawain ng tokenizer ay hatiin ang input sa isang array ng mga token. Pagkatapos, ang bawat token ay nakamapa sa isang token index, na siyang integer encoding ng orihinal na bahagi ng teksto.

- **Paghula ng mga output token**: Binigyan ng n token bilang input (na may max n na nag-iiba mula sa isang modelo patungo sa isa pa), ang modelo ay may kakayahang hulaan ang isang token bilang output. Ang token na ito ay pagkatapos ay isinama sa input ng susunod na iteration, sa isang pattern ng pagpapalawak ng window, na nagbibigay-daan sa mas magandang karanasan ng user na makakuha ng isa (o maramihang) pangungusap bilang sagot. Ito ang nagpapaliwanag kung bakit, kung nakipaglaro ka sa ChatGPT, maaaring napansin mo na kung minsan ay parang humihinto ito sa kalagitnaan ng isang pangungusap.

- **Proseso ng pagpili, pamamahagi ng posibilidad**: Ang output token ay pinipili ng modelo ayon sa posibilidad nitong mangyari pagkatapos ng kasalukuyang pagkakasunud-sunod ng teksto. Ito ay dahil ang modelo ay naghuhula ng isang pamamahagi ng posibilidad sa lahat ng posibleng 'susunod na mga token', na kinakalkula batay sa pagsasanay nito. Gayunpaman, hindi palaging ang token na may pinakamataas na posibilidad ang pinipili mula sa resulta ng pamamahagi. Ang isang antas ng randomness ay idinaragdag sa pagpili na ito, sa isang paraan na ang modelo ay kumikilos sa isang hindi-deterministikong paraan - hindi natin nakukuha ang eksaktong parehong output para sa parehong input. Ang antas ng randomness na ito ay idinaragdag upang gayahin ang proseso ng malikhaing pag-iisip at maaari itong i-tune gamit ang isang parameter ng modelo na tinatawag na temperatura.

## Paano magagamit ng aming startup ang Malalaking Modelo ng Wika?

Ngayon na mas naiintindihan na natin ang panloob na pag-andar ng isang malaking modelo ng wika, tingnan natin ang ilang praktikal na halimbawa ng mga pinakakaraniwang gawain na maaari nilang isagawa nang maayos, na may pagtingin sa aming senaryong pang-negosyo. Sinabi natin na ang pangunahing kakayahan ng isang Malaking Modelo ng Wika ay _pagbuo ng teksto mula sa simula, simula sa isang tekstuwal na input, na nakasulat sa natural na wika_.

Ngunit anong uri ng tekstuwal na input at output?
Ang input ng isang malaking modelo ng wika ay kilala bilang isang prompt, habang ang output ay kilala bilang isang completion, na tumutukoy sa mekanismo ng modelo ng pagbuo ng susunod na token upang makumpleto ang kasalukuyang input. Susuriin natin nang malalim kung ano ang isang prompt at kung paano ito idisenyo sa paraang makakakuha ng pinakamaraming pakinabang mula sa ating modelo. Ngunit sa ngayon, sabihin na lang natin na ang isang prompt ay maaaring magsama ng:

- Isang **instruksyon** na nagsasaad ng uri ng output na inaasahan natin mula sa modelo. Ang instruksyong ito ay kung minsan ay maaaring maglaman ng ilang mga halimbawa o ilang karagdagang data.

  1. Pagbubuod ng isang artikulo, libro, pagsusuri ng produkto at higit pa, kasama ang pagkuha ng mga pananaw mula sa hindi nakaayos na data.
  
  2. Malikhaing ideya at disenyo ng isang artikulo, sanaysay, takdang-aralin o higit pa.

- Isang **tanong**, na tinanong sa anyo ng isang pag-uusap sa isang ahente.

- Isang bahagi ng **teksto na kumpletuhin**, na implicit na isang hiling para sa tulong sa pagsulat.

- Isang bahagi ng **code** kasama ang hiling na ipaliwanag at idokumento ito, o isang komento na humihiling na bumuo ng isang piraso ng code na gumaganap ng isang tiyak na gawain.

Ang mga halimbawa sa itaas ay medyo simple at hindi nilalayong maging isang komprehensibong demonstrasyon ng mga kakayahan ng Malalaking Modelo ng Wika. Ang mga ito ay nilalayong ipakita ang potensyal ng paggamit ng generative AI, partikular ngunit hindi limitado sa mga konteksto ng edukasyon.

Gayundin, ang output ng isang generative AI model ay hindi perpekto at kung minsan ang pagkamalikhain ng modelo ay maaaring magtrabaho laban dito, na nagreresulta sa isang output na isang kumbinasyon ng mga salita na ang tao ay maaaring bigyang-kahulugan bilang isang mistipikasyon ng katotohanan, o maaari itong maging mapang-abuso. Ang Generative AI ay hindi matalino - hindi bababa sa mas komprehensibong kahulugan ng intelihensiya, kabilang ang kritikal at malikhaing pangangatwiran o emosyonal na intelihensiya; hindi ito deterministiko, at hindi ito mapagkakatiwalaan, dahil ang mga gawa-gawa, tulad ng maling mga sanggunian, nilalaman, at pahayag, ay maaaring pagsamahin sa tamang impormasyon, at ipakita sa isang mapanghikayat at kumpiyansang paraan. Sa mga susunod na aralin, haharapin natin ang lahat ng mga limitasyong ito at makikita natin kung ano ang maaari nating gawin upang mabawasan ang mga ito.

## Takdang-Aralin

Ang iyong takdang-aralin ay magbasa pa tungkol sa [generative AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) at subukang tukuyin ang isang lugar kung saan mo idagdag ang generative AI ngayon na wala pa ito. Paano magiging iba ang epekto mula sa paggawa nito sa "lumang paraan", makakagawa ka ba ng isang bagay na hindi mo magagawa dati, o mas mabilis ka ba? Sumulat ng isang 300 na salita na buod kung ano ang magiging hitsura ng iyong pangarap na AI startup at isama ang mga header gaya ng "Problema", "Paano ko gagamitin ang AI", "Epekto" at opsyonal na isang plano sa negosyo.

Kung nagawa mo ang gawaing ito, maaari ka nang maging handa na mag-aplay sa incubator ng Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) nag-aalok kami ng mga kredito para sa parehong Azure, OpenAI, mentoring at marami pa, tingnan ito!

## Pagsusuri ng Kaalaman

Ano ang totoo tungkol sa malalaking modelo ng wika?

1. Nakukuha mo ang eksaktong parehong tugon sa bawat oras.
2. Perpekto itong gumagawa ng mga bagay, mahusay sa pagdaragdag ng mga numero, paggawa ng gumaganang code atbp.
3. Ang tugon ay maaaring mag-iba sa kabila ng paggamit ng parehong prompt. Mahusay din ito sa pagbibigay sa iyo ng isang unang draft ng isang bagay, maging ito ay teksto o code. Ngunit kailangan mong pagbutihin ang mga resulta.

A: 3, ang isang LLM ay hindi deterministiko, ang tugon ay nag-iiba, gayunpaman, maaari mong kontrolin ang pagkakaiba nito sa pamamagitan ng isang setting ng temperatura. Hindi mo rin dapat asahan na gawin ito nang perpekto, narito ito upang gawin ang mabigat na gawain para sa iyo na madalas ay nangangahulugang nakakakuha ka ng isang magandang unang pagtatangka sa isang bagay na kailangan mong unti-unting pagbutihin.

## Mahusay na Trabaho! Ipagpatuloy ang Paglalakbay

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Koleksyon ng Pag-aaral sa Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapataas ng iyong kaalaman sa Generative AI!

Pumunta sa Aralin 2 kung saan titingnan natin kung paano [galugarin at ihambing ang iba't ibang uri ng LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ay dapat ituring na mapagkakatiwalaang sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Kami ay hindi mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.