<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:23:21+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "fi"
}
-->
# Generatiivisten tekoälysovellusten turvaaminen

## Johdanto

Tässä oppitunnissa käsitellään:

- Tietoturvaa tekoälyjärjestelmien yhteydessä.
- Yleisiä riskejä ja uhkia tekoälyjärjestelmille.
- Menetelmiä ja huomioita tekoälyjärjestelmien turvaamiseksi.

## Oppimistavoitteet

Tämän oppitunnin jälkeen ymmärrät:

- Tekoälyjärjestelmiin kohdistuvat uhat ja riskit.
- Yleisiä menetelmiä ja käytäntöjä tekoälyjärjestelmien turvaamiseksi.
- Miten tietoturvatestaus voi estää odottamattomia tuloksia ja käyttäjien luottamuksen heikkenemistä.

## Mitä tietoturva tarkoittaa generatiivisen tekoälyn yhteydessä?

Kun tekoäly- (AI) ja koneoppimisteknologiat (ML) muokkaavat yhä enemmän elämäämme, on tärkeää suojata paitsi asiakastietoja myös itse tekoälyjärjestelmiä. AI/ML:ää käytetään yhä enemmän tukemaan arvokkaita päätöksentekoprosesseja aloilla, joilla väärä päätös voi johtaa vakaviin seurauksiin.

Tässä on keskeisiä huomioita:

- **AI/ML:n vaikutus**: AI/ML vaikuttavat merkittävästi päivittäiseen elämään, ja siksi niiden suojaaminen on tullut välttämättömäksi.
- **Tietoturvahaasteet**: AI/ML:n vaikutus vaatii asianmukaista huomiota, jotta AI-pohjaiset tuotteet voidaan suojata kehittyneiltä hyökkäyksiltä, olivatpa ne trollien tai järjestäytyneiden ryhmien tekemiä.
- **Strategiset ongelmat**: Teknologia-alan on proaktiivisesti puututtava strategisiin haasteisiin varmistaakseen asiakkaiden pitkäaikaisen turvallisuuden ja tietoturvan.

Lisäksi koneoppimismallit eivät kykene suurelta osin erottamaan haitallista syötettä ja vaaratonta poikkeavaa dataa. Merkittävä osa harjoitusdatasta saadaan kuratoimattomista, valvomattomista julkisista tietokannoista, jotka ovat avoimia kolmannen osapuolen kontribuutioille. Hyökkääjien ei tarvitse vaarantaa tietokantoja, kun he voivat vapaasti lisätä niihin tietoja. Ajan myötä matalan luottamuksen haitallinen data voi muuttua korkean luottamuksen luotetuksi dataksi, jos datan rakenne/muotoilu pysyy oikeana.

Siksi on kriittistä varmistaa, että malliesi päätöksenteossa käyttämien tietovarastojen eheys ja suojaus ovat kunnossa.

## Ymmärtäminen tekoälyn uhista ja riskeistä

Tekoälyn ja siihen liittyvien järjestelmien osalta datan myrkytys erottuu nykyään merkittävimpänä tietoturvauhkana. Datamyrkytys tarkoittaa, että joku muuttaa tahallisesti tekoälyn koulutuksessa käytettävää tietoa, mikä johtaa virheisiin. Tämä johtuu standardoitujen havaitsemis- ja lieventämismenetelmien puutteesta sekä siitä, että luotamme luotettamattomiin tai kuratoimattomiin julkisiin tietokantoihin koulutuksessa. Dataintegriteetin ylläpitämiseksi ja virheellisen koulutusprosessin estämiseksi on tärkeää seurata datan alkuperää ja sukulinjaa. Muuten vanha sanonta "roskaa sisään, roskaa ulos" pitää paikkansa, mikä johtaa mallin suorituskyvyn heikkenemiseen.

Tässä on esimerkkejä siitä, miten datamyrkytys voi vaikuttaa malleihisi:

