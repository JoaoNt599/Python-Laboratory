"""
Uma loja necessita de um programa que facilite o cálculo de venda de seus produtos.
As áreas dos produtos são definidas como: 1) Informática; 2) Jogos; 3) Eletrônicos.
Os produtos de Informáticatêm 5% de desconto na compra, os jogos têm 8% e os produtos eletrônicos, 10%.
O Programa terá que receber via teclado o nome do produto, a área do produto (1, 2 ou 3), a quantidade comprada
e o valor unitário.
Deverá ser calculado o valor base (quantidade * unitário), o valor do desconto de acordo com o percentual de cada
área e o valor total com o desconto.

Baseando-se nos conceitos de vetores, remodele o programa da atividade 1 criando as variáveis:

nome_prod: Vetor tipo caractere de 100 posições;
quantidade: Vetor tipo float de 100 posições;
valor_unitario: Vetor tipo float de 100 posições.
percentual: Vetor tipo float de 100 posições;

Sobre a execução do programa:

O programa deverá cadastrar os itens de venda como linhas dos vetores:
nome_prod, quantidade, valor_unitario e percentual.

A cada item cadastrado, o programa deverá emitir uma mensagem perguntando se o usuário deseja continuar.
Como resposta a esta pergunta, o usuário digitará a letra ‘s’ para continuar cadastrando itens ou a letra ‘n’
para listar o relatório final.
Ao digitar a letra ‘n’, o programa deverá terminar o cadastro e emitir um relatório dos itens de venda na tela contendo:
nome do produto, quantidade, valor unitário, percentual de desconto, valor base, valor do desconto e valor final.
Ao listar todos os itens de venda, o programa deverá apresentar o valor total da venda.
"""


nome_prod = [""] * 100
quantidade = [0.0] * 100
valor_unitario = [0.0] * 100
percentual = [0.0] * 100

# Índice que controla as posições de cada protudo no vetor
index = 0
continuar = 's'


while continuar.lower() == 's' and index < 100:
    nome_prod[index] = input("Informe o nome do produto: ")
    print("Área do produto: 1) Informática, 2) Jogos, 3) Eletrônicos")
    area = int(input("Informe o número da área do produto (1, 2 ou 3): "))

    if area == 1:
        percentual[index] = 5.0
    elif area == 2:
        percentual[index] = 8.0
    elif area == 3:
        percentual[index] = 10.0
    else:
        print("Área inválida! Escolha entre 1, 2 ou 3.")
        continue


    # Coletando quantidade e valor unitário
    quantidade[index] = float(input("Informe a quantidade a ser comprada: "))
    valor_unitario[index] = float(input("Informe o valor uitário do produto: "))

    continuar = input("Deseja cadastrar mais itens? (s/n):")
    index += 1


print("\nRELATÓRIO FINAL DE VENDA")
print("Nome do Produto | Quantidade | Valor Unitário | % Desconto | Valor Base | Valor Desconto | Valor Final")
valor_total_venda = 0.0


for i in range(index):
    valor_base = quantidade[i] * valor_unitario[i]
    valor_desconto = valor_base * (percentual[i] / 100)
    valor_final = valor_base - valor_desconto
    valor_total_venda += valor_final

    print(f"{nome_prod[i]:<15} | {quantidade[i]:<10} | {valor_unitario[i]:<14.2f} | {percentual[i]:<9}% | {valor_base:<10.2f} | {valor_desconto:<12.2f} | {valor_final:<10.2f}")

print("\nValor total da venda: ", f"{valor_total_venda:.2f}")






























