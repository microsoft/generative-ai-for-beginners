<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:09:28+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "cs"
}
-->
# Frameworky pro neuronové sítě

Jak jsme se již naučili, abychom mohli efektivně trénovat neuronové sítě, musíme udělat dvě věci:

* Operovat s tensory, např. násobit, sčítat a počítat některé funkce jako sigmoid nebo softmax
* Vypočítat gradienty všech výrazů, abychom mohli provádět optimalizaci pomocí gradientního sestupu

Zatímco knihovna `numpy` zvládne první část, potřebujeme nějaký mechanismus pro výpočet gradientů. V našem frameworku, který jsme vyvinuli v předchozí sekci, jsme museli ručně programovat všechny derivace funkcí uvnitř metody `backward`, která provádí zpětnou propagaci. Ideálně by nám framework měl poskytnout možnost vypočítat gradienty *jakéhokoliv výrazu*, který můžeme definovat.

Další důležitou věcí je schopnost provádět výpočty na GPU nebo jiných specializovaných výpočetních jednotkách, jako je TPU. Trénink hlubokých neuronových sítí vyžaduje *mnoho* výpočtů a možnost paralelizace těchto výpočtů na GPU je velmi důležitá.

> ✅ Termín 'paralelizovat' znamená rozdělit výpočty mezi více zařízení.

V současné době jsou dvě nejpopulárnější frameworky pro neuronové sítě: TensorFlow a PyTorch. Oba poskytují nízkoúrovňové API pro operace s tensory na CPU i GPU. Nad nízkoúrovňovým API existuje také vyšší úrovňové API, které se odpovídajícím způsobem nazývá Keras a PyTorch Lightning.

Nízkoúrovňové API | TensorFlow | PyTorch
-----------------|-------------------------------------|--------------------------------
Vyšší úrovňové API | Keras | PyTorch Lightning

**Nízkoúrovňová API** v obou frameworkech vám umožňují vytvářet tzv. **výpočetní grafy**. Tento graf definuje, jak vypočítat výstup (obvykle ztrátovou funkci) s danými vstupními parametry a může být poslán k výpočtu na GPU, pokud je k dispozici. Existují funkce pro diferenciaci tohoto výpočetního grafu a výpočet gradientů, které pak mohou být použity k optimalizaci parametrů modelu.

**Vyšší úrovňová API** považují neuronové sítě v podstatě za **sekvenci vrstev** a konstrukce většiny neuronových sítí je tak mnohem jednodušší. Trénování modelu obvykle vyžaduje přípravu dat a poté zavolání funkce `fit` pro provedení úkolu.

Vyšší úrovňové API vám umožní velmi rychle vytvořit typické neuronové sítě bez starostí o mnoho detailů. Zároveň nízkoúrovňové API nabízí mnohem větší kontrolu nad tréninkovým procesem, a proto jsou často používána ve výzkumu, když se zabýváte novými architekturami neuronových sítí.

Je také důležité pochopit, že můžete použít obě API dohromady, např. můžete vyvinout svou vlastní architekturu vrstvy s použitím nízkoúrovňového API a pak ji použít v rámci větší sítě vytvořené a trénované s vyšší úrovňovým API. Nebo můžete definovat síť pomocí vyšší úrovňového API jako sekvenci vrstev a pak použít vlastní nízkoúrovňovou tréninkovou smyčku k provedení optimalizace. Obě API používají stejné základní koncepty a jsou navržena tak, aby dobře spolupracovala.

## Učení

V tomto kurzu nabízíme většinu obsahu jak pro PyTorch, tak pro TensorFlow. Můžete si vybrat preferovaný framework a projít pouze odpovídajícími zápisníky. Pokud si nejste jisti, který framework zvolit, přečtěte si nějaké diskuse na internetu ohledně **PyTorch vs. TensorFlow**. Můžete se také podívat na oba frameworky pro lepší pochopení.

Kde to bude možné, použijeme vyšší úrovňová API pro jednoduchost. Nicméně věříme, že je důležité pochopit, jak neuronové sítě fungují od základu, takže na začátku začneme pracovat s nízkoúrovňovým API a tensory. Nicméně pokud chcete rychle začít a nechcete trávit mnoho času učením těchto detailů, můžete tyto části přeskočit a jít rovnou do zápisníků s vyšší úrovňovým API.

