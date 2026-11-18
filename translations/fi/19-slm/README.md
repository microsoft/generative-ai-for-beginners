# Johdanto pieniin kielimalleihin generatiivisessa tekoälyssä aloittelijoille
Generatiivinen tekoäly on kiehtova tekoälyn ala, joka keskittyy järjestelmien luomiseen, jotka kykenevät tuottamaan uutta sisältöä. Tämä sisältö voi vaihdella tekstistä ja kuvista musiikkiin ja jopa kokonaisiin virtuaaliympäristöihin. Yksi jännittävimmistä generatiivisen tekoälyn sovelluksista on kielimalleissa.

## Mitä ovat pienet kielimallit?

Pieni kielimalli (SLM) on pienennetty versio suuresta kielimallista (LLM), joka hyödyntää monia LLM:ien arkkitehtuuriperiaatteita ja tekniikoita, mutta jonka laskennallinen jalanjälki on merkittävästi pienempi.

Pienet kielimallit ovat kielimallien alajoukko, jotka on suunniteltu tuottamaan ihmismäistä tekstiä. Toisin kuin suuremmat mallinsa, kuten GPT-4, pienet kielimallit ovat kompakteja ja tehokkaita, mikä tekee niistä ihanteellisia sovelluksiin, joissa laskentaresurssit ovat rajalliset. Kooltaan pienempinä ne voivat silti suorittaa monenlaisia tehtäviä. Tyypillisesti pienet kielimallit rakennetaan puristamalla tai tiivistämällä LLM:iä, pyrkien säilyttämään suuri osa alkuperäisen mallin toiminnallisuudesta ja kielellisistä kyvyistä. Mallin koon pienentäminen vähentää kokonaiskompleksisuutta, mikä tekee pienistä kielimalleista tehokkaampia sekä muistinkäytön että laskentavaatimusten suhteen. Näistä optimoinneista huolimatta pienet kielimallit voivat suorittaa laajan valikoiman luonnollisen kielen käsittelyn (NLP) tehtäviä:

- Tekstin generointi: Koherenttien ja kontekstuaalisesti sopivien lauseiden tai kappaleiden luominen.
- Tekstin täydentäminen: Lauseiden ennustaminen ja täydentäminen annetun kehotteen perusteella.
- Kääntäminen: Tekstin muuntaminen kielestä toiseen.
- Tiivistäminen: Pitkien tekstien tiivistäminen lyhyemmiksi, helpommin sulatettaviksi yhteenvetoiksi.

Vaikkakin jotkin suorituskyvyn tai ymmärryksen syvyyden kompromissit verrattuna suurempiin malleihin.

## Kuinka pienet kielimallit toimivat?
Pienet kielimallit koulutetaan valtavilla tekstiaineistoilla. Koulutuksen aikana ne oppivat kielen kuvioita ja rakenteita, mikä mahdollistaa kieliopillisesti oikean ja kontekstuaalisesti sopivan tekstin tuottamisen. Koulutusprosessi sisältää:

- Datan keruu: Suurien tekstiaineistojen kokoaminen eri lähteistä.
- Esikäsittely: Datan puhdistaminen ja järjestäminen koulutusta varten sopivaksi.
- Koulutus: Koneoppimisalgoritmien käyttö mallin opettamiseen tekstin ymmärtämiseksi ja tuottamiseksi.
- Hienosäätö: Mallin säätäminen parantamaan suoriutumista tietyissä tehtävissä.

Pienten kielimallien kehitys vastaa kasvavaa tarvetta malleille, jotka voidaan ottaa käyttöön resurssirajoitetuissa ympäristöissä, kuten mobiililaitteissa tai reunalaskentaympäristöissä, joissa täysin laajamittaiset LLM:t voivat olla epäkäytännöllisiä niiden raskaan resurssitarpeen vuoksi. Keskittymällä tehokkuuteen, pienet kielimallit tasapainottavat suorituskykyä ja saavutettavuutta, mahdollistaen laajemman soveltamisen eri aloilla.

