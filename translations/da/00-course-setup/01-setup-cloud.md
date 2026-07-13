# Cloud Opsætning ☁️ – GitHub Codespaces

**Brug denne guide, hvis du ikke vil installere noget lokalt.**  
Codespaces giver dig en gratis, browserbaseret VS Code-instans med alle afhængigheder forudinstalleret.

---

## 1.  Hvorfor Codespaces?

| Fordel | Hvad det betyder for dig |
|---------|--------------------------|
| ✅ Ingen installationer | Virker på Chromebook, iPad, skole-laboratorie-pc’er… |
| ✅ Forudbygget udviklingscontainer | Python 3, Node.js, .NET, Java allerede inkluderet |
| ✅ Gratis kvote | Personlige konti får **120 kerne-timer / 60 GB-timer pr. måned** |

> 💡 **Tip**  
> Hold din kvote sund ved at **stoppe** eller **slette** inaktive codespaces  
> (Vis ▸ Kommandopalette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Opret en Codespace (et klik)

1. **Fork** dette repo (øverst til højre **Fork**-knap).  
2. I dit fork, klik **Kode ▸ Codespaces ▸ Opret codespace på main**.  
   ![Dialog der viser knapper til at oprette en codespace](../../../translated_images/da/who-will-pay.4c0609b1c7780f44.webp)

✅ Et browser-VS Code-vindue åbnes, og udviklingscontaineren begynder at bygge.
Dette tager **~2 minutter** første gang.

## 3. Tilføj din API-nøgle (den sikre måde)

### Mulighed A Codespaces Secrets — Anbefalet

1. ⚙️ Tandhjulsikon -> Kommandopalette -> Codespaces : Administrer brugerhemmelighed -> Tilføj en ny hemmelighed.
2. Navn: OPENAI_API_KEY
3. Værdi: indsæt din nøgle → Tilføj hemmelighed

Det var det—vores kode vil automatisk hente den.

### Mulighed B .env-fil (hvis du virkelig har brug for en)

```bash
cp .env.copy .env
code .env         # udfyld OPENAI_API_KEY=din_nøgle_her
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->