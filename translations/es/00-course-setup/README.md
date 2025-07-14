<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T06:58:22+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "es"
}
-->
# Comenzando con este curso

¡Estamos muy emocionados de que comiences este curso y veas en qué te inspiras para crear con IA Generativa!

Para asegurar tu éxito, esta página describe los pasos de configuración, los requisitos técnicos y dónde obtener ayuda si la necesitas.

## Pasos de configuración

Para comenzar a tomar este curso, deberás completar los siguientes pasos.

### 1. Haz un fork de este repositorio

[Haz un fork de todo este repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a tu propia cuenta de GitHub para poder modificar cualquier código y completar los desafíos. También puedes [marcar con una estrella (🌟) este repositorio](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrarlo y localizar repos relacionados más fácilmente.

### 2. Crea un codespace

Para evitar problemas con dependencias al ejecutar el código, recomendamos usar este curso en un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Puedes crearlo seleccionando la opción `Code` en tu versión forked de este repositorio y luego eligiendo la opción **Codespaces**.

![Diálogo mostrando botones para crear un codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Almacenamiento de tus claves API

Mantener tus claves API seguras es importante al construir cualquier tipo de aplicación. Recomendamos no almacenar claves API directamente en tu código. Subir esos datos a un repositorio público podría causar problemas de seguridad e incluso costos no deseados si alguien malintencionado las usa.  
Aquí tienes una guía paso a paso para crear un archivo `.env` para Python y agregar el `GITHUB_TOKEN`:

1. **Navega a tu directorio de proyecto**: Abre tu terminal o consola y ve al directorio raíz de tu proyecto donde quieres crear el archivo `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crea el archivo `.env`**: Usa tu editor de texto preferido para crear un nuevo archivo llamado `.env`. Si usas la línea de comandos, puedes usar `touch` (en sistemas Unix) o `echo` (en Windows):

   Sistemas Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edita el archivo `.env`**: Abre el archivo `.env` en un editor de texto (por ejemplo, VS Code, Notepad++ u otro). Añade la siguiente línea, reemplazando `your_github_token_here` con tu token real de GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Guarda el archivo**: Guarda los cambios y cierra el editor.

5. **Instala `python-dotenv`**: Si aún no lo tienes, instala el paquete `python-dotenv` para cargar variables de entorno desde el archivo `.env` en tu aplicación Python. Puedes instalarlo con `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carga las variables de entorno en tu script Python**: En tu script Python, usa el paquete `python-dotenv` para cargar las variables de entorno desde el archivo `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

¡Eso es todo! Has creado correctamente un archivo `.env`, agregado tu token de GitHub y cargado las variables en tu aplicación Python.

## Cómo ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, necesitas tener alguna versión de [Python instalado](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Luego, para usar el repositorio, debes clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

¡Una vez que tengas todo listo, puedes comenzar!

## Pasos opcionales

### Instalando Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) es un instalador ligero para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python y algunos paquetes.  
Conda es un gestor de paquetes que facilita configurar y cambiar entre diferentes [**entornos virtuales**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) y paquetes de Python. También es útil para instalar paquetes que no están disponibles vía `pip`.

Puedes seguir la [guía de instalación de MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurarlo.

Con Miniconda instalado, necesitas clonar el [repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (si no lo has hecho ya).

Luego, crea un entorno virtual. Para hacerlo con Conda, crea un nuevo archivo de entorno (_environment.yml_). Si usas Codespaces, créalo dentro del directorio `.devcontainer`, es decir, `.devcontainer/environment.yml`.

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

Si tienes errores usando conda, puedes instalar manualmente las Microsoft AI Libraries con el siguiente comando en la terminal.

```
conda install -c microsoft azure-ai-ml
```

El archivo de entorno especifica las dependencias que necesitamos. `<environment-name>` es el nombre que quieres darle a tu entorno Conda, y `<python-version>` es la versión de Python que deseas usar, por ejemplo, `3` es la última versión mayor de Python.

Con eso listo, crea tu entorno Conda ejecutando los siguientes comandos en la línea de comandos o terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulta la [guía de entornos Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si tienes problemas.

### Usando Visual Studio Code con la extensión de soporte para Python

Recomendamos usar el editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con la [extensión de soporte para Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Sin embargo, esto es solo una recomendación, no un requisito obligatorio.

> **Nota**: Al abrir el repositorio del curso en VS Code, tienes la opción de configurar el proyecto dentro de un contenedor. Esto es posible gracias al [directorio especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) que se encuentra en el repositorio del curso. Más adelante hablaremos de esto.

> **Nota**: Una vez que clones y abras el directorio en VS Code, te sugerirá automáticamente instalar la extensión de soporte para Python.

> **Nota**: Si VS Code te sugiere reabrir el repositorio en un contenedor, rechaza esta solicitud para usar la versión de Python instalada localmente.

### Usando Jupyter en el navegador

También puedes trabajar en el proyecto usando el entorno [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directamente en tu navegador. Tanto Jupyter clásico como [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ofrecen un entorno de desarrollo agradable con funciones como autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, abre la terminal o línea de comandos, navega al directorio del curso y ejecuta:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Esto iniciará una instancia de Jupyter y la URL para acceder se mostrará en la ventana de la línea de comandos.

Al acceder a la URL, deberías ver el índice del curso y poder navegar a cualquier archivo `*.ipynb`. Por ejemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Ejecutando en un contenedor

Una alternativa a configurar todo en tu computadora o Codespace es usar un [contenedor](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). La carpeta especial `.devcontainer` dentro del repositorio del curso permite que VS Code configure el proyecto dentro de un contenedor. Fuera de Codespaces, esto requiere instalar Docker y, sinceramente, implica algo de trabajo, por lo que recomendamos esta opción solo a quienes tengan experiencia con contenedores.

Una de las mejores formas de mantener tus claves API seguras al usar GitHub Codespaces es mediante Codespace Secrets. Por favor, sigue la guía de [gestión de secretos en Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para aprender más.

## Lecciones y requisitos técnicos

El curso tiene 6 lecciones conceptuales y 6 lecciones de programación.

Para las lecciones de programación, usamos el Azure OpenAI Service. Necesitarás acceso a este servicio y una clave API para ejecutar el código. Puedes solicitar acceso [completando esta aplicación](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mientras esperas que procesen tu solicitud, cada lección de programación incluye un archivo `README.md` donde puedes ver el código y los resultados.

## Usando el Azure OpenAI Service por primera vez

Si es la primera vez que trabajas con el Azure OpenAI Service, sigue esta guía para [crear y desplegar un recurso de Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando la API de OpenAI por primera vez

Si es la primera vez que trabajas con la API de OpenAI, sigue la guía para [crear y usar la interfaz.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conoce a otros estudiantes

Hemos creado canales en nuestro servidor oficial de [Discord de la comunidad de IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para que puedas conocer a otros estudiantes. Es una excelente forma de conectar con otros emprendedores, creadores, estudiantes y cualquier persona que quiera avanzar en IA Generativa.

[![Únete al canal de discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

El equipo del proyecto también estará en este servidor de Discord para ayudar a los estudiantes.

## Contribuir

Este curso es una iniciativa de código abierto. Si ves áreas de mejora o problemas, por favor crea un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o reporta un [issue en GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

El equipo del proyecto hará seguimiento a todas las contribuciones. Contribuir a código abierto es una forma increíble de impulsar tu carrera en IA Generativa.

La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia de Contribuidor (CLA) declarando que tienes el derecho y realmente otorgas los derechos para usar tu contribución. Para más detalles, visita el [sitio web del CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: al traducir texto en este repositorio, asegúrate de no usar traducción automática. Verificaremos las traducciones con la comunidad, así que solo ofrece traducciones en idiomas que domines.

Cuando envíes un pull request, un bot CLA determinará automáticamente si necesitas proporcionar un CLA y etiquetará el PR apropiadamente (por ejemplo, con una etiqueta o comentario). Solo sigue las instrucciones del bot. Solo tendrás que hacerlo una vez para todos los repositorios que usen nuestro CLA.

Este proyecto ha adoptado el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para más información, lee las preguntas frecuentes del Código de Conducta o contacta a [Email opencode](opencode@microsoft.com) con cualquier duda o comentario adicional.

## ¡Comencemos!

Ahora que has completado los pasos necesarios para este curso, comencemos con una [introducción a la IA Generativa y los LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.