![slm](../../../translated_images/fi/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Oppimistavoitteet

Tässä oppitunnissa pyrimme esittelemään SLM:n tietämyksen ja yhdistämään sen Microsoft Phi-3:n kanssa oppiaksemme erilaisista teksti-, näkö- ja MoE-skenaarioista.

Oppitunnin lopussa sinun tulisi pystyä vastaamaan seuraaviin kysymyksiin:

- Mikä on SLM?
- Mikä on ero SLM:n ja LLM:n välillä?
- Mikä on Microsoft Phi-3/3.5 -perhe?
- Kuinka suorittaa inferenssi Microsoft Phi-3/3.5 -perheen kanssa?

Valmis? Aloitetaan.

## Erot suurten kielimallien (LLM) ja pienten kielimallien (SLM) välillä

Sekä LLM:t että SLM:t perustuvat todennäköisyyspohjaisiin koneoppimisen periaatteisiin, noudattavat samankaltaisia lähestymistapoja arkkitehtuurin suunnittelussa, koulutuksessa, datan generoinnissa ja mallien arvioinnissa. Kuitenkin useat keskeiset tekijät erottaa nämä kaksi mallityyppiä toisistaan.

## Pienten kielimallien sovellukset

Pienillä kielimalleilla on laaja sovellusalue, mukaan lukien:

- Chatbotit: Asiakastuen tarjoaminen ja käyttäjien kanssa keskusteleminen.
- Sisällöntuotanto: Kirjailijoiden auttaminen idea- ja kokonaisteosten laatimisessa.
- Koulutus: Opiskelijoiden auttaminen kirjoitustehtävissä tai uusien kielten oppimisessa.
- Toimintakyvyn tukeminen: Työkalujen luominen vammaisille henkilöille, kuten tekstistä puheeksi -järjestelmät.

**Koko**
  
Merkittävin ero LLM:ien ja SLM:ien välillä liittyy mallien kokoon. Suuret mallit, kuten ChatGPT (GPT-4), voivat sisältää arviolta 1,76 biljoonaa parametria, kun taas avoimen lähdekoodin pienet mallit, kuten Mistral 7B, on suunniteltu huomattavasti pienemmällä parametrimäärällä—noin 7 miljardia. Tämä ero johtuu pääasiassa eroista mallin arkkitehtuurissa ja koulutusprosesseissa. Esimerkiksi ChatGPT käyttää itsehuomio-mekanismia enkooderi-dekooderi-rakenteessa, kun taas Mistral 7B hyödyntää liukuvaa ikkunahuomiota, mikä mahdollistaa tehokkaamman koulutuksen dekooderipohjaisessa mallissa. Tämä arkkitehtoninen ero vaikuttaa voimakkaasti mallien monimutkaisuuteen ja suorituskykyyn.

**Ymmärrys**

Pienet kielimallit optimoidaan tyypillisesti suoriutumaan hyvin tietyillä aloilla, tehden niistä hyvin erikoistuneita mutta mahdollisesti rajallisia kyvyltään tarjota laajaa kontekstuaalista ymmärrystä useilla tieteenaloilla. Suuret kielimallit pyrkivät simuloimaan ihmismäistä älykkyyttä laajemmassa mittakaavassa. Laajojen ja monipuolisten aineistojen avulla koulutetut LLM:t suunnitellaan suoriutumaan hyvin monenlaisilla alueilla, tarjoten suurempaa monipuolisuutta ja mukautuvuutta. Tästä syystä LLM:t sopivat paremmin laajempaan valikoimaan jatkotehtäviä, kuten luonnollisen kielen käsittelyyn ja ohjelmointiin.

**Laskenta**

LLM:ien koulutus ja käyttöönotto ovat resurssisyöppöjä prosesseja, jotka usein vaativat merkittävää laskentainfrastruktuuria, mukaan lukien suuria GPU-klustereita. Esimerkiksi ChatGPT:n kaltaisen mallin opettaminen alusta asti voi vaatia tuhansia GPU:ita pitkien aikojen kuluessa. Verrattuna tähän pienet kielimallit, joiden parametrimäärä on huomattavasti pienempi, ovat saavutettavampia laskentaresurssien suhteen. Mistral 7B:n kaltaiset mallit voidaan kouluttaa ja ajaa paikallisilla koneilla, joissa on kohtuulliset GPU-ominaisuudet, vaikka koulutus vaatiikin useita tunteja usean GPU:n avulla.

**Vinouma**

Vinouma on tunnettu ongelma LLM:issä, pääosin koulutusdatan luonteen vuoksi. Nämä mallit käyttävät usein raakaa, avoimesti saatavilla olevaa internetdataa, joka voi aliedustaa tai vääristää tiettyjä ryhmiä, sisältää virheellisiä merkintöjä tai heijastaa kielellisiä vinoumia, joita vaikuttavat murteet, maantieteelliset vaihtelut ja kielioppisäännöt. Lisäksi LLM-arkkitehtuurien monimutkaisuus voi tahattomasti pahentaa vinoumaa, joka voi jäädä huomaamatta ilman huolellista hienosäätöä. Toisaalta pienet kielimallit, jotka koulutetaan rajatummille, alakohtaisille aineistoille, ovat luontaisesti vähemmän alttiita tällaisille vinoumille, vaikka eivät täysin immuuneja niille.

**Inferenssi**

Pienempään kokoon perustuva SLM antaa merkittävän edun inferenssin nopeudessa, mahdollistaen tulosten tehokkaan tuottamisen paikallisessa laitteistossa ilman laajaa rinnakkaislaskentaa. Suuret kielimallit puolestaan vaativat kokonsa ja kompleksisuutensa vuoksi yleensä huomattavia rinnakkaisia laskentaresursseja saavuttaakseen hyväksyttävät inferenssiajat. Useiden samanaikaisten käyttäjien läsnäolo hidastaa myös LLM:ien vastausaikoja, erityisesti laajassa käytössä.

Yhteenvetona, vaikka LLM:t ja SLM:t jakavat koneoppimisen perustan, ne eroavat merkittävästi mallin koon, resurssivaatimusten, kontekstuaalisen ymmärryksen, vinouman alttiuden ja inferenssin nopeuden suhteen. Nämä erot heijastavat mallien sopivuutta eri käyttötarkoituksiin: LLM:t ovat monipuolisempia mutta resurssi-intensiivisiä ja SLM:t tarjoavat alakohtaista tehokkuutta pienemmällä laskentavaatimuksella.

***Huomautus: Tässä oppitunnissa esittelemme SLM:n esimerkkinä Microsoft Phi-3 / 3.5 -mallin avulla.***

## Phi-3 / Phi-3.5 -perheen esittely

Phi-3 / 3.5 -perhe kohdistuu pääasiassa tekstin, näön ja Agentin (MoE) sovellusskenaarioihin:

### Phi-3 / 3.5 Instruct

Pääasiassa tekstin generointiin, keskustelun täydentämiseen ja sisällön tiedon poimintaan yms.

**Phi-3-mini**

3,8 miljardin parametrin kielimalli on saatavilla Microsoft Foundryssä, Hugging Facessa ja Ollamassa. Phi-3 -mallit päihittävät merkittävästi saman kokoiset ja suuremmat kielimallit tärkeissä vertailuissa (katso vertailuluvut alla, korkeammat numerot ovat parempia). Phi-3-mini ylittää kaksi kertaa suuremmat mallit, kun taas Phi-3-small ja Phi-3-medium päihittävät suuremmat mallit, mukaan lukien GPT-3.5.

**Phi-3-small & medium**

Phi-3-small, jossa on vain 7 miljardia parametria, päihittää GPT-3.5T useissa kieli-, päättely-, koodaus- ja matemaattisissa vertailuissa.

Phi-3-medium 14 miljardilla parametrilla jatkaa tätä trendiä ja päihittää Gemini 1.0 Pron.

**Phi-3.5-mini**

Voimme ajatella sitä Phi-3-mini:n päivityksenä. Parametrit pysyvät samoina, mutta kyky tukea useita kieliä paranee (tukee 20+ kieltä: arabia, kiina, tšekki, tanska, hollanti, englanti, suomi, ranska, saksa, heprea, unkari, italia, japani, korea, norja, puola, portugali, venäjä, espanja, ruotsi, thai, turkki, ukraina) sekä pitkän kontekstin tuki vahvistuu.

Phi-3.5-mini 3,8 miljardilla parametrilla päihittää saman kokoiset kielimallit ja on tasavertainen kaksi kertaa suurempien mallien kanssa.

### Phi-3 / 3.5 Vision

Voimme ajatella Phi-3/3.5 Instruct -mallia Phin kyvyksi ymmärtää, ja Vision antaa Phille silmät maailman ymmärtämiseen.


**Phi-3-Vision**

Phi-3-vision, jolla on vain 4,2 miljardia parametria, jatkaa tätä kehitystä ja päihittää suuremmat mallit kuten Claude-3 Haiku ja Gemini 1.0 Pro V yleisissä visuaalisissa päättelytehtävissä, OCR:ssä sekä taulukko- ja diagrammin ymmärtämisessä.


**Phi-3.5-Vision**

Phi-3.5-Vision on myös Phi-3-Visionin päivitys, joka lisää tukea useille kuville. Voit ajatella sitä visuaalisena parannuksena: sen avulla ei voi vain nähdä kuvia, vaan myös videoita.

Phi-3.5-vision päihittää suuremmat mallit kuten Claude-3.5 Sonnet ja Gemini 1.5 Flash OCR-, taulukko- ja kaavioiden ymmärtämistehtävissä ja on tasavertainen yleisissä visuaalisen tiedon päättelytehtävissä. Tukee monikehyssyötettä eli pystyy päättelyyn useista syötekuvista.


### Phi-3.5-MoE

***Ekspertsejen sekoitus (MoE)*** mahdollistaa mallien esikouluttamisen huomattavasti vähemmällä laskentateholla, mikä tarkoittaa, että mallin tai datamäärän kokoa voi skaalata dramaattisesti samalla laskentabudjetilla kuin tiheällä mallilla. Erityisesti MoE-malli saavuttaa saman laadun kuin tiheä vastinparinsa paljon nopeammin esikoulutuksen aikana.

Phi-3.5-MoE koostuu 16x3,8 miljardin ekspertimoduulista. Phi-3.5-MoE, jolla on vain 6,6 miljardia aktiivista parametria, saavuttaa saman tason päättelyssä, kielen ymmärryksessä ja matematiikassa kuin paljon suuremmat mallit.

Voimme käyttää Phi-3/3.5 -perheen malleja eri skenaarioiden perusteella. Toisin kuin LLM, Phi-3/3.5-mini tai Phi-3/3.5-Vision voidaan ottaa käyttöön reunalaitteissa.


## Kuinka käyttää Phi-3/3.5 -perheen malleja

Pyrimme käyttämään Phi-3/3.5 eri skenaarioissa. Seuraavaksi käytämme Phi-3/3.5 eri tilanteissa.

![phi3](../../../translated_images/fi/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferenssi pilvipalvelujen API:en kautta

**Microsoft Foundry -mallit**

> **Huom:** GitHub Models lopetetaan heinäkuun 2026 lopussa. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) on suora korvaaja.

> **Huom:** Koko Phi-3/3.5-perhe (Instruct-, Vision- ja MoE-versiot) poistettiin Microsoft Foundry Models -katalogista 30.8.2025. Käytä siellä sen sijaan `Phi-4` (Instruct) tai `Phi-4-mini-instruct` — alla olevat Phi-3/3.5-esimerkit toimivat edelleen Hugging Facen, Ollaman, ONNX Runtime:n ja NVIDIA NIM:n kautta.

Microsoft Foundry Models tarjoaa nyt Phi-4:n seuraajat. Käytä `Phi-4` tai `Phi-4-mini-instruct` sen sijaan, että käyttäisit poistettuja Phi-3/3.5-malleja pilvi-API-esimerkeissä.

- Demo: Phi-3-mini- ja Phi-3.5-mini-mallien vaikutusten vertailu kiinankielisissä tilanteissa

![phi3](../../../translated_images/fi/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/fi/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Jos haluat käyttää visiota (monimodaalisia) malleja pilvessä, käytä Microsoft Foundryn kautta nykyisiä `Phi-4-multimodal-instruct` sen sijaan, että käyttäisit poistettuja Phi-3/3.5 Vision -malleja; tekstitehtäviin käytä `Phi-4` tai `Phi-4-mini-instruct`. Phi-3.5 MoE -malli on poistettu Microsoft Foundrysta, joten kokeillaksesi sitä käytä tämän oppitunnin muita vaihtoehtoja (esim. Hugging Face). Jos olet kiinnostunut, voit lukea Phi Cookbookin oppiaksesi, miten Phi-malleja kutsutaan Microsoft Foundryn kautta [Klikkaa tätä linkkiä](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Pilvipohjaisen Microsoft Foundry Models -katalogin lisäksi voit käyttää [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) suorittaaksesi vastaavia kutsuja. Voit käyttää NVIDIA NIM:ää Phi-3/3.5-perheen API-kutsujen suorittamiseen. NVIDIA NIM (NVIDIA Inference Microservices) on joukko kiihtyneitä inference-mikropalveluita, jotka on suunniteltu auttamaan kehittäjiä mallien tehokkaassa käyttöönotossa eri ympäristöissä, mukaan lukien pilvet, datakeskukset ja työasemat.

Tässä on joitakin NVIDIA NIM:n keskeisiä ominaisuuksia:

- **Helppo käyttöönotto:** NIM mahdollistaa tekoälymallien käyttöönoton yhdellä komennolla, mikä tekee siitä helpon integroida olemassa oleviin työnkulkuihin.
- **Optimoitu suorituskyky:** Se hyödyntää NVIDIAn esivalmisteltuja inferenssimoottoreita, kuten TensorRT:tä ja TensorRT-LLM:ää, varmistaen pienen viiveen ja suuren läpimenon.
- **Skaalautuvuus:** NIM tukee automaattista skaalausta Kubernetesissa, mahdollistaen vaihtelevien työkuormien tehokkaan hallinnan.
- **Turvallisuus ja hallinta:** Organisaatiot voivat ylläpitää hallintaa omiin tietoihinsa ja sovelluksiinsa itse isännöimällä NIM-mikropalveluja omassa hallinnoidussa infrastruktuurissaan.
- **Standardoidut rajapinnat:** NIM tarjoaa alan standardien mukaisia API-rajapintoja, mikä helpottaa tekoälysovellusten, kuten chatbotien ja tekoälyavustajien, rakentamista ja integrointia.

NIM on osa NVIDIA AI Enterprise -pakettia, jonka tavoitteena on yksinkertaistaa tekoälymallien käyttöönottoa ja operointia, varmistaen niiden tehokkaan toiminnan NVIDIA:n suorittimilla.

- Demo: Käyttämällä NVIDIA NIM:ää Phi-3.5-Vision-API:n kutsumiseen [[Napsauta tätä linkkiä](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 ajaminen paikallisesti
Inferenssi Phi-3:n tai minkä tahansa kielimallin, kuten GPT-3:n, yhteydessä tarkoittaa prosessia, jossa generoidaan vastauksia tai ennusteita saatujen syötteiden perusteella. Kun annat kehotteen tai kysymyksen Phi-3:lle, se käyttää opetettua neuroverkkoaan päättelemään todennäköisimmän ja relevantin vastauksen analysoimalla malleja ja suhteita koulutusdatassa.

**Hugging Face Transformer**
Hugging Face Transformers on tehokas kirjasto, joka on suunniteltu luonnollisen kielen prosessointiin (NLP) ja muihin koneoppimistehtäviin. Tässä joitakin keskeisiä kohtia:

1. **Esikoulutetut mallit**: Se tarjoaa tuhansia esikoulutettuja malleja, joita voi käyttää erilaisiin tehtäviin, kuten tekstiluokitteluun, nimettyjen entiteettien tunnistukseen, kysymysten vastaukseen, tiivistämiseen, kääntämiseen ja tekstin generointiin.

2. **Kehyksen yhteensopivuus**: Kirjasto tukee useita syväoppimisen kehyksiä, kuten PyTorchia, TensorFlow'ta ja JAXia. Tämä mahdollistaa mallin kouluttamisen yhdessä kehyksessä ja käyttämisen toisessa.

3. **Monimodaaliset kyvyt**: NLP:n lisäksi Hugging Face Transformers tukee tehtäviä myös konenäössä (esim. kuvien luokittelu, kohteiden tunnistus) ja äänen käsittelyssä (esim. puheen tunnistus, äänen luokittelu).

4. **Helppokäyttöisyys**: Kirjasto tarjoaa rajapinnat ja työkalut, joilla mallit voi helposti ladata ja hienosäätää, tehden siitä saavutettavan sekä aloittelijoille että asiantuntijoille.

5. **Yhteisö ja resurssit**: Hugging Facella on aktiivinen yhteisö sekä laaja dokumentaatio, opetusohjelmat ja oppaat, jotka auttavat käyttäjiä alkuun ja hyödyntämään kirjastoa parhaalla mahdollisella tavalla.
[virallinen dokumentaatio](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) tai heidän [GitHub-repositorio](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Tämä on yleisimmin käytetty menetelmä, mutta se vaatii myös GPU-kiihdytyksen. Esimerkiksi Vision- ja MoE-skenaariot tarvitsevat paljon laskentaa, mikä olisi erittäin hidasta CPU:lla ilman kvantisointia.


- Demo: Transformer-kirjaston käyttö Phi-3.5-Instruct kutsuun [Napsauta tätä linkkiä](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer-kirjaston käyttö Phi-3.5-Vision kutsuun [Napsauta tätä linkkiä](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer-kirjaston käyttö Phi-3.5-MoE kutsuun [Napsauta tätä linkkiä](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) on alusta, joka on suunniteltu helpottamaan suurten kielimallien (LLM) paikallista ajoa omalla koneellasi. Se tukee monia malleja, kuten Llama 3.1, Phi 3, Mistral ja Gemma 2, muiden muassa. Alusta yksinkertaistaa prosessia paketoimalla mallipainot, konfiguraation ja datan yhdeksi paketiksi, tehden mallien räätälöinnistä ja luomisesta helpompaa käyttäjille. Ollama on saatavilla macOS:lle, Linuxille ja Windowsille. Se on loistava työkalu, jos haluat kokeilla tai ottaa käyttöön LLM:iä ilman pilvipalveluihin tukeutumista. Ollama on kaikkein suoraviivaisin tapa, tarvitsee vain suorittaa seuraava komento.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) on Microsoftin offline- ja laitepohjainen runtime-ympäristö, jolla voi ajaa malleja, kuten Phi, kokonaan omalla laitteistollasi – ei tarvitse Azure-tilausta, API-avainta tai verkkoyhteyttä. Se valitsee automaattisesti parhaan suoritustuen (NPU, GPU tai CPU) ja tarjoaa OpenAI-yhteensopivan päätepisteen, joten olemassa oleva `openai`/Azure AI Inference SDK-koodi voi käyttää sitä vähin muutoksin. Katso [Foundry Local -dokumentaatio](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) aloittaaksesi.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) on monialustainen inferenssi- ja koulutusnopeuttaja koneoppimiseen. ONNX Runtime for Generative AI (GENAI) on tehokas työkalu, joka auttaa suorittamaan generatiivisen tekoälyn malleja tehokkaasti eri alustoilla.

## Mikä on ONNX Runtime?
ONNX Runtime on avoimen lähdekoodin projekti, joka mahdollistaa koneoppimismallien korkean suorituskyvyn inferenssin. Se tukee Open Neural Network Exchange (ONNX) -muodossa olevia malleja, joka on standardi koneoppimismallien esittämiselle. ONNX Runtime inferenssi voi nopeuttaa asiakaskokemusta ja alentaa kustannuksia, tukien malleja syväoppimisen kehyksistä kuten PyTorch ja TensorFlow/Keras sekä perinteisistä koneoppimiskirjastoista kuten scikit-learn, LightGBM, XGBoost jne. ONNX Runtime on yhteensopiva eri laitteistojen, ajurien ja käyttöjärjestelmien kanssa, ja tarjoaa optimaalisen suorituskyvyn hyödyntämällä laitteistokiihdyttimiä sekä graafien optimointeja ja muunnoksia.

## Mikä on Generatiivinen tekoäly?
Generatiivinen tekoäly tarkoittaa tekoälyjärjestelmiä, jotka pystyvät luomaan uutta sisältöä, kuten tekstiä, kuvia tai musiikkia, koulutusdatansa perusteella. Esimerkkejä ovat kielimallit kuten GPT-3 ja kuvageneraatiomallit kuten Stable Diffusion. ONNX Runtime for GenAI -kirjasto tarjoaa generatiivisen tekoälyn silmukan ONNX-malleille, mukaan lukien inferenssi ONNX Runtime -ympäristössä, logitien käsittelyn, haun ja näytteenoton sekä KV-välimuistin hallinnan.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI laajentaa ONNX Runtimen kykyjä tukemaan generatiivisia tekoälymalleja. Tässä joitakin keskeisiä ominaisuuksia:

- **Laaja alustan tuki:** Se toimii useilla alustoilla, kuten Windows, Linux, macOS, Android ja iOS.
- **Mallien tuki:** Se tukee monia suosittuja generatiivisia tekoälymalleja, kuten LLaMA, GPT-Neo, BLOOM ja muita.
- **Suorituskyvyn optimointi:** Siihen sisältyy optimointeja eri laitteistokiihdyttimille, kuten NVIDIA- ja AMD-GPU:ille ja muille.
- **Helppokäyttöisyys:** Se tarjoaa rajapintoja sovelluksiin integrointiin, mahdollistaen tekstin, kuvien ja muun sisällön generoinnin vähäisellä koodilla.
- Käyttäjät voivat kutsua korkean tason generate()-metodia tai ajaa mallin jokaisen iteraation silmukassa, generoiden yhden tokenin kerrallaan ja tarvittaessa päivittäen generointiparametreja silmukan sisällä.
- ONNX Runtime tukee myös ahnetta/kehähakua ja TopP, TopK -näytteenottoa token-sekvenssien generointiin sekä sisäänrakennettua logits-käsittelyä, kuten toistuvuusrangaistuksia. Mukana on myös helppo tapa lisätä mukautettu pisteytys.

## Aloittaminen
Aloittaaksesi ONNX Runtime for GENAI:n kanssa voit seurata näitä vaiheita:

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
### Demo: Käyttämällä ONNX Runtime GenAI:ta Phi-3.5-Vision kutsuun


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

ONNX Runtimein, Ollaman ja Foundry Local -viitemenetelmien lisäksi voimme täydentää myös kvantitatiivisten mallien viitetietoa eri valmistajien tarjoamien malliviitemenetelmien perusteella. Kuten Apple MLX -kehys Apple Metalin kanssa, Qualcomm QNN NPU:n kanssa, Intel OpenVINO CPU/GPU:n kanssa jne. Voit myös saada lisää sisältöä osoitteesta [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Lisää

Olemme oppineet Phi-3/3.5 -perheen perusteet, mutta oppiaksemme lisää SLM:stä tarvitsemme enemmän tietoa. Vastauksia löydät Phi-3 Cookbookista. Jos haluat oppia lisää, käy osoitteessa [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->