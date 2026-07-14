# AGENTS.md

## Pregled projekta

Ovaj spremište sadrži sveobuhvatan kurikulum od 21 lekcije koji podučava osnove Generativne AI i razvoj aplikacija. Tečaj je dizajniran za početnike i pokriva sve od osnovnih koncepata do izrade aplikacija spremnih za produkciju.

**Ključne tehnologije:**
- Python 3.9+ s bibliotekama: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript s Node.js i bibliotekama: `openai` (Azure OpenAI preko v1 endpointa + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry modeli)
- Azure OpenAI servis, OpenAI API i Microsoft Foundry modeli (GitHub modeli se povlače krajem srpnja 2026.)
- Jupyter bilježnice za interaktivno učenje
- Dev kontejneri za konzistentno razvojno okruženje

**Struktura spremišta:**
- 21 numeriranih direktorija lekcija (00-21) koji sadrže README, primjere koda i zadatke
- Više implementacija: Python, TypeScript i ponekad .NET primjeri
- Direktorij prijevoda s 40+ jezičnih verzija
- Centralizirana konfiguracija preko `.env` datoteke (koristite `.env.copy` kao predložak)

## Komande za postavljanje

### Početno postavljanje spremišta

```bash
# Klonirajte repozitorij
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopirajte predložak okoline
cp .env.copy .env
# Uredite .env s vašim API ključevima i krajnjim točkama
```

### Postavljanje Python okruženja

```bash
# Kreiraj virtualno okruženje
python3 -m venv venv

# Aktiviraj virtualno okruženje
# Na macOS/Linux:
source venv/bin/activate
# Na Windows:
venv\Scripts\activate

# Instaliraj ovisnosti
pip install -r requirements.txt
```

### Postavljanje Node.js/TypeScript-a

```bash
# Instalirajte ovisnosti na razini root-a (za alate za dokumentaciju)
npm install

# Za pojedinačne primjere TypeScript lekcija, idite na određenu lekciju:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Postavljanje dev kontejnera (preporučeno)

Spremište uključuje `.devcontainer` konfiguraciju za GitHub Codespaces ili VS Code Dev Containers:

1. Otvorite spremište u GitHub Codespaces ili VS Code s Dev Containers ekstenzijom
2. Dev kontejner će automatski:
   - Instalirati Python ovisnosti iz `requirements.txt`
   - Pokrenuti post-create skriptu (`.devcontainer/post-create.sh`)
   - Postaviti Jupyter kernel

## Radni tijek razvoja

### Varijable okruženja

Sve lekcije koje zahtijevaju pristup API-ju koriste varijable okruženja definirane u `.env` datoteci:

- `OPENAI_API_KEY` - Za OpenAI API
- `AZURE_OPENAI_API_KEY` - Za Azure OpenAI u Microsoft Foundry (Azure OpenAI servis sada je dio Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL Azure OpenAI endpointa (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Naziv deploymenta modela za chat completions
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Naziv deploymenta modela za embeddings
- `AZURE_OPENAI_API_VERSION` - Verzija API-ja (zadano: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Za Hugging Face modele
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry modeli endpoint (katalog modela više pružatelja)
- `AZURE_INFERENCE_CREDENTIAL` - API ključ za Microsoft Foundry modele (zamjenjuje povlačeći se `GITHUB_TOKEN`)

### Pokretanje Python primjera

```bash
# Navigirajte do direktorija lekcije
cd 06-text-generation-apps/python

# Pokrenite Python skriptu
python aoai-app.py
```

### Pokretanje TypeScript primjera

```bash
# Navigirajte do direktorija TypeScript aplikacije
cd 06-text-generation-apps/typescript/recipe-app

# Izgradite TypeScript kod
npm run build

# Pokrenite aplikaciju
npm start
```

### Pokretanje Jupyter bilježnica

```bash
# Pokrenite Jupyter u korijenu spremišta
jupyter notebook

