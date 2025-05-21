<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:06:49+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sk"
}
-->
# Rámce pre neurónové siete

Ako sme sa už naučili, aby sme mohli efektívne trénovať neurónové siete, musíme urobiť dve veci:

* Operovať na tenzoroch, napr. násobiť, sčítať a počítať niektoré funkcie ako sigmoid alebo softmax
* Počítať gradienty všetkých výrazov, aby sme mohli vykonať optimalizáciu pomocou gradientného zostupu

Zatiaľ čo knižnica `numpy` dokáže prvú časť, potrebujeme nejaký mechanizmus na výpočet gradientov. V našom rámci, ktorý sme vyvinuli v predchádzajúcej sekcii, sme museli manuálne programovať všetky derivačné funkcie vo vnútri metódy `backward`, ktorá vykonáva spätnú propagáciu. Ideálne by mal rámec poskytnúť možnosť počítať gradienty *akéhokoľvek výrazu*, ktorý môžeme definovať.

Ďalšou dôležitou vecou je schopnosť vykonávať výpočty na GPU alebo iných špecializovaných výpočtových jednotkách, ako je TPU. Tréning hlbokých neurónových sietí vyžaduje *veľa* výpočtov a schopnosť paralelizovať tieto výpočty na GPU je veľmi dôležitá.

> ✅ Termín 'paralelizovať' znamená rozložiť výpočty na viacero zariadení.

V súčasnosti sú dva najpopulárnejšie rámce pre neurónové siete: TensorFlow a PyTorch. Oba poskytujú nízkoúrovňové API na operovanie s tenzormi na CPU aj GPU. Na vrchole nízkoúrovňového API je aj vysokoúrovňové API, nazývané Keras a PyTorch Lightning.

Nízkourovňové API | TensorFlow| PyTorch
------------------|-------------------------------------|--------------------------------
Vysokoúrovňové API| Keras| Pytorch

**Nízkoúrovňové API** v oboch rámcoch umožňujú vytvárať tzv. **výpočtové grafy**. Tento graf definuje, ako vypočítať výstup (zvyčajne funkciu straty) s danými vstupnými parametrami a môže byť poslaný na výpočet na GPU, ak je dostupný. Existujú funkcie na diferenciáciu tohto výpočtového grafu a výpočet gradientov, ktoré môžu byť následne použité na optimalizáciu parametrov modelu.

**Vysokoúrovňové API** považujú neurónové siete za **sekvenciu vrstiev** a konštrukcia väčšiny neurónových sietí je tak oveľa jednoduchšia. Tréning modelu zvyčajne vyžaduje prípravu dát a následné zavolanie funkcie `fit` na vykonanie práce.

Vysokoúrovňové API umožňujú rýchlu konštrukciu typických neurónových sietí bez obáv o množstvo detailov. Zároveň nízkoúrovňové API ponúkajú oveľa väčšiu kontrolu nad tréningovým procesom, a preto sa často používajú v výskume, keď sa zaoberáte novými architektúrami neurónových sietí.

Je tiež dôležité pochopiť, že môžete použiť obidve API spolu, napr. môžete vyvinúť vlastnú architektúru vrstvy siete pomocou nízkoúrovňového API a potom ju použiť vo väčšej sieti konštruovanej a trénovanej pomocou vysokoúrovňového API. Alebo môžete definovať sieť pomocou vysokoúrovňového API ako sekvenciu vrstiev a potom použiť vlastný nízkoúrovňový tréningový cyklus na vykonanie optimalizácie. Obe API používajú rovnaké základné koncepty a sú navrhnuté tak, aby spolu dobre fungovali.

## Učenie

V tomto kurze ponúkame väčšinu obsahu pre PyTorch a TensorFlow. Môžete si vybrať preferovaný rámec a prejsť len príslušné notebooky. Ak si nie ste istí, ktorý rámec zvoliť, prečítajte si niektoré diskusie na internete týkajúce sa **PyTorch vs. TensorFlow**. Môžete sa tiež pozrieť na oba rámce, aby ste získali lepšie pochopenie.

Kde je to možné, použijeme vysokoúrovňové API pre jednoduchosť. Veríme však, že je dôležité pochopiť, ako neurónové siete fungujú od základu, preto na začiatku začíname pracovať s nízkoúrovňovým API a tenzormi. Ak však chcete rýchlo začať a nechcete tráviť veľa času učením sa týchto detailov, môžete ich preskočiť a prejsť priamo do notebookov s vysokoúrovňovým API.

