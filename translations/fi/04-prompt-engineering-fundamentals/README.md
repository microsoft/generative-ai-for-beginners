# Promptin suunnittelun perusteet

[![Promptin suunnittelun perusteet](../../../translated_images/fi/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Johdanto
Tämä moduuli kattaa olennaiset käsitteet ja tekniikat tehokkaiden kehotteiden luomiseksi generatiivisille tekoälymalleille. Tapa, jolla kirjoitat kehotteen LLM:lle, on myös tärkeä. Huolellisesti laadittu kehotte voi saavuttaa paremman vastauksen laadun. Mutta mitä tarkalleen ottaen termit _prompt_ ja _prompt engineering_ tarkoittavat? Ja miten voin parantaa kehotteen _syötettä_, jonka lähetän LLM:lle? Näihin kysymyksiin yritämme vastata tässä ja seuraavassa luvussa.

_Generatiivinen tekoäly_ kykenee luomaan uutta sisältöä (esim. tekstiä, kuvia, ääntä, koodia jne.) käyttäjän pyynnön perusteella. Se saavuttaa tämän käyttämällä _suuria kielimalleja_ kuten OpenAI:n GPT ("Generative Pre-trained Transformer") -sarjaa, jotka on koulutettu käsittelemään luonnollista kieltä ja koodia.

Käyttäjät voivat nyt olla vuorovaikutuksessa näiden mallien kanssa tutuilla paradigmoilla kuten keskustelu, ilman teknistä asiantuntemusta tai koulutusta. Mallit ovat _kehotteisiin perustuvia_ - käyttäjät lähettävät tekstisyötteen (kehotteen) ja saavat vastauksena tekoälyn tuottaman lopputuloksen (completion). He voivat sitten "keskustella tekoälyn kanssa" iteratiivisesti, monikertaisissa vuorovaikutuksissa, hienosäätäen kehotettaan, kunnes vastaus vastaa odotuksia.

"Kehotteista" tulee nyt generatiivisten tekoälysovellusten ensisijainen _ohjelmointirajapinta_, joka kertoo malleille, mitä tehdä, ja vaikuttaa palautettujen vastausten laatuun. "Prompt engineering" on nopeasti kasvava tutkimusala, joka keskittyy _kehotteiden suunnitteluun ja optimointiin_ tuottaakseen johdonmukaisia ja laadukkaita vastauksia laajassa mittakaavassa.

## Oppimistavoitteet

Tässä oppitunnissa opimme, mitä prompt engineering on, miksi se on tärkeää ja miten voimme laadukkaasti laatia kehotteita tietylle mallille ja sovelluksen tavoitteelle. Ymmärrämme ydinkäsitteet ja parhaat käytännöt promptin suunnittelussa - sekä tutustumme interaktiiviseen Jupyter Notebooksin "hiekkalaatikko"-ympäristöön, jossa voimme nähdä näitä käsitteitä käytännössä.

Oppitunnin lopussa osaamme:

1. Selittää, mitä prompt engineering on ja miksi se on tärkeää.
2. Kuvata kehotteen osat ja niiden käyttötavat.
3. Oppia parhaat käytännöt ja tekniikat promptin suunnitteluun.
4. Soveltaa opittuja tekniikoita käytännön esimerkkeihin OpenAI-päätepisteen avulla.

## Keskeiset termit

Prompt engineering: Käytännössä tarkoittaa syötteiden suunnittelua ja hiomista, jotta tekoälymallit tuottaisivat haluttuja lopputuloksia.
Tokenisointi: Prosessi, jossa teksti muunnetaan pienemmiksi yksiköiksi, nimeltään tokeneiksi, jotka malli ymmärtää ja käsittelee.
Ohjeistettu LLM: Suuret kielimallit, joita on hienosäädetty erityisillä ohjeistuksilla parantamaan vastausten tarkkuutta ja merkityksellisyyttä.

## Oppimishiekkalaatikko

Prompt engineering on tällä hetkellä enemmänkin taidetta kuin tiedettä. Paras tapa kehittää tuntumaa siihen on _harjoitella lisää_ ja omaksua kokeileva lähestymistapa, joka yhdistää sovellusalueen asiantuntemuksen suositeltuihin tekniikoihin ja mallikohtaisiin optimointeihin.

Tämän oppitunnin mukana tuleva Jupyter Notebook tarjoaa _hiekkalaatikko_-ympäristön, jossa voit kokeilla oppimaasi sitä mukaa tai osana lopun kooditehtävää. Harjoitusten suorittamiseen tarvitset:

1. **Azure OpenAI -API-avaimen** - palvelun päätepisteen käyttöön otetulle LLM:lle.
2. **Pythonin suoritusympäristön** - jossa Notebookia voidaan ajaa.
3. **Paikalliset ympäristömuuttujat** - _suorita [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) -vaiheet nyt valmiiksi_.

Notebookissa on _aloitus_ harjoituksia, mutta sinua kehotetaan lisäämään omia _Markdown_- (kuvaus) ja _Code_-osioita (kehotepyyntöjä) kokeillaksesi lisää esimerkkejä tai ideoita - ja kehittääksesi tuntumaa promptin suunnitteluun.

## Kuvitettu opas

Haluatko saada kokonaiskuvan siitä, mitä oppitunti käsittelee, ennen syventymistä? Tutustu tähän kuvitettuun oppaaseen, joka antaa sinulle kuvan pääaiheista ja keskeisistä oivalluksista, joita pohtia. Oppitunnin tiekartta vie sinut ytimekkäiden käsitteiden ja haasteiden ymmärtämisestä niiden käsittelyyn sopivilla promptin suunnittelutekniikoilla ja parhailla käytännöillä. Huomaa, että tämän oppaan "Edistyneet tekniikat" -osio viittaa ensi luvussa käsiteltävään sisältöön.

![Kuvitettu opas promptin suunnitteluun](../../../translated_images/fi/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Startupimme

Nyt puhutaan, miten _tämä aihe_ liittyy startupimme tehtävään [tuoda tekoälyinnovaatioita koulutukseen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Haluamme rakentaa tekoälypohjaisia sovelluksia _personoidulle oppimiselle_ - joten mietitään, miten eri käyttäjäryhmät sovelluksessamme voisivat "suunnitella" kehotteita:

- **Ylläpitäjät** saattavat pyytää tekoälyä _analysoimaan opetussuunnitelman tietoja löytääkseen aukkoja sisällöstä_. Tekoäly voi tiivistää tuloksia tai visualisoida ne koodilla.
- **Opettajat** voivat pyytää tekoälyä _luomaan opetussuunnitelman kohdeyleisölle ja aiheelle_. Tekoäly voi rakentaa henkilökohtaisen suunnitelman määritellyssä muodossa.
- **Oppilaat** voivat pyytää tekoälyä _ohjaamaan vaikeassa oppiaineessa_. Tekoäly voi nyt opastaa oppilaita tunteihin, vinkkeihin ja esimerkkeihin heidän tasolleen sopivasti.

Tämä on vasta jäävuoren huippu. Tutustu [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - avoimen lähdekoodin kehotekirjastoon, jonka koulutusasiantuntijat ovat koonneet - saadaksesi laajemman kuvan mahdollisuuksista! _Kokeile ajaa joitain noista kehotteista hiekkalaatikossa tai OpenAI Playgroundissa nähdäksesi, mitä tapahtuu!_

<!--
OPPITUNNIN MALLI:
Tämä yksikkö käsittelee ydinkäsitettä #1.
Vahvista käsitettä esimerkkien ja viitteiden avulla.

KÄSITTEEN #1:
Prompt Engineering.
Määrittele se ja selitä, miksi sitä tarvitaan.
-->

## Mitä prompt engineering on?

Aloitimme tämän oppitunnin määrittelemällä **prompt engineeringin** prosessiksi, jossa _suunnitellaan ja optimoidaan_ tekstisyötteitä (kehotteita) tarjoamaan johdonmukaisia ja laadukkaita vastauksia (lopputuloksia) tietyn sovelluksen tavoitteen ja mallin tarpeisiin. Tätä voidaan ajatella kahden vaiheen prosessina:

- _suunnitellaan_ alkuperäinen kehotte tietylle mallille ja tavoitteelle
- _hiotaan_ kehotetta iteratiivisesti vastauksen laadun parantamiseksi

Tämä vaatii luonnollisesti kokeilu- ja erehdysmenetelmää, joka edellyttää käyttäjän intuitiota ja ponnisteluja optimaalisia tuloksia varten. Miksi se sitten on tärkeää? Vastataksemme, meidän on ensin ymmärrettävä kolme käsitettä:

- _Tokenisointi_ = miten malli "näkee" kehotteen
- _Perus-LLM:t_ = miten perustamalli "käsittelee" kehotteen
- _Ohjeistettu LLM_ = miten malli voi nyt nähdä "tehtävät"

### Tokenisointi

LLM näkee kehotteet _tokenien sarjana_, ja eri mallit (tai malliversiot) voivat tokenisoida saman kehotteen eri tavoin. Koska LLM:ia koulutetaan tokeneilla (ei raakatekstillä), kehotteiden tokenisoinnilla on suora vaikutus tuotetun vastauksen laatuun.

Saadaksesi intuitiota tokenisoinnista, kokeile esimerkiksi [OpenAI Tokenizeria](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), joka on esitetty alla. Kopioi kehotteesi siihen ja katso, miten se muuttuu tokeneiksi, kiinnittäen huomiota välilyöntien ja välimerkkien käsittelyyn. Huomaa, että tämä esimerkki käyttää vanhempaa LLM:ää (GPT-3) - joten uudemmalla mallilla kokeilu saattaa antaa erilaisen tuloksen.

![Tokenisointi](../../../translated_images/fi/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Käsite: Perusmallit

Kun kehotteesta on tehty tokenisointi, ["perus-LLM:n"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (tai Foundation-mallin) ensisijainen tehtävä on ennustaa seuraava token sekvenssissä. Koska LLM:ia on koulutettu valtavilla tekstiaineistoilla, niillä on hyvä käsitys tokenien tilastollisista suhteista ja ne pystyvät tekemään ennusteen varsin luotettavasti. On huomattava, etteivät ne kuitenkaan ymmärrä _sanoman merkitystä_ kehotteessa tai tokenissa; ne vain näkevät mallin, jonka voivat "täydentää" seuraavalla ennusteellaan. Ne voivat jatkaa ennustamista, kunnes käyttäjä lopettaa tai jokin ennalta määritelty ehto täyttyy.

Haluatko nähdä, miten kehotteeseen perustuva täydennys toimii? Syötä yllä oleva kehotte [Microsoft Foundryn leikkikenttään](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) oletusasetuksilla. Järjestelmä on konfiguroitu käsittelemään kehotteet tiedonpyyntöinä, joten sinun pitäisi saada vastaus, joka vastaa tätä kontekstia.

Mutta entä jos käyttäjä haluaa nähdä jotain tiettyä, joka täyttää jonkin kriteerin tai tehtävän tavoitteen? Tällöin kuvaan astuvat _ohjeistuksella hienosäädetyt_ LLM:t.

![Perus-LLM:n keskustelu täydennys](../../../translated_images/fi/04-playground-chat-base.65b76fcfde0caa67.webp)

### Käsite: Ohjeistuksella hienosäädetyt LLM:t

[Ohjeistuksella hienosäädetty LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) alkaa perusmallista ja hienosäätää sitä esimerkkien tai syöte-/tulospareilla (esim. monivuorokeskustelu "viestit"), jotka sisältävät selkeitä ohjeita - ja tekoälyn vastaus yrittää noudattaa näitä ohjeita.

Tätä käytetään tekniikoilla kuten ihmisen palautteella vahvistettu vahvistusoppiminen (RLHF), jonka avulla malli oppii _noudattamaan ohjeita_ ja _oppimaan palautteesta_, jotta se tuottaa vastauksia, jotka soveltuvat paremmin käytännön sovelluksiin ja ovat relevantimpia käyttäjän tavoitteille.

Kokeillaan tätä - palaa yllä olevaan kehotteeseen, mutta vaihda nyt _järjestelmäviesti_ antamaan seuraava ohje kontekstina:

> _Tiivistä sinulle annettu sisältö toisen luokan oppilaalle. Pidä tulos yhdessä kappaleessa, sisältäen 3-5 bullettikohtaa._

Näetkö, kuinka tulos on nyt säädetty vastaamaan toivottua tavoitetta ja muotoa? Opettaja voi nyt käyttää tätä vastausta suoraan luentodiapeissaan.

![Ohjeistuksella hienosäädetyllä LLM:n keskustelu täydennys](../../../translated_images/fi/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Miksi tarvitsemme prompt engineeringin?

Kun tiedämme, miten LLM:t käsittelevät kehotteita, puhutaanpa siitä, miksi prompt engineering on välttämätöntä. Vastaus löytyy siitä, että nykyisillä LLM:illä on useita haasteita, jotka tekevät _luotettavien ja johdonmukaisten vastauksien_ saavuttamisesta vaikeampaa ilman ponnisteluja kehotteiden rakentamisessa ja optimoinnissa. Esimerkiksi:

1. **Mallien vastaukset ovat stokastisia.** _Sama kehotte_ tuottaa todennäköisesti erilaisia vastauksia eri malleilla tai malliversioilla. Se voi jopa tuottaa erilaisia tuloksia _saman mallin_ kanssa eri aikoina. _Prompt engineering -tekniikat voivat auttaa minimoimaan näitä vaihteluita tarjoamalla parempia suojakeinoja_.

1. **Mallien vastaukset voivat olla keksittyjä.** Mallit on esikoulutettu _laajoilla mutta rajallisilla_ aineistoilla, joten niiltä puuttuu tieto aiheen ulkopuolisista käsitteistä. Tämän seurauksena ne voivat tuottaa vastauksia, jotka ovat epätarkkoja, kuviteltuja tai suoraan ristiriitaisia tunnettujen faktojen kanssa. _Prompt engineering -tekniikat auttavat käyttäjiä tunnistamaan ja lieventämään tällaisia keksintöjä, esim. pyytämällä tekoälyltä lähdeviitteitä tai perusteluja_.

1. **Mallien kyvyt vaihtelevat.** Uudemmat mallit tai mallisukupolvet tarjoavat laajempia kykyjä, mutta myös omia omituisuuksiaan ja vaihteluita kustannusten ja monimutkaisuuden suhteen. _Prompt engineering voi auttaa kehittämään parhaita käytäntöjä ja työnkulkuja, jotka abstraktoivat erot ja mukautuvat mallikohtaisiin vaatimuksiin skaalautuvasti ja saumattomasti_.

Katsotaan tätä käytännössä OpenAI:n tai Azure OpenAI Playgroundissa:

- Käytä samaa kehotetta eri LLM-asennuksilla (esim. OpenAI, Azure OpenAI, Hugging Face) - huomasitko vaihteluita?
- Käytä samaa kehotetta useasti _saman_ LLM-asennuksen kanssa (esim. Azure OpenAI Playground) - miten nämä vaihtelut erosivat?

### Keksinnöt esimerkkinä

Tässä kurssissa käytämme termiä **"keksintö"** viitataksemme ilmiöön, jossa LLM:t joskus tuottavat tosiasiallisesti virheellistä tietoa koulutuksensa rajoitusten tai muiden rajoitteiden takia. Saatat olla kuullut tätä kutsuttavan _"hallusinaatioiksi"_ suosituissa artikkeleissa tai tutkimuspapereissa. Suosittelemme kuitenkin vahvasti termiä _"keksintö"_, jotta emme epähuomiossa antropomorfisoisi käyttäytymistä antamalla koneohjatulle lopputulokselle ihmismäisen ominaisuuden. Tämä vahvistaa myös [Vastuullisen tekoälyn ohjeistuksia](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminologian näkökulmasta, poistaen termejä, joita voidaan pitää loukkaavina tai ei-sisältävinä joissakin konteksteissa.

Haluatko saada käsityksen siitä, miten keksinnöt toimivat? Ajattele kehotetta, joka käskee tekoälyä luomaan sisältöä olemattomasta aiheesta (varmistaaksesi, ettei se löydy koulutusdatasta). Esimerkiksi - kokeilin tätä kehotetta:

> **Kehote:** luo opetussuunnitelma marsilaissodasta vuonna 2076.

Verkkohaku näytti, että marsilaissodista on fiktiivisiä kertomuksia (esim. TV-sarjoja tai kirjoja) - mutta ei vuoden 2076 osalta. Terve järki kertoo myös, että vuosi 2076 on _tulevaisuudessa_ eikä siksi voi liittyä todelliseen tapahtumaan.


Mitä tapahtuu, kun ajoit tämän kehotteen eri LLM-palveluntarjoajilla?

> **Vastaus 1**: OpenAI Playground (GPT-35)

![Vastaus 1](../../../translated_images/fi/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Vastaus 2**: Azure OpenAI Playground (GPT-35)

![Vastaus 2](../../../translated_images/fi/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Vastaus 3**: : Hugging Face Chat Playground (LLama-2)

![Vastaus 3](../../../translated_images/fi/04-fabrication-huggingchat.faf82a0a51278956.webp)

Kuten odotettua, kukin malli (tai malliversio) tuottaa hieman erilaisia vastauksia satunnaisen käyttäytymisen ja mallin kykyerojen vuoksi. Esimerkiksi yksi malli on kohdistettu 8. luokan yleisölle, kun taas toinen olettaa lukio-opiskelijan. Kaikki kolme mallia kuitenkin loivat vastauksia, jotka voisivat vakuuttaa tiedottoman käyttäjän tapahtuman todeksi.

Kehoteoptimointitekniikat kuten _metakehotteet_ ja _lämpötilakonfiguraatio_ voivat jonkin verran vähentää mallien keksintöjä. Uudet kehoteoptimoinnin _arkkitehtuurit_ myös sulauttavat saumattomasti uusia työkaluja ja tekniikoita kehotevirtaan näiden vaikutusten lieventämiseksi tai vähentämiseksi.

## Tapaustutkimus: GitHub Copilot

Päätetään tämä osio katsomalla, miten kehoteoptimointia käytetään todellisissa ratkaisuissa yhden tapaustutkimuksen avulla: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot on "AI-koodipari" - se muuntaa tekstikehotteet koodin täydentämisiksi ja on integroitu kehitysympäristöösi (esim. Visual Studio Code) saumattoman käyttökokemuksen tarjoamiseksi. Alla dokumentoiduissa blogisarjoissa varhaisin versio perustui OpenAI Codex -malliin – ja insinöörit huomasivat nopeasti, että mallia täytyy hienosäätää ja kehittää parempia kehoteoptimointitekniikoita koodin laadun parantamiseksi. Heinäkuussa he [esittelivät parannetun AI-mallin, joka menee Codexin ohi](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) entistä nopeampien ehdotusten aikaansaamiseksi.

Lue postaukset järjestyksessä seuraten heidän oppimismatkaansa.

- **Toukokuu 2023** | [GitHub Copilot ymmärtää koodiasi entistä paremmin](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Toukokuu 2023** | [Sisältä GitHub: Työskentely GitHub Copilotin taustalla olevien LLM:ien kanssa](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Kesäkuu 2023** | [Kuinka kirjoittaa parempia kehoteita GitHub Copilotille](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Heinäkuu 2023** | [.. GitHub Copilot menee Codexin ohi parannetulla AI-mallilla](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Heinäkuu 2023** | [Kehittäjän opas kehoteoptimointiin ja LLM:iin](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Syyskuu 2023** | [Kuinka rakentaa yritystason LLM-sovellus: Oppeja GitHub Copilotilta](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Voit myös selata heidän [Insinööriblogiaan](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) löytääksesi lisää postauksia kuten [tämän](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), joka näyttää kuinka näitä malleja ja tekniikoita _sovelletaan_ todellisten sovellusten tukemiseen.

---

<!--
OPPITUNTIPOHJA:
Tämä yksikkö käsittelee ydinkonseptia #2.
Vahvista käsitystä esimerkkien ja viitteiden avulla.

KONSEPTI #2:
Kehotteen suunnittelu.
Selitetty esimerkkien avulla.
-->

## Kehotteen rakentaminen

Olemme nähneet, miksi kehoteoptimointi on tärkeää – nyt ymmärretään, miten kehotteet _rakennetaan_, jotta voimme arvioida eri tekniikoita tehokkaamman kehotteen suunnitteluun.

### Peruskehote

Aloitetaan peruskehotteella: tekstisyöte lähetetään mallille ilman muuta kontekstia. Tässä esimerkki – kun lähetämme Yhdysvaltojen kansallislaulun ensimmäiset sanat OpenAI:n [Completion API:lle](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), se heti _täydentää_ vastauksen seuraavilla riveillä, mikä kuvastaa perusennusteen toimintaa.

| Kehote (Syöte)     | Täydennys (Tuloste)                                                                                                                      |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Näyttää siltä, että alat laulaa "The Star-Spangled Banner" -kansallislaulua Yhdysvalloille. Koko laulun sanat ovat ...                   |

### Monimutkainen kehote

Lisätään nyt konteksti ja ohjeet tuohon peruskehotteeseen. [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) antaa rakentaa monimutkaisen kehotejoukon _viesteistä_:

- Syöte/vastaus-parit, jotka heijastavat _käyttäjän_ syötettä ja _avustajan_ vastausta.
- Järjestelmäviesti, joka asettaa kontekstin avustajan käyttäytymiselle tai persoonalle.

Pyyntö on nyt seuraavanlainen, jossa _tokenisointi_ kaappaa tehokkaasti olennaisen tiedon kontekstista ja keskustelusta. Järjestelmäkontekstin vaihtaminen voi vaikuttaa täydennysten laatuun yhtä paljon kuin annettu käyttäjän syöte.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Ohjekehote

Yllä olevissa esimerkeissä käyttäjän kehote oli yksinkertainen tekstikysely, joka voidaan tulkita tiedonpyynnöksi. _Ohjekehotteilla_ voimme käyttää tekstiä määrittämään tehtävän tarkemmin, antaen paremman ohjauksen tekoälylle. Tässä esimerkki:

| Kehote (Syöte)                                                                                                                                                                                                                      | Täydennys (Tuloste)                                                                                                   | Ohjetyyppi         |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Kirjoita kuvaus sisällissodasta                                                                                                                                                                                                  | _palautti yksinkertaisen kappaleen_                                                                                    | Yksinkertainen      |
| Kirjoita kuvaus sisällissodasta. Esitä avaintapahtumat ja niiden merkitys                                                                                                                                                         | _palautti kappaleen, jota seurasi avaintapahtumien päivämäärien luettelo ja kuvaukset_                                | Monimutkainen       |
| Kirjoita kuvaus sisällissodasta yhdellä kappaleella. Anna 3 luettelokohtaa avaintapahtumien päivämääristä ja niiden merkityksestä. Anna 3 lisää luettelokohtaa keskeisistä historiallisista henkilöistä ja heidän panoksistaan. Palauta tuloste JSON-tiedostona | _palauttaa laajemmat tiedot tekstikentässä JSON-muodossa, jonka voi kopioida tiedostoon ja validoida tarvittaessa_   | Monimutkainen. Muotoiltu. |

## Primäärisisältö

Edellä olevissa esimerkeissä kehote oli edelleen melko avoin, jolloin LLM sai itse päättää, mikä sen esikoulutusaineistosta on relevanttia. _Primäärisisältö_-suunnittelumallissa syötetty teksti jaetaan kahteen osaan:

- ohjeeseen (toimintaan)
- relevanttiin sisältöön (joka vaikuttaa toimintaan)

Tässä esimerkissä ohjeena on "tiivistä tämä kahteen lauseeseen".

| Kehote (Syöte)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Täydennys (Tuloste)                                                                                                                                                                                                                                                                    |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter on aurinkoa lähimpänä viidenneksi oleva planeetta ja suurin aurinkokunnassa. Se on kaasuplaneetta, jonka massa on tuhannesosa auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden planeettojen yhdessä. Jupiter on yksi kirkkaimmista paljain silmin näkyvistä taivaankappaleista ja se tunnetaan muinaisista sivilisaatioista ennen kirjoitettua historiaa. Se on nimetty roomalaisen jumalan Jupiterin mukaan.[19] Maasta katsottuna Jupiter voi olla tarpeeksi kirkas heijastamaan näkyviä varjoja,[20] ja se on keskimäärin kolmanneksi kirkkaimpia luonnollisia kohteita yötaivaalla kuun ja Venuksen jälkeen. <br/> **Tiivistä tämä kahteen lyhyeen lauseeseen** | Jupiter, aurinkoa lähimpänä viidenneksi oleva planeetta, on aurinkokunnan suurin ja tunnettu yhtenä kirkkaimmista taivaankappaleista. Nimeltään roomalaisen jumalan Jupiterin mukaan, se on kaasuplaneetta, jonka massa on kaksi ja puoli kertaa kaikkien muiden planeettojen yhteismassa. |

Primäärisisältöä voidaan käyttää eri tavoin tehokkaampien ohjeiden aikaansaamiseksi:

- **Esimerkit** - sen sijaan, että kerrot mallille suoraan, mitä tehdä, anna esimerkkejä tekemisestä ja anna mallin päätellä malli.
- **Vihjeet** - seuraa ohjetta "vihjeellä", joka ohjaa mallia kohti relevantimpia vastauksia.
- **Mallipohjat** - toistettavia 'reseptejä' kehotteille paikkamerkkeineen (muuttujat), jotka voi räätälöidä tietyille käyttötarkoituksille.

Tutkitaan näitä käytännössä.

### Esimerkkien käyttäminen

Tässä lähestymistavassa käytetään primäärisisältöä "ruokkimaan mallia" esimerkeillä halutusta tulosteesta annettuun ohjeeseen, ja mallin annetaan päätellä haluttu lopputulos. Esimerkkien lukumäärän mukaan voimme käyttää nollakertaa, yksinkertaista tai muutaman esimerkin kehoteoptimointia.

Kehote koostuu nyt kolmesta osasta:

- Tehtävän kuvauksesta
- Muutamista esimerkeistä halutusta tulosteesta
- Uuden esimerkin alusta (josta tulee implisiittinen tehtävän kuvaus)

| Oppimistyypi | Kehote (Syöte)                                                                                                                                    | Täydennys (Tuloste)         |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------- |
| Nollakerta    | "The Sun is Shining". Käännä espanjaksi                                                                                                           | "El Sol está brillando".    |
| Yksinkertainen | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                              | "Es un día frío y ventoso". |
| Muutama kerta | Pelaaja juoksi pesien välin => Baseball <br/> Pelaaja löi ässän => Tennis <br/> Pelaaja löi kuuden => Cricket <br/> Pelaaja teki donkin =>              | Koripallo                   |
|              |                                                                                                                                                  |                             |

Huomaa, että nollakertakehotteessa piti antaa selkeä ohje ("Käännä espanjaksi"), mutta yksinkertaisessa kehotteessa se päätellään esimerkin perusteella. Useamman esimerkin esimerkkitapa osoittaa, miten mallien päätelmiä voidaan parantaa ilman lisäohjeita.

### Kehotevihjeet

Toinen keino käyttää primäärisisältöä on antaa _vihjeitä_ esimerkkien sijaan. Tässä annamme mallille pienen sysäyksen oikeaan suuntaan _aloittamalla_ katkelmalla, joka heijastaa haluttua vastausmuotoa. Malli "ottaa vihjeen" ja jatkaa samalla tyylillä.

| Vihjeiden määrä | Kehote (Syöte)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Täydennys (Tuloste)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter on aurinkoa lähimpänä viidenneksi oleva planeetta ja suurin aurinkokunnassa. Se on kaasuplaneetta, jonka massa on tuhannesosa auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden planeettojen yhdessä. Jupiter on yksi kirkkaimmista paljain silmin näkyvistä taivaankappaleista ja se tunnetaan muinaisista sivilisaatioista ennen kirjoitettua historiaa. <br/>**Tiivistä tämä**                                               | Jupiter on aurinkokuntamme suurin planeetta ja aurinkoa lähimpänä viidenneksi. Se on kaasuplaneetta, jonka massa on 1/1000 osa auringosta, mutta se on raskaampi kuin kaikki muut planeetat yhteensä. Muinaiset sivilisaatiot ovat tunteneet Jupiterin pitkään, ja se näkyy helposti yötaivaalla. |
| 1              | Jupiter on aurinkoa lähimpänä viidenneksi oleva planeetta ja suurin aurinkokunnassa. Se on kaasuplaneetta, jonka massa on tuhannesosa auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden planeettojen yhdessä. Jupiter on yksi kirkkaimmista paljain silmin näkyvistä taivaankappaleista ja se tunnetaan muinaisista sivilisaatioista ennen kirjoitettua historiaa. <br/>**Tiivistä tämä** <br/> Mikä opin oli, että Jupiter | on aurinkoa lähimpänä viidenneksi oleva planeetta ja suurin aurinkokunnassa. Se on kaasuplaneetta, jonka massa on tuhannesosa auringon massasta, mutta kaksi ja puoli kertaa kaikkien muiden planeettojen massan yhteenlaskettu paino. Se on helposti paljain silmin nähtävissä ja tunnettu antiikin ajoilta lähtien.                        |

| 2              | Jupiter on Aurinkoa viidentenä oleva planeetta ja aurinkokunnan suurin. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta, mutta kaksikymmentäviisi kertaa kaikkien muiden aurinkokunnan planeettojen yhteismassaa suurempi. Jupiter on yksi kirkkaimmista paljain silmin nähtävistä kohteista yöllisellä taivaalla ja sitä on tunnettu antiikin sivilisaatioiden ajoista ennen kirjallista historiaa. <br/>**Tiivistä tämä** <br/> Top 3 oppimaamme faktaa:         | 1. Jupiter on Aurinkoa viidentenä oleva planeetta ja aurinkokunnan suurin. <br/> 2. Se on kaasujättiläinen, jonka massa on tuhannesosa Auringon massasta...<br/> 3. Jupiter on ollut paljain silmin nähtävissä antiikin ajoista lähtien ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Kehotekstit

Kehotemalli on _ennalta määritelty resepti kehotteelle_, jota voidaan tallentaa ja käyttää uudelleen tarpeen mukaan, jotta käyttäjäkokemukset olisivat johdonmukaisempia laajassa mittakaavassa. Yksinkertaisimmillaan se on vain kokoelma kehote-esimerkkejä kuten [tämä OpenAI:n esimerkki](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), joka tarjoaa sekä interaktiiviset kehote-komponentit (käyttäjän ja järjestelmän viestit) että API-kutsun rakenteen – tukemaan uudelleenkäyttöä.

Monimutkaisemmassa muodossa, kuten [tämä LangChainin esimerkki](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), se sisältää _paikkamerkkejä_, jotka voidaan korvata tiedoilla useista eri lähteistä (käyttäjän syöte, järjestelmän konteksti, ulkoiset tietolähteet jne.) luomaan kehotteen dynaamisesti. Tämä mahdollistaa uudelleenkäytettävien kehote-kirjastojen rakentamisen, joita voidaan käyttää **ohjelmallisesti** johdonmukaisten käyttäjäkokemusten aikaansaamiseksi suuressa mittakaavassa.

Lopuksi mallien todellinen arvo on kyvyssä luoda ja julkaista _kehote-kirjastoja_ vertikaalisille sovellusalueille – joissa kehotemalli on _optimoitu_ heijastamaan sovelluskohtaisia konteksteja tai esimerkkejä, jotka tekevät vastauksista merkityksellisempiä ja tarkempia kohdeyleisön kannalta. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) -arkisto on erinomainen esimerkki tästä lähestymistavasta, joka kokoaa kokoelman opetusalalle soveltuvia kehoteita keskittyen tärkeisiin tavoitteisiin kuten opetussuunnitelman suunnitteluun, opetuksen kurikulum-toteutukseen ja opiskelijoiden ohjaukseen.

## Tukeva sisältö

Jos ajattelemme kehotteen rakentamista siten, että sillä on ohjeistus (tehtävä) ja kohde (ensisijainen sisältö), niin _toissijainen sisältö_ on kuin lisäkonteksti, jota annamme **vaikuttamaan tulokseen jollain tavalla**. Se voi olla säätöparametreja, muotoiluohjeita, aiheiden taksonomioita jne., jotka auttavat mallia _räätälöimään_ vastauksensa vastaamaan haluttuja käyttäjätavoitteita tai odotuksia.

Esimerkiksi: Kun käytettävissämme on laaja opintoluettelo monimutkaisilla metatiedoilla (nimi, kuvaus, taso, metatunnisteet, opettaja jne.) kaikista kurssista opetussuunnitelmassa:

- voimme määritellä ohjeistuksen "tiivistä syksyn 2023 opintoluettelo"
- voimme käyttää ensisijaista sisältöä antaaksemme muutamia esimerkkejä halutusta lopputuloksesta
- voimme käyttää toissijaista sisältöä tunnistamaan viisi tärkeintä kiinnostuksen aihetta ("tagia")

Nyt malli voi tuottaa yhteenvedon annettujen esimerkkien mukaiseen muotoon - mutta jos tuloksessa on useita tunnisteita, se voi priorisoida toissijaisessa sisällössä määritellyt viisi tunnistettua tunnistetta.

---

<!--
OPPITUNNIN MALLI:
Tämä yksikkö kattaa ydinidean #1.
Vahvista konseptia esimerkkien ja viitteiden avulla.

KONSEPTI #3:
Kehotteen suunnittelutekniikat.
Mitä ovat perusmenetelmät kehotteen suunnittelussa?
Havainnollista niitä harjoituksilla.
-->

## Kehottamisen parhaat käytännöt

Nyt kun tiedämme, miten kehotteet voidaan _rakentaa_, voimme alkaa pohtia, miten ne voidaan _suunnitella_ heijastamaan parhaita käytäntöjä. Voimme ajatella tätä kahdessa osassa – oikean _asenteen_ omaksumisessa ja oikeiden _tekniikoiden_ soveltamisessa.

### Kehottamisen asenne

Kehottaminen on kokeilu- ja erehdysprosessi, joten pidä mielessä kolme laajaa ohjaavaa tekijää:

1. **Toimialaosaaminen on tärkeää.** Vastauksen tarkkuus ja merkityksellisyys riippuu _toimialasta_, jossa sovellus tai käyttäjä toimii. Käytä intuitiotasi ja toimialaasiantuntemustasi **mukauttaaksesi tekniikoita** paremmin. Esimerkiksi määrittele _toimialakohtaiset persoonallisuudet_ järjestelmän kehotteisiin tai käytä _toimialakohtaisia malleja_ käyttäjäkehotteissa. Tarjoa toissijaista sisältöä, joka heijastaa toimialakohtaisia konteksteja, tai käytä _toimialakohtaisia vihjeitä ja esimerkkejä_ ohjaamaan mallia tutumpiin käyttömalleihin.

2. **Mallin ymmärtäminen on tärkeää.** Tiedämme, että mallit ovat stokastisia luonteeltaan. Mutta mallien toteutukset voivat vaihdella käytetyn koulutusdatan (ennalta opetettu tieto), niiden tarjoamien ominaisuuksien (esim. API tai SDK kautta) ja niiden optimoiman sisältötyypin (koodi vs. kuvat vs. teksti) suhteen. Ymmärrä käyttämäsi mallin vahvuudet ja rajoitukset ja käytä tätä tietoa _priorisoidaksesi tehtäviä_ tai rakentaaksesi _mukautettuja malleja_, jotka on optimoitu mallin kyvykkyyksille.

3. **Iterointi ja validointi on tärkeää.** Mallit kehittyvät nopeasti, samoin kehotustekniikat. Toimiala-asiantuntijana sinulla saattaa olla muita konteksteja tai kriteereitä _sinun_ erityissovelluksellesi, jotka eivät välttämättä koske laajempaa yhteisöä. Käytä kehotteen suunnittelun työkaluja ja menetelmiä "aloittaaksesi" kehotteen rakentamisen, sitten tee iterointi ja validoi tulokset oman intuitiosi ja toimialaosaamisesi perusteella. Tallenna oivalluksesi ja luo **tietopankki** (esim. kehotteiden kirjastot), joita muut voivat käyttää uutena perustana nopeampaan kehitykseen tulevaisuudessa.

## Parhaat käytännöt

Tarkastellaanpa yleisiä parhaita käytäntöjä, joita suosittelevat [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ja [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) asiantuntijat.

| Mikä                              | Miksi                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Arvioi uusimmat mallit.           | Uudet mallisukupolvet todennäköisesti tarjoavat parannettuja ominaisuuksia ja laatua – mutta voivat myös aiheuttaa korkeampia kustannuksia. Arvioi vaikutuksia ja tee sitten siirtymispäätökset.                                                    |
| Erottele ohjeet ja konteksti       | Tarkista, määrittääkö mallisi/palveluntarjoajasi _rajoittimia_ ohjeiden, ensisijaisen ja toissijaisen sisällön selkeämpään erotteluun. Tämä voi auttaa malleja antamaan tarkemman painoarvon tokeneille.                                              |
| Ole täsmällinen ja selkeä          | Anna enemmän yksityiskohtia halutusta kontekstista, lopputuloksesta, pituudesta, muodosta, tyylistä jne. Tämä parantaa sekä vastauksen laatua että johdonmukaisuutta. Tallenna reseptit uudelleenkäytettäviin malleihin.                             |
| Ole kuvaileva, käytä esimerkkejä | Mallit voivat reagoida paremmin "näytä ja kerro" -lähestymistapaan. Aloita `zero-shot`-menetelmällä, jossa annat ohjeen (mutta et esimerkkejä), ja kokeile sitten `few-shot`-lähestymistapaa tarjoamalla muutama esimerkki halutusta tuloksesta. Käytä vertauksia. |
| Käytä vihjeitä käynnistämiseen    | Rohkaise mallia haluttuun lopputulokseen antamalla sille johdantasanat tai fraasit, joita se voi käyttää vastauksen lähtökohtana.                                                                                                                  |
| Korosta                        | Joskus saatat joutua toistamaan itsesi mallille. Anna ohjeet ennen ja jälkeen ensisijaisen sisällön, käytä sekä ohjetta että vihjettä jne. Iteroi ja validoi nähdäksesi, mikä toimii parhaiten.                                                     |
| Järjestyksellä on väliä           | Tiedon esitysjärjestys mallille voi vaikuttaa lopputulokseen, jopa oppimisesimerkeissä, johtuen tuoreuden vinoumasta. Kokeile erilaisia järjestyksiä nähdäksesi, mikä toimii parhaiten.                                                        |
| Anna mallille "uloskäynti"        | Anna mallille _varavaihtoehto_, jonka se voi palauttaa, jos se ei jostain syystä pysty suorittamaan tehtävää. Tämä voi vähentää väärien tai keksittyjen vastausten riskiä.                                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Kuten missä tahansa parhaassa käytännössä, muista, että _kokemuksesi voi vaihdella_ mallista, tehtävästä ja toimialasta riippuen. Käytä näitä lähtökohtina ja iteroi löytääksesi sinulle parhaiten toimivat ratkaisut. Arvioi kehotteen suunnitteluprosessiasi jatkuvasti uusien mallien ja työkalujen tullessa saataville, keskittyen prosessin skaalautuvuuteen ja vastausten laatuun.

<!--
OPPITUNNIN MALLI:
Tämä yksikkö tarjoaa kooditehtävän, jos soveltuu.

TEHTÄVÄ:
Linkki Jupyter-muistikirjaan, jossa ohjeissa on vain koodikommentteja (koodiosiot ovat tyhjiä).

RATKAISU:
Linkki kopioon kyseisestä muistikirjasta, jossa kehotteet on täytetty ja suoritettu, esitellen yhden esimerkin.
-->

## Tehtävä

Onnittelut! Pääsit oppitunnin loppuun! Nyt on aika laittaa osa näistä käsitteistä ja tekniikoista testiin oikeiden esimerkkien avulla!

Tehtävää varten käytämme Jupyter-muistikirjaa, jossa harjoitukset voi suorittaa interaktiivisesti. Voit myös laajentaa muistikirjaa omilla Markdown- ja koodisolillasi tutkiaksesi ideoita ja tekniikoita itse.

### Aloita näin: tee forkki reposta, sitten

- (Suositus) Käynnistä GitHub Codespaces
- (Vaihtoehtoisesti) Kloonaa repo paikalliselle laitteelle ja käytä sitä Docker Desktopin kanssa
- (Vaihtoehtoisesti) Avaa muistikirja mieluisalla muistikirja-ympäristöllä.

### Konfiguroi seuraavaksi ympäristömuuttujat

- Kopioi repossa juurikansiossa oleva `.env.copy` -tiedosto nimellä `.env` ja täytä arvot `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ja `AZURE_OPENAI_DEPLOYMENT`. Palaa sitten [Learning Sandbox -osioon](#oppimishiekkalaatikko) oppiaksesi miten.

### Avaa seuraavaksi Jupyter-muistikirja

- Valitse suoritinydin. Jos käytät vaihtoehtoja 1 tai 2, valitse kehityssäiliön tarjoama oletus Python 3.10.x -ydin.

Olet valmis suorittamaan harjoitukset. Huomaa, että tässä ei ole olemassa _oikeita tai vääriä_ vastauksia – pelkästään vaihtoehtojen kokeilemista ja intuitiotasi siitä, mikä toimii tietyssä mallissa ja sovellusalueessa.

_Tästä syystä tässä oppitunnissa ei ole Koodiratkaisu-osioita. Sen sijaan muistikirjassa on Markdown-soluja otsikolla "Minun ratkaisu:", joissa näytetään yksi esimerkkivastaus vertailuksi._

 <!--
OPPITUNNIN MALLI:
Päätä osio yhteenvedolla ja itsenäisen oppimisen materiaaleilla.
-->

## Tietovisa

Mikä seuraavista on hyvä kehotus kohtuullisten parhaiden käytäntöjen mukaisesti?

1. Näytä minulle kuva punaisesta autosta
2. Näytä minulle kuva punaisesta autosta, merkki Volvo ja malli XC90, parkkeerattuna kallion reunalle auringon laskiessa
3. Näytä minulle kuva punaisesta autosta, merkki Volvo ja malli XC90

Vastaus: 2, se on paras kehotus, koska se antaa tietoa "mitä" ja on tarkka (ei mikä tahansa auto, vaan tietty merkki ja malli) ja kuvaa myös kokonaistilanteen. 3 on seuraavaksi paras, sillä sekin sisältää paljon kuvausta.

## 🚀 Haaste

Kokeile käyttää "vihje"-tekniikkaa kehotteessa: Täydennä lause "Näytä minulle kuva punaisesta autosta, merkki Volvo ja ". Miten malli vastaa, ja miten parantaisit sitä?

## Hienoa työtä! Jatka oppimista

Haluatko oppia lisää erilaisista kehotteen suunnittelun käsitteistä? Mene [jatko-oppimisen sivulle](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) löytääksesi muita erinomaisia lähteitä tästä aiheesta.

Siirry seuraavaksi oppitunnille 5, jossa tarkastelemme [edistyneitä kehotustekniikoita](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->