livros=[
    {"Título": "Assim Falou Zaratustra", "Autor": "Friedrich Nietzsche", "Ano de publicação": 1883, "Número de páginas": 368},
    {"Título": "O Mundo como Vontade e Representação", "Autor": "Arthur Schopenhauer", "Ano de publicação": 1818, "Número de páginas": 600},
    {"Título": "Meditações", "Autor": "Marco Aurélio", "Ano de publicação": 180, "Número de páginas": 256},
    {"Título": "A Arte de Viver", "Autor": "Sêneca", "Ano de publicação": 65, "Número de páginas": 160},
    {"Título": "O Anti-Édipo", "Autor": "Gilles Deleuze e Félix Guattari", "Ano de publicação": 1972, "Número de páginas": 288},
    {"Título": "Crítica da Razão Pura", "Autor": "Immanuel Kant", "Ano de publicação": 1781, "Número de páginas": 480},
    {"Título": "O Ser e o Nada", "Autor": "Jean-Paul Sartre", "Ano de publicação": 1943, "Número de páginas": 720},
    {"Título": "A República", "Autor": "Platão", "Ano de publicação": 380,"Número de páginas": 400},
    {"Título": "Sobre a Brevidade da Vida", "Autor": "Sêneca", "Ano de publicação": 49, "Número de páginas": 80},
    {"Título": "A Genealogia da Moral", "Autor": "Friedrich Nietzsche", "Ano de publicação": 1887, "Número de páginas": 160}
]
nome_arquivo="meus_livros.csv"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        linha="{},{},{},{}\n".format(livro["Título"], livro["Autor"], livro["Ano de publicação"], livro["Número de páginas"])
        arquivo.write(linha)
print("Arquivo '{}' criado com sucesso!".format(nome_arquivo))