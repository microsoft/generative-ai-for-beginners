<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:30:10+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sk"
}
-->
# Úvod do neurónových sietí. Viacvrstvový perceptron

V predchádzajúcej sekcii ste sa naučili o najjednoduchšom modeli neurónových sietí - jednovrstvovom perceptrone, lineárnom modeli dvojtriednej klasifikácie.

V tejto sekcii rozšírime tento model do flexibilnejšieho rámca, ktorý nám umožní:

* vykonávať **viactriednu klasifikáciu** okrem dvojtriednej
* riešiť **regresné problémy** okrem klasifikácie
* oddeľovať triedy, ktoré nie sú lineárne oddeliteľné

Tiež si vyvineme vlastný modulárny rámec v Pythone, ktorý nám umožní konštruovať rôzne architektúry neurónových sietí.

## Formalizácia strojového učenia

Začnime formalizáciou problému strojového učenia. Predpokladajme, že máme tréningovú dátovú množinu **X** s označeniami **Y**, a potrebujeme vytvoriť model *f*, ktorý bude robiť čo najpresnejšie predpovede. Kvalita predpovedí je meraná **funkciou straty** ℒ. Často používané funkcie straty sú:

* Pre regresný problém, keď potrebujeme predpovedať číslo, môžeme použiť **absolútnu chybu** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, alebo **kvadratickú chybu** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pre klasifikáciu používame **0-1 stratu** (ktorá je v podstate rovnaká ako **presnosť** modelu), alebo **logistickú stratu**.

Pre jednovrstvový perceptron bola funkcia *f* definovaná ako lineárna funkcia *f(x)=wx+b* (tu je *w* matica váh, *x* je vektor vstupných vlastností a *b* je vektor predsudkov). Pre rôzne architektúry neurónových sietí môže táto funkcia mať zložitejší tvar.

> V prípade klasifikácie je často žiaduce získať pravdepodobnosti príslušných tried ako výstup siete. Na konverziu ľubovoľných čísel na pravdepodobnosti (napr. na normalizáciu výstupu) často používame funkciu **softmax** σ, a funkcia *f* sa stáva *f(x)=σ(wx+b)*

V definícii *f* vyššie sú *w* a *b* nazývané **parametre** θ=⟨*w,b*⟩. Vzhľadom na dátovú množinu ⟨**X**,**Y**⟩, môžeme vypočítať celkovú chybu na celej dátovej množine ako funkciu parametrov θ.

> ✅ **Cieľom tréningu neurónových sietí je minimalizovať chybu menením parametrov θ**

## Optimalizácia pomocou gradientného zostupu

Existuje dobre známa metóda optimalizácie funkcií nazývaná **gradientný zostup**. Myšlienka je, že môžeme vypočítať deriváciu (v multi-dimenzionálnom prípade nazývanú **gradient**) funkcie straty vzhľadom na parametre, a meniť parametre tak, aby sa chyba znižovala. Toto môže byť formalizované nasledovne:

* Inicializovať parametre pomocou náhodných hodnôt w<sup>(0)</sup>, b<sup>(0)</sup>
* Opakovať nasledujúci krok mnohokrát:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Počas tréningu sa predpokladá, že optimalizačné kroky sú vypočítané vzhľadom na celú dátovú množinu (pamätajte, že strata je vypočítaná ako suma cez všetky tréningové vzorky). Avšak, v reálnom živote berieme malé časti dátovej množiny nazývané **minibatch**, a vypočítavame gradienty na základe podmnožiny dát. Pretože podmnožina je každým razom náhodne vybraná, takáto metóda sa nazýva **stochastický gradientný zostup** (SGD).

## Viacvrstvové perceptrony a spätné šírenie

Jednovrstvová sieť, ako sme videli vyššie, je schopná klasifikovať lineárne oddeliteľné triedy. Aby sme vytvorili bohatší model, môžeme skombinovať niekoľko vrstiev siete. Matematicky by to znamenalo, že funkcia *f* by mala zložitejší tvar a bude vypočítaná v niekoľkých krokoch:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tu je α **nelineárna aktivačná funkcia**, σ je softmax funkcia, a parametre θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritmus gradientného zostupu by zostal rovnaký, ale bolo by ťažšie vypočítať gradienty. Vzhľadom na pravidlo reťazovej diferenciácie môžeme vypočítať derivácie ako:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravidlo reťazovej diferenciácie sa používa na výpočet derivácií funkcie straty vzhľadom na parametre.

Všimnite si, že ľavá časť všetkých týchto výrazov je rovnaká, a tak môžeme efektívne vypočítať derivácie začínajúce od funkcie straty a idúce "späť" cez výpočtový graf. Preto sa metóda tréningu viacvrstvového perceptronu nazýva **spätné šírenie**, alebo 'backprop'.

> TODO: citácia obrázka

> ✅ V našom príklade v notebooku pokryjeme spätné šírenie oveľa podrobnejšie.

## Záver

V tejto lekcii sme vytvorili vlastnú knižnicu neurónových sietí a použili sme ju na jednoduchú dvojrozmernú klasifikačnú úlohu.

## 🚀 Výzva

V priloženom notebooku implementujete vlastný rámec na vytváranie a tréning viacvrstvových perceptronov. Budete môcť vidieť podrobne, ako fungujú moderné neurónové siete.

Prejdite do notebooku OwnFramework a prejdite si ho.

## Prehľad a samostatné štúdium

Spätné šírenie je bežný algoritmus používaný v AI a ML, stojí za to ho študovať podrobnejšie.

## Úloha

V tomto laboratóriu sa od vás vyžaduje použiť rámec, ktorý ste skonštruovali v tejto lekcii na riešenie klasifikácie ručne písaných číslic MNIST.

* Pokyny
* Notebook

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladov [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.