# Johdanto pieniin kielimalleihin generatiivisessa tekoälyssä aloittelijoille
Generatiivinen tekoäly on kiehtova tekoälyn osa-alue, joka keskittyy järjestelmien luomiseen, jotka pystyvät tuottamaan uutta sisältöä. Tämä sisältö voi vaihdella tekstistä ja kuvista musiikkiin ja jopa kokonaisiin virtuaaliympäristöihin. Yksi jännittävimmistä generatiivisen tekoälyn sovelluksista on kielimallien alueella.

## Mitä ovat pienet kielimallit?

Pieni kielimalli (SLM) edustaa suurista kielimalleista (LLM) skaalattua pienempää versiota, hyödyntäen monia LLM:ien arkkitehtonisia periaatteita ja tekniikoita samalla kun hiukan vähentää laskennallista jalanjälkeä.

SLM:t ovat kielimalleja, jotka on suunniteltu tuottamaan ihmismäistä tekstiä. Toisin kuin suuremmat mallinsa, kuten GPT-4, SLM:t ovat kompakteja ja tehokkaita, mikä tekee niistä ihanteellisia sovelluksissa, joissa laskentaresurssit ovat rajalliset. Vaikka ne ovat pienempiä, ne pystyvät edelleen suorittamaan monenlaisia tehtäviä. Tyypillisesti SLM:t rakennetaan pakkaamalla tai tiivistämällä LLM:ejä, tavoitellen alkuperäisen mallin toiminnallisuuden ja kielitaidon suurta säilyttämistä. Mallin koon pienentäminen vähentää kokonaiskompleksisuutta, tehden SLM:istä tehokkaampia sekä muistinkäytön että laskentavaatimusten osalta. Näistä optimoinneista huolimatta SLM:t kykenevät edelleen suorittamaan laajan valikoiman luonnollisen kielen käsittelyn (NLP) tehtäviä:

- Tekstin generointi: Koherenttien ja kontekstuaalisesti relevanttien lauseiden tai kappaleiden luominen.
- Tekstin täydentäminen: Lauseiden ennustaminen ja täydentäminen annetun kehotteen perusteella.
- Kääntäminen: Tekstin muuntaminen kielestä toiseen.
- Tiivistäminen: Pitkien tekstien tiivistäminen lyhyemmiksi, helpommin omaksuttaviksi yhteenvetoiksi.

Vaikkakin suorituksessa tai ymmärryksen syvyydessä on joitakin kompromisseja verrattuna suurempiin malleihin.

## Miten pienet kielimallit toimivat?
SLM:t koulutetaan valtavissa tekstidatamäärissä. Koulutuksen aikana ne oppivat kielen kaavat ja rakenteet, mikä mahdollistaa kieliopillisesti oikean ja kontekstuaalisesti sopivan tekstin tuottamisen. Koulutusprosessiin kuuluu:

- Datan keruu: Suurten tekstidatasetsien kerääminen eri lähteistä.
- Esikäsittely: Datan puhdistaminen ja järjestäminen koulutusta varten sopivaksi.
- Koulutus: Koneoppimisalgoritmien käyttäminen mallin opettamiseksi ymmärtämään ja tuottamaan tekstiä.
- Hienosäätö: Mallin säätäminen parantamaan sen suorituskykyä tietyissä tehtävissä.

SLM:ien kehitys vastaa kasvavaan tarpeeseen malleista, joita voi ottaa käyttöön resurssirajoitetuissa ympäristöissä, kuten mobiililaitteissa tai reunalaskennassa, missä täysimittaiset LLM:t voivat olla epäkäytännöllisiä raskaan resurssien vaatimuksen vuoksi. Tehokkuuteen keskittyen SLM:t tasapainottavat suorituskyvyn ja saavutettavuuden, mahdollistaen laajemman soveltamisen eri aloilla.

