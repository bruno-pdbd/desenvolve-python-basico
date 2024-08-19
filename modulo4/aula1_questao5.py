num=int(input("Digite quantas idades serão lidas "))
som=med=0
while med<num:
    idade=int(input("Digite uma idade "))
    som+=idade
    med+=1
print("soma das idades {}".format(som))
print("media das idades {}".format(som/num))