larg=int(input("Digite a largura do terreno "))
comp=int(input("Digite o comprimento do terreno "))
preco=float(input("Qual o preço do metro quadrado? "))
area=larg*comp
custo=float(area*preco)
print("O terreno tem {} metros quadrados e custa R$ {}".format(area,custo))