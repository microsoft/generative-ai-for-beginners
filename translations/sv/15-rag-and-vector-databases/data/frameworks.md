<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:32:39+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sv"
}
-->
# Neural Network Frameworks

Som vi redan har lärt oss, för att kunna träna neurala nätverk effektivt behöver vi göra två saker:

* Att arbeta med tensorer, t.ex. multiplicera, addera och beräkna funktioner som sigmoid eller softmax
* Att beräkna gradienter för alla uttryck, för att kunna utföra gradientnedstigningsoptimering

Medan `numpy`-biblioteket kan hantera den första delen, behöver vi någon mekanism för att beräkna gradienter. I vårt ramverk som vi utvecklade i föregående avsnitt var vi tvungna att manuellt programmera alla derivatfunktioner inuti `backward`-metoden, som utför backpropagation. Idealiskt sett bör ett ramverk ge oss möjlighet att beräkna gradienter för *vilket uttryck som helst* som vi kan definiera.

En annan viktig sak är att kunna utföra beräkningar på GPU, eller andra specialiserade beräkningsenheter, som TPU. Träning av djupa neurala nätverk kräver *mycket* beräkningar, och att kunna parallellisera dessa beräkningar på GPU:er är mycket viktigt.

> ✅ Termen 'parallellisera' betyder att fördela beräkningarna över flera enheter.

För närvarande är de två mest populära neurala ramverken: TensorFlow och PyTorch. Båda erbjuder ett låg-nivå API för att arbeta med tensorer på både CPU och GPU. Ovanpå låg-nivå API:et finns även ett hög-nivå API, kallat Keras respektive PyTorch Lightning.

Low-Level API | TensorFlow | PyTorch  
--------------|-------------|---------  
High-level API| Keras       | PyTorch

**Låg-nivå API:er** i båda ramverken låter dig bygga så kallade **beräkningsgrafer**. Denna graf definierar hur man beräknar output (vanligtvis förlustfunktionen) med givna indata-parametrar, och kan skickas för beräkning på GPU om det finns tillgängligt. Det finns funktioner för att differentiera denna beräkningsgraf och beräkna gradienter, som sedan kan användas för att optimera modellparametrar.

**Hög-nivå API:er** betraktar neurala nätverk som en **sekvens av lager**, och gör konstruktionen av de flesta neurala nätverk mycket enklare. Att träna modellen kräver vanligtvis att man förbereder data och sedan anropar en `fit`-funktion för att utföra träningen.

Hög-nivå API:et låter dig snabbt bygga typiska neurala nätverk utan att behöva oroa dig för många detaljer. Samtidigt erbjuder låg-nivå API:et mycket mer kontroll över träningsprocessen, och används därför ofta inom forskning när man arbetar med nya neurala nätverksarkitekturer.

Det är också viktigt att förstå att du kan använda båda API:erna tillsammans, t.ex. kan du utveckla din egen nätverkslagerarkitektur med låg-nivå API och sedan använda den i ett större nätverk som konstrueras och tränas med hög-nivå API. Eller så kan du definiera ett nätverk med hög-nivå API som en sekvens av lager och sedan använda din egen låg-nivå träningsslinga för optimering. Båda API:erna använder samma grundläggande koncept och är designade för att fungera bra tillsammans.

## Learning

I denna kurs erbjuder vi det mesta av innehållet både för PyTorch och TensorFlow. Du kan välja ditt föredragna ramverk och bara gå igenom motsvarande notebooks. Om du är osäker på vilket ramverk du ska välja, läs några diskussioner på internet om **PyTorch vs. TensorFlow**. Du kan också titta på båda ramverken för att få en bättre förståelse.

Där det är möjligt kommer vi att använda hög-nivå API för enkelhetens skull. Men vi anser att det är viktigt att förstå hur neurala nätverk fungerar från grunden, så i början börjar vi med att arbeta med låg-nivå API och tensorer. Om du däremot vill komma igång snabbt och inte vill lägga mycket tid på att lära dig dessa detaljer, kan du hoppa över dem och gå direkt till hög-nivå API-notebooks.

## ✍️ Övningar: Frameworks

