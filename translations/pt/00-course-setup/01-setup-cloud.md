<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T16:13:23+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "pt"
}
-->
# Configuração na Cloud ☁️ – GitHub Codespaces

**Use este guia se não quiser instalar nada no seu computador.**  
O Codespaces oferece-lhe uma instância gratuita do VS Code no navegador, já com todas as dependências instaladas.

---

## 1.  Porquê usar Codespaces?

| Vantagem | O que significa para si |
|----------|------------------------|
| ✅ Sem instalações | Funciona em Chromebook, iPad, computadores da escola… |
| ✅ Contentor de desenvolvimento pré-configurado | Python 3, Node.js, .NET, Java já incluídos |
| ✅ Quota gratuita | Contas pessoais têm **120 horas de núcleo / 60 GB-horas por mês** |

> 💡 **Tip**  
> Mantenha a sua quota em dia **parando** ou **eliminando** codespaces que não está a usar  
> (Ver ▸ Paleta de Comandos ▸ *Codespaces: Stop Codespace*).

---

## 2.  Criar um Codespace (um clique)

1. **Faça fork** deste repositório (botão **Fork** no canto superior direito).  
2. No seu fork, clique em **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Diálogo a mostrar botões para criar um codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Abre-se uma janela do VS Code no navegador e o contentor de desenvolvimento começa a ser criado.
Isto demora cerca de **2 minutos** na primeira vez.

## 3. Adicione a sua chave API (de forma segura)

### Opção A Segredos do Codespaces — Recomendado

1. ⚙️ Ícone de engrenagem -> Paleta de Comandos -> Codespaces : Manage user secret -> Add a new secret.
2. Nome: OPENAI_API_KEY
3. Valor: cole a sua chave → Add secret

Pronto—o nosso código vai detetar automaticamente.

### Opção B Ficheiro .env (se precisar mesmo)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.