# Low Code AI-toepassingen bouwen

[![Low Code AI-toepassingen bouwen](../../../translated_images/nl/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

## Introductie

Nu we hebben geleerd hoe we beeldgenererende toepassingen bouwen, laten we het hebben over low code. Generatieve AI kan voor verschillende gebieden worden gebruikt, waaronder low code, maar wat is low code en hoe kunnen we AI daaraan toevoegen?

Het bouwen van apps en oplossingen is eenvoudiger geworden voor traditionele ontwikkelaars en niet-ontwikkelaars dankzij Low Code Development Platforms. Low Code Development Platforms stellen je in staat apps en oplossingen te bouwen met weinig tot geen code. Dit wordt bereikt door een visuele ontwikkelomgeving te bieden waarin je componenten kunt slepen en neerzetten om apps en oplossingen te bouwen. Dit maakt het mogelijk apps en oplossingen sneller en met minder middelen te bouwen. In deze les duiken we diep in hoe Low Code te gebruiken en hoe je low code ontwikkeling kunt verbeteren met AI met behulp van Power Platform.

Power Platform biedt organisaties de mogelijkheid hun teams te versterken om eigen oplossingen te bouwen via een intuïtieve low-code of no-code omgeving. Deze omgeving helpt het proces van het bouwen van oplossingen te vereenvoudigen. Met Power Platform kunnen oplossingen in dagen of weken worden gebouwd in plaats van maanden of jaren. Power Platform bestaat uit vijf kernproducten: Power Apps, Power Automate, Power BI, Power Pages en Copilot Studio.

Deze les behandelt:

- Introductie tot Generatieve AI in Power Platform
- Introductie tot Copilot en hoe het te gebruiken
- Gebruik van Generatieve AI om apps en flows te bouwen in Power Platform
- Begrijpen van de AI-modellen in Power Platform met AI Builder
- Intelligente agenten bouwen met Microsoft Copilot Studio

## Leerdoelen

Aan het einde van deze les zul je in staat zijn om:

- Begrijpen hoe Copilot werkt in Power Platform.

- Een Student Assignment Tracker App bouwen voor onze educatieve startup.

- Een Invoice Processing Flow bouwen die AI gebruikt om informatie uit facturen te halen.

- Beste praktijken toepassen bij het gebruik van het Create Text met GPT AI-model.

- Begrijpen wat Microsoft Copilot Studio is en hoe je intelligente agenten bouwt met deze tool.

De tools en technologieën die je in deze les zult gebruiken zijn:

- **Power Apps**, voor de Student Assignment Tracker app, die een low-code ontwikkelomgeving biedt voor het bouwen van apps om gegevens te volgen, beheren en ermee te interacteren.

- **Dataverse**, voor het opslaan van de data voor de Student Assignment Tracker app waar Dataverse een low-code dataplatform biedt voor het opslaan van app-gegevens.

- **Power Automate**, voor de Invoice Processing flow waar je een low-code ontwikkelomgeving gebruikt om workflows te bouwen die het factuurverwerkingsproces automatiseren.

- **AI Builder**, voor het Invoice Processing AI-model waar je kant-en-klare AI-modellen gebruikt om facturen voor onze startup te verwerken.

## Generatieve AI in Power Platform

Het verbeteren van low-code ontwikkeling en toepassingen met generatieve AI is een belangrijk aandachtsgebied voor Power Platform. Het doel is om iedereen in staat te stellen AI-gedreven apps, sites, dashboards te bouwen en processen met AI te automatiseren, _zonder dat daarvoor enige datawetenschappelijke expertise nodig is_. Dit doel wordt bereikt door generatieve AI te integreren in de low-code ontwikkelervaring van Power Platform in de vorm van Copilot en AI Builder.

### Hoe werkt dit?

Copilot is een AI-assistent die je helpt om Power Platform-oplossingen te bouwen door je requirements te beschrijven in een reeks conversatiestappen in natuurlijke taal. Je kunt bijvoorbeeld aan je AI-assistent vertellen welke velden je app zal gebruiken en het zal zowel de app als het onderliggende datamodel creëren of je kunt specificeren hoe je een flow in Power Automate wilt instellen.

Je kunt Copilot-aangedreven functionaliteiten gebruiken als een functie in je app-schermen om gebruikers via conversatie-interacties inzicht te laten krijgen.

AI Builder is een low-code AI-mogelijkheid die beschikbaar is in Power Platform en waarmee je AI-modellen kunt gebruiken om processen te automatiseren en uitkomsten te voorspellen. Met AI Builder kun je AI toevoegen aan je apps en flows die verbinding maken met je data in Dataverse of diverse cloud data bronnen zoals SharePoint, OneDrive of Azure.

Copilot is beschikbaar in alle Power Platform-producten: Power Apps, Power Automate, Power BI, Power Pages en Copilot Studio (voorheen Power Virtual Agents). AI Builder is beschikbaar in Power Apps en Power Automate. In deze les richten we ons op het gebruik van Copilot en AI Builder in Power Apps en Power Automate om een oplossing voor onze educatieve startup te bouwen.

### Copilot in Power Apps

Als onderdeel van Power Platform biedt Power Apps een low-code ontwikkelomgeving om apps te bouwen waarmee je data kunt volgen, beheren en ermee kunt interacteren. Het is een suite van app-ontwikkelingsdiensten met een schaalbaar dataplatform en de mogelijkheid om te verbinden met cloud-diensten en on-premises data. Power Apps stelt je in staat apps te bouwen die draaien op browsers, tablets en telefoons en die je met collega’s kunt delen. Power Apps begeleidt gebruikers eenvoudig in app-ontwikkeling met een eenvoudige interface, zodat elke zakelijke gebruiker of professionele ontwikkelaar aangepaste apps kan bouwen. De app-ontwikkelingservaring wordt ook verbeterd met Generative AI via Copilot.

De Copilot AI-assistent functie in Power Apps stelt je in staat te beschrijven wat voor soort app je nodig hebt en welke informatie je app moet volgen, verzamelen of tonen. Copilot genereert dan een responsieve Canvas-app op basis van je beschrijving. Je kunt de app vervolgens aanpassen aan je wensen. De AI Copilot genereert ook en stelt een Dataverse Tabel voor met de velden die je nodig hebt om de data op te slaan die je wilt volgen en enkele voorbeeldgegevens. We zullen later in deze les bekijken wat Dataverse is en hoe je dit in Power Apps kunt gebruiken. Je kunt vervolgens de tabel aanpassen aan je wensen via de AI Copilot assistent functie met behulp van conversatiestappen. Deze functie is direct beschikbaar vanaf het Power Apps startscherm.

### Copilot in Power Automate

Als onderdeel van Power Platform stelt Power Automate gebruikers in staat geautomatiseerde workflows te creëren tussen applicaties en diensten. Het helpt bij het automatiseren van repetitieve bedrijfsprocessen zoals communicatie, dataverzameling en goedkeuringen van beslissingen. De eenvoudige interface maakt het mogelijk voor gebruikers van elk technisch niveau (van beginners tot ervaren ontwikkelaars) om werktaken te automatiseren. De workflow-ontwikkelingservaring wordt ook verbeterd met Generative AI via Copilot.

De Copilot AI-assistent functie in Power Automate stelt je in staat te beschrijven wat voor soort flow je nodig hebt en welke acties je flow moet uitvoeren. Copilot genereert vervolgens een flow gebaseerd op je beschrijving. Je kunt de flow dan aanpassen aan je wensen. De AI Copilot genereert ook en stelt de acties voor die je nodig hebt om de taak die je wilt automatiseren uit te voeren. We zullen later in deze les bekijken wat flows zijn en hoe je die in Power Automate kunt gebruiken. Je kunt de acties aanpassen aan je wensen via de AI Copilot assistent functie met behulp van conversatiestappen. Deze functie is direct beschikbaar vanaf het Power Automate startscherm.

## Intelligente agenten bouwen met Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (voorheen Power Virtual Agents) is het low-code lid van Power Platform voor het bouwen van **AI-agenten** — conversationele copiloten die vragen kunnen beantwoorden, acties kunnen uitvoeren en taken kunnen automatiseren namens jouw gebruikers. Net als de rest van Power Platform bouw je deze agenten in een visuele, natural-language-first ervaring: je beschrijft wat je wilt dat de agent doet, en Copilot Studio helpt bij het opzetten van instructies, kennis en acties.

Voor onze educatieve startup kun je bijvoorbeeld een agent bouwen die vragen van studenten over cursussen beantwoordt, deadlines van opdrachten controleert en zelfs instructeurs per e-mail informeert — allemaal zonder code te schrijven.

Hier zijn enkele van de nieuwste mogelijkheden die Copilot Studio krachtig maken:

- **Generatieve antwoorden uit je kennis**. In plaats van elke conversatie handmatig te schrijven, kun je **kennisbronnen** verbinden — openbare websites, SharePoint, OneDrive, Dataverse, geüploade bestanden of bedrijfsdata via connectors — en genereert de agent hieruit gefundeerde antwoorden.

- **Generatieve orkestratie**. In plaats van te vertrouwen op starre triggerzinnen, gebruikt de agent AI om een verzoek te begrijpen en dynamisch te beslissen welke kennis, onderwerpen en acties te combineren om het te vervullen, inclusief het achtereenvolgens uitvoeren van meerdere stappen.

- **Acties en connectors**. Agenten kunnen dingen *doen*, niet alleen chatten. Je kunt een agent acties geven ondersteund door meer dan 1.500 vooraf gebouwde Power Platform-connectors, Power Automate-flows, aangepaste REST-API’s, prompts of **Model Context Protocol (MCP)** servers.

- **Autonome agenten**. Agenten zijn niet beperkt tot reageren in een chatvenster. Je kunt **autonome agenten** bouwen die worden geactiveerd door gebeurtenissen — zoals een nieuwe e-mail, een nieuwe record in Dataverse, of een bestand dat is geüpload — en vervolgens op de achtergrond een taak voltooien.

- **Multi-agent orkestratie**. Agenten kunnen andere agenten aanroepen. Een Copilot Studio-agent kan de overdracht doen naar, of worden uitgebreid door, andere agenten, inclusief agenten gepubliceerd in Microsoft 365 Copilot en agenten gebouwd in Microsoft Foundry.

- **Modelkeuze**. Naast de ingebouwde modellen kun je modellen uit de Microsoft Foundry modelcatalogus gebruiken om aan te passen hoe je agent redeneert en reageert.

- **Overal publiceren**. Eenmaal gebouwd, kan een agent worden gepubliceerd naar meerdere kanalen — Microsoft Teams, Microsoft 365 Copilot, een website of aangepaste app en meer — met beveiliging, authenticatie en analyses beheerd via de Power Platform beheerderservaring.

Je kunt je eerste agent bouwen op [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) en meer leren in de [Microsoft Copilot Studio documentatie](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Opdracht: Beheer studentenopdrachten en facturen voor onze startup, met Copilot

Onze startup biedt online cursussen aan studenten. De startup is snel gegroeid en worstelt nu om aan de vraag naar haar cursussen te voldoen. De startup heeft jou ingehuurd als Power Platform-ontwikkelaar om ze te helpen een low code-oplossing te bouwen om hun studentenopdrachten en facturen te beheren. Hun oplossing moet hen helpen studentenopdrachten bij te houden en te beheren via een app en het factuurverwerkingsproces automatiseren via een workflow. Je bent gevraagd Generatieve AI te gebruiken om de oplossing te ontwikkelen.

Wanneer je begint met het gebruik van Copilot, kun je de [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) gebruiken om te starten met prompts. Deze bibliotheek bevat een lijst met prompts die je kunt gebruiken om apps en flows te bouwen met Copilot. Je kunt de prompts in de bibliotheek ook gebruiken om een idee te krijgen hoe je je wensen aan Copilot kunt beschrijven.

### Bouw een Student Assignment Tracker App voor Onze Startup

De docenten bij onze startup hebben moeite met het bijhouden van studentenopdrachten. Ze hebben een spreadsheet gebruikt om de opdrachten te volgen, maar dit is moeilijk te beheren geworden met het toenemende aantal studenten. Ze hebben jou gevraagd een app te bouwen die hen helpt studentenopdrachten te volgen en te beheren. De app moet hen in staat stellen nieuwe opdrachten toe te voegen, opdrachten te bekijken, opdrachten bij te werken en opdrachten te verwijderen. De app moet ook docenten en studenten in staat stellen om de opdrachten te zien die zijn beoordeeld en die niet zijn beoordeeld.

Je bouwt de app met Copilot in Power Apps volgens de onderstaande stappen:

1. Ga naar het [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) startscherm.

1. Gebruik het tekstvak op het startscherm om de app te beschrijven die je wilt bouwen. Bijvoorbeeld, **_Ik wil een app bouwen om studentenopdrachten te volgen en beheren_**. Klik op de **Verstuur** knop om de prompt naar de AI Copilot te sturen.

![Beschrijf de app die je wilt bouwen](../../../translated_images/nl/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. De AI Copilot zal een Dataverse Tabel met de velden suggereren die je nodig hebt om de data te bewaren die je wilt volgen en enkele voorbeeldgegevens. Je kunt vervolgens de tabel aanpassen aan je wensen via de AI Copilot assistent functie met behulp van conversatiestappen.

   > **Belangrijk**: Dataverse is het onderliggende dataplatform voor Power Platform. Het is een low-code dataplatform voor het opslaan van app-gegevens. Het is een volledig beheerde service die data veilig opslaat in de Microsoft Cloud en is geconfigureerd binnen je Power Platform-omgeving. Het wordt geleverd met ingebouwde databeheerfuncties, zoals dataclassificatie, datalinieage, fijnmazige toegangscontrole en meer. Je kunt hier meer over Dataverse leren [hier](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Voorgestelde velden in je nieuwe tabel](../../../translated_images/nl/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Docenten willen e-mails sturen naar studenten die hun opdrachten hebben ingediend om hen op de hoogte te houden van de voortgang van hun opdrachten. Je kunt Copilot gebruiken om een nieuw veld toe te voegen aan de tabel om het e-mailadres van de student op te slaan. Bijvoorbeeld, je kunt de volgende prompt gebruiken om een nieuw veld aan de tabel toe te voegen: **_Ik wil een kolom toevoegen om student e-mail op te slaan_**. Klik op de **Verstuur** knop om de prompt naar de AI Copilot te sturen.

![Een nieuw veld toevoegen](../../../translated_images/nl/copilot-new-column.35e15ff21acaf274.webp)

1. De AI Copilot zal een nieuw veld genereren en je kunt het veld vervolgens aanpassen aan je wensen.


1. Zodra u klaar bent met de tabel, klikt u op de knop **Maak app** om de app te maken.

1. De AI Copilot zal een responsieve Canvas-app genereren op basis van uw beschrijving. U kunt de app vervolgens aanpassen aan uw behoeften.

1. Voor docenten om e-mails naar studenten te sturen, kunt u Copilot gebruiken om een nieuw scherm aan de app toe te voegen. U kunt bijvoorbeeld de volgende prompt gebruiken om een nieuw scherm toe te voegen aan de app: **_Ik wil een scherm toevoegen om e-mails naar studenten te sturen_**. Klik op de knop **Verzenden** om de prompt naar de AI Copilot te sturen.

![Adding a new screen via a prompt instruction](../../../translated_images/nl/copilot-new-screen.2e0bef7132a17392.webp)

1. De AI Copilot zal een nieuw scherm genereren en u kunt het scherm vervolgens aanpassen aan uw behoeften.

1. Zodra u klaar bent met de app, klikt u op de knop **Opslaan** om de app op te slaan.

1. Om de app met de docenten te delen, klikt u op de knop **Delen** en vervolgens nogmaals op de knop **Delen**. U kunt de app dan delen met de docenten door hun e-mailadressen in te voeren.

> **Uw huiswerk**: De app die u zojuist heeft gebouwd is een goed begin, maar kan verbeterd worden. Met de e-mailfunctie kunnen docenten alleen handmatig e-mails sturen naar studenten door hun e-mailadressen te typen. Kunt u met Copilot een automatisering bouwen die docenten in staat stelt om automatisch e-mails naar studenten te sturen wanneer zij hun opdrachten indienen? Uw hint is dat u met de juiste prompt Copilot in Power Automate kunt gebruiken om dit te bouwen.

### Bouw een tabel met factuurinformatie voor onze startup

Het financiën-team van onze startup heeft moeite gehad met het bijhouden van facturen. Ze hebben een spreadsheet gebruikt om de facturen bij te houden, maar dit is moeilijk te beheren geworden naarmate het aantal facturen is gegroeid. Ze hebben u gevraagd een tabel te bouwen die hen helpt om de informatie van de ontvangen facturen op te slaan, bij te houden en te beheren. De tabel moet gebruikt worden om een automatisering te bouwen die alle factuurinformatie zal extraheren en opslaan in de tabel. De tabel moet ook het financiën-team in staat stellen om te zien welke facturen betaald zijn en welke niet.

Het Power Platform heeft een onderliggend gegevensplatform genaamd Dataverse dat u in staat stelt de gegevens voor uw apps en oplossingen op te slaan. Dataverse biedt een low-code gegevensplatform voor het opslaan van de gegevens van de app. Het is een volledig beheerde service die gegevens veilig opslaat in de Microsoft-cloud en binnen uw Power Platform-omgeving wordt voorzien. Het wordt geleverd met ingebouwde gegevensbeheerfuncties, zoals dataclassificatie, gegevensherkomst, fijnmazige toegangscontrole en meer. U kunt meer leren [over Dataverse hier](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Waarom zouden we Dataverse gebruiken voor onze startup? De standaard- en aangepaste tabellen binnen Dataverse bieden een veilige en cloudgebaseerde opslagoptie voor uw gegevens. Tabellen laten u verschillende soorten gegevens opslaan, net zoals u meerdere werkbladen in één Excel-werkmap zou kunnen gebruiken. U kunt tabellen gebruiken om gegevens op te slaan die specifiek zijn voor uw organisatie of zakelijke behoeften. Enkele voordelen die onze startup zal verkrijgen door het gebruik van Dataverse zijn onder andere:

- **Gemakkelijk te beheren**: Zowel de metadata als de gegevens worden in de cloud opgeslagen, dus u hoeft zich geen zorgen te maken over de details van hoe ze worden opgeslagen of beheerd. U kunt zich richten op het bouwen van uw apps en oplossingen.

- **Veilig**: Dataverse biedt een veilige en cloudgebaseerde opslagoptie voor uw gegevens. U kunt beheren wie toegang heeft tot de gegevens in uw tabellen en hoe ze toegang hebben met behulp van rolgebaseerde beveiliging.

- **Rijke metadata**: Datatypes en relaties worden rechtstreeks binnen Power Apps gebruikt

- **Logica en validatie**: U kunt bedrijfsregels, berekende velden en validatieregels gebruiken om bedrijfslogica af te dwingen en datanauwkeurigheid te behouden.

Nu u weet wat Dataverse is en waarom u het moet gebruiken, laten we kijken hoe u Copilot kunt gebruiken om een tabel in Dataverse te maken die aan de eisen van ons financiën-team voldoet.

> **Opmerking** : U zult deze tabel in het volgende gedeelte gebruiken om een automatisering te bouwen die alle factuurinformatie zal extraheren en opslaan in de tabel.

Om een tabel in Dataverse te maken met Copilot, volgt u de onderstaande stappen:

1. Navigeer naar het [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) startscherm.

2. Selecteer in de linker navigatiebalk **Tabellen** en klik vervolgens op **Beschrijf de nieuwe tabel**.

![Select new table](../../../translated_images/nl/describe-new-table.0792373eb757281e.webp)

1. Gebruik op het scherm **Beschrijf de nieuwe tabel** het tekstvak om de tabel te beschrijven die u wilt maken. Bijvoorbeeld, **_Ik wil een tabel maken om factuurinformatie op te slaan_**. Klik op de knop **Verzenden** om de prompt naar de AI Copilot te sturen.

![Describe the table](../../../translated_images/nl/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. De AI Copilot zal een Dataverse-tabel voorstellen met de velden die u nodig hebt om de gegevens die u wilt bijhouden op te slaan en met enkele voorbeeldgegevens. U kunt vervolgens de tabel aanpassen aan uw behoeften met behulp van de AI Copilot assistentfunctie via gesprekgestuurde stappen.

![Suggested Dataverse table](../../../translated_images/nl/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Het financiën-team wil een e-mail naar de leverancier sturen om hen te informeren over de huidige status van hun factuur. U kunt Copilot gebruiken om een nieuw veld aan de tabel toe te voegen om het e-mailadres van de leverancier op te slaan. U kunt bijvoorbeeld de volgende prompt gebruiken om een nieuw veld toe te voegen: **_Ik wil een kolom toevoegen om leverancier e-mail op te slaan_**. Klik op de knop **Verzenden** om de prompt naar de AI Copilot te sturen.

1. De AI Copilot zal een nieuw veld genereren en u kunt het veld vervolgens aanpassen aan uw behoeften.

1. Zodra u klaar bent met de tabel, klikt u op de knop **Maken** om de tabel te maken.

## AI-modellen in Power Platform met AI Builder

AI Builder is een low-code AI-functionaliteit die beschikbaar is in Power Platform en waarmee u AI-modellen kunt gebruiken om processen te automatiseren en resultaten te voorspellen. Met AI Builder kunt u AI in uw apps en flows integreren die verbinding maken met uw gegevens in Dataverse of in verschillende cloudgegevensbronnen, zoals SharePoint, OneDrive of Azure.

## Vooraf gebouwde AI-modellen versus aangepaste AI-modellen

AI Builder biedt twee soorten AI-modellen: Vooraf gebouwde AI-modellen en Aangepaste AI-modellen. Vooraf gebouwde AI-modellen zijn kant-en-klare AI-modellen die door Microsoft zijn getraind en beschikbaar zijn in Power Platform. Deze helpen u intelligentie toe te voegen aan uw apps en flows zonder dat u zelf gegevens hoeft te verzamelen, modellen hoeft te bouwen, te trainen en te publiceren. U kunt deze modellen gebruiken om processen te automatiseren en resultaten te voorspellen.

Enkele van de vooraf gebouwde AI-modellen die beschikbaar zijn in Power Platform zijn:

- **Kernzinextractie**: Dit model haalt sleutelzinnen uit tekst.
- **Taalherkenning**: Dit model detecteert de taal van een tekst.
- **Sentimentanalyse**: Dit model detecteert een positieve, negatieve, neutrale of gemengde stemming in tekst.
- **Visitekaartjeslezer**: Dit model haalt informatie uit visitekaartjes.
- **Tekstherkenning**: Dit model haalt tekst uit afbeeldingen.
- **Objectdetectie**: Dit model detecteert en haalt objecten uit afbeeldingen.
- **Documentverwerking**: Dit model haalt informatie uit formulieren.
- **Factuurverwerking**: Dit model haalt informatie uit facturen.

Met aangepaste AI-modellen kunt u uw eigen model in AI Builder brengen zodat het functioneert als elk ander AI Builder aangepast model, waarmee u het model kunt trainen met uw eigen gegevens. U kunt deze modellen gebruiken om processen te automatiseren en resultaten te voorspellen zowel in Power Apps als in Power Automate. Bij het gebruik van uw eigen model gelden bepaalde beperkingen. Lees meer over deze [beperkingen](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/nl/ai-builder-models.8069423b84cfc47f.webp)

## Opdracht #2 - Bouw een factuurverwerkingsflow voor onze startup

Het financiën-team heeft moeite met het verwerken van facturen. Ze hebben een spreadsheet gebruikt om facturen bij te houden, maar naarmate het aantal facturen is gegroeid, is het moeilijk geworden dit te beheren. Ze hebben u gevraagd een workflow te bouwen die hen helpt facturen te verwerken met AI. De workflow moet hen in staat stellen om informatie uit facturen te extraheren en de informatie op te slaan in een Dataverse-tabel. De workflow moet hen ook in staat stellen een e-mail te sturen naar het financiën-team met de geëxtraheerde informatie.

Nu u weet wat AI Builder is en waarom u het moet gebruiken, laten we kijken hoe u het Factuurverwerkings-AI-model in AI Builder, dat we eerder hebben besproken, kunt gebruiken om een workflow te bouwen die het financiën-team helpt bij het verwerken van facturen.

Om een workflow te bouwen die het financiën-team helpt facturen te verwerken met behulp van het Factuurverwerkings-AI-model in AI Builder, volgt u de onderstaande stappen:

1. Navigeer naar het [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) startscherm.

2. Gebruik het tekstvak op het startscherm om de workflow te beschrijven die u wilt bouwen. Bijvoorbeeld, **_Verwerk een factuur zodra deze in mijn mailbox aankomt_**. Klik op de knop **Verzenden** om de prompt naar de AI Copilot te sturen.

   ![Copilot power automate](../../../translated_images/nl/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. De AI Copilot zal de acties voorstellen die nodig zijn om de taak te automatiseren die u wilt uitvoeren. U kunt op de knop **Volgende** klikken om door de volgende stappen te gaan.

4. In de volgende stap zal Power Automate u vragen om de verbindingen die voor de flow nodig zijn op te zetten. Zodra u klaar bent, klikt u op de knop **Flow maken** om de flow te maken.

5. De AI Copilot zal een flow genereren en u kunt de flow vervolgens aanpassen aan uw behoeften.

6. Werk de trigger van de flow bij en stel de **Map** in op de map waar de facturen worden opgeslagen. U kunt bijvoorbeeld de map **Inbox** instellen. Klik op **Geavanceerde opties weergeven** en stel **Alleen met bijlagen** in op **Ja**. Zo wordt ervoor gezorgd dat de flow alleen draait wanneer een e-mail met een bijlage wordt ontvangen in de map.

7. Verwijder de volgende acties uit de flow: **HTML naar tekst**, **Componeren**, **Componeren 2**, **Componeren 3** en **Componeren 4**, want u zult deze niet gebruiken.

8. Verwijder de actie **Voorwaarde** uit de flow, omdat u die niet zult gebruiken. Het zou eruit moeten zien als de volgende screenshot:

   ![power automate, remove actions](../../../translated_images/nl/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Klik op de knop **Een actie toevoegen** en zoek naar **Dataverse**. Selecteer de actie **Een nieuwe rij toevoegen**.

10. Bij de actie **Informatie uit facturen extraheren**, werk het veld **Factuurbestand** bij om te verwijzen naar de **Bijlage-inhoud** van de e-mail. Dit zorgt ervoor dat de flow informatie uit de factuurbijlage extraheert.

11. Selecteer de tabel die u eerder hebt gemaakt. U kunt bijvoorbeeld de tabel **Factuurinformatie** selecteren. Kies de dynamische inhoud van de vorige actie om de volgende velden te vullen:

    - ID
    - Bedrag
    - Datum
    - Naam
    - Status - Stel de **Status** in op **In afwachting**.
    - Leverancier e-mail - Gebruik de dynamische inhoud **Van** van de trigger **Wanneer een nieuwe e-mail aankomt**.

    ![power automate add row](../../../translated_images/nl/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Zodra u klaar bent met de flow, klikt u op de knop **Opslaan** om de flow op te slaan. U kunt de flow dan testen door een e-mail met een factuur te sturen naar de map die u in de trigger heeft opgegeven.

> **Uw huiswerk**: De flow die u zojuist heeft gebouwd is een goed begin. Nu moet u nadenken over hoe u een automatisering kunt bouwen die het financiën-team in staat stelt om een e-mail te sturen naar de leverancier om hen te informeren over de huidige status van hun factuur. Uw hint: de flow moet draaien wanneer de status van de factuur verandert.

## Gebruik een tekstgeneratie-AI-model in Power Automate

Het model Create Text with GPT in AI Builder stelt u in staat om tekst te genereren op basis van een prompt en wordt aangedreven door de Microsoft Azure OpenAI-service. Met deze functionaliteit kunt u GPT (Generative Pre-Trained Transformer) technologie integreren in uw apps en flows om diverse geautomatiseerde flows en inzichtgevende toepassingen te bouwen.

GPT-modellen worden uitgebreid getraind op enorme hoeveelheden gegevens, waardoor ze tekst kunnen produceren die sterk lijkt op menselijke taal wanneer ze een prompt krijgen. Wanneer ze geïntegreerd zijn met workflowautomatisering, kunnen AI-modellen zoals GPT worden ingezet om een breed scala aan taken te stroomlijnen en te automatiseren.

U kunt bijvoorbeeld flows bouwen om automatisch tekst te genereren voor allerlei toepassingen, zoals concepten van e-mails, productbeschrijvingen en meer. U kunt het model ook gebruiken om tekst te genereren voor diverse apps, zoals chatbots en klantenservice-apps waarmee klantenservicemedewerkers effectief en efficiënt kunnen reageren op klantvragen.

![create a prompt](../../../translated_images/nl/create-prompt-gpt.69d429300c2e870a.webp)


Om te leren hoe je dit AI-model in Power Automate gebruikt, doorloop je de module [Intelligentie toevoegen met AI Builder en GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Geweldig Werk! Ga Door met Je Leerproces

Nadat je deze les hebt afgerond, bekijk dan onze [Generative AI Learning verzameling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generative AI verder te ontwikkelen!

Wil je Copilot aanpassen en er meer uit halen? Verken [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — een community-gedragen verzameling van instructies, agents, vaardigheden en configuraties om je te helpen het meeste uit GitHub Copilot te halen.

Ga naar Les 11 waar we bekijken hoe je [Generative AI integreert met Function Calling](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->