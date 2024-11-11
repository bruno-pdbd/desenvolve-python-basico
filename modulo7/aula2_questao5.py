import random
def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra)<=3:
            return palavra
        primeira_letra=palavra[0]
        ultima_letra=palavra[-1]
        letras_internas=list(palavra[1:-1])
        random.shuffle(letras_internas)
        return primeira_letra+''.join(letras_internas) + ultima_letra
    palavras = frase.split()
    palavras_embaralhadas=[embaralhar_palavra(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)
frase = input("Digite uma frase: ")
frase_embaralhada = embaralhar_palavras(frase)
print("Hipotese de Matt Davis:", frase_embaralhada)