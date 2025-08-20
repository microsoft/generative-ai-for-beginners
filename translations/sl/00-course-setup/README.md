<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:18:48+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sl"
}
-->
# Začetek s tem tečajem

Zelo smo navdušeni, da začnete ta tečaj in vidite, kaj vas bo navdihnilo za ustvarjanje z Generativno AI!

Da zagotovimo vaš uspeh, ta stran opisuje korake za nastavitev, tehnične zahteve in kje poiskati pomoč, če jo potrebujete.

## Koraki za nastavitev

Za začetek tečaja morate opraviti naslednje korake.

### 1. Razvezi ta repozitorij

[Razvezi celoten repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) na svoj GitHub račun, da boste lahko spreminjali kodo in reševali izzive. Prav tako lahko [označite (🌟) ta repozitorij](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), da ga boste lažje našli skupaj s sorodnimi repozitoriji.

### 2. Ustvari codespace

Da se izognete težavam z odvisnostmi pri izvajanju kode, priporočamo, da tečaj izvajate v [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

To lahko ustvarite tako, da na svoji razvezi repozitorija izberete možnost `Code` in nato izberete **Codespaces**.

![Dialog, ki prikazuje gumbe za ustvarjanje codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Shranjevanje vaših API ključev

Pomembno je, da so vaši API ključi varni in zaščiteni pri gradnji katere koli aplikacije. Priporočamo, da API ključev ne shranjujete neposredno v kodo. Če bi te podatke objavili v javnem repozitoriju, bi to lahko povzročilo varnostne težave in celo nezaželene stroške, če jih uporabi zlonamerna oseba.  
Tukaj je korak za korakom vodič, kako ustvariti `.env` datoteko za Python in dodati `GITHUB_TOKEN`:

1. **Pojdite v mapo vašega projekta**: Odprite terminal ali ukazno vrstico in se premaknite v korensko mapo projekta, kjer želite ustvariti `.env` datoteko.

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

3. **Uredite `.env` datoteko**: Odprite `.env` datoteko v urejevalniku (npr. VS Code, Notepad++ ali katerem koli drugem). Dodajte naslednjo vrstico, pri čemer `your_github_token_here` zamenjajte z vašim dejanskim GitHub žetonom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Shrani datoteko**: Shrani spremembe in zapri urejevalnik.

5. **Namestite `python-dotenv`**: Če še niste, morate namestiti paket `python-dotenv`, da boste lahko naložili okoljske spremenljivke iz `.env` datoteke v vašo Python aplikacijo. Namestite ga lahko z `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Naložite okoljske spremenljivke v vaš Python skript**: V vašem Python skriptu uporabite paket `python-dotenv`, da naložite okoljske spremenljivke iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspešno ste ustvarili `.env` datoteko, dodali vaš GitHub žeton in ga naložili v Python aplikacijo.

## Kako zagnati lokalno na vašem računalniku

Za lokalno izvajanje kode na vašem računalniku morate imeti nameščeno neko različico [Pythona](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Nato morate repozitorij klonirati:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Ko imate vse pripravljeno, lahko začnete!

## Izbirni koraki

### Namestitev Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lahek namestitveni program za namestitev [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona in nekaj paketov.  
Conda je upravljalnik paketov, ki olajša nastavitev in preklapljanje med različnimi Python [**virtualnimi okolji**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) in paketi. Prav tako je uporaben za namestitev paketov, ki niso na voljo preko `pip`.

Sledite [MiniConda vodiču za namestitev](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), da jo nastavite.

Ko imate Minicondo nameščeno, morate klonirati [repozitorij](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (če tega še niste storili).

Nato morate ustvariti virtualno okolje. Za to z Condo ustvarite novo datoteko okolja (_environment.yml_). Če sledite navodilom v Codespaces, jo ustvarite v mapi `.devcontainer`, torej `.devcontainer/environment.yml`.

V datoteko okolja vnesite spodnjo kodo:

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

Če naletite na napake pri uporabi conde, lahko ročno namestite Microsoft AI knjižnice z naslednjim ukazom v terminalu.

```
conda install -c microsoft azure-ai-ml
```

Datoteka okolja določa potrebne odvisnosti. `<environment-name>` je ime, ki ga želite uporabiti za vaše Conda okolje, `<python-version>` pa različica Pythona, ki jo želite uporabiti, na primer `3` za najnovejšo glavno različico.

Ko je to pripravljeno, lahko ustvarite Conda okolje z izvajanjem spodnjih ukazov v ukazni vrstici/terminalu:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Če naletite na težave, si oglejte [Conda vodič za upravljanje okolij](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Uporaba Visual Studio Code z razširitvijo za Python

Priporočamo uporabo urejevalnika [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) z nameščeno [razširitvijo za podporo Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) za ta tečaj. To je priporočilo, ne pa obvezna zahteva.

> **Opomba**: Ko odprete repozitorij tečaja v VS Code, imate možnost nastaviti projekt znotraj kontejnerja. To omogoča [posebna mapa `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) v repozitoriju tečaja. Več o tem kasneje.

> **Opomba**: Ko klonirate in odprete mapo v VS Code, vam bo samodejno predlagal namestitev razširitve za Python.

> **Opomba**: Če vam VS Code predlaga ponovno odpiranje repozitorija v kontejnerju, to zahtevo zavrnite, če želite uporabljati lokalno nameščeno različico Pythona.

### Uporaba Jupyterja v brskalniku

Projekt lahko urejate tudi v [Jupyter okolju](https://jupyter.org?WT.mc_id=academic-105485-koreyst) neposredno v brskalniku. Tako klasični Jupyter kot [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) nudita prijetno razvojno okolje z funkcijami, kot so samodejno dokončanje, poudarjanje kode itd.

Za zagon Jupyterja lokalno odprite terminal/ukazno vrstico, pojdite v mapo tečaja in izvedite:

```bash
jupyter notebook
```

ali

```bash
jupyterhub
```

S tem se bo zagnal Jupyter in URL za dostop bo prikazan v ukazni vrstici.

Ko odprete URL, boste videli strukturo tečaja in lahko dostopali do katere koli `*.ipynb` datoteke, na primer `08-building-search-applications/python/oai-solution.ipynb`.

### Zagon v kontejnerju

Alternativa nastavitvi vsega na vašem računalniku ali Codespace je uporaba [kontejnerja](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Posebna mapa `.devcontainer` v repozitoriju tečaja omogoča VS Code, da nastavi projekt znotraj kontejnerja. Izven Codespaces to zahteva namestitev Dockerja in, iskreno, vključuje nekaj dela, zato to priporočamo le tistim z izkušnjami pri delu s kontejnerji.

Eden najboljših načinov za varno shranjevanje vaših API ključev pri uporabi GitHub Codespaces je uporaba Codespace Secrets. Za več informacij sledite vodiču za [upravljanje skrivnosti v Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Lekcije in tehnične zahteve

Tečaj vsebuje 6 konceptualnih lekcij in 6 programerskih lekcij.

Za programerske lekcije uporabljamo Azure OpenAI Service. Potrebovali boste dostop do Azure OpenAI storitve in API ključ za zagon kode. Dostop lahko zaprosite z [izpolnitvijo te prijave](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Medtem ko čakate na obdelavo vaše prijave, vsaka programerska lekcija vsebuje tudi datoteko `README.md`, kjer si lahko ogledate kodo in rezultate.

## Prvič uporabljate Azure OpenAI Service

Če prvič uporabljate Azure OpenAI storitev, sledite temu vodiču, kako [ustvariti in namestiti Azure OpenAI Service vir.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Prvič uporabljate OpenAI API

Če prvič uporabljate OpenAI API, sledite vodiču, kako [ustvariti in uporabljati vmesnik.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Spoznajte druge udeležence

Ustvarili smo kanale v našem uradnem [AI Community Discord strežniku](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) za spoznavanje drugih udeležencev. To je odličen način za mreženje z drugimi podjetniki, razvijalci, študenti in vsakim, ki želi napredovati v Generativni AI.

[![Pridruži se discord kanalu](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Ekipa projekta bo prav tako na voljo na tem Discord strežniku, da pomaga udeležencem.

## Prispevajte

Ta tečaj je odprtokodna pobuda. Če opazite možnosti za izboljšave ali težave, prosimo, ustvarite [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ali prijavite [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Ekipa projekta bo spremljala vse prispevke. Prispevanje v odprto kodo je odličen način za razvoj kariere v Generativni AI.

Večina prispevkov zahteva, da se strinjate s Contributor License Agreement (CLA), s katerim izjavite, da imate pravico in dejansko podeljujete pravice za uporabo vašega prispevka. Za podrobnosti obiščite [CLA, Contributor License Agreement spletno stran](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Pomembno: pri prevajanju besedila v tem repozitoriju ne uporabljajte strojnega prevajanja. Prevajanja bomo preverjali preko skupnosti, zato prosimo, da se prijavite za prevode samo v jezikih, v katerih ste vešči.

Ko oddate pull request, bo CLA-bot samodejno ugotovil, ali morate predložiti CLA, in ustrezno označil PR (npr. z oznako, komentarjem). Preprosto sledite navodilom bota. To boste morali storiti samo enkrat za vse repozitorije, ki uporabljajo naš CLA.

Ta projekt je sprejel [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Za več informacij preberite Pogosta vprašanja o kodeksu ravnanja ali kontaktirajte [Email opencode](opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Začnimo

Zdaj, ko ste opravili potrebne korake za ta tečaj, začnimo z [uvodom v Generativno AI in LLM-je](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.