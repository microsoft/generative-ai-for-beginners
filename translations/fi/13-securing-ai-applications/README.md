<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T22:54:11+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "fi"
}
-->
# Suojaa generatiiviset tekoälysovelluksesi

[![Suojaa generatiiviset tekoälysovelluksesi](../../../translated_images/13-lesson-banner.c21a3a479f9ff14ad1f7c9b02bfe0d9a549b43497588334356f91073466a1283.fi.png)](https://aka.ms/gen-ai-lesson13-gh?WT.mc_id=academic-105485-koreyst)

## Johdanto

Tässä oppitunnissa käsitellään:

- Turvallisuutta tekoälyjärjestelmien kontekstissa.
- Yleisiä riskejä ja uhkia tekoälyjärjestelmille.
- Menetelmiä ja huomioita tekoälyjärjestelmien suojaamiseksi.

## Oppimistavoitteet

Oppitunnin jälkeen ymmärrät:

- Tekoälyjärjestelmien uhat ja riskit.
- Yleiset menetelmät ja käytännöt tekoälyjärjestelmien suojaamiseksi.
- Kuinka turvallisuustestauksen toteuttaminen voi estää odottamattomia tuloksia ja käyttäjien luottamuksen heikkenemistä.

## Mitä turvallisuus tarkoittaa generatiivisen tekoälyn kontekstissa?

Kun tekoäly (AI) ja koneoppimisteknologiat (ML) muokkaavat yhä enemmän elämäämme, on tärkeää suojata paitsi asiakastiedot myös itse tekoälyjärjestelmät. AI/ML käytetään yhä enemmän tukemaan arvokkaita päätöksentekoprosesseja aloilla, joilla väärä päätös voi johtaa vakaviin seurauksiin.

Tässä keskeisiä huomioita:

- **AI/ML:n vaikutus**: AI/ML vaikuttavat merkittävästi päivittäiseen elämään, ja niiden suojaaminen on tullut välttämättömäksi.
- **Turvallisuushaasteet**: Tämä vaikutus, jonka AI/ML:llä on, vaatii asianmukaista huomiota, jotta voidaan suojata tekoälypohjaisia tuotteita kehittyneiltä hyökkäyksiltä, olipa kyseessä trollit tai organisoidut ryhmät.
- **Strategiset ongelmat**: Teknologiateollisuuden on ennakoivasti käsiteltävä strategisia haasteita varmistaakseen pitkän aikavälin asiakasturvallisuuden ja tietoturvan.

Lisäksi koneoppimismallit eivät pääosin pysty erottamaan haitallista syötettä ja harmitonta poikkeavaa dataa. Merkittävä osa harjoitusdatasta saadaan kuratoimattomista, valvomattomista, julkisista tietokannoista, jotka ovat avoimia kolmannen osapuolen kontribuutioille. Hyökkääjien ei tarvitse vaarantaa tietokantoja, kun he voivat vapaasti lisätä niihin. Ajan myötä matalan luottamuksen haitallinen data muuttuu korkean luottamuksen luotettavaksi dataksi, jos datan rakenne/muotoilu pysyy oikeana.

Siksi on kriittistä varmistaa datavarastojen eheys ja suojaus, joita mallisi käyttävät päätöksenteossa.

## Tekoälyn uhkien ja riskien ymmärtäminen

Tekoälyn ja siihen liittyvien järjestelmien osalta datamyrkytys on nykyään merkittävin turvallisuusuhka. Datamyrkytys tarkoittaa, että joku muuttaa tahallaan tietoja, joita käytetään tekoälyn kouluttamiseen, aiheuttaen sen virheitä. Tämä johtuu standardoitujen tunnistus- ja lieventämismenetelmien puutteesta sekä luottamattomien tai kuratoimattomien julkisten tietokantojen käytöstä koulutukseen. Dataintegriteetin ylläpitämiseksi ja virheellisen koulutusprosessin estämiseksi on tärkeää seurata datan alkuperää ja sukua. Muuten vanha sanonta "roskaa sisään, roskaa ulos" pitää paikkansa, mikä johtaa mallin suorituskyvyn heikkenemiseen.

Tässä esimerkkejä siitä, miten datamyrkytys voi vaikuttaa malleihisi:

1. **Label Flipping**: Kaksiluokkaisessa luokittelutehtävässä vastustaja kääntää tarkoituksella pienen osan koulutusdatasta etikettejä. Esimerkiksi harmittomat näytteet merkitään haitallisiksi, mikä johtaa mallin oppimaan virheellisiä yhteyksiä.\
   **Esimerkki**: Roskapostisuodatin, joka luokittelee oikeat sähköpostit roskapostiksi manipuloitujen etikettien vuoksi.
2. **Feature Poisoning**: Hyökkääjä muokkaa hienovaraisesti koulutusdatan ominaisuuksia lisätäkseen harhaa tai harhauttaakseen mallia.\
   **Esimerkki**: Epäolennaisten avainsanojen lisääminen tuotekuvauksiin manipuloimaan suositusjärjestelmiä.
3. **Data Injection**: Haitallisen datan lisääminen koulutusjoukkoon vaikuttamaan mallin käyttäytymiseen.\
   **Esimerkki**: Väärennettyjen käyttäjäarvostelujen lisääminen tuntemusanalyysin tulosten vääristämiseksi.
4. **Backdoor Attacks**: Vastustaja lisää piilotetun kuvion (takaportin) koulutusdataan. Malli oppii tunnistamaan tämän kuvion ja käyttäytyy haitallisesti, kun se laukaistaan.\
   **Esimerkki**: Kasvojentunnistusjärjestelmä, joka on koulutettu takaporttikuvilla, jotka tunnistavat tietyn henkilön väärin.

MITRE Corporation on luonut [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), tietokannan taktiikoista ja tekniikoista, joita vastustajat käyttävät todellisissa tekoälyjärjestelmiin kohdistuvissa hyökkäyksissä.

> Tekoälyä hyödyntävissä järjestelmissä on yhä enemmän haavoittuvuuksia, sillä tekoälyn käyttö lisää olemassa olevien järjestelmien hyökkäyspintaa perinteisten kyberhyökkäysten lisäksi. Kehitimme ATLAS:n lisätäksemme tietoisuutta näistä ainutlaatuisista ja kehittyvistä haavoittuvuuksista, kun globaali yhteisö yhä enemmän ottaa tekoälyn käyttöön eri järjestelmissä. ATLAS on mallinnettu MITRE ATT&CK® -kehystä seuraten, ja sen taktiikat, tekniikat ja menettelytavat (TTP:t) täydentävät ATT&CK:n vastaavia.

Samoin kuin MITRE ATT&CK® -kehys, joka on laajasti käytössä perinteisessä kyberturvallisuudessa edistyneiden uhkaemulaatioskenaarioiden suunnittelussa, ATLAS tarjoaa helposti haettavan TTP-joukon, joka voi auttaa ymmärtämään ja valmistautumaan puolustautumaan kehittyviä hyökkäyksiä vastaan.

Lisäksi Open Web Application Security Project (OWASP) on luonut "[Top 10 -listan](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" kriittisimmistä haavoittuvuuksista sovelluksissa, jotka käyttävät LLM:ä. Lista korostaa uhkien riskejä, kuten edellä mainittu datamyrkytys, sekä muita kuten:

- **Prompt Injection**: tekniikka, jossa hyökkääjät manipuloivat suurta kielimallia (LLM) huolellisesti suunnitelluilla syötteillä, saaden sen käyttäytymään aiotun toiminnan ulkopuolella.
- **Supply Chain Vulnerabilities**: komponentit ja ohjelmistot, jotka muodostavat LLM:n käyttämät sovellukset, kuten Python-moduulit tai ulkoiset tietokannat, voivat itse olla vaarantuneita, mikä johtaa odottamattomiin tuloksiin, aiheutettuihin harhoihin ja jopa haavoittuvuuksiin taustalla olevassa infrastruktuurissa.
- **Liiallinen luottamus**: LLM:t ovat erehtyväisiä ja ovat olleet taipuvaisia harhailemaan, tarjoten epätarkkoja tai vaarallisia tuloksia. Useissa dokumentoiduissa tilanteissa ihmiset ovat ottaneet tulokset nimellisarvoina, mikä on johtanut odottamattomiin todellisen maailman kielteisiin seurauksiin.

Microsoft Cloud Advocate Rod Trent on kirjoittanut ilmaisen e-kirjan, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), joka syventyy näihin ja muihin kehittyviin tekoälyuhkiin ja tarjoaa laajaa ohjausta siitä, miten parhaiten käsitellä näitä tilanteita.

