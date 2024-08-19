num1=int(input("Digite uma nota :"))
num2=int(input("Digite outra nota :"))
num3=int(input("Digite uma outra nota :"))
m=(num1+num2+num3)/3
if m>=60:
    print("Aprovado")
elif m>=40:
    print("Recuperação")
else:
    print("Reprovado")
print("Fim")
print("{:.2f}".format(m))