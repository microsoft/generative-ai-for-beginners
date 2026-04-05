# Lokalna namestitev 🖥️

**Uporabite ta vodič, če želite vse poganjati na svojem prenosniku.**  
Imate dve poti: **(A) izvorni Python + virtualno okolje** ali **(B) VS Code Dev Container z Dockerjem**.  
Izberite tisto, ki vam je lažja – obe vodita do istih lekcij.

## 1.  Predpogoji

| Orodje             | Verzija / Opombe                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (prenesite na <https://python.org>)                                         |
| **Git**            | Najnovejši (priložen z Xcode / Git za Windows / upravitelj paketov za Linux)        |
| **VS Code**        | Neobvezno, a priporočeno <https://code.visualstudio.com>                            |
| **Docker Desktop** | *Samo* za možnost B. Brezplačna namestitev: <https://docs.docker.com/desktop/>      |

> 💡 **Namig** – Preverite orodja v terminalu:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Možnost A – Izvorni Python (najhitrejši)

### Korak 1  Klonirajte ta repozitorij

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Korak 2 Ustvarite in aktivirajte virtualno okolje

```bash
python -m venv .venv          # naredi enega
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Poziv naj se zdaj začne z (.venv) – to pomeni, da ste znotraj okolja.

### Korak 3 Namestite odvisnosti

```bash
pip install -r requirements.txt
```

Preskočite na razdelek 3 o [API ključih](../../../00-course-setup)

## 2. Možnost B – VS Code Dev Container (Docker)

Ta repozitorij in tečaj smo nastavili z [razvojnim kontejnerjem](https://containers.dev?WT.mc_id=academic-105485-koreyst), ki ima univerzalno okolje za izvajanje, ki podpira Python3, .NET, Node.js in Java razvoj. Sorodna konfiguracija je definirana v datoteki `devcontainer.json`, ki se nahaja v mapi `.devcontainer/` v korenu tega repozitorija.

>**Zakaj izbrati to?**  
>Enako okolje kot Codespaces; brez odstopanj v odvisnostih.

### Korak 0 Namestite dodatke

Docker Desktop – preverite, da ```docker --version``` deluje.  
Razširitev VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Korak 1 Odprite repozitorij v VS Code

Datoteka ▸ Odpri mapo…  → generative-ai-for-beginners

VS Code zazna .devcontainer/ in prikaže poziv.

### Korak 2 Ponovno odprite v kontejnerju

Kliknite “Reopen in Container”. Docker zgradi sliko (≈ 3 min prvič).  
Ko se pojavi terminalski poziv, ste znotraj kontejnerja.

## 2.  Možnost C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lahek namestitveni program za namestitev [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona in nekaj paketov.  
Conda je upravitelj paketov, ki omogoča enostavno nastavitev in preklapljanje med različnimi Python [**virtualnimi okolji**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) in paketi. Prav tako je uporaben za namestitev paketov, ki niso na voljo preko `pip`.

### Korak 0  Namestite Minicondo

Sledite [MiniConda namestitvenemu vodiču](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) za nastavitev.

```bash
conda --version
```

### Korak 1 Ustvarite virtualno okolje

Ustvarite novo datoteko okolja (*environment.yml*). Če sledite navodilom v Codespaces, jo ustvarite v mapi `.devcontainer`, torej `.devcontainer/environment.yml`.

### Korak 2  Izpolnite datoteko okolja

Dodajte naslednji odlomek v vašo datoteko `environment.yml`

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

### Korak 3 Ustvarite Conda okolje

Zaženite spodnje ukaze v ukazni vrstici/terminalu

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Podpot .devcontainer velja samo za nastavitve Codespace
conda activate ai4beg
```

Če naletite na težave, si oglejte [vodič za Conda okolja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Možnost D – Klasični Jupyter / Jupyter Lab (v brskalniku)

> **Za koga je to?**  
> Za vse, ki imajo radi klasični Jupyter vmesnik ali želijo poganjati zvezke brez VS Code.

### Korak 1  Preverite, da je Jupyter nameščen

Za zagon Jupyter lokalno odprite terminal/ukazno vrstico, pojdite v mapo tečaja in izvedite:

```bash
jupyter notebook
```

ali

```bash
jupyterhub
```

To bo zagnalo Jupyter instanco in URL za dostop bo prikazan v ukazni vrstici.

Ko dostopate do URL-ja, bi morali videti oris tečaja in lahko dostopate do katere koli datoteke `*.ipynb`. Na primer, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Dodajte svoje API ključe

Pomembno je, da so vaši API ključi varni in zaščiteni pri gradnji katere koli aplikacije. Priporočamo, da ne shranjujete API ključev neposredno v vašo kodo. Če te podatke potisnete v javni repozitorij, lahko pride do varnostnih težav in celo nezaželenih stroškov, če jih uporabi zlonamerna oseba.  
Tukaj je korak za korakom vodič, kako ustvariti `.env` datoteko za Python in dodati `GITHUB_TOKEN`:

1. **Pojdite v mapo vašega projekta**: Odprite terminal ali ukazno vrstico in pojdite v korensko mapo vašega projekta, kjer želite ustvariti `.env` datoteko.

   ```bash
   cd path/to/your/project
   ```

2. **Ustvarite `.env` datoteko**: Uporabite svoj najljubši urejevalnik besedila za ustvarjanje nove datoteke z imenom `.env`. Če uporabljate ukazno vrstico, lahko uporabite `touch` (na Unix sistemih) ali `echo` (na Windows):

   Unix sistemi:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteko**: Odprite `.env` datoteko v urejevalniku besedila (npr. VS Code, Notepad++ ali katerem koli drugem urejevalniku). Dodajte naslednjo vrstico v datoteko, pri čemer `your_github_token_here` zamenjajte z vašim dejanskim GitHub žetonom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Shranjevanje datoteke**: Shranite spremembe in zaprite urejevalnik besedila.

5. **Namestite `python-dotenv`**: Če ga še niste, morate namestiti paket `python-dotenv`, da naložite spremenljivke okolja iz `.env` datoteke v vašo Python aplikacijo. Namestite ga lahko z `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Naložite spremenljivke okolja v vaš Python skript**: V vašem Python skriptu uporabite paket `python-dotenv`, da naložite spremenljivke okolja iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Naloži okoljske spremenljivke iz datoteke .env
   load_dotenv()

   # Dostop do spremenljivke GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspešno ste ustvarili `.env` datoteko, dodali vaš GitHub žeton in ga naložili v vašo Python aplikacijo.

🔐 Nikoli ne potiskajte .env – že je v .gitignore.  
Celotna navodila ponudnika so v [`providers.md`](03-providers.md).

## 4. Kaj sledi?

| Želim…             | Pojdi na…                                                               |
|--------------------|-------------------------------------------------------------------------|
| Začni lekcijo 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Nastavi LLM ponudnika | [`providers.md`](03-providers.md)                                     |
| Spoznaj druge učence | [Pridruži se našemu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Reševanje težav

| Simptom                                   | Popravek                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| `python not found`                        | Dodajte Python v PATH ali ponovno odprite terminal po namestitvi |
| `pip` ne more sestaviti koles (Windows)  | `pip install --upgrade pip setuptools wheel` in poskusite znova. |
| `ModuleNotFoundError: dotenv`             | Zaženite `pip install -r requirements.txt` (okolje ni bilo nameščeno). |
| Docker build ne uspe *Ni več prostora*    | Docker Desktop ▸ *Settings* ▸ *Resources* → povečajte velikost diska. |
| VS Code stalno zahteva ponovno odpiranje  | Morda imate aktivni obe možnosti; izberite eno (venv **ali** kontejner) |
| OpenAI 401 / 429 napake                   | Preverite vrednost `OPENAI_API_KEY` / omejitve hitrosti zahtevkov. |
| Napake pri uporabi Conca                  | Namestite Microsoft AI knjižnice z `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->