<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:19:53+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "fi"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.fi.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Johdanto

Avoimen lähdekoodin LLM-mallit tarjoavat jännittävän ja jatkuvasti kehittyvän maailman. Tämän oppitunnin tavoitteena on tarjota syvällinen katsaus avoimen lähdekoodin malleihin. Jos etsit tietoa siitä, miten suljetut mallit vertautuvat avoimen lähdekoodin malleihin, siirry ["Erilaisten LLM-mallien tutkiminen ja vertailu" -oppituntiin](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Tämä oppitunti käsittelee myös hienosäätöä, mutta yksityiskohtaisempi selitys löytyy ["LLM-mallien hienosäätö" -oppitunnista](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Oppimistavoitteet

- Ymmärtää avoimen lähdekoodin mallit
- Ymmärtää avoimen lähdekoodin mallien hyödyt
- Tutkia Hugging Facen ja Azure AI Studion tarjoamia avoimia malleja

## Mitä ovat avoimen lähdekoodin mallit?

Avoimen lähdekoodin ohjelmistoilla on ollut merkittävä rooli teknologian kehityksessä eri aloilla. Open Source Initiative (OSI) on määritellyt [10 kriteeriä ohjelmistolle](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst), jotta se voidaan luokitella avoimeksi lähdekoodiksi. Lähdekoodin tulee olla avoimesti jaettu OSI:n hyväksymän lisenssin alaisuudessa.

Vaikka LLM-mallien kehittäminen sisältää samankaltaisia elementtejä kuin ohjelmistojen kehittäminen, prosessi ei ole täysin sama. Tämä on herättänyt paljon keskustelua yhteisössä siitä, mitä avoimen lähdekoodin määritelmä tarkoittaa LLM-mallien yhteydessä. Jotta malli vastaisi perinteistä avoimen lähdekoodin määritelmää, seuraavat tiedot tulisi olla julkisesti saatavilla:

- Mallin koulutuksessa käytetyt datasetit.
- Täydelliset mallipainot osana koulutusta.
- Arviointikoodi.
- Hienosäätökoodi.
- Täydelliset mallipainot ja koulutusmetriikat.

Tällä hetkellä vain harvat mallit täyttävät nämä kriteerit. [OLMo-malli, jonka on luonut Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst), on yksi näistä.

Tässä oppitunnissa viittaamme malleihin "avoimina malleina", koska ne eivät välttämättä täytä yllä olevia kriteerejä kirjoitushetkellä.

## Avoimien mallien hyödyt

**Erittäin muokattavissa** - Koska avoimet mallit julkaistaan yksityiskohtaisilla koulutustiedoilla, tutkijat ja kehittäjät voivat muokata mallin sisäistä rakennetta. Tämä mahdollistaa erittäin erikoistuneiden mallien luomisen, jotka on hienosäädetty tiettyyn tehtävään tai tutkimusalueeseen. Esimerkkejä tästä ovat koodin generointi, matemaattiset laskelmat ja biologia.

**Kustannukset** - Näiden mallien käyttö- ja käyttöönottohinta per token on alhaisempi kuin suljettujen mallien. Generatiivisten AI-sovellusten rakentamisessa kannattaa tarkastella suorituskykyä suhteessa hintaan mallien käytön yhteydessä.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.fi.png)  
Lähde: Artificial Analysis

**Joustavuus** - Avoimien mallien kanssa työskentely mahdollistaa joustavuuden eri mallien käytössä tai niiden yhdistämisessä. Esimerkkinä tästä on [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), jossa käyttäjä voi valita käytettävän mallin suoraan käyttöliittymässä:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.fi.png)

## Erilaisten avoimien mallien tutkiminen

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), jonka Meta on kehittänyt, on avoin malli, joka on optimoitu chat-pohjaisiin sovelluksiin. Tämä johtuu sen hienosäätömenetelmästä, joka sisälsi suuren määrän dialogia ja ihmispalautetta. Tämän menetelmän ansiosta malli tuottaa enemmän ihmisten odotuksia vastaavia tuloksia, mikä parantaa käyttäjäkokemusta.

Esimerkkejä Llama-mallin hienosäädetyistä versioista ovat [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), joka erikoistuu japanin kieleen, ja [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), joka on parannettu versio perusmallista.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) on avoin malli, joka keskittyy korkeaan suorituskykyyn ja tehokkuuteen. Se käyttää Mixture-of-Experts-lähestymistapaa, jossa joukko erikoistuneita asiantuntijamalleja yhdistetään yhdeksi järjestelmäksi, jossa syötteen perusteella valitaan käytettävät mallit. Tämä tekee laskennasta tehokkaampaa, koska mallit käsittelevät vain syötteitä, joihin ne ovat erikoistuneet.

Esimerkkejä Mistral-mallin hienosäädetyistä versioista ovat [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), joka keskittyy lääketieteelliseen alaan, ja [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), joka suorittaa matemaattisia laskelmia.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) on LLM, jonka on luonut Technology Innovation Institute (**TII**). Falcon-40B koulutettiin 40 miljardilla parametrilla, ja sen on osoitettu suoriutuvan paremmin kuin GPT-3 pienemmällä laskentabudjetilla. Tämä johtuu sen käyttämästä FlashAttention-algoritmista ja multiquery attention -menetelmästä, jotka vähentävät muistivaatimuksia inferenssiaikana. Tämän lyhentyneen inferenssiajan ansiosta Falcon-40B soveltuu chat-sovelluksiin.

Esimerkkejä Falcon-mallin hienosäädetyistä versioista ovat [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), avoimiin malleihin perustuva assistentti, ja [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), joka tarjoaa paremman suorituskyvyn kuin perusmalli.

## Kuinka valita

Avoimen mallin valintaan ei ole yhtä oikeaa vastausta. Hyvä lähtökohta on käyttää Azure AI Studion tehtäväkohtaisen suodatusominaisuutta. Tämä auttaa ymmärtämään, millaisiin tehtäviin malli on koulutettu. Hugging Face ylläpitää myös LLM Leaderboardia, joka näyttää parhaiten suoriutuvat mallit tiettyjen mittareiden perusteella.

Jos haluat vertailla LLM-malleja eri tyyppien välillä, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) on toinen erinomainen resurssi:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.fi.png)  
Lähde: Artificial Analysis

Jos työskentelet tietyn käyttötapauksen parissa, hienosäädettyjen versioiden etsiminen, jotka keskittyvät samaan alueeseen, voi olla tehokasta. Useiden avoimien mallien kokeileminen ja niiden suorituskyvyn arviointi omien ja käyttäjiesi odotusten mukaan on myös hyvä käytäntö.

## Seuraavat askeleet

Avoimien mallien parasta puolta on, että niiden kanssa työskentelyn voi aloittaa nopeasti. Tutustu [Azure AI Foundry Model Catalogiin](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), joka sisältää erityisen Hugging Face -kokoelman näistä malleista, joita käsittelimme tässä.

## Oppiminen ei lopu tähän, jatka matkaasi

Tämän oppitunnin jälkeen tutustu [Generative AI Learning -kokoelmaan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen AI:n osaamisen kehittämistä!

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.