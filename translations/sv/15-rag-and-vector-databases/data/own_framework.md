<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:20:48+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sv"
}
-->
# Introduktion till Neurala Nätverk. Flerlagers Perceptron

I föregående avsnitt lärde du dig om den enklaste neurala nätverksmodellen - en enlagers perceptron, en linjär tvåklassklassificeringsmodell.

I det här avsnittet kommer vi att utöka denna modell till en mer flexibel ram, vilket tillåter oss att:

* utföra **flerklassklassificering** utöver tvåklass
* lösa **regressionsproblem** utöver klassificering
* separera klasser som inte är linjärt separerbara

Vi kommer också att utveckla vår egen modulära ram i Python som gör det möjligt för oss att konstruera olika neurala nätverksarkitekturer.

## Formalisering av Maskininlärning

Låt oss börja med att formalisera maskininlärningsproblemet. Antag att vi har en träningsdatamängd **X** med etiketter **Y**, och vi behöver bygga en modell *f* som gör de mest exakta förutsägelserna. Kvaliteten på förutsägelserna mäts av **förlustfunktionen** ℒ. Följande förlustfunktioner används ofta:

* För regressionsproblem, när vi behöver förutsäga ett tal, kan vi använda **absolut fel** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, eller **kvadratiskt fel** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* För klassificering använder vi **0-1 förlust** (vilket i princip är detsamma som **noggrannhet** hos modellen), eller **logistisk förlust**.

För en enlagers perceptron definierades funktionen *f* som en linjär funktion *f(x)=wx+b* (här är *w* viktmatrisen, *x* är vektorn av ingångsfunktioner, och *b* är biasvektorn). För olika neurala nätverksarkitekturer kan denna funktion anta en mer komplex form.

> Vid klassificering är det ofta önskvärt att få sannolikheter för motsvarande klasser som nätverksutgång. För att konvertera godtyckliga tal till sannolikheter (t.ex. för att normalisera utgången) använder vi ofta **softmax**-funktionen σ, och funktionen *f* blir *f(x)=σ(wx+b)*

I definitionen av *f* ovan kallas *w* och *b* för **parametrar** θ=⟨*w,b*⟩. Givet datasetet ⟨**X**,**Y**⟩, kan vi beräkna ett totalt fel på hela datasetet som en funktion av parametrarna θ.

> ✅ **Målet med träning av neurala nätverk är att minimera felet genom att variera parametrarna θ**

## Gradientnedstigningsoptimering

Det finns en välkänd metod för funktionsoptimering som kallas **gradientnedstigning**. Idén är att vi kan beräkna en derivata (i multidimensionellt fall kallad **gradient**) av förlustfunktionen med avseende på parametrarna, och variera parametrarna på ett sådant sätt att felet skulle minska. Detta kan formaliseras enligt följande:

* Initiera parametrar med några slumpvärden w<sup>(0)</sup>, b<sup>(0)</sup>
* Upprepa följande steg många gånger:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under träningen förväntas optimeringsstegen beräknas med hänsyn till hela datasetet (kom ihåg att förlusten beräknas som en summa genom alla träningsprover). Men i verkligheten tar vi små delar av datasetet kallade **minibatcher**, och beräknar gradienter baserat på en delmängd av data. Eftersom delmängden tas slumpmässigt varje gång, kallas sådan metod för **stokastisk gradientnedstigning** (SGD).

## Flerlagers Perceptroner och Backpropagation

En enlagers nätverk, som vi har sett ovan, kan klassificera linjärt separerbara klasser. För att bygga en rikare modell kan vi kombinera flera lager av nätverket. Matematiskt skulle det innebära att funktionen *f* skulle ha en mer komplex form och beräknas i flera steg:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Här är α en **icke-linjär aktiveringsfunktion**, σ är en softmax-funktion, och parametrarna θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradientnedstigningsalgoritmen skulle förbli densamma, men det skulle vara svårare att beräkna gradienter. Givet kedjedifferentieringsregeln kan vi beräkna derivator som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kedjedifferentieringsregeln används för att beräkna derivator av förlustfunktionen med avseende på parametrarna.

Observera att den vänstra delen av alla dessa uttryck är densamma, och därför kan vi effektivt beräkna derivator med start från förlustfunktionen och gå "bakåt" genom den beräkningsgrafen. Således kallas metoden för träning av en flerlagers perceptron för **backpropagation**, eller 'backprop'.

> TODO: bildcitering

> ✅ Vi kommer att gå igenom backprop mer detaljerat i vårt notebook-exempel.

## Slutsats

I denna lektion har vi byggt vårt eget neurala nätverksbibliotek, och vi har använt det för en enkel tvådimensionell klassificeringsuppgift.

## 🚀 Utmaning

I den medföljande notebooken kommer du att implementera din egen ram för att bygga och träna flerlagers perceptroner. Du kommer att kunna se i detalj hur moderna neurala nätverk fungerar.

Fortsätt till OwnFramework notebooken och arbeta igenom den.

## Granskning & Självstudier

Backpropagation är en vanlig algoritm som används inom AI och ML, värd att studera mer i detalj.

## Uppgift

I detta labb ombeds du använda den ram du konstruerade i denna lektion för att lösa MNIST-handritad sifferklassificering.

* Instruktioner
* Notebook

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller oriktigheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användningen av denna översättning.