import csv
def adicionar_usuario():
    id_usuario = input("ID do usuário: ")
    nome = input("Nome do usuário: ")
    email = input("Email do usuário: ")
    senha = input("Senha do usuário: ")
    categoria = input("Categoria (Administrador, Gerente, Vendedor, Cliente): ")
    with open('usuarios.csv', 'a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([id_usuario, nome, email, senha, categoria])
    print("Usuário adicionado com sucesso!")
def listar_usuarios():
    try:
        with open('usuarios.csv', 'r') as arquivo:
            reader = csv.reader(arquivo)
            print("Lista de Usuários:")
            for usuario in reader:
                print(usuario)
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
def editar_usuario():
    id_usuario = input("Digite o ID do usuário que deseja editar: ")
    usuarios = []
    try:
        with open('usuarios.csv', 'r') as arquivo:
            reader = csv.reader(arquivo)
            usuarios = list(reader)
        for i, usuario in enumerate(usuarios):
            if usuario[0] == id_usuario:
                print(f"Usuário encontrado: {usuario}")
                nome = input("Novo nome (deixe em branco para não alterar): ") or usuario[1]
                email = input("Novo email (deixe em branco para não alterar): ") or usuario[2]
                senha = input("Nova senha (deixe em branco para não alterar): ") or usuario[3]
                categoria = input("Nova categoria (deixe em branco para não alterar): ") or usuario[4]
                
                usuarios[i] = [id_usuario, nome, email, senha, categoria]
                break
        else:
            print("Usuário não encontrado.")      
        with open('usuarios.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(usuarios)
        print("Usuário atualizado com sucesso!")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
def excluir_usuario():
    id_usuario = input("Digite o ID do usuário que deseja excluir: ")
    usuarios = []  
    try:
        with open('usuarios.csv', 'r') as arquivo:
            reader = csv.reader(arquivo)
            usuarios = list(reader)     
        usuarios = [usuario for usuario in usuarios if usuario[0] != id_usuario]     
        with open('usuarios.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(usuarios)
        print("Usuário excluído com sucesso!")
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
def adicionar_produto():
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade disponível: "))
    with open('produtos.csv', 'a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([codigo, nome, descricao, preco, quantidade])
    print("Produto adicionado com sucesso!")
def listar_produtos():
    try:
        with open('produtos.csv', 'r') as arquivo:
            reader = csv.reader(arquivo)
            print("Lista de Produtos:")
            for produto in reader:
                print(produto)
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
def editar_produto():
    codigo_produto = input("Digite o código do produto que deseja editar: ")
    produtos = []
    try:
        with open('produtos.csv', 'r') as arquivo:
            reader = csv.reader(arquivo)
            produtos = list(reader)      
        for i, produto in enumerate(produtos):
            if produto[0] == codigo_produto:
                print(f"Produto encontrado: {produto}")
                nome = input("Novo nome (deixe em branco para não alterar): ") or produto[1]
                descricao = input("Nova descrição (deixe em branco para não alterar): ") or produto[2]
                preco = input("Novo preço (deixe em branco para não alterar): ") or produto[3]
                quantidade = input("Nova quantidade (deixe em branco para não alterar): ") or produto[4]
                produtos[i] = [codigo_produto, nome, descricao, preco, quantidade]
                break
        else:
            print("Produto não encontrado.")
        with open('produtos.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(produtos)
        print("Produto atualizado com sucesso!")
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
def excluir_produto():
    codigo_produto = input("Digite o código do produto que deseja excluir: ")
    produtos = []  
    try:
        with open('produtos.csv', 'r') as arquivo:
            reader = csv.reader(arquivo)
            produtos = list(reader)      
        produtos = [produto for produto in produtos if produto[0] != codigo_produto]       
        with open('produtos.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(produtos)
        print("Produto excluído com sucesso!")
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
def listar_produtos_ordenados_nome():
    try:
        with open('produtos.csv', 'r') as arquivo:
            produtos = list(csv.reader(arquivo))
        produtos.sort(key=lambda x: x[1])  # Ordena pelo nome
        for produto in produtos:
            print(produto)
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
def listar_produtos_ordenados_preco():
    try:
        with open('produtos.csv', 'r') as arquivo:
            produtos = list(csv.reader(arquivo))
        produtos.sort(key=lambda x: float(x[3]))  # Ordena pelo preço
        for produto in produtos:
            print(produto)
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
def buscar_produto():
    termo = input("Digite o código ou nome do produto para buscar: ")
    try:
        with open('produtos.csv', 'r') as arquivo:
            produtos = list(csv.reader(arquivo))
            encontrados = [produto for produto in produtos if termo.lower() in produto[1].lower() or termo in produto[0]]
            if encontrados:
                for produto in encontrados:
                    print(produto)
            else:
                print("Produto não encontrado.")
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Adicionar Usuário")
        print("2. Listar Usuários")
        print("3. Editar Usuário")
        print("4. Excluir Usuário")
        print("5. Adicionar Produto")
        print("6. Listar Produtos")
        print("7. Editar Produto")
        print("8. Excluir Produto")
        print("9. Buscar Produto")
        print("10. Listar Produtos Ordenados por Nome")
        print("11. Listar Produtos Ordenados por Preço")
        print("12. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_usuario()
        elif escolha == '2':
            listar_usuarios()
        elif escolha == '3':
            editar_usuario()
        elif escolha == '4':
            excluir_usuario()
        elif escolha == '5':
            adicionar_produto()
        elif escolha == '6':
            listar_produtos()
        elif escolha == '7':
            editar_produto()
        elif escolha == '8':
            excluir_produto()
        elif escolha == '9':
            buscar_produto()
        elif escolha == '10':
            listar_produtos_ordenados_nome()
        elif escolha == '11':
            listar_produtos_ordenados_preco()
        elif escolha == '12':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")
if __name__ == "__main__":
    menu()