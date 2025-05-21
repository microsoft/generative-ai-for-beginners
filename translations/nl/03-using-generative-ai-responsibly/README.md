<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:43:46+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "nl"
}
-->
# Verantwoord Gebruik van Generatieve AI

> _Klik op de afbeelding hierboven om de video van deze les te bekijken_

Het is gemakkelijk om gefascineerd te raken door AI en in het bijzonder generatieve AI, maar je moet overwegen hoe je het op een verantwoorde manier zou gebruiken. Je moet nadenken over zaken als hoe je ervoor zorgt dat de output eerlijk, niet-schadelijk en meer is. Dit hoofdstuk is bedoeld om je de genoemde context te bieden, wat je moet overwegen en hoe je actieve stappen kunt nemen om je AI-gebruik te verbeteren.

## Introductie

Deze les zal behandelen:

- Waarom je Verantwoordelijke AI zou moeten prioriteren bij het bouwen van Generatieve AI-toepassingen.
- Kernprincipes van Verantwoordelijke AI en hoe ze zich verhouden tot Generatieve AI.
- Hoe je deze principes van Verantwoordelijke AI in de praktijk kunt brengen via strategie en tools.

## Leerdoelen

Na het voltooien van deze les weet je:

- Het belang van Verantwoordelijke AI bij het bouwen van Generatieve AI-toepassingen.
- Wanneer je moet nadenken over en de kernprincipes van Verantwoordelijke AI moet toepassen bij het bouwen van Generatieve AI-toepassingen.
- Welke tools en strategieën beschikbaar zijn om het concept van Verantwoordelijke AI in de praktijk te brengen.

## Principes van Verantwoordelijke AI

De opwinding over Generatieve AI is nog nooit zo groot geweest. Deze opwinding heeft veel nieuwe ontwikkelaars, aandacht en financiering naar dit gebied gebracht. Hoewel dit erg positief is voor iedereen die producten en bedrijven wil bouwen met Generatieve AI, is het ook belangrijk dat we verantwoordelijk te werk gaan.

Gedurende deze cursus richten we ons op het bouwen van onze startup en ons AI-onderwijsproduct. We zullen de principes van Verantwoordelijke AI gebruiken: Eerlijkheid, Inclusiviteit, Betrouwbaarheid/Veiligheid, Beveiliging & Privacy, Transparantie en Verantwoording. Met deze principes zullen we onderzoeken hoe ze zich verhouden tot ons gebruik van Generatieve AI in onze producten.

## Waarom Verantwoordelijke AI Prioriteren

Bij het bouwen van een product leidt een mensgerichte benadering waarbij je het beste belang van je gebruiker in gedachten houdt tot de beste resultaten.

Het unieke van Generatieve AI is het vermogen om nuttige antwoorden, informatie, begeleiding en inhoud voor gebruikers te creëren. Dit kan zonder veel handmatige stappen, wat tot zeer indrukwekkende resultaten kan leiden. Zonder goede planning en strategieën kan het helaas ook leiden tot enkele schadelijke resultaten voor je gebruikers, je product en de samenleving als geheel.

Laten we kijken naar enkele (maar niet alle) van deze potentieel schadelijke resultaten:

### Hallucinaties

Hallucinaties is een term die wordt gebruikt om te beschrijven wanneer een LLM inhoud produceert die ofwel volledig onzinnig is of iets waarvan we weten dat het feitelijk onjuist is op basis van andere informatiebronnen.

Laten we bijvoorbeeld aannemen dat we een functie bouwen voor onze startup waarmee studenten historische vragen aan een model kunnen stellen. Een student stelt de vraag `Who was the sole survivor of Titanic?`

Het model produceert een antwoord zoals hieronder:

Dit is een zeer zelfverzekerd en grondig antwoord. Helaas is het onjuist. Zelfs met een minimale hoeveelheid onderzoek zou men ontdekken dat er meer dan één overlevende van de Titanic-ramp was. Voor een student die net begint met onderzoek naar dit onderwerp, kan dit antwoord overtuigend genoeg zijn om niet in twijfel te worden getrokken en als feit te worden behandeld. De gevolgen hiervan kunnen ertoe leiden dat het AI-systeem onbetrouwbaar is en de reputatie van onze startup negatief beïnvloedt.

Met elke iteratie van een gegeven LLM hebben we prestatieverbeteringen gezien rond het minimaliseren van hallucinaties. Zelfs met deze verbetering moeten wij als applicatiebouwers en gebruikers ons nog steeds bewust blijven van deze beperkingen.

### Schadelijke Inhoud

We hebben in de vorige sectie behandeld wanneer een LLM onjuiste of onzinnige reacties produceert. Een ander risico waarvan we ons bewust moeten zijn, is wanneer een model reageert met schadelijke inhoud.

Schadelijke inhoud kan worden gedefinieerd als:

- Instructies geven of aanmoedigen tot zelfbeschadiging of schade aan bepaalde groepen.
- Haatdragende of neerbuigende inhoud.
- Het plannen van enige vorm van aanval of gewelddadige handelingen begeleiden.
- Instructies geven over hoe je illegale inhoud kunt vinden of illegale handelingen kunt plegen.
- Seksueel expliciete inhoud weergeven.

Voor onze startup willen we ervoor zorgen dat we de juiste tools en strategieën hebben om te voorkomen dat dit soort inhoud door studenten wordt gezien.

### Gebrek aan Eerlijkheid

Eerlijkheid wordt gedefinieerd als “ervoor zorgen dat een AI-systeem vrij is van vooroordelen en discriminatie en dat ze iedereen eerlijk en gelijk behandelen.” In de wereld van Generatieve AI willen we ervoor zorgen dat uitsluitende wereldbeelden van gemarginaliseerde groepen niet worden versterkt door de output van het model.

