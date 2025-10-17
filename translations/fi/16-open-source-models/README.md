<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a83aac52158c23161046cbd13faa2b",
  "translation_date": "2025-10-17T19:48:48+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "fi"
}
-->
[![Avoimet lähdemallit](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.fi.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Johdanto

Avoimen lähdekoodin LLM-mallit ovat jännittävä ja jatkuvasti kehittyvä alue. Tämän oppitunnin tarkoituksena on tarjota syvällinen katsaus avoimiin lähdemalleihin. Jos etsit tietoa siitä, miten suljetut mallit vertautuvat avoimiin malleihin, siirry ["Erilaisten LLM-mallien tutkiminen ja vertailu" -oppituntiin](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Tässä oppitunnissa käsitellään myös hienosäätöä, mutta yksityiskohtaisempi selitys löytyy ["LLM-mallien hienosäätö" -oppitunnista](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Oppimistavoitteet

- Ymmärtää avoimia lähdemalleja
- Ymmärtää avoimien lähdemallien käytön hyödyt
- Tutkia Hugging Facen ja Azure AI Studion tarjoamia avoimia malleja

## Mitä ovat avoimet lähdemallit?

Avoimen lähdekoodin ohjelmistoilla on ollut keskeinen rooli teknologian kehityksessä eri aloilla. Open Source Initiative (OSI) on määritellyt [10 kriteeriä ohjelmistolle](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst), jotta se voidaan luokitella avoimeksi lähdekoodiksi. Lähdekoodin on oltava avoimesti jaettu OSI:n hyväksymän lisenssin alaisena.

Vaikka LLM-mallien kehittäminen sisältää samankaltaisia elementtejä kuin ohjelmistojen kehittäminen, prosessi ei ole täysin sama. Tämä on herättänyt paljon keskustelua yhteisössä siitä, mitä avoimen lähdekoodin määritelmä tarkoittaa LLM-mallien yhteydessä. Jotta malli vastaisi perinteistä avoimen lähdekoodin määritelmää, seuraavien tietojen tulisi olla julkisesti saatavilla:

- Mallin koulutuksessa käytetyt tietoaineistot.
- Täydet mallipainot osana koulutusta.
- Arviointikoodi.
- Hienosäätökoodi.
- Täydet mallipainot ja koulutusmittarit.

Tällä hetkellä vain harvat mallit täyttävät nämä kriteerit. [OLMo-malli, jonka on luonut Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst), kuuluu tähän kategoriaan.

Tässä oppitunnissa viittaamme malleihin "avoimina malleina", koska ne eivät välttämättä täytä yllä olevia kriteerejä kirjoitushetkellä.

## Avoimien mallien hyödyt

**Erittäin muokattavissa** - Koska avoimet mallit julkaistaan yksityiskohtaisilla koulutustiedoilla, tutkijat ja kehittäjät voivat muokata mallin sisäisiä toimintoja. Tämä mahdollistaa erittäin erikoistuneiden mallien luomisen, jotka on hienosäädetty tiettyyn tehtävään tai tutkimusalueeseen. Esimerkkejä tästä ovat koodin generointi, matemaattiset operaatiot ja biologia.

**Kustannukset** - Näiden mallien käyttö- ja käyttöönottohinta per token on alhaisempi kuin suljettujen mallien. Generatiivisten tekoälysovellusten rakentamisessa kannattaa tarkastella suorituskyvyn ja hinnan suhdetta mallien käytössä omassa käyttötapauksessa.

![Mallin kustannukset](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.fi.png)  
Lähde: Artificial Analysis

**Joustavuus** - Avoimien mallien kanssa työskentely mahdollistaa joustavuuden eri mallien käytössä tai niiden yhdistämisessä. Esimerkkinä tästä on [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), jossa käyttäjä voi valita käytettävän mallin suoraan käyttöliittymässä:

![Valitse malli](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.fi.png)

## Erilaisten avointen mallien tutkiminen

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), jonka Meta on kehittänyt, on avoin malli, joka on optimoitu keskustelupohjaisiin sovelluksiin. Tämä johtuu sen hienosäätömenetelmästä, joka sisälsi suuren määrän dialogia ja ihmisten antamaa palautetta. Tämän menetelmän ansiosta malli tuottaa enemmän ihmisten odotuksia vastaavia tuloksia, mikä parantaa käyttäjäkokemusta.

Joistakin Llama-mallin hienosäädetyistä versioista esimerkkejä ovat [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), joka on erikoistunut japanin kieleen, ja [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), joka on parannettu versio perusmallista.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) on avoin malli, joka keskittyy korkeaan suorituskykyyn ja tehokkuuteen. Se käyttää Mixture-of-Experts-lähestymistapaa, joka yhdistää joukon erikoistuneita asiantuntijamalleja yhdeksi järjestelmäksi, jossa syötteen mukaan valitaan käytettävät mallit. Tämä tekee laskennasta tehokkaampaa, koska mallit käsittelevät vain syötteitä, joihin ne ovat erikoistuneet.

Joistakin Mistral-mallin hienosäädetyistä versioista esimerkkejä ovat [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), joka keskittyy lääketieteelliseen alaan, ja [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), joka suorittaa matemaattisia laskutoimituksia.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) on LLM, jonka on luonut Technology Innovation Institute (**TII**). Falcon-40B on koulutettu 40 miljardilla parametrilla, ja sen on osoitettu suoriutuvan paremmin kuin GPT-3 pienemmällä laskentabudjetilla. Tämä johtuu sen käyttämästä FlashAttention-algoritmista ja monikyselyhuomiosta, jotka vähentävät muistivaatimuksia inferenssiaikana. Tämän lyhentyneen inferenssiajan ansiosta Falcon-40B soveltuu hyvin keskustelusovelluksiin.

Joistakin Falcon-mallin hienosäädetyistä versioista esimerkkejä ovat [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), avointen mallien pohjalta rakennettu assistentti, ja [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), joka tarjoaa paremman suorituskyvyn kuin perusmalli.

## Kuinka valita

Avoimen mallin valintaan ei ole yhtä oikeaa vastausta. Hyvä lähtökohta on käyttää Azure AI Studion tehtäväkohtaisen suodatuksen ominaisuutta. Tämä auttaa ymmärtämään, millaisiin tehtäviin malli on koulutettu. Hugging Face ylläpitää myös LLM Leaderboardia, joka näyttää parhaiten suoriutuvat mallit tiettyjen mittareiden perusteella.

Kun haluat vertailla LLM-malleja eri tyyppien välillä, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) on toinen erinomainen resurssi:

![Mallin laatu](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.fi.png)  
Lähde: Artificial Analysis

Jos työskentelet tietyn käyttötapauksen parissa, hienosäädettyjen versioiden etsiminen, jotka keskittyvät samaan alueeseen, voi olla tehokasta. Useiden avointen mallien kokeileminen ja niiden suorituskyvyn arviointi omien ja käyttäjiesi odotusten mukaan on myös hyvä käytäntö.

## Seuraavat askeleet

Avoimien mallien parasta puolta on, että niiden kanssa voi aloittaa työskentelyn melko nopeasti. Tutustu [Azure AI Foundry Model Catalogiin](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), joka sisältää erityisen Hugging Face -kokoelman näistä malleista, joita käsittelimme tässä.

## Oppiminen ei lopu tähän, jatka matkaasi

Tämän oppitunnin jälkeen tutustu [Generative AI Learning -kokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn tietämyksesi kehittämistä!

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.