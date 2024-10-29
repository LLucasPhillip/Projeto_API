import requests

def get_request(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon.lower()}"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

dados_da_requisicao = get_request("pikachu")

nome_pokemon = dados_da_requisicao['name']
tipos = [tipo['type']['name'] for tipo in dados_da_requisicao['types']]
movimentos = [move['move']['name'] for move in dados_da_requisicao['moves']]

print(f"Nome: {nome_pokemon.capitalize()}")
print("Tipos:", ", ".join(tipos).capitalize())
print("Movimentos:", ", ".join(movimentos).capitalize())
