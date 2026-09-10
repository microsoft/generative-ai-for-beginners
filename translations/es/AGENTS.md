# AGENTS.md

## Descripción del Proyecto

Este repositorio contiene un currículo integral de 21 lecciones que enseña los fundamentos de la IA Generativa y el desarrollo de aplicaciones. El curso está diseñado para principiantes y cubre desde conceptos básicos hasta la creación de aplicaciones listas para producción.

**Tecnologías Clave:**
- Python 3.9+ con bibliotecas: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript con Node.js y bibliotecas: `openai` (Azure OpenAI vía el endpoint v1 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API y Microsoft Foundry Models (GitHub Models se jubilará a finales de julio de 2026)
- Jupyter Notebooks para aprendizaje interactivo
- Contenedores de desarrollo para un entorno de desarrollo consistente

**Estructura del Repositorio:**
- 21 directorios numerados de lecciones (00-21) que contienen README, ejemplos de código y ejercicios
- Múltiples implementaciones: ejemplos en Python, TypeScript y a veces .NET
- Directorio de traducciones con más de 40 versiones en distintos idiomas
- Configuración centralizada mediante archivo `.env` (usar `.env.copy` como plantilla)

## Comandos para Configuración

### Configuración Inicial del Repositorio

```bash
# Clona el repositorio
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copia la plantilla de entorno
cp .env.copy .env
# Edita .env con tus claves API y puntos finales
```

### Configuración del Entorno Python

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
# En macOS/Linux:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Configuración de Node.js/TypeScript

```bash
# Instalar dependencias a nivel raíz (para herramientas de documentación)
npm install

# Para ejemplos de TypeScript de lecciones individuales, navega a la lección específica:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configuración del Contenedor de Desarrollo (Recomendado)

El repositorio incluye una configuración `.devcontainer` para GitHub Codespaces o VS Code Dev Containers:

1. Abre el repositorio en GitHub Codespaces o en VS Code con la extensión de Dev Containers
2. El Contenedor de Desarrollo automáticamente:
   - Instala dependencias de Python desde `requirements.txt`
   - Ejecuta el script post-creación (`.devcontainer/post-create.sh`)
   - Configura el kernel de Jupyter

## Flujo de Trabajo de Desarrollo

### Variables de Entorno

Todas las lecciones que requieren acceso a la API usan variables de entorno definidas en `.env`:

- `OPENAI_API_KEY` - Para OpenAI API
- `AZURE_OPENAI_API_KEY` - Para Azure OpenAI en Microsoft Foundry (Azure OpenAI Service ahora es parte de Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL del endpoint de Azure OpenAI (endpoint del recurso Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nombre del despliegue del modelo de chat completions (valor por defecto: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nombre del despliegue del modelo de embeddings (valor por defecto: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Versión de API (valor por defecto: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Para modelos de Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint de Microsoft Foundry Models (catálogo de modelos multiproveedor)
- `AZURE_INFERENCE_CREDENTIAL` - Clave API de Microsoft Foundry Models (reemplaza el `GITHUB_TOKEN` que se jubilará)
- `AZURE_INFERENCE_CHAT_MODEL` - Modelo no de razonamiento (ejemplo: `Llama-3.3-70B-Instruct`) usado en los ejemplos con `temperature`, ya que los modelos de razonamiento no soportan controles de muestreo

### Convenciones de Modelos (importante)

- **El modelo chat por defecto es `gpt-5-mini`** - un modelo actual, no desaprobado, de **razonamiento**. A partir de 2026, los modelos más antiguos "mini" con capacidad de temperatura (`gpt-4o-mini`, `gpt-4.1-mini`) están *depreciándose*, por lo que el currículo estandariza en la familia GPT-5.
- **Los modelos de razonamiento rechazan `temperature` y `top_p`**, y usan `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) en lugar de `max_tokens`. No añadas `temperature`/`top_p`/`max_tokens` en ejemplos que llamen a `gpt-5-mini`.
- **Para demostrar `temperature`**, los ejemplos usan un modelo **Llama** (`Llama-3.3-70B-Instruct`) mediante el endpoint Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). Dirige modelos de razonamiento con ingeniería de prompts y controles de razonamiento en lugar de botones de muestreo.
- **El ajuste fino (lección 18)** mantiene `gpt-4.1-mini`: GPT-5 solo soporta ajuste fino por refuerzo (RFT), no el ajuste fino supervisado (SFT) mostrado allí.
- Las lecciones 20 (Mistral) y 21 (Meta) mantienen `temperature`/`max_tokens` porque apuntan a modelos Mistral/Llama, que los soportan.

