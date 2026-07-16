# Generatiivisella tekoälyllä toimivien chat-sovellusten rakentaminen

[![Generatiivisella tekoälyllä toimivien chat-sovellusten rakentaminen](../../../translated_images/fi/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Nyt kun olemme nähneet, miten voimme rakentaa tekstinluontisovelluksia, tarkastellaan chat-sovelluksia.

Chat-sovellukset ovat tulleet osaksi jokapäiväistä elämäämme tarjoten muutakin kuin vain tapa keskustella rennosti. Ne ovat keskeisiä asiakaspalvelussa, teknisessä tuessa ja jopa kehittyneissä neuvontajärjestelmissä. On todennäköistä, että olet saanut apua chat-sovelluksesta äskettäin. Kun yhdistämme näihin alustoihin kehittyneempiä teknologioita, kuten generatiivista tekoälyä, monimutkaisuus kasvaa ja samalla myös haasteet.

Joitakin kysymyksiä, joihin meidän tulee vastata, ovat:

- **Sovelluksen rakentaminen**. Miten rakennamme tehokkaasti ja sulavasti integroimme nämä tekoälyllä toimivat sovellukset tiettyjä käyttötarkoituksia varten?
- **Valvonta**. Kun sovellukset on otettu käyttöön, miten voimme valvoa ja varmistaa, että ne toimivat parhaalla mahdollisella tavalla sekä toiminnallisuuden että [vastuullisen tekoälyn kuuden periaatteen](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) noudattamisen suhteen?

Kun siirrymme yhä enemmän automaation ja saumattomien ihmisen ja koneen vuorovaikutusten aikakauteen, on olennaista ymmärtää, miten generatiivinen tekoäly muuttaa chat-sovellusten laajuutta, syvyyttä ja mukautuvuutta. Tämä oppitunti tutkii arkkitehtuurin osa-alueita, jotka tukevat näitä monimutkaisia järjestelmiä, syventyy menetelmiin, joilla niitä hienosäädetään tiettyjä tehtäviä varten, sekä arvioi mittareita ja näkökulmia, jotka liittyvät vastuullisen tekoälyn käyttöönottoon.

## Johdanto

Tämä oppitunti käsittelee:

- Menetelmiä tehokkaaseen chat-sovellusten rakentamiseen ja integrointiin.
- Kuinka sovelluksia voidaan räätälöidä ja hienosäätää.
- Strategioita ja näkökulmia chat-sovellusten tehokkaaseen valvontaan.

## Oppimistavoitteet

Oppitunnin lopuksi osaat:

- Kuvailla tekijöitä chat-sovellusten rakentamisessa ja integroinnissa olemassa oleviin järjestelmiin.
- Räätälöidä chat-sovelluksia tiettyjä käyttötapauksia varten.
- Tunnistaa keskeiset mittarit ja näkökulmat, joilla valvotaan ja ylläpidetään tekoälyllä toimivien chat-sovellusten laatua.
- Varmistaa, että chat-sovellukset hyödyntävät tekoälyä vastuullisesti.

## Generatiivisen tekoälyn integrointi chat-sovelluksiin

Chat-sovellusten kohottaminen generatiivisella tekoälyllä ei tarkoita pelkästään älykkäämmäksi tekemistä, vaan myös niiden arkkitehtuurin, suorituskyvyn ja käyttöliittymän optimoimista tarjotakseen laadukkaan käyttökokemuksen. Tämä edellyttää arkkitehtuurin perusteiden, API-integraatioiden ja käyttöliittymään liittyvien näkökulmien tutkimista. Tämä osio tarjoaa sinulle kokonaisvaltaisen tiekartan monimutkaisten järjestelmien hallintaan, olitpa sitten liittämässä niitä olemassa oleviin järjestelmiin tai rakentamassa niitä itsenäisiksi alustoiksi.

Osion lopussa sinulla on asiantuntemus rakentaa ja ottaa chat-sovellukset tehokkaasti käyttöön.

### Chatbot vai chat-sovellus?

Ennen kuin sukellamme chat-sovellusten rakentamiseen, vertaillaan 'chatbotteja' ja 'tekoälyllä toimivia chat-sovelluksia', joilla on erilaiset roolit ja toiminnot. Chatbotin päätehtävä on automatisoida tiettyjä keskustelutehtäviä, kuten usein kysyttyihin kysymyksiin vastaamista tai paketin seurantaa. Se pohjautuu tyypillisesti sääntöpohjaiseen logiikkaan tai monimutkaisiin tekoälyalgoritmeihin. Sen sijaan tekoälyllä toimiva chat-sovellus on laajempi ympäristö, joka mahdollistaa erilaiset digitaaliset viestintämuodot, kuten tekstin, äänen ja videon välityksellä tapahtuvan keskustelun ihmisten välillä. Sen määrittävä ominaisuus on generatiivisen tekoälymallin integrointi, joka simuloi vivahteikkaita, ihmismäisiä keskusteluja luomalla vastauksia monipuolisen syötteen ja kontekstuaalisten vihjeiden perusteella. Generatiivisella tekoälyllä toimiva chat-sovellus voi käydä avoimia keskusteluja, sopeutua muuttuviin keskustelukonteksteihin ja jopa tuottaa luovia tai monimutkaisia dialogeja.

Alla oleva taulukko hahmottaa keskeiset erot ja samankaltaisuudet auttaakseen meitä ymmärtämään niiden ainutlaatuisia rooleja digitaalisessa viestinnässä.

| Chatbot                               | Generatiivisella tekoälyllä toimiva chat-sovellus      |
| ------------------------------------- | --------------------------------------                  |
| Tehtäväkeskeinen ja sääntöpohjainen  | Kontekstitietoinen                                      |
| Usein osana suurempia järjestelmiä    | Voi sisältää yhden tai useampia chatboteja              |
| Rajoittunut ohjelmoituihin toimintoihin | Sisältää generatiivisia tekoälymalleja                  |
| Erikoistuneet ja rakenteelliset vuorovaikutukset | Pystyy avoimen alueen keskusteluihin                      |

### Esivalmistettujen toimintojen hyödyntäminen SDK:illa ja API:lla

Chat-sovellusta rakentaessa hyvä ensimmäinen askel on arvioida, mitä valmiita ratkaisuja on jo olemassa. SDK:iden ja API:en käyttö chat-sovellusten rakentamisessa on hyödyllinen strategia monista syistä. Integroimalla hyvin dokumentoituja SDK:ita ja API:a asemoit sovelluksesi strategisesti kohti pitkäaikaista menestystä ottaen huomioon skaalautuvuuden ja ylläpidon näkökulmat.

- **Nopeuttaa kehitysprosessia ja vähentää ylimääräistä työtä**: Luottaessa valmiisiin toimintoihin sen sijaan, että rakentaisit ne itse kalliisti, voit keskittyä muihin sovelluksesi osa-alueisiin, jotka saattavat olla tärkeämpiä, kuten liiketoimintalogiikkaan.
- **Parempi suorituskyky**: Rakentaessasi toiminnallisuutta alusta alkaen kysyt lopulta itseltäsi "Miten tämä skaalautuu? Pystyykö tämä sovellus käsittelemään äkillisen käyttäjämäärän kasvun?" Hyvin ylläpidetyissä SDK:ssa ja API:ssa on usein sisäänrakennettuja ratkaisuja näihin haasteisiin.
- **Helpompi ylläpito**: Päivitysten ja parannusten hallinta on helpompaa, sillä useimmat API:t ja SDK:t vaativat vain kirjaston päivityksen, kun uudempi versio julkaistaan.
- **Pääsy huipputeknologiaan**: Mallien, joita on hienosäädetty ja koulutettu laajoilla datasetillä, hyödyntäminen tarjoaa sovelluksellesi luonnollisen kielen kyvykkyyksiä.

SDK:n tai API:n toiminnallisuuksiin pääsy edellyttää yleensä luvan saamista palvelun käyttöön, yleensä uniikin avaimen tai todennustunnuksen avulla. Tutustumme tähän käyttämällä OpenAI Python Libraryä ja katsomme, miltä tämä näyttää. Voit myös kokeilla sitä itse seuraavassa [OpenAI:n muistikirjassa](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) tai [Azure OpenAI -palveluiden muistikirjassa](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) tälle oppitunnille.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-4o-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Yllä oleva esimerkki käyttää GPT-4o mini -mallia Responses API:n kanssa kehotteen täydentämiseen, mutta huomaa, että API-avain asetetaan sitä ennen. Saisit virheen, jos et asettaisi avainta.

## Käyttäjäkokemus (UX)

Yleiset UX-periaatteet pätevät chat-sovelluksiin, mutta tässä on joitakin lisähuomioita, jotka ovat erityisen tärkeitä koneoppimiskomponenttien vuoksi.

- **Epätarkkuuden käsittelyn mekanismi**: Generatiiviset tekoälymallit tuottavat toisinaan epäselviä vastauksia. Toiminto, joka antaa käyttäjille mahdollisuuden pyytää tarkennusta, voi olla hyödyllinen tällaisissa tilanteissa.
- **Kontekstin säilyttäminen**: Kehittyneemmillä generatiivisilla malleilla on kyky muistaa keskustelun konteksti, mikä voi olla olennainen hyödyke käyttäjäkokemukseen. Käyttäjien mahdollisuus hallita ja säädellä kontekstia parantaa käyttökokemusta mutta tuo mukanaan riskin arkaluontoisten tietojen säilyttämisestä. Mieti, kuinka kauan tietoa säilytetään, esimerkiksi asettamalla säilytyskäytäntö, joka tasapainottaa kontekstin tarpeen ja yksityisyyden välillä.
- **Personointi**: Tekoälymallit tarjoavat yksilöllisen kokemuksen oppimalla ja sopeutumalla. Käyttäjäkokemuksen räätälöinti esimerkiksi käyttäjäprofiilien kautta saa käyttäjän tuntemaan itsensä ymmärretyksi ja auttaa löytämään tiettyjä vastauksia tehokkaammin, luoden sujuvamman ja tyydyttävämmän vuorovaikutuksen.

Yksi personoinnin esimerkki on OpenAI:n ChatGPT:n "Mukautettu ohjeistus" -asetukset. Ne antavat sinun antaa tietoja itsestäsi, jotka voivat olla tärkeitä kehotteiden kannalta. Tässä on esimerkki mukautetusta ohjeesta.

![Mukautetut ohjeistukset ChatGPT:ssä](../../../translated_images/fi/custom-instructions.b96f59aa69356fcf.webp)

Tämä "profiili" ohjaa ChatGPT:tä laatimaan oppituntisuunnitelman linkitetyistä listoista. Huomaa, että ChatGPT ottaa huomioon käyttäjän kokemuksen ja tarjoaa syvällisemmän oppituntisuunnitelman.

![ChatGPT-kehotteesta oppituntisuunnitelmaa linkitetyistä listoista](../../../translated_images/fi/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsoftin järjestelmäviestikehys suurille kielimalleille

[Microsoft on julkaissut ohjeistusta](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) tehokkaiden järjestelmäviestien kirjoittamiseksi LLM:ien vastausten tuottamiseen neljällä alueella:

1. Mallin kohderyhmän, kyvykkyyksien ja rajoitusten määrittely.
2. Mallin tulosteen formaatin määrittely.
3. Erityisten esimerkkien tarjoaminen, jotka osoittavat mallin tarkoitetun toiminnan.
4. Lisäkäyttäytymisen suojakeinojen tarjoaminen.

### Esteettömyys

Olipa käyttäjällä näkö-, kuulo-, motorisia tai kognitiivisia rajoitteita, hyvin suunnitellun chat-sovelluksen tulee olla kaikkien käytettävissä. Seuraava lista kattaa erityisiä ominaisuuksia, jotka parantavat esteettömyyttä eri käyttäjärajoitteissa.

- **Näkövammaiset**: Suurikontrastiset teemat ja muokattavat tekstit, ruudunlukuohjelmien yhteensopivuus.
- **Kuulovammaiset**: Teksti puheeksi- ja puhe tekstiksi -toiminnot, visuaaliset merkit äänitiedotteille.
- **Motorisesti rajoittuneet**: Näppäimistöohjaus, äänikomennot.
- **Kognitiivisesti rajoittuneet**: Yksinkertaistetut kielivaihtoehdot.

## Räätälöinti ja hienosäätö toimialakohtaisille kielimalleille

Kuvittele chat-sovellus, joka ymmärtää yrityksesi sanaston ja ennakoi sen käyttäjäkunnan yleisimmät kysymykset. On muutamia lähestymistapoja, jotka ovat mainitsemisen arvoisia:

- **DSL-mallien hyödyntäminen**. DSL tarkoittaa toimialakohtaista kieltä (domain specific language). Voit hyödyntää ns. DSL-mallia, joka on koulutettu tietylle toimialalle ymmärtämään sen käsitteitä ja tilanteita.
- **Hienosäätö**. Hienosäätö on prosessi, jossa mallia koulutetaan edelleen erityisellä aineistolla.

## Räätälöinti: DSL:n käyttö

Toimialakohtaisten kielimallien (DSL-mallit) hyödyntäminen voi parantaa käyttäjien sitoutumista tarjoamalla erikoistuneita ja tilanteeseen sopivia vuorovaikutuksia. Malli on koulutettu tai hienosäädetty ymmärtämään ja tuottamaan tekstiä tietystä alasta, teollisuudesta tai aiheesta. DSL-mallien käyttömahdollisuudet vaihtelevat kokonaan uuden mallin kouluttamisesta valmiiden mallien käyttöön SDK:iden ja API:en kautta. Toinen vaihtoehto on hienosäätö, jossa olemassa oleva esikoulutettu malli mukautetaan tietylle alalle.

## Räätälöinti: Hienosäätö

Hienosäätö on usein harkittava, kun esikoulutettu malli ei riitä erikoistuneella alalla tai tietyssä tehtävässä.

Esimerkiksi lääketieteelliset kyselyt ovat monimutkaisia ja vaativat paljon kontekstia. Kun lääkäri tekee diagnoosin, se perustuu moniin tekijöihin, kuten elämäntapaan tai olemassa oleviin sairauksiin, ja saattaa turvautua myös viimeisimpiin lääketieteellisiin julkaisuihin diagnoosin vahvistamiseksi. Tällaisissa nyansoiduissa tapauksissa yleiskäyttöinen tekoälyllä toimiva chat-sovellus ei voi olla luotettava lähde.

### Tilanne: lääketieteellinen sovellus

Kuvittele chat-sovellus, joka auttaa lääketieteen ammattilaisia tarjoamalla nopeasti hoito-ohjeita, lääkeaineiden yhteisvaikutuksia tai tuoreimpia tutkimustuloksia.

Yleiskäyttöinen malli voi olla riittävä peruskysymyksiin vastaamisessa tai yleisterveysohjeiden antamisessa, mutta se saattaa kohdata vaikeuksia seuraavissa:

- **Erittäin spesifit tai monimutkaiset tapaukset**. Esimerkiksi neurologi saattaa kysyä sovellukselta: "Mitkä ovat nykyiset parhaat käytännöt lääkeresistentin epilepsian hoitamiseksi lapsipotilailla?"
- **Viimeisimpien edistysaskeleiden puute**. Yleiskäyttöinen malli voi kokea vaikeuksia tarjota ajantasaista vastausta, joka sisältää uusimmat neurologian ja farmakologian edistysaskeleet.

Tällaisissa tapauksissa mallin hienosäätö erikoistuneella lääketieteellisellä aineistolla voi merkittävästi parantaa sen kykyä käsitellä näitä monimutkaisia lääketieteellisiä kysymyksiä tarkemmin ja luotettavammin. Tämä edellyttää pääsyä suureen ja asiaankuuluvaan aineistoon, joka edustaa toimialakohtaisia haasteita ja kysymyksiä.

## Korkealaatuisen tekoälypohjaisen chat-kokemuksen näkökulmat

Tässä osiossa kuvataan "korkealaatuisten" chat-sovellusten kriteerejä, jotka sisältävät käyttökelpoisten mittareiden keruun ja vastuullista tekoälyteknologian hyödyntämistä koskevan viitekehyksen noudattamisen.

### Keskeiset mittarit

Sovelluksen korkean suorituskyvyn ylläpitämiseksi on olennaista seurata keskeisiä mittareita ja näkökulmia. Nämä mittaukset eivät vain takaa sovelluksen toiminnallisuutta, vaan arvioivat myös tekoälymallin ja käyttäjäkokemuksen laatua. Alla on luettelo, joka kattaa perustason, tekoäly- ja käyttäjäkokemusmittarit huomioitavaksi.

| Mittari                       | Määritelmä                                                                                                            | Chat-kehittäjän näkökulma                                              |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Käyttöaika**                 | Mittaa ajan, jonka sovellus on toiminnassa ja käyttäjien saatavilla.                                                   | Kuinka minimoit käyttökatkokset?                                       |
| **Vastausaika**               | Aika, jonka sovellus käyttää vastatakseen käyttäjän kyselyyn.                                                         | Kuinka optimoit kyselyjen käsittelyn lyhentääksesi vastausaikaa?       |
| **Täsmällisyys**              | Todellisten positiivisten ennusteiden suhde kaikkiin positiivisiin ennusteisiin.                                      | Kuinka validoit mallisi täsmällisyyden?                                |
| **Herkkyys (Recall)**         | Todellisten positiivisten ennusteiden suhde todelliseen positiivisten määrään.                                        | Kuinka mittaat ja parannat herkkyyttä?                                |
| **F1-pisteet**                | Täsmällisyyden ja herkkyyden harmoninen keskiarvo, joka tasapainottaa näiden välisen vaihtokaupan.                     | Mikä on tavoittelemasi F1-piste? Kuinka tasapainotat täsmällisyyden ja herkkyyden?  |
| **Hämmennys**                | Mittaa, miten hyvin mallin ennustama todennäköisyysjakauma vastaa datan todellista jakaumaa.                            | Kuinka minimoit hämmennyksen?                                         |
| **Käyttäjätyytyväisyysmittarit** | Mittaavat käyttäjän kokemaa sovelluksesta. Usein kerätään kyselyiden avulla.                                            | Kuinka usein keräät käyttäjäpalautetta? Kuinka sopeudut sen perusteella? |
| **Virheiden määrä**           | Mallin virheiden ymmärryksessä tai tuotoksessa määrä.                                                                 | Mitä strategioita sinulla on virheiden vähentämiseksi?                  |
| **Uudelleenkoulutusjaksot**  | Kuinka usein mallia päivitetään ottamaan huomioon uutta dataa ja havaintoja.                                          | Kuinka usein uudelleenkoulutat mallin? Mikä käynnistää uudelleenkoulutusjakson?  |

| **Poikkeavuuksien tunnistaminen** | Työkalut ja tekniikat poikkeuksellisten kuvioiden tunnistamiseen, jotka eivät vastaa odotettua käyttäytymistä. | Miten reagoit poikkeavuuksiin?                                          |

### Vastuunalaisen tekoälyn käytäntöjen toteuttaminen chat-sovelluksissa

Microsoftin lähestymistapa vastuulliseen tekoälyyn on tunnistanut kuusi periaatetta, jotka tulisi ohjata tekoälyn kehitystä ja käyttöä. Alla ovat periaatteet, niiden määritelmät ja asioita, joita chat-kehittäjän tulisi harkita ja miksi niihin tulisi suhtautua vakavasti.

| Periaatteet           | Microsoftin määritelmä                               | Huomiot chat-kehittäjälle                                          | Miksi se on tärkeää                                                                   |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Oikeudenmukaisuus       | Tekoälyjärjestelmien tulisi kohdella kaikkia reilusti. | Varmista, ettei chat-sovellus syrji käyttäjätietojen perusteella.   | Rakentaa luottamusta ja osallisuutta käyttäjien keskuudessa; välttää oikeudellisia seuraamuksia. |
| Luotettavuus ja turvallisuus | Tekoälyjärjestelmien tulisi toimia luotettavasti ja turvallisesti. | Toteuta testaus ja turvatoimet virheiden ja riskien minimoimiseksi.  | Varmistaa käyttäjien tyytyväisyyden ja estää mahdolliset vahingot.                     |
| Yksityisyys ja tietoturva | Tekoälyjärjestelmien tulisi olla turvallisia ja kunnioittaa yksityisyyttä. | Toteuta vahva salaaminen ja tietosuojatoimet.                        | Suojaa arkaluonteiset käyttäjätiedot ja täyttää tietosuojalainsäädännön vaatimukset.   |
| Osallisuus             | Tekoälyjärjestelmien tulisi antaa voimaa kaikille ja sitouttaa ihmisiä. | Suunnittele käyttöliittymä/UX, joka on saavutettava ja helppokäyttöinen erilaisille käyttäjille. | Varmistaa, että laajempi joukko ihmisiä voi käyttää sovellusta tehokkaasti.            |
| Läpinäkyvyys           | Tekoälyjärjestelmien tulisi olla ymmärrettäviä.       | Tarjoa selkeää dokumentaatiota ja perusteluja tekoälyn vastauksille. | Käyttäjät luottavat järjestelmään paremmin, jos he voivat ymmärtää, miten päätökset tehdään. |
| Vastuuvelvollisuus     | Ihmisten tulisi olla vastuussa tekoälyjärjestelmistä. | Perusta selkeä prosessi tekoälypäätösten tarkastamiseen ja parantamiseen. | Mahdollistaa jatkuvan parantamisen ja korjaavat toimenpiteet virheiden sattuessa.       |

## Tehtävä

Katso [assignment](../../../07-building-chat-applications/python). Se vie sinut läpi sarjan harjoituksia ensimmäisten chat-kehotusten suorittamisesta tekstin luokitteluun ja tiivistämiseen sekä muuhun. Huomaa, että tehtävät ovat saatavilla eri ohjelmointikielillä!

## Hienoa työtä! Jatka matkaa

Tämän oppitunnin suorittamisen jälkeen tutustu [Generatiivisen tekoälyn oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), jotta voit jatkaa generatiivisen tekoälyn osaamisesi kehittämistä!

Siirry oppitunnille 8 nähdäksesi, miten voit aloittaa [hakusovellusten rakentamisen](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->