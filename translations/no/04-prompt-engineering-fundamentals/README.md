<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b3cb38518cf4fe7714d2f5e74dfa3eb",
  "translation_date": "2025-10-03T09:41:08+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "no"
}
-->
# Grunnleggende om Prompt Engineering

[![Grunnleggende om Prompt Engineering](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.no.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Introduksjon
Denne modulen dekker essensielle konsepter og teknikker for å lage effektive prompts i generative AI-modeller. Måten du skriver din prompt til en LLM har stor betydning. En nøye utformet prompt kan gi bedre kvalitet på responsen. Men hva betyr egentlig begreper som _prompt_ og _prompt engineering_? Og hvordan kan jeg forbedre prompt _input_ som jeg sender til LLM? Dette er spørsmålene vi skal forsøke å besvare i dette kapittelet og det neste.

_Generativ AI_ er i stand til å skape nytt innhold (f.eks. tekst, bilder, lyd, kode osv.) som svar på brukerforespørsler. Den oppnår dette ved hjelp av _Large Language Models_ som OpenAIs GPT ("Generative Pre-trained Transformer")-serien, som er trent til å bruke naturlig språk og kode.

Brukere kan nå samhandle med disse modellene gjennom kjente paradigmer som chat, uten behov for teknisk ekspertise eller opplæring. Modellene er _prompt-baserte_ - brukere sender en tekstinput (prompt) og får tilbake AI-responsen (completion). De kan deretter "chatte med AI-en" iterativt, i samtaler med flere runder, og finjustere sin prompt til responsen samsvarer med forventningene.

"Prompts" blir nå det primære _programmeringsgrensesnittet_ for generative AI-applikasjoner, som forteller modellene hva de skal gjøre og påvirker kvaliteten på de returnerte svarene. "Prompt Engineering" er et raskt voksende fagfelt som fokuserer på _design og optimalisering_ av prompts for å levere konsistente og kvalitetsmessige svar i stor skala.

## Læringsmål

I denne leksjonen lærer vi hva Prompt Engineering er, hvorfor det er viktig, og hvordan vi kan lage mer effektive prompts for en gitt modell og applikasjonsmål. Vi vil forstå kjernebegreper og beste praksis for prompt engineering - og lære om et interaktivt Jupyter Notebooks "sandbox"-miljø hvor vi kan se disse konseptene anvendt på virkelige eksempler.

Ved slutten av denne leksjonen vil vi kunne:

1. Forklare hva prompt engineering er og hvorfor det er viktig.
2. Beskrive komponentene i en prompt og hvordan de brukes.
3. Lære beste praksis og teknikker for prompt engineering.
4. Anvende lærte teknikker på virkelige eksempler, ved bruk av en OpenAI-endepunkt.

## Viktige begreper

Prompt Engineering: Praksisen med å designe og finjustere inputs for å veilede AI-modeller mot å produsere ønskede outputs.  
Tokenisering: Prosessen med å konvertere tekst til mindre enheter, kalt tokens, som en modell kan forstå og prosessere.  
Instruksjons-tilpassede LLM-er: Store språkmodeller (LLMs) som har blitt finjustert med spesifikke instruksjoner for å forbedre nøyaktigheten og relevansen av svarene.

## Læringsmiljø

Prompt engineering er for øyeblikket mer kunst enn vitenskap. Den beste måten å forbedre vår intuisjon for det er å _øve mer_ og adoptere en prøving-og-feiling-tilnærming som kombinerer ekspertise innen applikasjonsdomener med anbefalte teknikker og modellspesifikke optimaliseringer.

Jupyter Notebook som følger med denne leksjonen gir et _sandbox_-miljø hvor du kan prøve ut det du lærer - enten underveis eller som en del av kodeutfordringen på slutten. For å utføre øvelsene, trenger du:

1. **En Azure OpenAI API-nøkkel** - tjenesteendepunktet for en distribuert LLM.  
2. **Et Python-runtime** - hvor Notebook kan kjøres.  
3. **Lokale miljøvariabler** - _fullfør [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst)-trinnene nå for å bli klar_.  

Notebooken kommer med _startøvelser_ - men du oppfordres til å legge til dine egne _Markdown_- (beskrivelse) og _Code_- (promptforespørsler) seksjoner for å prøve ut flere eksempler eller ideer - og bygge din intuisjon for promptdesign.

## Illustrert guide

Vil du få et overblikk over hva denne leksjonen dekker før du dykker inn? Sjekk ut denne illustrerte guiden, som gir deg en følelse av hovedtemaene som dekkes og de viktigste læringspunktene du bør tenke på i hver av dem. Leksjonsveikartet tar deg fra å forstå kjernebegreper og utfordringer til å adressere dem med relevante teknikker og beste praksis for prompt engineering. Merk at "Avanserte teknikker"-seksjonen i denne guiden refererer til innhold som dekkes i _neste_ kapittel av dette pensumet.

![Illustrert guide til Prompt Engineering](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.no.png)

## Vår oppstart

La oss nå snakke om hvordan _dette temaet_ relaterer seg til vår oppstartsoppdrag om å [bringe AI-innovasjon til utdanning](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi ønsker å bygge AI-drevne applikasjoner for _personlig læring_ - så la oss tenke på hvordan ulike brukere av vår applikasjon kan "designe" prompts:

- **Administratorer** kan be AI om å _analysere pensumdata for å identifisere mangler i dekningen_. AI kan oppsummere resultater eller visualisere dem med kode.  
- **Lærere** kan be AI om å _lage en leksjonsplan for en målgruppe og et emne_. AI kan bygge den personlige planen i et spesifisert format.  
- **Studenter** kan be AI om å _veilede dem i et vanskelig emne_. AI kan nå veilede studenter med leksjoner, hint og eksempler tilpasset deres nivå.  

Dette er bare toppen av isfjellet. Sjekk ut [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - et åpen kildekode-bibliotek med prompts kuratert av utdanningseksperter - for å få en bredere forståelse av mulighetene! _Prøv å kjøre noen av disse prompts i sandkassen eller ved bruk av OpenAI Playground for å se hva som skjer!_

<!--
LEKSJONSMAL:
Denne enheten bør dekke kjernebegrep #1.
Forsterk begrepet med eksempler og referanser.

KJERNEBEGREP #1:
Prompt Engineering.
Definer det og forklar hvorfor det er nødvendig.
-->

## Hva er Prompt Engineering?

Vi startet denne leksjonen med å definere **Prompt Engineering** som prosessen med å _designe og optimalisere_ tekstinputs (prompts) for å levere konsistente og kvalitetsmessige svar (completions) for et gitt applikasjonsmål og modell. Vi kan tenke på dette som en 2-trinns prosess:

- _designe_ den innledende prompten for en gitt modell og mål  
- _finjustere_ prompten iterativt for å forbedre kvaliteten på responsen  

Dette er nødvendigvis en prøving-og-feiling-prosess som krever brukerintuisjon og innsats for å oppnå optimale resultater. Så hvorfor er det viktig? For å svare på det spørsmålet, må vi først forstå tre konsepter:

- _Tokenisering_ = hvordan modellen "ser" prompten  
- _Base LLMs_ = hvordan grunnmodellen "prosesserer" en prompt  
- _Instruksjons-tilpassede LLMs_ = hvordan modellen nå kan se "oppgaver"  

### Tokenisering

En LLM ser prompts som en _sekvens av tokens_ der ulike modeller (eller versjoner av en modell) kan tokenisere den samme prompten på forskjellige måter. Siden LLM-er er trent på tokens (og ikke på rå tekst), har måten prompts blir tokenisert direkte innvirkning på kvaliteten på den genererte responsen.

For å få en intuisjon for hvordan tokenisering fungerer, prøv verktøy som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) vist nedenfor. Kopier inn din prompt - og se hvordan den blir konvertert til tokens, og legg merke til hvordan mellomrom og tegnsetting håndteres. Merk at dette eksemplet viser en eldre LLM (GPT-3) - så å prøve dette med en nyere modell kan gi et annet resultat.

![Tokenisering](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.no.png)

### Konsept: Grunnmodeller

Når en prompt er tokenisert, er den primære funksjonen til ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller grunnmodellen) å forutsi token i den sekvensen. Siden LLM-er er trent på massive tekstdatasett, har de en god forståelse av de statistiske relasjonene mellom tokens og kan gjøre den forutsigelsen med en viss grad av selvtillit. Merk at de ikke forstår _meningen_ med ordene i prompten eller token; de ser bare et mønster de kan "fullføre" med sin neste forutsigelse. De kan fortsette å forutsi sekvensen til de blir stoppet av brukerintervensjon eller en forhåndsdefinert betingelse.

Vil du se hvordan prompt-basert fullføring fungerer? Skriv inn den ovennevnte prompten i Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) med standardinnstillingene. Systemet er konfigurert til å behandle prompts som forespørsler om informasjon - så du bør se en fullføring som tilfredsstiller denne konteksten.

Men hva om brukeren ønsket å se noe spesifikt som oppfylte visse kriterier eller oppgaveformål? Det er her _instruksjons-tilpassede_ LLM-er kommer inn i bildet.

![Base LLM Chat Completion](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.no.png)

### Konsept: Instruksjons-tilpassede LLMs

En [Instruksjons-tilpasset LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) starter med grunnmodellen og finjusterer den med eksempler eller input/output-par (f.eks. meldinger med flere runder) som kan inneholde klare instruksjoner - og responsen fra AI forsøker å følge den instruksjonen.

Dette bruker teknikker som Reinforcement Learning with Human Feedback (RLHF) som kan trene modellen til å _følge instruksjoner_ og _lære av tilbakemeldinger_ slik at den produserer svar som er bedre egnet til praktiske applikasjoner og mer relevante for brukerens mål.

La oss prøve det - gå tilbake til den ovennevnte prompten, men endre nå _systemmeldingen_ for å gi følgende instruksjon som kontekst:

> _Oppsummer innholdet du får for en andreklassing. Hold resultatet til ett avsnitt med 3-5 punktlister._

Se hvordan resultatet nå er tilpasset for å reflektere det ønskede målet og formatet? En lærer kan nå direkte bruke denne responsen i sine lysbilder for den klassen.

![Instruksjons-tilpasset LLM Chat Completion](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.no.png)

## Hvorfor trenger vi Prompt Engineering?

Nå som vi vet hvordan prompts behandles av LLM-er, la oss snakke om _hvorfor_ vi trenger prompt engineering. Svaret ligger i det faktum at nåværende LLM-er har en rekke utfordringer som gjør _pålitelig og konsistent fullføring_ mer utfordrende å oppnå uten å legge innsats i utformingen og optimaliseringen av prompts. For eksempel:

1. **Modellresponser er stokastiske.** Den _samme prompten_ vil sannsynligvis produsere forskjellige svar med forskjellige modeller eller modellversjoner. Og den kan til og med produsere forskjellige resultater med _samme modell_ på forskjellige tidspunkter. _Prompt engineering-teknikker kan hjelpe oss med å minimere disse variasjonene ved å gi bedre retningslinjer_.  

1. **Modeller kan fabrikere svar.** Modeller er forhåndstrent med _store, men begrensede_ datasett, noe som betyr at de mangler kunnskap om konsepter utenfor det treningsområdet. Som et resultat kan de produsere fullføringer som er unøyaktige, oppdiktede eller direkte motstridende med kjente fakta. _Prompt engineering-teknikker hjelper brukere med å identifisere og redusere slike fabrikasjoner, f.eks. ved å be AI om sitater eller resonnement_.  

1. **Modellers evner vil variere.** Nyere modeller eller modellgenerasjoner vil ha rikere evner, men også bringe unike særegenheter og avveininger i kostnad og kompleksitet. _Prompt engineering kan hjelpe oss med å utvikle beste praksis og arbeidsflyter som abstraherer bort forskjeller og tilpasser seg modellspesifikke krav på skalerbare, sømløse måter_.  

La oss se dette i aksjon i OpenAI eller Azure OpenAI Playground:

- Bruk den samme prompten med forskjellige LLM-distribusjoner (f.eks. OpenAI, Azure OpenAI, Hugging Face) - så du variasjonene?  
- Bruk den samme prompten gjentatte ganger med den _samme_ LLM-distribusjonen (f.eks. Azure OpenAI Playground) - hvordan skilte disse variasjonene seg?  

### Eksempel på fabrikasjoner

I dette kurset bruker vi begrepet **"fabrikasjon"** for å referere til fenomenet der LLM-er noen ganger genererer faktuelt feil informasjon på grunn av begrensninger i treningen eller andre faktorer. Du har kanskje også hørt dette omtalt som _"hallusinasjoner"_ i populære artikler eller forskningsartikler. Vi anbefaler imidlertid sterkt å bruke _"fabrikasjon"_ som begrep slik at vi ikke utilsiktet tillegger en menneskelignende egenskap til et maskindrevet resultat. Dette forsterker også [Retningslinjer for ansvarlig AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) fra et terminologiperspektiv, ved å fjerne begreper som kan anses som støtende eller ikke-inkluderende i visse kontekster.

Vil du få en følelse av hvordan fabrikasjoner fungerer? Tenk på en prompt som instruerer AI til å generere innhold for et ikke-eksisterende tema (for å sikre at det ikke finnes i treningsdatasettet). For eksempel - jeg prøvde denne prompten:

> **Prompt:** lag en leksjonsplan om den marsianske krigen i 2076.  
Et nettsøk viste at det finnes fiktive beretninger (f.eks. TV-serier eller bøker) om kriger på Mars – men ingen fra 2076. Sunn fornuft forteller oss også at 2076 er _i fremtiden_ og derfor ikke kan knyttes til en virkelig hendelse.

Så hva skjer når vi tester denne prompten med ulike LLM-leverandører?

> **Respons 1**: OpenAI Playground (GPT-35)

![Respons 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.no.png)

> **Respons 2**: Azure OpenAI Playground (GPT-35)

![Respons 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.no.png)

> **Respons 3**: Hugging Face Chat Playground (LLama-2)

![Respons 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.no.png)

Som forventet gir hver modell (eller modellversjon) litt forskjellige svar, takket være stokastisk oppførsel og variasjoner i modellens evner. For eksempel retter én modell seg mot et publikum på 8. klassetrinn, mens en annen antar en videregående elev. Men alle tre modellene genererte svar som kunne overbevise en uinformert bruker om at hendelsen var ekte.

Teknikker for promptutforming, som _metaprompting_ og _konfigurasjon av temperatur_, kan redusere modellens fabrikasjoner til en viss grad. Nye arkitekturer for promptutforming integrerer også nye verktøy og teknikker sømløst i promptflyten for å dempe eller redusere noen av disse effektene.

## Case Study: GitHub Copilot

La oss avslutte denne delen med å få en forståelse av hvordan promptutforming brukes i virkelige løsninger ved å se på en case study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot er din "AI-parprogrammerer" – den konverterer tekstprompter til kodeforslag og er integrert i ditt utviklingsmiljø (f.eks. Visual Studio Code) for en sømløs brukeropplevelse. Som dokumentert i serien av blogger nedenfor, var den tidligste versjonen basert på OpenAI Codex-modellen – med ingeniører som raskt innså behovet for å finjustere modellen og utvikle bedre teknikker for promptutforming for å forbedre kodekvaliteten. I juli [lanserte de en forbedret AI-modell som går utover Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for enda raskere forslag.

Les innleggene i rekkefølge for å følge deres læringsreise.

- **Mai 2023** | [GitHub Copilot blir bedre til å forstå koden din](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [Inne i GitHub: Arbeid med LLM-ene bak GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juni 2023** | [Hvordan skrive bedre promter for GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juli 2023** | [.. GitHub Copilot går utover Codex med forbedret AI-modell](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Juli 2023** | [En utviklers guide til promptutforming og LLM-er](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **September 2023** | [Hvordan bygge en bedrifts-LLM-app: Lærdom fra GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Du kan også bla gjennom deres [ingeniørblogg](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for flere innlegg som [dette](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) som viser hvordan disse modellene og teknikkene _brukes_ for å drive virkelige applikasjoner.

---

## Promptkonstruksjon

Vi har sett hvorfor promptutforming er viktig – nå skal vi forstå hvordan promter _konstrueres_ slik at vi kan evaluere ulike teknikker for mer effektiv utforming av promter.

### Grunnleggende prompt

La oss starte med den grunnleggende prompten: en tekstinput sendt til modellen uten annen kontekst. Her er et eksempel – når vi sender de første ordene av den amerikanske nasjonalsangen til OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), fullfører den umiddelbart responsen med de neste linjene, som illustrerer den grunnleggende prediksjonsatferden.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Det høres ut som du starter teksten til "The Star-Spangled Banner," USAs nasjonalsang. Den fullstendige teksten er ...                     |

### Kompleks prompt

Nå legger vi til kontekst og instruksjoner til den grunnleggende prompten. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) lar oss konstruere en kompleks prompt som en samling av _meldinger_ med:

- Input/output-par som reflekterer _brukerens_ input og _assistentens_ respons.
- Systemmelding som setter konteksten for assistentens oppførsel eller personlighet.

Forespørselen er nå i formen nedenfor, hvor _tokeniseringen_ effektivt fanger relevant informasjon fra kontekst og samtale. Nå kan endring av systemkonteksten ha like stor innvirkning på kvaliteten på responsene som brukerens input.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```


### Instruksjonsprompt

I eksemplene ovenfor var brukerens prompt en enkel tekstforespørsel som kan tolkes som en informasjonsforespørsel. Med _instruksjonspromter_ kan vi bruke teksten til å spesifisere en oppgave mer detaljert, og gi bedre veiledning til AI-en. Her er et eksempel:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Instruksjonstype    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Skriv en beskrivelse av den amerikanske borgerkrigen                                                                                                                                                                                   | _returnerte et enkelt avsnitt_                                                                                            | Enkel               |
| Skriv en beskrivelse av den amerikanske borgerkrigen. Oppgi viktige datoer og hendelser og beskriv deres betydning                                                                                                                      | _returnerte et avsnitt etterfulgt av en liste over viktige datoer med beskrivelser_                                       | Kompleks            |
| Skriv en beskrivelse av den amerikanske borgerkrigen i ett avsnitt. Oppgi 3 punktlister med viktige datoer og deres betydning. Oppgi 3 flere punktlister med viktige historiske personer og deres bidrag. Returner output som en JSON-fil | _returnerte mer omfattende detaljer i en tekstboks, formatert som JSON som du kan kopiere og validere etter behov_         | Kompleks. Formatert |

## Primærinnhold

I eksemplene ovenfor var prompten fortsatt ganske åpen, og lot LLM-en avgjøre hvilken del av dens forhåndstrente datasett som var relevant. Med designmønsteret _primærinnhold_ deles inputteksten i to deler:

- en instruksjon (handling)
- relevant innhold (som påvirker handlingen)

Her er et eksempel der instruksjonen er "oppsummer dette i 2 setninger".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter er den femte planeten fra solen og den største i solsystemet. Den er en gassgigant med en masse som er en tusendel av solens, men to og en halv gang så stor som alle de andre planetene i solsystemet til sammen. Jupiter er et av de lyseste objektene som er synlige for det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før historien ble nedskrevet. Den er oppkalt etter den romerske guden Jupiter. Når den ses fra jorden, kan Jupiter være lys nok til at det reflekterte lyset kaster synlige skygger, og er i gjennomsnitt det tredje lyseste naturlige objektet på nattehimmelen etter månen og Venus. <br/> **Oppsummer dette i 2 korte setninger** | Jupiter, den femte planeten fra solen, er den største i solsystemet og kjent for å være et av de lyseste objektene på nattehimmelen. Oppkalt etter den romerske guden Jupiter, er det en gassgigant med en masse som er to og en halv gang så stor som alle de andre planetene til sammen. |

Segmentet med primærinnhold kan brukes på ulike måter for å drive mer effektive instruksjoner:

- **Eksempler** – i stedet for å fortelle modellen hva den skal gjøre med en eksplisitt instruksjon, gi den eksempler på hva den skal gjøre og la den utlede mønsteret.
- **Hint** – følg instruksjonen med et "hint" som gir modellen en retning, og guider den mot mer relevante svar.
- **Maler** – dette er repeterbare "oppskrifter" for promter med plassholdere (variabler) som kan tilpasses med data for spesifikke bruksområder.

La oss utforske disse i praksis.

### Bruk av eksempler

Dette er en tilnærming der du bruker primærinnholdet til å "mate modellen" med noen eksempler på ønsket output for en gitt instruksjon, og lar den utlede mønsteret for ønsket output. Basert på antall eksempler som gis, kan vi ha zero-shot prompting, one-shot prompting, few-shot prompting osv.

Prompten består nå av tre komponenter:

- En oppgavebeskrivelse
- Noen eksempler på ønsket output
- Starten på et nytt eksempel (som blir en implisitt oppgavebeskrivelse)

| Læringstype | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot   | "Solen skinner". Oversett til spansk                                                                                                                  | "El Sol está brillando".    |
| One-shot    | "Solen skinner" => ""El Sol está brillando". <br> "Det er en kald og vindfull dag" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot    | Spilleren løp basene => Baseball <br/> Spilleren slo en ess => Tennis <br/> Spilleren slo en sekser => Cricket <br/> Spilleren gjorde en slam-dunk => | Basketball                  |
|             |                                                                                                                                                       |                             |

Legg merke til hvordan vi måtte gi eksplisitt instruksjon ("Oversett til spansk") i zero-shot prompting, men det blir utledet i one-shot prompting-eksemplet. Few-shot-eksemplet viser hvordan flere eksempler gir modellen mulighet til å gjøre mer nøyaktige utledninger uten ekstra instruksjoner.

### Prompt-hint

En annen teknikk for bruk av primærinnhold er å gi _hint_ i stedet for eksempler. I dette tilfellet gir vi modellen et dytt i riktig retning ved å _starte den_ med et utdrag som reflekterer ønsket responsformat. Modellen "tar hintet" og fortsetter i samme stil.

| Antall hint | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0           | Jupiter er den femte planeten fra solen og den største i solsystemet. Den er en gassgigant med en masse som er en tusendel av solens, men to og en halv gang så stor som alle de andre planetene i solsystemet til sammen. Jupiter er et av de lyseste objektene som er synlige for det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før historien ble nedskrevet. <br/>**Oppsummer dette**                                       | Jupiter er den største planeten i solsystemet og den femte fra solen. Den er en gassgigant med en masse som er 1/1000 av solens, men tyngre enn alle de andre planetene til sammen. Gamle sivilisasjoner har kjent til Jupiter lenge, og den er lett synlig på nattehimmelen. |
| 1              | Jupiter er den femte planeten fra solen og den største i solsystemet. Det er en gasskjempe med en masse som er en tusendel av solens, men to og en halv ganger massen av alle de andre planetene i solsystemet til sammen. Jupiter er et av de lyseste objektene som er synlige for det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før historien ble nedskrevet. <br/>**Oppsummer dette** <br/> Det vi lærte er at Jupiter | er den femte planeten fra solen og den største i solsystemet. Det er en gasskjempe med en masse som er en tusendel av solens, men to og en halv ganger massen av alle de andre planetene til sammen. Den er lett synlig for det blotte øye og har vært kjent siden antikken.                        |
| 2              | Jupiter er den femte planeten fra solen og den største i solsystemet. Det er en gasskjempe med en masse som er en tusendel av solens, men to og en halv ganger massen av alle de andre planetene i solsystemet til sammen. Jupiter er et av de lyseste objektene som er synlige for det blotte øye på nattehimmelen, og har vært kjent for gamle sivilisasjoner siden før historien ble nedskrevet. <br/>**Oppsummer dette** <br/> Topp 3 fakta vi lærte:         | 1. Jupiter er den femte planeten fra solen og den største i solsystemet. <br/> 2. Det er en gasskjempe med en masse som er en tusendel av solens...<br/> 3. Jupiter har vært synlig for det blotte øye siden antikken ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Maler for oppgaver

En oppgavemal er en _forhåndsdefinert oppskrift for en oppgave_ som kan lagres og brukes på nytt etter behov, for å sikre mer konsistente brukeropplevelser i stor skala. I sin enkleste form er det bare en samling av oppgaveeksempler som [dette fra OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) som gir både interaktive oppgavekomponenter (bruker- og systemmeldinger) og API-drevet forespørselsformat - for å støtte gjenbruk.

I sin mer komplekse form, som [dette eksemplet fra LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), inneholder den _plassholdere_ som kan erstattes med data fra ulike kilder (brukerinndata, systemkontekst, eksterne datakilder osv.) for å generere en oppgave dynamisk. Dette lar oss lage et bibliotek med gjenbrukbare oppgaver som kan brukes til å sikre konsistente brukeropplevelser **programmatisk** i stor skala.

Til slutt ligger den virkelige verdien av maler i evnen til å lage og publisere _oppgavebiblioteker_ for vertikale applikasjonsdomener - der oppgavemalen nå er _optimalisert_ for å reflektere applikasjonsspesifikke kontekster eller eksempler som gjør svarene mer relevante og nøyaktige for den målrettede brukergruppen. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst)-repoet er et godt eksempel på denne tilnærmingen, som kuraterer et bibliotek med oppgaver for utdanningssektoren med vekt på nøkkelmål som leksjonsplanlegging, læreplanutforming, studentveiledning osv.

## Støttende innhold

Hvis vi tenker på oppgavekonstruksjon som å ha en instruksjon (oppgave) og et mål (primært innhold), så er _sekundært innhold_ som ekstra kontekst vi gir for å **påvirke resultatet på en eller annen måte**. Det kan være justeringsparametere, formateringsinstruksjoner, emnetaksonomier osv. som kan hjelpe modellen med å _tilpasse_ svaret til å passe de ønskede brukerbehovene eller forventningene.

For eksempel: Gitt en kurskatalog med omfattende metadata (navn, beskrivelse, nivå, metadatakoder, instruktør osv.) om alle tilgjengelige kurs i læreplanen:

- vi kan definere en instruksjon for å "oppsummere kurskatalogen for høsten 2023"
- vi kan bruke det primære innholdet til å gi noen eksempler på ønsket resultat
- vi kan bruke det sekundære innholdet til å identifisere de 5 viktigste "kodene" av interesse.

Nå kan modellen gi en oppsummering i formatet vist av de få eksemplene - men hvis et resultat har flere koder, kan den prioritere de 5 kodene identifisert i det sekundære innholdet.

---

<!--
LEKSJONSMAL:
Denne enheten bør dekke kjernekonsept #1.
Forsterk konseptet med eksempler og referanser.

KONSEPT #3:
Teknikker for oppgaveutforming.
Hva er noen grunnleggende teknikker for oppgaveutforming?
Illustrer det med noen øvelser.
-->

## Beste praksis for oppgaveutforming

Nå som vi vet hvordan oppgaver kan _konstrueres_, kan vi begynne å tenke på hvordan vi kan _designe_ dem for å reflektere beste praksis. Vi kan tenke på dette i to deler - å ha riktig _tankesett_ og bruke riktige _teknikker_.

### Tankesett for oppgaveutforming

Oppgaveutforming er en prøving-og-feiling-prosess, så husk tre brede retningslinjer:

1. **Forståelse av domenet er viktig.** Svarets nøyaktighet og relevans er en funksjon av _domenet_ der applikasjonen eller brukeren opererer. Bruk din intuisjon og domenekunnskap til å **tilpasse teknikker** ytterligere. For eksempel, definer _domenespesifikke personligheter_ i systemoppgavene dine, eller bruk _domenespesifikke maler_ i brukeroppgavene dine. Gi sekundært innhold som reflekterer domenespesifikke kontekster, eller bruk _domenespesifikke ledetråder og eksempler_ for å veilede modellen mot kjente bruksmønstre.

2. **Forståelse av modellen er viktig.** Vi vet at modeller er stokastiske av natur. Men modellimplementeringer kan også variere når det gjelder treningsdatasettet de bruker (forhåndstrent kunnskap), funksjonene de gir (f.eks. via API eller SDK) og typen innhold de er optimalisert for (f.eks. kode vs. bilder vs. tekst). Forstå styrkene og begrensningene til modellen du bruker, og bruk den kunnskapen til å _prioritere oppgaver_ eller bygge _tilpassede maler_ som er optimalisert for modellens funksjoner.

3. **Iterasjon og validering er viktig.** Modeller utvikler seg raskt, og det gjør også teknikkene for oppgaveutforming. Som domenekspert kan du ha annen kontekst eller kriterier for _din_ spesifikke applikasjon, som kanskje ikke gjelder for det bredere samfunnet. Bruk verktøy og teknikker for oppgaveutforming for å "komme i gang" med oppgavekonstruksjon, og iterer og valider resultatene ved hjelp av din egen intuisjon og domenekunnskap. Registrer innsiktene dine og opprett en **kunnskapsbase** (f.eks. oppgavebiblioteker) som kan brukes som en ny baseline av andre, for raskere iterasjoner i fremtiden.

## Beste praksis

La oss nå se på vanlige beste praksiser som anbefales av [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) og [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst)-praktikere.

| Hva                               | Hvorfor                                                                                                                                                                                                                                               |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluer de nyeste modellene.      | Nye modellgenerasjoner har sannsynligvis forbedrede funksjoner og kvalitet - men kan også medføre høyere kostnader. Evaluer dem for innvirkning, og ta deretter migreringsbeslutninger.                                                               |
| Skill instruksjoner og kontekst   | Sjekk om modellen/leverandøren din definerer _avgrensere_ for å skille instruksjoner, primært og sekundært innhold tydeligere. Dette kan hjelpe modeller med å tildele vekter mer nøyaktig til tokens.                                                  |
| Vær spesifikk og tydelig          | Gi flere detaljer om ønsket kontekst, resultat, lengde, format, stil osv. Dette vil forbedre både kvaliteten og konsistensen i svarene. Fang oppskrifter i gjenbrukbare maler.                                                                         |
| Vær beskrivende, bruk eksempler   | Modeller kan respondere bedre på en "vis og fortell"-tilnærming. Start med en `zero-shot`-tilnærming der du gir en instruksjon (men ingen eksempler), og prøv deretter `few-shot` som en forbedring, ved å gi noen eksempler på ønsket resultat. Bruk analogier. |
| Bruk ledetråder for å starte svar | Gi det noen ledende ord eller fraser som det kan bruke som utgangspunkt for svaret, for å styre det mot et ønsket resultat.                                                                                                                           |
| Gjenta                           | Noen ganger kan det være nødvendig å gjenta seg selv til modellen. Gi instruksjoner før og etter ditt primære innhold, bruk en instruksjon og en ledetråd osv. Iterer og valider for å se hva som fungerer.                                              |
| Rekkefølge betyr noe              | Rekkefølgen du presenterer informasjon til modellen i, kan påvirke resultatet, selv i læringseksemplene, takket være nylighetsskjevhet. Prøv forskjellige alternativer for å se hva som fungerer best.                                                  |
| Gi modellen en "utvei"            | Gi modellen et _fallback_-svar den kan gi hvis den ikke kan fullføre oppgaven av en eller annen grunn. Dette kan redusere sjansen for at modellen genererer falske eller oppdiktede svar.                                                              |
|                                   |                                                                                                                                                                                                                                                       |

Som med enhver beste praksis, husk at _resultatene kan variere_ avhengig av modellen, oppgaven og domenet. Bruk disse som et utgangspunkt, og iterer for å finne hva som fungerer best for deg. Evaluer kontinuerlig prosessen for oppgaveutforming etter hvert som nye modeller og verktøy blir tilgjengelige, med fokus på prosessskalerbarhet og svarkvalitet.

<!--
LEKSJONSMAL:
Denne enheten bør gi en kodeutfordring hvis aktuelt

UTFORDRING:
Lenke til en Jupyter Notebook med kun kodekommentarer i instruksjonene (kodeseksjonene er tomme).

LØSNING:
Lenke til en kopi av den Notebook med oppgavene fylt ut og kjørt, som viser hva ett eksempel kan være.
-->

## Oppgave

Gratulerer! Du har kommet til slutten av leksjonen! Det er på tide å teste noen av disse konseptene og teknikkene med ekte eksempler!

For oppgaven vår skal vi bruke en Jupyter Notebook med øvelser du kan fullføre interaktivt. Du kan også utvide Notebook med dine egne Markdown- og kodeceller for å utforske ideer og teknikker på egen hånd.

### For å komme i gang, fork repoet, deretter

- (Anbefalt) Start GitHub Codespaces
- (Alternativt) Klon repoet til din lokale enhet og bruk det med Docker Desktop
- (Alternativt) Åpne Notebook med ditt foretrukne Notebook-runtime-miljø.

### Deretter, konfigurer miljøvariablene dine

- Kopier `.env.copy`-filen i repo-roten til `.env` og fyll inn verdiene for `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` og `AZURE_OPENAI_DEPLOYMENT`. Kom tilbake til [Learning Sandbox-seksjonen](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) for å lære hvordan.

### Deretter, åpne Jupyter Notebook

- Velg runtime-kjernen. Hvis du bruker alternativ 1 eller 2, velg bare standard Python 3.10.x-kjernen som tilbys av utviklingscontaineren.

Du er klar til å kjøre øvelsene. Merk at det ikke finnes _riktige eller gale_ svar her - bare utforsking av alternativer gjennom prøving-og-feiling og bygging av intuisjon for hva som fungerer for en gitt modell og applikasjonsdomene.

_Av denne grunn er det ingen kode-løsningssegmenter i denne leksjonen. I stedet vil Notebook ha Markdown-celler med tittelen "Min løsning:" som viser ett eksempel på resultat for referanse._

 <!--
LEKSJONSMAL:
Avslutt seksjonen med en oppsummering og ressurser for selvstyrt læring.
-->

## Kunnskapssjekk

Hvilken av følgende er en god oppgave som følger noen rimelige beste praksiser?

1. Vis meg et bilde av en rød bil
2. Vis meg et bilde av en rød bil av merke Volvo og modell XC90 parkert ved en klippe med solnedgang
3. Vis meg et bilde av en rød bil av merke Volvo og modell XC90

A: 2, det er den beste oppgaven da den gir detaljer om "hva" og går inn i spesifikasjoner (ikke bare en bil, men et spesifikt merke og modell), og den beskriver også den generelle settingen. 3 er nest best da den også inneholder mye beskrivelse.

## 🚀 Utfordring

Se om du kan bruke "ledetråd"-teknikken med oppgaven: Fullfør setningen "Vis meg et bilde av en rød bil av merke Volvo og ". Hva svarer den med, og hvordan ville du forbedret det?

## Flott arbeid! Fortsett læringen din

Vil du lære mer om ulike konsepter innen oppgaveutforming? Gå til [siden for videre læring](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å finne andre flotte ressurser om dette emnet.

Gå videre til leksjon 5 der vi skal se på [avanserte oppgaveteknikker](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.