### Ejecutando Ejemplos en Python

```bash
# Navegar al directorio de la lección
cd 06-text-generation-apps/python

# Ejecutar un script de Python
python aoai-app.py
```

### Ejecutando Ejemplos en TypeScript

```bash
# Navegar al directorio de la aplicación TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Compilar el código TypeScript
npm run build

# Ejecutar la aplicación
npm start
```

### Ejecutando Jupyter Notebooks

```bash
# Inicie Jupyter en la raíz del repositorio
jupyter notebook

# O use VS Code con la extensión de Jupyter
```

### Trabajando con Diferentes Tipos de Lecciones

- Lecciones de **"Aprendizaje"**: Enfocadas en la documentación de README.md y conceptos
- Lecciones de **"Construcción"**: Incluyen ejemplos funcionales en Python y TypeScript
- Cada lección tiene un README.md con teoría, walkthroughs de código y enlaces a contenido en video

## Guías de Estilo de Código

### Python

- Usar `python-dotenv` para manejo de variables de entorno
- Importar la biblioteca `openai` para interacciones con API
- Usar `pylint` para linting (algunos ejemplos incluyen `# pylint: disable=all` para simplicidad)
- Seguir la convención de nombres PEP 8
- Guardar credenciales API en `.env`, nunca en el código

### TypeScript

- Usar paquete `dotenv` para variables de entorno
- Configuración TypeScript en `tsconfig.json` para cada aplicación
- Usar paquete `openai` para Azure OpenAI (apuntar cliente al endpoint `/openai/v1/` y llamar a `client.responses.create`); usar `@azure-rest/ai-inference` para Microsoft Foundry Models
- Usar `nodemon` para desarrollo con recarga automática
- Compilar antes de ejecutar: `npm run build` y luego `npm start`

### Convenciones Generales

- Mantener los ejemplos de código simples y educativos
- Incluir comentarios explicando conceptos clave
- El código de cada lección debe ser autocontenible y ejecutable
- Usar nomenclatura consistente: prefijo `aoai-` para Azure OpenAI, `oai-` para OpenAI API, `githubmodels-` para Microsoft Foundry Models (prefijo legado de la era GitHub Models)

## Directrices para Documentación

### Estilo Markdown

- Todas las URL deben estar formateadas como `[texto](../../url)` sin espacios extra
- Los enlaces relativos deben comenzar con `./` o `../`
- Todos los enlaces a dominios Microsoft deben incluir ID de seguimiento: `?WT.mc_id=academic-105485-koreyst`
- No usar locales específicos de país en URL (evitar `/en-us/`)
- Las imágenes se almacenan en la carpeta `./images` con nombres descriptivos
- Usar caracteres ingleses, números y guiones en nombres de archivos

### Soporte para Traducciones

- El repositorio soporta más de 40 idiomas mediante GitHub Actions automatizadas
- Las traducciones se almacenan en el directorio `translations/`
- No enviar traducciones parciales
- No se aceptan traducciones automáticas
- Las imágenes traducidas se almacenan en el directorio `translated_images/`

## Pruebas y Validación

### Revisiones Previo a la Presentación

Este repositorio usa GitHub Actions para validación. Antes de enviar pull requests:

1. **Verificar enlaces Markdown**:
   ```bash
   # El flujo de trabajo validate-markdown.yml verifica:
   # - Rutas relativas rotas
   # - IDs de seguimiento faltantes en rutas
   # - IDs de seguimiento faltantes en URLs
   # - URLs con localización de país
   # - URLs externas rotas
   ```

2. **Pruebas manuales**:
   - Probar ejemplos en Python: activar venv y ejecutar scripts
   - Probar ejemplos en TypeScript: `npm install`, `npm run build`, `npm start`
   - Verificar que variables de entorno estén configuradas correctamente
   - Comprobar que las claves API funcionan con los ejemplos de código

3. **Ejemplos de código**:
   - Asegurarse de que todo el código corre sin errores
   - Probar con Azure OpenAI y OpenAI API cuando aplique
   - Verificar que los ejemplos funcionen con Microsoft Foundry Models cuando sean soportados

### Sin Pruebas Automatizadas

Este es un repositorio educativo enfocado en tutoriales y ejemplos. No hay pruebas unitarias ni de integración para ejecutar. La validación es principalmente:
- Pruebas manuales de ejemplos de código
- GitHub Actions para validación de Markdown
- Revisión comunitaria del contenido educativo

## Guías para Pull Requests

### Antes de Enviar

