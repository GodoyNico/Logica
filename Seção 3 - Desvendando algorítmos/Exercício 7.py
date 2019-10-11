##7- Tendo como dados de entrada a altura de uma pessoa, construa um algorítmo que calcule seu peso ideal, usando a seguinte fórmula:
##(72,7 * altura) - 58

#Insira sua altura
#Multiplique a altura por 72,7
#Subtraia 58 do valor obtido
#Mostre o resultado

altura=float(input('Insira a sua altura: '))
if altura < 3:
    multiplicação=float(altura)*72.7
    peso=float(multiplicação)-58
    print('Seu peso ideal e de {0} Kg'.format(peso))
else:
    multiplicação=(altura/100)*72.7
    peso = float(multiplicação)-58
    print('Seu peso ideal é de {0} Kg'.format(peso))