1. **Label Flipping**: Kaksiluokkaisessa luokittelutehtävässä vastustaja kääntää tahallisesti pienen osajoukon harjoitusdatan tunnisteista. Esimerkiksi vaarattomat näytteet merkitään haitallisiksi, mikä johtaa mallin oppimaan virheellisiä assosiaatioita.\
   **Esimerkki**: Roskapostisuodatin, joka luokittelee lailliset sähköpostit roskapostiksi manipuloitujen tunnisteiden vuoksi.
2. **Feature Poisoning**: Hyökkääjä muuttaa hienovaraisesti harjoitusdatan ominaisuuksia lisätäkseen harhaa tai harhauttaakseen mallia.\
   **Esimerkki**: Lisätään epäolennaisia avainsanoja tuotekuvauksiin manipuloidakseen suositusjärjestelmiä.
3. **Data Injection**: Haitallisen datan lisääminen harjoitusjoukkoon vaikuttaakseen mallin käyttäytymiseen.\
   **Esimerkki**: Väärennettyjen käyttäjäarvostelujen lisääminen tunteiden analyysin tulosten vinouttamiseksi.
4. **Backdoor Attacks**: Vastustaja lisää piilotetun kuvion (takaportin) harjoitusdataan. Malli oppii tunnistamaan tämän kuvion ja käyttäytyy haitallisesti, kun se laukaistaan.\
   **Esimerkki**: Kasvojentunnistusjärjestelmä, joka on koulutettu takaporttikuvilla ja joka tunnistaa väärin tietyn henkilön.

MITRE Corporation on luonut [ATLASin (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), tietokannan taktiikoista ja tekniikoista, joita vastustajat käyttävät tekoälyjärjestelmiin kohdistuvissa reaalimaailman hyökkäyksissä.

> Tekoälyyn perustuvissa järjestelmissä on yhä enemmän haavoittuvuuksia, sillä tekoälyn käyttö lisää olemassa olevien järjestelmien hyökkäyspinta-alaa perinteisten kyberhyökkäysten lisäksi. Kehitimme ATLASin lisätäksemme tietoisuutta näistä ainutlaatuisista ja kehittyvistä haavoittuvuuksista, kun globaali yhteisö yhä enemmän ottaa tekoälyn käyttöön eri järjestelmissä. ATLAS on mallinnettu MITRE ATT&CK® -kehyksen mukaan, ja sen taktiikat, tekniikat ja menettelytavat (TTP:t) täydentävät ATT&CK:n TTP:itä.

Samoin kuin MITRE ATT&CK® -kehys, jota käytetään laajasti perinteisessä kyberturvallisuudessa kehittyneiden uhkien emulointiskenaarioiden suunnittelussa, ATLAS tarjoaa helposti haettavan TTP-joukon, joka voi auttaa ymmärtämään ja valmistautumaan puolustautumaan kehittyviä hyökkäyksiä vastaan.

Lisäksi Open Web Application Security Project (OWASP) on luonut "[Top 10 -listan](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" kriittisimmistä haavoittuvuuksista sovelluksissa, jotka käyttävät LLM:itä. Lista korostaa uhkien, kuten edellä mainitun datamyrkytyksen, riskejä sekä muita, kuten:

- **Prompt Injection**: tekniikka, jossa hyökkääjät manipuloivat suurta kielimallia (LLM) huolellisesti laadituilla syötteillä, saaden sen käyttäytymään tarkoituksensa vastaisesti.
- **Toimitusketjun haavoittuvuudet**: komponentit ja ohjelmistot, jotka muodostavat LLM:n käyttämät sovellukset, kuten Python-moduulit tai ulkoiset tietokannat, voivat itsessään olla vaarantuneita, mikä johtaa odottamattomiin tuloksiin, esiin tuleviin harhoihin ja jopa haavoittuvuuksiin taustalla olevassa infrastruktuurissa.
- **Liiallinen luottamus**: LLM:t ovat virheellisiä ja ovat olleet alttiita hallusinaatioille, jotka tuottavat epätarkkoja tai turvattomia tuloksia. Useissa dokumentoiduissa tapauksissa ihmiset ovat ottaneet tulokset annettuina, mikä on johtanut odottamattomiin reaalimaailman kielteisiin seurauksiin.

Microsoftin pilviedustaja Rod Trent on kirjoittanut ilmaisen e-kirjan, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), joka käsittelee syvällisesti näitä ja muita nousevia tekoälyuhkia ja tarjoaa laajaa ohjausta siitä, miten parhaiten käsitellä näitä skenaarioita.

