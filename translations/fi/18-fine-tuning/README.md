[![Avoimen lähdekoodin mallit](../../../translated_images/fi/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# LLM-mallin hienosäätö

Suurten kielimallien käyttäminen generatiivisten tekoälysovellusten rakentamiseen tuo mukanaan uusia haasteita. Keskeinen kysymys on varmistaa vastausten laatu (tarkkuus ja merkityksellisyys) mallin tuottamassa sisällössä käyttäjän pyynnön perusteella. Aiemmissa oppitunneissa käsittelimme tekniikoita, kuten kehotteen suunnittelu ja hakuun perustuva generointi, jotka yrittävät ratkaista ongelman _muokkaamalla mallin syötteenä olevaa kehotetta_.

Nykyisessä oppitunnissa käsittelemme kolmatta tekniikkaa, **hienosäätöä**, joka pyrkii ratkaisemaan haasteen _kouluttamalla mallia uudelleen_ lisäaineistolla. Sukelletaan yksityiskohtiin.

## Oppimistavoitteet

Tässä oppitunnissa esittelemme käsitteen hienosäädölle valmiiksi koulutetuissa kielimalleissa, tarkastelemme tämän lähestymistavan etuja ja haasteita sekä annamme ohjeita, milloin ja miten hienosäätöä kannattaa käyttää parantamaan generatiivisten tekoälymalliesi suorituskykyä.

Oppitunnin lopussa pystyt vastaamaan seuraaviin kysymyksiin:

- Mitä hienosäätö tarkoittaa kielimalleissa?
- Milloin ja miksi hienosäätö on hyödyllistä?
- Kuinka voin hienosäätää valmiiksi koulutettua mallia?
- Mitkä ovat hienosäädön rajoitukset?

Valmiina? Aloitetaan.

## Kuvitettu opas

Haluatko saada kokonaiskuvan siitä, mitä aiomme käsitellä ennen syventymistä? Tutustu tähän kuvitettuun oppaaseen, joka kuvaa oppimispolkua tässä oppitunnissa – ydinkäsitteiden ja hienosäädön motiivien oppimisesta aina prosessin ja parhaiden käytäntöjen ymmärtämiseen hienosäätötehtävän toteuttamisessa. Tämä on kiehtova aihe tutkimiseen, joten älä unohda tarkistaa [Resurssit](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) -sivua lisälinkkejä varten, jotka tukevat itseopiskelupolkua!

![Kuvitettu opas kielimallien hienosäätöön](../../../translated_images/fi/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Mitä hienosäätö tarkoittaa kielimalleissa?

Määritelmän mukaan suuret kielimallit on _valmiiksi koulutettu_ suuriin tekstimääriin, joita on kerätty monista lähteistä, mukaan lukien internet. Kuten olemme oppineet aiemmissa oppitunneissa, tarvitsemme tekniikoita kuten _kehotteen suunnittelu_ ja _haulla rikastettu generointi_ parantamaan mallin vastausten laatua käyttäjän kysymyksiin ("kehotteet").

Suosittu kehotteen suunnittelutekniikka on antaa mallille enemmän ohjeistusta siitä, mitä vastauksessa odotetaan, joko tarjoamalla _ohjeita_ (selkeä ohjaus) tai _antamalla muutama esimerkki_ (epäsuora ohjaus). Tätä kutsutaan _pienellä oppimisella_, mutta sillä on kaksi rajoitusta:

- Mallin token-rajoitukset voivat rajoittaa annettavien esimerkkien määrää ja tehokkuutta.
- Mallin token-kustannukset voivat tehdä esimerkkien lisäämisestä jokaiseen kehotteeseen kallista ja rajoittaa joustavuutta.

Hienosäätö on yleinen käytäntö koneoppimisjärjestelmissä, joissa otetaan valmiiksi koulutettu malli ja koulutetaan sitä uudelleen uusilla tiedoilla, jotta sen suorituskyky tiettyyn tehtävään paranee. Kielimallien yhteydessä voimme hienosäätää valmiiksi koulutettua mallia _huolellisesti valitulla esimerkkiajolla tietystä tehtävästä tai sovellusalueesta_ luodaksemme **räätälöidyn mallin**, joka voi olla tarkempi ja merkityksellisempi kyseiselle tehtävälle tai alueelle. Hienosäädön sivuvaikutuksena on myös, että se voi vähentää tarvittavien esimerkkien määrää pienellä oppimisella – vähentäen tokenien käyttöä ja siihen liittyviä kustannuksia.

## Milloin ja miksi meidän pitäisi hienosäätää malleja?

Tässä yhteydessä, kun puhumme hienosäädöstä, tarkoitamme **valvottua** hienosäätöä, jossa uudelleenkoulutus tehdään **lisäämällä uutta dataa**, jota ei ollut alkuperäisessä koulutusjoukossa. Tämä eroaa valvomattomasta hienosäädöstä, jossa mallia koulutetaan uudelleen alkuperäisellä datalla, mutta eri hyperparametreilla.

Tärkeintä on muistaa, että hienosäätö on edistynyt tekniikka, joka vaatii tietyn tason asiantuntemusta haluttujen tulosten saavuttamiseksi. Jos sitä ei tehdä oikein, se ei välttämättä tuo odotettuja parannuksia ja saattaa jopa heikentää mallin suorituskykyä kohdistetulla alueella.

Joten ennen kuin opit "kuinka" hienosäätää kielimalleja, sinun täytyy tietää "miksi" valitset tämän tien ja "milloin" aloittaa hienosäätöprosessi. Aloita kysymällä itseltäsi nämä kysymykset:

- **Käyttötapaus**: Mikä on sinun _käyttötapauksesi_ hienosäädölle? Mitä haluat parantaa nykyisessä valmiiksi koulutetussa mallissa?
- **Vaihtoehdot**: Oletko kokeillut _muita menetelmiä_ saavuttaaksesi toivotut tulokset? Käytä niitä vertailupohjana.
  - Kehotteen suunnittelu: Kokeile tekniikoita, kuten pienellä oppimisella esimerkkien avulla merkityksellisistä kehotteista. Arvioi vastausten laatua.
  - Hakuun rikastettu generointi: Kokeile rikastaa kehotteita hakutuloksilla, jotka saat tietojesi haulla. Arvioi vastausten laatua.
- **Kustannukset**: Oletko tunnistanut hienosäädön kustannukset?
  - Säädettävyys – onko valmiiksi koulutettu malli käytettävissä hienosäätöön?
  - Työmäärä – koulutusdatan valmistelu, mallin arviointi ja hienosäätö
  - Suorituskyky – hienosäätötyöskentelyn ajaminen ja hienosäädön mallin käyttöönotto
  - Data – pääsy riittävän laadukkaisiin esimerkkeihin hienosäädön vaikutuksen aikaansaamiseksi
- **Hyödyt**: Oletko varmistunut hienosäädön eduista?
  - Laatu – paransiko hienosäädetty malli vertailukohtaa?
  - Kustannukset – vähentääkö se token-käyttöä yksinkertaistamalla kehotteita?
  - Laajennettavuus – voitko käyttää perusmallia uudelleen uusilla alueilla?

Vastaamalla näihin kysymyksiin sinun pitäisi pystyä päättämään, onko hienosäätö oikea lähestymistapa sinun käyttötapaukseesi. Ihannetapauksessa se on perusteltua vain, jos hyödyt ylittävät kustannukset. Kun päätät jatkaa, on aika miettiä _miten_ hienosäätää valmiiksi koulutettu malli.

Haluatko saada lisää näkemyksiä päätöksentekoprosessiin? Katso [Hienosäätö vai ei hienosäätöä](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Kuinka voimme hienosäätää valmiiksi koulutetun mallin?

Hienosäätöön tarvitset:

- valmiiksi koulutetun mallin hienosäädettäväksi
- aineiston hienosäätöä varten
- koulutusympäristön hienosäätötyön suorittamiseen
- käyttöönottoympäristön hienosäädetyn mallin käyttöönottoa varten

## Hienosäätö Microsoft Foundryllä

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) on paikka, jossa hienosäätö, käyttöönotto ja räätälöityjen mallien hallinta tapahtuu Azurella nykyään (se yhdistää aiemmin Azure OpenAI Studion ja Azure AI Studion toiminnot). Ennen työn aloittamista on hyvä ymmärtää, mitä Foundry tarjoaa - ja mitkä ovat suositellut parhaat käytännöt. Moottorin alla Foundry käyttää **LoRAa (low-rank adaptation)** mallien tehokkaaseen hienosäätöön, mikä pitää koulutuksen nopeampana ja edullisempana kuin painojen täydellinen uudelleenkoulutus.

### Vaihe 1: Valitse koulutustekniikka

Foundry tukee kolmea hienosäätötekniikkaa. **Aloita SFT:stä** – se kattaa laajimman valikoiman tilanteita.

| Tekniikka | Mitä se tekee | Milloin sitä käytetään |
| --- | --- | --- |
| **Ohjattu hienosäätö (SFT)** | Kouluttaa syöte-/vastesamplepareilla, jotta malli oppii tuottamaan haluamiasi vastauksia. | Tavallinen metodi useimpiin tehtäviin: erikoistuminen alaan, tehtävän suorituskyky, tyyli ja sävy, ohjeiden noudattaminen ja kielten mukauttaminen. |
| **Suora preferenssin optimointi (DPO)** | Oppii _suosituilta vs. ei-suosituilta_ vastauspareilta kohdentamaan tuotoksia ihmisten mieltymysten mukaisiksi. | Vastausten laadun, turvallisuuden ja kohdentamisen parantaminen, kun käytettävissä vertailevaa palautetta. |
| **Vahvistettu hienosäätö (RFT)** | Käyttää _arvioijilta_ saatavia palkkiosignaaleja monimutkaisten käyttäytymisten optimointiin vahvistusoppimisen avulla. | Objektiiviset, päättelyä vaativat alat (matematiikka, kemia, fysiikka) selkeillä oikeilla/väärillä vastauksilla. Vaatii enemmän koneoppimisosaamista. |

### Vaihe 2: Valitse koulutustaso

Foundry antaa valita, miten ja missä koulutus suoritetaan:

- **Standardi** – kouluttaa resurssisi alueella ja takaa datan säilymisen siellä. Käytä, kun datan pitää pysyä tietyssä alueessa.
- **Globaali** – edullisempi ja nopeampi jonottaa käyttämällä kapasiteettia oman alueesi ulkopuolella (data ja painot kopioidaan koulutusalueelle). Hyvä oletus, kun datan säilytyspaikkavaatimus ei päde.
- **Kehittäjä** – alhaisin hinta, käyttää käyttämätöntä kapasiteettia ilman latenssi- tai SLA-takuita (työt voidaan keskeyttää ja jatkaa). Ihanteellinen kokeiluun.

### Vaihe 3: Valitse perusmalli

Hienosäädettävät mallit sisältävät OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` ja `gpt-4.1-nano` (SFT; 4o/4.1-perhe tukee myös DPO:ta), päättelymallit `o4-mini` ja `gpt-5` (RFT), sekä avoimen lähdekoodin mallit kuten `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` ja `gpt-oss-20b` (SFT Foundryn resursseilla). Tarkista aina ajantasainen [Hienosäätömallien lista](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst) tuetuista menetelmistä, alueista ja saatavuudesta.

> Foundry tarjoaa kaksi toimintamallia: **palvelimeton** (kuluun perustuva hinnoittelu, ei GPU-rajoitusten hallintaa, OpenAI ja valitut mallit) ja **hallinnoitu suorituskyky** (vie omat VM:t Azure Machine Learningin kautta laajimman mallivalikoiman käyttämiseksi). Useimpien kannattaa aloittaa palvelimettomasta.

### Foundryn parhaat käytännöt

- **Vertaa ensin lähtötasoon.** Mittaa perusmallin suorituskyky kehotteen suunnittelulla ja RAG:lla _ennen_ hienosäätöä, jotta voit osoittaa parannuksen.
- **Aloita pienestä ja laajenna.** Aloita 50–100 korkealaatuisella esimerkillä lähestymistavan vahvistamiseksi, kasva sitten 500+ tuotantokäyttöön. Laatu on määrää tärkeämpää – karsi huonolaatuiset esimerkit.
- **Muotoile data oikein.** Koulutus- ja validointitiedostojen täytyy olla JSONL-muodossa, UTF-8 **BOMilla**, alle 512 Mt, käyttäen chat-completions -viestimuotoa. Sisällytä aina validointitiedosto, jotta voit seurata ylikoulutusta.
- **Pidä koulutusjärjestelmän kehotetta käytössä päättelyssä.** Käytä samaa järjestelmäviestiä mallin kutsussa kuin mitä käytit koulutuksessa.
- **Arvioi tarkistuspisteitä – älä ota viimeistä suoraan käyttöön.** Foundry säilyttää viimeiset kolme epookkia käyttöön otettavina tarkistuspisteinä; valitse parhaiten yleistyvä seuraamalla `train_loss` / `valid_loss` ja token-tarkkuutta.
- **Mittaa token-kustannukset laadun rinnalla** verrattaessa hienosäädettyä mallia lähtötasoon.
- **Jatkuva hienosäätö.** Voit hienosäätää jo hienosäädettyä mallia uudella datalla (tuettu OpenAI-malleilla).
- **Huomaa isännöintikustannukset.** Käytössä oleva räätälöity malli laskuttaa tuntiperusteisesti, ja käyttämätön käyttöönotto poistetaan 15 päivän jälkeen – siivoa tarpeettomat.

Käy läpi koko kädestä pitäen opastus [Mukauta mallia hienosäädöllä](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) ja tutustu opaisiin [DPO:sta](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) ja [RFT:stä](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst), kun olet valmis muihin tekniikoihin.

## Hienosäätö käytännössä

Seuraavat resurssit tarjoavat askel askeleelta opastuksia, jotka johdattavat sinut todennäköisen toteutusesimerkin pariin tällä hetkellä tuetulla mallilla ja huolellisesti valikoidulla aineistolla. Näiden kanssa työskentelemiseen tarvitset tilin kyseisellä palveluntarjoajalla sekä pääsyn asiaankuuluviin malleihin ja aineistoihin.

| Palveluntarjoaja     | Opas                                                                                                                                                                       | Kuvaus                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Kuinka hienosäätää chat-malleja](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Opettele hienosäätämään viimeisin OpenAI-chat-malli tiettyyn käyttötarkoitukseen ("reseptiavustaja") valmistamalla koulutusdata, suorittamalla hienosäätötyö ja käyttämällä hienosäädettyä mallia päättelyssä.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Mukauta mallia hienosäädöllä](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Opettele hienosäätämään tällä hetkellä tuettua mallia, kuten `gpt-4.1-mini` **Azuressa** Microsoft Foundryn avulla: valmistele ja lataa koulutus- ja validointidata, suorita hienosäätötyö, ota malli käyttöön ja käytä sitä.                                                                                                                                                                                                                                                                 |

| Hugging Face | [LLM-mallien hienosäätö Hugging Face -alustalla](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Tämä blogikirjoitus opastaa sinut hienosäätämään _avointa LLM:ää_ (esim. `CodeLlama 7B`) käyttäen [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) -kirjastoa ja [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) -työkalua avoimilla [aineistoilla](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) Hugging Face -alustalla. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [LLM-mallien hienosäätö AutoTrainilla](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (tai AutoTrain Advanced) on Hugging Facen kehittämä python-kirjasto, joka mahdollistaa hienosäädön moniin eri tehtäviin, mukaan lukien LLM-hienosäätö. AutoTrain on kooditon ratkaisu, ja hienosäätö voidaan suorittaa omassa pilvessäsi, Hugging Face Spaces -palvelussa tai paikallisesti. Se tukee sekä web-pohjaista käyttöliittymää, komentorivikäyttöä että koulutusta yaml-määritystiedostojen kautta.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [LLM-mallien hienosäätö Unslothilla](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth on avoimen lähdekoodin kehys, joka tukee LLM-hienosäätöä ja vahvistusoppimista (RL). Unsloth virtaviivaistaa paikallisen koulutuksen, arvioinnin ja käyttöönoton valmiiden [notebookien](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) avulla. Se tukee myös puheeksi muuntamista (TTS), BERT-malleja ja multimodaalisia malleja. Aloittaaksesi lue heidän vaiheittainen [LLM-mallien hienosäätö-opas](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tehtävä

Valitse jokin yllä olevista tutoriaaleista ja käy se läpi. _Saatamme toistaa joitain näistä tutoriaaleista Jupyter Notebookseissa tässä repoissa viitteeksi. Käytä kuitenkin suoraan alkuperäislähteitä saadaksesi uusimmat versiot_.

## Hienoa työtä! Jatka oppimista.

Tämän oppitunnin suorittamisen jälkeen tutustu [Generatiivisen tekoälyn oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn osaamisesi kehittämistä!

Onnittelut!! Olet suorittanut tämän kurssin v2-sarjan viimeisen oppitunnin! Älä lopeta oppimista ja rakentamista. \*\*Tutustu [RESURSSIT](RESOURCES.md?WT.mc_id=academic-105485-koreyst) -sivuun saadaksesi listan lisäehdotuksista juuri tähän aiheeseen liittyen.

Myös v1-sarjaamme on päivitetty lisää tehtäviä ja käsitteitä. Joten ota hetki kerrataksesi tietosi — ja ole hyvä, [jaa kysymyksesi ja palautteesi](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) auttaaksesi meitä parantamaan näitä oppitunteja yhteisölle.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->