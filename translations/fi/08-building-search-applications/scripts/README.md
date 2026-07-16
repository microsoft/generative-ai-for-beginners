# Puheen tunnistuksen datan valmistelu

Puheen tunnistuksen datan valmisteluskriptit lataavat YouTube-videoiden tekstitykset ja valmistelevat ne Semanttista hakua OpenAI-mallien ja Funktioiden näytettä varten.

Puheen tunnistuksen datan valmisteluskriptit on testattu uusimmilla Windows 11-, macOS Ventura- ja Ubuntu 22.04 (ja sitä uudemmilla) julkaisuilla.

## Luo tarvittavat Azure OpenAI -palveluresurssit

> [!IMPORTANT]
> Suosittelemme päivittämään Azure CLI:n uusimpaan versioon yhteensopivuuden varmistamiseksi OpenAI:n kanssa
> Katso [Dokumentaatio](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Luo resurssiryhmä

> [!NOTE]
> Näissä ohjeissa käytämme "semantic-video-search" -nimistä resurssiryhmää East US -alueella.
> Voit muuttaa resurssiryhmän nimeä, mutta kun vaihdat resurssien sijaintia,
> tarkista [mallien saatavuustaulukko](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Luo Azure OpenAI -palveluresurssi.

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
   - `gpt-4o-mini` nimeltään `gpt-4o-mini`

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
    --deployment-name gpt-4o-mini \
    --model-name gpt-4o-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Tarvittava ohjelmisto

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) tai uudempi

## Ympäristömuuttujat

Seuraavat ympäristömuuttujat ovat pakollisia YouTube-puheentunnistusdatan valmisteluskriptien suorittamiseen.

### Windowsissa

Suosittelemme lisäämään muuttujat käyttäjän ympäristömuuttujiin.
`Windowsin Käynnistä` > `Muokkaa järjestelmän ympäristömuuttujia` > `Ympäristömuuttujat` > `Käyttäjämuuttujat` kohdalla [USER] > `Uusi`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Voit myös lisätä ympäristömuuttujat PowerShell-profiiliisi.

```powershell
$env:AZURE_OPENAI_API_KEY = "<Azure OpenAI -palvelun API-avain>"
$env:AZURE_OPENAI_ENDPOINT = "<Azure OpenAI -palvelun päätepiste>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<Azure OpenAI -palvelun mallin käyttöönoton nimi>"
$env:GOOGLE_DEVELOPER_API_KEY = "<Google-kehittäjän API-avain>"
``` -->

### Linuxilla ja macOS:llä

Suosittelemme lisäämään seuraavat vientikomennot `~/.bashrc` tai `~/.zshrc` tiedostoon.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Asenna tarvittavat Python-kirjastot

1. Asenna [git-asiakas](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), jos sitä ei ole jo asennettu.
1. Avaa `Terminal`-ikkuna ja kloonaa näyte haluamaasi repositoriokansioon.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Siirry `data_prep` -kansioon.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Luo Pythonin virtuaaliympäristö.

    Windowsissa:

    ```powershell
    python -m venv .venv
    ```

    macOS:llä ja Linuxilla:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivoi Pythonin virtuaaliympäristö.

   Windowsissa:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS:llä ja Linuxilla:

   ```bash
   source .venv/bin/activate
   ```

1. Asenna tarvittavat kirjastot.

   Windowsissa:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS:llä ja Linuxilla:

   ```bash
   pip3 install -r requirements.txt
   ```

## Suorita YouTube-puheentunnistusdatan valmisteluskriptit

### Windowsissa

```powershell
.\transcripts_prepare.ps1
```

### macOS:llä ja Linuxilla

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->