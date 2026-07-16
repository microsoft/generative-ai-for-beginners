# Kursų pradžia

Labai džiaugiamės, kad pradedate šį kursą ir pamatysite, ką jus įkvėps kurti su Generatyviąja AI!

Norėdami užtikrinti jūsų sėkmę, šiame puslapyje aprašomi nustatymo veiksmai, techniniai reikalavimai ir kur kreiptis pagalbos, jei reikia.

## Nustatymo veiksmai

Norėdami pradėti šį kursą, turite atlikti šiuos veiksmus.

### 1. Padarykite šios saugyklos šaką (fork)

[Padarykite šaką visai šiai saugyklai](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) savo GitHub paskyroje, kad galėtumėte keisti bet kokį kodą ir įvykdyti užduotis. Taip pat galite [uždėti žvaigždutę (🌟) šiai saugyklai](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), kad ją ir susijusias saugyklas rastumėte lengviau.

### 2. Sukurkite codespace aplinką

Kad išvengtumėte priklausomybių problemų vykdydami kodą, rekomenduojame naudoti šį kursą [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Jūsų šakoje: **Code -> Codespaces -> New on main**

![Dialogas, rodantis mygtukus codespace kūrimui](../../../translated_images/lt/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Pridėkite slaptą raktą

1. ⚙️ Pavaros piktograma -> Komandų paletė -> Codespaces : Valdyti naudotojo slaptą raktą -> Pridėti naują slaptą raktą.
2. Pavadinkite OPENAI_API_KEY, įklijuokite savo raktą, išsaugokite.

### 3. Kas toliau?

| Noriu…             | Eiti į…                                                               |
|---------------------|-----------------------------------------------------------------------|
| Pradėti 1-ąją pamoką | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Dirbti neprisijungus | [`setup-local.md`](02-setup-local.md)                                 |
| Nustatyti LLM tiekėją | [`providers.md`](03-providers.md)                                      |
| Susipažinti su kitais mokiniais | [Prisijunkite prie mūsų Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Gedimų šalinimas


| Simptomas                                    | Sprendimas                                                      |
|---------------------------------------------|----------------------------------------------------------------|
| Konstravimo talpyklos trunka > 10 minučių   | **Codespaces ➜ „Rebuild Container“**                          |
| `python: command not found`                   | Terminalas neprisijungė; spustelėkite **+** ➜ *bash*           |
| `401 Unauthorized` iš OpenAI                  | Netinkamas / pasibaigęs `OPENAI_API_KEY`                        |
| VS Code rodo „Dev container mounting…“       | Atnaujinkite naršyklės skirtuką—Codespaces kartais praranda ryšį |
| Trūksta užrašų knygutės branduolio          | Užrašų knygutės meniu ➜ **Kernel ▸ Select Kernel ▸ Python 3**   |

   Unix pagrindu veikiančios sistemos:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redaguokite `.env` failiuką**: Atidarykite `.env` failą teksto redaktoriuje (pvz., VS Code, Notepad++ ar bet kuriame kitame redaktoriuje). Pridėkite šias eilutes, pakeisdami vietas savo tikru Microsoft Foundry Models galiniu tašku ir raktu (žr. [`providers.md`](03-providers.md), kaip tai gauti):

   > **Pastaba:** GitHub Modeliai (su `GITHUB_TOKEN` kintamuoju) pasitrauks 2026 m. liepos pabaigoje. Naudokite [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Išsaugokite failą**: Išsaugokite pakeitimus ir uždarykite teksto redaktorių.

5. **Įdiekite `python-dotenv`**: Jei dar to nepadarėte, reikės įdiegti `python-dotenv` paketą, kad aplinkos kintamieji iš `.env` failo būtų įkelti į jūsų Python programą. Tai galite padaryti naudodami `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Įkelkite aplinkos kintamuosius į savo Python skriptą**: Naudokite `python-dotenv` paketą savo Python skripte, kad įkeltumėte aplinkos kintamuosius iš `.env` failo:

   ```python
   from dotenv import load_dotenv
   import os

   # Įkelti aplinkos kintamuosius iš .env failo
   load_dotenv()

   # Prieiti prie Microsoft Foundry modelių kintamųjų
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Viskas! Jūs sukūrėte `.env` failą, pridėjote savo Microsoft Foundry Models kredencialus ir įkėlėte juos į Python programą.

## Kaip paleisti lokaliai savo kompiuteryje

Norėdami paleisti kodą lokaliai savo kompiuteryje, turite turėti įdiegtą [Python versiją](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Tada naudodami repozitoriją turite ją nuklonuoti:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Kai viskas paruošta, galite pradėti!

## Pasirenkami žingsniai

### Miniconda įdiegimas

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) yra lengvas įdiegėjas skirta įdiegti [Condą](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ir keletą paketų.
Conda yra paketų tvarkyklė, leidžianti lengvai kurti ir keisti skirtingas Python [**virtualias aplinkas**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ir paketus. Taip pat ji naudinga diegiant paketus, kurių nėra `pip`.

Galite sekti [MiniConda diegimo gidą](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Įdiegus Miniconda, reikia nuklonuoti [repozitoriją](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (jei dar to nepadarėte)

Tada sukurkite virtualią aplinką. Su Conda tai padarysite sukurdami naują aplinkos failą (_environment.yml_). Jei naudojatės Codespaces, sukurkite jį `.devcontainer` kataloge, taigi `.devcontainer/environment.yml`.

Užpildykite aplinkos failą pateiktu fragmentu:

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

Jei gaunate klaidų naudodami conda, galite rankiniu būdu įdiegti Microsoft AI bibliotekas vykdydami šią komandą terminale.

```
conda install -c microsoft azure-ai-ml
```

Aplinkos faile nurodomos reikalingos priklausomybės. `<environment-name>` yra Conda aplinkos pavadinimas, o `<python-version>` - Python versija, pavyzdžiui, `3` - naujausia pagrindinė versija.

Baigus, sukurkite Conda aplinką paleisdami žemiau pateiktas komandas komandinėje eilutėje/terminale

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer poskelis taikomas tik Codespace sąrankoms
conda activate ai4beg
```

Prireikus pagalbos žiūrėkite [Conda aplinkų gidą](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Naudojant Visual Studio Code su Python palaikymo priedu

Šiam kursui rekomenduojame naudoti [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) redaktorių su įdiegtu [Python palaikymo priedu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Tačiau tai tik rekomendacija, o ne privalomas reikalavimas.

> **Pastaba**: Atidarius šio kurso saugyklą VS Code, turite galimybę nustatyti projektą konteineryje. Tai įmanoma dėka specialaus `.devcontainer` katalogo esant savyje kurso saugykloje. Apie tai sužinosite vėliau.

> **Pastaba**: Nuklonavus ir atidarius katalogą VS Code automatiškai pasiūlys įdiegti Python palaikymo priedą.

> **Pastaba**: Jei VS Code siūlo iš naujo atidaryti saugyklą konteineryje, atminkite šį kvietimą, jei norite naudoti jūsų kompiuteryje įdiegtą Python.

### Naudojant Jupyter naršyklėje

Taip pat galite dirbti su projektu naudodami [Jupyter aplinką](https://jupyter.org?WT.mc_id=academic-105485-koreyst) tiesiai naršyklėje. Tiek klasikinis Jupyter, tiek [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) suteikia malonią plėtros aplinką su funkcijomis, tokiomis kaip automatinis užpildymas, kodo paryškinimas ir kt.

Norėdami paleisti Jupyter lokaliai, eikite į terminalą/komandinę eilutę, nueikite į kurso katalogą ir paleiskite:

```bash
jupyter notebook
```

arba

```bash
jupyterhub
```

Tai paleis Jupyter egzempliorių, kurio prieigos URL bus parodytas komandinės eilutės lange.

Atidarius URL, turėtumėte matyti kurso planą ir galėti naviguoti į bet kurį `*.ipynb` failą. Pavyzdžiui, `08-building-search-applications/python/oai-solution.ipynb`.

### Paleidimas konteineryje

Alternatyva viską dėlioti savo kompiuteryje ar Codespace yra naudoti [konteinerį](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Specialus `.devcontainer` katalogas kurso saugykloje leidžia VS Code nustatyti projektą konteineryje. Ne Codespaces atveju reikės įdiegti Docker. Tai gana sudėtinga, tad rekomenduojame tai tiems, kurie turi patirties dirbant su konteineriais.

Vienas geriausių būdų apsaugoti savo API raktus naudojant GitHub Codespaces yra naudoti Codespace Secrets. Prašome susipažinti su vadovu apie [Codespaces slaptų raktų valdymą](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).


## Pamokos ir techniniai reikalavimai

Kursą sudaro 6 koncepcinės pamokos ir 6 programavimo pamokos.

Programavimo pamokoms naudojame Azure OpenAI paslaugą. Jums reikės prieigos prie Azure OpenAI paslaugos ir API rakto, norint vykdyti šį kodą. Galite kreiptis dėl prieigos užpildę [šią paraišką](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Laukdami paraiškos patvirtinimo, kiekvienoje programavimo pamokoje rasite `README.md` failą, kuriame galite peržiūrėti kodą ir rezultatus.

## Naudojantis Azure OpenAI paslauga pirmą kartą

Jei tai jūsų pirmas kartas dirbant su Azure OpenAI paslauga, prašome vadovautis šia instrukcija, kaip [sukurti ir diegti Azure OpenAI išteklį](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## Naudojantis OpenAI API pirmą kartą

Jei tai jūsų pirmas kartas dirbant su OpenAI API, skaitykite [gairę, kaip sukurti ir naudoti sąsają](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst).

## Susipažinkite su kitais mokiniais

Mes sukūrėme kanalus mūsų oficialiame [AI bendruomenės Discord serveryje](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst), skirtus susipažinti su kitais mokiniais. Tai puikus būdas susitikti su panašaus mąstymo verslininkais, kūrėjais, studentais ir visais, siekiančiais tobulėti Generatyviojoje AI srityje.

[![Prisijunkite prie discord kanalo](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projekto komanda taip pat bus šiame Discord serveryje, kad padėtų mokiniams.

## Prisidėkite

Šis kursas yra atvirojo kodo iniciatyva. Jei matote, kur galima patobulinti ar radote problemų, prašome sukurti [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) arba užregistruoti [GitHub klaidą](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projekto komanda stebės visus indėlius. Prisidėjimas prie atvirojo kodo yra puikus būdas kurti savo karjerą Generatyvios AI srityje.

Daugeliu atvejų prisidėjimas reikalauja sutikti su Kontributoriaus licencijos sutartimi (CLA), kurioje patvirtinate, kad turite teisę ir iš tikrųjų suteikiate teisę naudoti jūsų indėlį. Daugiau informacijos rasite [CLA, Kontributoriaus licencijos sutarties svetainėje](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Svarbu: Vertinant šiame repozitorijoje pateiktus vertimus, prašome nenaudoti mašininio vertimo. Mes patikrinsime vertimus per bendruomenę, tad prašome savanoriauti tik tomis kalbomis, kuriomis iš tiesų gerai mokate.

Pateikus pull requestą, CLA roboto veiksmas automatiškai nustatys, ar jums reikia pateikti CLA ir tinkamai pažymės PR (pvz., etikete, komentaru). Tiesiog sekite roboto pateiktas instrukcijas. Tai darysite tik vieną kartą visuose repozitorijuose, naudojančiuose mūsų CLA.


Šis projektas priėmė [„Microsoft Open Source elgesio kodeksą“](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Daugiau informacijos rasite elgesio kodekso DUK arba susisiekite su [El. paštu opencode](opencode@microsoft.com) dėl papildomų klausimų ar komentarų.

## Pradėkime

Dabar, kai atlikote reikalingus žingsnius šiam kursui baigti, pradėkime nuo [generatyviosios DI ir LLM pagrindų įvado](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->