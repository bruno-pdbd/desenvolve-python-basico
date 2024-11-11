import os
frase=input("Digite uma frase: ")
nome="frase.txt"
with open(nome,"w") as arquivo:
    arquivo.write(frase)
caminho=os.path.abspath(nome)
print("Frase salva em {}".format(caminho))