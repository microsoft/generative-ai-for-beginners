# Bijdragen

Dit project verwelkomt bijdrages en suggesties. Voor de meeste bijdrages moet je
akkoord gaan met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt,
en daadwerkelijk, ons de rechten verleent om je bijdrage te gebruiken. Voor details, bezoek
<https://cla.microsoft.com>.

> Belangrijk: bij het vertalen van tekst in deze repo, zorg er alstublieft voor dat je geen machinevertaling gebruikt. We zullen vertalingen via de community verifiëren, dus meld je alleen aan voor vertalingen in talen waarin je vaardig bent.

Wanneer je een pull request indient, bepaalt een CLA-bot automatisch of je een CLA moet
aanleveren en voorziet het PR van de juiste aanduiding (bijv. label, commentaar). Volg simpelweg de
instructies van de bot. Dit hoef je slechts één keer te doen voor alle repositories die onze CLA gebruiken.

## Gedragscode

Dit project heeft de [Microsoft Open Source gedragscode](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) aangenomen.
Voor meer informatie lees de [Gedragscode FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) of neem contact op via [opencode@microsoft.com](mailto:opencode@microsoft.com) met aanvullende vragen of opmerkingen.

## Vraag of probleem?

Open alstublieft geen GitHub-issues voor algemene ondersteuningsvragen, aangezien de GitHub-lijst bedoeld is voor functieverzoeken en bugrapporten. Op deze manier kunnen we daadwerkelijk problemen of bugs in de code eenvoudiger volgen en het algemene gesprek gescheiden houden van de daadwerkelijke code.

## Typfouten, problemen, bugs en bijdragen

Wanneer je wijzigingen indient aan de Generative AI for Beginners repository, volg dan deze aanbevelingen.

* Fork altijd de repository naar je eigen account voordat je wijzigingen aanbrengt
* Combineer geen meerdere wijzigingen in één pull request. Dien bijvoorbeeld bugfixes en documentatie-updates in via aparte PR's
* Als je pull request merge-conflicten toont, zorg er dan voor dat je lokale main up-to-date is en een spiegel is van wat er in de hoofdrepository staat voordat je wijzigingen aanbrengt
* Als je een vertaling indient, maak dan één PR aan voor alle vertaalde bestanden; we accepteren geen gedeeltelijke vertalingen van de inhoud
* Als je een typfout of documentatiecorrectie indient, kun je wijzigingen combineren in één PR waar passend

## Redactionele scope en producten van derden

Dit curriculum richt zich op Microsoft-technologieën en leverancier-neutrale open standaarden. Bijdragen moeten een duidelijk educatief doel dienen en mogen niet primair bedoeld zijn om een commercieel product van derden, gehoste dienst, modelrouter, SDK, MCP-server of andere leverancier-specifieke aanbieding te introduceren of promoten.

Open-source software en afhankelijkheden van derden kunnen worden genoemd wanneer ze nodig zijn om een open standaard of interoperabiliteitsscenario uit te leggen, neutraal worden gepresenteerd en niet zijn gericht op een product of gehoste eindpunt van een leverancier. Als je voorgestelde bijdrage een leverancier-specifiek product of dienst omvat, open dan een issue en verkrijg goedkeuring van de beheerder voordat je een pull request indient.

Bijdragers moeten elke relevante werkrelatie, eigendom, sponsoring of andere affiliatie met een product of dienst die in hun bijdrage wordt genoemd, openbaar maken. Vermeld geen niet-ondersteunde claims over prijs, prestaties, veiligheid, privacy of vergelijkende aspecten. Uitvoerbare voorbeelden mogen standaard geen leerlinggegevens verzenden of publieke acties uitvoeren via een externe service van een derde partij.

## Algemene richtlijnen voor schrijven

- Zorg ervoor dat al je URL's zijn omgeven door vierkante haakjes gevolgd door haakjes zonder extra spaties eromheen of erin `[]()`.
- Zorg ervoor dat elke relatieve link (d.w.z. links naar andere bestanden en mappen in de repository) begint met een `./` die verwijst naar een bestand of map in de huidige werkdirectory of een `../` die verwijst naar een bestand of map in een bovenliggende werkdirectory.
- Zorg ervoor dat elke relatieve link (d.w.z. links naar andere bestanden en mappen in de repository) een tracking-ID (d.w.z. `?` of `&` dan `wt.mc_id=` of `WT.mc_id=`) aan het einde heeft.
- Zorg ervoor dat elke URL van de volgende domeinen _github.com, microsoft.com, visualstudio.com, aka.ms, en azure.com_ een tracking-ID (d.w.z. `?` of `&` dan `wt.mc_id=` of `WT.mc_id=`) aan het einde heeft.
- Zorg ervoor dat je links geen landspecifieke locale bevatten (d.w.z. `/en-us/` of `/en/`).
- Zorg ervoor dat alle afbeeldingen zijn opgeslagen in de `./images` map.
- Zorg ervoor dat de afbeeldingen beschrijvende namen hebben met Engelse letters, cijfers en streepjes in de bestandsnaam.

## GitHub Workflows

Wanneer je een pull request indient, worden vier verschillende workflows getriggerd om de bovenstaande regels te valideren.
Volg gewoon de hier vermelde instructies om te slagen voor de workflow checks.

