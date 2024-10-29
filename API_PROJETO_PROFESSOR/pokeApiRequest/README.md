# Atividade - POKEAPI

1. Importando a biblioteca requests.

2. Definir a função (pode ser qualquer nome) `get_request(nome_pokemon)`

OBS: Vamos passar um parametro chamado `nome_pokemon` para trazer insformações daquele pokemon.

3. Criar a URL da API (Pode ser como uma variavel)

4. Fazer a requisição HTTP.

```python
  resposta = requests.get(url)
```

5. Acessando os dados da resposta

```python
  dados = resposta.json()
```

6. Retornando os dados

```python
  return dados
```

7 . Usando a função `get_request(nome_pokemon)`

```python
  dados_da_requisicao = get_request("pikachu")
  print(dados_da_requisicao)
```

## Tratando os dados

Traga para o Usuario:

1. Nome do pokemon
2. Tipo do Pokemons
3. Movimentos (ataques)

## Movimentos

URL DE REFERÊNCIA: https://pokeapi.co/api/v2/pokemon/pikachu

`moves` é uma lista de dicionários dentro dos dados do Pokémon.
`move` é um dicionário dentro dessa lista.
Dentro do loop, `move` é um dicionário representando um movimento específico do Pokémon.
logo, `move['move']` acessa um dicionário associado a um movimento específico.

E ` moves["move"]["name"]` acessa o nome, associado ao movimento especifico.
