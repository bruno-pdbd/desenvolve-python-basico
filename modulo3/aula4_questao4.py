distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))
if distancia <= 100:
    tarifa = 1.00
elif 101 <= distancia <= 300:
    tarifa = 1.50
else:
    tarifa = 2.00
valor = tarifa * peso
if peso > 10:
    valor += 10
print("Valor do frete: R${:.2f}".format(valor))