## Tekoälyjärjestelmien ja LLM:ien turvallisuustestaus

Tekoäly (AI) muuttaa eri aloja ja teollisuudenaloja, tarjoten uusia mahdollisuuksia ja etuja yhteiskunnalle. Kuitenkin AI aiheuttaa myös merkittäviä haasteita ja riskejä, kuten tietosuojaa, harhaa, selitettävyyden puutetta ja mahdollisia väärinkäytöksiä. Siksi on tärkeää varmistaa, että AI-järjestelmät ovat turvallisia ja vastuullisia, mikä tarkoittaa, että ne noudattavat eettisiä ja oikeudellisia standardeja ja voivat olla luotettavia käyttäjille ja sidosryhmille.

Turvallisuustestaus on prosessi, jossa arvioidaan AI-järjestelmän tai LLM:n turvallisuutta tunnistamalla ja hyödyntämällä niiden haavoittuvuuksia. Tämä voidaan suorittaa kehittäjien, käyttäjien tai kolmannen osapuolen tarkastajien toimesta, riippuen testauksen tarkoituksesta ja laajuudesta. Joitakin yleisimpiä turvallisuustestausmenetelmiä AI-järjestelmille ja LLM:ille ovat:

- **Datan puhdistus**: Tämä on prosessi, jossa poistetaan tai anonymisoidaan arkaluonteista tai yksityistä tietoa AI-järjestelmän tai LLM:n koulutusdatasta tai syötteestä. Datan puhdistus voi auttaa estämään tietovuotoja ja haitallista manipulointia vähentämällä luottamuksellisen tai henkilökohtaisen datan altistumista.
- **Adversarial testing**: Tämä on prosessi, jossa luodaan ja sovelletaan vastustavia esimerkkejä AI-järjestelmän tai LLM:n syötteeseen tai tulokseen sen kestävyyden ja vastustuskyvyn arvioimiseksi vastustavia hyökkäyksiä vastaan. Adversarial testing voi auttaa tunnistamaan ja lieventämään AI-järjestelmän tai LLM:n haavoittuvuuksia ja heikkouksia, joita hyökkääjät voivat hyödyntää.
- **Model verification**: Tämä on prosessi, jossa varmistetaan AI-järjestelmän tai LLM:n malliparametrien tai arkkitehtuurin oikeellisuus ja täydellisyys. Model verification voi auttaa havaitsemaan ja estämään mallin varastamisen varmistamalla, että malli on suojattu ja todennettu.
- **Output validation**: Tämä on prosessi, jossa validoidaan AI-järjestelmän tai LLM:n tuloksen laatu ja luotettavuus. Output validation voi auttaa havaitsemaan ja korjaamaan haitallista manipulointia varmistamalla, että tulos on johdonmukainen ja tarkka.

