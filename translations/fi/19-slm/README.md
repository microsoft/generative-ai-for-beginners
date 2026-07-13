# Johdanto pieniin kielimalleihin generatiivisessa tekoälyssä aloittelijoille
Generatiivinen tekoäly on kiehtova tekoälyn osa-alue, joka keskittyy järjestelmien luomiseen, jotka pystyvät generoimaan uutta sisältöä. Tämä sisältö voi vaihdella tekstistä ja kuvista musiikkiin ja jopa kokonaisiin virtuaaliympäristöihin. Yksi generatiivisen tekoälyn jännittävimmistä sovelluksista on kielimallien alueella.

## Mitä ovat pienet kielimallit?

Pieni kielimalli (Small Language Model, SLM) edustaa kooltaan pienennettyä versiota suuresta kielimallista (Large Language Model, LLM), hyödyntäen monia LLM:ien arkkitehtuuriperiaatteita ja -tekniikoita, mutta osoittaen merkittävästi pienemmän laskennallisen jalanjäljen.

SLM:t ovat kielimalleja, jotka on suunniteltu tuottamaan ihmismäistä tekstiä. Toisin kuin suuremmat vastineensa, kuten GPT-4, SLM:t ovat kompakteja ja tehokkaita, mikä tekee niistä ihanteellisia sovelluksiin, joissa laskentaresurssit ovat rajalliset. Pienestä koosta huolimatta ne pystyvät suorittamaan monenlaisia tehtäviä. Tyypillisesti SLM:t rakennetaan puristamalla tai tiivistämällä LLM:iä, pyrkien säilyttämään huomattava osa alkuperäisen mallin toiminnallisuudesta ja kielitaidoista. Mallin koon pienentäminen vähentää kokonaiskomplikaatiota, tehden SLM:istä tehokkaampia sekä muistin käytön että laskennallisten vaatimusten osalta. Näistä optimoinneista huolimatta SLM:t pystyvät suorittamaan laajan valikoiman luonnollisen kielen käsittelyn (NLP) tehtäviä:

- Tekstin luominen: Yhtenäisten ja kontekstuaalisesti relevanttien lauseiden tai kappaleiden tuottaminen.
- Tekstin täydentäminen: Lauseiden ennustaminen ja täydentäminen annettuun kehotteeseen perustuen.
- Kääntäminen: Tekstin muuntaminen kielestä toiseen.
- Yhteenvedon tekeminen: Pitkien tekstien tiivistäminen lyhyemmiksi, helpommin omaksuttaviksi yhteenvetoiksi.

Vaikkakin jonkin verran suorituskyvyn tai syvällisen ymmärryksen kaltaisilla kompromisseilla verrattuna suurempiin malleihin.

## Kuinka pienet kielimallit toimivat?
SLM:t koulutetaan valtavilla tekstimassoilla. Koulutuksen aikana ne oppivat kielen kaavat ja rakenteet, jolloin ne pystyvät tuottamaan sekä kieliopillisesti oikeaa että kontekstuaalisesti sopivaa tekstiä. Koulutusprosessiin kuuluu:

- Datan keruu: Suurten tekstidatamassojen kokoaminen eri lähteistä.
- Esikäsittely: Datan puhdistaminen ja järjestäminen koulutusta varten sopivaksi.
- Koulutus: Koneoppimisalgoritmien käyttäminen mallin opettamiseen tekstin ymmärtämisestä ja tuottamisesta.
- Hienosäätö: Mallin säätäminen parantamaan sen suorituskykyä tiettyjen tehtävien osalta.

SLM:ien kehitys vastaa kasvavaa tarvetta malleille, jotka voidaan ottaa käyttöön resurssirajoitetuissa ympäristöissä, kuten mobiililaitteissa tai reunalaskentaympäristöissä, joissa täysimittaiset LLM:t voivat olla epäkäytännöllisiä raskaan resurssinkulutuksensa takia. Tehokkuuteen keskittyen SLM:t tasapainottavat suorituskykyä saavutettavuuden kanssa, mahdollistaen laajemman soveltamisen eri alueilla.

