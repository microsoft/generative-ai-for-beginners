<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:10:08+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sk"
}
-->
# Frameworky pre neurónové siete

Ako sme sa už naučili, aby sme mohli efektívne trénovať neurónové siete, musíme urobiť dve veci:

* Operovať na tenzoroch, napr. násobiť, sčítať a počítať niektoré funkcie ako sigmoid alebo softmax
* Počítať gradienty všetkých výrazov, aby sme mohli vykonávať optimalizáciu pomocou gradientného zostupu

Zatiaľ čo knižnica `numpy` dokáže urobiť prvú časť, potrebujeme nejaký mechanizmus na výpočet gradientov. V našom frameworku, ktorý sme vyvinuli v predchádzajúcej sekcii, sme museli manuálne programovať všetky derivatívne funkcie v rámci metódy `backward`, ktorá vykonáva spätnú propagáciu. Ideálne by nám framework mal poskytnúť možnosť vypočítať gradienty *akéhokoľvek výrazu*, ktorý môžeme definovať.

Ďalšou dôležitou vecou je schopnosť vykonávať výpočty na GPU alebo iných špecializovaných výpočtových jednotkách, ako sú TPU. Tréning hlbokých neurónových sietí vyžaduje *veľa* výpočtov a schopnosť paralelizovať tieto výpočty na GPU je veľmi dôležitá.

> ✅ Termín 'paralelizovať' znamená rozložiť výpočty na viacero zariadení.

Momentálne sú najpopulárnejšie neurónové frameworky: TensorFlow a PyTorch. Oba poskytujú nízkoúrovňové API na operácie s tenzormi na CPU aj GPU. Na vrchole nízkoúrovňového API existuje aj vysokoúrovňové API, nazývané Keras a PyTorch Lightning.

Nízkoúrovňové API | TensorFlow | PyTorch
------------------|---------------------|------------------
Vysokoúrovňové API | Keras | PyTorch Lightning

**Nízkoúrovňové API** v oboch frameworkoch vám umožňujú vytvárať tzv. **výpočtové grafy**. Tento graf definuje, ako vypočítať výstup (zvyčajne funkciu straty) s danými vstupnými parametrami a môže byť posunutý na výpočet na GPU, ak je k dispozícii. Existujú funkcie na diferenciáciu tohto výpočtového grafu a výpočet gradientov, ktoré potom môžu byť použité na optimalizáciu parametrov modelu.

**Vysokoúrovňové API** v podstate považujú neurónové siete za **sekvenciu vrstiev** a uľahčujú konštrukciu väčšiny neurónových sietí. Tréning modelu zvyčajne vyžaduje prípravu dát a následné zavolanie funkcie `fit` na vykonanie úlohy.

Vysokoúrovňové API vám umožňuje veľmi rýchlo konštruovať typické neurónové siete bez starostí o množstvo detailov. Zároveň nízkoúrovňové API ponúkajú oveľa viac kontroly nad procesom tréningu, a preto sa často používajú v výskume, keď sa zaoberáte novými architektúrami neurónových sietí.

Je tiež dôležité pochopiť, že môžete používať obe API spolu, napr. môžete vyvinúť vlastnú architektúru vrstvy siete pomocou nízkoúrovňového API a potom ju použiť vo väčšej sieti konštruovanej a trénovanej pomocou vysokoúrovňového API. Alebo môžete definovať sieť pomocou vysokoúrovňového API ako sekvenciu vrstiev a potom použiť vlastný nízkoúrovňový tréningový cyklus na vykonanie optimalizácie. Obe API používajú rovnaké základné koncepty a sú navrhnuté tak, aby spolu dobre fungovali.

## Učenie

V tomto kurze ponúkame väčšinu obsahu pre PyTorch aj TensorFlow. Môžete si vybrať preferovaný framework a prejsť len zodpovedajúce poznámky. Ak si nie ste istí, ktorý framework si vybrať, prečítajte si niektoré diskusie na internete ohľadom **PyTorch vs. TensorFlow**. Môžete sa tiež pozrieť na oba frameworky, aby ste získali lepšie pochopenie.

Kde je to možné, použijeme vysokoúrovňové API pre jednoduchosť. Veríme však, že je dôležité pochopiť, ako neurónové siete fungujú od základov, takže na začiatku začíname pracovať s nízkoúrovňovým API a tenzormi. Ak však chcete začať rýchlo a nechcete tráviť veľa času učením sa týchto detailov, môžete ich preskočiť a prejsť priamo do poznámok vysokoúrovňového API.

