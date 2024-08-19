num=int(input("Digite o numero de entradas "))
cont=0
som_sapo=som_rato=som_coelho=0
while cont<num:
    qnt=int(input("Digite a quantidade "))
    tipo=input("Digite o tipo S R ou C ")
    if tipo == 'S':
        som_sapo+=qnt
    elif tipo == 'R':
        som_rato+=qnt
    elif tipo == 'C':
        som_coelho+=qnt
    cont+=1
print("Total de cobaias: {}".format(som_coelho+som_rato+som_sapo))
print("Total de sapos {}".format(som_sapo))
print("Total de ratos {}".format(som_rato))
print("Total de coelhos {}".format(som_coelho))