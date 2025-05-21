<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:22:57+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "da"
}
-->
# Introduktion til Generativ AI og Store Sproglige Modeller

_(Klik på billedet ovenfor for at se videoen af denne lektion)_

Generativ AI er kunstig intelligens, der kan generere tekst, billeder og andre typer indhold. Det, der gør det til en fantastisk teknologi, er, at det demokratiserer AI; alle kan bruge det med blot en tekstprompt, en sætning skrevet på et naturligt sprog. Du behøver ikke at lære et sprog som Java eller SQL for at opnå noget værdifuldt, alt du behøver er at bruge dit sprog, angive hvad du vil, og så kommer der et forslag fra en AI-model. Anvendelserne og indflydelsen af dette er enorme, du kan skrive eller forstå rapporter, skrive applikationer og meget mere, alt sammen på få sekunder.

I denne læseplan vil vi udforske, hvordan vores startup udnytter generativ AI til at åbne op for nye scenarier i uddannelsesverdenen, og hvordan vi håndterer de uundgåelige udfordringer, der er forbundet med de sociale implikationer af dens anvendelse og teknologiens begrænsninger.

## Introduktion

Denne lektion vil dække:

- Introduktion til forretningsscenariet: vores startup-idé og mission.
- Generativ AI og hvordan vi landede på det nuværende teknologilandskab.
- Den indre virkemåde af en stor sproglig model.
- Hovedfunktionerne og praktiske anvendelsestilfælde af Store Sproglige Modeller.

## Læringsmål

Efter at have gennemført denne lektion, vil du forstå:

- Hvad generativ AI er, og hvordan Store Sproglige Modeller fungerer.
- Hvordan du kan udnytte store sproglige modeller til forskellige anvendelsestilfælde med fokus på uddannelsesscenarier.

## Scenario: vores uddannelses-startup

Generativ Kunstig Intelligens (AI) repræsenterer toppen af AI-teknologi og skubber grænserne for, hvad der engang blev anset for umuligt. Generative AI-modeller har flere kapaciteter og anvendelser, men for denne læseplan vil vi udforske, hvordan det revolutionerer uddannelse gennem en fiktiv startup. Vi vil henvise til denne startup som _vores startup_. Vores startup arbejder inden for uddannelsesområdet med den ambitiøse mission

> _at forbedre tilgængeligheden i læring på globalt plan, sikre lige adgang til uddannelse og give personlige læringsoplevelser til hver enkelt elev, i henhold til deres behov_.

Vores startupteam er klar over, at vi ikke vil kunne nå dette mål uden at udnytte et af de mest kraftfulde værktøjer i moderne tid – Store Sproglige Modeller (LLMs).

Generativ AI forventes at revolutionere den måde, vi lærer og underviser på i dag, med elever, der har virtuelle lærere til rådighed 24 timer i døgnet, som leverer store mængder information og eksempler, og lærere, der kan udnytte innovative værktøjer til at vurdere deres elever og give feedback.

For at starte, lad os definere nogle grundlæggende begreber og terminologi, vi vil bruge gennem hele læseplanen.

## Hvordan fik vi Generativ AI?

På trods af den ekstraordinære _hype_, der er skabt for nylig ved annonceringen af generative AI-modeller, har denne teknologi været årtier undervejs, med de første forskningsindsatser, der går tilbage til 60'erne. Vi er nu på et punkt, hvor AI har menneskelige kognitive evner, som samtale, som vist for eksempel ved [OpenAI ChatGPT](https://openai.com/chatgpt) eller [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), der også bruger en GPT-model til websøgnings-Bing-samtaler.

Når vi går lidt tilbage, bestod de allerførste prototyper af AI af maskinskrevne chatbots, der stolede på en vidensbase udtrukket fra en gruppe eksperter og repræsenteret i en computer. Svarene i vidensbasen blev udløst af nøgleord, der optrådte i inputteksten. Det blev dog hurtigt klart, at en sådan tilgang, ved brug af maskinskrevne chatbots, ikke skalerede godt.

### En statistisk tilgang til AI: Maskinlæring

Et vendepunkt kom i 90'erne med anvendelsen af en statistisk tilgang til tekstanalyse. Dette førte til udviklingen af nye algoritmer – kendt som maskinlæring – i stand til at lære mønstre fra data uden at være eksplicit programmeret. Denne tilgang gør det muligt for maskiner at simulere menneskelig sprogforståelse: en statistisk model trænes på tekst-etiket-par, hvilket gør det muligt for modellen at klassificere ukendt inputtekst med en foruddefineret etiket, der repræsenterer intentionen med beskeden.

