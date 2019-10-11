#7- Desenvolva um algorítmo que:

#A) Leia 4 (quatro) números;
#B) Calcule o quadrado de cada um;
#C) Se o valor resultante do quadrado do terceiro for >= 1000, imprima-o e finalize;
#D) Caso contrário, imprima os valores lidos e seus respectivos quadrados.

n1=input('Digite o primeiro número: ')
n2=input('Digite o segundo número: ')
n3=input('Digite o terceiro número: ')
n4=input('Digite o quarto número: ')

q1=int(n1)**int(2)
q2=int(n2)**int(2)
q3=int(n3)**int(2)
q4=int(n4)**int(2)

if q3>=1000:
    print(q3)
    print('Tudo top!')
else:
    print('O primeiro valor é',n1,'e seu quadrado é',q1)
    print('O segundo valor é',n2,'e seu quadrado é',q2)
    print('O terceiro valor é',n3,'e seu quadrado é',q3)
    print('O quarto valor é',n4,'e seu quadrado é',q4)

