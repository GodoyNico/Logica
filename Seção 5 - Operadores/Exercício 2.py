#2- Sabendo que a = 3, b = 7 e c = 4, informe se as expressões abaixo são verdadeiras ou falsas

a=3
b=7
c=4

#A) (a+c) > b       ( )Verdadeiro   (X)Falso

resultado_a= int(a+c) > int(b)
print(resultado_a)

#B) b >= (a+2)      (X)Verdadeiro   ( )Falso

resultado_b= int(b) >= int(a+2)
print(resultado_b)

#C) c == (b-a)      (X)Verdadeiro   ( )Falso

resultado_c= int(c) == int(b-a)
print(resultado_c)

#D) (b+a) <= c      ( )Verdadeiro   (X)Falso

resultado_d= int(b+a) <= int(c)
print(resultado_d)

#E) (c+a) > b       ( )Verdadeiro   (X)Falso

resultado_e= int(c+a) > int(b)
print(resultado_e)
