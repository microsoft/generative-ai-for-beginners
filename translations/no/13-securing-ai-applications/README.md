<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T22:52:41+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "no"
}
-->
# Sikre dine generative AI-applikasjoner

## Introduksjon

Denne leksjonen vil dekke:

- Sikkerhet innenfor konteksten av AI-systemer.
- Vanlige risikoer og trusler mot AI-systemer.
- Metoder og hensyn for å sikre AI-systemer.

## Læringsmål

Etter å ha fullført denne leksjonen, vil du ha en forståelse av:

- Truslene og risikoene mot AI-systemer.
- Vanlige metoder og praksiser for å sikre AI-systemer.
- Hvordan implementering av sikkerhetstesting kan forhindre uventede resultater og svekkelse av brukertillit.

## Hva betyr sikkerhet innen konteksten av generativ AI?

Etter hvert som kunstig intelligens (AI) og maskinlæring (ML) teknologier i økende grad former våre liv, er det viktig å beskytte ikke bare kundedata, men også selve AI-systemene. AI/ML brukes stadig mer i støtte av beslutningsprosesser av høy verdi i bransjer der feil avgjørelser kan føre til alvorlige konsekvenser.

Her er viktige punkter å vurdere:

- **Innvirkning av AI/ML**: AI/ML har betydelig innvirkning på dagliglivet, og derfor har det blitt essensielt å beskytte dem.
- **Sikkerhetsutfordringer**: Denne innvirkningen som AI/ML har, trenger riktig oppmerksomhet for å adressere behovet for å beskytte AI-baserte produkter mot sofistikerte angrep, enten av troll eller organiserte grupper.
- **Strategiske problemer**: Teknologibransjen må proaktivt adressere strategiske utfordringer for å sikre langsiktig kundesikkerhet og datasikkerhet.

I tillegg er maskinlæringsmodeller stort sett ute av stand til å skille mellom ondsinnet input og godartet avvikende data. En betydelig kilde til treningsdata er hentet fra ukurerte, umodererte, offentlige datasett, som er åpne for bidrag fra tredjeparter. Angripere trenger ikke å kompromittere datasett når de fritt kan bidra til dem. Over tid blir data med lav tillit til data med høy tillit, hvis datastrukturen/formateringen forblir korrekt.

Derfor er det kritisk å sikre integriteten og beskyttelsen av datalagringene som modellene dine bruker for å ta beslutninger.

## Forstå truslene og risikoene ved AI

Når det gjelder AI og relaterte systemer, fremstår dataforgiftning som den mest betydelige sikkerhetstrusselen i dag. Dataforgiftning er når noen bevisst endrer informasjonen som brukes til å trene en AI, slik at den gjør feil. Dette skyldes mangelen på standardiserte metoder for deteksjon og begrensning, kombinert med vår avhengighet av ubetrodde eller ukurerte offentlige datasett for trening. For å opprettholde dataintegritet og forhindre en feil treningsprosess, er det avgjørende å spore opprinnelsen og slektskapet til dataene dine. Ellers holder det gamle ordtaket "søppel inn, søppel ut" sant, noe som fører til kompromittert modellprestasjon.

Her er eksempler på hvordan dataforgiftning kan påvirke modellene dine:

1. **Etikettendring**: I en binær klassifiseringsoppgave snur en motstander bevisst etikettene til en liten del av treningsdataene. For eksempel blir godartede prøver merket som ondsinnede, noe som fører til at modellen lærer feil assosiasjoner.
   **Eksempel**: Et spamfilter som feilklassifiserer legitime e-poster som spam på grunn av manipulerte etiketter.
2. **Funksjonsforgiftning**: En angriper endrer subtilt funksjoner i treningsdataene for å introdusere skjevhet eller villede modellen.
   **Eksempel**: Legge til irrelevante nøkkelord i produktbeskrivelser for å manipulere anbefalingssystemer.
3. **Datainjeksjon**: Injisere ondsinnede data i treningssettet for å påvirke modellens oppførsel.
   **Eksempel**: Introdusere falske brukeromtaler for å skjev analysen av sentimentresultater.
