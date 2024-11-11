frase=input("Digite uma frase: ")
vogal="aeiouAEIOU"
frase_mod=''.join('*' if letra in vogal else letra for letra in frase)
print(frase_mod)