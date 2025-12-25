# 🐦 TWITTER FARM - GUIA COMPLETO DE INSTALAÇÃO

Sistema completo de automação para Twitter com contas postadoras e engajadoras.

---

## 📋 ÍNDICE

1. [Pré-requisitos](#pré-requisitos)
2. [Instalação](#instalação)
3. [Configuração de Contas](#configuração-de-contas)
4. [Obter Credenciais Twitter](#obter-credenciais-twitter)
5. [Configurar Conteúdo](#configurar-conteúdo)
6. [Primeiro Uso](#primeiro-uso)
7. [Automação 24/7](#automação-247)
8. [Troubleshooting](#troubleshooting)

---

## 🎯 PRÉ-REQUISITOS

### Software Necessário
- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)
- Contas do Twitter (3-5 postadoras + 15-20 engajadoras)

### Verificar Instalação
```bash
python --version
# Deve mostrar: Python 3.9.x ou superior

pip --version
# Deve mostrar a versão do pip
```

---

## 📦 INSTALAÇÃO

### Passo 1: Instalar Dependências

```bash
# Instalar tweepy (biblioteca oficial do Twitter)
pip install tweepy

# Instalar outras dependências
pip install python-dotenv schedule requests
```

### Passo 2: Estrutura de Pastas

Crie a seguinte estrutura no seu projeto:

```
farminst/
├── app/
│   └── twitter_bot.py          ← Script principal
├── config/
│   ├── contas_twitter.json     ← Suas contas
│   ├── tweets.json             ← Textos para postar
│   └── telegram_links.json     ← Links do Telegram
├── logs/                       ← Logs automáticos
├── sessoes/                    ← Sessões salvas
└── cache_local/
    └── twitter_media/          ← Imagens/vídeos
```

### Passo 3: Copiar Arquivos

Coloque os arquivos baixados nas respectivas pastas:
- `twitter_bot.py` → pasta `app/`
- `contas_twitter.json` → pasta `config/`
- `tweets.json` → pasta `config/`
- `telegram_links.json` → pasta `config/`

---

## 🔑 OBTER CREDENCIAIS TWITTER

### Passo 1: Criar Developer Account (100% GRÁTIS)

1. Acesse: https://developer.twitter.com/en/portal/dashboard
2. Faça login com sua conta Twitter
3. Clique em **"Sign up for Free Account"**
4. Preencha o formulário:
   - Como vai usar a API: "Building tools for Twitter users"
   - Selecione: "Making a bot"
5. Aceite os termos e confirme email

**💰 TIER FREE (R$ 0,00/mês):**
- ✅ 1.500 tweets por mês (50/dia)
- ✅ 500.000 leituras por mês
- ✅ Postar, curtir, RT, comentar
- ✅ **Perfeito para começar!**

### Passo 2: Criar um App

1. No Dashboard, clique em **"Create Project"**
2. Nome do projeto: `Twitter Bot`
3. Use case: `Making a bot`
4. Descrição: `Automated posting and engagement`
5. Clique em **"Next"** até criar o app

### Passo 3: Gerar Credenciais

1. Na página do App, vá em **"Keys and tokens"**
2. Gere as seguintes credenciais:

   **API Key and Secret:**
   - Clique em **"Regenerate"**
   - Copie `API Key` e `API Secret`
   
   **Access Token and Secret:**
   - Clique em **"Generate"**
   - Copie `Access Token` e `Access Token Secret`
   
   **Bearer Token:**
   - Copie o `Bearer Token`

3. **IMPORTANTE:** Salve tudo em lugar seguro! Não dá para ver de novo.

### Passo 4: Configurar Permissões

1. Ainda no App, vá em **"Settings"**
2. Em **"App permissions"**, selecione:
   - ✅ Read
   - ✅ Write
   - ✅ Direct Messages (opcional)
3. Clique em **"Save"**

### Passo 5: Repetir para Todas as Contas

**Para cada conta Twitter** (postadoras e engajadoras):
1. Faça login na conta
2. Crie um App para ela (passos acima)
3. Copie as 5 credenciais
4. Cole no arquivo `contas_twitter.json`

---

## ⚙️ CONFIGURAÇÃO DE CONTAS

### Arquivo: `config/contas_twitter.json`

```json
{
  "contas_postadoras": [
    {
      "id": 1,
      "username": "sua_conta_principal",
      "email": "email@example.com",
      "password": "sua_senha",
      "api_key": "COLE_API_KEY_AQUI",
      "api_secret": "COLE_API_SECRET_AQUI",
      "access_token": "COLE_ACCESS_TOKEN_AQUI",
      "access_token_secret": "COLE_ACCESS_TOKEN_SECRET_AQUI",
      "bearer_token": "COLE_BEARER_TOKEN_AQUI",
      "proxy_id": null,
      "status": "ativa",
      "bio": "Conteúdo sobre [SEU_NICHO] 🚀\\n\\nCanal VIP 👇",
      "link_bio": "https://t.me/seu_canal",
      "notas": "Conta principal"
    }
  ],
  
  "contas_engajadoras": [
    {
      "id": 101,
      "username": "engajador_01",
      "email": "eng01@example.com",
      "password": "senha",
      "api_key": "...",
      "api_secret": "...",
      "access_token": "...",
      "access_token_secret": "...",
      "bearer_token": "...",
      "proxy_id": null,
      "status": "ativa",
      "notas": "Conta engajadora"
    }
  ]
}
```

**Dicas:**
- Comece com 2-3 contas postadoras
- Adicione 10-15 contas engajadoras
- Use emails diferentes para cada conta
- Guarde bem as credenciais

---

## 📝 CONFIGURAR CONTEÚDO

### Arquivo: `config/tweets.json`

Edite os textos dos tweets:

```json
{
  "tweets": [
    "🔥 Seu primeiro tweet aqui!",
    "💡 Segundo tweet com conteúdo de valor",
    "⚡ Terceiro tweet chamativo"
  ],
  
  "hashtags": [
    "#viral #brasil #dinheiro #renda #online",
    "#negocio #empreender #sucesso #meta"
  ]
}
```

**Recomendações:**
- 20-30 tweets variados
- Máximo 280 caracteres por tweet
- Use 2-3 hashtags por grupo
- Varie os emojis

### Arquivo: `config/telegram_links.json`

Configure seus links do Telegram:

```json
{
  "links": [
    "https://t.me/seu_canal"
  ],
  
  "comentarios": [
    "🔥 Conteúdo completo aqui:",
    "💎 Material exclusivo no canal:",
    "⚡ Acesse o grupo VIP:"
  ]
}
```

---

## 🚀 PRIMEIRO USO

### Teste Rápido

```bash
# Ir para a pasta do projeto
cd C:\Users\Trabalho\Documents\farminst

# Executar o bot
python app/twitter_bot.py
```

### Menu Interativo

O sistema vai mostrar:

```
╔══════════════════════════════════════════════════════════╗
║   🐦 TWITTER BOT - MENU PRINCIPAL                        ║
╚══════════════════════════════════════════════════════════╝

1️⃣  Executar fluxo completo (Post + Comentário + Engajamento)
2️⃣  Postar tweet simples
3️⃣  Testar login de uma conta
4️⃣  Atualizar bio de uma conta
5️⃣  Engajar em tweet específico
6️⃣  Configurar contas
0️⃣  Sair

👉 Digite o número:
```

### Primeiro Teste

1. Digite **3** (Testar login)
2. Escolha **1** (Conta postadora)
3. Selecione a primeira conta
4. Aguarde o login

**Se der erro:**
- Verifique as credenciais
- Veja se a API está ativa
- Confira as permissões do App

**Se funcionar:**
```
✅ Login bem-sucedido: @sua_conta
```

---

## 🎯 EXECUTAR FLUXO COMPLETO

### Opção 1: Fluxo Automático

```bash
python app/twitter_bot.py
```

1. Digite **1** (Executar fluxo completo)
2. O sistema vai:
   - ✅ Escolher conta postadora aleatória
   - ✅ Postar tweet com texto + hashtags
   - ✅ Aguardar 30-90 segundos (humanização)
   - ✅ Comentar com link do Telegram
   - ✅ Chamar contas engajadoras (30-70%)
   - ✅ Fazer RT/Like/Save de forma natural

**Exemplo de saída:**

```
╔══════════════════════════════════════════════════════════╗
║   🐦 FLUXO COMPLETO - TWITTER AUTOMATION                 ║
╚══════════════════════════════════════════════════════════╝

📍 FASE 1: POSTAGEM
────────────────────────────────────────────────────────────
👤 Conta selecionada: @sua_conta_principal

📝 Tweet: 🔥 Conteúdo exclusivo que vai transformar sua vida!
#️⃣  Hashtags: #viral #brasil #dinheiro

⌨️  Simulando digitação...
⏳ Aguardando...
📤 Postando tweet...
✅ Tweet postado com sucesso!

   Tweet ID: 1234567890123456789
   Link: https://twitter.com/i/web/status/1234567890123456789

📍 FASE 2: COMENTÁRIO COM LINK
────────────────────────────────────────────────────────────
💬 Comentário: 🔥 Conteúdo completo aqui: https://t.me/seu_canal

⏳ Aguardando para comentar...
⌨️  Simulando digitação...
💬 Comentando...
✅ Comentário postado!

📍 FASE 3: ENGAJAMENTO COM OUTRAS CONTAS
────────────────────────────────────────────────────────────
👥 12 contas vão engajar

[1/12] @engajador_01
  ✅ Login bem-sucedido: @engajador_01
  🔁 Dando RT...
  ✅ RT realizado!
  ❤️  Curtindo...
  ✅ Like realizado!
  🔖 Salvando...
  ✅ Tweet salvo!
  
  RT: ✅
  Like: ✅
  Save: ✅

  ⏳ Aguardando próxima conta...

[2/12] @engajador_02
  ...

╔══════════════════════════════════════════════════════════╗
║   ✅ FLUXO COMPLETO FINALIZADO!                          ║
╚══════════════════════════════════════════════════════════╝

📊 RESUMO:
  • Tweet ID: 1234567890123456789
  • Link: https://twitter.com/i/web/status/1234567890123456789
  • Comentário: ✅
  • Engajamentos: 12 contas
```

---

## 🔄 AUTOMAÇÃO 24/7

### Script de Automação

Crie um arquivo `autopost_twitter.py`:

```python
"""
Automação 24/7 para Twitter
Posta automaticamente em intervalos regulares
"""

import time
import schedule
from app.twitter_bot import TwitterBot

def job():
    """Executa fluxo completo"""
    print("\n🤖 Iniciando novo ciclo de postagem...")
    bot = TwitterBot()
    bot.executar_fluxo_completo()

# Agendar posts
schedule.every(2).hours.do(job)  # A cada 2 horas

print("🚀 Bot Twitter rodando 24/7")
print("⏰ Postagens a cada 2 horas")
print("\nPressione CTRL+C para parar\n")

# Loop infinito
while True:
    schedule.run_pending()
    time.sleep(60)  # Verifica a cada minuto
```

### Executar:

```bash
python autopost_twitter.py
```

**Configurações recomendadas:**
- Postar a cada 2-4 horas
- Máximo 10 posts por dia por conta
- Variar horários (usar randomização)

---

## 🛡️ BOAS PRÁTICAS

### Rate Limits do Twitter

**Free Tier:**
- 50 tweets por dia
- 1.500 tweets por mês
- 500 RTs por dia

**Recomendações:**
- Não ultrapassar 5-10 tweets/dia por conta
- Espaçar ações em 2-5 minutos
- Usar delay humanizado (30-90s)

### Segurança

1. **Proxies (Opcional):**
   - Use 1 proxy por conta
   - Evita bloqueios em massa
   - Mais seguro para múltiplas contas

2. **Variação:**
   - Nunca poste o mesmo texto
   - Varie hashtags
   - Alterne horários

3. **Humanização:**
   - Sistema já tem delays automáticos
   - Simula digitação
   - Ações aleatórias (nem sempre RT/Like/Save tudo)

---

## 🐛 TROUBLESHOOTING

### Erro: "Authentication failed"

**Causa:** Credenciais incorretas

**Solução:**
1. Verifique se copiou todas as 5 credenciais
2. Veja se não tem espaços extras
3. Regenere as credenciais no Twitter Developer

### Erro: "Rate limit exceeded"

**Causa:** Muitas ações em pouco tempo

**Solução:**
1. Aguarde 15 minutos
2. Reduza frequência de posts
3. Adicione mais delays

### Erro: "Forbidden - 403"

**Causa:** Permissões do App

**Solução:**
1. No Twitter Developer Portal
2. Settings → App permissions
3. Marque: Read and Write
4. Regenere Access Token

### Bot não comenta

**Causa:** Delay insuficiente ou erro na função

**Solução:**
1. Aumente delay (60-120s)
2. Verifique se tweet foi postado
3. Veja logs para erros

---

## 📊 MONITORAMENTO

### Ver Estatísticas

```python
# Adicione ao final do twitter_bot.py

def ver_stats():
    """Mostra estatísticas"""
    bot = TwitterBot()
    
    print("\n📊 ESTATÍSTICAS")
    print("="*60)
    
    # Contas configuradas
    print(f"\nContas Postadoras: {len(bot.config_contas['contas_postadoras'])}")
    print(f"Contas Engajadoras: {len(bot.config_contas['contas_engajadoras'])}")
    
    # Conteúdo
    print(f"\nTweets cadastrados: {len(bot.config_tweets['tweets'])}")
    print(f"Grupos de hashtags: {len(bot.config_tweets['hashtags'])}")
    print(f"Links Telegram: {len(bot.config_telegram['links'])}")
```

### Logs Automáticos

O sistema salva logs em `logs/twitter_bot_YYYYMMDD.log`

Para ver:
```bash
# Windows PowerShell
Get-Content logs\twitter_bot_*.log -Tail 50 -Wait

# Linux/Mac
tail -f logs/twitter_bot_*.log
```

---

## 🎯 EXPANSÃO FUTURA

### Adicionar Imagens/Vídeos

Coloque mídias em `cache_local/twitter_media/`

Modifique o código para incluir mídia:

```python
# Em twitter_bot.py, função postar_tweet

# Verificar se tem mídia
media_path = "cache_local/twitter_media/imagem1.jpg"

if Path(media_path).exists():
    # Upload de mídia
    media = client.media_upload(media_path)
    
    # Postar com mídia
    response = client.create_tweet(
        text=tweet_completo,
        media_ids=[media.media_id]
    )
```

### Agendamento Inteligente

Use horários de pico:
- 7h-9h (manhã)
- 12h-14h (almoço)
- 18h-21h (noite)

### Integrar com Instagram

Poste o mesmo conteúdo nos dois:
```python
# Postar no Twitter
twitter_bot.executar_fluxo_completo()

# Postar no Instagram
instagram_bot.postar_reel(video, legenda)
```

---

## 📞 SUPORTE

**Problemas comuns:**
- Verifique credenciais
- Confirme permissões da API
- Aguarde rate limits
- Use proxies se necessário

**Recursos:**
- [Twitter API Docs](https://developer.twitter.com/en/docs)
- [Tweepy Docs](https://docs.tweepy.org/)
- [Rate Limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits)

---

## ✅ CHECKLIST FINAL

Antes de rodar 24/7:

- [ ] Credenciais configuradas corretamente
- [ ] Teste de login funcionando
- [ ] 20+ tweets cadastrados
- [ ] 5+ grupos de hashtags
- [ ] Links do Telegram configurados
- [ ] Teste manual do fluxo completo
- [ ] Delays adequados (30-90s)
- [ ] Contas engajadoras ativas
- [ ] Proxies configurados (opcional)
- [ ] Monitoramento de logs ativo

---

**🎉 Pronto! Seu Twitter Farm está configurado!**

**Boa sorte com a automação! 🚀**
