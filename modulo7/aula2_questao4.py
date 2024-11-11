import string
def validador_senha(senha):
    if len(senha)<8:
        return False
    if not any(char.isupper() for char in senha):
        return False
    if not any(char.islower() for char in senha):
        return False
    if not any(char.isdigit() for char in senha):
        return False
    if not any(char in string.punctuation for char in senha):
        return False
    return True
senha=input("Digite uma senha para verificar: ")
if validador_senha(senha):
    print("A senha é válida.")
else:
    print("A senha não atende aos critérios.")