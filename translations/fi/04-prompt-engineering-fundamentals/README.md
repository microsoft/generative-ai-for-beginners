# Promptin suunnittelun perusteet

[![Promptin suunnittelun perusteet](../../../translated_images/fi/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Johdanto
Tämä moduuli käsittelee olennaisia käsitteitä ja menetelmiä tehokkaiden kehotteiden luomiseen generatiivisissa tekoälymalleissa. Tapa, jolla kirjoitat kehotteesi LLM:lle, on myös merkityksellinen. Huolellisesti laadittu kehotepyyntö voi saavuttaa paremman vastauslaadun. Mutta mitä tarkalleen ottaen tarkoittavat termit _prompt_ ja _prompt engineering_? Ja miten parannan kehotteessa lähetettyä _syötettä_ LLM:lle? Näihin kysymyksiin pyrimme vastaamaan tässä ja seuraavassa luvussa.

_Generatiivinen tekoäly_ pystyy luomaan uutta sisältöä (esim. tekstiä, kuvia, ääntä, koodia jne.) käyttäjän pyyntöjen perusteella. Se toteutuu käyttämällä _suuria kielimalleja_ kuten OpenAI:n GPT ("Generative Pre-trained Transformer") -sarjaa, jotka on koulutettu käyttämään luonnollista kieltä ja koodia.

Käyttäjät voivat nyt olla vuorovaikutuksessa näiden mallien kanssa tutun kaltaisin paradigmin, kuten chatin avulla, ilman teknistä asiantuntemusta tai koulutusta. Mallit ovat _prompt-pohjaisia_ – käyttäjät lähettävät tekstisyötteen (kehotteen) ja saavat takaisin tekoälyn vastauksen (täydennyksen). He voivat jatkaa "keskustelua tekoälyn kanssa" iteratiivisesti, monenvaiheisissa keskusteluissa, hienosäätäen kehotettaan, kunnes vastaus vastaa odotuksia.

"Nyt promptit" ovat päätason _ohjelmointirajapinta_ generatiivisille tekoälysovelluksille, jotka kertovat malleille, mitä tehdä, ja vaikuttavat palautettujen vastausten laatuun. "Prompt engineering" on nopeasti kasvava tutkimusala, joka keskittyy kehotteiden _suunnitteluun ja optimointiin_ johdonmukaisten ja laadukkaiden vastausten tuottamiseksi laajasti.

## Tavoitteet

Tässä oppitunnissa opimme, mitä Prompt Engineering on, miksi se on tärkeää, ja miten voimme luoda tehokkaampia kehotteita tietylle mallille ja sovelluskohtaiselle tavoitteelle. Ymmärrämme keskeiset käsitteet ja parhaat käytännöt promptin suunnitteluun – ja opimme interaktiivisesta Jupyter Notebook -”hiekkalaatikko”-ympäristöstä, jossa näemme nämä käsitteet käytännön esimerkeissä.

Oppitunnin lopuksi osaamme:

1. Selittää, mitä prompt engineering on ja miksi se on tärkeää.
2. Kuvata kehotteen osat ja miten niitä käytetään.
3. Oppia parhaat käytännöt ja tekniikat prompt engineeringiin.
4. Soveltaa opittuja tekniikoita todellisiin esimerkkeihin OpenAI-päätepisteen avulla.

## Keskeiset termit

Prompt Engineering: Käytäntö suunnitella ja hioa syötteitä ohjatakseen tekoälymalleja tuottamaan haluttuja tuloksia.  
Tokenisointi: Prosessi, jossa teksti muunnetaan pienemmiksi yksiköiksi eli tokeneiksi, joita malli ymmärtää ja käsittelee.  
Ohjeistuksella hienosäädetyt LLM:t: Suuret kielimallit (LLM) joita on hienosäädetty erityisillä ohjeilla vastaustarkkuuden ja merkityksellisyyden parantamiseksi.

## Oppimishiekkalaatikko

Promptin suunnittelu on tällä hetkellä enemmän taitolaji kuin tiede. Parasta tapaa kehittää intuitioita on _harjoitella enemmän_ ja omaksua kokeiluvirheen menetelmä, joka yhdistää sovellusalueen asiantuntemuksen suositeltuihin tekniikoihin ja mallikohtaisiin optimointeihin.

Tähän oppituntiin liittyvä Jupyter Notebook tarjoaa _hiekkalaatikko_-ympäristön, jossa voit kokeilla oppimaasi – joko oppimisen aikana tai lopussa olevan kooditehtävän osana. Harjoitusten suorittamiseen tarvitset:

1. **Azure OpenAI API -avaimen** – palvelun päätepisteen käyttöön otetulle LLM:lle.  
2. **Python-ympäristön** – jossa Notebook voidaan suorittaa.  
3. **Paikalliset ympäristömuuttujat** – _täydennä [ASENNUS](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) -vaiheet nyt valmistautuaksesi_.

Notebookin mukana tulee _aloitusharjoituksia_ – mutta sinua kannustetaan lisäämään omia _Markdown_-tekstikuvauksia ja _Code_-kehotteita kokeillaksesi lisää esimerkkejä tai ideoita – ja kehittääksesi intuitiotasi kehotteiden suunnittelussa.

## Kuvitettu opas

Haluatko saada kokonaiskuvan tästä oppitunnista ennen kuin sukellat syvemmälle? Katso tämä kuvitusopas, joka antaa sinulle käsityksen keskeisistä aiheista ja avainasioista, joita kannattaa pohdiskella kussakin. Oppitunnin tiekartta vie sinut ydinajatusten ja haasteiden ymmärtämisestä niiden ratkomiseen asiaankuuluvilla promptin suunnittelun tekniikoilla ja parhailla käytännöillä. Huomaa, että tämän oppaan "Edistyneet tekniikat" -osio viittaa tämän opetussuunnitelman _seuraavassa_ luvussa käsiteltävään sisältöön.

![Illustrated Guide to Prompt Engineering](../../../translated_images/fi/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Yrityksemme

Nyt puhutaan siitä, miten _tämä aihe_ liittyy startup-yrityksemme missioon [tuoda tekoälyä innovaatioihin koulutuksessa](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Haluamme rakentaa tekoälyllä toimivia sovelluksia _personoituun oppimiseen_ – joten pohtikaamme, miten eri käyttäjät sovelluksessamme voisivat "suunnitella" kehotteita:

- **Järjestelmänvalvojat** voivat pyytää tekoälyä _analysoimaan opetussuunnitelmatietoja katvealueiden löytämiseksi_. Tekoäly voi tiivistää tulokset tai visualisoida niitä koodin avulla.  
- **Opettajat** voivat pyytää tekoälyä _luomaan oppituntisuunnitelman kohdeyleisölle ja aiheelle_. Tekoäly voi rakentaa personoidun suunnitelman määritellyssä muodossa.  
- **Oppilaat** voivat pyytää tekoälyä _ohjaamaan heitä vaikeassa oppiaineessa_. Tekoäly voi nyt opastaa oppilaita oppitunneilla, vihjeillä ja esimerkeillä, jotka on räätälöity heidän tasolleen.

Tämä on vasta jäävuoren huippu. Tutustu [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) -avoin lähdekoodi -kehotekirjastoon, jota koulutusasiantuntijat ylläpitävät – saat laajemman kuvan mahdollisuuksista! _Kokeile ajaa joitain näistä kehotteista hiekkalaatikossa tai OpenAI Playgroundissa nähdäksesi mitä tapahtuu!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Mitä on promptin suunnittelu?

Aloitimme tämän oppitunnin määrittelemällä **prompt engineeringin** prosessina, jossa _suunnitellaan ja optimoidaan_ tekstisyötteitä (kehotteita) johdonmukaisten ja laadukkaiden vastausten (täydennysten) tuottamiseksi tiettyyn sovelluskohteeseen ja malliin. Voimme ajatella sen olevan kaksivaiheinen prosessi:

- _suunnitellaan_ alkuperäinen kehotepyyntö tietylle mallille ja tavoitteelle  
- _hienosäädetään_ kehotetta iteratiivisesti vastauksen laadun parantamiseksi

Tämä on väistämättä kokeilu- ja virheprosessi, joka vaatii käyttäjän intuitiota ja vaivaa optimaalisien tulosten saavuttamiseksi. Miksi se sitten on tärkeää? Vastataksemme siihen, meidän täytyy ensin ymmärtää kolme käsitettä:

- _tokenisointi_ = miten malli "näkee" kehotteen  
- _Perus-LLM:t_ = kuinka perustason malli "käsittelee" kehotetta  
- _Ohjeistuksella hienosäädetyt LLM:t_ = miten malli voi nyt nähdä "tehtäviä"

### Tokenisointi

LLM näkee kehotteet _token-jonona_, jossa eri mallit (tai malliversiot) voivat tokenisoida saman kehotteen eri tavoin. Koska LLM:t on koulutettu tokeneihin (eikä raakaan tekstiin), kehotteiden tokenisoinnilla on suora vaikutus luodun vastauksen laatuun.

Tokenisoinnin toimintaa voi havainnollistaa kokeilemalla esimerkiksi [OpenAI Tokenizeria](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst). Kopioi oma kehotteesi ja katso, miten se muutetaan tokeneiksi, kiinnittäen huomiota välilyöntien ja välimerkkien käsittelyyn. Huomaa, että tämä esimerkki käyttää vanhempaa LLM-mallia (GPT-3), joten uudella mallilla tulos voi olla erilainen.

![Tokenization](../../../translated_images/fi/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Käsite: Perusmallit

Kun kehotteeseen on tehty tokenisointi, ["Perus-LLM:n"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (tai perustason mallin) päätarkoitus on ennustaa seuraava token tässä jonoissa. Koska LLM:t on koulutettu valtaviin tekstiaineistoihin, niillä on hyvä käsitys tokenien tilastollisista suhteista, ja ne voivat tehdä tämän ennustuksen varmuudella. Huomaa, etteivät ne ymmärrä sanojen _merkitystä_ kehotteessa tai tokenissa; ne vain näkevät kuviota, jonka voivat "täydentää" seuraavalla ennusteellaan. Ne voivat jatkaa sarjan ennustamista, kunnes prosessi päätetään käyttäjän toimesta tai jonkin ennalta määrätyn ehdon perusteella.

Haluatko nähdä, miten kehotteeseen perustuva täydennys toimii? Syötä yllä oleva kehoite Azure OpenAI Studioon [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) oletusasetuksilla. Järjestelmä on konfiguroitu käsittelemään kehotteet tiedonpyyntöinä, joten näet vastauksen, joka sopii tähän kontekstiin.

Mutta entä jos käyttäjä haluaa nähdä jotain tiettyä, mikä täyttää jonkin kriteerin tai tehtävässä määritellyn tavoitteen? Tässä kuvaan tulevat _ohjeistuksella hienosäädetyt_ LLM:t.

![Base LLM Chat Completion](../../../translated_images/fi/04-playground-chat-base.65b76fcfde0caa67.webp)

### Käsite: Ohjeistuksella hienosäädetyt LLM:t

[Ohjeistuksella hienosäädetty LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) lähtee perustason mallista ja hienosäätää sitä esimerkkien tai syöte-/tulosparien avulla (esim. monivaiheiset "viestit"), joihin voi sisältyä selkeitä ohjeita – ja tekoälyn vastaus yrittää noudattaa tätä ohjetta.

Tämä hyödyntää tekniikoita kuten vahvistusoppimista ihmispalautteen avulla (RLHF), joka voi opettaa mallia _noudattamaan ohjeita_ ja _oppimaan palautteesta_, jotta se tuottaa paremmin käytännön sovelluksiin soveltuvia ja käyttäjän tavoitteita vastaavia vastauksia.

Kokeillaan: palaa yllä olevaan kehotteeseen, mutta vaihda nyt _järjestelmäviesti_ antamaan seuraava ohje kontekstina:

> _Tiivistä annettu sisältö toisluokkalaiselle. Pidä tulos yhdessä kappaleessa, jossa on 3–5 kohdekohtaa._

Katso, miten tulos on nyt viritetty kuvastamaan haluttua tavoitetta ja muotoa? Opettaja voi käyttää tätä vastausta suoraan oppituntien dioissa.

![Instruction Tuned LLM Chat Completion](../../../translated_images/fi/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Miksi promptin suunnittelua tarvitaan?

Nyt kun tiedämme, miten kehotteet käsitellään LLM:issä, keskustellaan _miksi_ prompt engineering on tarpeen. Vastaus löytyy siitä, että nykyiset LLM:t aiheuttavat useita haasteita, jotka tekevät _luotettavien ja johdonmukaisten vastauksien_ saavuttamisen vaikeammaksi ilman työtä promptin rakentamiseksi ja optimoimiseksi. Esimerkiksi:

1. **Mallien vastaukset ovat stokastisia.** _Sama kehoite_ tuottaa todennäköisesti erilaisia vastauksia eri malleilla tai malliversioilla. Ja se voi jopa tuottaa eri tuloksia _samalla mallilla_ eri aikoina. _Promptin suunnittelun tekniikat auttavat minimoimaan näitä vaihteluita tarjoamalla paremmin hallittuja reunaehtoja._

1. **Mallien vastaukset voivat olla keksittyjä.** Mallit on koulutettu _suuriin mutta rajallisiin_ aineistoihin, mikä tarkoittaa, että niiltä puuttuu tieto käsitteistä koulutuksen ulkopuolella. Tämän seurauksena ne voivat tuottaa täydennyksiä, jotka ovat epätarkkoja, kuvitteellisia tai suoraan ristiriidassa tunnettujen tosiseikkojen kanssa. _Promptin suunnittelun tekniikat auttavat käyttäjiä tunnistamaan ja lieventämään tällaisia keksintöjä esimerkiksi pyytämällä tekoälyä antamaan lähdeviitteitä tai perusteluja._

1. **Mallien kyvyt vaihtelevat.** Uudemmilla malleilla tai mallisukupolvilla on rikkaammat ominaisuudet, mutta myös omat ainutlaatuiset omituisuutensa ja kompromissinsa kustannusten ja monimutkaisuuden suhteen. _Promptin suunnittelu voi auttaa kehittämään parhaat käytännöt ja työnkulut, jotka abstrahoivat erot ja sopeutuvat mallikohtaisiin vaatimuksiin skaalautuvasti ja saumattomasti._

Katso tätä käytännössä OpenAI:n tai Azure OpenAI Playgroundin avulla:

- Käytä samaa kehotetta eri LLM-julkaisuilla (esim. OpenAI, Azure OpenAI, Hugging Face) – näitkö vaihteluja?  
- Käytä samaa kehotetta toistuvasti _saman_ LLM-julkaisun kanssa (esim. Azure OpenAI Playground) – miten nämä vaihtelut erosivat?

### Keksinnän esimerkki

Tässä kurssissa käytämme termiä **"keksintä"** viittaamaan ilmiöön, jossa LLM:t joskus tuottavat tosiasiallisesti virheellistä tietoa koulutuksensa rajoitteiden tai muiden tekijöiden vuoksi. Olet ehkä kuullut tästä ilmiöstä myös nimellä _”hallusinaatiot”_ suosituissa artikkeleissa tai tutkimuspapereissa. Suosittelemme kuitenkin käyttämään _"keksintä"_ termiä, jotta emme vahingossa antropomorfisoi toimintaa liittämällä siihen inhimillisiä piirteitä koneohjatun tuloksen sijaan. Tämä myös vahvistaa [Vastuullisen tekoälyn ohjeistuksia](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminologian näkökulmasta, poistaa sanoja, joita joissain yhteyksissä voidaan pitää loukkaavina tai ei-vastuullisina.

Haluatko hahmottaa, miten keksinnät toimivat? Ajattele kehotetta, joka ohjeistaa tekoälyä tuottamaan sisältöä olemattomasta aiheesta (varmistaakseen, ettei sitä löydy koulutusaineistosta). Esimerkiksi – kokeilin tätä kehotetta:

> **Kehoite:** luo oppituntisuunnitelma vuonna 2076 käydystä Marsin sodasta.
Verkkohaku osoitti, että Martian sodista löytyi fiktiivisiä kertomuksia (esim. televisiosarjoja tai kirjoja) – mutta ei yhtään vuodelle 2076. Terve järki kertoo myös, että vuosi 2076 on _tulevaisuudessa_ eikä sitä siksi voida liittää todelliseen tapahtumaan.

Mitä sitten tapahtuu, kun ajatamme tätä kehotetta eri LLM-palveluntarjoajilla?

> **Vastaus 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/fi/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Vastaus 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/fi/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Vastaus 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/fi/04-fabrication-huggingchat.faf82a0a51278956.webp)

Kuten odotettua, kukin malli (tai malli-versio) tuottaa hieman erilaisia vastauksia stokastisen käyttäytymisen ja mallin kyvykkyyksissä esiintyvien vaihteluiden ansiosta. Esimerkiksi yksi malli kohdistaa vastauksen 8. luokan yleisölle, kun taas toinen olettaa lukion oppilaan. Mutta kaikki kolme mallia generoi vastauksia, jotka voisivat vakuuttaa tiedottoman käyttäjän siitä, että tapahtuma oli todellinen.

Kehoteinsinöörin tekniikat kuten _metakehotus_ ja _lämpötilan konfigurointi_ saattavat jonkin verran vähentää mallien sepitteitä. Uudet kehotearkkitehtuurit integroivat myös saumattomasti uusia työkaluja ja tekniikoita kehotevirtaan lieventääkseen tai vähentääkseen näitä ilmiöitä.

## Tapaustutkimus: GitHub Copilot

Päätetään tämä osio tarkastelemalla, miten kehotearkkitehtuuria käytetään todellisissa ratkaisuissa yhdellä tapaustutkimuksella: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot on sinun "tekoälypari-ohjelmoijasi" – se muuntaa tekstikehotteita koodin täydennyksiksi ja on integroitu kehitysympäristöösi (esim. Visual Studio Code) saumattoman käyttökokemuksen takaamiseksi. Alla dokumentoiduissa blogisarjoissa varhaisin versio perustui OpenAI Codex -malliin – insinöörit ymmärsivät nopeasti tarpeen hienosäätää mallia ja kehittää parempia kehotetekniikoita parantaakseen koodin laatua. Heinäkuussa he [esittelivät parannetun tekoälymallin, joka menee Codexin ohi](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) vielä nopeampia ehdotuksia varten.

Lue blogit järjestyksessä, niin seuraat heidän oppimispolkuaan.

- **Toukokuu 2023** | [GitHub Copilotin kyky ymmärtää koodiasi paranee](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Toukokuu 2023** | [GitHubin sisällä: Työskentely LLM-mallien kanssa GitHub Copilotin takana](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Kesäkuu 2023** | [Miten kirjoittaa parempia kehotteita GitHub Copilotille](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Heinäkuu 2023** | [GitHub Copilot menee Codexin ohi parannetulla tekoälymallilla](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Heinäkuu 2023** | [Kehittäjän opas kehotearkkitehtuurin ja LLM-mallien käyttöön](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Syyskuu 2023** | [Miten rakentaa yritystason LLM-sovellus: Oppeja GitHub Copilotista](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Voit myös selata heidän [Insinööriblogiaan](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) löytääksesi lisää tekstejä kuten [tämä](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), joka näyttää, miten näitä malleja ja tekniikoita _käytetään_ todellisten sovellusten ajamiseen.

---

## Kehotteen Rakentaminen

Olemme nähneet, miksi kehotearkkitehtuuri on tärkeää – nyt ymmärretään, miten kehotteet _rakennetaan_, jotta voimme arvioida eri tekniikoita tehokkaamman kehotteensuunnittelun saavuttamiseksi.

### Peruskehotteet

Aloitetaan peruskehotteesta: tekstisyöte, joka lähetetään mallille ilman muuta kontekstia. Tässä esimerkki – kun lähetämme ensimmäiset sanat Yhdysvaltain kansallislaulusta OpenAI:n [Completion API:lle](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), se _täyttää automaattisesti_ vastauksen seuraavilla riveillä, mikä havainnollistaa perusennustekäyttäytymistä.

| Kehote (Syöte)     | Täydennys (Vastaus)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Vaikuttaa siltä, että aloitat sanoituksia kappaleesta "The Star-Spangled Banner", Yhdysvaltain kansallislaulusta. Täydet sanat ovat ... |

### Monimutkainen kehotus

Lisätään nyt kontekstia ja ohjeita tähän peruskehotteeseen. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) antaa meille mahdollisuuden rakentaa monimutkainen kehotus viestien kokoelmana, jossa on:

- Käyttäjän syöte ja avustajan vastaus -parit.
- Järjestelmäviesti, joka asettaa kontekstin avustajan käyttäytymiselle tai persoonalle.

Pyyntö on nyt alla olevan muotoinen, ja _tokenisointi_ tallentaa tehokkaasti olennaisen tiedon kontekstista ja keskustelusta. Järjestelmäkontekstin muuttaminen voi vaikuttaa täydennysten laatuun yhtä paljon kuin käyttäjän syötteet.

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

### Ohjeistuskehotteet

Yllä olevissa esimerkeissä käyttäjän kehotus oli yksinkertainen tekstikysely, joka voidaan tulkita tiedonpyyntönä. _Ohjeistuskehotteissa_ voimme käyttää tekstiä tehtävän määrittelyyn tarkemmin, tarjoten tekoälylle parempaa ohjausta. Tässä esimerkki:

| Kehote (Syöte)                                                                                                                                                                                                                         | Täydennys (Vastaus)                                                                                                        | Ohjetyyppi          |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Kirjoita kuvaus sisällissodasta                                                                                                                                                                                                       | _palautti yksinkertaisen kappaleen_                                                                                        | Yksinkertainen      |
| Kirjoita kuvaus sisällissodasta. Anna keskeiset päivämäärät ja tapahtumat ja kuvaa niiden merkitys                                                                                                                                     | _palautti kappaleen, jota seurasi luettelo keskeisistä tapahtumapäivämääristä ja kuvauksista_                               | Monimutkainen       |
| Kirjoita kuvaus sisällissodasta yhdessä kappaleessa. Tarjoa 3 kohdalistan kohtaa, joissa on tärkeät päivämäärät ja niiden merkitys. Tarjoa 3 kohdalistan kohtaa, joissa keskeiset historialliset hahmot ja heidän panoksensa. Palauta tulos JSON-tiedostona | _palauttaa laajemmat tiedot tekstiruudussa, muotoiltuna JSONina, jonka voit kopioida tiedostoon ja validoida tarvittaessa_    | Monimutkainen. Muotoiltu. |

## Pääkohde

Yllä olevissa esimerkeissä kehotteet olivat vielä melko avoimia, jolloin LLM sai päättää, mikä osa sen esikoulutetusta aineistosta oli relevanttia. _Pääkohteen_ suunnittelumallissa syöteteksti jaetaan kahteen osaan:

- ohje (toiminto)
- relevantti sisältö (joka vaikuttaa toimintaan)

Tässä esimerkissä ohjeena on "tiivistä tämä kahteen lauseeseen".

| Kehote (Syöte)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Täydennys (Vastaus)                                                                                                                                                                                                                                                                              |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter on Aurinkoa lähinnä viidentenä planeettana ja aurinkokuntamme suurin planeetta. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksin ja puolin suurempi kuin kaikkien muiden aurinkokunnan planeettojen yhteismassa. Jupiter on yksi kirkkaimmista paljain silmin näkyvistä kohteista yötaivaalla, ja muinaiset sivilisaatiot ovat tunteneet sen ennen kirjallista historiaa. Se on nimetty roomalaisen Jumala Jupiterin mukaan.[19] Kun sitä katsotaan Maan suunnalta, Jupiter voi olla riittävän kirkas heijastamaan näkyviä varjoja,[20] ja on keskimäärin kolmanneksi kirkkain luonnollinen kohde yötaivaalla Kuun ja Venuksen jälkeen. <br/> **Tiivistä tämä kahteen lyhyeen lauseeseen** | Jupiter, Aurinkoa lähinnä viidentenä planeettana, on aurinkokuntamme suurin planeetta ja yksi kirkkaimmista yötaivaan kohteista. Nimetty roomalaisen jumalan Jupiterin mukaan, se on kaasujättiläinen, jonka massa on kaksin ja puolin suurempi kuin kaikkien muiden aurinkokunnan planeettojen yhteensä. |

Pääkohdeosaa voidaan käyttää monin tavoin tehokkaamman ohjauksen aikaansaamiseksi:

- **Esimerkit** – sen sijaan, että kertoisimme mallille suoran ohjeen, annamme sille esimerkkejä siitä, mitä tehdä, ja sallimme mallin päätellä kuvion.
- **Vihjeet** – ohjeen jälkeen annetaan "vihje", joka valmistaa täydennystä ohjaten mallia kohti relevantimpia vastauksia.
- **Mallipohjat** – nämä ovat toistettavia 'reseptejä' kehotteille, joissa on paikkamerkkejä (muuttujia), joita voidaan räätälöidä datalla erityistapauksia varten.

Tutkitaan näitä käytännössä.

### Esimerkkien käyttäminen

Tämä lähestymistapa käyttää pääkohdetta "ruokkien malli" esimerkeillä halutusta tuloksesta annetulle ohjeelle ja antaa mallin päätellä kuvion halutusta tuloksesta. Esimerkkien lukumäärän perusteella voimme käyttää nollalaukauksen, yksilaukauksen, muutaman laukauksen yms. kehotteita.

Kehote koostuu nyt kolmesta osasta:

- tehtävän kuvaus
- muutama esimerkki halutusta tuloksesta
- uuden esimerkin alku (josta tulee epäsuora tehtävän kuvaus)

| Oppimistyyppi | Kehote (Syöte)                                                                                                                                        | Täydennys (Vastaus)       |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------ |
| Nollalaukaus  | "The Sun is Shining". Käännä espanjaksi                                                                                                             | "El Sol está brillando".  |
| Yksilaukaus   | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                               | "Es un día frío y ventoso". |
| Muutaman laukaus | Pelaaja juoksi pesille => Pesäpallo <br/> Pelaaja sai ässän => Tennis <br/> Pelaaja sai kuutosen => Kriketti <br/> Pelaaja teki donkin => Koripallo  | Koripallo                  |
|               |                                                                                                                                                       |                           |

Huomaa, että nollalaukaus-kehotteessa piti antaa suora ohje ("Translate to Spanish"), mutta yksilaukaus-esimerkissä se pääteltiin. Muutaman laukauksen esimerkissä nähdään, että useamman esimerkin lisääminen antaa malleille tarkemman päättelyn ilman lisäohjeita.

### Kehotevihjeet

Toinen tapa käyttää pääkohdetta on antaa _vihjeitä_ esimerkkien sijaan. Tässä annamme mallille pienen sysäyksen oikeaan suuntaan aloittamalla tekstinpätkällä, joka kuvastaa haluttua vastausmuotoa. Malli "ottaa vihjeen" ja jatkaa samalla tavalla.

| Vihjeiden määrä | Kehote (Syöte)                                                                                                                                                                                                                                                                                                                                                                                                                   | Täydennys (Vastaus)                                                                                                                                                                                                                                                                         |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0                | Jupiter on Aurinkoa lähinnä viidentenä planeettana ja aurinkokuntamme suurin planeetta. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksin ja puolin suurempi kuin kaikkien muiden aurinkokunnan planeettojen yhteismassa. Jupiter on yksi kirkkaimmista paljain silmin näkyvistä kohteista yötaivaalla, ja muinaiset sivilisaatiot ovat tunteneet sen ennen kirjallista historiaa. <br/>**Tiivistä tämä**                                       | Jupiter on suurin planeetta aurinkokunnassamme ja Aurinkoa lähimpänä viidentenä planeettana. Se on kaasujättiläinen, jonka massa on 1/1000 osa Auringosta, mutta se on painavampi kuin kaikki muut planeetat yhteensä. Muinaiset sivilisaatiot ovat tunteneet Jupiterin kauan, ja se on helposti nähtävissä yötaivaalla. |
| 1              | Jupiter on Aurinkoa lähinnä oleva viides planeetta ja aurinkokunnan suurin. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksikymmentäviisi kertaa kaikkien muiden aurinkokunnan planeettojen massojen summa. Jupiter on yksi kirkkaimmista paljain silmin nähtävistä esineistä yötaivaalla, ja sitä on tunnettu muinaisista sivilisaatioista ennen kirjoitettua historiaa. <br/>**Tiivistä tämä** <br/> Opimme, että Jupiter | on Aurinkoa lähinnä oleva viides planeetta ja aurinkokunnan suurin. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksikymmentäviisi kertaa kaikkien muiden planeettojen yhteenlaskettu massa. Se on helposti nähtävissä paljain silmin ja sitä on tunnettu muinaisista ajoista lähtien.                        |
| 2              | Jupiter on Aurinkoa lähinnä oleva viides planeetta ja aurinkokunnan suurin. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksikymmentäviisi kertaa kaikkien muiden aurinkokunnan planeettojen massojen summa. Jupiter on yksi kirkkaimmista paljain silmin nähtävistä esineistä yötaivaalla, ja sitä on tunnettu muinaisista sivilisaatioista ennen kirjoitettua historiaa. <br/>**Tiivistä tämä** <br/> Kolme tärkeintä oppimaamme faktaa:         | 1. Jupiter on Aurinkoa lähinnä oleva viides planeetta ja aurinkokunnan suurin. <br/> 2. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta...<br/> 3. Jupiter on ollut nähtävissä paljain silmin muinaisista ajoista lähtien ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Kehote-mallit

Kehote-malli on _ennaltamääritelty kaava kehotteelle_, jonka voi tallentaa ja käyttää uudelleen tarpeen mukaan, jotta käyttäjäkokemukset olisivat johdonmukaisempia laajassa mittakaavassa. Yksinkertaisimmillaan se on pelkkä kehotteen esimerkkien kokoelma, kuten [tämä OpenAI:n esimerkki](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), joka tarjoaa sekä interaktiiviset kehotteen osat (käyttäjä- ja järjestelmäviestit) että API-pohjaisen pyyntötavan - tukeakseen uudelleenkäyttöä.

Monimutkaisemmassa muodossa, kuten [tämä esimerkki LangChainilta](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), se sisältää _paikkamerkkejä_, jotka voidaan korvata tiedoilla monista lähteistä (käyttäjän syötteet, järjestelmän konteksti, ulkoiset tietolähteet jne.), jotta kehote voidaan generoida dynaamisesti. Tämä mahdollistaa uudelleenkäytettävien kehotteiden kirjaston luomisen, joita voidaan ohjelmallisesti käyttää johdonmukaisten käyttäjäkokemusten toteuttamiseksi mittakaavassa.

Lopuksi, mallien todellinen arvo piilee kyvyssä luoda ja julkaista _kehote-kirjastoja_ vertikaalisille sovellusaloille - joissa kehotemalli on optimoitu heijastamaan sovelluskohtaisia konteksteja tai esimerkkejä, jotka tekevät vastauksista merkityksellisempiä ja tarkempia kohderyhmälle. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) -arkisto on erinomainen esimerkki tästä lähestymistavasta; se kokoaa kirjastoja kehote-esimerkkejä opetusalalle painottaen tärkeitä tavoitteita kuten tuntisuunnitelmat, opetussuunnitelman suunnittelu, opiskelijaohjaus jne.

## Tukisisältö

Jos ajatellaan kehotteen rakennusta niin, että siinä on ohje (tehtävä) ja kohde (pääsisältö), niin _toissijainen sisältö_ on ikään kuin lisäkonteksti, jota annamme **vaikuttaaksemme tulokseen jollain tavalla**. Tämä voi olla viritysparametreja, muotoiluohjeita, aiheiden taksonomioita jne., jotka auttavat mallia _räätälöimään_ vastauksensa toivottuihin käyttäjätavoitteisiin tai odotuksiin.

Esimerkiksi: Jos tarjolla on kurssiluettelo laajalla metatiedolla (nimi, kuvaus, taso, metatunnisteet, opettaja jne.) kaikista opetussuunnitelman kursseista:

- voimme antaa ohjeen "tiivistä syksyn 2023 kurssiluettelo"
- voimme käyttää pääsisältönä muutamia esimerkkejä halutusta lopputuloksesta
- voimme käyttää toissijaista sisältöä valitsemaan viisi kiinnostavinta "tunnistetta".

Nyt malli voi antaa yhteenvedon esimerkkien mukaisessa formaatissa - mutta jos tuloksessa on useita tunnisteita, se voi priorisoida toissijaisessa sisällössä määritellyt viisi tunnistetta.

---

<!--
LESSON TEMPLATE:
Tämä yksikkö kattaa ydinideaa #1.
Vahvista käsitettä esimerkkien ja viitteiden avulla.

KONSEPTI #3:
Kehoteinsinöörin tekniikat.
Mitkä ovat kehotetekniikoiden perustekniikat?
Hahmottele ne harjoitusten avulla.
-->

## Kehoteinsinöörin parhaat käytännöt

Nyt kun tiedämme, miten kehotteet voidaan _rakentaa_, voimme alkaa pohtia, miten niitä _suunnitellaan_ niin, että ne heijastavat parhaita käytäntöjä. Voimme ajatella tätä kahdessa osassa – oikeanlaisen _ajattelutavan_ omaksumisessa ja oikeiden _tekniikoiden_ soveltamisessa.

### Kehoteinsinöörin ajattelutapa

Kehoteinsinööriys on kokeilu- ja erehdysprosessi, joten pidä mielessä kolme yleistä ohjenuoraa:

1. **Toimialan ymmärrys on tärkeää.** Vastauksen tarkkuus ja merkityksellisyys riippuu _toimialasta_, jossa sovellus tai käyttäjä toimii. Käytä intuitiotasi ja toimialan asiantuntemustasi \*\*muokataksesi tekniikoita\*\* edelleen. Määrittele esim. _toimialakohtaiset persoonallisuudet_ järjestelmäkehotteissa tai käytä _toimialakohtaisia malleja_ käyttäjäkehotteissa. Tarjoa toissijaista sisältöä, joka heijastaa toimialakohtaisia konteksteja, tai käytä _toimialakohtaisia vihjeitä ja esimerkkejä_ ohjaamaan mallia tuttuun käyttöön.

2. **Mallin ymmärrys on tärkeää.** Mallit ovat luonteeltaan stokastisia. Mallien toteutuksissa voi myös olla eroja käyttämien koulutusdatakokoelmien (ennakkoon opetettu tieto), tarjottujen ominaisuuksien (API tai SDK) ja optimoidun sisältötyypin (esim. koodi vs. kuvat vs. teksti) suhteen. Tunne käyttämäsi mallin vahvuudet ja rajoitukset, ja käytä tätä tietoa _tehtävien priorisointiin_ tai _räätälöityjen mallien rakentamiseen_, jotka ovat optimoitu mallin ominaisuuksille.

3. **Iterointi ja validointi on tärkeää.** Mallit kehittyvät nopeasti, samoin kehotetekniikat. Toimialan asiantuntijana sinulla saattaa olla muita konteksteja tai kriteerejä _omalle_ sovelluksellesi, joita laajempi yhteisö ei käytä. Käytä kehotetekniikoita ja työkaluja nopean aloituksen saamiseksi, sitten iteroi ja validoi tuloksia omalla intuitiolla ja asiantuntemuksella. Tallenna havainnot ja luo **tietopohja** (esim. kehotekirjastoja), jota muut voivat hyödyntää nopeampiin iterointeihin tulevaisuudessa.

## Parhaat käytännöt

Seuraavaksi katsomme yleisiä parhaita käytäntöjä, joita suosittelevat [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ja [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) asiantuntijat.

| Mitä                              | Miksi                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Arvioi viimeisimmät mallit.       | Uudet mallin sukupolvet sisältävät todennäköisesti parannettuja ominaisuuksia ja laatua – mutta voivat myös olla kalliimpia. Arvioi vaikutuksia ja tee päätökset siirtymisestä sen mukaan.                                                                                        |
| Erottele ohjeet ja konteksti      | Tarkista, onko mallillasi/palveluntarjoajallasi _rajoittimia_, joilla ohjeet, pääsisältö ja toissijainen sisältö erotellaan selkeämmin. Tämä auttaa mallia määrittämään tokenien painotuksia tarkemmin.                                                                        |
| Ole tarkka ja selkeä              | Anna enemmän tietoa halutusta kontekstista, lopputuloksesta, pituudesta, formaatista, tyylistä jne. Tämä parantaa sekä laatua että yhdenmukaisuutta vastauksissa. Tallenna mallit uudelleenkäytettäviksi kaavoiksi.                                                         |
| Ole kuvaileva, käytä esimerkkejä  | Mallit voivat reagoida paremmin "näytä ja kerro" -lähestymistapaan. Aloita `zero-shot`-menetelmällä, jossa annat ohjeen (mutta et esimerkkejä), sitten kokeile `few-shot`-menetelmää täsmennyksenä, tarjoamalla muutama esimerkki halutusta tuloksesta. Käytä analogioita.               |
| Käytä vihjeitä vastausten aloitukseen | Ohjaa malli haluttuun lopputulokseen antamalla joitakin johdattavia sanoja tai lauseita, joita se voi käyttää lähtökohtana vastaukselle.                                                                                                                    |
| Toista tarvittaessa               | Joskus voi olla tarpeen toistaa ohjeita mallille. Anna ohjeet ennen ja jälkeen pääsisällön, käytä ohjetta ja vihjettä jne. Iteroi ja validoi, mikä toimii parhaiten.                                                                                          |
| Järjestys merkitsee               | Tiedon esittämisjärjestys mallille voi vaikuttaa tulokseen, jopa oppimisesimerkeissä, laatuvinouman vuoksi. Kokeile eri vaihtoehtoja nähdäksesi, mikä toimii parhaiten.                                                                                        |
| Anna mallille "uloskäynti"        | Tarjoa mallille _varalla oleva_ vastaus, jonka se voi antaa, jos tehtävää ei pysty suorittamaan syystä tai toisesta. Tämä vähentää vääriä tai tekaistuja vastauksia.                                                                                              |
|                                  |                                                                                                                                                                                                                                                   |

Kuten missä tahansa parhaassa käytännössä, muista, että _kokemuksesi voi vaihdella_ mallin, tehtävän ja toimialan mukaan. Käytä näitä lähtökohtana ja iteroi, kunnes löydät sinulle parhaiten sopivat tavat. Arvioi jatkuvasti uudelleen kehotetekniikkasi prosessia uusien mallien ja työkalujen myötä, keskittyen prosessin skaalautuvuuteen ja vastausten laatuun.

<!--
LESSON TEMPLATE:
Tässä yksikössä tulisi olla koodiharjoitus, jos sovellettavissa

HAASTE:
Linkki Jupyter-muistikirjaan, jossa vain koodikommentit ohjeina (koodiosat tyhjiä).

RATKAISU:
Linkki kopioon kyseisestä muistikirjasta, jossa kehotteet on täytetty ja ajetaan esimerkin näyttämiseksi.
-->

## Tehtävä

Onneksi olkoon! Pääsit oppitunnin loppuun! Nyt on aika testata joitakin näistä käsitteistä ja tekniikoista oikeilla esimerkeillä!

Tehtävässämme käytämme Jupyter-muistikirjaa, johon voit tehdä harjoituksia vuorovaikutteisesti. Voit myös laajentaa muistikirjaa omilla Markdown- ja Koodisoluillasi tutkiaksesi ideoita ja tekniikoita itsenäisesti.

### Aloittaaksesi, tee fork repoista, sitten

- (Suositeltu) Käynnistä GitHub Codespaces
- (Vaihtoehto) Kloonaa repo paikalliselle laitteellesi ja käytä sitä Docker Desktopin kanssa
- (Vaihtoehto) Avaa muistikirja suosimallasi Jupyter-ympäristöllä.

### Seuraavaksi määritä ympäristömuuttujat

- Kopioi juurihakemistosta `.env.copy` tiedosto `.env`:ksi ja täytä arvot `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ja `AZURE_OPENAI_DEPLOYMENT`. Palaa kohtaan [Learning Sandbox](#oppimishiekkalaatikko) oppiaksesi miten.

### Avaa sitten Jupyter-muistikirja

- Valitse suoritusympäristön (kernelin) asetus. Jos käytät vaihtoehtoja 1 tai 2, valitse kehityssäilön oletus Python 3.10.x -kernel.

Olet valmis ajamaan harjoitukset. Huomaa, ettei tässä ole _oikeita tai vääriä_ vastauksia – kyse on kokeilusta ja intuitiosta siitä, mikä toimii kullekin mallille ja sovellusalueelle.

_Tämän takia tässä oppitunnissa ei ole tarjolla valmiita koodiratkaisuja. Muistikirjassa on kuitenkin Markdown-soluja otsikolla "Oma ratkaisu:", joissa nähdään yksi esimerkkilähtö tuloksesta._

 <!--
LESSON TEMPLATE:
Tiivistä osio ja tarjoa itseopiskeluresursseja.
-->

## Tietämystesti

Mikä seuraavista on hyvä kehotelause, joka noudattaa kohtuullisia parhaita käytäntöjä?

1. Näytä minulle kuva punaisesta autosta
2. Näytä minulle kuva punaisesta autosta, merkiltään Volvo ja malliltaan XC90, joka on parkissa kallion reunalla auringonlaskun aikaan
3. Näytä minulle kuva punaisesta autosta, merkiltään Volvo ja malliltaan XC90

V: 2, se on paras kehotelause, koska se antaa tietoja "mitä" ja menee yksityiskohtiin (ei vain mikä tahansa auto, vaan tietty merkki ja malli) ja se kuvaa myös ympäristöä. Kohta 3 on seuraavaksi paras, sillä siinä on paljon kuvausta.

## 🚀 Haaste

Kokeile hyödyntää "vihje" -tekniikkaa kehotteella: Täydennä lause "Näytä minulle kuva punaisesta autosta, merkiltään Volvo ja ". Miten malli vastaa, ja miten parantaisit sitä?

## Hienoa työtä! Jatka oppimistasi

Haluatko oppia lisää eri Kehoteinsinöörin käsiteistä? Siirry [jatko-opintojen sivulle](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), josta löydät muita upeita resursseja tästä aiheesta.

Siirry oppitunnille 5, jossa käsittelemme [edistyneitä kehotetekniikoita](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->