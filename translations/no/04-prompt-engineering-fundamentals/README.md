<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T15:45:49+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "no"
}
-->
# Grunnleggende om prompt engineering

## Introduksjon
Denne modulen dekker essensielle konsepter og teknikker for å lage effektive spørsmål i generative AI-modeller. Måten du skriver spørsmålet til en LLM på, er også viktig. Et nøye utformet spørsmål kan gi bedre kvalitet på svaret. Men hva betyr egentlig begreper som _spørsmål_ og _prompt engineering_? Og hvordan kan jeg forbedre spørsmålsinnputten jeg sender til LLM-en? Dette er spørsmålene vi vil prøve å svare på i dette kapittelet og det neste.

_Generativ AI_ er i stand til å lage nytt innhold (f.eks. tekst, bilder, lyd, kode osv.) som svar på brukerforespørsler. Den oppnår dette ved å bruke _store språkmodeller_ som OpenAIs GPT ("Generative Pre-trained Transformer")-serien, som er trent for bruk av naturlig språk og kode.

Brukere kan nå samhandle med disse modellene ved hjelp av kjente paradigmer som chat, uten å trenge teknisk ekspertise eller opplæring. Modellene er _spørsmålsbaserte_ - brukere sender en tekstinnputt (spørsmål) og får AI-svaret (fullføring) tilbake. De kan deretter "chatte med AI-en" iterativt, i samtaler med flere omganger, for å finjustere spørsmålet til svaret matcher deres forventninger.

"Spørsmål" blir nå det primære _programmeringsgrensesnittet_ for generative AI-apper, som forteller modellene hva de skal gjøre og påvirker kvaliteten på de returnerte svarene. "Prompt Engineering" er et raskt voksende fagfelt som fokuserer på _design og optimalisering_ av spørsmål for å levere konsistente og kvalitetsrike svar i stor skala.

## Læringsmål

I denne leksjonen lærer vi hva Prompt Engineering er, hvorfor det er viktig, og hvordan vi kan lage mer effektive spørsmål for en gitt modell og applikasjonsmål. Vi vil forstå kjernekonsepter og beste praksis for prompt engineering - og lære om et interaktivt Jupyter Notebooks "sandbox"-miljø hvor vi kan se disse konseptene anvendt på ekte eksempler.

Ved slutten av denne leksjonen vil vi kunne:

1. Forklare hva prompt engineering er og hvorfor det er viktig.
2. Beskrive komponentene i et spørsmål og hvordan de brukes.
3. Lære beste praksis og teknikker for prompt engineering.
4. Anvende lærte teknikker på ekte eksempler, ved å bruke en OpenAI-endepunkt.

## Nøkkelbegreper

Prompt Engineering: Praksisen med å designe og raffinere innputt for å lede AI-modeller mot å produsere ønskede utganger.
Tokenisering: Prosessen med å konvertere tekst til mindre enheter, kalt tokens, som en modell kan forstå og prosessere.
Instruksjons-justerte LLM-er: Store språkmodeller (LLM-er) som har blitt finjustert med spesifikke instruksjoner for å forbedre deres svarnøyaktighet og relevans.

## Læringssandbox

Prompt engineering er for øyeblikket mer kunst enn vitenskap. Den beste måten å forbedre vår intuisjon for det er å _øve mer_ og ta i bruk en prøving-og-feiling-tilnærming som kombinerer applikasjonsdomeneekspertise med anbefalte teknikker og modellspecifikke optimaliseringer.

Jupyter Notebook som følger med denne leksjonen gir et _sandbox_-miljø hvor du kan prøve ut det du lærer - etter hvert som du går eller som en del av kodeutfordringen på slutten. For å utføre øvelsene, trenger du:

1. **En Azure OpenAI API-nøkkel** - tjenesteendepunktet for en distribuert LLM.
2. **En Python-runtime** - der Notebook kan kjøres.
3. **Lokale miljøvariabler** - _fullfør [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) trinnene nå for å bli klar_.

Notebooken kommer med _startøvelser_ - men du oppfordres til å legge til dine egne _Markdown_ (beskrivelse) og _kode_ (spørsmålsforespørsler) seksjoner for å prøve ut flere eksempler eller ideer - og bygge din intuisjon for spørsmålsdesign.

