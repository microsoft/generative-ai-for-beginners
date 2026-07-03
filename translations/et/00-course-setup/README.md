# Selle kursuse alustamine

Oleme väga põnevil, et alustate seda kursust ja näete, mida Generative AI abil inspireeritud ehitada!

Et tagada teie edu, sisaldab see leht seadistusetappe, tehnilisi nõudeid ja teavet selle kohta, kust vajadusel abi saada.

## Seadistusetapid

Kursusel osalemiseks peate läbima järgmised sammud.

### 1. Forkige see repo

[Forkige kogu see repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) oma GitHubi kontole, et saaksite koodi muuta ja väljakutseid lõpetada. Samuti võite [jätta selle repo tärniga (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), et leida seda ja seotud reposi kergemini.

### 2. Looge codespace

Et vältida sõltuvusprobleeme koodi käivitamisel, soovitame selle kursuse käivitamiseks kasutada [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Oma forkis: **Code -> Codespaces -> New on main**

![Dialoog, mis näitab nuppe codespace loomiseks](../../../translated_images/et/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Lisage saladus

1. ⚙️ Hammasratta ikoon -> Command Palette-> Codespaces : Manage user secret -> Add a new secret.
2. Nimetage OPENAI_API_KEY, kleepige oma võti, Salvestage.

### 3. Mis edasi?

| Soovin…            | Minge…                                                                 |
|---------------------|------------------------------------------------------------------------|
| Alustada õppetundi 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Töötada offline     | [`setup-local.md`](02-setup-local.md)                                  |
| Seadistada LLM pakkuja | [`providers.md`](03-providers.md)                                     |
| Kohtuda teiste õppijatega | [Liituge meie Discordi serveriga](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Probleemide lahendamine


| Sümptom                                  | Lahendus                                                      |
|------------------------------------------|---------------------------------------------------------------|
| Containeri ehitus jääb kinni > 10 min    | **Codespaces ➜ „Rebuild Container”**                         |
| `python: command not found`               | Terminal ei olnud ühendatud; klõpsake **+** ➜ *bash*           |
| `401 Unauthorized` OpenAI poolt           | Vale või aegunud `OPENAI_API_KEY`                              |
| VS Code kuvab “Dev container mounting…”  | Värskendage brauseri vahekaarti — Codespaces kaotab vahel ühenduse |
| Notebooki kernel puudub                   | Notebooki menüüst ➜ **Kernel ▸ Select Kernel ▸ Python 3**     |

   Unixipõhised süsteemid:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muuda `.env` faili**: Avage `.env` fail tekstiredaktoris (nt VS Code, Notepad++ või mõni muu redaktor). Lisage faili järgmine rida, asendades `your_github_token_here` oma tegeliku GitHubi tokeniga:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salvestage fail**: Salvestage muudatused ja sulgege tekstiredaktor.

5. **Installige `python-dotenv`**: Kui te pole seda veel teinud, peate paigaldama `python-dotenv` paketi, et laadida keskkonnamuutujad `.env` failist oma Pythonirakendusse. Seda saab paigaldada `pip` abil:

   ```bash
   pip install python-dotenv
   ```

6. **Laadige keskkonnamuutujad oma Python skriptis**: Kasutage oma Python skriptis `python-dotenv` paketti `.env` failist keskkonnamuutujate laadimiseks:

   ```python
   from dotenv import load_dotenv
   import os

   # Laadi keskkonnamuutujad .env failist
   load_dotenv()

   # Juurdepääs GITHUB_TOKEN muutujale
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

See ongi kõik! Olete edukalt loonud `.env` faili, lisanud oma GitHubi tokeni ja laadinud selle oma Pythonirakendusse.

## Kuidas käivitada kohapeal oma arvutis

Koodi kohalikuks käivitamiseks peab arvutis olema paigaldatud mõni [Python versioon](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Seejärel on vaja repositori kloonida:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kui olete kõik kontrollinud, saate alustadagi!

## Valikulised sammud

### Miniconda paigaldamine

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kerge paigaldaja [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythoni ja mõne paketi installimiseks.
Conda on pakettide haldur, mis lihtsustab erinevate Python [**virtuaalkeskkondade**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettide seadistamist ning vahetamist. See on kasulik ka selliste pakkide paigaldamiseks, mida `pip` kaudu ei leidu.

Miniconda seadistamise juhendiga saate tutvuda siin: [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Miniconda paigaldamisel peate kloonima ka [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kui te pole veel teinud).

Järgmisena peate looma virtuaalkeskkonna. Selleks looge Condaga uus keskkonna fail (_environment.yml_). Kui kasutate Codespaces, looge see `.devcontainer` kataloogi sisse, st `.devcontainer/environment.yml`.

Täiendage keskkonna faili alljärgneva fragmentiga:

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

Kui conda kasutamisel tekib vigu, võite käsitsi Microsoft AI teegid paigaldada, kasutades terminalis järgmist käsku.

```
conda install -c microsoft azure-ai-ml
```

Keskkonna faili määrab, milliseid sõltuvusi vaja on. `<environment-name>` on nimi, mida soovite Conda keskkonnale anda, ja `<python-version>` on Python'i versioon, mida soovite kasutada, näiteks `3` tähistab Python'i uusimat põhiversiooni.

Pärast seda looge Conda keskkond järgnevate terminalikäskude abil:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alamtee kehtib ainult Codespace'i seadete puhul
conda activate ai4beg
```

Kui ilmneb probleeme, vaadake [Conda keskkondade juhendit](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code kasutamine koos Pythoni laiendiga

Soovitame kasutada selle kursuse puhul [Visual Studio Code'i (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) koos [Pythoni toe laiendiga](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). See on pigem soovitus, mitte kohustus.

> **Märkus**: Avades kursuse reposi VS Codes, on teil võimalus seada projekt konteinerisse. Selle võimaldab [eriline `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kataloog kursuse repos. Rohkem selle kohta hiljem.

> **Märkus**: Kui kloonite ja avate kausta VS Codes, soovitab see automaatselt paigaldada Pythoni toe laiendi.

> **Märkus**: Kui VS Code soovitab avada reposi uuesti konteineris, lükake see taotlus tagasi, et kasutada kohapeal paigaldatud Pythoni versiooni.

### Jupyteri kasutamine brauseris

Projektiga saate töötada ka brauseris asuva [Jupyteri keskkonna](https://jupyter.org?WT.mc_id=academic-105485-koreyst) kaudu. Nii klassikaline Jupyter kui ka [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) pakuvad mugavat arenduskeskkonda automaatse täitmise, süntaksikohanduse jne funktsioonidega.

Jupyteri käivitamiseks kohapeal minge terminali/konsooli, navigeerige kursuse kataloogi ja käivitage:

```bash
jupyter notebook
```

või

```bash
jupyterhub
```

See käivitab Jupyteri ning ligipääsu URL kuvatakse käsureal.

Kui URL-ile pääsete ligi, näete kursuse ülevaadet ja saate avada ükskõik millise `*.ipynb` faili, näiteks `08-building-search-applications/python/oai-solution.ipynb`.

### Käivitamine konteineris

Alternatiivina arvutisse või Codespacesisse paigaldamisele saate kasutada [konteinerit](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Kursuse reposis on eriline `.devcontainer` kaust, mis võimaldab VS Codel projekti konteinerisse seadistada. väljaspool Codespacesi tuleb seejärel paigaldada Docker ning see nõuab veidi rohkem tööd, seega soovitame seda kasutada ainult kontneritega juba tuttavatele.

Üks parimaid viise oma API võtmete turvaliseks hoidmiseks GitHub Codespacesis on kasutada Codespaces Secrets'i. Lisateabe saamiseks järgige juhendit [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Õppetunnid ja tehnilised nõuded

Kursusel on 6 kontseptsioonitundi ja 6 programmeerimistundi.

Programmeerimistundides kasutame Azure OpenAI teenust. Koodi käitamiseks vajate ligipääsu Azure OpenAI teenusele ja API võtit. Ligipääsu saamiseks saate taotluse esitada, [täites selle avalduse](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kuni teie taotlust töödeldakse, sisaldab iga programmeerimistund ka `README.md` faili, kus saate vaadata koodi ja väljundeid.

## Azure OpenAI teenuse esmakordne kasutamine

Kui kasutate Azure OpenAI teenust esimest korda, järgige palun juhendit, kuidas [luua ja juurutada Azure OpenAI teenuse ressurss.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API esmakordne kasutamine

Kui kasutate OpenAI API-d esimest korda, järgige juhendit, kuidas [luua ja kasutada liidest.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Kohtuge teiste õppijatega

Oleme loonud ametlikus [AI kogukonna Discord serveris](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kanaleid teiste õppijate kohtumiseks. See on suurepärane võimalus suhelda teiste ettevõtlike, ehitajate, üliõpilaste ja kõigiga, kes soovivad Generative AI alal areneda.

[![Liitu discord kanaliga](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektimeeskond on samuti sellel Discord serveril valmis aitama kõiki õppijaid.

## Panustamine

See kursus on avatud lähtekoodiga algatus. Kui märkate parandamist vajavaid kohti või probleeme, palun esitage [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) või logige [GitHubi probleem](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektimeeskond jälgib kõiki panuseid. Avatud lähtekoodile panustamine on suurepärane võimalus oma karjääri ehitamiseks Generative AI valdkonnas.

Enamik panuseid nõuab, et nõustuksite Panustaja litsentsilepingu (CLA) tingimustega, mis kinnitavad, et teil on õigus ja tegelikult annate meile õigused kasutada teie panust. Lisateabe saamiseks külastage [CLA, Contributor License Agreement veebilehte](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Oluline: selle repo teksti tõlkimisel palun ärge kasutage masintõlget. Tõlkeid kontrollitakse kogukonna poolt, seega palun pakkuda tõlkeid ainult keeltes, milles olete pädev.

Pull requesti esitamisel tuvastab CLA-bot automaatselt, kas peate esitama CLA ja märgistab PRi vastavalt (nt silt, kommentaar). Järgige lihtsalt boti juhiseid. Seda on vaja teha vaid korra kõigis repodes, mis kasutavad meie CLA-t.

See projekt on vastu võtnud [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Lisateabe saamiseks lugege juhiseid või võtke ühendust aadressil [Email opencode](opencode@microsoft.com) täiendavate küsimuste või kommentaaride korral.

## Alustame!
Nüüd, kui olete lõpetanud selle kursuse vajalikud sammud, alustame [Sissejuhatusega generatiivse tehisintellekti ja suurtõlkimismudelite juurde](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud AI-tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüdleme täpsuse poole, palun pidage meeles, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles loetakse autoriteetseks allikaks. Kriitilise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->