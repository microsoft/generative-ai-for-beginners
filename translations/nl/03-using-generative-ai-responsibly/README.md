<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:26:58+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "nl"
}
-->
# Verantwoord Gebruik van Generatieve AI

> _Klik op de afbeelding hierboven om de video van deze les te bekijken_

Het is makkelijk om gefascineerd te raken door AI en generatieve AI in het bijzonder, maar je moet nadenken over hoe je het op een verantwoorde manier kunt gebruiken. Je moet nadenken over zaken als hoe je ervoor zorgt dat de output eerlijk en onschadelijk is en meer. Dit hoofdstuk heeft als doel om je de genoemde context te bieden, wat je moet overwegen en hoe je actieve stappen kunt nemen om je AI-gebruik te verbeteren.

## Inleiding

Deze les behandelt:

- Waarom je Verantwoorde AI zou moeten prioriteren bij het bouwen van Generatieve AI-toepassingen.
- Kernprincipes van Verantwoorde AI en hoe deze zich verhouden tot Generatieve AI.
- Hoe je deze principes van Verantwoorde AI in de praktijk kunt brengen via strategie en hulpmiddelen.

## Leerdoelen

Na het voltooien van deze les weet je:

- Het belang van Verantwoorde AI bij het bouwen van Generatieve AI-toepassingen.
- Wanneer je moet nadenken over en de kernprincipes van Verantwoorde AI moet toepassen bij het bouwen van Generatieve AI-toepassingen.
- Welke hulpmiddelen en strategieën beschikbaar zijn om het concept van Verantwoorde AI in de praktijk te brengen.

## Principes van Verantwoorde AI

De opwinding over Generatieve AI is nog nooit zo groot geweest. Deze opwinding heeft veel nieuwe ontwikkelaars, aandacht en financiering naar dit gebied gebracht. Hoewel dit zeer positief is voor iedereen die producten en bedrijven wil bouwen met Generatieve AI, is het ook belangrijk dat we verantwoordelijk te werk gaan.

Gedurende deze cursus richten we ons op het bouwen van onze startup en ons AI-onderwijsproduct. We zullen de principes van Verantwoorde AI gebruiken: Eerlijkheid, Inclusiviteit, Betrouwbaarheid/Veiligheid, Beveiliging & Privacy, Transparantie en Verantwoording. Met deze principes zullen we onderzoeken hoe ze zich verhouden tot ons gebruik van Generatieve AI in onze producten.

## Waarom Zou Je Verantwoorde AI Moeten Prioriteren

Bij het bouwen van een product leidt een mensgerichte benadering, waarbij je het beste belang van je gebruiker in gedachten houdt, tot de beste resultaten.

De uniekheid van Generatieve AI is zijn kracht om nuttige antwoorden, informatie, begeleiding en inhoud voor gebruikers te creëren. Dit kan zonder veel handmatige stappen, wat tot zeer indrukwekkende resultaten kan leiden. Zonder goede planning en strategieën kan het helaas ook leiden tot schadelijke resultaten voor je gebruikers, je product en de samenleving als geheel.

Laten we kijken naar enkele (maar niet alle) van deze potentieel schadelijke resultaten:

### Hallucinaties

Hallucinaties zijn een term die wordt gebruikt om te beschrijven wanneer een LLM inhoud produceert die ofwel volkomen onzinnig is of iets waarvan we weten dat het feitelijk onjuist is op basis van andere informatiebronnen.

Laten we bijvoorbeeld aannemen dat we een functie bouwen voor onze startup waarmee studenten historische vragen kunnen stellen aan een model. Een student stelt de vraag `Who was the sole survivor of Titanic?`

Het model geeft een antwoord zoals hieronder:

Dit is een zeer zelfverzekerd en grondig antwoord. Helaas is het onjuist. Zelfs met een minimale hoeveelheid onderzoek zou men ontdekken dat er meer dan één overlevende was van de Titanic-ramp. Voor een student die net begint met onderzoek naar dit onderwerp, kan dit antwoord overtuigend genoeg zijn om niet in twijfel te worden getrokken en als feit te worden behandeld. De gevolgen hiervan kunnen ertoe leiden dat het AI-systeem onbetrouwbaar is en een negatieve invloed heeft op de reputatie van onze startup.

Met elke iteratie van een gegeven LLM hebben we prestatieverbeteringen gezien rond het minimaliseren van hallucinaties. Zelfs met deze verbetering moeten wij als applicatiebouwers en gebruikers ons bewust blijven van deze beperkingen.

### Schadelijke Inhoud

We hebben in het eerdere gedeelte behandeld wanneer een LLM onjuiste of onzinnige reacties produceert. Een ander risico waar we ons bewust van moeten zijn, is wanneer een model reageert met schadelijke inhoud.

Schadelijke inhoud kan worden gedefinieerd als:

- Instructies geven of aanmoedigen tot zelfbeschadiging of schade aan bepaalde groepen.
- Haatdragende of denigrerende inhoud.
- Begeleiding bij het plannen van een aanval of gewelddadige handelingen.
- Instructies geven over hoe illegale inhoud te vinden of illegale handelingen te plegen.
- Seksueel expliciete inhoud weergeven.

Voor onze startup willen we ervoor zorgen dat we de juiste hulpmiddelen en strategieën hebben om te voorkomen dat dit soort inhoud door studenten wordt gezien.

### Gebrek aan Eerlijkheid

Eerlijkheid wordt gedefinieerd als "ervoor zorgen dat een AI-systeem vrij is van vooroordelen en discriminatie en dat ze iedereen eerlijk en gelijk behandelen." In de wereld van Generatieve AI willen we ervoor zorgen dat uitsluitende wereldbeelden van gemarginaliseerde groepen niet worden versterkt door de output van het model.

