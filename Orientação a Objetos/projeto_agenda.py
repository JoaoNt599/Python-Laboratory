""" Agenda Telefonica """


class Contato:
    def __init__(self, fone: str, nome: str) -> None:
        self.__fone = fone
        self.__nome = nome


    def __str__(self) -> str:
        resultado = f"\nNome: {self.__nome}"
        resultado += f"\nFone: {self.__fone}"
        return resultado


    @property
    def fone(self) -> str:
        return self.__fone


    @property
    def nome(self) -> str:
        return self.__nome


    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome


class RepositorioContatos:
    def __init__(self):
        self.__repositorio_contatos = []


    @property
    def repositorio_contatos(self) -> []:
        return self.__repositorio_contatos


    def incluir(self, contato: Contato) -> Contato:
        resultado = None
        if not contato == None:
            self.__repositorio_contatos.append(contato)
            resultado = contato
        else:
            print("Um contato deve ser fornecido.")
        return resultado


    def atulizar(self, indice: int, contato: Contato) -> None:
        pass


    def excluir_por_indice(self):
        pass


    def consultar_indice_por_nome(self):
        pass


    def existe(self):
        pass


    def vazio(self):
        pass


class CadastroContatos:
    pass


class ContatosApp:
    pass


if __name__ == "__main__":
    pass