# Johdanto pieniin kielimalleihin generatiivisen tekoälyn maailmassa aloittelijoille
Generatiivinen tekoäly on kiehtova tekoälyn ala, joka keskittyy järjestelmien luomiseen, jotka kykenevät tuottamaan uutta sisältöä. Tämä sisältö voi vaihdella tekstistä ja kuvista musiikkiin ja jopa kokonaisiin virtuaaliympäristöihin. Yksi mielenkiintoisimmista generatiivisen tekoälyn sovelluksista on kielimalleissa.

## Mitä ovat pienet kielimallit?

Pieni kielimalli (SLM) on pienennetty versio suuresta kielimallista (LLM), joka hyödyntää monia LLM:ien arkkitehtuurisia periaatteita ja tekniikoita, mutta jolla on merkittävästi pienempi laskennallinen jalanjälki.

SLM:t ovat kielimalleihin kuuluva alatyyppi, jotka on suunniteltu tuottamaan ihmismäistä tekstiä. Toisin kuin suuremmat vastineensa, kuten GPT-4, SLM:t ovat kompakteja ja tehokkaita, minkä vuoksi ne sopivat ihanteellisesti sovelluksiin, joissa laskentaresurssit ovat rajalliset. Pienestä koosta huolimatta ne pystyvät suorittamaan erilaisia tehtäviä. Tyypillisesti SLM:t rakennetaan puristamalla tai tislaten LLM:iä, pyrkien säilyttämään suuri osa alkuperäisen mallin toiminnallisuudesta ja kielellisistä kyvyistä. Mallin koon pienentäminen vähentää kokonaiskomplikaatiota tehden SLM:istä tehokkaampia sekä muistinkulutuksen että laskentavaatimusten osalta. Näistä optimoinneista huolimatta SLM:t pystyvät suorittamaan laajan valikoiman luonnollisen kielen käsittelyn (NLP) tehtäviä:

- Tekstin generointi: Yhtenäisten ja kontekstuaalisesti relevanttien lauseiden tai kappaleiden luominen.
- Tekstin täydentäminen: Lauseiden ennustaminen ja täydentäminen annetun kehotteen perusteella.
- Kääntäminen: Tekstin muuntaminen kielestä toiseen.
- Tiivistäminen: Pitkien tekstien tiivistäminen lyhyemmiksi, helpommin omaksuttaviksi yhteenvetoiksi.

Vaikka suorituskyvystä tai ymmärryksen syvyydestä joudutaan tekemään joitain kompromisseja verrattuna suurempiin malleihin.

## Kuinka pienet kielimallit toimivat?
SLM:t koulutetaan suurilla määrillä tekstidataa. Koulutuksen aikana ne oppivat kielen rakenteita ja kuvioita mahdollistaen tekstin tuottamisen, joka on sekä kieliopillisesti oikein että kontekstuaalisesti sopivaa. Koulutusprosessiin kuuluu:

- Datan kerääminen: Suurten tekstidatasetien kerääminen eri lähteistä.
- Esikäsittely: Datan puhdistaminen ja järjestäminen koulutukseen soveltuvaksi.
- Koulutus: Koneoppimisalgoritmien käyttäminen mallin opettamiseksi tekstin ymmärtämiseen ja tuottamiseen.
- Hienosäätö: Mallin säätäminen tiettyjen tehtävien suorituskyvyn parantamiseksi.

SLM:ien kehitys vastaa kasvavaa tarvetta malleille, jotka voidaan ottaa käyttöön resurssirajoitteisissa ympäristöissä, kuten mobiililaitteissa tai reunalaskennan alustoilla, joissa täysimittaiset LLM:t voivat olla epäkäytännöllisiä raskaan resurssitarpeensa vuoksi. Keskittymällä tehokkuuteen SLM:t tasapainottavat suorituskyvyn ja saavutettavuuden, mahdollistaen laajemman sovellettavuuden eri aloilla.

