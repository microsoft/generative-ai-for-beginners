# Comenzando con este curso

¡Estamos muy emocionados de que comiences este curso y veas lo que te inspira a construir con la IA Generativa!

Para que tu tiempo sea exitoso, hemos creado esta página que describe los pasos de configuración, los requisitos técnicos y cómo obtener ayuda cuando la necesites.

## Pasos de Configuración

Para comenzar a tomar este curso, necesitarás completar los siguientes pasos.

### 1. Haz un Fork de este Repositorio


[Haz un Fork de todo este repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) en tu propia cuenta de GitHub para poder cambiar cualquier código y completar los desafíos. También puedes [marcar este repositorio con una estrella (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrar este repositorio y otros relacionados más fácilmente.


### 2. Crea un codespace

Para evitar cualquier problema de dependencia al ejecutar el código, recomendamos ejecutar este curso en un codespace de GitHub.

Esto se puede crear seleccionando la opción `Code` en tu versión forked de este repositorio y seleccionando la opción **Codespaces**.


### 3. Almacenando tus claves de API

Mantener tus claves de API seguras es importante al construir cualquier tipo de aplicación. Te recomendamos no almacenar ninguna clave de API directamente en el código con el que estás trabajando, ya que comprometer esos detalles en un repositorio público podría resultar en costos y problemas no deseados.

![Diálogo mostrando botones para crear un codespace](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)


## Cómo Ejecutar Localmente en tu Computadora

Para ejecutar el código localmente en tu computadora, necesitarás tener alguna versión de [Python instalada](https://www.python.org/downloads?WT.mc_id=academic-105485-koreyst).

Para usar el repositorio, primero necesitarás clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ahora tienes todo configurado y puedes comenzar a aprender y trabajar con el código.

### Instalando miniconda (paso opcional)

Existen ventajas en instalar **[miniconda](https://conda.io/en/latest/miniconda.html)** - es una instalación bastante ligera que soporta el gestor de paquetes `conda` para diferentes **entornos virtuales** de Python. `conda` facilita la instalación y el cambio entre diferentes versiones y paquetes de Python, y también la instalación de paquetes que no están disponibles a través de `pip`.

Después de instalar miniconda, necesitarás clonar el repositorio (si aún no lo has hecho) y crear un entorno virtual para usarlo en este curso:

Antes de ejecutar el paso siguiente, asegúrate de que ya tienes un archivo *environment.yml*. El archivo *environment.yml* se usa para crear un entorno conda con las dependencias necesarias y que puede parecerse a esto:

```yml
name: <environment-name>
channels:  
 - defaults
dependencies:  
- python=<python-version>  
- openai  
- python-dotenv
```

Puedes sustituir `<environment-name>` por el nombre de tu entorno conda y `<python-version>` por la versión de Python que desees usar. Coloca el archivo *environment.yml* creado en la carpeta *.devcontainer* de tu repositorio.

Ahora que has creado un archivo *environment.yml*, puedes crear un entorno conda con el siguiente comando:


```bash
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

Si tienes problemas, consulta este enlace sobre la creación de [entornos conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).


### Usando Visual Studio Code con la Extensión de Python

Probablemente la mejor manera de usar el currículo es abriéndolo en [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con la [Extensión de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst).

> **Nota**: Una vez que clones y abras el directorio en VS Code, este automáticamente sugerirá que instales las extensiones de Python. También tendrías que instalar `miniconda` como se describió anteriormente.

> **Nota**: Si VS Code sugiere que reabras el repositorio en un contenedor, necesitarás rechazar esto para usar la instalación local de Python.


### Usando Jupyter en el Navegador

También puedes usar el entorno de Jupyter directamente desde el navegador en tu propia computadora. De hecho, tanto Jupyter clásico como Jupyter Hub proporcionan un entorno de desarrollo bastante conveniente con auto-completado, resaltado de código, etc.

Para iniciar Jupyter localmente, ve al directorio del curso y ejecuta:


```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Puedes navegar a cualquiera de los archivos `.ipynb`, abrir esos archivos y comenzar a trabajar.

### Ejecutando en un Contenedor

Una alternativa a la instalación de Python sería ejecutar el código en un contenedor. Como nuestro repositorio contiene una carpeta especial llamada `.devcontainer`, que instruye cómo crear un contenedor para este repositorio, VS Code ofrecerá la opción de reabrir el código en un contenedor. Esto requiere la instalación de Docker y es más complejo, por lo tanto, se recomienda para usuarios más experimentados.

Una de las mejores maneras de mantener tus claves de API seguras al usar GitHub Codespaces es utilizando `Codespace Secrets`. Sigue esta guía sobre cómo [gestionar secretos para tus Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).


## Lecciones y Requisitos Técnicos

El curso tiene 6 lecciones conceptuales y 6 lecciones incluyen codificación.

Para las lecciones de codificación, estamos utilizando el Servicio Azure OpenAI. Necesitarás acceso al servicio Azure OpenAI y una clave de API para ejecutar el código. Puedes solicitar acceso completando [esta solicitud](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOFA5Qk1UWDRBMjg0WFhPMkIzTzhKQ1dWNyQlQCN0PWcu&culture=en-us&country=us?WT.mc_id=academic-105485-koreyst).

Mientras esperas el procesamiento de tu solicitud, cada lección que tenga codificación también incluirá un archivo `README.md` donde podrás visualizar el código y sus respectivas salidas.

## Usando el Servicio Azure OpenAI por Primera Vez

Si esta es la primera vez que trabajas con el servicio Azure OpenAI, sigue esta guía sobre cómo [crear e implementar un recurso del Servicio Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## Conoce a Otros Estudiantes

Hemos creado canales en nuestro [servidor oficial AI Community en Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para que puedas conocer a otros estudiantes. Esta es una gran manera de conectar con otros emprendedores, desarrolladores, estudiantes y cualquier persona con ideas afines que quiera profundizar sobre la IA Generativa.

[![Únete al canal en Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

El equipo del proyecto también estará presente en este servidor de Discord para ayudar a cualquier estudiante.

## Contribuye

Este curso es una iniciativa de código abierto. Si identificas áreas de mejora o problemas, por favor crea un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o registra una [issue en Github](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

El equipo del proyecto dará seguimiento a todas las contribuciones. Además, contribuir al código abierto es una manera increíble de construir tu carrera en IA Generativa.

La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia de Colaborador (CLA) declarando que tienes el derecho a otorgarnos, y de hecho nos concedes, los derechos para usar tu contribución. Para más detalles, visita el [sitio web de CLA, Acuerdo de Licencia de Colaborador](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: al traducir texto en este repositorio, asegúrate de no utilizar traducción automática. Revisaremos las traducciones por medio de la comunidad, por lo tanto, ofrécete como voluntario para traducir solo en idiomas en los que seas competente.

Cuando envíes un Pull Request, un bot de CLA automáticamente determinará si necesitas proporcionar un CLA y decorar el PR adecuadamente (por ejemplo, con una etiqueta o comentario). Solo sigue las instrucciones proporcionadas por el bot. Solo necesitarás hacer esto una vez en todos los repositorios que usan nuestro CLA.

Este proyecto ha adoptado el Código de Conducta de Código Abierto de Microsoft. Para obtener más información, lee el FAQ del Código de Conducta o comunícate con [opencode](opencode@microsoft.com) por correo electrónico con cualquier pregunta o comentario adicional.

## Empecemos

Ahora que has completado las etapas necesarias para concluir este curso, comencemos con una [introducción a la IA Generativa y los LLMs](../../../01-introduction-to-genai/translations/es-mx/README.md?WT.mc_id=academic-105485-koreyst).