![slm](../../../translated_images/fi/slm.4058842744d0444a.webp)

## Oppimistavoitteet

Tämän oppitunnin tavoitteena on tutustuttaa SLM:ään ja yhdistää se Microsoft Phi-3:n kanssa, oppien erilaisia skenaarioita tekstisisällössä, näkökyvyssä ja MoE:ssa.

Oppitunnin lopussa sinun tulisi osata vastata seuraaviin kysymyksiin:

- Mikä on SLM?
- Mikä on ero SLM:n ja LLM:n välillä?
- Mikä on Microsoft Phi-3/3.5 -perhe?
- Kuinka tehdä inferenssi Microsoft Phi-3/3.5 -perheen kanssa?

Valmis? Aloitetaan.

## Erot suurten kielimallien (LLM) ja pienten kielimallien (SLM) välillä

Sekä LLM:t että SLM:t perustuvat todennäköisyyspohjaisen koneoppimisen periaatteisiin, noudattaen samankaltaisia lähestymistapoja arkkitehtuurin suunnittelussa, koulutusmenetelmissä, datan generointiprosesseissa ja mallin arvioinnissa. Kuitenkin useat keskeiset tekijät erottavat nämä kaksi mallityyppiä.

## Pienten kielimallien sovellukset

SLM:illä on laaja sovellusvalikoima, mukaan lukien:

- Chatbotit: Asiakastuen tarjoaminen ja käyttäjien kanssa keskusteleminen.
- Sisällöntuotanto: Kirjoittajien auttaminen ideoiden generoinnissa tai jopa kokonaisten artikkeleiden luonnostelussa.
- Koulutus: Opiskelijoiden auttaminen kirjoitustehtävissä tai uusien kielten oppimisessa.
- Saavutettavuus: Työkalujen luominen vammaisille, kuten puheentunnistuksen ja -muunnoksen järjestelmät.

**Koko**

Keskeinen ero LLM:ien ja SLM:ien välillä on mallien mittakaavassa. LLM:t, kuten ChatGPT (GPT-4), voivat koostua arvioiduista 1,76 biljoonasta parametristä, kun taas avoimen lähdekoodin SLM:t, kuten Mistral 7B, on suunniteltu huomattavasti pienemmällä parametrimäärällä — noin 7 miljardia. Tämä ero johtuu ensisijaisesti malliarkkitehtuurin ja koulutusprosessin eroista. Esimerkiksi ChatGPT käyttää itsehuomiointimekanismia enkooderi-dekooderi-rakenteessa, kun taas Mistral 7B hyödyntää liukuvaikkuna-huomiota, mikä mahdollistaa tehokkaamman koulutuksen pelkästään dekooderipohjaisessa mallissa. Tämä arkkitehtuurinen ero vaikuttaa merkittävästi mallien kompleksisuuteen ja suorituskykyyn.

**Ymmärrys**

SLM:t on tyypillisesti optimoitu suorituskyvyn osalta tietyissä alueilla, mikä tekee niistä hyvin erikoistuneita, mutta mahdollisesti rajoittaa niiden kykyä tarjota laajaa kontekstuaalista ymmärrystä monilla tieteenaloilla. Sen sijaan LLM:t pyrkivät simuloimaan ihmismäistä älykkyyttä monipuolisemmalla tasolla. Koulutettuina laajoilla, monipuolisilla datamassoilla, LLM:t on suunniteltu toimimaan hyvin monilla aloilla tarjoten suurempaa monipuolisuutta ja sopeutumiskykyä. Täten LLM:t soveltuvat laajempaan valikoimaan jälkikäteisiä tehtäviä, kuten luonnollisen kielen käsittelyyn ja ohjelmointiin.

**Laskenta**

