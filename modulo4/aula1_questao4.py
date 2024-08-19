num=int(input("Digite um numero "))
maior=0
while num>0:
    x=int(input("Digite outro numero "))
    if x>maior:
        maior=x
    num-=1
print(maior)