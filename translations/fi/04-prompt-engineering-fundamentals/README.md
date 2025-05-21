<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T15:48:21+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "fi"
}
-->
# Prompt Engineering - Perusteet

## Johdanto

Tässä moduulissa käsitellään keskeisiä käsitteitä ja tekniikoita tehokkaiden kehotteiden luomiseksi generatiivisissa tekoälymalleissa. Tapa, jolla kirjoitat kehotteesi LLM:lle, on myös tärkeä. Huolellisesti laadittu kehotus voi parantaa vastausten laatua. Mutta mitä tarkalleen ottaen tarkoittavat termit _kehotus_ ja _kehotussuunnittelu_? Ja miten voin parantaa LLM:lle lähettämääni kehotteen _sisältöä_? Näihin kysymyksiin pyrimme vastaamaan tässä ja seuraavassa luvussa.

_Generatiivinen tekoäly_ kykenee luomaan uutta sisältöä (esim. tekstiä, kuvia, ääntä, koodia jne.) käyttäjän pyyntöjen perusteella. Tämä saavutetaan _laajojen kielimallien_ avulla, kuten OpenAI:n GPT-sarjan ("Generative Pre-trained Transformer") avulla, jotka on koulutettu käyttämään luonnollista kieltä ja koodia.

Käyttäjät voivat nyt olla vuorovaikutuksessa näiden mallien kanssa tutuilla tavoilla, kuten chatin avulla, ilman teknistä osaamista tai koulutusta. Mallit ovat _kehotuspohjaisia_ - käyttäjät lähettävät tekstisyötteen (kehotus) ja saavat takaisin tekoälyn vastauksen (täydentäminen). He voivat sitten "keskustella tekoälyn kanssa" iteratiivisesti, monikierroksisissa keskusteluissa, hienosäätäen kehotettaan, kunnes vastaus vastaa heidän odotuksiaan.

"Kehotteet" ovat nyt ensisijainen _ohjelmointirajapinta_ generatiivisille tekoälysovelluksille, kertoen malleille, mitä tehdä ja vaikuttaen palautettujen vastausten laatuun. "Kehotussuunnittelu" on nopeasti kasvava tutkimusalue, joka keskittyy kehotteiden _suunnitteluun ja optimointiin_ tuottamaan johdonmukaisia ja laadukkaita vastauksia laajassa mittakaavassa.

## Oppimistavoitteet

Tässä oppitunnissa opimme, mitä kehotussuunnittelu on, miksi se on tärkeää ja miten voimme luoda tehokkaampia kehotteita tietylle mallille ja sovellustavoitteelle. Ymmärrämme kehotussuunnittelun keskeiset käsitteet ja parhaat käytännöt - ja opimme interaktiivisesta Jupyter Notebooks -"hiekkalaatikko" -ympäristöstä, jossa voimme nähdä nämä käsitteet sovellettuna todellisiin esimerkkeihin.

Oppitunnin lopussa pystymme:

1. Selittämään, mitä kehotussuunnittelu on ja miksi se on tärkeää.
2. Kuvailemaan kehotteen osat ja niiden käyttötavat.
3. Oppimaan parhaat käytännöt ja tekniikat kehotussuunnitteluun.
4. Soveltamaan opittuja tekniikoita todellisiin esimerkkeihin käyttäen OpenAI-päätepistettä.

## Keskeiset termit

Kehotussuunnittelu: Käytäntö suunnitella ja hienosäätää syötteitä ohjaamaan tekoälymalleja tuottamaan haluttuja tuloksia.
Tokenisointi: Prosessi, jossa teksti muunnetaan pienemmiksi yksiköiksi, joita kutsutaan tokeneiksi, joita malli voi ymmärtää ja käsitellä.
Ohjeistuksella hienosäädetyt LLM:t: Laajennetut kielimallit (LLM:t), joita on hienosäädetty erityisillä ohjeilla parantamaan niiden vastausten tarkkuutta ja merkityksellisyyttä.

## Oppimishiekkalaatikko

Kehotussuunnittelu on tällä hetkellä enemmän taidetta kuin tiedettä. Paras tapa parantaa intuitiotamme siitä on _harjoitella enemmän_ ja omaksua kokeilu- ja erehdyslähestymistapa, joka yhdistää sovellusalueen asiantuntemuksen suositeltuihin tekniikoihin ja mallikohtaisiin optimointeihin.

