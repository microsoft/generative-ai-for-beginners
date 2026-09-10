# Suuren kielimallin (LLM) tarjoajan valinta ja konfigurointi 🔑

Tehtävät **voidaan** lisäksi määrittää toimimaan yhtä tai useampaa Suuren Kielimallin (LLM) käyttöönottoa vastaan tuetun palveluntarjoajan kautta, kuten OpenAI, Azure tai Hugging Face. Nämä tarjoavat _isännöidyn päätepisteen_ (API), johon voimme ohjelmallisesti päästä käsiksi oikeilla tunnuksilla (API-avain tai token). Tässä kurssissa käsittelemme näitä palveluntarjoajia:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) monipuolisilla malleilla, mukaan lukien GPT-sarjan ydintä.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) OpenAI-malleihin keskittyen yritystason valmiuteen
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) yhdellä päätepisteellä ja API-avaimella satoihin malleihin OpenAI:lta, Metalta, Mistralilta, Cohere:lta, Microsoftilta ja muilta (korvaa GitHub Models -palvelun, joka poistuu käytöstä heinäkuun 2026 lopussa)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) avoimen lähdekoodin malleihin ja päättelypalvelimeen
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) tai [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), jos haluat mieluummin ajaa malleja täysin offline-tilassa omalla laitteellasi ilman pilvitilausta

**Tarvitset omat tilit näitä harjoituksia varten**. Tehtävät ovat valinnaisia, joten voit päättää määrittää yhden, kaikki tai ei yhtään tarjoajaa mielenkiintosi mukaan. Tässä ohjeita rekisteröitymiseen:

| Rekisteröityminen | Hinta | API-avain | Harjoitusalue | Kommentit |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektipohjainen](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Ei-koodia, Verkkopalvelu](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Useita malleja käytettävissä |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK:n pika-aloitus](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio-pika-aloitus](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Pääsyyn on haettava etukäteen](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Hinnoittelu](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projektin yleiskatsaus](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Harjoitusalue](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Ilmainen kerros; yksi päätepiste + avain monille mallitarjoajille |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Hinnoittelu](https://huggingface.co/pricing) | [Käyttötunnukset](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatissa on rajattu malli valikoima](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Ilmainen (ajetaan omalla laitteella) | Ei vaadita | [Paikallinen CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Täysin offline, OpenAI-yhteensopiva päätepiste |
| | | | | |

Seuraa alla olevia ohjeita tämän repositorion _konfiguroimiseksi_ eri palveluntarjoajien käyttöä varten. Tehtävissä, jotka vaativat tietyn tarjoajan, tiedostonimessä on jokin näistä tunnisteista:

- `aoai` - vaatii Azure OpenAI -päätepisteen ja avaimen
- `oai` - vaatii OpenAI-päätepisteen ja avaimen
- `hf` - vaatii Hugging Face -tokenin
- `githubmodels` - vaatii Microsoft Foundry Models -päätepisteen ja avaimen (GitHub Models poistuu käytöstä heinäkuun 2026 lopussa)

Voit määrittää yhden, ei yhtään tai kaikki palveluntarjoajat. Liittyvät tehtävät tuottavat virheen, jos tunnuksia puuttuu.

## Luo `.env`-tiedosto

Oletamme, että olet jo lukenut yllä olevan ohjeistuksen ja rekisteröitynyt asianmukaisen palveluntarjoajan käyttäjäksi sekä hankkinut vaaditut todennustiedot (API_KEY tai token). Azure OpenAI:n tapauksessa oletamme, että sinulla on myös voimassa oleva käyttöönotto Azure OpenAI -palvelusta (päätepiste), jossa vähintään yksi GPT-malli on otettu käyttöön chat-kompletiota varten.

Seuraava vaihe on konfiguroida **paikalliset ympäristömuuttujasi** seuraavasti:

1. Etsi juurikansiosta `.env.copy`-tiedosto, jonka sisältö pitäisi olla suunnilleen tällainen:

   ```bash
   # OpenAI-palveluntarjoaja
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI Microsoft Foundryssa
   ## (Azure OpenAI -palvelu on nyt osa Microsoft Foundrya: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Oletus on asetettu! (nykyinen vakaa GA API -versio)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundryn mallit (monipalveluntarjoajan malliluettelo, korvaa GitHubin mallit, jotka poistuvat käytöstä heinäkuun 2026 lopussa)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopioi tämä tiedosto nimellä `.env` alla olevalla komennolla. Tämä tiedosto on _gitignore:n_ piirissä, joten salaisuudet pysyvät turvassa.

   ```bash
   cp .env.copy .env
   ```

3. Täytä arvot (korvaa paikkamerkit merkkijonon oikealla puolella `=`) seuraavassa osiossa kuvatulla tavalla.

4. (Valinnainen) Jos käytät GitHub Codespacesia, voit tallentaa ympäristömuuttujat _Codespacesin salaisuuksina_, jotka liitetään tähän repositorioon. Tällöin paikallista .env-tiedostoa ei tarvitse määrittää. **Huomioi kuitenkin, että tämä toiminto toimii vain GitHub Codespacesissa.** Docker Desktopin käyttäjien on silti määritettävä .env-tiedosto.

## Täytä `.env`-tiedosto

Katsotaanpa nopeasti ympäristömuuttujien nimiä, jotta ymmärrämme mitä ne tarkoittavat:

| Muuttuja  | Kuvaus  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Käyttäjän käyttöoikeustunnus, jonka asetat profiilissasi |
| OPENAI_API_KEY | Autentikointiavain palvelun käyttämiseksi ei-Azure OpenAI -päätepisteissä |
| AZURE_OPENAI_API_KEY | Autentikointiavain kyseisen palvelun käyttöön |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI -resurssin käyttöönotettu päätepiste |
| AZURE_OPENAI_DEPLOYMENT | _Tekstin generointi_ mallin käyttöönoton päätepiste |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _Tekstin upotusten_ mallin käyttöönoton päätepiste |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundry -projektisi päätepiste, jota käytetään Microsoft Foundry Malien kanssa |
| AZURE_INFERENCE_CREDENTIAL | API-avain Microsoft Foundry -projektiisi |
| | |

Huom: Viimeiset kaksi Azure OpenAI -muuttujaa vastaavat oletusmallia chat-kompletioon (tekstin generointi) ja vektorihakuihin (upotukset). Niiden määrittäminen tapahtuu asiaankuuluvissa tehtävissä.

## Konfiguroi Azure OpenAI: Portaalista

> **Huom:** Azure OpenAI-palvelu on nyt osa [Microsoft Foundry -palvelua](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resurssit ja käyttöönotot näkyvät edelleen Azure-portaalissa, mutta päivittäinen mallien hallinta (käyttöönotot, harjoitusalue, seuranta) tapahtuu Foundry-portaalissa vanhan itsenäisen "Azure OpenAI Studion" sijaan.

Azure OpenAI:n päätepisteen ja avaimen löydät [Azure-portaalista](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), aloitetaan siis sieltä.

1. Mene [Azure-portaaliin](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Napsauta vasemman laidan valikosta **Keys and Endpoint**
1. Napsauta **Näytä avaimet** - näet arvot, kuten KEY 1, KEY 2 ja Endpoint
1. Käytä KEY 1 -arvoa `AZURE_OPENAI_API_KEY`-muuttujassa
1. Käytä Endpoint-arvoa `AZURE_OPENAI_ENDPOINT`-muuttujassa

Seuraavaksi tarvitsemme käyttöönotettujen mallien päätepisteet.

1. Napsauta vasemman laidan valikosta **Mallien käyttöönotot** kyseiselle Azure OpenAI -resurssille.
1. Kohdesivulla napsauta **Siirry Microsoft Foundry -portaaliin** (tai **Manage Deployments**, riippuen resurssityypistä)

Tämä vie sinut Microsoft Foundry -portaaliin, josta löydämme muut arvot alla kuvatusti.

## Konfiguroi Azure OpenAI: Microsoft Foundry -portaalista

1. Siirry [Microsoft Foundry -portaalille](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **resurssiltasi** yllä olevien ohjeiden mukaan.
1. Klikkaa vasemman laidan välilehteä **Deployments** nähdäksesi nykyiset mallikäyttöönotot.
1. Jos haluamasi malli ei ole käytössä, ota se käyttöön käyttämällä **Deploy model** toimintoa mallikatalogista ([mallikatalogi](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)).
1. Tarvitset _tekstin generointi_ mallin - suosittelemme: **gpt-5-mini**
1. Tarvitset _tekstin upotus_ mallin - suosittelemme **text-embedding-3-small**

Päivitä nyt ympäristömuuttujat vastaamaan _Käyttöönoton nimeä_, jota käytit. Se on tyypillisesti sama kuin mallin nimi, ellei sitä ole erikseen muutettu. Esimerkkinä voi olla:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Muista tallentaa .env-tiedosto lopuksi**. Voit nyt sulkea tiedoston ja siirtyä eteenpäin ohjeisiin muistiokansion ajamiseksi.

## Konfiguroi OpenAI: Profiilista

OpenAI API -avaimesi löytyy [OpenAI-tililtäsi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jos sinulla ei ole avainta, voit rekisteröityä tilille ja luoda API-avaimen. Saatuasi avaimen voit täyttää `OPENAI_API_KEY`-muuttujan `.env`-tiedostossa.

## Konfiguroi Hugging Face: Profiilista

Hugging Face -tokenisi löytyy profiilistasi kohdasta [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Älä julkaise tai jaa näitä julkisesti. Sen sijaan luo uusi token tätä projektia varten ja kopioi se `.env`-tiedostoon `HUGGING_FACE_API_KEY`-muuttujaan. _Huom:_ Tämä ei teknisesti ole API-avain, mutta sitä käytetään autentikointiin, joten pidämme nimeämiskäytännön johdonmukaisena.

## Konfiguroi Microsoft Foundry Models: Portaalista

> **Huom:** GitHub Models poistuu käytöstä heinäkuun 2026 lopussa. Microsoft Foundry Models on suora korvaaja, tarjoten saman ilmaisen kokeilukatalogin ja Azure AI Inference SDK / OpenAI SDK -kokemuksen.

1. Mene [Microsoft Foundryyn](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ja luo (tai avaa) Foundry-projekti.
1. Selaa [mallikatalogia](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ja ota malli käyttöön, esimerkiksi `gpt-5-mini`.
1. Projektin **Overview**-sivulla kopioi **päätepiste** ja **API-avain**.
1. Käytä päätepistettä `AZURE_INFERENCE_ENDPOINT` ja avainta `AZURE_INFERENCE_CREDENTIAL` muuttujissa omassa `.env`-tiedostossasi.

## Offline- tai paikalliset tarjoajat

Jos et halua käyttää lainkaan pilvitilausta, voit ajaa yhteensopivia avoimia malleja suoraan omalla laitteellasi:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoftin laitekohtainen ajonaikainen ympäristö. Se valitsee automaattisesti parhaimman suoritinlaitteen (NPU, GPU, tai CPU) ja tarjoaa OpenAI-yhteensopivan päätepisteen, joten voit käyttää suurinta osaa tämän kurssin esimerkkikoodista vähin muutoksin. Katso [Foundry Local -dokumentaatiota](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) aloittaaksesi, tai asenna komennolla `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - suosittu vaihtoehto avoimien mallien kuten Llama, Phi, Mistral ja Gemma paikalliseen ajamiseen.


Katso [Oppitunti 19: Rakentaminen SLM:illä](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) käytännön esimerkkejä molempien vaihtoehtojen käyttämiseen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->