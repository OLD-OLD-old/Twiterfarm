"""
🐦 TWITTER BOT - Sistema Completo de Automação
VERSÃO CORRIGIDA - OAuth 1.0a User Context
"""

import sys
import json
import random
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# Adicionar path
sys.path.insert(0, str(Path(__file__).parent.parent))

import tweepy
from tweepy.errors import TweepyException

from app.humanizer import Humanizer


class TwitterBot:
    """Bot completo para Twitter com multi-contas"""
    
    def __init__(self):
        self.root = Path(__file__).parent.parent
        self.humanizer = Humanizer(nivel='alto')
        
        # Carregar configs
        self._load_configs()
        
        # Clientes Twitter por conta
        self.clients = {}
        
        print("✅ TwitterBot inicializado!")
    
    def _load_configs(self):
        """Carrega configurações"""
        
        # Contas Twitter
        contas_file = self.root / 'config' / 'contas_twitter.json'
        if contas_file.exists():
            with open(contas_file, 'r', encoding='utf-8') as f:
                self.config_contas = json.load(f)
        else:
            print("⚠️  Arquivo contas_twitter.json não encontrado!")
            self.config_contas = {'contas_postadoras': [], 'contas_engajadoras': []}
        
        # Tweets
        tweets_file = self.root / 'config' / 'tweets.json'
        if tweets_file.exists():
            with open(tweets_file, 'r', encoding='utf-8') as f:
                self.config_tweets = json.load(f)
        else:
            print("⚠️  Arquivo tweets.json não encontrado!")
            self.config_tweets = {'tweets': [], 'hashtags': []}
        
        # Links Telegram
        telegram_file = self.root / 'config' / 'telegram_links.json'
        if telegram_file.exists():
            with open(telegram_file, 'r', encoding='utf-8') as f:
                self.config_telegram = json.load(f)
        else:
            print("⚠️  Arquivo telegram_links.json não encontrado!")
            self.config_telegram = {'links': [], 'comentarios': []}
    
    def fazer_login(self, conta: Dict) -> Optional[tweepy.Client]:
        """
        Faz login usando OAuth 1.0a User Context
        MÉTODO CORRETO para Read and Write
        """
        try:
            username = conta['username']
            print(f"\n🔐 Autenticando: @{username}")
            
            # OAuth 1.0a User Context - PERMITE ESCREVER
            client = tweepy.Client(
                consumer_key=conta['api_key'],
                consumer_secret=conta['api_secret'],
                access_token=conta['access_token'],
                access_token_secret=conta['access_token_secret'],
                wait_on_rate_limit=True
            )
            
            # Verificar
            me = client.get_me()
            if me.data:
                print(f"✅ Login OK: @{me.data.username}")
                self.clients[username] = client
                return client
            
            print(f"❌ Falha no login")
            return None
            
        except tweepy.errors.Unauthorized as e:
            print(f"❌ ERRO 401 Unauthorized")
            print(f"\n   🔧 SOLUÇÃO:")
            print(f"   1. Vá em: https://developer.twitter.com/en/portal/dashboard")
            print(f"   2. Seu App → Settings → User authentication settings")
            print(f"   3. App permissions → Read and write")
            print(f"   4. Type of App → Web App, Automated App or Bot")
            print(f"   5. Callback URL: http://127.0.0.1:3000/callback")
            print(f"   6. Website URL: https://example.com")
            print(f"   7. SAVE")
            print(f"   8. Keys and tokens → REGENERATE Access Token")
            print(f"   9. Copiar novos tokens → Colar em contas_twitter.json")
            return None
            
        except TweepyException as e:
            print(f"❌ Erro Twitter: {e}")
            return None
        except Exception as e:
            print(f"❌ Erro: {e}")
            return None
    
    def postar_tweet(self, client: tweepy.Client, texto: str, hashtags: str = "") -> Optional[Dict]:
        """Posta um tweet"""
        try:
            # Combinar texto + hashtags
            tweet_completo = f"{texto}\n\n{hashtags}".strip()
            
            # Limite de 280 caracteres
            if len(tweet_completo) > 280:
                print(f"⚠️  Tweet longo ({len(tweet_completo)} chars), truncando...")
                tweet_completo = tweet_completo[:277] + "..."
            
            # Humanização
            self.humanizer.simular_digitacao(tweet_completo)
            self.humanizer.delay_curto()
            
            # POSTAR
            print(f"📤 Postando: {tweet_completo[:50]}...")
            response = client.create_tweet(text=tweet_completo)
            
            if response.data:
                tweet_id = response.data['id']
                
                print(f"✅ Tweet postado!")
                print(f"   ID: {tweet_id}")
                print(f"   Link: https://twitter.com/i/web/status/{tweet_id}")
                
                return {
                    'tweet_id': tweet_id,
                    'texto': tweet_completo,
                    'timestamp': datetime.now()
                }
            
            return None
            
        except tweepy.errors.Forbidden as e:
            print(f"❌ ERRO 403 Forbidden")
            print(f"\n   🔧 SOLUÇÃO:")
            print(f"   1. Twitter Developer Portal → Seu App")
            print(f"   2. Settings → User authentication settings → Edit")
            print(f"   3. App permissions → Read and write")
            print(f"   4. Type of App → Web App, Automated App or Bot")
            print(f"   5. SAVE")
            print(f"   6. Keys and tokens → REGENERATE Access Token")
            print(f"   7. Copiar novos tokens para contas_twitter.json")
            return None
            
        except TweepyException as e:
            print(f"❌ Erro ao postar: {e}")
            return None
    
    def comentar_tweet(self, client: tweepy.Client, tweet_id: str, comentario: str) -> bool:
        """Comenta em um tweet"""
        try:
            print(f"\n💬 Preparando comentário...")
            
            # Delay humanizado (30-90s)
            self.humanizer.delay_medio()
            
            # Simular digitação
            self.humanizer.simular_digitacao(comentario)
            
            # COMENTAR
            print(f"💬 Comentando: {comentario[:30]}...")
            response = client.create_tweet(
                text=comentario,
                in_reply_to_tweet_id=tweet_id
            )
            
            if response.data:
                print(f"✅ Comentário postado!")
                return True
            
            return False
            
        except TweepyException as e:
            print(f"❌ Erro ao comentar: {e}")
            return False
    
    def dar_rt(self, client: tweepy.Client, tweet_id: str) -> bool:
        """Retweeta"""
        try:
            self.humanizer.delay_curto()
            print("🔁 Dando RT...")
            client.retweet(tweet_id)
            print("✅ RT OK!")
            return True
        except TweepyException as e:
            print(f"❌ Erro RT: {e}")
            return False
    
    def dar_like(self, client: tweepy.Client, tweet_id: str) -> bool:
        """Curte"""
        try:
            self.humanizer.delay_curto()
            print("❤️  Curtindo...")
            client.like(tweet_id)
            print("✅ Like OK!")
            return True
        except TweepyException as e:
            print(f"❌ Erro like: {e}")
            return False
    
    def salvar_tweet(self, client: tweepy.Client, tweet_id: str) -> bool:
        """Salva (bookmark)"""
        try:
            self.humanizer.delay_curto()
            print("🔖 Salvando...")
            client.bookmark(tweet_id)
            print("✅ Save OK!")
            return True
        except TweepyException as e:
            print(f"❌ Erro save: {e}")
            return False
    
    def engajar_completo(self, client: tweepy.Client, tweet_id: str) -> Dict:
        """RT + Like + Save (probabilístico)"""
        resultado = {'rt': False, 'like': False, 'save': False}
        
        # 90% RT, 70% Like, 40% Save
        if random.random() < 0.9:
            resultado['rt'] = self.dar_rt(client, tweet_id)
        
        if random.random() < 0.7:
            resultado['like'] = self.dar_like(client, tweet_id)
        
        if random.random() < 0.4:
            resultado['save'] = self.salvar_tweet(client, tweet_id)
        
        return resultado
    
    def atualizar_bio(self, client: tweepy.Client, bio: str, link: str = None) -> bool:
        """Atualiza bio"""
        try:
            bio_completa = bio
            if link:
                bio_completa = f"{bio}\n\n🔗 {link}"
            
            print("📝 Atualizando bio...")
            client.update_me(description=bio_completa)
            print("✅ Bio atualizada!")
            return True
        except TweepyException as e:
            print(f"❌ Erro bio: {e}")
            return False
    
    def executar_fluxo_completo(self):
        """FLUXO COMPLETO: Post + Comentário + Engajamento"""
        
        print("\n" + "="*80)
        print("🐦 FLUXO COMPLETO - TWITTER BOT")
        print("="*80)
        
        # ===== FASE 1: POSTAR =====
        print("\n📍 FASE 1: POSTAGEM")
        print("-"*80)
        
        contas_postadoras = self.config_contas.get('contas_postadoras', [])
        if not contas_postadoras:
            print("❌ Nenhuma conta postadora!")
            return
        
        conta_postadora = random.choice(contas_postadoras)
        print(f"👤 Conta: @{conta_postadora['username']}")
        
        # Login
        client_postador = self.fazer_login(conta_postadora)
        if not client_postador:
            return
        
        # Escolher conteúdo
        tweet_texto = random.choice(self.config_tweets.get('tweets', ['Tweet padrão']))
        hashtags = random.choice(self.config_tweets.get('hashtags', ['']))
        
        print(f"\n📝 Tweet: {tweet_texto[:50]}...")
        print(f"#️⃣  Hashtags: {hashtags}")
        
        # POSTAR
        resultado_post = self.postar_tweet(client_postador, tweet_texto, hashtags)
        
        if not resultado_post:
            print("❌ Falha ao postar!")
            return
        
        tweet_id = resultado_post['tweet_id']
        
        # ===== FASE 2: COMENTAR =====
        print("\n📍 FASE 2: COMENTÁRIO COM LINK TELEGRAM")
        print("-"*80)
        
        link_telegram = random.choice(self.config_telegram.get('links', ['https://t.me/seu_canal']))
        comentario_base = random.choice(self.config_telegram.get('comentarios', ['Acesse:']))
        comentario_completo = f"{comentario_base} {link_telegram}"
        
        print(f"💬 Comentário: {comentario_completo}")
        
        comentou = self.comentar_tweet(client_postador, tweet_id, comentario_completo)
        
        # ===== FASE 3: ENGAJAMENTO =====
        print("\n📍 FASE 3: ENGAJAMENTO")
        print("-"*80)
        
        contas_engajadoras = self.config_contas.get('contas_engajadoras', [])
        if not contas_engajadoras:
            print("⚠️  Sem contas engajadoras")
            print("\n✅ FLUXO FINALIZADO (só post + comentário)")
            return
        
        # 30-70% das contas
        num_contas = random.randint(
            int(len(contas_engajadoras) * 0.3),
            int(len(contas_engajadoras) * 0.7)
        )
        
        contas_escolhidas = random.sample(contas_engajadoras, min(num_contas, len(contas_engajadoras)))
        
        print(f"👥 {len(contas_escolhidas)} contas vão engajar")
        
        for i, conta in enumerate(contas_escolhidas, 1):
            print(f"\n[{i}/{len(contas_escolhidas)}] @{conta['username']}")
            
            client_engajador = self.fazer_login(conta)
            if not client_engajador:
                print("  ⚠️  Pulando")
                continue
            
            resultado = self.engajar_completo(client_engajador, tweet_id)
            
            print(f"  RT: {'✅' if resultado['rt'] else '❌'}")
            print(f"  Like: {'✅' if resultado['like'] else '❌'}")
            print(f"  Save: {'✅' if resultado['save'] else '❌'}")
            
            # Delay entre contas (2-5 min)
            if i < len(contas_escolhidas):
                print(f"  ⏳ Próxima conta...")
                self.humanizer.delay_longo()
        
        # ===== FIM =====
        print("\n" + "="*80)
        print("✅ FLUXO FINALIZADO!")
        print("="*80)
        print(f"\n📊 RESUMO:")
        print(f"  • Tweet ID: {tweet_id}")
        print(f"  • Link: https://twitter.com/i/web/status/{tweet_id}")
        print(f"  • Comentário: {'✅' if comentou else '❌'}")
        print(f"  • Engajamentos: {len(contas_escolhidas)} contas")
        print()


