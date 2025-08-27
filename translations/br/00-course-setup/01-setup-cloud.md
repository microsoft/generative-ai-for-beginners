<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T16:22:15+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "br"
}
-->
# Configuração na Nuvem ☁️ – GitHub Codespaces

**Use este guia se você não quiser instalar nada localmente.**  
O Codespaces oferece uma instância gratuita do VS Code no navegador, com todas as dependências já instaladas.

---

## 1.  Por que usar Codespaces?

| Benefício | O que isso significa para você |
|-----------|-------------------------------|
| ✅ Sem instalações | Funciona em Chromebook, iPad, PCs de laboratório da escola… |
| ✅ Container de desenvolvimento pré-configurado | Python 3, Node.js, .NET, Java já inclusos |
| ✅ Cota gratuita | Contas pessoais recebem **120 core-hours / 60 GB-hours por mês** |

> 💡 **Dica**  
> Mantenha sua cota em dia **parando** ou **excluindo** codespaces que não estiver usando  
> (Exibir ▸ Paleta de Comandos ▸ *Codespaces: Stop Codespace*).

---

## 2.  Crie um Codespace (um clique)

1. **Faça um fork** deste repositório (canto superior direito, botão **Fork**).  
2. No seu fork, clique em **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Diálogo mostrando botões para criar um codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Uma janela do VS Code no navegador será aberta e o container de desenvolvimento começará a ser criado.
Isso leva **cerca de 2 minutos** na primeira vez.

## 3. Adicione sua chave de API (de forma segura)

### Opção A Segredos do Codespaces — Recomendado

1. Ícone de engrenagem ⚙️ -> Paleta de Comandos -> Codespaces : Manage user secret -> Add a new secret.
2. Nome: OPENAI_API_KEY
3. Valor: cole sua chave → Add secret

Pronto—nosso código vai detectar automaticamente.

### Opção B Arquivo .env (se você realmente precisar de um)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.