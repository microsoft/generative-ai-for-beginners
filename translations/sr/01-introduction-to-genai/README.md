<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:39:37+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "sr"
}
-->
# Uvod u Generativnu veštačku inteligenciju i velike jezičke modele

_(Kliknite na sliku iznad da pogledate video ove lekcije)_

Generativna veštačka inteligencija je vrsta veštačke inteligencije sposobna da generiše tekst, slike i druge vrste sadržaja. Ono što je čini fantastičnom tehnologijom je to što demokratizuje veštačku inteligenciju, svako može da je koristi sa samo jednim tekstualnim promptom, rečenicom napisanom na prirodnom jeziku. Nema potrebe da učite jezik kao što je Java ili SQL da biste postigli nešto vredno, sve što vam treba je da koristite svoj jezik, navedete šta želite i dobijete sugestiju od AI modela. Aplikacije i uticaj ovoga su ogromni, možete pisati ili razumeti izveštaje, pisati aplikacije i još mnogo toga, sve u sekundi.

U ovom kurikulumu istražićemo kako naš startup koristi generativnu veštačku inteligenciju da otključa nove scenarije u svetu obrazovanja i kako se suočavamo sa neizbežnim izazovima vezanim za društvene implikacije njene primene i tehnološka ograničenja.

## Uvod

Ova lekcija će pokriti:

- Uvod u poslovni scenario: našu startup ideju i misiju.
- Generativnu veštačku inteligenciju i kako smo stigli do trenutnog tehnološkog pejzaža.
- Unutrašnje funkcionisanje velikog jezičkog modela.
- Glavne sposobnosti i praktične primene velikih jezičkih modela.

## Ciljevi učenja

Nakon završetka ove lekcije, razumećete:

- Šta je generativna veštačka inteligencija i kako funkcionišu veliki jezički modeli.
- Kako možete koristiti velike jezičke modele za različite primene, sa fokusom na obrazovne scenarije.

## Scenario: naš obrazovni startup

Generativna veštačka inteligencija (AI) predstavlja vrhunac AI tehnologije, pomerajući granice onoga što se nekada smatralo nemogućim. Generativni AI modeli imaju nekoliko sposobnosti i primena, ali za ovaj kurikulum istražićemo kako revolucionišu obrazovanje kroz fiktivni startup. Ovaj startup ćemo nazvati _naš startup_. Naš startup radi u oblasti obrazovanja sa ambicioznom misijom

> _poboljšanje pristupačnosti u učenju, na globalnom nivou, osiguravanje ravnopravnog pristupa obrazovanju i pružanje personalizovanih iskustava učenja svakom učeniku, prema njihovim potrebama_.

Tim našeg startupa je svestan da nećemo moći da postignemo ovaj cilj bez korišćenja jednog od najmoćnijih alata modernog doba – velikih jezičkih modela (LLMs).

Očekuje se da će generativna veštačka inteligencija revolucionisati način na koji danas učimo i predajemo, sa studentima koji imaju na raspolaganju virtuelne nastavnike 24 sata dnevno koji pružaju ogromne količine informacija i primera, i nastavnicima koji mogu koristiti inovativne alate za ocenjivanje svojih učenika i davanje povratnih informacija.

Da bismo počeli, definišimo neke osnovne pojmove i terminologiju koju ćemo koristiti tokom celog kurikuluma.

## Kako smo dobili generativnu veštačku inteligenciju?

