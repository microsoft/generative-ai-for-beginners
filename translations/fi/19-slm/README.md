# Johdanto pieniin kielimalleihin generatiivisessa tekoälyssä aloittelijoille
Generatiivinen tekoäly on kiehtova tekoälyn ala, joka keskittyy järjestelmien luomiseen, jotka pystyvät tuottamaan uutta sisältöä. Tämä sisältö voi vaihdella tekstistä ja kuvista musiikkiin ja jopa kokonaisiin virtuaalitodellisuuksiin. Yksi generatiivisen tekoälyn jännittävimmistä sovelluksista on kielimalleissa.

## Mitä ovat pienet kielimallit?

Pieni kielimalli (SLM) edustaa suuresta kielimallista (LLM) skaalattua pienempää versiota, hyödyntäen monia LLM:ien arkkitehtonisia periaatteita ja tekniikoita, samalla kun sillä on merkittävästi pienempi laskennallinen jalanjälki.

SLM:t ovat kielimalleja, jotka on suunniteltu tuottamaan ihmismäistä tekstiä. Toisin kuin suuremmat mallinsa, kuten GPT-4, SLM:t ovat kompakteja ja tehokkaita, mikä tekee niistä ihanteellisia sovelluksiin, joissa laskentaresurssit ovat rajallisia. Pienestä koosta huolimatta ne voivat suorittaa monenlaisia tehtäviä. Tyypillisesti SLM:t rakennetaan puristamalla tai tiivistämällä LLM:iä tavoitteena säilyttää merkittävä osa alkuperäisen mallin toiminnallisuudesta ja kielitaidoista. Mallin koon pienentäminen vähentää kokonaisvaltaista monimutkaisuutta, tehden SLM:istä tehokkaampia sekä muistin käytön että laskennallisten vaatimusten suhteen. Näistä optimoinneista huolimatta SLM:t voivat suorittaa laajan valikoiman luonnollisen kielen käsittelyn (NLP) tehtäviä:

- Tekstin generointi: Yhtenäisten ja asiayhteyteen sopivien lauseiden tai kappaleiden luominen.
- Tekstin täydennys: Lauseiden ennustaminen ja täyttäminen annetun kehotteen perusteella.
- Kääntäminen: Tekstin kääntäminen kielestä toiseen.
- Yhteenvedot: Pitkien tekstien tiivistäminen lyhyemmiksi, helpommin omaksuttaviksi yhteenvedoiksi.

Vaikkakin jonkinlaisten suorituskyky- tai ymmärryksen syvyyden kompromissien kera verrattuna suurempiin malleihin.

## Kuinka pienet kielimallit toimivat?
SLM:t koulutetaan valtavilla tekstidatoilla. Koulutuksen aikana ne oppivat kielen kaavat ja rakenteet, mikä mahdollistaa sekä kieliopillisesti oikean että asiayhteyteen sopivan tekstin generoinnin. Koulutusprosessi sisältää:

- Datan keruu: Suurten tekstiaineistojen kokoaminen eri lähteistä.
- Esikäsittely: Datan puhdistaminen ja järjestäminen koulutukseen sopivaksi.
- Koulutus: Koneoppimisalgoritmien käyttäminen mallin opettamiseksi tekstin ymmärtämiseen ja luomiseen.
- Hienosäätö: Mallin säätäminen parantamaan sen suorituskykyä tietyissä tehtävissä.

SLM:ien kehitys vastaa kasvavaa tarvetta malleille, joita voidaan ottaa käyttöön resurssirajoitetuissa ympäristöissä, kuten mobiililaitteissa tai reunalaskentalaitteissa, joissa täysimittaiset LLM:t voivat olla käytännössä epäkäytännöllisiä raskaiden resurssivaatimustensa vuoksi. Keskittymällä tehokkuuteen SLM:t tasapainottavat suorituskyvyn ja saavutettavuuden, mahdollistaen laajemman soveltamisen eri aloilla.