1. Probar cambios de código en Python y TypeScript cuando aplique
2. Ejecutar la validación de Markdown (se activa automáticamente en PR)
3. Asegurar que los ID de seguimiento estén presentes en todas las URL de Microsoft
4. Verificar que los enlaces relativos sean válidos
5. Confirmar que las imágenes estén correctamente referenciadas

### Formato del Título del PR

- Usar títulos descriptivos: `[Lesson 06] Corrige error tipográfico en ejemplo Python` o `Actualiza README de la lección 08`
- Referenciar números de issues cuando sea aplicable: `Fixes #123`

### Descripción del PR

- Explicar qué cambios se hicieron y por qué
- Enlazar issues relacionados
- Para cambios de código, especificar qué ejemplos se probaron
- Para PRs de traducción, incluir todos los archivos para una traducción completa

### Requisitos de Contribución

- Firmar CLA de Microsoft (automático en el primer PR)
- Hacer fork del repositorio en tu cuenta antes de hacer cambios
- Un PR por cambio lógico (no combinar correcciones no relacionadas)
- Mantener los PRs enfocados y pequeños cuando sea posible

## Flujos de Trabajo Comunes

### Añadiendo un Nuevo Ejemplo de Código

1. Navegar al directorio de la lección correspondiente
2. Crear el ejemplo en el subdirectorio `python/` o `typescript/`
3. Seguir la convención de nombres: `{proveedor}-{nombre-ejemplo}.{py|ts|js}`
4. Probar con credenciales API reales
5. Documentar cualquier nueva variable de entorno en el README de la lección

### Actualizando Documentación

1. Editar README.md en el directorio de la lección
2. Seguir guías Markdown (ID de seguimiento, enlaces relativos)
3. Las actualizaciones de traducciones son manejadas por GitHub Actions (no editar manualmente)
4. Probar que todos los enlaces son válidos

### Trabajando con Contenedores de Desarrollo

1. El repositorio incluye `.devcontainer/devcontainer.json`
2. El script post-creación instala automáticamente dependencias de Python
3. Extensiones para Python y Jupyter están preconfiguradas
4. El entorno se basa en `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Despliegue y Publicación

Este es un repositorio de aprendizaje - no hay proceso de despliegue. El currículo se consume mediante:

1. **Repositorio GitHub**: acceso directo a código y documentación
2. **GitHub Codespaces**: entorno de desarrollo instantáneo con configuración preestablecida
3. **Microsoft Learn**: el contenido puede ser sindicado a la plataforma oficial de aprendizaje
4. **docsify**: sitio de documentación construido desde Markdown (ver `docsifytopdf.js` y `package.json`)

### Construyendo el Sitio de Documentación

```bash
# Generar PDF a partir de la documentación (si es necesario)
npm run convert
```

## Solución de Problemas

### Problemas Comunes

**Errores de Importación en Python**:
- Asegúrate que el entorno virtual está activado
- Ejecutar `pip install -r requirements.txt`
- Verificar que la versión de Python sea 3.9+

**Errores de Compilación en TypeScript**:
- Ejecutar `npm install` en el directorio de la aplicación específica
- Verificar que la versión de Node.js sea compatible
- Limpiar `node_modules` y reinstalar si es necesario

**Errores de Autenticación API**:
- Verificar que el archivo `.env` exista y tenga los valores correctos
- Comprobar que las claves API sean válidas y no hayan expirado
- Asegurar que las URLs de endpoint sean correctas para tu región

**Variables de Entorno Faltantes**:
- Copiar `.env.copy` a `.env`
- Completar todos los valores requeridos para la lección en la que trabajas
- Reiniciar la aplicación después de actualizar `.env`

## Recursos Adicionales

- [Guía de Configuración del Curso](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Directrices de Contribución](./CONTRIBUTING.md)
- [Código de Conducta](./CODE_OF_CONDUCT.md)
- [Política de Seguridad](./SECURITY.md)
- [Discord de Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Colección de Ejemplos Avanzados de Código](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notas Específicas del Proyecto

- Este es un repositorio **educativo** enfocado en aprendizaje, no en código para producción
- Los ejemplos son intencionadamente simples y centrados en enseñar conceptos
- La calidad del código se balancea con la claridad educativa
- Cada lección es autónoma y puede completarse independientemente
- El repositorio soporta múltiples proveedores de API: Azure OpenAI, OpenAI, Microsoft Foundry Models y proveedores offline como Foundry Local y Ollama
- El contenido es multilingüe con flujos de trabajo automáticos de traducción
- Comunidad activa en Discord para preguntas y soporte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->