"""
Script separado para atualizar bio usando API v1.1
"""

import tweepy
import json

# Carregar credenciais
with open('config/contas_twitter.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Escolher conta
print("Contas disponíveis:")
contas = config['contas_postadoras']
for i, c in enumerate(contas, 1):
    print(f"{i}. @{c['username']}")

idx = int(input("\nEscolha: ")) - 1
conta = contas[idx]

# Autenticar com API v1.1
auth = tweepy.OAuthHandler(conta['api_key'], conta['api_secret'])
auth.set_access_token(conta['access_token'], conta['access_token_secret'])
api = tweepy.API(auth)

# Verificar autenticação
me = api.verify_credentials()
print(f"\n✅ Autenticado: @{me.screen_name}")
print(f"Bio atual: {me.description}")

# Nova bio
nova_bio = input("\nNova bio: ")
link = input("Link (opcional): ")

if link:
    nova_bio = f"{nova_bio}\n\n🔗 {link}"

# Atualizar
api.update_profile(description=nova_bio)
print("\n✅ Bio atualizada!")

# Verificar
me = api.verify_credentials()
print(f"\nBio nova: {me.description}")