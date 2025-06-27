<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:56:54+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "fi"
}
-->
# Kehoteohjelmoinnin perusteet

## Johdanto
Tämä moduuli kattaa olennaisia käsitteitä ja tekniikoita tehokkaiden kehotteiden luomiseksi generatiivisissa tekoälymalleissa. Myös tapa, jolla kirjoitat kehotteen LLM:lle, on tärkeä. Huolellisesti laadittu kehote voi saavuttaa paremman vastauksen laadun. Mutta mitä tarkalleen ottaen tarkoittavat termit _kehote_ ja _kehoteohjelmointi_? Ja miten voin parantaa LLM:lle lähettämääni kehote _syötettä_? Näihin kysymyksiin yritämme vastata tässä ja seuraavassa luvussa.

_Generatiivinen tekoäly_ pystyy luomaan uutta sisältöä (esim. tekstiä, kuvia, ääntä, koodia jne.) käyttäjän pyyntöihin vastaten. Se tekee tämän käyttämällä _laajoja kielimalleja_ kuten OpenAI:n GPT ("Generative Pre-trained Transformer") -sarjaa, jotka on koulutettu käyttämään luonnollista kieltä ja koodia.

Käyttäjät voivat nyt olla vuorovaikutuksessa näiden mallien kanssa tutuin paradigmojen, kuten chatin, kautta ilman teknistä asiantuntemusta tai koulutusta. Mallit ovat _kehoteperusteisia_ - käyttäjät lähettävät tekstisyötteen (kehote) ja saavat takaisin tekoälyn vastauksen (täydennys). He voivat sitten "keskustella tekoälyn kanssa" iteratiivisesti, monivaiheisissa keskusteluissa, hienosäätäen kehotettaan, kunnes vastaus vastaa heidän odotuksiaan.

"Kehotteista" tulee nyt ensisijainen _ohjelmointiliittymä_ generatiivisille tekoälysovelluksille, jotka kertovat malleille, mitä tehdä ja vaikuttavat palautettujen vastausten laatuun. "Kehoteohjelmointi" on nopeasti kasvava tutkimusala, joka keskittyy kehotteiden _suunnitteluun ja optimointiin_ tuottamaan johdonmukaisia ja laadukkaita vastauksia laajassa mittakaavassa.

## Oppimistavoitteet

Tässä oppitunnissa opimme, mitä kehoteohjelmointi on, miksi se on tärkeää ja kuinka voimme luoda tehokkaampia kehotteita tietylle mallille ja sovellustavoitteelle. Ymmärrämme kehoteohjelmoinnin ydinkäsitteet ja parhaat käytännöt - ja opimme interaktiivisesta Jupyter Notebooks "sandbox" -ympäristöstä, jossa voimme nähdä näiden käsitteiden soveltamista todellisiin esimerkkeihin.

Oppitunnin lopussa pystymme:

1. Selittämään, mitä kehoteohjelmointi on ja miksi se on tärkeää.
2. Kuvaamaan kehotteen osat ja miten niitä käytetään.
3. Oppimaan kehoteohjelmoinnin parhaat käytännöt ja tekniikat.
4. Soveltamaan opittuja tekniikoita todellisiin esimerkkeihin, käyttämällä OpenAI-päätepistettä.

## Keskeiset termit

Kehoteohjelmointi: Käytäntö suunnitella ja hienosäätää syötteitä ohjaamaan tekoälymalleja tuottamaan haluttuja tuloksia.
Tokenisointi: Prosessi, jossa teksti muunnetaan pienemmiksi yksiköiksi, joita kutsutaan tokeneiksi, joita malli voi ymmärtää ja käsitellä.
Ohjeviritetyt LLM:t: Suuret kielimallit (LLM:t), jotka on hienosäädetty erityisillä ohjeilla parantamaan niiden vastausten tarkkuutta ja osuvuutta.

## Oppimisen sandbox

Kehoteohjelmointi on tällä hetkellä enemmän taidetta kuin tiedettä. Paras tapa parantaa intuitiota siitä on _harjoitella enemmän_ ja omaksua kokeilu- ja erehdysmenetelmä, joka yhdistää sovellusalueen asiantuntemuksen suositeltuihin tekniikoihin ja mallikohtaisiin optimointeihin.

