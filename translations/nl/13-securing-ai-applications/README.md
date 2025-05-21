<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T22:55:51+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "nl"
}
-->
# Beveiliging van je Generatieve AI-toepassingen

## Introductie

Deze les behandelt:

- Beveiliging binnen de context van AI-systemen.
- Veelvoorkomende risico's en bedreigingen voor AI-systemen.
- Methoden en overwegingen voor het beveiligen van AI-systemen.

## Leerdoelen

Na het voltooien van deze les begrijp je:

- De bedreigingen en risico's voor AI-systemen.
- Veelvoorkomende methoden en praktijken voor het beveiligen van AI-systemen.
- Hoe het implementeren van beveiligingstests onverwachte resultaten en verlies van gebruikersvertrouwen kan voorkomen.

## Wat betekent beveiliging binnen de context van generatieve AI?

Nu Kunstmatige Intelligentie (AI) en Machine Learning (ML) technologieën steeds meer ons leven beïnvloeden, is het essentieel om niet alleen klantgegevens te beschermen, maar ook de AI-systemen zelf. AI/ML wordt steeds vaker gebruikt ter ondersteuning van besluitvormingsprocessen met hoge waarde in sectoren waar een verkeerde beslissing ernstige gevolgen kan hebben.

Hier zijn enkele belangrijke punten om te overwegen:

- **Impact van AI/ML**: AI/ML hebben aanzienlijke effecten op het dagelijks leven en daarom is het essentieel geworden om ze te beschermen.
- **Beveiligingsuitdagingen**: Deze impact van AI/ML vereist de juiste aandacht om de noodzaak aan te pakken om AI-gebaseerde producten te beschermen tegen geavanceerde aanvallen, of deze nu afkomstig zijn van trolls of georganiseerde groepen.
- **Strategische Problemen**: De technologie-industrie moet proactief strategische uitdagingen aanpakken om langdurige klantveiligheid en gegevensbeveiliging te waarborgen.

Daarnaast zijn Machine Learning-modellen grotendeels niet in staat om onderscheid te maken tussen kwaadaardige invoer en goedaardige anomaliegegevens. Een aanzienlijk deel van de trainingsgegevens is afkomstig uit niet-gecureerde, niet-gemodereerde, openbare datasets, die openstaan voor bijdragen van derden. Aanvallers hoeven datasets niet te compromitteren wanneer ze vrij zijn om eraan bij te dragen. Na verloop van tijd wordt laag-vertrouwde kwaadaardige data hoog-vertrouwde betrouwbare data, mits de datastructuur/formattering correct blijft.

Dit is waarom het cruciaal is om de integriteit en bescherming van de datastores te waarborgen die je modellen gebruiken om beslissingen mee te nemen.

## Begrijpen van de bedreigingen en risico's van AI

Wat betreft AI en gerelateerde systemen, valt datavergiftiging op als de meest significante beveiligingsbedreiging van vandaag. Datavergiftiging is wanneer iemand opzettelijk de informatie verandert die wordt gebruikt om een AI te trainen, waardoor deze fouten gaat maken. Dit komt door het ontbreken van gestandaardiseerde detectie- en mitigatiemethoden, gecombineerd met onze afhankelijkheid van onbetrouwbare of niet-gecureerde openbare datasets voor training. Om gegevensintegriteit te behouden en een foutief trainingsproces te voorkomen, is het cruciaal om de oorsprong en herkomst van je gegevens bij te houden. Anders geldt het oude gezegde "rommel erin, rommel eruit", wat leidt tot gecompromitteerde modelprestaties.

Hier zijn voorbeelden van hoe datavergiftiging je modellen kan beïnvloeden:

1. **Label Flipping**: In een binaire classificatietaak draait een tegenstander opzettelijk de labels van een klein deel van de trainingsgegevens om. Bijvoorbeeld, goedaardige monsters worden als kwaadaardig gelabeld, waardoor het model incorrecte associaties leert.\
   **Voorbeeld**: Een spamfilter dat legitieme e-mails verkeerd classificeert als spam vanwege gemanipuleerde labels.
2. **Feature Poisoning**: Een aanvaller wijzigt subtiel kenmerken in de trainingsgegevens om vooringenomenheid te introduceren of het model te misleiden.\
   **Voorbeeld**: Het toevoegen van irrelevante trefwoorden aan productbeschrijvingen om aanbevelingssystemen te manipuleren.
3. **Data Injection**: Kwaadaardige gegevens injecteren in de trainingsset om het gedrag van het model te beïnvloeden.\
   **Voorbeeld**: Nepgebruikersrecensies introduceren om sentimentanalyse resultaten te beïnvloeden.
