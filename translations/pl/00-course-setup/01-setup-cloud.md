# Konfiguracja w chmurze ☁️ – GitHub Codespaces

**Użyj tego przewodnika, jeśli nie chcesz nic instalować lokalnie.**  
Codespaces oferuje bezpłatną instancję VS Code w przeglądarce ze wszystkimi preinstalowanymi zależnościami.

---

## 1. Dlaczego Codespaces?

| Korzyść | Co to oznacza dla Ciebie |
|---------|-------------------------|
| ✅ Zero instalacji | Działa na Chromebooku, iPadzie, szkolnych komputerach… |
| ✅ Gotowy kontener deweloperski | Python 3, Node.js, .NET, Java już w środku |
| ✅ Darmowy limit | Konta osobiste mają **120 godzin rdzenia / 60 GB-godzin miesięcznie** |

> 💡 **Wskazówka**  
> Dbaj o swój limit, **zatrzymując** lub **usuwając** bezczynne codespaces  
> (Widok ▸ Paleta poleceń ▸ *Codespaces: Stop Codespace*).

---

## 2. Utwórz Codespace (jedno kliknięcie)

1. **Utwórz fork** tego repozytorium (przycisk **Fork** w prawym górnym rogu).  
2. W swoim forku kliknij **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog pokazujący przyciski do tworzenia codespace](../../../translated_images/pl/who-will-pay.4c0609b1c7780f44.webp)

✅ Otworzy się okno VS Code w przeglądarce, a kontener deweloperski zacznie się budować.
To zajmuje **~2 minuty** za pierwszym razem.

## 3. Dodaj swój klucz API (bezpiecznie)

### Opcja A Kody tajne Codespaces — zalecane

1. ⚙️ Ikona koła zębatego -> Paleta poleceń -> Codespaces : Zarządzaj tajnymi danymi użytkownika -> Dodaj nowy sekret.
2. Nazwa: OPENAI_API_KEY
3. Wartość: wklej swój klucz → Dodaj sekret

To wszystko — nasz kod automatycznie go odczyta.

### Opcja B plik .env (jeśli naprawdę potrzebujesz)

```bash
cp .env.copy .env
code .env         # wprowadź OPENAI_API_KEY=twoj_klucz_tutaj
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->