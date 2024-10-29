import requests

def obter_informacoes_cep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json"
    try:
        retorno = requests.get(url)
        retorno.raise_for_status()  # Lança uma exceção para códigos de status diferentes de 200
        dados = retorno.json()
        if 'erro' in dados:
            return None, "CEP não encontrado."
        logradouro = dados.get('logradouro', 'N/A')
        cidade = dados.get('localidade', 'N/A')
        return logradouro, cidade
    except requests.exceptions.RequestException as e:
        return None, f"Erro ao fazer a requisição: {e}"
    except ValueError:
        return None, "Erro ao decodificar o JSON."

cep = "01133-000"
logradouro, cidade = obter_informacoes_cep(cep)
if logradouro is not None:
    print(f"Logradouro: {logradouro} - Cidade: {cidade}")
else:
    print("Erro ao obter informações do CEP.")
