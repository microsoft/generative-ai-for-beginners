<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:35:12+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "sl"
}
-->
# Uporaba generativne umetne inteligence odgovorno

> _Kliknite zgornjo sliko za ogled videa te lekcije_

Enostavno je biti fasciniran z umetno inteligenco, še posebej z generativno umetno inteligenco, vendar morate razmisliti, kako jo uporabljati odgovorno. Razmisliti morate o stvareh, kot so zagotavljanje, da je izhod pošten, neškodljiv in še več. Ta poglavje si prizadeva, da vam zagotovi omenjeni kontekst, kaj upoštevati in kako sprejeti aktivne korake za izboljšanje uporabe vaše umetne inteligence.

## Uvod

Ta lekcija bo zajela:

- Zakaj bi morali dati prednost odgovorni umetni inteligenci pri gradnji aplikacij z generativno umetno inteligenco.
- Temeljna načela odgovorne umetne inteligence in kako se nanašajo na generativno umetno inteligenco.
- Kako ta načela odgovorne umetne inteligence uresničiti skozi strategijo in orodja.

## Cilji učenja

Po zaključku te lekcije boste vedeli:

- Pomen odgovorne umetne inteligence pri gradnji aplikacij z generativno umetno inteligenco.
- Kdaj razmišljati in uporabiti temeljna načela odgovorne umetne inteligence pri gradnji aplikacij z generativno umetno inteligenco.
- Katera orodja in strategije so vam na voljo, da koncept odgovorne umetne inteligence uresničite.

## Načela odgovorne umetne inteligence

Navdušenje nad generativno umetno inteligenco še nikoli ni bilo večje. To navdušenje je prineslo veliko novih razvijalcev, pozornosti in financiranja v ta prostor. Čeprav je to zelo pozitivno za vsakogar, ki želi graditi izdelke in podjetja z uporabo generativne umetne inteligence, je prav tako pomembno, da nadaljujemo odgovorno.

V tem tečaju se osredotočamo na gradnjo našega startup podjetja in našega izobraževalnega produkta umetne inteligence. Uporabili bomo načela odgovorne umetne inteligence: poštenost, vključenost, zanesljivost/varnost, varnost in zasebnost, preglednost in odgovornost. S temi načeli bomo raziskali, kako se nanašajo na našo uporabo generativne umetne inteligence v naših izdelkih.

## Zakaj bi morali dati prednost odgovorni umetni inteligenci

Pri gradnji produkta, humanocentrični pristop, ki upošteva najboljše interese vaših uporabnikov, vodi do najboljših rezultatov.

Edinstvenost generativne umetne inteligence je njena moč ustvariti koristne odgovore, informacije, smernice in vsebino za uporabnike. To je mogoče storiti brez številnih ročnih korakov, kar lahko vodi do zelo impresivnih rezultatov. Brez ustreznega načrtovanja in strategij lahko na žalost privede tudi do nekaterih škodljivih rezultatov za vaše uporabnike, vaš produkt in družbo kot celoto.

Poglejmo nekaj (a ne vseh) teh potencialno škodljivih rezultatov:

### Halucinacije

Halucinacije so izraz, ki se uporablja za opis, ko LLM ustvari vsebino, ki je bodisi popolnoma nesmiselna ali nekaj, kar vemo, da je dejansko napačno na podlagi drugih virov informacij.

Recimo, da zgradimo funkcijo za naš startup, ki omogoča študentom, da postavljajo zgodovinska vprašanja modelu. Študent postavi vprašanje `Who was the sole survivor of Titanic?`

Model ustvari odgovor, kot je prikazano spodaj:

To je zelo samozavesten in temeljit odgovor. Na žalost je napačen. Tudi z minimalno količino raziskav bi nekdo odkril, da je bilo več kot en preživel Titanic katastrofo. Za študenta, ki šele začenja raziskovati to temo, je ta odgovor lahko dovolj prepričljiv, da ga ne bo vprašal in obravnaval kot dejstvo. Posledice tega lahko privedejo do tega, da je sistem umetne inteligence nezanesljiv in negativno vpliva na ugled našega startup podjetja.

Pri vsaki iteraciji kateregakoli LLM smo opazili izboljšave zmogljivosti glede minimiziranja halucinacij. Tudi s to izboljšavo moramo kot graditelji aplikacij in uporabniki še vedno ostati pozorni na te omejitve.

### Škodljiva vsebina

V prejšnjem razdelku smo obravnavali, ko LLM ustvari napačne ali nesmiselne odgovore. Drugo tveganje, ki se ga moramo zavedati, je, ko model odgovori s škodljivo vsebino.

Škodljiva vsebina je lahko opredeljena kot:

- Nudenje navodil ali spodbujanje samopoškodovanja ali škodovanja določenim skupinam.
- Sovražna ali ponižujoča vsebina.
- Usmerjanje načrtovanja kakršnekoli vrste napada ali nasilnih dejanj.
- Nudenje navodil, kako najti nezakonito vsebino ali storiti nezakonita dejanja.
- Prikazovanje spolno eksplicitne vsebine.

Za naš startup želimo poskrbeti, da imamo ustrezna orodja in strategije za preprečevanje, da bi ta vrsta vsebine bila vidna študentom.

### Pomanjkanje poštenosti

Poštenost je opredeljena kot "zagotavljanje, da je sistem umetne inteligence brez pristranskosti in diskriminacije ter da obravnava vse pošteno in enako." V svetu generativne umetne inteligence želimo zagotoviti, da izključevalni svetovni pogledi marginaliziranih skupin niso ojačani z izhodom modela.

