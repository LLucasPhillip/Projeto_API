# Primeiro passo com API's em Python

## Request com Python

O arquivo `request.py` contém um exemplo de como fazemos uma requisição para uma API.

Para fins didáticos vamos utilizar a [API ViaCEP](https://viacep.com.br).

## Instalando as dependências

Vamos criar um exemplo de uma função Python que faz uma requisição REST utilizando a biblioteca requests.

Primeiraramente preciamos instalar a biblioteca requests. O `pip` é uma ferramenta que permite instalar pacotes Python facilmente. Você pode instalar o requests utilizando o pip da seguinte maneira:

```cmd
pip install requests
```

## Atividade ViaCEP

```python
import requests

cep = "01133-000"
url = f"http://viacep.com.br/ws/{cep}/json"
retorno = requests.get(url)
dici = retorno.json()

logradouro = dici['logradouro']
cidade = dici['localidade']
print(f"{logradouro} - {cidade}")
retorno.status_code #(deveria ser 200 se deu certo)
```
