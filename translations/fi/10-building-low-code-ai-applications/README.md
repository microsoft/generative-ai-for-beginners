# Rakennetaan vähäkoodisia tekoälysovelluksia

[![Rakennetaan vähäkoodisia tekoälysovelluksia](../../../translated_images/fi/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

## Johdanto

Nyt kun olemme oppineet rakentamaan kuvia tuottavia sovelluksia, puhutaan vähäkoodista. Generatiivista tekoälyä voidaan käyttää monilla eri alueilla, mukaan lukien vähäkoodi, mutta mitä vähäkoodi on ja miten voimme lisätä tekoälyä siihen?

Sovellusten ja ratkaisujen rakentaminen on helpottunut perinteisille kehittäjille ja ei-kehittäjille Vähäkoodikehitysalustojen avulla. Vähäkoodikehitysalustat mahdollistavat sovellusten ja ratkaisujen rakentamisen vähällä tai ilman koodausta. Tämä saavutetaan tarjoamalla visuaalinen kehitysympäristö, joka mahdollistaa komponenttien vetämisen ja pudottamisen sovellusten ja ratkaisujen rakentamiseen. Tämä mahdollistaa sovellusten ja ratkaisujen rakentamisen nopeammin ja vähäisemmillä resursseilla. Tässä oppitunnissa sukellamme syvälle siihen, miten vähäkoodia käytetään ja miten vähäkoodikehitystä voidaan parantaa tekoälyn avulla Power Platformin avulla.

Power Platform tarjoaa organisaatioille mahdollisuuden antaa tiimeilleen valtuudet rakentaa omia ratkaisujaan intuitiivisen vähäkoodin tai koodittoman ympäristön kautta. Tämä ympäristö auttaa yksinkertaistamaan ratkaisujen rakentamisprosessia. Power Platformin avulla ratkaisuja voidaan rakentaa päivissä tai viikoissa kuukausien tai vuosien sijaan. Power Platform koostuu viidestä keskeisestä tuotteesta: Power Apps, Power Automate, Power BI, Power Pages ja Copilot Studio.

Tämä oppitunti kattaa:

- Johdannon generatiiviseen tekoälyyn Power Platformissa
- Johdannon Copilotiin ja sen käyttöön
- Generatiivisen tekoälyn hyödyntämisen sovellusten ja työnkulkujen rakentamisessa Power Platformissa
- Tekoälymallien ymmärtämisen Power Platformissa AI Builderin avulla
- Älykkäiden agenttien rakentamisen Microsoft Copilot Studiolla

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Ymmärtää, miten Copilot toimii Power Platformissa.

- Rakentaa opiskelijoiden tehtävien seurantasovelluksen opetStartup-yrityksellemme.

- Rakentaa laskujen käsittelytyönkulun, joka käyttää tekoälyä laskutietojen poimimiseen.

- Soveltaa parhaita käytäntöjä Create Text with GPT -tekoälymallia käytettäessä.

- Ymmärtää, mikä Microsoft Copilot Studio on ja miten sen avulla rakennetaan älykkäitä agentteja.

Tässä oppitunnissa käytettävät työkalut ja teknologiat ovat:

- **Power Apps**, opiskelijoiden tehtävien seuraamiseen tarkoitetulle sovellukselle, joka tarjoaa vähäkoodisen kehitysympäristön sovellusten rakentamiseen datan seuraamiseksi, hallinnoimiseksi ja vuorovaikutukseen.

- **Dataverse**, opiskelijan tehtävien seurantaan liittyvän datan tallentamiseen, joka tarjoaa vähäkoodisen datapohjan sovelluksen datan tallentamiseen.

- **Power Automate**, laskujen käsittelytyönkululle, jossa on vähäkoodinen kehitysympäristö työnkulkujen rakentamiseen laskujen käsittelyprosessin automatisoimiseksi.

- **AI Builder**, laskujen käsittelyyn käytettävälle tekoälymallille, jossa hyödynnetään valmiita tekoälymalleja laskujen käsittelyyn startup-yrityksellemme.

## Generatiivinen tekoäly Power Platformissa

Vähäkoodikehityksen ja sovellusten parantaminen generatiivisen tekoälyn avulla on keskeinen tavoite Power Platformissa. Tavoitteena on mahdollistaa kaikkien rakentaa tekoälyllä tehostettuja sovelluksia, sivustoja, kojetauluja ja automatisoida prosesseja tekoälyn avulla _ilman että tarvitaan data-analytiikan asiantuntemusta_. Tämä tavoite saavutetaan integroimalla generatiivinen tekoäly vähäkoodikehityskokemukseen Power Platformissa Copilotin ja AI Builderin muodossa.

### Miten tämä toimii?

Copilot on tekoälyavustaja, joka mahdollistaa Power Platform -ratkaisujen rakentamisen kuvailemalla vaatimuksia vuorovaikutteisissa luonnolliskielisissä vaiheissa. Voit esimerkiksi ohjeistaa tekoälyavustajasi kertomaan, mitä kenttiä sovelluksesi käyttää, ja se luo sekä sovelluksen että sen taustalla olevan datamallin, tai voit määrittää, miten työnkulku rakennetaan Power Automatessa.

Voit käyttää Copilot-ohjattuja toiminnallisuuksia sovelluksesi näytöissä, jotta käyttäjät voivat löytää oivalluksia keskustelullisen vuorovaikutuksen kautta.

AI Builder on vähäkoodinen tekoälyominaisuus Power Platformissa, joka mahdollistaa tekoälymallien käytön prosessien automatisointiin ja tulosten ennustamiseen. AI Builderilla voit tuoda tekoälyn sovelluksiisi ja työnkulkuihisi, jotka yhdistyvät dataan Dataversessa tai erilaisissa pilvidatalähteissä kuten SharePoint, OneDrive tai Azure.

Copilot on saatavilla kaikissa Power Platform -tuotteissa: Power Apps, Power Automate, Power BI, Power Pages ja Copilot Studio (entinen Power Virtual Agents). AI Builder on saatavilla Power Appsissa ja Power Automatessa. Tässä oppitunnissa keskitymme Copilotin ja AI Builderin käyttöön Power Appsissa ja Power Automatessa ratkaisun rakentamiseksi opetustartupillemme.

### Copilot Power Appsissa

Power Platformin osana Power Apps tarjoaa vähäkoodisen kehitysympäristön sovellusten rakentamiseen datan seuraamiseen, hallintaan ja vuorovaikutukseen. Se on joukko sovelluskehityspalveluita, joissa on skaalautuva alusta datan tallentamiseen ja kyky yhdistää pilvipalveluihin ja paikalliseen dataan. Power Appsilla voit rakentaa sovelluksia selaimille, tableteille ja puhelimille, ja jakaa ne työkavereillesi. Power Apps helpottaa käyttäjiä sovelluskehityksessä yksinkertaisen käyttöliittymän avulla, jotta jokainen liiketoimintakäyttäjä tai ammattilaiskehittäjä voi rakentaa räätälöityjä sovelluksia. Sovelluskehityskokemusta parantaa myös generatiivinen tekoäly Copilotin kautta.

Copilotin tekoälyavustajaominaisuus Power Appsissa mahdollistaa sen, että voit kuvata, millaista sovellusta tarvitset ja mitä tietoja sovelluksesi tulisi seurata, kerätä tai näyttää. Copilot luo sitten kuvauksesi pohjalta responsiivisen Canvas-sovelluksen. Voit silloin mukauttaa sovellusta tarpeidesi mukaan. AI Copilot luo ja ehdottaa myös Dataverse-taulua, jossa on kentät, joita tarvitset lataamiesi tietojen tallentamiseen, sekä esimerkkitietoja. Tarkastelemme myöhemmin tässä oppitunnissa, mitä Dataverse on ja miten voit käyttää sitä Power Appsissa. Voit sitten mukauttaa taulua tarpeidesi mukaan AI Copilotin avustusominaisuuden avulla keskusteluvaiheissa. Tämä ominaisuus on helposti saatavilla Power Apps -aloitusnäytöltä.

### Copilot Power Automatessa

Power Platformin osana Power Automate mahdollistaa käyttäjien automatisoida työnkulkuja sovellusten ja palveluiden välillä. Se auttaa automatisoimaan toistuvia liiketoimintaprosesseja, kuten viestintää, tietojen keräämistä ja hyväksyntöjä. Sen yksinkertainen käyttöliittymä sallii käyttäjien kaikilla teknisillä taidoilla (aloittelijoista kokeneisiin kehittäjiin) automatisoida työtehtäviä. Työnkulkujen kehityskokemusta parantaa myös Generatiivinen tekoäly Copilotin kautta.

Copilotin tekoälyavustajaominaisuus Power Automatessa mahdollistaa sen, että voit kuvata, millainen työnkulku tarvitset ja mitä toimintoja työnkulun tulisi suorittaa. Copilot generoi kuvauksesi pohjalta työnkulun. Voit sitten mukauttaa työnkulun tarpeidesi mukaan. AI Copilot luo ja ehdottaa myös toimintoja, joita tarvitset automatisoitavan tehtävän suorittamiseksi. Tarkastelemme myöhemmin tässä oppitunnissa, mitä työnkulut ovat ja miten voit käyttää niitä Power Automatessa. Voit sitten mukauttaa toimintoja tarpeidesi mukaan AI Copilotin avustusominaisuuden kautta keskusteluvaiheissa. Tämä ominaisuus on helposti saatavilla Power Automate -aloitusnäytöltä.

## Älykkäiden agenttien rakentaminen Microsoft Copilot Studiolla

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (entinen Power Virtual Agents) on Power Platformin vähäkoodinen jäsen älykkäiden agenttien — keskustelevien copilottien — rakentamiseen, jotka voivat vastata kysymyksiin, suorittaa toimintoja ja automatisoida tehtäviä käyttäjiesi puolesta. Kuten muu Power Platform, nämä agentit rakennetaan visuaalisessa, luonnollisen kielen ensisijaisessa kokemuksessa: kuvailet mitä haluat agentin tekevän, ja Copilot Studio auttaa rakentamaan sen ohjeet, tiedot ja toiminnot.

Opetustartupillemme voisit rakentaa agentin, joka vastaa opiskelijoiden kysymyksiin kursseista, tarkistaa tehtävien määräajat ja jopa lähettää sähköpostia opettajalle — kaikki ilman koodaamista.

Tässä on joitain viimeisimpiä ominaisuuksia, jotka tekevät Copilot Studiosta tehokkaan:

- **Generatiiviset vastaukset tietämyksestäsi**. Sen sijaan, että kirjoittaisit jokaisen keskustelun käsin, voit liittää **tietolähteitä** — julkisia verkkosivuja, SharePointia, OneDrivea, Dataverseta, ladattuja tiedostoja tai yritystietoja liitäntöjen kautta — ja agentti muodostaa näistä perusteltuja vastauksia.

- **Generatiivinen orkestrointi**. Kiinteiden laukaisulauseiden sijaan agentti käyttää tekoälyä ymmärtääkseen pyynnön ja päättääkseen dynaamisesti, mitä tietoa, aiheita ja toimintoja yhdistelee pyynnön täyttämiseksi, mukaan lukien useiden vaiheiden ketjutus.

- **Toiminnot ja liitännät**. Agentit voivat *tehdä* asioita, eivät vain keskustella. Voit antaa agentille toimintoja, joita tukevat yli 1 500 valmiiksi rakennettua Power Platformin liitintä, Power Automate -työnkulut, mukautetut REST API:t, kehotteet tai **Model Context Protocol (MCP)** -palvelimet.

- **Itsenäiset agentit**. Agentit eivät rajoitu vastaamaan keskusteluikkunassa. Voit rakentaa **itseohjautuvia agenteja**, jotka laukaistaan tapahtumista — kuten uusi sähköposti, uusi tietue Dataversessa tai tiedoston lataus — ja toimivat taustalla suorittaakseen tehtävän.

- **Moniagenttinen orkestrointi**. Agentit voivat kutsua toisia agenteja. Copilot Studio -agentti voi antaa tehtävän toiselle agentille, tai sitä voi laajentaa muilla agenteilla, mukaan lukien Microsoft 365 Copilotiin julkaistut agentit ja Microsoft Foundryssä rakennetut agentit.

- **Mallin valinta**. Sisäänrakennettujen mallien lisäksi voit tuoda malleja Microsoft Foundryn mallikatalogista räätälöidäksesi agenttisi päättelyä ja vastauksia.

- **Julkaisu minne tahansa**. Rakentamisen jälkeen agentti voidaan julkaista monille kanaville — Microsoft Teamsiin, Microsoft 365 Copilotiin, verkkosivustolle tai mukautettuun sovellukseen — turvallisuuden, tunnistautumisen ja analytiikan hallinta tapahtuu Power Platformin hallintakokemuksen kautta.

Voit aloittaa ensimmäisen agenttisi rakentamisen osoitteessa [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) ja oppia lisää [Microsoft Copilot Studion dokumentaatiosta](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Tehtävä: Hallitse opiskelijoiden tehtäviä ja laskuja startupillamme Copilotia käyttäen

Startupimme tarjoaa opiskelijoille verkkokursseja. Startup on kasvanut nopeasti ja kamppailee nyt pysyäkseen kurssien kysynnän mukana. Startup on palkannut sinut Power Platform -kehittäjäksi auttamaan heitä rakentamaan vähäkoodisen ratkaisun opiskelijatöiden ja laskujen hallintaan. Ratkaisun tulisi auttaa opiskelijoiden tehtävien seuraamisessa ja hallinnassa sovelluksen avulla sekä automatisoida laskujen käsittely työnkulun kautta. Sinua on pyydetty käyttämään generatiivista tekoälyä ratkaisun kehittämiseen.

Kun aloitat Copilotin käytön, voit hyödyntää [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) -kirjastoa, joka sisältää luettelon kehotteista, joita voit käyttää sovellusten ja työnkulkujen rakentamiseen Copilotin kanssa. Voit myös käyttää kirjaston kehotteita idean saamiseksi siitä, miten kuvailla vaatimuksiasi Copilotille.

### Rakenna opiskelijoiden tehtävien seurantaan tarkoitettu sovellus startupillemme

Startupimme kouluttajat ovat kamppailleet opiskelijoiden tehtävien seuraamisessa. He ovat käyttäneet taulukkoa tehtävien seurantaan, mutta opiskelijoiden määrän kasvaessa tämän hallinta on vaikeutunut. He pyytävät sinua rakentamaan sovelluksen, joka auttaa heitä seuraamaan ja hallitsemaan opiskelijoiden tehtäviä. Sovelluksen tulisi mahdollista lisätä uusia tehtäviä, tarkastella tehtäviä, päivittää tehtäviä ja poistaa tehtäviä. Sovelluksen tulisi myös mahdollistaa kouluttajien ja opiskelijoiden nähdä arvioidut ja arvioimattomat tehtävät.

Rakennat sovelluksen Copilotin avulla Power Appsissa seuraavien vaiheiden mukaisesti:

1. Siirry [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) aloitusnäytölle.

1. Käytä aloitusnäytön tekstikenttää kuvaillaksesi sovelluksen, jonka haluat rakentaa. Esimerkiksi **_Haluan rakentaa sovelluksen opiskelijoiden tehtävien seuraamiseen ja hallintaan_**. Klikkaa **Lähetä**-painiketta lähettääksesi kehotteen tekoälyavustajalle.

![Kuvaile sovellusta, jonka haluat rakentaa](../../../translated_images/fi/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot ehdottaa Dataverse-taulua, jossa on kentät, joita tarvitset seurattavan datan tallentamiseen, sekä esimerkkidata. Voit mukauttaa taulua tarpeidesi mukaan AI Copilotin avustusominaisuuden kautta keskusteluvaiheissa.

   > **Tärkeää**: Dataverse on Power Platformin taustalla oleva datapohja. Se on vähäkoodinen datapohja sovelluksen datan tallentamiseen. Se on täysin hallinnoitu palvelu, joka tallentaa datan turvallisesti Microsoftin pilvessä ja joka on provisioitu Power Platform -ympäristössäsi. Se sisältää sisäänrakennettuja tietohallinnon ominaisuuksia kuten datan luokittelua, datan jäljitettävyyttä, hienojakoista käyttöoikeuksien hallintaa ja muuta. Voit oppia lisää Dataversesta [täältä](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Ehdotetut kentät uudessa taulussasi](../../../translated_images/fi/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Kouluttajat haluavat lähettää sähköpostia opiskelijoille, jotka ovat toimittaneet tehtävänsä, jotta he pysyvät ajan tasalla tehtävien etenemisestä. Voit käyttää Copilotia lisätäksesi uuden kentän tauluun opiskelijoiden sähköpostin tallentamista varten. Esimerkiksi voit käyttää seuraavaa kehotetta uuden kentän lisäämiseen: **_Haluan lisätä sarakkeen opiskelijan sähköpostin tallentamiseksi_**. Klikkaa **Lähetä**-painiketta lähettääksesi kehotteen tekoälyavustajalle.

![Uuden kentän lisääminen](../../../translated_images/fi/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot luo uuden kentän, jonka voit mukauttaa tarpeidesi mukaan.


1. Kun taulukko on valmis, napsauta **Luo sovellus** -painiketta luodaksesi sovelluksen.

1. AI Copilot luo kuvaustasi perustuvan responsiivisen Canvas-sovelluksen. Voit sitten mukauttaa sovellusta tarpeittesi mukaan.

1. Opettajille, jotka haluavat lähettää sähköposteja opiskelijoille, voit käyttää Copilotia lisätäksesi sovellukseen uuden näytön. Esimerkiksi voit käyttää seuraavaa kehotetta lisätäksesi sovellukseen uuden näytön: **_Haluan lisätä näytön, jolla voi lähettää sähköposteja opiskelijoille_**. Napsauta **Lähetä**-painiketta lähettääksesi kehotteen AI Copilotille.

![Uuden näytön lisääminen kehotteen avulla](../../../translated_images/fi/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot luo uuden näytön, ja voit sitten mukauttaa näytön tarpeidesi mukaan.

1. Kun sovellus on valmis, napsauta **Tallenna**-painiketta tallentaaksesi sovelluksen.

1. Jaa sovellus opettajille napsauttamalla **Jaa**-painiketta ja sen jälkeen uudelleen **Jaa**-painiketta. Voit sitten jakaa sovelluksen opettajille syöttämällä heidän sähköpostiosoitteensa.

> **Kotitehtäväsi**: Juuri rakentamasi sovellus on hyvä alku, mutta sitä voidaan parantaa. Sähköpostiominaisuudella opettajat voivat lähettää sähköpostit opiskelijoille vain manuaalisesti kirjoittamalla heidän sähköpostinsa. Voisitko käyttää Copilotia rakentaaksesi automaation, joka mahdollistaa opettajille opiskelijoiden sähköpostien automaattisen lähettämisen, kun he palauttavat tehtävänsä? Vihjeesi on, että oikealla kehotteella voit käyttää Copilotia Power Automatessa tämän rakentamiseen.

### Rakenna Laskutustietotaulukko Startupillemme

Startupimme taloustiimi on kamppaillut laskujen seuraamisen kanssa. He ovat käyttäneet taulukkolaskentaohjelmaa laskujen seurantaan, mutta sen hallinnasta on tullut vaikeaa laskujen määrän kasvaessa. He ovat pyytäneet sinua rakentamaan taulukon, joka auttaa heitä tallentamaan, seuraamaan ja hallitsemaan vastaanottamien laskujen tietoja. Taulukkoa käytetään automaation rakentamiseen, joka poimii kaikki laskutiedot ja tallentaa ne taulukkoon. Taulukon tulisi myös mahdollistaa taloustiimin tarkastella maksettuja ja maksamattomia laskuja.

Power Platformissa on alusta nimeltä Dataverse, joka mahdollistaa sovellustesi ja ratkaisujesi tietojen tallentamisen. Dataverse tarjoaa matalan koodin tietovaraston sovelluksen tiedoille. Se on täysin hallinnoitu palvelu, joka tallentaa tiedot turvallisesti Microsoft-pilveen ja on provisionoitu Power Platform -ympäristössäsi. Siinä on sisäänrakennettuja tietohallinnan ominaisuuksia, kuten tietojen luokittelu, tietojen jäljitettävyys, hienojakoinen käyttövalvonta ja paljon muuta. Voit oppia lisää [Dataversestä täältä](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Miksi meidän pitäisi käyttää Dataverseä startupissamme? Dataversen standardi- ja mukautetut taulukot tarjoavat turvallisen ja pilvipohjaisen varastointivaihtoehdon tietoillesi. Taulukot antavat sinun tallentaa erilaisia tietotyyppejä, samalla tavalla kuin käyttäisit useita työkirjan arkkeja Excelissä. Voit käyttää taulukoita tallentamaan tietoja, jotka ovat yrityksesi tai liiketoimintasi tarpeiden mukaisia. Joitakin hyötyjä, joita startupimme saa käyttäessään Dataverseä, ovat muun muassa:

- **Helppo hallita**: Sekä metatiedot että data tallennetaan pilveen, joten sinun ei tarvitse huolehtia siitä, miten ne tallennetaan tai hallitaan. Voit keskittyä sovellustesi ja ratkaisujesi rakentamiseen.

- **Turvallinen**: Dataverse tarjoaa turvallisen ja pilvipohjaisen tallennusvaihtoehdon tiedoillesi. Voit hallita, kuka pääsee käsiksi taulukkojasi ja miten he voivat niitä käyttää roolipohjaisen turvallisuuden avulla.

- **Rikkaita metatietoja**: Tietotyyppejä ja suhteita käytetään suoraan Power Appsissa

- **Logiikka ja validointi**: Voit käyttää liikeregeliä, laskettuja kenttiä ja validointisääntöjä liikelogian vahvistamiseksi ja tietojen tarkkuuden ylläpitämiseksi.

Nyt kun tiedät, mitä Dataverse on ja miksi sitä tulisi käyttää, katsotaan miten voit käyttää Copilotia luodaksesi taulukon Dataverseen taloustiimimme tarpeiden täyttämiseksi.

> **Huom:** Käytät tätä taulukkoa seuraavassa osiossa rakentaaksesi automaation, joka poimii kaikki laskutiedot ja tallentaa ne taulukkoon.

Dataversessa taulukon luomiseksi Copilotin avulla, seuraa alla olevia ohjeita:

1. Siirry [Power Appsin](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) kotinäyttöön.

2. Vasemmanpuoleisessa navigointipalkissa valitse **Taulukot** ja napsauta sitten **Kuvaile uutta taulukkoa**.

![Valitse uusi taulukko](../../../translated_images/fi/describe-new-table.0792373eb757281e.webp)

1. **Kuvaile uutta taulukkoa** -näytöllä käytä tekstikenttää kuvaamaan taulukko, jonka haluat luoda. Esimerkiksi **_Haluan luoda taulukon laskutietojen tallentamiseen_**. Napsauta **Lähetä**-painiketta lähettääksesi kehotteen AI Copilotille.

![Kuvaile taulukko](../../../translated_images/fi/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot ehdottaa Dataverse-taulukkoa niillä kentillä, joita tarvitset tallentaaksesi seurantaan haluamasi tiedot, sekä esimerkkitietoja. Sitten voit mukauttaa taulukkoa tarpeidesi mukaan AI Copilot -assistentin kautta keskustelumuotoisin askelin.

![Ehdotettu Dataverse-taulukko](../../../translated_images/fi/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Taloustiimi haluaa lähettää sähköpostin toimittajalle päivittääkseen heidät laskun nykytilasta. Voit käyttää Copilotia lisätäksesi taulukkoon uuden kentän toimittajan sähköpostin tallentamiseksi. Esimerkiksi voit käyttää seuraavaa kehotetta lisätäksesi taulukkoon uuden kentän: **_Haluan lisätä sarakkeen toimittajan sähköpostin tallentamista varten_**. Napsauta **Lähetä**-painiketta lähettääksesi kehotteen AI Copilotille.

1. AI Copilot luo uuden kentän, ja voit sitten mukauttaa kenttää tarpeidesi mukaan.

1. Kun taulukko on valmis, napsauta **Luo**-painiketta luodaksesi taulukon.

## AI-mallit Power Platformissa AI Builderin kanssa

AI Builder on matalan koodin tekoälyominaisuus Power Platformissa, joka mahdollistaa tekoälymallien käytön prosessien automatisointiin ja tulosten ennustamiseen. AI Builderin avulla voit lisätä tekoälyä sovelluksiisi ja automaatioihisi, jotka yhdistyvät tietoihisi Dataverse-palvelussa tai erilaisissa pilvitietolähteissä, kuten SharePoint, OneDrive tai Azure.

## Ennalta rakennettuja AI-malleja vs mukautettuja AI-malleja

AI Builder tarjoaa kahta tyyppiä tekoälymalleja: ennalta rakennettuja AI-malleja ja mukautettuja AI-malleja. Ennalta rakennetut mallit ovat käyttövalmiita, Microsoftin kouluttamia malleja, jotka ovat saatavilla Power Platformissa. Näiden avulla voit lisätä älykkyyttä sovelluksiisi ja automaatioihisi ilman, että sinun tarvitsee kerätä dataa ja rakentaa, kouluttaa ja julkaista omia mallejasi. Voit käyttää näitä malleja prosessien automatisointiin ja tulosten ennustamiseen.

Joitakin Power Platformissa saatavilla olevia ennalta rakennettuja AI-malleja ovat:

- **Avainsanaprässi**: Tämä malli poimii keskeiset ilmaisut tekstistä.
- **Kielentunnistus**: Tämä malli tunnistaa tekstin kielen.
- **Tunneanalyysi**: Tämä malli tunnistaa positiivisen, negatiivisen, neutraalin tai sekoitetun tunteen tekstistä.
- **Käyntikortin lukija**: Tämä malli poimii tietoja käyntikorteista.
- **Tekstin tunnistus**: Tämä malli poimii tekstiä kuvista.
- **Kohteen tunnistus**: Tämä malli tunnistaa ja poimii kohteita kuvista.
- **Asiakirjojen käsittely**: Tämä malli poimii tietoja lomakkeista.
- **Laskujen käsittely**: Tämä malli poimii tietoja laskuista.

Mukautettujen AI-mallien avulla voit tuoda oman mallisi AI Builderiin, jolloin se toimii kuten mikä tahansa AI Builderin mukautettu malli, ja voit kouluttaa mallia omilla tiedoillasi. Voit käyttää näitä malleja automatisoimaan prosesseja ja ennustamaan tuloksia sekä Power Appsissa että Power Automatessa. Oman mallin käytössä on rajoituksia, joista voit lukea lisää [täällä](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builderin mallit](../../../translated_images/fi/ai-builder-models.8069423b84cfc47f.webp)

## Tehtävä #2 - Rakenna Laskujen Käsittelyvirta Startupillemme

Taloustiimi on kamppaillut laskujen käsittelyn kanssa. He ovat käyttäneet taulukkolaskentaa laskujen seurantaan, mutta sen hallinnasta on tullut vaikeaa laskujen määrän kasvaessa. He ovat pyytäneet sinua rakentamaan työnkulun, joka auttaa heitä käsittelemään laskuja käyttämällä tekoälyä. Työnkulun tulisi poimia tiedot laskuista ja tallentaa tiedot Dataverse-taulukkoon. Työnkulun tulisi myös mahdollistaa sähköpostin lähettäminen taloustiimille poimituilla tiedoilla.

Nyt kun tiedät mitä AI Builder on ja miksi sitä tulisi käyttää, katsotaan miten voit käyttää aiemmin esiteltyä Laskujen Käsittely -AI-mallia AI Builderissa rakentaaksesi työnkulun, joka auttaa taloustiimiä laskujen käsittelyssä.

Rakentaaksesi työnkulun, joka auttaa taloustiimiä laskujen käsittelyssä käyttäen Laskujen Käsittely AI-mallia AI Builderissa, seuraa alla olevia ohjeita:

1. Siirry [Power Automaten](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) kotinäyttöön.

2. Käytä tekstikenttää kotinäytöllä kuvaamaan työnkulkua, jonka haluat rakentaa. Esimerkiksi **_Käsittele lasku, kun se saapuu sähköpostilaatikkooni_**. Napsauta **Lähetä**-painiketta lähettääksesi kehotteen AI Copilotille.

   ![Copilot power automate](../../../translated_images/fi/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot ehdottaa toiminnot, joita tarvitset automatisoidaksesi haluamasi tehtävän. Voit napsauttaa **Seuraava**-painiketta edetäksesi seuraaviin vaiheisiin.

4. Seuraavassa vaiheessa Power Automate pyytää sinua määrittämään työnkululle tarvittavat yhteydet. Kun olet valmis, napsauta **Luo virta** -painiketta luodaksesi työnkulun.

5. AI Copilot luo työnkulun, ja voit sitten mukauttaa työnkulkua tarpeidesi mukaan.

6. Päivitä työnkulun laukaiseva ehto ja aseta **Kansio** siihen kansioon, johon laskut tallennetaan. Esimerkiksi voit asettaa kansion **Saapuneet-kansio**. Napsauta **Näytä lisävaihtoehdot** ja aseta **Vain liitteelliset** kohtaan **Kyllä**. Tämä varmistaa, että työnkulku käynnistyy vain, kun kansioon tulee sähköposti liitteellä.

7. Poista työnkulusta seuraavat toiminnot: **HTML tekstiksi**, **Rakentaa**, **Rakentaa 2**, **Rakentaa 3** ja **Rakentaa 4**, sillä et tule käyttämään niitä.

8. Poista työnkulusta **Ehto**-toiminto, koska et tule käyttämään sitä. Sen tulisi näyttää seuraavalta kuvakaappaukselta:

   ![power automate, poista toiminnot](../../../translated_images/fi/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Napsauta **Lisää toiminto** -painiketta ja etsi **Dataverse**. Valitse **Lisää uusi rivi** -toiminto.

10. Toiminnossa **Poimi tietoja laskuista** päivitä **Laskutiedosto** osoittamaan sähköpostin **Liitteen sisältöön**. Tämä varmistaa, että työnkulku poimii tiedot laskuliitteestä.

11. Valitse aiemmin luomasi **Taulukko**. Esimerkiksi voit valita **Laskutustiedot** -taulukon. Valitse dynaamiset sisällöt edellisestä toiminnosta täyttääksesi seuraavat kentät:

    - ID
    - Summa
    - Päivämäärä
    - Nimi
    - Tila - Aseta **Tila** arvoon **Odottaa**.
    - Toimittajan sähköposti - Käytä **Lähettäjä**-dynaamista sisältöä laukaisevasta toiminnosta **Kun uusi sähköposti saapuu**.

    ![power automate lisää rivi](../../../translated_images/fi/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Kun työnkulku on valmis, napsauta **Tallenna**-painiketta tallentaaksesi työnkulun. Voit sitten testata työnkulkua lähettämällä laskun sisältävän sähköpostin kansioon, jonka määritit laukaisimeksi.

> **Kotitehtäväsi**: Rakentamasi työnkulku on hyvä alku, nyt sinun tulee miettiä, miten voisit rakentaa automaation, joka mahdollistaa taloustiimimme lähettää toimittajalle sähköpostin päivittääkseen heidät laskun nykytilasta. Vihjeesi: työnkulun tulee käynnistyä, kun laskun tila muuttuu.

## Käytä Tekstin Generointia AI-mallia Power Automatessa

Luo teksti GPT AI -malli AI Builderissa mahdollistaa tekstin generoinnin kehotteen perusteella ja toimii Microsoft Azure OpenAI -palvelun avulla. Tämän ominaisuuden avulla voit sisällyttää GPT-tekniikkaa sovelluksiisi ja työnkulkuihisi rakentaaksesi erilaisia automatisoituja työnkulkuja ja älykkäitä sovelluksia.

GPT-mallit käyvät läpi laajat koulutusvaiheet valtavilla datamäärillä, minkä ansiosta ne pystyvät tuottamaan tekstiä, joka muistuttaa ihmiskieltä kun ne saavat kehotteen. Kun ne integroidaan työnkulkuihin, tekoälymallit kuten GPT voivat auttaa sujuvoittamaan ja automatisoimaan useita tehtäviä.

Voit esimerkiksi rakentaa työnkulkuja, jotka generoi automaattisesti tekstiä erilaisiin käyttötarkoituksiin, kuten sähköpostiluonnokset, tuotekuvaukset ja paljon muuta. Voit myös käyttää mallia tekstin tuottamiseen erilaisissa sovelluksissa, kuten chatbotit ja asiakaspalvelusovellukset, jotka auttavat asiakaspalvelijoita vastaamaan tehokkaasti ja nopeasti asiakkaiden kyselyihin.

![luo kehotus](../../../translated_images/fi/create-prompt-gpt.69d429300c2e870a.webp)


Tutustu, miten tätä tekoälymallia käytetään Power Automatessa, käy läpi [Lisää älykkyyttä AI Builderin ja GPT:n avulla](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) -moduuli.

## Hienoa työtä! Jatka oppimista

Tämän oppitunnin jälkeen tutustu [Generatiivisen tekoälyn oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn tietämyksesi kehittämistä!

Haluatko räätälöidä ja saada enemmän irti Copilotista? Tutustu [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) – yhteisön kokoamaan ohjeiden, agenttien, taitojen ja määritysten kokoelmaan, joka auttaa sinua hyödyntämään GitHub Copilotia parhaalla tavalla.

Suuntaa oppitunnille 11, jossa tarkastelemme, miten [integroimme Generatiivisen tekoälyn Funktioiden kutsumisen kanssa](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->