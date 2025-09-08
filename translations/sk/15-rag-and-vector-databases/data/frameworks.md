<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:36:47+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sk"
}
-->
# Frameworky neurónových sietí

Ako sme sa už naučili, na efektívne trénovanie neurónových sietí potrebujeme urobiť dve veci:

* Operovať s tenzormi, napríklad násobiť, sčítať a počítať niektoré funkcie ako sigmoid alebo softmax
* Vypočítať gradienty všetkých výrazov, aby sme mohli vykonať optimalizáciu pomocou gradientného zostupu

Kým knižnica `numpy` zvládne prvú časť, potrebujeme mechanizmus na výpočet gradientov. V našom frameworku, ktorý sme vyvinuli v predchádzajúcej časti, sme museli manuálne programovať všetky derivácie vo funkcii `backward`, ktorá vykonáva spätnú propagáciu. Ideálne by framework mal umožniť výpočet gradientov *akéhokoľvek výrazu*, ktorý definujeme.

Ďalšou dôležitou vecou je možnosť vykonávať výpočty na GPU alebo iných špecializovaných výpočtových jednotkách, ako je TPU. Tréning hlbokých neurónových sietí vyžaduje *veľa* výpočtov, a preto je veľmi dôležité vedieť tieto výpočty paralelizovať na GPU.

> ✅ Termín 'paralelizovať' znamená rozložiť výpočty na viaceré zariadenia.

V súčasnosti sú dva najpopulárnejšie neurónové frameworky: TensorFlow a PyTorch. Obe poskytujú nízkoúrovňové API na prácu s tenzormi na CPU aj GPU. Nad týmto nízkoúrovňovým API existuje aj vysokoúrovňové API, nazývané Keras a PyTorch Lightning.

Nízkoúrovňové API | TensorFlow | PyTorch
------------------|------------|---------
Vysokoúrovňové API| Keras      | PyTorch

**Nízkoúrovňové API** v oboch frameworkoch umožňuje vytvárať tzv. **výpočtové grafy**. Tento graf definuje, ako vypočítať výstup (zvyčajne funkciu straty) pre dané vstupné parametre a môže byť odoslaný na výpočet na GPU, ak je k dispozícii. Existujú funkcie na diferenciáciu tohto výpočtového grafu a výpočet gradientov, ktoré sa potom používajú na optimalizáciu parametrov modelu.

**Vysokoúrovňové API** v podstate považuje neurónové siete za **sekvenciu vrstiev** a výrazne uľahčuje konštrukciu väčšiny neurónových sietí. Tréning modelu zvyčajne vyžaduje prípravu dát a následné zavolanie funkcie `fit`, ktorá vykoná tréning.

Vysokoúrovňové API umožňuje veľmi rýchlo zostaviť typické neurónové siete bez starostí o množstvo detailov. Na druhej strane nízkoúrovňové API ponúka oveľa väčšiu kontrolu nad tréningovým procesom, a preto sa často používa vo výskume, keď pracujete s novými architektúrami neurónových sietí.

Je tiež dôležité pochopiť, že môžete používať obe API spoločne, napríklad môžete vyvinúť vlastnú architektúru vrstvy pomocou nízkoúrovňového API a potom ju použiť v rámci väčšej siete zostavenej a trénovanej cez vysokoúrovňové API. Alebo môžete definovať sieť pomocou vysokoúrovňového API ako sekvenciu vrstiev a potom použiť vlastnú nízkoúrovňovú tréningovú slučku na optimalizáciu. Obe API používajú rovnaké základné koncepty a sú navrhnuté tak, aby dobre spolupracovali.

## Učenie

V tomto kurze ponúkame väčšinu obsahu pre PyTorch aj TensorFlow. Môžete si vybrať preferovaný framework a prejsť si len príslušné notebooky. Ak si nie ste istí, ktorý framework zvoliť, prečítajte si diskusie na internete o **PyTorch vs. TensorFlow**. Môžete si tiež pozrieť oba frameworky, aby ste získali lepšie pochopenie.

Kde je to možné, použijeme vysokoúrovňové API pre jednoduchosť. Veríme však, že je dôležité pochopiť, ako neurónové siete fungujú od základov, preto na začiatku pracujeme s nízkoúrovňovým API a tenzormi. Ak však chcete začať rýchlo a nechcete tráviť veľa času štúdiom detailov, môžete tieto časti preskočiť a ísť priamo do notebookov s vysokoúrovňovým API.