LLM:ien koulutus ja käyttö ovat resurssikriittisiä prosesseja, jotka usein vaativat merkittäviä laskenta-infrastruktuureja, kuten suuria GPU-klustereita. Esimerkiksi ChatGPT:n kaltaisen mallin kouluttaminen alusta alkaen saattaa vaatia tuhansia GPU-yksiköitä pitkien aikajaksojen ajan. Vastaavasti SLM:t, joiden parametrimäärät ovat pienemmät, ovat laskentaresurssien suhteen saavutettavampia. Mallit kuten Mistral 7B voidaan kouluttaa ja ajaa paikallisilla koneilla, joissa on kohtuulliset GPU-ominaisuudet, vaikka koulutus vaatiikin useita tunteja usean GPU:n voimin.

**Harha**

Harha on tunnettu ongelma LLM:issä, joka johtuu ensisijaisesti koulutusdatan laadusta. Nämä mallit käyttävät usein raakaa, avoimesti saatavilla olevaa internet-dataa, joka saattaa aliedustaa tai vääristää tiettyjä ryhmiä, sisältää virheellisiä merkintöjä tai heijastaa kielellisiä harhoja, jotka johtuvat murteista, maantieteellisistä vaihteluista ja kieliopillisista säännöistä. Lisäksi LLM-arkkitehtuurien monimutkaisuus voi tahattomasti pahentaa harhoja, jotka voivat jäädä huomaamatta ilman tarkkaa hienosäätöä. Toisaalta SLM:t, joita koulutetaan rajatuilla, alakohtaisilla tietoaineistoilla, ovat luonnostaan vähemmän alttiita tällaisille harhoille, vaikka ne eivät ole täysin immuuneja niille.

**Inferenssi**

SLM:ien pienempi koko antaa niille merkittävän edun inferenssin nopeudessa, mahdollistaen tulosteiden tehokkaan generoinnin paikallisessa laitteistossa ilman laajaa rinnakkaiskäsittelyä. LLM:t puolestaan vaativat koonsa ja monimutkaisuutensa vuoksi usein huomattavia rinnakkaisia laskentaresursseja saavuttaakseen hyväksyttävät inferenssiajat. Useiden samanaikaisten käyttäjien läsnäolo heikentää entisestään LLM:ien vasteaikoja etenkin laajamittaisessa käytössä.

Yhteenvetona, vaikka sekä LLM:t että SLM:t perustuvat koneoppimisen periaatteisiin, ne eroavat merkittävästi mallin koon, resurssivaatimusten, kontekstuaalisen ymmärryksen, harhalle altistumisen ja inferenssin nopeuden osalta. Nämä erot heijastavat niiden soveltuvuutta eri käyttötarkoituksiin: LLM:t ovat monipuolisempia mutta resursseja kuluttavia, kun taas SLM:t tarjoavat alakohtaista tehokkuutta pienemmillä laskentaresursseilla.

***Huom: Tässä oppitunnissa esittelemme SLM:n Microsoft Phi-3 / 3.5 -malliston avulla esimerkkinä.***

## Phi-3 / Phi-3.5 -perheen esittely

Phi-3 / 3.5 -perhe on suunnattu pääasiassa tekstin, näkymän ja Agent (MoE) sovellusskenaarioihin:

### Phi-3 / 3.5 Instruct

Pääasiassa tekstin generointiin, chat-keskusteluiden täydentämiseen ja sisällön tietojen poimintaan yms.

**Phi-3-mini**

3,8 miljardin parametrin kielimalli on saatavilla Microsoft Azure AI Studiosta, Hugging Facesta ja Ollamasta. Phi-3 -mallit ylittävät merkittävästi saman kokoiset ja suuremmat kielimallit avaintuloksissa (katso seuraavat vertailuluvut, suuremmat luvut ovat parempia). Phi-3-mini päihittää kaksinkertaista kokoa vastaavat mallit, kun taas Phi-3-small ja Phi-3-medium ylittävät suuremmat mallit, mukaan lukien GPT-3.5.

