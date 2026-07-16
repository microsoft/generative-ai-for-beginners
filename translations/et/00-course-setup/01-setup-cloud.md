# Pilve seadistamine ☁️ – GitHub Codespaces

**Kasuta seda juhendit, kui sa ei taha midagi kohapeal installeerida.**  
Codespaces annab sulle tasuta brauseripõhise VS Code' i eksemplari koos kõigi eelinstalleeritud sõltuvustega.

---

## 1.  Miks kasutada Codespaces?

| Kasu | Mida see sinu jaoks tähendab |
|---------|----------------------|
| ✅ Installeerimist pole vaja | Toimib Chromebookil, iPad'il, koolilabori arvutites… |
| ✅ Eelvalmistatud arenduskonteiner | Python 3, Node.js, .NET, Java juba sees |
| ✅ Tasuta limiit | Isiklikud kontod saavad **120 tuum-tundi / 60 GB-tundi kuus** |

> 💡 **Nipp**  
> Hoia oma limiit korras, **peatades** või **kustutades** tühikäigul olevad codespaces'id  
> (Vaata ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Loo Codespace (üks klõps)

1. **Forki** see repo (paremas ülanurgas **Fork** nupp).  
2. Oma forgis klõpsa **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialoog, mis näitab koode ruumi loomiseks vajalikke nuppe](../../../translated_images/et/who-will-pay.4c0609b1c7780f44.webp)

✅ Avaneb brauseri VS Code aken ja arenduskonteiner hakkab ehitama.
Esimene kord võtab see umbes **2 minutit**.

## 3. Lisa oma API võti (ohutu meetod)

### Variant A Codespaces Secrets — Soovitatav

1. ⚙️ Hammasratas -> Command Palette -> Codespaces : Manage user secret -> Lisa uus saladus.
2. Nimi: OPENAI_API_KEY
3. Väärtus: kleebi oma võti → Lisa saladus

See on kõik—meie kood kasutab seda automaatselt.

### Variant B .env fail (kui tõesti vajad)

```bash
cp .env.copy .env
code .env         # täitke OPENAI_API_KEY=teie_võti_siia
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->