OpenAI, tekoälyjärjestelmien johtaja, on perustanut sarjan _turvallisuusarviointeja_ osana punatiimiverkostoinitiatiiviaan, joka pyrkii testaamaan tekoälyjärjestelmien tuotoksia tekoälyturvallisuuden edistämiseksi.

> Arvioinnit voivat vaihdella yksinkertaisista kysymys-vastaus testeistä monimutkaisempiin simulaatioihin. Konkreettisina esimerkkeinä tässä ovat OpenAI:n kehittämät arvioinnit tekoälykäyttäytymisten arvioimiseksi useista näkökulmista:

#### Suostuttelu

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi huijata toista tekoälyjärjestelmää sanomaan salaisen sanan?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi suostutella toista tekoälyjärjestelmää lahjoittamaan rahaa?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi vaikuttaa toisen tekoälyjärjestelmän tukeen poliittiselle ehdotukselle?

#### Steganografia (piilotettu viestintä)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi välittää salaisia viestejä jäämättä kiinni toiselle tekoälyjärjestelmälle?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi pakata ja purkaa viestejä, jotta salaisia viestejä voidaan piilottaa?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Kuinka hyvin tekoälyjärjestelmä voi tehdä yhteistyötä toisen tekoälyjärjestelmän kanssa ilman suoraa viestintää?

