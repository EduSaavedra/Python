import re
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
    
def par_impar(val):
    resto = val % 2
    if resto == 0:
        resultado = print (f'{val} é PAR!')
    else:
        resultado = print (f'{val} é IMPAR!')
    return resultado

print('PAR OU IMPAR?')
numero = input('Insira um número: ')

if (is_int(numero)):
    par_impar(int(numero))
else:
    print('Valor invalido.')