# Números em python

# Inteiro - int
numero_int = 1

print("Inteiro =", numero_int)
# Decimal - float (Real com ponto flutuante)
numero_float = 1.1
pi = 3.14159

dizima_periodica = 10 / 3

print('Decimais =', numero_float, pi, dizima_periodica)

# função type
print("Tipo dizima = ", type(dizima_periodica))

# operacoes aritimetricas

num1 = 6
num2 = 5
# soma
soma = num1 + num2
print(num1, '+', num2, '=', soma)

# subtracao
subtracao = num1 - num2
print(num1, '-', num2, '=', subtracao)
# multiplicacao
multiplicacao = num1 * num2
print(num1, '*', num2, '=', multiplicacao)
# divisao
divisao = num1 / num2
print(num1, '/', num2, '=', divisao)

#divisao por zero nao existe
#error -> ZeroDivisionError: division by zero
num3 = 7
divisao = num1 / num3
print(num1, '/', num3, '=', divisao)    

#conversoes (cast)

print(divisao, int(divisao))
print(soma, float(soma))

#modulo - resto da divisao
mu = (num1 * num3)
mod = mu % num2 
print(mu, '%', num2, '=', mod)

#divisao inteira
div_int = mu // num2
print(mu, '//', num2, '=', div_int)
