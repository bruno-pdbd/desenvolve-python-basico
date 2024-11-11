import random
def carregar_palavras(arquivo):
    with open(arquivo, 'r') as file:
        palavras=[linha.strip() for linha in file]
    return palavras
def carregar_estagios(arquivo):
    estagios=[]
    with open(arquivo,'r') as file:
        bloco=[]
        for linha in file:
            linha=linha.rstrip()
            if linha=='':
                if bloco:
                    estagios.append('\n'.join(bloco))
                    bloco=[]
            else:
                bloco.append(linha)
        if bloco:
            estagios.append('\n'.join(bloco))
    return estagios
def imprime_enforcado(numErros, estagios):
    print(estagios[numErros])
def jogo_forca():
    palavras=carregar_palavras('gabarito_forca.txt')
    estagios=carregar_estagios('gabarito_enforcado.txt')
    palavra=random.choice(palavras).upper()
    palavra_oculta=['_' for _ in palavra]
    erros=0
    letras_erradas=set()
    print("Bem-vindo ao jogo da Forca!")
    while erros<6 and '_' in palavra_oculta:
        print(' '.join(palavra_oculta))
        print("Letras erradas: {}".format(','.join(letras_erradas)))
        imprime_enforcado(erros,estagios)
        tentativa=input("Digite uma letra: ").upper()
        if len(tentativa) !=1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue
        if tentativa in palavra:
            for idx, letra in enumerate(palavra):
                if letra==tentativa:
                    palavra_oculta[idx] = tentativa
        else:
            if tentativa not in letras_erradas:
                letras_erradas.add(tentativa)
                erros+=1
    if '_' not in palavra_oculta:
        print("Parabéns! Você adivinhou a palavra: {}".format(palavra))
    else:
        imprime_enforcado(erros, estagios)
        print("Game over! A palavra era: {}".format())
jogo_forca()