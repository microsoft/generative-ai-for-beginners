# Configurazione Cloud ☁️ – GitHub Codespaces

**Usa questa guida se non vuoi installare nulla in locale.**  
Codespaces ti offre un'istanza VS Code gratuita basata su browser con tutte le dipendenze preinstallate.

---

## 1.  Perché Codespaces?

| Vantaggio | Cosa significa per te |
|---------|----------------------|
| ✅ Zero installazioni | Funziona su Chromebook, iPad, PC di laboratorio scolastico… |
| ✅ Contenitore di sviluppo pre-configurato | Python 3, Node.js, .NET, Java già all'interno |
| ✅ Quota gratuita | Gli account personali ricevono **120 core-ore / 60 GB-ore al mese** |

> 💡 **Consiglio**  
> Mantieni la tua quota sana **fermandosi** o **eliminando** i codespaces inattivi  
> (Visualizza ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Crea un Codespace (con un clic)

1. **Forka** questo repo (pulsante **Fork** in alto a destra).  
2. Nel tuo fork, clicca **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog showing buttons to create a codespace](../../../translated_images/it/who-will-pay.4c0609b1c7780f44.webp)

✅ Si apre una finestra di VS Code nel browser e il contenitore di sviluppo inizia a costruirsi.
Questo richiede **~2 minuti** la prima volta.

## 3. Aggiungi la tua chiave API (il modo sicuro)

### Opzione A Secrets di Codespaces — Consigliato

1. ⚙️ Icona ingranaggio -> Command Palette -> Codespaces : Gestisci segreto utente -> Aggiungi un nuovo segreto.
2. Nome: OPENAI_API_KEY
3. Valore: incolla la tua chiave → Aggiungi segreto

Fatto—il nostro codice la rileverà automaticamente.

### Opzione B file .env (se proprio ti serve)

```bash
cp .env.copy .env
code .env         # inserisci OPENAI_API_KEY=tua_chiave_qua
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->