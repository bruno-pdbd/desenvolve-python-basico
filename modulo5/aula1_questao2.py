import random
import math
min_n = 1
max_n = 20
n = random.randint(min_n, max_n)
valor = [random.randint(0, 100) for _ in range(n)]
soma = sum(valor)
raiz = math.sqrt(soma)
print("Quantidade de valores: {}".format(n))
print("Valores gerados: {}".format(valor))
print("Soma dos valores: {}".format(soma))
print("Raiz quadrada da soma: {:.2f}".format(raiz))