<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:41:16+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "sv"
}
-->
# Använda Generativ AI Ansvarsfullt

[![Använda Generativ AI Ansvarsfullt](../../../translated_images/03-lesson-banner.63a265562d8a9f9230f5c636ab303a0137d11420177528f475b0a05c5f6a9ff9.sv.png)](https://aka.ms/gen-ai-lesson3-gh?WT.mc_id=academic-105485-koreyst)

> _Klicka på bilden ovan för att se videon av denna lektion_

Det är lätt att fascineras av AI och generativ AI i synnerhet, men du behöver överväga hur du skulle använda det ansvarsfullt. Du behöver tänka på saker som hur du säkerställer att output är rättvis, icke-skadlig och mer. Detta kapitel syftar till att ge dig den nämnda kontexten, vad du bör överväga och hur du kan ta aktiva steg för att förbättra din AI-användning.

## Introduktion

Denna lektion kommer att täcka:

- Varför du bör prioritera Ansvarsfull AI när du bygger Generativa AI-applikationer.
- Grundprinciper för Ansvarsfull AI och hur de relaterar till Generativ AI.
- Hur du omsätter dessa principer för Ansvarsfull AI i praktiken genom strategi och verktyg.

## Inlärningsmål

Efter att ha avslutat denna lektion kommer du att veta:

- Vikten av Ansvarsfull AI när du bygger Generativa AI-applikationer.
- När du ska tänka och tillämpa de grundläggande principerna för Ansvarsfull AI när du bygger Generativa AI-applikationer.
- Vilka verktyg och strategier som finns tillgängliga för att omsätta konceptet Ansvarsfull AI i praktiken.

## Principer för Ansvarsfull AI

Entusiasmen för Generativ AI har aldrig varit större. Denna entusiasm har fört med sig många nya utvecklare, uppmärksamhet och finansiering till detta område. Även om detta är mycket positivt för alla som vill bygga produkter och företag med Generativ AI, är det också viktigt att vi fortsätter ansvarsfullt.

Under hela denna kurs fokuserar vi på att bygga vår startup och vår AI-utbildningsprodukt. Vi kommer att använda principerna för Ansvarsfull AI: Rättvisa, Inkluderande, Pålitlighet/Säkerhet, Säkerhet & Integritet, Transparens och Ansvarighet. Med dessa principer kommer vi att utforska hur de relaterar till vår användning av Generativ AI i våra produkter.

## Varför Ska Du Prioritera Ansvarsfull AI

När du bygger en produkt, leder ett människocentrerat förhållningssätt med användarens bästa intresse i åtanke till de bästa resultaten.

Det unika med Generativ AI är dess kraft att skapa hjälpsamma svar, information, vägledning och innehåll för användare. Detta kan göras utan många manuella steg vilket kan leda till mycket imponerande resultat. Utan ordentlig planering och strategier kan det tyvärr också leda till skadliga resultat för dina användare, din produkt och samhället som helhet.

Låt oss titta på några (men inte alla) av dessa potentiellt skadliga resultat:

### Hallucinationer

Hallucinationer är en term som används för att beskriva när en LLM producerar innehåll som antingen är helt nonsens eller något vi vet är faktamässigt felaktigt baserat på andra informationskällor.

Låt oss ta ett exempel där vi bygger en funktion för vår startup som tillåter studenter att ställa historiska frågor till en modell. En student ställer frågan `Who was the sole survivor of Titanic?`

Modellen ger ett svar som det nedan:

![Uppmaning som säger "Vem var den enda överlevande från Titanic"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Källa: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Detta är ett mycket självsäkert och grundligt svar. Tyvärr är det felaktigt. Även med en minimal mängd forskning skulle man upptäcka att det fanns mer än en överlevande från Titanic-katastrofen. För en student som just börjat forska i detta ämne kan detta svar vara övertygande nog att inte ifrågasättas och behandlas som fakta. Konsekvenserna av detta kan leda till att AI-systemet blir opålitligt och negativt påverkar vår startups rykte.

Med varje iteration av en given LLM har vi sett prestandaförbättringar kring att minimera hallucinationer. Även med denna förbättring behöver vi som applikationsbyggare och användare fortfarande vara medvetna om dessa begränsningar.

### Skadligt Innehåll

Vi täckte i den tidigare sektionen när en LLM producerar felaktiga eller nonsensiska svar. En annan risk vi behöver vara medvetna om är när en modell svarar med skadligt innehåll.

Skadligt innehåll kan definieras som:

- Att ge instruktioner eller uppmuntra till självskada eller skada mot vissa grupper.
- Hatiskt eller nedsättande innehåll.
- Att vägleda planering av någon typ av attack eller våldsamma handlingar.
- Att ge instruktioner om hur man hittar olagligt innehåll eller begår olagliga handlingar.
- Att visa sexuellt explicit innehåll.

För vår startup vill vi se till att vi har rätt verktyg och strategier på plats för att förhindra att denna typ av innehåll ses av studenter.

### Brist på Rättvisa

Rättvisa definieras som “att säkerställa att ett AI-system är fritt från bias och diskriminering och att det behandlar alla rättvist och jämlikt.” I världen av Generativ AI vill vi säkerställa att exkluderande världsbilder av marginaliserade grupper inte förstärks av modellens output.

Dessa typer av outputs är inte bara destruktiva för att bygga positiva produktupplevelser för våra användare, utan de orsakar också ytterligare samhällelig skada. Som applikationsbyggare bör vi alltid hålla en bred och diversifierad användarbas i åtanke när vi bygger lösningar med Generativ AI.

## Hur Man Använder Generativ AI Ansvarsfullt

Nu när vi har identifierat vikten av Ansvarsfull Generativ AI, låt oss titta på 4 steg vi kan ta för att bygga våra AI-lösningar ansvarsfullt:

![Minska Cykel](../../../translated_images/mitigate-cycle.f82610b2048bda5a84aaa3a3cb2cda8b35fe614a7269743fdc63cbc2cbb8f20f.sv.png)

### Mäta Potentiella Skador

I mjukvarutestning testar vi de förväntade handlingarna av en användare på en applikation. På samma sätt är det bra att testa en diversifierad uppsättning uppmaningar som användare mest troligt kommer att använda för att mäta potentiell skada.

Eftersom vår startup bygger en utbildningsprodukt skulle det vara bra att förbereda en lista över utbildningsrelaterade uppmaningar. Detta kan vara för att täcka ett visst ämne, historiska fakta och uppmaningar om studentlivet.

### Minska Potentiella Skador

Det är nu dags att hitta sätt där vi kan förhindra eller begränsa den potentiella skada som orsakas av modellen och dess svar. Vi kan se på detta i 4 olika lager:

![Minskning Lager](../../../translated_images/mitigation-layers.db2d802e3affb2f49681cf8ae39e8f1a67ff1ce29c3f1099c96948a841d62037.sv.png)

- **Modell**. Välja rätt modell för rätt användningsområde. Större och mer komplexa modeller som GPT-4 kan orsaka mer risk för skadligt innehåll när de tillämpas på mindre och mer specifika användningsområden. Att använda din träningsdata för att finjustera minskar också risken för skadligt innehåll.

- **Säkerhetssystem**. Ett säkerhetssystem är en uppsättning verktyg och konfigurationer på plattformen som serverar modellen som hjälper till att minska skada. Ett exempel på detta är innehållsfiltreringssystemet på Azure OpenAI-tjänsten. System bör också upptäcka jailbreak-attacker och oönskad aktivitet som förfrågningar från bots.

- **Metaprompt**. Metaprompts och grundning är sätt vi kan styra eller begränsa modellen baserat på vissa beteenden och information. Detta kan vara att använda systeminputs för att definiera vissa gränser för modellen. Dessutom att tillhandahålla outputs som är mer relevanta för systemets omfattning eller domän.

Det kan också vara att använda tekniker som Retrieval Augmented Generation (RAG) för att få modellen att endast hämta information från ett urval av betrodda källor. Det finns en lektion senare i denna kurs för [att bygga sökapplikationer](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Användarupplevelse**. Det sista lagret är där användaren interagerar direkt med modellen genom vår applikationsgränssnitt på något sätt. På detta sätt kan vi designa UI/UX för att begränsa användaren på de typer av inputs de kan skicka till modellen samt text eller bilder som visas för användaren. När vi distribuerar AI-applikationen måste vi också vara transparenta om vad vår Generativa AI-applikation kan och inte kan göra.

Vi har en hel lektion dedikerad till [Designa UX för AI-applikationer](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Utvärdera modell**. Att arbeta med LLMs kan vara utmanande eftersom vi inte alltid har kontroll över datan som modellen tränades på. Oavsett bör vi alltid utvärdera modellens prestanda och outputs. Det är fortfarande viktigt att mäta modellens noggrannhet, likhet, grundlighet och relevans av output. Detta hjälper till att ge transparens och förtroende till intressenter och användare.

### Driva en Ansvarsfull Generativ AI-lösning

Att bygga en operativ praxis kring dina AI-applikationer är det sista steget. Detta inkluderar att samarbeta med andra delar av vår startup som Juridik och Säkerhet för att säkerställa att vi följer alla regulatoriska policyer. Innan lansering vill vi också bygga planer kring leverans, hantering av incidenter och återställning för att förhindra någon skada för våra användare från att växa.

## Verktyg

Även om arbetet med att utveckla Ansvarsfull AI-lösningar kan verka mycket, är det arbete som är väl värt ansträngningen. När området för Generativ AI växer, kommer fler verktyg för att hjälpa utvecklare att effektivt integrera ansvar i sina arbetsflöden att mogna. Till exempel kan [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) hjälpa till att upptäcka skadligt innehåll och bilder via en API-förfrågan.

## Kunskapskontroll

Vad är några saker du behöver bry dig om för att säkerställa ansvarsfull AI-användning?

1. Att svaret är korrekt.
1. Skadlig användning, att AI inte används för kriminella syften.
1. Att säkerställa att AI är fri från bias och diskriminering.

A: 2 och 3 är korrekta. Ansvarsfull AI hjälper dig att överväga hur du kan minska skadliga effekter och bias och mer.

## 🚀 Utmaning

Läs om [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) och se vad du kan anta för din användning.

## Bra Jobbat, Fortsätt Din Inlärning

Efter att ha avslutat denna lektion, kolla in vår [Generativ AI Inlärningssamling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din Generativ AI-kunskap!

Gå vidare till Lektion 4 där vi kommer att titta på [Grunderna i Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller oriktigheter. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller misstolkningar som uppstår vid användning av denna översättning.