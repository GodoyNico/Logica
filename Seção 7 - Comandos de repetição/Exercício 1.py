#1- Faça um algorítmo que determine o maior entre N números. A condição de parada é a entrada de um valor 0, ou seja, o algorítmo deve
#ficar calculando o maior até que a entrada seja igual a 0 (ZERO).

maior=0
n=int(input('Digite um número: '))

while n!=0:
    if n > maior:
        maior = n
    n = int(input('Digite um número: '))
print('O maior número é {0}'.format(maior))

#Vou começar a codar bebado
menor = 0

n= int(input('Fala o menor grau de bebado de 1 a 10'))

