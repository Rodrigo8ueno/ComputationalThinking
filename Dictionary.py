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

estoque = {"tomate": [1000, 2.3], "alface": [500, 0.45], "batata": [2001, 1.2], "feijão": [100, 1.5]}

venda = [["tomate", 5], ["batata", 10], ["alface", 5]]

total = 0

for operacao in venda:
  produto, quantidade = operacao
  preco = estoque[produto][1]
  custo = preco * quantidade
  print(f"{produto}: {quantidade} x {preco} = {custo}")
  estoque[produto][0] -= quantidade
  total += custo

  print(f"Custo total: {total}")
  for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: R$ {dados[1]}")
