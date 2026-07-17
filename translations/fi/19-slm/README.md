# Johdanto pieniin kielimalleihin generatiivisessa tekoälyssä aloittelijoille
Generatiivinen tekoäly on kiehtova tekoälyn osa-alue, joka keskittyy järjestelmien luomiseen, jotka pystyvät generoimaan uutta sisältöä. Tämä sisältö voi vaihdella tekstistä ja kuvista musiikkiin ja jopa kokonaisiin virtuaaliympäristöihin. Yksi jännittävimmistä generatiivisen tekoälyn sovelluksista on kielimalleissa.

## Mitä ovat pienet kielimallit?

Pieni kielimalli (SLM) edustaa pienennettyä versiota suuresta kielimallista (LLM), hyödyntäen monia LLM:ien arkkitehtonisia periaatteita ja tekniikoita, mutta sillä on merkittävästi pienempi laskentaresurssien tarve.

SLM:t ovat kielimalleja, jotka on suunniteltu tuottamaan ihmismäistä tekstiä. Toisin kuin suuremmat mallit, kuten GPT-4, SLM:t ovat kompakteja ja tehokkaita, mikä tekee niistä ihanteellisia sovelluksiin, joissa laskentaresurssit ovat rajalliset. Vaikka ne ovat kooltaan pienempiä, ne voivat silti suorittaa erilaisia tehtäviä. Tyypillisesti SLM:t rakennetaan puristamalla tai tiivistämällä LLM:iä, pyrkien säilyttämään suuri osa alkuperäisen mallin toiminnallisuudesta ja kielitaidoista. Mallin koon pienentäminen vähentää kokonaiskompleksisuutta, jolloin SLM:t ovat tehokkaampia sekä muistin käytön että laskentatarpeiden suhteen. Näistä optimoinneista huolimatta SLM:t voivat edelleen suorittaa laajan valikoiman luonnollisen kielen käsittelyn (NLP) tehtäviä:

- Tekstin generointi: Loogisten ja kontekstuaalisesti relevanttien lauseiden tai kappaleiden luominen.
- Tekstin täydentäminen: Lauseiden ennustaminen ja täydentäminen annetun kehotteen perusteella.
- Kääntäminen: Tekstin muuntaminen kielestä toiseen.
- Yhteenveto: Pitkien tekstien tiivistäminen lyhyemmiksi, helpommin sulatettaviksi yhteenvetoiksi.

Joskin joidenkin suorituskyvyn tai ymmärryksen syvyyden kompromissien kustannuksella verrattuna suurempiin malleihin.

## Kuinka pienet kielimallit toimivat?
SLM:t koulutetaan valtavilla tekstiaineistoilla. Koulutuksen aikana ne oppivat kielen rakenteet ja mallit, mikä mahdollistaa kieliopillisesti oikean ja kontekstuaalisesti sopivan tekstin generoinnin. Koulutusprosessi sisältää:

- Datan kerääminen: Suurten tekstiaineistojen kokoaminen eri lähteistä.
- Esikäsittely: Datan puhdistaminen ja järjestäminen koulutusta varten sopivaksi.
- Koulutus: Koneoppimisalgoritmien käyttäminen mallin opettamiseksi ymmärtämään ja tuottamaan tekstiä.
- Hienosäätö: Mallin säätäminen parantamaan sen suorituskykyä tietyissä tehtävissä.

SLM:ien kehitys vastaa kasvavaa tarvetta malleille, jotka voidaan ottaa käyttöön resurssirajoitetuissa ympäristöissä, kuten mobiililaitteissa tai reunalaskentaympäristöissä, joissa täysimittaiset LLM:t saattavat olla epäkäytännöllisiä niiden raskaan resurssivaatimusten vuoksi. Keskittymällä tehokkuuteen, SLM:t tasapainottavat suorituskyvyn ja saavutettavuuden, mahdollistaen laajemman soveltamisen eri alueilla.

![slm](../../../translated_images/fi/slm.4058842744d0444a.webp)

