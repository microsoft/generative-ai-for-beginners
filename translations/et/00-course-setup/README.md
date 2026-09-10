# Selle kursuse alustamine

Meil on väga hea meel, et alustate seda kursust ja näete, mida teie inspireerituna Generatiivse tehisintellektiga ehitada saate!

Teie edu tagamiseks kirjeldab see leht seadistamise samme, tehnilisi nõudeid ja kust abi saada, kui vaja.

## Seadistamise sammud

Selle kursuse alustamiseks peate täitma järgmised sammud.

### 1. Forkige see hoidla

[Forkige see kogu hoidla](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) enda GitHubi kontole, et saaksite koodi muuta ja väljakutseid täita. Samuti võite [seda hoidlat tähistada (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), et leida seda ja seotud hoidlaid kergemini.

### 2. Looge koodiruumi (codespace)

Et vältida sõltuvusprobleeme koodi käivitamisel, soovitame seda kursust kasutada [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) keskkonnas.

Oma forkis: **Code -> Codespaces -> New on main**

![Dialoog, mis kuvab nuppe koodiruumi loomiseks](../../../translated_images/et/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Lisage salajane võtmeandmed

1. ⚙️ Hammasratta ikoon -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Nimetage see OPENAI_API_KEY, kleepige oma võti ja salvestage.

### 3. Mis järgmiseks?

| Ma tahan…           | Liigu…                                                                   |
|---------------------|-------------------------------------------------------------------------|
| Alustada õppetundi 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Töö offline’is      | [`setup-local.md`](02-setup-local.md)                                   |
| Loo LLM-i pakkuja    | [`providers.md`](03-providers.md)                                        |
| Tutvuda teiste õppijatega | [Liitu meie Discordiga](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Tõrkeotsing


| Sümptom                                  | Lahendus                                                         |
|------------------------------------------|-----------------------------------------------------------------|
| Konteineri ehitus takerdub > 10 min        | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal ei kinnitunud; klõpsake **+** ➜ *bash*                   |
| `401 Unauthorized` OpenAI-lt              | Vale või aegunud `OPENAI_API_KEY`                                 |
| VS Code kuvab “Dev container mounting…”   | Värskendage brauseri vahekaarti—Codespaces kaotab vahel ühenduse  |
| Märkmiku tuuma puudumine                  | Märkmiku menüü ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-põhised süsteemid:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Muuda `.env` faili**: Ava `.env` fail tekstiredaktoris (nt VS Code, Notepad++ või mõnes muus redaktoris). Lisa faili järgmised read, asendades kohatäited oma Microsoft Foundry mudelite lõpp-punkti ja võtmega (vaata [`providers.md`](03-providers.md), kuidas neid saada):

   > **Märkus:** GitHub Models (ja selle `GITHUB_TOKEN` muutuja) suletakse 2026. aasta juuli lõpus. Kasuta selle asemel [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Salvesta fail**: Salvesta tehtud muudatused ja sulge tekstiredaktor.

5. **Installi `python-dotenv`**: Kui sa pole seda veel teinud, pead paigaldama `python-dotenv` paketi, et laadida keskkonnamuutujad `.env` failist oma Python rakendusse. Seda saab paigaldada `pip` abil:

   ```bash
   pip install python-dotenv
   ```

6. **Laadi keskkonnamuutujad oma Python skriptis**: Oma Python skriptis kasuta `python-dotenv` paketti, et laadida keskkonnamuutujad `.env` failist:

   ```python
   from dotenv import load_dotenv
   import os

   # Laadi keskkonnamuutujad .env failist
   load_dotenv()

   # Juurdepääs Microsoft Foundry Models muutujatele
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

See on kõik! Oled edukalt loonud `.env` faili, lisanud Microsoft Foundry mudelite mandaadid ja laadinud need oma Python rakendusse.

## Kuidas käivitada kohapeal arvutis

Koodi kohapeal arvutis käivitamiseks peab sul olema mõni [Python versioon paigaldatud](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Seejärel hoidla kasutamiseks tuleb see kloonida:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kui kõik on kloonitud, võid alustada!

## Valikulised sammud

### Miniconda paigaldamine

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) on kerge paigaldaja, mis võimaldab paigaldada [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythonit ja mõningaid pakette.
Conda ise on paketihaldur, mis lihtsustab erinevate Python [virtuaalsete keskkondade](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ja pakettide seadistamist ning vahetamist. See on kasulik ka `pip`-ist mitte-saadaval olevate pakettide installimiseks.

Järgi [MiniConda installatsioonijuhendit](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), et selle üles seada.

Miniconda paigaldamisel klooni hoidla [https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (kui seda pole veel tehtud)

Järgmiseks loo virtuaalne keskkond. Conda kasutamisel loo uus keskkonna fail (_environment.yml_). Kui järgite Codespaces keskkonnas, loo see `.devcontainer` kausta, st `.devcontainer/environment.yml`.

Täida keskkonna fail alljärgneva näidisega:

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

Kui Conda kasutamisel tekib vigu, saab Microsoft AI teegid installida käsitsi alljärgneva käsu abil terminalis.

```
conda install -c microsoft azure-ai-ml
```

Keskkonna fail määrab vajalikud sõltuvused. `<environment-name>` on nimi, mida soovid kasutada oma Conda keskkonnale, `<python-version>` on soovitud Python versioon, näiteks `3` on uusim tähtversioon.

Kui see tehtud, loo Conda keskkond, käivitades alljärgnevad käsud käsureal/terminalis

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontaineri alamtee kehtib ainult Codespace'i seadistuste puhul
conda activate ai4beg
```

Kui tekib probleeme, vaata [Conda keskkondade juhendit](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code kasutamine koos Python toega

Soovitame selle kursuse jaoks kasutada [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) redaktorit koos [Python toe laiendusega](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). See on pigem soovitus, mitte kohustus.

> **Märkus**: Kursuse hoidla avamisel VS Codes on võimalik projekt seadistada konteineris. Selle võimaldab kursuse hoidlas olev eriline [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kaust. Rohkem sellest hiljem.

> **Märkus**: Kui kloonid ja avad kausta VS Codes, soovitab programm automaatselt paigaldada Python toe laienduse.

> **Märkus**: Kui VS Code palub koduhoidla uuesti konteineris avada, keeldudes sellest, et kasutada kohalikult paigaldatud Pythonit.

### Jupyteri kasutamine brauseris

Võid tööd teha ka otse brauseris kasutades [Jupyterit](https://jupyter.org?WT.mc_id=academic-105485-koreyst). Nii klassikaline Jupyter kui ka [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) pakuvad mugavat arenduskeskkonda, mille funktsioonideks on automaatne täitmine, koodi esiletõstmine jne.

Jupyteri käivitamiseks lokaalselt ava terminal/ käsurida, liigu kursuse kausta ja käivita:

```bash
jupyter notebook
```

või

```bash
jupyterhub
```

See käivitab Jupyteri ning käsureal kuvatakse sellele ligipääsu URL.

Kui jõuad URL-ini, näed kursuse sisu ning saad avada suvalise `*.ipynb` faili. Näiteks `08-building-search-applications/python/oai-solution.ipynb`.

### Käivitamine konteineris

Alternatiiviks arvutisse või Codespace’i seadistamisele on kasutada [konteinerit](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Kursuse hoidlas olev eriline `.devcontainer` kaust võimaldab VS Codel projekti konteineris seadistada. Outside of Codespaces nõuab see Dockeri installeerimist, mis võtab aega ja on keerulisem, seega soovitame seda ainult neile, kel on konteineritega kogemusi.

Üks parimaid viise turvaliselt hoida oma API võtmeid GitHub Codespaces keskkonnas on kasutades Codespace Secrets funktsiooni. Palun vaata [Codespaces salajaste andmete halduse juhendit](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).


## Õppetunnid ja tehnilised nõuded

Kursusel on "Learn" õppetunnid, mis selgitavad Generatiivse tehisintellekti mõisteid ning "Build" õppetunnid käed-külge koodinäidetega nii **Pythonis** kui ka **TypeScriptis**, kui võimalik.

Koodiõppetundides kasutame Azure OpenAI-d Microsoft Foundrys. Sul peab olema Azure tellimus ja API võti. Ligipääs on avatud - vajalikku taotlust ei ole - seega saad [luua Microsoft Foundry ressursi ja juurutada mudeli](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst), et saada oma lõpp-punkt ja võti.

Igas koodiõppetunnis on ka `README.md` fail, kus saad koodi ja väljundeid ilma käivitamata vaadata.

## Azure OpenAI teenuse kasutamine esimest korda

Kui kasutad Azure OpenAI teenust esimest korda, palun järgi juhendit, kuidas [luua ja juurutada Azure OpenAI Teenuse ressurss.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API kasutamine esimest korda

Kui kasutad OpenAI API-t esimest korda, palun järgi juhendit, kuidas [luua ja kasutada liidest.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Tutvu teiste õppijatega

Oleme loonud oma ametlikus [AI kogukonna Discord serveris](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kanaleid, kus saab suhelda teiste õppijatega. See on suurepärane viis võrgustiku loomiseks koos teiste idufirmade asutajate, arendajate, tudengite ja kõigiga, kes soovivad Generatiivse tehisintellekti oskusi täiustada.

[![Liitu discord kanaliga](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektimeeskond on samuti sellel Discord serveril, et aidata õppijaid.

## Panusta

See kursus on avatud lähtekoodiga algatus. Kui märkad parandusvõimalusi või vigu, loo palun [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) või sisesta [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektimeeskond jälgib kõiki panuseid. Panustamine avatud lähtekoodi on suurepärane viis oma Generatiivse tehisintellekti karjääri arendamiseks.

Enamik panuseid nõuab, et nõustuksid Panustaja litsentsilepinguga (CLA), mis väidab, et sul on õigus ja sa annad meile õiguse sinu panust kasutada. Täpsemalt vaata [CLA, Panustaja litsentsilepingu veebisaiti](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Oluline: Kui tõlgid selle hoidla teksti, siis palun ära kasuta masintõlget. Me kontrollime tõlkeid kogukonna abil, seega palun märgi ennast tõlketööle ainult neis keeltes, mida sa hästi valdad.


Kui esitate tõmbepäringu, määrab CLA-bot automaatselt, kas peate esitama CLA ja märgistab tõmbepäringu vastavalt (näiteks sildi või kommentaariga). Lihtsalt järgige bot'i pakutud juhiseid. Seda peate tegema ainult korra kõigis meie CLA-d kasutavates hoidlates.

See projekt on vastu võtnud [Microsofti avatud lähtekoodi käitumisjuhised](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Lisateabe saamiseks lugege käitumisjuhiste KKK-d või võtke ühendust aadressil [Email opencode](opencode@microsoft.com) kõigi täiendavate küsimuste või kommentaaride korral.

## Alustame

Nüüd, kui olete selle kursuse läbimiseks vajalikud sammud teinud, alustame [sissejuhatusega generatiivsel AI-l ja LLM-del](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->