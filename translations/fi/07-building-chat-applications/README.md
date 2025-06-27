<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea4bbe640847aafbbba14dae4625e9af",
  "translation_date": "2025-06-25T15:41:13+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "fi"
}
-->
# Generatiiviseen tekoälyyn perustuvien chat-sovellusten rakentaminen

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Nyt kun olemme nähneet, miten tekstin tuottamiseen tarkoitettuja sovelluksia voidaan rakentaa, tarkastellaan chat-sovelluksia.

Chat-sovellukset ovat tulleet osaksi jokapäiväistä elämäämme, tarjoten enemmän kuin pelkän välineen rentoon keskusteluun. Ne ovat olennainen osa asiakaspalvelua, teknistä tukea ja jopa kehittyneitä neuvontajärjestelmiä. On todennäköistä, että olet saanut apua chat-sovelluksesta melko hiljattain. Kun integroimme kehittyneempiä teknologioita, kuten generatiivista tekoälyä, näihin alustoihin, monimutkaisuus kasvaa ja samoin haasteet.

Joihinkin kysymyksiin, jotka meidän on vastattava, kuuluvat:

- **Sovelluksen rakentaminen**. Miten voimme tehokkaasti rakentaa ja saumattomasti integroida nämä tekoälypohjaiset sovellukset tiettyihin käyttötapauksiin?
- **Valvonta**. Kun sovellukset on otettu käyttöön, miten voimme valvoa ja varmistaa, että ne toimivat korkeimmalla laatutasolla, sekä toiminnallisuuden että [tekoälyn vastuullisuuden kuuden periaatteen](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) noudattamisen suhteen?

Kun siirrymme eteenpäin aikaan, jota määrittää automaatio ja saumattomat ihmisen ja koneen väliset vuorovaikutukset, generatiivisen tekoälyn vaikutuksen ymmärtäminen chat-sovellusten laajuuteen, syvyyteen ja mukautuvuuteen tulee olennaiseksi. Tämä oppitunti tutkii näitä monimutkaisia järjestelmiä tukevan arkkitehtuurin näkökulmia, syventyy menetelmiin niiden hienosäätämiseksi alakohtaisiin tehtäviin ja arvioi mittareita ja näkökohtia, jotka ovat olennaisia vastuullisen tekoälyn käyttöönoton varmistamiseksi.

## Johdanto

Tämä oppitunti kattaa:

- Tekniikoita chat-sovellusten tehokkaaseen rakentamiseen ja integrointiin.
- Miten sovelluksiin sovelletaan räätälöintiä ja hienosäätöä.
- Strategioita ja näkökohtia chat-sovellusten tehokkaaseen valvontaan.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Kuvata chat-sovellusten rakentamisen ja integroinnin näkökohtia olemassa oleviin järjestelmiin.
- Räätälöidä chat-sovelluksia tiettyihin käyttötapauksiin.
- Tunnistaa avainmittarit ja näkökohtia tekoälypohjaisten chat-sovellusten laadun tehokkaaseen valvontaan ja ylläpitoon.
- Varmistaa, että chat-sovellukset hyödyntävät tekoälyä vastuullisesti.

## Generatiivisen tekoälyn integrointi chat-sovelluksiin

Chat-sovellusten parantaminen generatiivisella tekoälyllä ei keskity vain niiden älykkäämmäksi tekemiseen; se koskee niiden arkkitehtuurin, suorituskyvyn ja käyttöliittymän optimointia laadukkaan käyttäjäkokemuksen tarjoamiseksi. Tämä sisältää arkkitehtuurin perustan, API-integraatioiden ja käyttöliittymän näkökohtien tutkimisen. Tämä osio pyrkii tarjoamaan sinulle kattavan tiekartan näiden monimutkaisten maisemien navigointiin, olipa kyseessä niiden liittäminen olemassa oleviin järjestelmiin tai niiden rakentaminen itsenäisinä alustoina.

Tämän osion lopussa sinulla on tarvittava asiantuntemus chat-sovellusten tehokkaaseen rakentamiseen ja integrointiin.

### Chatbot vai chat-sovellus?

