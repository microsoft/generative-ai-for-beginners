<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:04:12+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sv"
}
-->
# Ramverk för neurala nätverk

Som vi redan har lärt oss, för att kunna träna neurala nätverk effektivt behöver vi göra två saker:

* Att arbeta med tensorer, t.ex. multiplicera, addera och beräkna vissa funktioner som sigmoid eller softmax
* Att beräkna gradienter av alla uttryck, för att kunna utföra gradientnedstigningsoptimering

Medan `numpy`-biblioteket kan göra den första delen, behöver vi någon mekanism för att beräkna gradienter. I vårt ramverk som vi utvecklade i föregående avsnitt var vi tvungna att manuellt programmera alla derivatafunktioner inuti `backward`-metoden, som utför backpropagation. Idealiskt sett bör ett ramverk ge oss möjligheten att beräkna gradienter av *vilket uttryck som helst* som vi kan definiera.

En annan viktig sak är att kunna utföra beräkningar på GPU, eller andra specialiserade beräkningsenheter, som TPU. Träning av djupa neurala nätverk kräver *mycket* beräkningar, och att kunna parallellisera dessa beräkningar på GPU:er är mycket viktigt.

> ✅ Termen 'parallellisera' betyder att fördela beräkningarna över flera enheter.

För närvarande är de två mest populära neurala ramverken: TensorFlow och PyTorch. Båda tillhandahåller ett låg-nivå API för att arbeta med tensorer på både CPU och GPU. Ovanpå låg-nivå API:et finns också hög-nivå API, kallat Keras respektive PyTorch Lightning.

Låg-nivå API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
Hög-nivå API | Keras| PyTorch Lightning

**Låg-nivå API:er** i båda ramverken låter dig bygga så kallade **beräkningsgrafer**. Denna graf definierar hur man beräknar utdata (vanligtvis förlustfunktionen) med givna indata-parametrar, och kan skickas för beräkning på GPU, om den finns tillgänglig. Det finns funktioner för att differentiera denna beräkningsgraf och beräkna gradienter, vilka sedan kan användas för att optimera modellparametrar.

**Hög-nivå API:er** betraktar i stort sett neurala nätverk som en **sekvens av lager**, och gör konstruktionen av de flesta neurala nätverk mycket enklare. Träning av modellen kräver vanligtvis att förbereda data och sedan anropa en `fit`-funktion för att utföra arbetet.

Hög-nivå API tillåter dig att konstruera typiska neurala nätverk mycket snabbt utan att oroa dig för många detaljer. Samtidigt erbjuder låg-nivå API mycket mer kontroll över träningsprocessen, och därför används de mycket inom forskning, när man arbetar med nya neurala nätverksarkitekturer.

Det är också viktigt att förstå att du kan använda båda API:erna tillsammans, t.ex. du kan utveckla din egen nätverkslagerarkitektur med låg-nivå API, och sedan använda den inuti det större nätverket som konstruerats och tränats med hög-nivå API. Eller så kan du definiera ett nätverk med hög-nivå API som en sekvens av lager, och sedan använda din egen låg-nivå träningsloop för att utföra optimering. Båda API:erna använder samma grundläggande underliggande koncept, och de är designade för att fungera bra tillsammans.

## Lärande

I denna kurs erbjuder vi det mesta av innehållet både för PyTorch och TensorFlow. Du kan välja ditt föredragna ramverk och bara gå igenom de motsvarande anteckningsböckerna. Om du inte är säker på vilket ramverk du ska välja, läs några diskussioner på internet om **PyTorch vs. TensorFlow**. Du kan också titta på båda ramverken för att få en bättre förståelse.

Där det är möjligt, kommer vi att använda hög-nivå API:er för enkelhetens skull. Men vi anser att det är viktigt att förstå hur neurala nätverk fungerar från grunden, därför börjar vi med att arbeta med låg-nivå API och tensorer. Men om du vill komma igång snabbt och inte vill lägga mycket tid på att lära dig dessa detaljer, kan du hoppa över dem och gå direkt till hög-nivå API-anteckningsböckerna.

## ✍️ Övningar: Ramverk

