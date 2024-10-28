lista1=lista2=lista3=[]
quantlista1 = int(input("Quantos elementos terá na lista 1: "))
quantlista2 = int(input("Quantos elementos terá na lista 2: "))
for i in range(quantlista1):
    lista1.append(int(input("Digite o elemento da lista 1: ")))
for i in range(quantlista2):
    lista2.append(int(input("Digite o elemento da lista 2: ")))
for i in range(max(quantlista1, quantlista2)):
    if i < quantlista1:
        lista3.append(lista1[i])
    if i < quantlista2:
        lista3.append(lista2[i])
print(f"Lista intercalada: {lista3}")