Uprkos izuzetnom _hajpu_ koji je nedavno stvoren objavljivanjem generativnih AI modela, ova tehnologija je decenijama u nastajanju, sa prvim istraživačkim naporima koji datiraju još iz 60-ih. Sada smo na tački gde AI ima ljudske kognitivne sposobnosti, kao što je razgovor, što je prikazano, na primer, sa [OpenAI ChatGPT](https://openai.com/chatgpt) ili [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), koji takođe koristi GPT model za pretragu na Bing-u.

Vratimo se malo unazad, prvi prototipovi AI su se sastojali od pisaćih chatbotova, oslanjajući se na bazu znanja izvučenu iz grupe stručnjaka i predstavljenu u računaru. Odgovori u bazi znanja su se aktivirali ključnim rečima koje su se pojavljivale u ulaznom tekstu. Međutim, ubrzo je postalo jasno da takav pristup, koristeći pisaće chatbotove, nije dobro skalirao.

### Statistički pristup AI: Mašinsko učenje

Prelomna tačka je stigla tokom 90-ih, primenom statističkog pristupa analizi teksta. Ovo je dovelo do razvoja novih algoritama – poznatih kao mašinsko učenje – sposobnih da uče obrasce iz podataka bez eksplicitnog programiranja. Ovaj pristup omogućava mašinama da simuliraju razumevanje ljudskog jezika: statistički model se obučava na uparivanju tekst-oznaka, omogućavajući modelu da klasifikuje nepoznat ulazni tekst sa unapred definisanom oznakom koja predstavlja nameru poruke.

### Neuronske mreže i moderni virtuelni asistenti

U poslednjih nekoliko godina, tehnološka evolucija hardvera, sposobnog da obrađuje veće količine podataka i složenije proračune, podstakla je istraživanje u AI, što je dovelo do razvoja naprednih algoritama mašinskog učenja poznatih kao neuronske mreže ili algoritmi dubokog učenja.

Neuronske mreže (i posebno Recurrent Neural Networks – RNNs) značajno su unapredile obradu prirodnog jezika, omogućavajući reprezentaciju značenja teksta na smisleniji način, vrednujući kontekst reči u rečenici.

Ovo je tehnologija koja je pokretala virtuelne asistente rođene u prvoj deceniji novog veka, vrlo sposobne u tumačenju ljudskog jezika, identifikovanju potrebe i izvršavanju akcije da je zadovolje – kao što je odgovaranje sa unapred definisanim skriptom ili korišćenje usluge treće strane.

### Danas, Generativna veštačka inteligencija

Tako smo stigli do generativne veštačke inteligencije danas, koja se može smatrati podskupom dubokog učenja.

Nakon decenija istraživanja u oblasti AI, nova arhitektura modela – nazvana _Transformer_ – prevazišla je ograničenja RNNs, sposobna da primi mnogo duže sekvence teksta kao ulaz. Transformeri su zasnovani na mehanizmu pažnje, omogućavajući modelu da daje različite težine ulazima koje prima, 'obraćajući više pažnje' tamo gde je koncentrisana najrelevantnija informacija, bez obzira na njihov redosled u tekstualnoj sekvenci.

Većina nedavnih generativnih AI modela – takođe poznatih kao veliki jezički modeli (LLMs), jer rade sa tekstualnim ulazima i izlazima – zaista su zasnovani na ovoj arhitekturi. Ono što je zanimljivo kod ovih modela – obučenih na ogromnoj količini neoznačenih podataka iz različitih izvora kao što su knjige, članci i veb sajtovi – jeste da se mogu prilagoditi širokom spektru zadataka i generisati gramatički ispravan tekst sa naznakama kreativnosti. Dakle, ne samo da su neverovatno unapredili sposobnost mašine da 'razume' ulazni tekst, već su omogućili njihovu sposobnost da generišu originalan odgovor na ljudskom jeziku.

## Kako funkcionišu veliki jezički modeli?

U sledećem poglavlju ćemo istražiti različite vrste generativnih AI modela, ali za sada hajde da pogledamo kako funkcionišu veliki jezički modeli, sa fokusom na OpenAI GPT (Generative Pre-trained Transformer) modele.

- **Tokenizator, tekst u brojeve**: Veliki jezički modeli primaju tekst kao ulaz i generišu tekst kao izlaz. Međutim, budući da su statistički modeli, mnogo bolje rade sa brojevima nego sa tekstualnim sekvencama. Zato se svaki ulaz u model obrađuje pomoću tokenizatora, pre nego što ga koristi osnovni model. Token je deo teksta – koji se sastoji od promenljivog broja karaktera, tako da je glavna uloga tokenizatora razdvajanje ulaza u niz tokena. Zatim, svaki token se mapira sa indeksom tokena, što je celobrojno kodiranje originalnog dela teksta.

- **Predviđanje izlaznih tokena**: S obzirom na n tokena kao ulaz (sa maksimalnim n koji varira od jednog modela do drugog), model je u stanju da predvidi jedan token kao izlaz. Ovaj token se zatim uključuje u ulaz sledeće iteracije, u obrascu proširujućeg prozora, omogućavajući bolje korisničko iskustvo dobijanja jedne (ili više) rečenice kao odgovora. Ovo objašnjava zašto, ako ste ikada koristili ChatGPT, možda ste primetili da ponekad izgleda kao da se zaustavlja na sredini rečenice.

- **Proces selekcije, distribucija verovatnoće**: Izlazni token bira model prema verovatnoći njegovog pojavljivanja nakon trenutne tekstualne sekvence. Ovo je zato što model predviđa distribuciju verovatnoće nad svim mogućim 'sledećim tokenima', izračunatu na osnovu svog treninga. Međutim, nije uvek izabran token sa najvećom verovatnoćom iz rezultirajuće distribucije. Stupanj slučajnosti se dodaje ovom izboru, na način da model deluje u nedeterminističkoj modi - ne dobijamo potpuno isti izlaz za isti ulaz. Ovaj stepen slučajnosti se dodaje kako bi se simulirao proces kreativnog razmišljanja i može se podesiti pomoću parametra modela zvanog temperatura.

## Kako naš startup može iskoristiti velike jezičke modele?

Sada kada bolje razumemo unutrašnje funkcionisanje velikog jezičkog modela, hajde da vidimo neke praktične primere najčešćih zadataka koje mogu prilično dobro obaviti, sa osvrtom na naš poslovni scenario.
Rekli smo da je glavna sposobnost velikog jezičkog modela _generisanje teksta od nule, počevši od tekstualnog ulaza, napisanog na prirodnom jeziku_.

Ali kakav tekstualni ulaz i izlaz?
Ulaz velikog jezičkog modela je poznat kao prompt, dok je izlaz poznat kao completion, termin koji se odnosi na mehanizam modela za generisanje sledećeg tokena za kompletiranje trenutnog ulaza. Uronićemo duboko u to šta je prompt i kako ga dizajnirati na način da izvučemo maksimum iz našeg modela. Ali za sada, recimo samo da prompt može uključivati:

- **Instrukciju** koja specificira vrstu izlaza koju očekujemo od modela. Ova instrukcija ponekad može uključivati neke primere ili dodatne podatke.

  1. Rezime članka, knjige, recenzija proizvoda i više, zajedno sa izvlačenjem uvida iz nestrukturiranih podataka.
  
  2. Kreativno osmišljavanje i dizajn članka, eseja, zadatka ili više.

- **Pitanje**, postavljeno u obliku razgovora sa agentom.

- Deo **teksta za dopunjavanje**, što implicitno znači traženje pomoći u pisanju.

- Deo **koda** zajedno sa zahtevom za objašnjenjem i dokumentovanjem, ili komentar koji traži generisanje dela koda koji obavlja određeni zadatak.

Gore navedeni primeri su prilično jednostavni i nisu zamišljeni kao iscrpna demonstracija sposobnosti velikih jezičkih modela. Oni su namenjeni da pokažu potencijal korišćenja generativne veštačke inteligencije, posebno ali ne ograničavajući se na obrazovne kontekste.

Takođe, izlaz generativnog AI modela nije savršen i ponekad kreativnost modela može delovati protiv njega, rezultirajući izlazom koji je kombinacija reči koju ljudski korisnik može protumačiti kao mistifikaciju stvarnosti, ili može biti uvredljiv. Generativna veštačka inteligencija nije inteligentna - barem u širem smislu definicije inteligencije, uključujući kritičko i kreativno razmišljanje ili emocionalnu inteligenciju; nije deterministička, i nije pouzdana, jer izmišljotine, kao što su pogrešne reference, sadržaj i izjave, mogu biti kombinovane sa tačnim informacijama, i predstavljene na ubedljiv i samouveren način. U sledećim lekcijama bavićemo se svim ovim ograničenjima i videćemo šta možemo učiniti da ih ublažimo.

## Zadaci

Vaš zadatak je da pročitate više o [generativnoj veštačkoj inteligenciji](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) i pokušate da identifikujete oblast u kojoj biste danas dodali generativnu veštačku inteligenciju koja je trenutno nema. Kako bi uticaj bio drugačiji od obavljanja na "stari način", možete li učiniti nešto što niste mogli ranije, ili ste brži? Napišite sažetak od 300 reči o tome kako bi izgledao vaš startup iz snova u oblasti veštačke inteligencije i uključite naslove kao što su "Problem", "Kako bih koristio veštačku inteligenciju", "Uticaj" i opciono poslovni plan.

Ako ste uradili ovaj zadatak, možda ste čak spremni da se prijavite za Microsoft-ov inkubator, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) nudimo kredite za Azure, OpenAI, mentorstvo i mnogo više, pogledajte!

## Provera znanja

Šta je tačno u vezi sa velikim jezičkim modelima?

1. Dobijate potpuno isti odgovor svaki put.
2. Radi stvari savršeno, odlično u sabiranju brojeva, proizvodnji funkcionalnog koda itd.
3. Odgovor može varirati uprkos korišćenju istog prompta. Takođe je odličan u davanju prvog nacrta nečega, bilo da je to tekst ili kod. Ali treba da unapredite rezultate.

Odgovor: 3, LLM je nedeterministički, odgovor varira, međutim, možete kontrolisati njegovu varijansu putem podešavanja temperature. Takođe ne bi trebalo da očekujete da radi stvari savršeno, tu je da obavi težak posao za vas, što često znači da dobijate dobar prvi pokušaj nečega što treba postepeno poboljšati.

## Odličan rad! Nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [kolekciju za učenje generativne veštačke inteligencije](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da nastavite sa unapređivanjem svog znanja o generativnoj veštačkoj inteligenciji!

Pređite na Lekciju 2 gde ćemo istražiti kako [istražiti i uporediti različite tipove LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Ограничење одговорности**:  
Овај документ је преведен користећи AI услугу превођења [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да постигнемо тачност, молимо вас да будете свесни да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације, препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.