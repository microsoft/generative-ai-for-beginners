# Puheen muokkausdatan valmistelu

Puheen muokkausdatan valmisteluskriptit lataavat YouTube-videoiden tekstitykset ja valmistavat ne käytettäväksi Semanttisen haun OpenAI Embeddings ja Functions -esimerkin kanssa.

Puheen muokkausdatan valmisteluskriptit on testattu uusimmilla Windows 11, macOS Venturan ja Ubuntu 22.04 (ja uudemmat) versioilla.

## Luo vaaditut Azure OpenAI Service -resurssit

> [!IMPORTANT]
> Suosittelemme päivittämään Azure CLI:n uusimpaan versioon yhteensopivuuden varmistamiseksi OpenAI:n kanssa.
> Katso [Dokumentaatio](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Luo resurssiryhmä

> [!NOTE]
> Näissä ohjeissa käytämme "semantic-video-search" nimistä resurssiryhmää East US -alueella.
> Voit vaihtaa resurssiryhmän nimen, mutta muuttaessasi resurssien sijaintia,
> tarkista [mallin saatavuustaulukko](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Luo Azure OpenAI Service -resurssi.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Hae tämän sovelluksen käyttöön päätepiste ja avaimet

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Ota käyttöön seuraavat mallit:
   - `text-embedding-ada-002` versio `2` tai uudempi, nimeltään `text-embedding-ada-002`
   - `gpt-5-mini` nimeltään `gpt-5-mini`

```console
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Vaadittava ohjelmisto

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) tai uudempi

## Ympäristömuuttujat

Seuraavat ympäristömuuttujat ovat pakollisia YouTube-tekstitysdatan valmisteluskriptien suorittamiseen.

### Windowsissa

Suositellaan lisäämään muuttujat käyttäjän ympäristömuuttujiin.
`Windowsin Käynnistä` > `Muokkaa järjestelmän ympäristömuuttujia` > `Ympäristömuuttujat` > `Käyttäjämuuttujat` kohdalla [USER] > `Uusi`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Voit lisätä ympäristömuuttujat PowerShell-profiiliisi.

```powershell
$env:AZURE_OPENAI_API_KEY = "<sinun Azure OpenAI Service API-avain>"
$env:AZURE_OPENAI_ENDPOINT = "<sinun Azure OpenAI Service päätepiste>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<sinun Azure OpenAI Service mallin käyttöönoton nimi>"
$env:GOOGLE_DEVELOPER_API_KEY = "<sinun Google kehittäjän API-avain>"
``` -->

### Linuxissa ja macOS:ssa

Suositellaan lisäämään seuraavat export-komennot `~/.bashrc` tai `~/.zshrc` tiedostoon.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Asenna vaadittavat Python-kirjastot

1. Asenna [git-asiakas](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), jos se ei ole jo asennettuna.
1. Kopioi esimerkkikoodi haluamaasi reposi kansioon `Terminal`-ikkunasta.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Siirry `data_prep`-kansioon.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Luo Python-virtuaaliympäristö.

    Windowsissa:

    ```powershell
    python -m venv .venv
    ```

    macOS:ssa ja Linuxissa:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivoi Python-virtuaaliympäristö.

   Windowsissa:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS:ssa ja Linuxissa:

   ```bash
   source .venv/bin/activate
   ```

1. Asenna vaaditut kirjastot.

   Windowsissa:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS:ssa ja Linuxissa:

   ```bash
   pip3 install -r requirements.txt
   ```

## Suorita YouTube-tekstitysdatan valmisteluskriptit

### Windowsissa

```powershell
.\transcripts_prepare.ps1
```

### macOS:ssa ja Linuxissa

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->