## Illustrert guide

Vil du få et helhetlig bilde av hva denne leksjonen dekker før du dykker inn? Sjekk ut denne illustrerte guiden, som gir deg en følelse av hovedtemaene som dekkes og de viktigste lærdommene du bør tenke på i hver av dem. Leksjonsveikartet tar deg fra å forstå kjernekonsepter og utfordringer til å adressere dem med relevante prompt engineering-teknikker og beste praksis. Merk at delen "Avanserte teknikker" i denne guiden refererer til innhold som dekkes i _neste_ kapittel av denne læreplanen.

## Vår oppstart

La oss nå snakke om hvordan _dette temaet_ relaterer seg til vår oppstartsoppdrag om å [bringe AI-innovasjon til utdanning](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vi ønsker å bygge AI-drevne applikasjoner for _personlig tilpasset læring_ - så la oss tenke på hvordan forskjellige brukere av vår applikasjon kan "designe" spørsmål:

- **Administratorer** kan be AI-en om å _analysere læreplan data for å identifisere hull i dekningen_. AI-en kan oppsummere resultater eller visualisere dem med kode.
- **Lærere** kan be AI-en om å _generere en leksjonsplan for en målgruppe og et emne_. AI-en kan bygge den personlig tilpassede planen i et spesifisert format.
- **Studenter** kan be AI-en om å _veilede dem i et vanskelig emne_. AI-en kan nå veilede studentene med leksjoner, hint og eksempler tilpasset deres nivå.

Dette er bare toppen av isfjellet. Sjekk ut [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - et åpen kildekode-bibliotek med spørsmål kuratert av utdanningseksperter - for å få en bredere forståelse av mulighetene! _Prøv å kjøre noen av disse spørsmålene i sandkassen eller ved å bruke OpenAI Playground for å se hva som skjer!_

## Hva er Prompt Engineering?

Vi startet denne leksjonen med å definere **Prompt Engineering** som prosessen med å _designe og optimalisere_ tekstinnputt (spørsmål) for å levere konsistente og kvalitetsrike svar (fullføringer) for en gitt applikasjonsmål og modell. Vi kan tenke på dette som en to-trinns prosess:

- _designe_ det første spørsmålet for en gitt modell og mål
- _raffinere_ spørsmålet iterativt for å forbedre kvaliteten på svaret

Dette er nødvendigvis en prøving-og-feiling-prosess som krever brukerintuisjon og innsats for å oppnå optimale resultater. Så hvorfor er det viktig? For å svare på det spørsmålet, må vi først forstå tre konsepter:

- _Tokenisering_ = hvordan modellen "ser" spørsmålet
- _Grunnmodeller_ = hvordan grunnmodellen "prosesserer" et spørsmål
- _Instruksjons-justerte LLM-er_ = hvordan modellen nå kan se "oppgaver"

### Tokenisering

En LLM ser spørsmål som en _sekvens av tokens_ der forskjellige modeller (eller versjoner av en modell) kan tokenisere det samme spørsmålet på forskjellige måter. Siden LLM-er er trent på tokens (og ikke på rå tekst), har måten spørsmål blir tokenisert en direkte innvirkning på kvaliteten på det genererte svaret.

For å få en intuisjon for hvordan tokenisering fungerer, prøv verktøy som [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) vist nedenfor. Kopier inn spørsmålet ditt - og se hvordan det blir konvertert til tokens, og legg merke til hvordan mellomromstegn og skilletegn håndteres. Merk at dette eksempelet viser en eldre LLM (GPT-3) - så å prøve dette med en nyere modell kan gi et annet resultat.

### Konsept: Grunnmodeller

Når et spørsmål er tokenisert, er den primære funksjonen til ["Grunnmodellen"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (eller Foundation model) å forutsi tokenet i den sekvensen. Siden LLM-er er trent på massive tekstdatasett, har de en god forståelse av de statistiske sammenhengene mellom tokens og kan gjøre den forutsigelsen med en viss grad av sikkerhet. Merk at de ikke forstår _meningen_ med ordene i spørsmålet eller tokenet; de ser bare et mønster de kan "fullføre" med sin neste forutsigelse. De kan fortsette å forutsi sekvensen til den avsluttes av brukerintervensjon eller en forhåndsbestemt betingelse.

Vil du se hvordan spørsmålsbasert fullføring fungerer? Skriv inn spørsmålet ovenfor i Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) med standardinnstillingene. Systemet er konfigurert til å behandle spørsmål som forespørsler om informasjon - så du bør se en fullføring som tilfredsstiller denne konteksten.

Men hva om brukeren ønsket å se noe spesifikt som oppfylte noen kriterier eller oppgave mål? Det er her _instruksjons-justerte_ LLM-er kommer inn i bildet.

### Konsept: Instruksjonsjusterte LLM-er

En [Instruksjonsjustert LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) starter med grunnmodellen og finjusterer den med eksempler eller innputt/utgangs-par (f.eks. samtaler med flere omganger) som kan inneholde klare instruksjoner - og responsen fra AI-en forsøker å følge den instruksjonen.

Dette bruker teknikker som Reinforcement Learning with Human Feedback (RLHF) som kan trene modellen til å _følge instruksjoner_ og _lære av tilbakemeldinger_ slik at den produserer svar som er bedre egnet til praktiske applikasjoner og mer relevante for brukerens mål.

La oss prøve det - gå tilbake til spørsmålet ovenfor, men endre nå _systemmeldingen_ for å gi følgende instruksjon som kontekst:

> _Oppsummer innholdet du får for en andreklasseelev. Hold resultatet til ett avsnitt med 3-5 punkter._

Se hvordan resultatet nå er justert for å reflektere det ønskede målet og formatet? En lærer kan nå direkte bruke dette svaret i sine lysbilder for den klassen.

## Hvorfor trenger vi Prompt Engineering?

Nå som vi vet hvordan spørsmål blir behandlet av LLM-er, la oss snakke om _hvorfor_ vi trenger prompt engineering. Svaret ligger i det faktum at nåværende LLM-er utgjør en rekke utfordringer som gjør _pålitelige og konsistente fullføringer_ mer utfordrende å oppnå uten å legge innsats i spørsmålsutforming og optimalisering. For eksempel:

1. **Modellresponsene er stokastiske.** Det _samme spørsmålet_ vil sannsynligvis gi forskjellige svar med forskjellige modeller eller modellversjoner. Og det kan til og med gi forskjellige resultater med _samme modell_ på forskjellige tidspunkter. _Prompt engineering-teknikker kan hjelpe oss med å minimere disse variasjonene ved å gi bedre retningslinjer_.

1. **Modeller kan fabrikkere svar.** Modeller er forhåndstrent med _store men begrensede_ datasett, noe som betyr at de mangler kunnskap om konsepter utenfor det treningsomfanget. Som et resultat kan de produsere fullføringer som er unøyaktige, imaginære eller direkte motstridende med kjente fakta. _Prompt engineering-teknikker hjelper brukere med å identifisere og redusere slike fabrikasjoner, f.eks. ved å be AI om henvisninger eller resonnement_.

1. **Modellens kapabiliteter vil variere.** Nyere modeller eller modellgenerasjoner vil ha rikere kapabiliteter, men også bringe unike særegenheter og avveininger i kostnad og kompleksitet. _Prompt engineering kan hjelpe oss med å utvikle beste praksis og arbeidsflyter som abstraherer bort forskjeller og tilpasser seg modellspecifikke krav på en skalerbar, sømløs måte_.

La oss se dette i aksjon i OpenAI eller Azure OpenAI Playground:

- Bruk det samme spørsmålet med forskjellige LLM-distribusjoner (f.eks, OpenAI, Azure OpenAI, Hugging Face) - så du variasjonene?
- Bruk det samme spørsmålet gjentatte ganger med den _samme_ LLM-distribusjonen (f.eks. Azure OpenAI Playground) - hvordan skilte disse variasjonene seg?

### Fabrikasjons eksempel

I dette kurset bruker vi begrepet **"fabrikkering"** for å referere til fenomenet der LLM-er noen ganger genererer faktuelt feil informasjon på grunn av begrensninger i deres trening eller andre begrensninger. Du kan også ha hørt dette referert til som _"hallusinasjoner"_ i populære artikler eller forskningspapirer. Vi anbefaler imidlertid sterkt å bruke _"fabrikkering"_ som begrep slik at vi ikke utilsiktet tillegger menneskelige egenskaper til en maskindrevet utgang. Dette forsterker også [Responsible AI-retningslinjer](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) fra et terminologisk perspektiv, ved å fjerne termer som også kan anses som støtende eller ikke-inkluderende i noen sammenhenger.

Vil du få en følelse av hvordan fabrikasjoner fungerer? Tenk på et spørsmål som instruerer AI-en til å generere innhold for et ikke-eksisterende emne (for å sikre at det ikke finnes i treningsdatasettet). For eksempel - jeg prøvde dette spørsmålet:

> **Spørsmål:** generer en leksjonsplan om Marskrigen i 2076.

Et nettsøk viste meg at det var fiktive beretninger (f.eks. TV-serier eller bøker) om Marskriger - men ingen i 2076. Sunn fornuft forteller oss også at 2076 er _i fremtiden_ og derfor ikke kan være knyttet til en virkelig hendelse.

Så hva skjer når vi kjører dette spørsmålet med forskjellige LLM-leverandører?

Som forventet produserer hver modell (eller modellversjon) litt forskjellige svar takket være stokastisk oppførsel og variasjoner i modellkapabiliteter. For eksempel retter en modell seg mot et publikum i 8. klasse mens den andre antar en videregående student. Men alle tre modellene genererte svar som kunne overbevise en uinformert bruker om at hendelsen var ekte

Prompt engineering-teknikker som _metaprompting_ og _temperaturkonfigurasjon_ kan redusere modellsfabrikasjoner til en viss grad. Nye prompt engineering _arkitekturer_ inkorporerer også nye verktøy og teknikker sømløst inn i spørsmålsflyten, for å redusere eller redusere noen av disse effektene.

## Case Study: GitHub Copilot

La oss avslutte denne seksjonen ved å få en følelse av hvordan prompt engineering brukes i virkelige løsninger ved å se på en Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot er din "AI Pair Programmer" - den konverterer tekstspørsmål til kodefullføringer og er integrert i ditt utviklingsmiljø (f.eks. Visual Studio Code) for en sømløs brukeropplevelse. Som dokumentert i serien av blogger nedenfor, var den tidligste versjonen basert på OpenAI Codex-modellen - med ingeniører som raskt innså behovet for å finjustere modellen og utvikle bedre prompt engineering-teknikker, for å forbedre kodekvaliteten. I juli [debuterte de en forbedret AI-modell som går utover Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) for enda raskere forslag.

Les innleggene i rekkefølge, for å følge deres læringsreise.

Du kan også bla gjennom deres [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) for flere innlegg som [dette](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) som viser hvordan disse modellene og teknikkene er _anvendt_ for å drive virkelige applikasjoner.

## Spørsmålsbygging

Vi har sett hvorfor prompt engineering er viktig - nå la oss forstå hvordan spørsmål er _konstruert_ slik at vi kan evaluere forskjellige teknikker for mer effektiv spørsmålsdesign.

### Grunnleggende Spørsmål

La oss starte med det grunnleggende spørsmålet: en tekstinnputt sendt til modellen uten annen kontekst. Her er et eksempel - når vi sender de første ordene av USAs nasjonals
The real value of templates lies in the ability to create and publish _prompt libraries_ for specific application domains, where the prompt template is _optimized_ to reflect application-specific context or examples that make responses more relevant and accurate for the intended user audience. The [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository is a great example of this approach, curating a library of prompts for the education domain with emphasis on key objectives like lesson planning, curriculum design, student tutoring, etc.

## Supporting Content

If we think about prompt construction as having an instruction (task) and a target (primary content), then _secondary content_ is like additional context we provide to **influence the output in some way**. It could be tuning parameters, formatting instructions, topic taxonomies, etc., that can help the model _tailor_ its response to suit the desired user objectives or expectations.

For example: Given a course catalog with extensive metadata (name, description, level, metadata tags, instructor, etc.) on all the available courses in the curriculum:

- we can define an instruction to "summarize the course catalog for Fall 2023"
- we can use the primary content to provide a few examples of the desired output
- we can use the secondary content to identify the top 5 "tags" of interest.

Now, the model can provide a summary in the format shown by the few examples - but if a result has multiple tags, it can prioritize the 5 tags identified in secondary content.

---

## Prompting Best Practices

Now that we know how prompts can be _constructed_, we can start thinking about how to _design_ them to reflect best practices. We can think about this in two parts - having the right _mindset_ and applying the right _techniques_.

### Prompt Engineering Mindset

Prompt Engineering is a trial-and-error process, so keep three broad guiding factors in mind:

1. **Domain Understanding Matters.** Response accuracy and relevance is a function of the _domain_ in which the application or user operates. Apply your intuition and domain expertise to **customize techniques** further. For instance, define _domain-specific personalities_ in your system prompts, or use _domain-specific templates_ in your user prompts. Provide secondary content that reflects domain-specific contexts, or use _domain-specific cues and examples_ to guide the model towards familiar usage patterns.

2. **Model Understanding Matters.** We know models are stochastic by nature. But model implementations can also vary in terms of the training dataset they use (pre-trained knowledge), the capabilities they provide (e.g., via API or SDK), and the type of content they are optimized for (e.g., code vs. images vs. text). Understand the strengths and limitations of the model you are using, and use that knowledge to _prioritize tasks_ or build _customized templates_ that are optimized for the model's capabilities.

3. **Iteration & Validation Matters.** Models are evolving rapidly, and so are the techniques for prompt engineering. As a domain expert, you may have other context or criteria _your_ specific application, that may not apply to the broader community. Use prompt engineering tools & techniques to "jump start" prompt construction, then iterate and validate the results using your own intuition and domain expertise. Record your insights and create a **knowledge base** (e.g., prompt libraries) that can be used as a new baseline by others, for faster iterations in the future.

## Best Practices

Now let's look at common best practices that are recommended by [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) and [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) practitioners.

| What                              | Why                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluate the latest models.       | New model generations are likely to have improved features and quality - but may also incur higher costs. Evaluate them for impact, then make migration decisions.                                                                                |
| Separate instructions & context   | Check if your model/provider defines _delimiters_ to distinguish instructions, primary and secondary content more clearly. This can help models assign weights more accurately to tokens.                                                         |
| Be specific and clear             | Give more details about the desired context, outcome, length, format, style, etc. This will improve both the quality and consistency of responses. Capture recipes in reusable templates.                                                          |
| Be descriptive, use examples      | Models may respond better to a "show and tell" approach. Start with a `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` values. Come back to [Learning Sandbox section](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) to learn how.

### Next, open the Jupyter Notebook

- Select the runtime kernel. If using options 1 or 2, simply select the default Python 3.10.x kernel provided by the dev container.

You're all set to run the exercises. Note that there are no _right and wrong_ answers here - just exploring options by trial-and-error and building intuition for what works for a given model and application domain.

_For this reason there are no Code Solution segments in this lesson. Instead, the Notebook will have Markdown cells titled "My Solution:" that shows one example output for reference._

## Knowledge check

Which of the following is a good prompt following some reasonable best practices?

1. Show me an image of red car
2. Show me an image of red car of make Volvo and model XC90 parked by a cliff with the sun setting
3. Show me an image of red car of make Volvo and model XC90

A: 2, it's the best prompt as it provides details on "what" and goes into specifics (not just any car but a specific make and model) and it also describes the overall setting. 3 is next best as it also contains a lot of description.

## 🚀 Challenge

See if you can leverage the "cue" technique with the prompt: Complete the sentence "Show me an image of red car of make Volvo and ". What does it respond with, and how would you improve it?

## Great Work! Continue Your Learning

Want to learn more about different Prompt Engineering concepts? Go to the [continued learning page](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to find other great resources on this topic.

Head over to Lesson 5 where we will look at [advanced prompting techniques](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi bestreber oss på nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår fra bruken av denne oversettelsen.