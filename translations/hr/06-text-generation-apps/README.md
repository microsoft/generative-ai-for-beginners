<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T17:25:25+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "hr"
}
-->
# Izgradnja aplikacija za generiranje teksta

> _(Kliknite na sliku iznad za pregled videa ove lekcije)_

Do sada ste kroz ovaj kurikulum vidjeli da postoje osnovni koncepti kao što su promptovi i čak cijela disciplina zvana "inženjering promptova". Mnogi alati s kojima možete komunicirati, kao što su ChatGPT, Office 365, Microsoft Power Platform i drugi, podržavaju korištenje promptova za postizanje nečega.

Da biste dodali takvo iskustvo u aplikaciju, trebate razumjeti koncepte kao što su promptovi, dovršetci i odabrati biblioteku s kojom ćete raditi. To je upravo ono što ćete naučiti u ovom poglavlju.

## Uvod

U ovom poglavlju ćete:

- Naučiti o openai biblioteci i njenim osnovnim konceptima.
- Izgraditi aplikaciju za generiranje teksta koristeći openai.
- Razumjeti kako koristiti koncepte kao što su prompt, temperatura i tokeni za izgradnju aplikacije za generiranje teksta.

## Ciljevi učenja

Na kraju ove lekcije, moći ćete:

- Objasniti što je aplikacija za generiranje teksta.
- Izgraditi aplikaciju za generiranje teksta koristeći openai.
- Konfigurirati vašu aplikaciju da koristi više ili manje tokena i također promijeniti temperaturu, za raznolik izlaz.

## Što je aplikacija za generiranje teksta?

Obično kada gradite aplikaciju ona ima neku vrstu sučelja kao što je sljedeće:

- Temeljeno na naredbama. Konzolne aplikacije su tipične aplikacije gdje upisujete naredbu i ona izvršava zadatak. Na primjer, `git` je aplikacija temeljena na naredbama.
- Korisničko sučelje (UI). Neke aplikacije imaju grafička korisnička sučelja (GUI) gdje klikate gumbe, unosite tekst, birate opcije i više.

### Konzolne i UI aplikacije su ograničene

Usporedite to s aplikacijom temeljeno na naredbama gdje upisujete naredbu:

- **Ograničeno je**. Ne možete jednostavno upisati bilo koju naredbu, samo one koje aplikacija podržava.
- **Jezično specifično**. Neke aplikacije podržavaju mnoge jezike, ali po defaultu aplikacija je izgrađena za specifičan jezik, čak i ako možete dodati podršku za više jezika.

### Prednosti aplikacija za generiranje teksta

Kako se aplikacija za generiranje teksta razlikuje?

U aplikaciji za generiranje teksta imate više fleksibilnosti, niste ograničeni na set naredbi ili specifičan ulazni jezik. Umjesto toga, možete koristiti prirodni jezik za interakciju s aplikacijom. Još jedna prednost je ta što već komunicirate s izvorom podataka koji je treniran na velikom korpusu informacija, dok bi tradicionalna aplikacija mogla biti ograničena na ono što je u bazi podataka.

### Što mogu izgraditi s aplikacijom za generiranje teksta?

Postoji mnogo stvari koje možete izgraditi. Na primjer:

- **Chatbot**. Chatbot koji odgovara na pitanja o temama, kao što su vaša tvrtka i njezini proizvodi, mogao bi biti dobar izbor.
- **Pomoćnik**. LLM-ovi su izvrsni u stvarima kao što su sažimanje teksta, dobivanje uvida iz teksta, proizvodnja teksta poput životopisa i više.
- **Asistent za kod**. Ovisno o jezičnom modelu koji koristite, možete izgraditi asistenta za kod koji vam pomaže pisati kod. Na primjer, možete koristiti proizvod poput GitHub Copilot kao i ChatGPT da vam pomognu pisati kod.

## Kako mogu započeti?

Pa, trebate pronaći način za integraciju s LLM-om što obično podrazumijeva sljedeća dva pristupa:

