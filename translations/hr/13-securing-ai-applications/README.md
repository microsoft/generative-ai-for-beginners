<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:47:13+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "hr"
}
-->
# Osiguranje vaših generativnih AI aplikacija

## Uvod

Ova lekcija će pokriti:

- Sigurnost u kontekstu AI sustava.
- Uobičajene rizike i prijetnje AI sustavima.
- Metode i razmatranja za osiguranje AI sustava.

## Ciljevi učenja

Nakon završetka ove lekcije, razumjet ćete:

- Prijetnje i rizike za AI sustave.
- Uobičajene metode i prakse za osiguranje AI sustava.
- Kako implementacija sigurnosnog testiranja može spriječiti neočekivane rezultate i narušavanje povjerenja korisnika.

## Što znači sigurnost u kontekstu generativne AI?

Kako tehnologije umjetne inteligencije (AI) i strojnog učenja (ML) sve više oblikuju naše živote, ključno je zaštititi ne samo podatke korisnika već i same AI sustave. AI/ML se sve više koristi za podršku procesa donošenja odluka visoke vrijednosti u industrijama gdje pogrešna odluka može rezultirati ozbiljnim posljedicama.

Evo ključnih točaka koje treba razmotriti:

- **Utjecaj AI/ML**: AI/ML ima značajan utjecaj na svakodnevni život i stoga je njihova zaštita postala neophodna.
- **Izazovi sigurnosti**: Ovaj utjecaj koji AI/ML ima zahtijeva odgovarajuću pažnju kako bi se adresirala potreba za zaštitom AI proizvoda od sofisticiranih napada, bilo od strane trolova ili organiziranih grupa.
- **Strategijski problemi**: Tehnička industrija mora proaktivno rješavati strateške izazove kako bi osigurala dugoročnu sigurnost korisnika i zaštitu podataka.

Osim toga, modeli strojnog učenja uglavnom nisu sposobni razlikovati zlonamjerne ulaze od benignih anomalnih podataka. Značajan izvor podataka za treniranje potječe iz nekuriranih, nemoderiranih javnih skupova podataka koji su otvoreni za doprinose trećih strana. Napadači ne moraju kompromitirati skupove podataka kada su slobodni doprinijeti njima. S vremenom, podaci niske pouzdanosti postaju podaci visoke pouzdanosti ako struktura/formata podataka ostaje ispravna.

Zato je ključno osigurati integritet i zaštitu skladišta podataka koje vaši modeli koriste za donošenje odluka.

## Razumijevanje prijetnji i rizika AI

U smislu AI i povezanih sustava, trovanje podataka ističe se kao najznačajnija sigurnosna prijetnja danas. Trovanje podataka događa se kada netko namjerno mijenja informacije koje se koriste za treniranje AI, uzrokujući da AI donosi pogrešne odluke. To je zbog nedostatka standardiziranih metoda za otkrivanje i ublažavanje, uz našu ovisnost o nepouzdanim ili nekuriranim javnim skupovima podataka za treniranje. Kako bi se održao integritet podataka i spriječio pogrešan proces treniranja, ključno je pratiti podrijetlo i porijeklo vaših podataka. Inače, stara izreka "smeće unutra, smeće van" vrijedi, što dovodi do kompromitiranog performansa modela.

Evo primjera kako trovanje podataka može utjecati na vaše modele:

1. **Promjena oznaka**: U zadatku binarne klasifikacije, protivnik namjerno mijenja oznake malog podskupa podataka za treniranje. Na primjer, benigni uzorci označeni su kao zlonamjerni, što dovodi do toga da model uči pogrešne asocijacije.\
   **Primjer**: Filter za neželjenu poštu pogrešno klasificira legitimne e-poruke kao neželjene zbog manipuliranih oznaka.
2. **Trovanje značajki**: Napadač suptilno mijenja značajke u podacima za treniranje kako bi uveo pristranost ili zavarao model.\
   **Primjer**: Dodavanje irelevantnih ključnih riječi opisima proizvoda za manipulaciju sustavima preporuka.