Tämän oppitunnin mukana tuleva Jupyter Notebook tarjoaa _hiekkalaatikko_ -ympäristön, jossa voit kokeilla oppimaasi - joko matkan varrella tai osana koodin haasteita lopussa. Harjoitusten suorittamiseen tarvitset:

1. **Azure OpenAI API -avain** - palvelupäätepiste käyttöönotetulle LLM:lle.
2. **Python-ajonaika** - jossa Notebook voidaan suorittaa.
3. **Paikalliset ympäristömuuttujat** - _suorita [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) vaiheet nyt valmistautuaksesi_.

Notebook sisältää _aloitus_ -harjoituksia - mutta sinua kannustetaan lisäämään omia _Markdown_ (kuvaus) ja _Code_ (kehotuspyynnöt) osioita kokeillaksesi enemmän esimerkkejä tai ideoita - ja kehittääksesi intuitiotasi kehotussuunnittelussa.

## Kuvitettu opas

Haluatko saada yleiskuvan siitä, mitä tämä oppitunti kattaa ennen kuin sukellat sisään? Tutustu tähän kuvitettuun oppaaseen, joka antaa sinulle käsityksen tärkeimmistä aiheista, joita käsitellään, ja keskeisistä havainnoista, joita sinun tulisi pohtia kussakin niistä. Oppitunnin tiekartta vie sinut ydinajatusten ja haasteiden ymmärtämisestä niiden käsittelyyn asiaankuuluvilla kehotussuunnittelutekniikoilla ja parhailla käytännöillä. Huomaa, että tämän oppaan "Edistyneet tekniikat" -osio viittaa seuraavan luvun sisältöön tässä opetussuunnitelmassa.

## Startup-yrityksemme

