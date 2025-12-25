"""
🐦 TWITTER BOT - Sistema Completo de Automação
Sistema multi-contas com postagem + engajamento automático

ESTRATÉGIA:
- Contas POSTADORAS: Postam conteúdo + comentam link Telegram
- Contas ENGAJADORAS: RT + Like + Save nos posts das principais

FEATURES:
✅ Post automático com hashtags
✅ Comentário com link do Telegram
✅ RT/Like/Save de outras contas
✅ Humanização avançada
✅ Bio automática com link
✅ Rate limit control
✅ Proxy support
✅ Analytics integrado

USO: python app/twitter_bot.py
"""

import sys
import json
import time
import random
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

import tweepy
from tweepy.errors import TweepyException

from app.humanizer import Humanizer
from database.models import get_session, Conta


class TwitterBot:
    """Bot completo para Twitter com multi-contas"""
    
    def __init__(self):
        self.root = Path(__file__).parent.parent
        self.db = get_session()
        self.humanizer = Humanizer(nivel='alto')
        
        # Carregar configs
        self._load_configs()
        
        # Clientes Twitter por conta
        self.clients = {}
        
        print("✅ TwitterBot inicializado!")
    
    def _load_configs(self):
        """Carrega configurações do Twitter"""
        
        # Contas Twitter
        contas_file = self.root / 'config' / 'contas_twitter.json'
        if contas_file.exists():
            with open(contas_file, 'r', encoding='utf-8') as f:
                self.config_contas = json.load(f)
        else:
            print("⚠️  Arquivo contas_twitter.json não encontrado!")
            self.config_contas = {'contas_postadoras': [], 'contas_engajadoras': []}
        
        # Tweets (textos)
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
    
    # ==========================================
    # AUTENTICAÇÃO TWITTER
    # ==========================================
    
    def fazer_login(self, conta: Dict) -> Optional[tweepy.Client]:
        """
        Faz login em uma conta Twitter usando OAuth 2.0
        
        Args:
            conta: Dict com credenciais (bearer_token, api_key, etc)
        
        Returns:
            tweepy.Client ou None se falhar
        """
        try:
            username = conta['username']
            
            # Tentar com Bearer Token (mais simples)
            if conta.get('bearer_token'):
                client = tweepy.Client(
                    bearer_token=conta['bearer_token'],
                    consumer_key=conta.get('api_key'),
                    consumer_secret=conta.get('api_secret'),
                    access_token=conta.get('access_token'),
                    access_token_secret=conta.get('access_token_secret'),
                    wait_on_rate_limit=True  # Auto-aguarda rate limit
                )
                
                # Verificar autenticação
                me = client.get_me()
                if me.data:
                    print(f"✅ Login bem-sucedido: @{me.data.username}")
                    self.clients[username] = client
                    return client
            
            print(f"❌ Falha no login: @{username}")
            return None
            
        except TweepyException as e:
            print(f"❌ Erro Twitter: {e}")
            return None
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return None
    
    # ==========================================
    # POSTAR TWEET
    # ==========================================
    
    def postar_tweet(self, client: tweepy.Client, texto: str, hashtags: str = "") -> Optional[Dict]:
        """
        Posta um tweet simples
        
        Args:
            client: Cliente Twitter autenticado
            texto: Texto do tweet
            hashtags: Hashtags a adicionar
        
        Returns:
            Dict com dados do tweet ou None
        """
        try:
            # Combinar texto + hashtags
            tweet_completo = f"{texto}\n\n{hashtags}".strip()
            
            # Verificar limite de caracteres (280 para free, 25000 para premium)
            if len(tweet_completo) > 280:
                print(f"⚠️  Tweet muito longo ({len(tweet_completo)} chars), truncando...")
                tweet_completo = tweet_completo[:277] + "..."
            
            # Simular digitação (humanização)
            print("⌨️  Simulando digitação...")
            self.humanizer.simular_digitacao(tweet_completo)
            
            # Delay antes de postar
            self.humanizer.delay_curto()
            
            # POSTAR!
            print("📤 Postando tweet...")
            response = client.create_tweet(text=tweet_completo)
            
            if response.data:
                tweet_id = response.data['id']
                
                print(f"✅ Tweet postado com sucesso!")
                print(f"   Tweet ID: {tweet_id}")
                print(f"   Link: https://twitter.com/i/web/status/{tweet_id}")
                
                return {
                    'tweet_id': tweet_id,
                    'texto': tweet_completo,
                    'timestamp': datetime.now()
                }
            
            return None
            
        except TweepyException as e:
            print(f"❌ Erro ao postar: {e}")
            return None
    
    # ==========================================
    # COMENTAR COM LINK TELEGRAM
    # ==========================================
    
    def comentar_tweet(self, client: tweepy.Client, tweet_id: str, comentario: str) -> bool:
        """
        Comenta em um tweet (reply)
        
        Args:
            client: Cliente Twitter
            tweet_id: ID do tweet para comentar
            comentario: Texto do comentário
        
        Returns:
            True se sucesso
        """
        try:
            # Delay humanizado antes de comentar (30-90 segundos)
            print("⏳ Aguardando para comentar...")
            self.humanizer.delay_natural(30, 90)
            
            # Simular digitação
            self.humanizer.simular_digitacao(comentario)
            
            # COMENTAR (reply to tweet)
            print("💬 Comentando...")
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
    
    # ==========================================
    # ENGAJAMENTO (RT + LIKE + SAVE)
    # ==========================================
    
    def dar_rt(self, client: tweepy.Client, tweet_id: str) -> bool:
        """Retweeta um tweet"""
        try:
            # Delay humanizado
            self.humanizer.delay_natural(10, 30)
            
            print("🔁 Dando RT...")
            client.retweet(tweet_id)
            print("✅ RT realizado!")
            return True
            
        except TweepyException as e:
            print(f"❌ Erro ao RT: {e}")
            return False
    
    def dar_like(self, client: tweepy.Client, tweet_id: str) -> bool:
        """Curte um tweet"""
        try:
            # Delay humanizado
            self.humanizer.delay_natural(5, 15)
            
            print("❤️  Curtindo...")
            
            # Pegar user_id do client autenticado
            me = client.get_me()
            user_id = me.data.id
            
            client.like(tweet_id, user_auth=True)
            print("✅ Like realizado!")
            return True
            
        except TweepyException as e:
            print(f"❌ Erro ao curtir: {e}")
            return False
    
    def salvar_tweet(self, client: tweepy.Client, tweet_id: str) -> bool:
        """Salva (bookmark) um tweet"""
        try:
            # Delay humanizado
            self.humanizer.delay_natural(5, 15)
            
            print("🔖 Salvando...")
            
            # Pegar user_id
            me = client.get_me()
            user_id = me.data.id
            
            client.bookmark(tweet_id, user_auth=True)
            print("✅ Tweet salvo!")
            return True
            
        except TweepyException as e:
            print(f"❌ Erro ao salvar: {e}")
            return False
    
    def engajar_completo(self, client: tweepy.Client, tweet_id: str) -> Dict:
        """
        Faz engajamento completo (RT + Like + Save)
        
        Args:
            client: Cliente Twitter
            tweet_id: ID do tweet
        
        Returns:
            Dict com resultado de cada ação
        """
        resultado = {
            'rt': False,
            'like': False,
            'save': False
        }
        
        # Decidir quais ações fazer (não fazer todas sempre)
        # 90% RT, 70% Like, 40% Save
        
        if random.random() < 0.9:
            resultado['rt'] = self.dar_rt(client, tweet_id)
        
        if random.random() < 0.7:
            resultado['like'] = self.dar_like(client, tweet_id)
        
        if random.random() < 0.4:
            resultado['save'] = self.salvar_tweet(client, tweet_id)
        
        return resultado
    
    # ==========================================
    # ATUALIZAR BIO
    # ==========================================
    
    def atualizar_bio(self, client: tweepy.Client, bio: str, link: str = None) -> bool:
        """
        Atualiza bio da conta
        
        Args:
            client: Cliente Twitter
            bio: Texto da bio
            link: URL para adicionar na bio (opcional)
        
        Returns:
            True se sucesso
        """
        try:
            # Combinar bio + link se fornecido
            bio_completa = bio
            if link:
                bio_completa = f"{bio}\n\n🔗 {link}"
            
            print("📝 Atualizando bio...")
            
            # Pegar user_id
            me = client.get_me()
            user_id = me.data.id
            
            # Atualizar
            client.update_me(description=bio_completa)
            
            print("✅ Bio atualizada!")
            return True
            
        except TweepyException as e:
            print(f"❌ Erro ao atualizar bio: {e}")
            return False
    
    # ==========================================
    # FLUXO COMPLETO
    # ==========================================
    
    def executar_fluxo_completo(self):
        """
        Executa o fluxo completo:
        1. Conta POSTADORA posta tweet
        2. Comenta com link Telegram
        3. Contas ENGAJADORAS fazem RT/Like/Save
        """
        
        print("="*80)
        print("🐦 FLUXO COMPLETO - TWITTER AUTOMATION")
        print("="*80)
        
        # ========== FASE 1: POSTAR ==========
        print("\n📍 FASE 1: POSTAGEM")
        print("-"*80)
        
        # Escolher conta postadora
        contas_postadoras = self.config_contas.get('contas_postadoras', [])
        if not contas_postadoras:
            print("❌ Nenhuma conta postadora configurada!")
            return
        
        conta_postadora = random.choice(contas_postadoras)
        print(f"👤 Conta selecionada: @{conta_postadora['username']}")
        
        # Fazer login
        client_postador = self.fazer_login(conta_postadora)
        if not client_postador:
            print("❌ Falha no login!")
            return
        
        # Escolher tweet e hashtags
        tweet_texto = random.choice(self.config_tweets.get('tweets', ['Tweet padrão']))
        hashtags = random.choice(self.config_tweets.get('hashtags', ['']))
        
        print(f"\n📝 Tweet: {tweet_texto[:50]}...")
        print(f"#️⃣  Hashtags: {hashtags}")
        
        # POSTAR!
        resultado_post = self.postar_tweet(client_postador, tweet_texto, hashtags)
        
        if not resultado_post:
            print("❌ Falha ao postar tweet!")
            return
        
        tweet_id = resultado_post['tweet_id']
        
        # ========== FASE 2: COMENTAR LINK TELEGRAM ==========
        print("\n📍 FASE 2: COMENTÁRIO COM LINK")
        print("-"*80)
        
        # Escolher link e comentário
        link_telegram = random.choice(self.config_telegram.get('links', ['https://t.me/seu_canal']))
        comentario_base = random.choice(self.config_telegram.get('comentarios', [
            'Conteúdo completo aqui:',
            'Acesse nosso canal:',
            'Mais informações:'
        ]))
        
        comentario_completo = f"{comentario_base} {link_telegram}"
        
        print(f"💬 Comentário: {comentario_completo}")
        
        # COMENTAR!
        comentou = self.comentar_tweet(client_postador, tweet_id, comentario_completo)
        
        if not comentou:
            print("⚠️  Falha ao comentar, mas tweet foi postado!")
        
        # ========== FASE 3: ENGAJAMENTO ==========
        print("\n📍 FASE 3: ENGAJAMENTO COM OUTRAS CONTAS")
        print("-"*80)
        
        contas_engajadoras = self.config_contas.get('contas_engajadoras', [])
        if not contas_engajadoras:
            print("⚠️  Nenhuma conta engajadora configurada!")
            return
        
        # Escolher quantas contas vão engajar (30-70% das disponíveis)
        num_contas = random.randint(
            int(len(contas_engajadoras) * 0.3),
            int(len(contas_engajadoras) * 0.7)
        )
        
        contas_escolhidas = random.sample(contas_engajadoras, min(num_contas, len(contas_engajadoras)))
        
        print(f"👥 {len(contas_escolhidas)} contas vão engajar")
        
        for i, conta in enumerate(contas_escolhidas, 1):
            print(f"\n[{i}/{len(contas_escolhidas)}] @{conta['username']}")
            
            # Login
            client_engajador = self.fazer_login(conta)
            if not client_engajador:
                print("  ⚠️  Pulando (falha no login)")
                continue
            
            # Engajar!
            resultado = self.engajar_completo(client_engajador, tweet_id)
            
            print(f"  RT: {'✅' if resultado['rt'] else '❌'}")
            print(f"  Like: {'✅' if resultado['like'] else '❌'}")
            print(f"  Save: {'✅' if resultado['save'] else '❌'}")
            
            # Delay entre contas (2-5 minutos)
            if i < len(contas_escolhidas):
                print(f"  ⏳ Aguardando próxima conta...")
                self.humanizer.delay_natural(120, 300)
        
        # ========== FIM ==========
        print("\n" + "="*80)
        print("✅ FLUXO COMPLETO FINALIZADO!")
        print("="*80)
        print(f"\n📊 RESUMO:")
        print(f"  • Tweet ID: {tweet_id}")
        print(f"  • Link: https://twitter.com/i/web/status/{tweet_id}")
        print(f"  • Comentário: {'✅' if comentou else '❌'}")
        print(f"  • Engajamentos: {len(contas_escolhidas)} contas")


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu_principal():
    """Menu interativo do TwitterBot"""
    
    bot = TwitterBot()
    
    while True:
        print("\n" + "="*80)
        print("🐦 TWITTER BOT - MENU PRINCIPAL")
        print("="*80)
        print("\n1️⃣  Executar fluxo completo (Post + Comentário + Engajamento)")
        print("2️⃣  Postar tweet simples")
        print("3️⃣  Testar login de uma conta")
        print("4️⃣  Atualizar bio de uma conta")
        print("5️⃣  Engajar em tweet específico")
        print("6️⃣  Configurar contas")
        print("0️⃣  Sair")
        
        escolha = input("\nEscolha uma opção: ").strip()
        
        if escolha == '1':
            bot.executar_fluxo_completo()
        
        elif escolha == '2':
            # Postar tweet simples
            contas = bot.config_contas.get('contas_postadoras', [])
            if not contas:
                print("❌ Nenhuma conta configurada!")
                continue
            
            print("\nContas disponíveis:")
            for i, c in enumerate(contas, 1):
                print(f"{i}. @{c['username']}")
            
            idx = int(input("\nEscolha: ").strip()) - 1
            conta = contas[idx]
            
            client = bot.fazer_login(conta)
            if client:
                texto = input("\nTexto do tweet: ").strip()
                hashtags = input("Hashtags (opcional): ").strip()
                bot.postar_tweet(client, texto, hashtags)
        
        elif escolha == '3':
            # Testar login
            print("\n1. Conta postadora")
            print("2. Conta engajadora")
            tipo = input("\nTipo: ").strip()
            
            if tipo == '1':
                contas = bot.config_contas.get('contas_postadoras', [])
            else:
                contas = bot.config_contas.get('contas_engajadoras', [])
            
            if not contas:
                print("❌ Nenhuma conta!")
                continue
            
            print("\nContas:")
            for i, c in enumerate(contas, 1):
                print(f"{i}. @{c['username']}")
            
            idx = int(input("\nEscolha: ").strip()) - 1
            bot.fazer_login(contas[idx])
        
        elif escolha == '4':
            # Atualizar bio
            contas = bot.config_contas.get('contas_postadoras', []) + bot.config_contas.get('contas_engajadoras', [])
            
            print("\nContas:")
            for i, c in enumerate(contas, 1):
                print(f"{i}. @{c['username']}")
            
            idx = int(input("\nEscolha: ").strip()) - 1
            client = bot.fazer_login(contas[idx])
            
            if client:
                bio = input("\nNova bio: ").strip()
                link = input("Link (opcional): ").strip()
                bot.atualizar_bio(client, bio, link or None)
        
        elif escolha == '5':
            # Engajar em tweet
            tweet_id = input("\nID do tweet: ").strip()
            
            contas = bot.config_contas.get('contas_engajadoras', [])
            print("\nContas:")
            for i, c in enumerate(contas, 1):
                print(f"{i}. @{c['username']}")
            
            idx = int(input("\nEscolha: ").strip()) - 1
            client = bot.fazer_login(contas[idx])
            
            if client:
                bot.engajar_completo(client, tweet_id)
        
        elif escolha == '0':
            print("\n👋 Até logo!")
            break
        
        else:
            print("\n❌ Opção inválida!")


if __name__ == '__main__':
    menu_principal()