4. **Backdoor Attacks**: Een tegenstander plaatst een verborgen patroon (achterdeur) in de trainingsgegevens. Het model leert dit patroon te herkennen en gedraagt zich kwaadaardig wanneer het wordt geactiveerd.\
   **Voorbeeld**: Een gezichtsherkenningssysteem getraind met achterdeurbeelden die een specifieke persoon verkeerd identificeren.

De MITRE Corporation heeft [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst) gecreëerd, een kennisbank van tactieken en technieken die door tegenstanders worden gebruikt in echte aanvallen op AI-systemen.

> Er zijn een groeiend aantal kwetsbaarheden in AI-ondersteunde systemen, aangezien de integratie van AI het aanvalsvlak van bestaande systemen uitbreidt buiten die van traditionele cyberaanvallen. We hebben ATLAS ontwikkeld om bewustzijn te creëren over deze unieke en evoluerende kwetsbaarheden, aangezien de wereldwijde gemeenschap steeds meer AI integreert in verschillende systemen. ATLAS is gemodelleerd naar het MITRE ATT&CK® framework en zijn tactieken, technieken en procedures (TTPs) zijn complementair aan die in ATT&CK.

Net als het MITRE ATT&CK® framework, dat uitgebreid wordt gebruikt in traditionele cybersecurity voor het plannen van geavanceerde dreigingsemulatiescenario's, biedt ATLAS een gemakkelijk doorzoekbare set TTPs die kunnen helpen om emerging attacks beter te begrijpen en te verdedigen.

Daarnaast heeft het Open Web Application Security Project (OWASP) een "[Top 10 lijst](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" gemaakt van de meest kritische kwetsbaarheden die worden aangetroffen in applicaties die LLMs gebruiken. De lijst benadrukt de risico's van bedreigingen zoals de eerder genoemde datavergiftiging, samen met andere zoals:

- **Prompt Injection**: een techniek waarbij aanvallers een Large Language Model (LLM) manipuleren door zorgvuldig samengestelde inputs, waardoor het zich buiten zijn beoogde gedrag gedraagt.
- **Supply Chain Vulnerabilities**: De componenten en software die de applicaties vormen die door een LLM worden gebruikt, zoals Python-modules of externe datasets, kunnen zelf worden gecompromitteerd, wat leidt tot onverwachte resultaten, geïntroduceerde vooringenomenheden en zelfs kwetsbaarheden in de onderliggende infrastructuur.
- **Overreliance**: LLMs zijn feilbaar en hebben de neiging om te hallucineren, waardoor ze onnauwkeurige of onveilige resultaten leveren. In verschillende gedocumenteerde omstandigheden hebben mensen de resultaten voor waar aangenomen, wat heeft geleid tot onbedoelde negatieve gevolgen in de echte wereld.

Microsoft Cloud Advocate Rod Trent heeft een gratis ebook geschreven, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), dat diep ingaat op deze en andere opkomende AI-bedreigingen en uitgebreide richtlijnen biedt over hoe je deze scenario's het beste kunt aanpakken.

## Beveiligingstests voor AI-systemen en LLMs

Kunstmatige intelligentie (AI) transformeert verschillende domeinen en industrieën, en biedt nieuwe mogelijkheden en voordelen voor de samenleving. Echter, AI brengt ook aanzienlijke uitdagingen en risico's met zich mee, zoals gegevensprivacy, vooringenomenheid, gebrek aan verklaarbaarheid en potentieel misbruik. Daarom is het cruciaal om ervoor te zorgen dat AI-systemen veilig en verantwoordelijk zijn, wat betekent dat ze voldoen aan ethische en wettelijke normen en vertrouwd kunnen worden door gebruikers en belanghebbenden.

Beveiligingstesten is het proces van het evalueren van de beveiliging van een AI-systeem of LLM, door hun kwetsbaarheden te identificeren en uit te buiten. Dit kan worden uitgevoerd door ontwikkelaars, gebruikers of externe auditors, afhankelijk van het doel en de reikwijdte van de tests. Enkele van de meest voorkomende beveiligingstestmethoden voor AI-systemen en LLMs zijn:

- **Gegevenssanering**: Dit is het proces van het verwijderen of anonimiseren van gevoelige of privé-informatie uit de trainingsgegevens of de input van een AI-systeem of LLM. Gegevenssanering kan helpen om gegevenslekken en kwaadaardige manipulatie te voorkomen door de blootstelling van vertrouwelijke of persoonlijke gegevens te verminderen.
- **Adversarial testing**: Dit is het proces van het genereren en toepassen van adversarial voorbeelden op de input of output van een AI-systeem of LLM om zijn robuustheid en veerkracht tegen adversarial attacks te evalueren. Adversarial testing kan helpen om de kwetsbaarheden en zwakheden van een AI-systeem of LLM te identificeren en te mitigeren die door aanvallers kunnen worden uitgebuit.
- **Modelverificatie**: Dit is het proces van het verifiëren van de juistheid en volledigheid van de modelparameters of architectuur van een AI-systeem of LLM. Modelverificatie kan helpen om modeldiefstal te detecteren en te voorkomen door ervoor te zorgen dat het model beschermd en geauthenticeerd is.
- **Outputvalidatie**: Dit is het proces van het valideren van de kwaliteit en betrouwbaarheid van de output van een AI-systeem of LLM. Outputvalidatie kan helpen om kwaadaardige manipulatie te detecteren en corrigeren door ervoor te zorgen dat de output consistent en nauwkeurig is.