## ✍️ Cvičenia: Frameworky

Pokračujte v učení v nasledujúcich poznámkach:

Nízkoúrovňové API | TensorFlow+Keras Notebook | PyTorch
------------------|---------------------|------------------
Vysokoúrovňové API | Keras | *PyTorch Lightning*

Po zvládnutí frameworkov si zopakujeme pojem overfittingu.

# Overfitting

Overfitting je mimoriadne dôležitý koncept v strojovom učení a je veľmi dôležité ho správne pochopiť!

Zvážte nasledujúci problém aproximácie 5 bodov (reprezentovaných `x` na grafoch nižšie):

!linear | overfit
-------------------------|--------------------------
**Lineárny model, 2 parametre** | **Nelineárny model, 7 parametrov**
Tréningová chyba = 5.3 | Tréningová chyba = 0
Validačná chyba = 5.1 | Validačná chyba = 20

* Naľavo vidíme dobrú aproximáciu priamkou. Pretože počet parametrov je adekvátny, model správne pochopí rozloženie bodov.
* Napravo je model príliš silný. Pretože máme len 5 bodov a model má 7 parametrov, môže sa nastaviť tak, aby prešiel všetkými bodmi, čím sa tréningová chyba stane 0. To však bráni modelu v pochopení správneho vzoru za dátami, takže validačná chyba je veľmi vysoká.

Je veľmi dôležité nájsť správnu rovnováhu medzi bohatstvom modelu (počet parametrov) a počtom tréningových vzoriek.

## Prečo dochádza k overfittingu

  * Nedostatok tréningových dát
  * Príliš silný model
  * Príliš veľa šumu vo vstupných dátach

## Ako detekovať overfitting

Ako vidíte z grafu vyššie, overfitting môže byť detekovaný veľmi nízkou tréningovou chybou a vysokou validačnou chybou. Normálne počas tréningu vidíme, ako tréningová aj validačná chyba začínajú klesať, a potom v určitom bode validačná chyba môže prestať klesať a začať stúpať. Toto bude znamenie overfittingu a indikátor, že by sme pravdepodobne mali prestať trénovať v tomto bode (alebo aspoň urobiť snímku modelu).

## Ako predísť overfittingu

Ak vidíte, že dochádza k overfittingu, môžete urobiť jednu z nasledujúcich vecí:

 * Zvýšiť množstvo tréningových dát
 * Znížiť zložitosť modelu
 * Použiť nejakú techniku regularizácie, ako je Dropout, ktorú budeme neskôr zvažovať.

## Overfitting a Bias-Variance Tradeoff

Overfitting je vlastne prípad generického problému v štatistike nazývaného Bias-Variance Tradeoff. Ak zvážime možné zdroje chyby v našom modeli, môžeme vidieť dva typy chýb:

* **Chyby zaujatosti** sú spôsobené tým, že náš algoritmus nedokáže správne zachytiť vzťah medzi tréningovými dátami. Môže to byť výsledok toho, že náš model nie je dostatočne silný (**underfitting**).
* **Chyby variancie**, ktoré sú spôsobené tým, že model aproximuje šum vo vstupných dátach namiesto zmysluplného vzťahu (**overfitting**).

Počas tréningu chyba zaujatosti klesá (keď sa náš model učí aproximovať dáta) a chyba variancie stúpa. Je dôležité zastaviť tréning - buď manuálne (keď detekujeme overfitting) alebo automaticky (zavedením regularizácie) - aby sme predišli overfittingu.

## Záver

V tejto lekcii ste sa naučili o rozdieloch medzi rôznymi API pre dva najpopulárnejšie AI frameworky, TensorFlow a PyTorch. Okrem toho ste sa naučili o veľmi dôležitej téme, overfittingu.

## 🚀 Výzva

V sprievodných poznámkach nájdete 'úlohy' na konci; prejdite cez poznámky a splňte úlohy.

## Preskúmanie & Samoštúdium

Vykonajte výskum na nasledujúce témy:

- TensorFlow
- PyTorch
- Overfitting

Položte si nasledujúce otázky:

- Aký je rozdiel medzi TensorFlow a PyTorch?
- Aký je rozdiel medzi overfittingom a underfittingom?

## Zadanie

V tomto laboratóriu ste požiadaní vyriešiť dva problémy klasifikácie pomocou jedno- a viacvrstvových plne prepojených sietí pomocou PyTorch alebo TensorFlow.

**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.