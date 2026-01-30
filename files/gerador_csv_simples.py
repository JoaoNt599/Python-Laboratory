import csv

# Exemplo para dados
dados = [
    {'Nome': 'Mateus', 'Idade': 23, 'Cidade': 'Campos'},
    {'Nome': 'Vander', 'Idade': 78, 'Cidade': 'Acre'},
    {'Nome': 'Anna', 'Idade': 21, 'Cidade': 'Duque de Caxias'},
    {'Nome': 'Joao', 'Idade': 26, 'Cidade': 'Niteroi' },
    {'Nome': 'Nathany', 'Idade': 21, 'Cidade': 'Sao Paulo'}
]

# Nome do arquivo csv
nome_arquivo = 'teste.csv'


# Escrevendo os dados no arquivo CSV
with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    campos = ['Nome', 'Idade', 'Cidade']
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)


    # Escrevendo o cabeçalho
    escritor_csv.writeheader()

    # Escrevendo os dados
    escritor_csv.writerows(dados)


print(f"Arquivo CSV: '{nome_arquivo} criado com sucesso.'")