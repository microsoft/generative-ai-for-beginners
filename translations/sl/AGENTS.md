# AGENTS.md

## Pregled projekta

Ta repozitorij vsebuje obsežen kurikulum z 21 lekcijami, ki poučuje osnove generativne umetne inteligence in razvoj aplikacij. Tečaj je zasnovan za začetnike in pokriva vse od osnovnih konceptov do izdelave aplikacij za proizvodnjo.

**Ključne tehnologije:**
- Python 3.9+ z knjižnicami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript z Node.js in knjižnicami: `openai` (Azure OpenAI prek v1 končne točke + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry modeli)
- Azure OpenAI Service, OpenAI API in Microsoft Foundry modeli (GitHub modeli bodo prenehali z delovanjem konec julija 2026)
- Jupyter Notebooks za interaktivno učenje
- Dev containerji za konsistentno razvojno okolje

**Struktura repozitorija:**
- 21 oštevilčenih map z lekcijami (00-21), ki vsebujejo README-je, primere kode in naloge
- Več implementacij: Python, TypeScript in včasih .NET primeri
- Mapa za prevode z več kot 40 jezikovnimi različicami
- Centralizirana konfiguracija preko `.env` datoteke (uporabi `.env.copy` kot predlogo)

## Ukazi za nastavitev

### Začetna nastavitev repozitorija

```bash
# Klonirajte repozitorij
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopirajte predlogo okolja
cp .env.copy .env
# Uredite .env z vašimi API ključi in končnimi točkami
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

### Nastavitev Node.js/TypeScript okolja

```bash
# Namestite odvisnosti na nivoju root (za orodja za dokumentacijo)
npm install

# Za posamezne primere lekcij v TypeScriptu pojdite do določene lekcije:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Nastavitev dev containerja (priporočeno)

Repozitorij vključuje konfiguracijo `.devcontainer` za GitHub Codespaces ali VS Code Dev Containers:

1. Odpri repozitorij v GitHub Codespaces ali v VS Code z razširitvijo Dev Containers
2. Dev container bo samodejno:
   - Namestil Python odvisnosti iz `requirements.txt`
   - Zagnal skripto po ustvarjanju (`.devcontainer/post-create.sh`)
   - Nastavil Jupyter jedro

## Razvojni potek dela

### Okoljske spremenljivke

Vse lekcije, ki zahtevajo dostop do API, uporabljajo okoljske spremenljivke definirane v `.env`:

- `OPENAI_API_KEY` - Za OpenAI API
- `AZURE_OPENAI_API_KEY` - Za Azure OpenAI v Microsoft Foundry (Azure OpenAI Service je zdaj del Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL končne točke Azure OpenAI (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Ime nameščene različice modela za končni pogovor (privzeto v tečaju: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Ime nameščene različice vdelanega modela (privzeto v tečaju: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Verzija API-ja (privzeto: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Za modele Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Končna točka Microsoft Foundry modelov (katalog modelov več ponudnikov)
- `AZURE_INFERENCE_CREDENTIAL` - API ključ za Microsoft Foundry modele (zamenja upokojeni `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - Model brez sklepanja (npr. `Llama-3.3-70B-Instruct`), ki ga uporabljajo primeri z `temperature`, ker modeli s sklepanjem ne podpirajo nadzora vzorčenja

### Konvencije modelov (pomembno)

- **Privzeti model za pogovor je `gpt-5-mini`** - trenutno, neoporečen **model za sklepanje**. Od leta 2026 starejši modeli mini z nadzorom temperature (`gpt-4o-mini`, `gpt-4.1-mini`) izhajajo iz uporabe, zato se tečaj standardizira na družino GPT-5.
- **Modeli za sklepanje ne sprejemajo `temperature` in `top_p`**, uporabljajo `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) namesto `max_tokens`. **Ne dodajajte** `temperature`/`top_p`/`max_tokens` v vzorce, ki kličejo `gpt-5-mini`.
- **Za prikaz `temperature`** uporabljajo vzorci **Llama** model (`Llama-3.3-70B-Instruct`) preko Microsoft Foundry Models končne točke (`AZURE_INFERENCE_CHAT_MODEL`). Modeli za sklepanje se usmerjajo z inženiringom pozivov in nadzorom sklepanja namesto s kontrolami vzorčenja.
- **Finetuning (lekcija 18)** ohranja `gpt-4.1-mini`: GPT-5 podpira le učvrstitveni finetuning (RFT), ne pa nadzorovanega finetuninga (SFT), prikazanega tam.
- Lekciji 20 (Mistral) in 21 (Meta) ohranita `temperature`/`max_tokens`, ker ciljajo modele Mistral/Llama, ki jih podpirajo.

### Zagon Python primerov

```bash
# Pomaknite se do imenika lekcije
cd 06-text-generation-apps/python

# Zaženite Python skripto
python aoai-app.py
```

### Zagon TypeScript primerov

```bash
# Pojdite v imenik aplikacije TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Sestavite kodo TypeScript
npm run build

# Zaženite aplikacijo
npm start
```

### Zagon Jupyter novičnikov

```bash
# Zaženite Jupyter v korenski mapi repozitorija
jupyter notebook

# Ali uporabite VS Code z razširitvijo Jupyter
```

### Delo z različnimi tipi lekcij

- **Lekcije "Learn"**: Osredotočene na dokumentacijo README.md in koncepte
- **Lekcije "Build"**: Vključujejo delujoče primere kode v Python in TypeScript
- Vsaka lekcija ima README.md z teorijo, razlago kode in povezavami na video gradivo

## Smernice za stil kode

### Python

- Uporabljajte `python-dotenv` za upravljanje okoljskih spremenljivk
- Uvoz knjižnice `openai` za interakcije z API
- Uporabljajte `pylint` za preverjanje kode (nekateri primeri vsebujejo `# pylint: disable=all` za preprostost)
- Sledite konvencijam poimenovanja PEP 8
- Shranjujte API poverilnice v `.env` datoteko, nikoli v kodo

### TypeScript

- Uporabljajte paket `dotenv` za okoljske spremenljivke
- Konfiguracija TypeScript v `tsconfig.json` za vsako aplikacijo
- Uporabljajte paket `openai` za Azure OpenAI (narekujte klienta na `/openai/v1/` končno točko in pokličite `client.responses.create`); za Microsoft Foundry modele pa `@azure-rest/ai-inference`
- Uporabljajte `nodemon` za razvoj z avtomatskim ponovnim zagonom
- Gradite pred zagonom: `npm run build` nato `npm start`

### Splošne konvencije

- Ohranite primere kode preproste in izobraževalne
- Vključite komentarje, ki razlagajo ključne koncepte
- Koda vsake lekcije naj bo samostojna in zaganjljiva
- Uporabljajte konsistentno poimenovanje: predpona `aoai-` za Azure OpenAI, `oai-` za OpenAI API, `githubmodels-` za Microsoft Foundry modele (ohranjen zastareli GitHub prefix)

## Smernice za dokumentacijo

### Stil Markdown

- Vse URL-je je treba zaviti v obliko `[besedilo](../../url)` brez dodatnih presledkov
- Relativne povezave morajo začeti z `./` ali `../`
- Vse povezave do Microsoft domen morajo vključevati ID sledenja: `?WT.mc_id=academic-105485-koreyst`
- Brez jezikovno specifičnih lokacij v URL-jih (izogibajte se `/en-us/`)
- Slike shranjene v mapi `./images` z opisnimi imeni
- Uporabljajte angleške znake, številke in pomišljaje v imenih datotek

### Podpora za prevajanje

- Repozitorij podpira več kot 40 jezikov prek avtomatiziranih GitHub Actions
- Prevodi so shranjeni v mapi `translations/`
- Ne pošiljajte delnih prevodov
- Strojni prevodi niso sprejeti
- Prevedene slike so shranjene v mapi `translated_images/`

## Testiranje in validacija

### Preverjanja pred oddajo

Ta repozitorij uporablja GitHub Actions za validacijo. Pred oddajo PR-jev:

1. **Preveri Markdown povezave**:
   ```bash
   # Delovni tok validate-markdown.yml preverja:
   # - Pokvarjene relativne poti
   # - Manjkajoče sledenje ID-jev na poteh
   # - Manjkajoče sledenje ID-jev na URL-jih
   # - URL-ji z lokalizacijo države
   # - Pokvarjeni zunanji URL-ji
   ```

2. **Ročno testiranje**:
   - Testirajte Python primere: aktivirajte venv in zaženite skripte
   - Testirajte TypeScript primere: `npm install`, `npm run build`, `npm start`
   - Preverite pravilno konfiguracijo okoljskih spremenljivk
   - Preverite, ali API ključi delujejo s primeri kode

3. **Primeri kode**:
   - Zagotovite, da se vsa koda izvaja brez napak
   - Testirajte z Azure OpenAI in OpenAI API, kjer je primerno
   - Preverite, ali primeri delujejo z Microsoft Foundry modeli, kjer so podprti

### Brez avtomatiziranih testov

To je izobraževalni repozitorij, osredotočen na vodiče in primere. Ni enotnih testov ali integracijskih testov za zagon. Validacija je predvsem:
- Ročno testiranje primerov kode
- GitHub Actions za validacijo Markdowna
- Skupnostni pregled izobraževalne vsebine

## Smernice za Pull Requeste

### Pred oddajo

1. Testirajte spremembe kode v Python in TypeScript, kjer je to primerno
2. Zaženite validacijo Markdowna (samodejno sproženo ob PR)
3. Prepričajte se, da so ID-ji za sledenje prisotni na vseh Microsoft URL-jih
4. Preverite veljavnost relativnih povezav
5. Preverite pravilno referenciranje slik

### Oblika naslova PR

- Uporabljajte opisne naslove: `[Lesson 06] Popravi tipkarsko napako v Python primeru` ali `Posodobitev README za lekcijo 08`
- Navedite številke težav, kadar so povezane: `Fixes #123`

### Opis PR

- Pojasnite, kaj je bilo spremenjeno in zakaj
- Navedite povezane težave
- Za spremembe kode navedite, kateri primeri so bili testirani
- Za prevodne PR-je vključite vse datoteke za celovit prevod

### Zahteve za prispevke

- Podpišite Microsoft CLA (samodejno ob prvem PR)
- Razvejajte repozitorij na svoj račun pred spreminjanjem
- Po en PR na logično spremembo (ne združujte nepovezanih popravkov)
- PR-ji naj bodo čim bolj osredotočeni in majhni

## Pogosti delovni poteki

### Dodajanje novega primera kode

1. Pomaknite se v ustrezno mapo z lekcijo
2. Ustvarite primer v podmapi `python/` ali `typescript/`
3. Sledite konvenciji poimenovanja: `{provider}-{example-name}.{py|ts|js}`
4. Testirajte z dejanskimi API poverilnicami
5. Dokumentirajte vse nove okoljske spremenljivke v README lekcije

### Posodabljanje dokumentacije

1. Uredite README.md v mapi lekcije
2. Sledite Markdown smernicam (ID-ji za sledenje, relativne povezave)
3. Posodobitve prevodov upravlja GitHub Actions (ne urejajte ročno)
4. Preverite, da so povezave veljavne

### Delo z Dev containerji

1. Repozitorij vključuje `.devcontainer/devcontainer.json`
2. Skripta po ustvarjanju namesti odvisnosti Pythona samodejno
3. Razširitve za Python in Jupyter so vnaprej konfigurirane
4. Okolje temelji na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Implementacija in objava

To je učni repozitorij - ni procesa implementacije. Kurikulum je dostopen preko:

1. **GitHub Repozitorij**: neposreden dostop do kode in dokumentacije
2. **GitHub Codespaces**: takojšnje razvojno okolje s prednastavljeno namestitvijo
3. **Microsoft Learn**: vsebine se lahko razširijo na uradno platformo za učenje
4. **docsify**: spletno mesto dokumentacije, zgrajeno iz Markdowna (glej `docsifytopdf.js` in `package.json`)

### Izdelava spletnega mesta dokumentacije

```bash
# Ustvari PDF iz dokumentacije (če je potrebno)
npm run convert
```

## Odpravljanje težav

### Pogoste težave

**Napake pri uvozu v Pythonu**:
- Preverite, da je virtualno okolje aktivirano
- Zaženite `pip install -r requirements.txt`
- Preverite, da je različica Pythona 3.9 ali novejša

**Napake pri gradnji TypeScripta**:
- Zaženite `npm install` v ustrezni mapi aplikacije
- Preverite združljivost verzije Node.js
- Po potrebi počistite `node_modules` in ponovno namestite

**Napake pri avtentikaciji API-ja**:
- Preverite, da obstaja `.env` datoteka in da vsebuje pravilne vrednosti
- Preverite, da so API ključi veljavni in niso potekli
- Preverite pravilne URL-je končnih točk glede na vašo regijo

**Manjkajoče okoljske spremenljivke**:
- Kopirajte `.env.copy` v `.env`
- Izpolnite vse zahtevane vrednosti za lekcijo, na kateri delate
- Po posodobitvi `.env` znova zaženite aplikacijo

## Dodatni viri

- [Vodnik za nastavitev tečaja](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Smernice za prispevke](./CONTRIBUTING.md)
- [Kodeks vedenja](./CODE_OF_CONDUCT.md)
- [Varnostna politika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Zbirka naprednih primerov kode](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Opombe specifične za projekt

- To je **izobraževalni repozitorij**, namenjen učenju, ne produkcijski kodi
- Primeri so namenoma preprosti in osredotočeni na poučevanje konceptov
- Kakovost kode je uravnotežena z jasnostjo izobraževalne vsebine
- Vsaka lekcija je samostojna in se lahko dokonča neodvisno
- Repozitorij podpira več ponudnikov API: Azure OpenAI, OpenAI, Microsoft Foundry modeli in offline ponudnike, kot sta Foundry Local in Ollama
- Vsebina je večjezična z avtomatiziranimi delovnimi tokovi za prevajanje
- Aktivna skupnost na Discordu za vprašanja in podporo

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->