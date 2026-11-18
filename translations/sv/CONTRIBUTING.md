# Bidra

Detta projekt välkomnar bidrag och förslag. De flesta bidrag kräver att du
godkänner ett Contributor License Agreement (CLA) som förklarar att du har rätt att,
och faktiskt gör det, ge oss rättigheter att använda ditt bidrag. För detaljer, besök
<https://cla.microsoft.com>.

> Viktigt: när du översätter text i detta repo, vänligen se till att du inte använder maskinöversättning. Vi kommer att verifiera översättningarna via communityn, så var vänlig och erbjud dig endast att översätta till språk där du är skicklig.

När du skickar in en pull request kommer en CLA-bot automatiskt avgöra om du behöver
tillhandahålla ett CLA och märka PR:n lämpligt (t.ex. etikett, kommentar). Följ helt enkelt
instruktionerna från boten. Du behöver bara göra detta en gång för alla repos som använder vårt CLA.

## Uppförandekod

Detta projekt har antagit [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
För mer information, läs [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) eller kontakta [opencode@microsoft.com](mailto:opencode@microsoft.com) med frågor eller kommentarer.

## Fråga eller problem?

Vänligen öppna inte GitHub-ärenden för allmän support eftersom GitHub-listan bör användas för funktionsförfrågningar och bugg-rapporter. På så sätt kan vi lättare spåra faktiska problem eller buggar i koden och hålla den allmänna diskussionen separat från själva koden.

## Skrivfel, problem, buggar och bidrag

När du skickar in ändringar till Generative AI for Beginners-repositoriet, följ dessa rekommendationer.

* Forka alltid repositoriet till ditt eget konto innan du gör ändringar
* Kombinera inte flera ändringar i en pull request. Till exempel, skicka in buggfixar och dokumentationsuppdateringar som separata PR:er
* Om din pull request visar mergekonflikter, se till att uppdatera din lokala main till en spegling av huvudrepositoriet innan du gör ändringar
* Om du skickar in en översättning, skapa en PR för alla översatta filer eftersom vi inte accepterar partiella översättningar av innehållet
* Om du skickar in en skrivfel- eller dokumentationsfix kan du kombinera ändringar i en enda PR där det är lämpligt

## Redaktionell omfattning och tredjepartsprodukter

Denna kurs fokuserar på Microsoft-teknologier och leverantörsneutrala öppna standarder. Bidrag bör tjäna ett tydligt utbildningssyfte och får inte främst vara avsedda att introducera eller främja en tredjeparts kommersiell produkt, hostad tjänst, modellrouter, SDK, MCP-server eller annan leverantörsspecifik tjänst.

Öppen källkod och tredjepartsberoenden kan refereras till när de är nödvändiga för att förklara en öppen standard eller interoperabilitetsscenario, presenteras neutralt och inte är centrerade kring en leverantörs produkt eller hostade slutpunkt. Om ditt föreslagna bidrag inkluderar en leverantörsspecifik produkt eller tjänst, öppna ett ärende och få godkännande från ansvarig innan du skickar en pull request.

Bidragsgivare måste avslöja relevant anställning, ägarskap, sponsring eller annan anknytning till en produkt eller tjänst som refereras i deras bidrag. Inkludera inte obevisade pris-, prestanda-, säkerhets-, sekretess- eller jämförande påståenden. Körbara exempel får inte överföra användardata eller utföra offentliga åtgärder via en extern tredjepartstjänst som standard.

## Allmän vägledning för skrivande

- Se till att alla dina URL:er är inneslutna i hakparenteser följda av parentes utan extra mellanslag runt eller inuti dem `[]()`.
- Se till att alla relativa länkar (dvs. länkar till andra filer och mappar i repositoriet) börjar med `./` som hänvisar till en fil eller mapp i nuvarande arbetskatalog eller med `../` som hänvisar till en fil eller mapp i en överordnad arbetskatalog.
- Se till att alla relativa länkar (dvs. länkar till andra filer och mappar i repositoriet) har ett spårnings-ID (dvs. `?` eller `&` följt av `wt.mc_id=` eller `WT.mc_id=`) i slutet av dem.
- Se till att alla URL:er från följande domäner _github.com, microsoft.com, visualstudio.com, aka.ms, och azure.com_ har ett spårnings-ID (dvs. `?` eller `&` följt av `wt.mc_id=` eller `WT.mc_id=`) i slutet av dem.
- Se till att dina länkar inte innehåller landspecifik lokal (dvs. `/en-us/` eller `/en/`).
- Se till att alla bilder lagras i `./images` mappen.
- Se till att bilderna har beskrivande namn med engelska tecken, siffror och bindestreck i dina bildnamn.

## GitHub Arbetsflöden

När du skickar in en pull request kommer fyra olika arbetsflöden att triggas för att validera ovanstående regler.
Följ bara instruktionerna som listas här för att klara arbetsflödeskontrollerna.

- [Kontrollera brutna relativa sökvägar](#check-broken-relative-paths)
- [Kontrollera att sökvägar har spårning](#check-paths-have-tracking)
- [Kontrollera att URL:er har spårning](#check-urls-have-tracking)
- [Kontrollera att URL:er inte har lokal](#check-urls-dont-have-locale)

### Kontrollera brutna relativa sökvägar

Detta arbetsflöde säkerställer att alla relativa sökvägar i dina filer fungerar.
Detta repo är distribuerat till GitHub pages så du behöver vara mycket noggrann när du skriver länkar för att undvika felaktiga riktningar.

För att försäkra dig om att dina länkar fungerar kan du enkelt använda VS code för att kontrollera detta.

Till exempel, när du hovrar över en länk i dina filer kommer du att uppmanas att följa länken genom att trycka på **ctrl + klicka**

![VS code följa länkar skärmdump](../../translated_images/sv/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Skärmdump från VS code som uppmanar att följa en länk när du hovrar över den.")

Om du klickar på en länk och den inte fungerar lokalt så kommer den säkerligen att trigga arbetsflödet och inte fungera på GitHub.

För att åtgärda detta försök att skriva länken med hjälp av VS code.

När du skriver `./` eller `../` kommer VS code att uppmana dig att välja från tillgängliga alternativ baserat på vad du skrivit.

![VS code välj relativ sökväg skärmdump](../../translated_images/sv/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Skärmdump från VS code som uppmanar att välja relativ sökväg från en pop-up lista.")

Följ sökvägen genom att klicka på önskad fil eller mapp och du kan vara säker på att din sökväg inte är bruten.

När du lagt till korrekt relativ sökväg, spara och pusha dina ändringar så triggas arbetsflödet igen för att verifiera dina ändringar.
Om du klarar kontrollen är du redo att gå vidare.

### Kontrollera att sökvägar har spårning

Detta arbetsflöde säkerställer att alla relativa sökvägar har spårning i sig.
Detta repo distribueras till GitHub pages så vi behöver spåra rörelsen mellan olika filer och mappar.

För att försäkra dig om att dina relativa sökvägar har spårning, kontrollera helt enkelt efter texten `?wt.mc_id=` i slutet av sökvägen.
Om det är tillagt i dina relativa sökvägar kommer du att klara kontrollen.

Om inte kan du få följande felmeddelande.

![GitHub kontrollera saknad spårning i sökvägar skärmdump](../../translated_images/sv/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Skärmdump från GitHub-kommentar som visar saknad spårning i relativa sökvägar")

För att åtgärda detta öppna filvägen som arbetsflödet markerat och lägg till spårnings-ID i slutet av de relativa sökvägarna.

När du lagt till spårnings-ID, spara och pusha dina ändringar så triggas arbetsflödet igen för att verifiera ändringarna.
Om du klarar kontrollen är du redo att gå vidare.

### Kontrollera att URL:er har spårning

Detta arbetsflöde säkerställer att alla webbadresser har spårning i sig.
Detta repo är tillgängligt för alla, så du behöver säkerställa att spårningen finns för att veta var trafiken kommer ifrån.

För att försäkra dig om att dina URL:er har spårning, kontrollera helt enkelt efter texten `?wt.mc_id=` i slutet av URL:en.
Om den är tillagd i dina URL:er kommer du att klara kontrollen.

Om inte kan du få följande felmeddelande.

![GitHub kontrollera saknad spårning i URL:er skärmdump](../../translated_images/sv/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Skärmdump från GitHub-kommentar som visar saknad spårning i URL:er")

För att åtgärda detta öppna filvägen arbetsflödet markerade och lägg till spårnings-ID i slutet av URL:erna.

När du lagt till spårnings-ID, spara och pusha dina ändringar så triggas arbetsflödet igen för att verifiera ändringarna.
Om du klarar kontrollen är du redo att gå vidare.

### Kontrollera att URL:er inte har lokal

Detta arbetsflöde säkerställer att inga webbadresser innehåller landspecifik lokal.
Detta repo är tillgängligt för alla i världen, så du måste se till att inte inkludera ditt lands lokal i URL:erna.

För att se till att URL:erna inte har landslokal, kontrollera helt enkelt efter texten `/en-us/` eller `/en/` eller någon annan språklokal var som helst i URL:en.
Om det inte finns med i dina URL:er kommer du att klara kontrollen.

Om inte kan du få följande felmeddelande.

![GitHub kontrollera landslokal komentar skärmdump](../../translated_images/sv/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Skärmdump från GitHub-kommentar som visar tillagd landslokal i URL:er")

För att åtgärda detta, öppna filvägen som arbetsflödet markerade och ta bort landslokalen från URL:erna.

När du tagit bort landslokalen, spara och pusha dina ändringar så triggas arbetsflödet igen för att verifiera ändringarna.
Om du klarar kontrollen är du redo att gå vidare.

Grattis! Vi återkommer så snart som möjligt med feedback om ditt bidrag.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->