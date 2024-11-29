# Comenzando con este curso

¡Estamos muy emocionados de que empieces este curso y ver qué te inspira a construir con IA Generativa!

Para asegurar tu éxito, esta página detalla los pasos de configuración, los requisitos técnicos y dónde obtener ayuda si es necesario.

## Pasos de Configuración

Para comenzar este curso, necesitarás completar los siguientes pasos.

### 1. Haz un fork de este repositorio

[Haz un fork de todo este repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a tu propia cuenta de GitHub para poder cambiar cualquier código y completar los desafíos. También puedes [darle una estrella (🌟) a este repositorio](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrarlo y los repositorios relacionados más fácilmente.

### 2. Crea un codespace

Para evitar problemas de dependencias al ejecutar el código, recomendamos ejecutar este curso en un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Esto se puede crear seleccionando la opción `Code` en tu versión bifurcada de este repositorio y seleccionando la opción **Codespaces**.

![Diálogo mostrando botones para crear un codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Almacenamiento de tus claves API

Mantener tus claves API seguras es importante al construir cualquier tipo de aplicación. Recomendamos no almacenar claves API directamente en tu código. Hacer commit de esos detalles en un repositorio público podría resultar en problemas de seguridad e incluso costos no deseados si son utilizadas por alguien malintencionado.

## Cómo ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, necesitarás tener alguna versión de [Python instalada](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Luego, para usar el repositorio, necesitas clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

¡Una vez que tengas todo revisado, puedes comenzar!

### Instalando Miniconda (paso opcional)

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) es un instalador ligero para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, así como algunos paquetes.
Conda en sí es un gestor de paquetes que facilita la configuración y el cambio entre diferentes [**entornos virtuales**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) de Python y paquetes. También es útil para instalar paquetes que no están disponibles a través de `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Adelante, completa tu archivo de entorno con el fragmento a continuación:

```yml
name: <environment-name>
channels:
 - defaults
dependencies:
- python=<python-version>
- openai
- python-dotenv
- azure-ai-inference

```

El archivo de entorno especifica las dependencias que necesitamos. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` es la última versión principal de Python.

Con eso hecho, puedes crear tu entorno Conda ejecutando los comandos a continuación en tu línea de comandos/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulta la [guía de entornos Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si tienes algún problema.

### Usando Visual Studio Code con la extensión de soporte para Python

Recomendamos usar el editor [Visual Studio Code (VS Code)](http://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con la [extensión de soporte para Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Sin embargo, esto es más una recomendación y no un requisito definitivo.

> **Nota**: Al abrir el repositorio del curso en VS Code, tienes la opción de configurar el proyecto dentro de un contenedor. Esto se debe al [directorio especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) que se encuentra dentro del repositorio del curso. Más sobre esto más adelante.

> **Nota**: Una vez que clonas y abres el directorio en VS Code, automáticamente te sugerirá instalar una extensión de soporte para Python.

> **Nota**: Si VS Code sugiere reabrir el repositorio en un contenedor, rechaza esta solicitud para usar la versión de Python instalada localmente.

### Usando Jupyter en el navegador

También puedes trabajar en el proyecto usando el [entorno Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directamente en tu navegador. Tanto Jupyter clásico como [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) proporcionan un entorno de desarrollo bastante agradable con características como autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, dirígete al terminal/línea de comandos, navega al directorio del curso y ejecuta:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Esto iniciará una instancia de Jupyter y la URL para acceder a ella se mostrará en la ventana de la línea de comandos.

Una vez que accedas a la URL, deberías ver el esquema del curso y poder navegar a cualquier archivo `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` donde puedes ver el código y los resultados.

## Usando el servicio Azure OpenAI por primera vez

Si es tu primera vez trabajando con el servicio Azure OpenAI, por favor sigue esta guía sobre cómo [crear e implementar un recurso de Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando la API de OpenAI por primera vez

Si es tu primera vez trabajando con la API de OpenAI, por favor sigue la guía sobre cómo [crear y usar la interfaz.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conoce a otros estudiantes

Hemos creado canales en nuestro servidor oficial de [Discord de la Comunidad de IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para conocer a otros estudiantes. Esta es una gran manera de hacer networking con otros emprendedores, constructores, estudiantes y cualquier persona que busque mejorar en IA Generativa.

[![Únete al canal de discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

El equipo del proyecto también estará en este servidor de Discord para ayudar a cualquier estudiante.

## Contribuir

Este curso es una iniciativa de código abierto. Si ves áreas de mejora o problemas, por favor crea un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o registra un [problema en GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

El equipo del proyecto estará siguiendo todas las contribuciones. Contribuir al código abierto es una manera increíble de construir tu carrera en IA Generativa.

La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia de Contribuidor (CLA) declarando que tienes el derecho y, de hecho, nos otorgas los derechos para usar tu contribución. Para más detalles, visita el [sitio web de CLA, Acuerdo de Licencia de Contribuidor](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: al traducir texto en este repositorio, por favor asegúrate de no usar traducción automática. Verificaremos las traducciones a través de la comunidad, así que por favor solo ofrece traducciones en idiomas en los que seas competente.

Cuando envíes un pull request, un bot de CLA determinará automáticamente si necesitas proporcionar un CLA y decorará el PR adecuadamente (por ejemplo, etiqueta, comentario). Simplemente sigue las instrucciones proporcionadas por el bot. Solo necesitarás hacer esto una vez en todos los repositorios que usen nuestro CLA.

Este proyecto ha adoptado el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para más información, lee las Preguntas Frecuentes del Código de Conducta o contacta a [Email opencode](opencode@microsoft.com) con cualquier pregunta o comentario adicional.

## Empecemos

Ahora que has completado los pasos necesarios para completar este curso, comencemos obteniendo una [introducción a la IA Generativa y los LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.