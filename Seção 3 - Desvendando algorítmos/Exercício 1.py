##Seção 3 - Exercícios

#1- Identificar os dados de entrada, processamento e saída no algorítmo abaixo:

#receber o código da peça
#receber o valor da peça
#receber a quantidade de peças
#calcular o valor total da peça (quantidade * valor da peça)
#mostrar o código da peça e seu valor total

#   Entradas:
 #       - Receber o código da peça
  #      - Receber o valor da peça
   #     - Receber a quantidade de peças
    
#    Processamento:
 #       - Calcular o valor total das peças
  #      (quantidade * valor da peça)

#    Saída:
 #       - Mostrar o código da peça
  #      - Mostrar o valor total

código=input('Insira o código da peça: ')
valor=input('Insira o valor da peça: ')
quantidade=input('Insira a quantidade de peças: ')

total=int(quantidade)*int(valor)

print('O código da peça é:',código)
print('O total da compra é:', total)

