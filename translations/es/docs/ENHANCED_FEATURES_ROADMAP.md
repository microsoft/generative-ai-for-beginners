# Hoja de Ruta de Funcionalidades Mejoradas y Mejoras

Este documento describe las mejoras y optimizaciones recomendadas para el plan de estudios de Generative AI for Beginners, basadas en una revisión integral del código y un análisis de las mejores prácticas de la industria.

## Resumen Ejecutivo

Se ha analizado la base de código en cuanto a seguridad, calidad de código y efectividad educativa. Este documento proporciona recomendaciones para correcciones inmediatas, mejoras a corto plazo y mejoras futuras.

---

## 1. Mejoras de Seguridad (Prioridad: Crítica)

### 1.1 Correcciones Inmediatas (Completadas)

| Problema | Archivos Afectados | Estado |
|---------|-------------------|--------|
| SECRET_KEY codificada | `05-advanced-prompts/python/aoai-solution.py` | Corregido |
| Falta validación de entorno | Múltiples archivos JS/TS | Corregido |
| Llamadas a funciones inseguras | `11-integrating-with-function-calling/js-githubmodels/app.js` | Corregido |
| Fugas de manejadores de archivos | `08-building-search-applications/scripts/` | Corregido |
| Falta de timeouts en requests | `09-building-image-applications/python/` | Corregido |

### 1.2 Funcionalidades adicionales recomendadas de seguridad

1. **Ejemplos de Limitación de Tasa**
   - Añadir código ejemplo que muestre cómo implementar limitación de tasa para llamadas API
   - Demostrar patrones de retroceso exponencial

2. **Rotación de claves API**
   - Añadir documentación sobre mejores prácticas para rotar claves API
   - Incluir ejemplos de uso de Azure Key Vault o servicios similares

3. **Integración de Seguridad de Contenidos**
   - Añadir ejemplos usando Azure Content Safety API
   - Demostrar patrones de moderación de entradas/salidas

---

## 2. Mejoras en la Calidad del Código

### 2.1 Archivos de configuración añadidos

| Archivo | Propósito |
|---------|----------|
| `.eslintrc.json` | Reglas de linting para JavaScript/TypeScript |
| `.prettierrc` | Estándares de formateo de código |
| `pyproject.toml` | Configuración de herramientas Python (Black, Ruff, mypy) |

### 2.2 Utilidades compartidas creadas

Nuevo módulo `shared/python/` con:
- `env_utils.py` - Manejo de variables de entorno
- `input_validation.py` - Validación y saneamiento de entradas
- `api_utils.py` - Wrappers seguros para llamadas API

### 2.3 Mejoras recomendadas en el código

1. **Cobertura de anotaciones de tipo**
   - Añadir anotaciones de tipo a todos los archivos Python
   - Habilitar modo estricto en TypeScript para todos los proyectos TS

2. **Estándares de documentación**
   - Añadir docstrings a todas las funciones Python
   - Añadir comentarios JSDoc a todas las funciones JavaScript/TypeScript

3. **Framework de pruebas**
   - Añadir configuración pytest y pruebas de ejemplo _(completado: configuración pytest en `pyproject.toml`; pruebas de ejemplo para utilidades compartidas en [`tests/`](../../../tests) ejecutadas en CI)_
   - Añadir configuración Jest para JavaScript/TypeScript

---

## 3. Mejoras Educativas

### 3.1 Nuevos temas para lecciones

1. **Seguridad en aplicaciones de IA** (Propuesta Lección 22)
   - Ataques y defensas contra inyección de prompts
   - Gestión de claves API
   - Moderación de contenido
   - Limitación de tasa y prevención de abuso

2. **Despliegue en producción** (Propuesta Lección 23)
   - Contenerización con Docker
   - Pipelines CI/CD
   - Monitorización y logging
   - Gestión de costes

