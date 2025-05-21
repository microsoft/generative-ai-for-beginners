<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:06:17+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "cs"
}
-->
# Rámce pro neuronové sítě

Jak jsme se již naučili, abychom mohli efektivně trénovat neuronové sítě, musíme udělat dvě věci:

* Pracovat s tensory, např. násobit, sčítat a počítat některé funkce jako sigmoid nebo softmax
* Počítat gradienty všech výrazů, abychom mohli provádět optimalizaci metodou gradientního sestupu

Zatímco knihovna `numpy` zvládne první část, potřebujeme nějaký mechanismus pro výpočet gradientů. V našem rámci, který jsme vyvinuli v předchozí sekci, jsme museli ručně programovat všechny derivátové funkce uvnitř metody `backward`, která provádí zpětnou propagaci. Ideálně by nám rámec měl umožnit počítat gradienty *jakéhokoli výrazu*, který můžeme definovat.

Další důležitou věcí je být schopen provádět výpočty na GPU nebo jiných specializovaných výpočetních jednotkách, jako je TPU. Trénování hlubokých neuronových sítí vyžaduje *hodně* výpočtů a je velmi důležité tyto výpočty paralelizovat na GPU.

> ✅ Termín 'paralelizovat' znamená rozdělit výpočty mezi více zařízení.

V současnosti jsou dva nejpopulárnější neuronové rámce: TensorFlow a PyTorch. Oba poskytují nízkoúrovňové API pro práci s tensory jak na CPU, tak na GPU. Nad nízkoúrovňovým API existuje také vyšší úroveň API, nazývaná Keras a PyTorch Lightning.

Nízkoúrovňové API | TensorFlow| PyTorch
-----------------|-------------------------------------|--------------------------------
Vysokoúrovňové API| Keras| Pytorch

**Nízkoúrovňové API** v obou rámcích vám umožňuje stavět tzv. **výpočetní grafy**. Tento graf definuje, jak vypočítat výstup (obvykle ztrátovou funkci) s danými vstupními parametry a může být odeslán k výpočtu na GPU, pokud je dostupný. Existují funkce pro diferenciaci tohoto výpočetního grafu a výpočet gradientů, které pak mohou být použity pro optimalizaci parametrů modelu.

**Vysokoúrovňové API** v podstatě považují neuronové sítě za **sekvenci vrstev** a usnadňují konstrukci většiny neuronových sítí. Trénování modelu obvykle vyžaduje přípravu dat a následné volání funkce `fit`, aby se práce vykonala.

Vysokoúrovňové API vám umožňuje velmi rychle sestavit typické neuronové sítě, aniž byste se museli starat o mnoho detailů. Zároveň nízkoúrovňové API nabízí mnohem větší kontrolu nad trénovacím procesem, a proto se hodně používají ve výzkumu, když se zabýváte novými architekturami neuronových sítí.

Je také důležité pochopit, že můžete použít obě API společně, např. můžete vyvinout vlastní architekturu vrstvy sítě pomocí nízkoúrovňového API a poté ji použít v rámci větší sítě sestavené a trénované pomocí vysokoúrovňového API. Nebo můžete definovat síť pomocí vysokoúrovňového API jako sekvenci vrstev a poté použít vlastní nízkoúrovňovou trénovací smyčku k provedení optimalizace. Obě API používají stejné základní koncepty a jsou navrženy tak, aby spolu dobře fungovaly.

## Učení

V tomto kurzu nabízíme většinu obsahu jak pro PyTorch, tak pro TensorFlow. Můžete si vybrat svůj preferovaný rámec a projít pouze odpovídajícími poznámkovými bloky. Pokud si nejste jisti, který rámec zvolit, přečtěte si některé diskuse na internetu ohledně **PyTorch vs. TensorFlow**. Můžete se také podívat na oba rámce, abyste získali lepší představu.

Kde je to možné, použijeme vysokoúrovňová API pro jednoduchost. Nicméně věříme, že je důležité pochopit, jak neuronové sítě fungují od základů, proto začínáme prací s nízkoúrovňovým API a tensory. Pokud však chcete začít rychle a nechcete trávit hodně času učením těchto detailů, můžete je přeskočit a přejít přímo k poznámkovým blokům vysokoúrovňového API.

## ✍️ Cvičení: Rámce

