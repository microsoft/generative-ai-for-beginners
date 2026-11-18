# Bidra

Dette prosjektet ønsker bidrag og forslag velkommen. De fleste bidrag krever at du
godtar en Contributor License Agreement (CLA) som erklærer at du har rett til,
og faktisk gir oss rettighetene til å bruke bidraget ditt. For detaljer, besøk
<https://cla.microsoft.com>.

> Viktig: når du oversetter tekst i dette repoet, vennligst sørg for at du ikke bruker maskinoversettelse. Vi vil verifisere oversettelsene via fellesskapet, så vennligst tilby deg kun å oversette til språk du behersker godt.

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du må
gi en CLA og merke PR-en passende (f.eks. etikett, kommentar). Bare følg
instruksjonene gitt av boten. Du trenger bare å gjøre dette én gang på tvers av alle repoer som bruker vår CLA.

## Adferdskodeks

Dette prosjektet har tatt i bruk [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
For mer informasjon, les [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) med eventuelle tilleggs spørsmål eller kommentarer.

## Spørsmål eller problem?

Vennligst ikke åpne GitHub-issues for generelle støttehenvendelser da GitHub-listen skal brukes for funksjonsforespørsler og feilrapporter. På denne måten kan vi lettere spore faktiske problemer eller feil i koden og holde generell diskusjon adskilt fra selve koden.

## Feil, problemer, bugs og bidrag

Når du sender inn endringer til Generative AI for Beginners-repositoriet, vennligst følg disse anbefalingene.

* Alltid fork repositoriet til din egen konto før du gjør endringer
* Ikke kombiner flere endringer i én pull request. For eksempel, send inn feilretting og dokumentasjonsoppdateringer som separate PRer
* Hvis pull requesten din viser flettkonflikter, sørg for å oppdatere din lokale main slik at den speiler hovedrepositoriet før du gjør endringene
* Hvis du sender inn en oversettelse, vennligst lag én PR for alle de oversatte filene da vi ikke godtar delvise oversettelser av innholdet
* Hvis du sender inn en feilretting eller dokumentasjonsfiks, kan du kombinere endringene i én PR der det passer

## Redaksjonell omfang og tredjepartsprodukter

Dette læreplanfokuset er på Microsoft-teknologier og leverandørnøytrale åpne standarder. Bidrag bør tjene et klart pedagogisk formål og må ikke primært være ment for å introdusere eller promotere et tredjeparts kommersielt produkt, vertstjeneste, modellruter, SDK, MCP-server eller annet leverandørspesifikt tilbud.

Åpen kildekode og tredjepartsavhengigheter kan refereres til når de er nødvendige for å forklare en åpen standard eller interoperabilitetsscenario, presenteres nøytralt og ikke er sentrert rundt et leverandørprodukt eller vert-endepunkt. Hvis ditt foreslåtte bidrag inkluderer et leverandørspesifikt produkt eller tjeneste, åpne en issue og få godkjenning fra vedlikeholder før du sender inn en pull request.

Bidragsytere må avsløre relevant ansettelse, eierskap, sponsing eller annen tilknytning til et produkt eller tjeneste som refereres til i deres bidrag. Ikke inkluder udokumenterte påstander om pris, ytelse, sikkerhet, privatliv eller sammenligninger. Kjørbare eksempler må som standard ikke sende elevdata eller utføre offentlige handlinger gjennom en ekstern tredjepartstjeneste.

## Generelle retningslinjer for skriving

- Sørg for at alle URL-ene dine er omsluttet av firkantede paranteser etterfulgt av en parentes uten ekstra mellomrom rundt eller innenfor dem `[]()`.
- Sørg for at alle relative lenker (dvs. lenker til andre filer og mapper i repoet) starter med en `./` som viser til en fil eller mappe i gjeldende arbeidskatalog eller en `../` som viser til en fil eller mappe i en overordnet arbeidskatalog.
- Sørg for at alle relative lenker (dvs. lenker til andre filer og mapper i repoet) har en sporings-ID (dvs. `?` eller `&` etterfulgt av `wt.mc_id=` eller `WT.mc_id=`) på slutten.
- Sørg for at alle URL-er fra følgende domener _github.com, microsoft.com, visualstudio.com, aka.ms, og azure.com_ har en sporings-ID (dvs. `?` eller `&` etterfulgt av `wt.mc_id=` eller `WT.mc_id=`) på slutten.
- Sørg for at lenkene dine ikke har lands-spesifikk lokalitet i seg (f.eks. `/en-us/` eller `/en/`).
- Sørg for at alle bilder er lagret i `./images`-mappen.
- Sørg for at bildene har beskrivende navn med engelske bokstaver, tall og bindestreker i navnet på bildet.

## GitHub arbeidsflyter

Når du sender inn en pull request, vil fire forskjellige arbeidsflyter utløses for å validere reglene ovenfor.
Følg bare instruksjonene som står her for å bestå arbeidsflytkontrollene.

- [Sjekk ødelagte relative stier](#check-broken-relative-paths)
- [Sjekk at stier har sporing](#check-paths-have-tracking)
- [Sjekk at URL-er har sporing](#check-urls-have-tracking)
- [Sjekk at URL-er ikke har lokalitet](#check-urls-dont-have-locale)

### Sjekk ødelagte relative stier

Denne arbeidsflyten sikrer at alle relative stier i filene dine fungerer.
Dette repositoriet er deployert til GitHub pages, så du må være svært nøye når du skriver linker som binder alt sammen for ikke å lede noen til feil sted.

For å være sikker på at lenkene dine fungerer, bruk enkelt VS code for å sjekke det.

For eksempel, når du holder musen over en lenke i filene dine, vil du få mulighet til å følge lenken ved å trykke **ctrl + klikk**

![VS code follow links screenshot](../../translated_images/no/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Skjermbilde fra vs code som viser prompt for å følge en lenke når du holder musen over den.")

Hvis du klikker på en lenke og den ikke fungerer lokalt, vil den definitivt utløse arbeidsflyten og ikke fungere på GitHub.

For å fikse dette, prøv å skrive lenken med hjelp fra VS code.

Når du skriver `./` eller `../` vil VS code gi deg mulighet til å velge blant tilgjengelige alternativer basert på det du har skrevet.

![VS code select relative path screenshot](../../translated_images/no/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Skjermbilde fra vs code som viser prompt for å velge relativ sti fra en popup-liste.")

Følg stien ved å klikke på ønsket fil eller mappe, så er du sikker på at stien ikke er ødelagt.

Når du legger til korrekt relativ sti, lagrer og pusher endringene, vil arbeidsflyten utløses igjen for å verifisere endringene dine.
Hvis du består sjekken, er alt klart.

### Sjekk at stier har sporing

Denne arbeidsflyten sørger for at alle relative stier har sporing i seg.
Dette repositoriet er deployert til GitHub pages, så vi må spore bevegelser mellom ulike filer og mapper.

For å være sikker på at dine relative stier har sporing i seg, sjekk at teksten `?wt.mc_id=` står på slutten av stien.
Hvis det er tilfelle, vil du bestå denne sjekken.

Hvis ikke, kan du få denne feilen.

![GitHub check paths missing tracking comment screenshot](../../translated_images/no/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Skjermbilde fra GitHub-kommentar som viser manglende sporing i relative stier")

For å fikse dette, åpne filstien som arbeidsflyten fremhevet og legg til sporings-ID på slutten av de relative stiene.

Når du har lagt til sporings-ID, lagret og pushet endringene, vil arbeidsflyten kjøre igjen for å verifisere.
Hvis du består sjekken, er det klart til bruk.

### Sjekk at URL-er har sporing

Denne arbeidsflyten sørger for at alle web-URL-er har sporing i seg.
Dette repositoriet er tilgjengelig for alle, så du må sørge for å spore tilgang for å vite hvor trafikken kommer fra.

For å være sikker på at URL-ene dine har sporing, sjekk at teksten `?wt.mc_id=` står på slutten av URL-en.
Hvis det er tilfelle, vil du bestå denne sjekken.

Hvis ikke, kan du få denne feilmeldingen.

![GitHub check urls missing tracking comment screenshot](../../translated_images/no/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Skjermbilde fra GitHub-kommentar som viser manglende sporing i URL-er")

For å fikse dette, åpne filstien som arbeidsflyten fremhevet og legg til sporings-ID på slutten av URL-ene.

Når du har lagt til sporings-ID, lagret og pushet endringene, vil arbeidsflyten kjøre igjen for å verifisere.
Hvis du består sjekken, er det klart til bruk.

### Sjekk at URL-er ikke har lokalitet

Denne arbeidsflyten sørger for at web-URL-er ikke har lands-spesifikk lokalitet i seg.
Dette repositoriet er tilgjengelig for alle i hele verden, så du må passe på å ikke inkludere ditt lands lokalitet i URL-ene.

For å være sikker på at URL-ene dine ikke har lands-lokalitet, sjekk etter teksten `/en-us/` eller `/en/` eller noe annet språklokalitet hvor som helst i URL-en.
Hvis det ikke finnes i URL-ene dine, vil du bestå denne sjekken.

Hvis ikke, kan du få denne feilen.

![GitHub check country locale comment screenshot](../../translated_images/no/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Skjermbilde fra GitHub-kommentar som viser lagt til lands-lokalitet i URL-er")

For å fikse dette, åpne filstien som arbeidsflyten fremhevet og fjern landets lokalitet fra URL-ene.

Når du har fjernet lokaliteten, lagret og pushet endringene, vil arbeidsflyten kjøre igjen for å verifisere.
Hvis du består sjekken, er det klart til bruk.

Gratulerer! Vi vil komme tilbake til deg så snart som mulig med tilbakemelding om bidraget ditt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->