nota = int(input("Avalie o filme de 1 a 5: "))
if 1 <= nota <= 5:
    if nota == 1:
        print("Classificação: Ruim")
    elif nota == 2:
        print("Classificação: Regular")
    elif nota == 3:
        print("Classificação: Bom")
    elif nota == 4:
        print("Classificação: Muito bom ")
    elif nota == 5:
        print("Classificação: Excelente")
else:
    print("Avaliação inválida. Por favor, insira um número entre 1 e 5.")