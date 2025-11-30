<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:12:45+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hr"
}
-->
# AGENTS.md

## Pregled projekta

Ovaj repozitorij sadrži sveobuhvatan kurikulum od 21 lekcije koji podučava osnove generativne umjetne inteligencije i razvoj aplikacija. Tečaj je namijenjen početnicima i pokriva sve, od osnovnih pojmova do izrade aplikacija spremnih za produkciju.

**Ključne tehnologije:**
- Python 3.9+ s bibliotekama: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript s Node.js i bibliotekama: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API i GitHub Models
- Jupyter Notebooks za interaktivno učenje
- Dev Containers za dosljedno razvojno okruženje

**Struktura repozitorija:**
- 21 numerirani direktorij lekcija (00-21) koji sadrže README datoteke, primjere koda i zadatke
- Višestruke implementacije: Python, TypeScript, a ponekad i .NET primjeri
- Direktorij za prijevode s verzijama na više od 40 jezika
- Centralizirana konfiguracija putem `.env` datoteke (koristite `.env.copy` kao predložak)

## Postavljanje okruženja

### Početno postavljanje repozitorija

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Postavljanje Python okruženja

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Postavljanje Node.js/TypeScript okruženja

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Postavljanje Dev Containera (preporučeno)

Repozitorij uključuje `.devcontainer` konfiguraciju za GitHub Codespaces ili VS Code Dev Containers:

1. Otvorite repozitorij u GitHub Codespaces ili VS Code s Dev Containers ekstenzijom
2. Dev Container automatski:
   - Instalira Python ovisnosti iz `requirements.txt`
   - Pokreće post-create skriptu (`.devcontainer/post-create.sh`)
   - Postavlja Jupyter kernel

## Radni tijek razvoja

### Varijable okruženja

Sve lekcije koje zahtijevaju pristup API-ju koriste varijable okruženja definirane u `.env`:

