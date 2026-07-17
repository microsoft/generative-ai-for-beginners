# Pradžia su šiuo kursu

Labai džiaugiamės, kad pradedate šį kursą ir pamatysite, ką įkvėpti sukurti naudojant Generatyvų AI!

Norėdami užtikrinti jūsų sėkmę, šiame puslapyje aprašyti nustatymo žingsniai, techniniai reikalavimai ir kur kreiptis pagalbos, jei prireiks.

## Nustatymo žingsniai

Norėdami pradėti šį kursą, turėsite atlikti šiuos veiksmus.

### 1. Sukurkite šio repozitorijos šaką (fork)

[Sukurkite šio repozitorijos šaką](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) į savo GitHub paskyrą, kad galėtumėte keisti bet kurį kodą ir atlikti iššūkius. Taip pat galite [pažymėti (🌟) šį repozitoriją](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), kad ją ir susijusius repozitorijus būtų lengviau rasti.

### 2. Sukurkite codespace

Norėdami išvengti priklausomybių problemų vykdant kodą, rekomenduojame šį kursą vykdyti [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Savo šakoje: **Code -> Codespaces -> New on main**

![Dialogas, rodantis mygtukus codespace kūrimui](../../../translated_images/lt/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Pridėkite slaptą informaciją

1. ⚙️ Pavaros piktograma -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Pavadinkite OPENAI_API_KEY, įklijuokite savo raktą, išsaugokite.

### 3. Kas toliau?

| Noriu…                | Eiti į…                                                               |
|-----------------------|---------------------------------------------------------------------|
| Pradėti 1 pamoką      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| Dirbti neprisijungus  | [`setup-local.md`](02-setup-local.md)                               |
| Nustatyti LLM tiekėją | [`providers.md`](03-providers.md)                                    |
| Susipažinti su kitais mokiniais | [Prisijunkite prie mūsų Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Trikčių šalinimas


| Simptomai                                | Sprendimas                                                      |
|-----------------------------------------|----------------------------------------------------------------|
| Konteinerio kūrimas užstringa > 10 min | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`             | Terminalas neprisijungė; spauskite **+** ➜ *bash*             |
| `401 Unauthorized` iš OpenAI             | Klaidingas / pasibaigęs `OPENAI_API_KEY`                       |
| VS Code rodo „Dev container mounting…”  | Atnaujinkite naršyklės skirtuką — Codespaces kartais praranda ryšį |
| Trūksta užrašų knygos (notebook) šerdies| Užrašų knygos meniu ➜ **Kernel ▸ Select Kernel ▸ Python 3**     |

   Unix pagrindu veikiančios sistemos:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redaguokite `.env` Failą**: Atidarykite `.env` failą teksto redaktoriuje (pvz., VS Code, Notepad++ arba kitame redaktoriuje). Įtraukite šias eilutes į failą, pakeisdami vietas laikiklius savo tikru Microsoft Foundry Models pabaigos tašku ir raktu (žr. [`providers.md`](03-providers.md) kaip gauti šiuos duomenis):

   > **Pastaba:** GitHub Models (ir jo `GITHUB_TOKEN` kintamasis) bus nutrauktas 2026 m. liepos pabaigoje. Vietoj jo naudokite [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Išsaugokite Failą**: Išsaugokite pakeitimus ir uždarykite teksto redaktorių.

5. **Įdiekite `python-dotenv`**: Jei dar neįdiegėte, turėsite įdiegti `python-dotenv` paketą, kad įkeltumėte aplinkos kintamuosius iš `.env` failo į savo Python programą. Įdiegti galite naudodami `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Įkelkite Aplinkos Kintamuosius į savo Python Skriptą**: Naudokite `python-dotenv` paketą savo Python skripte įkelti aplinkos kintamuosius iš `.env` failo:

   ```python
   from dotenv import load_dotenv
   import os

   # Įkelti aplinkos kintamuosius iš .env failo
   load_dotenv()

   # Pasiekti Microsoft Foundry Models kintamuosius
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Štai ir viskas! Jūs sėkmingai sukūrėte `.env` failą, pridėjote savo Microsoft Foundry Models kredencialus ir įkėlėte juos į Python programą.

## Kaip paleisti vietoje savo kompiuteryje

Norėdami paleisti kodą savo kompiuteryje, turite turėti įdiegtą tam tikrą [Python versiją](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Norėdami naudoti repozitoriją, turite ją klonuoti:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kai viską pasirinksite, galite pradėti!

## Papildomi žingsniai

### Miniconda diegimas

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) yra lengvas diegimo įrankis, skirtas diegti [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ir keletą paketų.
Conda yra paketų tvarkyklė, kuri palengvina skirtingų Python [**virtualių aplinkų**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ir paketų nustatymą bei perjungimą. Ji taip pat praverčia diegiant paketus, kurių nėra `pip`.

Galite sekti [MiniConda diegimo vadovą](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), kad ją nustatytumėte.

Įdiegę Miniconda, turite klonuoti [repozitoriją](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jei dar to nepadarėte)

Tada reikia sukurti virtualią aplinką. Norėdami tai padaryti su Conda, sukurkite naują aplinkos failą (_environment.yml_). Jei naudojate Codespaces, sukurkite jį `.devcontainer` kataloge, taigi `.devcontainer/environment.yml`.

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

Jei gaunate klaidų naudojant conda, galite rankiniu būdu įdiegti Microsoft AI bibliotekas naudodami šią komandą terminale.

```
conda install -c microsoft azure-ai-ml
```

Aplinkos faile nurodomos reikia priklausomybės. `<environment-name>` yra vardas, kurį norite suteikti savo Conda aplinkai, o `<python-version>` yra Python versija, kurią norite naudoti, pavyzdžiui, `3` yra naujausia pagrindinė Python versija.

Baigę galite sukurti savo Conda aplinką vykdydami šias komandas komandinėje eilutėje/terminale:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer poskelis taikomas tik Codespace nustatymams
conda activate ai4beg
```

Jei susiduriate su problemomis, žiūrėkite [Conda aplinkų vadovą](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Naudojant Visual Studio Code su Python palaikymo plėtiniu

Rekomenduojame naudoti [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) redaktorių su įdiegtu [Python palaikymo plėtiniu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) šiam kursui. Tai vis dėlto tik rekomendacija, ne griežtas reikalavimas.

> **Pastaba**: Atidarydami kurso repozitoriją VS Code, galite nustatyti projektą konteineryje. Tai įmanoma dėl specialaus `.devcontainer` katalogo kurso repozitorijoje. Apie tai vėliau.

> **Pastaba**: Kai klonuojate ir atidarote katalogą VS Code, automatiškai siūloma įdiegti Python palaikymo plėtinį.

> **Pastaba**: Jei VS Code siūlo atidaryti repozitoriją konteineryje, atsisakykite šio pasiūlymo, kad naudotumėte vietinę Python versiją.

### Naudojant Jupyter naršyklėje

Taip pat galite dirbti su projektu naudodami [Jupyter aplinką](https://jupyter.org?WT.mc_id=academic-105485-koreyst) tiesiogiai naršyklėje. Tiek klasikinis Jupyter, tiek [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) siūlo patogią kūrimo aplinką su automatinio užbaigimo, kodo paryškinimo ir kitomis funkcijomis.

Norėdami paleisti Jupyter vietoje, eikite į terminalą/komandinę eilutę, perkelkite į kurso katalogą ir vykdykite:

```bash
jupyter notebook
```

arba

```bash
jupyterhub
```

Tai paleis Jupyter egzempliorių, o prieigos URL bus rodomas komandinės eilutės lange.

Pasiekę URL, turėtumėte matyti kurso apžvalgą ir galėti naršyti į bet kurį `*.ipynb` failą. Pavyzdžiui, `08-building-search-applications/python/oai-solution.ipynb`.

### Vykdymas konteineryje

Alternatyva viską nustatyti savo kompiuteryje arba Codespace yra naudoti [konteinerį](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specialus `.devcontainer` katalogas kurso repozitorijoje leidžia VS Code sukurti projektą konteineryje. Už Codespaces ribų tai reikalauja Docker diegimo ir šiek tiek darbo, todėl rekomenduojame tai daryti tik tiems, kurie turi patirties su konteineriais.

Vienas geriausių būdų apsaugoti API raktus naudojant GitHub Codespaces yra naudoti Codespace Secrets. Prašome sekti [Codespaces slaptumo valdymo](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) vadovą, kad sužinotumėte daugiau.


## Pamokos ir techniniai reikalavimai

Kursas turi „Mokymosi“ pamokas, kurios paaiškina Generatyvaus AI sąvokas, ir „Kūrimo“ pamokas su praktiniais pavyzdžiais tiek **Python**, tiek **TypeScript**, kur įmanoma.

Kodavimo pamokoms naudojame Azure OpenAI Microsoft Foundry. Reikės Azure prenumeratos ir API rakto. Prieiga yra atvira – nereikia prašymo – tad galite [sukurti Microsoft Foundry išteklių ir įdiegti modelį](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst), kad gautumėte savo pabaigos tašką ir raktą.

Kiekviena kodavimo pamoka taip pat turi `README.md` failą, kuriame galite peržiūrėti kodą ir rezultatus be jokio vykdymo.

## Pirmą kartą naudojant Azure OpenAI paslaugą

Jei šį kartą pirmą kartą dirbate su Azure OpenAI paslauga, prašome sekti šį vadovą, kaip [sukurti ir įdiegti Azure OpenAI paslaugos išteklių.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Pirmą kartą naudojant OpenAI API

Jei šį kartą pirmą kartą dirbate su OpenAI API, prašome sekti vadovą, kaip [sukurti ir naudoti sąsają.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Susipažinkite su kitais mokiniais

Sukūrėme kanalus mūsų oficialiame [AI bendruomenės Discord serveryje](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), skirtus susitikti su kitais mokiniais. Tai puikus būdas megzti ryšius su panašių interesų verslininkais, kūrėjais, studentais ir visais, siekiančiais tobulėti generatyviame AI.

[![Prisijunkite prie discord kanalo](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projekto komanda taip pat bus šiame Discord serveryje, kad padėtų mokiniams.

## Prisidėkite

Šis kursas yra atviro kodo iniciatyva. Jei pastebėsite tobulinimo galimybių ar problemų, prašome sukurti [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) arba užregistruoti [GitHub problemą](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projekto komanda stebės visas indėles. Prisidėjimas prie atviro kodo yra puikus būdas kurti karjerą Generatyviame AI.

Daugumai indėlių būtina sutikti su Bendradarbio Licencijos Sutartimi (CLA), kurioje deklaruojate, kad turite teisę ir iš tikrųjų suteikiate mums teises naudoti jūsų indėlį. Daugiau informacijos žr. [CLA, Bendradarbio Licencijos Sutarties svetainę](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Svarbu: verčiant tekstus šiame repozitorijoje, prašome nenaudoti mašininio vertimo. Vertimus patikrins bendruomenė, tad siūlykite versti tik į kalbas, kuriose mokate puikiai.


Kai pateikiate pull request, CLA-botas automatiškai nustatys, ar jums reikia pateikti CLA, ir tinkamai pažymės PR (pvz., etikete, komentaru). Tiesiog sekite botui pateiktas instrukcijas. Tai reikės padaryti tik vieną kartą visuose saugyklose, naudojančiose mūsų CLA.

Šis projektas priėmė [Microsoft atvirojo kodo elgesio taisykles](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Daugiau informacijos galite rasti elgesio taisyklių DUK arba susisiekite el. paštu [Email opencode](opencode@microsoft.com) dėl papildomų klausimų ar pastabų.

## Pradėkime

Kadangi jau atlikote reikalingus veiksmus šiam kursui, pradėkime nuo [įvado į generatyviąją DI ir LLM](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->