Pokračujte ve svém učení v následujících poznámkových blocích:

Nízkoúrovňové API | TensorFlow+Keras Notebook | PyTorch
-----------------|-------------------------------------|--------------------------------
Vysokoúrovňové API| Keras | *PyTorch Lightning*

Po zvládnutí rámců si zopakujme pojem přetrénování.

# Přetrénování

Přetrénování je velmi důležitý koncept v strojovém učení a je velmi důležité ho pochopit správně!

Zvažte následující problém aproximace 5 bodů (reprezentovaných `x` na grafech níže):

!linear | overfit
-------------------------|--------------------------
**Lineární model, 2 parametry** | **Nelineární model, 7 parametrů**
Chyba trénování = 5.3 | Chyba trénování = 0
Chyba validace = 5.1 | Chyba validace = 20

* Vlevo vidíme dobrou aproximaci přímkou. Protože počet parametrů je adekvátní, model správně pochopí rozložení bodů.
* Vpravo je model příliš výkonný. Protože máme pouze 5 bodů a model má 7 parametrů, může se nastavit tak, aby procházel všemi body, což způsobí, že chyba trénování bude 0. To však brání modelu pochopit správný vzor v datech, takže chyba validace je velmi vysoká.

Je velmi důležité najít správnou rovnováhu mezi bohatostí modelu (počtem parametrů) a počtem trénovacích vzorků.

## Proč přetrénování nastává

  * Nedostatek trénovacích dat
  * Příliš výkonný model
  * Příliš mnoho šumu ve vstupních datech

## Jak zjistit přetrénování

Jak můžete vidět z výše uvedeného grafu, přetrénování lze zjistit velmi nízkou chybou trénování a vysokou chybou validace. Během trénování obvykle vidíme, že chyby trénování i validace začínají klesat, a pak v určitém bodě může chyba validace přestat klesat a začít růst. To bude známkou přetrénování a indikátorem, že bychom pravděpodobně měli trénování v tomto bodě zastavit (nebo alespoň udělat snímek modelu).

## Jak zabránit přetrénování

Pokud vidíte, že přetrénování nastává, můžete udělat jedno z následujících:

 * Zvýšit množství trénovacích dat
 * Snížit složitost modelu
 * Použít nějakou regularizační techniku, jako je Dropout, kterou se budeme zabývat později.

## Přetrénování a kompromis mezi zkreslením a rozptylem

Přetrénování je ve skutečnosti případ obecnějšího problému ve statistice nazývaného kompromis mezi zkreslením a rozptylem. Pokud zvažujeme možné zdroje chyby v našem modelu, můžeme vidět dva typy chyb:

* **Chyby zkreslení** jsou způsobeny tím, že náš algoritmus nedokáže správně zachytit vztah mezi trénovacími daty. Může to být důsledek toho, že náš model není dostatečně výkonný (**podtrénování**).
* **Chyby rozptylu**, které jsou způsobeny tím, že model aproximuje šum ve vstupních datech místo smysluplného vztahu (**přetrénování**).

Během trénování chyby zkreslení klesají (jak se náš model učí aproximovat data) a chyby rozptylu rostou. Je důležité zastavit trénování - buď ručně (když zjistíme přetrénování) nebo automaticky (zavedením regularizace) - abychom zabránili přetrénování.

## Závěr

V této lekci jste se naučili o rozdílech mezi různými API pro dva nejpopulárnější AI rámce, TensorFlow a PyTorch. Kromě toho jste se naučili o velmi důležitém tématu, přetrénování.

## 🚀 Výzva

V přiložených poznámkových blocích najdete 'úkoly' na konci; projděte si poznámkové bloky a dokončete úkoly.

## Přehled a samostudium

Proveďte výzkum na následující témata:

- TensorFlow
- PyTorch
- Přetrénování

Zeptejte se sami sebe na následující otázky:

- Jaký je rozdíl mezi TensorFlow a PyTorch?
- Jaký je rozdíl mezi přetrénováním a podtrénováním?

## Zadání

V tomto laboratorním cvičení jste požádáni, abyste vyřešili dva klasifikační problémy pomocí jedno- a vícevrstvých plně propojených sítí pomocí PyTorch nebo TensorFlow.

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, uvědomte si, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace je doporučen profesionální lidský překlad. Neodpovídáme za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.