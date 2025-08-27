<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T18:38:29+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "sw"
}
-->
# Mpangilio wa Wingu ☁️ – GitHub Codespaces

**Tumia mwongozo huu kama hutaki kusanidi chochote kwenye kompyuta yako.**  
Codespaces inakupa toleo la VS Code kupitia kivinjari, tayari na utegemezi wote umewekwa.

---

## 1.  Kwa nini Codespaces?

| Faida | Maana yake kwako |
|---------|----------------------|
| ✅ Hakuna usakinishaji | Inafanya kazi kwenye Chromebook, iPad, PC za maabara ya shule… |
| ✅ Kontena la maendeleo limejengwa tayari | Python 3, Node.js, .NET, Java vipo tayari ndani |
| ✅ Kipimo cha bure | Akaunti binafsi zinapata **masaa 120 ya msingi / masaa 60 ya GB kwa mwezi** |

> 💡 **Kidokezo**  
> Linda kipimo chako kwa **kusimamisha** au **kufuta** codespaces ambazo hazitumiki  
> (Tazama ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Tengeneza Codespace (bonyeza mara moja)

1. **Fork** repozitori hii (kitufe cha juu kulia cha **Fork**).  
2. Kwenye fork yako, bonyeza **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![ialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Dirisha la VS Code kwenye kivinjari linafunguka na kontena la maendeleo linaanza kujengwa.
Hii huchukua **~dakika 2** mara ya kwanza.

## 3. Ongeza API key yako (njia salama)

### Chaguo A Siri za Codespaces — Inapendekezwa

1. ⚙️ Piga alama ya gia -> Command Pallete-> Codespaces : Manage user secret -> Ongeza siri mpya.
2. Jina: OPENAI_API_KEY
3. Thamani: bandika ufunguo wako → Ongeza siri

Basi—msimbo wetu utaitambua moja kwa moja.

### Chaguo B Faili la .env (kama kweli unahitaji)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya utafsiri wa binadamu wa kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.