def menu_principal():
    """Menu interativo"""
    
    bot = TwitterBot()
    
    while True:
        print("\n" + "="*80)
        print("🐦 TWITTER BOT - MENU")
        print("="*80)
        print("\n1️⃣  Executar fluxo completo")
        print("2️⃣  Postar tweet simples")
        print("3️⃣  Testar login")
        print("4️⃣  Atualizar bio")
        print("0️⃣  Sair")
        
        escolha = input("\nEscolha: ").strip()
        
        if escolha == '1':
            bot.executar_fluxo_completo()
        
        elif escolha == '2':
            contas = bot.config_contas.get('contas_postadoras', [])
            if not contas:
                print("❌ Sem contas!")
                continue
            
            print("\nContas:")
            for i, c in enumerate(contas, 1):
                print(f"{i}. @{c['username']}")
            
            try:
                escolha_conta = input("\nEscolha (1-{}): ".format(len(contas))).strip()
                if not escolha_conta:
                    print("❌ Opção inválida!")
                    continue
                
                idx = int(escolha_conta) - 1
                
                if idx < 0 or idx >= len(contas):
                    print("❌ Opção inválida!")
                    continue
                
                conta = contas[idx]
                
                client = bot.fazer_login(conta)
                if client:
                    texto = input("\nTexto do tweet: ").strip()
                    if not texto:
                        print("❌ Tweet vazio!")
                        continue
                    
                    hashtags = input("Hashtags (opcional): ").strip()
                    bot.postar_tweet(client, texto, hashtags)
            
            except ValueError:
                print("❌ Digite um número válido!")
            except KeyboardInterrupt:
                print("\n\n👋 Cancelado!")
        
        elif escolha == '3':
            print("\n1. Postadora")
            print("2. Engajadora")
            
            tipo = input("\nTipo (1 ou 2): ").strip()
            
            if tipo == '1':
                contas = bot.config_contas.get('contas_postadoras', [])
            elif tipo == '2':
                contas = bot.config_contas.get('contas_engajadoras', [])
            else:
                print("❌ Opção inválida!")
                continue
            
            if not contas:
                print("❌ Sem contas!")
                continue
            
            print("\nContas:")
            for i, c in enumerate(contas, 1):
                print(f"{i}. @{c['username']}")
            
            try:
                escolha_conta = input("\nEscolha (1-{}): ".format(len(contas))).strip()
                if not escolha_conta:
                    print("❌ Opção inválida!")
                    continue
                
                idx = int(escolha_conta) - 1
                
                if idx < 0 or idx >= len(contas):
                    print("❌ Opção inválida!")
                    continue
                
                bot.fazer_login(contas[idx])
            
            except ValueError:
                print("❌ Digite um número válido!")
            except KeyboardInterrupt:
                print("\n\n👋 Cancelado!")
        
        elif escolha == '4':
            contas = bot.config_contas.get('contas_postadoras', [])
            
            if not contas:
                print("❌ Sem contas!")
                continue
            
            print("\nContas:")
            for i, c in enumerate(contas, 1):
                print(f"{i}. @{c['username']}")
            
            try:
                escolha_conta = input("\nEscolha (1-{}): ".format(len(contas))).strip()
                if not escolha_conta:
                    print("❌ Opção inválida!")
                    continue
                
                idx = int(escolha_conta) - 1
                
                if idx < 0 or idx >= len(contas):
                    print("❌ Opção inválida!")
                    continue
                
                client = bot.fazer_login(contas[idx])
                
                if client:
                    bio = input("\nNova bio: ").strip()
                    if not bio:
                        print("❌ Bio vazia!")
                        continue
                    
                    link = input("Link (opcional): ").strip()
                    bot.atualizar_bio(client, bio, link or None)
            
            except ValueError:
                print("❌ Digite um número válido!")
            except KeyboardInterrupt:
                print("\n\n👋 Cancelado!")
        
        elif escolha == '0':
            print("\n👋 Até logo!")
            break
        
        else:
            print("\n❌ Opção inválida! Digite 1, 2, 3, 4 ou 0")


if __name__ == '__main__':
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n👋 Programa encerrado!")
    except Exception as e:
        print(f"\n❌ Erro fatal: {e}")
        print("Por favor, relate este erro.")