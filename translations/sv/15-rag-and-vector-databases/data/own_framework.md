<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:25:20+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sv"
}
-->
# Introduktion till neurala nätverk. Flerlagers perceptron

I föregående avsnitt lärde du dig om den enklaste modellen för neurala nätverk - enlagers perceptron, en linjär tvåklassklassificeringsmodell.

I detta avsnitt kommer vi att utöka denna modell till en mer flexibel ram, vilket gör att vi kan:

* utföra **flerklassklassificering** utöver tvåklass
* lösa **regressionsproblem** utöver klassificering
* separera klasser som inte är linjärt separerbara

Vi kommer också att utveckla vår egen modulära ram i Python som gör att vi kan konstruera olika arkitekturer för neurala nätverk.

## Formalisering av maskininlärning

Låt oss börja med att formalisera maskininlärningsproblemet. Anta att vi har ett träningsdataset **X** med etiketter **Y**, och vi behöver bygga en modell *f* som gör de mest exakta förutsägelserna. Kvaliteten på förutsägelserna mäts med **förlustfunktion** ℒ. Följande förlustfunktioner används ofta:

* För regressionsproblem, när vi behöver förutsäga ett nummer, kan vi använda **absolut fel** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, eller **kvadratiskt fel** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* För klassificering använder vi **0-1 förlust** (som i princip är detsamma som **modellens noggrannhet**), eller **logistisk förlust**.

För enlagers perceptron definierades funktionen *f* som en linjär funktion *f(x)=wx+b* (här är *w* viktsmatrisen, *x* är vektorn av indatafunktioner, och *b* är biasvektorn). För olika arkitekturer för neurala nätverk kan denna funktion ta en mer komplex form.

> Vid klassificering är det ofta önskvärt att få sannolikheter för motsvarande klasser som nätverksutgång. För att konvertera godtyckliga nummer till sannolikheter (t.ex. för att normalisera utgången) använder vi ofta **softmax**-funktionen σ, och funktionen *f* blir *f(x)=σ(wx+b)*

I definitionen av *f* ovan kallas *w* och *b* **parametrar** θ=⟨*w,b*⟩. Givet datasetet ⟨**X**,**Y**⟩ kan vi beräkna ett övergripande fel på hela datasetet som en funktion av parametrarna θ.

> ✅ **Målet med träning av neurala nätverk är att minimera felet genom att variera parametrarna θ**

## Optimering med gradientnedstigning

Det finns en välkänd metod för funktionsoptimering kallad **gradientnedstigning**. Idén är att vi kan beräkna en derivata (i multidimensionellt fall kallad **gradient**) av förlustfunktionen med avseende på parametrarna, och variera parametrarna på ett sådant sätt att felet skulle minska. Detta kan formaliseras enligt följande:

* Initiera parametrar med några slumpmässiga värden w<sup>(0)</sup>, b<sup>(0)</sup>
* Upprepa följande steg många gånger:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under träning förväntas optimeringsstegen beräknas med hänsyn till hela datasetet (kom ihåg att förlusten beräknas som en summa genom alla träningsprover). Men i verkligheten tar vi små delar av datasetet kallade **minibatcher**, och beräknar gradienter baserat på en delmängd av data. Eftersom delmängden tas slumpmässigt varje gång, kallas en sådan metod **stokastisk gradientnedstigning** (SGD).

## Flerlagers perceptron och backpropagation

Enlagers nätverk, som vi har sett ovan, kan klassificera linjärt separerbara klasser. För att bygga en rikare modell kan vi kombinera flera lager av nätverket. Matematiskt skulle det innebära att funktionen *f* skulle ha en mer komplex form och beräknas i flera steg:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Här är α en **icke-linjär aktiveringsfunktion**, σ är en softmax-funktion, och parametrar θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradientnedstigningsalgoritmen skulle förbli densamma, men det skulle vara svårare att beräkna gradienter. Givet kedjedifferentieringsregeln kan vi beräkna derivator som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kedjedifferentieringsregeln används för att beräkna derivator av förlustfunktionen med avseende på parametrarna.

Observera att den vänstra delen av alla dessa uttryck är densamma, och därför kan vi effektivt beräkna derivator från förlustfunktionen och gå "bakåt" genom beräkningsgrafen. Således kallas metoden för att träna en flerlagers perceptron **backpropagation**, eller 'backprop'.

> TODO: bildcitering

> ✅ Vi kommer att täcka backprop i mycket mer detalj i vårt notebook-exempel.

## Slutsats

I denna lektion har vi byggt vårt eget bibliotek för neurala nätverk, och vi har använt det för en enkel tvådimensionell klassificeringsuppgift.

## 🚀 Utmaning

I den medföljande notebooken kommer du att implementera din egen ram för att bygga och träna flerlagers perceptrons. Du kommer att kunna se i detalj hur moderna neurala nätverk fungerar.

Fortsätt till OwnFramework notebook och arbeta igenom den.

## Granskning & Självstudie

Backpropagation är en vanlig algoritm som används inom AI och ML, värd att studera mer ingående.

## Uppgift

I detta labb ombeds du att använda den ram du konstruerade i denna lektion för att lösa MNIST-handskriven sifferklassificering.

* Instruktioner
* Notebook

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.