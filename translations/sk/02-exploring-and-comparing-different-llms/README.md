# Preskúmanie a porovnanie rôznych LLM

[![Preskúmanie a porovnanie rôznych LLM](../../../translated_images/sk/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie_

V predchádzajúcej lekcii sme videli, ako Generatívna AI mení technologickú krajinu, ako fungujú veľké jazykové modely (LLM) a ako ich môže podnik – ako napríklad náš startup – použiť na svoje prípady použitia a rásť! V tejto kapitole sa budeme snažiť porovnať a kontrastovať rôzne typy veľkých jazykových modelov (LLM), aby sme pochopili ich výhody a nevýhody.

Ďalším krokom na našej start-upovej ceste je preskúmať súčasný trh LLM a pochopiť, ktoré sú vhodné na náš prípad použitia.

## Úvod

Táto lekcia bude obsahovať:

- Rôzne typy LLM v súčasnom prostredí.
- Testovanie, iterovanie a porovnávanie rôznych modelov pre váš prípad použitia v Azure.
- Ako nasadiť LLM.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

- Vybrať správny model pre svoj prípad použitia.
- Pochopiť, ako testovať, iterovať a zlepšovať výkon modelu.
- Vedieť, ako podniky nasadzujú modely.

## Pochopiť rôzne typy LLM

LLM môžu mať viacero kategorizácií podľa ich architektúry, tréningových dát a prípadu použitia. Pochopenie týchto rozdielov pomôže nášmu start-upu vybrať správny model pre daný scenár a pochopiť, ako testovať, iterovať a zlepšovať výkon.

Existuje mnoho rôznych typov LLM modelov, výber modelu závisí od toho, na čo ich chcete použiť, aké máte dáta, koľko ste ochotní zaplatiť a ďalšie faktory.

Podľa cieľa použitia modelov na text, audio, video, generovanie obrázkov a pod. môžete zvoliť iný typ modelu.

- **Rozpoznávanie zvuku a reči**. Modely typu Whisper sú stále užitočné všeobecné modely rozpoznávania reči, ale produkčné voľby teraz zahŕňajú aj novšie modely pre prevod reči na text, ako napríklad `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` a varianty diarizácie. Zhodnoťte pokrytie jazykov, diarizáciu, podporu v reálnom čase, oneskorenie a náklady pre váš scenár. Viac sa dozviete v [dokumentácii OpenAI pre prevod reči na text](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Generovanie obrázkov**. DALL-E a Midjourney sú známe možnosti generovania obrázkov, ale súčasné OpenAI obrazy API sú založené na GPT Image modeloch ako `gpt-image-2`, zatiaľ čo Stable Diffusion, Imagen, Flux a iné rodiny modelov sú tiež bežné voľby. Porovnajte dodržiavanie promptov, podporu úprav, kontrolu štýlu, bezpečnostné požiadavky a licencie. Viac sa dozviete v [návode OpenAI pre generovanie obrázkov](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) a v kapitole 9 tohto kurikula.

- **Generovanie textu**. Textové modely teraz pokrývajú špičkové modely, modely na rozumné uvažovanie, menšie modely s nízkou latenciou a modely s otvorenou váhou. Príklady sú OpenAI GPT-5.x modely, Anthropic Claude 4.x modely, Google Gemini 3.x modely, Meta Llama 4 modely a Mistral modely. Nevychádzajte iba z dátumu vydania alebo ceny; porovnajte kvalitu úloh, latenciu, veľkosť kontextového okna, použitie nástrojov, bezpečnostné správanie, regionálnu dostupnosť a celkové náklady. [Microsoft Foundry modelový katalóg](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) je dobré miesto na porovnávanie modelov dostupných v Azure.

- **Multimodalita**. Mnoho súčasných modelov spracováva viac než len text. Niektoré prijímajú vstupy v podobe obrazu, zvuku alebo videa; niektoré môžu volať nástroje; a špecializované modely môžu generovať obrázky, zvuk alebo video. Napríklad súčasné OpenAI modely podporujú textové a obrazové vstupy, Gemini modely môžu podporovať text, kód, obraz, zvuk a video podľa variantu, a Llama 4 Scout a Maverick sú nativne multimodálne modely s otvorenou váhou. Vždy si skontrolujte kartu modelu pre podporované vstupy a výstupy pred vytvorením workflow založeného na ňom.

Výber modelu znamená, že získate základné schopnosti, ktoré však nemusia byť dostatočné. Často máte firemné špecifické dáta, o ktorých je potrebné modelu LLM niečo povedať. Existuje niekoľko rôznych možností, ako to spraviť, o tom viac v nasledujúcich častiach.

### Základné modely verzus LLM

Termín Základný model bol [uvoľnený výskumníkmi zo Stanfordu](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) a definovaný ako AI model, ktorý spĺňa isté kritériá, napríklad:

- **Sú trénované pomocou neřídeného učenia alebo sebariadeného učenia**, čo znamená, že sú trénované na nelatkovaných multimodálnych dátach a nepotrebujú ľudské anotácie alebo štítkovanie dát pre proces tréningu.
- **Sú veľmi veľké modely**, založené na veľmi hlbokých neurónových sieťach trénovaných na miliardách parametrov.
- **Normálne majú slúžiť ako „základ“ pre iné modely**, čo znamená, že môžu byť použité ako východiskový bod pre tvorbu ďalších modelov, ktoré sa môžu ďalej dolaďovať.

![Základné modely verzus LLM](../../../translated_images/sk/FoundationModel.e4859dbb7a825c94.webp)

Zdroj obrázka: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Aby sme túto rozdielnosť ďalej objasnili, pozrime sa na ChatGPT ako historický príklad. Rané verzie ChatGPT používali GPT-3.5 ako základný model. OpenAI potom použil chat-špecifické dáta a techniky zaradenia na vytvorenie doladenej verzie, ktorá fungovala lepšie v konverzačných scenároch, ako sú chatboti. Moderné AI služby často prepínajú medzi viacerými variantmi modelov, takže názov služby a základného modelu nie sú vždy rovnaké.

![Základný model](../../../translated_images/sk/Multimodal.2c389c6439e0fc51.webp)

Zdroj obrázka: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Otvorené váhy / open-source verzus proprietárne modely

Ďalším spôsobom kategorizácie LLM je, či sú modely s otvorenou váhou, open-source alebo proprietárne.

Open-source a open-weight modely umožňujú preskúmanie, stiahnutie alebo prispôsobenie modelových artefaktov, no ich licencie sa líšia. Niektoré sú úplne otvorené, iné majú obmedzenia používania. Môžu byť užitočné, keď podnik potrebuje väčšiu kontrolu nad nasadením, lokalitou dát, nákladmi alebo prispôsobením. Tímy však musia vždy skontrolovať licenčné podmienky, náklady na prevádzku, údržbu, bezpečnostné aktualizácie a kvalitu hodnotenia pred použitím v produkcii. Príklady sú [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), niektoré [Mistral modely](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) a mnoho modelov hosťovaných na [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Proprietárne modely sú vo vlastníctve a spravované poskytovateľom. Tieto modely sú často optimalizované pre produkčné použitie s manažmentom a môžu ponúkať silnú podporu, bezpečnostné systémy, integráciu nástrojov a škálovateľnosť. Zvyčajne ich zákazníci nemôžu preskúmať ani modifikovať váhy modelu, a musia sa zoznámiť s pravidlami poskytovateľa o súkromí, uchovaní dát, súlade a prijateľnom použití. Príklady zahŕňajú [OpenAI modely](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) a [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding versus generovanie obrázkov versus generovanie textu a kódu

LLM sa tiež kategorizujú podľa výstupu, ktorý vytvárajú.

Embedding modely sú skupina modelov, ktoré dokážu premeniť text na číselnú formu, nazývanú embedding, čo je číselná reprezentácia vstupného textu. Embedding modely uľahčujú počítačom pochopenie vzťahov medzi slovami alebo vetami a môžu sa použiť ako vstupy pre iné modely, ako sú klasifikačné alebo klastračné modely s lepším výkonom na číselných dátach. Embedding modely sa často používajú pri transferovom učení, kde sa model vytvorí pre náhradnú úlohu, pre ktorú existuje veľa dát, a potom sa váhy modelu (embeddingy) znovu použijú pre ďalšie úlohy. Príkladom je [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/sk/Embedding.c3708fe988ccf760.webp)

Modely generujúce obrázky sú modely, ktoré vytvárajú obrázky. Tieto modely sa často používajú na úpravu obrázkov, syntézu obrázkov a preklad obrázkov. Modely generujúce obrázky sú často trénované na veľkých dátových súboroch obrázkov, ako je [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), a môžu sa použiť na generovanie nových obrázkov alebo na úpravu existujúcich obrázkov pomocou techník inpaintingu, superrozlíšenia a kolorovania. Príklady zahŕňajú [GPT Image modely](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion modely](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) a Imagen modely.

![Generovanie obrázkov](../../../translated_images/sk/Image.349c080266a763fd.webp)

Modely generujúce text a kód sú modely, ktoré vytvárajú text alebo kód. Tieto modely sa často používajú na sumarizáciu textu, preklad a odpovede na otázky. Textové modely sú často trénované na veľkých dátových súboroch textu, ako je [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), a môžu sa použiť na generovanie nového textu alebo na odpovede na otázky. Modely generujúce kód, ako napríklad [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), sú často trénované na veľkých dátových súboroch kódu, ako je GitHub, a môžu sa použiť na generovanie nového kódu alebo na opravu chýb v existujúcom kóde.

![Generovanie textu a kódu](../../../translated_images/sk/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder verzus len Decoder

Aby sme si vysvetlili rôzne architektúry LLM, použijeme analógiu.

Predstavte si, že vám váš manažér zadal úlohu pripraviť kvíz pre študentov. Máte dvoch kolegov; jeden dohliada na tvorbu obsahu a druhý na jeho kontrolu.

Tvorca obsahu je ako model len s dekóderom: môže vidieť tému, čo ste už napísali, a pokračovať v generovaní obsahu na základe kontextu. Sú veľmi dobrí v písaní pútavého a informatívneho obsahu, no nie sú vždy tou najlepšou voľbou na klasifikovanie, vyhľadávanie alebo zakódovanie informácií. Príklady modelových rodín s len dekóderom sú modely GPT a Llama.

Kontrolór je ako model, ktorý je len enkóder, pozrie si napísaný kvíz a odpovede, všimne si vzťahy medzi nimi a pochopí kontext, ale nie je dobrý v generovaní obsahu. Príkladom modelu len s enkóderom je BERT.

Predstavte si, že môžeme mať niekoho, kto by dokázal kvíz aj vytvoriť, aj skontrolovať, to je model Encoder-Decoder. Príkladmi sú BART a T5.

### Služba verzus Model

Teraz si prejdime rozdiel medzi službou a modelom. Služba je produkt ponúkaný poskytovateľom cloudových služieb a často je kombináciou modelov, dát a ďalších komponentov. Model je jadro služby a často je základný model, ako LLM.

Služby sú často optimalizované pre produkčné použitie a môžu byť jednoduchšie na použitie než modely, napríklad cez grafické používateľské rozhranie. Avšak služby nie sú vždy zadarmo, a môžu vyžadovať predplatné alebo platbu, na oplátku za používanie vybavenia a zdrojov vlastníka služby, čo optimalizuje náklady a uľahčuje škálovanie. Príkladom služby je [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), ktorá ponúka platbu podľa spotreby, teda účtuje sa úmerne tomu, koľko služby používate. Azure OpenAI Service tiež ponúka bezpečnosť na podnikovej úrovni a rámec zodpovednej AI nad schopnosťami modelov.

Modely sú neurónové siete: parametre, váhy, architektúra, tokenizér a podporná konfigurácia. Používanie modelu lokálne alebo v súkromnom prostredí vyžaduje vhodný hardvér, infraštruktúru, monitoring a buď kompatibilnú licenciu open-source / open-weight, alebo komerčnú licenciu. Modely s otvorenou váhou ako Llama 4 alebo Mistral modely je možné hosťovať samostatne, no stále vyžadujú výpočtový výkon a prevádzkovú expertízu.

## Ako testovať a iterovať s rôznymi modelmi na pochopenie výkonu v Azure


Ak náš tím preskúmal súčasný stav LLM a identifikoval niekoľko dobrých kandidátov pre ich scenáre, ďalším krokom je testovanie ich na ich dátach a v ich záťaži. Ide o iteratívny proces vykonávaný prostredníctvom experimentov a meraní.
Väčšina modelov spomenutých v predchádzajúcich odstavcoch (modely OpenAI, modely s otvorenou váhou ako Llama 4 a Mistral a modely Hugging Face) je dostupná v [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), predtým Azure AI Studio/Azure AI Foundry, je jednotná platforma Azure pre budovanie AI aplikácií a agentov. Pomáha vývojárom spravovať životný cyklus od experimentovania a hodnotenia až po nasadenie, monitorovanie a správu. Katalóg modelov v Microsoft Foundry umožňuje používateľovi:

- Nájsť základný model záujmu v katalógu, vrátane modelov predávaných cez Azure a modelov od partnerov a komunitných poskytovateľov. Používatelia môžu filtrovať podľa úlohy, poskytovateľa, licencie, možnosti nasadenia alebo názvu.

![Model catalog](../../../translated_images/sk/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Prezrieť si kartu modelu, vrátane podrobného popisu zamýšľaného použitia a tréningových dát, ukážky kódu a výsledky hodnotení v internej knižnici hodnotení.

![Model card](../../../translated_images/sk/ModelCard.598051692c6e400d.webp)

- Porovnávať benchmarky medzi modelmi a datasetmi dostupnými v odbore, aby sa zistilo, ktorý najlepšie vyhovuje podnikateľskému scenáru, cez panel [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/sk/ModelBenchmarks.254cb20fbd06c03a.webp)

- Doladiť podporované modely na vlastných tréningových dátach, aby sa zlepšil výkon modelu v konkrétnej záťaži, pričom sa využívajú schopnosti experimentovania a sledovania Microsoft Foundry.

![Model fine-tuning](../../../translated_images/sk/FineTuning.aac48f07142e36fd.webp)

- Nasadiť pôvodný predtrénovaný model alebo jeho doladenú verziu do vzdialeného inferenčného endpointu v reálnom čase, pomocou spravovaných výpočtov alebo serverless možností nasadenia, aby mohol byť model využívaný aplikáciami.

![Model deployment](../../../translated_images/sk/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Nie všetky modely v katalógu sú momentálne dostupné na doladenie a/alebo nasadenie podľa spotreby. Skontrolujte kartu modelu pre detaily o schopnostiach a obmedzeniach modelu.

## Zlepšenie výsledkov LLM

S našim startup tímom sme preskúmali rôzne druhy LLM a cloudovú platformu (Microsoft Foundry), ktorá nám umožňuje porovnávať rôzne modely, hodnotiť ich na testovacích dátach, zlepšovať výkon a nasadzovať ich na inferenčné endpointy.

Ale kedy by mali zvážiť doladenie modelu namiesto použitia predtrénovaného? Existujú aj iné prístupy na zlepšenie výkonu modelu v konkrétnych záťažiach?

Existuje niekoľko prístupov, ktoré môže podnik použiť, aby dosiahol požadované výsledky z LLM. Pri nasadení LLM do produkcie môžete vybrať rôzne typy modelov s rôznou mierou tréningu, s rôznou úrovňou zložitosti, nákladov a kvality. Tu sú niektoré prístupy:

- **Prompt engineering s kontextom**. Myšlienka je poskytnúť dostatok kontextu, keď zadáte prompt, aby ste mali odpovede, ktoré potrebujete.

- **Retrieval Augmented Generation, RAG**. Vaše dáta môžu existovať napríklad v databáze alebo webovom endpointu, aby sa zabezpečilo začlenenie týchto dát alebo ich podmnožiny v momente promptovania, môžete získať relevantné dáta a pridať ich do promptu používateľa.

- **Doladený model**. Tu ste model ďalej trénovali na vlastných dátach, čo viedlo k tomu, že model je presnejší a flexibilnejší voči vašim potrebám, ale môže to byť nákladné.

![LLMs deployment](../../../translated_images/sk/Deploy.18b2d27412ec8c02.webp)

Zdroj obrázka: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt engineering s kontextom

Predtrénované LLM fungujú veľmi dobre na generalizovaných úlohách spracovania prirodzeného jazyka, dokonca aj keď sú zavolané krátkym promptom, ako doplnením vety alebo otázkou – tzv. „zero-shot“ učenie.

Avšak čím viac používateľ vie svoj dotaz rámcovať s podrobnou požiadavkou a príkladmi – Kontextom – tým presnejšia a bližšia očakávaniam používateľa bude odpoveď. V tomto prípade hovoríme o „one-shot“ učení, ak prompt obsahuje len jeden príklad, a o „few-shot“ učení, ak obsahuje viacero príkladov.
Prompt engineering s kontextom je nákladovo najefektívnejším prístupom na začatie.

### Retrieval Augmented Generation (RAG)

LLM majú obmedzenie, že môžu použiť iba údaje, ktoré boli použité počas ich tréningu na generovanie odpovede. To znamená, že nepoznajú fakty, ktoré sa stali po ich tréningovom procese, a nemajú prístup k neverejným informáciám (ako sú firemné dáta).
Toto sa dá prekonať pomocou RAG, techniky, ktorá dopĺňa prompt externými dátami vo forme častí dokumentov, pričom sa zohľadňujú limity dĺžky promptu. Toto podporujú nástroje na prácu s vektorovými databázami (ako [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), ktoré vyhľadávajú užitočné časti z rôznych vopred definovaných zdrojov dát a pridávajú ich do kontextu promptu.

Táto technika je veľmi užitočná, keď podnik nemá dostatok dát, času alebo zdrojov na doladenie LLM, ale stále chce zlepšiť výkon v konkrétnej záťaži a znížiť riziká z halucinovaných, zastaraných alebo nepodporovaných odpovedí.

### Doladený model

Doladenie je proces, ktorý využíva transfer learning na „prispôsobenie“ modelu na podradenú úlohu alebo na riešenie konkrétneho problému. Na rozdiel od few-shot učenia a RAG, vedie k vytvoreniu nového modelu s aktualizovanými váhami a posunmi. Vyžaduje súbor tréningových príkladov pozostávajúci z jedného vstupu (promptu) a jeho priradeného výstupu (doplnenia).
Tento prístup by bol preferovaný, ak:

- **Používate menšie modely špecifické na úlohu**. Podnik by chcel doladiť menší model pre úzko špecializovanú úlohu namiesto opakovaného promptovania väčšieho hraničného modelu, čo vedie k nákladovo efektívnejšiemu a rýchlejšiemu riešeniu.

- **Zohľadňuje latenciu**. Latencia je dôležitá pre konkrétny prípad použitia, takže nie je možné používať veľmi dlhé prompty alebo počet príkladov, z ktorých sa má model učiť, nevyhovuje limitu dĺžky promptu.

- **Prispôsobuje stabilné správanie**. Podnik má množstvo vysoko kvalitných príkladov a chce, aby model konzistentne sledoval vzor úlohy, formát výstupu, tón alebo špecifický štýl domény. Ak je hlavný problém čerstvé fakty alebo súkromné poznatky, ktoré sa často menia, použite namiesto samotného doladenia RAG.

### Trénovaný model

Tréning LLM od základu je bezpochyby najnáročnejší a najzložitejší prístup na adoptovanie, vyžadujúci obrovské množstvo dát, skúsené zdroje a primeraný výpočtový výkon. Túto možnosť treba zvážiť len v scenári, kde má podnik používanie špecifické pre doménu a veľké množstvo dát centrálnych pre túto doménu.

## Overenie vedomostí

Aký by mohol byť dobrý prístup na zlepšenie výsledkov doplnenia LLM?

1. Prompt engineering s kontextom
1. RAG
1. Doladený model

O: Všetky tri môžu pomôcť. Začnite s prompt engineeringom a kontextom pre rýchle zlepšenia a používajte RAG, keď model potrebuje aktuálne fakty alebo súkromné podnikové dáta. Vyberte doladenie, keď máte dostatok vysoko kvalitných príkladov a potrebujete, aby model konzistentne dodržiaval úlohu, formát, tón alebo vzor domény.

## 🚀 Výzva

Prečítajte si viac o tom, ako môžete [použiť RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) pre vaše podnikanie.

## Skvelá práca, pokračujte v učení

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali vo zvyšovaní vedomostí o Generatívnej AI!

Prejdite na Lekciu 3, kde sa pozrieme na to, ako [stavať s Generatívnou AI zodpovedne](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->