idade=int(input("Digite sua idade :"))
jogos=bool((input("Você já jogou pelo menos 3 jogos de tabulerio? True or False :")))
vitoria=bool((input("Quantas vezes venceu um jogo? :")))

entrar=(16 <= idade <=18 and jogos and vitoria >=1)
print(entrar) 