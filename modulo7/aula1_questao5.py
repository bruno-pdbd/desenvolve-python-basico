frase=input("Digite uma frase: ")
vogal="aeiouAEIOU"
contagem_vogais=0
indices_vogais=[]
for i, letra in enumerate(frase):
    if letra in vogal:
        contagem_vogais += 1
        indices_vogais.append(i)
print("Número de vogais: {} ".format(contagem_vogais))
print("Índices das vogais: {} ".format(indices_vogais))