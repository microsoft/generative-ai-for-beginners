<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5308963a56cfbad2d73b0fa99fe84b3",
  "translation_date": "2025-10-18T01:44:39+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "sl"
}
-->
# Gradnja klepetalnih aplikacij z generativno umetno inteligenco

[![Gradnja klepetalnih aplikacij z generativno umetno inteligenco](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.sl.png)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Kliknite na zgornjo sliko za ogled videoposnetka te lekcije)_

Zdaj, ko smo videli, kako lahko zgradimo aplikacije za generiranje besedil, si poglejmo še klepetalne aplikacije.

Klepetalne aplikacije so postale del našega vsakdana in ponujajo več kot le sredstvo za priložnostne pogovore. So ključni del storitev za stranke, tehnične podpore in celo naprednih svetovalnih sistemov. Verjetno ste pred kratkim že prejeli pomoč prek klepetalne aplikacije. Z vključevanjem naprednih tehnologij, kot je generativna umetna inteligenca, v te platforme se povečuje njihova kompleksnost, hkrati pa tudi izzivi.

Nekatera vprašanja, na katera moramo odgovoriti, so:

- **Gradnja aplikacije**. Kako učinkovito zgraditi in brezhibno integrirati te aplikacije, ki jih poganja umetna inteligenca, za specifične primere uporabe?
- **Spremljanje**. Ko so aplikacije uvedene, kako lahko spremljamo in zagotovimo, da delujejo na najvišji ravni kakovosti, tako glede funkcionalnosti kot tudi v skladu z [šestimi načeli odgovorne umetne inteligence](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Ko se vse bolj pomikamo v dobo, ki jo opredeljuje avtomatizacija in brezhibna interakcija med človekom in strojem, postaja razumevanje, kako generativna umetna inteligenca preoblikuje obseg, globino in prilagodljivost klepetalnih aplikacij, ključnega pomena. Ta lekcija bo raziskala vidike arhitekture, ki podpirajo te zapletene sisteme, se poglobila v metodologije za njihovo prilagajanje specifičnim nalogam in ocenila metrike ter premisleke, pomembne za zagotavljanje odgovorne uporabe umetne inteligence.

## Uvod

Ta lekcija zajema:

- Tehnike za učinkovito gradnjo in integracijo klepetalnih aplikacij.
- Kako prilagoditi in optimizirati aplikacije.
- Strategije in premisleke za učinkovito spremljanje klepetalnih aplikacij.

## Cilji učenja

Do konca te lekcije boste lahko:

- Opisali premisleke za gradnjo in integracijo klepetalnih aplikacij v obstoječe sisteme.
- Prilagodili klepetalne aplikacije za specifične primere uporabe.
- Prepoznali ključne metrike in premisleke za učinkovito spremljanje in vzdrževanje kakovosti klepetalnih aplikacij, ki jih poganja umetna inteligenca.
- Zagotovili, da klepetalne aplikacije odgovorno uporabljajo umetno inteligenco.

## Integracija generativne umetne inteligence v klepetalne aplikacije

Izboljšanje klepetalnih aplikacij z generativno umetno inteligenco ni osredotočeno le na to, da postanejo pametnejše; gre za optimizacijo njihove arhitekture, zmogljivosti in uporabniškega vmesnika za zagotavljanje kakovostne uporabniške izkušnje. To vključuje raziskovanje arhitekturnih temeljev, integracij API-jev in premislekov o uporabniškem vmesniku. Ta razdelek vam želi ponuditi celovit načrt za navigacijo po teh zapletenih področjih, ne glede na to, ali jih vključujete v obstoječe sisteme ali jih gradite kot samostojne platforme.

Do konca tega razdelka boste opremljeni z znanjem, potrebnim za učinkovito gradnjo in vključevanje klepetalnih aplikacij.

### Klepetalni robot ali klepetalna aplikacija?

Preden se poglobimo v gradnjo klepetalnih aplikacij, primerjajmo 'klepetalne robote' in 'klepetalne aplikacije, ki jih poganja umetna inteligenca', ki imajo različne vloge in funkcionalnosti. Glavni namen klepetalnega robota je avtomatizacija specifičnih nalog pogovora, kot so odgovarjanje na pogosto zastavljena vprašanja ali sledenje paketu. Običajno ga vodi logika, ki temelji na pravilih, ali zapleteni algoritmi umetne inteligence. Nasprotno pa je klepetalna aplikacija, ki jo poganja umetna inteligenca, veliko širše okolje, zasnovano za omogočanje različnih oblik digitalne komunikacije, kot so besedilni, glasovni in video klepeti med človeškimi uporabniki. Njena ključna značilnost je integracija generativnega modela umetne inteligence, ki simulira nianse, človeško podobne pogovore, in generira odgovore na podlagi širokega spektra vhodnih podatkov in kontekstualnih namigov. Klepetalna aplikacija, ki jo poganja generativna umetna inteligenca, se lahko vključuje v odprte pogovore, prilagaja spreminjajočim se kontekstom pogovora in celo ustvarja ustvarjalne ali zapletene dialoge.

Spodnja tabela prikazuje ključne razlike in podobnosti, ki nam pomagajo razumeti njihove edinstvene vloge v digitalni komunikaciji.

| Klepetalni robot                     | Klepetalna aplikacija, ki jo poganja generativna umetna inteligenca |
| ------------------------------------ | ------------------------------------------------------------------ |
| Osredotočen na naloge in temelji na pravilih | Zavedanje konteksta                                                |
| Pogosto integriran v večje sisteme   | Lahko gosti enega ali več klepetalnih robotov                      |
| Omejen na programirane funkcije      | Vključuje modele generativne umetne inteligence                    |
| Specializirane in strukturirane interakcije | Sposobnost odprtih pogovorov                                       |

### Uporaba vnaprej pripravljenih funkcionalnosti z SDK-ji in API-ji

Pri gradnji klepetalne aplikacije je odličen prvi korak oceniti, kaj že obstaja. Uporaba SDK-jev in API-jev za gradnjo klepetalnih aplikacij je koristna strategija iz več razlogov. Z integracijo dobro dokumentiranih SDK-jev in API-jev strateško postavljate svojo aplikacijo za dolgoročni uspeh, pri čemer se ukvarjate z vprašanji skalabilnosti in vzdrževanja.

- **Pospeši razvojni proces in zmanjša stroške**: Zanašanje na vnaprej pripravljene funkcionalnosti namesto na drage procese lastne gradnje vam omogoča, da se osredotočite na druge vidike svoje aplikacije, ki so morda pomembnejši, na primer poslovno logiko.
- **Boljša zmogljivost**: Pri gradnji funkcionalnosti iz nič se boste slej ko prej vprašali: "Kako se to razširi? Ali je ta aplikacija sposobna obvladati nenaden porast uporabnikov?" Dobro vzdrževani SDK-ji in API-ji pogosto vključujejo rešitve za te skrbi.
- **Lažje vzdrževanje**: Posodobitve in izboljšave so lažje za upravljanje, saj večina API-jev in SDK-jev zahteva le posodobitev knjižnice, ko je izdana novejša različica.
- **Dostop do najsodobnejše tehnologije**: Uporaba modelov, ki so bili fino nastavljeni in usposobljeni na obsežnih podatkovnih nizih, zagotavlja vaši aplikaciji naravne jezikovne zmogljivosti.

Dostop do funkcionalnosti SDK-ja ali API-ja običajno vključuje pridobitev dovoljenja za uporabo ponujenih storitev, kar se pogosto izvede z uporabo edinstvenega ključa ali avtentikacijskega žetona. Za raziskovanje, kako to izgleda, bomo uporabili knjižnico OpenAI Python. To lahko preizkusite tudi sami v naslednjem [zvezku za OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) ali [zvezku za Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) za to lekcijo.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Zgornji primer uporablja model GPT-3.5 Turbo za dokončanje poziva, vendar opazite, da je API ključ nastavljen pred tem. Če ključa ne bi nastavili, bi prejeli napako.

## Uporabniška izkušnja (UX)

Splošna načela uporabniške izkušnje veljajo za klepetalne aplikacije, vendar so tukaj nekateri dodatni premisleki, ki postanejo še posebej pomembni zaradi komponent strojnega učenja.

- **Mehanizem za reševanje nejasnosti**: Generativni modeli umetne inteligence občasno ustvarijo nejasne odgovore. Funkcija, ki uporabnikom omogoča, da zahtevajo pojasnila, je lahko koristna, če naletijo na to težavo.
- **Ohranjanje konteksta**: Napredni generativni modeli umetne inteligence imajo sposobnost zapomniti si kontekst v pogovoru, kar je lahko nujna prednost za uporabniško izkušnjo. Uporabnikom omogočiti nadzor in upravljanje konteksta izboljša uporabniško izkušnjo, vendar prinaša tveganje za shranjevanje občutljivih uporabniških informacij. Premisleki o tem, kako dolgo se te informacije shranjujejo, na primer z uvedbo politike hrambe, lahko uravnotežijo potrebo po kontekstu in zasebnosti.
- **Personalizacija**: S sposobnostjo učenja in prilagajanja modeli umetne inteligence ponujajo individualizirano izkušnjo za uporabnika. Prilagajanje uporabniške izkušnje s funkcijami, kot so uporabniški profili, ne le da uporabnika naredi razumljenega, ampak mu tudi pomaga pri iskanju specifičnih odgovorov, kar ustvarja bolj učinkovito in zadovoljivo interakcijo.

Eden takšnih primerov personalizacije je nastavitev "Custom instructions" v OpenAI-jevem ChatGPT. Omogoča vam, da zagotovite informacije o sebi, ki so lahko pomemben kontekst za vaše pozive. Tukaj je primer prilagojene nastavitve.

![Nastavitve prilagojenih navodil v ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.sl.png)

Ta "profil" ChatGPT-ju omogoča ustvarjanje učnega načrta o povezanih seznamih. Opazite, da ChatGPT upošteva, da uporabnik morda želi bolj poglobljen učni načrt glede na njene izkušnje.

![Poziv v ChatGPT za učni načrt o povezanih seznamih](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.sl.png)

### Microsoftov okvir sistemskih sporočil za velike jezikovne modele

[Microsoft je zagotovil smernice](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) za pisanje učinkovitih sistemskih sporočil pri generiranju odgovorov iz velikih jezikovnih modelov, razdeljene na 4 področja:

1. Določitev, za koga je model namenjen, ter njegovih zmožnosti in omejitev.
2. Določitev formata izhoda modela.
3. Zagotavljanje specifičnih primerov, ki prikazujejo želeno vedenje modela.
4. Zagotavljanje dodatnih varoval za vedenje.

### Dostopnost

Ne glede na to, ali ima uporabnik težave z vidom, sluhom, motorične ali kognitivne težave, mora biti dobro zasnovana klepetalna aplikacija dostopna vsem. Naslednji seznam razčlenjuje specifične funkcije, namenjene izboljšanju dostopnosti za različne uporabniške omejitve.

- **Funkcije za slabovidne**: Teme z visokim kontrastom in prilagodljiva velikost besedila, združljivost z bralniki zaslona.
- **Funkcije za naglušne**: Funkcije za pretvorbo besedila v govor in govora v besedilo, vizualni kazalniki za zvočna obvestila.
- **Funkcije za motorične težave**: Podpora za navigacijo s tipkovnico, glasovni ukazi.
- **Funkcije za kognitivne težave**: Možnosti poenostavljenega jezika.

## Prilagoditev in fino nastavljanje za jezikovne modele specifičnih domen

Predstavljajte si klepetalno aplikacijo, ki razume žargon vašega podjetja in predvideva specifična vprašanja, ki jih ima njena uporabniška baza. Obstajata dva pristopa, ki ju je vredno omeniti:

- **Uporaba modelov DSL**. DSL pomeni jezik specifične domene. Uporabite lahko tako imenovani DSL model, usposobljen na specifičnem področju, da razume njegove koncepte in scenarije.
- **Uporaba finega nastavljanja**. Fino nastavljanje je proces nadaljnjega usposabljanja vašega modela s specifičnimi podatki.

## Prilagoditev: Uporaba DSL

Uporaba jezikovnih modelov specifičnih domen (DSL modeli) lahko izboljša angažiranost uporabnikov z zagotavljanjem specializiranih, kontekstualno relevantnih interakcij. To je model, ki je usposobljen ali fino nastavljen za razumevanje in generiranje besedila, povezanega s specifičnim področjem, industrijo ali temo. Možnosti za uporabo DSL modela se lahko razlikujejo od usposabljanja enega od začetka do uporabe že obstoječih prek SDK-jev in API-jev. Druga možnost je fino nastavljanje, ki vključuje prilagoditev obstoječega predhodno usposobljenega modela za specifično področje.

## Prilagoditev: Uporaba finega nastavljanja

Fino nastavljanje se pogosto uporablja, kadar predhodno usposobljen model ne zadostuje za specializirano področje ali specifično nalogo.

Na primer, medicinska vprašanja so zapletena in zahtevajo veliko konteksta. Ko zdravnik postavi diagnozo pacientu, temelji na različnih dejavnikih, kot so življenjski slog ali predhodna stanja, in se lahko celo opira na nedavne medicinske članke za potrditev svoje diagnoze. V takšnih niansiranih scenarijih splošna klepetalna aplikacija, ki jo poganja umetna inteligenca, ne more biti zanesljiv vir.

### Scenarij: medicinska aplikacija

Razmislite o klepetalni aplikaciji, zasnovani za pomoč medicinskim strokovnjakom pri hitrem iskanju smernic za zdravljenje, interakcij med zdravili ali najnovejših raziskovalnih ugotovitev.

Splošni model je morda primeren za odgovarjanje na osnovna medicinska vprašanja ali zagotavljanje splošnih nasvetov, vendar se lahko sooči z naslednjimi težavami:

- **Zelo specifični ali zapleteni primeri**. Na primer, nevrolog lahko vpraša aplikacijo: "Kakšne so trenutne najboljše prakse za obvladovanje epilepsije, odporne na zdravila, pri otrocih?"
- **Pomanjkanje nedavnih napredkov**. Splošni model bi se lahko težko odzval z aktualnim odgovorom, ki vključuje najnovejše dosežke v nevrologiji in farmakologiji.

V takšnih primerih lahko fino nastavljanje modela s specializiranim medicinskim podatkovnim nizom bistveno izboljša njegovo sposobnost obravnavanja teh zapletenih medicinskih vprašanj bolj natančno in zanesljivo. To zahteva dostop do velikega in ustreznega podatkovnega niza, ki predstavlja izzive in vprašanja specifične za določeno področje.

## Premisleki za kakovostno izkušnjo klepeta, ki jo poganja umetna inteligenca

Ta razdelek opisuje merila za "visokokakovostne" klepetalne aplikacije, ki vključujejo zajemanje uporabnih metrik in upoštevanje okvira, ki odgovorno uporablja tehnologijo umetne inteligence.

### Ključne metrike

Za ohranjanje visokokakovostne zmogljivosti aplikacije je bistveno spremljanje ključnih metrik in premislekov. Te meritve ne zagotavljajo le funkcionalnosti aplikacije, temveč tudi ocenjujejo kakovost modela umetne inteligence in uporabniške izkušnje. Spodaj je seznam osnovnih, AI in uporabniških metrik, ki jih je treba upoštevati.

| Metrika                      | Definicija                                                                                                             | Premisleki za razvijalca klepeta                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Razpoložljivost**          | Meri čas, ko je aplikacija operativna in dostopna uporabnikom.                                                         | Kako boste zmanjšali čas nedelovanja?                                     |
| **Čas odgovora**             | Čas, ki ga aplikacija potrebuje za odgovor na uporabnikovo vprašanje.                                                  | Kako lahko optimizirate obdelavo poizvedb za izboljšanje časa odgovora?    |
| **Natančnost**               | Razmerje med
| **Odkrivanje anomalij**       | Orodja in tehnike za prepoznavanje nenavadnih vzorcev, ki ne ustrezajo pričakovanemu vedenju.                        | Kako boste reagirali na anomalije?                                        |

### Uvajanje odgovorne prakse umetne inteligence v klepetalne aplikacije

Microsoftov pristop k odgovorni umetni inteligenci je opredelil šest načel, ki naj usmerjajo razvoj in uporabo umetne inteligence. Spodaj so navedena načela, njihove definicije ter stvari, ki jih mora razvijalec klepetalnih aplikacij upoštevati, in zakaj so pomembne.

| Načela                 | Microsoftova definicija                              | Upoštevanje za razvijalca klepetalnih aplikacij                        | Zakaj je pomembno                                                                     |
| ---------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Poštenost              | Sistemi umetne inteligence naj obravnavajo vse ljudi pošteno. | Poskrbite, da aplikacija za klepet ne diskriminira na podlagi podatkov uporabnikov. | Za vzpostavitev zaupanja in vključevanja med uporabniki; izogibanje pravnim posledicam. |
| Zanesljivost in varnost| Sistemi umetne inteligence naj delujejo zanesljivo in varno. | Uvedite testiranje in varnostne mehanizme za zmanjšanje napak in tveganj. | Zagotavlja zadovoljstvo uporabnikov in preprečuje morebitno škodo.                     |
| Zasebnost in varnost   | Sistemi umetne inteligence naj bodo varni in spoštujejo zasebnost. | Uvedite močno šifriranje in ukrepe za zaščito podatkov.                | Za zaščito občutljivih podatkov uporabnikov in skladnost z zakoni o zasebnosti.         |
| Vključevanje           | Sistemi umetne inteligence naj opolnomočijo vse in vključujejo ljudi. | Oblikujte uporabniški vmesnik, ki je dostopen in enostaven za uporabo za raznolike skupine. | Zagotavlja, da lahko širok spekter ljudi učinkovito uporablja aplikacijo.              |
| Transparentnost        | Sistemi umetne inteligence naj bodo razumljivi.      | Zagotovite jasno dokumentacijo in razlago za odgovore umetne inteligence. | Uporabniki bolj zaupajo sistemu, če razumejo, kako so sprejete odločitve.               |
| Odgovornost            | Ljudje naj bodo odgovorni za sisteme umetne inteligence. | Vzpostavite jasen proces za pregledovanje in izboljšanje odločitev umetne inteligence. | Omogoča stalne izboljšave in korektivne ukrepe v primeru napak.                         |

## Naloga

Oglejte si [nalogo](../../../07-building-chat-applications/python). Vodila vas bo skozi vrsto vaj, od izvajanja prvih klepetalnih pozivov do razvrščanja in povzemanja besedila ter še več. Upoštevajte, da so naloge na voljo v različnih programskih jezikih!

## Odlično delo! Nadaljujte pot

Po zaključku te lekcije si oglejte našo [zbirko učenja o generativni umetni inteligenci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o generativni umetni inteligenci!

Pojdite na Lekcijo 8, da vidite, kako lahko začnete [graditi aplikacije za iskanje](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.