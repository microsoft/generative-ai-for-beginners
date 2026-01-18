<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T18:56:15+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "cs"
}
-->
[![Open Source Models](../../../../../translated_images/cs/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Doladění vašeho LLM

Používání velkých jazykových modelů pro tvorbu generativních AI aplikací přináší nové výzvy. Klíčovým problémem je zajistit kvalitu odpovědí (přesnost a relevanci) v obsahu generovaném modelem pro daný uživatelský požadavek. V předchozích lekcích jsme diskutovali techniky jako prompt engineering a generování s podporou vyhledávání, které se snaží problém vyřešit _úpravou vstupu promptu_ do existujícího modelu.

V dnešní lekci se budeme věnovat třetí technice, **doladění (fine-tuning)**, která se snaží výzvu řešit _přeškolením samotného modelu_ s použitím dalších dat. Pojďme se ponořit do detailů.

## Výukové cíle

Tato lekce představuje koncept doladění předtrénovaných jazykových modelů, prozkoumá výhody a výzvy tohoto přístupu a poskytuje doporučení, kdy a jak doladění použít ke zlepšení výkonu vašich generativních AI modelů.

Na konci lekce byste měli umět odpovědět na následující otázky:

- Co je doladění jazykových modelů?
- Kdy a proč je doladění užitečné?
- Jak mohu doladit předtrénovaný model?
- Jaká jsou omezení doladění?

Jste připraveni? Pojďme začít.

## Ilustrovaný průvodce

Chcete získat přehled o tom, co budeme probírat, ještě předtím, než se pustíme do podrobností? Podívejte se na tento ilustrovaný průvodce, který popisuje vzdělávací cestu této lekce – od seznámení s klíčovými koncepty a motivací pro doladění až po pochopení procesu a nejlepších postupů pro provedení doladění. Je to fascinující téma k prozkoumání, tak nezapomeňte navštívit stránku [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pro další odkazy na podporu vašeho samostatného vzdělávání!

![Ilustrovaný průvodce doladěním jazykových modelů](../../../../../translated_images/cs/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Co je doladění jazykových modelů?

Podle definice jsou velké jazykové modely _předtrénované_ na rozsáhlých množstvích textu získaných z různých zdrojů včetně internetu. Jak jsme se naučili v předchozích lekcích, potřebujeme techniky jako _prompt engineering_ a _generování s podporou vyhledávání_, abychom zlepšili kvalitu odpovědí modelu na uživatelské dotazy („prompty“).

Oblíbená technika prompt engineeringu zahrnuje poskytnutí modelu více pokynů, co se očekává v odpovědi, buď poskytnutím _instrukcí_ (explicitní vedení), nebo _několika příklady_ (implicitní vedení). To se nazývá _few-shot learning_, ale má dvě omezení:

- Limity tokenů modelu mohou omezit počet příkladů, které můžete uvést, a omezit efektivitu.
- Náklady na tokeny modelu mohou být vysoké, pokud přidáváte příklady do každého promptu, což omezuje flexibilitu.

Doladění je běžná praxe v systémech strojového učení, kde vezmeme předtrénovaný model a přeškolíme ho s novými daty, abychom zlepšili jeho výkon na určitém úkolu. V kontextu jazykových modelů můžeme doladit předtrénovaný model _na pečlivě vybrané sadě příkladů pro daný úkol nebo aplikační doménu_, abychom vytvořili **vlastní model**, který může být přesnější a relevantnější pro tento konkrétní úkol nebo doménu. Vedlejším přínosem doladění je, že může také snížit počet příkladů potřebných pro few-shot learning – tím se sníží využití tokenů a související náklady.

## Kdy a proč bychom měli doladit modely?

V _tomto_ kontextu, když mluvíme o doladění, odkazujeme na **řízené (supervised)** doladění, kde se přeškolení provádí **přidáním nových dat**, která nebyla součástí původní trénovací sady. To je odlišné od neřízeného doladění, kde je model přeškolen na původních datech, ale s jinými hyperparametry.

Klíčové je si uvědomit, že doladění je pokročilá technika, která vyžaduje určitou úroveň odbornosti k dosažení očekávaných výsledků. Pokud je provedena nesprávně, nemusí přinést očekávaná zlepšení a může dokonce zhoršit výkon modelu pro vaše cílové doméně.

Proto než se naučíte "jak" doladit jazykové modely, musíte vědět "proč" byste měli touto cestou jít a "kdy" začít s procesem doladění. Začněte tím, že si položíte tyto otázky:

- **Případ použití**: Jaký je váš _případ použití_ pro doladění? Jaký aspekt současného předtrénovaného modelu chcete zlepšit?
- **Alternativy**: Zkoušeli jste _jiné techniky_ k dosažení požadovaných výsledků? Použijte je k vytvoření základny pro porovnání.
  - Prompt engineering: Vyzkoušejte techniky jako few-shot prompting s příklady relevantních odpovědí. Zhodnoťte kvalitu odpovědí.
  - Generování s podporou vyhledávání: Vyzkoušejte rozšíření promptů o výsledky vyhledávané ve vašich datech. Zhodnoťte kvalitu odpovědí.
- **Náklady**: Identifikovali jste náklady doladění?
  - Schopnost ladění - je předtrénovaný model dostupný pro doladění?
  - Úsilí - příprava trénovacích dat, vyhodnocování a zdokonalování modelu.
  - Výpočetní náročnost - pro běh doladění a nasazení doladěného modelu.
  - Data - přístup k dostatečné kvalitě příkladů, které ovlivní doladění.
- **Přínosy**: Potvrdili jste přínosy doladění?
  - Kvalita - překonal doladěný model základní úroveň?
  - Náklady - snižuje použití tokenů zjednodušením promptů?
  - Rozšiřitelnost - lze základní model použít i pro nové domény?

Odpověďmi na tyto otázky byste měli být schopni rozhodnout, jestli je doladění správný přístup pro váš případ použití. Ideálně je tento přístup platný pouze tehdy, pokud přínosy převáží náklady. Jakmile se rozhodnete pokračovat, je čas přemýšlet o tom, _jak_ doladit předtrénovaný model.

Chcete získat více informací o rozhodovacím procesu? Podívejte se na [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Jak můžeme doladit předtrénovaný model?

K doladění předtrénovaného modelu potřebujete:

- předtrénovaný model k doladění
- datovou sadu k použití pro doladění
- trénovací prostředí pro spuštění doladění
- hostingové prostředí pro nasazení doladěného modelu

## Doladění v praxi

Následující zdroje poskytují podrobné návody krok za krokem, které vás provedou skutečným příkladem použití vybraného modelu s pečlivě vybranou datovou sadou. Pro práci s těmito návody potřebujete účet u konkrétního poskytovatele, spolu s přístupem k relevantnímu modelu a datovým sadám.

| Poskytovatel | Návod                                                                                                                                                                       | Popis                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Jak doladit chatovací modely](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Naučte se doladit `gpt-35-turbo` pro konkrétní doménu („asistent receptů“) přípravou tréninkových dat, spuštěním doladění a použitím doladěného modelu pro inference.                                                                                                                                                                                                                                                           |
| Azure OpenAI | [Návod na doladění GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst)      | Naučte se doladit model `gpt-35-turbo-0613` **na Azure** tím, že vytvoříte a nahrajete tréninková data, spustíte doladění, nasadíte a použijete nový model.                                                                                                                                                                                                                                                                        |
| Hugging Face | [Doladění LLM s Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                                     | Tento blogový příspěvek vás provede doladěním _otevřeného LLM_ (např. `CodeLlama 7B`) pomocí knihovny [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) s otevřenými [datasetů](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 🤗 AutoTrain | [Doladění LLM s AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                                 | AutoTrain (nebo AutoTrain Advanced) je pythonová knihovna vyvinutá Hugging Face, která umožňuje doladění pro různé úkoly včetně doladění LLM. AutoTrain je řešení bez kódu a doladění lze provádět ve vašem vlastním cloudu, na Hugging Face Spaces nebo lokálně. Podporuje webové GUI, CLI a trénování přes yaml konfigurační soubory.                                                                                                            |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 🦥 Unsloth   | [Doladění LLM s Unsloth](https://github.com/unslothai/unsloth)                                                                                                                | Unsloth je open-source framework, který podporuje doladění LLM a posilovací učení (RL). Unsloth usnadňuje lokální trénování, hodnocení a nasazení s ready-to-use [notebooky](https://github.com/unslothai/notebooks). Podporuje také text-to-speech (TTS), BERT a multimodální modely. Chcete-li začít, přečtěte si jejich krok za krokem [Průvodce doladěním LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                            |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
## Zadání

Vyberte si jeden z výše uvedených návodů a projděte si jej. _Můžeme v tomto repozitáři případně replikovat verzi těchto návodů jako Jupyter Notebooky pouze pro referenci. Pro aktuální verze prosím používejte přímo originální zdroje_.

## Skvělá práce! Pokračujte ve svém vzdělávání.

Po dokončení této lekce navštivte naši [kolekci Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali v rozvíjení svých znalostí generativní AI!

Gratulujeme!! Dokončili jste závěrečnou lekci z řady v2 tohoto kurzu! Nepřestávejte se učit a tvořit. \*\*Podívejte se na stránku [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pro seznam dalších doporučení přímo k tomuto tématu.

Naše řada lekcí v1 byla také aktualizována o další zadání a koncepty. Tak si na chvíli osvěžte své znalosti – a prosím [sdílejte své otázky a zpětnou vazbu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), abychom mohli tyto lekce pro komunitu vylepšit.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->