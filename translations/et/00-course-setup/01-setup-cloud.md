<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-10-11T11:44:06+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "et"
}
-->
# Pilve seadistamine ☁️ – GitHub Codespaces

**Kasuta seda juhendit, kui sa ei soovi midagi kohapeal installida.**  
Codespaces pakub tasuta, brauseripõhist VS Code'i instantsi, kus kõik sõltuvused on eelinstallitud.

---

## 1.  Miks kasutada Codespaces?

| Eelis | Mida see sinu jaoks tähendab |
|-------|-----------------------------|
| ✅ Null installimist | Töötab Chromebookil, iPadil, kooli arvutiklassi arvutitel jne. |
| ✅ Eelkonfigureeritud arenduskonteiner | Python 3, Node.js, .NET, Java juba sees |
| ✅ Tasuta kvoot | Isiklikud kontod saavad **120 tuuma-tundi / 60 GB-tundi kuus** |

> 💡 **Nõuanne**  
> Hoia oma kvoot korras, **peatades** või **kustutades** kasutamata codespaces'id  
> (Vaade ▸ Käsupalett ▸ *Codespaces: Stop Codespace*).

---

## 2.  Loo Codespace (üks klõps)

1. **Forki** see repo (paremal üleval **Fork** nupp).  
2. Oma forkis klõpsa **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialoog, mis näitab nuppe codespace'i loomiseks](../../../00-course-setup/images/who-will-pay.webp)

✅ Avaneb brauseri VS Code aken ja arenduskonteiner hakkab ehitama.  
Esimesel korral võtab see aega **~2 minutit**.

## 3. Lisa oma API võti (turvaliselt)

### Variant A Codespaces Secrets — Soovitatav

1. ⚙️ Hammasratta ikoon -> Käsupalett -> Codespaces : Manage user secret -> Lisa uus secret.  
2. Nimi: OPENAI_API_KEY  
3. Väärtus: kleebi oma võti → Lisa secret  

Ja ongi kõik—meie kood tuvastab selle automaatselt.

### Variant B .env fail (kui tõesti vajad seda)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.