Deze soorten outputs zijn niet alleen destructief voor het bouwen van positieve productervaringen voor onze gebruikers, maar ze veroorzaken ook verdere maatschappelijke schade. Als applicatiebouwers moeten we altijd een breed en divers gebruikersbestand in gedachten houden bij het bouwen van oplossingen met Generatieve AI.

## Hoe Generatieve AI Verantwoord te Gebruiken

Nu we het belang van Verantwoorde Generatieve AI hebben geïdentificeerd, laten we kijken naar 4 stappen die we kunnen nemen om onze AI-oplossingen verantwoord te bouwen:

### Potentiële Schade Meten

Bij softwaretesten testen we de verwachte acties van een gebruiker op een applicatie. Op dezelfde manier is het testen van een diverse set prompts die gebruikers waarschijnlijk gaan gebruiken een goede manier om potentiële schade te meten.

Aangezien onze startup een onderwijsproduct bouwt, zou het goed zijn om een lijst met onderwijsgerelateerde prompts voor te bereiden. Dit kan zijn om een bepaald onderwerp te behandelen, historische feiten en prompts over het studentenleven.

### Potentiële Schade Beperken

Het is nu tijd om manieren te vinden waarop we de potentiële schade veroorzaakt door het model en zijn reacties kunnen voorkomen of beperken. We kunnen dit bekijken in 4 verschillende lagen:

- **Model**. Het juiste model kiezen voor de juiste use case. Grotere en complexere modellen zoals GPT-4 kunnen meer risico op schadelijke inhoud veroorzaken wanneer ze worden toegepast op kleinere en specifiekere use cases. Het gebruik van je trainingsgegevens om het model af te stemmen, vermindert ook het risico op schadelijke inhoud.

- **Veiligheidssysteem**. Een veiligheidssysteem is een set van hulpmiddelen en configuraties op het platform dat het model bedient en helpt schade te beperken. Een voorbeeld hiervan is het inhoudfilteringssysteem op de Azure OpenAI-service. Systemen moeten ook jailbreak-aanvallen en ongewenste activiteiten zoals verzoeken van bots detecteren.

- **Metaprompt**. Metaprompts en gronding zijn manieren waarop we het model kunnen sturen of beperken op basis van bepaald gedrag en informatie. Dit kan zijn door systeeminvoer te gebruiken om bepaalde grenzen van het model te definiëren. Bovendien outputs te bieden die relevanter zijn voor de reikwijdte of het domein van het systeem.

Het kan ook zijn door technieken te gebruiken zoals Retrieval Augmented Generation (RAG) om het model alleen informatie te laten halen uit een selectie van vertrouwde bronnen. Er is later in deze cursus een les voor [het bouwen van zoektoepassingen](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Gebruikerservaring**. De laatste laag is waar de gebruiker op een of andere manier direct via de interface van onze applicatie met het model interageert. Op deze manier kunnen we de UI/UX zo ontwerpen dat we de gebruiker beperken in de soorten invoer die ze naar het model kunnen sturen, evenals tekst of afbeeldingen die aan de gebruiker worden getoond. Bij het implementeren van de AI-toepassing moeten we ook transparant zijn over wat onze Generatieve AI-toepassing wel en niet kan doen.

We hebben een hele les gewijd aan [Het Ontwerpen van UX voor AI-toepassingen](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Model evalueren**. Werken met LLM's kan een uitdaging zijn omdat we niet altijd controle hebben over de gegevens waarop het model is getraind. Desondanks moeten we altijd de prestaties en outputs van het model evalueren. Het is nog steeds belangrijk om de nauwkeurigheid, gelijkenis, grondigheid en relevantie van de output van het model te meten. Dit helpt transparantie en vertrouwen te bieden aan belanghebbenden en gebruikers.

### Een Verantwoorde Generatieve AI-oplossing Bedrijven

Het opbouwen van een operationele praktijk rond je AI-toepassingen is de laatste fase. Dit omvat samenwerken met andere delen van onze startup zoals Juridische Zaken en Beveiliging om ervoor te zorgen dat we voldoen aan alle regelgevende beleidsmaatregelen. Voordat we lanceren, willen we ook plannen opstellen rond levering, het omgaan met incidenten en terugrollen om schade aan onze gebruikers te voorkomen.

## Hulpmiddelen

Hoewel het ontwikkelen van Verantwoorde AI-oplossingen veel werk lijkt, is het werk dat de moeite waard is. Naarmate het gebied van Generatieve AI groeit, zullen er meer hulpmiddelen beschikbaar komen om ontwikkelaars efficiënt verantwoordelijkheid in hun workflows te laten integreren. Bijvoorbeeld, de [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) kan helpen schadelijke inhoud en afbeeldingen te detecteren via een API-verzoek.

## Kennischeck

Waar moet je op letten om verantwoord AI-gebruik te garanderen?

1. Dat het antwoord correct is.
1. Schadelijk gebruik, dat AI niet wordt gebruikt voor criminele doeleinden.
1. Ervoor zorgen dat de AI vrij is van vooroordelen en discriminatie.

A: 2 en 3 zijn correct. Verantwoorde AI helpt je na te denken over hoe schadelijke effecten en vooroordelen te beperken en meer.

## 🚀 Uitdaging

Lees over [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) en kijk wat je kunt toepassen voor jouw gebruik.

## Goed Gedaan, Ga Door met Leren

Na het voltooien van deze les, bekijk onze [Generatieve AI Leerverzameling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis over Generatieve AI verder te verdiepen!

Ga naar Les 4 waar we [Prompt Engineering Fundamentals](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) zullen bekijken!

**Disclaimer**:  
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons inzetten voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of misinterpretaties die voortvloeien uit het gebruik van deze vertaling.