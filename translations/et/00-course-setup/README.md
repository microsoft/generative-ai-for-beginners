<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T02:51:41+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "et"
}
-->
# Kursusega alustamine

Meil on väga hea meel, et alustate seda kursust ja näete, milliseid ideid generatiivne tehisintellekt inspireerib teid looma!

Teie edu tagamiseks on sellel lehel välja toodud seadistamise sammud, tehnilised nõuded ja juhised, kust vajadusel abi saada.

## Seadistamise sammud

Kursuse alustamiseks peate läbima järgmised sammud.

### 1. Forkige see repo

[Forkige kogu see repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) oma GitHubi kontole, et saaksite koodi muuta ja väljakutseid täita. Samuti saate [tärniga (🌟) tähistada seda repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), et seda ja seotud repod lihtsamini leida.

### 2. Looge Codespace

Et vältida sõltuvusprobleeme koodi käivitamisel, soovitame seda kursust käivitada [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) keskkonnas.

Teie forkis: **Code -> Codespaces -> New on main**

![Dialoog, mis näitab nuppe Codespace'i loomiseks](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Lisage salajane võti

1. ⚙️ Hammasratta ikoon -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Nimetage OPENAI_API_KEY, kleepige oma võti, salvestage.

### 3. Mis edasi?

| Ma tahan…           | Mine siia…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Alustada 1. õppetundi | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Töötada võrguühenduseta | [`setup-local.md`](02-setup-local.md)                                   |
| Seadistada LLM teenusepakkuja | [`providers.md`](03-providers.md)                                        |
| Kohtuda teiste õppijatega | [Liitu meie Discordiga](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Probleemide lahendamine

| Sümptom                                   | Lahendus                                                         |
|-------------------------------------------|------------------------------------------------------------------|
| Konteineri ehitamine kestab > 10 minutit  | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal ei ühendanud; klõpsake **+** ➜ *bash*                  |
| `401 Unauthorized` OpenAI-lt              | Vale / aegunud `OPENAI_API_KEY`                                 |
| VS Code näitab “Dev container mounting…”  | Värskendage brauseri vahelehte—Codespaces kaotab vahel ühenduse |
| Notebooki kernel puudub                   | Notebooki menüü ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Unix-põhised süsteemid:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muutke `.env` faili**: Avage `.env` fail tekstiredaktoris (nt VS Code, Notepad++ või mõni muu redaktor). Lisage failile järgmine rida, asendades `your_github_token_here` oma tegeliku GitHubi tokeniga:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salvestage fail**: Salvestage muudatused ja sulgege tekstiredaktor.

5. **Installige `python-dotenv`**: Kui te pole seda veel teinud, peate installima `python-dotenv` paketi, et laadida keskkonnamuutujad `.env` failist oma Python rakendusse. Seda saab installida `pip` abil:

   ```bash
   pip install python-dotenv
   ```

6. **Laadige keskkonnamuutujad oma Python skriptis**: Kasutage oma Python skriptis `python-dotenv` paketti, et laadida keskkonnamuutujad `.env` failist:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ja ongi kõik! Olete edukalt loonud `.env` faili, lisanud oma GitHubi tokeni ja laadinud selle oma Python rakendusse.

## Kuidas käivitada kohalikult oma arvutis

Koodi kohalikuks käivitamiseks oma arvutis peate olema installinud mõne versiooni [Pythonist](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Seejärel peate repo kloonima:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kui kõik on alla laaditud, saate alustada!

## Valikulised sammud

### Miniconda installimine

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kerge paigaldusprogramm [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ja mõnede pakettide installimiseks.
Conda ise on paketihaldur, mis teeb lihtsaks erinevate Python [**virtuaalsete keskkondade**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettide seadistamise ja vahetamise. Samuti on see kasulik pakettide installimiseks, mis pole saadaval `pip` kaudu.

Miniconda seadistamiseks järgige [Miniconda paigaldusjuhendit](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Kui Miniconda on paigaldatud, peate kloonima [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kui te pole seda veel teinud).

Seejärel peate looma virtuaalse keskkonna. Selleks kasutage Conda't ja looge uus keskkonnafail (_environment.yml_). Kui kasutate Codespaces'i, looge see `.devcontainer` kataloogi, seega `.devcontainer/environment.yml`.

Täiendage oma keskkonnafaili alloleva koodiga:

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

Kui teil tekib Conda kasutamisel vigu, saate Microsofti AI raamatukogud käsitsi installida, kasutades järgmist käsku terminalis.

```
conda install -c microsoft azure-ai-ml
```

Keskkonnafail määrab vajalikud sõltuvused. `<environment-name>` viitab nimele, mida soovite oma Conda keskkonnale anda, ja `<python-version>` on Python versioon, mida soovite kasutada, näiteks `3`, mis on Python'i uusim peamine versioon.

Kui see on tehtud, saate oma Conda keskkonna luua, käivitades allolevad käsud käsureal/terminalis:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Kui teil tekib probleeme, vaadake [Conda keskkondade juhendit](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code'i kasutamine Python'i laiendiga

Soovitame selle kursuse jaoks kasutada [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) redaktorit koos [Python'i laiendiga](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). See on siiski soovitus, mitte kohustus.

> **Märkus**: Kursuse repo avamisel VS Code'is on teil võimalus projekt konteineris seadistada. Seda võimaldab kursuse repo spetsiaalne [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kataloog. Rohkem infot hiljem.

> **Märkus**: Kui kloonite ja avate kataloogi VS Code'is, soovitab see automaatselt installida Python'i laiendi.

> **Märkus**: Kui VS Code soovitab teil repo konteineris uuesti avada, keelduge sellest, et kasutada kohalikult installitud Python'i versiooni.

### Jupyteri kasutamine brauseris

Projekti kallal töötamiseks saate kasutada [Jupyter keskkonda](https://jupyter.org?WT.mc_id=academic-105485-koreyst) otse oma brauseris. Nii klassikaline Jupyter kui ka [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) pakuvad meeldivat arenduskeskkonda, kus on automaatne täiendamine, koodi esiletõstmine jne.

Jupyteri kohalikuks käivitamiseks minge terminali/käsureale, navigeerige kursuse kataloogi ja käivitage:

```bash
jupyter notebook
```

või

```bash
jupyterhub
```

See käivitab Jupyteri instantsi ja URL selle juurde pääsemiseks kuvatakse käsurea aknas.

Kui olete URL-i avanud, peaksite nägema kursuse ülevaadet ja saama navigeerida mis tahes `*.ipynb` faili juurde. Näiteks `08-building-search-applications/python/oai-solution.ipynb`.

### Käivitamine konteineris

Alternatiiviks kõige seadistamisele oma arvutis või Codespaces'is on kasutada [konteinerit](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Kursuse repo spetsiaalne `.devcontainer` kaust võimaldab VS Code'il projekti konteineris seadistada. Väljaspool Codespaces'i nõuab see Docker'i paigaldamist ja ausalt öeldes on see veidi keerulisem, seega soovitame seda ainult neile, kellel on kogemusi konteineritega töötamisel.

Üks parimaid viise oma API võtmete turvalisuse tagamiseks GitHub Codespaces'i kasutamisel on kasutada Codespace Secrets'i. Järgige [Codespaces'i salajaste võtmete haldamise juhendit](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), et sellest rohkem teada saada.

## Õppetunnid ja tehnilised nõuded

Kursus sisaldab 6 kontseptuaalset õppetundi ja 6 koodiga seotud õppetundi.

Koodiga seotud õppetundide jaoks kasutame Azure OpenAI teenust. Selle koodi käivitamiseks vajate juurdepääsu Azure OpenAI teenusele ja API võtit. Juurdepääsu saamiseks saate [täita selle taotluse](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kui teie taotlust töödeldakse, sisaldab iga koodiga seotud õppetund ka `README.md` faili, kus saate vaadata koodi ja väljundeid.

## Azure OpenAI teenuse esmakordne kasutamine

Kui see on teie esimene kord Azure OpenAI teenusega töötada, järgige juhendit, kuidas [luua ja juurutada Azure OpenAI teenuse ressurssi.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API esmakordne kasutamine

Kui see on teie esimene kord OpenAI API-ga töötada, järgige juhendit, kuidas [luua ja kasutada liidest.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Kohtuge teiste õppijatega

Oleme loonud kanalid meie ametlikus [AI Community Discord serveris](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), et kohtuda teiste õppijatega. See on suurepärane viis suhelda teiste sarnaste huvidega ettevõtjate, arendajate, tudengite ja generatiivse tehisintellekti valdkonnas areneda soovivate inimestega.

[![Liitu Discordi kanaliga](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektimeeskond on samuti sellel Discordi serveris, et aidata õppijaid.

## Panustamine

See kursus on avatud lähtekoodiga algatus. Kui näete parendamise võimalusi või probleeme, looge [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) või logige [GitHubi probleem](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektimeeskond jälgib kõiki panuseid. Avatud lähtekoodiga panustamine on suurepärane viis oma karjääri edendamiseks generatiivse tehisintellekti valdkonnas.

Enamik panuseid nõuab, et nõustuksite Kaastöötaja Litsentsilepinguga (CLA), mis kinnitab, et teil on õigus ja tegelikult annate meile õiguse teie panust kasutada. Lisateabe saamiseks külastage [CLA, Kaastöötaja Litsentsilepingu veebisaiti](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Kui esitate pull request'i, määrab CLA-bot automaatselt, kas peate CLA-d esitama, ja lisab PR-le vastava märgise või kommentaari. Järgige lihtsalt boti antud juhiseid. Seda peate tegema ainult üks kord kõigi meie CLA-d kasutavate repode puhul.

See projekt on vastu võtnud [Microsofti avatud lähtekoodi käitumisjuhendi](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Lisateabe saamiseks lugege käitumisjuhendi KKK-d või võtke ühendust [Email opencode](opencode@microsoft.com), kui teil on täiendavaid küsimusi või kommentaare.

## Alustame!
Nüüd, kui olete lõpetanud kõik vajalikud sammud selle kursuse läbimiseks, alustame [Generatiivse tehisintellekti ja LLM-ide sissejuhatusega](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.