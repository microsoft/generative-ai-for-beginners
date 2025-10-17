<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-17T19:09:30+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "da"
}
-->
# Sikring af dine generative AI-applikationer

[![Sikring af dine generative AI-applikationer](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.da.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## Introduktion

Denne lektion vil dække:

- Sikkerhed i konteksten af AI-systemer.
- Almindelige risici og trusler mod AI-systemer.
- Metoder og overvejelser for at sikre AI-systemer.

## Læringsmål

Efter at have gennemført denne lektion vil du have forståelse for:

- Trusler og risici mod AI-systemer.
- Almindelige metoder og praksisser til at sikre AI-systemer.
- Hvordan implementering af sikkerhedstest kan forhindre uventede resultater og tab af brugertillid.

## Hvad betyder sikkerhed i konteksten af generativ AI?

Efterhånden som kunstig intelligens (AI) og maskinlæring (ML) teknologier i stigende grad påvirker vores liv, er det afgørende at beskytte ikke kun kundedata, men også selve AI-systemerne. AI/ML bruges i stigende grad til at understøtte beslutningsprocesser med høj værdi i industrier, hvor forkerte beslutninger kan få alvorlige konsekvenser.

Her er nogle vigtige punkter at overveje:

- **Indvirkning af AI/ML**: AI/ML har betydelig indflydelse på dagligdagen, og det er derfor blevet essentielt at beskytte dem.
- **Sikkerhedsudfordringer**: Den indflydelse, som AI/ML har, kræver opmærksomhed for at adressere behovet for at beskytte AI-baserede produkter mod sofistikerede angreb, uanset om de kommer fra trollere eller organiserede grupper.
- **Strategiske problemer**: Teknologiindustrien skal proaktivt tage fat på strategiske udfordringer for at sikre langsigtet kundesikkerhed og datasikkerhed.

Derudover er maskinlæringsmodeller generelt ude af stand til at skelne mellem skadelig input og harmløse anomale data. En betydelig kilde til træningsdata stammer fra ukurerede, umodererede, offentlige datasæt, som er åbne for bidrag fra tredjeparter. Angribere behøver ikke kompromittere datasæt, når de frit kan bidrage til dem. Over tid bliver lavtillids skadelige data til højtillids betroede data, hvis datastrukturen/formatet forbliver korrekt.

Derfor er det kritisk at sikre integriteten og beskyttelsen af de datalagre, som dine modeller bruger til at træffe beslutninger.

## Forståelse af trusler og risici ved AI

Når det kommer til AI og relaterede systemer, er datapoisoning den mest betydelige sikkerhedstrussel i dag. Datapoisoning opstår, når nogen bevidst ændrer de oplysninger, der bruges til at træne en AI, hvilket får den til at begå fejl. Dette skyldes manglen på standardiserede metoder til detektion og afhjælpning, kombineret med vores afhængighed af utroværdige eller ukurerede offentlige datasæt til træning. For at opretholde dataintegritet og forhindre en fejlbehæftet træningsproces er det afgørende at spore oprindelsen og afstamningen af dine data. Ellers gælder det gamle ordsprog "skrald ind, skrald ud", hvilket fører til kompromitteret modelpræstation.

Her er eksempler på, hvordan datapoisoning kan påvirke dine modeller:

1. **Label Flipping**: I en binær klassifikationsopgave ændrer en modstander bevidst etiketterne på en lille del af træningsdataene. For eksempel bliver harmløse prøver mærket som skadelige, hvilket får modellen til at lære forkerte associationer.\
   **Eksempel**: Et spamfilter klassificerer legitime e-mails som spam på grund af manipulerede etiketter.
2. **Feature Poisoning**: En angriber ændrer subtilt funktioner i træningsdataene for at introducere bias eller vildlede modellen.\
   **Eksempel**: Tilføjelse af irrelevante nøgleord til produktbeskrivelser for at manipulere anbefalingssystemer.
3. **Data Injection**: Indsprøjtning af skadelige data i træningssættet for at påvirke modellens adfærd.\
   **Eksempel**: Introduktion af falske brugeranmeldelser for at skævvride sentimentanalyse-resultater.
4. **Backdoor Attacks**: En modstander indsætter et skjult mønster (backdoor) i træningsdataene. Modellen lærer at genkende dette mønster og opfører sig skadeligt, når det aktiveres.\
   **Eksempel**: Et ansigtsgenkendelsessystem trænet med bagdørbilleder, der fejlagtigt identificerer en bestemt person.

MITRE Corporation har skabt [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), en vidensbase over taktikker og teknikker anvendt af modstandere i virkelige angreb på AI-systemer.

> Der er et stigende antal sårbarheder i AI-aktiverede systemer, da inkorporeringen af AI øger angrebsfladen for eksisterende systemer ud over traditionelle cyberangreb. Vi udviklede ATLAS for at øge bevidstheden om disse unikke og udviklende sårbarheder, da det globale samfund i stigende grad inkorporerer AI i forskellige systemer. ATLAS er modelleret efter MITRE ATT&CK®-rammen, og dens taktikker, teknikker og procedurer (TTP'er) er komplementære til dem i ATT&CK.

Ligesom MITRE ATT&CK®-rammen, som er meget brugt i traditionel cybersikkerhed til planlægning af avancerede trusselsimuleringer, giver ATLAS et let søgbart sæt TTP'er, der kan hjælpe med bedre at forstå og forberede sig på at forsvare sig mod nye angreb.

Derudover har Open Web Application Security Project (OWASP) skabt en "[Top 10-liste](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" over de mest kritiske sårbarheder fundet i applikationer, der anvender LLM'er. Listen fremhæver risici ved trusler som den førnævnte datapoisoning samt andre som:

- **Prompt Injection**: En teknik, hvor angribere manipulerer en Large Language Model (LLM) gennem nøje udformede inputs, hvilket får den til at opføre sig uden for sin tilsigtede adfærd.
- **Forsyningskædesårbarheder**: De komponenter og software, der udgør applikationerne, der bruges af en LLM, såsom Python-moduler eller eksterne datasæt, kan selv kompromitteres, hvilket fører til uventede resultater, introducerede bias og endda sårbarheder i den underliggende infrastruktur.
- **Overafhængighed**: LLM'er er fejlbehæftede og har været tilbøjelige til at hallucinere, hvilket resulterer i unøjagtige eller usikre resultater. I flere dokumenterede tilfælde har folk taget resultaterne for gode varer, hvilket har ført til utilsigtede negative konsekvenser i den virkelige verden.

Microsoft Cloud Advocate Rod Trent har skrevet en gratis e-bog, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), der går dybt ind i disse og andre fremvoksende AI-trusler og giver omfattende vejledning om, hvordan man bedst tackler disse scenarier.

## Sikkerhedstest for AI-systemer og LLM'er

Kunstig intelligens (AI) transformerer forskellige domæner og industrier og tilbyder nye muligheder og fordele for samfundet. Men AI medfører også betydelige udfordringer og risici, såsom databeskyttelse, bias, manglende forklarbarhed og potentiel misbrug. Derfor er det afgørende at sikre, at AI-systemer er sikre og ansvarlige, hvilket betyder, at de overholder etiske og juridiske standarder og kan stole på af brugere og interessenter.

Sikkerhedstest er processen med at evaluere sikkerheden af et AI-system eller LLM ved at identificere og udnytte deres sårbarheder. Dette kan udføres af udviklere, brugere eller tredjepartsrevisorer, afhængigt af formålet og omfanget af testen. Nogle af de mest almindelige metoder til sikkerhedstest for AI-systemer og LLM'er er:

- **Datasanering**: Dette er processen med at fjerne eller anonymisere følsomme eller private oplysninger fra træningsdataene eller inputtet til et AI-system eller LLM. Datasanering kan hjælpe med at forhindre datalækage og skadelig manipulation ved at reducere eksponeringen af fortrolige eller personlige data.
- **Adversarial testing**: Dette er processen med at generere og anvende fjendtlige eksempler på inputtet eller outputtet af et AI-system eller LLM for at evaluere dets robusthed og modstandsdygtighed mod fjendtlige angreb. Adversarial testing kan hjælpe med at identificere og afhjælpe sårbarheder og svagheder i et AI-system eller LLM, der kan udnyttes af angribere.
- **Modelverifikation**: Dette er processen med at verificere korrektheden og fuldstændigheden af modelparametrene eller arkitekturen for et AI-system eller LLM. Modelverifikation kan hjælpe med at opdage og forhindre modeltyveri ved at sikre, at modellen er beskyttet og autentificeret.
- **Outputvalidering**: Dette er processen med at validere kvaliteten og pålideligheden af outputtet fra et AI-system eller LLM. Outputvalidering kan hjælpe med at opdage og rette skadelig manipulation ved at sikre, at outputtet er konsistent og nøjagtigt.

OpenAI, en leder inden for AI-systemer, har oprettet en række _sikkerhedsevalueringer_ som en del af deres red teaming-netværksinitiativ, der sigter mod at teste output fra AI-systemer i håb om at bidrage til AI-sikkerhed.

> Evalueringer kan variere fra simple Q&A-tests til mere komplekse simuleringer. Som konkrete eksempler er her prøveevalueringer udviklet af OpenAI til at evaluere AI-adfærd fra flere vinkler:

#### Overtalelse

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system narre et andet AI-system til at sige et hemmeligt ord?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system overbevise et andet AI-system om at donere penge?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system påvirke et andet AI-systems støtte til et politisk forslag?

#### Steganografi (skjulte beskeder)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system sende hemmelige beskeder uden at blive opdaget af et andet AI-system?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system komprimere og dekomprimere beskeder for at muliggøre skjulte beskeder?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system koordinere med et andet AI-system uden direkte kommunikation?

### AI-sikkerhed

Det er afgørende, at vi stræber efter at beskytte AI-systemer mod skadelige angreb, misbrug eller utilsigtede konsekvenser. Dette inkluderer at tage skridt til at sikre sikkerheden, pålideligheden og troværdigheden af AI-systemer, såsom:

- Sikring af de data og algoritmer, der bruges til at træne og køre AI-modeller
- Forebyggelse af uautoriseret adgang, manipulation eller sabotage af AI-systemer
- Identifikation og afhjælpning af bias, diskrimination eller etiske problemer i AI-systemer
- Sikring af ansvarlighed, gennemsigtighed og forklarbarhed i AI-beslutninger og handlinger
- Tilpasning af AI-systemers mål og værdier med menneskers og samfundets

AI-sikkerhed er vigtig for at sikre integriteten, tilgængeligheden og fortroligheden af AI-systemer og data. Nogle af udfordringerne og mulighederne ved AI-sikkerhed er:

- Mulighed: Inkorporering af AI i cybersikkerhedsstrategier, da det kan spille en afgørende rolle i at identificere trusler og forbedre responstider. AI kan hjælpe med at automatisere og forstærke detektion og afhjælpning af cyberangreb, såsom phishing, malware eller ransomware.
- Udfordring: AI kan også bruges af modstandere til at lancere sofistikerede angreb, såsom at generere falsk eller vildledende indhold, udgive sig for at være brugere eller udnytte sårbarheder i AI-systemer. Derfor har AI-udviklere et unikt ansvar for at designe systemer, der er robuste og modstandsdygtige mod misbrug.

### Databeskyttelse

LLM'er kan udgøre risici for privatlivets fred og sikkerheden af de data, de bruger. For eksempel kan LLM'er potentielt huske og lække følsomme oplysninger fra deres træningsdata, såsom personlige navne, adresser, adgangskoder eller kreditkortnumre. De kan også manipuleres eller angribes af skadelige aktører, der ønsker at udnytte deres sårbarheder eller bias. Derfor er det vigtigt at være opmærksom på disse risici og tage passende foranstaltninger for at beskytte de data, der bruges med LLM'er. Der er flere trin, du kan tage for at beskytte de data, der bruges med LLM'er. Disse trin inkluderer:

- **Begrænsning af mængden og typen af data, der deles med LLM'er**: Del kun de data, der er nødvendige og relevante for de tilsigtede formål, og undgå at dele data, der er følsomme, fortrolige eller personlige. Brugere bør også anonymisere eller kryptere de data, de deler med LLM'er, såsom ved at fjerne eller maskere identificerende oplysninger eller bruge sikre kommunikationskanaler.
- **Verificering af de data, som LLM'er genererer**: Kontroller altid nøjagtigheden og kvaliteten af det output, der genereres af LLM'er, for at sikre, at det ikke indeholder uønskede eller upassende oplysninger.
- **Rapportering og alarmering af eventuelle databrud eller hændelser**: Vær opmærksom på mistænkelige eller unormale aktiviteter eller adfærd fra LLM'er, såsom generering af tekster, der er irrelevante, unøjagtige, stødende eller skadelige. Dette kan være en indikation på et databrud eller en sikkerhedshændelse.

Datasikkerhed, governance og overholdelse er kritisk for enhver organisation, der ønsker at udnytte data og AI's kraft i et multi-cloud-miljø. At sikre og styre alle dine data er en kompleks og mangefacetteret opgave. Du skal sikre og styre forskellige typer data (strukturerede, ustrukturerede og data genereret af AI) på forskellige lokationer på tværs af flere clouds, og du skal tage højde for eksisterende og fremtidige datasikkerheds-, governance- og AI-regler. For at beskytte dine data skal du vedtage nogle bedste praksisser og forholdsregler, såsom:

- Brug cloud-tjenester eller platforme, der tilbyder databeskyttelses- og privatlivsfunktioner.
- Brug værktøjer til datakvalitet og validering for at kontrollere dine data for fejl, uoverensstemmelser eller anomalier.
- Brug rammer for datastyring og etik for at sikre, at dine data bruges på en ansvarlig og gennemsigtig måde.

### Simulering af virkelige trusler - AI red teaming
At efterligne trusler fra den virkelige verden betragtes nu som en standardpraksis i opbygningen af robuste AI-systemer ved at anvende lignende værktøjer, taktikker og procedurer for at identificere risici for systemer og teste forsvarernes respons.

> Praksis med AI red teaming har udviklet sig til at få en mere udvidet betydning: det dækker ikke kun søgning efter sikkerhedssårbarheder, men også søgning efter andre systemfejl, såsom generering af potentielt skadeligt indhold. AI-systemer medfører nye risici, og red teaming er centralt for at forstå disse nye risici, såsom prompt injection og produktion af ubegrundet indhold. - [Microsoft AI Red Team bygger fremtidens sikrere AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Vejledning og ressourcer til red teaming](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.da.png)]()

Nedenfor er nøgleindsigter, der har formet Microsofts AI Red Team-program.

1. **Udvidet omfang af AI Red Teaming:**
   AI red teaming omfatter nu både sikkerhed og ansvarlig AI (RAI) resultater. Traditionelt fokuserede red teaming på sikkerhedsaspekter og behandlede modellen som en vektor (f.eks. tyveri af den underliggende model). Men AI-systemer introducerer nye sikkerhedssårbarheder (f.eks. prompt injection, poisoning), som kræver særlig opmærksomhed. Ud over sikkerhed undersøger AI red teaming også retfærdighedsproblemer (f.eks. stereotyper) og skadeligt indhold (f.eks. glorificering af vold). Tidlig identifikation af disse problemer gør det muligt at prioritere forsvarsinvesteringer.
2. **Ondsindede og harmløse fejl:**
   AI red teaming tager højde for fejl fra både ondsindede og harmløse perspektiver. For eksempel, når vi red teamer den nye Bing, undersøger vi ikke kun, hvordan ondsindede aktører kan undergrave systemet, men også hvordan almindelige brugere kan støde på problematisk eller skadeligt indhold. I modsætning til traditionel sikkerhedsred teaming, som primært fokuserer på ondsindede aktører, tager AI red teaming højde for et bredere spektrum af personas og potentielle fejl.
3. **Dynamisk natur af AI-systemer:**
   AI-applikationer udvikler sig konstant. I applikationer med store sprogmodeller tilpasser udviklere sig til skiftende krav. Kontinuerlig red teaming sikrer løbende årvågenhed og tilpasning til udviklende risici.

AI red teaming er ikke altomfattende og bør betragtes som et supplement til yderligere kontroller såsom [rollebaseret adgangskontrol (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) og omfattende datastyringsløsninger. Det er beregnet til at supplere en sikkerhedsstrategi, der fokuserer på at anvende sikre og ansvarlige AI-løsninger, der tager højde for privatliv og sikkerhed, samtidig med at man stræber efter at minimere bias, skadeligt indhold og misinformation, der kan underminere brugerens tillid.

Her er en liste over yderligere læsning, der kan hjælpe dig med bedre at forstå, hvordan red teaming kan hjælpe med at identificere og afbøde risici i dine AI-systemer:

- [Planlægning af red teaming for store sprogmodeller (LLMs) og deres applikationer](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [Hvad er OpenAI Red Teaming Network?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI Red Teaming - En nøglepraksis for at bygge sikrere og mere ansvarlige AI-løsninger](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), en vidensbase over taktikker og teknikker anvendt af modstandere i virkelige angreb på AI-systemer.

## Videnscheck

Hvad kunne være en god tilgang til at opretholde dataintegritet og forhindre misbrug?

1. Have stærke rollebaserede kontroller for dataadgang og datastyring  
1. Implementere og revidere datamærkning for at forhindre datamisrepræsentation eller misbrug  
1. Sikre, at din AI-infrastruktur understøtter indholdsfiltrering  

A:1, Selvom alle tre er gode anbefalinger, vil det at sikre, at du tildeler de korrekte dataadgangsrettigheder til brugere, gøre meget for at forhindre manipulation og misrepræsentation af de data, der bruges af LLM'er.

## 🚀 Udfordring

Læs mere om, hvordan du kan [styre og beskytte følsomme oplysninger](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) i AI's tidsalder.

## Godt arbejde, fortsæt din læring

Efter at have afsluttet denne lektion, kan du tjekke vores [Generative AI Learning-samling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at opbygge din viden om Generative AI!

Gå videre til Lektion 14, hvor vi vil se på [livscyklussen for generative AI-applikationer](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.