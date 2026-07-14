# Gradnja klepetalnih aplikacij, podprtih z generativno umetno inteligenco  

[![Gradnja klepetalnih aplikacij, podprtih z generativno umetno inteligenco](../../../translated_images/sl/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)  

> _(Kliknite sliko zgoraj za ogled videa te lekcije)_  

Zdaj, ko smo videli, kako lahko gradimo aplikacije za generiranje besedila, si poglejmo klepetalne aplikacije.  

Klepetalne aplikacije so postale sestavni del našega vsakdana in nudijo več kot le način za priložnostno pogovarjanje. So ključni del storitev za stranke, tehnične podpore in celo sofisticiranih svetovalnih sistemov. Verjetno ste v zadnjem času prejeli pomoč prek klepetalne aplikacije. Ko v te platforme vključujemo naprednejše tehnologije, kot je generativna umetna inteligenca, se kompleksnost povečuje, prav tako pa tudi izzivi.  

Nekaj vprašanj, na katera moramo odgovoriti, je:  

- **Gradnja aplikacije**. Kako učinkovito graditi in brezhibno integrirati te aplikacije, podprte z umetno inteligenco, za specifične primere uporabe?  
- **Nadzor**. Ko je aplikacija nameščena, kako lahko nadzorujemo in zagotovimo, da aplikacije delujejo na najvišji kvaliteti, tako z vidika funkcionalnosti kot spoštovanja [šestih načel odgovornih AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?  

Ko vstopamo v dobo, ki jo opredeljujeta avtomatizacija in brezhibna interakcija med človekom in strojem, postaja razumevanje, kako generativna AI spreminja obseg, globino in prilagodljivost klepetalnih aplikacij, nujno. Ta lekcija bo raziskala vidike arhitekture, ki podpirajo te zapletene sisteme, metode za njihovo natančno prilagoditev za domensko specifične naloge ter merila in dejavnike, pomembne za zagotovitev odgovorne uporabe AI.  

## Uvod  

Ta lekcija zajema:  

- Tehnike za učinkovito gradnjo in integracijo klepetalnih aplikacij.  
- Kako uporabiti prilagoditve in fino nastavitev aplikacij.  
- Strategije in dejavniki za učinkovito spremljanje klepetalnih aplikacij.  

## Cilji učenja  

Do konca te lekcije boste lahko:  

- Opisali upoštevane dejavnike za gradnjo in integracijo klepetalnih aplikacij v obstoječe sisteme.  
- Prilagodili klepetalne aplikacije za specifične primere uporabe.  
- Prepoznali ključne metrike in dejavnike za učinkovito spremljanje ter vzdrževanje kakovosti klepetalnih aplikacij, podprtih z AI.  
- Zagotovili, da klepetalne aplikacije uporabljajo AI odgovorno.  

## Integracija generativne AI v klepetalne aplikacije  

Nadgradnja klepetalnih aplikacij z generativno AI ni le ustvarjanje pametnejših sistemov; gre za optimizacijo arhitekture, zmogljivosti in uporabniškega vmesnika za zagotavljanje kakovostne uporabniške izkušnje. To vključuje raziskovanje arhitekturnih osnov, integracij API-jev in vidikov uporabniškega vmesnika. Ta oddelek vam bo ponudil celovito vodilo za navigacijo po teh kompleksnih področjih, ne glede na to, ali jih priklapljate na obstoječe sisteme ali gradite kot samostojne platforme.  

Do konca tega oddelka boste imeli znanje, potrebno za učinkovito ustvarjanje in vključevanje klepetalnih aplikacij.  

### Klepetalni robot ali klepetalna aplikacija?  

Preden se poglobimo v gradnjo klepetalnih aplikacij, primerjajmo "klepetalnike" in "klepetalne aplikacije, podprte z AI", ki opravljajo različne vloge in funkcionalnosti. Glavni namen klepetalnika je avtomatizacija določenih pogovornih nalog, kot je odgovarjanje na pogosta vprašanja ali sledenje pošiljke. Običajno ga upravlja pravilo osnovana logika ali kompleksni AI algoritmi. Nasprotno pa je klepetalna aplikacija, podprta z AI, veliko širše okolje, zasnovano za olajšanje različnih oblik digitalne komunikacije, kot so besedilni, glasovni in video klepeti med ljudmi. Njena značilnost je integracija generativnega AI modela, ki simulira nianse človeškega pogovora in ustvarja odzive na podlagi širokega nabora vhodnih in kontekstualnih podatkov. Takšna aplikacija lahko vodi odprte diskusije, se prilagaja spreminjajočim kontekstom pogovora in celo ustvarja kreativna ali kompleksna besedila.  

Tabela spodaj prikazuje ključne razlike in podobnosti, ki nam pomagajo razumeti njihove edinstvene vloge v digitalni komunikaciji.  

| Klepetalnik                         | Klepetalna aplikacija, podprta z generativno AI                   |  
| --------------------------------- | --------------------------------------------------------------- |  
| Osredotočen na naloge in pravila   | Zaveda se konteksta                                                |  
| Pogosto integriran v večje sisteme | Lahko gosti enega ali več klepetalnikov                           |  
| Omejen na programirane funkcije    | Vključuje modele generativne AI                                   |  
| Specializirane in strukturirane interakcije | Zmožen odprtih razprav na različne teme                         |  

### Uporaba predpripravljenih funkcionalnosti z SDK-ji in API-ji  

Pri gradnji klepetalne aplikacije je odličen prvi korak ocena že obstoječega. Uporaba SDK-jev in API-jev pri gradnji klepetalnih aplikacij je strateška prednost zaradi več razlogov. Z vključitvijo dobro dokumentiranih SDK-jev in API-jev si aplikacijo strateško postavite za dolgoročni uspeh, pri čemer rešujete izzive razširljivosti in vzdrževanja.  

- **Pospeši proces razvoja in zmanjša obremenitev**: Zanašanje na že zgrajene funkcionalnosti namesto na drag proces njihove izdelave omogoča, da se osredotočite na druge vidike aplikacije, ki so vam morda pomembnejši, kot je poslovna logika.  
- **Boljša zmogljivost**: Ko gradite funkcionalnost iz nič, se slej ko prej vprašate: "Kako se to razširja? Ali aplikacija zmore obvladati nenaden porast uporabnikov?" Dobro vzdrževani SDK-ji in API-ji pogosto vključujejo rešitve za te izzive.  
- **Enostavnejše vzdrževanje**: Posodobitve in izboljšave so lažje upravljati, saj večina API-jev in SDK-jev zahteva le posodobitev knjižnice ob izdaji nove različice.  
- **Dostop do najnovejše tehnologije**: Uporaba modelov, ki so fino nastavljeni in usposobljeni na obsežnih podatkovnih zbirkah, zagotavlja vaši aplikaciji zmogljivosti naravnega jezika.  

Dostop do funkcionalnosti SDK-ja ali API-ja običajno pomeni pridobitev dovoljenja za uporabo storitev, kar je pogosto prek edinstvenega ključa ali žetona za preverjanje pristnosti. Za prikaz, kako to izgleda, bomo uporabili knjižnico OpenAI za Python. Poskusite lahko tudi sami v naslednjem [zvezku za OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) ali [zvezku za Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) za to lekcijo.  

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-4o-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```
  
Primer zgoraj uporablja GPT-4o mini model z API-jem za odgovore, da dopolni poziv, a opazite, da je ključ API nastavljen pred tem. Če ključa ne nastavite, boste prejeli napako.  

## Uporabniška izkušnja (UX)  

Splošna načela UX veljajo za klepetalne aplikacije, tukaj pa je nekaj dodatnih dejavnikov, ki postanejo še posebej pomembni zaradi komponent strojnega učenja.  

- **Mehanizem za rešitev nejasnosti**: Generativni AI modeli včasih ustvarijo dvoumne odgovore. Funkcija, ki uporabnikom omogoča zahtevo za pojasnilo, je lahko koristna, če naletijo na ta problem.  
- **Ohranjanje konteksta**: Napredni generativni AI modeli imajo sposobnost ohranjanja konteksta znotraj pogovora, kar je lahko pomembna prednost za uporabniško izkušnjo. Uporabnikom omogočiti nadzor in upravljanje konteksta izboljša izkušnjo, vendar prinaša tveganje za hranjenje občutljivih informacij. Premisleki o tem, kako dolgo se te informacije shranjujejo, na primer uvedba politike zadrževanja, lahko uravnotežijo potrebo po kontekstu in zasebnosti.  
- **Personalizacija**: Zmožnost učenja in prilagajanja AI modelov ponuja individualizirano uporabniško izkušnjo. Prilagajanje izkušnje z lastnostmi, kot so uporabniški profili, ne le da uporabnik dobi občutek razumevanja, temveč mu tudi pomaga pri iskanju specifičnih odgovorov, s čimer se ustvari učinkovitejša in zadovoljivejša interakcija.  

Primer take personalizacije so nastavitve "Custom Instructions" v OpenAI-jevem ChatGPT-ju. Omogočajo vam, da podate informacije o sebi, ki so lahko pomemben kontekst za vaše pozive. Tukaj je primer prilagojene navodila.  

![Nastavitve prilagojenih navodil v ChatGPT](../../../translated_images/sl/custom-instructions.b96f59aa69356fcf.webp)  

Ta "profil" usmerja ChatGPT, da pripravi učni načrt o povezanih seznamih. Opazite, da ChatGPT upošteva, da uporabnik želi bolj poglobljen učni načrt glede na njene izkušnje.  

![Poziv v ChatGPT za učni načrt o povezanih seznamih](../../../translated_images/sl/lesson-plan-prompt.cc47c488cf1343df.webp)  

### Microsoftov sistemski okvir sporočil za velike jezikovne modele  

[Microsoft je zagotovil smernice](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) za učinkovito pisanje sistemskih sporočil pri generiranju odgovorov iz LLM-jev, razdeljenih na 4 področja:  

1. Določitev, za koga je model namenjen, ter njegovih zmožnosti in omejitev.  
2. Določitev formata izhoda modela.  
3. Predložitev specifičnih primerov, ki prikazujejo želeno vedenje modela.  
4. Zagotavljanje dodatnih vedenjskih varovalk.  

### Dostopnost  

Ne glede na to, ali ima uporabnik vidne, slušne, motorične ali kognitivne okvare, mora biti dobro zasnovana klepetalna aplikacija uporabna za vse. Spodnji seznam predstavi posebne funkcije, namenjene izboljšanju dostopnosti za različne vrste uporabniških omejitev.  

- **Funkcije za vidno invalidnost**: teme z visokim kontrastom in besedilo z nastavljivo velikostjo, združljivost z bralniki zaslona.  
- **Funkcije za slušno invalidnost**: funkcije besedilo-učno-naprej in govor-besedilo, vizualni znaki za zvočna obvestila.  
- **Funkcije za motorične omejitve**: podpora tipkovni navigaciji, glasovni ukazi.  
- **Funkcije za kognitivne omejitve**: poenostavljene jezikovne možnosti.  

## Prilagoditev in fino nastavljanje za domensko specifične jezikovne modele  

Predstavljajte si klepetalno aplikacijo, ki razume žargon vašega podjetja in predvidi specifična vprašanja, ki jih pogosto postavlja njena uporabniška baza. Obstajata dva pristopa, ki ju je vredno omeniti:  

- **Uporaba DSL modelov**. DSL pomeni domensko specifični jezik. Uporabite lahko tako imenovani DSL model, usposobljen na določeno področje, da razume njegove koncepte in scenarije.  
- **Uporaba fine-tuninga**. Fino nastavljanje je proces dodatnega treniranja vašega modela z določenimi podatki.  

## Prilagoditev: uporaba DSL  

Uporaba domensko specifičnih jezikovnih modelov (DSL modeli) lahko poveča uporabniško angažiranost z zagotavljanjem specializiranih, kontekstualno relevantnih interakcij. To je model, ki je usposobljen ali fino nastavljen za razumevanje in generiranje besedil, povezanih z določenim področjem, industrijo ali temo. Možnosti uporabe DSL modela se gibljejo od usposabljanja modela iz nič do uporabe že obstoječih prek SDK-jev in API-jev. Druga možnost je fino nastavljanje, kjer vzamete obstoječi predhodno usposobljeni model in ga prilagodite za specifično področje.  

## Prilagoditev: uporaba fino nastavljanja  

Fino nastavljanje se pogosto uporablja, kadar predhodno usposobljen model ni dovolj dober na specializiranem področju ali za specifično nalogo.  

Na primer, medicinska vprašanja so zapletena in zahtevajo veliko konteksta. Ko zdravnik postavi diagnozo, temelji na različnih dejavnikih, kot so življenjski slog ali predhodna stanja, ter pogosto uporablja tudi najnovejše medicinske članke za potrditev diagnoze. V tako zahtevnih primerih splošna AI klepetalna aplikacija ne more biti zanesljiv vir.  

### Primer: medicinska aplikacija  

Predstavljajte si klepetalno aplikacijo, zasnovano za pomoč zdravstvenim delavcem z nudenjem hitrih referenc o smernicah zdravljenja, interakcijah zdravil ali najnovejših raziskavah.  

Splošni model je lahko primeren za odgovore na osnovna medicinska vprašanja ali za splošne nasvete, vendar se lahko spopade z naslednjim:  

- **Zelo specifični ali kompleksni primeri**. Na primer, nevrolog bi lahko vprašal aplikacijo: "Kakšni so trenutni najboljši pristopi za obvladovanje zdravljenju odporne epilepsije pri pediatričnih bolnikih?"  
- **Pomanjkanje najnovejših znanstvenih dosežkov**. Splošni model bi lahko imel težave z zagotavljanjem aktualnih odgovorov, ki vključujejo najnovejše dosežke v nevrologiji in farmakologiji.  

V takih primerih lahko fino nastavljanje modela z ustrezno medicinsko bazo podatkov znatno izboljša njegovo sposobnost natančnega in zanesljivega obravnavanja teh zahtevnih medicinskih vprašanj. To zahteva dostop do velike in relevantne baze podatkov, ki predstavlja domensko specifične izzive in vprašanja, ki jih je treba nasloviti.  

## Dejavniki za visoko kakovostno klepetalno izkušnjo, pogonjeno z AI  

Ta oddelek navaja merila za "visokokakovostne" klepetalne aplikacije, ki zajemajo merjenje ključnih metrik in upoštevanje okvira, ki odgovorno uporablja tehnologijo AI.  

### Ključne metrike  

Za ohranjanje visokih zmogljivosti aplikacije je bistveno spremljati ključne metrike in dejavnike. Ta merila ne zagotavljajo le funkcionalnosti aplikacije, temveč tudi ocenjujejo kakovost AI modela in uporabniške izkušnje. Spodaj je seznam osnovnih metrik, AI in meril uporabniške izkušnje za razmislek.  

| Metrična vrednost           | Opis                                                                                                                   | Razmisleki za razvijalca klepeta                                  |  
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |  
| **Čas delovanja (Uptime)**  | Meri čas, ko je aplikacija delujoča in dostopna uporabnikom.                                                           | Kako boste zmanjšali čas nedosegljivosti?                        |  
| **Čas odziva**              | Čas, ki ga aplikacija potrebuje za odgovor na uporabnikov zahtevek.                                                    | Kako lahko optimizirate obdelavo poizvedb za hitrejše odzive?    |  
| **Natančnost (Precision)**  | Razmerje prave pozitivne napovedi glede na skupno število pozitivnih napovedi.                                         | Kako boste preverili natančnost vašega modela?                   |  
| **Pokritost (Recall)**      | Razmerje prave pozitivne napovedi glede na dejansko število pozitivnih primerov.                                      | Kako boste merili in izboljšali pokritost?                       |  
| **F1 rezultat**             | Harmonično povprečje natančnosti in pokritosti, ki uravnoteži kompromis med obema.                                    | Kakšen je vaš cilj za F1 rezultat? Kako boste uravnotežili natančnost in pokritost? |  
| **Perpleksnost**            | Meri, kako dobro se porazdelitev verjetnosti, ki jo napove model, ujema z dejansko porazdelitvijo podatkov.            | Kako boste zmanjšali perpleksnost?                               |  
| **Metrike zadovoljstva uporabnikov** | Meri uporabnikovo percepcijo aplikacije. Pogosto se zajema preko anket.                                        | Kako pogosto boste zbirali povratne informacije? Kako se boste nanje odzvali? |  
| **Stopnja napak**           | Stopnja, pri kateri model dela napake pri razumevanju ali izhodu.                                                      | Kake strategije imate za zmanjšanje stopnje napak?              |  
| **Cikli ponovnega usposabljanja** | Pogostost, s katero se model posodablja za vključitev novih podatkov in spoznanj.                               | Kako pogosto boste model ponovno usposabljali? Kaj sproži cikel ponovnega usposabljanja? |  

| **Odkrivanje anomalij**    | Orodja in tehnike za prepoznavanje nenavadnih vzorcev, ki niso skladni s pričakovanim vedenjem.                          | Kako boste odgovorili na anomalije?                                        |

### Uvajanje odgovornih praks AI v klepetalnih aplikacijah

Microsoftov pristop k odgovorni uporabi AI je identificiral šest načel, ki naj bi usmerjala razvoj in uporabo AI. Spodaj so navedena načela, njihova definicija ter stvari, ki jih naj razvijalec klepeta upošteva in zakaj jih mora jemati resno.

| Načela                 | Microsoftova definicija                                | Premisleki za razvijalca klepeta                                   | Zakaj je pomembno                                                                     |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| Poštenost              | AI sistemi naj bi vse ljudi obravnavali pravično.     | Zagotovite, da klepetalna aplikacija ne diskriminira na podlagi uporabniških podatkov. | Za izgradnjo zaupanja in vključenosti med uporabniki; preprečuje pravne posledice.  |
| Zanesljivost in varnost | AI sistemi naj delujejo zanesljivo in varno.          | Izvedite testiranja in varnostne ukrepe za zmanjšanje napak in tveganj.         | Zagotavlja zadovoljstvo uporabnikov in preprečuje morebitno škodo.                   |
| Zasebnost in varnost   | AI sistemi naj bodo varni in spoštujejo zasebnost.    | Uvedite močno šifriranje in ukrepe za zaščito podatkov.                        | Za varovanje občutljivih uporabniških podatkov in upoštevanje zakonov o zasebnosti.  |
| Vključenost            | AI sistemi naj opolnomočijo vse in vključujejo ljudi. | Oblikujte UI/UX, ki je dostopna in enostavna za uporabo različnim občinstvom. | Zagotavlja, da lahko širši krog ljudi učinkovito uporablja aplikacijo.               |
| Transparentnost        | AI sistemi naj bodo razumljivi.                        | Zagotovite jasno dokumentacijo in pojasnila za AI odzive.                       | Uporabniki bolj zaupajo sistemu, če razumejo, kako so sprejete odločitve.           |
| Odgovornost            | Ljudje naj so odgovorni za AI sisteme.                | Vzpostavite jasen proces za revizijo in izboljševanje AI odločitev.             | Omogoča stalno izboljševanje in korektivne ukrepe v primeru napak.                   |

## Naloga

Glej [nalogo](../../../07-building-chat-applications/python). Ta vas bo vodila skozi vrsto vaj od izvajanja prvih klepetalnih ukazov do razvrščanja in povzemanja besedila in še več. Opazite, da so naloge na voljo v različnih programskih jezikih!

## Odlično delo! Nadaljujte pot

Po končani tej lekciji si oglejte našo [Zbirko za učenje Generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgrajevanjem svojega znanja o Generativni AI!

Pojdite na Lekcijo 8, da vidite, kako lahko začnete [graditi iskalne aplikacije](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->