Tämän oppitunnin mukana oleva Jupyter Notebook tarjoaa _sandbox_-ympäristön, jossa voit kokeilla oppimaasi - joko matkan varrella tai osana koodaushaastetta lopussa. Harjoitusten suorittamiseen tarvitset:

1. **Azure OpenAI API -avain** - palvelupäätepiste käyttöön otetulle LLM:lle.
2. **Python-suoritusympäristö** - jossa Notebook voidaan suorittaa.
3. **Paikalliset ympäristömuuttujat** - _suorita [ASENNUS](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) -vaiheet nyt valmiiksi_.

Notebookissa on mukana _aloitusharjoituksia_ - mutta sinua kannustetaan lisäämään omia _Markdown_ (kuvaus) ja _Code_ (kehotepyynnöt) osioita kokeillaksesi lisää esimerkkejä tai ideoita - ja kehittämään intuitiota kehotteen suunnittelusta.

## Kuvitettu opas

Haluatko saada yleiskuvan siitä, mitä tämä oppitunti kattaa ennen kuin sukellat sisään? Tutustu tähän kuvitettuun oppaaseen, joka antaa sinulle käsityksen käsitellyistä pääaiheista ja keskeisistä huomioista, joita kannattaa miettiä jokaisessa niistä. Oppitunnin etenemissuunnitelma vie sinut ydinkäsitteiden ja haasteiden ymmärtämisestä niiden käsittelyyn asiaankuuluvilla kehoteohjelmoinnin tekniikoilla ja parhailla käytännöillä. Huomaa, että tämän oppaan "Edistyneet tekniikat" -osio viittaa tämän opetussuunnitelman _seuraavassa_ luvussa käsiteltyyn sisältöön.

## Startupimme