![slm](../../../translated_images/fi/slm.4058842744d0444a.webp)

## Oppimistavoitteet

Tässä oppitunnissa tarkoituksena on esitellä SLM:n tuntemus ja yhdistää se Microsoft Phi-3:n kanssa oppiaksemme erilaisista tekstisisällön, näön ja MoE:n skenaarioista.

Oppitunnin lopuksi sinun pitäisi pystyä vastaamaan seuraaviin kysymyksiin:

- Mitä on SLM?
- Mikä on ero SLM:n ja LLM:n välillä?
- Mikä on Microsoft Phi-3/3.5 -perhe?
- Kuinka suorittaa inferenssi Microsoft Phi-3/3.5 -perheellä?

Valmiina? Aloitetaan.

## Erot suurten kielimallien (LLM) ja pienten kielimallien (SLM) välillä

Sekä LLM:t että SLM:t perustuvat todennäköisyyksiin pohjautuvaan koneoppimiseen ja noudattavat samanlaisia lähestymistapoja arkkitehtuurinsa suunnittelussa, koulutusmenetelmissä, datan tuottamisessa ja mallin arvioinnissa. Kuitenkin useat keskeiset tekijät erottavat nämä kaksi mallityyppiä.

## Pienten kielimallien sovellukset

SLM:illä on monenlaisia käyttötarkoituksia, mukaan lukien:

- Chatbotit: Asiakastuen tarjoaminen ja käyttäjien kanssa keskusteleminen vuorovaikutteisesti.
- Sisällöntuotanto: Kirjoittajien avustaminen ideoiden luomisessa tai jopa kokonaisiin artikkeleihin.
- Koulutus: Opiskelijoiden auttaminen kirjoitustehtävissä tai uusien kielten oppimisessa.
- Saavutettavuus: Työkalujen luominen vamman tai vammaisuuden kanssa eläville, kuten tekstistä puheeksi -järjestelmät.

**Koko**
  
Suurin ero LLM:n ja SLM:n välillä on mallin koossa. LLM:t, kuten ChatGPT (GPT-4), voivat sisältää noin 1,76 biljoonaa parametria, kun taas avoimen lähdekoodin SLM:t, kuten Mistral 7B, on suunniteltu huomattavasti pienemmällä parametrimäärällä — noin 7 miljardia. Tämä ero johtuu pääosin mallin arkkitehtuurista ja koulutusmenetelmistä. Esimerkiksi ChatGPT käyttää itsehuomiomekanismia enkooderi-dekooderi-rakenteessa, kun taas Mistral 7B käyttää liukuikkuna-huomiota, mikä mahdollistaa tehokkaamman koulutuksen pelkästään dekooderipohjaisessa mallissa. Tämä arkkitehtoninen ero vaikuttaa merkittävästi mallien monimutkaisuuteen ja suorituskykyyn.

**Ymmärrys**

SLM:t on tyypillisesti optimoitu suoriutumaan hyvin tietyillä aloilla, tehden niistä erittäin erikoistuneita mutta mahdollisesti rajallisia kyvyltään tarjota laajaa asiayhteyteen perustuvaa ymmärrystä usealla tieteenalalla. Sen sijaan LLM:t pyrkivät simuloimaan ihmismäistä älykkyyttä laajemmin. Laajoilla ja monipuolisilla aineistoilla koulutettuina LLM:t on suunniteltu toimimaan hyvin monilla aloilla tarjoten suurempaa monipuolisuutta ja sopeutumiskykyä. Tästä syystä LLM:t soveltuvat paremmin laajempaan kirjoon alaspäin suuntautuvia tehtäviä, kuten luonnollisen kielen käsittelyä ja ohjelmointia.

**Laskenta**