## Oppimistavoitteet

Tässä oppitunnissa toivomme esitellä SLM:n tiedon ja yhdistää se Microsoft Phi-3:n kanssa oppiaksemme erilaisista tekstisisällön, kuvan ja MoE:n skenaarioista.

Oppitunnin lopussa sinun pitäisi pystyä vastaamaan seuraaviin kysymyksiin:

- Mikä on SLM?
- Mikä on ero SLM:n ja LLM:n välillä?
- Mikä on Microsoft Phi-3/3.5 perhe?
- Kuinka suorittaa inferenssi Microsoft Phi-3/3.5 perheellä?

Valmis? Aloitetaan.

## Erot suurten kielimallien (LLM) ja pienten kielimallien (SLM) välillä

Sekä LLM:t että SLM:t perustuvat todennäköisyyspohjaisen koneoppimisen perustavanlaatuisiin periaatteisiin, noudattaen samanlaisia lähestymistapoja arkkitehtuurinsa suunnittelussa, koulutusmenetelmissä, datan generointiprosesseissa ja mallin arviointitekniikoissa. Kuitenkin useat keskeiset tekijät erottavat nämä kaksi mallityyppiä.

## Pienten kielimallien sovellukset

SLM:illä on laaja sovellusalue, mukaan lukien:

- Chatbotit: Asiakastuen tarjoaminen ja käyttäjien kanssa keskusteleminen.
- Sisällön luominen: Kirjoittajien avustaminen ideoiden generoinnissa tai jopa koko artikkeleiden luonnostelussa.
- Koulutus: Oppilaiden auttaminen kirjoitustehtävissä tai uusien kielten oppimisessa.
- Saavutettavuus: Työkalujen luominen vammaisille henkilöille, kuten puheeksi muuttojärjestelmät.

**Koko**
  
Keskeinen ero LLM:ien ja SLM:ien välillä liittyy mallien kokoon. LLM:t, kuten ChatGPT (GPT-4), voivat sisältää arviolta 1,76 biljoonaa parametria, kun taas avoimen lähdekoodin SLM:t, kuten Mistral 7B, on suunniteltu merkittävästi pienemmillä parametrijoukoilla — noin 7 miljardia. Tämä ero johtuu pääasiassa erotuksista mallin arkkitehtuurissa ja koulutusprosesseissa. Esimerkiksi ChatGPT käyttää itsehuomiomekanismia kooderi-dekooderi -kehyksessä, kun taas Mistral 7B hyödyntää liukuvan ikkunan huomiota, mikä mahdollistaa tehokkaamman koulutuksen pelkän dekooderimallin sisällä. Tämä arkkitehtoninen ero vaikuttaa syvästi mallien monimutkaisuuteen ja suorituskykyyn.

**Ymmärrys**

SLM:t on tyypillisesti optimoitu suorituskyvyn suhteen tietyillä alueilla, tehden niistä erittäin erikoistuneita, mutta potentiaalisesti rajallisia kyvyssä tarjota laaja-alaista kontekstuaalista ymmärrystä useilla tieteenaloilla. Sen sijaan LLM:t pyrkivät simuloimaan ihmismäistä älykkyyttä laajemmalla tasolla. Koulutettuna valtavilla, monipuolisilla aineistoilla, LLM:t on suunniteltu toimimaan hyvin monipuolisissa tehtävissä tarjoten suuremman monipuolisuuden ja sopeutumiskyvyn. Tästä syystä LLM:t soveltuvat paremmin laajempaan tehtäväskaalaan, kuten luonnollisen kielen käsittelyyn ja ohjelmointiin.

**Laskenta**

