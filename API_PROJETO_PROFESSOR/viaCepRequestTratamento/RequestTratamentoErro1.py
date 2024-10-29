import requests

cep = "01133-000"
url = f"http://viacep.com.br/ws/{cep}/json"
try:
    retorno = requests.get(url)
    retorno.raise_for_status()  # Lança uma exceção para códigos de status diferentes de 200
    dados = retorno.json()
    logradouro = dados.get('logradouro', 'N/A')
    cidade = dados.get('localidade', 'N/A')
    print(f"Logradouro: {logradouro} - Cidade: {cidade}")
except requests.exceptions.RequestException as e:
    print("Erro ao fazer a requisição:", e)
except ValueError:
    print("Erro ao decodificar o JSON.")
