[![Open Source Models](../../../translated_images/cs/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Jemné doladění vašeho LLM

Používání velkých jazykových modelů pro vytváření generativních aplikací AI přináší nové výzvy. Klíčovým problémem je zajištění kvality odpovědí (přesnost a relevance) v obsahu generovaném modelem pro daný uživatelský požadavek. V předchozích lekcích jsme diskutovali techniky jako inženýrství promptu a generování s doplněním vyhledáváním, které se snaží problém řešit _modifikací vstupního promptu_ do existujícího modelu.

V dnešní lekci si představíme třetí techniku, **jemné doladění**, která se snaží tento problém řešit _znovuvytrénováním samotného modelu_ s dalšími daty. Pojďme se podívat na podrobnosti.

## Výukové cíle

Tato lekce představí koncept jemného doladění předtrénovaných jazykových modelů, prozkoumá přínosy a výzvy tohoto přístupu a poskytne doporučení, kdy a jak jemné doladění použít ke zlepšení výkonu vašich generativních AI modelů.

Na konci této lekce byste měli být schopni odpovědět na následující otázky:

- Co je to jemné doladění jazykových modelů?
- Kdy a proč je jemné doladění užitečné?
- Jak mohu jemně doladit předtrénovaný model?
- Jaká jsou omezení jemného doladění?

Jste připraveni? Pojďme začít.

## Ilustrovaný průvodce

Chcete získat celkový přehled o tom, co pokryjeme, než se do toho pustíme? Podívejte se na tento ilustrovaný průvodce, který popisuje vzdělávací cestu pro tuto lekci – od naučení si základních konceptů a motivace pro jemné doladění až po pochopení procesu a osvědčených postupů pro realizaci úkolu jemného doladění. Toto je fascinující téma k prozkoumání, tak nezapomeňte navštívit stránku [Zdroje](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pro další odkazy, které podpoří vaši samostatnou studijní cestu!

![Ilustrovaný průvodce jemným doladěním jazykových modelů](../../../translated_images/cs/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Co je jemné doladění jazykových modelů?

Velké jazykové modely jsou dle definice _předtrénované_ na velkém množství textu pocházejícím z rozmanitých zdrojů včetně internetu. Jak jsme se naučili v předchozích lekcích, potřebujeme techniky jako _inženýrství promptu_ a _generování s doplněním vyhledáváním_, abychom zlepšili kvalitu odpovědí modelu na otázky uživatele („prompty“).

Oblíbenou technikou inženýrství promptu je poskytnout modelu více vedení ohledně toho, co se očekává v odpovědi, buď prostřednictvím _instrukcí_ (explicitní vedení), nebo _dáním několika příkladů_ (implicitní vedení). Tomu se říká _few-shot learning_, ale má to dvě omezení:

- Limity počtu tokenů modelu mohou omezit počet příkladů, které můžete dát, a tím i účinnost.
- Náklady na tokeny mohou být vysoké, pokud přidáváte příklady do každého promptu, což omezuje flexibilitu.

Jemné doladění je běžná praktika v systémech strojového učení, kde vezmeme předtrénovaný model a znovu jej natrénujeme s novými daty, abychom zlepšili jeho výkon na konkrétním úkolu. V kontextu jazykových modelů můžeme předtrénovaný model jemně doladit _pomocí vybraných příkladů pro daný úkol nebo aplikační doménu_ a vytvořit tak **vlastní model**, který může být přesnější a relevantnější pro tento specifický úkol nebo oblast. Vedlejším přínosem jemného doladění je, že může také snížit počet příkladů potřebných pro few-shot learning – což snižuje využití tokenů a související náklady.

## Kdy a proč bychom měli jemně doladit modely?

V _tomto_ kontextu, když mluvíme o jemném doladění, máme na mysli **supervidované** jemné doladění, kde se znovuvytrénování provádí **přidáním nových dat**, která nebyla součástí původního tréninkového datasetu. To se liší od nesupervidovaného jemného doladění, kdy se model trénuje znovu na původních datech, ale s odlišnými hyperparametry.

Klíčové je si pamatovat, že jemné doladění je pokročilá technika vyžadující určitou úroveň odbornosti, aby přinesla požadované výsledky. Pokud je provedeno nesprávně, nemusí přinést očekávaná zlepšení a může dokonce zhoršit výkon modelu pro vaši cílovou oblast.

Než se tedy naučíte „jak“ jemně doladit jazykové modely, musíte vědět „proč“ byste tuto cestu měli zvolit a „kdy“ zahájit proces jemného doladění. Začněte tím, že si položíte tyto otázky:

- **Případ použití:** Jaký je váš _případ použití_ pro jemné doladění? Který aspekt současného předtrénovaného modelu chcete zlepšit?
- **Alternativy:** Zkoušeli jste _jiné techniky_ k dosažení požadovaných výsledků? Použijte je jako základ pro srovnání.
  - Inženýrství promptu: Vyzkoušejte techniky jako few-shot prompting s příklady relevantních odpovědí. Zhodnoťte kvalitu odpovědí.
  - Generování s doplněním vyhledáváním: Vyzkoušejte doplňování promptů výsledky z vyhledávání ve vašich datech. Zhodnoťte kvalitu odpovědí.
- **Náklady:** Identifikovali jste náklady na jemné doladění?
  - Možnost doladění - je předtrénovaný model dostupný pro jemné doladění?
  - Úsilí - příprava tréninkových dat, vyhodnocení a zpřesnění modelu.
  - Výpočetní výkon - pro běžecké úlohy jemného doladění a nasazení doladěného modelu.
  - Data - přístup k dostatečně kvalitním příkladům pro dopad jemného doladění.
- **Přínosy:** Potvrdili jste přínosy jemného doladění?
  - Kvalita - překonal doladěný model základní model?
  - Náklady - snižuje použití tokenů zjednodušením promptů?
  - Rozšiřitelnost - lze základní model využít pro nové domény?

Odpovědí na tyto otázky byste měli být schopni rozhodnout, zda je jemné doladění správný přístup pro váš případ použití. Ideálně je přístup platný jen tehdy, pokud přínosy převažují nad náklady. Jakmile se rozhodnete pokračovat, je čas přemýšlet o _jak_ jemně doladit předtrénovaný model.

Chcete získat více informací o rozhodovacím procesu? Sledujte [Doladit, nebo nedoladit](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Jak můžeme jemně doladit předtrénovaný model?

K jemnému doladění předtrénovaného modelu potřebujete:

- předtrénovaný model k doladění
- dataset pro jemné doladění
- tréninkové prostředí pro spuštění úlohy jemného doladění
- hostingové prostředí pro nasazení doladěného modelu

## Jemné doladění na Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) je místo, kde dnes jemně doladíte, nasadíte a spravujete vlastní modely na Azure (spojuje to, co dříve bylo Azure OpenAI Studio a Azure AI Studio). Než spustíte úlohu, je užitečné pochopit možnosti, které vám Foundry nabízí, a osvědčené postupy doporučované platformou. Pod kapotou Foundry používá **LoRA (low-rank adaptation)** k efektivnímu jemnému doladění modelů, což udržuje trénink rychlejší a cenově dostupnější než přeškolování každé váhy.

### Krok 1: Vyberte metodu tréninku

Foundry podporuje tři techniky jemného doladění. **Začněte se SFT** - pokrývá nejširší spektrum scénářů.

| Technika | Co dělá | Kdy ji použít |
| --- | --- | --- |
| **Supervidované jemné doladění (SFT)** | Trénuje na párech vstup/výstup, aby se model naučil produkovat požadované odpovědi. | Výchozí volba pro většinu úkolů: specializace domény, výkon úkolu, styl a tón, dodržování instrukcí a adaptace jazyka. |
| **Přímá optimalizace preferencí (DPO)** | Učí se z párů preferovaných vs. nepreferovaných odpovědí pro sladění výstupů s lidskými preferencemi. | Zlepšení kvality odpovědí, bezpečnosti a souladu, pokud máte srovnávací zpětnou vazbu. |
| **Reinforcement Fine-Tuning (RFT)** | Používá odměnovací signály od _hodnotitelů_ k optimalizaci komplexního chování pomocí posilovaného učení. | Objektivní, na uvažování náročné domény (matematika, chemie, fyzika) s jasnými správnými/nesprávnými odpověďmi. Vyžaduje více znalostí ML. |

### Krok 2: Vyberte úroveň tréninku

Foundry vám umožňuje vybrat, jak a kde trénink poběží:

- **Standardní** - trénink ve vaší oblasti zdrojů a zaručuje rezidenci dat. Použijte, když musí data zůstat v konkrétní oblasti.
- **Globální** - levnější a rychlejší fronta použitím kapacity mimo vaši oblast (data a váhy jsou zkopírovány do oblasti tréninku). Dobrá výchozí volba, pokud není vyžadována rezidence dat.
- **Vývojářská** - nejnižší náklady, využívá nevyužitou kapacitu bez záruk latence/SLA (úlohy mohou být přerušeny a obnoveny). Ideální pro experimentování.

### Krok 3: Vyberte základní model

Modely vhodné pro jemné doladění zahrnují OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` a `gpt-4.1-nano` (SFT; rodina 4o/4.1 podporuje také DPO), modely pro odvozování `o4-mini` a `gpt-5` (RFT), plus open-source modely jako `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` a `gpt-oss-20b` (SFT na Foundry zdrojích). Vždy si zkontrolujte aktuální [Seznam modelů pro jemné doladění](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) pro podporované metody, regiony a dostupnost.

> Foundry nabízí dva režimy: **serverless** (platba podle spotřeby, bez správy kvóty GPU, OpenAI a vybrané modely) a **managed compute** (přinesete vlastní VMs přes Azure Machine Learning pro nejširší řadu modelů). Většina by měla začít se serverless.

### Osvědčené postupy Foundry

- **Nejprve základní měření.** Změřte základní model pomocí inženýrství promptu a RAG _před_ jemným doladěním, abyste mohli prokázat zlepšení.
- **Začněte s malým množstvím, pak škálujte.** Začněte s 50-100 kvalitními příklady pro ověření přístupu, poté rozšiřte na 500+ pro produkci. Kvalita je důležitější než množství – odstraňujte nízkokvalitní příklady.
- **Formátujte data správně.** Tréninkové a validační soubory musí být JSONL, UTF-8 **s BOM**, menší než 512 MB, používající formát zpráv chat-completions. Vždy zahrňte validační soubor, abyste mohli sledovat přeučení.
- **Použijte při inferenci stejný systémový prompt jako při tréninku.**
- **Vyhodnoťte kontrolní body – ne nasazujte slepě ten poslední.** Foundry uchovává poslední tři epochy jako nasaditelné kontrolní body; vyberte ten, který nejlépe generalizuje podle `train_loss` / `valid_loss` a přesnosti tokenů.
- **Měřte náklady na tokeny spolu s kvalitou** při porovnávání doladěného modelu se základem.
- **Iterujte s průběžným jemným doladěním.** Můžete doladit již doladěný model na nových datech (podporováno pro OpenAI modely).
- **Dávejte pozor na náklady na hosting.** Nasazený vlastní model se účtuje na hodiny a neaktivní nasazení se po 15 dnech odstraní – odstraňte, co nepotřebujete.

Projděte kompletním návodem v [Přizpůsobení modelu jemným doladěním](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) a podívejte se na návody pro [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) a [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst), když budete připraveni vyzkoušet jiné techniky.

## Jemné doladění v praxi

Následující zdroje poskytují krok za krokem tutoriály, které vás provedou reálnými příklady na aktuálně podporovaném modelu s vybraným datasetem. Pro jejich použití potřebujete účet u příslušného poskytovatele spolu s přístupem k relevantnímu modelu a datasetům.

| Poskytovatel     | Tutoriál                                                                                                                                                                       | Popis                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Jak jemně doladit chatovací modely](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Naučte se jemně doladit nedávný chatovací model OpenAI pro specifickou doménu („asistent receptů“) přípravou tréninkových dat, spuštěním úlohy jemného doladění a používáním doladěného modelu pro inferenci.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Přizpůsobení modelu jemným doladěním](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Naučte se jemně doladit aktuálně podporovaný model jako `gpt-4.1-mini` **na Azure** s Microsoft Foundry: připravte a nahrajte tréninková a validační data, spusťte úlohu jemného doladění a poté nasadťe a používejte nový model.                                                                                                                                                                                                                                           |

| Hugging Face | [Doladění LLM s Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Tento blogový příspěvek vás provede doladěním _otevřeného LLM_ (např. `CodeLlama 7B`) pomocí knihovny [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) a [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) s otevřenými [datovými sadami](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Doladění LLM s AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (nebo AutoTrain Advanced) je python knihovna vyvinutá Hugging Face, která umožňuje doladění pro mnoho různých úkolů včetně doladění LLM. AutoTrain je řešení bez potřeby kódování a doladění lze provést ve vašem vlastním cloudu, na Hugging Face Spaces nebo lokálně. Podporuje webové GUI, CLI i trénink pomocí yaml konfiguračních souborů.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Doladění LLM s Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth je open-source rámec, který podporuje doladění LLM a posilované učení (RL). Unsloth zjednodušuje lokální trénink, vyhodnocování a nasazení s připravenými [notebooky](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Podporuje také převod textu na řeč (TTS), BERT a multimodální modely. Pro začátek si přečtěte jejich detailního průvodce [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Zadání

Vyberte si jeden z výše uvedených tutoriálů a projděte si ho. _Můžeme replikovat verzi těchto tutoriálů v Jupyter Noteboocích v tomto repozitáři pouze pro referenci. Pro nejaktuálnější verze prosím používejte přímo originální zdroje_.

## Skvělá práce! Pokračujte ve studiu.

Po dokončení této lekce si prohlédněte naši [sbírku o Generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste dále rozšiřovali své znalosti v oblasti Generativní AI!

Gratulujeme!! Dokončili jste poslední lekci ze série v2 tohoto kurzu! Nepřestávejte se učit a tvořit. \*\*Podívejte se na stránku [ZDROJE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pro seznam dalších doporučení právě k tomuto tématu.

Naše série lekcí v1 byla také aktualizována o další zadání a koncepty. Věnujte tedy chvilku obnovení svých znalostí – a prosím [sdílejte své otázky a zpětnou vazbu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), aby nám pomohly lekce zlepšit pro komunitu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->