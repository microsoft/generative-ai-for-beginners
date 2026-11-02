# Bidrag

Dette projekt byder velkommen til bidrag og forslag. De fleste bidrag kræver, at du
accepterer en Contributor License Agreement (CLA), der erklærer, at du har ret til,
og faktisk gør det, at give os rettigheder til at bruge dit bidrag. For detaljer, besøg
<https://cla.microsoft.com>.

> Vigtigt: når du oversætter tekst i dette repo, skal du sørge for ikke at bruge maskinoversættelse. Vi vil verificere oversættelser via fællesskabet, så vær venlig kun at melde dig som oversætter til sprog, du mestrer.

Når du indsender en pull request, vil en CLA-bot automatisk afgøre, om du skal
levere en CLA og mærke PR korrekt (f.eks. label, kommentar). Følg blot
instruktionerne fra botten. Du skal kun gøre dette én gang for alle repositoryer, der bruger vores CLA.

## Adfærdskodeks

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
For mere information læs [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) for yderligere spørgsmål eller kommentarer.

## Spørgsmål eller Problem?

Venligst åbn ikke GitHub issues for generelle supportspørgsmål, da GitHub-listen bør bruges til funktionsanmodninger og fejlrapporter. På den måde kan vi lettere holde styr på faktiske problemer eller fejl i koden og holde den generelle diskussion adskilt fra selve koden.

## Trykfejl, Problemer, Fejl og bidrag

Når du sender ændringer til Generative AI for Beginners repositoryet, følg venligst disse anbefalinger.

* Fork altid repositoryet til din egen konto, før du laver dine ændringer
* Kombiner ikke flere ændringer i én pull request. For eksempel, indsend en fejlrettelse og dokumentationsopdateringer med separate PR’er
* Hvis din pull request viser merge-konflikter, skal du sikre dig at opdatere din lokale main til at afspejle det, der er i det centrale repository, før du laver dine ændringer
* Hvis du indsender en oversættelse, opret venligst én PR for alle de oversatte filer, da vi ikke accepterer delvise oversættelser af indholdet
* Hvis du indsender en korrektur eller dokumentationsrettelse, kan du kombinere ændringer i én PR, hvor det er hensigtsmæssigt

## Redaktionelt scope og tredjepartsprodukter

Dette pensum fokuserer på Microsoft-teknologier og leverandør-neutrale åbne standarder. Bidrag bør tjene et klart uddannelsesmæssigt formål og må ikke primært have til hensigt at introducere eller promovere et tredjeparts kommercielt produkt, hostet service, modelruter, SDK, MCP-server eller anden leverandørspecifik tjeneste.

Open source-software og tredjepartsafhængigheder kan nævnes, når de er nødvendige for at forklare en åben standard eller interoperabilitetsscenario, præsenteres neutralt og ikke centrerer sig om en leverandørs produkt eller hostede endpoint. Hvis dit foreslåede bidrag indeholder et leverandørspecifikt produkt eller service, åbn en issue og få godkendelse fra en maintainer, før du indsender en pull request.

Bidragydere skal oplyse om relevant ansættelse, ejerskab, sponsorat eller anden tilknytning til et produkt eller en tjeneste, der refereres til i deres bidrag. Inkluder ikke uunderbyggede påstande om pris, ydeevne, sikkerhed, privatliv eller sammenligninger. Kørende eksempler må ikke som standard overføre lærerddata eller udføre offentlige handlinger via en ekstern tredjepartsservice.

## Generelle retningslinjer for skrivning

- Sørg for, at alle dine URLs er indrammet med firkantede parenteser efterfulgt af en parentes uden ekstra mellemrum omkring eller inden i dem `[]()`.
- Sørg for, at ethvert relativt link (dvs. links til andre filer og mapper i repositoryet) starter med en `./`, der henviser til en fil eller mappe i den aktuelle arbejdsmappe eller en `../`, der henviser til en fil eller mappe i en overordnet arbejdsmappe.
- Sørg for, at ethvert relativt link (dvs. links til andre filer og mapper i repositoryet) har et sporings-id (dvs. `?` eller `&` efterfulgt af `wt.mc_id=` eller `WT.mc_id=`) i slutningen af det.
- Sørg for, at enhver URL fra følgende domæner _github.com, microsoft.com, visualstudio.com, aka.ms, og azure.com_ har et sporings-id (dvs. `?` eller `&` efterfulgt af `wt.mc_id=` eller `WT.mc_id=`) i slutningen af det.
- Sørg for, at dine links ikke indeholder landespecifik lokalitet (dvs. `/en-us/` eller `/en/`).
- Sørg for, at alle billeder er gemt i `./images` mappen.
- Sørg for, at billederne har beskrivende navne ved brug af engelske tegn, tal og bindestreger i navnet.

## GitHub Arbejdsgange

Når du indsender en pull request, udløses fire forskellige arbejdsgange for at validere de tidligere nævnte regler.
Følg blot instruktionerne her for at bestå arbejdsgangskontrollerne.

