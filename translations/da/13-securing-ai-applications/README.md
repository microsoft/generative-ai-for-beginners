<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T21:19:55+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "da"
}
-->
# Sikring af dine generative AI-applikationer

## Introduktion

Denne lektion vil dække:

- Sikkerhed inden for AI-systemers kontekst.
- Almindelige risici og trusler mod AI-systemer.
- Metoder og overvejelser for at sikre AI-systemer.

## Læringsmål

Efter at have gennemført denne lektion vil du have en forståelse af:

- Trusler og risici mod AI-systemer.
- Almindelige metoder og praksisser til at sikre AI-systemer.
- Hvordan implementering af sikkerhedstest kan forhindre uventede resultater og tab af brugerens tillid.

## Hvad betyder sikkerhed inden for konteksten af generativ AI?

Efterhånden som kunstig intelligens (AI) og maskinlæring (ML) teknologier i stigende grad former vores liv, er det vigtigt at beskytte ikke kun kundedata, men også AI-systemerne selv. AI/ML anvendes i stigende grad til at støtte beslutningsprocesser med høj værdi i industrier, hvor forkerte beslutninger kan have alvorlige konsekvenser.

Her er vigtige punkter at overveje:

- **Indflydelse af AI/ML**: AI/ML har betydelig indflydelse på dagligdagen, og derfor er det blevet essentielt at beskytte dem.
- **Sikkerhedsudfordringer**: Denne indflydelse, som AI/ML har, kræver opmærksomhed for at beskytte AI-baserede produkter mod sofistikerede angreb, hvad enten de kommer fra trollere eller organiserede grupper.
- **Strategiske problemer**: Teknologibranchen skal proaktivt tage fat på strategiske udfordringer for at sikre langsigtet kundesikkerhed og databeskyttelse.

Desuden er maskinlæringsmodeller stort set ude af stand til at skelne mellem ondsindet input og harmløse anomale data. En betydelig kilde til træningsdata er afledt fra ukurerede, umodererede offentlige datasæt, som er åbne for bidrag fra tredjeparter. Angribere behøver ikke at kompromittere datasæt, når de frit kan bidrage til dem. Over tid bliver data med lav tillid til data med høj tillid, hvis datastrukturen/formatet forbliver korrekt.

Derfor er det kritisk at sikre integriteten og beskyttelsen af de datalagre, dine modeller bruger til at træffe beslutninger med.

## Forståelse af trusler og risici ved AI

Når det kommer til AI og relaterede systemer, skiller datapoisoning sig ud som den mest betydelige sikkerhedstrussel i dag. Datapoisoning er, når nogen bevidst ændrer de oplysninger, der bruges til at træne en AI, hvilket får den til at begå fejl. Dette skyldes fraværet af standardiserede detektions- og afhjælpningsmetoder, kombineret med vores afhængighed af upålidelige eller ukurerede offentlige datasæt til træning. For at opretholde dataintegritet og forhindre en fejlbehæftet træningsproces er det afgørende at spore oprindelsen og afstamningen af dine data. Ellers holder det gamle ordsprog "skrald ind, skrald ud" stik, hvilket fører til kompromitteret modelpræstation.

Her er eksempler på, hvordan datapoisoning kan påvirke dine modeller:

1. **Etiketombytning**: I en binær klassifikationsopgave ombytter en modstander bevidst etiketterne på en lille delmængde af træningsdataene. For eksempel mærkes harmløse prøver som ondsindede, hvilket får modellen til at lære forkerte associationer.\
   **Eksempel**: Et spamfilter, der fejlagtigt klassificerer legitime e-mails som spam på grund af manipulerede etiketter.
2. **Feature Poisoning**: En angriber ændrer subtilt features i træningsdataene for at introducere bias eller vildlede modellen.\
   **Eksempel**: Tilføjelse af irrelevante nøgleord til produktbeskrivelser for at manipulere anbefalingssystemer.
3. **Dataindsprøjtning**: Indsprøjtning af ondsindede data i træningssættet for at påvirke modellens adfærd.\
   **Eksempel**: Introduktion af falske brugeranmeldelser for at skævvride sentimentanalyse resultater.
4. **Bagdørsangreb**: En modstander indsætter et skjult mønster (bagdør) i træningsdataene. Modellen lærer at genkende dette mønster og opfører sig ondsindet, når det udløses.\
   **Eksempel**: Et ansigtsgenkendelsessystem trænet med bagdørsbilleder, der fejlidentificerer en bestemt person.

MITRE Corporation har skabt [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), en vidensbase over taktikker og teknikker anvendt af modstandere i virkelige angreb på AI-systemer.

