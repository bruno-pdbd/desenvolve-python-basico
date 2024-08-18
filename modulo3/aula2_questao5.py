genero=str(input("Digite seu gênero M ou F: "))
idade=int(input("Digite sua idade: "))
tempo=int(input("Digite seu tempo de serviço: "))
a=(genero=='m'and idade>=65) or (genero=='f'and idade>=60)
b=(tempo>30)
c=idade>=60 and tempo >=25
aposenta= a or b or c
print(aposenta)