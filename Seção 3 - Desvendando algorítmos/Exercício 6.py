##6- Faça um algorítmo que pergunte quanto você ganha por hora e o número de horas trabalhadas ao mês.
##Calcule e mostre o total do seu salário no referido mês.

#Insira a quantidade de horas que você trabalha por mês
#Insira o valor que você ganha por hora trabalhadas
#Multiplique a quantidade de horas pelo valor da hora
#Mostre o resultado

horas=input('Insira a quantidade de horas que você trabalha por mês: ')
valor=input('Insira o quanto você ganha por hora trabalhada: ')
salário=int(horas)*int(valor)
print('Seu salário mensal deve ser de R$',salário)
print('Seu salário mensal deve ser de R$ {0}'.format(salário))

