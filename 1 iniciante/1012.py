entrada = input()
A, B, C = entrada.split(' ')

A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

area_triangulo_retangulo = (A * C) / 2
area_circulo = pi * C ** 2
area_trapezio = ((A + B) * C) / 2
area_quadrado = B ** 2
area_retangulo = A * B

print('TRIANGULO: {:.3f}'.format(area_triangulo_retangulo))
print('CIRCULO: {:.3f}'.format(area_circulo))
print('TRAPEZIO: {:.3f}'.format(area_trapezio))
print('QUADRADO: {:.3f}'.format(area_quadrado))
print('RETANGULO: {:.3f}'.format(area_retangulo))