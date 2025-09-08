<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T17:40:55+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "fi"
}
-->
# Pilviasennus ☁️ – GitHub Codespaces

**Käytä tätä ohjetta, jos et halua asentaa mitään omalle koneellesi.**  
Codespaces tarjoaa ilmaisen, selaimessa toimivan VS Code -ympäristön, jossa kaikki tarvittavat riippuvuudet on valmiiksi asennettu.

---

## 1.  Miksi Codespaces?

| Hyöty | Mitä se tarkoittaa sinulle |
|-------|---------------------------|
| ✅ Ei asennuksia | Toimii Chromebookilla, iPadilla, koulun tietokoneilla… |
| ✅ Esirakennettu kehitysympäristö | Python 3, Node.js, .NET, Java valmiina |
| ✅ Ilmainen käyttökiintiö | Henkilökohtaiset tilit saavat **120 core-tuntia / 60 GB-tuntia kuukaudessa** |

> 💡 **Vinkki**  
> Säästä kiintiötäsi **pysäyttämällä** tai **poistamalla** käyttämättömät codespacet  
> (Näytä ▸ Komentopaletti ▸ *Codespaces: Stop Codespace*).

---

## 2.  Luo Codespace (yhdellä klikkauksella)

1. **Forkkaa** tämä repo (yläoikealla **Fork**-painike).  
2. Forkissasi klikkaa **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![ialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Selainikkunassa avautuu VS Code ja kehitysympäristön rakentaminen alkaa.
Tämä kestää **noin 2 minuuttia** ensimmäisellä kerralla.

## 3. Lisää API-avaimesi (turvallisesti)

### Vaihtoehto A Codespaces Secrets — Suositeltu

1. ⚙️ Ratasikoni -> Komentopaletti -> Codespaces : Manage user secret -> Lisää uusi salaisuus.
2. Nimeä: OPENAI_API_KEY
3. Arvo: liitä avain → Add secret

Siinä kaikki—koodimme löytää avaimen automaattisesti.

### Vaihtoehto B .env-tiedosto (jos todella tarvitset sitä)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen omalla kielellä tulee pitää ensisijaisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinkäsityksistä tai tulkintavirheistä.