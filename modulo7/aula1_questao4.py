celular=input("Digite o número do celular: ")
if len(celular)==8:
    celular="9"+celular
elif len(celular)==9:
    if celular[0]!='9':
        print("O primeiro dígito deve ser 9.")
        exit()
formatado=celular[:5]+"-"+celular[5:]
print("Número de celular formatado: {} ".format(formatado))