LLM:ien koulutus ja käyttöönotto ovat resurssi-intensiivisiä prosesseja, jotka vaativat usein merkittävää laskenta-infrastruktuuria, mukaan lukien laajamittaiset GPU-klusterit. Esimerkiksi mallin, kuten ChatGPT:n, koulutus tyhjästä voi edellyttää tuhansia GPU:ita pitkiä aikoja. Sen sijaan SLM:t, pienemmillä parametrimäärillä varustettuina, ovat helpommin saavutettavissa laskentaresurssien puolesta. Mallit, kuten Mistral 7B, voidaan kouluttaa ja ajaa paikallisilla koneilla, jotka on varustettu kohtuullisilla GPU-kapasiteeteilla, vaikkakin koulutus vaatii edelleen useita tunteja useilla GPU:illa.

**Vinouma**

Vinouma on tunnettu ongelma LLM:issä, pääasiassa koulutusdatan luonteen vuoksi. Nämä mallit käyttävät usein raakaa, avoimesti saatavilla olevaa internet-dataa, joka voi aliedustaa tai vääristää tiettyjä ryhmiä, aiheuttaa virheellisiä luokitteluja tai heijastaa kielellisiä vinoumia, joita vaikuttavat murre, maantieteelliset vaihtelut ja kieliopin säännöt. Lisäksi LLM-arkkitehtuurien monimutkaisuus voi tahattomasti pahentaa vinoumaa, mikä saattaa jäädä huomaamatta ilman huolellista hienosäätöä. Toisaalta SLM:t, jotka on koulutettu rajatummilla, alakohtaisilla aineistoilla, ovat luonnostaan vähemmän alttiita tällaisille vinoumille, vaikka eivät ole täysin immuuneja niille.

**Inferenssi**

Pienempi koko antaa SLM:ille merkittävän edun inferenssin nopeudessa, mahdollistaen tehokkaan suorituskyvyn paikallisella laitteistolla ilman laajamittaista rinnakkaislaskentaa. Sen sijaan LLM:t, koon ja monimutkaisuuden vuoksi, vaativat usein huomattavia rinnakkaisia laskentaresursseja saavuttaakseen hyväksyttävät inferenssiaikojen arvot. Useiden samanaikaisten käyttäjien läsnäolo hidastaa LLM:ien vasteaikoja entisestään, erityisesti laajamittaisessa käytössä.

Yhteenvetona, vaikka sekä LLM:t että SLM:t perustuvat koneoppimisen perusperiaatteisiin, ne eroavat merkittävästi mallin koon, resurssivaatimusten, kontekstuaalisen ymmärryksen, vinoumille alttiuden ja inferenssin nopeuden suhteen. Nämä erot heijastavat niiden soveltuvuutta erilaisiin käyttötarkoituksiin, joissa LLM:t ovat monipuolisempia mutta raskaita resursseiltaan, ja SLM:t tarjoavat alakohtaista tehokkuutta vähentyneiden laskentaresurssivaatimusten kera.

***Huomautus: Tässä oppitunnissa esittelemme SLM:n käyttäen esimerkkinä Microsoft Phi-3 / 3.5 -mallisarjaa.***

## Phi-3 / Phi-3.5 -perheen esittely

Phi-3 / 3.5 -perhe keskittyy pääasiassa tekstin, näön ja Agentin (MoE) sovelluskohtaisiin skenaarioihin:

### Phi-3 / 3.5 Ohjattu malli (Instruct)

Pääasiassa tekstin generointiin, keskustelun täydentämiseen ja sisällön tiedon purkuun jne.

**Phi-3-mini**

3,8 miljardin parametrin kielimalli on saatavilla Microsoft Foundryssa, Hugging Facessa ja Ollamassa. Phi-3-mallit ylittävät merkittävästi vastaavan ja suuremmat kielimallit keskeisillä vertailutaulukoilla (ks. alla benchmark-luvut, suurempi luku on parempi). Phi-3-mini päihittää kaksinkertaisia kokoja suuremmat mallit, kun taas Phi-3-small ja Phi-3-medium päihittävät suurempia malleja, mukaan lukien GPT-3.5.

**Phi-3-small & medium**

Vain 7 miljardilla parametrillaan Phi-3-small päihittää GPT-3.5T monissa kielen, päättelyn, koodauksen ja matematiikan vertailuissa.

