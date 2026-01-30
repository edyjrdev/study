# tratamento de exceções

numero_usr = input('Digite um número inteiro: ')

try:
    numero = int(numero_usr)  # ValueError
    divisao_num = 10 / numero  # ZeroDivisionError
except ValueError:  # ValueError: Exceção específica
    print(f'{numero_usr} não é uma valor válido.')
    raise ValueError('Valor inválido, necessário finailizar programa.')  # Provocar erro
except ZeroDivisionError:  # ZeroDivisionError: Exceção específica
    print(f'Não é possível dividir por zero.')
except Exception as e:  # Exception - para exceções genéricas
    print(f'Erro: {e}')
else:  # faz somente sem erro
    print(divisao_num) # Somente se não deu erro.
    print('Processamento finalizado sem erro...')
finally:  # faz com erro ou sem
    print('Encerramento do programa.') 