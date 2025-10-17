<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78bbeed50fd4dc9fdee931f5daf98cb3",
  "translation_date": "2025-10-17T18:58:36+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "sv"
}
-->
# Designa användarupplevelse för AI-applikationer

[![Designa användarupplevelse för AI-applikationer](../../../translated_images/12-lesson-banner.c53c3c7c802e8f563953ce388f6a987ca493472c724d924b060be470951c53c8.sv.png)](https://youtu.be/VKbCejSICA8?si=MKj7GQYHfXRZyWW6)

> _(Klicka på bilden ovan för att se videon till denna lektion)_

Användarupplevelse är en mycket viktig aspekt av att bygga appar. Användare måste kunna använda din app på ett effektivt sätt för att utföra uppgifter. Att vara effektiv är en sak, men du måste också designa appar så att de kan användas av alla, för att göra dem _tillgängliga_. Detta kapitel kommer att fokusera på detta område så att du förhoppningsvis kan designa en app som människor både kan och vill använda.

## Introduktion

Användarupplevelse handlar om hur en användare interagerar med och använder en specifik produkt eller tjänst, vare sig det är ett system, ett verktyg eller en design. När man utvecklar AI-applikationer fokuserar utvecklare inte bara på att säkerställa att användarupplevelsen är effektiv utan också etisk. I denna lektion går vi igenom hur man bygger artificiella intelligens-applikationer (AI) som möter användarnas behov.

Lektionens innehåll:

- Introduktion till användarupplevelse och förståelse för användarbehov
- Designa AI-applikationer för förtroende och transparens
- Designa AI-applikationer för samarbete och feedback

## Lärandemål

Efter att ha genomgått denna lektion kommer du att kunna:

- Förstå hur man bygger AI-applikationer som möter användarnas behov.
- Designa AI-applikationer som främjar förtroende och samarbete.

### Förkunskaper

Ta dig tid att läsa mer om [användarupplevelse och design thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introduktion till användarupplevelse och förståelse för användarbehov

I vårt fiktiva utbildningsföretag har vi två primära användare, lärare och elever. Var och en av dessa användare har unika behov. En användarcentrerad design prioriterar användaren och säkerställer att produkterna är relevanta och fördelaktiga för dem de är avsedda för.

Applikationen bör vara **användbar, pålitlig, tillgänglig och trevlig** för att ge en bra användarupplevelse.

### Användbarhet

Att vara användbar innebär att applikationen har funktioner som matchar dess avsedda syfte, såsom att automatisera betygsättningsprocessen eller generera flashcards för repetition. En applikation som automatiserar betygsättningsprocessen bör kunna tilldela poäng till elevers arbete korrekt och effektivt baserat på fördefinierade kriterier. På samma sätt bör en applikation som genererar repetitionskort kunna skapa relevanta och varierade frågor baserat på sin data.

### Pålitlighet

Att vara pålitlig innebär att applikationen kan utföra sina uppgifter konsekvent och utan fel. Men AI, precis som människor, är inte perfekt och kan vara benägen att göra misstag. Applikationer kan stöta på fel eller oväntade situationer som kräver mänsklig inblandning eller korrigering. Hur hanterar du fel? I den sista delen av denna lektion kommer vi att gå igenom hur AI-system och applikationer designas för samarbete och feedback.

### Tillgänglighet

Att vara tillgänglig innebär att utöka användarupplevelsen till användare med olika förmågor, inklusive de med funktionsnedsättningar, och säkerställa att ingen lämnas utanför. Genom att följa riktlinjer och principer för tillgänglighet blir AI-lösningar mer inkluderande, användbara och fördelaktiga för alla användare.

### Trevlig

Att vara trevlig innebär att applikationen är behaglig att använda. En tilltalande användarupplevelse kan ha en positiv inverkan på användaren, uppmuntra dem att återvända till applikationen och öka företagets intäkter.

![bild som illustrerar UX-överväganden i AI](../../../translated_images/uxinai.d5b4ed690f5cefff0c53ffcc01b480cdc1828402e1fdbc980490013a3c50935a.sv.png)

Inte alla utmaningar kan lösas med AI. AI används för att förstärka användarupplevelsen, vare sig det handlar om att automatisera manuella uppgifter eller att anpassa användarupplevelser.

## Designa AI-applikationer för förtroende och transparens

Att bygga förtroende är avgörande när man designar AI-applikationer. Förtroende säkerställer att en användare är säker på att applikationen kommer att utföra arbetet, leverera resultat konsekvent och att resultaten är vad användaren behöver. En risk i detta område är misstro och överdrivet förtroende. Misstro uppstår när en användare har lite eller inget förtroende för ett AI-system, vilket leder till att användaren avvisar din applikation. Överdrivet förtroende uppstår när en användare överskattar kapaciteten hos ett AI-system, vilket leder till att användare litar för mycket på AI-systemet. Till exempel kan ett automatiserat betygsättningssystem i fallet med överdrivet förtroende leda till att läraren inte granskar vissa av proven för att säkerställa att betygsättningssystemet fungerar korrekt. Detta kan resultera i orättvisa eller felaktiga betyg för eleverna, eller missade möjligheter till feedback och förbättring.

Två sätt att säkerställa att förtroende är centralt i designen är förklarbarhet och kontroll.

### Förklarbarhet

När AI hjälper till att fatta beslut, som att förmedla kunskap till framtida generationer, är det avgörande för lärare och föräldrar att förstå hur AI-beslut fattas. Detta är förklarbarhet - att förstå hur AI-applikationer fattar beslut. Att designa för förklarbarhet innebär att lägga till detaljer som belyser hur AI kom fram till resultatet. Publiken måste vara medveten om att resultatet genereras av AI och inte av en människa. Till exempel, istället för att säga "Börja chatta med din handledare nu", säg "Använd AI-handledare som anpassar sig till dina behov och hjälper dig att lära dig i din egen takt."

![en app-landningssida med tydlig illustration av förklarbarhet i AI-applikationer](../../../translated_images/explanability-in-ai.134426a96b498fbfdc80c75ae0090aedc0fc97424ae0734fccf7fb00a59a20d9.sv.png)

Ett annat exempel är hur AI använder användar- och personuppgifter. Till exempel kan en användare med personan student ha begränsningar baserat på sin persona. AI:n kanske inte kan avslöja svar på frågor men kan hjälpa användaren att tänka igenom hur de kan lösa ett problem.

![AI svarar på frågor baserat på persona](../../../translated_images/solving-questions.b7dea1604de0cbd2e9c5fa00b1a68a0ed77178a035b94b9213196b9d125d0be8.sv.png)

En sista viktig del av förklarbarhet är förenkling av förklaringar. Elever och lärare kanske inte är experter på AI, därför bör förklaringar av vad applikationen kan eller inte kan göra förenklas och vara lätta att förstå.

![förenklade förklaringar av AI-funktioner](../../../translated_images/simplified-explanations.4679508a406c3621fa22bad4673e717fbff02f8b8d58afcab8cb6f1aa893a82f.sv.png)

### Kontroll

Generativ AI skapar ett samarbete mellan AI och användaren, där användaren till exempel kan ändra uppmaningar för olika resultat. Dessutom, när ett resultat genereras, bör användare kunna ändra resultaten och därmed få en känsla av kontroll. Till exempel, när du använder Bing, kan du anpassa din uppmaning baserat på format, ton och längd. Dessutom kan du göra ändringar i ditt resultat och modifiera det som visas nedan:

![Bing-sökresultat med alternativ för att ändra uppmaning och resultat](../../../translated_images/bing1.293ae8527dbe2789b675c8591c9fb3cb1aa2ada75c2877f9aa9edc059f7a8b1c.sv.png)

En annan funktion i Bing som ger användaren kontroll över applikationen är möjligheten att välja att delta eller avstå från den data som AI använder. För en skolapplikation kanske en elev vill använda sina anteckningar samt lärarens resurser som repetitionsmaterial.

![Bing-sökresultat med alternativ för att ändra uppmaning och resultat](../../../translated_images/bing2.309f4845528a88c28c1c9739fb61d91fd993dc35ebe6fc92c66791fb04fceb4d.sv.png)

> När du designar AI-applikationer är det viktigt att vara medveten om att användare inte ska överdriva sitt förtroende för AI och dess kapacitet. Ett sätt att göra detta är att skapa en viss friktion mellan uppmaningarna och resultaten. Påminn användaren om att detta är AI och inte en annan människa.

## Designa AI-applikationer för samarbete och feedback

Som tidigare nämnts skapar generativ AI ett samarbete mellan användaren och AI. De flesta interaktioner sker genom att en användare matar in en uppmaning och AI genererar ett resultat. Vad händer om resultatet är felaktigt? Hur hanterar applikationen fel om de uppstår? Skyller AI på användaren eller tar den sig tid att förklara felet?

AI-applikationer bör vara utformade för att ta emot och ge feedback. Detta hjälper inte bara AI-systemet att förbättras utan bygger också förtroende hos användarna. En feedback-loop bör inkluderas i designen, ett exempel kan vara en enkel tumme upp eller ner på resultatet.

Ett annat sätt att hantera detta är att tydligt kommunicera systemets kapacitet och begränsningar. När en användare gör ett fel genom att begära något utanför AI:s kapacitet, bör det också finnas ett sätt att hantera detta, som visas nedan.

![Ge feedback och hantera fel](../../../translated_images/feedback-loops.7955c134429a94663443ad74d59044f8dc4ce354577f5b79b4bd2533f2cafc6f.sv.png)

Systemfel är vanliga i applikationer där användaren kan behöva hjälp med information utanför AI:s räckvidd eller där applikationen kan ha en gräns för hur många frågor/ämnen en användare kan generera sammanfattningar för. Till exempel kan en AI-applikation som är tränad med data om begränsade ämnen, som historia och matematik, kanske inte kunna hantera frågor om geografi. För att mildra detta kan AI-systemet ge ett svar som: "Tyvärr, vår produkt har tränats med data inom följande ämnen....., jag kan inte svara på frågan du ställde."

AI-applikationer är inte perfekta, därför är de benägna att göra misstag. När du designar dina applikationer bör du säkerställa att du skapar utrymme för feedback från användare och felhantering på ett sätt som är enkelt och lätt att förstå.

## Uppgift

Ta en av de AI-appar du har byggt hittills och överväg att implementera följande steg i din app:

- **Trevlig:** Fundera på hur du kan göra din app mer trevlig. Lägger du till förklaringar överallt? Uppmuntrar du användaren att utforska? Hur formulerar du dina felmeddelanden?

- **Användbarhet:** Bygg en webbapp. Se till att din app kan navigeras med både mus och tangentbord.

- **Förtroende och transparens:** Lita inte helt på AI och dess resultat, fundera på hur du skulle kunna lägga till en mänsklig kontroll för att verifiera resultaten. Överväg också och implementera andra sätt att uppnå förtroende och transparens.

- **Kontroll:** Ge användaren kontroll över de data de tillhandahåller till applikationen. Implementera ett sätt för användaren att välja att delta eller avstå från datainsamling i AI-applikationen.

## Fortsätt ditt lärande!

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om generativ AI!

Gå vidare till Lektion 13, där vi kommer att titta på hur man [säkrar AI-applikationer](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.