Phi-3-medium 14 miljardilla parametrillaan jatkaa tätä trendiä ja päihittää Gemini 1.0 Pron.

**Phi-3.5-mini**

Voimme ajatella sitä Phi-3-mini -mallin päivityksenä. Parametrit säilyvät ennallaan, mutta se parantaa monikielisyystukea (tukee yli 20 kieltä: arabia, kiina, tšekki, tanska, hollanti, englanti, suomi, ranska, saksa, heprea, unkari, italia, japani, korea, norja, puolassa, portugali, venäjä, espanja, ruotsi, thaimaa, turkki, ukraina) ja lisää vahvemman tuen pitkille konteksteille.

Phi-3.5-mini 3,8 miljardilla parametrilla päihittää saman kokoiset kielimallit ja on tasoltaan kaksinkertaisten mallien kanssa.

### Phi-3 / 3.5 Näkö

Voimme ajatella Phi-3/3.5 ohjatun mallin olevan Phi:n kyky ymmärtää, ja Näkö antaa Phille silmät maailman ymmärtämiseksi.


**Phi-3-Näkö**

Phi-3-näkö, vain 4,2 miljardilla parametrilla, jatkaa tätä trendiä ja päihittää suurempia malleja, kuten Claude-3 Haiku ja Gemini 1.0 Pro V yleisissä visuaalisen päättelyn tehtävissä, OCR:ssa sekä taulukko- ja diagrammin ymmärtämistehtävissä.


**Phi-3.5-Näkö**

Phi-3.5-Näkö on myös Phi-3-Näön päivitys, joka lisää tuen useille kuville. Voit ajatella sitä näön parantamisena: se ei pelkästään näe kuvia, vaan myös videoita.

Phi-3.5-näkö päihittää suurempia malleja, kuten Claude-3.5 Sonnet ja Gemini 1.5 Flash, OCR:ssa, taulukkojen ja kaavioiden ymmärtämisessä, ja on samalla tasolla yleisessä visuaalisen tiedon päättelyssä. Tukee monikehysin syötteitä, eli suorittaa päättelyn useilla syötekuvilla.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** mahdollistaa mallien esikoulutuksen paljon pienemmillä laskentaresursseilla, mikä tarkoittaa, että voit dramaattisesti kasvattaa mallin tai aineiston kokoa samalla laskentabudjetilla kuin tiheämmässä mallissa. Erityisesti MoE-malli saavuttaa saman laadun kuin tiheä vastine paljon nopeammin esikoulutuksessa.

Phi-3.5-MoE koostuu 16x3,8 miljardin asiantuntijamoduulista. Phi-3.5-MoE saavuttaa vain 6,6 miljardilla aktiivisella parametrilla saman tason päättelyssä, kielten ymmärtämisessä ja matematiikassa kuin huomattavasti suuremmat mallit.

Voimme käyttää Phi-3/3.5 -perheen malleja eri skenaarioissa. Toisin kuin LLM, voit ottaa käyttöön Phi-3/3.5-mini tai Phi-3/3.5-Näkö reunalaitteissa.


## Kuinka käyttää Phi-3/3.5 -perheen malleja

Toivomme käyttävämme Phi-3/3.5 eri skenaarioissa. Seuraavaksi käytämme Phi-3/3.5 eri sovelluksissa.

![phi3](../../../translated_images/fi/phi3.655208c3186ae381.webp)

### Inferenssi pilvipalveluiden API:en kautta

**Microsoft Foundry -mallit**

> **Huom:** GitHub-mallit poistuvat käytöstä heinäkuun 2026 lopussa. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) on suora korvaaja.

Microsoft Foundry -mallit ovat suorin tapa. Voit nopeasti käyttää Phi-3/3.5-Instruct-mallia Foundryn malliluettelon kautta. Yhdistettynä Azure AI Inference SDK:hon / OpenAI SDK:hon voit käyttää API:a koodin kautta suorittaaksesi Phi-3/3.5-Instruct-kutsun. Voit myös testata eri tuloksia PlayGroundissa.

