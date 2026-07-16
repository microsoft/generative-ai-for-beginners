# Suuren kielimallin (LLM) tarjoajan valinta ja konfigurointi 🔑

Tehtäviä **voidaan** myös määrittää toimimaan yhtä tai useampaa suuren kielimallin (LLM) käyttöönottoa vastaan tuetun palveluntarjoajan kautta, kuten OpenAI, Azure tai Hugging Face. Ne tarjoavat _isännöidyn päätepisteen_ (API), johon voimme ohjelmallisesti käyttää oikeilla tunnistetiedoilla (API-avain tai token). Tässä kurssissa käsittelemme näitä palveluntarjoajia:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) monipuolisilla malleilla, mukaan lukien ydinsarja GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI-malleille, joissa painotetaan yritysvalmiutta
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) yhdellä päätepisteellä ja API-avaimella satojen mallien käyttöön OpenAI:lta, Meta:lta, Mistralilta, Cohere:lta, Microsoftilta ja muilta (korvaa GitHub Modelsin, joka poistuu käytöstä heinäkuun 2026 lopussa)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) avoimen lähdekoodin malleille ja inferenssipalvelimelle
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) tai [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), jos mieluummin ajat malleja täysin offline-tilassa omalla laitteellasi ilman pilvitilausta

**Näihin harjoituksiin tarvitset omat tilisi**. Tehtävät ovat valinnaisia, joten voit päättää määrittää yhden, kaikki tai ei yhtäkään palveluntarjoajista kiinnostuksesi mukaan. Vinkkejä rekisteröitymiseen:

