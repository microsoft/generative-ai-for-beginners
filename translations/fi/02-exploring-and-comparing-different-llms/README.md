<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6b7629b8ee4d7d874a27213e903d86a7",
  "translation_date": "2025-10-17T19:42:38+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "fi"
}
-->
# Tutkimus ja vertailu eri LLM-malleista

[![Tutkimus ja vertailu eri LLM-malleista](../../../translated_images/02-lesson-banner.ef94c84979f97f60f07e27d905e708cbcbdf78707120553ccab27d91c947805b.fi.png)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon_

Edellisessä oppitunnissa näimme, kuinka Generatiivinen AI muuttaa teknologian kenttää, kuinka Suuret Kielimallit (LLM:t) toimivat ja kuinka yritys - kuten meidän startupimme - voi soveltaa niitä omiin käyttötapauksiinsa ja kasvaa! Tässä luvussa tarkastelemme ja vertailemme eri tyyppisiä suuria kielimalleja (LLM) ymmärtääksemme niiden hyvät ja huonot puolet.

Seuraava askel startupimme matkalla on tutkia nykyistä LLM-mallien kenttää ja ymmärtää, mitkä niistä sopivat käyttötapaukseemme.

## Johdanto

Tämä oppitunti kattaa:

- Eri tyyppiset LLM:t nykyisessä kentässä.
- Mallien testaaminen, iterointi ja vertailu Azurea käyttäen.
- Kuinka ottaa LLM käyttöön.

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat:

- Valita oikean mallin käyttötapaukseesi.
- Ymmärtää, kuinka testata, iteroida ja parantaa mallisi suorituskykyä.
- Tietää, kuinka yritykset ottavat malleja käyttöön.

## Ymmärrä eri tyyppiset LLM:t

LLM:t voidaan luokitella niiden arkkitehtuurin, koulutusdatan ja käyttötapauksen perusteella. Näiden erojen ymmärtäminen auttaa startupiamme valitsemaan oikean mallin tilanteeseen ja ymmärtämään, kuinka testata, iteroida ja parantaa suorituskykyä.

LLM-malleja on monenlaisia, ja mallin valinta riippuu siitä, mihin aiot käyttää niitä, datastasi, budjetistasi ja muista tekijöistä.

Riippuen siitä, aiotko käyttää malleja tekstin, äänen, videon, kuvien generointiin ja niin edelleen, saatat valita eri tyyppisen mallin.

- **Ääni ja puheentunnistus**. Tähän tarkoitukseen Whisper-tyyppiset mallit ovat erinomainen valinta, sillä ne ovat yleiskäyttöisiä ja suunniteltu puheentunnistukseen. Malli on koulutettu monipuolisella äänidatalla ja pystyy monikieliseen puheentunnistukseen. Lue lisää [Whisper-tyyppisistä malleista täältä](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Kuvien generointi**. Kuvien generointiin DALL-E ja Midjourney ovat kaksi hyvin tunnettua vaihtoehtoa. DALL-E on saatavilla Azure OpenAI:n kautta. [Lue lisää DALL-E:stä täältä](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) ja myös tämän oppimateriaalin luvusta 9.

- **Tekstin generointi**. Useimmat mallit on koulutettu tekstin generointiin, ja valittavana on laaja valikoima malleja GPT-3.5:stä GPT-4:ään. Niiden kustannukset vaihtelevat, ja GPT-4 on kallein. Kannattaa tutustua [Azure OpenAI -leikkikenttään](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) arvioidaksesi, mitkä mallit sopivat parhaiten tarpeisiisi kyvykkyyden ja kustannusten suhteen.

- **Monimodaalisuus**. Jos haluat käsitellä useita datatyyppejä syötteessä ja tulosteessa, kannattaa tutustua malleihin kuten [gpt-4 turbo visionilla tai gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) - uusimpiin OpenAI-malleihin - jotka yhdistävät luonnollisen kielen käsittelyn visuaaliseen ymmärrykseen ja mahdollistavat vuorovaikutuksen monimodaalisten käyttöliittymien kautta.

Mallin valinta tarjoaa joitakin perusominaisuuksia, mutta ne eivät välttämättä riitä. Usein yrityksellä on erityistä dataa, joka täytyy jollain tavalla välittää LLM:lle. Tähän on olemassa muutamia eri lähestymistapoja, joista lisää seuraavissa osioissa.

### Perusmallit vs. LLM:t

Termi Perusmalli (Foundation Model) [keksittiin Stanfordin tutkijoiden toimesta](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) ja määriteltiin AI-malliksi, joka täyttää tietyt kriteerit, kuten:

- **Ne on koulutettu valvomattomalla oppimisella tai itsevalvotulla oppimisella**, eli ne on koulutettu merkitsemättömällä monimodaalisella datalla, eikä niiden koulutusprosessissa tarvita ihmisen annotointia tai datan merkitsemistä.
- **Ne ovat erittäin suuria malleja**, jotka perustuvat erittäin syviin neuroverkkoihin, jotka on koulutettu miljardeilla parametreilla.
- **Ne on yleensä tarkoitettu toimimaan muiden mallien "perustana"**, eli niitä voidaan käyttää lähtökohtana muiden mallien rakentamiseen, mikä voidaan tehdä hienosäätämällä.

![Perusmallit vs. LLM:t](../../../translated_images/FoundationModel.e4859dbb7a825c94b284f17eae1c186aabc21d4d8644331f5b007d809cf8d0f2.fi.png)

Kuvan lähde: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Tämän eron selventämiseksi otetaan esimerkkinä ChatGPT. Ensimmäisen ChatGPT-version rakentamiseen käytettiin mallia nimeltä GPT-3.5 perusmallina. Tämä tarkoittaa, että OpenAI käytti chat-spesifistä dataa luodakseen GPT-3.5:stä hienosäädetyn version, joka oli erikoistunut suoriutumaan hyvin keskustelutilanteissa, kuten chatbotit.

![Perusmalli](../../../translated_images/Multimodal.2c389c6439e0fc51b0b7b226d95d7d900d372ae66902d71b8ce5ec4951b8efbe.fi.png)

Kuvan lähde: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Avoimen lähdekoodin vs. kaupalliset mallit

Toinen tapa luokitella LLM-malleja on se, ovatko ne avoimen lähdekoodin vai kaupallisia.

Avoimen lähdekoodin mallit ovat malleja, jotka ovat julkisesti saatavilla ja kaikkien käytettävissä. Ne ovat usein saatavilla mallin luoneen yrityksen tai tutkimusyhteisön toimesta. Näitä malleja voidaan tarkastella, muokata ja räätälöidä erilaisiin LLM-käyttötapauksiin. Ne eivät kuitenkaan aina ole optimoituja tuotantokäyttöön, eivätkä välttämättä ole yhtä suorituskykyisiä kuin kaupalliset mallit. Lisäksi avoimen lähdekoodin mallien rahoitus voi olla rajallista, eikä niitä välttämättä ylläpidetä pitkällä aikavälillä tai päivitetä uusimmalla tutkimuksella. Esimerkkejä suosituista avoimen lähdekoodin malleista ovat [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) ja [LLaMA](https://llama.meta.com).

Kaupalliset mallit ovat malleja, jotka ovat yrityksen omistamia eikä niitä ole saatavilla julkisesti. Nämä mallit ovat usein optimoituja tuotantokäyttöön. Niitä ei kuitenkaan voi tarkastella, muokata tai räätälöidä eri käyttötapauksiin. Lisäksi ne eivät aina ole ilmaisia, ja niiden käyttö voi vaatia tilauksen tai maksun. Käyttäjillä ei myöskään ole kontrollia mallin koulutuksessa käytettyyn dataan, mikä tarkoittaa, että heidän tulee luottaa mallin omistajaan datan yksityisyyden ja vastuullisen AI:n käytön varmistamisessa. Esimerkkejä suosituista kaupallisista malleista ovat [OpenAI-mallit](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) ja [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Upotukset vs. Kuvien generointi vs. Tekstin ja koodin generointi

LLM:t voidaan myös luokitella niiden tuottaman ulostulon perusteella.

Upotukset ovat joukko malleja, jotka voivat muuntaa tekstin numeeriseen muotoon, jota kutsutaan upotukseksi. Upotus on tekstin numeerinen esitys, joka helpottaa koneiden ymmärtää sanojen tai lauseiden välisiä suhteita ja jota voidaan käyttää syötteenä muille malleille, kuten luokittelumalleille tai klusterointimalleille, jotka toimivat paremmin numeerisella datalla. Upotusmalleja käytetään usein siirto-oppimisessa, jossa malli rakennetaan korvaavaa tehtävää varten, josta on runsaasti dataa, ja sitten mallin painoja (upotuksia) käytetään uudelleen muihin tehtäviin. Esimerkki tästä kategoriasta on [OpenAI upotukset](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Upotus](../../../translated_images/Embedding.c3708fe988ccf76073d348483dbb7569f622211104f073e22e43106075c04800.fi.png)

Kuvien generointimallit ovat malleja, jotka tuottavat kuvia. Näitä malleja käytetään usein kuvien muokkaukseen, kuvien synteesiin ja kuvien kääntämiseen. Kuvien generointimallit koulutetaan usein suurilla kuvadataseteillä, kuten [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), ja niitä voidaan käyttää uusien kuvien luomiseen tai olemassa olevien kuvien muokkaamiseen esimerkiksi täydennyksen, superresoluution ja väritystekniikoiden avulla. Esimerkkejä ovat [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) ja [Stable Diffusion -mallit](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Kuvien generointi](../../../translated_images/Image.349c080266a763fd255b840a921cd8fc526ed78dc58708fa569ff1873d302345.fi.png)

Tekstin ja koodin generointimallit ovat malleja, jotka tuottavat tekstiä tai koodia. Näitä malleja käytetään usein tekstin tiivistämiseen, kääntämiseen ja kysymyksiin vastaamiseen. Tekstin generointimallit koulutetaan usein suurilla tekstidataseteillä, kuten [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), ja niitä voidaan käyttää uuden tekstin luomiseen tai kysymyksiin vastaamiseen. Koodin generointimallit, kuten [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), koulutetaan usein suurilla koodidataseteillä, kuten GitHubilla, ja niitä voidaan käyttää uuden koodin luomiseen tai olemassa olevan koodin virheiden korjaamiseen.

![Tekstin ja koodin generointi](../../../translated_images/Text.a8c0cf139e5cc2a0cd3edaba8d675103774e6ddcb3c9fc5a98bb17c9a450e31d.fi.png)

### Kooderi-dekooderi vs. Vain dekooderi

Puhutaanpa LLM-mallien eri arkkitehtuureista analogian avulla.

Kuvittele, että esimiehesi antaa sinulle tehtäväksi laatia tietovisan opiskelijoille. Sinulla on kaksi kollegaa; toinen vastaa sisällön luomisesta ja toinen sen tarkistamisesta.

Sisällön luoja on kuin vain dekooderi -malli, hän voi katsoa aihetta ja nähdä, mitä olet jo kirjoittanut, ja sitten kirjoittaa kurssin sen perusteella. Hän on erittäin hyvä kirjoittamaan kiinnostavaa ja informatiivista sisältöä, mutta ei kovin hyvä ymmärtämään aihetta ja oppimistavoitteita. Esimerkkejä vain dekooderi -malleista ovat GPT-perheen mallit, kuten GPT-3.

Tarkistaja on kuin vain kooderi -malli, hän katsoo kirjoitettua kurssia ja vastauksia, huomaa niiden väliset suhteet ja ymmärtää kontekstin, mutta ei ole hyvä sisällön tuottamisessa. Esimerkki vain kooderi -mallista olisi BERT.

Kuvittele, että meillä voisi olla joku, joka sekä luo että tarkistaa tietovisan, tämä on kooderi-dekooderi -malli. Esimerkkejä olisivat BART ja T5.

### Palvelu vs. Malli

Puhutaan nyt palvelun ja mallin eroista. Palvelu on pilvipalveluntarjoajan tarjoama tuote, joka on usein yhdistelmä malleja, dataa ja muita komponentteja. Malli on palvelun ydinosa, ja se on usein perusmalli, kuten LLM.

Palvelut ovat usein optimoituja tuotantokäyttöön ja niitä on usein helpompi käyttää kuin malleja graafisen käyttöliittymän kautta. Palvelut eivät kuitenkaan aina ole ilmaisia, ja niiden käyttö voi vaatia tilauksen tai maksun, vastineeksi palvelun omistajan laitteiden ja resurssien hyödyntämisestä, kulujen optimoinnista ja helpposta skaalautumisesta. Esimerkki palvelusta on [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), joka tarjoaa käyttömäärään perustuvan hinnoittelumallin, eli käyttäjiltä veloitetaan suhteessa siihen, kuinka paljon he käyttävät palvelua. Lisäksi Azure OpenAI Service tarjoaa yritystason turvallisuutta ja vastuullisen AI-kehyksen mallien kyvykkyyksien päälle.

Mallit ovat vain neuroverkkoja, joissa on parametrit, painot ja muut. Ne mahdollistavat yritysten ajon paikallisesti, mutta vaativat laitteiden ostamista, rakenteen luomista skaalautumiseen ja lisenssin ostamista tai avoimen lähdekoodin mallin käyttöä. Malli kuten LLaMA on saatavilla käytettäväksi, mutta sen ajaminen vaatii laskentatehoa.

## Kuinka testata ja iteroida eri malleilla ymmärtääkseen suorituskykyä Azuren avulla

Kun tiimimme on tutkinut nykyistä LLM-mallien kenttää ja tunnistanut hyviä ehdokkaita heidän skenaarioihinsa, seuraava askel on testata niitä heidän datallaan ja työkuormallaan. Tämä on iteratiivinen prosessi, joka tehdään kokeiluilla ja mittauksilla.
Useimmat aiemmin mainitsemamme mallit (OpenAI-mallit, avoimen lähdekoodin mallit kuten Llama2 ja Hugging Face transformers) ovat saatavilla [Model Catalog](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) -katalogissa [Azure AI Studiossa](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) on pilvialusta, joka on suunniteltu kehittäjille generatiivisten tekoälysovellusten rakentamiseen ja koko kehitysprosessin hallintaan - kokeiluista arviointiin - yhdistämällä kaikki Azure AI -palvelut yhteen keskitettyyn käyttöliittymään. Model Catalog Azure AI Studiossa mahdollistaa käyttäjälle:

- Löytää kiinnostava Foundation Model - joko omistettu tai avoimen lähdekoodin - suodattamalla tehtävän, lisenssin tai nimen mukaan. Hakujen helpottamiseksi mallit on järjestetty kokoelmiin, kuten Azure OpenAI -kokoelma, Hugging Face -kokoelma ja muita.

![Model catalog](../../../translated_images/AzureAIStudioModelCatalog.3cf8a499aa8ba0314f2c73d4048b3225d324165f547525f5b7cfa5f6c9c68941.fi.png)

- Tarkastella mallikorttia, joka sisältää yksityiskohtaisen kuvauksen mallin käyttötarkoituksesta ja koulutusdatasta, koodiesimerkkejä sekä arviointituloksia sisäisestä arviointikirjastosta.

![Model card](../../../translated_images/ModelCard.598051692c6e400d681a713ba7717e8b6e5e65f08d12131556fcec0f1789459b.fi.png)

- Verrata mallien ja teollisuudessa saatavilla olevien datasetien vertailuarvoja arvioidakseen, mikä malli sopii parhaiten liiketoimintaskenaarioon, [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) -paneelin kautta.

![Model benchmarks](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.fi.png)

- Hienosäätää mallia omalla koulutusdatalla parantaakseen mallin suorituskykyä tietyssä työkuormassa hyödyntäen Azure AI Studion kokeilu- ja seurantatoimintoja.

![Model fine-tuning](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.fi.png)

- Ottaa käyttöön alkuperäinen esikoulutettu malli tai hienosäädetty versio etäreaaliaikaisessa inferenssissä - hallinnoitu laskenta - tai serverittömässä API-päätepisteessä - [pay-as-you-go](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - mahdollistamaan sovellusten kuluttavan sitä.

![Model deployment](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.fi.png)

> [!NOTE]
> Kaikkia katalogin malleja ei tällä hetkellä voi hienosäätää ja/tai ottaa käyttöön pay-as-you-go-mallilla. Tarkista mallikortista yksityiskohdat mallin ominaisuuksista ja rajoituksista.

## LLM-tulosten parantaminen

Olemme startup-tiimimme kanssa tutkineet erilaisia LLM-malleja ja pilvialustaa (Azure Machine Learning), joka mahdollistaa eri mallien vertailun, niiden arvioinnin testidatalla, suorituskyvyn parantamisen ja käyttöönoton inferenssipäätepisteissä.

Mutta milloin kannattaa harkita mallin hienosäätöä esikoulutetun mallin sijaan? Onko olemassa muita tapoja parantaa mallin suorituskykyä tietyissä työkuormissa?

On olemassa useita lähestymistapoja, joita yritys voi käyttää saadakseen haluamansa tulokset LLM-mallista. Voit valita eri tyyppisiä malleja, joilla on eri koulutustasoja, kun otat LLM:n käyttöön tuotannossa, ja niillä on erilaisia monimutkaisuuden, kustannusten ja laadun tasoja. Tässä joitakin lähestymistapoja:

- **Prompt engineering kontekstilla**. Ideana on antaa riittävästi kontekstia kehotuksessa, jotta saat haluamasi vastaukset.

- **Retrieval Augmented Generation, RAG**. Tietosi voivat olla esimerkiksi tietokannassa tai verkkopäätepisteessä. Jotta tämä tieto tai sen osa sisältyisi kehotukseen, voit hakea relevantin datan ja lisätä sen osaksi käyttäjän kehotusta.

- **Hienosäädetty malli**. Tässä mallia koulutetaan lisää omalla datalla, mikä tekee mallista tarkemman ja vastaamaan paremmin tarpeitasi, mutta voi olla kallista.

![LLMs deployment](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.fi.png)

Kuvan lähde: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering kontekstilla

Esikoulutetut LLM:t toimivat erittäin hyvin yleisissä luonnollisen kielen tehtävissä, jopa lyhyellä kehotuksella, kuten lauseen täydentämisellä tai kysymyksellä – niin sanottu "zero-shot"-oppiminen.

Kuitenkin mitä tarkemmin käyttäjä voi muotoilla kysymyksensä, yksityiskohtaisella pyynnöllä ja esimerkeillä – Kontekstilla – sitä tarkempi ja lähempänä käyttäjän odotuksia vastaus on. Tässä tapauksessa puhutaan "one-shot"-oppimisesta, jos kehotus sisältää vain yhden esimerkin, ja "few-shot"-oppimisesta, jos se sisältää useita esimerkkejä. Prompt engineering kontekstilla on kustannustehokkain tapa aloittaa.

### Retrieval Augmented Generation (RAG)

LLM-malleilla on rajoitus, että ne voivat käyttää vain dataa, joka on käytetty niiden koulutuksessa vastauksen tuottamiseen. Tämä tarkoittaa, että ne eivät tiedä mitään koulutuksen jälkeen tapahtuneista asioista, eivätkä ne voi käyttää ei-julkista tietoa (kuten yrityksen dataa). 

Tämä voidaan ratkaista RAG-tekniikalla, joka täydentää kehotusta ulkoisella datalla dokumenttien osina, ottaen huomioon kehotuksen pituusrajoitukset. Tätä tukevat vektoridatabasetyökalut (kuten [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), jotka hakevat hyödylliset osat ennalta määritellyistä tietolähteistä ja lisäävät ne kehotuksen kontekstiin.

Tämä tekniikka on erittäin hyödyllinen, kun yrityksellä ei ole tarpeeksi dataa, aikaa tai resursseja hienosäätää LLM-mallia, mutta haluaa silti parantaa suorituskykyä tietyssä työkuormassa ja vähentää virheellisten tietojen riskiä, kuten todellisuuden vääristelyä tai haitallista sisältöä.

### Hienosäädetty malli

Hienosäätö on prosessi, joka hyödyntää siirto-oppimista "mukauttaakseen" mallin tiettyyn tehtävään tai ongelman ratkaisuun. Toisin kuin few-shot-oppiminen ja RAG, se tuottaa uuden mallin, jossa on päivitetyt painot ja vinoumat. Se vaatii joukon koulutusesimerkkejä, jotka koostuvat yksittäisestä syötteestä (kehotus) ja siihen liittyvästä vastauksesta (täydennys). 

Tämä olisi suositeltava lähestymistapa, jos:

- **Hienosäädettyjen mallien käyttö**. Yritys haluaa käyttää hienosäädettyjä vähemmän kyvykkäitä malleja (kuten upotusmalleja) korkeatasoisten mallien sijaan, mikä johtaa kustannustehokkaampaan ja nopeampaan ratkaisuun.

- **Huomioida viive**. Viive on tärkeä tietylle käyttötapaukselle, joten ei ole mahdollista käyttää erittäin pitkiä kehotuksia tai esimerkkien määrää, joka ylittää kehotuksen pituusrajan.

- **Pysyä ajan tasalla**. Yrityksellä on paljon korkealaatuista dataa ja totuudenmukaisia merkintöjä sekä resursseja pitää tämä data ajan tasalla ajan myötä.

### Koulutettu malli

LLM:n kouluttaminen alusta alkaen on epäilemättä vaikein ja monimutkaisin lähestymistapa, joka vaatii valtavia määriä dataa, osaavia resursseja ja asianmukaista laskentatehoa. Tätä vaihtoehtoa tulisi harkita vain tilanteessa, jossa yrityksellä on toimialakohtainen käyttötapaus ja suuri määrä toimialakohtaista dataa.

## Tietotesti

Mikä voisi olla hyvä lähestymistapa LLM:n täydennystulosten parantamiseen?

1. Prompt engineering kontekstilla  
1. RAG  
1. Hienosäädetty malli  

V: 3, jos sinulla on aikaa, resursseja ja korkealaatuista dataa, hienosäätö on parempi vaihtoehto pysyä ajan tasalla. Kuitenkin, jos haluat parantaa tuloksia ja sinulla ei ole aikaa, kannattaa harkita ensin RAG:ia.

## 🚀 Haaste

Lue lisää siitä, miten voit [käyttää RAG:ia](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) yrityksessäsi.

## Hienoa työtä, jatka oppimista

Kun olet suorittanut tämän oppitunnin, tutustu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) -kokoelmaan jatkaaksesi generatiivisen tekoälyn tietämyksesi kehittämistä!

Siirry oppituntiin 3, jossa tarkastelemme, miten [rakentaa generatiivista tekoälyä vastuullisesti](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.