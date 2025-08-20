<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-07-09T10:30:16+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "fi"
}
-->
# Promptin suunnittelun perusteet

[![Promptin suunnittelun perusteet](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.fi.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Johdanto  
Tässä moduulissa käsitellään keskeisiä käsitteitä ja tekniikoita tehokkaiden promptien luomiseksi generatiivisissa tekoälymalleissa. Tapa, jolla kirjoitat promptin LLM:lle, on myös tärkeä. Huolellisesti laadittu prompti voi tuottaa parempilaatuisen vastauksen. Mutta mitä tarkalleen tarkoittavat termit _prompt_ ja _promptin suunnittelu_? Entä miten parannan promptin _syötettä_, jonka lähetän LLM:lle? Näihin kysymyksiin pyrimme vastaamaan tässä ja seuraavassa luvussa.

_Generatiivinen tekoäly_ pystyy luomaan uutta sisältöä (esim. tekstiä, kuvia, ääntä, koodia jne.) käyttäjän pyyntöjen perusteella. Se toteuttaa tämän käyttämällä _suuria kielimalleja_ kuten OpenAI:n GPT ("Generative Pre-trained Transformer") -sarjaa, jotka on koulutettu käyttämään luonnollista kieltä ja koodia.

Käyttäjät voivat nyt olla vuorovaikutuksessa näiden mallien kanssa tutuilla tavoilla, kuten chatin kautta, ilman teknistä osaamista tai koulutusta. Mallit ovat _prompt-pohjaisia_ – käyttäjät lähettävät tekstisyötteen (promptin) ja saavat takaisin tekoälyn vastauksen (completion). He voivat sitten "jutella tekoälyn kanssa" toistuvasti, monikierroksisissa keskusteluissa, hioen promptiaan, kunnes vastaus vastaa odotuksia.

"Promptit" ovat nyt generatiivisten tekoälysovellusten ensisijainen _ohjelmointirajapinta_, joka kertoo malleille, mitä tehdä, ja vaikuttaa palautettujen vastausten laatuun. "Promptin suunnittelu" on nopeasti kasvava tutkimusala, joka keskittyy promptien _suunnitteluun ja optimointiin_ tuottaakseen johdonmukaisia ja laadukkaita vastauksia laajassa mittakaavassa.

## Oppimistavoitteet

Tässä oppitunnissa opimme, mitä promptin suunnittelu on, miksi se on tärkeää ja miten voimme laatia tehokkaampia promptteja tietylle mallille ja sovellustavoitteelle. Ymmärrämme keskeiset käsitteet ja parhaat käytännöt promptin suunnittelussa – ja tutustumme interaktiiviseen Jupyter Notebook -"hiekkalaatikko"-ympäristöön, jossa näitä käsitteitä sovelletaan käytännön esimerkkeihin.

Oppitunnin lopussa osaat:

1. Selittää, mitä promptin suunnittelu on ja miksi se on tärkeää.
2. Kuvailla promptin osat ja niiden käyttötavat.
3. Oppia parhaat käytännöt ja tekniikat promptin suunnitteluun.
4. Soveltaa opittuja tekniikoita käytännön esimerkkeihin OpenAI-päätepisteen avulla.

## Keskeiset termit

Promptin suunnittelu: Tekstin syötteiden suunnittelu ja hienosäätö, jolla ohjataan tekoälymalleja tuottamaan haluttuja tuloksia.  
Tokenisointi: Prosessi, jossa teksti muunnetaan pienemmiksi yksiköiksi, tokeneiksi, joita malli voi ymmärtää ja käsitellä.  
Ohjeistuksella hienosäädetyt LLM:t: Suuret kielimallit, joita on hienosäädetty erityisillä ohjeilla parantamaan vastausten tarkkuutta ja merkityksellisyyttä.

## Oppimishiekkalaatikko

Promptin suunnittelu on tällä hetkellä enemmän taidetta kuin tiedettä. Paras tapa kehittää intuitiota on _harjoitella enemmän_ ja omaksua kokeileva lähestymistapa, joka yhdistää sovellusalueen asiantuntemuksen suositeltuihin tekniikoihin ja mallikohtaisiin optimointeihin.

Tämän oppitunnin mukana tuleva Jupyter Notebook tarjoaa _hiekkalaatikko_-ympäristön, jossa voit kokeilla oppimaasi – joko matkan varrella tai koodaushaasteen osana lopussa. Harjoitusten suorittamiseen tarvitset:

1. **Azure OpenAI API -avaimen** – palvelun päätepisteen käyttöön otetulle LLM:lle.  
2. **Python-ympäristön** – jossa Notebook voidaan suorittaa.  
3. **Paikalliset ympäristömuuttujat** – _suorita [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) -vaiheet nyt valmiiksi_.

Notebook sisältää _aloitus_ harjoituksia – mutta sinua kannustetaan lisäämään omia _Markdown_- (kuvaus) ja _Code_- (prompt-pyynnöt) osioita kokeillaksesi lisää esimerkkejä tai ideoita – ja kehittääksesi intuitiota promptin suunnitteluun.

## Kuvitettu opas

Haluatko saada kokonaiskuvan tästä oppitunnista ennen kuin sukellat syvemmälle? Tutustu tähän kuvitettuun oppaaseen, joka antaa yleiskuvan pääaiheista ja keskeisistä huomioista, joita voit pohtia kussakin osassa. Oppitunnin tiekartta vie sinut ydinkäsitteiden ja haasteiden ymmärtämisestä niiden ratkaisemiseen asiaankuuluvilla promptin suunnittelutekniikoilla ja parhailla käytännöillä. Huomaa, että tämän oppaan "Edistyneet tekniikat" -osio viittaa seuraavan luvun sisältöön tässä opetussuunnitelmassa.

![Kuvitettu opas promptin suunnitteluun](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.fi.png)

## Startup-yrityksemme

Keskustellaanpa nyt siitä, miten _tämä aihe_ liittyy startup-yrityksemme missioon [tuoda tekoälyinnovaatioita koulutukseen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Haluamme rakentaa tekoälypohjaisia sovelluksia _personoituun oppimiseen_ – joten pohditaan, miten eri käyttäjät voisivat "suunnitella" promptteja sovelluksessamme:

- **Ylläpitäjät** saattavat pyytää tekoälyä _analysoimaan opetussuunnitelman tietoja kattavuuden aukkojen löytämiseksi_. Tekoäly voi tiivistää tulokset tai visualisoida ne koodin avulla.  
- **Opettajat** voivat pyytää tekoälyä _luomaan oppituntisuunnitelman kohdeyleisölle ja aiheelle_. Tekoäly voi rakentaa personoidun suunnitelman määritellyssä muodossa.  
- **Oppilaat** voivat pyytää tekoälyä _ohjaamaan heitä vaikeassa aineessa_. Tekoäly voi nyt opastaa oppilaita oppitunneilla, vihjeillä ja esimerkeillä, jotka on räätälöity heidän tasolleen.

Tämä on vasta jäävuoren huippu. Tutustu [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) -avoin lähdekoodin prompt-kirjastoon, jonka ovat koonneet koulutusalan asiantuntijat – saadaksesi laajemman kuvan mahdollisuuksista! _Kokeile ajaa joitakin näistä promptteista hiekkalaatikossa tai OpenAI Playgroundissa nähdäksesi, mitä tapahtuu!_

<!--  
LESSON TEMPLATE:  
This unit should cover core concept #1.  
Reinforce the concept with examples and references.

CONCEPT #1:  
Prompt Engineering.  
Define it and explain why it is needed.  
-->

## Mitä on promptin suunnittelu?

Aloitimme tämän oppitunnin määrittelemällä **promptin suunnittelun** prosessiksi, jossa _suunnitellaan ja optimoidaan_ tekstisyötteitä (prompteja) tuottamaan johdonmukaisia ja laadukkaita vastauksia (completions) tiettyyn sovellustavoitteeseen ja malliin. Voimme ajatella tätä kahden vaiheen prosessina:

- _suunnitella_ alkuperäinen prompti tietylle mallille ja tavoitteelle  
- _hioa_ promptia iteratiivisesti parantaaksemme vastauksen laatua

Tämä on väistämättä kokeilu- ja erehdysprosessi, joka vaatii käyttäjän intuitiota ja vaivannäköä optimaalisten tulosten saavuttamiseksi. Miksi se sitten on tärkeää? Vastataksemme tähän kysymykseen meidän täytyy ensin ymmärtää kolme käsitettä:

- _Tokenisointi_ = miten malli "näkee" promptin  
- _Perus-LLM:t_ = miten perustamalli "käsittelee" promptin  
- _Ohjeistuksella hienosäädetyt LLM:t_ = miten malli nyt voi nähdä "tehtäviä"

### Tokenisointi

LLM näkee promptit _tokenien sarjana_, ja eri mallit (tai malliversiot) voivat tokenisoida saman promptin eri tavoin. Koska LLM:t on koulutettu tokeneilla (eivät raakatekstillä), promptin tokenisoinnilla on suora vaikutus tuotetun vastauksen laatuun.

Saadaksesi käsityksen tokenisoinnista, kokeile esimerkiksi [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) -työkalua alla. Kopioi promptisi siihen ja katso, miten se muunnetaan tokeneiksi, kiinnittäen huomiota välilyöntien ja välimerkkien käsittelyyn. Huomaa, että esimerkissä käytetään vanhempaa LLM:ää (GPT-3) – uudemmalla mallilla tulos voi olla erilainen.

![Tokenisointi](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.fi.png)

### Käsite: Perusmallit

Kun prompti on tokenisoitu, ["Perus-LLM:n"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (tai foundation-mallin) päätehtävä on ennustaa seuraava token tässä sarjassa. Koska LLM:t on koulutettu valtavilla tekstiaineistoilla, niillä on hyvä käsitys tokenien tilastollisista suhteista ja ne voivat tehdä ennustuksen varmuudella. Huomaa, että ne eivät ymmärrä promptin tai tokenin _merkitystä_; ne näkevät vain mallin, jonka voivat "täydentää" seuraavalla ennustuksellaan. Ne voivat jatkaa ennustamista, kunnes käyttäjä keskeyttää tai jokin ennalta määritelty ehto täyttyy.

Haluatko nähdä, miten prompt-pohjainen täydennys toimii? Syötä yllä oleva prompt Azure OpenAI Studion [_Chat Playgroundiin_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) oletusasetuksilla. Järjestelmä on konfiguroitu käsittelemään promptit tiedonpyyntöinä – joten näet vastauksen, joka täyttää tämän kontekstin.

Mutta entä jos käyttäjä haluaa nähdä jotain tiettyä, joka täyttää jonkin kriteerin tai tehtävän tavoitteen? Tässä kohtaa _ohjeistuksella hienosäädetyt_ LLM:t astuvat kuvaan.

![Perus-LLM:n chat-vastaus](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.fi.png)

### Käsite: Ohjeistuksella hienosäädetyt LLM:t

[Ohjeistuksella hienosäädetty LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) perustuu foundation-malliin, jota hienosäädetään esimerkkien tai syöte-/tulosparien (esim. monikierroksisten "viestien") avulla, jotka sisältävät selkeitä ohjeita – ja tekoälyn vastaus pyrkii noudattamaan näitä ohjeita.

Tässä käytetään tekniikoita kuten ihmispalautteella vahvistettu oppiminen (RLHF), joka kouluttaa mallin _noudattamaan ohjeita_ ja _oppimaan palautteesta_, jotta se tuottaa vastauksia, jotka soveltuvat paremmin käytännön sovelluksiin ja ovat merkityksellisempiä käyttäjän tavoitteille.

Kokeillaanpa – palaa yllä olevaan promptiin, mutta vaihda nyt _järjestelmäviesti_ antamaan seuraava ohje kontekstina:

> _Tiivistä annettu sisältö toisen luokan oppilaalle. Pidä tulos yhdessä kappaleessa, jossa on 3–5 lueteltua kohtaa._

Näetkö, miten tulos on nyt viritetty vastaamaan haluttua tavoitetta ja muotoa? Opettaja voi käyttää tätä vastausta suoraan luentokalvoillaan.

![Ohjeistuksella hienosäädetyn LLM:n chat-vastaus](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.fi.png)

## Miksi tarvitsemme promptin suunnittelua?

Nyt kun tiedämme, miten LLM:t käsittelevät promptit, keskustellaan siitä, _miksi_ promptin suunnittelu on tarpeen. Vastaus löytyy siitä, että nykyisillä LLM:illä on useita haasteita, jotka tekevät _luotettavien ja johdonmukaisten vastausten_ saavuttamisesta vaikeampaa ilman panostusta promptin rakentamiseen ja optimointiin. Esimerkiksi:

1. **Mallien vastaukset ovat stokastisia.** _Sama prompt_ tuottaa todennäköisesti erilaisia vastauksia eri malleilla tai malliversioilla. Se voi myös tuottaa eri tuloksia _samalla mallilla_ eri aikoina. _Promptin suunnittelutekniikat auttavat minimoimaan näitä vaihteluita tarjoamalla parempia suojakeinoja_.

1. **Mallien vastaukset voivat olla keksittyjä.** Mallit on esikoulutettu _laajoilla mutta rajallisilla_ aineistoilla, joten niiltä puuttuu tieto koulutusalueen ulkopuolisista käsitteistä. Tämän seurauksena ne voivat tuottaa vastauksia, jotka ovat epätarkkoja, kuvitteellisia tai suoraan ristiriidassa tunnettujen faktojen kanssa. _Promptin suunnittelutekniikat auttavat käyttäjiä tunnistamaan ja vähentämään tällaisia keksintöjä, esimerkiksi pyytämällä tekoälyltä lähdeviitteitä tai perusteluja_.

1. **Mallien kyvyt vaihtelevat.** Uudemmat mallit tai mallisukupolvet tarjoavat laajempia kykyjä, mutta niihin liittyy myös ainutlaatuisia erikoispiirteitä sekä kustannus- ja monimutkaisuustasapainoja. _Promptin suunnittelu auttaa kehittämään parhaita käytäntöjä ja työnkulkuja, jotka abstrahoivat erot ja mukautuvat mallikohtaisiin vaatimuksiin skaalautuvasti ja saumattomasti_.

Kokeile tätä käytännössä OpenAI:n tai Azure OpenAI:n Playgroundissa:

- Käytä samaa promptia eri LLM-julkaisuissa (esim. OpenAI, Azure OpenAI, Hugging Face) – huomasitko eroja?  
- Käytä samaa promptia toistuvasti _samassa_ LLM-julkaisussa (esim. Azure OpenAI playground) – miten nämä vaihtelut erosivat?

### Keksintöjen esimerkki

Tässä kurssissa käytämme termiä **"keksintö"** viittaamaan ilmiöön, jossa LLM:t joskus tuottavat tosiasiallisesti virheellistä tietoa rajoitustensa tai muiden tekijöiden vuoksi. Saatat olla kuullut tästä myös nimellä _"hallusinaatiot"_ suosituissa artikkeleissa tai tutkimuspapereissa. Suosittelemme kuitenkin käyttämään termiä _"keksintö"_, jotta emme vahingossa antropomorfisoisi käyttäytymistä antamalla koneen tuottamalle tulokselle ihmismäisiä piirteitä. Tämä tukee myös [Vastuullisen tekoälyn ohjeita](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminologian näkökulmasta, poistaen termejä, joita voidaan pitää loukkaavina tai ei-sisältävinä joissain yhteyksissä.

Haluatko saada käsityksen siitä, miten keksinnöt toimivat? Ajattele promptia, joka ohjeistaa tekoälyä luomaan sisältöä olemattomasta aiheesta (varmistaakseen, ettei sitä löydy koulutusdatasta). Esimerkiksi – kokeilin tätä promptia:
# Martian sota 2076 – oppituntisuunnitelma

## Tavoitteet
- Ymmärtää Martian sodan 2076 taustat ja syyt
- Tutkia sodan keskeiset tapahtumat ja osapuolet
- Analysoida sodan vaikutuksia Marsin asutukseen ja ihmiskunnan tulevaisuuteen

## Oppitunnin rakenne

### 1. Johdanto (15 min)
- Lyhyt katsaus Marsin asutuksen historiaan ennen vuotta 2076
- Miksi Martian sota syttyi? (poliittiset, taloudelliset ja sosiaaliset syyt)
- Keskustelu: Mitä oppilaat tietävät Marsista ja mahdollisista konflikteista siellä?

### 2. Martian sodan kulku (30 min)
- Keskeiset osapuolet ja heidän tavoitteensa
- Tärkeimmät taistelut ja strategiat
- Teknologian rooli sodassa (esim. @@INLINE_CODE_1@@, @@INLINE_CODE_2@@)
- Videoesitys tai kartta sodan etenemisestä

### 3. Sodan seuraukset (20 min)
- Vaikutukset Marsin asutukseen ja infrastruktuuriin
- Ihmiskunnan reaktiot Maassa ja Marsissa
- Pitkän aikavälin vaikutukset politiikkaan ja avaruustutkimukseen

### 4. Yhteenveto ja keskustelu (15 min)
- Oppilaiden mielipiteet sodan syistä ja seurauksista
- Mitä voimme oppia Martian sodasta tulevaisuuden konflikteja varten?
- Kysymyksiä ja vastauksia

## Kotitehtävä
Kirjoita lyhyt essee aiheesta: "Miten Martian sota 2076 muutti ihmiskunnan käsitystä avaruudesta ja sodankäynnistä?"

## Lisämateriaalit
- Linkkejä artikkeleihin ja dokumentteihin Martian sodasta
- Interaktiivinen aikajana @@INLINE_CODE_3@@
- Podcast-jakso sodan keskeisistä tapahtumista
Verkkohaku osoitti, että Marsin sodista on olemassa fiktiivisiä kertomuksia (esim. televisiosarjat tai kirjat) – mutta ei yhtään vuodelle 2076. Terve järki myös kertoo, että vuosi 2076 on _tulevaisuudessa_ eikä sitä siksi voi yhdistää todelliseen tapahtumaan.

Mitä siis tapahtuu, kun ajamme tämän kehotteen eri LLM-palveluntarjoajilla?

> **Vastaus 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.fi.png)

> **Vastaus 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.fi.png)

> **Vastaus 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.fi.png)

Kuten odottaa saattaa, kukin malli (tai malliversio) tuottaa hieman erilaisia vastauksia satunnaisuuden ja mallin kyvykkyyksien vaihtelun vuoksi. Esimerkiksi yksi malli kohdistaa vastauksensa 8. luokan oppilaille, kun taas toinen olettaa lukioikäisen käyttäjän. Kaikki kolme mallia kuitenkin tuottivat vastauksia, jotka voisivat saada tietämättömän käyttäjän uskomaan, että tapahtuma oli todellinen.

Kehoteinsinöörin tekniikat, kuten _metakehotteet_ ja _lämpötilan säätö_, voivat jonkin verran vähentää mallin keksintöjä. Uudet kehotteiden suunnittelun _arkkitehtuurit_ myös sulauttavat uusia työkaluja ja tekniikoita saumattomasti kehotteiden kulkuun, lieventäen tai vähentäen näitä ilmiöitä.

## Tapaustutkimus: GitHub Copilot

Päätetään tämä osio katsomalla, miten kehotteiden suunnittelua käytetään todellisissa ratkaisuissa, tarkastelemalla yhtä tapaustutkimusta: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot on "tekoälypariohjelmoijasi" – se muuntaa tekstikehotteet koodin täydennyksiksi ja on integroitu kehitysympäristöösi (esim. Visual Studio Code) sujuvan käyttökokemuksen takaamiseksi. Alla olevissa blogisarjoissa on dokumentoitu, että varhaisin versio perustui OpenAI Codex -malliin – ja insinöörit huomasivat nopeasti mallin hienosäädön ja parempien kehotteiden suunnittelutekniikoiden tarpeen koodin laadun parantamiseksi. Heinäkuussa he [esittelivät parannetun tekoälymallin, joka menee Codexin ohi](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) tarjoten entistä nopeampia ehdotuksia.

Lue postaukset järjestyksessä, jotta voit seurata heidän oppimisprosessiaan.

- **Toukokuu 2023** | [GitHub Copilot paranee koodisi ymmärtämisessä](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Toukokuu 2023** | [Sisältä GitHub: Työskentely LLM-mallien kanssa GitHub Copilotin takana](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Kesäkuu 2023** | [Kuinka kirjoittaa parempia kehotteita GitHub Copilotille](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Heinäkuu 2023** | [.. GitHub Copilot menee Codexin ohi parannetulla tekoälymallilla](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Heinäkuu 2023** | [Kehittäjän opas kehotteiden suunnitteluun ja LLM-malleihin](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Syyskuu 2023** | [Kuinka rakentaa yritystason LLM-sovellus: Oppeja GitHub Copilotista](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Voit myös selata heidän [Teknologia-blogiaan](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) löytääksesi lisää postauksia, kuten [tämän](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), joka näyttää, miten näitä malleja ja tekniikoita _käytetään_ todellisten sovellusten kehittämiseen.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Kehotteen Rakentaminen

Olemme nähneet, miksi kehotteiden suunnittelu on tärkeää – nyt ymmärretään, miten kehotteet _rakennetaan_, jotta voimme arvioida erilaisia tekniikoita tehokkaamman kehotteiden suunnittelun saavuttamiseksi.

### Peruskehotteet

Aloitetaan peruskehotteesta: tekstisyöte, joka lähetetään mallille ilman muuta kontekstia. Tässä esimerkki – kun lähetämme Yhdysvaltojen kansallislaulun ensimmäiset sanat OpenAI:n [Completion API:lle](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), se täydentää vastauksen välittömästi seuraavilla riveillä, havainnollistaen perusennustekäyttäytymistä.

| Kehote (Syöte)     | Täydennys (Vastaus)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Kuulostaa siltä, että aloitat "The Star-Spangled Banner" -kappaleen sanoituksia, joka on Yhdysvaltojen kansallislaulu. Koko teksti on ... |

### Monimutkainen Kehote

Lisätään nyt peruskehotteeseen konteksti ja ohjeet. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) antaa rakentaa monimutkaisen kehotteen kokoelmana _viestejä_, jotka sisältävät:

- Syöte/vastaus-parit, jotka heijastavat _käyttäjän_ syötettä ja _avustajan_ vastausta.
- Järjestelmäviestin, joka asettaa kontekstin avustajan käyttäytymiselle tai persoonallisuudelle.

Pyyntö on nyt alla olevan muotoinen, jossa _tokenisointi_ kaappaa tehokkaasti olennaisen tiedon kontekstista ja keskustelusta. Järjestelmäkontekstin muuttaminen voi vaikuttaa täydennysten laatuun yhtä paljon kuin käyttäjän antamat syötteet.

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

### Ohjeistava Kehote

Yllä olevissa esimerkeissä käyttäjän kehotteena oli yksinkertainen tekstikysely, joka voidaan tulkita tiedonpyynnöksi. _Ohjeistavissa_ kehotteissa voimme käyttää tekstiä tehtävän tarkempaan määrittelyyn, tarjoten tekoälylle parempaa ohjausta. Tässä esimerkki:

| Kehote (Syöte)                                                                                                                                                                                                                         | Täydennys (Vastaus)                                                                                                        | Ohjetyyppi          |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Kirjoita kuvaus sisällissodasta                                                                                                                                                                                                       | _palautti yksinkertaisen kappaleen_                                                                                        | Yksinkertainen      |
| Kirjoita kuvaus sisällissodasta. Anna tärkeät päivämäärät ja tapahtumat sekä kuvaa niiden merkitys                                                                                                                                     | _palautti kappaleen, jota seurasi luettelo tärkeistä päivämääristä ja tapahtumista kuvauksineen_                            | Monimutkainen       |
| Kirjoita kuvaus sisällissodasta yhdellä kappaleella. Anna 3 luetelmakohtaa tärkeistä päivämääristä ja niiden merkityksestä. Anna 3 luetelmakohtaa tärkeistä historiallisista henkilöistä ja heidän panoksistaan. Palauta tulos JSON-tiedostona | _palauttaa laajemmat tiedot tekstikentässä, muotoiltuna JSON-muotoon, jonka voi kopioida tiedostoon ja tarvittaessa validoida_ | Monimutkainen. Muotoiltu. |

## Pääsisältö

Yllä olevissa esimerkeissä kehotteet olivat vielä melko avoimia, antaen LLM:n päättää, mikä osa sen esikoulutetusta aineistosta on relevanttia. _Pääsisältö_-suunnittelumallissa syöteteksti jaetaan kahteen osaan:

- ohje (toiminto)
- relevantti sisältö (joka vaikuttaa toimintaan)

Tässä esimerkissä ohjeena on "tiivistä tämä kahteen lauseeseen".

| Kehote (Syöte)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Täydennys (Vastaus)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter on aurinkoa lähinnä viides planeetta ja aurinkokunnan suurin. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksikertaisesti ja puoli kaikkien muiden aurinkokunnan planeettojen massojen yhteensä. Jupiter on yksi kirkkaimmista paljain silmin nähtävistä kohteista yötaivaalla, ja se on ollut tunnettu muinaisista sivilisaatioista ennen kirjattua historiaa. Se on nimetty roomalaisen jumalan Jupiterin mukaan.[19] Maasta katsottuna Jupiter voi olla tarpeeksi kirkas heijastaakseen valoa, joka luo näkyviä varjoja,[20] ja se on keskimäärin kolmanneksi kirkkaimpia luonnollisia kohteita yötaivaalla Kuun ja Venuksen jälkeen. <br/> **Tiivistä tämä kahteen lyhyeen lauseeseen** | Jupiter, aurinkoa lähinnä viides planeetta, on aurinkokunnan suurin ja yksi kirkkaimmista yötaivaan kohteista. Se on nimetty roomalaisen jumalan Jupiterin mukaan, ja sen massa on kaksikertaisesti ja puoli kaikkien muiden planeettojen yhteismassa. |

Pääsisältöosaa voidaan käyttää monin tavoin tehokkaampien ohjeiden antamiseen:

- **Esimerkit** – sen sijaan, että kerrot mallille suoraan, mitä tehdä, anna esimerkkejä ja anna mallin päätellä kaava.
- **Vihjeet** – seuraa ohjetta "vihjeellä", joka ohjaa täydennystä ja ohjaa mallia kohti relevantimpia vastauksia.
- **Mallit** – toistettavia 'reseptejä' kehotteille, joissa on paikkamerkkejä (muuttujia), joita voi räätälöidä datalla tiettyihin käyttötarkoituksiin.

Tutkitaan näitä käytännössä.

### Esimerkkien Käyttö

Tässä lähestymistavassa käytetään pääsisältöä "ruokkimaan mallia" esimerkeillä halutusta tuloksesta tietylle ohjeelle, ja annetaan mallin päätellä kaava halutulle tulokselle. Esimerkkien määrän perusteella voidaan käyttää zero-shot-, one-shot-, few-shot-kehotteita jne.

Kehote koostuu nyt kolmesta osasta:

- Tehtävän kuvaus
- Muutama esimerkki halutusta tuloksesta
- Uuden esimerkin alku (joka toimii implisiittisenä tehtävän kuvauksena)

| Oppimistyppi  | Kehote (Syöte)                                                                                                                                        | Täydennys (Vastaus)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Käännä espanjaksi                                                                                                              | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => "El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | Pelaaja juoksi pesille => Baseball <br/> Pelaaja teki ässän => Tennis <br/> Pelaaja teki kuuden => Cricket <br/> Pelaaja teki donkin => | Koripallo                  |
|               |                                                                                                                                                       |                             |

Huomaa, että zero-shot-kehotteessa piti antaa selkeä ohje ("Käännä espanjaksi"), mutta one-shot-esimerkissä se pääteltiin automaattisesti. Few-shot-esimerkki osoittaa, miten useampien esimerkkien lisääminen antaa malleille tarkemman päätelmän ilman lisäohjeita.

### Kehotevihjeet

Toinen tapa käyttää pääsisältöä on antaa _vihjeitä_ esimerkkien sijaan. Tässä tapauksessa annamme mallille pienen sysäyksen oikeaan suuntaan _aloittamalla_ katkelmalla, joka heijastaa haluttua vastausmuotoa. Malli sitten "ottaa vihjeen" ja jatkaa samaan tyyliin.

| Vihjeiden määrä | Kehote (Syöte)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Täydennys (Vastaus)                                                                                                                                                                                                                                                                                       |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0               | Jupiter on aurinkoa lähinnä viides planeetta ja aurinkokunnan suurin. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksikertaisesti ja puoli kaikkien muiden aurinkokunnan planeettojen massojen yhteensä. Jupiter on yksi kirkkaimmista paljain silmin nähtävistä kohteista yötaivaalla, ja se on ollut tunnettu muinaisista sivilisaatioista ennen kirjattua historiaa.

**Summarize This**                                       | Jupiter on aurinkokuntamme suurin planeetta ja viides etäisyydeltään Auringosta. Se on kaasujättiläinen, jonka massa on 1/1000 Auringon massasta, mutta se painaa enemmän kuin kaikki muut planeetat yhteensä. Muinaiset sivilisaatiot ovat tunteneet Jupiterin jo pitkään, ja se näkyy helposti paljain silmin yötaivaalla. |
| 1              | Jupiter on viides planeetta Auringosta ja suurin aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden aurinkokunnan planeettojen yhteismassaa suurempi. Jupiter on yksi kirkkaimmista paljain silmin nähtävistä kohteista yötaivaalla, ja muinaiset sivilisaatiot ovat tunteneet sen jo ennen kirjoitettua historiaa. <br/>**Summarize This** <br/> Mitä opimme on, että Jupiter | on viides planeetta Auringosta ja suurin aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden planeettojen yhteismassaa suurempi. Se näkyy helposti paljain silmin ja on tunnettu jo muinaisajoista lähtien.                        |
| 2              | Jupiter on viides planeetta Auringosta ja suurin aurinkokunnassa. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden aurinkokunnan planeettojen yhteismassaa suurempi. Jupiter on yksi kirkkaimmista paljain silmin nähtävistä kohteista yötaivaalla, ja muinaiset sivilisaatiot ovat tunteneet sen jo ennen kirjoitettua historiaa. <br/>**Summarize This** <br/> Kolme tärkeintä faktaa, jotka opimme:         | 1. Jupiter on viides planeetta Auringosta ja suurin aurinkokunnassa. <br/> 2. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta...<br/> 3. Jupiter on ollut paljain silmin nähtävissä muinaisajoista lähtien ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

Prompt-malli on _ennalta määritelty ohjeistus_, jota voidaan tallentaa ja käyttää uudelleen tarpeen mukaan, jotta käyttäjäkokemukset olisivat johdonmukaisempia laajassa mittakaavassa. Yksinkertaisimmillaan se on kokoelma promptiesimerkkejä, kuten [tämä OpenAI:n esimerkki](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), joka sisältää sekä vuorovaikutteiset prompt-komponentit (käyttäjän ja järjestelmän viestit) että API-pohjaisen pyyntömuodon – tukemaan uudelleenkäyttöä.

Monimutkaisemmassa muodossa, kuten [tämä LangChainin esimerkki](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), se sisältää _paikkamerkkejä_, jotka voidaan korvata tiedoilla eri lähteistä (käyttäjän syöte, järjestelmän konteksti, ulkoiset tietolähteet jne.) luodakseen promptin dynaamisesti. Tämä mahdollistaa uudelleenkäytettävien prompt-kirjastojen luomisen, joita voidaan käyttää johdonmukaisten käyttäjäkokemusten luomiseen **ohjelmallisesti** laajassa mittakaavassa.

Lopuksi mallien todellinen arvo on kyvyssä luoda ja julkaista _prompt-kirjastoja_ vertikaalisille sovellusalueille – joissa prompt-malli on nyt _optimoitu_ heijastamaan sovelluskohtaisia konteksteja tai esimerkkejä, jotka tekevät vastauksista osuvampia ja tarkempia kohdeyleisölle. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) -arkisto on erinomainen esimerkki tästä lähestymistavasta, joka kokoaa koulutusalalle suunnattuja promptteja painottaen keskeisiä tavoitteita kuten opetussuunnitelman suunnittelua, kurssisuunnittelua ja opiskelijoiden ohjausta.

## Supporting Content

Jos ajattelemme promptin rakentamista ohjeena (tehtävä) ja kohteena (ensisijainen sisältö), niin _toissijainen sisältö_ on kuin lisäkonteksti, jota annamme **vaikuttaaksemme tulokseen jollain tavalla**. Se voi olla säätöparametreja, muotoiluohjeita, aiheiden taksonomioita jne., jotka auttavat mallia _räätälöimään_ vastauksensa vastaamaan haluttuja käyttäjätavoitteita tai odotuksia.

Esimerkiksi: Kun meillä on kurssiluettelo, jossa on laaja metadata (nimi, kuvaus, taso, metatunnisteet, opettaja jne.) kaikista opetussuunnitelman kursseista:

- voimme määritellä ohjeen "tiivistä syksyn 2023 kurssiluettelo"
- voimme käyttää ensisijaista sisältöä antaaksemme muutaman esimerkin halutusta lopputuloksesta
- voimme käyttää toissijaista sisältöä tunnistaaksemme viisi kiinnostavinta "tunnistetta".

Nyt malli voi antaa yhteenvedon esimerkkien mukaisessa muodossa – mutta jos tuloksessa on useita tunnisteita, se voi priorisoida toissijaisessa sisällössä määritellyt viisi tunnistetta.

---

<!--
LESSON TEMPLATE:
Tämän osion tulisi kattaa ydinkonsepti #1.
Vahvista konseptia esimerkeillä ja viitteillä.

KONSEPTI #3:
Prompt-tekniikat.
Mitkä ovat joitakin perusmenetelmiä promptin suunnittelussa?
Havainnollista niitä harjoituksilla.
-->

## Promptin parhaat käytännöt

Nyt kun tiedämme, miten promptteja voi _rakentaa_, voimme alkaa pohtia, miten niitä _suunnitellaan_ parhaiden käytäntöjen mukaisesti. Voimme ajatella tätä kahdessa osassa – oikean _ajattelutavan_ omaksuminen ja oikeiden _tekniikoiden_ käyttäminen.

### Prompt Engineering -ajattelutapa

Prompt Engineering on kokeiluun ja virheisiin perustuva prosessi, joten pidä mielessä kolme laajaa ohjenuoraa:

1. **Toimialan ymmärrys on tärkeää.** Vastauksen tarkkuus ja osuvuus riippuvat _toimialasta_, jolla sovellus tai käyttäjä toimii. Käytä intuitiotasi ja toimialan asiantuntemustasi _muokataksesi tekniikoita_ tarkemmin. Määrittele esimerkiksi _toimialakohtaiset persoonat_ järjestelmän promptteihin tai käytä _toimialakohtaisia malleja_ käyttäjän promptteihin. Tarjoa toissijaista sisältöä, joka heijastaa toimialakohtaisia konteksteja, tai käytä _toimialakohtaisia vihjeitä ja esimerkkejä_ ohjaamaan mallia tuttuun käyttötapaan.

2. **Mallin ymmärrys on tärkeää.** Tiedämme, että mallit ovat luonteeltaan stokastisia. Mutta mallien toteutukset voivat myös vaihdella käytetyn koulutusdatan (esikoulutettu tieto), tarjoamien ominaisuuksien (esim. API tai SDK) ja optimoidun sisältötyypin (esim. koodi vs. kuvat vs. teksti) suhteen. Ymmärrä käyttämäsi mallin vahvuudet ja rajoitukset, ja käytä tätä tietoa _priorisoidaksesi tehtäviä_ tai rakentaaksesi _räätälöityjä malleja_, jotka on optimoitu mallin kyvykkyyksille.

3. **Iterointi ja validointi ovat tärkeitä.** Mallit kehittyvät nopeasti, samoin prompt engineering -tekniikat. Toimialan asiantuntijana sinulla voi olla muuta kontekstia tai kriteerejä _oman_ sovelluksesi osalta, jotka eivät välttämättä päde laajempaan yhteisöön. Käytä prompt engineering -työkaluja ja -tekniikoita "aloittaaksesi" promptin rakentamisen, sitten iteroi ja validoi tulokset oman intuitiosi ja asiantuntemuksesi avulla. Tallenna oivalluksesi ja luo **tietopankki** (esim. prompt-kirjastoja), jota muut voivat käyttää uutena lähtökohtana nopeampiin iterointeihin tulevaisuudessa.

## Parhaat käytännöt

Katsotaanpa nyt yleisiä parhaita käytäntöjä, joita suosittelevat [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ja [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) -asiantuntijat.

| Mitä                              | Miksi                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Arvioi uusimmat mallit.           | Uudet mallisukupolvet sisältävät todennäköisesti parannettuja ominaisuuksia ja laatua – mutta voivat myös aiheuttaa korkeampia kustannuksia. Arvioi niiden vaikutus ja tee siirtymispäätökset sen perusteella.                                        |
| Erottele ohjeet ja konteksti      | Tarkista, määrittääkö mallisi/palveluntarjoajasi _erottimet_, joilla ohjeet, ensisijainen ja toissijainen sisältö erotetaan selkeämmin. Tämä auttaa malleja painottamaan tokeneita tarkemmin.                                                        |
| Ole tarkka ja selkeä              | Anna enemmän yksityiskohtia halutusta kontekstista, lopputuloksesta, pituudesta, muodosta, tyylistä jne. Tämä parantaa sekä vastauksen laatua että johdonmukaisuutta. Tallenna ohjeet uudelleenkäytettäviin malleihin.                              |
| Ole kuvaileva, käytä esimerkkejä  | Mallit voivat vastata paremmin "näytä ja kerro" -lähestymistapaan. Aloita `zero-shot`-menetelmällä, jossa annat ohjeen (mutta et esimerkkejä), ja kokeile sitten `few-shot`-menetelmää, jossa annat muutaman esimerkin halutusta lopputuloksesta. Käytä vertauksia. |
| Käytä vihjeitä aloittamaan vastaukset | Ohjaa mallia haluttuun lopputulokseen antamalla sille aloitussanoja tai -lauseita, joita se voi käyttää vastauksen lähtökohtana.                                                                                                               |
| Toista tarvittaessa               | Joskus mallille täytyy toistaa ohjeita. Anna ohjeet ennen ja jälkeen ensisijaisen sisällön, käytä ohjetta ja vihjettä jne. Iteroi ja validoi, mikä toimii parhaiten.                                                                             |
| Järjestyksellä on merkitystä      | Tiedon esitysjärjestys mallille voi vaikuttaa lopputulokseen, myös oppimisesimerkeissä, johtuen tuoreusvinoumasta. Kokeile eri vaihtoehtoja nähdäksesi, mikä toimii parhaiten.                                                                   |
| Anna mallille "uloskäynti"        | Anna mallille _varavastaus_, jonka se voi antaa, jos se ei jostain syystä pysty suorittamaan tehtävää. Tämä voi vähentää virheellisten tai keksittyjen vastausten riskiä.                                                                           |
|                                   |                                                                                                                                                                                                                                                   |

Kuten minkä tahansa parhaan käytännön kohdalla, muista että _kokemuksesi voi vaihdella_ mallin, tehtävän ja toimialan mukaan. Käytä näitä lähtökohtana ja iteroi löytääksesi sinulle parhaiten toimivat tavat. Arvioi prompt engineering -prosessiasi jatkuvasti uudelleen uusien mallien ja työkalujen tullessa saataville, keskittyen prosessin skaalautuvuuteen ja vastausten laatuun.

<!--
LESSON TEMPLATE:
Tämän osion tulisi sisältää kooditehtävä, jos sovellettavissa

TEHTÄVÄ:
Linkki Jupyter Notebookiin, jossa on vain koodikommentit ohjeissa (koodiosiot ovat tyhjiä).

RATKAISU:
Linkki kopioon kyseisestä Notebookista, jossa promptit on täytetty ja suoritettu, näyttäen yhden esimerkkiratkaisun.
-->

## Tehtävä

Onnittelut! Pääsit oppitunnin loppuun asti! Nyt on aika testata joitakin opittuja käsitteitä ja tekniikoita käytännössä!

Tehtävässämme käytämme Jupyter Notebookia, jossa on harjoituksia, joita voit tehdä vuorovaikutteisesti. Voit myös laajentaa Notebookia omilla Markdown- ja koodisoluillasi tutkiaksesi ideoita ja tekniikoita itsenäisesti.

### Aloittaaksesi, tee fork reposta, sitten

- (Suositeltu) Käynnistä GitHub Codespaces
- (Vaihtoehtoisesti) Kloonaa repo paikalliselle laitteellesi ja käytä sitä Docker Desktopin kanssa
- (Vaihtoehtoisesti) Avaa Notebook haluamallasi Notebook-ympäristöllä.

### Seuraavaksi määritä ympäristömuuttujat

- Kopioi repohakemiston juuresta `.env.copy` tiedosto nimellä `.env` ja täytä `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ja `AZURE_OPENAI_DEPLOYMENT` arvot. Palaa [Learning Sandbox -osioon](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) oppiaksesi miten.

### Avaa sitten Jupyter Notebook

- Valitse ajoympäristön ydin. Jos käytät vaihtoehtoja 1 tai 2, valitse kehityssäiliön tarjoama oletus Python 3.10.x -ydin.

Olet valmis suorittamaan harjoitukset. Huomaa, että tässä ei ole _oikeita tai vääriä_ vastauksia – kyse on vaihtoehtojen kokeilemisesta ja intuitiosi kehittämisestä sen suhteen, mikä toimii tietylle mallille ja sovellusalueelle.

_Tämän vuoksi tässä oppitunnissa ei ole koodiratkaisujen osioita. Sen sijaan Notebookissa on Markdown-soluja nimeltä "My Solution:", jotka näyttävät yhden esimerkkivastauksen vertailun vuoksi._

 <!--
LESSON TEMPLATE:
Päätä osio yhteenvedolla ja itseohjautuvan oppimisen resursseilla.
-->

## Tietovisa

Mikä seuraavista on hyvä prompt, joka noudattaa kohtuullisia parhaita käytäntöjä?

1. Näytä minulle kuva punaisesta autosta  
2. Näytä minulle kuva punaisesta Volvon XC90 -merkkisestä autosta, joka on pysäköity kallion reunalle auringonlaskun aikaan  
3. Näytä minulle kuva punaisesta Volvon XC90 -merkkisestä autosta

Vastaus: 2, se on paras prompt, koska se antaa yksityiskohtia "mitä" ja menee tarkkuuksiin (ei mikä tahansa auto, vaan tietty merkki ja malli) ja kuvaa myös kokonaisympäristön. 3 on seuraavaksi paras, koska se sisältää myös paljon kuvausta.

## 🚀 Haaste

Kokeile hyödyntää "vihje" -tekniikkaa promptilla: Täydennä lause "Näytä minulle kuva punaisesta Volvon merkistä ja ". Miten malli vastaa, ja miten parantaisit sitä?

## Hienoa työtä! Jatka oppimista

Haluatko oppia lisää erilaisista Prompt Engineering -käsitteistä? Mene [jatko-oppimissivulle](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) löytääksesi muita erinomaisia resursseja tästä aiheesta.

Siirry oppitunnille 5, jossa tarkastelemme [edistyneitä prompt-tekniikoita](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.