3. **Técnicas avanzadas de RAG** (Propuesta Lección 24)
   - Búsqueda híbrida (palabra clave + semántica)
   - Estrategias de reordenación
   - RAG multimodal
   - Métricas de evaluación

### 3.2 Mejoras en lecciones existentes

| Lección | Mejora recomendada |
|---------|--------------------|
| 06 - Generación de texto | Añadir ejemplos de respuesta en streaming |
| 07 - Aplicaciones de chat | Añadir patrones de memoria para conversación |
| 08 - Aplicaciones de búsqueda | Añadir comparación de bases de datos vectoriales |
| 09 - Generación de imágenes | Añadir ejemplos de edición/variación de imágenes |
| 11 - Llamada a funciones | Añadir llamada a funciones en paralelo |
| 15 - RAG | Añadir comparación de estrategias de chunking |
| 17 - Agentes de IA | Añadir orquestación multiagente |

---

## 4. Modernización de API

### 4.1 Patrones de API obsoletos (Migración completada)

Todos los ejemplos de Python y TypeScript para **chat** se han migrado de la API de Chat Completions a la **API de Responses** (`client.responses.create(...)` → `response.output_text`).

| Patrón antiguo | Patrón nuevo | Estado |
|--------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (API Responses) | Completado |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Completado |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | Paquete `openai` `client.responses.create()` → `response.output_text` | Completado |
| `df.append()` (pandas) | `pd.concat()` | Completado |

> **Nota:** Los ejemplos de Microsoft Foundry Models que usan el SDK `azure-ai-inference` / `@azure-rest/ai-inference` (`client.complete()`) permanecen en la API de Model Inference, la cual no soporta la API Responses. `AzureOpenAI()` se mantiene intencionadamente donde sigue siendo válido (incrustaciones y generación de imágenes).

### 4.2 Nuevas funcionalidades de API para demostrar

1. **Salidas estructuradas** (OpenAI)
   - Modo JSON
   - Llamada a funciones con esquemas estrictos

2. **Capacidades de visión**
   - Análisis de imágenes con GPT-4o (visión)
   - Prompts multimodales

3. **Herramientas integradas de API Responses** (reemplaza la antigua API Assistants)
   - Intérprete de código
   - Búsqueda de archivos
   - Búsqueda web y herramientas personalizadas

---

## 5. Mejoras en la Infraestructura

### 5.1 Mejoras en CI/CD

