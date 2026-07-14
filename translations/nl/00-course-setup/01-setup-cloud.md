# Cloud Setup ☁️ – GitHub Codespaces

**Gebruik deze gids als je niets lokaal wilt installeren.**  
Codespaces geeft je een gratis, browsergebaseerde VS Code-omgeving met alle afhankelijkheden vooraf geïnstalleerd.

---

## 1. Waarom Codespaces?

| Voordeel | Wat het voor jou betekent |
|---------|-------------------------|
| ✅ Geen installatie | Werkt op Chromebook, iPad, schoollab-pc's… |
| ✅ Vooraf gebouwde ontwikkelcontainer | Python 3, Node.js, .NET, Java al aanwezig |
| ✅ Gratis tegoed | Persoonlijke accounts krijgen **120 core-uren / 60 GB-uren per maand** |

> 💡 **Tip**  
> Houd je tegoed gezond door inactieve codespaces **te stoppen** of **te verwijderen**  
> (Bekijk ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2. Maak een Codespace aan (met één klik)

1. **Fork** deze repo (bovenaan rechts op de knop **Fork**).  
2. Klik in je fork op **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialoogvenster dat knoppen toont om een codespace te maken](../../../translated_images/nl/who-will-pay.4c0609b1c7780f44.webp)

✅ Een VS Code-venster in de browser opent en de ontwikkelcontainer begint te bouwen.
Dit duurt de eerste keer ongeveer **~2 minuten**.

## 3. Voeg je API-sleutel toe (de veilige manier)

### Optie A Codespaces Secrets — Aanbevolen

1. ⚙️ Tandwielicoon -> Command Pallet -> Codespaces : Manage user secret -> Voeg een nieuwe secret toe.
2. Naam: OPENAI_API_KEY
3. Waarde: plak je sleutel → Voeg secret toe

Dat is alles—onze code zal het automatisch oppikken.

### Optie B .env bestand (als je er echt eentje nodig hebt)

```bash
cp .env.copy .env
code .env         # vul OPENAI_API_KEY=je_sleutel_hier_in
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->