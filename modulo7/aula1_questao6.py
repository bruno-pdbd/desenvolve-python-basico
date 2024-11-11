from collections import Counter
def encontrar_anagramas(frase, palavraobj):
    countobj=Counter(palavraobj)
    lenobj=len(palavraobj)
    anagram=[]
    for i in range(len(frase)-lenobj+1):
        substring=frase[i:i+lenobj]
        contagem_substring=Counter(substring)
        if contagem_substring==countobj:
            anagram.append(substring)
    return anagram
frase=input("Digite a frase: ")
palavraobj=input("Digite a palavra objetivo: ")
anagramas=encontrar_anagramas(frase, palavraobj)
if anagramas:
    print("Anagramas encontrados:", anagramas)
else:
    print("Nenhum anagrama encontrado.")