<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:06:24+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "es"
}
-->
# Preparación de datos de transcripción

Los scripts de preparación de datos de transcripción descargan las transcripciones de videos de YouTube y las preparan para su uso con el ejemplo de Búsqueda Semántica con OpenAI Embeddings y Funciones.

Los scripts de preparación de datos de transcripción han sido probados en las últimas versiones de Windows 11, macOS Ventura y Ubuntu 22.04 (y superiores).

## Crear los recursos necesarios en Azure OpenAI Service

> [!IMPORTANT]
> Recomendamos actualizar Azure CLI a la última versión para asegurar la compatibilidad con OpenAI
> Consulta la [Documentación](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Crear un grupo de recursos

> [!NOTE]
> Para estas instrucciones estamos usando el grupo de recursos llamado "semantic-video-search" en East US.
> Puedes cambiar el nombre del grupo de recursos, pero al cambiar la ubicación de los recursos,
> revisa la [tabla de disponibilidad de modelos](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Crear un recurso de Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Obtener el endpoint y las claves para su uso en esta aplicación

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Desplegar los siguientes modelos:
   - `text-embedding-ada-002` versión `2` o superior, nombrado `text-embedding-ada-002`
   - `gpt-35-turbo` versión `0613` o superior, nombrado `gpt-35-turbo`

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

Las siguientes variables de entorno son necesarias para ejecutar los scripts de preparación de datos de transcripción de YouTube.

### En Windows

Se recomienda agregar las variables a las variables de entorno de tu `usuario`.
`Inicio de Windows` > `Editar las variables de entorno del sistema` > `Variables de entorno` > `Variables de usuario` para [USER] > `Nuevo`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### En Linux y macOS

Se recomienda agregar las siguientes exportaciones a tu archivo `~/.bashrc` o `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalar las librerías de Python requeridas

1. Instala el [cliente git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) si aún no está instalado.
1. Desde una ventana de `Terminal`, clona el ejemplo en la carpeta de tu repositorio preferido.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navega a la carpeta `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Crea un entorno virtual de Python.

    En Windows:

    ```powershell
    python -m venv .venv
    ```

    En macOS y Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Activa el entorno virtual de Python.

   En Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   En macOS y Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Instala las librerías requeridas.

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

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.