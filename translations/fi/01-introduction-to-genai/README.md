<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:24:27+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "fi"
}
-->
# Johdanto Generatiiviseen tekoälyyn ja suurten kielimallien maailmaan

_(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Generatiivinen tekoäly on tekoälyä, joka pystyy luomaan tekstiä, kuvia ja muun tyyppistä sisältöä. Sen tekee fantastiseksi teknologiaksi se, että se demokratisoi tekoälyn käytön; kuka tahansa voi käyttää sitä pelkällä tekstikehotteella, luonnollisella kielellä kirjoitetulla lauseella. Sinun ei tarvitse oppia Java- tai SQL-kieltä saavuttaaksesi jotain merkittävää; tarvitset vain omaa kieltäsi, ilmaise mitä haluat ja tekoälymalli ehdottaa jotain. Sovellukset ja vaikutukset ovat valtavia: voit kirjoittaa tai ymmärtää raportteja, kirjoittaa sovelluksia ja paljon muuta, kaikki sekunneissa.

Tässä opetussuunnitelmassa tutkimme, kuinka startup-yrityksemme hyödyntää generatiivista tekoälyä avatakseen uusia skenaarioita opetuksen maailmassa ja kuinka käsittelemme sen soveltamiseen liittyviä sosiaalisia vaikutuksia ja teknologisia rajoituksia.

## Johdanto

Tämä oppitunti käsittelee:

- Liiketoimintaskenaarion esittely: startup-ideamme ja missiomme.
- Generatiivinen tekoäly ja kuinka päädyimme nykyiseen teknologiaympäristöön.
- Suuren kielimallin sisäinen toiminta.
- Suurten kielimallien pääominaisuudet ja käytännön sovelluskohteet.

## Oppimistavoitteet

Tämän oppitunnin jälkeen ymmärrät:

- Mitä generatiivinen tekoäly on ja kuinka suuret kielimallit toimivat.
- Kuinka voit hyödyntää suuria kielimalleja eri käyttötarkoituksissa, erityisesti opetusskenaarioissa.

## Skenaario: koulutusalustamme

Generatiivinen tekoäly edustaa tekoälyteknologian huippua, joka rikkoo rajoja siitä, mitä kerran pidettiin mahdottomana. Generatiivisilla tekoälymalleilla on useita kykyjä ja sovelluksia, mutta tässä opetussuunnitelmassa tutkimme, kuinka se mullistaa koulutusta kuvitteellisen startup-yrityksen kautta. Viittaamme tähän startup-yritykseen nimellä _meidän startup_. Meidän startup toimii koulutusalalla kunnianhimoisella missiolla

> _parantaa oppimisen saavutettavuutta maailmanlaajuisesti, varmistaa tasapuolinen pääsy koulutukseen ja tarjota henkilökohtaisia oppimiskokemuksia jokaiselle oppijalle heidän tarpeidensa mukaan_.

Startup-tiimimme on tietoinen siitä, ettemme pysty saavuttamaan tätä tavoitetta ilman yhden nykypäivän voimakkaimman työkalun hyödyntämistä – suuria kielimalleja (LLM).

Generatiivisen tekoälyn odotetaan mullistavan tavan, jolla opimme ja opetamme nykyään, kun opiskelijoilla on käytössään virtuaaliset opettajat 24 tuntia vuorokaudessa, jotka tarjoavat valtavia määriä tietoa ja esimerkkejä, ja opettajat voivat hyödyntää innovatiivisia työkaluja arvioidakseen opiskelijoitaan ja antaakseen palautetta.

Aloitetaan määrittelemällä joitain peruskäsitteitä ja terminologiaa, joita käytämme koko opetussuunnitelman ajan.

## Kuinka saimme generatiivisen tekoälyn?

Huolimatta viime aikoina generatiivisten tekoälymallien julkistamisen luomasta valtavasta _hypestä_, tämä teknologia on ollut kehitteillä vuosikymmeniä, ja ensimmäiset tutkimusyritykset juontavat juurensa 60-luvulle. Olemme nyt pisteessä, jossa tekoälyllä on ihmisen kognitiivisia kykyjä, kuten keskustelu, kuten esimerkiksi [OpenAI ChatGPT](https://openai.com/chatgpt) tai [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), joka käyttää myös GPT-mallia verkkohakuun Bing-keskusteluissa.

Palataan hieman taaksepäin: AI:n ensimmäiset prototyypit koostuivat kirjoituskoneella kirjoitetuista chatboteista, jotka perustuivat asiantuntijaryhmältä kerättyyn tietokantaan ja esitettiin tietokoneeseen. Tietokannan vastaukset laukaistiin avainsanoilla, jotka esiintyivät syötetyn tekstin sisällä. Kuitenkin pian kävi selväksi, että tällainen lähestymistapa, kirjoituskoneella kirjoitettujen chatbotien käyttö, ei skaalautunut hyvin.

### Tilastollinen lähestymistapa tekoälyyn: Koneoppiminen

Käännekohta saavutettiin 90-luvulla, kun tilastollinen lähestymistapa tekstianalyysiin otettiin käyttöön. Tämä johti uusien algoritmien kehittämiseen – tunnetaan nimellä koneoppiminen – jotka pystyivät oppimaan kaavoja datasta ilman, että niitä ohjelmoitiin eksplisiittisesti. Tämä lähestymistapa mahdollistaa koneiden simuloida ihmiskielen ymmärtämistä: tilastollinen malli koulutetaan tekstin ja sen merkityksen yhdistelmillä, jolloin malli pystyy luokittelemaan tuntemattoman syötetyn tekstin ennalta määritellyllä etiketillä, joka edustaa viestin tarkoitusta.

### Neuroverkot ja modernit virtuaaliavustajat

Viime vuosina laitteistojen teknologinen kehitys, joka pystyy käsittelemään suurempia määriä dataa ja monimutkaisempia laskelmia, on kannustanut tekoälytutkimusta, mikä on johtanut kehittyneiden koneoppimisalgoritmien, kuten neuroverkkojen tai syväoppimisalgoritmien, kehitykseen.

Neuroverkot (ja erityisesti toistuvat neuroverkot – RNN:t) paransivat merkittävästi luonnollisen kielen käsittelyä, mahdollistaen tekstin merkityksen esittämisen merkityksellisemmällä tavalla, arvostaen sanan kontekstia lauseessa.

Tämä on teknologia, joka voimisti virtuaaliavustajia, jotka syntyivät uuden vuosisadan ensimmäisellä vuosikymmenellä ja jotka ovat erittäin taitavia tulkitsemaan ihmiskieltä, tunnistamaan tarpeen ja suorittamaan toiminnon sen tyydyttämiseksi – kuten vastaamaan ennalta määritellyllä käsikirjoituksella tai käyttämällä kolmannen osapuolen palvelua.

### Nykyhetki, Generatiivinen tekoäly

Näin päädyimme nykyiseen generatiiviseen tekoälyyn, jota voidaan pitää syväoppimisen alaryhmänä.

Useiden vuosikymmenten tutkimuksen jälkeen tekoälyn alalla uusi mallirakenne – nimeltään _Transformer_ – ylitti RNN:ien rajoitukset, ollen kykenevä ottamaan paljon pidempiä tekstijonoja syötteenä. Transformerit perustuvat huomiointimekanismiin, joka mahdollistaa mallin antaa erilaisia painoarvoja syötteille, jotka se vastaanottaa, 'kiinnittäen enemmän huomiota' kohtiin, joissa merkityksellisin tieto on keskittynyt, riippumatta niiden järjestyksestä tekstijonossa.

Useimmat viimeaikaiset generatiiviset tekoälymallit – tunnetaan myös nimellä Suuret Kielimallit (LLM), koska ne toimivat tekstuaalisten syötteiden ja tulosteiden kanssa – perustuvat tähän arkkitehtuuriin. Näiden mallien mielenkiintoinen piirre – jotka on koulutettu valtavalla määrällä merkitsemätöntä dataa erilaisista lähteistä, kuten kirjoista, artikkeleista ja verkkosivustoista – on, että ne voidaan mukauttaa monenlaisiin tehtäviin ja ne voivat tuottaa kieliopillisesti oikeaa tekstiä, jossa on ripaus luovuutta. Ne eivät ainoastaan parantaneet koneen kykyä 'ymmärtää' syötetyn tekstin, vaan ne mahdollistivat sen kyvyn luoda alkuperäisen vastauksen ihmiskielellä.

## Kuinka suuret kielimallit toimivat?

Seuraavassa luvussa tutkimme erilaisia generatiivisia tekoälymalleja, mutta nyt tarkastellaan kuinka suuret kielimallit toimivat, keskittyen OpenAI GPT (Generative Pre-trained Transformer) -malleihin.

- **Tokenisaattori, teksti numeroiksi**: Suuret Kielimallit saavat tekstin syötteenä ja tuottavat tekstin tulosteena. Kuitenkin, koska ne ovat tilastollisia malleja, ne toimivat paljon paremmin numeroiden kuin tekstijonojen kanssa. Siksi jokainen mallille syötetty syöte käsitellään tokenisaattorin avulla ennen kuin se käytetään ydintoiminnossa. Token on tekstin osa – joka koostuu vaihtelevasta määrästä merkkejä, joten tokenisaattorin päätehtävä on jakaa syöte tokenien taulukoksi. Sitten jokainen token yhdistetään token-indeksiin, joka on alkuperäisen tekstiosan kokonaislukukoodaus.

- **Tulostokenien ennustaminen**: Annettuna n tokenia syötteenä (max n vaihtelee mallista toiseen), malli pystyy ennustamaan yhden tokenin tulosteena. Tämä token sisällytetään sitten seuraavan iteraation syötteeseen, laajenevan ikkunan mallissa, mahdollistaen paremman käyttäjäkokemuksen saada yksi (tai useampi) lause vastauksena. Tämä selittää, miksi, jos olet koskaan leikitellyt ChatGPT:llä, saatat olla huomannut, että joskus se näyttää pysähtyvän keskellä lausetta.

- **Valintaprosessi, todennäköisyysjakauma**: Tulostoken valitaan mallin mukaan sen todennäköisyyden perusteella esiintyä nykyisen tekstijonon jälkeen. Tämä johtuu siitä, että malli ennustaa todennäköisyysjakauman kaikille mahdollisille 'seuraaville tokeneille', joka lasketaan sen koulutuksen perusteella. Kuitenkaan ei aina valita todennäköisintä tokenia tuloksena olevasta jakaumasta. Tähän valintaan lisätään satunnaisuutta, siten että malli toimii ei-deterministisesti - emme saa täsmälleen samaa tulosta samalle syötteelle. Tämä satunnaisuuden aste lisätään simuloimaan luovaa ajattelua ja sitä voidaan säätää mallin parametrilla nimeltä lämpötila.

## Kuinka startupimme voi hyödyntää suuria kielimalleja?

Nyt kun ymmärrämme paremmin suuren kielimallin sisäistä toimintaa, katsotaan joitain käytännön esimerkkejä yleisimmistä tehtävistä, joita ne voivat suorittaa melko hyvin, huomioiden liiketoimintaskenaarion.

Sanottiin, että suuren kielimallin pääominaisuus on _luoda tekstiä tyhjästä, lähtien tekstuaalisesta syötteestä, joka on kirjoitettu luonnollisella kielellä_.

Mutta millaista tekstuaalista syötettä ja tulostetta?
Suuren kielimallin syöte tunnetaan kehotteena, kun taas tuloste tunnetaan täydentämisenä, termi, joka viittaa mallin mekanismiin tuottaa seuraava token täydentämään nykyisen syötteen. Tutustumme syvällisesti siihen, mitä kehotus on ja kuinka se suunnitellaan siten, että saamme mallistamme parhaan hyödyn. Mutta nyt, sanotaan vain, että kehotus voi sisältää:

- **Ohjeen**, joka määrittelee millaista tulostetta odotamme mallilta. Tämä ohje voi joskus sisältää joitain esimerkkejä tai lisätietoja.

  1. Artikkelin, kirjan, tuote-arvostelujen ja muiden tiivistelmä sekä oivallusten poimiminen jäsentämättömästä datasta.

  2. Luova ideointi ja artikkelin, esseen, tehtävän tai muun suunnittelu.

- **Kysymyksen**, joka esitetään keskusteluna agentin kanssa.

- **Täydennettävän tekstin osan**, joka implisiittisesti pyytää kirjoitusapua.

- **Koodin osan** yhdessä pyynnön kanssa selittää ja dokumentoida se, tai kommentti, joka pyytää tuottamaan koodinpätkän, joka suorittaa tietyn tehtävän.

Yllä olevat esimerkit ovat melko yksinkertaisia eivätkä ole tarkoitettu tyhjentäväksi esitykseksi suurten kielimallien kyvyistä. Ne on tarkoitettu osoittamaan generatiivisen tekoälyn käytön potentiaalia, erityisesti mutta ei rajoittuen opetuskonteksteihin.

Lisäksi generatiivisen tekoälymallin tulos ei ole täydellinen ja joskus mallin luovuus voi kääntyä sitä vastaan, mikä johtaa tulokseen, joka on yhdistelmä sanoja, jotka ihmiskäyttäjä voi tulkita todellisuuden vääristymäksi, tai se voi olla loukkaava. Generatiivinen tekoäly ei ole älykäs - ainakaan laajemmassa älykkyyden määritelmässä, joka sisältää kriittisen ja luovan päättelyn tai tunneälyn; se ei ole deterministinen, eikä se ole luotettava, koska virheellisiä viittauksia, sisältöä ja lausuntoja voidaan yhdistää oikeaan tietoon ja esittää vakuuttavalla ja itsevarmalla tavalla. Seuraavissa oppitunneissa käsittelemme kaikkia näitä rajoituksia ja näemme, mitä voimme tehdä niiden lieventämiseksi.

## Tehtävä

Tehtäväsi on lukea lisää [generatiivisesta tekoälystä](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) ja yrittää tunnistaa alue, johon lisäisit generatiivista tekoälyä tänään, jossa sitä ei vielä ole. Miten vaikutus eroaisi tekemällä se "vanhalla tavalla", voitko tehdä jotain, mitä et voinut ennen, vai oletko nopeampi? Kirjoita 300 sanan yhteenveto siitä, miltä unelmiesi tekoäly-startup näyttäisi ja sisällytä otsikot kuten "Ongelma", "Kuinka käyttäisin tekoälyä", "Vaikutus" ja halutessasi liiketoimintasuunnitelma.

Jos teit tämän tehtävän, saatat jopa olla valmis hakemaan Microsoftin inkubaattoriin, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) tarjoamme krediittejä sekä Azurelle, OpenAI:lle, mentorointia ja paljon muuta, tutustu!

## Tietotarkistus

Mikä pitää paikkansa suurista kielimalleista?

1. Saat täsmälleen saman vastauksen joka kerta.
1. Se tekee asiat täydellisesti, loistava numeroiden lisäämisessä, toimivan koodin tuottamisessa jne.
1. Vastaus voi vaihdella, vaikka käytettäisiin samaa kehotetta. Se on myös loistava antamaan sinulle ensimmäisen luonnoksen jostain, olipa se sitten tekstiä tai koodia. Mutta sinun täytyy parantaa tuloksia.

A: 3, LLM on ei-deterministinen, vastaus vaihtelee, kuitenkin, voit hallita sen vaihtelua lämpötila-asetuksella. Sinun ei myöskään pitäisi odottaa sen tekevän asioita täydellisesti, se on täällä tekemässä raskasta työtä puolestasi, mikä usein tarkoittaa, että saat hyvän ensimmäisen yrityksen jostain, jota sinun täytyy vähitellen parantaa.

## Hienoa työtä! Jatka matkaa

Tämän oppitunnin jälkeen tutustu [Generatiivinen tekoäly -oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyosaamisesi kehittämistä!

Siirry oppituntiin 2, jossa tarkastelemme kuinka [tutkia ja vertailla erilaisia LLM-tyyppejä](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä AI-käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää auktoritatiivisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa mahdollisista väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.