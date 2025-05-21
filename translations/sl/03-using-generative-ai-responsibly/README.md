<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:53:18+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "sl"
}
-->
# Uporaba generativne umetne inteligence odgovorno

> _Kliknite na zgornjo sliko za ogled videa te lekcije_

Zlahka se je navdušiti nad umetno inteligenco, še posebej generativno umetno inteligenco, vendar je treba razmisliti, kako jo uporabljati odgovorno. Treba je razmisliti o tem, kako zagotoviti, da je rezultat pravičen, neškodljiv in še več. Ta poglavje vam želi ponuditi omenjeni kontekst, kaj je treba upoštevati in kako sprejeti aktivne korake za izboljšanje vaše uporabe umetne inteligence.

## Uvod

Ta lekcija bo obravnavala:

- Zakaj bi morali pri gradnji aplikacij generativne umetne inteligence dati prednost odgovorni umetni inteligenci.
- Osnovna načela odgovorne umetne inteligence in kako se nanašajo na generativno umetno inteligenco.
- Kako uresničiti ta načela odgovorne umetne inteligence s strategijo in orodji.

## Cilji učenja

Po končani lekciji boste vedeli:

- Pomembnost odgovorne umetne inteligence pri gradnji aplikacij generativne umetne inteligence.
- Kdaj razmisliti in uporabiti osnovna načela odgovorne umetne inteligence pri gradnji aplikacij generativne umetne inteligence.
- Katera orodja in strategije so vam na voljo za uresničitev koncepta odgovorne umetne inteligence.

## Načela odgovorne umetne inteligence

Navdušenje nad generativno umetno inteligenco še nikoli ni bilo večje. To navdušenje je prineslo veliko novih razvijalcev, pozornosti in financiranja na tem področju. Čeprav je to zelo pozitivno za vsakogar, ki želi graditi izdelke in podjetja z uporabo generativne umetne inteligence, je pomembno, da ravnamo odgovorno.

V tem tečaju se osredotočamo na gradnjo našega startupa in našega izobraževalnega produkta umetne inteligence. Uporabili bomo načela odgovorne umetne inteligence: pravičnost, vključenost, zanesljivost/varnost, varnost in zasebnost, preglednost in odgovornost. S temi načeli bomo raziskali, kako se nanašajo na našo uporabo generativne umetne inteligence v naših izdelkih.

## Zakaj bi morali dati prednost odgovorni umetni inteligenci

Pri gradnji izdelka pristop, ki je osredotočen na človeka in upošteva najboljše interese uporabnika, vodi do najboljših rezultatov.

Edinstvenost generativne umetne inteligence je njena moč, da ustvari koristne odgovore, informacije, usmeritve in vsebino za uporabnike. To je mogoče storiti brez veliko ročnih korakov, kar lahko vodi do zelo impresivnih rezultatov. Brez ustreznega načrtovanja in strategij lahko žal vodi tudi do nekaterih škodljivih rezultatov za vaše uporabnike, vaš izdelek in družbo kot celoto.

Poglejmo si nekaj (vendar ne vseh) teh potencialno škodljivih rezultatov:

### Halucinacije

Halucinacije so izraz, ki opisuje, ko LLM ustvari vsebino, ki je bodisi popolnoma nesmiselna bodisi nekaj, kar vemo, da je dejansko napačno na podlagi drugih virov informacij.

Recimo, da zgradimo funkcijo za naš startup, ki omogoča študentom, da modelu zastavijo zgodovinska vprašanja. Študent zastavi vprašanje `Who was the sole survivor of Titanic?`

Model ustvari odgovor, kot je spodnji:

To je zelo samozavesten in temeljit odgovor. Na žalost je napačen. Tudi z minimalno količino raziskav bi ugotovili, da je bilo več kot en preživeli katastrofe Titanika. Za študenta, ki šele začenja raziskovati to temo, je ta odgovor lahko dovolj prepričljiv, da ga ne bo vprašal in obravnaval kot dejstvo. Posledice tega lahko vodijo v nezanesljivost sistema umetne inteligence in negativno vplivajo na ugled našega startupa.

Z vsako iteracijo kateregakoli danega LLM smo videli izboljšave zmogljivosti pri zmanjševanju halucinacij. Tudi s to izboljšavo moramo kot graditelji aplikacij in uporabniki ostati pozorni na te omejitve.

### Škodljiva vsebina

V prejšnjem razdelku smo obravnavali, ko LLM ustvari napačne ali nesmiselne odgovore. Drugo tveganje, na katerega moramo biti pozorni, je, ko model odgovori s škodljivo vsebino.

Škodljiva vsebina je lahko opredeljena kot:

- Nudenje navodil ali spodbujanje k samopoškodbam ali škodi določenim skupinam.
- Sovražna ali poniževalna vsebina.
- Usmerjanje k načrtovanju kakršnih koli napadov ali nasilnih dejanj.
- Nudenje navodil, kako najti nezakonito vsebino ali storiti nezakonita dejanja.
- Prikazovanje spolno eksplicitne vsebine.

Za naš startup želimo zagotoviti, da imamo prava orodja in strategije, da preprečimo, da bi tovrstna vsebina bila videna s strani študentov.

### Pomanjkanje pravičnosti

Pravičnost je opredeljena kot "zagotavljanje, da je sistem umetne inteligence brez pristranskosti in diskriminacije ter da obravnava vse pošteno in enakopravno." V svetu generativne umetne inteligence želimo zagotoviti, da izključujoči pogledi marginaliziranih skupin niso okrepljeni z izhodom modela.

