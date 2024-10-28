import random
num = random.randint(1, 10)
print("Tente adivinhar o número entre 1 e 10!")
while True:
    palpite = int(input("Digite seu palpite: "))
    if palpite < num:
        print("Muito baixo! Tente novamente.")
    elif palpite > num:
        print("Muito alto! Tente novamente.")
    else:
        print("Você acertou!")
        break