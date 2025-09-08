<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:36:28+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "cs"
}
-->
# Frameworky neuronových sítí

Jak jsme se již naučili, abychom mohli efektivně trénovat neuronové sítě, musíme udělat dvě věci:

* Pracovat s tensory, např. násobit, sčítat a počítat některé funkce jako sigmoid nebo softmax
* Vypočítat gradienty všech výrazů, abychom mohli provést optimalizaci pomocí gradientního sestupu

Zatímco knihovna `numpy` zvládne první část, potřebujeme nějaký mechanismus pro výpočet gradientů. V našem frameworku, který jsme vyvinuli v předchozí části, jsme museli ručně naprogramovat všechny derivace uvnitř metody `backward`, která provádí zpětnou propagaci. Ideálně by framework měl umožnit výpočet gradientů *libovolného výrazu*, který definujeme.

Další důležitou věcí je možnost provádět výpočty na GPU nebo jiných specializovaných výpočetních jednotkách, jako je TPU. Trénování hlubokých neuronových sítí vyžaduje *mnoho* výpočtů, a proto je velmi důležité tyto výpočty paralelizovat na GPU.

> ✅ Termín 'paralelizovat' znamená rozdělit výpočty mezi více zařízení.

V současnosti jsou dva nejpopulárnější frameworky pro neuronové sítě: TensorFlow a PyTorch. Oba poskytují nízkoúrovňové API pro práci s tensory jak na CPU, tak na GPU. Nad tímto nízkoúrovňovým API existuje také vysokoúrovňové API, nazývané Keras a PyTorch Lightning.

Nízkourovňové API | TensorFlow | PyTorch
-----------------|------------|---------
Vysokoúrovňové API | Keras | PyTorch Lightning

**Nízkourovňová API** v obou frameworcích umožňují vytvářet tzv. **výpočetní grafy**. Tento graf definuje, jak spočítat výstup (obvykle ztrátovou funkci) pro dané vstupní parametry, a může být spuštěn na GPU, pokud je k dispozici. Existují funkce pro diferenciaci tohoto výpočetního grafu a výpočet gradientů, které lze následně použít k optimalizaci parametrů modelu.

**Vysokoúrovňová API** považují neuronové sítě za **sekvenci vrstev** a výrazně usnadňují konstrukci většiny neuronových sítí. Trénování modelu obvykle vyžaduje přípravu dat a následné zavolání funkce `fit`, která celý proces provede.

Vysokoúrovňové API umožňuje rychle sestavit typické neuronové sítě, aniž byste se museli zabývat mnoha detaily. Na druhou stranu nízkoúrovňové API nabízí mnohem větší kontrolu nad trénovacím procesem, a proto se často používá ve výzkumu, kdy pracujete s novými architekturami neuronových sítí.

Je také důležité pochopit, že můžete používat obě API společně, např. můžete vyvinout vlastní architekturu vrstvy pomocí nízkoúrovňového API a pak ji použít v rámci větší sítě vytvořené a trénované pomocí vysokoúrovňového API. Nebo můžete definovat síť pomocí vysokoúrovňového API jako sekvenci vrstev a pak použít vlastní nízkoúrovňovou trénovací smyčku pro optimalizaci. Obě API používají stejné základní koncepty a jsou navržena tak, aby spolu dobře fungovala.

## Učení

V tomto kurzu nabízíme většinu obsahu jak pro PyTorch, tak pro TensorFlow. Můžete si vybrat preferovaný framework a projít si pouze odpovídající notebooky. Pokud si nejste jisti, který framework zvolit, přečtěte si na internetu diskuse o **PyTorch vs. TensorFlow**. Můžete také vyzkoušet oba frameworky, abyste lépe porozuměli.

Kde je to možné, použijeme pro jednoduchost vysokoúrovňová API. Nicméně věříme, že je důležité pochopit, jak neuronové sítě fungují od základů, proto na začátku pracujeme s nízkoúrovňovým API a tensory. Pokud ale chcete rychle začít a nechcete trávit čas učením těchto detailů, můžete je přeskočit a rovnou přejít k notebookům s vysokoúrovňovým API.

