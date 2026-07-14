[![Open Source Models](../../../translated_images/sk/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Doladenie vášho LLM

Použitie veľkých jazykových modelov na vytváranie generatívnych AI aplikácií prináša nové výzvy. Kľúčovou otázkou je zabezpečiť kvalitu odpovedí (presnosť a relevantnosť) v obsahu generovanom modelom pre danú požiadavku používateľa. V predchádzajúcich lekciách sme diskutovali techniky ako prompt engineering a retrieval-augmented generation, ktoré sa snažia riešiť problém _úpravou vstupného promptu_ pre existujúci model.

V dnešnej lekcii sa budeme venovať tretej technike, **doladeniu (fine-tuning)**, ktorá sa snaží vyriešiť túto výzvu _prestúsením samotného modelu_ s použitím ďalších dát. Pozrime sa na detaily.

## Ciele učenia

Táto lekcia predstavuje koncept doladenia pre predtrénované jazykové modely, skúma výhody a výzvy tohto prístupu a poskytuje usmernenie, kedy a ako doladenie využiť na zlepšenie výkonu vašich generatívnych AI modelov.

Na konci tejto lekcie by ste mali byť schopní odpovedať na tieto otázky:

- Čo je doladenie jazykových modelov?
- Kedy a prečo je doladenie užitočné?
- Ako môžem doladiť predtrénovaný model?
- Aké sú obmedzenia doladenia?

Pripravení? Poďme na to.

## Ilustrovaný sprievodca

Chcete mať prehľad o téme predtým, než do nej ponoríme? Pozrite si tento ilustrovaný sprievodca, ktorý popisuje vzdelávaciu cestu tejto lekcie - od učenia základných konceptov a motivácie pre doladenie až po pochopenie procesu a najlepších postupov pre vykonanie doladenia. Toto je fascinujúca téma na preskúmanie, tak nezabudnite navštíviť stránku [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pre ďalšie odkazy na podporu vášho samoštúdia!

![Ilustrovaný sprievodca doladením jazykových modelov](../../../translated_images/sk/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Čo je doladenie pre jazykové modely?

Veľké jazykové modely sú podľa definície _predtrénované_ na veľkom množstve textov zo zdrojov ako internet. Ako sme sa naučili v predchádzajúcich lekciách, potrebujeme techniky ako _prompt engineering_ a _retrieval-augmented generation_, aby sme zlepšili kvalitu odpovedí modelu na otázky používateľa ("prompty").

Populárna technika prompt-inžinierstva zahŕňa poskytnutie modelu väčšej podpory v tom, čo sa od neho očakáva v odpovedi, buď prostredníctvom _inštrukcií_ (explicitné usmernenie) alebo _poskytnutím niekoľkých príkladov_ (nepriame usmernenie). Toto sa nazýva _few-shot learning_, ale má dve obmedzenia:

- Limity tokenov modelu môžu obmedzovať počet príkladov, ktoré môžete uviesť, a tým aj efektivitu.
- Náklady na tokeny modelu môžu spraviť pridávanie príkladov k promptom drahým, čo obmedzuje flexibilitu.

Doladenie je bežná prax v systémoch strojového učenia, kde vezmeme predtrénovaný model a pretrénujeme ho s novými dátami, aby sme zlepšili jeho výkon na konkrétnej úlohe. V kontexte jazykových modelov môžeme doladiť predtrénovaný model _vybranou sadou príkladov pre konkrétnu úlohu alebo aplikačnú doménu_, aby sme vytvorili **vlastný model**, ktorý môže byť presnejší a relevantnejší pre danú úlohu alebo doménu. Vedľajšou výhodou doladenia je, že môže znížiť počet príkladov potrebných pre few-shot learning - čím sa zníži využitie tokenov a súvisiace náklady.

## Kedy a prečo by sme mali doladiť modely?

V _tomto_ kontexte sa doladenie týka **supervidovaného** doladenia, kde sa pretrénovanie robí **pridaním nových dát**, ktoré neboli súčasťou pôvodného tréningového datasetu. To sa líši od nesupervidovaného doladenia, kde sa model pretrénuje na pôvodných dátach, ale s inými hyperparametrami.

Kľúčové je si uvedomiť, že doladenie je pokročilá technika, ktorá vyžaduje určitú úroveň odbornosti, aby sa dosiahli želané výsledky. Ak je spravené nesprávne, nemusí priniesť očakávané zlepšenia a môže dokonca zhoršiť výkon modelu pre vašu cieľovú doménu.

Takže predtým, než sa naučíte "ako" doladiť jazykové modely, musíte vedieť "prečo" by ste mali ísť touto cestou a "kedy" začať proces doladenia. Začnite týmito otázkami:

- **Prípad použitia**: Aký je váš _prípad použitia_ pre doladenie? Ktorý aspekt aktuálneho predtrénovaného modelu chcete zlepšiť?
- **Alternatívy**: Vyskúšali ste _iné techniky_, aby ste dosiahli požadované výsledky? Použite ich na vytvorenie základnej línie na porovnanie.
  - Prompt engineering: Vyskúšajte techniky ako few-shot prompting s príkladmi relevantných odpovedí. Vyhodnoťte kvalitu odpovedí.
  - Retrieval Augmented Generation: Vyskúšajte doplnenie promptov o výsledky dopytov na vašich dátach. Vyhodnoťte kvalitu odpovedí.
- **Náklady**: Identifikovali ste náklady na doladenie?
  - Možnosť doladenia - je predtrénovaný model dostupný na doladenie?
  - Úsilie - pre prípravu tréningových dát, vyhodnocovanie a doladenie modelu.
  - Výpočtová kapacita - pre spustenie úloh doladenia a nasadenie doladeného modelu.
  - Dáta - prístup k dostatočne kvalitným príkladom pre efekt doladenia.
- **Výhody**: Potvrdili ste si výhody doladenia?
  - Kvalita - prekonal doladený model pôvodnú základnú líniu?
  - Náklady - znižuje to spotrebu tokenov zjednodušením promptov?
  - Rozšíriteľnosť - môžete základný model využiť pre nové domény?

Odpovedaním na tieto otázky by ste mali vedieť rozhodnúť, či je doladenie správnym prístupom pre váš prípad použitia. Ideálne je, ak prínosy prevážia náklady. Keď sa rozhodnete pokračovať, je čas zamyslieť sa nad tým, _ako_ môžete doladiť predtrénovaný model.

Chcete získať viac informácií o rozhodovacom procese? Pozrite si [Doladiť alebo nedoladiť](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Ako môžeme doladiť predtrénovaný model?

Na doladenie predtrénovaného modelu potrebujete:

- predtrénovaný model na doladenie
- dataset na použitie pre doladenie
- tréningové prostredie pre spustenie úlohy doladenia
- hostingové prostredie na nasadenie doladeného modelu

## Doladenie v praxi

> **Poznámka:** `gpt-35-turbo` / `gpt-3.5-turbo`, zmienené v niektorých tutoriáloch nižšie, bolo vyradené z obehu pre inference aj doladenie. Ak dnes začínate novú úlohu doladenia, zamerajte sa na aktuálne podporovaný model, napríklad `gpt-4o-mini` alebo `gpt-4.1-mini`. Pozrite si [zoznam modelov na doladenie](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) pre aktuálne dostupné modely na doladenie. Koncepty a kroky v týchto tutoriáloch sú stále platné.

Nasledujúce zdroje poskytujú podrobné návody, ktoré vás prevedú reálnym príkladom s vybraným modelom a starostlivo vybraným datasetom. Na prácu s týmito tutoriálmi potrebujete účet u konkrétneho poskytovateľa, spolu s prístupom k relevantnému modelu a datasetom.

| Poskytovateľ | Tutoriál                                                                                                                                                                       | Popis                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Ako doladiť chat modely](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Naučte sa doladiť `gpt-35-turbo` pre špecifickú doménu ("asistent pre recepty") prípravou tréningových dát, spustením úlohy doladenia a využitím doladeného modelu na inferenciu.                                                                                                                                                                                                                                              |
| Azure OpenAI | [Tutoriál doladenia GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Naučte sa doladiť model `gpt-35-turbo-0613` **na Azure** krok za krokom: vytvorenie & nahranie tréningových dát, spustenie úlohy doladenia, nasadenie a použitie nového modelu.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Doladenie LLM pomocou Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Tento blog vás prevedie doladením _otvoreného LLM_ (napr. `CodeLlama 7B`) pomocou knižnice [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) a [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) s otvorenými [datasetmi](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Doladenie LLM pomocou AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (alebo AutoTrain Advanced) je python knižnica vyvinutá Hugging Face, ktorá umožňuje doladenie pre rôzne úlohy vrátane finetuningu LLM. AutoTrain je riešenie bez kódu a doladenie možno vykonať vo vašom vlastnom cloude, na Hugging Face Spaces alebo lokálne. Podporuje webové GUI, CLI a tréning cez yaml konfiguračné súbory.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Doladenie LLM s Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth je open-source framework podporujúci doladenie LLM a reinforcement learning (RL). Unsloth zjednodušuje lokálne tréningy, hodnotenie a nasadenie s pripravenými [notebookmi](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Podporuje tiež text-to-speech (TTS), BERT a multimodálne modely. Pre začatie si prečítajte ich podrobný [Sprievodca doladením LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Zadanie

Vyberte si jeden z vyššie uvedených tutoriálov a prejdite si ich. _Môžeme replikovať verziu týchto tutoriálov v Jupyter Notebookoch v tomto repozitári len na referenciu. Pre najnovšie verzie používajte priamo originálne zdroje_.

## Skvelá práca! Pokračujte vo svojom učení.

Po dokončení tejto lekcie si pozrite našu [kolekciu Generatívneho AI učenia](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte v zvyšovaní svojich znalostí o generatívnej AI!

Gratulujeme!! Dokončili ste záverečnú lekciu série v2 tohto kurzu! Nezastavujte sa v učení a tvorbe. \*\*Pozrite si stránku [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pre zoznam ďalších tipov práve k tejto téme.

Naša séria lekcií v1 bola tiež aktualizovaná o viac úloh a konceptov. Tak si dajte chvíľku na osvieženie vedomostí - a prosím [zdieľajte svoje otázky a spätnú väzbu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), aby sme mohli tieto lekcie komunitne vylepšiť.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->