<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T17:48:58+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "nl"
}
-->
# Cloud Setup ☁️ – GitHub Codespaces

**Gebruik deze gids als je niets lokaal wilt installeren.**  
Codespaces biedt je een gratis, browser-gebaseerde VS Code-omgeving met alle benodigde afhankelijkheden al geïnstalleerd.

---

## 1.  Waarom Codespaces?

| Voordeel | Wat betekent het voor jou |
|----------|--------------------------|
| ✅ Geen installaties nodig | Werkt op Chromebook, iPad, schoolcomputers… |
| ✅ Vooraf gebouwde ontwikkelcontainer | Python 3, Node.js, .NET, Java zitten er al in |
| ✅ Gratis tegoed | Persoonlijke accounts krijgen **120 core-uren / 60 GB-uren per maand** |

> 💡 **Tip**  
> Houd je tegoed gezond door **niet-gebruikte codespaces te stoppen of te verwijderen**  
> (Weergave ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Maak een Codespace (met één klik)

1. **Fork** deze repo (rechtsboven de knop **Fork**).  
2. In je fork, klik op **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialoogvenster met knoppen om een codespace te maken](../../../00-course-setup/images/who-will-pay.webp)

✅ Er opent een VS Code-venster in je browser en de ontwikkelcontainer wordt opgebouwd.
Dit duurt de **eerste keer ongeveer 2 minuten**.

## 3. Voeg je API-sleutel toe (op de veilige manier)

### Optie A Codespaces Secrets — Aanbevolen

1. ⚙️ Tandwiel-icoon -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Naam: OPENAI_API_KEY
3. Waarde: plak je sleutel → Add secret

Klaar—onze code vindt hem automatisch.

### Optie B .env-bestand (alleen als je er echt één nodig hebt)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.