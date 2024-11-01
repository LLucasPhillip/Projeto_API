from datetime import datetime
import re

def formatar_data(data_str):
    """
    Formata uma string de data no formato 'dd/mm/aaaa' para 'aaaa-mm-dd'.
    """
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        return data.strftime('%Y-%m-%d')
    except ValueError:
        raise ValueError('Data deve estar no formato dd/mm/aaaa.')

def validar_email(email):
    """
    Valida se um email está no formato correto.
    """
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        return True
    return False

def calcular_idade(data_nascimento):
    """
    Calcula a idade a partir da data de nascimento.
    """
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def gerar_codigo_unico(prefixo):
    """
    Gera um código único com um prefixo e um número aleatório.
    """
    import random
    codigo = f"{prefixo}-{random.randint(1000, 9999)}"
    return codigo
