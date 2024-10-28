num=[]
print("Digite 4 ou mais numeros inteiros (fim encerra): ")
while True:
    entrada=input()
    if entrada.lower()=="fim":
        if len(num)<4:
            print("Insira pelo menos 4 números.")
        else:
            break
    try:
        numero=int(entrada)
        num.append(numero)
    except ValueError:
        print("Número inválido.")
print("Lista original:",num)
print("Os 3 primeiros elementos:",num[:3])
print("Os 2 últimos elementos:",num[-2:])
print("Lista invertida:",num[::-1])
print("Elementos de índice par:",num[::2])
print("Elementos de índice ímpar:",num[1::2])