<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T09:56:48+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "fi"
}
-->
# Johdanto Generatiiviseen AI:hin ja Suuriin KieliMalleihin

_(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Generatiivinen AI on tekoäly, joka pystyy tuottamaan tekstiä, kuvia ja muita sisältötyyppejä. Se tekee siitä fantastisen teknologian, sillä se demokratisoi tekoälyn: kuka tahansa voi käyttää sitä pelkällä tekstikehotteella, lauseella luonnollisella kielellä. Sinun ei tarvitse oppia kieltä kuten Java tai SQL saavuttaaksesi jotain merkityksellistä, riittää kun käytät omaa kieltäsi, kerrot mitä haluat ja tekoälymalli antaa sinulle ehdotuksen. Sovellukset ja vaikutukset ovat valtavia: voit kirjoittaa tai ymmärtää raportteja, laatia sovelluksia ja paljon muuta sekunneissa.

Tässä opintokokonaisuudessa tutkimme, kuinka startupimme hyödyntää generatiivista AI:ta avatakseen uusia mahdollisuuksia opetuksen maailmassa ja kuinka käsittelemme sen soveltamiseen liittyviä sosiaalisia vaikutuksia ja teknologian rajoituksia.

## Johdanto

Tämä oppitunti käsittelee:

- Liiketoimintaskenaarion esittely: startup-ideamme ja missiomme.
- Generatiivinen AI ja kuinka päädyimme nykyiseen teknologiaympäristöön.
- Suuren kielimallin sisäinen toiminta.
- Suurten kielimallien pääominaisuudet ja käytännön käyttötapaukset.

## Oppimistavoitteet

Tämän oppitunnin jälkeen ymmärrät:

- Mitä generatiivinen AI on ja kuinka suuret kielimallit toimivat.
- Kuinka voit hyödyntää suuria kielimalleja eri käyttötapauksissa, keskittyen opetusskenaarioihin.

## Skenaariomme: koulutukseen keskittyvä startupimme

Generatiivinen tekoäly (AI) edustaa tekoälyteknologian huippua, venyttäen rajat siitä, mitä kerran pidettiin mahdottomana. Generatiivisilla AI-malleilla on useita kykyjä ja sovelluksia, mutta tässä opintokokonaisuudessa tutkimme, kuinka se mullistaa koulutuksen kuvitteellisen startupin kautta. Viittaamme tähän startupiin nimellä _startupimme_. Startupimme toimii koulutusalalla kunnianhimoisella missiolla

> _parantaa oppimisen saavutettavuutta maailmanlaajuisesti, varmistaen tasavertaisen pääsyn koulutukseen ja tarjoten henkilökohtaisia oppimiskokemuksia jokaiselle oppijalle heidän tarpeidensa mukaan_.

Startup-tiimimme on tietoinen siitä, että emme voi saavuttaa tätä tavoitetta ilman yhtä nykyajan voimakkaimmista työkaluista – Suuria KieliMalleja (LLM).

Generatiivisen AI:n odotetaan mullistavan oppimisen ja opettamisen tavat, sillä opiskelijoilla on käytössään virtuaaliopettajia 24 tuntia vuorokaudessa, jotka tarjoavat valtavan määrän tietoa ja esimerkkejä, ja opettajat voivat hyödyntää innovatiivisia työkaluja arvioidakseen oppilaitaan ja antaakseen palautetta.

Aloitetaan määrittelemällä joitakin peruskäsitteitä ja terminologiaa, joita käytämme koko opintokokonaisuuden ajan.

## Miten saimme Generatiivisen AI:n?

Huolimatta viimeaikaisesta generatiivisten AI-mallien aiheuttamasta _hypestä_, tämä teknologia on ollut vuosikymmeniä kehitteillä, ja ensimmäiset tutkimusyritykset ulottuvat 60-luvulle. Olemme nyt pisteessä, jossa AI:lla on ihmisen kognitiivisia kykyjä, kuten keskustelu, kuten esimerkiksi [OpenAI ChatGPT](https://openai.com/chatgpt) tai [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst) osoittavat, jotka myös käyttävät GPT-mallia verkkohakuihin Bing-keskusteluissa.

Palataan hieman taaksepäin: AI:n ensimmäiset prototyypit koostuivat kirjoituskoneella kirjoitetuista chatbot-ohjelmista, jotka perustuivat asiantuntijaryhmältä kerättyyn tietopohjaan ja esitettiin tietokoneella. Tietopohjan vastaukset käynnistyivät syötetyn tekstin avainsanoista. Kuitenkin pian kävi selväksi, että tällainen lähestymistapa, jossa käytetään kirjoituskoneella kirjoitettuja chatbot-ohjelmia, ei skaalautunut hyvin.

### Tilastollinen lähestymistapa AI:hin: Koneoppiminen

Käännekohta saapui 90-luvulla, kun tilastollista lähestymistapaa sovellettiin tekstianalyysiin. Tämä johti uusien algoritmien kehittämiseen – tunnetaan nimellä koneoppiminen – jotka pystyivät oppimaan kaavoja datasta ilman, että niitä ohjelmoitiin eksplisiittisesti. Tämä lähestymistapa mahdollisti koneiden simuloida ihmisen kielen ymmärtämistä: tilastollinen malli koulutetaan teksti-etiketti -parituksilla, jolloin malli pystyy luokittelemaan tuntemattoman syötetyn tekstin ennalta määritellyllä etiketillä, joka edustaa viestin tarkoitusta.

### Neuroverkot ja modernit virtuaaliassistentit

Viime vuosina laitteistojen teknologinen kehitys, joka pystyy käsittelemään suurempia datamääriä ja monimutkaisempia laskutoimituksia, kannusti AI-tutkimusta, mikä johti kehittyneiden koneoppimisalgoritmien kehittämiseen, jotka tunnetaan nimellä neuroverkot tai syväoppimisalgoritmit.

Neuroverkot (ja erityisesti toistuvat neuroverkot – RNN:t) paransivat merkittävästi luonnollisen kielen käsittelyä, mahdollistaen tekstin merkityksen esittämisen merkityksellisemmällä tavalla, arvostaen sanan kontekstia lauseessa.

Tämä on teknologia, joka voimaannutti uuden vuosituhannen ensimmäisellä vuosikymmenellä syntyneet virtuaaliassistentit, jotka olivat erittäin taitavia tulkitsemaan ihmisen kieltä, tunnistamaan tarpeen ja suorittamaan toiminnon sen tyydyttämiseksi – kuten vastaamalla ennalta määritellyllä käsikirjoituksella tai käyttämällä kolmannen osapuolen palvelua.

### Nykyhetki, Generatiivinen AI

Näin päädyimme Generatiiviseen AI:hin tänään, jota voidaan pitää syväoppimisen alaryhmänä.

Useiden vuosikymmenten tutkimuksen jälkeen AI-alalla uusi mallin arkkitehtuuri – nimeltään _Transformer_ – ylitti RNN:ien rajat, pystyessään ottamaan paljon pidempiä tekstijaksoja syötteenä. Transformerit perustuvat huomion mekanismiin, mikä mahdollistaa mallin antaa erilaisia painoja vastaanottamilleen syötteille, "kiinnittäen enemmän huomiota" kohtiin, joissa merkityksellisin tieto on keskittynyt, riippumatta niiden järjestyksestä tekstijaksossa.

Suurin osa viimeaikaisista generatiivisista AI-malleista – tunnetaan myös nimellä Suuret KieliMallit (LLM), koska ne toimivat tekstisyötteiden ja -tulosteiden kanssa – perustuu tähän arkkitehtuuriin. Mielenkiintoista näissä malleissa – jotka on koulutettu valtavalla määrällä merkitsemätöntä dataa erilaisista lähteistä kuten kirjoista, artikkeleista ja verkkosivustoista – on, että ne voidaan mukauttaa monenlaisiin tehtäviin ja tuottaa kieliopillisesti oikeaa tekstiä, jolla on luovuuden tuntua. Joten, ne eivät vain uskomattomasti parantaneet koneen kykyä "ymmärtää" syötetyn tekstin, vaan ne mahdollistivat kyvyn tuottaa alkuperäisen vastauksen ihmisen kielellä.

## Kuinka suuret kielimallit toimivat?

Seuraavassa luvussa tutkimme erilaisia Generatiivisia AI-malleja, mutta nyt katsotaan, kuinka suuret kielimallit toimivat, keskittyen OpenAI GPT (Generative Pre-trained Transformer) -malleihin.

- **Tokenizer, teksti numeroiksi**: Suuret KieliMallit saavat tekstin syötteenä ja tuottavat tekstin tulosteena. Kuitenkin, koska ne ovat tilastollisia malleja, ne toimivat paljon paremmin numeroiden kuin tekstijonojen kanssa. Siksi jokainen mallin syöte käsitellään tokenisoijalla ennen kuin sitä käytetään ydinmallissa. Token on tekstin osa – joka koostuu vaihtelevasta määrästä merkkejä, joten tokenisoijan päätehtävä on jakaa syöte tokenien taulukoksi. Sitten jokainen token yhdistetään token-indeksiin, joka on alkuperäisen tekstin osan kokonaislukuinen koodaus.

- **Tulostetokenien ennustaminen**: Annettuna n tokenia syötteenä (maksimi n vaihtelee mallista toiseen), malli pystyy ennustamaan yhden tokenin tulosteena. Tämä token sisällytetään sitten seuraavan iteraation syötteeseen laajenevan ikkunan mallin mukaisesti, mikä mahdollistaa paremman käyttäjäkokemuksen saada yksi (tai useampi) lause vastauksena. Tämä selittää, miksi, jos olet koskaan käyttänyt ChatGPT:tä, olet saattanut huomata, että joskus näyttää siltä, että se pysähtyy kesken lauseen.

- **Valintaprosessi, todennäköisyysjakauma**: Tulostetoken valitaan mallin mukaan sen todennäköisyyden perusteella esiintyä nykyisen tekstijonon jälkeen. Tämä johtuu siitä, että malli ennustaa todennäköisyysjakauman kaikille mahdollisille "seuraaville tokeneille", joka lasketaan sen koulutuksen perusteella. Kuitenkaan ei aina valita tokenia, jolla on korkein todennäköisyys tuloksena olevasta jakaumasta. Tähän valintaan lisätään satunnaisuuden aste, jotta malli toimii ei-deterministisesti - emme saa täsmälleen samaa tulosta samalle syötteelle. Tämä satunnaisuuden aste lisätään simuloimaan luovan ajattelun prosessia, ja sitä voidaan säätää mallin parametrista nimeltä lämpötila.

## Kuinka startupimme voi hyödyntää Suuria KieliMalleja?

Nyt kun ymmärrämme paremmin suuren kielimallin sisäisen toiminnan, katsotaan joitakin käytännön esimerkkejä yleisimmistä tehtävistä, joita ne voivat suorittaa melko hyvin, huomioiden liiketoimintaskenaarioomme.
Sanottiin, että suuren kielimallin pääkyky on _tuottaa tekstiä tyhjästä, alkaen tekstisyötteestä, joka on kirjoitettu luonnollisella kielellä_.

Mutta millainen tekstisyöte ja -tuloste?
Suuren kielimallin syöte tunnetaan nimellä kehotus, kun taas tuloste tunnetaan nimellä täydentäminen, termi, joka viittaa mallin mekanismiin luoda seuraava token täydentämään nykyinen syöte. Sukellamme syvälle siihen, mitä kehotus on ja kuinka suunnitella se niin, että saamme mallistamme kaiken irti. Mutta nyt sanottakoon, että kehotus voi sisältää:

- **Ohjeen**, joka määrittelee, millaista tulostetta odotamme mallilta. Tämä ohje voi joskus sisältää esimerkkejä tai lisätietoja.

  1. Artikkelin, kirjan, tuotearvostelujen ja muiden tiivistäminen sekä oivallusten poimiminen jäsentämättömästä datasta.
  
  2. Luova ideointi ja artikkelin, esseen, tehtävän tai muun suunnittelu.
  
- **Kysymyksen**, joka esitetään keskustelumuodossa agentin kanssa.
  
- **Tekstin osan täydentäminen**, joka implisiittisesti pyytää kirjoitusapua.
  
- **Koodin osan** yhdessä sen selittämisen ja dokumentoinnin pyynnön kanssa tai kommentin, joka pyytää tuottamaan koodinpätkän, joka suorittaa tietyn tehtävän.

Yllä olevat esimerkit ovat melko yksinkertaisia eivätkä ole tarkoitettu kattavaksi esitykseksi Suurten KieliMallien kyvyistä. Niiden tarkoitus on osoittaa generatiivisen AI:n potentiaali, erityisesti mutta ei rajoittuen opetuskonteksteihin.

Myös generatiivisen AI-mallin tulos ei ole täydellinen ja joskus mallin luovuus voi kääntyä sitä vastaan, mikä johtaa tulokseen, joka on yhdistelmä sanoja, jotka ihmiskäyttäjä voi tulkita todellisuuden mystifikaatioksi, tai se voi olla loukkaavaa. Generatiivinen AI ei ole älykäs - ainakaan älykkyyden laajemmassa määritelmässä, joka sisältää kriittisen ja luovan päättelyn tai tunneälyn; se ei ole deterministinen, eikä se ole luotettava, koska keksityt asiat, kuten virheelliset viittaukset, sisällöt ja lausunnot, voidaan yhdistää oikeaan tietoon ja esittää vakuuttavalla ja itsevarmalla tavalla. Seuraavissa oppitunneissa käsittelemme näitä rajoituksia ja näemme, mitä voimme tehdä niiden lieventämiseksi.

## Tehtävä

Tehtäväsi on lukea lisää [generatiivisesta AI:sta](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) ja yrittää tunnistaa alue, johon lisäisit generatiivisen AI:n tänään, jossa sitä ei vielä ole. Kuinka vaikutus eroaisi tekemisestä "vanhalla tavalla", voitko tehdä jotain, mitä et voinut ennen, vai oletko nopeampi? Kirjoita 300 sanan yhteenveto siitä, miltä unelmiesi AI-startup näyttäisi ja sisällytä otsikot kuten "Ongelma", "Kuinka käyttäisin AI:ta", "Vaikutus" ja halutessasi liiketoimintasuunnitelma.

Jos teit tämän tehtävän, saatat jopa olla valmis hakemaan Microsoftin inkubaattoriin, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) tarjoamme krediittejä sekä Azurelle, OpenAI:lle, mentorointia ja paljon muuta, tutustu!

## Tietämystarkistus

Mikä on totta suurista kielimalleista?

1. Saat täsmälleen saman vastauksen joka kerta.
2. Se tekee asiat täydellisesti, loistava lisäämään numeroita, tuottaa toimivaa koodia jne.
3. Vastaus voi vaihdella, vaikka käyttäisit samaa kehotusta. Se on myös loistava antamaan sinulle ensimmäisen luonnoksen jostakin, olipa se sitten tekstiä tai koodia. Mutta sinun on parannettava tuloksia.

A: 3, LLM on ei-deterministinen, vastaus vaihtelee, mutta voit hallita sen vaihtelua lämpötila-asetuksen avulla. Sinun ei myöskään pitäisi odottaa sen tekevän asioita täydellisesti, se on täällä tekemässä raskasta työtä puolestasi, mikä usein tarkoittaa, että saat hyvän ensimmäisen yrityksen jostakin, jota sinun on parannettava asteittain.

## Hienoa työtä! Jatka matkaa

Kun olet suorittanut tämän oppitunnin, tutustu [Generatiivisen AI:n oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generatiivisen AI:n tietosi kehittämistä!

Siirry oppitunnille 2, jossa tarkastelemme, kuinka [tutkia ja vertailla erilaisia LLM-tyyppejä](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttäen tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virheellisistä tulkinnoista.