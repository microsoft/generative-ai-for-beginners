<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T17:15:36+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "sv"
}
-->
# Molninstallation ☁️ – GitHub Codespaces

**Använd den här guiden om du inte vill installera något lokalt.**  
Codespaces ger dig en gratis, webbaserad VS Code-miljö med alla beroenden förinstallerade.

---

## 1.  Varför Codespaces?

| Fördel | Vad det betyder för dig |
|--------|------------------------|
| ✅ Inga installationer | Fungerar på Chromebook, iPad, skolans datorer… |
| ✅ Färdigutvecklad dev-container | Python 3, Node.js, .NET, Java finns redan med |
| ✅ Gratis användning | Personliga konton får **120 kärntimmar / 60 GB-timmar per månad** |

> 💡 **Tip**  
> Håll koll på din användning genom att **stoppa** eller **ta bort** inaktiva codespaces  
> (Visa ▸ Kommandopalett ▸ *Codespaces: Stop Codespace*).

---

## 2.  Skapa en Codespace (ett klick)

1. **Forka** detta repo (uppe till höger, **Fork**-knappen).  
2. I din fork, klicka på **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialogruta med knappar för att skapa en codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Ett VS Code-fönster öppnas i webbläsaren och dev-containern börjar byggas.
Detta tar **ungefär 2 minuter** första gången.

## 3. Lägg till din API-nyckel (på ett säkert sätt)

### Alternativ A Codespaces Secrets — Rekommenderas

1. ⚙️ Kugghjulsikon -> Kommandopalett -> Codespaces : Manage user secret -> Add a new secret.
2. Namn: OPENAI_API_KEY
3. Värde: klistra in din nyckel → Add secret

Klart—vår kod hittar den automatiskt.

### Alternativ B .env-fil (om du verkligen behöver en)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.