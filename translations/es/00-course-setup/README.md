# Comenzando con este curso

¡Estamos muy emocionados de que empieces este curso y veas qué te inspira a construir con IA Generativa!

Para asegurar tu éxito, esta página describe los pasos de configuración, los requisitos técnicos y dónde obtener ayuda si es necesario.

## Pasos de configuración

Para comenzar a tomar este curso, deberás completar los siguientes pasos.

### 1. Hacer un fork de este repositorio

[Haz un fork de todo este repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a tu propia cuenta de GitHub para poder cambiar cualquier código y completar los desafíos. También puedes [marcar con una estrella (🌟) este repositorio](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrarlo y repos relacionados más fácilmente.

### 2. Crear un codespace

Para evitar problemas con dependencias al ejecutar el código, recomendamos ejecutar este curso en un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

En tu fork: **Código -> Codespaces -> Nuevo en main**

![Diálogo mostrando botones para crear un codespace](../../../translated_images/es/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Agregar un secreto

1. ⚙️ Icono de engranaje -> Paleta de comandos-> Codespaces : Administrar secreto de usuario -> Agregar un nuevo secreto.
2. Nombre OPENAI_API_KEY, pega tu clave, Guarda.

### 3. ¿Qué sigue?

| Quiero...           | Ir a...                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Comenzar la Lección 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Trabajar sin conexión | [`setup-local.md`](02-setup-local.md)                                   |
| Configurar un Proveedor LLM | [`providers.md`](03-providers.md)                                        |
| Conocer a otros estudiantes | [Únete a nuestro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Solución de problemas


| Síntoma                                  | Solución                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Construcción del contenedor atascada > 10 min | **Codespaces ➜ “Reconstruir contenedor”**                       |
| `python: command not found`                | El terminal no se adjuntó; haz clic en **+** ➜ *bash*             |
| `401 Unauthorized` de OpenAI               | `OPENAI_API_KEY` incorrecta o expirada                            |
| VS Code muestra “Montaje de contenedor Dev…” | Actualiza la pestaña del navegador—Codespaces a veces pierde conexión |
| Kernel del notebook faltante               | Menú del notebook ➜ **Kernel ▸ Seleccionar Kernel ▸ Python 3**    |

   Sistemas basados en Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Editar el archivo `.env`**: Abre el archivo `.env` en un editor de texto (por ejemplo, VS Code, Notepad++, o cualquier otro editor). Agrega las siguientes líneas al archivo, reemplazando los marcadores de posición con tu endpoint y clave reales de Microsoft Foundry Models (consulta [`providers.md`](03-providers.md) para saber cómo obtenerlos):

   > **Nota:** GitHub Models (y su variable `GITHUB_TOKEN`) se retirará a finales de julio de 2026. Usa [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) en su lugar.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Guardar el archivo**: Guarda los cambios y cierra el editor de texto.

5. **Instalar `python-dotenv`**: Si aún no lo has hecho, necesitarás instalar el paquete `python-dotenv` para cargar variables de entorno desde el archivo `.env` en tu aplicación Python. Puedes instalarlo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Cargar variables de entorno en tu script de Python**: En tu script de Python, usa el paquete `python-dotenv` para cargar las variables de entorno desde el archivo `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Cargar variables de entorno desde el archivo .env
   load_dotenv()

   # Acceder a las variables de Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

¡Eso es todo! Has creado exitosamente un archivo `.env`, agregado tus credenciales de Microsoft Foundry Models y cargado en tu aplicación Python.

## Cómo ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, necesitarás tener alguna versión de [Python instalado](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para usar el repositorio, necesitas clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

¡Una vez que tengas todo listo, puedes comenzar!

## Pasos opcionales

### Instalando Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) es un instalador ligero para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, así como algunos paquetes.
Conda en sí es un gestor de paquetes que facilita configurar y cambiar entre diferentes [entornos virtuales](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) y paquetes de Python. También es útil para instalar paquetes que no están disponibles vía `pip`.

Puedes seguir la [guía de instalación de MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurarlo.

Con Miniconda instalado, necesitas clonar el [repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (si aún no lo has hecho)

Luego, necesitas crear un entorno virtual. Para hacerlo con Conda, crea un nuevo archivo de entorno (_environment.yml_). Si estás siguiendo usando Codespaces, créalo dentro del directorio `.devcontainer`, es decir, `.devcontainer/environment.yml`.

Ve y completa tu archivo de entorno con el siguiente fragmento:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

Si encuentras errores usando conda, puedes instalar manualmente las bibliotecas de Microsoft AI usando el siguiente comando en una terminal.

```
conda install -c microsoft azure-ai-ml
```

El archivo de entorno especifica las dependencias que necesitamos. `<environment-name>` se refiere al nombre que te gustaría usar para tu entorno Conda, y `<python-version>` es la versión de Python que quieres usar, por ejemplo, `3` es la última versión mayor de Python.

Con eso hecho, puedes crear tu entorno Conda ejecutando los siguientes comandos en tu línea de comandos/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # La subruta .devcontainer se aplica solo a configuraciones de Codespace
conda activate ai4beg
```

Consulta la [guía de entornos Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si tienes algún problema.

### Usar Visual Studio Code con la extensión de soporte para Python

Recomendamos usar el editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con la [extensión de soporte para Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Sin embargo, esto es más una recomendación que un requisito definitivo.

> **Nota**: Al abrir el repositorio del curso en VS Code, tienes la opción de configurar el proyecto dentro de un contenedor. Esto es por el [especial directorio `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) que se encuentra en el repositorio del curso. Más sobre esto más adelante.

> **Nota**: Una vez clonado y abierto el directorio en VS Code, te sugerirá automáticamente instalar una extensión de soporte para Python.

> **Nota**: Si VS Code te sugiere reabrir el repositorio en un contenedor, rechaza esta solicitud para usar la versión localmente instalada de Python.

### Usar Jupyter en el navegador

También puedes trabajar en el proyecto usando el entorno de [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directamente en el navegador. Tanto Jupyter clásico como [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) proporcionan un entorno de desarrollo bastante agradable con funciones como autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, ve a la terminal/línea de comandos, navega al directorio del curso y ejecuta:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Esto iniciará una instancia de Jupyter y la URL para acceder a ella se mostrará en la ventana de línea de comandos.

Una vez accedas a la URL, deberías ver el esquema del curso y poder navegar a cualquier archivo `*.ipynb`. Por ejemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Ejecutar en un contenedor

Una alternativa para configurar todo en tu computadora o Codespace es usar un [contenedor](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). La carpeta especial `.devcontainer` dentro del repositorio del curso hace posible que VS Code configure el proyecto dentro de un contenedor. Fuera de Codespaces, esto requerirá la instalación de Docker y, francamente, implica un poco de trabajo, por lo que recomendamos esto solo a quienes tienen experiencia trabajando con contenedores.

Una de las mejores formas de mantener tus claves API seguras cuando usas GitHub Codespaces es utilizando los Secretos de Codespace. Por favor, sigue la guía de [gestión de secretos en Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para aprender más al respecto.


## Lecciones y requisitos técnicos

El curso tiene lecciones de "Aprender" que explican conceptos de IA Generativa y lecciones de "Construir" con ejemplos prácticos en código en **Python** y **TypeScript** donde sea posible.

Para las lecciones de codificación, usamos Azure OpenAI en Microsoft Foundry. Necesitarás una suscripción de Azure y una clave API. El acceso es abierto - no se requiere solicitud - por lo que puedes [crear un recurso Microsoft Foundry y desplegar un modelo](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) para obtener tu endpoint y clave.

Cada lección de codificación también incluye un archivo `README.md` donde puedes ver el código y salidas sin ejecutar nada.

## Usando el servicio Azure OpenAI por primera vez

Si es la primera vez que trabajas con el servicio Azure OpenAI, sigue esta guía sobre cómo [crear y desplegar un recurso de Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando la API de OpenAI por primera vez

Si es tu primera vez usando la API de OpenAI, sigue la guía sobre cómo [crear y usar la interfaz.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conoce a otros estudiantes

Hemos creado canales en nuestro servidor oficial de Discord de la [Comunidad AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para que puedas conocer a otros estudiantes. Es una excelente forma de conectarte con otros emprendedores, creadores, estudiantes y cualquiera que quiera avanzar en IA Generativa.

[![Unirse al canal de discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

El equipo del proyecto también estará en este servidor de Discord para ayudar a cualquier estudiante.

## Contribuir

Este curso es una iniciativa de código abierto. Si ves áreas de mejora o problemas, por favor crea un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o registra un [issue en GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

El equipo del proyecto hará seguimiento de todas las contribuciones. Contribuir a código abierto es una manera increíble de construir tu carrera en IA Generativa.

La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia de Contribuidores (CLA) declarando que tienes el derecho y efectivamente nos otorgas los derechos para usar tu contribución. Para detalles, visita el sitio web del [CLA, Acuerdo de Licencia de Contribuidores](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: al traducir texto en este repositorio, asegúrate de no usar traducción automática. Verificaremos las traducciones a través de la comunidad, así que por favor solo colabora con traducciones en los idiomas que dominas.


Cuando envíes una solicitud de extracción, un bot CLA determinará automáticamente si necesitas proporcionar un CLA y decorará la PR apropiadamente (por ejemplo, etiqueta, comentario). Simplemente sigue las instrucciones proporcionadas por el bot. Solo necesitarás hacer esto una vez en todos los repositorios que usen nuestro CLA.

Este proyecto ha adoptado el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para más información, lee las Preguntas Frecuentes del Código de Conducta o contacta a [Email opencode](opencode@microsoft.com) con cualquier pregunta o comentario adicional.

## Empecemos

Ahora que has completado los pasos necesarios para completar este curso, comencemos con una [introducción a la IA Generativa y LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->