# Ili koristite VS Code s Jupyter ekstenzijom
```

### Rad s različitim vrstama lekcija

- **Lekcije "Uči"**: Fokusirane na README.md dokumentaciju i koncepte
- **Lekcije "Gradi"**: Uključuju funkcionalne primjere koda u Pythonu i TypeScriptu
- Svaka lekcija ima README.md s teorijom, prolazima kroz kod i linkovima na video sadržaj

## Smjernice za stil koda

### Python

- Koristite `python-dotenv` za upravljanje varijablama okruženja
- Importajte `openai` biblioteku za API interakcije
- Koristite `pylint` za lintanje (neki primjeri uključuju `# pylint: disable=all` radi jednostavnosti)
- Slijedite PEP 8 konvencije imenovanja
- Pohranite API podatke u `.env` datoteku, nikada u kod

### TypeScript

- Koristite `dotenv` paket za varijable okruženja
- Konfiguracija TypeScript-a u `tsconfig.json` za svaku aplikaciju
- Koristite `openai` paket za Azure OpenAI (usmjerite klijenta na `/openai/v1/` endpoint i pozovite `client.responses.create`); koristite `@azure-rest/ai-inference` za Microsoft Foundry modele
- Koristite `nodemon` za razvoj s automatskim reloadom
- Izgradite prije pokretanja: `npm run build` zatim `npm start`

### Opće konvencije

- Držite primjere koda jednostavnim i edukativnim
- Uključite komentare koji objašnjavaju ključne koncepte
- Kod svake lekcije treba biti samostalan i izvršiv
- Koristite dosljedna imena: prefiks `aoai-` za Azure OpenAI, `oai-` za OpenAI API, `githubmodels-` za Microsoft Foundry modele (naslijeđeni prefiks iz ere GitHub modela)

## Smjernice za dokumentaciju

### Markdown stil

- Svi URL-ovi moraju biti u `[tekst](../../url)` formatu bez dodatnih razmaka
- Relativni linkovi moraju počinjati s `./` ili `../`
- Svi linkovi na Microsoft domene moraju imati tracking ID: `?WT.mc_id=academic-105485-koreyst`
- Bez zemljopisnih lokalizacija u URL-ovima (izbjegavajte `/en-us/`)
- Slike pohranjene u `./images` direktoriju s opisnim imenima
- Koristite engleske znakove, brojeve i crtice u imenima datoteka

### Podrška za prijevod

- Spremište podržava 40+ jezika putem automatiziranih GitHub Actions
- Prijevodi se pohranjuju u direktorij `translations/`
- Ne šaljite djelomične prijevode
- Strojni prijevodi nisu prihvaćeni
- Prevedene slike pohranjene u direktoriju `translated_images/`

## Testiranje i validacija

### Provjere prije predaje

Ovo spremište koristi GitHub Actions za validaciju. Prije predaje PR-ova:

1. **Provjerite Markdown linkove**:
   ```bash
   # Radni tijek validate-markdown.yml provjerava:
   # - Pokvarene relativne putanje
   # - Nedostajuće ID-ove za praćenje na putanjama
   # - Nedostajuće ID-ove za praćenje na URL-ovima
   # - URL-ove s lokalizacijom zemlje
   # - Pokvarene vanjske URL-ove
   ```

2. **Ručno testiranje**:
   - Testirajte Python primjere: aktivirajte venv i pokrenite skripte
   - Testirajte TypeScript primjere: `npm install`, `npm run build`, `npm start`
   - Provjerite jesu li varijable okruženja ispravno postavljene
   - Provjerite rade li API ključevi s primjerima koda

3. **Primjeri koda**:
   - Osigurajte da sav kod radi bez pogrešaka
   - Testirajte s Azure OpenAI i OpenAI API-jem gdje je primjenjivo
   - Provjerite rade li primjeri s Microsoft Foundry modelima gdje su podržani

### Nema automatiziranih testova

Ovo je edukativno spremište usmjereno na tutorijale i primjere. Nema jedinicnih ni integracijskih testova za pokretanje. Validacija uključuje prvenstveno:
- Ručno testiranje primjera koda
- GitHub Actions za validaciju Markdowna
- Pregled edukativnog sadržaja zajednice

## Smjernice za Pull Requestove

### Prije predaje

1. Testirajte promjene koda u Pythonu i TypeScriptu kad je primjenjivo
2. Pokrenite validaciju Markdowna (automatski aktivirana na PR-u)
3. Provjerite da su tracking ID-ovi prisutni na svim Microsoft URL-ovima
4. Provjerite da relativni linkovi vrijede
5. Provjerite da su slike ispravno referencirane

