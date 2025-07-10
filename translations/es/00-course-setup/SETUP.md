<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:21:00+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "es"
}
-->
# Configura Tu Entorno de Desarrollo

Hemos configurado este repositorio y curso con un [contenedor de desarrollo](https://containers.dev?WT.mc_id=academic-105485-koreyst) que cuenta con un entorno universal capaz de soportar desarrollo en Python3, .NET, Node.js y Java. La configuración relacionada está definida en el archivo `devcontainer.json` ubicado en la carpeta `.devcontainer/` en la raíz de este repositorio.

Para activar el contenedor de desarrollo, ejecútalo en [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (para un entorno en la nube) o en [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (para un entorno local). Consulta [esta documentación](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) para más detalles sobre cómo funcionan los contenedores de desarrollo en VS Code.

> [!TIP]  
> Recomendamos usar GitHub Codespaces para comenzar rápidamente con el mínimo esfuerzo. Ofrece una generosa [cuota de uso gratuita](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) para cuentas personales. Configura los [tiempos de espera](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) para detener o eliminar codespaces inactivos y así maximizar el uso de tu cuota.

## 1. Ejecución de Tareas

Cada lección tendrá tareas _opcionales_ que pueden estar disponibles en uno o más lenguajes de programación, incluyendo: Python, .NET/C#, Java y JavaScript/TypeScript. Esta sección ofrece una guía general para ejecutar esas tareas.

### 1.1 Tareas en Python

Las tareas en Python se proporcionan ya sea como aplicaciones (`.py`) o como notebooks de Jupyter (`.ipynb`).  
- Para ejecutar el notebook, ábrelo en Visual Studio Code, luego haz clic en _Seleccionar Kernel_ (arriba a la derecha) y elige la opción predeterminada de Python 3. Ahora puedes usar _Ejecutar todo_ para ejecutar el notebook.  
- Para ejecutar aplicaciones Python desde la línea de comandos, sigue las instrucciones específicas de la tarea para asegurarte de seleccionar los archivos correctos y proporcionar los argumentos requeridos.

## 2. Configuración de Proveedores

Las tareas **pueden** estar configuradas para funcionar con uno o más despliegues de Modelos de Lenguaje Grande (LLM) a través de un proveedor de servicios compatible como OpenAI, Azure o Hugging Face. Estos ofrecen un _endpoint alojado_ (API) al que podemos acceder programáticamente con las credenciales adecuadas (clave API o token). En este curso, tratamos los siguientes proveedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) con diversos modelos, incluyendo la serie principal GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI con enfoque en preparación empresarial.  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos de código abierto y servidor de inferencia.

**Necesitarás usar tus propias cuentas para estos ejercicios**. Las tareas son opcionales, por lo que puedes elegir configurar uno, todos o ninguno de los proveedores según tus intereses. Aquí tienes una guía para el registro:

| Registro | Costo | Clave API | Playground | Comentarios |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Precios](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Por proyecto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sin código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Múltiples modelos disponibles |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Precios](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [Inicio rápido SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Inicio rápido Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Se debe solicitar acceso previamente](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Precios](https://huggingface.co/pricing) | [Tokens de acceso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat tiene modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sigue las indicaciones a continuación para _configurar_ este repositorio para usar diferentes proveedores. Las tareas que requieran un proveedor específico tendrán una de estas etiquetas en el nombre del archivo:  
 - `aoai` - requiere endpoint y clave de Azure OpenAI  
 - `oai` - requiere endpoint y clave de OpenAI  
 - `hf` - requiere token de Hugging Face

Puedes configurar uno, ninguno o todos los proveedores. Las tareas relacionadas simplemente mostrarán error si faltan las credenciales.

###  2.1. Crear archivo `.env`

Asumimos que ya has leído la guía anterior, te has registrado con el proveedor correspondiente y has obtenido las credenciales de autenticación necesarias (API_KEY o token). En el caso de Azure OpenAI, también asumimos que tienes un despliegue válido de un servicio Azure OpenAI (endpoint) con al menos un modelo GPT desplegado para chat.

El siguiente paso es configurar tus **variables de entorno locales** de la siguiente manera:

1. Busca en la carpeta raíz un archivo `.env.copy` que debería tener un contenido similar a este:

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

2. Copia ese archivo a `.env` usando el siguiente comando. Este archivo está _gitignoreado_, manteniendo los secretos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Completa los valores (reemplaza los marcadores a la derecha del `=`) como se describe en la siguiente sección.

3. (Opcional) Si usas GitHub Codespaces, tienes la opción de guardar las variables de entorno como _secretos de Codespaces_ asociados a este repositorio. En ese caso, no necesitarás configurar un archivo .env local. **Sin embargo, ten en cuenta que esta opción solo funciona si usas GitHub Codespaces.** Aún necesitarás configurar el archivo .env si usas Docker Desktop.

### 2.2. Completar archivo `.env`

Veamos rápidamente los nombres de las variables para entender qué representan:

| Variable  | Descripción  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este es el token de acceso de usuario que configuraste en tu perfil |
| OPENAI_API_KEY | Esta es la clave de autorización para usar el servicio en endpoints OpenAI no Azure |
| AZURE_OPENAI_API_KEY | Esta es la clave de autorización para usar ese servicio |
| AZURE_OPENAI_ENDPOINT | Este es el endpoint desplegado para un recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este es el endpoint de despliegue del modelo de _generación de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este es el endpoint de despliegue del modelo de _embeddings de texto_ |
| | |

Nota: Las dos últimas variables de Azure OpenAI corresponden a un modelo predeterminado para chat (generación de texto) y búsqueda vectorial (embeddings) respectivamente. Las instrucciones para configurarlas se definirán en las tareas correspondientes.

### 2.3 Configurar Azure: Desde el Portal

Los valores del endpoint y la clave de Azure OpenAI se encuentran en el [Portal de Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), así que comencemos por ahí.

1. Ve al [Portal de Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Haz clic en la opción **Claves y Endpoint** en la barra lateral (menú a la izquierda).  
1. Haz clic en **Mostrar claves** - deberías ver lo siguiente: CLAVE 1, CLAVE 2 y Endpoint.  
1. Usa el valor de CLAVE 1 para AZURE_OPENAI_API_KEY  
1. Usa el valor del Endpoint para AZURE_OPENAI_ENDPOINT

Luego, necesitamos los endpoints para los modelos específicos que hemos desplegado.

1. Haz clic en la opción **Despliegues de modelos** en la barra lateral (menú izquierdo) del recurso Azure OpenAI.  
1. En la página destino, haz clic en **Administrar despliegues**

Esto te llevará al sitio web de Azure OpenAI Studio, donde encontraremos los otros valores como se describe a continuación.

### 2.4 Configurar Azure: Desde Studio

1. Navega a [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **desde tu recurso** como se describió arriba.  
1. Haz clic en la pestaña **Despliegues** (barra lateral, izquierda) para ver los modelos actualmente desplegados.  
1. Si el modelo que deseas no está desplegado, usa **Crear nuevo despliegue** para desplegarlo.  
1. Necesitarás un modelo de _generación de texto_ - recomendamos: **gpt-35-turbo**  
1. Necesitarás un modelo de _embedding de texto_ - recomendamos **text-embedding-ada-002**

Ahora actualiza las variables de entorno para reflejar el _nombre del despliegue_ usado. Esto normalmente será igual al nombre del modelo a menos que lo hayas cambiado explícitamente. Por ejemplo, podrías tener:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**No olvides guardar el archivo .env cuando termines**. Ahora puedes cerrar el archivo y volver a las instrucciones para ejecutar el notebook.

### 2.5 Configurar OpenAI: Desde Perfil

Tu clave API de OpenAI se puede encontrar en tu [cuenta de OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Si no tienes una, puedes registrarte y crear una clave API. Una vez que tengas la clave, úsala para completar la variable `OPENAI_API_KEY` en el archivo `.env`.

### 2.6 Configurar Hugging Face: Desde Perfil

Tu token de Hugging Face se encuentra en tu perfil bajo [Tokens de acceso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). No publiques ni compartas estos públicamente. En su lugar, crea un nuevo token para el uso de este proyecto y cópialo en el archivo `.env` bajo la variable `HUGGING_FACE_API_KEY`. _Nota:_ Técnicamente esto no es una clave API, pero se usa para autenticación, por lo que mantenemos esta convención de nombres para consistencia.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.