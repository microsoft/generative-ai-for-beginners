# Lokalna nastavitev 🖥️

**Uporabite ta vodič, če želite vse poganjati na svojem prenosniku.**   
Imate dve poti: **(A) izvorni Python + virtualno okolje** ali **(B) VS Code Dev Container z Dockerjem**.  
Izberite tisto, kar vam je bolj enostavno – obe vodita do istih lekcij.

## 1.  Predpogoji

| Orodje             | Verzija / Opombe                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (pridobite ga iz <https://python.org>)                                        |
| **Git**            | Najnovejša (priložena z Xcode / Git za Windows / upravitelj paketov za Linux)         |
| **VS Code**        | Neobvezno, a priporočeno <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Samo* za možnost B. Brezplačna namestitev: <https://docs.docker.com/desktop/>       |

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

✅ Poziv naj se sedaj začne z (.venv) – to pomeni, da ste znotraj okolja.

### Korak 3 Namestite odvisnosti

```bash
pip install -r requirements.txt
```

Preskočite na poglavje 3 o [API ključih](#3-dodajte-svoje-api-ključe)

## 2. Možnost B – VS Code Dev Container (Docker)

Ta repozitorij in tečaj smo pripravili z [razvojnim kontejnerjem](https://containers.dev?WT.mc_id=academic-105485-koreyst), ki ima univerzalno runtime okolje, ki podpira Python3, .NET, Node.js in Java razvoj. Sorodno konfiguracijo določa datoteka `devcontainer.json`, ki se nahaja v mapi `.devcontainer/` v korenu tega repozitorija.

>**Zakaj izbrati to?**
>Enako okolje kot Codespaces; brez odvisnostnih drifta.

### Korak 0 Namestite dodatke

Docker Desktop – preverite, da ukaz ```docker --version``` deluje.
VS Code Remote – Containers razširitev (ID: ms-vscode-remote.remote-containers).

### Korak 1 Odprite repozitorij v VS Code

Datoteka ▸ Odpri mapo…  → generative-ai-for-beginners

VS Code zazna `.devcontainer/` in pojavi se poziv.

### Korak 2 Odprite v kontejnerju

Kliknite "Reopen in Container". Docker zgradi sliko (≈ 3 minute prvič).
Ko se pokaže poziv v terminalu, ste znotraj kontejnerja.

## 2.  Možnost C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lahek namestitveni program za namestitev [Conde](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona, ter nekaj paketov.
Conda sama je upravitelj paketov, ki olajša nastavitev in preklapljanje med različnimi Python [**virtualnimi okolji**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) in paketi. Uporabna je tudi za namestitev paketov, ki niso na voljo preko `pip`.

### Korak 0  Namestite Minicondo

Sledite [MiniConda namestitvenemu vodiču](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) za njeno postavitev.

```bash
conda --version
```

### Korak 1 Ustvarite virtualno okolje

Ustvarite novo datoteko okolja (*environment.yml*). Če sledite iz Codespaces, jo ustvarite znotraj `.devcontainer` imenika, torej `.devcontainer/environment.yml`.

### Korak 2  Izpolnite datoteko okolja

Dodajte naslednjo kodo v `environment.yml`

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

Zaženite spodnje ukaze v vašem ukaznem pozivu/terminalu

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Podpot .devcontainer velja samo za nastavitve Codespace
conda activate ai4beg
```

Za več informacij glejte [vodnik za Conda okolja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), če naletite na težave.

## 2  Možnost D – Klasični Jupyter / Jupyter Lab (v vašem brskalniku)

> **Komu je namenjeno?**  
> Vsem, ki imajo radi klasičen Jupyter vmesnik ali želijo izvajati zvezke brez VS Code.  

### Korak 1  Preverite, ali je Jupyter nameščen

Za zagon Jupytra lokalno odprite terminal/ukazno vrstico, pojdite v direktorij tečaja in izvedite:

```bash
jupyter notebook
```

ali

```bash
jupyterhub
```

To bo zagnalo Jupyter instanco in URL za dostop bo prikazan v ukaznem oknu.

Ko dostopate do URL-ja, boste videli vsebino tečaja in lahko krmarili do vsake datoteke z `*.ipynb`. Na primer, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Dodajte svoje API ključe

Za varnost vaših API ključev je pomembno, da jih ne shranjujete neposredno v kodi. Če jih potisnete v javni repozitorij, lahko to povzroči varnostne težave in celo nezaželene stroške, če jih uporabi nekdo zlonameren.
Tukaj je korak-po-korak vodič, kako ustvariti datoteko `.env` za Python in dodati poverilnice za Microsoft Foundry Models:

> **Opomba:** GitHub Models (in njegova spremenljivka `GITHUB_TOKEN`) se upokaja konec julija 2026. Ta vodič uporablja [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Raje delate popolnoma brez povezave? Oglejte si [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Pojdite v Mapa Projekta**: Odprite terminal ali ukazno vrstico in se pomaknite v glavno mapo vašega projekta, kjer želite ustvariti `.env` datoteko.

   ```bash
   cd path/to/your/project
   ```

2. **Ustvarite `.env` datoteko**: Uporabite svoj najljubši urejevalnik besedil za ustvarjanje nove datoteke z imenom `.env`. Če uporabljate ukazno vrstico, lahko uporabite `touch` (na Unix sistemih) ali `echo` (na Windows):

   Unix sistemi:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteko**: Odprite `.env` datoteko v besedilnem urejevalniku (npr. VS Code, Notepad++ ali katerikoli drug urejevalnik). Dodajte naslednje vrstice, pri čemer zamenjajte vrednosti s svojim Microsoft Foundry končnim točko in API ključem:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Shrani datoteko**: Shrani spremembe in zapri urejevalnik.

5. **Namestite `python-dotenv`**: Če še niste, morate namestiti paket `python-dotenv`, da naložite spremenljivke okolja iz `.env` datoteke v vašo Python aplikacijo. Namestite ga lahko z `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Naložite spremenljivke okolja v Python skripti**: V vaši Python skripti uporabite paket `python-dotenv`, da naložite spremenljivke okolja iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Naloži okoljske spremenljivke iz datoteke .env
   load_dotenv()

   # Dostopaj do spremenljivk Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To je to! Uspešno ste ustvarili `.env` datoteko, dodali poverilnice za Microsoft Foundry Models in jih naložili v svojo Python aplikacijo.

🔐 Datoteke .env nikoli ne komitirajte – že je v .gitignore.
Celotna navodila za ponudnike so v [`providers.md`](03-providers.md).

## 4. Kaj sledi?

| Želim…              | Pojdi na…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Začeti Lekcijo 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Nastaviti LLM ponudnika | [`providers.md`](03-providers.md)                                       |
| Spoznati druge učence | [Pridruži se našemu Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)  |

## 5. Reševanje težav

| Simptom                                    | Popravek                                                         |
|--------------------------------------------|-----------------------------------------------------------------|
| `python ni najden`                        | Dodajte Python v PATH ali znova odprite terminal po namestitvi. |
| `pip` ne more zgraditi koles (Windows)   | `pip install --upgrade pip setuptools wheel` nato poskusite znova.|
| `ModuleNotFoundError: dotenv`              | Zaženite `pip install -r requirements.txt` (okolje ni bilo nameščeno).|
| Docker build spodleti *Ni prostora*        | Docker Desktop ▸ *Settings* ▸ *Resources* → povečajte velikost diska.|
| VS Code vas stalno poziva k ponovnemu odpiranju | Morda imate aktivni oba možnosti; izberite eno (venv **ali** kontejner)|
| OpenAI 401 / 429 napake                    | Preverite vrednost `OPENAI_API_KEY` / omejitve zahtevkov.         |
| Napake pri uporabi Conde                   | Namestite Microsoft AI knjižnice z `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->