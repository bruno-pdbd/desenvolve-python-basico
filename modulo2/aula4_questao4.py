notas=int(input("Digite a quantidade de notas "))
notas100=notas//100
notas=notas%100
notas50=notas//50
notas=notas%50
notas20=notas//20
notas=notas%20
notas10=notas//10
notas=notas%10
notas5=notas//5
notas=notas%5
notas2=notas//2
notas=notas%2
notas1=notas//1
notas=notas%1
print("{} nota(s) de 100".format(notas100))
print("{} nota(s) de 50".format(notas50))
print("{} nota(s) de 20".format(notas20))
print("{} nota(s) de 10".format(notas10))
print("{} nota(s) de 5".format(notas5))
print("{} nota(s) de 2".format(notas2))
print("{} nota(s) de 1".format(notas1))