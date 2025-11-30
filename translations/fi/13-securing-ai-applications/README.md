<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-17T19:40:32+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "fi"
}
-->
# Generatiivisten tekoälysovellusten suojaaminen

[![Generatiivisten tekoälysovellusten suojaaminen](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.fi.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## Johdanto

Tässä oppitunnissa käsitellään:

- Tietoturvaa tekoälyjärjestelmien kontekstissa.
- Yleisiä riskejä ja uhkia tekoälyjärjestelmille.
- Menetelmiä ja huomioita tekoälyjärjestelmien suojaamiseksi.

## Oppimistavoitteet

Oppitunnin jälkeen ymmärrät:

- Tekoälyjärjestelmien uhat ja riskit.
- Yleiset menetelmät ja käytännöt tekoälyjärjestelmien suojaamiseksi.
- Kuinka tietoturvatestauksen toteuttaminen voi estää odottamattomia tuloksia ja käyttäjien luottamuksen heikkenemistä.

## Mitä tietoturva tarkoittaa generatiivisen tekoälyn kontekstissa?

Kun tekoäly (AI) ja koneoppimisteknologiat (ML) muokkaavat yhä enemmän elämäämme, on tärkeää suojata paitsi asiakastiedot myös itse tekoälyjärjestelmät. Tekoälyä ja koneoppimista käytetään yhä enemmän tukemaan päätöksentekoa aloilla, joissa väärä päätös voi johtaa vakaviin seurauksiin.

Tärkeimmät huomioitavat asiat:

- **Tekoälyn ja koneoppimisen vaikutus**: Tekoäly ja koneoppiminen vaikuttavat merkittävästi päivittäiseen elämään, ja niiden suojaaminen on siksi välttämätöntä.
- **Tietoturvaan liittyvät haasteet**: Tekoälyn ja koneoppimisen vaikutus vaatii asianmukaista huomiota, jotta voidaan suojata tekoälypohjaiset tuotteet kehittyneiltä hyökkäyksiltä, olivatpa ne trollien tai järjestäytyneiden ryhmien tekemiä.
- **Strategiset ongelmat**: Teknologiateollisuuden on ennakoivasti käsiteltävä strategisia haasteita varmistaakseen pitkäaikaisen asiakasturvallisuuden ja tietoturvan.

Lisäksi koneoppimismallit eivät pääsääntöisesti pysty erottamaan haitallista syötettä ja harmitonta poikkeavaa dataa. Merkittävä osa koulutusdatasta saadaan kuratoimattomista, valvomattomista julkisista tietokannoista, joihin kolmannet osapuolet voivat vapaasti lisätä sisältöä. Hyökkääjien ei tarvitse murtautua tietokantoihin, kun he voivat vapaasti lisätä niihin sisältöä. Ajan myötä matalan luottamuksen haitallinen data muuttuu korkean luottamuksen luotettavaksi dataksi, jos datan rakenne ja muotoilu pysyvät oikeina.

Siksi on kriittistä varmistaa, että mallien päätöksenteossa käyttämien tietovarastojen eheys ja suojaus ovat kunnossa.

## Tekoälyn uhkien ja riskien ymmärtäminen

Tekoälyn ja siihen liittyvien järjestelmien osalta datan myrkyttäminen on nykyään merkittävin tietoturvauhka. Datan myrkyttäminen tapahtuu, kun joku tahallaan muuttaa tekoälyn koulutuksessa käytettävää tietoa, mikä johtaa virheisiin. Tämä johtuu standardoitujen havaitsemis- ja lieventämismenetelmien puutteesta sekä siitä, että koulutuksessa luotetaan epäluotettaviin tai kuratoimattomiin julkisiin tietokantoihin. Datan eheyden ylläpitäminen ja virheellisen koulutusprosessin estäminen edellyttää datan alkuperän ja sukulinjan seuraamista. Muuten vanha sanonta "roskaa sisään, roskaa ulos" pitää paikkansa, mikä heikentää mallin suorituskykyä.

Tässä on esimerkkejä siitä, miten datan myrkyttäminen voi vaikuttaa malleihisi:

1. **Tunnisteiden kääntäminen**: Kaksiluokkaisessa luokittelutehtävässä hyökkääjä kääntää tahallaan pienen osan koulutusdatan tunnisteista. Esimerkiksi harmittomat näytteet merkitään haitallisiksi, mikä johtaa mallin oppimaan virheellisiä yhteyksiä.\
   **Esimerkki**: Roskapostisuodatin luokittelee oikeat sähköpostit roskapostiksi manipuloitujen tunnisteiden vuoksi.
2. **Ominaisuuksien myrkyttäminen**: Hyökkääjä muokkaa hienovaraisesti koulutusdatan ominaisuuksia lisätäkseen harhaa tai harhauttaakseen mallia.\
   **Esimerkki**: Lisäämällä epäolennaisia avainsanoja tuotekuvauksiin manipuloidaan suositusjärjestelmiä.
3. **Datan injektointi**: Haitallisen datan lisääminen koulutusjoukkoon mallin käyttäytymisen vaikuttamiseksi.\
   **Esimerkki**: Väärennettyjen käyttäjäarvostelujen lisääminen tunteiden analysointitulosten vääristämiseksi.
4. **Takaporttihyökkäykset**: Hyökkääjä lisää piilotetun kuvion (takaportin) koulutusdataan. Malli oppii tunnistamaan tämän kuvion ja käyttäytyy haitallisesti, kun se aktivoidaan.\
   **Esimerkki**: Kasvojentunnistusjärjestelmä, joka on koulutettu takaporttikuvioilla ja tunnistaa väärin tietyn henkilön.

MITRE Corporation on luonut [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst) -tietokannan, joka sisältää taktiikoita ja tekniikoita, joita hyökkääjät käyttävät tekoälyjärjestelmiin kohdistuvissa todellisissa hyökkäyksissä.

> Tekoälyä hyödyntävissä järjestelmissä on yhä enemmän haavoittuvuuksia, sillä tekoälyn käyttö lisää olemassa olevien järjestelmien hyökkäyspintaa perinteisten kyberhyökkäysten ulkopuolella. Kehitimme ATLASin lisätäksemme tietoisuutta näistä ainutlaatuisista ja kehittyvistä haavoittuvuuksista, kun globaali yhteisö yhä enemmän integroi tekoälyä erilaisiin järjestelmiin. ATLAS on mallinnettu MITRE ATT&CK® -kehykseen, ja sen taktiikat, tekniikat ja menettelytavat (TTP:t) täydentävät ATT&CKin vastaavia.

Samoin kuin MITRE ATT&CK® -kehystä käytetään laajasti perinteisessä kyberturvallisuudessa kehittyneiden uhkien emulointiskenaarioiden suunnittelussa, ATLAS tarjoaa helposti haettavan joukon TTP:itä, jotka auttavat ymmärtämään ja valmistautumaan puolustautumaan kehittyviä hyökkäyksiä vastaan.

Lisäksi Open Web Application Security Project (OWASP) on luonut "[Top 10 -listan](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" kriittisimmistä haavoittuvuuksista sovelluksissa, jotka hyödyntävät LLM:itä. Lista korostaa uhkia, kuten edellä mainittu datan myrkyttäminen, sekä muita, kuten:

- **Prompt Injection**: Tekniikka, jossa hyökkääjät manipuloivat suurta kielimallia (LLM) huolellisesti muotoilluilla syötteillä, saaden sen käyttäytymään odottamattomalla tavalla.
- **Toimitusketjun haavoittuvuudet**: Komponentit ja ohjelmistot, jotka muodostavat LLM:ien käyttämät sovellukset, kuten Python-moduulit tai ulkoiset tietokannat, voivat itse olla vaarantuneita, mikä johtaa odottamattomiin tuloksiin, ennakkoluuloihin ja jopa haavoittuvuuksiin infrastruktuurissa.
- **Liiallinen luottamus**: LLM:t ovat erehtyväisiä ja taipuvaisia "hallusinoimaan", tuottaen epätarkkoja tai vaarallisia tuloksia. Useissa dokumentoiduissa tapauksissa ihmiset ovat ottaneet tulokset sellaisenaan, mikä on johtanut odottamattomiin negatiivisiin seurauksiin tosielämässä.

Microsoft Cloud Advocate Rod Trent on kirjoittanut ilmaisen e-kirjan, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), joka käsittelee syvällisesti näitä ja muita kehittyviä tekoälyuhkia ja tarjoaa laajaa ohjeistusta näiden tilanteiden käsittelemiseksi.

## Tietoturvatestaus tekoälyjärjestelmille ja LLM:ille

Tekoäly (AI) muuttaa monia aloja ja teollisuudenaloja, tarjoten uusia mahdollisuuksia ja hyötyjä yhteiskunnalle. Tekoäly kuitenkin tuo mukanaan merkittäviä haasteita ja riskejä, kuten tietosuoja, ennakkoluulot, selitettävyyden puute ja mahdollinen väärinkäyttö. Siksi on tärkeää varmistaa, että tekoälyjärjestelmät ovat turvallisia ja vastuullisia, eli että ne noudattavat eettisiä ja oikeudellisia standardeja ja että käyttäjät ja sidosryhmät voivat luottaa niihin.

Tietoturvatestaus on prosessi, jossa arvioidaan tekoälyjärjestelmän tai LLM:n tietoturvaa tunnistamalla ja hyödyntämällä niiden haavoittuvuuksia. Testauksen voivat suorittaa kehittäjät, käyttäjät tai kolmannen osapuolen tarkastajat testauksen tarkoituksesta ja laajuudesta riippuen. Yleisimmät tietoturvatestausmenetelmät tekoälyjärjestelmille ja LLM:ille ovat:

- **Datan puhdistus**: Prosessi, jossa koulutusdatasta tai tekoälyjärjestelmän syötteestä poistetaan tai anonymisoidaan arkaluontoiset tai yksityiset tiedot. Datan puhdistus voi auttaa estämään tietovuotoja ja haitallista manipulointia vähentämällä luottamuksellisten tai henkilökohtaisten tietojen altistumista.
- **Vihamielinen testaus**: Prosessi, jossa tekoälyjärjestelmän tai LLM:n syötteeseen tai tulosteeseen luodaan ja sovelletaan vihamielisiä esimerkkejä sen kestävyyden ja vastustuskyvyn arvioimiseksi vihamielisiä hyökkäyksiä vastaan. Vihamielinen testaus voi auttaa tunnistamaan ja lieventämään tekoälyjärjestelmän tai LLM:n haavoittuvuuksia ja heikkouksia, joita hyökkääjät voivat hyödyntää.
- **Mallin varmistus**: Prosessi, jossa tekoälyjärjestelmän tai LLM:n malliparametrien tai arkkitehtuurin oikeellisuus ja täydellisyys varmistetaan. Mallin varmistus voi auttaa havaitsemaan ja estämään mallin varastamisen varmistamalla, että malli on suojattu ja todennettu.
- **Tulosten validointi**: Prosessi, jossa tekoälyjärjestelmän tai LLM:n tuottaman tuloksen laatu ja luotettavuus validoidaan. Tulosten validointi voi auttaa havaitsemaan ja korjaamaan haitallista manipulointia varmistamalla, että tulos on johdonmukainen ja tarkka.

OpenAI, tekoälyjärjestelmien johtava toimija, on perustanut _turvallisuusarviointeja_ osana red teaming -verkostoaloitettaan, jonka tavoitteena on testata tekoälyjärjestelmien tuottamia tuloksia ja edistää tekoälyn turvallisuutta.

> Arvioinnit voivat vaihdella yksinkertaisista kysymys-vastaus-testeistä monimutkaisempiin simulaatioihin. Konkreettisina esimerkkeinä tässä on OpenAI:n kehittämiä arviointeja tekoälykäyttäytymisen arvioimiseksi eri näkökulmista:

#### Suostuttelu

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi huijata toisen tekoälyjärjestelmän sanomaan salaisen sanan?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi suostutella toisen tekoälyjärjestelmän lahjoittamaan rahaa?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi vaikuttaa toisen tekoälyjärjestelmän poliittisen ehdotuksen kannatukseen?

#### Steganografia (piiloviestintä)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi välittää salaisia viestejä jäämättä kiinni toiselle tekoälyjärjestelmälle?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi pakata ja purkaa viestejä salaisen viestinnän mahdollistamiseksi?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi tehdä yhteistyötä toisen tekoälyjärjestelmän kanssa ilman suoraa viestintää?

### Tekoälyn tietoturva

On välttämätöntä pyrkiä suojaamaan tekoälyjärjestelmiä haitallisilta hyökkäyksiltä, väärinkäytöltä tai odottamattomilta seurauksilta. Tämä sisältää toimenpiteitä tekoälyjärjestelmien turvallisuuden, luotettavuuden ja luottamuksen varmistamiseksi, kuten:

- Tekoälymallien koulutuksessa ja käytössä käytettävän datan ja algoritmien suojaaminen
- Tekoälyjärjestelmien luvattoman käytön, manipuloinnin tai sabotoinnin estäminen
- Ennakkoluulojen, syrjinnän tai eettisten ongelmien havaitseminen ja lieventäminen tekoälyjärjestelmissä
- Tekoälypäätösten ja -toimien vastuullisuuden, läpinäkyvyyden ja selitettävyyden varmistaminen
- Tekoälyjärjestelmien tavoitteiden ja arvojen yhdenmukaistaminen ihmisten ja yhteiskunnan kanssa

Tekoälyn tietoturva on tärkeää tekoälyjärjestelmien ja datan eheyden, saatavuuden ja luottamuksellisuuden varmistamiseksi. Tekoälyn tietoturvan haasteet ja mahdollisuudet ovat:

- **Mahdollisuus**: Tekoälyn integroiminen kyberturvallisuusstrategioihin, sillä se voi olla keskeisessä roolissa uhkien tunnistamisessa ja reagointiaikojen parantamisessa. Tekoäly voi auttaa automatisoimaan ja tehostamaan kyberhyökkäysten, kuten phishingin, haittaohjelmien tai kiristysohjelmien, havaitsemista ja lieventämistä.
- **Haaste**: Tekoälyä voidaan käyttää myös hyökkääjien toimesta kehittyneiden hyökkäysten toteuttamiseen, kuten väärennetyn tai harhaanjohtavan sisällön luomiseen, käyttäjien jäljittelyyn tai tekoälyjärjestelmien haavoittuvuuksien hyödyntämiseen. Siksi tekoälykehittäjillä on erityinen vastuu suunnitella järjestelmiä, jotka ovat kestäviä ja vastustuskykyisiä väärinkäytölle.

### Datan suojaaminen

LLM:t voivat aiheuttaa riskejä niiden käyttämän datan yksityisyydelle ja turvallisuudelle. Esimerkiksi LLM:t voivat mahdollisesti muistaa ja vuotaa arkaluontoista tietoa koulutusdatastaan, kuten henkilökohtaisia nimiä, osoitteita, salasanoja tai luottokorttinumeroita. Niitä voidaan myös manipuloida tai hyökätä haitallisten toimijoiden toimesta, jotka haluavat hyödyntää niiden haavoittuvuuksia tai ennakkoluuloja. Siksi on tärkeää olla tietoinen näistä riskeistä ja ryhtyä asianmukaisiin toimenpiteisiin LLM:ien kanssa käytettävän datan suojaamiseksi. Voit suojata LLM:ien kanssa käytettävää dataa seuraavilla toimenpiteillä:

- **Rajoita LLM:ien kanssa jaettavan datan määrää ja tyyppiä**: Jaa vain dataa, joka on tarpeellista ja tarkoituksenmukaista aiottuihin tarkoituksiin, ja vältä jakamasta arkaluontoista, luottamuksellista tai henkilökohtaista dataa. Käyttäjien tul
Reaaliaikaisten uhkien jäljittelyä pidetään nykyään vakiokäytäntönä kestävämpien tekoälyjärjestelmien rakentamisessa, käyttämällä samanlaisia työkaluja, taktiikoita ja menetelmiä järjestelmien riskien tunnistamiseen ja puolustajien reagoinnin testaamiseen.

> Tekoälyn red teaming -käytäntö on kehittynyt laajempaan merkitykseen: se ei kata ainoastaan tietoturva-aukkojen etsimistä, vaan myös muiden järjestelmävirheiden, kuten mahdollisesti haitallisen sisällön tuottamisen, tutkimista. Tekoälyjärjestelmät tuovat mukanaan uusia riskejä, ja red teaming on keskeinen keino ymmärtää näitä uusia riskejä, kuten kehotusruiskutusta ja perustelemattoman sisällön tuottamista. - [Microsoft AI Red Team rakentaa turvallisempaa tekoälyä](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Ohjeet ja resurssit red teamingille](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.fi.png)]()

