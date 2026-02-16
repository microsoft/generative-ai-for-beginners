# Comenzando con este curso

¡Estamos muy emocionados de que comiences este curso y veas qué te inspira a construir con IA Generativa!

Para asegurar tu éxito, esta página describe los pasos de configuración, los requisitos técnicos y dónde obtener ayuda si es necesario.

## Pasos de configuración

Para comenzar a tomar este curso, necesitarás completar los siguientes pasos.

### 1. Haz un fork de este repositorio

[Haz un fork de todo este repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a tu propia cuenta de GitHub para poder cambiar cualquier código y completar los desafíos. También puedes [marcar con una estrella (🌟) este repositorio](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrarlo y encontrar repos relacionados más fácilmente.

### 2. Crea un codespace

Para evitar cualquier problema de dependencias al ejecutar el código, recomendamos ejecutar este curso en un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

En tu fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/es/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Añade un secreto

1. ⚙️ Icono de engranaje -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Nombre OPENAI_API_KEY, pega tu clave, guarda.

### 3. ¿Qué sigue?

| Quiero…           | Ir a…                                                                  |
|-------------------|-------------------------------------------------------------------------|
| Empezar la Lección 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Trabajar sin conexión | [`setup-local.md`](02-setup-local.md)                                   |
| Configurar un proveedor LLM | [`providers.md`](03-providers.md)                                        |
| Conocer a otros estudiantes | [Únete a nuestro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Solución de problemas


| Síntoma                                     | Solución                                                        |
|---------------------------------------------|----------------------------------------------------------------|
| Compilación del contenedor atascada > 10 min | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                 | Terminal no se conectó; haz clic en **+** ➜ *bash*              |
| `401 Unauthorized` de OpenAI                | `OPENAI_API_KEY` incorrecta / expirada                          |
| VS Code muestra “Dev container mounting…”   | Actualiza la pestaña del navegador—A veces Codespaces pierde conexión |
| Falta el kernel del cuaderno                | Menú del cuaderno ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Sistemas basados en Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edita el archivo `.env`**: Abre el archivo `.env` en un editor de texto (por ejemplo, VS Code, Notepad++ u otro editor). Añade la siguiente línea al archivo, reemplazando `your_github_token_here` con tu token real de GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Guarda el archivo**: Guarda los cambios y cierra el editor de texto.

5. **Instala `python-dotenv`**: Si aún no lo has hecho, necesitarás instalar el paquete `python-dotenv` para cargar variables de entorno desde el archivo `.env` en tu aplicación Python. Puedes instalarlo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carga las variables de entorno en tu script Python**: En tu script Python, usa el paquete `python-dotenv` para cargar las variables de entorno desde el archivo `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Cargar variables de entorno desde el archivo .env
   load_dotenv()

   # Acceder a la variable GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

¡Eso es todo! Has creado exitosamente un archivo `.env`, añadido tu token de GitHub y lo has cargado en tu aplicación Python.

## Cómo ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, necesitas tener alguna versión de [Python instalado](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Después, para usar el repositorio, necesitas clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

¡Una vez que tengas todo descargado, puedes comenzar!

## Pasos opcionales

### Instalando Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) es un instalador ligero para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, así como algunos paquetes.
Conda en sí es un gestor de paquetes que facilita configurar y alternar entre diferentes [**entornos virtuales**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) y paquetes Python. También es útil para instalar paquetes que no están disponibles vía `pip`.

Puedes seguir la [guía de instalación de Miniconda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurarlo.

Con Miniconda instalado, necesitas clonar el [repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (si aún no lo has hecho)

Luego necesitas crear un entorno virtual. Para hacer esto con Conda, crea un nuevo archivo de entorno (_environment.yml_). Si estás siguiendo el curso con Codespaces, créalo dentro del directorio `.devcontainer`, es decir, `.devcontainer/environment.yml`.

Llena tu archivo de entorno con el siguiente fragmento:

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

Si tienes problemas usando conda, puedes instalar manualmente las Bibliotecas de IA de Microsoft usando el siguiente comando en una terminal.

```
conda install -c microsoft azure-ai-ml
```

El archivo de entorno especifica las dependencias que necesitamos. `<environment-name>` se refiere al nombre que deseas usar para tu entorno Conda, y `<python-version>` es la versión de Python que quieres usar, por ejemplo, `3` es la última versión principal de Python.

Con eso listo, puedes crear tu entorno Conda ejecutando los siguientes comandos en tu línea de comandos/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # La subruta .devcontainer se aplica solo a configuraciones de Codespace
conda activate ai4beg
```

Consulta la [guía de entornos Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si tienes algún problema.

### Usando Visual Studio Code con la extensión de soporte para Python

Recomendamos usar el editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con la [extensión de soporte para Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Sin embargo, esto es solo una recomendación y no un requisito definitivo.

> **Nota**: Al abrir el repositorio del curso en VS Code, tienes la opción de configurar el proyecto dentro de un contenedor. Esto es gracias al [directorio especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) que se encuentra en el repositorio del curso. Más adelante hablaremos de esto.

> **Nota**: Una vez que clones y abras el directorio en VS Code, te sugerirá automáticamente instalar una extensión de soporte para Python.

> **Nota**: Si VS Code te sugiere volver a abrir el repositorio en un contenedor, rechaza esta petición para usar la versión instalada localmente de Python.

### Usando Jupyter en el navegador

También puedes trabajar en el proyecto usando el [entorno Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directamente en tu navegador. Tanto el Jupyter clásico como [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ofrecen un entorno de desarrollo muy agradable con características como autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, abre la terminal/línea de comandos, navega al directorio del curso y ejecuta:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Esto iniciará una instancia de Jupyter y la URL para acceder a ella se mostrará en la ventana de la terminal.

Una vez que accedas a la URL, deberías ver el esquema del curso y poder navegar a cualquier archivo `*.ipynb`. Por ejemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Ejecutando en un contenedor

Una alternativa a configurar todo en tu computadora o Codespace es usar un [contenedor](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). La carpeta especial `.devcontainer` dentro del repositorio del curso permite que VS Code configure el proyecto dentro de un contenedor. Fuera de Codespaces, esto requerirá la instalación de Docker, y francamente, implica algo de trabajo, por lo que recomendamos esta opción solo a quienes tienen experiencia trabajando con contenedores.

Una de las mejores maneras de mantener seguras tus claves API cuando usas GitHub Codespaces es usando los Secrets de Codespace. Por favor, sigue la guía [Gestión de secrets en Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para aprender más al respecto.


## Lecciones y requisitos técnicos

El curso tiene 6 lecciones conceptuales y 6 lecciones de codificación.

Para las lecciones de codificación usamos el Azure OpenAI Service. Necesitarás acceso al servicio Azure OpenAI y una clave API para ejecutar este código. Puedes solicitar acceso [completando esta solicitud](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mientras esperas que procesen tu solicitud, cada lección de codificación también incluye un archivo `README.md` donde puedes ver el código y los resultados.

## Usando el Azure OpenAI Service por primera vez

Si es la primera vez que trabajas con el servicio Azure OpenAI, por favor sigue esta guía sobre cómo [crear y desplegar un recurso de Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando la API de OpenAI por primera vez

Si es la primera vez que trabajas con la API de OpenAI, por favor sigue la guía sobre cómo [crear y usar la interfaz.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conoce a otros estudiantes

Hemos creado canales en nuestro servidor oficial de Discord de [la Comunidad de IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para que puedas conocer a otros estudiantes. Esta es una excelente manera de hacer networking con otros emprendedores, creadores, estudiantes, y cualquiera que quiera avanzar en IA Generativa.

[![Únete al canal de discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

El equipo del proyecto también estará en este servidor de Discord para ayudar a cualquier estudiante.

## Contribuye

Este curso es una iniciativa de código abierto. Si ves áreas de mejora o problemas, por favor crea un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o reporta un [issue en GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

El equipo del proyecto estará gestionando todas las contribuciones. Contribuir al código abierto es una manera increíble de construir tu carrera en IA Generativa.

La mayoría de contribuciones requieren que aceptes un Acuerdo de Licencia para Colaboradores (CLA) declarando que tienes el derecho y realmente otorgas los derechos de uso de tu contribución. Para más detalles, visita el [sitio web del CLA, Acuerdo de Licencia para Colaboradores](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: al traducir texto en este repositorio, por favor asegúrate de no usar traducción automática. Verificaremos las traducciones mediante la comunidad, así que por favor solo ofrece voluntariamente traducciones en idiomas que domines.

Cuando envíes un pull request, un robot CLA-bot determinará automáticamente si necesitas proveer un CLA y decorará el PR apropiadamente (por ejemplo, con una etiqueta o comentario). Simplemente sigue las instrucciones del bot. Solo necesitarás hacer esto una vez en todos los repositorios que usan nuestro CLA.

Este proyecto ha adoptado el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para más información lee las preguntas frecuentes del Código de Conducta o contacta a [Email opencode](opencode@microsoft.com) para cualquier pregunta o comentario adicional.

## ¡Comencemos!
Ahora que has completado los pasos necesarios para completar este curso, comencemos con una [introducción a la IA Generativa y los LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->