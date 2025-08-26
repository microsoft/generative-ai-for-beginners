<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T17:33:00+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "no"
}
-->
# Cloud-oppsett ☁️ – GitHub Codespaces

**Bruk denne guiden hvis du ikke vil installere noe lokalt.**  
Codespaces gir deg en gratis, nettleserbasert VS Code-instans med alle avhengigheter ferdig installert.

---

## 1.  Hvorfor Codespaces?

| Fordel | Hva betyr det for deg |
|--------|----------------------|
| ✅ Ingen installasjoner | Fungerer på Chromebook, iPad, skole-PCer osv. |
| ✅ Ferdigbygd utviklingscontainer | Python 3, Node.js, .NET, Java er allerede inkludert |
| ✅ Gratis kvote | Personlige kontoer får **120 kjernetimer / 60 GB-timer per måned** |

> 💡 **Tip**  
> Hold kvoten din sunn ved å **stoppe** eller **slette** inaktive codespaces  
> (Vis ▸ Kommandopalett ▸ *Codespaces: Stop Codespace*).

---

## 2.  Opprett en Codespace (ett klikk)

1. **Fork** dette repoet (øverst til høyre, **Fork**-knappen).  
2. I din fork, klikk **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog som viser knapper for å opprette en codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Et VS Code-vindu åpnes i nettleseren og utviklingscontaineren begynner å bygges.
Dette tar **ca. 2 minutter** første gang.

## 3. Legg til din API-nøkkel (på en trygg måte)

### Alternativ A Codespaces Secrets — Anbefalt

1. ⚙️ Gir-ikon -> Kommandopalett -> Codespaces : Manage user secret -> Add a new secret.
2. Navn: OPENAI_API_KEY
3. Verdi: lim inn nøkkelen din → Add secret

Det er alt—koden vår finner den automatisk.

### Alternativ B .env-fil (hvis du virkelig trenger det)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.