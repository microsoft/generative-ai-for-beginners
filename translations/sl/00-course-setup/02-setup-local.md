<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T19:46:53+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "sl"
}
-->
# Lokalna namestitev 🖥️

**Uporabite ta vodič, če želite vse poganjati na svojem prenosniku.**  
Imate dve možnosti: **(A) izvorni Python + virtualno okolje** ali **(B) VS Code Dev Container z Dockerjem**.  
Izberite tisto, ki vam je lažja—obe vodita do istih lekcij.

## 1.  Predpogoji

| Orodje             | Različica / Opombe                                                                |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (prenesi na <https://python.org>)                                          |
| **Git**            | Najnovejši (pride z Xcode / Git za Windows / Linux upravljalnik paketov)          |
| **VS Code**        | Ni obvezen, a priporočljiv <https://code.visualstudio.com>                        |
| **Docker Desktop** | *Samo* za možnost B. Brezplačna namestitev: <https://docs.docker.com/desktop/>    |

> 💡 **Namig** – Preverite orodja v terminalu:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Možnost A – Izvorni Python (najhitreje)

### Korak 1  Klonirajte ta repozitorij

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Korak 2 Ustvarite in aktivirajte virtualno okolje

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Poziv se mora zdaj začeti z (.venv)—to pomeni, da ste v okolju.

### Korak 3 Namestite odvisnosti

```bash
pip install -r requirements.txt
```

Preskočite na 3. poglavje o [API ključih](../../../00-course-setup)

## 2. Možnost B – VS Code Dev Container (Docker)

Ta repozitorij in tečaj smo pripravili z [razvojnim kontejnerjem](https://containers.dev?WT.mc_id=academic-105485-koreyst), ki ima univerzalno okolje za Python3, .NET, Node.js in Java razvoj. Konfiguracija je določena v datoteki `devcontainer.json`, ki se nahaja v mapi `.devcontainer/` na vrhu repozitorija.

>**Zakaj izbrati to možnost?**
>Enako okolje kot Codespaces; ni razlik v odvisnostih.

### Korak 0 Namestite dodatke

Docker Desktop – preverite, da ```docker --version``` deluje.
VS Code Remote – Containers razširitev (ID: ms-vscode-remote.remote-containers).

### Korak 1 Odprite repozitorij v VS Code

Datoteka ▸ Odpri mapo…  → generative-ai-for-beginners

VS Code zazna .devcontainer/ in prikaže obvestilo.

### Korak 2 Ponovno odprite v kontejnerju

Kliknite “Reopen in Container”. Docker zgradi sliko (≈ 3 min prvič).
Ko se pojavi terminal, ste v kontejnerju.

## 2.  Možnost C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lahek namestitveni program za [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python in nekaj paketov.
Conda je upravljalnik paketov, ki olajša nastavitev in preklapljanje med različnimi Python [**virtualnimi okolji**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) in paketi. Prav tako je uporabna za namestitev paketov, ki jih ni mogoče dobiti prek `pip`.

### Korak 0  Namestite Minicondo

Sledite [MiniConda vodiču za namestitev](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) za nastavitev.

```bash
conda --version
```

### Korak 1 Ustvarite virtualno okolje

Ustvarite novo datoteko okolja (*environment.yml*). Če sledite navodilom v Codespaces, jo ustvarite v mapi `.devcontainer`, torej `.devcontainer/environment.yml`.

### Korak 2  Izpolnite datoteko okolja

Dodajte spodnji izsek v vaš `environment.yml`

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
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Če naletite na težave, si oglejte [Conda vodič za okolja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Možnost D – Klasični Jupyter / Jupyter Lab (v brskalniku)

> **Za koga je to?**  
> Za vse, ki imajo radi klasični Jupyter vmesnik ali želijo poganjati zvezke brez VS Code.  

### Korak 1  Preverite, da je Jupyter nameščen

Za zagon Jupyterja lokalno pojdite v terminal/ukazno vrstico, se premaknite v mapo tečaja in zaženite:

```bash
jupyter notebook
```

ali

```bash
jupyterhub
```

S tem se bo zagnal Jupyter in URL za dostop bo prikazan v oknu ukazne vrstice.

Ko dostopate do URL-ja, boste videli oris tečaja in lahko odprete katero koli `*.ipynb` datoteko. Na primer, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Dodajte svoje API ključe

Varno shranjevanje API ključev je pomembno pri razvoju katerekoli aplikacije. Priporočamo, da API ključev ne shranjujete neposredno v kodi. Če te podatke po nesreči objavite v javnem repozitoriju, lahko pride do varnostnih težav in celo neželenih stroškov, če jih kdo zlorabi.
Tukaj je korak-po-korak vodič, kako ustvariti `.env` datoteko za Python in dodati `GITHUB_TOKEN`:

1. **Pojdite v mapo projekta**: Odprite terminal ali ukazno vrstico in se premaknite v korensko mapo projekta, kjer želite ustvariti `.env` datoteko.

   ```bash
   cd path/to/your/project
   ```

2. **Ustvarite `.env` datoteko**: Uporabite poljuben urejevalnik besedila za ustvarjanje nove datoteke z imenom `.env`. Če uporabljate ukazno vrstico, lahko uporabite `touch` (na Unix sistemih) ali `echo` (na Windows):

   Unix sistemi:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteko**: Odprite `.env` datoteko v urejevalniku besedila (npr. VS Code, Notepad++ ali kateremkoli drugem). Dodajte naslednjo vrstico v datoteko in zamenjajte `your_github_token_here` s svojim dejanskim GitHub žetonom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Shrani datoteko**: Shranite spremembe in zaprite urejevalnik.

5. **Namestite `python-dotenv`**: Če še niste, morate namestiti paket `python-dotenv`, da naložite okoljske spremenljivke iz `.env` datoteke v Python aplikacijo. Namestite ga lahko z `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Naložite okoljske spremenljivke v Python skripti**: V Python skripti uporabite paket `python-dotenv` za nalaganje okoljskih spremenljivk iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspešno ste ustvarili `.env` datoteko, dodali svoj GitHub žeton in ga naložili v Python aplikacijo.

🔐 Nikoli ne objavite .env—že je v .gitignore.
Celotna navodila za ponudnike so v [`providers.md`](03-providers.md).

## 4. Kaj sledi?

| Želim…              | Pojdi na…                                                                |
|---------------------|--------------------------------------------------------------------------|
| Začni z lekcijo 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Nastavi LLM ponudnika | [`providers.md`](03-providers.md)                                        |
| Spoznaj druge udeležence | [Pridruži se Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Reševanje težav

| Simptom                                 | Rešitev                                                        |
|-----------------------------------------|----------------------------------------------------------------|
| `python not found`                      | Dodajte Python v PATH ali ponovno odprite terminal po namestitvi|
| `pip` ne more zgraditi wheels (Windows) | `pip install --upgrade pip setuptools wheel` in poskusite znova.|
| `ModuleNotFoundError: dotenv`           | Zaženite `pip install -r requirements.txt` (okolje ni nameščeno).|
| Docker build fails *No space left*      | Docker Desktop ▸ *Settings* ▸ *Resources* → povečajte prostor na disku.|
| VS Code stalno poziva k ponovnemu odpiranju | Morda imate aktivirani obe možnosti; izberite eno (venv **ali** container)|
| OpenAI 401 / 429 napake                 | Preverite vrednost `OPENAI_API_KEY` / omejitve zahtevkov.      |
| Napake pri uporabi Conde                | Namestite Microsoft AI knjižnice z `conda install -c microsoft azure-ai-ml`|

---

**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden s pomočjo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko samodejni prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvoru jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.