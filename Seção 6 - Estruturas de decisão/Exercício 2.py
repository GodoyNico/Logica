#2- Elabore um algorítmo que leia um número. Se positivo armazene-o em 'a', se for negativo, em 'b'. No final mostrar
#o resultado.

num=int(input('Digite um número: '))

if num>=0:
    a=num
    print('Número positivo')
    print(a)
else:
    b=num
    print('Número negativo')
    print(b)
