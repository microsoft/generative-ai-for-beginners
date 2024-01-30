# Comenzando con este curso

¡Estamos muy emocionados de que comiences este curso y ver con qué te inspiras para crear con la ayuda de la Inteligencia Artificial Generativa!

Para apoyarte, hemos creado esta página que describe los pasos de configuración, los requisitos técnicos y cómo obtener ayuda cuando la necesites.

## Pasos de configuración

Para comenzar este curso, deberás completar los siguientes pasos.

### 1. Fork (Bifurca) este repo

[Fork (Bifurca) todo el repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) A tu propia cuenta de GitHub para poder modificar cualquier código y completar los desafíos. También puedes [marcar con una estrella (🌟) este repositorio](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrarlo más fácilmente.

### 2. Crea un espacio en codespace

Para evitar problemas de dependencias al ejecutar el código, recomendamos realizar este curso en un codespace de GitHub.

Esto se puede hacer seleccionando la opción `Code` en tu propia versión bifurcada (forked) de este repositorio y luego seleccionando la opción **Codespaces** .

### 3. Almacena tus claves de API

Mantenen seguras y protegidas tus claves de API es importante al desarrollar cualquier tipo de aplicación. Te recomendamos no almacenar las claves de API directamente en el código con el que estás trabajando, ya que comprometer esos detalles en un repositorio público podría ocasionar costos no deseados e issues.

![Diálogo mostrando botones para crear un espacio de código](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

## Cómo ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, necesitarás tener alguna versión de [Python instalada](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Para utilizar el repositorio, necesitas clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ahora tienes todo listo y puedes comenzar a aprender y trabajar con el código.

### Instalación de Miniconda (paso opcional)

Hay ventajas en instalar **[miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)** - es una instalación bastante ligera que admite `conda` administrador de paquetes para diferentes versiones de Python **virtual environments**. `conda` facilita la instalación y el cambio entre diferentes versiones de Python y paquetes, además de permitir la instalación de paquetes que no están disponibles a través de `pip`.

Después de instalar Miniconda, necesitas clonar el repositorio (si aún no lo has hecho) y crear un entorno virtual para utilizar en este curso:

Antes de ejecutar el siguiente paso, asegúrate primero de tener un *environment.yml* file. El *environment.yml* archivo se utiliza para crear un entorno conda con las dependencias necesarias y puede lucir así:

```yml
name: <environment-name>
channels:  
 - defaults
dependencies:  
- python=<python-version>  
- openai  
- python-dotenv
```

Puedes reemplazar `<environment-name>` con el nombre de tu entorno conda, y `<python-version>` con la versión de Python que desees usar. Coloca tu archivo *environment.yml*  creado
en la capeta *.devcontainer* de tu repo.

Ahora que idealmente has creado un archivo *environment.yml* , puedes crear un entorno conda con el siguiente comando:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

Consulta este enlace sobre cómo crear un [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) 
si encuentras algún problema.


### Usando Visual Studio Code con la Extensión de Python


Probablemente la mejor manera de usar el plan de estudios sea abrirlo en [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst).

> **Nota**: Una vez que clones y abras el directorio en VS Code, automáticamente te sugerirá instalar las extensiones de Python. También tendrás que instalar Miniconda como se describe arriba.

> **Nota**: Si VS Code te sugiere volver a abrir el repositorio en un contenedor, debes rechazarlo para utilizar la instalación local de Python.

### Usando Jupyter en el navegador

También puedes utilizar el entorno Jupyter directamente desde el navegador en tu propia computadora. De hecho, tanto Jupyter clásico como Jupyter Hub ofrecen un entorno de desarrollo bastante conveniente con autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, ve al directorio del curso y ejecuta:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

Luego puedes navegar a cualquiera de los `.ipynb` archivos, abrirlos y empezar a trabajar.

### Ejecutando en un contenedor

Una alternativa a la instalación de Python sería ejecutar el código en un contenedor. Dado que nuestro repositorio contiene una carpeta especial `.devcontainer` que indica cómo construir un contenedor para este repositorio, VS Code te ofrecería volver a abrir el código en un contenedor. Esto requerirá la instalación de Docker y será más complejo, así que lo recomendamos para usuarios más experimentados.

Una de las mejores formas de mantener seguras tus claves de API al usar GitHub Codespaces es mediante el uso de Secrets (Secretos) de Codespace. Sigue esta guía sobre cómo [Administrar secrets para tus codespaces.](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Lecciones y Requisitos Técnicos

El curso consta de 6 lecciones conceptuales y 6 lecciones de codificación.

Para las lecciones de codificación, estamos utilizando el servicio Azure OpenAI. Necesitarás acceso al servicio Azure OpenAI y una clave de API para ejecutar este código. Puedes solicitar acceso [completando esta solicitud](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mientras esperas que procesen tu solicitud, cada lección de codificación también incluye un archivo `README.md` donde puedes ver el código y los resultados.

## Usando el Servicio Azure OpenAI por Primera Vez

Si es la primera vez que trabajas con el servicio Azure OpenAI, por favor sigue esta guía sobre cómo [crear y desplegar un recurso de Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Conocer a Otros Aprendices

Hemos creado canales en nuestro oficial [Servidor de Discord de la Comunidad de IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para conocer a otros estudiantes. Esta es una excelente manera de conectarte con otros emprendedores, creadores, estudiantes y cualquier persona interesada en avanzar en el campo de la Inteligencia Artificial Generativa.

[![Unete al canal de Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

El equipo del proyecto también estará en este servidor de Discord para ayudar a cualquier estudiante.

## Contribuye

Este curso es una iniciativa de código abierto. Si encuentras áreas de mejora o problemas, por favor crea un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o registrar un [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

El equipo del proyecto estará siguiendo todas las contribuciones y contribuir al código abierto es una manera increíble de construir tu carrera en la Inteligencia Artificial Generativa.

La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia para Colaboradores (CLA) en el que declaras que tienes derecho, y de hecho lo haces, a otorgarnos los derechos para usar tu contribución. Para más detalles, visita [CLA, sitio web del Acuerdo de Licencia para Colaboradores](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: al traducir texto en este repositorio, asegúrate de no utilizar traducción automática. Verificaremos las traducciones a través de la comunidad, así que por favor ofrécete como voluntario solo para traducir a idiomas en los que seas competente.

Cuando envíes un pull request, un bot del Acuerdo de Licencia para Colaboradores (CLA-bot) determinará automáticamente si necesitas proporcionar un CLA y decorará la PR apropiadamente (por ejemplo, etiqueta, comentario). Simplemente sigue las instrucciones proporcionadas por el bot. Solo necesitarás hacer esto una vez en todos los repositorios que utilicen nuestro CLA.

Este proyecto ha adoptado el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para más información, lee las Preguntas Frecuentes del Código de Conducta o contacta al [opencode Email](opencode@microsoft.com) con cualquier pregunta o comentario adicional.

## Empecemos 😄

Ahora que has completado los pasos necesarios para terminar este curso, comencemos obteniendo una [Introducción a la Inteligencia Artificial Generativa y Modelos de Lenguaje de Aprendizaje Profundo (LLMs, por sus siglas en inglés).](../../../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).
