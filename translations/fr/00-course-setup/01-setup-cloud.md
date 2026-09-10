# Configuration Cloud ☁️ – GitHub Codespaces

**Utilisez ce guide si vous ne voulez rien installer localement.**  
Codespaces vous offre une instance VS Code gratuite dans le navigateur avec toutes les dépendances préinstallées.

---

## 1. Pourquoi Codespaces ?

| Avantage | Ce que cela signifie pour vous |
|---------|------------------------------|
| ✅ Aucune installation | Fonctionne sur Chromebook, iPad, PC de laboratoire scolaire… |
| ✅ Conteneur de développement pré-construit | Python 3, Node.js, .NET, Java déjà inclus |
| ✅ Quota gratuit | Les comptes personnels obtiennent **120 heures-cœur / 60 Go-heure par mois** |

> 💡 **Astuce**  
> Gardez votre quota en bonne santé en **arrêtant** ou **supprimant** les codespaces inactifs  
> (Voir ▸ Palette de commandes ▸ *Codespaces : Arrêter Codespace*).

---

## 2. Créer un Codespace (en un clic)

1. **Forkez** ce repo (bouton **Fork** en haut à droite).  
2. Dans votre fork, cliquez sur **Code ▸ Codespaces ▸ Créer un codespace sur main**.  
   ![Dialog showing buttons to create a codespace](../../../translated_images/fr/who-will-pay.4c0609b1c7780f44.webp)

✅ Une fenêtre VS Code dans le navigateur s’ouvre et le conteneur de développement commence à se construire.
Cela prend environ **2 minutes** la première fois.

## 3. Ajoutez votre clé API (la méthode sécurisée)

### Option A Secrets Codespaces — Recommandé

1. ⚙️ Icône engrenage -> Palette de commandes -> Codespaces : Gérer le secret utilisateur -> Ajouter un nouveau secret.
2. Nom : OPENAI_API_KEY
3. Valeur : collez votre clé → Ajouter le secret

C’est tout — notre code la prendra automatiquement en compte.

### Option B Fichier .env (si vraiment nécessaire)

```bash
cp .env.copy .env
code .env         # remplissez OPENAI_API_KEY=votre_clef_ici
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->