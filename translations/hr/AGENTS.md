# AGENTS.md

## Pregled Projekta

Ovo spremište sadrži sveobuhvatan kurikulum od 21 lekcije koji podučava osnove Generativne AI i razvoj aplikacija. Tečaj je namijenjen početnicima i obuhvaća sve, od osnovnih koncepata do izgradnje aplikacija spremnih za proizvodnju.

**Ključne tehnologije:**
- Python 3.9+ s bibliotekama: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript s Node.js i bibliotekama: `openai` (Azure OpenAI preko v1 krajnje točke + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry modeli)
- Azure OpenAI Service, OpenAI API i Microsoft Foundry modeli (GitHub Models se povlače krajem srpnja 2026)
- Jupyter bilježnice za interaktivno učenje
- Dev Containers za dosljedno razvojno okruženje

**Struktura spremišta:**
- 21 direktorij označenih lekcija (00-21) s README datotekama, primjerima koda i zadacima
- Višestruke implementacije: Python, TypeScript i ponekad .NET primjeri
- Direktorij prijevoda s 40+ jezičnih verzija
- Centralizirana konfiguracija putem `.env` datoteke (koristite `.env.copy` kao predložak)

## Komande za postavljanje

### Inicijalno postavljanje spremišta

```bash
# Klonirajte spremište
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopirajte predložak okoline
cp .env.copy .env
# Uredite .env sa svojim API ključevima i krajnjim točkama
```

### Postavljanje Python okruženja

```bash
# Kreirajte virtualno okruženje
python3 -m venv venv

# Aktivirajte virtualno okruženje
# Na macOS/Linux:
source venv/bin/activate
# Na Windows:
venv\Scripts\activate

# Instalirajte ovisnosti
pip install -r requirements.txt
```

### Postavljanje Node.js/TypeScript okruženja

```bash
# Instalirajte ovisnosti na root razini (za alate za dokumentaciju)
npm install

# Za pojedinačne TypeScript primjere lekcija, idite na specifičnu lekciju:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Postavljanje Dev Container-a (Preporučeno)

Spremište uključuje `.devcontainer` konfiguraciju za GitHub Codespaces ili VS Code Dev Containers:

1. Otvorite spremište u GitHub Codespaces ili VS Code s Dev Containers ekstenzijom
2. Dev Container će automatski:
   - Instalirati Python ovisnosti iz `requirements.txt`
   - Pokrenuti post-create skriptu (`.devcontainer/post-create.sh`)
   - Postaviti Jupyter kernel

## Razvojni tok rada

### Varijable okruženja

Sve lekcije koje zahtijevaju pristup API-ju koriste varijable okruženja definirane u `.env`:

- `OPENAI_API_KEY` - Za OpenAI API
- `AZURE_OPENAI_API_KEY` - Za Azure OpenAI u Microsoft Foundry (Azure OpenAI Service je sada dio Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL Azure OpenAI krajnje točke (Foundry resurs krajnja točka)
- `AZURE_OPENAI_DEPLOYMENT` - Naziv implementacije modela chat dovršetka (zadano za tečaj: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Naziv implementacije modela za ugradnje (zadano za tečaj: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Verzija API-ja (zadano: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Za Hugging Face modele
- `AZURE_INFERENCE_ENDPOINT` - Krajnja točka Microsoft Foundry modela (katalog modela s više pružatelja)
- `AZURE_INFERENCE_CREDENTIAL` - API ključ Microsoft Foundry modela (zamjenjuje povlačeći `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - Model bez rezoniranja (npr. `Llama-3.3-70B-Instruct`) koji koriste `temperature` primjeri, jer modeli s rezoniranjem ne podržavaju kontrole uzorkovanja

### Konvencije modela (važno)

- **Zadani model za chat je `gpt-5-mini`** - trenutačni, ne-povlačeni **model s rezoniranjem**. Od 2026 stariji modeli "mini" s podrškom za temperaturu (`gpt-4o-mini`, `gpt-4.1-mini`) se *povlače*, pa kurikulum standardizira GPT-5 obitelj.
- **Modeli s rezoniranjem odbacuju `temperature` i `top_p`**, te koriste `max_output_tokens` (Responses API) / `max_completion_tokens` (chat dovršetci) umjesto `max_tokens`. Nemojte dodavati `temperature`/`top_p`/`max_tokens` uzorkima koji pozivaju `gpt-5-mini`.
- **Za demonstraciju `temperature`**, primjeri koriste **Llama** model (`Llama-3.3-70B-Instruct`) putem Microsoft Foundry Models krajnje točke (`AZURE_INFERENCE_CHAT_MODEL`). Upravljajte modelima s rezoniranjem pomoću inženjeringa poticaja + kontrola rezoniranja umjesto kontrola uzorkovanja.
- **Fino podešavanje (lekcija 18)** zadržava `gpt-4.1-mini`: GPT-5 podržava samo finu usavršavanje putem pojačanja (RFT), ne nadzirano fino podešavanje (SFT) prikazano tamo.
- Lekcije 20 (Mistral) i 21 (Meta) zadržavaju `temperature`/`max_tokens` jer ciljaju Mistral/Llama modele koji to podržavaju.