3. **Ubrizgavanje podataka**: Ubrizgavanje zlonamjernih podataka u skup za treniranje kako bi se utjecalo na ponašanje modela.\
   **Primjer**: Uvođenje lažnih korisničkih recenzija za iskrivljavanje rezultata analize sentimenta.
4. **Napadi stražnjih vrata**: Protivnik ubacuje skriveni obrazac (stražnja vrata) u podatke za treniranje. Model uči prepoznati taj obrazac i ponaša se zlonamjerno kada se pokrene.\
   **Primjer**: Sustav prepoznavanja lica treniran sa slikama sa stražnjim vratima koje pogrešno identificiraju određenu osobu.

MITRE Corporation je stvorio [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), bazu znanja o taktikama i tehnikama koje koriste protivnici u stvarnim napadima na AI sustave.

> Postoji sve veći broj ranjivosti u sustavima omogućena AI, jer uključivanje AI povećava površinu napada postojećih sustava izvan tradicionalnih cyber-napada. Razvili smo ATLAS kako bismo podigli svijest o tim jedinstvenim i evoluirajućim ranjivostima, kako globalna zajednica sve više uključuje AI u razne sustave. ATLAS je modeliran prema MITRE ATT&CK® okviru i njegove taktike, tehnike i procedure (TTPs) su komplementarne onima u ATT&CK.

Slično kao MITRE ATT&CK® okvir, koji se opsežno koristi u tradicionalnoj cyber sigurnosti za planiranje scenarija emulacije naprednih prijetnji, ATLAS pruža lako pretraživi skup TTP-ova koji mogu pomoći u boljem razumijevanju i pripremi za obranu od novih napada.

Osim toga, Open Web Application Security Project (OWASP) je stvorio "[Top 10 listu](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" najkritičnijih ranjivosti pronađenih u aplikacijama koje koriste LLM-ove. Lista ističe rizike prijetnji kao što je spomenuto trovanje podataka zajedno s drugima kao što su:

- **Ubrizgavanje upita**: tehnika gdje napadači manipuliraju Velikim Jezičnim Modelom (LLM) kroz pažljivo izrađene ulaze, uzrokujući da se ponaša izvan svoje predviđene funkcije.
- **Ranjivosti opskrbnog lanca**: Komponente i softver koji čine aplikacije koje koristi LLM, kao što su Python moduli ili vanjski skupovi podataka, mogu biti kompromitirani što dovodi do neočekivanih rezultata, uvedenih pristranosti i čak ranjivosti u temeljnoj infrastrukturi.
- **Pretjerano oslanjanje**: LLM-ovi su podložni pogreškama i skloni su halucinacijama, pružajući netočne ili nesigurne rezultate. U nekoliko dokumentiranih okolnosti, ljudi su prihvatili rezultate zdravo za gotovo, što je dovelo do neželjenih negativnih posljedica u stvarnom svijetu.

Microsoft Cloud Advocate Rod Trent napisao je besplatnu e-knjigu, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), koja duboko istražuje ove i druge nadolazeće prijetnje AI-a i pruža opsežne smjernice o tome kako najbolje riješiti ove scenarije.

## Sigurnosno testiranje za AI sustave i LLM-ove

Umjetna inteligencija (AI) transformira razne domene i industrije, nudeći nove mogućnosti i koristi za društvo. Međutim, AI također postavlja značajne izazove i rizike, kao što su privatnost podataka, pristranost, nedostatak objašnjivosti i potencijalna zloupotreba. Stoga je ključno osigurati da AI sustavi budu sigurni i odgovorni, što znači da se pridržavaju etičkih i pravnih standarda i mogu biti pouzdani od strane korisnika i dionika.

