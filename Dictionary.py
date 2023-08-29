# Aula sobre dicionário
# tabela = {"alface":0.45, "batata":1.2, "tomate": 2.3, "feijão": 1.5}
# while True:
#     produto = input("Digite o nome do produto ou fim para terminar:")
#     if produto =="fim":
#         break
#     if produto in tabela:
#         print(f"Preço: R$ {tabela[produto]:.2f}")
#     else:
#         print("Produto não encontrado.")
#
# print(tabela)


# carros = {"Jeep Renegade":['R$90.000,00', 'Ano 2018'], "Jeep Compass":'R$150.000,00', "Troller": 'R$200.000,00'}
# print(carros)
#
# print(carros["Jeep Renegade"])
#
# carros["Jeep Compass"] = 'R$180.000,00'
# print(carros)
#
# carros["Jeep Renegade"][1] = "2016"
# print(carros)
#
# del carros["Troller"]
# print(carros)
#
# carros["Audi"] = ['R$250.000,00' , "2023"]
# print(carros)
#
# print("Audi" in carros)
# print("BMW" in carros)
#
# print(carros.keys())
# print(carros.values())

#Aula de Dicionário com Lista embutida
#
# estoque = {"tomate": [1000, 2.3], "alface": [500, 0.45], "batata": [2001, 1.2], "feijão": [100, 1.5]}
#
# venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
#
# total = 0
#
# for operacao in venda:
#   produto, quantidade = operacao
#   preco = estoque[produto][1]
#   custo = preco * quantidade
#   print(f"{produto}: {quantidade} x {preco} = {custo}")
#   estoque[produto][0] -= quantidade
#   total += custo
#
#   print(f"Custo total: {total}")
#   for chave, dados in estoque.items():
#     print("Descrição: ", chave)
#     print("Quantidade: ", dados[0])
#     print(f"Preço: R$ {dados[1]}")

#NAC 1 do 2oSEM Comp_Thinking 20230821
# estoque = {'TIJOLO':[10.00, 10],
#            'PREGO':[20.35, 33],
#            'CIMENTO':[17.90, 25],
#            'VIGA':[42.50, 20]}
#
# while True:
#     print('''----Menu----
#
#     1- Incluir produto
#     2- Dar baixa no produto
#     3- Mostrar estoque
#     4- Sair
#     ''')
#     op = str(input('Escolha uma opção [1, 2, 3, 4]: ')).strip()[0]
#     if op == '1':
#         tipo = str(input('Tipo do produto:')).strip().upper()
#         if tipo in estoque:
#             print('Produto já existe no estoque!')
#             continue
#         preco = float(input('Preço do produto: R$'))
#         qtd = int(input('Quantidade do produto:'))
#         estoque[tipo] = [preco, qtd]
#     elif op == '2':
#         tipo = str(input('Tipo do produto:')).strip().upper()
#         if tipo not in estoque:
#             print('Produto não existe no estoque!')
#             continue
#         qtd = int(input('Quantidade do produto:'))
#         if qtd > estoque[tipo][1]:
#             print('Quantidade insuficiente no estoque!')
#             continue
#         estoque[tipo][1] -= qtd
#     elif op == '3':
#         for k, v in estoque.items():
#             print(f'''Tipo: {k.capitalize()} / Preço: R${v[0]:.2f} / Quantidade: {v[1]}\n{'-'*50}''')
#     elif op == '4':
#         break

#Aula 8 - Manipular Strings (20230828)

frase = "Hello world!"
# print(frase)
# print(len(frase))
# print(frase[0])
# print(frase[1])
# a = "Hello"
# b = "world"
# c = " "
# d = "!"
# print(a + c + b)
# print(a + " " + b + d * 3)
# print(a + " " + b + "!")
#
# print(frase[0:5])
# print(frase[6:])


# nome = "Michele"
# idade = 44
# altura = 1.58
#
# print("A %s tem %d anos e %.2f m de altura." % (nome, idade, altura))
#
# print("A {} tem {} anos e {} m de altura.".format(nome, idade, altura))
#
# print(f"A {nome} tem {idade} anos e {altura} m de altura.")


#frase = "Hello world!" #agora eu posso mudar uma letra maiscula por minuscula ou acrescentar coisas
#frase[11] = "!!!”

# frase_lista = list(frase)
# print(frase_lista)
# frase_lista[5] = " , "
# print(frase_lista)
#
# frase_inteira = " ".join(frase_lista)
# print(frase_inteira)

print(frase.startswith("Hello"))
print(frase.endswith("world!"))
print("d!" in frase)

print(frase.count("Hello"))
print(frase.count("o"))

print(frase.find("Hello"))
print(frase.find("mundo"))
print(frase.split())

titulo = "Hello world!"
print(titulo.split())
print(titulo.replace("world", "mundo"))

print('Hello', 'world')
print('Hello', 'world', sep=' ')
print('Hello', 'world', sep=',')
print('Hello', 'world')
print('Hello', 'world', end='\n')
rint('Hello', 'world', end='\n\n')
print('Hello', 'world', sep=',', end='!')
