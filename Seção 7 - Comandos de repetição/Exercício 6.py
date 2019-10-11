#6- Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10. O usuário deve informar de qual
#número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    #Tabuada de 5:
    #5 x 1 = 5
    #5 x 2 = 10
    #...
    #5 x 10 = 50

numero=int(input('Insira um número entre 1 e 10 que deseja ver a tabuada: '))

while numero < 1 or numero > 10:
    numero=int(input('Insira um número entre 1 e 10 que deseja ver a tabuada: '))
print('Tabuada de {0}'.format(numero))
for n in range (1,11):
    print('{0} x {1} = {2}'.format(numero,n,(numero * n)))
