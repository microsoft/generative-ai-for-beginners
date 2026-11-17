# Bidrag

Dette projekt byder velkommen til bidrag og forslag. De fleste bidrag kræver, at du
accepterer en Contributor License Agreement (CLA), der erklærer, at du har ret til,
og faktisk gør, at give os rettighederne til at bruge dit bidrag. For detaljer, besøg
<https://cla.microsoft.com>.

> Vigtigt: når du oversætter tekst i dette repo, skal du sikre, at du ikke bruger maskinoversættelse. Vi vil verificere oversættelser via fællesskabet, så meld dig kun som frivillig til oversættelser på sprog, hvor du er kompetent.

Når du indsender en pull request, vil en CLA-bot automatisk afgøre, om du skal
fremlægge en CLA og dekorere PR'en passende (f.eks. mærke, kommentar). Følg blot
instruktionerne, som botten giver. Du skal kun gøre dette én gang på tværs af alle repositories, der bruger vores CLA.

## Adfærdskodeks

Dette projekt har taget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) til sig.
For mere information læs [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) ved yderligere spørgsmål eller kommentarer.

## Spørgsmål eller problem?

Undlad venligst at oprette GitHub issues til generelle supportspørgsmål, da GitHub-listen skal bruges til funktionsanmodninger og fejlrapporter. På den måde kan vi nemmere spore faktiske problemer eller fejl i koden og holde den generelle diskussion adskilt fra den faktiske kode.

## Fejl, problemer, bugs og bidrag

Når du indsender ændringer til Generative AI for Beginners repositoryet, bedes du følge disse anbefalinger.

* Fork altid repositoryet til din egen konto, inden du laver dine ændringer
* Kombiner ikke flere ændringer i en enkelt pull request. For eksempel, indsend rettelser af fejl og dokumentationsopdateringer i separate PR'er
* Hvis din pull request viser merge-konflikter, så sørg for at opdatere din lokale main, så den spejler hovedrepositoryet, inden du laver dine ændringer
* Hvis du indsender en oversættelse, så lav én PR for alle de oversatte filer, da vi ikke accepterer delvise oversættelser af indholdet
* Hvis du indsender en fejl eller dokumentationsrettelse, kan du kombinere ændringer i en enkelt PR, hvor det er passende

## Redaktionelt omfang og tredjepartsprodukter

Dette pensum fokuserer på Microsoft-teknologier og leverandørneutrale åbne standarder. Bidrag bør tjene et klart undervisningsformål og må ikke primært have til hensigt at introducere eller promovere et tredjeparts kommercielt produkt, hosted service, modelrouter, SDK, MCP-server eller andet leverandørspecifikt tilbud.

Open source-software og tredjepartsafhængigheder kan nævnes, når de er nødvendige for at forklare en åben standard eller interoperabilitetsscenarie, præsenteres neutralt og ikke er centreret omkring en leverandørs produkt eller hosted endpoint. Hvis dit foreslåede bidrag inkluderer et leverandørspecifikt produkt eller service, opret da en issue og få godkendelse fra vedligeholderen, inden du indsender en pull request.

Bidragydere skal oplyse om relevant ansættelse, ejerskab, sponsorskab eller anden tilknytning til et produkt eller en tjeneste nævnt i deres bidrag. Medtag ikke uunderbyggede påstande vedrørende pris, ydeevne, sikkerhed, privatliv eller sammenligninger. Kørbare eksempler må som standard ikke sende deltagedata eller udføre offentlige handlinger gennem en ekstern tredjepartstjeneste.

## Generelle retningslinjer for skrivning

- Sørg for, at alle dine URLs er indrammet i firkantede parenteser efterfulgt af en parentes uden ekstra mellemrum omkring eller indeni dem `[]()`.
- Sørg for, at ethvert relativt link (dvs. links til andre filer og mapper i repositoryet) starter med en `./`, der refererer til en fil eller en mappe lokaliseret i den nuværende arbejdsmappe eller en `../`, der refererer til en fil eller mappe i en overordnet mappe.
- Sørg for, at ethvert relativt link (dvs. links til andre filer og mapper i repositoryet) har et tracking-ID (dvs. `?` eller `&` efterfulgt af `wt.mc_id=` eller `WT.mc_id=`) i slutningen af det.
- Sørg for, at alle URLs fra følgende domæner _github.com, microsoft.com, visualstudio.com, aka.ms, og azure.com_ har et tracking-ID (dvs. `?` eller `&` efterfulgt af `wt.mc_id=` eller `WT.mc_id=`) i slutningen af det.
- Sørg for, at dine links ikke indeholder lande- eller regionsspecifikke lokaliteter (dvs. `/en-us/` eller `/en/`).
- Sørg for, at alle billeder er gemt i `./images` mappen.
- Sørg for, at billederne har beskrivende navne med engelske tegn, tal og bindestreger i navnet.

## GitHub Workflows

Når du indsender en pull request, udløses fire forskellige workflows for at validere de tidligere regler.
Følg blot instruktionerne her for at bestå workflow-tjek.

