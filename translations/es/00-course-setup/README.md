<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T13:35:08+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "es"
}
-->
# Comenzando con este curso

¡Estamos muy emocionados de que empieces este curso y ver en qué te inspiras para crear con IA Generativa!

Para asegurar tu éxito, en esta página encontrarás los pasos de configuración, los requisitos técnicos y dónde pedir ayuda si la necesitas.

## Pasos de configuración

Para comenzar este curso, necesitas completar los siguientes pasos.

### 1. Haz un fork de este repositorio

[Haz un fork de todo este repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) a tu propia cuenta de GitHub para poder modificar el código y completar los desafíos. También puedes [darle una estrella (🌟) a este repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) para encontrarlo más fácilmente junto con otros repos relacionados.

### 2. Crea un codespace

Para evitar problemas de dependencias al ejecutar el código, te recomendamos realizar este curso en un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

En tu fork: **Code -> Codespaces -> New on main**

![Diálogo mostrando los botones para crear un codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Agrega un secreto

1. ⚙️ Icono de engranaje -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nombra OPENAI_API_KEY, pega tu clave, y guarda.

### 3. ¿Qué sigue?

| Quiero…              | Ir a…                                                                  |
|----------------------|------------------------------------------------------------------------|
| Empezar la Lección 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Trabajar sin conexión| [`setup-local.md`](02-setup-local.md)                                  |
| Configurar un proveedor LLM | [`providers.md`](providers.md)                                  |
| Conocer a otros estudiantes | [Únete a nuestro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Resolución de problemas

| Síntoma                                   | Solución                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| La construcción del contenedor se queda atascada > 10 min | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | El terminal no se adjuntó; haz clic en **+** ➜ *bash*           |
| `401 Unauthorized` de OpenAI              | `OPENAI_API_KEY` incorrecta o expirada                          |
| VS Code muestra “Dev container mounting…” | Refresca la pestaña del navegador—Codespaces a veces pierde la conexión |
| Falta el kernel del notebook              | Menú del notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   Sistemas basados en Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edita el archivo `.env`**: Abre el archivo `.env` en un editor de texto (por ejemplo, VS Code, Notepad++, o cualquier otro editor). Agrega la siguiente línea al archivo, reemplazando `your_github_token_here` con tu token real de GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Guarda el archivo**: Guarda los cambios y cierra el editor de texto.

5. **Instala `python-dotenv`**: Si aún no lo has hecho, necesitas instalar el paquete `python-dotenv` para cargar las variables de entorno desde el archivo `.env` en tu aplicación de Python. Puedes instalarlo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carga las variables de entorno en tu script de Python**: En tu script de Python, usa el paquete `python-dotenv` para cargar las variables de entorno desde el archivo `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

¡Eso es todo! Has creado correctamente un archivo `.env`, agregado tu token de GitHub y lo has cargado en tu aplicación de Python.

## Cómo ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, necesitas tener alguna versión de [Python instalada](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Luego, para usar el repositorio, necesitas clonarlo:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

¡Una vez que tengas todo listo, puedes comenzar!

## Pasos opcionales

### Instalando Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) es un instalador ligero para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python y algunos paquetes.
Conda es un gestor de paquetes que facilita la configuración y el cambio entre diferentes [**entornos virtuales**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) de Python y paquetes. También es útil para instalar paquetes que no están disponibles vía `pip`.

Puedes seguir la [guía de instalación de MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurarlo.

Con Miniconda instalado, necesitas clonar el [repositorio](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (si aún no lo has hecho).

Luego, necesitas crear un entorno virtual. Para hacerlo con Conda, crea un nuevo archivo de entorno (_environment.yml_). Si estás siguiendo los pasos usando Codespaces, crea esto dentro del directorio `.devcontainer`, es decir, `.devcontainer/environment.yml`.

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

Si encuentras errores usando conda, puedes instalar manualmente las librerías de Microsoft AI usando el siguiente comando en una terminal.

```
conda install -c microsoft azure-ai-ml
```

El archivo de entorno especifica las dependencias que necesitamos. `<environment-name>` se refiere al nombre que quieres usar para tu entorno de Conda, y `<python-version>` es la versión de Python que deseas usar, por ejemplo, `3` es la última versión principal de Python.

Con eso listo, puedes crear tu entorno de Conda ejecutando los siguientes comandos en tu línea de comandos/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulta la [guía de entornos de Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si tienes algún problema.

### Usando Visual Studio Code con la extensión de soporte para Python

Recomendamos usar el editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) con la [extensión de soporte para Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalada para este curso. Sin embargo, esto es solo una recomendación y no un requisito obligatorio.

> **Note**: Al abrir el repositorio del curso en VS Code, tienes la opción de configurar el proyecto dentro de un contenedor. Esto es posible gracias al [directorio especial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) que se encuentra dentro del repositorio del curso. Más sobre esto más adelante.

> **Note**: Una vez que clones y abras el directorio en VS Code, automáticamente te sugerirá instalar una extensión de soporte para Python.

> **Note**: Si VS Code te sugiere volver a abrir el repositorio en un contenedor, rechaza esta solicitud para usar la versión de Python instalada localmente.

### Usando Jupyter en el navegador

También puedes trabajar en el proyecto usando el [entorno Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directamente en tu navegador. Tanto el Jupyter clásico como [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ofrecen un entorno de desarrollo muy cómodo con funciones como autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, ve al terminal/línea de comandos, navega al directorio del curso y ejecuta:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Esto iniciará una instancia de Jupyter y la URL para acceder aparecerá en la ventana de la línea de comandos.

Una vez que accedas a la URL, deberías ver el índice del curso y poder navegar a cualquier archivo `*.ipynb`. Por ejemplo, `08-building-search-applications/python/oai-solution.ipynb`.

### Ejecutando en un contenedor

Una alternativa a configurar todo en tu computadora o Codespace es usar un [contenedor](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). La carpeta especial `.devcontainer` dentro del repositorio del curso permite que VS Code configure el proyecto dentro de un contenedor. Fuera de Codespaces, esto requerirá instalar Docker y, siendo sinceros, implica un poco de trabajo, así que solo lo recomendamos para quienes ya tienen experiencia trabajando con contenedores.

Una de las mejores formas de mantener seguras tus claves API al usar GitHub Codespaces es usando los Secrets de Codespace. Por favor, sigue la [guía de gestión de secrets en Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) para aprender más sobre esto.

## Lecciones y requisitos técnicos

El curso tiene 6 lecciones de conceptos y 6 lecciones de codificación.

Para las lecciones de codificación, usamos el servicio Azure OpenAI. Necesitarás acceso al servicio Azure OpenAI y una clave API para ejecutar este código. Puedes solicitar acceso [completando esta solicitud](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mientras esperas que tu solicitud sea procesada, cada lección de codificación también incluye un archivo `README.md` donde puedes ver el código y los resultados.

## Usando el servicio Azure OpenAI por primera vez

Si es tu primera vez trabajando con el servicio Azure OpenAI, por favor sigue esta guía sobre cómo [crear y desplegar un recurso de Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Usando la API de OpenAI por primera vez

Si es tu primera vez trabajando con la API de OpenAI, por favor sigue la guía sobre cómo [crear y usar la interfaz.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Conoce a otros estudiantes

Hemos creado canales en nuestro [servidor oficial de Discord de la Comunidad de IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) para que puedas conocer a otros estudiantes. Es una excelente manera de conectar con otros emprendedores, desarrolladores, estudiantes y cualquier persona interesada en mejorar sus habilidades en IA Generativa.

[![Únete al canal de discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

El equipo del proyecto también estará en este servidor de Discord para ayudar a los estudiantes.

## Contribuye

Este curso es una iniciativa de código abierto. Si ves áreas de mejora o encuentras problemas, por favor crea un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) o reporta un [issue en GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

El equipo del proyecto hará seguimiento de todas las contribuciones. Contribuir a proyectos de código abierto es una excelente manera de impulsar tu carrera en IA Generativa.

La mayoría de las contribuciones requieren que aceptes un Acuerdo de Licencia de Colaborador (CLA), declarando que tienes el derecho y realmente nos concedes los derechos para usar tu contribución. Para más detalles, visita el [sitio web del CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Importante: al traducir texto en este repositorio, por favor asegúrate de no usar traducción automática. Verificaremos las traducciones a través de la comunidad, así que solo ofrece tu ayuda para traducir a idiomas en los que seas competente.

Cuando envíes un pull request, un bot de CLA determinará automáticamente si necesitas aceptar un CLA y marcará el PR adecuadamente (por ejemplo, con una etiqueta o comentario). Simplemente sigue las instrucciones que te indique el bot. Solo tendrás que hacer esto una vez para todos los repositorios que usen nuestro CLA.

Este proyecto ha adoptado el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Para más información, lee las preguntas frecuentes del Código de Conducta o contacta a [Email opencode](opencode@microsoft.com) si tienes preguntas o comentarios adicionales.

## ¡Empecemos!
Ahora que has completado los pasos necesarios para terminar este curso, vamos a comenzar con una [introducción a la IA generativa y los LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.