<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:18:11+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "sv"
}
-->
# Säkerhet för dina generativa AI-applikationer

## Introduktion

Denna lektion kommer att täcka:

- Säkerhet inom AI-systemens kontext.
- Vanliga risker och hot mot AI-system.
- Metoder och överväganden för att säkra AI-system.

## Inlärningsmål

Efter att ha slutfört denna lektion kommer du att ha en förståelse för:

- Hot och risker mot AI-system.
- Vanliga metoder och praxis för att säkra AI-system.
- Hur implementering av säkerhetstestning kan förhindra oväntade resultat och förlust av användarförtroende.

## Vad betyder säkerhet inom kontexten av generativ AI?

Eftersom artificiell intelligens (AI) och maskininlärning (ML) i allt högre grad formar våra liv är det avgörande att skydda inte bara kunddata utan även AI-systemen själva. AI/ML används alltmer för att stödja beslutsfattande processer med högt värde inom industrier där fel beslut kan få allvarliga konsekvenser.

Här är viktiga punkter att tänka på:

- **Påverkan av AI/ML**: AI/ML har betydande påverkan på vardagen och därför har det blivit nödvändigt att skydda dem.
- **Säkerhetsutmaningar**: Denna påverkan från AI/ML kräver rätt uppmärksamhet för att adressera behovet av att skydda AI-baserade produkter från sofistikerade attacker, vare sig från troll eller organiserade grupper.
- **Strategiska problem**: Teknikindustrin måste proaktivt adressera strategiska utmaningar för att säkerställa långsiktig kundsäkerhet och datasäkerhet.

Dessutom är maskininlärningsmodeller i stort sett oförmögna att skilja mellan skadlig input och godartad avvikande data. En betydande källa till träningsdata kommer från okurerade, omodererade, offentliga dataset som är öppna för bidrag från tredje part. Angripare behöver inte kompromettera dataset när de fritt kan bidra till dem. Med tiden blir lågkonfident skadlig data högkonfident betrodd data, om datastrukturen/formateringen förblir korrekt.

Det är därför det är kritiskt att säkerställa integriteten och skyddet av de datalager dina modeller använder för att fatta beslut med.

## Förstå hot och risker för AI

När det gäller AI och relaterade system framstår datagiftning som det mest betydande säkerhetshotet idag. Datagiftning är när någon avsiktligt ändrar informationen som används för att träna en AI, vilket får den att göra misstag. Detta beror på avsaknaden av standardiserade detektions- och mildringsmetoder, tillsammans med vårt beroende av otillförlitliga eller okurerade offentliga dataset för träning. För att bibehålla dataintegritet och förhindra en bristfällig träningsprocess är det avgörande att spåra ursprung och härkomst av din data. Annars gäller det gamla talesättet "skräp in, skräp ut", vilket leder till komprometterad modellprestanda.

Här är exempel på hur datagiftning kan påverka dina modeller:

1. **Etikettväxling**: I en binär klassificeringsuppgift växlar en motståndare avsiktligt etiketter för en liten del av träningsdata. Till exempel märks godartade prover som skadliga, vilket får modellen att lära sig felaktiga associationer.\
   **Exempel**: Ett skräppostfilter som felklassificerar legitima e-postmeddelanden som skräppost på grund av manipulerade etiketter.
2. **Funktionförgiftning**: En angripare modifierar subtilt funktioner i träningsdata för att införa bias eller vilseleda modellen.\
   **Exempel**: Lägga till irrelevanta nyckelord i produktbeskrivningar för att manipulera rekommendationssystem.
3. **Datainjektion**: Injicera skadlig data i träningsuppsättningen för att påverka modellens beteende.\
   **Exempel**: Introducera falska användarrecensioner för att snedvrida resultat av sentimentanalys.
4. **Bakdörrsattacker**: En motståndare sätter in ett dolt mönster (bakdörr) i träningsdata. Modellen lär sig känna igen detta mönster och beter sig skadligt när det utlöses.\
   **Exempel**: Ett ansiktsigenkänningssystem tränat med bilder med bakdörrar som felidentifierar en specifik person.

MITRE Corporation har skapat [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), en kunskapsbas av taktiker och tekniker som används av motståndare i verkliga attacker på AI-system.

> Det finns ett växande antal sårbarheter i AI-aktiverade system, eftersom införandet av AI ökar attackytan för befintliga system bortom de traditionella cyberattackerna. Vi utvecklade ATLAS för att öka medvetenheten om dessa unika och utvecklande sårbarheter, eftersom det globala samfundet i allt högre grad införlivar AI i olika system. ATLAS är modellerad efter MITRE ATT&CK®-ramverket och dess taktiker, tekniker och procedurer (TTPs) kompletterar de i ATT&CK.

Precis som MITRE ATT&CK®-ramverket, som används i stor utsträckning inom traditionell cybersäkerhet för att planera avancerade hotemuleringsscenarier, tillhandahåller ATLAS en lätt sökbar uppsättning TTPs som kan hjälpa till att bättre förstå och förbereda sig för att försvara sig mot framväxande attacker.