Fortsätt ditt lärande i följande anteckningsböcker:

Låg-nivå API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
Hög-nivå API | Keras | *PyTorch Lightning*

Efter att ha bemästrat ramverken, låt oss återblicka på begreppet överanpassning.

# Överanpassning

Överanpassning är ett extremt viktigt koncept inom maskininlärning, och det är mycket viktigt att få det rätt!

Tänk på följande problem med att approximera 5 punkter (representerade av `x` på graferna nedan):

!linear | overfit
-------------------------|--------------------------
**Linjär modell, 2 parametrar** | **Icke-linjär modell, 7 parametrar**
Träningsfel = 5.3 | Träningsfel = 0
Valideringsfel = 5.1 | Valideringsfel = 20

* Till vänster ser vi en bra rak linjeapproximation. Eftersom antalet parametrar är adekvat, får modellen rätt på idén bakom punktfördelningen.
* Till höger är modellen för kraftfull. Eftersom vi bara har 5 punkter och modellen har 7 parametrar, kan den justera sig så att den går genom alla punkter, vilket gör träningsfelet till 0. Detta förhindrar dock modellen från att förstå det korrekta mönstret bakom data, och därför är valideringsfelet mycket högt.

Det är mycket viktigt att hitta en korrekt balans mellan modellens rikedom (antal parametrar) och antalet träningsprover.

## Varför överanpassning uppstår

  * Inte tillräckligt med träningsdata
  * För kraftfull modell
  * För mycket brus i indata

## Hur man upptäcker överanpassning

Som du kan se från grafen ovan, kan överanpassning upptäckas genom ett mycket lågt träningsfel och ett högt valideringsfel. Normalt under träning kommer vi att se både tränings- och valideringsfel börja minska, och sedan vid någon punkt kan valideringsfelet sluta minska och börja öka. Detta kommer att vara ett tecken på överanpassning, och en indikator på att vi förmodligen bör sluta träna vid denna punkt (eller åtminstone ta en ögonblicksbild av modellen).

## Hur man förhindrar överanpassning

Om du kan se att överanpassning uppstår, kan du göra ett av följande:

 * Öka mängden träningsdata
 * Minska modellens komplexitet
 * Använd någon regulariseringsteknik, som Dropout, vilket vi kommer att överväga senare.

## Överanpassning och Bias-Variance Avvägning

Överanpassning är faktiskt ett fall av ett mer generellt problem inom statistik kallat Bias-Variance Avvägning. Om vi betraktar de möjliga källorna till fel i vår modell, kan vi se två typer av fel:

* **Bias-fel** orsakas av att vår algoritm inte kan fånga relationen mellan träningsdata korrekt. Det kan bero på att vår modell inte är tillräckligt kraftfull (**underanpassning**).
* **Variansfel**, som orsakas av att modellen approximerar brus i indata istället för meningsfull relation (**överanpassning**).

Under träningen minskar bias-fel (eftersom vår modell lär sig att approximera data), och variansfel ökar. Det är viktigt att sluta träna - antingen manuellt (när vi upptäcker överanpassning) eller automatiskt (genom att införa regularisering) - för att förhindra överanpassning.

## Slutsats

I denna lektion lärde du dig om skillnaderna mellan de olika API:erna för de två mest populära AI-ramverken, TensorFlow och PyTorch. Dessutom lärde du dig om ett mycket viktigt ämne, överanpassning.

## 🚀 Utmaning

I de medföljande anteckningsböckerna hittar du 'uppgifter' längst ner; arbeta igenom anteckningsböckerna och slutför uppgifterna.

## Granskning & Självstudier

Gör lite forskning om följande ämnen:

- TensorFlow
- PyTorch
- Överanpassning

Fråga dig själv följande frågor:

- Vad är skillnaden mellan TensorFlow och PyTorch?
- Vad är skillnaden mellan överanpassning och underanpassning?

## Uppgift

I detta laboratorium blir du ombedd att lösa två klassificeringsproblem med hjälp av enkla och flerskiktade fullt anslutna nätverk med PyTorch eller TensorFlow.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.