4. **Bakdørsangrep**: En motstander setter inn et skjult mønster (bakdør) i treningsdataene. Modellen lærer å gjenkjenne dette mønsteret og oppfører seg ondsinnet når det utløses.
   **Eksempel**: Et ansiktsgjenkjenningssystem trent med bilder med bakdør som feilgjenkjenner en bestemt person.

MITRE Corporation har laget [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)], en kunnskapsbase med taktikker og teknikker brukt av motstandere i virkelige angrep på AI-systemer.

Det finnes et økende antall sårbarheter i AI-aktiverte systemer, ettersom innføringen av AI øker angrepsflaten til eksisterende systemer utover de tradisjonelle cyber-angrepene. Vi utviklet ATLAS for å øke bevisstheten rundt disse unike og utviklende sårbarhetene, ettersom det globale samfunnet i økende grad innlemmer AI i ulike systemer. ATLAS er modellert etter MITRE ATT&CK®-rammeverket og dets taktikker, teknikker og prosedyrer (TTPs) er komplementære til de i ATT&CK.

I likhet med MITRE ATT&CK®-rammeverket, som er mye brukt i tradisjonell cybersikkerhet for å planlegge avanserte trusselemuleringsscenarier, gir ATLAS et lett søkbart sett med TTPs som kan hjelpe til med å bedre forstå og forberede seg på å forsvare seg mot nye angrep.

I tillegg har Open Web Application Security Project (OWASP) laget en "[Topp 10 liste]" over de mest kritiske sårbarhetene funnet i applikasjoner som bruker LLMs. Listen fremhever risikoen for trusler som den nevnte dataforgiftningen sammen med andre som:

- **Prompt Injection**: en teknikk der angripere manipulerer en Large Language Model (LLM) gjennom nøye utformede innganger, slik at den oppfører seg utenfor sin tiltenkte oppførsel.
- **Forsyningskjede-sårbarheter**: Komponentene og programvaren som utgjør applikasjonene som brukes av en LLM, som Python-moduler eller eksterne datasett, kan selv kompromitteres, noe som fører til uventede resultater, introduserte skjevheter og til og med sårbarheter i den underliggende infrastrukturen.
- **Overavhengighet**: LLMs er feilbare og har vært utsatt for å hallusinere, og gir unøyaktige eller usikre resultater. I flere dokumenterte tilfeller har folk tatt resultatene for god fisk, noe som har ført til utilsiktede negative konsekvenser i den virkelige verden.

Microsoft Cloud Advocate Rod Trent har skrevet en gratis e-bok, [Must Learn AI Security], som går dypt inn i disse og andre fremvoksende AI-trusler og gir omfattende veiledning om hvordan man best kan takle disse scenariene.

## Sikkerhetstesting for AI-systemer og LLMs

Kunstig intelligens (AI) transformerer ulike domener og bransjer, og gir nye muligheter og fordeler for samfunnet. Imidlertid medfører AI også betydelige utfordringer og risikoer, som databeskyttelse, skjevhet, mangel på forklarbarhet og potensiell misbruk. Derfor er det avgjørende å sikre at AI-systemer er sikre og ansvarlige, noe som betyr at de overholder etiske og juridiske standarder og kan stoles på av brukere og interessenter.

Sikkerhetstesting er prosessen med å evaluere sikkerheten til et AI-system eller LLM, ved å identifisere og utnytte deres sårbarheter. Dette kan utføres av utviklere, brukere eller tredjepartsrevisorer, avhengig av formålet og omfanget av testingen. Noen av de vanligste sikkerhetstestingsmetodene for AI-systemer og LLMs er:

- **Datasanering**: Dette er prosessen med å fjerne eller anonymisere sensitiv eller privat informasjon fra treningsdataene eller inputen til et AI-system eller LLM. Datasanering kan bidra til å forhindre datalekkasjer og ondsinnet manipulasjon ved å redusere eksponeringen av konfidensielle eller personlige data.
- **Adversarial testing**: Dette er prosessen med å generere og anvende motstridende eksempler til input eller output av et AI-system eller LLM for å evaluere dets robusthet og motstand mot motstridende angrep. Adversarial testing kan bidra til å identifisere og redusere sårbarhetene og svakhetene til et AI-system eller LLM som kan utnyttes av angripere.
- **Modellverifisering**: Dette er prosessen med å verifisere korrektheten og fullstendigheten av modellparametrene eller arkitekturen til et AI-system eller LLM. Modellverifisering kan bidra til å oppdage og forhindre modelltyveri ved å sikre at modellen er beskyttet og autentisert.
- **Output-validering**: Dette er prosessen med å validere kvaliteten og påliteligheten til outputen av et AI-system eller LLM. Output-validering kan bidra til å oppdage og korrigere ondsinnet manipulasjon ved å sikre at outputen er konsistent og nøyaktig.

