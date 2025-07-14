<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-07-09T14:58:42+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "sv"
}
-->
# Designa UX för AI-applikationer

[![Designa UX för AI-applikationer](../../../translated_images/12-lesson-banner.c53c3c7c802e8f563953ce388f6a987ca493472c724d924b060be470951c53c8.sv.png)](https://aka.ms/gen-ai-lesson12-gh?WT.mc_id=academic-105485-koreyst)

> _(Klicka på bilden ovan för att se videon till denna lektion)_

Användarupplevelse är en mycket viktig aspekt när man bygger appar. Användare behöver kunna använda din app på ett effektivt sätt för att utföra uppgifter. Att vara effektiv är en sak, men du behöver också designa appar så att de kan användas av alla, för att göra dem _tillgängliga_. Detta kapitel fokuserar på detta område så att du förhoppningsvis slutar med att designa en app som människor kan och vill använda.

## Introduktion

Användarupplevelse är hur en användare interagerar med och använder en specifik produkt eller tjänst, vare sig det är ett system, verktyg eller design. När man utvecklar AI-applikationer fokuserar utvecklare inte bara på att säkerställa att användarupplevelsen är effektiv utan också etisk. I denna lektion går vi igenom hur man bygger artificiell intelligens (AI)-applikationer som möter användarnas behov.

Lektionens innehåll omfattar följande områden:

- Introduktion till användarupplevelse och förståelse för användarbehov
- Designa AI-applikationer för förtroende och transparens
- Designa AI-applikationer för samarbete och återkoppling

## Lärandemål

Efter att ha genomgått denna lektion kommer du att kunna:

- Förstå hur man bygger AI-applikationer som uppfyller användarnas behov.
- Designa AI-applikationer som främjar förtroende och samarbete.

### Förkunskaper

Ta dig tid att läsa mer om [användarupplevelse och design thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introduktion till användarupplevelse och förståelse för användarbehov

I vårt fiktiva utbildningsstartup har vi två huvudsakliga användare, lärare och elever. Var och en av dessa användare har unika behov. En användarcentrerad design prioriterar användaren och säkerställer att produkterna är relevanta och fördelaktiga för dem de är avsedda för.

Applikationen bör vara **användbar, pålitlig, tillgänglig och trevlig** för att ge en bra användarupplevelse.

### Användbarhet

Att vara användbar innebär att applikationen har funktioner som matchar dess avsedda syfte, som att automatisera betygsättningsprocessen eller generera flashcards för repetition. En applikation som automatiserar betygsättningen bör kunna tilldela poäng till elevernas arbete på ett korrekt och effektivt sätt baserat på fördefinierade kriterier. På samma sätt bör en applikation som genererar repetitionsflashcards kunna skapa relevanta och varierade frågor baserat på dess data.

### Pålitlighet

Att vara pålitlig innebär att applikationen kan utföra sin uppgift konsekvent och utan fel. Men AI, precis som människor, är inte perfekt och kan göra misstag. Applikationerna kan stöta på fel eller oväntade situationer som kräver mänsklig inblandning eller korrigering. Hur hanterar du fel? I den sista delen av denna lektion går vi igenom hur AI-system och applikationer är designade för samarbete och återkoppling.

### Tillgänglighet

Att vara tillgänglig innebär att utöka användarupplevelsen till användare med olika förmågor, inklusive personer med funktionsnedsättningar, så att ingen lämnas utanför. Genom att följa riktlinjer och principer för tillgänglighet blir AI-lösningar mer inkluderande, användbara och fördelaktiga för alla användare.

### Trevlig

Att vara trevlig innebär att applikationen är rolig och behaglig att använda. En tilltalande användarupplevelse kan ha en positiv effekt på användaren, uppmuntra dem att återvända till applikationen och öka företagets intäkter.

![bild som illustrerar UX-överväganden i AI](../../../translated_images/uxinai.d5b4ed690f5cefff0c53ffcc01b480cdc1828402e1fdbc980490013a3c50935a.sv.png)

Inte alla utmaningar kan lösas med AI. AI kommer in för att förstärka din användarupplevelse, vare sig det handlar om att automatisera manuella uppgifter eller anpassa användarupplevelser.

## Designa AI-applikationer för förtroende och transparens

Att bygga förtroende är avgörande när man designar AI-applikationer. Förtroende säkerställer att en användare är säker på att applikationen kommer att utföra arbetet, leverera resultat konsekvent och att resultaten är vad användaren behöver. En risk i detta område är misstro och överförtroende. Misstro uppstår när en användare har lite eller inget förtroende för ett AI-system, vilket leder till att användaren avvisar din applikation. Överförtroende uppstår när en användare överskattar kapaciteten hos ett AI-system, vilket leder till att användare litar för mycket på AI-systemet. Till exempel kan ett automatiserat betygssystem vid överförtroende leda till att läraren inte granskar vissa uppgifter för att säkerställa att betygssystemet fungerar korrekt. Detta kan resultera i orättvisa eller felaktiga betyg för eleverna, eller missade möjligheter till återkoppling och förbättring.

Två sätt att säkerställa att förtroende står i centrum för designen är förklarbarhet och kontroll.

### Förklarbarhet

När AI hjälper till att informera beslut, som att förmedla kunskap till framtida generationer, är det avgörande för lärare och föräldrar att förstå hur AI-beslut fattas. Detta är förklarbarhet – att förstå hur AI-applikationer fattar beslut. Design för förklarbarhet inkluderar att lägga till exempel på vad en AI-applikation kan göra. Till exempel, istället för "Kom igång med AI-lärare", kan systemet använda: "Sammanfatta dina anteckningar för enklare repetition med AI."

![en appstartsida med tydlig illustration av förklarbarhet i AI-applikationer](../../../translated_images/explanability-in-ai.134426a96b498fbfdc80c75ae0090aedc0fc97424ae0734fccf7fb00a59a20d9.sv.png)

Ett annat exempel är hur AI använder användar- och personuppgifter. Till exempel kan en användare med personan studenten ha begränsningar baserat på sin persona. AI:n kanske inte kan avslöja svar på frågor men kan hjälpa användaren att tänka igenom hur de kan lösa ett problem.

![AI som svarar på frågor baserat på persona](../../../translated_images/solving-questions.b7dea1604de0cbd2e9c5fa00b1a68a0ed77178a035b94b9213196b9d125d0be8.sv.png)

En sista viktig del av förklarbarhet är att förenkla förklaringarna. Elever och lärare är kanske inte AI-experter, därför bör förklaringar av vad applikationen kan eller inte kan göra vara förenklade och lätta att förstå.

![förenklade förklaringar om AI:s kapabiliteter](../../../translated_images/simplified-explanations.4679508a406c3621fa22bad4673e717fbff02f8b8d58afcab8cb6f1aa893a82f.sv.png)

### Kontroll

Generativ AI skapar ett samarbete mellan AI och användaren, där till exempel en användare kan ändra prompts för olika resultat. Dessutom, när ett resultat har genererats, bör användare kunna modifiera resultatet för att få en känsla av kontroll. Till exempel, när du använder Bing kan du anpassa din prompt baserat på format, ton och längd. Dessutom kan du göra ändringar i ditt resultat och modifiera det som visas nedan:

![Bing-sökresultat med alternativ för att ändra prompt och resultat](../../../translated_images/bing1.293ae8527dbe2789b675c8591c9fb3cb1aa2ada75c2877f9aa9edc059f7a8b1c.sv.png)

En annan funktion i Bing som ger användaren kontroll över applikationen är möjligheten att välja att delta eller avstå från den data som AI använder. För en skolapplikation kan en elev vilja använda sina anteckningar samt lärarens resurser som repetitionsmaterial.

![Bing-sökresultat med alternativ för att ändra prompt och resultat](../../../translated_images/bing2.309f4845528a88c28c1c9739fb61d91fd993dc35ebe6fc92c66791fb04fceb4d.sv.png)

> När du designar AI-applikationer är avsiktlighet nyckeln för att säkerställa att användare inte överskattar AI och sätter orealistiska förväntningar på dess kapabiliteter. Ett sätt att göra detta är att skapa friktion mellan prompts och resultat. Påminn användaren om att detta är AI och inte en medmänniska.

## Designa AI-applikationer för samarbete och återkoppling

Som nämnts tidigare skapar generativ AI ett samarbete mellan användaren och AI. De flesta interaktioner består av att användaren matar in en prompt och AI:n genererar ett resultat. Vad händer om resultatet är felaktigt? Hur hanterar applikationen fel om de uppstår? Skyller AI på användaren eller tar den tid att förklara felet?

AI-applikationer bör byggas för att ta emot och ge återkoppling. Detta hjälper inte bara AI-systemet att förbättras utan bygger också förtroende hos användarna. En återkopplingsloop bör ingå i designen, ett exempel kan vara en enkel tumme upp eller ner på resultatet.

Ett annat sätt att hantera detta är att tydligt kommunicera systemets kapabiliteter och begränsningar. När en användare gör ett fel genom att begära något utanför AI:s kapabiliteter bör det också finnas ett sätt att hantera detta, som visas nedan.

![Ge återkoppling och hantera fel](../../../translated_images/feedback-loops.7955c134429a94663443ad74d59044f8dc4ce354577f5b79b4bd2533f2cafc6f.sv.png)

Systemfel är vanliga i applikationer där användaren kan behöva hjälp med information utanför AI:s räckvidd eller där applikationen kan ha en gräns för hur många frågor/ämnen en användare kan generera sammanfattningar för. Till exempel kan en AI-applikation som är tränad med data inom begränsade ämnen, till exempel historia och matematik, kanske inte kunna hantera frågor om geografi. För att mildra detta kan AI-systemet ge ett svar som: "Tyvärr, vår produkt är tränad med data inom följande ämnen....., jag kan inte svara på frågan du ställde."

AI-applikationer är inte perfekta, därför kommer de att göra misstag. När du designar dina applikationer bör du se till att skapa utrymme för återkoppling från användare och felhantering på ett sätt som är enkelt och lätt att förklara.

## Uppgift

Ta vilka AI-appar du än har byggt hittills och överväg att implementera följande steg i din app:

- **Trevlig:** Fundera på hur du kan göra din app mer trevlig. Lägger du till förklaringar överallt? Uppmuntrar du användaren att utforska? Hur formulerar du dina felmeddelanden?

- **Användbarhet:** Bygger du en webbapp? Se till att din app är navigerbar både med mus och tangentbord.

- **Förtroende och transparens:** Lita inte helt på AI och dess resultat, fundera på hur du kan lägga till en människa i processen för att verifiera resultatet. Överväg och implementera också andra sätt att uppnå förtroende och transparens.

- **Kontroll:** Ge användaren kontroll över den data de tillhandahåller applikationen. Implementera ett sätt för användare att välja att delta eller avstå från datainsamling i AI-applikationen.

## Fortsätt din lärande!

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om Generativ AI!

Gå vidare till Lektion 13, där vi tittar på hur man [säkrar AI-applikationer](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.