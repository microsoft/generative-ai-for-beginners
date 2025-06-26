<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-06-25T20:24:31+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "sv"
}
-->
# Designa UX för AI-applikationer

> _(Klicka på bilden ovan för att se videon av denna lektion)_

Användarupplevelse är en mycket viktig aspekt av att bygga appar. Användare måste kunna använda din app på ett effektivt sätt för att utföra uppgifter. Att vara effektiv är en sak, men du måste också designa appar så att de kan användas av alla, för att göra dem _tillgängliga_. Detta kapitel kommer att fokusera på detta område så att du förhoppningsvis slutar med att designa en app som människor kan och vill använda.

## Introduktion

Användarupplevelse är hur en användare interagerar med och använder en specifik produkt eller tjänst, oavsett om det är ett system, verktyg eller design. När man utvecklar AI-applikationer fokuserar utvecklare inte bara på att säkerställa att användarupplevelsen är effektiv utan också etisk. I denna lektion täcker vi hur man bygger artificiell intelligens (AI) applikationer som adresserar användarbehov.

Lektionens innehåll kommer att täcka följande områden:

- Introduktion till användarupplevelse och förståelse för användarbehov
- Designa AI-applikationer för förtroende och transparens
- Designa AI-applikationer för samarbete och feedback

## Lärandemål

Efter att ha tagit denna lektion kommer du att kunna:

- Förstå hur man bygger AI-applikationer som möter användarbehoven.
- Designa AI-applikationer som främjar förtroende och samarbete.

### Förkunskapskrav

