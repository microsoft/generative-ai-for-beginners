<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d57fad773cbeb69c5dd62e65c34200d",
  "translation_date": "2025-10-17T19:41:15+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "fi"
}
-->
# Generatiivisen tekoälyn vastuullinen käyttö

[![Generatiivisen tekoälyn vastuullinen käyttö](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.fi.png)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon_

On helppo innostua tekoälystä ja erityisesti generatiivisesta tekoälystä, mutta on tärkeää miettiä, miten sitä käytetään vastuullisesti. On otettava huomioon esimerkiksi, miten varmistetaan, että tuotokset ovat oikeudenmukaisia, eivät vahingollisia ja paljon muuta. Tämä luku pyrkii tarjoamaan mainitun kontekstin, mitä tulee huomioida ja miten ryhtyä aktiivisiin toimiin tekoälyn käytön parantamiseksi.

## Johdanto

Tässä oppitunnissa käsitellään:

- Miksi vastuullinen tekoäly tulisi asettaa etusijalle generatiivisen tekoälyn sovelluksia rakennettaessa.
- Vastuullisen tekoälyn perusperiaatteet ja niiden yhteys generatiiviseen tekoälyyn.
- Miten näitä vastuullisen tekoälyn periaatteita voidaan soveltaa käytännössä strategioiden ja työkalujen avulla.

## Oppimistavoitteet

Oppitunnin jälkeen tiedät:

- Vastuullisen tekoälyn merkityksen generatiivisen tekoälyn sovelluksia rakennettaessa.
- Milloin ajatella ja soveltaa vastuullisen tekoälyn perusperiaatteita generatiivisen tekoälyn sovelluksia rakennettaessa.
- Mitä työkaluja ja strategioita on käytettävissä vastuullisen tekoälyn käsitteen toteuttamiseksi.

## Vastuullisen tekoälyn periaatteet

Generatiivisen tekoälyn innostus ei ole koskaan ollut suurempi. Tämä innostus on tuonut paljon uusia kehittäjiä, huomiota ja rahoitusta tälle alalle. Vaikka tämä on erittäin positiivista kaikille, jotka haluavat rakentaa tuotteita ja yrityksiä generatiivisen tekoälyn avulla, on myös tärkeää edetä vastuullisesti.

Tässä kurssissa keskitymme startupimme ja tekoälyyn liittyvän koulutustuotteemme rakentamiseen. Käytämme vastuullisen tekoälyn periaatteita: oikeudenmukaisuus, osallistavuus, luotettavuus/turvallisuus, tietoturva ja yksityisyys, läpinäkyvyys ja vastuuvelvollisuus. Näiden periaatteiden avulla tutkimme, miten ne liittyvät generatiivisen tekoälyn käyttöön tuotteissamme.

## Miksi sinun tulisi asettaa vastuullinen tekoäly etusijalle

Tuotetta rakentaessa ihmiskeskeinen lähestymistapa, jossa pidetään käyttäjän etu mielessä, johtaa parhaisiin tuloksiin.

Generatiivisen tekoälyn ainutlaatuisuus piilee sen kyvyssä luoda hyödyllisiä vastauksia, tietoa, ohjeita ja sisältöä käyttäjille. Tämä voidaan tehdä ilman monia manuaalisia vaiheita, mikä voi johtaa erittäin vaikuttaviin tuloksiin. Ilman asianmukaista suunnittelua ja strategioita tämä voi kuitenkin valitettavasti johtaa haitallisiin tuloksiin käyttäjille, tuotteellesi ja yhteiskunnalle kokonaisuudessaan.

Tarkastellaan joitakin (mutta ei kaikkia) näistä mahdollisesti haitallisista tuloksista:

### Harhat

Harhat ovat termi, jota käytetään kuvaamaan tilannetta, jossa LLM tuottaa sisältöä, joka on joko täysin järjetöntä tai jotain, jonka tiedämme olevan faktuaalisesti väärin muiden tietolähteiden perusteella.

Otetaan esimerkiksi tilanne, jossa rakennamme startupillemme ominaisuuden, joka mahdollistaa opiskelijoiden esittää historiallisia kysymyksiä mallille. Opiskelija kysyy kysymyksen `Kuka oli Titanicin ainoa selviytyjä?`

Malli tuottaa vastauksen, kuten alla:

![Kehote, jossa lukee "Kuka oli Titanicin ainoa selviytyjä"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Lähde: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Tämä on erittäin itsevarma ja perusteellinen vastaus. Valitettavasti se on virheellinen. Jo vähäisellä tutkimuksella huomaisi, että Titanicin katastrofista selviytyi useampi kuin yksi henkilö. Opiskelijalle, joka vasta aloittaa aiheen tutkimista, tämä vastaus voi olla tarpeeksi vakuuttava, ettei sitä kyseenalaisteta ja sitä pidetään faktana. Tämän seuraukset voivat johtaa siihen, että tekoälyjärjestelmä on epäluotettava ja vaikuttaa negatiivisesti startupimme maineeseen.

Jokaisen LLM:n iteraation myötä olemme nähneet suorituskyvyn parantumista harhojen minimoinnissa. Vaikka tämä parannus on tapahtunut, meidän sovellusten rakentajina ja käyttäjinä on silti oltava tietoisia näistä rajoituksista.

### Haitallinen sisältö

Käsittelimme aiemmassa osiossa tilannetta, jossa LLM tuottaa virheellisiä tai järjettömiä vastauksia. Toinen riski, josta meidän on oltava tietoisia, on tilanne, jossa malli vastaa haitallisella sisällöllä.

Haitallinen sisältö voidaan määritellä seuraavasti:

- Ohjeiden antaminen tai kannustaminen itsensä vahingoittamiseen tai tiettyjen ryhmien vahingoittamiseen.
- Vihamielinen tai halventava sisältö.
- Ohjeiden antaminen minkä tahansa tyyppisen hyökkäyksen tai väkivaltaisen teon suunnitteluun.
- Ohjeiden antaminen laittoman sisällön löytämiseen tai laittomien tekojen tekemiseen.
- Seksuaalisesti eksplisiittisen sisällön näyttäminen.

Startuppimme osalta haluamme varmistaa, että meillä on oikeat työkalut ja strategiat käytössä estääksemme tämän tyyppisen sisällön pääsyn opiskelijoiden nähtäville.

### Oikeudenmukaisuuden puute

Oikeudenmukaisuus määritellään "varmistamiseksi, että tekoälyjärjestelmä on vapaa ennakkoluuloista ja syrjinnästä ja että se kohtelee kaikkia oikeudenmukaisesti ja tasapuolisesti." Generatiivisen tekoälyn maailmassa haluamme varmistaa, että mallin tuotokset eivät vahvista syrjiviä maailmankatsomuksia marginalisoiduista ryhmistä.

Tämän tyyppiset tuotokset eivät ainoastaan tuhoa positiivisten tuotekokemusten rakentamista käyttäjillemme, vaan ne aiheuttavat myös lisää yhteiskunnallista haittaa. Sovellusten rakentajina meidän tulisi aina pitää laaja ja monimuotoinen käyttäjäkunta mielessä, kun rakennamme ratkaisuja generatiivisen tekoälyn avulla.

## Miten käyttää generatiivista tekoälyä vastuullisesti

Nyt kun olemme tunnistaneet vastuullisen generatiivisen tekoälyn merkityksen, tarkastellaan neljää askelta, joita voimme ottaa rakentaaksemme tekoälyratkaisujamme vastuullisesti:

![Vähentämisen sykli](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.fi.png)

### Mahdollisten haittojen mittaaminen

Ohjelmistotestauksessa testaamme käyttäjän odotettuja toimia sovelluksessa. Samoin monipuolisen joukon käyttäjien todennäköisesti käyttämiä kehotteita testaaminen on hyvä tapa mitata mahdollisia haittoja.

Koska startupimme rakentaa koulutustuotetta, olisi hyvä valmistella lista koulutukseen liittyvistä kehotteista. Tämä voisi kattaa tietyn aiheen, historialliset faktat ja kehotteet opiskelijaelämästä.

### Mahdollisten haittojen vähentäminen

On nyt aika löytää tapoja, joilla voimme estää tai rajoittaa mallin ja sen vastausten aiheuttamia mahdollisia haittoja. Voimme tarkastella tätä neljällä eri tasolla:

![Vähentämisen tasot](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.fi.png)

- **Malli**. Oikean mallin valitseminen oikeaan käyttötapaukseen. Suuremmat ja monimutkaisemmat mallit, kuten GPT-4, voivat aiheuttaa enemmän haitallisen sisällön riskiä, kun niitä sovelletaan pienempiin ja tarkempiin käyttötapauksiin. Koulutusdatan käyttäminen hienosäätöön vähentää myös haitallisen sisällön riskiä.

- **Turvajärjestelmä**. Turvajärjestelmä on joukko työkaluja ja konfiguraatioita mallia palvelevalla alustalla, jotka auttavat haittojen vähentämisessä. Esimerkki tästä on Azure OpenAI -palvelun sisällönsuodatusjärjestelmä. Järjestelmien tulisi myös havaita jailbreak-hyökkäykset ja ei-toivottu toiminta, kuten bottien pyynnöt.

- **Metakehote**. Metakehotteet ja ankkurointi ovat tapoja, joilla voimme ohjata tai rajoittaa mallia tiettyjen käyttäytymisten ja tietojen perusteella. Tämä voisi olla järjestelmän syötteiden käyttö mallin tiettyjen rajojen määrittämiseksi. Lisäksi voidaan tarjota tuotoksia, jotka ovat relevantimpia järjestelmän laajuudelle tai alalle.

Tämä voi myös olla tekniikoiden, kuten Retrieval Augmented Generation (RAG), käyttöä, jotta malli hakee tietoa vain valikoiduista luotettavista lähteistä. Kurssin myöhemmässä osassa on oppitunti [hakusovellusten rakentamisesta](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Käyttäjäkokemus**. Viimeinen taso on se, missä käyttäjä on suoraan vuorovaikutuksessa mallin kanssa sovelluksemme käyttöliittymän kautta jollain tavalla. Tällä tavoin voimme suunnitella käyttöliittymän/UX:n rajoittamaan käyttäjää lähettämästä mallille tietynlaisia syötteitä sekä rajoittaa käyttäjälle näytettävää tekstiä tai kuvia. Kun tekoälysovellus otetaan käyttöön, meidän on myös oltava läpinäkyviä siitä, mitä generatiivinen tekoälysovelluksemme voi ja ei voi tehdä.

Meillä on kokonainen oppitunti omistettu [tekoälysovellusten UX:n suunnittelulle](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Mallin arviointi**. LLM:ien kanssa työskentely voi olla haastavaa, koska meillä ei aina ole kontrollia mallin koulutuksessa käytettyyn dataan. Siitä huolimatta meidän tulisi aina arvioida mallin suorituskykyä ja tuotoksia. On edelleen tärkeää mitata mallin tarkkuutta, samankaltaisuutta, ankkurointia ja tuotoksen relevanssia. Tämä auttaa tarjoamaan läpinäkyvyyttä ja luottamusta sidosryhmille ja käyttäjille.

### Vastuullisen generatiivisen tekoälyratkaisun operointi

Operatiivisen käytännön rakentaminen tekoälysovellusten ympärille on viimeinen vaihe. Tämä sisältää yhteistyön muiden startupimme osien, kuten lakiosaston ja tietoturvan, kanssa varmistaaksemme, että noudatamme kaikkia sääntelypolitiikkoja. Ennen lanseerausta haluamme myös rakentaa suunnitelmat toimitusta, ongelmatilanteiden käsittelyä ja palautusta varten estääksemme käyttäjille aiheutuvia haittoja.

## Työkalut

Vaikka vastuullisten tekoälyratkaisujen kehittäminen saattaa tuntua työläältä, se on vaivan arvoista. Generatiivisen tekoälyn alueen kasvaessa kehittäjien työnkulkuun vastuullisuutta tehokkaasti integroivia työkaluja kehittyy yhä enemmän. Esimerkiksi [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) voi auttaa havaitsemaan haitallista sisältöä ja kuvia API-pyynnön avulla.

## Tietojen tarkistus

Mitä asioita sinun tulee ottaa huomioon varmistaaksesi vastuullisen tekoälyn käytön?

1. Että vastaus on oikein.
1. Haitallinen käyttö, ettei tekoälyä käytetä rikollisiin tarkoituksiin.
1. Varmistaminen, että tekoäly on vapaa ennakkoluuloista ja syrjinnästä.

V: 2 ja 3 ovat oikein. Vastuullinen tekoäly auttaa sinua pohtimaan, miten haitallisia vaikutuksia ja ennakkoluuloja voidaan vähentää ja paljon muuta.

## 🚀 Haaste

Lue lisää [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) -palvelusta ja katso, mitä voit ottaa käyttöön omassa toiminnassasi.

## Hienoa työtä, jatka oppimista

Kun olet suorittanut tämän oppitunnin, tutustu [Generatiivisen tekoälyn oppimiskokoelmaan](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn tietämyksesi kehittämistä!

Siirry oppituntiin 4, jossa tarkastelemme [kehotetekniikan perusteita](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.