Implementado en [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Linting/formateo Python (Ruff + Black) es **obligatorio** en el módulo de utilidades mantenidas `shared/` y corre **de manera consultiva** en el resto del plan, además de una pasada consultiva ESLint para JavaScript/TypeScript. La línea base ilustrativa fue:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Escaneo de seguridad

Implementado en [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): Análisis CodeQL para Python y JavaScript/TypeScript (en push, pull request y semanal) más revisión de dependencias en pull requests. La línea base ilustrativa fue:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Mejoras en la experiencia del desarrollador

### 6.1 Mejoras en DevContainer

Implementado en [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) y [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): el contenedor ahora incluye Pylance, el formateador Black, Ruff, ESLint, Prettier y las extensiones de Copilot, habilita formateo al guardar ajustado a la configuración Black/Prettier del repositorio, e instala las herramientas de desarrollo (`ruff`, `black`, `mypy`, `pytest`) para que el [workflow de calidad de código](../../../.github/workflows/code-quality.yml) pueda reproducirse localmente. La imagen base `mcr.microsoft.com/devcontainers/universal` ya incluye Python y Node, por lo que no se requieren características extra. La línea base ilustrativa fue:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Área interactiva (Playground)

Considerar añadir:
- Notebooks Jupyter con claves API prellenadas (vía entorno)
- Demos Gradio/Streamlit para aprendices visuales
- Cuestionarios interactivos para evaluación de conocimientos

---

## 7. Soporte Multi-idioma

### 7.1 Cobertura actual de idiomas

| Tecnología | Lecciones cubiertas | Estado |
|------------|--------------------|---------|
| Python | Todas | Completo |
| TypeScript | 06-09, 11 | Parcial |
| JavaScript | 06-08, 11 | Parcial |
| .NET/C# | Algunas | Parcial |

### 7.2 Recomendaciones de añadidos

1. **Go** - Crecimiento en herramientas AI/ML
2. **Rust** - Aplicaciones críticas en rendimiento
3. **Java/Kotlin** - Aplicaciones empresariales

---

## 8. Optimización del rendimiento

### 8.1 Optimización a nivel de código

1. **Patrones Async/Await**
   - Añadir ejemplos async para procesamiento por lotes
   - Demostrar llamadas concurrentes a API

2. **Estrategias de caché**
   - Añadir ejemplos de caché de embeddings
   - Demostrar patrones de caché de respuestas

3. **Optimización de tokens**
   - Añadir ejemplos de uso de tiktoken
   - Demostrar técnicas de compresión de prompts

### 8.2 Ejemplos de optimización de costos

Añadir ejemplos que demuestren:
- Selección de modelo basada en complejidad de tarea
- Ingeniería de prompts para eficiencia en tokens
- Procesamiento por lotes en operaciones masivas

---

## 9. Accesibilidad e Internacionalización

### 9.1 Estado actual de las traducciones

Todas las traducciones están **completas** y son generadas automáticamente por el [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), que produce y mantiene más de 50 versiones del plan de estudios sincronizadas con la fuente en inglés. El contenido traducido está bajo `translations/` e imágenes localizadas bajo `translated_images/`; la lista completa de idiomas disponibles se publica en la parte superior del README del repositorio.

| Aspecto | Estado |
|--------|--------|
| Cobertura de traducción | Completa — 50+ idiomas, todas las lecciones |
| Método de traducción | Automatizado vía [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Mantenido sincronizado con la fuente en inglés | Sí — regenerado automáticamente |

### 9.2 Mejoras de accesibilidad

1. Añadir texto alternativo a todas las imágenes
2. Asegurar que los ejemplos de código tienen resaltado de sintaxis adecuado
3. Añadir transcripciones de video para todo el contenido audiovisual
4. Asegurar que el contraste de color cumple con las pautas WCAG

---

## 10. Prioridad de Implementación

### Fase 1: Inmediata (Semana 1-2)
- [x] Corregir problemas de seguridad críticos
- [x] Añadir configuración de calidad de código
- [x] Crear utilidades compartidas
- [x] Documentar directrices de seguridad

### Fase 2: Corto plazo (Semana 3-4)
- [x] Actualizar patrones de API obsoletos (Chat Completions → Responses API, Python + TypeScript)
- [ ] Añadir anotaciones de tipo a todos los archivos Python (completado para el módulo `shared/` mantenido; muestras de lecciones mantenidas simples)
- [x] Añadir workflows CI/CD para calidad de código
- [x] Crear workflow de escaneo de seguridad

### Fase 3: Mediano plazo (Mes 2-3)
- [ ] Añadir nueva lección de seguridad
- [ ] Añadir lección de despliegue en producción
- [x] Mejorar configuración del DevContainer
- [ ] Añadir demos interactivas

### Fase 4: Largo plazo (Mes 4+)
- [ ] Añadir lección avanzada de RAG
- [ ] Ampliar cobertura de idiomas
- [ ] Añadir suite de pruebas completa
- [ ] Crear programa de certificación

---

## Conclusión

Esta hoja de ruta proporciona un enfoque estructurado para mejorar el plan de estudios de Generative AI for Beginners. Al abordar preocupaciones de seguridad, modernizar APIs y añadir contenido educativo, el curso preparará mejor a los estudiantes para el desarrollo de aplicaciones de IA en el mundo real.

Para preguntas o contribuciones, por favor abra un issue en el repositorio de GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->