"""
📊 CALCULADOR DE LIMITES - TWITTER FREE TIER
==============================================

Calcula quantos posts você pode fazer com API gratuita
"""

import json
from datetime import datetime, timedelta

class TwitterFreeCalculator:
    """Calculador para Twitter API Free Tier"""
    
    def __init__(self):
        # Limites do FREE TIER
        self.LIMITE_TWEETS_MES = 1500
        self.LIMITE_TWEETS_DIA = 50
        self.LIMITE_LEITURA_MES = 500000
        
    def calcular_estrategia(self, num_postadoras, num_engajadoras):
        """
        Calcula melhor estratégia com contas FREE
        
        Args:
            num_postadoras: Número de contas postadoras
            num_engajadoras: Número de contas engajadoras
        """
        
        print("="*70)
        print("📊 CALCULADOR - TWITTER FREE TIER")
        print("="*70)
        
        print(f"\n📌 CONFIGURAÇÃO:")
        print(f"   Contas Postadoras: {num_postadoras}")
        print(f"   Contas Engajadoras: {num_engajadoras}")
        
        # Cálculos para POSTADORAS
        print(f"\n🔥 CONTAS POSTADORAS ({num_postadoras} contas)")
        print("─"*70)
        
        tweets_totais_mes = num_postadoras * self.LIMITE_TWEETS_MES
        tweets_totais_dia = num_postadoras * self.LIMITE_TWEETS_DIA
        
        print(f"   Limite total/mês: {tweets_totais_mes:,} tweets")
        print(f"   Limite total/dia: {tweets_totais_dia} tweets")
        
        # Considerando: 1 post + 1 comentário = 2 tweets
        posts_com_comentario_mes = tweets_totais_mes // 2
        posts_com_comentario_dia = tweets_totais_dia // 2
        
        print(f"\n   Posts com comentário:")
        print(f"      • Por mês: {posts_com_comentario_mes:,} posts")
        print(f"      • Por dia: {posts_com_comentario_dia} posts")
        print(f"      • Por conta/dia: {posts_com_comentario_dia // num_postadoras}")
        
        # Cálculos para ENGAJADORAS
        print(f"\n💎 CONTAS ENGAJADORAS ({num_engajadoras} contas)")
        print("─"*70)
        
        # RT não conta como tweet, mas Like precisa de API call
        # Considerando: RT + Like + Save = 3 ações por post
        
        acoes_totais_mes = num_engajadoras * self.LIMITE_TWEETS_MES
        acoes_totais_dia = num_engajadoras * self.LIMITE_TWEETS_DIA
        
        print(f"   Ações totais/mês: {acoes_totais_mes:,}")
        print(f"   Ações totais/dia: {acoes_totais_dia}")
        
        # Cada engajamento = RT + Like + Save (3 ações)
        engajamentos_dia = acoes_totais_dia // 3
        
        print(f"\n   Engajamentos completos/dia: {engajamentos_dia}")
        print(f"   Por post: ~{engajamentos_dia // posts_com_comentario_dia} contas engajam")
        
        # RESUMO FINAL
        print(f"\n{'='*70}")
        print("📈 RESUMO DA ESTRATÉGIA")
        print(f"{'='*70}")
        
        print(f"\n🎯 CAPACIDADE DIÁRIA:")
        print(f"   • {posts_com_comentario_dia} posts (com comentário)")
        print(f"   • {engajamentos_dia} engajamentos completos")
        print(f"   • ~{engajamentos_dia // posts_com_comentario_dia} contas engajam por post")
        
        print(f"\n📅 CAPACIDADE MENSAL:")
        print(f"   • {posts_com_comentario_mes:,} posts (com comentário)")
        print(f"   • {acoes_totais_mes:,} engajamentos")
        
        # RECOMENDAÇÕES
        print(f"\n{'='*70}")
        print("💡 RECOMENDAÇÕES")
        print(f"{'='*70}")
        
        # Usar 70% da capacidade (margem de segurança)
        posts_recomendados = int(posts_com_comentario_dia * 0.7)
        
        print(f"\n✅ Use 70% da capacidade (margem de segurança):")
        print(f"   • {posts_recomendados} posts/dia")
        print(f"   • {posts_recomendados * 30} posts/mês")
        
        # Distribuição de horários
        print(f"\n⏰ DISTRIBUIÇÃO RECOMENDADA:")
        
        intervalo_horas = 24 / posts_recomendados
        
        print(f"   • Postar a cada {intervalo_horas:.1f} horas")
        print(f"   • Ou: {posts_recomendados // num_postadoras} posts/dia por conta")
        
        horarios = []
        hora_atual = 7  # Começar às 7h
        
        print(f"\n   Horários sugeridos:")
        for i in range(posts_recomendados):
            horarios.append(f"{int(hora_atual):02d}:{int((hora_atual % 1) * 60):02d}")
            print(f"      {i+1}. {horarios[-1]}")
            hora_atual += intervalo_horas
            if hora_atual >= 24:
                hora_atual -= 24
        
        # CUSTO
        print(f"\n{'='*70}")
        print("💰 ANÁLISE DE CUSTO")
        print(f"{'='*70}")
        
        print(f"\n🆓 FREE TIER:")
        print(f"   Custo: R$ 0,00/mês")
        print(f"   Capacidade: {posts_com_comentario_mes:,} posts/mês")
        print(f"   Custo por post: R$ 0,00")
        
        print(f"\n💵 COMPARAÇÃO COM PAGO:")
        print(f"   Basic ($100/mês): 3.000 tweets/mês")
        print(f"      → Você tem: {tweets_totais_mes:,} tweets/mês (GRÁTIS!)")
        
        if tweets_totais_mes > 3000:
            print(f"      ✅ Capacidade {tweets_totais_mes / 3000:.1f}x MAIOR que o plano pago!")
        
        print(f"\n{'='*70}\n")
        
        return {
            'posts_dia': posts_recomendados,
            'posts_mes': posts_recomendados * 30,
            'horarios': horarios
        }
    
    def exemplo_configuracoes(self):
        """Mostra exemplos de configurações"""
        
        print("\n" + "="*70)
        print("🎯 EXEMPLOS DE CONFIGURAÇÃO")
        print("="*70)
        
        configs = [
            {"postadoras": 3, "engajadoras": 10, "descricao": "Iniciante"},
            {"postadoras": 5, "engajadoras": 15, "descricao": "Intermediário"},
            {"postadoras": 5, "engajadoras": 20, "descricao": "Avançado"},
            {"postadoras": 10, "engajadoras": 30, "descricao": "Profissional"}
        ]
        
        for config in configs:
            print(f"\n📌 {config['descricao'].upper()}:")
            print(f"   {config['postadoras']} postadoras + {config['engajadoras']} engajadoras")
            
            posts_dia = (config['postadoras'] * 50) // 2
            posts_mes = posts_dia * 30
            
            print(f"   → {posts_dia} posts/dia ({posts_mes:,}/mês)")
            print(f"   → R$ 0,00/mês (100% GRÁTIS)")