**Phi-3-small & medium**

Vain 7 miljardilla parametrilla Phi-3-small voittaa GPT-3.5T useilla kieli-, päättely-, koodaus- ja matematiikkatestilaudoilla.

Phi-3-medium 14 miljardilla parametrilla jatkaa tätä linjaa ja päihittää Gemini 1.0 Pro:n.

**Phi-3.5-mini**

Voidaan ajatella Phi-3-mini:n päivitettynä versiona. Parametrit pysyvät ennallaan, mutta parannetaan kykyä tukea useita kieliä (yli 20 kieltä: arabia, kiina, tsekki, tanska, hollanti, englanti, suomi, ranska, saksa, heprea, unkari, italia, japani, korea, norja, puola, portugali, venäjä, espanja, ruotsi, thai, turkki, ukraina) ja lisätään vahvempi tuki pitkälle kontekstille.

Phi-3.5-mini, jossa on 3,8 miljardia parametria, päihittää saman kokoiset kielimallit ja on samalla tasolla kaksinkertaisia kooltaan olevien mallien kanssa.

### Phi-3 / 3.5 Vision

Voimme ajatella Phi-3/3.5 Instruct -mallia Phin kyvyksi ymmärtää, ja Visionia, joka antaa Phille silmät ymmärtää maailmaa.

**Phi-3-Vision**

Phi-3-vision, jossa on vain 4,2 miljardia parametria, jatkaa tätä suuntausta ja päihittää suurempia malleja, kuten Claude-3 Haiku ja Gemini 1.0 Pro V, yleisissä visuaalisen päättelyn, OCR:n sekä taulukoiden ja diagrammien ymmärtämisen tehtävissä.

**Phi-3.5-Vision**

Phi-3.5-Vision on myös päivitys Phi-3-Visionista, lisäten tuen useammalle kuvalle. Voit ajatella tätä parannuksena näkökykyyn; voit nähdä paitsi kuvia myös videoita.

Phi-3.5-vision päihittää suurempia malleja, kuten Claude-3.5 Sonnet ja Gemini 1.5 Flash OCR:ssa, taulukkojen ja kaavioiden ymmärtämisessä sekä yleisessä visuaalisen tiedon päättelyssä. Tukee monikehyksistä syötettä, eli suorittaa päättelyä useilla syöttökuvilla.

### Phi-3.5-MoE

***Eksperttiseoksen (Mixture of Experts, MoE)*** avulla malleja voidaan esikouluttaa huomattavasti vähemmällä laskennalla, mikä tarkoittaa, että voit skaalata mallin tai datamäärän kokoa dramaattisesti samalla laskentabudjetilla kuin tiheä malli. Erityisesti MoE-mallin pitäisi saavuttaa sama laatu kuin tiheän mallin vastine paljon nopeammin esikoulutuksen aikana.

Phi-3.5-MoE koostuu 16:sta 3,8 miljardin parametrin asiantuntijamoduulista. Phi-3.5-MoE, jossa on vain 6,6 miljardia aktiivista parametria, saavuttaa saman tason päättelyssä, kielten ymmärryksessä ja matematiikassa kuin paljon suuremmat mallit.

Voimme käyttää Phi-3/3.5-perheen malleja eri skenaarioiden mukaan. Toisin kuin LLM:t, voit ottaa Phi-3/3.5-mini- tai Phi-3/3.5-Vision-mallin käyttöön reunalaitteissa.

## Kuinka käyttää Phi-3/3.5 -perheen malleja

Toivomme käyttävämme Phi-3/3.5 eri skenaarioissa. Seuraavaksi käytämme Phi-3/3.5 eri skenaarioiden pohjalta.

![phi3](../../../translated_images/fi/phi3.655208c3186ae381.webp)

### Inferenssi pilvi-API:en kautta

