#1- Ler uma variável numérica n e imprimi-la somente se a mesma for maior que 100, caso contrário imprimi-la com o
#valor zero.

n=int(input('Insira um número: '))

while n <= 100:
    print('Numero menor que 100')
    n=int(input('Insira um número: '))
else:
    print('OK, número maior que 100, o número é {0}'.format(n))