![slm](../../../translated_images/fi/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Oppimistavoitteet

Tässä oppitunnissa pyrimme esittelemään SLM:n tiedot ja yhdistämään ne Microsoft Phi-3:een oppiaksemme erilaisista tekstisisällön, näön ja MoE:n käyttöskenaarioista.

Oppitunnin päätteeksi sinun tulisi pystyä vastaamaan seuraaviin kysymyksiin:

- Mikä on SLM?
- Mikä on ero SLM:n ja LLM:n välillä?
- Mikä on Microsoft Phi-3/3.5 -perhe?
- Kuinka suorittaa päättely Microsoft Phi-3/3.5 -perheellä?

Valmiina? Aloitetaan.

## Erot suurten kielimallien (LLM) ja pienten kielimallien (SLM) välillä

Sekä LLM:t että SLM:t perustuvat todennäköisyyspohjaiseen koneoppimiseen, noudattaen samankaltaisia periaatteita arkkitehtuurisuunnittelussa, koulutusmenetelmissä, datan tuottamisprosesseissa ja mallin arviointitekniikoissa. Kuitenkin useat keskeiset tekijät erottavat nämä kaksi mallityyppiä.

## Pienten kielimallien sovellukset

SLM:illä on laaja sovellusalue, mukaan lukien:

- Chatbotit: Asiakastuen tarjoaminen ja käyttäjien kanssa keskustelu vuorovaikutteisesti.
- Sisällön luominen: Kirjoittajien avustaminen ideoiden generoinnissa tai jopa koko artikkelien luonnostelussa.
- Koulutus: Auttaa opiskelijoita kirjoitustehtävissä tai uusien kielten oppimisessa.
- Saavutettavuus: Työkalujen luominen vammaisille, kuten puheeksi muuntamisjärjestelmät.

**Koko**
  
Tärkein ero LLM:ien ja SLM:ien välillä perustuu mallien kokoon. LLM:t, kuten ChatGPT (GPT-4), voivat sisältää arviolta 1,76 biljoonaa parametria, kun taas avoimen lähdekoodin SLM, kuten Mistral 7B, on suunniteltu huomattavasti vähemmillä parametreilla — noin 7 miljardia. Tämä ero johtuu pääasiassa erosta mallin arkkitehtuurissa ja koulutusprosesseissa. Esimerkiksi ChatGPT käyttää itsehuomiomekanismia enkooderi-dekooderi-rakenteessa, kun taas Mistral 7B käyttää liukuikkunahuomiota, mikä mahdollistaa tehokkaamman koulutuksen pelkästään dekooderimallissa. Tämä arkkitehtuurinen ero vaikuttaa merkittävästi mallin monimutkaisuuteen ja suorituskykyyn.

**Ymmärrys**

SLM:t on tyypillisesti optimoitu suorituskykyyn tietyillä aloilla, mikä tekee niistä hyvin erikoistuneita, mutta mahdollisesti rajoittaa niiden kykyä tarjota laaja-alaista kontekstuaalista ymmärrystä useiden tieteenalojen välillä. Sen sijaan LLM:t pyrkivät simuloimaan ihmismäistä älykkyyttä laajemmin. Koulutettuna valtavalla ja monipuolisella datalla LLM:t on suunniteltu toimimaan hyvin monilla aloilla tarjoten suurempaa monipuolisuutta ja mukautuvuutta. Tämän seurauksena LLM:t soveltuvat monenlaisiin tehtäviin, kuten luonnollisen kielen käsittelyyn ja ohjelmointiin.

**Laskenta**

LLM:ien koulutus ja käyttöönotto kuluttavat paljon resursseja, usein vaativat merkittäviä laskenta-infrastruktuureja, kuten laajamittaisia GPU-klustereita. Esimerkiksi mallin kuten ChatGPT kouluttaminen alusta alkaen saattaa edellyttää tuhansia GPU-yksiköitä pitkän ajan kuluessa. Sen sijaan SLM:t, joissa on pienempi parametritarkkuus, ovat helpommin saavutettavissa laskennallisten resurssien osalta. Mallit kuten Mistral 7B voidaan kouluttaa ja suorittaa paikallisissa koneissa, joissa on kohtuulliset GPU-ominaisuudet, vaikka koulutus vaatiikin useiden tuntien suoritusta useilla GPU:illa.

**Vinouma**

Vinouma on tunnettu ongelma LLM:issä, pääasiassa koulutusdatan luonteen vuoksi. Nämä mallit luottavat usein raakadataan, joka on saatavilla avoimesti internetistä, mikä saattaa aliedustaa tai vääristää tiettyjä ryhmiä, sisältää virheellisiä merkintöjä tai heijastaa kieliopillisia vinoumia, joita aiheuttavat murteet, maantieteelliset vaihtelut ja kielioppisäännöt. Lisäksi LLM:ien arkkitehtuurin monimutkaisuus saattaa tahattomasti pahentaa vinoumaa, mikä saattaa jäädä huomaamatta ilman huolellista hienosäätöä. Toisaalta SLM:t, jotka on koulutettu rajatuilla, alakohtaisilla dataseteillä, ovat luontaisesti vähemmän alttiita tällaisille vinoumille, vaikka eivät täysin immuuneja niille.

**Päättely**

Pienempi koko antaa SLM:ille suuren edun päättelynopeudessa, mahdollistaen tehokkaan tuotannon paikallisessa laitteistossa ilman laajaa rinnakkaisprosessointia. Sen sijaan LLM:t, koon ja monimutkaisuuden vuoksi, vaativat usein merkittäviä rinnakkaisia laskentaresursseja hyväksyttävien päättelyaikojen saavuttamiseksi. Useiden samanaikaisten käyttäjien läsnäolo hidastaa entisestään LLM:ien vasteaikoja, erityisesti laajassa käyttöönotossa.

Yhteenvetona, vaikka sekä LLM:t että SLM:t perustuvat koneoppimisen perusperiaatteisiin, ne eroavat merkittävästi mallin koon, resurssivaatimusten, kontekstuaalisen ymmärryksen, vinouman alttiuden ja päättelynopeuden osalta. Nämä erot heijastavat niiden soveltuvuutta eri käyttötarkoituksiin, LLM:ien ollessa monipuolisempia mutta resursseja kuluttavampia ja SLM:ien tarjotessa alakohtaista tehokkuutta pienemmillä laskentavaatimuksilla.

***Huomautus: Tässä oppitunnissa esittelemme SLM:n Microsoft Phi-3 / 3.5:n avulla esimerkkinä.***

## Esittely Phi-3 / Phi-3.5 -perhe

Phi-3 / 3.5 -perhe kohdistuu pääasiassa tekstin, näön ja agentin (MoE) sovellusskenaarioihin:

### Phi-3 / 3.5 Instruct

Pääasiassa tekstin generointiin, keskustelun täydentämiseen ja sisältötiedon poimintaan jne.

**Phi-3-mini**

3,8 miljardin parametrin kielimalli on saatavilla Microsoft Foundryssä, Hugging Facessa ja Ollamassa. Phi-3-mallit ylittävät merkittävästi samankokoisten tai suurempien kielimallien suorituskyvyn keskeisillä testialustoilla (katso alla benchmark-numerot, korkeammat numerot ovat parempia). Phi-3-mini päihittää kaksinkertaisen kokonsa omaavat mallit, kun taas Phi-3-small ja Phi-3-medium päihittävät suurempia malleja, mukaan lukien GPT-3.5.

**Phi-3-small & medium**

Vain 7 miljardilla parametrilla Phi-3-small päihittää GPT-3.5T monissa kielen, päättelyn, koodaamisen ja matematiikan testialustoissa.

Phi-3-medium 14 miljardilla parametrilla jatkaa tätä trendiä ja päihittää Gemini 1.0 Pron.

**Phi-3.5-mini**

Voimme ajatella sitä Phi-3-minin päivityksenä. Vaikka parametrimäärä säilyy samana, se parantaa kykyä tukea useita kieliä (tukee yli 20 kieltä: arabia, kiina, tšekki, tanska, hollanti, englanti, suomi, ranska, saksa, heprea, unkari, italia, japani, korea, norja, puola, portugali, venäjä, espanja, ruotsi, thai, turkki, ukraina) ja lisää vahvempaa tukea pitkälle kontekstille.

Phi-3.5-mini 3,8 miljardilla parametrilla päihittää saman kokoiset kielimallit ja on samalla tasolla kaksinkertaisen kokonsa mallien kanssa.

### Phi-3 / 3.5 Vision

Voimme ajatella Phi-3/3.5 Instruct -mallia Phin kyvykkyytenä ymmärtää, ja Vision antaa Philä silmät maailman ymmärtämiseen.


**Phi-3-Vision**

Phi-3-Vision, jossa on vain 4,2 miljardia parametria, jatkaa tätä trendiä ja päihittää suurempia malleja, kuten Claude-3 Haikun ja Gemini 1.0 Pro V:n yleisissä visuaalisissa päättelytehtävissä, OCR-tehtävissä sekä taulukkojen ja diagrammien ymmärryksessä.


**Phi-3.5-Vision**

Phi-3.5-Vision on myös Phi-3-Visionin päivitys, joka lisää tuen useille kuville. Voit ajatella sitä näkön parannuksena: näet paitsi kuvat myös videot.

Phi-3.5-vision päihittää suurempia malleja, kuten Claude-3.5 Sonnetin ja Gemini 1.5 Flashin OCR-, taulukko- ja kaavioiden ymmärtämistehtävissä ja on samalla tasolla yleisissä visuaalisissa tietopäättelytehtävissä. Tukee monikehyksistä syötettä, eli suorittaa päättelyä useilla syötekuvilla.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** mahdollistaa mallien esikoulutuksen paljon vähemmällä laskennalla, mikä tarkoittaa, että mallin tai datasetin kokoa voi kasvattaa dramaattisesti samalla laskentabudjetilla kuin tiheällä mallilla. Erityisesti MoE-mallin tulisi saavuttaa sama laatu kuin tiheän mallin vastaava paljon nopeammin esikoulutuksen aikana.

Phi-3.5-MoE koostuu 16 x 3,8 miljardin parametrin asiantuntijamoduulista. Phi-3.5-MoE, jossa on vain 6,6 miljardia aktiivista parametria, saavuttaa saman tason päättelyssä, kielen ymmärryksessä ja matematiikassa kuin paljon suuremmat mallit.

Voimme käyttää Phi-3/3.5 -perheen malleja eri skenaarioiden mukaan. Toisin kuin LLM, voit ottaa Phi-3/3.5-mini tai Phi-3/3.5-Vision käyttöön reunalaitteissa.


## Kuinka käyttää Phi-3/3.5 -perheen malleja

Toivomme käyttää Phi-3/3.5 eri skenaarioissa. Seuraavaksi käytämme Phi-3/3.5 eri skenaarioiden mukaan.

![phi3](../../../translated_images/fi/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Päättely pilvi-API:en kautta

**Microsoft Foundry -mallit**

> **Huom:** GitHub Models lopettaa toimintansa heinäkuun 2026 lopussa. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) on suora korvaaja.

Microsoft Foundry Models on suorin tapa. Voit nopeasti käyttää Phi-3/3.5-Instruct -mallia Foundryn malliluettelon kautta. Yhdistämällä Azure AI Inference SDK:n / OpenAI SDK:n kautta voit käyttää API:a koodilla Phi-3/3.5-Instruct-pyynnön suorittamiseen. Voit myös testata erilaisia tuloksia Playgroundissa.

- Demo: Vertailu Phi-3-minin ja Phi-3.5-minin vaikutuksista kiinan kielen skenaarioissa

![phi3](../../../translated_images/fi/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/fi/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Tai jos haluamme käyttää näkö- ja MoE-malleja, voit käyttää Microsoft Foundrya kutsujen suorittamiseen. Jos olet kiinnostunut, voit lukea Phi-3 Cookbookin oppiaksesi kuinka kutsua Phi-3/3.5 Instruct, Vision, MoE Microsoft Foundryn kautta [Klikkaa tätä linkkiä](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Pilvipohjaisen Microsoft Foundry Models -luettelon lisäksi voit käyttää myös [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) tehtävien kutsujen toteuttamiseen. Voit käydä NVIDIA NIM:ssä suorittamassa Phi-3/3.5 -perheen API-kutsut. NVIDIA NIM (NVIDIA Inference Microservices) on joukko nopeutettuja inferenssimikropalveluita, jotka auttavat kehittäjiä ottamaan tekoälymalleja tehokkaasti käyttöön eri ympäristöissä kuten pilvissä, datakeskuksissa ja työasemissa.

Tässä muutamia NVIDIA NIM:n avainominaisuuksia:

- **Helppo käyttöönotto:** NIM mahdollistaa tekoälymallien käyttöönoton yhdellä komentorivillä, tehden integraatiosta olemassa oleviin työnkulkuun vaivatonta.
- **Optimoitu suorituskyky:** Hyödyntää NVIDIAn ennakkoon optimoituja inferenssimoottoreita, kuten TensorRT:tä ja TensorRT-LLM:ää, varmistaen matalan viiveen ja korkean läpäisyn.
- **Skaalautuvuus:** NIM tukee automaattista skaalaamista Kubernetesissä, mahdollistaen tehokkaan kuormien hallinnan.
- **Turvallisuus ja hallinta:** Organisaatiot voivat säilyttää hallinnan omista tiedoistaan ja sovelluksistaan itse hallinnoimalla NIM-mikropalveluita omalla infrastruktuurilla.
- **Vakiopalvelut:** NIM tarjoaa alan vakiintuneita rajapintoja, mikä tekee tekoälysovellusten, kuten chatbotien, tekoälyavustajien ja muiden, rakentamisesta ja integroinnista helppoa.

NIM on osa NVIDIA AI Enterprisea, jonka tavoitteena on yksinkertaistaa tekoälymallien käyttöönottoa ja operointia, varmistaen niiden tehokkaan toiminnan NVIDIA:n GPU:illa.

- Demo: NVIDIA NIM:n käyttö Phi-3.5-Vision-API:n kutsumiseen [[Klikkaa tästä](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5:n ajaminen paikallisesti
Päätteleminen Phi-3:n, tai minkä tahansa kielimallin, kuten GPT-3:n, yhteydessä viittaa prosessiin, jossa generoituaan vastauksia tai ennusteita annettujen syötteiden perusteella. Kun annat kehotteen tai kysymyksen Phi-3:lle, se käyttää koulutettua neuroverkkoaan päätelläkseen todennäköisimmän ja aiheeseen liittyvän vastauksen analysoimalla mallin oppimia kuvioita ja suhteita.

**Hugging Face Transformer**
Hugging Face Transformers on tehokas kirjasto luonnollisen kielen käsittelyyn (NLP) ja muihin koneoppimistehtäviin. Tässä joitakin keskeisiä seikkoja:

1. **Esikoulutetut mallit**: Tarjoaa tuhansia esikoulutettuja malleja, joita voidaan käyttää erilaisiin tehtäviin, kuten tekstin luokitteluun, nimeämättömien entiteettien tunnistukseen, kysymyksiin vastaamiseen, tiivistämiseen, kääntämiseen ja tekstin generointiin.

2. **Kehyksen yhteensopivuus**: Kirjasto tukee useita syväoppimiskehyksiä, mukaan lukien PyTorch, TensorFlow ja JAX. Tämä mahdollistaa mallin kouluttamisen yhdessä kehyksessä ja käytön toisessa.

3. **Monimodaaliset kyvyt**: NLP:n lisäksi Hugging Face Transformers tukee myös tehtäviä tietokonenäössä (esim. kuvien luokittelu, kohteiden tunnistus) ja äänenkäsittelyssä (esim. puheentunnistus, ääniluokittelu).

4. **Helppokäyttöisyys**: Kirjasto tarjoaa rajapintoja ja työkaluja mallien helppoon lataamiseen ja hienosäätöön, tehden siitä saavutettavan sekä aloittelijoille että asiantuntijoille.

5. **Yhteisö ja resurssit**: Hugging Facella on aktiivinen yhteisö sekä laaja dokumentaatio, opetusohjelmat ja oppaat, jotka auttavat käyttäjiä pääsemään alkuun ja hyödyntämään kirjastoa parhaalla mahdollisella tavalla.
[virallinen dokumentaatio](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) tai heidän [GitHub-repositorionsa](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Tämä on yleisimmin käytetty menetelmä, mutta se vaatii myös GPU-kiihdytyksen. Esimerkiksi Vision ja MoE -tapaukset vaativat paljon laskentaa, joka olisi hyvin hidasta CPU:lla, ellei niitä kvantisoida.


- Demo: Transformerilla Phi-3.5-Instruct -kutsun teko [Klikkaa tästä](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformerilla Phi-3.5-Vision -kutsun teko [Klikkaa tästä](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformerilla Phi-3.5-MoE -kutsun teko [Klikkaa tästä](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) on alusta, joka tekee suurten kielimallien (LLM) suorittamisesta paikallisesti omalla koneellasi helpompaa. Se tukee useita malleja, kuten Llama 3.1, Phi 3, Mistral ja Gemma 2, muiden joukossa. Alusta yksinkertaistaa prosessia paketoimalla mallipainot, konfiguraation ja datan yhdeksi paketiksi, tehden räätälöinnistä ja omien mallien luomisesta helpompaa käyttäjille. Ollama on saatavilla macOS:lle, Linuxille ja Windowsille. Se on erinomainen työkalu, jos haluat kokeilla tai ottaa käyttöön LLM:iä ilman pilvipalveluihin luottamista. Ollama on suorin tapa, sinun tarvitsee vain suorittaa seuraava komento.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) on Microsoftin offline- ja laitteistokohtainen ajonaikaympäristö, jolla voi ajaa malleja kuten Phi täysin omalla laitteistollasi – ei tarvita Azure-tilausta, API-avainta tai verkkoyhteyttä. Se valitsee automaattisesti parhaan käytettävissä olevan suoritusympäristön (NPU, GPU tai CPU) ja tarjoaa OpenAI-yhteensopivan päätepisteen, joten olemassa oleva `openai`/Azure AI Inference SDK -koodi voi osoittaa siihen pienin muutoksin. Katso [Foundry Localin dokumentaatio](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) aloittaaksesi.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) on monialustainen koneoppimisen päätelmien ja koulutuksen kiihdytin. ONNX Runtime for Generative AI (GENAI) on tehokas työkalu, joka auttaa sinua ajamaan generatiivisia tekoälymalleja tehokkaasti eri alustoilla.

## Mikä on ONNX Runtime?
ONNX Runtime on avoimen lähdekoodin projekti, joka mahdollistaa koneoppimismallien suorituskykyisen päättelyn. Se tukee malleja Open Neural Network Exchange (ONNX) -muodossa, joka on standardi koneoppimismallien esittämiseen. ONNX Runtime -päätteleminen voi mahdollistaa nopeammat asiakaskokemukset ja alhaisemmat kustannukset, tukien malleja syväoppimiskehyksistä kuten PyTorch ja TensorFlow/Keras sekä perinteisemmistä koneoppimiskirjastoista kuten scikit-learn, LightGBM, XGBoost ym. ONNX Runtime on yhteensopiva erilaisten laitteistojen, ajurien ja käyttöjärjestelmien kanssa ja tarjoaa optimaalisen suorituskyvyn hyödyntämällä laitteistokiihdyttimiä soveltuvin osin sekä käyttämällä graafien optimointeja ja muunnoksia.

## Mikä on generatiivinen tekoäly?
Generatiivinen tekoäly tarkoittaa tekoälyjärjestelmiä, jotka pystyvät tuottamaan uutta sisältöä, kuten tekstiä, kuvia tai musiikkia, niiden koulutusdatan perusteella. Esimerkkejä ovat kielimallit kuten GPT-3 ja kuvageneraatiomallit kuten Stable Diffusion. ONNX Runtime for GenAI -kirjasto tarjoaa generatiivisen tekoälyn silmukan ONNX-malleille, mukaan lukien oletuspäättely ONNX Runtimella, logien käsittely, haku ja otannan hallinta sekä KV-välimuistin hallinta.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI laajentaa ONNX Runtimen kykyjä tukemaan generatiivisia tekoälymalleja. Tässä joitakin keskeisiä ominaisuuksia:

- **Laaja alustatuki:** Se toimii erilaisilla alustoilla, mukaan lukien Windows, Linux, macOS, Android ja iOS.
- **Mallituki:** Se tukee monia suosittuja generatiivisia tekoälymalleja, kuten LLaMA, GPT-Neo, BLOOM ja muita.
- **Suorituskyvyn optimointi:** Se sisältää optimointeja erilaisille laitteistokiihdyttimille, kuten NVIDIA:n ja AMD:n GPU:t sekä muita.
- **Helppokäyttöisyys:** Se tarjoaa rajapintoja helppoon integrointiin sovelluksiin, joiden avulla voit generoida tekstiä, kuvia ja muuta sisältöä minimaalisella koodilla.
- Käyttäjät voivat kutsua korkean tason generate()-metodia tai ajaa mallin jokaisen iteraation silmukassa, generoiden yhden tokenin kerrallaan ja tarvittaessa päivittää generointiparametreja silmukan sisällä.
- ONNX Runtime tukee myös ahne-/ palkkihakua sekä TopP- ja TopK-otantaa token-jaksojen generointiin ja sisäänrakennettua logits-käsittelyä, kuten toiston rangaistuksia. Voit myös helposti lisätä mukautettua pistetystä.

## Aloitusohjeet
Aloittaaksesi ONNX Runtime for GENAI:n käytön voit seurata näitä ohjeita:

### Asenna ONNX Runtime:
```Python
pip install onnxruntime
```
### Asenna generatiivisen tekoälyn laajennukset:
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
### Demo: ONNX Runtime GenAI:n käyttö Phi-3.5-Vision-kutsuun


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

ONNX Runtime, Ollama ja Foundry Local -viitemenetelmien lisäksi voimme täydentää kvantitatiivisten mallien viitetietoja eri valmistajien tarjoamien malliviitemenetelmien perusteella. Esimerkiksi Apple MLX -kehys Apple Metalilla, Qualcomm QNN NPU:lla, Intel OpenVINO CPU/GPU:lla jne. Lisää sisältöä löytyy myös [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst):sta.


## Lisää

Olemme oppineet Phi-3/3.5-perheen perusteet, mutta SLM:stä oppiminen vaatii lisää tietoa. Vastauksia löydät Phi-3 Cookbookista. Jos haluat oppia lisää, käy [Phi-3 Cookbookissa](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->