### Neurale netværk og moderne virtuelle assistenter

I de senere år har den teknologiske udvikling af hardware, i stand til at håndtere større datamængder og mere komplekse beregninger, opmuntret forskning i AI, hvilket har ført til udviklingen af avancerede maskinlæringsalgoritmer kendt som neurale netværk eller dyb læring algoritmer.

Neurale netværk (og især Recurrent Neural Networks – RNNs) har væsentligt forbedret naturlig sprogbehandling, hvilket gør det muligt at repræsentere betydningen af tekst på en mere meningsfuld måde, ved at værdsætte konteksten af et ord i en sætning.

Dette er teknologien, der drev de virtuelle assistenter, der blev født i det første årti af det nye århundrede, meget dygtige til at fortolke menneskeligt sprog, identificere et behov og udføre en handling for at opfylde det – som at svare med et foruddefineret manuskript eller forbruge en tredjepartstjeneste.

### Nutid, Generativ AI

Sådan kom vi til Generativ AI i dag, som kan ses som en undergruppe af dyb læring.

Efter årtiers forskning inden for AI-feltet, overvandt en ny modelarkitektur – kaldet _Transformer_ – begrænsningerne ved RNNs, idet den kunne modtage meget længere tekstsekvenser som input. Transformers er baseret på opmærksomhedsmekanismen, hvilket gør det muligt for modellen at give forskellige vægte til de input, den modtager, 'at være mere opmærksom' der, hvor den mest relevante information er koncentreret, uanset deres rækkefølge i tekstsekvensen.

De fleste af de nylige generative AI-modeller – også kendt som Store Sproglige Modeller (LLMs), da de arbejder med tekstlige input og output – er faktisk baseret på denne arkitektur. Det interessante ved disse modeller – trænet på en enorm mængde uetiketterede data fra forskellige kilder som bøger, artikler og websites – er, at de kan tilpasses til en bred vifte af opgaver og generere grammatisk korrekt tekst med en antydning af kreativitet. Så ikke alene har de utroligt forbedret maskinens evne til at 'forstå' en inputtekst, men de har også gjort det muligt for dem at generere et originalt svar på menneskesprog.

## Hvordan fungerer store sproglige modeller?

I det næste kapitel vil vi udforske forskellige typer af Generative AI-modeller, men for nu lad os se på, hvordan store sproglige modeller fungerer, med fokus på OpenAI GPT (Generative Pre-trained Transformer) modeller.

- **Tokenizer, tekst til tal**: Store Sproglige Modeller modtager en tekst som input og genererer en tekst som output. Men da de er statistiske modeller, fungerer de meget bedre med tal end tekstsekvenser. Derfor bliver hvert input til modellen behandlet af en tokenizer, før det bruges af kernemodellen. En token er et stykke tekst – bestående af et variabelt antal tegn, så tokenizerens hovedopgave er at opdele inputtet i en række tokens. Derefter bliver hver token kortlagt med en token-indeks, som er den heltalskodning af det oprindelige tekststykke.

- **Forudsigelse af outputtokens**: Givet n tokens som input (med max n varierende fra model til model), er modellen i stand til at forudsige en token som output. Denne token inkorporeres derefter i inputtet til næste iteration, i et udvidende vinduesmønster, hvilket muliggør en bedre brugeroplevelse ved at få en (eller flere) sætning som svar. Dette forklarer, hvorfor, hvis du nogensinde har leget med ChatGPT, du måske har bemærket, at det nogle gange ser ud som om, det stopper midt i en sætning.

- **Udvælgelsesproces, sandsynlighedsfordeling**: Outputtokenen vælges af modellen i henhold til dens sandsynlighed for at forekomme efter den aktuelle tekstsekvens. Dette skyldes, at modellen forudsiger en sandsynlighedsfordeling over alle mulige 'næste tokens', beregnet baseret på dens træning. Men det er ikke altid den token med den højeste sandsynlighed, der vælges fra den resulterende fordeling. En grad af tilfældighed tilføjes til dette valg, på en måde at modellen opfører sig på en ikke-deterministisk måde - vi får ikke den nøjagtige samme output for det samme input. Denne grad af tilfældighed tilføjes for at simulere processen med kreativ tænkning, og det kan justeres ved hjælp af en modelparameter kaldet temperatur.

## Hvordan kan vores startup udnytte Store Sproglige Modeller?

