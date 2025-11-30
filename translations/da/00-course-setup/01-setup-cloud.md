<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T17:24:32+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "da"
}
-->
# Cloud-opsætning ☁️ – GitHub Codespaces

**Brug denne guide, hvis du ikke vil installere noget lokalt.**  
Codespaces giver dig en gratis, browserbaseret VS Code-instans med alle afhængigheder forudinstalleret.

---

## 1.  Hvorfor Codespaces?

| Fordel | Hvad betyder det for dig |
|--------|-------------------------|
| ✅ Ingen installationer | Fungerer på Chromebook, iPad, skolecomputere osv. |
| ✅ Forudbygget udviklingscontainer | Python 3, Node.js, .NET, Java er allerede med |
| ✅ Gratis kvote | Personlige konti får **120 kerne-timer / 60 GB-timer pr. måned** |

> 💡 **Tip**  
> Hold din kvote sund ved at **stoppe** eller **slette** inaktive codespaces  
> (Vis ▸ Kommandopaletten ▸ *Codespaces: Stop Codespace*).

---

## 2.  Opret et Codespace (ét klik)

1. **Fork** dette repo (øverst til højre, **Fork**-knappen).  
2. I din fork, klik på **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog der viser knapper til at oprette et codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Et VS Code-vindue åbner i browseren, og udviklingscontaineren begynder at bygge.
Det tager **~2 minutter** første gang.

## 3. Tilføj din API-nøgle (den sikre måde)

### Mulighed A Codespaces Secrets — Anbefales

1. ⚙️ Tandhjulsikon -> Kommandopaletten -> Codespaces : Manage user secret -> Add a new secret.
2. Navn: OPENAI_API_KEY
3. Værdi: indsæt din nøgle → Add secret

Så er du klar—vores kode finder den automatisk.

### Mulighed B .env-fil (hvis du virkelig har brug for det)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.