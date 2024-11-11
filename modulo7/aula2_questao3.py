import string
def palin(frase):
    frase_limpa=''.join(c.lower() for c in frase if c.isalnum())
    return frase_limpa==frase_limpa[::-1]
while True:
    frase=input("Digite uma frase (ou 'Fim' para encerrar): ")
    if frase.lower()=="fim":
        break
    if palin(frase):
        print("{} é um palíndromo.".format(frase))
    else:
        print("{} não é um palíndromo.".format(frase))