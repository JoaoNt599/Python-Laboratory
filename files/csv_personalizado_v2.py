import csv


def criar_csv():
    nome_arquivo = input("Informe o nome do arquivo CSV: ")

    # Usuário informa os campos e seus tipos
    campos_personalizados = []
    while True:
        nome_campo = input("Informe o nome do campo (ou digite 'fim' para encerrar): ")
        if nome_campo.lower() == 'fim':
            break
        tipo_campo = input("Informe o tipo do campo (texto ou numerico): ").lower()
        campos_personalizados.append((nome_campo, tipo_campo))

    # Formato adequado para o cabeçalho do CSV
    campos_para_cabecalho = [campo[0] for campo in campos_personalizados]

    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        # Escrevendo os campos no cabeçalho
        escritor_csv.writerow(campos_para_cabecalho)

        # Usuário informa os dados para cada campo
        while True:
            dados = []
            for campo in campos_para_cabecalho:
                valor = input(f"Informe o valor para o campo '{campo}': ")
                dados.append(valor)

            # Escrevendo os dados no arquivo CSV
            escritor_csv.writerow(dados)

            continuar = input("Deseja adicionar mais dados? (s/n): ").lower()
            if continuar != 's':
                break

    print(f"Arquivo CSV '{nome_arquivo}' criado com sucesso.")


if __name__ == "__main__":
    criar_csv()