Ta dig tid och läs mer om [användarupplevelse och design thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introduktion till användarupplevelse och förståelse för användarbehov

I vår fiktiva utbildningsstart har vi två primära användare, lärare och elever. Var och en av de två användarna har unika behov. En användarcentrerad design prioriterar användaren och säkerställer att produkterna är relevanta och fördelaktiga för dem de är avsedda för.

Applikationen bör vara **användbar, pålitlig, tillgänglig och trevlig** för att ge en bra användarupplevelse.

### Användbarhet

Att vara användbar innebär att applikationen har funktionalitet som matchar dess avsedda syfte, såsom att automatisera betygsättningsprocessen eller generera flashcards för repetition. En applikation som automatiserar betygsättningsprocessen bör kunna exakt och effektivt tilldela poäng till elevers arbete baserat på fördefinierade kriterier. På samma sätt bör en applikation som genererar repetitionsflashcards kunna skapa relevanta och varierande frågor baserat på sina data.

### Tillförlitlighet

Att vara pålitlig innebär att applikationen kan utföra sin uppgift konsekvent och utan fel. Dock, precis som människor, är AI inte perfekt och kan vara benägen för fel. Applikationerna kan stöta på fel eller oväntade situationer som kräver mänsklig intervention eller korrigering. Hur hanterar du fel? I den sista delen av denna lektion kommer vi att täcka hur AI-system och applikationer är designade för samarbete och feedback.

### Tillgänglighet

Att vara tillgänglig innebär att utöka användarupplevelsen till användare med olika förmågor, inklusive de med funktionsnedsättningar, och säkerställa att ingen lämnas utanför. Genom att följa tillgänglighetsriktlinjer och principer blir AI-lösningar mer inkluderande, användbara och fördelaktiga för alla användare.

### Trevlighet

Att vara trevlig innebär att applikationen är njutbar att använda. En tilltalande användarupplevelse kan ha en positiv inverkan på användaren, uppmuntra dem att återvända till applikationen och öka företagets intäkter.

Inte alla utmaningar kan lösas med AI. AI kommer in för att komplettera din användarupplevelse, vare sig det är att automatisera manuella uppgifter eller att anpassa användarupplevelser.

## Designa AI-applikationer för förtroende och transparens

Att bygga förtroende är avgörande när man designar AI-applikationer. Förtroende säkerställer att en användare är säker på att applikationen kommer att utföra arbetet, leverera resultat konsekvent och att resultaten är vad användaren behöver. En risk i detta område är misstro och övertro. Misstro uppstår när en användare har lite eller inget förtroende för ett AI-system, vilket leder till att användaren avvisar din applikation. Övertro uppstår när en användare överskattar kapaciteten hos ett AI-system, vilket leder till att användare litar för mycket på AI-systemet. Till exempel, ett automatiserat betygssystem i fallet med övertro kan leda till att läraren inte granskar några av papperen för att säkerställa att betygssystemet fungerar bra. Detta kan resultera i orättvisa eller felaktiga betyg för eleverna, eller missade möjligheter till feedback och förbättring.

Två sätt att säkerställa att förtroendet sätts i centrum för designen är förklarbarhet och kontroll.

### Förklarbarhet

När AI hjälper till att informera beslut, såsom att ge kunskap till framtida generationer, är det viktigt för lärare och föräldrar att förstå hur AI-beslut fattas. Detta är förklarbarhet - att förstå hur AI-applikationer fattar beslut. Design för förklarbarhet inkluderar att lägga till detaljer om exempel på vad en AI-applikation kan göra. Till exempel, istället för "Kom igång med AI-lärare", kan systemet använda: "Sammanfatta dina anteckningar för enklare repetition med AI."

Ett annat exempel är hur AI använder användar- och personliga data. Till exempel kan en användare med personan student ha begränsningar baserat på deras persona. AI kanske inte kan avslöja svar på frågor men kan hjälpa till att vägleda användaren att tänka igenom hur de kan lösa ett problem.

En sista nyckeldel av förklarbarhet är förenklingen av förklaringar. Studenter och lärare kanske inte är AI-experter, därför bör förklaringar av vad applikationen kan eller inte kan göra förenklas och vara lätta att förstå.

### Kontroll

Generativ AI skapar ett samarbete mellan AI och användaren, där till exempel en användare kan ändra promptar för olika resultat. Dessutom, när ett resultat genereras, bör användare kunna ändra resultaten och ge dem en känsla av kontroll. Till exempel, när du använder Bing, kan du anpassa din prompt baserat på format, ton och längd. Dessutom kan du lägga till ändringar i ditt resultat och modifiera resultatet som visas nedan:

En annan funktion i Bing som gör det möjligt för en användare att ha kontroll över applikationen är möjligheten att välja att delta och välja bort den data AI använder. För en skolapplikation kan en student vilja använda sina anteckningar samt lärarens resurser som repetitionsmaterial.

> När du designar AI-applikationer är avsiktlighet nyckeln för att säkerställa att användare inte övertro och sätter orealistiska förväntningar på dess kapacitet. Ett sätt att göra detta är genom att skapa friktion mellan promptarna och resultaten. Påminna användaren om att detta är AI och inte en medmänniska

## Designa AI-applikationer för samarbete och feedback

Som tidigare nämnts skapar generativ AI ett samarbete mellan användaren och AI. De flesta interaktioner sker med en användare som matar in en prompt och AI som genererar ett resultat. Vad händer om resultatet är felaktigt? Hur hanterar applikationen fel om de uppstår? Skyller AI på användaren eller tar sig tid att förklara felet?

AI-applikationer bör byggas för att ta emot och ge feedback. Detta hjälper inte bara AI-systemet att förbättras utan bygger också förtroende med användarna. En feedbackloop bör inkluderas i designen, ett exempel kan vara en enkel tumme upp eller ner på resultatet.

Ett annat sätt att hantera detta är att tydligt kommunicera systemets kapacitet och begränsningar. När en användare gör ett fel genom att begära något bortom AI-kapaciteten, bör det också finnas ett sätt att hantera detta, som visas nedan.

Systemfel är vanliga med applikationer där användaren kan behöva hjälp med information utanför AI:s räckvidd eller applikationen kan ha en gräns för hur många frågor/ämnen en användare kan generera sammanfattningar. Till exempel, en AI-applikation som tränats med data om begränsade ämnen som Historia och Matematik kanske inte kan hantera frågor om Geografi. För att mildra detta kan AI-systemet ge ett svar som: "Tyvärr, vår produkt har tränats med data i följande ämnen....., jag kan inte svara på frågan du ställde."

AI-applikationer är inte perfekta, därför är de benägna att göra misstag. När du designar dina applikationer bör du säkerställa att du skapar utrymme för feedback från användare och felhantering på ett sätt som är enkelt och lättförståeligt.

## Uppgift

Ta någon AI-app du har byggt hittills, överväg att implementera följande steg i din app:

- **Trevlig:** Överväg hur du kan göra din app mer trevlig. Lägger du till förklaringar överallt? Uppmuntrar du användaren att utforska? Hur formulerar du dina felmeddelanden?

- **Användbarhet:** Bygg en webbapp. Se till att din app är navigerbar både med mus och tangentbord.

- **Förtroende och transparens:** Lita inte helt på AI och dess resultat, överväg hur du skulle lägga till en människa i processen för att verifiera resultatet. Överväg också och implementera andra sätt att uppnå förtroende och transparens.

- **Kontroll:** Ge användaren kontroll över de data de tillhandahåller applikationen. Implementera ett sätt för en användare att välja att delta och välja bort datainsamling i AI-applikationen.

## Fortsätt ditt lärande!

Efter att ha avslutat denna lektion, kolla in vår [Generativ AI-lärandekollektion](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om Generativ AI!

Gå vidare till Lektion 13, där vi kommer att titta på hur man [säkrar AI-applikationer](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.