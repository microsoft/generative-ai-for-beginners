<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T13:34:50+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "es"
}
-->
# Elegir y Configurar un Proveedor de LLM 🔑

Las tareas **también pueden** configurarse para funcionar con uno o más despliegues de Modelos de Lenguaje Grande (LLM) a través de un proveedor de servicios compatible como OpenAI, Azure o Hugging Face. Estos ofrecen un _endpoint alojado_ (API) al que podemos acceder de forma programática con las credenciales adecuadas (clave API o token). En este curso, hablamos de estos proveedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) con modelos diversos, incluyendo la serie principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) para modelos de OpenAI con enfoque empresarial
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos de código abierto y servidor de inferencia

**Necesitarás usar tus propias cuentas para estos ejercicios**. Las tareas son opcionales, así que puedes elegir configurar uno, todos, o ninguno de los proveedores según tus intereses. Algunas recomendaciones para el registro:

| Registro | Costo | Clave API | Playground | Comentarios |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Precios](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Por proyecto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sin código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Hay varios modelos disponibles |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Precios](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Debes solicitar acceso previamente](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Precios](https://huggingface.co/pricing) | [Tokens de acceso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tiene modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Sigue las instrucciones a continuación para _configurar_ este repositorio y usarlo con diferentes proveedores. Las tareas que requieren un proveedor específico tendrán una de estas etiquetas en su nombre de archivo:

- `aoai` - requiere endpoint y clave de Azure OpenAI
- `oai` - requiere endpoint y clave de OpenAI
- `hf` - requiere token de Hugging Face

Puedes configurar uno, ninguno o todos los proveedores. Las tareas relacionadas simplemente mostrarán error si faltan las credenciales.

## Crear archivo `.env`

Suponemos que ya leíste las recomendaciones anteriores, te registraste con el proveedor correspondiente y obtuviste las credenciales de autenticación necesarias (API_KEY o token). En el caso de Azure OpenAI, también suponemos que tienes un despliegue válido del servicio Azure OpenAI (endpoint) con al menos un modelo GPT desplegado para completar chats.

El siguiente paso es configurar tus **variables de entorno locales** de la siguiente manera:

1. Busca en la carpeta raíz un archivo `.env.copy` que debería tener un contenido como este:

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

2. Copia ese archivo a `.env` usando el siguiente comando. Este archivo está _gitignoreado_, así que tus secretos estarán protegidos.

   ```bash
   cp .env.copy .env
   ```

3. Rellena los valores (reemplaza los marcadores de posición a la derecha del `=`) como se describe en la siguiente sección.

4. (Opcional) Si usas GitHub Codespaces, tienes la opción de guardar las variables de entorno como _secrets de Codespaces_ asociados a este repositorio. En ese caso, no necesitarás configurar un archivo .env local. **Sin embargo, ten en cuenta que esta opción solo funciona si usas GitHub Codespaces.** Si usas Docker Desktop, igual tendrás que configurar el archivo .env.

## Rellenar el archivo `.env`

Veamos rápidamente los nombres de las variables para entender qué representan:

| Variable  | Descripción  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este es el token de acceso de usuario que configuras en tu perfil |
| OPENAI_API_KEY | Esta es la clave de autorización para usar el servicio en endpoints de OpenAI que no sean de Azure |
| AZURE_OPENAI_API_KEY | Esta es la clave de autorización para usar ese servicio |
| AZURE_OPENAI_ENDPOINT | Este es el endpoint desplegado para un recurso de Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este es el endpoint de despliegue del modelo de _generación de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este es el endpoint de despliegue del modelo de _embeddings de texto_ |
| | |

Nota: Las dos últimas variables de Azure OpenAI reflejan el modelo por defecto para completar chats (generación de texto) y búsqueda vectorial (embeddings) respectivamente. Las instrucciones para configurarlas se definirán en las tareas correspondientes.

## Configurar Azure: Desde el Portal

Los valores de endpoint y clave de Azure OpenAI se encuentran en el [Portal de Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), así que empecemos ahí.

1. Ve al [Portal de Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Haz clic en la opción **Keys and Endpoint** en la barra lateral (menú a la izquierda).
1. Haz clic en **Show Keys** - deberías ver lo siguiente: KEY 1, KEY 2 y Endpoint.
1. Usa el valor de KEY 1 para AZURE_OPENAI_API_KEY
1. Usa el valor de Endpoint para AZURE_OPENAI_ENDPOINT

Ahora necesitamos los endpoints de los modelos específicos que hemos desplegado.

1. Haz clic en la opción **Model deployments** en la barra lateral (menú izquierdo) del recurso Azure OpenAI.
1. En la página de destino, haz clic en **Manage Deployments**

Esto te llevará al sitio web de Azure OpenAI Studio, donde encontraremos los otros valores como se describe a continuación.

## Configurar Azure: Desde Studio

1. Ve a [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **desde tu recurso** como se indicó arriba.
1. Haz clic en la pestaña **Deployments** (barra lateral, izquierda) para ver los modelos desplegados actualmente.
1. Si el modelo que quieres no está desplegado, usa **Create new deployment** para desplegarlo.
1. Necesitarás un modelo de _generación de texto_ - recomendamos: **gpt-35-turbo**
1. Necesitarás un modelo de _embeddings de texto_ - recomendamos **text-embedding-ada-002**

Ahora actualiza las variables de entorno para reflejar el _nombre de despliegue_ usado. Normalmente será igual al nombre del modelo, a menos que lo hayas cambiado explícitamente. Por ejemplo, podrías tener:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**No olvides guardar el archivo .env cuando termines**. Ya puedes salir del archivo y volver a las instrucciones para ejecutar el notebook.

## Configurar OpenAI: Desde el Perfil

Tu clave API de OpenAI se encuentra en tu [cuenta de OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Si no tienes una, puedes registrarte y crear una clave API. Una vez que la tengas, puedes usarla para rellenar la variable `OPENAI_API_KEY` en el archivo `.env`.

## Configurar Hugging Face: Desde el Perfil

Tu token de Hugging Face se encuentra en tu perfil bajo [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). No lo publiques ni lo compartas. En su lugar, crea un nuevo token para usar en este proyecto y cópialo en el archivo `.env` bajo la variable `HUGGING_FACE_API_KEY`. _Nota:_ Técnicamente esto no es una clave API, pero se usa para autenticación, así que mantenemos esa convención de nombres por consistencia.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.