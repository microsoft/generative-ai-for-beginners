# Cloud-oppsett ☁️ – GitHub Codespaces

**Bruk denne guiden hvis du ikke vil installere noe lokalt.**  
Codespaces gir deg en gratis, nettleserbasert VS Code-instans med alle avhengigheter forhåndsinstallert.

---

## 1.  Hvorfor Codespaces?

| Fordel | Hva det betyr for deg |
|---------|-----------------------|
| ✅ Ingen installasjoner | Fungerer på Chromebook, iPad, skole-laboratorie-PCer… |
| ✅ Ferdiglaget utviklingscontainer | Python 3, Node.js, .NET, Java er allerede inne |
| ✅ Gratis kvote | Personlige kontoer får **120 core-timer / 60 GB-timer per måned** |

> 💡 **Tips**  
> Hold kvoten din sunn ved å **stoppe** eller **slette** inaktive codespaces  
> (Se ▸ Kommando-palett ▸ *Codespaces: Stopp Codespace*).

---

## 2.  Opprett en Codespace (ett klikk)

1. **Fork** dette repoet (øverst til høyre **Fork**-knappen).  
2. I ditt fork, klikk **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog som viser knapper for å opprette en codespace](../../../translated_images/no/who-will-pay.4c0609b1c7780f44.webp)

✅ Et nettleservindu med VS Code åpnes, og utviklingscontaineren begynner å bygges.
Dette tar **~2 minutter** første gangen.

## 3. Legg til din API-nøkkel (den sikre måten)

### Alternativ A Codespaces Secrets – Anbefalt

1. ⚙️ Gir-ikon -> Kommando-palett -> Codespaces : Administrer brukerhemmelighet -> Legg til en ny hemmelighet.
2. Navn: OPENAI_API_KEY
3. Verdi: lim inn nøkkelen din → Legg til hemmelighet

Det er det—vår kode vil hente den automatisk.

### Alternativ B .env-fil (hvis du virkelig trenger en)

```bash
cp .env.copy .env
code .env         # fyll inn OPENAI_API_KEY=dinnøkkel_her
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->