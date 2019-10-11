##3- Teste o algorítmo anterior com os dados definidos por você

#estoquemédio= quantminima + quantmaxima) / 2
#_________________________________________________________
#| Quantidade mínima | Quantidade máxima | Estoque médio |
#|--------------------------------------------------------
#|        10         |        10         |       10      |
#|--------------------------------------------------------
#|        13         |        87         |       50      |
#---------------------------------------------------------

quantminima=input('Insira a quantidade mínima do estoque: ')
quantmaxima=input('Insira a quantidade máxima do estoque: ')
média=(int(quantminima)+int(quantmaxima))/2
print('A média do estoque é: {0}'.format(int(média)))

