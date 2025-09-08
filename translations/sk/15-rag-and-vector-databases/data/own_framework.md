<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:50:50+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sk"
}
-->
# Úvod do neurónových sietí. Viacvrstvový perceptrón

V predchádzajúcej časti ste sa naučili o najjednoduchšom modeli neurónovej siete – jednovrstvovom perceptróne, lineárnom modeli pre binárnu klasifikáciu.

V tejto časti tento model rozšírime do flexibilnejšieho rámca, ktorý nám umožní:

* vykonávať **viactriednu klasifikáciu** okrem binárnej
* riešiť **regresné úlohy** okrem klasifikácie
* separovať triedy, ktoré nie sú lineárne oddeliteľné

Tiež si vyvineme vlastný modulárny rámec v Pythone, ktorý nám umožní zostavovať rôzne architektúry neurónových sietí.

## Formalizácia strojového učenia

Začnime formalizáciou problému strojového učenia. Predpokladajme, že máme trénovaciu množinu dát **X** s označeniami **Y** a potrebujeme vytvoriť model *f*, ktorý bude robiť čo najpresnejšie predikcie. Kvalita predikcií sa meria pomocou **funkcie straty** ℒ. Často používané funkcie straty sú:

* Pre regresné úlohy, kde potrebujeme predpovedať číslo, môžeme použiť **absolútnu chybu** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| alebo **štvorcovú chybu** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pre klasifikáciu používame **0-1 stratu** (čo je v podstate to isté ako **presnosť** modelu) alebo **logistickú stratu**.

Pre jednovrstvový perceptrón bola funkcia *f* definovaná ako lineárna funkcia *f(x)=wx+b* (kde *w* je matica váh, *x* je vektor vstupných vlastností a *b* je vektor biasu). Pre rôzne architektúry neurónových sietí môže mať táto funkcia zložitejšiu podobu.

> Pri klasifikácii je často žiaduce získať pravdepodobnosti príslušných tried ako výstup siete. Na prevod ľubovoľných čísel na pravdepodobnosti (napr. na normalizáciu výstupu) často používame **softmax** funkciu σ, a funkcia *f* sa stáva *f(x)=σ(wx+b)*

V definícii *f* vyššie sa *w* a *b* nazývajú **parametre** θ=⟨*w,b*⟩. Pre danú množinu dát ⟨**X**,**Y**⟩ môžeme vypočítať celkovú chybu na celej množine ako funkciu parametrov θ.

> ✅ **Cieľom trénovania neurónovej siete je minimalizovať chybu zmenou parametrov θ**

## Optimalizácia pomocou gradientného zostupu

Existuje známa metóda optimalizácie funkcií nazývaná **gradientný zostup**. Myšlienka je, že môžeme vypočítať deriváciu (v prípade viacrozmernom nazývanú **gradient**) funkcie straty vzhľadom na parametre a meniť parametre tak, aby sa chyba znižovala. Dá sa to formalizovať takto:

* Inicializujeme parametre náhodnými hodnotami w<sup>(0)</sup>, b<sup>(0)</sup>
* Opakujeme nasledujúci krok mnohokrát:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup> - η ∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup> - η ∂ℒ/∂b

Počas trénovania by sa optimalizačné kroky mali počítať so zohľadnením celej množiny dát (pamätajte, že strata sa počíta ako súčet cez všetky trénovacie vzorky). V praxi však berieme malé časti dát nazývané **minibatches** a počítame gradienty na základe podmnožiny dát. Keďže podmnožina sa vyberá náhodne pri každom kroku, táto metóda sa nazýva **stochastický gradientný zostup** (SGD).

## Viacvrstvové perceptróny a spätná propagácia

Jednovrstvová sieť, ako sme videli vyššie, dokáže klasifikovať lineárne oddeliteľné triedy. Na vytvorenie bohatšieho modelu môžeme spojiť niekoľko vrstiev siete. Matematicky to znamená, že funkcia *f* bude mať zložitejšiu podobu a bude sa počítať v niekoľkých krokoch:
* z<sub>1</sub> = w<sub>1</sub>x + b<sub>1</sub>
* z<sub>2</sub> = w<sub>2</sub>α(z<sub>1</sub>) + b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Kde α je **nelineárna aktivačná funkcia**, σ je softmax funkcia a parametre θ = ⟨*w<sub>1</sub>, b<sub>1</sub>, w<sub>2</sub>, b<sub>2</sub>*⟩.

Algoritmus gradientného zostupu zostáva rovnaký, ale výpočet gradientov je zložitejší. Vďaka pravidlu reťazovej derivácie môžeme derivácie vypočítať takto:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravidlo reťazovej derivácie sa používa na výpočet derivácií funkcie straty vzhľadom na parametre.

Všimnite si, že ľavá časť všetkých týchto výrazov je rovnaká, a preto môžeme efektívne počítať derivácie začínajúc od funkcie straty a postupovať „dozadu“ cez výpočtový graf. Táto metóda trénovania viacvrstvového perceptrónu sa nazýva **spätná propagácia** alebo „backprop“.

> TODO: citácia obrázka

> ✅ Spätnú propagáciu podrobnejšie rozoberieme v našom príklade v notebooku.

## Záver

V tejto lekcii sme si vytvorili vlastnú knižnicu neurónových sietí a použili ju na jednoduchú dvojrozmernú klasifikačnú úlohu.

## 🚀 Výzva

V sprievodnom notebooku si implementujete vlastný rámec na tvorbu a trénovanie viacvrstvových perceptrónov. Podrobne tak uvidíte, ako moderné neurónové siete fungujú.

Prejdite do notebooku OwnFramework a prejdite si ho.

## Prehľad a samostatné štúdium

Spätná propagácia je bežný algoritmus používaný v AI a ML, stojí za to sa mu venovať podrobnejšie.

## Zadanie

V tomto laboratóriu máte použiť rámec, ktorý ste si vytvorili v tejto lekcii, na riešenie klasifikácie ručne písaných číslic MNIST.

* Inštrukcie
* Notebook

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.