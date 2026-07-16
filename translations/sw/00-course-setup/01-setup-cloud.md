# Usanidi wa Wingu ☁️ – GitHub Codespaces

**Tumia mwongozo huu ikiwa hutaki kusakinisha chochote ndani ya mfumo wako.**  
Codespaces inakupa toleo la VS Code linalotumia kivinjari, lisilo na malipo, lenye utegemezi wote tayari kusakinishwa.

---

## 1.  Kwa nini Codespaces?

| Faida | Inamaanisha nini kwako |
|---------|----------------------|
| ✅ Hakuna usakinishaji | Inaweza kutumika kwenye Chromebook, iPad, kompyuta za maabara shuleni… |
| ✅ Kontena la maendeleo lililojengiwa tayari | Python 3, Node.js, .NET, Java tayari ndani |
| ✅ Kiasi cha bure cha matumizi | Akaunti binafsi hupata **masaa 120 ya cores / masaa 60 ya GB kwa mwezi** |

> 💡 **Shauri**  
> Weka kiasi chako kuwa kizuri kwa **kusitisha** au **kufuta** codespaces zisizotumika  
> (Tazama ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Tengeneza Codespace (bonyeza moja)

1. **Fanya Fork** kwenye repo hii (kitufe cha juu-kulia **Fork**).  
2. Katika fork yako, bonyeza **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog showing buttons to create a codespace](../../../translated_images/sw/who-will-pay.4c0609b1c7780f44.webp)

✅ Dirisha la VS Code katika kivinjari linafunguka na kontena la maendeleo linaanza kujengwa.
Hili huchukua takriban **dakika 2** mara ya kwanza.

## 3. Ongeza ufunguo wako wa API (njia salama)

### Chaguo A Siri za Codespaces — Inapendekezwa

1. ⚙️ Ikoni ya gia -> Command Palette -> Codespaces : Manage user secret -> Ongeza siri mpya.
2. Jina: OPENAI_API_KEY
3. Thamani: bandika ufunguo wako → Ongeza siri

Hilo ndilo tu—msimbo wetu utaichukua moja kwa moja.

### Chaguo B Faili la .env (ikiwa unahitaji kwa dhati)

```bash
cp .env.copy .env
code .env         # jaza OPENAI_API_KEY=ufunguo_wako_hapa
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->