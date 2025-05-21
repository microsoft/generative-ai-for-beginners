<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T01:59:56+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sv"
}
-->
# Ramverk för neurala nätverk

Som vi redan har lärt oss, för att kunna träna neurala nätverk effektivt behöver vi göra två saker:

* Att arbeta med tensorer, t.ex. multiplicera, addera och beräkna funktioner som sigmoid eller softmax
* Att beräkna gradienter av alla uttryck för att kunna utföra gradientnedstigningsoptimering

Medan `numpy`-biblioteket kan göra den första delen, behöver vi någon mekanism för att beräkna gradienter. I vårt ramverk som vi utvecklade i föregående avsnitt var vi tvungna att manuellt programmera alla derivatfunktioner inom `backward`-metoden, som gör bakåtpropagering. Idealiskt sett borde ett ramverk ge oss möjligheten att beräkna gradienter av *vilket uttryck som helst* som vi kan definiera.

En annan viktig sak är att kunna utföra beräkningar på GPU eller andra specialiserade beräkningsenheter, som TPU. Träning av djupa neurala nätverk kräver *väldigt mycket* beräkningar, och att kunna parallellisera dessa beräkningar på GPU:er är mycket viktigt.

> ✅ Termen 'parallellisera' betyder att fördela beräkningarna över flera enheter.

För närvarande är de två mest populära neurala ramverken: TensorFlow och PyTorch. Båda erbjuder ett lågnivå-API för att arbeta med tensorer på både CPU och GPU. Ovanpå lågnivå-API:et finns också högre nivå-API, kallat Keras respektive PyTorch Lightning.

Lågnivå-API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
Högnivå-API| Keras| Pytorch

**Lågnivå-API:er** i båda ramverken låter dig bygga så kallade **beräkningsgrafer**. Denna graf definierar hur man beräknar utgången (vanligtvis förlustfunktionen) med givna inmatningsparametrar och kan skickas för beräkning på GPU om den är tillgänglig. Det finns funktioner för att differentiera denna beräkningsgraf och beräkna gradienter, som sedan kan användas för att optimera modellparametrar.

**Högnivå-API:er** betraktar i stort sett neurala nätverk som en **sekvens av lager**, och gör det mycket enklare att konstruera de flesta neurala nätverk. Träning av modellen kräver vanligtvis att förbereda data och sedan kalla på en `fit`-funktion för att göra jobbet.

Högnivå-API:et låter dig konstruera typiska neurala nätverk mycket snabbt utan att behöva oroa dig för många detaljer. Samtidigt erbjuder lågnivå-API mycket mer kontroll över träningsprocessen, och därför används de mycket inom forskning, när du arbetar med nya neurala nätverksarkitekturer.

Det är också viktigt att förstå att du kan använda båda API:erna tillsammans, t.ex. du kan utveckla din egen nätverkslagerarkitektur med lågnivå-API och sedan använda den inom det större nätverket som konstrueras och tränas med högnivå-API. Eller du kan definiera ett nätverk med högnivå-API som en sekvens av lager och sedan använda din egen lågnivå-träningsloop för att utföra optimering. Båda API:erna använder samma grundläggande underliggande koncept, och de är designade för att fungera bra tillsammans.

## Lärande

I denna kurs erbjuder vi det mesta av innehållet både för PyTorch och TensorFlow. Du kan välja ditt föredragna ramverk och bara gå igenom de motsvarande notböckerna. Om du är osäker på vilket ramverk du ska välja, läs några diskussioner på internet om **PyTorch vs. TensorFlow**. Du kan också titta på båda ramverken för att få bättre förståelse.

Där det är möjligt kommer vi att använda högnivå-API:er för enkelhetens skull. Men vi tror att det är viktigt att förstå hur neurala nätverk fungerar från grunden, så i början börjar vi med att arbeta med lågnivå-API och tensorer. Men om du vill komma igång snabbt och inte vill lägga mycket tid på att lära dig dessa detaljer, kan du hoppa över dem och gå direkt till högnivå-API-notböckerna.

## ✍️ Övningar: Ramverk

Fortsätt ditt lärande i följande notböcker:

Lågnivå-API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
Högnivå-API| Keras | *PyTorch Lightning*

Efter att ha bemästrat ramverken, låt oss återgå till begreppet överanpassning.

# Överanpassning

Överanpassning är ett extremt viktigt begrepp inom maskininlärning, och det är väldigt viktigt att få det rätt!

Tänk på följande problem med att approximera 5 punkter (representerade av `x` på graferna nedan):

!linjär | överanpassad
-------------------------|--------------------------
**Linjär modell, 2 parametrar** | **Icke-linjär modell, 7 parametrar**
Träningsfel = 5.3 | Träningsfel = 0
Valideringsfel = 5.1 | Valideringsfel = 20

* Till vänster ser vi en bra rak linjeapproximation. Eftersom antalet parametrar är adekvat, får modellen rätt på idén bakom punktfördelningen.
* Till höger är modellen för kraftfull. Eftersom vi bara har 5 punkter och modellen har 7 parametrar, kan den justera sig så att den går genom alla punkter, vilket gör träningsfelet till 0. Men detta hindrar modellen från att förstå det korrekta mönstret bakom datan, så valideringsfelet är väldigt högt.

Det är väldigt viktigt att hitta en korrekt balans mellan modellens rikedom (antalet parametrar) och antalet träningsprover.

## Varför överanpassning uppstår

  * Inte tillräckligt med träningsdata
  * För kraftfull modell
  * För mycket brus i inmatningsdata

## Hur man upptäcker överanpassning

Som du kan se från grafen ovan kan överanpassning upptäckas genom ett väldigt lågt träningsfel och ett högt valideringsfel. Normalt under träning kommer vi att se både tränings- och valideringsfel börja minska, och sedan vid någon punkt kanske valideringsfelet slutar minska och börjar öka. Detta kommer att vara ett tecken på överanpassning, och en indikator på att vi förmodligen borde sluta träna vid denna punkt (eller åtminstone ta en ögonblicksbild av modellen).

överanpassning

## Hur man förhindrar överanpassning

Om du kan se att överanpassning uppstår, kan du göra något av följande:

 * Öka mängden träningsdata
 * Minska modellens komplexitet
 * Använd någon regulariseringsteknik, såsom Dropout, som vi kommer att överväga senare.

## Överanpassning och Bias-Variance Tradeoff

Överanpassning är faktiskt ett fall av ett mer generiskt problem inom statistik kallat Bias-Variance Tradeoff. Om vi betraktar de möjliga källorna till fel i vår modell, kan vi se två typer av fel:

* **Bias-fel** orsakas av att vår algoritm inte kan fånga relationen mellan träningsdata korrekt. Det kan bero på att vår modell inte är tillräckligt kraftfull (**underanpassning**).
* **Variansfel**, som orsakas av att modellen approximera brus i inmatningsdata istället för meningsfull relation (**överanpassning**).

Under träning minskar bias-fel (när vår modell lär sig att approximera datan), och variansfel ökar. Det är viktigt att sluta träna - antingen manuellt (när vi upptäcker överanpassning) eller automatiskt (genom att införa regularisering) - för att förhindra överanpassning.

## Slutsats

I denna lektion har du lärt dig om skillnaderna mellan de olika API:erna för de två mest populära AI-ramverken, TensorFlow och PyTorch. Dessutom har du lärt dig om ett mycket viktigt ämne, överanpassning.

## 🚀 Utmaning

I de medföljande notböckerna hittar du 'uppgifter' längst ner; arbeta igenom notböckerna och slutför uppgifterna.

## Granskning & Självstudier

Gör lite forskning om följande ämnen:

- TensorFlow
- PyTorch
- Överanpassning

Ställ dig själv följande frågor:

- Vad är skillnaden mellan TensorFlow och PyTorch?
- Vad är skillnaden mellan överanpassning och underanpassning?

## Uppgift

I detta labb ombeds du att lösa två klassificeringsproblem med hjälp av enlagers och flerlager fullt anslutna nätverk med PyTorch eller TensorFlow.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiserade översättningar kan innehålla fel eller oriktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.