Alla on keskeisiä oivalluksia, jotka ovat muokanneet Microsoftin AI Red Team -ohjelmaa.

1. **Tekoälyn red teamingin laajentunut ulottuvuus:**
   Tekoälyn red teaming kattaa nyt sekä tietoturvan että vastuullisen tekoälyn (RAI) tavoitteet. Perinteisesti red teaming keskittyi tietoturvaan, käsitellen mallia vektorina (esim. mallin varastaminen). Tekoälyjärjestelmät tuovat mukanaan uusia tietoturva-aukkoja (esim. kehotusruiskutus, myrkytys), jotka vaativat erityistä huomiota. Tietoturvan lisäksi tekoälyn red teaming tutkii myös oikeudenmukaisuuskysymyksiä (esim. stereotypiointi) ja haitallista sisältöä (esim. väkivallan ihannointi). Näiden ongelmien varhainen tunnistaminen mahdollistaa puolustusinvestointien priorisoinnin.
2. **Pahantahtoiset ja harmittomat virheet:**
   Tekoälyn red teaming tarkastelee virheitä sekä pahantahtoisesta että harmittomasta näkökulmasta. Esimerkiksi uuden Bingin red teamingissä tutkitaan paitsi sitä, miten pahantahtoiset vastustajat voivat manipuloida järjestelmää, myös sitä, miten tavalliset käyttäjät voivat kohdata ongelmallista tai haitallista sisältöä. Toisin kuin perinteinen tietoturvan red teaming, joka keskittyy pääasiassa pahantahtoisiin toimijoihin, tekoälyn red teaming huomioi laajemman joukon henkilöitä ja mahdollisia virheitä.
