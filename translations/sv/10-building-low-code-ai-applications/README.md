<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5ff3b6204a695a117d6f452403c95f7",
  "translation_date": "2025-06-25T18:48:24+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "sv"
}
-->
# Bygga AI-applikationer med låg kod

[![Bygga AI-applikationer med låg kod](../../../translated_images/10-lesson-banner.a01ac8fe3fd86310c2e4065c0b3c584879f33b8ce797311821a636992f8a5b2f.sv.png)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

## Introduktion

Nu när vi har lärt oss hur man bygger bildgenererande applikationer, låt oss prata om låg kod. Generativ AI kan användas inom olika områden inklusive låg kod, men vad är låg kod och hur kan vi lägga till AI i det?

Att bygga appar och lösningar har blivit enklare för traditionella utvecklare och icke-utvecklare genom användning av plattformar för utveckling med låg kod. Dessa plattformar möjliggör att du kan bygga appar och lösningar med lite eller ingen kod. Detta uppnås genom att tillhandahålla en visuell utvecklingsmiljö där du kan dra och släppa komponenter för att bygga appar och lösningar. Detta gör att du kan bygga appar och lösningar snabbare och med mindre resurser. I denna lektion går vi djupt in i hur man använder låg kod och hur man förbättrar utveckling med låg kod med AI genom Power Platform.

Power Platform ger organisationer möjlighet att ge sina team kraft att bygga sina egna lösningar genom en intuitiv miljö med låg kod eller ingen kod. Denna miljö hjälper till att förenkla processen att bygga lösningar. Med Power Platform kan lösningar byggas på dagar eller veckor istället för månader eller år. Power Platform består av fem nyckelprodukter: Power Apps, Power Automate, Power BI, Power Pages och Copilot Studio.

Denna lektion omfattar:

- Introduktion till generativ AI i Power Platform
- Introduktion till Copilot och hur man använder det
- Använda generativ AI för att bygga appar och flöden i Power Platform
- Förstå AI-modellerna i Power Platform med AI Builder

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Förstå hur Copilot fungerar i Power Platform.

- Bygga en app för att spåra studentuppgifter för vår utbildningsstartup.

- Bygga ett fakturabehandlingsflöde som använder AI för att extrahera information från fakturor.

- Använda bästa praxis när du använder GPT AI-modellen för att skapa text.

De verktyg och teknologier som du kommer att använda i denna lektion är:

- **Power Apps**, för appen Student Assignment Tracker, som tillhandahåller en utvecklingsmiljö med låg kod för att bygga appar för att spåra, hantera och interagera med data.

- **Dataverse**, för att lagra data för appen Student Assignment Tracker där Dataverse kommer att tillhandahålla en dataplattform med låg kod för att lagra appens data.

- **Power Automate**, för fakturabehandlingsflödet där du kommer att ha en utvecklingsmiljö med låg kod för att bygga arbetsflöden för att automatisera fakturabehandlingsprocessen.

- **AI Builder**, för fakturabehandlings-AI-modellen där du kommer att använda förbyggda AI-modeller för att bearbeta fakturorna för vår startup.

## Generativ AI i Power Platform

Att förbättra utveckling och applikation med låg kod genom generativ AI är ett nyckelområde för Power Platform. Målet är att möjliggöra för alla att bygga AI-drivna appar, webbplatser, instrumentpaneler och automatisera processer med AI, _utan att kräva någon expertis inom data science_. Detta mål uppnås genom att integrera generativ AI i utvecklingsupplevelsen med låg kod i Power Platform i form av Copilot och AI Builder.

### Hur fungerar detta?

Copilot är en AI-assistent som gör det möjligt att bygga Power Platform-lösningar genom att beskriva dina krav i en serie konversativa steg med naturligt språk. Du kan till exempel instruera din AI-assistent att ange vilka fält din app ska använda, och den kommer att skapa både appen och den underliggande datamodellen, eller så kan du specificera hur du ska ställa in ett flöde i Power Automate.

Du kan använda Copilot-drivna funktioner som en funktion i dina appskärmar för att möjliggöra att användare kan upptäcka insikter genom konversativa interaktioner.

AI Builder är en AI-funktion med låg kod tillgänglig i Power Platform som gör det möjligt att använda AI-modeller för att hjälpa dig att automatisera processer och förutsäga resultat. Med AI Builder kan du ta med AI till dina appar och flöden som ansluter till din data i Dataverse eller i olika molndatakällor, såsom SharePoint, OneDrive eller Azure.

Copilot är tillgängligt i alla Power Platform-produkter: Power Apps, Power Automate, Power BI, Power Pages och Power Virtual Agents. AI Builder är tillgängligt i Power Apps och Power Automate. I denna lektion kommer vi att fokusera på hur man använder Copilot och AI Builder i Power Apps och Power Automate för att bygga en lösning för vår utbildningsstartup.

### Copilot i Power Apps

Som en del av Power Platform tillhandahåller Power Apps en utvecklingsmiljö med låg kod för att bygga appar för att spåra, hantera och interagera med data. Det är en uppsättning apputvecklingstjänster med en skalbar dataplattform och förmågan att ansluta till molntjänster och lokala data. Power Apps gör det möjligt att bygga appar som körs på webbläsare, surfplattor och telefoner, och kan delas med medarbetare. Power Apps förenklar användarna i apputveckling med ett enkelt gränssnitt, så att varje affärsanvändare eller professionell utvecklare kan bygga anpassade appar. Apputvecklingsupplevelsen förbättras också med generativ AI genom Copilot.

Copilot AI-assistentfunktionen i Power Apps gör det möjligt att beskriva vilken typ av app du behöver och vilken information du vill att din app ska spåra, samla eller visa. Copilot genererar sedan en responsiv Canvas-app baserat på din beskrivning. Du kan sedan anpassa appen för att möta dina behov. AI Copilot genererar och föreslår också en Dataverse-tabell med de fält du behöver för att lagra den data du vill spåra och lite exempeldata. Vi kommer att titta på vad Dataverse är och hur du kan använda det i Power Apps senare i denna lektion. Du kan sedan anpassa tabellen för att möta dina behov genom AI Copilot-assistentfunktionen genom konversativa steg. Denna funktion är lätt tillgänglig från Power Apps hemskärm.

### Copilot i Power Automate

Som en del av Power Platform gör Power Automate det möjligt för användare att skapa automatiserade arbetsflöden mellan applikationer och tjänster. Det hjälper till att automatisera repetitiva affärsprocesser såsom kommunikation, datainsamling och beslutsgodkännanden. Dess enkla gränssnitt gör det möjligt för användare med alla tekniska kompetenser (från nybörjare till erfarna utvecklare) att automatisera arbetsuppgifter. Arbetsflödesutvecklingsupplevelsen förbättras också med generativ AI genom Copilot.

Copilot AI-assistentfunktionen i Power Automate gör det möjligt att beskriva vilken typ av flöde du behöver och vilka åtgärder du vill att ditt flöde ska utföra. Copilot genererar sedan ett flöde baserat på din beskrivning. Du kan sedan anpassa flödet för att möta dina behov. AI Copilot genererar och föreslår också de åtgärder du behöver för att utföra den uppgift du vill automatisera. Vi kommer att titta på vad flöden är och hur du kan använda dem i Power Automate senare i denna lektion. Du kan sedan anpassa åtgärderna för att möta dina behov genom AI Copilot-assistentfunktionen genom konversativa steg. Denna funktion är lätt tillgänglig från Power Automate hemskärm.

## Uppgift: Hantera studentuppgifter och fakturor för vår startup, med Copilot

Vår startup tillhandahåller onlinekurser till studenter. Starten har vuxit snabbt och kämpar nu för att hålla jämna steg med efterfrågan på sina kurser. Starten har anställt dig som Power Platform-utvecklare för att hjälpa dem bygga en lösning med låg kod för att hjälpa dem att hantera sina studentuppgifter och fakturor. Deras lösning bör kunna hjälpa dem att spåra och hantera studentuppgifter genom en app och automatisera fakturabehandlingsprocessen genom ett arbetsflöde. Du har blivit ombedd att använda generativ AI för att utveckla lösningen.

När du börjar använda Copilot kan du använda [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) för att komma igång med uppmaningarna. Detta bibliotek innehåller en lista över uppmaningar som du kan använda för att bygga appar och flöden med Copilot. Du kan också använda uppmaningarna i biblioteket för att få en idé om hur du beskriver dina krav till Copilot.

### Bygg en app för att spåra studentuppgifter för vår startup

Lärarna på vår startup har kämpat för att hålla koll på studentuppgifter. De har använt ett kalkylblad för att spåra uppgifterna men detta har blivit svårt att hantera när antalet studenter har ökat. De har bett dig att bygga en app som hjälper dem att spåra och hantera studentuppgifter. Appen bör göra det möjligt för dem att lägga till nya uppgifter, visa uppgifter, uppdatera uppgifter och ta bort uppgifter. Appen bör också göra det möjligt för lärare och studenter att se de uppgifter som har blivit betygsatta och de som inte har blivit betygsatta.

Du kommer att bygga appen med hjälp av Copilot i Power Apps enligt följande steg:

1. Navigera till [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) hemskärm.

1. Använd textområdet på hemskärmen för att beskriva appen du vill bygga. Till exempel, **_Jag vill bygga en app för att spåra och hantera studentuppgifter_**. Klicka på **Skicka**-knappen för att skicka uppmaningen till AI Copilot.

![Beskriv appen du vill bygga](../../../translated_images/copilot-chat-prompt-powerapps.84250f341d060830a296b68512e6b3b3aa3a4559f4f1c2d7bafeba8ad3fcd17a.sv.png)

1. AI Copilot kommer att föreslå en Dataverse-tabell med de fält du behöver för att lagra den data du vill spåra och lite exempeldata. Du kan sedan anpassa tabellen för att möta dina behov genom AI Copilot-assistentfunktionen genom konversativa steg.

   > **Viktigt**: Dataverse är den underliggande dataplattformen för Power Platform. Det är en dataplattform med låg kod för att lagra appens data. Det är en fullt hanterad tjänst som säkert lagrar data i Microsoft Cloud och provisioneras inom din Power Platform-miljö. Den kommer med inbyggda datastyrningsfunktioner, såsom dataklassificering, datalinje, finfördelad åtkomstkontroll och mer. Du kan lära dig mer om Dataverse [här](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Föreslagna fält i din nya tabell](../../../translated_images/copilot-dataverse-table-powerapps.f4cc07b5d5f9327bd3783dd288debb2a959ce3320107512e235137aebd8a1a4c.sv.png)

1. Lärare vill skicka e-post till de studenter som har lämnat in sina uppgifter för att hålla dem uppdaterade om framstegen med deras uppgifter. Du kan använda Copilot för att lägga till ett nytt fält i tabellen för att lagra studentens e-post. Till exempel kan du använda följande uppmaning för att lägga till ett nytt fält i tabellen: **_Jag vill lägga till en kolumn för att lagra studentens e-post_**. Klicka på **Skicka**-knappen för att skicka uppmaningen till AI Copilot.

![Lägga till ett nytt fält](../../../translated_images/copilot-new-column.35e15ff21acaf2745965d427b130f2be772f0484835b44fe074d496b1a455f2a.sv.png)

1. AI Copilot kommer att generera ett nytt fält och du kan sedan anpassa fältet för att möta dina behov.

1. När du är klar med tabellen, klicka på **Skapa app**-knappen för att skapa appen.

1. AI Copilot kommer att generera en responsiv Canvas-app baserat på din beskrivning. Du kan sedan anpassa appen för att möta dina behov.

1. För att lärare ska kunna skicka e-post till studenter, kan du använda Copilot för att lägga till en ny skärm i appen. Till exempel kan du använda följande uppmaning för att lägga till en ny skärm i appen: **_Jag vill lägga till en skärm för att skicka e-post till studenter_**. Klicka på **Skicka**-knappen för att skicka uppmaningen till AI Copilot.

![Lägga till en ny skärm via en uppmaningsinstruktion](../../../translated_images/copilot-new-screen.2e0bef7132a173928bc621780b39799e03982d315cb5a9ff75a34b08054641d4.sv.png)

1. AI Copilot kommer att generera en ny skärm och du kan sedan anpassa skärmen för att möta dina behov.

1. När du är klar med appen, klicka på **Spara**-knappen för att spara appen.

1. För att dela appen med lärarna, klicka på **Dela**-knappen och klicka sedan på **Dela**-knappen igen. Du kan sedan dela appen med lärarna genom att ange deras e-postadresser.

> **Din hemläxa**: Appen du just byggde är en bra start men kan förbättras. Med e-postfunktionen kan lärare endast skicka e-post till studenter manuellt genom att behöva skriva deras e-postadresser. Kan du använda Copilot för att bygga en automation som gör det möjligt för lärare att skicka e-post till studenter automatiskt när de lämnar in sina uppgifter? Din ledtråd är att med rätt uppmaning kan du använda Copilot i Power Automate för att bygga detta.

### Bygg en fakturainformationstabell för vår startup

Finansteamet på vår startup har kämpat för att hålla koll på fakturor. De har använt ett kalkylblad för att spåra fakturorna men detta har blivit svårt att hantera när antalet fakturor har ökat. De har bett dig att bygga en tabell som hjälper dem att lagra, spåra och hantera informationen om de fakturor de har mottagit. Tabellen bör användas för att bygga en automation som extraherar all fakturainformation och lagrar den i tabellen. Tabellen bör också göra det möjligt för finansteamet att se de fakturor som har blivit betalda och de som inte har blivit betalda.

Power Platform har en underliggande dataplattform som heter Dataverse som gör det möjligt att lagra data för dina appar och lösningar. Dataverse tillhandahåller en dataplattform med låg kod för att lagra appens data. Det är en fullt hanterad tjänst som säkert lagrar data i Microsoft Cloud och provisioneras inom din Power Platform-miljö. Den kommer med inbyggda datastyrningsfunktioner, såsom dataklassificering, datalinje, finfördelad åtkomstkontroll och mer. Du kan lära dig mer [om Dataverse här](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Varför ska vi använda Dataverse för vår startup? De standard- och anpassade tabellerna inom Dataverse tillhandahåller ett säkert och molnbaserat lagringsalternativ för din data. Tabeller gör det möjligt att lagra olika typer av data, liknande hur du kanske använder flera kalkylblad i en enda Excel-arbetsbok. Du kan använda tabeller för att lagra data som är specifik för dina organisations- eller affärsbehov. Några av de fördelar vår startup kommer att få från att använda Dataverse inkluderar men är inte begränsade till:

- **Lätt att hantera**: Både metadata och data lagras i molnet, så du behöver inte oroa dig för detaljerna om hur de lagras eller hanteras. Du kan fokusera på att bygga dina appar och lösningar.

- **Säker**: Dataverse tillhandahåller ett säkert och molnbaserat lagringsalternativ för din data. Du kan kontrollera vem som har åtkomst till data i dina tabeller och hur de kan komma åt den med hjälp av rollbaserad säkerhet.

- **Rik metadata**: Datatyper och relationer används direkt inom Power Apps

- **Logik och validering**: Du kan använda affärsregler, beräknade fält och valideringsregler för att upprätthålla affärslogik och bibehålla datanoggrannhet.

Nu när du vet vad Dataverse är och varför du bör använda det, låt oss titta på hur du kan använda Copilot för att skapa en tabell i Dataverse för att möta kraven från vårt finansteam.

> **Obs**: Du kommer att använda denna tabell i nästa avsnitt för att bygga en automation som extraherar all fakturainformation och lagrar den i tabellen.
För att skapa en tabell i Dataverse med hjälp av Copilot, följ stegen nedan: 1. Navigera till [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) hemskärm. 2. På den vänstra navigeringspanelen, välj **Tabeller** och klicka sedan på **Beskriv den nya tabellen**. ![Välj ny tabell](./
en text. - **Sentimentanalys**: Den här modellen upptäcker positiv, negativ, neutral eller blandad känsla i text. - **Visitkortsläsare**: Den här modellen extraherar information från visitkort. - **Textigenkänning**: Den här modellen extraherar text från bilder. - **Objektdetektion**: Den här modellen upptäcker och extraherar objekt från bilder. - **Dokumentbearbetning**: Den här modellen extraherar information från formulär. - **Fakturabearbetning**: Den här modellen extraherar information från fakturor. Med Anpassade AI-modeller kan du ta med din egen modell till AI Builder så att den kan fungera som vilken AI Builder-anpassad modell som helst, vilket gör att du kan träna modellen med din egen data. Du kan använda dessa modeller för att automatisera processer och förutsäga resultat i både Power Apps och Power Automate. När du använder din egen modell finns det begränsningar som gäller. Läs mer om dessa [begränsningar](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst). ![AI builder modeller](../../../translated_images/ai-builder-models.8069423b84cfc47f6bb989bc3cd0584b5b2471c80fad80bf504d356928a08c9c.sv.png) ## Uppgift #2 - Bygg ett flöde för fakturabearbetning för vår startup Ekonomiteamet har haft svårt att bearbeta fakturor. De har använt ett kalkylblad för att hålla koll på fakturorna, men det har blivit svårt att hantera eftersom antalet fakturor har ökat. De har bett dig att bygga ett arbetsflöde som hjälper dem att bearbeta fakturor med hjälp av AI. Arbetsflödet ska göra det möjligt för dem att extrahera information från fakturor och lagra informationen i en Dataverse-tabell. Arbetsflödet ska också göra det möjligt för dem att skicka ett e-postmeddelande till ekonomiteamet med den extraherade informationen. Nu när du vet vad AI Builder är och varför du bör använda det, låt oss titta på hur du kan använda AI-modellen för fakturabearbetning i AI Builder, som vi täckte tidigare, för att bygga ett arbetsflöde som hjälper ekonomiteamet att bearbeta fakturor. För att bygga ett arbetsflöde som hjälper ekonomiteamet att bearbeta fakturor med hjälp av AI-modellen för fakturabearbetning i AI Builder, följ stegen nedan: 1. Navigera till [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) hemskärmen. 2. Använd textområdet på hemskärmen för att beskriva det arbetsflöde du vill bygga. Till exempel, **_Bearbeta en faktura när den anländer i min brevlåda_**. Klicka på **Skicka**-knappen för att skicka prompten till AI Copilot. ![Copilot power automate](../../../translated_images/copilot-chat-prompt-powerautomate.f377e478cc8412de4394fab09e5b72f97b3fc9312526b516ded426102f51c30d.sv.png) 3. AI Copilot kommer att föreslå de åtgärder du behöver utföra för att automatisera den uppgift du vill. Du kan klicka på **Nästa**-knappen för att gå igenom nästa steg. 4. På nästa steg kommer Power Automate att be dig ställa in de anslutningar som krävs för flödet. När du är klar, klicka på **Skapa flöde**-knappen för att skapa flödet. 5. AI Copilot kommer att generera ett flöde och du kan sedan anpassa flödet för att möta dina behov. 6. Uppdatera flödets trigger och ställ in **Mapp** till den mapp där fakturorna kommer att lagras. Till exempel kan du ställa in mappen till **Inkorg**. Klicka på **Visa avancerade alternativ** och ställ in **Endast med bilagor** till **Ja**. Detta kommer att säkerställa att flödet endast körs när ett e-postmeddelande med en bilaga tas emot i mappen. 7. Ta bort följande åtgärder från flödet: **HTML till text**, **Compose**, **Compose 2**, **Compose 3** och **Compose 4** eftersom du inte kommer att använda dem. 8. Ta bort **Condition**-åtgärden från flödet eftersom du inte kommer att använda den. Det bör se ut som följande skärmdump: ![power automate, ta bort åtgärder](../../../translated_images/powerautomate-remove-actions.7216392fe684ceba4b73c6383edd1cc5e7ded11afd0ca812052a11487d049ef8.sv.png) 9. Klicka på **Lägg till en åtgärd**-knappen och sök efter **Dataverse**. Välj **Lägg till en ny rad**-åtgärden. 10. På **Extrahera information från fakturor**-åtgärden, uppdatera **Fakturafil** för att peka på **Bilageinnehåll** från e-postmeddelandet. Detta kommer att säkerställa att flödet extraherar information från fakturabilagan. 11. Välj den **Tabell** du skapade tidigare. Till exempel kan du välja **Fakturainformation**-tabellen. Välj det dynamiska innehållet från föregående åtgärd för att fylla i följande fält: - ID - Belopp - Datum - Namn - Status - Ställ in **Status** till **Väntande**. - Leverantörens e-post - Använd **Från** dynamiskt innehåll från **När ett nytt e-postmeddelande anländer**-triggern. ![power automate lägg till rad](../../../translated_images/powerautomate-add-row.5edce45e5dd3d51e5152688dc140ad43e1423e7a9fef9a206f82a7965ea68d73.sv.png) 12. När du är klar med flödet, klicka på **Spara**-knappen för att spara flödet. Du kan sedan testa flödet genom att skicka ett e-postmeddelande med en faktura till den mapp du angav i triggern. > **Din läxa**: Flödet du just byggde är en bra start, nu behöver du fundera på hur du kan bygga en automation som gör det möjligt för vårt ekonomiteam att skicka ett e-postmeddelande till leverantören för att uppdatera dem med den aktuella statusen för deras faktura. Din ledtråd: flödet måste köras när fakturans status ändras.

## Använd en Textgenereringsmodell i Power Automate

Skapa Text med GPT AI-modellen i AI Builder gör det möjligt för dig att generera text baserat på en prompt och drivs av Microsoft Azure OpenAI Service. Med denna kapacitet kan du integrera GPT (Generative Pre-Trained Transformer) teknologi i dina appar och flöden för att bygga en mängd automatiserade flöden och insiktsfulla applikationer.

GPT-modeller genomgår omfattande träning på stora mängder data, vilket gör det möjligt för dem att producera text som nära liknar mänskligt språk när de ges en prompt. När de integreras med arbetsflödesautomation kan AI-modeller som GPT utnyttjas för att effektivisera och automatisera en mängd olika uppgifter.

Till exempel kan du bygga flöden för att automatiskt generera text för olika användningsområden, såsom: utkast till e-postmeddelanden, produktbeskrivningar och mer. Du kan också använda modellen för att generera text för olika appar, såsom chatbots och kundtjänstappar som gör det möjligt för kundtjänstagenter att svara effektivt och snabbt på kundförfrågningar.

![skapa en prompt](../../../translated_images/create-prompt-gpt.69d429300c2e870a12ec95556cda9bacf6a173e452cdca02973c90df5f705cee.sv.png)

För att lära dig hur du använder denna AI-modell i Power Automate, gå igenom [Lägg till intelligens med AI Builder och GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) modulen.

## Bra jobbat! Fortsätt din inlärning

Efter att ha avslutat denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta höja din kunskap om Generative AI!

Gå vidare till Lektion 11 där vi kommer att titta på hur man [integrerar Generative AI med funktionanrop](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.