Puhutaanpa nyt siitä, miten _tämä aihe_ liittyy startup-missioomme [tuoda tekoälyinnovaatioita koulutukseen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Haluamme rakentaa tekoälyllä toimivia sovelluksia _henkilökohtaiseen oppimiseen_ - joten mietitään, miten eri käyttäjät sovelluksessamme voisivat "suunnitella" kehotteita:

- **Ylläpitäjät** saattavat pyytää tekoälyä _analysoimaan opetussuunnitelman tietoja kattavuusaukkojen tunnistamiseksi_. Tekoäly voi tiivistää tulokset tai visualisoida ne koodin avulla.
- **Kouluttajat** saattavat pyytää tekoälyä _luomaan oppituntisuunnitelman kohdeyleisölle ja aiheelle_. Tekoäly voi rakentaa henkilökohtaisen suunnitelman määritetyssä muodossa.
- **Opiskelijat** saattavat pyytää tekoälyä _ohjaamaan heitä vaikeassa aiheessa_. Tekoäly voi nyt opastaa opiskelijoita oppitunneilla, vihjeillä ja esimerkeillä, jotka on räätälöity heidän tasolleen.

Tämä on vain jäävuoren huippu. Tutustu [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - avoimen lähdekoodin kehotekirjastoon, jota koulutuksen asiantuntijat ovat kuratoineet - saadaksesi laajemman käsityksen mahdollisuuksista! _Kokeile suorittaa joitakin näistä kehotteista hiekkalaatikossa tai käyttämällä OpenAI Playgoundia nähdäksesi, mitä tapahtuu!_

## Mikä on kehoteohjelmointi?

Aloitimme tämän oppitunnin määrittelemällä **kehoteohjelmoinnin** prosessiksi, jossa _suunnitellaan ja optimoidaan_ tekstisyötteitä (kehotteita) tuottamaan johdonmukaisia ja laadukkaita vastauksia (täydennyksiä) tietylle sovellustavoitteelle ja mallille. Voimme ajatella tätä kaksivaiheisena prosessina:

- _suunnitellaan_ alkuperäinen kehote tietylle mallille ja tavoitteelle
- _hienosäädetään_ kehotetta iteratiivisesti parantamaan vastauksen laatua

Tämä on väistämättä kokeilu- ja erehdysprosessi, joka vaatii käyttäjän intuitiota ja vaivannäköä optimaalisten tulosten saavuttamiseksi. Miksi se sitten on tärkeää? Vastaaksemme tähän kysymykseen meidän on ensin ymmärrettävä kolme käsitettä:

- _Tokenisointi_ = miten malli "näkee" kehotteen
- _Perus-LLM:t_ = miten perustamalli "käsittelee" kehotteen
- _Ohjeviritetyt LLM:t_ = miten malli voi nyt nähdä "tehtäviä"

### Tokenisointi

LLM näkee kehotteet _tokenien jonoina_, joissa eri mallit (tai mallin versiot) voivat tokenisoida saman kehotteen eri tavoin. Koska LLM:t on koulutettu tokeneilla (eikä raakatiedolla), tapa, jolla kehotteet tokenisoidaan, vaikuttaa suoraan tuotetun vastauksen laatuun.

Saadaksesi intuitiota siitä, miten tokenisointi toimii, kokeile työkaluja kuten [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), joka on esitetty alla. Kopioi kehoteesi - ja katso, miten se muunnetaan tokeneiksi, kiinnittäen huomiota siihen, miten välilyöntimerkit ja välimerkit käsitellään. Huomaa, että tämä esimerkki näyttää vanhemman LLM:n (GPT-3) - joten kokeilemalla tätä uudempaan malliin voi tuottaa erilaisen tuloksen.

### Käsite: Perustamallit

Kun kehote on tokenisoitu, ["Perus-LLM:n"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (tai perustamallin) ensisijainen tehtävä on ennustaa tokeni siinä järjestyksessä. Koska LLM:t on koulutettu massiivisilla tekstiaineistoilla, niillä on hyvä käsitys tokenien välisistä tilastollisista suhteista ja ne voivat tehdä ennustuksen jonkin verran luottamuksella. Huomaa, että ne eivät ymmärrä sanojen _merkitystä_ kehoteessa tai tokenissa; ne vain näkevät kuvion, jonka ne voivat "täydentää" seuraavalla ennustuksellaan. Ne voivat jatkaa järjestyksen ennustamista, kunnes käyttäjä keskeyttää tai jokin ennalta määrätty ehto päättyy.

Haluatko nähdä, miten kehoteperusteinen täydennys toimii? Syötä yllä oleva kehote Azure OpenAI Studion [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) oletusasetuksilla. Järjestelmä on konfiguroitu käsittelemään kehotteita tietopyyntöinä - joten sinun pitäisi nähdä täydennys, joka tyydyttää tämän kontekstin.

Mutta entä jos käyttäjä halusi nähdä jotain erityistä, joka täytti jotkin kriteerit tai tehtävätavoitteen? Tässä kohtaa _ohjeviritetyt_ LLM:t tulevat kuvaan.

### Käsite: Ohjeviritetyt LLM:t

[Ohjeviritetty LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) alkaa perustamallista ja hienosäätää sitä esimerkeillä tai syöte-/tulosteparilla (esim. monivaiheiset "viestit"), jotka voivat sisältää selkeitä ohjeita - ja tekoälyn vastaus yrittää noudattaa kyseistä ohjetta.

Tämä käyttää tekniikoita, kuten vahvistusoppimista ihmisen palautteen avulla (RLHF), joka voi kouluttaa mallia _seuraamaan ohjeita_ ja _oppimaan palautteesta_ siten, että se tuottaa vastauksia, jotka sopivat paremmin käytännön sovelluksiin ja ovat käyttäjän tavoitteiden kannalta merkityksellisempiä.

Kokeillaan sitä - palaa yllä olevaan kehoteeseen, mutta muuta nyt _järjestelmäviesti_ antamaan seuraava ohje kontekstina:

> _Yhteenveto annetusta sisällöstä toisen luokan oppilaalle. Pidä tulos yhtenä kappaleena, jossa on 3-5 luettelomerkkiä._

Näetkö, kuinka tulos on nyt viritetty heijastamaan haluttua tavoitetta ja muotoa? Kouluttaja voi nyt käyttää tätä vastausta suoraan luentokalvoissaan.

## Miksi tarvitsemme kehoteohjelmointia?

Nyt kun tiedämme, miten LLM:t käsittelevät kehotteita, puhutaan siitä, _miksi_ tarvitsemme kehoteohjelmointia. Vastaus löytyy siitä, että nykyiset LLM:t asettavat useita haasteita, jotka tekevät _luotettavien ja johdonmukaisten täydennysten_ saavuttamisesta haastavampaa ilman, että panostetaan kehotteen rakentamiseen ja optimointiin. Esimerkiksi:

1. **Mallien vastaukset ovat stokastisia.** _Sama kehote_ tuottaa todennäköisesti erilaisia vastauksia eri malleilla tai malliversioilla. Ja se voi jopa tuottaa erilaisia tuloksia _samalla mallilla_ eri aikoina. _Kehoteohjelmointitekniikat voivat auttaa meitä minimoimaan nämä vaihtelut tarjoamalla parempia suojarajoja_.

1. **Mallit voivat sepittää vastauksia.** Mallit on esikoulutettu _laajoilla mutta rajallisilla_ aineistoilla, mikä tarkoittaa, että ne eivät tunne koulutuksen ulkopuolisia käsitteitä. Tämän seurauksena ne voivat tuottaa täydennyksiä, jotka ovat epätarkkoja, kuviteltuja tai suoranaisesti ristiriidassa tunnettujen tosiasioiden kanssa. _Kehoteohjelmointitekniikat auttavat käyttäjiä tunnistamaan ja lieventämään tällaisia sepityksiä esimerkiksi pyytämällä tekoälyä antamaan lähteitä tai perusteluja_.

1. **Mallien kyvyt vaihtelevat.** Uudemmilla malleilla tai mallisukupolvilla on rikkaampia kykyjä, mutta ne tuovat mukanaan myös ainutlaatuisia omituisuuksia ja kompromisseja kustannusten ja monimutkaisuuden suhteen. _Kehoteohjelmointi voi auttaa meitä kehittämään parhaita käytäntöjä ja työnkulkuja, jotka abstrahoivat erot ja mukautuvat mallikohtaisiin vaatimuksiin skaalautuvalla, saumattomalla tavalla_.

Katsotaanpa tätä toiminnassa OpenAI:n tai Azure OpenAI:n Playgroundissa:

- Käytä samaa kehotetta eri LLM-toteutuksilla (esim. OpenAI, Azure OpenAI, Hugging Face) - näitkö vaihtelut?
- Käytä samaa kehotetta toistuvasti _samalla_ LLM-toteutuksella (esim. Azure OpenAI Playground) - miten nämä vaihtelut erosivat?

### Sepitysten esimerkki

Tässä kurssissa käytämme termiä **"sepitys"** viittaamaan ilmiöön, jossa LLM:t joskus tuottavat tosiasiallisesti virheellistä tietoa koulutuksen tai muiden rajoitteiden vuoksi. Saatat myös olla kuullut tästä viitattavan _"hallusinaatioina"_ suosituissa artikkeleissa tai tutkimuspapereissa. Suosittelemme kuitenkin vahvasti käyttämään termiä _"sepitys"_, jotta emme vahingossa antropomorfisoisi käyttäytymistä antamalla ihmismäistä ominaisuutta koneen ohjaamalle tulokselle. Tämä myös vahvistaa [vastuullisen tekoälyn ohjeita](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminologian näkökulmasta, poistamalla termejä, joita voidaan pitää loukkaavina tai ei-sisällyttävinä joissakin yhteyksissä.

Haluatko saada käsityksen siitä, miten sepitykset toimivat? Mieti kehote, joka ohjeistaa tekoälyä tuottamaan sisältöä olemattomasta aiheesta (jotta se ei löydy koulutusaineistosta). Esimerkiksi - kokeilin tätä kehotetta:

> **Kehote:** laadi oppituntisuunnitelma Marsin sodasta vuonna 2076.

Verkkohaku osoitti minulle, että oli olemassa fiktiivisiä kertomuksia (esim. televisiosarjoja tai kirjoja) Marsin sodista - mutta ei vuodelta 2076. Järki myös kertoo meille, että vuosi 2076 on _tulevaisuudessa_ ja siten, sitä ei voida yhdistää todelliseen tapahtumaan.

Joten mitä tapahtuu, kun suoritamme tämän kehotteen eri LLM-palveluntarjoajilla?

> **Vastaus 1**: OpenAI Playground (GPT-35)

> **Vastaus 2**: Azure OpenAI Playground (GPT-35)

> **Vastaus 3**: Hugging
Lopulta mallipohjien todellinen arvo on kyvyssä luoda ja julkaista _kehotekirjastoja_ tiettyihin sovellusalueisiin - missä kehotemalli on nyt _optimoitu_ heijastamaan sovelluskohtaista kontekstia tai esimerkkejä, jotka tekevät vastauksista käyttäjäkohderyhmälle merkityksellisempiä ja tarkempia. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) -arkisto on loistava esimerkki tästä lähestymistavasta, sillä se kokoaa kirjaston kehotteista opetusalalle, painottaen avaintavoitteita kuten oppituntien suunnittelu, opetussuunnitelman suunnittelu, opiskelijoiden ohjaus jne.

## Tukisisältö

Jos ajattelemme kehotteen rakentamista sisältävän ohjeen (tehtävän) ja kohteen (ensisijaisen sisällön), niin _toissijainen sisältö_ on kuin lisäkonteksti, jonka tarjoamme **vaikuttaaksemme jollain tavalla tuotokseen**. Se voi olla säätöparametreja, muotoiluohjeita, aiheiden taksonomioita jne., jotka voivat auttaa mallia _mukauttamaan_ vastauksensa vastaamaan haluttuja käyttäjätavoitteita tai -odotuksia.

Esimerkiksi: Annetaan kurssiluettelo, jossa on laaja metadata (nimi, kuvaus, taso, metadatamerkit, ohjaaja jne.) kaikista opetussuunnitelman saatavilla olevista kursseista:

- voimme määritellä ohjeen "tiivistää syksyn 2023 kurssiluettelo"
- voimme käyttää ensisijaista sisältöä antamaan muutamia esimerkkejä halutusta tuotoksesta
- voimme käyttää toissijaista sisältöä tunnistamaan viisi kiinnostavinta "merkkiä".

Nyt malli voi tarjota tiivistelmän muutaman esimerkin osoittamassa muodossa - mutta jos tuloksella on useita merkkejä, se voi priorisoida toissijaisessa sisällössä tunnistetut viisi merkkiä.

---

## Kehotetekniikan parhaat käytännöt

Nyt kun tiedämme, miten kehotteita voidaan _rakentaa_, voimme alkaa miettiä, miten ne voidaan _suunnitella_ heijastamaan parhaita käytäntöjä. Voimme ajatella tätä kahdessa osassa - oikean _ajattelutavan_ omaksumisessa ja oikeiden _tekniikoiden_ soveltamisessa.

### Kehotetekniikan ajattelutapa

Kehotetekniikka on yrityksen ja erehdyksen prosessi, joten pidä mielessä kolme laajaa ohjaavaa tekijää:

1. **Toimialan ymmärtäminen on tärkeää.** Vastausten tarkkuus ja merkityksellisyys riippuvat _toimialasta_, jolla sovellus tai käyttäjä toimii. Sovella intuitiotasi ja toimialan asiantuntemustasi **räätälöidäksesi tekniikoita** edelleen. Määrittele esimerkiksi _toimialakohtaiset persoonallisuudet_ järjestelmäkehotteissasi tai käytä _toimialakohtaisia malleja_ käyttäjäkehotteissasi. Tarjoa toissijaista sisältöä, joka heijastaa toimialakohtaisia konteksteja, tai käytä _toimialakohtaisia vihjeitä ja esimerkkejä_ ohjataksesi mallia kohti tuttuja käyttötapoja.

2. **Mallin ymmärtäminen on tärkeää.** Tiedämme, että mallit ovat luonteeltaan stokastisia. Mutta mallien toteutukset voivat myös vaihdella käyttämänsä koulutusdatan (esikoulutettu tieto), tarjoamiensa kykyjen (esim. API:n tai SDK:n kautta) ja optimoidun sisällön (esim. koodi vs. kuvat vs. teksti) osalta. Ymmärrä käyttämäsi mallin vahvuudet ja rajoitukset, ja käytä tätä tietoa _priorisoidaksesi tehtäviä_ tai rakentaaksesi _räätälöityjä malleja_, jotka on optimoitu mallin kyvyille.

3. **Iterointi ja validointi ovat tärkeitä.** Mallit kehittyvät nopeasti, ja samoin tekevät kehotetekniikan tekniikat. Toimialan asiantuntijana sinulla voi olla muuta kontekstia tai kriteerejä _sinun_ erityiselle sovelluksellesi, jotka eivät välttämättä päde laajempaan yhteisöön. Käytä kehotetekniikan työkaluja ja tekniikoita "käynnistääksesi" kehotteen rakentamisen, sitten iteroi ja validoi tulokset oman intuitiosi ja toimialan asiantuntemuksesi avulla. Kirjaa havaintosi ja luo **tietopohja** (esim. kehotekirjastot), jota muut voivat käyttää uutena lähtökohtana nopeampiin iterointeihin tulevaisuudessa.

## Parhaat käytännöt

Katsotaanpa nyt yleisiä parhaita käytäntöjä, joita suosittelevat [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ja [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) asiantuntijat.

| Mitä                              | Miksi                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Arvioi uusimmat mallit.           | Uudet mallisukupolvet todennäköisesti tarjoavat parannettuja ominaisuuksia ja laatua - mutta voivat myös aiheuttaa korkeampia kustannuksia. Arvioi niiden vaikutus ja tee sitten siirtymispäätökset.                                              |
| Erota ohjeet ja konteksti         | Tarkista, määritteleekö mallisi/tarjoajasi _erottimia_, jotka erottavat ohjeet, ensisijaisen ja toissijaisen sisällön selkeämmin. Tämä voi auttaa malleja määrittämään tarkemmin painotukset tokenille.                                         |
| Ole tarkka ja selkeä              | Anna enemmän yksityiskohtia halutusta kontekstista, lopputuloksesta, pituudesta, muodosta, tyylistä jne. Tämä parantaa sekä vastausten laatua että johdonmukaisuutta. Tallenna reseptit uudelleenkäytettäviin malleihin.                           |
| Ole kuvaileva, käytä esimerkkejä  | Mallit voivat vastata paremmin "näytä ja kerro" -lähestymistapaan. Aloita `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` arvoilla. Palaa [Learning Sandbox -osioon](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) oppiaksesi lisää.

### Seuraavaksi avaa Jupyter Notebook

- Valitse ajonaikainen ydin. Jos käytät vaihtoehtoja 1 tai 2, valitse yksinkertaisesti dev-kontin tarjoama oletus Python 3.10.x -ydin.

Olet valmis suorittamaan harjoitukset. Huomaa, että täällä ei ole _oikeita tai vääriä_ vastauksia - vain vaihtoehtojen tutkimista yrityksen ja erehdyksen kautta ja intuition rakentamista siitä, mikä toimii tietylle mallille ja sovellusalueelle.

_Tämän vuoksi tässä oppitunnissa ei ole koodiratkaisuosioita. Sen sijaan Notebookissa on Markdown-soluja otsikolla "Oma ratkaisuni:", joka näyttää yhden esimerkkituloksen viitteeksi._

## Tietämystarkistus

Mikä seuraavista on hyvä kehotus noudattaen joitakin kohtuullisia parhaita käytäntöjä?

1. Näytä minulle kuva punaisesta autosta
2. Näytä minulle kuva punaisesta Volvo XC90 -autosta, joka on pysäköity kallion reunalle auringon laskiessa
3. Näytä minulle kuva punaisesta Volvo XC90 -autosta

A: 2, se on paras kehotus, koska se antaa yksityiskohtia "mitä" ja menee tarkempiin yksityiskohtiin (ei vain mikä tahansa auto, vaan tietty merkki ja malli) ja se kuvailee myös yleistä ympäristöä. 3 on seuraavaksi paras, koska se sisältää myös paljon kuvausta.

## 🚀 Haaste

Katso, voitko hyödyntää "vihje" -tekniikkaa kehotteen kanssa: Täydennä lause "Näytä minulle kuva punaisesta Volvo-merkkisestä autosta ja ". Mitä se vastaa, ja miten parantaisit sitä?

## Hienoa työtä! Jatka oppimista

Haluatko oppia lisää erilaisista kehotetekniikan käsitteistä? Mene [jatkuvan oppimisen sivulle](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) löytääksesi muita loistavia resursseja tästä aiheesta.

Siirry oppituntiin 5, jossa tarkastelemme [edistyneitä kehotetekniikoita](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä AI-käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.