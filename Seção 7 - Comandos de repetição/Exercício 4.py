#4- Construa um algotítmo que leia 10 valoes inteiros e positivos e:

#A) Encontre o maior valor
#B) Encontre o menor valor
#C) Calcule a média dos números lidos

maior = -999
menor = 999
soma = 0

for n in range (1,11):
    valor = int(input('Informe um valor: '))
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        soma = soma + valor
    else:
        valor = int(input('Informe um valor: '))
media = soma / 10

print('0 maior número é {0}'.format(maior))
print('O menor valor é {0}'.format(menor))
print('A média dos números é {0}'.format(media))