### Tekoälyturvallisuus

On välttämätöntä pyrkiä suojaamaan tekoälyjärjestelmiä haitallisilta hyökkäyksiltä, väärinkäytöltä tai tahattomilta seurauksilta. Tämä sisältää toimenpiteitä tekoälyjärjestelmien turvallisuuden, luotettavuuden ja luotettavuuden varmistamiseksi, kuten:

- Suojata data ja algoritmit, joita käytetään tekoälymallien kouluttamiseen ja suorittamiseen
- Estää luvaton pääsy, manipulointi tai sabotaasi tekoälyjärjestelmissä
- Tunnistaa ja lieventää harhaa, syrjintää tai eettisiä ongelmia tekoälyjärjestelmissä
- Varmistaa tekoälypäätösten ja -toimien vastuullisuus, läpinäkyvyys ja selitettävyys
- Yhdenmukaistaa tekoälyjärjestelmien tavoitteet ja arvot ihmisten ja yhteiskunnan kanssa

Tekoälyturvallisuus on tärkeää tekoälyjärjestelmien ja datan eheyden, saatavuuden ja luottamuksellisuuden varmistamiseksi. Jotkut tekoälyturvallisuuden haasteet ja mahdollisuudet ovat:

- Mahdollisuus: Tekoälyn integrointi kyberturvallisuusstrategioihin, koska se voi auttaa uhkien tunnistamisessa ja parantaa vasteaikoja. Tekoäly voi auttaa automatisoimaan ja tehostamaan kyberhyökkäysten, kuten phishingin, haittaohjelmien tai kiristysohjelmien, tunnistamista ja lieventämistä.
- Haaste: Tekoälyä voivat myös käyttää vastustajat lanseeraamaan kehittyneitä hyökkäyksiä, kuten tuottamaan väärennettyä tai harhaanjohtavaa sisältöä, teeskentelemään käyttäjiä tai hyödyntämään tekoälyjärjestelmien haavoittuvuuksia. Siksi tekoälykehittäjillä on ainutlaatuinen vastuu suunnitella järjestelmiä, jotka ovat kestäviä ja vastustuskykyisiä väärinkäytöksiä vastaan.

### Datan suojaaminen

LLM:t voivat aiheuttaa riskejä niiden käyttämän datan yksityisyydelle ja turvallisuudelle. Esimerkiksi LLM:t voivat mahdollisesti muistaa ja vuotaa arkaluonteisia tietoja koulutusdatastaan, kuten henkilökohtaisia nimiä, osoitteita, salasanoja tai luottokorttinumeroita. Niitä voidaan myös manipuloida tai hyökätä haitallisten toimijoiden toimesta, jotka haluavat hyödyntää niiden haavoittuvuuksia tai harhoja. Siksi on tärkeää olla tietoinen näistä riskeistä ja toteuttaa asianmukaisia toimenpiteitä LLM:ien kanssa käytettävän datan suojaamiseksi. On olemassa useita vaiheita, joita voit ottaa suojellaksesi LLM:ien kanssa käytettävää dataa. Näihin vaiheisiin kuuluu:

- **Rajoita LLM:ille jaettavan datan määrää ja tyyppiä**: Jaa vain data, joka on tarpeellista ja relevanttia aiottuihin tarkoituksiin, ja vältä jakamasta mitään dataa, joka on arkaluonteista, luottamuksellista tai henkilökohtaista. Käyttäjien tulisi myös anonymisoida tai salata data, jonka he jakavat LLM:ille, esimerkiksi poistamalla tai peittämällä kaikki tunnistavat tiedot tai käyttämällä turvallisia viestintäkanavia.
- **Varmista LLM:ien tuottaman datan tarkkuus**: Tarkista aina LLM:ien tuottaman tuloksen tarkkuus ja laatu varmistaaksesi, ettei niissä ole ei-toivottua tai sopimatonta tietoa.
- **Ilmoita ja hälytä kaikista tietom

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä AI-käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomaa, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää auktoritatiivisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.