Ennen kuin sukellamme chat-sovellusten rakentamiseen, vertaillaan 'chatbotteja' ja 'tekoälypohjaisia chat-sovelluksia', jotka palvelevat erillisiä rooleja ja toimintoja. Chatbotin pääasiallinen tarkoitus on automatisoida tiettyjä keskustelutehtäviä, kuten usein kysyttyihin kysymyksiin vastaaminen tai paketin seuranta. Sitä ohjaa tyypillisesti sääntöihin perustuva logiikka tai monimutkaiset tekoälyalgoritmit. Tekoälypohjainen chat-sovellus puolestaan on paljon laajempi ympäristö, joka on suunniteltu helpottamaan erilaisia digitaalisen viestinnän muotoja, kuten tekstin, äänen ja videokeskusteluja ihmiskäyttäjien kesken. Sen määrittelevä piirre on generatiivisen tekoälymallin integrointi, joka simuloi vivahteikkaita, ihmismäisiä keskusteluja, tuottaen vastauksia monenlaisten syötteiden ja kontekstuaalisten vihjeiden perusteella. Generatiivinen tekoälypohjainen chat-sovellus voi osallistua avoimen alueen keskusteluihin, mukautua kehittyviin keskustelukonteksteihin ja jopa tuottaa luovia tai monimutkaisia dialogeja.

Alla oleva taulukko esittää keskeiset erot ja yhtäläisyydet, jotka auttavat meitä ymmärtämään niiden ainutlaatuiset roolit digitaalisessa viestinnässä.

| Chatbot                               | Generatiivinen tekoälypohjainen chat-sovellus |
| ------------------------------------- | --------------------------------------------- |
| Tehtäväkeskeinen ja sääntöihin perustuva | Kontekstia huomioiva                         |
| Usein integroituna suurempiin järjestelmiin | Voi isännöidä yhtä tai useampaa chatbotia    |
| Rajoittuu ohjelmoituihin toimintoihin  | Sisältää generatiivisia tekoälymalleja        |
| Erikoistuneet & rakenteelliset vuorovaikutukset | Pystyy avoimen alueen keskusteluihin        |

### Valmiiden toimintojen hyödyntäminen SDK:iden ja API:iden avulla

Kun rakennat chat-sovellusta, hyvä ensimmäinen askel on arvioida, mitä on jo olemassa. SDK:iden ja API:iden käyttö chat-sovellusten rakentamisessa on edullinen strategia useista syistä. Integroimalla hyvin dokumentoituja SDK:ita ja API:ita, sijoitat sovelluksesi strategisesti pitkäaikaiseen menestykseen, käsitellen skaalautuvuus- ja ylläpitohuolia.

- **Kehitysprosessin nopeuttaminen ja kustannusten vähentäminen**: Luottamalla valmiisiin toimintoihin sen sijaan, että rakennat ne itse kalliilla prosessilla, voit keskittyä muihin sovelluksesi osa-alueisiin, joita pidät tärkeämpinä, kuten liiketoimintalogiikkaan.
- **Parempi suorituskyky**: Kun rakennat toiminnallisuutta alusta alkaen, kysyt lopulta itseltäsi "Miten se skaalautuu? Onko tämä sovellus kykenevä käsittelemään äkillistä käyttäjämäärän nousua?" Hyvin ylläpidetyt SDK:t ja API:t sisältävät usein ratkaisuja näihin huoliin.
- **Helpompi ylläpito**: Päivitykset ja parannukset on helpompi hallita, koska useimmat API:t ja SDK:t vaativat yksinkertaisesti kirjaston päivityksen, kun uudempi versio julkaistaan.
- **Pääsy huipputeknologiaan**: Mallien hyödyntäminen, joita on hienosäädetty ja koulutettu laajoilla tietoaineistoilla, tarjoaa sovelluksellesi luonnollisen kielen kyvykkyyksiä.

SDK:n tai API:n toiminnallisuuden käyttöön ottaminen edellyttää tyypillisesti lupaa tarjottujen palveluiden käyttöön, mikä tapahtuu usein ainutlaatuisen avaimen tai todennustunnuksen avulla. Käytämme OpenAI Python-kirjastoa tutkiaksemme, miltä tämä näyttää. Voit kokeilla sitä itse seuraavassa [OpenAI:n muistikirjassa](../../../07-building-chat-applications/python/oai-assignment.ipynb) tai [Azure OpenAI Services -muistikirjassa](../../../07-building-chat-applications/python/aoai-assignment.ipynb) tämän oppitunnin yhteydessä.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Yllä oleva esimerkki käyttää GPT-3.5 Turbo -mallia kehotteen täydentämiseen, mutta huomaa, että API-avain asetetaan ennen kuin tämä tehdään. Saat virheen, jos et aseta avainta.

