# Molninställning ☁️ – GitHub Codespaces

**Använd denna guide om du inte vill installera något lokalt.**  
Codespaces ger dig en kostnadsfri VS Code-instans i webbläsaren med alla beroenden förinstallerade.

---

## 1.  Varför Codespaces?

| Fördel | Vad det betyder för dig |
|---------|----------------------|
| ✅ Inga installationer | Fungerar på Chromebook, iPad, skolans labbdatorer… |
| ✅ Förbyggd utvecklingscontainer | Python 3, Node.js, .NET, Java redan inuti |
| ✅ Kostnadsfri kvot | Personliga konton får **120 core-timmar / 60 GB-timmar per månad** |

> 💡 **Tips**  
> Håll din kvot hälsosam genom att **stoppa** eller **ta bort** inaktiva codespaces  
> (Visa ▸ Kommandopalett ▸ *Codespaces: Stoppa Codespace*).

---

## 2.  Skapa en Codespace (ett klick)

1. **Forka** detta repo (knappen **Fork** uppe till höger).  
2. I din fork, klicka **Code ▸ Codespaces ▸ Skapa codespace på main**.  
   ![Dialog som visar knappar för att skapa en codespace](../../../translated_images/sv/who-will-pay.4c0609b1c7780f44.webp)

✅ Ett webbläsarfönster för VS Code öppnas och utvecklingscontainern börjar byggas.
Detta tar **~2 minuter** första gången.

## 3. Lägg till din API-nyckel (det säkra sättet)

### Alternativ A Codespaces Secrets — Rekommenderat

1. ⚙️ Kugghjulsikon -> Kommandopalett -> Codespaces : Hantera användarhemlighet -> Lägg till en ny hemlighet.
2. Namn: OPENAI_API_KEY
3. Värde: klistra in din nyckel → Lägg till hemlighet

Det är allt—vår kod plockar upp den automatiskt.

### Alternativ B .env-fil (om du verkligen behöver en)

```bash
cp .env.copy .env
code .env         # fyll i OPENAI_API_KEY=ditt_nyckel_här
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->