- Koristite API. Ovdje konstruirate web zahtjeve sa svojim promptom i dobivate generirani tekst nazad.
- Koristite biblioteku. Biblioteke pomažu u kapsuliranju API poziva i olakšavaju njihovo korištenje.

## Biblioteke/SDK-ovi

Postoji nekoliko dobro poznatih biblioteka za rad s LLM-ovima kao što su:

- **openai**, ova biblioteka olakšava povezivanje s vašim modelom i slanje promptova.

Zatim postoje biblioteke koje djeluju na višoj razini kao što su:

- **Langchain**. Langchain je dobro poznat i podržava Python.
- **Semantic Kernel**. Semantic Kernel je biblioteka od Microsofta koja podržava jezike C#, Python i Java.

## Prva aplikacija koristeći openai

Pogledajmo kako možemo izgraditi našu prvu aplikaciju, koje biblioteke trebamo, koliko je potrebno i tako dalje.

### Instalirajte openai

Postoji mnogo biblioteka vani za interakciju s OpenAI ili Azure OpenAI. Moguće je koristiti brojne programske jezike kao što su C#, Python, JavaScript, Java i više. Odabrali smo koristiti `openai` Python biblioteku, pa ćemo koristiti `pip` za instalaciju.

### Kreirajte resurs

Trebate provesti sljedeće korake:

- Kreirajte račun na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Dobijte pristup Azure OpenAI. Idite na [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) i zatražite pristup.

  > [!NOTE]
  > U vrijeme pisanja, trebate se prijaviti za pristup Azure OpenAI.

