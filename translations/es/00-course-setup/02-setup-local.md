# Configuración Local 🖥️

**Usa esta guía si prefieres ejecutar todo en tu propia portátil.**   
Tienes dos caminos: **(A) Python nativo + virtual-env** o **(B) Contenedor Dev de VS Code con Docker**.  
Escoge el que te resulte más fácil; ambos llevan a las mismas lecciones.

## 1.  Requisitos previos

| Herramienta        | Versión / Notas                                                                    |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (descárgalo de <https://python.org>)                                       |
| **Git**            | Última versión (viene con Xcode / Git para Windows / gestor de paquetes en Linux) |
| **VS Code**        | Opcional pero recomendado <https://code.visualstudio.com>                         |
| **Docker Desktop** | *Solo* para la Opción B. Instalación gratuita: <https://docs.docker.com/desktop/> |

> 💡 **Consejo** – Verifica las herramientas en una terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opción A – Python nativo (la más rápida)

### Paso 1  Clona este repositorio

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Paso 2 Crea y activa un entorno virtual

```bash
python -m venv .venv          # hacer uno
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ El prompt debería iniciar ahora con (.venv)—eso significa que estás dentro del entorno.

### Paso 3 Instala dependencias

```bash
pip install -r requirements.txt
```

Salta a la Sección 3 sobre [Llaves API](#3-añade-tus-llaves-api)

## 2. Opción B – Contenedor Dev de VS Code (Docker)

Configuramos este repositorio y curso con un [contenedor de desarrollo](https://containers.dev?WT.mc_id=academic-105485-koreyst) que tiene un runtime universal que puede soportar desarrollo en Python3, .NET, Node.js y Java. La configuración relacionada está definida en el archivo `devcontainer.json` ubicado en la carpeta `.devcontainer/` en la raíz de este repositorio.

>**¿Por qué elegir esto?**
>Ambiente idéntico a Codespaces; sin desviación en dependencias.

### Paso 0 Instala los extras

Docker Desktop – confirma que ```docker --version``` funcione.
Extensión Remote – Containers de VS Code (ID: ms-vscode-remote.remote-containers).

### Paso 1 Abre el repositorio en VS Code

Archivo ▸ Abrir carpeta…  → generative-ai-for-beginners

VS Code detecta .devcontainer/ y muestra un aviso.

### Paso 2 Reabrir en el contenedor

Haz clic en “Reopen in Container”. Docker construye la imagen (≈ 3 min la primera vez).
Cuando aparezca el prompt en la terminal, estarás dentro del contenedor.

## 2.  Opción C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) es un instalador ligero para instalar [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, así como algunos paquetes.
Conda es un gestor de paquetes que facilita configurar y alternar entre diferentes [**entornos virtuales**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) y paquetes en Python. También es útil para instalar paquetes que no están disponibles vía `pip`.

### Paso 0  Instala Miniconda

Sigue la [guía de instalación de Miniconda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) para configurarlo.

```bash
conda --version
```

### Paso 1 Crea un entorno virtual

Crea un nuevo archivo de entorno (*environment.yml*). Si sigues usando Codespaces, colócalo dentro del directorio `.devcontainer`, es decir `.devcontainer/environment.yml`.

### Paso 2  Llena tu archivo de entorno

Añade el siguiente fragmento a tu `environment.yml`

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

Ejecuta los comandos abajo en tu línea de comandos/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # La subruta .devcontainer se aplica solo a configuraciones de Codespace
conda activate ai4beg
```

Consulta la [guía de entornos Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si tienes algún problema.

## 2  Opción D – Jupyter clásico / Jupyter Lab (en tu navegador)

> **¿Para quién es esto?**  
> Para quienes aman la interfaz clásica de Jupyter o quieren ejecutar notebooks sin VS Code.  

### Paso 1  Asegúrate de que Jupyter esté instalado

Para iniciar Jupyter localmente, abre una terminal/línea de comandos, navega al directorio del curso y ejecuta:

```bash
jupyter notebook
```

o

```bash
jupyterhub
```

Esto iniciará una instancia de Jupyter y la URL para acceder se mostrará en la ventana de la línea de comandos.

Una vez que accedas a la URL, deberías ver el índice del curso y poder navegar a cualquier archivo `*.ipynb`. Por ejemplo, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Añade tus Llaves API

Mantener tus llaves API seguras es importante al construir cualquier tipo de aplicación. Recomendamos no almacenar llaves API directamente en tu código. Publicarlas en un repositorio público podría causar problemas de seguridad e incluso costos indeseados si un actor malintencionado las utiliza.
Aquí hay una guía paso a paso para crear un archivo `.env` para Python y agregar tus credenciales de Microsoft Foundry Models:

> **Nota:** Los Modelos de GitHub (y su variable `GITHUB_TOKEN`) se retirarán a finales de julio de 2026. Esta guía usa [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) en su lugar. ¿Prefieres trabajar completamente offline? Mira [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Navega a tu directorio de proyecto**: Abre tu terminal o línea de comandos y navega al directorio raíz de tu proyecto donde quieres crear el archivo `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Crea el archivo `.env`**: Usa tu editor de texto preferido para crear un nuevo archivo llamado `.env`. Si usas la línea de comandos, puedes usar `touch` (en sistemas Unix) o `echo` (en Windows):

   Sistemas basados en Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Edita el archivo `.env`**: Abre el archivo `.env` en un editor de texto (ej., VS Code, Notepad++ u otro editor). Añade las siguientes líneas, reemplazando los marcadores con tu punto de enlace y llave API reales de Microsoft Foundry:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Guarda el archivo**: Guarda los cambios y cierra el editor de texto.

5. **Instala `python-dotenv`**: Si aún no lo has hecho, necesitarás instalar el paquete `python-dotenv` para cargar las variables de entorno desde el archivo `.env` en tu aplicación Python. Puedes instalarlo usando `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Carga las variables de entorno en tu script Python**: En tu script Python, usa el paquete `python-dotenv` para cargar las variables de entorno desde el archivo `.env`:

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

¡Eso es todo! Has creado correctamente un archivo `.env`, agregado tus credenciales de Microsoft Foundry Models y cargado esas variables en tu aplicación Python.

🔐 Nunca comites .env—ya está en .gitignore.
Las instrucciones completas del proveedor están en [`providers.md`](03-providers.md).

## 4. ¿Qué sigue?

| Quiero…            | Ir a…                                                                 |
|---------------------|---------------------------------------------------------------------|
| Empezar la Lección 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md) |
| Configurar un proveedor LLM | [`providers.md`](03-providers.md)                                 |
| Conocer a otros estudiantes | [Únete a nuestro Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Solución de problemas

| Síntoma                                   | Solución                                                      |
|-------------------------------------------|--------------------------------------------------------------|
| `python not found`                        | Añade Python al PATH o reabre la terminal después de instalar |
| `pip` no puede construir ruedas (Windows)| Ejecuta `pip install --upgrade pip setuptools wheel` y reintenta.|
| `ModuleNotFoundError: dotenv`             | Ejecuta `pip install -r requirements.txt` (el entorno no fue instalado).|
| Fallo al construir Docker *No queda espacio*| Docker Desktop ▸ *Settings* ▸ *Resources* → incrementa el tamaño del disco.|
| VS Code sigue pidiendo reabrir           | Puede que tengas ambas opciones activas; elige una (venv **o** contenedor)|
| Errores OpenAI 401 / 429                   | Verifica el valor de `OPENAI_API_KEY` / límites de tasa de solicitud.|
| Errores usando Conda                      | Instala las librerías de Microsoft AI usando `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->