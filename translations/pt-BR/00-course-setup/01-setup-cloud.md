# Configuração na Nuvem ☁️ – GitHub Codespaces

**Use este guia se você não quiser instalar nada localmente.**  
Codespaces oferece uma instância gratuita do VS Code baseada no navegador com todas as dependências pré-instaladas.

---

## 1. Por que Codespaces?

| Benefício | O que significa para você |
|---------|----------------------|
| ✅ Nenhuma instalação | Funciona em Chromebook, iPad, PCs do laboratório da escola… |
| ✅ Container de desenvolvimento pré-configurado | Python 3, Node.js, .NET, Java já incluídos |
| ✅ Cota gratuita | Contas pessoais recebem **120 horas-core / 60 GB-horas por mês** |

> 💡 **Dica**  
> Mantenha sua cota saudável **parando** ou **excluindo** codespaces inativos  
> (Visualizar ▸ Paleta de Comandos ▸ *Codespaces: Parar Codespace*).

---

## 2. Crie um Codespace (um clique)

1. **Faça um fork** deste repositório (botão **Fork** no canto superior direito).  
2. No seu fork, clique em **Code ▸ Codespaces ▸ Criar codespace no main**.  
   ![Caixa de diálogo mostrando botões para criar um codespace](../../../translated_images/pt-BR/who-will-pay.4c0609b1c7780f44.webp)

✅ Uma janela do VS Code no navegador será aberta e o container de desenvolvimento começará a ser construído.
Isso leva **~2 minutos** na primeira vez.

## 3. Adicione sua chave API (de forma segura)

### Opção A Segredos do Codespaces — Recomendado

1. ⚙️ Ícone de engrenagem -> Paleta de Comandos -> Codespaces: Gerenciar segredo do usuário -> Adicionar um novo segredo.
2. Nome: OPENAI_API_KEY
3. Valor: cole sua chave → Adicionar segredo

É isso — nosso código irá capturá-la automaticamente.

### Opção B Arquivo .env (se você realmente precisar)

```bash
cp .env.copy .env
code .env         # preencha OPENAI_API_KEY=sua_chave_aqui
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->