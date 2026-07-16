# Eri LLM-mallien tutkiminen ja vertailu

[![Eri LLM-mallien tutkiminen ja vertailu](../../../translated_images/fi/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon_

Edellisessä oppitunnissa olemme nähneet, miten Generatiivinen AI muuttaa teknologia-alaa, miten suurten kielimallien (LLM) toiminta tapahtuu ja miten yritys – kuten startupimme – voi soveltaa niitä omiin käyttötapauksiinsa ja kasvaa! Tässä luvussa tarkastelemme eri suurten kielimallien (LLM) tyyppejä vertaillen niiden hyviä ja huonoja puolia.

Seuraava askel startup-yrityksemme matkalla on tutustua nykytilanteeseen LLM-mallien osalta ja ymmärtää, mitkä niistä soveltuvat käyttötapaamme.

## Johdanto

Tässä oppitunnissa käsittelemme:

- Nykyisen kentän eri LLM-tyyppejä.
- Mallien testaamista, iterointia ja vertailua omaan käyttötapaasi Azuren ympäristössä.
- Miten LLM otetaan käyttöön.

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Valita oikean mallin omaan käyttötapaukseesi.
- Ymmärtää, miten testata, kehittää ja parantaa mallin suorituskykyä.
- Tietää, miten yritykset ottavat malleja käyttöön.

## Ymmärrä eri LLM-tyypit

LLM-malleja voidaan luokitella useilla tavoilla arkkitehtuurin, harjoitusdatan ja käyttötarkoituksen perusteella. Näiden erojen ymmärtäminen auttaa startupiamme valitsemaan oikean mallin tiettyyn tilanteeseen sekä ymmärtämään, miten testata, kehittää ja parantaa suorituskykyä.

LLM-malleja on monenlaisia, ja valintasi riippuu siitä, mihin aiot niitä käyttää, millaista dataa sinulla on, paljonko olet valmis maksamaan ja muista tekijöistä.

Riippuen siitä, aiotko käyttää mallia tekstin, äänen, videon, kuvan luomiseen tai muuhun, saatat valita eri mallityypin.

- **Ääni ja puheentunnistus**. Whisper-tyyppiset mallit ovat edelleen hyödyllisiä yleiskäyttöisiä puheentunnistusmalleja, mutta tuotantovaihtoehtoja ovat myös uudemmat puheesta tekstiksi -mallit kuten `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` ja diarisaatioversiot. Arvioi kielivalikoimaa, diarisaatiota, reaaliaikaista tukea, viivettä ja kustannuksia käyttötapaasi varten. Lisätietoja löytyy [OpenAI:n puheesta tekstiksi -dokumentaatiosta](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Kuvageneraattorit**. DALL-E ja Midjourney ovat tunnettuja kuvageneraattoreita, mutta tällä hetkellä OpenAI:n kuvien API:t keskittyvät GPT-kuvamalleihin kuten `gpt-image-2`. Myös Stable Diffusion, Imagen, Flux ja muut malliperheet ovat yleisiä vaihtoehtoja. Vertaa kehotteiden noudattamista, muokkaustukea, tyylin hallintaa, turvallisuusvaatimuksia ja lisensointia. Lisätietoja löytyy [OpenAI-kuvageneroinnin oppaasta](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) ja tämän oppimateriaalin 9. luvusta.

- **Tekstin generointi**. Tekstimallit kattavat laajasti huippumallit, päättelymallit, pienemmät ja vähäviiveiset mallit sekä avoimen painon mallit. Nykyisiä esimerkkejä ovat OpenAI GPT-5.x -mallit, Anthropic Claude 4.x -mallit, Google Gemini 3.x -mallit, Meta Llama 4 -mallit ja Mistral-mallit. Älä tee valintaa pelkän julkaisupäivän tai hinnan perusteella; vertaa tehtävän laatua, viivettä, kontekstin ikkunaa, työkalujen käyttöä, turvallisuuskäyttäytymistä, alueellista saatavuutta ja kokonaiskustannuksia. [Microsoft Foundryn mallikatalogi](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) on hyvä paikka vertailla Azuren saatavilla olevia malleja.

- **Monimodaalisuus**. Monet nykyiset mallit pystyvät käsittelemään muutakin kuin pelkkää tekstiä. Jotkut ottavat vastaan kuvia, ääntä tai videoita; jotkut voivat kutsua työkaluja; ja erikoistuneet mallit voivat luoda kuvia, ääntä tai videoita. Esimerkiksi nykyiset OpenAI-mallit tukevat teksti- ja kuvaa syötteinä, Gemini-mallit voivat tukea tekstiä, koodia, kuvaa, ääntä ja videoita malliversiosta riippuen, ja Llama 4 Scout ja Maverick ovat avoimen painon natiivisti monimodaalisia malleja. Tarkista aina kyseisen mallin sivu tuettujen tulostus- ja syöttemuotojen osalta ennen työnkulun rakentamista.

Mallin valinta tarkoittaa, että saat peruskyvykkyydet, mutta ne eivät välttämättä ole riittäviä. Usein yrityksellä on omaa dataa, josta LLM:lle pitää jollain tavoin kertoa. Tätä varten on muutamia eri lähestymistapoja, joista kerrotaan lisää tulevissa osioissa.

### Perusmallit vs. LLM-mallit

Termi "Foundation Model" (perusmalli) [määriteltiin Stanfordin tutkijoiden toimesta](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst), ja se tarkoittaa tekoälymallia, joka täyttää tiettyjä kriteereitä, kuten:

- **Niitä koulutetaan valvomattomalla tai itsevalvotulla oppimisella**, eli ne koulutetaan ilman merkittyä monimodaalista dataa, eikä niiden koulutus vaadi ihmisen tekemää annotointia tai merkintöjä.
- **Ne ovat erittäin suuria malleja**, jotka perustuvat hyvin syviin neuroverkkoihin ja joita on koulutettu miljardeilla parametreilla.
- **Niiden on tarkoitus toimia perusmallina muille malleille**, eli niitä voidaan käyttää lähtökohtana muiden mallien kehittämiselle hienosäätämällä.

![Perusmallit vs LLM](../../../translated_images/fi/FoundationModel.e4859dbb7a825c94.webp)

Kuvan lähde: [Essential Guide to Foundation Models and Large Language Models | kirjoittanut Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Selkeyttääksemme tätä eroa käytetään historiallista esimerkkiä ChatGPT:stä. Varhaiset ChatGPT-versiot käyttivät GPT-3.5 -perusmallia. OpenAI käytti keskustelukohdistettua dataa ja sovitusmenetelmiä luodakseen hienosäätöversion, joka toimi paremmin keskustelutilanteissa, kuten chateissa. Nykyaikaiset AI-palvelut käyttävät usein useita mallivariaatioita, joten palvelun nimi ja taustalla oleva mallin nimi eivät aina ole sama.

![Perusmalli](../../../translated_images/fi/Multimodal.2c389c6439e0fc51.webp)

Kuvan lähde: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Avoimen painon/avoimen lähdekoodin ja suljetun mallien vertailu

Toinen tapa luokitella LLM-malleja on tarkastella, ovatko ne avoimen painon, avoimen lähdekoodin vai suljettuja malleja.

Avoimen lähdekoodin ja avoimen painon mallit tekevät mallien artefaktit tarkasteltaviksi, ladattaviksi tai muokattaviksi, mutta niiden lisenssit vaihtelevat. Jotkut ovat täysin avoimen lähdekoodin, toiset ovat avoimen painon malleja, joilla on käyttörajoituksia. Ne ovat hyödyllisiä, kun yritys tarvitsee enemmän kontrollia käyttöönotossa, datan sijainnissa, kustannuksissa tai räätälöinnissä. Tiimien tulee kuitenkin tarkistaa lisenssiehdot, käyttökustannukset, ylläpito, turvallisuuspäivitykset ja arviointilaatu ennen tuotantoon viemistä. Esimerkkejä ovat [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), jotkin [Mistral-mallit](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) ja monet mallit, jotka löytyvät [Hugging Facesta](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Suljetut mallit ovat palveluntarjoajien omistuksessa ja isännöimiä. Näitä malleja optimoidaan usein hallittua tuotantokäyttöä varten, ja ne voivat tarjota vahvaa tukea, turvallisuusjärjestelmiä, työkaluintegraatioita ja skaalausta. Asiakkaat eivät kuitenkaan yleensä voi tarkastella tai muokata mallin painoja, ja heidän tulee tarkistaa palveluntarjoajan ehdot yksityisyydestä, säilytyksestä, säädösten noudattamisesta ja hyväksyttävästä käytöstä. Esimerkkejä ovat [OpenAI-mallit](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) ja [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Upotukset vs. kuvageneraatiot vs. teksti- ja koodigeneraatiot

LLM-mallit voidaan myös luokitella sen perusteella, minkälaisia tulosteita ne tuottavat.

Upotukset ovat malleja, jotka pystyvät muuntamaan tekstiä numeeriseen muotoon, nimeltään upotus, joka on tekstisyötteen numeerinen esitys. Upotukset helpottavat koneiden ymmärtämään sanojen tai lauseiden välisiä suhteita, ja niitä voidaan käyttää syötteinä muille malleille, kuten luokittelumalleille tai klusterointimalleille, jotka toimivat paremmin numeerisella datalla. Upotusmalleja käytetään usein siirto-opetuksessa, jossa malli rakennetaan välilliseen tehtävään, josta on runsaasti dataa, ja sitten mallin painoja (upotuksia) käytetään uudelleen muihin tehtäviin. Esimerkki tästä kategoriasta on [OpenAI:n upotusmallit](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Upotus](../../../translated_images/fi/Embedding.c3708fe988ccf760.webp)

Kuvageneraatiomallit ovat malleja, jotka luovat kuvia. Näitä malleja käytetään usein kuvan muokkaukseen, synteesiin ja kääntämiseen. Kuvageneraatiomallit koulutetaan usein suurilla kuva-aineistoilla, kuten [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), ja niitä voidaan käyttää uusien kuvien luomiseen tai olemassa olevien kuvien muokkaamiseen käyttämällä täyte- (inpainting), suuren resoluution ja väritystekniikoita. Esimerkkejä ovat [GPT-kuvamallit](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion -mallit](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) ja Imagen-mallit.

![Kuvagenerointi](../../../translated_images/fi/Image.349c080266a763fd.webp)

Teksti- ja koodigeneraatiomallit ovat malleja, jotka tuottavat tekstiä tai koodia. Näitä malleja käytetään usein tekstin tiivistämiseen, kääntämiseen ja kysymyksiin vastaamiseen. Tekstigeneraatiomallit koulutetaan usein suurilla tekstiaineistoilla, kuten [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), ja niitä voidaan käyttää uuden tekstin luomiseen tai kysymyksiin vastaamiseen. Koodigeneraatiomallit, kuten [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), koulutetaan usein suurilla koodiaineistoilla, kuten GitHubissa, ja niitä voidaan käyttää uuden koodin luomiseen tai olemassa olevan koodin virheiden korjaamiseen.

![Teksti- ja koodigenerointi](../../../translated_images/fi/Text.a8c0cf139e5cc2a0.webp)

### Kooderin ja dekooderin vertailu vs. pelkkä dekooderi

Kun puhumme eri LLM-arkkitehtuurityypeistä, käytetään kuvaannollista esimerkkiä.

Kuvittele, että esimiehesi antoi sinulle tehtäväksi laatia opiskelijoille visailukysymyksiä. Sinulla on kaksi kollegaa; toinen vastaa sisällön luomisesta ja toinen tarkistaa ne.

Sisällöntuottaja on kuin pelkkä dekooderimalli: hän voi katsoa aihetta, nähdä mitä olet jo kirjoittanut, ja jatkaa sisällön tuottamista sen kontekstin pohjalta. He ovat erittäin hyviä kirjoittamaan kiinnostavaa ja informatiivista sisältöä, mutta eivät ole aina paras valinta, kun tehtävänä on vain luokitella, hakea tai koodata tietoa. Esimerkkejä pelkän dekooderin malliperheistä ovat GPT ja Llama-mallit.

Tarkastaja on kuin pelkkä kooderimalli, hän tarkastelee kirjoitettua kurssia ja vastauksia, huomaa niiden välisen yhteyden ja ymmärtää kontekstin, mutta ei ole hyvä tuottamaan sisältöä. Esimerkki pelkästä kooderimallista on BERT.

Kuvittele, että meillä olisi joku, joka voisi sekä luoda että tarkistaa tietokilpailun, tämä on kooderi-dekooderimalli. Esimerkkejä ovat BART ja T5.

### Palvelu vs. malli

Nyt keskustellaan palvelun ja mallin eroista. Palvelu on pilvipalveluntarjoajan tarjoama kokonaisuus, joka on usein yhdistelmä malleja, dataa ja muita komponentteja. Malli on palvelun ydin, ja usein perusmalli kuten LLM.

Palvelut on usein optimoitu tuotantokäyttöön ja ne ovat usein helpompi käyttää käyttöliittymän kautta kuin pelkät mallit. Palvelut eivät kuitenkaan aina ole ilmaisia, ja käyttö voi vaatia tilauksen tai maksun, samalla kun hyödynnetään palvelun omistajan laitteistoa ja resursseja, optimoidaan kustannuksia ja skaalataan helposti. Esimerkki palvelusta on [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), joka tarjoaa maksun käytön mukaan -hintamallin. Azure OpenAI Service tarjoaa myös yritystason tietoturvan ja vastuullisen tekoälykehyksen mallien kyvykkyyksien lisäksi.

Mallit ovat neuroverkkokomponentteja: parametreja, painoja, arkkitehtuuria, tokenizeria ja tukevia asetuksia. Mallin ajaminen paikallisesti tai yksityisessä ympäristössä vaatii soveltuvan laitteiston, palvelu-infrastruktuurin, valvonnan ja joko yhteensopivan avoimen lähdekoodin/avoimen painon lisenssin tai kaupallisen lisenssin. Avoimen painon mallit kuten Llama 4 tai Mistral voivat olla itseisännöityjä, mutta ne vaativat silti laskentatehoa ja operatiivista asiantuntemusta.

## Kuinka testata ja kehittää eri mallien suorituskykyä Azuren ympäristössä


Kun tiimimme on tutkinut nykyiset LLM:t ja tunnistanut joitain hyviä ehdokkaita omiin skenaarioihinsa, seuraava askel on testata niitä heidän datallaan ja työkuormallaan. Tämä on iteratiivinen prosessi, joka tehdään kokeilujen ja mittausten avulla.
Suurin osa malleista, joita mainitsimme aiemmissa kappaleissa (OpenAI-mallit, avoimilla painoilla varustetut mallit kuten Llama 4 ja Mistral sekä Hugging Face -mallit) ovat saatavilla [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst) -palvelussa.

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), aiemmin Azure AI Studio / Azure AI Foundry, on yhtenäinen Azure-alusta AI-sovellusten ja -agenttien rakentamiseen. Se auttaa kehittäjiä hallitsemaan elinkaarta kokeilemisesta ja arvioinnista käyttöönottoon, monitorointiin ja hallintaan. Microsoft Foundryn mallikatalogin avulla käyttäjä voi:

- Löytää mielenkiintoisen perustan mallin katalogista, mukaan lukien Azure:n myymät mallit sekä kumppaneiden ja yhteisön tarjoamat mallit. Käyttäjät voivat suodattaa tehtävän, tarjoajan, lisenssin, käyttöönottooption tai nimen mukaan.

![Model catalog](../../../translated_images/fi/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Tarkastella mallikorttia, joka sisältää yksityiskohtaisen kuvauksen käyttötarkoituksesta ja koulutusdatasta, koodiesimerkkejä sekä arviointituloksia sisäisestä arviointikirjastosta.

![Model card](../../../translated_images/fi/ModelCard.598051692c6e400d.webp)

- Verrata teollisuudessa saatavilla olevien mallien ja aineistojen vertailuarvoja arvioidakseen, mikä malli sopii parhaiten liiketoimintaskenaarioon, [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) -ikkunan avulla.

![Model benchmarks](../../../translated_images/fi/ModelBenchmarks.254cb20fbd06c03a.webp)

- Hienosäätää tuettuja malleja omalla koulutusdatallasi parantaaksesi mallin suorituskykyä tietyssä työkuormassa hyödyntäen Microsoft Foundryn kokeilu- ja seurantatyökaluja.

![Model fine-tuning](../../../translated_images/fi/FineTuning.aac48f07142e36fd.webp)

- Ota käyttöön alkuperäinen esikoulutettu malli tai hienosäädetty versio etäkäytössä reaaliaikaisella päätepisteellä käyttäen hallittua laskentaa tai palvelimetta käyttöönotto- vaihtoehtoja, jolloin sovellukset voivat hyödyntää sitä.

![Model deployment](../../../translated_images/fi/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Kaikki katalogin mallit eivät tällä hetkellä ole saatavilla hienosäätöön ja/tai pay-as-you-go -käyttöönottoon. Tarkista mallikortista lisätiedot mallin ominaisuuksista ja rajoituksista.

## LLM-tulosten parantaminen

Olemme tutustuneet startup-tiimimme kanssa erilaisiin LLM-malleihin ja pilvialustaan (Microsoft Foundry), joka mahdollistaa eri mallien vertailun, testidatan arvioinnin, suorituskyvyn parantamisen ja mallien käyttöönoton päätepisteissä.

Mutta milloin heidän tulisi harkita mallin hienosäätöä sen sijaan, että käyttäisivät esikoulutettua mallia? Onko olemassa muita tapoja parantaa mallin suorituskykyä erityisissä työkuormissa?

Liiketoiminnalla on useita lähestymistapoja saavuttaa tarvitsemansa tulokset LLM:ltä. Voit valita erilaisia malleja eri koulutustasoilla käyttöönotossa, eri monimutkaisuusasteilla, kustannuksilla ja laadulla. Tässä muutamia erilaisia lähestymistapoja:

- **Kontekstiin perustuva kehotteiden suunnittelu (Prompt engineering)**. Ajatuksena on antaa riittävästi kontekstia kehotteeseen, jotta saat tarvitsemiasi vastauksia.

- **Retrieval Augmented Generation, RAG**. Datasi voi olla esimerkiksi tietokannassa tai verkkopäätepisteessä. Varmistaaksesi, että tämä data tai sen osa sisältyy kehotteeseen, voit hakea relevantin datan ja lisätä sen osaksi käyttäjän kehotetta.

- **Hienosäädetty malli**. Tässä olet kouluttanut mallia edelleen omalla datallasi, mikä tekee mallista tarkemman ja vastaavuudeltaan paremman tarpeisiisi, mutta voi olla kustannuksiltaan kallis.

![LLMs deployment](../../../translated_images/fi/Deploy.18b2d27412ec8c02.webp)

Kuvalähde: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Kehotteiden suunnittelu kontekstin kanssa

Esikoulutetut LLM:t toimivat erittäin hyvin yleistetyissä luonnollisen kielen tehtävissä, jopa lyhyellä kehotteella, kuten lauseen täydentämisellä tai kysymyksellä - ns. "zero-shot" -oppiminen.

Mitä paremmin käyttäjä pystyy muotoilemaan kyselynsä yksityiskohtaisesti ja esimerkkien avulla – eli tarjoamalla kontekstin – sitä osuvampi ja käyttäjän odotuksia vastaavampi vastaus on. Tällöin puhutaan "one-shot"-oppimisesta, jos kehotteessa on vain yksi esimerkki, ja "few-shot"-oppimisesta, jos mukana on useita esimerkkejä.
Kehotteiden suunnittelu kontekstin avulla on kustannustehokkain tapa aloittaa.

### Retrieval Augmented Generation (RAG)

LLM:illä on rajoitus, että ne voivat käyttää vain koulutuksessaan käytettyä dataa vastauksen tuottamiseen. Tämä tarkoittaa, etteivät ne tiedä koulutuksensa jälkeen tapahtuneista faktoista eivätkä pääse käsiksi ei-julkiseen tietoon (kuten yritystietoihin).
Tämä voidaan kiertää RAG-tekniikalla, jossa kehotteeseen lisätään ulkopuolista dataa, esimerkiksi dokumenttien osina, ottaen huomioon kehotteen pituusrajoitukset. Tätä tukee vektorihakukannat (kuten [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), jotka hakemalla löytävät hyödylliset osat eri ennalta määritellyistä tietolähteistä ja lisäävät ne kehotteen kontekstiin.

Tämä tekniikka on erittäin hyödyllinen tilanteissa, joissa liiketoiminnalla ei ole tarpeeksi dataa, aikaa tai resursseja hienosäätää LLM:ää, mutta se haluaa silti parantaa suorituskykyä tietyssä työkuormassa ja pienentää väärien, vanhentuneiden tai tukemattomien vastausten riskiä.

### Hienosäädetty malli

Hienosäätö on prosessi, joka hyödyntää siirto-oppimista mukauttaakseen mallin jälkikäyttöön tai ratkaisemaan tietyn ongelman. Toisin kuin few-shot oppimisessa ja RAG:ssa, se johtaa uuden mallin syntymiseen, jossa on päivitetyt painokertoimet ja vinot. Se vaatii koulutusjoukon, joka koostuu yksittäisistä syötteistä (kehotteista) ja niihin liittyvistä vasteista (lopputulos).
Tämä olisi suositeltava lähestymistapa, jos:

- **Käytetään pienempiä, tehtäväkohtaisia malleja**. Liiketoiminta haluaa hienosäätää pienemmän mallin kapeaan tehtävään sen sijaan, että jatkuvasti kutsuisi suurempaa rajamallia, mikä tekee ratkaisusta kustannustehokkaan ja nopeamman.

- **Harkitaan viivettä (latenssia)**. Viive on tärkeä tietylle käyttötapaukselle, joten ei ole mahdollista käyttää hyvin pitkiä kehotteita, tai mallin olisi opittava useista esimerkeistä mutta kehotteen pituusrajoitus estää sen.

- **Mukautetaan vakaata käyttäytymistä**. Liiketoiminnalla on monta korkealaatuista esimerkkiä ja halutaan, että malli noudattaa johdonmukaisesti tehtävän mallia, tulosteformaattia, sävyä tai toimialakohtaista tyyliä. Jos pääongelmana ovat tuoreet faktat tai yksityinen tieto, joka muuttuu usein, käytä mieluummin RAG:ia kuin luota pelkästään hienosäätöön.

### Koulutettu malli

LLM:n kouluttaminen alusta asti on kiistatta vaikein ja monimutkaisin lähestymistapa, joka vaatii valtavan määrän dataa, osaavia resursseja ja riittävää laskentatehoa. Tätä vaihtoehtoa tulisi harkita vain tilanteissa, joissa liiketoiminnalla on toimialakohtainen käyttötapaus ja suuri määrä siihen liittyvää dataa.

## Tiedon tarkistus

Mikä voisi olla hyvä tapa parantaa LLM:n vastaustuloksia?

1. Kehotteiden suunnittelu kontekstin kanssa
1. RAG
1. Hienosäädetty malli

V: Kaikki kolme voivat auttaa. Aloita kehotteiden suunnittelulla ja kontekstilla nopeisiin parannuksiin, ja käytä RAG:ia, kun mallin tarvitsee käyttää ajankohtaisia faktoja tai yrityksen yksityistietoja. Valitse hienosäätö, kun sinulla on riittävästi laadukkaita esimerkkejä ja haluat mallin noudattavan tehtävää, formaattia, sävyä tai toimialakuviota johdonmukaisesti.

## 🚀 Haaste

Lue lisää siitä, miten voit [käyttää RAGia](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) liiketoiminnassasi.

## Hienoa työtä, jatka oppimista

Kurssin suorittamisen jälkeen tutustu [Generative AI Learning -kokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generative AI -osaamisesi kehittämistä!

Siirry Oppitunnille 3, jossa käsittelemme sitä, miten [rakentaa Generative AI:ta vastuullisesti](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->