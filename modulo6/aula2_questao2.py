import random
num_elementos=random.randint(5,20)
valor=[]
for i in range(num_elementos):
    valor.append(random.randint(1,10))
print(valor)
print(sum(valor))
print(sum(valor)/len(valor))