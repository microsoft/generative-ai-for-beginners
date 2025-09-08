<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:47:15+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sv"
}
-->
# Introduktion till neurala nätverk. Flerlagersperceptron

I föregående avsnitt lärde du dig om den enklaste modellen för neurala nätverk – enlagersperceptron, en linjär tvåklassklassificeringsmodell.

I det här avsnittet kommer vi att utöka denna modell till en mer flexibel ram som gör det möjligt för oss att:

* utföra **flerklassklassificering** utöver tvåklass
* lösa **regressionsproblem** utöver klassificering
* separera klasser som inte är linjärt separerbara

Vi kommer också att utveckla vår egen modulära ram i Python som låter oss konstruera olika arkitekturer för neurala nätverk.

## Formalisering av maskininlärning

Låt oss börja med att formalisera problemet inom maskininlärning. Anta att vi har en träningsdatamängd **X** med etiketter **Y**, och vi behöver bygga en modell *f* som ger så korrekta förutsägelser som möjligt. Kvaliteten på förutsägelserna mäts med en **förlustfunktion** ℒ. Följande förlustfunktioner används ofta:

* För regressionsproblem, när vi behöver förutsäga ett tal, kan vi använda **absolut fel** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, eller **kvadratiskt fel** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* För klassificering använder vi **0-1-förlust** (vilket i princip är samma som modellens **noggrannhet**), eller **logistisk förlust**.

För en enlagersperceptron definierades funktionen *f* som en linjär funktion *f(x)=wx+b* (här är *w* viktmatrisen, *x* är vektorn med indatafunktioner, och *b* är bias-vektorn). För olika arkitekturer av neurala nätverk kan denna funktion anta en mer komplex form.

> Vid klassificering är det ofta önskvärt att få sannolikheter för respektive klasser som nätverkets output. För att omvandla godtyckliga tal till sannolikheter (t.ex. för att normalisera output) använder vi ofta **softmax**-funktionen σ, och funktionen *f* blir *f(x)=σ(wx+b)*

I definitionen av *f* ovan kallas *w* och *b* för **parametrar** θ=⟨*w,b*⟩. Givet datamängden ⟨**X**,**Y**⟩ kan vi beräkna ett totalt fel över hela datamängden som en funktion av parametrarna θ.

> ✅ **Målet med träningen av neurala nätverk är att minimera felet genom att variera parametrarna θ**

## Optimering med gradientnedstigning

Det finns en välkänd metod för funktionsoptimering som kallas **gradientnedstigning**. Idén är att vi kan beräkna en derivata (i flerdimensionellt fall kallad **gradient**) av förlustfunktionen med avseende på parametrarna, och variera parametrarna på ett sätt som minskar felet. Detta kan formaliseras så här:

* Initiera parametrarna med några slumpmässiga värden w<sup>(0)</sup>, b<sup>(0)</sup>
* Upprepa följande steg många gånger:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under träningen ska optimeringsstegen beräknas med hänsyn till hela datamängden (kom ihåg att förlusten beräknas som en summa över alla träningsprov). Men i praktiken tar vi små delar av datamängden som kallas **minibatcher**, och beräknar gradienter baserat på en delmängd av data. Eftersom delmängden tas slumpmässigt varje gång kallas denna metod **stokastisk gradientnedstigning** (SGD).

## Flerlagersperceptroner och backpropagation

Ett enlagers nätverk, som vi sett ovan, kan klassificera linjärt separerbara klasser. För att bygga en rikare modell kan vi kombinera flera lager i nätverket. Matematiskt innebär det att funktionen *f* får en mer komplex form och beräknas i flera steg:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Här är α en **icke-linjär aktiveringsfunktion**, σ är en softmax-funktion, och parametrarna θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradientnedstigningsalgoritmen är densamma, men det blir svårare att beräkna gradienterna. Med hjälp av kedjeregeln kan vi beräkna derivator som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kedjeregeln används för att beräkna derivator av förlustfunktionen med avseende på parametrarna.

Observera att den vänstermest delen i alla dessa uttryck är densamma, vilket gör att vi effektivt kan beräkna derivator genom att börja från förlustfunktionen och gå "bakåt" genom beräkningsgrafen. Därför kallas metoden för att träna en flerskiktsperceptron för **backpropagation**, eller 'backprop'.



> TODO: bildreferens

> ✅ Vi kommer att gå igenom backpropagation i mycket större detalj i vårt notebook-exempel.  

## Slutsats

I denna lektion har vi byggt vårt eget bibliotek för neurala nätverk och använt det för en enkel tvådimensionell klassificeringsuppgift.

## 🚀 Utmaning

I det medföljande notebooket kommer du att implementera din egen ram för att bygga och träna flerskiktsperceptroner. Du kommer att kunna se i detalj hur moderna neurala nätverk fungerar.

Fortsätt till OwnFramework-notebooket och arbeta dig igenom det.



## Repetition & Självstudier

Backpropagation är en vanlig algoritm som används inom AI och ML, och är värd att studera mer ingående.

## Uppgift

I denna labb ska du använda ramen du byggde i denna lektion för att lösa MNIST-klassificering av handskrivna siffror.

* Instruktioner
* Notebook

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.