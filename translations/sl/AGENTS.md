# AGENTS.md

## Pregled projekta

Ta repozitorij vsebuje obsežen program učenja s 21 lekcijami, ki učijo osnovne pojme generativne umetne inteligence in razvoj aplikacij. Tečaj je zasnovan za začetnike in pokriva vse od osnovnih konceptov do izdelave aplikacij pripravljenih za produkcijo.

**Ključne tehnologije:**
- Python 3.9+ z bibliotekami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript z Node.js in knjižnicami: `openai` (Azure OpenAI prek v1 končne točke + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API in Microsoft Foundry Models (GitHub Models bo prenehal konec julija 2026)
- Jupyter zvezki za interaktivno učenje
- Dev Containers za dosledno razvojno okolje

**Struktura repozitorija:**
- 21 po številkah označenih imenikov lekcij (00-21), ki vsebujejo README datoteke, primere kode in naloge
- Več implementacij: Python, TypeScript in občasno primeri .NET
- Imenik prevodov z več kot 40 jezikovnimi različicami
- Centralizirana konfiguracija prek datoteke `.env` (uporabite `.env.copy` kot predlogo)

## Ukazi za nastavitev

### Prva nastavitev repozitorija

```bash
# Klonirajte repozitorij
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopirajte predlogo okolja
cp .env.copy .env
# Uredite .env s svojimi API ključi in končnimi točkami
```

### Nastavitev Python okolja

```bash
# Ustvari virtualno okolje
python3 -m venv venv

# Aktiviraj virtualno okolje
# Na macOS/Linux:
source venv/bin/activate
# Na Windows:
venv\Scripts\activate

# Namesti odvisnosti
pip install -r requirements.txt
```

### Nastavitev Node.js/TypeScript

```bash
# Namestite odvisnosti na nivoju root (za orodja za dokumentacijo)
npm install

# Za posamezne primere TypeScript lekcij pojdite na določeno lekcijo:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Nastavitev Dev Containerja (priporočeno)

Repozitorij vključuje konfiguracijo `.devcontainer` za GitHub Codespaces ali VS Code Dev Containers:

1. Odprite repozitorij v GitHub Codespaces ali VS Code z razširitvijo Dev Containers
2. Dev Container bo samodejno:
   - Namestil Python odvisnosti iz `requirements.txt`
   - Zagnal skripto po ustvaritvi (`.devcontainer/post-create.sh`)
   - Nastavil Jupyter jedro

## Razvojni potek

### Okoljske spremenljivke

Vse lekcije, ki potrebujejo dostop do API, uporabljajo okoljske spremenljivke definirane v `.env`:

- `OPENAI_API_KEY` - Za OpenAI API
- `AZURE_OPENAI_API_KEY` - Za Azure OpenAI v Microsoft Foundry (Azure OpenAI Service je zdaj del Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL končne točke Azure OpenAI (končna točka Foundry vira)
- `AZURE_OPENAI_DEPLOYMENT` - Ime nameščene različice modela za klepet
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Ime nameščene različice modela za vdelave
- `AZURE_OPENAI_API_VERSION` - Verzija API (privzeto: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Za modele Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Končna točka Microsoft Foundry Models (katalog modelov več ponudnikov)
- `AZURE_INFERENCE_CREDENTIAL` - API ključ Microsoft Foundry Models (nadomešča opuščeni `GITHUB_TOKEN`)

### Zagon Python primerov

```bash
# Pomaknite se do imenika lekcije
cd 06-text-generation-apps/python

# Zaženite Python skripto
python aoai-app.py
```

### Zagon TypeScript primerov

```bash
# Pojdi v imenik aplikacije TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Zgradi TypeScript kodo
npm run build

# Zaženi aplikacijo
npm start
```

### Zagon Jupyter zvezkov

```bash
# Zaženi Jupyter v korenu repozitorija
jupyter notebook

# Ali uporabi VS Code z Jupyter razširitvijo
```

### Delo z različnimi vrstami lekcij

- **Lekcije "Learn"**: Osredotočene na dokumentacijo README.md in koncepte
- **Lekcije "Build"**: Vsebujejo delujoče primere kode v Python in TypeScript
- Vsaka lekcija ima README.md z teorijo, razlagami kode in povezavami do video vsebin

## Smernice stile kode

### Python

- Uporabljajte `python-dotenv` za upravljanje okoljskih spremenljivk
- Uvozite knjižnico `openai` za interakcije z API
- Uporabite `pylint` za pregled kode (nekateri primeri vključujejo `# pylint: disable=all` za poenostavitev)
- Upoštevajte poimenovalne konvencije PEP 8
- Shranjujte API poverilnice v `.env` datoteki, nikoli v kodi

### TypeScript

- Uporabljajte paket `dotenv` za okoljske spremenljivke
- Konfiguracija TypeScript v `tsconfig.json` za vsako aplikacijo
- Uporabite paket `openai` za Azure OpenAI (usmerite klienta na `/openai/v1/` končno točko in pokličite `client.responses.create`); za Microsoft Foundry Models uporabite `@azure-rest/ai-inference`
- Za razvoj uporabite `nodemon` z avtomatskim ponovnim nalaganjem
- Pred zagonom zgradite: `npm run build` nato `npm start`

### Splošne konvencije

- Naj bodo primeri kode enostavni in poučni
- Vključite komentarje, ki pojasnjujejo ključne koncepte
- Koda v vsaki lekciji naj bo samostojna in izvedljiva
- Uporabljajte dosledno poimenovanje: predpona `aoai-` za Azure OpenAI, `oai-` za OpenAI API, `githubmodels-` za Microsoft Foundry Models (ohranjen dedni predpona iz obdobja GitHub Models)

## Smernice za dokumentacijo

### Stil Markdown

- Vsi URL-ji morajo biti v obliki `[text](../../url)` brez dodatnih presledkov
- Relativne povezave morajo začeti z `./` ali `../`
- Vse povezave do Microsoft domen morajo vsebovati ID za sledenje: `?WT.mc_id=academic-105485-koreyst`
- Brez lokalizacij specifičnih za državo v URL-jih (izogibajte se `/en-us/`)
- Slike shranjene v mapi `./images` z opisnimi imeni
- Uporabljajte angleške znake, številke in vezaje v imenih datotek

### Podpora za prevajanje

- Repozitorij podpira več kot 40 jezikov preko avtomatiziranih GitHub Actions
- Prevodi so shranjeni v imeniku `translations/`
- Ne pošiljajte delnih prevodov
- Strojni prevodi niso sprejeti
- Prevedene slike so shranjene v imeniku `translated_images/`

## Testiranje in preverjanje

### Preverjanja pred oddajo

Ta repozitorij uporablja GitHub Actions za preverjanje. Pred oddajo PR:

1. **Preverite Markdown povezave**:
   ```bash
   # Potek validate-markdown.yml preverja:
   # - Pokvarjene relativne poti
   # - Manjkajoče ID-je za sledenje na poteh
   # - Manjkajoče ID-je za sledenje na URL-jih
   # - URL-ji z državno lokalizacijo
   # - Pokvarjeni zunanji URL-ji
   ```

2. **Ročno testiranje**:
   - Testirajte Python primere: Aktivirajte venv in zaženite skripte
   - Testirajte TypeScript primere: `npm install`, `npm run build`, `npm start`
   - Preverite, da so okoljske spremenljivke pravilno konfigurirane
   - Preverite, da API ključi delujejo s primeri kode

3. **Primeri kode**:
   - Zagotovite, da se vsa koda izvaja brez napak
   - Testirajte z obema Azure OpenAI in OpenAI API kadar je to mogoče
   - Preverite, da primeri delujejo z Microsoft Foundry Models kjer so podprti

### Brez avtomatiziranih testov

To je izobraževalni repozitorij osredotočen na vodiče in primere. Ni enotnih ali integracijskih testov za zagon. Preverjanje je predvsem:
- Ročno testiranje primerov kode
- GitHub Actions za preverjanje Markdowna
- Skupnostni pregled izobraževalnih vsebin

## Smernice za Pull Request

### Pred oddajo

1. Testirajte spremembe kode v Python in TypeScript kadar je to mogoče
2. Zaženite preverjanje Markdowna (samodejno sproženo na PR)
3. Prepričajte se, da so ID-ji za sledenje prisotni na vseh Microsoft URL-jih
4. Preverite, da so relativne povezave veljavne
5. Preverite, da so slike ustrezno referencirane

### Oblika naslova PR

- Uporabljajte opisne naslove: `[Lesson 06] Popravi tipkarsko napako v Python primeru` ali `Posodobi README za lekcijo 08`
- Navedejte številke težav, kjer je to ustrezno: `Popravlja #123`

### Opis PR

- Pojasnite, kaj je bilo spremenjeno in zakaj
- Povežite sorodne težave
- Za spremembe kode navedite, kateri primeri so bili testirani
- Za prevodne PR vključite vse datoteke za popoln prevod

### Zahteve za prispevke

- Podpišite Microsoft CLA (samodejno ob prvem PR)
- Razvejajte repozitorij na svoj račun pred spremembami
- En PR na logično spremembo (ne kombinirajte nepovezanih popravkov)
- Kadar je možno ohranite PR osredotočen in majhen

## Pogosti poteki dela

### Dodajanje novega primera kode

1. Pojdite v ustrezni imenik lekcije
2. Ustvarite primer v podimeniku `python/` ali `typescript/`
3. Upoštevajte konvencijo poimenovanja: `{provider}-{primer-ime}.{py|ts|js}`
4. Testirajte z dejanskimi API poverilnicami
5. Dokumentirajte nove okoljske spremenljivke v README lekcije

### Posodabljanje dokumentacije

1. Uredite README.md v imeniku lekcije
2. Upoštevajte Markdown smernice (ID-ji za sledenje, relativne povezave)
3. Prevode posodablja GitHub Actions (ne urejajte ročno)
4. Preizkusite, da so vse povezave veljavne

### Delo z Dev Containers

1. Repozitorij vsebuje `.devcontainer/devcontainer.json`
2. Skripta po ustvaritvi samodejno namesti Python odvisnosti
3. Razširitve za Python in Jupyter so predhodno konfigurirane
4. Okolje temelji na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Razmestitev in objava

To je izobraževalni repozitorij - proces razmestitve ni potreben. Program uporablja:

1. **GitHub Repozitorij**: Neposreden dostop do kode in dokumentacije
2. **GitHub Codespaces**: Takojšnje razvojno okolje z vnaprej nastavljenim okoljem
3. **Microsoft Learn**: Vsebina je lahko sinhronizirana z uradno platformo za učenje
4. **docsify**: Spletno mesto dokumentacije zgrajeno iz Markdowna (glejte `docsifytopdf.js` in `package.json`)

### Izdelava spletnega mesta dokumentacije

```bash
# Ustvari PDF iz dokumentacije (če je potrebno)
npm run convert
```

## Reševanje težav

### Pogoste težave

**Napake uvoza v Pythonu**:
- Prepričajte se, da je virtualno okolje aktivirano
- Zaženite `pip install -r requirements.txt`
- Preverite, da je verzija Pythona 3.9 ali novejša

**Napake pri gradnji TypeScript**:
- Zaženite `npm install` v specifičnem imeniku aplikacije
- Preverite združljivost verzije Node.js
- Po potrebi počistite `node_modules` in ponovno namestite

**Napake avtorizacije API**:
- Preverite obstoj `.env` datoteke in pravilne vrednosti
- Preverite, da so API ključi veljavni in niso potekli
- Prepričajte se, da URL-ji končnih točk ustrezajo vaši regiji

**Manjkajoče okoljske spremenljivke**:
- Kopirajte `.env.copy` v `.env`
- Izpolnite vse zahtevane vrednosti za lekcijo, na kateri delate
- Po posodobitvi `.env` ponovno zaženite aplikacijo

## Dodatni viri

- [Vodnik za nastavitev tečaja](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Smernice za prispevke](./CONTRIBUTING.md)
- [Kodeks ravnanja](./CODE_OF_CONDUCT.md)
- [Varnostna politika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Zbirka naprednih primerov kode](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Opombe specifične za projekt

- To je **izobraževalni repozitorij**, osredotočen na učenje, ne produkcijsko kodo
- Primeri so namensko preprosti in usmerjeni v poučevanje konceptov
- Kakovost kode je uravnotežena z jasnostjo učenja
- Vsaka lekcija je samostojna in jo je mogoče dokončati neodvisno
- Repozitorij podpira več ponudnikov API: Azure OpenAI, OpenAI, Microsoft Foundry Models in offline ponudnike, kot sta Foundry Local in Ollama
- Vsebina je večjezična z avtomatiziranimi poteki prevajanja
- Aktivna skupnost na Discordu za vprašanja in podporo

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->