LLM:ien koulutus ja käyttöönotto ovat raskaita resursseja vaativia prosesseja, jotka usein edellyttävät huomattavaa laskentainfrastruktuuria, kuten suuria GPU-klustereita. Esimerkiksi ChatGPT:n kaltaisen mallin kouluttaminen alusta alkaen voi vaatia tuhansia GPU:ita pitkiä aikoja. Sitä vastoin SLM:t, pienemmän parametrimääränsä vuoksi, ovat helpommin saavutettavissa laskentaresurssien osalta. Mallit kuten Mistral 7B voidaan kouluttaa ja ajaa paikallisissa koneissa, joissa on kohtuulliset GPU-ominaisuudet, vaikka koulutus vie silti useita tunteja useilla GPU:illa.

**Vääristymä**

Vääristymät ovat tunnettu ongelma LLM:issä, pääasiassa koulutusdatan luonteen vuoksi. Nämä mallit usein käyttävät raakadataa, joka on avoimesti saatavilla internetistä, ja data voi aliedustaa tai vääristää tiettyjä ryhmiä, sisältää virheellisiä merkintöjä tai heijastaa kielisiä vinoumia, jotka johtuvat murteista, maantieteellisistä eroista ja kielioppisäännöistä. Lisäksi LLM:ien arkkitehtuurin monimutkaisuus voi tahattomasti pahentaa vääristymiä, jotka voivat jäädä huomaamatta ilman tarkkaa hienosäätöä. SLM:t, koulutettuna rajatuilla, toimialakohtaisilla aineistoilla, ovat luontaisesti vähemmän alttiita näille vääristymille, vaikka eivät täysin immuuneja niille.

**Inferenssi**

Pienempi koko antaa SLM:ille merkittävän edun inferenssin nopeudessa, mahdollistaen tehokkaan tulosten tuottamisen paikallisella laitteistolla ilman laajamittaista rinnakkaislaskentaa. LLM:t, kokonsa ja monimutkaisuutensa vuoksi, vaativat usein merkittäviä rinnakkaisia laskentaresursseja saavuttaakseen hyväksyttävät inferenssiajan. Useiden samanaikaisten käyttäjien läsnäolo hidastaa LLM:ien vastausaikoja vielä enemmän, varsinkin suurissa käyttöönottoympäristöissä.

Yhteenvetona, vaikka LLM:t ja SLM:t jakavat koneoppimisen perustan, ne eroavat merkittävästi mallin koon, resurssivaatimusten, asiayhteyden ymmärtämisen, alttiuden vääristymille ja inferenssin nopeuden osalta. Nämä erot heijastavat niiden soveltuvuutta eri käyttötarkoituksiin, siten että LLM:t ovat monipuolisempia mutta vaativat runsaasti resursseja, kun taas SLM:t tarjoavat toimialakohtaista tehokkuutta ja vähäisemmät laskennalliset vaatimukset.

***Huomautus: Tässä oppitunnissa esittelemme SLM:n käyttäen Microsoft Phi-3 / 3.5 -malleja esimerkein.***

## Esittely Phi-3 / Phi-3.5 -perheestä

Phi-3 / 3.5 -perhe kohdentuu pääasiassa tekstin, näön ja Agentin (MoE) sovellustilanteisiin:

### Phi-3 / 3.5 Instruct

Pääasiassa tekstin generointiin, keskustelun täydennykseen ja sisällön tiedon erotteluun jne.

**Phi-3-mini**

3,8 miljardin parametrin kielimalli on saatavilla Microsoft Foundryssä, Hugging Face:ssa ja Ollamassa. Phi-3-mallit päihittävät merkittävästi saman kokoiset ja suuremmat kielimallit keskeisissä vertailuissa (katso vertailuluvut alla, suuremmat luvut ovat parempia). Phi-3-mini päihittää kaksinkertaisen kokonsa omaavat mallit, kun taas Phi-3-small ja Phi-3-medium päihittävät suuremmat mallit, mukaan lukien GPT-3.5.

**Phi-3-small & medium**

Vain 7 miljardilla parametrilla Phi-3-small päihittää GPT-3.5T useissa kieli-, päättely-, koodaus- ja matematiikkaverrokkitehtävissä.