Keskustellaan nyt siitä, miten _tämä aihe_ liittyy startup-yrityksemme tehtävään [tuoda tekoälyinnovaatioita koulutukseen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Haluamme rakentaa tekoälypohjaisia sovelluksia _henkilökohtaiseen oppimiseen_ - joten mietitään, miten eri käyttäjät sovelluksessamme saattavat "suunnitella" kehotteita:

- **Ylläpitäjät** saattavat pyytää tekoälyä _analysoimaan opetussuunnitelman tietoja katvealueiden tunnistamiseksi_. Tekoäly voi tiivistää tulokset tai visualisoida ne koodin avulla.
- **Opettajat** saattavat pyytää tekoälyä _luomaan oppituntisuunnitelman kohdeyleisölle ja aiheelle_. Tekoäly voi rakentaa henkilökohtaisen suunnitelman määritellyssä muodossa.
- **Oppilaat** saattavat pyytää tekoälyä _opettamaan heitä vaikeassa aiheessa_. Tekoäly voi nyt opastaa oppilaita oppitunneilla, vihjeillä ja esimerkeillä, jotka on räätälöity heidän tasolleen.

Tämä on vain jäävuoren huippu. Tutustu [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - avoimen lähdekoodin kehotekirjastoon, jonka ovat kuratoineet koulutuksen asiantuntijat - saadaksesi laajemman käsityksen mahdollisuuksista! _Kokeile ajaa joitain näistä kehotteista hiekkalaatikossa tai käyttämällä OpenAI Playgroundia nähdäksesi, mitä tapahtuu!_

## Mitä on kehotussuunnittelu?

Aloitimme tämän oppitunnin määrittelemällä **kehotussuunnittelun** prosessiksi, jossa _suunnitellaan ja optimoidaan_ tekstisyötteitä (kehotteita) tuottamaan johdonmukaisia ja laadukkaita vastauksia (täydentämisiä) tietylle sovellustavoitteelle ja mallille. Voimme ajatella tätä kaksivaiheisena prosessina:

- _suunnitellaan_ alkuperäinen kehotus tietylle mallille ja tavoitteelle
- _hienosäädetään_ kehotusta iteratiivisesti parantamaan vastauksen laatua

Tämä on välttämättä kokeilu- ja erehdysprosessi, joka vaatii käyttäjän intuitiota ja vaivannäköä optimaalisten tulosten saavuttamiseksi. Miksi se sitten on tärkeää? Vastaamme tähän kysymykseen ymmärtämällä ensin kolme käsitettä:

- _Tokenisointi_ = miten malli "näkee" kehotteen
- _Perus-LLM:t_ = miten perusmalli "käsittelee" kehotteen
- _Ohjeistuksella hienosäädetyt LLM:t_ = miten malli voi nyt nähdä "tehtävät"

### Tokenisointi

LLM näkee kehotteet _tokenien sarjana_, jossa eri mallit (tai mallin versiot) voivat tokenisoida saman kehotteen eri tavoin. Koska LLM:t on koulutettu tokeneilla (eikä raakatekstillä), kehotteiden tokenisoinnin tapa vaikuttaa suoraan tuotetun vastauksen laatuun.

Jos haluat saada käsityksen tokenisoinnin toiminnasta, kokeile työkaluja, kuten [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst). Kopioi kehotteesi - ja katso, miten se muunnetaan tokeneiksi, kiinnittäen huomiota siihen, miten välilyönnit ja välimerkit käsitellään. Huomaa, että tämä esimerkki näyttää vanhemman LLM:n (GPT-3) - joten kokeilemalla tätä uudemmalla mallilla voi tuottaa erilaisen tuloksen.

### Käsite: Perusmallit

Kun kehotus on tokenisoitu, "Perus-LLM":n (tai perusmallin) ensisijainen tehtävä on ennustaa token kyseisessä sarjassa. Koska LLM:t on koulutettu massiivisilla tekstidatakoosteilla, niillä on hyvä käsitys tokenien välisistä tilastollisista suhteista ja ne voivat tehdä ennusteen luottavaisesti. Huomaa, että ne eivät ymmärrä sanojen _merkitystä_ kehotteessa tai tokenissa; ne vain näkevät kuvion, jonka ne voivat "täydentää" seuraavalla ennusteellaan. Ne voivat jatkaa ennustamista, kunnes käyttäjä keskeyttää ne tai jokin ennalta määritelty ehto täyttyy.

Haluatko nähdä, miten kehotepohjainen täydentäminen toimii? Syötä yllä oleva kehotus Azure OpenAI Studion [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) oletusasetuksilla. Järjestelmä on konfiguroitu käsittelemään kehotteita tiedonpyyntöinä - joten sinun pitäisi nähdä täydentäminen, joka täyttää tämän kontekstin.

Mutta entä jos käyttäjä halusi nähdä jotain erityistä, joka täyttää jonkin kriteerin tai tehtävän tavoitteen? Tässä kohtaa _ohjeistuksella hienosäädetyt_ LLM:t tulevat kuvaan.

### Käsite: Ohjeistuksella hienosäädetyt LLM:t

[Ohjeistuksella hienosäädetty LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) alkaa perusmallista ja hienosäätää sitä esimerkkien tai syöte/vastausparien (esim. monikierroksisten "viestien") avulla, jotka voivat sisältää selkeitä ohjeita - ja tekoälyn vastaus yrittää noudattaa kyseistä ohjetta.

Tämä käyttää tekniikoita, kuten vahvistusoppimista ihmisen palautteen avulla (RLHF), jotka voivat kouluttaa mallia _seuraamaan ohjeita_ ja _oppimaan palautteesta_, jotta se tuottaa vastauksia, jotka soveltuvat paremmin käytännön sovelluksiin ja ovat merkityksellisempiä käyttäjän tavoitteille.

Kokeillaan sitä - palataan yllä olevaan kehotteeseen, mutta nyt muutetaan _järjestelmäviesti_ antamaan seuraava ohje kontekstina:

> _Tiivistä sinulle annettu sisältö toisen luokan oppilaalle. Pidä tulos yhdessä kappaleessa, jossa on 3-5 kohtaa._

Näetkö, miten tulos on nyt hienosäädetty heijastamaan haluttua tavoitetta ja muotoa? Opettaja voi nyt suoraan käyttää tätä vastausta kyseisen luokan dioissa.

## Miksi tarvitsemme kehotussuunnittelua?

Nyt kun tiedämme, miten LLM:t käsittelevät kehotteita, keskustellaan _miksi_ tarvitsemme kehotussuunnittelua. Vastaus löytyy siitä, että nykyiset LLM:t aiheuttavat useita haasteita, jotka tekevät _luotettavien ja johdonmukaisten täydennysten_ saavuttamisesta haastavampaa ilman kehotteen rakentamiseen ja optimointiin panostamista. Esimerkiksi:

1. **Mallien vastaukset ovat stokastisia.** _Sama kehotus_ tuottaa todennäköisesti erilaisia vastauksia eri malleilla tai malliversioilla. Ja se voi jopa tuottaa erilaisia tuloksia _samalla mallilla_ eri aikoina. _Kehotussuunnittelutekniikoilla voimme minimoida näitä vaihteluita tarjoamalla parempia suojakaiteita_.

2. **Mallit voivat sepittää vastauksia.** Mallit on esikoulutettu _laajoilla mutta rajallisilla_ tietokokonaisuuksilla, mikä tarkoittaa, että niiltä puuttuu tietämys koulutuksen ulkopuolisista käsitteistä. Tämän seurauksena ne voivat tuottaa täydennyksiä, jotka ovat epätarkkoja, kuvitteellisia tai suoraan ristiriidassa tunnettujen faktojen kanssa. _Kehotussuunnittelutekniikoilla autamme käyttäjiä tunnistamaan ja lieventämään tällaisia sepityksiä esim. pyytämällä tekoälyltä viittauksia tai perusteluja_.

3. **Mallien kyvyt vaihtelevat.** Uudemmilla malleilla tai mallisukupolvilla on rikkaampia kykyjä, mutta ne tuovat myös ainutlaatuisia omituisuuksia ja kompromisseja kustannuksissa ja monimutkaisuudessa. _Kehotussuunnittelulla voimme kehittää parhaita käytäntöjä ja työnkulkuja, jotka abstrahoivat erot ja mukautuvat mallikohtaisiin vaatimuksiin skaalautuvalla, saumattomalla tavalla_.

Katsotaanpa tätä toiminnassa OpenAI:n tai Azure OpenAI:n Playgroundissa:

- Käytä samaa kehotetta eri LLM-järjestelmissä (esim. OpenAI, Azure OpenAI, Hugging Face) - näitkö vaihteluita?
- Käytä samaa kehotetta toistuvasti _samassa_ LLM-järjestelmässä (esim. Azure OpenAI Playground) - miten nämä vaihtelut erosivat?

### Sepitysten esimerkki

Tässä kurssissa käytämme termiä **"sepitys"** viittaamaan ilmiöön, jossa LLM:t joskus tuottavat tosiasiallisesti virheellistä tietoa koulutuksen rajoitusten tai muiden rajoitteiden vuoksi. Saatat myös olla kuullut tätä kutsuttavan _"hallusinaatioiksi"_ suosituissa artikkeleissa tai tutkimuspapereissa. Suosittelemme kuitenkin vahvasti käyttämään termiä _"sepitys"_ niin, ettemme vahingossa inhimillistäisi käyttäytymistä antamalla koneohjatulle tulokselle ihmismäistä ominaisuutta. Tämä myös vahvistaa [Vastuullisen tekoälyn ohjeita](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminologian näkökulmasta, poistamalla termejä, joita saatetaan pitää loukkaavina tai epäinklusiivisina joissakin yhteyksissä.

Haluatko saada käsityksen siitä, miten sepitykset toimivat? Mieti kehotetta, joka ohjeistaa tekoälyä tuottamaan sisältöä olemattomasta aiheesta (jotta se ei löydy koulutusaineistosta). Esimerkiksi - kokeilin tätä kehotetta:

> **Kehotus:** luo oppituntisuunnitelma Marsin sodasta vuodelta 2076.

Verkkohaku näytti minulle, että oli olemassa fiktiivisiä kertomuksia (esim. televisiosarjoja tai kirjoja) Marsin sodista - mutta ei vuodelta 2076. Järki myös kertoo meille, että vuosi 2076 on _tulevaisuudessa_ ja siten, sitä ei voida liittää todelliseen tapahtumaan.

Mitä tapahtuu, kun ajamme tämän kehotteen eri LLM-tarjoajilla?

> **Vastaus 1**: OpenAI Playground (GPT-35)

> **Vastaus 2**: Azure OpenAI Playground (GPT-35)

> **Vastaus 3**: Hugging Face Chat Playground (LLama-2)

Kuten odotettiin, jokainen malli (
Lopulta mallipohjien todellinen arvo piilee kyvyssä luoda ja julkaista _kehotekirjastoja_ vertikaalisille sovellusalueille - joissa kehotemalli on nyt _optimoitu_ heijastamaan sovelluskohtaisia konteksteja tai esimerkkejä, jotka tekevät vastauksista käyttäjäyleisölle osuvampia ja tarkempia. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) -tietovarasto on hyvä esimerkki tästä lähestymistavasta, kuratoiden kirjaston kehotteita koulutusalueelle, keskittyen keskeisiin tavoitteisiin kuten oppituntien suunnittelu, opetussuunnitelman suunnittelu, opiskelijoiden ohjaus jne.

## Tukisisältö

Jos ajattelemme kehotteen rakentamista sisältävän ohjeen (tehtävä) ja kohteen (ensisijainen sisältö), niin _toissijainen sisältö_ on kuin lisäkonteksti, jonka annamme **vaikuttaaksemme jollain tavalla tulokseen**. Se voi olla säätöparametreja, muotoiluohjeita, aiheluokituksia jne., jotka voivat auttaa mallia _räätälöimään_ vastauksensa vastaamaan haluttuja käyttäjän tavoitteita tai odotuksia.

Esimerkiksi: Annetaan kurssiluettelo, jossa on laaja metatieto (nimi, kuvaus, taso, metatietotunnisteet, opettaja jne.) kaikista opetussuunnitelman kursseista:

- voimme määritellä ohjeen "tiivistää syksyn 2023 kurssiluettelo"
- voimme käyttää ensisijaista sisältöä antaaksemme muutamia esimerkkejä halutusta tuloksesta
- voimme käyttää toissijaista sisältöä tunnistaaksemme viisi kiinnostavinta "tunnistetta".

Nyt malli voi tarjota yhteenvedon muodossa, joka on esitetty muutamissa esimerkeissä - mutta jos tuloksessa on useita tunnisteita, se voi priorisoida toissijaisessa sisällössä tunnistetut viisi tunnistetta.

---

<!--
OPETUSMALLI:
Tämän yksikön tulisi kattaa ydinajatus #1.
Vahvista konsepti esimerkeillä ja viitteillä.

KONSEPTI #3:
Kehotetekniikat.
Mitkä ovat perusmenetelmiä kehotetekniikoissa?
Havainnollista se harjoituksilla.
-->

## Kehotetekniikoiden parhaat käytännöt

Nyt kun tiedämme, kuinka kehotteita voidaan _rakentaa_, voimme alkaa miettiä, kuinka _suunnitella_ niitä heijastamaan parhaita käytäntöjä. Voimme ajatella tätä kahdessa osassa - oikean _ajattelutavan_ omaksuminen ja oikeiden _tekniikoiden_ soveltaminen.

### Kehotetekniikoiden ajattelutapa

Kehotetekniikka on kokeilu- ja erehdysprosessi, joten pidä mielessä kolme laajaa ohjaavaa tekijää:

1. **Toimialan ymmärtäminen on tärkeää.** Vastausten tarkkuus ja osuvuus ovat _toimialan_ funktio, jossa sovellus tai käyttäjä toimii. Käytä intuitiotasi ja toimialaosaamistasi **räätälöidäksesi tekniikoita** edelleen. Määritä esimerkiksi _toimialakohtaisia persoonallisuuksia_ järjestelmäkehotteissasi tai käytä _toimialakohtaisia malleja_ käyttäjäkehotteissasi. Tarjoa toissijaista sisältöä, joka heijastaa toimialakohtaisia konteksteja, tai käytä _toimialakohtaisia vihjeitä ja esimerkkejä_ ohjataksesi mallia kohti tuttuja käyttötapoja.

2. **Mallin ymmärtäminen on tärkeää.** Tiedämme, että mallit ovat luonteeltaan satunnaisia. Mutta mallien toteutukset voivat myös vaihdella käyttämänsä harjoitusdatan (ennalta koulutettu tieto), tarjoamiensa ominaisuuksien (esim. API:n tai SDK:n kautta) ja sen sisällön tyypin mukaan, johon ne on optimoitu (esim. koodi vs. kuvat vs. teksti). Ymmärrä käyttämäsi mallin vahvuudet ja rajoitukset, ja käytä tätä tietoa _priorisoidaksesi tehtäviä_ tai rakentaaksesi _räätälöityjä malleja_, jotka on optimoitu mallin ominaisuuksille.

3. **Iteraatio ja validointi ovat tärkeitä.** Mallit kehittyvät nopeasti, ja niin kehittyvät myös kehotetekniikat. Toimiala-asiantuntijana sinulla voi olla muuta kontekstia tai kriteerejä _sinun_ erityissovelluksellesi, joka ei välttämättä koske laajempaa yhteisöä. Käytä kehotetekniikkatyökaluja ja -menetelmiä "aloittaaksesi" kehotteen rakentamisen, sitten toista ja validoi tulokset käyttäen omaa intuitiotasi ja toimialaosaamistasi. Tallenna oivalluksesi ja luo **tietokanta** (esim. kehotekirjastot), jota muut voivat käyttää uutena lähtökohtana nopeampiin iterointeihin tulevaisuudessa.

## Parhaat käytännöt

Katsotaanpa nyt yleisiä parhaita käytäntöjä, joita [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ja [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) -käytännön harjoittajat suosittelevat.

| Mitä                               | Miksi                                                                                                                                                                                                                                               |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Arvioi uusimmat mallit.            | Uudet mallisukupolvet todennäköisesti tarjoavat parannettuja ominaisuuksia ja laatua - mutta voivat myös aiheuttaa korkeampia kustannuksia. Arvioi niiden vaikutus ja tee sitten siirtymäpäätökset.                                                 |
| Erottele ohjeet ja konteksti       | Tarkista, määritteleekö mallisi/toimittajasi _erottimia_ ohjeiden, ensisijaisen ja toissijaisen sisällön selkeämpään erottamiseen. Tämä voi auttaa malleja kohdistamaan painotukset tarkemmin tokeneihin.                                            |
| Ole tarkka ja selkeä               | Anna enemmän yksityiskohtia halutusta kontekstista, tuloksesta, pituudesta, muodosta, tyylistä jne. Tämä parantaa sekä vastausten laatua että johdonmukaisuutta. Tallenna reseptit uudelleenkäytettäviin malleihin.                                 |
| Ole kuvaileva, käytä esimerkkejä   | Mallit voivat vastata paremmin "näytä ja kerro" -lähestymistapaan. Aloita `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` -arvoilla. Palaa [Learning Sandbox -osioon](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) oppiaksesi lisää.

### Seuraavaksi avaa Jupyter Notebook

- Valitse ajonaikainen ydin. Jos käytät vaihtoehtoja 1 tai 2, valitse yksinkertaisesti oletusarvoinen Python 3.10.x -ydin, jonka dev-kontti tarjoaa.

Olet valmis suorittamaan harjoitukset. Huomaa, että täällä ei ole _oikeita tai vääriä_ vastauksia - vain vaihtoehtojen tutkimista kokeilemalla ja erehdyksellä ja intuition rakentamista siitä, mikä toimii tietylle mallille ja sovellusalueelle.

_Tästä syystä tässä oppitunnissa ei ole koodiratkaisuosuuksia. Sen sijaan Notebookissa on Markdown-soluja, jotka on otsikoitu "My Solution:", ja ne näyttävät yhden esimerkkituloksen viitteeksi._

<!--
OPETUSMALLI:
Päätä osio yhteenvedolla ja resursseilla itseohjautuvaan oppimiseen.
-->

## Tietojen tarkistus

Mikä seuraavista on hyvä kehotus, joka noudattaa kohtuullisia parhaita käytäntöjä?

1. Näytä minulle kuva punaisesta autosta
2. Näytä minulle kuva punaisesta autosta, merkiltään Volvo ja malliltaan XC90, joka on pysäköity jyrkänteen reunalle auringon laskiessa
3. Näytä minulle kuva punaisesta autosta, merkiltään Volvo ja malliltaan XC90

A: 2, se on paras kehotus, koska se antaa yksityiskohtia "mistä" ja menee yksityiskohtiin (ei vain mikä tahansa auto, vaan tietty merkki ja malli) ja se myös kuvailee kokonaisasetelman. 3 on seuraavaksi paras, koska se sisältää myös paljon kuvailua.

## 🚀 Haaste

Katso, voitko hyödyntää "vihje" -tekniikkaa kehotteella: Täydennä lause "Näytä minulle kuva punaisesta autosta, merkiltään Volvo ja ". Mitä se vastaa, ja miten parantaisit sitä?

## Hienoa työtä! Jatka oppimista

Haluatko oppia lisää erilaisista kehotetekniikoista? Mene [jatkuvan oppimisen sivulle](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) löytääksesi muita hienoja resursseja tästä aiheesta.

Siirry oppituntiin 5, jossa tarkastelemme [edistyneitä kehotetekniikoita](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää auktoritatiivisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virheellisistä tulkinnoista.