### Format naslova PR-a

- Koristite opisne naslove: `[Lesson 06] Popravak tipfelera u Python primjeru` ili `Ažuriraj README za lekciju 08`
- Reference na brojeve problema kad je primjenjivo: `Fixes #123`

### Opis PR-a

- Objasnite što je promijenjeno i zašto
- Povežite se na povezane probleme
- Za izmjene koda, navedite koji su primjeri testirani
- Za prijevode PR-ove, uključite sve datoteke za potpuni prijevod

### Zahtjevi za doprinos

- Potpišite Microsoft CLA (automatski pri prvom PR-u)
- Forkajte spremište na svoj račun prije promjena
- Jedan PR po logičnoj promjeni (nemojte kombinirati nepovezane ispravke)
- Držite PR-ove fokusiranima i malima kad je moguće

## Uobičajeni radni tijekovi

### Dodavanje novog primjera koda

1. Navigirajte do odgovarajućeg direktorija lekcije
2. Kreirajte primjer u poddirektoriju `python/` ili `typescript/`
3. Slijedite konvenciju imenovanja: `{provider}-{example-name}.{py|ts|js}`
4. Testirajte s stvarnim API vjerodajnicama
5. Dokumentirajte nove varijable okruženja u README lekcije

### Ažuriranje dokumentacije

1. Uredite README.md u direktoriju lekcije
2. Slijedite Markdown smjernice (tracking ID-jevi, relativni linkovi)
3. Ažuriranja prijevoda upravlja GitHub Actions (nemojte ih uređivati ručno)
4. Testirajte da su svi linkovi validni

### Rad s Dev kontejnerima

1. Spremište uključuje `.devcontainer/devcontainer.json`
2. Post-create skripta automatski instalira Python ovisnosti
3. Ekstenzije za Python i Jupyter su unaprijed konfigurirane
4. Okruženje je bazirano na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deploy i objavljivanje

Ovo je edukativno spremište - nema procesa deploya. Kurikulum se koristi kroz:

1. **GitHub spremište**: Direktan pristup kodu i dokumentaciji
2. **GitHub Codespaces**: Instant razvojno okruženje s unaprijed konfiguriranim setupom
3. **Microsoft Learn**: Sadržaj se može distribuirati na službenu platformu za učenje
4. **docsify**: Stranica dokumentacije izrađena iz Markdowna (pogledajte `docsifytopdf.js` i `package.json`)

### Izgradnja stranice dokumentacije

```bash
# Generiraj PDF iz dokumentacije (ako je potrebno)
npm run convert
```

## Otklanjanje poteškoća

### Uobičajeni problemi

**Python greške u uvozu**:
- Provjerite je li virtualno okruženje aktivirano
- Pokrenite `pip install -r requirements.txt`
- Provjerite da je verzija Pythona 3.9+

**Greške prilikom builda TypeScripta**:
- Pokrenite `npm install` u specifičnom direktoriju aplikacije
- Provjerite kompatibilnost verzije Node.js
- Očistite `node_modules` i ponovno instalirajte ako je potrebno

**Greške kod autentikacije API-ja**:
- Provjerite postoji li `.env` datoteka i ima li točne vrijednosti
- Provjerite jesu li API ključevi valjani i nisu istekli
- Provjerite ispravnost URL-ova endpointa za vaš regiju

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
- [Kolekcija naprednih primjera koda](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Napomene specifične za projekt

- Ovo je **edukativno spremište** usmjereno na učenje, a ne produkcijski kod
- Primjeri su namjerno jednostavni i usredotočeni na podučavanje koncepata
- Kvaliteta koda je izbalansirana s edukativnom jasnoćom
- Svaka lekcija je samostalna i može se dovršiti neovisno
- Spremište podržava više pružatelja API-ja: Azure OpenAI, OpenAI, Microsoft Foundry modeli i offline pružatelje poput Foundry Local i Ollama
- Sadržaj je višejezičan s automatiziranim radnim tijekovima za prijevod
- Aktivna zajednica na Discordu za pitanja i podršku

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->