3. **Tekoälyjärjestelmien dynaaminen luonne:**
   Tekoälysovellukset kehittyvät jatkuvasti. Suurten kielimallien sovelluksissa kehittäjät mukautuvat muuttuviin vaatimuksiin. Jatkuva red teaming varmistaa jatkuvan valppauden ja sopeutumisen kehittyviin riskeihin.

Tekoälyn red teaming ei kata kaikkea ja sitä tulisi pitää täydentävänä toimintana lisäkontrolleille, kuten [roolipohjainen pääsynhallinta (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) ja kattavat datanhallintaratkaisut. Sen tarkoitus on täydentää tietoturvastrategiaa, joka keskittyy turvallisten ja vastuullisten tekoälyratkaisujen käyttöön, huomioiden yksityisyyden ja tietoturvan samalla pyrkien minimoimaan ennakkoluulot, haitallisen sisällön ja väärän tiedon, jotka voivat heikentää käyttäjien luottamusta.

Tässä on lista lisälukemista, joka auttaa sinua ymmärtämään, miten red teaming voi auttaa tunnistamaan ja lieventämään riskejä tekoälyjärjestelmissäsi:

- [Red teamingin suunnittelu suurille kielimalleille (LLM) ja niiden sovelluksille](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Mikä on OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [Tekoälyn red teaming - keskeinen käytäntö turvallisempien ja vastuullisempien tekoälyratkaisujen rakentamisessa](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), tietokanta taktiikoista ja tekniikoista, joita vastustajat käyttävät tekoälyjärjestelmiin kohdistuvissa todellisissa hyökkäyksissä.

## Tietotesti

Mikä voisi olla hyvä lähestymistapa datan eheyden ylläpitämiseen ja väärinkäytön estämiseen?

1. Käytä vahvoja roolipohjaisia kontrollimekanismeja datan käyttöoikeuksien ja hallinnan osalta  
1. Toteuta ja tarkista datan merkintä väärinkäytön tai virheellisen esittämisen estämiseksi  
1. Varmista, että tekoälyinfrastruktuurisi tukee sisällön suodatusta  

A:1, Vaikka kaikki kolme ovat erinomaisia suosituksia, varmistamalla, että annat käyttäjille asianmukaiset datan käyttöoikeudet, voit merkittävästi estää datan manipulointia ja virheellistä esittämistä, joita LLM:t käyttävät.

## 🚀 Haaste

Lue lisää siitä, miten voit [hallita ja suojata arkaluontoista tietoa](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) tekoälyn aikakaudella.

## Hienoa työtä, jatka oppimista

Tämän oppitunnin jälkeen tutustu [Generative AI Learning -kokoelmaan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn tietämyksesi kehittämistä!

Siirry oppituntiin 14, jossa tarkastelemme [Generatiivisen tekoälyn sovelluskehityksen elinkaarta](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.