- [Tjek for brudte relative stier](#check-broken-relative-paths)
- [Tjek at stier har tracking](#check-paths-have-tracking)
- [Tjek at URLs har tracking](#check-urls-have-tracking)
- [Tjek at URLs ikke har lokalitet](#check-urls-dont-have-locale)

### Tjek for brudte relative stier

Denne workflow sikrer, at enhver relativ sti i dine filer virker.
Dette repository er distribueret på GitHub pages, så du skal være meget forsigtig, når du skriver links, der binder alting sammen, for ikke at dirigere nogen til det forkerte sted.

For at sikre, at dine links virker korrekt, brug blot VS code til at tjekke det.

For eksempel, når du holder musen over et hvilket som helst link i dine filer, bliver du bedt om at følge linket ved at trykke på **ctrl + klik**

![VS code følg links screenshot](../../translated_images/da/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Screenshot fra vs code prompt til at følge et link, når du holder musen over linket.")

Hvis du klikker på et link, og det ikke virker lokalt, så vil det helt sikkert udløse workflowen og ikke fungere på GitHub.

For at løse dette problem, prøv at skrive linket med hjælp fra VS code.

Når du skriver `./` eller `../`, vil VS code bede dig vælge mellem tilgængelige muligheder i henhold til det, du skrev.

![VS code vælg relativ sti screenshot](../../translated_images/da/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Screenshot fra vs code prompt til at vælge relativ sti fra en pop-up liste.")

Følg stien ved at klikke på den ønskede fil eller mappe, og du sikrer dig, at din sti ikke er brudt.

Når du har tilføjet den korrekte relative sti, gem og push dine ændringer, og workflowen bliver udløst igen for at bekræfte dine ændringer.
Hvis du består tjekket, er du good to go.

### Tjek at stier har tracking

Denne workflow sikrer, at enhver relativ sti har tracking i sig.
Dette repository er udgivet på GitHub pages, så vi skal spore bevægelsen mellem de forskellige filer og mapper.

For at sikre, at dine relative stier har tracking, skal du blot tjekke for følgende tekst `?wt.mc_id=` i slutningen af stien.
Hvis det er tilføjet til dine relative stier, vil du bestå dette tjek.

Hvis ikke, kan du få følgende fejl.

![GitHub tjek stier mangler tracking kommentar screenshot](../../translated_images/da/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Screenshot fra github-kommentar, der viser manglende tracking i relative stier")

For at rette dette problem, prøv at åbne den filsti, som workflowen har fremhævet, og tilføj tracking-ID'et til slutningen af de relative stier.

Når du har tilføjet tracking-ID'et, gem og push dine ændringer, og workflowen bliver udløst igen for at bekræfte dine ændringer.
Hvis du består tjekket, er du good to go.

### Tjek at URLs har tracking

Denne workflow sikrer, at enhver web-URL har tracking i sig.
Dette repository er tilgængeligt for alle, så du skal sikre dig at spore adgang for at kende trafikkens oprindelse.

For at sikre, at dine URLs har tracking i sig, skal du blot tjekke for følgende tekst `?wt.mc_id=` i slutningen af URL'en.
Hvis det er tilføjet til dine URLs, vil du bestå dette tjek.

Hvis ikke, kan du få følgende fejl.

![GitHub tjek urls mangler tracking kommentar screenshot](../../translated_images/da/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Screenshot fra github-kommentar, der viser manglende tracking i urls")

For at rette dette problem, prøv at åbne den filsti, som workflowen har fremhævet, og tilføj tracking-ID'et til slutningen af URLs.

Når du har tilføjet tracking-ID'et, gem og push dine ændringer, og workflowen bliver udløst igen for at bekræfte dine ændringer.
Hvis du består tjekket, er du good to go.

### Tjek at URLs ikke har lokalitet

Denne workflow sikrer, at enhver web-URL ikke har et lande-specifikt lokalitet i sig.
Dette repository er tilgængeligt for alle i verden, så du skal sikre dig, at du ikke inkluderer dit lands lokalitet i URLs.

For at sikre, at dine URLs ikke har landespecifik lokalitet, skal du blot tjekke for teksten `/en-us/` eller `/en/` eller enhver anden sprog-lokalitet hvor som helst i URL'en.
Hvis det ikke er til stede i dine URLs, vil du bestå dette tjek.

Hvis ikke, kan du få følgende fejl.

![GitHub tjek lande lokalitet kommentar screenshot](../../translated_images/da/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Screenshot fra github-kommentar, der viser tilføjet lande-lokalitet til urls")

For at rette dette problem, prøv at åbne den filsti, som workflowen har fremhævet, og fjern landets lokalitet fra URLs.

Når du har fjernet landets lokalitet, gem og push dine ændringer, og workflowen bliver udløst igen for at bekræfte dine ændringer.
Hvis du består tjekket, er du good to go.

Tillykke! Vi vender tilbage til dig så hurtigt som muligt med feedback om dit bidrag.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->