## ✍️ Cvičenia: Rámce

Pokračujte vo svojom učení v nasledujúcich notebookoch:

Nízkourovňové API | TensorFlow+Keras Notebook | PyTorch
------------------|-------------------------------------|--------------------------------
Vysokoúrovňové API| Keras | *PyTorch Lightning*

Po zvládnutí rámcov si zopakujeme pojem preučenia.

# Preučenie

Preučenie je mimoriadne dôležitý koncept v strojovom učení a je veľmi dôležité ho pochopiť správne!

Zvážte nasledujúci problém aproximácie 5 bodov (reprezentovaných `x` na grafoch nižšie):

!lineárny | preučenie
-------------------------|--------------------------
**Lineárny model, 2 parametre** | **Nelineárny model, 7 parametrov**
Chyba tréningu = 5.3 | Chyba tréningu = 0
Chyba validácie = 5.1 | Chyba validácie = 20

* Vľavo vidíme dobrú aproximáciu priamkou. Pretože počet parametrov je adekvátny, model správne pochopí rozloženie bodov.
* Vpravo je model príliš silný. Pretože máme len 5 bodov a model má 7 parametrov, môže sa prispôsobiť tak, aby prešiel cez všetky body, čím sa chyba tréningu stane 0. Avšak, to zabráni modelu pochopiť správny vzor za dátami, preto je chyba validácie veľmi vysoká.

Je veľmi dôležité nájsť správnu rovnováhu medzi bohatosťou modelu (počet parametrov) a počtom tréningových vzoriek.

## Prečo dochádza k preučeniu

  * Nedostatok tréningových dát
  * Príliš silný model
  * Príliš veľa šumu vo vstupných dátach

## Ako detekovať preučenie

Ako môžete vidieť z grafu vyššie, preučenie môže byť detekované veľmi nízkou chybou tréningu a vysokou chybou validácie. Normálne počas tréningu vidíme, ako chyby tréningu a validácie začínajú klesať, a potom v určitom bode chyba validácie môže prestať klesať a začať stúpať. To bude znamením preučenia a indikátorom, že by sme pravdepodobne mali zastaviť tréning v tomto bode (alebo aspoň urobiť snímku modelu).

## Ako predísť preučeniu

Ak vidíte, že dochádza k preučeniu, môžete urobiť jedno z nasledujúcich:

 * Zvýšiť množstvo tréningových dát
 * Znížiť komplexnosť modelu
 * Použiť nejakú techniku regularizácie, ako je Dropout, ktorú budeme neskôr rozoberať.

## Preučenie a kompromis medzi zaujatím a rozptylom

Preučenie je vlastne prípad všeobecnejšieho problému v štatistike nazývaného kompromis medzi zaujatím a rozptylom. Ak zvážime možné zdroje chyby v našom modeli, môžeme vidieť dva typy chýb:

* **Chyby zaujatia** sú spôsobené tým, že náš algoritmus nedokáže správne zachytiť vzťah medzi tréningovými dátami. Môže to byť výsledok toho, že náš model nie je dostatočne silný (**podučenie**).
* **Chyby rozptylu**, ktoré sú spôsobené tým, že model aproximuje šum vo vstupných dátach namiesto zmysluplného vzťahu (**preučenie**).

Počas tréningu sa chyba zaujatia znižuje (ako sa náš model učí aproximovať dáta) a chyba rozptylu sa zvyšuje. Je dôležité zastaviť tréning - buď manuálne (keď detekujeme preučenie) alebo automaticky (zavedením regularizácie) - aby sme predišli preučeniu.

## Záver

V tejto lekcii ste sa naučili o rozdieloch medzi rôznymi API pre dva najpopulárnejšie AI rámce, TensorFlow a PyTorch. Okrem toho ste sa naučili o veľmi dôležitej téme, preučení.

## 🚀 Výzva

V priložených notebookoch nájdete 'úlohy' na konci; prejdite si notebooky a splňte úlohy.

## Prehľad & Samoštúdium

Urobte si výskum na nasledujúce témy:

- TensorFlow
- PyTorch
- Preučenie

Položte si nasledujúce otázky:

- Aký je rozdiel medzi TensorFlow a PyTorch?
- Aký je rozdiel medzi preučením a podučením?

## Zadanie

V tomto laboratóriu sa od vás požaduje vyriešiť dva problémy klasifikácie pomocou jedno- a viacvrstvových plne prepojených sietí pomocou PyTorch alebo TensorFlow.

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.