Phi-3-medium, jossa on 14 miljardia parametria, jatkaa tätä trendiä ja päihittää Gemini 1.0 Pro:n.

**Phi-3.5-mini**

Voimme ajatella sitä Phi-3-minin päivityksenä. Vaikka parametrimäärä pysyy samana, se parantaa kykyä tukea monia kieliä (tukee yli 20 kieltä: arabia, kiina, tšekki, tanska, hollanti, englanti, suomi, ranska, saksa, heprea, unkari, italia, japani, korea, norja, puola, portugali, venäjä, espanja, ruotsi, thai, turkki, ukraina) ja lisää vahvempaa tukea pitkäkestoiselle asiayhteydelle.

Phi-3.5-mini, jossa on 3,8 miljardia parametria, päihittää saman kokoiset kielimallit ja on tasavertainen kaksinkertaisen kokoisten mallien kanssa.

### Phi-3 / 3.5 Vision

Voimme ajatella Phi-3/3.5 Instruct-mallia Phin kyvyksi ymmärtää, ja Visionia ikään kuin Phin silmiksi maailman ymmärtämiseen.


**Phi-3-Vision**

Phi-3-vision, jossa on vain 4,2 miljardia parametria, jatkaa tätä kehityslinjaa ja päihittää suurempia malleja kuten Claude-3 Haiku ja Gemini 1.0 Pro V yleisissä visuaalisissa päättelytehtävissä, OCR-tehtävissä sekä taulukkojen ja diagrammien ymmärtämisessä.


**Phi-3.5-Vision**

Phi-3.5-Vision on myös Phi-3-Visionin päivitys, lisäten tuen useille kuville. Voit ajatella sitä näön parannuksena – voit nähdä ei pelkästään kuvia, vaan myös videoita.

Phi-3.5-vision päihittää suuremmat mallit kuten Claude-3.5 Sonnet ja Gemini 1.5 Flash OCR-, taulukko- ja kaaviotehtävissä ja on tasavertainen yleisissä visuaalisen tiedon päättelytehtävissä. Tukee monikehyksistä syötettä eli tekee päättelyä useilla kuvasyötteillä.


### Phi-3.5-MoE

***Asiantuntijoiden sekoitus (Mixture of Experts, MoE)*** mahdollistaa mallien esikoulutuksen paljon pienemmällä laskentateholla, mikä tarkoittaa, että voit dramaattisesti kasvattaa mallin tai aineiston kokoa samalla laskentabudjetilla kuin tiheä malli. Erityisesti MoE-mallin pitäisi saavuttaa sama laatu kuin tiheän mallin versio paljon nopeammin esikoulutuksen aikana.

Phi-3.5-MoE koostuu 16x3,8 miljardin asiantuntijamoduulista. Phi-3.5-MoE, jossa on vain 6,6 miljardia aktiivista parametria, saavuttaa saman tason päättelyssä, kielten ymmärryksessä ja matematiikassa kuin paljon suuremmat mallit.

Voimme käyttää Phi-3/3.5 Perhemuotia eri tilanteissa. Toisin kuin LLM, voit ottaa käyttöön Phi-3/3.5-mini- tai Phi-3/3.5-Vision -malleja reunalaitteissa.


## Kuinka käyttää Phi-3/3.5 -perheen malleja

Haluamme käyttää Phi-3/3.5:ttä eri skenaarioissa. Seuraavaksi käytämme Phi-3/3.5:tä eri tilanteissa.

![phi3](../../../translated_images/fi/phi3.655208c3186ae381.webp)

### Inferenssi pilvipalvelujen API-en kautta

**Microsoft Foundry -mallit**

> **Huom:** GitHub Models poistuu käytöstä heinäkuun 2026 lopussa. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) on suora korvaaja.

