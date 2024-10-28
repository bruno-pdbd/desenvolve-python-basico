emojis = {
    ":smile:": "😀",
    ":laugh:": "😂",
    ":heart:": "❤️",
    ":like:": "👍",
    ":party:": "🎉",
}
print("Emojis:")
for cod, emoji in emojis.items():
    print(f"{emoji} : {cod}")
codificado = input("Digite sua frase codificada (use os códigos de emojis): ")
emojizado = codificado
for cod, emoji in emojis.items():
    emojizado = emojizado.replace(cod, emoji)
print("Frase emojizada:", emojizado)