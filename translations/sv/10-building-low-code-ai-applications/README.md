# Bygga lågkodade AI-applikationer

[![Bygga lågkodade AI-applikationer](../../../translated_images/sv/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

## Introduktion

Nu när vi har lärt oss att bygga bildgenererande applikationer, låt oss prata om lågkod. Generativ AI kan användas för flera olika områden, inklusive lågkod, men vad är lågkod och hur kan vi lägga till AI i det?

Att bygga appar och lösningar har blivit enklare för traditionella utvecklare och icke-utvecklare genom användning av lågkodutvecklingsplattformar. Lågkodutvecklingsplattformar gör det möjligt att bygga appar och lösningar med liten eller ingen kod. Detta uppnås genom att tillhandahålla en visuell utvecklingsmiljö som gör att du kan dra och släppa komponenter för att bygga appar och lösningar. Detta gör att du kan bygga appar och lösningar snabbare och med färre resurser. I denna lektion går vi på djupet om hur man använder lågkod och hur man förbättrar lågkodutveckling med AI med Power Platform.

Power Platform ger organisationer möjlighet att stärka sina team att bygga sina egna lösningar genom en intuitiv lågkod- eller inga-kod-miljö. Denna miljö förenklar processen att bygga lösningar. Med Power Platform kan lösningar byggas på dagar eller veckor istället för månader eller år. Power Platform består av fem nyckelprodukter: Power Apps, Power Automate, Power BI, Power Pages och Copilot Studio.

Denna lektion täcker:

- Introduktion till Generativ AI i Power Platform
- Introduktion till Copilot och hur man använder det
- Använda Generativ AI för att bygga appar och flöden i Power Platform
- Förstå AI-modeller i Power Platform med AI Builder
- Bygga intelligenta agenter med Microsoft Copilot Studio

## Lärandemål

Vid slutet av denna lektion kommer du att kunna:

- Förstå hur Copilot fungerar i Power Platform.

- Bygga en app för studentuppgiftsuppföljning för vår utbildningsstartup.

- Bygga ett fakturahanteringsflöde som använder AI för att extrahera information från fakturor.

- Använda bästa praxis när du använder AI-modellen Create Text med GPT.

- Förstå vad Microsoft Copilot Studio är och hur man bygger intelligenta agenter med det.

Verktygen och teknologierna du kommer att använda i denna lektion är:

- **Power Apps**, för appen Studentuppgiftsuppföljare, som tillhandahåller en lågkodsutvecklingsmiljö för att bygga appar för att spåra, hantera och interagera med data.

- **Dataverse**, för att lagra data för appen Studentuppgiftsuppföljare där Dataverse erbjuder en lågkodsdatalagringsplattform för appens data.

- **Power Automate**, för flödet för fakturahantering där du får en lågkodsutvecklingsmiljö för att bygga arbetsflöden som automatiserar fakturahanteringsprocessen.

- **AI Builder**, för AI-modellen för fakturahantering där du använder förbyggda AI-modeller för att behandla fakturorna för vår startup.

## Generativ AI i Power Platform

Att förbättra lågkodsutveckling och applikationer med generativ AI är ett nyckelområde för Power Platform. Målet är att möjliggöra för alla att bygga AI-drivna appar, webbplatser, instrumentpaneler och automatisera processer med AI, _utan att kräva någon expertis i datavetenskap_. Detta mål uppnås genom att integrera generativ AI i lågkodutvecklingsupplevelsen i Power Platform i form av Copilot och AI Builder.

### Hur fungerar detta?

Copilot är en AI-assistent som gör det möjligt att bygga Power Platform-lösningar genom att beskriva dina krav i en serie konversationssteg med naturligt språk. Du kan till exempel instruera din AI-assistent att ange vilka fält din app ska använda och den kommer skapa både appen och den underliggande datamodellen eller så kan du specificera hur du ställer in ett flöde i Power Automate.

Du kan använda Copilot-drivna funktioner som en egenskap i dina appskärmar för att låta användare upptäcka insikter genom konversationsinteraktioner.

AI Builder är en lågkods-AI-möjlighet som finns i Power Platform som gör det möjligt att använda AI-modeller för att hjälpa dig automatisera processer och förutsäga resultat. Med AI Builder kan du integrera AI i dina appar och flöden som kopplas till din data i Dataverse eller i olika molndatakällor, såsom SharePoint, OneDrive eller Azure.

Copilot finns i alla Power Platform-produkter: Power Apps, Power Automate, Power BI, Power Pages och Copilot Studio (tidigare Power Virtual Agents). AI Builder finns i Power Apps och Power Automate. I denna lektion fokuserar vi på hur man använder Copilot och AI Builder i Power Apps och Power Automate för att bygga en lösning för vår utbildningsstartup.

### Copilot i Power Apps

Som en del av Power Platform erbjuder Power Apps en lågkodsutvecklingsmiljö för att bygga appar som spårar, hanterar och interagerar med data. Det är en tjänstesvit för apputveckling med en skalbar dataplattform och möjligheten att ansluta till molntjänster och lokala databaser. Power Apps låter dig bygga appar som kan köras i webbläsare, på surfplattor och telefoner, och som kan delas med kollegor. Power Apps gör apputveckling tillgänglig med ett enkelt gränssnitt, så att varje affärsanvändare eller professionell utvecklare kan skapa anpassade appar. Apputvecklingsupplevelsen förbättras också med Generativ AI via Copilot.

Copilot AI-assistenten i Power Apps gör det möjligt att beskriva vilken typ av app du behöver och vilken information du vill att appen ska spåra, samla in eller visa. Copilot genererar sedan en responsiv Canvas-app baserad på din beskrivning. Du kan sedan anpassa appen efter dina behov. AI Copilot genererar och föreslår också en Dataverse-tabell med de fält du behöver för att lagra datan du vill spåra samt lite exempeldata. Vi kommer senare i denna lektion att titta på vad Dataverse är och hur du kan använda det i Power Apps. Sedan kan du anpassa tabellen efter dina behov med AI Copilot assistentfunktion via konversationssteg. Denna funktion är lättillgänglig från Power Apps hemskärm.

### Copilot i Power Automate

Som en del av Power Platform låter Power Automate användare skapa automatiserade arbetsflöden mellan applikationer och tjänster. Det hjälper till att automatisera repetitiva affärsprocesser som kommunikation, datainsamling och beslutsgodkännanden. Dess enkla gränssnitt tillåter användare med alla tekniska nivåer (från nybörjare till erfarna utvecklare) att automatisera arbetsuppgifter. Arbetsflödesutvecklingen förbättras också med Generativ AI via Copilot.

Copilot AI-assistentfunktionen i Power Automate gör det möjligt att beskriva vilken typ av flöde du behöver och vilka åtgärder flödet ska utföra. Copilot genererar sedan ett flöde baserat på din beskrivning. Du kan sedan anpassa flödet efter dina behov. AI Copilot genererar och föreslår också de åtgärder som behövs för att utföra uppgiften du vill automatisera. Vi kommer senare i denna lektion att titta på vad flöden är och hur du kan använda dem i Power Automate. Du kan sedan anpassa åtgärderna efter dina behov med AI Copilot assistentfunktionen via konversationssteg. Denna funktion är lättillgänglig från Power Automate hemskärm.

## Bygga intelligenta agenter med Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (tidigare Power Virtual Agents) är lågkodsmedlemmen i Power Platform för att bygga **AI-agenter** — konversationsassistenter som kan svara på frågor, utföra åtgärder och automatisera uppgifter åt dina användare. Precis som resten av Power Platform bygger du dessa agenter i en visuell, naturligt språk-först-upplevelse: du beskriver vad du vill att agenten ska göra, och Copilot Studio hjälper till att strukturera dess instruktioner, kunskap och åtgärder.

För vår utbildningsstartup kan du bygga en agent som besvarar studenters frågor om kurser, kontrollerar inlämningsdatum för uppgifter och till och med mailar en instruktör — allt utan att skriva kod.

Här är några av de senaste funktionerna som gör Copilot Studio kraftfullt:

- **Generativa svar från din kunskap**. Istället för att författa varje konversation manuellt, kan du koppla **kunskapskällor** — offentliga webbplatser, SharePoint, OneDrive, Dataverse, uppladdade filer eller företagsdata via kopplingar — och agenten genererar grundade svar från dem.

- **Generativ orkestrering**. Istället för att förlita sig på fasta triggerfraser, använder agenten AI för att förstå en förfrågan och dynamiskt bestämma vilken kunskap, ämnen och åtgärder som ska kombineras för att uppfylla den, inklusive att kedja ihop flera steg.

- **Åtgärder och kopplingar**. Agenter kan *göra* saker, inte bara chatta. Du kan ge en agent åtgärder stödda av 1 500+ förbyggda Power Platform-kopplingar, Power Automate-flöden, anpassade REST-APIer, promptar eller **Model Context Protocol (MCP)**-servrar.

- **Autonoma agenter**. Agenter är inte begränsade till att svara i ett chattfönster. Du kan bygga **autonoma agenter** som triggas av händelser — som ett nytt e-postmeddelande, en ny post i Dataverse eller en uppladdad fil — och sedan agera i bakgrunden för att slutföra en uppgift.

- **Mångagent-orkestrering**. Agenter kan kalla på andra agenter. En Copilot Studio-agent kan överlämna till, eller utökas av, andra agenter, inklusive agenter publicerade till Microsoft 365 Copilot och agenter byggda i Microsoft Foundry.

- **Modellval**. Utöver de inbyggda modellerna kan du ta med modeller från Microsoft Foundrys modellkatalog för att anpassa hur din agent resonerar och svarar.

- **Publicera överallt**. När en agent byggts kan den publiceras till flera kanaler — Microsoft Teams, Microsoft 365 Copilot, en webbplats eller anpassad app med mera — med säkerhet, autentisering och analys hanterad via Power Platform administratörsupplevelse.

Du kan börja bygga din första agent på [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) och läsa mer i [Microsoft Copilot Studio-dokumentationen](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Uppgift: Hantera studentuppgifter och fakturor för vår startup med Copilot

Vår startup erbjuder onlinekurser till studenter. Startuppen har vuxit snabbt och har nu svårt att hinna med efterfrågan på sina kurser. Startuppen har anställt dig som Power Platform-utvecklare för att hjälpa dem bygga en lågkodslösning som hjälper dem att hantera sina studentuppgifter och fakturor. Deras lösning bör kunna hjälpa dem spåra och hantera studentuppgifter via en app och automatisera fakturahanteringsprocessen via ett arbetsflöde. Du har blivit ombedd att använda generativ AI för att utveckla lösningen.

När du börjar använda Copilot kan du använda [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) för att komma igång med promptar. Detta bibliotek innehåller en lista med promptar som du kan använda för att bygga appar och flöden med Copilot. Du kan också använda promptarna i biblioteket för att få en idé om hur du beskriver dina krav till Copilot.

### Bygg en app för studentuppgiftsuppföljning för vår startup

Pedagogerna på vår startup har haft svårt att hålla reda på studentuppgifter. De har använt ett kalkylblad för att spåra uppgifterna men detta har blivit svårt att hantera i takt med att antalet studenter ökat. De har bett dig skapa en app som hjälper dem att spåra och hantera studentuppgifterna. Appen ska göra det möjligt att lägga till nya uppgifter, visa uppgifter, uppdatera uppgifter och ta bort uppgifter. Appen ska också möjliggöra för pedagoger och studenter att se vilka uppgifter som har bedömts och vilka som inte har bedömts.

Du kommer att bygga appen med Copilot i Power Apps enligt följande steg:

1. Navigera till [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) hemskärm.

1. Använd textrutan på hemskärmen för att beskriva vilken app du vill bygga. Till exempel, **_Jag vill bygga en app för att spåra och hantera studentuppgifter_**. Klicka på **Skicka**-knappen för att skicka prompten till AI Copilot.

![Beskriv appen du vill bygga](../../../translated_images/sv/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot föreslår en Dataverse-tabell med de fält du behöver för att lagra datan du vill spåra och lite exempeldata. Du kan sedan anpassa tabellen efter dina behov med AI Copilot assistentfunktionen via konversationssteg.

   > **Viktigt**: Dataverse är den underliggande dataplattformen för Power Platform. Det är en lågkodsdatalagringsplattform för appens data. Det är en helt hanterad tjänst som säkert lagrar data i Microsoft Cloud och är tillhandahållen inom din Power Platform-miljö. Den har inbyggda styrningsfunktioner för data, såsom dataklassificering, dataledning, detaljerad åtkomstkontroll med mera. Du kan läsa mer om Dataverse [här](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Föreslagna fält i din nya tabell](../../../translated_images/sv/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Pedagoger vill skicka e-post till studenter som har lämnat in sina uppgifter för att hålla dem uppdaterade om deras uppgiftsstatus. Du kan använda Copilot för att lägga till ett nytt fält i tabellen för att lagra studentens e-post. Till exempel kan du använda följande prompt för att lägga till ett nytt fält: **_Jag vill lägga till en kolumn för att lagra studentens e-post_**. Klicka på **Skicka**-knappen för att skicka prompten till AI Copilot.

![Lägga till nytt fält](../../../translated_images/sv/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot genererar ett nytt fält och du kan sedan anpassa fältet efter dina behov.


1. När du är klar med tabellen klickar du på **Create app**-knappen för att skapa appen.

1. AI Copilot kommer att generera en responsiv Canvas-app baserad på din beskrivning. Du kan sedan anpassa appen för att möta dina behov.

1. För lärare som ska skicka e-post till elever kan du använda Copilot för att lägga till en ny skärm i appen. Till exempel kan du använda följande prompt för att lägga till en ny skärm i appen: **_Jag vill lägga till en skärm för att skicka e-post till elever_**. Klicka på **Send**-knappen för att skicka prompten till AI Copilot.

![Adding a new screen via a prompt instruction](../../../translated_images/sv/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot kommer att generera en ny skärm och du kan sedan anpassa skärmen efter dina behov.

1. När du är klar med appen klickar du på **Save**-knappen för att spara appen.

1. För att dela appen med lärarna klickar du på **Share**-knappen och sedan klickar du på **Share** igen. Du kan sedan dela appen med lärarna genom att ange deras e-postadresser.

> **Din läxa**: Appen du precis byggde är en bra start men kan förbättras. Med e-postfunktionen kan lärare bara manuellt skicka e-post till elever genom att skriva in deras e-postadresser. Kan du använda Copilot för att bygga en automation som gör det möjligt för lärare att automatiskt skicka e-post till elever när de lämnar in sina uppgifter? En ledtråd är att med rätt prompt kan du använda Copilot i Power Automate för att bygga detta.

### Bygg en fakturainformations-tabell för vårt startup

Ekonomiteamet i vårt startup har haft svårt att hålla reda på fakturor. De har använt ett kalkylblad för att spåra fakturorna men det har blivit svårt att hantera eftersom antalet fakturor har ökat. De har bett dig att bygga en tabell som hjälper dem att lagra, spåra och hantera informationen om de fakturor de mottagit. Tabellen ska användas för att bygga en automation som extraherar all fakturainformation och lagrar den i tabellen. Tabellen ska också göra det möjligt för ekonomiteamet att se vilka fakturor som har betalats och vilka som inte har betalats.

Power Platform har en underliggande dataplattform som heter Dataverse som gör det möjligt att lagra data för dina appar och lösningar. Dataverse tillhandahåller en low-code dataplattform för att lagra appens data. Det är en fullt hanterad tjänst som säker lagrar data i Microsoft Cloud och provisioneras inom din Power Platform-miljö. Det kommer med inbyggda funktioner för datastyrning, såsom dataklassificering, datalining, finmaskig åtkomstkontroll och mer. Du kan lära dig mer [om Dataverse här](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Varför ska vi använda Dataverse för vårt startup? Standard- och anpassade tabeller inom Dataverse erbjuder ett säkert och molnbaserat lagringsalternativ för din data. Tabeller låter dig lagra olika typer av data, liknande hur du kan använda flera kalkylblad i en enda Excel-arbetsbok. Du kan använda tabeller för att lagra data som är specifik för din organisation eller verksamhetsbehov. Några av fördelarna vårt startup får av att använda Dataverse inkluderar men är inte begränsade till:

- **Lätt att hantera**: Både metadata och data lagras i molnet, så du behöver inte oroa dig för detaljer kring hur de lagras eller hanteras. Du kan fokusera på att bygga dina appar och lösningar.

- **Säkert**: Dataverse erbjuder ett säkert och molnbaserat lagringsalternativ för din data. Du kan kontrollera vem som har åtkomst till data i dina tabeller och hur de kan komma åt den med hjälp av rollbaserad säkerhet.

- **Rik metadata**: Datatyper och relationer används direkt inom Power Apps

- **Logik och validering**: Du kan använda affärsregler, beräknade fält och valideringsregler för att upprätthålla affärslogik och säkerställa data noggrannhet.

Nu när du vet vad Dataverse är och varför du ska använda det, låt oss titta på hur du kan använda Copilot för att skapa en tabell i Dataverse som uppfyller vårt ekonomiteams krav.

> **Notera**: Du kommer att använda denna tabell i nästa avsnitt för att bygga en automation som extraherar all fakturainformation och lagrar den i tabellen.

För att skapa en tabell i Dataverse med Copilot, följ stegen nedan:

1. Navigera till [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) hemskärm.

2. På vänstra navigeringsfältet, välj **Tables** och klicka sedan på **Describe the new Table**.

![Select new table](../../../translated_images/sv/describe-new-table.0792373eb757281e.webp)

1. På skärmen **Describe the new Table** använder du textfältet för att beskriva tabellen du vill skapa. Till exempel, **_Jag vill skapa en tabell för att lagra fakturainformation_**. Klicka på **Send**-knappen för att skicka prompten till AI Copilot.

![Describe the table](../../../translated_images/sv/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot kommer att föreslå en Dataverse-tabell med de fält du behöver för att lagra den data du vill spåra samt exempeldata. Du kan sedan anpassa tabellen för att möta dina behov med hjälp av AI Copilot-assistenten genom samtalssteg.

![Suggested Dataverse table](../../../translated_images/sv/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Ekonomiteamet vill skicka ett e-postmeddelande till leverantören för att uppdatera dem om fakturans aktuella status. Du kan använda Copilot för att lägga till ett nytt fält i tabellen för att lagra leverantörens e-post. Till exempel kan du använda följande prompt för att lägga till ett nytt fält i tabellen: **_Jag vill lägga till en kolumn för att lagra leverantörens e-post_**. Klicka på **Send**-knappen för att skicka prompten till AI Copilot.

1. AI Copilot kommer att generera ett nytt fält och du kan sedan anpassa fältet för att möta dina behov.

1. När du är klar med tabellen klickar du på **Create**-knappen för att skapa tabellen.

## AI-modeller i Power Platform med AI Builder

AI Builder är en low-code AI-funktion tillgänglig i Power Platform som gör det möjligt att använda AI-modeller för att hjälpa dig automatisera processer och förutsäga resultat. Med AI Builder kan du integrera AI i dina appar och flöden som ansluter till din data i Dataverse eller i olika molndatakällor som SharePoint, OneDrive eller Azure.

## Förbyggda AI-modeller vs anpassade AI-modeller

AI Builder erbjuder två typer av AI-modeller: Förbyggda AI-modeller och Anpassade AI-modeller. Förbyggda AI-modeller är färdiga att använda och tränade av Microsoft, och finns tillgängliga i Power Platform. Dessa hjälper dig att lägga till intelligens i dina appar och flöden utan att du behöver samla data och sedan bygga, träna och publicera egna modeller. Du kan använda dessa modeller för att automatisera processer och förutsäga resultat.

Några av de förbyggda AI-modellerna som finns i Power Platform inkluderar:

- **Nyckelfrasextraktion**: Den här modellen extraherar nyckelfraser från text.
- **Språkdetection**: Den här modellen upptäcker språket i en text.
- **Sentimentanalys**: Den här modellen upptäcker positiv, negativ, neutral eller blandad känsla i text.
- **Visitkortsläsare**: Den här modellen extraherar information från visitkort.
- **Textigenkänning**: Den här modellen extraherar text från bilder.
- **Objektdetektion**: Den här modellen upptäcker och extraherar objekt från bilder.
- **Dokumentbehandling**: Den här modellen extraherar information från formulär.
- **Fakturabehandling**: Den här modellen extraherar information från fakturor.

Med Anpassade AI-modeller kan du ta med din egen modell till AI Builder så att den kan fungera som vilken AI Builder-anpassad modell som helst, vilket låter dig träna modellen med din egen data. Du kan använda dessa modeller för att automatisera processer och förutsäga resultat i både Power Apps och Power Automate. Det finns begränsningar när du använder egen modell. Läs mer om dessa [begränsningar](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/sv/ai-builder-models.8069423b84cfc47f.webp)

## Uppgift #2 - Bygg ett fakturabehandlingsflöde för vårt startup

Ekonomiteamet har haft svårt att hantera fakturabehandling. De har använt ett kalkylblad för att spåra fakturorna, men det har blivit svårt att hantera eftersom antalet fakturor har ökat. De har bett dig bygga ett arbetsflöde som hjälper dem att bearbeta fakturor med hjälp av AI. Arbetsflödet ska göra det möjligt att extrahera information från fakturor och lagra informationen i en Dataverse-tabell. Arbetsflödet ska också kunna skicka ett e-postmeddelande till ekonomiteamet med den extraherade informationen.

Nu när du vet vad AI Builder är och varför du ska använda det, låt oss titta på hur du kan använda Fakturabehandlings-AI-modellen i AI Builder, som vi tagit upp tidigare, för att bygga ett arbetsflöde som hjälper ekonomiteamet att bearbeta fakturor.

För att bygga ett arbetsflöde som hjälper ekonomiteamet att bearbeta fakturor med Fakturabehandlings-AI-modellen i AI Builder, följ stegen nedan:

1. Navigera till [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) hemskärm.

2. Använd textfältet på hemskärmen för att beskriva arbetsflödet du vill bygga. Till exempel, **_Bearbeta en faktura när den anländer i min inkorg_**. Klicka på **Send**-knappen för att skicka prompten till AI Copilot.

   ![Copilot power automate](../../../translated_images/sv/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot kommer att föreslå åtgärder du behöver för att automatisera uppgiften. Du kan klicka på **Next** för att gå vidare till nästa steg.

4. I nästa steg kommer Power Automate att be dig konfigurera de anslutningar som behövs för flödet. När du är klar, klicka på **Create flow**-knappen för att skapa flödet.

5. AI Copilot kommer att generera ett flöde och du kan sedan anpassa det för att möta dina behov.

6. Uppdatera triggaren för flödet och ställ in **Folder** till den mapp där fakturorna kommer att lagras. Till exempel kan du ställa in mappen till **Inkorg**. Klicka på **Show advanced options** och ställ in **Only with Attachments** till **Yes**. Detta säkerställer att flödet bara körs när ett e-postmeddelande med bifogad fil tas emot i mappen.

7. Ta bort följande åtgärder från flödet: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** och **Compose 4** eftersom du inte kommer att använda dem.

8. Ta bort **Condition**-åtgärden från flödet eftersom du inte kommer att använda den. Det ska se ut som i följande skärmbild:

   ![power automate, remove actions](../../../translated_images/sv/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Klicka på **Add an action**-knappen och sök efter **Dataverse**. Välj åtgärden **Add a new row**.

10. På åtgärden **Extract Information from invoices**, uppdatera **Invoice File** så att det pekar på **Attachment Content** från e-postmeddelandet. Detta säkerställer att flödet extraherar information från fakturabilagan.

11. Välj den **Table** du skapade tidigare. Till exempel kan du välja **Invoice Information**-tabellen. Välj dynamiskt innehåll från föregående åtgärd för att fylla i följande fält:

    - ID
    - Amount
    - Date
    - Name
    - Status - Sätt **Status** till **Pending**.
    - Supplier Email - Använd **From**-dynamikinnehållet från triggern **When a new email arrives**.

    ![power automate add row](../../../translated_images/sv/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. När du är klar med flödet klickar du på **Save**-knappen för att spara flödet. Du kan sedan testa flödet genom att skicka ett e-postmeddelande med en faktura till den mapp du angav i triggern.

> **Din läxa**: Flödet du precis byggde är en bra start, nu behöver du fundera på hur du kan bygga en automation som gör det möjligt för vårt ekonomiteam att skicka ett e-postmeddelande till leverantören för att uppdatera dem med den aktuella statusen för deras faktura. En ledtråd: flödet måste köras när fakturans status ändras.

## Använd en textgenererande AI-modell i Power Automate

AI-modellen Create Text with GPT i AI Builder låter dig generera text baserat på en prompt och drivs av Microsoft Azure OpenAI Service. Med denna kapacitet kan du integrera GPT (Generative Pre-Trained Transformer)-teknologi i dina appar och flöden för att bygga olika automatiserade flöden och insiktsfulla applikationer.

GPT-modeller genomgår omfattande träning på stora mängder data, vilket gör det möjligt för dem att producera text som liknar mänskligt språk när de får en prompt. När de integreras med arbetsflödesautomatisering kan AI-modeller som GPT användas för att effektivisera och automatisera en mängd olika uppgifter.

Till exempel kan du bygga flöden för att automatiskt generera text för olika användningsområden, såsom utkast till e-post, produktbeskrivningar med mera. Du kan också använda modellen för att generera text för olika appar, som chattbottar och kundtjänstappar som gör det möjligt för kundtjänstagenter att svara effektivt och korrekt på kundförfrågningar.

![create a prompt](../../../translated_images/sv/create-prompt-gpt.69d429300c2e870a.webp)


För att lära dig hur du använder denna AI-modell i Power Automate, gå igenom modulen [Lägg till intelligens med AI Builder och GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Bra jobbat! Fortsätt din lärande

Efter att ha slutfört denna lektion, kolla in vår [Generativ AI Learning-samling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din kunskap om Generativ AI!

Vill du anpassa och få ut mer av Copilot? Utforska [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — en communitybidragen samling av instruktioner, agenter, färdigheter och konfigurationer för att hjälpa dig att få ut det mesta av GitHub Copilot.

Gå vidare till lektion 11 där vi kommer att titta på hur man [integrerar Generativ AI med Function Calling](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->