<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T16:30:02+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "it"
}
-->
# Configurazione Cloud ☁️ – GitHub Codespaces

**Usa questa guida se non vuoi installare nulla sul tuo computer.**  
Codespaces ti offre una versione gratuita di VS Code nel browser, con tutte le dipendenze già installate.

---

## 1.  Perché Codespaces?

| Vantaggio | Cosa significa per te |
|-----------|----------------------|
| ✅ Nessuna installazione | Funziona su Chromebook, iPad, PC dei laboratori scolastici… |
| ✅ Dev container preconfigurato | Python 3, Node.js, .NET, Java già inclusi |
| ✅ Quota gratuita | Gli account personali hanno **120 core-ore / 60 GB-ore al mese** |

> 💡 **Suggerimento**  
> Mantieni la tua quota in salute **arrestando** o **eliminando** i codespace inattivi  
> (Visualizza ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Crea un Codespace (un solo clic)

1. **Forka** questo repository (pulsante **Fork** in alto a destra).  
2. Nel tuo fork, clicca su **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Finestra di dialogo che mostra i pulsanti per creare un codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Si aprirà una finestra di VS Code nel browser e il dev container inizierà a configurarsi.
La prima volta ci vorranno circa **2 minuti**.

## 3. Aggiungi la tua API key (in modo sicuro)

### Opzione A Secrets di Codespaces — Consigliato

1. ⚙️ Icona ingranaggio -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Nome: OPENAI_API_KEY
3. Valore: incolla la tua chiave → Add secret

Fatto—il nostro codice la rileverà automaticamente.

### Opzione B File .env (se proprio ti serve)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.