- `OPENAI_API_KEY` - Za OpenAI API
- `AZURE_OPENAI_API_KEY` - Za Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL za Azure OpenAI endpoint
- `AZURE_OPENAI_DEPLOYMENT` - Naziv modela za chat completion
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Naziv modela za embeddings
- `AZURE_OPENAI_API_VERSION` - Verzija API-ja (zadano: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Za Hugging Face modele
- `GITHUB_TOKEN` - Za GitHub Models

### Pokretanje Python primjera

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Pokretanje TypeScript primjera

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Pokretanje Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Rad s različitim vrstama lekcija

- **Lekcije "Learn"**: Fokus na README.md dokumentaciju i koncepte
- **Lekcije "Build"**: Uključuju funkcionalne primjere koda u Pythonu i TypeScriptu
- Svaka lekcija ima README.md s teorijom, pregledom koda i poveznicama na video sadržaj

## Smjernice za stil koda

### Python

- Koristite `python-dotenv` za upravljanje varijablama okruženja
- Uvozite `openai` biblioteku za interakciju s API-jem
- Koristite `pylint` za provjeru koda (neki primjeri uključuju `# pylint: disable=all` radi jednostavnosti)
- Pridržavajte se PEP 8 konvencija imenovanja
- Pohranite API vjerodajnice u `.env` datoteku, nikada u kod

### TypeScript

- Koristite `dotenv` paket za varijable okruženja
- Konfiguracija TypeScript-a u `tsconfig.json` za svaku aplikaciju
- Koristite `@azure/openai` ili `@azure-rest/ai-inference` za Azure usluge
- Koristite `nodemon` za razvoj s automatskim ponovnim učitavanjem
- Izgradite prije pokretanja: `npm run build` zatim `npm start`

### Opće konvencije

- Primjeri koda trebaju biti jednostavni i edukativni
- Uključite komentare koji objašnjavaju ključne koncepte
- Kod svake lekcije treba biti samostalan i funkcionalan
- Koristite dosljedna imena: `aoai-` prefiks za Azure OpenAI, `oai-` za OpenAI API, `githubmodels-` za GitHub Models

## Smjernice za dokumentaciju

### Stil Markdowna

- Sve URL-ove treba omotati u `[tekst](../../url)` format bez dodatnih razmaka
- Relativne poveznice moraju počinjati s `./` ili `../`
- Sve poveznice na Microsoft domene moraju uključivati ID za praćenje: `?WT.mc_id=academic-105485-koreyst`
- Izbjegavajte lokalizirane URL-ove (npr. `/en-us/`)
- Slike se pohranjuju u `./images` direktorij s opisnim nazivima
- Koristite engleske znakove, brojeve i crtice u nazivima datoteka

### Podrška za prijevode

- Repozitorij podržava više od 40 jezika putem automatiziranih GitHub Actions
- Prijevodi se pohranjuju u `translations/` direktorij
- Nemojte slati djelomične prijevode
- Strojni prijevodi nisu prihvaćeni
- Prijevodi slika pohranjuju se u `translated_images/` direktorij

## Testiranje i validacija

### Provjere prije slanja

Ovaj repozitorij koristi GitHub Actions za validaciju. Prije slanja PR-ova:

1. **Provjerite poveznice u Markdownu**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Ručno testiranje**:
   - Testirajte Python primjere: Aktivirajte venv i pokrenite skripte
   - Testirajte TypeScript primjere: `npm install`, `npm run build`, `npm start`
   - Provjerite jesu li varijable okruženja ispravno konfigurirane
   - Provjerite da API ključevi rade s primjerima koda

3. **Primjeri koda**:
   - Provjerite da se sav kod pokreće bez grešaka
   - Testirajte s Azure OpenAI i OpenAI API gdje je primjenjivo
   - Provjerite da primjeri rade s GitHub Models gdje je podržano

### Nema automatiziranih testova

Ovo je edukacijski repozitorij fokusiran na tutorijale i primjere. Nema jediničnih ili integracijskih testova za pokretanje. Validacija se primarno sastoji od:
- Ručnog testiranja primjera koda
- GitHub Actions za validaciju Markdowna
- Pregleda edukacijskog sadržaja od strane zajednice

## Smjernice za Pull Requestove

### Prije slanja

1. Testirajte promjene koda u Pythonu i TypeScriptu gdje je primjenjivo
2. Pokrenite validaciju Markdowna (automatski se pokreće na PR)
3. Provjerite da ID-ovi za praćenje postoje na svim Microsoft URL-ovima
4. Provjerite da su relativne poveznice valjane
5. Provjerite da su slike ispravno referencirane

### Format naslova PR-a

- Koristite opisne naslove: `[Lekcija 06] Ispravak tipfelera u Python primjeru` ili `Ažuriranje README za lekciju 08`
- Referencirajte brojeve problema gdje je primjenjivo: `Fixes #123`

### Opis PR-a

- Objasnite što je promijenjeno i zašto
- Povežite se na povezane probleme
- Za promjene koda, navedite koji su primjeri testirani
- Za PR-ove prijevoda, uključite sve datoteke za potpuni prijevod

### Zahtjevi za doprinos

- Potpišite Microsoft CLA (automatski na prvom PR-u)
- Forkajte repozitorij na svoj račun prije izmjena
- Jedan PR po logičkoj promjeni (ne kombinirajte nepovezane ispravke)
- PR-ovi trebaju biti fokusirani i mali kad je moguće

## Uobičajeni radni tijekovi

### Dodavanje novog primjera koda

1. Navigirajte do odgovarajućeg direktorija lekcije
2. Kreirajte primjer u `python/` ili `typescript/` poddirektoriju
3. Slijedite konvenciju imenovanja: `{provider}-{example-name}.{py|ts|js}`
4. Testirajte s stvarnim API vjerodajnicama
5. Dokumentirajte nove varijable okruženja u README lekcije

### Ažuriranje dokumentacije

1. Uredite README.md u direktoriju lekcije
2. Slijedite smjernice za Markdown (ID-ovi za praćenje, relativne poveznice)
3. Ažuriranje prijevoda se obavlja putem GitHub Actions (ne uređujte ručno)
4. Testirajte da su sve poveznice valjane

### Rad s Dev Containerima

1. Repozitorij uključuje `.devcontainer/devcontainer.json`
2. Post-create skripta automatski instalira Python ovisnosti
3. Ekstenzije za Python i Jupyter su unaprijed konfigurirane
4. Okruženje se temelji na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Implementacija i objavljivanje

Ovo je edukacijski repozitorij - nema procesa implementacije. Kurikulum se koristi putem:

1. **GitHub repozitorija**: Direktan pristup kodu i dokumentaciji
2. **GitHub Codespaces**: Instant razvojno okruženje s unaprijed konfiguriranim postavkama
3. **Microsoft Learn**: Sadržaj može biti distribuiran na službenoj platformi za učenje
4. **docsify**: Dokumentacijska stranica izrađena iz Markdowna (vidi `docsifytopdf.js` i `package.json`)

### Izrada dokumentacijske stranice

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Rješavanje problema

### Uobičajeni problemi

**Greške pri uvozu u Pythonu**:
- Provjerite je li virtualno okruženje aktivirano
- Pokrenite `pip install -r requirements.txt`
- Provjerite da je verzija Pythona 3.9+

**Greške pri izgradnji TypeScript-a**:
- Pokrenite `npm install` u specifičnom direktoriju aplikacije
- Provjerite je li verzija Node.js kompatibilna
- Očistite `node_modules` i ponovno instalirajte ako je potrebno

**Greške pri autentifikaciji API-ja**:
- Provjerite da `.env` datoteka postoji i ima ispravne vrijednosti
- Provjerite da su API ključevi valjani i nisu istekli
- Provjerite da su URL-ovi endpointa ispravni za vašu regiju

**Nedostaju varijable okruženja**:
- Kopirajte `.env.copy` u `.env`
- Ispunite sve potrebne vrijednosti za lekciju na kojoj radite
- Ponovno pokrenite aplikaciju nakon ažuriranja `.env`

## Dodatni resursi

- [Vodič za postavljanje tečaja](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Smjernice za doprinos](./CONTRIBUTING.md)
- [Kodeks ponašanja](./CODE_OF_CONDUCT.md)
- [Sigurnosna politika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Zbirka naprednih primjera koda](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Napomene specifične za projekt

- Ovo je **edukacijski repozitorij** fokusiran na učenje, a ne produkcijski kod
- Primjeri su namjerno jednostavni i fokusirani na podučavanje koncepata
- Kvaliteta koda je uravnotežena s edukacijskom jasnoćom
- Svaka lekcija je samostalna i može se završiti neovisno
- Repozitorij podržava više API pružatelja: Azure OpenAI, OpenAI i GitHub Models
- Sadržaj je višejezičan s automatiziranim radnim tijekovima za prijevod
- Aktivna zajednica na Discordu za pitanja i podršku

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.