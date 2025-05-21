<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:52:35+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "hr"
}
-->
# Odgovorno korištenje generativne AI

> _Kliknite na sliku iznad za pregled videa ove lekcije_

Lako je biti fasciniran AI-jem, a posebno generativnom AI, ali morate razmisliti o tome kako ga koristiti odgovorno. Trebate razmotriti stvari poput osiguravanja da je izlaz pravedan, neškodljiv i više. Ovaj poglavlje ima za cilj pružiti vam navedeni kontekst, što uzeti u obzir i kako poduzeti aktivne korake za poboljšanje vašeg korištenja AI.

## Uvod

Ova lekcija će pokriti:

- Zašto biste trebali prioritizirati Odgovornu AI kada gradite aplikacije s Generativnom AI.
- Osnovne principe Odgovorne AI i kako se odnose na Generativnu AI.
- Kako primijeniti ove principe Odgovorne AI kroz strategiju i alate.

## Ciljevi učenja

Nakon završetka ove lekcije znat ćete:

- Važnost Odgovorne AI pri izgradnji aplikacija s Generativnom AI.
- Kada razmišljati i primijeniti osnovne principe Odgovorne AI pri izgradnji aplikacija s Generativnom AI.
- Koji alati i strategije su vam dostupni za primjenu koncepta Odgovorne AI.

## Principi Odgovorne AI

Uzbuđenje oko Generativne AI nikada nije bilo veće. Ovo uzbuđenje donijelo je mnogo novih programera, pažnje i financiranja u ovaj prostor. Iako je ovo vrlo pozitivno za svakoga tko želi graditi proizvode i tvrtke koristeći Generativnu AI, također je važno da postupamo odgovorno.

Kroz ovaj tečaj, fokusiramo se na izgradnju našeg startupa i našeg AI obrazovnog proizvoda. Koristit ćemo principe Odgovorne AI: Pravednost, Inkluzivnost, Pouzdanost/Sigurnost, Sigurnost i Privatnost, Transparentnost i Odgovornost. S ovim principima istražit ćemo kako se odnose na našu upotrebu Generativne AI u našim proizvodima.

## Zašto biste trebali prioritizirati Odgovornu AI

Kada gradite proizvod, uzimanje pristupa usmjerenog na ljude držeći najbolje interese vašeg korisnika u umu vodi do najboljih rezultata.

Jedinstvenost Generativne AI je njezina moć stvaranja korisnih odgovora, informacija, smjernica i sadržaja za korisnike. To se može učiniti bez mnogo ručnih koraka, što može dovesti do vrlo impresivnih rezultata. Bez odgovarajućeg planiranja i strategija, to također nažalost može dovesti do nekih štetnih rezultata za vaše korisnike, vaš proizvod i društvo u cjelini.

Pogledajmo neke (ali ne sve) od ovih potencijalno štetnih rezultata:

### Halucinacije

Halucinacije su pojam koji se koristi za opisivanje kada LLM generira sadržaj koji je ili potpuno besmislen ili nešto što znamo da je faktualno netočno na temelju drugih izvora informacija.

Uzmimo za primjer da gradimo značajku za naš startup koja omogućuje studentima da postavljaju povijesna pitanja modelu. Student postavlja pitanje `Who was the sole survivor of Titanic?`

Model generira odgovor kao što je dolje:

Ovo je vrlo samopouzdan i detaljan odgovor. Nažalost, netočan je. Čak i uz minimalno istraživanje, otkrilo bi se da je bilo više od jednog preživjelog iz katastrofe Titanica. Za studenta koji tek počinje istraživati ovu temu, ovaj odgovor može biti dovoljno uvjerljiv da se ne dovodi u pitanje i tretira kao činjenica. Posljedice ovoga mogu dovesti do toga da AI sustav bude nepouzdan i negativno utječe na reputaciju našeg startupa.

Svakom iteracijom bilo kojeg danog LLM-a, vidjeli smo poboljšanja performansi oko minimiziranja halucinacija. Čak i s ovim poboljšanjem, mi kao graditelji aplikacija i korisnici još uvijek moramo biti svjesni ovih ograničenja.

### Štetni sadržaj

Pokrijali smo u ranijem dijelu kada LLM generira netočne ili besmislene odgovore. Još jedan rizik koji moramo biti svjesni je kada model odgovara štetnim sadržajem.

Štetni sadržaj može se definirati kao:

- Pružanje uputa ili poticanje na samoozljeđivanje ili ozljeđivanje određenih grupa.
- Mrziteljski ili ponižavajući sadržaj.
- Vođenje planiranja bilo kakvog napada ili nasilnih djela.
- Pružanje uputa kako pronaći ilegalni sadržaj ili počiniti ilegalna djela.
- Prikazivanje seksualno eksplicitnog sadržaja.

Za naš startup, želimo biti sigurni da imamo prave alate i strategije na mjestu kako bismo spriječili da ovaj tip sadržaja bude viđen od strane studenata.

### Nedostatak pravednosti

Pravednost se definira kao “osiguravanje da AI sustav nije pristran i diskriminirajući i da tretira svakoga pravedno i jednako.” U svijetu Generativne AI, želimo osigurati da isključujući pogledi marginaliziranih grupa nisu pojačani izlazom modela.

