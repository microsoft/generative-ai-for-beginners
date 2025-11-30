<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:50:05+00:00",
  "source_file": "AGENTS.md",
  "language_code": "es"
}
-->
# AGENTS.md

## Resumen del Proyecto

Este repositorio contiene un plan de estudios completo de 21 lecciones que enseña los fundamentos de la IA Generativa y el desarrollo de aplicaciones. El curso está diseñado para principiantes y abarca desde conceptos básicos hasta la creación de aplicaciones listas para producción.

**Tecnologías Clave:**
- Python 3.9+ con las bibliotecas: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript con Node.js y las bibliotecas: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API y Modelos de GitHub
- Jupyter Notebooks para aprendizaje interactivo
- Contenedores de desarrollo para un entorno de desarrollo consistente

**Estructura del Repositorio:**
- 21 directorios de lecciones numerados (00-21) que contienen READMEs, ejemplos de código y tareas
- Múltiples implementaciones: Python, TypeScript y, en ocasiones, ejemplos en .NET
- Directorio de traducciones con versiones en más de 40 idiomas
- Configuración centralizada mediante el archivo `.env` (usar `.env.copy` como plantilla)

## Comandos de Configuración

### Configuración Inicial del Repositorio

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Configuración del Entorno de Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuración de Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configuración del Contenedor de Desarrollo (Recomendado)

El repositorio incluye una configuración `.devcontainer` para GitHub Codespaces o contenedores de desarrollo en VS Code:

1. Abre el repositorio en GitHub Codespaces o VS Code con la extensión de contenedores de desarrollo.
2. El contenedor de desarrollo automáticamente:
   - Instalará las dependencias de Python desde `requirements.txt`
   - Ejecutará el script posterior a la creación (`.devcontainer/post-create.sh`)
   - Configurará el kernel de Jupyter

## Flujo de Trabajo de Desarrollo

### Variables de Entorno

Todas las lecciones que requieren acceso a API utilizan variables de entorno definidas en `.env`:

- `OPENAI_API_KEY` - Para la API de OpenAI
- `AZURE_OPENAI_API_KEY` - Para el servicio Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL del endpoint de Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Nombre del despliegue del modelo de completado de chat
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nombre del despliegue del modelo de embeddings
- `AZURE_OPENAI_API_VERSION` - Versión de la API (por defecto: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Para modelos de Hugging Face
- `GITHUB_TOKEN` - Para modelos de GitHub

### Ejecución de Ejemplos en Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Ejecución de Ejemplos en TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Ejecución de Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Trabajo con Diferentes Tipos de Lecciones

- **Lecciones "Learn"**: Se centran en la documentación README.md y conceptos.
- **Lecciones "Build"**: Incluyen ejemplos de código funcional en Python y TypeScript.
- Cada lección tiene un README.md con teoría, recorridos de código y enlaces a contenido en video.

## Guías de Estilo de Código

### Python

- Usa `python-dotenv` para la gestión de variables de entorno.
- Importa la biblioteca `openai` para interacciones con la API.
- Usa `pylint` para análisis de código (algunos ejemplos incluyen `# pylint: disable=all` por simplicidad).
- Sigue las convenciones de nomenclatura de PEP 8.
- Almacena las credenciales de la API en el archivo `.env`, nunca en el código.

### TypeScript

- Usa el paquete `dotenv` para variables de entorno.
- Configuración de TypeScript en `tsconfig.json` para cada aplicación.
- Usa `@azure/openai` o `@azure-rest/ai-inference` para servicios de Azure.
- Usa `nodemon` para desarrollo con recarga automática.
- Compila antes de ejecutar: `npm run build` y luego `npm start`.

### Convenciones Generales

- Mantén los ejemplos de código simples y educativos.
- Incluye comentarios que expliquen conceptos clave.
- El código de cada lección debe ser autónomo y ejecutable.
- Usa nombres consistentes: prefijo `aoai-` para Azure OpenAI, `oai-` para OpenAI API, `githubmodels-` para Modelos de GitHub.

## Guías de Documentación

### Estilo de Markdown

- Todas las URLs deben estar envueltas en formato `[texto](../../url)` sin espacios adicionales.
- Los enlaces relativos deben comenzar con `./` o `../`.
- Todos los enlaces a dominios de Microsoft deben incluir el ID de seguimiento: `?WT.mc_id=academic-105485-koreyst`.
- No se permiten locales específicos de país en las URLs (evitar `/en-us/`).
- Las imágenes se almacenan en la carpeta `./images` con nombres descriptivos.
- Usa caracteres en inglés, números y guiones en los nombres de archivo.

### Soporte de Traducción

- El repositorio admite más de 40 idiomas mediante acciones automatizadas de GitHub.
- Las traducciones se almacenan en el directorio `translations/`.
- No se aceptan traducciones parciales.
- No se aceptan traducciones automáticas.
- Las imágenes traducidas se almacenan en el directorio `translated_images/`.

## Pruebas y Validación

### Verificaciones Antes de Enviar

Este repositorio utiliza GitHub Actions para validación. Antes de enviar PRs:

1. **Verificar Enlaces en Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Pruebas Manuales**:
   - Prueba ejemplos en Python: Activa el entorno virtual y ejecuta los scripts.
   - Prueba ejemplos en TypeScript: `npm install`, `npm run build`, `npm start`.
   - Verifica que las variables de entorno estén configuradas correctamente.
   - Comprueba que las claves de API funcionen con los ejemplos de código.

3. **Ejemplos de Código**:
   - Asegúrate de que todo el código se ejecute sin errores.
   - Prueba con Azure OpenAI y OpenAI API cuando sea aplicable.
   - Verifica que los ejemplos funcionen con Modelos de GitHub donde se admitan.

### Sin Pruebas Automatizadas

Este es un repositorio educativo enfocado en tutoriales y ejemplos. No hay pruebas unitarias ni de integración para ejecutar. La validación es principalmente:
- Pruebas manuales de ejemplos de código.
- GitHub Actions para validación de Markdown.
- Revisión comunitaria del contenido educativo.

## Guías para Pull Requests

### Antes de Enviar

1. Prueba los cambios de código en Python y TypeScript cuando sea aplicable.
2. Ejecuta la validación de Markdown (se activa automáticamente en el PR).
3. Asegúrate de que los IDs de seguimiento estén presentes en todas las URLs de Microsoft.
4. Verifica que los enlaces relativos sean válidos.
5. Comprueba que las imágenes estén correctamente referenciadas.

### Formato del Título del PR

- Usa títulos descriptivos: `[Lección 06] Corrige error tipográfico en ejemplo de Python` o `Actualiza README para la lección 08`.
- Referencia números de problemas cuando sea aplicable: `Fixes #123`.

### Descripción del PR

- Explica qué se cambió y por qué.
- Enlaza problemas relacionados.
- Para cambios de código, especifica qué ejemplos se probaron.
- Para PRs de traducción, incluye todos los archivos para una traducción completa.

### Requisitos de Contribución

- Firma el CLA de Microsoft (automático en el primer PR).
- Haz un fork del repositorio en tu cuenta antes de realizar cambios.
- Un PR por cambio lógico (no combines correcciones no relacionadas).
- Mantén los PRs enfocados y pequeños cuando sea posible.

## Flujos de Trabajo Comunes

### Agregar un Nuevo Ejemplo de Código

1. Navega al directorio de la lección correspondiente.
2. Crea el ejemplo en el subdirectorio `python/` o `typescript/`.
3. Sigue la convención de nombres: `{proveedor}-{nombre-ejemplo}.{py|ts|js}`.
4. Prueba con credenciales reales de API.
5. Documenta cualquier nueva variable de entorno en el README de la lección.

### Actualizar Documentación

1. Edita el README.md en el directorio de la lección.
2. Sigue las guías de Markdown (IDs de seguimiento, enlaces relativos).
3. Las actualizaciones de traducciones son manejadas por GitHub Actions (no las edites manualmente).
4. Prueba que todos los enlaces sean válidos.

### Trabajar con Contenedores de Desarrollo

1. El repositorio incluye `.devcontainer/devcontainer.json`.
2. El script posterior a la creación instala automáticamente las dependencias de Python.
3. Las extensiones para Python y Jupyter están preconfiguradas.
4. El entorno se basa en `mcr.microsoft.com/devcontainers/universal:2.11.2`.

## Despliegue y Publicación

Este es un repositorio de aprendizaje: no hay un proceso de despliegue. El plan de estudios se consume mediante:

1. **Repositorio de GitHub**: Acceso directo al código y documentación.
2. **GitHub Codespaces**: Entorno de desarrollo instantáneo con configuración preestablecida.
3. **Microsoft Learn**: El contenido puede ser sindicado en la plataforma oficial de aprendizaje.
4. **docsify**: Sitio de documentación construido a partir de Markdown (ver `docsifytopdf.js` y `package.json`).

### Construcción del Sitio de Documentación

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Solución de Problemas

### Problemas Comunes

**Errores de Importación en Python**:
- Asegúrate de que el entorno virtual esté activado.
- Ejecuta `pip install -r requirements.txt`.
- Verifica que la versión de Python sea 3.9+.

**Errores de Compilación en TypeScript**:
- Ejecuta `npm install` en el directorio de la aplicación específica.
- Verifica que la versión de Node.js sea compatible.
- Limpia `node_modules` y reinstala si es necesario.

**Errores de Autenticación en API**:
- Verifica que el archivo `.env` exista y tenga valores correctos.
- Comprueba que las claves de API sean válidas y no hayan expirado.
- Asegúrate de que las URLs de los endpoints sean correctas para tu región.

**Variables de Entorno Faltantes**:
- Copia `.env.copy` a `.env`.
- Rellena todos los valores requeridos para la lección en la que estás trabajando.
- Reinicia tu aplicación después de actualizar `.env`.

## Recursos Adicionales

- [Guía de Configuración del Curso](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Guías de Contribución](./CONTRIBUTING.md)
- [Código de Conducta](./CODE_OF_CONDUCT.md)
- [Política de Seguridad](./SECURITY.md)
- [Discord de Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Colección de Ejemplos de Código Avanzados](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notas Específicas del Proyecto

- Este es un repositorio **educativo** enfocado en el aprendizaje, no en código de producción.
- Los ejemplos están diseñados para ser simples y centrados en enseñar conceptos.
- La calidad del código se equilibra con la claridad educativa.
- Cada lección es autónoma y puede completarse de forma independiente.
- El repositorio admite múltiples proveedores de API: Azure OpenAI, OpenAI y Modelos de GitHub.
- El contenido es multilingüe con flujos de trabajo de traducción automatizados.
- Comunidad activa en Discord para preguntas y soporte.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.