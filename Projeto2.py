from time import sleep

lista = [{'nome': 'Geladeira', 'preço': 999.90}, {'nome': 'Notbook Dell', 'preço': 2499.90},
         {'nome': 'Microondas X', 'preço': 299.29}, {'nome': 'Notbook Asus', 'preço': 3999.90},
         {'nome': 'Iphone 8', 'preço': 2199.12}, {'nome': 'Ventilador Gelado', 'preço': 199.90},
         {'nome': 'Freezer', 'preço': 849.00}, {'nome': 'Tv 55', 'preço': 4346.99},
         {'nome': 'Tv 50', 'preço': 3999.90}, {'nome': 'Tv 42', 'preço': 2999.90},
         {'nome': 'Notbook Lenovo', 'preço': 1999.90}, {'nome': 'Microondas Y', 'preço': 429.90},
         {'nome': 'Microodas Z', 'preço': 429.90}, {'nome': 'Geladeira faz frio', 'preço': 1199.98}]

carrinho = []
soma = 0
login_loja = 'Funcionário01'
senha_loja = 123456

# Menu para o usuário entrar como funcionário ou cliente

print("=-"*5,"BEM VINDO","=-"*5)
acesso = input("Cliente [A] Funcionário [B]\n").upper()

# Entrando como cliente

# Produtos em estoque com seus respectivos códigos
if acesso == 'A':
    sleep(1)
    print("=-=-=-Produtos em estoque=-=-=-=")
    print()
    sleep(2)
    codigo = 1
    for e in lista:
        print(f"Código do produto {codigo}")
        for k, v in e.items():
            print(f"{k}:  {v}")
        codigo += 1
        print("-"*30)
        sleep(1)

# Adicionando os produtos no carrinho

    adicionar_carrinho = int(input("Qual item deseja adicionar ao carrinho?\n"))
    while True:
        sleep(1)
        print("Adicionando", end='')
        sleep(1)
        print(".", end=''), sleep(1)
        print(".", end=''), sleep(1)
        print(".", end=''), sleep(1)
        print()
        sleep(1)
        print()
        print("=-=" * 15)
        print(" "*9, "Adicionado com sucesso!!")
        print("=-=" * 15)
        print()
        h = 0
        if adicionar_carrinho <= len(lista):
            j = adicionar_carrinho - 1
            carrinho.append(lista[j]['nome'])
            soma += lista[j]['preço']
        while True:
            continuar = input("Deseja adicionar mais produtos? [S/N]")
            print()
            if continuar in 'Nn':
                break
            if continuar in 'Ss':
                adicionar_carrinho = int(input("Qual produto deseja adicionar?\n"))
                j = adicionar_carrinho - 1
                if lista[j]['nome'] not in carrinho:
                    break
                else:
                    carrinho.append(lista[j]['nome'])
                    print("*"*40)
                    print("** Item selecionado ja foi adicionado **")
                    print("*"*40)
                    print()
                    h = input("Deseja remove-lo do carrinho? [S/N]")
                    if h in 'Ss':
                        carrinho.remove(lista[j]['nome'])
                    if h in 'Nn':
                        carrinho.remove(lista[j]['nome'])
                        break
        if continuar in 'Nn':
            break

# Mostra os produtos no carrinho

    print(" "*10, ">SEU CARRINHO<")
    print()
    for itens in carrinho:
        print(f"- {itens}")
    print('=-='*12)
    print(f"Valor total: R$ {soma:.2f}")
    compra = input("Deseja realizar a compra? [S/N]")
    print()
    if compra in 'Ss':
        sleep(1)
        print("Compra realizada com seuceso!!")
    elif compra in 'Nn':
        sleep(1)
        print("Compra recusada!!")

# Fim

# Entrando como funcionário

# Login e Senha que os funcionários vão possuir
# (Login: 'Funcionário01') ; (Senha: '123456')
elif acesso == 'B':
    print("~~FUNCIONÁRIOS~~")
    sleep(1)
    while True:
        login = input("login: ").title().strip(" ")
        sleep(1)
        senha = int(input("Senha: "))

# Adicionando produtos ao estoque

        if login == login_loja:
            print(">Adicionar ao estoque<")
            while True:
                produto_novo = {}
                produto_novo['nome'] = input("Nome: ")
                produto_novo['preço'] = input("Preço: ")
                lista.append(produto_novo.copy())
                produto_novo.clear()
                continuar_inserindo_produtos = input("Deseja continuar inserindo produtos? [S/N]")
                if continuar_inserindo_produtos in 'Ss':
                    continue
                if continuar_inserindo_produtos in 'Nn':
                    break
            if continuar_inserindo_produtos in 'Nn':
                break
        else:
            print(" "*5, "***ERRO***")
            print("Login ou Senha incorretos")
# Fim






