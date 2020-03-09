input1 = input()
input2 = input()

c1, q1, v1 = input1.split(' ')
c2, q2, v2 = input2.split(' ')

valor_a_pagar = (int(q1) * float(v1)) + (int(q2) * float(v2))

print('VALOR A PAGAR: R$ {:.2f}'.format(valor_a_pagar))