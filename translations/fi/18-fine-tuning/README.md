<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T18:24:56+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "fi"
}
-->
[![Open Source Models](../../../../../translated_images/fi/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Hienosäätä LLM:ääsi

Suurten kielimallien käyttäminen generatiivisten tekoälysovellusten rakentamiseen tuo mukanaan uusia haasteita. Keskeinen kysymys on varmistaa vastausten laatu (tarkkuus ja merkityksellisyys) mallin tuottamassa sisällössä käyttäjän esittämään pyyntöön. Aiemmissa oppitunneissa olemme käsitelleet tekniikoita kuten kehotteiden suunnittelu ja hakua tukevan generoinnin, jotka pyrkivät ratkaisemaan ongelman muuttamalla olemassa olevan mallin _kehotteen syötettä_.

Tämän päivän oppitunnilla käsittelemme kolmatta tekniikkaa, **hienosäätöä**, joka pyrkii vastaamaan haasteeseen _mallin uudelleenkoulutuksella_ lisäaineistolla. Sukelletaan yksityiskohtiin.

## Oppimistavoitteet

Tässä oppitunnissa esitellään hienosäädön käsite esikoulutettuihin kielimalleihin, tutkitaan lähestymistavan etuja ja haasteita sekä annetaan ohjeita, milloin ja miten hienosäätöä voi käyttää generatiivisten tekoälymalliesi suorituskyvyn parantamiseen.

Oppitunnin lopussa sinun pitäisi pystyä vastaamaan seuraaviin kysymyksiin:

- Mitä hienosäätö kielimalleille tarkoittaa?
- Milloin ja miksi hienosäätö on hyödyllistä?
- Kuinka voin hienosäätää esikoulutetun mallin?
- Mitkä ovat hienosäädön rajoitukset?

Valmiina? Aloitetaan.

## Kuvitettu opas

Haluatko saada kokonaiskuvan siitä, mitä käsittelemme ennen syvempää sukellusta? Tutustu tähän kuvitettuun oppaaseen, joka kuvaa oppimispolkua tälle oppitunnille – alkaen ydinkäsitteiden ja hienosäädön motivoinnin oppimisesta aina hienosäätöprosessin ja parhaiden käytäntöjen ymmärtämiseen asti. Tämä on kiehtova aihe, joten muista vierailla myös [Resurssit](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) -sivulla lisälinkkien saamiseksi itseohjattua oppimista varten!

![Illustrated Guide to Fine Tuning Language Models](../../../../../translated_images/fi/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Mitä hienosäätö kielimalleille on?

Määritelmän mukaan suuret kielimallit on _esikoulutettu_ suurilla määrillä tekstiä, joka on kerätty monista lähteistä, mukaan lukien internet. Kuten olemme oppineet aiemmissa oppitunneissa, tarvitsemme tekniikoita kuten _kehotteiden suunnittelua_ ja _hakua tukevaa generointia_ parantamaan mallin vastausten laatua käyttäjän kysymyksiin ("kehotteisiin").

Suosittu kehotteiden suunnittelutekniikka on antaa mallille enemmän ohjausta siitä, mitä vastauksessa odotetaan, joko antamalla _ohjeita_ (eksplisiittinen ohjaus) tai _antamalla muutama esimerkki_ (implisiittinen ohjaus). Tätä kutsutaan _few-shot-oppimiseksi_, mutta siinä on kaksi rajoitetta:

- Mallin token-rajoitukset voivat rajoittaa annettavien esimerkkien määrää ja tehokkuutta.
- Mallin token-kustannukset voivat tehdä esimerkkien lisäämisestä jokaiseen kehotteeseen kallista ja rajoittaa joustavuutta.

Hienosäätö on koneoppimisjärjestelmissä yleinen käytäntö, jossa otetaan esikoulutettu malli ja koulutetaan sitä uudelleen uudella aineistolla parantaakseen sen suorituskykyä tietyssä tehtävässä. Kielimallien yhteydessä voimme hienosäätää esikoulutettua mallia _valikoidulla joukolla esimerkkejä tiettyyn tehtävään tai sovellusalueeseen_ luodaksemme **räätälöidyn mallin**, joka voi olla tarkempi ja merkityksellisempi juuri kyseiseen tehtävään tai alaan. Hienosäädön sivuetu on, että se voi myös vähentää tarvittavien esimerkkien määrää few-shot-oppimisessa – vähentäen token-käyttöä ja siihen liittyviä kustannuksia.

## Milloin ja miksi mallit pitäisi hienosäätää?

_Tässä_ yhteydessä, kun puhumme hienosäädöstä, tarkoitamme **valvottua** hienosäätöä, jossa mallin uudelleenkoulutus tehdään **lisäämällä uusia aineistoja**, joita ei ollut alkuperäisessä koulutusdatassa. Tämä eroaa valvomattomasta hienosäädön lähestymistavasta, jossa mallia koulutetaan uudelleen alkuperäisellä aineistolla, mutta eri hyperparametreillä.

Tärkein asia muistaa on, että hienosäätö on kehittynyt tekniikka, joka vaatii tiettyä asiantuntijuuden tasoa saavuttaakseen toivotut tulokset. Jos hienosäätö tehdään väärin, se ei välttämättä tuota odotettuja parannuksia, ja voi jopa heikentää mallin suorituskykyä kohdealueellasi.

Joten ennen kuin opit "miten" hienosäätää kielimalleja, sinun on tiedettävä "miksi" haluat käyttää tätä menetelmää ja "milloin" aloittaa hienosäätöprosessi. Aloita kysymällä itseltäsi nämä kysymykset:

- **Käyttötarkoitus**: Mikä on hienosäädön _käyttötarkoituksesi_? Mitä osa-aluetta nykyisessä esikoulutetussa mallissa haluat parantaa?
- **Vaihtoehdot**: Oletko kokeillut _muita tekniikoita_ saavuttaaksesi halutun lopputuloksen? Käytä niitä vertailutasoksi.
  - Kehotteiden suunnittelu: Kokeile few-shot-kehotteita esimerkkien avulla. Arvioi vastausten laatua.
  - Hakua tukevan generoinnin menetelmät: Kokeile laajentaa kehotteita hakutuloksilla omasta datastasi. Arvioi vastausten laatua.
- **Kustannukset**: Oletko tunnistanut hienosäädön kustannukset?
  - Säädettävyys – onko esikoulutettu malli saatavilla hienosäätöön?
  - Työmäärä – koulutusdatan valmistelu, mallin arviointi ja hienosäätö.
  - Laskenta – hienosäätötehtävien suorittaminen ja hienosäädetyn mallin käyttöönotto.
  - Data – riittävän laadukkaiden esimerkkien saatavuus hienosäädön vaikutuksen aikaansaamiseksi.
- **Edut**: Oletko varmistunut hienosäädön eduista?
  - Laatu – ylittikö hienosäädetty malli vertailutason?
  - Kustannukset – vähentääkö se token-kulutusta yksinkertaistamalla kehotteita?
  - Laajennettavuus – voitko käyttää pohjamallia uudelleen uusille sovellusalueille?

Vastaamalla näihin kysymyksiin sinun pitäisi pystyä päättämään, onko hienosäätö oikea tapaus juuri sinun käyttötarkoituksellesi. Ihanteellisesti lähestymistapa on perusteltu vain, jos edut ylittävät kustannukset. Kun päätät jatkaa, on aika miettiä, _kuinka_ voit hienosäätää esikoulutettua mallia.

Haluatko lisää näkemyksiä päätöksenteon tueksi? Katso [Hienosäätöön vai ei hienosäätöön](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kuinka hienosäätää esikoulutettua mallia?

Hienosäätääksesi esikoulutettua mallia tarvitset:

- esikoulutetun mallin hienosäätöä varten
- aineiston, jota käytät hienosäätöön
- koulutusympäristön hienosäätötehtävien suorittamiseen
- isäntäympäristön hienosäädetyn mallin käyttöönottoon

## Hienosäätö käytännössä

Seuraavat resurssit tarjoavat vaiheittaiset ohjeet, joiden avulla voit käytännössä kokeilla valitun mallin hienosäätöä valikoidulla aineistolla. Näiden opetusohjelmien käyttöön tarvitset tilin kyseisen palveluntarjoajan järjestelmässä sekä pääsyn asiaankuuluvaan malliin ja aineistoihin.

| Palveluntarjoaja | Opetusohjelma                                                                                                                                                                  | Kuvaus                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI           | [Miten hienosäätää chat-malleja](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)               | Opettele hienosäätämään `gpt-35-turbo` tiettyyn sovellusalueeseen ("reseptiavustaja") valmistamalla koulutusdataa, suorittamalla hienosäätötehtävä ja käyttämällä hienosäädettyä mallia ennusteisiin.                                                                                                                                                                                                            |
| Azure OpenAI     | [GPT 3.5 Turbon hienosäätö-opas](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst)           | Opi hienosäätämään `gpt-35-turbo-0613` -malli **Azure-palvelussa** luomalla ja lataamalla koulutusdataa, suorittamalla hienosäätötehtävä sekä ottamalla uusi malli käyttöön ja käyttämään sitä.                                                                                                                                                                                                                     |
| Hugging Face     | [LLM-mallien hienosäätö Hugging Facen avulla](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                      | Tämä blogikirjoitus opastaa hienosäätämään _avoin LLM:n_ (esim. `CodeLlama 7B`) käyttäen [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) -kirjastoa ja [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) -työkaluja avoimien [aineistojen](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) kanssa Hugging Facessa.  |
|                  |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 🤗 AutoTrain     | [LLM-mallien hienosäätö AutoTrainilla](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                    | AutoTrain (tai AutoTrain Advanced) on Hugging Facen kehittämä python-kirjasto, joka mahdollistaa hienosäädön moniin eri tehtäviin, mukaan lukien LLM-mallien hienosäätö. AutoTrain on kooditon ratkaisu, jossa hienosäätö voidaan tehdä omassa pilvessä, Hugging Face Spaces -palvelussa tai paikallisesti. Se tukee selainpohjaista käyttöliittymää, CLI:tä ja koulutusta yaml-konfiguraatiotiedostoilla.                                              |
|                  |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 🦥 Unsloth       | [LLM-mallien hienosäätö Unslothilla](https://github.com/unslothai/unsloth)                                                                                                  | Unsloth on avoimen lähdekoodin kehys, joka tukee LLM-mallien hienosäätöä ja vahvistusoppimista (RL). Unsloth virtaviivaistaa paikallisen koulutuksen, arvioinnin ja käyttöönoton valmiiden [muistikirjojen](https://github.com/unslothai/notebooks) avulla. Se tukee myös puheeksi muuntoa (TTS), BERT- ja multimodaalimalleja. Aloittaaksesi tutustu vaiheittaiseen [LLM-hienosäätöoppaaseen](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                |
|                  |                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                        |
## Tehtävä

Valitse yllä olevista opetusohjelmista yksi ja käy se läpi. _Saatamme kopioida näiden opetusohjelmien versiota Jupyter-notebookeihin tämän repoon vain viitteeksi. Käytä alkuperäisiä lähteitä saadaksesi viimeisimmät versiot_.

## Hienoa työtä! Jatka oppimista.

Kun olet suorittanut tämän oppitunnin, tutustu Generative AI Learning -kokoelmaamme osoitteessa [https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn tietämyksesi syventämistä!

Onnittelut!! Olet suorittanut tämän kurssin v2-sarjan viimeisen oppitunnin! Älä lopeta oppimista ja rakentamista. \*\*Tutustu [RESURSSIT](RESOURCES.md?WT.mc_id=academic-105485-koreyst) -sivuun saadaksesi lisää ehdotuksia juuri tähän aiheeseen.

Myös v1-sarjan oppitunnit on päivitetty lisäämällä uusia tehtäviä ja käsitteitä. Joten ota hetki päivittääksesi tietosi – ja pyydämme sinua [jakamaan kysymyksiäsi ja palautteesi](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) auttaaksesi meitä parantamaan näitä oppitunteja yhteisölle.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty tekoälykäännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->