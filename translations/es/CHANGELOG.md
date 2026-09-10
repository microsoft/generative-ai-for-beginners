# Registro de cambios

Todos los cambios notables en el plan de estudios de IA Generativa para Principiantes están documentados en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Como este es un
plan de estudios de aprendizaje en lugar de un paquete de software versionado, las entradas están agrupadas por fecha.

## [2026-07-16] — Validación de contenido + Recursos de imágenes de la lección 09

### Cambiado

- **Lección 10 (aplicaciones de IA low-code):** actualizados dos enlaces retirados de `docs.microsoft.com/powerapps/...` de Dataverse
  a `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro`
  (verificado en vivo).
- **Lección 17 (agentes de IA):** modernizado un ejemplo de modelo anticuado (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, y Llama 3.3`) y un nombre de implementación provisional en el ejemplo del Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **`README.md` raíz:** añadido el ID de seguimiento faltante `?WT.mc_id=academic-105485-koreyst` al
  enlace *Microsoft for Startups*.
- **Recursos de imágenes de la lección 09** regenerados con el modelo `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` y
  `images/startup.png` (el par antes/después del ejemplo de edición se produjo mediante una llamada real
  `client.images.edit` con una máscara generada).

### Validado

- Auditado los README de las lecciones 01, 03, 05, 12, 14 y 16 — todos actuales (nombres y enlaces correctos de Microsoft Foundry);
  no se requieren cambios.
- Ejecutada una validación completa de markdown en los 41 archivos markdown del repositorio (excluidas traducciones)
  para rutas de documentación obsoletas, locales Microsoft `/en-us/`, nombres antiguos de productos/modelos,
  IDs de seguimiento faltantes y enlaces/imágenes relativas rotas. Solo se pudo corregir la única brecha del ID de
  seguimiento *Microsoft for Startups*; todas las demás señales fueron confirmadas como falsos positivos (enlaces de traducción automáticos,
  marcadores desactivados y URLs estructurales de terceros `/en/`).

## [2026-07-15] — Reescritura de la lección 09 (Aplicaciones de Imagen) para modelos de imagen GPT

### Cambiado

- **Reescrita la lección 09 "Construyendo aplicaciones de generación de imagen"** alrededor de la familia moderna **`gpt-image`**
  de modelos (por defecto **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` también GA), reemplazando el
  contenido legado de DALL·E 2/3. Correcciones clave:
  - Los modelos `gpt-image` devuelven la imagen como **base64 (`b64_json`)**, no una URL. Se actualizaron todos los ejemplos para usar
    `base64.b64decode(...)` en lugar de descargar una `url` con `requests`.
  - Se actualizó la versión de la API de imagen a `2025-04-01-preview`.

  - Reemplazada la sección fabricada "temperatura" (los modelos de imagen no usan `temperature`) y el
    contenido de **variaciones** de imagen exclusivo de DALL·E-2 por una sección de **edición de imágenes** (máscara/re-pintado).
  - Actualizados `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, ambos
    cuadernos de asignaciones (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), y el cuaderno .NET `.dib`.

### Eliminado

- Eliminados los ejemplos obsoletos `python/aoai-app-variation.py` y `python/oai-app-variation.py`
  (`images.create_variation` es exclusivo de DALL·E-2 y no compatible con `gpt-image`).
- Eliminados 4 recursos de imagen huérfanos ligados a la sección eliminada de comparación de temperatura
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Se eliminó la dependencia innecesaria `requests` de los ejemplos de Python y requisitos de la lección.

### Validado

- Ejecutado `aoai-app.py` de extremo a extremo contra un modelo desplegado `gpt-image-1.5` y confirmado que el flujo de
  decodificación/guardado base64 produce un PNG. Cuadernos confirmados como JSON válido.

## [2026-07-14] — Actualización del modelo predeterminado + Guía de modelo de razonamiento

### Cambiado

- **Modelo de chat predeterminado `gpt-4o-mini` → `gpt-5-mini`** en todos los ejemplos ejecutables del currículo,
  documentación y configuración. Esto se debe al ciclo de vida del modelo: en Microsoft Foundry,
  `gpt-4o-mini` (se retira 2026-10-01) y toda la familia `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, se retiran 2026-10-14) están **en desuso**, mientras que la **familia GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) está Generalmente Disponible** (se retira 2027-02-06). Actualizado:
  - `.env.copy`, `00-course-setup/03-providers.md` (despliegue recomendado y comandos `az cognitiveservices`
    de despliegue), y los README de las lecciones 04, 06, 07 y 15.
  - Ejemplos en Python en la lección 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) y scripts de la lección 08.
  - Ejemplos en TypeScript / JavaScript en las lecciones 06, 07 y 11, y los cuadernos `.dib` .NET para
    las lecciones 06 y 07.
  - Cuadernos de asignación en las lecciones 04, 06, 07 y 11 (celdas de código), más ejemplos de docstring en `shared/python/api_utils.py`.
    .