OpenAI, en leder innen AI-systemer, har satt opp en serie med _sikkerhetsevalueringer_ som en del av deres red teaming-nettverksinitiativ, med mål om å teste outputen til AI-systemer i håp om å bidra til AI-sikkerhet.

Evalueringer kan variere fra enkle spørsmål og svar-tester til mer komplekse simuleringer. Som konkrete eksempler, her er prøveevalueringer utviklet av OpenAI for å evaluere AI-oppførsel fra flere vinkler:

#### Overbevisning

- [MakeMeSay]: Hvor godt kan et AI-system lure et annet AI-system til å si et hemmelig ord?
- [MakeMePay]: Hvor godt kan et AI-system overbevise et annet AI-system til å donere penger?
- [Ballot Proposal]: Hvor godt kan et AI-system påvirke et annet AI-systems støtte til et politisk forslag?

#### Steganografi (skjult meldingsformidling)

- [Steganography]: Hvor godt kan et AI-system ​​formidle hemmelige meldinger uten å bli oppdaget av et annet AI-system?
- [Text Compression]: Hvor godt kan et AI-system komprimere og dekomprimere meldinger, for å muliggjøre skjuling av hemmelige meldinger?
- [Schelling Point]: Hvor godt kan et AI-system koordinere med et annet AI-system, uten direkte kommunikasjon?

### AI-sikkerhet

Det er avgjørende at vi har som mål å beskytte AI-systemer mot ondsinnede angrep, misbruk eller utilsiktede konsekvenser. Dette inkluderer å ta skritt for å sikre sikkerheten, påliteligheten og tilliten til AI-systemer, slik som:

- Sikre dataene og algoritmene som brukes til å trene og kjøre AI-modeller
- Forhindre uautorisert tilgang, manipulasjon eller sabotasje av AI-systemer
- Oppdage og redusere skjevhet, diskriminering eller etiske problemer i AI-systemer
- Sikre ansvarlighet, åpenhet og forklarbarhet av AI-beslutninger og handlinger
- Justere målene og verdiene til AI-systemer med de til mennesker og samfunn

AI-sikkerhet er viktig for å sikre integriteten, tilgjengeligheten og konfidensialiteten til AI-systemer og data. Noen av utfordringene og mulighetene ved AI-sikkerhet er:

- Mulighet: Inkorporere AI i cybersikkerhetsstrategier siden det kan spille en viktig rolle i å identifisere trusler og forbedre responstider. AI kan bidra til å automatisere og forsterke deteksjon og reduksjon av cyberangrep, som phishing, malware eller ransomware.
- Utfordring: AI kan også brukes av motstandere til å lansere sofistikerte angrep, som å generere falskt eller misvisende innhold, utgi seg for brukere, eller utnytte sårbarheter i AI-systemer. Derfor har AI-utviklere et unikt ansvar for å designe systemer som er robuste og motstandsdyktige mot misbruk.

### Databeskyttelse

LLMs kan utgjøre risikoer for personvernet og sikkerheten til dataene de bruker. For eksempel kan LLMs potensielt huske og lekke sensitiv informasjon fra treningsdataene sine, som personlige navn, adresser, passord eller kredittkortnumre. De kan også manipuleres eller angripes av ondsinnede aktører som ønsker å utnytte deres sårbarheter eller skjevheter. Derfor er det viktig å være klar over disse risikoene og ta passende tiltak for å beskytte dataene som brukes med LLMs. Det finnes flere trinn du kan ta for å beskytte dataene som brukes med LLMs. Disse trinnene inkluderer:

