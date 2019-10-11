#4- Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algorítmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#Para homens: (72.7 * altura) - 58
#Para mulheres: (62.1 * altura) - 44.7


#altura=float(input('Insira sua altura: '))
#sexo=input('Insira seu sexo: ')

#if sexo == str('Masculino') or sexo == str('masculino'):
#    peso_ideal= (72.7 * float(altura)) - 58

#if sexo == str('Feminino') or sexo == str('feminino'):
#    peso_ideal= (62.1 * float(altura)) - 44.7

#print('Seu peso ideal é:',peso_ideal,'Kg.')

#Inserir variável que aceite m e cm

altura = float(input('Insira a sua altura: '))
sexo = input('Insira o seu sexo: ')

if altura >= 5:
    altura=altura/100

if sexo == str('Masculino') or sexo == str('masculino'):
    peso_ideal= (72.7 * altura) - 58

if sexo == str('Feminino') or sexo == str('feminino'):
    peso_ideal= (62.1 * altura) - 44.7

print('Seu peso ideal é: {:.3f} Kg.'.format(peso_ideal))