- [Check Broken Relative Paths](#check-broken-relative-paths)
- [Check Paths Have Tracking](#check-paths-have-tracking)
- [Check URLs Have Tracking](#check-urls-have-tracking)
- [Check URLs Don't Have Locale](#check-urls-dont-have-locale)

### Check Broken Relative Paths

Denne arbejdsgang sikrer, at alle relative stier i dine filer fungerer.
Dette repository deployeres til GitHub pages, så du skal være meget omhyggelig, når du skriver links, der binder alting sammen, for ikke at sende nogen til det forkerte sted.

For at sikre, at dine links fungerer korrekt, kan du blot bruge VS code til at tjekke det.

For eksempel, når du hover over et link i dine filer, vil du blive opfordret til at følge linket ved at trykke på **ctrl + klik**

![VS code follow links screenshot](../../translated_images/da/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Screenshot from vs code prompt to follow a link when you hover over a link.")

Hvis du klikker på et link, og det ikke virker lokalt, vil det med sikkerhed udløse arbejdsgangen og ikke fungere på GitHub.

For at løse dette problem, prøv at skrive linket med hjælp fra VS code.

Når du skriver `./` eller `../`, vil VS code opfordre dig til at vælge blandt tilgængelige muligheder i henhold til det, du har skrevet.

![VS code select relative path screenshot](../../translated_images/da/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Screenshot from vs code prompt to select relative path from a pop up list.")

Følg stien ved at klikke på den ønskede fil eller mappe, og du kan være sikker på, at din sti ikke er brudt.

Når du tilføjer den korrekte relative sti, gemmer og pusher dine ændringer, vil arbejdsgangen blive aktiveret igen for at verificere dine ændringer.
Hvis du består kontrollen, er du klar til at fortsætte.

### Check Paths Have Tracking

Denne arbejdsgang sikrer, at enhver relativ sti har tracking i sig.
Dette repository deployeres til GitHub pages, så vi skal spore bevægelsen mellem de forskellige filer og mapper.

For at sikre, at dine relative stier har tracking, skal du blot tjekke for følgende tekst `?wt.mc_id=` i slutningen af stien.
Hvis det er tilføjet til dine relative stier, består du kontrollen.

Hvis ikke, kan du få følgende fejl.

![GitHub check paths missing tracking comment screenshot](../../translated_images/da/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Screenshot from github comment that shows missing tracking from relative paths")

For at løse dette problem, prøv at åbne filstien, som arbejdsgangen har fremhævet, og tilføj tracking ID til enden af de relative stier.

Når du tilføjer tracking ID, gemmer og pusher dine ændringer, udløses arbejdsgangen igen for at verificere ændringerne.
Hvis du består kontrollen, er du klar til at fortsætte.

### Check URLs Have Tracking

Denne arbejdsgang sikrer, at enhver web-URL har tracking i sig.
Dette repository er tilgængeligt for alle, så du skal sikre dig at spore adgangen for at vide, hvor trafikken kommer fra.

For at sikre, at dine URLs har tracking, skal du blot tjekke for følgende tekst `?wt.mc_id=` i slutningen af URL'en.
Hvis det er tilføjet til dine URLs, består du kontrollen.

Hvis ikke, kan du få følgende fejl.

![GitHub check urls missing tracking comment screenshot](../../translated_images/da/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Screenshot from github comment that shows missing tracking from urls")

For at løse dette problem, prøv at åbne filstien, som arbejdsgangen har fremhævet, og tilføj tracking ID til slutningen af URL'erne.

Når du tilføjer tracking ID, gemmer og pusher dine ændringer, udløses arbejdsgangen igen for at verificere ændringerne.
Hvis du består kontrollen, er du klar til at fortsætte.

### Check URLs Don't Have Locale

Denne arbejdsgang sikrer, at ingen web-URL indeholder landspecifik lokalitet.
Dette repository er tilgængeligt for alle i hele verden, så du skal sikre, at du ikke inkluderer dit lands lokalitet i URLs.

For at sikre, at dine URLs ikke indeholder landelokalitet, skal du blot tjekke for følgende tekst `/en-us/` eller `/en/` eller andre språk-lokaliteter hvor som helst i URL'en.
Hvis disse ikke findes i dine URLs, består du kontrollen.

Hvis ikke, kan du få følgende fejl.

![GitHub check country locale comment screenshot](../../translated_images/da/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Screenshot from github comment that shows added country locale to urls")

For at løse dette problem, prøv at åbne filstien, som arbejdsgangen har fremhævet, og fjern landelokaliteten fra URL'erne.

Når du fjerner landelokaliteten, gemmer og pusher dine ændringer, udløses arbejdsgangen igen for at verificere ændringerne.
Hvis du består kontrollen, er du klar til at fortsætte.

Tillykke! Vi vender tilbage til dig så hurtigt som muligt med feedback på dit bidrag.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->