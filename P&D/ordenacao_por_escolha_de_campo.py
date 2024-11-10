import csv

def obter_campos_csv(arquivo_csv):
    with open(arquivo_csv, 'r', newline='') as arquivo_entrada:
        leitor_csv = csv.reader(arquivo_entrada)
        campos = next(leitor_csv)  # Lê a primeira linha para obter os campos
    return campos


def quick_sort(dados, campo_para_ordenar):
    if len(dados) <= 1:
        return dados
    else:
        pivo = dados[0]
        menores = [item for item in dados[1:] if item[campo_para_ordenar] < pivo[campo_para_ordenar]]
        maiores = [item for item in dados[1:] if item[campo_para_ordenar] >= pivo[campo_para_ordenar]]
        return quick_sort(menores, campo_para_ordenar) + [pivo] + quick_sort(maiores, campo_para_ordenar)


def ordenar_csv_por_campo(arquivo_csv, campo_para_ordenar, arquivo_saida=None):
    with open(arquivo_csv, 'r', newline='') as arquivo_entrada:
        leitor_csv = csv.DictReader(arquivo_entrada)
        dados = list(leitor_csv)

        # Verificar se o campo para ordenar existe
        if campo_para_ordenar not in dados[0]:
            raise ValueError(f'O campo "{campo_para_ordenar}" não existe no arquivo CSV.')

        # Aplica o quick sort para ordenação
        dados_ordenados = quick_sort(dados, campo_para_ordenar)

    if arquivo_saida:
        with open(arquivo_saida, 'w', newline='') as arquivo_saida:
            escritor_csv = csv.DictWriter(arquivo_saida, fieldnames=dados[0].keys())
            escritor_csv.writeheader()
            escritor_csv.writerows(dados_ordenados)
            print(f"Arquivo CSV ordenado salvo em {arquivo_saida}")
    else:
        return dados_ordenados


if __name__ == "__main__":
    arquivo_csv = "dados.csv"
    campos = obter_campos_csv(arquivo_csv)

    print("Campos disponíveis para ordenação:", campos)
    campo_para_ordenar = input("Digite o campo pelo qual deseja ordenar os dados: ")

    # Planilha chamada "dados.csv" e deseja ordenar pelo campo especificado
    ordenar_csv_por_campo(arquivo_csv, campo_para_ordenar, arquivo_saida="dados_ordenados.csv")
