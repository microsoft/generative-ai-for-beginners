<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c110db04c35490138065d75c34041823",
  "translation_date": "2025-08-25T12:21:33+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "lt"
}
-->
# Pradžia su šiuo kursu

Labai džiaugiamės, kad pradedate šį kursą ir laukiame, ką įkvėpti sukursite naudodami generatyvųjį dirbtinį intelektą!

Kad jums sektųsi, šiame puslapyje aprašyti paruošimo žingsniai, techniniai reikalavimai ir pagalbos gavimo būdai, jei jos prireiktų.

## Paruošimo žingsniai

Norėdami pradėti šį kursą, turite atlikti šiuos veiksmus.

### 1. Fork’inkite šį repozitoriją

[Padarykite šio repozitorijos fork’ą](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) į savo GitHub paskyrą, kad galėtumėte keisti kodą ir atlikti užduotis. Taip pat galite [pažymėti šį repozitorijų žvaigždute (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), kad lengviau jį ir susijusius repozitorijus rastumėte.

### 2. Sukurkite codespace

Kad išvengtumėte priklausomybių problemų paleidžiant kodą, rekomenduojame šį kursą vykdyti [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) aplinkoje.

Savo fork’e: **Code -> Codespaces -> New on main**

![Dialogas su mygtukais codespace’ui sukurti](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Pridėkite slaptą raktą

1. ⚙️ Krumpliaračio piktograma -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Įrašykite OPENAI_API_KEY, įklijuokite savo raktą, išsaugokite.

### 3. Kas toliau?

| Noriu…               | Eiti į…                                                                 |
|----------------------|--------------------------------------------------------------------------|
| Pradėti 1 pamoką      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Dirbti neprisijungus  | [`setup-local.md`](02-setup-local.md)                                   |
| Nustatyti LLM tiekėją | [`providers.md`](providers.md)                                          |
| Susipažinti su kitais | [Prisijunkite prie mūsų Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Problemos ir sprendimai

| Simptomas                                 | Sprendimas                                                      |
|-------------------------------------------|-----------------------------------------------------------------|
| Konteinerio kūrimas užtruko > 10 min      | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminalas neprisijungė; spauskite **+** ➜ *bash*               |
| `401 Unauthorized` iš OpenAI              | Neteisingas / pasibaigęs `OPENAI_API_KEY`                       |
| VS Code rodo “Dev container mounting…”    | Perkraukite naršyklės kortelę—Codespaces kartais praranda ryšį  |
| Trūksta Notebook kernelio                 | Notebook meniu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix pagrindu veikiančios sistemos:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redaguokite `.env` failą**: Atidarykite `.env` failą tekstų redaktoriuje (pvz., VS Code, Notepad++ ar kitame). Pridėkite šią eilutę, pakeisdami `your_github_token_here` į savo tikrąjį GitHub raktą:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Išsaugokite failą**: Išsaugokite pakeitimus ir uždarykite redaktorių.

5. **Įdiekite `python-dotenv`**: Jei dar neturite, įdiekite `python-dotenv` paketą, kad galėtumėte įkelti aplinkos kintamuosius iš `.env` failo į savo Python programą. Įdiegti galite su `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Įkelkite aplinkos kintamuosius savo Python skripte**: Savo Python kode naudokite `python-dotenv` paketą, kad įkeltumėte kintamuosius iš `.env` failo:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Viskas! Sėkmingai sukūrėte `.env` failą, pridėjote savo GitHub raktą ir įkėlėte jį į Python programą.

## Kaip paleisti lokaliai savo kompiuteryje

Norėdami paleisti kodą savo kompiuteryje, turite turėti įdiegtą [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Norėdami naudoti repozitoriją, ją reikia nusiklonuoti:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kai viską atsisiųsite, galite pradėti!

## Papildomi žingsniai

### Miniconda diegimas

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) yra lengvas [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ir kelių paketų diegimo įrankis.
Pati Conda yra paketų tvarkyklė, kuri leidžia lengvai kurti ir keisti skirtingas Python [**virtualias aplinkas**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ir paketus. Ji taip pat naudinga diegiant paketus, kurių nėra per `pip`.

Galite vadovautis [MiniConda diegimo instrukcija](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), kad ją įdiegtumėte.

Kai Miniconda įdiegta, reikia nusiklonuoti [repozitoriją](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jei dar to nepadarėte).

Toliau reikia sukurti virtualią aplinką. Tai padaryti su Conda galite sukūrę naują aplinkos failą (_environment.yml_). Jei dirbate su Codespaces, sukurkite jį `.devcontainer` kataloge, t.y. `.devcontainer/environment.yml`.

Užpildykite savo aplinkos failą žemiau pateiktu fragmentu:

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

Jei naudojant conda kyla klaidų, Microsoft AI bibliotekas galite įdiegti rankiniu būdu šia komanda terminale.

```
conda install -c microsoft azure-ai-ml
```

Aplinkos faile nurodomos reikalingos priklausomybės. `<environment-name>` – tai jūsų norimos Conda aplinkos pavadinimas, o `<python-version>` – Python versija, pvz., `3` yra naujausia pagrindinė Python versija.

Atlikę šiuos veiksmus, galite sukurti Conda aplinką paleisdami šias komandas terminale:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Jei kyla problemų, žiūrėkite [Conda aplinkų vadovą](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code naudojimas su Python plėtiniu

Rekomenduojame naudoti [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) redaktorių su įdiegtu [Python plėtiniu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) šiame kurse. Tai tik rekomendacija, o ne būtinas reikalavimas.

> **Pastaba**: Atidarę kurso repozitoriją VS Code, galite pasirinkti projektą nustatyti konteineryje. Taip yra dėl [specialaus `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) katalogo kurso repozitorijoje. Apie tai daugiau vėliau.

> **Pastaba**: Kai nusiklonuosite ir atidarysite katalogą VS Code, jis automatiškai pasiūlys įdiegti Python plėtinį.

> **Pastaba**: Jei VS Code pasiūlys atidaryti repozitoriją konteineryje, atsisakykite šio pasiūlymo, kad naudotumėte lokaliai įdiegtą Python versiją.

### Jupyter naudojimas naršyklėje

Taip pat galite dirbti su projektu [Jupyter aplinkoje](https://jupyter.org?WT.mc_id=academic-105485-koreyst) tiesiai naršyklėje. Tiek klasikinis Jupyter, tiek [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) suteikia patogią kūrimo aplinką su tokiomis funkcijomis kaip automatinis užbaigimas, kodo paryškinimas ir pan.

Norėdami paleisti Jupyter lokaliai, atidarykite terminalą, nueikite į kurso katalogą ir vykdykite:

```bash
jupyter notebook
```

arba

```bash
jupyterhub
```

Tai paleis Jupyter ir komandinėje eilutėje parodys URL, kuriuo galėsite jį pasiekti.

Atsidarę tą URL, matysite kurso turinį ir galėsite naršyti po bet kurį `*.ipynb` failą. Pavyzdžiui, `08-building-search-applications/python/oai-solution.ipynb`.

### Paleidimas konteineryje

Alternatyva viską diegti savo kompiuteryje ar Codespace – naudoti [konteinerį](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specialus `.devcontainer` aplankas kurso repozitorijoje leidžia VS Code nustatyti projektą konteineryje. Už Codespaces ribų tam reikės įdiegti Docker, ir tai reikalauja daugiau darbo, todėl šį būdą rekomenduojame tik turintiems patirties su konteineriais.

Vienas geriausių būdų saugoti savo API raktus naudojant GitHub Codespaces – naudoti Codespace Secrets. Daugiau apie tai rasite [Codespaces slaptų duomenų valdymo gide](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Pamokos ir techniniai reikalavimai

Kursą sudaro 6 teorinės ir 6 programavimo pamokos.

Programavimo pamokose naudojame Azure OpenAI Service. Norėdami paleisti šį kodą, turėsite turėti prieigą prie Azure OpenAI paslaugos ir API raktą. Prieigą galite gauti [užpildę šią paraišką](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kol laukiate, kol jūsų paraiška bus patvirtinta, kiekvienoje programavimo pamokoje taip pat yra `README.md` failas, kuriame galite peržiūrėti kodą ir rezultatus.

## Pirmą kartą naudojant Azure OpenAI Service

Jei pirmą kartą dirbate su Azure OpenAI paslauga, sekite šį gidą, kaip [sukurti ir diegti Azure OpenAI Service resursą.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Pirmą kartą naudojant OpenAI API

Jei pirmą kartą dirbate su OpenAI API, sekite gidą, kaip [sukurti ir naudoti sąsają.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Susipažinkite su kitais mokiniais

Oficialiame [AI Community Discord serveryje](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) sukūrėme kanalus susipažinti su kitais mokiniais. Tai puiki proga užmegzti ryšius su kitais panašiai mąstančiais kūrėjais, studentais ar visais, norinčiais tobulėti generatyviojo DI srityje.

[![Prisijunkite prie Discord kanalo](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projekto komanda taip pat bus šiame Discord serveryje ir padės mokiniams.

## Prisidėkite

Šis kursas yra atviro kodo iniciatyva. Jei matote, ką galima patobulinti ar pastebite klaidų, sukurkite [Pull Request’ą](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) arba praneškite apie [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projekto komanda stebės visus indėlius. Prisidėjimas prie atviro kodo yra puikus būdas kurti karjerą generatyviojo DI srityje.

Daugumai indėlių reikės sutikti su Contributor License Agreement (CLA), kuriame patvirtinate, kad turite teisę ir iš tikrųjų suteikiate mums teisę naudoti jūsų indėlį. Daugiau informacijos rasite [CLA, Contributor License Agreement svetainėje](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Svarbu: verčiant tekstą šiame repozitorijoje, nenaudokite automatinio vertimo. Vertimus tikrins bendruomenė, tad savanoriaukite tik toms kalboms, kurias tikrai mokate.

Kai pateiksite pull request’ą, CLA-bot automatiškai nustatys, ar reikia pateikti CLA, ir atitinkamai pažymės PR (pvz., etikete, komentaru). Tiesiog sekite boto nurodymus. Tai reikės padaryti tik vieną kartą visiems mūsų CLA naudojantiems repozitorijams.

Šis projektas laikosi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Daugiau informacijos rasite Code of Conduct DUK arba rašykite [Email opencode](opencode@microsoft.com), jei turite klausimų ar pastabų.

## Pradėkime!
Dabar, kai jau atlikote visus reikiamus šio kurso žingsnius, pradėkime nuo [įvado į generatyvųjį dirbtinį intelektą ir didelius kalbos modelius (LLM)](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.