Microsoft Foundry Models on suoraviivaisin tapa. Voit nopeasti käyttää Phi-3/3.5-Instruct -mallia Foundryn malliluettelon kautta. Yhdessä Azure AI Inference SDK:n / OpenAI SDK:n kanssa voit käyttää API:a koodin kautta Phi-3/3.5-Instruct -kutsun suorittamiseen. Voit myös testata eri vaikutuksia Playgroundin kautta.

- Demo: Phi-3-mini:n ja Phi-3.5-mini:n vertailu kiinankielisissä skenaarioissa

![phi3](../../../translated_images/fi/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/fi/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Tai jos haluamme käyttää Vision- ja MoE-malleja, voit käyttää Microsoft Foundrya kutsujen suorittamiseen. Jos olet kiinnostunut, voit lukea Phi-3 CookBookin ja oppia, kuinka kutsua Phi-3/3.5 Instruct-, Vision-, MoE-malleja Microsoft Foundryn kautta [Klikkaa tästä linkistä](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Pilvipohjaisen Microsoft Foundry Models -katalogin lisäksi voit käyttää myös [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) suorittamaan vastaavat kutsut. Voit vierailla NVIDIA NIM:ssä suorittaaksesi Phi-3/3.5 -perheen API-kutsut. NVIDIA NIM (NVIDIA Inference Microservices) on joukko kiihtyviä inferenssimikropalveluja, jotka auttavat kehittäjiä ottamaan tekoälymalleja tehokkaasti käyttöön eri ympäristöissä, mukaan lukien pilvet, datakeskukset ja työasemat.

Tässä joitakin NVIDIA NIM:n keskeisiä ominaisuuksia:

- **Helppokäyttöisyys käyttöönotossa:** NIM mahdollistaa tekoälymallien käyttöönoton yhdellä komennolla, tehden sen helposti integroitavaksi olemassa oleviin työnkulkuhin.

- **Optimoitu suorituskyky:** Se hyödyntää NVIDIA:n esivalmisteltuja inferenssimoottoreita, kuten TensorRT:tä ja TensorRT-LLM:ää, varmistaen pienen viiveen ja korkean läpimenon.
- **Skaalautuvuus:** NIM tukee automaattista skaalausta Kubernetesissa, mikä mahdollistaa vaihtelevien kuormitusten tehokkaan käsittelyn.
- **Turvallisuus ja hallinta:** Organisaatiot voivat säilyttää hallinnan tiedoistaan ja sovelluksistaan itse isännöimällä NIM-mikropalveluita omalla hallinnoidulla infrastruktuurillaan.
- **Standardoidut API:t:** NIM tarjoaa alan standardien mukaisia API:ita, mikä helpottaa tekoälysovellusten, kuten chatbotien, tekoälyavustajien ja muiden rakentamista ja integrointia.

NIM on osa NVIDIA AI Enterprise -ohjelmistoa, jonka tavoitteena on yksinkertaistaa tekoälymallien käyttöönottoa ja operatiivista hallintaa, varmistaen niiden tehokkaan toiminnan NVIDIA GPU:illa.

- Demo: NVIDIA NIM:n käyttäminen Phi-3.5-Vision-API:n kutsumiseen  [[Klikkaa tästä](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 paikallinen suoritus
Inferenssi Phi-3:n tai minkä tahansa kielimallin, kuten GPT-3:n, yhteydessä tarkoittaa prosessia, jossa luodaan vastauksia tai ennusteita saatujen syötteiden perusteella. Kun annat Phi-3:lle kehotteen tai kysymyksen, se käyttää koulutettua neuroverkkoaan päättääkseen todennäköisimmän ja olennaisimman vastauksen analysoimalla malleja ja yhteyksiä koulutusdatassaan.

**Hugging Face Transformer**
Hugging Face Transformers on tehokas kirjasto, joka on suunniteltu luonnollisen kielen käsittelyyn (NLP) ja muihin koneoppimistehtäviin. Tässä muutama keskeinen kohta siitä:

1. **Valmiiksi koulutetut mallit**: Kirjasto tarjoaa tuhansia valmiiksi koulutettuja malleja, joita voi käyttää eri tehtäviin, kuten tekstiluokitteluun, nimettyjen entiteettien tunnistamiseen, kysymyksiin vastaamiseen, tiivistämiseen, käännöksiin ja tekstin generointiin.

2. **Yhteensopivuus eri kehysten kanssa**: Kirjasto tukee useita syväoppimiskehyksiä, kuten PyTorchia, TensorFlow'ta ja JAX:ia. Tämä antaa mahdollisuuden kouluttaa malli yhdessä kehyksessä ja käyttää sitä toisessa.

3. **Monimodaaliset ominaisuudet**: NLP:n lisäksi Hugging Face Transformers tukee tehtäviä myös tietokonenäössä (esim. kuvien luokittelu, kohteiden tunnistus) ja äänen käsittelyssä (esim. puheentunnistus, äänen luokittelu).

4. **Helppokäyttöisyys**: Kirjasto tarjoaa API:t ja työkalut mallien lataamiseen ja hienosäätöön, tehden siitä helposti lähestyttävän sekä aloittelijoille että asiantuntijoille.

5. **Yhteisö ja resurssit**: Hugging Facella on elinvoimainen yhteisö sekä laaja dokumentaatio, opetusohjelmat ja oppaat, jotka auttavat käyttäjiä pääsemään alkuun ja hyödyntämään kirjastoa parhaalla mahdollisella tavalla.
[virallinen dokumentaatio](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) tai heidän [GitHub-repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Tämä on eniten käytetty menetelmä, mutta se vaatii myös GPU-kiihdytyksen. Esimerkiksi Vision- ja MoE-tilanteet edellyttävät paljon laskentaa, mikä olisi hyvin hidasta CPU:lla, ellei malleja ole kvantisoitu.


- Demo: Transformerilla Phi-3.5-Instructin kutsuminen [Klikkaa tästä](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformerilla Phi-3.5-Visionin kutsuminen [Klikkaa tästä](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformerilla Phi-3.5-MoEn kutsuminen [Klikkaa tästä](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) on alusta, joka tekee isojen kielimallien (LLM) paikallisesta suorittamisesta koneellasi helpompaa. Se tukee useita malleja kuten Llama 3.1, Phi 3, Mistral ja Gemma 2. Alusta yksinkertaistaa prosessia paketoimalla mallipainot, konfiguraation ja datan yhdeksi paketiksi, jolloin käyttäjien on helpompi muokata ja luoda omia mallejaan. Ollama on saatavana macOS:lle, Linuxille ja Windowsille. Se on erinomainen työkalu, jos haluat kokeilla tai ottaa käyttöön LLM-malleja ilman pilvipalveluihin turvautumista. Ollama on suoraviivaisin tapa, sinun tarvitsee vain suorittaa seuraava komento.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) on Microsoftin offline- ja laitteella toimiva runtime-ympäristö, joka mahdollistaa mallien kuten Phi suorittamisen kokonaan omalla raudallasi – ei Azure-tilausta, API-avainta tai verkkoyhteyttä tarvita. Se valitsee automaattisesti parhaan käytettävissä olevan suoritusteknologian (NPU, GPU tai CPU) ja tarjoaa OpenAI-yhteensopivan päätepisteen, joten olemassa olevaa `openai`/Azure AI Inference SDK -koodia voi käyttää vähäisillä muutoksilla. Katso [Foundry Local -dokumentaatio](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) aloitusta varten.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Tai käytä SDK:ta suoraan Pythonissa:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) on monialustainen inferenssi- ja koneoppimisen koulutuskiihdytin. ONNX Runtime for Generative AI (GENAI) on tehokas työkalu, joka auttaa suorittamaan generatiivisia tekoälymalleja tehokkaasti eri alustoilla.

## Mikä on ONNX Runtime?
ONNX Runtime on avoimen lähdekoodin projekti, joka mahdollistaa koneoppimismallien korkean suorituskyvyn inferenssin. Se tukee Open Neural Network Exchange (ONNX) -muotoa, joka on standardi koneoppimismallien esittämiseen. ONNX Runtime -inferenssi voi parantaa asiakaskokemusta ja alentaa kustannuksia tukemalla malleja syväoppimiskehyksistä kuten PyTorch ja TensorFlow/Keras sekä perinteisemmistä koneoppimiskirjastoista kuten scikit-learn, LightGBM, XGBoost jne. ONNX Runtime on yhteensopiva eri laitteistojen, ajureiden ja käyttöjärjestelmien kanssa ja tarjoaa optimaalisen suorituskyvyn hyödyntämällä laitteistokiihdyttimiä yhdessä graafien optimointien ja muunnosten kanssa.

## Mikä on Generatiivinen tekoäly?
Generatiivinen tekoäly tarkoittaa tekoälyjärjestelmiä, jotka voivat luoda uutta sisältöä, kuten tekstiä, kuvia tai musiikkia, koulutusdataansa perustuen. Esimerkkejä ovat kielimallit kuten GPT-3 ja kuvanluontimallit kuten Stable Diffusion. ONNX Runtime for GenAI -kirjasto tarjoaa generatiivisen tekoälyn silmukan ONNX-malleille, mukaan lukien inferenssin ONNX Runtime -alustalla, logitsien käsittelyn, haun ja otannan sekä KV-välimuistin hallinnan.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI laajentaa ONNX Runtime -alustan kyvykkyyksiä tukemaan generatiivisia tekoälymalleja. Tässä joitakin keskeisiä ominaisuuksia:

- **Laaja alustan tuki:** Toimii eri alustoilla, kuten Windows, Linux, macOS, Android ja iOS.
- **Mallien tuki:** Tukee monia suosittuja generatiivisia tekoälymalleja, kuten LLaMA, GPT-Neo, BLOOM ja muita.
- **Suorituskyvyn optimointi:** Sisältää optimointeja erilaisille laitteistokiihdyttimille, kuten NVIDIA GPU:t, AMD GPU:t ja muut.
- **Helppokäyttöisyys:** Tarjoaa API:t helppoon integrointiin sovelluksiin, mahdollistaen tekstin, kuvien ja muun sisällön generoinnin vähäisellä koodilla.
- Käyttäjät voivat kutsua korkean tason generate()-metodia tai suorittaa mallin jokaisen silmukan iteroinnin erikseen, generoiden yhden tokenin kerrallaan ja tarvittaessa päivittäen generointiparametreja silmukan sisällä.
- ONNX Runtime tukee myös ahne-/palkkihausta ja TopP, TopK -näytteistystä token-sekvenssien tuottamiseen ja sisäänrakennettua logits-käsittelyä kuten toistojen rajoituksia. Lisäksi voidaan helposti lisätä mukautettua pisteytystä.

## Aloittaminen
Aloittaaksesi ONNX Runtime for GENAI:n käytön, voit seurata seuraavia vaiheita:

### Asenna ONNX Runtime:
```Python
pip install onnxruntime
```
### Asenna Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Suorita malli: Tässä yksinkertainen esimerkki Pythonilla:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo: ONNX Runtime GenAI:n käyttö Phi-3.5-Visionin kutsumiseen


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Muut**

ONNX Runtime:n, Ollaman ja Foundry Localin viitemenettelyiden lisäksi voimme myös täydentää kvantitatiivisten mallien referenssejä eri valmistajien mallireferenssien avulla. Esimerkiksi Apple MLX -kehys Apple Metalin kanssa, Qualcomm QNN NPU:lla, Intel OpenVINO CPU/GPU:lla jne. Lisäsisältöä löytyy myös [Phi-3 Cookbookista](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Lisää

Olemme oppineet Phi-3/3.5 -perheen perusteet, mutta SLM:ään tutustuminen vaatii lisätietoa. Vastaukset löydät Phi-3 Cookbookista. Jos haluat oppia lisää, käy [Phi-3 Cookbookissa](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->