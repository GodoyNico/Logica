#3- Ler um número e verificar se ele é par ou impar. Quando for par armazenar esse valor em 'p' e quando for ímpar
#armazená-lo em 'i'. Exibir 'p' e 'i' no final do processamento.

num=int(input('Insira um número: '))

if num%2 == 0:
    p=num
    print(p)
    print('O número é par')
else:
    i=num
    print(i)
    print('O número é impar')