Dessutom har Open Web Application Security Project (OWASP) skapat en "[Topp 10-lista](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" över de mest kritiska sårbarheterna som finns i applikationer som använder LLMs. Listan belyser riskerna med hot som den tidigare nämnda datagiftningen tillsammans med andra som:

- **Prompt Injection**: en teknik där angripare manipulerar en stor språkmodell (LLM) genom noggrant utformade inmatningar, vilket får den att bete sig utanför sitt avsedda beteende.
- **Leveranskedjesårbarheter**: Komponenterna och programvaran som utgör applikationerna som används av en LLM, såsom Python-moduler eller externa dataset, kan själva komprometteras vilket leder till oväntade resultat, införda biaser och till och med sårbarheter i den underliggande infrastrukturen.
- **Överdriven tillit**: LLMs är felbara och har varit benägna att hallucinera, vilket ger felaktiga eller osäkra resultat. I flera dokumenterade omständigheter har människor tagit resultaten för givna vilket lett till oavsiktliga negativa konsekvenser i verkligheten.

Microsoft Cloud Advocate Rod Trent har skrivit en gratis e-bok, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), som går djupt in i dessa och andra framväxande AI-hot och ger omfattande vägledning om hur man bäst hanterar dessa scenarier.

## Säkerhetstestning för AI-system och LLMs

Artificiell intelligens (AI) förändrar olika domäner och industrier, och erbjuder nya möjligheter och fördelar för samhället. Men AI medför också betydande utmaningar och risker, såsom dataintegritet, bias, brist på förklarbarhet och potentiell missbruk. Därför är det avgörande att säkerställa att AI-system är säkra och ansvarstagande, vilket innebär att de följer etiska och juridiska standarder och kan litas på av användare och intressenter.

Säkerhetstestning är processen att utvärdera säkerheten hos ett AI-system eller LLM, genom att identifiera och utnyttja deras sårbarheter. Detta kan utföras av utvecklare, användare eller tredje parts revisorer, beroende på syftet och omfattningen av testningen. Några av de vanligaste säkerhetstestningsmetoderna för AI-system och LLMs är:

- **Datasanering**: Detta är processen att ta bort eller anonymisera känslig eller privat information från träningsdata eller inmatningen av ett AI-system eller LLM. Datasanering kan hjälpa till att förhindra dataläckage och skadlig manipulation genom att minska exponeringen av konfidentiell eller personlig data.
- **Adversarial testing**: Detta är processen att generera och tillämpa motståndarexempel på inmatningen eller utmatningen av ett AI-system eller LLM för att utvärdera dess robusthet och motståndskraft mot motståndareattacker. Adversarial testing kan hjälpa till att identifiera och mildra sårbarheterna och svagheterna hos ett AI-system eller LLM som kan utnyttjas av angripare.
- **Modellverifiering**: Detta är processen att verifiera korrektheten och fullständigheten av modellparametrarna eller arkitekturen för ett AI-system eller LLM. Modellverifiering kan hjälpa till att upptäcka och förhindra modellstöld genom att säkerställa att modellen är skyddad och autentiserad.
- **Utmatningsvalidering**: Detta är processen att validera kvaliteten och tillförlitligheten hos utmatningen av ett AI-system eller LLM. Utmatningsvalidering kan hjälpa till att upptäcka och korrigera skadlig manipulation genom att säkerställa att utmatningen är konsekvent och korrekt.

OpenAI, en ledare inom AI-system, har satt upp en serie _säkerhetsutvärderingar_ som en del av deras red teaming-nätverksinitiativ, som syftar till att testa utmatningen av AI-system i hopp om att bidra till AI-säkerhet.

> Utvärderingar kan sträcka sig från enkla Q&A-tester till mer komplexa simuleringar. Som konkreta exempel är här exempelutvärderingar utvecklade av OpenAI för att utvärdera AI-beteenden ur flera vinklar:

#### Övertalning

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Hur väl kan ett AI-system lura ett annat AI-system att säga ett hemligt ord?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Hur väl kan ett AI-system övertyga ett annat AI-system att donera pengar?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Hur väl kan ett AI-system påverka ett annat AI-systems stöd för ett politiskt förslag?

#### Steganografi (dolda meddelanden)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Hur väl kan ett AI-system skicka hemliga meddelanden utan att bli upptäckt av ett annat AI-system?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Hur väl kan ett AI-system komprimera och dekomprimera meddelanden, för att möjliggöra dolda meddelanden?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Hur väl kan ett AI-system samordna med ett annat AI-system, utan direkt kommunikation?

### AI-säkerhet

Det är avgörande att vi strävar efter att skydda AI-system från skadliga attacker, missbruk eller oavsiktliga konsekvenser. Detta inkluderar att vidta åtgärder för att säkerställa säkerheten, tillförlitligheten och trovärdigheten hos AI-system, såsom:

- Säkring av data och algoritmer som används för att träna och köra AI-modeller
- Förhindra obehörig åtkomst, manipulation eller sabotage av AI-system
- Upptäcka och mildra bias, diskriminering eller etiska frågor i AI-system
- Säkerställa ansvarsskyldighet, transparens och förklarbarhet i AI-beslut och handlingar
- Anpassa AI-systemens mål och värderingar med människors och samhällets

AI-säkerhet är viktigt för att säkerställa integriteten, tillgängligheten och konfidentialiteten hos AI-system och data. Några av utmaningarna och möjligheterna med AI-säkerhet är:

- Möjlighet: Att införliva AI i cybersäkerhetsstrategier eftersom det kan spela en avgörande roll i att identifiera hot och förbättra svarstider. AI kan hjälpa till att automatisera och förstärka upptäckten och mildringen av cyberattacker, såsom phishing, malware eller ransomware.
- Utmaning: AI kan också användas av motståndare för att starta sofistikerade attacker, såsom att generera falskt eller vilseledande innehåll, imitera användare eller utnyttja sårbarheter i AI-system. Därför har AI-utvecklare ett unikt ansvar att designa system som är robusta och motståndskraftiga mot missbruk.

### Dataskydd

LLMs kan utgöra risker för integriteten och säkerheten för den data de använder. Till exempel kan LLMs potentiellt memorera och läcka känslig information från deras träningsdata, såsom personnamn, adresser, lösenord eller kreditkortsnummer. De kan också manipuleras eller attackeras av skadliga aktörer som vill utnyttja deras sårbarheter eller biaser. Därför är det viktigt att vara medveten om dessa risker och vidta lämpliga åtgärder för att skydda den data som används med LLMs. Det finns flera steg du kan ta för att skydda den data som används med LLMs. Dessa steg inkluderar:

- **Begränsa mängden och typen av data som de delar med LLMs**: Dela endast den data som är nödvändig och relevant för de avsedda syftena, och undvik att dela någon data som är känslig, konfidentiell eller personlig. Användare bör också anonymisera eller kryptera den data de delar med LLMs, såsom genom att ta bort eller maskera någon identifierande information, eller använda säkra kommunikationskanaler.
- **Verifiera den data som LLMs genererar**: Kontrollera alltid noggrannheten och kvaliteten på den utmatning som genereras av LLMs för att säkerställa att de inte innehåller någon oönskad eller olämplig information.
- **Rapportera och varna om några dataintrång eller incidenter**: Var vaksam på några misstänkta eller onormala aktiviteter eller beteenden från LLMs, såsom att generera texter som är irrelevanta, felaktiga, stötande eller skadliga. Detta kan vara en indikation på ett dataintrång eller säkerhetsincident.

Datasäkerhet, styrning och efterlevnad är avgörande för alla organisationer som vill utnyttja kraften i data och AI i en multi-molnmiljö. Att säkra och styra all din data är en komplex och mångfacetterad uppgift. Du behöver säkra och styra olika typer av data (strukturerad, ostrukturerad och data genererad av AI) på olika platser över flera moln, och du behöver ta hänsyn till befintliga och framtida dataskydd, styrning och AI-regleringar. För att skydda din data behöver du anta några bästa praxis och försiktighetsåtgärder, såsom:

- Använd molntjänster eller plattformar som erbjuder dataskydd och sekretessfunktioner.
- Använd verktyg för datakvalitet och validering för att kontrollera din data för fel, inkonsekvenser eller avvikelser.
- Använd ramverk för datastyrning och etik för att säkerställa att din data används på ett ansvarsfullt och transparent sätt.

### Emulera verkliga hot - AI red teaming

Att emulera verkliga hot anses nu vara en standardpraxis vid byggandet av motståndskraftiga AI-system genom att använda liknande verktyg, taktiker och procedurer för att identifiera riskerna för system och testa försvararnas respons.

> Praktiken av AI red teaming har utvecklats till att ta på sig en mer utökad betydelse: det täcker inte bara sökandet efter säkerhetssårbarheter, utan inkluderar också sökandet efter andra systemfel, såsom generering av potentiellt skadligt innehåll. AI-system kommer med nya risker, och red teaming är kärnan i att förstå dessa nya risker, såsom prompt injection och produktion av ogrundat innehåll. - [Microsoft AI Red Team bygger framtiden för säkrare AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

Nedan följer viktiga insikter som har format Microsofts AI Red Team-program.

1. **Omfattande omfattning av AI Red Teaming:**
   AI red teaming omfattar nu både säkerhets- och Ansvarsfull AI (RAI) resultat. Traditionellt fokuserade red teaming på säkerhetsaspekter och behandlade modellen som en vektor (t.ex. stöld av den underliggande modellen). Men AI-system introducerar nya säkerhetssårbarheter (t.ex. prompt injection, förgiftning), vilket kräver särskild uppmär

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller oriktigheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi är inte ansvariga för eventuella missförstånd eller misstolkningar som uppstår vid användning av denna översättning.