- **Begrense mengden og typen data de deler med LLMs**: Del kun dataene som er nødvendige og relevante for de tiltenkte formålene, og unngå å dele data som er sensitive, konfidensielle eller personlige. Brukere bør også anonymisere eller kryptere dataene de deler med LLMs, som ved å fjerne eller maskere identifiserende informasjon, eller bruke sikre kommunikasjonskanaler.
- **Verifisere dataene som LLMs genererer**: Sjekk alltid nøyaktigheten og kvaliteten på outputen generert av LLMs for å sikre at de ikke inneholder uønsket eller upassende informasjon.
- **Rapportere og varsle om datalekkasjer eller hendelser**: Vær oppmerksom på mistenkelige eller unormale aktiviteter eller oppførsel fra LLMs, som å generere tekster som er irrelevante, unøyaktige, støtende eller skadelige. Dette kan være en indikasjon på en datalekkasje eller sikkerhetshendelse.

Datasikkerhet, styring og samsvar er kritisk for enhver organisasjon som ønsker å utnytte kraften av data og AI i et multi-cloud miljø. Å sikre og styre all din data er en kompleks og mangesidig oppgave. Du trenger å sikre og styre ulike typer data (strukturert, ustrukturert, og data generert av AI) på ulike steder over flere skyer, og du må ta hensyn til eksisterende og fremtidige datasikkerhet, styring, og AI-reguleringer. For å beskytte dine data, må du ta i bruk noen beste praksiser og forholdsregler, som:

- Bruk sky-tjenester eller plattformer som tilbyr databeskyttelse og personvernfunksjoner.
- Bruk datakvalitet og valideringsverktøy for å sjekke dine data for feil, inkonsistenser eller avvik.
- Bruk datastyring og etiske rammeverk for å sikre at dine data brukes på en ansvarlig og transparent måte.

### Emulering av virkelige trusler - AI red teaming

Emulering av virkelige trusler anses nå som en standard praksis i byggingen av robuste AI-systemer ved å bruke lignende verktøy, taktikker, prosedyrer for å identifisere risikoene til systemer og teste responsen til forsvarere.

Praksisen med AI red teaming har utviklet seg til å ta på en mer utvidet betydning: det dekker ikke bare prøving for sikkerhetssårbarheter, men inkluderer også prøving for andre systemfeil, som generering av potensielt skadelig innhold. AI-systemer kommer med nye risikoer, og red teaming er sentralt for å forstå de nye risikoene, som prompt injection og produksjon av ubegrunnet innhold. - [Microsoft AI Red Team bygger fremtiden for sikrere AI]

Nedenfor er viktige innsikter som har formet Microsofts AI Red Team-program.

1. **Utvidet omfang av AI Red Teaming:**
   AI red teaming dekker nå både sikkerhet og Responsible AI (RAI) utfall. Tradisjonelt fokuserte red teaming på sikkerhetsaspekter, og behandlet modellen som en vektor (f.eks. stjele den underliggende modellen). Imidlertid introduserer AI-systemer nye sikkerhetssårbarheter (f.eks. prompt injection, forgiftning), som krever spesiell oppmerksomhet. Utover sikkerhet, undersøker AI red teaming også rettferdighetsproblemer (f.eks. stereotyping) og skadelig innhold (f.eks. glorifisering av vold). Tidlig identifikasjon av disse problemene tillater prioritering av forsvarsinvesteringer.
2. **Ondsinnede og godartede feil:**
   AI red teaming vurderer feil fra både ondsinnede og godartede perspektiver. For eksempel, når vi red teaming den nye Bing, utforsker vi ikke bare hvordan ondsinnede motstandere kan undergrave systemet, men også hvordan vanlige brukere kan støte på problematisk eller skadelig innhold. I motsetning til tradisjonell sikkerhetsred teaming, som fokuserer hovedsakelig på ondsinnede aktører, tar AI red teaming hensyn til et bredere spekter av personaer og potensielle feil.
3. **Dynamisk natur av AI-systemer:**
   AI-applikasjoner utvikler seg kontinuerlig. I applikasjoner med store språkmodeller tilpasser utviklere seg til skiftende krav. Kontinuerlig red teaming sikrer vedvarende årvåkenhet og tilpasning til utviklende risikoer.

AI red teaming er ikke altomfattende og bør betraktes som

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår fra bruken av denne oversettelsen.