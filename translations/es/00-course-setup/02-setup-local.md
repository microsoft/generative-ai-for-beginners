<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T13:34:32+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "es"
}
-->
# Configuración local 🖥️

**Usa esta guía si prefieres ejecutar todo en tu propio portátil.**  
Tienes dos opciones: **(A) Python nativo + virtual-env** o **(B) Dev Container de VS Code con Docker**.  
Elige la que te resulte más sencilla—ambas llevan a las mismas lecciones.

## 1.  Requisitos previos

| Herramienta         | Versión / Notas                                                                      |
|---------------------|--------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (descárgalo de <https://python.org>)                                          |
| **Git**             | Última versión (incluido en Xcode / Git para Windows / gestor de paquetes de Linux)  |
| **VS Code**         | Opcional pero recomendado <https://code.visualstudio.com>                            |
| **Docker Desktop**  | *Solo* para la Opción B. Instalación gratuita: <https://docs.docker.com/desktop/>    |

> 💡 **Tip** – Verifica las herramientas en una terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opción A – Python nativo (la más rápida)

### Paso 1  Clona este repositorio

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Paso 2 Crea y activa un entorno virtual

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ El prompt ahora debería comenzar con (.venv)—eso significa que estás dentro del entorno.

### Paso 3 Instala las dependencias

```bash
pip install -r requirements.txt
```

Salta a la Sección 3 sobre [claves de API](../../../00-course-setup)

## 2. Opción B – Dev Container de VS Code (Docker)

Preparamos este repositorio y curso con un [contenedor de desarrollo](https://containers.dev?WT.mc_id=academic-105485-koreyst) que tiene un entorno universal compatible con Python3, .NET, Node.js y Java. La configuración relacionada está definida en el archivo `devcontainer.json` ubicado en la carpeta `.devcontainer/` en la raíz de este repositorio.

>**¿Por qué elegir esto?**
>Entorno idéntico a Codespaces; sin diferencias de dependencias.

### Paso 0 Instala los extras

Docker Desktop – confirma que ```docker --version``` funciona.
Extensión VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Paso 1 Abre el repositorio en VS Code

Archivo ▸ Abrir carpeta…  → generative-ai-for-beginners

VS Code detecta .devcontainer/ y muestra un aviso.

### Paso 2 Reabrir en el contenedor

Haz clic en “Reopen in Container”. Docker construye la imagen (≈ 3 min la primera vez).
Cuando aparezca el prompt de la terminal, ya estás dentro del contenedor.

## 2.  Opción C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) es un instalador ligero para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python y algunos paquetes.
Conda es un gestor de paquetes que facilita la configuración y el cambio entre diferentes [**entornos virtuales**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) y paquetes de Python. También es útil para instalar paquetes que no están disponibles vía `pip`.

### Paso 0  Instala Miniconda

Sigue la [guía de instalación de MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurarlo.

```bash
conda --version
```

### Paso 1 Crea un entorno virtual

Crea un nuevo archivo de entorno (*environment.yml*). Si estás siguiendo el curso en Codespaces, créalo dentro del directorio `.devcontainer`, es decir, `.devcontainer/environment.yml`.

### Paso 2  Llena tu archivo de entorno

Agrega el siguiente fragmento a tu `environment.yml`

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

### Paso 3 Crea tu entorno Conda

Ejecuta los siguientes comandos en tu terminal o línea de comandos

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consulta la [guía de entornos Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si tienes algún problema.

## 2  Opción D – Jupyter clásico / Jupyter Lab (en tu navegador)

> **¿Para quién es esto?**  
> Para quienes prefieren la interfaz clásica de Jupyter o quieren ejecutar notebooks sin VS Code.  

### Paso 1  Asegúrate de que Jupyter esté instalado

Para iniciar Jupyter localmente, abre la terminal/línea de comandos, navega al directorio del curso y ejecuta:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Esto iniciará una instancia de Jupyter y la URL para acceder aparecerá en la ventana de la línea de comandos.

Una vez que accedas a la URL, deberías ver el índice del curso y poder navegar a cualquier archivo `*.ipynb`. Por ejemplo, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Agrega tus claves de API

Mantener tus claves de API seguras es fundamental al crear cualquier tipo de aplicación. Recomendamos no guardar ninguna clave de API directamente en tu código. Si subes esos datos a un repositorio público, podrías tener problemas de seguridad e incluso costos no deseados si alguien los usa indebidamente.
Aquí tienes una guía paso a paso para crear un archivo `.env` para Python y agregar el `GITHUB_TOKEN`:

1. **Navega a tu directorio de proyecto**: Abre tu terminal o línea de comandos y ve al directorio raíz de tu proyecto donde quieres crear el archivo `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crea el archivo `.env`**: Usa tu editor de texto favorito para crear un archivo nuevo llamado `.env`. Si usas la línea de comandos, puedes usar `touch` (en sistemas Unix) o `echo` (en Windows):

   Sistemas Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edita el archivo `.env`**: Abre el archivo `.env` en un editor de texto (por ejemplo, VS Code, Notepad++, o cualquier otro). Agrega la siguiente línea al archivo, reemplazando `your_github_token_here` por tu token real de GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Guarda el archivo**: Guarda los cambios y cierra el editor de texto.

5. **Instala `python-dotenv`**: Si aún no lo has hecho, necesitas instalar el paquete `python-dotenv` para cargar las variables de entorno desde el archivo `.env` en tu aplicación Python. Puedes instalarlo usando `pip`:

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

¡Listo! Has creado el archivo `.env`, agregado tu token de GitHub y lo has cargado en tu aplicación Python.

🔐 Nunca subas .env—ya está en .gitignore.
Las instrucciones completas de los proveedores están en [`providers.md`](03-providers.md).

## 4. ¿Qué sigue?

| Quiero…             | Ir a…                                                                   |
|---------------------|-------------------------------------------------------------------------|
| Comenzar la Lección 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Configurar un proveedor LLM | [`providers.md`](03-providers.md)                                       |
| Conocer a otros estudiantes | [Únete a nuestro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Resolución de problemas

| Síntoma                                   | Solución                                                         |
|-------------------------------------------|------------------------------------------------------------------|
| `python not found`                        | Agrega Python al PATH o reinicia la terminal después de instalar |
| `pip` no puede construir wheels (Windows) | `pip install --upgrade pip setuptools wheel` y vuelve a intentar |
| `ModuleNotFoundError: dotenv`             | Ejecuta `pip install -r requirements.txt` (el entorno no se instaló)|
| Falla la construcción de Docker *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → aumenta el tamaño de disco |
| VS Code sigue pidiendo reabrir            | Puede que tengas ambas opciones activas; elige una (venv **o** contenedor)|
| Errores 401 / 429 de OpenAI               | Revisa el valor de `OPENAI_API_KEY` / límites de solicitudes     |
| Errores usando Conda                      | Instala las librerías de IA de Microsoft con `conda install -c microsoft azure-ai-ml`|

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de cualquier malentendido o interpretación incorrecta que surja del uso de esta traducción.