- [Controleer gebroken relatieve paden](#check-broken-relative-paths)
- [Controleer of paden tracking bevatten](#check-paths-have-tracking)
- [Controleer of URL's tracking bevatten](#check-urls-have-tracking)
- [Controleer of URL's geen locale bevatten](#check-urls-dont-have-locale)

### Controleer gebroken relatieve paden

Deze workflow zorgt ervoor dat elk relatief pad in je bestanden werkt.
Deze repository wordt gedeployed naar GitHub Pages, dus je moet erg voorzichtig zijn wanneer je de links typt die alles aan elkaar koppelen, zodat je niemand naar de verkeerde plek leidt.

Om te zorgen dat je links correct werken, gebruik gewoon VS Code om dat te controleren.

Bijvoorbeeld: wanneer je over een link in je bestanden zweeft, wordt je gevraagd om de link te volgen door **ctrl + klik** te drukken

![VS code volg links screenshot](../../translated_images/nl/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Screenshot van vs code prompt om een link te volgen wanneer je over een link zweeft.")

Als je op een link klikt en deze werkt lokaal niet, zal de workflow waarschijnlijk ook falen en zal het niet werken op GitHub.

Om dit probleem op te lossen, probeer de link te typen met behulp van VS Code.

Wanneer je `./` of `../` typt, zal VS Code je opties tonen op basis van wat je typt.

![VS code selecteer relatieve pad screenshot](../../translated_images/nl/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Screenshot van vs code prompt om relatief pad te selecteren uit een pop-up lijst.")

Volg het pad door te klikken op het gewenste bestand of map en je zult zeker weten dat je pad niet gebroken is.

Zodra je het juiste relatieve pad toevoegt, opslaat en je wijzigingen pusht, zal de workflow opnieuw getriggerd worden om je wijzigingen te verifiëren.
Als je de check doorstaat, dan ben je klaar om verder te gaan.

### Controleer of paden tracking bevatten

Deze workflow zorgt ervoor dat elk relatief pad tracking bevat.
Deze repository wordt gedeployed naar GitHub Pages, dus we moeten de beweging tussen de verschillende bestanden en mappen volgen.

Om te zorgen dat je relatieve paden tracking bevatten, controleer gewoon of de volgende tekst `?wt.mc_id=` aan het einde van het pad staat.
Als het wordt toegevoegd aan je relatieve paden, dan zul je deze controle doorstaan.

Zo niet, dan kun je de volgende foutmelding krijgen.

![GitHub check paths missing tracking comment screenshot](../../translated_images/nl/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Screenshot van github-opmerking die ontbrekende tracking van relatieve paden toont")

Om dit probleem op te lossen, probeer het bestandspad te openen dat door de workflow is gemarkeerd en voeg de tracking-ID toe aan het einde van de relatieve paden.

Zodra je de tracking-ID hebt toegevoegd, opslaat en je wijzigingen pusht, wordt de workflow opnieuw geactiveerd om je wijzigingen te verifiëren.
Als je de controle doorstaat, ben je klaar om verder te gaan.

### Controleer of URL's tracking hebben

Deze workflow zorgt ervoor dat elke web-URL tracking bevat.
Deze repository is beschikbaar voor iedereen, dus je moet ervoor zorgen dat je de toegang volgt om te weten van waar het verkeer komt.

Om er zeker van te zijn dat je URL's tracking bevatten, controleer je eenvoudigweg of de volgende tekst `?wt.mc_id=` aan het einde van de URL staat.
Als het is toegevoegd aan je URL's, dan zul je deze controle doorstaan.

Zo niet, dan kun je de volgende foutmelding krijgen.

![GitHub check urls missing tracking comment screenshot](../../translated_images/nl/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Screenshot van github-opmerking die ontbrekende tracking van URL's toont")

Om dit probleem op te lossen, probeer het bestandspad te openen dat door de workflow is gemarkeerd en voeg de tracking-ID toe aan het einde van de URL's.

Zodra je de tracking-ID hebt toegevoegd, opslaat en je wijzigingen pusht, wordt de workflow opnieuw geactiveerd om je wijzigingen te verifiëren.
Als je de controle doorstaat, ben je klaar om verder te gaan.

### Controleer of URL's geen locale bevatten

Deze workflow zorgt ervoor dat geen enkele web-URL een landafhankelijke locale bevat.
Deze repository is beschikbaar voor iedereen over de hele wereld, dus je moet ervoor zorgen dat je de locale van je land niet opneemt in URL's.

Om er zeker van te zijn dat je URL's geen landlocale bevatten, controleer je eenvoudig of de volgende tekst `/en-us/` of `/en/` of een andere taallocale ergens in de URL voorkomt.
Als dat niet voorkomt in je URL's, dan zul je deze controle doorstaan.

Zo niet, dan kun je de volgende foutmelding krijgen.

![GitHub check country locale comment screenshot](../../translated_images/nl/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Screenshot van github-opmerking die toegevoegde landlocale aan URL's toont")

Om dit probleem op te lossen, probeer het bestandspad te openen dat door de workflow is gemarkeerd en verwijder de landlocale uit de URL's.

Zodra je de landlocale hebt verwijderd, opslaat en je wijzigingen pusht, wordt de workflow opnieuw geactiveerd om je wijzigingen te verifiëren.
Als je de controle doorstaat, ben je klaar om verder te gaan.

Gefeliciteerd! We nemen zo snel mogelijk contact met je op met feedback over je bijdrage.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->