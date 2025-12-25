"""
Humanizer - Simula comportamento humano
"""

import random
import time


class Humanizer:
    """Humaniza ações para evitar detecção"""
    
    def __init__(self, nivel='alto'):
        self.nivel = nivel
        
        self.configs = {
            'baixo': {'delay_min': 10, 'delay_max': 30},
            'medio': {'delay_min': 30, 'delay_max': 60},
            'alto': {'delay_min': 30, 'delay_max': 90}
        }
        
        self.config = self.configs.get(nivel, self.configs['alto'])
        print(f"✅ Humanizer: nível {nivel}")
    
    def delay_natural(self, min_sec=None, max_sec=None):
        """Delay aleatório personalizado"""
        if min_sec is None:
            min_sec = self.config['delay_min']
        if max_sec is None:
            max_sec = self.config['delay_max']
        
        delay = random.uniform(min_sec, max_sec)
        print(f"⏳ Aguardando {delay:.1f}s...")
        time.sleep(delay)
        return delay
    
    def delay_curto(self):
        """Delay curto: 5-15 segundos"""
        return self.delay_natural(5, 15)
    
    def delay_medio(self):
        """Delay médio: 30-90 segundos"""
        return self.delay_natural(30, 90)
    
    def delay_longo(self):
        """Delay longo: 2-5 minutos"""
        return self.delay_natural(120, 300)
    
    def simular_digitacao(self, texto):
        """Simula digitação humana"""
        chars_por_seg = random.uniform(3, 6)
        tempo = len(texto) / chars_por_seg
        print(f"⌨️  Digitando {len(texto)} caracteres ({tempo:.1f}s)...")
        time.sleep(tempo)
        return tempo