- Demo: Vertailu Phi-3-mini ja Phi-3.5-mini vaikutuksista kiinankielisissä skenaarioissa

![phi3](../../../translated_images/fi/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/fi/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Tai jos haluat käyttää näkö- ja MoE-malleja, voit käyttää Microsoft Foundry -palvelua suorittaaksesi kutsut. Jos olet kiinnostunut, voit lukea Phi-3 CookBookin oppiaksesi kuinka kutsua Phi-3/3.5 Instruct, Vision ja MoE Microsoft Foundryn kautta [Klikkaa tästä linkistä](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Pilvipohjaisen Microsoft Foundry Models -luettelon lisäksi voit käyttää myös [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) suorittaaksesi aiheeseen liittyviä kutsuja. Voit vierailla NVIDIA NIM:ssä suorittaaksesi Phi-3/3.5-perheen API-kutsut. NVIDIA NIM (NVIDIA Inference Microservices) on joukko kiihdytettyjä inferenssimikropalveluita, joiden tarkoituksena on auttaa kehittäjiä ottamaan tekoälymallit käyttöön tehokkaasti eri ympäristöissä, mukaan lukien pilvet, datakeskukset ja työasemat.

Tässä muutamia NVIDIA NIM:n keskeisiä ominaisuuksia:

- **Helppo käyttöönotto:** NIM mahdollistaa tekoälymallien käyttöönoton yhdellä komennolla, mikä tekee sen integroinnista olemassa oleviin työnkulkuihin suoraviivaista.

- **Optimoitu suorituskyky:** Se hyödyntää NVIDIA:n esivalmistettuja inferenssimoottoreita, kuten TensorRT:tä ja TensorRT-LLM:ää, varmistaen matalan viiveen ja korkean läpimenon.
- **Skaalautuvuus:** NIM tukee automaattista skaalausta Kubernetesissa, mikä mahdollistaa erilaisten työkuormien tehokkaan käsittelyn.
- **Tietoturva ja hallinta:** Organisaatiot voivat pitää hallinnan omista tiedoistaan ja sovelluksistaan itse-isännöimällä NIM-mikropalveluita omalla hallinnoimallaan infrastruktuurilla.
- **Standardoidut rajapinnat:** NIM tarjoaa alan standardin mukaiset rajapinnat, jotka tekevät AI-sovellusten, kuten chatbotien, AI-avustajien ym. rakentamisesta ja integroinnista helppoa.

NIM on osa NVIDIA AI Enterprise -ohjelmistoa, jonka tavoitteena on yksinkertaistaa AI-mallien käyttöönottoa ja operointia, varmistaen niiden tehokkaan toiminnan NVIDIA:n GPU:illa.

- Demo: NVIDIA NIM:n käyttäminen Phi-3.5-Vision-API:n kutsumiseen [[Klikkaa tästä](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 ajaminen paikallisesti
Inferenssi Phi-3:n tai minkä tahansa kielimallin, kuten GPT-3:n, yhteydessä tarkoittaa vasteiden tai ennusteiden luomista annetun syötteen perusteella. Kun annat kehotteen tai kysymyksen Phi-3:lle, se käyttää koulutettua neuroverkkoaan arvioidakseen todennäköisimmän ja asiaankuuluvimman vastauksen analysoimalla koulutusdatassaan havaittuja malleja ja yhteyksiä.

**Hugging Face Transformer**
Hugging Face Transformers on tehokas kirjasto, joka on suunniteltu luonnollisen kielen käsittelyyn (NLP) ja muihin koneoppimistehtäviin. Tässä joitain keskeisiä kohtia siitä:

1. **Esikoulutetut mallit**: Se tarjoaa tuhansia valmiiksi koulutettuja malleja, joita voi käyttää erilaisissa tehtävissä, kuten tekstiluokittelussa, nimettyjen entiteettien tunnistuksessa, kysymyksiin vastaamisessa, tiivistämisessä, kääntämisessä ja tekstin generoinnissa.

2. **Kehysten yhteentoimivuus**: Kirjasto tukee useita syväoppimiskehyksiä, kuten PyTorchia, TensorFlow'ta ja JAX:ia. Tämä mahdollistaa mallin kouluttamisen yhdessä kehyksessä ja käytön toisessa.

3. **Monimuotoiset ominaisuudet**: NLP:n lisäksi Hugging Face Transformers tukee myös tietokonenäön tehtäviä (esim. kuvien luokittelu, kohteiden tunnistus) ja äänenkäsittelyä (esim. puheentunnistus, äänen luokittelu).

4. **Helppokäyttöisyys**: Kirjasto tarjoaa sovellusrajapintoja ja työkaluja mallien helppoon lataamiseen ja hienosäätöön, mikä tekee siitä saavutettavan sekä aloittelijoille että asiantuntijoille.

5. **Yhteisö ja resurssit**: Hugging Facella on elinvoimainen yhteisö sekä laaja dokumentaatio, opetusohjelmat ja oppaat, jotka auttavat käyttäjiä pääsemään alkuun ja hyödyntämään kirjastoa parhaalla mahdollisella tavalla.
[virallinen dokumentaatio](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) tai heidän [GitHub-repositorio](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Tämä on yleisimmin käytetty menetelmä, mutta se tarvitsee myös GPU-kiihdytyksen. Lopulta skenaariot kuten Vision ja MoE vaativat paljon laskentaa, mikä olisi hyvin hidasta CPU:lla, jos ne eivät ole kvantisoituja.


- Demo: Transformerilla Phi-3.5-Instruct -kutsun tekeminen [Klikkaa tästä](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformerilla Phi-3.5-Vision -kutsun tekeminen [Klikkaa tästä](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformerilla Phi-3.5-MoE -kutsun tekeminen [Klikkaa tästä](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) on alusta, joka on suunniteltu helpottamaan suurten kielimallien (LLM) ajoa paikallisesti omalla koneellasi. Se tukee erilaisia malleja, kuten Llama 3.1, Phi 3, Mistral ja Gemma 2. Alusta yksinkertaistaa prosessia niputtamalla mallipainot, konfiguraation ja datan yhteen pakettiin, tehden käyttäjille helpommaksi mukauttaa ja luoda omia mallejaan. Ollama on saatavilla macOS:lle, Linuxille ja Windowsille. Se on erinomainen työkalu, jos haluat kokeilla tai ottaa käyttöön LLM-malleja ilman pilvipalveluihin tukeutumista. Ollama on suorin tapa, sinun tarvitsee vain suorittaa seuraava komento.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) on Microsoftin offline- ja laitteistolla ajettava ympäristö, jolla voi ajaa malleja kuten Phi täysin omalla laitteistollasi – ei tarvitse Azure-tilausta, API-avainta tai verkkoyhteyttä. Se valitsee automaattisesti parhaan suorituskykyyn soveltuvan ajon tarjoajan (NPU, GPU tai CPU) ja tarjoaa OpenAI-yhteensopivan päätepisteen, joten olemassa oleva `openai`/Azure AI Inferenssi SDK -koodi voi käyttää sitä vähäisin muutoksin. Katso [Foundry Localin dokumentaatio](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) aloittaaksesi.

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

**ONNX Runtime generatiiviselle AI:lle**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) on monialustainen inferenssi- ja koneoppimismallien koulutuksen kiihdytin. ONNX Runtime generatiiviselle AI:lle (GENAI) on tehokas työkalu, joka auttaa sinua ajamaan generatiivisia AI-malleja tehokkaasti eri alustoilla.

## Mikä on ONNX Runtime?
ONNX Runtime on avoimen lähdekoodin projekti, joka mahdollistaa koneoppimismallien suorittamisen suurella suorituskyvyllä. Se tukee Open Neural Network Exchange (ONNX) -muodossa olevia malleja, joka on standardi koneoppimismallien esittämiseen. ONNX Runtime -inferenssi voi mahdollistaa nopeammat asiakaskokemukset ja pienemmät kustannukset, tukiessaan malleja syväoppimiskehyksistä kuten PyTorch ja TensorFlow/Keras sekä klassisia koneoppimiskirjastoja kuten scikit-learn, LightGBM, XGBoost ym. ONNX Runtime on yhteensopiva eri laitteistojen, ajurien ja käyttöjärjestelmien kanssa, tarjoten optimaalisen suorituskyvyn hyödyntämällä laitteistokiihdyttimiä soveltuvin osin yhdessä graafin optimointien ja muunnosten kanssa.

## Mikä on generatiivinen AI?
Generatiivinen AI tarkoittaa AI-järjestelmiä, jotka voivat tuottaa uutta sisältöä, kuten tekstiä, kuvia tai musiikkia, koulutusdatansa perusteella. Esimerkkejä ovat kielimallit kuten GPT-3 ja kuvageneraatiomallit kuten Stable Diffusion. ONNX Runtime for GenAI -kirjasto tarjoaa generatiivisen AI:n silmukan ONNX-malleille, mukaan lukien inferenssin ONNX Runtime -ympäristössä, logitien käsittelyn, haun ja näytteenoton sekä KV-välimuistin hallinnan.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI laajentaa ONNX Runtimen kykyjä tukemaan generatiivisia AI-malleja. Tässä on joitakin keskeisiä ominaisuuksia:

- **Laaja alustan tuki:** Se toimii useilla alustoilla, mukaan lukien Windows, Linux, macOS, Android ja iOS.
- **Mallien tuki:** Se tukee monia suosittuja generatiivisia AI-malleja, kuten LLaMA, GPT-Neo, BLOOM ja muita.
- **Suorituskyvyn optimointi:** Se sisältää optimointeja eri laitteistokiihdyttimille kuten NVIDIA:n GPU:t, AMD:n GPU:t ja muita2.
- **Helppokäyttöisyys:** Se tarjoaa API-rajapintoja helppoa integrointia varten sovelluksiin, jolloin voit generoida tekstiä, kuvia ja muuta sisältöä vähäisellä koodilla.
- Käyttäjät voivat kutsua korkean tason generate()-metodia tai suorittaa mallin jokaisen iteraation silmukassa generoiden aina yhden tokenin kerrallaan ja tarvittaessa päivittämällä generointiparametreja silmukan sisällä.
- ONNX Runtimella on myös tuki ahneelle/sädehaulle ja TopP, TopK -näytteistämiselle tokeneiden jonoja generoiden sekä sisäänrakennettu logitien käsittely kuten toistokieltoja. Voit myös helposti lisätä omia pisteytysmalleja.

## Aloittaminen
Aloittaaksesi ONNX Runtime for GENAI:n kanssa voit noudattaa seuraavia vaiheita:

### Asenna ONNX Runtime:
```Python
pip install onnxruntime
```
### Asenna Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Aja malli: Tässä yksinkertainen esimerkki Pythonissa:
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
### Demo: ONNX Runtime GenAI:n käyttäminen Phi-3.5-Vision kutsuun


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

ONNX Runtime, Ollama ja Foundry Local -viittausmenetelmien lisäksi voimme myös täydentää kvantitatiivisten mallien referenssejä eri valmistajien tarjoamien mallimenetelmien perusteella. Esimerkiksi Apple MLX -kehys Applen Metallilla, Qualcomm QNN NPU:lla, Intel OpenVINO CPU/GPU:lla jne. Saat lisää sisältöä myös [Phi-3 Cookbookista](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).


## Lisää

Olemme oppineet Phi-3/3.5-perheen perusteet, mutta oppiaksemme enemmän SLM:stä tarvitsemme lisätietoa. Vastausten löytämiseen voi hyödyntää Phi-3 Cookbookia. Jos haluat oppia lisää, käy [Phi-3 Cookbookissa](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->