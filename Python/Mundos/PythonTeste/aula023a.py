# Tratamento de erro e excecoes:
# Exceptions:
# Link: https://docs.python.org/3/library/exceptions.html
# -------------------------------------------

#Tratamento de excecoes e Erros:

'''
try: #Tente fazer alguma coisa

# Operacoes

except:  #Senao, acontecera uma excecao

# Falha

else:  #Deu certo

finally: # Sempre sera executado

'''
# else e finally sao opcionais!

# Mostrando os erros que deram no "except":

# except Exception as erro:

# print(f'O problema encontrado foi: {erro.__class__}')

# -----------------------------------------------------------------------------------------------------------------------------------------

'''
try:         # Tentando algo
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:      # Se der algo errado no code acima, o except sera lido e vai mostrar o tipo de erro encontrado.
    print(f'Infelizmente tivemos um problema!\nO erro encontrado foi: {erro.__class__}')
else:        # Se der tudo certo no code do try, nao tiver nada errado, o comando else sera executado. Tornando, assim, o resultado.
    print(f'O resultado e: {r:.1f}')
finally:
    print('\nVolte sempre! Muito obrigado!')
'''

# -----------------------------------------------------------------------------------------------------------------------------------------

try:         # Tentando algo
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
             # Pode conter varios valores except para serem tratados no seu code
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print('Nao e possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}')
else:        # Se der tudo certo no code do try, nao tiver nada errado, o comando else sera executado. Tornando, assim, o resultado.
    print(f'O resultado e: {r:.1f}')
finally:
    print('\nVolte sempre! Muito obrigado!')
