<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0135e6c271f3ece8699050d4debbce88",
  "translation_date": "2025-10-17T19:47:00+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "fi"
}
-->
# Promptien suunnittelun perusteet

[![Promptien suunnittelun perusteet](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.fi.png)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Johdanto
Tämä moduuli käsittelee keskeisiä käsitteitä ja tekniikoita tehokkaiden kehotteiden luomiseksi generatiivisissa tekoälymalleissa. Tapa, jolla kirjoitat kehotteen LLM:lle, vaikuttaa myös lopputulokseen. Huolellisesti laadittu kehotus voi tuottaa laadukkaamman vastauksen. Mutta mitä tarkalleen ottaen tarkoittavat termit _kehotus_ ja _promptien suunnittelu_? Ja miten voin parantaa kehotteen _syötettä_, jonka lähetän LLM:lle? Näihin kysymyksiin pyrimme vastaamaan tässä ja seuraavassa luvussa.

_Generatiivinen tekoäly_ pystyy luomaan uutta sisältöä (esim. tekstiä, kuvia, ääntä, koodia jne.) käyttäjän pyyntöjen perusteella. Se saavuttaa tämän käyttämällä _suuria kielimalleja_ kuten OpenAI:n GPT ("Generative Pre-trained Transformer") -sarjaa, jotka on koulutettu käyttämään luonnollista kieltä ja koodia.

Käyttäjät voivat nyt olla vuorovaikutuksessa näiden mallien kanssa tuttujen toimintatapojen, kuten chatin, kautta ilman teknistä asiantuntemusta tai koulutusta. Mallit ovat _kehotuspohjaisia_ - käyttäjät lähettävät tekstisyötteen (kehotus) ja saavat takaisin tekoälyn vastauksen (täydennys). He voivat sitten "keskustella tekoälyn kanssa" iteratiivisesti, monivaiheisissa keskusteluissa, hienosäätäen kehotettaan, kunnes vastaus vastaa heidän odotuksiaan.

"Kehotukset" ovat nyt generatiivisten tekoälysovellusten ensisijainen _ohjelmointirajapinta_, joka kertoo malleille, mitä tehdä ja vaikuttaa palautettujen vastausten laatuun. "Promptien suunnittelu" on nopeasti kasvava tutkimusala, joka keskittyy kehotusten _suunnitteluun ja optimointiin_ johdonmukaisten ja laadukkaiden vastausten tuottamiseksi laajassa mittakaavassa.

## Oppimistavoitteet

Tässä oppitunnissa opimme, mitä promptien suunnittelu on, miksi se on tärkeää ja miten voimme laatia tehokkaampia kehotuksia tietylle mallille ja sovellustavoitteelle. Ymmärrämme keskeiset käsitteet ja parhaat käytännöt promptien suunnittelussa - ja opimme interaktiivisesta Jupyter Notebooks - "hiekkalaatikko"-ympäristöstä, jossa voimme soveltaa näitä käsitteitä todellisiin esimerkkeihin.

Oppitunnin lopussa osaamme:

1. Selittää, mitä promptien suunnittelu on ja miksi se on tärkeää.
2. Kuvailla kehotteen osat ja niiden käyttötavat.
3. Oppia parhaat käytännöt ja tekniikat promptien suunnitteluun.
4. Soveltaa opittuja tekniikoita todellisiin esimerkkeihin käyttäen OpenAI:n rajapintaa.

## Keskeiset termit

Promptien suunnittelu: Käytäntö suunnitella ja hienosäätää syötteitä ohjaamaan tekoälymalleja tuottamaan haluttuja tuloksia.  
Tokenisaatio: Prosessi, jossa teksti muunnetaan pienemmiksi yksiköiksi, joita kutsutaan tokeneiksi, joita malli voi ymmärtää ja käsitellä.  
Ohjeviritetyt LLM:t: Suuret kielimallit (LLM:t), joita on hienosäädetty erityisillä ohjeilla vastausten tarkkuuden ja osuvuuden parantamiseksi.

## Oppimishiekkalaatikko

Promptien suunnittelu on tällä hetkellä enemmän taidetta kuin tiedettä. Paras tapa parantaa intuitiota sen suhteen on _harjoitella enemmän_ ja omaksua kokeiluun ja erehdykseen perustuva lähestymistapa, joka yhdistää sovellusalueen asiantuntemuksen suositeltuihin tekniikoihin ja mallikohtaisiin optimointeihin.

Tämän oppitunnin mukana tuleva Jupyter Notebook tarjoaa _hiekkalaatikko_-ympäristön, jossa voit kokeilla oppimaasi - joko oppitunnin aikana tai lopun koodaushaasteen osana. Harjoitusten suorittamiseen tarvitset:

1. **Azure OpenAI API -avaimen** - palvelupisteen käyttöönotetulle LLM:lle.  
2. **Python-ympäristön** - jossa Notebook voidaan suorittaa.  
3. **Paikalliset ympäristömuuttujat** - _suorita [ASENNUS](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) -vaiheet nyt valmistautuaksesi_.  

Notebook sisältää _aloitusharjoituksia_ - mutta sinua rohkaistaan lisäämään omia _Markdown_- (kuvaus) ja _Code_- (kehotuspyynnöt) osioita kokeillaksesi lisää esimerkkejä tai ideoita - ja kehittääksesi intuitiotasi kehotusten suunnittelussa.

## Kuvitettu opas

Haluatko saada yleiskuvan siitä, mitä tämä oppitunti kattaa ennen kuin sukellat syvemmälle? Tutustu tähän kuvitettuun oppaaseen, joka antaa sinulle käsityksen pääaiheista ja keskeisistä huomioista, joita kannattaa miettiä kunkin aiheen kohdalla. Oppitunnin etenemissuunnitelma vie sinut ydinkäsitteiden ja haasteiden ymmärtämisestä niiden käsittelyyn asiaankuuluvilla promptien suunnittelutekniikoilla ja parhailla käytännöillä. Huomaa, että tämän oppaan "Edistyneet tekniikat" -osio viittaa seuraavan luvun sisältöön tässä oppimateriaalissa.

![Kuvitettu opas promptien suunnitteluun](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.fi.png)

## Startupimme

Puhutaanpa siitä, miten _tämä aihe_ liittyy startupimme missioon [tuoda tekoälyinnovaatioita koulutukseen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Haluamme rakentaa tekoälypohjaisia sovelluksia _henkilökohtaiselle oppimiselle_ - joten mietitään, miten eri käyttäjät sovelluksessamme voisivat "suunnitella" kehotuksia:

- **Hallinnoijat** saattavat pyytää tekoälyä _analysoimaan opetussuunnitelman tietoja ja tunnistamaan puutteita sisällössä_. Tekoäly voi tiivistää tulokset tai visualisoida ne koodin avulla.  
- **Opettajat** saattavat pyytää tekoälyä _luomaan oppituntisuunnitelman kohderyhmälle ja aiheelle_. Tekoäly voi rakentaa henkilökohtaisen suunnitelman määritetyssä muodossa.  
- **Opiskelijat** saattavat pyytää tekoälyä _opettamaan heitä vaikeassa aiheessa_. Tekoäly voi ohjata opiskelijoita oppitunneilla, vihjeillä ja esimerkeillä, jotka on räätälöity heidän tasolleen.  

Tämä on vasta jäävuoren huippu. Tutustu [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - avoimen lähdekoodin kehotekirjastoon, jonka ovat kuratoineet koulutuksen asiantuntijat - saadaksesi laajemman käsityksen mahdollisuuksista! _Kokeile joitakin näistä kehotteista hiekkalaatikossa tai OpenAI Playgroundissa ja katso, mitä tapahtuu!_

<!--
OPPITUNTIPOHJA:
Tämän yksikön tulisi kattaa ydinkäsite #1.
Vahvista käsitettä esimerkeillä ja viittauksilla.

KÄSITE #1:
Promptien suunnittelu.
Määrittele se ja selitä, miksi sitä tarvitaan.
-->

## Mitä on promptien suunnittelu?

Aloitimme tämän oppitunnin määrittelemällä **promptien suunnittelun** prosessiksi, jossa _suunnitellaan ja optimoidaan_ tekstisyötteitä (kehotuksia) tuottamaan johdonmukaisia ja laadukkaita vastauksia (täydennyksiä) tiettyä sovellustavoitetta ja mallia varten. Voimme ajatella tätä kaksivaiheisena prosessina:

- _suunnitellaan_ alkuperäinen kehotus tietylle mallille ja tavoitteelle  
- _hienosäädetään_ kehotusta iteratiivisesti vastausten laadun parantamiseksi  

Tämä on väistämättä kokeiluun ja erehdykseen perustuva prosessi, joka vaatii käyttäjän intuitiota ja vaivannäköä optimaalisten tulosten saavuttamiseksi. Miksi se sitten on tärkeää? Vastaus tähän kysymykseen edellyttää kolmen käsitteen ymmärtämistä:

- _Tokenisaatio_ = miten malli "näkee" kehotteen  
- _Perus-LLM:t_ = miten perustamalli "käsittelee" kehotteen  
- _Ohjeviritetyt LLM:t_ = miten malli voi nyt nähdä "tehtävät"  

### Tokenisaatio

LLM näkee kehotteet _tokenien sarjana_, jossa eri mallit (tai mallin versiot) voivat tokenisoida saman kehotteen eri tavoin. Koska LLM:t on koulutettu tokeneilla (eikä raakatiedolla), tapa, jolla kehotteet tokenisoidaan, vaikuttaa suoraan tuotetun vastauksen laatuun.

Saadaksesi käsityksen siitä, miten tokenisaatio toimii, kokeile työkaluja kuten [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), joka on esitetty alla. Kopioi kehotteesi - ja katso, miten se muunnetaan tokeneiksi, kiinnittäen huomiota siihen, miten välilyönnit ja välimerkit käsitellään. Huomaa, että tämä esimerkki näyttää vanhemman LLM:n (GPT-3) - joten kokeilu uudemmalla mallilla voi tuottaa erilaisen tuloksen.

![Tokenisaatio](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.fi.png)

### Käsite: Perustamallit

Kun kehotus on tokenisoitu, ["Perus-LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (tai perustamalli) ennustaa seuraavan tokenin kyseisessä sarjassa. Koska LLM:t on koulutettu valtavilla tekstiaineistoilla, niillä on hyvä käsitys tokenien välisistä tilastollisista suhteista ja ne voivat tehdä ennusteen melko luotettavasti. Huomaa, että ne eivät ymmärrä sanojen _merkitystä_ kehotteessa tai tokenissa; ne vain näkevät kuvion, jonka ne voivat "täydentää" seuraavalla ennusteellaan. Ne voivat jatkaa sarjan ennustamista, kunnes käyttäjä keskeyttää prosessin tai jokin ennalta määritetty ehto täyttyy.

Haluatko nähdä, miten kehotuspohjainen täydennys toimii? Syötä yllä oleva kehotus Azure OpenAI Studion [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) -työkaluun oletusasetuksilla. Järjestelmä on konfiguroitu käsittelemään kehotteet tiedonpyyntöinä - joten sinun pitäisi nähdä täydennys, joka vastaa tätä kontekstia.

Mutta entä jos käyttäjä halusi nähdä jotain erityistä, joka täyttää tietyt kriteerit tai tehtävätavoitteen? Tässä kohtaa _ohjeviritetyt_ LLM:t astuvat kuvaan.

![Perus-LLM Chat-täydennys](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.fi.png)

### Käsite: Ohjeviritetyt LLM:t

[Ohjeviritetty LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) alkaa perustamallista ja hienosäätää sitä esimerkeillä tai syöte/vastauspareilla (esim. monivaiheiset "viestit"), jotka voivat sisältää selkeitä ohjeita - ja tekoälyn vastaus pyrkii noudattamaan näitä ohjeita.

Tämä käyttää tekniikoita, kuten ihmisen palautteeseen perustuvaa vahvistusoppimista (RLHF), joka voi kouluttaa mallia _noudattamaan ohjeita_ ja _oppimaan palautteesta_, jotta se tuottaa vastauksia, jotka sopivat paremmin käytännön sovelluksiin ja ovat käyttäjän tavoitteiden kannalta merkityksellisempiä.

Kokeillaan - palataan yllä olevaan kehotteeseen, mutta muutetaan nyt _järjestelmäviestiä_ antamaan seuraava ohje kontekstina:

> _Tiivistä sinulle annettu sisältö toisen luokan oppilaalle. Pidä tulos yhdessä kappaleessa, jossa on 3-5 kohtaa._

Huomaatko, kuinka tulos on nyt viritetty vastaamaan haluttua tavoitetta ja muotoa? Opettaja voi nyt käyttää tätä vastausta suoraan luokkansa dioissa.

![Ohjeviritetty LLM Chat-täydennys](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.fi.png)

## Miksi tarvitsemme promptien suunnittelua?

Nyt kun tiedämme, miten LLM:t käsittelevät kehotteita, puhutaan siitä, _miksi_ tarvitsemme promptien suunnittelua. Vastaus löytyy siitä, että nykyiset LLM:t tuottavat useita haasteita, jotka tekevät _luotettavien ja johdonmukaisten täydennysten_ saavuttamisesta haastavampaa ilman kehotteen rakentamiseen ja optimointiin panostamista. Esimerkiksi:

1. **Mallin vastaukset ovat satunnaisia.** _Sama kehotus_ tuottaa todennäköisesti erilaisia vastauksia eri malleilla tai malliversioilla. Ja se voi jopa tuottaa erilaisia tuloksia _samalla mallilla_ eri aikoina. _Promptien suunnittelutekniikat voivat auttaa meitä minimoimaan nämä vaihtelut tarjoamalla parempia ohjauskehyksiä_.  

1. **Mallit voivat keksiä vastauksia.** Mallit on esikoulutettu _laajoilla mutta rajallisilla_ aineistoilla, mikä tarkoittaa, että niiltä puuttuu tietoa koulutuksen ulkopuolisista käsitteistä. Tämän seurauksena ne voivat tuottaa täydennyksiä, jotka ovat epätarkkoja, kuvitteellisia tai suoraan ristiriidassa tunnettujen faktojen kanssa. _Promptien suunnittelutekniikat auttavat käyttäjiä tunnistamaan ja lieventämään tällaisia keksintöjä, esimerkiksi pyytämällä tekoälyä antamaan lähteitä tai perusteluja_.  

1. **Mallien kyvyt vaihtelevat.** Uudemmilla malleilla tai mallisukupolvilla on rikkaammat kyvyt, mutta ne tuovat mukanaan myös ainutlaatuisia omituisuuksia ja kompromisseja kustannusten ja monimutkaisuuden suhteen. _Promptien suunnittelu voi auttaa meitä kehittämään parhaita käytäntöjä ja työnkulkuja, jotka abstrahoivat erot ja mukautuvat mallikohtaisiin vaatimuksiin skaalautuvalla ja saumattomalla tavalla_.  

Katsotaanpa tätä käytännössä OpenAI:n tai Azure OpenAI Playgroundissa:

- Käytä samaa kehotusta eri LLM-toteutuksilla (esim. OpenAI, Azure OpenAI, Hugging Face) - huomasitko vaihtelut?  
- Käytä samaa kehotusta toistuvasti _samalla_ LLM-toteutuksella (esim. Azure OpenAI Playground) - miten nämä vaihtelut erosivat toisistaan?  

### Keksintöjen esimerkki

Tässä kurssissa käytämme termiä **"keksintö"** viittaamaan ilmiöön, jossa LLM:t joskus tuottavat tosiasiallisesti virheellistä tietoa koulutuksen rajoitusten tai muiden tekijöiden vuoksi. Saatat myös olla kuullut tästä puhuttavan _"hallusinaationa"_ suosituissa artikkeleissa tai tutkimuspapereissa. Suosittelemme kuitenkin vahvasti käyttämään termiä _"keksintö"_, jotta emme vahingossa inhimillistäisi käyttäytymistä antamalla ihmismäisiä piirteitä koneohjatulle lopputulokselle. Tämä myös vahvistaa [Vastuullisen tekoälyn ohjeita](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminologian näkökulmasta, poistamalla termejä, jotka voivat olla loukkaavia
Verkkohaku osoitti, että Marsin sodista on olemassa fiktiivisiä kertomuksia (esim. televisiosarjoja tai kirjoja) - mutta ei vuodelta 2076. Järki sanoo myös, että vuosi 2076 on _tulevaisuudessa_ eikä siksi voi liittyä todelliseen tapahtumaan.

Mitä tapahtuu, kun käytämme tätä kehotetta eri LLM-palveluntarjoajien kanssa?

> **Vastaus 1**: OpenAI Playground (GPT-35)

![Vastaus 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.fi.png)

> **Vastaus 2**: Azure OpenAI Playground (GPT-35)

![Vastaus 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.fi.png)

> **Vastaus 3**: Hugging Face Chat Playground (LLama-2)

![Vastaus 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.fi.png)

Kuten odotettua, jokainen malli (tai malliversio) tuottaa hieman erilaisia vastauksia johtuen stokastisesta käyttäytymisestä ja mallien kyvykkyyksien eroista. Esimerkiksi yksi malli kohdistuu kahdeksannen luokan yleisölle, kun taas toinen olettaa lukion opiskelijan. Mutta kaikki kolme mallia tuottivat vastauksia, jotka voisivat vakuuttaa tietämättömän käyttäjän siitä, että tapahtuma oli todellinen.

Kehotetekniikat, kuten _metakehotus_ ja _lämpötilan säätö_, voivat vähentää mallien virheellisiä vastauksia jossain määrin. Uudet kehotetekniikoiden _arkkitehtuurit_ myös integroivat uusia työkaluja ja tekniikoita saumattomasti kehotteen kulkuun, lieventääkseen tai vähentääkseen näitä vaikutuksia.

## Tapaustutkimus: GitHub Copilot

Päätetään tämä osio tutustumalla siihen, miten kehotetekniikoita käytetään tosielämän ratkaisuissa tarkastelemalla yhtä tapaustutkimusta: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot on "AI-pariohjelmoijasi" - se muuntaa tekstikehotteet koodiehdotuksiksi ja on integroitu kehitysympäristöösi (esim. Visual Studio Code) saumattoman käyttäjäkokemuksen takaamiseksi. Kuten alla olevissa blogisarjoissa dokumentoidaan, varhaisin versio perustui OpenAI Codex -malliin - ja insinöörit huomasivat nopeasti tarpeen hienosäätää mallia ja kehittää parempia kehotetekniikoita koodin laadun parantamiseksi. Heinäkuussa he [julkaisivat parannetun AI-mallin, joka menee Codexin ohi](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) tarjoten entistä nopeampia ehdotuksia.

Lue julkaisut järjestyksessä, jotta voit seurata heidän oppimismatkaansa.

- **Toukokuu 2023** | [GitHub Copilot ymmärtää koodiasi entistä paremmin](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Toukokuu 2023** | [GitHubin sisällä: Työskentely LLM-mallien kanssa GitHub Copilotin taustalla](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Kesäkuu 2023** | [Kuinka kirjoittaa parempia kehotteita GitHub Copilotille](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Heinäkuu 2023** | [.. GitHub Copilot menee Codexin ohi parannetulla AI-mallilla](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Heinäkuu 2023** | [Kehittäjän opas kehotetekniikoihin ja LLM-malleihin](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Syyskuu 2023** | [Kuinka rakentaa yrityksen LLM-sovellus: Oppeja GitHub Copilotista](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Voit myös selata heidän [Engineering-blogiaan](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) löytääksesi lisää julkaisuja, kuten [tämän](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), joka näyttää, miten näitä malleja ja tekniikoita _sovelletaan_ tosielämän sovellusten kehittämiseen.

---

<!--
OPETUSMALLI:
Tämän yksikön tulisi kattaa ydinkonsepti #2.
Vahvista konsepti esimerkeillä ja viittauksilla.

KONSEPTI #2:
Kehotteen suunnittelu.
Havainnollistettu esimerkeillä.
-->

## Kehotteen rakentaminen

Olemme nähneet, miksi kehotetekniikat ovat tärkeitä - nyt ymmärretään, miten kehotteet _rakennetaan_, jotta voimme arvioida erilaisia tekniikoita tehokkaamman kehotteen suunnitteluun.

### Peruskehotus

Aloitetaan peruskehotteesta: tekstisyöte, joka lähetetään mallille ilman muuta kontekstia. Tässä esimerkki - kun lähetämme Yhdysvaltain kansallislaulun ensimmäiset sanat OpenAI:n [Completion API:lle](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), se täydentää vastauksen välittömästi seuraavilla riveillä, havainnollistaen perusennustuskäyttäytymistä.

| Kehotus (Syöte)   | Täydennys (Vastaus)                                                                                                                        |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Kuulostaa siltä, että aloitat "The Star-Spangled Bannerin", Yhdysvaltain kansallislaulun, sanat. Täydelliset sanat ovat ...               |

### Monimutkainen kehotus

Lisätään nyt konteksti ja ohjeet peruskehotteeseen. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) antaa meidän rakentaa monimutkaisen kehotteen _viestien_ kokoelmana, jossa:

- Syöte/vastausparit heijastavat _käyttäjän_ syötettä ja _avustajan_ vastausta.
- Järjestelmäviesti asettaa kontekstin avustajan käyttäytymiselle tai persoonallisuudelle.

Pyyntö on nyt alla olevassa muodossa, jossa _tokenisointi_ tehokkaasti tallentaa olennaiset tiedot kontekstista ja keskustelusta. Nyt järjestelmän kontekstin muuttaminen voi vaikuttaa yhtä paljon täydennysten laatuun kuin annetut käyttäjän syötteet.

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

Yllä olevissa esimerkeissä käyttäjän kehotus oli yksinkertainen tekstikysely, joka voidaan tulkita tiedonpyynnöksi. _Ohjekehotuksilla_ voimme käyttää kyseistä tekstiä tehtävän tarkempaan määrittelyyn ja tarjota parempaa ohjausta tekoälylle. Tässä esimerkki:

| Kehotus (Syöte)                                                                                                                                                                                                                         | Täydennys (Vastaus)                                                                                                        | Ohjeen tyyppi      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :----------------- |
| Kirjoita kuvaus sisällissodasta                                                                                                                                                                                                        | _palautti yksinkertaisen kappaleen_                                                                                       | Yksinkertainen     |
| Kirjoita kuvaus sisällissodasta. Anna keskeiset päivämäärät ja tapahtumat ja kuvaile niiden merkitys                                                                                                                                   | _palautti kappaleen, jota seurasi luettelo keskeisistä tapahtumapäivämääristä ja kuvauksista_                              | Monimutkainen      |
| Kirjoita kuvaus sisällissodasta yhdessä kappaleessa. Anna 3 luettelopistettä keskeisistä päivämääristä ja niiden merkityksestä. Anna 3 muuta luettelopistettä keskeisistä historiallisista henkilöistä ja heidän panoksistaan. Palauta vastaus JSON-tiedostona | _palautti laajemmat tiedot tekstilaatikossa, muotoiltuna JSON-muotoon, jonka voi kopioida ja liittää tiedostoon ja validoida_ | Monimutkainen. Muotoiltu. |

## Ensisijainen sisältö

Yllä olevissa esimerkeissä kehotus oli edelleen melko avoin, jolloin LLM päätti, mikä osa sen esikoulutetusta tietokannasta oli relevantti. _Ensisijaisen sisällön_ suunnittelumallilla syöte jaetaan kahteen osaan:

- ohje (toiminta)
- olennainen sisältö (joka vaikuttaa toimintaan)

Tässä esimerkki, jossa ohjeena on "tiivistä tämä kahteen lauseeseen".

| Kehotus (Syöte)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Täydennys (Vastaus)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter on viides planeetta Auringosta ja suurin planeetta aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden aurinkokunnan planeettojen yhteenlaskettu massa. Jupiter on yksi kirkkaimmista paljaalla silmällä näkyvistä kohteista yötaivaalla, ja se on ollut tunnettu muinaisista sivilisaatioista lähtien ennen kirjoitettua historiaa. Se on nimetty roomalaisen jumalan Jupiterin mukaan. Kun Jupiteria katsotaan Maasta, se voi olla niin kirkas, että sen heijastunut valo voi heittää näkyviä varjoja, ja se on keskimäärin kolmanneksi kirkkain luonnollinen kohde yötaivaalla Kuun ja Venuksen jälkeen. <br/> **Tiivistä tämä kahteen lyhyeen lauseeseen** | Jupiter, viides planeetta Auringosta, on aurinkokunnan suurin ja tunnetaan yhtenä kirkkaimmista kohteista yötaivaalla. Roomalaisen jumalan Jupiterin mukaan nimetty kaasujättiläinen on massaltaan kaksi ja puoli kertaa kaikkien muiden planeettojen yhteenlaskettu massa. |

Ensisijaisen sisällön segmenttiä voidaan käyttää monin tavoin tehokkaampien ohjeiden luomiseen:

- **Esimerkit** - sen sijaan, että kerrot mallille, mitä tehdä eksplisiittisellä ohjeella, anna sille esimerkkejä siitä, mitä tehdä, ja anna sen päätellä kaava.
- **Vihjeet** - seuraa ohjetta "vihjeellä", joka ohjaa täydennystä, ohjaten mallia kohti relevantimpia vastauksia.
- **Mallipohjat** - nämä ovat toistettavia "reseptikehotteita", joissa on paikkamerkkejä (muuttujia), joita voidaan mukauttaa tiettyihin käyttötapauksiin.

Tutkitaan näitä käytännössä.

### Esimerkkien käyttö

Tämä on lähestymistapa, jossa käytät ensisijaista sisältöä "syöttämään mallille" joitakin esimerkkejä halutusta tuotoksesta tietylle ohjeelle ja annat sen päätellä halutun tuotoksen kaavan. Annettujen esimerkkien määrän perusteella voimme puhua nolla-, yksi- tai muutaman esimerkin kehotuksesta.

Kehotus koostuu nyt kolmesta osasta:

- Tehtävän kuvaus
- Muutamia esimerkkejä halutusta tuotoksesta
- Uuden esimerkin alku (joka toimii implisiittisenä tehtävän kuvauksena)

| Oppimistyyppi | Kehotus (Syöte)                                                                                                                                        | Täydennys (Vastaus)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Nolla-esimerkki | "Aurinko paistaa". Käännä espanjaksi                                                                                                                | "El Sol está brillando".    |
| Yksi-esimerkki | "Aurinko paistaa" => ""El Sol está brillando". <br> "On kylmä ja tuulinen päivä" =>                                                                  | "Es un día frío y ventoso". |
| Muutaman esimerkin | Pelaaja juoksi pesät => Baseball <br/> Pelaaja löi ässän => Tennis <br/> Pelaaja löi kuutosen => Cricket <br/> Pelaaja teki donkin =>            | Koripallo                   |
|               |                                                                                                                                                       |                             |

Huomaa, kuinka meidän piti antaa eksplisiittinen ohje ("Käännä espanjaksi") nolla-esimerkin kehotuksessa, mutta se päätellään yksi-esimerkin kehotuksessa. Muutaman esimerkin kehotus näyttää, kuinka lisäämällä enemmän esimerkkejä mallit voivat tehdä tarkempia päätelmiä ilman lisäohjeita.

### Kehotteen vihjeet

Toinen tekniikka ensisijaisen sisällön käyttämiseen on antaa _vihjeitä_ eikä esimerkkejä. Tässä tapauksessa annamme mallille "sysäyksen" oikeaan suuntaan _aloittamalla_ sen halutun vastausmuodon heijastavalla katkelmalla. Malli sitten "ottaa vihjeen" ja jatkaa samalla tavalla.

| Vihjeiden määrä | Kehotus (Syöte)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Täydennys (Vastaus)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter on viides planeetta Auringosta ja suurin planeetta aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden aurinkokunnan planeettojen yhteenlaskettu massa. Jupiter on yksi kirkkaimmista paljaalla silmällä näkyvistä kohteista yötaivaalla, ja se on ollut tunnettu muinaisista sivilisaatioista ennen kirjoitettua historiaa. <br/>**Tiivistä Tämä**                                       | Jupiter on aurinkokunnan suurin planeetta ja viides Auringosta. Se on kaasujättiläinen, jonka massa on 1/1000 Auringon massasta, mutta se on painavampi kuin kaikki muut planeetat yhteensä. Muinaiset sivilisaatiot ovat tunteneet Jupiterin pitkään, ja se näkyy helposti yötaivaalla. |
| 1              | Jupiter on viides planeetta Auringosta ja suurin planeetta aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden aurinkokunnan planeettojen yhteenlaskettu massa. Jupiter on yksi kirkkaimmista paljain silmin näkyvistä kohteista yötaivaalla, ja se on ollut tunnettu muinaisista sivilisaatioista lähtien, jo ennen kirjoitettua historiaa. <br/>**Tiivistä tämä** <br/> Opimme, että Jupiter | on viides planeetta Auringosta ja suurin aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden planeettojen yhteenlaskettu massa. Se on helposti paljain silmin nähtävissä ja tunnettu jo muinaisista ajoista lähtien.                        |
| 2              | Jupiter on viides planeetta Auringosta ja suurin planeetta aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden aurinkokunnan planeettojen yhteenlaskettu massa. Jupiter on yksi kirkkaimmista paljain silmin näkyvistä kohteista yötaivaalla, ja se on ollut tunnettu muinaisista sivilisaatioista lähtien, jo ennen kirjoitettua historiaa. <br/>**Tiivistä tämä** <br/> 3 tärkeintä oppimaamme asiaa:         | 1. Jupiter on viides planeetta Auringosta ja suurin aurinkokunnassa. <br/> 2. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta...<br/> 3. Jupiter on ollut paljain silmin nähtävissä jo muinaisista ajoista lähtien ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Kehotemallit

Kehotemalli on _ennalta määritelty kehotteen resepti_, joka voidaan tallentaa ja käyttää uudelleen tarpeen mukaan, jotta käyttäjäkokemukset olisivat johdonmukaisempia laajassa mittakaavassa. Yksinkertaisimmillaan se on vain kokoelma kehotteiden esimerkkejä, kuten [tämä OpenAI:n esimerkki](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), joka sisältää sekä interaktiiviset kehotekomponentit (käyttäjän ja järjestelmän viestit) että API-pohjaisen pyyntömuodon - tukemaan uudelleenkäyttöä.

Monimutkaisemmassa muodossaan, kuten [tämä LangChain-esimerkki](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), se sisältää _paikkamerkkejä_, jotka voidaan korvata tiedoilla eri lähteistä (käyttäjän syöte, järjestelmän konteksti, ulkoiset tietolähteet jne.) kehotteen dynaamiseksi luomiseksi. Tämä mahdollistaa uudelleenkäytettävien kehotteiden kirjaston luomisen, joita voidaan käyttää johdonmukaisten käyttäjäkokemusten **ohjelmalliseen** tuottamiseen laajassa mittakaavassa.

Lopulta mallien todellinen arvo piilee mahdollisuudessa luoda ja julkaista _kehotekirjastoja_ tiettyihin sovellusalueisiin - jolloin kehotemalli on nyt _optimoitu_ heijastamaan sovelluskohtaista kontekstia tai esimerkkejä, jotka tekevät vastauksista kohdeyleisölle merkityksellisempiä ja tarkempia. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) -tietovarasto on hyvä esimerkki tästä lähestymistavasta, sillä se kokoaa kirjaston kehotteita koulutuksen alalle painottaen keskeisiä tavoitteita, kuten oppituntien suunnittelua, opetussuunnitelman laatimista, opiskelijoiden ohjausta jne.

## Tukisisältö

Jos ajattelemme kehotteen rakentamista tehtävänannon (tehtävä) ja kohteen (ensisijainen sisältö) yhdistelmänä, niin _toissijainen sisältö_ on kuin lisäkonteksti, jonka tarjoamme **vaikuttaaksemme tulokseen jollain tavalla**. Se voi olla hienosäätöparametreja, muotoiluohjeita, aiheiden luokitteluja jne., jotka voivat auttaa mallia _räätälöimään_ vastauksensa vastaamaan haluttuja käyttäjätavoitteita tai -odotuksia.

Esimerkiksi: Kun käytettävissä on kurssikatalogi, joka sisältää laajasti metatietoja (nimi, kuvaus, taso, metatunnisteet, opettaja jne.) kaikista opetussuunnitelman kursseista:

- voimme määritellä tehtävänannon "tiivistä syksyn 2023 kurssikatalogi"
- voimme käyttää ensisijaista sisältöä tarjoamaan muutamia esimerkkejä halutusta lopputuloksesta
- voimme käyttää toissijaista sisältöä tunnistamaan viisi tärkeintä kiinnostavaa "tunnistetta".

Nyt malli voi tarjota tiivistelmän esimerkkien osoittamassa muodossa - mutta jos tuloksessa on useita tunnisteita, se voi priorisoida toissijaisessa sisällössä tunnistetut viisi tärkeintä tunnistetta.

---

<!--
OPPITUNTIMALLI:
Tämä osio kattaa ydinkonseptin #1.
Vahvista konsepti esimerkeillä ja viitteillä.

KONSEPTI #3:
Kehotetekniikat.
Mitkä ovat perusmenetelmät kehotetekniikoille?
Havainnollista harjoituksilla.
-->

## Kehottamisen parhaat käytännöt

Nyt kun tiedämme, miten kehotteita voidaan _rakentaa_, voimme alkaa miettiä, miten ne voidaan _suunnitella_ parhaita käytäntöjä noudattaen. Voimme ajatella tätä kahdessa osassa - oikean _ajattelutavan_ omaksumisessa ja oikeiden _tekniikoiden_ soveltamisessa.

### Kehotetekniikoiden ajattelutapa

Kehotetekniikat perustuvat kokeiluun ja erehdykseen, joten pidä mielessä kolme laajaa ohjenuoraa:

1. **Toimialan ymmärrys on tärkeää.** Vastausten tarkkuus ja merkityksellisyys riippuvat siitä _toimialasta_, jolla sovellus tai käyttäjä toimii. Käytä intuitiotasi ja toimialan asiantuntemustasi **mukauttaaksesi tekniikoita** edelleen. Määrittele esimerkiksi _toimialakohtaisia persoonallisuuksia_ järjestelmäkehotteissasi tai käytä _toimialakohtaisia malleja_ käyttäjäkehotteissasi. Tarjoa toissijaista sisältöä, joka heijastaa toimialakohtaisia konteksteja, tai käytä _toimialakohtaisia vihjeitä ja esimerkkejä_ ohjataksesi mallia kohti tuttuja käyttötapoja.

2. **Mallin ymmärrys on tärkeää.** Tiedämme, että mallit ovat luonteeltaan stokastisia. Mutta mallien toteutukset voivat myös vaihdella käyttämänsä koulutusdatan (ennalta koulutettu tieto), tarjoamiensa ominaisuuksien (esim. API:n tai SDK:n kautta) ja sen sisällön tyypin mukaan, johon ne on optimoitu (esim. koodi vs. kuvat vs. teksti). Ymmärrä käyttämäsi mallin vahvuudet ja rajoitukset, ja käytä tätä tietoa _priorisoidaksesi tehtäviä_ tai rakentaaksesi _räätälöityjä malleja_, jotka on optimoitu mallin kykyjen mukaan.

3. **Iterointi ja validointi ovat tärkeitä.** Mallit kehittyvät nopeasti, samoin kuin kehotetekniikat. Toimialan asiantuntijana sinulla voi olla muuta kontekstia tai kriteerejä, jotka koskevat _juuri sinun_ sovellustasi, mutta eivät välttämättä koske laajempaa yhteisöä. Käytä kehotetekniikoita ja -työkaluja "käynnistääksesi" kehotteen rakentamisen, sitten iteroi ja validoi tulokset oman intuitiosi ja toimialan asiantuntemuksesi avulla. Tallenna oivalluksesi ja luo **tietopohja** (esim. kehotekirjastoja), joita muut voivat käyttää uutena lähtökohtana nopeampaan iterointiin tulevaisuudessa.

## Parhaat käytännöt

Tarkastellaan nyt yleisiä parhaita käytäntöjä, joita suosittelevat [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ja [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) -käytännön asiantuntijat.

| Mitä                              | Miksi                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Arvioi uusimmat mallit.           | Uusilla mallisukupolvilla on todennäköisesti parannettuja ominaisuuksia ja laatua - mutta ne voivat myös aiheuttaa korkeampia kustannuksia. Arvioi niiden vaikutus ja tee sitten siirtymispäätökset.                                                |
| Erottele ohjeet ja konteksti      | Tarkista, määritteleekö mallisi/palveluntarjoajasi _erottimia_, jotka erottavat ohjeet, ensisijaisen ja toissijaisen sisällön selkeämmin. Tämä voi auttaa malleja määrittämään tarkemmin painoarvot tokeneille.                                       |
| Ole tarkka ja selkeä              | Anna enemmän yksityiskohtia halutusta kontekstista, lopputuloksesta, pituudesta, muodosta, tyylistä jne. Tämä parantaa sekä vastausten laatua että johdonmukaisuutta. Tallenna reseptit uudelleenkäytettäviin malleihin.                              |
| Ole kuvaileva, käytä esimerkkejä  | Mallit voivat reagoida paremmin "näytä ja kerro" -lähestymistapaan. Aloita `zero-shot`-lähestymistavalla, jossa annat sille ohjeen (mutta ei esimerkkejä), ja kokeile sitten `few-shot`-lähestymistapaa, jossa annat muutamia esimerkkejä halutusta lopputuloksesta. Käytä analogioita. |
| Käytä vihjeitä aloittaaksesi vastaukset | Ohjaa mallia kohti haluttua lopputulosta antamalla sille joitakin johtolauseita tai -sanoja, joita se voi käyttää vastauksen lähtökohtana.                                                                                                       |
| Toista tarvittaessa               | Joskus sinun täytyy toistaa itseäsi mallille. Anna ohjeet ennen ja jälkeen ensisijaisen sisällön, käytä ohjetta ja vihjettä jne. Iteroi ja validoi nähdäksesi, mikä toimii.                                                                          |
| Järjestyksellä on väliä           | Tiedon esittämisjärjestys mallille voi vaikuttaa tulokseen, jopa oppimisesimerkeissä, kiitos tuoreusvinouman. Kokeile eri vaihtoehtoja nähdäksesi, mikä toimii parhaiten.                                                                            |
| Anna mallille "pakotie"           | Anna mallille _varavaihtoehto_, jonka se voi tarjota, jos se ei pysty suorittamaan tehtävää jostain syystä. Tämä voi vähentää mallien mahdollisuutta tuottaa vääriä tai keksittyjä vastauksia.                                                       |
|                                   |                                                                                                                                                                                                                                                   |

Kuten minkä tahansa parhaan käytännön kohdalla, muista, että _kokemuksesi voi vaihdella_ mallin, tehtävän ja toimialan mukaan. Käytä näitä lähtökohtana ja iteroi löytääksesi, mikä toimii parhaiten sinulle. Arvioi jatkuvasti kehotetekniikoiden prosessiasi, kun uusia malleja ja työkaluja tulee saataville, keskittyen prosessin skaalautuvuuteen ja vastausten laatuun.

<!--
OPPITUNTIMALLI:
Tämä osio sisältää koodiharjoituksen, jos sovellettavissa.

HARJOITUS:
Linkki Jupyter Notebookiin, jossa vain koodikommentit ovat ohjeina (koodiosiot ovat tyhjiä).

RATKAISU:
Linkki kopioon kyseisestä Notebookista, jossa kehotteet on täytetty ja suoritettu, esimerkkinä yhdestä mahdollisesta ratkaisusta.
-->

## Tehtävä

Onnittelut! Olet päässyt oppitunnin loppuun! Nyt on aika testata joitakin näistä konsepteista ja tekniikoista todellisten esimerkkien avulla!

Tehtävää varten käytämme Jupyter Notebookia, jossa voit suorittaa harjoituksia interaktiivisesti. Voit myös laajentaa Notebookia omilla Markdown- ja koodisoluillasi tutkiaksesi ideoita ja tekniikoita itsenäisesti.

### Aloittaaksesi, forkkaa repo ja

- (Suositeltu) Käynnistä GitHub Codespaces
- (Vaihtoehtoisesti) Kloonaa repo paikalliselle laitteellesi ja käytä sitä Docker Desktopin kanssa
- (Vaihtoehtoisesti) Avaa Notebook suosimassasi Notebook-ympäristössä.

### Seuraavaksi, määritä ympäristömuuttujasi

- Kopioi `.env.copy` -tiedosto reposta `.env`-tiedostoksi ja täytä `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ja `AZURE_OPENAI_DEPLOYMENT` arvot. Palaa [Learning Sandbox -osioon](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) oppiaksesi lisää.

### Seuraavaksi, avaa Jupyter Notebook

- Valitse ajonaikainen ydin. Jos käytät vaihtoehtoja 1 tai 2, valitse yksinkertaisesti oletuksena oleva Python 3.10.x -ydin, jonka kehityskontti tarjoaa.

Olet valmis suorittamaan harjoitukset. Huomaa, että tässä ei ole _oikeita tai vääriä_ vastauksia - vain vaihtoehtojen tutkimista kokeilemalla ja erehtymällä sekä intuition rakentamista siitä, mikä toimii tietylle mallille ja sovellusalueelle.

_Tästä syystä tässä oppitunnissa ei ole koodiratkaisusegmenttejä. Sen sijaan Notebook sisältää Markdown-soluja otsikolla "Oma ratkaisu:", joka näyttää yhden esimerkkituloksen viitteeksi._

 <!--
OPPITUNTIMALLI:
Päätä osio yhteenvedolla ja itseopiskeluresursseilla.
-->

## Tietojen tarkistus

Mikä seuraavista on hyvä kehotus, joka noudattaa kohtuullisia parhaita käytäntöjä?

1. Näytä minulle kuva punaisesta autosta  
2. Näytä minulle kuva punaisesta Volvo-merkkisestä XC90-mallin autosta, joka on pysäköity kallion viereen auringonlaskun aikaan  
3. Näytä minulle kuva punaisesta Volvo-merkkisestä XC90-mallin autosta  

V: 2, se on paras kehotus, koska se antaa yksityiskohtia "mitä" ja menee tarkempiin yksityiskohtiin (ei vain mikä tahansa auto, vaan tietty merkki ja malli), ja se myös kuvailee yleistä ympäristöä. 3 on seuraavaksi paras, koska se sisältää myös paljon kuvausta.

## 🚀 Haaste

Kokeile hyödyntää "vihje"-tekniikkaa kehotteella: Täydennä lause "Näytä minulle kuva punaisesta Volvo-merkkisestä ". Mitä se vastaa, ja miten voisit parantaa sitä?

## Hienoa työtä! Jatka oppimista

Haluatko oppia lisää erilaisista kehotetekniikoista? Siirry [jatko-opiskelusivulle](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) löytääksesi muita loistavia resursseja tästä aiheesta.

Siirry oppituntiin 5, jossa tarkastelemme [edistyneitä kehotetekniikoita](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.