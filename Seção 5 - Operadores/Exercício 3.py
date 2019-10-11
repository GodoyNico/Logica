#3- Sabendo que a = 5, b = 4, c = 3 e d = 6, informe se as expressões abaixo são verdadeiras ou falsas

a=5
b=4
c=3
d=6

#A) (a > c) AND (c <= d)                 (X)Verdadeiro   ( )Falso

resultado_a=bool(a>c) and bool(c<=d)
print(resultado_a)

#B) (a + b) > 10 OR (a+b) == (c+d)       (X)Verdadeiro   ( )Falso

resultado_b=bool(a+b) > 10 or bool(a+b) == bool(c+d)
print(resultado_b)

#C) (a >= c) AND (d >= c)                (X)Verdadeiro   ( )Falso

resultado_c=bool(a>=c) and bool(d>=c)
print(resultado_c)

