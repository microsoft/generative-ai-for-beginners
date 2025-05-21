<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:26:22+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sk"
}
-->
# Úvod do Neurónových Sietí. Viacvrstvový Perceptron

V predchádzajúcej časti ste sa naučili o najjednoduchšom modeli neurónovej siete - jednovrstvovom perceptrone, lineárnom modeli dvojtriednej klasifikácie.

V tejto časti rozšírime tento model na flexibilnejší rámec, ktorý nám umožní:

* vykonávať **viactriednu klasifikáciu** okrem dvojtriednej
* riešiť **regresné problémy** okrem klasifikácie
* oddeliť triedy, ktoré nie sú lineárne oddeliteľné

Vyvineme tiež vlastný modulárny rámec v Pythone, ktorý nám umožní konštruovať rôzne architektúry neurónových sietí.

## Formalizácia Strojového Učenia

Začnime formalizáciou problému strojového učenia. Predpokladajme, že máme tréningovú dátovú sadu **X** s označeniami **Y**, a potrebujeme vytvoriť model *f*, ktorý bude robiť najpresnejšie predpovede. Kvalita predpovedí sa meria pomocou **funkcie straty** ℒ. Nasledujúce funkcie straty sa často používajú:

* Pre regresný problém, keď potrebujeme predpovedať číslo, môžeme použiť **absolútnu chybu** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, alebo **kvadratickú chybu** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pre klasifikáciu používame **0-1 stratu** (čo je v podstate to isté ako **presnosť** modelu), alebo **logistickú stratu**.

Pre jednovrstvový perceptron bola funkcia *f* definovaná ako lineárna funkcia *f(x)=wx+b* (tu *w* je matica váh, *x* je vektor vstupných vlastností, a *b* je vektor predpojatosti). Pre rôzne architektúry neurónových sietí môže táto funkcia nadobudnúť zložitejšiu formu.

> V prípade klasifikácie je často žiaduce získať pravdepodobnosti zodpovedajúcich tried ako výstup siete. Na prevod ľubovoľných čísel na pravdepodobnosti (napr. na normalizáciu výstupu) často používame funkciu **softmax** σ, a funkcia *f* sa stáva *f(x)=σ(wx+b)*

V definícii *f* vyššie, *w* a *b* sa nazývajú **parametre** θ=⟨*w,b*⟩. S danou dátovou sadou ⟨**X**,**Y**⟩ môžeme vypočítať celkovú chybu na celej dátovej sade ako funkciu parametrov θ.

> ✅ **Cieľom tréningu neurónovej siete je minimalizovať chybu zmenou parametrov θ**

## Optimalizácia Pomocou Gradientného Zostupu

Existuje dobre známa metóda optimalizácie funkcií nazývaná **gradientný zostup**. Idea je, že môžeme vypočítať deriváciu (v multi-dimenzionálnom prípade nazývanú **gradient**) funkcie straty vzhľadom na parametre, a meniť parametre tak, aby sa chyba zmenšovala. To môžeme formalizovať nasledovne:

* Inicializujte parametre nejakými náhodnými hodnotami w<sup>(0)</sup>, b<sup>(0)</sup>
* Opakujte nasledujúci krok mnohokrát:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Počas tréningu by sa optimalizačné kroky mali vypočítavať s ohľadom na celú dátovú sadu (pamätajte, že strata sa počíta ako súčet cez všetky tréningové vzorky). Avšak v reálnom živote berieme malé časti dátovej sady nazývané **minibatch**, a počítame gradienty na základe podmnožiny dát. Pretože podmnožina je vyberaná náhodne zakaždým, takáto metóda sa nazýva **stochastický gradientný zostup** (SGD).

## Viacvrstvové Perceptrony a Spätná Propagácia

Jednovrstvová sieť, ako sme videli vyššie, je schopná klasifikovať lineárne oddeliteľné triedy. Aby sme vytvorili bohatší model, môžeme kombinovať niekoľko vrstiev siete. Matematicky by to znamenalo, že funkcia *f* by mala zložitejšiu formu a bude sa počítať v niekoľkých krokoch:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tu, α je **nelineárna aktivačná funkcia**, σ je softmax funkcia, a parametre θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritmus gradientného zostupu by zostal rovnaký, ale bolo by ťažšie počítať gradienty. Vzhľadom na pravidlo reťazovej diferenciácie môžeme vypočítať derivácie ako:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravidlo reťazovej diferenciácie sa používa na výpočet derivácií funkcie straty vzhľadom na parametre.

Všimnite si, že ľavá časť všetkých týchto výrazov je rovnaká, a preto môžeme efektívne počítať derivácie počnúc funkciou straty a ísť "späť" cez výpočtový graf. Takže metóda tréningu viacvrstvového perceptronu sa nazýva **spätná propagácia**, alebo 'backprop'.

> TODO: citácia obrázku

> ✅ Spätnú propagáciu pokryjeme oveľa podrobnejšie v našom príklade v notebooku.  

## Záver

V tejto lekcii sme vytvorili vlastnú knižnicu neurónových sietí a použili sme ju na jednoduchú dvojrozmernú klasifikačnú úlohu.

## 🚀 Výzva

V sprievodnom notebooku implementujete vlastný rámec na vytváranie a tréning viacvrstvových perceptronov. Budete môcť vidieť podrobne, ako moderné neurónové siete fungujú.

Pokračujte do notebooku OwnFramework a prejdite si ho.

## Prehľad a Samoštúdium

Spätná propagácia je bežný algoritmus používaný v AI a ML, stojí za to ho študovať podrobnejšie.

## Zadanie

V tomto laboratóriu sa od vás požaduje použiť rámec, ktorý ste vytvorili v tejto lekcii, na riešenie klasifikácie ručne písaných číslic MNIST.

* Pokyny
* Notebook

**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.