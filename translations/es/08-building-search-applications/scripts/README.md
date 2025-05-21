<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T10:25:43+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "es"
}
-->
# Preparación de datos de transcripción

Los scripts de preparación de datos de transcripción descargan las transcripciones de videos de YouTube y las preparan para su uso con el ejemplo de Búsqueda Semántica con OpenAI Embeddings y Functions.

Los scripts de preparación de datos de transcripción han sido probados en las últimas versiones de Windows 11, macOS Ventura y Ubuntu 22.04 (y superiores).

## Crear los recursos necesarios del servicio Azure OpenAI

> [!IMPORTANT]
> Sugerimos actualizar Azure CLI a la última versión para asegurar la compatibilidad con OpenAI.
> Ver [Documentación](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Crear un grupo de recursos

> [!NOTE]
> Para estas instrucciones estamos usando el grupo de recursos llamado "semantic-video-search" en East US.
> Puedes cambiar el nombre del grupo de recursos, pero al cambiar la ubicación de los recursos,
> verifica la [tabla de disponibilidad de modelos](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Crear un recurso del servicio Azure OpenAI.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Obtener el punto final y las claves para su uso en esta aplicación

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Desplegar los siguientes modelos:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

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

## Software requerido

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) o superior

## Variables de entorno

Se requieren las siguientes variables de entorno para ejecutar los scripts de preparación de datos de transcripción de YouTube.

### En Windows

Se recomienda agregar las variables a tu `usuario` environment variables.
`Inicio de Windows` > `Editar las variables de entorno del sistema` > `Variables de entorno` > `Variables de usuario` for [USER] > `Nuevo`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### En Linux y macOS

Se recomienda agregar las siguientes exportaciones a tu archivo `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalar las bibliotecas de Python requeridas

1. Instalar el [cliente de git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) si aún no está instalado.
1. Desde una ventana de `Terminal`, clona el ejemplo en tu carpeta de repositorio preferida.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navega a la carpeta `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Crear un entorno virtual de Python.

    En Windows:

    ```powershell
    python -m venv .venv
    ```

    En macOS y Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Activar el entorno virtual de Python.

   En Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   En macOS y Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Instalar las bibliotecas requeridas.

   En Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   En macOS y Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Ejecutar los scripts de preparación de datos de transcripción de YouTube

### En Windows

```powershell
.\transcripts_prepare.ps1
```

### En macOS y Linux

```bash
./transcripts_prepare.sh
```

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción humana profesional. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.