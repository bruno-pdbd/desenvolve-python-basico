classe = input("Escolha a classe do personagem (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite seus pontos de força: "))
magia = int(input("Digite seus pontos de magia: "))
validar = {
    "guerreiro": forca > 16 and magia < 11,
    "mago": forca < 11 and magia > 16,
    "arqueiro": 5 < forca < 16 and 5 < magia < 16
}
valido = validar.get(classe, False)
print(valido)