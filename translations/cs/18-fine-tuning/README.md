[![Open Source Models](../../../translated_images/cs/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Doladění vašeho LLM

Používání rozsáhlých jazykových modelů k vytváření generativních aplikací umělé inteligence přináší nové výzvy. Klíčovým problémem je zajistit kvalitu odpovědí (přesnost a relevantnost) v obsahu generovaném modelem pro daný uživatelský požadavek. V předchozích lekcích jsme diskutovali techniky jako prompt engineering a retrieval-augmented generation, které se snaží problém vyřešit _úpravou vstupního promptu_ pro existující model.

V dnešní lekci budeme hovořit o třetí technice, **doladění (fine-tuning)**, která se snaží výzvu vyřešit _přeškolením samotného modelu_ pomocí dodatečných dat. Pojďme se ponořit do detailů.

## Výukové cíle

Tato lekce představuje koncept doladění předtrénovaných jazykových modelů, prozkoumává výhody a výzvy tohoto přístupu a poskytuje návod, kdy a jak doladění použít k zlepšení výkonu vašich generativních AI modelů.

Na konci této lekce byste měli být schopni odpovědět na následující otázky:

- Co je doladění jazykových modelů?
- Kdy a proč je doladění užitečné?
- Jak mohu doladit předtrénovaný model?
- Jaká jsou omezení doladění?

Připraveni? Pojďme začít.

## Ilustrovaný průvodce

Chcete získat přehled o tom, co budeme probírat dříve, než se do toho pustíme? Podívejte se na tento ilustrovaný průvodce, který popisuje učební cestu této lekce - od poznání základních konceptů a motivace pro doladění až po pochopení procesu a nejlepších praktik realizace úlohy doladění. Je to fascinující téma k prozkoumání, tak nezapomeňte navštívit stránku [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pro další odkazy, které podpoří vaše samostatné učení!

![Ilustrovaný průvodce doladěním jazykových modelů](../../../translated_images/cs/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Co je doladění jazykových modelů?

Velké jazykové modely jsou dle definice _předtrénované_ na velkém množství textu získaného z různorodých zdrojů včetně internetu. Jak jsme se naučili v předchozích lekcích, k zlepšení kvality odpovědí modelu na uživatelské otázky („prompty“) potřebujeme techniky jako _prompt engineering_ a _retrieval-augmented generation_.

Oblíbená technika prompt engineeringu zahrnuje poskytnutí modelu více pokynů, co se očekává v odpovědi, buď _poskytnutím instrukcí_ (explicitní vedení) nebo _ukázáním několika příkladů_ (implicitní vedení). Toto se nazývá _few-shot learning_, ale má dvě omezení:

- Limity tokenů modelu mohou omezit počet příkladů, které můžete dodat, a omezit účinnost.
- Náklady na tokeny modelu mohou ztížit přidávání příkladů ke každému promptu a omezit flexibilitu.

Doladění je běžná praxe v systémech strojového učení, kde vezmeme předtrénovaný model a přeškolíme jej na nových datech, aby se zlepšil jeho výkon na konkrétním úkolu. V kontextu jazykových modelů můžeme doladit předtrénovaný model _vybranou sadou příkladů pro daný úkol nebo aplikační doménu_, abychom vytvořili **vlastní model**, který může být přesnější a relevantnější pro konkrétní úkol nebo doménu. Vedlejší výhodou doladění je také to, že může snížit počet příkladů potřebných pro few-shot learning - čímž se snižuje využití tokenů a související náklady.

## Kdy a proč bychom měli modely doladit?

V _tomto_ kontextu, když hovoříme o doladění, myslíme tím **řízené** doladění, kde se přeškolení provádí **přidáním nových dat**, která nebyla součástí původní tréninkové sady. To se liší od neřízeného doladění, kde je model přeškolen na původních datech, ale s odlišnými hyperparametry.

Klíčovou věcí, kterou je třeba si pamatovat, je, že doladění je pokročilá technika vyžadující určitou úroveň odbornosti k dosažení požadovaných výsledků. Pokud je provedena nesprávně, nemusí přinést očekávaná zlepšení a může dokonce zhoršit výkon modelu pro cílovou doménu.

Proto než se naučíte „jak“ doladit jazykové modely, musíte vědět „proč“ byste měli jít touto cestou a „kdy“ začít proces doladění. Začněte tím, že si položíte tyto otázky:

- **Případ použití:** Jaký je váš _případ použití_ pro doladění? Který aspekt současného předtrénovaného modelu chcete zlepšit?
- **Alternativy:** Zkoušeli jste _jiné techniky_ k dosažení požadovaných výsledků? Použijte je k vytvoření základny pro srovnání.
  - Prompt engineering: Vyzkoušejte techniky jako few-shot prompting s příklady relevantních odpovědí na prompt. Zhodnoťte kvalitu odpovědí.
  - Retrieval Augmented Generation: Zkuste doplnit prompty výsledky dotazů získanými vyhledáváním ve vašich datech. Zhodnoťte kvalitu odpovědí.
- **Náklady:** Identifikovali jste náklady na doladění?
  - Možnost doladění - je předtrénovaný model k doladění dostupný?
  - Úsilí - příprava tréninkových dat, vyhodnocování a zdokonalování modelu.
  - Výpočetní zdroje - pro běh úloh doladění a nasazení doladěného modelu.
  - Data - přístup k dostatečně kvalitním příkladům pro význam doladění.
- **Přínosy:** Potvrdili jste přínosy doladění?
  - Kvalita - překonal doladěný model základní model?
  - Náklady - snižuje použití tokenů zjednodušením promptů?
  - Rozšiřitelnost - můžete základní model znovu použít pro nové domény?

Na základě odpovědí na tyto otázky byste měli být schopni rozhodnout, zda je doladění správný přístup pro váš případ použití. Ideálně je tento přístup platný jen pokud přínosy převyšují náklady. Jakmile se rozhodnete pokračovat, je čas přemýšlet o _jak_ můžete doladit předtrénovaný model.

Chcete získat více informací o rozhodovacím procesu? Sledujte [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Jak můžeme doladit předtrénovaný model?

K doladění předtrénovaného modelu potřebujete:

- předtrénovaný model k doladění
- dataset pro doladění
- tréninkové prostředí pro spuštění úlohy doladění
- prostředí pro nasazení doladěného modelu

## Doladění v praxi

> **Poznámka:** `gpt-35-turbo` / `gpt-3.5-turbo`, zmíněné v některých tutoriálech níže, jsou vyřazeny jak pro inferenci, tak pro doladění. Pokud dnes začínáte novou úlohu doladění, cílem by měl být aktuálně podporovaný model - například `gpt-4o-mini` nebo `gpt-4.1-mini`. Podívejte se na [Seznam doladitelných modelů](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) pro aktuální sadu doladitelných modelů. Koncepty a kroky v těchto tutoriálech stále platí.

Následující zdroje poskytují krok za krokem tutoriály, které vás provedou skutečným příkladem použití vybraného modelu s vybranou sadou dat. Abyste mohli tutoriály absolvovat, potřebujete účet u konkrétního poskytovatele spolu s přístupem k relevantnímu modelu a datasetům.

| Poskytovatel | Tutoriál                                                                                                                                                                       | Popis                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Jak doladit chatovací modely](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Naučte se doladit `gpt-35-turbo` pro konkrétní doménu („asistent na recepty“) přípravou tréninkových dat, spuštěním úlohy doladění a využitím doladěného modelu pro inferenci.                                                                                                                                                                                                                                                     |
| Azure OpenAI | [Tutoriál k doladění GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Naučte se doladit model `gpt-35-turbo-0613` **na Azure** vytvořením a nahráním tréninkových dat, spuštěním úlohy doladění. Nasazení a použití nového modelu.                                                                                                                                                                                                                                                                        |
| Hugging Face | [Doladění LLM s Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                                      | Tento blogový příspěvek vás provede doladěním _otevřeného LLM_ (například `CodeLlama 7B`) za použití knihovny [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) a [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) pomocí otevřených [datových sad](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 🤗 AutoTrain | [Doladění LLM s AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                               | AutoTrain (nebo AutoTrain Advanced) je python knihovna vyvinutá Hugging Face, která umožňuje doladění pro mnohé různé úkoly včetně doladění LLM. AutoTrain je řešení bez nutnosti kódování a doladění lze provést ve vlastním cloudu, na Hugging Face Spaces nebo lokálně. Podporuje webové GUI, CLI i trénink prostřednictvím yaml konfiguračních souborů.                                                                                   |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 🦥 Unsloth  | [Doladění LLM s Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                                                 | Unsloth je open-source framework podporující doladění LLM a posilované učení (RL). Unsloth zjednodušuje lokální trénink, vyhodnocování a nasazení s připravenými [notebooky](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Podporuje také text-to-speech (TTS), BERT a multimodální modely. K začátku si přečtěte jejich krok-za-krokem [Průvodce doladěním LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                           |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
## Zadání

Vyberte si jeden z výše uvedených tutoriálů a projděte si jej. _Můžeme vytvořit verzi těchto tutoriálů v Jupyter Notebooks v tomto repozitáři pouze pro referenci. Pro nejnovější verze ale prosím používejte přímo původní zdroje._

## Skvělá práce! Pokračujte ve svém učení.

Po dokončení této lekce navštivte naši [kolekci pro učení Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte v rozšiřování svých znalostí o Generative AI!

Gratulujeme!! Dokončili jste závěrečnou lekci z verze v2 tohoto kurzu! Nepřestávejte se učit a tvořit. \*\*Navštivte stránku [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pro seznam dalších doporučení právě na toto téma.

Naše série lekcí verze v1 byla také aktualizována o více zadání a konceptů. Tak si na chvíli osvěžte své znalosti – a prosím [sdílejte své otázky a zpětnou vazbu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), aby nám pomohly vylepšit tyto lekce pro komunitu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->