# Elegir y Configurar un Proveedor de LLM 🔑

Las tareas **pueden** también configurarse para trabajar contra uno o más despliegues de Modelos de Lenguaje Grande (LLM) a través de un proveedor de servicios compatible como OpenAI, Azure o Hugging Face. Estos proporcionan un _endpoint alojado_ (API) al que podemos acceder programáticamente con las credenciales adecuadas (clave API o token). En este curso, discutimos estos proveedores:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) con diversos modelos incluyendo la serie principal GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) para modelos OpenAI con enfoque en preparación empresarial
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) para un único endpoint y clave API para acceder a cientos de modelos de OpenAI, Meta, Mistral, Cohere, Microsoft y más (reemplaza GitHub Models, que será retirado a finales de julio 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) para modelos de código abierto y servidor de inferencia
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) o [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) si prefieres ejecutar modelos completamente offline en tu propio dispositivo, sin necesidad de suscripción en la nube

**Necesitarás usar tus propias cuentas para estos ejercicios**. Las tareas son opcionales, por lo que puedes elegir configurar uno, todos - o ninguno - de los proveedores según tus intereses. Algunas indicaciones para registrarte:

| Registro | Costo | Clave API | Playground | Comentarios |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Precios](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Por proyecto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Sin código, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Múltiples Modelos Disponibles |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Precios](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Inicio rápido](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Inicio rápido](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Debe Solicitar Acceso Previo](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Precios](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Página de Resumen del Proyecto](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Nivel gratuito disponible; un endpoint + clave para múltiples proveedores de modelos |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Precios](https://huggingface.co/pricing) | [Tokens de Acceso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat tiene modelos limitados](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratis (se ejecuta en tu dispositivo) | No requerido | [CLI/SDK Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Endpoint totalmente offline compatible con OpenAI |
| | | | | |

Sigue las instrucciones a continuación para _configurar_ este repositorio para usar con diferentes proveedores. Las tareas que requieran un proveedor específico contendrán una de estas etiquetas en su nombre de archivo:

- `aoai` - requiere endpoint y clave de Azure OpenAI
- `oai` - requiere endpoint y clave de OpenAI
- `hf` - requiere token de Hugging Face
- `githubmodels` - requiere endpoint y clave de Microsoft Foundry Models (GitHub Models se retira a finales de julio de 2026)

Puedes configurar uno, ninguno o todos los proveedores. Las tareas relacionadas simplemente fallarán si faltan credenciales.

## Crear archivo `.env`

Suponemos que ya has leído la guía anterior, te has registrado con el proveedor relevante y obtuviste las credenciales de autenticación requeridas (API_KEY o token). En el caso de Azure OpenAI, también asumimos que tienes un despliegue válido de un servicio Azure OpenAI (endpoint) con al menos un modelo GPT desplegado para chat.

El siguiente paso es configurar tus **variables de entorno locales** como sigue:

1. Busca en la carpeta raíz un archivo `.env.copy` que debería tener un contenido similar a este:

   ```bash
   # Proveedor OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI en Microsoft Foundry
   ## (El servicio Azure OpenAI ahora forma parte de Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ¡El valor predeterminado está establecido! (versión estable actual GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modelos Microsoft Foundry (catálogo de modelos multiproveedor, reemplaza a Modelos GitHub, que se retira a finales de julio de 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copia ese archivo a `.env` usando el comando abajo. Este archivo está _gitignore-ado_, manteniendo los secretos seguros.

   ```bash
   cp .env.copy .env
   ```

3. Llena los valores (reemplaza los marcadores de posición a la derecha del `=`) como se describe en la siguiente sección.

4. (Opcional) Si usas GitHub Codespaces, tienes la opción de guardar variables de entorno como _secretos de Codespaces_ asociados con este repositorio. En ese caso, no necesitarás configurar un archivo .env local. **Sin embargo, nota que esta opción solo funciona si usas GitHub Codespaces.** Aún necesitarás configurar el archivo .env si usas Docker Desktop.

## Completar archivo `.env`

Echémos un vistazo rápido a los nombres de las variables para entender qué representan:

| Variable  | Descripción  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Este es el token de acceso de usuario que configuras en tu perfil |
| OPENAI_API_KEY | Esta es la clave de autorización para usar el servicio para endpoints de OpenAI no Azure |
| AZURE_OPENAI_API_KEY | Esta es la clave de autorización para usar ese servicio |
| AZURE_OPENAI_ENDPOINT | Este es el endpoint desplegado de un recurso Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Este es el endpoint del despliegue del modelo de _generación de texto_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Este es el endpoint del despliegue del modelo de _incrustaciones de texto_ |
| AZURE_INFERENCE_ENDPOINT | Este es el endpoint para tu proyecto Microsoft Foundry, usado para Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Esta es la clave API para tu proyecto Microsoft Foundry |
| | |

Nota: Las últimas dos variables de Azure OpenAI reflejan un modelo por defecto para chat completions (generación de texto) y búsqueda vectorial (incrustaciones) respectivamente. Las instrucciones para configurarlas se definirán en tareas relevantes.

## Configurar Azure OpenAI: Desde Portal

> **Nota:** Azure OpenAI Service ahora es parte de [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Los recursos y despliegues aún se muestran en el Portal Azure, pero la gestión diaria de modelos (despliegues, playground, monitoreo) ahora ocurre en el portal Foundry en lugar del antiguo "Azure OpenAI Studio" independiente.

Los valores del endpoint y clave de Azure OpenAI se encontrarán en el [Portal de Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), así que comencemos allí.

1. Ve al [Portal de Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Haz clic en la opción **Claves y Endpoint** en la barra lateral (menú a la izquierda).
1. Haz clic en **Mostrar Claves** - deberías ver lo siguiente: CLAVE 1, CLAVE 2 y Endpoint.
1. Usa el valor de CLAVE 1 para AZURE_OPENAI_API_KEY
1. Usa el valor del Endpoint para AZURE_OPENAI_ENDPOINT

A continuación, necesitamos los endpoints para los modelos específicos que hemos desplegado.

1. Haz clic en la opción **Despliegues de modelos** en la barra lateral (menú izquierdo) para el recurso Azure OpenAI.
1. En la página de destino, haz clic en **Ir al portal Microsoft Foundry** (o **Administrar Despliegues**, dependiendo de tu tipo de recurso)

Esto te llevará al portal Microsoft Foundry, donde encontraremos los otros valores como se describe a continuación.

## Configurar Azure OpenAI: Desde portal Microsoft Foundry

1. Navega al [portal Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **desde tu recurso** como se describió arriba.
1. Haz clic en la pestaña **Despliegues** (barra lateral, izquierda) para ver los modelos actualmente desplegados.
1. Si tu modelo deseado no está desplegado, usa **Desplegar modelo** para desplegarlo desde el [catálogo de modelos](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Necesitarás un modelo de _generación de texto_ - recomendamos: **gpt-5-mini**
1. Necesitarás un modelo de _incrustación de texto_ - recomendamos **text-embedding-3-small**

Ahora actualiza las variables de entorno para reflejar el _nombre del despliegue_ usado. Esto normalmente será el mismo que el nombre del modelo a menos que lo hayas cambiado explícitamente. Así, como ejemplo, podrías tener:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**No olvides guardar el archivo .env cuando termines**. Ahora puedes salir del archivo y regresar a las instrucciones para ejecutar el cuaderno.

## Configurar OpenAI: Desde Perfil

Tu clave API de OpenAI puede encontrarse en tu [cuenta de OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Si no tienes una, puedes registrarte para obtener una cuenta y crear una clave API. Una vez que la tienes, puedes usarla para completar la variable `OPENAI_API_KEY` en el archivo `.env`.

## Configurar Hugging Face: Desde Perfil

Tu token de Hugging Face puede encontrarse en tu perfil bajo [Tokens de Acceso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). No publiques ni compartas estos públicamente. En su lugar, crea un nuevo token para el uso de este proyecto y cópialo en el archivo `.env` bajo la variable `HUGGING_FACE_API_KEY`. _Nota:_ Técnicamente esto no es una clave API pero se usa para autenticación, por lo que mantenemos esa convención de nombres por consistencia.

## Configurar Microsoft Foundry Models: Desde Portal

> **Nota:** GitHub Models será retirado a finales de julio de 2026. Microsoft Foundry Models es el reemplazo directo, ofreciendo el mismo catálogo de modelos para prueba gratuita y experiencia con Azure AI Inference SDK / OpenAI SDK.

1. Ve a [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) y crea (o abre) un proyecto Foundry.
1. Explora el [catálogo de modelos](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) y despliega un modelo, por ejemplo `gpt-5-mini`.
1. En la página de **Resumen** del proyecto, copia el **endpoint** y la **clave API**.
1. Usa el valor del endpoint para `AZURE_INFERENCE_ENDPOINT` y el valor de la clave para `AZURE_INFERENCE_CREDENTIAL` en tu archivo `.env`.

## Proveedores Offline / Locales

Si prefieres no usar una suscripción en la nube, puedes ejecutar modelos abiertos compatibles directamente en tu propio dispositivo:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - el runtime en dispositivo de Microsoft. Selecciona automáticamente el mejor proveedor de ejecución (NPU, GPU o CPU) y expone un endpoint compatible con OpenAI, por lo que puedes reutilizar la mayoría del código de ejemplo en este curso con cambios mínimos. Consulta la [documentación de Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para comenzar, o instala con `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - una alternativa popular para ejecutar modelos abiertos como Llama, Phi, Mistral y Gemma localmente.


Consulte [Lección 19: Construcción con SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) para ejemplos prácticos que usan ambas opciones.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->