## ✍️ Cvičení: Frameworky

Pokračujte ve studiu v následujících noteboocích:

Nízkourovňové API | TensorFlow+Keras Notebook | PyTorch
-----------------|-----------------------------|---------
Vysokoúrovňové API | Keras | *PyTorch Lightning*

Po zvládnutí frameworků si shrneme pojem přeučení.

# Přeučení (Overfitting)

Přeučení je extrémně důležitý pojem v oblasti strojového učení a je velmi důležité mu správně porozumět!

Zvažme následující problém aproximace 5 bodů (na grafech níže označených `x`):

!linear | overfit
-------------------------|--------------------------
**Lineární model, 2 parametry** | **Nelineární model, 7 parametrů**
Trénovací chyba = 5.3 | Trénovací chyba = 0
Validacní chyba = 5.1 | Validacní chyba = 20

* Vlevo vidíme dobrou přímkovou aproximaci. Protože počet parametrů je adekvátní, model správně zachycuje rozložení bodů.
* Vpravo je model příliš složitý. Protože máme jen 5 bodů a model má 7 parametrů, může se přizpůsobit tak, že projde všemi body, což vede k nulové trénovací chybě. To však brání modelu pochopit správný vzor za daty, a proto je validační chyba velmi vysoká.

Je velmi důležité najít správnou rovnováhu mezi složitostí modelu (počtem parametrů) a počtem trénovacích vzorků.

## Proč dochází k přeučení

  * Nedostatek trénovacích dat
  * Příliš složitý model
  * Příliš mnoho šumu ve vstupních datech

## Jak odhalit přeučení

Jak vidíte z grafu výše, přeučení lze odhalit podle velmi nízké trénovací chyby a vysoké validační chyby. Během tréninku obvykle vidíme, že jak trénovací, tak validační chyba klesají, ale v určitém bodě může validační chyba přestat klesat a začít růst. To je známka přeučení a signál, že bychom měli pravděpodobně trénink zastavit (nebo alespoň uložit momentální stav modelu).

overfitting

## Jak přeučení zabránit

Pokud zjistíte, že dochází k přeučení, můžete udělat jednu z následujících věcí:

 * Zvýšit množství trénovacích dat
 * Snížit složitost modelu
 * Použít nějakou regularizační techniku, například Dropout, kterou si později ukážeme.

## Přeučení a kompromis mezi biasem a variancí

Přeučení je ve skutečnosti případ obecnějšího problému ve statistice nazývaného kompromis mezi biasem a variancí. Pokud zvážíme možné zdroje chyb v našem modelu, můžeme rozlišit dva typy chyb:

* **Bias (systémová chyba)** je způsobena tím, že náš algoritmus nedokáže správně zachytit vztah mezi trénovacími daty. Může to být způsobeno tím, že model není dostatečně výkonný (**podtrénování**).
* **Variance (rozptyl)** je způsobena tím, že model aproximuje šum ve vstupních datech místo smysluplného vztahu (**přetrénování**).

Během tréninku bias klesá (model se učí data aproximovat) a variance roste. Je důležité trénink zastavit – buď ručně (když odhalíme přeučení), nebo automaticky (zavedením regularizace) – aby se přeučení zabránilo.

## Závěr

V této lekci jste se dozvěděli o rozdílech mezi různými API u dvou nejpopulárnějších AI frameworků, TensorFlow a PyTorch. Navíc jste se seznámili s velmi důležitým tématem, přeučením.

## 🚀 Výzva

V přiložených noteboocích najdete na konci „úkoly“; projděte si notebooky a úkoly splňte.

## Přehled a samostudium

Proveďte si vlastní průzkum na následující témata:

- TensorFlow
- PyTorch
- Přeučení (Overfitting)

Zeptejte se sami sebe:

- Jaký je rozdíl mezi TensorFlow a PyTorch?
- Jaký je rozdíl mezi přeučením a podtrénováním?

## Zadání

V tomto laboratorním cvičení máte za úkol vyřešit dva klasifikační problémy pomocí jednovrstvých a vícevrstvých plně propojených sítí s využitím PyTorch nebo TensorFlow.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.