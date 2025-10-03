<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b3cb38518cf4fe7714d2f5e74dfa3eb",
  "translation_date": "2025-10-03T09:44:03+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "fi"
}
-->
# Promptien suunnittelun perusteet

[![Promptien suunnittelun perusteet](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.fi.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Johdanto
Tässä moduulissa käsitellään keskeisiä käsitteitä ja tekniikoita tehokkaiden promptien luomiseksi generatiivisille tekoälymalleille. Tapa, jolla kirjoitat promptin LLM:lle, vaikuttaa merkittävästi lopputulokseen. Huolellisesti laadittu prompti voi tuottaa laadukkaamman vastauksen. Mutta mitä tarkalleen ottaen tarkoittavat termit _prompt_ ja _promptien suunnittelu_? Ja miten voin parantaa promptin _syötettä_, jonka lähetän LLM:lle? Näihin kysymyksiin pyrimme vastaamaan tässä ja seuraavassa luvussa.

_Generatiivinen tekoäly_ pystyy luomaan uutta sisältöä (esim. tekstiä, kuvia, ääntä, koodia jne.) käyttäjän pyyntöjen perusteella. Se saavuttaa tämän käyttämällä _suuriin kielimalleihin_ perustuvia järjestelmiä, kuten OpenAI:n GPT ("Generative Pre-trained Transformer") -sarjaa, jotka on koulutettu käyttämään luonnollista kieltä ja koodia.

Käyttäjät voivat nyt olla vuorovaikutuksessa näiden mallien kanssa tutuilla tavoilla, kuten chatin kautta, ilman teknistä osaamista tai koulutusta. Mallit ovat _prompt-pohjaisia_ – käyttäjät lähettävät tekstisyötteen (promptin) ja saavat takaisin tekoälyn vastauksen (completion). He voivat sitten "keskustella tekoälyn kanssa" iteratiivisesti, monivaiheisissa keskusteluissa, hienosäätäen promptia, kunnes vastaus vastaa odotuksia.

"Promptit" ovat nyt generatiivisten tekoälysovellusten ensisijainen _ohjelmointirajapinta_, joka kertoo malleille, mitä tehdä ja vaikuttaa palautettujen vastausten laatuun. "Promptien suunnittelu" on nopeasti kasvava tutkimusala, joka keskittyy promptien _suunnitteluun ja optimointiin_ laadukkaiden ja johdonmukaisten vastausten tuottamiseksi laajassa mittakaavassa.

## Oppimistavoitteet

Tässä oppitunnissa opimme, mitä promptien suunnittelu on, miksi se on tärkeää ja miten voimme luoda tehokkaampia promptia tietylle mallille ja sovellustavoitteelle. Ymmärrämme keskeiset käsitteet ja parhaat käytännöt promptien suunnittelussa – ja tutustumme interaktiiviseen Jupyter Notebooks -ympäristöön, jossa voimme soveltaa näitä käsitteitä todellisiin esimerkkeihin.

Oppitunnin lopussa osaamme:

1. Selittää, mitä promptien suunnittelu on ja miksi se on tärkeää.
2. Kuvata promptin osat ja niiden käyttötavat.
3. Oppia parhaat käytännöt ja tekniikat promptien suunnitteluun.
4. Soveltaa opittuja tekniikoita todellisiin esimerkkeihin OpenAI:n rajapinnan avulla.

## Keskeiset termit

Promptien suunnittelu: Käytäntö, jossa suunnitellaan ja hienosäädetään syötteitä ohjaamaan tekoälymalleja tuottamaan haluttuja tuloksia.  
Tokenisaatio: Prosessi, jossa teksti muunnetaan pienemmiksi yksiköiksi, joita kutsutaan tokeneiksi, ja joita malli voi ymmärtää ja käsitellä.  
Ohjeistuksella hienosäädetyt LLM:t: Suuret kielimallit (LLM:t), joita on hienosäädetty erityisillä ohjeilla vastausten tarkkuuden ja relevanssin parantamiseksi.

## Oppimisympäristö

Promptien suunnittelu on tällä hetkellä enemmän taidetta kuin tiedettä. Paras tapa kehittää intuitiota sen suhteen on _harjoitella enemmän_ ja omaksua kokeiluun perustuva lähestymistapa, joka yhdistää sovellusalueen asiantuntemuksen suositeltuihin tekniikoihin ja mallikohtaisiin optimointeihin.

Tämän oppitunnin mukana tuleva Jupyter Notebook tarjoaa _sandbox_-ympäristön, jossa voit kokeilla oppimiasi asioita – joko oppitunnin aikana tai lopun kooditehtävän osana. Harjoitusten suorittamiseen tarvitset:

1. **Azure OpenAI API -avaimen** – palvelupisteen käyttöön otetulle LLM:lle.  
2. **Python-ympäristön** – jossa Notebook voidaan suorittaa.  
3. **Paikalliset ympäristömuuttujat** – _suorita [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) -vaiheet nyt valmistautuaksesi_.  

Notebook sisältää _aloitusharjoituksia_ – mutta sinua kannustetaan lisäämään omia _Markdown_- (kuvaus) ja _Code_- (prompt-pyynnöt) osioita kokeillaksesi lisää esimerkkejä tai ideoita – ja rakentaaksesi intuitiota promptien suunnittelusta.

## Kuvitettu opas

Haluatko saada yleiskuvan siitä, mitä tämä oppitunti kattaa ennen kuin sukellat syvemmälle? Tutustu tähän kuvitettuun oppaaseen, joka antaa sinulle käsityksen pääaiheista ja keskeisistä huomioista, joita kannattaa miettiä kunkin osion kohdalla. Oppitunnin etenemissuunnitelma vie sinut keskeisten käsitteiden ja haasteiden ymmärtämisestä niiden ratkaisemiseen asiaankuuluvilla promptien suunnittelutekniikoilla ja parhailla käytännöillä. Huomaa, että tämän oppaan "Edistyneet tekniikat" -osio viittaa sisältöön, joka käsitellään _seuraavassa_ luvussa.

![Promptien suunnittelun kuvitettu opas](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.fi.png)

## Startupimme

Puhutaanpa siitä, miten _tämä aihe_ liittyy startupimme missioon [tuoda tekoälyinnovaatioita koulutukseen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Haluamme rakentaa tekoälypohjaisia sovelluksia _henkilökohtaisen oppimisen_ tueksi – joten mietitään, miten eri käyttäjät sovelluksessamme voisivat "suunnitella" promptia:

- **Hallinnoijat** saattavat pyytää tekoälyä _analysoimaan opetussuunnitelman dataa ja tunnistamaan katvealueita_. Tekoäly voi tiivistää tulokset tai visualisoida ne koodin avulla.  
- **Opettajat** saattavat pyytää tekoälyä _luomaan oppituntisuunnitelman kohdeyleisölle ja aiheelle_. Tekoäly voi rakentaa henkilökohtaisen suunnitelman määritetyssä muodossa.  
- **Oppilaat** saattavat pyytää tekoälyä _opettamaan heitä vaikeassa aiheessa_. Tekoäly voi nyt ohjata oppilaita oppitunneilla, vihjeillä ja esimerkeillä, jotka on räätälöity heidän tasolleen.  

Tämä on vasta jäävuoren huippu. Tutustu [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) -kirjastoon – avoimen lähdekoodin prompt-kirjastoon, jonka ovat kuratoineet koulutusalan asiantuntijat – saadaksesi laajemman käsityksen mahdollisuuksista! _Kokeile ajaa joitakin näistä promteista sandboxissa tai OpenAI Playgroundissa ja katso, mitä tapahtuu!_

<!--
OPPITUNTIPOHJA:
Tämän yksikön tulisi kattaa keskeinen käsite #1.
Vahvista käsitettä esimerkeillä ja viittauksilla.

KÄSITE #1:
Promptien suunnittelu.
Määrittele se ja selitä, miksi sitä tarvitaan.
-->

## Mitä on promptien suunnittelu?

Aloitimme tämän oppitunnin määrittelemällä **promptien suunnittelun** prosessiksi, jossa _suunnitellaan ja optimoidaan_ tekstisyötteitä (promptia) tuottamaan johdonmukaisia ja laadukkaita vastauksia (completions) tiettyä sovellustavoitetta ja mallia varten. Voimme ajatella tätä kaksivaiheisena prosessina:

- _suunnitellaan_ alkuperäinen prompti tietylle mallille ja tavoitteelle  
- _hienosäädetään_ promptia iteratiivisesti vastausten laadun parantamiseksi  

Tämä on väistämättä kokeiluun perustuva prosessi, joka vaatii käyttäjän intuitiota ja vaivannäköä optimaalisten tulosten saavuttamiseksi. Miksi se sitten on tärkeää? Vastataksemme tähän kysymykseen meidän on ensin ymmärrettävä kolme käsitettä:

- _Tokenisaatio_ = miten malli "näkee" promptin  
- _Perus-LLM:t_ = miten perustamalli "käsittelee" promptin  
- _Ohjeistuksella hienosäädetyt LLM:t_ = miten malli voi nyt nähdä "tehtävät"  

### Tokenisaatio

LLM näkee promptit _tokenien sarjana_, jossa eri mallit (tai malliversiot) voivat tokenisoida saman promptin eri tavoin. Koska LLM:t on koulutettu tokeneilla (eikä raakatiedolla), tapa, jolla promptit tokenisoidaan, vaikuttaa suoraan tuotetun vastauksen laatuun.

Saadaksesi intuitiota siitä, miten tokenisaatio toimii, kokeile työkaluja, kuten [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), joka on esitetty alla. Kopioi promptisi – ja katso, miten se muunnetaan tokeneiksi, kiinnittäen huomiota siihen, miten välilyöntimerkit ja välimerkit käsitellään. Huomaa, että tämä esimerkki näyttää vanhemman LLM:n (GPT-3) – joten kokeilemalla tätä uudemmalla mallilla tulos voi olla erilainen.

![Tokenisaatio](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.fi.png)

### Käsite: Perustamallit

Kun prompti on tokenisoitu, ["Perus-LLM:n"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (tai perustamallin) ensisijainen tehtävä on ennustaa seuraava token sarjassa. Koska LLM:t on koulutettu valtavilla tekstidatamäärillä, niillä on hyvä käsitys tokenien välisistä tilastollisista suhteista ja ne voivat tehdä ennustuksen jonkinlaisella varmuudella. Huomaa, että ne eivät ymmärrä sanojen _merkitystä_ promptissa tai tokenissa; ne näkevät vain kuvion, jonka ne voivat "täydentää" seuraavalla ennustuksellaan. Ne voivat jatkaa sarjan ennustamista, kunnes käyttäjä keskeyttää prosessin tai jokin ennalta määritetty ehto täyttyy.

Haluatko nähdä, miten prompt-pohjainen täydentäminen toimii? Syötä yllä oleva prompti Azure OpenAI Studion [_Chat Playgroundiin_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) oletusasetuksilla. Järjestelmä on konfiguroitu käsittelemään promptit tietopyyntöinä – joten sinun pitäisi nähdä täydentäminen, joka vastaa tätä kontekstia.

Mutta entä jos käyttäjä halusi nähdä jotain erityistä, joka täyttää tietyt kriteerit tai tehtävätavoitteen? Tässä _ohjeistuksella hienosäädetyt_ LLM:t astuvat kuvaan.

![Perus-LLM Chat Completion](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.fi.png)

### Käsite: Ohjeistuksella hienosäädetyt LLM:t

[Ohjeistuksella hienosäädetty LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) alkaa perustamallista ja hienosäätää sitä esimerkeillä tai syöte/vastauspareilla (esim. monivaiheiset "viestit"), jotka voivat sisältää selkeitä ohjeita – ja tekoälyn vastaus pyrkii seuraamaan näitä ohjeita.

Tämä käyttää tekniikoita, kuten vahvistusoppimista ihmisen palautteen avulla (RLHF), joka voi kouluttaa mallia _seuraamaan ohjeita_ ja _oppimaan palautteesta_, jotta se tuottaa vastauksia, jotka sopivat paremmin käytännön sovelluksiin ja ovat relevantimpia käyttäjän tavoitteille.

Kokeillaan – palaa yllä olevaan promptiin, mutta muuta nyt _järjestelmäviesti_ antamaan seuraava ohje kontekstina:

> _Tiivistä sinulle annettu sisältö toisen luokan oppilaalle. Pidä tulos yhdessä kappaleessa, jossa on 3–5 kohtaa._

Huomaatko, miten tulos on nyt hienosäädetty vastaamaan haluttua tavoitetta ja muotoa? Opettaja voi nyt käyttää tätä vastausta suoraan luokkansa dioissa.

![Ohjeistuksella hienosäädetty LLM Chat Completion](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.fi.png)

## Miksi tarvitsemme promptien suunnittelua?

Nyt kun tiedämme, miten LLM:t käsittelevät promptia, puhutaan siitä, _miksi_ tarvitsemme promptien suunnittelua. Vastaus löytyy siitä, että nykyiset LLM:t tuovat mukanaan useita haasteita, jotka tekevät _luotettavien ja johdonmukaisten täydentämisten_ saavuttamisesta haastavampaa ilman, että panostamme promptin rakentamiseen ja optimointiin. Esimerkiksi:

1. **Mallien vastaukset ovat satunnaisia.** _Sama prompti_ tuottaa todennäköisesti erilaisia vastauksia eri malleilla tai malliversioilla. Ja se voi tuottaa erilaisia tuloksia jopa _samalla mallilla_ eri aikoina. _Promptien suunnittelutekniikat voivat auttaa meitä minimoimaan nämä vaihtelut tarjoamalla parempia ohjauskehyksiä_.  

1. **Mallit voivat keksiä vastauksia.** Mallit on esikoulutettu _laajoilla mutta rajallisilla_ datamäärillä, mikä tarkoittaa, että niiltä puuttuu tietoa koulutuksen ulkopuolisista käsitteistä. Tämän seurauksena ne voivat tuottaa täydentämisiä, jotka ovat epätarkkoja, kuvitteellisia tai suoraan ristiriidassa tunnettujen faktojen kanssa. _Promptien suunnittelutekniikat auttavat käyttäjiä tunnistamaan ja lieventämään tällaisia keksintöjä, esim. pyytämällä tekoälyä antamaan lähteitä tai perusteluja_.  

1. **Mallien kyvyt vaihtelevat.** Uudemmilla malleilla tai mallisukupolvilla on rikkaampia ominaisuuksia, mutta ne tuovat myös mukanaan ainutlaatuisia piirteitä ja kompromisseja kustannusten ja monimutkaisuuden suhteen. _Promptien suunnittelu voi auttaa meitä kehittämään parhaita käytäntöjä ja työnkulkuja, jotka abstrahoivat erot ja mukautuvat mallikohtaisiin vaatimuksiin skaalautuvilla ja saumattomilla tavoilla_.  

Katsotaanpa tätä käytännössä OpenAI:n tai Azure OpenAI Playgroundissa:

- Käytä samaa promptia eri LLM-toteutuksilla (esim. OpenAI, Azure OpenAI, Hugging Face) – huomasitko vaihtelut?  
- Käytä samaa promptia toistuvasti _samalla_ LLM-toteutuksella (esim. Azure OpenAI Playground) – miten nämä vaihtelut erosivat?  

### Keksintöjen esimerkki

Tässä kurssissa käytämme termiä **"keksintö"** viittaamaan ilmiöön, jossa LLM:t joskus tuottavat tosiasiallisesti virheellistä tietoa koulutuksen rajoitusten tai muiden rajoitteiden vuoksi. Olet ehkä kuullut tästä puhuttavan myös _"hallusinaationa"_ suosituissa artikkeleissa tai tutkimuspapereissa. Suosittelemme kuitenkin vahvasti käyttämään termiä _"keksintö"_, jotta emme vahingossa inhimillistäisi käyttäytymistä antamalla ihmismäisen piirteen koneohjatulle tulokselle. Tämä myös vahvistaa [Vastuullisen tekoälyn ohjeita](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminologian näkökulmasta, poistamalla termejä, jotka voivat olla loukkaavia tai ei-sisällyttäviä joissakin konteksteissa.

Haluatko saada käsityksen siitä, miten keksinnöt toimivat? Mieti promptia, joka ohjeistaa tekoälyä tuottamaan sisältöä olemattomasta aiheesta (jotta varmist
Verkkohaku osoitti, että Marsin sodista on olemassa fiktiivisiä kertomuksia (esim. televisiosarjoja tai kirjoja) – mutta ei vuodelta 2076. Järki kertoo myös, että vuosi 2076 on _tulevaisuudessa_ eikä siksi voi liittyä todelliseen tapahtumaan.

Mitä tapahtuu, kun käytämme tätä kehotetta eri LLM-palveluntarjoajien kanssa?

> **Vastaus 1**: OpenAI Playground (GPT-35)

![Vastaus 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.fi.png)

> **Vastaus 2**: Azure OpenAI Playground (GPT-35)

![Vastaus 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.fi.png)

> **Vastaus 3**: Hugging Face Chat Playground (LLama-2)

![Vastaus 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.fi.png)

Kuten odotettua, jokainen malli (tai malliversio) tuottaa hieman erilaisia vastauksia johtuen stokastisesta käyttäytymisestä ja mallien kyvykkyyksien eroista. Esimerkiksi yksi malli kohdistaa vastauksensa kahdeksannen luokan yleisölle, kun taas toinen olettaa lukion opiskelijan. Mutta kaikki kolme mallia tuottivat vastauksia, jotka voisivat vakuuttaa tietämättömän käyttäjän siitä, että tapahtuma oli todellinen.

Kehotetekniikat, kuten _metakehotus_ ja _lämpötilan säätö_, voivat vähentää mallien virheellisiä väitteitä jossain määrin. Uudet kehotetekniikoiden _arkkitehtuurit_ myös integroivat uusia työkaluja ja tekniikoita saumattomasti kehotusprosessiin, lieventääkseen tai vähentääkseen näitä vaikutuksia.

## Tapaustutkimus: GitHub Copilot

Päätetään tämä osio tutustumalla siihen, miten kehotetekniikoita käytetään tosielämän ratkaisuissa tarkastelemalla yhtä tapaustutkimusta: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot on "tekoälykoodauspari" – se muuntaa tekstikehotteet koodiehdotuksiksi ja on integroitu kehitysympäristöösi (esim. Visual Studio Code) saumattoman käyttökokemuksen tarjoamiseksi. Kuten alla olevassa blogisarjassa dokumentoidaan, varhaisimmat versiot perustuivat OpenAI Codex -malliin – ja insinöörit huomasivat nopeasti tarpeen hienosäätää mallia ja kehittää parempia kehotetekniikoita koodin laadun parantamiseksi. Heinäkuussa he [julkaisivat parannetun tekoälymallin, joka menee Codexin yli](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) tarjoten entistä nopeampia ehdotuksia.

Lue blogit järjestyksessä, jotta voit seurata heidän oppimismatkaansa.

- **Toukokuu 2023** | [GitHub Copilot ymmärtää koodiasi entistä paremmin](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Toukokuu 2023** | [GitHubin sisällä: Työskentely GitHub Copilotin LLM-mallien kanssa](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Kesäkuu 2023** | [Kuinka kirjoittaa parempia kehotteita GitHub Copilotille](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Heinäkuu 2023** | [.. GitHub Copilot menee Codexin yli parannetulla tekoälymallilla](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Heinäkuu 2023** | [Kehittäjän opas kehotetekniikoihin ja LLM-malleihin](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Syyskuu 2023** | [Kuinka rakentaa yritystason LLM-sovellus: Oppeja GitHub Copilotista](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Voit myös selata heidän [Engineering-blogiaan](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) löytääksesi lisää postauksia, kuten [tämän](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), joka näyttää, miten näitä malleja ja tekniikoita _sovelletaan_ tosielämän sovellusten kehittämiseen.

---

## Kehotteen rakentaminen

Olemme nähneet, miksi kehotetekniikka on tärkeää – nyt ymmärretään, miten kehotteet _rakennetaan_, jotta voimme arvioida eri tekniikoita tehokkaamman kehotteen suunnitteluun.

### Peruskehotus

Aloitetaan peruskehotteesta: tekstisyöte, joka lähetetään mallille ilman muuta kontekstia. Tässä esimerkki – kun lähetämme Yhdysvaltain kansallislaulun ensimmäiset sanat OpenAI:n [Completion API:lle](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), se täydentää vastauksen seuraavilla riveillä, havainnollistaen perusennustuskäyttäytymistä.

| Kehotus (Syöte)     | Täydennys (Vastaus)                                                                                                                        |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see  | Kuulostaa siltä, että aloitat "The Star-Spangled Banner" -kappaleen sanat, joka on Yhdysvaltain kansallislaulu. Koko sanat ovat ...         |

### Monimutkainen kehotus

Lisätään nyt konteksti ja ohjeet peruskehotteeseen. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) antaa meidän rakentaa monimutkaisen kehotteen _viestien_ kokoelmana, jossa:

- Syöte/vastausparit heijastavat _käyttäjän_ syötettä ja _avustajan_ vastausta.
- Järjestelmäviesti asettaa kontekstin avustajan käyttäytymiselle tai persoonallisuudelle.

Pyyntö on nyt alla olevan muotoinen, jossa _tokenisointi_ tehokkaasti tallentaa relevantin tiedon kontekstista ja keskustelusta. Järjestelmän kontekstin muuttaminen voi olla yhtä vaikuttavaa täydennysten laadulle kuin käyttäjän antamat syötteet.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```


### Ohjekehotus

Yllä olevissa esimerkeissä käyttäjän kehotus oli yksinkertainen tekstikysely, joka voidaan tulkita tiedonhakupyynnöksi. _Ohjekehotuksilla_ voimme käyttää tekstiä tehtävän tarkempaan määrittelyyn, tarjoten parempaa ohjausta tekoälylle. Tässä esimerkki:

| Kehotus (Syöte)                                                                                                                                                                                                                         | Täydennys (Vastaus)                                                                                                        | Ohjetyyppi          |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Kirjoita kuvaus sisällissodasta                                                                                                                                                                                                        | _palautti yksinkertaisen kappaleen_                                                                                         | Yksinkertainen      |
| Kirjoita kuvaus sisällissodasta. Anna keskeiset päivämäärät ja tapahtumat ja kuvaile niiden merkitys                                                                                                                                   | _palautti kappaleen, jota seurasi lista keskeisistä tapahtumapäivämääristä ja kuvauksista_                                  | Monimutkainen       |
| Kirjoita kuvaus sisällissodasta yhdessä kappaleessa. Anna 3 luettelopistettä keskeisistä päivämääristä ja niiden merkityksestä. Anna 3 lisää luettelopistettä keskeisistä historiallisista henkilöistä ja heidän panoksistaan. Palauta vastaus JSON-tiedostona | _palautti laajemmat tiedot tekstilaatikossa, joka on muotoiltu JSON-muotoon ja jonka voi kopioida ja liittää tiedostoon_    | Monimutkainen. Muotoiltu. |

## Ensisijainen sisältö

Yllä olevissa esimerkeissä kehotus oli edelleen melko avoin, jolloin LLM päätti, mikä osa sen esikoulutetusta tietokannasta oli relevanttia. _Ensisijaisen sisällön_ suunnittelumallissa syöteteksti jaetaan kahteen osaan:

- ohje (toiminta)
- relevantti sisältö (joka vaikuttaa toimintaan)

Tässä esimerkki, jossa ohjeena on "tiivistä tämä kahteen lauseeseen".

| Kehotus (Syöte)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Täydennys (Vastaus)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter on viides planeetta Auringosta ja suurin aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden aurinkokunnan planeettojen yhteenlaskettu massa. Jupiter on yksi kirkkaimmista paljaalla silmällä näkyvistä kohteista yötaivaalla, ja se on ollut tunnettu muinaisista sivilisaatioista jo ennen kirjoitettua historiaa. Se on nimetty roomalaisen jumalan Jupiterin mukaan. Kun Jupiteria katsotaan Maasta, se voi olla niin kirkas, että sen heijastunut valo voi luoda näkyviä varjoja, ja se on keskimäärin kolmanneksi kirkkain luonnollinen kohde yötaivaalla Kuun ja Venuksen jälkeen. <br/> **Tiivistä tämä kahteen lyhyeen lauseeseen** | Jupiter, viides planeetta Auringosta, on aurinkokunnan suurin ja yksi kirkkaimmista kohteista yötaivaalla. Roomalaisen jumalan mukaan nimetty Jupiter on kaasujättiläinen, jonka massa on kaksi ja puoli kertaa kaikkien muiden aurinkokunnan planeettojen yhteenlaskettu massa. |

Ensisijaisen sisältösegmentin avulla voidaan ohjata tehokkaampia ohjeita eri tavoin:

- **Esimerkit** – sen sijaan, että kerrot mallille, mitä tehdä eksplisiittisellä ohjeella, anna sille esimerkkejä siitä, mitä tehdä, ja anna sen päätellä kaava.
- **Vihjeet** – seuraa ohjetta "vihjeellä", joka ohjaa täydennystä, ohjaten mallia kohti relevantimpia vastauksia.
- **Pohjat** – nämä ovat toistettavia 'reseptikehotteita', joissa on paikkamerkkejä (muuttujia), joita voidaan mukauttaa tiettyihin käyttötapauksiin.

Tutkitaan näitä käytännössä.

### Esimerkkien käyttö

Tämä on lähestymistapa, jossa käytät ensisijaista sisältöä "syöttämään mallille" joitakin esimerkkejä halutusta tuotoksesta tietylle ohjeelle ja annat sen päätellä kaavan halutulle tuotokselle. Esimerkkien määrän perusteella voimme käyttää nollashottikehotusta, yksishottikehotusta, muutamanshottikehotusta jne.

Kehotus koostuu nyt kolmesta osasta:

- Tehtävän kuvaus
- Muutama esimerkki halutusta tuotoksesta
- Uuden esimerkin alku (joka toimii implisiittisenä tehtävän kuvauksena)

| Oppimistyyppi | Kehotus (Syöte)                                                                                                                                        | Täydennys (Vastaus)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Nollashotti   | "Aurinko paistaa". Käännä espanjaksi                                                                                                                  | "El Sol está brillando".    |
| Yksishotti    | "Aurinko paistaa" => ""El Sol está brillando". <br> "On kylmä ja tuulinen päivä" =>                                                                    | "Es un día frío y ventoso". |
| Muutamanshotti| Pelaaja juoksi pesät => Baseball <br/> Pelaaja löi ässän => Tennis <br/> Pelaaja löi kuutosen => Cricket <br/> Pelaaja teki donkin =>                 | Koripallo                   |
|               |                                                                                                                                                       |                             |

Huomaa, kuinka meidän piti antaa eksplisiittinen ohje ("Käännä espanjaksi") nollashottikehotuksessa, mutta se päätellään yksishottikehotuksen esimerkissä. Muutamanshottiesimerkki näyttää, kuinka lisäämällä enemmän esimerkkejä mallit voivat tehdä tarkempia päätelmiä ilman lisäohjeita.

### Kehotusvihjeet

Toinen ensisijaisen sisällön käyttötapa on antaa _vihjeitä_ esimerkkien sijaan. Tässä tapauksessa annamme mallille "sysäyksen" oikeaan suuntaan _aloittamalla_ sen halutun vastausmuodon heijastavalla katkelmalla. Malli sitten "ottaa vihjeen" ja jatkaa samalla tavalla.

| Vihjeiden määrä | Kehotus (Syöte)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Täydennys (Vastaus)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter on viides planeetta Auringosta ja suurin aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden aurinkokunnan planeettojen yhteenlaskettu massa. Jupiter on yksi kirkkaimmista paljaalla silmällä näkyvistä kohteista yötaivaalla, ja se on ollut tunnettu muinaisista sivilisaatioista jo ennen kirjoitettua historiaa. <br/>**Tiivistä tämä**                                       | Jupiter on aurinkokunnan suurin planeetta ja viides Auringosta. Se on kaasujättiläinen, jonka massa on 1/1000 Auringon massasta, mutta se on painavampi kuin kaikki muut planeetat yhteensä. Muinaiset sivilisaatiot ovat tunteneet Jupiterin pitkään, ja se näkyy helposti yötaivaalla. |
| 1              | Jupiter on viides planeetta Auringosta ja suurin planeetta aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa suurempi kuin kaikkien muiden aurinkokunnan planeettojen yhteenlaskettu massa. Jupiter on yksi kirkkaimmista kohteista, jotka ovat paljain silmin nähtävissä yötaivaalla, ja se on ollut tunnettu muinaisista sivilisaatioista jo ennen kirjoitettua historiaa. <br/>**Tiivistä Tämä** <br/> Opimme, että Jupiter | on viides planeetta Auringosta ja suurin aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa suurempi kuin kaikkien muiden planeettojen yhteenlaskettu massa. Se on helposti nähtävissä paljain silmin ja tunnettu muinaisista ajoista lähtien.                        |
| 2              | Jupiter on viides planeetta Auringosta ja suurin planeetta aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa suurempi kuin kaikkien muiden aurinkokunnan planeettojen yhteenlaskettu massa. Jupiter on yksi kirkkaimmista kohteista, jotka ovat paljain silmin nähtävissä yötaivaalla, ja se on ollut tunnettu muinaisista sivilisaatioista jo ennen kirjoitettua historiaa. <br/>**Tiivistä Tämä** <br/> Top 3 Faktaa, jotka opimme:         | 1. Jupiter on viides planeetta Auringosta ja suurin aurinkokunnassa. <br/> 2. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta...<br/> 3. Jupiter on ollut paljain silmin nähtävissä muinaisista ajoista lähtien ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt-mallit

Prompt-malli on _ennalta määritelty resepti promptille_, joka voidaan tallentaa ja käyttää uudelleen tarpeen mukaan, jotta käyttäjäkokemukset olisivat johdonmukaisempia laajassa mittakaavassa. Yksinkertaisimmillaan se on vain kokoelma prompt-esimerkkejä, kuten [tämä OpenAI:n esimerkki](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), joka sisältää sekä interaktiiviset prompt-komponentit (käyttäjän ja järjestelmän viestit) että API-pohjaisen pyyntöformaatin - tukemaan uudelleenkäyttöä.

Monimutkaisemmassa muodossaan, kuten [tämä LangChain-esimerkki](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), se sisältää _paikkamerkkejä_, jotka voidaan korvata tiedoilla eri lähteistä (käyttäjän syöte, järjestelmän konteksti, ulkoiset tietolähteet jne.) luodakseen promptin dynaamisesti. Tämä mahdollistaa kirjaston luomisen uudelleenkäytettäviä prompt-malleja, joita voidaan käyttää johdonmukaisten käyttäjäkokemusten luomiseen **ohjelmallisesti** laajassa mittakaavassa.

Lopulta mallien todellinen arvo piilee kyvyssä luoda ja julkaista _prompt-kirjastoja_ vertikaalisille sovellusalueille - missä prompt-malli on nyt _optimoitu_ heijastamaan sovelluskohtaisia konteksteja tai esimerkkejä, jotka tekevät vastauksista kohdeyleisölle merkityksellisempiä ja tarkempia. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) -tietovarasto on hyvä esimerkki tästä lähestymistavasta, joka kuratoi kirjaston prompt-malleja koulutusalalle keskittyen keskeisiin tavoitteisiin, kuten oppituntien suunnitteluun, opetussuunnitelman suunnitteluun, opiskelijoiden ohjaukseen jne.

## Tukisisältö

Jos ajattelemme promptin rakentamista tehtävän (ohjeen) ja kohteen (ensisijaisen sisällön) yhdistelmänä, niin _toissijainen sisältö_ on kuin lisäkonteksti, jonka tarjoamme **vaikuttaaksemme lopputulokseen jollain tavalla**. Se voi olla säätöparametreja, muotoiluohjeita, aiheiden taksonomioita jne., jotka auttavat mallia _räätälöimään_ vastauksensa vastaamaan haluttuja käyttäjätavoitteita tai odotuksia.

Esimerkiksi: Kun käytettävissä on kurssiluettelo, jossa on laaja metadata (nimi, kuvaus, taso, metadatatunnisteet, ohjaaja jne.) kaikista opetussuunnitelman kursseista:

- voimme määritellä ohjeen "tiivistä kurssiluettelo syksylle 2023"
- voimme käyttää ensisijaista sisältöä tarjoamaan muutamia esimerkkejä halutusta lopputuloksesta
- voimme käyttää toissijaista sisältöä tunnistamaan viisi tärkeintä "tunnistetta", jotka kiinnostavat.

Nyt malli voi tarjota tiivistelmän esimerkkien osoittamassa muodossa - mutta jos tuloksessa on useita tunnisteita, se voi priorisoida toissijaisessa sisällössä tunnistetut viisi tärkeintä tunnistetta.

---

<!--
OPPITUNTIMALLI:
Tämän yksikön tulisi kattaa ydinkonsepti #1.
Vahvista konsepti esimerkeillä ja viitteillä.

KONSEPTI #3:
Promptin suunnittelutekniikat.
Mitkä ovat joitakin perusmenetelmiä promptin suunnittelussa?
Havainnollista harjoituksilla.
-->

## Promptin parhaat käytännöt

Nyt kun tiedämme, miten promptit voidaan _rakentaa_, voimme alkaa miettiä, miten ne voidaan _suunnitella_ heijastamaan parhaita käytäntöjä. Voimme ajatella tätä kahdessa osassa - oikean _ajattelutavan_ omaksuminen ja oikeiden _tekniikoiden_ soveltaminen.

### Promptin suunnittelun ajattelutapa

Promptin suunnittelu on kokeiluun perustuva prosessi, joten pidä mielessä kolme laajaa ohjaavaa tekijää:

1. **Alakohtainen ymmärrys on tärkeää.** Vastausten tarkkuus ja merkityksellisyys riippuvat sovelluksen tai käyttäjän toiminta-alasta. Käytä intuitiotasi ja alakohtaista asiantuntemustasi **räätälöidäksesi tekniikoita** edelleen. Esimerkiksi määrittele _alakohtaisia persoonallisuuksia_ järjestelmäprompteissasi tai käytä _alakohtaisia malleja_ käyttäjäprompteissasi. Tarjoa toissijaista sisältöä, joka heijastaa alakohtaisia konteksteja, tai käytä _alakohtaisia vihjeitä ja esimerkkejä_ ohjataksesi mallia kohti tuttuja käyttötapoja.

2. **Mallin ymmärtäminen on tärkeää.** Tiedämme, että mallit ovat luonteeltaan satunnaisia. Mutta mallien toteutukset voivat myös vaihdella käyttämänsä koulutusdatan (esikoulutettu tieto), tarjoamiensa ominaisuuksien (esim. API:n tai SDK:n kautta) ja optimoimansa sisällön tyypin (esim. koodi vs. kuvat vs. teksti) suhteen. Ymmärrä käyttämäsi mallin vahvuudet ja rajoitukset, ja käytä tätä tietoa _tehtävien priorisointiin_ tai _räätälöityjen mallien_ rakentamiseen, jotka on optimoitu mallin ominaisuuksille.

3. **Iterointi ja validointi ovat tärkeitä.** Mallit kehittyvät nopeasti, samoin promptin suunnittelutekniikat. Alakohtaisena asiantuntijana sinulla voi olla muuta kontekstia tai kriteerejä, jotka koskevat _sinun_ erityistä sovellustasi, mutta eivät välttämättä koske laajempaa yhteisöä. Käytä promptin suunnittelutyökaluja ja -tekniikoita "käynnistääksesi" promptin rakentamisen, sitten iteroi ja validoi tulokset oman intuitiosi ja alakohtaisen asiantuntemuksesi avulla. Tallenna oivalluksesi ja luo **tietopohja** (esim. prompt-kirjastoja), joita muut voivat käyttää uutena lähtökohtana nopeampaan iterointiin tulevaisuudessa.

## Parhaat käytännöt

Tarkastellaan nyt yleisiä parhaita käytäntöjä, joita suosittelevat [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ja [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) -käytännön asiantuntijat.

| Mitä                              | Miksi                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Arvioi uusimmat mallit.           | Uudet mallisukupolvet todennäköisesti sisältävät parannettuja ominaisuuksia ja laatua - mutta voivat myös aiheuttaa korkeampia kustannuksia. Arvioi niiden vaikutus ja tee sitten siirtymispäätökset.                                                |
| Erottele ohjeet ja konteksti      | Tarkista, määrittääkö mallisi/palveluntarjoajasi _erottimia_, jotka erottavat ohjeet, ensisijaisen ja toissijaisen sisällön selkeämmin. Tämä voi auttaa malleja määrittämään painotukset tarkemmin tokeneille.                                      |
| Ole tarkka ja selkeä             | Anna enemmän yksityiskohtia halutusta kontekstista, lopputuloksesta, pituudesta, muodosta, tyylistä jne. Tämä parantaa sekä vastausten laatua että johdonmukaisuutta. Tallenna reseptit uudelleenkäytettäviin malleihin.                              |
| Ole kuvaileva, käytä esimerkkejä  | Mallit voivat vastata paremmin "näytä ja kerro" -lähestymistapaan. Aloita `zero-shot`-lähestymistavalla, jossa annat sille ohjeen (mutta ei esimerkkejä), ja kokeile sitten `few-shot`-lähestymistapaa, jossa annat muutamia esimerkkejä halutusta lopputuloksesta. Käytä analogioita. |
| Käytä vihjeitä käynnistääksesi vastaukset | Ohjaa sitä kohti haluttua lopputulosta antamalla sille joitakin johtavia sanoja tai lauseita, joita se voi käyttää vastauksen lähtökohtana.                                                                                                       |
| Toista tarvittaessa               | Joskus sinun täytyy toistaa itsesi mallille. Anna ohjeet ennen ja jälkeen ensisijaisen sisällön, käytä ohjetta ja vihjettä jne. Iteroi ja validoi nähdäksesi, mikä toimii.                                                                          |
| Järjestyksellä on merkitystä      | Tiedon esittämisjärjestys mallille voi vaikuttaa lopputulokseen, jopa oppimisesimerkeissä, kiitos tuoreusvinouman. Kokeile eri vaihtoehtoja nähdäksesi, mikä toimii parhaiten.                                                                        |
| Anna mallille "poistumistie"      | Anna mallille _varavaihtoehto_, jonka se voi tarjota, jos se ei voi suorittaa tehtävää mistä tahansa syystä. Tämä voi vähentää mallien väärien tai keksittyjen vastausten tuottamisen mahdollisuuksia.                                               |
|                                   |                                                                                                                                                                                                                                                   |

Kuten minkä tahansa parhaan käytännön kohdalla, muista, että _kokemuksesi voivat vaihdella_ mallin, tehtävän ja alan mukaan. Käytä näitä lähtökohtana ja iteroi löytääksesi, mikä toimii parhaiten sinulle. Arvioi jatkuvasti promptin suunnitteluprosessiasi, kun uusia malleja ja työkaluja tulee saataville, keskittyen prosessin skaalautuvuuteen ja vastausten laatuun.

<!--
OPPITUNTIMALLI:
Tämän yksikön tulisi tarjota koodiharjoitus, jos sovellettavissa.

HARJOITUS:
Linkki Jupyter Notebookiin, jossa vain koodikommentit ovat ohjeissa (koodiosiot ovat tyhjiä).

RATKAISU:
Linkki kopioon Notebookista, jossa promptit on täytetty ja suoritettu, näyttäen yhden esimerkin.
-->

## Tehtävä

Onnittelut! Pääsit oppitunnin loppuun! Nyt on aika testata joitakin näistä konsepteista ja tekniikoista todellisten esimerkkien avulla!

Tehtävää varten käytämme Jupyter Notebookia, jossa on harjoituksia, joita voit suorittaa interaktiivisesti. Voit myös laajentaa Notebookia omilla Markdown- ja koodisoluilla tutkiaksesi ideoita ja tekniikoita itsenäisesti.

### Aloittaaksesi, haarauta repo, sitten

- (Suositeltu) Käynnistä GitHub Codespaces
- (Vaihtoehtoisesti) Kloonaa repo paikalliselle laitteellesi ja käytä sitä Docker Desktopin kanssa
- (Vaihtoehtoisesti) Avaa Notebook suosikkisi Notebook-ajoalustalla.

### Seuraavaksi, määritä ympäristömuuttujat

- Kopioi `.env.copy` tiedosto repokansiosta `.env`-tiedostoksi ja täytä `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ja `AZURE_OPENAI_DEPLOYMENT` arvot. Palaa [Learning Sandbox -osioon](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) oppiaksesi lisää.

### Seuraavaksi, avaa Jupyter Notebook

- Valitse ajoalustan ydin. Jos käytät vaihtoehtoja 1 tai 2, valitse yksinkertaisesti oletus Python 3.10.x -ydin, jonka kehityskontti tarjoaa.

Olet valmis suorittamaan harjoitukset. Huomaa, että tässä ei ole _oikeita ja vääriä_ vastauksia - vain vaihtoehtojen tutkimista kokeilemalla ja virheillä ja intuition rakentamista siitä, mikä toimii tietylle mallille ja sovellusalueelle.

_Tämän vuoksi tässä oppitunnissa ei ole koodiratkaisuosioita. Sen sijaan Notebookissa on Markdown-solut otsikolla "My Solution:", jotka näyttävät yhden esimerkkituloksen viitteeksi._

 <!--
OPPITUNTIMALLI:
Päätä osio yhteenvedolla ja resursseilla itseohjautuvaan oppimiseen.
-->

## Tietojen tarkistus

Mikä seuraavista on hyvä prompt, joka noudattaa kohtuullisia parhaita käytäntöjä?

1. Näytä minulle kuva punaisesta autosta
2. Näytä minulle kuva punaisesta autosta, merkki Volvo ja malli XC90, pysäköitynä kallion reunalle auringon laskiessa
3. Näytä minulle kuva punaisesta autosta, merkki Volvo ja malli XC90

V: 2, se on paras prompt, koska se antaa yksityiskohtia "mitä" ja menee tarkempiin yksityiskohtiin (ei vain mikä tahansa auto, vaan tietty merkki ja malli) ja se myös kuvailee yleistä ympäristöä. 3 on seuraavaksi paras, koska se sisältää myös paljon kuvailua.

## 🚀 Haaste

Katso, voitko hyödyntää "vihje"-tekniikkaa promptilla: Täydennä lause "Näytä minulle kuva punaisesta autosta, merkki Volvo ja ". Mitä se vastaa, ja miten parantaisit sitä?

## Hienoa työtä! Jatka oppimista

Haluatko oppia lisää erilaisista Promptin suunnittelukonsepteista? Siirry [jatkuvan oppimisen sivulle](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) löytääksesi muita loistavia resursseja tästä aiheesta.

Siirry oppituntiin 5, jossa tarkastelemme [edistyneitä prompt-tekniikoita](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.