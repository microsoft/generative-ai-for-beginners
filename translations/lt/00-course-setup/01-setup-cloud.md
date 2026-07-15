# Debesų nustatymas ☁️ – GitHub Codespaces

**Naudokite šią gaires, jei nenorite nieko diegti vietoje.**  
Codespaces suteikia nemokamą, naršyklėje veikiančią VS Code versiją su visomis išankstiniais įdiegtais priklausomybėmis.

---

## 1.  Kodėl Codespaces?

| Privalumas | Ką tai reiškia jums |
|---------|----------------------|
| ✅ Nuliniai diegimai | Veikia Chromebook'uose, iPaduose, mokyklos laboratorijos kompiuteriuose… |
| ✅ Iš anksto paruoštas kūrimo konteineris | Python 3, Node.js, .NET, Java jau viduje |
| ✅ Nemokamas kvotas | Asmeniniai paskyros vartotojai gauna **120 branduolių valandų / 60 GB valandų per mėnesį** |

> 💡 **Patarimas**  
> Išlaikykite savo kvotą sveiką, **sustabdykite** arba **ištrinkite** nenaudojamus codespaces  
> (Peržiūrėti ▸ Komandų paletė ▸ *Codespaces: Stop Codespace*).

---

## 2.  Sukurkite Codespace (vienu paspaudimu)

1. **Sukurti šaką** (dešinėje viršuje mygtukas **Fork**).  
2. Jūsų šakoje spustelėkite **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialogo langas, rodantis mygtukus codespace kūrimui](../../../translated_images/lt/who-will-pay.4c0609b1c7780f44.webp)

✅ Atsidarys naršyklėje veikiantis VS Code langas ir pradės kasti kūrimo konteinerį.
Tai užtrunka **~2 minutes** pirmą kartą.

## 3. Pridėkite savo API raktą (saugus būdas)

### A variantas: Codespaces Secrets — rekomenduojama

1. ⚙️ Pavarėlės ikonėlė -> Komandų paletė -> Codespaces : Valdyti vartotojo slaptus duomenis -> Pridėti naują slaptažodį.
2. Pavadinimas: OPENAI_API_KEY
3. Reikšmė: įdėkite savo raktą → Pridėti slaptažodį

Viskas — mūsų kodas tai automatiškai paims.

### B variantas: .env failas (jei tikrai reikia)

```bash
cp .env.copy .env
code .env         # įrašykite OPENAI_API_KEY=jūsų_atslēga_čia
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->