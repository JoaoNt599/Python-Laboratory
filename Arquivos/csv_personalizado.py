import csv


def criar_csv(nome_arquivo, campos):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        # Campos no cabeçalho
        escritor_csv.writerow(campos)

        # Usuário informa os dados para cada campo
        while True:
            dados = []
            for campo in campos:
                valor = input(f"Informe o valor para o campo '{campo}: ")
                dados.append(valor)

            # Escrevendo os dados no arquivo csv
            escritor_csv.writerow(dados)

            continuar = input("Deseja adicionar mais dados? (s/n): ").lower()
            if continuar != 's':
                break

        print(f"Arquivo CSV '{nome_arquivo}' criado com sucesso.")

# Exemplo para uso:
nome_arquivo = 'dados_personalizados.csv'


# Usuário informa os campos e seus tipos
campos_personalizados = []
while True:
    nome_campo = input("Informe o nome do campo (ou digite 'fim' para encerrar): ")
    if nome_campo.lower() == 'fim':
        break
    tipo_campo = input("Informe o tipo do campo (texto ou numerico): ").lower()
    campos_personalizados.append((nome_campo, tipo_campo))

# Conversão para o formato adequado para cabeçalho CSV
campos_para_cabecalho = [campo[0] for campo in campos_personalizados]

# Gerando o arquivo CSV com os campos informados
criar_csv(nome_arquivo, campos_para_cabecalho)


if __name__ == "__main__":
    criar_csv('dados_csv_custom.csv', 'nome')
