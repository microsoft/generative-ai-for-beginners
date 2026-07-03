# Pradžia su šiuo kursu

Mes labai džiaugiamės, kad pradedate šį kursą ir pamatysite, ką įkvėpti kuriate su Generatyviąja AI!

Norėdami užtikrinti jūsų sėkmę, šiame puslapyje aprašyti nustatymo žingsniai, techniniai reikalavimai ir kur gauti pagalbą, jei reikės.

## Nustatymo žingsniai

Norėdami pradėti šį kursą, turėsite atlikti šiuos veiksmus.

### 1. Atšakokite šį repozitoriją

[Atšakokite visą šį repozitoriją](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) į savo GitHub paskyrą, kad galėtumėte keisti bet kokį kodą ir įveikti iššūkius. Taip pat galite [pažymėti (🌟) šią repozitoriją](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), kad ją ir susijusias repozitorijas rastumėte lengviau.

### 2. Sukurkite codespace

Kad išvengtumėte priklausomybių problemų vykdant kodą, rekomenduojame šį kursą vykdyti [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Savo atšakoje: **Code -> Codespaces -> New on main**

![Dialogas su mygtukais sukurti codespace](../../../translated_images/lt/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Pridėkite slaptažodį (secret)

1. ⚙️ Pavaros piktograma -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Pavadinkite OPENAI_API_KEY, įklijuokite savo raktą, Išsaugokite.

### 3. Kas toliau?

| Noriu…              | Eiti į…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Pradėti 1 pamoką    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Dirbti neprisijungus | [`setup-local.md`](02-setup-local.md)                                   |
| Nustatyti LLM teikėją | [`providers.md`](03-providers.md)                                        |
| Susipažinti su kitais besimokančiais | [Prisijunkite prie mūsų Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Trikčių šalinimas

| Simptomas                                    | Sprendimas                                                    |
|----------------------------------------------|--------------------------------------------------------------|
| Kūrimo konteineris stringa > 10 min           | **Codespaces ➜ „Rebuild Container“**                         |
| `python: command not found`                    | Terminalas neprisijungė; spustelėkite **+** ➜ *bash*         |
| `401 Unauthorized` iš OpenAI                   | Neteisingas / pasibaigęs `OPENAI_API_KEY`                    |
| VS Code rodo „Dev container mounting…“        | Atšviežinkite naršyklės skirtuką – Codespaces kartais praranda ryšį   |
| Notebook branduolys dingęs                    | Notebook meniu ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   Unix pagrindu veikiantys sistemos:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redaguokite `.env` Failą**: Atidarykite `.env` failą teksto redaktoriuje (pvz., VS Code, Notepad++ arba bet kuriame kitame redaktoriuje). Pridėkite šią eilutę, pakeisdami `your_github_token_here` savo tikru GitHub raktu:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Išsaugokite failą**: Išsaugokite pakeitimus ir uždarykite teksto redaktorių.

5. **Įdiekite `python-dotenv`**: Jei dar neturite, turėsite įdiegti `python-dotenv` paketą, kad įkeltumėte aplinkos kintamuosius iš `.env` failo į savo Python programą. Galite įdiegti naudodami `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Įkelkite aplinkos kintamuosius savo Python skripte**: Savo Python skripte naudokite `python-dotenv` paketą, kad įkeltumėte aplinkos kintamuosius iš `.env` failo:

   ```python
   from dotenv import load_dotenv
   import os

   # Įkelkite aplinkos kintamuosius iš .env failo
   load_dotenv()

   # Gaukite prieigą prie GITHUB_TOKEN kintamojo
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Štai ir viskas! Jūs sėkmingai sukūrėte `.env` failą, pridėjote savo GitHub raktą ir jį įkrovėte į savo Python programą.

## Kaip vykdyti lokaliai savo kompiuteryje

Norėdami vykdyti kodą lokaliai savo kompiuteryje, turite turėti įdiegtą tam tikrą [Python versiją](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Tada norėdami naudoti repozitoriją, turite ją klonuoti:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kai viskas bus paruošta, galite pradėti darbą!

## Pasirenkami veiksmai

### Miniconda įdiegimas

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) yra lengva įdiegimo priemonė, skirta įdiegti [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python bei keletą paketų.
Conda yra paketų tvarkyklė, kuri palengvina skirtingų Python [**virtualių aplinkų**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ir paketų nustatymą bei perjungimą. Ji taip pat naudinga įdiegiant paketus, kurių nėra prieinami per `pip`.

Galite sekti [MiniConda įdiegimo gidą](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Įsidiegus Miniconda, turite klonuoti [repozitoriją](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jei dar nepadarėte)

Tada turite sukurti virtualią aplinką. Norėdami tai padaryti su Conda, sukurkite naują aplinkos failą (_environment.yml_). Jei sekate kurso eigą naudodami Codespaces, sukurkite jį `.devcontainer` kataloge, t.y. `.devcontainer/environment.yml`.

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

Jei gaunate klaidų naudodami conda, galite rankiniu būdu įdiegti Microsoft AI bibliotakas naudodami šią komandą terminale.

```
conda install -c microsoft azure-ai-ml
```

Aplinkos faile nurodytos priklausomybės, kurių reikia. `<environment-name>` yra vardas, kurį norite naudoti savo Conda aplinkai, o `<python-version>` – tai Python versija, kurios norite, pavyzdžiui, `3` yra naujausia pagrindinė Python versija.

Pasibaigus, galite sukurti savo Conda aplinką paleisdami žemiau pateiktas komandas savo komandinėje eilutėje/terminale

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer subtakas taikomas tik Codespace nustatymams
conda activate ai4beg
```

Jei kyla problemų, žr. [Conda aplinkų gido](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code naudojimas su Python palaikymo įskiepiu

Rekomenduojame naudoti [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) redaktorių su įdiegtu [Python palaikymo įskiepiu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) šiam kursui. Tačiau tai labiau rekomendacija, o ne privaloma sąlyga.

> **Pastaba**: Atidarius kurso repozitoriją VS Code, turite galimybę nustatyti projektą konteineryje. Tai įmanoma dėl [specialaus `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) katalogo, esančio kurso repozitorijoje. Apie tai vėliau.

> **Pastaba**: Kai klonuosite ir atidarysite katalogą VS Code, jis automatiškai pasiūlys įdiegti Python palaikymo įskiepį.

> **Pastaba**: Jei VS Code siūlo atidaryti repozitoriją konteineryje, atminkite šį prašymą, jei norite naudoti lokaliai įdiegtą Python versiją.

### Jupyter naudojimas naršyklėje

Taip pat galite dirbti projekte naudodami [Jupyter aplinką](https://jupyter.org?WT.mc_id=academic-105485-koreyst) tiesiog savo naršyklėje. Tiek klasikinis Jupyter, tiek [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) siūlo patogią kūrimo aplinką su funkcijomis kaip automatinis pildymas, kodo išryškinimas ir t.t.

Norėdami paleisti Jupyter lokaliai, atverkite terminalą/komandinę eilutę, eikite į kurso katalogą ir vykdykite:

```bash
jupyter notebook
```

arba

```bash
jupyterhub
```

Tai paleis Jupyter instanciją ir URL, kurį galite pasiekti, bus parodytas komandinės eilutės lange.

Patekę į URL turėtumėte matyti kurso struktūrą ir galėsite naršyti bet kurį `*.ipynb` failą, pvz., `08-building-search-applications/python/oai-solution.ipynb`.

### Vykdymas konteineryje

Alternatyva nustatyti viską savo kompiuteryje ar Codespace yra naudoti [konteinerį](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specialus `.devcontainer` aplankas kurso repozitorijoje leidžia VS Code nustatyti projektą konteineryje. Ne Codespaces aplinkoje tai reikalauja Docker diegimo ir iš tiesų yra šiek tiek sudėtinga, todėl rekomenduojame tai tik patyrusiems konteinerių naudotojams.

Vienas geriausių būdų saugiai laikyti savo API raktus naudojant GitHub Codespaces yra naudoti Codespace Secrets. Prašome sekti [Codespaces slaptažodžių valdymo](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) gido nurodymus.

## Pamokos ir techniniai reikalavimai

Kursą sudaro 6 koncepcinės pamokos ir 6 programavimo pamokos.

Programavimo pamokoms naudojame Azure OpenAI paslaugą. Norėdami vykdyti šį kodą, jums reikės prieigos prie Azure OpenAI paslaugos ir API rakto. Prieigą galite gauti [užpildę šią paraišką](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Kol laukiate savo paraiškos apdorojimo, kiekvienoje programavimo pamokoje yra `README.md` failas, kuriame galite peržiūrėti kodą ir rezultatus.

## Azure OpenAI paslaugos naudojimas pirmą kartą

Jei pirmą kartą dirbate su Azure OpenAI paslauga, prašome sekti šį gidą, kaip [sukurti ir diegti Azure OpenAI paslaugos resursą.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API naudojimas pirmą kartą

Jei pirmą kartą dirbate su OpenAI API, prašome sekti gidą, kaip [sukurti ir naudoti sąsają.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Susipažinkite su kitais besimokančiais

Mes sukūrėme kanalus oficialiame mūsų [AI bendruomenės Discord serveryje](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), kad galėtumėte susipažinti su kitais besimokančiais. Tai puikus būdas užmegzti ryšius su panašiai mąstančiais verslininkais, kūrėjais, studentais ir visais, kurie nori žengti į priekį Generatyvios AI srityje.

[![Prisijunk prie discord kanalo](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projekto komanda taip pat bus šiame Discord serveryje, kad padėtų besimokančiesiems.

## Prisidėkite

Šis kursas yra atviro kodo iniciatyva. Jei matote tobulinimo galimybių ar klaidų, prašome sukurti [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) arba užregistruoti [GitHub problemą](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projekto komanda stebės visas indėlius. Prisidėjimas prie atviro kodo yra nuostabus būdas kurti savo karjerą Generatyvioje AI srityje.

Daugeliui indėlių reikės sutikti su Bendradarbio licencijos sutartimi (CLA), kurioje deklaruojama, kad turite teisę ir tikrai suteikiate mums teisę naudoti jūsų indėlį. Daugiau informacijos rasite [CLA, bendradarbio licencijos sutarties svetainėje](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Svarbu: verčiant tekstą šiame repozitorijoje, prašome nenaudoti mašininio vertimo. Mes tikrinsime vertimus bendruomenės pagalba, tad savanoriškai prisijunkite tik prie tų kalbų vertimų, kuriomis tikrai mokate.

Pateikus pull request, CLA-botas automatiškai nustatys, ar jums reikia pateikti CLA ir pažymės PR atitinkamai (pvz., žyma, komentaras). Viskas, ką jums reikės padaryti – sekti roboto pateiktas instrukcijas. Tai reikės padaryti tik vieną kartą visuose repozitorijuose, naudojančiuose mūsų CLA.

Šis projektas priėmė [Microsoft Atvirojo kodo elgesio kodeksą](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Daugiau informacijos skaitykite Elgesio kodekso DUK arba susisiekite su [Elgesio kodekso el. paštu](opencode@microsoft.com) dėl papildomų klausimų ar pastabų.

## Pradėkime!
Dabar, kai atlikote reikalingus veiksmus šiam kursui užbaigti, pradėkime nuo [įvado į generatyviąją DI ir didelius kalbos modelius (LLM)](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Pirminis dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogiškas vertimas. Neatsakome už bet kokius nesusipratimus ar neteisingą aiškinimą, kylančius naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->