> Der er et stigende antal sårbarheder i AI-aktiverede systemer, da inkorporeringen af AI øger angrebsfladen af eksisterende systemer ud over traditionelle cyberangreb. Vi udviklede ATLAS for at øge bevidstheden om disse unikke og udviklende sårbarheder, da det globale samfund i stigende grad inkorporerer AI i forskellige systemer. ATLAS er modelleret efter MITRE ATT&CK®-rammen, og dens taktikker, teknikker og procedurer (TTP'er) er komplementære til dem i ATT&CK.

Ligesom MITRE ATT&CK®-rammen, der er udbredt i traditionel cybersikkerhed til planlægning af avancerede trusselsimuleringer, giver ATLAS et let søgbart sæt TTP'er, der kan hjælpe med at forstå og forberede sig på at forsvare sig mod nye angreb.

Derudover har Open Web Application Security Project (OWASP) skabt en "[Top 10-liste](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" over de mest kritiske sårbarheder fundet i applikationer, der bruger LLM'er. Listen fremhæver risikoen for trusler som den førnævnte datapoisoning sammen med andre som:

- **Prompt Injection**: en teknik, hvor angribere manipulerer en Large Language Model (LLM) gennem omhyggeligt udformede inputs, hvilket får den til at opføre sig uden for dens tilsigtede adfærd.
- **Forsyningskædesårbarheder**: De komponenter og software, der udgør applikationerne brugt af en LLM, såsom Python-moduler eller eksterne datasæt, kan selv blive kompromitteret, hvilket fører til uventede resultater, introducerede bias og endda sårbarheder i den underliggende infrastruktur.
- **Overafhængighed**: LLM'er er fejlbarlige og har været tilbøjelige til at hallucinere, hvilket giver unøjagtige eller usikre resultater. I flere dokumenterede omstændigheder har folk taget resultaterne for pålydende, hvilket har ført til utilsigtede negative konsekvenser i den virkelige verden.

Microsoft Cloud Advocate Rod Trent har skrevet en gratis e-bog, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), der dykker dybt ned i disse og andre nye AI-trusler og giver omfattende vejledning i, hvordan man bedst håndterer disse scenarier.

## Sikkerhedstest for AI-systemer og LLM'er

Kunstig intelligens (AI) omformer forskellige domæner og industrier, hvilket tilbyder nye muligheder og fordele for samfundet. Dog udgør AI også betydelige udfordringer og risici, såsom databeskyttelse, bias, manglende forklarlighed og potentiel misbrug. Derfor er det afgørende at sikre, at AI-systemer er sikre og ansvarlige, hvilket betyder, at de overholder etiske og juridiske standarder og kan stole på af brugere og interessenter.

Sikkerhedstest er processen med at evaluere sikkerheden af et AI-system eller LLM ved at identificere og udnytte deres sårbarheder. Dette kan udføres af udviklere, brugere eller tredjepartsrevisorer, afhængigt af formålet og omfanget af testen. Nogle af de mest almindelige sikkerhedstestmetoder for AI-systemer og LLM'er er:

- **Datasanitering**: Dette er processen med at fjerne eller anonymisere følsomme eller private oplysninger fra træningsdataene eller inputtet til et AI-system eller LLM. Datasanitering kan hjælpe med at forhindre datalækager og ondsindet manipulation ved at reducere eksponeringen af fortrolige eller personlige data.
- **Adversarial testing**: Dette er processen med at generere og anvende modstridende eksempler til input eller output af et AI-system eller LLM for at evaluere dets robusthed og modstandsdygtighed mod modstridende angreb. Adversarial testing kan hjælpe med at identificere og afhjælpe sårbarheder og svagheder i et AI-system eller LLM, der kan udnyttes af angribere.
- **Modelverifikation**: Dette er processen med at verificere korrektheden og fuldstændigheden af modelparametrene eller arkitekturen af et AI-system eller LLM. Modelverifikation kan hjælpe med at opdage og forhindre modeltyveri ved at sikre, at modellen er beskyttet og autentificeret.
- **Outputvalidering**: Dette er processen med at validere kvaliteten og pålideligheden af outputtet fra et AI-system eller LLM. Outputvalidering kan hjælpe med at opdage og rette ondsindet manipulation ved at sikre, at outputtet er konsistent og præcist.

OpenAI, en leder inden for AI-systemer, har oprettet en række _sikkerhedsevalueringer_ som en del af deres red teaming-netværksinitiativ, med det formål at teste output fra AI-systemer i håb om at bidrage til AI-sikkerhed.

> Evalueringer kan spænde fra simple spørgsmål og svar-tests til mere komplekse simulationer. Som konkrete eksempler er her eksempler på evalueringer udviklet af OpenAI til at evaluere AI-adfærd fra flere vinkler:

#### Overbevisning

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system narre et andet AI-system til at sige et hemmeligt ord?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system overbevise et andet AI-system til at donere penge?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system påvirke et andet AI-systems støtte til et politisk forslag?

#### Steganografi (skjulte beskeder)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system sende hemmelige beskeder uden at blive fanget af et andet AI-system?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system komprimere og dekomprimere beskeder for at muliggøre skjulte beskeder?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Hvor godt kan et AI-system koordinere med et andet AI-system uden direkte kommunikation?

### AI Sikkerhed

