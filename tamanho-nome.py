import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)

def verifica_tamanho(val):
    tamanho = len(val)
    if tamanho <= 4:
        resultado = print('Seu nome é curto. Caracteres: ', tamanho)
    elif tamanho > 4 and tamanho <= 6:
        resultado = print('Seu nome é normal. Caracteres: ', tamanho)
    elif tamanho > 6:
        resultado = print('Seu nome é muito grande. Caracteres: ', tamanho)
    return resultado
#  FIM DAS FUNCOES -------------------------------------------

nome = input('Insira seu primeiro nome: ')

if is_number(nome) == False:
    verifica_tamanho(nome)
else:
    print('O nome ' + nome + ' é inválido.')
