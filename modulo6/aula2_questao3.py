import random
lista1=[]
for i in range (20):
    num=random.randint(0,50)
    lista1.append(num)
lista2=[]
for i in range (20):
    num=random.randint(0,50)
    lista2.append(num)
inter=[]
for elemento in lista1:
    if elemento in lista2 and elemento not in inter:
        inter.append(elemento)
inter.sort()
for i in inter:
    print("{}:({},{})".format(i,lista1.count(i),lista2.count(i)))
print("lista1 = {}".format(lista1))
print("lista2 = {}".format(lista2))