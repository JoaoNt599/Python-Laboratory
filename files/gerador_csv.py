import csv

def gerador_csv(dados, nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        campos = list(dados[0].keys())
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)

        # Escrevendo o cabeçalho
        escritor_csv.writeheader()

        # Escrevendo os dados
        escritor_csv.writerows(dados)

    print(f"Arquivo CSV '{nome_arquivo}' criado com sucesso.")

# Exemplo de uso:
dados_exemplo = [
    {'Nome': 'Mateus', 'Idade': 23, 'Cidade': 'Campos'},
    {'Nome': 'Vander', 'Idade': 78, 'Cidade': 'Acre'},
    {'Nome': 'Anna', 'Idade': 21, 'Cidade': 'Duque de Caxias'},
    {'Nome': 'Joao', 'Idade': 26, 'Cidade': 'Niteroi' },
    {'Nome': 'Nathany', 'Idade': 21, 'Cidade': 'Sao Paulo'}
]


if __name__ == "__main__":
    nome_arquivo_exemplo = 'teste2.csv'
    gerador_csv(dados_exemplo, nome_arquivo_exemplo)