- **Guía de parámetros para el modelo de razonamiento (nuevo).** `gpt-5-mini` es un modelo de *razonamiento*: no 
  admite `temperature`/`top_p`, y utiliza `max_completion_tokens` (chat completions) / 
  `max_output_tokens` (Responses API) en lugar de `max_tokens`. En consecuencia:

  - Se eliminaron `temperature`/`top_p`/`max_tokens` de las muestras que ahora usan por defecto `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, README de la lección 15 RAG).
  - Se añadió una nota **"Los modelos de razonamiento no usan `temperature`"** a la lección 06, explicando que
    los modelos de razonamiento se guían con **ingeniería de prompts + controles de razonamiento** en lugar de
    perillas de muestreo, mientras que `temperature`/`top_p` siguen siendo válidos en modelos no de razonamiento
    (GPT-4.x, Mistral, Llama, Phi, modelos abiertos).
- **`gpt-5-mini` no se usa para el tutorial de fine-tuning (lección 18).** GPT-5 solo soporta
  fine-tuning por refuerzo (RFT); el recorrido de fine-tuning supervisado (SFT) de la lección 18 mantiene
  `gpt-4.1-mini`, que soporta SFT/DPO.
- **Las demos de Temperature usan un modelo Llama.** Para seguir enseñando `temperature` (que los modelos de razonamiento
  rechazan), se usa un modelo `Llama-3.3-70B-Instruct` a través del endpoint Foundry Models. Se añadió una nueva
  variable `AZURE_INFERENCE_CHAT_MODEL` a `.env.copy`; los notebooks `githubmodels` de la lección 04/06 y
  la muestra `06` `js-githubmodels` la leen (usando `Llama-3.3-70B-Instruct` como fallback) y mantienen
  sus demos de `temperature`/`top_p`/`max_tokens`.
- **Muestras JS / .NET actualizadas para GPT-5.** Se eliminaron `temperature`/`top_p`/`max_tokens` de las
  muestras GPT-5 (`06` `recipe-app` TypeScript, `06` `.dib` .NET — que también eleva `MaxOutputTokenCount`
  para que la salida de razonamiento no se trunque). La muestra `06` `js-githubmodels` ahora usa Llama para mantener
  su demo de temperature. El `.dib` señala que `Azure.AI.Inference` + un modelo Llama es la forma de
  demostrar `Temperature` en .NET.
- Se dejaron `gpt-4o-mini` / `gpt-5-mini` donde siguen siendo precisos: referencias de codificación de tokens `tiktoken`,
  listas de disponibilidad del catálogo de modelos, y modelos de voz de la lección 02 (`gpt-4o-transcribe`).
- Las muestras de la lección 20 (Mistral) y 21 (Meta) mantienen `temperature`/`max_tokens` porque apuntan a
  modelos Mistral/Llama, que soportan esos parámetros.

## [2026-07-06] — Actualización de modernización de contenido

Una actualización amplia para mantener el currículo preciso para 2026: APIs modernas, nombres actuales de productos y
nombres de modelos, guía actualizada para proveedores, y nuevas herramientas para la experiencia del desarrollador.

### Añadido

- Sección **Microsoft Agent Framework** en la lección `17-ai-agents` cubriendo agentes de chat únicos,
  llamadas a herramientas/funciones, configuración de Azure OpenAI (Microsoft Foundry), y orquestación del flujo de trabajo multi-agente
  (`SequentialBuilder` / `ConcurrentBuilder`).
- Documentado **Foundry Local** como proveedor offline/en dispositivo (junto a Ollama) en
  `00-course-setup/03-providers.md` y la lección `19-slm`.
- **Flujos de trabajo de integración continua**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (aplicado en el módulo mantenido `shared/`,
    asesoría en el resto del currículo), una pasada asesora ESLint, y un trabajo pytest.
  - `.github/workflows/security.yml` — Análisis CodeQL (Python + JavaScript/TypeScript) y
    revisión de dependencias en pull requests.
- **Suite de pruebas** bajo `tests/` — 41 tests pytest que cubren el módulo utilitario compartido.
- Habilidad **Migración Azure OpenAI → Responses API** bajo
  `.github/skills/azure-openai-to-responses/` usada para guiar la migración de la API.

### Cambiado

- **Chat Completions API → Responses API** en todas las muestras de chat Python y TypeScript
  (`client.responses.create(...)` → `response.output_text`), incluyendo lecciones 04, 06, 07, 11,
  15 y 18, además de sus READMEs.
- **GitHub Models → Microsoft Foundry Models** en todo el texto, enlaces y muestras. GitHub Models
  se retira a finales de julio de 2026; las muestras ahora apuntan al catálogo de modelos Microsoft Foundry y usan
  las variables de entorno `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, y documentación de proveedores** actualizados para reflejar que Azure OpenAI ahora es parte
  de Microsoft Foundry, y la versión API predeterminada actualizada a `2024-10-21`.