![slm](../../../translated_images/fi/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Oppimistavoitteet

Tässä oppitunnissa pyrimme esittelemään SLM:n tiedon ja yhdistämään sen Microsoft Phi-3:n kanssa oppiaksemme erilaisia skenaarioita tekstisisällössä, näössä ja MoE:ssa.

Oppitunnin lopussa sinun pitäisi pystyä vastaamaan seuraaviin kysymyksiin:

- Mitä on SLM?
- Mikä on ero SLM:n ja LLM:n välillä?
- Mikä on Microsoft Phi-3/3.5 -perhe?
- Kuinka suorittaa inferenssi Microsoft Phi-3/3.5 -perheen malleilla?

Valmiina? Aloitetaan.

## Erot suurten kielimallien (LLM) ja pienten kielimallien (SLM) välillä

Sekä LLM:t että SLM:t perustuvat todennäköisyyksiä hyödyntävään koneoppimiseen, noudattaen samankaltaisia lähestymistapoja arkkitehtuurissa, koulutusmenetelmissä, datan generointiprosesseissa ja mallin arvioinnissa. Kuitenkin useat keskeiset tekijät erottavat nämä kaksi mallityyppiä.

## Pienten kielimallien sovellukset

SLM:illä on laaja sovellusalue, mukaan lukien:

- Chatbotit: Asiakastuen tarjoaminen ja käyttäjien kanssa keskustelu vuorovaikutteisesti.
- Sisällöntuotanto: Kirjoittajien avustaminen ideoiden generoinnissa tai jopa kokonaisten artikkeleiden luonnostelussa.
- Koulutus: Opiskelijoiden auttaminen kirjoitustehtävissä tai uusien kielten oppimisessa.
- Saavutettavuus: Työkalujen luominen vammaisille, kuten tekstistä puheeksi -järjestelmät.

**Koko**
  
Keskeinen ero LLM:ien ja SLM:ien välillä on mallien mittakaavassa. LLM:t, kuten ChatGPT (GPT-4), voivat sisältää arviolta 1,76 biljoonaa parametria, kun taas avoimen lähdekoodin SLM:t, kuten Mistral 7B, on suunniteltu paljon vähemmillä parametreilla — noin 7 miljardia. Tämä ero johtuu pääasiassa mallin arkkitehtuurin ja koulutusprosessien eroista. Esimerkiksi ChatGPT käyttää itsehuomiomekanismia kooderi-dekooderi-rakenteessa, kun taas Mistral 7B hyödyntää liukuvalla ikkunalla varustettua huomiomekanismia, mikä mahdollistaa tehokkaamman koulutuksen pelkästään dekooderipohjaisessa mallissa. Tämä arkkitehtoninen ero vaikuttaa merkittävästi mallin kompleksisuuteen ja suorituskykyyn.

**Ymmärrys**

SLM:t on tyypillisesti optimoitu toimimaan hyvin tietyillä aloilla, mikä tekee niistä erittäin erikoistuneita mutta mahdollisesti rajallisia laajemman asiayhteyden ymmärtämisessä monilla tieteenaloilla. Toisaalta LLM:t pyrkivät simuloimaan ihmismäistä älykkyyttä laajemmassa mittakaavassa. Koulutettuina valtavilla, monipuolisilla dataseteillä LLM:t on suunniteltu toimimaan hyvin monilla aloilla, tarjoten suurempaa monipuolisuutta ja sopeutumiskykyä. Näin ollen LLM:t soveltuvat paremmin monenlaisiin jälkikäsittelytehtäviin, kuten luonnollisen kielen käsittelyyn ja ohjelmointiin.

**Laskenta**

LLM:ien koulutus ja käyttöönotto ovat resurssi-intensiivisiä prosesseja, jotka usein vaativat merkittävää laskenta-infrastruktuuria, kuten suuria GPU-klustereita. Esimerkiksi ChatGPT:n kaltaisen mallin kouluttaminen alusta asti voi vaatia tuhansia GPU:ita pitkien jaksojen ajan. SLM:t, pienempien parametrimäärien ansiosta, ovat helpommin saavutettavissa laskentaresurssien suhteen. Mallit kuten Mistral 7B voidaan kouluttaa ja käyttää paikallisilla koneilla, joissa on kohtuulliset GPU-ominaisuudet, vaikkakin koulutus vaatii silti useiden tuntien ajanjakson useilla GPU:illa.

**Vinouma**

Vinouma on tunnettu ongelma LLM:issä, pääasiassa koulutusdatan luonnon vuoksi. Nämä mallit usein luottavat internetistä saatavaan raakaan ja avoimeen dataan, joka voi aliedustaa tai vääristää tiettyjä ryhmiä, sisältää virheellisiä luokituksia tai heijastaa kielivääristymiä, joita vaikuttavat murteet, maantieteelliset erot ja kielioppisäännöt. Lisäksi LLM:ien arkkitehtuurin monimutkaisuus voi tahattomasti pahentaa vinoumasta johtuvia ongelmia, jotka saattavat jäädä huomaamatta ilman huolellista hienosäätöä. Toisaalta, SLM:t, jotka on koulutettu rajatummilla, alakohtaisilla dataseteillä, ovat luontaisesti vähemmän alttiita tällaisille vinoumille, vaikka eivät ole immuuneja niille.

**Inferenssi**

Pienemmät SLM:t tarjoavat merkittävän edun inferenssin nopeudessa, antaen niiden generoida tulosteita tehokkaasti paikallisella laitteistolla ilman laajamittaista rinnakkaislaskentaa. Toisin kuin LLM:t, joiden koko ja monimutkaisuus vaativat usein merkittäviä rinnakkaisia laskentaresursseja hyväksyttävien vasteaikojen saavuttamiseksi. Useiden samanaikaisten käyttäjien läsnäolo hidastaa entisestään LLM:ien vasteaikoja erityisesti suurissa käyttöönottoympäristöissä.

Yhteenvetona, vaikka sekä LLM:t että SLM:t perustuvat koneoppimisen perustekniikoihin, ne eroavat merkittävästi mallin koon, resurssivaatimusten, asiayhteyden ymmärryksen, vinouman alttiuden ja inferenssin nopeuden suhteen. Nämä erot heijastavat niiden soveltuvuutta erilaisiin käyttötarkoituksiin, joissa LLM:t ovat monipuolisempia mutta resurssi-intensiivisempiä ja SLM:t tarjoavat alakohtaista tehokkuutta pienemmillä laskentaresurssivaatimuksilla.

***Huomautus: Tässä oppitunnissa esittelemme SLM:n esimerkin avulla Microsoft Phi-3 / 3.5:n kautta.***

## Esittely Phi-3 / Phi-3.5 -perheestä

Phi-3 / 3.5 -perhe keskittyy pääasiassa tekstin, näön ja Agentin (MoE) sovellusskenaarioihin:

### Phi-3 / 3.5 Instruct

Pääasiassa tekstin generointiin, chatin täydentämiseen ja sisällön tietojen poimintaan, jne.

**Phi-3-mini**

3,8 miljardin parametrin kielimalli on saatavilla Microsoft Foundryssä, Hugging Facessa ja Ollamassa. Phi-3 -mallit ylittävät merkittävästi saman tai suuremman koon kielimallit tärkeimmissä vertailuissa (katso vertailuluvut alla, suuremmat luvut ovat parempia). Phi-3-mini päihittää kaksi kertaa suuremmat mallit, kun taas Phi-3-small ja Phi-3-medium päihittävät suuremmat mallit, mukaan lukien GPT-3.5.

**Phi-3-small & medium**

Vain 7 miljardilla parametrilla Phi-3-small voittaa GPT-3.5T useissa kielen, päättelyn, koodauksen ja matematiikan vertailuissa.

Phi-3-medium 14 miljardilla parametrilla jatkaa tätä trendiä ja päihittää Gemini 1.0 Pron.

**Phi-3.5-mini**

Voimme ajatella sitä Phi-3-minin päivityksenä. Vaikka parametrit pysyvät samoina, se parantaa kykyä tukea useita kieliä (tukee yli 20 kieltä: arabia, kiina, tsekki, tanska, hollanti, englanti, suomi, ranska, saksa, heprea, unkari, italia, japani, korea, norja, puola, portugali, venäjä, espanja, ruotsi, thai, turkki, ukraina) ja lisää vahvemman tuen pitkälle kontekstille.

Phi-3.5-mini 3,8 miljardilla parametrilla päihittää saman kokoiset kielimallit ja on tasoltaan kahdenkertaisia suurempien mallien kanssa.

### Phi-3 / 3.5 Vision

Voimme ajatella Phi-3/3.5 Instruct -mallia Phin kyvyksi ymmärtää, ja Vision antaa Phille silmät maailman ymmärtämiseen.


**Phi-3-Vision**

Phi-3-vision, vain 4,2 miljardilla parametrilla, jatkaa tätä kehitystä ja päihittää suuremmat mallit kuten Claude-3 Haiku ja Gemini 1.0 Pro V yleisissä visuaalisen päättelyn tehtävissä, OCR:ssa sekä taulukko- ja diagrammikäsittelyssä.


**Phi-3.5-Vision**

Phi-3.5-Vision on myös Phi-3-Visionin päivitys, joka lisää tuen useille kuville. Voit ajatella sitä näön parannuksena: voit nähdä paitsi kuvia myös videoita.

Phi-3.5-vision päihittää suuremmat mallit kuten Claude-3.5 Sonnet ja Gemini 1.5 Flash OCR:n, taulukoiden ja kaavioiden ymmärtämisen tehtävissä sekä on tasoltaan yleisessä visuaalisessa tietopäättelyssä. Tukee monikehyssyötettä, eli päättelyä useilla syötekuvilla.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** mahdollistaa mallien esikoulutuksen paljon pienemmin laskentakustannuksin, mikä tarkoittaa, että mallia tai datasetin kokoa voidaan kasvattaa dramaattisesti samalla laskentabudjetilla kuin tiheällä mallilla. Erityisesti MoE-mallin pitäisi saavuttaa tiheän vastineensa laatu paljon nopeammin esikoulutuksen aikana.

Phi-3.5-MoE koostuu 16x 3,8 miljardin parametrin ekspertimoduulista. Phi-3.5-MoE, jossa on vain 6,6 miljardia aktiivista parametria, saavuttaa saman tason päättelyssä, kielen ymmärryksessä ja matematiikassa kuin paljon suuremmat mallit.

Phi-3/3.5 -perheen malleja voidaan käyttää eri skenaarioissa. Toisin kuin LLM, voit ottaa käyttöön Phi-3/3.5-mini tai Phi-3/3.5-Vision reunalaitteissa.


## Kuinka käyttää Phi-3/3.5 -perheen malleja

Pyrimme käyttämään Phi-3/3.5 mallia eri tilanteissa. Seuraavaksi käytämme Phi-3/3.5 mallia eri skenaarioiden perusteella.

![phi3](../../../translated_images/fi/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferenssi pilvipalveluiden API:en kautta

**Microsoft Foundry -mallit**

> **Huom:** GitHub Models lopetetaan heinäkuun 2026 lopussa. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) on suora korvaaja.

> **Huom:** Koko Phi-3/3.5 -perhe (Instruct, Vision ja MoE -variantit) poistettiin Microsoft Foundry Models -katalogista 30.8.2025. Käytä siellä sen sijaan `Phi-4` (Instruct) tai `Phi-4-mini-instruct` — alla olevat Phi-3/3.5 -esimerkit toimivat yhä Hugging Facen, Ollaman, ONNX Runtime:n ja NVIDIA NIM:n kautta.

Microsoft Foundry Models tarjoaa nyt Phi-4 jatkajat. Käytä `Phi-4` tai `Phi-4-mini-instruct` Phi-3/3.5 mallien sijaan, kun seuraat pilvi-API-esimerkkejä.

- Demo: Vertailu Phi-3-mini ja Phi-3.5-mini vaikutuksista kiinalaisissa skenaarioissa

![phi3](../../../translated_images/fi/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/fi/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Jos haluat käyttää vision (multimodaalisia) malleja pilvessä, käytä tällä hetkellä saatavilla olevia `Phi-4-multimodal-instruct` Microsoft Foundryn kautta sen sijaan, että käyttäisit eläkkeelle siirrettyjä Phi-3/3.5 Vision -malleja; tekstitehtäviin käytä `Phi-4` tai `Phi-4-mini-instruct`. Phi-3.5 MoE -malli on poistettu Microsoft Foundrystä, joten käytä tässä oppitunnissa kuvattuja muita vaihtoehtoja (esimerkiksi Hugging Face), jos haluat kokeilla sitä. Jos olet kiinnostunut, voit lukea Phi Cookbookin oppiaksesi, miten kutsua Phi-malleja Microsoft Foundryn kautta [Napsauta tätä linkkiä](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Pilvipohjaisen Microsoft Foundryn malliluettelon lisäksi voit myös käyttää [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) suorittaaksesi niihin liittyviä kutsuja. Voit käydä NVIDIA NIM:ssä suorittamassa Phi-3/3.5-perheen API-kutsut. NVIDIA NIM (NVIDIA Inference Microservices) on joukko kiihdytettyjä päätelaitteiden mikro-palveluita, jotka on suunniteltu auttamaan kehittäjiä ottamaan AI-malleja käyttöön tehokkaasti eri ympäristöissä, mukaan lukien pilvet, datakeskukset ja työasemat.

Tässä on joitain NVIDIA NIM:n keskeisiä ominaisuuksia:

- **Helppo käyttöönotto:** NIM mahdollistaa tekoälymallien käyttöönoton yhdellä komennolla, mikä tekee siitä helppoa integroida olemassa oleviin työnkulkuihin.
- **Optimoitu suorituskyky:** Se hyödyntää NVIDIAn esiohjelmoituja päättelymoottoreita, kuten TensorRT ja TensorRT-LLM, varmistaakseen pienen viiveen ja korkean läpäisykyvyn.
- **Skaalautuvuus:** NIM tukee automaattista skaalausta Kubernetesissä, mahdollistaen vaihtelevien työkuormien tehokkaan käsittelyn.
- **Turvallisuus ja hallinta:** Organisaatiot voivat säilyttää hallinnan omiin tietoihinsa ja sovelluksiinsa itse isännöimällä NIM-mikropalveluita hallitulla infrastruktuurillaan.
- **Standardoidut API:t:** NIM tarjoaa alan standardien mukaisia API-rajapintoja, jotka helpottavat tekoälysovellusten, kuten chatbotien, AI-avustajien ja muiden, rakentamista ja integrointia.

NIM on osa NVIDIA AI Enterprisea, jonka tavoitteena on yksinkertaistaa tekoälymallien käyttöönottoa ja operatiivistamista varmistaen niiden tehokas toiminta NVIDIA GPU:illa.

- Demo: NVIDIA NIM:llä Phi-3.5-Vision-API:in kutsuminen  [[Klikkaa tästä](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5:n paikallinen ajaminen
Päättely Phi-3:n tai minkä tahansa kielimallin kuten GPT-3 yhteydessä viittaa prosessiin, jossa se tuottaa vastauksia tai ennusteita saamansa syötteen perusteella. Kun annat Phi-3:lle kehotteen tai kysymyksen, se käyttää koulutettua neuroverkkoaan ennustaakseen todennäköisimmän ja relevanteimman vastauksen analysoimalla koulutusdatansa kuvioita ja suhteita.

**Hugging Face Transformer**
Hugging Face Transformers on tehokas kirjasto, joka on suunniteltu luonnollisen kielen käsittelyyn (NLP) ja muihin koneoppimistehtäviin. Tässä joitakin keskeisiä seikkoja siitä:

1. **Esikoulutetut mallit**: Se tarjoaa tuhansia esikoulutettuja malleja erilaisiin tehtäviin, kuten tekstin luokitteluun, nimettyjen entiteettien tunnistukseen, kysymyksiin vastaamiseen, tiivistämiseen, kääntämiseen ja tekstin generointiin.

2. **Alustojen välinen yhteensopivuus:** Kirjasto tukee useita syväoppimiskehyksiä, mukaan lukien PyTorch, TensorFlow ja JAX. Tämä mahdollistaa mallin kouluttamisen yhdessä kehyksessä ja käytön toisessa.

3. **Monimodaaliset kyvyt:** NLP:n lisäksi Hugging Face Transformers tukee myös tietokonenäköön liittyviä tehtäviä (esim. kuvien luokittelu, kohteiden tunnistus) ja äänenkäsittelyä (esim. puheentunnistus, äänen luokittelu).

4. **Helppokäyttöisyys:** Kirjasto tarjoaa API-rajapintoja ja työkaluja mallien lataamiseen ja hienosäätöön, mikä tekee siitä saavutettavan sekä aloittelijoille että asiantuntijoille.

5. **Yhteisö ja resurssit:** Hugging Facella on aktiivinen yhteisö sekä laaja dokumentaatio, tutoriaalit ja oppaat, jotka auttavat käyttäjiä pääsemään alkuun ja hyödyntämään kirjastoa parhaalla mahdollisella tavalla.
[virallinen dokumentaatio](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) tai heidän [GitHub-repositoriosa](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Tämä on yleisimmin käytetty menetelmä, mutta se vaatii myös GPU-kiihdytyksen. Esimerkiksi Vision- ja MoE-skenaarioissa lasketaan paljon, mikä olisi hyvin hidasta CPU:lla, ellei niitä kvantisoida.


- Demo: Transformerilla Phi-3.5-Instructin kutsuminen [Klikkaa tästä](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformerilla Phi-3.5-Visionin kutsuminen [Klikkaa tästä](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformerilla Phi-3.5-MoE:n kutsuminen [Klikkaa tästä](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) on alusta, joka helpottaa suurten kielimallien (LLM) paikallista ajamista omalla koneellasi. Se tukee erilaisia malleja kuten Llama 3.1, Phi 3, Mistral ja Gemma 2, muiden muassa. Alusta yksinkertaistaa prosessia yhdistämällä mallin painot, konfiguraation ja datan yhteen pakettiin, mikä tekee sitä käyttäjille helpommin muokattavaksi ja omien mallien luomiseksi. Ollama on saatavilla macOS:lle, Linuxille ja Windowsille. Se on erinomainen työkalu, jos haluat kokeilla tai ottaa käyttöön LLM-malleja ilman pilvipalveluihin tukeutumista. Ollama on suoraviivaisin tapa, sinun tarvitsee vain suorittaa seuraava komento.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) on Microsoftin offline- ja laitteistokohtainen suoritusaikaympäristö, joka mahdollistaa Phi-mallien ajamisen kokonaan omalla laitteistollasi – ilman Azure-tilausta, API-avainta tai verkkoyhteyttä. Se valitsee automaattisesti parhaan käytettävissä olevan suoritussuorittajan (NPU, GPU tai CPU) ja tarjoaa OpenAI-yhteensopivan päätepisteen, joten olemassa oleva `openai`/Azure AI Inference SDK -koodi voi käyttää sitä vain vähäisin muutoksin. Katso [Foundry Local -dokumentaatio](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) aloittaaksesi.

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

**ONNX Runtime GenAI:lle**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) on alustojen välinen koneoppimisen päättely- ja koulutuskiihdytin. ONNX Runtime Generative AI:lle (GENAI) on tehokas työkalu, joka auttaa ajamaan generatiivisia tekoälymalleja tehokkaasti eri alustoilla.

## Mikä on ONNX Runtime?
ONNX Runtime on avoimen lähdekoodin projekti, joka mahdollistaa koneoppimismallien korkean suorituskyvyn päätelun. Se tukee Open Neural Network Exchange (ONNX) -muodossa olevia malleja, joka on koneoppimismallien standardimuoto. ONNX Runtime -päättely voi mahdollistaa nopeammat asiakaskokemukset ja pienemmät kustannukset, tuki malleille syväoppimiskehyksistä kuten PyTorch ja TensorFlow/Keras sekä perinteisille koneoppimiskirjastoille kuten scikit-learn, LightGBM, XGBoost jne. ONNX Runtime on yhteensopiva eri laitteistojen, ajurien ja käyttöjärjestelmien kanssa, ja tarjoaa optimaalisen suorituskyvyn hyödyntämällä laitteistokiihdyttimiä, kun mahdollista, yhdessä graafien optimointien ja muunnosten kanssa.

## Mikä on generatiivinen tekoäly?
Generatiivinen tekoäly viittaa tekoälyjärjestelmiin, jotka pystyvät tuottamaan uutta sisältöä, kuten tekstiä, kuvia tai musiikkia, perustuen koulutusdataansa. Esimerkkejä ovat kielimallit kuten GPT-3 ja kuvageneraatiomallit kuten Stable Diffusion. ONNX Runtime for GenAI -kirjasto tarjoaa generatiivisen AI-silmukan ONNX-malleille, sisältäen inference-vaiheen ONNX Runtime -alustalla, logitien käsittelyn, etsinnän ja satunnaisotannan sekä KV-välimuistin hallinnan.

## ONNX Runtime GENAI:lle
ONNX Runtime for GENAI laajentaa ONNX Runtime -alustan ominaisuuksia tukemaan generatiivisia AI-malleja. Tässä joitain keskeisiä ominaisuuksia:

- **Laaja alustatuki:** Se toimii useilla alustoilla, kuten Windows, Linux, macOS, Android ja iOS.
- **Mallituki:** Tukee monia suosittuja generatiivisia AI-malleja, kuten LLaMA, GPT-Neo, BLOOM ja muita.
- **Suorituskyvyn optimointi:** Sisältää optimointeja eri laitteistokiihdyttimille, kuten NVIDIA GPU:t, AMD GPU:t ja muita.
- **Helppokäyttöisyys:** Tarjoaa API-rajapinnat sovelluksiin integroitavaksi helposti, mahdollistaen tekstin, kuvien ja muun sisällön generoinnin vähällä koodilla.
- Käyttäjät voivat kutsua korkeantason generate()-metodia tai ajaa mallin jokaista iteraatiota silmukassa, generoiden yhden tokenin kerrallaan ja tarvittaessa päivittäen generointiparametreja silmukan sisällä.
- ONNX-runtime tukee myös ahne-/palkkihakua ja TopP, TopK -otantaa token-sekvenssien luomiseksi sekä sisäistä logitien käsittelyä, kuten toistuvuusrangaistuksia. Voit helposti lisätä myös omia arviointimenetelmiä.

## Aloittaminen
Aloittaaksesi ONNX Runtime for GENAI:n käytön, voit seurata näitä vaiheita:

### Asenna ONNX Runtime:
```Python
pip install onnxruntime
```
### Asenna Generative AI -laajennukset:
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
### Demo: ONNX Runtime GenAI:lla Phi-3.5-Vision kutsuminen


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

ONNX Runtimein, Ollaman ja Foundry Localin viite- / vertausmenetelmien lisäksi voimme täydentää määrällisten mallien viitettä eri valmistajien tarjoamien mallin viite -menetelmien perusteella. Esimerkiksi Apple MLX -kehys Apple Metallin kanssa, Qualcomm QNN NPU:n kanssa, Intel OpenVINO CPU/GPU:n kanssa jne. Löydät lisää sisältöä myös osoitteesta [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Lisää

Olemme oppineet perusasiat Phi-3/3.5 -perheestä, mutta oppiaksemme lisää SLM:stä tarvitsemme lisää tietoa. Vastaukset löydät Phi-3 Cookbookista. Jos haluat oppia lisää, käy osoitteessa [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->