## Käyttäjäkokemus (UX)

Yleiset UX-periaatteet pätevät chat-sovelluksiin, mutta tässä on joitain lisänäkökohtia, jotka tulevat erityisen tärkeiksi koneoppimiskomponenttien vuoksi.

- **Keino epäselvyyden käsittelyyn**: Generatiiviset tekoälymallit tuottavat joskus epäselviä vastauksia. Ominaisuus, joka sallii käyttäjien pyytää selvennystä, voi olla hyödyllinen, jos he kohtaavat tämän ongelman.
- **Kontekstin säilyttäminen**: Kehittyneet generatiiviset tekoälymallit kykenevät muistamaan keskustelun kontekstin, mikä voi olla tarpeellinen lisä käyttäjäkokemukseen. Antamalla käyttäjille mahdollisuus hallita ja ohjata kontekstia parantaa käyttäjäkokemusta, mutta tuo mukanaan riskin herkkien käyttäjätietojen säilyttämisestä. Harkinnat siitä, kuinka kauan tämä tieto säilytetään, kuten säilytyspolitiikan käyttöönotto, voi tasapainottaa kontekstin tarpeen yksityisyyden kanssa.
- **Personointi**: Kyky oppia ja mukautua tarjoaa tekoälymalleille yksilöllisen kokemuksen käyttäjälle. Käyttäjäprofiilien kaltaisten ominaisuuksien avulla räätälöity käyttäjäkokemus ei ainoastaan saa käyttäjän tuntemaan itsensä ymmärretyksi, vaan se myös auttaa heitä löytämään erityisiä vastauksia, luoden tehokkaamman ja tyydyttävämmän vuorovaikutuksen.

Yksi esimerkki personoinnista on OpenAI:n ChatGPT:n "Custom instructions" -asetukset. Sen avulla voit antaa tietoja itsestäsi, jotka voivat olla tärkeitä konteksteja kehotteillesi. Tässä on esimerkki mukautetusta ohjeesta.

Tämä "profiili" kehottaa ChatGPT:tä luomaan oppituntisuunnitelman linkkilistoista. Huomaa, että ChatGPT ottaa huomioon, että käyttäjä saattaa haluta syvällisemmän oppituntisuunnitelman hänen kokemuksensa perusteella.

### Microsoftin järjestelmäviestikehys suurille kielimalleille

[Microsoft on antanut ohjeita](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) tehokkaiden järjestelmäviestien kirjoittamiseen LLM:ien vastauksia generoitaessa, jaettuna neljään alueeseen:

1. Määrittele, kenelle malli on tarkoitettu, sekä sen kyvyt ja rajoitukset.
2. Määrittele mallin ulostulomuoto.
3. Tarjoa erityisiä esimerkkejä, jotka osoittavat mallin tarkoitetun käyttäytymisen.
4. Tarjoa lisäkäyttäytymisen ohjausrajoja.

### Saavutettavuus

Olipa käyttäjällä visuaalisia, auditiivisia, motorisia tai kognitiivisia häiriöitä, hyvin suunniteltu chat-sovellus pitäisi olla kaikkien käytettävissä. Seuraava lista jakaa erityisiä ominaisuuksia, jotka on suunniteltu parantamaan saavutettavuutta eri käyttäjähäiriöille.

- **Ominaisuudet visuaalisille häiriöille**: Korkean kontrastin teemat ja säädettävä teksti, näytönlukijan yhteensopivuus.
- **Ominaisuudet auditiivisille häiriöille**: Teksti-puheeksi ja puhe-tekstiksi toiminnot, visuaaliset vihjeet äänimuistutuksille.
- **Ominaisuudet motorisille häiriöille**: Näppäimistön navigointituki, äänikomennot.
- **Ominaisuudet kognitiivisille häiriöille**: Yksinkertaistetut kielivaihtoehdot.

## Räätälöinti ja hienosäätö alakohtaisille kielimalleille

Kuvittele chat-sovellus, joka ymmärtää yrityksesi jargonia ja ennakoi käyttäjäkuntansa yleisesti esittämiä kysymyksiä. On olemassa muutamia lähestymistapoja, jotka kannattaa mainita:

