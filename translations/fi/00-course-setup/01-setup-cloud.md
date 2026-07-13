# Pilviasennus ☁️ – GitHub Codespaces

**Käytä tätä opasta, jos et halua asentaa mitään paikallisesti.**  
Codespaces tarjoaa sinulle ilmaisen, selaimessa toimivan VS Code -instanssin, jossa on esiasennetut kaikki riippuvuudet.

---

## 1. Miksi Codespaces?

| Etu | Mitä se tarkoittaa sinulle |
|---------|----------------------|
| ✅ Ei asennuksia | Toimii Chromebookilla, iPadilla, koulun työasemilla… |
| ✅ Esirakennettu kehityssäiliö | Python 3, Node.js, .NET, Java valmiina sisällä |
| ✅ Ilmainen käyttökyky | Henkilökohtaiset tilit saavat **120 ydin-tuntia / 60 GB-tuntia kuukaudessa** |

> 💡 **Vinkki**  
> Pidä käyttökyky hyvänä **pysäyttämällä** tai **poistamalla** käyttämättä olevat codespacet  
> (Näkyvyys ▸ Komentopaletti ▸ *Codespaces: Stop Codespace*).

---

## 2. Luo Codespace (yhdellä napsautuksella)

1. **Forkkaa** tämä repositorio (oikean yläkulman **Fork**-painike).  
2. Forkissasi napsauta **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog showing buttons to create a codespace](../../../translated_images/fi/who-will-pay.4c0609b1c7780f44.webp)

✅ Selaimeen avautuu VS Code -ikkuna ja kehityssäiliö alkaa rakentua.
Tämä kestää **~2 minuuttia** ensimmäisellä kerralla.

## 3. Lisää API-avain (turvallinen tapa)

### Vaihtoehto A Codespaces Secrets — Suositeltu

1. ⚙️ Ratas-kuvake -> Komentopaletti -> Codespaces: Hallitse käyttäjän salaista -> Lisää uusi salainen.
2. Nimi: OPENAI_API_KEY
3. Arvo: liitä avain → Lisää salainen

Siinä kaikki—koodimme poimii sen automaattisesti.

### Vaihtoehto B .env-tiedosto (jos sitä todella tarvitset)

```bash
cp .env.copy .env
code .env         # täytä OPENAI_API_KEY=avaimesi_tähän
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->