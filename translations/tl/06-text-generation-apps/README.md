<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T14:41:07+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "tl"
}
-->
# Paggawa ng Mga Aplikasyon para sa Pagbuo ng Teksto

> _(I-click ang larawan sa itaas upang panoorin ang video ng leksyon na ito)_

Sa ngayon, nakita mo sa kurikulum na ito na may mga pangunahing konsepto tulad ng mga prompt at kahit isang buong disiplina na tinatawag na "prompt engineering". Maraming mga tool na maaari mong makipag-ugnayan tulad ng ChatGPT, Office 365, Microsoft Power Platform at iba pa, na sumusuporta sa paggamit mo ng mga prompt upang makamit ang isang bagay.

Para maidagdag mo ang ganitong karanasan sa isang app, kailangan mong maunawaan ang mga konsepto tulad ng mga prompt, mga completion, at pumili ng library na gagamitin. Iyan mismo ang matututunan mo sa kabanatang ito.

## Panimula

Sa kabanatang ito, ikaw ay:

- Matututo tungkol sa openai library at mga pangunahing konsepto nito.
- Bubuo ng isang app para sa pagbuo ng teksto gamit ang openai.
- Mauunawaan kung paano gamitin ang mga konsepto tulad ng prompt, temperatura, at mga token upang bumuo ng isang app para sa pagbuo ng teksto.

## Mga Layunin sa Pag-aaral

Sa pagtatapos ng leksyon na ito, magagawa mong:

- Ipaliwanag kung ano ang isang app para sa pagbuo ng teksto.
- Bumuo ng isang app para sa pagbuo ng teksto gamit ang openai.
- I-configure ang iyong app upang gumamit ng mas marami o mas kaunting mga token at baguhin din ang temperatura, para sa iba't ibang output.

## Ano ang isang app para sa pagbuo ng teksto?

Karaniwang kapag nagbuo ka ng isang app, mayroon itong uri ng interface tulad ng mga sumusunod:

- Batay sa utos. Ang mga console app ay mga tipikal na app kung saan nagta-type ka ng utos at isinasagawa nito ang isang gawain. Halimbawa, ang `git` ay isang app na batay sa utos.
- User interface (UI). Ang ilang mga app ay may mga graphical user interfaces (GUIs) kung saan nagki-click ka ng mga button, naglalagay ng teksto, pumipili ng mga opsyon at iba pa.

### Limitado ang mga Console at UI apps

Ihambing ito sa isang app na batay sa utos kung saan nagta-type ka ng utos:

- **Ito ay limitado**. Hindi mo basta-basta mai-type ang anumang utos, tanging ang mga suportado ng app.
- **Specific sa wika**. Ang ilang mga app ay sumusuporta sa maraming wika, ngunit sa default ang app ay binuo para sa isang partikular na wika, kahit na maaari kang magdagdag ng suporta sa higit pang mga wika.

### Mga Benepisyo ng mga app para sa pagbuo ng teksto

Kaya paano naiiba ang isang app para sa pagbuo ng teksto?

Sa isang app para sa pagbuo ng teksto, mayroon kang mas maraming kakayahang umangkop, hindi ka limitado sa isang hanay ng mga utos o isang partikular na input na wika. Sa halip, maaari mong gamitin ang natural na wika upang makipag-ugnayan sa app. Ang isa pang benepisyo ay dahil nakikipag-ugnayan ka na sa isang pinagmulan ng data na sinanay sa isang malawak na corpus ng impormasyon, samantalang ang isang tradisyunal na app ay maaaring limitado sa kung ano ang nasa database.

### Ano ang maaari kong buuin gamit ang isang app para sa pagbuo ng teksto?

Maraming bagay ang maaari mong buuin. Halimbawa:

- **Isang chatbot**. Isang chatbot na sumasagot sa mga tanong tungkol sa mga paksa, tulad ng iyong kumpanya at mga produkto nito ay maaaring maging magandang tugma.
- **Helper**. Mahusay ang LLMs sa mga bagay tulad ng pagsasama ng teksto, pagkuha ng mga insight mula sa teksto, paggawa ng teksto tulad ng mga resume at iba pa.
- **Code assistant**. Depende sa modelo ng wika na iyong ginagamit, maaari kang bumuo ng isang code assistant na tumutulong sa iyo na magsulat ng code. Halimbawa, maaari kang gumamit ng isang produkto tulad ng GitHub Copilot pati na rin ang ChatGPT upang matulungan kang magsulat ng code.

## Paano ko masisimulan?

Kailangan mong humanap ng paraan upang isama ang isang LLM na karaniwang kinabibilangan ng sumusunod na dalawang diskarte:

- Gumamit ng API. Dito ka bumubuo ng mga web request kasama ang iyong prompt at makakakuha ng bumubuo na teksto pabalik.
- Gumamit ng library. Ang mga library ay tumutulong sa encapsulate ng mga tawag sa API at gawing mas madali ang paggamit.

## Mga Library/SDKs

May ilang kilalang library para sa pagtatrabaho sa LLMs tulad ng:

- **openai**, ang library na ito ay ginagawang madali upang kumonekta sa iyong modelo at magpadala ng mga prompt.

Pagkatapos ay may mga library na gumagana sa mas mataas na antas tulad ng:

- **Langchain**. Kilala ang Langchain at sumusuporta sa Python.
- **Semantic Kernel**. Ang Semantic Kernel ay isang library ng Microsoft na sumusuporta sa mga wika C#, Python, at Java.

## Unang app gamit ang openai

Tingnan natin kung paano natin mabubuo ang ating unang app, kung anong mga library ang kailangan natin, kung gaano karami ang kinakailangan at iba pa.

### I-install ang openai

Maraming mga library doon para sa pakikipag-ugnayan sa OpenAI o Azure OpenAI. Posible ring gumamit ng maraming mga programming language tulad ng C#, Python, JavaScript, Java at iba pa. Pinili naming gamitin ang `openai` Python library, kaya gagamitin namin ang `pip` upang i-install ito.

### Lumikha ng resource

Kailangan mong isagawa ang mga sumusunod na hakbang:

- Lumikha ng account sa Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Makakuha ng access sa Azure OpenAI. Pumunta sa [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) at humiling ng access.