**GitHub Models**

GitHub Models on kaikkein suoraviivaisin tapa. Voit nopeasti käyttää Phi-3/3.5-Instruct-mallia GitHub Modelsin kautta. Yhdistettynä Azure AI Inference SDK:han tai OpenAI SDK:han, voit tehdä API-kutsun koodilla Phi-3/3.5-Instruct-mallille. Voit testata eri tuloksia myös Playgroundin kautta.

- Demo: Vertailu Phi-3-mini:n ja Phi-3.5-mini:n vaikutuksista kiinankielisissä skenaarioissa

![phi3](../../../translated_images/fi/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/fi/gh2.07d7985af66f178d.webp)


**Azure AI Studio**

Tai jos haluamme käyttää näkymä- ja MoE-malleja, voit käyttää Azure AI Studiota kutsujen tekemiseen. Jos olet kiinnostunut, voit lukea Phi-3 Cookbookin oppiaksesi kuinka kutsua Phi-3/3.5 Instruct-, Vision- ja MoE-malleja Azure AI Studion kautta [Klikkaa tätä linkkiä](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Azure- ja GitHub-pohjaisten pilvipalveluiden lisäksi voit käyttää myös [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) -ratkaisua liittyvien kutsujen tekemiseen. Voit vierailla NVIDIA NIM:ssä ja hoitaa Phi-3/3.5 -perheen API-kutsut. NVIDIA NIM (NVIDIA Inference Microservices) on joukko kiihdytettyjä inferenssimikropalveluja, joiden tarkoituksena on auttaa kehittäjiä ottamaan tekoälymalleja käyttöön tehokkaasti eri ympäristöissä, mukaan lukien pilvet, datakeskukset ja työasemat.

Tässä muutamia NVIDIA NIM:n keskeisiä ominaisuuksia:

- **Helppo käyttöönotto:** NIM mahdollistaa tekoälymallien käyttöönoton yhdellä komennolla, tehden integraatiosta yksinkertaista olemassa oleviin työnkulkuihin.
- **Optimoitu suorituskyky:** Se hyödyntää NVIDIAn esivalmiiksi optimoituja inferenssimoottoreita, kuten TensorRT:tä ja TensorRT-LLM:ää, varmistaen matalan viiveen ja korkean läpimenon.
- **Skaalautuvuus:** NIM tukee Kubernetes-autoskaalausta, mikä mahdollistaa tehokkaan työkuormien käsittelyn.
- **Turvallisuus ja hallinta:** Organisaatiot voivat säilyttää hallinnan tietoihinsa ja sovelluksiinsa itse isännöimällä NIM-mikropalveluita omalla hallinnoimallaan infrastruktuurilla.
- **Standardoidut API:t:** NIM tarjoaa teollisuusstandardin mukaiset API:t, joiden avulla on helppo rakentaa ja integroida tekoälysovelluksia, kuten chatbotteja, tekoälyavustajia ja muita.

NIM on osa NVIDIA AI Enterprise -ohjelmaa, jonka tavoitteena on yksinkertaistaa tekoälymallien käyttöönottoa ja operatiivista hallintaa, varmistaen että ne toimivat tehokkaasti NVIDIA:n GPU:illa.

- Demo: NVIDIA NIM:n käyttäminen Phi-3.5-Vision-API:n kutsumiseen  [[Klikkaa tästä](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 ajaminen paikallisesti
Päätelmällä Phi-3:n tai minkä tahansa kielimallin, kuten GPT-3:n, yhteydessä tarkoitetaan vastausten tai ennusteiden tuottamisprosessia syötteen perusteella. Kun annat kehotteen tai kysymyksen Phi-3:lle, se käyttää koulutettua neuroverkkoaan päätelläkseen todennäköisimmän ja merkityksellisimmän vastauksen analysoimalla malliin koulutettua dataa koskevia kuvioita ja suhteita.

**Hugging Face Transformer**
Hugging Face Transformers on tehokas kirjasto, joka on suunniteltu luonnollisen kielen käsittelyyn (NLP) ja muihin koneoppimistehtäviin. Tässä on joitakin keskeisiä seikkoja siitä:

1. **Esikoulutetut mallit**: Se tarjoaa tuhansia esikoulutettuja malleja, joita voidaan käyttää erilaisiin tehtäviin, kuten tekstiluokitteluun, nimettyjen entiteettien tunnistukseen, kysymyksiin vastaamiseen, yhteenvedon tekemiseen, kääntämiseen ja tekstin generointiin.

2. **Kehyksen yhteensopivuus**: Kirjasto tukee useita syväoppimiskehyksiä, mukaan lukien PyTorch, TensorFlow ja JAX. Tämä mahdollistaa mallin kouluttamisen yhdessä kehyksessä ja sen käytön toisessa.

3. **Monimodaaliset kyvyt**: NLP:n lisäksi Hugging Face Transformers tukee tehtäviä myös konenäössä (esim. kuvaluokittelu, kohteen tunnistus) ja äänikäsittelyssä (esim. puheentunnistus, ääniluokittelu).

4. **Helppokäyttöisyys**: Kirjasto tarjoaa API:t ja työkalut mallien lataamiseen ja hienosäätöön, tehden siitä saavutettavan niin aloittelijoille kuin asiantuntijoille.

5. **Yhteisö ja resurssit**: Hugging Facella on vilkas yhteisö sekä laaja dokumentaatio, opetusohjelmat ja oppaat, jotka auttavat käyttäjiä pääsemään alkuun ja hyödyntämään kirjastoa parhaalla mahdollisella tavalla.
[virallinen dokumentaatio](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) tai heidän [GitHub-repositorionsa](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Tämä on yleisimmin käytetty menetelmä, mutta se vaatii myös GPU-kiihdytyksen. Etenkin Vision- ja MoE-tyyppiset skenaariot tarvitsevat paljon laskentatehoa, joka on CPU:lla erittäin hidasta ellei malleja ole kvantisoitu.

- Demo: Transformerilla Phi-3.5-Instructin kutsuminen [Klikkaa tästä](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformerilla Phi-3.5-Visionin kutsuminen [Klikkaa tästä](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformerilla Phi-3.5-MoEn kutsuminen [Klikkaa tästä](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) on alusta, joka on suunniteltu helpottamaan suurten kielimallien (LLM) paikallista suorittamista koneellasi. Se tukee useita malleja, kuten Llama 3.1, Phi 3, Mistral ja Gemma 2. Alusta yksinkertaistaa prosessia paketoimalla mallipainot, konfiguraation ja datan yhdeksi kokonaisuudeksi, tehden käyttäjille helpommaksi mukauttaa ja luoda omia malleja. Ollama on saatavilla macOS:lle, Linuxille ja Windowsille. Se on erinomainen työkalu, jos haluat kokeilla tai ottaa käyttöön LLM:iä ilman pilvipalveluihin tukeutumista. Ollama on kaikkein suoraviivaisin tapa, tarvitsee vain ajaa seuraava komento.


```bash

ollama run phi3.5

```


**ONNX Runtime GenAI:lle**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) on alustojen välinen suorituskyvyn ja koulutuksen kiihtyvyysmoottori koneoppimisessa. ONNX Runtime Generative AI (GENAI) on tehokas työkalu, joka auttaa ajamaan generatiivisia tekoälymalleja tehokkaasti eri alustoilla.

## Mikä on ONNX Runtime?
ONNX Runtime on avoimen lähdekoodin projekti, joka mahdollistaa koneoppimismallien korkeasuorituskykyisen päättelemisen. Se tukee Open Neural Network Exchange (ONNX) -muodossa olevia malleja, joka on standardi koneoppimismallien esittämiselle. ONNX Runtime:n päättelemistä voidaan käyttää asiakaskokemuksen nopeuttamiseen ja kustannusten alentamiseen tukemalla malleja syväoppimiskehyksistä kuten PyTorch ja TensorFlow/Keras sekä klassisista koneoppimiskirjastoista kuten scikit-learn, LightGBM, XGBoost jne. ONNX Runtime toimii eri laitteistoilla, ajureilla ja käyttöjärjestelmissä, tarjoten optimaalisen suorituskyvyn hyödyntämällä laitteistokiihdyttimiä tarpeen mukaan sekä graafien optimointeja ja muunnoksia.

## Mikä on generatiivinen tekoäly?
Generatiivinen tekoäly tarkoittaa tekoälyjärjestelmiä, jotka pystyvät tuottamaan uutta sisältöä, kuten tekstiä, kuvia tai musiikkia, koulutusdatansa pohjalta. Esimerkkejä ovat kielimallit kuten GPT-3 ja kuvanluontimallit kuten Stable Diffusion. ONNX Runtime for GenAI -kirjasto tarjoaa generatiivisen tekoälyn silmukan ONNX-malleille, mukaan lukien päättelemisen ONNX Runtime -moottorilla, logits-käsittelyn, haun ja näytteenoton sekä KV-välimuistin hallinnan.

## ONNX Runtime GENAI:lle
ONNX Runtime for GENAI laajentaa ONNX Runtime -moottorin ominaisuuksia tukemaan generatiivisia tekoälymalleja. Tässä muutamia avainominaisuuksia:

- **Laaja alustatuki:** Se toimii monilla alustoilla, kuten Windows, Linux, macOS, Android ja iOS.
- **Mallien tuki:** Se tukee monia suosittuja generatiivisia tekoälymalleja, kuten LLaMA, GPT-Neo, BLOOM ja muita.
- **Suorituskyvyn optimointi:** Mukana on optimointeja eri laitteistokiihdyttimille kuten NVIDIA GPU:t, AMD GPU:t ja muita2.
- **Helppokäyttöisyys:** Tarjolla on API:t helppoon integrointiin sovelluksiin, joiden avulla voi generoida tekstiä, kuvia ja muuta sisältöä vähällä koodilla.
- Käyttäjät voivat kutsua korkean tason generate()-metodia tai ajaa mallin joka toiston silmukassa, generoiden yhtä tokenia kerrallaan ja tarvittaessa päivittäen generointiparametreja silmukan sisällä.
- ONNX Runtime tukee myös ahne-/sädehakua sekä TopP- ja TopK-näytteenottoa token-jaksojen luomiseksi ja sisäistä logits-käsittelyä kuten toistokieltoja. Voit myös helposti lisätä omia pisteytystoimintoja.

## Aloittaminen
Aloittaaksesi ONNX Runtime for GENAI:n käytön, voit suorittaa seuraavat vaiheet:

### Asenna ONNX Runtime:
```Python
pip install onnxruntime
```
### Asenna Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Aja malli: Tässä yksinkertainen esimerkki Pythonilla:
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
### Demo: ONNX Runtime GenAI:n käyttäminen Phi-3.5-Visionin kutsumiseen


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

ONNX Runtime- ja Ollama-viitemenetelmien lisäksi voimme täydentää kvantitatiivisten mallien viitteitä eri valmistajien tarjoamien malliviitemenetelmien perusteella. Esimerkiksi Apple MLX -kehys Apple Metalilla, Qualcomm QNN NPU:lla, Intel OpenVINO CPU/GPU:lla jne. Voit myös saada lisää sisältöä Phi-3 Cookbookista [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Lisää

Olemme oppineet Phi-3/3.5 -perheen perusteet, mutta oppiaksemme lisää SLM:stä tarvitsemme laajempaa tietämystä. Vastauksia löydät Phi-3 Cookbookista. Jos haluat oppia lisää, käy osoitteessa [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->