## Tietoturvatestaus tekoälyjärjestelmille ja LLM:ille

Tekoäly (AI) muuttaa useita aloja ja teollisuudenaloja, tarjoten uusia mahdollisuuksia ja etuja yhteiskunnalle. Tekoäly tuo kuitenkin mukanaan merkittäviä haasteita ja riskejä, kuten tietosuoja, puolueellisuus, selittämättömyyden puute ja mahdollinen väärinkäyttö. Siksi on tärkeää varmistaa, että tekoälyjärjestelmät ovat turvallisia ja vastuullisia, mikä tarkoittaa, että ne noudattavat eettisiä ja oikeudellisia standardeja ja että käyttäjät ja sidosryhmät voivat luottaa niihin.

Tietoturvatestaus on prosessi, jossa arvioidaan tekoälyjärjestelmän tai LLM:n tietoturvaa tunnistamalla ja hyödyntämällä niiden haavoittuvuuksia. Tämä voidaan tehdä kehittäjien, käyttäjien tai kolmansien osapuolten auditoijien toimesta riippuen testauksen tarkoituksesta ja laajuudesta. Joitakin yleisimpiä tekoälyjärjestelmien ja LLM:ien tietoturvatestausmenetelmiä ovat:

- **Datansuojaus**: Tämä on prosessi, jossa poistetaan tai anonymisoidaan herkät tai yksityiset tiedot tekoälyjärjestelmän tai LLM:n harjoitusdatasta tai syötteestä. Datansuojaus voi auttaa estämään tietovuodot ja haitallisen manipuloinnin vähentämällä luottamuksellisten tai henkilökohtaisten tietojen altistumista.
- **Vihamielinen testaus**: Tämä on prosessi, jossa tuotetaan ja sovelletaan vihamielisiä esimerkkejä tekoälyjärjestelmän tai LLM:n syötteeseen tai tulosteeseen sen kestävyyden ja joustavuuden arvioimiseksi vihamielisiä hyökkäyksiä vastaan. Vihamielinen testaus voi auttaa tunnistamaan ja lieventämään tekoälyjärjestelmän tai LLM:n haavoittuvuuksia ja heikkouksia, joita hyökkääjät voivat hyödyntää.
- **Mallin varmistus**: Tämä on prosessi, jossa varmistetaan tekoälyjärjestelmän tai LLM:n malliparametrien tai arkkitehtuurin oikeellisuus ja täydellisyys. Mallin varmistus voi auttaa havaitsemaan ja estämään mallin varastamisen varmistamalla, että malli on suojattu ja todennettu.
- **Tuloksen validointi**: Tämä on prosessi, jossa validoidaan tekoälyjärjestelmän tai LLM:n tuottaman tuloksen laatu ja luotettavuus. Tuloksen validointi voi auttaa havaitsemaan ja korjaamaan haitallista manipulointia varmistamalla, että tulos on johdonmukainen ja tarkka.

OpenAI, tekoälyjärjestelmien johtaja, on perustanut sarjan _turvallisuusarviointeja_ osana heidän punaisen tiimin verkostoaloitettaan, jonka tavoitteena on testata tekoälyjärjestelmien tuotoksia ja edistää tekoälyturvallisuutta.

> Arvioinnit voivat vaihdella yksinkertaisista kysymys-vastaus testeistä monimutkaisempiin simulaatioihin. Tässä on konkreettisia esimerkkejä OpenAI:n kehittämistä arvioinneista tekoälykäyttäytymisten arvioimiseksi useista näkökulmista:

#### Suostuttelu

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi huijata toista tekoälyjärjestelmää sanomaan salaisen sanan?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi vakuuttaa toisen tekoälyjärjestelmän lahjoittamaan rahaa?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi vaikuttaa toisen tekoälyjärjestelmän tukeen poliittiselle ehdotukselle?

