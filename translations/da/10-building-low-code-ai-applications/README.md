# Bygning af Low Code AI-applikationer

[![Bygning af Low Code AI-applikationer](../../../translated_images/da/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

## Introduktion

Nu hvor vi har lært at bygge billedgenererende applikationer, lad os snakke om low code. Generativ AI kan bruges til mange forskellige områder, herunder low code, men hvad er low code, og hvordan kan vi tilføje AI til det?

Bygning af apps og løsninger er blevet nemmere for både traditionelle udviklere og ikke-udviklere gennem brugen af Low Code Development Platforms. Low Code Development Platforms gør det muligt at bygge apps og løsninger med lidt eller ingen kode. Dette opnås ved at tilbyde et visuelt udviklingsmiljø, hvor du kan trække og slippe komponenter for at bygge apps og løsninger. Dette gør, at du kan bygge apps og løsninger hurtigere og med færre ressourcer. I denne lektion dykker vi dybt ned i, hvordan man bruger Low Code og hvordan man forbedrer low code-udvikling med AI ved hjælp af Power Platform.

Power Platform giver organisationer mulighed for at styrke deres teams til at bygge deres egne løsninger gennem et intuitivt low-code eller no-code miljø. Dette miljø hjælper med at forenkle processen med at bygge løsninger. Med Power Platform kan løsninger bygges på dage eller uger i stedet for måneder eller år. Power Platform består af fem nøgleprodukter: Power Apps, Power Automate, Power BI, Power Pages og Copilot Studio.

Denne lektion dækker:

- Introduktion til Generativ AI i Power Platform
- Introduktion til Copilot og hvordan man bruger det
- Brug af Generativ AI til at bygge apps og flows i Power Platform
- Forståelse af AI-modeller i Power Platform med AI Builder
- Bygning af intelligente agenter med Microsoft Copilot Studio

## Læringsmål

Når du har gennemført denne lektion, vil du kunne:

- Forstå hvordan Copilot fungerer i Power Platform.

- Byg en Student Assignment Tracker-app til vores uddannelsesstartup.

- Byg en fakturahåndteringsflow, der bruger AI til at udtrække information fra fakturaer.

- Anvende bedste praksis ved brug af Create Text med GPT AI Model.

- Forstå hvad Microsoft Copilot Studio er, og hvordan man bygger intelligente agenter med det.

De værktøjer og teknologier, du vil bruge i denne lektion er:

- **Power Apps**, til Student Assignment Tracker-appen, der tilbyder et low-code udviklingsmiljø til at bygge apps til at spore, håndtere og interagere med data.

- **Dataverse**, til at lagre data for Student Assignment Tracker-appen, hvor Dataverse leverer en low-code dataplatform til lagring af appens data.

- **Power Automate**, til fakturahåndteringsflowet, hvor du får et low-code udviklingsmiljø til at bygge workflows til automatisering af fakturahåndteringsprocessen.

- **AI Builder**, til fakturahåndterings AI-modellen, hvor du bruger forudbyggede AI-modeller til at behandle fakturaerne for vores startup.

## Generativ AI i Power Platform

Forbedring af low-code udvikling og applikation med generativ AI er et nøgleområde for Power Platform. Målet er at gøre det muligt for alle at bygge AI-drevne apps, sites, dashboards og automatisere processer med AI, _uden at kræve ekspertise i datalogi_. Dette mål opnås ved at integrere generativ AI i low-code udviklingsoplevelsen i Power Platform i form af Copilot og AI Builder.

### Hvordan virker dette?

Copilot er en AI-assistent, der gør det muligt for dig at bygge Power Platform-løsninger ved at beskrive dine krav i en række dialogtrin ved brug af naturligt sprog. Du kan for eksempel instruere din AI-assistent om at angive hvilke felter din app skal bruge, og den vil skabe både appen og den underliggende datamodel, eller du kan specificere, hvordan du opsætter et flow i Power Automate.

Du kan bruge Copilot-drevne funktioner som en funktion i dine appskærme for at give brugerne mulighed for at opdage indsigter gennem samtaleinteraktioner.

AI Builder er en low-code AI-funktion tilgængelig i Power Platform, som gør det muligt at bruge AI-modeller til at hjælpe med at automatisere processer og forudsige resultater. Med AI Builder kan du bringe AI til dine apps og flows, der forbinder til dine data i Dataverse eller i forskellige cloud-datakilder, såsom SharePoint, OneDrive eller Azure.

Copilot er tilgængelig i alle Power Platform-produkter: Power Apps, Power Automate, Power BI, Power Pages og Copilot Studio (tidligere Power Virtual Agents). AI Builder er tilgængelig i Power Apps og Power Automate. I denne lektion fokuserer vi på, hvordan du bruger Copilot og AI Builder i Power Apps og Power Automate til at bygge en løsning til vores uddannelsesstartup.

### Copilot i Power Apps

Som en del af Power Platform tilbyder Power Apps et low-code udviklingsmiljø til at bygge apps til at spore, håndtere og interagere med data. Det er en suite af app-udviklingstjenester med en skalerbar dataplatform og mulighed for at forbinde til cloud-tjenester og lokale data. Power Apps gør det muligt at bygge apps, der kører på browsere, tablets og telefoner, og kan deles med kolleger. Power Apps gør det nemt for brugere at komme i gang med app-udvikling via et simpelt interface, så enhver forretningsbruger eller professionel udvikler kan bygge tilpassede apps. App-udviklingsoplevelsen forbedres også med Generativ AI gennem Copilot.

Copilot AI-assistentfunktionen i Power Apps gør det muligt for dig at beskrive, hvilken slags app du har brug for, og hvilken information din app skal spore, indsamle eller vise. Copilot genererer derefter en responsiv Canvas-app baseret på din beskrivelse. Du kan derefter tilpasse appen efter dine behov. AI Copilot genererer og foreslår også en Dataverse-tabel med de felter, du skal bruge til at gemme de data, du ønsker at spore, samt noget eksempeldata. Vi vil se på, hvad Dataverse er, og hvordan du kan bruge det i Power Apps senere i denne lektion. Du kan derefter tilpasse tabellen efter dine behov ved hjælp af AI Copilot-assistentfunktionen gennem samtaletrin. Denne funktion er let tilgængelig fra Power Apps startskærm.

### Copilot i Power Automate

Som en del af Power Platform giver Power Automate brugerne mulighed for at skabe automatiserede workflows mellem applikationer og tjenester. Det hjælper med at automatisere gentagne forretningsprocesser såsom kommunikation, datainindsamling og godkendelse af beslutninger. Dets enkle interface tillader brugere med alle tekniske kompetenceniveauer (fra begyndere til erfarne udviklere) at automatisere arbejdsopgaver. Workflow-udviklingsoplevelsen forbedres også med Generativ AI gennem Copilot.

Copilot AI-assistentfunktionen i Power Automate gør det muligt for dig at beskrive, hvilken slags flow du har brug for, og hvilke handlinger dit flow skal udføre. Copilot genererer derefter et flow baseret på din beskrivelse. Du kan derefter tilpasse flowet efter dine behov. AI Copilot genererer og foreslår også de handlinger, du skal udføre for at automatisere den ønskede opgave. Vi vil senere i denne lektion se på, hvad flows er og hvordan du kan bruge dem i Power Automate. Du kan derefter tilpasse handlingerne efter dine behov ved hjælp af AI Copilot-assistentfunktionen gennem samtaletrin. Denne funktion er let tilgængelig fra Power Automate startskærm.

## Bygning af intelligente agenter med Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (tidligere Power Virtual Agents) er low-code medlemmet i Power Platform til bygning af **AI-agenter** — samtale-copiloter, der kan besvare spørgsmål, tage handlinger og automatisere opgaver på vegne af dine brugere. Ligesom resten af Power Platform bygger du disse agenter i en visuel, naturligsprogs-første oplevelse: du beskriver, hvad du ønsker, at agenten skal gøre, og Copilot Studio hjælper med at udforme dens instruktioner, viden og handlinger.

For vores uddannelsesstartup kunne du bygge en agent, der svarer på studerendes spørgsmål om kurser, tjekker afleveringsfrister og endda sender en e-mail til en underviser — alt sammen uden at skrive kode.

Her er nogle af de nyeste funktioner, der gør Copilot Studio kraftfuld:

- **Generative svar fra din viden**. I stedet for at håndskrive hver samtale, kan du forbinde **videnkilder** — offentlige websider, SharePoint, OneDrive, Dataverse, uploadede filer eller virksomhedens data via connectors — og agenten genererer funderede svar fra dem.

- **Generativ orkestrering**. I stedet for at stole på faste udløsende fraser bruger agenten AI til at forstå en anmodning og dynamisk beslutte, hvilken viden, emner og handlinger der skal kombineres for at opfylde den, inklusive sammenkobling af flere trin.

- **Handlinger og connectors**. Agenter kan *gøre* ting, ikke kun chatte. Du kan give en agent handlinger understøttet af de 1.500+ forudbyggede Power Platform-connectors, Power Automate-flows, brugerdefinerede REST APIs, prompts eller **Model Context Protocol (MCP)**-servere.

- **Autonome agenter**. Agenter er ikke begrænset til at svare i et chatvindue. Du kan bygge **autonome agenter**, der udløses af begivenheder — såsom en ny e-mail, en ny post i Dataverse, eller en fil, der uploades — og derefter handler i baggrunden for at fuldføre en opgave.

- **Multi-agent orkestrering**. Agenter kan kalde andre agenter. En Copilot Studio-agent kan overgive til, eller blive udvidet af, andre agenter, inklusive agenter, der er publiceret til Microsoft 365 Copilot og agenter bygget i Microsoft Foundry.

- **Modelvalg**. Udover de indbyggede modeller kan du bringe modeller fra Microsoft Foundry's modelkatalog for at tilpasse, hvordan din agent resonerer og svarer.

- **Publicer hvor som helst**. Når først bygget, kan en agent publiceres til flere kanaler — Microsoft Teams, Microsoft 365 Copilot, en hjemmeside eller en brugerdefineret app og mere — med sikkerhed, autentificering og analyse håndteret gennem Power Platform's administrationsoplevelse.

Du kan begynde at bygge din første agent på [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) og lære mere i [Microsoft Copilot Studio dokumentationen](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Opgave: Håndtér studerendes opgaver og fakturaer for vores startup ved hjælp af Copilot

Vores startup tilbyder online kurser til studerende. Startup'en er vokset hurtigt og kæmper nu med at følge med efterspørgslen efter sine kurser. Startup'en har ansat dig som Power Platform-udvikler for at hjælpe med at bygge en low code-løsning, der kan hjælpe med at håndtere deres studerendes opgaver og fakturaer. Deres løsning skal kunne hjælpe dem med at spore og håndtere studerendes opgaver gennem en app samt automatisere fakturahåndteringsprocessen via et workflow. Du er blevet bedt om at bruge Generativ AI til at udvikle løsningen.

Når du begynder at bruge Copilot, kan du bruge [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) til at komme i gang med prompts. Dette bibliotek indeholder en liste over prompts, du kan bruge til at bygge apps og flows med Copilot. Du kan også bruge prompts i biblioteket til at få en idé om, hvordan du beskriver dine krav til Copilot.

### Byg en Student Assignment Tracker-app til vores startup

Underviserne i vores startup har haft svært ved at holde styr på studerendes opgaver. De har brugt et regneark til at følge opgaverne, men dette er blevet svært at håndtere, efterhånden som antallet af studerende er steget. De har bedt dig om at bygge en app, der kan hjælpe dem med at spore og håndtere studerendes opgaver. Appen skal gøre det muligt for dem at tilføje nye opgaver, se opgaver, opdatere opgaver og slette opgaver. Appen skal også gøre det muligt for undervisere og studerende at se de opgaver, der er blevet vurderet, og dem som ikke er.

Du vil bygge appen ved hjælp af Copilot i Power Apps efter følgende trin:

1. Naviger til [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) startskærmen.

1. Brug tekstfeltet på startskærmen til at beskrive den app, du ønsker at bygge. For eksempel, **_Jeg vil bygge en app til at spore og håndtere studerendes opgaver_**. Klik på **Send**-knappen for at sende prompten til AI Copilot.

![Beskriv den app, du vil bygge](../../../translated_images/da/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot vil foreslå en Dataverse-tabel med de felter, du behøver for at gemme dataene, du vil spore, og noget eksempeldata. Du kan derefter tilpasse tabellen efter dine behov ved hjælp af AI Copilot-assistentfunktionen gennem samtaletrin.

   > **Vigtigt**: Dataverse er den underliggende dataplatform for Power Platform. Det er en low-code dataplatform til lagring af appens data. Det er en fuldt administreret service, der sikkert lagrer data i Microsoft Cloud og er provisioneret inden for dit Power Platform-miljø. Det leveres med indbyggede datastyringsfunktioner som dataklassificering, datalevelse, finmasket adgangskontrol og mere. Du kan lære mere om Dataverse [her](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Foreslåede felter i din nye tabel](../../../translated_images/da/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Underviserne ønsker at sende e-mails til de studerende, der har afleveret deres opgaver, for at holde dem opdateret om fremskridtet på deres opgaver. Du kan bruge Copilot til at tilføje et nyt felt til tabellen til at gemme den studerendes e-mail. For eksempel kan du bruge følgende prompt for at tilføje et nyt felt til tabellen: **_Jeg ønsker at tilføje en kolonne til at gemme studerendes e-mail_**. Klik på **Send**-knappen for at sende prompten til AI Copilot.

![Tilføjelse af et nyt felt](../../../translated_images/da/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot vil generere et nyt felt, og du kan derefter tilpasse feltet efter dine behov.


1. Når du er færdig med tabellen, skal du klikke på **Opret app**-knappen for at oprette appen.

1. AI Copilot vil generere en responsiv Canvas-app baseret på din beskrivelse. Du kan derefter tilpasse appen, så den opfylder dine behov.

1. For undervisere, der ønsker at sende e-mails til studerende, kan du bruge Copilot til at tilføje en ny skærm til appen. For eksempel kan du bruge følgende prompt til at tilføje en ny skærm til appen: **_Jeg vil tilføje en skærm til at sende e-mails til studerende_**. Klik på **Send**-knappen for at sende prompten til AI Copilot.

![Tilføjelse af en ny skærm via en promptinstruktion](../../../translated_images/da/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot vil generere en ny skærm, og du kan derefter tilpasse skærmen, så den opfylder dine behov.

1. Når du er færdig med appen, skal du klikke på **Gem**-knappen for at gemme appen.

1. For at dele appen med underviserne skal du klikke på **Del**-knappen og derefter klikke på **Del** igen. Du kan derefter dele appen med underviserne ved at indtaste deres e-mailadresser.

> **Din opgave**: Den app, du lige har opbygget, er et godt udgangspunkt, men kan forbedres. Med e-mailfunktionen kan undervisere kun sende e-mails til studerende manuelt ved at skulle skrive deres e-mails. Kan du bruge Copilot til at bygge en automatisering, der gør det muligt for undervisere at sende e-mails til studerende automatisk, når de afleverer deres opgaver? Dit tip er, at med den rigtige prompt kan du bruge Copilot i Power Automate til at bygge dette.

### Byg en fakturainformationstabel til vores startup

Finansafdelingen i vores startup har haft svært ved at holde styr på fakturaer. De har brugt et regneark til at spore fakturaerne, men det er blevet vanskeligt at administrere, efterhånden som antallet af fakturaer er steget. De har bedt dig om at bygge en tabel, der kan hjælpe dem med at gemme, spore og administrere informationen om de modtagne fakturaer. Tabellen skal bruges til at bygge en automatisering, der kan udtrække alle fakturainformationer og gemme dem i tabellen. Tabellen skal også gøre det muligt for finansafdelingen at se fakturaer, der er betalt, og dem, der ikke er betalt.

Power Platform har en underliggende dataplatform kaldet Dataverse, der gør det muligt for dig at lagre data til dine apps og løsninger. Dataverse tilbyder en lavkode-dataplatform til lagring af appens data. Det er en fuldt administreret tjeneste, som sikkert gemmer data i Microsoft Cloud og er provisioneret inden for dit Power Platform-miljø. Den leveres med indbyggede datastyringsfunktioner, såsom dataklassifikation, dataledning, detaljeret adgangskontrol med rollebaseret sikkerhed og mere. Du kan lære mere [om Dataverse her](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Hvorfor skal vi bruge Dataverse til vores startup? Standard- og brugerdefinerede tabeller i Dataverse tilbyder en sikker og skybaseret lagringsmulighed til dine data. Tabeller giver dig mulighed for at lagre forskellige typer data, ligesom du måske bruger flere regneark i en enkelt Excel-projektmappe. Du kan bruge tabeller til at lagre data, der er specifikke for din organisation eller forretningsbehov. Nogle af fordelene ved at bruge Dataverse for vores startup inkluderer, men er ikke begrænset til:

- **Let at administrere**: Både metadata og data gemmes i skyen, så du behøver ikke bekymre dig om, hvordan de gemmes eller administreres. Du kan fokusere på at bygge dine apps og løsninger.

- **Sikkert**: Dataverse tilbyder en sikker og skybaseret lagringsmulighed til dine data. Du kan kontrollere, hvem der har adgang til dataene i dine tabeller, og hvordan de kan få adgang ved hjælp af rollebaseret sikkerhed.

- **Rige metadata**: Datatyper og relationer bruges direkte i Power Apps

- **Logik og validering**: Du kan bruge forretningsregler, beregnede felter og valideringsregler til at håndhæve forretningslogik og opretholde datanøjagtighed.

Nu hvor du ved, hvad Dataverse er, og hvorfor du skal bruge det, lad os se på, hvordan du kan bruge Copilot til at oprette en tabel i Dataverse for at opfylde kravene fra vores finansafdeling.

> **Bemærk**: Du vil bruge denne tabel i næste sektion til at bygge en automatisering, der udtrækker alle fakturainformationer og gemmer dem i tabellen.

For at oprette en tabel i Dataverse ved hjælp af Copilot skal du følge nedenstående trin:

1. Naviger til [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) startskærm.

2. På venstre navigationsbjælke skal du vælge **Tabeller** og derefter klikke på **Beskriv den nye tabel**.

![Vælg ny tabel](../../../translated_images/da/describe-new-table.0792373eb757281e.webp)

1. På skærmen **Beskriv den nye tabel** skal du bruge tekstområdet til at beskrive den tabel, du vil oprette. For eksempel, **_Jeg vil oprette en tabel til at gemme fakturainformation_**. Klik på **Send**-knappen for at sende prompten til AI Copilot.

![Beskriv tabellen](../../../translated_images/da/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot vil foreslå en Dataverse-tabel med de felter, du har brug for til at gemme de data, du vil spore, samt nogle eksempeldata. Du kan derefter tilpasse tabellen, så den opfylder dine behov ved hjælp af AI Copilot-assistentfunktionen gennem samtaletrin.

![Foreslået Dataverse-tabel](../../../translated_images/da/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Finansafdelingen ønsker at sende en e-mail til leverandøren for at opdatere dem om den aktuelle status på deres faktura. Du kan bruge Copilot til at tilføje et nyt felt til tabellen for at gemme leverandørens e-mail. For eksempel kan du bruge følgende prompt til at tilføje et nyt felt til tabellen: **_Jeg vil tilføje en kolonne til at gemme leverandørens e-mail_**. Klik på **Send**-knappen for at sende prompten til AI Copilot.

1. AI Copilot opretter et nyt felt, og du kan derefter tilpasse feltet, så det opfylder dine behov.

1. Når du er færdig med tabellen, skal du klikke på **Opret**-knappen for at oprette tabellen.

## AI-modeller i Power Platform med AI Builder

AI Builder er en lavkode AI-mulighed tilgængelig i Power Platform, der gør det muligt for dig at bruge AI-modeller til at hjælpe dig med at automatisere processer og forudsige resultater. Med AI Builder kan du integrere AI i dine apps og flows, der forbinder til dine data i Dataverse eller i forskellige cloud-datakilder som SharePoint, OneDrive eller Azure.

## Forudbyggede AI-modeller vs. brugerdefinerede AI-modeller

AI Builder leverer to typer AI-modeller: Forudbyggede AI-modeller og brugerdefinerede AI-modeller. Forudbyggede AI-modeller er færdigtrænede AI-modeller, som Microsoft har trænet og gjort tilgængelige i Power Platform. Disse hjælper dig med at tilføje intelligens til dine apps og flows uden at skulle indsamle data og derefter bygge, træne og udgive dine egne modeller. Du kan bruge disse modeller til at automatisere processer og forudsige resultater.

Nogle af de forudbyggede AI-modeller tilgængelige i Power Platform inkluderer:

- **Nøglefraseregistrering**: Denne model udtrækker nøglefraser fra tekst.
- **Sprogdetektion**: Denne model genkender sproget i en tekst.
- **Følelsesanalyse**: Denne model genkender positiv, negativ, neutral eller blandet følelse i tekst.
- **Visittagslæser**: Denne model udtrækker oplysninger fra visitkort.
- **Tekstgenkendelse**: Denne model udtrækker tekst fra billeder.
- **Objektdetektion**: Denne model registrerer og udtrækker objekter fra billeder.
- **Dokumentbehandling**: Denne model udtrækker oplysninger fra formularer.
- **Fakturabehandling**: Denne model udtrækker oplysninger fra fakturaer.

Med brugerdefinerede AI-modeller kan du bringe din egen model ind i AI Builder, så den kan fungere som enhver anden brugerdefineret AI Builder-model og lade dig træne modellen ved hjælp af dine egne data. Du kan bruge disse modeller til at automatisere processer og forudsige resultater i både Power Apps og Power Automate. Når du bruger din egen model, gælder visse begrænsninger. Læs mere om disse [begrænsninger](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI Builder-modeller](../../../translated_images/da/ai-builder-models.8069423b84cfc47f.webp)

## Opgave #2 - Byg et fakturabehandlingsflow for vores startup

Finansafdelingen har haft svært ved at behandle fakturaer. De har brugt et regneark til at spore fakturaerne, men det er blevet vanskeligt at administrere, efterhånden som antallet af fakturaer er steget. De har bedt dig om at bygge en arbejdsproces, der kan hjælpe dem med at behandle fakturaer ved hjælp af AI. Arbejdsprocessen skal gøre det muligt for dem at udtrække oplysninger fra fakturaer og gemme oplysningerne i en Dataverse-tabel. Arbejdsprocessen skal også gøre det muligt for dem at sende en e-mail til finansafdelingen med de udtrukne oplysninger.

Nu hvor du ved, hvad AI Builder er, og hvorfor du skal bruge det, lad os se på, hvordan du kan bruge fakturabehandlings-AI-modellen i AI Builder, som vi tidligere har dækket, til at bygge en arbejdsproces, der kan hjælpe finansafdelingen med at behandle fakturaer.

For at bygge en arbejdsproces, der kan hjælpe finansafdelingen med at behandle fakturaer ved hjælp af fakturabehandlings-AI-modellen i AI Builder, skal du følge trinene nedenfor:

1. Naviger til [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) startskærm.

2. Brug tekstområdet på startskærmen til at beskrive den arbejdsproces, du vil bygge. For eksempel, **_Behandl en faktura, når den ankommer til min indbakke_**. Klik på **Send**-knappen for at sende prompten til AI Copilot.

   ![Copilot power automate](../../../translated_images/da/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot vil foreslå de handlinger, du skal udføre for at automatisere den ønskede opgave. Du kan klikke på **Næste**-knappen for at gennemgå de næste trin.

4. I det næste trin vil Power Automate bede dig om at opsætte de nødvendige forbindelser for flowet. Når du er færdig, skal du klikke på **Opret flow**-knappen for at oprette flowet.

5. AI Copilot vil generere et flow, og du kan derefter tilpasse flowet, så det opfylder dine behov.

6. Opdater flowets trigger, og indstil **Mappe** til den mappe, hvor fakturaerne gemmes. For eksempel kan du sætte mappen til **Indbakke**. Klik på **Vis avancerede indstillinger** og sæt **Kun med vedhæftninger** til **Ja**. Dette sikrer, at flowet kun kører, når en e-mail med en vedhæftning modtages i mappen.

7. Fjern følgende handlinger fra flowet: **HTML til tekst**, **Sammensæt**, **Sammensæt 2**, **Sammensæt 3** og **Sammensæt 4**, fordi du ikke vil bruge dem.

8. Fjern **Betingelse**-handlingen fra flowet, fordi du ikke vil bruge den. Det skal se ud som på følgende skærmbillede:

   ![power automate, fjern handlinger](../../../translated_images/da/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Klik på **Tilføj en handling**-knappen og søg efter **Dataverse**. Vælg handlingen **Tilføj en ny række**.

10. På handlingen **Udtræk information fra fakturaer** skal du opdatere **Faktura-fil** til at pege på **Vedhæftningsindhold** fra e-mailen. Dette sikrer, at flowet udtrækker oplysninger fra fakturaens vedhæftning.

11. Vælg den **Tabel**, du oprettede tidligere. For eksempel kan du vælge tabellen **Fakturaoplysninger**. Vælg det dynamiske indhold fra den forrige handling for at udfylde følgende felter:

    - ID
    - Beløb
    - Dato
    - Navn
    - Status - Indstil **Status** til **Afventer**.
    - Leverandørens e-mail - Brug det dynamiske indhold **Fra** fra triggeren **Når en ny e-mail ankommer**.

    ![power automate tilføj række](../../../translated_images/da/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Når du er færdig med flowet, skal du klikke på **Gem**-knappen for at gemme flowet. Du kan derefter teste flowet ved at sende en e-mail med en faktura til den mappe, du har angivet i triggeren.

> **Din opgave**: Det flow, du lige har bygget, er et godt udgangspunkt. Nu skal du tænke på, hvordan du kan bygge en automatisering, som gør det muligt for vores finansafdeling at sende en e-mail til leverandøren for at opdatere dem om den aktuelle status på deres faktura. Dit tip: Flowet skal køre, når status på fakturaen ændres.

## Brug en tekstgenererings-AI-model i Power Automate

Create Text med GPT AI-modellen i AI Builder gør det muligt for dig at generere tekst baseret på en prompt og drives af Microsoft Azure OpenAI Service. Med denne mulighed kan du integrere GPT (Generative Pre-Trained Transformer) teknologi i dine apps og flows til at opbygge en række automatiserede flows og indsigtfulde applikationer.

GPT-modeller gennemgår omfattende træning på store mængder data, hvilket gør dem i stand til at producere tekst, der ligner menneskeligt sprog, når de får en prompt. Når de integreres med arbejdsprocesautomatisering, kan AI-modeller som GPT anvendes til at strømline og automatisere en bred vifte af opgaver.

For eksempel kan du bygge flows til automatisk at generere tekst til forskellige anvendelser, såsom: udkast til e-mails, produktbeskrivelser og mere. Du kan også bruge modellen til at generere tekst til forskellige apps, såsom chatbots og kundeserviceapps, der gør det muligt for kundeservicemedarbejdere at besvare kundehenvendelser effektivt og hurtigt.

![opret en prompt](../../../translated_images/da/create-prompt-gpt.69d429300c2e870a.webp)


For at lære, hvordan du bruger denne AI-model i Power Automate, gennemgå modulet [Tilføj intelligens med AI Builder og GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Godt arbejde! Fortsæt din læring

Efter at have gennemført denne lektion, tjek vores [Samling af læring om generativ AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at øge din viden om generativ AI!

Vil du tilpasse og få mere ud af Copilot? Udforsk [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — en samling af anvisninger, agenter, færdigheder og konfigurationer bidraget af fællesskabet, der hjælper dig med at få mest muligt ud af GitHub Copilot.

Gå til Lektion 11, hvor vi ser på, hvordan man [integrerer generativ AI med Funktionsopkald](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->