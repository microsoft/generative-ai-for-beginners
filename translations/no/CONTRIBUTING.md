# Bidra

Dette prosjektet ønsker bidrag og forslag velkommen. De fleste bidrag krever at du
godtar en Contributor License Agreement (CLA) som erklærer at du har rett til,
og faktisk gir oss rettighetene til å bruke ditt bidrag. For detaljer, besøk
<https://cla.microsoft.com>.

> Viktig: når du oversetter tekst i dette depotet, vær vennlig å ikke bruke maskinoversettelse. Vi vil verifisere oversettelser via fellesskapet, så vennligst meld deg bare til å oversette språk du behersker.

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du må
levere en CLA og markere PR-en passende (f.eks. etikett, kommentar). Følg
bare instruksjonene gitt av boten. Du trenger bare gjøre dette én gang på tvers av alle depot som bruker vår CLA.

## Atferdskodeks

Dette prosjektet har tatt i bruk [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
For mer informasjon, les [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) med eventuelle spørsmål eller kommentarer.

## Spørsmål eller problem?

Vennligst ikke åpne GitHub-issues for generelle støtteforespørsler, da GitHub-listen skal brukes til feature requests og bug-rapporter. På denne måten kan vi lettere spore faktiske problemer eller feil i koden og holde generell diskusjon atskilt fra koden.

## Feil, problemer, bugs og bidrag

Når du sender inn endringer til Generative AI for Beginners-depotet, vennligst følg disse anbefalingene.

* Alltid lag en fork av depotet til din egen konto før du gjør dine endringer
* Ikke kombiner flere endringer i én pull request. For eksempel send bugfikser og dokumentasjonsoppdateringer i separate PR-er
* Hvis din pull request viser merge konflikter, sørg for å oppdatere din lokale main til å være en kopi av hoveddepotet før du gjør endringer
* Hvis du sender inn en oversettelse, vennligst opprett én PR for alle de oversatte filene da vi ikke godtar delvise oversettelser av innholdet
* Hvis du sender inn en skrivefeil eller dokumentasjonsfikser, kan du kombinere endringer i én PR der det passer

## Redaksjonell omfang og tredjepartsprodukter

Dette læreplanen fokuserer på Microsoft-teknologier og leverandørnøytrale åpne standarder. Bidrag skal tjene et klart pedagogisk formål og må ikke primært ha som hensikt å introdusere eller promotere et tredjeparts kommersielt produkt, hostet tjeneste, modellruter, SDK, MCP-server eller annen leverandørspesifikk tjeneste.

Åpen kildekode-programvare og tredjepartsavhengigheter kan refereres til når de er nødvendige for å forklare en åpen standard eller interoperabilitetsscenario, presentert nøytralt og ikke sentrert rundt et leverandørs produkt eller hostet endepunkt. Hvis ditt foreslåtte bidrag inkluderer et leverandørspesifikt produkt eller tjeneste, åpne en issue og få godkjenning fra vedlikeholder før du sender en pull request.

Bidragsytere må opplyse om relevant ansettelse, eierskap, sponsing eller annen tilknytning til et produkt eller tjeneste nevnt i deres bidrag. Ikke inkluder ubekreftede påstander om pris, ytelse, sikkerhet, personvern eller sammenligninger. Kjørbare eksempler må som standard ikke sende data om deltakere eller utføre offentlige handlinger gjennom en ekstern tredjepartstjeneste.

## Generelle retningslinjer for skriving

- Sørg for at alle URL-er er omsluttet av firkantede parenteser etterfulgt av paranteser uten ekstra mellomrom rundt eller inni `[]()`.
- Sørg for at relative linker (dvs. linker til andre filer og mapper i depotet) starter med en `./` som refererer til en fil eller mappe i gjeldende arbeidskatalog eller en `../` som refererer til en fil eller mappe i en overordnet arbeidskatalog.
- Sørg for at relative linker (dvs. linker til andre filer og mapper i depotet) har et sporings-ID (dvs. `?` eller `&` så `wt.mc_id=` eller `WT.mc_id=`) på slutten.
- Sørg for at URL-er fra følgende domener _github.com, microsoft.com, visualstudio.com, aka.ms, og azure.com_ har et sporings-ID (dvs. `?` eller `&` så `wt.mc_id=` eller `WT.mc_id=`) på slutten.
- Sørg for at dine linker ikke har lands-spesifikt lokalisering i dem (dvs. `/en-us/` eller `/en/`).
- Sørg for at alle bilder er lagret i `./images`-mappen.
- Sørg for at bildene har beskrivende navn med engelske tegn, tall og bindestreker i navnet.

## GitHub Arbeidsflyter

Når du sender inn en pull request, vil fire forskjellige arbeidsflyter trigges for å validere de tidligere reglene.
Følg bare instruksjonene listet her for å bestå arbeidsflytsjekkene.

- [Sjekk Brutte Relative Stier](#check-broken-relative-paths)
- [Sjekk Stier Har Sporings-ID](#check-paths-have-tracking)
- [Sjekk URL-er Har Sporings-ID](#check-urls-have-tracking)
- [Sjekk URL-er Har Ikke Lokalisering](#check-urls-dont-have-locale)

### Sjekk Brutte Relative Stier

Denne arbeidsflyten sikrer at alle relative stier i filene dine fungerer.
Dette depotet er distribuert til GitHub Pages, så du må være veldig nøye med hvordan du skriver linker som binder alt sammen for å ikke sende noen til feil sted.

For å sikre at linkene dine fungerer riktig, bruk VS Code til å verifisere dette.

For eksempel, når du holder musepekeren over en link i filene dine, blir du bedt om å følge linken ved å trykke **ctrl + klikk**.

![VS code follow links screenshot](../../translated_images/no/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Skjermbilde fra VS Code som viser forespørsel om å følge en link når du holder musepekeren over en link.")

Hvis du klikker på en link og den ikke fungerer lokalt, vil den sannsynligvis trigge arbeidsflyten og ikke fungere på GitHub.

For å fikse dette, prøv å skrive linken med hjelp av VS Code.

Når du skriver `./` eller `../`, vil VS Code foreslå valg basert på det du har skrevet.

![VS code select relative path screenshot](../../translated_images/no/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Skjermbilde fra VS Code som viser valg av relativ sti fra en popup-liste.")

Følg stien ved å klikke på ønsket fil eller mappe, og du vil være sikker på at stien ikke er brutt.

Når du legger til korrekt relativ sti, lagrer og pusher endringene dine, vil arbeidsflyten bli trigget igjen for å verifisere endringene.
Hvis du består sjekken, er du klar til å gå videre.

### Sjekk Stier Har Sporings-ID

Denne arbeidsflyten sikrer at alle relative stier har sporings-ID i seg.
Dette depotet er distribuert til GitHub Pages, så vi må spore bevegelsen mellom de forskjellige filene og mappene.

For å sikre at dine relative stier har sporings-ID, sjekk etter teksten `?wt.mc_id=` på slutten av stien.
Hvis det er lagt til i dine relative stier, vil du bestå denne sjekken.

Hvis ikke kan du få følgende feil.

![GitHub check paths missing tracking comment screenshot](../../translated_images/no/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Skjermbilde av GitHub-kommentar som viser manglende sporings-ID i relative stier")

For å fikse dette, åpne filstien som arbeidsflyten har indikert og legg til sporings-ID på slutten av de relative stiene.

Når du har lagt til sporings-ID, lagret og pushet endringene, vil arbeidsflyten trigges på nytt for å verifisere.
Hvis du består sjekken, er du klar til å gå videre.

### Sjekk URL-er Har Sporings-ID

Denne arbeidsflyten sikrer at alle nett-URL-er har sporings-ID.
Dette depotet er tilgjengelig for alle, så du må sørge for å spore tilgangen for å vite hvor trafikken kommer fra.

For å sikre at URL-er har sporings-ID, sjekk etter teksten `?wt.mc_id=` på slutten av URL-en.
Hvis det er lagt til i dine URL-er, vil du bestå denne sjekken.

Hvis ikke kan du få følgende feil.

![GitHub check urls missing tracking comment screenshot](../../translated_images/no/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Skjermbilde av GitHub-kommentar som viser manglende sporings-ID i URL-er")

For å fikse dette, åpne filstien arbeidsflyten har indikert og legg til sporings-ID på slutten av URL-ene.

Når du har lagt til sporings-ID, lagret og pushet endringene, vil arbeidsflyten trigges på nytt for å verifisere.
Hvis du består sjekken, er du klar til å gå videre.

### Sjekk URL-er Har Ikke Lokalisering

Denne arbeidsflyten sikrer at ingen nett-URL-er har lands-spesifikk lokalisering.
Dette depotet er tilgjengelig for alle i hele verden, så du må sørge for å ikke inkludere ditt lands lokalisering i URLs.

For å sikre at URL-ene ikke har landslokalisering, sjekk etter teksten `/en-us/` eller `/en/` eller andre språk-lokaliseringer hvor som helst i URL-en.
Hvis det ikke er tilstede i URL-ene, vil du bestå sjekken.

Hvis ikke kan du få følgende feil.

![GitHub check country locale comment screenshot](../../translated_images/no/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Skjermbilde av GitHub-kommentar som viser lagt til lands-lokalisering i URL-er")

For å fikse dette, åpne filstien arbeidsflyten har indikert og fjern landslokalisering fra URL-ene.

Når du fjerner landslokaliseringen, lagrer og pusher endringene, vil arbeidsflyten trigges på nytt for å verifisere.
Hvis du består sjekken, er du klar til å gå videre.

Gratulerer! Vi vil kontakte deg så snart som mulig med tilbakemeldinger om ditt bidrag.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->