## ✍️ Cvičení: Frameworky

Pokračujte ve svém učení v následujících zápisnících:

Nízkoúrovňové API | TensorFlow+Keras Zápisník | PyTorch
-----------------|-------------------------------------|--------------------------------
Vyšší úrovňové API | Keras | *PyTorch Lightning*

Po zvládnutí frameworků si zopakujme pojem přetrénování.

# Přetrénování

Přetrénování je velmi důležitý koncept v oblasti strojového učení a je velmi důležité ho správně pochopit!

Zvažte následující problém aproximace 5 bodů (reprezentovaných `x` na grafech níže):

!lineární | přetrénování
-------------------------|--------------------------
**Lineární model, 2 parametry** | **Nelineární model, 7 parametrů**
Tréninková chyba = 5.3 | Tréninková chyba = 0
Validační chyba = 5.1 | Validační chyba = 20

* Vlevo vidíme dobré přímkové přiblížení. Protože počet parametrů je adekvátní, model správně chápe rozložení bodů.
* Vpravo je model příliš výkonný. Protože máme pouze 5 bodů a model má 7 parametrů, může se přizpůsobit tak, aby procházel všemi body, čímž je tréninková chyba 0. To však brání modelu pochopit správný vzor v datech, takže validační chyba je velmi vysoká.

Je velmi důležité najít správnou rovnováhu mezi bohatostí modelu (počtem parametrů) a počtem tréninkových vzorků.

## Proč přetrénování nastává

  * Nedostatek tréninkových dat
  * Příliš výkonný model
  * Příliš mnoho šumu ve vstupních datech

## Jak detekovat přetrénování

Jak můžete vidět z grafu výše, přetrénování lze detekovat velmi nízkou tréninkovou chybou a vysokou validační chybou. Obvykle během tréninku vidíme, jak tréninková i validační chyba začínají klesat, a pak v určitém bodě může validační chyba přestat klesat a začít stoupat. To bude známka přetrénování a indikátor, že bychom pravděpodobně měli zastavit trénink v tomto bodě (nebo alespoň udělat snímek modelu).

## Jak zabránit přetrénování

Pokud vidíte, že přetrénování nastává, můžete udělat jedno z následujících:

 * Zvýšit množství tréninkových dat
 * Snížit složitost modelu
 * Použít nějakou regularizační techniku, jako je Dropout, kterou později zvážíme.

## Přetrénování a kompromis mezi odchylkou a rozptylem

Přetrénování je vlastně případ obecnějšího problému ve statistice nazývaného kompromis mezi odchylkou a rozptylem. Pokud zvažujeme možné zdroje chyb v našem modelu, můžeme vidět dva typy chyb:

* **Chyby odchylky** jsou způsobeny tím, že náš algoritmus nedokáže správně zachytit vztah mezi tréninkovými daty. Může to být důsledek toho, že náš model není dostatečně výkonný (**podtrénování**).
* **Chyby rozptylu**, které jsou způsobeny tím, že model aproximuje šum ve vstupních datech místo smysluplného vztahu (**přetrénování**).

Během tréninku chyby odchylky klesají (jak se náš model učí aproximovat data) a chyby rozptylu rostou. Je důležité zastavit trénink - buď ručně (když detekujeme přetrénování) nebo automaticky (zavedením regularizace) - aby se zabránilo přetrénování.

## Závěr

V této lekci jste se naučili o rozdílech mezi různými API pro dva nejpopulárnější AI frameworky, TensorFlow a PyTorch. Kromě toho jste se naučili o velmi důležitém tématu, přetrénování.

## 🚀 Výzva

V doprovodných zápisnících najdete na konci 'úkoly'; projděte si zápisníky a splňte úkoly.

## Recenze & Samostudium

Proveďte výzkum na následující témata:

- TensorFlow
- PyTorch
- Přetrénování

Položte si následující otázky:

- Jaký je rozdíl mezi TensorFlow a PyTorch?
- Jaký je rozdíl mezi přetrénováním a podtrénováním?

## Úkol

V tomto cvičení jste požádáni, abyste vyřešili dva klasifikační problémy pomocí jedno- a vícevrstvých plně propojených sítí s využitím PyTorch nebo TensorFlow.

**Prohlášení**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, vezměte prosím na vědomí, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument ve svém původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.