Deze soorten outputs zijn niet alleen destructief voor het bouwen van positieve productervaringen voor onze gebruikers, maar ze veroorzaken ook verdere maatschappelijke schade. Als applicatiebouwers moeten we altijd een breed en divers gebruikersbestand in gedachten houden bij het bouwen van oplossingen met Generatieve AI.

## Hoe Generatieve AI Verantwoord Gebruiken

Nu we het belang van Verantwoordelijke Generatieve AI hebben geïdentificeerd, laten we kijken naar 4 stappen die we kunnen nemen om onze AI-oplossingen verantwoord te bouwen:

### Potentiële Schade Meten

In softwaretesten testen we de verwachte acties van een gebruiker op een applicatie. Evenzo is het testen van een diverse set prompts die gebruikers waarschijnlijk gaan gebruiken een goede manier om potentiële schade te meten.

Aangezien onze startup een onderwijsproduct bouwt, zou het goed zijn om een lijst met onderwijsgerelateerde prompts voor te bereiden. Dit zou kunnen zijn om een bepaald onderwerp te behandelen, historische feiten en prompts over het studentenleven.

### Potentiële Schade Beperken

Het is nu tijd om manieren te vinden waarop we de potentiële schade veroorzaakt door het model en zijn reacties kunnen voorkomen of beperken. We kunnen dit op 4 verschillende lagen bekijken:

- **Model**. Het juiste model kiezen voor het juiste gebruik. Grotere en complexere modellen zoals GPT-4 kunnen meer risico op schadelijke inhoud veroorzaken wanneer ze worden toegepast op kleinere en specifiekere gebruiksgevallen. Het gebruik van je trainingsgegevens om te fine-tunen vermindert ook het risico op schadelijke inhoud.

- **Veiligheidssysteem**. Een veiligheidssysteem is een set tools en configuraties op het platform dat het model bedient om schade te beperken. Een voorbeeld hiervan is het contentfilteringssysteem op de Azure OpenAI-service. Systemen moeten ook jailbreak-aanvallen en ongewenste activiteiten zoals verzoeken van bots detecteren.

- **Metaprompt**. Metaprompts en gronding zijn manieren waarop we het model kunnen sturen of beperken op basis van bepaald gedrag en informatie. Dit kan zijn door systeeminvoer te gebruiken om bepaalde limieten van het model te definiëren. Bovendien het bieden van outputs die relevanter zijn voor de scope of het domein van het systeem.

Het kan ook het gebruik van technieken zoals Retrieval Augmented Generation (RAG) zijn om het model alleen informatie te laten halen uit een selectie van vertrouwde bronnen. Er is later in deze cursus een les voor [het bouwen van zoektoepassingen](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Gebruikerservaring**. De laatste laag is waar de gebruiker direct interactie heeft met het model via de interface van onze applicatie op een bepaalde manier. Op deze manier kunnen we de UI/UX ontwerpen om de gebruiker te beperken in de soorten invoer die ze naar het model kunnen sturen, evenals de tekst of afbeeldingen die aan de gebruiker worden getoond. Bij het implementeren van de AI-toepassing moeten we ook transparant zijn over wat onze Generatieve AI-toepassing wel en niet kan doen.

We hebben een hele les gewijd aan [Ontwerpen van UX voor AI-toepassingen](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Model Evalueren**. Werken met LLMs kan uitdagend zijn omdat we niet altijd controle hebben over de gegevens waarop het model is getraind. Toch moeten we altijd de prestaties en outputs van het model evalueren. Het is nog steeds belangrijk om de nauwkeurigheid, gelijkenis, gronding en relevantie van de output van het model te meten. Dit helpt om transparantie en vertrouwen te bieden aan belanghebbenden en gebruikers.

### Een Verantwoordelijke Generatieve AI-oplossing Bedrijven

Het opbouwen van een operationele praktijk rond je AI-toepassingen is de laatste fase. Dit omvat samenwerking met andere delen van onze startup zoals Juridisch en Beveiliging om ervoor te zorgen dat we voldoen aan alle regelgevende beleidsregels. Voordat we lanceren, willen we ook plannen opstellen rond levering, het omgaan met incidenten en terugdraaien om eventuele schade aan onze gebruikers te voorkomen.

## Tools

Hoewel het werk van het ontwikkelen van Verantwoordelijke AI-oplossingen veel lijkt, is het werk de moeite waard. Naarmate het gebied van Generatieve AI groeit, zullen meer tools om ontwikkelaars te helpen verantwoordelijkheid efficiënt in hun workflows te integreren volwassen worden. Bijvoorbeeld, de [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) kan helpen schadelijke inhoud en afbeeldingen te detecteren via een API-verzoek.

## Kenniscontrole

Waar moet je op letten om verantwoord AI-gebruik te waarborgen?

1. Dat het antwoord correct is.
2. Schadelijk gebruik, dat AI niet voor criminele doeleinden wordt gebruikt.
3. Ervoor zorgen dat de AI vrij is van vooroordelen en discriminatie.

A: 2 en 3 zijn correct. Verantwoordelijke AI helpt je na te denken over hoe je schadelijke effecten en vooroordelen kunt beperken en meer.

## 🚀 Uitdaging

Lees over [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) en kijk wat je kunt toepassen voor jouw gebruik.

## Goed Gedaan, Ga Door met Leren

Na het voltooien van deze les, bekijk onze [Generatieve AI Leercollectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis over Generatieve AI verder te vergroten!

Ga naar Les 4 waar we gaan kijken naar [Prompt Engineering Fundamentals](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.