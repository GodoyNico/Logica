#1- Tendo as variáveis salário, ir e salliq, e considerando os valores abaixo, informe se as expressões são verdadeiras ou falsas

#|-----------------------------------------------------------------------|
#| Salário |   Ir  | Salliq |       Expressão      | Verdadeiro ou falso |
#|-----------------------------------------------------------------------|
#| 100,00  |  0,00 | 100,00 |  (salliq >= 100,00)  |     Verdadeiro      |
#|-----------------------------------------------------------------------|
#| 200,00  | 10,00 | 190,00 |  (salliq < 190,00)   |       Falso         |
#|-----------------------------------------------------------------------|
#| 300,00  | 15,00 | 285,00 | (salliq = salario+ir)|       Falso         |
#|-----------------------------------------------------------------------|

salario1=100.00
ir1=0.00
salliq1=100.00

resultado1=bool(salliq1 >= 100.00)

salario2=200.00
ir2=10.00
salliq2=190.00

resultado2=bool(salliq2 < 190.00)

salario3=300.00
ir3=15.00
salliq3=285.00

resultado3=bool(salliq3 == salario3+ir3)

total_salario=float(salario1)+float(salario2)+float(salario3)
total_ir=float(ir1)+float(ir2)+float(ir3)
total_salliq=float(salliq1)+float(salliq2)+float(salliq3)

print(resultado1)
print(resultado2)
print(resultado3)