Det er afgørende, at vi sigter mod at beskytte AI-systemer mod ondsindede angreb, misbrug eller utilsigtede konsekvenser. Dette inkluderer at tage skridt til at sikre sikkerheden, pålideligheden og troværdigheden af AI-systemer, såsom:

- Sikring af de data og algoritmer, der bruges til at træne og køre AI-modeller
- Forhindre uautoriseret adgang, manipulation eller sabotage af AI-systemer
- Detektere og afhjælpe bias, diskrimination eller etiske problemer i AI-systemer
- Sikre ansvarlighed, gennemsigtighed og forklarlighed af AI-beslutninger og handlinger
- Tilpasse AI-systemers mål og værdier med dem fra mennesker og samfundet

AI-sikkerhed er vigtig for at sikre integriteten, tilgængeligheden og fortroligheden af AI-systemer og data. Nogle af udfordringerne og mulighederne for AI-sikkerhed er:

- Mulighed: Inkorporering af AI i cybersikkerhedsstrategier, da det kan spille en afgørende rolle i at identificere trusler og forbedre reaktionstider. AI kan hjælpe med at automatisere og forstærke detektionen og afhjælpningen af cyberangreb, såsom phishing, malware eller ransomware.
- Udfordring: AI kan også bruges af modstandere til at lancere sofistikerede angreb, såsom generering af falsk eller vildledende indhold, efterligning af brugere eller udnyttelse af sårbarheder i AI-systemer. Derfor har AI-udviklere et unikt ansvar for at designe systemer, der er robuste og modstandsdygtige mod misbrug.

### Databeskyttelse

LLM'er kan udgøre risici for privatlivets fred og sikkerheden for de data, de bruger. For eksempel kan LLM'er potentielt huske og lække følsomme oplysninger fra deres træningsdata, såsom personlige navne, adresser, adgangskoder eller kreditkortnumre. De kan også manipuleres eller angribes af ondsindede aktører, der ønsker at udnytte deres sårbarheder eller bias. Derfor er det vigtigt at være opmærksom på disse risici og tage passende foranstaltninger for at beskytte de data, der bruges med LLM'er. Der er flere skridt, du kan tage for at beskytte de data, der bruges med LLM'er. Disse skridt inkluderer:

- **Begrænse mængden og typen af data, de deler med LLM'er**: Del kun de data, der er nødvendige og relevante for de tilsigtede formål, og undgå at dele data, der er følsomme, fortrolige eller personlige. Brugere bør også anonymisere eller kryptere de data, de deler med LLM'er, såsom ved at fjerne eller maskere enhver identificerende information eller bruge sikre kommunikationskanaler.
- **Verificere de data, som LLM'er genererer**: Tjek altid nøjagtigheden og kvaliteten af outputtet genereret af LLM'er for at sikre, at de ikke indeholder uønsket eller upassende information.
- **Rapportere og advare om databrud eller hændelser**: Vær opmærksom på enhver mistænkelig eller unormal aktivitet eller adfærd fra LLM'er, såsom generering af tekster, der er irrelevante, unøjagtige, stødende eller skadelige. Dette kan være en indikation af et databrud eller en sikkerhedshændelse.

Datasikkerhed, styring og overholdelse er kritisk for enhver organisation, der ønsker at udnytte dataens og AI's kraft i et multi-cloud-miljø. At sikre og styre alle dine data er en kompleks og mangefacetteret opgave. Du skal sikre og styre forskellige typer data (struktureret, ustruktureret og data genereret af AI) på forskellige steder på tværs af flere skyer, og du skal tage højde for eksisterende og fremtidige datasikkerhed, styring og AI-reguleringer. For at beskytte dine data skal du vedtage nogle bedste praksisser og forholdsregler, såsom:

- Brug cloud-tjenester eller platforme, der tilbyder databeskyttelse og privatlivsfunktioner.
- Brug datakvalitets- og valideringsværktøjer til at tjekke dine data for fejl, uoverensstemmelser eller anomalier.
- Brug data governance og etiske rammer til at sikre, at dine data bruges på en ansvarlig og gennemsigtig måde.

### Emulering af virkelige trusler - AI red teaming

Emulering af virkelige trusler betragtes nu som en standardpraksis i opbygningen af modstandsdygtige AI-systemer ved at anvende lignende værktøjer, taktikker og procedurer til at identificere risici for systemer og teste forsvarernes respons.

> Praksis med AI red teaming har udviklet sig til at få en mere udvidet betydning: det dækker ikke kun sondering for sikkerhedssårbarheder, men inkluderer også sondering for andre systemfejl, såsom generering af potentielt skadeligt indhold. AI-systemer kommer med nye risici, og red teaming er kernen i at forstå disse nye risici, såsom prompt injection og produktion af ubegrundet indhold. - [Microsoft AI Red Team bygger fremtiden for sikrere AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

Nedenfor er vigtige indsigter, der har formet Microsofts AI Red Team-program.

1. **Udvidet omfang af AI Red Teaming:**
   AI red teaming omfatter nu både sikkerheds- og ansvarlig AI (RAI) resultater

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå ved brugen af denne oversættelse.