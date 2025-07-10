<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:10:55+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "fi"
}
-->
# Puheen tekstitysdataprep

Puheen tekstitysdataprep-skriptit lataavat YouTube-videoiden tekstitykset ja valmistavat ne käytettäväksi Semantic Search with OpenAI Embeddings and Functions -esimerkin kanssa.

Puheen tekstitysdataprep-skriptejä on testattu uusimmilla Windows 11-, macOS Ventura- ja Ubuntu 22.04 (ja uudemmilla) versioilla.

## Luo tarvittavat Azure OpenAI Service -resurssit

> [!IMPORTANT]
> Suosittelemme päivittämään Azure CLI:n uusimpaan versioon yhteensopivuuden varmistamiseksi OpenAI:n kanssa
> Katso [Dokumentaatio](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Luo resurssiryhmä

> [!NOTE]
> Näissä ohjeissa käytämme "semantic-video-search" nimistä resurssiryhmää East US -alueella.
> Voit vaihtaa resurssiryhmän nimeä, mutta jos vaihdat resurssien sijaintia,
> tarkista [mallien saatavuustaulukko](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Luo Azure OpenAI Service -resurssi.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Hanki tämän sovelluksen käyttöön tarvittavat päätepiste ja avaimet

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Ota käyttöön seuraavat mallit:
   - `text-embedding-ada-002` versio `2` tai uudempi, nimeltään `text-embedding-ada-002`
   - `gpt-35-turbo` versio `0613` tai uudempi, nimeltään `gpt-35-turbo`

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
    --deployment-name gpt-35-turbo \
    --model-name gpt-35-turbo \
    --model-version "0613"  \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Tarvittava ohjelmisto

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) tai uudempi

## Ympäristömuuttujat

Seuraavat ympäristömuuttujat ovat pakollisia YouTube-tekstitysdatan valmisteluskriptien suorittamiseen.

### Windowsilla

Suosittelemme lisäämään muuttujat käyttäjän ympäristömuuttujiin.
`Windowsin Käynnistä` > `Muokkaa järjestelmän ympäristömuuttujia` > `Ympäristömuuttujat` > `Käyttäjämuuttujat` kohdalla [USER] > `Uusi`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### Linuxilla ja macOS:llä

Suosittelemme lisäämään seuraavat export-komennot tiedostoon `~/.bashrc` tai `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Asenna tarvittavat Python-kirjastot

1. Asenna [git-asiakasohjelma](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), jos sitä ei ole jo asennettu.
1. Avaa `Terminal`-ikkuna ja kloonaa esimerkkikansio haluamaasi repositorioon.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Siirry `data_prep`-kansioon.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Luo Python-virtuaaliympäristö.

    Windowsilla:

    ```powershell
    python -m venv .venv
    ```

    macOS:llä ja Linuxilla:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivoi Python-virtuaaliympäristö.

   Windowsilla:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS:llä ja Linuxilla:

   ```bash
   source .venv/bin/activate
   ```

1. Asenna tarvittavat kirjastot.

   Windowsilla:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS:llä ja Linuxilla:

   ```bash
   pip3 install -r requirements.txt
   ```

## Suorita YouTube-tekstitysdatan valmisteluskriptit

### Windowsilla

```powershell
.\transcripts_prepare.ps1
```

### macOS:llä ja Linuxilla

```bash
./transcripts_prepare.sh
```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.