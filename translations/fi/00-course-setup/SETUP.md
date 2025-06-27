<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:22:18+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "fi"
}
-->
# Aseta kehitysympäristösi

Olemme asentaneet tämän arkiston ja kurssin [kehityskontin](https://containers.dev?WT.mc_id=academic-105485-koreyst) avulla, joka sisältää universaalin käyttöympäristön, joka tukee Python3-, .NET-, Node.js- ja Java-kehitystä. Asiaankuuluva konfiguraatio on määritelty `devcontainer.json`-tiedostossa, joka sijaitsee `.devcontainer/`-kansiossa tämän arkiston juurella.

Aktivoidaksesi kehityskontin, käynnistä se [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pilvipohjainen käyttöympäristö) tai [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (paikallinen laitepohjainen käyttöympäristö). Lue [tästä dokumentaatiosta](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) lisätietoja siitä, miten kehityskontit toimivat VS Code -ympäristössä.

> [!TIP]  
> Suosittelemme käyttämään GitHub Codespacesia nopeaan aloitukseen vähäisellä vaivalla. Se tarjoaa anteliaan [ilmaisen käyttökiintiön](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) henkilökohtaisille tileille. Konfiguroi [aikakatkaisut](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) pysäyttämään tai poistamaan passiivisia codespaceja maksimoidaksesi kiintiön käyttöä.

## 1. Tehtävien suorittaminen

Jokaisessa oppitunnissa on _valinnaisia_ tehtäviä, jotka voidaan antaa yhdessä tai useammassa ohjelmointikielessä, mukaan lukien: Python, .NET/C#, Java ja JavaScript/TypeScript. Tämä osio tarjoaa yleisiä ohjeita näiden tehtävien suorittamiseen.

### 1.1 Python-tehtävät

Python-tehtävät annetaan joko sovelluksina (`.py`-tiedostot) tai Jupyter-muistikirjoina (`.ipynb`-tiedostot).
- Suorittaaksesi muistikirjan, avaa se Visual Studio Codessa, valitse _Select Kernel_ (oikeassa yläkulmassa) ja valitse oletuksena näytetty Python 3 -vaihtoehto. Nyt voit _Run All_ suorittaaksesi muistikirjan.
- Suorittaaksesi Python-sovelluksia komentoriviltä, seuraa tehtäväkohtaisia ohjeita varmistaaksesi, että valitset oikeat tiedostot ja annat tarvittavat argumentit.

## 2. Palveluntarjoajien konfigurointi

Tehtävät **voidaan** myös asettaa toimimaan yhtä tai useampaa suurta kielimallia (LLM) vastaan tuetun palveluntarjoajan, kuten OpenAI, Azure tai Hugging Face, kautta. Nämä tarjoavat _isännöidyn päätepisteen_ (API), johon voimme päästä ohjelmallisesti oikeilla tunnistetiedoilla (API-avain tai tunniste). Tässä kurssissa käsittelemme näitä palveluntarjoajia:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) eri malleilla, mukaan lukien ydin GPT-sarja.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI-malleille, keskittyen yritysvalmiuteen
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) avoimen lähdekoodin malleille ja inferenssipalvelimelle

**Sinun täytyy käyttää omia tilejäsi näissä harjoituksissa**. Tehtävät ovat valinnaisia, joten voit valita yhden, kaikki - tai ei yhtään - palveluntarjoajista kiinnostuksesi mukaan. Joitain ohjeita rekisteröitymiseen:

| Rekisteröityminen | Kustannus | API-avain | Leikkikenttä | Kommentit |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektipohjainen](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Ei koodia, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Useita malleja saatavilla |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Hinnoittelu](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK-pikakäynnistys](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio-pikakäynnistys](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Täytyy hakea etukäteen pääsyä varten](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Hinnoittelu](https://huggingface.co/pricing) | [Pääsytunnisteet](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chatilla on rajalliset mallit](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Seuraa alla olevia ohjeita _konfiguroidaksesi_ tämän arkiston käytettäväksi eri palveluntarjoajien kanssa. Tehtävät, jotka vaativat tiettyä palveluntarjoajaa, sisältävät jonkin näistä tunnisteista tiedostonimessään:
 - `aoai` - vaatii Azure OpenAI -päätepisteen, avaimen
 - `oai` - vaatii OpenAI-päätepisteen, avaimen
 - `hf` - vaatii Hugging Face -tunnisteen

Voit konfiguroida yhden, ei yhtään, tai kaikki palveluntarjoajat. Asiaankuuluvat tehtävät yksinkertaisesti virheilevät puuttuvista tunnistetiedoista.

### 2.1. Luo `.env`-tiedosto

Oletamme, että olet jo lukenut yllä olevat ohjeet ja rekisteröitynyt asianmukaisen palveluntarjoajan kanssa sekä saanut tarvittavat tunnistetiedot (API_KEY tai tunniste). Azure OpenAI:n tapauksessa oletamme, että sinulla on myös kelvollinen Azure OpenAI Service -palvelun käyttöönotto (päätepiste), jossa on vähintään yksi GPT-malli otettu käyttöön chatin täydentämistä varten.

Seuraava askel on konfiguroida **paikalliset ympäristömuuttujasi** seuraavasti:

1. Katso juurikansiosta `.env.copy`-tiedostoa, jonka pitäisi sisältää seuraavanlaiset sisällöt:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopioi tiedosto `.env`:ksi alla olevan komennon avulla. Tämä tiedosto on _gitignore-d_, pitäen salaisuudet turvassa.

   ```bash
   cp .env.copy .env
   ```

3. Täytä arvot (korvaa paikkamerkit oikealla puolella `=`) kuten seuraavassa osiossa kuvataan.

3. (Vaihtoehto) Jos käytät GitHub Codespacesia, sinulla on mahdollisuus tallentaa ympäristömuuttujat _Codespaces secrets_ -salaisuuksina, jotka liittyvät tähän arkistoon. Tässä tapauksessa sinun ei tarvitse asettaa paikallista .env-tiedostoa. **Huomaa kuitenkin, että tämä vaihtoehto toimii vain, jos käytät GitHub Codespacesia.** Sinun täytyy silti asettaa .env-tiedosto, jos käytät Docker Desktopia.

### 2.2. Täytä `.env`-tiedosto

Katsotaan nopeasti muuttujien nimiä ymmärtääksemme, mitä ne edustavat:

| Muuttuja  | Kuvaus  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Tämä on käyttäjän pääsytunniste, jonka asetat profiilissasi |
| OPENAI_API_KEY | Tämä on valtuutusavain palvelun käyttämiseen ei-Azure OpenAI -päätepisteille |
| AZURE_OPENAI_API_KEY | Tämä on valtuutusavain palvelun käyttämiseen |
| AZURE_OPENAI_ENDPOINT | Tämä on käyttöön otettu päätepiste Azure OpenAI -resurssille |
| AZURE_OPENAI_DEPLOYMENT | Tämä on _tekstin generointi_ -mallin käyttöönoton päätepiste |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Tämä on _tekstin upotukset_ -mallin käyttöönoton päätepiste |
| | |

Huomaa: Viimeiset kaksi Azure OpenAI -muuttujaa heijastavat oletusmallia chatin täydentämistä (tekstin generointi) ja vektorihakua (upotukset) varten. Ohjeet niiden asettamiseksi määritellään asiaankuuluvissa tehtävissä.

### 2.3 Konfiguroi Azure: Portaalista

Azure OpenAI -päätepisteen ja avainarvot löytyvät [Azure-portaalista](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), joten aloitetaan sieltä.

1. Mene [Azure-portaaliin](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Napsauta **Keys and Endpoint** -vaihtoehtoa sivupalkissa (valikko vasemmalla).
1. Napsauta **Show Keys** - näet seuraavat: KEY 1, KEY 2 ja Endpoint.
1. Käytä KEY 1 -arvoa AZURE_OPENAI_API_KEY:lle
1. Käytä Endpoint-arvoa AZURE_OPENAI_ENDPOINT:lle

Seuraavaksi tarvitsemme päätepisteet erityisesti käyttöön otetuille malleille.

1. Napsauta **Model deployments** -vaihtoehtoa sivupalkissa (vasen valikko) Azure OpenAI -resurssille.
1. Kohdesivulla napsauta **Manage Deployments**

Tämä vie sinut Azure OpenAI Studio -verkkosivustolle, jossa löydämme muut arvot kuten alla kuvataan.

### 2.4 Konfiguroi Azure: Studiosta

1. Siirry [Azure OpenAI Studioon](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **resurssistasi** kuten yllä kuvattu.
1. Napsauta **Deployments**-välilehteä (sivupalkki, vasen) nähdäksesi tällä hetkellä käyttöön otetut mallit.
1. Jos haluttu malli ei ole käyttöön otettu, käytä **Create new deployment** ottaaksesi sen käyttöön.
1. Tarvitset _tekstin generointi_ -mallin - suosittelemme: **gpt-35-turbo**
1. Tarvitset _tekstin upotukset_ -mallin - suosittelemme **text-embedding-ada-002**

Päivitä nyt ympäristömuuttujat heijastamaan käytettyä _Deployment name_ -nimeä. Tämä on yleensä sama kuin mallin nimi, ellei sitä ole muutettu erikseen. Esimerkiksi sinulla voisi olla:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Älä unohda tallentaa .env-tiedostoa, kun olet valmis**. Voit nyt poistua tiedostosta ja palata ohjeisiin muistikirjan suorittamista varten.

### 2.5 Konfiguroi OpenAI: Profiilista

OpenAI API -avaimesi löytyy [OpenAI-tililtäsi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jos sinulla ei ole sellaista, voit rekisteröityä tilille ja luoda API-avaimen. Kun sinulla on avain, voit käyttää sitä `.env`-tiedoston `OPENAI_API_KEY`-muuttujan täyttämiseen.

### 2.6 Konfiguroi Hugging Face: Profiilista

Hugging Face -tunnisteesi löytyy profiilistasi kohdasta [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Älä julkaise tai jaa niitä julkisesti. Sen sijaan, luo uusi tunniste tämän projektin käyttöä varten ja kopioi se `.env`-tiedostoon `HUGGING_FACE_API_KEY`-muuttujan alle. _Huom:_ Tämä ei teknisesti ole API-avain, mutta sitä käytetään autentikointiin, joten pidämme tämän nimeämiskäytännön johdonmukaisena.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta ole tietoinen siitä, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja omalla kielellään tulisi pitää ensisijaisena lähteenä. Kriittisten tietojen osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.