## ✍️ Cvičenia: Frameworky

Pokračujte v učení v nasledujúcich notebookoch:

Nízkoúrovňové API | TensorFlow+Keras Notebook | PyTorch
------------------|-----------------------------|---------
Vysokoúrovňové API| Keras                       | *PyTorch Lightning*

Po zvládnutí frameworkov si zrekapitulujme pojem overfitting.

# Overfitting

Overfitting je mimoriadne dôležitý pojem v strojovom učení a je veľmi dôležité ho správne pochopiť!

Zvážte nasledujúci problém aproximácie 5 bodov (na grafoch nižšie označených `x`):

!linear | overfit
-------------------------|--------------------------
**Lineárny model, 2 parametre** | **Nelineárny model, 7 parametrov**
Tréningová chyba = 5.3 | Tréningová chyba = 0
Validácia chyba = 5.1 | Validácia chyba = 20

* Vľavo vidíme dobrú priamu aproximáciu. Pretože počet parametrov je primeraný, model správne zachytáva rozloženie bodov.
* Vpravo je model príliš silný. Keďže máme len 5 bodov a model má 7 parametrov, môže sa prispôsobiť tak, že prejde všetkými bodmi, čím je tréningová chyba nulová. To však bráni modelu pochopiť správny vzor za dátami, a preto je validačná chyba veľmi vysoká.

Je veľmi dôležité nájsť správnu rovnováhu medzi komplexnosťou modelu (počtom parametrov) a počtom trénovacích vzoriek.

## Prečo dochádza k overfittingu

  * Nedostatok trénovacích dát
  * Príliš silný model
  * Príliš veľa šumu vo vstupných dátach

## Ako odhaliť overfitting

Ako vidíte z grafu vyššie, overfitting sa dá odhaliť podľa veľmi nízkej tréningovej chyby a vysokej validačnej chyby. Počas tréningu zvyčajne vidíme, že tréningová aj validačná chyba začnú klesať, no v určitom bode sa validačná chyba môže prestať znižovať a začne rásť. To je znak overfittingu a indikácia, že by sme mali tréning pravdepodobne zastaviť (alebo aspoň uložiť momentálny stav modelu).

overfitting

## Ako predísť overfittingu

Ak vidíte, že dochádza k overfittingu, môžete urobiť niektoré z nasledujúcich krokov:

 * Zvýšiť množstvo trénovacích dát
 * Znížiť zložitosť modelu
 * Použiť nejakú regularizačnú techniku, napríklad Dropout, ktorú si neskôr rozoberieme.

## Overfitting a kompromis medzi Bias a Varianciou

Overfitting je vlastne špecifický prípad všeobecnejšieho problému v štatistike nazývaného kompromis Bias-Variance. Ak zvážime možné zdroje chýb v našom modeli, môžeme rozlíšiť dva typy chýb:

* **Bias chyby** sú spôsobené tým, že náš algoritmus nedokáže správne zachytiť vzťah v trénovacích dátach. Môže to byť spôsobené tým, že model nie je dostatočne silný (**underfitting**).
* **Variance chyby** sú spôsobené tým, že model aproximuje šum vo vstupných dátach namiesto zmysluplného vzťahu (**overfitting**).

Počas tréningu sa bias chyba znižuje (model sa učí aproximovať dáta) a variance chyba rastie. Je dôležité tréning zastaviť – buď manuálne (keď zistíme overfitting) alebo automaticky (zavedením regularizácie) – aby sme predišli overfittingu.

## Zhrnutie

V tejto lekcii ste sa dozvedeli o rozdieloch medzi rôznymi API pre dva najpopulárnejšie AI frameworky, TensorFlow a PyTorch. Okrem toho ste sa naučili o veľmi dôležitej téme, overfittingu.

## 🚀 Výzva

V sprievodných notebookoch nájdete na konci „úlohy“; prejdite si notebooky a splňte ich.

## Prehľad a samostatné štúdium

Urobte si prieskum na nasledujúce témy:

- TensorFlow
- PyTorch
- Overfitting

Položte si nasledujúce otázky:

- Aký je rozdiel medzi TensorFlow a PyTorch?
- Aký je rozdiel medzi overfittingom a underfittingom?

## Zadanie

V tomto laboratóriu máte vyriešiť dva klasifikačné problémy pomocou jednovrstvových a viacvrstvových plne prepojených sietí s použitím PyTorch alebo TensorFlow.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.