def main():
    """Menu interativo"""
    
    calc = TwitterFreeCalculator()
    
    print("\n" + "="*70)
    print("🆓 CALCULADOR TWITTER FREE TIER")
    print("="*70)
    
    print("\n💡 Calcule quantos posts você pode fazer GRATUITAMENTE!")
    
    # Mostrar exemplos
    calc.exemplo_configuracoes()
    
    print("\n" + "="*70)
    print("\n❓ CALCULAR PARA SUA CONFIGURAÇÃO")
    print("="*70)
    
    try:
        num_postadoras = int(input("\nQuantas contas POSTADORAS? (ex: 5): ") or "5")
        num_engajadoras = int(input("Quantas contas ENGAJADORAS? (ex: 20): ") or "20")
        
        resultado = calc.calcular_estrategia(num_postadoras, num_engajadoras)
        
        # Salvar configuração recomendada
        print("\n💾 Salvando configuração recomendada...")
        
        config_recomendada = {
            "contas_postadoras": num_postadoras,
            "contas_engajadoras": num_engajadoras,
            "posts_por_dia": resultado['posts_dia'],
            "posts_por_mes": resultado['posts_mes'],
            "horarios_sugeridos": resultado['horarios'],
            "modo": "FREE_TIER",
            "custo_mensal": 0,
            "gerado_em": datetime.now().isoformat()
        }
        
        with open('config/twitter_config_recomendada.json', 'w', encoding='utf-8') as f:
            json.dump(config_recomendada, f, indent=2, ensure_ascii=False)
        
        print("✅ Salvo em: config/twitter_config_recomendada.json")
        
    except ValueError:
        print("\n❌ Valor inválido!")
    except KeyboardInterrupt:
        print("\n\n👋 Cancelado!")


if __name__ == '__main__':
    main()