Takšni izhodi niso samo destruktivni za gradnjo pozitivnih izkušenj izdelka za naše uporabnike, ampak povzročajo tudi nadaljnjo družbeno škodo. Kot graditelji aplikacij bi morali vedno upoštevati široko in raznoliko bazo uporabnikov pri gradnji rešitev z generativno umetno inteligenco.

## Kako uporabljati generativno umetno inteligenco odgovorno

Sedaj, ko smo opredelili pomen odgovorne generativne umetne inteligence, si poglejmo 4 korake, ki jih lahko sprejmemo za gradnjo naših rešitev umetne inteligence odgovorno:

### Merjenje potencialnih škod

Pri testiranju programske opreme testiramo pričakovane akcije uporabnika na aplikaciji. Podobno je testiranje raznolikega nabora pozivov, ki jih bodo uporabniki najverjetneje uporabili, dober način za merjenje potencialnih škod.

Ker naš startup gradi izobraževalni produkt, bi bilo dobro pripraviti seznam izobraževalnih pozivov. To bi lahko zajemalo določen predmet, zgodovinska dejstva in pozive o študentskem življenju.

### Zmanjšanje potencialnih škod

Sedaj je čas, da najdemo načine, kako lahko preprečimo ali omejimo potencialno škodo, ki jo povzroči model in njegovi odgovori. To lahko obravnavamo na 4 različnih plasteh:

- **Model**. Izbira pravega modela za pravi primer uporabe. Večji in bolj kompleksni modeli, kot je GPT-4, lahko povzročijo večje tveganje škodljive vsebine, ko se uporabljajo za manjše in bolj specifične primere uporabe. Uporaba vaših podatkov za usposabljanje za fino nastavitev prav tako zmanjšuje tveganje škodljive vsebine.

- **Varnostni sistem**. Varnostni sistem je niz orodij in konfiguracij na platformi, ki služi modelu in pomaga zmanjšati škodo. Primer tega je sistem filtriranja vsebine na storitvi Azure OpenAI. Sistemi bi morali tudi zaznati napade jailbreak in neželeno dejavnost, kot so zahteve botov.

- **Metaprompt**. Metaprompti in utemeljitev so načini, kako lahko usmerjamo ali omejujemo model na podlagi določenih vedenj in informacij. To bi lahko bilo uporaba sistemskih vhodov za določitev določenih omejitev modela. Poleg tega nudenje izhodov, ki so bolj relevantni za obseg ali področje sistema.

To lahko vključuje tudi uporabo tehnik, kot je pridobivanje z okrepljeno generacijo (RAG), da model črpa informacije samo iz izbora zaupanja vrednih virov. Kasneje v tem tečaju je lekcija za [gradnjo iskalnih aplikacij](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Uporabniška izkušnja**. Končna plast je, kjer uporabnik neposredno interagira z modelom prek vmesnika naše aplikacije na nek način. Na ta način lahko oblikujemo UI/UX, da omejimo uporabnika glede vrste vhodov, ki jih lahko pošlje modelu, kot tudi besedilo ali slike, prikazane uporabniku. Pri uvajanju aplikacije umetne inteligence moramo biti tudi pregledni glede tega, kaj lahko naša generativna aplikacija umetne inteligence naredi in česa ne more.

Imamo celotno lekcijo, posvečeno [Oblikovanju UX za AI aplikacije](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Ocena modela**. Delo z LLM-ji je lahko izziv, ker nimamo vedno nadzora nad podatki, na katerih je bil model usposobljen. Kljub temu bi morali vedno oceniti zmogljivost in izhode modela. Še vedno je pomembno meriti natančnost, podobnost, utemeljenost in relevantnost izhoda modela. To pomaga zagotoviti preglednost in zaupanje deležnikom in uporabnikom.

### Upravljanje odgovorne rešitve generativne umetne inteligence

Gradnja operativne prakse okoli vaših aplikacij umetne inteligence je končna faza. To vključuje partnerstvo z drugimi deli našega startup podjetja, kot sta pravna in varnostna služba, da zagotovimo skladnost z vsemi regulativnimi politikami. Pred lansiranjem želimo tudi zgraditi načrte okoli dostave, obravnavanja incidentov in vračanja, da preprečimo kakršnokoli škodo našim uporabnikom.

## Orodja

Čeprav se delo pri razvoju rešitev odgovorne umetne inteligence morda zdi veliko, je to delo, ki se izplača. Ko področje generativne umetne inteligence raste, bo več orodij, ki bodo razvijalcem pomagala učinkovito vključiti odgovornost v njihove delovne tokove, dozorelo. Na primer, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) lahko pomaga zaznati škodljivo vsebino in slike prek zahteve API.

## Preverjanje znanja

Na kaj morate biti pozorni, da zagotovite odgovorno uporabo umetne inteligence?

1. Da je odgovor pravilen.
1. Škodljiva uporaba, da umetna inteligenca ni uporabljena za kriminalne namene.
1. Zagotavljanje, da je umetna inteligenca brez pristranskosti in diskriminacije.

A: 2 in 3 sta pravilna. Odgovorna umetna inteligenca vam pomaga razmisliti, kako omiliti škodljive učinke in pristranskosti ter še več.

## 🚀 Izziv

Preberite o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) in preverite, kaj lahko sprejmete za svojo uporabo.

## Odlično delo, nadaljujte z učenjem

Po zaključku te lekcije si oglejte našo [Generativno AI zbirko znanja](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgrajevanjem svojega znanja o generativni umetni inteligenci!

Pojdite na lekcijo 4, kjer si bomo ogledali [Osnove inženiringa pozivov](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Omejitev odgovornosti**: 
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.