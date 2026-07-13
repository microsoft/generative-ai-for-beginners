[![Avoimen lähdekoodin mallit](../../../translated_images/fi/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Räätälöi LLM-malliasi

Suurten kielimallien käyttäminen generatiivisten tekoälysovellusten rakentamiseen tuo mukanaan uusia haasteita. Keskeinen kysymys on varmistaa vastauksen laatu (tarkkuus ja merkityksellisyys) mallin tuottamassa sisällössä käyttäjän pyynnön perusteella. Aiemmissa oppitunneissa käsittelimme tekniikoita, kuten kehotteen suunnittelua ja tiedonhakuun perustuvaa generointia, jotka pyrkivät ratkaisemaan ongelmaa _muokkaamalla mallin syötettä_.

Tänään tarkastelemme kolmatta tekniikkaa, **täsmäoppimista**, joka pyrkii ratkaisemaan haasteen _kouluttamalla mallia uudelleen_ lisädatan avulla. Sukelletaan yksityiskohtiin.

## Oppimistavoitteet

Tässä oppitunnissa perehdytään täsmäoppimisen käsitteeseen esikoulutetuilla kielimalleilla, tutustutaan tämän lähestymistavan hyötyihin ja haasteisiin sekä annetaan ohjeita, milloin ja miten täsmäoppimista voidaan käyttää generatiivisten tekoälymallien suorituskyvyn parantamiseen.

Oppitunnin lopussa sinun tulisi pystyä vastaamaan seuraaviin kysymyksiin:

- Mitä täsmäoppiminen kielimalleille tarkoittaa?
- Milloin ja miksi täsmäoppiminen on hyödyllistä?
- Kuinka voin täsmäopettaa esikoulutetun mallin?
- Mitkä ovat täsmäoppimisen rajoitukset?

Valmis? Aloitetaan.

## Kuvitettu opas

Haluatko saada kokonaiskuvan siitä, mitä aiomme käsitellä ennen syvempää tutustumista? Katso tämä kuvitettu opas, joka kuvaa oppimismatkaa tälle oppitunnille - alkaen täsmäoppimisen keskeisten käsitteiden ja motivaation oppimisesta aina prosessin ja parhaiden käytäntöjen ymmärtämiseen täsmäoppimistehtävän suorittamiseksi. Tämä on kiehtova aihe tutkittavaksi, joten muista myös katsoa [Resurssit](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) -sivu lisälinkkejä itseohjattuun oppimiseen!

![Kuvitettu opas kielimallien täsmäoppimiseen](../../../translated_images/fi/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Mitä täsmäoppiminen kielimalleille tarkoittaa?

Määritelmän mukaan suuret kielimallit on _esikoulutettu_ suuriin tekstimääriin, joita on kerätty monipuolisista lähteistä, mukaan lukien internet. Kuten olemme oppineet aiemmissa oppitunneissa, tarvitsemme tekniikoita kuten _kehotteen suunnittelua_ ja _tiedonhakuun perustuvaa generointia_ parantaaksemme mallin vastauksien laatua käyttäjän kysymyksiin ("kehotteisiin").

Yleinen kehotteen suunnittelun tekniikka on antaa mallille enemmän ohjeita siitä, mitä vastauksessa odotetaan joko antamalla _ohjeita_ (eksplisiittinen ohjaus) tai _antamalla muutama esimerkki_ (implisiittinen ohjaus). Tätä kutsutaan _muutama-esimerkkinen oppimiseksi_, mutta siinä on kaksi rajoitusta:

- Mallin token-rajoitukset voivat estää antamiesi esimerkkien määrää ja rajoittaa tehokkuutta.
- Mallin token-kustannukset voivat tehdä esimerkkien lisäämisestä jokaiseen kehotteeseen kallista ja rajoittaa joustavuutta.

Täsmäoppiminen on yleinen käytäntö koneoppimisjärjestelmissä, jossa otetaan esikoulutettu malli ja koulutetaan sitä uudelleen uudella datalla parantaakseen sen suorituskykyä tietyssä tehtävässä. Kielimallien yhteydessä voimme täsmäopettaa esikoulutettua mallia _valikoidulla joukolla esimerkkejä tiettyä tehtävää tai sovellusaluetta varten_ luodaksemme **räätälöidyn mallin**, joka voi olla tarkempi ja merkityksellisempi juuri kyseiseen tehtävään tai alueeseen. Täsmäoppimisen sivu-etuna on myös se, että se voi vähentää muutama-esimerkkisen oppimisen tarvitsemien esimerkkien määrää - vähentäen token-kulutusta ja siihen liittyviä kustannuksia.

## Milloin ja miksi täsmäopettaa malleja?

Tässä yhteydessä, kun puhumme täsmäoppimisesta, tarkoitamme **valvottua** täsmäoppimista, jossa uudelleenkoulutus tehdään **lisäämällä uutta dataa**, jota ei ollut alkuperäisessä koulutusdatassa. Tämä eroaa valvomattomasta täsmäkoulutuksesta, jossa mallia uudelleenkoulutetaan alkuperäiseen dataan perustuen, mutta eri hyperparametreilla.

Tärkeintä on muistaa, että täsmäoppiminen on edistynyt tekniikka, joka vaatii tietyn tason asiantuntemusta toivottujen tulosten saavuttamiseksi. Jos sitä tehdään väärin, se ei välttämättä tuota odotettuja parannuksia, ja saattaa jopa heikentää mallin suorituskykyä kohdealueellasi.

Joten ennen kuin opit "miten" täsmäopettaa kielimalleja, sinun tulee tietää "miksi" tämä tie kannattaa valita ja "milloin" aloittaa täsmäoppimisprosessi. Aloita kysymällä itseltäsi nämä kysymykset:

- **Käyttötapaus**: Mikä on _käyttötapauksesi_ täsmäoppimiselle? Mitä mallin osa-aluetta haluat parantaa?
- **Vaihtoehdot**: Oletko kokeillut _muita tekniikoita_ haluttujen tulosten saavuttamiseksi? Käytä niitä perustana vertailulle.
  - Kehotteen suunnittelu: Kokeile esimerkiksi muutama-esimerkkistä promptausta asiaankuuluvilla esimerkeillä. Arvioi vastausten laatu.
  - Tiedonhakuun perustuva generointi: Yritä täydentää kehotteita hakutuloksilla, jotka löydät datastasi. Arvioi vastausten laatu.
- **Kustannukset**: Oletko tunnistanut täsmäoppimisen kustannukset?
  - Täsmäytettävyys - onko esikoulutettu malli saatavilla täsmäoppimiseen?
  - Työmäärä - koulutusdatan valmistelu, mallin arviointi ja hienosäätö.
  - Laskenta - täsmäoppimisen suorittaminen ja täsmäytetyn mallin käyttöönotto
  - Data - riittävän laadukkaiden esimerkkien saatavuus täsmäoppimisen vaikutukseen
- **Hyödyt**: Oletko varmistanut täsmäoppimisen hyödyt?
  - Laatu - ylittikö täsmäytetty malli perusmallin suorituskyvyn?
  - Kustannukset - vähentääkö se tokenin kulutusta yksinkertaistamalla kehotteita?
  - Joustavuus - voitko hyödyntää perusmallia uusilla alueilla?

Vastaamalla näihin kysymyksiin sinun pitäisi pystyä päättämään, onko täsmäoppiminen oikea lähestymistapa käyttötapauksellesi. Ihanteellisesti tapa on perusteltu vain, jos hyödyt ovat suuremmat kuin kustannukset. Kun päätät jatkaa, on aika miettiä _miten_ voit täsmäopettaa esikoulutettua mallia.

Haluatko lisää näkemyksiä päätöksentekoprosessiin? Katso [Täsmäopeta vai älä täsmäopeta](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kuinka voimme täsmäopettaa esikoulutetun mallin?

Täsmäoppimiseen tarvitset:

- täsmäytettävän esikoulutetun mallin
- datasetin täsmäoppimista varten
- koulutusympäristön täsmäoppimistehtävän suorittamiseksi
- hosting-ympäristön täsmäytetyn mallin käyttöönottamiseksi

## Täsmäoppiminen käytännössä

> **Huom:** Joissakin alla olevissa opetusohjelmissa mainittu `gpt-35-turbo` / `gpt-3.5-turbo` on poistettu käytöstä sekä inferenssissä että täsmäoppimisessa. Jos aloitat uuden täsmäoppimistehtävän tänään, valitse sen sijaan tällä hetkellä tuettu malli, kuten `gpt-4o-mini` tai `gpt-4.1-mini`. Katso [Täsmäytettävien mallien lista](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) ajantasaisista malleista. Näiden opetusohjelmien käsitteet ja vaiheet pätevät yhä.

Seuraavat resurssit tarjoavat askel askeleelta ohjeita opastamaan sinua todellisen esimerkin läpi käyttämällä valittua mallia valikoidulla datasetilla. Näitä opetusohjelmia varten tarvitset tilin kyseisellä palveluntarjoajalla, sekä pääsyn asiaankuuluviin malleihin ja datoihin.

| Tarjoaja     | Opetusohjelma                                                                                                                                                                  | Kuvaus                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Kuinka täsmäopettaa chat-malleja](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Opettele täsmäopettamaan `gpt-35-turbo` tiettyyn toimialaan ("reseptiassistenti") valmistamalla koulutusdataa, suorittamalla täsmäoppimistehtävä ja käyttämällä täsmäytettyä mallia inferenssiin.                                                                                                                                                                                                                                   |
| Azure OpenAI | [GPT 3.5 Turbo täsmäoppimisen opas](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst)           | Opettele täsmäopettamaan `gpt-35-turbo-0613` mallia **Azurella** askel askeleelta luoden ja lataen koulutusdataa, suorittamalla täsmäoppimistehtävän sekä käyttöönottoa ja uuden mallin käyttöä.                                                                                                                                                                                                                                    |
| Hugging Face | [Kielimallien täsmäoppiminen Hugging Facella](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                          | Tämä blogikirjoitus opastaa täsmäoppimisessa _avoimelle LLM-mallille_ (esim. `CodeLlama 7B`) käyttäen [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) kirjasto & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) avoimilla [dataseteillä](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) Hugging Facessa.      |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Kielimallien täsmäoppiminen AutoTrainilla](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                               | AutoTrain (tai AutoTrain Advanced) on Hugging Facen python-kirjasto, joka mahdollistaa täsmäoppimisen moniin eri tehtäviin, mukaan lukien LLM-täsmäoppiminen. AutoTrain on kooditon ratkaisu ja täsmäoppimista voi tehdä omassa pilvessä, Hugging Face Spacessa tai paikallisesti. Tukee web-pohjaista GUI:ta, komentoriviä sekä koulutusta yaml-konfiguraatiotiedostojen avulla.                                                                              |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Kielimallien täsmäoppiminen Unslothilla](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                               | Unsloth on avoimen lähdekoodin kehys, joka tukee LLM-täsmäoppimista ja vahvistusoppimista (RL). Unsloth virtaviivaistaa paikallisen koulutuksen, arvioinnin ja käyttöönoton valmiiksi rakennetuilla [notebookeilla](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Tukee myös tekstistä puheeksi (TTS), BERT- ja multimodaalisia malleja. Aloittaaksesi lue heidän vaiheittainen [Täsmäoppimisen opas LLM:lle](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                 |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tehtävä

Valitse yllä olevista opetusohjelmista yksi ja käy se läpi. _Saatamme kopioida osan näistä opetusohjelmista Jupyter Notebookeihin tässä repossa vain viitteeksi. Käytä kuitenkin alkuperäisiä lähteitä saadaksesi uusimmat versiot_.

## Hienoa työtä! Jatka oppimista.

Kun olet suorittanut tämän oppitunnin, tutustu [Generative AI Learning kokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn tietojesi kehittämistä!

Onneksi olkoon!! Olet suorittanut tämän kurssin v2-sarjan viimeisen oppitunnin! Älä lopeta oppimista ja rakentamista. \*\*Tutustu [RESURSSIT](RESOURCES.md?WT.mc_id=academic-105485-koreyst) -sivuun saadaksesi lisää ehdotuksia juuri tähän aiheeseen.

Myös v1-sarjamme oppitunnit on päivitetty lisäämällä tehtäviä ja konsepteja. Joten ota hetki ja virkistä tietosi - ja ole hyvä ja [jaa kysymyksesi ja palautteesi](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) auttaaksesi meitä parantamaan näitä oppitunteja yhteisölle.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->