| Rekisteröityminen | Hinta | API-avain | Playground | Kommentit |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektikohtainen](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Useita malleja saatavilla |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Pääsy on haettava etukäteen](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Hinnoittelu](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projektin yleiskatsaus](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Ilmainen taso saatavilla; yksi päätepiste + avain monille mallipalveluille |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Hinnoittelu](https://huggingface.co/pricing) | [Käyttöoikeustunnukset](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatissa on rajoitettu määrä malleja](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Ilmainen (käyttää omaa laitetta) | Ei vaadita | [Paikallinen CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Täysin offline, OpenAI-yhteensopiva päätepiste |
| | | | | |

Seuraa alla olevia ohjeita tämän repositorion _konfiguroimiseksi_ eri palveluntarjoajille. Tehtävät, jotka vaativat tietyn palveluntarjoajan, sisältävät tiedostonimessään yhden näistä tageista:

- `aoai` - vaatii Azure OpenAI -päätepisteen ja avaimen
- `oai` - vaatii OpenAI-päätepisteen ja avaimen
- `hf` - vaatii Hugging Face -tokenin
- `githubmodels` - vaatii Microsoft Foundry Models -päätepisteen ja avaimen (GitHub Models poistuu käytöstä heinäkuun 2026 lopussa)

Voit määrittää yhden, ei yhtäkään tai kaikki palveluntarjoajat. Liittyvät tehtävät vain antavat virheen, jos tunnistetiedot puuttuvat.

## Luo `.env` tiedosto

Oletamme, että olet jo lukenut yllä olevat ohjeet, rekisteröitynyt asianmukaiselle palveluntarjoajalle ja saanut tarvittavat todennustiedot (API_KEY tai token). Azure OpenAI:n kohdalla oletamme myös, että sinulla on voimassa oleva käyttöönotto Azure OpenAI -palvelusta (päätepiste) ja vähintään yksi GPT-malli käyttöönotettuna chat-kompletioon.

Seuraava vaihe on määrittää **paikalliset ympäristömuuttujat** seuraavasti:

1. Etsi juurikansiosta tiedosto nimeltä `.env.copy`, jonka sisältö on jotakuinkin tällainen:

   ```bash
   # OpenAI-tarjoaja
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI Microsoft Foundryssa
   ## (Azure OpenAI -palvelu on nyt osa Microsoft Foundrya: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Oletus asetettu! (nykyinen vakaa GA API -versio)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundryn mallit (monitarjoajainen malliluettelo, korvaa GitHub-mallit, jotka poistuvat käytöstä heinäkuun 2026 lopussa)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopioi tuo tiedosto nimelle `.env` alla olevalla komennolla. Tämä tiedosto on _gitignore:n_ listalla, jotta salaisuudet pysyvät turvassa.

   ```bash
   cp .env.copy .env
   ```

3. Täytä arvot (korvaa oikean puolen paikkamerkit) seuraavan osion ohjeiden mukaan.

4. (Valinnainen) Jos käytät GitHub Codespacesia, voit tallentaa ympäristömuuttujat _Codespaces-salaisuuksina_ tähän repositorioon liittyen. Tällöin paikallisen .env -tiedoston asennusta ei välttämättä tarvita. **Huomaa kuitenkin, että tämä vaihtoehto toimii vain GitHub Codespacesin kanssa.** Sinun tulee silti määrittää .env tiedosto, jos käytät Docker Desktopia.

## Täytä `.env` tiedosto

Katsotaanpa nopeasti muuttujien nimiä ymmärtääksemme, mitä ne tarkoittavat:

| Muuttuja  | Kuvaus  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Tämä on käyttäjän käyttöoikeustunnus, jonka olet määrittänyt profiilissasi |
| OPENAI_API_KEY | Tämä on valtuutusavain palvelun käyttämiseen ei-Azure OpenAI -päätteillä |
| AZURE_OPENAI_API_KEY | Tämä on kyseisen palvelun valtuutusavain |
| AZURE_OPENAI_ENDPOINT | Tämä on käyttöön otettu päätepiste Azure OpenAI -resurssissa |
| AZURE_OPENAI_DEPLOYMENT | Tämä on _tekstin generoinnin_ mallin käyttöönoton päätepiste |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Tämä on _tekstin upotusten_ mallin käyttöönoton päätepiste |
| AZURE_INFERENCE_ENDPOINT | Tämä on Microsoft Foundry -projektisi päätepiste, käytetään Microsoft Foundry Modelsissa |
| AZURE_INFERENCE_CREDENTIAL | Tämä on API-avain Microsoft Foundry -projektille |
| | |

Huom: Viimeiset kaksi Azure OpenAI -muuttujaa kuvaavat oletusmallia chat-kompletiota (tekstin generointia) ja vektorihakua (upotuksia) varten. Niiden asennusohjeet löytyvät asiaankuuluvista tehtävistä.

## Konfiguroi Azure OpenAI: Portaalista

> **Huom:** Azure OpenAI Service on nyt osa [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resurssit ja käyttöönotot näkyvät edelleen Azure Portaalissa, mutta päivittäinen mallien hallinta (käyttöönottaminen, playground, monitorointi) tapahtuu Foundry-portaalissa entisen itsenäisen "Azure OpenAI Studion" sijaan.

Azure OpenAI -päätepiste ja avain löytyvät [Azure Portaalista](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), joten aloitetaan sieltä.

1. Mene [Azure Portaaliin](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikkaa vasemman sivupalkin **Avain ja päätepiste** -valintaa.
1. Klikkaa **Näytä avaimet** - sinun pitäisi nähdä seuraavaa: AVAIN 1, AVAIN 2 ja Päätepiste.
1. Käytä AVAIN 1 arvoa AZURE_OPENAI_API_KEY muuttujassa
1. Käytä Päätepiste-arvoa AZURE_OPENAI_ENDPOINT muuttujassa

Seuraavaksi tarvitsemme käyttöönoton päätepisteet erityisille malleille.

1. Klikkaa vasemman sivupalkin **Mallien käyttöönotot** Azure OpenAI -resurssissa.
1. Kohdesivulla klikkaa **Siirry Microsoft Foundry portaalille** (tai **Hallinnoi käyttöönottoja**, resurssityypistä riippuen)

Tämä vie Microsoft Foundry -portaaliin, josta löydämme muut tarvittavat arvot, kuten alla on kuvattu.

## Konfiguroi Azure OpenAI: Microsoft Foundry portaalista

1. Siirry [Microsoft Foundry portaaliin](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **resurssiltasi** kuten yllä kuvattu.
1. Klikkaa vasemman sivupalkin **Käyttöönotot** -välilehteä nähdäksesi käytössä olevat mallit.
1. Jos haluamaasi mallia ei ole otettu käyttöön, käytä **Ota malli käyttöön** käynnistääksesi sen malliluettelosta.
1. Tarvitset _tekstin generointimallin_ – suosittelemme: **gpt-4o-mini**
1. Tarvitset _tekstin upotusmallin_ – suosittelemme **text-embedding-3-small**

Päivitä ympäristömuuttujat vastaamaan käytettyä _Käyttöönoton nimeä_. Se on tavallisesti mallin nimi, ellei sitä ole erikseen muutettu. Esimerkiksi:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Älä unohda tallentaa .env-tiedostoa lopuksi**. Voit nyt sulkea tiedoston ja palata muistiinpanojen suoritusohjeisiin.

## Konfiguroi OpenAI: Profiilista

OpenAI API-avaimesi löytyy [OpenAI-tililtäsi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jos sinulla ei ole sellaista, voit rekisteröityä tilille ja luoda API-avaimen. Saatuasi avaimen, voit lisätä sen `OPENAI_API_KEY` muuttujaan `.env` tiedostossa.

## Konfiguroi Hugging Face: Profiilista

Hugging Face -tokenisi löytyy profiilistasi kohdasta [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Älä julkaise tai jaa näitä julkisesti. Luo sen sijaan uusi token tätä projektia varten ja kopioi se `.env` tiedostoon `HUGGING_FACE_API_KEY` muuttujaksi. _Huom:_ Tämä ei teknisesti ole API-avain, mutta sitä käytetään autentikointiin, joten pidämme nimeämiskäytännön johdonmukaisena.

## Konfiguroi Microsoft Foundry Models: Portaalista

> **Huom:** GitHub Models poistuu käytöstä heinäkuun 2026 lopussa. Microsoft Foundry Models on suora korvaaja, tarjoten saman ilmaisen kokeiltavan malliluettelon ja Azure AI Inference SDK / OpenAI SDK -kokemuksen.

1. Mene [Microsoft Foundryyn](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ja luo (tai avaa) Foundry-projekti.
1. Selaa [malliluetteloa](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ja ota malli käyttöön, esimerkiksi `gpt-4o-mini`.
1. Projektin **Yleiskatsaus** -sivulla kopioi **päätepiste** ja **API-avain**.
1. Käytä päätepisteen arvoa `AZURE_INFERENCE_ENDPOINT` ja avaimen arvoa `AZURE_INFERENCE_CREDENTIAL` muuttujina `.env` tiedostossasi.

## Offline / Paikalliset palveluntarjoajat

Jos et halua käyttää pilvitilausta lainkaan, voit ajaa yhteensopivia avoimia malleja suoraan omalla laitteellasi:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoftin laitteella suoritettava runtime. Se valitsee automaattisesti parhaan suoritusympäristön (NPU, GPU tai CPU) ja tarjoaa OpenAI-yhteensopivan päätepisteen, joten voit käyttää suurinta osaa tämän kurssin esimerkkikoodista vähäisin muutoksin. Katso [Foundry Local -dokumentaatio](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) aloittaaksesi tai asenna komennolla `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - suosittu vaihtoehto ajaa avoimia malleja kuten Llama, Phi, Mistral ja Gemma paikallisesti.


Katso [Oppitunti 19: Rakentaminen SLM:ien avulla](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) käytännön esimerkkejä varten, joissa käytetään molempia vaihtoehtoja.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->