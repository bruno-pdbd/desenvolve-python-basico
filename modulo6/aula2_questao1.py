import random
valor=[]
for i in range (20):
    num=random.randint(-100,100)
    valor.append(num)
valor_ord=sorted(valor)
maior=max(valor)
maior=[i for i,v in enumerate(valor) if v==maior]
menor=min(valor)
menor=[i for i,v in enumerate(valor) if v==menor]
print(valor_ord)
print(valor)
print(maior)
print(menor)