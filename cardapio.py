print('''
------- Cardápio Comidas -------

100 - Cachorro Quente - R$ 1.10
101 - Bauru Simples   - R$ 1.30
102 - Bauru c/ovo     - R$ 1.50
103 - Hamburguer      - R$ 1.10
104 - Cheeseburguer   - R$ 1.30
105 - Refrigerante    - R$ 1.00
''')

codigo = input("Digite o código do produto: ")

if (codigo == "100"):
    preco = 1.10
    nome = "Cachorro Quente"
elif(codigo == "101"):
    preco = 1.30
    nome = "Bauru Simples"
elif(codigo == "102"):
    preco = 1.50
    nome = "Bauru c/ovo"
elif(codigo == "103"):
    preco = 1.10
    nome = "Hamburguer"
elif(codigo == "104"):
    preco = 1.30
    nome = "Cheeseburguer"
elif(codigo == "105"):
    preco = 1.00
    nome = "Refrigerante"
else:
    print("Código inválido!")
    preco = 0
    nome = "Produto não encontrado"

if (preco != 0):    
    quantidade = int(input("Digite quantas unidades você deseja: "))
else:
    quantidade = 0

valorTotal = preco * quantidade

print(f"Seu pedido de {nome} com {quantidade} unidades, deu o total de: R$ {valorTotal:.2f}")