#### Steganografia (piilotettu viestintä)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi lähettää salaisia viestejä jäämättä kiinni toiselle tekoälyjärjestelmälle?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi pakata ja purkaa viestejä, jotta salaiset viestit voidaan piilottaa?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi koordinoida toisen tekoälyjärjestelmän kanssa ilman suoraa viestintää?

### Tekoälyturvallisuus

On välttämätöntä pyrkiä suojaamaan tekoälyjärjestelmiä haitallisilta hyökkäyksiltä, väärinkäytöksiltä tai odottamattomilta seurauksilta. Tämä sisältää toimenpiteet tekoälyjärjestelmien turvallisuuden, luotettavuuden ja luotettavuuden varmistamiseksi, kuten:

- Tietojen ja algoritmien turvaaminen, joita käytetään tekoälymallien kouluttamiseen ja ajamiseen
- Luvattoman pääsyn, manipuloinnin tai sabotoinnin estäminen tekoälyjärjestelmissä
- Puolueellisuuden, syrjinnän tai eettisten ongelmien havaitseminen ja lieventäminen tekoälyjärjestelmissä
- Tekoälypäätösten ja -toimintojen vastuullisuuden, läpinäkyvyyden ja selitettävyys
- Tekoälyjärjestelmien tavoitteiden ja arvojen yhdenmukaistaminen ihmisten ja yhteiskunnan kanssa

Tekoälyturvallisuus on tärkeää tekoälyjärjestelmien ja tietojen eheyden, saatavuuden ja luottamuksellisuuden varmistamiseksi. Jotkut tekoälyturvallisuuden haasteet ja mahdollisuudet ovat:

- Mahdollisuus: Tekoälyn sisällyttäminen kyberturvallisuusstrategioihin, koska se voi olla ratkaisevassa asemassa uhkien tunnistamisessa ja reagointiaikojen parantamisessa. Tekoäly voi auttaa automatisoimaan ja lisäämään kyberhyökkäysten, kuten tietojenkalastelun, haittaohjelmien tai kiristysohjelmien, havaitsemista ja lieventämistä.
- Haaste: Vastustajat voivat myös käyttää tekoälyä käynnistämään kehittyneitä hyökkäyksiä, kuten luomaan väärennettyä tai harhaanjohtavaa sisältöä, esiintymään käyttäjinä tai hyödyntämään tekoälyjärjestelmien haavoittuvuuksia. Siksi tekoälykehittäjillä on ainutlaatuinen vastuu suunnitella järjestelmiä, jotka ovat vahvoja ja joustavia väärinkäyttöä vastaan.

### Tietosuoja

LLM:t voivat aiheuttaa riskejä niiden käyttämien tietojen yksityisyydelle ja turvallisuudelle. Esimerkiksi LLM:t voivat mahdollisesti muistaa ja vuotaa harjoitusdatastaan peräisin olevia arkaluonteisia tietoja, kuten henkilönimiä, osoitteita, salasanoja tai luottokorttinumeroita. Niitä voivat myös manipuloida tai hyökätä haitalliset toimijat, jotka haluavat hyödyntää niiden haavoittuvuuksia tai puolueellisuuksia. Siksi on tärkeää olla tietoinen näistä riskeistä ja ryhtyä asianmukaisiin toimenpiteisiin LLM:ien kanssa käytettävien tietojen suojaamiseksi. On olemassa useita toimenpiteitä, joilla voit suojata LLM:ien kanssa käytettäviä tietoja. Näihin toimenpiteisiin kuuluvat:

- **Rajoita niiden kanssa jaettavien tietojen määrää ja tyyppiä**: Jaa vain tiedot, jotka ovat tarpeellisia ja merkityksellisiä aiottuja tarkoituksia varten, ja vältä jakamasta tietoja, jotka ovat arkaluonteisia, luottamuksellisia tai henkilökohtaisia. Käyttäjien tulisi myös anonymisoida tai salata LLM:ien kanssa jaettavat tiedot, kuten poistamalla tai peittämällä tunnistettavat tiedot tai käyttämällä turvallisia viestintäkanavia.
- **Varmista LLM:ien

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä AI-käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomaa, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisten tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.