### Pokretanje Python Primjera

```bash
# Navigirajte do direktorija lekcije
cd 06-text-generation-apps/python

# Pokrenite Python skriptu
python aoai-app.py
```

### Pokretanje TypeScript Primjera

```bash
# Navigirajte do direktorija TypeScript aplikacije
cd 06-text-generation-apps/typescript/recipe-app

# Izgradite TypeScript kod
npm run build

# Pokrenite aplikaciju
npm start
```

### Pokretanje Jupyter Bilježnica

```bash
# Pokrenite Jupyter u korijenu repozitorija
jupyter notebook

# Ili koristite VS Code s Jupyter proširenjem
```

### Rad sa različitim tipovima lekcija

- **"Learn" lekcije**: Fokus na dokumentaciju README.md i koncepte
- **"Build" lekcije**: Uključuju radne primjere koda u Python i TypeScript
- Svaka lekcija ima README.md s teorijom, pregledima koda i poveznicama na video sadržaj

## Smjernice za stil koda

### Python

- Koristite `python-dotenv` za upravljanje varijablama okruženja
- Uvezite `openai` biblioteku za interakcije s API-jem
- Koristite `pylint` za linting (neki primjeri uključuju `# pylint: disable=all` za jednostavnost)
- Slijedite PEP 8 pravila imenovanja
- Spremite API vjerodajnice u `.env` datoteku, nikad u kod

### TypeScript

- Koristite `dotenv` paket za varijable okruženja
- TypeScript konfiguracija u `tsconfig.json` za svaku aplikaciju
- Koristite `openai` paket za Azure OpenAI (usmjerite klijenta na `/openai/v1/` krajnju točku i pozovite `client.responses.create`); koristite `@azure-rest/ai-inference` za Microsoft Foundry modele
- Koristite `nodemon` za razvoj s automatskim ponovnim učitavanjem
- Gradite prije pokretanja: `npm run build` zatim `npm start`

### Opće konvencije

- Držite primjere koda jednostavnim i edukativnim
- Uključite komentare koji objašnjavaju ključne koncepte
- Kod svake lekcije treba biti samostalan i može se pokrenuti
- Koristite dosljedno imenovanje: prefiks `aoai-` za Azure OpenAI, `oai-` za OpenAI API, `githubmodels-` za Microsoft Foundry modele (naslijeđeni prefiks iz GitHub Models ere)

## Smjernice za dokumentaciju

### Stil Markdowna

- Sve URL adrese moraju biti u `[text](../../url)` formatu bez dodatnih razmaka
- Relativne poveznice moraju početi s `./` ili `../`
- Sve poveznice na Microsoft domene moraju uključivati ID praćenja: `?WT.mc_id=academic-105485-koreyst`
- Bez lokalizacija specifičnih za države u URL-ovima (izbjegavajte `/en-us/`)
- Slike pohranjene u `./images` mapi s opisnim imenima
- Koristite engleske znakove, brojeve i crtice u nazivima datoteka

### Podrška za prijevode

- Spremište podržava 40+ jezika preko automatiziranih GitHub Actions
- Prijevodi pohranjeni u `translations/` direktoriju
- Nemojte predavati djelomične prijevode
- Strojni prijevodi se ne prihvaćaju
- Prevedene slike pohranjene u `translated_images/` direktoriju

## Testiranje i validacija

### Provjere prije predaje

Ovo spremište koristi GitHub Actions za validaciju. Prije predaje PR-ova:

1. **Provjerite Markdown poveznice**:
   ```bash
   # Radni tok validate-markdown.yml provjerava:
   # - Pokvarene relativne putanje
   # - Nedostajući ID-evi za praćenje na putanjama
   # - Nedostajući ID-evi za praćenje na URL-ovima
   # - URL-ovi s lokalizacijom zemlje
   # - Pokvareni vanjski URL-ovi
   ```

2. **Ručna testiranja**:
   - Testirajte Python primjere: Aktivirajte venv i pokrenite skripte
   - Testirajte TypeScript primjere: `npm install`, `npm run build`, `npm start`
   - Provjerite da su varijable okruženja ispravno konfigurirane
   - Provjerite da API ključevi rade s primjerima koda

3. **Primjeri koda**:
   - Osigurajte da sav kod radi bez pogrešaka
   - Testirajte s Azure OpenAI i OpenAI API-jem gdje je primjenjivo
   - Provjerite da primjeri funkcioniraju s Microsoft Foundry modelima gdje su podržani

