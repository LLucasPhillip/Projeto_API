import re
import requests

def formatar_cep(cep):
    cep_formatado = re.sub(r'\D', '', cep)  # Remove caracteres não numéricos
    if len(cep_formatado) != 8:
        return None
    return cep_formatado

def obter_informacoes_cep(cep):
    cep_formatado = formatar_cep(cep)
    if not cep_formatado:
        return None, "CEP inválido."
    url = f"http://viacep.com.br/ws/{cep_formatado}/json"
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

cep = input("Digite o CEP: ")
logradouro, cidade = obter_informacoes_cep(cep)
if logradouro is not None:
    print(f"Logradouro: {logradouro} - Cidade: {cidade}")
else:
    print("Erro ao obter informações do CEP.")
