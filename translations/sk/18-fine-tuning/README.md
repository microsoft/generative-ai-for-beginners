<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T21:59:00+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "sk"
}
-->
[![Open Source Models](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.sk.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Jemné doladenie vášho LLM

Používanie veľkých jazykových modelov na vytváranie aplikácií generatívnej AI prináša nové výzvy. Kľúčovým problémom je zabezpečenie kvality odpovedí (presnosť a relevantnosť) v obsahu generovanom modelom na základe požiadavky používateľa. V predchádzajúcich lekciách sme diskutovali o technikách, ako je návrh výzvy (prompt engineering) a generovanie s rozšíreným vyhľadávaním, ktoré sa snažia vyriešiť problém _úpravou vstupu výzvy_ existujúceho modelu.

V dnešnej lekcii sa zaoberáme treťou technikou, **jemným doladením**, ktorá sa snaží riešiť výzvu _pretrénovaním samotného modelu_ s dodatočnými údajmi. Poďme sa pozrieť na detaily.

## Ciele učenia

Táto lekcia predstavuje koncept jemného doladenia pre predtrénované jazykové modely, skúma výhody a výzvy tohto prístupu a poskytuje usmernenia, kedy a ako použiť jemné doladenie na zlepšenie výkonu vašich generatívnych AI modelov.

Na konci tejto lekcie by ste mali vedieť odpovedať na nasledujúce otázky:

- Čo je jemné doladenie jazykových modelov?
- Kedy a prečo je jemné doladenie užitočné?
- Ako môžem jemne doladiť predtrénovaný model?
- Aké sú obmedzenia jemného doladenia?

Pripravení? Poďme na to.

## Ilustrovaný sprievodca

Chcete si urobiť prehľad o tom, čo budeme preberať, ešte predtým, než sa do toho pustíme? Pozrite si tento ilustrovaný sprievodca, ktorý popisuje učebnú cestu tejto lekcie - od učenia sa základných konceptov a motivácie pre jemné doladenie až po pochopenie procesu a najlepších postupov pri vykonávaní úlohy jemného doladenia. Je to fascinujúca téma na preskúmanie, takže nezabudnite navštíviť stránku [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pre ďalšie odkazy na podporu vašej samostatnej učebnej cesty!

![Ilustrovaný sprievodca jemným doladením jazykových modelov](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.sk.png)

## Čo je jemné doladenie jazykových modelov?

Podľa definície sú veľké jazykové modely _predtrénované_ na veľkých množstvách textu získaného z rôznych zdrojov vrátane internetu. Ako sme sa naučili v predchádzajúcich lekciách, na zlepšenie kvality odpovedí modelu na otázky používateľa ("výzvy") potrebujeme techniky ako _návrh výzvy_ a _generovanie s rozšíreným vyhľadávaním_.

Populárna technika návrhu výzvy zahŕňa poskytnutie modelu väčšieho množstva pokynov o tom, čo sa očakáva v odpovedi, buď poskytnutím _inštrukcií_ (explicitné usmernenie), alebo _poskytnutím niekoľkých príkladov_ (implicitné usmernenie). Toto sa nazýva _few-shot learning_, ale má dve obmedzenia:

- Limity tokenov modelu môžu obmedziť počet príkladov, ktoré môžete poskytnúť, a tým znížiť efektivitu.
- Náklady na tokeny modelu môžu byť drahé pri pridávaní príkladov ku každej výzve, čo obmedzuje flexibilitu.

Jemné doladenie je bežná prax v systémoch strojového učenia, kde vezmeme predtrénovaný model a pretrénujeme ho s novými údajmi, aby sme zlepšili jeho výkon na konkrétnej úlohe. V kontexte jazykových modelov môžeme jemne doladiť predtrénovaný model _s kurátorskou sadou príkladov pre danú úlohu alebo aplikačnú oblasť_, aby sme vytvorili **vlastný model**, ktorý môže byť presnejší a relevantnejší pre túto konkrétnu úlohu alebo oblasť. Vedľajším prínosom jemného doladenia je, že môže tiež znížiť počet potrebných príkladov pre few-shot learning - čím sa znižuje používanie tokenov a súvisiace náklady.

## Kedy a prečo by sme mali jemne doladiť modely?

V _tomto_ kontexte, keď hovoríme o jemnom doladení, máme na mysli **supervízované** jemné doladenie, kde sa pretrénovanie vykonáva **pridaním nových údajov**, ktoré neboli súčasťou pôvodného tréningového datasetu. To sa líši od nesupervízovaného jemného doladenia, kde sa model pretrénuje na pôvodných údajoch, ale s rôznymi hyperparametrami.

Kľúčová vec, ktorú si treba zapamätať, je, že jemné doladenie je pokročilá technika, ktorá si vyžaduje určitú úroveň odbornosti na dosiahnutie požadovaných výsledkov. Ak sa vykoná nesprávne, nemusí priniesť očakávané zlepšenia a môže dokonca zhoršiť výkon modelu pre váš cieľový doménový priestor.

Takže predtým, než sa naučíte "ako" jemne doladiť jazykové modely, musíte vedieť "prečo" by ste mali zvoliť túto cestu a "kedy" začať proces jemného doladenia. Začnite tým, že si položíte tieto otázky:

- **Použitie**: Aký je váš _prípad použitia_ pre jemné doladenie? Aký aspekt aktuálneho predtrénovaného modelu chcete zlepšiť?
- **Alternatívy**: Skúsili ste _iné techniky_ na dosiahnutie požadovaných výsledkov? Použite ich na vytvorenie základnej línie pre porovnanie.
  - Návrh výzvy: Skúste techniky ako few-shot prompting s príkladmi relevantných odpovedí na výzvy. Vyhodnoťte kvalitu odpovedí.
  - Generovanie s rozšíreným vyhľadávaním: Skúste rozšíriť výzvy výsledkami vyhľadávania vo vašich údajoch. Vyhodnoťte kvalitu odpovedí.
- **Náklady**: Identifikovali ste náklady na jemné doladenie?
  - Možnosť doladenia - je predtrénovaný model dostupný na jemné doladenie?
  - Úsilie - na prípravu tréningových údajov, hodnotenie a doladenie modelu.
  - Výpočtová kapacita - na spustenie úloh jemného doladenia a nasadenie jemne doladeného modelu.
  - Údaje - prístup k dostatočnému množstvu kvalitných príkladov na dosiahnutie vplyvu jemného doladenia.
- **Výhody**: Potvrdili ste výhody jemného doladenia?
  - Kvalita - prekonal jemne doladený model základnú líniu?
  - Náklady - znižuje používanie tokenov zjednodušením výziev?
  - Rozšíriteľnosť - môžete základný model prispôsobiť novým doménam?

Odpoveďou na tieto otázky by ste mali byť schopní rozhodnúť, či je jemné doladenie správnym prístupom pre váš prípad použitia. Ideálne je, ak prístup platí iba vtedy, ak výhody prevažujú nad nákladmi. Keď sa rozhodnete pokračovať, je čas premýšľať o _tom, ako_ môžete jemne doladiť predtrénovaný model.

Chcete získať viac informácií o rozhodovacom procese? Pozrite si [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Ako môžeme jemne doladiť predtrénovaný model?

Na jemné doladenie predtrénovaného modelu potrebujete:

- predtrénovaný model na jemné doladenie
- dataset na použitie pri jemnom doladení
- tréningové prostredie na spustenie úlohy jemného doladenia
- hostingové prostredie na nasadenie jemne doladeného modelu

## Jemné doladenie v praxi

Nasledujúce zdroje poskytujú podrobné návody, ktoré vás prevedú skutočným príkladom použitia vybraného modelu s kurátorským datasetom. Na prácu s týmito návodmi potrebujete účet u konkrétneho poskytovateľa spolu s prístupom k relevantnému modelu a datasetom.

| Poskytovateľ | Návod                                                                                                                                                                       | Popis                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Ako jemne doladiť chatovacie modely](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)       | Naučte sa jemne doladiť `gpt-35-turbo` pre konkrétnu doménu ("asistent receptov") prípravou tréningových údajov, spustením úlohy jemného doladenia a použitím jemne doladeného modelu na inferenciu.                                                                                                                                                                                                                              |
| Azure OpenAI | [Návod na jemné doladenie GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Naučte sa jemne doladiť model `gpt-35-turbo-0613` **na Azure** vykonaním krokov na vytvorenie a nahranie tréningových údajov, spustenie úlohy jemného doladenia. Nasadenie a použitie nového modelu.                                                                                                                                                                                                                             |
| Hugging Face | [Jemné doladenie LLMs s Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                           | Tento blogový príspevok vás prevedie jemným doladením _otvoreného LLM_ (napr. `CodeLlama 7B`) pomocou knižnice [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) a [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) s otvorenými [datasetmi](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|              |                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Jemné doladenie LLMs s AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                     | AutoTrain (alebo AutoTrain Advanced) je python knižnica vyvinutá spoločnosťou Hugging Face, ktorá umožňuje jemné doladenie pre mnoho rôznych úloh vrátane jemného doladenia LLM. AutoTrain je riešenie bez potreby kódu a jemné doladenie je možné vykonať vo vašom vlastnom cloude, na Hugging Face Spaces alebo lokálne. Podporuje webové GUI, CLI a tréning prostredníctvom yaml konfiguračných súborov.                                           |
|              |                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Zadanie

Vyberte si jeden z vyššie uvedených návodov a prejdite si ho. _Môžeme replikovať verziu týchto návodov v Jupyter Notebooks v tomto repozitári len na referenciu. Prosím, použite priamo pôvodné zdroje na získanie najnovších verzií_.

## Skvelá práca! Pokračujte vo svojom učení.

Po dokončení tejto lekcie si pozrite našu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v rozširovaní svojich znalostí o generatívnej AI!

Gratulujeme!! Dokončili ste poslednú lekciu zo série v2 tohto kurzu! Nezastavujte sa v učení a budovaní. \*\*Pozrite si stránku [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pre zoznam ďalších návrhov práve na túto tému.

Naša séria lekcií v1 bola tiež aktualizovaná s viacerými zadaniami a konceptmi. Takže si nájdite chvíľu na osvieženie svojich vedomostí - a prosím [zdieľajte svoje otázky a spätnú väzbu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), aby ste nám pomohli zlepšiť tieto lekcie pre komunitu.

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.