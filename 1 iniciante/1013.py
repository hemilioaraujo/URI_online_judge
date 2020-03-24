entrada = input()

numeros = [int(numero) for numero in entrada.split(' ')]

maior = max(numeros)

print('{} eh o maior'.format(maior))