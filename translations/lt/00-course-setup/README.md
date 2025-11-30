<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T02:25:16+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "lt"
}
-->
# Pradžia su šiuo kursu

Labai džiaugiamės, kad pradedate šį kursą ir nekantraujame pamatyti, ką sukursite naudodami generatyvinį dirbtinį intelektą!

Kad užtikrintume jūsų sėkmę, šiame puslapyje pateikiami nustatymo žingsniai, techniniai reikalavimai ir informacija, kur kreiptis pagalbos, jei prireiktų.

## Nustatymo žingsniai

Norėdami pradėti šį kursą, turite atlikti šiuos veiksmus.

### 1. Fork'inkite šį repo

[Padarykite šio repo fork'ą](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) savo GitHub paskyroje, kad galėtumėte keisti kodą ir atlikti užduotis. Taip pat galite [pažymėti šį repo žvaigždute (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), kad lengviau rastumėte jį ir susijusius repo.

### 2. Sukurkite Codespace

Kad išvengtumėte priklausomybių problemų vykdydami kodą, rekomenduojame šį kursą vykdyti [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Savo fork'e: **Code -> Codespaces -> New on main**

![Dialogo langas su mygtukais, leidžiančiais sukurti Codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Pridėkite slaptą raktą

1. ⚙️ Pavaros piktograma -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Pavadinkite OPENAI_API_KEY, įklijuokite savo raktą, išsaugokite.

### 3. Kas toliau?

| Noriu…              | Eiti į…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Pradėti 1 pamoką    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Dirbti neprisijungus | [`setup-local.md`](02-setup-local.md)                                   |
| Nustatyti LLM tiekėją | [`providers.md`](03-providers.md)                                        |
| Susipažinti su kitais mokiniais | [Prisijunkite prie mūsų Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Problemų sprendimas

| Simptomas                                | Sprendimas                                                      |
|------------------------------------------|-----------------------------------------------------------------|
| Konteinerio kūrimas užtruko > 10 min     | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`              | Terminalas neprisijungė; spustelėkite **+** ➜ *bash*            |
| `401 Unauthorized` iš OpenAI             | Neteisingas / pasibaigęs `OPENAI_API_KEY`                       |
| VS Code rodo “Dev container mounting…”   | Atnaujinkite naršyklės skirtuką—Codespaces kartais praranda ryšį |
| Trūksta Notebook branduolio              | Notebook meniu ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unix pagrindu veikiančios sistemos:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redaguokite `.env` failą**: Atidarykite `.env` failą teksto redaktoriuje (pvz., VS Code, Notepad++ ar kitame). Pridėkite šią eilutę į failą, pakeisdami `your_github_token_here` savo tikruoju GitHub token'u:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Išsaugokite failą**: Išsaugokite pakeitimus ir uždarykite teksto redaktorių.

5. **Įdiekite `python-dotenv`**: Jei dar to nepadarėte, turėsite įdiegti `python-dotenv` paketą, kad galėtumėte įkelti aplinkos kintamuosius iš `.env` failo į savo Python programą. Galite jį įdiegti naudodami `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Įkelkite aplinkos kintamuosius į savo Python skriptą**: Savo Python skripte naudokite `python-dotenv` paketą, kad įkeltumėte aplinkos kintamuosius iš `.env` failo:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Viskas! Jūs sėkmingai sukūrėte `.env` failą, pridėjote savo GitHub token'ą ir įkėlėte jį į savo Python programą.

## Kaip paleisti lokaliai savo kompiuteryje

Norėdami paleisti kodą lokaliai savo kompiuteryje, turite turėti įdiegtą [Python versiją](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Norėdami naudoti saugyklą, turite ją nukopijuoti:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kai viskas bus paruošta, galėsite pradėti!

## Papildomi žingsniai

### Miniconda diegimas

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) yra lengvas įrankis, skirtas įdiegti [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ir keletą paketų.
Conda yra paketų valdymo įrankis, kuris leidžia lengvai nustatyti ir keisti skirtingas Python [**virtualias aplinkas**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ir paketus. Jis taip pat naudingas diegiant paketus, kurių nėra `pip`.

Galite sekti [MiniConda diegimo vadovą](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), kad jį įdiegtumėte.

Įdiegę Miniconda, turite nukopijuoti [saugyklą](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jei dar to nepadarėte).

Tada turite sukurti virtualią aplinką. Norėdami tai padaryti su Conda, sukurkite naują aplinkos failą (_environment.yml_). Jei dirbate su Codespaces, sukurkite jį `.devcontainer` kataloge, taigi `.devcontainer/environment.yml`.

Užpildykite savo aplinkos failą šiuo fragmentu:

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

Jei susiduriate su klaidomis naudodami conda, galite rankiniu būdu įdiegti Microsoft AI bibliotekas naudodami šią komandą terminale.

```
conda install -c microsoft azure-ai-ml
```

Aplinkos failas nurodo mums reikalingas priklausomybes. `<environment-name>` reiškia pavadinimą, kurį norėtumėte naudoti savo Conda aplinkai, o `<python-version>` yra Python versija, kurią norėtumėte naudoti, pavyzdžiui, `3` yra naujausia pagrindinė Python versija.

Kai tai atliksite, galite sukurti savo Conda aplinką vykdydami šias komandas komandinėje eilutėje/terminale:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Jei susiduriate su problemomis, kreipkitės į [Conda aplinkų vadovą](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code naudojimas su Python palaikymo plėtiniu

Rekomenduojame naudoti [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) redaktorių su įdiegtu [Python palaikymo plėtiniu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) šiam kursui. Tačiau tai yra tik rekomendacija, o ne būtinybė.

> **Pastaba**: Atidarę kurso saugyklą VS Code, turėsite galimybę nustatyti projektą konteineryje. Tai įmanoma dėl [specialaus `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) katalogo, esančio kurso saugykloje. Apie tai daugiau vėliau.

> **Pastaba**: Kai nukopijuosite ir atidarysite katalogą VS Code, jis automatiškai pasiūlys įdiegti Python palaikymo plėtinį.

> **Pastaba**: Jei VS Code pasiūlys iš naujo atidaryti saugyklą konteineryje, atsisakykite šio pasiūlymo, kad galėtumėte naudoti lokaliai įdiegtą Python versiją.

### Jupyter naudojimas naršyklėje

Taip pat galite dirbti su projektu naudodami [Jupyter aplinką](https://jupyter.org?WT.mc_id=academic-105485-koreyst) tiesiai naršyklėje. Tiek klasikinis Jupyter, tiek [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) suteikia malonią kūrimo aplinką su tokiomis funkcijomis kaip automatinis užbaigimas, kodo paryškinimas ir kt.

Norėdami paleisti Jupyter lokaliai, eikite į terminalą/komandinę eilutę, pereikite į kurso katalogą ir vykdykite:

```bash
jupyter notebook
```

arba

```bash
jupyterhub
```

Tai paleis Jupyter instanciją, o URL, per kurį galima ją pasiekti, bus rodomas komandinės eilutės lange.

Kai pasieksite URL, turėtumėte matyti kurso planą ir galėsite naršyti po bet kurį `*.ipynb` failą. Pavyzdžiui, `08-building-search-applications/python/oai-solution.ipynb`.

### Paleidimas konteineryje

Alternatyva viską nustatyti savo kompiuteryje ar Codespace yra naudoti [konteinerį](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specialus `.devcontainer` aplankas kurso saugykloje leidžia VS Code nustatyti projektą konteineryje. Už Codespaces ribų tai reikalaus Docker įdiegimo, ir iš esmės tai reikalauja šiek tiek darbo, todėl rekomenduojame tai tik tiems, kurie turi patirties dirbant su konteineriais.

Vienas geriausių būdų apsaugoti savo API raktus naudojant GitHub Codespaces yra naudoti Codespace Secrets. Prašome sekti [Codespaces secrets valdymo](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) vadovą, kad sužinotumėte daugiau apie tai.

## Pamokos ir techniniai reikalavimai

Kursą sudaro 6 koncepcinės pamokos ir 6 programavimo pamokos.

Programavimo pamokoms naudojame Azure OpenAI Service. Jums reikės prieigos prie Azure OpenAI paslaugos ir API rakto, kad galėtumėte vykdyti šį kodą. Prieigai gauti galite [užpildyti šią paraišką](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kol jūsų paraiška bus apdorojama, kiekvienoje programavimo pamokoje taip pat yra `README.md` failas, kuriame galite peržiūrėti kodą ir rezultatus.

## Pirmą kartą naudojant Azure OpenAI Service

Jei pirmą kartą dirbate su Azure OpenAI paslauga, prašome sekti šį vadovą, kaip [sukurti ir įdiegti Azure OpenAI Service resursą.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Pirmą kartą naudojant OpenAI API

Jei pirmą kartą dirbate su OpenAI API, prašome sekti vadovą, kaip [sukurti ir naudoti sąsają.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Susipažinkite su kitais mokiniais

Mes sukūrėme kanalus mūsų oficialiame [AI bendruomenės Discord serveryje](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), kad galėtumėte susipažinti su kitais mokiniais. Tai puikus būdas užmegzti ryšius su kitais panašiai mąstančiais verslininkais, kūrėjais, studentais ir visais, kurie nori tobulėti generatyvinio dirbtinio intelekto srityje.

[![Prisijunkite prie Discord kanalo](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projekto komanda taip pat bus šiame Discord serveryje, kad padėtų mokiniams.

## Prisidėkite

Šis kursas yra atvirojo kodo iniciatyva. Jei pastebėsite tobulinimo galimybių ar problemų, prašome sukurti [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) arba užregistruoti [GitHub problemą](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projekto komanda stebės visus indėlius. Prisidėjimas prie atvirojo kodo yra nuostabus būdas kurti savo karjerą generatyvinio dirbtinio intelekto srityje.

Dauguma indėlių reikalauja, kad sutiktumėte su Contributor License Agreement (CLA), kuriame deklaruojate, kad turite teisę ir iš tikrųjų suteikiate mums teisę naudoti jūsų indėlį. Daugiau informacijos rasite [CLA, Contributor License Agreement svetainėje](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Kai pateiksite pull request, CLA-bot automatiškai nustatys, ar jums reikia pateikti CLA, ir atitinkamai pažymės PR (pvz., žyma, komentaras). Tiesiog sekite bot'o pateiktas instrukcijas. Tai reikės padaryti tik vieną kartą visose saugyklose, naudojančiose mūsų CLA.

Šis projektas priėmė [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Daugiau informacijos rasite Code of Conduct DUK arba susisiekite su [Email opencode](opencode@microsoft.com), jei turite papildomų klausimų ar komentarų.

## Pradėkime!
Dabar, kai atlikote reikalingus žingsnius, kad užbaigtumėte šį kursą, pradėkime nuo [įvado į generatyvinį dirbtinį intelektą ir LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius naudojant šį vertimą.