- Instalirajte Python <https://www.python.org/>
- Kreirajte Azure OpenAI Service resurs. Pogledajte ovaj vodič kako [kreirati resurs](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Locirajte API ključ i endpoint

U ovom trenutku, trebate reći svojoj `openai` biblioteci koji API ključ koristiti. Da biste pronašli svoj API ključ, idite na sekciju "Keys and Endpoint" vašeg Azure OpenAI resursa i kopirajte vrijednost "Key 1".

Sada kada imate ove informacije kopirane, uputimo biblioteke da ih koriste.

> [!NOTE]
> Vrijedi odvojiti vaš API ključ od koda. Možete to učiniti koristeći varijable okruženja.

### Postavljanje konfiguracije Azure

Ako koristite Azure OpenAI, evo kako postaviti konfiguraciju:

Gore postavljamo sljedeće:

U gornjem kodu, kreiramo objekt dovršetka i prosljeđujemo model koji želimo koristiti i prompt. Zatim ispisujemo generirani tekst.

### Dovršetci za chat

Do sada ste vidjeli kako smo koristili `Completion` to generate text. But there's another class called `ChatCompletion` koji je više prikladan za chatbote. Evo primjera korištenja:

Više o ovoj funkcionalnosti u nadolazećem poglavlju.

## Vježba - vaša prva aplikacija za generiranje teksta

Sada kada smo naučili kako postaviti i konfigurirati openai, vrijeme je da izgradite svoju prvu aplikaciju za generiranje teksta. Da biste izgradili svoju aplikaciju, slijedite ove korake:

1. Kreirajte virtualno okruženje i instalirajte openai:

   > [!NOTE]
   > Ako koristite Windows upišite `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` vrijednost.

1. Kreirajte _app.py_ datoteku i dodajte joj sljedeći kod:

   > [!NOTE]
   > Ako koristite Azure OpenAI, trebate postaviti `api_type` to `azure` and set the `api_key` na vaš Azure OpenAI ključ.

   Trebali biste vidjeti izlaz kao sljedeći:

## Različite vrste promptova, za različite stvari

Sada ste vidjeli kako generirati tekst koristeći prompt. Čak imate program koji radi i koji možete modificirati i promijeniti kako biste generirali različite vrste teksta.

Promptovi se mogu koristiti za sve vrste zadataka. Na primjer:

- **Generirajte vrstu teksta**. Na primjer, možete generirati pjesmu, pitanja za kviz itd.
- **Pretraživanje informacija**. Možete koristiti promptove za traženje informacija kao što je sljedeći primjer 'Što znači CORS u web razvoju?'.
- **Generiranje koda**. Možete koristiti promptove za generiranje koda, na primjer razvijanje regularnog izraza koji se koristi za validaciju emailova ili zašto ne generirati cijeli program, kao web aplikaciju?

## Praktičniji slučaj: generator recepata

Zamislite da imate sastojke kod kuće i želite kuhati nešto. Za to vam je potreban recept. Način da pronađete recepte je korištenje tražilice ili možete koristiti LLM da to učinite.

Možete napisati prompt ovako:

> "Prikaži mi 5 recepata za jelo sa sljedećim sastojcima: piletina, krumpiri i mrkva. Po receptu, navedi sve korištene sastojke"

S obzirom na gornji prompt, mogli biste dobiti odgovor sličan:

Ovaj rezultat je izvrstan, znam što kuhati. U ovom trenutku, što bi moglo biti korisno poboljšanje su:

- Filtriranje sastojaka koje ne volim ili na koje sam alergičan.
- Izrada popisa za kupovinu, u slučaju da nemam sve sastojke kod kuće.

Za gore navedene slučajeve, dodajmo dodatni prompt:

> "Molim te ukloni recepte s češnjakom jer sam alergičan i zamijeni ga nečim drugim. Također, molim te izradi popis za kupovinu za recepte, uzimajući u obzir da već imam piletinu, krumpire i mrkvu kod kuće."

Sada imate novi rezultat, naime:

To je vaših pet recepata, bez spominjanja češnjaka i također imate popis za kupovinu uzimajući u obzir ono što već imate kod kuće.

## Vježba - izgradite generator recepata

Sada kada smo izložili scenarij, napišimo kod koji odgovara prikazanom scenariju. Da bismo to učinili, slijedite ove korake:

1. Koristite postojeću _app.py_ datoteku kao početnu točku
1. Locirajte `prompt` varijablu i promijenite njen kod u sljedeći:

   Ako sada pokrenete kod, trebali biste vidjeti izlaz sličan:

   > NOTE, vaš LLM je nedeterministički, tako da možete dobiti različite rezultate svaki put kada pokrenete program.

   Odlično, pogledajmo kako možemo poboljšati stvari. Da bismo poboljšali stvari, želimo biti sigurni da je kod fleksibilan, tako da se sastojci i broj recepata mogu poboljšati i promijeniti.

1. Promijenimo kod na sljedeći način:

   Uzimajući kod za testiranje, mogao bi izgledati ovako:

### Poboljšajte dodavanjem filtra i popisa za kupovinu

Sada imamo radnu aplikaciju sposobnu za proizvodnju recepata i fleksibilna je jer se oslanja na ulaze korisnika, kako na broj recepata, tako i na korištene sastojke.

Da bismo to dodatno poboljšali, želimo dodati sljedeće:

- **Filtrirajte sastojke**. Želimo biti sposobni filtrirati sastojke koje ne volimo ili na koje smo alergični. Da bismo postigli ovu promjenu, možemo urediti naš postojeći prompt i dodati uvjet filtra na kraj ovako:

  Gore dodajemo `{filter}` na kraj prompta i također hvatamo vrijednost filtra od korisnika.

  Primjer ulaza prilikom pokretanja programa sada može izgledati ovako:

  Kao što možete vidjeti, svi recepti s mlijekom su filtrirani. Ali, ako ste netolerantni na laktozu, možda želite filtrirati recepte s sirom također, tako da postoji potreba da budete jasni.

- **Izradite popis za kupovinu**. Želimo izraditi popis za kupovinu, uzimajući u obzir ono što već imamo kod kuće.

  Za ovu funkcionalnost, mogli bismo pokušati riješiti sve u jednom promptu ili bismo mogli podijeliti na dva prompta. Pokušajmo pristup drugog. Ovdje predlažemo dodavanje dodatnog prompta, ali da bi to funkcioniralo, trebamo dodati rezultat prvog prompta kao kontekst za drugi prompt.

  Locirajte dio u kodu koji ispisuje rezultat prvog prompta i dodajte sljedeći kod ispod:

  Obratite pažnju na sljedeće:

  1. Konstruiramo novi prompt dodavanjem rezultata iz prvog prompta u novi prompt:

  1. Radimo novi zahtjev, ali također uzimajući u obzir broj tokena koje smo zatražili u prvom promptu, pa ovaj put kažemo `max_tokens` je 1200.

     Uzimajući ovaj kod za testiranje, sada dolazimo do sljedećeg izlaza:

## Poboljšajte svoju postavku

Ono što imamo do sada je kod koji radi, ali postoje neki pomaci koje bismo trebali učiniti da bismo dodatno poboljšali stvari. Neke stvari koje bismo trebali učiniti su:

- **Odvojite tajne od koda**, kao što je API ključ. Tajne ne pripadaju kodu i trebale bi biti pohranjene na sigurnom mjestu. Da biste odvojili tajne od koda, možete koristiti varijable okruženja i biblioteke kao `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` datoteku sa sljedećim sadržajem:

     > Napomena, za Azure, trebate postaviti sljedeće varijable okruženja:

     U kodu, učitali biste varijable okruženja ovako:

- **Riječ o duljini tokena**. Trebali bismo razmotriti koliko tokena trebamo generirati tekst koji želimo. Tokeni koštaju novac, pa gdje je moguće, trebali bismo pokušati biti ekonomični s brojem tokena koje koristimo. Na primjer, možemo li formulirati prompt tako da možemo koristiti manje tokena?

  Da biste promijenili korištene tokene, možete koristiti `max_tokens` parametar. Na primjer, ako želite koristiti 100 tokena, učinili biste:

- **Eksperimentiranje s temperaturom**. Temperatura je nešto što nismo spomenuli do sada, ali je važan kontekst za način na koji naš program radi. Što je veća vrijednost temperature, to će izlaz biti slučajniji. Suprotno tome, što je niža vrijednost temperature, to će izlaz biti predvidljiviji. Razmislite želite li varijaciju u vašem izlazu ili ne.

  Da biste promijenili temperaturu, možete koristiti `temperature` parametar. Na primjer, ako želite koristiti temperaturu od 0.5, učinili biste:

  > Napomena, što bliže 1.0, to je izlaz raznolikiji.

## Zadatak

Za ovaj zadatak, možete odabrati što želite izgraditi.

Evo nekoliko prijedloga:

- Poboljšajte aplikaciju za generiranje recepata kako biste je dodatno poboljšali. Igrajte se s vrijednostima temperature i promptovima da vidite što možete smisliti.
- Izgradite "study buddy". Ova aplikacija bi trebala biti sposobna odgovarati na pitanja o temi, na primjer Python, mogli biste imati promptove poput "Što je određena tema u Pythonu?", ili biste mogli imati prompt koji kaže, prikaži mi kod za određenu temu itd.
- Povijesni bot, oživite povijest, uputite bota da igra određenog povijesnog lika i postavite mu pitanja o njegovom životu i vremenu.

## Rješenje

### Study buddy

Ispod je početni prompt, pogledajte kako ga možete koristiti i prilagoditi po svojoj želji.

### Povijesni bot

Evo nekih promptova koje biste mogli koristiti:

## Provjera znanja

Što radi koncept temperature?

1. Kontrolira koliko je izlaz slučajan.
1. Kontrolira koliko je velik odgovor.
1. Kontrolira koliko tokena se koristi.

## 🚀 Izazov

Kada radite na zadatku, pokušajte varirati temperaturu, pokušajte je postaviti na 0, 0.5 i 1. Zapamtite da je 0 najmanje varijabilan, a 1 najviše, koja vrijednost najbolje odgovara vašoj aplikaciji?

## Odličan rad! Nastavite s učenjem

Nakon završetka ove lekcije, pogledajte našu [kolekciju za učenje generativnog AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili s povećanjem svog znanja o generativnom AI!

Idite na Lekciju 7 gdje ćemo pogledati kako [izgraditi chat aplikacije](../07-building-chat-applications

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako se trudimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.