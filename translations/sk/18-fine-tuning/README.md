[![Open Source Models](../../../translated_images/sk/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Doladenie vášho LLM

Používanie veľkých jazykových modelov na vytváranie generatívnych AI aplikácií prináša nové výzvy. Kľúčovým problémom je zabezpečiť kvalitu odpovedí (presnosť a relevantnosť) v obsahu generovanom modelom na daný používateľský dopyt. V predchádzajúcich lekciách sme diskutovali techniky ako návrh promptov (prompt engineering) a generovanie doplnené o vyhľadávanie (retrieval-augmented generation), ktoré sa snažia vyriešiť problém _úpravou vstupného promptu_ do existujúceho modelu.

V dnešnej lekcii si predstavíme tretiu techniku, **doladenie (fine-tuning)**, ktorá sa snaží riešiť výzvu _preškolením samotného modelu_ s použitím ďalších dát. Poďme sa pozrieť na detaily.

## Učebné ciele

Táto lekcia predstavuje koncept doladenia pre predtrénované jazykové modely, skúma výhody a výzvy tohto prístupu a poskytuje usmernenie, kedy a ako použiť doladenie na zlepšenie výkonu vašich generatívnych AI modelov.

Na konci tejto lekcie by ste mali vedieť odpovedať na nasledujúce otázky:

- Čo je doladenie pre jazykové modely?
- Kedy a prečo je doladenie užitočné?
- Ako môžem doladiť predtrénovaný model?
- Aké sú obmedzenia doladenia?

Ste pripravení? Poďme začať.

## Ilustrovaný sprievodca

Chcete získať celkový obraz o tom, čo pokryjeme, ešte pred tým, ako sa do toho pustíme? Pozrite si tento ilustrovaný sprievodca, ktorý popisuje vzdelávaciu cestu pre túto lekciu – od učenia sa základných konceptov a motivácie doladenia, až po pochopenie procesu a najlepších praktík pri vykonávaní úlohy doladenia. Je to fascinujúca téma na preskúmanie, tak nezabudnite navštíviť stránku [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pre ďalšie odkazy, ktoré podporia vaše samostatné štúdium!

![Ilustrovaný sprievodca doladením jazykových modelov](../../../translated_images/sk/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Čo je doladenie pre jazykové modely?

Podľa definície sú veľké jazykové modely _predtrénované_ na veľkých množstvách textu z rôznych zdrojov vrátane internetu. Ako sme sa učili v predchádzajúcich lekciách, potrebujeme techniky ako _návrh promptov_ a _generovanie doplnené o vyhľadávanie_, aby sme zlepšili kvalitu odpovedí modelu na používateľské otázky („prompty“).

Populárna technika návrhu promptov zahŕňa poskytnutie modelu viac usmernení o tom, čo sa očakáva v odpovedi, buď poskytnutím _inštrukcií_ (explicitné usmernenie) alebo _poskytnutím niekoľkých príkladov_ (implicitné usmernenie). Toto sa nazýva _few-shot learning_, ale má dve obmedzenia:

- Limity tokenov modelu môžu obmedziť počet príkladov, ktoré môžete dať, a tým aj efektívnosť.
- Náklady na tokeny v modeli môžu spraviť pridanie príkladov do každého promptu drahšie a obmedziť flexibilitu.

Doladenie je bežná prax v systémoch strojového učenia, kde vezmeme predtrénovaný model a preškolíme ho s novými dátami, aby sme zlepšili jeho výkon pri špecifickej úlohe. V kontexte jazykových modelov môžeme doladiť predtrénovaný model _s vybraným súborom príkladov pre danú úlohu alebo oblasť použitia_, aby sme vytvorili **vlastný model**, ktorý môže byť presnejší a relevantnejší pre túto konkrétnu úlohu alebo oblasť. Vedľajším prínosom doladenia je, že môže znížiť počet potrebných príkladov pre few-shot learning – znižujúc tým spotrebu tokenov a súvisiace náklady.

## Kedy a prečo by sme mali doladiť modely?

V _tomto_ kontexte, keď hovoríme o doladení, myslíme na **riadené (supervised)** doladenie, kde sa preškolenie vykonáva **pridaním nových dát**, ktoré neboli súčasťou pôvodnej tréningovej sady. Toto sa líši od neriadeného (unsupervised) doladenia, kde sa model preškoli na pôvodných dátach, ale s inými hyperparametrami.

Kľúčové je si uvedomiť, že doladenie je pokročilá technika vyžadujúca určitú úroveň odbornosti na dosiahnutie požadovaných výsledkov. Ak sa vykoná nesprávne, nemusí priniesť očakávané zlepšenia, a môže dokonca zhoršiť výkon modelu pre váš cieľový domén.

Takže predtým, než sa naučíte „ako“ doladiť jazykové modely, musíte vedieť „prečo“ by ste mali touto cestou ísť a „kedy“ začať proces doladenia. Začnite položením si týchto otázok:

- **Použitie**: Aký je váš _prípad použitia_ doladenia? Ktorý aspekt aktuálneho predtrénovaného modelu chcete zlepšiť?
- **Alternatívy**: Skúsili ste _iné techniky_ na dosiahnutie požadovaných výsledkov? Použite ich na vytvorenie základnej línie porovnania.
  - Návrh promptov: Skúste techniky ako few-shot promptovanie s príkladmi relevantných odpovedí. Vyhodnoťte kvalitu odpovedí.
  - Generovanie doplnené o vyhľadávanie: Skúste doplniť prompty výsledkami vyhľadávania vo vašich dátach. Vyhodnoťte kvalitu odpovedí.
- **Náklady**: Identifikovali ste náklady spojené s doladením?
  - Možnosť doladenia - je predtrénovaný model dostupný na doladenie?
  - Úsilie - na prípravu tréningových dát, vyhodnocovanie a doladenie modelu.
  - Výpočtové zdroje - pre spustenie doladenia a nasadenie doladeného modelu.
  - Dáta - prístup k dostatočne kvalitným príkladom pre efekt doladenia.
- **Výhody**: Potvrdili ste výhody doladenia?
  - Kvalita - prekonal doladený model základnú líniu?
  - Náklady - znižuje použitie tokenov zjednodušením promptov?
  - Rozšíriteľnosť - môžete základný model použiť pre nové domény?

Odpovedaním na tieto otázky by ste mali byť schopní rozhodnúť, či je doladenie správnym prístupom pre váš prípad použitia. Ideálne je, ak sú výhody väčšie ako náklady. Keď sa rozhodnete pokračovať, je čas premýšľať o tom, _ako_ môžete doladiť predtrénovaný model.

Chcete získať ďalšie poznatky o rozhodovacom procese? Pozrite si [Doladiť alebo nedoladiť?](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Ako môžeme doladiť predtrénovaný model?

Na doladenie predtrénovaného modelu potrebujete:

- predtrénovaný model na doladenie
- dátovú sadu na použitie pri doladení
- tréningové prostredie na spustenie doladenia
- hostingové prostredie na nasadenie doladeného modelu

## Doladenie na Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) je miesto, kde dnes doladíte, nasadíte a spravujete vlastné modely na Azure (spája to, čo bolo Azure OpenAI Studio a Azure AI Studio). Pred spustením úlohy je užitočné porozumieť voľbám, ktoré Foundry ponúka, a najlepším praktikám, ktoré platforma odporúča. Pod kapotou Foundry používa **LoRA (nízkorozmerová adaptácia)** na efektívne doladenie modelov, čo udržuje tréning rýchlejší a dostupnejší než preškolenie všetkých váh.

### Krok 1: Vyberte tréningovú techniku

Foundry podporuje tri techniky doladenia. **Začnite SFT** – pokrýva najširšie spektrum scenárov.

| Technika | Čo robí | Kedy ju použiť |
| --- | --- | --- |
| **Supervised Fine-Tuning (SFT)** | Trénuje na pároch vstup/výstup, aby sa model naučil produkovať požadované odpovede. | Štandard pre väčšinu úloh: špecializácia na doménu, výkon úlohy, štýl a tón, sledovanie inštrukcií, a adaptácia jazyka. |
| **Direct Preference Optimization (DPO)** | Učí sa z párov preferovaných a nepreferovaných odpovedí na zosúladenie výstupov s ľudskými preferenciami. | Zlepšenie kvality odpovedí, bezpečnosti a zosúladenia, keď máte porovnávaciu spätnú väzbu. |
| **Reinforcement Fine-Tuning (RFT)** | Používa odmeňovacie signály od _hodnotiteľov_ na optimalizáciu zložitých správaní s posilňovacím učením. | Objektívne, sťažné domény s jasnými správnymi/chybami odpoveďami (matematika, chémia, fyzika). Vyžaduje väčšiu ML expertízu. |

### Krok 2: Vyberte úroveň tréningu

Foundry vám umožňuje vybrať, ako a kde sa tréning spustí:

- **Štandardná** - trénuje sa v regióne vášho zdroja a garantuje rezidenciu dát. Používajte, keď musia dáta zostať v konkrétnom regióne.
- **Globálna** - lacnejšia a rýchlejšia fronta využitím kapacity mimo vášho regiónu (dáta a váhy sa kopírujú do tréningového regiónu). Dobrá predvolená voľba, keď rezidencia dát nie je požiadavkou.
- **Vývojárska** - najnižšie náklady, využíva nevyužitú kapacitu bez záruk latencie/SLA (úlohy môžu byť prerušované a obnovené). Ideálne na experimentovanie.

### Krok 3: Vyberte základný model

Modely, ktoré je možné doladiť, zahŕňajú OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` a `gpt-4.1-nano` (SFT; rodina 4o/4.1 tiež podporuje DPO), rozumové modely `o4-mini` a `gpt-5` (RFT), plus open-source modely ako `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` a `gpt-oss-20b` (SFT na Foundry zdrojoch). Vždy skontrolujte aktuálny [zoznam doladiteľných modelov](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) pre podporované metódy, regióny a dostupnosť.

> Foundry ponúka dva režimy: **serverless** (cenová politika podľa spotreby, bez správy kvóty GPU, OpenAI a vybrané modely) a **spravované výpočty** (privádzajte vlastné VM cez Azure Machine Learning pre najširšiu škálu modelov). Väčšina ľudí by mala začať so serverless.

### Najlepšie praktiky Foundry

- **Najprv základná línia.** Zmerajte základný model pomocou návrhu promptov a RAG _predtým_, než doladíte, aby ste mohli dokázať zisk.
- **Začnite s malým množstvom, potom škálujte.** Začnite s 50-100 kvalitnými príkladmi na overenie prístupu, potom prejdite na 500+ na produkciu. Kvalita je dôležitejšia ako množstvo – odstráňte nízkokvalitné príklady.
- **Formátujte dáta správne.** Súbory tréningu a validácie musia byť vo formáte JSONL, UTF-8 **s BOM**, pod 512 MB, používajúc formát správ chat-completions. Vždy zahrňte validáciu, aby ste mohli sledovať pretrénovanie.
- **Používajte rovnaký systémový prompt pri inferencii.** Použite tú istú systémovú správu, akú ste použili pri tréningu, keď voláte model.
- **Vyhodnocujte kontrolné body – nevyužívajte slepo posledný.** Foundry uchováva posledné tri epochy ako nasaditeľné kontrolné body; vyberte ten, ktorý najlepšie generalizuje sledovaním `train_loss` / `valid_loss` a presnosti tokenov.
- **Merajte náklady na tokeny spolu s kvalitou** pri porovnaní doladeného modelu s základnou líniou.
- **Iterujte s kontinuálnym doladením.** Môžete doladiť už doladený model na nové dáta (podporované pre OpenAI modely).
- **Majte na pamäti náklady na hosting.** Nasadený vlastný model sa účtuje na hodinu a neaktívne nasadenie sa po 15 dňoch odstráni – upracte, čo nepotrebujete.

Prejdite si celý návod v [Prispôsobenie modelu doladením](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) a pozrite si príručky pre [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) a [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst), keď budete pripravení na ďalšie techniky.

## Doladenie v praxi

Nasledujúce zdroje poskytujú podrobné návody, ktoré vás prevedú reálnym príkladom na aktuálne podporovanom modeli s vybranou dátovou sadou. Na ich spracovanie potrebujete účet u konkrétneho poskytovateľa, spolu s prístupom k zodpovedajúcemu modelu a dátam.

| Poskytovateľ | Návod                                                                                                                                                                      | Popis                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Ako doladiť chatovacie modely](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Naučte sa doladiť nedávny chatovací model OpenAI pre konkrétnu doménu („asistent na recepty“) prípravou tréningových dát, spustením úlohy doladenia a použitím doladeného modelu na inferenciu.                                                                                                                                                                                                                                   |
| Microsoft Foundry | [Prispôsobenie modelu doladením](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Naučte sa doladiť aktuálne podporovaný model ako `gpt-4.1-mini` **na Azure** pomocou Microsoft Foundry: príprava & nahrávanie tréningových a validačných dát, spustenie úlohy doladenia, potom nasadenie a použitie nového modelu.                                                                                                                                                                                     |

| Hugging Face | [Doladenie LLM pomocou Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Tento blogový príspevok vás prevedie doladením _otvoreného LLM_ (napr.: `CodeLlama 7B`) pomocou knižnice [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) a [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) s otvorenými [datovými súbormi](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Doladenie LLM pomocou AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (alebo AutoTrain Advanced) je pythonová knižnica vyvinutá Hugging Face, ktorá umožňuje doladenie pre mnoho rôznych úloh vrátane doladenia LLM. AutoTrain je riešenie bez kódu a doladenie môže byť vykonané vo vašom vlastnom cloude, na Hugging Face Spaces alebo lokálne. Podporuje webové GUI, CLI a tréning cez yaml konfiguračné súbory.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Doladenie LLM pomocou Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth je open-source rámec, ktorý podporuje doladenie LLM a posilňovacie učenie (RL). Unsloth zjednodušuje lokálny tréning, hodnotenie a nasadenie s pripravenými na použitie [notebookmi](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Tiež podporuje syntézu reči (TTS), BERT a multimodálne modely. Na začiatok si prečítajte ich krok za krokom [Sprievodcu doladením LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Zadanie

Vyberte si jeden z vyššie uvedených tutoriálov a prejdite si ho. _Tieto tutoriály môžeme replikovať vo verzii Jupyter Notebooks v tomto repozitári len ako referenciu. Pre najnovšie verzie prosím používajte originálne zdroje priamo_.

## Skvelá práca! Pokračujte v učení.

Po dokončení tejto lekcie si pozrite našu [kolekciu vzdelávania Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v zdokonaľovaní svojich vedomostí o Generatívnej AI!

Gratulujeme!! Dokončili ste poslednú lekciu z v2 série tohto kurzu! Nezastavujte sa v učení a tvorbe. \*\*Pozrite si stránku [Zdroje](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pre zoznam ďalších odporúčaní na túto tému.

Naša séria v1 lekcií bola tiež aktualizovaná s ďalšími zadaniami a konceptmi. Tak si nájdite chvíľku na obnovenie svojich vedomostí - a prosím [zdieľajte vaše otázky a spätnú väzbu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), aby sme mohli tieto lekcie zlepšiť pre komunitu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->