Fortsätt din inlärning i följande notebooks:

Low-Level API | TensorFlow+Keras Notebook | PyTorch  
--------------|----------------------------|---------  
High-level API| Keras                      | *PyTorch Lightning*

Efter att ha behärskat ramverken, låt oss sammanfatta begreppet överanpassning.

# Overfitting

Överanpassning är ett extremt viktigt begrepp inom maskininlärning, och det är mycket viktigt att förstå det rätt!

Tänk på följande problem med att approximera 5 punkter (representerade av `x` på graferna nedan):

!linear | overfit  
-------------------------|--------------------------  
**Linjär modell, 2 parametrar** | **Icke-linjär modell, 7 parametrar**  
Träningsfel = 5.3 | Träningsfel = 0  
Valideringsfel = 5.1 | Valideringsfel = 20

* Till vänster ser vi en bra rak linje-approximation. Eftersom antalet parametrar är lämpligt, fångar modellen rätt mönster bakom punktfördelningen.
* Till höger är modellen för kraftfull. Eftersom vi bara har 5 punkter och modellen har 7 parametrar, kan den anpassa sig så att den går igenom alla punkter, vilket gör träningsfelet till 0. Detta hindrar dock modellen från att förstå det korrekta mönstret bakom datan, vilket gör valideringsfelet mycket högt.

Det är mycket viktigt att hitta en rätt balans mellan modellens komplexitet (antal parametrar) och antalet träningsdata.

## Varför överanpassning uppstår

  * Inte tillräckligt med träningsdata  
  * För kraftfull modell  
  * För mycket brus i indata

## Hur man upptäcker överanpassning

Som du kan se i grafen ovan kan överanpassning upptäckas genom mycket lågt träningsfel och högt valideringsfel. Normalt under träning ser vi både tränings- och valideringsfel minska, men vid en viss punkt kan valideringsfelet sluta minska och börja öka. Detta är ett tecken på överanpassning och en indikation på att vi förmodligen bör stoppa träningen vid denna punkt (eller åtminstone ta en snapshot av modellen).

overfitting

## Hur man förhindrar överanpassning

Om du ser att överanpassning uppstår kan du göra något av följande:

 * Öka mängden träningsdata  
 * Minska modellens komplexitet  
 * Använd någon regulariseringsteknik, som Dropout, vilket vi kommer att titta på senare.

## Överanpassning och Bias-Variance Tradeoff

Överanpassning är egentligen ett fall av ett mer generellt problem inom statistik som kallas Bias-Variance Tradeoff. Om vi betraktar möjliga felkällor i vår modell kan vi se två typer av fel:

* **Bias-fel** orsakas av att vår algoritm inte kan fånga relationen i träningsdata korrekt. Det kan bero på att modellen inte är tillräckligt kraftfull (**underanpassning**).
* **Variansfel**, som orsakas av att modellen approximera brus i indata istället för meningsfulla samband (**överanpassning**).

Under träning minskar bias-felet (eftersom modellen lär sig att approximera datan), medan variansfelet ökar. Det är viktigt att stoppa träningen – antingen manuellt (när vi upptäcker överanpassning) eller automatiskt (genom att införa regularisering) – för att förhindra överanpassning.

## Slutsats

I denna lektion har du lärt dig om skillnaderna mellan de olika API:erna för de två mest populära AI-ramverken, TensorFlow och PyTorch. Dessutom har du lärt dig om ett mycket viktigt ämne, överanpassning.

## 🚀 Utmaning

I de medföljande notebooks hittar du 'uppgifter' längst ner; arbeta igenom notebooks och slutför uppgifterna.

## Review & Självstudier

Gör lite research om följande ämnen:

- TensorFlow  
- PyTorch  
- Overfitting

Ställ dig själv följande frågor:

- Vad är skillnaden mellan TensorFlow och PyTorch?  
- Vad är skillnaden mellan överanpassning och underanpassning?

## Uppgift

I detta labb ska du lösa två klassificeringsproblem med hjälp av enkla och flerskiktade fullt anslutna nätverk med PyTorch eller TensorFlow.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.