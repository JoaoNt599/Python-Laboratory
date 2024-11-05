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
        """ Recebe um objeto Contato, localiza-o no repositorio e atualiza seus dados"""
        if (contato == None):
            print("Um contato deve ser fornecido.")
        elif (indice == None):
            print("Um indice deve ser fornecido.")
        elif (indice < 0):
            print("O indice não deve ser negativo")
        else:
            self.__repositorio_contatos[indice] = contato
            resultado = contato
        return resultado


    def excluir_por_indice(self, indice: int) -> None:
        """ Recebe o indice do contato de repositorio e o remove """
        resultado = None
        if (indice == None):
            print("Um indice deve ser fornecido.")
        elif (indice < 0):
            print("O indice não deve ser negativo.")
        else:
            resultado = self.__repositorio_contatos.pop(indice)
        return resultado


    def consultar_indice_por_nome(self, nome: str) -> None:
        """ Recebe o nome do contato e retorna se existir no repositorio; se não, retorna  -1 """
        resultado = -1
        indice = -1
        for i in range(0, len(self.__repositorio_contatos)):
            contato = self.__repositorio_contatos[i]
            if contato.nome == nome:
                indice = i
        if indice != -1:
            resultado = indice
        return resultado


    def existe(self, contato: Contato) -> bool:
        """
        Recebe um objeto Contato e retorna True caso exista algum com mesmo telefone;
        Se não, retorna False
        """
        resultado = False
        for c in self.__repositorio_contatos:
            if c.fone == contato.fone:
                resultado = True
                break
        return resultado


    def vazio(self) -> bool:
        return (len(self.__repositorio_contatos) == 0)


class CadastroContatos:
    pass


class ContatosApp:
    pass


if __name__ == "__main__":
    pass