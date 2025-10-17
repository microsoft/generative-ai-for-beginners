<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T19:45:12+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "fi"
}
-->
[![Avoimet lähdemallit](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.fi.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# LLM:n hienosäätö

Suurten kielimallien käyttö generatiivisten tekoälysovellusten rakentamiseen tuo mukanaan uusia haasteita. Yksi keskeinen ongelma on varmistaa mallin tuottaman sisällön vastausten laatu (tarkkuus ja osuvuus) käyttäjän antamaan pyyntöön. Aiemmissa oppitunneissa käsittelimme tekniikoita, kuten kehotteen suunnittelua ja hakuun perustuvaa generointia, jotka pyrkivät ratkaisemaan ongelman _muokkaamalla kehotteen syötettä_ olemassa olevaan malliin.

Tämän päivän oppitunnilla käsittelemme kolmatta tekniikkaa, **hienosäätöä**, joka pyrkii ratkaisemaan haasteen _kouluttamalla mallia uudelleen_ lisädatan avulla. Sukelletaan yksityiskohtiin.

## Oppimistavoitteet

Tämä oppitunti esittelee hienosäädön käsitteen esikoulutetuille kielimalleille, tutkii tämän lähestymistavan etuja ja haasteita sekä tarjoaa ohjeita siitä, milloin ja miten hienosäätöä kannattaa käyttää generatiivisten tekoälymallien suorituskyvyn parantamiseksi.

Oppitunnin lopussa sinun pitäisi pystyä vastaamaan seuraaviin kysymyksiin:

- Mitä hienosäätö kielimalleille tarkoittaa?
- Milloin ja miksi hienosäätö on hyödyllistä?
- Kuinka voin hienosäätää esikoulutettua mallia?
- Mitkä ovat hienosäädön rajoitukset?

Valmis? Aloitetaan.

## Havainnollistettu opas

Haluatko saada yleiskuvan siitä, mitä käsittelemme ennen kuin sukellamme syvemmälle? Tutustu tähän havainnollistettuun oppaaseen, joka kuvaa oppimismatkaa tämän oppitunnin aikana - ydinajatuksista ja hienosäädön motivaatiosta prosessin ja parhaiden käytäntöjen ymmärtämiseen hienosäätötehtävän suorittamiseksi. Tämä on kiehtova aihe tutkittavaksi, joten älä unohda tarkistaa [Resurssit](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) -sivua saadaksesi lisälinkkejä itseohjautuvaan oppimismatkaasi!

![Havainnollistettu opas kielimallien hienosäätöön](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.fi.png)

## Mitä hienosäätö kielimalleille tarkoittaa?

Määritelmän mukaan suuret kielimallit ovat _esikoulutettuja_ suurilla määrillä tekstiä, jotka on kerätty monipuolisista lähteistä, kuten internetistä. Kuten olemme oppineet aiemmilla oppitunneilla, tarvitsemme tekniikoita, kuten _kehotteen suunnittelu_ ja _hakuun perustuva generointi_, parantaaksemme mallin vastausten laatua käyttäjän kysymyksiin ("kehotteisiin").

Yksi suosittu kehotteen suunnittelutekniikka sisältää mallille enemmän ohjeita siitä, mitä vastaukselta odotetaan, joko antamalla _ohjeita_ (selkeät ohjeet) tai _muutamia esimerkkejä_ (epäsuorat ohjeet). Tätä kutsutaan _few-shot learningiksi_, mutta sillä on kaksi rajoitusta:

- Mallin token-rajoitukset voivat rajoittaa annettavien esimerkkien määrää ja vaikuttavuutta.
- Mallin token-kustannukset voivat tehdä esimerkkien lisäämisestä jokaiseen kehotteeseen kallista ja rajoittaa joustavuutta.

Hienosäätö on yleinen käytäntö koneoppimisjärjestelmissä, jossa otamme esikoulutetun mallin ja koulutamme sen uudelleen uudella datalla parantaaksemme sen suorituskykyä tiettyyn tehtävään. Kielimallien kontekstissa voimme hienosäätää esikoulutetun mallin _huolellisesti valitulla esimerkkijoukolla tiettyä tehtävää tai sovellusaluetta varten_ luodaksemme **räätälöidyn mallin**, joka voi olla tarkempi ja osuvampi kyseiselle tehtävälle tai alueelle. Hienosäädön sivuhyötynä on myös se, että se voi vähentää tarvittavien esimerkkien määrää few-shot learningissa - vähentäen tokenien käyttöä ja siihen liittyviä kustannuksia.

## Milloin ja miksi meidän pitäisi hienosäätää malleja?

Tässä kontekstissa, kun puhumme hienosäädöstä, viittaamme **valvottuun** hienosäätöön, jossa uudelleenkoulutus tehdään **lisäämällä uutta dataa**, joka ei ollut osa alkuperäistä koulutusdatakokonaisuutta. Tämä eroaa valvomattomasta hienosäätömenetelmästä, jossa mallia koulutetaan uudelleen alkuperäisellä datalla, mutta eri hyperparametreilla.

Keskeinen asia muistaa on, että hienosäätö on edistynyt tekniikka, joka vaatii tietyn tason asiantuntemusta haluttujen tulosten saavuttamiseksi. Jos se tehdään väärin, se ei välttämättä tuota odotettuja parannuksia ja voi jopa heikentää mallin suorituskykyä kohdealueellasi.

Joten ennen kuin opit "kuinka" hienosäätää kielimalleja, sinun täytyy tietää "miksi" sinun pitäisi valita tämä reitti ja "milloin" aloittaa hienosäätöprosessi. Aloita kysymällä itseltäsi nämä kysymykset:

- **Käyttötapaus**: Mikä on hienosäädön _käyttötapauksesi_? Mitä osaa nykyisestä esikoulutetusta mallista haluat parantaa?
- **Vaihtoehdot**: Oletko kokeillut _muita tekniikoita_ haluttujen tulosten saavuttamiseksi? Käytä niitä vertailukohtana.
  - Kehotteen suunnittelu: Kokeile tekniikoita, kuten few-shot-kehotteita, joissa on esimerkkejä asiaankuuluvista kehotusvastauksista. Arvioi vastausten laatu.
  - Hakuun perustuva generointi: Kokeile kehotteiden täydentämistä hakutuloksilla, jotka on haettu etsimällä dataasi. Arvioi vastausten laatu.
- **Kustannukset**: Oletko tunnistanut hienosäädön kustannukset?
  - Säädettävyys - onko esikoulutettu malli saatavilla hienosäätöön?
  - Työ - koulutusdatan valmistelu, mallin arviointi ja hienosäätö.
  - Laskenta - hienosäätötehtävien suorittaminen ja hienosäädetyn mallin käyttöönotto.
  - Data - riittävän laadukkaiden esimerkkien saatavuus hienosäätövaikutuksen saavuttamiseksi.
- **Hyödyt**: Oletko vahvistanut hienosäädön hyödyt?
  - Laatu - ylittääkö hienosäädetty malli vertailukohdan?
  - Kustannukset - vähentääkö se tokenien käyttöä yksinkertaistamalla kehotteita?
  - Laajennettavuus - voiko perusmallia käyttää uudelleen uusille alueille?

Vastaamalla näihin kysymyksiin sinun pitäisi pystyä päättämään, onko hienosäätö oikea lähestymistapa käyttötapauksessasi. Ihanteellisesti lähestymistapa on perusteltu vain, jos hyödyt ylittävät kustannukset. Kun päätät jatkaa, on aika miettiä _kuinka_ voit hienosäätää esikoulutettua mallia.

Haluatko lisätietoja päätöksentekoprosessista? Katso [Hienosäätääkö vai ei](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kuinka voimme hienosäätää esikoulutettua mallia?

Hienosäätääksesi esikoulutettua mallia tarvitset:

- esikoulutetun mallin hienosäätöä varten
- datakokonaisuuden hienosäätöön
- koulutusympäristön hienosäätötehtävän suorittamiseen
- isännöintialustan hienosäädetyn mallin käyttöönottoon

## Hienosäätö käytännössä

Seuraavat resurssit tarjoavat vaiheittaisia opetusohjelmia, jotka opastavat sinut todellisen esimerkin läpi valitun mallin ja huolellisesti valitun datakokonaisuuden avulla. Näiden opetusohjelmien läpikäymiseen tarvitset tilin kyseisellä palveluntarjoajalla sekä pääsyn asiaankuuluvaan malliin ja datakokonaisuuksiin.

| Palveluntarjoaja | Opetusohjelma                                                                                                                                                                       | Kuvaus                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI           | [Kuinka hienosäätää chat-malleja](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Opettele hienosäätämään `gpt-35-turbo` tiettyä aluetta varten ("reseptiassistentti") valmistamalla koulutusdataa, suorittamalla hienosäätötehtävä ja käyttämällä hienosäädettyä mallia päättelyyn.                                                                                                                                                                                                                                              |
| Azure OpenAI     | [GPT 3.5 Turbo hienosäätöopetusohjelma](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Opettele hienosäätämään `gpt-35-turbo-0613` -mallia **Azurella** ottamalla askeleet koulutusdatan luomiseen ja lataamiseen, hienosäätötehtävän suorittamiseen. Ota käyttöön ja käytä uutta mallia.                                                                                                                                                                                                                                                                 |
| Hugging Face     | [Hienosäätö LLM:ille Hugging Facen avulla](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Tämä blogikirjoitus opastaa sinut hienosäätämään _avointa LLM:ää_ (esim. `CodeLlama 7B`) käyttämällä [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) -kirjastoa ja [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) avoimilla [datakokonaisuuksilla](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) Hugging Facessa. |
|                   |                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain     | [Hienosäätö LLM:ille AutoTrainin avulla](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (tai AutoTrain Advanced) on Hugging Facen kehittämä Python-kirjasto, joka mahdollistaa hienosäädön monille eri tehtäville, mukaan lukien LLM-hienosäätö. AutoTrain on kooditon ratkaisu, ja hienosäätö voidaan tehdä omassa pilvessä, Hugging Face Spacesissa tai paikallisesti. Se tukee sekä verkkopohjaista käyttöliittymää, CLI:tä että koulutusta yaml-konfiguraatiotiedostojen avulla.                                                                               |
|                   |                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Tehtävä

Valitse yksi yllä olevista opetusohjelmista ja käy se läpi. _Saatamme kopioida version näistä opetusohjelmista Jupyter Notebooks -tiedostoihin tässä repossa vain viitteeksi. Käytä alkuperäisiä lähteitä saadaksesi uusimmat versiot_.

## Hienoa työtä! Jatka oppimista.

Tämän oppitunnin jälkeen tutustu [Generatiivisen tekoälyn oppimiskokoelmaan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn tietämyksesi kehittämistä!

Onnittelut!! Olet suorittanut tämän kurssin v2-sarjan viimeisen oppitunnin! Älä lopeta oppimista ja rakentamista. \*\*Tutustu [RESURSSIT](RESOURCES.md?WT.mc_id=academic-105485-koreyst) -sivuun saadaksesi lisäehdotuksia juuri tästä aiheesta.

Myös v1-sarjan oppitunteja on päivitetty lisää tehtävillä ja käsitteillä. Joten ota hetki aikaa päivittääksesi tietosi - ja ole hyvä [ja jaa kysymyksesi ja palautteesi](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) auttaaksesi meitä parantamaan näitä oppitunteja yhteisölle.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.