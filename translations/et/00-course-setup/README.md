# Selle kursusega alustamine

Me oleme väga põnevil, et alustate seda kursust ja näete, mida teid inspireerib Generatiivse AI abil ehitama!

Oma edu tagamiseks kirjeldab see leht seadistamise samme, tehnilisi nõudeid ja seda, kust vajadusel abi saada.

## Seadistamise sammud

Selle kursuse läbimiseks peate täitma järgmised sammud.

### 1. Forki see repo

[Forkige see kogu repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) oma GitHubi kontole, et saaksite koodi muuta ja ülesandeid sooritada. Samuti võite [tähistada (🌟) seda repo-d](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), et seda ja seotud repod hõlpsamini leida.

### 2. Loo codespace

Koodi täitmisel sõltuvuste probleemide vältimiseks soovitame seda kursust käivitada [GitHub Codespaces’is](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Oma forkis: **Code -> Codespaces -> New on main**

![Dialoog, mis näitab nuppe codespace’i loomiseks](../../../translated_images/et/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Lisa salajane võti

1. ⚙️ Hammasratta ikoon -> Command Pallete -> Codespaces: Manage user secret -> Lisa uus salajane võti.
2. Nimi OPENAI_API_KEY, kleebi oma võti, Salvesta.

### 3. Mis edasi?

| Tahaksin…           | Minge…                                                                 |
|---------------------|------------------------------------------------------------------------|
| Alustada õppetundi 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Töötada võrguühenduseta | [`setup-local.md`](02-setup-local.md)                                   |
| Seadistada LLM pakkuja | [`providers.md`](03-providers.md)                                        |
| Tutvuda teiste õppijatega | [Liitu meie Discordiga](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Tõrkeotsing


| Sümptom                                 | Lahendus                                                        |
|-----------------------------------------|----------------------------------------------------------------|
| Konteineri ehitus takerdub > 10 minutit | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`             | Terminal ei olnud seotud; klõpsake **+** ➜ *bash*               |
| `401 Unauthorized` OpenAI’st             | Vale / aegunud `OPENAI_API_KEY`                                 |
| VS Code kuvab “Dev container mounting…” | Värskenda brauseri vaheleht—Codespaces kaotab mõnikord ühenduse |
| Märkmiku kernel puudub                   | Märkmiku menüü ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unix-põhised süsteemid:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muuda `.env` faili**: Ava `.env` fail tekstiredaktoris (nt VS Code, Notepad++ või mistahes muus redaktoris). Lisa failile järgmised read, asendades kohatäited oma Microsoft Foundry Models lõpp-punkti ja võtmega (vt [`providers.md`](03-providers.md), kuidas need saada):

   > **Märkus:** GitHubi mudelid (ja nende `GITHUB_TOKEN` muutuja) lõpetavad tegevuse 2026. aasta juuli lõpus. Selle asemel kasuta [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Salvesta fail**: Salvesta muudatused ja sulge tekstiredaktor.

5. **Paigalda `python-dotenv`**: Kui seda pole veel installitud, siis pead paigaldama `python-dotenv` paketi, et laadida keskkonnamuutujaid `.env` failist oma Python rakendusse. Saad paigaldada selle `pip` abil:

   ```bash
   pip install python-dotenv
   ```

6. **Laadi keskkonnamuutujad oma Python skriptis**: Kasuta `python-dotenv` paketti, et laadida keskkonnamuutujad `.env` failist oma Python skriptis:

   ```python
   from dotenv import load_dotenv
   import os

   # Laadi keskkonnamuutujad failist .env
   load_dotenv()

   # Juurdepääs Microsoft Foundry mudelitele muutujaid
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

See on kõik! Sa lõid edukalt `.env` faili, lisasid Microsoft Foundry Models volitused ja laadisid need oma Python rakendusse.

## Kuidas käivitada lokaalselt oma arvutis

Koodi käivitamiseks lokaalselt oma arvutis peate olema oma seadmesse installinud mingi versiooni [Pythonist](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Seejärel peate repository kloonima:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kui kõik on kontrollitud, võite alustada!

## Valikulised sammud

### Miniconda paigaldamine

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kergekaaluline paigaldaja [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythoni ja mõne muu paketi paigaldamiseks.
Conda ise on pakihaldur, mis lihtsustab Python [**virtuaalsete keskkondade**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettide seadistamist ning nende vahel vahetamist. See on kasulik ka pakettide paigaldamiseks, mis ei ole saadaval `pip` kaudu.

Võite järgida [MiniConda paigaldamise juhendit](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) selle seadistamiseks.

Kui Miniconda on paigaldatud, siis klooni [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kui sa pole seda veel teinud)

Seejärel loo virtuaalkeskkond. Conda abil loo uus keskkonna fail (_environment.yml_). Kui kasutad Codespaces’e, loo see `.devcontainer` kaustas, st `.devcontainer/environment.yml`.

Täida oma keskkonna fail alljärgneva näidisega:

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

Kui Conda kasutamisel tekivad vead, võid käsitsi paigaldada Microsoft AI teegid, kasutades terminalis järgmist käsku.

```
conda install -c microsoft azure-ai-ml
```

Keskkonna fail määrab sõltuvused, mida vajame. `<environment-name>` on nimi, mida soovid oma Conda keskkonnale anda ja `<python-version>` on Pythoni versioon, mida soovid kasutada, näiteks `3` on uuem peamine Pythoni versioon.

Kui see on tehtud, siis loo oma Conda keskkond, käivitades alljärgnevad käsud oma käsureal/terminalis

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alamtee kehtib ainult Codespace'i seadistuste puhul
conda activate ai4beg
```

Kui tekivad probleemid, vaata [Conda keskkondade juhendit](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code kasutamine koos Python laiendusega

Soovitame selle kursuse puhul kasutada [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) redaktorit koos [Python toe laiendusega](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). See on pigem soovitus, mitte kohustus.

> **Märkus**: Kursuse repod avades VS Code’is on olemas võimalus projekti paigaldada konteineri sees. Selle võimaluse annab [eriline `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kaust kursuse repos. Rohkem sellest hiljem.

> **Märkus**: Kui kloonid ja avad kausta VS Code’is, soovitatakse automaatselt Python toe laiendit paigaldada.

> **Märkus**: Kui VS Code soovitab repot konteineris uuesti avada, siis keeldumiseks, kui soovid kasutada lokaalselt paigaldatud Pythoni versiooni.

### Jupyteri kasutamine brauseris

Saad ka projektiga töötada otse brauseris, kasutades [Jupyterit](https://jupyter.org?WT.mc_id=academic-105485-koreyst). Nii klassikaline Jupyter kui ka [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) pakuvad meeldivat arenduskeskkonda automaatse täitmise, koodi esiletõstmise jmt funktsioonidega.

Jupyteri käivitamiseks lokaalselt mine terminali/käsureale, liigu kursuse kausta ja käivita:

```bash
jupyter notebook
```

või

```bash
jupyterhub
```

See käivitab Jupyteri ja URL, millega sellele ligi pääseda, kuvatakse käsurea aknas.

URL-ile ligi pääsedes peaksid nägema kursuse ülesehitust ja saama liikuda ükskõik millisesse `*.ipynb` faili. Näiteks `08-building-search-applications/python/oai-solution.ipynb`.

### Käivitamine konteineris

Alternatiiv arvutisse või codespace’i seadistamisele on kasutada [konteinerit](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Eriline `.devcontainer` kaust kursuse repos võimaldab VS Code’il seadistada projekti konteineris. Codespace’ist väljaspool vajab see Dockeri paigaldamist ja teatud tööd, seega soovitame seda teha neile, kellel konteineritega kogemusi on.

Üks parimaid viise API võtmete turvaliseks hoidmiseks GitHub Codespaces’i kasutades on Codespace Secrets’i kasutamine. Palun vaata [Codespaces salajaste võtmete haldamise](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) juhendit täpsemaks info saamiseks.


## Õppetunnid ja tehnilised nõuded

Kursusel on 6 kontseptsiooniõppetundi ja 6 programmeerimistund.

Programmeerimistundide jaoks kasutame Azure OpenAI teenust. Selle koodi tööle panemiseks on vajalik Azure OpenAI teenuse ligipääs ja API võti. Ligipääsu saamiseks saad [täita selle avalduse](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Samal ajal kui ootad avalduse menetlust, sisaldab iga programmeerimistund ka `README.md` faili, kus saad vaadata koodi ja väljundeid.

## Azure OpenAI teenuse kasutamine esimest korda

Kui kasutad Azure OpenAI teenust esimest korda, palun järgi seda juhendit, kuidas luua ja juurutada Azure OpenAI teenuse ressurss. [Loe juhendit siit](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API kasutamine esimest korda

Kui kasutad OpenAI API-d esimest korda, palun järgi juhendit, kuidas [luua ja kasutada liidest.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Tutvu teiste õppijatega

Oleme loonud kanalid ametlikus [AI kogukonna Discord serveris](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) teiste õppijatega tutvumiseks. See on suurepärane võimalus võrgustiku loomiseks sarnase mõtlemisega ettevõtjate, arendajate, tudengite ja kõigi teistega, kes soovivad Generatiivset AI-d paremini osata.

[![Liitu discord kanaliga](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektimeeskond on samuti sellel Discord serveril, et aidata õppijaid.

## Panusta

See kursus on avatud lähtekoodiga algatus. Kui näed parendusvõimalusi või vigu, palun loo [tõmbepäring (Pull Request)](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) või registreeri [GitHubi probleem](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektimeeskond jälgib kõiki panuseid. Panustamine avatud lähtekoodile on suurepärane võimalus ehitada oma karjääri Generatiivse AI valdkonnas.

Enamik panuseid nõuab, et nõustuksid panustaja litsentsilepinguga (CLA), mis kinnitab, et sul on õigus ja sa annad meile õiguse sinu panust kasutada. Rohkem teavet leiad [CLA, Contributor License Agreement veebilehelt](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Tähtis: selles repos teksti tõlkimisel palun ära kasuta masintõlget. Kinnitame tõlkeid kogukonna kaudu, seega palun paku oma abi tõlgetes ainult neis keeltes, mida oskad hästi.

Kui esitad tõmbepäringu, CLA-bot otsustab automaatselt, kas pead esitama CLA ja lisab vastava märgise või kommentaari tõmbepäringule. Järgi lihtsalt boti juhiseid. Seda tuleb teha vaid üks kord kõigi meie CLA kasutavate repode puhul.


See projekt on võtnud kasutusele [Microsofti avatud lähtekoodi käitumiskoodeksi](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Lisateabe saamiseks lugege käitumiskoodeksi KKK-d või võtke ühendust [Email opencode](opencode@microsoft.com), kui teil on lisaküsimusi või kommentaare.

## Alustame

Nüüd, kui olete lõpetanud selle kursuse jaoks vajalikud sammud, alustame [sissejuhatusega generatiivsesse tehisintellekti ja suurtel keelemudelitel](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->