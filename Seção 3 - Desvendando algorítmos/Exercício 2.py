##2- Fazer um algorítmo para "Calcular o estoque médio de uma peça", sendo que:
##Estoque médio = (quantidade mínima + quantidade máxima) / 2

#    Inserir a quantminima
 #   Inserir a quantmaxima
  #  Somar quantminima e quantmaxima
   # Dividir o resultado da soma por 2
    #Mostrar o resultado da divisão

quantminima=input('Digite a quantidade mínima do estoque: ')
quantmaxima=input('Digite a quantidade máxima do estoque: ')
soma=int(quantminima)+int(quantmaxima)
média=int(soma)/2
print('O estoque médio é de {0} itens'.format(int(média)))