Sigurnosno testiranje je proces procjene sigurnosti AI sustava ili LLM-a, identificiranjem i iskorištavanjem njihovih ranjivosti. To može obaviti programeri, korisnici ili treće strane revizori, ovisno o svrsi i opsegu testiranja. Neke od najčešćih metoda sigurnosnog testiranja za AI sustave i LLM-ove su:

- **Sanitacija podataka**: Proces uklanjanja ili anonimiziranja osjetljivih ili privatnih informacija iz podataka za treniranje ili ulaza AI sustava ili LLM-a. Sanitacija podataka može pomoći u sprječavanju curenja podataka i zlonamjerne manipulacije smanjenjem izloženosti povjerljivih ili osobnih podataka.
- **Adversarijalno testiranje**: Proces generiranja i primjene adversarijalnih primjera na ulaz ili izlaz AI sustava ili LLM-a kako bi se procijenila njegova robusnost i otpornost na adversarijalne napade. Adversarijalno testiranje može pomoći u identifikaciji i ublažavanju ranjivosti i slabosti AI sustava ili LLM-a koje napadači mogu iskoristiti.
- **Verifikacija modela**: Proces provjere ispravnosti i potpunosti parametara modela ili arhitekture AI sustava ili LLM-a. Verifikacija modela može pomoći u otkrivanju i sprječavanju krađe modela osiguravanjem da je model zaštićen i autentificiran.
- **Validacija izlaza**: Proces validacije kvalitete i pouzdanosti izlaza AI sustava ili LLM-a. Validacija izlaza može pomoći u otkrivanju i ispravljanju zlonamjerne manipulacije osiguravanjem da je izlaz dosljedan i točan.

OpenAI, lider u AI sustavima, postavio je niz _evaluacija sigurnosti_ kao dio njihove inicijative za crveni tim, s ciljem testiranja izlaza AI sustava u nadi da će doprinijeti sigurnosti AI.

### AI Sigurnost

Važno je da nastojimo zaštititi AI sustave od zlonamjernih napada, zloupotrebe ili neželjenih posljedica. To uključuje poduzimanje koraka kako bi se osigurala sigurnost, pouzdanost i povjerenje u AI sustave, kao što su:

- Osiguranje podataka i algoritama koji se koriste za treniranje i pokretanje AI modela
- Sprječavanje neovlaštenog pristupa, manipulacije ili sabotaže AI sustava
- Otkrivanje i ublažavanje pristranosti, diskriminacije ili etičkih problema u AI sustavima
- Osiguranje odgovornosti, transparentnosti i objašnjivosti AI odluka i radnji
- Usklađivanje ciljeva i vrijednosti AI sustava s onima ljudi i društva

AI sigurnost je važna za osiguranje integriteta, dostupnosti i povjerljivosti AI sustava i podataka. Neki od izazova i prilika AI sigurnosti su:

- Prilika: Uključivanje AI u strategije cyber sigurnosti budući da može igrati ključnu ulogu u identifikaciji prijetnji i poboljšanju vremena odgovora. AI može pomoći automatizirati i poboljšati otkrivanje i ublažavanje cyber napada, kao što su phishing, malware ili ransomware.
- Izazov: AI također može biti korišten od strane protivnika za pokretanje sofisticiranih napada, kao što je generiranje lažnog ili obmanjujućeg sadržaja, lažno predstavljanje korisnika ili iskorištavanje ranjivosti u AI sustavima. Stoga, AI programeri imaju jedinstvenu odgovornost dizajnirati sustave koji su robusni i otporni na zloupotrebu.

### Zaštita podataka

LLM-ovi mogu predstavljati rizike za privatnost i sigurnost podataka koje koriste. Na primjer, LLM-ovi mogu potencijalno zapamtiti i otkriti osjetljive informacije iz svojih podataka za treniranje, kao što su osobna imena, adrese, lozinke ili brojevi kreditnih kartica. Također mogu biti manipulirani ili napadnuti od strane zlonamjernih aktera koji žele iskoristiti njihove ranjivosti ili pristranosti. Stoga je važno biti svjestan tih rizika i poduzeti odgovarajuće mjere za zaštitu podataka koji se koriste s LLM-ovima. Postoji nekoliko koraka koje možete poduzeti kako biste zaštitili podatke koji se koriste s LLM-ovima. Ti koraci uključuju:

- **Ograničavanje količine i vrste podataka koje dijele s LLM-ovima**: Dijelite samo podatke koji su nužni i relevantni za predviđene svrhe, i izbjegavajte dijeljenje bilo kakvih podataka koji su osjetljivi, povjerljivi ili osobni. Korisnici također trebaju anonimizirati ili šifrirati podatke koje dijele s LLM-ovima, kao što je uklanjanje ili maskiranje bilo kakvih identifikacijskih informacija, ili korištenje sigurnih komunikacijskih kanala.
- **Provjeravanje podataka koje LLM-ovi generiraju**: Uvijek provjerite točnost i kvalitetu izlaza generiranog od strane LLM-ova kako biste osigurali da ne sadrži neželjene ili neprikladne informacije.
- **Prijavljivanje i upozoravanje na bilo kakva kršenja podataka ili incidente**: Budite budni na bilo kakve sumnjive ili abnormalne aktivnosti ili ponašanja LLM-ova, kao što je generiranje tekstova koji su irelevantni, netočni, uvredljivi ili štetni. To može biti indikacija kršenja podataka ili sigurnosnog incidenta.

Sigurnost podataka, upravljanje i usklađenost su ključni za svaku organizaciju koja želi iskoristiti snagu podataka i AI u multi-cloud okruženju. Osiguranje i upravljanje svim vašim podacima je složen i višestran zadatak. Morate osigurati i upravljati različitim vrstama podataka (strukturiranim, nestrukturiranim i podacima generiranim od strane AI) na različitim lokacijama u više oblaka, i morate uzeti u obzir postojeće i buduće regulative o sigurnosti podataka, upravljanju i AI. Kako biste zaštitili svoje podatke, trebate usvojiti neke najbolje prakse i mjere opreza, kao što su:

- Koristite cloud usluge ili platforme koje nude zaštitu podataka i značajke privatnosti.
- Koristite alate za kvalitetu podataka i validaciju kako biste provjerili svoje podatke na greške, nedosljednosti ili anomalije.
- Koristite okvire za upravljanje podacima i etiku kako biste osigurali da se vaši podaci koriste na odgovoran i transparentan način.

### Emulacija stvarnih prijetnji - AI crveni tim

Emulacija stvarnih prijetnji sada se smatra standardnom praksom u izgradnji otpornijih AI sustava primjenom sličnih alata, taktika, procedura za identifikaciju rizika za sustave i testiranje odgovora branitelja.

AI crveni tim nije sveobuhvatan i trebao bi se smatrati komplementarnim kretanjem dodatnim kontrolama kao što su [kontrola pristupa temeljena na ulogama (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) i sveobuhvatna rješenja za upravljanje podacima. Trebao bi nadopuniti sigurnosnu strategiju koja se fokusira na primjenu sigurnih i odgovornih AI rješenja koja uzimaju u obzir privatnost i sigurnost dok nastoje minimizirati pristranosti, štetan sadržaj i dezinformacije koje mogu narušiti povjerenje korisnika.

Evo popisa dodatnog čitanja koji vam može pomoći da bolje razumijete kako crveni tim može pomoći u identifikaciji i ublažavanju rizika u vašim AI sustavima:

- [Planiranje crvenog timiranja za velike jezične modele (LLM-ove) i njihove aplikacije](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Što je OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - Ključna praksa za izgradnju sigurnijih i odgovornih AI rješenja](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), baza znanja o taktikama i tehnikama koje koriste protivnici u stvarnim napadima na AI sustave.

## Provjera znanja

Što bi mogao biti dobar pristup za održavanje integriteta podataka i sprječavanje zloupotrebe?

1. Imati jake kontrole pristupa temeljene na ulogama za pristup podacima i

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.