Ove vrste izlaza nisu samo destruktivne za izgradnju pozitivnih iskustava proizvoda za naše korisnike, već također uzrokuju daljnju društvenu štetu. Kao graditelji aplikacija, uvijek bismo trebali imati široku i raznoliku korisničku bazu na umu kada gradimo rješenja s Generativnom AI.

## Kako koristiti Generativnu AI odgovorno

Sada kada smo identificirali važnost Odgovorne Generativne AI, pogledajmo 4 koraka koje možemo poduzeti da odgovorno izgradimo naša AI rješenja:

### Mjerenje potencijalnih šteta

U testiranju softvera, testiramo očekivane radnje korisnika na aplikaciji. Slično tome, testiranje raznolikog skupa upita koje korisnici najvjerojatnije će koristiti je dobar način za mjerenje potencijalne štete.

Budući da naš startup gradi obrazovni proizvod, bilo bi dobro pripremiti popis obrazovnih upita. Ovo bi moglo pokriti određeni predmet, povijesne činjenice i upite o studentskom životu.

### Ublažavanje potencijalnih šteta

Vrijeme je da pronađemo načine kako možemo spriječiti ili ograničiti potencijalnu štetu uzrokovanu modelom i njegovim odgovorima. Možemo pogledati ovo u 4 različita sloja:

- **Model**. Odabir pravog modela za pravi slučaj upotrebe. Veći i složeniji modeli kao GPT-4 mogu uzrokovati veći rizik od štetnog sadržaja kada se primjenjuju na manje i specifičnije slučajeve upotrebe. Korištenje vaših podataka za obuku za fino podešavanje također smanjuje rizik od štetnog sadržaja.

- **Sigurnosni sustav**. Sigurnosni sustav je skup alata i konfiguracija na platformi koja poslužuje model koji pomaže ublažiti štetu. Primjer toga je sustav filtriranja sadržaja na Azure OpenAI usluzi. Sustavi bi također trebali otkriti napade na sustav i neželjene aktivnosti kao što su zahtjevi od botova.

- **Metaprompt**. Metaprompts i uzemljenje su načini na koje možemo usmjeriti ili ograničiti model na temelju određenih ponašanja i informacija. Ovo bi moglo biti korištenje sistemskih unosa za definiranje određenih granica modela. Osim toga, pružanje izlaza koji su relevantniji za opseg ili domenu sustava.

Također može biti korištenje tehnika kao što je Retrieval Augmented Generation (RAG) da model samo povlači informacije iz odabira pouzdanih izvora. Postoji lekcija kasnije u ovom tečaju za [izgradnju aplikacija za pretraživanje](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Korisničko iskustvo**. Završni sloj je gdje korisnik izravno komunicira s modelom putem sučelja naše aplikacije na neki način. Na taj način možemo dizajnirati UI/UX da ograničimo korisnika na vrste unosa koje mogu poslati modelu kao i tekst ili slike prikazane korisniku. Kada implementiramo AI aplikaciju, također moramo biti transparentni o tome što naša Generativna AI aplikacija može i ne može učiniti.

Imamo cijelu lekciju posvećenu [Dizajnu UX za AI aplikacije](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluacija modela**. Rad s LLM-ima može biti izazovan jer nemamo uvijek kontrolu nad podacima na kojima je model treniran. Bez obzira na to, uvijek bismo trebali evaluirati performanse i izlaze modela. Još uvijek je važno mjeriti točnost, sličnost, uzemljenost i relevantnost izlaza modela. Ovo pomaže pružiti transparentnost i povjerenje dionicima i korisnicima.

### Operativno odgovorno rješenje Generativne AI

Izgradnja operativne prakse oko vaših AI aplikacija je završna faza. Ovo uključuje partnerstvo s drugim dijelovima našeg startupa kao što su Pravni i Sigurnosni odjel kako bismo osigurali da smo u skladu sa svim regulatornim politikama. Prije lansiranja, također želimo izgraditi planove oko isporuke, rukovanja incidentima i povratka kako bismo spriječili bilo kakvu štetu našim korisnicima od rasta.

## Alati

Iako se rad na razvoju rješenja Odgovorne AI može činiti puno, to je rad koji se isplati. Kako područje Generativne AI raste, više alata za pomoć programerima da učinkovito integriraju odgovornost u svoje radne tokove će sazrijeti. Na primjer, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) može pomoći u otkrivanju štetnog sadržaja i slika putem API zahtjeva.

## Provjera znanja

Koje su neke stvari na koje trebate paziti kako biste osigurali odgovorno korištenje AI?

1. Da je odgovor točan.
1. Štetna upotreba, da se AI ne koristi za kriminalne svrhe.
1. Osiguravanje da AI nije pristran i diskriminirajući.

A: 2 i 3 su točni. Odgovorna AI pomaže vam razmotriti kako ublažiti štetne učinke i pristranosti i više.

## 🚀 Izazov

Pročitajte o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) i pogledajte što možete usvojiti za svoju upotrebu.

## Odličan rad, nastavite sa učenjem

Nakon završetka ove lekcije, pogledajte našu [Generativnu AI zbirku za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili podizati svoje znanje o Generativnoj AI!

Pređite na Lekciju 4 gdje ćemo pogledati [Osnove inženjeringa upita](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Odricanje odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.