<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d57fad773cbeb69c5dd62e65c34200d",
  "translation_date": "2025-10-18T01:40:52+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "sl"
}
-->
# Uporaba generativne umetne inteligence odgovorno

[![Uporaba generativne umetne inteligence odgovorno](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.sl.png)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Kliknite zgornjo sliko za ogled videa te lekcije_

Generativna umetna inteligenca je fascinantna, vendar je pomembno razmisliti, kako jo uporabljati odgovorno. Pomembno je upoštevati, kako zagotoviti, da so rezultati pravični, neškodljivi in še več. Ta poglavje vam želi ponuditi kontekst, kaj upoštevati in kako sprejeti aktivne korake za izboljšanje uporabe umetne inteligence.

## Uvod

Ta lekcija bo obravnavala:

- Zakaj bi morali dati prednost odgovorni umetni inteligenci pri gradnji aplikacij z generativno umetno inteligenco.
- Temeljna načela odgovorne umetne inteligence in kako se nanašajo na generativno umetno inteligenco.
- Kako ta načela odgovorne umetne inteligence uresničiti s strategijo in orodji.

## Cilji učenja

Po zaključku te lekcije boste vedeli:

- Pomen odgovorne umetne inteligence pri gradnji aplikacij z generativno umetno inteligenco.
- Kdaj razmišljati o temeljnih načelih odgovorne umetne inteligence in jih uporabiti pri gradnji aplikacij z generativno umetno inteligenco.
- Katera orodja in strategije so na voljo za uresničitev koncepta odgovorne umetne inteligence.

## Načela odgovorne umetne inteligence

Navdušenje nad generativno umetno inteligenco je večje kot kdajkoli prej. To navdušenje je pritegnilo veliko novih razvijalcev, pozornosti in financiranja na tem področju. Čeprav je to zelo pozitivno za vse, ki želijo graditi izdelke in podjetja z generativno umetno inteligenco, je prav tako pomembno, da ravnamo odgovorno.

V tem tečaju se osredotočamo na gradnjo našega startupa in našega izobraževalnega produkta z umetno inteligenco. Uporabili bomo načela odgovorne umetne inteligence: pravičnost, vključenost, zanesljivost/varnost, varnost in zasebnost, transparentnost ter odgovornost. S temi načeli bomo raziskali, kako se nanašajo na našo uporabo generativne umetne inteligence v naših izdelkih.

## Zakaj bi morali dati prednost odgovorni umetni inteligenci

Pri gradnji izdelka je človeško usmerjen pristop, ki upošteva najboljše interese uporabnika, ključnega pomena za doseganje najboljših rezultatov.

Posebnost generativne umetne inteligence je njena sposobnost ustvarjanja koristnih odgovorov, informacij, nasvetov in vsebin za uporabnike. To je mogoče doseči brez številnih ročnih korakov, kar lahko vodi do zelo impresivnih rezultatov. Brez ustreznega načrtovanja in strategij pa lahko na žalost povzroči tudi škodljive rezultate za vaše uporabnike, vaš izdelek in družbo kot celoto.

Poglejmo nekaj (ne vseh) potencialno škodljivih rezultatov:

### Halucinacije

Halucinacije so izraz, ki opisuje, ko LLM ustvari vsebino, ki je bodisi popolnoma nesmiselna bodisi nekaj, kar vemo, da je dejansko napačno glede na druge vire informacij.

Recimo, da zgradimo funkcijo za naš startup, ki omogoča študentom, da modelu postavljajo zgodovinska vprašanja. Študent postavi vprašanje: `Kdo je bil edini preživeli Titanika?`

Model ustvari odgovor, kot je spodnji:

![Vprašanje: "Kdo je bil edini preživeli Titanika"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Vir: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

To je zelo samozavesten in podroben odgovor. Na žalost je napačen. Tudi z minimalno količino raziskav bi ugotovili, da je bilo več preživelih v katastrofi Titanika. Za študenta, ki šele začenja raziskovati to temo, je tak odgovor lahko dovolj prepričljiv, da ga ne bo podvomil in ga bo obravnaval kot dejstvo. Posledice tega lahko privedejo do nezanesljivosti sistema umetne inteligence in negativno vplivajo na ugled našega startupa.

Z vsako iteracijo določenega LLM smo opazili izboljšave zmogljivosti pri zmanjševanju halucinacij. Kljub tem izboljšavam moramo kot graditelji aplikacij in uporabniki ostati pozorni na te omejitve.

### Škodljiva vsebina

V prejšnjem razdelku smo obravnavali primere, ko LLM ustvari napačne ali nesmiselne odgovore. Drugo tveganje, na katerega moramo biti pozorni, je, ko model odgovori s škodljivo vsebino.

Škodljiva vsebina je lahko opredeljena kot:

- Podajanje navodil ali spodbujanje samopoškodovanja ali škodovanja določenim skupinam.
- Sovražna ali ponižujoča vsebina.
- Usmerjanje načrtovanja kakršnih koli napadov ali nasilnih dejanj.
- Podajanje navodil, kako najti nezakonito vsebino ali storiti nezakonita dejanja.
- Prikazovanje spolno eksplicitne vsebine.

Za naš startup želimo zagotoviti, da imamo na voljo prava orodja in strategije za preprečevanje prikaza tovrstne vsebine študentom.

### Pomanjkanje pravičnosti

Pravičnost je opredeljena kot "zagotavljanje, da je sistem umetne inteligence brez pristranskosti in diskriminacije ter da obravnava vse pravično in enakopravno." V svetu generativne umetne inteligence želimo zagotoviti, da izključujoči pogledi na marginalizirane skupine niso ojačani z izhodom modela.

Takšni izhodi ne le škodujejo gradnji pozitivnih izkušenj z izdelki za naše uporabnike, temveč povzročajo tudi dodatno družbeno škodo. Kot graditelji aplikacij bi morali vedno imeti v mislih široko in raznoliko bazo uporabnikov pri gradnji rešitev z generativno umetno inteligenco.

## Kako uporabljati generativno umetno inteligenco odgovorno

Zdaj, ko smo opredelili pomen odgovorne generativne umetne inteligence, si poglejmo 4 korake, ki jih lahko naredimo, da odgovorno gradimo naše rešitve z umetno inteligenco:

![Cikel zmanjševanja tveganj](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.sl.png)

### Merjenje potencialnih škod

Pri testiranju programske opreme testiramo pričakovane akcije uporabnika v aplikaciji. Podobno je testiranje raznolikega nabora pozivov, ki jih bodo uporabniki najverjetneje uporabili, dober način za merjenje potencialne škode.

Ker naš startup gradi izobraževalni produkt, bi bilo dobro pripraviti seznam pozivov, povezanih z izobraževanjem. To bi lahko vključevalo določene predmete, zgodovinska dejstva in pozive o študentskem življenju.

### Zmanjšanje potencialnih škod

Zdaj je čas, da najdemo načine, kako preprečiti ali omejiti potencialno škodo, ki jo povzroča model in njegovi odgovori. To lahko obravnavamo na 4 različnih ravneh:

![Plasti zmanjševanja tveganj](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.sl.png)

- **Model**. Izbira pravega modela za pravi primer uporabe. Večji in bolj zapleteni modeli, kot je GPT-4, lahko predstavljajo večje tveganje za škodljivo vsebino, če se uporabljajo za manjše in bolj specifične primere uporabe. Uporaba vaših podatkov za prilagoditev modela prav tako zmanjšuje tveganje za škodljivo vsebino.

- **Varnostni sistem**. Varnostni sistem je niz orodij in konfiguracij na platformi, ki služi modelu in pomaga zmanjšati škodo. Primer tega je sistem za filtriranje vsebine na storitvi Azure OpenAI. Sistemi bi morali zaznati tudi napade na varnost in neželeno dejavnost, kot so zahteve botov.

- **Metaprompt**. Metaprompti in utemeljitve so načini, kako lahko usmerimo ali omejimo model na podlagi določenih vedenj in informacij. To bi lahko vključevalo uporabo sistemskih vnosov za določanje določenih omejitev modela. Poleg tega pa zagotavljanje izhodov, ki so bolj relevantni za obseg ali področje sistema.

Lahko se uporablja tudi tehnike, kot je Retrieval Augmented Generation (RAG), da model pridobi informacije samo iz izbranih zaupanja vrednih virov. Kasneje v tem tečaju je lekcija o [gradnji iskalnih aplikacij](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Uporabniška izkušnja**. Zadnja plast je tam, kjer uporabnik neposredno komunicira z modelom prek vmesnika naše aplikacije. Na ta način lahko oblikujemo UI/UX, da omejimo uporabnika glede vrst vnosov, ki jih lahko pošlje modelu, kot tudi glede besedila ali slik, prikazanih uporabniku. Pri uvajanju aplikacije z umetno inteligenco moramo biti tudi transparentni glede tega, kaj naša aplikacija z generativno umetno inteligenco zmore in česa ne.

Imamo celotno lekcijo, posvečeno [Oblikovanju UX za aplikacije z umetno inteligenco](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Ocenjevanje modela**. Delo z LLM-ji je lahko zahtevno, ker nimamo vedno nadzora nad podatki, na katerih je bil model usposobljen. Kljub temu bi morali vedno oceniti delovanje in izhode modela. Še vedno je pomembno meriti natančnost modela, podobnost, utemeljenost in relevantnost izhoda. To pomaga zagotoviti transparentnost in zaupanje deležnikom in uporabnikom.

### Upravljanje odgovorne rešitve z generativno umetno inteligenco

Zadnja faza je vzpostavitev operativne prakse okoli vaših aplikacij z umetno inteligenco. To vključuje sodelovanje z drugimi deli našega startupa, kot sta pravni oddelek in varnost, da zagotovimo skladnost z vsemi regulativnimi politikami. Pred lansiranjem želimo tudi pripraviti načrte za dostavo, obravnavo incidentov in povratne ukrepe, da preprečimo kakršno koli škodo našim uporabnikom.

## Orodja

Čeprav se delo pri razvoju rešitev z odgovorno umetno inteligenco morda zdi obsežno, je to delo vredno truda. Z rastjo področja generativne umetne inteligence se bodo razvijala tudi orodja, ki bodo razvijalcem pomagala učinkovito vključiti odgovornost v njihove delovne procese. Na primer, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) lahko pomaga zaznati škodljivo vsebino in slike prek API zahteve.

## Preverjanje znanja

Na kaj morate biti pozorni, da zagotovite odgovorno uporabo umetne inteligence?

1. Da je odgovor pravilen.
1. Škodljiva uporaba, da umetna inteligenca ni uporabljena za kriminalne namene.
1. Zagotavljanje, da je umetna inteligenca brez pristranskosti in diskriminacije.

A: 2 in 3 sta pravilna. Odgovorna umetna inteligenca vam pomaga razmisliti, kako zmanjšati škodljive učinke in pristranskosti ter še več.

## 🚀 Izziv

Preberite več o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) in preverite, kaj lahko uporabite za svoje potrebe.

## Odlično delo, nadaljujte z učenjem

Po zaključku te lekcije si oglejte našo [zbirko učenja o generativni umetni inteligenci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da še naprej nadgrajujete svoje znanje o generativni umetni inteligenci!

Pojdite na lekcijo 4, kjer bomo obravnavali [Osnove inženiringa pozivov](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.