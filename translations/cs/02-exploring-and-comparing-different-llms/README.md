# Průzkum a porovnání různých LLM

[![Průzkum a porovnání různých LLM](../../../translated_images/cs/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Klikněte na obrázek výše pro zobrazení videa této lekce_

V předchozí lekci jsme viděli, jak Generativní AI mění technologickou krajinu, jak fungují velké jazykové modely (LLM) a jak je může podnik - jako náš startup - aplikovat na své případové použití a růst! V této kapitole si chceme porovnat a rozlišit různé typy velkých jazykových modelů (LLM), abychom pochopili jejich výhody a nevýhody.

Dalším krokem v cestě našeho startupu je prozkoumání současné krajiny LLM a porozumění tomu, které jsou vhodné pro náš případ použití.

## Úvod

Tato lekce pokryje:

- Různé typy LLM v současné krajině.
- Testování, iteraci a porovnávání různých modelů pro váš případ použití v Azure.
- Jak nasadit LLM.

## Výukové cíle

Po dokončení této lekce budete schopni:

- Vybrat správný model pro váš případ použití.
- Porozumět tomu, jak testovat, iterovat a zlepšovat výkon svého modelu.
- Vědět, jak podniky nasazují modely.

## Porozumět různým typům LLM

LLM lze kategorizovat různými způsoby podle jejich architektury, tréninkových dat a případu použití. Porozumění těmto rozdílům pomůže našemu startupu vybrat správný model pro daný scénář a pochopit, jak testovat, iterovat a zlepšovat výkon.

Existuje mnoho různých typů LLM modelů, výběr modelu závisí na tom, k čemu je chcete používat, jaká máte data, kolik jste ochotni zaplatit a další faktory.

V závislosti na tom, zda chcete modely použít pro text, audio, video, generování obrázků a podobně, můžete volit jiný typ modelu.

- **Rozpoznávání zvuku a řeči**. Modely ve stylu Whisper jsou stále užitečné obecné modely pro rozpoznávání řeči, ale produkčně se nyní používají také novější modely převodu řeči na text, jako `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` a varianty pro diarizaci. Vyhodnoťte pokrytí jazyků, diarizaci, podporu v reálném čase, latenci a náklady pro váš scénář. Více se dozvíte v [dokumentaci OpenAI k převodu řeči na text](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Generování obrazů**. DALL-E a Midjourney jsou známé možnosti generování obrázků, ale aktuální OpenAI image API jsou založena na GPT Image modelech, jako je `gpt-image-2`, zatímco Stable Diffusion, Imagen, Flux a další rodiny modelů jsou rovněž běžné. Porovnejte dodržování promptu, podporu úprav, kontrolu stylu, bezpečnostní požadavky a licencování. Více se dozvíte v [průvodci OpenAI generováním obrazů](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) a v kapitole 9 tohoto kurikula.

- **Generování textu**. Textové modely nyní zahrnují frontové modely, modely pro uvažování, menší modely s nízkou latencí a modely s otevřenou vahou. Aktuální příklady jsou OpenAI GPT-5.x modely, Anthropic Claude 4.x modely, Google Gemini 3.x modely, Meta Llama 4 modely a Mistral modely. Nevybírejte jen podle data vydání nebo ceny; porovnejte kvalitu úloh, latenci, kontextové okno, použití nástrojů, bezpečnostní chování, regionální dostupnost a celkové náklady. [Microsoft Foundry katalog modelů](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) je dobrým místem k porovnání modelů dostupných v Azure.

- **Multimodalita**. Mnoho současných modelů může zpracovávat více než text. Některé přijímají vstupy obrázků, zvuku nebo videa; některé mohou volat nástroje; a specializované modely mohou generovat obrázky, zvuk nebo video. Například aktuální OpenAI modely podporují text a vstup obrázků, Gemini modely mohou podporovat text, kód, obrázky, zvuk a video v závislosti na variantě, a Llama 4 Scout a Maverick jsou nativně multimodální modely s otevřenou vahou. Vždy zkontrolujte popis modelu (model card) pro podporované vstupní a výstupní modality před vytvořením pracovního postupu.

Výběr modelu znamená získání základních schopností, které však nemusí být dostačující. Často máte data specifická pro firmu, o kterých je třeba LLM nějak informovat. Existuje několik různých způsobů, jak k tomu přistoupit, více o tom v následujících sekcích.

### Základní modely versus LLM

Termín Základní model (Foundation Model) byl [zaveden vědci ze Stanfordu](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) a definuje se jako AI model, který splňuje určitá kritéria, jako například:

- **Jsou trénovány pomocí učení bez dozoru nebo samo-řízeného učení**, což znamená, že jsou trénovány na neoznačených multimodálních datech a nevyžadují lidskou anotaci nebo označování dat pro trénink.
- **Jsou to velmi velké modely**, založené na velmi hlubokých neuronových sítích trénovaných na miliardách parametrů.
- **Obvykle slouží jako "základ" pro další modely**, což znamená, že mohou být použity jako výchozí bod pro další modely, které lze ladit (fine-tune).

![Základní modely versus LLM](../../../translated_images/cs/FoundationModel.e4859dbb7a825c94.webp)

Zdroj obrázku: [Essential Guide to Foundation Models and Large Language Models | od Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Pro lepší pochopení tohoto rozlišení vezměme ChatGPT jako historický příklad. Rané verze ChatGPT používaly GPT-3.5 jako základní model. OpenAI pak použil data specifická pro chat a techniky zarovnání, aby vytvořil doladěnou verzi, která fungovala lépe v konverzačních scénářích, jako jsou chatboty. Moderní AI služby často přepínají mezi několika variantami modelů, takže název služby a základní model nemusí být vždy stejný.

![Základní model](../../../translated_images/cs/Multimodal.2c389c6439e0fc51.webp)

Zdroj obrázku: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modely s otevřenou vahou / open-source versus proprietární modely

Další způsob klasifikace LLM je podle toho, zda jsou open-weight, open-source nebo proprietární.

Open-source a modely s otevřenou vahou umožňují přístup k artefaktům modelu pro inspekci, stažení nebo přizpůsobení, ale jejich licence se liší. Některé jsou plně open-source, jiné jsou open-weight s omezeními použití. Mohou být užitečné, když firma potřebuje větší kontrolu nad nasazením, lokalitou dat, náklady nebo přizpůsobením. Nicméně týmy stále musí zkontrolovat licenční podmínky, náklady na provoz, údržbu, bezpečnostní aktualizace a kvalitu hodnocení před použitím v produkci. Příklady zahrnují [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), některé [Mistral modely](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) a mnoho modelů hostovaných na [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Proprietární modely jsou vlastněny a hostovány poskytovatelem. Tyto modely jsou často optimalizované pro řízený produkční provoz a mohou nabízet robustní podporu, bezpečnostní systémy, integraci nástrojů a škálovatelnost. Nicméně zákazníci obvykle nemohou modelové váhy prohlížet nebo měnit a musí zkontrolovat podmínky poskytovatele pro ochranu soukromí, uchování dat, dodržování předpisů a přijatelných způsobů použití. Příklady zahrnují [OpenAI modely](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) a [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Vkládání vs. generování obrázků vs. generování textu a kódu

LLM lze také kategorizovat podle výstupu, který generují.

Vkládání (embeddingy) jsou skupiny modelů, které dokážou převést text do číselné podoby, zvané embedding, což je číselná reprezentace vstupního textu. Embeddingy usnadňují strojům porozumět vztahům mezi slovy nebo větami a mohou být používány jako vstupy do jiných modelů, jako jsou klasifikační modely nebo klastrovací modely, které mají lepší výkon na číselných datech. Embedding modely se často používají pro transfer learning, kdy je model vytvořen pro náhradní úlohu, pro kterou existuje mnoho dat, a pak se váhy modelu (embeddingy) znovu používají pro jiné úlohy. Příkladem této kategorie jsou [OpenAI embeddingy](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/cs/Embedding.c3708fe988ccf760.webp)

Modely generování obrázků jsou modely, které generují obrázky. Tyto modely se často používají pro úpravu obrázků, syntézu obrázků a převod obrázků. Jsou často trénovány na velkých datasetech obrázků, jako je [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), a mohou být použity k generování nových obrázků nebo k úpravě existujících obrázků technikami jako inpainting, super-resolution a kolorizace. Příklady zahrnují [GPT Image modely](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion modely](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) a Imagen modely.

![Generování obrázků](../../../translated_images/cs/Image.349c080266a763fd.webp)

Modely generování textu a kódu jsou modely, které generují text nebo kód. Tyto modely se často používají pro shrnutí textu, překlady a odpovědi na otázky. Textové modely jsou často trénovány na velkých datasetech textu, jako je [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), a mohou sloužit k generování nového textu nebo odpovídání na otázky. Modely generující kód, jako je [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), jsou často trénovány na velkých datasetech kódu, jako je GitHub, a mohou být použity k generování nového kódu nebo opravě chyb v existujícím kódu.

![Generování textu a kódu](../../../translated_images/cs/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus pouze Decoder

Pro objasnění různých typů architektur LLM použijme analogii.

Představte si, že váš manažer vám zadal úkol napsat kvíz pro studenty. Máte dva kolegy; jeden se stará o tvorbu obsahu a druhý o jeho kontrolu.

Tvůrce obsahu je jako model pouze s dekodérem: může se podívat na téma, vidět, co jste již napsali, a pokračovat v generování obsahu na základě tohoto kontextu. Jsou velmi dobří v psaní poutavého a informativního obsahu, ale nejsou vždy nejlepší volbou, pokud je úkolem pouze klasifikovat, vyhledávat nebo kódovat informace. Příklady rodin pouze dekodérových modelů jsou GPT a Llama.

Kontrolor je jako model pouze s enkodérem, prohlíží si napsaný kurz a odpovědi, vnímá vztahy mezi nimi a rozumí kontextu, ale nevytváří obsah. Příkladem modelu pouze s enkodérem je BERT.

Představte si, že máme někoho, kdo by mohl vytvořit i zkontrolovat kvíz, to je model Encoder-Decoder. Některé příklady jsou BART a T5.

### Služba versus Model

Nyní si povíme rozdíl mezi službou a modelem. Služba je produkt nabízený poskytovatelem cloudových služeb a často je kombinací modelů, dat a dalších komponent. Model je jádrem služby a často je to základní model, jako LLM.

Služby jsou často optimalizovány pro produkční použití a bývají snazší na použití než modely, například přes grafické uživatelské rozhraní. Služby však nejsou vždy zdarma a mohou vyžadovat předplatné nebo platbu za využití, výměnou za využití zařízení a zdrojů vlastníka služby, optimalizaci nákladů a snadné škálování. Příkladem služby je [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), která nabízí tarif pay-as-you-go, kdy jsou uživatelé účtováni úměrně k využití služby. Azure OpenAI Service také poskytuje podnikovou bezpečnost a rámec zodpovědné AI nad schopnostmi modelů.

Modely jsou artefakty neuronových sítí: parametry, váhy, architektura, tokenizér a podporující konfigurace. Provoz modelu lokálně nebo v soukromém prostředí vyžaduje vhodný hardware, infrastrukturu pro nasazení, monitorování a kompatibilní open-source/open-weight licenci nebo komerční licenci. Modely s otevřenou vahou jako Llama 4 nebo Mistral modely lze hostovat samostatně, ale stále potřebují výpočetní výkon a provozní zkušenosti.

## Jak testovat a iterovat s různými modely pro pochopení výkonu v Azure


Jakmile náš tým prozkoumal aktuální krajinu LLM a identifikoval několik dobrých kandidátů pro jejich scénáře, dalším krokem je jejich testování na jejich datech a pracovním zatížení. Je to iterativní proces, prováděný experimenty a měřeními.
Většina modelů, které jsme zmínili v předchozích odstavcích (modely OpenAI, open-weight modely jako Llama 4 a Mistral, a modely Hugging Face) je dostupná v [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), dříve Azure AI Studio/Azure AI Foundry, je jednotná platforma Azure pro vytváření AI aplikací a agentů. Pomáhá vývojářům řídit životní cyklus od experimentování a hodnocení po nasazení, monitorování a správu. Katalog modelů v Microsoft Foundry umožňuje uživateli:

- Najít ve fondu základní model zájmu, včetně modelů prodávaných Azure a modelů od partnerů a komunitních poskytovatelů. Uživatelé mohou filtrovat podle úkolu, poskytovatele, licence, možnosti nasazení nebo názvu.

![Model catalog](../../../translated_images/cs/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Prohlédnout si modelovou kartu, včetně podrobného popisu zamýšleného použití a tréninkových dat, ukázkových kódů a výsledků hodnocení v interní knihovně hodnocení.

![Model card](../../../translated_images/cs/ModelCard.598051692c6e400d.webp)

- Porovnat benchmarky napříč modely a datasetů dostupných v průmyslu, aby se vyhodnotilo, který nejlépe odpovídá obchodnímu scénáři, prostřednictvím panelu [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/cs/ModelBenchmarks.254cb20fbd06c03a.webp)

- Doladit podporované modely na vlastních tréninkových datech, aby se zlepšil výkon modelu v konkrétním pracovním zatížení, využívající schopnosti experimentování a sledování Microsoft Foundry.

![Model fine-tuning](../../../translated_images/cs/FineTuning.aac48f07142e36fd.webp)

- Nasadit původní předtrénovaný model nebo jeho doladěnou verzi na vzdálený inference endpoint v reálném čase, pomocí spravovaného výpočetního výkonu nebo serverless možností nasazení, aby aplikace mohly model využívat.

![Model deployment](../../../translated_images/cs/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Ne všechny modely v katalogu jsou v současnosti dostupné pro doladění a/nebo nasazení na platbu podle využití. Zkontrolujte modelovou kartu pro detaily o schopnostech a omezeních modelu.

## Zlepšování výsledků LLM

Náš startupový tým prozkoumal různé druhy LLM a cloudovou platformu (Microsoft Foundry), která nám umožňuje porovnat různé modely, vyhodnotit je na testovacích datech, zlepšit výkon a nasadit je na inference endpoints.

Ale kdy by měli zvážit doladění modelu namísto použití předtrénovaného? Existují jiné přístupy ke zlepšení výkonu modelu na specifickém pracovním zatížení?

Existuje několik přístupů, které může podnik použít, aby dosáhl výsledků, které od LLM potřebuje. Při nasazení LLM v produkci můžete zvolit různé typy modelů s různým stupněm tréninku, s rozdílnou složitostí, náklady a kvalitou. Zde jsou různé přístupy:

- **Prompt engineering s kontextem**. Myšlenka je poskytnout dostatek kontextu při vyvolání, aby byla zajištěna požadovaná odpověď.

- **Retrieval Augmented Generation, RAG**. Vaše data mohou existovat například v databázi nebo na webovém endpointu, aby bylo zajištěno, že tato data nebo jejich podmnožina jsou zahrnuta v době promptu, můžete načíst relevantní data a učinit je součástí uživatelova promptu.

- **Doladěný model**. Zde jste model dále trénovali na vlastních datech, což vedlo k tomu, že model je přesnější a reaguje lépe na vaše potřeby, ale může to být nákladné.

![LLMs deployment](../../../translated_images/cs/Deploy.18b2d27412ec8c02.webp)

Zdroj obrázku: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt engineering s kontextem

Předtrénované LLM fungují velmi dobře u obecných úloh přirozeného jazyka, dokonce i když je vyvoláte krátkým promptem, jako je věta k doplnění nebo otázka – tzv. „zero-shot“ učení.

Čím více uživatel dokáže rámovat svůj dotaz podrobnou žádostí a příklady – Kontext – tím přesnější a bližší očekáváním uživatele bude odpověď. V tomto případě mluvíme o „one-shot“ učení, pokud prompt zahrnuje pouze jeden příklad, a „few-shot“ učení, pokud obsahuje více příkladů.
Prompt engineering s kontextem je nejefektivnější přístup, od kterého začít.

### Retrieval Augmented Generation (RAG)

LLM mají omezení, že mohou použít pouze data, která byla použita během jejich tréninku, aby generovaly odpověď. To znamená, že neznají fakta, která se stala po jejich tréninkovém procesu, a nemají přístup k neveřejným informacím (jako jsou firemní data).
To lze překonat pomocí RAG, techniky, která doplňuje prompt o externí data ve formě částí dokumentů, s ohledem na omezení délky promptu. Toto podporují nástroje vektorových databází (jako [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), které vyhledávají užitečné fragmenty z různých předem definovaných datových zdrojů a přidávají je do Kontextu promptu.

Tato technika je velmi užitečná, když podnik nemá dostatek dat, času nebo zdrojů pro doladění LLM, ale přesto chce zlepšit výkon na specifickém pracovním zatížení a snížit riziko halucinovaných, zastaralých nebo nepodložených odpovědí.

### Doladěný model

Doladění je proces, který využívá transfer learning k „adaptaci“ modelu na následný úkol nebo k řešení specifického problému. Na rozdíl od few-shot učení a RAG vede k vytvoření nového modelu s aktualizovanými vahami a biasy. Vyžaduje sadu tréninkových příkladů složených z jediného vstupu (promptu) a jeho odpovídajícího výstupu (kompletace).
Toto je preferovaný přístup, pokud:

- **Používáte menší modely specifické pro úkol**. Podnik chce doladit menší model pro úzce vymezený úkol místo opakovaného vyvolávání většího frontier modelu, což přináší efektivnější a rychlejší řešení.

- **Zvažujete latenci**. Latence je důležitá pro specifický případ použití, takže není možné použít velmi dlouhé prompty nebo počet příkladů, ze kterých by se měl model učit, nevyhovuje limitu délky promptu.

- **Adaptujete stabilní chování**. Podnik má mnoho kvalitních příkladů a chce, aby model konzistentně následoval vzor úkolu, výstupní formát, tón nebo doménově specifický styl. Pokud je hlavním problémem čerstvá fakta nebo soukromé znalosti, které se často mění, použijte RAG místo spoléhání se výhradně na doladění.

### Trénovaný model

Trénovat LLM od začátku bezpochyby je nejtěžší a nejkomplexnější přístup, vyžadující obrovské množství dat, kvalifikované zdroje a odpovídající výpočetní výkon. Tuto možnost je vhodné zvážit pouze v případě, že má podnik doménově specifický případ použití a velké množství doménových dat.

## Kontrola znalostí

Jaký by mohl být dobrý přístup ke zlepšení výsledků dokončení u LLM?

1. Prompt engineering s kontextem
1. RAG
1. Doladěný model

A: Všechny tři mohou pomoci. Začněte s prompt engineeringem a kontextem pro rychlá zlepšení a použijte RAG, když model potřebuje aktuální fakta nebo soukromá firemní data. Zvolte doladění, pokud máte dostatek kvalitních příkladů a potřebujete, aby model konzistentně následoval úkol, formát, tón nebo doménový vzor.

## 🚀 Výzva

Přečtěte si více o tom, jak můžete [použít RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) pro vaše podnikání.

## Skvělá práce, pokračujte ve vzdělávání

Po dokončení této lekce si prohlédněte naši [kolekci pro učení Generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali v rozšiřování svých znalostí o Generativní AI!

Přesuňte se do Lekce 3, kde se podíváme na to, jak [stavět s Generativní AI zodpovědně](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->