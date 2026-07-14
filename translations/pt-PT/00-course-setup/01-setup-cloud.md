# Configuração na Nuvem ☁️ – GitHub Codespaces

**Use este guia se não quiser instalar nada localmente.**  
O Codespaces oferece-lhe uma instância gratuita do VS Code baseada no navegador com todas as dependências pré-instaladas.

---

## 1.  Porquê o Codespaces?

| Benefício | O que isso significa para si |
|---------|----------------------------|
| ✅ Zero instalações | Funciona em Chromebook, iPad, PCs do laboratório da escola... |
| ✅ Contentor de desenvolvimento pré-construído | Python 3, Node.js, .NET, Java já incluídos |
| ✅ Quota gratuita | Contas pessoais recebem **120 horas-core / 60 GB-horas por mês** |

> 💡 **Dica**  
> Mantenha a sua quota saudável **parando** ou **apagando** codespaces inativos  
> (Ver ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Criar um Codespace (com um clique)

1. **Faça fork** deste repositório (botão **Fork** no canto superior-direito).  
2. No seu fork, clique **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog showing buttons to create a codespace](../../../translated_images/pt-PT/who-will-pay.4c0609b1c7780f44.webp)

✅ Abrirá uma janela do VS Code no navegador e o contentor de desenvolvimento começará a ser construído.
Isto demora **~2 minutos** na primeira vez.

## 3. Adicione a sua chave API (da forma segura)

### Opção A Segredos Codespaces — Recomendado

1. ⚙️ Ícone de engrenagem -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Nome: OPENAI_API_KEY
3. Valor: cole a sua chave → Add secret

É tudo – o nosso código irá usá-la automaticamente.

### Opção B ficheiro .env (se realmente precisar)

```bash
cp .env.copy .env
code .env         # preencha OPENAI_API_KEY=sua_chave_aqui
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->