Nu hvor vi har en bedre forståelse af den indre virkemåde af en stor sproglig model, lad os se nogle praktiske eksempler på de mest almindelige opgaver, de kan udføre ret godt, med øje for vores forretningsscenarie. Vi sagde, at den vigtigste kapacitet af en Stor Sproglig Model er _at generere en tekst fra bunden, startende fra en tekstlig input, skrevet på naturligt sprog_.

Men hvilken slags tekstlig input og output?
Inputtet af en stor sproglig model er kendt som en prompt, mens outputtet er kendt som en completion, et begreb, der henviser til modelmekanismen for at generere den næste token for at fuldføre det aktuelle input. Vi vil dykke dybt ned i, hvad en prompt er, og hvordan man designer den på en måde for at få mest muligt ud af vores model. Men for nu lad os bare sige, at en prompt kan inkludere:

- En **instruktion**, der specificerer den type output, vi forventer fra modellen. Denne instruktion kan nogle gange indeholde nogle eksempler eller nogle yderligere data.

  1. Opsummering af en artikel, bog, produktanmeldelser og mere, sammen med udtrækning af indsigter fra ustrukturerede data.
  
  2. Kreativ idéudvikling og design af en artikel, et essay, en opgave eller mere.

- Et **spørgsmål**, stillet i form af en samtale med en agent.

- Et stykke **tekst, der skal fuldføres**, som implicit er en anmodning om skriveassistance.

- Et stykke **kode** sammen med en anmodning om at forklare og dokumentere det, eller en kommentar, der beder om at generere et stykke kode, der udfører en specifik opgave.

Eksemplerne ovenfor er ret simple og er ikke beregnet til at være en udtømmende demonstration af Store Sproglige Modellers kapaciteter. De er ment til at vise potentialet ved at bruge generativ AI, især men ikke begrænset til uddannelseskontekster.

Desuden er outputtet af en generativ AI-model ikke perfekt, og nogle gange kan modellens kreativitet arbejde imod den, hvilket resulterer i et output, der er en kombination af ord, som den menneskelige bruger kan fortolke som en mystificering af virkeligheden, eller det kan være stødende. Generativ AI er ikke intelligent - i det mindste ikke i den mere omfattende definition af intelligens, der inkluderer kritisk og kreativ ræsonnering eller følelsesmæssig intelligens; den er ikke deterministisk, og den er ikke pålidelig, da fabrikationer, såsom fejlagtige referencer, indhold og udsagn, kan kombineres med korrekt information og præsenteres på en overbevisende og selvsikker måde. I de følgende lektioner vil vi beskæftige os med alle disse begrænsninger, og vi vil se, hvad vi kan gøre for at afbøde dem.

## Opgave

Din opgave er at læse mere om [generativ AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) og forsøge at identificere et område, hvor du ville tilføje generativ AI i dag, som ikke har det. Hvordan ville indvirkningen være forskellig fra at gøre det på den "gamle måde", kan du gøre noget, du ikke kunne før, eller er du hurtigere? Skriv en 300 ords opsummering om, hvordan din drømme-AI-startup ville se ud, og inkluder overskrifter som "Problem", "Hvordan jeg ville bruge AI", "Indvirkning" og eventuelt en forretningsplan.

Hvis du gjorde denne opgave, er du måske endda klar til at ansøge til Microsofts inkubator, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst), vi tilbyder kreditter til både Azure, OpenAI, mentoring og meget mere, tjek det ud!

## Videnscheck

Hvad er sandt om store sproglige modeller?

1. Du får den nøjagtige samme respons hver gang.
1. Den gør ting perfekt, er god til at lægge tal sammen, producere fungerende kode osv.
1. Responsen kan variere, selvom du bruger den samme prompt. Den er også god til at give dig et første udkast af noget, hvad enten det er tekst eller kode. Men du skal forbedre resultaterne.

A: 3, en LLM er ikke-deterministisk, responsen varierer, men du kan kontrollere dens variation via en temperaturindstilling. Du bør heller ikke forvente, at den gør tingene perfekt, den er her for at gøre det tunge arbejde for dig, hvilket ofte betyder, at du får et godt første forsøg på noget, som du gradvist skal forbedre.

## Godt arbejde! Fortsæt rejsen

Efter at have gennemført denne lektion, tjek vores [Generative AI Learning-samling](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at forbedre din viden om Generativ AI!

Gå videre til Lektion 2, hvor vi vil se på, hvordan man [udforsker og sammenligner forskellige LLM-typer](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.