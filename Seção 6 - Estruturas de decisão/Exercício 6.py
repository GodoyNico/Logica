#6- Elabore um algorítmo que leia as variáveis 'c' e 'n', respectivamente código e número de horas trabalhadas de um
#operário. Calcule o salário sabendo-se que ele ganha R$ 10.00 por hora. Quando o número de horas exceder a 50 calcule
#o excesso de pagamento armazenando-o na variável 'e'. Caso contrário zerar tal variável. A hora excedente de trabalho
#vale R$ 20.00. No final do processamento imprimir o salário total e o salário excedente.

n=float(input('Insira o número de horas trabalhadas: '))
c=0

if (n)>50:
    salário_normal=float(500)
    salário_extra=(n-50)*20
    salário_total=(salário_normal+salário_extra)
    print(salário_normal,'mais',salário_extra)
    print(salário_total)
else:
    print('Tchuale!')