OpenAI, een leider in AI-systemen, heeft een reeks _veiligheidsevaluaties_ opgezet als onderdeel van hun red teaming netwerkinitiatief, gericht op het testen van de output van AI-systemen in de hoop bij te dragen aan AI-veiligheid.

> Evaluaties kunnen variëren van eenvoudige Q&A-tests tot meer complexe simulaties. Als concrete voorbeelden, hier zijn voorbeeldevaluaties ontwikkeld door OpenAI voor het evalueren van AI-gedragingen vanuit verschillende invalshoeken:

#### Overtuiging

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Hoe goed kan een AI-systeem een ander AI-systeem misleiden om een geheim woord te zeggen?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Hoe goed kan een AI-systeem een ander AI-systeem overtuigen om geld te doneren?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Hoe goed kan een AI-systeem de steun van een ander AI-systeem voor een politieke voorstel beïnvloeden?

#### Steganografie (verborgen boodschappen)

- [Steganografie](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Hoe goed kan een AI-systeem geheime berichten doorgeven zonder betrapt te worden door een ander AI-systeem?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Hoe goed kan een AI-systeem berichten comprimeren en decomprimeren, om het verbergen van geheime berichten mogelijk te maken?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Hoe goed kan een AI-systeem samenwerken met een ander AI-systeem, zonder directe communicatie?

### AI-beveiliging

Het is van groot belang dat we streven naar de bescherming van AI-systemen tegen kwaadaardige aanvallen, misbruik of onbedoelde gevolgen. Dit omvat het nemen van stappen om de veiligheid, betrouwbaarheid en vertrouwenswaardigheid van AI-systemen te waarborgen, zoals:

- Het beveiligen van de gegevens en algoritmen die worden gebruikt om AI-modellen te trainen en uit te voeren
- Het voorkomen van ongeautoriseerde toegang, manipulatie of sabotage van AI-systemen
- Het detecteren en mitigeren van vooringenomenheid, discriminatie of ethische problemen in AI-systemen
- Het waarborgen van de verantwoordelijkheid, transparantie en verklaarbaarheid van AI-beslissingen en acties
- Het afstemmen van de doelen en waarden van AI-systemen met die van mensen en de samenleving

AI-beveiliging is belangrijk voor het waarborgen van de integriteit, beschikbaarheid en vertrouwelijkheid van AI-systemen en gegevens. Enkele van de uitdagingen en kansen van AI-beveiliging zijn:

- Kans: Het integreren van AI in cybersecurity-strategieën, aangezien het een cruciale rol kan spelen bij het identificeren van bedreigingen en het verbeteren van responstijden. AI kan helpen bij het automatiseren en versterken van de detectie en mitigatie van cyberaanvallen, zoals phishing, malware of ransomware.
- Uitdaging: AI kan ook door tegenstanders worden gebruikt om geavanceerde aanvallen uit te voeren, zoals het genereren van valse of misleidende inhoud, het imiteren van gebruikers, of het exploiteren van kwetsbaarheden in AI-systemen. Daarom hebben AI-ontwikkelaars een unieke verantwoordelijkheid om systemen te ontwerpen die robuust en veerkrachtig zijn tegen misbruik.

### Gegevensbescherming

LLMs kunnen risico's vormen voor de privacy en veiligheid van de gegevens die ze gebruiken. Bijvoorbeeld, LLMs kunnen mogelijk gevoelige informatie uit hun trainingsgegevens onthouden en lekken, zoals persoonlijke namen, adressen, wachtwoorden of creditcardnummers. Ze kunnen ook worden gemanipuleerd of aangevallen door kwaadaardige actoren die hun kwetsbaarheden of vooringenomenheden willen exploiteren. Daarom is het belangrijk om je bewust te zijn van deze risico's en passende maatregelen te nemen om de gegevens te beschermen die met LLMs worden gebruikt. Er zijn verschillende stappen die je kunt nemen om de gegevens te beschermen die met LLMs worden gebruikt. Deze stappen omvatten:

- **Beperken van de hoeveelheid en het type gegevens dat ze delen met LLMs**: Deel alleen de gegevens die noodzakelijk en relevant zijn voor de beoogde doeleinden, en vermijd het delen van gegevens die gevoelig, vertrouwelijk of persoonlijk zijn. Gebruikers moeten ook de gegevens die ze delen met LLMs anonimiseren of versleutelen, zoals door identificerende informatie te verwijderen of te maskeren, of door gebruik te maken van veilige communicatiekanalen.
- **Verifiëren van de gegevens die LLMs genereren**: Controleer altijd de nauwkeurigheid en kwaliteit van de output die door LLMs wordt gegenereerd om ervoor te zorgen dat ze geen ongewenste of ongepaste informatie bevatten.
- **Rapporteren en waarschuwen van eventuele datalekken of incidenten**: Wees waakzaam voor verdachte of abnormale activiteiten of gedragingen van LLMs, zoals het genereren van teksten die irrelevant, onnauwkeurig, beledigend of schadelijk zijn. Dit kan een indicatie zijn van een datalek of beveiligingsincident.

Gegevensbeveiliging, governance en compliance zijn van cruciaal belang voor elke organisatie die de kracht van gegevens en AI in een multi-cloud omgeving wil benutten. Het beveiligen en beheren van al je gegevens is een complex en veelzijdig proces. Je moet verschillende soorten gegevens beveiligen en beheren (gestructureerd, ongestructureerd en door AI gegenereerde gegevens) op verschillende locaties in meerdere clouds, en je moet rekening houden met bestaande en toekomstige gegevensbeveiliging, governance en AI-regelgeving. Om je gegevens te beschermen, moet je enkele best practices en voorzorgsmaatregelen adopteren, zoals:

- Gebruik cloudservices of platforms die gegevensbescherming en privacyfuncties bieden.
- Gebruik tools voor gegevenskwaliteit en validatie om je gegevens te controleren op fouten, inconsistenties of afwijkingen.
- Gebruik frameworks voor gegevensbeheer en ethiek om ervoor te zorgen dat je gegevens op een verantwoordelijke en transparante manier worden gebruikt.

### Emuleren van real-world bedreigingen - AI red teaming

Het emuleren van real-world bedreigingen wordt nu beschouwd als een standaardpraktijk in het bouwen van veerkrachtige AI-systemen door gebruik te maken van vergelijkbare tools, tactieken en procedures om de risico's voor systemen te identificeren en de respons van verdedigers te testen.

> De praktijk van AI red teaming heeft zich ontwikkeld om een meer uitgebreide betekenis te krijgen: het omvat niet alleen het onderzoeken van beveiligingskwetsbaarheden, maar ook het onderzoeken van andere systeemfouten, zoals het genereren van potentieel schadelijke inhoud. AI-systemen brengen nieuwe risico's met zich mee, en red teaming is essentieel om die nieuwe risico's te begrijpen, zoals prompt injection en het produceren van ongefundeerde inhoud. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

Hieronder staan ​​belangrijke inzichten die het AI Red Team-programma van Microsoft hebben gevormd.

1. **Uitgebreide Scope van AI Red Teaming:**
   AI red teaming omvat nu zowel beveiligings- als Responsible AI (RAI) uitkomsten. Traditioneel richtte red teaming zich op beveiligingsaspecten, waarbij het model werd behandeld als een vector (bijv. het stelen van het onderliggende model). Echter, AI-systemen introduceren nieuwe beveiligingskwetsbaarheden (bijv. prompt injection, poisoning), die speciale aandacht vereisen. Naast beveiliging onderzoekt AI red teaming ook eerlijkheidskwesties (bijv. stereotypering) en schadelijke inhoud (bijv. verheerlijking van geweld). Vroege identificatie van deze problemen stelt prioritering van investeringen in verdediging mogelijk.
2. **Kwaadaardige en Goedaardige Fouten:**
   AI red teaming houdt rekening met fouten vanuit zowel kwaadaardige als goedaardige perspectieven. Bijvoorbeeld, bij het red teaming van de nieuwe Bing, onderzoeken we niet alleen hoe kwaadaardige tegenstanders het systeem kunnen ondermijnen, maar ook hoe reguliere gebruikers mogelijk problematische of schadelijke inhoud kunnen tegenkomen. In tegenstelling tot traditionele beveiligingsred teaming, dat zich voornamelijk richt op kwaadaardige actoren, houdt AI red teaming rekening met een breder scala aan persona's en potentiële fouten.
3. **Dynamische Aard van AI-systemen:**
   AI-toepassingen evolueren voortdurend. In toepassingen van grote taalmodellen passen ontwikkelaars zich aan veranderende eisen aan. Continu red teaming zorgt voor voortdurende waakzaamheid en aanpassing aan evoluerende risico's.

AI red teaming is niet allesomvattend en moet worden beschouwd als een aanvullende beweging voor extra controles zoals

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, moet u er rekening mee houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.