- **DSL-mallien hyödyntäminen**. DSL tarkoittaa alakohtaista kieltä. Voit hyödyntää niin sanottua DSL-mallia, joka on koulutettu tietyllä alalla ymmärtämään sen käsitteitä ja skenaarioita.
- **Hienosäädön soveltaminen**. Hienosäätö on prosessi, jossa mallia koulutetaan edelleen erityisellä datalla.

## Räätälöinti: DSL:n käyttö

Alakohtaisten kielimallien (DSL-mallien) hyödyntäminen voi parantaa käyttäjien sitoutumista tarjoamalla erikoistuneita, kontekstiin liittyviä vuorovaikutuksia. Se on malli, joka on koulutettu tai hienosäädetty ymmärtämään ja tuottamaan tekstiä, joka liittyy tiettyyn alaan, teollisuuteen tai aiheeseen. Vaihtoehdot DSL-mallin käyttämiseen voivat vaihdella sellaisen kouluttamisesta alusta alkaen, valmiiden mallien käyttämiseen SDK:iden ja API:iden kautta. Toinen vaihtoehto on hienosäätö, joka tarkoittaa olemassa olevan valmiiksi koulutetun mallin ottamista ja sen mukauttamista tietylle alalle.

## Räätälöinti: Hienosäätö

Hienosäätöä harkitaan usein, kun valmiiksi koulutettu malli ei riitä erikoistuneella alalla tai tietyssä tehtävässä.

Esimerkiksi lääketieteelliset kyselyt ovat monimutkaisia ja vaativat paljon kontekstia. Kun lääketieteen ammattilainen diagnosoi potilasta, se perustuu monenlaisiin tekijöihin, kuten elämäntapaan tai olemassa oleviin sairauksiin, ja saattaa jopa luottaa viimeaikaisiin lääketieteellisiin julkaisuihin diagnoosin vahvistamiseksi. Tällaisissa vivahteikkaissa skenaarioissa yleiskäyttöinen tekoälypohjainen chat-sovellus ei voi olla luotettava lähde.

### Skenaario: lääketieteellinen sovellus

Kuvittele chat-sovellus, joka on suunniteltu auttamaan lääketieteen ammattilaisia tarjoamalla nopeita viittauksia hoitosuosituksiin, lääkeinteraktioihin tai viimeaikaisiin tutkimustuloksiin.

Yleiskäyttöinen malli saattaa olla riittävä vastaamaan peruslääketieteellisiin kysymyksiin tai antamaan yleisiä neuvoja, mutta se saattaa kamppailla seuraavien kanssa:

- **Erittäin spesifiset tai monimutkaiset tapaukset**. Esimerkiksi neurologi saattaa kysyä sovellukselta: "Mitkä ovat nykyiset parhaat käytännöt lääkeresistentin epilepsian hoidossa lapsipotilailla?"
- **Viimeaikaisten edistysaskelien puute**. Yleiskäyttöinen malli voisi kamppailla tarjotakseen ajankohtaisen vastauksen, joka sisältää viimeisimmät edistysaskeleet neurologiassa ja farmakologiassa.

Tällaisissa tapauksissa mallin hienosäätö erikoistuneella lääketieteellisellä tietoaineistolla voi merkittävästi parantaa sen kykyä käsitellä näitä monimutkaisia lääketieteellisiä kyselyitä tarkemmin ja luotettavammin. Tämä vaatii pääsyn laajaan ja asiaankuuluvaan tietoaineistoon, joka edustaa alakohtaisia haasteita ja kysymyksiä, jotka tarvitsevat ratkaisemista.

## Näkökohdat korkealaatuiselle tekoälypohjaiselle chat-kokemukselle

Tämä osio esittää "korkealaatuisen" chat-sovelluksen kriteerit, jotka sisältävät toiminnallisten mittareiden keräämisen ja kehyksen noudattamisen, joka vastuullisesti hyödyntää tekoälyteknologiaa.

### Keskeiset mittarit

Sovelluksen korkealaatuisen suorituskyvyn ylläpitämiseksi on olennaista seurata keskeisiä mittareita ja näkökohtia. Nämä mittaukset eivät ainoastaan varmistaa sovelluksen toiminnallisuutta, vaan myös arvioivat tekoälymallin ja käyttäjäkokemuksen laatua. Alla on lista, joka kattaa perus-, tekoäly- ja käyttäjäkokemuksen mittareita, joita kannattaa harkita.

| Mittari                        | Määritelmä                                                                                                           | Näkökohdat chat-kehittäjälle                                              |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Käyttöa

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.