"""
🤖 TWITTER BOT - AUTOMAÇÃO 24/7
Posta automaticamente 3x por dia em horários aleatórios (8h - 23h)
"""

import schedule
import time
import random
from datetime import datetime, timedelta
from app.twitter_bot import TwitterBot


class AutoPoster:
    """Gerenciador de postagens automáticas"""
    
    def __init__(self, posts_por_dia=3, hora_inicio=8, hora_fim=23):
        self.posts_por_dia = posts_por_dia
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.horarios_agendados = []
        self.posts_hoje = 0
        
    def gerar_horarios_aleatorios(self):
        """
        Gera horários aleatórios entre hora_inicio e hora_fim
        Garante pelo menos 2 horas de distância entre posts
        """
        horarios = []
        
        # Dividir o dia em slots
        total_horas = self.hora_fim - self.hora_inicio
        
        # Intervalo mínimo entre posts (em horas)
        intervalo_minimo = total_horas / (self.posts_por_dia + 1)
        
        for i in range(self.posts_por_dia):
            # Calcular janela para este post
            inicio_janela = self.hora_inicio + (i * intervalo_minimo)
            fim_janela = inicio_janela + intervalo_minimo
            
            # Gerar hora aleatória dentro da janela
            hora = random.uniform(inicio_janela, fim_janela)
            horas = int(hora)
            minutos = int((hora - horas) * 60)
            
            horarios.append(f"{horas:02d}:{minutos:02d}")
        
        # Ordenar horários
        horarios.sort()
        
        return horarios
    
    def agendar_posts_do_dia(self):
        """Agenda os posts do dia em horários aleatórios"""
        
        # Limpar agendamentos antigos
        schedule.clear()
        
        # Gerar novos horários
        self.horarios_agendados = self.gerar_horarios_aleatorios()
        
        print("\n" + "="*80)
        print(f"📅 HORÁRIOS DE HOJE ({datetime.now().strftime('%d/%m/%Y')})")
        print("="*80)
        
        for i, horario in enumerate(self.horarios_agendados, 1):
            # Agendar cada post
            schedule.every().day.at(horario).do(self.executar_post, numero=i)
            print(f"   {i}º post: {horario}")
        
        # Agendar renovação dos horários para meia-noite
        schedule.every().day.at("00:01").do(self.renovar_horarios)
        
        print("="*80)
        print()
        
        self.posts_hoje = 0
    
    def renovar_horarios(self):
        """Renova os horários para o próximo dia"""
        print("\n🔄 Meia-noite! Gerando novos horários para hoje...")
        self.agendar_posts_do_dia()
    
    def executar_post(self, numero):
        """Executa um post"""
        print("\n" + "="*80)
        print(f"🤖 EXECUTANDO POST {numero}/{self.posts_por_dia}")
        print(f"⏰ Horário: {datetime.now().strftime('%H:%M:%S')}")
        print("="*80)
        
        try:
            bot = TwitterBot()
            bot.executar_fluxo_completo()
            
            self.posts_hoje += 1
            
            print("\n" + "="*80)
            print(f"✅ POST {numero}/{self.posts_por_dia} CONCLUÍDO!")
            print(f"📊 Posts hoje: {self.posts_hoje}/{self.posts_por_dia}")
            print("="*80)
            
        except Exception as e:
            print(f"\n❌ ERRO ao executar post {numero}: {e}")
            print("⚠️  Tentando novamente no próximo horário...")
    
    def mostrar_status(self):
        """Mostra próximo post agendado"""
        agora = datetime.now()
        
        # Encontrar próximo horário
        proximo = None
        for horario_str in self.horarios_agendados:
            h, m = map(int, horario_str.split(':'))
            horario_dt = agora.replace(hour=h, minute=m, second=0)
            
            if horario_dt > agora:
                proximo = horario_dt
                break
        
        if proximo:
            diferenca = proximo - agora
            horas = int(diferenca.total_seconds() // 3600)
            minutos = int((diferenca.total_seconds() % 3600) // 60)
            
            print(f"\r⏳ Próximo post: {proximo.strftime('%H:%M')} (em {horas}h {minutos}min) | Posts hoje: {self.posts_hoje}/{self.posts_por_dia}", end='', flush=True)
        else:
            print(f"\r✅ Todos os posts de hoje concluídos! ({self.posts_hoje}/{self.posts_por_dia}) | Próximo: amanhã", end='', flush=True)


def main():
    """Função principal"""
    
    print("\n" + "="*80)
    print("🐦 TWITTER BOT - AUTOMAÇÃO 24/7")
    print("="*80)
    print("\n⚙️  CONFIGURAÇÕES:")
    print("   • Posts por dia: 3")
    print("   • Horário: 08:00 - 23:00")
    print("   • Distribuição: Aleatória (mínimo 2h entre posts)")
    print("\n💡 DICA: Deixe esta janela aberta 24/7")
    print("   Para parar: CTRL+C")
    print("="*80)
    
    # Criar autoposter
    poster = AutoPoster(posts_por_dia=3, hora_inicio=8, hora_fim=23)
    
    # Agendar posts do dia
    poster.agendar_posts_do_dia()
    
    print("\n🚀 Bot ativo! Aguardando horários...")
    print()
    
    # Loop infinito
    try:
        while True:
            schedule.run_pending()
            poster.mostrar_status()
            time.sleep(30)  # Atualiza a cada 30 segundos
    
    except KeyboardInterrupt:
        print("\n\n" + "="*80)
        print("👋 Bot encerrado pelo usuário")
        print("="*80)
        print(f"\n📊 Estatísticas de hoje:")
        print(f"   Posts realizados: {poster.posts_hoje}/{poster.posts_por_dia}")
        print()


if __name__ == '__main__':
    main()