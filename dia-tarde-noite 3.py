import re
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
    
def verifica_hora(val):
    if val >= 0 and val <= 11:
        resultado = print ('BOM DIA!')
    elif val >= 12 and val <= 17:
        resultado = print ('BOA TARDE!')
    elif val >= 18 and val <= 23:
        resultado = print ('BOA NOITE!')
    else:
        resultado = print('Hora inválida!')
    
    return resultado
#  -------------- fim da funcao de hora
#  INSERE HORA    
hora = input('Insira a hora (h): ')

#  RESULTADO
if (is_int(hora)):
    verifica_hora(int(hora))
else:
    print('Valor invalido.')
