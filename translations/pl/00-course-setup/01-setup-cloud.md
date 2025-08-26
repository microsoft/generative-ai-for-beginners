<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T16:38:05+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "pl"
}
-->
# Konfiguracja w chmurze ☁️ – GitHub Codespaces

**Skorzystaj z tego przewodnika, jeśli nie chcesz niczego instalować lokalnie.**  
Codespaces udostępnia darmową, przeglądarkową wersję VS Code ze wszystkimi potrzebnymi zależnościami już zainstalowanymi.

---

## 1.  Dlaczego Codespaces?

| Korzyść | Co to dla Ciebie oznacza |
|---------|-------------------------|
| ✅ Brak instalacji | Działa na Chromebooku, iPadzie, komputerach w szkolnej pracowni… |
| ✅ Gotowy kontener deweloperski | Python 3, Node.js, .NET, Java już w środku |
| ✅ Darmowy limit | Konta osobiste mają **120 core-godzin / 60 GB-godzin miesięcznie** |

> 💡 **Tip**  
> Dbaj o swój limit, **zatrzymując** lub **usuwając** nieużywane codespaces  
> (Widok ▸ Paleta poleceń ▸ *Codespaces: Stop Codespace*).

---

## 2.  Utwórz Codespace (jednym kliknięciem)

1. **Forkuj** to repozytorium (przycisk **Fork** w prawym górnym rogu).  
2. W swoim forku kliknij **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Okno dialogowe z przyciskami do utworzenia codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Otworzy się okno VS Code w przeglądarce i rozpocznie się budowanie kontenera deweloperskiego.
Za pierwszym razem trwa to **około 2 minut**.

## 3. Dodaj swój klucz API (bezpiecznie)

### Opcja A Sekrety Codespaces — Zalecane

1. ⚙️ Ikona koła zębatego -> Paleta poleceń -> Codespaces : Manage user secret -> Add a new secret.
2. Nazwa: OPENAI_API_KEY
3. Wartość: wklej swój klucz → Add secret

To wszystko — nasz kod sam go wykryje.

### Opcja B Plik .env (jeśli naprawdę go potrzebujesz)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było dokładne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego ojczystym języku powinien być traktowany jako źródło nadrzędne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnych usług tłumaczeniowych. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.