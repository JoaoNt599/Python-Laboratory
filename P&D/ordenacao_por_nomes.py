""" Biblioteca para suporte em análise de dados  """

import csv


def quick_sort(dados, coluna_para_ordenar):
    if len(dados) <= 1:
        return dados
    else:
        pivo = dados[0]
        menores = [item for item in dados[1:] if item[coluna_para_ordenar] < pivo[coluna_para_ordenar]]
        maiores = [item for item in dados[1:] if item[coluna_para_ordenar] >= pivo[coluna_para_ordenar]]
        return quick_sort(menores, coluna_para_ordenar) + [pivo] + quick_sort(maiores, coluna_para_ordenar)


def ordernar_planilha(planilha_path, coluna_para_ordenar, planilha_saida_path=None):
    with open(planilha_path, 'r', newline='') as arquivo_entrada:
        leitor_csv = csv.DictReader(arquivo_entrada)

        # Lendo dados da planilha
        dados = list(leitor_csv)

        # Aplicando ordenação
        dados_ordenados = quick_sort(dados, coluna_para_ordenar)

    if planilha_saida_path:
        with open(planilha_saida_path, 'w', newline='') as arquivo_saida:
            # Escreve os dados ordenados em uma nova planilha
            campos = leitor_csv.fieldnames
            escritor_csv = csv.DictWriter(arquivo_saida, fieldnames=campos)
            escritor_csv.writeheader()
            escritor_csv.writerows(dados_ordenados)
            print(f"Planilha organizada salva em: {planilha_saida_path}")
    else:
        return dados_ordenados


if __name__ == "__main__":
    planilha_ordenada = ordernar_planilha("teste2.csv", coluna_para_ordenar="Nome")

    ordernar_planilha("teste2.csv", coluna_para_ordenar="Nome", planilha_saida_path="dados_ordenado_por_nomes.csv")