- I-install ang Python <https://www.python.org/>
- Nakalikha ng Azure OpenAI Service resource. Tingnan ang gabay na ito para sa kung paano [lumikha ng resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Hanapin ang API key at endpoint

Sa puntong ito, kailangan mong sabihin sa iyong `openai` library kung anong API key ang gagamitin. Upang hanapin ang iyong API key, pumunta sa "Keys and Endpoint" section ng iyong Azure OpenAI resource at kopyahin ang "Key 1" value.

Ngayon na mayroon kang impormasyong ito, ipapagamit natin ito sa mga library.

### Setup configuration Azure

Kung gumagamit ka ng Azure OpenAI, narito kung paano mo i-setup ang configuration:

Sa itaas, isinaset natin ang mga sumusunod:

Sa itaas na code, gumagawa tayo ng completion object at ipinapasa ang model na gusto nating gamitin at ang prompt. Pagkatapos ay ipinapakita natin ang bumubuo na teksto.

### Mga Chat completions

Sa ngayon, nakita mo kung paano natin ginagamit ang `Completion` to generate text. But there's another class called `ChatCompletion` na mas angkop para sa mga chatbot. Narito ang isang halimbawa ng paggamit nito:

Higit pa sa functionality na ito sa darating na kabanata.

## Ehersisyo - ang iyong unang app para sa pagbuo ng teksto

Ngayon na natutunan natin kung paano i-setup at i-configure ang openai, oras na para bumuo ng iyong unang app para sa pagbuo ng teksto. Para buuin ang iyong app, sundin ang mga hakbang na ito:

1. Lumikha ng virtual environment at i-install ang openai:

1. Lumikha ng _app.py_ file at bigyan ito ng sumusunod na code:

Makikita mo ang output na katulad ng sumusunod:

## Iba't ibang uri ng mga prompt, para sa iba't ibang bagay

Ngayon nakita mo kung paano bumuo ng teksto gamit ang isang prompt. Mayroon ka pang programang tumatakbo na maaari mong baguhin at palitan upang bumuo ng iba't ibang uri ng teksto.

Ang mga prompt ay maaaring gamitin para sa lahat ng uri ng mga gawain. Halimbawa:

- **Bumuo ng uri ng teksto**. Halimbawa, maaari kang bumuo ng isang tula, mga tanong para sa isang quiz atbp.
- **Hanapin ang impormasyon**. Maaari mong gamitin ang mga prompt upang maghanap ng impormasyon tulad ng sumusunod na halimbawa 'Ano ang ibig sabihin ng CORS sa web development?'.
- **Bumuo ng code**. Maaari mong gamitin ang mga prompt upang bumuo ng code, halimbawa pagbuo ng regular expression na ginagamit upang i-validate ang mga email o bakit hindi bumuo ng isang buong programa, tulad ng isang web app?

## Isang mas praktikal na kaso: isang generator ng recipe

Isipin na mayroon kang mga sangkap sa bahay at gusto mong magluto ng isang bagay. Para doon, kailangan mo ng recipe. Ang isang paraan upang makahanap ng mga recipe ay ang paggamit ng search engine o maaari mong gamitin ang isang LLM para gawin ito.

Maaari kang sumulat ng isang prompt na ganito:

> "Ipakita sa akin ang 5 mga recipe para sa isang ulam na may mga sumusunod na sangkap: manok, patatas, at karot. Sa bawat recipe, ilista ang lahat ng mga sangkap na ginamit"

Dahil sa itaas na prompt, maaari kang makakuha ng tugon na katulad ng:

Ang kinalabasan na ito ay mahusay, alam ko na kung ano ang lulutuin. Sa puntong ito, ang mga kapaki-pakinabang na pagpapabuti ay maaaring:

- Pagtanggal ng mga sangkap na hindi ko gusto o allergic ako.
- Gumawa ng listahan ng pamimili, kung sakaling wala akong lahat ng sangkap sa bahay.

Para sa mga nabanggit na kaso, magdagdag tayo ng karagdagang prompt:

> "Mangyaring alisin ang mga recipe na may bawang dahil allergic ako at palitan ito ng iba. Gayundin, mangyaring gumawa ng listahan ng pamimili para sa mga recipe, isinasaalang-alang na mayroon na akong manok, patatas at karot sa bahay."

Ngayon mayroon kang bagong resulta, na:

Iyan ang iyong limang recipe, na walang binanggit na bawang at mayroon ka ring listahan ng pamimili na isinasaalang-alang ang mayroon ka na sa bahay.

## Ehersisyo - bumuo ng isang generator ng recipe

Ngayon na mayroon tayong senaryo, isulat natin ang code upang tumugma sa ipinakitang senaryo. Para gawin ito, sundin ang mga hakbang na ito:

1. Gamitin ang umiiral na _app.py_ file bilang panimulang punto
1. Hanapin ang `prompt` variable at palitan ang code nito sa sumusunod:

Kung ngayon ay patakbuhin mo ang code, makikita mo ang output na katulad ng:

Mahusay, tingnan natin kung paano natin mapapabuti ang mga bagay. Upang mapabuti ang mga bagay, gusto nating tiyakin na ang code ay nababaluktot, kaya ang mga sangkap at bilang ng mga recipe ay maaaring mapabuti at mabago.

1. Palitan natin ang code sa sumusunod na paraan:

Ang pagkuha ng code para sa isang test run, ay maaaring ganito:

### Pagbutihin sa pamamagitan ng pagdaragdag ng filter at listahan ng pamimili

Ngayon ay mayroon na tayong gumaganang app na may kakayahang gumawa ng mga recipe at ito ay nababaluktot habang ito ay umaasa sa mga input mula sa user, pareho sa bilang ng mga recipe ngunit pati na rin ang mga sangkap na ginamit.

Upang higit pang mapabuti ito, nais naming idagdag ang mga sumusunod:

- **Tanggalin ang mga sangkap**. Nais naming magawa na tanggalin ang mga sangkap na hindi namin gusto o allergic kami. Upang makamit ang pagbabagong ito, maaari naming i-edit ang aming umiiral na prompt at magdagdag ng kondisyon sa filter sa dulo nito tulad ng:

  Sa itaas, idinagdag namin ang `{filter}` sa dulo ng prompt at kinukuha rin namin ang halaga ng filter mula sa user.

  Ang halimbawa ng input ng pagpapatakbo ng programa ay maaaring ganito:

  Tulad ng nakikita mo, ang anumang mga recipe na may gatas ay na-filter out. Ngunit, kung ikaw ay lactose intolerant, maaaring gusto mong tanggalin ang mga recipe na may keso, kaya may pangangailangan na maging malinaw.

- **Gumawa ng listahan ng pamimili**. Nais naming gumawa ng listahan ng pamimili, isinasaalang-alang ang mayroon na kami sa bahay.

  Para sa functionality na ito, maaari nating subukang lutasin ang lahat sa isang prompt o maaari nating hatiin ito sa dalawang prompt. Subukan natin ang huling diskarte. Dito ay nagmumungkahi kaming magdagdag ng karagdagang prompt, ngunit para magawa ito, kailangan nating idagdag ang resulta ng unang prompt bilang konteksto sa pangalawang prompt.

  Hanapin ang bahagi ng code na nagpapakita ng resulta mula sa unang prompt at idagdag ang sumusunod na code sa ibaba:

  Tandaan ang mga sumusunod:

  1. Nagko-construct kami ng bagong prompt sa pamamagitan ng pagdaragdag ng resulta mula sa unang prompt sa bagong prompt:

  1. Gumagawa kami ng bagong request, ngunit isinasaalang-alang din ang bilang ng mga token na hiniling namin sa unang prompt, kaya sa pagkakataong ito ay sinasabi namin na `max_tokens` ay 1200.

     Ang pagkuha ng code para sa isang spin, ngayon ay dumating kami sa sumusunod na output:

## Pagbutihin ang iyong setup

Ang mayroon tayo sa ngayon ay code na gumagana, ngunit may ilang mga pagbabago na dapat nating gawin upang higit pang mapabuti ang mga bagay. Ang ilang mga bagay na dapat nating gawin ay:

- **Paghiwalayin ang mga sikreto mula sa code**, tulad ng API key. Ang mga sikreto ay hindi kabilang sa code at dapat na itago sa isang ligtas na lokasyon. Upang paghiwalayin ang mga sikreto mula sa code, maaari tayong gumamit ng mga environment variable at mga library tulad ng `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` file na may sumusunod na nilalaman:

     Tandaan, para sa Azure, kailangan mong itakda ang mga sumusunod na environment variable:

     Sa code, iloload mo ang mga environment variable tulad ng:

- **Isang salita sa haba ng token**. Dapat nating isaalang-alang kung gaano karaming mga token ang kailangan natin upang bumuo ng teksto na gusto natin. Ang mga token ay may halaga, kaya kung maaari, dapat tayong subukang maging matipid sa bilang ng mga token na ginagamit natin. Halimbawa, maaari ba nating ipahayag ang prompt upang makagamit tayo ng mas kaunting mga token?

  Upang baguhin ang mga token na ginagamit, maaari mong gamitin ang `max_tokens` parameter. Halimbawa, kung gusto mong gumamit ng 100 token, gagawin mo:

- **Pag-eeksperimento sa temperatura**. Ang temperatura ay isang bagay na hindi pa natin nabanggit sa ngayon ngunit ito ay isang mahalagang konteksto para sa kung paano gumaganap ang ating programa. Ang mas mataas na halaga ng temperatura, mas random ang output. Sa kabaligtaran, mas mababa ang halaga ng temperatura, mas predictable ang output. Isaalang-alang kung gusto mo ng variation sa iyong output o hindi.

  Upang baguhin ang temperatura, maaari mong gamitin ang `temperature` parameter. Halimbawa, kung gusto mong gumamit ng temperatura na 0.5, gagawin mo:

  Tandaan, mas malapit sa 1.0, mas iba-iba ang output.

## Takdang-aralin

Para sa takdang-aralin na ito, maaari kang pumili kung ano ang iyong bubuuin.

Narito ang ilang mga mungkahi:

- I-tweak ang app ng generator ng recipe upang higit pang mapabuti ito. Maglaro sa mga halaga ng temperatura, at mga prompt upang makita kung ano ang maaari mong buuin.
- Bumuo ng "study buddy". Ang app na ito ay dapat na makasagot sa mga tanong tungkol sa isang paksa halimbawa Python, maaari kang magkaroon ng mga prompt tulad ng "Ano ang isang tiyak na paksa sa Python?", o maaari kang magkaroon ng isang prompt na nagsasabi, ipakita sa akin ang code para sa isang tiyak na paksa atbp.
- History bot, gawing buhay ang kasaysayan, utusan ang bot na maglaro ng isang tiyak na karakter sa kasaysayan at tanungin ito ng mga tanong tungkol sa kanyang buhay at panahon.

## Solusyon

### Study buddy

Sa ibaba ay isang panimulang prompt, tingnan kung paano mo ito magagamit at i-tweak ito ayon sa gusto mo.

### History bot

Narito ang ilang mga prompt na maaari mong gamitin:

## Pagsusuri ng Kaalaman

Ano ang ginagawa ng konsepto ng temperatura?

1. Kinokontrol nito kung gaano ka-random ang output.
1. Kinokontrol nito kung gaano kalaki ang tugon.
1. Kinokontrol nito kung gaano karaming mga token ang ginagamit.

## 🚀 Hamon

Kapag nagtatrabaho sa takdang-aralin, subukan na iiba-iba ang temperatura, subukang itakda ito sa 0, 0.5, at 1. Tandaan na ang 0 ay ang hindi gaanong iba-iba at 1 ang pinaka, anong halaga ang pinakamahusay na gumagana para sa iyong app?

## Mahusay na Trabaho! Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos makumpleto ang leksyon na ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

Pumunta sa Lesson 7 kung saan titingnan natin kung paano [bumuo ng mga

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI na serbisyo sa pagsasalin [Co-op Translator](https://github.com/Azure/co-op-translator). Habang nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa kanyang katutubong wika ay dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-wika ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.