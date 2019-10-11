#5- João da Silva, pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 Kg)
#deve pagar uma multa de R$ 4.00 por Kg excedente. João precisa que você faça um algorismo que leia a variável 'p'
#(peso de peixes) e verifique se há excesso. Se houver, gravar na variável 'e' (excesso) e na variável 'm' (multa) o valor
#da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo 'zero'.

kg_peixe=int(20)
vm=int(4)
p=float(input('Insira o peso que a pescaria rendeu: '))
print()

if float(p > 50):
    e=float(p-50)
    m=e*vm
    lucro= p * kg_peixe - m
    print('O excesso de peso é de',e,'Kg.')
    print('O valor por cada Kg de excesso é R$ 4.00')
    print('O valor de multa a ser pago por João da Silva é de',m,'reais.')
    print('João teve {} reais de lucro.'.format(lucro))

else:
    lucro= p * kg_peixe
    print('A pescaria rendeu',p,'Kg.')
    print('Não houve excesso de peso.')
    print('Não existe multa a ser pega por João da Silva.')
    print('João teve {} reais de lucro.'.format(lucro))


#Inserir quanto pesca rendeu, lucro