import re
arquivo_frase="frase.txt"
arquivo_palavras="palavras.txt"
with open(arquivo_frase, "r") as arquivo:
    frase=arquivo.read()
palavras=re.findall(r'[a-zA-Z]+',frase)
with open(arquivo_palavras, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra+"\n")
with open(arquivo_palavras, "r") as arquivo:
    conteudo=arquivo.read()
print("Conteúdo de 'palavras.txt':")
print(conteudo)