Takšne vrste izhodov niso le uničujoče za gradnjo pozitivnih izkušenj izdelkov za naše uporabnike, temveč povzročajo tudi nadaljnjo družbeno škodo. Kot graditelji aplikacij bi morali vedno imeti široko in raznoliko bazo uporabnikov v mislih pri gradnji rešitev z generativno umetno inteligenco.

## Kako uporabljati generativno umetno inteligenco odgovorno

Sedaj, ko smo opredelili pomembnost odgovorne generativne umetne inteligence, si poglejmo 4 korake, ki jih lahko sprejmemo, da odgovorno gradimo naše AI rešitve:

### Merjenje potencialnih škod

Pri testiranju programske opreme testiramo pričakovane akcije uporabnika na aplikaciji. Podobno je testiranje raznolikega nabora pozivov, ki jih uporabniki najverjetneje bodo uporabili, dober način za merjenje potencialne škode.

Ker naš startup gradi izobraževalni produkt, bi bilo dobro pripraviti seznam pozivov povezanih z izobraževanjem. To bi lahko zajemalo določeno temo, zgodovinska dejstva in pozive o študentskem življenju.

### Zmanjšanje potencialnih škod

Sedaj je čas, da poiščemo načine, kjer lahko preprečimo ali omejimo potencialno škodo, ki jo povzroča model in njegovi odgovori. To lahko obravnavamo v 4 različnih slojih:

- **Model**. Izbira pravega modela za pravi primer uporabe. Večji in bolj kompleksni modeli, kot je GPT-4, lahko povzročijo večje tveganje za škodljivo vsebino, ko se uporabijo za manjše in bolj specifične primere uporabe. Uporaba vaših podatkov za fino nastavitev prav tako zmanjša tveganje za škodljivo vsebino.

- **Varnostni sistem**. Varnostni sistem je niz orodij in konfiguracij na platformi, ki služi modelu in pomaga zmanjšati škodo. Primer tega je sistem filtriranja vsebine na storitvi Azure OpenAI. Sistemi bi morali tudi zaznati napade z izogibanjem in nezaželeno aktivnost, kot so zahteve od botov.

- **Metaprompt**. Metaprompti in utemeljitev so načini, kako lahko usmerimo ali omejimo model na podlagi določenih vedenj in informacij. To bi lahko bilo uporaba sistemskih vnosov za določitev določenih omejitev modela. Poleg tega nudenje izhodov, ki so bolj relevantni za obseg ali domeno sistema.

Lahko se tudi uporabi tehnike, kot je Generacija z obogatitvijo pridobivanja (RAG), da model pridobi informacije samo iz izbora zaupanja vrednih virov. Kasneje v tem tečaju je lekcija za [gradnjo iskalnih aplikacij](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Uporabniška izkušnja**. Končni sloj je, kjer uporabnik neposredno sodeluje z modelom prek vmesnika naše aplikacije na nek način. Na ta način lahko oblikujemo UI/UX, da omejimo uporabnika glede vrste vnosov, ki jih lahko pošlje modelu, kot tudi besedilo ali slike, prikazane uporabniku. Pri uvajanju AI aplikacije moramo biti tudi transparentni glede tega, kaj naša aplikacija generativne umetne inteligence lahko in česa ne more storiti.

Imamo celotno lekcijo, posvečeno [Oblikovanju UX za AI aplikacije](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Ocenjevanje modela**. Delo z LLM-ji je lahko zahtevno, ker nimamo vedno nadzora nad podatki, na katerih je bil model usposobljen. Kljub temu bi morali vedno oceniti zmogljivost in izhode modela. Še vedno je pomembno meriti natančnost modela, podobnost, utemeljenost in relevantnost izhoda. To pomaga zagotoviti preglednost in zaupanje deležnikom ter uporabnikom.

### Upravljanje odgovorne generativne AI rešitve

Gradnja operativne prakse okoli vaših AI aplikacij je končna faza. To vključuje partnerstvo z drugimi deli našega startupa, kot sta pravni in varnostni oddelek, da zagotovimo skladnost z vsemi regulativnimi politikami. Pred lansiranjem želimo tudi zgraditi načrte okoli dostave, obravnave incidentov in povratka, da preprečimo kakršno koli škodo našim uporabnikom pri rasti.

## Orodja

Čeprav se zdi delo razvoja rešitev odgovorne umetne inteligence veliko, je delo zelo vredno truda. Ko področje generativne umetne inteligence raste, se bo več orodij za pomoč razvijalcem pri učinkovitem vključevanju odgovornosti v njihove delovne tokove razvijalo. Na primer, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) lahko pomaga zaznati škodljivo vsebino in slike prek zahteve API.

## Preverjanje znanja

Na kaj morate biti pozorni, da zagotovite odgovorno uporabo umetne inteligence?

1. Da je odgovor pravilen.
2. Škodljiva uporaba, da umetna inteligenca ni uporabljena za kriminalne namene.
3. Zagotavljanje, da je umetna inteligenca brez pristranskosti in diskriminacije.

A: 2 in 3 sta pravilna. Odgovorna umetna inteligenca vam pomaga razmisliti, kako zmanjšati škodljive učinke in pristranskosti ter več.

## 🚀 Izziv

Preberite o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) in preverite, kaj lahko sprejmete za svojo uporabo.

## Odlično delo, nadaljujte z učenjem

Po končani lekciji si oglejte našo [Generativno AI zbirko učenja](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o generativni umetni inteligenci!

Pojdite na Lekcijo 4, kjer si bomo ogledali [Osnove inženiringa pozivov](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Omejitev odgovornosti**: 
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljivo profesionalno človeško prevajanje. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.