### Nema automatiziranih testova

Ovo je edukativno spremište fokusirano na tutorijale i primjere. Nema jediničnih ili integracijskih testova za pokretanje. Validacija je prvenstveno:
- Ručno testiranje primjera koda
- GitHub Actions za Markdown validaciju
- Pregled zajednice edukativnog sadržaja

## Smjernice za Pull Requestove

### Prije predavanja

1. Testirajte izmjene koda u Pythonu i TypeScriptu gdje je primjenjivo
2. Pokrenite provjeru Markdowna (automatski pokrenuto prilikom PR-a)
3. Osigurajte da su ID-jevi praćenja prisutni na svim Microsoft URL-ovima
4. Provjerite jesu li relativne poveznice valjane
5. Provjerite jesu li slike pravilno referencirane

### Format Naslova PR-a

- Koristite opisne naslove: `[Lesson 06] Popravi tipfeler u Python primjeru` ili `Ažuriraj README za lekciju 08`
- Referencirajte brojeve problema gdje je primjenjivo: `Popravljeno #123`

### Opis PR-a

- Objasnite što je promijenjeno i zašto
- Povežite povezane probleme
- Za promjene koda, navedite koji su primjeri testirani
- Za PR-ove prijevoda, uključite sve datoteke za potpun prijevod

### Zahtjevi za doprinos

- Potpišite Microsoft CLA (automatski pri prvom PR-u)
- Forkajte spremište na svoj račun prije mijenjanja
- Jedan PR po logičnoj izmjeni (nemojte spajati nepovezane ispravke)
- Držite PR-ove fokusirane i male kad je moguće

## Uobičajeni radni tokovi

### Dodavanje novog primjera koda

1. Navigirajte do odgovarajućeg direktorija lekcije
2. Napravite primjer u `python/` ili `typescript/` poddirektoriju
3. Slijedite konvenciju imenovanja: `{provider}-{example-name}.{py|ts|js}`
4. Testirajte s pravim API vjerodajnicama
5. Dokumentirajte sve nove varijable okruženja u README lekcije

### Ažuriranje dokumentacije

1. Uredite README.md u direktoriju lekcije
2. Slijedite Markdown smjernice (ID-jevi praćenja, relativne poveznice)
3. Ažuriranja prijevoda obrađuju GitHub Actions (nemojte ručno uređivati)
4. Testirajte da su sve poveznice valjane

### Rad s Dev Container-ima

1. Spremište uključuje `.devcontainer/devcontainer.json`
2. Post-create skripta automatski instalira Python ovisnosti
3. Ekstenzije za Python i Jupyter su unaprijed konfigurirane
4. Okruženje je bazirano na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deploy i objavljivanje

Ovo je spremište za učenje - nema procesa objavljivanja. Kurikulum se koristi kroz:

1. **GitHub spremište**: izravan pristup kodu i dokumentaciji
2. **GitHub Codespaces**: trenutno razvojno okruženje s unaprijed konfiguriranim postavkama
3. **Microsoft Learn**: sadržaj se može distribuirati na službenu platformu za učenje
4. **docsify**: stranica dokumentacije izgrađena od Markdowna (pogledajte `docsifytopdf.js` i `package.json`)

### Izgradnja stranice dokumentacije

```bash
# Generiraj PDF iz dokumentacije (ako je potrebno)
npm run convert
```

## Rješavanje problema

### Uobičajeni problemi

**Pogreške uvoza u Pythonu**:
- Provjerite je li virtualno okruženje aktivirano
- Pokrenite `pip install -r requirements.txt`
- Provjerite verziju Pythona je 3.9+

**Pogreške pri izgradnji TypeScripta**:
- Pokrenite `npm install` u specifičnom direktoriju aplikacije
- Provjerite je li verzija Node.js kompatibilna
- Obrišite `node_modules` i ponovno instalirajte ako je potrebno

**Pogreške autentifikacije API-ja**:
- Provjerite postoji li `.env` i jesu li vrijednosti točne
- Provjerite API ključeve jesu li valjani i nisu istekli
- Provjerite jesu li URL-ovi krajnjih točaka točni za vašu regiju

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

## Projekt-specifične bilješke

- Ovo je **edukativno spremište** usmjereno na učenje, a ne proizvodni kod
- Primjeri su namjerno jednostavni i fokusirani na podučavanje koncepata
- Kvaliteta koda je balansirana s edukativnom jasnoćom
- Svaka lekcija je samostalna i može se završiti neovisno
- Spremište podržava više API pružatelja: Azure OpenAI, OpenAI, Microsoft Foundry modeli i offline pružatelje poput Foundry Local i Ollama
- Sadržaj je višejezičan s automatiziranim tijekovima prijevoda
- Aktivna zajednica na Discordu za pitanja i podršku

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->