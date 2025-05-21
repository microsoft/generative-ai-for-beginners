<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T09:00:55+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "es"
}
-->
# Configura tu entorno de desarrollo

Hemos configurado este repositorio y curso con un [contenedor de desarrollo](https://containers.dev?WT.mc_id=academic-105485-koreyst) que tiene un entorno de ejecución universal que puede soportar desarrollo en Python3, .NET, Node.js y Java. La configuración relacionada está definida en el archivo `devcontainer.json` ubicado en la carpeta `.devcontainer/` en la raíz de este repositorio.

Para activar el contenedor de desarrollo, lánzalo en [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (para un entorno de ejecución alojado en la nube) o en [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (para un entorno de ejecución alojado en un dispositivo local). Lee [esta documentación](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) para más detalles sobre cómo funcionan los contenedores de desarrollo dentro de VS Code.

> [!TIP]  
> Recomendamos usar GitHub Codespaces para un inicio rápido con mínimo esfuerzo. Proporciona una generosa [cuota de uso gratuita](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) para cuentas personales. Configura [tiempos de espera](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) para detener o eliminar codespaces inactivos y maximizar el uso de tu cuota.

## 1. Ejecutando Asignaciones

Cada lección tendrá asignaciones _opcionales_ que pueden estar disponibles en uno o más lenguajes de programación incluyendo: Python, .NET/C#, Java y JavaScript/TypeScript. Esta sección proporciona orientación general relacionada con la ejecución de esas asignaciones.

### 1.1 Asignaciones en Python

Las asignaciones en Python se proporcionan como aplicaciones (archivos `.py`) o como cuadernos Jupyter (archivos `.ipynb`).
- Para ejecutar el cuaderno, ábrelo en Visual Studio Code y luego haz clic en _Select Kernel_ (en la parte superior derecha) y selecciona la opción predeterminada de Python 3 que se muestra. Ahora puedes _Run All_ para ejecutar el cuaderno.
- Para ejecutar aplicaciones de Python desde la línea de comandos, sigue las instrucciones específicas de la asignación para asegurarte de seleccionar los archivos correctos y proporcionar los argumentos requeridos.

## 2. Configurando Proveedores

Las asignaciones **pueden** también configurarse para trabajar contra uno o más despliegues de Modelos de Lenguaje Grande (LLM) a través de un proveedor de servicios compatible como OpenAI, Azure o Hugging Face. Estos proporcionan un _endpoint alojado_ (API) al que podemos acceder programáticamente con las credenciales correctas (clave API o token). En este curso, discutimos estos proveedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) con modelos diversos incluyendo la serie principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos de OpenAI con enfoque en preparación empresarial.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos de código abierto y servidor de inferencia.

**Necesitarás usar tus propias cuentas para estos ejercicios**. Las asignaciones son opcionales, por lo que puedes elegir configurar uno, todos o ninguno de los proveedores según tus intereses. Algunas orientaciones para el registro:

| Registro | Costo | Clave API | Playground | Comentarios |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Precios](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Basado en proyectos](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sin código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Múltiples modelos disponibles |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Precios](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Inicio rápido SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Inicio rápido Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Debes aplicar anticipadamente para acceso](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Precios](https://huggingface.co/pricing) | [Tokens de acceso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tiene modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sigue las instrucciones a continuación para _configurar_ este repositorio para su uso con diferentes proveedores. Las asignaciones que requieran un proveedor específico contendrán una de estas etiquetas en su nombre de archivo:
 - `aoai` - requiere endpoint de Azure OpenAI, clave
 - `oai` - requiere endpoint de OpenAI, clave
 - `hf` - requiere token de Hugging Face

Puedes configurar uno, ninguno o todos los proveedores. Las asignaciones relacionadas simplemente generarán errores por falta de credenciales.

### 2.1. Crear archivo `.env`

Asumimos que ya has leído la orientación anterior y te has registrado con el proveedor relevante, y obtenido las credenciales de autenticación requeridas (API_KEY o token). En el caso de Azure OpenAI, asumimos que también tienes un despliegue válido de un Servicio de Azure OpenAI (endpoint) con al menos un modelo GPT desplegado para completar chat.

El siguiente paso es configurar tus **variables de entorno locales** de la siguiente manera:

1. Busca en la carpeta raíz un archivo `.env.copy` que debería tener contenido como este:

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

2. Copia ese archivo a `.env` usando el comando a continuación. Este archivo está _gitignore-d_, manteniendo los secretos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Llena los valores (reemplaza los marcadores de posición en el lado derecho del `=`) como se describe en la siguiente sección.

3. (Opcional) Si usas GitHub Codespaces, tienes la opción de guardar las variables de entorno como _secretos de Codespaces_ asociados con este repositorio. En ese caso, no necesitarás configurar un archivo .env local. **Sin embargo, ten en cuenta que esta opción solo funciona si usas GitHub Codespaces.** Aún necesitarás configurar el archivo .env si usas Docker Desktop.

### 2.2. Completar archivo `.env`

Echemos un vistazo rápido a los nombres de las variables para entender qué representan:

| Variable  | Descripción  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este es el token de acceso de usuario que configuraste en tu perfil |
| OPENAI_API_KEY | Esta es la clave de autorización para usar el servicio para endpoints de OpenAI no Azure |
| AZURE_OPENAI_API_KEY | Esta es la clave de autorización para usar ese servicio |
| AZURE_OPENAI_ENDPOINT | Este es el endpoint desplegado para un recurso de Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este es el endpoint de despliegue del modelo de _generación de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este es el endpoint de despliegue del modelo de _embeddings de texto_ |
| | |

Nota: Las dos últimas variables de Azure OpenAI reflejan un modelo predeterminado para completar chat (generación de texto) y búsqueda vectorial (embeddings) respectivamente. Las instrucciones para configurarlas se definirán en las asignaciones relevantes.

### 2.3 Configurar Azure: Desde el Portal

Los valores de endpoint y clave de Azure OpenAI se encontrarán en el [Portal de Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) así que comencemos allí.

1. Ve al [Portal de Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Haz clic en la opción **Keys and Endpoint** en la barra lateral (menú a la izquierda).
1. Haz clic en **Show Keys** - deberías ver lo siguiente: KEY 1, KEY 2 y Endpoint.
1. Usa el valor de KEY 1 para AZURE_OPENAI_API_KEY
1. Usa el valor de Endpoint para AZURE_OPENAI_ENDPOINT

A continuación, necesitamos los endpoints para los modelos específicos que hemos desplegado.

1. Haz clic en la opción **Model deployments** en la barra lateral (menú a la izquierda) para el recurso de Azure OpenAI.
1. En la página de destino, haz clic en **Manage Deployments**

Esto te llevará al sitio web de Azure OpenAI Studio, donde encontraremos los otros valores como se describe a continuación.

### 2.4 Configurar Azure: Desde el Studio

1. Navega a [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **desde tu recurso** como se describió anteriormente.
1. Haz clic en la pestaña **Deployments** (barra lateral, izquierda) para ver los modelos actualmente desplegados.
1. Si tu modelo deseado no está desplegado, usa **Create new deployment** para desplegarlo.
1. Necesitarás un modelo de _generación de texto_ - recomendamos: **gpt-35-turbo**
1. Necesitarás un modelo de _embeddings de texto_ - recomendamos **text-embedding-ada-002**

Ahora actualiza las variables de entorno para reflejar el _nombre de despliegue_ utilizado. Esto típicamente será el mismo que el nombre del modelo a menos que lo hayas cambiado explícitamente. Así que, como ejemplo, podrías tener:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**No olvides guardar el archivo .env cuando hayas terminado**. Ahora puedes salir del archivo y volver a las instrucciones para ejecutar el cuaderno.

### 2.5 Configurar OpenAI: Desde el Perfil

Tu clave API de OpenAI se puede encontrar en tu [cuenta de OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Si no tienes una, puedes registrarte para una cuenta y crear una clave API. Una vez que tengas la clave, puedes usarla para completar la variable `OPENAI_API_KEY` en el archivo `.env`.

### 2.6 Configurar Hugging Face: Desde el Perfil

Tu token de Hugging Face se puede encontrar en tu perfil bajo [Tokens de Acceso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). No los publiques ni los compartas públicamente. En su lugar, crea un nuevo token para el uso de este proyecto y cópialo en el archivo `.env` bajo la variable `HUGGING_FACE_API_KEY`. _Nota:_ Técnicamente, este no es una clave API pero se usa para autenticación, así que mantenemos esa convención de nombres para consistencia.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción humana profesional. No somos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.