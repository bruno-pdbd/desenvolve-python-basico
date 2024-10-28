aluno=["Maria", "Jose", "Carla", "Sol"]
nota=[35, 50, 20, 80]
aprov=[aluno[i] for i in range(len(nota)) if nota[i] >= 60]
print("aprovados: {}".format(aprov))