- **Muestras TypeScript** (lecciones 06, 07, 08, 11) migradas fuera del SDK beta deprecated `@azure/openai`
  al paquete `openai` (las aplicaciones de chat usan la Responses API; la app de búsqueda usa el
  cliente de embeddings).
- **Notebooks .NET** (`dotnet/*.dib`) estandarizados en `Azure.AI.OpenAI` **2.1.0**: las lecciones 06 y 07
  usan la API `ChatClient`, la lección 08 usa `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), y
  la lección 09 usa `ImageClient` (`GenerateImage`) con `gpt-image-1`, reemplazando el legado
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` de `1.0.0-beta.9`.
- **Modernización de nombres de productos**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (lecciones 14, 16, 17) y "Bing" → **Microsoft Copilot** (lección 12), donde esos se referían a los
  productos actuales.
- **DevContainer** (`.devcontainer/`) ahora incluye extensiones Pylance, Black, Ruff, ESLint, Prettier, y Copilot,
  habilita formato al guardar, e instala `ruff`, `black`, `mypy` y `pytest` para que las comprobaciones CI
  se puedan reproducir localmente.
- La **generación de imágenes** (lección 09) recomienda `gpt-image-1` para Azure (el catálogo de Azure eliminó
  `dall-e-3`).

- **`docs/ENHANCED_FEATURES_ROADMAP.md`** actualizado para reflejar el trabajo completado (migración de API, CI,
  DevContainer, pruebas) y hechos actuales (las traducciones se producen automáticamente mediante el
  Azure Co-op Translator; la API de Asistentes está reemplazada por la API de Respuestas).

### Arreglado

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` ahora devuelve una
  cadena vacía para entradas que solo contienen espacios en blanco en lugar de generar un error de "demasiado corto" (consistente con el
  caso `None`). Encontrado y cubierto por la nueva suite de pruebas.
- **Muestras de imágenes de la Lección 09** — se corrigieron errores reales: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  y una variable que enmascaraba el módulo `openai`.
- **Cuaderno RAG de la Lección 15** — se reparó la configuración del cliente, se reemplazó el `DataFrame.append` eliminado
  con `pd.concat`, y se modernizó el uso del SDK antiguo.
- Nombres de modelos obsoletos / retirados (`gpt-3.5-turbo`, `gpt-35-turbo`) reemplazados por `gpt-4o-mini`
  en muestras activas; las salidas históricas de fine-tuning en la lección 18 se preservaron y anotaron
  en lugar de reescribirse.

### Obsoletos / Notas

- **Muestras de modelos Microsoft Foundry** que usan el SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — las muestras `githubmodels-*` y `js-githubmodels` y las lecciones 19, 20,
  y 21 — permanecen en la API de Inferencia de Modelos, que **no** soporta la API de Respuestas. Estos se
  dejaron intencionalmente en ese SDK.
- `AzureOpenAI()` se mantiene intencionalmente donde aún es apropiado (embeddings y generación de imágenes),
  ya que esos flujos de trabajo no forman parte de la migración a la API de Respuestas.
- Las referencias a `text-embedding-ada-002` se mantienen donde un índice de embedding precomputado depende de ellas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->