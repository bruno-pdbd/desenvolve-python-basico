import random
def encrypt(strings):
    chave=random.randint(1, 10)
    nomes_criptografados=[]
    for string in strings:
        criptografada=""
        for char in string:
            unicode=ord(char)
            novocod=(unicode+chave)
            if novocod>126:
                novocod=33+(novocod-127)
            criptografada+=chr(novocod)
        nomes_criptografados.append(criptografada)
    return nomes_criptografados,chave
nomes=["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)
print("Nomes criptografados:", nomes_criptografados)
print("Chave de criptografia:", chave)