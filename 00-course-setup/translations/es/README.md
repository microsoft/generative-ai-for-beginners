# -- Traducción en Progreso 😀 --

# Comenzando con este curso

¡Estamos muy emocionados de que comiences este curso y ver lo que te inspiras a construir con la IA Generativa!

Para que tu tiempo sea exitoso, hemos creado esta página que describe los pasos de configuración, los requisitos técnicos y cómo obtener ayuda cuando la necesites.

## Pasos de Configuración

Para comenzar con este curso, deberás completar los siguientes pasos.

### 1. Realizar un Fork de este Repositorio

[Haz un fork de todo este repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) en tu propia cuenta de GitHub para poder cambiar cualquier código y completar los desafíos. También puedes [marcar (🌟) este repositorio](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrarlo y acceder a repositorios relacionados más fácilmente.

### 2. Crea un Codespace

Para evitar problemas de dependencias al ejecutar el código, recomendamos ejecutar este curso en un Codespace de GitHub.

Puedes crearlo seleccionando la opción `Code` en tu versión con fork de este repositorio y eligiendo la opción **Codespaces**.

![Diálogo que muestra botones para crear un Codespace](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

### 3. Almacenar tus Claves de API

Mantener seguras y protegidas tus claves de API es importante al construir cualquier tipo de aplicación. Te recomendamos que no almacenes las claves de API directamente en el código con el que estás trabajando, ya que comprometer esos detalles en un repositorio público podría resultar en costos no deseados y problemas.

## Cómo Ejecutar Localmente en tu Computadora

Para ejecutar el código localmente en tu computadora, necesitarás tener alguna versión de [Python instalada](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Luego, para usar el repositorio, deberás clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ahora tienes todo descargado y puedes comenzar a aprender y trabajar con el código.

### Instalación de miniconda (paso opcional)

Existen ventajas al instalar **[miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)**; es una instalación bastante ligera que admite el administrador de paquetes `conda` para diferentes entornos virtuales de Python. `conda` facilita la instalación y el cambio entre diferentes versiones de Python y paquetes, y también la instalación de paquetes que no están disponibles a través de `pip`.

Después de instalar miniconda, debes clonar el repositorio (si aún no lo has hecho) y crear un entorno virtual que se utilizará para este curso:

Antes de ejecutar el siguiente paso, asegúrate de tener un archivo *environment.yml*. El archivo *environment.yml* se utiliza para crear un entorno conda con las dependencias necesarias y puede tener esta apariencia:

```yml
name: <nombre-del-entorno>
channels:  
 - defaults
dependencies:  
- python=<versión-de-python>  
- openai  
- python-dotenv
```

Puedes reemplazar `<nombre-del-entorno>` con el nombre de tu entorno conda y `<versión-de-python>` con la versión de Python que deseas utilizar. Coloca tu archivo *environment.yml* creado en la carpeta *.devcontainer* de tu repositorio.

Ahora que has creado (o esperamos que hayas creado) un archivo *environment.yml*, puedes crear un entorno conda con el siguiente comando:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

Si tienes problemas, consulta este enlace sobre la [creación de entornos conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Uso de Visual Studio Code con la Extensión de Python

Probablemente, la mejor forma de utilizar el plan de estudios es abrirlo en [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con la [Extensión de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst).

> **Nota**: Una vez que clones y abras el directorio en VS Code, te sugerirá automáticamente instalar las extensiones de Python. También deberás instalar miniconda como se describe anteriormente.

> **Nota**: Si VS Code te sugiere reabrir el repositorio en un contenedor, debes rechazar esta sugerencia para usar la instalación local de Python.

### Uso de Jupyter en el Navegador

También puedes utilizar el entorno de Jupyter directamente desde el navegador en tu propia computadora. De hecho, tanto Jupyter clásico como Jupyter Hub proporcionan un entorno de desarrollo bastante conveniente con autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, ve al directorio del curso y ejecuta:

```bash
jupyter notebook
```
o

```bash
jupyterhub
```

Luego puedes navegar hasta cualquiera de los archivos `.ipynb`, abrirlos y empezar a trabajar.

### Ejecución en un Contenedor

Una alternativa a la instalación de Python sería ejecutar el código en un contenedor. Dado que nuestro repositorio contiene una carpeta `.devcontainer` especial que indica cómo construir un contenedor para este repositorio, VS Code te ofrecerá volver a abrir el código en un contenedor. Esto requerirá la instalación de Docker y será más complejo, por lo que lo recomendamos para usuarios más experimentados.

Una de las mejores formas de mantener seguras tus claves de API al usar GitHub Codespaces es mediante el uso de Secrets de Codespace. Sigue esta guía sobre cómo [gestionar secrets para tus codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Lecciones y Requisitos Técnicos

El curso consta de 6 lecciones de concepto y 6 lecciones de programación.

Para las lecciones de programación, estamos utilizando el Servicio Azure OpenAI. Necesitarás acceso al servicio Azure OpenAI y una clave de API para ejecutar este código. Puedes solicitar acceso completando [esta solicitud](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOFA5Qk1UWDRBMjg0WFhPMkIzTzhKQ1dWNyQlQCN0PWcu&culture=en-us&country=us&WT.mc_id=academic-105485-koreyst).

Mientras esperas que se procese tu solicitud, cada lección de programación también incluye un archivo `README.md` donde puedes ver el código y los resultados.

## Uso del Servicio Azure OpenAI por Primera Vez

Si es la primera vez que trabajas con el servicio Azure OpenAI, sigue esta guía sobre cómo [crear y implementar un recurso de Servicio Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## Conoce a Otros Estudiantes

Hemos creado canales en nuestro [servidor oficial de Discord de la Comunidad de IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para conocer a otros estudiantes. Esta es una excelente manera de establecer contactos con otros emprendedores, desarrolladores, estudiantes y cualquier persona interesada en mejorar en IA Generativa.

[![Únete al canal de Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

El equipo del proyecto también estará en este servidor de Discord para ayudar a los estudiantes.

## Contribuye

Este curso es una iniciativa de código abierto. Si ves áreas de mejora o problemas, crea una [solicitud de extracción (Pull Request)](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o registra un [problema en Github](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

El equipo del proyecto seguirá todas las contribuciones y contribuir a proyectos de código abierto es una excelente manera de construir tu carrera en IA Generativa.

La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia del Colaborador (CLA) que declare que tienes el derecho y realmente otorgas los derechos para que utilicemos tu contribución. Para obtener detalles, visita el sitio web [CLA, Acuerdo de Licencia del Colaborador](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: al traducir texto en este repositorio, asegúrate de no utilizar traducción automática. Verificaremos las traducciones a través de la comunidad, así que, por favor, ofrécete como voluntario solo para traducciones en idiomas en los que seas competente.

Cuando envíes una solicitud de extracción, un bot de CLA determinará automáticamente si debes proporcionar un CLA y decorará la solicitud de extracción de manera apropiada (por ejemplo, etiquetas, comentarios). Simplemente sigue las instrucciones proporcionadas por el bot. Solo tendrás que hacer esto una vez en todos los repositorios que utilicen nuestro CLA.

Este proyecto ha adoptado el Código de Conducta de Código Abierto de Microsoft. Para obtener más información, lee el FAQ del Código de Conducta o contacta con [Email opencode](opencode@microsoft.com) para cualquier pregunta o comentario adicional.

## ¡Empecemos!

Ahora que has completado los pasos necesarios para realizar este curso, comencemos con una [introducción a la IA Generativa y a los Modelos de Lenguaje Gigantes (LLMs)](../../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).