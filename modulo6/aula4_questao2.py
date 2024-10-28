vogal="aeiouAEIOU"
frase=input("Digite uma frase: ")
vogais=sorted([char for char in frase if char in vogal])
consoantes=[char for char in frase if char.isalpha() and char not in vogal]
print(vogais)
print(consoantes)