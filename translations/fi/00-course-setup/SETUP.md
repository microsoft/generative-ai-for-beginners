<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:32:20+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "fi"
}
-->
# Määritä kehitysympäristösi

Olemme määrittäneet tämän repositorion ja kurssin [kehityssäiliöllä](https://containers.dev?WT.mc_id=academic-105485-koreyst), jossa on Universal runtime, joka tukee Python3-, .NET-, Node.js- ja Java-kehitystä. Asiaankuuluva konfiguraatio on määritelty `devcontainer.json`-tiedostossa, joka sijaitsee `.devcontainer/`-kansiossa tämän repositorion juurihakemistossa.

Aktivoi kehityssäiliö käynnistämällä se [GitHub Codespacesissa](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pilvipohjainen runtime) tai [Docker Desktopissa](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (paikallinen laite). Lue [tämä dokumentaatio](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) saadaksesi lisätietoja siitä, miten kehityssäiliöt toimivat VS Codessa.

> [!TIP]  
> Suosittelemme GitHub Codespacesin käyttöä nopeaan alkuun mahdollisimman vähällä vaivalla. Se tarjoaa anteliaan [ilmaisen käyttökiintiön](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) henkilökohtaisille tileille. Määritä [aikakatkaisut](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) pysäyttämään tai poistamaan käyttämättömät codespacet, jotta saat kiintiöstäsi parhaan hyödyn.

## 1. Tehtävien suorittaminen

Jokaisella oppitunnilla on _valinnaisia_ tehtäviä, jotka voivat olla tarjolla yhdessä tai useammassa ohjelmointikielessä, kuten Python, .NET/C#, Java ja JavaScript/TypeScript. Tässä osiossa annetaan yleisiä ohjeita näiden tehtävien suorittamiseen.

### 1.1 Python-tehtävät

Python-tehtävät toimitetaan joko sovelluksina (`.py`-tiedostot) tai Jupyter-muistikirjoina (`.ipynb`-tiedostot).  
- Suorittaaksesi muistikirjan, avaa se Visual Studio Codessa, klikkaa _Select Kernel_ (oikeassa yläkulmassa) ja valitse näkyviin tuleva oletusvaihtoehto Python 3. Voit nyt valita _Run All_ suorittaaksesi koko muistikirjan.  
- Python-sovellusten suorittamiseksi komentoriviltä noudata tehtäväkohtaisia ohjeita varmistaaksesi, että valitset oikeat tiedostot ja annat tarvittavat argumentit.

## 2. Palveluntarjoajien määrittäminen

Tehtävät **voivat** myös olla määritetty toimimaan yhden tai useamman suuren kielimallin (LLM) käyttöönoton kanssa tuetun palveluntarjoajan, kuten OpenAI:n, Azuren tai Hugging Facen kautta. Nämä tarjoavat _isännöidyn päätepisteen_ (API), johon pääsemme ohjelmallisesti käsiksi oikeilla tunnistetiedoilla (API-avain tai token). Tässä kurssissa käsittelemme seuraavia palveluntarjoajia:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), jolla on monipuolisia malleja, mukaan lukien GPT-sarjan ydint mallit.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst), joka keskittyy OpenAI-malleihin yrityskäyttövalmiudella
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) avoimen lähdekoodin malleille ja inferenssipalvelimelle

**Näitä harjoituksia varten tarvitset omat tilisi**. Tehtävät ovat valinnaisia, joten voit valita, määritätkö yhden, kaikki vai et yhtään palveluntarjoajaa kiinnostuksesi mukaan. Tässä ohjeita rekisteröitymiseen:

| Rekisteröityminen | Hinta | API-avain | Playground | Kommentit |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Hinnoittelu](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Projektikohtainen](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Ei-koodia, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Useita malleja saatavilla |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Hinnoittelu](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Pääsyyn on haettava etukäteen](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Hinnoittelu](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chatissa on rajattu määrä malleja](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Noudata alla olevia ohjeita määrittääksesi tämän repositorion käytettäväksi eri palveluntarjoajien kanssa. Tehtävissä, jotka vaativat tietyn palveluntarjoajan, tiedoston nimessä on jokin seuraavista tunnisteista:  
 - `aoai` - vaatii Azure OpenAI -päätepisteen ja avaimen  
 - `oai` - vaatii OpenAI-päätepisteen ja avaimen  
 - `hf` - vaatii Hugging Face -tokenin  

Voit määrittää yhden, useamman tai kaikki palveluntarjoajat. Tehtävät, jotka vaativat tietyn palveluntarjoajan, antavat virheen, jos tunnistetietoja ei ole.

### 2.1. Luo `.env`-tiedosto

Oletamme, että olet jo lukenut yllä olevat ohjeet, rekisteröitynyt asianmukaiselle palveluntarjoajalle ja saanut tarvittavat tunnistetiedot (API_KEY tai token). Azuren OpenAI:n tapauksessa oletamme myös, että sinulla on voimassa oleva käyttöönotto Azure OpenAI -palvelussa (päätepiste), jossa on vähintään yksi GPT-malli chat-suoritusta varten.

Seuraava vaihe on määrittää **paikalliset ympäristömuuttujat** seuraavasti:

1. Etsi juurihakemistosta `.env.copy`-tiedosto, jonka sisältö on suunnilleen tällainen:

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

2. Kopioi tiedosto nimellä `.env` alla olevalla komennolla. Tämä tiedosto on _gitignore:ssa_, joten salaisuudet pysyvät turvassa.

   ```bash
   cp .env.copy .env
   ```

3. Täytä arvot (korvaa oikealla puolella olevat paikkamerkit) seuraavan osion ohjeiden mukaisesti.

3. (Valinnainen) Jos käytät GitHub Codespacesia, voit tallentaa ympäristömuuttujat _Codespaces-salaisuuksina_, jotka liittyvät tähän repositorioon. Tällöin sinun ei tarvitse määrittää paikallista .env-tiedostoa. **Huomaa kuitenkin, että tämä vaihtoehto toimii vain GitHub Codespacesin kanssa.** Jos käytät Docker Desktopia, sinun on silti määritettävä .env-tiedosto.

### 2.2. Täytä `.env`-tiedosto

Katsotaan nopeasti muuttujien nimet ja mitä ne tarkoittavat:

| Muuttuja  | Kuvaus  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Tämä on käyttäjän käyttöoikeustoken, jonka määritit profiilissasi |
| OPENAI_API_KEY | Tämä on valtuutusavain palvelun käyttöön ei-Azure OpenAI -päätepisteissä |
| AZURE_OPENAI_API_KEY | Tämä on valtuutusavain kyseisen palvelun käyttöön |
| AZURE_OPENAI_ENDPOINT | Tämä on käyttöönotettu päätepiste Azure OpenAI -resurssille |
| AZURE_OPENAI_DEPLOYMENT | Tämä on _tekstin generointiin_ käytettävän mallin käyttöönoton päätepiste |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Tämä on _tekstin upotuksiin_ käytettävän mallin käyttöönoton päätepiste |
| | |

Huom: Viimeiset kaksi Azure OpenAI -muuttujaa viittaavat oletusmalliin chat-suoritusta (tekstin generointi) ja vektorihaun (upotukset) osalta. Niiden määrittämisohjeet löytyvät asiaankuuluvista tehtävistä.

### 2.3. Määritä Azure: Portaalista

Azure OpenAI -päätepisteen ja avaimen arvot löytyvät [Azure-portaalista](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), joten aloitetaan sieltä.

1. Mene [Azure-portaaliin](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. Klikkaa vasemman laidan valikosta **Keys and Endpoint**  
3. Klikkaa **Show Keys** -näet seuraavat arvot: KEY 1, KEY 2 ja Endpoint  
4. Käytä KEY 1 -arvoa muuttujalle AZURE_OPENAI_API_KEY  
5. Käytä Endpoint-arvoa muuttujalle AZURE_OPENAI_ENDPOINT  

Seuraavaksi tarvitsemme käyttöönotettujen mallien päätepisteet.

1. Klikkaa vasemman laidan valikosta **Model deployments** Azure OpenAI -resurssille  
2. Kohdesivulla klikkaa **Manage Deployments**

Tämä vie sinut Azure OpenAI Studio -sivustolle, josta löydämme muut arvot alla kuvatulla tavalla.

### 2.4. Määritä Azure: Studiosta

1. Siirry [Azure OpenAI Studioon](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **resurssiltasi** kuten yllä on kuvattu.  
2. Klikkaa vasemman laidan välilehteä **Deployments** nähdäksesi tällä hetkellä käytössä olevat mallit.  
3. Jos haluamaasi mallia ei ole käytössä, käytä **Create new deployment** -toimintoa ottaaksesi sen käyttöön.  
4. Tarvitset _tekstin generointiin_ tarkoitetun mallin – suosittelemme: **gpt-35-turbo**  
5. Tarvitset _tekstin upotuksiin_ tarkoitetun mallin – suosittelemme **text-embedding-ada-002**

Päivitä nyt ympäristömuuttujat vastaamaan käytettyä _Deployment name_ -arvoa. Tämä on yleensä sama kuin mallin nimi, ellei sitä ole erikseen muutettu. Esimerkiksi:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Muista tallentaa .env-tiedosto, kun olet valmis**. Voit nyt sulkea tiedoston ja palata ohjeisiin muistikirjan suorittamisesta.

### 2.5. Määritä OpenAI: Profiilista

OpenAI API-avaimesi löytyy [OpenAI-tililtäsi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jos sinulla ei vielä ole avainta, voit rekisteröityä tilille ja luoda API-avaimen. Kun sinulla on avain, voit lisätä sen `OPENAI_API_KEY`-muuttujaan `.env`-tiedostossa.

### 2.6. Määritä Hugging Face: Profiilista

Hugging Face -tokenisi löytyy profiilistasi kohdasta [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Älä julkaise tai jaa näitä julkisesti. Sen sijaan luo uusi token tätä projektia varten ja kopioi se `.env`-tiedostoon muuttujan `HUGGING_FACE_API_KEY` arvoksi. _Huom:_ Tämä ei teknisesti ole API-avain, mutta sitä käytetään tunnistautumiseen, joten pidämme nimeämiskäytännön johdonmukaisena.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.