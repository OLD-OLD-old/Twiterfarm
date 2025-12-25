# 🚀 INÍCIO RÁPIDO - Twitter Farm

Guia para começar em **5 minutos**.

---

## 📥 PASSO 1: BAIXAR E EXTRAIR

### Windows:
1. Baixe o arquivo `twifarm.tar.gz`
2. Use **7-Zip** ou **WinRAR** para extrair
3. Ou use PowerShell:
```powershell
tar -xzf twifarm.tar.gz
cd twifarm
```

### Linux/Mac:
```bash
tar -xzf twifarm.tar.gz
cd twifarm
```

---

## 📦 PASSO 2: INSTALAR DEPENDÊNCIAS

```bash
pip install -r requirements.txt
```

**O que instala:**
- tweepy (Twitter API)
- schedule (Agendamento)
- python-dotenv (Variáveis)
- colorlog (Logs bonitos)

---

## ⚙️ PASSO 3: CONFIGURAR CONTAS

### 3.1 - Obter Credenciais Twitter (GRÁTIS)

1. Acesse: https://developer.twitter.com/en/portal/dashboard
2. Crie uma conta developer (FREE)
3. Crie um App
4. Gere as 5 credenciais:
   - API Key
   - API Secret  
   - Access Token
   - Access Token Secret
   - Bearer Token

### 3.2 - Editar `config/contas_twitter.json`

```json
{
  "contas_postadoras": [
    {
      "id": 1,
      "username": "sua_conta",
      "api_key": "COLE_AQUI",
      "api_secret": "COLE_AQUI",
      "access_token": "COLE_AQUI",
      "access_token_secret": "COLE_AQUI",
      "bearer_token": "COLE_AQUI"
    }
  ],
  "contas_engajadoras": [
    // Adicione 10-20 contas aqui
  ]
}
```

### 3.3 - Editar `config/tweets.json`

Adicione seus textos:

```json
{
  "tweets": [
    "Seu primeiro tweet aqui! 🔥",
    "Segundo tweet com valor 💡"
  ],
  "hashtags": [
    "#viral #brasil #dinheiro"
  ]
}
```

### 3.4 - Editar `config/telegram_links.json`

```json
{
  "links": [
    "https://t.me/seu_canal"
  ]
}
```

---

## 🧪 PASSO 4: TESTAR

```bash
python app/twitter_bot.py
```

### Menu:
```
1️⃣  Executar fluxo completo
2️⃣  Postar tweet simples
3️⃣  Testar login          ← COMECE POR AQUI
```

**Escolha opção 3** para testar login primeiro!

---

## ✅ PASSO 5: EXECUTAR

Quando login funcionar:

```bash
python app/twitter_bot.py
```

**Escolha opção 1** (Executar fluxo completo)

O sistema vai:
1. ✅ Postar tweet
2. ✅ Comentar link Telegram (30-90s depois)
3. ✅ Chamar contas engajadoras
4. ✅ RT/Like/Save automaticamente

---

## 📊 CALCULAR CAPACIDADE (GRÁTIS)

```bash
python calculador_twitter_free.py
```

Mostra quantos posts você pode fazer gratuitamente!

**Exemplo com 5 contas:**
```
📊 CAPACIDADE DIÁRIA:
   • 125 posts (com comentário)
   • 500 engajamentos completos
   • ~4 contas engajam por post

💰 Custo: R$ 0,00/mês
```

---

## 📁 ESTRUTURA DO PROJETO

```
twifarm/
├── app/
│   └── twitter_bot.py          ← Sistema principal
├── config/
│   ├── contas_twitter.json     ← EDITE AQUI
│   ├── tweets.json             ← EDITE AQUI
│   └── telegram_links.json     ← EDITE AQUI
├── cache_local/
│   └── twitter_media/          ← Coloque imagens/vídeos
├── logs/                       ← Logs automáticos
├── sessoes/                    ← Sessões salvas
├── calculador_twitter_free.py  ← Calculadora
├── GUIA_TWITTER_FARM.md        ← Guia completo
├── ESTRATEGIA_FREE.md          ← Estratégia gratuita
└── requirements.txt            ← Dependências
```

---

## 🐛 PROBLEMAS COMUNS

### "Authentication failed"
**Solução:** Verifique as 5 credenciais no config/contas_twitter.json

### "Rate limit exceeded"
**Solução:** Aguarde 15 minutos ou use menos contas

### "Forbidden - 403"
**Solução:**
1. Vá em Twitter Developer Portal
2. Settings → App permissions
3. Marque: Read and Write
4. Regenere Access Token

---

## 📖 PRÓXIMOS PASSOS

Depois que funcionar:

1. **Adicione mais contas** (10-20 engajadoras)
2. **Crie mais tweets** (50+ variações)
3. **Adicione imagens** em `cache_local/twitter_media/`
4. **Automatize** (agende para rodar de hora em hora)

---

## 🎯 AUTOMAÇÃO 24/7

Crie arquivo `autopost.py`:

```python
import schedule
import time
from app.twitter_bot import TwitterBot

def job():
    bot = TwitterBot()
    bot.executar_fluxo_completo()

# Postar a cada 2 horas
schedule.every(2).hours.do(job)

print("🚀 Bot rodando 24/7")

while True:
    schedule.run_pending()
    time.sleep(60)
```

Execute:
```bash
python autopost.py
```

---

## 💡 DICAS FINAIS

1. **Comece com 1-2 contas** para testar
2. **Use 70% da capacidade** (margem de segurança)
3. **Varie conteúdo** sempre
4. **Monitore logs** em `logs/`
5. **Leia documentação completa** em GUIA_TWITTER_FARM.md

---

## 🆘 SUPORTE

- 📖 [GUIA_TWITTER_FARM.md](GUIA_TWITTER_FARM.md) - Tutorial completo
- 📈 [ESTRATEGIA_FREE.md](ESTRATEGIA_FREE.md) - Usar 100% grátis
- 🐛 Problemas? Veja seção Troubleshooting no guia

---

## ✅ CHECKLIST

- [ ] Baixar e extrair twifarm.tar.gz
- [ ] Instalar dependências (`pip install -r requirements.txt`)
- [ ] Configurar contas_twitter.json
- [ ] Configurar tweets.json
- [ ] Configurar telegram_links.json
- [ ] Testar login (opção 3)
- [ ] Executar fluxo completo (opção 1)
- [ ] Monitorar logs
- [ ] Adicionar mais contas
- [ ] Automatizar 24/7

---

**🎉 Pronto! Em 5 minutos você tem um Twitter Farm funcionando!**

**Boa sorte! 🚀**
